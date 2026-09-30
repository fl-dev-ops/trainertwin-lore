---
id: skkXL5QdDwk
title: My first question in every front-end developer interview (Hoisting Ep - 1)
date: '2022-02-23'
url: https://www.youtube.com/watch?v=skkXL5QdDwk
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Hoisting is very important concept of JavaScript. Reason for that is, when you\
  \ know what is hoisting in JavaScript, you will definitely know\n\n1. Different\
  \ ways to create variables in JavaScript\n2. Local Scope, Lexical Scope and Global\
  \ Scope\n3. How JavaScript Engine works\n\nSo, just by asking one question, interviewer\
  \ can understand most of your fundamental skills. \n\nMy Medium Blogs - https://mevasanth.medium.com/\n\
  Github URL which contains questions - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  Follow me on LinkedIn - https://www.linkedin.com/in/vasanth-bhat-4180909b/"
author: careerwithvasanth
duration: 00:11:24
model: saaras:v3
transcript: true
---

# My first question in every front-end developer interview (Hoisting Ep - 1)

## Transcript

### 00:00:01 · Speaker 1

Hello all, welcome to Uncommon Geeks. Myself Vasant. I hope you are all doing well. And you know what is today's topic? It's hoisting. Hoisting is considered to be one of the most fundamental topic of JavaScript and it's been very common in most of the interviews. In fact, in recent past I haven't attended an interview where they did not ask me what is hoisting in JavaScript.

### 00:00:21 · Speaker 1

There is a reason why hosting has become so important. Because if you have to answer all questions of hosting, you should have a thorough understanding of how to create variables in JavaScript, what is global scope, what is local scope, how to create a function, how to create a class. So just by asking one question, interviewer can touch base upon multiple skill sets of yours on fundamentals of JavaScript.

### 00:00:42 · Speaker 1

But even after knowing the importance of hosting, many candidates either they will not prepare for this topic or they think they know the answer but they will not be they will face difficulty when some in-depth questions are asked or let's say some variations of the simple topic is asked also they will fail to answer it.

### 00:00:58 · Speaker 1

So in my upcoming videos on hoisting, I'll be covering each and every topic. Just by watching my entire series, I'll guarantee you hundred percent. No matter what question they ask

### 00:01:08 · Speaker 0

ask you related to hosting an interview you'll be able to answer it. Stay tuned let's start the video.

### 00:01:15 · Speaker 1

geek, myself Vasant. So in this video series, we'll be mainly discussing front end developer interview questions. In case if you have not seen my introduction video and directly landed into this, this is not for an absolute beginner. In this this series is for the those candidates who are preparing for the interview on any JavaScript or front end driven technologies, okay?

### 00:01:34 · Speaker 1

Without wasting further time, let's get started with our first topic, hosting.

### 00:01:39 · Speaker 1

hosting uh in in the normal English term as you know refers to something putting on top. The most common phrase that is used is hosting of the flag where the flag moves on to the top of the pole. Okay?

### 00:01:51 · Speaker 1

So with respect to JavaScript, I'll explain what is hosting. Before that, let's see a small example. I'll explain the concept with an example, okay? Hello world.

### 00:02:03 · Speaker 1

Test

### 00:02:05 · Speaker 1

Okay. I'm copying this, I'm pasting here. And let me run this. Okay. So we're getting hello world twice. So let me comment this for the sake of understanding. uh Yeah, we're getting one time the hello world. Now I'm commenting this.

### 00:02:24 · Speaker 1

So we are getting one time the hello world. Okay?

### 00:02:27 · Speaker 1

The reason I I I I showed uh I wrote the function, I called the function from above and below and I commented and I shown you the output is because no matter whether you're trying to invoke the function from line number two or line number six, the JavaScript engine or the compiler is aware of where is the function. This sounds possible because from if you're from any other programming languages like C, you might be thinking yeah, uh uh the compilation is sequential line by line. So it will know that there is a line number three functional number test is there.

### 00:02:57 · Speaker 1

and then from line number six we can invoke it. But this seems quite unnatural. From line number two you're trying to invoke line number three. If it's a sequential execution in line number two it will fail because it is not aware line number three there is a function called test. A function called test. Okay? This is happening in JavaScript mainly because of the concept of hoisting. Where...

### 00:03:16 · Speaker 1

द फंक्शन डिक्लेरेशन्स आर मूव्ड टू द टॉप ऑफ द करंट फाइल और टू द करंट ब्लॉक आई कैन टेल।

### 00:03:23 · Speaker 1

during the first phase of the execution. JavaScript execution is actually two step. If possible I'll make a video in this series itself how the execution actually happens. So but into with respect to this video I'll keep it brief. So JavaScript execution of a program happens in two steps. One step it will go through the entire file and identify some functions variable which all need be actually called in the second step. So what happens during first step is whenever it encounters line number three the definition or the function definition will be

### 00:03:53 · Speaker 1

to the top of the particular block let's say here something like function test so which will make it accessible during the second run so no matter whether you call from line number three or line number six the JavaScript engine is aware of a function called test which already exist okay so we'll be able to invoke it

### 00:04:13 · Speaker 1

So this is something that all of us use every day where we try to invoke a function from above and below but most of us doesn't know how this really works. So this is a fundamental concept of the JavaScript that is hosting. Okay. Let's let me see let me just walk you through the actual definition. This is copied directly from developer.mozilla.com. So JavaScript hosting refers to the process whereby the interpreter appears to move the declaration of functions.

### 00:04:37 · Speaker 1

variable or classes to the top of their scope prior to the execution of the code. So prior to the execution of the code here means like I said the two step. The first step it scans the second step where the actual execution happens. Okay?

### 00:04:50 · Speaker 1

