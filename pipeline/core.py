"""Immutable text sources -> resumable JSONL evidence -> maintained Markdown wiki."""

from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from collections import Counter, defaultdict
from datetime import UTC, datetime
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Protocol

import httpx

from . import prompts
from .sources import SOURCE_FORMAT_VERSION, Source, chunks, paths, read_source

VERSION = "2"
KINDS = (
    "fact_claim",
    "self_report",
    "belief",
    "advice",
    "teaching_move",
    "observed_behavior",
    "style",
    "case_study",
    "offering",
)
CONTEXTS = ("observed", "advised", "hypothetical", "self_reported", "third_party")


def object_schema(properties: dict[str, Any]) -> dict[str, Any]:
    return {
        "type": "object",
        "properties": properties,
        "required": list(properties),
        "additionalProperties": False,
    }


def string(description: str = "") -> dict[str, Any]:
    return {"type": "string", "description": description}


EXTRACTION_SCHEMA = object_schema(
    {
        "overview": string(
            "Brief description of this source chunk, including its format"
        ),
        "items": {
            "type": "array",
            "items": object_schema(
                {
                    "kind": {"type": "string", "enum": list(KINDS)},
                    "context": {"type": "string", "enum": list(CONTEXTS)},
                    "topic": string("Reusable 1-4 word theme label"),
                    "statement": string(
                        "One precise sourced observation; do not assert external truth"
                    ),
                    "unit_id": string("An exact source unit ID"),
                    "quote": string(
                        "Contiguous excerpt from that unit, >=12 characters"
                    ),
                }
            ),
        },
    }
)
GROUP_SCHEMA = object_schema(
    {
        "groups": {
            "type": "array",
            "items": object_schema(
                {
                    "name": string("Canonical human-readable topic, 1-4 words"),
                    "topics": {
                        "type": "array",
                        "items": string("Exact input topic label"),
                    },
                }
            ),
        }
    }
)

FINDINGS_SCHEMA = object_schema(
    {
        "findings": {
            "type": "array",
            "items": object_schema(
                {
                    "finding": string(
                        "Specific cross-source conclusion, bounded to provided evidence"
                    ),
                    "support_ids": {
                        "type": "array",
                        "items": string("Evidence ID from input"),
                    },
                    "counter_ids": {
                        "type": "array",
                        "items": string("Contrary evidence ID from input"),
                    },
                    "qualification": string(
                        "Limits, alternative interpretation, or why this is not verified"
                    ),
                }
            ),
        }
    }
)

BEHAVIOR_SCHEMA = object_schema(
    {
        "platform": string("Platform name, e.g. linkedin, twitter, youtube, instagram"),
        "confidence": {
            "type": "string",
            "enum": ["high", "medium", "provisional"],
        },
        "summary": string(
            "1-2 sentence core characterization of persona and behavior on this platform (or sparse-data disclaimer)"
        ),
        "content_patterns": {
            "type": "array",
            "items": string(
                "Observable pattern in what they post, content formats, topics, or hooks"
            ),
        },
        "communication_style": {
            "type": "array",
            "items": string(
                "Observable pattern in how they write or speak: tone, structure, pacing"
            ),
        },
        "decision_rules": {
            "type": "array",
            "items": string(
                "Observable decision rule, mental model, or behavioral policy"
            ),
        },
        "key_phrases": {
            "type": "array",
            "items": string(
                "Signature phrase, catchphrase, or recurring rhetorical trope"
            ),
        },
    }
)


def render_platform_behavior(
    data: dict, source_count: int = 0, card_count: int = 0
) -> str:
    platform = data.get("platform", "Platform").title()
    confidence = data.get("confidence", "medium")
    summary = data.get("summary", "")
    lines = [
        f"# {platform} Behavioral & Communication Analysis",
        "",
    ]
    if confidence == "provisional" or (source_count and source_count < 5):
        lines += [
            f"> ⚠️ **Provisional observation ({source_count} sources, {card_count} evidence records)**: Insufficient volume to establish a recurring platform persona. The patterns below reflect isolated posts only, not an ongoing content strategy.",
            "",
        ]
    lines += [
        f"> {summary}",
        "",
        "## Content Patterns",
        "",
    ]
    lines.extend(f"- {p}" for p in data.get("content_patterns", []))
    lines += ["", "## Communication Style", ""]
    lines.extend(f"- {s}" for s in data.get("communication_style", []))
    lines += ["", "## Decision Rules & Mental Models", ""]
    lines.extend(f"- {d}" for d in data.get("decision_rules", []))
    lines += ["", "## Key Phrases & Tropes", ""]
    for k in data.get("key_phrases", []):
        clean = k.strip('"*')
        lines.append(f'- *"{clean}"*')
    return "\n".join(lines).strip() + "\n"


class Model(Protocol):
    model: str

    def complete(self, name: str, schema: dict, system: str, user: str) -> dict: ...

    def decide(
        self,
        state: str,
        questions: dict[str, dict[str, Any]],
        *,
        model: str = "typesafe/jev-1.13",
    ) -> dict[str, Any]: ...


def verify_author_with_jev(source: Source, user_slug: str, model: Any) -> bool:
    """Verify whether a social source belongs to the target author using Jev."""
    if not hasattr(model, "decide") or not user_slug or not source.units:
        return True
    if source.category in ("youtube", "instagram"):
        return True
    user_normalized = re.sub(r"[^a-z0-9]", "", user_slug.lower())
    if source.author:
        author_normalized = re.sub(r"[^a-z0-9]", "", source.author.lower())
        if author_normalized and (
            author_normalized in user_normalized or user_normalized in author_normalized
        ):
            return True
        sample_text = " ".join(u["text"] for u in source.units[:3])[:800]
        try:
            answers = model.decide(
                f"Target user: {user_slug}.\nSource URL: {source.url}\nDeclared author: {source.author or 'unknown'}\n\nContent excerpt:\n{sample_text}",
                {
                    "is_author": {
                        "type": "noul",
                        "instructions": f"Was this post written directly by {user_slug} rather than another person?",
                    }
                },
            )
            prob = answers.get("is_author", {}).get("noul", 1.0)
            return prob >= 0.35
        except (httpx.HTTPError, ValueError, RuntimeError, KeyError):
            return True
    return True


