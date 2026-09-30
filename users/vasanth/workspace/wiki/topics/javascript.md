# javascript

> Source-local records, not independent fact verification. Original steps and qualifications are retained.

<a id="record-26a4944f8ab9ca19"></a>
## Global Execution Context

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- A new global execution context will be created even if the current one is removed from the stack, maintaining variable references.
  - “a new global execution context will also be created” — [lines 1678-1678](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000393`)

### Original context

**vasanth** · lines 1678-1678 · spoken_turn

> actually spin up a new execution context. In fact a new global execution context will also be created. Okay? So though the current global execution context is removed from the stack, still the references will be there. On that it will be creating a new global execution context, then execution context will be getting executed. Okay? Please remember this. So ninety nine percent of the interviews they don't ask this question. Okay? This much depth nobody will go. But I want you guys to know this quite well so that like whenever similar question asked you can show your proficiency in the interview.

**vasanth** · lines 1682-1682 · spoken_turn

> Okay. Now, I think set time out when I have explained this I explained about the global and local execution context. I'm just thinking anything I missed. I've added some of the interesting questions on this section called thought probing question.

<a id="record-cce9a266c77320a8"></a>
## Event loop and task queues

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- In JavaScript, the event loop decides execution order, and micro task queues have a higher priority than macro task queues.
  - “JavaScript executes code using a single call stack. Asynchronous operations are handled by browser with APS. Micro task queue have a higher priority than macro task queue. Event loop decides the execution order.” — [lines 990-990](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000221`)

### Original context

**vasanth** · lines 990-990 · spoken_turn

> So I'm going, I'm assuming everybody understood so far. I tried answering questions. I'm going to further, okay? And, yeah, key takeaways, JavaScript executes code using a single call stack. Asynchronous operations are handled by browser with APS. Micro task queue have a higher priority than macro task queue. Event loop decides the execution order. Set time out of zero doesn't mean immediate execution. Now, I'll tell you few of the things where people go wrong. Maybe I'll just quickly finish off these things. I think I'll not go over these differences. By now we have

<a id="record-28eb7bfd363c4ff7"></a>
## JavaScript runtime implementation

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- JavaScript does not put restrictions on how the runtime environment or the compiler should be implemented in different languages like Python, C++, or Java.
  - “There is one more section around like why event loop, uh why does JS engine do not include the event loop? I'll explain more. But in a nutshell if you have to see, the implementation is left to the different environments because however they want to implement, they can implement it.” — [lines 822-822](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000179`)
  - “Whether you write a compiler in Python, C++, Java, whichever the thing that you can write and make that to work faster or efficient up to you. JavaScript as a language or as a body it is not putting a restriction on that.” — [lines 834-834](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000182`)

### Original context

**vasanth** · lines 822-822 · spoken_turn

> correct? Like there is no concept of all the things that whatever browser is providing. Those things are not there. So I'm going to explain actually. There is one more section around like why event loop, uh why does JS engine do not include the event loop? I'll explain more. But in a nutshell if you have to see, the implementation is left to the different environments because however they want to implement, they can implement it.

**vasanth** · lines 826-826 · spoken_turn

> So what is the key difference? JavaScript is basically giving an option to everyone who is implementing. In fact, the compilers also if you see. The V8 and Chrome, V8 and Safari are not same compilers, right? At least with my experience like the websites load much fluent and better in Chrome compared to Safari. Even if you see the Open AI recently come with their browser, they are also using the Chromium which is an engine that is finally behind all the Chrome things, right? So the implementation like I have I have given you these are my rules. Like variable created with var keyword need to be hosted. This is my rules which is

**unknown speaker** · lines 830-830 · spoken_turn

> So

**vasanth** · lines 834-834 · spoken_turn

> script or JavaScript says. However you want to implement whether you write a compiler in Python, C++, Java, whichever the thing that you can write and make that to work faster or efficient up to you. JavaScript as a language or as a body it is not putting a restriction on that. Okay.

<a id="record-c00a74fc2638d13d"></a>
## Execution context and call stack

**Product:** knowledge · **Type:** advice · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- To understand execution, it's important to learn about execution contexts and call stacks which maintain chronological order during function calls.
  - “a statement like this will individually will not be put into the stack. There is an execution context that will be created and statements will be executed inside that.” — [lines 886-886](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000195`)
  - “there is a chronological order that we need to maintain, like how to which function should be popped when and the return value of that should be passed to which function.” — [lines 890-890](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000196`)

### Original context

**vasanth** · lines 886-886 · spoken_turn

> Very good. Yeah. This question also I ask in interviews. So it's good that you asked the same question to me. So if you observe, right, like to be honest, I'm going to explain more about execution context and other things. See, a statement like this will individually will not be put into the stack. There is an execution context that will be created and statements will be executed inside that. We'll learn more, okay? Now, answering your question, if everything coming here executing one after another, why do we need a stack? I explained that actually. Let's say there are multiple different functions, right, which you are calling one after another. uh I think somewhere I had that.

**vasanth** · lines 890-890 · spoken_turn

> like for example, A calling B, B calling C, right? Then what would happen is like the first whenever you are calling A, A is pushed onto the stack. You are calling A first, A is pushed onto the stack. Then B is pushed onto the stack, then console.log is executed. So there is a chronological order that we need to maintain, like how to which function should be popped when and the return value of that should be passed to which function. So there is an order required in terms of execution. And call stack is not actually property of just the the JavaScript itself. Almost all the programming

<a id="record-6bdce364c0588579"></a>
## JavaScript Variable Override

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- JavaScript will not override variables since overriding would disrupt program logic.
  - “it cannot override because override means then your whatever logic will be like ruined” — [lines 1798-1798](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000423`)

### Original context

**vasanth** · lines 1798-1798 · spoken_turn

