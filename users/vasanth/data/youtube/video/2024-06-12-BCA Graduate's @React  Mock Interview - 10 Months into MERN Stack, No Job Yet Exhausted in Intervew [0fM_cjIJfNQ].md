---
id: 0fM_cjIJfNQ
title: BCA Graduate's @React  Mock Interview - 10 Months into MERN Stack, No Job Yet|Exhausted
  in Intervew?
url: https://www.youtube.com/watch?v=0fM_cjIJfNQ
date: '2024-06-12'
duration: 00:22:03
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 3
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
---

# BCA Graduate's @React  Mock Interview - 10 Months into MERN Stack, No Job Yet|Exhausted in Intervew?


## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to career with Vasant YouTube channel. My name is Vasant. With me I have Vinay. So Vinay is a BCA graduate and after completing BCA he is currently spending almost 10 months in Monstack course. More about Vinay, Vinay himself will be explaining. This particular interview is going to be focused on some basic questions of JavaScript and React.js. We are also going to spend some time on solving a real React.js scenario driven question. Okay, so if any question if Vinay do not answer properly, I'm going to answer them at the end of the video. So please watch until end of the video.

### 00:00:30 · Speaker 1

for all the questions and answers and if you're not already subscribed to my channel please subscribe i'll be bringing more such good content and you don't regret it so without wasting further time let's get started when i can you pre-synthesize yourself

### 00:00:41 · Speaker 2

Yes, sir. Good morning, good afternoon, sir. My name is Vinay. I'm from Balarai. I graduated in BCA in 2023. Previously, I have done an internship in IntelliPath company as a technical research analyst, where I worked on Python, Numpy, Pandas and Matplotlib as a data analyst, and also I have tutored as a TA. And apart from that, I've been currently learning MERN stack from past eight months. I've built a lot of projects. Good.

### 00:01:11 · Speaker 2

projects and apart from that in the college I have been the head of coding club I organized events and from that my interest in coding actually picked up so that's a wonderful

### 00:01:20 · Speaker 1

Wonderful wonderful wonderful Vinay see as you told like you have been doing a mon stack this one right mon stack course so yes let me let us start with a simple scenario driven question Vinay

### 00:01:34 · Speaker 1

So let me do

### 00:01:43 · Speaker 1

So let's name this as like comment section. This is the video section.

### 00:01:52 · Speaker 1

This is the video set

### 00:01:52 · Speaker 2

Thank you

### 00:01:53 · Speaker 1

And here, I think if you have to compress it a little bit, here we will have all the suggestions, correct? Suggestions and other things.

### 00:02:04 · Speaker 1

Okay suggested videos

### 00:02:09 · Speaker 1

Okay, so now we'll start. I'll ask some very basic questions, Vinay, as you have done the module development and end event. Let's say we have to build this screen, right? Let's start by answering question one by one. Let's say you have to build this video player. How are you going to do that, Vinay?

### 00:02:14 · Speaker 2

The most common

### 00:02:25 · Speaker 2

Okay, this is a video player video section is a video player, right? Correct. Okay, now comments is fine. So firstly I'll break it down into two parts.

### 00:02:34 · Speaker 1

And now let's get to like question by question I'll ask. Let's say only let's stick to video section where you have to build a video player in a simple words. How are you going to build a video player? Please tell me.

### 00:02:46 · Speaker 2

So

### 00:02:49 · Speaker 2

Yeah. So firstly, I think I know a FM package, which allows us to render in different quality pixels, which we actually get in YouTube. Even in YouTube, actually, that is a package that is used in 480 pixel, 720 pixel, we can choose the quality section. So from using that, that will render as the quality of the video which we want. That's first thing. And apart from that, for the player, I think

### 00:03:19 · Speaker 2

we can build a player as normal like we can use uh we can create a different component and uh we we can it since video is also a set of images ultimately we can use set timeout and also render the particular component for a particular section ultimately if i would build it from the scratch i think uh the first thing that will come in my mind is breaking down the images into many parts right so let's

### 00:03:47 · Speaker 1

Now let's let's not get into that that depth vina let's say video is readily available on the server now we have to just play the video on the browser right probably how how you're gonna play you told like you're gonna build the video player on your own correct let's you have to build the video player on your own what is the first thing that you're gonna use which component or what is the thing that you'll use to build the video player

### 00:03:55 · Speaker 3

I'll help you

### 00:03:59 · Speaker 2