def stamp() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def digest(value: Any) -> str:
    data = (
        value
        if isinstance(value, bytes)
        else json.dumps(value, ensure_ascii=False, sort_keys=True).encode()
    )
    return hashlib.sha256(data).hexdigest()


def atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False
    ) as f:
        temp = Path(f.name)
        try:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
            temp.replace(path)
        finally:
            temp.unlink(missing_ok=True)


def js(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2) + "\n"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def slug(topic: str) -> str:
    value = re.sub(r"[^\w]+", "-", topic.casefold()).strip("-_")
    if not value or len(value) > 60:
        raise ValueError(f"Invalid topic: {topic!r}")
    return value


def plain(value: str) -> str:
    return " ".join(value.split())


def extract_items(
    result: dict, chunk: list[dict], source: Source, chunk_number: int
) -> list[dict]:
    if (
        not isinstance(result, dict)
        or not isinstance(result.get("overview"), str)
        or not isinstance(result.get("items"), list)
    ):
        raise ValueError("Invalid extraction response")  # noqa: TRY004 - malformed model output
    if len(result["items"]) > 40:
        raise ValueError("Too many evidence records in one chunk")
    units = {u["id"]: u for u in chunk}
    cards = []
    for n, item in enumerate(result["items"], 1):
        if not isinstance(item, dict) or set(item) != set(
            EXTRACTION_SCHEMA["properties"]["items"]["items"]["properties"]
        ):
            raise ValueError("Unexpected extraction fields")
        if item["kind"] not in KINDS or item["context"] not in CONTEXTS:
            raise ValueError("Invalid kind/context/attribution")
        if not all(
            isinstance(item[k], str) for k in ("topic", "statement", "unit_id", "quote")
        ):
            raise ValueError("Non-string extraction field")
        unit = units.get(item["unit_id"])
        if not unit and re.fullmatch(r"u\d{6}", item["unit_id"]):
            candidates = [u for u in chunk if u["id"].endswith(":" + item["unit_id"])]
            if len(candidates) == 1:
                unit = candidates[0]
        quote = plain(item["quote"])
        if unit and quote not in unit["text"]:
            match = SequenceMatcher(
                None, quote, unit["text"], autojunk=False
            ).find_longest_match()
            # ponytail: salvage only near-identical quotes; review semantic mismatches manually.
            if match.size >= max(30, int(len(quote) * 0.95 + 0.999)):
                quote = unit["text"][match.b : match.b + match.size]
        if not unit or len(quote) < 12 or quote not in unit["text"]:
            detail = (
                "unknown unit"
                if not unit
                else f"quote {quote[:120]!r}; exact source text {unit['text']!r}"
            )
            raise ValueError(
                f"Unsupported excerpt or unit ID {item['unit_id']}: {detail}"
            )
        topic = plain(item["topic"])
        slug(topic)
        statement = plain(item["statement"])
        if len(statement) < 12:
            raise ValueError("Empty finding")
        kind = item["kind"]
        context = item["context"]
        if (
            unit.get("speaker_id") in ("2", "3", "4", "5")
            and context == "self_reported"
        ):
            context = "third_party"
            if kind in ("self_report", "belief"):
                kind = "fact_claim"
        client_objection_markers = (
            "can you just send me",
            "im already invested in",
            "i'm already invested in",
            "send me some options",
            "not interested",
            "i have no budget",
            "call me later",
            "too expensive",
            "market will crash",
            "what if the developer",
        )
        if any(marker in quote.lower() for marker in client_objection_markers) and (
            context in ("self_reported", "observed")
            or kind in ("self_report", "belief")
        ):
            context = "hypothetical"
            kind = "teaching_move"
        cards.append(
            {
                "id": f"{source.id}:c{chunk_number:03d}:e{n:03d}:{digest([statement, quote])[:8]}",
                "source_id": source.id,
                "title": source.title,
                "source_hash": source.sha256,
                "metadata_hash": source.metadata_hash,
                "unit_id": unit["id"],
                "locator": unit["locator"],
                "time": unit["t"],
                "speaker_id": unit["speaker_id"],
                "category": source.category,
                "published_at": source.date or None,
                "source_url": source.url or None,
                "external_id": source.external_id or None,
                "author": source.author or None,
                "date_basis": source.date_basis,
                "kind": kind,
                "context": context,
                "topic": topic,
                "topic_slug": slug(topic),
                "statement": statement,
                "quote": quote,
                "external_status": "not_checked",
            }
        )
    return cards


def cite(card: dict, page: Path, source_path: Path) -> str:
    link = os.path.relpath(source_path, page.parent).replace(os.sep, "/")
    return f"[{card['category']} · {card.get('published_at') or 'undated'} · {card['locator']}{' · ' + card['time'] if card['time'] else ''}]({link}) (`{card['unit_id']}`; `{card['id']}`)"


def render_source(
    source: Source, cards: list[dict], page: Path, overviews: list[str], sig: str
) -> str:
    lines = [
        f"# {source.title}",
        "",
        f"Source: {os.path.relpath(source.path, page.parent)} · category: {source.category} · published: {source.date or 'unknown'} ({source.date_basis}) · author: {source.author or 'unknown'}",
        f"SHA-256: `{source.sha256}` · external ID: `{source.external_id or 'unknown'}` · {len(source.units)} source units",
        *(
            [f"Original: {source.url}"]
            if source.url.startswith(("https://", "http://"))
            else []
        ),
        f"Extraction signature: `{sig}`",
        "",
        "> Source-grounded research, not externally verified. Speaker IDs (if present) are unverified.",
        "",
        "## Chunk summaries",
        "",
    ]
    lines.extend(f"- {plain(v)}" for v in overviews)
    lines += ["", "## Extracted evidence", ""]
    for c in cards:
        lines += [
            f"### {c['topic']} · {c['kind']}",
            "",
            c["statement"],
            "",
            f"> {c['quote']}",
            "",
            (
                f"Source: {cite(c, page, source.path)}. Context: `{c['context']}`; "
                f"speaker ID: `{c['speaker_id'] or 'not supplied'}` (unverified)."
            ),
            "",
        ]
    return "\n".join(lines) + "\n"


def signature(model: str, schema: dict, prompt: str) -> str:
    return digest([VERSION, model, schema, prompt])


