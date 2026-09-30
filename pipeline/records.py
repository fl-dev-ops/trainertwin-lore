"""The three source-local information products and their citation contracts."""

import re
from copy import deepcopy

from .evidence import literal, materialize, selection_schema, span_inputs
from .sources import Source
from .storage import InvalidItems, digest

PRODUCTS = ("knowledge", "cases", "expression")
KNOWLEDGE_KINDS = ("claim", "self_report", "belief", "method", "advice", "offering")
CASE_KINDS = ("recorded_exchange", "reported_exchange", "illustration", "demonstration")


def obj(properties):
    return {
        "type": "object",
        "properties": properties,
        "required": list(properties),
        "additionalProperties": False,
    }


def text(description="", maximum=2000):
    return {
        "type": "string",
        "description": description,
        "minLength": 1,
        "maxLength": maximum,
    }


def array(items, maximum=24, minimum=0):
    return {"type": "array", "items": items, "maxItems": maximum, "minItems": minimum}


def enum(values):
    return {"type": "string", "enum": list(values)}


def nullable(schema):
    return {**schema, "type": [schema["type"], "null"]}


CITATION = obj(
    {
        "unit_id": text("Exact input unit ID", 200),
        "quote": text("Exact contiguous excerpt; quote short units in full", 800),
    }
)
GROUNDED = obj(
    {
        "text": text(
            "One source-supported statement; no added justification or inferred outcome"
        ),
        "citations": array(CITATION, 12, 1),
    }
)
COMMON = {
    "title": text("Short navigation label, not an extra claim", 160),
    "topic": text("Reusable topic label", 60),
    "context_unit_ids": array(
        text("Exact unit IDs spanning the original context", 200), 80, 1
    ),
}
KNOWLEDGE = obj(
    {
        **COMMON,
        "kind": enum(KNOWLEDGE_KINDS),
        "summary": GROUNDED,
        "goal": nullable(GROUNDED),
        "prerequisites": array(GROUNDED),
        "steps": array(GROUNDED),
        "constraints": array(GROUNDED),
        "exceptions": array(GROUNDED),
    }
)
CASE = obj(
    {
        **COMMON,
        "kind": enum(CASE_KINDS),
        "speaker_id": nullable(
            text("Focal recorded speaker ID; null for written/reported cases", 80)
        ),
        "situation": GROUNDED,
        "cue": nullable(GROUNDED),
        "diagnosis": nullable(GROUNDED),
        "strategy": nullable(GROUNDED),
        "rationale": nullable(GROUNDED),
        "response": nullable(GROUNDED),
        "outcome": nullable(GROUNDED),
    }
)
EXPRESSION = obj(
    {
        **COMMON,
        "form": enum(("structure", "wording", "tone", "rhetorical_move")),
        "speaker_id": nullable(
            text("Focal recorded speaker ID; null for authored text", 80)
        ),
        "observation": GROUNDED,
        "purpose": nullable(GROUNDED),
    }
)
SCHEMAS = {"knowledge": KNOWLEDGE, "cases": CASE, "expression": EXPRESSION}
EXTRACTION_SCHEMA = obj({name: array(schema, 24) for name, schema in SCHEMAS.items()})
EXTRACTION_REQUEST_SCHEMA = selection_schema(EXTRACTION_SCHEMA)


def validate_schema(value, schema, path="response"):
    """Validate the small JSON-schema subset emitted above, without a dependency."""
    types = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
    actual = (
        "null"
        if value is None
        else "object"
        if isinstance(value, dict)
        else "array"
        if isinstance(value, list)
        else "string"
        if isinstance(value, str)
        else "integer"
        if type(value) is int
        else "unknown"
    )
    if actual not in types:
        raise ValueError(f"{path}: expected {types}, got {actual}")
    if value is None:
        return
    if "enum" in schema and value not in schema["enum"]:
        raise ValueError(f"{path}: invalid enum value")
    if actual == "object":
        if set(value) != set(schema["properties"]):
            raise ValueError(f"{path}: missing or unexpected fields")
        for key, child in schema["properties"].items():
            validate_schema(value[key], child, f"{path}.{key}")
    elif actual == "array":
        if not schema.get("minItems", 0) <= len(value) <= schema.get("maxItems", 1000):
            raise ValueError(f"{path}: invalid item count")
        for n, item in enumerate(value):
            validate_schema(item, schema["items"], f"{path}.{n}")
    elif actual == "integer":
        if not schema.get("minimum", value) <= value <= schema.get("maximum", value):
            raise ValueError(f"{path}: integer out of range")
    elif actual == "string":
        if not value.strip() or not schema.get("minLength", 0) <= len(
            value
        ) <= schema.get("maxLength", 10000):
            raise ValueError(f"{path}: invalid text length")


