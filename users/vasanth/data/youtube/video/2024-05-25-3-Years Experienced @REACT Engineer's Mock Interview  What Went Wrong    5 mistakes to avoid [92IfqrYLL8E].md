---
id: 92IfqrYLL8E
title: '3-Years Experienced @REACT Engineer''s Mock Interview: What Went Wrong? |
  5 mistakes to avoid'
url: https://www.youtube.com/watch?v=92IfqrYLL8E
date: '2024-05-25'
duration: 00:30:37
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 3
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
---

# 3-Years Experienced @REACT Engineer's Mock Interview: What Went Wrong? | 5 mistakes to avoid


## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to career with person youtube channel my name is wasan the previous channel was known as uncommon geeks as you know this is a video series where i am doing a lot of mock interview with me today i have madhan more about madhan madhan himself will be telling so this is a mock interview where it's gonna be purely based on javascript we are gonna discuss two fundamental javascript questions for next 30 minutes like i always say the best way to utilize this mock interview is like after i ask a question pause the video answer or solve the problem whatever i give

### 00:00:30 · Speaker 1

then resume the video and see whether your answer and answer given by mother is matching and at the end of the video i'll try to give answers to all the questions that mother might have given a wrong answer or if he's given a right answer probably i will tell what was right or what was wrong so that you can get yourself clarified so make a best use of this and if you're not subscribed to my channel carry this person please subscribe and like the video you'll not regret it and let's start now mother can you please introduce yourself

### 00:00:54 · Speaker 2

Yeah, hi everyone. So my name is Madhan. I did graduated in 2020. I did I'm from computer science background. So I have totally three and a half years experience working in JavaScript. So I have experience working in full stack applications as well. And currently I'm working as a front end developer.

### 00:01:18 · Speaker 1

Wonderful, wonderful Madhan. So Madhan, which place you are from?

### 00:01:24 · Speaker 2

I'm from Turchia as well

### 00:01:26 · Speaker 1

Richi is in Tamil Nadu correct

### 00:01:28 · Speaker 2

Yeah yeah so

### 00:01:29 · Speaker 1

Okay, sure. If any audience watching and there from Tamil Nadu, please comment for the session, comment in the add a comment. So I've shared a link with you Madan and open that link, close any other tabs that are open. Just open this tab and present your screen. Let's get started. It is time to answer.

### 00:01:43 · Speaker 2

The screen is visible

### 00:01:45 · Speaker 1

Yes now it's visible okay so Madan let's start with some extreme basics

### 00:01:45 · Speaker 2

Yes I know what she means

### 00:01:50 · Speaker 1

Okay, maybe let the zoom be there. Give one control plus, it'll be easy for the audience to see.

### 00:01:58 · Speaker 1

Yes. So tell me like what are polyfills modern?

### 00:02:06 · Speaker 1

Have you heard the term polyfills P-O-L-Y F-I-L-L-S polyfills

### 00:02:09 · Speaker 2

You

### 00:02:12 · Speaker 2

All of us are nonsense

### 00:02:14 · Speaker 1

You might have you're not heard also okay see

### 00:02:17 · Speaker 2

I have heard about it yes

### 00:02:18 · Speaker 1

Yes, yes, sure. See, another way to put that it's like the most common term that I use obviously the custom implementation of the bulletin methods. Okay. For example, they'll ask you to write like polyfill for array.map, array.reduce, array.forage. Have you ever encountered those questions or have you practiced them?

### 00:02:38 · Speaker 2

Uh yeah, got it. Uh yeah. So yeah, mainly we will be uh I have a written few polyfills for array methods actually. Wonderful.

### 00:02:47 · Speaker 1

Wonderful wonderful if I ask you to write you sh will you be able to write

### 00:02:51 · Speaker 2

Uh yes uh some basic uh questions like

### 00:02:54 · Speaker 1

Sure, sure. Now we'll go to the writing part first, but you tell me, definitely a concept itself cannot be created for the interview, correct? The polyfill as a concept is definitely not introduced for somebody to ask in the interview, correct? It might have some other significance. So where I'm coming from is, can you tell me why are polyfills essential?

### 00:03:14 · Speaker 1

Or it is a custom implementation for a built-in method right why it is necessary

### 00:03:14 · Speaker 2

Very difficult

