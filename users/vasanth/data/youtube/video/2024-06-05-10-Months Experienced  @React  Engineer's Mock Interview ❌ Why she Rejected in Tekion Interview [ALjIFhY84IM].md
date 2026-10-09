---
id: ALjIFhY84IM
title: "10-Months Experienced  @React  Engineer's Mock Interview \u274C Why she Rejected\
  \ in Tekion Interview"
url: https://www.youtube.com/watch?v=ALjIFhY84IM
date: '2024-06-05'
duration: 00:28:13
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 3
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
---

# 10-Months Experienced  @React  Engineer's Mock Interview ❌ Why she Rejected in Tekion Interview


## Transcript

### 00:00:00 · Speaker 1

Paul welcome back to Keral with Vasant YouTube channel. My name is Vasant. With me today I have Shini. As you know this is an interview series where we're recording a lot of mock interview. Shini is having around nine months of overall IT industry experience. So this interview is primarily focused on fundamentals of JavaScript and React. We are going to dig deeper into a lot of concepts. So I'm not going to take a lot of time on this. But only the one thing that I would suggest is the best way to make utilize of this mock interview would be try to answer questions whenever asked to Shini and then go forward.

### 00:00:30 · Speaker 1

I ask a question to Shiny, you can pause the video, you can try to answer yourself and every answer that I'm giving wrong or if every answer that Shiny is struggling, I'm going to give all right answers to all of that at the end of the video. So please watch the video till the end or end so it will be useful for everybody. Okay. Now Shiny, if you can introduce yourself, we can get started.

### 00:00:47 · Speaker 2

Okay, so hi, my name is Shreemay and I'm currently working as a front-end developer at a mid-site startup and I have around nine to ten months years of experience months of experience in front-end development.

### 00:00:59 · Speaker 1

Wonderful wonderful Shiny what is primary textbook of yours

### 00:01:03 · Speaker 2

family stack is known

### 00:01:06 · Speaker 1

Okay so you'll

### 00:01:06 · Speaker 2

So they totally

### 00:01:07 · Speaker 1

You work on both front end and back end shiny

### 00:01:11 · Speaker 2

Mostly content sometimes it's text

### 00:01:14 · Speaker 1

It's just a

### 00:01:14 · Speaker 2

which consists of node node and express

### 00:01:16 · Speaker 1

Yes, wonderful, wonderful Shani. So can you share the screen Shani? We can get started immediately. Okay. And for audience who are not subscribed to my channel, I request you to subscribe to my channel. So I will guarantee you do not regret. Okay. This is a very simple snippet. Okay. And my question is also very simple. Let's say in line number nine, you remove the hello world and you put the count. What is going to be the output? Line number nine. Don't do it. SFS you tell, then we will make it.

### 00:01:44 · Speaker 2

Okay okay so if I replace count here

### 00:01:48 · Speaker 1

In the meanwhile

### 00:01:49 · Speaker 2

It was the phone

### 00:01:53 · Speaker 2

It would be zero when the page loads initially and when after rendering the it will become one

### 00:01:59 · Speaker 1

Okay, yeah, I got in the behind this is how it work. Let's say I run the code. I'm not gonna get a lot of differences. 0, 1, it will not become. When I run the code, I'm gonna see some value on the screen. What is that value?

### 00:02:12 · Speaker 1

Okay, please do it. Line number nine. Let's do it. Remove hello world and put the count.

### 00:02:20 · Speaker 2

Saving

### 00:02:22 · Speaker 1

I think you can refresh. Yeah. So we are seeing one. Correct, Shiny? So now you explain me what happens behind this. Whatever you started explaining, right? Please continue to that.

### 00:02:24 · Speaker 2

So we

### 00:02:32 · Speaker 2

So behind the scene how use effect and use tilt works is first of all the initial value was zero. The page got rendered with that zero value and it was it got rendered for very little time unless there was there and after that use effect got called as soon as it got rendered. So use effect made it one and that's why we can see one and since like in use effect there's a dependency array which is empty which means only this will run once after the page

### 00:03:02 · Speaker 2

is rendered that's why only one we can see

### 00:03:04 · Speaker 1

