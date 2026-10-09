---
id: FUX1aObKaTQ
title: "ReactJS & JS Mock Interview Pt - 2 |  \U0001F389 Senior Developer \U0001F389\
  \ | \U0001F525  All questions rightly answered \U0001F525"
url: https://www.youtube.com/watch?v=FUX1aObKaTQ
date: '2022-09-14'
duration: 00:39:16
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# ReactJS & JS Mock Interview Pt - 2 |  🎉 Senior Developer 🎉 | 🔥  All questions rightly answered 🔥


## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Uncommon Geeks. Myself, Fasant, I hope you all are doing well. In case if you are seeing me for the first time on the internet, I am a content creator. I help people to clear the interview. Like I always have made a lot of beautiful series in the past, which has been appreciated by many. I'll try to add link to those series somewhere on the screen also in the description section. Please go ahead and watch it. Any sort of interview you are preparing, this will be definitely helpful for you. Okay, now as you already know, I have got close to 1.1k subscribers on YouTube. As a part of the love and the blessing that you have given and I have accomplished it in a very short span.

### 00:00:30 · Speaker 1

I'm trying to give something back. So I'm taking few free mock interviews. Okay. And in today's episode, I'll be interviewing a very senior developer. His name is Deepak. So I'll be interviewing him. I'll be interviewing as in I'll be taking the interview of him with a basic JavaScript and React. Let's see how the interview goes. Let's get started.

### 00:00:58 · Speaker 1

Hi Deepak, as you already know, this is regarding the mock interview with JavaScript and React. I'll start by giving basic introduction of mine, then I'll take your introduction, then I'll give a brief overview about the overall interview process, then we shall get started. Okay, as you know I'm Vasanth, I'm a YouTuber. I work as a front-end developer, I have a good knowledge on both web and the mobile application development.

### 00:01:20 · Speaker 1

And this interview very specifically, as we have decided to be mock interview of JavaScript and React, we have a half an hour time where in the first half, let us try to delve into concepts where I'll be asking you a few questions on JavaScript and React concepts. And remaining 15 minutes to 15, 20 minutes, I'll share certain snippets with you and you need to be predicting the output of it. So whenever you are predicting, I'll touch base on some more concepts in them.

### 00:01:44 · Speaker 1

So that's all from my end regarding myself and the interview process can I please get you an introduction deepak your skills your aspirations yeah

### 00:01:51 · Speaker 3

Yeah, sure. So I'm Deepak Chandani and I have around eight years of experience working as a full stack developer. I started my journey from jQuery days and then I worked on different frameworks as JS ecosystem kept evolving. So I worked on AngularJS and then I worked on BackboneJS. And from past three or four years, I've been working in ReactJS majorly.

### 00:02:20 · Speaker 3

So that's a brief about my journey and I'm aspiring for product based companies where I can utilize my knowledge and work on some challenging steps that they are building. Wonderful. That's what I want.

### 00:02:35 · Speaker 1

Sure, sure Deepak. Clean net introduction. Thanks for the same. Okay. Let's get started with the extreme basics Deepak. Okay. So please tell me what is hoisting in JavaScript.

### 00:02:46 · Speaker 3

All right, hosting, hosting is, so what happens is when JavaScript engine gets a program to be executed, it runs, it, it runs that program in two phases. So first one is the creation phase in which it basically scans what is inside the code and then the interpreter comes into a second phase, which is the execution phase in which line by line it executes all the program that we have written.

### 00:03:16 · Speaker 3

So in the creation phase, what happens that first when we give a program file to an interpreter, then in the creation phase, all the variable declarations are hoisted to the top of the program. So they are basically, say suppose we have 10 lines in the program and on the fifth line you are creating a variable. So on those top four lines, what happens is you can use that variable X.

### 00:03:46 · Speaker 3

in in those four lines why because hoisting is happening so javascript union uh creates a separate space for those variables even though they are defined at the bottom of the file but it in the scanning process it creates them and and declares them or initializes them with undefined value

### 00:04:05 · Speaker 3

This is hoisting basically

### 00:04:09 · Speaker 1

