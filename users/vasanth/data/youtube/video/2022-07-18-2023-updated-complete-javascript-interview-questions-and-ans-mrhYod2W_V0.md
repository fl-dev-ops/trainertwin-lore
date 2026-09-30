---
id: mrhYod2W_V0
title: 2023 updated ! 🔥 Complete Javascript interview questions and answers🔥 [All
  common topics covered]
date: '2022-07-18'
url: https://www.youtube.com/watch?v=mrhYod2W_V0
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ JavaScript Interview Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nMedium Blog https://mevasanth.medium.com/ \n\nFollow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  \nMedium Article about frontEnd developer interview preparation: https://mevasanth.medium.com/dont-skip-top-5-frontend-interview-topics-to-prepare-in-2022-8adc8801677e\n\
  \nGithub Repository that contains examples: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \nJavaScript Custom implementation introduction: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\
  \ \n\nMAANG Series for frontEnd dev:\nhttps://www.youtube.com/watch?v=s-b-txm_Gvk&list=PLmcRO0ZwQv4SNhbW4CI4vc-6IHBHCKzZN"
author: careerwithvasanth
duration: 00:41:44
model: saaras:v3
transcript: true
---

# 2023 updated ! 🔥 Complete Javascript interview questions and answers🔥 [All common topics covered]

## Transcript

### 00:00:00 · Speaker 1

printed three times, correct? Many will tell this answer rightly in the interview because of this becomes so common. Next question that I ask is with what interval?

### 00:00:10 · Speaker 1

with what interval it is printing three. For example, three one second, three one second, three or one second delay, three three three. No delay, all three at once, three three three, suddenly. Now again candidates get confused because nowhere this is explained.

### 00:00:33 · Speaker 1

Hello all, welcome back to Uncommon Geeks. Myself Asant. I hope you all doing well. In case if you are seeing for the first time on the internet, I'm a content creator. I help people to clear their interviews. I have made lot of beautiful series in the past which has been appreciated by many. So today I am back with a brand new video where I will be discussing about complete interview preparation gate for front end developer. So if you are applying for any role, JavaScript related, just apply in JavaScript, HTML, CSS, Node.js, View.js, Angular.js, React.js, React Native, no matter any

### 00:01:03 · Speaker 1

base role that you are applying there will be one common round where the fundamentals of JavaScript are tested. So because all the frameworks that has evolved over the JavaScript they can come anytime soon like new framework can come tomorrow but JavaScript as a language hasn't changed. So the fundamentals of JavaScript are very very essential for all these roles. So there will be at least one or two rounds even if there is let's say there is a round for testing your React skills React JS skills. In that round also interviewer will be asking you some or the other JavaScript questions to make sure are you familiar with JavaScript concepts.

### 00:01:33 · Speaker 1

then only you'll become a very good programmer in React, correct? So all the topics, important topics that are asked and some questions in that also I'll be discussing in this video. So please watch the video till the end, not for any other reason, just for you to clear your interview, okay? Without wasting further time, let's get started.

### 00:01:50 · Speaker 1

So, I have created one uh small presentation, okay, which covers uh different topics that are most commonly asked in the interview. I'm going to talk about the topic a little bit, okay? Then probably I'll get into the question that are asked in the topic. If required, I'll also show you the official documentation of this topic, what all it contains, okay? So let's get started with the very first topic that is hosting, okay? Hosting is considered to be one of the very, very important interview questions. In fact, I have overall if I say if the interview that I've taken and interview that I've given, I have covered more than two hundred interviews, okay?

### 00:02:20 · Speaker 1

There has been very very few interviews where hosting concepts are directly or indirectly are not asked. Very few interviews. In most interviews the first, second or third, top third question in most of my interviews with respect to JavaScript was hosting. Okay? Why it is very important I've explained in my other videos, I'll try to link that on the screen also in description. But in very simple words, hosting, uh, whenever you're learning hosting, there are a lot of things you learn internally. Uh, like the variable declaration, the scope of the variables. So interviewer by asking one question, he can check lot of

### 00:02:50 · Speaker 1

different skills of yours. Due to which the hosting has become very very important. Let's see the definition. So and very important. This video is going to be slightly longer. I don't know how many minutes but it's going to be slightly longer. You have to bear with me because it's going to be one video that will brush up all your basic skills of the JavaScript interview preparation, okay? So official definition. JavaScript hosting refers to process whereby the interpreter appears to move the declaration of function variable classes to the top of their scope prior to execution of the code. Correct?

### 00:03:21 · Speaker 1

So in case if you uh go to the official documentation, correct? I'm I'm opening the official documentation here with respect to hosting, correct? So JavaScript same thing, the definition was taken by here itself. I am no one to give a definition for hosting, whatever the definition in Mozilla, same definition I'm also giving, okay? So here if you see the same is response JavaScript refers to move the declaration of function variables class to the top of their scope. So this is fine, I guess most of you are aware basics of hosting. So this is not like absolute beginner video, you need to have some basic sense of JavaScript to get along, okay?

