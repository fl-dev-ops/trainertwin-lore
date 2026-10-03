"""Test the Updated instructions.md + Newly Authored SKILL.md in tandem.

Replays key dialogue turns from production session cmurpfxg6000pfjiawplkcone
against the combined prompt:
  [Updated chat/agent/instructions.md] + [Lore SKILL.md]

Evaluates using TypeSafe Jev (typesafe/jev-1.13):
1. Voice Authenticity vs Robotic AI Drift
2. Pedagogical Rescue & Depth
3. Closing Sequence & Clean Termination
"""

import json
import os
import re
import time
import urllib.request
from pathlib import Path
from dotenv import load_dotenv
from pipeline.normalize import JevClient

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY required")

MODEL = "google/gemini-3.8-flash"
ROOT = Path(__file__).resolve().parents[1]

# Paths
INSTRUCTIONS_PATH = Path("/Users/suryaumapathy/Developers/Github/foreverlearning/trainertwin/application/chat/agent/instructions.md")
SKILL_PATH = ROOT / "users" / "vasanth" / "workspace" / "scenarios" / "resume-project-deep-dive-and-technical-cross-examination.md"

instructions_text = INSTRUCTIONS_PATH.read_text(encoding="utf-8")
skill_text = SKILL_PATH.read_text(encoding="utf-8")

# Unified system prompt: instructions.md + active scenario skill specification
SYSTEM_PROMPT = f"""{instructions_text}

---
# ACTIVE SCENARIO BEHAVIORAL SPECIFICATION (TOP PRIORITY)
The following is Vasanth's exact grounded behavioral skill prompt for this session.
Adhere strictly to its relational stance, decision heuristics, signature phrases, and negative boundaries.

{skill_text}
"""

TEST_TURNS = [
    {
        "turn": 1,
        "name": "Opening Turn",
        "input": "session-start",
        "context": "Start of interview. Candidate is Harini Shekar. Attached resume is on screen.",
        "history": []
    },
    {
        "turn": 4,
        "name": "Initial Buzzword Claim",
        "input": "Yeah. So the, um, AI powered Sentry trial was something where I was enabling MCP for automated error classification. And, uh, my role was to reduce the minimum triage effort and improving, uh, the engineering efficiency.",
        "history": [
            {"role": "assistant", "content": "Hello Harini, welcome to the session. I have your resume open on screen. Please introduce yourself briefly whenever you're ready."},
            {"role": "user", "content": "Hi. I'm Harini, and I have been working at Forever Learning for the last five years as a software engineer."},
            {"role": "assistant", "content": "Looking at your resume section about building an AI-powered Sentry triage automation system, what was your specific role and responsibility within this project?"}
        ]
    },
    {
        "turn": 14,
        "name": "Concrete Mechanism (Offline POS & CRDTs)",
        "input": "Internet connections are notoriously unreliable. So we embedded local databases with eventual consistency, and, uh, we made sure the conflict pre replicated data types or deterministic conflict evolution where register A and B both sell the last bottle of wine in stock while offline. Then we also made sure there is a background sync via queuing.",
        "history": [
            {"role": "assistant", "content": "Could you describe one specific technical challenge you faced while building these POS modules and how you addressed it?"}
        ]
    },
    {
        "turn": 20,
        "name": "Candidate Memory Lapse / Struggle",
        "input": "Uh-huh. So I Yeah. I don't remember, actually.",
        "history": [
            {"role": "user", "content": "I built a scalable state management and component libraries and design systems. I also worked on type safe API integration."},
            {"role": "assistant", "content": "What was a key technical decision you made in building those component libraries or the state management system, and why did you choose that approach?"}
        ]
    },
    {
        "turn": 26,
        "name": "Candidate Uncertainty on Core Framework",
        "input": "Not sure. Sorry.",
        "history": [
            {"role": "user", "content": "I consider react as most critical, and one of the projects I took was around the SIM activation project."},
            {"role": "assistant", "content": "What architectural or technical choices did you make for the large-scale post-purchase SIM activation flows using React?"}
        ]
    },
    {
        "turn": 28,
        "name": "Closing Confirmation",
        "input": "Yeah. Sure.",
        "history": [
            {"role": "assistant", "content": "Okay, we have covered the key areas I had planned today. Based on what we walked through, I will put together detailed feedback on what was solid and which core mechanisms to practice next. Shall we wrap up here?"}
        ]
    }
]