you said is absolutely right uh deepak i'll just add certain variations to it uh you confirm whether what i'm i'm saying is right or wrong so hosting is a process like you said it's uh moves to the top of the block so i i'll add just small one more word into it does it really move the declaration to the top of the block or it just appears to move the declaration to the top of the block

### 00:04:29 · Speaker 3

It appears to

### 00:04:31 · Speaker 1

Why it appears to move and why it doesn't really move

### 00:04:42 · Speaker 3

It doesn't really moves I can say that

### 00:04:50 · Speaker 3

Um because it it doesn't really moves because we know that it's not happening like the JavaScript engine is not changing the code that we have provided to him

### 00:05:03 · Speaker 3

Yeah, so that's I'm feeling.

### 00:05:05 · Speaker 1

What you're saying is correct, basically like you said it doesn't move because there is nobody sitting in the background who will take our variable from line number 8 and move it to line number 2, correct? Just because of the memory allocation the variables can be accessed even before they are declared. It seems to be like that, correct? So just the appearing, not the actual moment. Good.

### 00:05:24 · Speaker 1

Please tell me what are closures sir the book

### 00:05:27 · Speaker 3

Yeah, so closures in JavaScript happen when we have, say, suppose we have an outer function and we have an inner function. Now that outer function is returning an inner function, which will be later executed. The inner will be later executed. And what happens is, because we know that the inner function will be executed later in some time, but it can use some of the variables which were local to that outer function. So the parent function.

### 00:05:57 · Speaker 3

Correct. And due to that JavaScript has to has to keep some closure. So in this scenario closure happens where the even if the in outer function was execution was completed but still the inner function has access to the variables defined inside the outer function. So that's a scenario where closures happen.

### 00:06:20 · Speaker 1

Absolutely it's absolutely right can you give me one real time example deepak where closures can be used

### 00:06:26 · Speaker 3

Yeah, so I've seen in some of the scenarios like

### 00:06:32 · Speaker 3

Um, like there is a module pattern in JavaScript where what happens is people used to, uh, like we, we, we can create a module in which we want some private variables to be there and we want to return some of the functions which, which we, we want to expose them so that the user of those module can utilize those functions. And in a simple example, we can say that, say, suppose we have a function which has

### 00:07:02 · Speaker 3

counter and then it returns two functions for adding and deleting but the value of counter is accessible only to that module not to the external user

### 00:07:16 · Speaker 3

This is

### 00:07:17 · Speaker 1

is the right can you give me an any practical example that you think of this one you said is fine anything maybe in a little broader perspective you know anything

### 00:07:32 · Speaker 3

I think one example can be where we where I actually use where we all use it regularly is that in react what happens we create a hook or we create a component and in that component

### 00:07:47 · Speaker 3

we create a function or say suppose we are creating a custom component custom hook sorry

### 00:07:54 · Speaker 3

In that we we create a variable but we have access to that variable inside some of the utility functions which we are returning from that custom hook.

### 00:08:05 · Speaker 3

So say suppose you are creating a custom hook to fetch something, fetch from, say suppose use fetch. And in that you create some is loading and other variables or other state variables. And those state variables can be used inside the click handlers also. So what essentially we are doing is we are using a local variable of the parent function that is outer function inside an inner one.

### 00:08:33 · Speaker 1

Yeah I mean not wrong uh can it can be little improvised but no no issues deep down can it invert its function currying in JavaScript C-U-R-Y-I-N-G currying

### 00:08:46 · Speaker 3

Okay um currying is

### 00:08:52 · Speaker 3

Yeah, so in currying what happens is we say suppose we have a function which takes some arguments and then uh...

### 00:09:02 · Speaker 3

we want that function to be partially executed so say suppose like it I'll take an example and that will make it easier so suppose we have an add function and add function takes multiple arguments let's say three or four arguments

### 00:09:20 · Speaker 3

And we want to curry it. So in currying, what happens is when you pass that function from a curried function, then what we get is a new function which can be invoked with single parameter. So say suppose A, B, C were passed to the original function and the curried function can be executed partially. So you can pass one and then two.

### 00:09:50 · Speaker 3

And then it will return a new function which can be invoked by passing three

