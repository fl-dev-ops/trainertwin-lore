# javascript execution

> Source-local records, not independent fact verification. Original steps and qualifications are retained.

<a id="record-2eada5993e4973a3"></a>
## Microtask and macrotask queues

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Microtasks have higher priority than macrotasks and are executed before them.
  - “micro tasks are always executed before the macro task.” — [lines 634-634](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000132`)

### Original context

**vasanth** · lines 634-634 · spoken_turn

> Okay. So macro task queue is a lower priority queue. Okay, contains set timeout, set interval, DOM events like click, mouse over, mouse up scroll, anything that is asyncing nature and of lesser priority, they'll be kept in the macro task queue. Okay. So macro task are always execute, micro tasks are always executed before the macro task. Okay. Now look at the event loop as a concept now. uh Okay, I'll explain event loop as a concept. Then I'll take a pause, we could collectively discuss everything that I explained so far. See many a times

**vasanth** · lines 638-638 · spoken_turn

> whenever people ask like what is event loop in interview right? we have a common way of explaining this call stack micro task queue micro task queue web APIs all of them collectively which is also not wrong. but you can also consider like the event loop is also

**vasanth** · lines 642-642 · spoken_turn

> just an algorithm actually. Okay, I'll explain more. So event loop continuously checks the call stack in queues. In very very simple words, event loop consider event loop is an algorithm that checks whether call stack is empty. If call stack is empty, what is the next item to be put into call stack for execution. Okay? So event loop as a concept of call stack, call back queue, micro task queue, web IPS, all of that is also a right explanation. Plus explaining event loop as an algorithm is also a right explanation. Okay? So

**vasanth** · lines 646-646 · spoken_turn

> Event loop is an algorithm that checks whether call stack and queues whether they have something to execute or not. It's going to continuously keep on checking and event loop is a property of the browser again. It's not a JavaScript engine, it's again one of the capability offered by the browser. Different different places where JavaScript engine JavaScript executes, they might have a different event loop implementation. For example, Node.js though it uses V8 engine, the event loop of Node.js is different, event loop of the Chrome algorithm is different. Event loop in simple words is an algorithm that

**vasanth** · lines 650-650 · spoken_turn

> whichever the browser or whichever the place where JavaScript is running however they want to implement their event group they are free to do it. Okay. Now what is execution order in general many people don't know this okay. So please listen to this carefully. So execution order call stack must be empty. Let's say first priority of executing the task is everything in the call stack get executed once after call stack is empty execute all micro tasks micro task means you already just now saw correct. Micro task means promises async await

**vasanth** · lines 654-654 · spoken_turn

> Q micro task, mutation observer, all of those will be executed. Followed by you execute one micro task. Only one micro task, okay? Execute call stack should be empty, that means everything in the call stack should be executed first. Followed by you execute one micro task. Followed by, sorry, followed by you execute all the micro task. Followed by you execute one macro task and you repeat the cycle. Okay, repeat the cycle means again you see call stack is empty, execute one all micro task, execute one micro task, macro

<a id="record-f152a0b5443b197c"></a>
## Web APIs in JavaScript

**Product:** knowledge · **Type:** belief · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Web APIs handle activities that are difficult for the JavaScript engine, like timers and other async events.
  - “Web APIs are basically used for handling the any activity that is difficult for JavaScript engine to handle all of those are basically offloaded into web APIs.” — [lines 534-534](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000107`)

### Original context

**vasanth** · lines 534-534 · spoken_turn

> that need to be kept like unless there is some T T L to expire it will be kept there forever. So all those things JavaScript engine cannot handle. So don't consider web APIs like primary responsible for taking care of the async events. Web APIs are basically used for handling the any activity that is difficult for JavaScript engine to handle all of those are basically ofloaded into web APIs. Okay? So I've written few of the capabilities as an example here. Like example also I've just wrote the set timer. So JavaScript registers a timer browser web APIs

**vasanth** · lines 538-538 · spoken_turn

> handles the timer. JavaScript continues running without waiting. So JavaScript do not worry whenever this timer continues. Okay? So now

<a id="record-cbfa295db64735e4"></a>
## Microtask Priority in Execution

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Microtasks are given higher priority than macrotasks after the call stack is empty.
  - “after the call stack is empty, highest priority is given to micro task.” — [lines 662-662](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000139`)
  - “micro task queue have higher priority than the macro task queue.” — [lines 678-678](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000143`)

### Original context

**vasanth** · lines 662-662 · spoken_turn

> call stack, the highest priority is given to micro task and uh some somehow the order should be adjusted. There is no logical explanation. Depending on the priority, after the call stack is empty, highest priority is given to micro task. So all the micro tasks will be executed, followed by the micro task, repeat the cycle, okay? I'll just explain this and then I'll take a pause, okay?

**unknown speaker** · lines 666-666 · spoken_turn

> Hmm

**vasanth** · lines 670-670 · spoken_turn

> just one minute, I'll just I'll just show this and I'll end and then I can take your question. The complete execution example. So we have console.log a very very popular interview question maybe two three year back. Now also people ask this question actually. There is a console.log a, then there is a set timeout, then there is a promise, then there is a console.log b. Okay? So as we all know console.log a is a sync event. So a will be printed on the screen. A is logged. Then set timeout comes. Set timeout callback is registered with web APIs. Third, there is a promise.resolve again

**vasanth** · lines 674-674 · spoken_turn

> promise callback is added into micro task queue. And then D will be printed. So after A, D will be printed. Then call stack becomes empty. And then micro task queue executes C because promise are having higher priority than set timeout. Then micro task queue executes B. So the output will be A, D, C and B. A, D, C and B. Okay? I'll repeat. So all the sync events will be executed first. Among the async events, the micro task queue is having a higher priority than

**vasanth** · lines 678-678 · spoken_turn

> the macro the micro task queue promise or micro task queue have higher priority than the macro task queue. So it will be printing A D C and followed by B. Now very very interesting I think you all know this. I think it was an interview question for four five years back. Even though set set term mode is set to zero duration the JavaScript processor considers like this is something that is async in nature. Set term mode is async in nature. So it will it will place it in the web APS. So anytime you need to execute that like this it it should not be executed sync. Only after the call stack is empty it's going to be executed.

