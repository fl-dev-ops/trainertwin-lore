"""Audit the production session cmurpfxg6000pfjiawplkcone with Jev (typesafe/jev-1.13).

Evaluates:
1. Trainer Spoken Turns: Does each turn adhere to Vasanth's authentic behavioral stance & voice,
   or is it generic/synthetic AI drift?
2. Report & Assessment Claims: Are the trainer's evaluative claims (in T27, T33, and the report)
   grounded in Harini's actual transcript, or are they hallucinations?
"""

import json
import os
import time
from pathlib import Path
from dotenv import load_dotenv
from pipeline.normalize import JevClient

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY is required")

with open("/tmp/session_full_audit.json") as f:
    audit_data = json.load(f)

transcript = audit_data["session"]["transcript"]
report = audit_data["session"]["report"]

# Extract candidate utterances
candidate_answers = "\n\n".join(
    f"[Turn {i+1}]: {t['text']}" for i, t in enumerate(transcript) if t["role"] == "user"
)

# Extract trainer utterances
trainer_turns = [
    (i + 1, t["text"]) for i, t in enumerate(transcript) if t["role"] == "trainer"
]

jev = JevClient(api_key)

print("=" * 80)
print("PRODUCTION RUN AUDIT WITH TYPESAFE JEV (typesafe/jev-1.13)")
print(f"Session ID: {audit_data['session']['id']} | Candidate: Harini Shekar | Persona: Vasanth")
print("=" * 80)

# -----------------------------------------------------------------------------
# AUDIT 1: Assessment & Report Grounding (Did the agent hallucinate candidate competence?)
# -----------------------------------------------------------------------------
print("\n--- AUDIT 1: Evaluative Claims vs. Candidate's Actual Words ---")

eval_claims = [
    {
        "id": "claim_t27_tradeoffs",
        "turn": 27,
        "text": "Your technical reasoning around trade-offs was clear.",
        "description": "Trainer Turn 27: Praise for clear reasoning on trade-offs"
    },
    {
        "id": "claim_t27_ownership",
        "turn": 27,
        "text": "Overall, you demonstrated solid ownership and contribution across multiple projects.",
        "description": "Trainer Turn 27: Solid ownership across multiple projects"
    },
    {
        "id": "claim_t33_tradeoffs",
        "turn": 33,
        "text": "Based on your answers, you show strong ownership and clear reasoning on trade-offs.",
        "description": "Trainer Turn 33: Strong ownership and clear reasoning on trade-offs"
    },
    {
        "id": "claim_rep_crdts",
        "turn": "Report",
        "text": "Effectively explaining technical mechanisms like CRDTs and background queuing for unreliable network environments.",
        "description": "Report Summary: Effectively explaining CRDTs and background queuing"
    },
    {
        "id": "claim_rep_inconsistent_depth",
        "turn": "Report",
        "text": "Depth was inconsistent when probed on frontend architecture and specific project details, where she was unable to recall key design decisions for component libraries and SIM activation flows.",
        "description": "Report Summary: Inability to recall component library and SIM activation decisions"
    }
]

eval_questions = {}
for ec in eval_claims:
    eval_questions[ec["id"]] = {
        "type": "choice",
        "instructions": (
            f"Based strictly on what the candidate actually said in the transcript, evaluate this statement:\n"
            f"Statement: \"{ec['text']}\""
        ),
        "criteria": {
            "grounded": "The statement is factually supported by concrete details the candidate provided in the transcript.",
            "hallucinated": "The statement is unearned, unsupported, or contradicts the candidate's actual answers (e.g. candidate admitted they don't remember or gave surface summaries without mechanism)."
        }
    }

t0 = time.time()
eval_res = jev.decide(
    state=f"CANDIDATE ACTUAL TRANSCRIPT ANSWERS:\n\"\"\"\n{candidate_answers}\n\"\"\"",
    questions=eval_questions
)
t_eval = time.time() - t0

for ec in eval_claims:
    ans = eval_res.get(ec["id"], {})
    choice = ans.get("choice", "unknown")
    conf = ans.get("confidence", 0.0)
    icon = "✅ GROUNDED" if choice == "grounded" else "❌ HALLUCINATED / UNEARNED"
    print(f"\n{icon} [{ec['description']}]")
    print(f"  Statement: \"{ec['text']}\"")
    print(f"  → Jev Verdict: {choice.upper()} (confidence: {conf:.2f})")

# -----------------------------------------------------------------------------
# AUDIT 2: Voice & Pedagogical Stance (Did the trainer sound like Vasanth or a robotic AI?)
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("--- AUDIT 2: Trainer Utterance Voice & Behavioral Fidelity ---")
print("=" * 80)

vasanth_persona_reference = """
VASANTH'S AUTHENTIC BEHAVIORAL CORPUS:
- Approachable, practical, adult-to-adult technical mentor.
- Avoids mechanical, repetitive corporate acknowledgments like 'Right, <name>' or 'Okay, <name>'.
- When candidates give high-level buzzwords, he immediately challenges surface breadth and asks for concrete implementation details or underlying fundamentals.
- Uses signature verbal check-ins: 'okay?', 'correct?', 'Let's do one thing', 'Got it', 'extreme fundamentals', 'under the hood'.
- Never provides empty flattery or repetitive procedural loops.
"""

voice_questions = {}
for turn_num, text in trainer_turns[:12]:  # Evaluate the first 12 interview turns
    qid = f"turn_{turn_num:02d}"
    voice_questions[qid] = {
        "type": "choice",
        "instructions": (
            f"Evaluate this interviewer utterance against Vasanth's authentic voice and interviewing style:\n"
            f"Utterance: \"{text}\""
        ),
        "criteria": {
            "vasanth_authentic": "Reflects Vasanth's natural conversational cadence, authentic phrasing, or direct diagnostic probing.",
            "robotic_ai_drift": "Exhibits repetitive robotic formula (e.g. rigid '[Ack], Harini. Looking at your resume section...'), corporate AI tropes, or artificial framing."
        }
    }

t0 = time.time()
voice_res = jev.decide(
    state=vasanth_persona_reference,
    questions=voice_questions
)
t_voice = time.time() - t0

robotic_count = 0
for turn_num, text in trainer_turns[:12]:
    qid = f"turn_{turn_num:02d}"
    ans = voice_res.get(qid, {})
    choice = ans.get("choice", "unknown")
    conf = ans.get("confidence", 0.0)
    is_robotic = (choice == "robotic_ai_drift")
    if is_robotic:
        robotic_count += 1
    tag = "🤖 ROBOTIC DRIFT" if is_robotic else "🗣️ VASANTH VOICE"
    print(f"\n{tag} [Turn {turn_num:02d}]")
    print(f"  \"{text}\"")
    print(f"  → Jev Verdict: {choice} (confidence: {conf:.2f})")

print("\n" + "=" * 80)
print(f"SUMMARY STATS:")
print(f"- Evaluative Claims Checked: {len(eval_claims)} (latency: {t_eval:.2f}s)")
print(f"- Trainer Turns Checked: 12 (latency: {t_voice:.2f}s)")
print(f"- Robotic AI Drift Rate: {robotic_count}/12 ({robotic_count/12*100:.1f}%)")
print("=" * 80)

jev.close()
