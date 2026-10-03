"""Full Multi-Turn End-to-End Session Test: Targeting 100% Persona Alignment Across All Turns.

Tests all interview phases:
- Opening / Greeting
- Project Deep Dive
- Buzzword Challenge
- Candidate Struggle / Rescue
- Closing Review & Clean Finish
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

INSTRUCTIONS_PATH = Path("/Users/suryaumapathy/Developers/Github/foreverlearning/trainertwin/application/chat/agent/instructions.md")
SKILL_PATH = ROOT / "users" / "vasanth" / "workspace" / "scenarios" / "resume-project-deep-dive-and-technical-cross-examination.md"

instructions_text = INSTRUCTIONS_PATH.read_text(encoding="utf-8")
skill_text = SKILL_PATH.read_text(encoding="utf-8")

SYSTEM_PROMPT = f"""{instructions_text}

---
# ACTIVE SCENARIO BEHAVIORAL SPECIFICATION (TOP PRIORITY)
The following is Vasanth's exact grounded behavioral skill prompt for this session.
Adhere strictly to its relational stance, decision heuristics, signature phrases, and negative boundaries across EVERY turn.

{skill_text}
"""

FULL_CONVERSATION_TURNS = [
    {
        "turn": 1,
        "phase": "Opening / Greeting",
        "candidate": "Hi. I'm Harini, and I've been working at Forever Learning for the last five years as a frontend engineer.",
        "history": [
            {"role": "assistant", "content": "Hello Harini, welcome to the session. I have your resume open on screen. Please introduce yourself briefly whenever you're ready."}
        ]
    },
    {
        "turn": 2,
        "phase": "Project Deep Dive Intro",
        "candidate": "I'd like to talk about the AI-powered Sentry triage automation system I built to reduce error resolution time.",
        "history": [
            {"role": "assistant", "content": "Welcome, Harini. I have your resume open on screen. Let's start with one important project from your experience: what was the problem it was solving?"}
        ]
    },
    {
        "turn": 3,
        "phase": "Buzzword Probing",
        "candidate": "We enabled MCP for automated error classification across all our microservices to improve triage efficiency.",
        "history": [
            {"role": "assistant", "content": "What was the main problem your team was facing with error classification?"},
            {"role": "user", "content": "Sentry had too many noise alerts and manual triage was taking over 2 hours a day for our engineers."},
            {"role": "assistant", "content": "Got it. And what was the specific component you personally built to solve that?"}
        ]
    },
    {
        "turn": 4,
        "phase": "Candidate Struggle (Memory Lapse)",
        "candidate": "Uh-huh. So I Yeah. I don't remember the exact technical decisions for that state layer, actually.",
        "history": [
            {"role": "assistant", "content": "What was a key architectural decision you made in building your component library or state management system?"}
        ]
    },
    {
        "turn": 5,
        "phase": "Candidate Uncertainty (Not Sure)",
        "candidate": "Not sure how the virtual DOM diffing handles keys, sorry.",
        "history": [
            {"role": "assistant", "content": "No problem. Let's do one thing: in React, how does the reconciliation algorithm update the browser DOM when a list items re-order?"}
        ]
    },
    {
        "turn": 6,
        "phase": "Closing Review (Beat 1)",
        "candidate": "I think I covered the main parts of my experience. That's all from my side.",
        "history": [
            {"role": "assistant", "content": "Got it, got it. We walked through your Sentry triage project and your React frontend experience."}
        ]
    },
    {
        "turn": 7,
        "phase": "Closing Confirmation (Beat 2)",
        "candidate": "Yes, sounds good. Let's finish.",
        "history": [
            {"role": "assistant", "content": "Okay, we have covered the key areas I had planned today. Based on what we walked through, I will put together detailed feedback on what was solid and which core mechanisms to practice next. Shall we wrap up here?"}
        ]
    }
]

def generate_reply(messages: list[dict]) -> str:
    conversation = list(messages)
    spoken_chunks = []
    executed_tools = []
    
    # Simulate up to 2 tool execution steps in a turn
    for step in range(3):
        payload = {
            "model": MODEL,
            "messages": [{"role": "system", "content": SYSTEM_PROMPT}] + conversation,
            "temperature": 0.2,
            "max_tokens": 1024,
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
            content = (msg.get("content") or "").strip()
            if content:
                spoken_chunks.append(content)
            
            tool_calls = msg.get("tool_calls")
            if not tool_calls:
                break
            
            # Feed simulated tool results back into conversation
            conversation.append(msg)
            for tc in tool_calls:
                tc_name = tc["function"]["name"]
                args_str = tc["function"].get("arguments", "{}")
                executed_tools.append(f"[TOOL: {tc_name}({args_str})]")
                conversation.append({
                    "role": "tool",
                    "tool_call_id": tc.get("id", f"call_{step}"),
                    "name": tc_name,
                    "content": json.dumps({"ok": True, "status": "active", "nextAction": {"kind": "finish_session" if "confirm_end" in args_str else "continue"}})
                })
    
    parts = []
    if executed_tools:
        parts.append(" ".join(executed_tools))
    if spoken_chunks:
        parts.append(" ".join(spoken_chunks))
    return " \n".join(parts).strip()

print("=" * 85)
print("RUNNING COMPLETE FULL-SESSION MULTI-TURN TEST (ALL 7 PHASES)")
print("=" * 85)

generated_turns = []
for t in FULL_CONVERSATION_TURNS:
    msgs = t["history"] + [{"role": "user", "content": t["candidate"]}]
    reply = generate_reply(msgs)
    generated_turns.append({
        "turn": t["turn"],
        "phase": t["phase"],
        "candidate": t["candidate"],
        "reply": reply
    })
    print(f"\n[Turn {t['turn']} - {t['phase']}]")
    print(f"Candidate: \"{t['candidate']}\"")
    print(f"Trainer Reply: \"{reply}\"")

# Run Jev across ALL turns
print("\n" + "=" * 85)
print("EVALUATING ALL 7 TURNS WITH TYPESAFE JEV...")
print("=" * 85)

jev = JevClient(api_key)

vasanth_reference = """
VASANTH'S VERIFIED BEHAVIORAL CORPUS (YOUTUBE TRANSCRIPTS):
- Conversational, approachable, practical Adult-to-Adult mentor.
- Avoids mechanical repetitive formulas like 'Right, <learner>. Looking at your resume section...'
- Directly probes concrete engineering mechanics, extreme fundamentals, and implementation bottlenecks.
- Uses natural verbal check-ins: 'okay?', 'correct?', 'Let\\'s do one thing', 'Got it', 'extreme fundamentals', 'under the hood'.
- Never provides empty flattery when candidate struggles; pivots or tests simpler baseline concepts.
- When closing is confirmed, finishes cleanly without circular repetition.
"""

questions = {}
for gt in generated_turns:
    qid = f"eval_t{gt['turn']}"
    questions[qid] = {
        "type": "choice",
        "instructions": (
            f"Evaluate this interviewer utterance in the context of the '{gt['phase']}' turn:\n"
            f"Candidate: \"{gt['candidate']}\"\n"
            f"Interviewer: \"{gt['reply']}\""
        ),
        "criteria": {
            "vasanth_authentic": "Reflects Vasanth's natural conversational cadence, direct diagnostic probing, authentic rescue, or clean closing.",
            "robotic_ai_drift": "Exhibits repetitive robotic formula (e.g. rigid '[Ack], <name>. Looking at...', corporate meta-commentary, hollow praise, or circular closing loops)."
        }
    }

t0 = time.time()
jev_results = jev.decide(state=vasanth_reference, questions=questions)
elapsed = time.time() - t0

authentic_count = 0
for gt in generated_turns:
    t_num = gt["turn"]
    reply = gt["reply"]
    qid = f"eval_t{t_num}"
    ans = jev_results.get(qid, {})
    choice = ans.get("choice", "unknown")
    conf = ans.get("confidence", 0.0)
    is_auth = (choice == "vasanth_authentic")
    if is_auth:
        authentic_count += 1
    icon = "✅ VASANTH AUTHENTIC" if is_auth else "❌ ROBOTIC DRIFT"
    print(f"\n{icon} [Turn {t_num}: {gt['phase']}] (confidence: {conf:.2f})")
    print(f"  \"{reply}\"")

pct = (authentic_count / len(generated_turns)) * 100
print("\n" + "=" * 85)
print(f"FINAL RESULT ACROSS ALL PHASES: {authentic_count}/{len(generated_turns)} ({pct:.1f}%) AUTHENTIC")
print("=" * 85)

jev.close()