Excellent

### 00:04:09 · Speaker 2

First, I will just set up the utility file because I need it will be more usable for me. Quality and the play pause buttons, which we get, I'll be working on that. And apart from that, if this looks for me very gruesome, I'll be like using any import, importing a package particularly. But if it comes to building on myself, I think I'll break it down into utilities and finally use a particular useState component, which

### 00:04:39 · Speaker 2

actually break down each video for a particular second maybe in set time not set time or I think it will be a set interval which will help me to do that

### 00:04:48 · Speaker 1

Okay, sure. See, maybe I not sure whether I did not put it in the right way or not. If I have to build a video player, I would have been using the basic video tag of HTML5. Will you not use it? You'll be using it. Yes, sir.

### 00:04:58 · Speaker 2

You'll be using it yes yes of course

### 00:05:01 · Speaker 1

Yeah, because most of the things, whatever you told, comes by default with that particular video player.

### 00:05:06 · Speaker 2

Yeah, yeah. I thought like to build from the scratch, how I'll go about it.

### 00:05:12 · Speaker 1

Okay, sure. Yeah, no problem. But if we have, let's say, build, obvious thing, we all will be using the video tag itself, correct? So that's for pause, play and whatever the quality other things you told, fine.

### 00:05:18 · Speaker 2

Yes yes yes

### 00:05:23 · Speaker 1

So now we'll get into actually full stack question. Okay. As you see, we have comment section here. Correct. So in comment section, we will have like one, one master comment and to one master comment, there will be some replies.

### 00:05:23 · Speaker 2

Sorry

### 00:05:30 · Speaker 2

So comment

### 00:05:37 · Speaker 2

Can we reply here

### 00:05:38 · Speaker 1

reply here and it goes forward correct let's say somebody else can again respond to this this particular comment

### 00:05:45 · Speaker 1

See there is an important thing that happens when I for very popular videos right let's say whenever you are reading the comments itself somebody else from the world can add comment to that

### 00:05:56 · Speaker 1

let's say we have like comments 1 to 10 let's let's consider like this is comment 1 to 10 correct so from we have comments from 1 to 10 okay so now we were reading the comments let's say 10 comments are read by then a new comment got added by somebody else correct the newly added comment where to show it on top or bottom let's say you have to implement this feature because we have guaranteed to user probably we are going to show all the comments correct that's the expectation whenever

### 00:05:56 · Speaker 2

Let's say we have like

### 00:06:26 · Speaker 1

user comes to comment section he should be able to see you should not miss basically correct

### 00:06:29 · Speaker 1

So if you have to architect this as a full stack developer how are you going to handle this comment section can you please tell me

### 00:06:29 · Speaker 2

Yes well you see how to

### 00:06:39 · Speaker 2

Basically, the first thing that can be used is for a comment section, useState is common, but to call that useState continuously on its own, whenever there is a new comment added, either I'll use recursion, which will help me to do that. Apart from that, that will be set for the comment section because it's a simple function where we write a particular comment, just an input tag, and it will be calling itself. But showing the comments on the top or in the bottom, it's a...

### 00:07:03 · Speaker 1

By the way

### 00:07:09 · Speaker 2

I think I'll be showing it in the bottom because I generally as much as I have seen in YouTube, the list as always comes from the older comments or the most liked comments. So there is a particular filter for everything. So the first filter with there is no if there is no filter, I'll be showing the the most recent comment in the bottom. But as per the filters, the user can select the most liked, the most disliked.

### 00:07:39 · Speaker 2

whatever so based on the filters it can be shown

### 00:07:40 · Speaker 1

Based on the

### 00:07:42 · Speaker 1

Sure, sure, Vinay. Okay, let me stop the whiteboard. See, I know like you're just starting your career, Vinay. You're not having so much experience. The whole point of asking such questions to you or all the freshers or who are just starting their careers to give you actually perspective, correct? So whenever you look at a system after this looking at this interview, you should not look at a system like a developer. You should not look at a system like a user. You should look at a system like a developer, correct? Probably how they might have built it. So every question may not have answer because I or you have not built the UDU, correct? But definitely there'll be something.

### 00:08:12 · Speaker 1

that we could think like we can come up with our own version of YouTube right if you have to build that is the whole point of asking such questions because many would comment like Fresher you're asking like how to build YouTube the intention is this okay please share your screen Vinay we will start with some stuff

### 00:08:14 · Speaker 3

