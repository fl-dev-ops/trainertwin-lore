"""Collect a person's public social sources from an absolute UTC calendar date to today.

Run: uv run python -m social --user jane-doe --since 2026-08-01 --linkedin URL ...
"""

import argparse
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import UTC, date, datetime
from pathlib import Path
from urllib.parse import urlparse

import yaml

from .dates import published_day
from .instagram import cli as instagram
from .linkedin import cli as linkedin
from .loom import cli as loom
from .progress import platform_progress, stage, status, track
from .transcribe import transcribe_videos
from .twitter import cli as twitter
from .youtube import cli as youtube

ROOT = Path(__file__).resolve().parents[1]
DOMAINS = {
    "linkedin": {"linkedin.com"},
    "twitter": {"x.com", "twitter.com"},
    "instagram": {"instagram.com"},
    "youtube": {"youtube.com", "youtu.be"},
    "loom": {"loom.com"},
}


def profile_url(value: str, platform: str) -> str:
    if platform == "loom":
        loom.source_urls(value)  # Validate the share URL or all links in the source file.
        return value
    parsed = urlparse(value)
    host = (parsed.hostname or "").lower().removeprefix("www.")
    if (
        parsed.scheme != "https"
        or host not in DOMAINS[platform]
        or not parsed.path.strip("/")
    ):
        raise ValueError(
            f"--{platform} needs an https profile/channel URL on {', '.join(sorted(DOMAINS[platform]))}"
        )
    if platform in {"linkedin", "twitter", "instagram"} and (
        "/status/" in parsed.path or "/posts/" in parsed.path or "/p/" in parsed.path
    ):
        raise ValueError(f"--{platform} needs a profile URL, not an individual post")
    return value


def collect_linkedin(url: str, data: Path, since: date) -> None:
    key = linkedin.get_api_key(None)
    slug = linkedin.extract_slug(url)
    profile = linkedin.fetch_harvest("/linkedin/profile", {"url": url}, key)
    result = linkedin.split_profile_sections(profile.get("element", profile))
    stage("profile fetched")
    posts = linkedin.fetch_all_posts(url, key, since=since)
    stage(f"{len(posts)} dated posts fetched")
    result["posts"] = linkedin.save_posts_to_markdown(
        posts, data / "posts", api_key=key, comments_min=1
    )
    linkedin.dump_yaml(result, data / f"{slug}.yaml")
    stage(f"{len(result['posts'])} posts saved")


def collect_twitter(url: str, data: Path, since: date) -> None:
    key = twitter.get_api_key(None)
    username = twitter.extract_username(url)
    profile = twitter.fetch_user_profile(username, key)
    stage("profile fetched")
    tweets = twitter.fetch_user_tweets(username, key, since=since)
    stage(f"{len(tweets)} dated tweets fetched")
    result = {
        "profile": profile,
        "tweets": twitter.save_tweets_to_markdown(tweets, data / "tweets"),
    }
    twitter.dump_yaml(result, data / f"{username}.yaml")
    stage(f"{len(result['tweets'])} tweets saved")


def collect_instagram(url: str, data: Path, since: date) -> None:
    key = instagram.get_api_key(None)
    username = instagram.extract_username(url)
    profile = instagram.fetch_profile(username, key)
    stage("profile fetched")
    posts = instagram.fetch_posts(username, key, since=since)
    stage(f"{len(posts)} dated posts fetched")
    result = {
        "profile": profile,
        "posts": instagram.save_posts_to_markdown(posts, data / "posts"),
    }
    instagram.dump_yaml(result, data / f"{username}.yaml")
    stage(f"{len(result['posts'])} posts enriched and saved")


def video_date(video: dict) -> date | None:
    """Flat playlists may omit dates; fetch full metadata when required."""
    if not video.get("upload_date"):
        try:
            youtube.enrich_video(video)
        except ValueError:
            return None
    raw_date = video.get("upload_date")
    if not raw_date:
        return None
    try:
        return published_day(raw_date)
    except ValueError:
        return None


