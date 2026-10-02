"""Index captured posts and transcripts into one list."""

import argparse
import math
import os
from fnmatch import fnmatchcase
from pathlib import Path

import httpx
from dotenv import load_dotenv

from .client import OpenRouter, SpendBudget
from .index import index_paths, plan

ROOT = Path(__file__).resolve().parents[1]
EXTENSIONS = {".md", ".markdown", ".txt", ".yaml", ".yml"}


def model_client(model: str) -> OpenRouter:
    load_dotenv(ROOT / ".env")
    key = os.getenv("OPENROUTER_API_KEY", "")
    if not key or not model:
        raise ValueError("Set OPENROUTER_API_KEY and --model")
    return OpenRouter(key, model)


def selected_paths(root: Path, patterns, limit):
    available = sorted(
        p
        for p in root.rglob("*")
        if p.is_file()
        and not p.is_symlink()
        and p.suffix.lower() in EXTENSIONS
        and not any(part.startswith(".") or part == "__pycache__" for part in p.relative_to(root).parts)
    )
    for pattern in patterns or []:
        if not any(fnmatchcase(p.relative_to(root).as_posix(), pattern) for p in available):
            raise ValueError(f"No source matches --include {pattern!r}")
    selected = [
        p
        for p in available
        if not patterns or any(fnmatchcase(p.relative_to(root).as_posix(), g) for g in patterns)
    ]
    if limit is not None and limit < 1:
        raise ValueError("--limit must be positive")
    return selected[:limit] if limit is not None else selected