### 00:03:51 · Speaker 1

this is like a brush up for your entire interview preparation. So, in case if you really don't know what is hosting itself, I'll link this my playlist in the description. So where I've clearly created, I created three videos and explained the hosting very much in detail. Like how my first five questions that are very important from hosting, five questions that cover the hosting, all of these are very detailed explained in this series, okay? So but in very simple words hosting as you know is like a uh moving the declaration to the top of the functions, correct? So in very simple words

### 00:04:21 · Speaker 1

Let's say, these are the examples which I want to discuss but let me keep it little slow. I'll give a small thing to explain, okay? Let's say you're creating variable X and you're logging

### 00:04:36 · Speaker 1

log x, okay? If I do node hosting, so undefined. See, you're trying to uh you're you're trying to printing the value of x after it is declared, you're getting undefined, which is fine because no value was initialized. So it has been declared but not defined, all right? Not initialized. Same if I do on top,

### 00:04:57 · Speaker 1

I'm sorry

### 00:04:58 · Speaker 0

Mmm

### 00:05:01 · Speaker 0

Node

### 00:05:03 · Speaker 1

hosting. So you're seeing undefined, even in this case also you're seeing undefined, correct? So why you are seeing undefined when you are trying to access the valuable even before it is declared. This is because of the hosting where the JavaScript interpreter appears to move the declaration to the top of the block, okay? So first question that I ask whenever I'm whenever candidate gives this answer, I'll ask first give the definition of hosting. Many try to write and explain, okay? I kind of stop them there itself. I'll say don't write. Try to express it.

### 00:05:33 · Speaker 1

at first. The reason being as an engineer you will not get a option to always write and explain, correct? You need to coordinate with lot of teams. So you should have at least moderate communication skills to explain the technicalities, correct? So what is hosting? Candidates say, candidates say it's moving declaration to the top of the block or top of this clope is known as the hosting, okay? So then I'll ask is it really moving the definition or declaration or sorry declaration to the top of the block? Then they're like yeah it is moving but not like

### 00:06:03 · Speaker 1

cannot see it. It is happening in the background or some people say back end. So it is not back end, please don't say that. At least say it is happening in background, okay? Fine. So then I'll ask, is it really happening where the declaration is moving to the top of the block? Some say yes, some will get confused. So, why I'm saying this is don't read thing as it is. So if you somebody is saying somebody has written in the blog and you start following it, no. Look at this definition carefully, carefully again. Hosting refers the process whereby the interpreter appears is to move the declaration of a function variable classes to the top of their scope.

### 00:06:37 · Speaker 1

pre-execution of the code. Here very very important thing that you have to notice here is it appears to move. It is not moving. It just creates an impression that it is moving. Why? Because it is just as you know JavaScript execution is two step. First step is initialization, second step is execution. In first step of initialization it will allocate memory to the variable X, okay? So in this scope, let's say it is declared like this whether you can make the above one function or any other thing. So now what is

### 00:07:07 · Speaker 1

is happening whenever the compiler is running through the interpreter is running through this block in the first run variable x is allotted a memory. Correct? And in the second run is when the console.log is printing. So for us it feels like variable x is present here. Correct? Variable x is present here and the value given is undefined. So this is just a appears to or feels like but this is not what happening, okay? And even in the background also this is what not happening. Very very careful about this point, okay? It just

### 00:07:37 · Speaker 1

years just because of the memories allocated to variable legs you are able to access it even before it has been initialized okay that is what hosting is now you also know that once after the candidate asked this question the next question I ask is about all these like I can say one after the other similar to multiple choice question I'll ask whether let is hosted

### 00:07:58 · Speaker 1

and some say yes, some say no, and then I'll ask whether const is hoisted. Some say yes, some say no. Okay? To I mean most will know this answer already, but let me clarify. The variable created with let const where all the three are hoisted.

### 00:08:12 · Speaker 1

I think this point I think somewhere you bookmark and keep. Variable created with let, var and const. All the three variable creations are hoisted. Okay? Very first point. Then what is the difference? So variable created with var is hoisted and initialized with a value of undefined. Okay? So only whenever you're trying to create variable x, it is coming as undefined. But let and const are also hoisted, but they are not initialized with any value. Okay? And they are in a temporal dead zone. So the inner range where they cannot be accessed.

### 00:08:42 · Speaker 1

So let and cons are hoisted but their memories are allotted but there is no value that is initialized to that. So until the let and cons are declared, sorry defined, you will not be able to use them, okay? Be clear about this very first because still whenever I ask this question the interview candidates are getting confused. Let and cons are hoisted or not, they are hoisted. So if candidate has answered these three questions correctly, first explain hoisting definition properly, let and cons are hoisted or not. Third question that I ask is whether functions are hoisted, okay?

### 00:09:12 · Speaker 1

