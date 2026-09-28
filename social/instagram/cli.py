"""CLI tool to fetch Instagram data via Apify and export as YAML and Markdown."""

import argparse
import os
import re
import sys
from datetime import UTC, date, datetime
from pathlib import Path
from typing import Any

import httpx
import yaml
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if __package__ is None:  # Allow direct script invocation after moving under social/.
    sys.path.insert(0, str(PROJECT_ROOT))
from social.dates import in_window

load_dotenv(PROJECT_ROOT / ".env")
load_dotenv()

APIFY_BASE = "https://api.apify.com/v2/acts"
DEFAULT_DATA_DIR = PROJECT_ROOT / "users" / "olga" / "data" / "instagram"


def get_api_key(args_key: str | None) -> str:
    key = args_key or os.getenv("APIFY_API_KEY")
    if not key:
        print("Error: APIFY_API_KEY not found in args or .env", file=sys.stderr)
        sys.exit(1)
    return key


def extract_username(target: str) -> str:
    cleaned = target.strip().rstrip("/")
    if "instagram.com" in cleaned:
        cleaned = cleaned.split("?")[0].split("/")[-1]
    return cleaned.lstrip("@")


def run_apify_actor(actor_id: str, input_payload: dict[str, Any], api_key: str) -> list[dict[str, Any]]:
    """Run an Apify actor synchronously and return its dataset items."""
    url = f"{APIFY_BASE}/{actor_id}/run-sync-get-dataset-items"
    params = {"token": api_key}
    with httpx.Client(timeout=180.0) as client:
        resp = client.post(url, params=params, json=input_payload)
        if resp.status_code != 200 and resp.status_code != 201:
            print(f"Error {resp.status_code} running Apify actor {actor_id}: {resp.text}", file=sys.stderr)
            sys.exit(1)
        data = resp.json()
        return data if isinstance(data, list) else []


def fetch_profile(username: str, api_key: str) -> dict[str, Any]:
    """Fetch Instagram profile metadata."""
    print(f"Fetching profile for @{username}...", file=sys.stderr)
    items = run_apify_actor("apify~instagram-profile-scraper", {"usernames": [username]}, api_key)
    if not items:
        print(f"Warning: No profile data returned for @{username}", file=sys.stderr)
        return {}
    raw = items[0]
    return {
        "id": str(raw.get("id") or ""),
        "username": raw.get("username") or username,
        "fullName": raw.get("fullName") or "",
        "biography": raw.get("biography") or "",
        "externalUrl": raw.get("externalUrl") or "",
        "followersCount": raw.get("followersCount", 0),
        "followsCount": raw.get("followsCount", 0),
        "postsCount": raw.get("postsCount", 0),
        "verified": raw.get("verified", False),
        "profilePicUrl": raw.get("profilePicUrl") or "",
    }


def normalize_post_type(item: dict[str, Any]) -> str:
    raw_type = item.get("type", "").lower()
    prod = item.get("productType", "").lower()
    if raw_type == "video" or prod == "clips":
        return "reel"
    if raw_type == "sidecar" or prod == "carousel_container":
        return "carousel"
    return "image"


def fetch_posts(
    username: str,
    api_key: str,
    max_per_type: int | None = None,
    max_posts: int | None = None,
    since: date | None = None,
) -> list[dict[str, Any]]:
    """Fetch posts using apify~instagram-scraper and filter by type/limits."""
    target_url = f"https://www.instagram.com/{username}/"
    scrape_limit = 10000 if since is not None and max_posts is None else (60 if max_per_type else (max_posts or 30))

    print(f"Fetching posts from {target_url} (query limit: {scrape_limit})...", file=sys.stderr)
    input_payload = {
        "directUrls": [target_url],
        "resultsType": "posts",
        "resultsLimit": scrape_limit,
    }
    if since is not None:
        input_payload["onlyPostsNewerThan"] = since.isoformat()
    raw_posts = run_apify_actor("apify~instagram-scraper", input_payload, api_key)
    if since is not None:
        if len(raw_posts) >= scrape_limit:
            raise ValueError("Instagram hit its resultsLimit; increase it before claiming full date coverage")
        today = datetime.now(UTC).date()
        raw_posts = [p for p in raw_posts if in_window(p.get("timestamp"), since, today)]

    if not max_per_type:
        return raw_posts[:max_posts] if max_posts else raw_posts

    # Filter to most recent N of each type
    counts: dict[str, int] = {"reel": 0, "carousel": 0, "image": 0}
    filtered: list[dict[str, Any]] = []

    for p in raw_posts:
        ptype = normalize_post_type(p)
        if counts.get(ptype, 0) < max_per_type:
            filtered.append(p)
            counts[ptype] = counts.get(ptype, 0) + 1

        if all(c >= max_per_type for c in counts.values()):
            break

    print(f"Selected by type breakdown: {counts}", file=sys.stderr)
    return filtered


def make_post_filename(caption: str | None, post_id: str, date_str: str | None, ptype: str, seen: set[str]) -> str:
    prefix = ""
    if date_str:
        prefix = date_str[:10] + "-"
    words = re.sub(r"[^\w\s-]", "", caption or "").split()[:5]
    slug_part = "-".join(w.lower() for w in words)
    if not slug_part:
        slug_part = f"{ptype}-{post_id}"
    base = f"{prefix}{slug_part[:40]}".strip("-")
    filename = f"{base}.md"
    if filename in seen:
        suffix = post_id[-6:]
        filename = f"{base}-{suffix}.md"
    seen.add(filename)
    return filename