### 00:03:19 · Speaker 2

So uh yeah I got it so um

### 00:03:25 · Speaker 2

Right now, the array methods which we have doesn't actually may not match with our business logic or okay sometimes. So when we are working in our projects, so everything has some standards, right? Every software. So maybe there some developers might have implemented array methods. I mean custom implementation for this and

### 00:03:55 · Speaker 2

They might use their yeah

### 00:03:57 · Speaker 1

I agree. So one reason could be like whatever you want that may not exist already. So you built, right, add your own, correct? Definitely that is a use case. But with my experience, it has never happened. Has it happened to you? Like where you wanted something and that has never existed in the built-in library? Has it ever happened?

### 00:04:13 · Speaker 2

Uh yeah yeah yes I have I do haven't used it

### 00:04:17 · Speaker 1

Yes, sure. I mean, you're telling you also never encountered a scenario, correct? Where you wanted a built-in function and that doesn't exist. Anyways, because it may not be that way. All of us try to achieve what we want using the built-in methods. That's the usual tendency, correct? So that could be one reason, obvious reason, okay? Any other reason that you can think of, Madhan? Okay, let's start with a very extreme simple example, Madhan. Okay, like array.map. Right now, first write array.map and give me a small example, not polyfill.

### 00:04:47 · Speaker 1

the array documents

### 00:04:49 · Speaker 2

Sure I think so let me create a dummy array

### 00:04:55 · Speaker 2

So for now, I will use this map method and inside this, I will have one array element. So I will use this as an arrow function. Here I will...

### 00:05:11 · Speaker 2

return this array array element into two so I will implement multiply

### 00:05:26 · Speaker 2

This is uh multiply by two. So if I lock this I will be getting an output uh two four and a six

### 00:05:35 · Speaker 1

Mm it does

### 00:05:36 · Speaker 2

Yeah

### 00:05:38 · Speaker 1

Mm

### 00:05:38 · Speaker 2

So basically this is creating a new array keeping this as an absolute one.

### 00:05:45 · Speaker 1

Yeah then I'm sure you are aware of the difference between map and forage. What is the difference?

### 00:05:49 · Speaker 2

Yeah forage doesn't actually create a new array map actually creates one new array

### 00:05:55 · Speaker 1

Absolutely. Tell me a scenario like when we'll use a forage and when you will use map like try to come up with some practical scenario to just to differentiate.

### 00:06:04 · Speaker 2

So uh yeah for each okay you you need some practical examples

### 00:06:09 · Speaker 1

Mm yeah if you know please tell me yes

### 00:06:11 · Speaker 2

Oh

### 00:06:14 · Speaker 2

Uh yes, I don't have one practical example, but the ideal scenario is when we just wanted to iterate over the array and uh do some calculations we will go with for each, but we need to uh get on a new array out of that array something, then we will be going with map.

### 00:06:37 · Speaker 1

Okay, sure, sure. We'll get into these polyfills in a while. Okay, I'll share a small code snippet with you in the chat section. Okay, and I want you to look at the snippet and guess the output.

### 00:06:45 · Speaker 2

And uh I want to

### 00:06:50 · Speaker 2

Yeah sure

### 00:06:51 · Speaker 1

Copy the code and put in the chat section and for the even the audience whoever is watching this you also just look at the snippet and pause the video and try to guess the output.

### 00:07:01 · Speaker 2

so we will be removing this top yes so look at it carefully

### 00:07:04 · Speaker 1

Look at it carefully. Take one to two minutes. Okay. And at the end of the day, I'm not expecting the right answer. I'm expecting a right explanation. So you tell the output and I will not give you 100 marks. I just want you to give a right explanation for that. Okay.

### 00:07:14 · Speaker 2

And uh

### 00:07:20 · Speaker 2

Yeah sure

### 00:07:25 · Speaker 2

Set time out it is actually an asynchronous browser API then we have a promise resolve

### 00:07:34 · Speaker 2

and okay okay listen i have

### 00:07:37 · Speaker 1

Yeah tell me what is output

### 00:07:40 · Speaker 2

so the output will be first this start log will be printed okay then we have set time out this is actually this will be going into this uh uh macro task and we will be the control will be reaching to line number five so here the promise is resolved immediately so inside promise will be logged then we will be uh the end will be printed then we this set time out log inside set time out

