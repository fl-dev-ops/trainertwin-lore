"""Model-facing evidence selections; stored quotations always come from source text."""

import re
from copy import deepcopy


def literal(quote, text):
    """Only whitespace normalization is permitted, never case/fuzzy/ellipsis repair."""
    return bool(quote.strip()) and " ".join(quote.split()) in " ".join(text.split())


def frontmatter(text):
    import yaml

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, 0
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("Unclosed Markdown frontmatter") from exc
    metadata = yaml.safe_load("\n".join(lines[1:end])) or {}
    if not isinstance(metadata, dict):
        raise ValueError("Invalid Markdown frontmatter")  # noqa: TRY004 - invalid source document
    return metadata, end + 1


def span_inputs(units, *, entities=False):
    """Keep stable unit IDs; offer whole-unit and sentence spans, not invented quotes.

    Sentence splitting is only an addressing aid, not linguistic segmentation. Every
    unit remains selectable in full, including short replies and transcription noise.
    """
    result, spans = [], {}
    for unit in units:
        ident = unit["id"].rsplit(":", 1)[-1]
        raw = unit.get("raw_text", unit.get("text", ""))
        entry = {**unit, "id": ident, "text": raw}
        spans[ident] = {"unit_id": unit["id"], "quote": raw}
        parts = re.split(r"(?<=[.!?])\s+|\n+", raw)
        sentences, pending = [], ""
        for part in parts:
            pending = (pending + " " + part).strip()
            if len(pending) >= 12:
                sentences.append(pending)
                pending = ""
        if pending:
            if sentences:
                sentences[-1] += " " + pending
            else:
                sentences.append(pending)
        entry["citation_spans"] = []
        for n, quote in enumerate(sentences):
            sid = f"{ident}.s{n}"
            spans[sid] = {"unit_id": unit["id"], "quote": quote}
            entry["citation_spans"].append({"id": sid, "text": quote})
        if entities:
            entry["words"] = [
                f"{i}:{m.group()}" for i, m in enumerate(re.finditer(r"\S+", raw))
            ]
        result.append(entry)
    return result, spans


def selection_schema(schema):
    """Use span references on the wire without changing stored record contracts."""
    if schema.get("type") == "object" and set(schema.get("properties", {})) == {
        "unit_id",
        "quote",
    }:
        return {
            "type": "object",
            "properties": {
                "span_id": {"type": "string", "minLength": 1, "maxLength": 240}
            },
            "required": ["span_id"],
            "additionalProperties": False,
        }
    return {
        k: selection_schema(v) if isinstance(v, dict) else v for k, v in schema.items()
    }


def materialize(value, spans):
    if isinstance(value, list):
        return [materialize(item, spans) for item in value]
    if not isinstance(value, dict):
        return value
    if "span_id" in value:
        if value["span_id"] not in spans:
            raise ValueError(f"Unknown evidence span: {value['span_id']}")
        return {
            **deepcopy(spans[value["span_id"]]),
            **{
                key: materialize(item, spans)
                for key, item in value.items()
                if key != "span_id"
            },
        }
    return {key: materialize(item, spans) for key, item in value.items()}
