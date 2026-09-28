"""Model Context Protocol (MCP) server for TrainerTwin Lore.

Exposes source-grounded wiki ingestion, platform behavioral analysis,
social media collection, and persona intelligence tools over stdio for any
MCP-compliant agent harness (Claude Code, Claude Desktop, Codex, OpenCode,
Pi, Cursor, Windsurf, Zed).

Run:
    uv run python -m pipeline.mcp
"""

import json
import os
import re
from datetime import UTC, date, datetime
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
# Preload .env across the whole server so API keys are ready for social & pipeline
load_dotenv(ROOT / ".env")

app = MCPServer(
    name="trainertwin-lore",
    version="0.1.0",
    description="TrainerTwin living wiki synthesis, social collection, and persona behavioral analysis engine",
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

    Supports LinkedIn (HarvestAPI), Twitter/X (TwitterAPI.io),
    Instagram (Apify), and YouTube (yt-dlp + Sarvam AI transcription).

    Args:
        user: Lowercase user slug under users/ (e.g. 'jane-doe')
        since: Inclusive UTC start date formatted as YYYY-MM-DD
        linkedin: Profile URL on linkedin.com
        twitter: Profile URL on x.com or twitter.com
        instagram: Profile URL on instagram.com
        youtube: Channel or playlist URL on youtube.com
        no_transcribe: If True, skips YouTube audio download and Sarvam transcription
    """
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", user):
        return f"Error: user '{user}' must be a lowercase slug (e.g. 'jane-doe')"

    try:
        since_date = date.fromisoformat(since)
        if since_date > datetime.now(UTC).date():
            return "Error: --since cannot be in the future"
    except ValueError:
        return "Error: since date must be formatted as YYYY-MM-DD"

    from social.cli import (
        collect_instagram,
        collect_linkedin,
        collect_twitter,
        collect_youtube,
        profile_url,
    )

    targets = {
        "linkedin": linkedin,
        "twitter": twitter,
        "instagram": instagram,
        "youtube": youtube,
    }
    active_targets = {k: v for k, v in targets.items() if v}
    if not active_targets:
        return "Error: Provide at least one social profile URL (linkedin, twitter, instagram, or youtube)"

    user_base = ROOT / "users" / user
    reports = []

    for platform, url in active_targets.items():
        try:
            valid_url = profile_url(url, platform)
            data_dir = user_base / "data" / platform
            data_dir.mkdir(parents=True, exist_ok=True)

            if platform == "linkedin":
                collect_linkedin(valid_url, data_dir, since_date)
                reports.append(f"• LinkedIn: Collected from {valid_url}")
            elif platform == "twitter":
                collect_twitter(valid_url, data_dir, since_date)
                reports.append(f"• Twitter/X: Collected from {valid_url}")
            elif platform == "instagram":
                collect_instagram(valid_url, data_dir, since_date)
                reports.append(f"• Instagram: Collected from {valid_url}")
            elif platform == "youtube":
                collect_youtube(
                    valid_url,
                    data_dir,
                    user_base / "audios",
                    since_date,
                    not no_transcribe,
                )
                reports.append(
                    f"• YouTube: Collected from {valid_url} (transcribed={not no_transcribe})"
                )
        except (ValueError, RuntimeError, OSError, KeyError, TypeError) as e:
            reports.append(f"• {platform.title()} failed: {e}")

    return f"Social collection finished for user '{user}' since {since}:\n" + "\n".join(
        reports
    )


@app.tool()
def run_full_persona_pipeline(
    user: str,
    since: str = "",
    linkedin: str = "",
    twitter: str = "",
    instagram: str = "",
    youtube: str = "",
    model: str = "",
    max_ingest_calls: int = 20,
    max_build_calls: int = 50,
) -> str:
    """Run the complete end-to-end persona workflow in one step:
    1. Optionally collects social posts if platform URLs are provided.
    2. Ingests source documents and extracts atomic evidence cards with TypeSafe Jev validation.
    3. Builds the living wiki and platform behavioral analysis pages.
    4. Compiles the offline persona analysis report (reports/analysis.md) and timeline.
    5. Returns an executive summary of the compiled persona.

    Args:
        user: Lowercase user slug under users/ (e.g. 'olga', 'jane-doe')
        since: Inclusive UTC start date YYYY-MM-DD (required if social URLs are provided)
        linkedin: Optional LinkedIn profile URL
        twitter: Optional Twitter/X profile URL
        instagram: Optional Instagram profile URL
        youtube: Optional YouTube channel/playlist URL
        model: Model identifier for ingestion & wiki synthesis (default: OPENROUTER_MODEL)
        max_ingest_calls: Max LLM API calls allowed for evidence ingestion
        max_build_calls: Max LLM API calls allowed for wiki synthesis
    """
    summary_lines = [f"### Full Persona Pipeline Execution: {user}"]

    # 1. Social collection if URLs provided
    if any([linkedin, twitter, instagram, youtube]):
        if not since:
            return "Error: 'since' (YYYY-MM-DD) is required when social URLs are provided."
        col_res = collect_social(
            user=user,
            since=since,
            linkedin=linkedin,
            twitter=twitter,
            instagram=instagram,
            youtube=youtube,
        )
        summary_lines.append(f"**Step 1: Social Collection**\n{col_res}")
    else:
        summary_lines.append(
            "**Step 1: Social Collection**: Skipped (using existing files in users/{user}/data/)"
        )

    # 2. Ingest
    ingest_res = run_ingest(
        user=user, model=model, max_calls=max_ingest_calls, dry_run=False
    )
    summary_lines.append(f"**Step 2: Evidence Ingestion**\n{ingest_res}")

    # 3. Build wiki
    build_res = build_wiki(user=user, model=model, max_calls=max_build_calls)
    summary_lines.append(f"**Step 3: Living Wiki Build**\n{build_res}")

    # 4. Analyze
    analyze_res = analyze_persona(user=user)
    summary_lines.append(f"**Step 4: Persona Analysis Compilation**\n{analyze_res}")

    # 5. Read preview of report
    report_preview = read_report(user=user, report_name="analysis")
    preview_snippet = "\n".join(report_preview.splitlines()[:25])
    summary_lines.append(f"**Persona Report Preview:**\n```markdown\n{preview_snippet}\n...\n```")

    return "\n\n".join(summary_lines)


# ============================================================================
# MCP Resources — Direct data access for AI harnesses (Claude, Cursor, OpenCode)
# ============================================================================


@app.resource("trainertwin://users/{user}/analysis")
def get_user_analysis_resource(user: str) -> str:
    """Read the latest compiled persona analysis report for a trainer."""
    try:
        _, workspace = _get_user_paths(user)
        report = workspace / "reports" / "analysis.md"
        if report.is_file():
            return report.read_text(encoding="utf-8")
        return f"Persona report not yet compiled for {user}. Run analyze_persona first."
    except (ValueError, OSError) as e:
        return f"Error reading analysis resource: {e}"


@app.resource("trainertwin://users/{user}/overview")
def get_user_overview_resource(user: str) -> str:
    """Read the cross-topic living wiki overview for a trainer."""
    try:
        _, workspace = _get_user_paths(user)
        overview = workspace / "wiki" / "overview.md"
        if overview.is_file():
            return overview.read_text(encoding="utf-8")
        return f"Wiki overview not yet built for {user}. Run build_wiki first."
    except (ValueError, OSError) as e:
        return f"Error reading overview resource: {e}"


@app.resource("trainertwin://users/{user}/persona-prompt")
def get_user_persona_prompt_resource(user: str) -> str:
    """Read the compiled LLM digital twin system prompt specification."""
    try:
        _, workspace = _get_user_paths(user)
        prompt_file = workspace / "reports" / "persona-prompt.md"
        if prompt_file.is_file():
            return prompt_file.read_text(encoding="utf-8")
        return f"Persona prompt not yet compiled for {user}."
    except (ValueError, OSError) as e:
        return f"Error reading persona prompt resource: {e}"


# ============================================================================
# MCP Prompts — Standard interaction templates for harnesses
# ============================================================================


@app.prompt()
def analyze_trainer_persona(user: str = "olga") -> str:
    """Prompt the agent to inspect and analyze a trainer's communication style and decision rules."""
    return f"""You are analyzing the trainer persona for '{user}' using the TrainerTwin living wiki and evidence cards.
Please inspect the reports and platform behaviors using the available tools:
1. Call `read_report('{user}', 'analysis')` to inspect their platform writing styles, decision heuristics, and linguistic tropes.
2. Call `get_wiki_topic('{user}', 'linkedin')` and `get_wiki_topic('{user}', 'youtube')` to analyze channel-specific behaviors.
3. Summarize:
   - How their tone and structure change between long-form video (YouTube) and text (LinkedIn).
   - Their core non-negotiable decision rules and coaching philosophies.
   - Any linguistic tropes, repeated hooks, and signature phrases.
   - Any areas with provisional or sparse evidence."""


@app.prompt()
def chat_as_trainer_twin(user: str = "olga", user_inquiry: str = "") -> str:
    """Prompt the agent to respond as the authentic trainer twin grounded in verified lore."""
    return f"""You are the authentic digital twin for trainer '{user}'.
First, call `read_report('{user}', 'persona-prompt')` or `read_report('{user}', 'analysis')` to ground your voice, tone, and decision rules strictly in observed evidence.
Then, answer the user's inquiry:
"{user_inquiry}"
Remember:
- Emulate the observed communication style and linguistic tropes.
- Follow the documented decision rules.
- Never hallucinate unverified personal background or services."""


def main() -> None:
    """Start MCP stdio server."""
    app.run("stdio")


if __name__ == "__main__":
    main()