> No, that like that it cannot execute. As I told you that like there is it cannot override because override means then your whatever logic you return pranam will be like will be like ruined. It will be like somebody else will be taking on that. Correct? Anand, you want to say anything?

<a id="record-613ef098ad39761d"></a>
## Call stack in programming languages

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Almost all programming languages use a stack-like structure to maintain execution order, similar to the JavaScript call stack.
  - “there is an order required in terms of execution. And call stack is not actually property of just the the JavaScript itself. Almost all the programming” — [lines 890-890](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000196`)
  - “language that we use has a equivalent property as that of the stack where execution order is maintained.” — [lines 894-894](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000197`)

### Original context

**vasanth** · lines 890-890 · spoken_turn

> like for example, A calling B, B calling C, right? Then what would happen is like the first whenever you are calling A, A is pushed onto the stack. You are calling A first, A is pushed onto the stack. Then B is pushed onto the stack, then console.log is executed. So there is a chronological order that we need to maintain, like how to which function should be popped when and the return value of that should be passed to which function. So there is an order required in terms of execution. And call stack is not actually property of just the the JavaScript itself. Almost all the programming

**vasanth** · lines 894-894 · spoken_turn

> language that we use has a equivalent property as that of the stack where execution order is maintained. That's the reason call stack is stack. Okay. Yes Sagar please go ahead.

<a id="record-4d3325105609e5b4"></a>
## JavaScript compiler creation

**Product:** knowledge · **Type:** advice · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- It's possible to create a lightweight JavaScript compiler using ECMAScript tools and write it in languages like Python, Rust, or any other.
  - “you can actually write a lightweight uh JavaScript compiler actually. You can just take the ECMAScript tools” — [lines 942-942](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000209`)
  - “you can try building a simple uh like JavaScript compiler. You can write in any language like Python, Rust or any language wherever you are comfortable and you can give a shot.” — [lines 950-950](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000211`)

### Original context

**vasanth** · lines 942-942 · spoken_turn

> actually it's a very interesting project. If anyone of you are interested, right, you can actually write a lightweight uh JavaScript compiler actually. You can just take the ECMAScript tools and if you have a paid subscription of Cloud or Gemini or these things, right, you can ask it to build a very basic version of the compiler where you can do many things. Like for example, we have let, var and const, right? And let's say you want to manipulate them and want them to behave in slightly different way. You can actually make it like you you can call it like your own version of the JavaScript. It is possible. If anybody has time with help of Jane, without Jane it would have been very very easy.

**unknown speaker** · lines 946-946 · spoken_turn

> hmm

**vasanth** · lines 950-950 · spoken_turn

> which definitely you can try building a simple uh like JavaScript compiler. You can write in any language like Python, Rust or any language wherever you are comfortable and you can give a shot. Where you can make let's say functions are hoisted in nature, right? What if you want in your JavaScript functions are not hoisted? The person should be calling the functions only after they are declared. So, maybe practicality law of no use, but you can just explore how to write a compiler. Okay?

<a id="record-0967c5bfef7f9f46"></a>
## Logical separation of files

**Product:** knowledge · **Type:** self_report · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Logical separation of JavaScript files like one.js, two.js is only for human understanding and not used by browsers for execution.
  - “files are something a logical separation for human to understand, like one dot js, two dot js to ten dot js, right? So whatever the files that you are seeing logically, it need not to be the way the browser sees it.” — [lines 858-858](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000188`)
  - “logical separation of the file is only for human to understand, not for the browsers.” — [lines 862-862](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000189`)

### Original context

**vasanth** · lines 858-858 · spoken_turn

> I'm going to explain more about the execution context where I'm going to go deep there, but I give you some simple analogy. See, files are something a logical separation for human to understand, like one dot js, two dot js to ten dot js, right? So whatever the files that you are seeing logically, it need not to be the way the browser sees it. So you can consider like one regime of work, one regime I mean like everything that is required to execute one web page many a times, I would not want to say all the time, many a times is just one big JavaScript dump for the browser.

**vasanth** · lines 862-862 · spoken_turn

> So whatever the logical separation that you think you have according as per the files, that are not a logical separation for the browser to execute. Okay, but there will be at times where there is more than one global I'm going to explain more about global execution model where one more than one can exist. But in simple words to conclude, logical separation of the file is only for human to understand, not for the browsers. Okay.

<a id="record-e4026a4c209b58bf"></a>
## Closure and Execution Context

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Set Timeout and promises form a closure and maintain references to variables even after the global execution context is removed.
  - “they form a closure” — [lines 1674-1674](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000392`)
  - “they will have reference to the variables” — [lines 1674-1674](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000392`)

### Original context

**vasanth** · lines 1674-1674 · spoken_turn

> whatever the set time amount which has gone to the macro task will come back. Now comes an interesting question. Wasn't like now globalization context is cleared. From where we are going to get a reference to these variables? Like y is equal to ten, x equal to ten etcetera, right? Because there is no execution context to have a reference to that. What happens is like the set time amount or promises they form a closure. And they will have reference to the variables. You all know closure. We are going to discuss more tomorrow also. So they will already have reference to the variable that they used. So whenever they come back to the stack, they're going to

**vasanth** · lines 1678-1678 · spoken_turn

> actually spin up a new execution context. In fact a new global execution context will also be created. Okay? So though the current global execution context is removed from the stack, still the references will be there. On that it will be creating a new global execution context, then execution context will be getting executed. Okay? Please remember this. So ninety nine percent of the interviews they don't ask this question. Okay? This much depth nobody will go. But I want you guys to know this quite well so that like whenever similar question asked you can show your proficiency in the interview.

<a id="record-0871a7d7d6db7e56"></a>
## Execution Context

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Set Timeout will not be processed until the call stack is empty due to the execution context constraint.
  - “until call stack is empty set timeout will not come here” — [lines 1670-1670](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000391`)
  - “as long as there's execution context then nothing comes to call stack” — [lines 1670-1670](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000391`)

