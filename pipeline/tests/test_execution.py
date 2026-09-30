"""Regression checks from the stopped runs. No provider requests or user-data writes."""

import json
from copy import deepcopy

import httpx
import pytest

from pipeline import __main__ as cli
from pipeline.client import OpenRouter, ProviderBlocked, SpendBudget
from pipeline.core import build, extraction_payload, ingest_one
from pipeline.evidence import literal, span_inputs
from pipeline.execution import audit_grounding, completeness, plan
from pipeline.organization import organize
from pipeline.records import extract_records, extract_selected
from pipeline.sources import read_source
from pipeline.storage import atomic, file_hash, json_lines, load_json
from pipeline.tests.helpers import FakeModel, post, products, transcript
from pipeline.tests.test_wiki import WikiModel


def test_negation_case_and_editorial_ellipsis_are_not_literal(tmp_path):
    source = read_source(
        post(tmp_path, body="The client is not interested in buying this property."),
        tmp_path,
    )
    raw = products(extraction_payload(source, source.units))
    for bad in (
        "The client is interested in buying this property.",
        "the client is not interested in buying this property.",
        "The client ... buying this property.",
    ):
        assert not literal(bad, source.units[0]["text"])
        value = deepcopy(raw)
        value["knowledge"][0]["summary"]["citations"][0]["quote"] = bad
        with pytest.raises(ValueError, match="Unsupported excerpt"):
            extract_records(value, source.units, source)


def test_model_selects_evidence_not_quotations(tmp_path):
    source = read_source(post(tmp_path), tmp_path)
    payload = extraction_payload(source, source.units)
    response = FakeModel().complete("source_products", {}, "", json.dumps(payload))
    assert "span_id" in response["knowledge"][0]["summary"]["citations"][0]
    result = extract_selected(response, source.units, source)
    assert literal(
        result[0]["content"]["summary"]["citations"][0]["quote"],
        source.units[0]["raw_text"],
    )
    response["knowledge"][0]["summary"]["citations"][0]["quote"] = "Injected quote."
    with pytest.raises(ValueError, match="unexpected fields"):
        extract_selected(response, source.units, source)


def test_span_splitting_preserves_short_replies_and_original_units(tmp_path):
    source = read_source(transcript(tmp_path), tmp_path)
    _, spans = span_inputs(source.units)
    for span in spans.values():
        unit = next(u for u in source.units if u["id"] == span["unit_id"])
        assert literal(span["quote"], unit["raw_text"])
    assert any(s["quote"] == "Never." for s in spans.values())


def test_targeted_repair_preserves_valid_siblings_and_needs_explicit_retry(tmp_path):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    source = read_source(post(data), data)

    class Broken(FakeModel):
        def complete(self, *args):
            value = super().complete(*args)
            value["knowledge"][0]["summary"]["citations"][0] = {"span_id": "unknown"}
            return value

    with pytest.raises(ValueError, match="after repair"):
        ingest_one(source, ws, Broken(), budget=[2])
    model = FakeModel()
    with pytest.raises(ValueError, match="retry-failed"):
        ingest_one(source, ws, model, budget=[2])
    assert model.calls == 0
    assert list((ws / "rejected/source_products").glob("*.json"))
    assert ingest_one(source, ws, model, budget=[1], retry_failed=True)

    data2, ws2 = tmp_path / "data2", tmp_path / "workspace2"
    source2 = read_source(post(data2), data2)

    class Repair(FakeModel):
        def complete(self, name, schema, system, user):
            value = super().complete(name, schema, system, user)
            if self.calls == 1:
                self.initial_expression = deepcopy(value["expression"])
                value["knowledge"][0]["summary"]["citations"][0] = {
                    "span_id": "unknown"
                }
            else:
                payload = json.loads(user)
                assert set(schema["properties"]) == {"knowledge"}
                assert set(payload["failed_items"]) == {"knowledge"}
                assert "previous_response" not in payload
            return value

    model = Repair()
    ingest_one(source2, ws2, model, budget=[2])
    cached = load_json(next((ws2 / "cache/source_products").glob("*.json")))
    assert cached["expression"] == model.initial_expression
    assert model.operations == ["source_products", "source_products_repair"]
    assert all(
        r["duration_seconds"] >= 0 and r["key"] for r in json_lines(ws2 / "usage.jsonl")
    )


def test_provider_credit_failure_stops_before_second_source(tmp_path):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    first, second = post(data, "a"), post(data, "b")
    requests = []

    def handle(request):
        requests.append(request)
        return httpx.Response(402)

    model = OpenRouter("test-key", "test/model", transport=httpx.MockTransport(handle))
    with pytest.raises(ProviderBlocked, match="402"):
        cli.ingest_paths([first, second], data, ws, model, [20], 24000)
    model.close()
    assert len(requests) == 1
    state = load_json(next((ws / "work/source_products").glob("*.json")))
    assert state["status"] == "blocked"


