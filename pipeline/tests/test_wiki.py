"""Linked wiki contracts, including organization cache and original-source boundaries."""

import json
from copy import deepcopy

import pytest

from pipeline.core import build, ingest_one, lint, read_records
from pipeline.organization import (
    organization_windows,
    organize,
    source_units,
    validate_source,
    validate_topics,
)
from pipeline.sources import read_source
from pipeline.storage import file_hash, load_json
from pipeline.tests.helpers import (
    FakeModel,
    post,
    repair_sections,
    selected_citations,
    transcript,
)
from pipeline.wiki import browse


class WikiModel(FakeModel):
    def complete(self, name, schema, system, user):
        payload = json.loads(user.split("\nValidation error:", 1)[0])
        if name in {"wiki_source", "wiki_source_repair"}:
            self.calls += 1
            self.operations.append(name)
            units = payload["units"]
            episodes = []
            for part in dict.fromkeys(u["part"] for u in units):
                group = [u for u in units if u["part"] == part]
                first, last = group[0], group[-1]
                episodes.append(
                    {
                        "title": "Source explanation " + part,
                        "start_unit_id": first["id"],
                        "end_unit_id": last["id"],
                        "topics": ["training_practice"],
                        "activities": ["teaching"],
                        "summary": {
                            "text": "An explanation in this source.",
                            "citations": [
                                {"unit_id": first["id"], "quote": first["text"]}
                            ],
                        },
                        "moves": [
                            {
                                "unit_id": u["id"],
                                "quote": u["text"],
                                "action": "explains",
                                "role": "instructor",
                            }
                            for u in group
                        ],
                    }
                )
            mentions = [
                {"unit_id": u["id"], "quote": "React"}
                for u in units
                if "React" in u["text"]
            ]
            result = {
                "entities": [{"kind": "product", "mentions": mentions}]
                if mentions
                else [],
                "episodes": episodes,
            }
            if schema:
                result["episodes"] = selected_citations(episodes, units)
                for entity in result["entities"]:
                    entity["mentions"] = [
                        {
                            "unit_id": m["unit_id"],
                            "start_word": next(
                                i
                                for i, word in enumerate(
                                    next(u for u in units if u["id"] == m["unit_id"])[
                                        "text"
                                    ].split()
                                )
                                if "React" in word
                            ),
                            "end_word": next(
                                i
                                for i, word in enumerate(
                                    next(u for u in units if u["id"] == m["unit_id"])[
                                        "text"
                                    ].split()
                                )
                                if "React" in word
                            ),
                        }
                        for m in entity["mentions"]
                    ]
            return repair_sections(result, payload)
        if name == "wiki_topics":
            self.calls += 1
            self.operations.append(name)
            return {
                "topics": [
                    {
                        "name": "Learning",
                        "parent_name": None,
                        "aliases": [],
                    },
                    {
                        "name": "Training practice",
                        "parent_name": "Learning",
                        "aliases": payload["labels"],
                    },
                ]
            }
        return super().complete(name, schema, system, user)


