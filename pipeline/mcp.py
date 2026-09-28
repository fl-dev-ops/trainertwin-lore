"""Model Context Protocol (MCP) server for TrainerTwin Lore.

Exposes source-grounded wiki ingestion, platform behavioral analysis,
and persona intelligence tools over stdio for any MCP-compliant agent harness
(Pi, Claude Code, Cursor, Windsurf, Zed, OpenCode).

Run:
    uv run python -m pipeline.mcp
"""

import json
import os
from pathlib import Path

from dotenv import load_dotenv
from mcp.server.mcpserver import MCPServer

from .client import OpenRouter
from .core import (
    analyze,
    build,
    chunks,
    ingest_one,
    lint,
    load_json,
    read_source,
)
from .sources import paths, source_id

ROOT = Path(__file__).resolve().parents[1]
app = MCPServer(
    name="trainertwin-lore",
    version="0.1.0",
    description="TrainerTwin living wiki synthesis and persona behavioral analysis engine",
)


def _get_user_paths(user: str) -> tuple[Path, Path]:
    user_root = ROOT / "users" / user
    source_dir = (user_root / "data").resolve()
    workspace = (user_root / "workspace").resolve()
    if not source_dir.is_dir():
        raise ValueError(f"User data directory not found: {source_dir}")
    workspace.mkdir(parents=True, exist_ok=True)
    return source_dir, workspace


def _get_client(model: str = "") -> OpenRouter:
    load_dotenv(ROOT / ".env")
    key = os.getenv("OPENROUTER_API_KEY", "")
    if not key:
        raise ValueError("OPENROUTER_API_KEY is missing from environment or .env")
    target_model = model or os.getenv("OPENROUTER_MODEL", "openai/gpt-4o")
    return OpenRouter(key, target_model)


@app.tool()
def get_status(user: str = "olga") -> str:
    """Check pipeline ingestion status, source counts, and stale manifests for a user.

    Args:
        user: Lowercase user slug under users/ (default: 'olga')
    """
    try:
        source_dir, workspace = _get_user_paths(user)
        available = paths(source_dir)
        manifests = list((workspace / "manifest").glob("*.json"))
        known = {source_id(p, source_dir): p for p in available}
        stale = [
            p.stem
            for p in manifests
            if p.stem not in known
            or load_json(p)["source_sha256"]
            != read_source(known[p.stem], source_dir).sha256
            or load_json(p).get("metadata_hash")
            != read_source(known[p.stem], source_dir).metadata_hash
        ]
        return json.dumps(
            {
                "user": user,
                "sources_available": len(available),
                "sources_ingested": len(manifests),
                "stale_manifests_count": len(stale),
                "stale_manifests": stale[:10],
            },
            indent=2,
        )
    except (ValueError, RuntimeError, OSError, KeyError, TypeError) as e:
        return f"Error getting status for {user}: {e}"


@app.tool()
def lint_workspace(user: str = "olga") -> str:
    """Audit evidence card integrity, verbatim quote locators, and topic citations.

    Runs completely offline with zero API calls.

    Args:
        user: Lowercase user slug under users/ (default: 'olga')
    """
    try:
        source_dir, workspace = _get_user_paths(user)
        res = lint(workspace, source_dir)
        return json.dumps({"user": user, "status": "ok", **res}, indent=2)
    except (ValueError, RuntimeError, OSError, KeyError, TypeError) as e:
        return f"Lint failed for {user}: {e}"


@app.tool()
def read_report(user: str = "olga", report_name: str = "analysis") -> str:
    """Read a compiled persona report (analysis, timeline, or persona-prompt).

    Args:
        user: Lowercase user slug under users/ (default: 'olga')
        report_name: One of 'analysis', 'timeline', 'persona-prompt' (default: 'analysis')
    """
    try:
        _, workspace = _get_user_paths(user)
        target = workspace / "reports" / f"{report_name}.md"
        if not target.is_file():
            return f"Report {report_name}.md not found in {workspace / 'reports'}. Run analyze first."
        return target.read_text(encoding="utf-8")
    except (ValueError, RuntimeError, OSError, KeyError, TypeError) as e:
        return f"Error reading report: {e}"


@app.tool()
def get_wiki_topic(user: str = "olga", topic_slug: str = "") -> str:
    """Read an attested living wiki topic page or platform behavioral analysis page.

    Args:
        user: Lowercase user slug under users/ (default: 'olga')
        topic_slug: Topic name or behavior page (e.g. 'linkedin', 'youtube', 'overview', or blank to list all)
    """
    try:
        _, workspace = _get_user_paths(user)
        wiki = workspace / "wiki"
        if not wiki.is_dir():
            return f"Wiki directory not found for {user}. Build wiki first."

        if not topic_slug or topic_slug == "list":
            topics = [p.stem for p in (wiki / "topics").glob("*.md")]
            behaviors = [p.stem for p in (wiki / "behavior").glob("*.md")]
            return json.dumps(
                {"topics": sorted(topics), "behaviors": sorted(behaviors)}, indent=2
            )

        if topic_slug == "overview":
            p = wiki / "overview.md"
        elif (wiki / "behavior" / f"{topic_slug}.md").is_file():
            p = wiki / "behavior" / f"{topic_slug}.md"
        elif (wiki / "topics" / f"{topic_slug}.md").is_file():
            p = wiki / "topics" / f"{topic_slug}.md"
        else:
            return f"Topic or behavior '{topic_slug}' not found."

        return p.read_text(encoding="utf-8")
    except (ValueError, RuntimeError, OSError, KeyError, TypeError) as e:
        return f"Error getting wiki topic: {e}"


