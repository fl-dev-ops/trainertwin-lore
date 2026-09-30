# javascript execution context

> Source-local records, not independent fact verification. Original steps and qualifications are retained.

<a id="record-52eba3ebc14159f9"></a>
## Global Execution Context

**Product:** knowledge · **Type:** belief · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- In JavaScript, a global execution context is created once for each JavaScript realm in a browser, representing code not inside any function.
  - “In a browser typically only one global execution context is created per JavaScript rel.” — [lines 1066-1066](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000240`)
  - “Browser considers one realm of JavaScript as one entity only, okay?” — [lines 1066-1066](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000240`)

### Original context

**vasanth** · lines 1062-1062 · spoken_turn

> In a browser typically only one global execution context is created per JavaScript rel. You can consider like one for one page or one window, only one global execution context is created. As I already explained, files are just a source, just a source of code, not a runtime bound piece. Let's say you have from one JS to ten JS you have, like ten different files if you are having and you call them intermittently, like two is calling eight, eight is calling five etcetera. I explained that in many of them in the screening call also and in my webinar that I did last week as well.

**vasanth** · lines 1066-1066 · spoken_turn

> So if you're doing that, that doesn't mean browser consider them as like separate entities. Browser considers one realm of JavaScript as one entity only, okay? Represent code not inside any function, sits at the sits at the bottom of the call stack, okay? See global execution context means given a program.

<a id="record-1853c857f82b0f56"></a>
## Memory Creation Phase

**Product:** knowledge · **Type:** self_report · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- During the memory creation phase, memory is allocated, and variables are hoisted and declared with 'undefined'. Function declarations are fully hoisted.
  - “In memory creation phase what happens? It allocates the memory, sets up the scope. During this phase like variable creators is where keyword are like hoisted and declared with undefined. Function declarations are fully hoisted.” — [lines 1086-1086](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000245`)

### Original context

**vasanth** · lines 1086-1086 · spoken_turn

> So now, what does global execution contents? What does it contain? It contains actually primarily two phases in general. So one is a memory creation phase, another is a code execution phase. I believe almost all of you might be aware of this, how a JavaScript executes its code, right? There is a two phase of execution. One is a memory of creation phase, another is actual code execution. So in memory creation phase what happens? It allocates the memory, sets up the scope. During this phase like variable creators is where keyword are like hoisted and declared with undefined. Function declarations are fully hoisted, latent constant allocates

**vasanth** · lines 1090-1090 · spoken_turn

> but not initialized. This will get a reference like different places you are using that this will have a different references. Sometimes it will be window object that sometimes it will be a caller references. All of that set will be during the memory creation phase. Okay? Again I'll repeat. Global execution context or in general execution context has two phases. One is a memory creation phase, another one is a code execution phase. On contrary you can also consider JavaScript code execution also has two parts. One is memory creation phase, another one is a code execution phase. Okay? Now in the code

**vasanth** · lines 1094-1094 · spoken_turn

> execution phase is where the app has to execute the codes line by line. Variables get actual values, functions are invoked. I'll repeat. Memory creation phase is a phase where actually memory is allocated. How much ever memory required to execute that block of code, that will be allocated. During the code execution phase, actual values will be added and execution will happen. Now many people ask why we are doing it in two phases. So the reason being,

<a id="record-2233745890e68b49"></a>
## JavaScript Execution Context Phases

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- The global execution context contains two phases: memory creation and code execution.
  - “global execution context. Function execution context or local execution context is pretty much the same. It also has two things, memory creation phase and the code execution phase.” — [lines 1122-1122](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000254`)

### Original context

**vasanth** · lines 1086-1086 · spoken_turn

> So now, what does global execution contents? What does it contain? It contains actually primarily two phases in general. So one is a memory creation phase, another is a code execution phase. I believe almost all of you might be aware of this, how a JavaScript executes its code, right? There is a two phase of execution. One is a memory of creation phase, another is actual code execution. So in memory creation phase what happens? It allocates the memory, sets up the scope. During this phase like variable creators is where keyword are like hoisted and declared with undefined. Function declarations are fully hoisted, latent constant allocates