<a id="record-65c17186d181a9cd"></a>
## Execution order in queues

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- The execution order involves clearing the call stack, executing all microtasks, followed by one macrotask, and then repeating the cycle.
  - “execute call stack should be empty, that means everything in the call stack should be executed first. Followed by you execute one micro task. Followed by, sorry, followed by you execute all the micro task. Followed by you execute one macro task and you repeat the cycle.” — [lines 654-654](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000137`)

### Original context

**vasanth** · lines 650-650 · spoken_turn

> whichever the browser or whichever the place where JavaScript is running however they want to implement their event group they are free to do it. Okay. Now what is execution order in general many people don't know this okay. So please listen to this carefully. So execution order call stack must be empty. Let's say first priority of executing the task is everything in the call stack get executed once after call stack is empty execute all micro tasks micro task means you already just now saw correct. Micro task means promises async await

**vasanth** · lines 654-654 · spoken_turn

> Q micro task, mutation observer, all of those will be executed. Followed by you execute one micro task. Only one micro task, okay? Execute call stack should be empty, that means everything in the call stack should be executed first. Followed by you execute one micro task. Followed by, sorry, followed by you execute all the micro task. Followed by you execute one macro task and you repeat the cycle. Okay, repeat the cycle means again you see call stack is empty, execute one all micro task, execute one micro task, macro

<a id="record-cdea3f3a7d761158"></a>
## Event loop variations

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Different JavaScript environments can have different implementations of the event loop, such as Node.js and Chrome.
  - “Different different places where JavaScript engine JavaScript executes, they might have a different event loop implementation. For example, Node.js though it uses V8 engine, the event loop of Node.js is different, event loop of the Chrome algorithm is different.” — [lines 646-646](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000135`)

### Original context

**vasanth** · lines 646-646 · spoken_turn

> Event loop is an algorithm that checks whether call stack and queues whether they have something to execute or not. It's going to continuously keep on checking and event loop is a property of the browser again. It's not a JavaScript engine, it's again one of the capability offered by the browser. Different different places where JavaScript engine JavaScript executes, they might have a different event loop implementation. For example, Node.js though it uses V8 engine, the event loop of Node.js is different, event loop of the Chrome algorithm is different. Event loop in simple words is an algorithm that

<a id="record-6d7744252ae891a8"></a>
## Execution Context and JavaScript

**Product:** knowledge · **Type:** self_report · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- In JavaScript, after a block is executed, the execution context may not wait for a setTimeout to complete.
  - “Once after this block is executed, it is going to be there until set amount executes or it will be removed. It will not wait for set amount to complete.” — [lines 1410-1410](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000326`)

### Original context

**vasanth** · lines 1394-1394 · spoken_turn

> I'll repeat the question. See, I am not, my Prashant, my question is not like the order of execution that I already explained, but I'm sure you guys are going to explain. My question is with respect to execution context. So you think like say his execution model will be there or will be removed?

**unknown speaker** · lines 1398-1398 · spoken_turn

> Sorry guys

**unknown speaker** · lines 1402-1402 · spoken_turn

> Mm-hmm

**unknown speaker** · lines 1406-1406 · spoken_turn

> Bye

**vasanth** · lines 1410-1410 · spoken_turn

> Once after this block is executed, it is going to be there until set amount executes or it will be removed. It will not wait for set amount to complete. What will happen?

**vasanth** · lines 1414-1414 · spoken_turn

> You can you can take

**unknown speaker** · lines 1418-1418 · spoken_turn

> I'm audible

**vasanth** · lines 1422-1422 · spoken_turn

> Yeah, Muthuraj, yeah, please go.

**unknown speaker** · lines 1426-1426 · spoken_turn

> Okay. Okay, so sorry my my time sorry my side is wrong. So the set time mode is already pushed to the macro task. So execute execution context will be the completed. So it will taking care by the event loop automatically after the time given time completed, it will execute based upon the whether the call stack is empty or not. Okay.

<a id="record-d5a3a803875aa527"></a>
## JavaScript event loop definition

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- The event loop is an algorithm that checks whether the call stack and queues have tasks to execute, and it is a property of the browser, not the JavaScript engine.
  - “So event loop as a concept of call stack, call back queue, micro task queue, web IPS, all of that is also a right explanation.” — [lines 642-642](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000134`)
  - “Event loop is an algorithm that checks whether call stack and queues whether they have something to execute or not.” — [lines 646-646](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000135`)

### Original context

**vasanth** · lines 642-642 · spoken_turn

> just an algorithm actually. Okay, I'll explain more. So event loop continuously checks the call stack in queues. In very very simple words, event loop consider event loop is an algorithm that checks whether call stack is empty. If call stack is empty, what is the next item to be put into call stack for execution. Okay? So event loop as a concept of call stack, call back queue, micro task queue, web IPS, all of that is also a right explanation. Plus explaining event loop as an algorithm is also a right explanation. Okay? So

**vasanth** · lines 646-646 · spoken_turn

> Event loop is an algorithm that checks whether call stack and queues whether they have something to execute or not. It's going to continuously keep on checking and event loop is a property of the browser again. It's not a JavaScript engine, it's again one of the capability offered by the browser. Different different places where JavaScript engine JavaScript executes, they might have a different event loop implementation. For example, Node.js though it uses V8 engine, the event loop of Node.js is different, event loop of the Chrome algorithm is different. Event loop in simple words is an algorithm that

<a id="record-20c1b6a17909c4f0"></a>
## JavaScript Event Loop Basics

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- The execution order in JavaScript involves ensuring that the call stack is empty, executing all microTasks, and then executing one macroTask, repeating the cycle.
  - “execution order call stack must be empty” — [lines 650-650](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000136`)
  - “execute call stack should be empty, that means everything in the call stack should be executed first. Followed by you execute one micro task. Followed by, sorry, followed by you execute all the micro task. Followed by you execute one macro task and you repeat the cycle.” — [lines 654-654](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000137`)

### Original context

**vasanth** · lines 650-650 · spoken_turn

> whichever the browser or whichever the place where JavaScript is running however they want to implement their event group they are free to do it. Okay. Now what is execution order in general many people don't know this okay. So please listen to this carefully. So execution order call stack must be empty. Let's say first priority of executing the task is everything in the call stack get executed once after call stack is empty execute all micro tasks micro task means you already just now saw correct. Micro task means promises async await

**vasanth** · lines 654-654 · spoken_turn

> Q micro task, mutation observer, all of those will be executed. Followed by you execute one micro task. Only one micro task, okay? Execute call stack should be empty, that means everything in the call stack should be executed first. Followed by you execute one micro task. Followed by, sorry, followed by you execute all the micro task. Followed by you execute one macro task and you repeat the cycle. Okay, repeat the cycle means again you see call stack is empty, execute one all micro task, execute one micro task, macro

<a id="record-fced09c70276e8a1"></a>
## Execution Example with JavaScript Code

**Product:** knowledge · **Type:** self_report · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Vasanth provided an example involving \`console.log\`, \`setTimeout\`, and \`promise\`. The output sequence demonstrated the priority of sync tasks followed by microtasks, and then macrotasks.
  - “there is a promise, then there is a console.log b” — [lines 670-670](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000141`)
  - “And then D will be printed.” — [lines 674-674](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000142`)

### Original context

**vasanth** · lines 670-670 · spoken_turn

> just one minute, I'll just I'll just show this and I'll end and then I can take your question. The complete execution example. So we have console.log a very very popular interview question maybe two three year back. Now also people ask this question actually. There is a console.log a, then there is a set timeout, then there is a promise, then there is a console.log b. Okay? So as we all know console.log a is a sync event. So a will be printed on the screen. A is logged. Then set timeout comes. Set timeout callback is registered with web APIs. Third, there is a promise.resolve again

**vasanth** · lines 674-674 · spoken_turn

> promise callback is added into micro task queue. And then D will be printed. So after A, D will be printed. Then call stack becomes empty. And then micro task queue executes C because promise are having higher priority than set timeout. Then micro task queue executes B. So the output will be A, D, C and B. A, D, C and B. Okay? I'll repeat. So all the sync events will be executed first. Among the async events, the micro task queue is having a higher priority than

<a id="record-3498201e9bd4daa6"></a>
## Global Execution Context Persistence

**Product:** knowledge · **Type:** self_report · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- There is a discussion whether the global execution context will stay until the setTimeout runs or will be removed.
  - “Yeah, so global education context will stay even” — [lines 1470-1470](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000341`)
  - “global execution context will stay” — [lines 1518-1518](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000353`)
  - “I think it will be executed but the sec timeout will have its own variable context” — [lines 1530-1530](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000356`)

