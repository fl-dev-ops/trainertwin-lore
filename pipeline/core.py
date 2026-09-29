"""Source-local extraction and deterministic knowledge/case/expression wiki views."""

from __future__ import annotations

import html
import os
import re
from collections import Counter, defaultdict
from dataclasses import asdict
from pathlib import Path
from urllib.parse import quote, unquote, urlparse

from . import prompts
from .records import (
    EXTRACTION_SCHEMA,
    PRODUCTS,
    extract_records,
    grounded_fields,
    original_context,
    slug,
    verify_records,
)
from .sources import SOURCE_FORMAT_VERSION, Source, chunks, read_source, source_id
from .storage import (
    SCHEMA_VERSION,
    Model,
    atomic,
    cached_call,
    check_artifacts,
    digest,
    file_hash,
    inside,
    js,
    json_lines,
    jsonl,
    load_json,
    log,
    publish,
    stamp,
)

# Public helpers used by the CLI and integration callers.
__all__ = [
    "EXTRACTION_SCHEMA",
    "SCHEMA_VERSION",
    "Model",
    "analyze",
    "atomic",
    "build",
    "chunks",
    "digest",
    "evidence_signature",
    "ingest_one",
    "js",
    "lint",
    "load_json",
    "log",
    "read_records",
    "read_source",
    "stamp",
    "verification_overlay",
]


def source_root(source: Source) -> Path:
    return source.path.parents[len(Path(source.relative_path).parts) - 1]


def extraction_payload(source: Source, window: list[dict]) -> dict:
    return {
        "source_id": source.id,
        "title": source.title,
        "author": source.author or None,
        "format": source.format,
        "audience": source.audience or None,
        "purpose": source.purpose or None,
        "speakers": source.speakers,
        "units": [
            {
                "id": u["id"].rsplit(":", 1)[1],
                "text": u["raw_text"],
                "locator": u["locator"],
                "time": u["t"] or None,
                "representation": u["representation"],
                "speaker_id": u["speaker_id"] or None,
            }
            for u in window
        ],
    }


def ingest_one(
    source: Source,
    workspace: Path,
    model: Model,
    *,
    max_chars=15000,
    budget: list[int],
    user_slug="",
) -> bool:
    """Commit all three record products only after every source window validates."""
    signature = digest(
        [
            SCHEMA_VERSION,
            SOURCE_FORMAT_VERSION,
            model.model,
            EXTRACTION_SCHEMA,
            prompts.EXTRACT,
            max_chars,
        ]
    )
    revision = digest([source.sha256, source.metadata_hash, signature])[:20]
    manifest = workspace / "manifest" / f"{source.id}.json"
    snapshot = workspace / "sources" / f"{source.id}-{revision}.json"
    evidence = workspace / "evidence" / f"{source.id}-{revision}.jsonl"
    if manifest.exists():
        old = load_json(manifest)
        if (
            old.get("version") == SCHEMA_VERSION
            and old.get("revision") == revision
            and all(
                p.exists() and file_hash(p) == old.get(key)
                for p, key in ((snapshot, "snapshot_hash"), (evidence, "evidence_hash"))
            )
        ):
            return False
    pieces = chunks(source, max_chars)
    positions = {u["id"]: n for n, u in enumerate(source.units)}
    records, empty_chunks = {}, 0
    for piece in pieces:
        first, last = positions[piece[0]["id"]], positions[piece[-1]["id"]]
        window = source.units[max(0, first - 1) : last + 2]
        result = cached_call(
            workspace,
            model,
            "source_products",
            EXTRACTION_SCHEMA,
            prompts.EXTRACT,
            extraction_payload(source, window),
            budget,
            lambda raw, window=window: extract_records(raw, window, source),
        )
        empty_chunks += not bool(result)
        records.update((r["id"], r) for r in result)
    # Do not activate results produced from a source/sidecar that changed mid-run.
    current = read_source(source.path, source_root(source))
    if (
        current is None
        or current.sha256 != source.sha256
        or current.metadata_hash != source.metadata_hash
    ):
        raise ValueError(
            f"Source or metadata changed during ingestion: {source.id}; retry"
        )
    values = list(records.values())
    document = asdict(source)
    document["path"] = source.relative_path
    atomic(snapshot, js(document))
    atomic(evidence, jsonl(values))
    used = {
        c["unit_id"]
        for r in values
        for f in grounded_fields(r["content"]).values()
        for c in f["citations"]
    }
    atomic(
        manifest,
        js(
            {
                "version": SCHEMA_VERSION,
                "source_format": SOURCE_FORMAT_VERSION,
                "source_id": source.id,
                "revision": revision,
                "source_sha256": source.sha256,
                "metadata_hash": source.metadata_hash,
                "source_root": str(source_root(source)),
                "source_path": source.relative_path,
                "source_snapshot": snapshot.name,
                "snapshot_hash": file_hash(snapshot),
                "evidence_file": evidence.name,
                "evidence_hash": file_hash(evidence),
                "evidence_count": len(values),
                "products": dict(Counter(r["product"] for r in values)),
                "chunks": len(pieces),
                "chunk_chars": max_chars,
                "model": model.model,
                "extraction_signature": signature,
                "ingested_at": stamp(),
                "quality": {
                    "status": "complete" if values else "empty",
                    "empty_chunks": empty_chunks,
                    "units_total": len(source.units),
                    "units_cited": len(used),
                    "semantic_support": "not_reviewed",
                    "coverage_is_recall": False,
                },
            }
        ),
    )
    log(
        workspace,
        f"ingest | {source.id} | {len(values)} records | {len(pieces)} windows",
    )
    return True


