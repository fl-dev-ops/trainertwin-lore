---
id: 0Mmx1ri70ME
title: Only 1/100 can solve this Meta Interview qstn, Flatten Array without Recurssion
  (MAANG Series Pt -3)
date: '2022-06-19'
url: https://www.youtube.com/watch?v=0Mmx1ri70ME
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ At the time of this series recording, there was no video series which was discussing\
  \ MAANG (Meta, Apple, Amazon, Netflix, Google) interview questions for the frontend\
  \ developers in detail. So, I have decided to decode most of the interview questions\
  \ that were available on the internet. \nThe purpose of this series is not just\
  \ to help you to clear MAANG interview, but help you become a fundamentally strong\
  \ frontEnd Engineer. Stay tuned and watch this entire series.\n\nGithub Repository\
  \ that contains examples: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \nMedium Blog: https://mevasanth.medium.com/  \n\nFlatten an array Medium Blog:\
  \ https://mevasanth.medium.com/flatten-array-of-array-in-javascript-microsoft-interview-question-345c71ff9ccd\n\
  \nArray.flat custom implementation: https://www.youtube.com/watch?v=v1sWRw5azYU&list=PLmcRO0ZwQv4RWqjZCajaKBAdCJjmkAL_I&index=4\n\
  \nInterview Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nJavaScript Custom implementation Series:\nhttps://www.youtube.com/watch?v=eGzErMUfdpk&list=PLmcRO0ZwQv4RWqjZCajaKBAdCJjmkAL_I"
author: careerwithvasanth
duration: 00:10:18
model: saaras:v3
transcript: true
---

# Only 1/100 can solve this Meta Interview qstn, Flatten Array without Recurssion (MAANG Series Pt -3)

## Transcript

### 00:00:00 · Speaker 1

So today I have picked up a question which is asked in Facebook or Facebook or Meta, Amazon, Apple, Google, also in Microsoft, okay? Five companies have asked this. Don't think it is very old, even in last April, twenty twenty two April also they have asked this question.

### 00:00:20 · Speaker 1

Hello all, welcome back to Uncommon Geeks. Myself Vasant. I hope you all doing well. So as you already know this is a video series where we are discussing about the most common interview questions that are asked in MANG. MANG stands for Meta or Facebook, Apple, Amazon, Netflix and Google, okay? So today I have picked up a question which is asked in Facebook or Facebook or Meta, Amazon, Apple, Google, also in Microsoft, okay? Five companies have asked this. Don't think it is very old, even in last April 2020

### 00:00:50 · Speaker 1

to April also they have asked this question. Okay? So it's not I have already discussed solution to this question in different ways in my articles and also in one of my video. But in this particular video I am gonna give a all altogether different approach towards that problem. This is very very important video if you are preparing for MAG interviews please watch this video till the end. Okay? Without wasting further time let's get started.

### 00:01:14 · Speaker 1

So, this video is mainly on flattening the array in JavaScript. Okay? So in my medium blog, I've already written a beautiful article to explain how to flatten a given array in JavaScript. Okay? So to be very precise, if given this as an input, one, two, comma, three, five, six, seven, which is a nested array or array of array, so you should flatten it. That's the requirement. Okay? I've written a recursive solution here. In my previous video, where I have explained a custom implementation of array dot flat, even there, I have written a recursive approach.

### 00:01:44 · Speaker 1

yourself. But in Facebook interviews, they have asked both solutions, like an iterative solution, also a recursive solution, okay? So in this video, I'll be discussing the iterative approach. So in same interview for the same candidate, they'll ask both approaches to it. The reason being how many different solutions that you can come up for a single problem, okay? That's very, very important when you're applying for companies like this, okay? Let me start by explaining you the flat first. So it is here, as you can see. So if you run, so this

### 00:02:14 · Speaker 1

three comma four went away. If you don't pass anything inside the flat, it is considered as zero hierarchy, okay? So one level of hierarchy it will remove. Not zero hierarchy, one hierarchy. One array inside this array will be removed, one level of hierarchy. If you pass infinity, then it will remove all the

### 00:02:31 · Speaker 1

hierarchy. No matter how many array inside an array, it will remove all the arrays and it will just make sure the entire array is flattened. Okay? So this is about the array.flat.

### 00:02:42 · Speaker 1

and what recursive approach for this I've already shown you here how we can write a recursive approach. So there is also iterative approach which I've taken from here, okay? I have not written this logic, I've taken this logic from here itself. I assume if it is documented here this could have gone through lot of iterations and best minds of the world might have approved this. So I am also picking the same and I'll be explaining you how to do that, okay? I'll link this also in the description so that you can go ahead and read by yourself as well, okay? Also my blog where I've explained the

### 00:03:12 · Speaker 1

recursive approach very clearly. Also I'll link my YouTube video where I've explained the recursive approach. Now, without wasting further time, let's get started. But before I start writing any code for the flattening, if you are someone who is seriously preparing for JavaScript related interviews like Vue, Angular, Node, React, etc. So I would highly advise you to go ahead and watch my basic interview questions. So I've linked that on the screen also in the description. So twenty plus videos which are most commonly asked across all the companies, okay? And how

### 00:03:42 · Speaker 1