### Original context

**unknown speaker** · lines 1470-1470 · spoken_turn

> Yeah, so global education context will stay even

**vasanth** · lines 1474-1474 · spoken_turn

> you you're saying global execution context is gonna stay until the set amount comes back. Okay. Superior what do you think?

**unknown speaker** · lines 1478-1478 · spoken_turn

> Yeah

**unknown speaker** · lines 1482-1482 · spoken_turn

> So

**vasanth** · lines 1486-1486 · spoken_turn

> Supriyo, am I audible?

**unknown speaker** · lines 1490-1490 · spoken_turn

> Yeah

**vasanth** · lines 1494-1494 · spoken_turn

> What do you think? Global exhibition contest is going to stay until the exhibition happens or global exhibition contest will also be removed?

**unknown speaker** · lines 1498-1498 · spoken_turn

> you think

**unknown speaker** · lines 1502-1502 · spoken_turn

> No, it will stay.

**vasanth** · lines 1506-1506 · spoken_turn

> it will stay okay. And

**vasanth** · lines 1510-1510 · spoken_turn

> Vineet, what do you think?

**vasanth** · lines 1514-1514 · spoken_turn

> maybe we need having audio issues. Rameshree, what do you think?

**unknown speaker** · lines 1518-1518 · spoken_turn

> global execution context will stay

**vasanth** · lines 1522-1522 · spoken_turn

> It will stay, okay? Sure. Mahesh, what do you think?

**vasanth** · lines 1526-1526 · spoken_turn

> Mahesh could be very polite. I have spoken to him giving screening. Mahesh is Mahesh thinks before speaking whether should I speak or not. Okay. Please tell me Mahesh what will happen in global exam context.

**unknown speaker** · lines 1530-1530 · spoken_turn

> not sure I think it will be executed but the sec timeout will have its own variable context like y and x it will get from there.

<a id="record-3ebf69e29ae0f9d4"></a>
## JavaScript engine limitations

**Product:** knowledge · **Type:** belief · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- The JavaScript engine is responsible for executing code and cannot handle activities beyond execution, such as storing variables for a long period.
  - “if it is sync in nature, why can't JavaScript handle it by itself? Why it's giving that to the web APS? If you think like JavaScript engine in a nutshell is something that is responsible for executing the code” — [lines 530-530](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000106`)

### Original context

**vasanth** · lines 530-530 · spoken_turn

> synchronous in nature. There are many things actually which are sync in nature, not just the local storage. I'm just taking example of local storage. So if it is sync in nature, why can't JavaScript handle it by itself? Why it's giving that to the web APS? If you think like JavaScript engine in a nutshell is something that is responsible for executing the code, very very simple. So anything beyond execution is is is something that JavaScript engine cannot handle. I'll tell you why. So now local storage is something that where you have to store the variable for a while and like whenever you were trying to execute

**vasanth** · lines 534-534 · spoken_turn

> that need to be kept like unless there is some T T L to expire it will be kept there forever. So all those things JavaScript engine cannot handle. So don't consider web APIs like primary responsible for taking care of the async events. Web APIs are basically used for handling the any activity that is difficult for JavaScript engine to handle all of those are basically ofloaded into web APIs. Okay? So I've written few of the capabilities as an example here. Like example also I've just wrote the set timer. So JavaScript registers a timer browser web APIs

<a id="record-91189250f6ca220a"></a>
## Execution Context Popped from Call Stack

**Product:** knowledge · **Type:** self_report · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- The execution context will be popped out of the call stack, and once the call stack is empty, the callback's execution context is created and executed.
  - “and once the call stack is empty, this call backs execution context is created and executed.” — [lines 1446-1446](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000335`)

### Original context

**unknown speaker** · lines 1426-1426 · spoken_turn

> Okay. Okay, so sorry my my time sorry my side is wrong. So the set time mode is already pushed to the macro task. So execute execution context will be the completed. So it will taking care by the event loop automatically after the time given time completed, it will execute based upon the whether the call stack is empty or not. Okay.

**vasanth** · lines 1430-1430 · spoken_turn

> ओके. थँक्यू मुताराज. प्रणीता, योर आंसर.

**unknown speaker** · lines 1434-1434 · spoken_turn

> Yeah

**unknown speaker** · lines 1438-1438 · spoken_turn

> say hi execution context will be popped out of call stack. Once it locks hi, then after that when timer completes that set time of callbacks will be taken into macro task queue.