def generate_reply(messages: list[dict]) -> str:
    payload = {
        "model": MODEL,
        "messages": [{"role": "system", "content": SYSTEM_PROMPT}] + messages,
        "temperature": 0.2,
        "max_tokens": 2048,
        "reasoning": {"effort": "low"}
    }
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        msg = data["choices"][0]["message"]
        if msg.get("tool_calls"):
            calls = [f"[TOOL CALL: {tc['function']['name']}({tc['function'].get('arguments', '')})]" for tc in msg["tool_calls"]]
            content = msg.get("content") or ""
            return (content + " " + " ".join(calls)).strip()
        content = msg.get("content") or ""
        if not content:
            # Check reasoning if content was omitted by provider
            content = msg.get("reasoning") or ""
        return content.strip()

print("=" * 85)
print("TESTING UPDATED instructions.md + LORE SKILL.md WITH GEMINI 3.8 FLASH")
print("=" * 85)

generated_replies = {}
for test in TEST_TURNS:
    t_num = test["turn"]
    user_msg = test["input"]
    msgs = test["history"] + [{"role": "user", "content": user_msg}]
    reply = generate_reply(msgs)
    generated_replies[t_num] = reply
    print(f"\n--- Turn {t_num}: {test['name']} ---")
    print(f"Candidate: \"{user_msg}\"")
    print(f"Generated Trainer Reply:\n\"{reply}\"")

# -----------------------------------------------------------------------------
# Jev Evaluation: Audit Voice Authenticity and Drift
# -----------------------------------------------------------------------------
print("\n" + "=" * 85)
print("EVALUATING GENERATED RESPONSES WITH TYPESAFE JEV (typesafe/jev-1.13)...")
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

questions = {}
for t_num, reply in generated_replies.items():
    qid = f"eval_turn_{t_num}"
    questions[qid] = {
        "type": "choice",
        "instructions": (
            f"Evaluate this interviewer utterance against Vasanth's authentic voice and style:\n"
            f"Utterance: \"{reply}\""
        ),
        "criteria": {
            "vasanth_authentic": "Reflects Vasanth's natural conversational cadence, direct diagnostic probing, or authentic verbal markers.",
            "robotic_ai_drift": "Exhibits repetitive robotic formula (e.g. rigid '[Ack], <name>. Looking at...', corporate meta-commentary, or ungrounded praise)."
        }
    }

t0 = time.time()
jev_results = jev.decide(state=vasanth_reference, questions=questions)
elapsed = time.time() - t0

robotic_count = 0
for test in TEST_TURNS:
    t_num = test["turn"]
    reply = generated_replies[t_num]
    qid = f"eval_turn_{t_num}"
    ans = jev_results.get(qid, {})
    choice = ans.get("choice", "unknown")
    conf = ans.get("confidence", 0.0)
    is_robotic = (choice == "robotic_ai_drift")
    if is_robotic:
        robotic_count += 1
    tag = "🤖 ROBOTIC DRIFT" if is_robotic else "🗣️ VASANTH AUTHENTIC"
    print(f"\n{tag} [Turn {t_num}: {test['name']}] (conf: {conf:.2f})")
    print(f"  \"{reply}\"")

print("\n" + "=" * 85)
drift_rate = (robotic_count / len(TEST_TURNS)) * 100
auth_rate = 100.0 - drift_rate
print(f"BENCHMARK RESULTS (UPDATED INSTRUCTIONS + LORE SKILL.md):")
print(f"• Authentic Vasanth Voice Rate: {len(TEST_TURNS) - robotic_count}/{len(TEST_TURNS)} ({auth_rate:.1f}%)")
print(f"• Robotic AI Drift Rate: {robotic_count}/{len(TEST_TURNS)} ({drift_rate:.1f}%) [Was 57.5% in Production!]")
print(f"• Jev Evaluation Runtime: {elapsed:.2f}s")
print("=" * 85)

jev.close()
