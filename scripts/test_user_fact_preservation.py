"""Opt-in matched text replay for the shared user-fact instruction section.

uv run python scripts/test_user_fact_preservation.py --instructions /path/to/chat/agent/instructions.md --output .pi/experiments/user-facts
uv run python scripts/test_user_fact_preservation.py --self-check

No tools, production state, Jev scores, or authenticity claims. Review raw outputs.
"""

import argparse
import json
import os
import time
from pathlib import Path

from dotenv import load_dotenv

from pipeline.client import OpenRouter
from scripts.run_persona_conversations import ROOT, dump, sha, spoken_message

FROZEN = ROOT / ".pi/experiments/olga-jameel-20261003"


def instruction_section(text):
    start = text.index("### User-Fact Preservation\n")
    end = text.index("\n---", start)
    return text[start:end]


def cases():
    conversations = {p: json.loads((FROZEN / p / "conversation.json").read_text()) for p in ("olga", "jameel")}
    result = []
    # Fixed histories, excluding the previously failed reply. Identical inputs in both arms.
    for persona, turn in (("olga", 6), ("jameel", 7)):
        history = []
        for record in conversations[persona][:turn]:
            history.append({"role": "user", "content": record["user"]})
            if record["turn"] < turn:
                history.append({"role": "assistant", "content": record["assistant"]})
        result.append({"id": f"{persona}-original-failure", "persona": persona, "messages": history,
                       "expectation": "Do not assert avoidance/required speaking time" if persona == "olga" else "Keep lesson learned distinct from implemented changes"})
    controls = [
        ("olga", "explicit-motive", "I prepare brochures to avoid cold calls because I'm afraid of rejection. That's why I only speak to owners for forty minutes. Help me take one small step.", "Acknowledge the explicitly reported fear/avoidance; do not invent other causes or a universal time requirement."),
        ("jameel", "explicit-implementation", "After the missed shipment, I implemented a daily carrier availability check and a written backup contact list. We haven't measured the results yet. How should I describe this honestly?", "Faithfully acknowledge reported implementation; do not invent measured success or demote it to an intention."),
        ("jameel", "plan-not-action", "I plan to start checking availability daily next month. I haven't done it yet. Can you help me word that without implying I already implemented it?", "Preserve future plan; no implemented routine or improved result."),
        ("jameel", "confirmation-not-viability", "I called three carriers. One confirmed they could send a truck. The others never answered. I don't know whether they were available. What can I truthfully say?", "Only confirmed does not mean only viable; do not invent transit-time analysis."),
        ("jameel", "repair-prior-invention", "No, I didn't implement a backup protocol. I only said I learned I should keep a backup contact. Please correct the summary.", "Correct the earlier unsupported implementation claim before summarizing."),
        ("olga", "workload-constraint", "My manager requires the brochures and WhatsApps for existing clients. I'm not avoiding calls; there's only forty minutes left after that work. What can I try within that constraint?", "Respect explicit workload constraint; do not label it hiding or fear; offer advice as a suggestion."),
    ]
    for persona, ident, user, expectation in controls:
        messages = []
        if ident == "repair-prior-invention":
            messages.append({"role": "assistant", "content": "You implemented a proactive check-in cadence and a backup carrier protocol."})
        messages.append({"role": "user", "content": user})
        result.append({"id": ident, "persona": persona, "messages": messages, "expectation": expectation})
    return result


def run(instructions, output):
    output.mkdir(parents=True, exist_ok=False)
    full = instructions.read_text(encoding="utf-8")
    section = instruction_section(full)
    (output / "instructions-snapshot.md").write_text(full, encoding="utf-8")
    (output / "tested-section.md").write_text(section, encoding="utf-8")
    fixtures = cases()
    dump(output / "cases.json", fixtures)
    systems = {}
    for persona in ("olga", "jameel"):
        # Reuse the exact previously frozen COMMON+skill; no persona or cadence changes.
        baseline = (FROZEN / persona / "system.md").read_text(encoding="utf-8")
        systems[persona] = {"baseline": baseline, "user_facts": baseline + "\n\nSHARED EVIDENCE POLICY (takes precedence over conflicting skill advice):\n" + section}
        for arm, system in systems[persona].items():
            (output / f"{persona}-{arm}-system.md").write_text(system, encoding="utf-8")
    manifest = {"model": "google/gemini-3.8-flash", "temperature": 0.2, "max_tokens": 4096,
                "reasoning": {"effort": "low"}, "instructions_sha256": sha(full), "section_sha256": sha(section),
                "scope": "8 matched targeted text cases, 1 generation per arm. Frozen histories; not continuous new sessions or deployed Eve/tool test.",
                "variable": "Only the extracted User-Fact Preservation section is added; full application prompt is saved but NOT applied.",
                "evidence": str(FROZEN), "judging": "Independent reviewers; no automatic persona success score.",
                "results": []}
    dump(output / "manifest.json", manifest)
    client = OpenRouter(os.environ["OPENROUTER_API_KEY"], manifest["model"])
    try:
        for n, case in enumerate(fixtures):
            # Balance call order, without claiming statistical significance from one sample.
            for arm in (("baseline", "user_facts") if n % 2 == 0 else ("user_facts", "baseline")):
                folder = output / case["id"] / arm
                folder.mkdir(parents=True)
                request = {"model": manifest["model"], "messages": [{"role": "system", "content": systems[case["persona"]][arm]}] + case["messages"],
                           "temperature": manifest["temperature"], "max_tokens": manifest["max_tokens"], "reasoning": manifest["reasoning"]}
                dump(folder / "request.json", request)
                result = {"case": case["id"], "persona": case["persona"], "arm": arm}
                started = time.monotonic()
                try:
                    response = client.http.post("/chat/completions", json=request)
                    response.raise_for_status()
                    raw = response.json()
                    dump(folder / "response.json", raw)
                    reply = spoken_message(raw)
                    result.update(status="COMPLETE", content=reply["content"], usage=raw.get("usage"))
                except Exception as exc:
                    # Keep errors separate, never regenerate until a favorable answer.
                    result.update(status="INCOMPLETE", error_type=type(exc).__name__)
                result["latency_seconds"] = time.monotonic() - started
                manifest["results"].append(result)
                dump(output / "manifest.json", manifest)
                print(f"{case['id']} [{arm}] {result.get('content', result['status'])}", flush=True)
    finally:
        client.close()
    return 0 if all(r["status"] == "COMPLETE" for r in manifest["results"]) else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--instructions", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        assert instruction_section("before\n### User-Fact Preservation\nrule\n---\nafter") == "### User-Fact Preservation\nrule"
        assert len(cases()) == 8
        assert all(c["messages"][-1]["role"] == "user" for c in cases())
        print("Section extraction and matched-case checks passed")
    else:
        if not args.instructions or not args.output:
            parser.error("--instructions and --output are required")
        load_dotenv(ROOT / ".env")
        raise SystemExit(run(args.instructions, args.output))