**unknown speaker** · lines 1442-1442 · spoken_turn

> Okay

**unknown speaker** · lines 1446-1446 · spoken_turn

> and once the call stack is empty, this call backs execution context is created and executed.

<a id="record-a87c17ad1739fb41"></a>
## Explanation of event loop

**Product:** expression · **Type:** rhetorical_move · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- The speaker explains the concept of the event loop in JavaScript as both a collection of components \(call stack, microtask queue, macrotask queue, web APIs\) and an algorithm checking for tasks to execute.
  - “Plus explaining event loop as an algorithm is also a right explanation.” — [lines 642-642](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000134`)

### Purpose

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 638-638 · spoken_turn

> whenever people ask like what is event loop in interview right? we have a common way of explaining this call stack micro task queue micro task queue web APIs all of them collectively which is also not wrong. but you can also consider like the event loop is also

**vasanth** · lines 642-642 · spoken_turn

> just an algorithm actually. Okay, I'll explain more. So event loop continuously checks the call stack in queues. In very very simple words, event loop consider event loop is an algorithm that checks whether call stack is empty. If call stack is empty, what is the next item to be put into call stack for execution. Okay? So event loop as a concept of call stack, call back queue, micro task queue, web IPS, all of that is also a right explanation. Plus explaining event loop as an algorithm is also a right explanation. Okay? So

**vasanth** · lines 646-646 · spoken_turn

> Event loop is an algorithm that checks whether call stack and queues whether they have something to execute or not. It's going to continuously keep on checking and event loop is a property of the browser again. It's not a JavaScript engine, it's again one of the capability offered by the browser. Different different places where JavaScript engine JavaScript executes, they might have a different event loop implementation. For example, Node.js though it uses V8 engine, the event loop of Node.js is different, event loop of the Chrome algorithm is different. Event loop in simple words is an algorithm that

<a id="record-9aa6d2e6b9c16914"></a>
## Question Format

**Product:** expression · **Type:** structure · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- The speaker repeats the question to engage the audience during a discussion about execution contexts.
  - “I'll repeat the question okay now I'll call some of the people in the call randomly so that everybody is active in the call.” — [lines 1466-1466](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000340`)

### Purpose

- To ensure active participation of the audience.
  - “I'll call some of the people in the call randomly so that everybody is active in the call.” — [lines 1466-1466](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000340`)

### Original context

**vasanth** · lines 1466-1466 · spoken_turn

> say hi has created a function execution context FEC and it will be removed it is not going to wait for set timeout to come back whenever set timeout comes back it's going to create its own execution context and it will execute but what happens to the global execution context will it stay until the set timeout comes back or it will be also removed. Pranita is a new hand raise or last name whatever you raise that hand only okay sure thank you. So I'll repeat the question okay now I'll call some of the people in the call randomly so that everybody is active in the call. ओके. सो मनीष कुमार, यू गॉट माय क्वेश्चन व्हाट आई एम सेइंग.

<a id="record-6822fa5f34561aad"></a>
## Explaining Execution Order

**Product:** expression · **Type:** structure · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- Vasanth uses a step-by-step explanation to describe the execution order in JavaScript, starting from the call stack to microtasks and then macrotasks, repeating the cycle.
  - “execute call stack should be empty, that means everything in the call stack should be executed first.” — [lines 654-654](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000137`)

### Purpose

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 650-650 · spoken_turn

> whichever the browser or whichever the place where JavaScript is running however they want to implement their event group they are free to do it. Okay. Now what is execution order in general many people don't know this okay. So please listen to this carefully. So execution order call stack must be empty. Let's say first priority of executing the task is everything in the call stack get executed once after call stack is empty execute all micro tasks micro task means you already just now saw correct. Micro task means promises async await

**vasanth** · lines 654-654 · spoken_turn

> Q micro task, mutation observer, all of those will be executed. Followed by you execute one micro task. Only one micro task, okay? Execute call stack should be empty, that means everything in the call stack should be executed first. Followed by you execute one micro task. Followed by, sorry, followed by you execute all the micro task. Followed by you execute one macro task and you repeat the cycle. Okay, repeat the cycle means again you see call stack is empty, execute one all micro task, execute one micro task, macro

**vasanth** · lines 658-658 · spoken_turn

> task, go back. You're going to continuously keep on doing this. So, we might ask that there there's a question comes, why not like execute all macro task at once? It's similar to how macro task work, right? The simplest explanation is like see call stack is kept for the sync events or you can consider something that is of priority. More priority events are kept at call stack. So if you end up processing everything from the macro task queue, then something priority comes into call stack, you will not have you will not be able to process it. Now again comes the question if that is the case like then why execute all from macro task? So after

**vasanth** · lines 662-662 · spoken_turn

> call stack, the highest priority is given to micro task and uh some somehow the order should be adjusted. There is no logical explanation. Depending on the priority, after the call stack is empty, highest priority is given to micro task. So all the micro tasks will be executed, followed by the micro task, repeat the cycle, okay? I'll just explain this and then I'll take a pause, okay?

<a id="record-9c97339a5c45fc09"></a>
## Execution Example

**Product:** expression · **Type:** structure · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- Provides a sequence of commands with expected outputs to demonstrate how JavaScript execution order affects console outputs.
  - “console.log a, then there is a set timeout, then there is a promise, then there is a console.log b.” — [lines 670-670](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000141`)

### Purpose

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 670-670 · spoken_turn

> just one minute, I'll just I'll just show this and I'll end and then I can take your question. The complete execution example. So we have console.log a very very popular interview question maybe two three year back. Now also people ask this question actually. There is a console.log a, then there is a set timeout, then there is a promise, then there is a console.log b. Okay? So as we all know console.log a is a sync event. So a will be printed on the screen. A is logged. Then set timeout comes. Set timeout callback is registered with web APIs. Third, there is a promise.resolve again

**vasanth** · lines 674-674 · spoken_turn

> promise callback is added into micro task queue. And then D will be printed. So after A, D will be printed. Then call stack becomes empty. And then micro task queue executes C because promise are having higher priority than set timeout. Then micro task queue executes B. So the output will be A, D, C and B. A, D, C and B. Okay? I'll repeat. So all the sync events will be executed first. Among the async events, the micro task queue is having a higher priority than

<a id="record-c4dd01250c30f421"></a>
## Priority Explanation