### 00:08:10 · Speaker 2

Printer

### 00:08:11 · Speaker 1

Good. So start inside promise and end followed by inside set timeout, correct?

### 00:08:17 · Speaker 2

Yeah yeah

### 00:08:18 · Speaker 1

start inside promise and an inside timeout correct

### 00:08:21 · Speaker 1

Can you please run the code we will check start

### 00:08:21 · Speaker 2

Okay okay please

### 00:08:23 · Speaker 2

Okay

### 00:08:24 · Speaker 1

end inside promise and inside set timeout you can you can still like it's no problem you tell me why do you think like this output is coming

### 00:08:33 · Speaker 2

Yeah, okay. So one thing for sure, set timeout, this will be moving to macro task. And this promise is also, I think it's actually an asynchronous operation. So that's why it's getting logged after all the synchronous tasks are over.

### 00:08:50 · Speaker 1

exactly so it may not be like uh giving the answers at the early like it's not a process synchronously correct

### 00:08:58 · Speaker 2

Okay yeah okay correct

### 00:08:59 · Speaker 1

Okay, sure. Let me share another snippet with you. So I'm sharing the snippet here. Again, copy page the snippet and if you you can comment the snippet or even if you remove the snippet also no problem. I can share with you after the recording the all the that I've asked you.

### 00:09:15 · Speaker 2

Yeah sure

### 00:09:16 · Speaker 1

yeah even the audience also look at the snippet try to guess the output for this

### 00:09:21 · Speaker 2

So I think this is kind of a closure. So one, we will be, control will be reaching into this first outer function is called. So inside outer function, we are logging one. And then we have one another function called inner. So we are calling this inner function. Inner function will also be logging one. And then we are setting this variable x to two.

### 00:09:51 · Speaker 2

Okay, we already have variable named x equal to 1. So I think there is a possibility this might error on 8, but if not the error case, the output will be 1 and 1.

### 00:10:09 · Speaker 1

So we have two console.log. I'm calling the outer function and inside outer function, in line number three, we are logging it. And then the control would come to line number seven, where we are calling the inner function. Both the places we are logging the value of x only, correct? Yeah. So in line number three, you are saying what will be the output?

### 00:10:23 · Speaker 2

Yeah so in line number three

### 00:10:27 · Speaker 2

Line number three the output will be one okay

### 00:10:32 · Speaker 1

Okay

### 00:10:33 · Speaker 2

And here as well the output will be one. Then only we are logging actually x equal to two. But if this suman is called after line number eight, this could have been two.

### 00:10:47 · Speaker 1

Okay run the code let us see

### 00:10:53 · Speaker 2

defined

### 00:10:55 · Speaker 1

Okay again like I told you can still check why it is undefined

### 00:10:55 · Speaker 2

like a tool

### 00:10:58 · Speaker 2

outer function is called

### 00:11:03 · Speaker 2

This is actually an uh, this has the global scope. So I don't have clear explanation. Okay.

### 00:11:12 · Speaker 1

Yeah, this is something to do with the hoisting, okay? Concept of hoisting. So you tell me, explain more about hoisting. Just let's stick to variable hoisting. Tell me how the variable hoisting works.

### 00:11:23 · Speaker 2

So there are actually three parts actually where a variable can be hosted at the global phase of one particular script, function level, and then the block level.

### 00:11:40 · Speaker 2

So uh yeah and also there are

### 00:11:41 · Speaker 1

No so there are I'm coming from is uh explain me like the hosting with respect to variable right variable with the const whether it's hosted where and electric how they're hosted please explain

### 00:11:47 · Speaker 2

We got it

### 00:11:51 · Speaker 2

Okay, so let and const have a block scope. So it cannot be actually, if we declare a variable inside a block with let or const, and if we try to access it outside that block, we will be getting an undefined or an error out. But there is actually globally posted and it can be accessed anywhere.

### 00:12:19 · Speaker 1

So where is your global heartshot so you can access from anywhere you are saying manthan am i right

### 00:12:24 · Speaker 2

Yeah correct very good

### 00:12:25 · Speaker 1

So let's say there is a function block like line number two to line number nine. Okay. So there is a bad keyword inside that block.

### 00:12:30 · Speaker 2

So that is a vacuum

