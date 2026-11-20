---
id: '7503829767935201280'
date: '2026-09-10T15:00:31.091Z'
url: https://www.linkedin.com/posts/areganti_with-many-enterprises-now-looking-to-build-activity-7503829767935201280-_PcP
likes: 60
comments: 1
images_count: 1
---

With many enterprises now looking to build their own agent harnesses to avoid vendor lock-in, HarnessDev is a great paper to review.

This paper explores whether LLMs can build harnesses themselves and also improve them using feedback from agent tasks.

The researchers tested six models across coding, writing, research and ML experimentation. They looked at two stages:

- Creation: start with a minimal runnable scaffold and a few example tasks. The model builds the execution loop, tool handling, context management and checks needed to complete tasks.
- Evolution: give the model feedback from runs and let it revise that code. This stage focuses on coding agents, with unseen tasks kept separate for evaluation.

A few findings from the paper:

- Switching models could break assumptions built into the harness. In an Opus search harness, repeated queries rose from about 10% to 88% when Gemini ran it.
- Some features existed in code but never ran. Several harnesses defined memory or state components without using them in recorded executions.
- Feedback helped identify specific failures. Opus caught its agent declaring success too early and added a completion check. Improvements across unseen tasks were still inconsistent.

Paper: https://lnkd.in/gKAhW2Hb
