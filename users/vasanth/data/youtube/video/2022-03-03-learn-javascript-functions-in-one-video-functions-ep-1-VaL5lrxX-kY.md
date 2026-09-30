---
id: VaL5lrxX-kY
title: Learn JavaScript functions in One video (Functions Ep-1)
date: '2022-03-03'
url: https://www.youtube.com/watch?v=VaL5lrxX-kY
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ If you know how to call functions and what it returns, you can clear half of JavaScript\
  \ interviews. \n\nJavaScript functions could be the topic, on which most interview\
  \ questions can be formed. Because it contains other subtopics like closure, currying,\
  \ nesting of functions etc. Most tricky questions can be easily formed in this topic.\
  \ I will cover each and every topic of functions in this series, watch it carefully\
  \ and practice well, you will definitely answer all questions on this topic in upcoming\
  \ interviews. \n\n\nMy Medium Blogs - https://mevasanth.medium.com/ \nGithub URL\
  \ which contains questions - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \ Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\nHoisting\
  \ Introduction video: https://www.youtube.com/watch?v=skkXL5QdDwk&t=1s"
author: careerwithvasanth
duration: 00:10:57
model: saaras:v3
transcript: true
---

# Learn JavaScript functions in One video (Functions Ep-1)

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome to Uncommon Geeks. I hope you all doing well. Myself Vasant. So today's topic is functions. I know most of you are already aware of functions and you think it is very straightforward topic Vasant why you are covering it. Actually function is very straightforward topic itself. uh But the problem is function has lot of entities inside in it. Like for example closures, function nesting, function carrying. uh Then there are lot many different topics which become difficult during the interview for candidate to answer. There is something also called self invoking functions. Unless

### 00:00:30 · Speaker 1

you have practiced them very well, you will face lot of difficulty in interview to answer those questions. Okay? So due to which I have picked functions. So this video I will dedicate for explaining the basics of function and upcoming videos I will be discussing on the Q and A's. Okay? So without waiting for that time, let's get started.

### 00:00:46 · Speaker 1

So, function, uh, very first let me tell you how to create a function, as you all know, with help of a function statement. Function name starts with a key function, followed by the name, whatever the function name that you want to give, then the parameters, optional parameters. If it is a type script, then you can also specify the return type, which return type you are sending, like integer, string, etc. Basically, what value the function would return after processing is an integer value, string value, promise, etc. But whereas in in the plain Java

### 00:01:16 · Speaker 1

there is no habit of uh mentioning the return type. Okay, so I'm not emphasizing even on the official documentation, you don't see it much. So now we have a function name and parameters. Uh optionally you can pass parameters or you may not pass parameters depending on your requirement. So depending on the parameters you pass or not, there are two categories of function. One is parameterized function, another one is non-parameterized function. So if you pass parameters to function, it will be parameterized function. If you don't pass, it will be non-parameterized function. Okay? And the

### 00:01:46 · Speaker 1

category of function I can tell you one is arrow function and one is a normal function. Arrow function I'll be taking separately in a different sequel but normal function I'll be sticking to this video series. I mean at least the few videos that I'll be making in upcoming sessions.

### 00:02:00 · Speaker 1

So now let us call this function as welcome, okay? And inside which what I'll do? I'll do welcome to uncommon geeks, okay? And I'll invoke welcome

### 00:02:16 · Speaker 1

from here. So this is how you call a function. You most of you already know this is very basic, I understand. But keeping in a mind of a larger audience, I have to go from the basics, only I'll be able to explain very complicated topics, okay? So I'm calling welcome. So as in whenever you invoke this, the function from here, the function gets triggered and you'll see the value welcome to uncommon geeks, okay? If I execute it,

### 00:02:40 · Speaker 1

No

### 00:02:40 · Speaker 0

code

### 00:02:45 · Speaker 1

So you're saying welcome to Uncommon Geek. So basically whatever you have logged inside that you are getting that value. So this is about the normal function. So normal function this is also called as a named function because this function with a name, okay, this is one. So if we can invoke this function even from above or from below, so if I run this, you get the same. This is because the functions are actually function created with a function keyword is hoisted or named functions are hoisted. If you don't know what is hoisting I've explained very much in detail in my previous videos. I'll try to link that video somewhere.

### 00:03:15 · Speaker 1

on the screen also in the description. So if you don't know what is hosting please watch those videos. Okay.

### 00:03:22 · Speaker 1

So this has been hoisted so you are able to get all the I mean you are able to invoke it from above or below. Okay? So this is about normal function or named function. Next and named function you also understood what is parameterized function and what is non-parameterized function. Okay? Now I let me go to the unnamed or anonymous function. Okay? So for example now constant welcome is equals to function okay? And

### 00:03:47 · Speaker 1

log

### 00:03:50 · Speaker 1

Welcome to

### 00:03:53 · Speaker 1

Uncommon Geeks

### 00:03:56 · Speaker 1

and I'll invoke welcome from down. Okay? So the difference uh from there and this is like it is a named function and anonymous function is, see, function after the function keyword there is no name. Okay? That is the main difference. So this function reference is actually been passed to this welcome variable and this welcome variable along with the two parenthesis is actually invokes the this function. Okay? So if I execute it,

### 00:04:23 · Speaker 1

Welcome to Uncommon Geeks. Okay, so same this is getting printed on the screen. Hope you are clear on that. Now, there is Vasanth if this is all the difference where there is nothing much man, there is what's happening is just like rather putting welcome here, we are putting welcome here. Is that all the difference? No. The another difference is in case if you move the welcome up, okay, welcome to the top, you would see error, reference error, cannot access welcome store before initialization. The reason being, this is not hoisted.