Absolutely correct. So there is a hook if you know that get executed before the use effect. You know which hook is that?

### 00:03:15 · Speaker 1

I tell the hook name you tell me whether that is right or not use layout effect you are have you heard the hook use layout effect

### 00:03:23 · Speaker 2

No honestly no I haven't heard of this

### 00:03:25 · Speaker 1

Yeah, you and the audience, if you don't know what is usually out there, please go ahead and read after the session. So now let's do a small update to this, Shani. Okay. Again, line number nine, remove the count and keep maybe again Hollowood in line number nine.

### 00:03:44 · Speaker 1

So now copy paste the use effect again line number five to seven paste it again

### 00:03:52 · Speaker 1

Okay now tell me what will be the output save it you can save it and guess the output

### 00:03:59 · Speaker 1

Nothing will change yeah

### 00:03:59 · Speaker 2

And the

### 00:04:01 · Speaker 2

See both use effects will run so probably the output should be two

### 00:04:06 · Speaker 1

Hmm okay let's leave this hello world with the again count if we can yeah comment it and keep and we can keep reusing in future

### 00:04:14 · Speaker 2

Yeah

### 00:04:16 · Speaker 1

refresh on the right side

### 00:04:17 · Speaker 2

Ready for

### 00:04:18 · Speaker 1

Yeah, yeah, just right side. Yes. So we're still getting one shiny. You can tell me why it is still one.

### 00:04:25 · Speaker 2

I suspect like the as soon as the like use effect is called both use effects will be called for sure this is for sure okay but I think the problem is with this set count like even though we are doing it on line nine it does not immediately update it update the state it takes some time that's why it's coming once so suppose we are at line number six even though it updates the to one and when it comes to 10 it's still not updated to one

### 00:04:55 · Speaker 1

Mm

### 00:04:57 · Speaker 2

It will think it's still zero that's why it is making it one

### 00:05:00 · Speaker 1

So so problem

### 00:05:00 · Speaker 2

So problem with state updating delay

### 00:05:03 · Speaker 1

Got it. Got it. Got it. Let's, let's understand a little bit in depth, Ashrini. Okay. So we have like two use effects now, correct? Use effect one and use effect two. And both the use effects will run synchronously or asynchronously, you tell me.

### 00:05:24 · Speaker 1

Got my question right

### 00:05:25 · Speaker 2

Yeah I got your question

### 00:05:31 · Speaker 2

They run synchronously like one after the other

### 00:05:35 · Speaker 1

Okay, so you're saying like line number five, whatever user effect we have that is executed first, followed by the user effect in line number nine, correct? One after another. If execution is synchronous, one after another, then definitely the count value should be two, right? In line number 10, because that is completed the execution user effect, because we are not doing any asynchronous operation, correct? So in line number 10, when it comes, the value of count should be two, like value of count should be one, so it should become two, the output of line number 10.

### 00:06:02 · Speaker 2

Yeah right

### 00:06:06 · Speaker 1

Anyways, like see, the whole purpose of asking this question is not to you also. First time when actually I'm uploading a video today, which is a first of June, around 1pm, the video is going to live. I also where I myself discovered a lot of things about user effect in the video. The first question is around this only. So a lot of asking you or and the audience to just start thinking. So it's not like if you don't know answer to this, you cannot build a good app, correct? It's just that like how we all understand the things to a level where which is comfortable enough to

### 00:06:06 · Speaker 2

It's like

### 00:06:36 · Speaker 1

correct sometimes you don't dig deeper and understand that is the reason so after the interview you and the candidates please go ahead and like understand depth i will also try to explain in the end like how probably this is working okay yeah now let's the that is how the use effect works but only one extension to this question i ask and then probably we will go to the next question let's say i want two now like by the execution of two use effects the value of count should be two do you think you can do some modification to make it two because right now though it is becoming one any modification

### 00:07:06 · Speaker 1

do you think of doing

### 00:07:08 · Speaker 2

Like here it should become one and then it should be here too. Like if I do it two then also it can be on the screen it will appear two but that's not a good way right? That's not what you're expecting. You want me to change something in this function five six seven