### Original context

**vasanth** · lines 1670-1670 · spoken_turn

> Okay. Sure. I'll I'll quickly summarize. uh Actually global execution is not gonna stay. See, every whatever is in the stack as somebody clearly pointed out I think Shivam or Pranita told I think. So if you think right until call stack is empty set timeout will not come here. We already agreed that right? So if there what what do you mean by call stack is empty? There shouldn't be any execution context. So as long as there's execution context then nothing comes to call stack. Correct? So even the global execution context also removed and these also will be removed. Only then the stack is empty and

**vasanth** · lines 1674-1674 · spoken_turn

> whatever the set time amount which has gone to the macro task will come back. Now comes an interesting question. Wasn't like now globalization context is cleared. From where we are going to get a reference to these variables? Like y is equal to ten, x equal to ten etcetera, right? Because there is no execution context to have a reference to that. What happens is like the set time amount or promises they form a closure. And they will have reference to the variables. You all know closure. We are going to discuss more tomorrow also. So they will already have reference to the variable that they used. So whenever they come back to the stack, they're going to

**vasanth** · lines 1678-1678 · spoken_turn

> actually spin up a new execution context. In fact a new global execution context will also be created. Okay? So though the current global execution context is removed from the stack, still the references will be there. On that it will be creating a new global execution context, then execution context will be getting executed. Okay? Please remember this. So ninety nine percent of the interviews they don't ask this question. Okay? This much depth nobody will go. But I want you guys to know this quite well so that like whenever similar question asked you can show your proficiency in the interview.

<a id="record-757462cf12b284fc"></a>
## JavaScript flexibility

**Product:** expression · **Type:** rhetorical_move · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- Vasanth emphasizes the flexibility of implementing JavaScript runtime across different programming languages without restrictions.
  - “JavaScript says. However you want to implement whether you write a compiler in Python, C++, Java, whichever the thing that you can write and make that to work faster or efficient up to you.” — [lines 834-834](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000182`)

### Purpose

- To highlight the adaptability and lack of limitations in creating JavaScript compilers.
  - “JavaScript as a language or as a body it is not putting a restriction on that.” — [lines 834-834](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000182`)

### Original context

**vasanth** · lines 834-834 · spoken_turn

> script or JavaScript says. However you want to implement whether you write a compiler in Python, C++, Java, whichever the thing that you can write and make that to work faster or efficient up to you. JavaScript as a language or as a body it is not putting a restriction on that. Okay.

<a id="record-f0e9f9b6014c1e34"></a>
## Call stack discussion

**Product:** cases · **Type:** reported_exchange · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- A participant asked how calling a stack data structure relates to immediate task execution in JavaScript.
  - “But as you mentioned that any task that is put inside this stack is executed immediately.” — [lines 874-874](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000192`)

### Cue

- But as you mentioned that any task that is put inside this stack is executed immediately.
  - “But as you mentioned that any task that is put inside this stack is executed immediately.” — [lines 874-874](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000192`)

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

- JavaScript uses an execution context for tasks, and there is an execution order maintained in the call stack for function calls like A calling B, B calling C.
  - “there is an execution context that will be created and statements will be executed inside that.” — [lines 886-886](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000195`)
  - “Then B is pushed onto the stack, then console.log is executed. So there is a chronological order that we need to maintain, like how to which function should be popped when and the return value of that should be passed to which function.” — [lines 890-890](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000196`)

### Outcome

Not stated in the cited excerpt.

### Original context

**unknown speaker** · lines 874-874 · spoken_turn

> I was just I had a question that since this is called as call stack, right? So, I think it is inferred from the stack data structure, right? But as you mentioned that any task that is put inside this stack is executed immediately. We don't have to wait for another to be pushed on top of it, right? Yes. So how how does that relate? Like calling it as stack data structure and executing it immediately?

**vasanth** · lines 878-878 · spoken_turn

> Correct

**vasanth** · lines 882-882 · spoken_turn

> Yes

**vasanth** · lines 886-886 · spoken_turn

> Very good. Yeah. This question also I ask in interviews. So it's good that you asked the same question to me. So if you observe, right, like to be honest, I'm going to explain more about execution context and other things. See, a statement like this will individually will not be put into the stack. There is an execution context that will be created and statements will be executed inside that. We'll learn more, okay? Now, answering your question, if everything coming here executing one after another, why do we need a stack? I explained that actually. Let's say there are multiple different functions, right, which you are calling one after another. uh I think somewhere I had that.

**vasanth** · lines 890-890 · spoken_turn

> like for example, A calling B, B calling C, right? Then what would happen is like the first whenever you are calling A, A is pushed onto the stack. You are calling A first, A is pushed onto the stack. Then B is pushed onto the stack, then console.log is executed. So there is a chronological order that we need to maintain, like how to which function should be popped when and the return value of that should be passed to which function. So there is an order required in terms of execution. And call stack is not actually property of just the the JavaScript itself. Almost all the programming

<a id="record-8e538e8810771ac2"></a>
## Execution Context Understanding

**Product:** cases · **Type:** reported_exchange · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- Discussion on whether the JavaScript execution context will stay or not.
  - “It won't stay. Shivam saying it won't stay, Pranita saying it won't stay and many here in the call thinks it will stay.” — [lines 1642-1642](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000384`)

### Cue

