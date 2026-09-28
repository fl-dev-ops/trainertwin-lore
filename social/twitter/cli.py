#!/usr/bin/env python3
"""CLI tool to fetch Twitter/X data via TwitterAPI.io and export as YAML and Markdown."""

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
if __package__ is None:  # Allow direct script invocation after moving under social/.
    sys.path.insert(0, str(PROJECT_ROOT))
from social.dates import published_day

load_dotenv(PROJECT_ROOT / ".env")
load_dotenv()

BASE_URL = "https://api.twitterapi.io"
DEFAULT_DATA_DIR = PROJECT_ROOT / "users" / "olga" / "data" / "twitter"
RATE_LIMIT_SLEEP = 5.0  # TwitterAPI.io free tier is 1 req / 5 seconds


def get_api_key(args_key: str | None) -> str:
    key = args_key or os.getenv("TWITTER_API_KEY")
    if not key:
        print("Error: TWITTER_API_KEY not found in args or .env", file=sys.stderr)
        sys.exit(1)
    return key


def extract_username(target: str) -> str:
    cleaned = target.strip().rstrip("/")
    if "x.com" in cleaned or "twitter.com" in cleaned:
        cleaned = cleaned.split("?")[0].split("/")[-1]
    return cleaned.lstrip("@")


def extract_tweet_id(target: str) -> str:
    cleaned = target.strip()
    if "/" in cleaned:
        # e.g. https://x.com/user/status/1808511113124048946
        parts = cleaned.split("?")[0].split("/")
        return parts[-1]
    return cleaned


def fetch_api(endpoint: str, params: dict[str, Any], api_key: str) -> dict[str, Any]:
    url = f"{BASE_URL}{endpoint}"
    headers = {"x-api-key": api_key}
    with httpx.Client(timeout=60.0) as client:
        resp = client.get(url, params=params, headers=headers)
        if resp.status_code == 429:
            print("  Rate limited. Waiting 6 seconds before retrying...", file=sys.stderr)
            time.sleep(6.0)
            resp = client.get(url, params=params, headers=headers)

        if resp.status_code != 200:
            print(f"Error {resp.status_code}: {resp.text}", file=sys.stderr)
            sys.exit(1)
        return resp.json()


def fetch_user_profile(username: str, api_key: str) -> dict[str, Any]:
    res = fetch_api("/twitter/user/info", {"userName": username}, api_key)
    return res.get("data", {})


def fetch_user_following(username: str, api_key: str, max_count: int = 50) -> list[dict[str, Any]]:
    followings: list[dict[str, Any]] = []
    cursor: str | None = None
    page = 1

    while True:
        params: dict[str, Any] = {"userName": username, "pageSize": min(max_count, 100)}
        if cursor:
            params["cursor"] = cursor

        data = fetch_api("/twitter/user/followings", params, api_key)
        items = data.get("followings", [])
        if not items:
            break
        followings.extend(items)

        if len(followings) >= max_count or not data.get("has_next_page"):
            break
        cursor = data.get("next_cursor")
        if not cursor:
            break

        time.sleep(RATE_LIMIT_SLEEP)
        page += 1

    return followings[:max_count]


def fetch_user_followers(username: str, api_key: str, max_count: int = 50) -> list[dict[str, Any]]:
    followers: list[dict[str, Any]] = []
    cursor: str | None = None
    page = 1

    while True:
        params: dict[str, Any] = {"userName": username, "pageSize": min(max_count, 100)}
        if cursor:
            params["cursor"] = cursor

        data = fetch_api("/twitter/user/followers", params, api_key)
        items = data.get("followers", [])
        if not items:
            break
        followers.extend(items)

        if len(followers) >= max_count or not data.get("has_next_page"):
            break
        cursor = data.get("next_cursor")
        if not cursor:
            break

        time.sleep(RATE_LIMIT_SLEEP)
        page += 1

    return followers[:max_count]


