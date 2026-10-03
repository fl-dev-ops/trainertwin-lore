"""Opt-in continuous text probes with multi-dimensional evaluation.

Dimensions evaluated per turn:
  (a) user-fact grounding (via Jev entailment over accumulated user disclosures)
  (b) persona fidelity against held-out transcripts (via Jev over creator evidence)
  (c) conversational cadence & turn discipline (deterministic length, focal questions, repetition)

uv run python scripts/run_persona_conversations.py --output .pi/experiments/persona-conversations-multi
uv run python scripts/run_persona_conversations.py --self-check
"""

import argparse
import hashlib
import json
import math
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

from pipeline.client import OpenRouter
from pipeline.normalize import JevClient
from pipeline.validate import parse_citations, validate_scenario

ROOT = Path(__file__).resolve().parents[1]
INSTRUCTIONS_PATH = ROOT.parent / "trainertwin/application/chat/agent/instructions.md"

COMMON = """This is a text-only coaching conversation with the persona in the attached skill.
Follow that persona's evidenced behavior, not a generic technical-interviewer role.
Treat the user's claims as unverified claims; do not invent facts, numbers, or personal history.
Use the skill's conversational style without mechanically repeating signature phrases.
Keep turns short and use one focal ask at a time. Do not guarantee financial outcomes or
fabricate interview accomplishments. If the user ends the conversation, acknowledge briefly
without another question. There are no tools or screen controls in this experiment.
Safety, factual accuracy, and the current user's intent take precedence over style instructions.
"""

CASES = {
    "olga": {
        "skill": "cold-calling-openings-and-first-call.md",
        "held_out_sources": [
            "linkedin/posts/2026-09-27-why-do-buyers-disappear-after.md",
            "linkedin/posts/2026-09-29-your-client-is-not-interested.md",
        ],
        "inputs": [
            "I'm a new real estate agent in Dubai, with no referrals. Owners hang up when I ask if they want to sell. Can you help me practise?",
            "I say: Hi, I'm Alex from a brokerage, how are you today? Are you selling or renting your property?",
            "I thought sounding really enthusiastic would make them trust me. Should I sound even happier?",
            "I don't actually have a reason for calling beyond trying to get a listing. I guess I need a better conversation first.",
            "Could I say there is a buyer ready with a cheque even though I haven't found one yet?",
            "Okay, no made-up buyer. I spend most of my day preparing brochures and sending WhatsApps. I only speak to owners for about forty minutes.",
            "What should I practise first tomorrow? I want something concrete, not a magic script or guaranteed deal.",
            "Thanks, that's enough for today. Let's stop here.",
        ],
    },
    "jameel": {
        "skill": "answering-star-method-behavioral-interviews.md",
        "held_out_sources": [
            "youtube/video/2023-11-06-how-to-ace-the-how-do-you-solve-problems-at-work-interview-q-cOwAgReljkA.md",
            "youtube/video/2021-03-26-3-things-you-should-do-after-an-unsuccessful-job-interview-WOv19znuBOg.md",
        ],
        "inputs": [
            "I'm preparing for a supply planner interview. When they ask about disruptions I say I'm adaptable and work hard. Can you coach me?",
            "One time a supplier missed a shipment. I spent the afternoon calling freight brokers until I found another truck.",
            "It risked an order for our largest retail customer. I had to find transport before the warehouse cutoff that afternoon.",
            "Our team solved it. I don't know how to explain what I did personally without taking everyone else's credit.",
            "I personally called three carriers, checked which could meet cutoff, and chose the only confirmed truck. I didn't do a days-of-supply analysis.",
            "Can we say I saved a hundred thousand dollars? I don't know the actual number. It sounds more impressive.",
            "I won't invent it. The truck arrived late and part of the order missed cutoff. I learned to confirm availability earlier and record a backup contact.",
            "Thanks, I have enough to practise now. Let's end here.",
        ],
    },
}

SIGNATURE_PHRASES = [
    "equal adult",
    "tried and tested star model",
    "star model",
    "loosey goosey",
    "passive whatsapp",
    "real cost is your time",
    "cold calling is your",
    "safe place to hide",
    "fairytale ending",
    "tidy ending",
]


def load_user_fact_policy() -> str:
    """Load the verified User-Fact Preservation section from the application instructions if available."""
    if INSTRUCTIONS_PATH.exists():
        text = INSTRUCTIONS_PATH.read_text(encoding="utf-8")
        if "### User-Fact Preservation\n" in text:
            start = text.index("### User-Fact Preservation\n")
            end = text.index("\n---", start)
            return text[start:end].strip()
    return ""


