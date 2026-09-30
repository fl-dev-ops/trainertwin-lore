---
id: PeSM8zPypL0
title: Top 10 JavaScript Coding Interview Question and Answers 🔥 MUST WATCH BEFORE
  ATTENDING NEXT INTERVIEW
date: '2024-06-08'
url: https://www.youtube.com/watch?v=PeSM8zPypL0
description: "#interview   #react #reactjs  #frontend  #javascript \n@careerwithvasanth\
  \     is a Youtube channel dedicated to helping candidates clear their interview.\
  \ There are more than 150 videos and new videos will be uploaded every week. If\
  \ you're seriously preparing for interviews and looking for tips and tricks, please\
  \ subscribe to my channel and press the bell icon.\n\nTo get a dedicated one on\
  \ one,  you can reach out to me here: https://topmate.io/vasanth_bhat\n\nLink to\
  \ questions: https://github.com/coolvasanth/JavaScriptInterviewQ_A/tree/main/Personal/Youtube/JavaScript%20interviewVideos/JavaScriptInterviewQ_A/Top10_Questions_Answers\
  \ (Don't forget to star the project)\n\nJoin CareerwithVasanth community to discuss\
  \ with other developers: t.me/uncommongeek. \n\nFollow me on LinkedIn - https://www.linkedin.com/in/careerwithvasanth/\n\
  \nMedium Blog https://careerwithvasanth.medium.com/\n\n\U0001F449 “Contact on WhatsApp:\
  \ 9731039408”\n\nJoin my 3100+ members frontend developer telegram group here: http://t.me/uncommongeek\
  \ \n\nJavaScript Interview preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nJavaScript Custom implementation/polyfills Series: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\n\
  \nFrontend system design series: https://www.youtube.com/watch?v=gN8LQTff21g&list=PLmcRO0ZwQv4RYUD10hUnWjWb-RRSpm3KM&ab_channel=UncommonGeeks\n\
  \nMAANG series for frontend developer: https://www.youtube.com/watch?v=s-b-txm_Gvk&list=PLmcRO0ZwQv4SNhbW4CI4vc-6IHBHCKzZN&ab_channel=UncommonGeeks\n\
  \nFrontend mock interview series: https://www.youtube.com/watch?v=uW7MfzoD1po&list=PLmcRO0ZwQv4SwXLVpnKb_nFQx1Wd2XEjD&ab_channel=UncommonGeeks\n\
  \nShorts for quick access to all frontend resources: https://www.youtube.com/watch?v=8ByBOT7Aehs&list=PLmcRO0ZwQv4SXtrTYIU_dPygZgOgYV81S&ab_channel=UncommonGeeks\n\
  \nTips for freshers: https://www.youtube.com/watch?v=hGIOIdPNNqE&list=PLmcRO0ZwQv4QBiZns-nYX5qnHKAepVeqH&ab_channel=UncommonGeeks"
author: careerwithvasanth
duration: 00:23:32
model: saaras:v3
transcript: true
---

# Top 10 JavaScript Coding Interview Question and Answers 🔥 MUST WATCH BEFORE ATTENDING NEXT INTERVIEW

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Career with Vasanth YouTube channel. My name is Vasanth. I hope you all doing well. So this is a very important video where I'm going to discuss top ten snippet driven JavaScript interview questions. These questions are of medium to hard difficulty. For freshers it's again close to hard difficulty. For experienced person it could be of medium to hard difficulty. So the whole point of making this video is not that you guess an output which is right or wrong. It's probably help you to understand the concept in in depth. So most of the time whenever snippet driven questions are asked in the interview, let's say the output could be a function that returns three and four.

### 00:00:30 · Speaker 1

and you'd say the output as four, which is the right answer, no interviewer will shortlist you. You need to be able to justify why it is four and not three. That's the whole purpose of this interview, this particular session, where I'm going to basically explain the snippets and in depth, like why that particular output is coming, okay? Without wasting further time, let's get started. If you see me first time on the internet, I'm Vasanth, I create content in front and in interview preparation. Please subscribe to my channel Career with Vasanth. Let's get started. So I have exercise number one here.

### 00:00:57 · Speaker 1

