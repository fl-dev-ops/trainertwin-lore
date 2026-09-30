---
id: FUX1aObKaTQ
title: ReactJS & JS Mock Interview Pt - 2 | 🎉 Senior Developer 🎉 | 🔥 All questions
  rightly answered 🔥
date: '2022-09-14'
url: https://www.youtube.com/watch?v=FUX1aObKaTQ
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ #frontenddeveloper #mockinterview #uncommonGeeks \nLink for registering mock interview,\
  \ register only if your ready to publish your video on Youtube: https://forms.gle/38sNpiqrdrUrhm7MA\n\
  \nReactJS & JS Mock Interview Pt - 1: https://youtu.be/O7n9w_f9u9A\n\nInterview\
  \ Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nMedium Blog https://mevasanth.medium.com/ \n\nFollow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  \nGithub Repository that contains examples: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript/blob/main/MockInterviewQuestions/DeepakMock.js\n\
  \nJavaScript Custom implementation introduction: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s"
author: careerwithvasanth
duration: 00:39:16
model: saaras:v3
transcript: true
---

# ReactJS & JS Mock Interview Pt - 2 | 🎉 Senior Developer 🎉 | 🔥 All questions rightly answered 🔥

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Uncommon Geeks. Myself, Fasant. I hope you all doing well. In case if you are seeing me first time on the internet, I'm a content creator. I help people to clear the interview. Like I always have made lot of beautiful series in the past which has been appreciated by many. I'll try to add link to those series somewhere on the screen also in the description section. Please go ahead and watch it. Any sort of front end interview you are preparing, this will be definitely helpful for you. Okay? Now, as you already know, I have got close to 1.1k subscribers on YouTube. As a part of the love and the blessing that you have given and I have accomplished it in a very short

### 00:00:30 · Speaker 1

fan. I'm trying to give something back. So I'm taking few free mock interviews, okay? And in today's episode, I'll be interviewing a very senior developer. His name is Deepak. So I'll be interviewing him. I mean interviewing as in I'll be taking the interview of him with a basic JavaScript and React. Let's see how the interview goes. Let's get started.

### 00:00:56 · Speaker 1

Yeah

### 00:00:57 · Speaker 1

So, hi Deepak, uh as you already know, uh this is regarding the mock interview with JavaScript and React. I'll start by giving basic introduction of mine, then I'll take your introduction, then I'll give a brief overview about the overall interview process, then we shall get started, okay? As you know I'm Vasant, I'm a YouTuber. uh I I work as a front end developer, I have a good knowledge on both web and the mobile application development. uh And this interview very specifically as we have decided to be mock interview of JavaScript and React, we have a half an hour time where

### 00:01:27 · Speaker 1

In the first half let us try to delve into concepts where I'll be asking you few questions on JavaScript and React concepts. And remaining fifteen minutes to fifteen twenty minutes I'll share certain snippets with you and you need to be predicting the output of it. So whenever you are predicting I'll touch base on some more concepts in depth. Okay? So that's all from my end regarding myself and the interview process. Can I please get your introduction Deepak? Your skills, your aspirations. Yeah.

### 00:01:49 · Speaker 3

respiration

### 00:01:51 · Speaker 3

Yeah, sure. So, I'm Deepak Chandani and I have around eight years of experience working as a full stack developer.

### 00:01:58 · Speaker 2

Wonderful

### 00:01:58 · Speaker 3

I started my journey from JQuery days and then I worked on different frameworks as JS ecosystem kept evolving. So I worked on Angular JS and then I worked on Backbone JS. And from past three or four years I've been working in React JS majorly. And

### 00:02:08 · Speaker 2

character

### 00:02:18 · Speaker 2

and

### 00:02:20 · Speaker 3

So, uh that's a brief about my journey and I am aspiring for product based companies where I can utilize my knowledge and work on some challenging stuffs that they are building.

### 00:02:27 · Speaker 1

Pan

### 00:02:33 · Speaker 1

Wonderful

### 00:02:33 · Speaker 3

That's what I want, yeah.

### 00:02:35 · Speaker 1

Sure, sure Deepak. Clean introduction, thanks for the same, okay? Let's get started with the extreme basics Deepak, okay? So please tell me what is hosting in JavaScript.

### 00:02:42 · Speaker 3

complete

### 00:02:46 · Speaker 3

Alright, hosting, uh hosting is. So what happens is when uh JavaScript engine gets a program to be executed, it runs uh it it runs that program in two phases. So first one is the uh creation phase in which it basically scans uh what is inside the code and then the interpreter comes into a second phase which is the execution phase in which line by line it executes uh all the program that we have written.

### 00:03:16 · Speaker 3

So in in the creation phase what happens that first when we given a program file to interpreter then in the creation phase all the variables declarations are hoisted to the top of the program so they are basically say suppose we have ten lines in the program and on the fifth line you are creating a variable so on those top four four lines what happens is you can use that variable X

### 00:03:46 · Speaker 3

in in those four lines. Why because hoisting is happening so JavaScript engine uh creates a separate space for those variables even though they are defined at the bottom of the file but it in the scanning process it creates them and and declares them or initializes them with undefined value. This is uh hoisting basically.

### 00:04:07 · Speaker 1

Got it. So, what you said is absolutely right, Deepak. I'll just add certain variations to it. You confirm whether what I'm saying is right or wrong. So, hosting is a process, like you said, it's moves to the top of the block. So, I'll add just small one more word into it. Does it really move the declaration to the top of the block or it just appears to move the declaration to the top of the block?