- Participant expresses a belief on execution context behavior.
  - “because yeah because I think like execution context is removed only after everything has completed their execution” — [lines 1662-1662](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000389`)

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

**vasanth** · lines 1642-1642 · spoken_turn

> It won't stay. Shivam saying it won't stay, Pranita saying it won't stay and many here in the call thinks it will stay. See I'll tell you how it works. It won't stay. Okay. Prashant also said it won't stay. Okay. Anybody in the chat have their anybody comment anything. Okay. Muthura says it will stay and many Vaishali says it will stay. You want to say answer anything Vaishali will it stay? You say it will stay. You want to justify?

**unknown speaker** · lines 1646-1646 · spoken_turn

> don't

**unknown speaker** · lines 1650-1650 · spoken_turn

> call

**unknown speaker** · lines 1654-1654 · spoken_turn

> So I'll tell you how it works

**vasanth** · lines 1658-1658 · spoken_turn

> Achha

**unknown speaker** · lines 1662-1662 · spoken_turn

> because yeah because I think like execution context is removed only after everything has completed their execution. So I think set timeout will complete and then global execution.

**vasanth** · lines 1666-1666 · spoken_turn

> Yes. So I think

**vasanth** · lines 1670-1670 · spoken_turn

> Okay. Sure. I'll I'll quickly summarize. uh Actually global execution is not gonna stay. See, every whatever is in the stack as somebody clearly pointed out I think Shivam or Pranita told I think. So if you think right until call stack is empty set timeout will not come here. We already agreed that right? So if there what what do you mean by call stack is empty? There shouldn't be any execution context. So as long as there's execution context then nothing comes to call stack. Correct? So even the global execution context also removed and these also will be removed. Only then the stack is empty and

**vasanth** · lines 1674-1674 · spoken_turn

> whatever the set time amount which has gone to the macro task will come back. Now comes an interesting question. Wasn't like now globalization context is cleared. From where we are going to get a reference to these variables? Like y is equal to ten, x equal to ten etcetera, right? Because there is no execution context to have a reference to that. What happens is like the set time amount or promises they form a closure. And they will have reference to the variables. You all know closure. We are going to discuss more tomorrow also. So they will already have reference to the variable that they used. So whenever they come back to the stack, they're going to

**vasanth** · lines 1678-1678 · spoken_turn

> actually spin up a new execution context. In fact a new global execution context will also be created. Okay? So though the current global execution context is removed from the stack, still the references will be there. On that it will be creating a new global execution context, then execution context will be getting executed. Okay? Please remember this. So ninety nine percent of the interviews they don't ask this question. Okay? This much depth nobody will go. But I want you guys to know this quite well so that like whenever similar question asked you can show your proficiency in the interview.

**vasanth** · lines 1682-1682 · spoken_turn

> Okay. Now, I think set time out when I have explained this I explained about the global and local execution context. I'm just thinking anything I missed. I've added some of the interesting questions on this section called thought probing question.

**vasanth** · lines 1686-1686 · spoken_turn

> Ha, this is a very interesting question. Anyway, this notion I'll be sharing in the discord, all of the things that I'm speaking so far will be there. Let's say there is a variable named A declared in multiple different JS files. Like one.js, two.js, three.js, all of the different JS files have this variable A. And that there is one single global execution context as we agreed, for one realm of code there is only one execution context. How will the global execution execution context will be able to uniquely identify these variables? If anybody know the answer, you can raise your and put in the chat section.

**unknown speaker** · lines 1690-1690 · spoken_turn

> I believe you guys understood the problem.

**vasanth** · lines 1694-1694 · spoken_turn

> The problem is, let's say there are multiple different variables in the across different files like one.js, two.js, three.js, etcetera, which having the same name. And usually global execution context has responsibilities to have a reference of all of those variables, correct? Like one.js has a variable A and two.js also has a variable A. During execution, the values should be different for each of them, right? How does global execution context will actually be able to understand and explain? Yeah, Mutaraj, please explain.

**unknown speaker** · lines 1698-1698 · spoken_turn

> Yeah, so I'm just understanding this from the uh JavaScript not JavaScript perspective, I'm understanding this in the React perspective. When we have the same variable name or same function name in the uh JavaScript or anything, so browser will convert into according to the it will understand this the both are the different. So it will convert to the different name whatever we given it won't be executed. So in that way I guess the...

**vasanth** · lines 1702-1702 · spoken_turn

> You think the variable A, you think the variable A will be renamed to something like A underscore one dot JS, something like that? Yes, yes. So that it can uniquely identify. Yes. Right? Okay. Sure. Yeah, Sudeep, what do you think?

**unknown speaker** · lines 1706-1706 · spoken_turn

> Yes, yes, so that it can

**unknown speaker** · lines 1710-1710 · spoken_turn

> Yes, yes, I.

<a id="record-6d94dcba16c42b30"></a>
## Visualizing task execution

**Product:** cases · **Type:** reported_exchange · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- A participant asked whether task execution between micro and macro can be visualized in the network tab.
  - “how like browser things will know whether I have to move this promise to micro or macro.” — [lines 898-898](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000198`)

### Cue

- how like browser things will know whether I have to move this promise to micro or macro.
  - “how like browser things will know whether I have to move this promise to micro or macro.” — [lines 898-898](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000198`)

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

- It cannot be visualized because these distinctions are predefined and intrinsic.
  - “No, I think you'll not be able to visualize because these are intrinsic. And which one to put in micro task and which one to put in macro task is predefined” — [lines 910-910](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000201`)

### Outcome

Not stated in the cited excerpt.

### Original context

**unknown speaker** · lines 898-898 · spoken_turn

> Uh yeah. So Vasanth, the one which you explained, right? The macro task or the micro task. Yes. So how this uh like browser things will know whether I have to move this promise to micro or macro. Yes. So are we able to visualize this in our like network tab or somewhere like how we will come to know?

**vasanth** · lines 902-902 · spoken_turn

> Yes

**vasanth** · lines 906-906 · spoken_turn

> Yes

**vasanth** · lines 910-910 · spoken_turn

> No, I think you'll not be able to visualize because these are intrinsic. And which one to put in micro task and which one to put in macro task is predefined as.

<a id="record-d705014ce533abe2"></a>
## File execution in JavaScript