**Product:** expression · **Type:** rhetorical_move · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- Vasanth highlights the concept of priority by explaining why microtasks have higher priority than macrotasks in the execution cycle.
  - “the highest priority is given to micro task.” — [lines 662-662](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000139`)

### Purpose

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 662-662 · spoken_turn

> call stack, the highest priority is given to micro task and uh some somehow the order should be adjusted. There is no logical explanation. Depending on the priority, after the call stack is empty, highest priority is given to micro task. So all the micro tasks will be executed, followed by the micro task, repeat the cycle, okay? I'll just explain this and then I'll take a pause, okay?

**unknown speaker** · lines 666-666 · spoken_turn

> Hmm

**vasanth** · lines 670-670 · spoken_turn

> just one minute, I'll just I'll just show this and I'll end and then I can take your question. The complete execution example. So we have console.log a very very popular interview question maybe two three year back. Now also people ask this question actually. There is a console.log a, then there is a set timeout, then there is a promise, then there is a console.log b. Okay? So as we all know console.log a is a sync event. So a will be printed on the screen. A is logged. Then set timeout comes. Set timeout callback is registered with web APIs. Third, there is a promise.resolve again

**vasanth** · lines 674-674 · spoken_turn

> promise callback is added into micro task queue. And then D will be printed. So after A, D will be printed. Then call stack becomes empty. And then micro task queue executes C because promise are having higher priority than set timeout. Then micro task queue executes B. So the output will be A, D, C and B. A, D, C and B. Okay? I'll repeat. So all the sync events will be executed first. Among the async events, the micro task queue is having a higher priority than

**vasanth** · lines 678-678 · spoken_turn

> the macro the micro task queue promise or micro task queue have higher priority than the macro task queue. So it will be printing A D C and followed by B. Now very very interesting I think you all know this. I think it was an interview question for four five years back. Even though set set term mode is set to zero duration the JavaScript processor considers like this is something that is async in nature. Set term mode is async in nature. So it will it will place it in the web APS. So anytime you need to execute that like this it it should not be executed sync. Only after the call stack is empty it's going to be executed.

<a id="record-d89f9faaf1156484"></a>
## Microtask Queue Execution

**Product:** cases · **Type:** recorded_exchange · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- Soumya asks how microtask queue execution is handled when multiple tasks are involved.
  - “So say you have ten of those. So all ten of those would be like transferred to the call stack in the same order.” — [lines 726-726](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000155`)

### Cue

- say you have ten of those. So all ten of those would be like transferred to the call stack in the same order
  - “say you have ten of those. So all ten of those would be like transferred to the call stack in the same order” — [lines 726-726](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000155`)

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

- Event loop checks how many tasks are present within a period and moves them in the same order.
  - “What Event-to does is it checks in this in this particular period how many of them are there and it'll move all of them to call stack in the same order.” — [lines 750-750](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000161`)

### Outcome

Not stated in the cited excerpt.

### Original context

**unknown speaker** · lines 726-726 · spoken_turn

> Yeah, so I read out like you talked about that for micro task queue, like all of the like say, say promise or like fetch calls, everything that is in the micro task queue would get be, you know, like transferred to the call stack at once. So say you have like multiple events, right? Like say promise, fetch and everything. So say you have ten of those. So all ten of those would be like transferred to the call stack in the same order.

**vasanth** · lines 730-730 · spoken_turn

> Pack

**vasanth** · lines 734-734 · spoken_turn

> from a

**vasanth** · lines 738-738 · spoken_turn

> all

**unknown speaker** · lines 742-742 · spoken_turn

> and then they would be executed one by one, right? And once the call stack is empty, then say if I have any other thing in the macro task queue, then that would be executed.

**vasanth** · lines 746-746 · spoken_turn

> Exactly

**vasanth** · lines 750-750 · spoken_turn

> agreed, Samya. Correct. So slightly a one level deep if you see, right? Event-to-also will maintain the concept of delay actually. See because there is let's say there are hundred things are running at once, right? So now when do you get to know like these many things are there in the micro task queue? You're getting my point, right? How many of them to move? By the time you move something else might come. Correct? So what Event-to does is it checks in this in this particular period how many of them are there and it'll move all of them to call stack in the same order. Okay? And get executed.

<a id="record-054f464aff57ad73"></a>
## Execution Order Example in JavaScript

**Product:** cases · **Type:** demonstration · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- Vasanth demonstrates the execution order of JavaScript using a simple code snippet involving \`console.log\`, \`setTimeout\`, and \`Promise.resolve\`.
  - “The complete execution example. So we have console.log a very very popular interview question maybe two three year back.” — [lines 670-670](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000141`)

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

**vasanth** · lines 670-670 · spoken_turn

> just one minute, I'll just I'll just show this and I'll end and then I can take your question. The complete execution example. So we have console.log a very very popular interview question maybe two three year back. Now also people ask this question actually. There is a console.log a, then there is a set timeout, then there is a promise, then there is a console.log b. Okay? So as we all know console.log a is a sync event. So a will be printed on the screen. A is logged. Then set timeout comes. Set timeout callback is registered with web APIs. Third, there is a promise.resolve again

**vasanth** · lines 674-674 · spoken_turn

> promise callback is added into micro task queue. And then D will be printed. So after A, D will be printed. Then call stack becomes empty. And then micro task queue executes C because promise are having higher priority than set timeout. Then micro task queue executes B. So the output will be A, D, C and B. A, D, C and B. Okay? I'll repeat. So all the sync events will be executed first. Among the async events, the micro task queue is having a higher priority than

**vasanth** · lines 678-678 · spoken_turn

> the macro the micro task queue promise or micro task queue have higher priority than the macro task queue. So it will be printing A D C and followed by B. Now very very interesting I think you all know this. I think it was an interview question for four five years back. Even though set set term mode is set to zero duration the JavaScript processor considers like this is something that is async in nature. Set term mode is async in nature. So it will it will place it in the web APS. So anytime you need to execute that like this it it should not be executed sync. Only after the call stack is empty it's going to be executed.

<a id="record-0be89f3c57051ce6"></a>
## Async Execution with setTimeout

**Product:** cases · **Type:** reported_exchange · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- A discussion about asynchronous function execution in JavaScript using setTimeout.
  - “the question is you have a function called say hi. Within the function there is a set timeout. The set timeout can take a lot of time to execute and there is a caller who has called this function.” — [lines 1290-1290](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000296`)

### Cue

- Will the say hi wait until the time is over and then returns to greetings or it will gonna do something else.
  - “Will the say hi wait until the time is over and then returns to greetings or it will gonna do something else.” — [lines 1290-1290](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000296`)

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