def ingest_one(
    source: Source,
    workspace: Path,
    model: Model,
    *,
    max_chars: int = 15000,
    budget: list[int],
    user_slug: str = "",
) -> bool:
    if user_slug and not verify_author_with_jev(source, user_slug, model):
        log(workspace, f"repost-skipped | {source.id} | not authored by {user_slug}")
        return False
    manifest = workspace / "manifest" / f"{source.id}.json"
    sig = signature(
        model.model, EXTRACTION_SCHEMA, prompts.EXTRACT + SOURCE_FORMAT_VERSION
    )
    evidence_file = (
        workspace
        / "evidence"
        / f"{source.id}-{digest([source.sha256, source.metadata_hash, sig, max_chars])[:16]}.jsonl"
    )
    page = workspace / "wiki" / "sources" / f"{source.id}.md"
    if manifest.exists() and evidence_file.exists() and page.exists():
        old = load_json(manifest)
        if (
            old.get("source_sha256") == source.sha256
            and old.get("metadata_hash") == source.metadata_hash
            and old.get("extraction_signature") == sig
            and old.get("chunk_chars") == max_chars
        ):
            return False
    pieces = chunks(source, max_chars)
    cards, overviews = [], []
    previous = Counter()
    for active in (workspace / "manifest").glob("*.json"):
        if active.stem != source.id:
            existing = workspace / "evidence" / load_json(active)["evidence_file"]
            for line in existing.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    previous[json.loads(line)["topic"]] += 1
    known_topics: list[str] = [topic for topic, _ in previous.most_common(40)]
    for number, piece in enumerate(pieces, 1):
        key = digest([source.sha256, sig, max_chars, piece])
        cache = workspace / "cache" / source.id / f"{number:03d}-{key[:16]}.json"
        if cache.exists():
            result = load_json(cache)
        else:
            if budget[0] <= 0:
                raise RuntimeError(
                    f"Call budget exhausted; resume with --max-calls (next: {source.id} chunk {number})"
                )
            budget[0] -= 1
            user = (
                f"Source {source.id}: {source.title}; author={source.author or 'unknown'}; "
                f"published={source.date or 'unknown'}; chunk {number}/{len(pieces)}. "
                f"Known topics: {', '.join(known_topics[:40]) or '(none)'}\n\n"
                + "\n".join(
                    f"[{t['id'].rsplit(':', 1)[1]}] {t['locator']} time={t['t'] or 'n/a'} speaker={t['speaker_id'] or 'n/a'}: {t['text']}"
                    for t in piece
                )
            )
            result = model.complete(
                "source_evidence", EXTRACTION_SCHEMA, prompts.EXTRACT, user
            )
            record_usage(workspace, model, f"extract:{source.id}:{number}")
            try:
                extracted = extract_items(result, piece, source, number)
            except ValueError as error:
                if budget[0] <= 0:
                    raise ValueError(
                        f"Invalid extraction for {source.id} chunk {number}: {error}"
                    ) from error
                budget[0] -= 1
                result = model.complete(
                    "source_evidence",
                    EXTRACTION_SCHEMA,
                    prompts.EXTRACT,
                    user + f"\n\nYour previous JSON failed validation: {error}. "
                    "Return a corrected complete JSON response. For the failed item copy an exact "
                    "contiguous substring (at least 12 characters) from the cited unit, character for character. "
                    "Do not quote across separate lines or units.",
                )
                record_usage(workspace, model, f"extract-repair:{source.id}:{number}")
                try:
                    extracted = extract_items(result, piece, source, number)
                except ValueError:
                    if not isinstance(result, dict) or not isinstance(
                        result.get("items"), list
                    ):
                        raise
                    valid = []
                    for n, item in enumerate(result["items"], 1):
                        try:
                            extract_items(
                                {"overview": result.get("overview"), "items": [item]},
                                piece,
                                source,
                                number,
                            )
                            valid.append(item)
                        except ValueError as invalid:
                            log(
                                workspace,
                                f"rejected-item | {source.id} chunk {number} item {n} | {invalid}",
                            )
                    if not valid:
                        raise ValueError(
                            f"No valid evidence in {source.id} chunk {number} after repair"
                        )
                    result["items"] = valid
                    extracted = extract_items(result, piece, source, number)
        if cache.exists():
            extracted = extract_items(result, piece, source, number)
        else:
            atomic(cache, js(result))
        overviews.append(result["overview"])
        cards.extend(extracted)
        known_topics = list(
            dict.fromkeys(known_topics + [c["topic"] for c in extracted])
        )
    if not cards:
        raise ValueError(
            f"No evidence extracted from {source.id}; source not committed"
        )
    atomic(
        evidence_file,
        "".join(
            json.dumps(c, ensure_ascii=False, sort_keys=True) + "\n" for c in cards
        ),
    )
    atomic(page, render_source(source, cards, page, overviews, sig))
    atomic(
        manifest,
        js(
            {
                "source_sha256": source.sha256,
                "metadata_hash": source.metadata_hash,
                "source_path": source.path.as_posix(),
                "published_at": source.date or None,
                "source_url": source.url or None,
                "external_id": source.external_id or None,
                "author": source.author or None,
                "extraction_signature": sig,
                "evidence_file": evidence_file.name,
                "chunk_chars": max_chars,
                "chunks": len(pieces),
                "evidence_count": len(cards),
                "ingested_at": stamp(),
                "model": model.model,
            }
        ),
    )
    log(
        workspace,
        f"ingest | {source.id} | {len(cards)} evidence records | {len(pieces)} chunks",
    )
    return True


def log(workspace: Path, event: str) -> None:
    path = workspace / "wiki" / "log.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(f"## [{stamp()}] {event}\n")


def record_usage(workspace: Path, model: Model, operation: str) -> None:
    usage = getattr(model, "last_usage", None)
    if isinstance(usage, dict) and usage:
        path = workspace / "usage.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    {
                        "at": stamp(),
                        "model": model.model,
                        "operation": operation,
                        "usage": usage,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )


def read_cards(
    workspace: Path, source_dir: Path, *, require_fresh: bool = True
) -> tuple[list[dict], dict[str, Source]]:
    sources = {
        s.id: s for path in paths(source_dir) if (s := read_source(path, source_dir))
    }
    records: list[dict] = []
    for manifest in sorted((workspace / "manifest").glob("*.json")):
        ident = manifest.stem
        source = sources.get(ident)
        if not source:
            raise ValueError(
                f"Missing source for ingested record {ident}; do not silently keep stale wiki pages"
            )
        meta = load_json(manifest)
        if require_fresh and (
            meta["source_sha256"] != source.sha256
            or meta.get("metadata_hash") != source.metadata_hash
        ):
            raise ValueError(
                f"Source or metadata for {ident} changed: run ingest before build/lint"
            )
        evidence_name = meta.get("evidence_file", "")
        if (
            not evidence_name.startswith(f"{ident}-")
            or Path(evidence_name).name != evidence_name
        ):
            raise ValueError(f"Invalid evidence filename in manifest: {ident}")
        evidence = workspace / "evidence" / evidence_name
        if not evidence.exists():
            raise ValueError(f"Missing evidence file: {evidence}")
        cards = [
            json.loads(line)
            for line in evidence.read_text().splitlines()
            if line.strip()
        ]
        if len(cards) != meta["evidence_count"]:
            raise ValueError(f"Evidence count mismatch: {ident}")
        records.extend(cards)
    return records, sources


def verify_cards(cards: list[dict], sources: dict[str, Source]) -> None:
    seen: set[str] = set()
    for card in cards:
        source = sources[card["source_id"]]
        unit = next((u for u in source.units if u["id"] == card["unit_id"]), None)
        if (
            not unit
            or card["quote"] not in unit["text"]
            or card["locator"] != unit["locator"]
            or card["time"] != unit["t"]
            or card["source_hash"] != source.sha256
            or card.get("metadata_hash") != source.metadata_hash
            or card["category"] != source.category
            or card.get("published_at") != (source.date or None)
            or card.get("source_url") != (source.url or None)
            or card.get("external_id") != (source.external_id or None)
            or card.get("author") != (source.author or None)
        ):
            raise ValueError(f"Broken citation: {card['id']}")
        if card["id"] in seen or card["external_status"] != "not_checked":
            raise ValueError(f"Duplicate or mislabeled evidence: {card['id']}")
        seen.add(card["id"])


def verification_overlay(cards: list[dict], workspace: Path) -> None:
    path = workspace / "verifications.jsonl"
    if not path.exists():
        return
    by_id = {c["id"]: c for c in cards}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        if record.get("evidence_id") not in by_id or record.get("status") not in (
            "verified",
            "contradicted",
        ):
            raise ValueError(f"Invalid verification: {record}")
        if not str(record.get("url", "")).startswith(
            ("https://", "http://")
        ) or not record.get("checked_at"):
            raise ValueError(
                "External verification requires a public URL and checked_at"
            )
        by_id[record["evidence_id"]]["external_status"] = record["status"]
        by_id[record["evidence_id"]]["verification_url"] = record["url"]
        by_id[record["evidence_id"]]["checked_at"] = record["checked_at"]
    # This is a human-supplied assertion, not a web check performed by the pipeline.


def partition(items: list[Any], max_chars: int) -> list[list[Any]]:
    groups: list[list[Any]] = []
    group: list[Any] = []
    size = 0
    for item in items:
        length = len(json.dumps(item, ensure_ascii=False)) + 2
        if length > max_chars:
            raise ValueError("Single evidence item exceeds synthesis chunk size")
        if group and size + length > max_chars:
            groups.append(group)
            group, size = [], 0
        group.append(item)
        size += length
    if group:
        groups.append(group)
    return groups


def resolve_evidence_id(v: Any, allowed: set[str]) -> str | None:
    if not isinstance(v, str):
        return None
    val = v.strip()
    if val in allowed:
        return val
    matches = [a for a in allowed if a.endswith(val) or val.endswith(a)]
    if len(matches) == 1:
        return matches[0]
    return None


def validate_findings(result: dict, allowed: set[str]) -> list[dict]:
    if not isinstance(result, dict) or not isinstance(result.get("findings"), list):
        raise ValueError("Invalid synthesis response")  # noqa: TRY004 - malformed model output
    findings = result["findings"]
    if len(findings) > 20:
        findings = findings[:20]  # Keep first 20; log the overflow instead of failing.
    valid_findings = []
    for finding in findings:
        if not isinstance(finding, dict) or set(finding) != {
            "finding",
            "support_ids",
            "counter_ids",
            "qualification",
        }:
            continue
        if not all(
            isinstance(finding[k], str) and finding[k].strip()
            for k in ("finding", "qualification")
        ):
            continue
        if not isinstance(finding.get("support_ids"), list) or not isinstance(
            finding.get("counter_ids"), list
        ):
            continue
        clean_support = []
        for sid in finding["support_ids"]:
            res = resolve_evidence_id(sid, allowed)
            if res and res not in clean_support:
                clean_support.append(res)
        clean_counter = []
        for cid in finding["counter_ids"]:
            res = resolve_evidence_id(cid, allowed)
            if res and res not in clean_counter:
                clean_counter.append(res)
        if not clean_support:
            continue
        finding["support_ids"] = clean_support
        finding["counter_ids"] = clean_counter
        valid_findings.append(finding)
    if not valid_findings:
        raise ValueError("Finding cites unknown or no evidence")
    return valid_findings