**Product:** cases · **Type:** reported_exchange · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- A participant asked about executing similar files across multiple files and how it impacts the JavaScript execution.
  - “Okay, okay, so my second question is, now you explain that concept of micro task, macro task with the one simple file with the console, right? What if if I have the same kind of file in two files? So how it will execute?” — [lines 838-838](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000183`)

### Cue

- What if if I have the same kind of file in two files? So how it will execute?
  - “What if if I have the same kind of file in two files? So how it will execute?” — [lines 838-838](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000183`)

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

- Files are logical separations for humans and don't affect browser execution much. At times more than one global execution can exist.
  - “files are something a logical separation for human to understand, like one dot js, two dot js to ten dot js” — [lines 858-858](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000188`)
  - “whatever the logical separation that you think you have according as per the files, that are not a logical separation for the browser to execute. Okay, but there will be at times where there is more than one global I'm going to explain more about global execution model where one more than one can exist.” — [lines 862-862](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000189`)

### Outcome

Not stated in the cited excerpt.

### Original context

**unknown speaker** · lines 838-838 · spoken_turn

> Okay. Okay, so my second question is, now you explain that concept of micro task, macro task with the one simple file with the console, right? What if if I have the same kind of file in two files? So how it will execute? It will create one file like this, then it will take the another file or how how it is execute?

**vasanth** · lines 842-842 · spoken_turn

> Sundar

**vasanth** · lines 846-846 · spoken_turn

> What is

**vasanth** · lines 850-850 · spoken_turn

> it will

**vasanth** · lines 854-854 · spoken_turn

> How it is

**vasanth** · lines 858-858 · spoken_turn

> I'm going to explain more about the execution context where I'm going to go deep there, but I give you some simple analogy. See, files are something a logical separation for human to understand, like one dot js, two dot js to ten dot js, right? So whatever the files that you are seeing logically, it need not to be the way the browser sees it. So you can consider like one regime of work, one regime I mean like everything that is required to execute one web page many a times, I would not want to say all the time, many a times is just one big JavaScript dump for the browser.

**vasanth** · lines 862-862 · spoken_turn

> So whatever the logical separation that you think you have according as per the files, that are not a logical separation for the browser to execute. Okay, but there will be at times where there is more than one global I'm going to explain more about global execution model where one more than one can exist. But in simple words to conclude, logical separation of the file is only for human to understand, not for the browsers. Okay.

<a id="record-1a955bbedb5f9e3c"></a>
## Execution Context References

**Product:** cases · **Type:** reported_exchange · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- Participants discuss how global execution context identifies variables with the same name across different files.
  - “I believe you guys understood the problem.” — [lines 1686-1686](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000395`)

### Cue

- Speaker raises a problem about variable reference in global execution context.
  - “If anybody know the answer, you can raise your and put in the chat section.” — [lines 1686-1686](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000395`)

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

- Participants propose solutions such as renaming variables and using closures.
  - “browser will convert into according to the it will understand this the both are the different” — [lines 1698-1698](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000398`)

### Outcome

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 1686-1686 · spoken_turn

> Ha, this is a very interesting question. Anyway, this notion I'll be sharing in the discord, all of the things that I'm speaking so far will be there. Let's say there is a variable named A declared in multiple different JS files. Like one.js, two.js, three.js, all of the different JS files have this variable A. And that there is one single global execution context as we agreed, for one realm of code there is only one execution context. How will the global execution execution context will be able to uniquely identify these variables? If anybody know the answer, you can raise your and put in the chat section.

**unknown speaker** · lines 1690-1690 · spoken_turn

> I believe you guys understood the problem.

**vasanth** · lines 1694-1694 · spoken_turn

> The problem is, let's say there are multiple different variables in the across different files like one.js, two.js, three.js, etcetera, which having the same name. And usually global execution context has responsibilities to have a reference of all of those variables, correct? Like one.js has a variable A and two.js also has a variable A. During execution, the values should be different for each of them, right? How does global execution context will actually be able to understand and explain? Yeah, Mutaraj, please explain.

**unknown speaker** · lines 1698-1698 · spoken_turn

> Yeah, so I'm just understanding this from the uh JavaScript not JavaScript perspective, I'm understanding this in the React perspective. When we have the same variable name or same function name in the uh JavaScript or anything, so browser will convert into according to the it will understand this the both are the different. So it will convert to the different name whatever we given it won't be executed. So in that way I guess the...

**vasanth** · lines 1702-1702 · spoken_turn

> You think the variable A, you think the variable A will be renamed to something like A underscore one dot JS, something like that? Yes, yes. So that it can uniquely identify. Yes. Right? Okay. Sure. Yeah, Sudeep, what do you think?

**unknown speaker** · lines 1706-1706 · spoken_turn

> Yes, yes, so that it can

**unknown speaker** · lines 1710-1710 · spoken_turn

> Yes, yes, I.

**unknown speaker** · lines 1714-1714 · spoken_turn

> I think would it form a closure and like a separate execution context?

**vasanth** · lines 1718-1718 · spoken_turn

> Okay

**vasanth** · lines 1722-1722 · spoken_turn

> you're saying see that we agreed there is one global execution context, correct?

**unknown speaker** · lines 1726-1726 · spoken_turn

> Okay, Okay

**vasanth** · lines 1730-1730 · spoken_turn

> okay okay. So in one globalization context we have to reference multiple different variables which are given us a common name.

**unknown speaker** · lines 1734-1734 · spoken_turn

> Okay

**vasanth** · lines 1738-1738 · spoken_turn

> the closure may not be like the very valid answer, Sudeepta.

**unknown speaker** · lines 1742-1742 · spoken_turn

> Okay

**vasanth** · lines 1746-1746 · spoken_turn

> Yeah, Rameshree, please go ahead.

**unknown speaker** · lines 1750-1750 · spoken_turn

> those variables will be referenced by a function execution context.

**vasanth** · lines 1754-1754 · spoken_turn

> Correct

**vasanth** · lines 1758-1758 · spoken_turn

> No, actually see function execution context, how it works, right? Function execution, okay, good that like you brought that up. Maybe I missed explaining also. See how you all know the priority how the execution happens, right? See global execution, how you let's say there is a variable A, first it will check the variable A exist in the function. If it do not exist in A, then it will look in the global scope. Correct? So what do you mean by it will be looking in global scope? It is actually looking in the global execution context. It checks in the function execution context. If it is not there, then it is going to expect them in the global execution context. So my question

**vasanth** · lines 1762-1762 · spoken_turn

> question there only that whatever you are saying Ramya where the variable actually do not exist in the local execution context so it refer the global execution context but there are multiple different files which are having the same uh variable. So how does that work is my question. Okay.

**vasanth** · lines 1766-1766 · spoken_turn

> Anybody wants to answer? Yes, sir, go ahead.

**unknown speaker** · lines 1770-1770 · spoken_turn

> one thing that I can think of is that creating a separate context for each and every file. That is how

**vasanth** · lines 1774-1774 · spoken_turn

> separate context for each and every file. That is not happening, I told, right? See, what you want, what we want to do like that the JavaScript do not work. For files are just a logical separation for us, not for the JavaScript. Okay? uh Param, yeah, what is your answer?

**unknown speaker** · lines 1778-1778 · spoken_turn

> Yeah, I think like, it will get overridden by the last execution corner because whenever we'll be because whenever we'll be

**vasanth** · lines 1782-1782 · spoken_turn

> like it can happen, param, how can it get overridden? See, one A it was ten, another it is twenty, if you override it by twenty, your program will break. Correct, param.

**unknown speaker** · lines 1786-1786 · spoken_turn

> Yeah, like I mean if we are including all the files in some main JavaScript script file and we are consoling at the end of this script.

<a id="record-b90e8d8647b89fe0"></a>
## JavaScript Execution and Files

**Product:** cases · **Type:** reported_exchange · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- A participant suggests that JavaScript would create separate contexts for each file.
  - “separate context for each and every file. That is not happening, I told, right?” — [lines 1774-1774](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000417`)

