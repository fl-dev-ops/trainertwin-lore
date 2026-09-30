# javascript concepts

> Source-local records, not independent fact verification. Original steps and qualifications are retained.

<a id="record-c87e24d5f93c0adc"></a>
## Call Stack Execution

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Anything that gets executed, even if it is not part of the JavaScript engine's capability, goes to the call stack at once, comes out, and gets into the other block.
  - “Anything that get executed, even if it is not something that is not the JavaScript engine's capability, still it is something that goes to call stack at once and comes out and gets into the other block.” — [lines 514-514](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000116`)

### Original context

**vasanth** · lines 514-514 · spoken_turn

> remember this point very carefully. Anything that get executed, even if it is not something that is not the JavaScript engine's capability, still it is something that goes to call stack at once and comes out and gets into the other block. Okay, always remember that. And uh I'll get into the queues now. I think again this queues concepts also most of us would know. Like there are uh quite a few names. I don't know like why there are so many different names for the queue. Like some call it micro task queue and macro task queue.

<a id="record-313c5fea4c61d26d"></a>
## Micro and Macro Task Queues

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- There are two types of queues referred to as the micro task queue and the macro task queue, despite not being officially defined as such in MDN documentation.
  - “there isn't mentioning of this macro task queue and micro task queue, at least the last time I read.” — [lines 518-518](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000117`)
  - “there are two queues that everybody popularly call it.” — [lines 518-518](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000117`)

### Original context

**vasanth** · lines 518-518 · spoken_turn

> But if you go and open the official definition of the MDN or the MDN document, there isn't mentioning of this macro task queue and micro task queue, at least the last time I read. But maybe because of the behavior of it, there are two queues that everybody popularly call it. One is a micro task queue and another one is a macro task queue. And all the images that you see in this document, I've given a credit to wherever I picked it from. Okay. So we have a macro task queue and micro task queue. All the things that are having the higher priority, we'll get into the micro task queue. All the things that have a relatively

**unknown speaker** · lines 522-522 · spoken_turn

> and

**vasanth** · lines 526-526 · spoken_turn

> lesser priority that go and sit in the macro task queue. Okay. Also as I told we have this web API section for providing us all the web related capabilities. Okay.

<a id="record-7062f1a756648b31"></a>
## Task Queue Explanation

**Product:** expression · **Type:** rhetorical_move · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- The explanation contrasts priorities by categorizing promises and async operations into higher priority tasks, placing them in the micro task queue, while others go into the macro task queue.
  - “promises are higher priority, so they get into the micro task queue. And uh and async await again a higher priority, similar to promise” — [lines 530-530](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000120`)
  - “if any any changes are happening and user is listening to such changes, so they all get you know micro task queue.” — [lines 538-538](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000122`)

### Purpose

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 530-530 · spoken_turn

> So what goes into micro task queue, what goes into macro task queue, okay? Few everybody would know that is promises are higher priority, so they get into the micro task queue. And uh and async await again a higher priority, similar to promise as we all know, that also gets into the micro task queue. And queue micro task, honestly this is something that I was also not knowing for until like I started preparing for this and I read about it. Queue micro task is nothing but like schedules a specified function to be executed as a micro task.

**vasanth** · lines 534-534 · spoken_turn

> Let's say you have a block of code and you want that to be like quickly executed. So you can read more about it. You get a simple simple uh snippet similar to set timeout. The syntax is very similar to set timeout. So you can keep a block of code there. So instead of going into macro task queue, those code will get into the micro task queue. You manually prioritizing uh by using this queue micro task. Another one is a mutation observer is a built in JavaScript observer where what certain changes are happening. Again you can get the lot of examples for mutation observer.

**vasanth** · lines 538-538 · spoken_turn

> So if any any changes are happening and user is listening to such changes, so they all get you know micro task queue. Maybe like network change, on end of the page reached, all of these are listeners, so they all have a micro task. The reason being, as you can definitely guess. So whenever such change happen, JavaScript may want to do something very immediately. So because of that, they are part of the micro task queue. Micro task queue are set timeout, set interval and DOM image, okay? Micro tasks are always executed before the macro task.