### 00:07:22 · Speaker 1

Yeah

### 00:07:23 · Speaker 2

Oh

### 00:07:24 · Speaker 1

Yeah either of the functions you make some correct change so that the count becomes actually two

### 00:07:32 · Speaker 2

What if I like stop the flow at line number six and force it to become one

### 00:07:38 · Speaker 1

how how you're gonna stop the execution at line number six

### 00:07:43 · Speaker 2

I think our in JavaScript helps with that

### 00:07:47 · Speaker 1

Okay you you want to make the set count operation you want to await until set timeout is done right

### 00:07:52 · Speaker 2

Yes yes yes

### 00:07:54 · Speaker 1

Actually, we came into a good segue. You tell me now, actually, how set timeout works behind the scenes, sorry, set state works behind the scenes, right? Is it a synchronous operation, a synchronous operation? How it's gonna work behind the scenes?

### 00:08:07 · Speaker 2

I think it is an asynchronous operation as we saw it was not updating the count immediately it was taking some time

### 00:08:15 · Speaker 1

So let's get into a little bit of the practical questions, Sashrani. Okay, why do you think the set state operation is synchronous and not synchronous?

### 00:08:26 · Speaker 1

In line number six, we have that, right? Line number six. Let's say, do you do one enter there after line number six, do an enter? Let's say you put a console.log here and try to log the value of count to what it's gonna be.

### 00:08:42 · Speaker 1

Divide it by zero

### 00:08:43 · Speaker 2

It won't it won't update it directly because said state is an asynchronous function every

### 00:08:48 · Speaker 1

Exactly. So what we will do is 100% right chain. I think most of audience might have experienced this because we all might have tried accessing the value of something immediately after it is set, correct? And we would not got the updated, then we would have used user effect and update it, correct? You tell me now, what is the problem? Why you think React update the states in a synchronous way, not in a synchronous way? Okay, no problem.

### 00:09:10 · Speaker 2

So obviously because of it, the agent does not want to block the main thread if he keeps on doing all the operations synchronously the main thread will be blocked it will become slow that's why asynchronous operations are done I guess

### 00:09:23 · Speaker 1

Okay, sure, sure. I'll share another small snippet with you, okay? Copy the snippet and try to paste. Very interesting snippet. I think you can carefully copy only what is required, okay?

### 00:09:36 · Speaker 2

Uh okay so if I click on the click me button uh the zero is there it will become one okay and after three seconds I will get the alert which will say

### 00:09:50 · Speaker 1

Okay, let's do click me once only click the button once.

### 00:09:54 · Speaker 2

Let me say that

### 00:09:56 · Speaker 1

So we're getting like embedded pieces and the value coming as zero, correct? Yeah. The count is one on screen, but on alert it is zero. And it's okay. You look at the snippet and tell. And if end goal is not getting the right answer, end goal is giving the right explanation for the output. Just look again and tell why zero is coming.

### 00:10:16 · Speaker 2

Maybe it's because rev it it is probably referencing the old state of

### 00:10:22 · Speaker 2

And why is it not updating it

### 00:10:25 · Speaker 1

Yeah so look at this snippet again and tell like probably why that is happening

### 00:10:31 · Speaker 1

You can click on you can close the alert click on okay hit close alert go back check again

### 00:10:42 · Speaker 2

Okay, so as we know, this is an async function. So after some time interval update the state. So it's when it entered the set timeout, set timeout, it was still zero.

### 00:10:54 · Speaker 1

Correct. Which famous property of the JavaScript is used here?

### 00:11:08 · Speaker 2

JavaScript property um

### 00:11:11 · Speaker 1

or JavaScript concept. Tell me a few JavaScript concepts that you know. One, I'll give an example like hosting, promises. Give me some more examples.

### 00:11:18 · Speaker 2

Closures

### 00:11:20 · Speaker 1

correct so you are able to guess so what is happening now now we've got to know it is happening because of closure and the previous value can you please elaborate shani

### 00:11:29 · Speaker 2

What's happening is um okay so

### 00:11:33 · Speaker 2

It is entering this set timeout and it is taking this alert is forming a closure with the count value of the parent which is still zero which is still not updated