def data_root(workspace: Path, override: Path | None = None) -> Path:
    if override is not None:
        return override.resolve()
    roots = {
        load_json(p).get("source_root") for p in (workspace / "manifest").glob("*.json")
    }
    if len(roots) != 1 or None in roots:
        raise ValueError(
            "Cannot determine one source root; provide --data and --workspace, or ingest first"
        )
    return Path(roots.pop()).resolve()


def read_records(
    workspace: Path, source_dir: Path | None = None, *, require_fresh=True
):
    manifests = sorted((workspace / "manifest").glob("*.json"))
    if not manifests:
        return [], {}
    root = data_root(workspace, source_dir)
    records, sources = [], {}
    for path in manifests:
        meta = load_json(path)
        if (
            meta.get("version") != SCHEMA_VERSION
            or meta.get("source_format") != SOURCE_FORMAT_VERSION
        ):
            raise ValueError(
                f"Incompatible stored records for {path.stem}; run ingest to rebuild them in this workspace"
            )
        source_path = inside(root, meta["source_path"])
        if source_id(source_path, root) != path.stem:
            raise ValueError(f"Source path/identity mismatch: {path.stem}")
        snapshot = inside(workspace / "sources", meta["source_snapshot"])
        evidence = inside(workspace / "evidence", meta["evidence_file"])
        for artifact, key in ((snapshot, "snapshot_hash"), (evidence, "evidence_hash")):
            if not artifact.exists() or file_hash(artifact) != meta.get(key):
                raise ValueError(f"Missing or modified source artifact: {artifact}")
        saved = load_json(snapshot)
        saved["path"] = source_path
        source = Source(**saved)
        if (
            source.id != path.stem
            or source.sha256 != meta["source_sha256"]
            or source.metadata_hash != meta["metadata_hash"]
        ):
            raise ValueError(f"Snapshot/manifest mismatch: {path.stem}")
        if require_fresh:
            if not source_path.exists():
                raise ValueError(f"Missing active source: {source_path}")
            current = read_source(source_path, root)
            if (
                current is None
                or current.sha256 != source.sha256
                or current.metadata_hash != source.metadata_hash
            ):
                raise ValueError(f"Source or metadata changed: {path.stem}; run ingest")
        source_records = json_lines(evidence)
        if len(source_records) != meta["evidence_count"]:
            raise ValueError(f"Record count mismatch: {path.stem}")
        sources[source.id] = source
        records.extend(source_records)
    verify_records(records, sources)
    return records, sources


def verification_overlay(records: list[dict], workspace: Path) -> None:
    by_id = {r["id"]: r for r in records}
    for review in json_lines(workspace / "verifications.jsonl"):
        if (
            review.get("status") not in {"verified", "contradicted"}
            or not isinstance(review.get("note"), str)
            or not review["note"].strip()
        ):
            raise ValueError("External review needs a valid status and scoped note")
        url = urlparse(str(review.get("url", "")))
        if (
            url.scheme not in {"http", "https"}
            or not url.hostname
            or not review.get("checked_at")
        ):
            raise ValueError("External review needs a public URL and timestamp")
        record = by_id.get(review.get("evidence_id"))
        if record:
            record["external_status"] = review["status"]
            record["external_review"] = review
    for review in json_lines(workspace / "reviews.jsonl"):
        if (
            review.get("status") not in {"supported", "unsupported", "uncertain"}
            or not isinstance(review.get("note"), str)
            or not review["note"].strip()
            or not review.get("checked_at")
        ):
            raise ValueError("Source-support review needs status, note and timestamp")
        record = by_id.get(review.get("record_id"))
        if record:
            record["semantic_status"] = "human_" + review["status"]
            record["source_review"] = review


