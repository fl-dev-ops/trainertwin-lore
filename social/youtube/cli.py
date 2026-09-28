"""CLI tool for YouTube video extraction, audio downloading, and Sarvam AI transcription."""

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")
load_dotenv()

DEFAULT_DATA_DIR = PROJECT_ROOT / "users" / "olga" / "data" / "youtube"
DEFAULT_AUDIOS_DIR = PROJECT_ROOT / "users" / "olga" / "audios"
DEFAULT_TRANSCRIPTS_DIR = DEFAULT_DATA_DIR / "transcripts"
BATCH_SIZE = 20
CHUNK_SECONDS = 30.0  # Sarvam hard-splits long speech at 30s boundaries


def get_sarvam_key(args_key: str | None) -> str:
    key = args_key or os.getenv("SARVAM_API_KEY")
    if not key:
        print("Error: SARVAM_API_KEY not found in args or .env", file=sys.stderr)
        sys.exit(1)
    return key


def hhmmss(seconds: float) -> str:
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def ffprobe_duration(path: Path) -> str:
    out = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    try:
        return hhmmss(float(out.stdout.strip()))
    except ValueError:
        return "unknown"


# --- YAML Formatting Helpers for Pipeline Compatibility ---
class _Folded(str):
    """Render long text with folded block style (>-)."""


class _Quoted(str):
    """Force quoting for sexagesimal ints (00:00:00)."""


class _SingleQuoted(str):
    """Force single quoting for date strings ('YYYY-MM-DD')."""


def _str_representer(dumper, data):
    if isinstance(data, _Folded):
        return dumper.represent_scalar("tag:yaml.org,2002:str", str(data), style=">")
    if isinstance(data, _SingleQuoted):
        return dumper.represent_scalar("tag:yaml.org,2002:str", str(data), style="'")
    if isinstance(data, _Quoted):
        return dumper.represent_scalar("tag:yaml.org,2002:str", str(data), style='"')
    return dumper.represent_scalar("tag:yaml.org,2002:str", str(data))


yaml.SafeDumper.add_representer(_Folded, _str_representer)
yaml.SafeDumper.add_representer(_SingleQuoted, _str_representer)
yaml.SafeDumper.add_representer(_Quoted, _str_representer)
yaml.SafeDumper.add_representer(str, _str_representer)


