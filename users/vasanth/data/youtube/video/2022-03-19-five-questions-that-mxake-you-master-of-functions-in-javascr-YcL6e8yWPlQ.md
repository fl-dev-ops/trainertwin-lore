---
id: YcL6e8yWPlQ
title: Five questions that mxake you master of functions in JavaScript Pt -1(Functions
  Ep - 3)
date: '2022-03-19'
url: https://www.youtube.com/watch?v=YcL6e8yWPlQ
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ If you know how to call functions and what it returns, you can clear half of JavaScript\
  \ interviews. \n\nJavaScript functions could be the topic, on which most interview\
  \ questions can be formed. Because it contains other subtopics like closure, currying,\
  \ nesting of functions etc. Most tricky questions can be easily formed in this topic.\
  \ I will cover each and every topic of functions in this series, watch it carefully\
  \ and practice well, you will definitely answer all questions on this topic in upcoming\
  \ interviews\n\n\nMy Medium Blogs - https://mevasanth.medium.com/ \nGithub URL which\
  \ contains questions - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \ Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\nDeep\
  \ copy and Shallow copy part 1 - https://www.youtube.com/watch?v=OFJmoIRyqw4&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t&index=7\n\
  Hoisting in JavaScript Part 1 - https://www.youtube.com/watch?v=skkXL5QdDwk&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t&index=2"
author: careerwithvasanth
duration: 00:10:13
model: saaras:v3
transcript: true
---

# Five questions that mxake you master of functions in JavaScript Pt -1(Functions Ep - 3)

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome to Uncommon Geeks. Myself, Asanth. I hope you all doing well. So, as you know, I've already discussed about functions and different aspects of the function in my last two videos and this this video, like I promise, I'm going to discuss question and answers that are generally asked on functions. Okay? In case if you have not seen my previous video, I would highly advise, please go ahead and watch it. I'll add some description somewhere on the link and also somewhere on the screen. The reason being where that is those are the videos where I've explained the concept and if you directly land in this video, you may face a difficult to answer. Okay? the question that I ask in this video, okay? Without wasting further time, let's get started.

### 00:00:38 · Speaker 1

So, this is the question number one, very straightforward. If you watch my first video carefully, you'll be able to answer this without any problem, okay? So,

### 00:00:47 · Speaker 1

If you know the answer already, mention question number one in the comment section and put your answer. For those of you who are not so sure about the answer, I'll let me explain the question to you first, okay? So we have a anonymous function called const square, okay? Where square is a function.

### 00:01:04 · Speaker 1

And inside the square what we are doing is we are basically whatever the input that we are getting, whatever the value we are getting, we are squaring it n into n, okay? And in line number two we are trying to log the square and in line number three, we are trying to invoke the square function by passing the value of phi, okay? My question is what will be the output? Now after I explain the question in case if you understood and you know the output, please do mention question number one and put your answer. If not let me execute it then I will explain what is happening, okay?

### 00:01:34 · Speaker 1

or without executing also. First let me let me walk through what's happening, okay? So line number four constant square. So and in line number two you're trying to print square. Just see this part, okay? Let's say this part is not there, okay? This part is not there, only this is there, what would have been the output?

### 00:01:51 · Speaker 1

you would have got a reference error because const is hoisted but it goes to a temporal dead zone. So line number two square has no value, correct? So due to which you would get a reference error, right? So what's happening is the same. So here here you should should get a reference error, correct? So why I'm explaining this is you have to break down the question into chunks and understand it carefully and tackle it. So now you know here we get a reference error. First let me execute it.

### 00:02:17 · Speaker 1

So reference error cannot access square before initialization. Which is right. The same way we predicted the output is coming. So if there is a reference error or a reference error is actually a runtime error. If the program crashes here, it doesn't go to the next blocks. So we don't know what is happening here. Okay? Now, uh what would happen here is also I have explained in the previous video. That is the variable declared with const is hoisted, but the function is not hoisted. So whenever you try to invoke square, you will get an error that uh

### 00:02:47 · Speaker 1

I mean basically I don't know where the function is. I don't know the exact error so I'm telling but the error would symbolically mean the same. So I will comment this line.

### 00:02:54 · Speaker 1

and let me execute it here. So you would get reference error cannot access square before initialization. It's saying the same I don't know man where is square. I cannot invoke it. Okay. So now. So this much if you have understood and you know basically square is the very important thing you have to know here is const square is hoisted but it is in temporal dead zone. Square of phi is not hoisted. So this is the expectation from the interview point of view. You should know in depth what is happening. Okay. Now. So Let me do this

### 00:03:26 · Speaker 1

rather having const I'll make it var.

### 00:03:29 · Speaker 1

So only if you know the concept of hoisting variable you will be able to answer it. Otherwise no. So if you don't know what is hoisting, I'll link the hoisting videos of mine in the description, go ahead and watch it. So basically what's happening here is we have a function called square. This has a function. You know that

### 00:03:45 · Speaker 1

variable created with a var keyword or hoisted. And initialized with a default value of undefined. So what should be here? It should be undefined. Here, you you only guess what will happen here.

### 00:03:58 · Speaker 1

obviously. This will get hoisted. Again the function will not be hoisted. So you get a reference error there also but this line will execute successfully and the output you get is undefined.

### 00:04:08 · Speaker 1