So where which is very simple, looks very simple. So where we have a create counter and we have like two variable counter one and counter two. I could zoom in little bit for

### 00:01:06 · Speaker 1

make you a little easy. So we have a counter one, count like variable called counter one, variable called counter two and we have function create counter. And we are calling it in line number twelve, thirteen and fourteen, okay? So where we are calling counter one, counter one and counter two, okay? If you know the answer, okay? Please mention like question number one and your answer in the comment section. I'll be more than happy to review and uh tell whether that was the right answer or not. If not, definitely you can wait for my answer, okay? So I'm running

### 00:01:34 · Speaker 1

So the output is one, two and one, okay? Like I told it's not about output, let's dig deeper like why it is one, two and one.

### 00:01:42 · Speaker 1

So, whenever you create a counter one, we are calling this function called create counter, which is returning this function, correct? So if you know by the property of closure, this return function will have access to the count value. In very simple words, closure means inner function having access to the value of inner function having access to the outer scope variable, correct? I'm not using very fancy terms lexical scope and all. If inner function can access outer scope variable, that is called closure in very simple words. So we are returning

### 00:02:12 · Speaker 1

returning a function and that function is basically is present on the counter. Correct? So here if you see, whenever you're calling the counter first time, you're nothing but you're invoking this function. Correct? Which is actually returning the value of count after incrementing it. So value of count was zero before and after incrementing, it's a post increment. Even if it would have been a pre increment, same value I think we would have got. So we are so the value of count became one here. We are calling the same function again because of the property of closure. Closure you know right? Consider closure like a box. Okay? So that

### 00:02:42 · Speaker 1

box knew the value of count one when that box was locked. And whenever you call the box only then the value of box would change. And let's say the whatever was outside let's change to anything this box is unaffected, okay? Consider it like a pilot that whatever that one black box will be there right whenever the airport flight crashes. That black box basically captures all the information and it doesn't know what happened to flight whether it is flight landed properly or it crashed it only knows like capturing that way the closure is, correct? So now counter one basically giving the value of one and two

### 00:03:12 · Speaker 1

the second time whenever you're invoking it knew the value counter incremented by one now it's incrementing by one more which is making it to two. And the thing is like counter two right counter two also you're returning the function. The difference that you need to note here is whatever the counter one the closure form right that is different than whatever the counter two form. The value of counter two whenever it is formed the count value was zero only so every time it is creating a new instance basically okay. So counter two the default value of count was zero so it returned a value of one whenever you

### 00:03:42 · Speaker 1

call it. So let's say I call the counter to once again, I would be getting the values same one and two, okay? I hope most of you are able to answer this correctly. Let's go to exercise number two, okay? Which is slightly little more complicated but not like very complicated, okay?

### 00:03:58 · Speaker 1

So we have a function called fetch data and we have something called a process data. Okay? So fetch data as you can see I've mocked an API called implementation where I'm returning a promise which basically sends a I have a set timeout inside that particular promise which wait for like one second and then I have like constant data so where I'm resolving the data. Okay? And I have a process data which is again returning another promise. Okay? And inside this what I'm actually doing is whatever the data that I have resolved I'm making an upper case of it. Okay? me zoom out so that you can see the complete snippet once. And from

### 00:04:33 · Speaker 1

from this here line number nineteen which is basically a trigger point. I'm calling a function called fetch data, passing this URL, then to then I have and then I have a catch, okay? Again if you know the answer, please mention question number two and your answer in the comment section. Let me answer if you don't know. If you are not able to answer like question by question, at least by end of the video answer like how many questions you are able to answer correctly without watching my answer, okay? Now, if I have to give a right answer to this, let first let me run.

### 00:05:01 · Speaker 1

So we waited for one second and then we got like data retrieved. Correct? Let's see again.

### 00:05:06 · Speaker 1

one, maybe then after that a point five second, which is a five hundred millisecond here. So then we got like data retrieved. So what happened? So first is like this then executed after fetch data. So fetch data basically took one second and it resolved the data which is like data retrieved, a string. And then we came to the another then where we actually pass

### 00:05:27 · Speaker 1

