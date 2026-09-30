"""Per-field provenance, preserved methods/cases, truthful attribution and diagnostics."""

from copy import deepcopy

import pytest

from pipeline.audit import audit_records, validate_checks
from pipeline.context import select_context
from pipeline.core import (
    active_records,
    build,
    extraction_payload,
    ingest_one,
    read_records,
)
from pipeline.records import (
    attributed_to,
    extract_records,
    grounded_fields,
    original_context,
)
from pipeline.sources import read_source, spans
from pipeline.storage import append, js, load_json
from pipeline.tests.helpers import FakeModel, post, products, transcript
from pipeline.twin import build_twin, prepare_examples, validate_patterns


def extracted(source):
    raw = products(extraction_payload(source, source.units))
    return raw, extract_records(raw, source.units, source)


def test_short_turns_and_full_original_offsets(tmp_path):
    source = read_source(transcript(tmp_path))
    assert [u["text"] for u in source.units] == [
        "Should I invest all my savings?",
        "Never.",
    ]
    _, records = extracted(source)
    case = next(r for r in records if r["product"] == "cases")
    assert case["content"]["response"]["citations"][0]["quote"] == "Never."
    context = original_context(case, source)
    assert context[0]["speaker_name"] is None and context[1]["speaker_name"] == "jane"
    assert context[1]["text"] == "Never."
    assert case["content"]["diagnosis"] is None
    assert case["content"]["rationale"] is None
    assert case["content"]["outcome"] is None
    token = "x" * 1601
    assert "".join(token[a:b] for a, b in spans(token)) == token
    assert max(b - a for a, b in spans(token)) <= 800


def test_method_steps_constraints_and_unknowns_are_first_class(tmp_path):
    source = read_source(post(tmp_path), tmp_path)
    _, records = extracted(source)
    method = next(r for r in records if r["product"] == "knowledge")
    assert method["content"]["kind"] == "method"
    assert len(method["content"]["steps"]) == 4
    assert method["content"]["constraints"][0]["text"] == "A 60-second time limit."
    assert method["content"]["exceptions"] == []
    for field in grounded_fields(method["content"]).values():
        assert field["citations"]
    assert method["semantic_status"] == "not_reviewed"


def test_per_field_citations_are_strict_and_nonmutating(tmp_path):
    source = read_source(post(tmp_path), tmp_path)
    raw, _ = extracted(source)
    raw["knowledge"][0]["steps"][2]["citations"][0]["quote"] = (
        "Invented text not in this source."
    )
    before = deepcopy(raw)
    with pytest.raises(ValueError, match="Unsupported excerpt"):
        extract_records(raw, source.units, source)
    assert raw == before
    raw, _ = extracted(source)
    raw["expression"][0]["observation"]["citations"][0]["unit_id"] = "u999999"
    with pytest.raises(ValueError, match="Unknown source unit"):
        extract_records(raw, source.units, source)
    raw, _ = extracted(source)
    raw["knowledge"][0]["summary"]["citations"] = []
    with pytest.raises(ValueError, match="item count"):
        extract_records(raw, source.units, source)


def test_real_quote_still_does_not_prove_semantic_entailment(tmp_path):
    source = read_source(post(tmp_path), tmp_path)
    raw, _ = extracted(source)
    raw["knowledge"][0]["summary"]["text"] = "The author is a Nobel Prize winner."
    records = extract_records(raw, source.units, source)
    assert records[0]["semantic_status"] == "not_reviewed"
    # This intentionally documents the boundary; a lexical check is not a semantic judge.


def test_reported_speech_does_not_become_recorded_or_all_author_spoken(tmp_path):
    body = "I described this client exchange yesterday.\nClient: Can I get a discount?\nMe: What would you do with five buyers?\n"
    source = read_source(post(tmp_path, body=body), tmp_path)
    raw, records = extracted(source)
    case = next(r for r in records if r["product"] == "cases")
    assert case["content"]["kind"] == "reported_exchange"
    assert case["content"]["rationale"] is None and case["content"]["outcome"] is None
    context = original_context(case, source)
    assert context[0]["author"] == "jane" and context[0]["speaker_name"] is None
    assert context[0]["representation"] == "authored_text"
    assert "reported speech" in context[0]["attribution_note"]
    assert "Client:" in context[0]["text"]
    raw["cases"][0]["kind"] = "recorded_exchange"
    with pytest.raises(ValueError, match="Recorded exchange"):
        extract_records(raw, source.units, source)


def test_literal_self_reports_are_not_keyword_reclassified(tmp_path):
    source = read_source(
        post(tmp_path, body="I am not interested in buying a house this year."),
        tmp_path,
    )
    raw, _ = extracted(source)
    raw["knowledge"][0]["kind"] = "self_report"
    result = extract_records(raw, source.units, source)
    assert result[0]["content"]["kind"] == "self_report"