def active_records(workspace: Path, source_dir: Path | None = None):
    records, sources = read_records(workspace, source_dir)
    verification_overlay(records, workspace)
    return [r for r in records if r["semantic_status"] != "human_unsupported"], sources


def evidence_signature(workspace: Path) -> str:
    files = sorted((workspace / "manifest").glob("*.json"))
    files += [
        workspace / name
        for name in ("reviews.jsonl", "verifications.jsonl")
        if (workspace / name).exists()
    ]
    return digest([(str(p.relative_to(workspace)), file_hash(p)) for p in files])


def artifact_inputs(workspace: Path, source_dir: Path | None = None) -> dict:
    return {
        "evidence": evidence_signature(workspace),
        "source_root": str(data_root(workspace, source_dir)),
        "workspace_root": str(workspace.resolve()),
    }


def escaped(value) -> str:
    return re.sub(r"([\\`*_\[\]()])", r"\\\1", html.escape(str(value), quote=False))


def link(target: Path, page: Path) -> str:
    return quote(
        os.path.relpath(target, page.parent).replace(os.sep, "/"), safe="/-_.~"
    )


def anchor(record: dict) -> str:
    return "record-" + digest(record["id"])[:16]


def record_link(record: dict, workspace: Path, page: Path) -> str:
    return (
        link(workspace / "wiki/topics" / f"{record['topic_slug']}.md", page)
        + "#"
        + anchor(record)
    )


def render_record(record: dict, source: Source, page: Path) -> str:
    content = record["content"]
    lines = [
        f'<a id="{anchor(record)}"></a>',
        f"## {escaped(record['title'])}",
        "",
        f"**Product:** {record['product']} · **Type:** {content.get('kind', content.get('form'))} · **Source support:** {record['semantic_status']}",
        f"**Publication:** {record['published_at'] or 'unknown'} · **Author:** {escaped(source.author or 'unknown')} · **Format:** {source.format}",
        "",
    ]
    fields = grounded_fields(content)
    order = {
        "knowledge": [
            "summary",
            "goal",
            "prerequisites",
            "steps",
            "constraints",
            "exceptions",
        ],
        "cases": [
            "situation",
            "cue",
            "diagnosis",
            "strategy",
            "rationale",
            "response",
            "outcome",
        ],
        "expression": ["observation", "purpose"],
    }[record["product"]]
    for name in order:
        value = content[name]
        if (
            record["product"] == "knowledge"
            and content["kind"] != "method"
            and name != "summary"
            and not value
        ):
            continue
        lines += [f"### {name.replace('_', ' ').title()}", ""]
        selected = [
            (key, field)
            for key, field in fields.items()
            if key == name or key.startswith(name + ".")
        ]
        if not selected:
            lines += ["Not stated in the cited excerpt.", ""]
        for number, (_, field) in enumerate(selected, 1):
            lines.append(
                f"{str(number) + '.' if name == 'steps' else '-'} {escaped(field['text'])}"
            )
            units = {u["id"]: u for u in source.units}
            for cite in field["citations"]:
                unit = units[cite["unit_id"]]
                lines.append(
                    f"  - “{escaped(cite['quote'])}” — [{escaped(unit['locator'])}]({link(source.path, page)}) (`{unit['id']}`)"
                )
            lines.append("")
    for key, label in (
        ("source_review", "Source-support review"),
        ("external_review", "External human review — scope"),
    ):
        review = record.get(key)
        if review:
            lines += [
                f"**{label}:** {review['status']} — {escaped(review['note'])} ({review['checked_at']})",
                "",
            ]
            if review.get("url"):
                lines += [f"[Review source]({review['url']})", ""]
    lines += ["### Original context", ""]
    for passage in original_context(record, source):
        who = (
            passage["speaker_name"] or "unknown speaker"
            if passage["representation"] == "spoken_turn"
            else f"authored text by {source.author or 'unknown author'}"
        )
        lines += [
            f"**{escaped(who)}** · {escaped(passage['locator'])} · {passage['representation']}",
            "",
            "\n".join("> " + escaped(line) for line in passage["text"].splitlines()),
            "",
        ]
    return "\n".join(lines)


