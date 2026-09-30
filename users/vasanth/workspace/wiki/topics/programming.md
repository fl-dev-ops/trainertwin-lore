# programming

> Source-local records, not independent fact verification. Original steps and qualifications are retained.

<a id="record-56df6833a6e8bcde"></a>
## Use of System Time for Accuracy

**Product:** knowledge · **Type:** offering · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- Interacting with system time using device crystals like quad crystal may improve timing accuracy in programming.
  - “because there are crystals that are moving even when you close the laptop.” — [lines 1114-1114](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000266`)

### Original context

**vasanth** · lines 1114-1114 · spoken_turn

> because there are crystals that are moving even when you close the laptop. Quad crystal is one of the most popular crystals that is used. There are many other crystals as well. Correct? So if there is anywhere we could use that device crystal capability, that could be somewhere but I haven't explored that deep. Only then we could make the timer very accurate.

**unknown speaker** · lines 1118-1118 · spoken_turn

> ओके, थैंक यू

<a id="record-7f6f41ff1642916c"></a>
## Synchronization in Event Loop

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- In JavaScript, until the call stack is empty, no macro task or micro task is picked for execution.
  - “until the call stack is empty, no macro task is picked or no micro task is picked” — [lines 986-986](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000234`)

### Original context

**vasanth** · lines 986-986 · spoken_turn

> understood this correctly. That means until the call stack is empty, no macro task is picked or no micro task is picked, right? So what do I mean by call stack is empty? So let's say there is certain uh synchronous activity that's happening. I gave an example of for loop, right? Let's say you are running a for loop for a million times. Definitely it's going to take some time. Correct? Arpan. So by that time that much time is taken, uh you you also have written a set interval which is supposed to execute every one second. Now that has to be ideally picked from the the macro task queue, the macro task queue, but it has not been picked because call stack is busy.

**vasanth** · lines 990-990 · spoken_turn

> until the call stack event loop event loop would nudge. But call stack until it is free it wouldn't pick anything here. So you expected it to run after one second but call stack got free after two seconds. Now it will pick the things from the micro macro task queue.

**unknown speaker** · lines 994-994 · spoken_turn

> Got you, got you.

**vasanth** · lines 998-998 · spoken_turn

> Correct? So but it may not be a usual case honestly. Like nobody would write a follow up with a million values, right? That is the assumption with which JavaScript is built.

<a id="record-1501407b9751ba46"></a>
## Choice of Technology for Critical Timing

**Product:** knowledge · **Type:** advice · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- For applications requiring precise timing, JavaScript may not be suitable and reliance on backend or other technologies that depend on accurate time sources like crystals may be needed.
  - “Like uh let's say we want to build something like a timer that has required for example space mission and all right. So there has to be like super critical.” — [lines 1154-1154](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000276`)

### Original context

**unknown speaker** · lines 1150-1150 · spoken_turn

> Yeah, so not related to JavaScript. If something is related to use case, like if we can't build some application which is most accurate with JavaScript, at that point of time we need to choose some other languages or anything, right?

**vasanth** · lines 1154-1154 · spoken_turn

> This is a good question Anas. Like uh let's say we want to build something like a timer that has required for example space mission and all right. So there has to be like super critical. Like you cannot even a millisecond delay is not acceptable. In such situations I would say definitely the client JavaScript is not should not be the approach for you. So what you could do is you could have certain time that you reline back end or some time which comes from the crystal that they're looking for. If you read about a time it's a very very interesting subject.

**unknown speaker** · lines 1158-1158 · spoken_turn

> So there has to be

**unknown speaker** · lines 1162-1162 · spoken_turn

> in

**unknown speaker** · lines 1166-1166 · spoken_turn

> approach for you

**vasanth** · lines 1170-1170 · spoken_turn