### 00:04:29 · Speaker 3

it appears to

### 00:04:30 · Speaker 1

Correct. Why it appears to move and why it doesn't really move?

### 00:04:31 · Speaker 3

it appears

### 00:04:35 · Speaker 3

um

### 00:04:38 · Speaker 3

Um

### 00:04:42 · Speaker 3

it doesn't really moves, I can say that

### 00:04:49 · Speaker 3

because it it doesn't really moves because we know that it's not happening like the JavaScript engine is not changing the code that we have provided to MDF.

### 00:05:00 · Speaker 1

Exactly. Yes.

### 00:05:02 · Speaker 3

And yeah, so that's I'm feeling.

### 00:05:05 · Speaker 1

Correct. What you're saying is correct, Deepak. Basically, like you said, it doesn't move because there is nobody sitting in the background who will take our variable from line number eight and move it to line number two. Correct? Just because of the memory allocation, the variables can be accessed even before they are declared. It seems to be like that. Correct? So just appearing, not the actual moment. Good. Okay. uh Please tell me what are closures, Deepak?

### 00:05:13 · Speaker 3

but

### 00:05:14 · Speaker 3

speaker

### 00:05:27 · Speaker 3

Yeah, so closures in JavaScript are happen when we have a say suppose we have a outer function and we have a inner function. Now that outer function is returning an inner function which will be later executed, the inner will be later executed. And what happens is because we know that the inner function will be executed later in some time but it can use some of the variables which were local to that outer outer function. Correct. So the parent function.

### 00:05:36 · Speaker 2

Hmm

### 00:05:43 · Speaker 2

Hmm

### 00:05:56 · Speaker 1

Correct

### 00:05:57 · Speaker 3

correct. And due to that JavaScript has to has to keep some closure. So in this scenario closure happens where the even if the outer function was execution was completed but still the inner function has access to the variables defined inside the outer function. So that's a scenario where closures happen.

### 00:05:57 · Speaker 1

correct

### 00:06:12 · Speaker 1

but

### 00:06:20 · Speaker 1

Absolutely. It's absolutely right. Can you give me one real-time example, Deepak, where closures can be used?

### 00:06:26 · Speaker 3

Yeah, so I've seen in some of the scenarios like

### 00:06:32 · Speaker 3

like there is a module pattern in in JavaScript where what happens is people used to like we we we can create a module in which we want some private variables to be there and we want to return some of the functions which which we are we want to expose them so that the user of those module can utilize those functions and in a simple example we can say that say suppose we have a function which

### 00:07:02 · Speaker 3

as a counter and then it returns two functions for adding and deleting. But the value of counter is accessible only to that module not to the external user.

### 00:07:14 · Speaker 1

Hmm

### 00:07:15 · Speaker 1

Okay

### 00:07:16 · Speaker 3

this somewhere.

### 00:07:17 · Speaker 1

This is right. Can you give me any practical example that you think of? This one you said is fine. Anything maybe in a little broader perspective. You know anything?

### 00:07:26 · Speaker 3

Yeah

### 00:07:32 · Speaker 3

I think one example can be where we where I actually use where we all use it regularly is that in React what happens we create a hook. Correct. Or uh we create a component. And in that component

### 00:07:41 · Speaker 2

correct

### 00:07:44 · Speaker 2

Hmm

### 00:07:47 · Speaker 3

we create a function or say suppose we are creating a custom component, custom hook, sorry. And in that we we create a variable but we have access to that variable inside some of the utility functions which we are returning from that custom hook.

### 00:07:51 · Speaker 2

Hmm

### 00:08:04 · Speaker 2

Hmm hmm

### 00:08:05 · Speaker 3

So, uh say suppose you are creating a custom hook to fetch something. Got it. Fetch from uh say suppose use fetch. And in that you create some is loading and other variables or another other state variables. Yeah. And those state variables can be used inside the click handlers also.

### 00:08:10 · Speaker 2

Got it

### 00:08:12 · Speaker 2

and in

### 00:08:16 · Speaker 2

video

### 00:08:17 · Speaker 2

Yeah

### 00:08:21 · Speaker 2

Hmm hmm

### 00:08:22 · Speaker 3

So what what essentially we are doing is we are using a local variable of the parent function that is outer function inside an inner one.

### 00:08:31 · Speaker 1

Hmm

### 00:08:33 · Speaker 1

Yeah, I mean, not wrong. Can can be little improvised, but no, no issues, Deepak. Can you tell me what is function currying in JavaScript? C U double R Y I N G, currying.

### 00:08:37 · Speaker 3

Hmm

### 00:08:43 · Speaker 3

Yeah

### 00:08:46 · Speaker 3

Okay, uh, Karim is

### 00:08:52 · Speaker 3

Yeah, so in in currying what happens is we say suppose we have a function which takes some arguments and then uh

### 00:09:02 · Speaker 3

we want that function to be partially executed. So say suppose like it I'll take an example and that will make it easier.

### 00:09:10 · Speaker 1

Sure

### 00:09:11 · Speaker 3

So suppose we have an add function and add function takes multiple arguments, let's say three or four arguments.

### 00:09:13 · Speaker 1

and

### 00:09:18 · Speaker 1

Correct

### 00:09:19 · Speaker 3

and and we want to curry it. So in currying what happens is when you pass that function from a from a curried function then

### 00:09:31 · Speaker 3