Then many tell, yes, functions are hoisted. I I have seen very less candidates who say functions are not hoisted. Most say functions are hoisted and that is absolutely right, functions are hoisted. Okay. Then next question I'll ask is why functions need to be hoisted?

### 00:09:27 · Speaker 1

correct? So you know functions are hosted. Why functions are hosted? This is again a very very important concept. Then I'll ask somebody will not be able to answer then I'll ask him. You know the Java.

### 00:09:36 · Speaker 1

you know C# where everything is inside the class, correct? So you are able to call the function etcetera. But JavaScript is not like that and why hosting is present only in JavaScript and not other languages. Even Python has it but not any object on the programming language are not having hosting. Then candidates are linking like that, correct? So I'll I'll answer that question also. Why function need to be hosted? In fact I've answered this in my other hosting video as well which I showed you in my channel, okay? So if you see here if you have a function Next

### 00:10:09 · Speaker 1

you have a function test. Okay, in fact, this was my first example that I explained in my hosting series, but many are not finding time to watch the entire series, so I'm quickly summarizing it here. Okay? So if you see now, test and test here as well. So you want to invoke a function before and after it has been declared. This is something common that we all do when in our day-to-day programming, correct? So to make this accessible, there has to be way, unlike Java or C#, JavaScript doesn't have a class. Everything is not tied to a class, correct? There has to be another way where we can do this. So hosting

### 00:10:39 · Speaker 1

functions very very essential. Okay? This is the third question. Then let's say this also people are asked or if they have not answered now at least you know. Then next question I'll ask is arrow functions are hoisted. Then I'll ask whether normal functions are hoisted, then I'll ask arrow functions are hoisted. Many again get confused, no arrow functions are not hoisted. Okay? So these are all the things that basically I'll ask even before I getting into questions. So these are are you conceptually clear? Then I'll ask you the snippet driven questions. Lot of snippets I have already discussed in the this

### 00:11:09 · Speaker 1

series that I was mentioning. Here in each video you would see lot of snippets in this I guess five in this I guess four many questions I have discussed throughout the series. Okay? So that also you can watch to get more information. Here I'll just summarize few questions. Okay?

### 00:11:23 · Speaker 1

Now, let us start by the first question in hosting. As I mentioned, this video is going to be slightly lengthier, so please stay with me, okay? Now, even before I I start showing you the first question, I have the simple request, okay? So, see, I think most of you watching my videos since quite some time or this is the first video you might have landed, at least whatever you saw till now quite impressive, I believe, correct? Some things that are not usually taught on the internet, there are many videos, but very few have

### 00:11:53 · Speaker 1

summarize you for the interview preparation, correct? So it is how difficult it is to like this video and comment about what are the work I'm doing. Comment anything, whether if you're liking the entire whatever you heard so far, please comment like that. Or if you're not liking, let's say I can improvise somewhere, please comment that. Please like the videos. By liking you more and more, the videos will appear in lot of screens, lot of people screen. We call what YouTube calls it impression. More impression is more people will click the video, more clicks means lot, my content will reach lot of people. I have a

### 00:12:23 · Speaker 1

full cause of helping people to clear their interview, okay? So that can be possible only if this video reaches to lot of people. So please like and comment before you continue watching the video. Thank you so much. Now let us go to the first video, okay? So here, the first, sorry, not first question, not the first video. Here the first question is you're trying to call function one and function two, okay?

### 00:12:43 · Speaker 1

where function one I have written a message like I'll subscribe to Geeks for Geeks. If you are not subscribed, please do that. Geeks for Geeks is my channel name. And second function is welcome to Geeks for Geeks. Okay? So you are invoking both the function. So guess the output. This is the question. This is this is very simple question. There are quite variations of this question that is asked across. So I have also picked this question. Try to guess the output for of this this particular function. This particular block I can say. Yeah.

### 00:13:10 · Speaker 1

If you know, please mention hosting question number one and your answer. If you don't know, let me like and execute, but try to relate all the topics that I explained about the hosting so far. What I asked, is functions hosted in JavaScript? I said yes. So is it a normal function in JavaScript? Yes. So function one will be able to invoke this? Yes. What about the second function? This is always there will be a interviewer wants to create a confusion in you and see how you're reacting to that. Okay? So, Now this if you see function two, correct?

### 00:13:44 · Speaker 1

If this was not there, okay, most would have said welcome to Geeks for Geeks is the output. But now just because this is there, you start getting confused. So there is always a combination of one thing that looks very firm and another thing that creates a confusion among both, okay, between both. So be in that mindset and don't allow interviewer to confuse you. You if you strong at fundamentals, what I said, this is an arrow function, correct? Arrow functions are hoisted? No. So arrow functions are not hoisted but the variable created with var keyword is hoisted? Yes. So then what will happen? So this you

### 00:14:14 · Speaker 1

this block is not hoisted function expression but only the variable created where is hoisted. So function one will print this. Function two you are trying to call a function correct which is not at all hoisted so you don't have access to that so you should get an error correct. So now if I run but only where function two was there there is no function block then you have got undefined. But you have a function you are trying to invoke the function then definitely you will get error okay. So you are seeing the same thing. So where you are seeing function one