### 00:12:32 · Speaker 1

So whether that variable is accessible throughout the block

### 00:12:33 · Speaker 2

And then

### 00:12:37 · Speaker 2

uh got it so the function is actually also holstered the functions are also actually posted by the time of this uh declaration of this outer function this where keyword is not actually uh declared that's why we are getting the error undefined

### 00:12:56 · Speaker 1

No, you're not getting an error. You're not getting an error. Okay. So you, you told about let and const hoisting, right? Tell me about variable hoisting, variable created with the var keyword is hoisted or not.

### 00:12:56 · Speaker 2

You're not getting an edit

### 00:13:06 · Speaker 2

So uh yeah variable with back element is hosted

### 00:13:10 · Speaker 1

Okay, variable contributed to where keyword is hoisted, correct? And what is the difference then between let const and where hoisting?

### 00:13:18 · Speaker 2

So yeah as I mentioned let and const have a block scope where has that a global scope

### 00:13:24 · Speaker 1

I'll tell you another difference along with that a variable created with var keyword is hoisted and initialized with a value of undefined

### 00:13:31 · Speaker 2

Oh okay

### 00:13:33 · Speaker 1

Is that true or not

### 00:13:33 · Speaker 2

True or not

### 00:13:36 · Speaker 2

So that is by uh by uh by analyzing this function I think you are right actually

### 00:13:44 · Speaker 1

correct correct see undefined is not an error for you and the audience also i'm saying undefined is a value that expected value in this case

### 00:13:52 · Speaker 1

Sure. So you can stop sharing, Amadhan. Okay. So now let us understand like some some fundamentals of JavaScript. Let's say now I want you to know how the JavaScript engine works. The fundamentally, right? Let's say you wrote a code, same code, whatever we wrote just now, and we want to execute that code. Tell me step by step operations, what will happen behind the scenes to execute the code.

### 00:14:16 · Speaker 2

Uh, okay. So, um, yeah, uh, if we consider one script, a main JS script or something, so, um, the functions will be actually, uh, declared. So there will be few functions and variables, let's say. So the variables and functions also will be declared. Upon calling that, uh, one of the function, uh, the control will be going to that function.

### 00:14:46 · Speaker 2

and doing that operation so it will be executed line by line and the synchronous javascript codes

### 00:14:54 · Speaker 1

No, correct. This is at a very, very high level. So I just wanted to understand a little bit in depth. I'll give you some hints probably where I'm going at mother. Okay. So whenever we have a JavaScript code, first it goes to a parser. A parser will generate an abstract syntax tree and then the further execution goes. Any chance you are aware of this flow?

### 00:15:14 · Speaker 2

Uh

### 00:15:15 · Speaker 1

Okay, please read it. You and the audience who is watching, you can read more about this particular concept by going to the MDN official documentation. Okay. So tell me, what is callback hell Madan?

### 00:15:15 · Speaker 2

Please state it

### 00:15:24 · Speaker 2

Tell me

### 00:15:28 · Speaker 2

callback hill okay yeah so the prod the problem with this callback hills are actually the codes will be a little bit messier to uh read actually and adding any features on changes on top of it will be a bit difficult but uh and it is actually used to perform some asynchronous operations

### 00:15:55 · Speaker 1

Give me an example for callback, Alec. What is, or can you give me one simple example?

### 00:16:02 · Speaker 1

So call back in

### 00:16:02 · Speaker 2

Back in

### 00:16:04 · Speaker 1

No problem. I'll ask you another simple question. Okay. Tell me what are promises in JavaScript?

### 00:16:05 · Speaker 3

Yeah

### 00:16:12 · Speaker 2

So yeah, promises in JavaScript is actually used to handle asynchronous operations. So that's why we use promises.

### 00:16:23 · Speaker 1

I don't want a bookish definition but give a very basic definition that you have understood what are promises

### 00:16:29 · Speaker 2

Okay, so promises are generally used to fetch any service data HTTP calls or one main special common use cases may be this one.

### 00:16:44 · Speaker 1

promise will that's not the exact definition you go and read after the interview okay so you are you aware of something called promise.all in javascript

### 00:16:53 · Speaker 2

I promise at all I know I have

### 00:16:55 · Speaker 1

Okay sure are are you aware of what are called higher order functions in JavaScript