def synthesize(
    items: list[dict],
    model: Model,
    workspace: Path,
    key: str,
    prompt: str,
    budget: list[int],
    max_chars: int = 15000,
    previous_page: str = "",
) -> list[dict]:
    """Map/reduce with per-batch checkpoints, preserving real evidence IDs throughout."""
    original_ids = set().union(
        *(
            set(x.get("support_ids", []) + x.get("counter_ids", [])) or {x["id"]}
            for x in items
        )
    )
    if not original_ids:
        raise ValueError(f"No evidence for synthesis: {key}")
    level = 0
    current = items
    while True:
        groups = partition(current, max_chars)
        reduced = []
        for n, batch in enumerate(groups, 1):
            allowed = set().union(
                *(
                    set(x.get("support_ids", []) + x.get("counter_ids", []))
                    or {x["id"]}
                    for x in batch
                )
            )
            context = previous_page[:2500] if level == 0 else ""
            fingerprint = digest(
                [VERSION, model.model, prompt, FINDINGS_SCHEMA, batch, context]
            )
            cache = (
                workspace
                / "cache"
                / "synthesis"
                / key
                / f"{level}-{n:03d}-{fingerprint[:16]}.json"
            )
            target_ids = sorted(allowed & original_ids)
            id_guidance = f"\nValid evidence IDs (you MUST copy support_ids strictly from this list):\n{json.dumps(target_ids)}\n"
            if cache.exists():
                print(
                    f"  [{key}] Level {level} - batch {n}/{len(groups)} (cached)",
                    flush=True,
                )
                result = load_json(cache)
            else:
                if budget[0] <= 0:
                    raise RuntimeError(
                        f"Call budget exhausted; resume with --max-calls (next: {key})"
                    )
                budget[0] -= 1
                print(
                    f"  [{key}] Level {level} - batch {n}/{len(groups)} (calling {model.model}, remaining budget: {budget[0]})...",
                    flush=True,
                )
                result = model.complete(
                    "wiki_findings",
                    FINDINGS_SCHEMA,
                    prompt,
                    f"Topic: {key}. Group {n}/{len(groups)}. Existing page for editorial continuity ONLY (not evidence):\n{context}{id_guidance}\nCurrent source-backed evidence:\n"
                    + json.dumps(batch, ensure_ascii=False),
                )
                record_usage(workspace, model, f"synthesize:{key}:{level}:{n}")
            try:
                findings = validate_findings(result, allowed & original_ids)
            except ValueError:
                if (
                    level > 0
                    and isinstance(batch, list)
                    and batch
                    and "finding" in batch[0]
                ):
                    print(
                        f"  [{key}] Level {level} batch {n} reduction cited invalid IDs; retaining validated findings from previous level.",
                        flush=True,
                    )
                    findings = batch
                elif isinstance(batch, list) and batch and "id" in batch[0]:
                    print(
                        f"  [{key}] Level {level} batch {n} cited invalid IDs; falling back to batch evidence.",
                        flush=True,
                    )
                    findings = [
                        {
                            "finding": batch[0]["statement"],
                            "support_ids": [batch[0]["id"]],
                            "counter_ids": [],
                            "qualification": "Extracted from source evidence.",
                        }
                    ]
                else:
                    raise
            if not findings:
                raise ValueError(
                    f"Synthesis omitted entire evidence batch: {key} group {n}"
                )
            if not cache.exists():
                atomic(cache, js(result))
            reduced.extend(findings)
        if len(groups) == 1:
            return reduced
        if len(reduced) >= len(current) and level > 0:
            return reduced[:20] if len(reduced) > 20 else reduced
        level += 1
        if level > 6:
            raise ValueError(f"Synthesis exceeded six reduction levels: {key}")
        current = reduced


def render_findings(
    title: str,
    findings: list[dict],
    cards: dict[str, dict],
    sources: dict[str, Source],
    page: Path,
) -> str:
    lines = [
        f"# {title}",
        "",
        "> AI-generated draft from source-attested excerpts. External claims are unverified unless a reviewed verification record is supplied.",
        "",
    ]
    for number, f in enumerate(findings, 1):
        lines += [f"## {number}. {plain(f['finding'])}", ""]
        documents = {cards[i]["source_id"] for i in f["support_ids"]}
        lines += [
            f"**Evidence:** {len(f['support_ids'])} excerpts from {len(documents)} source(s).",
            "",
        ]
        for ident in dict.fromkeys(f["support_ids"]):
            c = cards[ident]
            lines += [
                f"- {cite(c, page, sources[c['source_id']].path)} · {c['kind']} / {c['context']} / external: **{c['external_status']}** — “{c['quote']}”"
            ]
        if f["counter_ids"]:
            lines += ["", "**Counterevidence / tension:**"]
            for ident in dict.fromkeys(f["counter_ids"]):
                c = cards[ident]
                lines += [
                    f"- {cite(c, page, sources[c['source_id']].path)} — “{c['quote']}”"
                ]
        lines += ["", f"**Qualification:** {plain(f['qualification'])}", ""]
    return "\n".join(lines) + "\n"


def group_topics(
    cards: list[dict], workspace: Path, model: Model, budget: list[int]
) -> dict[str, str]:
    """Merge synonymous labels in bounded rounds; retain every original label."""
    initial: dict[str, list[dict]] = defaultdict(list)
    for card in cards:
        initial[card["topic_slug"]].append(card)
    items = [
        {
            "topic": label,
            "originals": [label],
            "examples": [c["statement"][:130] for c in group[:2]],
        }
        for label, group in sorted(initial.items())
    ]
    signature_value = digest([VERSION, model.model, prompts.GROUP, GROUP_SCHEMA, items])
    record = workspace / "wiki" / "topic-map.json"
    if record.exists():
        old = load_json(record)
        if old.get("signature") == signature_value:
            return old["mapping"]

    def group_batch(batch: list[dict]) -> list[dict]:
        if len(batch) == 1:
            return [{"name": batch[0]["topic"], "topics": [batch[0]["topic"]]}]
        labels = {item["topic"] for item in batch}
        payload = [{"topic": x["topic"], "examples": x["examples"]} for x in batch]
        fingerprint = digest(
            [model.model, prompts.GROUP, GROUP_SCHEMA, payload, VERSION]
        )
        cache = workspace / "cache" / "grouping" / f"{fingerprint[:20]}.json"
        if cache.exists():
            result = load_json(cache)
        else:
            if budget[0] <= 0:
                raise RuntimeError("Call budget exhausted while grouping topics")
            budget[0] -= 1
            result = model.complete(
                "wiki_topic_groups",
                GROUP_SCHEMA,
                prompts.GROUP,
                json.dumps(payload, ensure_ascii=False),
            )
            record_usage(workspace, model, "group-topics")
        groups = result.get("groups") if isinstance(result, dict) else None
        if not isinstance(groups, list):
            groups = []

        seen_topics: set[str] = set()
        clean_groups: dict[str, dict] = {}
        for g in groups:
            if not isinstance(g, dict):
                continue
            raw_name = (g.get("name") or "").strip()
            if not raw_name:
                continue
            name_slug = slug(raw_name)
            if not name_slug:
                continue
            if name_slug not in clean_groups:
                clean_groups[name_slug] = {"name": raw_name, "topics": []}
            for t in g.get("topics", []):
                if t in labels and t not in seen_topics:
                    seen_topics.add(t)
                    clean_groups[name_slug]["topics"].append(t)

        for missing in labels - seen_topics:
            m_slug = slug(missing)
            if m_slug in clean_groups:
                clean_groups[m_slug]["topics"].append(missing)
            else:
                clean_groups[m_slug] = {"name": missing, "topics": [missing]}

        groups = [g for g in clean_groups.values() if g["topics"]]
        if not cache.exists():
            atomic(cache, js({"groups": groups}))
        return groups

    for level in range(8):
        next_items: dict[str, dict] = {}
        for start in range(0, len(items), 35):
            batch = items[start : start + 35]
            by_label = {x["topic"]: x for x in batch}
            for group in group_batch(batch):
                name = slug(group["name"])
                merged = next_items.setdefault(
                    name, {"topic": name, "originals": [], "examples": []}
                )
                for label in group["topics"]:
                    merged["originals"].extend(by_label[label]["originals"])
                    merged["examples"].extend(by_label[label]["examples"][:1])
                merged["examples"] = merged["examples"][:3]
        reduced = list(next_items.values())
        if len(items) <= 35 or len(reduced) >= len(items):
            mapping = {
                original: x["topic"] for x in reduced for original in x["originals"]
            }
            atomic(record, js({"signature": signature_value, "mapping": mapping}))
            log(
                workspace,
                f"topic-map | {len(mapping)} labels -> {len(set(mapping.values()))} pages",
            )
            return mapping
        items = sorted(reduced, key=lambda x: x["topic"])
    raise ValueError("Topic grouping exceeded eight rounds")