- fundamental says that until and unless the call stack is empty, nothing won't be pushed, right? So when so when the say hi is called, right? It sees an asynchronous uh code and it pushes to the micro task queue.
  - “fundamental says that until and unless the call stack is empty, nothing won't be pushed, right? So when so when the say hi is called, right? It sees an asynchronous uh code and it pushes to the micro task queue.” — [lines 1294-1294](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000297`)

### Outcome

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 1290-1290 · spoken_turn

> I can repeat the question for those who might have not understood. The question is you have a function called say hi. Within the function there is a set timeout. The set timeout can take a lot of time to execute and there is a caller who has called this function. Will the say hi wait until the time is over and then returns to greetings or it will gonna do something else. Okay please go ahead Shad your answer.

**unknown speaker** · lines 1294-1294 · spoken_turn

> fundamental says that until and unless the call stack is empty, nothing won't be pushed, right? So when so when the say hi is called, right? It sees an asynchronous uh code and it pushes to the micro task queue. uh sorry, micro task queue. And micro task queue checks for the main call stack if this is empty or not. Only once it is empty like

**vasanth** · lines 1298-1298 · spoken_turn

> so

**vasanth** · lines 1302-1302 · spoken_turn

> It's

**unknown speaker** · lines 1306-1306 · spoken_turn

> Sorry

**unknown speaker** · lines 1310-1310 · spoken_turn

> it will do further operations like console logging high and every other thing. and once the main call stack is empty it will push that that thing to the

**vasanth** · lines 1314-1314 · spoken_turn

> So now now you're saying like say hi will not wait until the set time mode is finished its execution. So when the rest of the other statements are executed say hi will be removed from the stack that's what you're saying sir.

**unknown speaker** · lines 1318-1318 · spoken_turn

> not say hi entirely once it is called like once greeting is called right? uh greeting should be printed and then say hi is called right? Correct. So say uh so say hi when it is called then it encounters an asynchronous part of code then it will push to the main call string. Sorry.

**vasanth** · lines 1322-1322 · spoken_turn

> Uh huh

**vasanth** · lines 1326-1326 · spoken_turn

> Correct

**vasanth** · lines 1330-1330 · spoken_turn

> My question is with respect to this stacks, right? I'm not asking the order of execution. So now with respect to items in the stack, how they actually get executed? Like, let's say now say hi, will it be removed before even set timeout is executed or will it be staying until the set timeout is executed? That's my question.

<a id="record-5c3c43f825f1f8d7"></a>
## Discussion on Call Stack Operation

**Product:** cases · **Type:** reported_exchange · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- A question was posed about when JavaScript functions are pushed to the call stack.
  - “just a small question that uh JavaScript pushes anything in the call stack only when uh the function is called right not it is when it is declared” — [lines 1206-1206](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000275`)

### Cue

- just a small question that uh JavaScript pushes anything in the call stack only when uh the function is called right not it is when it is declared
  - “just a small question that uh JavaScript pushes anything in the call stack only when uh the function is called right not it is when it is declared” — [lines 1206-1206](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000275`)

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

- correct
  - “correct” — [lines 1210-1210](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000276`)

### Outcome

Not stated in the cited excerpt.

### Original context

**unknown speaker** · lines 1206-1206 · spoken_turn

> just a small question that uh JavaScript pushes anything in the call stack only when uh the function is called right not it is when it is declared

**vasanth** · lines 1210-1210 · spoken_turn

> correct

**vasanth** · lines 1214-1214 · spoken_turn

> नो नो करेक्ट। ओनली व्हेन देयर इज अ रेफरेंस गेटिंग, दैट टाइम इट विल गेट गेटिंग एट एडेड साथ। करेक्ट।

**unknown speaker** · lines 1218-1218 · spoken_turn

> Okay

<a id="record-c7ac667c924a70dc"></a>
## Execution Context Handling of setTimeout

**Product:** cases · **Type:** reported_exchange · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- The speaker explains the execution of JavaScript with respect to execution context and how setTimeout affects it.
  - “My question is with respect to execution context.” — [lines 1394-1394](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000322`)

### Cue

- Will the execution context stay until setTimeout executes or will it be removed?
  - “Once after this block is executed, it is going to be there until set amount executes or it will be removed.” — [lines 1410-1410](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000326`)

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

- The setTimeout is already pushed to the macro task, and the execution context is completed. It is managed by the event loop.
  - “So execute execution context will be the completed. So it will taking care by the event loop automatically after the time given time completed.” — [lines 1426-1426](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000330`)

### Outcome

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 1394-1394 · spoken_turn

> I'll repeat the question. See, I am not, my Prashant, my question is not like the order of execution that I already explained, but I'm sure you guys are going to explain. My question is with respect to execution context. So you think like say his execution model will be there or will be removed?

**unknown speaker** · lines 1398-1398 · spoken_turn

> Sorry guys

**unknown speaker** · lines 1402-1402 · spoken_turn

> Mm-hmm

**unknown speaker** · lines 1406-1406 · spoken_turn

> Bye

**vasanth** · lines 1410-1410 · spoken_turn

> Once after this block is executed, it is going to be there until set amount executes or it will be removed. It will not wait for set amount to complete. What will happen?

**vasanth** · lines 1414-1414 · spoken_turn

> You can you can take

**unknown speaker** · lines 1418-1418 · spoken_turn

> I'm audible

**vasanth** · lines 1422-1422 · spoken_turn

> Yeah, Muthuraj, yeah, please go.

**unknown speaker** · lines 1426-1426 · spoken_turn

> Okay. Okay, so sorry my my time sorry my side is wrong. So the set time mode is already pushed to the macro task. So execute execution context will be the completed. So it will taking care by the event loop automatically after the time given time completed, it will execute based upon the whether the call stack is empty or not. Okay.

<a id="record-4c79eeba189c5021"></a>
## Execution Context and Memory Allocation

**Product:** cases · **Type:** reported_exchange · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- The speaker was asked about reasons for the creation of execution context in JavaScript.
  - “Yeah, so I was just thinking that, you know, why do we even need an execution context in the first place?” — [lines 1238-1238](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000283`)

### Cue

- Yeah, so I was just thinking that, you know, why do we even need an execution context in the first place?
  - “Yeah, so I was just thinking that, you know, why do we even need an execution context in the first place?” — [lines 1238-1238](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000283`)

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