> So quad crystal I told you basically it's a crystal that resonates at a frequency today if you see most watches have that crystal that that that whatever the frequency at which it is resonating that we are considering as a second. So if you use some other crystals which are more accurate than quad we might get more accurate time. So if it's a very time critical then they will have that way of like basically ideal implementation of this to answer your question should be running the back end. And those back end should be deriving their time from some crystals like this. Like which are like giving the very accurate frequency for their use cases.

<a id="record-1cc412ae0616aa35"></a>
## JavaScript Event Loop Architecture

**Product:** knowledge · **Type:** claim · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- In JavaScript's architecture for the event loop, the call stack has the highest priority, followed by a micro task queue and a macro task queue.
  - “From the architecture point of view if you see, this is our architecture of the overall event loop, right? So, call stack has the highest priority, followed by we have, here I've written call by queue and priority queue, but here we have like micro task and macro task.” — [lines 982-982](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000233`)

### Original context

**vasanth** · lines 982-982 · spoken_turn

> Yeah, why it cannot be accurate I told, right? From the architecture point of view if you see, this is our architecture of the overall event loop, right? So, call stack has the highest priority, followed by we have, here I've written call by queue and priority queue, but here we have like micro task and macro task, your common convention. So we have a call stack, we have a micro task and micro task queue. So the order of the execution you you guys already saw, like how it will executed is, first call stack must be empty, executes all micro task, executes one micro task, repeat the cycle.

**vasanth** · lines 986-986 · spoken_turn

> understood this correctly. That means until the call stack is empty, no macro task is picked or no micro task is picked, right? So what do I mean by call stack is empty? So let's say there is certain uh synchronous activity that's happening. I gave an example of for loop, right? Let's say you are running a for loop for a million times. Definitely it's going to take some time. Correct? Arpan. So by that time that much time is taken, uh you you also have written a set interval which is supposed to execute every one second. Now that has to be ideally picked from the the macro task queue, the macro task queue, but it has not been picked because call stack is busy.

**vasanth** · lines 990-990 · spoken_turn

> until the call stack event loop event loop would nudge. But call stack until it is free it wouldn't pick anything here. So you expected it to run after one second but call stack got free after two seconds. Now it will pick the things from the micro macro task queue.

**unknown speaker** · lines 994-994 · spoken_turn

> Got you, got you.

<a id="record-422995608b2bc60d"></a>
## Executing Timers in JavaScript

**Product:** knowledge · **Type:** method · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Summary

- The accurate execution of timers in JavaScript is not predictable due to its design with an event loop.
  - “there is no language as far as I know, something like this where you write a timeout and an interval, but those will not be executed at the duration that you specify because it's not fully predictable.” — [lines 1002-1002](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000238`)

### Goal

- To make timer execution in JavaScript more accurate relative to its inherent inaccuracies.
  - “what we can make probably it we can make it more accurate.” — [lines 1078-1078](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000257`)

### Prerequisites

- Understand that JavaScript's timing execution is inherently imprecise due to its architecture.
  - “JavaScript is not unlike C or C++, you cannot fully predict it.” — [lines 1002-1002](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000238`)

### Steps

1. Run an interval at a short duration, such as every 100 milliseconds, to increase the chances it executes on time.
  - “you will run it at every hundred millisecond.” — [lines 1086-1086](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000259`)

2. Use a date object within the interval to track time and adjust the next interval based on any differences.
  - “you can have some date object used within that interval so that like you could check the start date and end date.” — [lines 1086-1086](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000259`)

### Constraints