### 00:14:47 · Speaker 1

which I'm triggering first. Welcome to Gix for Gix and function two is giving you an error. Correct? So first question is solved. Now let's go to the second question, okay?

### 00:14:58 · Speaker 1

All these questions I've already put in my GitHub, you can go and practice them, okay? I'll link that in the description. Second question, very, very, very, very classic problem. So many scenarios this question is asked. In fact, I think I have also asked in my other series, but still a lot of get confused to answer this, okay?

### 00:15:14 · Speaker 1

So if you know the answer mention hosting question number two and put your answer in the comment section then continue watching. Okay? So if not, you are calling a function called get rate, okay? So then you are trying to see rate is undefined, then you have initial let rate is equals to let's make it var to introduce more confusion. Var rate is equal to six then you are returning the rate, correct? Then you are returning else and returning ten, okay? So what is the output? You are calling get rate, rate is undefined, so rate is ten here, so rate is

### 00:15:44 · Speaker 1

not undefined, then you're returning the value ten, correct? So the most of the time, whatever the answer that I get in the interview will be ten, okay? So

### 00:15:54 · Speaker 1

Many times interviewer will try to give you a hint by asking questions like are you sure? Most of the time when interviewer saying are you sure are there for two reasons. One, they are sure you are telling a wrong answer and they are giving a second option. So try to think. Or second reason whenever they ask are you sure you will be damn sure but still they want to create a confusion in you. So don't give chance to that. If they say are you sure if you are really sure then you tell damn sure this is the answer. If you are not really sure then try to analyze it once again and try to guess the output. Okay?

### 00:16:24 · Speaker 1

So you don't use this, uh, use both opportunities for betterment of yours. Okay? Now, uh, most will say answer is ten, but let us see what is the answer. Answer is six.

### 00:16:37 · Speaker 1

two types of interviewers again. One who will like totally give a negative credit for this question. Another who will try to give a option to you and they'll tell can you deduce why it is six. Okay. If you don't know what is deduce, please the meaning for the deduce and put that in the comment section. Okay. So some people will ask you to deduce why it is six. Now, uh why why that this happens is it is not like always people will look for a problem solver. People will also look for somebody who can analyze

### 00:17:07 · Speaker 1

and tell. They don't want to know everything and come, but at least whenever it is you are given an opportunity, are you able to check it and tell. So they will see where rate is equal to some starts thinking. Some, what some check the problem always with a prejudice. Prejudice as in they will not think something out of the box. They only try to align it to whatever they know. How they think I'll show you. So where rate equals to ten, rate equals to has to be ten, then it is coming to. No, I think the compiler has a problem. It should it cannot become ten, it should not it should not become six it should be ten because rate is already defined here.

### 00:17:42 · Speaker 1

This is a blunder that candidates do in the interview. See how come compiler be wrong? Okay, I do understand depending on compiler version some things here and go be there but you have to be damn sure to tell such statements in interview. Because interviewer gets pissed off if you say like this is happening compiler is showing wrong or in lab sometimes in engineering lab exam people will say this if you go to this computer output will not come. So these are very stupid reasons an engineer can give, correct? So first don't give such silly reasons. Second some people will try to analyze.

### 00:18:11 · Speaker 1

So you many will tell like variable created with var keyword is hosted. Correct? So you already said that, then what you are doing? So variable created with var keyword is hosted. Also people very explicitly they say variable created with var keyword has a global scope or a function scope, then what is that function or global scope? So it should be accessible everywhere, correct? So that means variable created with var is accessed here because of hosting and it is global or a block function scope property, correct? Now it has been hosted and defined undefined.

### 00:18:41 · Speaker 1

So now get rate has two uh variables with rate. One is a local rate, one is a global rate. Whenever there are two variables with same name, what is the priority? Local function gets a higher priority than the global function. That's all. So rate is equal to undefined. Correct? Where right this statement is being true, then you are returning rate, which is six. Correct? It is very very simple. Okay? But only thing uh is like you should show keen analysis. Most of the time interviewers will not ask you very easy question.

### 00:19:11 · Speaker 1

whenever this. This is not so difficult question also. If you are confident about topic, you will be definitely able to answer this. Okay? So this is all about the hosting. I cannot spend more time, but all of you can learn hosting very much in detail by watching these three videos. Totally, totally you will understand the entire hosting concept by watching these three videos. Okay?

### 00:19:28 · Speaker 1

Now, let's go to the next next topic, okay? If I go to the presentation, the next topic is set timeout. See, set timeout is again very very important topic because it is tricky.

### 00:19:38 · Speaker 1

It is not like set timeout itself is important because of the trickiness of the set timeout, this becomes very common interview question because they want to puzzle you in by asking set timeout, set interval, promise, etcetera. Okay? So, this is the definition again taken from Mozilla. Set timeout method calls a function after number of milliseconds. Very, very simple, correct? So if I go to the definition here in set timeout.