- Yes, Soumya. So primary reason is that only. Like, unlike languages like Java or C++ where it is not compiled many a times. So we are trying to allocate memory during the runtime. So that's the primary reason why execution context is is there, Soumya.
  - “Yes, Soumya. So primary reason is that only. Like, unlike languages like Java or C++ where it is not compiled many a times. So we are trying to allocate memory during the runtime. So that's the primary reason why execution context is is there, Soumya.” — [lines 1258-1258](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000288`)

### Outcome

Not stated in the cited excerpt.

### Original context

**unknown speaker** · lines 1238-1238 · spoken_turn

> Yeah, so I was just thinking that, you know, why do we even need an execution context in the first place? So, one reason that I could think of is the memory thing that you talked about, right? That like before executing any piece of code, there's a memory creation phase where you kind of check that if you have enough memory or not. So, apart from that, is there any other reason like why execution context is specifically created?

**vasanth** · lines 1242-1242 · spoken_turn

> okay

**vasanth** · lines 1246-1246 · spoken_turn

> Correct

**vasanth** · lines 1250-1250 · spoken_turn

> uh that

**vasanth** · lines 1254-1254 · spoken_turn

> you

**vasanth** · lines 1258-1258 · spoken_turn

> Yes, Soumya. So primary reason is that only. Like, unlike languages like Java or C++ where it is not compiled many a times. So we are trying to allocate memory during the runtime. So that's the primary reason why execution context is is there, Soumya. Yeah.

**unknown speaker** · lines 1262-1262 · spoken_turn

> ओके, थैंक यू।

<a id="record-1d7c2073d1593e03"></a>
## Global Execution Context during setTimeout

**Product:** cases · **Type:** reported_exchange · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- There is a discussion about whether the global execution context will persist during the execution of setTimeout.
  - “you you're saying global execution context is gonna stay until the set amount comes back.” — [lines 1470-1470](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000341`)

### Cue

- Will the global execution context stay until setTimeout runs or be removed?
  - “but what happens to the global execution context will it stay until the set timeout comes back or it will be also removed.” — [lines 1466-1466](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000340`)

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

- Most responses indicate that the global execution context will stay.
  - “global execution context will stay” — [lines 1518-1518](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000353`)
  - “I think it will be executed but the sec timeout will have its own variable context” — [lines 1530-1530](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000356`)

### Outcome

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 1466-1466 · spoken_turn

> say hi has created a function execution context FEC and it will be removed it is not going to wait for set timeout to come back whenever set timeout comes back it's going to create its own execution context and it will execute but what happens to the global execution context will it stay until the set timeout comes back or it will be also removed. Pranita is a new hand raise or last name whatever you raise that hand only okay sure thank you. So I'll repeat the question okay now I'll call some of the people in the call randomly so that everybody is active in the call. ओके. सो मनीष कुमार, यू गॉट माय क्वेश्चन व्हाट आई एम सेइंग.

**unknown speaker** · lines 1470-1470 · spoken_turn

> Yeah, so global education context will stay even

**vasanth** · lines 1474-1474 · spoken_turn

> you you're saying global execution context is gonna stay until the set amount comes back. Okay. Superior what do you think?

**unknown speaker** · lines 1478-1478 · spoken_turn

> Yeah

**unknown speaker** · lines 1482-1482 · spoken_turn

> So

**vasanth** · lines 1486-1486 · spoken_turn

> Supriyo, am I audible?

**unknown speaker** · lines 1490-1490 · spoken_turn

> Yeah

**vasanth** · lines 1494-1494 · spoken_turn

> What do you think? Global exhibition contest is going to stay until the exhibition happens or global exhibition contest will also be removed?

**unknown speaker** · lines 1498-1498 · spoken_turn

> you think

**unknown speaker** · lines 1502-1502 · spoken_turn

> No, it will stay.

**vasanth** · lines 1506-1506 · spoken_turn

> it will stay okay. And

**vasanth** · lines 1510-1510 · spoken_turn

> Vineet, what do you think?

**vasanth** · lines 1514-1514 · spoken_turn

> maybe we need having audio issues. Rameshree, what do you think?

**unknown speaker** · lines 1518-1518 · spoken_turn

> global execution context will stay

**vasanth** · lines 1522-1522 · spoken_turn

> It will stay, okay? Sure. Mahesh, what do you think?

**vasanth** · lines 1526-1526 · spoken_turn

> Mahesh could be very polite. I have spoken to him giving screening. Mahesh is Mahesh thinks before speaking whether should I speak or not. Okay. Please tell me Mahesh what will happen in global exam context.

**unknown speaker** · lines 1530-1530 · spoken_turn

> not sure I think it will be executed but the sec timeout will have its own variable context like y and x it will get from there.

**vasanth** · lines 1534-1534 · spoken_turn

> Okay. Sure. Divya, you have something to say?

**unknown speaker** · lines 1538-1538 · spoken_turn

> I think it will stay global.

**vasanth** · lines 1542-1542 · spoken_turn

> Okay. Shrisha, what do you think?

**unknown speaker** · lines 1546-1546 · spoken_turn

> I also think it will stay.

**vasanth** · lines 1550-1550 · spoken_turn

> Okay, anybody thinks it doesn't stay? You can raise your hand.

**unknown speaker** · lines 1554-1554 · spoken_turn

> Hello

**unknown speaker** · lines 1558-1558 · spoken_turn

> not available

**vasanth** · lines 1562-1562 · spoken_turn

> Yeah Shivam, please

**unknown speaker** · lines 1566-1566 · spoken_turn

> Yeah, I think it won't stay because the only reason the set timeout will run is when the call stack is empty. So I think that's one of the reasons.

**vasanth** · lines 1570-1570 · spoken_turn

> Hmm

<a id="record-06f10559610dc848"></a>
## Use of Defer in JavaScript Execution

**Product:** cases · **Type:** reported_exchange · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- A participant questions how the defer attribute in HTML correlates with the JavaScript event loop and call stack.
  - “we have the defer which we'll be using for HTML. And how does it correlate with you know the event loop and the call stack?” — [lines 1878-1878](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000443`)

### Cue

Not stated in the cited excerpt.

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

