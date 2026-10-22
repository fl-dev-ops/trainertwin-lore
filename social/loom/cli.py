"""Collect Loom share links using audio, never Loom's built-in transcripts.

Run: uv run python -m social.loom.cli --user jane --since 2020-01-01 --source URL_OR_FILE
"""

import argparse
import re
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlparse

from social.transcribe import (
    download_loom_audio as download_audio,  # noqa: F401 - shared download entry point
)
from social.youtube import cli as youtube


def share_url(value: str) -> str:
    parsed = urlparse(value)
    match = re.fullmatch(r"/share/(?:[\w-]+-)?([a-f0-9]{32})/?", parsed.path, re.IGNORECASE)
    if (parsed.scheme != "https"
            or parsed.netloc.lower() not in {"loom.com", "www.loom.com"}
            or not match):
        raise ValueError("Loom needs an HTTPS loom.com/share/<video-id> link, not a folder URL")
    return f"https://www.loom.com/share/{match[1].lower()}"


def source_urls(source: str) -> list[str]:
    """Accept one share link or a text/YAML file; deduplicate URLs in file order."""
    if urlparse(source).scheme:
        return [share_url(source)]
    path = Path(source)
    if not path.is_file():
        raise ValueError(f"Loom source file not found: {path}")
    urls = re.findall(r'https://(?:www\.)?loom\.com/share/[^\s\"\'<>),]+', path.read_text(), re.IGNORECASE)
    if not urls:
        raise ValueError(f"No Loom share links found in {path}")
    return list(dict.fromkeys(share_url(url) for url in urls))


def fetch_video(url: str) -> dict:
    """Read metadata through yt-dlp, without requesting any subtitle/transcript URLs."""
    url = share_url(url)
    video_id = url.rsplit("/", 1)[-1]
    details = youtube.fetch_video_details(url)
    if details.get("id") and str(details["id"]).lower() != video_id:
        raise ValueError(f"Loom metadata ID does not match {url}")
    upload_date = details.get("upload_date")
    if not upload_date and details.get("timestamp") is not None:
        upload_date = datetime.fromtimestamp(float(details["timestamp"]), UTC).date().isoformat()
    return {
        "id": video_id,
        "url": url,
        "title": details.get("title") or video_id,
        "upload_date": upload_date,
        "description": details.get("description") or "",
        "author": details.get("uploader") or "",
    }


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--user", required=True)
    parser.add_argument("--since", required=True, help="Inclusive UTC publication date YYYY-MM-DD")
    parser.add_argument("--source", required=True, help="Loom share URL or text/YAML file of share links")
    parser.add_argument("--no-transcribe", action="store_true")
    args = parser.parse_args(argv)
    from social.cli import main as collect

    options = ["--user", args.user, "--since", args.since, "--loom", args.source]
    if args.no_transcribe:
        options.append("--no-transcribe")
    collect(options)


if __name__ == "__main__":
    main()