### 00:20:01 · Speaker 1

Same

### 00:20:03 · Speaker 1

specified piece of a time and the time code once expires. See very simple words you know JavaScript is a single threaded interpreted programming language. So as it is single threaded the execution happens sequentially. But there are certain activities that will take time. For example API call. Or for example you want to do a certain things in a periodic interval. For example refreshing the screen. Correct? So after every ten second refresh the screen and get some details. So these are things that should happen periodically. So main thread cannot wait for this periodicity. So it should go away and do the other things whenever this is required.

### 00:20:33 · Speaker 1

come back and process, correct? This is called event loop and lot of things you can search on the web regarding the event loop and understand that carefully, okay? But in very simple word, set timeout is one of the capability that will help code to run asynchronously. Synchronously means one after the other. Asynchronously means you encounter one, go to the next and this will be executed separately. That is asynchronity and executing one after the other is a synchronity, correct? So there are many ways in JavaScript you can achieve asynchronity. The one is set timeout, another is set interval.

### 00:21:03 · Speaker 1

another is promise, there is something called observables, many other ways also, but these are the four very very common ways of getting asynchronity in JavaScript. Okay. Now.

### 00:21:12 · Speaker 1

So this is basics of set timeout. Then let me ask you one simple question about set timeout. So this is the question. When discussing about closures I'll discuss more questions on set timeout. Okay? So let us see this question now. So where set timeout function so this entire block. The question what they ask is what is the output? Guess the output. So one very very mistake very common mistake that interview candidates have done that I've seen is suddenly guess the output.

### 00:21:39 · Speaker 1

don't delve into problem at all. Don't check line by line. Just you have understood one or two lines, dental. Don't do that. Some interviewers are good enough. They'll give you time to give a second answer. Some interviewers are not like that. You said the answer, no, gone. Especially tier one interviewers will always like that. They wouldn't give you second chance of correcting your answer. They will if first chance you are not able to, they think you are lacking patience. You are not able to interpret the program properly. Especially if you are a senior role, mostly that question is done for you. So take your moment, analyze the things

### 00:22:09 · Speaker 1

properly before giving the answer. So if I am given this question what I will do I will tell. So I have a function.

### 00:22:15 · Speaker 1

So this function is a self invoking function that means it doesn't need anyone to trigger it it will be triggered automatically and as soon as this function is triggered the entire block is gone okay I mean this is done executing then I have a console.lock where I'm printing one definitely this is something that should execute first then I have a set timeout with one thousand millisecond or one second then I have another set timeout with zero second then I have a console.lock four so here the what is the tricky part I would identify the tricky part this is the tricky part

### 00:22:45 · Speaker 1

Okay, why this is a tricky part? It's a set timeout with zero second. Correct? So and you have a console.log one and four, definitely one will be printed first. There is no doubt about it. This will most will be able to guess this. Then people will be sure this will execute at the last because it has a one second delay. People get confused between these two.

### 00:23:06 · Speaker 1

whether it is zero or four. Correct? I am aware of the concept that whenever JavaScript main thread encounters a timeout, it doesn't bother how much delay you have given. It will straight away move that block into a another memory location where it has to finish, it should finish its execution, wait for the main thread to get free. So whether it is zero or one, it doesn't bother. Okay? So both the set timeouts are gone into a separate memory location. So if you read the event loop concept detail, you will be able to get to know. I'll link that in the description.

### 00:23:36 · Speaker 1

Okay. So now console.log we are printing one, then I'll be printing four. Then I'll be printing three, then I'll be printing two. See if you look at the numbers here, it is one, four, two, three. It is also created added in a way to create a confusion in you where one, two, three, four seems to be the way it should execute, correct? So many will tell one, two, three, four just by looking at the numbers. So don't do that. So output is one, four, two, three. Let me execute. one four three two, okay? Node, SetTimeout

### 00:24:11 · Speaker 1

one, four, three and wait for a second and it will print two. So this is another important question. So they will ask you let's say you say this. one, four, three, two. Then they will tell is there any delay between each printing? Yes, there is a delay that also you need to specify. If you don't specify the delay some companies especially the tier one companies, they will cut the marks for that also, correct? So it is one, four, three, one second delay and two. That is the right answer. So be this much specific. Let's say this is the first question asked.

### 00:24:41 · Speaker 1

to you and you said like this one four three wait for a second and then two is printed they'll be like yeah this guy knows the each and every aspect of this question then they will also be in that mindset of ask like in the mindset you know something whenever they asking the next question if you if you are not giving that viable like you know something then they always try to trick you so that you will not be able to answer the next question okay

### 00:25:06 · Speaker 1

So this is about the set timeout. Very basics I've discussed, more I'll discuss in the closures. Okay? Next, next concept is closure. Closure is a function having access to parent scope, even after a parent function has closed. Very, very simple. I I know most of you are aware of closures and it's very, very, very, very important interview concept. Okay? So if I go back and to the official documentation again, okay? So if you see here, uh closures. Okay? Very, very important topic for the interview. Okay? And before I explain closure, I'm just calling out

