"""Comparative Replay Benchmark: Baseline vs. TrainerTwin Lore SKILL.md.

Replays candidate Harini's key turns from production session cmurpfxg6000pfjiawplkcone
against both:
1. Baseline (current production instructions.md + raw persona prompt)
2. Lore SKILL.md (Vasanth calibrated Trigger-Action-Avoid scenario skill)

Evaluates on:
- Robotic opener rate (e.g. "Right, <name>", "Okay, <name>")
- Signature phrase presence (e.g. "Got it", "Wonderful", "under the hood")
- Buzzword probe depth (T04/T06: does it accept or isolate a mechanism?)
- Rescue handling on struggle (T20: drops abstraction level vs stays abstract)
- Premature termination check (T26: bails to wrapup vs tests fundamentals)
"""

import json
import os
import re
from pathlib import Path
from dotenv import load_dotenv
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "google/gemini-3.8-flash"

SKILL_PATH = ROOT / "users" / "vasanth" / "workspace" / "scenarios" / "mock-interview-on-resume-project-deep-dive-impact-quantifica.md"
PROD_INSTRUCTIONS_PATH = Path("/Users/suryaumapathy/Developers/Github/foreverlearning/trainertwin/application/chat/agent/instructions.md")

CANDIDATE_TURNS = [
    {
        "turn": 4,
        "situation": "Initial Buzzword Claim",
        "input": "Yeah. So the, um, AI powered Sentry trial was something where I was enabling MCP for automated error classification. And, uh, my role was to reduce the minimum triage effort and improving, uh, the engineering efficiency.",
        "history": [
            {"role": "assistant", "content": "Hello Harini Shekar, welcome to this session. I have your resume open on screen. When you're ready, please introduce yourself briefly so we can get started."},
            {"role": "user", "content": "Hi. I'm Harini, and I have been working at Forever Learning for the last five years. and, uh, I'm a software engineer. And... sorry. I've been working at Lotus Split."},
            {"role": "assistant", "content": "Right, Harini. Looking at your resume section about building an AI-powered Sentry triage automation system, can you explain your specific role and responsibility within this project?"}
        ]
    },
    {
        "turn": 20,
        "situation": "Candidate Memory Lapse / Struggle",
        "input": "Uh-huh. So I Yeah. I don't remember, actually.",
        "history": [
            {"role": "user", "content": "I built a scalable state management and component libraries and design systems. I also worked on type safe API integration and system configurations."},
            {"role": "assistant", "content": "What was a key technical decision you made in building those component libraries or the state management system, and why did you choose that approach?"}
        ]
    },
    {
        "turn": 26,
        "situation": "Candidate Uncertainty on Core Framework",
        "input": "Not sure. Sorry.",
        "history": [
            {"role": "user", "content": "I consider react as most critical, and, uh, um, one of the projects I took was around, uh, um, as I said, the SM activation project."},
            {"role": "assistant", "content": "Harini, what architectural or technical choices did you make for the large-scale post-purchase SIM activation flows using React?"}
        ]
    }
]

def call_llm(system_prompt: str, messages: list[dict]) -> str:
    payload = {
        "model": MODEL,
        "messages": [{"role": "system", "content": system_prompt}] + messages,
        "temperature": 0.2,
    }
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {API_KEY}",
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
        return (msg.get("content") or "").strip()

def run_benchmark():
    skill_text = SKILL_PATH.read_text(encoding="utf-8")
    prod_instructions = PROD_INSTRUCTIONS_PATH.read_text(encoding="utf-8") if PROD_INSTRUCTIONS_PATH.exists() else "You are an interviewer."

    print("=" * 70)
    print("COMPARATIVE REPLAY BENCHMARK: BASELINE vs. LORE SKILL.md")
    print(f"Model: {MODEL}")
    print("=" * 70)

    for case in CANDIDATE_TURNS:
        print(f"\n--- Turn {case['turn']}: {case['situation']} ---")
        print(f"Candidate: \"{case['input']}\"\n")

        # 1. Baseline production prompt
        baseline_messages = case["history"] + [{"role": "user", "content": case["input"]}]
        baseline_reply = call_llm(prod_instructions, baseline_messages)
        print(f"[BASELINE (Production Instructions)]:\n{baseline_reply}\n")

        # 2. Lore SKILL.md prompt
        lore_system = (
            "You are a real-time voice interview twin operating strictly under this behavioral skill specification.\n\n"
            f"{skill_text}\n\n"
            "MANDATORY VOICE CONSTRAINTS FOR TTS:\n"
            "- Exactly one focal question.\n"
            "- Strictly 2 to 4 sentences maximum.\n"
            "- Zero markdown formatting (no bold, no backticks, no bullets).\n"
            "- Spell out all numbers and abbreviations phonetically."
        )
        lore_reply = call_llm(lore_system, baseline_messages)
        print(f"[LORE SKILL.MD (Vasanth Grounded Skill)]:\n{lore_reply}\n")

        # Quick comparative metrics
        print("Analysis:")
        robotic_rx = re.compile(r"^(Right|Okay|Thanks|Understood),\s+[A-Z][a-z]+", re.IGNORECASE)
        b_robotic = bool(robotic_rx.search(baseline_reply))
        l_robotic = bool(robotic_rx.search(lore_reply))
        print(f"  • Baseline robotic opener: {b_robotic} | Lore robotic opener: {l_robotic}")
        
        sig_phrases = ["wonderful", "got it", "under the hood", "fundamentals", "one stack", "extreme fundamentals"]
        b_sig = [p for p in sig_phrases if p in baseline_reply.lower()]
        l_sig = [p for p in sig_phrases if p in lore_reply.lower()]
        print(f"  • Baseline signature phrases: {b_sig} | Lore signature phrases: {l_sig}")

if __name__ == "__main__":
    run_benchmark()