def plain(value: str) -> str:
    return " ".join(value.split())


def slug(value: str) -> str:
    result = re.sub(r"[^\w]+", "-", value.casefold()).strip("-_")
    if not result or len(result) > 60:
        raise ValueError(f"Invalid topic label: {value!r}")
    return result


def grounded_fields(content: dict) -> dict[str, dict]:
    result = {}
    for key, value in content.items():
        if isinstance(value, dict) and "citations" in value:
            result[key] = value
        elif isinstance(value, list):
            for index, item in enumerate(value):
                if isinstance(item, dict) and "citations" in item:
                    result[f"{key}.{index}"] = item
    return result


def resolve_unit(ident: str, units: dict) -> str:
    if ident in units:
        return ident
    if re.fullmatch(r"u\d{6}", ident):
        matches = [key for key in units if key.endswith(":" + ident)]
        if len(matches) == 1:
            return matches[0]
    raise ValueError(f"Unknown source unit: {ident}")


def normalize_item(product: str, item: dict, source: Source, chunk: list[dict]) -> dict:
    validate_schema(item, SCHEMAS[product], product)
    item = deepcopy(item)
    item["topic"] = plain(item["topic"])
    slug(item["topic"])
    units = {u["id"]: u for u in chunk}
    context = list(
        dict.fromkeys(resolve_unit(ident, units) for ident in item["context_unit_ids"])
    )
    cited = set(context)
    positions = {u["id"]: n for n, u in enumerate(source.units)}
    for path, field in grounded_fields(item).items():
        field["text"] = plain(field["text"])
        seen, citations = set(), []
        for citation in field["citations"]:
            ident = resolve_unit(citation["unit_id"], units)
            quote = plain(citation["quote"])
            unit = units[ident]
            if not literal(quote, unit["text"]) or len(quote) < min(
                12, len(unit["text"])
            ):
                raise ValueError(
                    f"Unsupported excerpt in {product}.{path}: {citation['quote']!r}"
                )
            if (ident, quote) in seen:
                continue
            seen.add((ident, quote))
            citation.update(unit_id=ident, quote=quote)
            citations.append(citation)
            cited.add(ident)
        field["citations"] = citations
    first, last = min(positions[i] for i in cited), max(positions[i] for i in cited)
    span = source.units[first : last + 1]
    if any(u["id"] not in units for u in span):
        raise ValueError("Context crosses the supplied extraction window")
    item["context_unit_ids"] = [u["id"] for u in span]
    speaker = item.get("speaker_id")
    if speaker is not None and speaker not in {
        u["speaker_id"] for u in span if u["representation"] == "spoken_turn"
    }:
        raise ValueError("Focal speaker is not present in the cited recorded context")
    focal_field = (
        item.get("observation")
        if product == "expression"
        else item.get("response")
        if product == "cases"
        else None
    )
    if (
        speaker
        and focal_field
        and any(
            units[c["unit_id"]]["speaker_id"] != speaker
            for c in focal_field["citations"]
        )
    ):
        raise ValueError("Focal speaker does not match the cited contribution")
    if product == "cases" and item["kind"] == "recorded_exchange":
        ids = {
            u["speaker_id"]
            for u in span
            if u["representation"] == "spoken_turn" and u["speaker_id"]
        }
        if source.format in {"post", "document"}:
            raise ValueError(
                "Recorded exchange requires explicit Q&A/interview context, multiple speakers and a focal response"
            )
        if len(ids) < 2 or not speaker or item["response"] is None:
            item["kind"] = (
                "reported_exchange"
                if item.get("response") or item.get("cue")
                else "demonstration"
            )
            if item["kind"] != "recorded_exchange":
                item["speaker_id"] = None
    return item


def make_record(product: str, content: dict, source: Source) -> dict:
    ident = f"{source.id}:{product}:{digest([source.sha256, source.metadata_hash, content])[:16]}"
    return {
        "id": ident,
        "product": product,
        "source_id": source.id,
        "source_hash": source.sha256,
        "metadata_hash": source.metadata_hash,
        "source_format": source.format,
        "source_url": source.url or None,
        "published_at": source.date or None,
        "author": source.author or None,
        "category": source.category,
        "content_hash": source.content_hash,
        "title": content["title"],
        "topic": content["topic"],
        "topic_slug": slug(content["topic"]),
        "content": content,
        "semantic_status": "not_reviewed",
        "external_status": "not_checked",
        "extraction_scope": "source_excerpt",
    }


