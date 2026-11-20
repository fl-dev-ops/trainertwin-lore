---
id: '7481739082277183488'
date: '2026-07-11T16:00:01.205Z'
url: https://www.linkedin.com/posts/areganti_hugging-face-released-a-small-open-source-activity-7481739082277183488-CcA2
likes: 347
comments: 7
images_count: 1
---

💯 Hugging Face released a small open source coding agent called Tau that can help developers understand how these agents are actually built. Pretty cool if you want to get a masterclass in coding agent system design.

Some features:
⛳ It runs in the terminal, so you can ask it to explain a repo, add tests, or fix a stack trace.
⛳It can read files, edit code, run commands, and keep durable session history.
⛳ It has built in coding tools like read, write, edit, and bash.
⛳ It supports durable JSONL sessions with resume and branching, which is a nice way to understand how state is handled.
⛳ It supports project instructions from AGENTS.md, .tau, and .agents resources.
⛳ It has context accounting, manual compaction, and optional automatic compaction.
⛳ The architecture is split cleanly across the model provider layer, the agent harness, and the coding app layer.
⛳ Tools are treated as ordinary typed functions, which is a good mental model for people building agent systems.

I think the most useful thing here is not that Tau is another coding agent.
It’s that it’s small and readable enough to study.

https://twotimespi.dev/
