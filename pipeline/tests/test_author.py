from unittest.mock import MagicMock, patch
from pathlib import Path
from pipeline.author import format_clips_context, author_scenario_prompt


def test_format_clips_context():
    clips = [
        {
            "path": "test.md",
            "span": {"start_line": 10, "end_line": 20},
            "title": "Handling Stalling",
            "tags": [{"facet": "situation", "label": "client stalls"}],
            "verbatim_text": "Hello world from the transcript.",
        }
    ]
    formatted = format_clips_context(clips)
    assert "EVIDENCE CLIP 1" in formatted
    assert "test.md" in formatted
    assert "lines 10-20" in formatted
    assert "Hello world from the transcript." in formatted


@patch("pipeline.author.retrieve")
@patch("pipeline.author.OpenRouter")
def test_author_scenario_prompt(mock_openrouter_class, mock_retrieve, tmp_path):
    mock_retrieve.return_value = {
        "clips": [
            {
                "path": "video.md",
                "span": {"start_line": 1, "end_line": 5},
                "title": "Overcoming Objection",
                "tags": [{"facet": "topic", "label": "sales"}],
                "verbatim_text": "Do not defend the price.",
            }
        ]
    }

    mock_client = MagicMock()
    mock_resp = MagicMock()
    mock_resp.json.return_value = {
        "choices": [{"message": {"content": "# Runtime Scenario Prompt\n\n- Role: Sales Trainer"}}]
    }
    mock_client.http.post.return_value = mock_resp
    mock_openrouter_class.return_value = mock_client

    workspace = tmp_path / "workspace"
    data_dir = tmp_path / "data"
    workspace.mkdir()
    data_dir.mkdir()

    out_path, content = author_scenario_prompt(
        workspace, data_dir, "Handling price defense", "fake-key"
    )

    assert out_path.exists()
    assert "Runtime Scenario Prompt" in content
    assert out_path.name == "handling-price-defense.md"