def save_posts_to_markdown(
    posts: list[dict[str, Any]],
    posts_dir: Path,
    rel_prefix: str = "./posts",
) -> list[dict[str, Any]]:
    posts_dir.mkdir(parents=True, exist_ok=True)
    seen_filenames: set[str] = set()
    post_index: list[dict[str, Any]] = []

    for p in posts:
        post_id = str(p.get("id") or "")
        ptype = normalize_post_type(p)
        url = p.get("url") or f"https://www.instagram.com/p/{p.get('shortCode')}/"
        date_str = p.get("timestamp") or ""
        caption = p.get("caption") or ""
        likes = p.get("likesCount", 0)
        comments_count = p.get("commentsCount", 0)
        views = p.get("videoViewCount") or p.get("videoPlayCount")
        location = p.get("locationName")

        filename = make_post_filename(caption, post_id, date_str, ptype, seen_filenames)
        filepath = posts_dir / filename

        frontmatter: dict[str, Any] = {
            "id": post_id,
            "type": ptype,
            "date": date_str,
            "url": url,
            "likes": likes,
            "comments": comments_count,
        }
        if views is not None:
            frontmatter["views"] = views
        if location:
            frontmatter["location"] = location

        video_url = p.get("videoUrl")
        if ptype == "reel" and video_url:
            frontmatter["videoUrl"] = video_url

        # Check for firstComment or latestComments
        comments_section = ""
        latest_comments = p.get("latestComments", [])
        if latest_comments and isinstance(latest_comments, list):
            comment_lines = [f"\n\n## Comments ({len(latest_comments)})\n"]
            for c in latest_comments:
                author = c.get("ownerUsername") or "user"
                c_text = (c.get("text") or "").strip()
                quoted_text = "\n".join(f"> {line}" for line in c_text.splitlines())
                comment_lines.append(f"### @{author}\n{quoted_text}\n")
            comments_section = "\n".join(comment_lines)

        fm_yaml = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
        md_content = f"---\n{fm_yaml}\n---\n\n## Caption\n{caption}{comments_section}\n"
        filepath.write_text(md_content, encoding="utf-8")

        entry: dict[str, Any] = {
            "id": post_id,
            "type": ptype,
            "date": date_str[:10] if date_str else "",
            "url": url,
            "likes": likes,
            "comments": comments_count,
            "file": f"{rel_prefix}/{filename}",
        }
        if views is not None:
            entry["views"] = views
        post_index.append(entry)

    return post_index


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
    common.add_argument("--api-key", help="Apify API token (default: APIFY_API_KEY env var)")
    common.add_argument("-o", "--output", help="Explicit path to output manifest YAML")
    common.add_argument("--data-dir", help="Base directory for output (default: users/olga/data/instagram)")
    common.add_argument("--slug", help="Slug for filenames (default: extracted username)")
    common.add_argument("--max-posts", type=int, default=None, help="Max total posts to fetch")
    common.add_argument("--max-per-type", type=int, default=None, help="Max posts to select per type (reel, carousel, image)")

    parser = argparse.ArgumentParser(
        description="Fetch Instagram data via Apify and export as YAML and Markdown",
        parents=[common],
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # profile
    p_profile = subparsers.add_parser("profile", parents=[common], help="Fetch Instagram profile metadata")
    p_profile.add_argument("username", help="Instagram username or profile URL")

    # posts
    p_posts = subparsers.add_parser("posts", parents=[common], help="Fetch posts from an Instagram profile")
    p_posts.add_argument("username", help="Instagram username or profile URL")

    # all
    p_all = subparsers.add_parser("all", parents=[common], help="Fetch both profile and posts")
    p_all.add_argument("username", help="Instagram username or profile URL")

    args = parser.parse_args()
    api_key = get_api_key(args.api_key)

    data_dir = Path(args.data_dir).resolve() if args.data_dir else DEFAULT_DATA_DIR
    username = extract_username(args.username)
    slug = args.slug or username

    if args.command == "profile":
        profile = fetch_profile(username, api_key)
        out_file = Path(args.output).resolve() if args.output else data_dir / f"{slug}.yaml"
        dump_yaml({"profile": profile}, out_file)

    elif args.command == "posts":
        posts_list = fetch_posts(
            username,
            api_key,
            max_per_type=args.max_per_type,
            max_posts=args.max_posts,
        )
        posts_dir = data_dir / "posts"
        post_index = save_posts_to_markdown(posts_list, posts_dir)
        print(f"Generated {len(post_index)} post markdown files in {posts_dir}", file=sys.stderr)

        out_file = Path(args.output).resolve() if args.output else data_dir / f"{slug}-posts.yaml"
        dump_yaml({"posts": post_index}, out_file)

    elif args.command == "all":
        profile = fetch_profile(username, api_key)
        posts_list = fetch_posts(
            username,
            api_key,
            max_per_type=args.max_per_type,
            max_posts=args.max_posts,
        )
        posts_dir = data_dir / "posts"
        post_index = save_posts_to_markdown(posts_list, posts_dir)
        print(f"Generated {len(post_index)} post markdown files in {posts_dir}", file=sys.stderr)

        result = {
            "profile": profile,
            "posts": post_index,
        }
        out_file = Path(args.output).resolve() if args.output else data_dir / f"{slug}.yaml"
        dump_yaml(result, out_file)


if __name__ == "__main__":
    main()
