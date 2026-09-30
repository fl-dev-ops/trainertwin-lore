---
id: 1N1wq742qeo
title: Learn how to implement Array.map by passing callback to prototype (JS Custom
  Implementation Ep-4)
date: '2022-06-10'
url: https://www.youtube.com/watch?v=1N1wq742qeo
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ As you all know JavaScript has thousands of builtIn methods which we all use on\
  \ a day to day basis Ex: Array concat, Array filter, String charAt etc. It is very\
  \ important for a developer to know at least how few of these methods are implemented.\
  \ Asking candidate to write the custom implementations have become one of the most\
  \ common interview questions these days. I will be discussing most common custom\
  \ implementations in this series. \n\n Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  \nJavaScript Custom implementation introduction: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\
  \ \n\n\nHow add custom methods to JavaScript Prototype: https://www.youtube.com/watch?v=R5vbUc0uB7E&t=134s\
  \ \n\n\nHow to write custom implementation for Array.concat: https://www.youtube.com/watch?v=wTQwuZuEBHU\
  \ \n\n\nInterview Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\n\nMedium Blog https://mevasanth.medium.com/ \n\n\n\nArray Flat from developer.mozilla.org:\
  \ https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map\n\
  \n\nJavaScript Function: https://www.youtube.com/watch?v=VaL5lrxX-kY&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t&index=10\
  \ \n\n\nGithub Repository that contains examples: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript"
author: careerwithvasanth
duration: 00:15:00
model: saaras:v3
transcript: true
---

# Learn how to implement Array.map by passing callback to prototype (JS Custom Implementation Ep-4)

## Transcript

### 00:00:00 · Speaker 1

हेलो ऑल, वेलकम बैक टू अनकॉमन गीग्स, मैसेल्फ़ वसंत, आई होप यू ऑल डूइंग वेल।

### 00:00:04 · Speaker 1

So in today's video, we are discussing about another custom implementation that is array.map, okay? So far we have already covered multiple functions in this series like array.concat, array.flat, etcetera. So this is a very very important series because in so far in all the videos that we discussed, we were passing a values into a custom implementation. In this case, you have to pass a callback or a function to the custom implementation. So actually I thought of first starting with an array.reduce method which is asked in very very all the

### 00:00:34 · Speaker 1

companies, okay, and very commonly. But before I take up array.reduce, which is slightly complicated, I thought of taking this array.map method, which will act as a helping before I going to the very complicated implementation of reduce, okay? So please be with me, watch this video till the end, okay? Once you are sure how array.map works, you will be able to write any custom implementation that takes a callback as an input or a function as an input and perform certain action, okay? Without wasting further time, let's get started, but only one, one last thing, in case if you are

### 00:01:04 · Speaker 1

who hasn't seen my past videos in this series and directly land into this video. I would highly advise please go back and watch at least first and second and third video of mine. So where I have explained things step by step manner about the custom implementation, how a programming constraint get access to different methods, like let's if you create let array one, how array one get access to lot of built in methods etcetera I have explained. Without that if you directly come to this it will be slightly difficult for you because I assume you know some things, okay? That is the only thing without wasting further time. Let's get started

### 00:01:36 · Speaker 0

So now

### 00:01:37 · Speaker 1

you have a array.prototype.map method, okay? So this is a method that takes, that creates a new array.

### 00:01:45 · Speaker 1

populated with the result of the calling a provided function on every element in the calling array. I don't know why developer.mozilla.org makes always the definition quite difficult for at least majority of people to understand. Definitely this is understandable but not so easily understandable, okay? So I will explain very simple words. So we have array one four five six and map function where we are doing array one dot map and inside that you have a function x which is doing x star two, okay?

### 00:02:15 · Speaker 1

x every time refers to the value like one four nine six every like a loop it is running and then what it is doing it is multiplying that with a two then after the end of this iteration it is returning the value back to the map one function okay map one basically now contains the output of this execution so if you run you would see two two eight uh eighteen thirty two basically double of this whenever you multiply two into this whatever you get that is been logged here okay so that's about what map does

### 00:02:45 · Speaker 1

okay? But you need to little more understand about map like same way how I said about concat, correct? It is not about just understanding one bit of a method and starting implementation. Especially the tier one company engineers expect you to cover all the scenarios that a method covers. So if you come here now in syntax, so first element by default points to element, okay? Straight away I'm coming here where

### 00:03:08 · Speaker 1

First is the element. Second is the index. Third is the array itself. So basically the custom function whatever is inside the map block will take three arguments that is element, index and the array itself, okay? Depending on whatever you want to perform, you can perform inside, correct? Now, when you will use the array.map method? Interviewer will definitely ask this question to you, okay? You will use array.map method when you want to transform the input array. So array one was the array. you want to

### 00:03:38 · Speaker 1

