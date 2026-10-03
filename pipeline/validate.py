"""Validate authored SKILL.md prompts against source evidence using an independent judge."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .client import OpenRouter
from .normalize import JevClient

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
3. Gemini Adherence Readiness (1-10): Does it have strict voice turn bounds (strictly under 50 words), single focal question rule, frequency calibration for verbal ticks, and explicit "Never" boundaries?
4. Hallucinations / Unsupported Claims: Identify ANY assertion or rule that cannot be verified in the provided evidence.

If there are fabricated core tactics or facts, verdict MUST be FAIL. Otherwise PASS."""


def parse_signature_phrases(content: str) -> list[str]:
    """Extract signature phrases listed under Section 2."""
    match = re.search(
        r"Signature Phrases[^\n]*:\s*\n((?:\s*-\s*[\"'].*?[\"'].*?\n)+)",
        content,
        re.IGNORECASE,
    )
    if not match:
        return []
    block = match.group(1)
    phrases = []
    for line in block.strip().splitlines():
        p_match = re.search(r"-\s*[\"']([^\"']+)[\"']", line)
        if p_match:
            phrases.append(p_match.group(1).strip())
    return phrases


def audit_signature_phrases(phrases: list[str], source_texts: list[str]) -> list[dict[str, Any]]:
    """Verify that every signature phrase is a literal verbatim substring in the source evidence."""
    combined_evidence = " ".join(source_texts).lower()
    norm_evidence = re.sub(r"\s+", " ", combined_evidence.replace("…", "..."))
    results = []
    for phrase in phrases:
        norm_phrase = re.sub(r"\s+", " ", phrase.lower().replace("…", "...").strip())
        found = norm_phrase in norm_evidence
        if not found and norm_phrase.endswith(("?", "!", ".", ":", ",")):
            found = norm_phrase[:-1].strip() in norm_evidence
        results.append({
            "phrase": phrase,
            "verified": found,
            "status": "VERIFIED" if found else "FABRICATED_OR_ABSENT",
        })
    return results


def check_cadence_bounds(content: str) -> dict[str, Any]:
    """Check whether SKILL.md specifies strict voice turn bounds and single focal questions."""
    has_brevity = bool(re.search(r"under 50 words|<= ?50 words|strictly under 50", content, re.IGNORECASE))
    has_single_q = bool(re.search(r"one focal|single focal|exactly one (?:diagnostic )?question", content, re.IGNORECASE))
    
    # Extract dialogue turns specifically from Section 4
    section_4 = re.search(r"## 4\. Exemplar Dialogue Turns(.*?)(?=## 5|\Z)", content, re.DOTALL)
    dialogue_text = section_4.group(1) if section_4 else ""
    exemplars = re.findall(r"\*\*(?!Trigger|Action|Avoid|Grounding Citation|Rule)[^*]+\*\*:\s*([^\n]+)", dialogue_text)
    long_exemplars = []
    for ex in exemplars:
        words = ex.split()
        if len(words) > 50:
            long_exemplars.append({"text": ex[:80] + "...", "word_count": len(words)})
    return {
        "has_brevity_bound": has_brevity,
        "has_single_focal_question": has_single_q,
        "long_exemplars_found": len(long_exemplars),
        "passed": has_brevity and has_single_q and len(long_exemplars) == 0,
    }


def find_preceding_speaker_heading(lines: list[str], start_idx: int) -> str | None:
    """Find the nearest preceding '### ... · Speaker X' line above start_idx."""
    for i in range(start_idx, -1, -1):
        line = lines[i].strip()
        if line.startswith("###") and ("Speaker" in line or "·" in line):
            return line
    return None


def parse_citations(content: str) -> list[tuple[str, int, int]]:
    """Extract `file.md` (lines X-Y) citations from content."""
    matches = re.findall(
        r'[`"]?([^`"\n\s]+\.(?:md|yaml))[`"]?\s*\(lines?\s*(\d+)\s*[-–]\s*(\d+)\)',
        content,
    )
    return [(f, int(s), int(e)) for f, s, e in matches]