def collect_youtube(
    url: str, data: Path, since: date, transcribe: bool, workers: int = 2
) -> None:
    videos = youtube.fetch_channel_videos(url)
    stage(f"{len(videos)} videos discovered")
    manifest = data / f"{data.parent.parent.name}.yaml"
    previous = (
        yaml.safe_load(manifest.read_text(encoding="utf-8")) if manifest.exists() else {}
    ) or {}
    known = {v["id"]: v for v in previous.get("videos", []) if v.get("id")}
    today = datetime.now(UTC).date()
    selected = []
    for video in track(videos, "YouTube metadata / dates", unit="video"):
        if not str(video.get("url", "")).startswith("https://"):
            video["url"] = f"https://www.youtube.com/watch?v={video['id']}"
        old = known.get(video["id"], {})
        for key in ("upload_date", "description", "author", "title"):
            if not video.get(key) and old.get(key):
                video[key] = old[key]
        day = video_date(video)
        if day is None:
            status(f"YouTube: skipped {video.get('id', 'unknown')} — publication date unavailable")
        elif since <= day <= today:
            video["upload_date"] = day.isoformat()
            youtube.enrich_video(video)
            selected.append(video)
    status(f"YouTube: selected {len(selected)}/{len(videos)} videos for {since} through {today}")
    youtube.save_video_index(url, selected, manifest)
    stage(f"{len(selected)} dated videos indexed")
    if not transcribe or not selected:
        stage("audio skipped")
        stage("transcription skipped")
        return

    transcribe_videos("YouTube", selected, data / "video", youtube.download_video_audio, workers=workers)
    youtube.save_video_index(url, selected, manifest)


def collect_loom(
    source: str, data: Path, since: date, transcribe: bool, workers: int = 2
) -> None:
    urls = loom.source_urls(source)
    stage(f"{len(urls)} Loom share links discovered")
    selected = []
    today = datetime.now(UTC).date()
    for url in track(urls, "Loom metadata / dates", unit="video"):
        video = loom.fetch_video(url)
        try:
            day = published_day(video.get("upload_date"))
        except ValueError:
            status(f"Loom: skipped {video['id']} — publication date unavailable")
            continue
        if since <= day <= today:
            video["upload_date"] = day.isoformat()
            selected.append(video)
    status(f"Loom: selected {len(selected)}/{len(urls)} videos for {since} through {today}")
    youtube.save_video_index(source, selected, data / "collected.yaml")
    stage(f"{len(selected)} dated Loom videos indexed")
    if not transcribe or not selected:
        stage("audio skipped")
        stage("transcription skipped")
        return
    transcribe_videos("Loom", selected, data / "videos", loom.download_audio, workers=workers)
    youtube.save_video_index(source, selected, data / "collected.yaml")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--user", required=True, help="Lowercase folder slug under users/"
    )
    parser.add_argument(
        "--since",
        required=True,
        help="Inclusive UTC publication date YYYY-MM-DD; upper bound is today",
    )
    for platform in DOMAINS:
        parser.add_argument(
            f"--{platform}", help="Loom share URL or text/YAML file of share links" if platform == "loom" else f"{platform.title()} profile/channel URL"
        )
    parser.add_argument(
        "--no-transcribe",
        action="store_true",
        help="YouTube/Loom: save dated video metadata without downloading/transcribing",
    )
    parser.add_argument(
        "--workers", type=int, default=2,
        help="Parallel per-video YouTube/Loom download+transcribe jobs (default: 2)",
    )
    args = parser.parse_args(argv)
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.user):
        parser.error("--user must be a lowercase slug (e.g. jane-doe)")
    try:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.since):
            raise ValueError("Expected YYYY-MM-DD")
        since = date.fromisoformat(args.since)
    except ValueError:
        parser.error("--since must be a valid YYYY-MM-DD date")
    if since > datetime.now(UTC).date():
        parser.error("--since cannot be in the future")
    urls = {p: getattr(args, p) for p in DOMAINS if getattr(args, p)}
    if not urls:
        parser.error("Provide at least one social profile/channel URL or --loom source")
    try:
        urls = {p: profile_url(url, p) for p, url in urls.items()}
    except ValueError as exc:
        parser.exit(1, f"Collection stopped: {exc}\n")

    base = ROOT / "users" / args.user

    def collect(platform: str, url: str, position: int) -> None:
        with platform_progress(platform, position, 4 if platform in {"youtube", "loom"} else 3, len(urls)):
            status(f"{platform}: collecting {since} through {datetime.now(UTC).date()}")
            data = base / "data" / platform
            if platform == "linkedin":
                collect_linkedin(url, data, since)
            elif platform == "twitter":
                collect_twitter(url, data, since)
            elif platform == "instagram":
                collect_instagram(url, data, since)
            elif platform == "loom":
                collect_loom(url, data, since, not args.no_transcribe, args.workers)
            else:
                collect_youtube(url, data, since, not args.no_transcribe, args.workers)
            status(f"{platform}: collection finished")

    failures = []
    with ThreadPoolExecutor(max_workers=len(urls)) as pool:
        jobs = {
            pool.submit(collect, platform, url, position): platform
            for position, (platform, url) in enumerate(urls.items())
        }
        for job in as_completed(jobs):
            try:
                job.result()
            except Exception as exc:  # noqa: BLE001 - one platform must not abort the others.
                status(f"Error collecting {jobs[job]}: {exc}")
                failures.append(f"{jobs[job]}: {exc}")
    if failures:
        parser.exit(1, "Collection finished with errors:\n  " + "\n  ".join(failures) + "\n")


if __name__ == "__main__":
    main()
