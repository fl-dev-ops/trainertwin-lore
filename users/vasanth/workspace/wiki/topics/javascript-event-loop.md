# javascript event loop

> Source-local records, not independent fact verification. Original steps and qualifications are retained.

<a id="record-61da90212d6ecb62"></a>
## Understanding JavaScript Event Loop

**Product:** knowledge · **Type:** belief · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Each browser tab or application context has its own unique event loop in JavaScript.
  - “Naturally, there is only one instance. Each tab can have a different event loop running.” — [lines 1042-1042](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000234`)
  - “every tab has its own event loop.” — [lines 1046-1046](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000235`)

### Original context

**vasanth** · lines 1042-1042 · spoken_turn

> Next thing, for a given tab, let's say I'm on this app.notion.com. For a given tab, how many event loop or this the complete diagram what you have seen, right? How many such instances exist? Naturally, there is only one instance. Each tab can have a different event loop running. Okay, many people think there is only one event loop that runs across all the tabs. No. The event loop will run for each of the tab, it runs one event loop. The reason being, let's say your app might be fast, another app might be slow, they are not architected to be fast.

**vasanth** · lines 1046-1046 · spoken_turn

> So your app might get slowed down because of that. So every tab has its own event loop. Okay? That's something that you should be aware. Can a single tab have multiple event loops? That is also possible, especially whenever you have seen things like push notification etcetera, that I'll explain more. But to begin with, naturally there is only one event loop. Okay? Now, in the things that I explained so far in the summary, if you have any questions, you can raise your hand or in general also so far, whatever you have covered, right? If you have any questions, you can raise your hand.

<a id="record-891241398b58e269"></a>
## Explaining Event Loop in Interviews

**Product:** cases · **Type:** illustration · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- A detailed explanation of how the event loop can be described in interviews as an algorithm and a process, along with a focus on the setTimeout function and its movement between the call stack and API queues.
  - “And event loop whenever it is asked in the interview, you can explain event loop as an algorithm also and event loop as a process as well, how overall it's going to do.” — [lines 1022-1022](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000229`)

### Cue

- An event loop query often arises during interviews.
  - “event loop whenever it is asked in the interview” — [lines 1022-1022](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000229`)

### Diagnosis

Not stated in the cited excerpt.

### Strategy

- Explain the event loop both as an algorithm and a process.
  - “you can explain event loop as an algorithm also and event loop as a process as well” — [lines 1022-1022](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000229`)

### Rationale

Not stated in the cited excerpt.

### Response

Not stated in the cited excerpt.

### Outcome

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 1022-1022 · spoken_turn

> I think I explained why call stack is stack and about the queues, why queues are designed such a way. And event loop whenever it is asked in the interview, you can explain event loop as an algorithm also and event loop as a process as well, how overall it's going to do. Now comes a very important question, okay? If you look at this example, I have the example. So now, I explained like JavaScript engine has call stack and queues and everything, right? Now, does the set time out really gets into call stack or no? In the first

<a id="record-e811a4a613f6984d"></a>
## Event Loop Explanation

**Product:** knowledge · **Type:** belief · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- The event loop is like a polling program that checks the call stack and tells the JavaScript engine about tasks in the callback queue or micro task queue.
  - “event loop is nothing but a polling that happens, let's say for simple examples like let's say every hundred millisecond event loop checks call stack and tells JavaScript engine that hey, there is a callback queue or micro task queue which is empty, the macro task queue which has some data.” — [lines 870-870](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000205`)

### Original context

**vasanth** · lines 866-866 · spoken_turn

> Okay. See, event loop is actually something but a software. Software is not the right word. Event loop is actually a scheduler program, okay, that a browser or a different JavaScript environments will have. That is its responsibility is basically nudge the JS engine. JS engine is here, event loop is here. If you see JS engine is here, event loop is here. It'll just nudge the loop that like if your stack is empty, here are something that you can do.

**vasanth** · lines 870-870 · spoken_turn

> Okay. This is more like you could consider in a very simple words is like a program that runs at a periodic interval of time like polling, very common example, right? Like polling that happens very common. So event loop is nothing but a polling that happens, let's say for simple examples like let's say every hundred millisecond event loop checks call stack and tells JavaScript engine that hey, there is a callback queue or micro task queue which is empty, the macro task queue which has some data. Do you want to pick from that? But the ultimate responsibility of picking that task

<a id="record-7815667f532ecea3"></a>
## Event Loop Structure Explanation

**Product:** expression · **Type:** structure · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- The speaker explains the event loop, comparing it to a scheduler program that interacts with the JS engine.
  - “Event loop is actually a scheduler program, okay, that a browser or a different JavaScript environments will have. That is its responsibility is basically nudge the JS engine.” — [lines 866-866](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000204`)

### Purpose

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 866-866 · spoken_turn

> Okay. See, event loop is actually something but a software. Software is not the right word. Event loop is actually a scheduler program, okay, that a browser or a different JavaScript environments will have. That is its responsibility is basically nudge the JS engine. JS engine is here, event loop is here. If you see JS engine is here, event loop is here. It'll just nudge the loop that like if your stack is empty, here are something that you can do.