### 00:16:59 · Speaker 2

Higher order functions uh yeah I have uh heard of them tell me what are

### 00:17:02 · Speaker 1

Tell me what are higher order functions

### 00:17:05 · Speaker 2

So, there can be few functions actually. Let's say some inner functions actually. But we want to actually do some modification to functions. Maybe I can put it as we have YouTube, right? YouTube application. In YouTube application, there will be grids actually. Many grids will be present, video grids.

### 00:17:35 · Speaker 2

In that add section alone, we will be having a few additional changes added on top of it. Okay. That might have been created with the higher order functions. Yeah.

### 00:17:47 · Speaker 1

Yeah, I mean what you're saying is not fully wrong, Madan. All I want is a somewhat basic definition. What do you think higher order functions are? One basic definition, like not bookish one. Like you can give anything that you have understood, right? That way only you can narrate. Tell me what is higher order functions.

### 00:18:04 · Speaker 2

Adding some special capabilities or additional features to one common function is what I mean higher order functions and similar to higher order components as well

### 00:18:22 · Speaker 1

Okay, not not fully correct. Again, this also you can go and check after the interview. Okay. So you know what is what are prototype chain in JavaScript.

### 00:18:30 · Speaker 2

Prototype chain or prototypes

### 00:18:32 · Speaker 1

Or prototypes in general do you know what are prototype or prototypical inheritance

### 00:18:35 · Speaker 2

Uh no I'm not having to no problem

### 00:18:37 · Speaker 1

No problem no problem you hope your average call apply by tomorrow

### 00:18:40 · Speaker 2

yeah it comes under a prototyping yeah

### 00:18:44 · Speaker 1

Yeah no yeah I mean but in general also it's a very common interview topic will you be able to write an example for call apply and bind

### 00:18:52 · Speaker 2

Uh no something I need to

### 00:18:54 · Speaker 1

No problem no problem okay so

### 00:18:54 · Speaker 3

No problem no problem okay

### 00:18:56 · Speaker 3

Okay

### 00:18:58 · Speaker 1

No, no, no problem. Like, like, I always say this, right? Interview is just a game. There are things that you know. There are things that I know. If you are lucky, then you will know what I know. That's all. Correct? Like, let's say you start taking the interview. I'll also not able to answer some questions. Correct? So, whatever from my understanding and what is the commonly asked interview question, right? From that, I'm trying to ask some questions primarily. Okay? Now, let's go back to the same question that I asked. Now, present your screen and write a polyfill for RA.map method and we'll end the interview. Then I'll give my feedback. And for audio.

### 00:19:28 · Speaker 1

who want to write and don't know how to get started with polyfills there is a series of mine dedicated for writing polyfills i'll put the link in the up as well as in the description section please go ahead and check polyfills basically are like he told creating the custom implementation for built-in methods okay so even i i have written implementation for map method also

### 00:19:58 · Speaker 2

I think uh I need to actually

### 00:20:03 · Speaker 2

a refresh on this topic

### 00:20:05 · Speaker 1

You want to refresh the browser

### 00:20:07 · Speaker 2

Oh no I need to refresh on these topics

### 00:20:10 · Speaker 1

You want to refer to the concept is it Ok sure

### 00:20:10 · Speaker 3

to refer to the content

### 00:20:13 · Speaker 1

stop sharing madam let's let's get uh get i'll give my relief for whatever we have had so far but just before i give my honest feedback about whatever i interacted with you so far if you have any questions in your mind please tell me madam

### 00:20:25 · Speaker 2

Uh no Santa I think uh this is actually uh good uh I uh got on where I stand so yes I think I need to refresh the content

### 00:20:32 · Speaker 1

Yes I think

### 00:20:34 · Speaker 1

Yes, yes, sure. No problem, Madan. Like I told, like there's a different level in the interview preparation. Like whatever the level that you know, you can clear some interview, but there's some levels that you need to prepare for clearing some other interviews, correct? So I'm gonna, like, like you already told, my honest opinion is like this way, Madan. This might applicable for even the audience who is watching. So fundamental concepts of you, Madan, whatever you know, you know it well. like whatever the concept that you know to a large extent you know it well but there's some concept which you don't know or you barely

### 00:21:04 · Speaker 1