def fetch_user_mentions(username: str, api_key: str, max_count: int = 20) -> list[dict[str, Any]]:
    mentions: list[dict[str, Any]] = []
    cursor: str | None = None

    while True:
        params: dict[str, Any] = {"userName": username}
        if cursor:
            params["cursor"] = cursor

        data = fetch_api("/twitter/user/mentions", params, api_key)
        items = data.get("tweets", [])
        if not items:
            break
        mentions.extend(items)

        if len(mentions) >= max_count or not data.get("has_next_page"):
            break
        cursor = data.get("next_cursor")
        if not cursor:
            break

        time.sleep(RATE_LIMIT_SLEEP)

    return mentions[:max_count]


def fetch_user_tweets(username: str, api_key: str, max_tweets: int | None = None, since: date | None = None) -> list[dict[str, Any]]:
    all_tweets: list[dict[str, Any]] = []
    cursor: str | None = None
    page = 1

    while True:
        params: dict[str, Any] = {"userName": username}
        if cursor:
            params["cursor"] = cursor

        data = fetch_api("/twitter/user/last_tweets", params, api_key)
        data_block = data.get("data", {})
        tweets = data_block.get("tweets", []) if isinstance(data_block, dict) else []
        if not tweets and isinstance(data.get("tweets"), list):
            tweets = data["tweets"]

        if not tweets:
            break

        if since is not None:
            today = datetime.now(UTC).date()
            dates = [published_day(t.get("createdAt")) for t in tweets]
            all_tweets.extend(t for t, day in zip(tweets, dates) if since <= day <= today)
            if all(day < since for day in dates):
                break
        else:
            all_tweets.extend(tweets)
        print(f"  Fetched page {page}: {len(tweets)} tweets (Total: {len(all_tweets)})", file=sys.stderr)

        if max_tweets and len(all_tweets) >= max_tweets:
            all_tweets = all_tweets[:max_tweets]
            break

        if not data.get("has_next_page"):
            break

        cursor = data.get("next_cursor")
        if not cursor:
            break

        time.sleep(RATE_LIMIT_SLEEP)
        page += 1

    return all_tweets


def fetch_tweet_thread(tweet_id: str, api_key: str) -> list[dict[str, Any]]:
    thread_tweets: list[dict[str, Any]] = []
    cursor: str | None = None

    while True:
        params: dict[str, Any] = {"tweetId": tweet_id}
        if cursor:
            params["cursor"] = cursor

        data = fetch_api("/twitter/tweet/thread_context", params, api_key)
        items = data.get("tweets", [])
        if not items:
            break
        thread_tweets.extend(items)

        if not data.get("has_next_page"):
            break
        cursor = data.get("next_cursor")
        if not cursor:
            break

        time.sleep(RATE_LIMIT_SLEEP)

    return thread_tweets


def fetch_article(tweet_id: str, api_key: str) -> dict[str, Any]:
    return fetch_api("/twitter/article", {"tweet_id": tweet_id}, api_key)


def to_iso_datetime(date_str: str) -> str:
    if not date_str:
        return ""
    try:
        from datetime import datetime, timezone
        dt = datetime.strptime(date_str, "%a %b %d %H:%M:%S %z %Y")
        return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except Exception:
        return date_str


def make_tweet_filename(content: str | None, tweet_id: str, date_str: str | None, seen: set[str]) -> str:
    prefix = ""
    if date_str:
        try:
            from datetime import datetime
            dt = datetime.strptime(date_str, "%a %b %d %H:%M:%S %z %Y")
            prefix = dt.strftime("%Y-%m-%d-")
        except Exception:
            prefix = date_str[:10].replace(" ", "-") + "-"
    words = re.sub(r"[^\w\s-]", "", content or "").split()[:5]
    slug_part = "-".join(w.lower() for w in words)
    if not slug_part:
        slug_part = str(tweet_id)
    base = f"{prefix}{slug_part[:40]}".strip("-")
    filename = f"{base}.md"
    if filename in seen:
        suffix = str(tweet_id)[-6:]
        filename = f"{base}-{suffix}.md"
    seen.add(filename)
    return filename