- The speaker explains that defer postpones downloading, but execution depends on browser operations and the JavaScript engine's responsibilities.
  - “whenever you're having a defer, like you are gonna basically postpone the downloadment of certain things. Correct. So what in in nutshell, whatever that you would see in the event loop concept or the JavaScript engine, anything that is loaded and available for execution, its responsibility to only to execute it.” — [lines 1882-1882](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000444`)

### Outcome

Not stated in the cited excerpt.

### Original context

**unknown speaker** · lines 1878-1878 · spoken_turn

> So like we have the defer which we'll be using for HTML. And how does it correlate with you know the event loop and the call stack?

**vasanth** · lines 1882-1882 · spoken_turn

> Okay, you're saying like whenever you're having a defer, like you are gonna basically postpone the downloadment of certain things. Correct. So what in in nutshell, whatever that you would see in the event loop concept or the JavaScript engine, anything that is loaded and available for execution, its responsibility to only to execute it. And however the codes are getting downloaded, that is purely the way you coded plus the browser capability, like browser however it want to download, right? So it's something that is browser doing. Consider browser is actually doing lot of things. See,

**unknown speaker** · lines 1886-1886 · spoken_turn

> Okay

**unknown speaker** · lines 1890-1890 · spoken_turn

> Correct

**vasanth** · lines 1894-1894 · spoken_turn

> We are calling the JavaScript engine, we are calling the event loop, and lot of other things. Browser is a combination of all of them. Browser is only offering them very explicitly. Okay? But JavaScript engine's responsibility to only execute the code that is ready to execute server.

<a id="record-5262753010aa4fcc"></a>
## JavaScript Compilation vs Interpretation

**Product:** knowledge · **Type:** self_report · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- JavaScript may be interpreted or compiled depending on the engine, as modern engines like V8 compile the code to detect issues early.
  - “JavaScript, if engines want them to be interpreted, it can be interpreted. If engines want them to be compiled, they can be compiled.” — [lines 330-330](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000070`)
  - “they all actually compile your code. So because of which if there are any issues or something they'll be like able to detect earlier only.” — [lines 338-338](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000072`)

### Original context

**vasanth** · lines 318-318 · spoken_turn

> who is asking now? Abhijit, Abhijit. Abhijit, yeah. So there are like quite a few different ways to look at it. As I told JavaScript uh is not by default from the definition point of view it is neither interpreted nor compiled. There used to be a definition which I saw on MDN very long back which said said it was interpreted. Now they don't officially say it is an interpreted sort of a language. So it all depends on how engine want to process the language. Like if you see like modern whenever you're coding now VS code or any other engines, right? If you create if you try to create

**unknown speaker** · lines 322-322 · spoken_turn

> Abhijit Abhijit

**vasanth** · lines 326-326 · spoken_turn

> variable and don't use try to use it before that we get warnings now. On that way, uh like now the engines or the whatever the IDs that are being, they are quite brilliant. So JavaScript right now depends on how engine is executing them. So it is very difficult to call an interpretation. The reason being, uh there is two phase of execution as you all know, one is a memory allocation phase, another one is a actual execution. So if something that executed like this, then certainly it is not getting interpreted. But what I think there could

**vasanth** · lines 330-330 · spoken_turn

> certain engines where if they want to make a JavaScript as an interpreted language, it's possible to do that. Some languages cannot be interpreted at all. For example, languages like C or C++. Those are always compiled languages. JavaScript, if engines want them to be interpreted, it can be interpreted. If engines want them to be compiled, they can be compiled. So these engines are written in the pursuit of the product. Like for example, V8 which is a Chrome's engine, whatever is best required for them or however they want to use the language, that's the way they are executing it or using it.

**unknown speaker** · lines 334-334 · spoken_turn

> So is it different in different different engines or the same structure or behavior? Today yeah all the model

**vasanth** · lines 338-338 · spoken_turn

> today yeah all the modern modern engines that I gave above like B8, Chakra and other engines they are they all actually compile your code. So because of which if there are any issues or something they'll be like able to detect earlier only. So they no there's no line by like execution happening here.

<a id="record-980da6432d7a3d21"></a>
## JavaScript Compilation and Execution

**Product:** cases · **Type:** reported_exchange · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- vasanth discusses how JavaScript execution can be interpreted or compiled based on what is best for the engine, highlighting that modern engines compile to detect issues earlier.
  - “JavaScript, if engines want them to be interpreted, it can be interpreted. If engines want them to be compiled, they can be compiled.” — [lines 330-330](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000070`)
  - “they all actually compile your code. So because of which if there are any issues or something they'll be like able to detect earlier only.” — [lines 338-338](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000072`)

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

**vasanth** · lines 318-318 · spoken_turn

> who is asking now? Abhijit, Abhijit. Abhijit, yeah. So there are like quite a few different ways to look at it. As I told JavaScript uh is not by default from the definition point of view it is neither interpreted nor compiled. There used to be a definition which I saw on MDN very long back which said said it was interpreted. Now they don't officially say it is an interpreted sort of a language. So it all depends on how engine want to process the language. Like if you see like modern whenever you're coding now VS code or any other engines, right? If you create if you try to create

**unknown speaker** · lines 322-322 · spoken_turn

> Abhijit Abhijit

**vasanth** · lines 326-326 · spoken_turn

> variable and don't use try to use it before that we get warnings now. On that way, uh like now the engines or the whatever the IDs that are being, they are quite brilliant. So JavaScript right now depends on how engine is executing them. So it is very difficult to call an interpretation. The reason being, uh there is two phase of execution as you all know, one is a memory allocation phase, another one is a actual execution. So if something that executed like this, then certainly it is not getting interpreted. But what I think there could

**vasanth** · lines 330-330 · spoken_turn

> certain engines where if they want to make a JavaScript as an interpreted language, it's possible to do that. Some languages cannot be interpreted at all. For example, languages like C or C++. Those are always compiled languages. JavaScript, if engines want them to be interpreted, it can be interpreted. If engines want them to be compiled, they can be compiled. So these engines are written in the pursuit of the product. Like for example, V8 which is a Chrome's engine, whatever is best required for them or however they want to use the language, that's the way they are executing it or using it.

**unknown speaker** · lines 334-334 · spoken_turn

> So is it different in different different engines or the same structure or behavior? Today yeah all the model

**vasanth** · lines 338-338 · spoken_turn

> today yeah all the modern modern engines that I gave above like B8, Chakra and other engines they are they all actually compile your code. So because of which if there are any issues or something they'll be like able to detect earlier only. So they no there's no line by like execution happening here.