def build(
    workspace: Path,
    source_dir: Path,
    model: Model | None = None,
    *,
    budget=None,
    max_chars=15000,
) -> Path:
    """Offline, lossless projection of accepted records. No second LLM summary."""
    records, sources = active_records(workspace, source_dir)
    if not sources:
        raise ValueError("No ingested sources; run ingest first")
    wiki = workspace / "wiki"
    files, topics = {}, defaultdict(list)
    for record in records:
        topics[record["topic_slug"]].append(record)
    for topic, items in sorted(topics.items()):
        page = wiki / "topics" / f"{topic}.md"
        files[f"topics/{topic}.md"] = (
            f"# {escaped(topic.replace('-', ' '))}\n\n> Source-local records, not independent fact verification. Original steps and qualifications are retained.\n\n"
            + "\n".join(
                render_record(r, sources[r["source_id"]], page)
                for r in sorted(
                    items,
                    key=lambda r: (r["published_at"] or "", r["id"]),
                    reverse=True,
                )
            )
        )
    for product in PRODUCTS:
        subset = [r for r in records if r["product"] == product]
        files[f"{product}.jsonl"] = jsonl(subset)
        page = wiki / f"{product}.md"
        files[f"{product}.md"] = (
            f"# {product.title()}\n\n"
            + "\n".join(
                f"- [{escaped(r['title'])}]({record_link(r, workspace, page)})"
                for r in subset
            )
            + "\n"
        )
    for source in sources.values():
        page = wiki / "sources" / f"{source.id}.md"
        items = [r for r in records if r["source_id"] == source.id]
        files[f"sources/{source.id}.md"] = (
            f"# {escaped(source.title)}\n\n[Original captured file]({link(source.path, page)}) · {source.date or 'undated'} · {source.category}\n\n"
            + "\n".join(
                f"- [{escaped(r['title'])}]({record_link(r, workspace, page)})"
                for r in items
            )
            + "\n"
        )
    by_channel = Counter(s.category for s in sources.values())
    for channel in by_channel:
        files[f"channels/{slug(channel)}.md"] = (
            f"# {escaped(channel)}\n\n"
            + "\n".join(
                f"- [{escaped(s.title)}](../sources/{s.id}.md)"
                for s in sources.values()
                if s.category == channel
            )
            + "\n"
        )
    counts = dict(Counter(r["product"] for r in records))
    qualities = [
        load_json(p)["quality"] for p in (workspace / "manifest").glob("*.json")
    ]
    summary = {
        "sources": len(sources),
        "records": len(records),
        "products": counts,
        "content_families": len({s.content_hash for s in sources.values()}),
        "channels": dict(by_channel),
        "processing": qualities,
        "unknown_case_fields": dict(
            Counter(
                k
                for r in records
                if r["product"] == "cases"
                for k in ("diagnosis", "rationale", "outcome")
                if r["content"][k] is None
            )
        ),
    }
    files["overview.json"] = js(summary)
    files["overview.md"] = (
        "# Corpus overview\n\n"
        + f"{len(sources)} source publications; {len(records)} accepted source-local records; {summary['content_families']} normalized content families.\n\n"
        + "\n".join(f"- {name}: {counts.get(name, 0)} records" for name in PRODUCTS)
        + "\n\nNo new conclusions are generated here. Missing rationales/outcomes remain unknown. Publication dates are not event dates; repetition is not independent verification. Processing coverage is not semantic recall.\n"
    )
    dated = sorted(
        (s for s in sources.values() if s.date), key=lambda s: (s.date, s.id)
    )
    undated = sorted((s for s in sources.values() if not s.date), key=lambda s: s.id)
    files["timeline.md"] = (
        "# Publication timeline\n\n> Publication dates, not event dates.\n\n"
        + "\n".join(
            f"- {s.date} · [{escaped(s.title)}](sources/{s.id}.md)" for s in dated
        )
        + "\n\n## Undated sources\n\n"
        + "\n".join(f"- [{escaped(s.title)}](sources/{s.id}.md)" for s in undated)
        + "\n"
    )
    files["index.md"] = (
        "# TrainerTwin knowledge wiki\n\n[Corpus overview](overview.md) · [Publication timeline](timeline.md)\n\n"
        + "\n".join(
            f"- [{p.title()}]({p}.md) — {counts.get(p, 0)} records" for p in PRODUCTS
        )
        + "\n\n## Topics\n\n"
        + "\n".join(
            f"- [{escaped(t.replace('-', ' '))}](topics/{t}.md)" for t in sorted(topics)
        )
        + "\n"
    )
    publish(wiki, files, artifact_inputs(workspace, source_dir))
    return wiki / "index.md"


