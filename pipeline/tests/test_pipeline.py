"""End-to-end contracts; models/HTTP are mocked, original data is untouched."""

import json
import shutil
import sys

import httpx
import pytest
import yaml

from pipeline import __main__ as cli
from pipeline.client import ModelError, OpenRouter
from pipeline.core import analyze, build, ingest_one, lint, read_records
from pipeline.sources import chunks, normalize_date, paths, read_source
from pipeline.storage import load_json
from pipeline.tests.helpers import METHOD, FakeModel, post, transcript
from pipeline.twin import build_twin


def test_source_to_three_views_and_zero_call_rebuild(tmp_path):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    source = read_source(post(data), data)
    model = FakeModel()
    assert ingest_one(source, ws, model, budget=[1])
    assert model.calls == 1
    assert not (ws / "wiki").exists()
    assert not ingest_one(source, ws, model, budget=[0])
    meta = load_json(ws / "manifest" / f"{source.id}.json")
    document = load_json(ws / "sources" / meta["source_snapshot"])
    assert document["original_text"] == source.original_text
    assert document["path"] == "linkedin/post.md"
    assert meta["products"] == {"knowledge": 1, "expression": 1}
    page = build(ws, data, model, budget=[0])
    assert page.exists() and model.calls == 1
    topic = (ws / "wiki/topics/training-practice.md").read_text()
    assert "60-second time limit" in topic
    assert topic.index("### Steps") < topic.index("### Constraints")
    assert "Not stated in the cited excerpt" in topic
    assert "theoretically sound" not in topic
    assert all(
        (ws / "wiki" / f"{name}.jsonl").exists()
        for name in ("knowledge", "cases", "expression")
    )
    twin = build_twin(ws, data, model, authors=["jane"], budget=[1])
    assert model.calls == 2
    assert "Proposed adaptation" in twin.read_text()
    report = analyze(ws, user="jane")
    assert "60-second time limit" in report.read_text()
    assert lint(ws, data)["products"] == {"knowledge": 1, "expression": 1}
    build(ws, data, model, budget=[0])
    build_twin(ws, data, model, authors=["jane"], budget=[0])
    analyze(ws)
    assert model.calls == 2


def test_chunks_resume_without_partial_source_commit(tmp_path):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    source = read_source(transcript(data, count=18), data)
    count = len(chunks(source, 1000))
    assert count > 1
    with pytest.raises(RuntimeError, match="budget"):
        ingest_one(source, ws, FakeModel(), budget=[1], max_chars=1000)
    assert not (ws / "manifest" / f"{source.id}.json").exists()
    assert len(list((ws / "cache/source_products").glob("*.json"))) == 1
    model = FakeModel()
    ingest_one(source, ws, model, budget=[20], max_chars=1000)
    assert model.calls == count - 1
    assert lint(ws, data)["sources"] == 1


def test_local_edit_reuses_unchanged_windows_and_invalidates_derived_outputs(tmp_path):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    path = transcript(data, count=18)
    model = FakeModel()
    ingest_one(read_source(path, data), ws, model, budget=[20], max_chars=1000)
    build(ws, data)
    before = model.calls
    previous = {r["id"] for r in read_records(ws, data)[0]}
    content = yaml.safe_load(path.read_text())
    content["turns"][-1]["text"] += " Ask about their timeline too."
    path.write_text(yaml.safe_dump(content))
    with pytest.raises(ValueError, match="changed"):
        lint(ws, data)
    ingest_one(read_source(path, data), ws, model, budget=[20], max_chars=1000)
    assert 0 < model.calls - before < before
    assert not previous & {r["id"] for r in read_records(ws, data)[0]}
    with pytest.raises(ValueError, match="Stale"):
        lint(ws, data)
    build(ws, data)
    assert lint(ws, data)["sources"] == 1


def test_metadata_dates_can_reuse_extraction_but_authorship_cannot(tmp_path):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    path = post(data)
    model = FakeModel()
    ingest_one(read_source(path, data), ws, model, budget=[1])
    sidecar = data / ".source-metadata.yaml"
    sidecar.write_text("linkedin/post.md:\n  date: '2026-02-01'\n")
    ingest_one(read_source(path, data), ws, model, budget=[0])
    assert model.calls == 1
    sidecar.write_text(
        "linkedin/post.md:\n  date: '2026-02-01'\n  author: another-author\n"
    )
    ingest_one(read_source(path, data), ws, model, budget=[1])
    assert model.calls == 2
    assert normalize_date("Sun Aug 02 03:00:09 +0000 2026") == "2026-08-02T03:00:09Z"