then what we what we get is a new function which can be uh invoked with single parameters. So say suppose A B C were uh passed to the original function and the carried function can be executed partially. So you can pass one and then two and then it will return a new function which can be invoked by passing three.

### 00:09:54 · Speaker 1

Correct. Correct. What he said is correct. Basically, currying is not like a fundamental concept, like there is not much of a documentation related to it in developer Mozilla. So it doesn't have an appropriate definition. Like what he explained was right. I am coming that way. Because many in the interview they try to find a definition, there is no absolute definition as such. So it's more like explanation with a definition. Okay. Sure. Tell me what are pure components in React, Deepak?

### 00:09:55 · Speaker 3

Right

### 00:10:20 · Speaker 3

Yeah, so

### 00:10:23 · Speaker 3

your components in React. Okay. So,

### 00:10:29 · Speaker 2

Hmm

### 00:10:32 · Speaker 3

um

### 00:10:34 · Speaker 3

Yeah, so in React what happens is, uh whenever we whenever we change the props, whenever a component's prop is changed or a state is changed, state is inside that component only, but props are passed from outside. So whenever the prop is changed, uh so the parent component might be providing some prop and then later on it provide a new value of that prop. That time component rerenders. And and usually what happens is

### 00:10:50 · Speaker 2

Hmm

### 00:11:01 · Speaker 2

Hmm

### 00:11:04 · Speaker 3

it's a default behavior but sometimes what we want is we want that component to re-render only when we receive a new prop new value of the prop and we want to skip the re-rendering whenever the same props are being passed

### 00:11:14 · Speaker 2

uh

### 00:11:16 · Speaker 2

Hmm

### 00:11:25 · Speaker 2

Got it

### 00:11:25 · Speaker 3

Right. So in that in that case we create a component we can say that the component that we want is a pure component which only rerenders when uh when when the props are changing and and by default in class components there is a pure component class which from which we extend and create a new component.

### 00:11:47 · Speaker 1

Correct. Correct.

### 00:11:49 · Speaker 3

Sir

### 00:11:49 · Speaker 1

in functional components have you will create your components in functional components

### 00:11:55 · Speaker 3

Okay. This pure behavior can be achieved in in the functional components in React by using React

### 00:12:04 · Speaker 1

correct. React.memo you can definitely use for creating the functional component, a pure component with the help of functional component, correct? I'll give I'll ask you one practical example Deepak. Tell me. Let's say you have a pure component inside a parent component and you are passing a prop called X. Okay? The value of X was ten before.

### 00:12:23 · Speaker 1

Now, the parent component has re-rendered. uh due to some reason the value of x has been changed from ten to ten again. Some processing happened but x is still ten. But there is a set state of x has happened. Okay? Now, will the pure component re-render or not?

### 00:12:41 · Speaker 3

Okay

### 00:12:43 · Speaker 3

Um

### 00:12:46 · Speaker 3

I'll I'll need a repeat of that. Sorry. Got it. So you have

### 00:12:47 · Speaker 1

of that. Sorry. So you have yeah, there's a parent component and a child component inside that parent component and the child component is a pure component. Okay? So child component is taking a prop called X. Okay? Whose value by default was ten. And during some processing, the X value is recomputed, but even the recomputed value is also ten. Okay? But there is a set state has been called for that X with a new value of ten. Okay? Old also ten, new also ten.

### 00:12:57 · Speaker 3

Hmm

### 00:13:16 · Speaker 3

Hello sir

### 00:13:17 · Speaker 1

will the pure component rerender or not?

### 00:13:21 · Speaker 3

Okay. So, uh so we have a child component which was previously also receiving ten as a prop value. And then uh again after later some computation, ten value was again passed to it.

### 00:13:26 · Speaker 1

proper

### 00:13:27 · Speaker 1

Yeah

### 00:13:31 · Speaker 1

correct

### 00:13:33 · Speaker 1

Correct, Correct.

### 00:13:33 · Speaker 3

third

### 00:13:34 · Speaker 3

and that child component is a pure one. Correct.

### 00:13:36 · Speaker 1

Correct. Correct.

### 00:13:37 · Speaker 3

Right

### 00:13:38 · Speaker 3

Okay, so in this case, it won't be re-rendered, I think.

### 00:13:42 · Speaker 1

Got it. So I'll extend this example a little bit. Let's say you're passing an object to the child component. And the object is again reset to the same object value. Will it rerender or not?

### 00:13:54 · Speaker 3

Yeah, in in case of objects, what happens is if that object coming from the parent component is memoized or memoized one or not. If it's a memoized one, so that means referentially the previous object and the new object that is being passed are equal. Correct. In that case, it won't rerender, but if if you're creating a new object, referentially they are not equal, then that will rerender.

### 00:14:09 · Speaker 1

correct

### 00:14:11 · Speaker 1

Okay

### 00:14:15 · Speaker 1

Okay

### 00:14:17 · Speaker 1

Good. What about functions?

### 00:14:20 · Speaker 1

you're passing function

### 00:14:21 · Speaker 3

It's the same

### 00:14:22 · Speaker 1

Hmm

### 00:14:22 · Speaker 3

Yeah, the same applies to functions also. So if that function is the memoized one, we can say it's referring or pointing to the same function which was previously passed. Then re-rendering will not happen.

### 00:14:34 · Speaker 1

cut

### 00:14:37 · Speaker 1

Wonderful. But you say

### 00:14:38 · Speaker 3

But if, Yeah, yeah, you got the answer.

