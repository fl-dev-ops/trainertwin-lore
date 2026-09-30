"""Offline planning, completeness, and strict audit of existing source records."""

from collections import Counter
from pathlib import Path

import yaml

from . import prompts
from .core import extraction_payload, extraction_signature, ingestion_windows
from .organization import (
    SOURCE_PROMPT,
    SOURCE_REQUEST_SCHEMA,
    organization_payload,
    organization_windows,
    source_units,
)
from .records import EXTRACTION_REQUEST_SCHEMA, verify_records
from .sources import Source, paths, read_source
from .storage import (
    call_key,
    digest,
    file_hash,
    inside,
    js,
    json_lines,
    load_json,
    work_state,
)


def plan(
    workspace,
    root,
    selected,
    model,
    stage,
    max_chars,
    *,
    input_price=None,
    output_price=None,
    max_output_tokens=8192,
    seconds_per_call=None,
    retry_failed=False,
):
    counts = Counter()
    requests = []
    sources = []
    errors = []
    for path in selected:
        try:
            source = read_source(path, root)
            if source is None:
                counts["metadata_only"] += 1
                continue
            sources.append(source.id)
            if stage == "ingest":
                revision = digest(
                    [
                        source.sha256,
                        source.metadata_hash,
                        extraction_signature(model, max_chars),
                    ]
                )[:20]
                manifest = workspace / "manifest" / f"{source.id}.json"
                if manifest.exists():
                    old = load_json(manifest)
                    if old.get("revision") == revision and all(
                        inside(workspace / directory, old[name]).exists()
                        and file_hash(inside(workspace / directory, old[name]))
                        == old[hash_key]
                        for directory, name, hash_key in (
                            ("sources", "source_snapshot", "snapshot_hash"),
                            ("evidence", "evidence_file", "evidence_hash"),
                        )
                    ):
                        counts["completed_sources"] += 1
                        continue
                schema, prompt, operation = (
                    EXTRACTION_REQUEST_SCHEMA,
                    prompts.EXTRACT,
                    "source_products",
                )
                payloads = [
                    extraction_payload(source, batch)
                    for batch in ingestion_windows(source, max_chars)
                ]
            else:
                manifest = workspace / "manifest" / f"{source.id}.json"
                if not manifest.exists():
                    counts["requires_ingestion"] += 1
                    continue
                meta = load_json(manifest)
                if (
                    meta["source_sha256"] != source.sha256
                    or meta["metadata_hash"] != source.metadata_hash
                ):
                    counts["requires_ingestion"] += 1
                    continue
                schema, prompt, operation = (
                    SOURCE_REQUEST_SCHEMA,
                    SOURCE_PROMPT,
                    "wiki_source",
                )
                payloads = [
                    organization_payload(source, batch)
                    for batch in organization_windows(source_units(source), max_chars)
                ]
            for payload in payloads:
                key = call_key(model, operation, schema, prompt, payload)
                state = work_state(workspace, operation, key)["status"]
                cached = (
                    state != "failed"
                    and (workspace / "cache" / operation / f"{key}.json").exists()
                )
                counts["cached_windows" if cached else state + "_windows"] += 1
                if not cached:
                    # Planning never treats invalid/blocked work as completed. Cache
                    # presence is reported separately; execution revalidates it.
                    body = {
                        "messages": [
                            {"role": "system", "content": prompt},
                            {"role": "user", "content": js(payload)},
                        ],
                        "response_format": schema,
                    }
                    byte_bound = len(js(body).encode("utf-8")) + 512
                    requests.append(
                        {
                            "source_id": source.id,
                            "key": key,
                            "status": state,
                            "input_token_upper_estimate": byte_bound,
                            "output_token_cap": max_output_tokens,
                        }
                    )
        except (ValueError, OSError, KeyError, yaml.YAMLError) as exc:
            errors.append({"path": str(path), "error": str(exc)})
    eligible = [r for r in requests if retry_failed or r["status"] != "failed"]
    costs = None
    if input_price is not None and output_price is not None:
        upper = sum(
            (
                r["input_token_upper_estimate"] * input_price
                + max_output_tokens * output_price
            )
            / 1_000_000
            for r in eligible
        )
        costs = {
            "request_reservation_estimate_usd": upper,
            "with_one_repair_per_window_usd": upper * 2,
        }
    return {
        "stage": stage,
        "model": model,
        "selected_sources": len(sources),
        "counts": dict(counts),
        "uncached_windows": len(requests),
        "schedulable_windows": len(eligible),
        "requests": requests,
        "cost": costs,
        "estimated_seconds": len(eligible) * seconds_per_call
        if seconds_per_call
        else None,
        "errors": errors,
        "notes": [
            "No network calls. Cache files are revalidated during execution.",
            "Failed windows require --retry-failed. Pending/blocked work resumes normally.",
            "Cost reservations use UTF-8 byte bounds, not a measured tokenizer; retries/repairs may cost more.",
            "Organization topic grouping is an additional corpus-wide operation; not included in source-window estimates.",
        ],
    }