don't want to transform the input array. You want to perform some action from the given array and you will return a new array. So whenever you want to form a new array from the existing array, then you will use array.map. What if you don't want to change the existing array or what if you want to change the existing array itself? Then you can use the for loop or for each, for of, etcetera. So this is also another very important interview question, when you will use map and when you will use for each. I answered that here itself. Okay. Now, without wasting further time, let's start the implementation. I'll copy the same things, okay?

### 00:04:13 · Speaker 1

and I have also not come prepared for this video, okay? Roughly I know how to pass a call back. The reason I have not come prepared is the same as you already know. I'll want to make some I not intentionally I want to make mistake but if I make some mistake by miss, at least you guys get to learn my mistakes and do not repeat that in the interview. The videos where I come prepared I don't make mistake then you will not you will miss out that chance, okay? But still I think I'll be able to write it, that's what I'm hoping. So we have array one with one four nine sixteen, one same array basically so I'm just executing.

### 00:04:43 · Speaker 1

nothing much we got it. So let us start by first writing a custom method okay. So maybe I'll keep all these things below.

### 00:04:53 · Speaker 1

So where I am writing a custom method that is array dot prototype dot my map, okay? uh In case if you are someone who don't know what I'm doing here, what is prototype, what is map and all, as I said, please do watch my first videos and come back to this, okay? Then only you will get a sense of what all happening here, okay? I'll try to link that also somewhere on the screen and in the description section so that you can quickly get access to that. Now. So first thing is, basically this function, as I said, it takes a callback as an input.

### 00:05:23 · Speaker 1

correct? A callback as an input it takes, okay? Then what we do is we will run, okay? I is equal to zero, I less than, maybe I won't put the for loop, okay? Before I start the actual implementation, I just have one call out. In case if you are someone who is preparing for JavaScript driven interviews, anything React, React Native, Angular, Vue, not just anything. I prepared a beautiful series. I'll try to link that somewhere in the description with most common

### 00:05:53 · Speaker 1

your question and how to tackle them, okay? Please go ahead and watch that. uh because that will definitely help you if you're preparing for interview. I'm sorry I'm I'm repeating it in my all the videos, someone who is watching continuously may get annoyed. But I'm just want to make sure as many people as possible, I just want to help them to clear their interviews, okay? So I'm just telling again in this video. Now let me start the implementation, okay? So,

### 00:06:14 · Speaker 1

So what I will be doing now is, very first, we should get access to this array, whatever we are passing because we have to run the map or the iteration till the length of the array, correct? So you know how to get that? const input array

### 00:06:30 · Speaker 1

is equals to this. See if I am writing a this kind of program in a top tier one companies, man companies, I wouldn't be doing this, okay? The reason being I am using extra memory for already existing variable, but for the explanation purpose because of the diverse audience, I just do this way, okay? So once you get a hand of understanding of what is this, then you can you do you also don't have to do this, okay? For those of you are straight away watching this video, not watched my previous video, this basically refers to the reference with which you are triggering this. In this case,

### 00:07:00 · Speaker 1

array one you are triggering my map method. Okay. So you are triggering my map method so array one points to this. Now.

### 00:07:08 · Speaker 1

Next you have, you have to run the loop till the length of the array, correct? So input array dot length. Now, next, you already have a callback method here, correct? You already have a callback method here which does x equal to x star two. What you have to do is you have to execute the callback method, whatever the callback that you got, okay? But as per the definition, it takes three things. First one is the value, okay? Three things. First is

### 00:07:38 · Speaker 1

value, second is index, third is array itself, correct? So here what is the value? That is input array of I is the value, which will points to one in the beginning, four, nine, six going forward. What is the second argument? Index. We already know I is the index. What is the third argument? Array itself. So that also we have input array. So we now know all the things. So whatever the callback that function that you are passing, so we are triggering the same callback method inside this block.

### 00:08:08 · Speaker 1

Okay? But one important thing to observe here is we need to form a new array, correct? That is what the, that is what map does. To do that, what I'm doing, I'll create one array, const output.

### 00:08:21 · Speaker 1

And whatever the value of this, correct? Whatever the value that I'm getting from this, I will be pushing that into this array. I know it is getting slightly confusing. I'll explain this once again, okay?

### 00:08:38 · Speaker 1

okay? First, I'll try to run this code and again I'll explain step by step what is happening, okay? I think most of you understood till calling the callback method, maybe what happened or what why I'm doing output.push, some of you might be confused, but I'll explain that, okay? So then I would do return output. First, we'll make sure it is working well as I'm also writing just like any of you in the interview, okay? So map one array.mymap, but let me do a dry run. So this is a practice that I do no matter which kind of a company I'm going to interview.

### 00:09:08 · Speaker 1

