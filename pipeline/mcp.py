"""Model Context Protocol (MCP) server for TrainerTwin Lore.

Exposes source-grounded indexing, Jev taxonomy normalization, scenario retrieval,
SKILL.md authoring, and adversarial validation over stdio for any MCP-compliant
agent harness (Pi, Claude Code, Claude Desktop, Cursor, Windsurf, Zed).

Run:
    uv run python -m pipeline.mcp
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from mcp.server import MCPServer

from .author import author_scenario_prompt
from .normalize import normalize_workspace
from .retrieve import retrieve
from .storage import load_json
from .validate import validate_scenario

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

app = MCPServer(
    name="trainertwin-lore",
    version="0.2.0",
    description="TrainerTwin source-grounded indexing, behavioral retrieval, and SKILL.md authoring engine",
)


def _get_user_dirs(user: str) -> tuple[Path, Path]:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", user):
        raise ValueError("User must be a lowercase slug (e.g. olga, vasanth, jameel)")
    user_root = ROOT / "users" / user
    data_dir = (user_root / "data").resolve()
    workspace = (user_root / "workspace").resolve()
    if not data_dir.is_dir():
        raise ValueError(f"User data directory not found: {data_dir}")
    workspace.mkdir(parents=True, exist_ok=True)
    return data_dir, workspace


def _get_api_key() -> str:
    load_dotenv(ROOT / ".env")
    key = os.getenv("OPENROUTER_API_KEY", "")
    if not key:
        raise ValueError("OPENROUTER_API_KEY is missing from environment or .env")
    return key


@app.tool()
def get_status(user: str = "olga") -> str:
    """Inspect index status, item counts, taxonomy clusters, and authored scenarios for a creator."""
    _, workspace = _get_user_dirs(user)
    index_path = workspace / "index.json"
    tax_path = workspace / "taxonomy.json"
    scenarios_dir = workspace / "scenarios"

    total_sources = 0
    total_items = 0
    if index_path.exists():
        d = load_json(index_path)
        total_sources = len(d.get("sources", {}))
        total_items = len(d.get("items", []))

    concepts_summary = {}
    if tax_path.exists():
        tax = load_json(tax_path)
        for facet, concepts in tax.items():
            concepts_summary[facet] = len(concepts)

    authored_scenarios = []
    if scenarios_dir.is_dir():
        authored_scenarios = [f.stem for f in sorted(scenarios_dir.glob("*.md"))]

    return json.dumps({
        "user": user,
        "indexed_sources": total_sources,
        "indexed_items": total_items,
        "canonical_concepts": concepts_summary,
        "authored_scenarios": authored_scenarios,
    }, indent=2)


@app.tool()
def query_scenarios(user: str, scenario_query: str, max_clips: int = 5) -> str:
    """Retrieve grounded clips for a target scenario using Jev routing + taxonomy expansion.

    Returns the matched canonical concept, Jev confidence, and verbatim source clips with line coordinates.
    """
    data_dir, workspace = _get_user_dirs(user)
    api_key = _get_api_key()
    res = retrieve(workspace, data_dir, scenario_query, api_key, max_clips=max_clips)
    return json.dumps(res, indent=2, ensure_ascii=False)


@app.tool()
def author_scenario_skill(
    user: str,
    scenario_query: str,
    model: str = "google/gemini-3.8-flash",
) -> str:
    """Retrieve grounded clips and author a production-grade SKILL.md runtime prompt.

    Generates YAML frontmatter, Adult-to-Adult relational stance, verbatim signature phrases,
    priority-ordered decision heuristics (with exact file and line citations), and negative boundaries.
    """
    data_dir, workspace = _get_user_dirs(user)
    api_key = _get_api_key()
    out_path, content = author_scenario_prompt(
        workspace, data_dir, scenario_query, api_key, model=model
    )
    return json.dumps({
        "status": "success",
        "output_file": str(out_path.relative_to(ROOT)),
        "content": content,
    }, indent=2)


@app.tool()
def validate_scenario_skill(
    user: str,
    scenario_filename: str,
    judge_model: str = "openai/gpt-4o-mini",
) -> str:
    """Run an adversarial audit on an authored SKILL.md against its verified source evidence.

    Checks citation line integrity, verifies verbatim phrases, and reports grounding/authenticity scores.
    """
    data_dir, workspace = _get_user_dirs(user)
    api_key = _get_api_key()
    skill_path = workspace / "scenarios" / scenario_filename
    if not skill_path.is_file():
        # Try appending .md if omitted
        skill_path = workspace / "scenarios" / f"{scenario_filename}.md"
    if not skill_path.is_file():
        raise FileNotFoundError(f"Scenario file not found: {skill_path}")

    report = validate_scenario(skill_path, data_dir, api_key, judge_model=judge_model)
    return json.dumps(report, indent=2, ensure_ascii=False)


@app.tool()
def read_scenario_skill(user: str, scenario_slug: str) -> str:
    """Read an authored scenario SKILL.md prompt from users/<user>/workspace/scenarios/."""
    _, workspace = _get_user_dirs(user)
    filename = scenario_slug if scenario_slug.endswith(".md") else f"{scenario_slug}.md"
    skill_path = workspace / "scenarios" / filename
    if not skill_path.is_file():
        raise FileNotFoundError(f"Scenario prompt not found at {skill_path}")
    return skill_path.read_text(encoding="utf-8")


@app.tool()
def list_taxonomy(user: str, facet: str = "situation") -> str:
    """List canonical concepts and aliases from taxonomy.json for a given facet (situation, topic, activity)."""
    _, workspace = _get_user_dirs(user)
    tax_path = workspace / "taxonomy.json"
    if not tax_path.exists():
        raise FileNotFoundError(f"Missing {tax_path}. Run normalize first.")
    tax = load_json(tax_path)
    facet_data = tax.get(facet, {})
    return json.dumps(facet_data, indent=2, ensure_ascii=False)


@app.tool()
def collect_social(
    user: str,
    since: str,
    linkedin: str = "",
    youtube: str = "",
    instagram: str = "",
    twitter: str = "",
) -> str:
    """Collect social media posts and transcripts for a creator since a UTC date (YYYY-MM-DD)."""
    cmd = [sys.executable, "-m", "social", "--user", user, "--since", since]
    if linkedin:
        cmd.extend(["--linkedin", linkedin])
    if youtube:
        cmd.extend(["--youtube", youtube])
    if instagram:
        cmd.extend(["--instagram", instagram])
    if twitter:
        cmd.extend(["--twitter", twitter])

    proc = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
    if proc.returncode != 0:
        return json.dumps({"status": "error", "message": proc.stderr or proc.stdout})
    return json.dumps({"status": "success", "output": proc.stdout[-1500:]})


@app.tool()
def reindex_corpus(
    user: str,
    workers: int = 8,
    model: str = "google/gemini-3.8-flash",
) -> str:
    """Index source files into index.json and automatically build normalized taxonomy.json with Jev."""
    cmd = [
        sys.executable, "-m", "pipeline", "--user", user, "index",
        "--workers", str(workers), "--model", model
    ]
    proc = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
    if proc.returncode != 0:
        return json.dumps({"status": "error", "message": proc.stderr or proc.stdout})
    return json.dumps({"status": "success", "output": proc.stdout[-1500:]})


@app.tool()
def normalize_taxonomy(user: str, threshold: float = 0.70) -> str:
    """Run Jev-powered taxonomy normalization to cluster raw tags into canonical concepts."""
    _, workspace = _get_user_dirs(user)
    api_key = _get_api_key()
    taxonomy = normalize_workspace(workspace, api_key, threshold=threshold)
    summary = {f: len(c) for f, c in taxonomy.items()}
    return json.dumps({"status": "success", "canonical_concepts": summary}, indent=2)


@app.resource("lore://{user}/status")
def resource_status(user: str) -> str:
    """Status and counts of the creator's lore corpus."""
    return get_status(user)


@app.resource("lore://{user}/taxonomy")
def resource_taxonomy(user: str) -> str:
    """Full taxonomy concepts and aliases for the creator."""
    _, workspace = _get_user_dirs(user)
    tax_path = workspace / "taxonomy.json"
    if not tax_path.exists():
        return json.dumps({"error": "Taxonomy not generated yet."})
    return tax_path.read_text(encoding="utf-8")


@app.resource("lore://{user}/scenarios/{slug}")
def resource_scenario(user: str, slug: str) -> str:
    """Authored SKILL.md runtime prompt for a scenario."""
    return read_scenario_skill(user, slug)


def main():
    """Run the MCP server over stdio."""
    app.run(transport="stdio")


if __name__ == "__main__":
    main()