### 00:25:36 · Speaker 1

once again. Please like the video. It's been already close to twenty five minutes. I think I'm trying to give a good content. If you like the video, please like it on YouTube channel and do not forget to comment something. You liking the comment, you want me to make some changes, please comment that so that I get more impression and lot of people will watch my video. Please do that before continue watching. Okay? Now, closure. Closure is a combination of function bundle together with the difference to its surrounding state. Okay? Lexical environment what we call. Closure gives you access to outer function. See in this this is the this is a typical example. where you're trying to call the function, let me copy this, okay? and try to execute in JSFiddle, okay?

### 00:26:15 · Speaker 1

and

### 00:26:17 · Speaker 1

It's right. I think the video would last for at least ten at least ten fifteen more minutes so stay tuned with me. You will not disappoint. Lot of important question I'll I'll answer going forward. Okay? I'm running the code.

### 00:26:31 · Speaker 1

So I'm getting the Mozilla. So what happened is I triggered a function called init, correct? In this function, this variable called Mozilla declared, variable in name whose value is actually Mozilla. What it is doing is it is calling the display name function inside this function. So console.log name. So this display name which is inner function to init has access to the variables of the outer function. That in very simple words is called closures. Okay? There are a lot of variations of this but in very simple words function with its lexical environment, which is parent's lexical

### 00:27:01 · Speaker 1

environment is called closure. Correct? If you see the definition again, a closure is a function having access to parent scope even after parent function has closed. This you have to specify even after parent function has closed. Okay? Because to be very precise about your answer. Now.

### 00:27:16 · Speaker 1

Let's see few of the very important interview questions. Generally closures and the timeouts are tied together, okay? Lot of fancy questions are created with this, okay? So I'm going to discuss most of the questions. Definitely I'll try to trick you, okay? Don't get trucked and try to answer the questions with very carefully, okay? Very first question, most common, uh, everywhere you might have seen this, correct? I'll tell even in this question how many mistakes you will do in the interview, okay? Let's say you're calling example one, okay?

### 00:27:46 · Speaker 1

If you know the answer mention closure question number one and your answer, what will most of them what will the answer will tell? So

### 00:27:54 · Speaker 1

I think maybe let us make it star only to avoid confusion. Okay? So where we have something called example one and this question is also in GitHub you can copy for practice purpose. Okay? So where how I'll be analyzing the question I'll show you. So we have a for loop. I I less than three and I plus plus. We have a set timeout which is running in a loop which is running for thousand into I. So that means a second. So first time it is a zero second, second time it is one second, next time it is two second. Correct? When I becomes three, this for loop will fail and

### 00:28:24 · Speaker 1

And as you know the follow up runs much quicker after follow up is finished execution the set time mode starts execution. Because of property of closure this I and the variable created with var keyword has a block scope. All the timeouts that have been created and all the logs console.log which is present inside will have a same reference of I. Okay? So due to which I value by the time when they finish let's say like one timeout second timeout and third timeout that three blocks all pointing to same

### 00:28:54 · Speaker 1

I. Okay? So, when the time the timeout is finished, the value that I is will be presenting is the last value of I which is three. Correct? So what we'll be doing is three times three is printed.

### 00:29:06 · Speaker 1

I think most will be able to deduce this. Very first tell what mistake people will do. This question is very commonly asked with I less than five. Some people will tell five will be printed five times. Are yaar question toh dekh lo, correct? It is not even five, it is just three, correct? So don't look at any problem with a prejudice. Interview will do a small variation and you will do a mistake, okay? Fine.

### 00:29:28 · Speaker 1

Now you said this like what is the thing you said is three is printed three times correct? Many will tell this answer rightly in the interview because of this becomes so common. Next question that I ask is with what interval?

### 00:29:42 · Speaker 1

with what interval it is printing three? for example, three one second, three one second, three or one second delay three three three. no delay all three at once three three three suddenly.

### 00:29:57 · Speaker 1

Now again candidates get confused because nowhere this is explained. Correct? All the videos that you watch on the YouTube, they will only say what is the output, but they are not focusing on the interval. So then you will get tricked. So now you should be able to analyze from the delay perspective also. So the first timer is having a delay of zero second because I is zero. So second timer is having a delay of one second. Third timer is having a delay of two second. Correct? So by the time the first timer is running, there is the second timer is also finished one second.

### 00:30:27 · Speaker 1

time that is finished the third timer also has finished the second. Okay? So you should think in that direction and try to give the exact answer. Let me run and show what is happening.

### 00:30:37 · Speaker 0

close

### 00:30:38 · Speaker 1

January

### 00:30:41 · Speaker 1

See, there is a one second delay each. Why? So timer one, timer one is having a zero second. Okay? Timer, okay, let me make it timer zero only, the first timer. Timer one is having one second. So timer two is having two second.