# --- 1. Video Discovery & Metadata ---
def fetch_channel_videos(channel_url: str, max_videos: int | None = None) -> list[dict[str, Any]]:
    """Extract video metadata from a channel or playlist using yt-dlp flat playlist extraction."""
    cmd = [
        "yt-dlp",
        "--flat-playlist",
        "-J",
        channel_url,
    ]
    print(f"Extracting video list from {channel_url}...", file=sys.stderr)
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        print(f"Error fetching channel metadata: {proc.stderr}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(proc.stdout)
    entries = data.get("entries", [])
    if not entries and data.get("id"):
        entries = [data]

    videos = []
    for item in entries:
        vid_id = item.get("id")
        title = item.get("title")
        url = item.get("url") or f"https://www.youtube.com/watch?v={vid_id}"
        duration = item.get("duration")
        dur_str = hhmmss(duration) if duration else "unknown"

        videos.append({
            "id": vid_id,
            "title": title,
            "url": url,
            "duration": dur_str,
            "upload_date": item.get("upload_date"),
            "view_count": item.get("view_count"),
        })

        if max_videos and len(videos) >= max_videos:
            break

    return videos


# --- 2. Audio Download ---
def download_video_audio(video_url: str, output_dir: Path) -> Path | None:
    """Download single YouTube video audio as MP3."""
    output_dir.mkdir(parents=True, exist_ok=True)
    out_template = str(output_dir / "%(title)s [%(id)s].%(ext)s")
    cmd = [
        "yt-dlp",
        "-x",
        "--audio-format",
        "mp3",
        "--audio-quality",
        "0",
        "--extractor-args",
        "youtube:player_client=web_embedded",  # default client hits HTTP 403 as of Sep 2026
        "-o",
        out_template,
        video_url,
    ]
    print(f"Downloading audio: {video_url}...", file=sys.stderr)
    res = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if res.returncode != 0:
        print(f"Failed to download {video_url}: {res.stderr}", file=sys.stderr)
        return None
    return output_dir


# --- 3. Sarvam AI Batch Transcription ---
@dataclass
class Entry:
    speaker_id: str
    text: str
    start: float
    end: float
    sources: list[int]


def stage_audio_files(audios_dir: Path, uploads_dir: Path) -> list[tuple[Path, Path]]:
    """Hard-link originals to API-safe numbered names without duplicating audio data."""
    files = sorted(audios_dir.glob("*.mp3"))
    if not files:
        raise SystemExit(f"No MP3s found in {audios_dir}")
    uploads_dir.mkdir(parents=True, exist_ok=True)
    staged = []
    for idx, source in enumerate(files, 1):
        upload = uploads_dir / f"{idx:03d}.mp3"
        if upload.exists() and not upload.samefile(source):
            upload.unlink()
        if not upload.exists():
            os.link(source, upload)
        staged.append((upload, source))
    return staged


def submit_sarvam_jobs(
    audios_dir: Path,
    uploads_dir: Path,
    state_file: Path,
    api_key: str,
) -> None:
    from sarvamai import SarvamAI

    client = SarvamAI(api_subscription_key=api_key)
    files = stage_audio_files(audios_dir, uploads_dir)
    states = []
    state_file.parent.mkdir(parents=True, exist_ok=True)

    for start in range(0, len(files), BATCH_SIZE):
        batch = files[start : start + BATCH_SIZE]
        print(f"Submitting batch of {len(batch)} files to Sarvam AI...", file=sys.stderr)
        job = client.speech_to_text_job.create_job(
            model="saaras:v3",
            mode="verbatim",
            language_code="unknown",
            with_timestamps=True,
            with_diarization=True,
        )
        job.upload_files([str(upload) for upload, _ in batch], timeout=600)
        job.start()
        states.append({
            "job_id": job.job_id,
            "files": [{"upload": upload.name, "audio": source.name} for upload, source in batch],
        })
        state_file.write_text(json.dumps(states, indent=2) + "\n")
        print(f"  Submitted job: {job.job_id}", file=sys.stderr)


def wait_and_download_sarvam(
    state_file: Path,
    json_out_dir: Path,
    api_key: str,
) -> None:
    from sarvamai import SarvamAI

    if not state_file.exists():
        raise SystemExit(f"Error: {state_file} not found. Run submit first.")

    json_out_dir.mkdir(parents=True, exist_ok=True)
    client = SarvamAI(api_subscription_key=api_key)
    states = json.loads(state_file.read_text())

    for state in states:
        job = client.speech_to_text_job.get_job(state["job_id"])
        print(f"Waiting for job {job.job_id}...", file=sys.stderr)
        status = job.wait_until_complete(poll_interval=10, timeout=7200)
        print(f"  Job {job.job_id} state: {status.job_state}", file=sys.stderr)
        if not job.is_successful():
            print(json.dumps(job.get_file_results(), indent=2, default=str), file=sys.stderr)
            continue
        job.download_outputs(str(json_out_dir))
        print(f"  Downloaded outputs to {json_out_dir}", file=sys.stderr)


def load_entries(sarvam_path: Path) -> list[Entry]:
    data = json.loads(sarvam_path.read_text())
    raw = (data.get("diarized_transcript") or {}).get("entries", [])
    if not raw:
        raise SystemExit(f"No diarized entries in {sarvam_path}")
    ordered = sorted(raw, key=lambda e: (e["start_time_seconds"], e["end_time_seconds"]))
    return [
        Entry(
            speaker_id=str(e["speaker_id"]),
            text=e["transcript"].strip(),
            start=float(e["start_time_seconds"]),
            end=float(e["end_time_seconds"]),
            sources=[i],
        )
        for i, e in enumerate(ordered)
    ]


def restitch_chunks(entries: list[Entry]) -> list[Entry]:
    """Rejoin entries Sarvam split at the 30s chunk boundary when same speaker + short tail."""
    out: list[Entry] = []
    for e in entries:
        if out:
            prev = out[-1]
            prev_full = abs(prev.end - prev.start - CHUNK_SECONDS) < 0.2
            if prev_full and e.speaker_id == prev.speaker_id and len(e.text.split()) < 20:
                out[-1] = Entry(
                    prev.speaker_id,
                    prev.text + " " + e.text,
                    prev.start,
                    e.end,
                    prev.sources + e.sources,
                )
                continue
        out.append(e)
    return out


def match_sarvam_json(name: str, json_dir: Path) -> Path | None:
    wanted = {f"{name}.json", f"{Path(name).stem}.json"}
    hits = [p for p in json_dir.rglob("*.json") if p.name in wanted]
    return hits[0] if len(hits) == 1 else None


def load_date_cache(data_dir: Path) -> dict[str, str]:
    for p in [data_dir / ".dates_cache.json"]:
        if p.exists():
            try:
                return json.loads(p.read_text())
            except (OSError, json.JSONDecodeError):
                pass
    return {}


def save_date_cache(data_dir: Path, cache: dict[str, str]) -> None:
    cache_file = data_dir / ".dates_cache.json"
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    try:
        cache_file.write_text(json.dumps(cache, indent=2) + "\n")
    except OSError:
        pass


def resolve_video_date(
    mp3_path: Path,
    cache: dict[str, str],
    data_dir: Path,
) -> str | None:
    m = re.search(r"\[([a-zA-Z0-9_-]{11})\]", mp3_path.name)
    vid = m.group(1) if m else None

    if vid and vid in cache:
        return cache[vid]
    if mp3_path.stem in cache:
        return cache[mp3_path.stem]

    # Query yt-dlp if video ID is known
    if vid:
        cmd = [
            "yt-dlp",
            "--extractor-args",
            "youtube:player_client=web_embedded",
            "--print",
            "%(upload_date)s",
            "--no-warnings",
            f"https://www.youtube.com/watch?v={vid}",
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, check=False)
        raw = res.stdout.strip()
        if len(raw) == 8 and raw.isdigit():
            formatted = f"{raw[:4]}-{raw[4:6]}-{raw[6:]}"
            cache[vid] = formatted
            save_date_cache(data_dir, cache)
            return formatted

    return None


def build_yamls_from_json(
    audios_dir: Path,
    json_dir: Path,
    transcripts_dir: Path,
    id_prefix: str = "",
) -> int:
    files = sorted(audios_dir.glob("*.mp3"))
    transcripts_dir.mkdir(parents=True, exist_ok=True)
    date_cache = load_date_cache(transcripts_dir.parent)
    count = 0

    for idx, mp3 in enumerate(files, 1):
        jp = match_sarvam_json(f"{idx:03d}.mp3", json_dir)
        if jp is None:
            continue

        entries = restitch_chunks(load_entries(jp))
        title = re.sub(r" \[[\w-]{6,}\]$", "", mp3.stem).replace("：", ": ")
        video_date = resolve_video_date(mp3, date_cache, transcripts_dir.parent)

        turns = [
            {"t": _Quoted(hhmmss(e.start)), "speaker": e.speaker_id, "text": _Folded(e.text)}
            for e in entries
        ]
        doc: dict[str, Any] = {
            "id": f"{id_prefix}{idx:02d}",
            "title": title,
        }
        if video_date:
            doc["date"] = _SingleQuoted(video_date)
        doc.update({
            "source": title,
            "audio_file": mp3.name,
            "duration": _Quoted(ffprobe_duration(mp3)),
            "model": "saaras:v3",
            "raw_speaker_ids": sorted(
                {e.speaker_id for e in entries},
                key=lambda s: int(s) if s.isdigit() else 99,
            ),
            "counts": {"raw_entries": len(entries)},
            "turns": turns,
        })
        out = transcripts_dir / f"{id_prefix}{idx:02d}.yaml"
        out.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=100))
        count += 1

    return count