### 00:09:54 · Speaker 1

Correct, correct. What you said is correct. Basically, currying is not like a fundamental concept. Like there is not much of a documentation related to it in developer Mozilla. So it doesn't have an appropriate definition. Like what you explained was right. I am coming that way. Because many in the interview that try to find a definition, there is no absolute definition as such. So it's more like explanation with a definition.

### 00:10:16 · Speaker 1

Tell me what are pure components and reactant

### 00:10:20 · Speaker 3

Yeah so

### 00:10:23 · Speaker 3

components in react okay so

### 00:10:34 · Speaker 3

Yeah, so in React, what happens is whenever we change the props, whenever a component's prop is changed or a state is changed, state is inside that component only, but props are passed from outside. So whenever the prop is changed, so the parent component might be providing some prop and then later on it provided new value of that prop, that time component re-renders.

### 00:11:03 · Speaker 3

And usually what happens is it's a default behavior, but sometimes what we want is we want that component to re-render only when we receive a new prop, a new value of the prop. And we want to skip the re-rendering whenever the same props are being passed.

### 00:11:26 · Speaker 3

So in that case, we create a component, we can say that the component that we want is a pure component, which only re-renders when the props are changing. And by default, in class components, there is a pure component class from which we extend and create a new component.

### 00:11:49 · Speaker 1

In functional components how you will create your components in functional components

### 00:11:58 · Speaker 3

This PR behavior can be achieved in in the functional uh components in React by using React

### 00:12:04 · Speaker 1

react.memo you can definitely use for creating the functional component a pure components in with the help of functional component correct i'll give i'll ask you in practical example tell me let's say you have a pure component inside a parent component and you are passing a prop called x

### 00:12:19 · Speaker 1

The value of x was ten before.

### 00:12:24 · Speaker 1

The parent component has re-rendered. Due to some reason, the value of x has been changed from 10 to 10 again. Some processing happened, but x is still 10. But there's a set state of x has happened. Okay. Now, will the pure component re-render or not?

### 00:12:46 · Speaker 3

I'll I'll need a a repeat of that sorry

### 00:12:49 · Speaker 1

So you have yeah there's a parent component and a child component inside that parent component

### 00:12:49 · Speaker 3

Oh you have

### 00:12:54 · Speaker 1

the child component is a pure component okay so child component is taking a prop called x okay whose value by default was 10 and during some processing uh the x value is recomputed but the even the recomputed value is also 10 okay but there is a set set state has been called for that x with a new value of 10 okay old also 10 new also 10 will the pure component re-render or not

### 00:13:21 · Speaker 3

Okay, so we have a child component which was previously also receiving 10 as a prop value. And then again, after later some computation, 10 value was again passed to it.

### 00:13:26 · Speaker 1

I got a problem

### 00:13:33 · Speaker 1

Correct correct

### 00:13:34 · Speaker 3

And that child component is a pure one. Correct. Okay. So in this case, it won't be re-rendered, I think.

### 00:13:43 · Speaker 1

So I'll extend this example a little bit. Let's say you're passing an object to the child component and the object is again reset to the same object value. Will it re-render or not?

### 00:13:54 · Speaker 3

Yeah, in case of objects, what happens is if that object coming from the parent component is memoized or memoized one or not. If it's a memoized one, so that means referentially the previous object and the new object that is being passed are equal. Correct. In that case, it won't re-render. But if you're creating a new object, referentially they are not equal, then that will re-render.

### 00:14:17 · Speaker 1

What a what about functions

### 00:14:20 · Speaker 1

You're passing function as a

### 00:14:21 · Speaker 3

the same yeah the same applies to functions also uh so if that function is the memoized one uh we can say it's uh referring or pointing to the same function which was previously passed then uh re-rendering will not happen

### 00:14:37 · Speaker 1

Wonderful what you say

### 00:14:38 · Speaker 3

is but if uh yeah you've got the answer

### 00:14:41 · Speaker 1

Yes exactly can you tell me what is component composition in react

### 00:14:46 · Speaker 3

All right component composition so in React what happens is

### 00:14:54 · Speaker 3

we can have a component which has uh generally what we do we create a component say suppose a list component and we create li's in uh ul and then inside that li this is all html composition