No, I'm sorry. Then we came to the first then, where we passed this process data, that is data retarded here, which took another five hundred millisecond, which is half a second, and then actually all it did was it it converted the value whatever you pass into upper case and returned it, okay? And then we'll basically logged it in another the then here, okay? Putting other way, you could see like

### 00:05:49 · Speaker 1

the return value of a promise is passed to another promise, okay? See, line number fetch data is a promise and we returned a value that was passed to this line number twenty-eight done and process data is another promise, okay? So two promise we could call in this particular operation where we got the value of the data retrieved. So what is the takeaway from this? Let's say you would have used async and await, right? How you would have solved it? You have to call await fetch data, again you have to call await process data, correct? Instead of that, we could use

### 00:06:19 · Speaker 1

one promise dot then to like you can use only one promise and then two times to achieve whatever is required. Correct? So this is the advantage of using the promises in some cases whenever you have to do the multiple operation depending on the promise response. Okay? We'll quickly go to exercise number three.

### 00:06:35 · Speaker 1

looks very very simple. If you know the answer again, mention that in the comment section. So we have like function greet and function say hi, correct? So you are calling the greet from the line number one and from line number twelve you are calling say hi, okay? What is the expected output for this?

### 00:06:50 · Speaker 1

you could even interpret without running as well. So greet is a function, normal function, so which is hoisted. So you can call it from anywhere basically. So you're calling passing it as John. So hello John will be printed. Say hi is a function which is a arrow function, definitely it is not hoisted. So whenever you, you can call it only after it's getting declared. So whenever you call from here, you get hi there. So hello John and hi there will be the output. Okay?

### 00:07:16 · Speaker 1

hello John and hi there is output which is exactly as expected okay now let's say you you want to make like understand the property of closure properly you can mention the say hi here okay which if you run

### 00:07:31 · Speaker 1

one second I did not save maybe. carefully here you are seeing like say hi before the initialization because say hi cannot be accessed before it's declared because the arrow functions or the function declaration this

### 00:07:44 · Speaker 1

this block is basically is not hosted so you are able to you will not be able to call it even before it is declared. If you don't know hosting I have a very dedicated series on basics of JavaScript that link will be there in the description. Please go ahead and read please go ahead and watch that particular video where I explain the hosting in detail. Okay? That link I'll put in the description if possible also on the screen so please go ahead and watch. Now I'm going to exercise number four. Okay?

### 00:08:05 · Speaker 1

very simple snippet, but you have to think very carefully before answering, okay? So let me zoom in a bit.

### 00:08:12 · Speaker 1

So I have a mystery function called mystery which takes a value x could be of any type. So where I'm checking like type of x is number if number then I'm converting it to a string. Okay? See if you see here type of x is equal to number.

### 00:08:27 · Speaker 1

okay? And then I have type of x equal to string. Then I return the parse int of x, okay? And then finally I'm returning unknown, okay? If you're someone who never know what is the difference between parse int and number, but at least after this video go and check. The difference between parse int and number, both are used for actually type conversion, but there is a difference. That is also another important interview question, okay? Now. So, now whenever I call a mixed tree, first I'm passing the true, second I'm passing an array, third I'm passing a null. Again, by now at least you some light

### 00:08:57 · Speaker 1

has been lumped on your brain and you are able to answer, please mention the question number four and your answer, if not let me run the code. Okay?

### 00:09:06 · Speaker 1

So the answer for all is unknown. Definitely it is very straightforward. Lot of some of the times the snippets are unnecessarily complicated just to make you think like how calm your mind whenever you're interpreting the code. Mystery of passing the true. If x is equal to uh x the type of x which is boolean is not equal to number, it's not equal to string. So we return this. So type here is an array. Again do not match both, we're returning here. Type null. Null is also not a number, not a string, type of null. So basically because of which we are returning as unknown all the cases. Only one

### 00:09:36 · Speaker 1

question I have for you if you know the that mention question number four and tell what is the type of null in the comment section okay I'm not answering I want you to answer what is the type of null in the comment section okay so exercise number five is where we have something called a create increment so create increment returns two functions one is increment another one is log if you see here we have two functions one is increment another one is log okay we are calling the increment three times followed by we are calling the log okay so increment what we are doing we are incrementing the count every time and every

