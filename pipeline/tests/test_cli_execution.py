"""CLI-level offline status and spending guards."""

import json
import sys

import pytest

from pipeline import __main__ as cli
from pipeline.core import build, ingest_one
from pipeline.organization import source_units
from pipeline.sources import read_source
from pipeline.tests.helpers import FakeModel, post


def test_plan_requires_no_client_and_reports_failed_parsing(
    tmp_path, monkeypatch, capsys
):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    post(data)
    (data / "broken.yaml").write_text("[invalid")
    monkeypatch.setattr(
        cli, "model_client", lambda _: pytest.fail("Plan must remain offline")
    )
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "pipeline",
            "--data",
            str(data),
            "--workspace",
            str(ws),
            "plan",
            "--model",
            "offline/fake",
        ],
    )
    cli.cli()
    result = json.loads(capsys.readouterr().out)
    assert result["errors"] and result["uncached_windows"] == 1
    assert result["cost"] is None and not ws.exists()


def test_completion_gate_is_distinct_from_wiki_integrity(tmp_path, monkeypatch, capsys):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    ingest_one(read_source(post(data), data), ws, FakeModel(), budget=[1])
    build(ws, data)
    post(data, "not-yet-ingested")
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "pipeline",
            "--data",
            str(data),
            "--workspace",
            str(ws),
            "lint",
            "--wiki-only",
            "--require-complete",
        ],
    )
    with pytest.raises(RuntimeError, match="processing is incomplete"):
        cli.cli()
    assert not json.loads(capsys.readouterr().out)["processing"]["ingestion_complete"]


def test_dollar_budget_requires_prices_before_constructing_client(
    tmp_path, monkeypatch
):
    data, ws = tmp_path / "data", tmp_path / "workspace"
    post(data)
    monkeypatch.setattr(
        cli,
        "model_client",
        lambda _: pytest.fail("Invalid budget must not construct a client"),
    )
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "pipeline",
            "--data",
            str(data),
            "--workspace",
            str(ws),
            "ingest",
            "--max-usd",
            "1",
        ],
    )
    with pytest.raises(SystemExit) as invalid:
        cli.cli()
    assert invalid.value.code == 2


def test_yaml_document_marker_is_not_markdown_frontmatter(tmp_path):
    p = tmp_path / "source.yaml"
    p.write_text(
        "---\ntitle: Test source\ncontent: A useful example of preserved source text.\n"
    )
    assert source_units(read_source(p, tmp_path))