def parse_rules_with_citations(content: str) -> list[dict[str, Any]]:
    """Extract each rule's name, action, and citation from SKILL.md."""
    rule_blocks = re.findall(
        r"###\s+Rule\s+(\d+):\s*([^\n]+)\n(.*?)(?=###\s+Rule|\n##\s+|\Z)",
        content,
        re.DOTALL,
    )
    rules = []
    for num, title, body in rule_blocks:
        action_m = re.search(r"-\s+(?:\*\*)?Action(?:\*\*)?:\s*([^\n]+)", body)
        cite_m = re.search(
            r"-\s+(?:\*\*)?Grounding Citation(?:\*\*)?:\s*[`\"]?([^`\"\n\s]+\.(?:md|yaml))[`\"]?\s*\(lines?\s*(\d+)\s*[-–]\s*(\d+)\)",
            body,
        )
        if cite_m:
            rules.append({
                "rule_num": int(num),
                "title": title.strip(),
                "action": action_m.group(1).strip() if action_m else "",
                "file": cite_m.group(1).strip(),
                "start": int(cite_m.group(2)),
                "end": int(cite_m.group(3)),
            })
    return rules


def validate_scenario(
    skill_path: Path,
    data_dir: Path,
    api_key: str,
    *,
    judge_model: str = "openai/gpt-4o-mini",
) -> dict[str, Any]:
    """Audit an authored SKILL.md against its verified source evidence."""
    import sys
    content = skill_path.read_text(encoding="utf-8")
    citations = parse_citations(content)

    citation_audit = []
    valid_citations = 0
    collected_evidence = []
    full_source_texts = []

    for fpath, s, e in citations:
        full_path = data_dir / fpath
        if not full_path.is_file():
            candidates = list(data_dir.rglob(Path(fpath).name))
            if candidates:
                full_path = candidates[0]

        if not full_path.is_file():
            citation_audit.append({"file": fpath, "lines": f"{s}-{e}", "status": "FILE_NOT_FOUND"})
            continue

        raw_text = full_path.read_text(encoding="utf-8")
        full_source_texts.append(raw_text)
        raw_lines = raw_text.splitlines()
        if not (1 <= s <= e <= len(raw_lines)):
            citation_audit.append({"file": fpath, "lines": f"{s}-{e}", "status": "OUT_OF_BOUNDS"})
            continue

        valid_citations += 1
        # Preserve speaker headings (### 00:01:23 · Speaker 1) for speaker attribution verification
        verbatim_slice = "\n".join(
            line.strip() for line in raw_lines[s - 1 : e]
            if line.strip() and not line.strip().startswith("---")
        )
        citation_audit.append({"file": fpath, "lines": f"{s}-{e}", "status": "VALID"})
        collected_evidence.append(f"[{fpath} L{s}-{e}]:\n\"{verbatim_slice}\"")

    # Verbatim signature phrase audit (deterministic, zero LLM cost)
    signature_phrases = parse_signature_phrases(content)
    phrase_audit = audit_signature_phrases(signature_phrases, full_source_texts)

    # Jev semantic entailment verification on cited rules
    jev_client = JevClient(api_key)
    jev_hallucinations = []
    jev_results = []
    jev_error = None
    try:
        rules = parse_rules_with_citations(content)
        for r in rules:
            full_path = data_dir / r["file"]
            if not full_path.is_file():
                candidates = list(data_dir.rglob(Path(r["file"]).name))
                if candidates:
                    full_path = candidates[0]
            if not full_path.is_file():
                continue
            raw_lines = full_path.read_text(encoding="utf-8").splitlines()
            if not (1 <= r["start"] <= r["end"] <= len(raw_lines)):
                continue
            # Preserve speaker lines in the excerpt so Jev verifies speaker attribution
            slice_lines = [
                line.strip() for line in raw_lines[r["start"] - 1 : r["end"]]
                if line.strip() and not line.strip().startswith("---")
            ]
            if slice_lines and not slice_lines[0].startswith("###"):
                heading = find_preceding_speaker_heading(raw_lines, r["start"] - 2)
                if heading:
                    slice_lines.insert(0, heading)
            excerpt = "\n".join(slice_lines)

            jev_ans = jev_client.decide(
                state=f"TRANSCRIPT / EVIDENCE EXCERPT (WITH SPEAKERS):\n\"\"\"\n{excerpt}\n\"\"\"",
                questions={
                    "entailment": {
                        "type": "choice",
                        "instructions": (
                            f"Evaluate whether the following rule is factually supported by the excerpt without misattributing speakers:\n"
                            f"Rule: \"{r['title']}. Action: {r['action']}\""
                        ),
                        "criteria": {
                            "grounded": "The advice and core action are directly asserted or logically entailed by the excerpt.",
                            "hallucinated": "The claim invents concepts absent from the text, contradicts the excerpt, or misattributes statements to another speaker."
                        }
                    }
                }
            )
            ans = jev_ans.get("entailment")
            choice = ans.get("choice") if isinstance(ans, dict) else None
            conf = float(ans.get("confidence", 0.0)) if isinstance(ans, dict) else 0.0

            # FAIL CLOSED: Missing, null, or unexpected choice values cannot pass as grounded
            if not isinstance(ans, dict) or choice not in ("grounded", "hallucinated"):
                item_res = {
                    "rule": r["title"],
                    "citation": f"{r['file']} L{r['start']}-{r['end']}",
                    "choice": "unverified_error",
                    "confidence": 0.0,
                    "error": f"Jev returned invalid choice: {choice!r}"
                }
                jev_results.append(item_res)
                jev_hallucinations.append(item_res)
                continue

            item_res = {
                "rule": r["title"],
                "citation": f"{r['file']} L{r['start']}-{r['end']}",
                "choice": choice,
                "confidence": conf,
            }
            jev_results.append(item_res)
            # High-confidence hallucination fails the validation
            if choice == "hallucinated" and conf >= 0.60:
                jev_hallucinations.append(item_res)
    except Exception as exc:
        jev_error = str(exc)
        print(f"Error: Jev entailment verification failed ({exc})", file=sys.stderr)
        jev_hallucinations.append({
            "rule": "Jev Evaluator",
            "citation": "N/A",
            "choice": "evaluator_error",
            "confidence": 1.0,
            "error": str(exc),
        })
    finally:
        jev_client.close()

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

    # Fail closed on citation integrity issues
    invalid_cites = [c for c in citation_audit if c["status"] != "VALID"]
    if invalid_cites:
        judge_res["verdict"] = "FAIL"
        for ic in invalid_cites:
            judge_res["unsupported_claims"].append(
                f"[Citation Failure]: {ic['file']} ({ic['lines']}) -> {ic['status']}"
            )

    if jev_hallucinations:
        judge_res["verdict"] = "FAIL"
        for h in jev_hallucinations:
            err_msg = f"[Jev Entailment Failure]: Rule '{h['rule']}' is ungrounded/hallucinated against {h['citation']} (confidence: {h.get('confidence', 0.0):.2f})"
            if err_msg not in judge_res["hallucinations_found"]:
                judge_res["hallucinations_found"].append(err_msg)

    grounded_count = sum(1 for r in jev_results if r["choice"] == "grounded" and r not in jev_hallucinations)
    cadence_res = check_cadence_bounds(content)

    # Fail closed on cadence violations
    if not cadence_res["passed"]:
        judge_res["verdict"] = "FAIL"
        if not cadence_res["has_brevity_bound"]:
            judge_res["unsupported_claims"].append("[Cadence Failure]: Section 2 missing strict voice brevity bound (< 50 words).")
        if not cadence_res["has_single_focal_question"]:
            judge_res["unsupported_claims"].append("[Cadence Failure]: Section 2 missing single focal question protocol.")
        if cadence_res["long_exemplars_found"] > 0:
            judge_res["unsupported_claims"].append(f"[Cadence Failure]: Found {cadence_res['long_exemplars_found']} exemplar turn(s) exceeding length bounds.")

    # Fail closed on unverified/fabricated signature phrases
    unverified_phrases = [p for p in phrase_audit if not p["verified"]]
    if unverified_phrases:
        judge_res["verdict"] = "FAIL"
        for up in unverified_phrases:
            judge_res["hallucinations_found"].append(
                f"[Fabricated Signature Phrase]: '{up['phrase']}' was not found word-for-word in the evidence sources."
            )

    return {
        "file": skill_path.name,
        "citation_integrity": {
            "total_citations": len(citations),
            "valid_citations": valid_citations,
            "citations": citation_audit,
        },
        "signature_phrase_audit": {
            "total_phrases": len(signature_phrases),
            "verified_phrases": sum(1 for p in phrase_audit if p["verified"]),
            "phrases": phrase_audit,
        },
        "jev_entailment_audit": {
            "total_rules_checked": len(jev_results),
            "grounded_rules": grounded_count,
            "hallucinations": jev_hallucinations,
            "rules": jev_results,
        },
        "cadence_audit": cadence_res,
        "judge_evaluation": judge_res,
    }
