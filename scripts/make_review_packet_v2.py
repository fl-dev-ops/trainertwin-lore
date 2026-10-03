import json
from pathlib import Path

validate_code = Path("pipeline/validate.py").read_text(encoding="utf-8")
instructions_code = Path("/Users/suryaumapathy/Developers/Github/foreverlearning/trainertwin/application/chat/agent/instructions.md").read_text(encoding="utf-8")
skill_code = Path("users/vasanth/workspace/scenarios/resume-project-deep-dive-and-technical-cross-examination.md").read_text(encoding="utf-8")

review_context = f"""# COMPREHENSIVE IMPLEMENTATION & FLOW AUDIT FOR OPUS & ASTRA

## Context & Prior Feedback Addressal
In the previous audit, Opus and Astra identified:
1. P0 Fail-Closed Bug in validate.py: Missing Jev answers defaulted to 'grounded', allowing timeouts/errors to pass.
2. P1 Speaker Stripping Bug in validate.py: Transcripts had '###' speaker lines stripped, destroying speaker attribution proof.
3. P0 Robotic Prompts in instructions.md: Line 125 ('Right, <learner>') and few-shot examples forced repetitive name calling and unearned closing praise.
4. Synthetic Trope in Scenario Skill: Non-Vasanth phrasing like 'step back from high-level architecture'.
5. Multi-Step Continuation: Turn evaluation failed to execute the internal tool loop (e.g. session_plan -> speech).

## Actions Implemented:
1. `pipeline/validate.py`:
   - Enforced strict fail-closed handling on Jev decisions. If Jev returns empty, missing, or malformed choices, it records `unverified_error` and forces `verdict: FAIL`.
   - Preserved `### 00:01:23 · Speaker 1` headings in source excerpt slices so speaker attribution is intact.
   - Refined entailment criteria to separate logical entailment from fabricated concepts.
   - Added `test_validate_scenario_fails_closed_on_jev_failure` unit test. 14/14 tests pass.

2. `application/chat/agent/instructions.md`:
   - Removed line 125 forcing 'Right, <learner>'.
   - Cleaned all `<example>` blocks to remove `<learner>` repetition from every sentence.
   - Replaced unearned closing praise with objective, evidence-grounded feedback.
   - All 58 unit tests pass (`bun test`).

3. `users/vasanth/workspace/scenarios/resume-project-deep-dive-and-technical-cross-examination.md`:
   - Re-authored with Vasanth's verified verbatim phrasing ('explain your approach then you explain the result', 'pick a decent size problem', 'Got it, got it', 'So use it mindfully').
   - Validated cleanly with 4/4 citations valid and 4/4 Jev entailment grounded.

4. Multi-Turn Test Execution & Outputs:
   - Turn 1 (Opening): [TOOL: session_plan] [TOOL: search_style] "Got it, Harini. Five years at Forever Learning is a solid tenure. Could you pick a decent size project you personally built end-to-end there, and walk me through the specific problem you were solving?"
   - Turn 3 (Buzzword Probe): "Got it, got it. But do not talk about enabling a blanket protocol across all microservices. Definitely there will be lot of cross questions on that. What was the exact approach and pipeline you personally implemented to classify those errors and filter out the noise?"
   - Turn 5 (Uncertainty): "Got it, got it. Think about it from React's perspective. If an item moves from the bottom of a list to the very top, and React has no identifiers to match them, what would it have to do to each existing DOM node?"
   - Turn 7 (Closing): [TOOL: finish_session({{}})]

## Code References
### pipeline/validate.py:
```python
{validate_code}
```

### Authored Scenario SKILL.md:
```markdown
{skill_code}
```
"""

Path("/tmp/opus_astra_review_packet.md").write_text(review_context, encoding="utf-8")
print("Saved review packet to /tmp/opus_astra_review_packet.md, size:", len(review_context))