@app.tool()
def analyze_persona(user: str = "olga") -> str:
    """Compile persona intelligence report (analysis.md) and chronology offline.

    Runs completely offline without LLM API calls.

    Args:
        user: Lowercase user slug under users/ (default: 'olga')
    """
    try:
        source_dir, workspace = _get_user_paths(user)
        lint(workspace, source_dir, check_report=False)
        report = analyze(workspace, user=user)
        lint(workspace, source_dir)
        return f"Successfully compiled persona report: {report}"
    except (ValueError, RuntimeError, OSError, KeyError, TypeError) as e:
        return f"Error compiling persona report: {e}"


@app.tool()
def run_ingest(
    user: str = "olga",
    model: str = "",
    max_calls: int = 20,
    dry_run: bool = False,
    include_globs: list[str] | None = None,
) -> str:
    """Extract source-grounded evidence cards with verbatim quotes and Jev authorship validation.

    Args:
        user: Lowercase user slug under users/ (default: 'olga')
        model: Structured-output LLM model identifier (e.g. 'openai/gpt-4o')
        max_calls: Maximum logical LLM API calls allowed for this run
        dry_run: If True, inspects planned chunks without making API calls
        include_globs: Optional root-relative glob patterns to restrict ingestion
    """
    try:
        source_dir, workspace = _get_user_paths(user)
        available = paths(source_dir)
        if include_globs:
            from fnmatch import fnmatchcase

            available = [
                p
                for p in available
                if any(
                    fnmatchcase(str(p.relative_to(source_dir)), g)
                    for g in include_globs
                )
            ]

        manifests = list((workspace / "manifest").glob("*.json"))
        known = {source_id(p, source_dir): p for p in available}

        stale = [
            known[p.stem]
            for p in manifests
            if p.stem in known
            and (
                load_json(p)["source_sha256"]
                != read_source(known[p.stem], source_dir).sha256
                or load_json(p).get("metadata_hash")
                != read_source(known[p.stem], source_dir).metadata_hash
            )
        ]
        unprocessed = [
            p
            for p in available
            if not (workspace / "manifest" / f"{source_id(p, source_dir)}.json").exists()
        ]
        work = sorted(set(stale + unprocessed))

        if dry_run:
            total_chunks = sum(
                len(list(chunks(read_source(p, source_dir), 15000))) for p in work
            )
            return json.dumps(
                {
                    "dry_run": True,
                    "sources_to_process": len(work),
                    "estimated_chunks": total_chunks,
                    "max_calls": max_calls,
                },
                indent=2,
            )

        client = _get_client(model)
        calls_used = 0
        for p in work:
            if calls_used >= max_calls:
                break
            src = read_source(p, source_dir)
            source_chunks = list(chunks(src, 15000))
            if calls_used + len(source_chunks) > max_calls:
                break
            ingest_one(workspace, src, client, 15000)
            calls_used += len(source_chunks)

        return f"Ingest completed. Processed sources with {calls_used} API call(s)."
    except (ValueError, RuntimeError, OSError, KeyError, TypeError) as e:
        return f"Error running ingest: {e}"


@app.tool()
def build_wiki(
    user: str = "olga",
    model: str = "",
    max_calls: int = 50,
) -> str:
    """Group topics and synthesize living wiki topic pages and platform behavioral models.

    Args:
        user: Lowercase user slug under users/ (default: 'olga')
        model: Structured-output LLM model identifier (e.g. 'openai/gpt-4o')
        max_calls: Maximum logical LLM API calls allowed for this build
    """
    try:
        source_dir, workspace = _get_user_paths(user)
        client = _get_client(model)
        calls = build(workspace, source_dir, client, max_calls)
        return f"Build completed using {calls} API call(s)."
    except (ValueError, RuntimeError, OSError, KeyError, TypeError) as e:
        return f"Error running build: {e}"


@app.tool()
def collect_social(
    user: str,
    since: str,
    linkedin: str = "",
    twitter: str = "",
    instagram: str = "",
    youtube: str = "",
    no_transcribe: bool = False,
) -> str:
    """Collect public posts from social platforms since an absolute UTC date.

    Args:
        user: Lowercase user slug under users/ (e.g. 'jane-doe')
        since: Inclusive UTC start date formatted as YYYY-MM-DD
        linkedin: Profile URL on linkedin.com
        twitter: Profile URL on x.com or twitter.com
        instagram: Profile URL on instagram.com
        youtube: Channel or playlist URL on youtube.com
        no_transcribe: If True, skips YouTube audio download and Sarvam transcription
    """
    try:
        from social.cli import main as social_main

        argv = ["--user", user, "--since", since]
        if linkedin:
            argv.extend(["--linkedin", linkedin])
        if twitter:
            argv.extend(["--twitter", twitter])
        if instagram:
            argv.extend(["--instagram", instagram])
        if youtube:
            argv.extend(["--youtube", youtube])
        if no_transcribe:
            argv.append("--no-transcribe")

        social_main(argv)
        return f"Successfully collected social sources for {user} since {since}."
    except (ValueError, RuntimeError, OSError, KeyError, TypeError) as e:
        return f"Social collection failed for {user}: {e}"


def main() -> None:
    """Start MCP stdio server."""
    app.run("stdio")


if __name__ == "__main__":
    main()
