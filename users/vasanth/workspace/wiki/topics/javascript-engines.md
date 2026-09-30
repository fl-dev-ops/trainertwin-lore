# javascript engines

> Source-local records, not independent fact verification. Original steps and qualifications are retained.

<a id="record-c5ed058613e2b6e4"></a>
## JavaScript Engines

**Product:** knowledge · **Type:** self_report · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- The V8 engine is considered the most popular JavaScript engine on the internet, used in both Chrome and the browser developed by OpenAI.
  - “the most popular engine on internet right now is V8.” — [lines 238-238](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000047`)

### Original context

**vasanth** · lines 234-234 · spoken_turn

> Okay, you're free to unmute and ask if at all there are any. Okay. Next, I'll go to the JavaScript engine. So JavaScript engine is basically responsible for executing the JavaScript code. The very popular engine I think most of you would know is V8. It's a Chrome browser's engine. There's a JavaScript core which is by Safari and there is a engine called Chakra which is a legacy browser which is used in Internet Explorer and all. Safari has, sorry, the Mozilla Firefox has its own version of the its own engine. Every browser almost has its own engine, but according to me the most

**vasanth** · lines 238-238 · spoken_turn

> popular engine on internet right now is V8. Even the recent the browser that Open AI built was built using the Chromium which again runs on the V8. Okay. As again most of you would know V8 is an engine that is written using the C++.

**vasanth** · lines 242-242 · spoken_turn

> Okay. uh If you look at it like it is more like a writing a compiler for executing a code. So JavaScript or the ECMAScript, right, they will propose some standards like whenever there is a variable created with var keyword, this is the way you need to treat it. Whenever there is a variable created with lang keyword, this is the way you need to treat it. Engines are nothing but compilers or a software that basically understand this these nuances or how this code need to be executed and they help you basically execute. So if you are really interested or if you have time, you can now you can build your own

<a id="record-858ed76ce1b72a30"></a>
## JavaScript Engine Execution

**Product:** knowledge · **Type:** self_report · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- The call stack executes code in a last-in, first-out order, and if blocked, no further code can be executed.
  - “If the call stack is blocked, no further JavaScript code can execute.” — [lines 262-262](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000053`)

### Original context

**vasanth** · lines 262-262 · spoken_turn

> then we would end the execution. Okay? If you look at the execution flow, A is pushed onto the stack. B is pushed onto the stack, console log executes, function completes and pre finally popped out of the stack. If the call stack is blocked, no further JavaScript code can execute. This is very common sense. If stack is taking more time because let's say you have a for loop that is running for example one million times or two million times and the stack is stopped the call stack is blocked till that time and nothing executes. So main thread is busy. Correct? So if you look at this in overall

**vasanth** · lines 266-266 · spoken_turn

> structure as I told. JavaScript engine has memory heap, call stack, garbage collector, event loop. Regarding the these things like web API, event loop, these I'm gonna discuss in a while. Now, just now we discussed this part, okay? JavaScript engine has two parts, memory engine and call stack. These two things I suppose you guys are clear.

<a id="record-774deecb0a936b2f"></a>
## JavaScript Engine Components

**Product:** knowledge · **Type:** self_report · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- A JavaScript engine contains a memory heap and a call stack, with the latter managing the execution order of code.
  - “One is a memory heap, another one is a call stack.” — [lines 250-250](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000050`)
  - “Memory heap is basically as the very word says, is primarily used to store the variables.” — [lines 250-250](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000050`)
  - “the call stack. I suppose most of us would also definitely know what is a call stack. So this is basically where the JavaScript code get executed.” — [lines 254-254](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000051`)

### Original context

**vasanth** · lines 250-250 · spoken_turn

> only two parts. One is a memory heap, another one is a call stack. Okay? Memory heap is basically as the very word says, is primarily used to store the variables, like storing the variables, objects, functions, all of this basically happens in the memory heap. Okay? And next we have the call stack. I suppose most of us would also definitely know what is a call stack. So this is basically where the JavaScript code get executed. So as it's a stack, it's a last in first out, uh I'm putting but like we are having a plate, one one on top of another, whatever is in the last

**vasanth** · lines 254-254 · spoken_turn

> can be picked for same way whatever is the last part of code that get executed first. Okay. Only one piece of code get executed anytime in the call stack because it's a stack. You can pick only one plate on from the top. Correct? Same way the call stack also works. Okay. And I'll execute the call I'll explain the call stack and again I'll take a pause you could ask me any question if there in your mind. Okay. Next is the call stack execution. Correct? Suppose this also everybody would know. So now let's say this is a small block of code that I have written here. Function A I

**vasanth** · lines 258-258 · spoken_turn

> calling the A. So A is getting called function A. Function A is calling function B. Function B has a lock statement which is getting executed. Then if it is not returning anything by default it will return the void. And then we come to A. Again it is not returning anything by default we will return the void.

<a id="record-9c090dc3e9dd5603"></a>
## Build Your Own JavaScript Engine

**Product:** knowledge · **Type:** advice · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- It's manageable to build a basic JavaScript engine that parses and executes simple code examples, although it requires more effort to match the capability of established engines like V8.
  - “But to begin with if you want to just play around and build your own engine, you can certainly do it.” — [lines 246-246](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000049`)

### Original context

**vasanth** · lines 242-242 · spoken_turn