### 00:15:09 · Speaker 3

what in react the beauty is that we can create our own list component which can have list items a custom component so in a way what we are doing is we are creating a parent list list component and then we can create list items in that so those are custom components and the parent component can receive those children in a children prop

### 00:15:37 · Speaker 1

Can you give me one one realistic example where component composition can be used?

### 00:15:37 · Speaker 3

Can you give me one one

### 00:15:44 · Speaker 3

Um

### 00:15:54 · Speaker 3

Generally I have seen in in some of the UI kits if I can say like in in react bootstrap or in material UI we see a lot of rows and then columns and then table so we create a parent table and inside that we create a row and then inside it we create a column this is a real example

### 00:16:19 · Speaker 1

But this is a real example. More from the project point of view or something like that, if you have to say, whenever we are having kind of an embedding process, let's say one is creating the entire container and somebody will embed the things inside that. Correct? For example, some cards or some shopping related items. So the one who create a container, he doesn't bother. Who will come tomorrow and insert the things? He'll only worry about the containers. So that with the help of compositions, we can allow that. Like if you don't pass anything, I'll render this. If you wish to pass something, you can pass. So just make sure my layout doesn't break.

### 00:16:49 · Speaker 1

Correct good can you please open JS fiddle and

### 00:16:53 · Speaker 3

Yeah, just one example I remembered is of the accordion. So accordion can be a parent one and inside accordion we have different panels. And accordion itself takes care of whichever panel is open or closed.

### 00:17:11 · Speaker 1

Yes, yes, Deepak, correct. Yeah, can you please open GS Fiddle and present your screen?

### 00:17:16 · Speaker 3

Yeah just one second

### 00:17:37 · Speaker 3

Um

### 00:17:43 · Speaker 3

Spreading the screen

### 00:17:52 · Speaker 3

It's actually giving me error that um I'm not the host that's why I can't

### 00:17:58 · Speaker 1

One sec one sec let me give you permission yeah can you try now

### 00:18:08 · Speaker 1

Zoom has added a lot of securities last year after the breach right Zoom has made it so so complicated to join

### 00:18:19 · Speaker 3

Alright

### 00:18:22 · Speaker 3

Not sure

### 00:18:24 · Speaker 1

Yes I can see your screen

### 00:18:27 · Speaker 1

So I'm presenting I'm sharing a code snippet in the zoom chart. Please copy the snippet and paste that in the JavaScript editor. Don't run the code.

### 00:18:47 · Speaker 1

Can you zoom in a bit so that me and the audience can see it much better

### 00:18:54 · Speaker 1

Yeah maybe two more Two more times

### 00:18:58 · Speaker 1

Last one more one more yes

### 00:19:02 · Speaker 1

Please guess the output it can take two minutes and try to guess the output

### 00:19:07 · Speaker 1

Sorry to disturb you in the middle. So in case if you're enjoying the session, like how Deepak is answering and how I'm asking the question, please like the video and comment whatever you feel. Like are you liking the mock interview or this could have been improved further? Please add your comment. By more likes and comment, I get more impressions. More impression means more people have a chance of watching my video. When more people watch, obviously this channel becomes popular and I'll be able to reach a lot of people. So please like and comment about the video and continue watching further. Thank you so much.

### 00:19:38 · Speaker 3

we have a function here we have object object length and we have this function

### 00:19:48 · Speaker 3

increments of zero and then we are calling it

### 00:19:55 · Speaker 3

so we are calling object.method

### 00:20:00 · Speaker 3

And method inside this method we are passing fn to this fn and we call this fn

### 00:20:13 · Speaker 3

and this is called using this object so here this will be pointing to this object

### 00:20:22 · Speaker 3

So the length here, length here could, I think it should be five because this might be pointing to object.

### 00:20:33 · Speaker 3

Uh okay

### 00:20:38 · Speaker 3

And then here we have arguments of zero and then we are calling it

### 00:20:44 · Speaker 3

So we are calling that function

### 00:20:48 · Speaker 3

Oh dear

### 00:20:51 · Speaker 3

Alright

### 00:20:54 · Speaker 3