### 00:11:42 · Speaker 1

Yeah yeah

### 00:11:45 · Speaker 2

That that is right was giving us zero

### 00:11:47 · Speaker 1

Sure. See, whenever the closure get start the execution, right? Closure is nothing but what we are forming a execution context and keeping it aside. Correct. So whenever that time is done, whatever is the callback function inside that block, that's actually executing. Correct. So no matter now by the time the three second over, even if you make count from zero to one million, that block do not know what happened. Correct. This is the same as like popular that for loop and set timeout example. Correct. Same happens this way where the count value is only whatever it.

### 00:12:17 · Speaker 1

noun at that time because of which we are getting the previous value okay now just as a little bit tickling the brain i'll ask again let's say you click the button three times now don't click tell me what will happen

### 00:12:30 · Speaker 2

If I click it three times uh instead of zero it will be

### 00:12:39 · Speaker 2

that timeout

### 00:12:41 · Speaker 2

because it's final closure with zero that timeout will probably you know give us zero three times in alert

### 00:12:49 · Speaker 1

Okay, let's do it

### 00:12:52 · Speaker 1

F click three times

### 00:13:06 · Speaker 1

zero one two right not zero now you can again look back and explain what is happening

### 00:13:06 · Speaker 2

Gives it over

### 00:13:11 · Speaker 2

Okay so I clicked the button value was zero it entered here

### 00:13:16 · Speaker 1

Mm

### 00:13:18 · Speaker 2

So set timeout of somewhere running in the background to make it to one we entered set timeout alert was shown with zero

### 00:13:24 · Speaker 1

Mm-hmm

### 00:13:26 · Speaker 2

In the meanwhile set count made it one

### 00:13:28 · Speaker 1

Perfect

### 00:13:30 · Speaker 2

Yes. Yeah. Count made it one in the meanwhile and then again button was pressed. So it formed the closure now with the value one of the count.

### 00:13:38 · Speaker 1

Correct. Correct. So basically, every time, whenever I'm pressing one handle click, multiple closures are getting not multiple every time one new closure is getting formed. Correct. The number of times you click, the number of times the closure has formed. Correct. As simple as that. So one practical question again, I'll ask.

### 00:13:55 · Speaker 1

What is the value that is returned from set timeout

### 00:14:02 · Speaker 1

Set timeout is a function, right? End of a day set timeout is a function set timeout set interval use state user if they're all functions, correct? What is the value returned from set timeout?

### 00:14:10 · Speaker 2

This alert is returned from here

### 00:14:12 · Speaker 1

Now alert is what is the callback function that's not return that is happening after three second right

### 00:14:19 · Speaker 2

that timeout okay I think it returns

### 00:14:23 · Speaker 2

timer something id timer id

### 00:14:26 · Speaker 1

Okay, so I'll ask like one last question on this particular topic and we will move forward. Let's say now every time whenever a new you are clicking a button like you told like it's going to be just zero, right? I want to basically clear the timeout if the timer already exists and I should go forward. How do you do that? Let's say click the button once. Okay, that is the timeout as you could see line number seven to nine. Correct. That timer I want to clear. And our second time whenever I click if that timer

### 00:14:56 · Speaker 1

Already there. Only when timer is not there I'm going to set the timer. If timer is not already there I'm just going to clear it.

### 00:14:58 · Speaker 2

But it's dark

### 00:15:02 · Speaker 1

How can we do that

### 00:15:04 · Speaker 2

So basically if timer is there clear it and then again set a set timer which is what you want me to do

### 00:15:09 · Speaker 1

Yes yes so every time you click like eight times

### 00:15:11 · Speaker 2

Everything alright by the way

### 00:15:15 · Speaker 1

You are actually gonna get only one alert because all the four you are cleared now. Only fifth alert is gonna actually persist, correct? All the four timeouts have been cleared. How can we do that?

### 00:15:27 · Speaker 2

Again we'll need closures here

### 00:15:29 · Speaker 1

Mm-hmm the closure already there September already there how we are gonna do yeah

### 00:15:29 · Speaker 2

The closure already there September

