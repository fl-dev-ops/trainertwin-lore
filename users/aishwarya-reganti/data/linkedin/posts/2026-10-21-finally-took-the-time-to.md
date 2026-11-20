---
id: '7518498821123895296'
date: '2026-10-21T02:30:05.909Z'
url: https://www.linkedin.com/posts/areganti_finally-took-the-time-to-review-googles-activity-7518498821123895296-vXTO
likes: 253
comments: 35
images_count: 1
---

Finally took the time to review Google's viral paper, Harness², which talks about self-improving harnesses. I see the hype, but I also think there's a long way to go before this works in the real world.

Harness² keeps the model weights fixed. For each task, it proposes changes to prompts, memory, tool guidance, guardrails, skills, scripts or subagents. It runs multiple versions under the same conditions, compares how they behave, keeps changes that appear useful and saves lessons for future tasks.

I see 2 main issues in the real world, especially for enterprise use cases:

- For open-ended work, there may be no perfect answer to check against. The system relies on model judgment to decide which behavior is better. The same blind spot could exist in the agent and in the model evaluating it, especially when the surrounding ecosystem is complex.

- There is also a governance problem. The system can rewrite guardrails, scripts and plugins, some of the exact layers controlling what the agent can do. Those changes need eval gates, versioning, staged rollouts, rollback and probably human review.

The version I would be comfortable trying today is more controlled: let it propose improvements offline, test them against a regression set, and review the changes before promoting them to production.

But this is a nice step toward harnesses also becoming scaffolding that gets commoditized or absorbed by the model pretty quickly. If a harness can improve itself, maybe those improvements can eventually be moved into the model, reducing the amount of scaffolding around it.

Was a nice read though.

Paper: https://lnkd.in/giShhcSw