know like for example uh the hosting question that i asked you know what is hosting but uh whenever i barely you know like you don't know completely so only you're not able to predict the output for the given snippet correct and even on the the whatever the array dot map polyfill that i asked right so don't do this mistake in the interview whenever you're not so comfortable you're writing so pick up those question where your probability of answering at least 70 percent you think you will be able to solve it otherwise there will be definitely a negative mark

### 00:21:34 · Speaker 1

you not picking opting for a question but you opt and don't answer then it's going to be fully negative instead you can say like probably i don't know at the moment roughly i know if you want me to do write the skeleton i'll be able to write but i'll not be able to write it fully okay that way you can put instead of like accepting a problem and like not solving it and also like do not debug live like this this is applicable for you and the audience are watching like this the way you start debugging i've told in multiple times in my videos where you whenever you start debugging it creates an impression you're not confident

### 00:22:04 · Speaker 1

about your code mother uh i mean i'm not saying like we will not make mistake like in the day-to-day activity everybody do the debugging like this only in interview instead of debugging this way try to do the mental debugging uh like let's say you go to one level of logging not a problem don't put into like multiple level of logging and debug point etc try to do that in mind mapping and try to get probably where you're going wrong all right so that gives you like more confidence to the interviewer like mother is really aware of the concepts maybe small mistake he did so he's able to come up with a solution

### 00:22:34 · Speaker 1

that to that by putting couple of log statements okay don't get like too much too much of a debugging in the interviews

### 00:22:42 · Speaker 2

Yeah sure and

### 00:22:43 · Speaker 1

and uh yeah these are that a very very high level mother and some concepts like i asked you right like for example a prototypical inheritance call apply bind promise uh callback hell and all of and promise definition see all of these are like extremely basic question mother and i don't think you are gonna get away without answering these questions in the interview so you have to learn and there's no escape for this so whenever you are free please read these questions carefully before going to the next interview okay any other closing notes mother

### 00:23:13 · Speaker 1

Have any questions or yeah

### 00:23:14 · Speaker 2

yeah only one question so even though if we if i learned the uh i mean the real-time implementation so you asked about promises and prototype call i play blind has well right even though i know the concepts and know to code that i also need to know that the real uh definition of that correct yes okay i'll give you

### 00:23:35 · Speaker 1

Correct. Yes. Okay. I'll give you a framework to actually read to you and again, published audience also. The framework of reading every concept is very simple. Read the concept and understand the basic definition. So this basic definition is very essential because see, what is hoisting? Hoisting, the people give a lot of definition, like a moving declaration on top of the block, et cetera. So the ideal definition is JavaScript engine. because of this concept of like two-part execution, right? It appears to move declaration to the top of the block.

### 00:24:05 · Speaker 1

See, there is a difference in APS to move declaration and move the declaration to the top of the block, correct? So, people say like a white definition is not like a graduate students. It is necessary because you understand the concept very clearly. So, first is definition. Second is a bookish example. Bookish example means the one on the MDM. the very basic one you understand that third one is a practical example for your experience of around two to three point five years practical examples are not like very critical but somebody who's having five plus years they need to should be able to give practical example no

### 00:24:35 · Speaker 1

will ask you hosting like you create like variable x and try to do console.log and tell x and x that is not an example for five plus years like you know the concepts where did you use it correct for example closure everybody know inner function has access to outer function variable that is not the use right so you are not learning for interview where you use it in your project so one definition one practical example one bookish example if you learn these three for every topic that you are studying you should be good for interview as well as your day-to-day work

### 00:25:04 · Speaker 2

Yeah I'm sure

### 00:25:05 · Speaker 1

okay sure so it was very nice talking to you mother like i got to know a lot about you and whatever the interview question that i ask every interview i feel like a lot of learning for me also i assume you also like the session now mother

### 00:25:18 · Speaker 2

Yeah some tips are helpful I gotta know where I stand actually

### 00:25:21 · Speaker 1

Yes, thank you so much, Madhan. So for audience who have watched the video and whoever were able to answer all the questions that I asked, wonderful. If you don't know the answer, like I'm going to answer all the questions that I asked in the next part of the video. And if you not like the video, please like and subscribe to my channel and comment. Thank you so much. I'll watch you in the next video. So I think you have already watched the session with Madhan. And in this particular short video, post video where I'll be primarily explaining your answers to all the most of the questions that I asked. Okay. Let me start the explanation. I'll not be answering.