### Cue

- Speaker suggests each file has a separate execution context.
  - “creating a separate context for each and every file” — [lines 1770-1770](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000416`)

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

- Response highlights that files are logical separations, not execution contexts in JavaScript.
  - “For files are just a logical separation for us, not for the JavaScript.” — [lines 1774-1774](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000417`)

### Outcome

Not stated in the cited excerpt.

### Original context

**unknown speaker** · lines 1698-1698 · spoken_turn

> Yeah, so I'm just understanding this from the uh JavaScript not JavaScript perspective, I'm understanding this in the React perspective. When we have the same variable name or same function name in the uh JavaScript or anything, so browser will convert into according to the it will understand this the both are the different. So it will convert to the different name whatever we given it won't be executed. So in that way I guess the...

**vasanth** · lines 1702-1702 · spoken_turn

> You think the variable A, you think the variable A will be renamed to something like A underscore one dot JS, something like that? Yes, yes. So that it can uniquely identify. Yes. Right? Okay. Sure. Yeah, Sudeep, what do you think?

**unknown speaker** · lines 1706-1706 · spoken_turn

> Yes, yes, so that it can

**unknown speaker** · lines 1710-1710 · spoken_turn

> Yes, yes, I.

**unknown speaker** · lines 1714-1714 · spoken_turn

> I think would it form a closure and like a separate execution context?

**vasanth** · lines 1718-1718 · spoken_turn

> Okay

**vasanth** · lines 1722-1722 · spoken_turn

> you're saying see that we agreed there is one global execution context, correct?

**unknown speaker** · lines 1726-1726 · spoken_turn

> Okay, Okay

**vasanth** · lines 1730-1730 · spoken_turn

> okay okay. So in one globalization context we have to reference multiple different variables which are given us a common name.

**unknown speaker** · lines 1734-1734 · spoken_turn

> Okay

**vasanth** · lines 1738-1738 · spoken_turn

> the closure may not be like the very valid answer, Sudeepta.

**unknown speaker** · lines 1742-1742 · spoken_turn

> Okay

**vasanth** · lines 1746-1746 · spoken_turn

> Yeah, Rameshree, please go ahead.

**unknown speaker** · lines 1750-1750 · spoken_turn

> those variables will be referenced by a function execution context.

**vasanth** · lines 1754-1754 · spoken_turn

> Correct

**vasanth** · lines 1758-1758 · spoken_turn

> No, actually see function execution context, how it works, right? Function execution, okay, good that like you brought that up. Maybe I missed explaining also. See how you all know the priority how the execution happens, right? See global execution, how you let's say there is a variable A, first it will check the variable A exist in the function. If it do not exist in A, then it will look in the global scope. Correct? So what do you mean by it will be looking in global scope? It is actually looking in the global execution context. It checks in the function execution context. If it is not there, then it is going to expect them in the global execution context. So my question

**vasanth** · lines 1762-1762 · spoken_turn

> question there only that whatever you are saying Ramya where the variable actually do not exist in the local execution context so it refer the global execution context but there are multiple different files which are having the same uh variable. So how does that work is my question. Okay.

**vasanth** · lines 1766-1766 · spoken_turn

> Anybody wants to answer? Yes, sir, go ahead.

**unknown speaker** · lines 1770-1770 · spoken_turn

> one thing that I can think of is that creating a separate context for each and every file. That is how

**vasanth** · lines 1774-1774 · spoken_turn

> separate context for each and every file. That is not happening, I told, right? See, what you want, what we want to do like that the JavaScript do not work. For files are just a logical separation for us, not for the JavaScript. Okay? uh Param, yeah, what is your answer?