### 00:14:39 · Speaker 1

Hmm

### 00:14:41 · Speaker 1

Yes, exactly. Can you tell me what is component composition in React?

### 00:14:46 · Speaker 3

all right, component composition. So, in React, what happens is, uh

### 00:14:54 · Speaker 3

we can have a component which has uh generally what we do we create a component say suppose a list component and we create allies in uh UL and then inside that ally. This is all HTML composition.

### 00:15:05 · Speaker 1

that

### 00:15:06 · Speaker 1

Hmm

### 00:15:08 · Speaker 1

Correct

### 00:15:08 · Speaker 3

But what in React the beauty is that we can create our own list component which can have list items, a custom component.

### 00:15:16 · Speaker 2

custom com

### 00:15:17 · Speaker 2

Hmm

### 00:15:18 · Speaker 3

So in a way what we are doing is uh we are creating a parent uh list uh list component and then we can create list items in that. So those are custom components. And the parent component can receive those children in a children prop.

### 00:15:35 · Speaker 1

Hmm

### 00:15:37 · Speaker 1

Yeah, can you give me one one realistic example where component composition can be used?

### 00:15:37 · Speaker 3

one

### 00:15:43 · Speaker 3

Yeah

### 00:15:44 · Speaker 3

um

### 00:15:48 · Speaker 3

Hmm

### 00:15:55 · Speaker 3

generally I have seen in in some of the UI kits if I can say like in in React bootstrap or in material UI we see a lot of

### 00:16:04 · Speaker 2

material

### 00:16:07 · Speaker 3

rows and then columns and then table so we create a parent table and inside that we create a row and then inside it we create a column. This is a real example.

### 00:16:13 · Speaker 1

then

### 00:16:15 · Speaker 1

Correct

### 00:16:18 · Speaker 1

true, true, true. What is this is a real example. More from the project point of view or something like that if you have to say, whenever we are having kind of an embedding process. Let's say one is creating the entire container and somebody will embed the things inside that. Correct? For example, some cards or some shopping related items. So the one who create a container, he doesn't bother. Who will come tomorrow and insert the things? He will only worry about the containers. So that with the help of compositions, we can allow that. Like if you don't pass anything, I'll render this. If you wish to pass something, you can pass. So just make sure my

### 00:16:44 · Speaker 3

one pass

### 00:16:48 · Speaker 1

doesn't break. Correct? Good Deepak. Can you please open JS Fiddle and Yeah just one one

### 00:16:50 · Speaker 3

good

### 00:16:53 · Speaker 3

Yeah, just one example I remembered is of accordion. Yeah. So accordion can be a parent one and inside accordion we have different panels. Yeah. And accordion itself takes care of whichever panel is open or closed. Exactly. So

### 00:16:56 · Speaker 1

recording

### 00:16:57 · Speaker 1

Yeah

### 00:17:04 · Speaker 1

Yeah

### 00:17:09 · Speaker 1

closed. Exactly. So, Yes, yes Deepak, correct. Yeah, can you please open GS Fidel and present your screen?

### 00:17:16 · Speaker 3

Yeah

### 00:17:16 · Speaker 2

just one second

### 00:17:17 · Speaker 1

Achha

### 00:17:37 · Speaker 2

Hello

### 00:17:43 · Speaker 2

Sharing

### 00:17:44 · Speaker 3

screen. Sure.

### 00:17:51 · Speaker 3

it's actually giving me error that I'm not the host that's why I can't show you

### 00:17:57 · Speaker 1

हां, वन सेकंड, वन सेकंड, लेट मी गिव यू परमिशन। हां, कैन यू ट्राई नाउ?

### 00:18:08 · Speaker 1

Zoom has added a lot of securities last year after the breach, right? Zoom has made it so so complicated to join.

### 00:18:12 · Speaker 2

has made it

### 00:18:19 · Speaker 2

Alright. uh Share.

### 00:18:23 · Speaker 1

Yes, I can see your screen. Okay? So, I'm presenting, I'm sharing a code snippet in the Zoom chat. Please copy the snippet and paste that in the JavaScript editor. Don't run the code. Okay?

### 00:18:42 · Speaker 2

Hmm

### 00:18:47 · Speaker 1

Can you zoom in a bit so that me and the audience can see it much better?

### 00:18:53 · Speaker 1

yeah, maybe two more, two more times.

### 00:18:58 · Speaker 1

last one more. one more. Yes, sorry. Now better. Please guess the output, Deepak. You can take two minutes and try to guess the output.

### 00:18:59 · Speaker 3

Modern

### 00:19:07 · Speaker 1

sorry to disturb you in the middle. So in case if you're enjoying the session like how Deepak is answering and how I'm asking the question, please like the video and comment whatever you feel. Like are you liking the mock interview or this could have been improved further. Please add your comment. By more likes and comment I get more impressions. More impression means more people have a chance of watching my video. When more people watch obviously the channel becomes popular and I'll be able to reach a lot of people. So please like and comment about the video and continue watching further. Thank you so much.

### 00:19:38 · Speaker 2

we have a function here, we have a object, object length and we have this function

### 00:19:48 · Speaker 2

outermost of zero and then we are calling it

### 00:19:55 · Speaker 2

So we are calling object dot method

### 00:20:00 · Speaker 2

method inside this method we are passing f n to this f n and we call this f n

### 00:20:11 · Speaker 3

Okay

### 00:20:13 · Speaker 2

this is called using this object so here this will be pointing to this object