def test_incompatible_records_rebuild_in_the_same_workspace(tmp_path):
    from pipeline.chronology import evidence_for

    data, ws = tmp_path / "data", tmp_path / "workspace"
    source = read_source(post(data), data)
    (ws / "manifest").mkdir(parents=True)
    (ws / "manifest" / f"{source.id}.json").write_text('{"source_format":"flat-cards"}')
    with pytest.raises(ValueError, match="run ingest.*this workspace"):
        read_records(ws, data)
    with pytest.raises(ValueError, match="run ingest.*this workspace"):
        evidence_for([source], ws)
    ingest_one(source, ws, FakeModel(), budget=[1])
    assert read_records(ws, data)[0][0]["product"] == "knowledge"
    assert build(ws, data) == ws / "wiki/index.md"
    assert lint(ws, data)["sources"] == 1


def test_artifact_tampering_and_relocation(tmp_path):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    source = read_source(post(data, name="space (one)"), data)
    model = FakeModel()
    ingest_one(source, ws, model, budget=[1])
    build(ws, data)
    build_twin(ws, data, model, authors=["jane"], budget=[1])
    analyze(ws)
    moved = tmp_path / "moved/nested/workspace"
    shutil.copytree(ws, moved)
    with pytest.raises(ValueError, match="Stale"):
        lint(moved, data)
    build(moved, data)
    build_twin(moved, data, model, authors=["jane"], budget=[0])
    analyze(moved)
    assert lint(moved, data)["sources"] == 1
    assert model.calls == 2
    topic = moved / "wiki/topics/training-practice.md"
    topic.write_text(topic.read_text() + "\nAn unsupported editorial claim.\n")
    with pytest.raises(ValueError, match="Modified"):
        lint(moved, data)
    build(moved, data)
    assert "unsupported editorial" not in topic.read_text()
    meta = load_json(moved / "manifest" / f"{source.id}.json")
    (moved / "sources" / meta["source_snapshot"]).write_text("{}")
    with pytest.raises(ValueError, match="modified"):
        read_records(moved, data)


def test_uningested_bad_file_does_not_block_existing_records(tmp_path):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    source = read_source(post(data), data)
    ingest_one(source, ws, FakeModel(), budget=[1])
    (data / "unprocessed.yaml").write_text("[invalid")
    build(ws, data)
    assert lint(ws, data)["sources"] == 1


def test_cli_isolates_bad_sources_and_offline_build_needs_no_key(tmp_path, monkeypatch):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    path = post(data)
    (data / "a-bad.yaml").write_text("[invalid")
    model = FakeModel()
    monkeypatch.setattr(cli, "model_client", lambda _: model)
    monkeypatch.setattr(
        sys, "argv", ["pipeline", "--data", str(data), "--workspace", str(ws), "ingest"]
    )
    with pytest.raises(RuntimeError, match="incomplete"):
        cli.cli()
    assert (ws / "manifest" / f"{read_source(path, data).id}.json").exists()

    def no_client(_):
        pytest.fail("Offline build must not request an API client")

    monkeypatch.setattr(cli, "model_client", no_client)
    monkeypatch.setattr(
        sys, "argv", ["pipeline", "--data", str(data), "--workspace", str(ws), "build"]
    )
    cli.cli()
    assert (ws / "wiki/index.md").exists()


