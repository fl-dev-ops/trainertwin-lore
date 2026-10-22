"""The single media-transcription path: temporary audio/video -> AssemblyAI -> speaker turns.

Gemini is used separately for image OCR, never for transcription. Existing corpus
transcripts are preserved; new jobs use Universal-3.5 Pro with metadata context.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlparse

import httpx
import yaml
from dotenv import load_dotenv

from .board import ParallelJobBoard, active_job
from .fs import atomic_write
from .progress import stage, status, track

MODEL = "universal-3-5-pro"
API_BASE = "https://api.assemblyai.com"
CACHE_DIR = "assemblyai-json"
POLL_TIMEOUT = 3600


def get_api_key(api_key: str | None = None) -> str:
    load_dotenv(Path(__file__).resolve().parents[1] / ".env")
    key = (api_key or os.getenv("ASSEMBLYAI_API_KEY") or "").strip()
    if not key:
        raise ValueError("ASSEMBLYAI_API_KEY is required for audio transcription")
    return key


def validate_transcript(data: dict) -> dict:
    """Validate the shared cache/export contract; speaker counts come from IDs."""
    if (not isinstance(data, dict) or not {"speakers", "turns"} <= data.keys()
            or data.keys() - {"speakers", "turns", "model", "speaker_count"}
            or data.get("model", MODEL) != MODEL):
        raise ValueError("Invalid AssemblyAI transcript object/model")
    if not isinstance(data["speakers"], list) or not isinstance(data["turns"], list):
        raise TypeError("Transcript speakers and turns must be arrays")
    speakers, ids = [], set()
    for row in data["speakers"]:
        if (not isinstance(row, dict) or set(row) != {"id", "label"}
                or not isinstance(row["id"], str) or not re.fullmatch(r"[1-9]\d*", row["id"])
                or row["id"] in ids or not isinstance(row["label"], str) or not row["label"].strip()):
            raise ValueError("Invalid or duplicate speaker")
        ids.add(row["id"])
        speakers.append({"id": row["id"], "label": " ".join(row["label"].split())})
    turns, used = [], set()
    for row in data["turns"]:
        if (not isinstance(row, dict) or set(row) != {"speaker_id", "text"}
                or not isinstance(row["speaker_id"], str) or row["speaker_id"] not in ids
                or not isinstance(row["text"], str) or not row["text"].strip()):
            raise ValueError("Invalid turn or unknown speaker ID")
        used.add(row["speaker_id"])
        turns.append({"speaker_id": row["speaker_id"], "text": row["text"].strip()})
    if ids and not used:
        raise ValueError("Listed speakers but no spoken turns")
    speakers = [s for s in speakers if s["id"] in used]
    count = len(used)
    if "speaker_count" in data and (type(data["speaker_count"]) is not int or data["speaker_count"] != count):
        raise ValueError("Cached speaker_count does not match speaker IDs")
    return {"model": MODEL, "speaker_count": count, "speakers": speakers, "turns": turns}


def _assembly_transcript(data: dict) -> dict:
    """Do not silently label a fallback model or missing diarization as a success."""
    if data.get("status") != "completed" or data.get("speech_model_used") != MODEL:
        raise ValueError("AssemblyAI did not complete with the requested model")
    text, words, utterances = data.get("text"), data.get("words"), data.get("utterances")
    if text is None and words == [] and utterances == []:
        text = ""  # Provider's explicit no-speech result.
    if not isinstance(text, str) or not isinstance(words, list) or not isinstance(utterances, list):
        raise ValueError("Malformed AssemblyAI transcript/diarization")
    if not text.strip():
        if words or utterances:
            raise ValueError("Empty AssemblyAI text alongside spoken words")
        return validate_transcript({"speakers": [], "turns": []})
    if not words or not utterances:
        raise ValueError("AssemblyAI returned text without words or speaker turns")
    speakers, turns, ids = [], [], {}
    previous_end = 0
    for row in utterances:
        speaker = row.get("speaker") if isinstance(row, dict) else None
        if (not isinstance(speaker, str) or not speaker.strip()
                or not isinstance(row.get("text"), str) or not row["text"].strip()
                or type(row.get("start")) not in (int, float) or type(row.get("end")) not in (int, float)
                or not 0 <= row["start"] <= row["end"] or row["end"] < previous_end):
            raise ValueError("Invalid AssemblyAI speaker turn")
        previous_end = row["end"]
        if speaker not in ids:
            ident = str(len(ids) + 1)
            ids[speaker] = ident
            speakers.append({"id": ident, "label": f"Speaker {ident}"})
        turns.append({"speaker_id": ids[speaker], "text": row["text"]})
    # Diarized export must contain all recognized text, not a partial utterance list.
    tokens = lambda s: re.findall(r"\w+", s.casefold())
    if tokens(text) != tokens(" ".join(t["text"] for t in turns)):
        raise ValueError("AssemblyAI speaker turns do not cover the transcript text")
    return validate_transcript({"speakers": speakers, "turns": turns})


def _request(client: httpx.Client, method: str, path: str, **kwargs) -> dict:
    # Never retry a paid POST automatically: an ambiguous timeout may already have submitted it.
    for attempt in range(4):
        response = client.request(method, path, **kwargs)
        if method == "GET" and response.status_code in {429, 500, 502, 503, 504} and attempt < 3:
            time.sleep(2 ** attempt)
            continue
        if response.is_error:
            # Provider errors can contain URLs/content; do not print response bodies or keys.
            raise RuntimeError(f"AssemblyAI HTTP {response.status_code} during {method} {path}")
        data = response.json()
        if not isinstance(data, dict):
            raise TypeError("Malformed AssemblyAI response")
        return data
    raise AssertionError("unreachable")


def transcribe_audio(audio: Path, context: str = "", api_key: str | None = None,
                     *, cache_path: Path | None = None) -> dict:
    """Transcribe a local audio/video file. The caller's original file is never deleted.

    A cache path also enables durable job-ID checkpoints: interrupted polling resumes
    without submitting a second paid job. Temporary downloads belong to their caller.
    """
    if cache_path and cache_path.exists():
        return validate_transcript(json.loads(cache_path.read_text(encoding="utf-8")))
    if not audio.is_file() or audio.stat().st_size == 0:
        raise ValueError(f"Missing or empty audio: {audio}")
    if audio.stat().st_size > 2_200_000_000:
        raise ValueError("AssemblyAI upload exceeds 2.2 GB; split the recording first")
    key = get_api_key(api_key)
    config = {"speech_models": [MODEL], "speaker_labels": True, "language_detection": True}
    if context.strip():
        config["prompt"] = context.strip()[:1500]
    job_path = cache_path.with_suffix(".job.json") if cache_path else None
    ident = None
    with httpx.Client(base_url=API_BASE, headers={"authorization": key}, timeout=180) as client:
        if job_path and job_path.exists():
            job = json.loads(job_path.read_text(encoding="utf-8"))
            if job.get("config") != config or not re.fullmatch(r"[A-Za-z0-9-]+", str(job.get("id", ""))):
                raise ValueError("Saved AssemblyAI job has different settings or an invalid ID")
            with audio.open("rb") as handle:
                digest = hashlib.file_digest(handle, "sha256").hexdigest()
            if job.get("sha256") != digest:
                raise ValueError("Saved AssemblyAI job does not match this media file")
            ident = job["id"]
            status("AssemblyAI: resuming transcription job")
        else:
            status("AssemblyAI: uploading temporary audio")
            with audio.open("rb") as handle:
                uploaded = _request(client, "POST", "/v2/upload", content=handle,
                                    headers={"content-type": "application/octet-stream"})
            url = uploaded.get("upload_url")
            if not isinstance(url, str) or urlparse(url).scheme != "https":
                raise ValueError("AssemblyAI upload returned no HTTPS media URL")
            job = _request(client, "POST", "/v2/transcript", json={**config, "audio_url": url})
            ident = job.get("id")
            if not isinstance(ident, str) or not re.fullmatch(r"[A-Za-z0-9-]+", ident):
                raise ValueError("AssemblyAI returned an invalid transcript ID")
            if job_path:
                with audio.open("rb") as handle:
                    digest = hashlib.file_digest(handle, "sha256").hexdigest()
                atomic_write(job_path, json.dumps({"id": ident, "config": config, "sha256": digest}))
        status("AssemblyAI: transcribing audio (percentage unavailable)")
        deadline = time.monotonic() + POLL_TIMEOUT
        while True:
            data = _request(client, "GET", f"/v2/transcript/{ident}")
            if data.get("status") == "error":
                raise RuntimeError("AssemblyAI transcription failed; inspect the saved job ID before retrying")
            if data.get("status") == "completed":
                result = _assembly_transcript(data)
                break
            if data.get("status") not in {"queued", "processing"}:
                raise ValueError("Unexpected AssemblyAI job status")
            if time.monotonic() >= deadline:
                raise TimeoutError("AssemblyAI polling timed out; saved jobs can be resumed")
            time.sleep(3)
        if cache_path:
            atomic_write(cache_path, json.dumps(result, ensure_ascii=False, indent=2) + "\n")
        try:
            _request(client, "DELETE", f"/v2/transcript/{ident}")
        except Exception:  # noqa: BLE001 - cleanup must not discard a validated, cached transcript.
            status(f"Warning: could not delete AssemblyAI transcript {ident}")
        if job_path:
            job_path.unlink(missing_ok=True)
    status(f"AssemblyAI: transcript ready ({result['speaker_count']} speakers, {len(result['turns'])} turns)")
    return result


def download_video_audio(video_url: str, output_dir: Path) -> Path | None:
    """YouTube audio extraction with existing yt-dlp auth/client fallbacks."""
    from .youtube.cli import ytdlp_auth_args, ytdlp_error
    output_dir.mkdir(parents=True, exist_ok=True)
    errors = []
    for client, fallback_format in (("web_embedded", None), ("android_vr", None), ("mweb", "18")):
        status(f"YouTube: downloading audio {video_url} ({client})")
        format_args = ["-f", fallback_format] if fallback_format else []
        result = subprocess.run(
            ["yt-dlp", "--no-update", "-x", "--audio-format", "mp3", "--audio-quality", "0", "--no-playlist",
             *format_args, "--extractor-args", f"youtube:player_client={client}", *ytdlp_auth_args(),
             "-o", str(output_dir / "%(title)s [%(id)s].%(ext)s"), video_url],
            capture_output=True, text=True, check=False, timeout=1800)
        files = [p for p in output_dir.glob("*.mp3") if p.stat().st_size > 0]
        if result.returncode == 0 and len(files) == 1:
            return files[0]
        errors.append(f"{client}: {ytdlp_error(result.stderr)}")
    status(f"Failed to download {video_url}: {'; '.join(errors)}")
    return None


def download_loom_audio(url: str, output_dir: Path) -> Path:
    from .loom.cli import share_url
    from .youtube.cli import ytdlp_error
    url = share_url(url)
    video_id = url.rsplit("/", 1)[-1]
    output_dir.mkdir(parents=True, exist_ok=True)
    status(f"Loom: downloading audio {url}")
    result = subprocess.run(
        ["yt-dlp", "--no-update", "--no-playlist", "-x", "--audio-format", "mp3", "--audio-quality", "0",
         "-f", "hls-raw-audio-audio/bestaudio/best", "--socket-timeout", "30", "--retries", "3",
         "--fragment-retries", "3", "--concurrent-fragments", "10",
         "-o", str(output_dir / "%(title)s [%(id)s].%(ext)s"), url],
        capture_output=True, text=True, check=False, timeout=1800)
    if result.returncode != 0:
        raise ValueError(f"Loom audio download failed for {video_id}: {ytdlp_error(result.stderr)}")
    files = [p for p in output_dir.glob("*.mp3") if p.name.endswith(f"[{video_id}].mp3")]
    if len(files) != 1 or files[0].stat().st_size == 0:
        raise ValueError(f"Missing or ambiguous downloaded Loom audio: {video_id}")
    return files[0]


def download_audio_ephemeral(media_url: str, target_dir: Path) -> Path | None:
    """Generic media/reels: extract temporary MP3, with a direct-media fallback."""
    cmd = ["yt-dlp", "-x", "--audio-format", "mp3", "--audio-quality", "0",
           "--no-playlist", "--no-warnings", "-o", str(target_dir / "audio.%(ext)s"), media_url]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False, timeout=1800)
    if proc.returncode != 0:
        with (httpx.Client(timeout=60.0, follow_redirects=True) as client,
              client.stream("GET", media_url) as resp):
            resp.raise_for_status()
            direct_file = target_dir / "audio.mp4"
            with direct_file.open("wb") as stream:
                for chunk in resp.iter_bytes(chunk_size=65536):
                    stream.write(chunk)
        convert = subprocess.run(
            ["ffmpeg", "-y", "-i", str(direct_file), "-vn", "-acodec", "libmp3lame", str(target_dir / "audio.mp3")],
            capture_output=True, text=True, check=False, timeout=1800)
        direct_file.unlink(missing_ok=True)
        if convert.returncode != 0:
            raise ValueError(f"Audio conversion failed: {convert.stderr[-300:]}")
    mp3s = [p for p in target_dir.glob("*.mp3") if p.stat().st_size > 0]
    return mp3s[0] if len(mp3s) == 1 else None


def transcribe_media_url(media_url: str, api_key: str | None = None, context: str = "",
                         *, cache_path: Path | None = None) -> dict | None:
    """Reel enrichment is best-effort; None means failure, empty turns mean silence."""
    try:
        if cache_path and cache_path.exists():
            return validate_transcript(json.loads(cache_path.read_text(encoding="utf-8")))
        key = get_api_key(api_key)
        with tempfile.TemporaryDirectory() as temporary:
            status("Reel: downloading / extracting temporary audio")
            audio = download_audio_ephemeral(media_url, Path(temporary))
            if audio is None:
                raise ValueError("No extracted audio")
            return transcribe_audio(audio, context, key, cache_path=cache_path)
    except Exception as exc:  # noqa: BLE001 - one reel must not abort the other posts.
        status(f"Warning: audio transcription failed ({type(exc).__name__})")
        return None


def transcript_path(video_dir: Path, video_id: str) -> Path | None:
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", video_id):
        raise ValueError(f"Invalid video ID: {video_id}")
    # Legacy filenames contain [id] instead of -id; both are the same source.
    files = [p for p in video_dir.glob("*.md") if p.name.endswith((f"-{video_id}.md", f"[{video_id}].md"))]
    if len(files) > 1:
        raise ValueError(f"Multiple transcripts for {video_id}: {files}")
    return files[0] if files else None


def transcript_metadata(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    try:
        end = lines.index("---", 1)
        meta = yaml.safe_load("\n".join(lines[1:end]))
        return meta if isinstance(meta, dict) else {}
    except (ValueError, yaml.YAMLError):
        return {}


def needs_transcript(video_dir: Path, video_id: str) -> bool:
    path = transcript_path(video_dir, video_id)
    if path is None:
        return True
    meta = transcript_metadata(path)
    return not (str(meta.get("id")) == video_id and meta.get("transcript") is True
                and "## Transcript" in path.read_text(encoding="utf-8"))


def transcript_body(result: dict) -> str:
    result = validate_transcript(result)
    speakers = {s["id"]: s["label"] for s in result["speakers"]}
    return "\n\n".join(f"### Speaker {t['speaker_id']} · {speakers[t['speaker_id']]}\n\n{t['text']}"
                         for t in result["turns"]) or "> [No spoken dialogue detected]"


def save_transcript(video: dict, result: dict, video_dir: Path) -> Path:
    result = validate_transcript(result)
    video_id = str(video["id"])
    existing = transcript_path(video_dir, video_id)
    previous = transcript_metadata(existing) if existing else {}
    if existing and not result["turns"]:
        raise ValueError(f"Empty result; refusing to overwrite existing transcript for {video_id}")
    title = " ".join(str(video.get("title") or video_id).split())
    day = str(video.get("upload_date") or "")
    if len(day) == 8 and day.isdigit():
        day = f"{day[:4]}-{day[4:6]}-{day[6:]}"
    slug = re.sub(r"[^\w]+", "-", title.lower()).strip("-")[:60].rstrip("-") or "video"
    path = existing or video_dir / f"{day or 'undated'}-{slug}-{video_id}.md"
    speakers = {s["id"]: s["label"] for s in result["speakers"]}
    meta = {
        "id": video_id, "title": title, "date": day,
        "url": video.get("url") or (f"https://www.loom.com/share/{video_id}"
            if re.fullmatch(r"[a-f0-9]{32}", video_id) else f"https://www.youtube.com/watch?v={video_id}"),
        "description": video.get("description") or "", "author": video.get("author") or "",
        "model": result["model"], "transcript": True, "speaker_count": result["speaker_count"], "speakers": speakers,
    }
    category = video.get("category") or previous.get("category")
    if category:
        meta["category"] = category
    md = "---\n" + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True) \
         + f"---\n\n# {title}\n\n## Transcript\n\n{transcript_body(result)}\n"
    from pipeline.transcript_norm import TranscriptValidationError, normalize_transcript
    try:
        md = normalize_transcript(md, source=str(path))
    except TranscriptValidationError:
        status(f"Warning: transcript normalization refused for {video_id}; keeping raw transcript")
    atomic_write(path, md)
    video.update({k: meta[k] for k in ("model", "speaker_count", "speakers")})
    return path


def transcribe_videos(platform: str, selected: list[dict], video_dir: Path,
                      download, api_key: str | None = None, workers: int = 2) -> None:
    """One orchestration path for YouTube and Loom, including caching and concurrency."""
    if workers < 1:
        raise ValueError("--workers must be at least 1")
    pending = []
    for video in selected:
        ident = str(video["id"])
        if needs_transcript(video_dir, ident):
            pending.append(video)
        else:
            meta = transcript_metadata(transcript_path(video_dir, ident))
            for key in ("model", "speaker_count", "speakers"):
                if key in meta:
                    video[key] = meta[key]
    stage(f"{len(selected) - len(pending)} transcripts already saved; {len(pending)} pending")
    board = ParallelJobBoard(f"{platform} transcripts", len(pending))
    for video in pending:
        board.add_job(str(video["id"]), str(video.get("title") or video["id"]))

    def run_one(video: dict) -> None:
        ident = str(video["id"])
        with active_job(board, ident):
            cache = video_dir.parent / CACHE_DIR / f"{ident}.json"
            if cache.exists():
                result = validate_transcript(json.loads(cache.read_text(encoding="utf-8")))
            else:
                key = get_api_key(api_key)
                with tempfile.TemporaryDirectory() as temporary:
                    board.update(ident, stage="downloading audio", step=1, style="yellow")
                    mp3 = download(video["url"], Path(temporary))
                    if mp3 is None:
                        raise ValueError(f"Download failed for {platform} video {ident}")
                    match = re.search(r"\[([a-zA-Z0-9_-]+)\]$", mp3.stem)
                    if not match or match[1] != ident:
                        raise ValueError(f"Downloaded audio does not match selected {platform} video")
                    context = (f"Title: {video.get('title') or ''}\nChannel: {video.get('author') or ''}\n"
                               f"Description: {video.get('description') or ''}")
                    result = transcribe_audio(mp3, context, key, cache_path=cache)
                atomic_write(cache, json.dumps(validate_transcript(result), ensure_ascii=False, indent=2) + "\n")
            board.update(ident, stage="saving transcript", step=4.5, style="cyan")
            save_transcript(video, result, video_dir)
            board.update(ident, stage="complete", done=True)

    failures = []
    with ThreadPoolExecutor(max_workers=workers) as pool, board.run():
        futures = {pool.submit(run_one, video): video for video in pending}
        finished = as_completed(futures)
        if not board.terminal:
            finished = track(finished, f"{platform} audio / AssemblyAI transcripts", unit="video", total=len(futures))
        for future in finished:
            try:
                future.result()
            except Exception as exc:  # noqa: BLE001 - finish other sources before surfacing failures.
                failures.append(exc)
                if board.progress is not None:
                    board.update(str(futures[future]["id"]), stage="failed", error=str(exc))
                else:
                    status(f"Error: {platform} {exc}")
            finally:
                board.advance_overall()
    if failures:
        raise failures[0]
    stage(f"{len(selected)} transcripts available")


def rebuild_transcripts(videos: list[dict], video_dir: Path) -> int:
    """Re-export only AssemblyAI caches offline; never relabel legacy model output."""
    count = 0
    for video in videos:
        transcript_path(video_dir, str(video["id"]))
        cache = video_dir.parent / CACHE_DIR / f"{video['id']}.json"
        if cache.exists():
            save_transcript(video, validate_transcript(json.loads(cache.read_text())), video_dir)
            count += 1
    return count


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("media", type=Path, help="Local audio or video file (original preserved)")
    parser.add_argument("--context", default="", help="Recording context, not a rewrite instruction")
    parser.add_argument("--output", required=True, type=Path, help="Validated transcript JSON; also enables resume")
    args = parser.parse_args(argv)
    if args.media.resolve() == args.output.resolve():
        parser.error("--output must not overwrite the input media")
    transcribe_audio(args.media, args.context, cache_path=args.output)


if __name__ == "__main__":
    main()