### 00:20:21 · Speaker 2

So the length here length here could I think it should be five because this might be pointing to object

### 00:20:33 · Speaker 2

Okay

### 00:20:36 · Speaker 2

Oh

### 00:20:38 · Speaker 2

and then here we have arguments of zero and then we are calling it

### 00:20:44 · Speaker 2

we are calling that function

### 00:20:48 · Speaker 2

from here.

### 00:20:51 · Speaker 2

and

### 00:20:54 · Speaker 2

inside we don't have this and here I

### 00:20:59 · Speaker 2

should give

### 00:21:02 · Speaker 2

and

### 00:21:04 · Speaker 3

I've quickly done it. I'll try to explain my thought process what I First first confirm

### 00:21:10 · Speaker 1

first first confirm the output yeah first confirm what will be the output

### 00:21:14 · Speaker 3

Okay. So for

### 00:21:16 · Speaker 2

for this first call

### 00:21:18 · Speaker 1

Yeah

### 00:21:20 · Speaker 2

um

### 00:21:23 · Speaker 2

passing the function. So inside this we are calling from here.

### 00:21:29 · Speaker 2

Hmm

### 00:21:34 · Speaker 2

here we

### 00:21:38 · Speaker 2

which don't have anything.

### 00:21:41 · Speaker 2

but by default it will be where it is being called. So it's being called from here so this will be fine.

### 00:21:51 · Speaker 2

this

### 00:21:54 · Speaker 2

This is again being called from here only. Not from the event.

### 00:22:04 · Speaker 2

and inside this, this is pointing to this object.

### 00:22:09 · Speaker 2

ஓகே

### 00:22:12 · Speaker 3

this will also be fine. Yeah, so I think

### 00:22:17 · Speaker 3

this should return, yeah, yeah, this will return five and this will also return five, but I might be wrong.

### 00:22:17 · Speaker 1

I am

### 00:22:24 · Speaker 1

Sure, top left, you see a run icon, please click.

### 00:22:28 · Speaker 1

Top Left

### 00:22:30 · Speaker 3

extreme

### 00:22:32 · Speaker 1

extreme left, extreme left.

### 00:22:35 · Speaker 1

top se left near the URL.

### 00:22:37 · Speaker 3

Oh yeah

### 00:22:38 · Speaker 3

Yeah, this one?

### 00:22:39 · Speaker 1

Yes, yes, please.

### 00:22:43 · Speaker 1

Yeah, so you're seeing the in bottom right, you're seeing the output.

### 00:22:47 · Speaker 3

ten and then two

### 00:22:49 · Speaker 1

any idea? Why turn into? You can try take a minute and try to deduce.

### 00:22:57 · Speaker 3

So ten I understand. uh like this is returning ten. Yes. So what this means is this this here is pointing to window actually. I was thinking that it's pointing to this object but this is pointing to window and uh the length variable is coming from the

### 00:23:02 · Speaker 1

Yes

### 00:23:07 · Speaker 2

Hmm

### 00:23:12 · Speaker 1

Hmm

### 00:23:16 · Speaker 3

parent window object

### 00:23:16 · Speaker 1

Hmm

### 00:23:18 · Speaker 1

Hmm hmm

### 00:23:21 · Speaker 3

and for this

### 00:23:21 · Speaker 1

for this

### 00:23:24 · Speaker 3

Was that right one?

### 00:23:26 · Speaker 1

Yeah, that is correct. Yes, what you're saying is right. Yeah. Basically, it doesn't take objects reference because you're calling a function which is completely external. Let's say there is a method inside the object, like a method two, which has a function and that you are invoking. That time it will look for the reference in the object, correct? So now you're calling somewhere something altogether external function. So there is nothing of this objects, this you are not passing. So there this points to window, okay? Any idea why two is printing?

### 00:23:30 · Speaker 3

doesn't take

### 00:23:34 · Speaker 3

Amethyl

### 00:23:50 · Speaker 2

step

### 00:23:55 · Speaker 2

Yeah, so this one is interesting. So we have F N. What it's saying is we have two arguments passed to this.

### 00:24:03 · Speaker 1

Hmm

### 00:24:05 · Speaker 2

it's saying arguments of zero and invoking it.

### 00:24:07 · Speaker 1

and

### 00:24:08 · Speaker 1

Hmm

### 00:24:10 · Speaker 2

arguments of zero we see that it's F N.

### 00:24:12 · Speaker 1

Correct

### 00:24:13 · Speaker 2

F N is called

### 00:24:18 · Speaker 3

No

### 00:24:20 · Speaker 2

F M is called

### 00:24:21 · Speaker 3

Okay

### 00:24:22 · Speaker 2

this way.

### 00:24:24 · Speaker 3

Okay. So here what I see is this might be referring to that function.

### 00:24:31 · Speaker 2

Hmm

### 00:24:31 · Speaker 3

to

### 00:24:33 · Speaker 2

Hmm

### 00:24:34 · Speaker 3

Yeah, this might

### 00:24:37 · Speaker 3

referring to

### 00:24:40 · Speaker 2

Oh

### 00:24:42 · Speaker 2

arguments of zero is an F N and F N is this.

### 00:24:50 · Speaker 2

and

### 00:24:52 · Speaker 2

when this function is called, it's saying this function's length.

### 00:25:02 · Speaker 2

Hmm

### 00:25:04 · Speaker 3

what what I can guess right now I'm not sure I'm right or wrong but I think in this case this is pointing to the function