### 00:31:01 · Speaker 1

timer two is having two second delay. Correct? So first this is printed.

### 00:31:06 · Speaker 1

By the time this is printed that one second is already and this should execute after one second, correct? After this this will execute one second delay. So when this one second delay happened, here also one second got minused, correct? So now only one more second it has to wait. So it will wait one more second and again after one second delay the three is printed, correct? So be very very mindful of this. Don't think like after one second is done, then two seconds. No. After one second when this one second is elapsed, here also one second is

### 00:31:36 · Speaker 1

because all the timers are created in a parallelly, correct? So it will also print after one second. Be very very mindful about this. Then there was a question like what if I make it plus?

### 00:31:47 · Speaker 1

Correct, what if you make it it will plus. So in that case, I'll I'll just to avoid. Sorry, okay, let's make it plus. So thousand plus zero is thousand. So first timer will run at one second. Thousand plus one is thousand and one again one second. Thousand plus two again one second with some milliseconds, correct? Now what will be the output? Do you still expect a delay in each display? What will be the thought process? If you know the answer, please mention that in the comments. section, okay? If not, let me execute it.

### 00:32:20 · Speaker 1

all the three printed almost instantly because the first timer took a zero second, second timer took one second and third timer also took the same. Correct? So it they all printed almost at the equal interval. So if you are mindful you will be able to answer this. Okay? Now, let's go to example number two. Let's cut this.

### 00:32:38 · Speaker 1

And like I mentioned this question is already in my GitHub you can take it from my GitHub okay and practice it. Do not forget to like my GitHub project what we call starring my GitHub project okay. So this small variation of the question okay. If there is some problem in running here so I'll put it in JS Fiddle.

### 00:32:56 · Speaker 1

small variation, okay? What I have done here is

### 00:32:59 · Speaker 1

The function whatever was here, correct? Maybe let me zoom in a bit so that it is much easy for you to see. What I have done is this inner function whatever was there, that I have made a self-invoking function. Okay, self-invoking function what they call ify, need will execute automatically. It will not wait for any external trigger, correct? So in this case what is the output?

### 00:33:21 · Speaker 1

You know already the concept, you already guessed the output in the previous, again you get confused here. Why you are getting confused is because you really don't know the concept, you only know the question. You expecting the same question to be asked in the interview and you want to clear. That will happen only, only if both of you watch the same video. If you get an interviewer like me, I'm not boosting, but I know the concepts in depth. So if you tweak a problem, right, I like to tweak the problem and see your approach. So then it will be very difficult for you to clear the interview. So don't learn the question, learn the concept. Okay? So if you see here,

### 00:33:51 · Speaker 1

self inoking function what is the what is the duty of self inoking function trigger immediately correct inside set inside set amount you have it but what is it is responsibility trigger immediately it will don't wait correct so in that case what will happen it is at the I reference so here still I am having var only but what will happen so it will print zero one two three with we cannot print because for loop will be exited before it comes equals to three correct let me run the code for you

### 00:34:18 · Speaker 1

So zero one two. So let me try expanding it. What is the delay? Can you see is there any delay? There is no delay because set timeout self invoking function the job is only that it will trigger immediately. But how even though it is inside I'm sorry self invoking function inside set timeout also triggering immediately. But how set timeout is able to not able to prevent it because set timeout is set to execute after a period but still set timeout is not able to prevent it. Why? At least read this on the internet. I mean this is something homework for you. Why a

### 00:34:48 · Speaker 1

self-invoking function present inside a set timeout is triggering immediately, not waiting for that period to get over, okay? That you can please read on the internet and comment if you get the solution. If you don't get the solution, also comment. I'll try to explain that, okay? Now, this is the example two. Let's check the example three, okay? Simple one, example three, okay?

### 00:35:10 · Speaker 1

I think you're enjoying. We are already cover almost thirty thirty five minutes. I think you're enjoying the content that I'm making. Okay. Please like and comment if you are enjoying. If you are not also add the comment what is making you boring. Now example three. This is again quite small variation of the above question. This is also discussed in many other YouTube videos and the blogs. Okay. So what the variation is here?

### 00:35:31 · Speaker 1

you have a set timeout, you have a normal function, okay, not self invoking or anything, but that function has been triggered and the value of I is passed to this, okay? value of I you are passing and that is I mean K and the I are basically the same, just to avoid confusion I'm referring here as a K, okay? the argument that you're passing is first you'll pass zero, second you'll pass one, third you'll pass two, correct? whenever it is the third, the loop will be exited. Now what will be the output? console.log of K, what will be the output? Then put star only, which is most commonly asked.

### 00:36:01 · Speaker 1

Don't say again something related to five, we are running the loop only till three, okay? What will be the output?

### 00:36:09 · Speaker 1

