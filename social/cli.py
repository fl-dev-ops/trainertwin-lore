"""Collect a person's public social sources from an absolute UTC calendar date to today.

Run: uv run python -m social --user jane-doe --since 2026-08-01 --linkedin URL ...
"""

import argparse
import hashlib
import json
import re
from datetime import UTC, date, datetime
from pathlib import Path
from urllib.parse import urlparse

from .dates import published_day
from .instagram import cli as instagram
from .linkedin import cli as linkedin
from .twitter import cli as twitter
from .youtube import cli as youtube

ROOT = Path(__file__).resolve().parents[1]
DOMAINS = {
    "linkedin": {"linkedin.com"},
    "twitter": {"x.com", "twitter.com"},
    "instagram": {"instagram.com"},
    "youtube": {"youtube.com", "youtu.be"},
}


def profile_url(value: str, platform: str) -> str:
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
    posts = linkedin.fetch_all_posts(url, key, since=since)
    result["posts"] = linkedin.save_posts_to_markdown(
        posts, data / "posts", api_key=key, comments_min=1
    )
    linkedin.dump_yaml(result, data / f"{slug}.yaml")


def collect_twitter(url: str, data: Path, since: date) -> None:
    key = twitter.get_api_key(None)
    username = twitter.extract_username(url)
    profile = twitter.fetch_user_profile(username, key)
    tweets = twitter.fetch_user_tweets(username, key, since=since)
    result = {
        "profile": profile,
        "tweets": twitter.save_tweets_to_markdown(tweets, data / "tweets"),
    }
    twitter.dump_yaml(result, data / f"{username}.yaml")


def collect_instagram(url: str, data: Path, since: date) -> None:
    key = instagram.get_api_key(None)
    username = instagram.extract_username(url)
    profile = instagram.fetch_profile(username, key)
    posts = instagram.fetch_posts(username, key, since=since)
    result = {
        "profile": profile,
        "posts": instagram.save_posts_to_markdown(posts, data / "posts"),
    }
    instagram.dump_yaml(result, data / f"{username}.yaml")


def video_date(video: dict) -> date:
    """Flat playlists may omit dates; fetch full metadata when required."""
    if not video.get("upload_date"):
        youtube.enrich_video(video)
    return published_day(video.get("upload_date"))


def collect_youtube(
    url: str, data: Path, audio_root: Path, since: date, transcribe: bool
) -> None:
    videos = youtube.fetch_channel_videos(url)
    today = datetime.now(UTC).date()
    selected = []
    for video in videos:
        if not str(video.get("url", "")).startswith("https://"):
            video["url"] = f"https://www.youtube.com/watch?v={video['id']}"
        day = video_date(video)
        if since <= day <= today:
            video["upload_date"] = day.isoformat()
            youtube.enrich_video(video)
            selected.append(video)
    manifest = data / f"{data.parent.parent.name}.yaml"
    youtube.save_video_index(url, selected, manifest)
    if not transcribe or not selected:
        return
    run_id = hashlib.sha256(url.encode()).hexdigest()[:10]
    audio_dir = audio_root / since.isoformat() / run_id
    run = audio_root / "runs" / since.isoformat() / run_id
    selection = run / "selection.json"
    identifiers = [
        v["id"] for v in sorted(selected, key=lambda v: v.get("title") or "")
    ]
    if selection.exists() and json.loads(selection.read_text()) != identifiers:
        raise ValueError(
            f"Video selection changed for {since}; review {run} before reusing Sarvam jobs"
        )
    selection.parent.mkdir(parents=True, exist_ok=True)
    selection.write_text(json.dumps(identifiers) + "\n", encoding="utf-8")
    for video in selected:
        ident = video.get("id")
        if (
            not ident
            or not any(
                p.name.endswith(f"[{ident}].mp3") for p in audio_dir.glob("*.mp3")
            )
        ) and youtube.download_video_audio(video["url"], audio_dir) is None:
            raise ValueError(f"Download failed: {video['url']}")
    state, raw = run / "sarvam-jobs.json", run / "sarvam-json"
    video_dir = data / "video"
    if all(list(video_dir.glob(f"*-{v['id']}.md")) for v in selected):
        return
    cache = youtube.load_date_cache(audio_dir)
    cache.update({v["id"]: v["upload_date"] for v in selected if v.get("id")})
    youtube.save_date_cache(audio_dir, cache)
    key = youtube.get_sarvam_key(None)
    if not state.exists():
        youtube.submit_sarvam_jobs(audio_dir, run / "uploads", state, key)
    youtube.wait_and_download_sarvam(state, raw, key)
    count = youtube.build_markdowns_from_json(audio_dir, raw, video_dir, selected)
    if count != len(selected):
        raise ValueError(
            f"Only {count}/{len(selected)} YouTube transcripts built; inspect {run}"
        )


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
            f"--{platform}", help=f"{platform.title()} profile/channel URL"
        )
    parser.add_argument(
        "--no-transcribe",
        action="store_true",
        help="YouTube: save dated video metadata without downloading/transcribing",
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
        parser.error("Provide at least one social profile/channel URL")
    try:
        urls = {p: profile_url(url, p) for p, url in urls.items()}
        base = ROOT / "users" / args.user
        for platform, url in urls.items():
            data = base / "data" / platform
            if platform == "linkedin":
                collect_linkedin(url, data, since)
            elif platform == "twitter":
                collect_twitter(url, data, since)
            elif platform == "instagram":
                collect_instagram(url, data, since)
            else:
                collect_youtube(
                    url, data, base / "audios", since, not args.no_transcribe
                )
    except ValueError as exc:
        parser.exit(1, f"Collection stopped: {exc}\n")


if __name__ == "__main__":
    main()