I never run the code. More run with failures will decrease your confidence by the interviewer. Interviewer think you are not confident about the code you are writing. So try to run as many less times as possible. Okay? So now we have array one which has one four nine sixteen as the input. Then we are calling my map and I'm passing a callback. Okay? I have a callback here. So input array points to one four nine six. Then for I is equal to zero I less than input array dot length. Okay? So input array is one two nine sixteen. In the first it read

### 00:09:38 · Speaker 1

what I'm doing I'm call back. So this method, this method I'm calling by passing input array value which is two, okay? As you know you're having you're using only X here. That means the first value if you see here.

### 00:09:52 · Speaker 1

We have three values, element, index and array. If you are not passing second and third, only one value of passing by default that points to the value. Okay? If you pass two, that points to value and the index. If you pass three, value index and the array. So you're passing only one here. uh So I we could have only passed one, but I am sticking to the constant. So I and input array we are passing, so it will execute one by one. Then finally I'm returning the output. Looks like it will work. Fingers crossed. Let's run and see whether it will work or not. If not, let's quickly try to

### 00:10:22 · Speaker 1

It worked. Two four eighteen and thirty two. Correct? Double of this. Correct. It worked. Luckily it worked. Okay? I was not expecting it will work straight away. Okay? Luckily it worked. Now let me try to explain what I am doing. Okay?

### 00:10:39 · Speaker 1

I believe many of you might have understood till here. What why I'm doing output.push some of you might have not understood. Okay? So let me just remove the output.push. Okay? Then explain step by step. So whenever you are calling the callback method, correct? Technically you are invoking this method. Okay? Let's say let me extend this rather having X, what I'll do? value index array. Okay? I'll let me do like that. Then I'm doing value star two.

### 00:11:09 · Speaker 1

for this particular example I don't need the value of index and array so I'm just keeping that. I'm not using it. your implementation you can continue you may use it. So now value star two you know this an arrow function arrow function when you are not keeping a flower brackets like this okay this then by default you are returning whatever is on the inside. So to make sure you understand it properly okay I'm just keeping a flower bracket. then

### 00:11:39 · Speaker 1

I am returning this value. Okay, return. So whenever you're invoking this particular block of code, every time you're returning the double value by multiplying to whatever the value you got, you're you're sending it back. So in this my map method, what I'm doing for the first time is, I'm running till the length you already know, for the first time I will execute this block where I know the value, correct? So what I'm doing, I'm just calling this method by passing three values.

### 00:12:08 · Speaker 1

This method only I'm calling where value I'm passing as input array of I. Index is one, input array is input array itself. Then inside this it is returning the value star two, which is first case one star two which is two. So you called the method but somewhere you have to store the output so that you can form a big array and return it. Correct? I mean big array I mean the array that contains the result. So that I need to form. To form that what I'm doing I created an output array and then

### 00:12:38 · Speaker 1

I am adding the pushing the values into the output array here and I'm returning it. You can make it a two step process if you are getting confused, okay? const

### 00:12:48 · Speaker 1

partial output, correct? This is one line output, then output dot

### 00:12:57 · Speaker 1

push

### 00:12:58 · Speaker 1

partial output. Okay? Then you can you can return output. This remains same. Just one step to I'm breaking down that into two step process. Hope now you all understood what we are doing. So basically for a map method it takes a callback. So we are passing a callback into my map method also. Then this callback method is something that a developer writes like for example like this. Same method you are triggering for each and every element here. Okay? Only thing that you are doing is

### 00:13:28 · Speaker 1

you are copying that result or taking the result and pushing into the output array, finally returning that output array. Okay? So this callback is basic nothing but this method. It takes three argument which you are passing here. It is returning a value star two, double of the value that you are passing, that is stored here. Then you are finally pushing that into the output array. Correct? And once the array iteration is done, you are returning that value. That's all we are doing. Got it? So this is about the array

### 00:13:58 · Speaker 1

my map. Wait. Now I have homework for you. So, for each I said is a method which does a similar thing, but it doesn't return a new array, but it will modify whatever the existing array or you can use it to do any other thing. So try to implement array.foreach on your own. If most of you are not able to implement, definitely I'll write, mention that in comment section. I'll try to write a medium blog or another video and post that in the description section. If not, if you return, please link your medium blog or your gist or your whatever you have written.

### 00:14:28 · Speaker 1

button. Please link that. I will read and if it is wrong, if need any correction then I will let you know. Okay? Thank you so much for watching this video. If you would have liked my video, please do like it on my YouTube channel. Share this video along with your friends who and all are preparing for the seriously preparing for the interviews. Do not forget to subscribe to Uncommon Gist. Please, please subscribe to Uncommon Gist. That is the thing that gives me motivation to make more such good content. Okay? Catch you in my next video but I will link my medium blogs where I have beautifully explained different concepts like this. Please do follow me on medium also and read my article. Thank you again