**vasanth** · lines 1090-1090 · spoken_turn

> but not initialized. This will get a reference like different places you are using that this will have a different references. Sometimes it will be window object that sometimes it will be a caller references. All of that set will be during the memory creation phase. Okay? Again I'll repeat. Global execution context or in general execution context has two phases. One is a memory creation phase, another one is a code execution phase. On contrary you can also consider JavaScript code execution also has two parts. One is memory creation phase, another one is a code execution phase. Okay? Now in the code

**vasanth** · lines 1094-1094 · spoken_turn

> execution phase is where the app has to execute the codes line by line. Variables get actual values, functions are invoked. I'll repeat. Memory creation phase is a phase where actually memory is allocated. How much ever memory required to execute that block of code, that will be allocated. During the code execution phase, actual values will be added and execution will happen. Now many people ask why we are doing it in two phases. So the reason being,

**vasanth** · lines 1098-1098 · spoken_turn

> when JavaScript was designed, it was primarily designed to work on a browser, not like on Node.js and all that, etcetera, right? It was designed to work on the browser. As it's working on the browser, the browser basically has like limited memory. If you see even if you go and inspect your Chrome browser now, it might be taking majority of your app. Correct? So memory creation phase is required to ensure this program can be executed or not. Like, let's say many a times you feel like the program execute like the in a page, right? We are not able to run the page like the something got handled or you have to

**vasanth** · lines 1102-1102 · spoken_turn

> the tab etcetera, right? That's happening because the browser is not able to allocate the memory that is required to execute that realm of code.

**vasanth** · lines 1106-1106 · spoken_turn

> So if you are getting that much of memory then it is reserved for you then you will be able to execute it. But probably the language like Java etcetera they directly interact with hardware. They have a higher chance of getting more memory compared to the browser. So JavaScript in general is always competing for more and more memory. That's the reason why first is a memory creation phase. Just if I have to digress and explain if you see the deep copy and shallow copy in JavaScript the variables created all the array and object types are actually shallow copy whereas the primitive types like number, string are deep

**vasanth** · lines 1110-1110 · spoken_turn

> copied. Same reason why they are also shallow copied like array and object expected to be like larger in terms of size. If they keep creating a newer instances or if they keep making if a JavaScript makes a deeper copy of it it end up have consuming more memory. So unless you manually specify JavaScript engine to like make it a deep copy naturally they are all shallow copied. Okay? And if you look at the simple example variable a is equal to ten function foo foo and function test so you are calling the test test will get executed.

**vasanth** · lines 1114-1114 · spoken_turn

> and then you have foo also. foo also will call this one. Both can call the each of them functions in parallel. So if you see memory creation phase, A is undefined. foo function has a reference. Function execution phase A is ten, foo is invoked. Okay?

**vasanth** · lines 1118-1118 · spoken_turn

> And if you look at this particular simple block of code, so first, second and third, if you see first is getting called, then the first calls second, then second calls the third. So if you see the third one is on the top of the execution context. So there's a global execution context and a multiple function execution function execution context. They are created in the order they are getting invoked. The first, second and third, three different execution context is created. Okay?

**vasanth** · lines 1122-1122 · spoken_turn

> So first in the call stack, the global execution context always sits at the bottom. Function execution contexts are keep on getting added on the top. Okay? What is function execution context? Now so far you understood about the global execution context. Function execution context or local execution context is pretty much the same. It also has two things, memory creation phase and the code execution phase. Created every time when a function is called, each function call gets a new execution context, pushed onto call stack, destroyed after the function finishes its execution. Okay? So if you see in this example,

