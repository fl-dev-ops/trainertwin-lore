#!/usr/bin/env python3
"""CLI tool to fetch LinkedIn data via HarvestAPI and export as YAML and Markdown."""

import argparse
import os
import re
import sys
import time
from datetime import UTC, date, datetime
from pathlib import Path
from typing import Any

import httpx
import yaml
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if __package__ is None:  # Allow `python social/linkedin/cli.py` as well as `python -m social.linkedin.cli`.
    sys.path.insert(0, str(PROJECT_ROOT))
from social.dates import published_day
from social.progress import status, track

load_dotenv(PROJECT_ROOT / ".env")
load_dotenv()

BASE_URL = "https://api.harvestapi.io"
DEFAULT_DATA_DIR = PROJECT_ROOT / "users" / "olga" / "data" / "linkedin"


def get_api_key(args_key: str | None) -> str:
    key = args_key or os.getenv("HARVEST_API_KEY")
    if not key:
        print("Error: HARVEST_API_KEY not found in args or .env", file=sys.stderr)
        sys.exit(1)
    return key


def extract_slug(target: str) -> str:
    cleaned = target.strip().rstrip("/")
    if "/" in cleaned:
        slug = cleaned.split("/")[-1]
    else:
        slug = cleaned
    return re.sub(r"[^\w-]", "", slug) or "profile"


def normalize_profile_url(target: str) -> str:
    if target.startswith(("http://", "https://")):
        return target
    return f"https://www.linkedin.com/in/{target.strip('/')}/"


def fetch_harvest(endpoint: str, params: dict[str, Any], api_key: str) -> dict[str, Any]:
    url = f"{BASE_URL}{endpoint}"
    headers = {"X-API-Key": api_key}
    with httpx.Client(timeout=60.0) as client:
        resp = client.get(url, params=params, headers=headers)
        if resp.status_code != 200:
            print(f"Error {resp.status_code}: {resp.text}", file=sys.stderr)
            sys.exit(1)
        return resp.json()


def fetch_all_posts(profile_url: str, api_key: str, max_posts: int | None = None, since: date | None = None) -> list[dict[str, Any]]:
    all_posts: list[dict[str, Any]] = []
    token: str | None = None
    page = 1

    with httpx.Client(timeout=60.0) as client:
        while True:
            params: dict[str, Any] = {"profile": profile_url}
            if token:
                params["paginationToken"] = token
            resp = client.get(f"{BASE_URL}/linkedin/profile-posts", params=params, headers={"X-API-Key": api_key})
            if resp.status_code != 200:
                if since is not None:
                    raise ValueError(f"LinkedIn page {page} returned {resp.status_code}; refusing partial date window")
                print(f"Warning: page {page} returned {resp.status_code}: {resp.text}", file=sys.stderr)
                break
            data = resp.json()
            elements = data.get("elements", [])
            if not elements:
                break
            if since is not None:
                today = datetime.now(UTC).date()
                dates = [published_day(p.get("postedAt", {}).get("date")) for p in elements]
                all_posts.extend(p for p, day in zip(elements, dates) if since <= day <= today)
                if all(day < since for day in dates):
                    break
            else:
                all_posts.extend(elements)
            print(f"  Fetched page {page}: {len(elements)} posts (Total: {len(all_posts)})", file=sys.stderr)

            if max_posts and len(all_posts) >= max_posts:
                all_posts = all_posts[:max_posts]
                break

            pagination = data.get("pagination", {})
            next_token = pagination.get("paginationToken")
            if next_token == token and since is not None:
                raise ValueError("LinkedIn pagination repeated its token; refusing partial date window")
            if not next_token or next_token == token:
                break
            token = next_token
            page += 1

    return all_posts


def fetch_comments_for_post(post_url: str, api_key: str) -> list[dict[str, Any]]:
    try:
        data = fetch_harvest("/linkedin/post-comments", {"post": post_url}, api_key)
        return data.get("elements", [])
    except (ValueError, httpx.HTTPError) as exc:
        print(f"Warning: failed to fetch comments for {post_url}: {exc}", file=sys.stderr)
        return []


def format_comments_markdown(comments: list[dict[str, Any]]) -> str:
    if not comments:
        return ""
    lines = [f"\n\n## Comments ({len(comments)})\n"]
    for c in comments:
        actor = c.get("actor", {})
        name = actor.get("name") or "LinkedIn User"
        pos = actor.get("position")
        role_str = f" ({pos})" if pos else ""
        is_author = " (Author)" if actor.get("author") else ""
        body = (c.get("commentary") or "").strip()
        body_quoted = "\n".join(f"> {line}" for line in body.splitlines()) if body else "> [Empty comment]"
        lines.append(f"### {name}{role_str}{is_author}\n{body_quoted}\n")
    return "\n".join(lines)


