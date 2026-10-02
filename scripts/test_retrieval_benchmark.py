"""Benchmark retrieval across Olga, Vasanth, and Jameel with 10 queries each."""

import json
import os
import time
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

from pipeline.retrieve import retrieve

QUERIES = {
    "olga": [
        "Client says: 'I will wait until prices crash before buying'",
        "How to handle a buyer who completely ghosts after receiving property options",
        "What should an agent do when the client asks for an unrealistic 40% distressed discount?",
        "How does Olga explain off-plan vs secondary market investment?",
        "Establishing authority and status when booking appointments with high-net-worth clients",
        "Overcoming fear and panic in the property market during war or regional conflict",
        "How to make cold calls when starting with zero referrals in Dubai",
        "Client says: 'I need some time to think' and stalls on making an offer",
        "Explaining the decision-making funnel and buyer awareness stages",
        "How to handle clients who say 'Dubai is oversupplied with new projects'",
    ],
    "vasanth": [
        "Candidate gets stuck on implementing array reduce or map polyfill",
        "Explaining JavaScript closures and lexical scope in a technical interview",
        "How does Vasanth explain debouncing vs throttling for search inputs?",
        "How to design an autocomplete system for frontend system design",
        "Explaining the event loop, microtasks, and macrotasks execution order",
        "Candidate argues with the interviewer about feedback or defends a wrong answer",
        "How to handle the 'Tell me about yourself / your project' interview question",
        "Difference between shallow copy and deep copy in JavaScript",
        "How to optimize React component re-rendering using useMemo and useCallback",
        "Solving two-pointer linked list problems in coding interviews",
    ],
    "jameel": [
        "How to answer behavioral interview questions using the STAR method",
        "What to do when someone sends you a nasty or aggressive work email",
        "Why your supply chain resume is getting rejected and how to fix it",
        "Explaining the difference between corporate and humanitarian supply chains",
        "How to explain Demand Planning vs Supply Planning in a job interview",
        "What questions should a candidate ask the interviewer at the end of the meeting?",
        "Using the 5 Whys technique for root cause analysis in operations",
        "Transitioning into supply chain from an engineering or non-supply chain background",
        "How to give constructive feedback to team members without triggering defensiveness",
        "How to prepare for the P&G or Amazon supply chain interview",
    ],
}


def run_benchmark():
    api_key = os.getenv("OPENROUTER_API_KEY", "")
    if not api_key:
        raise SystemExit("Set OPENROUTER_API_KEY")

    report = {}

    for user, queries in QUERIES.items():
        ws = (ROOT / "users" / user / "workspace").resolve()
        data_dir = (ROOT / "users" / user / "data").resolve()

        print(f"\n{'='*70}\nBENCHMARK: {user.upper()} (10 QUERIES)\n{'='*70}")
        user_results = []

        for idx, q in enumerate(queries, 1):
            t0 = time.time()
            res = retrieve(ws, data_dir, q, api_key, max_clips=4)
            dt = time.time() - t0

            concept = res.get("matched_concept") or "lexical-fallback"
            conf = res.get("concept_confidence", 0.0)
            clips = res.get("clips", [])

            print(f"\nQ{idx}: \"{q}\"")
            print(f"  Matched: [{concept}] (conf: {conf:.2f}, {dt:.2f}s) → {len(clips)} clips found")
            for c_i, clip in enumerate(clips[:2], 1):
                print(f"    Clip {c_i}: \"{clip['title']}\" ({clip['path']})")
                print(f"      \"{clip['verbatim_text'][:120]}...\"")

            user_results.append({
                "query": q,
                "concept": concept,
                "confidence": conf,
                "latency_s": round(dt, 2),
                "clip_count": len(clips),
                "clips": clips,
            })

        report[user] = user_results

    out_file = ROOT / "workspace_retrieval_benchmark.json"
    out_file.write_text(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"\n\nFull benchmark report saved to {out_file}")


if __name__ == "__main__":
    run_benchmark()