def test_offline_views_then_organized_wiki_and_cached_resume(tmp_path):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    source = read_source(post(data), data)
    model = WikiModel()
    ingest_one(source, ws, model, budget=[1])
    before = {
        p: file_hash(p)
        for d in ("sources", "evidence", "manifest")
        for p in (ws / d).glob("*")
    }
    build(ws, data)
    assert all(
        (ws / "wiki" / d / "index.md").exists()
        for d in ("topics", "entities", "methods", "episodes", "expression", "sources")
    )
    assert len(list((ws / "wiki/methods").glob("*.md"))) == 2
    assert (
        "60-second"
        in next(
            p for p in (ws / "wiki/methods").glob("*.md") if p.name != "index.md"
        ).read_text()
    )
    assert "not been run" in (ws / "wiki/sources" / f"{source.id}.md").read_text()
    organize(ws, data, model, budget=[2])
    assert model.calls == 3
    catalog = load_json(ws / "wiki/catalog.json")
    assert len(catalog["episodes"]) == 1
    assert {t["id"] for t in catalog["topics"]} == {"learning", "training-practice"}
    assert (
        r"training\_practice" in (ws / "wiki/topics/training-practice.md").read_text()
    )
    assert (
        "training_practice"
        in next(t for t in catalog["topics"] if t["id"] == "training-practice")[
            "aliases"
        ]
    )
    assert browse(ws, activity="teaching", kind="episodes")["entries"]
    assert not browse(ws, activity="interviewing")["entries"]
    assert lint(ws, data, wiki_only=True)["sources"] == 1
    hashes = {p: file_hash(p) for p in before}
    assert hashes == before  # Organization never rewrites source/extraction evidence.
    organized_hash = file_hash(ws / "organization/build.json")
    organize(ws, data, model, budget=[0])
    assert model.calls == 3
    assert organized_hash == file_hash(ws / "organization/build.json")
    assert all(
        r["semantic_status"] == "not_reviewed" for r in read_records(ws, data)[0]
    )


def test_captions_descriptions_comments_and_unknown_voices_are_separate(tmp_path):
    p = tmp_path / "instagram/reel.md"
    p.parent.mkdir()
    p.write_text(
        "---\nauthor: jane\ntranscript: true\ndescription: Learn React with examples.\n---\n\n## Caption\nA question? 👀\n\nA second paragraph.\n\n#React #Learning\n\n## Transcript\n\n### 00:00:00 · Speaker 7\nNever.\n\n## Comments (2)\n\n### Someone Else\n> Good explanation of React.\n\n### Jane (Author)\n> Thank you for the question.\n"
    )
    source = read_source(p, tmp_path)
    units = source_units(source)
    assert {u["part"] for u in units} >= {
        "description",
        "caption",
        "transcript",
        "comment",
    }
    assert any("#React" in u["text"] for u in units)
    voice = next(u for u in units if u["part"] == "transcript")
    assert voice["speaker_name"] is None and voice["author"] is None
    comments = [u for u in units if u["part"] == "comment"]
    assert comments[0]["author"] is None and comments[1]["author"] == "jane"
    assert "### Someone Else" in comments[0]["text"]
    assert "### Jane (Author)" in comments[1]["text"]
    assert "\n\n" in next(u["text"] for u in units if u["part"] == "caption")
    model = WikiModel()
    raw = model.complete("wiki_source", {}, "", json.dumps({"units": units}))
    result = validate_source(raw, units)
    short_name = deepcopy(raw)
    short_name["entities"][0]["mentions"] = [
        {"unit_id": raw["entities"][0]["mentions"][0]["unit_id"], "quote": "React"}
    ]
    assert validate_source(short_name, units)["entities"][0]["name"] == "React"
    header_name = {
        "entities": [
            {
                "kind": "person",
                "mentions": [{"unit_id": comments[1]["id"], "quote": "Jane"}],
            }
        ],
        "episodes": [],
    }
    assert validate_source(header_name, units)["entities"]
    invalid = deepcopy(raw)
    invalid["entities"][0]["mentions"][0]["quote"] = (
        "This text was never in the source."
    )
    rejected = validate_source(invalid, units)
    assert rejected["entities"] == [] and rejected["omitted_entities"] == 1
    invalid = deepcopy(raw)
    invalid["entities"][0]["mentions"][0]["quote"] = "React Software Corporation"
    assert validate_source(invalid, units)["entities"] == []
    invalid = deepcopy(raw)
    invalid["episodes"][0]["summary"]["citations"][0]["quote"] = (
        "Fabricated episode evidence."
    )
    with pytest.raises(ValueError, match="wiki citation"):
        validate_source(invalid, units)
    invalid = deepcopy(raw)
    invalid["episodes"][0]["end_unit_id"] = units[-1]["id"]
    with pytest.raises(ValueError, match="content parts"):
        validate_source(invalid, units)
    assert result["episodes"]


