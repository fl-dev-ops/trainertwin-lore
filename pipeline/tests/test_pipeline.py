import json
import re
import sys

import httpx
import pytest
import yaml

from pipeline import __main__ as pipeline_cli
from pipeline import chronology
from pipeline.chronology import evidence_for, published_datetime
from pipeline.client import ModelError, OpenRouter
from pipeline.core import (
    analyze,
    build,
    chunks,
    extract_items,
    group_topics,
    ingest_one,
    lint,
    load_json,
    read_source,
    validate_findings,
    verification_overlay,
)
from pipeline.sources import normalize_date, paths, source_id


class FakeModel:
    model = "offline/fake"

    def __init__(self, fail_at=0):
        self.calls = 0
        self.fail_at = fail_at

    def complete(self, name, schema, system, user):
        self.calls += 1
        if self.calls == self.fail_at:
            raise RuntimeError("temporary failure")
        if name == "source_evidence":
            match = re.search(r"\[(u\d{6})\] [^\n]+?: ([^\n]+)", user)
            assert match
            return {
                "overview": "Coaching commentary on a client interaction.",
                "items": [
                    {
                        "kind": "advice",
                        "context": "advised",
                        "topic": "client discovery",
                        "statement": "Ask about the client's goals before proposing property options.",
                        "unit_id": match[1],
                        "quote": match[2][:35],
                    }
                ],
            }
        if name == "wiki_topic_groups":
            labels = [x["topic"] for x in json.loads(user)]
            return {"groups": [{"name": "client discovery", "topics": labels}]}
        if name == "platform_behavior":
            payload = json.loads(user)
            plat = payload.get("platform", "general")
            return {
                "platform": plat,
                "confidence": (
                    "provisional" if payload.get("source_count", 0) < 5 else "high"
                ),
                "summary": f"Observed communication style and behavior on {plat}.",
                "content_patterns": [
                    f"Posts educational breakdowns and examples on {plat}."
                ],
                "communication_style": [
                    f"Direct and structured communication style on {plat}."
                ],
                "decision_rules": ["Validates claims before proceeding with advice."],
                "key_phrases": ["Ask about goals before pitching"],
            }
        batch = json.loads(user.split("Current source-backed evidence:\n", 1)[1])
        refs = []
        for item in batch:
            refs.extend(item.get("support_ids", [item.get("id")]))
        return {
            "findings": [
                {
                    "finding": "The example supports asking questions before a property pitch.",
                    "support_ids": list(dict.fromkeys(refs))[:3],
                    "counter_ids": [],
                    "qualification": "This is transcript-derived advice, not independently verified behavior.",
                }
            ]
        }

    def decide(self, state, questions, *, model="typesafe/jev-1.13"):
        answers = {}
        for q_name, q_val in questions.items():
            q_type = q_val.get("type", "noul")
            if q_type == "noul":
                answers[q_name] = {"type": "noul", "noul": 0.9}
            elif q_type == "choice":
                opts = list(q_val.get("criteria", q_val.get("options", {})))
                pick = opts[0] if opts else "default"
                answers[q_name] = {
                    "type": "choice",
                    "choice": pick,
                    "confidence": 0.95,
                }
        return answers


def make_source(folder, ident, count=4):
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{ident}.yaml"
    path.write_text(
        yaml.safe_dump(
            {
                "id": ident,
                "title": f"Interview {ident}",
                "duration": "00:01:00",
                "turns": [
                    {
                        "t": f"00:00:{i:02d}",
                        "speaker": "1",
                        "text": f"Ask a buyer about their goals and needs before sharing listings number {i}.",
                    }
                    for i in range(count)
                ],
            }
        )
    )
    return path