### 00:15:35 · Speaker 2

So what I'll do is I'll have make a timer first of all

### 00:15:40 · Speaker 2

which will be empty for now

### 00:15:42 · Speaker 1

Okay

### 00:15:42 · Speaker 2

And this is a timeout

### 00:15:46 · Speaker 2

is uh returning us a timer every time

### 00:15:49 · Speaker 1

Correct

### 00:15:51 · Speaker 2

And before this we need to see like if the timer exists just you know clear interval timer

### 00:16:02 · Speaker 2

But there's a catch we need to wrap this inside a function

### 00:16:10 · Speaker 1

Uh what

### 00:16:11 · Speaker 2

Because yeah, because this timer we need to make the count of that timer, right?

### 00:16:18 · Speaker 1

No we need to mention only one instance right we have we need only one instance of timer we don't need like multiple instance like

### 00:16:18 · Speaker 2

No we have to maintain only one instance

### 00:16:24 · Speaker 2

to maybe make and make it have global

### 00:16:28 · Speaker 1

Okay, sure. So now

### 00:16:29 · Speaker 2

But not global

### 00:16:31 · Speaker 1

Hmm okay so you made it global you clicked on handle click function now correct we're checking whether if if timer exist

### 00:16:31 · Speaker 2

I don't think so

### 00:16:39 · Speaker 1

If timer exists, you're clearing the interval. Why why for what reason clear interval function is used in line number nine?

### 00:16:48 · Speaker 2

So if already a timer is set this function helps us to clear all the it is a cleaner function for that timer it clears all the side effects of that timer

### 00:16:58 · Speaker 1

Does it have a clear interval or clear time out

### 00:16:58 · Speaker 2

Kansas is a state

### 00:17:00 · Speaker 2

I think it should be clear timeout

### 00:17:02 · Speaker 1

Okay good job

### 00:17:04 · Speaker 2

Clear interval will probably use be used for set intervals we have another function

### 00:17:10 · Speaker 1

Yes, I was setting the over. Okay, sure. So now one last question I ask, which you did not answer correctly was, what is the return value of set timeout, right? It's not a timer or anything as such. It's actually a numeric identifier.

### 00:17:25 · Speaker 2

ID unique ID unique ID of that time

### 00:17:27 · Speaker 1

numerical it returns like zero one two three etc and you're gonna clear all of them uh like actually the clear timeout will clear only that interval that particular number if you want to clear all you can just click clear uh clear all timeout then you're gonna create all the numerical identifiers okay fine um i'll share a small javascript snippet in the chat section copy the snippet and paste the snippet in the

### 00:17:54 · Speaker 1

Mm one second

### 00:17:57 · Speaker 1

Pay the simple in the other editor

### 00:17:59 · Speaker 2

Create counter one right

### 00:18:01 · Speaker 1

Exactly yes please paste the snippet on the JavaScript editor

### 00:18:07 · Speaker 1

Yeah, you can remove everything that's here and paste it. Again, don't click on run. Analyze the code carefully and I want to guess the output.

### 00:18:17 · Speaker 2

Output would be um

### 00:18:21 · Speaker 2

One two one

### 00:18:24 · Speaker 1

One two one

### 00:18:24 · Speaker 2

One two one

### 00:18:27 · Speaker 1

Yeah yeah so

### 00:18:28 · Speaker 2

So reasonably, let's just consider line number 11. We called a function create counter, which is returning a function. So counter one has a function there. Okay. And now we are calling counter one two times.

### 00:18:42 · Speaker 2

So initially count value was zero

### 00:18:46 · Speaker 1

Correct

### 00:18:47 · Speaker 2

line number 14 we came inside line number six made it one and uh uh made it one and one was returned so this line will print one okay now this count value will have one because this is uh like this count value you know it's forming a closure here again closure is used in this thing

### 00:19:12 · Speaker 1

So you just comment and type, okay, here it's the one. Second time you're invoking the same function where counter is already incremented. So you're saying two, correct? And from counter two, whenever you're trying.

### 00:19:23 · Speaker 2

it's one because again we are creating a new instance of that counter which will not have reference to the old values of count because a new instance is created so it will be one