Come on

### 00:08:27 · Speaker 1

Yeah, so we know this is the snippet, a very simple and straightforward snippet. As you know, this is just a JS where we cannot run it. But I want you to like go through the snippet carefully and guess what is the output. Take a minute, look at the snippet carefully and guess the output.

### 00:08:40 · Speaker 3

So use state is declared a default value is zero and in use fact there there is a depend empty dependence here so it will run for the first time.

### 00:08:49 · Speaker 3

the in use effect okay id sent interval set count okay fine so it will take the previous count every time and it will add a plus one so but the timer it will be repeating is uh every one second it will be incrementing so yeah fine but return so clear interval is returned so it will cancel out itself i think after one second yeah so mostly the answer should be one uh but here i'll get one i guess

### 00:09:19 · Speaker 3

and then use effect if count is equal to five

### 00:09:25 · Speaker 3

Count equals five

### 00:09:28 · Speaker 3

Clear interval ID

### 00:09:30 · Speaker 3

Count dependent on count okay

### 00:09:34 · Speaker 3

This will return

### 00:09:42 · Speaker 3

okay if count equals five clear interval okay fine fine this is all fine

### 00:09:48 · Speaker 3

So, uh, yes, uh, so I think the first thing is from here, uh, the default value is zero in count. Okay. But in use effect, there is an empty dependency area and there's a set interval. So set interval repeat the same, uh, print the same value, which is inside the, uh, block. So set count will be repeated, uh, every one second. So, yes.

### 00:10:11 · Speaker 1

Yes yes

### 00:10:12 · Speaker 3

So previous count is zero so zero plus one it will count it will add up

### 00:10:16 · Speaker 1

Goodbye

### 00:10:18 · Speaker 3

But return a clear interval, this will end the interval. I think after completion of this. And yeah, if count equals five, clear interval, I believe that this should not not make any effect. Because after one second, it will print the value like count and it will end up the clear interval. So count will be only one. So I don't think this statement will actually get executed.

### 00:10:48 · Speaker 1

Hmm okay we'll dig a little deeper okay so we have a function app in line number three we have created like count set content we have kept it initialized to zero correct we have two two use effects and a second use effect line number 11 has a dependency or of count

### 00:11:06 · Speaker 1

Okay, so every time whenever the count is changing in line number six the second user file should be triggered, correct?

### 00:11:14 · Speaker 1

So obviously though it is coming into this block, correct? It may not be able to do something, but the control- The state will come-

### 00:11:20 · Speaker 3

It will come to this block, but count will never be five, so I thought it would be after.

### 00:11:24 · Speaker 1

You are saying after the set interval is done it will go to line number eight and it will clear the time interval correct

### 00:11:30 · Speaker 3

Exactly yes

### 00:11:31 · Speaker 1

So I'll ask a very fundamental question, Vinay. So if what is actually written here, when what it what does it doing? You're clearing the tempot immediately after the set interval is initialized.

### 00:11:46 · Speaker 1

Or if we go back to the more basics, the whole purpose of introducing use effect was where we could combine the lifecycle methods into one block, correct? If for example, in the component did mount and component did unmount when we had in the class component, correct? Where you, let's say you have to subscribe to an event, you would have done that in the component did mount, correct? The unsubscribing part of it was happening in the component did unmount. So though the both are actually related to each other, we are keeping them in a two different blocks, correct? Component did mount and component did unmount.

### 00:12:16 · Speaker 1

unmode so to overcome that problem actually use effect was one of the

### 00:12:20 · Speaker 3

How this effect was reacted Yes right

### 00:12:22 · Speaker 1

That's right. So to couple this together. So now you are saying line number eight written if it executes immediately after the ID, then how do I execute like if I have to do something like unsubscribing party news effect, where can I do that? Or you could you are free to negate your answer and tell what is the answer.

### 00:12:44 · Speaker 3

I think this set interval will actually continuously execute this statement for every one second but uh

### 00:12:55 · Speaker 3

Yeah, it will, but since there is a update of value in count, the count value is updated. When it comes to five, this clear interval will actually clear this interval. And finally, the value of clear interval is returned.

### 00:13:11 · Speaker 1

Okay, according to me that line number eight return whatever we have right that is executed whenever user leaves the current page componented unmount whenever unmount happening right that is the time when line number eight get executed you can correct me if I am wrong what do you think

### 00:13:11 · Speaker 3