def dump_yaml(data: Any, output_path: Path | None = None) -> None:
    yaml_str = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=120)
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(yaml_str, encoding="utf-8")
        print(f"Saved to {output_path}", file=sys.stderr)
    else:
        print(yaml_str)


def main():
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--api-key", help="Sarvam AI API key (default: SARVAM_API_KEY env var)")
    common.add_argument("--data-dir", help="Base directory for output (default: users/olga/data/youtube)")
    common.add_argument("--audios-dir", help="Directory containing audio MP3s (default: users/olga/audios)")
    common.add_argument("--id-prefix", default="", help="Prefix for transcript ids/filenames (e.g. 's' for shorts)")
    common.add_argument("-o", "--output", help="Explicit path to output manifest YAML")

    parser = argparse.ArgumentParser(
        description="YouTube Ingestion & Sarvam AI Transcription CLI",
        parents=[common],
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # list
    p_list = subparsers.add_parser("list", parents=[common], help="List videos and metadata from a channel/playlist")
    p_list.add_argument("url", help="YouTube channel or playlist URL")
    p_list.add_argument("--max-videos", type=int, default=None, help="Max videos to list")
    p_list.add_argument("--slug", help="Slug for manifest filename (default: channel name or youtube)")

    # download
    p_dl = subparsers.add_parser("download", parents=[common], help="Download MP3 audio from a video or playlist")
    p_dl.add_argument("url", help="YouTube video, playlist, or channel URL")

    # transcribe
    p_trans = subparsers.add_parser("transcribe", parents=[common], help="Transcribe audios via Sarvam AI batch jobs")
    p_trans.add_argument("--submit", action="store_true", help="Submit staged audios to Sarvam AI")
    p_trans.add_argument("--wait", action="store_true", help="Wait for jobs and download JSON outputs")
    p_trans.add_argument("--build", action="store_true", help="Build clean YAML transcripts from downloaded JSON")

    # all
    p_all = subparsers.add_parser("all", parents=[common], help="Full pipeline: list -> download -> transcribe -> build")
    p_all.add_argument("url", help="YouTube channel or playlist URL")
    p_all.add_argument("--max-videos", type=int, default=None, help="Max videos to process")
    p_all.add_argument("--slug", default="youtube", help="Slug for manifest filename")

    args = parser.parse_args()

    data_dir = Path(args.data_dir).resolve() if args.data_dir else DEFAULT_DATA_DIR
    audios_dir = Path(args.audios_dir).resolve() if args.audios_dir else DEFAULT_AUDIOS_DIR
    transcripts_dir = data_dir / "transcripts"
    uploads_dir = data_dir / "uploads"
    state_file = data_dir / "sarvam-jobs.json"
    json_dir = data_dir / "sarvam-json"

    if args.command == "list":
        slug = args.slug or "channel"
        videos = fetch_channel_videos(args.url, max_videos=args.max_videos)
        manifest = {
            "channel_url": args.url,
            "total_videos": len(videos),
            "videos": videos,
        }
        out_file = Path(args.output).resolve() if args.output else data_dir / f"{slug}.yaml"
        dump_yaml(manifest, out_file)
        print(f"Listed {len(videos)} videos into {out_file}", file=sys.stderr)

    elif args.command == "download":
        download_video_audio(args.url, audios_dir)

    elif args.command == "transcribe":
        if args.submit:
            api_key = get_sarvam_key(args.api_key)
            submit_sarvam_jobs(audios_dir, uploads_dir, state_file, api_key)
        elif args.wait:
            api_key = get_sarvam_key(args.api_key)
            wait_and_download_sarvam(state_file, json_dir, api_key)
            count = build_yamls_from_json(audios_dir, json_dir, transcripts_dir, args.id_prefix)
            print(f"Built {count} YAML transcripts in {transcripts_dir}", file=sys.stderr)
        elif args.build:
            count = build_yamls_from_json(audios_dir, json_dir, transcripts_dir, args.id_prefix)
            print(f"Built {count} YAML transcripts in {transcripts_dir}", file=sys.stderr)
        else:
            # Default behavior: submit if not submitted, then wait and build
            api_key = get_sarvam_key(args.api_key)
            if not state_file.exists():
                submit_sarvam_jobs(audios_dir, uploads_dir, state_file, api_key)
            wait_and_download_sarvam(state_file, json_dir, api_key)
            count = build_yamls_from_json(audios_dir, json_dir, transcripts_dir, args.id_prefix)
            print(f"Built {count} YAML transcripts in {transcripts_dir}", file=sys.stderr)

    elif args.command == "all":
        # 1. Fetch channel videos
        videos = fetch_channel_videos(args.url, max_videos=args.max_videos)
        manifest = {
            "channel_url": args.url,
            "total_videos": len(videos),
            "videos": videos,
        }
        out_file = Path(args.output).resolve() if args.output else data_dir / f"{args.slug}.yaml"
        dump_yaml(manifest, out_file)

        # 2. Download audio for each video
        for v in videos:
            download_video_audio(v["url"], audios_dir)

        # 3. Transcribe with Sarvam AI
        api_key = get_sarvam_key(args.api_key)
        submit_sarvam_jobs(audios_dir, uploads_dir, state_file, api_key)
        wait_and_download_sarvam(state_file, json_dir, api_key)
        count = build_yamls_from_json(audios_dir, json_dir, transcripts_dir, args.id_prefix)
        print(f"Finished pipeline: {count} transcripts created in {transcripts_dir}", file=sys.stderr)


if __name__ == "__main__":
    main()