- It will not make the timer 100% accurate, just relatively more accurate than traditional approaches.
  - “But will it make it 100% accurate? No, relatively more accurate.” — [lines 1102-1102](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000263`)

### Exceptions

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 1002-1002 · spoken_turn

> I think, uh, if if probably there is no language as far as I know, something like this where you write a timeout and an interval, but those will not be executed at the duration that you specify because it's not fully predictable. JavaScript is not unlike C or C++, you cannot fully predict it. But I think it is under the basis of the same programming, a real or a same programming would not be done that way. Without assumption, the JavaScript works well in most cases. So anything around the time, anything around the accuracy, you have to put additional effort.

**vasanth** · lines 1006-1006 · spoken_turn

> Also one more small point in interview if you look the if you think the problem is very easy for the company you applied. Like the one I gave right? Can you build a timer which is accurately? So then see there is some catch.

**vasanth** · lines 1010-1010 · spoken_turn

> probably like if you're applying for a company that is not paying you well or anything like that then probably the question might be simple. But if you think there's a disproportionality in the question and the company and the salary then there is something that is hidden meaning in the question. So like go through it two three times and you can ask interviewer to get the questions clarified. Like hardly anybody asked me what is accurate in the question. If they were asked like then I have to explain then there's high chance they at least try in the right direction.

**vasanth** · lines 1014-1014 · spoken_turn

> Okay. Now, are there any questions? Otherwise, we have a small quiz, maybe a matter of ten minutes small quiz followed by we can take a five minutes break before I go to the next topic.

**vasanth** · lines 1018-1018 · spoken_turn

> Any questions?

**unknown speaker** · lines 1022-1022 · spoken_turn

> So Vasanth, if you have pen, micro

**unknown speaker** · lines 1026-1026 · spoken_turn

> we have pen micro

**unknown speaker** · lines 1030-1030 · spoken_turn

> all at once it executes all the ten micro tests then it

**unknown speaker** · lines 1034-1034 · spoken_turn

> come back to call step

**unknown speaker** · lines 1038-1038 · spoken_turn

> then go back to macro, is it a

**unknown speaker** · lines 1042-1042 · spoken_turn

> Okay

**unknown speaker** · lines 1046-1046 · spoken_turn

> Correct

**vasanth** · lines 1050-1050 · spoken_turn

> Correct. First all the things in call stack executed then once the once it comes to the micro task queue everything in the micro task queue is executed and then again it go back to call stack.

**unknown speaker** · lines 1054-1054 · spoken_turn

> But it is not same as macro task. If macro task has ten execution, it is only one thing at a time.

**unknown speaker** · lines 1058-1058 · spoken_turn

> scan

**unknown speaker** · lines 1062-1062 · spoken_turn

> I can

**vasanth** · lines 1066-1066 · spoken_turn

> correct, correct victor, yes, that's how it is built.

**unknown speaker** · lines 1070-1070 · spoken_turn

> actually I want to ask how we can patch the set timeout issue in the store watch

**unknown speaker** · lines 1074-1074 · spoken_turn

> issue

**vasanth** · lines 1078-1078 · spoken_turn

> uh yeah I mean that is something that I wanted to give as a take home assignment but um in in a nutshell Chirag with with my so much of explanation that I did you cannot solve that problem. Okay? Because this is how that was like executes you cannot make it accurate. Okay. You getting my point? So but what we can make probably it we can make it more accurate. That is um you can have an interval for a very short duration so the chances that it executes is quite high and you can

**unknown speaker** · lines 1082-1082 · spoken_turn

> ಓಕೆ

**vasanth** · lines 1086-1086 · spoken_turn

> clarify some differences. I'll give an example. Let's say instead of run, you want to have a timer for one second, okay? Instead of you running an interval for one second, you will run it at every hundred millisecond. So, to achieve that one second of interval, you are running the interval for ten times and you can have some date object used within that interval so that like you could check the start date and end date. If there are any nuance differences, you can try to subtract it and add it to the next interval. Like for example, the first interval was supposed to execute, let's say started from zero, it was supposed to

**unknown speaker** · lines 1090-1090 · spoken_turn

> of India

**unknown speaker** · lines 1094-1094 · spoken_turn

> Clear

**vasanth** · lines 1098-1098 · spoken_turn

> execute at hundred right? Let's say it executed at one hundred and twenty. Now the next interval you could make it eighty millisecond. KDM upon chirag.

**vasanth** · lines 1102-1102 · spoken_turn

> Yes. Yeah. But will it make it 100% accurate? No, relatively more accurate. Okay. Okay. But if there anyone of you can find a way to make it more accurate, I'll be more than happy. I researched a lot, I could not find. Only the I could think of my mind is if there is a way where we could interact with the system time that if you know, right, like today in a laptop, how does actually the time works? There are crystals inside the laptop, right? Even if you're not connected internet, you you even if you turn off your laptop and turn it on, how does always the accurate time

<a id="record-d08e4f5a262bbe92"></a>
## Explaining JavaScript Event Loop

**Product:** expression · **Type:** structure · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- The explanation of the JavaScript event loop's priority structure follows a hierarchy from call stack to queues, discussed in a sequential order of priority.
  - “From the architecture point of view if you see, this is our architecture of the overall event loop, right? So, call stack has the highest priority, followed by...micro task and macro task.” — [lines 982-982](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000233`)

