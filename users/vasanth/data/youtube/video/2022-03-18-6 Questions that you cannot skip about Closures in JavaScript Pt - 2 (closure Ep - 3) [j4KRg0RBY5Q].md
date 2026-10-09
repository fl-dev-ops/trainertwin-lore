---
id: j4KRg0RBY5Q
title: 6 Questions that you cannot skip about Closures in JavaScript Pt - 2 (closure
  Ep - 3)
url: https://www.youtube.com/watch?v=j4KRg0RBY5Q
date: '2022-03-18'
duration: 00:10:11
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
---

# 6 Questions that you cannot skip about Closures in JavaScript Pt - 2 (closure Ep - 3)


## Transcript

### 00:00:00 · Speaker 1

Hi all welcome to uncommon geeks myself Asant I hope you all doing well

### 00:00:04 · Speaker 2

This is a continuation of our videos on closure. We have already discussed the basics of closure, the classic counter dilemma and some kuyunde on the basics of closure. This video will try to discuss some advanced questions on closure. So if you have not watched my previous videos on closure, I'll try to add the link somewhere on the screen also in the description section. Please go ahead and watch those videos. Only if you watch those videos, this section becomes easy where I'll be asking some complex questions on closure. So without wasting further time, let's get started.

### 00:00:32 · Speaker 2

question number one uh an easy question uh where this is actually a self-invoking uh function okay uh if you have understood my previous video where i have explained the self-invoking function this question is quite straightforward and you'll be able to answer it okay so where we have created if you already know the answer just by looking at it you can pause the video put that in comment section question number four and your answer if not let me just uh give a quick walkthrough of the question so we have one function called testa which is self-invoking function you are you you know

### 00:01:02 · Speaker 2

self-invoking function with those function that doesn't need any external invocation they get executed by themselves they're mainly used to create a closure so test a is getting invoked inside which you have another function that is getting returned which is test b okay and inside which we are basically triggering the we are logging the value of a okay so questions remain the same so and you're you're calling the self-invoking function from invoking function one from here and two from here and you're passing the arguments

### 00:01:32 · Speaker 2

and 1. So in line number 4, will you be able to access the value of a or not? So just think about it. It is not just the normal closure thing. It is actually having self-inoking function. I want you to chuck it in detail and guess the output. Okay. So and only if you are able to answer this question, this question, assume that you have a pretty good hold on closure. If not, you may have to still practice further to understand the properties of closure. Okay. Let me execute it. So we're getting 0. That means whatever the value of 0 you passed.

### 00:02:02 · Speaker 2

what have what happening I'll do a do a dry run so in line number six you are passing zero so this a becomes zero and this block got executed this outer block got executed okay and the inner block which is returning the function b so b is getting triggered from here so it is having the value of one okay and in line number four we are as soon as it's self invoking function the inside the block gets executed so it'll be logging the value of a which is zero so the a which was a

### 00:02:32 · Speaker 2

of the outer function can be accessed inner function due to a property of closure so this

### 00:02:38 · Speaker 2

value of a in line number 4 is actually 0. So, a is accessed inside here. So, this is a good example for closure. This is very simple question. Only if you understood the closure property very well, you will be able to answer it. Now, we will go to the second question. This is a classic question.

### 00:02:57 · Speaker 2

You might have seen it in multiple places okay but still many will not be able to answer this question or they will not be able to answer it correctly so that is the reason I picked this question

### 00:03:09 · Speaker 2

So basically you are invoking a function called test here and inside which you have created a for loop and inside which you have a timeout set timeout for those of you who don't know what is the timeout basically set timeout is used for making an asynchronous task. So if you want to perform a task after a particular time interval then you specify the time interval here and perform the task here 1000 stands for one minute one second so where it is one second is equal to 1000 millisecond okay so set timeout is getting formed here and you are logging the value of i so if you know the value

### 00:03:39 · Speaker 2

of it please do mention that in comment section okay if not uh let me let me give a quick walkthrough of the question and let us predict the output so you're calling the test and inside which we have a for loop so this is what anything inside the for loop as you know will get executed as long as the condition is correct the condition will hold good for three times that is zero one and two then when i becomes three the condition will fail and the for loop will be stopped so inside which so three timers are created for

### 00:04:09 · Speaker 2

thousand second that is a thousand millisecond or one second so we have a function here which gets executed after one second which prints the value of i okay so the first time whenever the set time mode is formed the value of i will be zero second time it is one third time it is two straightforward correct so now whenever you log the the output expected output is zero one and two okay let me execute it

### 00:04:35 · Speaker 2