def build(
    workspace: Path,
    source_dir: Path,
    model: Model,
    *,
    budget: list[int],
    max_chars: int = 15000,
) -> None:
    cards, sources = read_cards(workspace, source_dir)
    if not cards:
        raise ValueError("No evidence records; run ingest first")
    verify_cards(cards, sources)
    verification_overlay(cards, workspace)
    mapping = group_topics(cards, workspace, model, budget)
    by_id = {c["id"]: c for c in cards}
    topics: dict[str, list[dict]] = defaultdict(list)
    for card in cards:
        card["topic_slug"] = mapping[card["topic_slug"]]
        topics[card["topic_slug"]].append(card)
    wiki = workspace / "wiki"
    topic_dir = wiki / "topics"
    topic_dir.mkdir(parents=True, exist_ok=True)
    all_findings = []
    for i, (topic, topic_cards) in enumerate(sorted(topics.items()), 1):
        page = topic_dir / f"{topic}.md"
        record = topic_dir / f"{topic}.json"
        sig = digest(
            [
                model.model,
                prompts.TOPIC,
                FINDINGS_SCHEMA,
                topic_cards,
                max_chars,
                VERSION,
            ]
        )
        if (
            record.exists()
            and page.exists()
            and load_json(record).get("signature") == sig
        ):
            print(f"Topic [{i}/{len(topics)}]: {topic} (up to date)", flush=True)
            findings = load_json(record)["findings"]
        else:
            print(
                f"Topic [{i}/{len(topics)}]: {topic} ({len(topic_cards)} cards)...",
                flush=True,
            )
            findings = synthesize(
                topic_cards,
                model,
                workspace,
                topic,
                prompts.TOPIC,
                budget,
                max_chars,
                previous_page=page.read_text(encoding="utf-8") if page.exists() else "",
            )
            atomic(page, render_findings(topic, findings, by_id, sources, page))
            atomic(record, js({"signature": sig, "findings": findings}))
            log(workspace, f"topic | {topic} | {len(topic_cards)} evidence records")
        all_findings.extend(findings)
    # Build fails on changed/missing sources; removal of a fully ingested source is deliberately manual.
    for old in topic_dir.glob("*.md"):
        if old.stem not in topics:
            old.unlink()
            old.with_suffix(".json").unlink(missing_ok=True)
            log(workspace, f"prune-topic | {old.stem}")
    overview_page = wiki / "overview.md"
    overview_record = wiki / "overview.json"
    sig = digest(
        [
            model.model,
            prompts.OVERVIEW,
            FINDINGS_SCHEMA,
            all_findings,
            max_chars,
            VERSION,
        ]
    )
    if (
        overview_record.exists()
        and overview_page.exists()
        and load_json(overview_record).get("signature") == sig
    ):
        overview = load_json(overview_record)["findings"]
    else:
        print("Synthesizing wiki overview...", flush=True)
        overview = synthesize(
            all_findings,
            model,
            workspace,
            "overview",
            prompts.OVERVIEW,
            budget,
            max_chars,
        )
        atomic(
            overview_page,
            render_findings(
                "Cross-topic synthesis", overview, by_id, sources, overview_page
            ),
        )
        atomic(overview_record, js({"signature": sig, "findings": overview}))
        log(
            workspace,
            f"overview | {len(topics)} topics | {len(cards)} evidence records",
        )

    # Synthesize platform-specific behavioral and communication analysis
    behavior_dir = wiki / "behavior"
    behavior_dir.mkdir(parents=True, exist_ok=True)
    active_channels = sorted(
        {
            s.category
            for s in sources.values()
            if any(c["source_id"] == s.id for c in cards)
        }
    )
    for channel in active_channels:
        channel_cards = [c for c in cards if c.get("category") == channel]
        channel_sources = {c["source_id"] for c in channel_cards}
        source_count = len(channel_sources)
        card_count = len(channel_cards)
        page = behavior_dir / f"{slug(channel)}.md"
        record = behavior_dir / f"{slug(channel)}.json"
        sample_cards = [
            {
                "topic": c["topic"],
                "kind": c["kind"],
                "statement": c["statement"],
                "quote": c["quote"],
            }
            for c in channel_cards[:70]
        ]
        sig = digest(
            [
                model.model,
                prompts.PLATFORM_BEHAVIOR,
                BEHAVIOR_SCHEMA,
                sample_cards,
                source_count,
                card_count,
                VERSION,
            ]
        )
        if (
            record.exists()
            and page.exists()
            and load_json(record).get("signature") == sig
        ):
            print(f"Platform behavior [{channel}] (up to date)", flush=True)
            continue
        if budget[0] <= 0:
            continue
        budget[0] -= 1
        print(
            f"Synthesizing behavior on {channel} ({source_count} sources, {card_count} cards)...",
            flush=True,
        )
        user_prompt = js(
            {
                "platform": channel,
                "source_count": source_count,
                "card_count": card_count,
                "evidence": sample_cards,
            }
        )
        try:
            result = model.complete(
                "platform_behavior",
                BEHAVIOR_SCHEMA,
                prompts.PLATFORM_BEHAVIOR,
                user_prompt,
            )
            record_usage(workspace, model, f"platform_behavior:{channel}")
            atomic(
                record,
                js(
                    {
                        "signature": sig,
                        "source_count": source_count,
                        "card_count": card_count,
                        "behavior": result,
                    }
                ),
            )
            atomic(
                page,
                render_platform_behavior(
                    result, source_count=source_count, card_count=card_count
                ),
            )
            log(
                workspace,
                f"behavior | {channel} | {source_count} sources | {card_count} evidence records",
            )
        except (ValueError, RuntimeError) as exc:
            print(
                f"Warning: platform behavior synthesis for {channel} failed ({exc})",
                flush=True,
            )

    ingested_ids = {c["source_id"] for c in cards}
    index = [
        "# Wiki index",
        "",
        f"{len(sources)} discovered text file(s); {len(ingested_ids)} ingested source(s), {len(cards)} evidence records across {len(topics)} topics.",
        "",
        "Start with [cross-topic synthesis](overview.md) or the [publication timeline](timeline.md). Reports are generated separately with `pipeline analyze`.",
        "",
        "## Topics",
        "",
    ]
    for name, topic_cards in sorted(topics.items()):
        index.append(
            f"- [{name}](topics/{name}.md) — {len(topic_cards)} excerpts from {len({c['source_id'] for c in topic_cards})} source(s)"
        )
    categories = {
        "behavior": {"teaching_move", "observed_behavior", "style"},
        "methods": {"advice"},
        "knowledge": {"fact_claim", "self_report", "belief", "case_study"},
        "offers": {"offering"},
    }
    index += ["", "## Evidence categories", ""]
    for category, kinds in categories.items():
        relevant = [c for c in cards if c["kind"] in kinds]
        names = sorted({c["topic_slug"] for c in relevant})
        page = wiki / "categories" / f"{category}.md"
        atomic(
            page,
            "\n".join(
                [
                    f"# {category.title()}",
                    "",
                    "> Navigation by evidence type, not independent verification.",
                    "",
                ]
                + [
                    f"- [{name}](../topics/{name}.md) — {sum(c['topic_slug'] == name for c in relevant)} excerpts"
                    for name in names
                ]
            )
            + "\n",
        )
        index.append(
            f"- [{category}](categories/{category}.md) — {len(relevant)} excerpts"
        )
    index += ["", "## Channels", ""]
    for channel in sorted({s.category for s in sources.values()}):
        channel_sources = sorted(
            (
                s
                for s in sources.values()
                if s.category == channel and any(c["source_id"] == s.id for c in cards)
            ),
            key=lambda s: s.title,
        )
        if not channel_sources:
            continue
        channel_page = wiki / "channels" / f"{slug(channel)}.md"
        atomic(
            channel_page,
            "\n".join(
                [f"# {channel.title()} sources", ""]
                + [f"- [{s.title}](../sources/{s.id}.md)" for s in channel_sources]
            )
            + "\n",
        )
        index.append(
            f"- [{channel}](channels/{slug(channel)}.md) — {len(channel_sources)} ingested sources"
        )
    index += ["", "## Sources", ""]
    ingested = {c["source_id"] for c in cards}
    for ident in sorted(ingested):
        index.append(f"- [{ident}: {sources[ident].title}](sources/{ident}.md)")
    timeline = [
        "# Publication timeline",
        "",
        "> Source publication dates, not event dates or pipeline ingestion dates. Unknown dates are not inferred.",
        "",
    ]
    dated = sorted(
        (sources[i] for i in ingested if sources[i].date), key=lambda s: (s.date, s.id)
    )
    undated = sorted(
        (sources[i] for i in ingested if not sources[i].date), key=lambda s: s.id
    )
    for source in dated:
        timeline.append(
            f"- {source.date} · [{source.title}](sources/{source.id}.md) · {source.category} · {source.author or 'author unknown'}"
        )
    timeline += ["", "## Undated sources", ""]
    timeline += [
        f"- [{source.title}](sources/{source.id}.md) · {source.category}"
        for source in undated
    ]
    atomic(wiki / "timeline.md", "\n".join(timeline) + "\n")
    atomic(wiki / "index.md", "\n".join(index) + "\n")
    # The old one-step pipeline placed a report in the wiki; it is not a wiki source.
    (wiki / "analysis.md").unlink(missing_ok=True)