def split_profile_sections(raw_element: dict[str, Any]) -> dict[str, Any]:
    profile_data = dict(raw_element)
    experience = profile_data.pop("experience", [])
    education = profile_data.pop("education", [])
    skills = profile_data.pop("skills", [])
    profile_data.pop("currentPosition", None)
    profile_data.pop("profileTopEducation", None)

    return {
        "profile": profile_data,
        "experience": experience,
        "education": education,
        "skills": skills,
    }


def make_post_filename(content: str | None, post_id: str | None, date_str: str | None, seen: set[str]) -> str:
    prefix = ""
    if date_str:
        prefix = date_str[:10] + "-"
    words = re.sub(r"[^\w\s-]", "", content or "").split()[:5]
    slug_part = "-".join(w.lower() for w in words)
    if not slug_part:
        slug_part = str(post_id) if post_id else "post"
    base = f"{prefix}{slug_part[:40]}".strip("-")
    filename = f"{base}.md"
    if filename in seen:
        suffix = str(post_id)[-6:] if post_id else "dup"
        filename = f"{base}-{suffix}.md"
    seen.add(filename)
    return filename


def save_posts_to_markdown(
    posts: list[dict[str, Any]],
    posts_dir: Path,
    rel_prefix: str = "./posts",
    api_key: str | None = None,
    comments_min: int = 0,
) -> list[dict[str, Any]]:
    posts_dir.mkdir(parents=True, exist_ok=True)
    seen_filenames: set[str] = set()
    post_index: list[dict[str, Any]] = []

    for post in track(posts, "LinkedIn posts / comments", unit="post"):
        post_id = str(post.get("id") or "")
        url = post.get("linkedinUrl") or ""
        date_str = post.get("postedAt", {}).get("date") or post.get("postedAt", {}).get("postedAgoText") or ""
        content = post.get("content") or ""
        likes = post.get("engagement", {}).get("likes", 0) or post.get("stats", {}).get("likesCount", 0)
        comments_count = post.get("engagement", {}).get("comments", 0) or post.get("stats", {}).get("commentsCount", 0)
        reposts_count = post.get("engagement", {}).get("reposts", 0) or post.get("stats", {}).get("repostsCount", 0)

        is_repost = bool(post.get("isRepost"))
        is_quote_post = bool(post.get("isQuotePost"))
        reshared_post = post.get("resharedPost") or {}
        article = post.get("article") or {}
        document = post.get("document") or {}
        post_video = post.get("postVideo") or {}
        post_images = post.get("postImages") or []

        comments_text = ""
        has_fetched_comments = False
        if api_key and comments_min > 0 and comments_count >= comments_min and url:
            status(f"LinkedIn: fetching comments for {post_id} ({comments_count} reported)")
            fetched_comments = fetch_comments_for_post(url, api_key)
            comments_text = format_comments_markdown(fetched_comments)
            has_fetched_comments = True
            time.sleep(0.5)

        filename = make_post_filename(content or (reshared_post.get("content") if reshared_post else ""), post_id, date_str, seen_filenames)
        filepath = posts_dir / filename

        frontmatter: dict[str, Any] = {
            "id": post_id,
            "date": date_str,
            "url": url,
            "likes": likes,
            "comments": comments_count,
        }
        if reposts_count:
            frontmatter["reposts"] = reposts_count
        if is_repost:
            frontmatter["is_repost"] = True
        if is_quote_post:
            frontmatter["is_quote_post"] = True
        if article and isinstance(article, dict) and article.get("title"):
            frontmatter["article"] = {
                k: v for k, v in {
                    "title": article.get("title"),
                    "subtitle": article.get("subtitle"),
                    "link": article.get("link"),
                }.items() if v
            }
        if document and isinstance(document, dict) and document.get("title"):
            frontmatter["document"] = {
                k: v for k, v in {
                    "title": document.get("title"),
                    "documentUrl": document.get("documentUrl"),
                    "pageCount": document.get("pageCount"),
                }.items() if v
            }
        if post_video and isinstance(post_video, dict) and post_video.get("videoUrl"):
            frontmatter["videoUrl"] = post_video.get("videoUrl")
        if post_images and isinstance(post_images, list):
            frontmatter["images_count"] = len(post_images)

        # Build Reshared / Quoted Post block (attributed as Quoting @author so pipeline respects boundaries)
        reshared_block = ""
        if reshared_post and isinstance(reshared_post, dict):
            orig_author_info = reshared_post.get("author") or {}
            orig_author = (
                orig_author_info.get("name")
                or orig_author_info.get("publicIdentifier")
                or "unknown"
            )
            orig_url = reshared_post.get("linkedinUrl") or ""
            orig_content = (reshared_post.get("content") or "").strip()
            orig_article = reshared_post.get("article") or {}
            orig_doc = reshared_post.get("document") or {}

            orig_lines: list[str] = []
            if orig_content:
                orig_lines.extend(f"> {line}" for line in orig_content.splitlines())
            if orig_article and orig_article.get("title"):
                orig_lines.append(f"> [Article: {orig_article.get('title')}]({orig_article.get('link', '')})")
            if orig_doc and orig_doc.get("title"):
                orig_lines.append(f"> [Document: {orig_doc.get('title')}]({orig_doc.get('documentUrl', '')})")
            if orig_url:
                orig_lines.append(f"> Original Post: {orig_url}")

            quoted_body = "\n".join(orig_lines) if orig_lines else "> [No text content]"
            reshared_block = f"\n\n### Quoting @{orig_author}:\n{quoted_body}\n"

        article_block = ""
        if article and isinstance(article, dict) and article.get("title"):
            art_title = article.get("title")
            art_link = article.get("link") or ""
            art_sub = article.get("subtitle") or ""
            article_block = f"\n\n### Shared Article: [{art_title}]({art_link})\n" + (f"> {art_sub}\n" if art_sub else "")

        doc_block = ""
        if document and isinstance(document, dict) and document.get("title"):
            doc_title = document.get("title")
            doc_link = document.get("documentUrl") or ""
            pages = document.get("pageCount")
            doc_block = f"\n\n### Shared Document: [{doc_title}]({doc_link})" + (f" ({pages} pages)\n" if pages else "\n")

        fm_yaml = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
        md_content = f"---\n{fm_yaml}\n---\n\n{content}{reshared_block}{article_block}{doc_block}{comments_text}\n"
        filepath.write_text(md_content, encoding="utf-8")

        entry: dict[str, Any] = {
            "id": post_id,
            "date": date_str,
            "url": url,
            "likes": likes,
            "comments": comments_count,
            "file": f"{rel_prefix}/{filename}",
        }
        if reposts_count:
            entry["reposts"] = reposts_count
        if is_repost:
            entry["isRepost"] = True
        if is_quote_post:
            entry["isQuotePost"] = True
        if reshared_post:
            entry["hasResharedPost"] = True
        if article:
            entry["hasArticle"] = True
        if document:
            entry["hasDocument"] = True
        if has_fetched_comments:
            entry["commentsFetched"] = True
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