def analyze_cadence(record: dict, prior_records: list[dict]) -> dict:
    """Deterministically analyze conversational cadence, word count, questions, and phrase repetitions."""
    text = record.get("assistant", "")
    words = text.split()
    word_count = len(words)
    q_count = text.count("?")
    has_markdown = bool(re.search(r"(\*\*|`|#|\b_\b|\[.*?\]\(.*?\))", text))

    text_lower = text.lower()
    repeated_phrases = []
    if prior_records:
        last_turn = prior_records[-1].get("assistant", "").lower()
        for phrase in SIGNATURE_PHRASES:
            if phrase in text_lower and phrase in last_turn:
                repeated_phrases.append(phrase)

    user_ended = any(term in record.get("user", "").lower() for term in ("stop here", "end here", "that's enough"))

    passed_length = word_count <= 75
    passed_questions = (q_count == 0 if user_ended else q_count == 1)
    passed_formatting = not has_markdown
    passed_repetition = len(repeated_phrases) == 0

    overall_pass = passed_length and passed_questions and passed_formatting and passed_repetition

    return {
        "word_count": word_count,
        "question_count": q_count,
        "has_markdown": has_markdown,
        "repeated_phrases": repeated_phrases,
        "user_ended": user_ended,
        "checks": {
            "brevity": passed_length,
            "focal_question": passed_questions,
            "formatting": passed_formatting,
            "no_consecutive_repetition": passed_repetition,
        },
        "verdict": "PASS" if overall_pass else "FAIL",
    }


def dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def spoken_message(response):
    choice = response["choices"][0]
    msg = choice["message"]
    if msg.get("tool_calls"):
        raise ValueError("Unexpected tool call in a no-tools text experiment")
    if choice.get("finish_reason") != "stop" or not isinstance(msg.get("content"), str) or not msg["content"].strip():
        raise ValueError("Missing or incomplete spoken content; reasoning is not a reply")
    return {"role": "assistant", "content": msg["content"].strip()}


def self_check():
    assert spoken_message({"choices": [{"finish_reason": "stop", "message": {"content": "Hi"}}]})["content"] == "Hi"
    for msg in ({"content": None, "reasoning": "Not speech"}, {"content": "", "tool_calls": [{}]}):
        try:
            spoken_message({"choices": [{"finish_reason": "stop", "message": msg}]})
        except ValueError:
            continue
        raise AssertionError("Invalid response was accepted as speech")

    # Cadence analysis unit check
    r1 = {"user": "Hi", "assistant": "Hello there as an equal adult. How are you?"}
    r2 = {"user": "Fine", "assistant": "Great to speak as an equal adult. What is your goal?"}
    c2 = analyze_cadence(r2, [r1])
    assert c2["checks"]["no_consecutive_repetition"] is False
    assert "equal adult" in c2["repeated_phrases"]

    r3 = {"user": "Thanks, let's stop here.", "assistant": "You bet."}
    c3 = analyze_cadence(r3, [r1, r2])
    assert c3["checks"]["focal_question"] is True
    assert c3["verdict"] == "PASS"

    policy = load_user_fact_policy()
    assert "User-Fact Preservation" in policy

    print("Multi-dimensional evaluation self-check passed")