<a id="record-adc947c9bcd542d0"></a>
## JavaScript Execution Contexts

**Product:** knowledge · **Type:** method · **Source support:** not_reviewed
**Publication:** 2026-05-31 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- JavaScript execution contexts include a global execution context and local execution contexts for functions.
  - “There'll be two execution context. One is a global execution context, another one is a local execution context.” — [lines 459-459](../../../data/youtube/video/2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-Z-Zj0bYQqnU.md) (`youtube-video-2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-48f7608352:u000084`)

### Goal

- To understand how execution contexts work in JavaScript.
  - “Every time whenever you want to execute a code, you wrap it an execution context created, a memory created for that” — [lines 459-459](../../../data/youtube/video/2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-Z-Zj0bYQqnU.md) (`youtube-video-2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-48f7608352:u000084`)

### Prerequisites

- Basic understanding of JavaScript execution contexts.
  - “Most of you here would know what is execution context.” — [lines 459-459](../../../data/youtube/video/2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-Z-Zj0bYQqnU.md) (`youtube-video-2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-48f7608352:u000084`)

### Steps

1. Recognize the analogy of execution context like a box.
  - “So there is a very simple analogy is that like a box.” — [lines 459-459](../../../data/youtube/video/2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-Z-Zj0bYQqnU.md) (`youtube-video-2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-48f7608352:u000084`)

2. Create an execution context when executing code.
  - “Every time whenever you want to execute a code, you wrap it an execution context created” — [lines 459-459](../../../data/youtube/video/2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-Z-Zj0bYQqnU.md) (`youtube-video-2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-48f7608352:u000084`)

### Constraints

Not stated in the cited excerpt.

### Exceptions

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 459-459 · spoken_turn

> One of the things that I teach in cohort or during the mentorship as well is like there's a concept called execution context in JavaScript. Most of you here would know what is execution context. So there is a very simple analogy is that like a box. Every time whenever you want to execute a code, you wrap it an execution context created, a memory created for that or the execution things whatever required for that is getting created. There'll be two execution context. One is a global execution context, another one is a local execution context. Okay. So every time whenever a function need to get executed, a local execution context is created for that function.

<a id="record-001a6fababb5ebf2"></a>
## Execution context in JavaScript

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-05-31 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- In JavaScript, there is a concept called execution context, which operates like a box where code execution is wrapped, with two types: global and local execution contexts.
  - “there's a concept called execution context in JavaScript... like a box... global execution context... local execution context.” — [lines 459-459](../../../data/youtube/video/2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-Z-Zj0bYQqnU.md) (`youtube-video-2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-48f7608352:u000084`)

### Original context

**vasanth** · lines 459-459 · spoken_turn

> One of the things that I teach in cohort or during the mentorship as well is like there's a concept called execution context in JavaScript. Most of you here would know what is execution context. So there is a very simple analogy is that like a box. Every time whenever you want to execute a code, you wrap it an execution context created, a memory created for that or the execution things whatever required for that is getting created. There'll be two execution context. One is a global execution context, another one is a local execution context. Okay. So every time whenever a function need to get executed, a local execution context is created for that function.

<a id="record-18365c70efc7b4db"></a>
## Analogical Explanation of Execution Context

**Product:** expression · **Type:** rhetorical_move · **Source support:** not_reviewed
**Publication:** 2026-05-31 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- Vasanth uses an analogy of a box to explain the concept of execution context in JavaScript, making it relatable and easier to visualize.
  - “So there is a very simple analogy is that like a box.” — [lines 459-459](../../../data/youtube/video/2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-Z-Zj0bYQqnU.md) (`youtube-video-2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-48f7608352:u000084`)

### Purpose

- To simplify the understanding of execution context for the audience.
  - “Most of you here would know what is execution context.” — [lines 459-459](../../../data/youtube/video/2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-Z-Zj0bYQqnU.md) (`youtube-video-2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-48f7608352:u000084`)

### Original context

**vasanth** · lines 459-459 · spoken_turn

> One of the things that I teach in cohort or during the mentorship as well is like there's a concept called execution context in JavaScript. Most of you here would know what is execution context. So there is a very simple analogy is that like a box. Every time whenever you want to execute a code, you wrap it an execution context created, a memory created for that or the execution things whatever required for that is getting created. There'll be two execution context. One is a global execution context, another one is a local execution context. Okay. So every time whenever a function need to get executed, a local execution context is created for that function.

<a id="record-911532a66ea3374d"></a>
## Execution context analogy

**Product:** expression · **Type:** rhetorical_move · **Source support:** not_reviewed
**Publication:** 2026-05-31 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- The speaker compares the JavaScript execution context to a box, which creates a dedicated space for each code execution.
  - “there is a very simple analogy is that like a box.” — [lines 459-459](../../../data/youtube/video/2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-Z-Zj0bYQqnU.md) (`youtube-video-2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-48f7608352:u000084`)

### Purpose

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 459-459 · spoken_turn

> One of the things that I teach in cohort or during the mentorship as well is like there's a concept called execution context in JavaScript. Most of you here would know what is execution context. So there is a very simple analogy is that like a box. Every time whenever you want to execute a code, you wrap it an execution context created, a memory created for that or the execution things whatever required for that is getting created. There'll be two execution context. One is a global execution context, another one is a local execution context. Okay. So every time whenever a function need to get executed, a local execution context is created for that function.

<a id="record-c4fd6618e43a3492"></a>
## JavaScript Concept in Interview

**Product:** cases · **Type:** illustration · **Source support:** not_reviewed
**Publication:** 2026-05-31 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- Interviewers ask about global execution contexts in a scenario involving multiple JavaScript files calling each other.
  - “Now what interviewers ask is, let's say there are ten different JS files, one dot JS, two dot JS, three dot JS to ten dot JS, correct? So now one dot JS is calling nine dot JS, nine dot JS is calling two dot JS, a lot of this internally they are calling each other.” — [lines 463-463](../../../data/youtube/video/2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-Z-Zj0bYQqnU.md) (`youtube-video-2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-48f7608352:u000085`)

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