### 00:19:32 · Speaker 1

Okay please run top center you see the run button there

### 00:19:43 · Speaker 1

whatever you told is correct shreeni okay so if you have to little dig deeper and understand so in line number 11 and line number 12 we are forming a two variables counter one and counter two correct both having a reference to create counter function itself but in line number 14 whenever you call the counter we actually the counter one is basically nothing but returning the function in line number five returning a function which has access to the outer scope because of the property of closure correct so whose value is actually initially zero so and it is

### 00:20:13 · Speaker 1

the updated count as it's a post increment not a pre increment correct so we will be incrementing and we'll be getting the value as one and then whenever we invoke it to the second time we still have the access to the count that was declared in the outer scope which is already incremented correct so putting other way the closure of one is not affecting the closure property of the another sheen

### 00:20:36 · Speaker 1

Okay sure so yeah you can you can stop we can stop sharing the shini okay

### 00:20:38 · Speaker 2

Yeah

### 00:20:42 · Speaker 2

Just a minute yeah the screen sharing stopped

### 00:20:46 · Speaker 1

yeah screen shot okay now let's discuss some practical questions training okay so let me present a whiteboard okay see now the question here would be one let's take a practical example shini well like you might have not worked on it directly but there are a lot of uh one of the common interview question is how do you basically maintain a infinite scrolling list okay in a typical social media application okay let's say you have to build a list where the list is can be

### 00:21:16 · Speaker 1

continuously scrolled. Tell me what are all things comes to your mind like what are all the problems that comes to your mind and how you're gonna solve the problems.

### 00:21:24 · Speaker 2

Okay um

### 00:21:27 · Speaker 2

Infinite scrolling means infinite content infinite content means infinite calls to the server

### 00:21:33 · Speaker 1

Correct yes

### 00:21:34 · Speaker 2

Yes. Right? Yeah. This is what comes to my mind right now. Obviously, we cannot, you know, just make it in the first go and then, you know, we have to do it on runtime. The user scrolls and on runtime, we'll probably try to make calls and bring data and display data. This is what I'm thinking of.

### 00:21:55 · Speaker 1

Okay, so just to unlock like as a basic UI, I'm drawing. Okay, let's say this is your website where this is the segment. Like let's take a typical example of Facebook where we have like the center portion, correct? So this is the portion where we would be basically just rendering the colors, correct?

### 00:21:56 · Speaker 3

It's not looking good

### 00:22:13 · Speaker 1

Uh one second

### 00:22:16 · Speaker 1

So this is the center portion I'm just drawing so this is the portion basically where we will be showing the content

### 00:22:22 · Speaker 1

So now let's say we have like multiple cards here, right? Like let's say there's one image, one video and one problem textual content and users keep scrolling, all right? So we will have like a lot of data that should be flowing in. Tell me like, uh, if you have to store so much of data, what all things comes to your mind, Shiny? How you're gonna actually store the data efficiently? Because you might know typical Instagram scrolling happens for about at least 10 to 15 minutes. By that time, we might have looked at easily like 50, 40, 50 reels.

### 00:22:52 · Speaker 1

Correct. If you start storing all the information in an array, the array becomes bulkier. What do you think should be the right way to store the information?

### 00:23:00 · Speaker 2

First of all your question is are we getting a whole data like you tell me all of the

### 00:23:04 · Speaker 1

You tell me like I'm telling I have to build a social media you should tell me what is the right way to store the data

### 00:23:10 · Speaker 2

okay yeah right so array we cannot use continuous it will take continuous memory space and you we don't know how much memory we'll you know we'll use because it's runtime so one thing coming to my mind if we can use linked list okay where you know at least continuous memory space will not be used okay so and we can have nodes with where which will help us to backtrack also so if you scroll down you can go to the previous

### 00:23:40 · Speaker 2

which you were watching so the link this would be I think ideal thing here

### 00:23:44 · Speaker 1

Sure, sure, Shiny. Okay. And I'm stopped. I'm stopped the whiteboard, Shiny. Okay. I'm mostly done from my end. Before I give feedback, if you have any questions, Shiny, regarding the interview, you can ask me.