You know, whenever you are invoking a function and passing an argument to it, correct? So that whatever the argument that you are passing, function forms a closure. So the each argument that you are passing is independent. So it is not relying on any other external clope, okay? When there is no nothing internally, it will look for the external. But whenever there is something internally, then that is the gives a higher priority. So you you have formed the three functions now, okay? Where the value of I was different. It is not the same as the above example where variable I was referenced by all the timeouts, no. In this case, it is all different. So now if I run this

### 00:36:44 · Speaker 1

zero, one and two. The reason being, so zero, one and two because every time it is forming a different block. Okay? With a different eyes that you are passing. So there is no trace of variable I and it is global or a functional scope. Okay? Now the delay also is easily predictable because of this I, zero, one and two. I already explained the similar delays formed here as well. Okay? So that's about closures. Closure and set timeout has become a deadly combination for interview. Okay? So I've covered most common question here and in case you go here also

### 00:37:16 · Speaker 1

I've I've I've discussed lot of important concepts, okay? So where, you know, these are all about functions, you can watch that also, very very important. So this is another important question called counter dilemma, okay? I muted myself and the video to avoid confusion. So counter dilemma in JavaScript again a concept related to the closure, very very important, okay? Whenever the interviewer ask if you know counter dilemma without by yourself, interviewer will be very happy because it's a very common dilemma, okay? JavaScript developers have tried to watch this video, then also have uh five questions that make you master your functions

### 00:37:52 · Speaker 1

Okay, somewhere I've also explained the closures in very much detail. See? Six questions that you cannot skip with respect to closures. Very, very in detail I've explained, picked the questions and explained about the closure. So that is part two of this are almost another six questions are discussed here. So many beautiful questions about the closure are discussed here. If you've seen my this video and that video too, definitely you'll be able to solve most and most of the closed related interview questions. Because I don't teach you the questions, I teach you concepts. If you conceptually it's wrong, definitely you'll be able to crack them. interview. Okay? Now, so next question, next topic is and the last topic is promise and the caring. Okay?

### 00:38:29 · Speaker 1

both the topics let me explain it together. See promise I made four beautiful videos here explaining every aspect of promise one by one. So how to create a promise, how to resolve a promise, reject a promise, promise.all, promise.all settled, all the things I've tried explaining very much in detail here. It is just around again thirty thirty five minutes. Watch the four videos I'll guarantee all the question that could be possibly asked in promise are covered in this. So watch that and you won't regret. Okay? I'm not going to explain that again in this video because it is most of a theory because promise is

### 00:38:59 · Speaker 1

not having any tricky questions like I explained about closure. It is having lot of theoretical questions which you can definitely learn by watching this. Then the next thing is currying. Okay?

### 00:39:11 · Speaker 1

currying is also a very very important concept but it is not like so frequently asked in the interview some interviewers ask some some interviewers doesn't do not ask people for those who don't know what is carrying it is like this you have a function called sum okay you have a function called sum where you will try to call it this way okay where ten comma twenty okay interviewer just curious to know can you deduce this what is ten comma twenty and try to write a function for this okay so that I very much in detail I have explained here

### 00:39:41 · Speaker 1

in the this this closure function currying. In fact, I've explained a very very important concept here, like how do you make a function closure and a normal function also. Like the same function behaving in a currying way and non currying way. It's not that easy, okay? So I've explained this very much in detail in this video. So please watch this video. I'll try to link this entire series and specific videos that I talk also in the description. Please watch this video. Currying can be this just ten minutes video. If I try explaining here also it'll become ten minutes. So I'm just linking you there, okay?

### 00:40:11 · Speaker 1

Please watch that currying video, definitely you won't regret. You will learn a very, very, very important interview question, okay? So, this is all about this entire thing, but there is another very important point that I want to mention. As you know, this is not it.

### 00:40:26 · Speaker 1

There are many other wonderful JavaScript concepts which are generally asked in the interview. These category whatever I made are most common. There is something called a little bit of a second priority. Okay, let's say top six, they are then the next six. So but even they are very very important considering lot of other interviews like tier one, right? They can ask you any question. Like what is history API in JavaScript? Or they will ask you tell me more about deep copy and shallow copy. There are many other interesting topics which are asked in the interview. I am planning to make a part two of this series, but that I'll be able to make only

### 00:40:56 · Speaker 1

if I get a lot of love from you. If you like, share, and comment about this video and subscribe to my channel if you're not subscribed, definitely I'll try to make a second part of this where I'll cover more topics in a similar way with a lot of questions. Okay? If you liked whatever I've made so far in the video, please like this video on my YouTube channel. Do not forget to subscribe to my channel Uncommon Geeks and all these questions are put in my GitHub repository. Star my project in GitHub repository, clone the project, practice all the question, watch my other series that I was referring in detail. I'll link that on the screen also in the description.

### 00:41:26 · Speaker 1

watch that entire series. Definitely you won't be regretted. Okay, you will enjoy the series and you will learn lot of things about the interview preparation. Okay? And lot of medium articles I have written, go to my medium blogs to get a code snippets in a very short duration and practice them also. Thank you so much for watching the series. Catch you in the next video.
