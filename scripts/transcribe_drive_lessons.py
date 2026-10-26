"""Transcribe the Drive closing-system lessons through the shared social.transcribe module.

Downloads live in users/olga/data/drive/src (gitignored media); speaker-labeled
Markdown goes to users/olga/data/drive/videos, validated AssemblyAI JSON cache to
users/olga/data/drive/assemblyai-json (both house conventions).

Run: uv run python scripts/transcribe_drive_lessons.py [--workers 2]
"""

import argparse
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from social.transcribe import save_transcript, transcribe_audio, transcript_path

DATA = Path("users/olga/data/drive")
SRC = DATA / "src"
VIDEOS_DIR = DATA / "videos"
CACHE_DIR = DATA / "assemblyai-json"
FOLDER_URL = "https://drive.google.com/drive/folders/1__ZcIuyySYXH741DlnKdQxGxSeLSv2KA"
CONTEXT = ("Off-Plan Closing System course lesson by Olga Sinenko, real-estate sales coaching "
           "for Dubai off-plan property: lead handling, objection handling, Zoom sales calls, "
           "presenting projects, and closing the sale.")

MEDIA_EXTS = {".mp4", ".mov", ".m4a", ".mp3", ".webm", ".mkv"}


def lesson_date(name: str) -> str:
    """Share dates from the Drive folder listing (2026, current year per Drive UI)."""
    m = re.search(r"[Ll]esson\s+(\d+)", name)
    if not m:
        return ""
    n = int(m.group(1))
    if n >= 7:
        return "2026-09-26"
    if n >= 4:
        return "2026-10-01"
    return "2026-09-28"


def extract_audio(video_path: Path, temp_dir: Path) -> Path:
    """Extract audio with ffmpeg so upload to AssemblyAI is ~15MB instead of 400MB."""
    if video_path.suffix.lower() in {".m4a", ".mp3"}:
        return video_path
    audio_path = temp_dir / f"{video_path.stem}.m4a"
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-i", str(video_path),
        "-vn", "-c:a", "aac", "-b:a", "96k",
        str(audio_path),
    ]
    subprocess.run(cmd, check=True)
    return audio_path


def run_one(path: Path) -> str:
    title = path.stem
    vid = "drive-" + re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60]
    
    # Skip if markdown transcript already exists and is non-empty
    existing = transcript_path(VIDEOS_DIR, vid)
    if existing and existing.stat().st_size > 0:
        return f"SKIP {title} (already transcribed at {existing.name})"

    cache_file = CACHE_DIR / f"{vid}.json"
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as td:
        media_to_upload = extract_audio(path, Path(td))
        result = transcribe_audio(media_to_upload, CONTEXT, cache_path=cache_file)

    out = save_transcript({
        "id": vid, "title": title, "upload_date": lesson_date(title),
        "url": FOLDER_URL, "description": "", "author": "Olga Sinenko",
    }, result, VIDEOS_DIR)
    return f"OK   {title} -> {out.name}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=2, help="Parallel AssemblyAI jobs")
    args = parser.parse_args()

    if not SRC.is_dir():
        sys.exit(f"Source folder not found: {SRC}")

    files = sorted(
        p for p in SRC.rglob("*")
        if p.is_file() and p.suffix.lower() in MEDIA_EXTS and not p.name.startswith(".")
    )
    if not files:
        sys.exit(f"No media files ({MEDIA_EXTS}) found in {SRC}")
    print(f"{len(files)} lesson file(s) found in {SRC}", flush=True)

    failures = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(run_one, p): p for p in files}
        for fut in as_completed(futures):
            try:
                print(fut.result(), flush=True)
            except Exception as exc:
                title = futures[fut].name
                failures.append(title)
                print(f"FAIL {title}: {exc}", flush=True)

    if failures:
        sys.exit(f"{len(failures)} failed: {failures}")
    print("\nAll lessons transcribed successfully!")


if __name__ == "__main__":
    main()