### 00:23:58 · Speaker 2

no no major questions as such for the interview but you can tell me any one of the interesting most interesting thing you worked on in react or maybe you know like it just boggled you like oh this exists in react

### 00:24:12 · Speaker 1

So in the past, I worked on a project where it was a mobile application using React Native, which had a video call feature. Okay. So building a video call feature is very easy because nobody builds it from scratch. There are so many open source libraries or paid libraries where they give you step by step instruction to integrate it. So that portion of integrating video call is very easy, but mobile has a lot of modes. Like mobile has a, when the app is in the foreground, when the app is in the background, when the app is killed. Okay. And all the three states should happen for both Android and iOS.

### 00:24:42 · Speaker 1

So whenever you have to handle so many states, let's say your screen is locked, you cannot open your video call things because somebody need to unlock the screen, correct? So background, foreground, killed and screen locked, four states available. And all the four states need to be handled in the same way in both in case of both Android and iOS, okay? So this is around 2016 and 2017 when React Native did not have so much of documentation and not many are using it. So we have to undergo a lot of things to understand like probably how it works under the whole window.

### 00:25:12 · Speaker 1

a lot of native mobile code as well to unblock this but it took a good amount of time but end result was good we were able to achieve but probably if you do it now people do not take so much time because of jenny and so many other things it's much straightforward but back then it was something very major thing okay

### 00:25:31 · Speaker 1

Considering the time concept, I'll give my honest feedback, whatever I felt regarding the interview, right? Some you might already know. One thing that I ask you and most of the audience to look at it, like from the system design point of view, right? I know you just have nine months of experience. It's not like too much. But don't look at any system as a consumer. As you are a developer, look at every system as a developer. Let's say we are using Facebook or we are using Instagram, right? Let's look at it sometimes like how probably they might have solved this problem. Like I gave a very common example.

### 00:26:01 · Speaker 1

of book my show where book my show we render the different screen layouts like for example one one theater has more seat on the left no seat on the right we they have been just a walking path or all the seats on right or there's somewhere gap in the middle and there's sections like lower premium super premium there are some gaps in middle so to render this dynamic layout on the screen is a very tedious task correct but book my show solved it in a very simple way like only when you think from that point of view probably go and inspect their response and see how they're sending

### 00:26:31 · Speaker 1

data correct same happened with the social media question i asked so you and everybody who's watching spend time as a developer whenever looking at product like that okay that's one simple feedback another feedback she needs don't jump to answer especially when the question looks simple

### 00:26:47 · Speaker 1

This is a trick that is used by most of the interviewers to keep a very simple snippet. The second snippet where I extended the use effect, right? That snippet looks very simple and most obvious answer is two. Our mind also says like we should not say two, but we will not get a right justification for not saying it as two, correct? The two use effects that you used. So my advice is whenever you think the snippet is simple and the answer is most obvious, right? Try to just think what is an unobvious thing because interviewer is also not that dumb. He might not have given a very simple question, correct?

### 00:27:17 · Speaker 1

if again some simple question there could be some trick in that so try to decipher that and try to give the answer okay and the small feedback could be on a little bit on the analytical thinking like set interval set time out all of this right so probably working more towards it will help you to like master that uh these are all my my very basic feedback for you and whoever the audience watch and just in case for the audience who are watching all the question that i discussed are actually part of my video in the top 10 reactjs question that video i'm going to link in the comments

### 00:27:47 · Speaker 1

So this video is not going to have an extension where I'm going to answer the question that video itself answers all your doubts. Okay. Any closing thoughts, Shreene?

### 00:27:55 · Speaker 1

Hope you like the video and whatever

### 00:27:57 · Speaker 2

Yeah I just enjoyed it I got to know about so many things about use effect and set in terms

### 00:28:02 · Speaker 1

Yeah

### 00:28:03 · Speaker 1

Thank you so much thank you all the audience who watched the video if you're not already subscribed to my channel Kare Bhai Thassam please subscribe and like the video and share it with your friends if you liked it thank you so much for watching catch you in the next video

### 00:28:03 · Speaker 2

Yes thank you so much

