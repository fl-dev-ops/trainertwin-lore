"""Validate authored SKILL.md prompts against source evidence using an independent judge."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .client import OpenRouter

JUDGE_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "verdict": {"type": "string", "enum": ["PASS", "FAIL"]},
        "grounding_score": {"type": "integer", "minimum": 1, "maximum": 10},
        "voice_authenticity_score": {"type": "integer", "minimum": 1, "maximum": 10},
        "gemini_adherence_readiness": {"type": "integer", "minimum": 1, "maximum": 10},
        "hallucinations_found": {
            "type": "array",
            "items": {"type": "string"},
        },
        "unsupported_claims": {
            "type": "array",
            "items": {"type": "string"},
        },
        "summary": {"type": "string"},
    },
    "required": [
        "verdict",
        "grounding_score",
        "voice_authenticity_score",
        "gemini_adherence_readiness",
        "hallucinations_found",
        "unsupported_claims",
        "summary",
    ],
}

JUDGE_SYSTEM_PROMPT = """You are an adversarial quality assurance auditor evaluating an Agent Skill (SKILL.md) authored for an AI digital twin.
Your role is to check whether the authored prompt is grounded in real source evidence, or if it hallucinates, invents generic advice, or distorts facts.

Evaluation Criteria:
1. Grounding & Fidelity (1-10): Are the heuristics, tactics, and rules supported by the provided source evidence?
2. Voice & Authenticity (1-10): Does it capture the creator's real tone, phrases, and posture rather than generic AI assistant speech?
3. Gemini Adherence Readiness (1-10): Does it have turn bounds (2-4 sentences), frequency calibration for verbal ticks, and explicit "Never" boundaries?
4. Hallucinations / Unsupported Claims: Identify ANY assertion or rule that cannot be verified in the provided evidence.

If there are fabricated core tactics or facts, verdict MUST be FAIL. Otherwise PASS."""


def parse_citations(content: str) -> list[tuple[str, int, int]]:
    """Extract `file.md` (lines X-Y) citations from content."""
    matches = re.findall(
        r'[`"]?([^`"\n\s]+\.(?:md|yaml))[`"]?\s*\(lines?\s*(\d+)\s*[-–]\s*(\d+)\)',
        content,
    )
    return [(f, int(s), int(e)) for f, s, e in matches]


def validate_scenario(
    skill_path: Path,
    data_dir: Path,
    api_key: str,
    *,
    judge_model: str = "openai/gpt-4o-mini",
) -> dict[str, Any]:
    """Audit an authored SKILL.md against its verified source evidence."""
    content = skill_path.read_text(encoding="utf-8")
    citations = parse_citations(content)

    citation_audit = []
    valid_citations = 0
    collected_evidence = []

    for fpath, s, e in citations:
        full_path = data_dir / fpath
        if not full_path.is_file():
            candidates = list(data_dir.rglob(Path(fpath).name))
            if candidates:
                full_path = candidates[0]

        if not full_path.is_file():
            citation_audit.append({"file": fpath, "lines": f"{s}-{e}", "status": "FILE_NOT_FOUND"})
            continue

        raw_lines = full_path.read_text(encoding="utf-8").splitlines()
        if not (1 <= s <= e <= len(raw_lines)):
            citation_audit.append({"file": fpath, "lines": f"{s}-{e}", "status": "OUT_OF_BOUNDS"})
            continue

        valid_citations += 1
        verbatim_slice = " ".join(
            line.strip() for line in raw_lines[s - 1 : e]
            if line.strip() and not line.strip().startswith("###") and not line.strip().startswith("---")
        )
        citation_audit.append({"file": fpath, "lines": f"{s}-{e}", "status": "VALID"})
        collected_evidence.append(f"[{fpath} L{s}-{e}]: \"{verbatim_slice}\"")

    judge_client = OpenRouter(api_key, judge_model)
    user_prompt = (
        f"AUTHORED SKILL PROMPT TO AUDIT:\n\n{content}\n\n"
        f"VERIFIED EVIDENCE EXCERPTS FROM SOURCE TRANSCRIPTS:\n\n"
        + "\n\n".join(collected_evidence)
        + "\n\nPerform a strict adversarial audit."
    )

    try:
        judge_res = judge_client.complete("skill_audit", JUDGE_SCHEMA, JUDGE_SYSTEM_PROMPT, user_prompt)
    finally:
        judge_client.close()

    return {
        "file": skill_path.name,
        "citation_integrity": {
            "total_citations": len(citations),
            "valid_citations": valid_citations,
            "citations": citation_audit,
        },
        "judge_evaluation": judge_res,
    }
