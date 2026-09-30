---
id: DeboHpbzVu8
title: Five questions that cover entire hoisting in JavaScript Part - 2 (Hoisting
  Ep - 3)
date: '2022-02-23'
url: https://www.youtube.com/watch?v=DeboHpbzVu8
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ My Medium Blogs - https://mevasanth.medium.com/ \nGithub URL which contains questions\
  \ - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\nHoisting\
  \ Video Part 1 - https://www.youtube.com/watch?v=skkXL5QdDwk\nHoisting Video Part\
  \ 2 -  https://youtu.be/U1BXdBkXFgw"
author: careerwithvasanth
duration: 00:11:33
model: saaras:v3
transcript: true
---

# Five questions that cover entire hoisting in JavaScript Part - 2 (Hoisting Ep - 3)

## Transcript

### 00:00:00 · Speaker 1

So here we are going to mainly discuss questions on a hoisting. Different questions that generally asked during the interview on the concept of hoisting. Okay. As you've already understood what is hoisting in my previous video if not the link is in the description please go ahead and check this video because

### 00:00:16 · Speaker 1

you need to understand the concept before answering the questions. Okay? Very first question that I am asking here is

### 00:00:25 · Speaker 1

explain the scope of temporal dead zone. Okay. So question number one, this is on the snippet driven, uh how we generally categorize where there is a code snippet given and we want you to analyze that code and answer the given question. So this is a seasoned interview who generally takes interview, they will have their own set of code snippets which is generally showed to the candidates during the interview. If it's a virtual, they will share it, if it's a real, they can show it on their monitors and then

### 00:00:55 · Speaker 1

ask you to interpret the code and come with the answer. Okay. Now let's see what is my question here. My question is quite straightforward. I want you to answer in the given snippet where the temporal Ted zone starts.

### 00:01:09 · Speaker 1

where is actual temporal dead zone and where the temporal dead zone ends and which is the statement or which line exists outside the temporal dead zone. This is my question. Okay? So I I believe you already aware what is temporal dead zone. Okay? Now I want you to answer this question. So let's make it simple. If you are not aware or if you know the answer then mention the question that is question number one and put your answer in YouTube comment section.

### 00:01:39 · Speaker 1

Why I'm asking this is, if I if I'm the only one who is explaining, the video becomes one-sided. If you if you mention the answers, then it will become interactive. Okay?

### 00:01:51 · Speaker 1

Now, uh let let me answer this question, okay? For those of you who haven't uh who are not fully sure of it, okay? Basically, we have created a variable with a keyword let and the variable name is letvar. Uh this

### 00:02:05 · Speaker 1

example is straight away taken from developer.mozilla.com, okay? mostly I refer all examples from developer.mozilla.com because that's a single source of truth. anywhere in the world if you see a video or a documentation that was written on any JavaScript topic, it is directly either taken from the developer.mozilla.com or referenced internally to any other documentation. So I generally go and straight away check in the developer.mozilla.com. I suggest you also do the same. Now,

### 00:02:31 · Speaker 1

This is the statement where, uh, line number six is we are declaring the variable let var, which actually get hoisted to the top of this block. That is in this case now line number five. Here temporal dead zone starts.

### 00:02:45 · Speaker 1

okay? Where the temporal dead zone ends, basically whenever you define the value or initialize the value to a variable, then the temporal dead zone will end, okay? What is the reason of temporal dead zone? Between the start and end.

### 00:03:00 · Speaker 1

This is a temporal dead zone, actual temporal dead zone is this. So no matter how many lines of code you write in this, uh this entire region will be a temporal dead zone for variable let var. So you will not be able to access the variable of let var there. Okay? So this was my question number one, uh where I've answered it. If you have also answered in the comment section, I'll reply back to your comments. I'll try to reply back to your comments, okay? Now I'll ask the second question. So second question on the same snippet, so I'm not changing the number here. So second question what is the output of this program?

### 00:03:33 · Speaker 1

So if you know the answer again do the same thing mention your answer on the comment okay. I'll execute it. So we are getting like output as three. So what happened was we created a variable called let var three. uh this got hosted here and a function to

### 00:03:51 · Speaker 1

print that value of the variable letvar. But good thing is we um the function was called in line number nine by the time which the variable letvar was already defined or initialized. So we are we are not having any problem uh in printing this value. So the function no function function defined with the name F U N C knows what is letvar and it is printing it. So there is no problem. Now let me do a small variation to this.

### 00:04:17 · Speaker 1

Okay. I'm removing these comments because I'm kind of uh gambling the code or moving the code up and down. So those statements may not hold good. Tell me the output of this. This is the third question on the same snippet I'm asking. The reason I'm showing you this variation is you have to be very confident on this temporal dead zone concept so that once you watch my video you will be able to answer any questions on temporal dead zone. Okay. If you know the answer again comment it by mentioning the video time and your answer.

### 00:04:45 · Speaker 1

you're getting a reference error cannot access func f u n c before initialization. So, ideally you in the previous video you saw the function declared with the keyword f u function was getting hoisted. But arrow functions are generally which are declared with the keyword const are not hoisted. So we are trying to call a function which is not hoisted so you will not be able to call it from here. Okay? You have to call it only below this. Okay? This is another question. Arrow functions are not hoisted. Okay? So now I'm calling this function.

### 00:05:15 · Speaker 1