### 00:10:06 · Speaker 1

you're calling. Log you're printing this message. Okay? So if you know the answer, mention question number five and put your output. Whatever the answer that you were able to interpret. Okay? Now let's look at the snippet carefully for those who have unable to answer it properly.

### 00:10:20 · Speaker 1

So the count which is differed outside can be accessed inside because of the simple property of closure. So whenever you call the create element, the increment method whatever was written, definitely it is having access to this outer variable count. So every time whenever you incrementing, the value of count is always incrementing, correct? So which is like it was zero first, like remember the box example I told, it was zero first, you called it again, it became one, you called it again, it became two, okay? Now.

### 00:10:46 · Speaker 1

Now we'll go to let's relief run the code.

### 00:10:51 · Speaker 1

એક્સસાયઝ નંબર ફાઈવ. ઓકે?

### 00:10:54 · Speaker 1

So the count is zero is coming. Which is little different than probably what you thought. Correct? Because the count was supposed to be we called it once which was became one. Second time we called it became two. Third time we called it became three. So the log whenever you are printing it was supposed to be three. Correct? Why it's not three?

### 00:11:13 · Speaker 1

So that is, see, these snippets, a lot of people ask me, Vasanth, why you ask such snippets in the videos when we are not going to use it in the day-to-day activity. Listen to this answer very carefully. It is not like the same snippet you are going to use in your day-to-day work.

### 00:11:26 · Speaker 1

The snippets are created to understand how depth actually you are thinking, correct or how keenly you are observing at something because let's say tomorrow you start, you join the company and then you start working. The most important point for you to like debug quickly and fix a bug. If you cannot observe the snippets carefully, you cannot debug carefully or you cannot debug quickly. That is the whole point of asking such snippets in the interview, okay? Now, let us say what was happened whenever you call create increment, it returned two things, this and this. Meanwhile, even this line got executed, correct?

### 00:11:56 · Speaker 1

where the message was initialized with a value of count which is the value zero. During the log you are not printing the count you are printing the message so this is the observation that you need to have. So message was never updated only here it got called and message value remained as it is. So we are getting the value is zero. If we replace message by count then probably the value

### 00:12:21 · Speaker 1

So the value was three. You got the point? Why it was zero and why it is three. Okay? Now let's go to another important exercise, exercise number six. Okay?

### 00:12:34 · Speaker 1

Okay. So now exercise number six we are. So where we are calling a function called test, we are trying to log a variable A which is dependent line number five whose value is one. Okay. And then we have a function foo which is returning a value two. Okay. And we are calling that function as well from line number three. Okay. So you're calling the test, as soon as you call the test, the first thing that happens is console log of A whose value is actually

### 00:13:01 · Speaker 1

you have to tell. If you know the answer, mention question number six and put that in the comment section. I'm going to explain in a while. And then you're calling the function for which is actually returning two. So there's no doubt line number three would print two only because you're returning a numerical value. So there's no brainer. Line number six will be printing two only. Line number two, what it will be returning is the question. As you know, the variable created is var keyword is hoisted, obviously. Hoisted and initialize the value of undefined. So whenever this block is coming, A actually went to the top.

### 00:13:30 · Speaker 1

and value of A is undefined. Correct? I think most of you are aware of this hosting concept. If you don't know again, I'll link my video in the description section. Please go ahead and watch it. So, undefined and two will be the output. Let's see whether I am right or not. Okay?

### 00:13:44 · Speaker 1

as as I told it is undefined and two okay. Now let's go to the next snippet exercise number seven.

### 00:13:51 · Speaker 1

This is very tricky, huh? I'm sure at least some of you will not be able to answer it properly. If you are able to answer answer number seven correctly, please mention that in the comment section without taking much, in a minute you are able to guess this answer absolutely right with proper reasoning. Consider you are like almost fit for most of the JavaScript related interviews, okay? So where we have a simple object called person.

### 00:14:12 · Speaker 1

and person has a name which is Alice and we have a function called greet which is actually a function okay. What we are doing in line number seven line number eight we are calling we are assigning person number greet to greet and then we are calling the greet okay.