### Purpose

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 982-982 · spoken_turn

> Yeah, why it cannot be accurate I told, right? From the architecture point of view if you see, this is our architecture of the overall event loop, right? So, call stack has the highest priority, followed by we have, here I've written call by queue and priority queue, but here we have like micro task and macro task, your common convention. So we have a call stack, we have a micro task and micro task queue. So the order of the execution you you guys already saw, like how it will executed is, first call stack must be empty, executes all micro task, executes one micro task, repeat the cycle.

**vasanth** · lines 986-986 · spoken_turn

> understood this correctly. That means until the call stack is empty, no macro task is picked or no micro task is picked, right? So what do I mean by call stack is empty? So let's say there is certain uh synchronous activity that's happening. I gave an example of for loop, right? Let's say you are running a for loop for a million times. Definitely it's going to take some time. Correct? Arpan. So by that time that much time is taken, uh you you also have written a set interval which is supposed to execute every one second. Now that has to be ideally picked from the the macro task queue, the macro task queue, but it has not been picked because call stack is busy.

<a id="record-e67e008c1587735f"></a>
## Questioning JavaScript Timer Accuracy

**Product:** expression · **Type:** tone · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- The speaker uses a skeptical tone about achieving timer accuracy in JavaScript, indicating unpredictability.
  - “I think, uh, if if probably there is no language as far as I know, something like this where you write a timeout and an interval, but those will not be executed at the duration that you specify because it's not fully predictable.” — [lines 1002-1002](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000238`)

### Purpose

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 1002-1002 · spoken_turn

> I think, uh, if if probably there is no language as far as I know, something like this where you write a timeout and an interval, but those will not be executed at the duration that you specify because it's not fully predictable. JavaScript is not unlike C or C++, you cannot fully predict it. But I think it is under the basis of the same programming, a real or a same programming would not be done that way. Without assumption, the JavaScript works well in most cases. So anything around the time, anything around the accuracy, you have to put additional effort.

**vasanth** · lines 1006-1006 · spoken_turn

> Also one more small point in interview if you look the if you think the problem is very easy for the company you applied. Like the one I gave right? Can you build a timer which is accurately? So then see there is some catch.

<a id="record-cf198817fa84ff9f"></a>
## Interview Question Strategy Advice

**Product:** expression · **Type:** rhetorical_move · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Observation

- The speaker advises to question the interviewer on the definition of 'accurate' and suggests achieving relative accuracy as a strategy.
  - “try to understand for the question what do they mean by accurate.” — [lines 1138-1138](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000272`)

### Purpose

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 1138-1138 · spoken_turn

> So if if if if the question like if let's say somebody like me ask this question to in the interview Om, my suggestion is like try to understand for the question what do they mean by accurate. So if they ask accurate, then if you could really say I cannot build an accurate clock, then you already are in the right track. But you could only make it more accurate than the traditional approach. That's it.

**unknown speaker** · lines 1142-1142 · spoken_turn

> Okay, got it. Thanks.

<a id="record-1a23c4b4d41b5191"></a>
## Explanation on JavaScript Event Loop Timing

**Product:** cases · **Type:** reported_exchange · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- The speaker describes the event loop in JavaScript and its timing limitations to their audience.
  - “From the architecture point of view if you see, this is our architecture of the overall event loop, right?” — [lines 982-982](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000233`)

