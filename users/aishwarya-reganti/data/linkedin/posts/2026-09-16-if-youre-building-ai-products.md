---
id: '7505815497842565120'
date: '2026-09-16T02:31:05.994Z'
url: https://www.linkedin.com/posts/areganti_linkedins-engineering-cto-on-building-ai-native-activity-7505815497842565120-vPff
likes: 71
comments: 7
article:
  title: LinkedIn’s Engineering CTO on Building AI-Native Products in 2026
  subtitle: thenuancedperspective.substack.com
  link: https://thenuancedperspective.substack.com/p/linkedins-engineering-cto-on-building
---

👀 If you're building AI products right now, these are a few lessons I'd steal from LinkedIn!

Erran Berger, CTO of Engineering at LinkedIn, joined us at the AI Builders Summit and shared a lot about what changes when you're actually building and shipping AI at scale.

Some highlights from our discussion:
- Optimize for the product metric, not the model metric.
You can make the model materially better and still not move the business outcome. If that happens, stop tuning and look at the rest of the system. The bottleneck could be the UX, the 
workflow, or another model downstream.

- Your benchmark should be a product asset.
Don't let public leaderboards pick your model. Build a rubric around your real queries, train a judge against it, and make that evaluation pipeline reusable every time a new model lands.
Crosscheck is a pretty interesting example of this philosophy in practice. It lets users compare model outputs side by side, while also giving LinkedIn much richer signal into how different models perform across real user segments.

- Design for model replacement from day one.
You should be able to drop a new model into your system and know pretty quickly whether it performs better for your use case. If changing models is painful, every new model release becomes more tech debt.

- The moat isn't the harness. It's what the harness can reach.
Models and harnesses are getting easier to replicate. The real advantage increasingly sits in the tools, systems, workflows, and proprietary data your agents can actually act through.

- Use AI to remove handoffs, not just make each handoff faster.
At LinkedIn, PMs and designers can draft PRs, and engineers can take more work from idea to production. The bigger opportunity is changing how the work gets done, not just speeding up every step in the old process.

- Measure engineering by impact shipped, not artifacts produced.
Lines of code, PR count, and token usage are all easy metrics to optimize. The better question is how much useful software actually reaches production and what business outcome it creates.

There were a lot more gems in the conversation. We wrote a full article based on the session if you want to go deeper, and the full video recording is available as well.

Find both here: https://lnkd.in/gXCTKfQk
