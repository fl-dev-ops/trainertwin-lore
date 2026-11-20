---
id: '7466314975649927168'
date: '2026-05-30T02:30:07.619Z'
url: https://www.linkedin.com/posts/areganti_the-biggest-ai-coding-question-today-activity-7466314975649927168-yZEv
likes: 100
comments: 17
images_count: 1
author_comments:
- |-
  Mihail's courses:
  1. Stanford course: https://themodernsoftware.dev/
  2. Maven course (with a special promo code): https://maven.com/the-modern-software-developer/ai-course?promoCode=problem-first-26
---

😅 The biggest AI coding question today: how do you get to production without shipping vibe coded slop?

A lot of developers now understand that AI can help them move fast. You can vibe code a prototype, generate a feature quickly, and get a working draft in minutes. But the harder question is, how do you make sure the code actually stands the test of time?

This is exactly what Mihail Eric covered in our internal Chai & AI community session last week. 

Mihail teaches the "The Modern Software Developer" course at Stanford, is Head of AI at Monaco, and was also a colleague of mine back at Alexa. In the session, he introduced his RePPIT framework for using AI to ship production quality code.

RePPIT breaks down the coding process into five deliberate steps: (Re)search, (P)ropose, (P)lan, (I)mplement, and (T)est.

A few ideas from the RePPIT framework, although I’d recommend reading the whole the whole article we wrote around the session (linked below):

⛳ Research the codebase: Before asking AI to implement anything, first ask it to understand the architecture, file layout, dependencies, design decisions, and existing patterns. This keeps the model grounded in the actual codebase.

⛳ Propose solutions: Instead of jumping straight into code, ask the model to generate a couple of different implementation paths with tradeoffs, validation plans, and open questions. This is where you, as the developer, make the judgment call.

⛳ Plan the chosen solution: Once you pick a direction, turn it into a proper design doc. This helps define what’s in scope, what’s out of scope, what files need to change, and how the feature should be tested.

⛳ Implement the plan: Only after the research, proposal, and planning steps should the model start writing code. At this point, it has enough context to avoid guessing its way through the implementation.

⛳ Test what got built: Don’t let the same model instance blindly approve its own work. Use a fresh context or a different model to review, test, and critique the implementation before you trust it.

I think a lot of this boils down to strong context engineering. It was also super useful to walk through a concrete example, which you can see in the article.

Article: https://lnkd.in/gG9uF6kC

Mihail also runs an incredibly cool course at Stanford as well as on Maven. You can find links to both below!