from the line number six. This also I want you to guess this output as well, okay? Now if you know please comment, otherwise I will run the code for you. So now I'm getting a reference error. This is the temporal dead zone error where cannot access the variable let var before initialization. We are trying to access the variable of let var even before it is getting initialized. So this is a temporal dead zone error, okay? So I I showed you all the variations of it, what is going to happen and where the temporal dead zone starts and where the temporal dead zone ends.

### 00:05:44 · Speaker 1

function which functions are hoisted I mean the normal functions are hoisted the arrow functions are not hoisted so these are all the variations of the question that can be asked around temporary zone so please be sure of all these things okay

### 00:05:58 · Speaker 1

Now, since you are aware of all these things, I'll go to the question number two. This quietly, this is more on the quietly on the theoretical part, okay? Why warehousing is present in JavaScript?

### 00:06:14 · Speaker 1

If you know the answer, state it or go and answer in the comment section. If not, listen to my video. See, I in the previous video, I explained you what is hoisting and what is variable hoisting or variable declared with the keyword where you are getting hoisted, okay? And they are also being initially this is the value of undefined, okay? And variable declared with let and cons are being hoisted, but they are not declared with a variable of value of undefined. This question I have mainly taken here because after I want you to inculcate this culture where you start

### 00:06:44 · Speaker 1

asking why for everything. uh for example now, I explained you variable created with var keyword or hoisted and the value is undefined initialized to undefined. But let and const are hoisted and value is not defined to value is default value is not initialized to undefined. Why only variable created with var keyword are initialized? Now why not let and const? Okay. Only when you ask such questions in your mind you will be able to find out somewhere that on the internet and that that inquisitiveness inside you will make

### 00:07:14 · Speaker 1

to learn more. Okay, this question is mainly taken on that purpose. I got this question when I was learning hosting and the answer I found out on the internet is this.

### 00:07:23 · Speaker 1

The JS creator Brendan once said that var hosting thus an unintended consequence of function hosting. No block scope JS as a nineteen ninety five rush job. So he basically mentioned this was not an intended job. Variable hosting was not something that was intended. Hosting the variable and initializing it to undefined was happened during during the rush on the release. I believe it was not removed in the later terms because variable creator var keyword has a global scope. So they might have hosted they they kept

### 00:07:53 · Speaker 1

uh since it is already accessible throughout the scope, uh they might have that undefined whatever they initialized was not removed. Okay? This is what my assumption I did not get answer anywhere. It will be great if you find somewhere the answer, uh why even if it was a bug that was done in the rush for release, why it was not removed. If you find answer anywhere, please mention that in the comment section. Okay? This is question number two. Now question number three.

### 00:08:18 · Speaker 1

how hosting works in JavaScript

### 00:08:26 · Speaker 1

If it is interpreted

### 00:08:29 · Speaker 1

This is another interesting question. This also you you have to ask yourself. These questions will not come suddenly somewhere like no one will write answers to this right away. So these are the questions that you have to come come upon your own when you understand the topic and then you have to find the answers. Okay? As you know JavaScript is interpreted. Interpreted means line by line. Okay? Log uh X is. Okay? So JavaScript interpretation in general means uh this line is executed, then this line gets executed, then the next line. Line by line execution. It's not like entire programming.

### 00:08:59 · Speaker 1

taken as an input then it is compiled and given as output which happens in the compiled languages okay so here let's go with the var only so we are trying to access the variable x okay if it is an interpreted language where line by line execution happens how come if you run this code we will get the value of undefined I mean x got hoisted okay if it's a line by line execution how come line number six went up before line number five hope you are understanding the question

### 00:09:29 · Speaker 1

If it's an interpreter, how hosting will work? Okay. If you know the answer, please put it in the comments, but answer to this is in the way how the JavaScript engine works. Okay.

### 00:09:42 · Speaker 1

JavaScript engine or the compilation happens in two steps like I already mentioned. First step it scans the function, allocates the memory and second step where the actual execution happens. Okay. But even this doesn't answer how interpreted languages like JavaScript will get a capability of concept of hosting. Okay. This basically happens because JavaScript compilers are not written in JavaScript. They are written in some other programming languages like C++. Let's take an example of Google Chrome which uses a JavaScript engine called V8. So V8 is written in C++ which is

### 00:10:12 · Speaker 1

object oriented programming language and it's a compiled language it's not interpreted. So what happens is that entire JavaScript code that you wrote on Google Chrome is passed as an input to V8 engine and this V8 engine processes the code and it will execute the code in two steps which will give it a capability of concepts like hosting. Even though JavaScript is interpreted because of the reason where the compilers are written in some object oriented language or the compiled languages which have which can give a capability

### 00:10:42 · Speaker 1

like hosting, it is available in JavaScript at the moment, okay? Just as a JavaScript is always an interpreter language, just because of the compilers, we are getting the, just because of those compilers which have the capability of running the JavaScript in two steps. So that is the reason why we are getting the concept of hosting in JavaScript. This applies to many other concept which interviewer could ask you how this works in JavaScript if it is interpreted. For all those, the reason is same because of the compiler capabilities. It's not JavaScript itself

### 00:11:12 · Speaker 1

JavaScript itself capability. Okay. So these were the three questions that I want to discuss in this video. If you like the video, please like it on YouTube and share it with your friends and subscribe to our channel Uncommon Geek. Okay. And if you want me to make any video, any particular video, please mention that also in the comment. I'll try to make that those videos for you. Thank you.