**vasanth** · lines 463-463 · spoken_turn

> Now, this is something that if you know this much in twenty twenty one or twenty twenty two, you would have cleared an interview. Now what interviewers ask is, let's say there are ten different JS files, one dot JS, two dot JS, three dot JS to ten dot JS, correct? So now one dot JS is calling nine dot JS, nine dot JS is calling two dot JS, a lot of this internally they are calling each other. How many global execution contexts will be created for this?

<a id="record-024d2b4657c5b3fb"></a>
## Example of Using Closure in React

**Product:** cases · **Type:** illustration · **Source support:** not_reviewed
**Publication:** 2026-05-31 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- While closures are often exemplified using counter increment examples, a more practical use is in React, where a child component is able to invoke the parent component function.
  - “But the good example of closure is actually in React if you see, there is a parent child component. You are passing props to the child component and from the child component you are able to invoke the parent component function.” — [lines 479-479](../../../data/youtube/video/2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-Z-Zj0bYQqnU.md) (`youtube-video-2026-05-31-should-frontend-developers-learn-ai-full-stack-or-system-des-48f7608352:u000089`)

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

**vasanth** · lines 479-479 · spoken_turn

> will never increment a count using a closure in our project. Correct? Then where you are using the closure? And many try to give all of these random examples which they never use. So interviewers start getting a feeling they know concept but they never used it. Correct? But the good example of closure is actually in React if you see, there is a parent child component. You are passing props to the child component and from the child component you are able to invoke the parent component function, right? What is that? That is a simple closure. It's working only because of closure. Correct? And we are able to access variables from everywhere because of

<a id="record-b6d1bb5aa99ba89f"></a>
## JavaScript Engine

**Product:** knowledge · **Type:** self_report · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- JavaScript is described as 'single threaded and synchronous by default'.
  - “So JavaScript is a single threaded and synchronous by default.” — [lines 1246-1246](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000299`)

### Original context

**vasanth** · lines 1246-1246 · spoken_turn

> multithreaded and asynchronous by default, single threaded and synchronous by default. I suppose I repeated multiple times this in the session today. So JavaScript is a single threaded and synchronous by default. Okay?

<a id="record-f637ad8fc51ddd20"></a>
## JavaScript Execution Responsibility

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- The JavaScript engine is responsible for executing the JavaScript code, not web APIs, event loop, or task queue.
  - “Certainly the JavaScript engine is responsible for executing the JavaScript code. Neither the web API is non event loop or the task queue.” — [lines 1250-1250](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000300`)

### Original context

**vasanth** · lines 1250-1250 · spoken_turn

> Which component is representing responsible for executing the JavaScript code? Certainly the JavaScript engine is responsible for executing the JavaScript code. Neither the web API is non event loop or the task queue. What will be the output? So we have start and timeout, though timeout has zero, definitely it, I'm sorry. uh There is a start, timeout and there is an end here, that was not shown. So it is start, end and timeout, this also we discussed in the session. Couple of questions were like this only in the similar pattern. Which

<a id="record-e3343425023fae1f"></a>
## JavaScript Description

**Product:** expression · **Type:** structure · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- The speaker uses a simple assertion format to describe JavaScript's threading model: 'JavaScript is a single threaded and synchronous by default.'
  - “So JavaScript is a single threaded and synchronous by default.” — [lines 1246-1246](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000299`)

### Purpose

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 1246-1246 · spoken_turn

> multithreaded and asynchronous by default, single threaded and synchronous by default. I suppose I repeated multiple times this in the session today. So JavaScript is a single threaded and synchronous by default. Okay?

<a id="record-0d99cff659730d1d"></a>
## Importance of understanding JavaScript fundamentals

**Product:** knowledge · **Type:** advice · **Source support:** not_reviewed
**Publication:** 2025-01-03 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Vasanth advises learning the fundamental concepts of JavaScript deeply, as being fundamentally strong is crucial for progressing beyond basic product development.
  - “So become extremely fundamentally strong, which is a core thing that somebody should learn if they want to learn front end in 2025.” — [lines 130-130](../../../data/youtube/video/2025-01-03-master-frontend-development-in-2025-a-complete-roadmap-BfDVA_OsFLM.md) (`youtube-video-2025-01-03-master-frontend-development-in-2025-a-complete-roadmap-bfdva-7c1566cce2:u000024`)

### Original context

**vasanth** · lines 122-122 · spoken_turn

> to do. Thing is like I got an opportunity to work in like startups and mid-range companies where the the progress was extremely important than perfection. So I wanted to deliver things not necessarily in the right way. Because of which what happened I never understood the fundamentals concepts of JavaScript. I was always behind like given a requirement I just used to convert them into product. After two three years in my career like when this section I started like 2019 and 2020 where I realized I'm extremely hollow. I don't know how

**vasanth** · lines 126-126 · spoken_turn

> actually JavaScript works behind the scene. Like you might be surprised till two thousand nineteen I did not even know how hosting works or what is execution context, how closures work. Should my project have more closure or less closure? Even after I'm three years of experience I did not know none of these basics. That time when I took a pause.

**vasanth** · lines 130-130 · spoken_turn

> Instead of building the things, I started understanding how things work behind the scenes step by step. So what I recommend today, if you start learning JavaScript, do not make the mistake that I did. It's not about building the screens. Now with the help of Chat GPT or Gemini, even like some tenth or twelfth graduate can also build the screens. But if you're fundamentally strong, there is a scope for you to build things which is beyond like somebody who can use Chat GPT or Gemini can build. So become extremely fundamentally strong, which is a core thing that somebody should learn if they want to learn front end in 2025. Thank you.
