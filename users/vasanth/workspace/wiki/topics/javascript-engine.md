# javascript engine

> Source-local records, not independent fact verification. Original steps and qualifications are retained.

<a id="record-895cc569ec78e36e"></a>
## Call Stack Execution

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- The call stack in JavaScript executes code in a last in, first out order, managing the function execution.
  - “Call stack execute JavaScript code, follows last in first out order.” — [lines 438-438](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000083`)

### Original context

**vasanth** · lines 438-438 · spoken_turn

> V8, Safari, Chakra, etcetera. It contains primarily two parts, memory heap and a call stack. Memory heap is where variables, function, objects are actually stored. Call stack execute JavaScript code, follows last in first out order. Only one piece of code executes at a time. Please remember that, okay? Because single threaded, we cannot do more than one at a time, correct? So only one piece of code executed at a time, okay? So, I'll give a pause probably after I explain few more because the doubts that you might get, I might cover in next five to ten minutes, okay?

**vasanth** · lines 442-442 · spoken_turn

> after I finish the JavaScript runtime encounter fully, I'll give a pause and we can spend like five to ten minutes discussing the questions. Okay? So JavaScript heap is a region in the RAM used by the JavaScript engine for dynamic memory allocation. Objects, arrays, functions, closures are typically stored there, while variables on the stack usually hold a reference to the those objects on the heap. Okay? I'll make a slight digressing while while I'm explaining this, right? Many people think, um whenever that many people think whenever they're basically calling a function and passing an

**vasanth** · lines 446-446 · spoken_turn

> object to that function and that function may be processing that object or passing to another function. We have a feeling right let's say that's a very bulky object. If we send it to a function and it transforms it and sends it back. Many times during the PR reviews and other times I've seen like let us not send this heavy object to that function because it might be like um like taking more processing. But that is not the case. So this is a tip to all the senior developers out here. Whenever we are calling a function passing a argument etcetera we are just passing the references not the

**vasanth** · lines 450-450 · spoken_turn

> table itself in physicality we are not sending anything to function okay so even if you want to transform a large object within a utility function and get it back all you are doing is just passing a reference to that utility and getting these things done okay so in your programming you can use it exclusively like you can pass any bigger objects to a utility get the transformation done and get it back so you don't have to shy away from doing that okay maybe in though I wanted to give a pause later but so far whatever I explained anybody has any doubts you can raise your hand

**vasanth** · lines 454-454 · spoken_turn

> So as I told what Vaishali asked, there are two types of compilation. One is just in time compilation, another one is ahead of time compilation, two compilations I request. So ahead of time compilation means even before the program executes, very similar to how Java runs. So the complete code base is analyzed and seen whether there is like whatever the variable that we declared, can that be initialized? That for example, you declare int x, we have to allocate I think eight bytes or four bytes to int in Java. So can we allocate that much, that much of memory available? So during the compilation phase itself, the memory checks will happen any single

**vasanth** · lines 458-458 · spoken_turn

> text error will be checked. If any problem is there, code itself will not execute. This is ahead of time compilation. Large part of Angular uses this. And another thing is just in time compilation. So code is not fully analyzed. So during the runtime itself, the compilation happens. So there will be at times where all the files which are present as a part of the code will not be compiled. As and when things are needed, they will be compiled and they will be executed. So if there is a

**vasanth** · lines 462-462 · spoken_turn

> If you have to compare something that is like ahead of time compilation is much better because all the program is scanned before it starts executing but it comes at a cost of time and processing because it has everything need to be processed and need to be analyzed. Okay. Now let's go to the call stack execution. Very very interesting and I like this concept a lot. The call stack manages the function execution order. So if you see we are going in a synchronous order. So JavaScript runtime enabler consists of JavaScript engine and browser capability. JavaScript engine

**vasanth** · lines 466-466 · spoken_turn

> consist of call stack and memory heap. Now memory heap as I told it's largely an unorganized memory but it is safe to assume the memory is given by the RAM itself. Next in the call stack is basically a stack that holds reference to the whatever the variables function that are declared in the heap. Now let's go little deeper and try to understand the call stack. I'm pretty sure everyone in the call might have know the concept of event loop and about the call stack. But let I'll try to give few perspectives that you some of you at least might have not thought by yourself. Okay. The call stack manages the function

**vasanth** · lines 470-470 · spoken_turn

> function execution order. So that means you are calling A and there is this is the A function then A function is calling B correct execution flow A is pushed onto the stack then B is pushed onto the stack then console.log executes function completes and popped off the stack.

**vasanth** · lines 474-474 · spoken_turn

> Let's say, I mean this this diagram do not directly explain what I'm saying above, but you can consider call stack as like, you can consider like there is a set of things that are going to the stack. Multiple things will go into the stack and they'll execute one after another. Okay? So, I used to ask in interview, you can also listen to this, why call stack is actually a stack? Why can't call stack be actually linked list or why not call stack be tree? Okay? So if you observe, let's say, let's take a simple example, I believe. there will be some simple N of code somewhere.

**vasanth** · lines 478-478 · spoken_turn

> Let's say we have these four lines of code. console.log a, set timeout, and for a while let us imagine promise is not there. There is one more console.log. Three statements are there. So, in typical whenever I ask this question in the interview what people say is, first console.log, which is this first line, gets into call stack. Then the set timeout will comes and it will go to the web API. Then the console.log b will come to call stack, then the execution starts. This is what many people say.

**vasanth** · lines 482-482 · spoken_turn

> again I'll repeat. So first console.log a comes to call stack, it'll be waiting, then set timeout comes and it'll be waiting, like it'll go to whatever the delay that's supposed to execute, then console.log b comes and start executing. And then like console.log d comes, then finally execution starts. If execution happens that way, then the d will be printed first, because it's a stack, right? It's a pile of plates, one one on top of another. So you have to take the top plate first, followed by the next. Correct? If you do that, then what would happen?

**vasanth** · lines 486-486 · spoken_turn

> whatever came in the last will be running first which is totally opposite to how a programming language should work okay the call stack is a stack only because it holds the function references like I explained here okay so let's say function A you are calling A A is calling B we will call C we have a chronological order of calling the function one after another so we are using the stack to maintain that order okay and coming to the simple example that I was saying

**vasanth** · lines 490-490 · spoken_turn

> We're going to explain more how actually the execution happens but in simple words if I have to say as soon as console.log a gets into call stack it get executed. It is not going to wait for anything else to come. Okay. A executes then set timeout then d comes. I'm going to explain more exactly how it works but in simple words you can assume. A executes then probably d executes then set timeout whenever it comes again comes to call stack and get executed. So there is no waiting in the call stack. Okay. Also why stack is used only because of this reason. Okay to maintain a chronological order of the function call. Okay. So

<a id="record-101c4a3f31d3a372"></a>
## JavaScript Engine Overview

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- The JavaScript engine primarily contains two parts: the memory heap and the call stack.
  - “JavaScript engine primarily contains two things, memory heap and a call stack.” — [lines 430-430](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000081`)