### 00:14:25 · Speaker 1

function greet is basically printing hello my name is this dot name which is actually Alice. my name is Alice. okay? so now where basically this always refers to a caller as you very well know. there is a priority of this I'm not going to dig very much. most of you might have answered hello my name is Alice as the answer. let us see what is actually the output. okay?

### 00:14:39 · Speaker 0

not going to

### 00:14:49 · Speaker 1

See, output if you see here, hello my name is undefined.

### 00:14:52 · Speaker 1

Okay, which is very important and very tricky. I want you to like look at it carefully why like my name is undefined, correct? My name is undefined because whenever you in in like initialize person.greet into this greet a separate variable, right? You understand things carefully. Like how this object is actually defined. You see a name, right? This name is is basically person is an object where you are having a name and whose value is Alice. Then you have a greet which is actually referencing a function. So this function is actually referencing to a particular memory location. I hope you agree.

### 00:15:28 · Speaker 1

and that memory location is basically assigned to a variable called greet. Correct? So this memory location of this greet and name, they are all inside the person. Correct? So let's say whenever you call person dot greet, not this way, I'm going to tell in a different way, that time it would reference the name which is a part of that object. This would reference. In this case, what will happen is

### 00:15:51 · Speaker 1

person.greet whenever you're extracting it is just like any other normal function function reference. So variable greet will hold person.greet which is pointing to a memory location. In that case there is no this.

### 00:16:04 · Speaker 1

okay? So we are getting the value of this dot name is undefined. So we are getting hello my name is undefined. If you want the greet actually to know that you are a part of person, then what you could do is we could bind it, okay? We could bind this to a person.

### 00:16:22 · Speaker 1

Let's say whenever we do this, then it knows that that greet function belongs to the person object. In that case, it would know name is actually Alice. Let me run the code. Okay, so you see like hello my name is Alice in this case. I hope you got the the difference. Whenever you just assign person.greet, you are referencing actually a global function.

### 00:16:43 · Speaker 1

But whenever you bind it to that person, then you're referencing to this particular object where the this.name is defined, okay? So if you if you really answer this question properly with right explanation, please mention that in the comment section like I told. Let's go to exercise number eight.

### 00:16:58 · Speaker 1

Very simple snippet, looks very simple, okay? So where we are calling x equal to one and we have a function console.log of two, let x equal to two, okay? We have two x here. One is a global x, one is a local x, okay? So whenever we have two x's or whenever we have two variable with same name which is also present on the global scope and which also present on the local scope, you very well know the priority is given to the local scope. So line number five, whatever you define x equal to two, that has highest priority than this. So now in line number four, whatever console.log of x we have,

### 00:17:28 · Speaker 1

it is definitely running with respect to the inside x. So outer x you totally ignore. So inner x is producing the value. What value it is producing is something you need to tell. If you know the answer please mention that in the comment section. If not let me execute the code. Okay?

### 00:17:45 · Speaker 1

we are getting a reference error cannot access X before initialization you all know this. Okay. Property of hoisting again if you don't know watch my video. So where where it's clearly told like X is defined in line number five if you try to access it in line number four we get a reference error. Correct? Let's let's make a small tweak here which is like just for to

### 00:18:05 · Speaker 1

check like how much you know I am doing this. In this case what will be the output? Can you try guessing?

### 00:18:12 · Speaker 1

I'm not changed anything. I have not initialized x with anything. I've just written x in line number four. I'm trying to log it in line number five. Okay? What will be the output? In that case, it is undefined, correct? So all variables that are declared and not initialized will give a value of undefined. Okay? Now we'll go to exercise number nine. I have two variations of it just to like little bit tickle your mind. So now I am actually doing a simple object destructuring here. A colon x, B colon y, and here I have a is equal to one, b is equal to two, and c is equal to three. If you know the answer,

### 00:18:42 · Speaker 1

So most of you will be able to answer this correctly. Please mention that in the comment section. So the answer would be very straightforward. One and two because A we are assigning the value of A to a new variable called X.

### 00:18:54 · Speaker 1

we are assigning the value of B to a new variable called Y. So here in the right hand side A is one, B is two. So console dot log X comma Y which is like one comma two. Which is no brainer, correct? Let's do one very interesting thing here, okay? The second snippet.

