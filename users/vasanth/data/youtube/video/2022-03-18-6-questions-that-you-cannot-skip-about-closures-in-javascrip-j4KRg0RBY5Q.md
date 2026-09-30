---
id: j4KRg0RBY5Q
title: 6 Questions that you cannot skip about Closures in JavaScript Pt - 2 (closure
  Ep - 3)
date: '2022-03-18'
url: https://www.youtube.com/watch?v=j4KRg0RBY5Q
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Questions on closure Part 1 - https://youtu.be/pycV_CSoj1g\n\nClosure and nested\
  \ functions in JavaScript - https://www.youtube.com/watch?v=6xU_VIDB-zw&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t&index=11&t=26s\n\
  \nCounter dilemma in JavaScript - https://www.youtube.com/watch?v=nJhQRotbIis&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t&index=15\n\
  \nMy Medium Blogs - https://mevasanth.medium.com/ \nGithub URL which contains questions\
  \ - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \ Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/"
author: careerwithvasanth
duration: 00:10:11
model: saaras:v3
transcript: true
---

# 6 Questions that you cannot skip about Closures in JavaScript Pt - 2 (closure Ep - 3)

## Transcript

### 00:00:00 · Speaker 1

all, welcome to Uncommon Gigs. Myself, Fasant. I hope you all doing well. This is a continuation of our videos on Clojure. We have already discussed the basics of Clojure, the classic counter dilemma and some Q&A on the basics of Clojure. This video will try to discuss some advanced questions on Clojure. So if you have not watched my previous videos on Clojure, I'll try to add the link somewhere on the screen also on the description section. Please go ahead and watch those videos. Only if you watch those videos, this section becomes easy, so where I'll be asking some complex questions on Clojure. So without wasting further time, Let's get started

### 00:00:31 · Speaker 1

So the question number one, uh an easy question where this is actually a self-invoking function, okay? If you have understood my previous video where I have explained the self-invoking function, this question is quite straightforward and you'll be able to answer it, okay? So where we have created, if you already know the answer just by looking at it, you can pause the video, put that in comment section question number four and your answer. If not, let me just uh give a quick walk through of the question. So we have one function called test A which is self-invoking function.

### 00:01:01 · Speaker 1

self invoking function means those function that doesn't need any external invocation they get executed by themselves they mainly used to create a closure so test A is getting invoked inside which you have another function that is getting returned which is test B okay and inside which we are basically triggering the

### 00:01:18 · Speaker 1

we are logging the value of A, okay? So questions remain the same. So and you're you're calling the self inoking function from invoking function one from here and two from here and you're passing the arguments zero and one. So in line number four will you be able to access the value of A or not? So just think about it it is not just the normal closure thing it is actually having self inoking function. I want you to check it in detail and guess the output, okay? So and only if you're able to answer these questions this

### 00:01:48 · Speaker 1

question, assume that you have a pretty good hold on closure. If not, you may have to still practice further to understand the properties of closure, okay? Let me execute it.

### 00:01:57 · Speaker 1

So we're getting zero. That means whatever the value of zero you passed, so what what happening I'll do a do a dry run. So in line number six you're passing zero. So this A becomes zero and this block got executed. This outer block got executed, okay? And the inner block which is returning the function B. So B is getting triggered from here. So it is having the value of one, okay? And in line number four we are as soon as its self invoking function the inside the block gets executed. So it will be

### 00:02:27 · Speaker 1

logging the value of A which is zero. So the A which was a part of the outer function can be accessed inner function due to a property of closure. So this

### 00:02:37 · Speaker 1

So value of A in line number four is actually zero. So A is accessed inside here. So this is a good example for closure. Okay? This is this is very simple question. Only if you understood the closure property very well, you will be able to answer it. Okay? Now we'll go to the second question. This is a classic question. Okay?

### 00:02:56 · Speaker 1

you might have seen it in multiple places, okay? but still many will not be able to answer this question or they will not be able to answer it correctly. So that is the reason I picked this question, okay?

### 00:03:09 · Speaker 1

So basically you are invoking a function called test here and inside which you have created a for loop and inside which you have a timeout, set timeout. For those of you who don't know what is timeout, basically set timeout is used for making an asynchronous task. So if you want to perform a task after a particular time interval, then you specify the time interval here and perform the task. Here thousand stands for one minute, one second. So where it is one second is equal to thousand millisecond, okay? So set timeout is getting formed here and you are logging the value of I. So if you know the value

### 00:03:39 · Speaker 1

output of it, please do mention that in the comment section, okay? If not, uh let me let me give a quick walk through of the question and let us predict the output. So you're calling the test and inside which we have a for loop. So this anything inside the for loop as you know will get executed as long as the condition is correct. The condition will hold good for three times, that is zero, one and two. Then when I becomes three, the condition will fail and the the for loop will be stopped. So inside which so three timers are created for

### 00:04:09 · Speaker 1

thousand second that is thousand millisecond or one second. So we have a function here which gets executed after one second which prints the value of I. Okay. The first time whenever the set amout is formed the value of I will be zero. Second time it is one. Third time it is two. Straightforward. Correct? So now whenever you log the the output expected output is zero one and two. Okay. Let me execute it.