def test_cli_shared_run_budget_and_user_paths(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(cli, "ROOT", tmp_path)
    data = tmp_path / "users/jane/data"
    post(data)
    model = FakeModel()
    monkeypatch.setattr(cli, "model_client", lambda _: model)
    monkeypatch.setattr(
        sys,
        "argv",
        ["pipeline", "--user", "jane", "run", "--author", "jane", "--max-calls", "2"],
    )
    cli.cli()
    assert model.calls == 2
    assert (tmp_path / "users/jane/workspace/reports/analysis.md").exists()
    monkeypatch.setattr(sys, "argv", ["pipeline", "--user", "../jane", "status"])
    with pytest.raises(SystemExit):
        cli.cli()
    monkeypatch.setattr(sys, "argv", ["pipeline", "--user", "jane", "status"])
    capsys.readouterr()
    cli.cli()
    assert json.loads(capsys.readouterr().out)["ingested"] == 1


def test_profile_indexes_do_not_become_independent_post_evidence(tmp_path):
    path = tmp_path / "profile.yaml"
    path.write_text(
        yaml.safe_dump(
            {
                "profile": {
                    "publicIdentifier": "jane",
                    "summary": "I teach practical communication skills.",
                },
                "posts": [
                    {"file": "posts/example.md", "url": "https://example.org/post"}
                ],
            }
        )
    )
    source = read_source(path, tmp_path)
    assert source.author == "jane"
    assert not any(
        "example.md" in u["text"] or "https://" in u["text"] for u in source.units
    )
    (tmp_path / "index.yaml").write_text(
        "channel_url: https://youtube.com/@jane\nvideos: []\n"
    )
    assert read_source(tmp_path / "index.yaml", tmp_path) is None
    (tmp_path / ".hidden.md").write_text(METHOD)
    assert all(not p.name.startswith(".") for p in paths(tmp_path))


def test_openrouter_retries_complete_json_and_drops_previous_usage(monkeypatch):
    calls = []

    def handle(request):
        calls.append(request)
        if len(calls) == 1:
            return httpx.Response(429, headers={"Retry-After": "0"})
        return httpx.Response(
            200,
            json={
                "usage": {"total_tokens": 10},
                "choices": [
                    {"finish_reason": "stop", "message": {"content": '{"ok":true}'}}
                ],
            },
        )

    monkeypatch.setattr("pipeline.client.time.sleep", lambda _: None)
    client = OpenRouter("fake", "test/model", transport=httpx.MockTransport(handle))
    assert client.complete("test", {}, "system", "user") == {"ok": True}
    assert len(calls) == 2
    assert json.loads(calls[-1].content)["response_format"]["json_schema"]["strict"]
    client.close()
    bad = OpenRouter(
        "fake",
        "test/model",
        transport=httpx.MockTransport(
            lambda request: httpx.Response(
                200,
                json={
                    "choices": [
                        {"finish_reason": "length", "message": {"content": "{}"}}
                    ]
                },
            )
        ),
    )
    bad.last_usage = {"total_tokens": 999}
    with pytest.raises(ModelError, match="Incomplete"):
        bad.complete("test", {}, "system", "user")
    assert bad.last_usage == {}
    bad.close()


def test_chronology_uses_main_field_citation_not_first_json_key(tmp_path):
    from pipeline.chronology import evidence_for

    data, ws = tmp_path / "data", tmp_path / "workspace"
    source = read_source(post(data), data)
    ingest_one(source, ws, FakeModel(), budget=[1])
    records, _ = read_records(ws, data)
    method = next(r for r in records if r["product"] == "knowledge")
    display = next(
        r for r in evidence_for([source], ws)[source.id] if r["id"] == method["id"]
    )
    assert display["kind"] == "teaching_move"
    assert display["quote"] == method["content"]["summary"]["citations"][0]["quote"]
    assert (
        display["quote"] != method["content"]["constraints"][0]["citations"][0]["quote"]
    )


def test_pilot_uses_current_pipeline_and_preserves_lifetime_cap(tmp_path, monkeypatch):
    from scripts import run_pipeline_pilot

    data, ws = tmp_path / "data", tmp_path / "workspace"
    output = tmp_path / "pilot.json"
    post(data)
    clients = []

    class OfflineClient(FakeModel):
        def __init__(self, key, model):
            super().__init__()
            self.model = model
            clients.append(self)

    monkeypatch.setattr("pipeline.client.OpenRouter", OfflineClient)
    monkeypatch.setenv("OPENROUTER_API_KEY", "offline-test-key")
    args = [
        "pilot",
        "--data",
        str(data),
        "--workspace",
        str(ws),
        "--output",
        str(output),
        "--max-calls",
        "1",
    ]
    monkeypatch.setattr(sys, "argv", args)
    run_pipeline_pilot.main()
    report = load_json(output)
    assert report["records"] == 2 and report["total_logical_calls"] == 1
    assert report["code_root"] == str(cli.ROOT)
    run_pipeline_pilot.main()
    assert sum(client.calls for client in clients) == 1
    post(data, "second")
    with pytest.raises(SystemExit) as stopped:
        run_pipeline_pilot.main()
    assert stopped.value.code == 1
    assert load_json(ws / "pilot-meter.json")["calls"] == 1
    assert sum(client.calls for client in clients) == 1
    monkeypatch.setattr(sys, "argv", args + ["--code-root", "."])
    with pytest.raises(SystemExit) as invalid:
        run_pipeline_pilot.main()
    assert invalid.value.code == 2


def test_existing_mcp_entry_points_still_use_core(tmp_path, monkeypatch):
    from pipeline import mcp

    monkeypatch.setattr(mcp, "ROOT", tmp_path)
    root = tmp_path / "users/jane/data"
    post(root)
    model = FakeModel()
    monkeypatch.setattr(mcp, "_get_client", lambda _: model)
    assert "using 1 extraction call" in mcp.run_ingest("jane", max_calls=1)
    assert "using 0 extraction call" in mcp.run_ingest("jane", max_calls=0)
    assert "Build completed" in mcp.build_wiki("jane", max_calls=0)
    assert "compiled" in mcp.analyze_persona("jane")
    assert json.loads(mcp.lint_workspace("jane"))["sources"] == 1
    assert (
        "training-practice" in json.loads(mcp.get_wiki_topic("jane", "list"))["topics"]
    )
    assert "Unknown report" in mcp.read_report("jane", "../../secret")
    assert "Invalid topic" in mcp.get_wiki_topic("jane", "../secret")