> Okay. uh If you look at it like it is more like a writing a compiler for executing a code. So JavaScript or the ECMAScript, right, they will propose some standards like whenever there is a variable created with var keyword, this is the way you need to treat it. Whenever there is a variable created with lang keyword, this is the way you need to treat it. Engines are nothing but compilers or a software that basically understand this these nuances or how this code need to be executed and they help you basically execute. So if you are really interested or if you have time, you can now you can build your own

**vasanth** · lines 246-246 · spoken_turn

> your own engine. You need not to be like should solve all the problems. You could take few basic examples like creating a function, creating a variable and you can write your own engine where the code is set to your engine and you can parse and you can output the result. It's quite easy now if you are using any Janaya tool right and you want to build your own engine, not that complicated. But to build something of as capable as V8 is difficult because it's an industry grade, they might have built it over a period of lot of time. But to begin with if you want to just play around and build your own engine, you can certainly do it. Okay? So engine also contains

<a id="record-a02fb0dea907861d"></a>
## Explanation of JavaScript Engine Components

**Product:** expression · **Type:** structure · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- The speaker explains JavaScript engine by dividing it into components such as memory heap and call stack.
  - “only two parts. One is a memory heap, another one is a call stack.” — [lines 250-250](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000050`)

### Purpose

- Clarifies the fundamental parts of a JavaScript engine to aid understanding.
  - “memory heap is primarily used to store the variables.” — [lines 250-250](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000050`)

### Original context

**vasanth** · lines 250-250 · spoken_turn

> only two parts. One is a memory heap, another one is a call stack. Okay? Memory heap is basically as the very word says, is primarily used to store the variables, like storing the variables, objects, functions, all of this basically happens in the memory heap. Okay? And next we have the call stack. I suppose most of us would also definitely know what is a call stack. So this is basically where the JavaScript code get executed. So as it's a stack, it's a last in first out, uh I'm putting but like we are having a plate, one one on top of another, whatever is in the last

<a id="record-3dd9a60e178130b8"></a>
## Understanding JavaScript Engines

**Product:** cases · **Type:** reported_exchange · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- vasanth addresses the role of JavaScript engines like V8, explaining its importance and ubiquity.
  - “JavaScript engine is basically responsible for executing the JavaScript code.” — [lines 234-234](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000046`)
  - “the most popular engine on internet right now is V8.” — [lines 238-238](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000047`)

### Cue

Not stated in the cited excerpt.

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

Not stated in the cited excerpt.

### Outcome

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 234-234 · spoken_turn

> Okay, you're free to unmute and ask if at all there are any. Okay. Next, I'll go to the JavaScript engine. So JavaScript engine is basically responsible for executing the JavaScript code. The very popular engine I think most of you would know is V8. It's a Chrome browser's engine. There's a JavaScript core which is by Safari and there is a engine called Chakra which is a legacy browser which is used in Internet Explorer and all. Safari has, sorry, the Mozilla Firefox has its own version of the its own engine. Every browser almost has its own engine, but according to me the most

**vasanth** · lines 238-238 · spoken_turn

> popular engine on internet right now is V8. Even the recent the browser that Open AI built was built using the Chromium which again runs on the V8. Okay. As again most of you would know V8 is an engine that is written using the C++.

**vasanth** · lines 242-242 · spoken_turn

> Okay. uh If you look at it like it is more like a writing a compiler for executing a code. So JavaScript or the ECMAScript, right, they will propose some standards like whenever there is a variable created with var keyword, this is the way you need to treat it. Whenever there is a variable created with lang keyword, this is the way you need to treat it. Engines are nothing but compilers or a software that basically understand this these nuances or how this code need to be executed and they help you basically execute. So if you are really interested or if you have time, you can now you can build your own

<a id="record-620aafe2963a28f9"></a>
## JavaScript Engine Function

**Product:** cases · **Type:** reported_exchange · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- vasanth discusses the components of JavaScript engines, focusing on memory heap and call stack.
  - “One is a memory heap, another one is a call stack.” — [lines 250-250](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000050`)
  - “So this is basically where the JavaScript code get executed.” — [lines 254-254](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000051`)

### Cue

Not stated in the cited excerpt.

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

Not stated in the cited excerpt.

### Outcome

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 250-250 · spoken_turn

> only two parts. One is a memory heap, another one is a call stack. Okay? Memory heap is basically as the very word says, is primarily used to store the variables, like storing the variables, objects, functions, all of this basically happens in the memory heap. Okay? And next we have the call stack. I suppose most of us would also definitely know what is a call stack. So this is basically where the JavaScript code get executed. So as it's a stack, it's a last in first out, uh I'm putting but like we are having a plate, one one on top of another, whatever is in the last

**vasanth** · lines 254-254 · spoken_turn

> can be picked for same way whatever is the last part of code that get executed first. Okay. Only one piece of code get executed anytime in the call stack because it's a stack. You can pick only one plate on from the top. Correct? Same way the call stack also works. Okay. And I'll execute the call I'll explain the call stack and again I'll take a pause you could ask me any question if there in your mind. Okay. Next is the call stack execution. Correct? Suppose this also everybody would know. So now let's say this is a small block of code that I have written here. Function A I

**vasanth** · lines 258-258 · spoken_turn

> calling the A. So A is getting called function A. Function A is calling function B. Function B has a lock statement which is getting executed. Then if it is not returning anything by default it will return the void. And then we come to A. Again it is not returning anything by default we will return the void.
