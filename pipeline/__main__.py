"""TrainerTwin research pipeline: source products, wiki, twin, context and audit."""

import argparse
import math
import os
import re
from fnmatch import fnmatchcase
from pathlib import Path
from urllib.parse import urlparse

import httpx
import yaml
from dotenv import load_dotenv

from .client import ModelError, OpenRouter, ProviderBlocked, SpendBudget
from .core import active_records, analyze, build, ingest_one, lint, read_records
from .sources import SOURCE_FORMAT_VERSION, chunks, paths, read_source, source_id
from .storage import SCHEMA_VERSION, append, js, load_json, log, one_writer, stamp

ROOT = Path(__file__).resolve().parents[1]


def model_client(model: str) -> OpenRouter:
    load_dotenv(ROOT / ".env")
    key = os.getenv("OPENROUTER_API_KEY", "")
    if not key or not model:
        raise ValueError(
            "Set OPENROUTER_API_KEY and OPENROUTER_MODEL (or --model) for paid stages"
        )
    return OpenRouter(key, model)


def selected_paths(root, patterns, limit):
    available = paths(root)
    for pattern in patterns or []:
        if not any(
            fnmatchcase(p.relative_to(root).as_posix(), pattern) for p in available
        ):
            raise ValueError(f"No source matches --include {pattern!r}")
    selected = [
        p
        for p in available
        if not patterns
        or any(fnmatchcase(p.relative_to(root).as_posix(), g) for g in patterns)
    ]
    if limit is not None and limit < 1:
        raise ValueError("--limit must be positive")
    return selected[:limit] if limit is not None else selected


def ingest_paths(
    selected, root, workspace, model, budget, chunk_chars, *, retry_failed=False
):
    failures = []
    for path in selected:
        try:
            source = read_source(path, root)
            if source is None:
                print(f"{path.relative_to(root)}: metadata-only / empty source skipped")
                continue
            changed = ingest_one(
                source,
                workspace,
                model,
                budget=budget,
                max_chars=chunk_chars,
                retry_failed=retry_failed,
            )
            print(
                f"{source.id}: {'ingested' if changed else 'unchanged'}; {budget[0]} calls left",
                flush=True,
            )
        except (
            ValueError,
            RuntimeError,
            OSError,
            yaml.YAMLError,
            httpx.HTTPError,
        ) as exc:
            failures.append(path)
            log(workspace, f"source-incomplete | {path.relative_to(root)} | {exc}")
            print(f"{path.relative_to(root)}: incomplete ({exc})", flush=True)
            if isinstance(exc, (ProviderBlocked, ModelError)):
                raise
            if "Call budget exhausted" in str(exc):
                break
    if failures:
        raise RuntimeError(
            f"Ingestion incomplete for {len(failures)} source(s); validated windows remain cached"
        )