<a id="record-0949f5b99703a27d"></a>
## Function Execution Context

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- A function execution context is created every time a function is called, has memory creation and code execution phases, and is destroyed after execution.
  - “Function execution context or local execution context is pretty much the same. It also has two things, memory creation phase and the code execution phase. Created every time when a function is called, each function call gets a new execution context, pushed onto call stack, destroyed after the function finishes its execution.” — [lines 1122-1122](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000254`)

### Original context

**vasanth** · lines 1122-1122 · spoken_turn

> So first in the call stack, the global execution context always sits at the bottom. Function execution contexts are keep on getting added on the top. Okay? What is function execution context? Now so far you understood about the global execution context. Function execution context or local execution context is pretty much the same. It also has two things, memory creation phase and the code execution phase. Created every time when a function is called, each function call gets a new execution context, pushed onto call stack, destroyed after the function finishes its execution. Okay? So if you see in this example,

**vasanth** · lines 1126-1126 · spoken_turn

> the greetings got pushed and greetings is calling say hi. When for this particular say hi, you're going to create an execution context. It also has two phases, one is memory allocation phase and another one is a code execution phase. Once after the code is executed, the say hi function will be removed from the stack. Then if it has to return something, it will be returned and that returned reference will go to the greetings. If there is nothing, then what will be returned? Then the greetings will be executed and then the greetings will be cleared. After these two are cleared, the global execution context is also cleared and fully removed from the stack. Okay? I'll take a pause.

**vasanth** · lines 1130-1130 · spoken_turn

> months after I finished this execution. Now explaining this I'm sorry. Okay. So now you have function add, same thing x becomes two, y becomes three during the execution phase and result will be undefined during the creation phase, result becomes five during the execution phase. Okay. How they work? Global execution context pushed first. Each function call creates a new function execution context, pushed onto the call stack. When function returns, the execution context is popped out of the stack. Whenever the function returned or whenever function completes its execution, it will be popped out of the stack. Okay. Again, I will not repeat most of these things I have already explained. Okay?

<a id="record-18d95722f4fb8f04"></a>
## JavaScript Execution Context

**Product:** knowledge · **Type:** belief · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- An execution context in JavaScript is the environment in which code is evaluated and executed. Only one execution context is active at any time.
  - “Execution context is an environment in which JavaScript code is evaluated and executed.” — [lines 1054-1054](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000237`)
  - “At any moment, only one execution context is active. One execution context is active, okay?” — [lines 1058-1058](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000238`)

### Original context

**vasanth** · lines 1050-1050 · spoken_turn

> Thank you. Now we'll quickly move to the second concept that is execution context. Okay? See by the time when I was explaining this somebody also asked it what do you mean by like console dot looking into this or anything getting into the call stack right? In reality the statements there by themselves are not going to get into call stack and get executed. Just it like in a safer way to like whenever you're explaining concepts to someone in interview also or in general also it's safe easier to explain so we explain like this. But nothing actually like individual statements do not get into call stack. Okay?

**vasanth** · lines 1054-1054 · spoken_turn

> What gets into call stack is actually a execution context. What is an execution context? Execution context is an environment in which JavaScript code is evaluated and executed. Every time JavaScript runs the code, it does inside the execution context. At any moment, only one execution context is active. One execution context is active, okay? Not like only one execution context is present. At any given point in time, only one execution context is active. It always sits on top of the call stack. A multiple

**vasanth** · lines 1058-1058 · spoken_turn

> things it always sits on top of the call stack. Okay. So whichever is gonna execute that will be always on the top. Types of execution context are two execution context. Global execution context and the function execution context. Sometimes it's also referred as a local execution context but in interview I prefer you can say global execution context and function execution context. Now. So global execution context I'll come to the diagram in a while. What is global execution context? It created once when a JavaScript file start executing.

<a id="record-f37b2092546f97b7"></a>
## JavaScript Execution Context

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Execution context is created only for global code and function calls.
  - “Execution context is created for not for every line.” — [lines 1850-1850](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000436`)

### Original context

**vasanth** · lines 1850-1850 · spoken_turn

> and uh pretty much covered everything that I wanted to cover for the day. Execution context is created for not for every line. Created only for global code and function call like only function call creates an execution context. Async callbacks run in every new execution context. Hosting happens during execution not hosting happens during the memory creation phase. Um okay quick summary I'll not reiterate same thing I explained. See always ask this question to yourself in physicality what a