### 00:04:53 · Speaker 1

So again I'm telling this is what happens in the interview just by knowing a function topic you will not be able to answer you should know what is hosting. Just by knowing hosting you will not be able to answer you should know sometimes a deep copy and shallow copy. So it's a combination of multiple topics then only you'll be able to answer in the interview. That is the reason I'll be answering taking all the topics and making videos. Okay. Stay tuned with me regarding that. So so again welcome

### 00:05:15 · Speaker 1

remember, though I have explained hosting in detail in my previous video, I'll take a minute to explain it. So, the const welcome is a variable, as you know it got hoisted, it is already hoisted. But what has happened, it has gone into temporal dead zone because the initialization happens here.

### 00:05:31 · Speaker 1

important thing to observe. Welcome as a variable has been hoisted, but this function is not hoisted. Okay? As this function is not hoisted, what happened is whenever you're trying to invoke a function, you're getting the reference error. Okay? So this is about the anonymous function, parameterized function, non-parameterized function, and named functions. Now, there is another important type of function called self-invoking functions. Okay? So let me write a self-invoking function. The syntax for self-invoking function is this.

### 00:06:01 · Speaker 1

self-invoking function need not have a name also the parameter okay so

### 00:06:08 · Speaker 1

Welcome to Uncommon Geeks, okay? Let me execute it, then I'll explain what's happening.

### 00:06:15 · Speaker 1

So welcome to Uncommon Geeks. See, this is a function which no one is invoking. So it's called self-invoking function. Okay? And whenever you execute this, right away you're getting whatever inside the block is getting executed. This is mainly used in the concept of closure, which I'll be explaining in maybe my second or third video in detail. Okay? So this is very much used in closure because this outer scope gets, I mean, the outer function will be removed, only the inner function will be retained. Okay? So this is about the self-invoking function. I'll explain last topic and end this video that is

### 00:06:50 · Speaker 1

We can pass one of the beautiful top concept of JavaScript is you can pass functions as an argument to another function. Okay, let me show you that. So function add, okay, it takes two values, number one, number two, then what you do is you will return number one plus number

### 00:07:10 · Speaker 1

two, okay? Next is you have a function. uh let me call it a test. What it takes is it takes first argument as function, second argument number one, third argument number two. So what it does is let R const

### 00:07:29 · Speaker 1

sum is equals to function of

### 00:07:32 · Speaker 1

number one, comma number two, okay? Then from here, I'll invoke the test and let me completely write it, don't worry, I'll explain this in depth, okay? What is happening.

### 00:07:45 · Speaker 1

then so test then const output is equals to this then I will be logging the output

### 00:07:57 · Speaker 1

cough

### 00:07:59 · Speaker 1

output is

### 00:08:04 · Speaker 1

output. Okay. So basically what I'm doing here is very straightforward, looks very straightforward, but I'll explain step by step.

### 00:08:12 · Speaker 1

First is we have a function called add. So it basically takes two arguments and returns the sum of both two arguments, which is very straightforward. Then we have another function called test, whose first argument is basically a function. Second and third arguments are numbers, okay? Don't think specifying a F, we are making it express that it will take a function as an argument, nothing like that. Any any name you can give, just for the purpose of understanding I've given it a F. Then we have number one and number two, and whatever the number one, number two are, ten and twenty, passed here. and add function. So rather calling add ten comma twenty, we are mimicking that here. Okay?

### 00:08:51 · Speaker 1

So first let me execute then I'll tell why it is required.

### 00:08:55 · Speaker 1

So we are getting output as undefined. So where did we do a mistake? I'm sorry, we haven't returned the sum. Okay, this is very important in the interviews.

### 00:09:05 · Speaker 1

Okay, sum is thirty. So whenever you write a function, I've said this multiple times, whatever you have to return plus return it off even with the default value, then only you start the execution. I made a mistake, it was a simple function I was able to figure out. If it's a complicated one, then you would face a difficulty, okay? Anyways, so what happened is like this. So we have a variable called constant output and we have invoked this test function and here the sum happened and sum is returned. Listen, this is very straightforward. Like I would have invoked add itself by passing the two values. What is the point of having this, correct?

### 00:09:35 · Speaker 1

But there is a point. See, this in this example it is easy but in in the whenever you're working on a real project, there could be a team who has built this ad and they decide not to support you for a for due to some reason. So in that case, you can pass some other team's ad or you can write your own ad function and pass here.

### 00:09:53 · Speaker 1

Correct? So there is no dependency on uh whatever the function, I mean there is no dependency on add now. Whatever the function that you pass that takes two arguments is fine for you now. Correct? And or else if you want to improvise a function by rather using some other team's function, you decide to use your own function and improvise it like you will log some values after adding etcetera. So you have a freedom. Correct? So passing function as an argument is a very beautiful concept in JavaScript and it has lot of advantages. Okay? So these are things that I want to explain for this video.

### 00:10:20 · Speaker 1

If you like my video, please do like it on YouTube channel. And if you want your friends also to get benefited from it, please do share the video link with them. Do not forget to subscribe to Uncommon Geeks. And if you want me to make a video on any particular topic in JavaScript or any other content technologies, please do mention that in comment section. I'll link my medium blog where I've explained a lot of different topics on JavaScript, so you can go there and follow me there also and comment there if you want to know something about the article I've written. I'll also try to link my GitHub projects where I've added all these

### 00:10:50 · Speaker 1

questions and you can go ahead and practice there. Okay. Thank you so much for watching. Catch you next video.