def test_invalid_chunk_is_repaired_or_failed_not_silently_salvaged(tmp_path):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    source = read_source(post(data), data)

    class Broken(FakeModel):
        def complete(self, *args):
            result = super().complete(*args)
            result["knowledge"][0]["summary"]["citations"][0]["unit_id"] = "u999999"
            return result

    broken = Broken()
    with pytest.raises(ValueError, match="after repair"):
        ingest_one(source, ws, broken, budget=[2])
    assert broken.calls == 2
    assert not (ws / "manifest" / f"{source.id}.json").exists()
    assert not list((ws / "cache").rglob("*.json"))

    class Repair(FakeModel):
        def complete(self, *args):
            result = super().complete(*args)
            if self.calls == 1:
                result["knowledge"][0]["summary"]["citations"][0]["quote"] = (
                    "Not in the source."
                )
            return result

    model = Repair()
    assert ingest_one(source, ws, model, budget=[2], retry_failed=True)
    assert model.calls == 2


def test_empty_extraction_is_explicit_and_resumable(tmp_path):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    source = read_source(post(data), data)

    class Empty(FakeModel):
        def complete(self, *args):
            self.calls += 1
            return {"knowledge": [], "cases": [], "expression": []}

    model = Empty()
    ingest_one(source, ws, model, budget=[1])
    meta = load_json(ws / "manifest" / f"{source.id}.json")
    assert meta["quality"]["status"] == "empty" and meta["quality"]["empty_chunks"] == 1
    assert not ingest_one(source, ws, model, budget=[0])
    build(ws, data)
    assert "0 accepted" in (ws / "wiki/overview.md").read_text()
    build_twin(ws, data, model, authors=["jane"], budget=[0])
    assert model.calls == 1
    assert "No supported patterns" in (ws / "twin/profile.md").read_text()


def test_known_speaker_knowledge_survives_author_filter(tmp_path):
    from pipeline.tests.helpers import grounded

    source = read_source(transcript(tmp_path), tmp_path)
    raw, _ = extracted(source)
    raw["knowledge"][0]["summary"] = grounded(source.units[-1])
    record = extract_records(raw, source.units, source)[0]
    assert attributed_to(record, source, {"jane"})
    assert not attributed_to(record, source, {"someone-else"})
    raw["knowledge"][0]["summary"] = grounded(source.units[0])
    record = extract_records(raw, source.units, source)[0]
    assert not attributed_to(record, source, {"jane"})


def test_context_rejects_question_larger_than_packet_budget(tmp_path):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    ingest_one(read_source(post(data), data), ws, FakeModel(), budget=[1])
    with pytest.raises(ValueError, match="metadata exceed"):
        select_context(ws, data, "thinking " * 1000, max_chars=1000)


def test_unknown_recorded_speakers_do_not_inherit_channel_author(tmp_path):
    data = tmp_path / "data"
    path = transcript(data, mapped=False)
    source = read_source(path, data)
    source.author = "jane"
    _, records = extracted(source)
    examples, coverage = prepare_examples(records, {source.id: source}, ["jane"], 5)
    assert examples == []
    assert coverage["excluded_records"]["attribution_unknown_or_other"] == 2


def test_role_play_is_not_personal_behavior_evidence(tmp_path):
    source = read_source(post(tmp_path), tmp_path)
    source.format = "role_play"
    _, records = extracted(source)
    examples, coverage = prepare_examples(records, {source.id: source}, ["jane"], 5)
    assert not examples and coverage["excluded_records"]["role_play"] == 1


def test_twin_preserves_all_eligible_records_not_one_card_per_source(tmp_path):
    source = read_source(post(tmp_path), tmp_path)
    raw, _ = extracted(source)
    extra = deepcopy(raw["expression"][0])
    extra["title"] = "Repeated constraint"
    extra["form"] = "rhetorical_move"
    extra["observation"]["text"] = "Repeats the time constraint at the end."
    raw["expression"].append(extra)
    records = extract_records(raw, source.units, source)
    examples, coverage = prepare_examples(records, {source.id: source}, ["jane"], 1)
    assert coverage["selected_sources"] == 1 and coverage["selected_examples"] == 2
    assert len(examples) == 2