Okay according to me that line

### 00:13:25 · Speaker 3

Yeah yeah yeah yes okay yes

### 00:13:27 · Speaker 1

Putting other way in our case where we have only one fine line number eight almost has no effect

### 00:13:33 · Speaker 3

Mm-hmm yes or

### 00:13:34 · Speaker 1

Okay, so now first the count start counter starts getting incremented, correct? In line number 13, you have a clear timeout of ID.

### 00:13:39 · Speaker 3

But

### 00:13:42 · Speaker 3

Yes

### 00:13:44 · Speaker 1

The actual output for this according to you Vinay is what because of the same number

### 00:13:47 · Speaker 3

The question number

### 00:13:49 · Speaker 1

number seven put the value of count here yeah i'm sorry put the value of count here

### 00:13:49 · Speaker 3

Because you didn't put on the badge

### 00:13:54 · Speaker 1

Because if put the count in the beginning only then it will be easy for you to guess the output so I ask you to put some sentence okay

### 00:14:02 · Speaker 1

What will be the value

### 00:14:03 · Speaker 3

Observe the end

### 00:14:06 · Speaker 3

I think it will be zero one two three four

### 00:14:10 · Speaker 1

Okay then you are clearing the timer and it stopped correct

### 00:14:13 · Speaker 3

Yes, yes

### 00:14:14 · Speaker 1

Go back to the now the code sandbox

### 00:14:21 · Speaker 1

See, snippets like this are intentionally given to an extent to confuse the candidate. What is the output we are getting?

### 00:14:31 · Speaker 1

Put the yeah put the count here

### 00:14:40 · Speaker 3

Uh okay the thing is yeah it will update the value obviously but I set all the values

### 00:14:47 · Speaker 1

Not that way in line number 13 the expectation from you was line number 13 you are able to tell it is an error

### 00:14:57 · Speaker 3

It is okay

### 00:14:59 · Speaker 1

Why it is an error?

### 00:15:03 · Speaker 3

the ID okay it got incremented the ID reference which is passed to ID variable I think that didn't uh where that was not generated actually so that is why it is saying ID is not defined

### 00:15:18 · Speaker 1

Not that way. It is simple JavaScript concept of scoping, right? Const is available only in the scope. So between line number four and nine, const ID is available. In line number 13 is not available, correct? Yeah, I'm not saying this is an easy snippet to answer for you or the audience, but I want you to answer in the next interview, okay? We should not make a silly take like this. We should not make a silly take.

### 00:15:25 · Speaker 3

Yes

### 00:15:30 · Speaker 3

Yeah

### 00:15:37 · Speaker 3

You should not make a serious take like this because you should not make a serious take

### 00:15:41 · Speaker 1

Okay, so that is the example I gave you the snippet. Now we'll solve a very interesting problem in React.js. Okay, I'm sharing the question in the chat section if you wish you could stop sharing and copy and so.

### 00:15:42 · Speaker 3

It is

### 00:15:51 · Speaker 1

add it again okay so this is a problem where i'll give you 15 minutes when i okay i wanted to solve it end to end read the question understand the question first copy paste and you can share so that audience first understand the question read the question carefully yourself an audience look at the question read it carefully can you do little zoom in as minute control plus a couple of times yes so read the question carefully understand it you and the audience both can take 15 minutes to solve the problem and if audience who are watching

### 00:16:21 · Speaker 1

If you solve the problem, please mention your GitHub URL, GST URL, or if you hosted somewhere in CodeSandbox, comment there. I'm going to personally review the code and tell whether that is right or not. Okay. Please read the question when I...

### 00:16:34 · Speaker 3

Build a traffic light where the light switch from green to yellow to red after predetermined intervals and loop indefinitely. Each light should be lit for the following durations red light four milliseconds yellow light five okay green light three mill three seconds you are free to exercise order to sell the appearance of the traffic light fine so we'll be building a traffic light where the light switch from green to yellow to red yeah after a set intervals just like they are mentioned after every four seconds

### 00:17:04 · Speaker 3

Red light will be shown each light should be lit for the following reason red light will be shown for four seconds yellow will be shown for that is five milliseconds and green light will be shown for three seconds okay

### 00:17:48 · Speaker 1

We have a last five minutes

### 00:17:48 · Speaker 3

I mean I'm not sure

### 00:18:00 · Speaker 1

We have two more minutes Vinay you think you'll be able to solve if not at least we could discuss the solution

