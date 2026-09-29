"""Optional field-level source-support diagnostics, not a holistic persona score."""

from collections import Counter
from pathlib import Path

from . import prompts
from .core import artifact_inputs, escaped, link, read_records
from .records import (
    array,
    enum,
    grounded_fields,
    obj,
    original_context,
    text,
    validate_schema,
)
from .storage import cached_call, js, partition, publish

AUDIT_SCHEMA = obj(
    {
        "checks": array(
            obj(
                {
                    "field_id": text("Exact field ID from input", 300),
                    "verdict": enum(("supported", "unsupported", "uncertain")),
                    "reason": text(
                        "Specific source comparison; do not introduce outside facts",
                        1200,
                    ),
                    "unit_ids": array(
                        text("Exact source units used for this judgment", 200), 24
                    ),
                }
            ),
            1000,
        )
    }
)


def validate_checks(result, tasks):
    validate_schema(result, AUDIT_SCHEMA)
    fields = {f["id"]: task for task in tasks for f in task["fields"]}
    checks = result["checks"]
    ids = [c["field_id"] for c in checks]
    if len(ids) != len(set(ids)) or set(ids) != set(fields):
        raise ValueError("Audit must assess every supplied field exactly once")
    for check in checks:
        allowed = {
            i
            for p in fields[check["field_id"]]["original_context"]
            for i in p["unit_ids"]
        }
        if any(ident not in allowed for ident in check["unit_ids"]):
            raise ValueError(
                "Audit cites units outside the field's original source context"
            )
        if check["verdict"] == "supported" and not check["unit_ids"]:
            raise ValueError("A supported verdict needs source-unit evidence")
    return checks


def audit_records(
    workspace: Path,
    source_dir: Path,
    model,
    *,
    budget,
    record_ids=None,
    max_chars=32000,
) -> Path:
    records, sources = read_records(workspace, source_dir)
    if record_ids:
        unknown = set(record_ids) - {r["id"] for r in records}
        if unknown:
            raise ValueError(f"Unknown audit records: {sorted(unknown)}")
        records = [r for r in records if r["id"] in record_ids]
    tasks = [
        {
            "record_id": r["id"],
            "product": r["product"],
            "original_context": original_context(r, sources[r["source_id"]]),
            "fields": [
                {
                    "id": r["id"] + "#" + path,
                    "statement": field["text"],
                    "citations": field["citations"],
                }
                for path, field in grounded_fields(r["content"]).items()
            ],
        }
        for r in records
    ]
    checks = []
    for batch in partition(tasks, max_chars):
        checks.extend(
            cached_call(
                workspace,
                model,
                "source_support_audit",
                AUDIT_SCHEMA,
                prompts.AUDIT,
                {"records": batch},
                budget,
                lambda result, batch=batch: validate_checks(result, batch),
            )
        )
    fields = {f["id"]: (task, f) for task in tasks for f in task["fields"]}
    by_record = {r["id"]: r for r in records}
    report = workspace / "audit/report.md"
    lines = [
        "# Field-level source-support audit",
        "",
        "> Model-generated diagnostics, not human approval, calibrated accuracy or external fact checking.",
        "",
        "Source support and information retention are separate. Null fields mean not stated in the excerpt, not extraction failure.",
        "",
    ]
    for check in checks:
        task, field = fields[check["field_id"]]
        record = by_record[task["record_id"]]
        source = sources[record["source_id"]]
        lines += [
            f"## {check['verdict']}: {escaped(field['statement'])}",
            "",
            escaped(check["reason"]),
            "",
            f"Field: `{check['field_id']}` · [Original source]({link(source.path, report)})",
            "",
        ]
    summary = {
        "records_checked": len(records),
        "fields_checked": len(checks),
        "verdicts": dict(Counter(c["verdict"] for c in checks)),
        "review_status": "model_diagnostic_only",
        "not_measured": ["information recall", "trainer resemblance", "external truth"],
    }
    publish(
        workspace / "audit",
        {
            "checks.json": js({"summary": summary, "checks": checks}),
            "report.md": "\n".join(lines),
        },
        artifact_inputs(workspace, source_dir),
    )
    return report
