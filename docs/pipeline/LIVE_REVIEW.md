# Live ingestion review

## Run scope

Current `pipeline/` implementation, `openai/gpt-4o`, normal `users/olga/workspace/`. Three selected sources; persistent cap of six logical calls and six actual OpenRouter HTTP attempts, including retries. Other collector/source changes are outside this run.

This is an output inspection, not a trainer-resemblance benchmark or external fact check. The expectations below were written before inspecting model output.

## Source-grounded checks

### LinkedIn: “1% — That was the conversion rate” (2026-06-15)

- Preserve 1%, 35% or more, and the under-5% diagnostic threshold with their different meanings. These are source claims, not verified conversion statistics.
- Preserve multiple touchpoints, video calls, and materials explaining “why Dubai, why now, why with you.” Do not invent a prescribed number or order of touchpoints.
- The brochure/pitch/repeated-follow-up sequence is criticized, not recommended.
- The client story is reported, not a recorded dialogue. Do not claim that this particular client demonstrably improved from 1% to 35%; the post does not establish that outcome.
- Do not use follower comments as the author's evidence.

### LinkedIn: “Your client is not interested. Now what?” (2026-09-29)

- Retain the author's self-reported 2015 start and cold-calling experience as self-reports.
- Distinguish agents' reported complaints from the author's personal beliefs.
- Preserve the advice about creating interest, sustaining engagement and understanding the client's priorities, without inventing an unstated detailed sales protocol.
- Do not use follower comments as the author's evidence.

### YouTube: “How to Stop Procrastination!” (2026-04-27)

- Preserve the suggestion to look at a self-image daily and the stated motivation/decision-making purpose.
- AI-created imagery and the “fifteen kg heavier” depiction must not become claims of actual weight gain or a real photograph.
- Preserve original turns, including short fragments, without pretending that every fragment is useful instruction.
- Speaker IDs 1 and 2 have no supplied identity mapping. Do not identify either as Olga or treat this as verified multi-party Q&A.

## Results

### Execution

| Item | Result |
| --- | --- |
| Source ingestion | All 3 completed |
| Structured records | 12: 7 knowledge, 2 cases, 3 expression |
| Wiki | 5 topic pages; build and structural lint passed |
| Report | `users/olga/workspace/reports/analysis.md` compiled |
| Twin | Incomplete; no profile published |
| Logical calls / actual HTTP attempts | 6 / 6; cap not increased |
| Provider-reported tokens | 20,838 input + 5,177 output = 26,015 |
| Provider-reported cost | $0.094585; not an audited bill |
| Elapsed time | 55.12 seconds |
| Source files changed during run | No |

The first two extraction responses failed exact-quote checks and were repaired within budget. One quote crossed unit boundaries; another omitted intervening text. The twin response then attempted an `interaction` pattern from a narrated case. Validation rejected it, and no request budget remained for repair. Consequently the overall runner exited nonzero even though ingestion, wiki build, report compilation and structural lint completed.

### Source-fidelity inspection

This is an assistant's inspection against the originals, not an external truth check, human approval, or an LLM-judge score. Stored records remain `not_reviewed`; generated records/pages have not been manually corrected.

| Record / field | Observation |
| --- | --- |
| Lead Process Review — summary | Faithfully preserves the under-five-percent diagnostic threshold and the instruction to examine the process before blaming leads. |
| Sales Process Advice — summary | Retains multiple touchpoints, video calls and materials; its quotation retains “why Dubai, why now, why with you.” Does not invent a touchpoint count. |
| Lead Conversion Rates — summary | Overgeneralizes the reported 1% example to a rate that is **“often just 1%.”** The source does not establish that frequency. |
| June sales-process post — coverage | The **35% or more** claim is absent from extracted substantive fields. It remains in preserved original context, so it is not erased from the stored source. |
| Typical but Ineffective Sales Process — cue | Attributes the “Pray” joke to the client, which the source does not establish. The cue's quote only says the client described a process; it does not itself support the detailed sequence in the extracted text. |
| Same case — unknown fields | Diagnosis, strategy, rationale, response and outcome remain null. It does not invent a demonstrated 1%→35% outcome for that client. |
| September post — coverage | Captures learning to engage disinterested clients but omits the explicit **2015** start and cold-calling history from substantive fields; originals remain available. |
| Need for Pre-Client Engagement System — summary | Strengthens a tentative “may be” explanation and shifts “before the client gets to that [follow-up] point” into **before client engagement begins**. That timing is not established by the quote. |
| Using visual motivation — summary | Adds **“past self”**, while the quoted speech does not establish a past-self photograph; later context discusses AI imagery. |
| Comparing physical appearance over time — observation | Adds a **“heavier past self”** and plural “speakers,” neither established by the cited utterance. It should describe the depiction without inventing personal history. |
| AI generated visual aid — kind | The statement about an AI-created image is supported, but `reported_exchange` is an inappropriate label for this demonstration fragment; no reported exchange is supplied. |
| Attribution and raw context | No numbered YouTube speaker was identified as Olga. Short original turns remain stored. Follower comments were excluded from extraction units. |

**Conclusion:** the infrastructure and structural safeguards work, but this sample exposes semantic overreach, misclassification and incomplete extraction. Do not treat a passing lint result as a faithful twin, and fix these extraction issues before a full-corpus run.

### Inspect the output

- Wiki: `users/olga/workspace/wiki/index.md`
- Products: `users/olga/workspace/wiki/knowledge.md`, `cases.md`, `expression.md` (JSONL alongside each)
- Report: `users/olga/workspace/reports/analysis.md`
- Original snapshots: `users/olga/workspace/sources/`
- Validation failures: `users/olga/workspace/events.jsonl`
- Provider usage: `users/olga/workspace/usage.jsonl`
- Persistent caps: `users/olga/workspace/pilot-meter.json`, `pilot-http-meter.json`
- Run diagnostics: `.pi/live-ingest-result.json`