def test_twin_wrong_unit_quote_and_overbroad_scope_rejected(tmp_path):
    source = read_source(transcript(tmp_path), tmp_path)
    _, records = extracted(source)
    examples, _ = prepare_examples(records, {source.id: source}, ["jane"], 5)
    model = FakeModel()
    result = model.complete("twin_observations", {}, "", js({"examples": examples}))
    allowed = {e["id"]: e for e in examples}
    assert validate_patterns(result, allowed)
    counter = deepcopy(examples[0])
    counter["id"] = "ex-counter"
    invalid = deepcopy(result)
    invalid["patterns"][0]["counter_ids"] = [counter["id"]]
    with pytest.raises(ValueError, match="counterexample needs"):
        validate_patterns(invalid, {**allowed, counter["id"]: counter})
    invalid = deepcopy(result)
    invalid["patterns"][0]["citations"][0]["quote"] = source.units[0]["text"]
    relocated = validate_patterns(invalid, allowed)
    assert relocated[0]["citations"][0]["unit_id"] == source.units[0]["id"]
    invalid = deepcopy(result)
    invalid["patterns"][0]["citations"][0]["quote"] = (
        "This quotation does not exist in the source."
    )
    with pytest.raises(ValueError, match="unsupported quotation"):
        validate_patterns(invalid, allowed)
    invalid = deepcopy(result)
    invalid["patterns"][0]["scope"] = "general"
    narrowed = validate_patterns(invalid, allowed)
    assert narrowed[0]["scope"] == source.category
    expression = deepcopy(examples[0])
    expression["id"] = "ex-expression"
    expression["product"] = "expression"
    expression["record"] = {
        "observation": examples[0]["record"]["response"],
    }
    invalid = deepcopy(result)
    invalid["patterns"][0].update(
        dimension="interaction",
        support_ids=[expression["id"]],
        citations=[
            {
                "example_id": expression["id"],
                **expression["record"]["observation"]["citations"][0],
            }
        ],
    )
    assert (
        validate_patterns(invalid, {expression["id"]: expression})[0]["dimension"]
        == "expression"
    )
    invalid["patterns"][0]["dimension"] = "teaching_strategy"
    assert (
        validate_patterns(invalid, {expression["id"]: expression})[0]["dimension"]
        == "expression"
    )
    invalid = deepcopy(result)
    invalid["patterns"][0]["support_ids"].append("ex-missing")
    with pytest.raises(ValueError, match="Unknown"):
        validate_patterns(invalid, allowed)


def test_source_reviews_exclude_rejected_records_without_rewriting_history(tmp_path):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    source = read_source(post(data), data)
    ingest_one(source, ws, FakeModel(), budget=[1])
    record = next(r for r in read_records(ws, data)[0] if r["product"] == "knowledge")
    review = {
        "record_id": record["id"],
        "status": "unsupported",
        "note": "Fixture rejection for review test.",
        "checked_at": "2026-09-29T00:00:00Z",
    }
    append(ws / "reviews.jsonl", review)
    assert len(read_records(ws, data)[0]) == 2
    assert not any(r["id"] == record["id"] for r in active_records(ws, data)[0])
    build(ws, data)
    assert not (ws / "wiki/knowledge.jsonl").read_text().strip()
    review.update(status="supported", note="Rechecked the actual quoted method.")
    append(ws / "reviews.jsonl", review)
    assert any(
        r["id"] == record["id"] and r["source_review"]["note"] == review["note"]
        for r in active_records(ws, data)[0]
    )


def test_context_keeps_complete_methods_and_abstains_on_no_match(tmp_path):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    ingest_one(read_source(post(data), data), ws, FakeModel(), budget=[1])
    result = select_context(
        ws, data, "spontaneous thinking exercise time limit", authors=["jane"]
    )
    assert not result["abstain"]
    method = result["knowledge"][0]["record"]["content"]
    assert len(method["steps"]) == 4 and "60-second" in method["constraints"][0]["text"]
    assert select_context(ws, data, "volcanic geology")["abstain"]
    small = select_context(ws, data, "thinking exercise", max_chars=1000)
    assert len(js(small)) <= 1000 and small["budget_omitted"] > 0
    assert select_context(ws, data, "thinking exercise", as_of="2025-01-01")["abstain"]
    assert select_context(ws, data, "thinking exercise", reviewed_only=True)["abstain"]


def test_audit_checks_every_substantive_field_not_one_overall_score(tmp_path):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    model = FakeModel()
    ingest_one(read_source(post(data), data), ws, model, budget=[1])
    report = audit_records(ws, data, model, budget=[1])
    result = load_json(ws / "audit/checks.json")
    records = read_records(ws, data)[0]
    assert result["summary"]["fields_checked"] == sum(
        len(grounded_fields(r["content"])) for r in records
    )
    assert result["summary"]["review_status"] == "model_diagnostic_only"
    assert "not human approval" in report.read_text()
    assert all(
        r["semantic_status"] == "not_reviewed" for r in read_records(ws, data)[0]
    )
    task = {
        "fields": [{"id": "one"}, {"id": "two"}],
        "original_context": [{"unit_ids": ["u1"]}],
    }
    check = {
        "field_id": "one",
        "verdict": "supported",
        "reason": "Example source.",
        "unit_ids": ["u1"],
    }
    with pytest.raises(ValueError, match="every supplied field"):
        validate_checks({"checks": [check]}, [task])
    with pytest.raises(ValueError, match="every supplied field"):
        validate_checks({"checks": [check, check]}, [task])