inside we don't have this and here

### 00:20:59 · Speaker 3

This should go

### 00:21:02 · Speaker 3

Take care

### 00:21:04 · Speaker 3

I've quickly done it I'll try to explain my thought process what I

### 00:21:10 · Speaker 3

First first can

### 00:21:10 · Speaker 4

First first confirm the output yeah first confirm what will be the output

### 00:21:16 · Speaker 3

So for for this first call

### 00:21:23 · Speaker 3

passing the function so inside this we are calling from here

### 00:21:34 · Speaker 3

So here the

### 00:21:38 · Speaker 3

We don't have anything

### 00:21:41 · Speaker 3

but by default it will be where it is being called so it's being called from here so this will be fine

### 00:21:52 · Speaker 3

Cheers

### 00:21:55 · Speaker 3

This is again being called from here only not from the event

### 00:22:04 · Speaker 3

And inside is this is pointing to this object

### 00:22:12 · Speaker 3

This will also be fine. Yeah, so I think I should return.

### 00:22:17 · Speaker 4

I am Shu

### 00:22:18 · Speaker 3

Yeah, the yeah, this will return five and this will also return time, but I might be wrong.

### 00:22:24 · Speaker 1

Here top left you see I've done it

### 00:22:31 · Speaker 3

Excellent

### 00:22:32 · Speaker 1

Extreme left, extreme left.

### 00:22:35 · Speaker 1

Now top say left we have the URL

### 00:22:40 · Speaker 1

Yes yes please

### 00:22:44 · Speaker 1

So you're seeing the in bottom right you're seeing the output

### 00:22:47 · Speaker 3

Yeah ten and then two

### 00:22:49 · Speaker 1

Any idea why it turned into you can try to take a minute and try to deduce

### 00:22:58 · Speaker 3

So 10, I understand, like this is returning 10. So what this means is this here is pointing to window actually. I was thinking that it's pointing to this object, but this is pointing to window and the length variable is coming from the parent window object.

### 00:23:21 · Speaker 2

Ready for this

### 00:23:21 · Speaker 3

Ready for this

### 00:23:24 · Speaker 3

Was that the right one?

### 00:23:26 · Speaker 1

Yeah that is correct yes what you're saying is right

### 00:23:30 · Speaker 1

Basically it doesn't take objects reference because you're calling a function which is completely external. Let's say there is a method inside the object like a method two which has a function and that you are invoking. That time it will look for the reference in the object, correct? So now you're calling somewhere something altogether an external function. So there is nothing of this objects this you are not passing. So there this rep points to window, okay? Any idea why two is the print?

### 00:23:55 · Speaker 3

Yeah so this one is interesting so we have fn and what it's saying is we have two arguments passed to this

### 00:24:05 · Speaker 3

saying arguments of zero and invoking it

### 00:24:10 · Speaker 3

In arguments of zero we see that it's fn

### 00:24:14 · Speaker 3

Can I finish

### 00:24:20 · Speaker 3

FN is called this way

### 00:24:26 · Speaker 3

So here what I see is this might be referring to that function.

### 00:24:34 · Speaker 3

Yeah this might

### 00:24:37 · Speaker 3

referring to

### 00:24:43 · Speaker 3

Arguments of zero is an fn and fn is this

### 00:24:52 · Speaker 3

when this function is called it's saying this function's length

### 00:25:04 · Speaker 3

Yeah, what I can guess right now, I'm not sure I'm right or wrong, but I think in this case, this is pointing to the function.

### 00:25:16 · Speaker 1

Okay function as in the one that you're passing line number fourteen

### 00:25:19 · Speaker 1

The function that you are passing in line number fourteen is which is on line number two

### 00:25:27 · Speaker 1

I mean I don't know

### 00:25:27 · Speaker 3

I mean

### 00:25:28 · Speaker 1

How two can come

### 00:25:31 · Speaker 1

Do one thing in line number 14 after function comma 1 add comma 2

### 00:25:36 · Speaker 1

And number forty

### 00:25:40 · Speaker 1

After one day

### 00:25:40 · Speaker 4

Yeah one comma two

### 00:25:48 · Speaker 1