### 00:19:11 · Speaker 1

Let me zoom in a bit so that you could see it properly. So now you have a

### 00:19:16 · Speaker 1

is equals to like again A X here you see ten most of you know it is a default value whenever a particular object you are not getting the actual value you are assigning to default value lot of cases you will be doing that in type script whenever you have a variable function taking a variable you will define a default value let's say it's a string you define like empty string it's a boolean you define like true or false as a default value okay so those arguments are actually not mandatory if you have a default value you could skip them okay now A is equal to X you are assigning the

### 00:19:46 · Speaker 1

value of a into x if there is no a then it will become ten okay but if there's a exist which is one so value of x would be one here and we have y whose value is actually default value is twenty

### 00:20:00 · Speaker 1

but let's say B is also defined here with a value of undefined. So B is undefined here. So the value of Y should be what you guess. And we have a C who is actually which is actually referencing the value of C is assigned to Z.

### 00:20:14 · Speaker 1

But there is no C here. Correct? C does not exist. So default value is thirty. So X and Z are already defined which is the value of X is one. Value of Z is thirty because C has not present on the object.

### 00:20:28 · Speaker 1

The only tricky part is why. Actually, why is we are assigning the value of B. B value is undefined. So what will be the output you mentioned in the comment section, if not please check my code now.

### 00:20:40 · Speaker 1

it is one twenty and thirty. Okay? See, we have B here whose value is undefined, still it is not getting added to the uh object or the Y here. The reason for that is the whole point of as an default value is whenever the value is undefined or like value is not at all passed, use the default value. Okay? A lot of people do not know this. So because of which the we are we are though be present here, we are make we are initializing the value as twenty. But think from the practical point of view why JavaScript somebody who developed this has made this feature would be

### 00:21:14 · Speaker 1

If it has a legit value of twenty or legit value of something, there is a high chance the program would execute properly than initializing it with undefined. Because of which value of Y is twenty. Now let's go to last snippet, the tenth snippet. Okay?

### 00:21:29 · Speaker 1

So we have a return, we have a nursing function, okay? Where we are awaiting inside that, where we are resolving the promise or resolve of hello. Immediately, almost immediately we would do this, but definitely JavaScript takes into event loop and all the concepts exit as you very well know. So where we are doing console.log of result and console.log of world, okay? So this is returning almost immediately because we are not keeping any set time out or anything, this particular promise is returned immediately, correct? So in this the problem here is or the crux of the problem

### 00:21:59 · Speaker 1

problem is which log is executed first. Okay, this is almost an easy question for most of the middle level engineers. For a fresher you can still think and tell what the order it would execute. Okay, let me execute the code for you.

### 00:22:12 · Speaker 1

So it is world followed by hello. First we are printing the world and then we are printing the hello. That that's the difference. The reason for that is despite it is returning almost immediately, JavaScript has certain keywords that are known to it. Whenever such keywords appear, JavaScript thinks that these are the keywords that I need to process asynchronously, okay? Because of which it will be keep moving those things to asynchronous block and it will execute the synchronous things first and then it will take that. Because of which world is printed first followed by the result, okay? As simple as that, uh I have all the

### 00:22:42 · Speaker 1

snippet that whatever I asked in the whatever I asked in the particular video I'm going to put that in my github repository or the new book that I'm publishing I'm going to part of that book and I put the link in the description section so that you can copy the snippets and practice on your own and that's all for the video if you like the video please like the video comment whatever you felt honestly please share the video with your friends so that they can also get benefited and if you're not subscribed to my channel kids subscribe more such content I'll be always putting see videos are made once in a while but lot of such contents I'll be keep putting on my linkedin so you're not

### 00:23:12 · Speaker 1

follow my LinkedIn account, please follow. link in the link in the description section where I put lot of technical concepts on a day to day basis, okay? Be a part of our Telegram group where we have three thousand hundred plus content developers all across the world. I'm going to share a lot of interesting things. Day to day discussions cannot be we cannot make a video on that. Lot of such good discussions happen in the group. So be a part of that. Thank you so much for watching. Catch you in the next video.