### 00:25:16 · Speaker 1

Okay, function as in the one that you're passing in line number fourteen, correct? The function that you're passing in line number fourteen is which is on line number two.

### 00:25:24 · Speaker 1

Correct?

### 00:25:26 · Speaker 2

Yeah. I mean,

### 00:25:27 · Speaker 1

I mean that is how two can come

### 00:25:30 · Speaker 2

Hmm

### 00:25:31 · Speaker 1

Do one thing, in line number fourteen, after function comma one, add comma two.

### 00:25:36 · Speaker 1

Line number 14

### 00:25:38 · Speaker 2

Hmm

### 00:25:40 · Speaker 1

after one, yeah, one comma two. Please run.

### 00:25:48 · Speaker 1

Now you get a sense. Correct?

### 00:25:48 · Speaker 3

correct? Yeah. So this is the method which is being passed.

### 00:25:54 · Speaker 1

Hmm

### 00:25:56 · Speaker 1

No, no, object.method is in line number eight. That only you are calling. Okay. So now how two became three? You got a sense, right? How two is two turned into three?

### 00:25:56 · Speaker 3

projector method

### 00:26:00 · Speaker 3

Now how

### 00:26:07 · Speaker 3

this is actually the arguments array

### 00:26:10 · Speaker 1

You got it. Yes. So that's that's what I say maybe even if we work with JavaScript our whole life not that you couldn't get none of us will be able to master it I'm thinking. There will be somewhere or the other edge case where we all miss. Okay? Good. I'll I'll share one last snippet with you. Okay? So that will

### 00:26:12 · Speaker 3

that

### 00:26:34 · Speaker 1

one moment I'll share

### 00:26:44 · Speaker 1

Can you just copy the snippet and paste there?

### 00:26:48 · Speaker 1

Again you do please don't run.

### 00:26:51 · Speaker 3

Yep. I can remove this.

### 00:26:53 · Speaker 1

Yeah, yeah, please remove.

### 00:26:57 · Speaker 1

Please guess the output. Much straightforward.

### 00:27:02 · Speaker 2

so we are creating a function self invoking it. So, I'm going to found here. So we'll get one first of all. Then

### 00:27:16 · Speaker 2

four straight away

### 00:27:20 · Speaker 3

then these two will go in Q.

### 00:27:25 · Speaker 3

as this is having both are set timeout

### 00:27:29 · Speaker 3

So

### 00:27:31 · Speaker 3

put our set timeout this first one is zero so this should execute first

### 00:27:35 · Speaker 1

Hmm

### 00:27:36 · Speaker 3

then to that is after one second.

### 00:27:39 · Speaker 1

Sure. Please run. Yeah, yeah.

### 00:27:40 · Speaker 3

Please run

### 00:27:42 · Speaker 3

hmm

### 00:27:42 · Speaker 1

you're confident? This is the order?

### 00:27:43 · Speaker 3

That's

### 00:27:44 · Speaker 3

order. Yeah, I think I don't see any tricky thing here.

### 00:27:47 · Speaker 1

Please run, Please run, top left.

### 00:27:53 · Speaker 1

So one four three two, correct? Let's do this. In line number four, whatever you have four, line number four, set timeout is taking basically a function, right? Can you convert that into a self-invoking function?

### 00:27:55 · Speaker 3

Yep

### 00:28:05 · Speaker 2

Alright. So

### 00:28:09 · Speaker 2

this way

### 00:28:10 · Speaker 1

Yes, so you have to add one more brackets in the starting and the end.

### 00:28:14 · Speaker 2

Oh yeah

### 00:28:18 · Speaker 1

Yeah. Now can you guess the output?

### 00:28:26 · Speaker 3

So basically this will be invoked immediately

### 00:28:28 · Speaker 2

Hmm

### 00:28:29 · Speaker 1

Hmm

### 00:28:29 · Speaker 3

So the

### 00:28:34 · Speaker 3

So we'll have one as previous and then

### 00:28:39 · Speaker 3

this will be immediately executed.

### 00:28:42 · Speaker 1

Hmm

### 00:28:43 · Speaker 3

So this will give you S three

### 00:28:44 · Speaker 1

hum

### 00:28:46 · Speaker 3

then we'll have four and then we'll have two.

### 00:28:49 · Speaker 1

Yeah. Please explain why that will be immediately executed.

### 00:28:54 · Speaker 3

Yeah, so we what we have done is this part is creating a function and these two parenthesis are immediately executing that function.

### 00:29:04 · Speaker 1

Sure, as per event loop concept what should happen whenever set timeout is encountered?

### 00:29:05 · Speaker 3

Sorry

### 00:29:11 · Speaker 3

I miss that. Can you repeat it?

### 00:29:13 · Speaker 1

As per event loop concept, whenever a set timeout is encountered, what should the JavaScript engine do? Will it take it from call stack and move somewhere else or what is the process?

### 00:29:20 · Speaker 3

call

### 00:29:24 · Speaker 3

Yeah, so whenever set timeout is encountered,

### 00:29:28 · Speaker 1

Yeah

### 00:29:28 · Speaker 3

and whatever function is provided

### 00:29:30 · Speaker 1

Hmm

### 00:29:31 · Speaker 3

that set timeout executes but this callback is moved into an queue. And uh it's a it's a queue in which uh which will wait for this particular time to complete and then uh it the event loop will check if this if the call execution stack is empty or not. If it's empty then it will bring that pending callback into the stack and that will be executed.

