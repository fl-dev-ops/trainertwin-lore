"""YouTube discovery; all media processing is delegated to social.transcribe."""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if not __package__:
    sys.path.insert(0, str(PROJECT_ROOT))
from social.fs import atomic_write
from social.progress import status, track
from social.transcribe import (
    download_video_audio,
    rebuild_transcripts,
    transcribe_videos,
)

load_dotenv(PROJECT_ROOT / ".env")
load_dotenv()
DEFAULT_DATA_DIR = PROJECT_ROOT / "users" / "olga" / "data" / "youtube"


def fetch_channel_videos(channel_url: str, max_videos: int | None = None) -> list[dict[str, Any]]:
    """Discover both regular videos and shorts; also accepts playlists or single videos."""
    clean_url = channel_url.rstrip("/")
    base_channel = re.sub(r"/(videos|shorts|featured|playlists|community|streams)$", "", clean_url)
    if re.search(r"(/@[^/]+|/channel/[^/]+|/c/[^/]+|/user/[^/]+)$", base_channel):
        targets = [f"{base_channel}/videos", f"{base_channel}/shorts"]
    else:
        targets = [clean_url]
    seen, entries = set(), []
    for target in targets:
        status(f"YouTube: discovering content from {target} (waiting for yt-dlp)")
        proc = subprocess.run(["yt-dlp", "--no-update", "--flat-playlist", "-J", target],
                              capture_output=True, text=True, check=False)
        if proc.returncode != 0:
            continue
        try:
            data = json.loads(proc.stdout)
        except ValueError:
            continue
        for item in data.get("entries") or ([data] if data.get("id") else []):
            vid = str(item.get("id") or "")
            if len(vid) != 11 or vid.startswith("UC") or vid in seen:
                continue
            seen.add(vid)
            entries.append(item)
    if not entries:
        raise ValueError(f"No videos found from {channel_url}")
    videos = []
    for item in entries:
        vid = str(item["id"])
        url = item.get("url") or ""
        if not str(url).startswith("https://"):
            url = f"https://www.youtube.com/watch?v={vid}"
        videos.append({
            "id": vid, "title": item.get("title"), "url": url,
            "upload_date": item.get("upload_date"), "view_count": item.get("view_count"),
            "description": item.get("description") or "",
            "author": str(item.get("uploader_id") or item.get("channel") or item.get("uploader") or "").removeprefix("@"),
        })
        if max_videos and len(videos) >= max_videos:
            break
    return videos


def ytdlp_auth_args() -> list[str]:
    """Extra yt-dlp auth flags when set (datacenter IPs get bot-blocked without cookies).

    Set YT_DLP_COOKIES to a cookie jar, or explicitly opt into a local browser
    with YT_DLP_COOKIES_FROM_BROWSER=safari. Browser cookies are not exported.
    """
    if cookies := os.getenv("YT_DLP_COOKIES"):
        return ["--cookies", cookies]
    if browser := os.getenv("YT_DLP_COOKIES_FROM_BROWSER"):
        return ["--cookies-from-browser", browser]
    return []


def ytdlp_error(stderr: str) -> str:
    """yt-dlp stderr is mostly update/PO-token warnings; the last ERROR line is the reason."""
    lines = [line.strip() for line in stderr.splitlines() if line.strip()]
    errors = [line for line in lines if line.startswith("ERROR:")]
    return (errors or lines or ["unknown yt-dlp error"])[-1]


def fetch_video_details(url: str) -> dict[str, Any]:
    result = subprocess.run(["yt-dlp", "--no-update", "--skip-download", "--no-playlist", *ytdlp_auth_args(), "-J", url],
                            capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise ValueError(f"Could not fetch video metadata for {url}: {ytdlp_error(result.stderr)}")
    return json.loads(result.stdout)


def enrich_video(video: dict[str, Any]) -> None:
    if video.get("upload_date") and video.get("description") and video.get("author"):
        return
    try:
        details = fetch_video_details(video["url"])
    except ValueError as exc:
        status(f"Warning: could not fetch details for {video.get('url')}: {exc}")
        if not video.get("upload_date"):
            raise
        return
    video["upload_date"] = video.get("upload_date") or details.get("upload_date")
    video["description"] = video.get("description") or details.get("description") or ""
    video["author"] = video.get("author") or str(
        details.get("uploader_id") or details.get("channel") or details.get("uploader") or ""
    ).removeprefix("@")


def save_video_index(url: str, videos: list[dict[str, Any]], path: Path) -> None:
    """Preserve earlier collected videos; refresh metadata without keeping media."""
    previous = (yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else {}) or {}
    known = {v["id"]: v for v in previous.get("videos", []) if v.get("id")}
    for video in videos:
        old = known.get(video["id"], {})
        known[video["id"]] = {**old, **video}
        known[video["id"]].pop("duration", None)
        if not video.get("description") and old.get("description"):
            known[video["id"]]["description"] = old["description"]
    dump_yaml({"channel_url": previous.get("channel_url") or url,
               "total_videos": len(known), "videos": list(known.values())}, path)


def dump_yaml(data: Any, output_path: Path | None = None) -> None:
    text = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=120)
    if output_path:
        atomic_write(output_path, text)
        status(f"Saved to {output_path}")
    else:
        print(text)


def main(argv: list[str] | None = None) -> None:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--api-key", help="AssemblyAI API key (default: ASSEMBLYAI_API_KEY)")
    common.add_argument("--data-dir", help="Output directory (default: users/olga/data/youtube)")
    common.add_argument("-o", "--output", help="Manifest YAML path")
    parser = argparse.ArgumentParser(description=__doc__, parents=[common])
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ("list", "all"):
        sub = commands.add_parser(command, parents=[common])
        sub.add_argument("url", help="YouTube channel, playlist, or video URL")
        sub.add_argument("--max-videos", type=int)
        sub.add_argument("--slug", help="Manifest filename slug")
    sub = commands.add_parser("transcribe", parents=[common])
    sub.add_argument("url", nargs="?", help="YouTube video URL")
    sub.add_argument("--build", action="store_true", help="Rebuild saved AssemblyAI JSON offline")
    args = parser.parse_args(argv)
    data = Path(args.data_dir).resolve() if args.data_dir else DEFAULT_DATA_DIR
    manifest = Path(args.output).resolve() if args.output else data / f"{getattr(args, 'slug', None) or data.parent.parent.name}.yaml"
    if args.command == "transcribe" and args.build:
        index = (yaml.safe_load(manifest.read_text()) if manifest.exists() else {}) or {}
        count = rebuild_transcripts(index.get("videos", []), data / "video")
        save_video_index(index.get("channel_url", ""), index.get("videos", []), manifest)
        status(f"Rebuilt {count} transcripts")
        return
    if not args.url:
        parser.error("transcribe requires a video URL or --build; batch submit/wait is no longer supported")
    if args.command == "transcribe":
        details = fetch_video_details(args.url)
        videos = [{"id": str(details["id"]), "url": args.url, "title": details.get("title"),
                   "upload_date": details.get("upload_date"), "description": details.get("description") or "",
                   "author": details.get("uploader") or ""}]
    else:
        videos = fetch_channel_videos(args.url, args.max_videos)
        for video in track(videos, "YouTube metadata / dates", unit="video"):
            enrich_video(video)
    save_video_index(args.url, videos, manifest)
    if args.command != "list":
        transcribe_videos("YouTube", videos, data / "video", download_video_audio,
                          api_key=args.api_key)
        save_video_index(args.url, videos, manifest)


if __name__ == "__main__":
    main()
