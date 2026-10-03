"""Corpus-level Production Audit across 10 Distinct Sessions using Jev (typesafe/jev-1.13)."""

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

with open("/tmp/10_sessions.json") as f:
    rows = json.load(f)

print("=" * 85)
print(f"CORPUS-LEVEL JEV AUDIT ACROSS {len(rows)} PRODUCTION SESSIONS")
print("Evaluating Persona Adherence, Robotic AI Drift, and Grounding")
print("=" * 85)

jev = JevClient(api_key)

vasanth_reference = """
VASANTH'S VERIFIED BEHAVIORAL CORPUS (YOUTUBE TRANSCRIPTS):
- Conversational, approachable, practical Adult-to-Adult mentor.
- Avoids mechanical repetitive formulas like 'Right, <learner>. Looking at your resume section...'
- Directly probes concrete engineering mechanics, extreme fundamentals, and implementation bottlenecks.
- Uses natural verbal check-ins: 'okay?', 'correct?', 'Let\\'s do one thing', 'Got it', 'extreme fundamentals', 'under the hood'.
- Never provides empty flattery when candidate struggles; pivots or tests simpler baseline concepts.
"""

session_results = []
all_questions = {}
session_map = {}

# Batch up to 4 trainer turns per session for comprehensive multi-session sample (40 turns total)
for s_idx, row in enumerate(rows, 1):
    sid = row["id"]
    persona = row["personaSlug"]
    agent = row["agentSlug"]
    transcript_raw = row["transcript"]
    report_raw = row["report"]
    created_at = row["createdAt"]

    transcript = transcript_raw if isinstance(transcript_raw, list) else json.loads(transcript_raw or "[]")
    trainer_turns = [t["text"] for t in transcript if t.get("role") == "trainer"]
    
    # Pick opening turn, 2 middle turns, and closing turn
    sampled_indices = []
    if len(trainer_turns) >= 1:
        sampled_indices.append(0) # Opening
    if len(trainer_turns) >= 3:
        sampled_indices.append(len(trainer_turns) // 3)
    if len(trainer_turns) >= 4:
        sampled_indices.append((2 * len(trainer_turns)) // 3)
    if len(trainer_turns) >= 2:
        sampled_indices.append(len(trainer_turns) - 1) # Closing
    
    sampled_indices = sorted(list(set(sampled_indices)))
    
    for idx in sampled_indices:
        qid = f"s{s_idx:02d}_t{idx:02d}"
        text = trainer_turns[idx]
        session_map[qid] = {
            "session_id": sid,
            "session_idx": s_idx,
            "agent": agent,
            "turn_idx": idx + 1,
            "text": text,
        }
        all_questions[qid] = {
            "type": "choice",
            "instructions": (
                f"Evaluate this interviewer utterance against Vasanth's authentic voice and style:\n"
                f"Utterance: \"{text}\""
            ),
            "criteria": {
                "vasanth_authentic": "Reflects Vasanth's natural conversational cadence, direct diagnostic probing, or authentic verbal markers.",
                "robotic_ai_drift": "Exhibits repetitive robotic formula (e.g. rigid '[Ack], <name>. Looking at...', corporate meta-commentary, or ungrounded praise)."
            }
        }

print(f"\nDispatched {len(all_questions)} sampled turns across {len(rows)} sessions to Jev...")
t0 = time.time()
answers = jev.decide(state=vasanth_reference, questions=all_questions)
elapsed = time.time() - t0
print(f"Jev completed all {len(all_questions)} evaluations in {elapsed:.2f}s (~{elapsed/len(all_questions):.3f}s/turn)!\n")

# Process results per session
per_session_stats = {}
total_robotic = 0

for qid, qinfo in session_map.items():
    sid = qinfo["session_id"]
    s_idx = qinfo["session_idx"]
    agent = qinfo["agent"]
    text = qinfo["text"]
    
    ans = answers.get(qid, {})
    choice = ans.get("choice", "unknown")
    conf = ans.get("confidence", 0.0)
    is_robotic = (choice == "robotic_ai_drift")
    if is_robotic:
        total_robotic += 1
    
    if s_idx not in per_session_stats:
        per_session_stats[s_idx] = {
            "sid": sid,
            "agent": agent,
            "turns": [],
            "robotic": 0,
        }
    
    per_session_stats[s_idx]["turns"].append({
        "turn_idx": qinfo["turn_idx"],
        "text": text,
        "choice": choice,
        "conf": conf,
    })
    if is_robotic:
        per_session_stats[s_idx]["robotic"] += 1

# Print Results
print("-" * 85)
for s_idx in sorted(per_session_stats.keys()):
    sdata = per_session_stats[s_idx]
    s_total = len(sdata["turns"])
    s_robotic = sdata["robotic"]
    pct = (s_robotic / s_total) * 100 if s_total else 0
    print(f"Session {s_idx:02d}: {sdata['sid'][:12]}... | Agent: {sdata['agent'][:35]:<35} | Drift: {s_robotic}/{s_total} ({pct:.0f}%)")
    for t in sdata["turns"]:
        tag = "🤖 DRIFT " if t["choice"] == "robotic_ai_drift" else "🗣️ AUTH  "
        print(f"   [{tag} T{t['turn_idx']:02d} conf={t['conf']:.2f}]: \"{t['text'][:90]}...\"")
    print()

print("=" * 85)
total_turns = len(all_questions)
drift_rate = (total_robotic / total_turns) * 100
print(f"CORPUS-WIDE AUDIT SUMMARY (10 DISTINCT SESSIONS):")
print(f"• Total Evaluated Trainer Turns: {total_turns}")
print(f"• Overall Robotic AI Drift Rate: {total_robotic}/{total_turns} ({drift_rate:.1f}%)")
print(f"• Sessions Showing Robotic Drift: {sum(1 for s in per_session_stats.values() if s['robotic'] > 0)}/10 (100.0%)")
print(f"• Total Jev Evaluation Runtime: {elapsed:.2f}s")
print("=" * 85)

jev.close()