### 00:18:07 · Speaker 3

We'll discuss the solutions later

### 00:18:09 · Speaker 1

Sure. See, considering the problem, whatever we wanted to solve in a, correct? The problem is to an extent straightforward. We have three different lights. They show that particular light for a given duration of time.

### 00:18:22 · Speaker 1

So you have created like multiple set timers which different duration

### 00:18:22 · Speaker 3

So

### 00:18:26 · Speaker 3

Yes yes what

### 00:18:27 · Speaker 1

What would have been the ideal approach you might have not implemented not a problem in the time constant if you have to implement like from the idealistic point of view what would be your implementation behind

### 00:18:36 · Speaker 3

I would s actually I was able to only think of this way to be honest

### 00:18:39 · Speaker 1

Yeah we are not you can stop sharing Vinay

### 00:18:42 · Speaker 3

I didn't even get other any other perspective as well

### 00:18:45 · Speaker 1

No problem, no problem. Like considering so far whatever the interview happened with I'm gonna give my feedback but before I give a feedback if you have any questions you can ask me.

### 00:18:57 · Speaker 3

No so I just want to know the of the entire

### 00:18:58 · Speaker 1

the result of the entire see vinay this is uh the first question was around that guessing the output on the use effect right so the intentionally such questions are asked at front fresher to a mid mid-level experienced engineer correct probably after point it may not be very relevant at your experience level it will be relevant because how you basically interpret the code correct so where the id is undefined or number of intervals number of times the count is shown etc correct so where i'm coming from is look at the snippets and try

### 00:19:28 · Speaker 1

to analyze as much as possible before giving an answer okay so putting other way if interviewer is like me where answer do not matter a lot but your explanation matter a lot let's say you would have told like the right answer let me some snippets will give you exact output right like three or four you tell three and not four my i'm not happy let's say three is the answer you told three i'm not happy i'm happy only if you give the right explanation why it is three correct it's not like where you guess the answer and i'll give you money correct the explanation

### 00:19:54 · Speaker 3

Yes

### 00:19:58 · Speaker 1

has more value there are times where people tell the wrong answer but when after looking at the right answer they amend the answer and explain like why it is even that is also fine at least they are able to interpret after looking at the output correct though it is little subsidized compared to the guessing the output of the first time but it is still better correct that is first feedback you and everybody who is watching at your level please consider this and another very important thing when i is especially whenever a machine coding question is given like the one i asked the traffic timer correct

### 00:20:25 · Speaker 1

Don't jump into solving the problem. This is not you. Even I used to do the same mistake whenever I started solving, right? Instead, break down the core logic in your mind, only then approach the problem. Okay. For example, in this particular case, how do we show a timer for a specific duration of time and do that indefinitely? That is the ask.

### 00:20:37 · Speaker 3

Component

### 00:20:45 · Speaker 1

Correct. If you are able to solve that problem, UI is a secondary. If you do UI very good, you get more marks. Even if you are not solving UI, still, if you are able to solve this problem accurately, you are going to get a good mark. You will clear the interview. Correct. So solve the crux of the problem somewhere on paper and pen or your mind only then start the implementation. Don't get started busy building the basic UI, which you anyhow can do. Got my point. So focus on this. These are my candidate feedback when I, if you have any other question, you can feel free to ask.

### 00:21:08 · Speaker 3

Yeah

### 00:21:16 · Speaker 1

Or overall how was the session Mina You felt is it useful

### 00:21:19 · Speaker 3

Yeah yes of course actually I just wanted to know right now how I'm doing because I'll be giving further interviews so I wanted to know the negatives where I can work on to be honest that was the whole point of the interview

### 00:21:25 · Speaker 1

Exactly

### 00:21:29 · Speaker 1

Exactly. That was the whole point of the interview. Exactly. Sure, Vinay. Thank you so much for that. And audience who is watching, like, I recommend everybody to act, especially if you're a fresher and you want to get started it, find somebody who is at your experience level and try to give as many mock interviews as possible. Definitely you can approach people like me or somebody else on various different mentoring, paid and free mentoring platforms. But try to pair up with someone during the interview session. That'll be very helpful for you. Okay. I'm sure you might have liked the video. If you like the video, please like the video. Share the video with your friends. It might be useful for them.

### 00:21:59 · Speaker 1

If you are not subscribed to my channel, please subscribe to my channel. Thank you so much for watching, catch you in the next video.