def completeness(workspace, root):
    expected, current, errors = [], [], []
    for path in paths(root):
        try:
            source = read_source(path, root)
            if source is None:
                continue
            expected.append(source.id)
            manifest = workspace / "manifest" / f"{source.id}.json"
            if manifest.exists():
                m = load_json(manifest)
                if (
                    m.get("source_sha256") == source.sha256
                    and m.get("metadata_hash") == source.metadata_hash
                ):
                    current.append(source.id)
        except (ValueError, OSError, yaml.YAMLError) as exc:
            errors.append({"path": str(path), "error": str(exc)})
    states, source_states = {}, {}
    for directory in (workspace / "work").glob("*"):
        if directory.is_dir():
            target = source_states if directory.name.endswith("_sources") else states
            target[directory.name] = dict(
                Counter(
                    load_json(p).get("status", "unknown")
                    for p in directory.glob("*.json")
                )
            )
    return {
        "expected_sources": len(expected),
        "current_source_manifests": len(current),
        "missing_sources": sorted(set(expected) - set(current)),
        "parse_errors": errors,
        "ingestion_complete": bool(expected)
        and set(expected) == set(current)
        and not errors,
        "source_states": source_states,
        "historical_window_states": states,
        "note": "Completeness is separate from artifact integrity and semantic quality; window states include older request signatures.",
    }


def audit_grounding(workspace):
    """Read-only migration check. Never rewrite/quarantine active evidence automatically."""
    issues, checked = [], 0
    for path in sorted((workspace / "manifest").glob("*.json")):
        try:
            meta = load_json(path)
            snapshot = inside(workspace / "sources", meta["source_snapshot"])
            evidence = inside(workspace / "evidence", meta["evidence_file"])
            if (
                file_hash(snapshot) != meta["snapshot_hash"]
                or file_hash(evidence) != meta["evidence_hash"]
            ):
                raise ValueError("Snapshot/evidence hash mismatch")
            saved = load_json(snapshot)
            saved["path"] = Path(saved["path"])
            source = Source(**saved)
            if (
                source.id != path.stem
                or source.sha256 != meta["source_sha256"]
                or source.metadata_hash != meta["metadata_hash"]
            ):
                raise ValueError("Snapshot/manifest identity mismatch")
            records = json_lines(evidence)
            if len(records) != meta["evidence_count"]:
                raise ValueError("Manifest record count mismatch")
            for record in records:
                checked += 1
                try:
                    verify_records([record], {source.id: source})
                except ValueError as exc:
                    issues.append(
                        {
                            "source_id": source.id,
                            "record_id": record.get("id"),
                            "error": str(exc),
                        }
                    )
        except (KeyError, ValueError, OSError) as exc:
            issues.append({"manifest": str(path), "error": str(exc)})
    return {
        "checked_records": checked,
        "issues": issues,
        "passed": not issues,
        "note": "Exact grounding against stored snapshots only; not semantic entailment, current-source freshness, or human approval. No files modified.",
    }