### Original context

**vasanth** · lines 426-426 · spoken_turn

> Uh yeah so now let's get into understand the JavaScript engine okay? So JavaScript engine are I think many of you at least know V8 which is an engine used by the Chrome and many other things also Node.js also uses V8. So many other JavaScript libraries which even open source libraries also use the V8 engine by the Chrome and JavaScript core is a engine used by Safari. Chakra is a used old engine used by the browsers like Internet Explorer okay? What JavaScript engine

**vasanth** · lines 430-430 · spoken_turn

> contains, it primarily contains two two things, memory heap and a call stack. Okay. So what is a memory heap? You could consider like it stores variable objects and function. You can look at this diagram, okay. So JavaScript engine primarily contains two things, memory heap, memory heap and a call stack. So if you look at this diagram, heap is a place where actually things are getting stored, a memory location. So it is very hard to say where exactly JavaScript stores the things because unlike Java or C++ C++ C#, the

**vasanth** · lines 434-434 · spoken_turn

> and which do not directly interact with the hardware. So JavaScript consider assuming let's assume like on the browser sort of a where we are running JavaScript. So JavaScript primarily interacts with the browser. Browser internally interacts with the hardware, correct? So but it is very safe to say primarily most of this heap memory or the memory heap is from the RAM memory itself, whatever the RAM memory that we have. So the variables are actually stored in the RAM and stack is going to have a reference to it. The call stack is going to have a reference to it. I'll repeat. So JavaScript engine, they are very popular in this.

**vasanth** · lines 438-438 · spoken_turn