def wiki_signature(wiki: Path) -> str:
    required = [
        wiki / "index.md",
        wiki / "timeline.md",
        wiki / "overview.md",
        *sorted((wiki / "topics").glob("*.md")),
    ]
    if (wiki / "behavior").exists():
        required += sorted((wiki / "behavior").glob("*.md"))
    if not all(page.is_file() for page in required) or len(required) < 4:
        raise ValueError("Wiki is incomplete; run build before analyze")
    return digest(
        [
            (page.relative_to(wiki).as_posix(), digest(page.read_bytes()))
            for page in required
        ]
    )


def analyze(workspace: Path, *, user: str = "") -> Path:
    """Compile an on-demand report from persisted wiki pages and platform behaviors."""
    wiki = workspace / "wiki"
    revision = wiki_signature(wiki)
    report = workspace / "reports" / "analysis.md"
    timeline_report = workspace / "reports" / "timeline.md"

    def rebase(text: str, source: Path) -> str:
        def replace(match: re.Match) -> str:
            link, anchor = match.group(1), match.group(2) or ""
            if link.startswith(("http://", "https://", "#")):
                return match.group(0)
            target = (source.parent / link).resolve()
            return f"]({os.path.relpath(target, report.parent).replace(os.sep, '/')}{anchor})"

        return re.sub(r"\]\(([^)#]+)(#[^)]*)?\)", replace, text)

    # 1. Output dedicated timeline report
    timeline_page = wiki / "timeline.md"
    if timeline_page.exists():
        atomic(
            timeline_report,
            "# Cross-Platform Publication Timeline\n\n"
            + "> Source publication chronology from this user's wiki.\n\n"
            + rebase(
                timeline_page.read_text(encoding="utf-8").split("\n", 1)[1],
                timeline_page,
            ).strip()
            + "\n",
        )

    # 2. Output comprehensive behavioral, platform, and persona analysis
    topic_pages = sorted((wiki / "topics").glob("*.md"))
    behavior_pages = (
        sorted((wiki / "behavior").glob("*.md")) if (wiki / "behavior").exists() else []
    )

    sections = [
        f"# Wiki-derived research draft: {user.replace('-', ' ').title() if user else 'Persona'} & Platform Behavioral Analysis",
        "",
        "> Actionable persona and behavioral intelligence for TrainerTwin. Follow citations to original sources.",
        "",
        f"[Browse the Full Wiki](../wiki/index.md) · [Cross-Platform Timeline](timeline.md) · [Cross-topic synthesis](../wiki/overview.md) · {len(topic_pages)} Topic Pages",
        "",
        "---",
        "",
        "## 1. Platform-by-Platform Behavior & Communication",
        "",
    ]

    all_decision_rules: list[str] = []
    all_key_phrases: list[str] = []

    if behavior_pages:
        for bp in behavior_pages:
            body = bp.read_text(encoding="utf-8")
            title = bp.stem.replace("-", " ").title()
            sections += [
                f"### [{title}](../wiki/behavior/{bp.name})",
                "",
                rebase(body.split("\n", 1)[1], bp).strip(),
                "",
            ]
            b_json = bp.with_suffix(".json")
            if b_json.exists():
                data = load_json(b_json).get("behavior", {})
                all_decision_rules.extend(data.get("decision_rules", []))
                all_key_phrases.extend(data.get("key_phrases", []))
    else:
        sections += [
            "> No platform behavior synthesized yet. Run `build` with an LLM to generate platform behavior analyses.",
            "",
        ]

    if all_decision_rules:
        sections += [
            "---",
            "",
            "## 2. Core Decision Rules & Behavioral Heuristics",
            "",
            "> Cross-platform mental models and behavioral state policies observed across the corpus:",
            "",
        ]
        sections.extend(f"- {rule}" for rule in dict.fromkeys(all_decision_rules))
        sections.append("")

    if all_key_phrases:
        sections += [
            "---",
            "",
            "## 3. Linguistic Fingerprint & Signature Tropes",
            "",
            "> Recurring terminology, catchphrases, and rhetorical devices:",
            "",
        ]
        for phrase in dict.fromkeys(all_key_phrases):
            clean = phrase.strip('"*')
            sections.append(f'- *"{clean}"*')
        sections.append("")

    # Pass through any human editorial notes from wiki topic pages
    editorial_notes: list[str] = []
    for page in topic_pages:
        raw = page.read_text(encoding="utf-8")
        tail = re.split(r"\n## \d+\.", raw)[-1] if re.search(r"\n## \d+\.", raw) else ""
        tail_lines = tail.strip().split("\n")
        past_qual = False
        notes: list[str] = []
        for t in tail_lines:
            if t.startswith("**Qualification:"):
                past_qual = True
                continue
            if past_qual and t.strip() and not t.startswith(("- [", "**Evidence:")):
                notes.append(t.strip())
        if notes:
            editorial_notes.append(
                f"### [{page.stem.replace('-', ' ').title()}](../wiki/topics/{page.name})"
            )
            editorial_notes.extend(f"- {n}" for n in notes)

    if editorial_notes:
        sections += [
            "---",
            "",
            "## 4. Editorial Notes & Domain Overlays",
            "",
            *editorial_notes,
            "",
        ]

    sections += [
        "---",
        "",
        "> Detailed topic findings and evidence card citations are maintained in the [Living Wiki](../wiki/index.md). Chronological post history is in the [Publication Timeline](timeline.md).",
        "",
    ]

    atomic(report, "\n".join(sections).rstrip() + "\n")
    atomic(
        report.with_suffix(".json"),
        js({"wiki_signature": revision, "generated_at": stamp()}),
    )
    return report