### 00:25:51 · Speaker 1

every basic question that I asked, but primarily around the questions on the snippet driven or some of the important question that I asked in the video I'm trying to answer here. So this was the first snippet that I asked for Madhan. So if I run the code, the output for this is, I'm running the snippet. So the output for this, as you see, like it's start, end, inside promise and inside set timeout. Okay. The answer that Madhan had given, initial answer was he had not considered, he had given in a different order, like start, end, and then he told inside,

### 00:26:21 · Speaker 1

Sorry, he had told start inside promise, then end and inside timeout. Because we consider like promise.resolve is resolving immediately. Let's consider that as the next thing to be printed. But right answer is whatever you are saying. That is start, end, inside promise and inside timeout. The reason for is very simple. Like I've told in multiple other videos of mine also, where inside promise is basically executed first because it is an asynchronous task. And even set timeout,

### 00:26:51 · Speaker 1

also is an asynchronous task okay so whenever basically the browser or the js engine encounter this particular the promise line it will be executing that in asynchronous way as it is already resolved it's going to be executed first compared to the set timeout okay so that's a simple explanation for this so keep this in your mind okay and another snippet that i've given to madan was this i've tried to explain this to a certain level in the uh in the video itself but i'm just giving you a little more explanation here so variable kit

### 00:27:21 · Speaker 1

with where keyword is hoisted and initially with the default value of undefined correct so variable created with latin cons are also hoisted but they are not issued with any value so you cannot use them unless they are declared as simple as that okay now if you look at this block i am calling a function called outer here and inside which in line number five i have a console.log and in line number six i have an inner function in line number nine i have a method called inner okay and line number 10 i have variable x equal to two so if you look at a block from line number four to line number 11 i have a

### 00:27:51 · Speaker 1

variable called variable x okay and like i told whenever you have a variable inside a block that variable will be hoisted and the value of that variable will be initialized with a value of undefined only variable with wire keyword so anywhere in this block if you want to access the variable x you can access so the value of x would be undefined so there is also variable outside this corporate line number three that's the global variable whenever we have a global variable and a local variable always the prior is given to the local variable let's say local variable

### 00:28:21 · Speaker 1

is not there then the period will be given to the global variable so let's say if i run this code undefined why both are undefined is so in this entire block it knows the value of x as it has not come to line number 10 and line number 10 is the last line so that where the actual definition or variable x getting defined till that all are actually it is only declared with a value of undefined so here also it is 2 and here also it is undefined here also it is undefined let's say if this is not there then both

### 00:28:51 · Speaker 1

Both of them I might have printed the value of one. Okay, as you can see here. Now, the other important question that I asked in the interview was like polyfills, correct? So I asked like, what are the reasons for creating the polyfills? One right isn't he already gave in the video that we write the polyfills because let's say there is some implementation not readily available. We will use the polyfills for that. That is a right. But in most cases, that is not true because whatever you want is most of the cases are available. The ideal reason why we would use polyfills is

### 00:29:21 · Speaker 1

there are browsers which don't support the newer methods of whatever is coming in. Let's say we have a explorer and we have a new function that has been introduced and that particular function may not be supported in the old browser. In such situations, we'll try to mock those behavior by writing the polyfills. So remember this. And I ask you to write a forum custom implementation of array.map method that I've clearly explained in my playlist. So we're writing the custom implementation for built-in methods.

### 00:29:51 · Speaker 1

array.map itself i've written here i've opened the video i'll try to put this link somewhere in the description also in the seven the top of the video so please check this out another thing that i was asked in the interview was regarding the hosting concept that i've already explained but you want to understand hosting in detail you can go and check out this particular playlist document again i put this link also in the in the screen as well as in the chat section description section please go ahead and check it out and all the other question that i asked like prototypical inheritance closure related questions all of them are like readily available in this playlist this is the one place that you

### 00:30:21 · Speaker 1

refer 31 videos where you will should be able to clear most of the interview okay in this playlist please refer again i'm going to put this in chat section on also on the top of the screen thank you so much for watching if you still have any questions that are unclear for you mention that in the comment section i'll be more than happy to answer them thank you so much catch you in the next video

