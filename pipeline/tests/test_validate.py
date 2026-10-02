from unittest.mock import MagicMock, patch
from pipeline.validate import parse_citations, validate_scenario


def test_parse_citations():
    text = """
    ### Rule 1
    - Grounding Citation: `test.md` (lines 10-25)
    ### Rule 2
    - Grounding Citation: "another.md" (lines 30-50)
    """
    cites = parse_citations(text)
    assert len(cites) == 2
    assert cites[0] == ("test.md", 10, 25)
    assert cites[1] == ("another.md", 30, 50)


@patch("pipeline.validate.OpenRouter")
def test_validate_scenario(mock_openrouter, tmp_path):
    mock_judge = MagicMock()
    mock_judge.complete.return_value = {
        "verdict": "PASS",
        "grounding_score": 10,
        "voice_authenticity_score": 9,
        "gemini_adherence_readiness": 10,
        "hallucinations_found": [],
        "unsupported_claims": [],
        "summary": "Passed audit cleanly",
    }
    mock_openrouter.return_value = mock_judge

    skill_file = tmp_path / "skill.md"
    skill_file.write_text("""
    ### Rule 1: Grounded Rule
    - Trigger: X
    - Action: Y
    - Grounding Citation: `source.md` (lines 1-2)
    """)

    source_file = tmp_path / "source.md"
    source_file.write_text("Line 1\nLine 2\n")

    report = validate_scenario(skill_file, tmp_path, "fake-key")
    assert report["judge_evaluation"]["verdict"] == "PASS"
    assert report["citation_integrity"]["valid_citations"] == 1
    assert report["judge_evaluation"]["grounding_score"] == 10