def run(output: Path, api_key: str, model: str):
    output.mkdir(parents=True, exist_ok=False)
    policy = load_user_fact_policy()
    manifest = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "model": model,
        "scope": "Multi-dimensional continuous text coaching probes: (a) user-fact grounding, (b) persona fidelity on held-out transcripts, (c) cadence discipline.",
        "inputs": "Scripted user turns testing cold-calling and STAR interview scenarios.",
        "user_fact_policy_sha256": sha(policy) if policy else None,
        "personas": {},
    }
    client, jev = OpenRouter(api_key, model), JevClient(api_key)
    try:
        for persona, case in CASES.items():
            folder = output / persona
            folder.mkdir()
            skill_path = ROOT / "users" / persona / "workspace/scenarios" / case["skill"]
            skill = skill_path.read_text(encoding="utf-8")
            (folder / "skill.md").write_text(skill, encoding="utf-8")

            # Load cited sources
            citations = parse_citations(skill)
            references = []
            cited_paths = set()
            for path, start, end in dict.fromkeys(citations):
                source_path = ROOT / "users" / persona / "data" / path
                raw = source_path.read_text(encoding="utf-8")
                if not 1 <= start <= end <= len(raw.splitlines()):
                    raise ValueError(f"Invalid citation: {path} {start}-{end}")
                references.append({
                    "path": path, "sha256": sha(raw), "citation": [start, end],
                    "full_source_text": raw, "type": "cited",
                })
                cited_paths.add(path)

            # Load held-out sources (not cited in the skill prompt)
            held_out_references = []
            for path in case.get("held_out_sources", []):
                source_path = ROOT / "users" / persona / "data" / path
                raw = source_path.read_text(encoding="utf-8")
                held_out_references.append({
                    "path": path, "sha256": sha(raw), "full_source_text": raw, "type": "held_out",
                })

            dump(folder / "sources.json", references + held_out_references)

            try:
                validation = validate_scenario(skill_path, ROOT / "users" / persona / "data", api_key)
            except Exception as exc:
                validation = {"error_type": type(exc).__name__, "verdict": "INCOMPLETE"}
            dump(folder / "skill_validation.json", validation)

            policy_block = f"\n\nSHARED EVIDENCE POLICY (takes precedence over conflicting skill advice):\n{policy}\n" if policy else ""
            system = COMMON + policy_block + "\nACTIVE PERSONA SKILL:\n" + skill
            (folder / "system.md").write_text(system, encoding="utf-8")
            history = [{"role": "system", "content": system}]
            records = []

            for index, user in enumerate(case["inputs"], 1):
                history.append({"role": "user", "content": user})
                payload = {
                    "model": model, "messages": list(history), "temperature": 0.2,
                    "max_tokens": 4096, "reasoning": {"effort": "low"},
                }
                dump(folder / f"turn-{index:02d}-request.json", payload)
                started = time.monotonic()
                response = client.http.post("/chat/completions", json=payload)
                response.raise_for_status()
                raw_response = response.json()
                dump(folder / f"turn-{index:02d}-response.json", raw_response)
                try:
                    reply = spoken_message(raw_response)
                except (ValueError, KeyError, IndexError, TypeError) as exc:
                    records.append({"turn": index, "user": user, "status": "INCOMPLETE", "error": str(exc)})
                    dump(folder / "conversation.json", records)
                    break
                history.append(reply)
                text = reply["content"]
                records.append({
                    "turn": index, "user": user, "assistant": text, "status": "COMPLETE",
                    "latency_seconds": time.monotonic() - started, "usage": raw_response.get("usage"),
                    "word_count": len(text.split()), "question_marks": text.count("?"),
                    "opening": text.split(".")[0],
                })
                dump(folder / "conversation.json", records)
                print(f"{persona} T{index}: {text}", flush=True)

            # Build creator evidence for persona fidelity: cited excerpts + held-out excerpts
            cited_evidence = "\n\n".join(
                f"CITED SOURCE {r['path']} L{r['citation'][0]}-{r['citation'][1]}:\n" +
                "\n".join(f"{i}|{line}" for i, line in enumerate(r["full_source_text"].splitlines(), 1)
                          if r["citation"][0] <= i <= r["citation"][1])
                for r in references
            )
            held_out_evidence = "\n\n".join(
                f"HELD-OUT SOURCE {r['path']}:\n" +
                "\n".join(r["full_source_text"].splitlines()[:60])  # Bounded sample of held-out
                for r in held_out_references
            )
            creator_evidence = cited_evidence + "\n\n" + held_out_evidence

            evaluations = []
            for record in records:
                if record["status"] != "COMPLETE":
                    continue

                prior_records = [r for r in records if r["turn"] < record["turn"]]
                # 1. Deterministic Cadence Evaluation
                cadence = analyze_cadence(record, prior_records)

                # 2. User-Fact Grounding Jev Evaluation
                user_disclosures = "\n".join(
                    f"Turn {r['turn']} User Statement: {r['user']}"
                    for r in records if r["turn"] <= record["turn"]
                )
                user_state = f"ACCUMULATED USER STATEMENTS THROUGH TURN {record['turn']}:\n{user_disclosures}"
                user_question = {
                    "type": "choice",
                    "instructions": (
                        f"Evaluate whether the assistant faithfully preserves the user's stated facts, timing, and constraints.\n"
                        f"Assistant reply under evaluation:\n\"{record['assistant']}\"\n\n"
                        "Criteria:\n"
                        "- grounded: Accurately reflects user statements/constraints without inventing unstated actions, completed implementations, unprompted motives, or fabricated metrics. Neutral clarifying questions and general coaching suggestions are grounded.\n"
                        "- ungrounded_addition: Invents unstated actions, upgrades lessons/plans into completed implementations, asserts unprompted motives, or attributes unstated metrics/outcomes.\n"
                        "- unsupported_refusal: Refuses to accept facts explicitly reported by the user."
                    ),
                    "criteria": {
                        "grounded": "Accurately reflects user statements and constraints without inventing unstated actions, completed implementations, unprompted motives, or fabricated metrics.",
                        "ungrounded_addition": "Invents unstated actions, upgrades lessons/plans into completed implementations, asserts unprompted motives, or attributes unstated metrics/outcomes.",
                        "unsupported_refusal": "Refuses to accept facts explicitly reported by the user.",
                    },
                }

                # 3. Persona Fidelity Jev Evaluation (against creator sources + held-out)
                persona_question = {
                    "type": "choice",
                    "instructions": (
                        f"Compare only the latest assistant turn to the persona source excerpts:\n"
                        f"Assistant reply under evaluation:\n\"{record['assistant']}\"\n\n"
                        "Evaluate whether the assistant demonstrates the authentic coaching register, directness, and strategy of the persona "
                        "rather than generic synthetic AI tropes ('Let us step back', 'I understand your perspective', corporate disclaimers). "
                        "If references do not cover this conversational situation, select insufficient_evidence."
                    ),
                    "criteria": {
                        "authentic": "Evidences comparable coaching strategy, direct register, and authentic tone without synthetic AI tropes.",
                        "synthetic_drift": "Exhibits generic AI tropes, hollow corporate meta-commentary, or mechanical repetitive patterns.",
                        "different": "Concretely conflicts with the evidenced coaching strategy or register.",
                        "insufficient_evidence": "The excerpts cannot establish a persona-specific judgment for this situation.",
                    },
                }

                # Run Jev queries
                grounding_res = {}
                fidelity_res = {}
                try:
                    ans_g = jev.decide(user_state, {"user_grounding": user_question})
                    grounding_res = ans_g.get("user_grounding", {})
                except Exception as exc:
                    grounding_res = {"error": type(exc).__name__}

                try:
                    ans_f = jev.decide(creator_evidence, {"persona_fidelity": persona_question})
                    fidelity_res = ans_f.get("persona_fidelity", {})
                except Exception as exc:
                    fidelity_res = {"error": type(exc).__name__}

                eval_record = {
                    "turn": record["turn"],
                    "cadence": cadence,
                    "user_grounding": grounding_res,
                    "persona_fidelity": fidelity_res,
                }
                evaluations.append(eval_record)
                dump(folder / "evaluations.json", evaluations)

            # Summarize multi-dimensional results
            cadence_passes = sum(1 for e in evaluations if e["cadence"]["verdict"] == "PASS")
            grounding_passes = sum(1 for e in evaluations if e["user_grounding"].get("choice") == "grounded")
            fidelity_passes = sum(1 for e in evaluations if e["persona_fidelity"].get("choice") == "authentic")

            summary = {
                "skill_path": str(skill_path),
                "skill_sha256": sha(skill),
                "system_sha256": sha(system),
                "requested_turns": len(case["inputs"]),
                "completed_turns": sum(r["status"] == "COMPLETE" for r in records),
                "evaluated_turns": len(evaluations),
                "dimensions": {
                    "cadence_discipline": {"passed": cadence_passes, "total": len(evaluations)},
                    "user_grounding": {"grounded": grounding_passes, "total": len(evaluations)},
                    "persona_fidelity": {"authentic": fidelity_passes, "total": len(evaluations)},
                },
                "pipeline_judge_verdict": validation.get("judge_evaluation", {}).get("verdict", "INCOMPLETE"),
            }
            manifest["personas"][persona] = summary
            dump(output / "manifest.json", manifest)
    finally:
        client.close()
        jev.close()
    print(f"Artifacts: {output.resolve()}", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--model", default="google/gemini-3.8-flash")
    args = parser.parse_args()
    if args.self_check:
        self_check()
    else:
        if not args.output:
            parser.error("--output is required unless --self-check is passed")
        load_dotenv(ROOT / ".env")
        run(args.output, os.environ["OPENROUTER_API_KEY"], args.model)
