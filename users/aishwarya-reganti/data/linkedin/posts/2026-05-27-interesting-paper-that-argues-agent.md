---
id: '7465416797152841729'
date: '2026-05-27T15:01:05.178Z'
url: https://www.linkedin.com/posts/areganti_interesting-paper-that-argues-agent-skills-activity-7465416797152841729-Ucnc
likes: 142
comments: 11
images_count: 1
author_comments:
- 'We''re also running a free session on the latest updates to the AI agent stack, which includes some insights skills as well. Feel free to sign up if you''re interested: https://maven.com/p/7fd39b/the-ai-agent-stack-in-2026'
---

👀 Interesting paper that argues agent skills should be treated more like AI models: something you optimize over time instead of treating them as one time artifacts.

The paper introduces SkillOpt, a method for optimizing agent skills without changing the model weights. The model stays fixed. The agent setup stays fixed. What improves is the skill file itself, based on scored rollouts and validation.

Notes from the paper:

- Skills are becoming an adaptation layer for agents, not just better prompts.

- The strongest improvements show up in procedural tasks where the agent needs to use tools, inspect files, follow steps, and verify work.

- Small edits to a skill file can lead to meaningful gains when those edits are guided by evals rather than intuition.

- The paper also shows that optimized skills can transfer across models and agent harnesses, which makes this more useful than a narrow prompt tuning trick.

IMO though, a lot of the takeaways feel very similar to prompt optimization for a task, which is why I don’t think this is an entirely new idea. I’m also not fully sold on automatic skill optimization. 
It feels very similar to automatic prompt optimization, which still needs human oversight to avoid optimizing for the wrong behavior.

The big takeaway for me is more high level: skills, just like every other part of an AI system, need a feedback loop. They won’t work out of the box all the time.

Link: https://lnkd.in/gB-nB7gQ