def extract_records(result: dict, chunk: list[dict], source: Source) -> list[dict]:
    validate_schema(result, EXTRACTION_SCHEMA)
    if sum(len(items) for items in result.values()) > 40:
        raise ValueError("Too many source records in one extraction window")
    records = [
        make_record(product, normalize_item(product, item, source, chunk), source)
        for product in PRODUCTS
        for item in result[product]
    ]
    if len({r["id"] for r in records}) != len(records):
        raise ValueError("Duplicate source record")
    return records


def extract_selected(result, chunk, source):
    if not isinstance(result, dict) or set(result) != set(PRODUCTS):
        raise ValueError("Expected knowledge, cases and expression arrays")
    _, spans = span_inputs(chunk)
    records, errors = [], []
    for product in PRODUCTS:
        items = result[product]
        if not isinstance(items, list) or len(items) > 24:
            raise ValueError(f"Invalid {product} array")
        for i, item in enumerate(items):
            try:
                validate_schema(
                    item, EXTRACTION_REQUEST_SCHEMA["properties"][product]["items"]
                )
                content = normalize_item(
                    product, materialize(item, spans), source, chunk
                )
                records.append(make_record(product, content, source))
            except ValueError as exc:
                errors.append((product, i, str(exc)))
    if errors:
        raise InvalidItems(errors)
    if len(records) > 40:
        raise ValueError("Too many source records in one extraction window")
    return list({r["id"]: r for r in records}.values())


def verify_records(records: list[dict], sources: dict[str, Source]) -> None:
    seen = set()
    for record in records:
        source = sources.get(record.get("source_id"))
        product = record.get("product")
        if source is None or product not in PRODUCTS:
            raise ValueError("Record references an unknown source/product")
        content = normalize_item(product, record.get("content"), source, source.units)
        if record != make_record(product, content, source) or record["id"] in seen:
            raise ValueError(f"Modified or duplicate source record: {record.get('id')}")
        seen.add(record["id"])


def record_summary(record: dict) -> str:
    content = record["content"]
    return content[
        {"knowledge": "summary", "cases": "situation", "expression": "observation"}[
            record["product"]
        ]
    ]["text"]


def original_context(record: dict, source: Source) -> list[dict]:
    """Exact original spans; author and spoken-speaker identity are separate."""
    wanted = set(record["content"]["context_unit_ids"])
    grouped = {}
    for unit in source.units:
        if unit["id"] in wanted:
            grouped.setdefault(unit["passage_id"], []).append(unit)
    passages = {p["id"]: p for p in source.passages}
    result = []
    for ident, units in grouped.items():
        passage = passages[ident]
        representation = passage["representation"]
        result.append(
            {
                "passage_id": ident,
                "unit_ids": [u["id"] for u in units],
                "units": [
                    {"id": u["id"], "text": u["text"], "speaker_id": u["speaker_id"]}
                    for u in units
                ],
                "text": passage["text"][units[0]["start"] : units[-1]["end"]],
                "locator": passage["locator"],
                "time": passage["t"] or None,
                "representation": representation,
                "author": source.author or None,
                "speaker_id": passage["speaker_id"] or None,
                "speaker_name": source.speakers.get(passage["speaker_id"])
                if representation == "spoken_turn"
                else None,
                "attribution_note": "Recorded speaker identity is supplied, not independently authenticated"
                if representation == "spoken_turn"
                else "Authored text; embedded dialogue/quotes are reported speech, not the author's recorded utterance",
            }
        )
    return result


def attributed_to(record: dict, source: Source, aliases: set[str]) -> bool:
    normalize = lambda name: plain(name or "").casefold().removeprefix("@")
    context = original_context(record, source)
    if not context:
        return False
    if all(p["representation"] == "authored_text" for p in context):
        return normalize(source.author) in aliases
    if record["product"] == "knowledge":
        cited = {
            c["unit_id"]
            for field in grounded_fields(record["content"]).values()
            for c in field["citations"]
        }
        return bool(cited) and all(
            u["representation"] == "spoken_turn"
            and normalize(source.speakers.get(u["speaker_id"])) in aliases
            for u in source.units
            if u["id"] in cited
        )
    speaker = record["content"].get("speaker_id")
    return bool(speaker) and normalize(source.speakers.get(speaker)) in aliases
