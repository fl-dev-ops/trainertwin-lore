# Auto-iterator handoff — output quality, not score chasing

Run the config-driven optimization loop in this workspace. This is a native Pi adaptation
of the installed OpenCode `auto-iterate` skill; `references/auto-iterator.md` describes the
role, but config.yaml and this bounded authority contract override its generic defaults.
No external agent process, recursion, installs, or unbounded loop.

## Objective

Improve the information produced by TrainerTwin: source-faithful evidence and knowledge,
concrete observations of communication, and clearly proposed (not allegedly observed)
twin adaptations. The review found that rich original posts were reduced to generic topic
summaries. A post's author was also presented like the speaker of all embedded dialogue.
Look for root causes and make the smallest generalizable corrections. Do not hardcode
this author, the development posts, their wording, or evaluator expectations.

## Ownership

You are the sole writer for one tightly coupled representation/prompt seam, in isolated
`workspace/current`. You may modify only pipeline/{sources,core,prompts,twin}.py there.
Do not edit the main repository, workspace/best (runner-owned), references, tests,
configuration, evaluator, history, budget, result artifacts or locked-files manifest.
The main repository contains extensive pre-existing user edits and data moves; never
reset, clean, stage, commit, delete or restore any of those files.

You may read `research.md`, config.yaml, baseline code, development results, and the
original two development posts identified in the seed's active manifests. Do not inspect
the held-out input or invoke the holdout command. Keep it for the parent's final check.
Do not read .env or other credential files. Only the frozen runner may access the API.

## Commands

1. Establish the unchanged baseline FIRST:
   `bash run.sh experiment --note 'Unchanged baseline'`
2. Inspect the generated packet, judge feedback and concrete source/output differences in
   `results/run_001/`. The point is the actual information, not the numeric score alone.
3. Form one hypothesis, edit current's allowed files, and run:
   `bash run.sh experiment --note 'Specific failure class and proposed correction'`
4. The runner performs frozen tests, runs the full development pipeline with reusable
   caches, judges anonymous output packets, records evidence, and owns keep/discard.
   Follow its decision; it restores current to best automatically.
5. At most one further candidate is available (three runs total, including baseline).
   Stop after two non-improvements, budget exhaustion, or a failure needing a decision.
6. Return a concise report with actual before/after examples, files changed, tested
   behavior, score/call evidence, what did NOT improve, and remaining uncertainties.
   The durable answer path is supplied by the subagent output binding.

The hard API budget is <=12 actual OpenRouter HTTP attempts overall; development uses
<=8 and <=3/experiment. Four are reserved for the parent. Retries and judging count.
Do not bypass the runner or reset counters. Use existing `.venv` tooling only.

## Evaluation and limits

The fixed rubric inspects evidence, wiki findings, examples and twin output against raw
sources. It rewards fidelity, useful specifics, meaningful distinctions and usability,
not volume or polished adjectives. Critical factual/attribution errors and regression
failures disqualify a candidate. The evaluator's own feedback quotes must match the
sources. Treat its scores as noisy research feedback, not ground truth or trainer likeness.

All existing test expectations stay frozen. If a useful additive output field is needed,
keep legacy in-memory patterns/test doubles compatible without weakening validation for
fields actually supplied. Do not loosen citation, scope, speaker or artifact safeguards.
If a change needs more API calls than fit this pass (e.g. re-extracting/rebuilding many
upstream artifacts), report the limitation rather than claiming it was evaluated.

A malformed judge response or genuine runner/tool/provider failure is not an application
quality verdict. Stop and contact the supervisor with the exact error/artifact; do not
modify the evaluator, silently change models/tools, or launch an alternate CLI.

## Acceptance

- Original inputs/code untouched and protected-file checks pass.
- Baseline plus at most two candidate experiments, within the shared cap.
- Best code passes the existing tests; no new dependencies.
- Actual output evidence supports any claimed improvement; residual weaknesses are explicit.
- Best stays isolated until the parent reviews the patch and untouched-source comparison.
