---
id: '7457791336210018304'
date: '2026-05-06T14:00:13.615Z'
url: https://www.linkedin.com/posts/areganti_this-paper-is-a-super-deep-dive-into-how-activity-7457791336210018304-6lfT
likes: 571
comments: 15
images_count: 1
---

🙌 This paper is a super deep dive into how Claude Code works under the hood. It’s really useful as a system design artifact for anyone building agentic systems.

Claude Code has become one of the gold standards for agent harnesses. People are using it extensively to build software, but also increasingly as a knowledge coworker.

This paper analyzes Claude Code based on the publicly available code and documentation. I’ll let you read the paper for the exact details, but here are a few things I learned that I didn’t know before.

- The “agent” part is tiny compared to the harness: The paper cites an estimate that only about 1.6% of Claude Code’s codebase is AI decision logic, while 98.4% is operational infrastructure. That means the real engineering weight is in permissions, tool routing, context management, recovery, sessions, hooks, and execution control.

- Claude Code has up to 54 built in tools, but the model doesn’t always see all of them.: The paper says 19 tools are always included, while 35 are conditionally included based on feature flags, environment variables, user type, worktree mode, agent swarm settings, and other runtime conditions.

- Context compaction is not one thing, it’s a five stage pipeline: Claude Code doesn’t just truncate old messages. The paper describes five different context reduction strategies: budget reduction, snip, microcompact, context collapse, and auto compact. Each handles a different kind of context pressure.

- Permissions don’t fully carry over when you resume a session: The transcript is stored, but session scoped permissions live in memory and are not serialized into the transcript. On resume, Claude Code rebuilds the permission context from CLI arguments and disk settings, and unknown requests fall back to deny first prompting.


Really fun paper to read if you want to understand how frontier agent harnesses are built, and what to think about when designing your own.

Link: https://lnkd.in/gkpFP9rk
