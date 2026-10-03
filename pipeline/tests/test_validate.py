from unittest.mock import MagicMock, patch
from pipeline.validate import parse_citations, parse_rules_with_citations, validate_scenario


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


def test_parse_rules_with_citations():
    text = """
    ### Rule 1: First Heuristic
    - Trigger: When user asks X
    - Action: Do Y
    - Avoid: Do not do Z
    - Grounding Citation: `source.md` (lines 5-10)
    """
    rules = parse_rules_with_citations(text)
    assert len(rules) == 1
    assert rules[0]["rule_num"] == 1
    assert rules[0]["title"] == "First Heuristic"
    assert rules[0]["action"] == "Do Y"
    assert rules[0]["file"] == "source.md"
    assert rules[0]["start"] == 5
    assert rules[0]["end"] == 10


@patch("pipeline.validate.JevClient")
@patch("pipeline.validate.OpenRouter")
def test_validate_scenario(mock_openrouter, mock_jev_class, tmp_path):
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

    mock_jev = MagicMock()
    mock_jev.decide.return_value = {
        "entailment": {"type": "choice", "choice": "grounded", "confidence": 0.95}
    }
    mock_jev_class.return_value = mock_jev

    skill_file = tmp_path / "skill.md"
    skill_file.write_text("""
    ## 2. Voice & Conversational Cadence
    - **Signature Phrases (Verbatim Grounded & Frequency Calibrated)**:
      - "Line 1"
    - **Pacing & Length Bounds**: strictly under 50 words
    - **Turn-Taking Protocol**: exactly one focal diagnostic question

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
    assert report["jev_entailment_audit"]["total_rules_checked"] == 1
    assert report["jev_entailment_audit"]["grounded_rules"] == 1
    assert report["signature_phrase_audit"]["verified_phrases"] == 1
    assert report["cadence_audit"]["passed"] is True


@patch("pipeline.validate.JevClient")
@patch("pipeline.validate.OpenRouter")
def test_validate_scenario_fails_closed_on_jev_failure(mock_openrouter, mock_jev_class, tmp_path):
    mock_judge = MagicMock()
    mock_judge.complete.return_value = {
        "verdict": "PASS",
        "grounding_score": 10,
        "voice_authenticity_score": 9,
        "gemini_adherence_readiness": 10,
        "hallucinations_found": [],
        "unsupported_claims": [],
        "summary": "Judge thinks it passed",
    }
    mock_openrouter.return_value = mock_judge

    # Simulate Jev API returning empty answers on error
    mock_jev = MagicMock()
    mock_jev.decide.return_value = {}
    mock_jev_class.return_value = mock_jev

    skill_file = tmp_path / "skill.md"
    skill_file.write_text("""
    ## 2. Voice & Conversational Cadence
    - **Pacing & Length Bounds**: strictly under 50 words
    - **Turn-Taking Protocol**: exactly one focal diagnostic question

    ### Rule 1: Grounded Rule
    - Trigger: X
    - Action: Y
    - Grounding Citation: `source.md` (lines 1-2)
    """)

    source_file = tmp_path / "source.md"
    source_file.write_text("Line 1\nLine 2\n")

    report = validate_scenario(skill_file, tmp_path, "fake-key")
    # MUST FAIL CLOSED: Even if LLM judge passed, empty Jev result forces FAIL verdict
    assert report["judge_evaluation"]["verdict"] == "FAIL"
    assert len(report["jev_entailment_audit"]["hallucinations"]) == 1
    assert any("[Jev Entailment Failure]" in h for h in report["judge_evaluation"]["hallucinations_found"])


@patch("pipeline.validate.JevClient")
@patch("pipeline.validate.OpenRouter")
def test_validate_scenario_fails_on_fabricated_signature_phrase(mock_openrouter, mock_jev_class, tmp_path):
    mock_judge = MagicMock()
    mock_judge.complete.return_value = {
        "verdict": "PASS",
        "grounding_score": 10,
        "voice_authenticity_score": 9,
        "gemini_adherence_readiness": 10,
        "hallucinations_found": [],
        "unsupported_claims": [],
        "summary": "Passed",
    }
    mock_openrouter.return_value = mock_judge

    mock_jev = MagicMock()
    mock_jev.decide.return_value = {
        "entailment": {"type": "choice", "choice": "grounded", "confidence": 0.95}
    }
    mock_jev_class.return_value = mock_jev

    skill_file = tmp_path / "skill.md"
    skill_file.write_text("""
    ## 2. Voice & Conversational Cadence
    - **Signature Phrases (Verbatim Grounded & Frequency Calibrated)**:
      - "Totally Fabricated Catchphrase That Never Appeared"
    - **Pacing & Length Bounds**: strictly under 50 words
    - **Turn-Taking Protocol**: exactly one focal diagnostic question

    ### Rule 1: Grounded Rule
    - Trigger: X
    - Action: Y
    - Grounding Citation: `source.md` (lines 1-2)
    """)

    source_file = tmp_path / "source.md"
    source_file.write_text("Line 1\nLine 2\n")

    report = validate_scenario(skill_file, tmp_path, "fake-key")
    assert report["judge_evaluation"]["verdict"] == "FAIL"
    assert report["signature_phrase_audit"]["verified_phrases"] == 0
    assert any("[Fabricated Signature Phrase]" in h for h in report["judge_evaluation"]["hallucinations_found"])


@patch("pipeline.validate.JevClient")
@patch("pipeline.validate.OpenRouter")
def test_validate_scenario_fails_on_missing_cadence_bounds(mock_openrouter, mock_jev_class, tmp_path):
    mock_judge = MagicMock()
    mock_judge.complete.return_value = {
        "verdict": "PASS",
        "grounding_score": 10,
        "voice_authenticity_score": 9,
        "gemini_adherence_readiness": 10,
        "hallucinations_found": [],
        "unsupported_claims": [],
        "summary": "Passed",
    }
    mock_openrouter.return_value = mock_judge

    mock_jev = MagicMock()
    mock_jev.decide.return_value = {
        "entailment": {"type": "choice", "choice": "grounded", "confidence": 0.95}
    }
    mock_jev_class.return_value = mock_jev

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
    assert report["judge_evaluation"]["verdict"] == "FAIL"
    assert report["cadence_audit"]["passed"] is False
    assert any("[Cadence Failure]" in u for u in report["judge_evaluation"]["unsupported_claims"])