### 00:29:36 · Speaker 2

Hmm

### 00:29:46 · Speaker 2

Hmm

### 00:30:00 · Speaker 1

Correct. So now in this case set timeout is there inside that there is a self invoking function, correct? How come the function will execute immediately?

### 00:30:10 · Speaker 1

It cannot directly into call stack, right? It cannot directly take into call stack as per the explanation. Correct?

### 00:30:10 · Speaker 3

Yeah, direct

### 00:30:17 · Speaker 3

Yes. So, uh what I see here is, uh like in in the difference between line number three and four is that this is a reference to a function. Consider it as a callback. Got it. But this is actually executed immediately.

### 00:30:28 · Speaker 1

Hmm

### 00:30:30 · Speaker 1

Got it

### 00:30:34 · Speaker 1

Hmm. Got it.

### 00:30:35 · Speaker 3

So, Sure.

### 00:30:37 · Speaker 1

Sure. So, in line number four, instead of zero, make it three second.

### 00:30:42 · Speaker 1

three double zero three second. Okay.

### 00:30:45 · Speaker 1

Yeah, I'm not asking the output. In this case now, after three seconds, something has to happen. What will happen?

### 00:30:52 · Speaker 1

So will a set timeout to be registered or not? That you tell me.

### 00:30:53 · Speaker 2

amount to get it

### 00:30:56 · Speaker 2

Okay

### 00:31:00 · Speaker 3

Hmm

### 00:31:03 · Speaker 3

So this is a function and it's returned. So the output of this expression would be undefined actually. Correct. And what what what set timeout will be receiving is basically once this is executed it will be receiving undefined or void as we can say.

### 00:31:09 · Speaker 1

correct

### 00:31:18 · Speaker 1

Got it

### 00:31:19 · Speaker 3

and

### 00:31:21 · Speaker 3

uh so there is a chance that it might check that if undefined is passed as a call back to set timeout then it won't do anything

### 00:31:28 · Speaker 1

set time

### 00:31:29 · Speaker 1

then it

### 00:31:31 · Speaker 1

True, true. Correct. What you said is absolutely right, Deepak. Okay. Many get confused in this process. First of all, many will not be able to guess the output only, the order of. Even if they're able to guess the order, whenever a self-invoking function comes, they get confused. Okay. Even after self-invoking function, whenever this undefined kind of a concepts come, they further get confused. You are able to answer all the things well. Can you stop sharing?

### 00:31:53 · Speaker 2

there.

### 00:31:53 · Speaker 1

Okay

### 00:31:55 · Speaker 2

Hello

### 00:31:59 · Speaker 2

Shruti

### 00:32:01 · Speaker 1

ओके. या दीपक, सो वी आई मीन, आई डिड नॉट गेट टू नो हाउ द टाइम फ्ली, वी ऑलमोस्ट फिनिश्ड हाफ एन आवर ऑलरेडी, ओके? सो फर्स्ट प्लीज फील फ्री टू आस्क मी दीपक इफ यू हैव एनी क्वेश्चंस फॉर मी.

### 00:32:02 · Speaker 2

Okay

### 00:32:09 · Speaker 2

So

### 00:32:14 · Speaker 2

Hmm

### 00:32:16 · Speaker 1

not specifically from interview if you have any other questions also generally also you can ask.

### 00:32:22 · Speaker 3

um

### 00:32:26 · Speaker 3

I don't have any question right now

### 00:32:27 · Speaker 1

Good

### 00:32:28 · Speaker 1

Sure, Sure Deepak

### 00:32:29 · Speaker 3

Uh, yeah.

### 00:32:31 · Speaker 1

Yes. Good good Deepak. I I'll just give pass on my feedback Deepak. Every viewer also got my feedback. I don't have to explicitly say it. uh I mean it was a very clean neat interview. Not just the mock interview that I take for the channel. Overall in my interview process very few will have very in-depth knowledge. Okay? And I think you will also be taking interviews for a lot of candidates. We there is a concept of breadth and depth. Where people touch upon a lot of topics and they get in whenever they feel candidate might not be confident. Okay? With my breadth and depth whatever I applied with you have

### 00:33:01 · Speaker 1

good amount of knowledge on all the concepts. Okay? Like a first thing always I see is the technical communication. Communication is one thing. Technical communication is very very important, correct? Let's say when I ask you function currying, you you should you do not say like I'll type and explain, correct? Because as a developer our job is not just the coding. We you should be able to articulate our thoughts to lot of folks, correct? So the technical communication part is very very good. And the second part is the conceptual knowledge. This is something that you applaud in an engineer after a point,

### 00:33:31 · Speaker 1

senior engineer like you, eight year, ten year, whenever some concepts come, they should be able to articulate it well. I mean, explain the with help of concept. Like the pure component example which I might have asked. Like you're passing a function, you're passing an object, you clearly know what is happening under the hood. That is something that will give a respect to engineer after a point, correct? Just because if somebody becomes an architect, people will not respect. Only because he has that kind of a knowledge, then only people respect. So fundamental knowledge is very, very good. Third point is the the guessing the output. The way

### 00:34:01 · Speaker 1

snippet driven thing. So first you were able unable to answer, I mean partially you were right, second you were able to answer clearly, okay? First question uh with my experience, I haven't seen anyone answering in the first go including me, okay? It's not straightforward. I mean obviously I I also don't say it is something with that we can judge an engineer, but it also depends on how depth you have understood. That's the only thing. Uh just because somebody says one, guess the output wrong, that doesn't mean they are bad, right? But only thing we just try to uh evaluate how depth they are able to understand.