Now you get a sense

### 00:25:50 · Speaker 3

Exactly yeah so this is the method which is being tested

### 00:25:56 · Speaker 1

No object.method is in line number eight

### 00:25:56 · Speaker 3

They're taking

### 00:25:58 · Speaker 1

That only you're calling

### 00:26:00 · Speaker 1

So now how two became three you got a sense right how two is two turned into three

### 00:26:07 · Speaker 3

Or this is actually the ar arguments

### 00:26:12 · Speaker 1

So that's what I say. Maybe even if you work with JavaScript our whole life, not that you couldn't get, none of us will be able to master it, I'm thinking. There will be somewhere or the other edge case where we all miss. Okay. Good. I'll share one last snippet with you. Okay. So that will.

### 00:26:34 · Speaker 1

This is uh one moment I'll share

### 00:26:45 · Speaker 1

You just copy the snippet and paste there

### 00:26:48 · Speaker 1

Again you do please don't run

### 00:26:52 · Speaker 3

I can remove this

### 00:26:54 · Speaker 1

Yeah yeah

### 00:26:58 · Speaker 1

Please guess the output much straightforward

### 00:27:02 · Speaker 3

So we are creating a function self invoking it so

### 00:27:08 · Speaker 3

right to form here so we'll get one first of all

### 00:27:16 · Speaker 3

or straight away

### 00:27:20 · Speaker 3

Then these two will go in queue.

### 00:27:25 · Speaker 3

as this is having both us at time out

### 00:27:29 · Speaker 3

So

### 00:27:31 · Speaker 3

Put us at time out this first one is zero so this should execute first

### 00:27:36 · Speaker 3

And then two that is after one second

### 00:27:40 · Speaker 1

Oh please

### 00:27:42 · Speaker 1

You're confident in that

### 00:27:43 · Speaker 3

I know that

### 00:27:44 · Speaker 1

It's dark, eh?

### 00:27:45 · Speaker 3

Yeah I think I don't see any ticky thing here

### 00:27:48 · Speaker 1

Listen listen

### 00:27:48 · Speaker 3

Listen

### 00:27:53 · Speaker 1

So one, four, three, two, correct? Let's do this. In line number four, whatever you have for line number four, set time would just be basically a function, right? Can you convert that into a self-invoking function?

### 00:28:05 · Speaker 3

Alright so

### 00:28:10 · Speaker 1

Yes, so you have to add one more brackets in the starting and the end.

### 00:28:20 · Speaker 1

Now can you guess that

### 00:28:26 · Speaker 3

So basically this will be invoked immediately

### 00:28:30 · Speaker 3

Um

### 00:28:34 · Speaker 3

So we'll have one as previous and then

### 00:28:39 · Speaker 3

This will be immediately executed. So, this will give us three.

### 00:28:46 · Speaker 3

then we'll have four and then we'll have two

### 00:28:50 · Speaker 1

Please explain why that will be immediately executed

### 00:28:54 · Speaker 3

Yeah, so we what we have done is this part is creating a function and these two parameter parentheses are immediately executing that function.

### 00:29:04 · Speaker 1

Sure, as per event loop concept what should happen whenever set timeout is encountered

### 00:29:05 · Speaker 3

That's pretty good

### 00:29:12 · Speaker 3

I missed that can you repeat it

### 00:29:13 · Speaker 1

As per event loop concept, whenever a set timeout is encountered, what should the JavaScript engine do? Will it take it from call stack and move somewhere else or what is the process?

### 00:29:24 · Speaker 3

Yeah so whenever set timeout is encountered

### 00:29:28 · Speaker 3

And whatever function is provided

### 00:29:32 · Speaker 3

that set timeout executes but this callback is moved into an queue and it's a it's a queue in which which will wait for this particular time to complete and then uh it the event loop will check if this if the call is the execution stack is empty or not if it's empty then it will bring that pending callback into the stack and that will be executed

### 00:30:01 · Speaker 1

So now in this case, set timeout is there inside that there is a self invoking function, correct? How come the function will execute immediately?

### 00:30:10 · Speaker 1

Yeah directly into a call stack right it cannot directly take into call stack

