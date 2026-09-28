---
id: '7495831894887002112'
date: '2026-08-19T13:19:49.563Z'
url: https://www.linkedin.com/posts/suryaumapathy2812_weve-been-benchmarking-different-llms-in-activity-7495831894887002112-ZjG_
likes: 24
comments: 4
---

We've been benchmarking different LLMs in Trainer Twin (Forever Learning) as we are building digital human twins for trainers. 

Not accuracy benchmarks, but behaviour benchmarks.

Same system prompt, same temperature, same token limits. 25 models. 5 interview scenarios. 1,613 total turns.

And the models didn’t just give different answers. They behaved like completely different interviewers.

Sharing my condensed observations below:

👉  Gemini 3.6 Flash was the strongest overall interviewer. Detailed feedback, technically relevant follow-ups, and good tool use. It understood things like transactional outboxes, CRDTs and React race conditions in context. But it also had some protocol-level errors.

👉 GPT-5.6 Luna was the most reliable. Concise, disciplined and consistent. Good second-order questions, stayed in character and followed the interview flow without drifting. Less ambitious than Gemini, but very dependable.

👉 GPT-4o was fluent and natural, with the fastest first-token latency among the non-Qwen models. But it sometimes wasn’t listening. It would suggest coding exercises during a system design interview or pivot to a new topic instead of following up.

👉 Claude Haiku was detailed and technically strong, but sometimes leaked <thinking> tags into the output. Good model, wrong format.

👉 Qwen 3.7 Flash was the fastest model I tested at around half a second to first token. It also stayed in character, asked concise follow-ups and didn’t ramble. It didn’t try to impress. It just did the job. For roleplay, that restraint actually felt more natural.

👉 DeepSeek was slow and frequently hit the token cap. Mimo had similar tool issues. Inkling sometimes returned serialized tool requests as visible text.

👉 Grok 4.6 had decent technical instincts but drifted into unrelated topics. Kimi K3 was concise to the point of being shallow. GPT-OSS models on Fireworks produced detailed responses that were often truncated.

So here’s our thought:

When you stop evaluating models on “did it get the answer right?” and start asking:

Does it probe? Does it challenge you? Does it notice when you’re stuck? Does it give hints or answers? Does it adapt? Does it stay in character?

That's when you start evaluating behaviour, not intelligence.

And as for us, we are building AI versions of teachers, engineers, coaches and interviewers, so, that distinction matters a lot.

Curious what others have noticed when running different LLMs on the same task. Do you see different “personalities” emerge? Or does it not matter as long as the experience feels right?

Shanmuga(Shyam) Anandaraman Harini Shekar Mohammed Hasan Catherine Nivedha Dharshini Jenefer Bhuvan T

## Comments (3)

### Praveen Kumar (Software Engineer @Zipstack)
> Surya Umapathy Fascinating that Qwen came out on top. Curious if its restraint held up over longer sessions?

### Vinit Gore (CSE & AI Enthusiast | AI Researcher | Ex-NavGurukul | Ex-Freshworks | MTech. AI from IITJ)
> Back when I built a Socratic tutor 1 year back, I had also used Gemini-2.5-Flash. No complaints until we changed it to DeepSeek. Then, the application started facing frequent silent rate-limits. The responses however, obeyed the prompt and the answers seemed to be similar as before. You can try the Socratic tutor at https://flowchart.navgurukul.org
> 
> One thumb rule to keep in mind: Less intelligent the model, longer and structured your prompt should be. I would rather prefer going with a lesser intelligent model with more control like using separate stage-wise prompts. 
> 
> Rutwik Kadam Kunal Shukla Inviting you to share your insights from the interviewer app.

### Shanmuga(Shyam) Anandaraman (Co-Founder & CEO TrainerTwin | Freshworks | FRILP (STANFORD & IIMA incubated) | GoldmanSachs, Newyork | Rutgers University, New jersey | CEG Guindy Annauniversity, Chennai)
> Karthikeyan Marudhachalam any experiences you have had on this while working on voiceAi, at 8loop ? 
> 
> Hope this is useful for people on the fence, thinking about right models to use for Ai-Roleplays, Ai-MockInterviews, Ai-Conversational-Twins.
> 
> Tagging a few who will find value in this.
> cc - Kowshik Chilamkurthy, Naman Soni, Raka Dalal

