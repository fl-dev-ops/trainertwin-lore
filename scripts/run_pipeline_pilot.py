"""Bounded live pilot using the current pipeline and explicitly selected inputs.

Uses OPENROUTER_API_KEY from the current repository's .env. No collection, source
editing, hosted telemetry, or semantic/persona scoring. A persistent meter caps the
TOTAL logical requests for this workspace, including reruns and failed requests.
"""

import argparse
import hashlib
import json
import os
import sys
import time
from fnmatch import fnmatchcase
from pathlib import Path

from dotenv import load_dotenv


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--workspace", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--model", default="openai/gpt-4o")
    parser.add_argument("--max-calls", type=int, default=12)
    parser.add_argument("--with-twin", action="store_true")
    parser.add_argument("--author", action="append", default=[])
    parser.add_argument(
        "--include",
        action="append",
        default=[],
        help="Explicit data-root-relative pilot glob; repeat as needed",
    )
    args = parser.parse_args()
    if args.max_calls < 0 or (args.with_twin and not args.author):
        parser.error("Use a nonnegative budget and explicit --author aliases for twin")
    data, ws = args.data.resolve(), args.workspace.resolve()
    if ws.is_relative_to(data) or data.is_relative_to(ws):
        parser.error("Data and workspace must be separate, non-nested directories")
    repo = Path(__file__).resolve().parents[1]
    load_dotenv(repo / ".env")
    sys.path.insert(0, str(repo))
    from pipeline import core
    from pipeline.__main__ import one_writer
    from pipeline.client import OpenRouter
    from pipeline.sources import paths, read_source

    key = os.getenv("OPENROUTER_API_KEY", "")
    if not key:
        parser.error("OPENROUTER_API_KEY is required for this explicitly live pilot")
    ws.mkdir(parents=True, exist_ok=True)
    meter_path = ws / "pilot-meter.json"
    started = time.monotonic()
    stages = []

    class MeteredClient(OpenRouter):
        def complete(self, *call_args, **kwargs):
            self.charge()
            return super().complete(*call_args, **kwargs)

        def charge(self):
            if meter["calls"] >= args.max_calls:
                raise RuntimeError("Pilot lifetime call cap exhausted")
            meter["calls"] += 1
            core.atomic(meter_path, core.js(meter))

    def step(name, fn):
        before = meter["calls"]
        print(f"=== {name} ===", flush=True)
        try:
            fn()
            result = {"stage": name, "status": "completed"}
        except (ValueError, RuntimeError, OSError) as exc:
            result = {"stage": name, "status": "incomplete", "error": str(exc)}
            print(f"{name}: {exc}", flush=True)
        result["new_logical_calls"] = meter["calls"] - before
        stages.append(result)

    available = paths(data)
    for pattern in args.include:
        if not any(
            fnmatchcase(p.relative_to(data).as_posix(), pattern) for p in available
        ):
            parser.error(f"No source matches {pattern!r}")
    selected = [
        p
        for p in available
        if not args.include
        or any(
            fnmatchcase(p.relative_to(data).as_posix(), pattern)
            for pattern in args.include
        )
    ]
    inputs = {
        p.relative_to(data).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in available
    }
    code_hashes = {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted((repo / "pipeline").glob("*.py"))
    }
    with one_writer(ws):
        meter = (
            json.loads(meter_path.read_text()) if meter_path.exists() else {"calls": 0}
        )
        client = MeteredClient(key, args.model)
        try:
            for path in selected:

                def ingest(path=path):
                    source = read_source(path, data)
                    if source:
                        core.ingest_one(
                            source,
                            ws,
                            client,
                            budget=[args.max_calls - meter["calls"]],
                            user_slug="olga",
                        )

                step(f"ingest:{path.relative_to(data)}", ingest)
            step("build", lambda: core.build(ws, data))
            if args.with_twin:
                from pipeline.twin import build_twin

                step(
                    "twin",
                    lambda: build_twin(
                        ws,
                        data,
                        client,
                        authors=args.author,
                        budget=[args.max_calls - meter["calls"]],
                        max_sources=8,
                    ),
                )
            step("analyze", lambda: core.analyze(ws, user="olga"))
            step("lint", lambda: core.lint(ws, data))
        finally:
            client.close()

    manifests = [core.load_json(p) for p in (ws / "manifest").glob("*.json")]
    usage_file = ws / "usage.jsonl"
    usage = (
        [
            json.loads(line)
            for line in usage_file.read_text().splitlines()
            if line.strip()
        ]
        if usage_file.exists()
        else []
    )
    final_inputs = {
        p.relative_to(data).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in paths(data)
    }
    report = {
        "mode": "live OpenRouter pilot; not semantic/persona scoring",
        "model": args.model,
        "code_root": str(repo),
        "workspace": str(ws),
        "code_sha256": code_hashes,
        "input_sha256": inputs,
        "selected_inputs": [p.relative_to(data).as_posix() for p in selected],
        "inputs_unchanged": inputs == final_inputs,
        "total_call_cap": args.max_calls,
        "total_logical_calls": meter["calls"],
        "elapsed_seconds": round(time.monotonic() - started, 2),
        "stages": stages,
        "active_sources": len(manifests),
        "records": sum(m["evidence_count"] for m in manifests),
        "source_snapshots": len(list((ws / "sources").glob("*.json"))),
        "topic_pages": len(list((ws / "wiki" / "topics").glob("*.md"))),
        "processing_quality": [
            m.get("quality", {"status": "not_recorded"}) for m in manifests
        ],
        "usage": usage,
        "not_measured": [
            "semantic correctness",
            "extraction recall",
            "trainer resemblance",
            "chat response latency/cost",
        ],
    }
    twin_record = ws / "twin" / "profile.json"
    if twin_record.exists():
        twin = core.load_json(twin_record)
        report["twin"] = {
            "coverage": twin["coverage"],
            "patterns": len(twin["patterns"]),
            "review_status": twin["observation_review"],
        }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(core.js(report))
    print(
        core.js(
            {
                k: v
                for k, v in report.items()
                if k not in {"usage", "code_sha256", "input_sha256"}
            }
        )
    )
    if not report["inputs_unchanged"] or any(
        s["status"] != "completed" for s in stages
    ):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