### 00:30:10 · Speaker 3

Yeah

### 00:30:14 · Speaker 1

As per the explanation

### 00:30:18 · Speaker 3

So what I see here is like in the difference between line number three and four is that this is a reference to a function. Consider it as a callback. Got it. But this is actually executed immediately.

### 00:30:38 · Speaker 1

So in line number four instead of zero make it three second

### 00:30:42 · Speaker 1

Three double zero three second

### 00:30:45 · Speaker 1

I'm not asking the output in this case now after three seconds something has to happen what will happen

### 00:30:52 · Speaker 1

So will a set time have to be registered or no

### 00:31:03 · Speaker 3

So this is a function and it's written. So the output of this expression would be undefined actually. And what what what set timeout will be receiving is basically once this is executed, it will be receiving undefined or void as we can see.

### 00:31:23 · Speaker 3

So there is a chance that it might check that if undefined is passed as a callback to set timeout, then it won't do anything.

### 00:31:31 · Speaker 1

True, true. Correct. What you said is absolutely right, Deepak. Okay. Many get confused in this process. First of all, many will not be able to guess the output only, the order of. Even if they're able to guess the order, whenever a self-involving function comes, they get confused. Okay. Even after self-involving function, whenever this undefined kind of a concepts come, they further get confused. You're able to answer all the things well. Can you stop sharing?

### 00:32:02 · Speaker 1

Yeah, Deepak, so we, I mean, I did not get to know how the time flew. We almost finished half an hour already. Okay. So first, please feel free to ask me, Deepak, if you have any questions for me.

### 00:32:16 · Speaker 1

Not specifically from interview if you have any other questions also generally also you can ask yeah

### 00:32:26 · Speaker 3

I don't have any question right now

### 00:32:29 · Speaker 1

Just shed the

### 00:32:29 · Speaker 3

The car

### 00:32:31 · Speaker 1

good good i i'll just give pass on my feedback every viewer also got my feedback i don't have to explicitly say it yeah uh i mean it was a very clean neat interview in not just the mock into that i take for the channel overall in my interview process very few will have very in-depth knowledge okay and i think you will also be taking interviews a lot of candidate we there is a concept of the breadth and depth where people touch base on a lot of topics and they get in whenever they feel candidate might not be confident okay with my breadth and depth whatever i applied with you have good

### 00:33:01 · Speaker 1

of knowledge on all the concepts okay like a first thing always i say is the technical communication communication is one thing technical communication is very very important correct let's say when i ask you function currying you should you do not say like i'll type and explain correct because as a developer our job is not just the coding we have you should be able to articulate our thoughts to a lot of folks correct so the technical communication part is very very good and the second part is the conceptual knowledge this is something that you uh upload in an engineer after a point like senior

### 00:33:31 · Speaker 1

engineer like you eight year ten year whenever some concepts come they should be able to articulate it well i mean explain the with help of concept like the pure component example which i might have asked like you're passing a function you're passing an object you clearly know what is happening under the hood that is something that will give a respect to engineer after a point correct just because if somebody becomes an architect people will not respect only because he has that kind of a knowledge then only people respect so fundamental knowledge is very very good third point is the uh the guessing the output the way the snippet

### 00:34:01 · Speaker 1

thing so first you were able unable to answer i mean partially you were right second you were able to answer clearly okay first question uh with my experience i haven't seen anyone answering in the first go including me okay it's not uh straightforward i mean obviously i i also don't say it is something with that we can judge an engineer but uh it also depends on how depth you have understood that's the only thing uh just because somebody says one gets the output wrong that doesn't mean they're bad all right but only thing we just try to uh evaluate how depth they are able to understand or

### 00:34:31 · Speaker 1

Just connect between the thoughts. Only that I can tell. Maybe more snippet driven questions you can solve. Rest seems to be good. I mean, if you are applying for tier 2 and tier 3, you are already there. Maybe if you are applying for tier 1, you very well know. Maybe you may have to practice if you are not done machine coding and the DSA. That's all I have to say. Any other questions you have, Deepak?

### 00:34:50 · Speaker 3

No it was it was really good to communicate with you and doing this

