---
id: '7513614667211218944'
date: '2026-10-07T15:02:12.873Z'
url: https://www.linkedin.com/posts/areganti_nice-article-from-anthropic-on-automating-activity-7513614667211218944-aATC
likes: 296
comments: 44
images_count: 1
---

Nice article from Anthropic on automating eval design.

I would have preferred to call it semi-automating, just so we don't set unreasonable expectations, but anyhoo...😅

Anthropic added 2 commands to the claude-api skill in Claude Code:

- /claude-api build-eval helps create test cases from production traces, bug reports, support tickets, or examples you provide. It asks you to review the cases and grader before running the eval.
- /claude-api hillclimb uses that eval to improve your application. You decide what Claude can change, including the prompt, skills, tool descriptions, model settings, or harness code.

In each round, Claude looks at the failures, proposes 1 change, and runs the eval again. It can study one set of cases, but it also checks the change against held-out cases it hasn't seen. If the score improves only on the cases it studied, the change gets reverted.

Anthropic also shows a customer-support example where the loop removed unnecessary prompt steps, tried cheaper model and effort settings, and ended up with better accuracy on held-out tickets at about 1/5 of the original token cost per ticket.

It's a good step. We've built several eval-design skills in our work with companies, and I wouldn't run any of them without domain experts looking at the cases and grader. It's very easy to spend a lot of time improving the wrong thing. I like that Anthropic has at least codified the process and made those review points explicit.

Link: https://lnkd.in/gbCmRdtg
