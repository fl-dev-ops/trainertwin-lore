"""Command-line interface: uv run python -m pipeline --help."""

import argparse
import fcntl
import json
import os
import re
from contextlib import contextmanager
from fnmatch import fnmatchcase
from pathlib import Path

import httpx
from dotenv import load_dotenv

from .client import OpenRouter
from .core import (
    analyze,
    build,
    chunks,
    ingest_one,
    js,
    lint,
    load_json,
    log,
    read_cards,
    read_source,
    stamp,
)
from .sources import paths, source_id

ROOT = Path(__file__).resolve().parents[1]


@contextmanager
def one_writer(workspace: Path):
    workspace.mkdir(parents=True, exist_ok=True)
    with (workspace / ".lock").open("w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        try:
            yield
        finally:
            fcntl.flock(lock, fcntl.LOCK_UN)


def model_client(model: str) -> OpenRouter:
    load_dotenv(ROOT / ".env")
    key = os.getenv("OPENROUTER_API_KEY", "")
    if not key:
        raise ValueError(
            "OPENROUTER_API_KEY is missing; add it to .env before paid ingestion"
        )
    if not model:
        raise ValueError(
            "Choose a structured-output-capable --model (or OPENROUTER_MODEL)"
        )
    return OpenRouter(key, model)


def cli() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--user",
        default="olga",
        help="User directory name under users/ (default: olga)",
    )
    parser.add_argument(
        "--data",
        type=Path,
        help="Override recursive text source root (requires --workspace)",
    )
    parser.add_argument(
        "--workspace", type=Path, help="Override workspace (requires --data)"
    )
    sub = parser.add_subparsers(dest="command", required=True)
    ingest = sub.add_parser("ingest", help="Resumable source-grounded extraction")
    ingest.add_argument("--model", default=os.getenv("OPENROUTER_MODEL", ""))
    ingest.add_argument(
        "--include",
        action="append",
        help="Root-relative file glob; repeat for a pilot (e.g. youtube/transcripts/06.yaml)",
    )
    ingest.add_argument(
        "--limit", type=int, help="Only process first N selected sources"
    )
    ingest.add_argument("--chunk-chars", type=int, default=15000)
    ingest.add_argument(
        "--max-calls",
        type=int,
        default=20,
        help="Max NEW logical LLM calls in this invocation (default: 20)",
    )
    ingest.add_argument(
        "--dry-run",
        action="store_true",
        help="Inspect planned chunks; no key or API calls",
    )
    build_cmd = sub.add_parser(
        "build", help="Incrementally maintain Markdown wiki pages"
    )
    build_cmd.add_argument("--model", default=os.getenv("OPENROUTER_MODEL", ""))
    build_cmd.add_argument("--chunk-chars", type=int, default=15000)
    build_cmd.add_argument("--max-calls", type=int, default=20)
    sub.add_parser(
        "analyze", help="Compile a report from the saved wiki only (offline)"
    )
    sub.add_parser(
        "lint", help="Check references, freshness, and synthesis IDs offline"
    )
    sub.add_parser("status", help="Show ingestion coverage offline")
    verify = sub.add_parser(
        "verify", help="Record HUMAN-reviewed external evidence; never auto-verifies"
    )
    verify.add_argument("--evidence-id", required=True)
    verify.add_argument("--status", choices=("verified", "contradicted"), required=True)
    verify.add_argument(
        "--url", required=True, help="Public external evidence URL, checked by a human"
    )
    verify.add_argument(
        "--note", required=True, help="What exactly was checked, and any qualification"
    )
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.user):
        parser.error("--user must be a lowercase slug (e.g. jane-doe)")
    if (args.data is None) != (args.workspace is None):
        parser.error("--data and --workspace must be supplied together")
    user_root = ROOT / "users" / args.user
    source_dir = (args.data or user_root / "data").resolve()
    workspace = (args.workspace or user_root / "workspace").resolve()
    if not source_dir.is_dir():
        parser.error(f"Data directory not found: {source_dir}")
    if args.command == "status":
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
        print(f"files={len(available)} ingested={len(manifests)} stale={stale}")
        return
    if args.command == "lint":
        print(js(lint(workspace, source_dir)), end="")
        return
    if args.command == "analyze":
        with one_writer(workspace):
            lint(workspace, source_dir, check_report=False)
            report = analyze(workspace, user=args.user if args.data is None else "")
            lint(workspace, source_dir)
        print(f"Compiled {report}")
        return
    if args.command == "verify":
        if not args.url.startswith(("http://", "https://")) or not args.note.strip():
            parser.error("A public http(s) URL and meaningful note are required")
        with one_writer(workspace):
            cards, _ = read_cards(workspace, source_dir)
            selected = next((c for c in cards if c["id"] == args.evidence_id), None)
            if not selected:
                parser.error("Unknown or stale evidence ID")
            if selected["kind"] not in ("fact_claim", "self_report", "case_study"):
                parser.error(
                    "External fact verification applies only to fact claims/self-reports/case studies"
                )
            record = {
                "evidence_id": args.evidence_id,
                "status": args.status,
                "url": args.url,
                "note": args.note,
                "checked_at": stamp(),
            }
            with (workspace / "verifications.jsonl").open("a", encoding="utf-8") as out:
                out.write(json.dumps(record, ensure_ascii=False) + "\n")
        print("Recorded human review; rebuild to reflect it in wiki pages")
        return
    if args.max_calls < 0 or args.chunk_chars < 1000:
        parser.error("--max-calls must be nonnegative and --chunk-chars >= 1000")
    if args.command == "ingest":
        selected = paths(source_dir)
        if args.include:
            for pattern in args.include:
                if not any(
                    fnmatchcase(p.relative_to(source_dir).as_posix(), pattern)
                    for p in selected
                ):
                    parser.error(f"No source matches --include {pattern!r}")
            selected = [
                p
                for p in selected
                if any(
                    fnmatchcase(p.relative_to(source_dir).as_posix(), pattern)
                    for pattern in args.include
                )
            ]
        if args.limit is not None:
            if args.limit < 1:
                parser.error("--limit must be positive")
            selected = selected[: args.limit]
        sources = [s for p in selected if (s := read_source(p, source_dir))]
        if args.dry_run:
            for s in sources:
                print(
                    f"{s.path.relative_to(source_dir)}: {len(chunks(s, args.chunk_chars))} chunks · {s.title}"
                )
            print(
                f"{len(sources)} sources; {sum(len(chunks(s, args.chunk_chars)) for s in sources)} maximum uncached extraction calls; {len(selected) - len(sources)} metadata-only files skipped"
            )
            return
        with one_writer(workspace):
            client = model_client(args.model)
            try:
                budget = [args.max_calls]
                for source in sources:
                    try:
                        changed = ingest_one(
                            source,
                            workspace,
                            client,
                            max_chars=args.chunk_chars,
                            budget=budget,
                            user_slug=args.user,
                        )
                        status_label = (
                            "ingested"
                            if changed
                            else (
                                "unchanged"
                                if (
                                    workspace / "manifest" / f"{source.id}.json"
                                ).exists()
                                else "skipped (repost / not target author)"
                            )
                        )
                        print(
                            f"{source.id}: {status_label} (calls left: {budget[0]})",
                            flush=True,
                        )
                    except (ValueError, RuntimeError, httpx.HTTPError) as exc:
                        # One bad source must not kill a 1,600-source run.
                        log(workspace, f"rejected-source | {source.id} | {exc}")
                        print(f"{source.id}: skipped ({exc})", flush=True)
                    if budget[0] <= 0:
                        break
            finally:
                client.close()
    elif args.command == "build":
        with one_writer(workspace):
            client = model_client(args.model)
            try:
                build(
                    workspace,
                    source_dir,
                    client,
                    budget=[args.max_calls],
                    max_chars=args.chunk_chars,
                )
            finally:
                client.close()
        print(
            f"Updated {workspace / 'wiki' / 'index.md'}; run analyze separately for a report"
        )


def main() -> None:
    try:
        cli()
    except (ValueError, RuntimeError, BlockingIOError) as exc:
        raise SystemExit(f"Pipeline error: {exc}") from exc


if __name__ == "__main__":
    main()