def save_tweets_to_markdown(
    tweets: list[dict[str, Any]],
    tweets_dir: Path,
    rel_prefix: str = "./tweets",
) -> list[dict[str, Any]]:
    tweets_dir.mkdir(parents=True, exist_ok=True)
    seen_filenames: set[str] = set()
    tweet_index: list[dict[str, Any]] = []

    for tw in tweets:
        tweet_id = str(tw.get("id") or "")
        url = tw.get("url") or tw.get("twitterUrl") or f"https://x.com/i/web/status/{tweet_id}"
        date_str = to_iso_datetime(tw.get("createdAt") or "")
        text = tw.get("text") or ""
        likes = tw.get("likeCount", 0)
        retweets = tw.get("retweetCount", 0)
        replies = tw.get("replyCount", 0)
        quotes = tw.get("quoteCount", 0)
        views = tw.get("viewCount", 0)
        is_reply = tw.get("isReply", False)

        filename = make_tweet_filename(text, tweet_id, date_str, seen_filenames)
        filepath = tweets_dir / filename

        frontmatter = {
            "id": tweet_id,
            "date": date_str,
            "url": url,
            "likes": likes,
            "retweets": retweets,
            "replies": replies,
            "quotes": quotes,
            "views": views,
            "isReply": is_reply,
        }

        # Check for quoted tweet
        quoted = tw.get("quoted_tweet")
        quoted_block = ""
        if quoted and isinstance(quoted, dict):
            q_text = quoted.get("text") or ""
            q_author = quoted.get("author", {}).get("userName") or "unknown"
            q_quoted_lines = "\n".join(f"> {line}" for line in q_text.splitlines())
            quoted_block = f"\n\n### Quoting @{q_author}:\n{q_quoted_lines}\n"

        fm_yaml = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
        md_content = f"---\n{fm_yaml}\n---\n\n{text}{quoted_block}\n"
        filepath.write_text(md_content, encoding="utf-8")

        tweet_index.append({
            "id": tweet_id,
            "date": date_str,
            "url": url,
            "likes": likes,
            "retweets": retweets,
            "replies": replies,
            "file": f"{rel_prefix}/{filename}",
        })

    return tweet_index


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
    common.add_argument("--api-key", help="TwitterAPI.io key (default: TWITTER_API_KEY env var)")
    common.add_argument("-o", "--output", help="Explicit path to output YAML/MD file")
    common.add_argument("--data-dir", help="Base directory for output (default: users/olga/data/twitter)")
    common.add_argument("--slug", help="Slug for filenames (default: extracted username)")
    common.add_argument("--max-tweets", type=int, default=None, help="Max tweets to fetch (default: all)")
    common.add_argument("--with-following", type=int, default=30, help="Max following to extract (default: 30, 0 to skip)")
    common.add_argument("--with-followers", type=int, default=30, help="Max followers to extract (default: 30, 0 to skip)")
    common.add_argument("--with-mentions", type=int, default=20, help="Max mentions to extract (default: 20, 0 to skip)")

    parser = argparse.ArgumentParser(
        description="Fetch Twitter/X data via TwitterAPI.io and export as YAML and Markdown",
        parents=[common],
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # profile
    p_profile = subparsers.add_parser("profile", parents=[common], help="Fetch Twitter profile and network")
    p_profile.add_argument("username", help="Twitter handle or profile URL")

    # tweets
    p_tweets = subparsers.add_parser("tweets", parents=[common], help="Fetch tweets for a user")
    p_tweets.add_argument("username", help="Twitter handle or profile URL")

    # thread
    p_thread = subparsers.add_parser("thread", parents=[common], help="Fetch full conversation thread for a tweet")
    p_thread.add_argument("target", help="Tweet ID or tweet URL")

    # article
    p_article = subparsers.add_parser("article", parents=[common], help="Fetch long-form article for a tweet")
    p_article.add_argument("target", help="Tweet ID or tweet URL")

    # all
    p_all = subparsers.add_parser("all", parents=[common], help="Fetch profile, network, mentions, and all tweets")
    p_all.add_argument("username", help="Twitter handle or profile URL")

    args = parser.parse_args()
    api_key = get_api_key(args.api_key)

    data_dir = Path(args.data_dir).resolve() if args.data_dir else DEFAULT_DATA_DIR

    if args.command == "profile":
        username = extract_username(args.username)
        slug = args.slug or username
        print(f"Fetching profile for @{username}...", file=sys.stderr)
        profile = fetch_user_profile(username, api_key)

        result: dict[str, Any] = {"profile": profile}

        if args.with_following > 0:
            time.sleep(RATE_LIMIT_SLEEP)
            print(f"Fetching following accounts for @{username}...", file=sys.stderr)
            result["following"] = fetch_user_following(username, api_key, max_count=args.with_following)

        if args.with_followers > 0:
            time.sleep(RATE_LIMIT_SLEEP)
            print(f"Fetching followers for @{username}...", file=sys.stderr)
            result["followers"] = fetch_user_followers(username, api_key, max_count=args.with_followers)

        if args.with_mentions > 0:
            time.sleep(RATE_LIMIT_SLEEP)
            print(f"Fetching mentions for @{username}...", file=sys.stderr)
            result["mentions"] = fetch_user_mentions(username, api_key, max_count=args.with_mentions)

        out_file = Path(args.output).resolve() if args.output else data_dir / f"{slug}.yaml"
        dump_yaml(result, out_file)

    elif args.command == "tweets":
        username = extract_username(args.username)
        slug = args.slug or username
        print(f"Fetching tweets for @{username}...", file=sys.stderr)
        tweets_list = fetch_user_tweets(username, api_key, max_tweets=args.max_tweets)

        tweets_dir = data_dir / "tweets"
        tweet_index = save_tweets_to_markdown(tweets_list, tweets_dir)
        print(f"Generated {len(tweet_index)} tweet markdown files in {tweets_dir}", file=sys.stderr)

        out_file = Path(args.output).resolve() if args.output else data_dir / f"{slug}-tweets.yaml"
        dump_yaml({"tweets": tweet_index}, out_file)

    elif args.command == "thread":
        tweet_id = extract_tweet_id(args.target)
        print(f"Fetching thread context for tweet {tweet_id}...", file=sys.stderr)
        thread_tweets = fetch_tweet_thread(tweet_id, api_key)
        print(f"Retrieved {len(thread_tweets)} tweets in thread.", file=sys.stderr)

        if args.output:
            dump_yaml({"thread": thread_tweets}, Path(args.output))
        else:
            for tw in thread_tweets:
                author = tw.get("author", {}).get("userName") or "unknown"
                text = tw.get("text") or ""
                print(f"--- @{author} ({tw.get('createdAt')}) ---\n{text}\n")

    elif args.command == "article":
        tweet_id = extract_tweet_id(args.target)
        print(f"Fetching article for tweet {tweet_id}...", file=sys.stderr)
        art_data = fetch_article(tweet_id, api_key)
        if args.output:
            dump_yaml(art_data, Path(args.output))
        else:
            dump_yaml(art_data)

    elif args.command == "all":
        username = extract_username(args.username)
        slug = args.slug or username

        print(f"Fetching profile for @{username}...", file=sys.stderr)
        profile = fetch_user_profile(username, api_key)
        result = {"profile": profile}

        if args.with_following > 0:
            time.sleep(RATE_LIMIT_SLEEP)
            print(f"Fetching following accounts for @{username}...", file=sys.stderr)
            result["following"] = fetch_user_following(username, api_key, max_count=args.with_following)

        if args.with_followers > 0:
            time.sleep(RATE_LIMIT_SLEEP)
            print(f"Fetching followers for @{username}...", file=sys.stderr)
            result["followers"] = fetch_user_followers(username, api_key, max_count=args.with_followers)

        if args.with_mentions > 0:
            time.sleep(RATE_LIMIT_SLEEP)
            print(f"Fetching mentions for @{username}...", file=sys.stderr)
            result["mentions"] = fetch_user_mentions(username, api_key, max_count=args.with_mentions)

        time.sleep(RATE_LIMIT_SLEEP)
        print(f"Fetching timeline tweets for @{username}...", file=sys.stderr)
        tweets_list = fetch_user_tweets(username, api_key, max_tweets=args.max_tweets)

        tweets_dir = data_dir / "tweets"
        tweet_index = save_tweets_to_markdown(tweets_list, tweets_dir)
        print(f"Generated {len(tweet_index)} tweet markdown files in {tweets_dir}", file=sys.stderr)

        result["tweets"] = tweet_index
        out_file = Path(args.output).resolve() if args.output else data_dir / f"{slug}.yaml"
        dump_yaml(result, out_file)


if __name__ == "__main__":
    main()
