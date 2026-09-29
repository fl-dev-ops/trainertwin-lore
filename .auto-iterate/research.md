# Research summary: improving TrainerTwin's information products

## Goal

Improve actual pipeline output quality. A successful loop must leave information that is
more faithful, concrete, useful and inspectable, without silently weakening safeguards.
A higher model-judge number alone is not sufficient.

## Sources for this analysis

Local code (`sources.py`, `core.py`, `prompts.py`, `twin.py`), the saved live pilot and its
original development posts, the prior output review, and the prompt-engineering skill's
principles: diagnose observed failures, trace their cause, generalize the failure class,
and make the smallest testable change. No external research or trainer approval is claimed.

## Findings

- The source foundation now preserves original context, 38 regression tests pass, and
  the live pilot produced 12 cards, four topics and two cited expression observations.
  That proves mechanics, not semantic adequacy.
- The first twin observation mostly summarizes a taught sales method rather than how
  the writer communicates. The second identifies step-by-step instructions but misses
  concrete explanatory structure. Both are under-specific despite rich original passages.
- A post narrating client/coaching exchanges is authored text containing reported speech,
  not a recording of those events. Authorship of a whole post is not speaker identity for
  every quoted sentence. Avoid both claiming verified practice and dismissing narrated
  experience as merely hypothetical/theoretical.
- Observation and proposed runtime adaptation are different claims. A reasonable design
  adaptation must be labeled as a proposal, supported by the source observation, and bounded
  to an appropriate context. A public call-to-action is not a universal chat policy.
- Additional items, elaborate terminology, repetitive disclaimers and longer prompts can
  game subjective scoring without improving information. Evaluate against complete raw
  source passages and inspect actual before/after artifacts.

## Evaluation design

Use frozen regression tests and artifact integrity as hard gates. A separate OpenRouter
request receives anonymous source-grounded output packets with no candidate code, previous
scores, suggested answer, or optimization rationale. Four anchored criteria (fidelity,
useful information, distinctions, usability) are weighted 0.40/0.25/0.20/0.15. Compare the
candidate and current best in the same judging request, with randomized packet ordering.
The judge must cite source text and describe concrete gains and remaining errors.
Scores are a noisy selection aid, not calibrated accuracy. A paired untouched-source check
is reserved for the parent after development; the optimizer must not inspect it.

## Scope and simplicity

One writer owns the tightly coupled source-to-output representation and prompting seam.
The four allowed files provide room to fix a root cause, not an instruction to modify all
of them. Prefer a focused prompt/representation correction if it addresses the observed
failure. Existing tests, schemas and clients remain usable; backward-compatible additions
are preferable to breaking the interface. No new architecture, database or dependency.

## Budget

At most 12 actual OpenRouter HTTP requests across the entire pass, including retries and
judging. Development may use at most eight, with at most three per experiment; four are
reserved for the final untouched-source check. There is one unchanged baseline and at most
two candidate experiments. The full dev path runs on cached upstream artifacts unless a
change legitimately invalidates them. Expensive upstream changes may not fit this pass;
report that limit instead of bypassing the cap or pretending those stages were exercised.

## Outcomes to report

- Concrete source/output examples that became better, stayed weak, or regressed.
- What changed, why it addresses a failure class, and what the checks actually establish.
- API request counts/usage, paired scores, keep/discard decisions and untouched-source results.
- Residual semantic uncertainty, tiny sample size, single-platform coverage, judge variability,
  and the absence of trainer-approved conversation evaluation.