def find_post_md_file(target: str, data_dir: Path) -> tuple[str, Path | None]:
    """Resolve target to (post_url, md_filepath)."""
    target_path = Path(target)
    if target_path.is_file():
        # Read URL from frontmatter
        content = target_path.read_text(encoding="utf-8")
        match = re.search(r"^url:\s*([^\n]+)", content, re.MULTILINE)
        if match:
            return match.group(1).strip(), target_path
        return "", target_path

    # Treat as URL: look up in posts directory
    posts_dir = data_dir / "posts"
    if posts_dir.is_dir():
        for md_file in posts_dir.glob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            if target in content:
                return target, md_file

    return target, None


def main():
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--api-key", help="HarvestAPI key (default: HARVEST_API_KEY env var)")
    common.add_argument("-o", "--output", help="Explicit path to output YAML/MD file")
    common.add_argument("--data-dir", help="Base directory for output (default: users/olga/data/linkedin)")
    common.add_argument("--slug", help="Slug for filenames (default: extracted from URL)")
    common.add_argument("--comments-min", type=int, default=0, help="Min comments count to trigger comment fetching")
    common.add_argument("--max-posts", type=int, default=None, help="Max posts to fetch (default: all)")

    parser = argparse.ArgumentParser(
        description="Fetch LinkedIn data via HarvestAPI and export as YAML and Markdown",
        parents=[common],
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # profile
    p_profile = subparsers.add_parser("profile", parents=[common], help="Fetch LinkedIn profile")
    p_profile.add_argument("url", help="LinkedIn profile URL or username")
    p_profile.add_argument("--find-email", action="store_true", help="Find and verify work email")

    # posts
    p_posts = subparsers.add_parser("posts", parents=[common], help="Fetch posts from a LinkedIn profile")
    p_posts.add_argument("url", help="LinkedIn profile URL or username")

    # comments
    p_comments = subparsers.add_parser("comments", parents=[common], help="Fetch comments on a post and update its .md file")
    p_comments.add_argument("target", help="LinkedIn post URL or path to post .md file")

    # all
    p_all = subparsers.add_parser("all", parents=[common], help="Fetch both profile and posts for a user")
    p_all.add_argument("url", help="LinkedIn profile URL or username")
    p_all.add_argument("--find-email", action="store_true", help="Find and verify work email")

    args = parser.parse_args()
    api_key = get_api_key(args.api_key)

    data_dir = Path(args.data_dir).resolve() if args.data_dir else DEFAULT_DATA_DIR
    slug = args.slug or extract_slug(getattr(args, "url", getattr(args, "target", "output")))

    if args.command == "profile":
        url = normalize_profile_url(args.url)
        params: dict[str, Any] = {"url": url}
        if args.find_email:
            params["findEmail"] = "true"
        data = fetch_harvest("/linkedin/profile", params, api_key)
        sections = split_profile_sections(data.get("element", data))
        out_file = Path(args.output).resolve() if args.output else data_dir / f"{slug}.yaml"
        dump_yaml(sections, out_file)

    elif args.command == "posts":
        url = normalize_profile_url(args.url)
        print(f"Fetching posts for {url}...", file=sys.stderr)
        posts_list = fetch_all_posts(url, api_key, max_posts=args.max_posts)

        posts_dir = data_dir / "posts"
        post_index = save_posts_to_markdown(
            posts_list,
            posts_dir,
            api_key=api_key,
            comments_min=args.comments_min,
        )
        print(f"Generated {len(post_index)} post markdown files in {posts_dir}", file=sys.stderr)

        out_file = Path(args.output).resolve() if args.output else data_dir / f"{slug}-posts.yaml"
        dump_yaml({"posts": post_index}, out_file)

    elif args.command == "comments":
        post_url, md_path = find_post_md_file(args.target, data_dir)
        if not post_url:
            print(f"Error: could not resolve post URL from {args.target}", file=sys.stderr)
            sys.exit(1)

        print(f"Fetching comments for {post_url}...", file=sys.stderr)
        comments_list = fetch_comments_for_post(post_url, api_key)
        print(f"Retrieved {len(comments_list)} comments.", file=sys.stderr)

        if md_path and md_path.is_file():
            # Append or replace ## Comments in the existing .md file
            raw_text = md_path.read_text(encoding="utf-8")
            if "## Comments" in raw_text:
                body_part = raw_text.split("## Comments")[0].rstrip()
            else:
                body_part = raw_text.rstrip()
            comments_block = format_comments_markdown(comments_list)
            updated_text = f"{body_part}{comments_block}\n"
            md_path.write_text(updated_text, encoding="utf-8")
            print(f"Updated {md_path} with {len(comments_list)} comments.", file=sys.stderr)
        elif args.output:
            dump_yaml({"comments": comments_list}, Path(args.output))
        else:
            print(format_comments_markdown(comments_list))

    elif args.command == "all":
        url = normalize_profile_url(args.url)
        prof_params: dict[str, Any] = {"url": url}
        if args.find_email:
            prof_params["findEmail"] = "true"

        print(f"Fetching profile for {url}...", file=sys.stderr)
        prof_data = fetch_harvest("/linkedin/profile", prof_params, api_key)
        sections = split_profile_sections(prof_data.get("element", prof_data))

        print(f"Fetching all posts for {url}...", file=sys.stderr)
        posts_list = fetch_all_posts(url, api_key, max_posts=args.max_posts)

        posts_dir = data_dir / "posts"
        post_index = save_posts_to_markdown(
            posts_list,
            posts_dir,
            api_key=api_key,
            comments_min=args.comments_min,
        )
        print(f"Generated {len(post_index)} post markdown files in {posts_dir}", file=sys.stderr)

        sections["posts"] = post_index
        out_file = Path(args.output).resolve() if args.output else data_dir / f"{slug}.yaml"
        dump_yaml(sections, out_file)


if __name__ == "__main__":
    main()