def test_ingest_build_resume_and_changed_source(tmp_path):
    src_dir = tmp_path / "transcripts"
    one = make_source(src_dir, "01", 4)
    make_source(src_dir, "02", 2)
    ws = tmp_path / "workspace"
    model = FakeModel()
    source = read_source(one)
    assert len(chunks(source, 1000)) == 1
    assert ingest_one(source, ws, model, max_chars=1000, budget=[10])
    assert model.calls == 1
    assert not ingest_one(source, ws, model, max_chars=1000, budget=[0])
    ingest_one(read_source(src_dir / "02.yaml"), ws, model, max_chars=1000, budget=[10])
    build(ws, src_dir, model, budget=[10], max_chars=5000)
    assert not (ws / "wiki" / "analysis.md").exists()
    assert not (ws / "reports" / "analysis.md").exists()
    assert (ws / "wiki" / "topics" / "client-discovery.md").exists()
    assert len((ws / "wiki" / "log.md").read_text().splitlines()) == 6
    report = analyze(ws)
    assert "Wiki-derived research draft" in report.read_text()
    topic = ws / "wiki" / "topics" / "client-discovery.md"
    topic.write_text(topic.read_text() + "\nWiki-only editorial note.\n")
    with pytest.raises(ValueError, match="Stale analysis"):
        lint(ws, src_dir)
    analyze(ws)
    assert "Wiki-only editorial note." in report.read_text()
    assert "Cross-topic synthesis" in report.read_text()
    assert lint(ws, src_dir) == {"sources": 2, "evidence": 2, "topics": 1}
    old_calls = model.calls
    build(ws, src_dir, model, budget=[0], max_chars=5000)
    assert model.calls == old_calls
    assert lint(ws, src_dir)["sources"] == 2
    make_source(src_dir, "01", 5)
    with pytest.raises(ValueError, match="changed"):
        build(ws, src_dir, model, budget=[10], max_chars=5000)
    assert ingest_one(read_source(one), ws, model, max_chars=1000, budget=[10])
    build(ws, src_dir, model, budget=[10], max_chars=5000)
    with pytest.raises(ValueError, match="Stale analysis"):
        lint(ws, src_dir)
    analyze(ws)
    assert lint(ws, src_dir)["sources"] == 2