Now let us get into variable hoisting, okay? Variables as you are aware in JavaScript we can create variable in in three uh with three different keywords. Let's start with a var, okay? I'm creating a variable x and here I'm trying to declare a value of x is, okay?

### 00:05:09 · Speaker 1

and I'm logging the X here.

### 00:05:12 · Speaker 1

If you are new to new to JavaScript, you will be expecting value of X to be some reference error. The reason being, uh we are trying to access value of X even before it is getting initialized. So here it is actually it is getting declared or initialized. There so far there is no definition. We haven't initialized any value to X. Okay?

### 00:05:30 · Speaker 1

So line number four we have variable declared x and we are trying to execute this uh block, okay? We will get a strange error, let me explain that to you. So nothing came actually, even the error did not came, even the output did not came. Intentionally I am showing you this because we haven't invoked the function. The reason I am showing this is many people during the interview get uh confused or in tension, they will write all the code and they will not invoke the function itself. And if it's a complex code, even interviewer will not be able to help you. I mean calling a function from another function, in that case you will miss out.

### 00:06:00 · Speaker 1

your actual logic whatever you're trying to implement. Okay? So don't miss this. So whenever you write a function first call it then only you start further execution. Okay? So now the output you would get is a value of x is undefined. The value of x became undefined because of the concept of hoisting where actually during the first run this happened. The value of the variable x which was in line number five moved to the top of the block in this case line number three and initialized with a value of undefined. Okay?

### 00:06:29 · Speaker 1

So you are getting the value of x as undefined here. So let us try to just uh just check another variation of it, okay? Even if you do value of where x equal to sixty, it still be hold good. I mean the undefined value itself is there. The reason being

### 00:06:45 · Speaker 1

that a variable definition happens still on line number four but just the declaration part of it will be moved to the top and by default the value will be initialized to it as undefined. Okay. This is about the hosting with respect to keyword of variable created with var keyword. Let me do the same with variable created with let keyword. Okay. So if you're not sure what is the var let and const keywords and how to create a variable with that I would advise you go and watch you go and watch some videos on YouTube or read

### 00:07:15 · Speaker 1

official documentation to understand that if I create any series related to that I'll definitely link the description in the video okay so in this case let x I'm defining it as value of sixty

### 00:07:26 · Speaker 1

So, uh, if you are aware of this answer, don't, uh, watch the next video for a couple of seconds, comment your answer, then, uh, continue the video. Let me execute it. So we are getting reference error, cannot access X before the initialization, okay?

### 00:07:41 · Speaker 1

So, uh with your previous mindset of using var, you would have expected even this also to come undefined, but it does not. The reason being, what happens during the first run is this happens, but uh value of variable uh x uh will not be initialized with any value, okay? The hosting happens, uh in fact even this also doesn't happen, like let x will not come because if you do the let x, you will still get undefined.

### 00:08:05 · Speaker 1

uh because the the variable got declared and there's no default value initialized to it. So in this case the default value get initialized but if you're trying to access it before this the hoisting happens the variable declaration moves on to the top but there will not be any default value initialized to it number one. Second it goes into a state called temporal dead zone. Okay temporal dead zone is also one of the famous interview question where the time where or the zone where the variable got uh declared or where the variable got hoisted

### 00:08:35 · Speaker 1

and the variable actually defined, I mean when you assign a value into it, that zone is called temporal dead zone. Here the word temporal is used to indicate that it is not the order in which you write the code, it is the zone where you belong, okay? I'll I will explain that in detail in the next video, how temporal dead zone work and when the temporal dead zone starts and when the temporal dead zone ends, okay? So for this example, I I want you to be clear that variable

### 00:09:05 · Speaker 1

declared with the keyword let is also hoisted but you will not be able to access the value of it even before it is getting uh defined. So so we are getting the error as uh accessor unable to access the variable. Let's do the same with a const also another way of uh creating the variable constex.

### 00:09:25 · Speaker 1

So here, uh

### 00:09:28 · Speaker 1

as a front end interviewer preparing the candidate who is preparing for the front end interview you must be able to uh answer that this statement itself wrong because you cannot create a constant variable without the value initializing to it. So constex itself wrong there should be some value to it. So if I run this code

### 00:09:45 · Speaker 1

you'll get an error missing initializer const declaration. Okay? So you cannot declare a variable without initializing it or without defining it. Okay? Let's do ten. So const x equal to ten. So now whatever error you got here, this is nothing to do with hosting. This is a typical JavaScript error.

### 00:10:00 · Speaker 1

Now what you get, let's see, reference error cannot access X before the initialization. So same thing that happened with let is happening with the const also. So const variables are also getting hoisted, but the default value of it is not initialized and it also goes into state of temporal dead zone where you will not be able to access the value of it until it is getting defined. So the zone in which it get hoisted and the value is not you will not be able to access the value of it is called the temporal dead zone. Okay.

### 00:10:30 · Speaker 1

take away from this video I'll summarize. uh the functions in JavaScript get hoisted. variable declared with var keyword get hoisted. let variable declared with let and const keyword also get hoisted. classes also get hoisted. I'm not showing the classes here because most interviews you'll interviews will not ask you the class concept. But even if they ask the class concept it is fundamentally the same because there is no class as such in JavaScript. The it will under the hood they all are functions. So same way how you are able to invoke a function and above and below of it.

### 00:11:00 · Speaker 1

be able to create a class objects above and below of it. Okay? This is about the hosting. Okay? If you like my video, the way I'm explaining, please like it, share it and subscribe to our channel Uncommon Geek. Okay? I'll see you in the next video.

### 00:11:15 · Speaker 1

If you want me to make any videos, any particular kind of videos, please comment it and definitely I'll make those videos in the upcoming sessions. Thank you all.
