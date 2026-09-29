"""Ephemeral audio transcription helper using Sarvam AI.

Features:
- Downloads video/reel audio into a temporary directory.
- Uploads audio to Sarvam AI and IMMEDIATELY deletes the local audio file.
- Downloads transcription JSON into temporary directory, parses diarized turns,
  and cleans up all temporary artifacts automatically.
- Zero permanent local media storage.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

from .progress import status
from .youtube.cli import get_sarvam_key, hhmmss, load_entries, restitch_chunks


def download_audio_ephemeral(media_url: str, target_dir: Path) -> Path | None:
    """Download audio stream from media URL into target_dir as MP3. Returns path or None."""
    out_template = str(target_dir / "audio.%(ext)s")
    # yt-dlp handles direct MP4 URLs, YouTube, Instagram reels, Twitter videos
    cmd = [
        "yt-dlp",
        "-x",
        "--audio-format",
        "mp3",
        "--audio-quality",
        "0",
        "--no-warnings",
        "-o",
        out_template,
        media_url,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False, timeout=180)
    if proc.returncode != 0:
        # Fallback for direct audio/video HTTP streaming
        try:
            import httpx

            with (
                httpx.Client(timeout=60.0, follow_redirects=True) as client,
                client.stream("GET", media_url) as resp,
            ):
                if resp.status_code == 200:
                    direct_file = target_dir / "audio.mp4"
                    with direct_file.open("wb") as f:
                        for chunk in resp.iter_bytes(chunk_size=65536):
                            f.write(chunk)
                    mp3_file = target_dir / "audio.mp3"
                    convert = subprocess.run(
                        ["ffmpeg", "-y", "-i", str(direct_file), "-vn", "-acodec", "libmp3lame", str(mp3_file)],
                        capture_output=True,
                        text=True,
                        check=False,
                    )
                    direct_file.unlink(missing_ok=True)
                    if convert.returncode == 0 and mp3_file.exists():
                        return mp3_file
        except Exception as exc:  # noqa: BLE001
            print(f"Warning: Ephemeral audio download failed for {media_url[:60]}: {exc}", file=sys.stderr)
            return None
        return None

    mp3s = [p for p in target_dir.glob("*.mp3") if p.stat().st_size > 1000]
    return mp3s[0] if mp3s else None


def transcribe_media_url(
    media_url: str,
    api_key: str | None = None,
) -> list[dict[str, str]]:
    """Download audio, upload to Sarvam, immediately delete audio, and return transcript turns."""
    try:
        key = get_sarvam_key(api_key)
    except SystemExit:
        return []
    if not key or not media_url:
        return []

    from sarvamai import SarvamAI

    with tempfile.TemporaryDirectory() as tmp_str:
        tmp_dir = Path(tmp_str)
        status("Reel: downloading / extracting temporary audio")
        audio_file = download_audio_ephemeral(media_url, tmp_dir)
        if not audio_file or not audio_file.exists():
            return []

        try:
            client = SarvamAI(api_subscription_key=key)
            job = client.speech_to_text_job.create_job(
                model="saaras:v3",
                mode="verbatim",
                language_code="unknown",
                with_timestamps=True,
                with_diarization=True,
            )
            status("Reel: uploading audio to Sarvam")
            job.upload_files([str(audio_file)], timeout=600)
            # IMMEDIATELY delete the local audio file upon upload!
            audio_file.unlink(missing_ok=True)
            job.start()

            status("Reel: local audio deleted; waiting for Sarvam transcription (percentage unavailable)")
            result = job.wait_until_complete(poll_interval=5, timeout=1200)
            if not job.is_successful():
                print(f"Warning: Sarvam transcription failed for {media_url[:60]}: {result.job_state}", file=sys.stderr)
                return []

            json_out = tmp_dir / "sarvam_out"
            json_out.mkdir(parents=True, exist_ok=True)
            status("Reel: downloading transcript results")
            job.download_outputs(str(json_out))

            json_files = list(json_out.rglob("*.json"))
            if not json_files:
                return []

            raw_entries = load_entries(json_files[0])
            stitched = restitch_chunks(raw_entries)
            status(f"Reel: transcript ready ({len(stitched)} turns)")
            return [
                {
                    "t": hhmmss(e.start),
                    "speaker": str(e.speaker_id),
                    "text": e.text.strip(),
                }
                for e in stitched
            ]
        except Exception as exc:  # noqa: BLE001
            print(f"Warning: Error during ephemeral Sarvam transcription: {exc}", file=sys.stderr)
            return []
        finally:
            if audio_file and audio_file.exists():
                audio_file.unlink(missing_ok=True)