> V8, Safari, Chakra, etcetera. It contains primarily two parts, memory heap and a call stack. Memory heap is where variables, function, objects are actually stored. Call stack execute JavaScript code, follows last in first out order. Only one piece of code executes at a time. Please remember that, okay? Because single threaded, we cannot do more than one at a time, correct? So only one piece of code executed at a time, okay? So, I'll give a pause probably after I explain few more because the doubts that you might get, I might cover in next five to ten minutes, okay?

<a id="record-280299a6631339e8"></a>
## Explaining Call Stack Order

**Product:** expression · **Type:** rhetorical_move · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- Vasanth uses a rhetorical question to explain why the call stack is a stack and not another data structure like a linked list or tree.
  - “I used to ask in interview, you can also listen to this, why call stack is actually a stack? Why can't call stack be actually linked list or why not call stack be tree?” — [lines 474-474](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000092`)

### Purpose

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 470-470 · spoken_turn

> function execution order. So that means you are calling A and there is this is the A function then A function is calling B correct execution flow A is pushed onto the stack then B is pushed onto the stack then console.log executes function completes and popped off the stack.

**vasanth** · lines 474-474 · spoken_turn

> Let's say, I mean this this diagram do not directly explain what I'm saying above, but you can consider call stack as like, you can consider like there is a set of things that are going to the stack. Multiple things will go into the stack and they'll execute one after another. Okay? So, I used to ask in interview, you can also listen to this, why call stack is actually a stack? Why can't call stack be actually linked list or why not call stack be tree? Okay? So if you observe, let's say, let's take a simple example, I believe. there will be some simple N of code somewhere.

**vasanth** · lines 478-478 · spoken_turn

> Let's say we have these four lines of code. console.log a, set timeout, and for a while let us imagine promise is not there. There is one more console.log. Three statements are there. So, in typical whenever I ask this question in the interview what people say is, first console.log, which is this first line, gets into call stack. Then the set timeout will comes and it will go to the web API. Then the console.log b will come to call stack, then the execution starts. This is what many people say.

**vasanth** · lines 482-482 · spoken_turn

> again I'll repeat. So first console.log a comes to call stack, it'll be waiting, then set timeout comes and it'll be waiting, like it'll go to whatever the delay that's supposed to execute, then console.log b comes and start executing. And then like console.log d comes, then finally execution starts. If execution happens that way, then the d will be printed first, because it's a stack, right? It's a pile of plates, one one on top of another. So you have to take the top plate first, followed by the next. Correct? If you do that, then what would happen?

**vasanth** · lines 486-486 · spoken_turn

> whatever came in the last will be running first which is totally opposite to how a programming language should work okay the call stack is a stack only because it holds the function references like I explained here okay so let's say function A you are calling A A is calling B we will call C we have a chronological order of calling the function one after another so we are using the stack to maintain that order okay and coming to the simple example that I was saying

<a id="record-1702d8de4662bde9"></a>
## Use of Analogy with Plates

**Product:** expression · **Type:** rhetorical_move · **Source support:** not_reviewed
**Publication:** 2026-06-09 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- Explains the concept of the call stack using the analogy of a pile of plates to demonstrate the LIFO \(Last In First Out\) order.
  - “If execution happens that way, then the d will be printed first, because it's a stack, right? It's a pile of plates, one one on top of another.” — [lines 482-482](../../../data/youtube/video/2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-OnQvAtOm8cg.md) (`youtube-video-2026-06-09-careerwithvasanth-frontend-mastery-cohort-2-session-1-javasc-0f97878bf2:u000094`)

### Purpose

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 482-482 · spoken_turn

> again I'll repeat. So first console.log a comes to call stack, it'll be waiting, then set timeout comes and it'll be waiting, like it'll go to whatever the delay that's supposed to execute, then console.log b comes and start executing. And then like console.log d comes, then finally execution starts. If execution happens that way, then the d will be printed first, because it's a stack, right? It's a pile of plates, one one on top of another. So you have to take the top plate first, followed by the next. Correct? If you do that, then what would happen?

**vasanth** · lines 486-486 · spoken_turn

> whatever came in the last will be running first which is totally opposite to how a programming language should work okay the call stack is a stack only because it holds the function references like I explained here okay so let's say function A you are calling A A is calling B we will call C we have a chronological order of calling the function one after another so we are using the stack to maintain that order okay and coming to the simple example that I was saying