def test_organization_windows_keep_content_parts_separate_and_ordered():
    units = [
        {"id": f"u{i}", "part": part, "text": "Exact source passage."}
        for i, part in enumerate(
            ("title", "description", "caption", "transcript", "comment", "comment")
        )
    ]
    windows = organization_windows(units, 60000)
    assert len(windows) == 5
    assert [u for window in windows for u in window] == units
    assert all(len({u["part"] for u in window}) == 1 for window in windows)
    assert windows[-1] == units[-2:]


def test_short_comment_citation_uses_body_length_not_author_heading(tmp_path):
    p = tmp_path / "post.md"
    p.write_text(
        "A useful authored passage.\n\n## Comments (1)\n\n### @reader\n> 👏👏👏👏\n"
    )
    units = source_units(read_source(p, tmp_path))
    comment = next(u for u in units if u["part"] == "comment")
    raw = {
        "entities": [],
        "episodes": [
            {
                "title": "Reader response",
                "start_unit_id": comment["id"],
                "end_unit_id": comment["id"],
                "topics": ["feedback"],
                "activities": ["discussion"],
                "summary": {
                    "text": "The reader applauds.",
                    "citations": [
                        {
                            "unit_id": comment["id"],
                            "quote": "👏👏👏👏",
                        }
                    ],
                },
                "moves": [],
            }
        ],
    }
    assert validate_source(raw, units)["episodes"]
    raw["episodes"][0]["summary"]["citations"][0]["quote"] = "👏👏"
    with pytest.raises(ValueError, match="wiki citation"):
        validate_source(raw, units)
    comment["text"] = "### @reader\n> 👏👏👏👏 This is a much longer comment."
    raw["episodes"][0]["summary"]["citations"][0]["quote"] = "👏👏👏👏"
    with pytest.raises(ValueError, match="wiki citation"):
        validate_source(raw, units)


def test_indented_yaml_description_separator_is_not_frontmatter_end(tmp_path):
    p = tmp_path / "video.md"
    p.write_text(
        "---\ntitle: Lesson\ndescription: 'First section\n\n  ---\n\n  Second section'\n---\n\nA useful lesson body.\n"
    )
    source = read_source(p, tmp_path)
    units = source_units(source)
    description = next(u for u in units if u["part"] == "description")
    assert description["text"] == "First section\n---\nSecond section"
    assert any(u["text"] == "A useful lesson body." for u in units)


def test_ordered_episodes_and_safe_complete_topic_mapping(tmp_path):
    source = read_source(transcript(tmp_path), tmp_path)
    units = source_units(source)
    raw = WikiModel().complete("wiki_source", {}, "", json.dumps({"units": units}))
    raw["episodes"][0]["moves"].reverse()
    with pytest.raises(ValueError, match="source order"):
        validate_source(raw, units)
    topic = {
        "id": "training",
        "name": "Training",
        "parent_id": None,
        "aliases": ["a", "b"],
    }
    assert validate_topics({"topics": [topic]}, ["a", "b"])
    for change, error in (
        ({"parent_id": "training"}, "Cycle"),
        ({"id": "../bad"}, "unsafe"),
        ({"aliases": ["a"]}, "exactly once"),
    ):
        with pytest.raises(ValueError, match=error):
            validate_topics({"topics": [{**topic, **change}]}, ["a", "b"])