def cli():
    load_dotenv(ROOT / ".env")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--user", default="olga")
    parser.add_argument("--data", type=Path)
    parser.add_argument("--workspace", type=Path)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("status", "analyze", "audit-grounding"):
        sub.add_parser(name)
    preflight = sub.add_parser(
        "plan", help="Offline window/cache/cost preflight; no model requests"
    )
    preflight.add_argument("--stage", choices=("ingest", "organize"), default="ingest")
    preflight.add_argument("--model", default=os.getenv("OPENROUTER_MODEL", ""))
    preflight.add_argument("--chunk-chars", type=int, default=24000)
    preflight.add_argument("--include", action="append")
    preflight.add_argument("--limit", type=int)
    preflight.add_argument("--retry-failed", action="store_true")
    preflight.add_argument(
        "--input-price",
        type=float,
        help="USD per million input tokens; operator-supplied",
    )
    preflight.add_argument(
        "--output-price",
        type=float,
        help="USD per million output tokens; operator-supplied",
    )
    preflight.add_argument("--max-output-tokens", type=int, default=8192)
    preflight.add_argument(
        "--seconds-per-call",
        type=float,
        help="Measured request duration for ETA, otherwise unknown",
    )
    lint_parser = sub.add_parser("lint")
    lint_parser.add_argument(
        "--require-complete",
        action="store_true",
        help="Fail if corpus ingestion or linked-wiki organization is incomplete",
    )
    lint_parser.add_argument(
        "--wiki-only",
        action="store_true",
        help="Check wiki and source integrity without requiring later reports/twin to be rebuilt",
    )
    browse = sub.add_parser(
        "browse", help="Search the structured wiki catalog, offline"
    )
    browse.add_argument("query", nargs="?", default="")
    browse.add_argument(
        "--kind",
        choices=("sources", "topics", "entities", "methods", "episodes", "expression"),
    )
    for name in ("platform", "activity", "part", "role"):
        browse.add_argument("--" + name)
    browse.add_argument("--limit", type=int, default=20)
    sub.add_parser(
        "build", help="Render all three information products into a wiki, offline"
    )
    for name in ("ingest", "organize", "twin", "audit", "run"):
        command = sub.add_parser(name)
        command.add_argument("--model", default=os.getenv("OPENROUTER_MODEL", ""))
        command.add_argument(
            "--max-calls", type=int, default=20 if name in {"ingest", "run"} else 8
        )
        command.add_argument(
            "--chunk-chars",
            type=int,
            default=32000
            if name == "audit"
            else 24000
            if name in {"twin", "organize"}
            else 15000,
        )
        command.add_argument(
            "--retry-failed",
            action="store_true",
            help="Explicitly retry quarantined failed requests",
        )
        command.add_argument(
            "--max-usd",
            type=float,
            help="Persistent workspace dollar ceiling; raise explicitly to extend it",
        )
        command.add_argument(
            "--input-price",
            type=float,
            help="USD per million input tokens; required with --max-usd",
        )
        command.add_argument(
            "--output-price",
            type=float,
            help="USD per million output tokens; required with --max-usd",
        )
        command.add_argument("--max-output-tokens", type=int, default=8192)
        if name in {"ingest", "organize", "run"}:
            command.add_argument("--include", action="append")
            command.add_argument("--limit", type=int)
        if name in {"twin", "run"}:
            command.add_argument("--author", action="append", required=True)
            command.add_argument("--max-sources", type=int, default=12)
            command.add_argument("--reviewed-only", action="store_true")
        if name != "audit":
            command.add_argument("--dry-run", action="store_true")
        else:
            command.add_argument("--record-id", action="append")
    context = sub.add_parser(
        "context",
        help="Select complete task-relevant records and original context, offline",
    )
    context.add_argument("query")
    context.add_argument("--author", action="append")
    context.add_argument("--platform")
    context.add_argument(
        "--as-of",
        help="Only sources published on/before YYYY-MM-DD; undated sources excluded",
    )
    context.add_argument("--max-records", type=int, default=8)
    context.add_argument("--max-chars", type=int, default=24000)
    context.add_argument("--reviewed-only", action="store_true")
    review = sub.add_parser(
        "review",
        help="Record HUMAN source-support review; unsupported records are withheld from serving views",
    )
    review.add_argument("--record-id", required=True)
    review.add_argument(
        "--status", choices=("supported", "unsupported", "uncertain"), required=True
    )
    review.add_argument("--note", required=True)
    verify = sub.add_parser(
        "verify", help="Record scoped HUMAN external fact review; never fetches a URL"
    )
    verify.add_argument("--evidence-id", required=True)
    verify.add_argument("--status", choices=("verified", "contradicted"), required=True)
    verify.add_argument("--note", required=True)
    verify.add_argument("--url", required=True)
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.user):
        parser.error("--user must be a lowercase slug")
    if (args.data is None) != (args.workspace is None):
        parser.error("--data and --workspace must be supplied together")
    root = (args.data or ROOT / "users" / args.user / "data").resolve()
    workspace = (args.workspace or ROOT / "users" / args.user / "workspace").resolve()
    if not root.is_dir():
        parser.error(f"Data directory not found: {root}")
    if root.is_relative_to(workspace) or workspace.is_relative_to(root):
        parser.error("Data and workspace must be separate, non-nested directories")
    if getattr(args, "max_calls", 0) < 0 or getattr(args, "chunk_chars", 15000) < 1000:
        parser.error("Use nonnegative --max-calls and --chunk-chars >= 1000")
    if getattr(args, "max_sources", 1) < 1:
        parser.error("--max-sources must be positive")
    for field in ("max_usd", "input_price", "output_price", "seconds_per_call"):
        value = getattr(args, field, None)
        if value is not None and (not math.isfinite(value) or value < 0):
            parser.error(f"--{field.replace('_', '-')} must be finite and nonnegative")
    if getattr(args, "max_output_tokens", 1) < 1:
        parser.error("--max-output-tokens must be positive")
    if getattr(args, "max_usd", None) is not None and (
        args.input_price is None or args.output_price is None
    ):
        parser.error("--max-usd requires explicit --input-price and --output-price")
    if args.command == "plan":
        from .execution import plan

        print(
            js(
                plan(
                    workspace,
                    root,
                    selected_paths(root, args.include, args.limit),
                    args.model,
                    args.stage,
                    args.chunk_chars,
                    input_price=args.input_price,
                    output_price=args.output_price,
                    max_output_tokens=args.max_output_tokens,
                    seconds_per_call=args.seconds_per_call,
                    retry_failed=args.retry_failed,
                )
            ),
            end="",
        )
        return
    if args.command == "audit-grounding":
        from .execution import audit_grounding

        result = audit_grounding(workspace)
        print(js(result), end="")
        if not result["passed"]:
            raise RuntimeError(
                "Stored records failed strict grounding audit; no data changed"
            )
        return
    if args.command == "status":
        available = {source_id(p, root): p for p in paths(root)}
        manifests = list((workspace / "manifest").glob("*.json"))
        stale = []
        for path in manifests:
            try:
                meta = load_json(path)
                source = (
                    read_source(available[path.stem], root)
                    if path.stem in available
                    else None
                )
                if (
                    not source
                    or meta.get("version") != SCHEMA_VERSION
                    or meta.get("source_format") != SOURCE_FORMAT_VERSION
                    or meta["source_sha256"] != source.sha256
                    or meta.get("metadata_hash") != source.metadata_hash
                ):
                    stale.append(path.stem)
            except (ValueError, OSError, yaml.YAMLError):
                stale.append(path.stem)
        from .execution import completeness

        print(
            js(
                {
                    "files": len(available),
                    "ingested": len(manifests),
                    "stale": stale,
                    "processing": completeness(workspace, root),
                }
            ),
            end="",
        )
        return
    if args.command == "lint":
        from .execution import completeness

        result = lint(workspace, root, wiki_only=args.wiki_only)
        result["processing"] = completeness(workspace, root)
        catalog = workspace / "wiki/catalog.json"
        coverage = load_json(catalog)["coverage"] if catalog.exists() else {}
        result["organization"] = coverage
        print(js(result), end="")
        if args.require_complete and (
            not result["processing"]["ingestion_complete"]
            or coverage.get("unorganized_sources", 1)
            or not coverage.get("topic_aliases_organized")
        ):
            raise RuntimeError(
                "Artifacts checked, but requested corpus processing is incomplete"
            )
        return
    if args.command == "browse":
        from .wiki import browse as browse_wiki

        active_records(workspace, root)  # Refuse stale source-backed results.
        print(
            js(
                browse_wiki(
                    workspace,
                    args.query,
                    kind=args.kind,
                    platform=args.platform,
                    activity=args.activity,
                    part=args.part,
                    role=args.role,
                    limit=args.limit,
                )
            ),
            end="",
        )
        return
    if args.command == "context":
        from .context import select_context

        print(
            js(
                select_context(
                    workspace,
                    root,
                    args.query,
                    authors=args.author,
                    platform=args.platform,
                    max_records=args.max_records,
                    max_chars=args.max_chars,
                    as_of=args.as_of,
                    reviewed_only=args.reviewed_only,
                )
            ),
            end="",
        )
        return
    if args.command in {"build", "analyze", "review", "verify"}:
        with one_writer(workspace):
            if args.command == "build":
                print(build(workspace, root))
            elif args.command == "analyze":
                print(analyze(workspace, user=args.user, source_dir=root))
            else:
                if not args.note.strip():
                    parser.error("A meaningful review note is required")
                records, _ = read_records(workspace, root)
                ident = args.record_id if args.command == "review" else args.evidence_id
                record = next((r for r in records if r["id"] == ident), None)
                if record is None:
                    parser.error("Unknown or inactive record ID")
                if args.command == "review":
                    append(
                        workspace / "reviews.jsonl",
                        {
                            "record_id": ident,
                            "status": args.status,
                            "note": args.note,
                            "checked_at": stamp(),
                        },
                    )
                else:
                    parsed = urlparse(args.url)
                    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
                        parser.error("A public HTTP(S) source URL is required")
                    if record["product"] != "knowledge" or record["content"][
                        "kind"
                    ] not in {"claim", "self_report"}:
                        parser.error(
                            "External fact review applies to knowledge claims and self-reports"
                        )
                    append(
                        workspace / "verifications.jsonl",
                        {
                            "evidence_id": ident,
                            "status": args.status,
                            "note": args.note,
                            "url": args.url,
                            "checked_at": stamp(),
                        },
                    )
                print(
                    "Recorded human review; rebuild affected wiki/twin/audit/report artifacts"
                )
        return
    selected = (
        selected_paths(root, args.include, args.limit)
        if args.command in {"ingest", "run"}
        else []
    )
    if getattr(args, "dry_run", False):
        if args.command == "organize":
            from .organization import (
                organization_windows,
                selected_sources,
                source_units,
            )

            _, sources = active_records(workspace, root)
            for source in selected_sources(sources, args.include, args.limit):
                print(
                    f"{source.relative_path}: {len(organization_windows(source_units(source), args.chunk_chars))} organization windows"
                )
            return
        if args.command == "twin":
            from .twin import prepare_examples

            records, sources = active_records(workspace, root)
            _, coverage = prepare_examples(
                records,
                sources,
                args.author,
                args.max_sources,
                reviewed_only=args.reviewed_only,
            )
            print(js(coverage), end="")
        else:
            errors = []
            for path in selected:
                try:
                    source = read_source(path, root)
                    print(
                        f"{path.relative_to(root)}: {len(chunks(source, args.chunk_chars)) if source else 0} extraction windows"
                    )
                except (ValueError, OSError, yaml.YAMLError) as exc:
                    errors.append(str(exc))
                    print(f"{path.relative_to(root)}: invalid ({exc})")
            if errors:
                raise RuntimeError("Dry run found invalid source files")
        return
    with one_writer(workspace):
        model = model_client(args.model)
        budget = [args.max_calls]
        try:
            model.max_output_tokens = args.max_output_tokens
            if args.max_usd is not None:
                model.spend_budget = SpendBudget(
                    args.max_usd,
                    args.input_price,
                    args.output_price,
                    workspace / "work/spend.json",
                )
            if args.command == "organize":
                from .organization import organize

                print(
                    organize(
                        workspace,
                        root,
                        model,
                        budget=budget,
                        patterns=args.include,
                        limit=args.limit,
                        max_chars=args.chunk_chars,
                        retry_failed=args.retry_failed,
                    )
                )
            if args.command in {"ingest", "run"}:
                ingest_paths(
                    selected,
                    root,
                    workspace,
                    model,
                    budget,
                    args.chunk_chars,
                    retry_failed=args.retry_failed,
                )
            if args.command == "run":
                build(workspace, root)
            if args.command in {"twin", "run"}:
                from .twin import build_twin

                print(
                    build_twin(
                        workspace,
                        root,
                        model,
                        authors=args.author,
                        budget=budget,
                        max_sources=args.max_sources,
                        max_chars=args.chunk_chars,
                        reviewed_only=args.reviewed_only,
                        retry_failed=args.retry_failed,
                    )
                )
            if args.command == "run":
                print(analyze(workspace, user=args.user, source_dir=root))
                print(js(lint(workspace, root)), end="")
            if args.command == "audit":
                from .audit import audit_records

                print(
                    audit_records(
                        workspace,
                        root,
                        model,
                        budget=budget,
                        record_ids=args.record_id,
                        max_chars=args.chunk_chars,
                        retry_failed=args.retry_failed,
                    )
                )
        finally:
            model.close()
        print(f"New logical calls: {args.max_calls - budget[0]} / {args.max_calls}")


def main():
    try:
        cli()
    except (ValueError, RuntimeError, OSError, yaml.YAMLError, httpx.HTTPError) as exc:
        raise SystemExit(f"Pipeline error: {exc}") from exc


if __name__ == "__main__":
    main()