def analyze(workspace: Path, *, user="", source_dir: Path | None = None) -> Path:
    """Compile managed wiki/twin pages, without interpreting them again."""
    root = data_root(workspace, source_dir)
    lint(workspace, root, check_report=False)
    wiki = check_artifacts(workspace / "wiki", artifact_inputs(workspace, root))
    report = workspace / "reports/analysis.md"
    inputs = {"wiki": digest(wiki), "evidence": evidence_signature(workspace)}
    sections = [
        f"# TrainerTwin research: {escaped(user or 'source corpus')}",
        "",
        "> Source support, usefulness and trainer resemblance are different questions. This is not a verified personality.",
        "",
    ]
    pages = [workspace / "wiki/overview.md"] + [
        workspace / "wiki" / p
        for p in sorted(wiki["files"])
        if p.startswith("topics/") and p.endswith(".md")
    ]
    if (workspace / "twin/build.json").exists():
        inputs["twin"] = digest(check_artifacts(workspace / "twin"))
        pages.insert(0, workspace / "twin/profile.md")
    else:
        sections += [
            "No twin specification yet. Build it separately from the original cases and expression records.",
            "",
        ]

    def rebase(text, page):
        def replace(match):
            target = match[1]
            if target.startswith(("https://", "http://", "#")):
                return match[0]
            path, _, fragment = target.partition("#")
            return (
                "]("
                + link(page.parent / unquote(path), report)
                + ("#" + fragment if fragment else "")
                + ")"
            )

        return re.sub(r"(?<!\\)\]\(([^)]+)\)", replace, text)

    for page in pages:
        sections += [rebase(page.read_text(encoding="utf-8"), page), "\n---\n"]
    publish(
        workspace / "reports",
        {
            "analysis.md": "\n".join(sections),
            "timeline.md": rebase(
                (workspace / "wiki/timeline.md").read_text(),
                workspace / "wiki/timeline.md",
            ),
        },
        inputs,
    )
    return report


def lint(workspace: Path, source_dir: Path, *, check_report=True) -> dict:
    records, sources = read_records(workspace, source_dir)
    verification_overlay(records, workspace)
    wiki_receipt = None
    if (workspace / "wiki").exists():
        wiki_receipt = check_artifacts(
            workspace / "wiki", artifact_inputs(workspace, source_dir)
        )
    twin_receipt = None
    if (workspace / "twin").exists():
        from .twin import validate_twin

        validate_twin(workspace, records, sources)
        twin_receipt = check_artifacts(workspace / "twin")
    if (workspace / "audit").exists():
        check_artifacts(workspace / "audit", artifact_inputs(workspace, source_dir))
    directories = [workspace / "wiki", workspace / "twin"]
    if check_report and (workspace / "reports").exists():
        expected = {
            "wiki": digest(wiki_receipt),
            "evidence": evidence_signature(workspace),
        }
        if twin_receipt:
            expected["twin"] = digest(twin_receipt)
        check_artifacts(workspace / "reports", expected)
        directories.append(workspace / "reports")
    for directory in directories:
        if not (directory / "build.json").exists():
            continue
        for name in load_json(directory / "build.json")["files"]:
            if not name.endswith(".md"):
                continue
            page = inside(directory, name)
            for target in re.findall(
                r"(?<!\\)\]\(([^)#]+)(?:#[^)]*)?\)", page.read_text()
            ):
                if (
                    not target.startswith(("http://", "https://"))
                    and not (page.parent / unquote(target)).exists()
                ):
                    raise ValueError(f"Broken Markdown link in {page}: {target}")
    return {
        "sources": len(sources),
        "evidence": len(records),
        "topics": len(
            {
                r["topic_slug"]
                for r in records
                if r["semantic_status"] != "human_unsupported"
            }
        ),
        "products": dict(Counter(r["product"] for r in records)),
    }