def test_dollar_reservations_survive_restart_and_prevent_dispatch(tmp_path):
    path = tmp_path / "spend.json"
    budget = SpendBudget(0.0002, 0, 10, path)
    amount = budget.reserve({}, 10)
    assert amount == pytest.approx(0.0001)
    resumed = SpendBudget(0.0002, 0, 10, path)
    resumed.reserve({}, 10)
    with pytest.raises(ProviderBlocked, match="Dollar budget"):
        resumed.reserve({}, 10)
    resumed.settle(amount, {"cost": 0.00001})
    assert load_json(path)["spent_or_reserved_usd"] == pytest.approx(0.00011)
    client = OpenRouter(
        "test-key",
        "test/model",
        transport=httpx.MockTransport(
            lambda _: pytest.fail("No request may be dispatched")
        ),
    )
    client.spend_budget = SpendBudget(0, 1, 1, tmp_path / "zero.json")
    with pytest.raises(ProviderBlocked):
        client.complete("test", {}, "system", "user")
    client.close()


def test_checkpoint_is_not_full_wiki_rebuild_and_unchanged_files_keep_inode(
    tmp_path, monkeypatch
):
    from pipeline import core

    data, ws = tmp_path / "data", tmp_path / "workspace"
    model = WikiModel()
    for name in ("a", "b", "c"):
        ingest_one(read_source(post(data, name), data), ws, model, budget=[1])
    original_build = core.build
    builds = []

    def counted(*args, **kwargs):
        builds.append(1)
        return original_build(*args, **kwargs)

    monkeypatch.setattr(core, "build", counted)
    organize(ws, data, model, budget=[4])
    assert len(builds) == 1
    receipt = ws / "wiki/build.json"
    inode = receipt.stat().st_ino
    calls = model.calls
    organize(ws, data, model, budget=[0])
    assert model.calls == calls and receipt.stat().st_ino == inode
    file = tmp_path / "same.txt"
    atomic(file, "same")
    inode = file.stat().st_ino
    atomic(file, "same")
    assert file.stat().st_ino == inode


def test_offline_plan_counts_cached_windows_and_missing_sources(tmp_path):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    path = transcript(data, count=18)
    source = read_source(path, data)
    before = plan(
        ws,
        data,
        [path],
        "offline/fake",
        "ingest",
        1000,
        input_price=2.5,
        output_price=10,
        seconds_per_call=10,
    )
    with pytest.raises(RuntimeError, match="budget"):
        ingest_one(source, ws, FakeModel(), budget=[1], max_chars=1000)
    after = plan(ws, data, [path], "offline/fake", "ingest", 1000)
    assert after["counts"]["cached_windows"] == 1
    assert after["uncached_windows"] == before["uncached_windows"] - 1
    assert before["cost"]["request_reservation_estimate_usd"] > 0
    assert before["estimated_seconds"] == before["uncached_windows"] * 10
    assert not completeness(ws, data)["ingestion_complete"]
    assert completeness(ws, data)["source_states"]["ingest_sources"]["blocked"] == 1
    calls = FakeModel()
    ingest_one(source, ws, calls, budget=[30], max_chars=1000)
    assert calls.calls == after["uncached_windows"]
    assert completeness(ws, data)["source_states"]["ingest_sources"]["completed"] == 1


def test_read_only_audit_flags_legacy_fuzzy_quote_without_rewriting(tmp_path):
    from pipeline.storage import js

    data, ws = tmp_path / "data", tmp_path / "workspace"
    source = read_source(
        post(data, body="The client is not interested in buying this property."), data
    )
    ingest_one(source, ws, FakeModel(), budget=[1])
    assert audit_grounding(ws)["passed"]
    manifest = ws / "manifest" / f"{source.id}.json"
    meta = load_json(manifest)
    evidence = ws / "evidence" / meta["evidence_file"]
    records = json_lines(evidence)
    records[0]["content"]["summary"]["citations"][0]["quote"] = (
        "The client is interested in buying this property."
    )
    evidence.write_text("".join(json.dumps(r) + "\n" for r in records))
    meta["evidence_hash"] = file_hash(evidence)
    manifest.write_text(js(meta))
    before = {p: file_hash(p) for p in ws.rglob("*") if p.is_file()}
    audit = audit_grounding(ws)
    assert not audit["passed"] and audit["issues"][0]["record_id"] == records[0]["id"]
    assert before == {p: file_hash(p) for p in before}


def test_missing_corpus_does_not_become_success_from_lint(tmp_path):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    ingest_one(read_source(post(data, "first"), data), ws, FakeModel(), budget=[1])
    post(data, "second")
    build(ws, data)
    status = completeness(ws, data)
    assert status["current_source_manifests"] == 1 and status["expected_sources"] == 2
    assert not status["ingestion_complete"]