def test_user_roots_isolate_sources_and_reports(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(pipeline_cli, "ROOT", tmp_path)
    for user in ("olga", "jane-doe"):
        root = tmp_path / "users" / user / "data"
        make_source(root / "youtube" / "transcripts", user)
        workspace = tmp_path / "users" / user / "workspace"
        source = read_source(next(root.rglob("*.yaml")), root)
        ingest_one(source, workspace, FakeModel(), max_chars=1000, budget=[1])
        build(workspace, root, FakeModel(), budget=[10])
        analyze(workspace, user=user)
        report = (workspace / "reports" / "analysis.md").read_text()
        assert lint(workspace, root)["sources"] == 1
        assert "## 1. Platform-by-Platform Behavior & Communication" in report
        assert (workspace / "wiki" / "behavior" / "youtube.md").exists()
        assert (workspace / "reports" / "timeline.md").exists()

    monkeypatch.setattr(sys, "argv", ["pipeline", "--user", "jane-doe", "status"])
    pipeline_cli.cli()
    assert "files=1 ingested=1 stale=[]" in capsys.readouterr().out
    monkeypatch.setattr(sys, "argv", ["pipeline", "--user", "../olga", "status"])
    with pytest.raises(SystemExit):
        pipeline_cli.cli()
    monkeypatch.setattr(
        sys,
        "argv",
        ["pipeline", "--data", str(tmp_path / "users" / "jane-doe" / "data"), "status"],
    )
    with pytest.raises(SystemExit):
        pipeline_cli.cli()


def test_recursive_mixed_sources_share_topic(tmp_path):
    root = tmp_path / "data"
    youtube = root / "youtube" / "transcripts"
    linkedin = root / "linkedin" / "posts"
    make_source(youtube, "01")
    linkedin.mkdir(parents=True)
    post = linkedin / "buyers.md"
    post.write_text(
        "---\ndate: 2026-09-21\nurl: https://example.org/post\n---\n\nAsk a buyer about their goals and needs before sharing listings.\n"
    )
    raw = root / "other" / "notes.json"
    raw.parent.mkdir()
    raw.write_text(
        json.dumps(
            {
                "notes": [
                    "Ask a buyer about their goals and needs before sharing listings."
                ]
            }
        )
    )
    (raw.parent / "job.json").write_text('{"job_id": "123"}')
    (youtube.parent / "olga.yaml").write_text(
        yaml.safe_dump(
            {
                "channel_url": "https://www.youtube.com/@OlgaSinenkoRealEstate/videos",
                "videos": [
                    {"title": "Example lecture on real estate coaching", "id": "123"}
                ],
            }
        )
    )
    (root / "twitter").mkdir()
    (root / "twitter" / "olga-tweets.yaml").write_text(
        yaml.safe_dump(
            {
                "tweets": [
                    {
                        "file": "./tweets/post.md",
                        "url": "https://x.com/Olga_Si_Sales/status/123",
                    }
                ]
            }
        )
    )
    found = [s for p in paths(root) if (s := read_source(p, root))]
    assert len(found) == 3
    by_channel = {s.category: s for s in found}
    assert by_channel["linkedin"].id == source_id(post, root)
    assert by_channel["linkedin"].title.startswith("Ask a buyer")
    assert by_channel["linkedin"].units[0]["locator"] == "lines 6-6"
    assert by_channel["other"].units[0]["locator"] == "/notes/0"
    ws = tmp_path / "workspace"
    model = FakeModel()
    for source in found:
        ingest_one(source, ws, model, max_chars=1000, budget=[10])
    build(ws, root, model, budget=[30], max_chars=5000)
    assert lint(ws, root)["sources"] == 3
    topic = (ws / "wiki" / "topics" / "client-discovery.md").read_text()
    assert "linkedin" in topic and "youtube" in topic
    assert (ws / "wiki" / "channels" / "linkedin.md").exists()
    assert (ws / "wiki" / "categories" / "methods.md").exists()
    assert model.calls > 3
    build(ws, root, model, budget=[0], max_chars=5000)


def test_publication_metadata_and_sidecar_update(tmp_path):
    root = tmp_path / "data"
    post = root / "twitter" / "tweets" / "note.md"
    post.parent.mkdir(parents=True)
    post.write_text(
        "---\nid: '123'\ndate: 'Sun Aug 02 03:00:09 +0000 2026'\nurl: https://x.com/Olga_Si_Sales/status/123\n---\n\nAsk clients what matters to them before describing a property.\n"
    )
    source = read_source(post, root)
    assert source.date == "2026-08-02T03:00:09Z"
    assert source.external_id == "123"
    assert source.author == "Olga_Si_Sales"
    assert source.date_basis == "source"
    assert normalize_date("2026-04-15") == "2026-04-15"
    ws = tmp_path / "workspace"
    model = FakeModel()
    ingest_one(source, ws, model, max_chars=1000, budget=[1])
    evidence = (
        ws
        / "evidence"
        / load_json(ws / "manifest" / f"{source.id}.json")["evidence_file"]
    )
    assert json.loads(evidence.read_text())["published_at"] == source.date
    assert json.loads(evidence.read_text())["external_id"] == "123"
    sidecar = root / ".source-metadata.yaml"
    sidecar.write_text(
        yaml.safe_dump(
            {"twitter/tweets/note.md": {"date": "2026-08-03", "author": "Olga"}}
        )
    )
    changed = read_source(post, root)
    assert changed.date == "2026-08-03" and changed.date_basis == "sidecar"
    assert len(evidence_for([changed], ws)[changed.id]) == 1
    assert published_datetime(changed.date).utcoffset().total_seconds() == 0
    with pytest.raises(ValueError, match="metadata"):
        build(ws, root, model, budget=[10])
    assert ingest_one(changed, ws, model, max_chars=1000, budget=[0])
    assert model.calls == 1  # metadata changes reuse exact-content extraction
    build(ws, root, model, budget=[10])
    assert "2026-08-03" in (ws / "wiki" / "timeline.md").read_text()
    assert lint(ws, root)["sources"] == 1


def test_chronology_withholds_unmatched_youtube_metadata(tmp_path, monkeypatch):
    root = tmp_path / "users" / "olga" / "data"
    video = root / "youtube" / "transcripts" / "01.yaml"
    video.parent.mkdir(parents=True)
    video.write_text(
        yaml.safe_dump(
            {
                "title": "A new unverified video title",
                "turns": [
                    {
                        "t": "00:00:01",
                        "speaker": "0",
                        "text": "This transcript has content but no publication metadata.",
                    }
                ],
            }
        )
    )
    post = root / "linkedin" / "posts" / "dated.md"
    post.parent.mkdir(parents=True)
    post.write_text(
        "---\ndate: '2026-03-01'\nurl: https://www.linkedin.com/posts/olgasi_example\n---\n\nA dated source with substantive text and an original URL.\n"
    )
    selection = tmp_path / "pilot-sources.txt"
    selection.write_text("youtube/transcripts/01.yaml\nlinkedin/posts/dated.md\n")
    monkeypatch.setattr(chronology, "ROOT", tmp_path)
    monkeypatch.setattr(chronology, "SELECTION", selection)
    selected, omitted = chronology.selected_sources()
    assert [s.path for s in selected] == [post]
    assert omitted == ["youtube/transcripts/01.yaml"]


def test_quoted_tweet_is_not_attributed_to_author(tmp_path):
    root = tmp_path / "data"
    post = root / "twitter" / "tweets" / "post.md"
    post.parent.mkdir(parents=True)
    post.write_text(
        "---\nurl: https://x.com/Olga_Si_Sales/status/123\n---\n\nI teach agents to ask better questions.\n\n### Quoting @someone_else:\n> I invented this other person's method.\n"
    )
    source = read_source(post, root)
    assert len(source.units) == 1
    assert "I teach agents" in source.units[0]["text"]
    assert "I invented" not in source.units[0]["text"]


def test_markdown_passage_allows_adjacent_line_quote(tmp_path):
    root = tmp_path / "data"
    post = root / "linkedin" / "post.md"
    post.parent.mkdir(parents=True)
    post.write_text(
        "---\ndate: 2026-09-08\n---\n\nThis is why learning to control focus is not just positive thinking.\n\nIt is a practical life skill.\n"
    )
    source = read_source(post, root)
    assert len(source.units) == 1
    assert "positive thinking. It is a practical life skill." in source.units[0]["text"]
    assert source.units[0]["locator"] == "lines 5-7"


def test_bad_excerpt_is_repaired_once(tmp_path):
    source = read_source(make_source(tmp_path / "transcripts", "01"))

    class NeedsRepair(FakeModel):
        def complete(self, name, schema, system, user):
            result = super().complete(name, schema, system, user)
            if self.calls == 1:
                result["items"][0]["quote"] = "Unsupported fabricated quotation"
            return result

    model = NeedsRepair()
    assert ingest_one(source, tmp_path / "workspace", model, max_chars=1000, budget=[2])
    assert model.calls == 2


def test_bad_item_after_repair_is_logged_not_published(tmp_path):
    source = read_source(make_source(tmp_path / "transcripts", "01"))

    class MixedModel(FakeModel):
        def complete(self, name, schema, system, user):
            response = super().complete(name, schema, system, user)
            if name == "source_evidence":
                bad = dict(response["items"][0], unit_id="u999999")
                response["items"].append(bad)
            return response

    ws = tmp_path / "workspace"
    assert ingest_one(source, ws, MixedModel(), max_chars=1000, budget=[2])
    assert "rejected-item" in (ws / "wiki" / "log.md").read_text()
    assert lint(ws, source.path.parent)["evidence"] == 1


def test_chunk_checkpoint_and_budget(tmp_path):
    src = read_source(make_source(tmp_path / "transcripts", "01", 18))
    ws = tmp_path / "workspace"
    assert len(chunks(src, 1000)) > 1
    with pytest.raises(RuntimeError, match="budget"):
        ingest_one(src, ws, FakeModel(), max_chars=1000, budget=[1])
    assert not (ws / "manifest" / f"{src.id}.json").exists()
    cached = list((ws / "cache" / src.id).glob("*.json"))
    assert len(cached) == 1
    fake = FakeModel()
    ingest_one(src, ws, fake, max_chars=1000, budget=[10])
    assert fake.calls == len(chunks(src, 1000)) - 1
    assert lint(ws, src.path.parent)["evidence"] == len(chunks(src, 1000))


def test_large_topic_reduction_and_broken_links(tmp_path):
    source_dir = tmp_path / "transcripts"
    ws = tmp_path / "workspace"
    model = FakeModel()
    for number in range(12):
        source = read_source(make_source(source_dir, f"{number:02}"))
        ingest_one(source, ws, model, max_chars=1000, budget=[1])
    build(ws, source_dir, model, budget=[100], max_chars=1000)
    assert lint(ws, source_dir)["sources"] == 12
    assert not (ws / "reports" / "analysis.md").exists()
    report = analyze(ws)
    assert "Cross-topic synthesis" in report.read_text()
    report.write_text(report.read_text() + "\n[broken](topics/missing.md)\n")
    with pytest.raises(ValueError, match="Broken Markdown link"):
        lint(ws, source_dir)


def test_topic_grouping_merges_labels_and_resumes(tmp_path):
    cards = [
        {"topic_slug": "questioning-techniques", "statement": "Ask better questions."},
        {"topic_slug": "client-engagement", "statement": "Engage the client."},
    ]
    model = FakeModel()
    mapped = group_topics(cards, tmp_path, model, [1])
    assert mapped == {
        "questioning-techniques": "client-discovery",
        "client-engagement": "client-discovery",
    }
    assert group_topics(cards, tmp_path, model, [0]) == mapped
    assert model.calls == 1


def test_bad_synthesis_reference():
    with pytest.raises(ValueError, match="unknown or no evidence"):
        validate_findings(
            {
                "findings": [
                    {
                        "finding": "Test",
                        "support_ids": ["fake"],
                        "counter_ids": [],
                        "qualification": "unverified",
                    }
                ]
            },
            {"valid"},
        )


def test_bad_quote_and_unknown_turn_are_rejected(tmp_path):
    source = read_source(make_source(tmp_path, "01"))
    piece = chunks(source, 1000)[0]
    result = FakeModel().complete(
        "source_evidence",
        {},
        "",
        f"[{piece[0]['id'].rsplit(':', 1)[1]}] /turns/0/text time=00:00:00 speaker=1: {piece[0]['text']}",
    )
    result["items"][0]["quote"] = "A fabricated quote not in the transcript"
    with pytest.raises(ValueError, match="Unsupported excerpt"):
        extract_items(result, piece, source, 1)
    result["items"][0]["quote"] = piece[0]["text"][:35]
    result["items"][0]["unit_id"] = "u999999"
    with pytest.raises(ValueError, match="Unsupported excerpt"):
        extract_items(result, piece, source, 1)


def test_quote_punctuation_recovery_keeps_literal_source(tmp_path):
    source = read_source(make_source(tmp_path, "01"))
    unit = source.units[0]
    result = {
        "overview": "Buyer example",
        "items": [
            {
                "kind": "advice",
                "context": "advised",
                "topic": "buyer questions",
                "statement": "Ask the buyer about their goals before showing listings.",
                "unit_id": unit["id"],
                "quote": unit["text"][:-1] + "!",
            }
        ],
    }
    cards = extract_items(result, [unit], source, 1)
    assert cards[0]["quote"] == unit["text"][:-1]
    result["items"][0]["unit_id"] = unit["id"].rsplit(":", 1)[1]
    assert extract_items(result, [unit], source, 1)[0]["unit_id"] == unit["id"]


def test_verification_is_separate_human_record(tmp_path):
    src = read_source(make_source(tmp_path / "transcripts", "01"))
    ws = tmp_path / "workspace"
    ingest_one(src, ws, FakeModel(), max_chars=1000, budget=[1])
    evidence = (
        ws / "evidence" / load_json(ws / "manifest" / f"{src.id}.json")["evidence_file"]
    )
    card = json.loads(evidence.read_text())
    assert card["external_status"] == "not_checked"
    (ws / "verifications.jsonl").write_text(
        json.dumps(
            {
                "evidence_id": card["id"],
                "status": "verified",
                "url": "https://example.com/report",
                "checked_at": "2026-09-24T00:00:00Z",
                "note": "Human review",
            }
        )
        + "\n"
    )
    verification_overlay([card], ws)
    assert card["external_status"] == "verified"
    assert json.loads(evidence.read_text())["external_status"] == "not_checked"


def test_openrouter_retries_and_requires_complete_json(monkeypatch):
    calls = []

    def handle(request):
        calls.append(request)
        if len(calls) == 1:
            return httpx.Response(429, headers={"Retry-After": "0"})
        return httpx.Response(
            200,
            json={
                "choices": [
                    {"finish_reason": "stop", "message": {"content": '{"ok":true}'}}
                ]
            },
        )

    monkeypatch.setattr("pipeline.client.time.sleep", lambda _: None)
    client = OpenRouter("fake", "test/model", transport=httpx.MockTransport(handle))
    assert client.complete("test", {}, "system", "user") == {"ok": True}
    body = json.loads(calls[0].content)
    assert body["provider"]["require_parameters"] is True
    assert body["response_format"]["json_schema"]["strict"] is True
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
    with pytest.raises(ModelError, match="Incomplete"):
        bad.complete("test", {}, "system", "user")
    bad.close()


def test_mcp_server_tools(tmp_path, monkeypatch):
    from pipeline import mcp

    monkeypatch.setattr(mcp, "ROOT", tmp_path)
    root = tmp_path / "users" / "test-user" / "data"
    make_source(root / "youtube" / "transcripts", "01")
    ws = tmp_path / "users" / "test-user" / "workspace"
    source = read_source(next(root.rglob("*.yaml")), root)
    ingest_one(source, ws, FakeModel(), max_chars=1000, budget=[1])
    build(ws, root, FakeModel(), budget=[10])
    analyze(ws, user="test-user")

    status_raw = mcp.get_status("test-user")
    status_data = json.loads(status_raw)
    assert status_data["sources_ingested"] == 1
    assert status_data["stale_manifests_count"] == 0

    lint_raw = mcp.lint_workspace("test-user")
    lint_data = json.loads(lint_raw)
    assert lint_data["status"] == "ok"
    assert lint_data["evidence"] == 1

    report_text = mcp.read_report("test-user", "analysis")
    assert "Platform-by-Platform Behavior" in report_text

    topics_raw = mcp.get_wiki_topic("test-user", "list")
    topics_data = json.loads(topics_raw)
    assert "client-discovery" in topics_data["topics"]