### Cue

Not stated in the cited excerpt.

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

- The speaker explains that the call stack must be empty to process further tasks and illustrates with a for loop example.
  - “understood this correctly. That means until the call stack is empty, no macro task is picked or no micro task is picked, right?” — [lines 986-986](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000234`)

### Outcome

Not stated in the cited excerpt.

### Original context

**vasanth** · lines 982-982 · spoken_turn

> Yeah, why it cannot be accurate I told, right? From the architecture point of view if you see, this is our architecture of the overall event loop, right? So, call stack has the highest priority, followed by we have, here I've written call by queue and priority queue, but here we have like micro task and macro task, your common convention. So we have a call stack, we have a micro task and micro task queue. So the order of the execution you you guys already saw, like how it will executed is, first call stack must be empty, executes all micro task, executes one micro task, repeat the cycle.

**vasanth** · lines 986-986 · spoken_turn

> understood this correctly. That means until the call stack is empty, no macro task is picked or no micro task is picked, right? So what do I mean by call stack is empty? So let's say there is certain uh synchronous activity that's happening. I gave an example of for loop, right? Let's say you are running a for loop for a million times. Definitely it's going to take some time. Correct? Arpan. So by that time that much time is taken, uh you you also have written a set interval which is supposed to execute every one second. Now that has to be ideally picked from the the macro task queue, the macro task queue, but it has not been picked because call stack is busy.

**vasanth** · lines 990-990 · spoken_turn

> until the call stack event loop event loop would nudge. But call stack until it is free it wouldn't pick anything here. So you expected it to run after one second but call stack got free after two seconds. Now it will pick the things from the micro macro task queue.

<a id="record-ca1f104d4d76743c"></a>
## Discussion on Interview Timer Question

**Product:** cases · **Type:** recorded_exchange · **Source support:** not_reviewed
**Publication:** 2026-01-13 · **Author:** careerwithvasanth · **Format:** transcript

### Situation

- A participant asked how to create an accurate timer in interviews, questioning the feasibility of the task.
  - “So in the interview you can ask create the accurate timer so we can answer we cannot I mean try to make accurate” — [lines 1126-1126](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000269`)

### Cue

- Participant asks about creating an accurate timer in an interview context.
  - “So in the interview you can ask create the accurate timer so we can answer we cannot I mean try to make accurate” — [lines 1126-1126](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000269`)

### Diagnosis

Not stated in the cited excerpt.

### Strategy

Not stated in the cited excerpt.

### Rationale

Not stated in the cited excerpt.

### Response

- Speaker suggests clarifying the meaning of 'accurate' in the question and admits absolute accuracy isn't achievable.
  - “try to understand for the question what do they mean by accurate. So if they ask accurate, then if you could really say I cannot build an accurate clock, then you already are in the right track.” — [lines 1138-1138](../../../data/youtube/video/2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1JtAHqwKhfM.md) (`youtube-video-2026-01-13-how-to-crack-frontend-interviews-cohort-session-1-1jtahqwkhf-cad8a717e8:u000272`)

### Outcome

Not stated in the cited excerpt.

### Original context

**unknown speaker** · lines 1126-1126 · spoken_turn

> So in the interview you can ask create the accurate timer so we can answer we cannot I mean try to make accurate

**unknown speaker** · lines 1130-1130 · spoken_turn

> accurate time also we can answer we can

**vasanth** · lines 1134-1134 · spoken_turn

> try to

**vasanth** · lines 1138-1138 · spoken_turn

> So if if if if the question like if let's say somebody like me ask this question to in the interview Om, my suggestion is like try to understand for the question what do they mean by accurate. So if they ask accurate, then if you could really say I cannot build an accurate clock, then you already are in the right track. But you could only make it more accurate than the traditional approach. That's it.

**unknown speaker** · lines 1142-1142 · spoken_turn

> Okay, got it. Thanks.
