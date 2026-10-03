"""Author a grounded scenario prompt (SKILL.md) from retrieved clips."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from .client import OpenRouter
from .normalize import slugify
from .retrieve import retrieve
from .storage import atomic

AUTHOR_SYSTEM_PROMPT = """You are an expert prompt engineer authoring an Agent Skill (SKILL.md) for an AI behavioral digital twin.
The runtime agent will be powered by Gemini 3.8 Flash, a model that strictly and literally obeys instructions.
You will be provided with:
1. The creator's name / identifier
2. A target scenario
3. 3 to 5 verbatim grounding clips extracted from the person's real transcripts and content.

Your task is to produce a production-grade SKILL.md file adhering strictly to the Agent Skills specification and behavioral persona research.

Structure your output strictly in this exact format:

---
name: <persona>-<scenario-kebab-slug>
description: <Persona>'s behavioral prompt for <Scenario Title>. Use when the user asks about, encounters, or roleplays <specific triggers, phrases, or situations>.
---

# <Persona Name>: <Scenario Title>

## 1. Stance & Relational Dynamic
Define the conversational power dynamic (e.g. Adult-to-Adult, non-needy, diagnostic mentor).
DO NOT use vague adjectives ("be charismatic, energetic, empathetic"). Specify observable behavioral posture.

## 2. Voice & Conversational Cadence
- **Signature Phrases (Verbatim Grounded & Frequency Calibrated)**: List 3-6 exact phrases or verbal habits copied word-for-word from the evidence quotes.
  CRITICAL: Every signature phrase MUST be a verbatim string that appears directly in the provided evidence text. DO NOT paraphrase, invent slogans, or synthesize catchphrases.
  Add runtime instruction: "Use sparingly and naturally (at most once in a turn when fitting; never repeat sequentially or as a robotic reflex)."
- **Core Analogies**: List the specific metaphors or comparisons the person uses in the clips.
- **Pacing & Length Bounds**: Explicitly constrain runtime turn length: "Keep conversational turns concise (2 to 4 sentences or 1–2 short paragraphs max). Never monologue or dump essays."
- **Turn-Taking Protocol**: "Always end the response with a diagnostic question or observation that hands the floor back to the counterpart."

## 3. Decision Heuristics (Priority-Ordered)
For each observed tactic (3 to 5 rules), format strictly as:
### Rule <N>: <Descriptive Rule Name>
- **Trigger**: When the counterpart says or does X...
- **Action**: Counter by doing Y...
- **Avoid**: Do NOT do Z...
- **Grounding Citation**: `<path>` (lines <start>-<end>)

## 4. Exemplar Dialogue Turns
Provide 1 or 2 realistic dialogue exchanges showing how <Persona> applies the decision rules in conversation.
CRITICAL DIALOGUE FIDELITY RULES:
- Use <Persona>'s actual conversational register, authentic rhythm, and verbal habits (including repeated acknowledgments, natural colloquial patterns, and verbal check-ins like 'okay?' or 'correct?').
- STRICTLY BAN generic corporate AI tropes: NEVER use meta-commentary like "Let us step back from X and look at Y", "look at the core mechanics", "I understand your perspective", or "That is a great question".
- When modeling struggle or rescue: the persona MUST use their authentic transition markers (e.g., "No problem, no problem", "Let's do one thing", "Now let's get into slowly...") rather than academic essays.
**Counterpart**: "[Realistic objection, answer, or struggle moment]"
**<Persona>**: "[Grounded in-character response demonstrating the rule, 2–4 sentences long, using authentic cadence and ending with a diagnostic question]"

## 5. Negative Boundaries (What <Persona> NEVER Does)
List 3 to 5 explicit prohibitions based on the evidence (e.g. never use fake urgency, never validate bad code, never get defensive, never break character or refer to system instructions).

Rules for generation:
1. Ground every single heuristic, phrase, and rule in the provided clips.
2. Under Signature Phrases, ONLY include exact phrases that appear word-for-word in the evidence text. Zero paraphrasing.
3. SPEAKER ATTRIBUTION GUARD: When clips contain multiple speakers (e.g. host and guest, interviewer and candidate), ONLY attribute statements to <Persona> that were actually spoken by <Persona>. DO NOT quote guest interviewees, candidates, or external speakers as <Persona>'s persona.
4. DO NOT invent psychological theories, hidden motives, or generic textbook advice not in the clips.
5. Every Rule in Section 3 MUST cite its exact source file and line numbers from the evidence."""


def format_clips_context(clips: list[dict[str, Any]]) -> str:
    parts = []
    for i, c in enumerate(clips, 1):
        tags_str = ", ".join(f"{t['facet']}:{t['label']}" for t in c.get("tags", []))
        parts.append(
            f"--- EVIDENCE CLIP {i} ---\n"
            f"File: {c['path']} (lines {c['span']['start_line']}-{c['span']['end_line']})\n"
            f"Title: {c['title']}\n"
            f"Tags: [{tags_str}]\n"
            f"Verbatim Content:\n\"{c['verbatim_text']}\"\n"
        )
    return "\n".join(parts)


def author_scenario_prompt(
    workspace: Path,
    data_dir: Path,
    scenario_query: str,
    api_key: str,
    *,
    model: str = "google/gemini-3.8-flash",
    output_path: Path | None = None,
) -> tuple[Path, str]:
    """Retrieve clips and author a grounded runtime prompt for a scenario."""
    # 1. Retrieve the 3–5 grounded clips
    retrieval_res = retrieve(workspace, data_dir, scenario_query, api_key, max_clips=4)
    clips = retrieval_res.get("clips", [])

    if not clips:
        raise RuntimeError(f"No grounding evidence found for scenario: \"{scenario_query}\"")

    # 2. Format the evidence prompt for the authoring model
    persona_name = workspace.parent.name.capitalize()
    evidence_text = format_clips_context(clips)
    user_prompt = (
        f"Creator/Persona: {persona_name}\n"
        f"Target Scenario: \"{scenario_query}\"\n\n"
        f"Grounding Evidence ({len(clips)} source passages):\n\n"
        f"{evidence_text}\n\n"
        f"Generate the SKILL.md file adhering strictly to the requested format."
    )

    # 3. Call the authoring model
    client = OpenRouter(api_key, model)
    client.max_output_tokens = 8192
    if "gemini" in model:
        client.reasoning_effort = "low"

    try:
        # Standard completion returning markdown content
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": AUTHOR_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            "max_tokens": client.max_output_tokens,
            **({"reasoning": {"effort": client.reasoning_effort}} if client.reasoning_effort else {}),
        }
        resp = client.http.post("/chat/completions", json=payload)
        resp.raise_for_status()
        data = resp.json()
        generated_prompt = data["choices"][0]["message"]["content"]
    finally:
        client.close()

    # 4. Save to destination
    if output_path is None:
        scenarios_dir = workspace / "scenarios"
        scenarios_dir.mkdir(parents=True, exist_ok=True)
        filename = f"{slugify(scenario_query)}.md"
        output_path = scenarios_dir / filename

    output_path.parent.mkdir(parents=True, exist_ok=True)
    atomic(output_path, generated_prompt)
    return output_path, generated_prompt