We are not getting 0 1 and 2 instead we are getting 3 3 and 3. Uh have you done some mistake?

### 00:04:42 · Speaker 2

The mistake is in the explanation and are unable to understand the closure property correctly. Okay. So just to make this question quite trickier, what I'll do, I'll make it zero. So basically zero means you got the set time out executed straight away. Do not wait for any time. Okay. So if I execute this, still I'm getting three, three, three. So basically expectation was this set time out with a value of zero, it will execute immediately. Correct. So whatever the zero here. So basically the set time out is not waiting.

### 00:05:12 · Speaker 2

for anything we are not making it asynchronously we are making synchronous try to make it synchronously execute immediately but still we are getting 333 so to solve this problem first we have to identify why we are getting 333 then we can figure out how to get 0 1 and 2 okay so if you come here we have created a variable with i okay so you all know variable created with var keyword will have a global scope if you do not know what is global scope and how let and where and const differ in the in the scope property

### 00:05:42 · Speaker 2

You can watch my hosting video. I'll try to link somewhere on the screen also in the description box. Okay. So here we have created a variable i which has a global scope. So inside the entire block of the test, we have only one variable that can be created with the value of i.

### 00:05:56 · Speaker 2

And we have a three set timers, set timeout, or we can also call it three timers, which will expire after one second. Okay. So that is zero or one doesn't make sense because actually set timeout, whenever you write the set timeout, it will become asynchronous block. And only after main thread executes all the synchronous things, it will come to the set timeout. So due to which whether it specifies zero or thousand in this example has not much of a difference. Okay. So here we have a function. So what is happening? Three set timers are

### 00:06:26 · Speaker 2

timer getting created which will expire after one second this is a this is value property one every time whenever this set time mode was created right it formed a closure or you can tell a egg or a nest okay that is formed and the value of i was bound inside this you can tell value of i was bound putting other way the reference to the memory location of i okay then after the uh was uh after one second all the three timers will get expire and it look for the value

### 00:06:56 · Speaker 2

of i so the reference of i was already there with the property of closure so at the moment i is actually since it's a global scope i points to 3 actually because it was 0 1 2 3 when 3 it got filled so in the memory location of i you would see a value of 3 so due to which after the timer is expired you are getting 3 3 3 all the i's pointing that i points to the same memory reference and we're getting 3 as an output how to solve this was it's very straightforward you don't have to

### 00:07:26 · Speaker 2

know any rocket sensors all this if you know the concept of let var and const you will be able to solve this so let it's unlike the var which is a global scope let has a block scope or in the in the wherever that you define the scope for that inside only that it will be we will be able to access it so in this case if you use let same thing happens three nests are formed but only difference is the value of i in all the three blocks will be unique they all point to different memory location so first time it will be zero second time it will be one third time it will be two i becomes

### 00:07:56 · Speaker 2

three but data is different than all these threes okay all these three uh x or nes that are formed which enclosed the i within them so due to which if we execute now

### 00:08:09 · Speaker 2

you'll see 0 1 and 2. So there is another tricky question we generally ask in this topic is we have you have to use var itself because there are still browsers which are like it doesn't support ES2016 where let's end calls are introduced. So how do you support those browsers? The easiest answer for that is you form a function. Okay. Let's name it test2. It takes an argument of j and we'll enclose this block inside this and we trigger test2.

### 00:08:39 · Speaker 2

And pass the value of i let me execute it then I'll explain what is happening okay

### 00:08:46 · Speaker 2

test to J so here I'm making it J

### 00:08:49 · Speaker 2

execute 0 1 into got it right so what happens is whenever we have we are having a function what function does is uh test to which is a function so it will be taking the value of i here and be passing to this test to so basically function forms again a closure so no matter whether you're using within using var or let inside this it's a function so function is having again a block scope this j every time that is a new j okay unlike the where this function was

### 00:09:19 · Speaker 2

not there the value of where was all the different blocks are pointing to the same location doesn't happen here so inside the function block every time it's a different jay okay so this is one of very classic problem and most interview they still ask this and there's a variation of this that can be asked like i tried explaining all the common variation that are asked to me in the interview okay please do watch this video again if you're not understood it and practice them by copying my project from the github okay thank you so much for watching my video if you would have liked my

### 00:09:49 · Speaker 2

video please do like it on my youtube channel if you want your friends or get benefited please do share the video with them do not forget to subscribe to uncommon geeks my medium blogs my github projects are linked in the description follow me on medium read my articles there download project from the github url and give a start for that project and practice the questions very thoroughly okay thank you so much for watching catch you in next video