approach that problem, what mistakes can they do, how to avoid that, all of that I've explained in the series. If you don't watch that and directly landed here, the problem is this is advanced level questions. So companies like MANG are asking it, correct? So if you have not watched that and directly landed in this video, problem is you may not go to this level only in the interview, because every interview starts the basic question. If you're answering the basic, he would go for the advanced. If you're not answering basic question itself, then there is no point, correct? So watch that series and come to this video, okay? Also, I've created another video series custom implementation

### 00:04:14 · Speaker 1

So how to write your own array.map method, array.flat method, array.concat, all of this, okay? So please watch that series also, that has become very, very trendy question across all the high paying jobs now. Implement your own functions. Watch that series also and come to this as a next level of further preparations, okay? Now, without wasting further time, now let's get started. So crux of the logic I'll explain first. So you have an array, a nested array, okay?

### 00:04:41 · Speaker 1

one, two, three, comma, four. Okay? So three, comma, four is a nested array. Okay?

### 00:04:47 · Speaker 1

inside the entire array. What you would do is you will get the last element of this, okay? By just array dot pop. Okay, array dot pop would give you the last element, correct? So you can log last. Then what you would do is you will push that value, push that array back into the uh the source array, but without using the array brackets. So how you would do that is array dot push, you will just spread the last.

### 00:05:17 · Speaker 1

Okay, so what this does is three comma four will turn into three comma four. Okay, just the array bracket will be eliminated due to which the output will be if you log it now array, it will be one comma two comma three comma four. Okay, that array bracket will be gone. So this is the crux of the logic. So what you would do is you'll take the last element and insert it back to the array if it is an array, if it is

### 00:05:47 · Speaker 1

not an array, in the case of one and two it is not an array, then just push this values into a result. Okay, let me run this.

### 00:05:54 · Speaker 1

So you are saying three four was the last. Correct? This was the last.

### 00:05:59 · Speaker 1

one two three four is the array that is the final output. So this is a crux, okay? First you should always try to find out the crux or a repeating pattern in the question with which you can form a solution. So now you know the crux. With this logic you will be implementing the actual implementation, okay? So I don't need these so I'm removing. I would need this the two statements I'll keep them, okay? Function now I'll create flatten array, flatten array is my function, okay? Which will take input as the input array.

### 00:06:34 · Speaker 1

So I would call flatten array from this log, okay? What I would do is I'm using a variable called stack. Actually it's a stack based approach only. Stack I think most of you know first in last out, okay? Arranging of plates, you pick the last plate in the first. Now here

### 00:06:52 · Speaker 1

original spread operator, okay? So here usage of spread operator is because not because of anything any significant reason. It is mainly because this input is used, uh not to use the same reference of this array, okay? They want to use a different array reference here. So you are using dot dot dot input here, okay? As array passed, always array is passed as a reference and not by value, okay? Now, now it's very simple, what you would do is, you also need an variable to hold the output. Cons response is this, okay? Then you have a while loop.

### 00:07:24 · Speaker 1

inside which you will check and you will run this till stack is not empty. Okay? Then what you do is very simple. Same like you will get the last element from the stack by using the stack dot pop. Okay? Here, two two things are possible. One array is one the last value is an array, second last value is not an array. Correct? So if

### 00:07:49 · Speaker 1

and else. See, I have practiced this solution before giving explaining you guys, but otherwise also, I will have a solid bifurcation of the problem, correct? So first I know the crux. Then I know what are the major two conditions. If this condition what I do, this condition what I'll do. An algorithm should think, algorithm should run in your mind, then only you'll be able to write an efficient code, okay? So please do follow in this direction whenever you are thinking in the interview. Now if first you need to check whether last element is an

### 00:08:19 · Speaker 1

array. So you know array.isArray method is available which will help you to identify that. So I'm passing last here.

### 00:08:26 · Speaker 1

So if it is not an array, in this case one and two are not an array, you can directly push it into the result, correct? result dot push, you are pushing the array of, sorry, you are pushing the last value, correct? If it is an array, then also you know by the crux what you need to do, correct? You will push the value back into the stack, only thing is you will extract it. Only thing is you will use a dot operator just to get the remove that array bracket, spread operator you will use to get the values out of the array.

### 00:08:56 · Speaker 1

Okay? Then you have to return the result. Only thing that you have to make a change here is you have to reverse the return. The reason being you are popping the values, putting other way, iterating the array from the last. So you have to reverse it and you have to send it as a response. Okay? First let us run, then we'll see what is happening. So three comma four is happening, let's say I put five here.

### 00:09:19 · Speaker 0

Yeah

### 00:09:20 · Speaker 1

So it is flattening.

### 00:09:21 · Speaker 0

Okay

### 00:09:22 · Speaker 1

So that's about the crux of the logic and how to flatten the array in an iterative approach. Okay? So so Vasant, why pop? Can we now do this by using the first, like rather using the last element? Can't we use from the first element? Obviously, you can do that also. Like you would start iterating from this, keep pushing the values, then whenever an array is encountered, then you can you can follow the similar approach. Even that is also possible. Okay? I'm just sticking to the Mozilla approach considering that could be the best approach possible. Okay?

### 00:09:52 · Speaker 1

So if you like the content that I have made in this video, please do like this video on YouTube channel. Do not forget to share the videos with your friends. And please do subscribe to my channel Uncommon Geeks that will help me to make more such good content. I also link my medium blog this in this video link in the description. Please do subscribe to please do follow me on the medium as well, okay? I'll be putting the solution in my GitHub repository, you can copy that and practice on your own, okay? Thank you again for watching this video. Catch you in the next one.