def cli():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--user", default="olga")
    parser.add_argument("--data", type=Path)
    parser.add_argument("--workspace", type=Path)
    subparsers = parser.add_subparsers(dest="command", required=True)

    command = subparsers.add_parser("index")
    command.add_argument("--model", default="google/gemini-3.8-flash")
    command.add_argument("--max-calls", type=int, default=500)
    command.add_argument("--max-output-tokens", type=int, default=65536)
    command.add_argument("--workers", type=int, default=1)
    command.add_argument("--reasoning-effort", choices=("minimal", "low", "medium", "high"), default="low")
    command.add_argument("--include", action="append")
    command.add_argument("--limit", type=int)
    command.add_argument("--dry-run", action="store_true")
    command.add_argument("--no-normalize", action="store_true", help="Skip automatic taxonomy normalization after indexing")
    command.add_argument("--max-usd", type=float)
    command.add_argument("--input-price", type=float)
    command.add_argument("--output-price", type=float)

    norm = subparsers.add_parser("normalize")
    norm.add_argument("--threshold", type=float, default=0.70)

    query_cmd = subparsers.add_parser("query")
    query_cmd.add_argument("query_text", help="Scenario or question to retrieve grounding clips for")
    query_cmd.add_argument("--max-clips", type=int, default=5)

    author_cmd = subparsers.add_parser("author")
    author_cmd.add_argument("scenario", help="Scenario description to author a prompt for")
    author_cmd.add_argument("--model", default="google/gemini-3.8-flash")
    author_cmd.add_argument("--output", type=Path)

    val_cmd = subparsers.add_parser("validate")
    val_cmd.add_argument("scenario_file", nargs="?", help="Specific scenario file to validate (or all if omitted)")
    val_cmd.add_argument("--judge-model", default="openai/gpt-4o-mini")

    args = parser.parse_args()
    root = (args.data or ROOT / "users" / args.user / "data").resolve()
    workspace = (args.workspace or ROOT / "users" / args.user / "workspace").resolve()

    if args.command == "normalize":
        load_dotenv(ROOT / ".env")
        key = os.getenv("OPENROUTER_API_KEY", "")
        if not key:
            parser.error("OPENROUTER_API_KEY required")
        from .normalize import normalize_workspace
        normalize_workspace(workspace, key, threshold=args.threshold)
        return

    if args.command == "query":
        load_dotenv(ROOT / ".env")
        key = os.getenv("OPENROUTER_API_KEY", "")
        if not key:
            parser.error("OPENROUTER_API_KEY required")
        from .retrieve import retrieve
        res = retrieve(workspace, root, args.query_text, key, max_clips=args.max_clips)
        print(f"\nTarget Scenario: \"{res['query']}\"")
        print(f"Matched Concept: {res['matched_concept']} (Confidence: {res['concept_confidence']})")
        if res['aliases_used']:
            print(f"Aliases Used: {res['aliases_used']}")
        print(f"\nRetrieved {len(res['clips'])} Grounding Clips:\n" + "=" * 60)
        for i, c in enumerate(res['clips'], 1):
            print(f"\nClip {i}: \"{c['title']}\" [Score: {c['retrieval_score']}]")
            print(f"  File: {c['path']} (lines {c['span']['start_line']}-{c['span']['end_line']})")
            print(f"  Tags: {c['tags']}")
            print(f"  Verbatim:\n    \"{c['verbatim_text'][:260]}...\"")
        return

    if args.command == "author":
        load_dotenv(ROOT / ".env")
        key = os.getenv("OPENROUTER_API_KEY", "")
        if not key:
            parser.error("OPENROUTER_API_KEY required")
        from .author import author_scenario_prompt
        out_path, content = author_scenario_prompt(
            workspace, root, args.scenario, key, model=args.model, output_path=args.output
        )
        print(f"\nScenario prompt authored successfully: {out_path}\n" + "=" * 60)
        print(content)
        return

    if args.command == "validate":
        load_dotenv(ROOT / ".env")
        key = os.getenv("OPENROUTER_API_KEY", "")
        if not key:
            parser.error("OPENROUTER_API_KEY required")
        from .validate import validate_scenario
        scenarios_dir = workspace / "scenarios"
        if not scenarios_dir.is_dir():
            parser.error(f"No scenarios directory found at {scenarios_dir}")

        files_to_validate = (
            [scenarios_dir / args.scenario_file] if args.scenario_file
            else sorted(scenarios_dir.glob("*.md"))
        )
        for sf in files_to_validate:
            print(f"\n{'='*70}\nVALIDATING: {sf.name}\n{'='*70}")
            report = validate_scenario(sf, root, key, judge_model=args.judge_model)
            je = report["judge_evaluation"]
            ci = report["citation_integrity"]
            print(f"VERDICT: {je['verdict']} | Grounding: {je['grounding_score']}/10 | Voice: {je['voice_authenticity_score']}/10 | Gemini Readiness: {je['gemini_adherence_readiness']}/10")
            print(f"Citations: {ci['valid_citations']}/{ci['total_citations']} valid")
            if je.get("hallucinations_found"):
                print(f"⚠️ Hallucinations: {je['hallucinations_found']}")
            if je.get("unsupported_claims"):
                print(f"⚠️ Unsupported Claims: {je['unsupported_claims']}")
            print(f"\nSummary:\n  {je['summary']}\n")
        return

    if not root.is_dir():
        parser.error(f"Data directory not found: {root}")
    if args.max_calls < 0 or args.workers < 1 or args.max_output_tokens < 1:
        parser.error("Invalid limit")
    if args.max_usd is not None and (args.input_price is None or args.output_price is None):
        parser.error("--max-usd requires --input-price and --output-price")
    for value in (args.max_usd, args.input_price, args.output_price):
        if value is not None and (not math.isfinite(value) or value < 0):
            parser.error("Prices and the dollar cap must be finite and nonnegative")
    selected = selected_paths(root, args.include, args.limit)
    if args.dry_run:
        for path in selected:
            mode, _ = plan(path.read_text())
            print(f"{path.relative_to(root)}: {mode}")
        return
    model = model_client(args.model)
    budget = [args.max_calls]
    clients = [model]
    try:
        model.max_output_tokens = args.max_output_tokens
        model.reasoning_effort = args.reasoning_effort
        if args.max_usd is not None:
            model.spend_budget = SpendBudget(
                args.max_usd, args.input_price, args.output_price, workspace / "spend.json"
            )
        for _ in range(args.workers - 1):
            client = model_client(args.model)
            client.max_output_tokens = model.max_output_tokens
            client.reasoning_effort = model.reasoning_effort
            client.spend_budget = model.spend_budget
            clients.append(client)
        index_paths(selected, root, workspace, model, budget, workers=args.workers, clients=clients)
    finally:
        for client in clients:
            client.close()
    print(f"Calls left: {budget[0]}")

    if not getattr(args, "no_normalize", False):
        load_dotenv(ROOT / ".env")
        key = os.getenv("OPENROUTER_API_KEY", "")
        if key:
            from .normalize import normalize_workspace
            normalize_workspace(workspace, key, workers=args.workers)


def main():
    try:
        cli()
    except (ValueError, RuntimeError, OSError, httpx.HTTPError) as exc:
        raise SystemExit(f"Pipeline error: {exc}") from exc


if __name__ == "__main__":
    main()