### 00:34:57 · Speaker 3

Actually yeah actually the general thing is it's always good to listen to someone who can give a feedback to you so I'm I'm happy with that

### 00:35:06 · Speaker 1

Yes, yes. Share Deepak. Like I mentioned, definitely I'll share a detailed feedback over the email. And hope you're watching uncommon geeks Deepak, my YouTube channel. How are you thinking? How the videos are coming?

### 00:35:17 · Speaker 3

It's good. And I would say most of us, with most of us, what happens is we, we really, we try very hard to understand things and then come up with our answers. But we, we don't know where a mistake is happening and where we need to work upon. So this is, and this, this very much happens when you are in an early phase, when you're learning some.

### 00:35:47 · Speaker 3

and trying and I'm hustling and doing all those things so that information is very valuable which you are passing in your channel that this is something which should you should work upon and this is your thought process this should be your thought process to explain a solution to any interviewer this is very valuable thing I'm getting from your videos

### 00:36:09 · Speaker 1

Thank you thank you so much

### 00:36:12 · Speaker 1

the bug then we are almost at the end of the interview it was very nice talking to you i mean um you you are a senior engineer good that i could explore and i also learned a lot of things from you generally sometimes i get kind of very fast sometimes now now i've reduced a lot but even before the questions are people try to jump in and try to answer i had that attitude long way back but i see you whenever you come reading you are very matured like you wait until the question is fully asked that is one of the very important quality in interview you should never jump in correct you should fully listen to the question because interviewer

### 00:36:42 · Speaker 1

then say I was still explaining you jumped in correct so that we should have that patience um and the whenever total listening skills how the communication skills are important in the interview listening skills are also equally important I I that is something that I still working on and I I got to learn that from you further

### 00:37:01 · Speaker 1

Thank you very nice talking thank you have a good day bye

### 00:37:04 · Speaker 3

Thank you bye

### 00:37:06 · Speaker 1

Again, welcome back. I think, hope you enjoyed the interview session with Deepak. Deepak is a very senior engineer and he was able to answer all the different areas that I was asking the question, whether it is conceptual, whether it is technical communication or whether it is the problem solving, depending on the snippets getting the output. He was absolutely on top notch. So like I mentioned, he is almost at the, he could easily clear most of the type two and type three interviews if he appeared to. So I'm very happy I could interview him as a senior to me as well. I learned the sense, like I mentioned, I was a, I got that,

### 00:37:36 · Speaker 1

knowledge of being very calm in the interview. I'm still trying to be more better at it. Sometimes I get quite enthu and I'll try to answer much quickly. So but Deepak was very calm throughout the interview. Might have absorbed him. So where he he he waited for the question to complete. He took his time. Then he was trying to give a right answer. So this is the strategy. Some of you who are at least in junior and mid-level will have a little more enthusiasm where they will not listen for the question completion. So please don't do that. Like how Deepak did properly in the interview.

### 00:38:06 · Speaker 1

please follow this method of comment compost okay and if you're someone who is also looking for a free mock interview like this okay please register in the google form which is there in the comment section it's very obvious i'll not be able to take interview for all but whomsoever possible i'll definitely try to take if not now in future like whenever i need some partners for my video i'll definitely reach out to you i take very basic minimal details to contact you okay and if the form is inactive it's an indication because somebody may watch this video after one year if the form is inactive it's an indication i'm no longer taking the mock interview at that point in time

### 00:38:36 · Speaker 1

Okay, thank you so much for watching. If you're not like with that video, please like the video, comment whatever you felt in the mock interview. Was it beneficial for you, et cetera? The question that I snipped that I asked in the interview, that snippets are available in my GitHub repository. I'll try to link that in the description. Please go ahead and download the questions and practice on your own. My medium blog URL is also in the description. Please follow me on medium. Almost every week I write a very interesting article, which will be helpful for you to clear your interview in the front end domain. So please follow me on medium and subscribe to my newsletter. Star my GitHub project so that I can.

### 00:39:06 · Speaker 1

I'll be able to make more add more content to my project and the project becomes visible whenever people search in the Google etc. Okay. Thank you so much for watching. Catch you next video.

