"""Deterministic model fixtures. These are not LLM quality evaluations."""

import json

import yaml

METHOD = """My favourite exercise for training spontaneous thinking:

Time yourself for 60 seconds.
Grab any book.
Open randomly choose one word.
Based on this word come up with a character's name, age, appearance, personality, and backstory.
Remember you only have 60 seconds.
"""


def grounded(unit, value=None, quote=None):
    return {
        "text": value or unit["text"],
        "citations": [{"unit_id": unit["id"], "quote": quote or unit["text"]}],
    }


def empty_products():
    return {"knowledge": [], "cases": [], "expression": []}


def products(payload):
    units = payload["units"]
    first = units[0]
    ids = [u["id"] for u in units]
    timed = "Time yourself for 60 seconds." in first["text"]
    result = empty_products()
    knowledge = {
        "title": "Timed thinking exercise" if timed else "Source advice",
        "topic": "training practice",
        "context_unit_ids": ids,
        "kind": "method" if timed else "advice",
        "summary": grounded(
            first, "The author describes a timed thinking exercise." if timed else None
        ),
        "goal": None,
        "prerequisites": [],
        "steps": [],
        "constraints": [],
        "exceptions": [],
    }
    if timed:
        knowledge["goal"] = grounded(
            first, "Practice spontaneous thinking.", "training spontaneous thinking"
        )
        knowledge["prerequisites"] = [grounded(first, "A book.", "Grab any book.")]
        steps = [
            "Time yourself for 60 seconds.",
            "Grab any book.",
            "Open randomly choose one word.",
            "Based on this word come up with a character's name, age, appearance, personality, and backstory.",
        ]
        knowledge["steps"] = [grounded(first, step, step) for step in steps]
        knowledge["constraints"] = [
            grounded(
                first, "A 60-second time limit.", "Remember you only have 60 seconds."
            )
        ]
    result["knowledge"].append(knowledge)
    expression = {
        "title": "Instructional form",
        "topic": "training practice",
        "context_unit_ids": ids,
        "form": "structure",
        "speaker_id": first.get("speaker_id"),
        "observation": grounded(
            first, "Uses short instructions in an ordered exercise." if timed else None
        ),
        "purpose": None,
    }
    result["expression"].append(expression)
    spoken = {u.get("speaker_id") for u in units if u.get("speaker_id")}
    if len(spoken) > 1 and payload["format"] in {"qa", "interview"}:
        reply = units[-1]
        result["cases"].append(
            {
                "title": "Question and response",
                "topic": "training practice",
                "context_unit_ids": ids,
                "kind": "recorded_exchange",
                "speaker_id": reply["speaker_id"],
                "situation": grounded(first),
                "cue": grounded(first),
                "diagnosis": None,
                "strategy": None,
                "rationale": None,
                "response": grounded(reply),
                "outcome": None,
            }
        )
    elif "Client:" in first["text"]:
        result["cases"].append(
            {
                "title": "Reported client case",
                "topic": "training practice",
                "context_unit_ids": ids,
                "kind": "reported_exchange",
                "speaker_id": None,
                "situation": grounded(first),
                "cue": grounded(first),
                "diagnosis": None,
                "strategy": grounded(
                    first, "The author reports responding with a question."
                ),
                "rationale": None,
                "response": grounded(first),
                "outcome": None,
            }
        )
    return result


def selected_citations(value, units):
    if isinstance(value, list):
        return [selected_citations(v, units) for v in value]
    if not isinstance(value, dict):
        return value
    if "quote" in value and "unit_id" in value:
        unit = next(u for u in units if u["id"] == value["unit_id"])
        candidates = [
            s for s in unit.get("citation_spans", []) if value["quote"] in s["text"]
        ]
        sid = (
            min(candidates, key=lambda s: len(s["text"]))["id"]
            if candidates
            else unit["id"]
        )
        return {
            "span_id": sid,
            **{
                k: selected_citations(v, units)
                for k, v in value.items()
                if k not in {"unit_id", "quote"}
            },
        }
    return {k: selected_citations(v, units) for k, v in value.items()}


def repair_sections(result, payload):
    if "failed_items" not in payload:
        return result
    return {
        section: [
            next(
                (v for v in result[section] if v.get("title") == bad.get("title")),
                result[section][0],
            )
            for bad in items
        ]
        for section, items in payload["failed_items"].items()
    }


class FakeModel:
    model = "offline/fake"

    def __init__(self, fail_at=0):
        self.calls = 0
        self.operations = []
        self.fail_at = fail_at

    def close(self):
        pass

    def complete(self, name, schema, system, user):
        self.calls += 1
        self.operations.append(name)
        if self.calls == self.fail_at:
            raise RuntimeError("temporary failure")
        payload = json.loads(user.split("\nValidation error:", 1)[0])
        if name in {"source_products", "source_products_repair"}:
            return repair_sections(
                selected_citations(products(payload), payload["units"]), payload
            )
        if name == "twin_observations":
            ex = payload["examples"][0]
            content = ex["record"]
            dimension = (
                "interaction"
                if ex["product"] == "cases" and content["kind"] == "recorded_exchange"
                else "teaching_strategy"
                if ex["product"] == "cases" and content["strategy"]
                else "expression"
            )
            field = (
                content.get("observation")
                or content.get("response")
                or content["situation"]
            )
            citation = field["citations"][0]
            return {
                "patterns": [
                    {
                        "dimension": dimension,
                        "scope": ex["channel"],
                        "situation": "Presenting a teaching example.",
                        "observation": "The source presents a concrete teaching example.",
                        "support_ids": [ex["id"]],
                        "counter_ids": [],
                        "citations": [{"example_id": ex["id"], **citation}],
                        "qualification": "One source-local observation, not a universal habit.",
                        "proposed_adaptation": {
                            "when": "Presenting a similar teaching example.",
                            "action": "Consider a short example before an explanation.",
                            "limits": "A proposed adaptation, not verified personal behavior.",
                        },
                    }
                ]
            }
        if name == "source_support_audit":
            return {
                "checks": [
                    {
                        "field_id": field["id"],
                        "verdict": "supported",
                        "reason": "Fixture source support.",
                        "unit_ids": list(
                            dict.fromkeys(c["unit_id"] for c in field["citations"])
                        ),
                    }
                    for task in payload["records"]
                    for field in task["fields"]
                ]
            }
        raise AssertionError(f"Unexpected model operation: {name}")


def post(
    root,
    name="post",
    *,
    author="jane",
    date="2026-01-01",
    channel="linkedin",
    body=METHOD,
):
    path = root / channel / f"{name}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"---\nauthor: {author}\ndate: '{date}'\n---\n\n{body}", encoding="utf-8"
    )
    return path


def transcript(root, name="qa", *, mapped=True, count=None):
    root.mkdir(parents=True, exist_ok=True)
    path = root / f"{name}.yaml"
    turns = [
        {"t": "00:00:00", "speaker": "1", "text": "Should I invest all my savings?"},
        {"t": "00:00:02", "speaker": "2", "text": "Never."},
    ]
    if count:
        turns = [
            {
                "t": f"00:00:{n:02d}",
                "speaker": "1",
                "text": f"Ask about the buyer's goals before recommending properties, example {n}.",
            }
            for n in range(count)
        ]
    path.write_text(
        yaml.safe_dump(
            {
                "title": name,
                "format": "qa",
                "speakers": {"2": "jane"} if mapped else {},
                "turns": turns,
            }
        ),
        encoding="utf-8",
    )
    return path
