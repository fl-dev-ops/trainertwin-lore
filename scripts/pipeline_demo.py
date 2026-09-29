"""Exercise the current pipeline offline using fixture-authored model output.

Run: uv run python scripts/pipeline_demo.py --output /tmp/trainertwin-demo
No API client is constructed. This checks plumbing and retention, not LLM quality.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pipeline.audit import audit_records
from pipeline.context import select_context
from pipeline.core import analyze, build, ingest_one, lint, read_records
from pipeline.sources import read_source
from pipeline.storage import atomic, js, load_json, one_writer
from pipeline.tests.helpers import FakeModel, post, transcript
from pipeline.twin import build_twin


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists():
        parser.error(
            "Use a new output directory; the demo never overwrites an existing run"
        )
    data, workspace = output / "data", output / "workspace"
    inputs = [
        post(data, "method"),
        post(
            data,
            "reported-case",
            body="I described this client exchange yesterday.\nClient: Can I get a discount?\nMe: What would you do with five buyers?\n",
        ),
        transcript(data / "interview"),
    ]
    model = FakeModel()
    budget = [10]
    with one_writer(workspace):
        for path in inputs:
            ingest_one(read_source(path, data), workspace, model, budget=budget)
        build(workspace, data)
        build_twin(workspace, data, model, authors=["jane"], budget=budget)
        audit_records(workspace, data, model, budget=budget)
        analyze(workspace, user="fixture-jane", source_dir=data)
        checks = lint(workspace, data)
        context = select_context(
            workspace,
            data,
            "spontaneous thinking exercise time limit",
            authors=["jane"],
        )
        atomic(output / "context.json", js(context))
        records, _ = read_records(workspace, data)
        method = next(
            r
            for r in records
            if r["product"] == "knowledge" and r["content"]["kind"] == "method"
        )
        assert len(method["content"]["steps"]) == 4
        assert method["content"]["constraints"][0]["text"] == "A 60-second time limit."
        cases = [r["content"] for r in records if r["product"] == "cases"]
        assert {c["kind"] for c in cases} == {"reported_exchange", "recorded_exchange"}
        assert all(c["rationale"] is None and c["outcome"] is None for c in cases)
        assert any(c["response"]["text"] == "Never." for c in cases)
        assert context["knowledge"] and not context["abstain"]
        calls = model.calls
        build(workspace, data)
        build_twin(workspace, data, model, authors=["jane"], budget=[0])
        audit_records(workspace, data, model, budget=[0])
        analyze(workspace, user="fixture-jane", source_dir=data)
        lint(workspace, data)
        assert model.calls == calls
    result = {
        "validation": "offline_fixture_only_not_live_model_quality",
        "paid_calls": 0,
        "fixture_model_calls": calls,
        "cached_rebuild_calls": model.calls - calls,
        "checks": checks,
        "audit": load_json(workspace / "audit/checks.json")["summary"],
        "retention_assertions": [
            "four ordered method steps",
            "60-second constraint",
            "reported/recorded cases distinct",
            "unknown rationales/outcomes remain null",
            "Never. preserved",
            "task-selected knowledge",
            "zero-call cached rebuild",
        ],
    }
    atomic(output / "result.json", js(result))
    atomic(
        output / "README.md",
        "# Offline TrainerTwin fixture demo\n\nThese sources and model responses are test fixtures, not a real trainer evaluation. No paid calls.\n\nSee `workspace/wiki/index.md`, `workspace/twin/profile.md`, `workspace/audit/report.md`, `context.json`, and `result.json`.\n",
    )
    print(js(result), end="")
    print(f"Artifacts: {output}")


if __name__ == "__main__":
    main()