<a id="record-e0e5543f89e868f6"></a>
## Phases of Global Execution Context

**Product:** knowledge · **Type:** belief · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Global execution context consists of two phases: memory creation and code execution. Memory creation involves allocating memory and setting up scope.
  - “So one is a memory creation phase, another is a code execution phase.” — [lines 1086-1086](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000245`)
  - “In memory creation phase what happens? It allocates the memory, sets up the scope.” — [lines 1086-1086](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000245`)

### Original context

**vasanth** · lines 1082-1082 · spoken_turn

> represents a code not inside any function. Anything inside the code is basically handled by the global the that particular function execution context. sits at the bottom of the call stack. I'll show you a diagram. Okay. sits at the bottom of the call stack. Similar to this. I'll explain more. Okay.

**vasanth** · lines 1086-1086 · spoken_turn

> So now, what does global execution contents? What does it contain? It contains actually primarily two phases in general. So one is a memory creation phase, another is a code execution phase. I believe almost all of you might be aware of this, how a JavaScript executes its code, right? There is a two phase of execution. One is a memory of creation phase, another is actual code execution. So in memory creation phase what happens? It allocates the memory, sets up the scope. During this phase like variable creators is where keyword are like hoisted and declared with undefined. Function declarations are fully hoisted, latent constant allocates

<a id="record-4f09807f04f77c32"></a>
## Code Execution Phase

**Product:** knowledge · **Type:** self_report · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- During the code execution phase, the app executes the code line by line. Variables get actual values, and functions are invoked.
  - “execution phase is where the app has to execute the codes line by line. Variables get actual values, functions are invoked.” — [lines 1094-1094](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000247`)

### Original context

**vasanth** · lines 1094-1094 · spoken_turn

> execution phase is where the app has to execute the codes line by line. Variables get actual values, functions are invoked. I'll repeat. Memory creation phase is a phase where actually memory is allocated. How much ever memory required to execute that block of code, that will be allocated. During the code execution phase, actual values will be added and execution will happen. Now many people ask why we are doing it in two phases. So the reason being,

**vasanth** · lines 1098-1098 · spoken_turn

> when JavaScript was designed, it was primarily designed to work on a browser, not like on Node.js and all that, etcetera, right? It was designed to work on the browser. As it's working on the browser, the browser basically has like limited memory. If you see even if you go and inspect your Chrome browser now, it might be taking majority of your app. Correct? So memory creation phase is required to ensure this program can be executed or not. Like, let's say many a times you feel like the program execute like the in a page, right? We are not able to run the page like the something got handled or you have to

**vasanth** · lines 1102-1102 · spoken_turn

> the tab etcetera, right? That's happening because the browser is not able to allocate the memory that is required to execute that realm of code.

**vasanth** · lines 1106-1106 · spoken_turn

> So if you are getting that much of memory then it is reserved for you then you will be able to execute it. But probably the language like Java etcetera they directly interact with hardware. They have a higher chance of getting more memory compared to the browser. So JavaScript in general is always competing for more and more memory. That's the reason why first is a memory creation phase. Just if I have to digress and explain if you see the deep copy and shallow copy in JavaScript the variables created all the array and object types are actually shallow copy whereas the primitive types like number, string are deep

**vasanth** · lines 1110-1110 · spoken_turn

> copied. Same reason why they are also shallow copied like array and object expected to be like larger in terms of size. If they keep creating a newer instances or if they keep making if a JavaScript makes a deeper copy of it it end up have consuming more memory. So unless you manually specify JavaScript engine to like make it a deep copy naturally they are all shallow copied. Okay? And if you look at the simple example variable a is equal to ten function foo foo and function test so you are calling the test test will get executed.

**vasanth** · lines 1114-1114 · spoken_turn

> and then you have foo also. foo also will call this one. Both can call the each of them functions in parallel. So if you see memory creation phase, A is undefined. foo function has a reference. Function execution phase A is ten, foo is invoked. Okay?

<a id="record-54a1bf3cd7671732"></a>
## JavaScript Execution Context Explanation

**Product:** expression · **Type:** structure · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- The speaker clarifies the concept of execution context by stating its role as the environment for JavaScript code evaluation and execution, emphasizing that only one execution context is active at a time.
  - “Execution context is an environment in which JavaScript code is evaluated and executed.” — [lines 1054-1054](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000237`)
  - “At any moment, only one execution context is active.” — [lines 1054-1054](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000237`)

### Purpose

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 1050-1050 · spoken_turn

> Thank you. Now we'll quickly move to the second concept that is execution context. Okay? See by the time when I was explaining this somebody also asked it what do you mean by like console dot looking into this or anything getting into the call stack right? In reality the statements there by themselves are not going to get into call stack and get executed. Just it like in a safer way to like whenever you're explaining concepts to someone in interview also or in general also it's safe easier to explain so we explain like this. But nothing actually like individual statements do not get into call stack. Okay?

**vasanth** · lines 1054-1054 · spoken_turn

> What gets into call stack is actually a execution context. What is an execution context? Execution context is an environment in which JavaScript code is evaluated and executed. Every time JavaScript runs the code, it does inside the execution context. At any moment, only one execution context is active. One execution context is active, okay? Not like only one execution context is present. At any given point in time, only one execution context is active. It always sits on top of the call stack. A multiple

<a id="record-170967befa4ea091"></a>
## Explanation of Execution Context

**Product:** expression · **Type:** wording · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- The speaker emphasizes the importance of understanding execution context for interviews and fundamental understanding of JavaScript, using direct statements.
  - “Again it's a super important concept. The concept of execution context is very very important in terms of interview. Plus also it will give you like fundamental understanding of JavaScript.” — [lines 1166-1166](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000265`)