def test_transcription_boundary_quotes_are_exact_and_keep_both_unit_references():
    units = [
        {
            "id": "u1",
            "text": "The definition comes",
            "part": "transcript",
            "speaker_id": "1",
            "author": None,
            "locator": "first",
        },
        {
            "id": "u2",
            "text": "before practical examples.",
            "part": "transcript",
            "speaker_id": "1",
            "author": None,
            "locator": "second",
        },
    ]
    raw = {
        "entities": [],
        "episodes": [
            {
                "title": "Explanation",
                "start_unit_id": "u2",
                "end_unit_id": "u2",
                "topics": ["learning"],
                "activities": ["teaching"],
                "summary": {
                    "text": "Explains the order.",
                    "citations": [
                        {
                            "unit_id": "u2",
                            "quote": "The definition comes before practical examples.",
                        }
                    ],
                },
                "moves": [],
            }
        ],
    }
    result = validate_source(raw, units)
    citation = result["episodes"][0]["summary"]["citations"][0]
    assert citation["unit_id"] == "u1" and citation["end_unit_id"] == "u2"
    assert result["episodes"][0]["unit_ids"] == ["u1", "u2"]
    assert raw["episodes"][0]["start_unit_id"] == "u2"
    for invented in (
        "The definition comes Before practical examples.",
        "The definition comes with practical examples.",
    ):
        invalid = deepcopy(raw)
        invalid["episodes"][0]["summary"]["citations"][0]["quote"] = invented
        with pytest.raises(ValueError, match="Copy a short contiguous quote exactly"):
            validate_source(invalid, units)
    units[1]["speaker_id"] = "2"
    with pytest.raises(ValueError, match="wiki citation"):
        validate_source(raw, units)
    units[0]["speaker_id"] = units[1]["speaker_id"] = None
    with pytest.raises(ValueError, match="wiki citation"):
        validate_source(raw, units)


def test_invalid_source_organization_does_not_block_later_sources(tmp_path):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    bad = read_source(post(data, "a-bad"), data)
    good = read_source(post(data, "b-good"), data)

    class InvalidSourceModel(WikiModel):
        def complete(self, name, schema, system, user):
            result = super().complete(name, schema, system, user)
            payload = json.loads(user.split("\nValidation error:", 1)[0])
            if (
                name in {"wiki_source", "wiki_source_repair"}
                and payload["source_id"] == bad.id
            ):
                result["episodes"][0]["summary"]["citations"][0]["quote"] = (
                    "Invented source passage."
                )
            return result

    model = InvalidSourceModel()
    for source in (bad, good):
        ingest_one(source, ws, model, budget=[1])
    with pytest.raises(RuntimeError, match="Wiki organization incomplete for 1 source"):
        organize(ws, data, model, budget=[4])
    assert not (ws / "organization/sources" / f"{bad.id}.json").exists()
    assert (ws / "organization/sources" / f"{good.id}.json").exists()
    catalog = load_json(ws / "wiki/catalog.json")
    assert catalog["coverage"]["organized_sources"] == 1
    assert catalog["coverage"]["unorganized_sources"] == 1
    assert catalog["coverage"]["topic_aliases_organized"]
    assert "wiki-source-incomplete" in (ws / "events.jsonl").read_text()
    assert lint(ws, data, wiki_only=True)["sources"] == 2


def test_organization_failure_keeps_previous_publication_and_stale_is_visible(tmp_path):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    p = post(data)
    model = WikiModel()
    ingest_one(read_source(p, data), ws, model, budget=[1])
    with pytest.raises(RuntimeError, match="budget"):
        organize(ws, data, model, budget=[1])
    # Completed sources survive a later topic-budget failure; no partial source is served.
    assert (ws / "organization/build.json").exists()
    assert len(load_json(ws / "wiki/catalog.json")["episodes"]) == 1
    organize(ws, data, model, budget=[1])  # source operation is cached
    p.write_text(p.read_text() + "\nLearn React through examples.\n")
    ingest_one(read_source(p, data), ws, model, budget=[1])
    build(ws, data)
    catalog = load_json(ws / "wiki/catalog.json")
    assert not catalog["episodes"] and catalog["coverage"]["stale_organization"]
    assert lint(ws, data, wiki_only=True)["sources"] == 1
    with pytest.raises(ValueError, match="No ingested source"):
        organize(ws, data, model, budget=[0], patterns=["missing/*"])