See, you're getting undefined, then a reference error. Okay? This was about the first question. So to answer this first question, you should know the concept of hosting. You should know the concept of anonymous function and hosting with different keywords like let var key and to an extent the scope also, then only you'll be able to answer it. Okay? Let's go to the question number two.

### 00:04:30 · Speaker 1

So question number two is here. Very straightforward question.

### 00:04:34 · Speaker 1

Okay. Glance at the like glance at a question. If you want pause the video, uh glance through the question. If you know the answer, mention question number two and answer it. Okay. This is very straightforward question. The reason I've taken this type of question is, um it looks very easy, but unless you have a deep understanding about the fundamentals of JavaScript, you may end up doing a wrong answer. Okay. For those of you who are still struggling to answer, let me give let me walk through the question. So we have a function called test which basically takes an object and object

### 00:05:04 · Speaker 1

text make we are changing here and in line number twenty one we have an object called car details which has make model and year okay what I'm doing here is car details make one car details dot make car and I'm calling the function test then again I'm printing the same so this is first and second before invoking function after invoking function okay this is an object now if something is flashing in your mind pause the video work on it then mention question number two and put your answer okay still it is not flashing you are not able to identify what is happening let me walk through

### 00:05:35 · Speaker 1

So we have a object called car details and this has three things. So to answer this question I'll give you one hint you should know what is deep copying and shallow copying in JavaScript. If you don't know what is deep copying and shallow copying I'll link my videos on deep copy and shallow copying in the description or also somewhere on the screen. Go ahead and watch it then come back to this definitely you'll be able to answer okay. uh So this car details is an object. So whenever you call a function and pass the object okay. But but I'll tell before I explain the answer in detail what most of you might have guessed.

### 00:06:05 · Speaker 1

So car details dot make is Honda. So first thing will be car details dot make one will be comes as Honda. And second you are invoking after you invoke a function but car details make two and you are trying to print make. So no matter you called a function or not because function is something the whatever change you do that is inside this block. So you would think nothing affects and here also it will come as Honda only both. But it doesn't work like that, okay? The first I'll show you the output. So first you get Honda, second you get Toyota, okay? The reason being

### 00:06:35 · Speaker 1

whenever you call a function and pass the reference type. So whenever you passing an object it is not a pass by value it's a pass by reference. So you are modifying the reference here when you modify the reference obviously you will be both the I mean whatever you change and modify here or here they both internally point to the same reference. Okay you may have variable A and variable B but ultimately they are pointing to the same memory location. So even if you change it here it will get changed in the outside also. So due to which the variable is getting updated.

### 00:07:05 · Speaker 1

okay? So to answer this question you should know what is deep copy and shallow copy, you should know what is function, correct? And after knowing all those things definitely you will be able to answer it.

### 00:07:15 · Speaker 0

is about

### 00:07:16 · Speaker 1

question number two. Let me go to question number three. Okay. This is a slightly tricky one. not because of complexity because of the arrangement of the things so you may get slightly confused.

### 00:07:30 · Speaker 1

If you want to go glance through the question, pause the video, glance through it and work out and if you know the answer, mention question number three, put your answer or if you're facing little difficulty, let me walk through the question.

### 00:07:39 · Speaker 1

So what we have is we have a function called get store and inside that we have two variables called variable number one and number two. You already know from the property of closure so add is an inner function get store is an outer function this together is a function nesting. So add function has access to these variables which are declared outside. Okay this you already know. Now what we are doing name

### 00:08:00 · Speaker 1

scored number one and number two. Number one and number two are defined here. But the name is something that is not defined in the outer function. But it is defined outside the function. So which is in line number forty two. So will this closure have an access to that name? If it doesn't then it comes as undefined.

### 00:08:16 · Speaker 1

If it has an axis, then it should print chamak. Okay? So think through it and put your answer. Now I explained the question very much in detail and I've broken down the different parts also. So if you know the answer, guess the answer. Let me show you what happens.

### 00:08:32 · Speaker 1

So chamak scored five is output. So name has come from here. Scored is a string. Number one and number two are basically taken from here.

### 00:08:41 · Speaker 1

Now you know what might have happened. So the name though name is defined here, it is able to access this name. Okay? Because basically the closure definition says the same. Variables declared or the variables in function declared outside of the function can be accessed inside the function, that's the property of closure. If you remember from here. Okay, I've removed the definition. That is what the closure is, so it has access to the name. So due to which we are able to uh get the name as a chamak. Now I'll give a small assignment.

### 00:09:11 · Speaker 1

You have a number one number two here and number one number two here. Remove the number two from here. Okay? Then number one number two addition what will happen check whether will it given throw some error or will it take the number two from here. Okay that's a small assignment for you. So mention question number three A and if you are able to solve that put that in the comment section. Okay? So these are the three questions that I wanted to cover for this video because we are already almost around ten minutes so I don't want to stretch this video. I have couple more questions on the normal function which I'll be asking next video.

### 00:09:41 · Speaker 1

If you like my video, please do like it on my YouTube channel. If you want your friends also to get benefited from this, benefited from this, please do share with them. Do not forget to subscribe to Uncommon Geeks.

### 00:09:52 · Speaker 1

And I have linked my medium blogs links on the URL in the description section where I have written a lot of articles on the different topics and my GitHub URL is also on the description where this project whatever the questions you are seeing right these projects are being uploaded you can download it follow me on GitHub and practice all those questions. Thank you so much for watching catch you in next video.