### Purpose

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 1166-1166 · spoken_turn

> Again it's a super important concept. The concept of execution context is very very important in terms of interview. Plus also it will give you like fundamental understanding of JavaScript. Like you start looking at a concept differently once you understand the call stack very well. Okay. Please go ahead Sagar. Yeah.

<a id="record-96fc171c8712a0b3"></a>
## Global Execution Without Function

**Product:** cases · **Type:** reported_exchange · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- A participant questions how global execution context handles JavaScript code when no functions are defined.
  - “See this is not having any function to begin with, correct? So situation like this where JavaScript itself will assume this complete block as one execution context and the execution context is only pushed into the stack.” — [lines 1142-1142](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000259`)

### Cue

- Whenever I say actually execution context goes into the stack, right? What do we truly mean by that?
  - “Whenever I say actually execution context goes into the stack, right? What do we truly mean by that?” — [lines 1142-1142](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000259`)

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

- JavaScript assumes this block as one execution context, and no statement gets into the stack; the entire context is managed globally.
  - “JavaScript itself will assume this complete block as one execution context and the execution context is only pushed into the stack. Okay? And things like this where there is no external functions, the global everything is global in nature, so global execution context itself will start executing them.” — [lines 1142-1142](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000259`)

### Outcome

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 1142-1142 · spoken_turn

> just give me a moment. See this is not having any function to begin with, correct? So situation like this where JavaScript itself will assume this complete block as one execution context and the execution context is only pushed into the stack. Okay? And things like this where there is no external functions, the global everything is global in nature, so global execution context itself will start executing them. Okay? So nothing as a statement gets into the stack. Now, one more interesting question, whenever I say actually execution context goes into the stack, right? What do we truly mean by that?

**vasanth** · lines 1146-1146 · spoken_turn

> For example now, function execution context say I moved here right? See imagine like there is no code that is getting moved into the stack. I repeat, there is no code that is getting moved into the stack. There is a memory where this complete execution context is created, a reference to that is moving into the stack and that reference will be pointing to all the functions, variables, all of that is declared and JavaScript engine or the browser capabilities takes care of defining the memory and everything. In the stack whenever before it starts executing, the memory creation phase is already