### 00:04:34 · Speaker 1

We are not getting zero one and two. Instead we are getting three three and three. Have we done some mistake?

### 00:04:42 · Speaker 0

Yes

### 00:04:42 · Speaker 1

The mistake is in the explanation and are are in a way to understand the closure property correctly, okay? So just just to make this question quite trickier, what I'll do, I'll make it zero. So basically zero means you got the set time out, execute it straight away. Do not wait for any any time, okay? So if I execute this, still I'm getting three three three. So basically expectation was this set time out with a value of zero, it will execute immediately, correct? So whatever the zero here, so basically the set time out is not

### 00:05:12 · Speaker 1

getting for anything. We are not making it asynchronously, we are making it synchronously. Try to make it synchronously. Execute immediately, but still we are getting three three three.

### 00:05:20 · Speaker 1

So to solve this problem, first we have to identify why we are getting three three three, then we can figure out how to get zero one and two, okay? So if you come here, we have created a variable with I, okay? So you all know variable created with var keyword will have a global scope. If you not know what is global scope and how let and var and cons are differ in the in the scope property, you can watch my hosting video. I'll try to link somewhere on the screen also in the description box, okay? So here we have created a variable I which has a global scope. So in

### 00:05:50 · Speaker 1

inside the entire block of the test, we have only one variable that can be created with a value of I. Okay?

### 00:05:56 · Speaker 1

And we have a three set timers, set timeout or you can also call it three timers, which will expire after one second, okay? So there is zero or one, doesn't make sense because actually set timeout whenever you write the set timeout, it will go it will become asynchronous block and only after main thread executes all the synchronous synchronous things, it will come to the set timeout. So due to which whether you specify zero or thousand, in this example has not much of a difference, okay? So here we have a function.

### 00:06:24 · Speaker 1

So what is happening? Three set timers or three timers getting created which will expire after one second. This is a this is property one. Every time whenever this set timeout was created, right? It formed a closure or you can tell a egg or a nest. Okay, that is formed and the value of I was bound inside this. You can tell value of I was bound putting other way the reference to I, the memory location of I. Okay? Then after the was after one second, all the three

### 00:06:54 · Speaker 1

timers will get expired and it looks for the value of I. So the reference of I was already there with the property of closure. So at the moment, I is actually since it's a global scope, I points to three actually. Because it was zero, one, two, three, when three it got failed. So in the memory location of I, you would see a value of three. So due to which, after the time over is expired, you are getting three three three, all the I's pointing that I points to the same memory reference and we are getting three as an output.

### 00:07:23 · Speaker 1

How to solve this Vasant? It's very straightforward. You don't have to know any rocket science to solve this. If you know the concept of let, var and const, you'll be able to solve this. So let, unlike the var which is a global scope, let has a block scope or in the in the wherever the you define the scope for that, inside only that it will be we'll be able to access it. So in this case if you use let, same thing happens. Three nests are formed, but only difference is the value of I in all the three blocks will be unique. They all point to different memory location. So first

### 00:07:53 · Speaker 1

it will be zero, second time it will be one, third time it will be two. I becomes three, but that I is different than all these threes. Okay, all these three uh eggs or nests that are formed, which enclosed the I within them. So due to which if we execute now,

### 00:08:09 · Speaker 1

you'll see zero one and two. So there is another tricky question which generally asked in this topic is we have you have to use var itself because there are still browsers which are like uh which doesn't support ES two thousand sixteen where latent cons are introduced. So how do you support those browsers? The easiest answer for that is you form a function, okay? Let's name it test two. It takes an argument of J and will enclose this block inside this and we trigger test two.

### 00:08:40 · Speaker 1

and pass the value of I. Let me execute it, then I'll explain what is happening, okay? Test two J. So here I'm making it J.

### 00:08:49 · Speaker 1

execute

### 00:08:51 · Speaker 1

zero one into. Got it right? So what happens is whenever we have we are having a function, what function does is test two which is a function. So it will be taking the value of I here and will be passing to this test two. So basically function forms again a closure. So no matter whether you are using using var or let, inside this it's a function. So function is having again a block scope. This J every time that is a new J, okay? Unlike the where this function was not there, the value of var was

### 00:09:21 · Speaker 1

all the different blocks are pointing to the same location doesn't happen here. So inside the function block every time it's a different J. Okay? So this is one of very classic problem and most interviews they still ask this and there is a variation of this that can be asked like I tried explaining all the common variation that are asked to me in the interview. Okay? Please do watch this video again if you have not understood it and practice them by copying my project from the GitHub. Okay? Thank you so much for watching my video. If you would have liked my video please do like it on my YouTube channel.

### 00:09:51 · Speaker 1

If you want your friends also get benefited, please do share the video with them. Do not forget to subscribe to Uncommon Geeks. My medium blogs, my GitHub projects are linked in the description. Follow me on Medium, read my articles there, download project from the GitHub URL and give a start for that project and practice the questions very thoroughly, okay? Thank you so much for watching, catch you in next video.