### 00:34:22 · Speaker 3

Please

### 00:34:31 · Speaker 1

just connect between the thoughts. Only that I can tell, maybe more snippet driven questions you can solve. Rest seems to be good. I mean if you are applying for tier two and tier three are already there. Maybe if you are applying for tier one you very well know. Maybe you may have to practice if you have not done machine coding and the DSA. That's all I have to say. Any other questions you have Deepak?

### 00:34:50 · Speaker 3

No, it was it was really good to communicate with you and doing this. Yes.

### 00:34:53 · Speaker 1

Hello

### 00:34:55 · Speaker 1

Yes

### 00:34:57 · Speaker 1

Thank you

### 00:34:57 · Speaker 3

actually, actually the general thing is it's always good to listen to someone who can give a feedback to you. So I'm I'm I'm happy with that.

### 00:35:03 · Speaker 1

So

### 00:35:06 · Speaker 1

Yes, yes. Sure Deepak, like I mentioned, definitely I'll share a detailed feedback over the email. And hope you're watching Uncommon Geeks Deepak, my YouTube channel. How are you thinking? How the videos are coming?

### 00:35:06 · Speaker 3

Yes, yes.

### 00:35:17 · Speaker 3

it's good and I would say most of us with most of us what happens is we we really

### 00:35:25 · Speaker 3

we try very hard to understand things and then come up with our answers. But we we don't know where a mistake is happening and where we need to work upon. Correct. So this is and and this this very much happens when you are in an early phase when you're learning something and trying and and hustling and doing all those things. So that information is very valuable which you are passing in your

### 00:35:32 · Speaker 2

Hello

### 00:35:39 · Speaker 1

correct

### 00:35:47 · Speaker 1

Right

### 00:35:55 · Speaker 3

channel that this is something which should you should work upon and this is your thought process this should be your thought process to explain a solution to an interviewer. This is very valuable thing I'm getting from your videos.

### 00:36:06 · Speaker 1

This is

### 00:36:09 · Speaker 1

Thank you. Thank you so much Deepak. Okay.

### 00:36:12 · Speaker 1

fine Deepak then we are almost at the end of the interview. It was very nice talking to you. I mean, uh you are a senior engineer good that I could explore and I also learned a lot of things from you. Generally sometimes I get uh kind of very fast. Sometimes now now I have reduced a lot. But even before the questions are asked people try to jump in and try to answer. I had that attitude long way back. But I see you whenever you come in you are very matured. Like you wait until the question is fully asked. That is one of the very important quality in interview. You should never jump in. Correct? You should fully listen to the question because interview

### 00:36:42 · Speaker 1

at the end say I was still explaining you jumped in. Correct? So that we should have that patience and the whenever total listening skills. How the communication skills are important in the interview, listening skills are also equally important. I I that is something that I still working on and I I got to learn that from you further well. Okay. Thank you. Thank you Deepak. Very nice talking to you. Thank you. Have a good day. Bye.

### 00:37:02 · Speaker 2

Thank you

### 00:37:04 · Speaker 2

Thank you, bye.

### 00:37:06 · Speaker 1

Again welcome back. I think hope you enjoyed the interview session with Deepak. Deepak is a very senior engineer and he was able to answer all the different areas that I asked him the question whether it is conceptual, whether it is technical communication or whether it is the problem solving depending on the simple things that but he was absolutely on top notch. So like I mentioned him he is almost at the he could easily clear most of the tier two and tier three interviews if he appear to. So I'm very happy I could interview him as he's a senior to me as well. I learned the sense like I mentioned I was I got that

### 00:37:36 · Speaker 1

knowledge of being very calm in the interview. I I'm still trying to be more better at it. But sometimes I get quite enthu and I'll try to answer much quickly. So but Deepak was very calm throughout the interview, you might have observed him. So where he he he waited for the question to complete. He took his time, then he was trying to give a right answer. This is a strategy. Some of you who are at least in junior and mid level will have little more enthusiasm where they will not listen for the question completion. So please don't do that. Like how Deepak did properly in the

### 00:38:06 · Speaker 1

interview, please follow this method of comment compost. Okay? And if you're someone who is also looking for a free mock interview like this, okay? Please register in the Google form, which is there in the comment section. It's very obvious I'll not be able to take interview for all, but whomsoever possible I'll definitely try to take. If not now in future like whenever I need some partners for my video, I'll definitely reach out to you. I take very basic minimal details to contact you, okay? And if the form is inactive, it's an indication because somebody may watch this video after one year. If the form is inactive, it's an indication. I'm no longer taking the mock interview at that point in time.

### 00:38:36 · Speaker 1

Okay. Thank you so much for watching. If you not liked the video, please like the video, comment whatever you felt in the mock interview, was it beneficial for you, etcetera. The question that I snippets that I asked in the interview, that snippets are available in my GitHub repository. I'll try to link that in the description. Please go ahead and download the questions and practice on your own. My medium blog URL is also in the description. Please follow me on Medium. Almost every week I write a very interesting article which will be helpful for you to clear your interview in the front end domain. So please follow me on Medium and subscribe to my newsletter. Star my GitHub project so that I

### 00:39:06 · Speaker 1

okay, I'll be able to make more, add more content to my GitHub project and the project becomes visible whenever people search in the Google etcetera, okay. Thank you so much for watching, catch you in next video.