def lint(
    workspace: Path, source_dir: Path, *, check_report: bool = True
) -> dict[str, int]:
    cards, sources = read_cards(workspace, source_dir)
    verify_cards(cards, sources)
    verification_overlay(cards, workspace)
    for manifest in (workspace / "manifest").glob("*.json"):
        ident = manifest.stem
        source_page = workspace / "wiki" / "sources" / f"{ident}.md"
        if not source_page.exists():
            raise ValueError(f"Missing source wiki page: {ident}")
        if (
            f"Extraction signature: `{load_json(manifest)['extraction_signature']}`"
            not in source_page.read_text()
        ):
            raise ValueError(f"Stale source wiki page: {ident}")
    report = workspace / "reports" / "analysis.md"
    if check_report and report.exists():
        meta = report.with_suffix(".json")
        if not meta.exists() or load_json(meta).get("wiki_signature") != wiki_signature(
            workspace / "wiki"
        ):
            raise ValueError(
                "Stale analysis report; run analyze after building the wiki"
            )
    pages = list((workspace / "wiki").rglob("*.md")) + (
        [report] if report.exists() and check_report else []
    )
    for page in pages:
        for link in re.findall(
            r"\]\(([^)#]+)(?:#[^)]*)?\)", page.read_text(encoding="utf-8")
        ):
            if link.startswith(("http://", "https://")):
                continue
            if not (page.parent / link).exists():
                raise ValueError(f"Broken Markdown link in {page}: {link}")
    ids = {c["id"] for c in cards}
    for page in list((workspace / "wiki" / "topics").glob("*.json")) + [
        workspace / "wiki" / "overview.json"
    ]:
        if page.exists():
            for f in load_json(page)["findings"]:
                validate_findings({"findings": [f]}, ids)
            if not page.with_suffix(".md").exists():
                raise ValueError(f"Missing wiki page: {page.with_suffix('.md')}")
    return {
        "sources": len(list((workspace / "manifest").glob("*.json"))),
        "evidence": len(cards),
        "topics": len(list((workspace / "wiki" / "topics").glob("*.md"))),
    }
