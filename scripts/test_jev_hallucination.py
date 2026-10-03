"""Accurate Jev Entailment & Hallucination Test using state=source_text."""

import json
import os
import time
from dotenv import load_dotenv
from pipeline.normalize import JevClient

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
jev = JevClient(api_key)

TEST_CASES = [
    {
        "id": "1_grounded_framework",
        "description": "True Grounded Rule: 4-Point Project Walkthrough",
        "source": (
            "Vasanth: First, what was the project and what problem was it solving? "
            "Second, what was your specific role and approach? "
            "Third, what exactly did you build or how did you solve it? "
            "And fourth, what was the outcome or impact of the project?"
        ),
        "claim": "Direct the candidate to explain their project using 4 anchors: the problem, approach, solution, and impact.",
        "expected": "grounded"
    },
    {
        "id": "2_hallucinated_phrase",
        "description": "Synthetic Phrase: 'step back from high-level architecture'",
        "source": (
            "Vasanth: No problem, no problem. Okay? So tell me, have you heard the term reconciliation in React? "
            "Like how React basically updates the DOM whenever something changes?"
        ),
        "claim": "Vasanth tells candidates: 'Let us step back from the high-level architecture and look at the core mechanics of React itself.'",
        "expected": "hallucinated"
    },
    {
        "id": "3_invented_theory",
        "description": "Invented Academic Theory: Eric Berne Transactional Analysis",
        "source": (
            "Olga: When you make a cold call, don't sound needy. You need to speak like a professional peer. "
            "Ask them what properties they currently own before offering discounts."
        ),
        "claim": "Olga teaches sales agents to apply Eric Berne's Transactional Analysis Adult-Parent ego state model to cold calls.",
        "expected": "hallucinated"
    },
    {
        "id": "4_guest_speaker_attribution",
        "description": "Guest Speaker Quote: Srijan Gulati misattributed to Vasanth",
        "source": (
            "Speaker 1 (Srijan Gulati): And if you lay a really strong fundamentals underneath, whatever pillar you grow on top will stay solid.\n"
            "Speaker 2 (Vasanth): Correct, correct. You have to be patient with the preparation."
        ),
        "claim": "Vasanth advises candidates: 'If you lay a really strong fundamentals underneath, whatever pillar you grow will stay solid.'",
        "expected": "hallucinated"
    },
    {
        "id": "5_lodash_complexity",
        "description": "Grounded Performance Heuristic: Lodash Overhead",
        "source": (
            "Vasanth: But remember, all these approaches will add some complexity into the program—basically whether you use Lodash or clone recursively, "
            "all of this is gonna be some costly operation. So use it mindfully."
        ),
        "claim": "Vasanth warns that using Lodash or recursive cloning adds performance overhead and complexity, so use it mindfully.",
        "expected": "grounded"
    },
    {
        "id": "6_verbatim_signature_phrase",
        "description": "Signature Phrase Check: 'Let\\'s do one thing'",
        "source": (
            "Vasanth: Let's do one thing. You you start the implementation where at least let it start updating the time. "
            "Stop part will come. Like how do we solve? Probably by the time you start solving it you might get some idea."
        ),
        "claim": "Vasanth uses the phrase 'Let\\'s do one thing' when breaking down an implementation block.",
        "expected": "grounded"
    },
    {
        "id": "7_invented_signature_phrase",
        "description": "Invented Signature Phrase: 'Always remember to synergize your components'",
        "source": (
            "Vasanth: Let's do one thing. You you start the implementation where at least let it start updating the time. "
            "Stop part will come. Like how do we solve? Probably by the time you start solving it you might get some idea."
        ),
        "claim": "Vasanth uses the signature phrase: 'Always remember to synergize your components.'",
        "expected": "hallucinated"
    }
]

print("=" * 80)
print("ACCURATE JEV EVALUATION: SOURCE AS 'STATE' + CRITERIA CLASSIFICATION")
print("=" * 80)

correct_count = 0
total_time = 0

for case in TEST_CASES:
    t0 = time.time()
    # In Jev, the source text IS the state. The question evaluates the claim against the state.
    res = jev.decide(
        state=f"TRANSCRIPT / EVIDENCE EXCERPT:\n\"\"\"{case['source']}\"\"\"",
        questions={
            "entailment": {
                "type": "choice",
                "instructions": (
                    f"Evaluate whether the following claim is strictly grounded in the excerpt:\n"
                    f"Claim: \"{case['claim']}\""
                ),
                "criteria": {
                    "grounded": "The claim is factually supported, directly asserted, or logically entailed by the excerpt without misattributing speakers or inventing terminology.",
                    "hallucinated": "The claim invents facts, uses terminology not present in the excerpt, or misattributes statements."
                }
            }
        }
    )
    duration = time.time() - t0
    total_time += duration

    ans = res.get("entailment", {})
    choice = ans.get("choice", "unknown")
    conf = ans.get("confidence", 0.0)
    is_correct = (choice == case["expected"])
    if is_correct:
        correct_count += 1

    symbol = "✅ PASS" if is_correct else "❌ FAIL"
    print(f"\n{symbol} [{case['id']}] ({case['description']})")
    print(f"  Claim: \"{case['claim']}\"")
    print(f"  Expected: {case['expected']} | Jev Decision: {choice} (conf: {conf:.2f}) in {duration:.3f}s")
    if not is_correct:
        print(f"  Details: {ans}")

print("\n" + "=" * 80)
print(f"FINAL SCORE: {correct_count}/{len(TEST_CASES)} correct ({correct_count/len(TEST_CASES)*100:.1f}%) in {total_time:.2f}s (~{total_time/len(TEST_CASES):.3f}s/check)")
print("=" * 80)

jev.close()
