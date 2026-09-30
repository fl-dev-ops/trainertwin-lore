# javascript runtimes

> Source-local records, not independent fact verification. Original steps and qualifications are retained.

<a id="record-cb599989868d6240"></a>
## Algorithm Interval in Event Loop

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- The interval at which an event loop checks the call stack and queues can vary by environment and is specific to its implementation.
  - “what is the millisecond or microsecond with which it is gonna check is largely that browser or however the implementation dependent” — [lines 782-782](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000169`)

### Original context

**vasanth** · lines 782-782 · spoken_turn

> Good question, Soumya. Interval point of view as far I know, maybe I can double check. So event loop is a custom algorithm for different JavaScript environments. As I told, Chrome has a different event loop, Node.js has a different event loop, maybe Safari has a different event loop. And each of them have might have custom implementation of theirs. So what is the millisecond or microsecond with which it is gonna check is largely that browser or however the implementation dependent. Maybe we can check how much Chrome takes in general and you can remember that. But the delay is particularly a algorithm written for that particular execution anyway. Government Swami

<a id="record-3f40e8837e4d1b77"></a>
## Custom Event Loops by Environment

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Different JavaScript environments like Chrome and Node.js can have custom implementations of the event loop.
  - “event loop is a custom algorithm for different JavaScript environments. As I told, Chrome has a different event loop, Node.js has a different event loop” — [lines 782-782](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000169`)
  - “event loop: JavaScript has given implementation for the whoever wants to use the event loop implementation is kept open” — [lines 822-822](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000179`)

### Original context

**vasanth** · lines 782-782 · spoken_turn

> Good question, Soumya. Interval point of view as far I know, maybe I can double check. So event loop is a custom algorithm for different JavaScript environments. As I told, Chrome has a different event loop, Node.js has a different event loop, maybe Safari has a different event loop. And each of them have might have custom implementation of theirs. So what is the millisecond or microsecond with which it is gonna check is largely that browser or however the implementation dependent. Maybe we can check how much Chrome takes in general and you can remember that. But the delay is particularly a algorithm written for that particular execution anyway. Government Swami

**unknown speaker** · lines 786-786 · spoken_turn

> श्योर श्योर. थैंक यू सर.

**vasanth** · lines 790-790 · spoken_turn

> தேங்க்யூ சார். தேங்க்யூ. யா. யா முத்துராஜ் ப்ளீஸ்.

**vasanth** · lines 794-794 · spoken_turn

> S. R. K. Raj, I think your name is Muthuraj only. I am telling correct na?

**unknown speaker** · lines 798-798 · spoken_turn

> या करेक्ट करेक्ट

**vasanth** · lines 802-802 · spoken_turn

> at least

**vasanth** · lines 806-806 · spoken_turn

> Yes, you are audible Muthuraj, please tell me.

**unknown speaker** · lines 810-810 · spoken_turn

> Okay. Okay. So you have said the different browser have the different kind of event loop. But all the primary work is to listen the call stack heap and web APIs, right? Yes. So what is the other key differences here we can see? That is my first question. Then answer I can ask second question.

**vasanth** · lines 814-814 · spoken_turn

> Yes

**vasanth** · lines 818-818 · spoken_turn

> Sure. See, event loop like JavaScript has given implementation for the whoever wants to use the event loop implementation is kept open. The reason being, let's say Node.js don't have web APIs.

**vasanth** · lines 822-822 · spoken_turn

> correct? Like there is no concept of all the things that whatever browser is providing. Those things are not there. So I'm going to explain actually. There is one more section around like why event loop, uh why does JS engine do not include the event loop? I'll explain more. But in a nutshell if you have to see, the implementation is left to the different environments because however they want to implement, they can implement it.
