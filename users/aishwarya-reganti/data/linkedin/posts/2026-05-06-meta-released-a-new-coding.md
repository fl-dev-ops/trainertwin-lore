---
id: '7457617653927432192'
date: '2026-05-06T02:30:04.532Z'
url: https://www.linkedin.com/posts/areganti_meta-released-a-new-coding-benchmark-on-activity-7457617653927432192-u1w3
likes: 94
comments: 12
images_count: 1
---

⛳ Meta released a new coding benchmark on which all frontier AI models score 0%.

The authors argue that existing benchmarks measure focused, limited tasks such as fixing a single bug or developing a single, specified feature. In ProgramBench, given only a program and its documentation, agents must architect and implement a codebase that matches the reference executable’s behavior. End-to-end behavioral tests are generated via agent-driven fuzzing, enabling evaluation without prescribing implementation structure.

A few highlights from the paper:
⛳ The benchmark has 200 programming tasks. These include smaller CLI programs, but also well known software like SQLite, FFmpeg, Lua, PHP, ripgrep, jq, fzf, and zstd.
⛳ All tested frontier models scored 0% on full task completion. Some models made partial progress, but none fully recreated a program well enough to pass the benchmark’s full test suite.
⛳The models don’t get the source code. They get access to the executable and documentation. So they need to interact with the program, observe behavior, infer requirements, and then implement their own version.
⛳ This tests a different kind of coding ability. A lot of current coding benchmarks are about localized coding tasks. ProgramBench is closer to software reconstruction: understanding behavior, making design choices, writing multiple files, setting up builds, and matching edge cases.
⛳ The generated code looked different from human code. The paper found that model generated programs were often more monolithic, with fewer files, shallower directory structures, and longer functions.
⛳  Internet access made evaluation harder. When models had unrestricted internet access, the paper observed source code lookup behavior in a meaningful number of runs. That’s a useful reminder that evaluating agentic systems gets harder once browsing is allowed.

Link: https://lnkd.in/g2rYgGnB

I guess the takeaway from papers like this is not that agent harnesses are useless.  It’s more that older typical benchmarks may overstate what they can actually do autonomously, and understate how much human grounding is still required to get something working end to end.
