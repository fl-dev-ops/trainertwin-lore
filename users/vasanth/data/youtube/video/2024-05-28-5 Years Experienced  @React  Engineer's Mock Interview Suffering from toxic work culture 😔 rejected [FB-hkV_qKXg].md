---
id: FB-hkV_qKXg
title: "5 Years Experienced  @React  Engineer's Mock Interview:Suffering from toxic\
  \ work culture \U0001F614 rejected?"
url: https://www.youtube.com/watch?v=FB-hkV_qKXg
date: '2024-05-28'
duration: 00:22:58
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 3
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
---

# 5 Years Experienced  @React  Engineer's Mock Interview:Suffering from toxic work culture 😔 rejected?


## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Kedari with Wasam Tutees channel. With me I have today Sumit. As you know this is a series where we are doing a lot of mock interviews. This particular interview we are going to discuss primarily like three different levels of question. One is a scenario driven question primarily on HTML5 technology. Another one is the basics of React and another one is basics of JavaScript where Sumit will be we will be testing Sumit across different levels of his intelligence. More about Sumit I definitely Sumit only will be explaining and if you're not subscribed to my channel Kedari with Wasam Tutees channel which was previously known as uncommon gifts please subscribe to my channel

### 00:00:30 · Speaker 1

channel like the video share if you like this particular video and at the end of the video whatever sumith hasn't answered properly i'm gonna answer all the questions so support the video till the end thank you so much without wasting further time let's get started sumith over to you can you please introduce yourself

### 00:00:45 · Speaker 2

Yeah, hi, this is Sumit and I've been doing React for past five years and I'm last three and a half years I'm in one company and before that I was in one company which is has very toxic environment that's why I changed that company and and yeah I'm trying to now switch again that's why I'm preparing for this

### 00:01:12 · Speaker 1

Wonderful, wonderful. So for audience sake, I'm just saying, before you start the video, me and Sumit had a short connect. So there was a lot of toxicness he faced in his previous company. I will not take much time explaining that, but let me quickly summarize. The primary toxicness he was facing was like, uh he was just to join as a two years of experience but there were leads who are having like eight to ten years of experience they were expecting him to code like similar level of that so which was like hard to do and also whenever he's not meeting that particular expectation they were

### 00:01:42 · Speaker 1

holding him so which led sumit to go to some moment of depression and it took a lot of time to recovery so the reason i'm saying this is that there could be a lot of people among you who are also facing this type of problem so if you're facing that type of problem like my advice is like if you are facing please comment like whatever the i could help i'll help but i would highly recommend you to like leave the company unless your financial situation is extremely bad please try to switch to a different company because end of the day we have to leave this life and not getting into this toxic environment and get into

### 00:02:12 · Speaker 1

and that sort of a thing okay anything you want to add Sumit before we start the actual interview

### 00:02:16 · Speaker 2

Yeah, I just want to like advise people like if you face any kind of toxic toxic environment in your place and you are not able to cope it so just like I think the best advice is to switch the job. Yes, not just leave the job because that will do more harm if you are working in that exactly.

### 00:02:33 · Speaker 1

exactly yes yes absolutely so sumit so sumit now let us start so i have a very simple question okay so where uh how do we basically handle a real-time notification in uh in in real-time notification in a web application okay so the best example for real-time notification are like chatting systems like facebook messenger or zoom chat or uh the chat boards that are available on various different websites correct so whenever you go to b2c web application

### 00:03:03 · Speaker 1

chartboards that are available correct so let's say we have to implement that functionality where a client basically sends a message to server whenever server sends the message the client is receiving it okay i've opened the whiteboard so that audience can also resonate uh with it very very comfortably so i want you to explain an architecture something because you have a five plus years of experience if you have to implement this feature how are you going to implement audience also who are watching if you think you know an approach you can just mention the video timing and please mention and then you can see

### 00:03:33 · Speaker 1

uh hear what Sumit answer is or to you Sumit

### 00:03:37 · Speaker 2

Okay, so I've never worked with chatbots and all that, but what I can say, like what I do sometimes, do general Googling stuff, new stuff. So I think web sockets are used for to get the messages to and fro, like if this is a chatbot. So web socket, we can initialize a web socket on a URL that is given to us, and it starts talking to it. So maybe when the web socket,

### 00:04:07 · Speaker 2

has a different functions like on message or something like that whenever that messages come we will just store that data into a state whenever the state changes we can just render a new component or render the complex depending on the depending on the messages coming yeah so like that's the approach I will take

### 00:04:30 · Speaker 1

see i've drawn a diagram uh for simple starter diagram smith okay so we have a client we have a server so let's say chatbot runs here okay so now whatever you're saying is so there is a dedicated connection that has been established correct

### 00:04:35 · Speaker 2

We have a server let's say chatbot runs here okay so now

### 00:04:44 · Speaker 2

No it's a word

### 00:04:45 · Speaker 1

yes so the right way to represent it would be like using a plain line like for example or let me draw so you have a dedicated socket between the client and server correct so you have established a connection so with which you can actually client can send the data to server and server can send data

### 00:04:56 · Speaker 2

Yeah

### 00:05:02 · Speaker 2

Yes I can see

### 00:05:03 · Speaker 1

Correct. Yeah. So there are like, you know, depending on the use case, there can be like multiple things. Like, for example, let's say it's a charting application, then there'll be another client. Correct. So there'll be like another client, client two. Correct. Because you're sending a message.

### 00:05:15 · Speaker 3

Yeah

### 00:05:16 · Speaker 1

So now we are saying that this whatever the socket we have so we will have a socket connection here as well

### 00:05:16 · Speaker 3

Are you seeing this

### 00:05:23 · Speaker 2

Yeah

### 00:05:24 · Speaker 1

So we have a dedicated connection between connection one, let's say we call this connection one. Okay. So this, this particular thing is connection one and the whatever this we have is connection two.

### 00:05:37 · Speaker 1

So but both primarily interacting with server and whenever a whenever you receive a message from this this particular client

### 00:05:45 · Speaker 1

Let me just colour it

### 00:05:48 · Speaker 1

So you get a connection you get a message from

### 00:05:48 · Speaker 2

Get a connection

### 00:05:51 · Speaker 1

this client to the server and then you are gonna send this to this

### 00:05:56 · Speaker 1

And whenever they send a back you're gonna send it back immediately to here

### 00:06:02 · Speaker 1

And like you told, it's a pub sub model where the client is always waiting for something to happen. So the client will get the most updated information whenever there is a change. Basically, it will be getting that new message and we'll be showing that. Correct, Swetha?

### 00:06:16 · Speaker 2

Yeah

### 00:06:17 · Speaker 1

Can we the disadvantages of using web sockets

### 00:06:19 · Speaker 2

I think the web secrets, there can be loss of data.

### 00:06:24 · Speaker 1

No there'll not be loss of data that's not the thing

### 00:06:30 · Speaker 1

At a high level you tell me what network protocols do you think this web sockets will use or else in general tell me what are all the protocols that comes to your mind that is usually used for sharing the data. On block I'll tell one TCP is one protocol correct like that what other protocols exist.

### 00:06:44 · Speaker 2

UDP is there

### 00:06:46 · Speaker 1

Mm correct

### 00:06:46 · Speaker 2

HTTP

### 00:06:48 · Speaker 1

In this yes in this case if you have to use a protocol which protocol you will use

### 00:06:52 · Speaker 2

HTTPS cannot run because HTTP doesn't uh like it's uh it's not continuous it's not bi-directional I think

### 00:07:00 · Speaker 2

And web socket I think it uses uh TCP UDP

### 00:07:05 · Speaker 1

You're guessing Craig Smith

### 00:07:07 · Speaker 2

Yeah yeah

### 00:07:08 · Speaker 1

Sure no problem okay

### 00:07:11 · Speaker 2

So never work with web sockets and all that chat and all that

### 00:07:14 · Speaker 1

Sure sure but at your experience it's become like slightly like required or something

### 00:07:19 · Speaker 2

Mm yeah

### 00:07:20 · Speaker 1

Yeah, can you please present the screen uh with uh JS Fiddle open to me not JS Fiddle the any other React editor that is code sandbox or any editor open Thank you I'm sharing a very very simple

### 00:07:25 · Speaker 2

Yes we did

### 00:07:32 · Speaker 1

snippet with you in the chat section okay please copy the snippet not this one in the code sandbox for react copy the snippet and paste the snippet

### 00:07:45 · Speaker 1

Yeah in line number twenty remove that yeah

### 00:07:48 · Speaker 1

Okay, I think some some spaces are also copied. Can you please remove the spaces? So if you press the add item four times, what will be printed? Don't don't press. Don't don't press and tell me what will come.

### 00:07:59 · Speaker 2

I don't know

### 00:08:03 · Speaker 2

add item handle like and this will new item is the two items uh like this one for for if you press four times uh four uh four will be added four times

### 00:08:14 · Speaker 1

Okay so I press

### 00:08:16 · Speaker 2

No uh no no uh four will be the four then you again

### 00:08:24 · Speaker 2

I think four or eight times something I have to do the map again if I press

### 00:08:28 · Speaker 1

Or again if I

### 00:08:31 · Speaker 1

they're saying let's say refresh it and click on add item four times what will be shown in the list that is my question now you think and give me exact answer

### 00:08:41 · Speaker 2

One two three

### 00:08:43 · Speaker 2

Four times four

### 00:08:45 · Speaker 1

Okay, one, two, three, four times four. Am I right? Sumit. Okay. Yeah. For audience who are watching this video, you guys also please try to comment the video time duration and the output for this. Sumit answer is one, two, three, four times four, whatever your answer you mention. Sumit now just refresh there. Yes. Click there, refresh. Yeah. Click on add item four times. One, two, three, four.

### 00:09:09 · Speaker 1

What happened

### 00:09:10 · Speaker 1

You can click some more times click some more times

### 00:09:12 · Speaker 2

Uh nothing happened

### 00:09:14 · Speaker 1

Why nothing happening

### 00:09:15 · Speaker 2

If I press one time and I swipe

### 00:09:25 · Speaker 2

item.push the array will be updated new array will be set item

### 00:09:33 · Speaker 2

Then items in P

### 00:09:37 · Speaker 2

No I think nothing is happening

### 00:09:40 · Speaker 1

Can I refer the entire page please

### 00:09:41 · Speaker 2

Add a page one

### 00:09:42 · Speaker 1

Top left you see this you can click add item let's see let the code load you click on add item

### 00:09:51 · Speaker 1

One time you click two time yeah

### 00:09:53 · Speaker 2

Yeah

### 00:09:59 · Speaker 2

No it's not happening

### 00:10:01 · Speaker 1

So then whatever you're saying that is not happening Smit right

### 00:10:02 · Speaker 2

However you're saying that is not

### 00:10:05 · Speaker 2

Yeah nothing is happening

### 00:10:08 · Speaker 1

No it's not like nothing is happening what you told is not happening

### 00:10:08 · Speaker 2

Nothing really happened

### 00:10:11 · Speaker 2

Mm hmm hmm hmm

### 00:10:12 · Speaker 1

So you and audience whoever thought like one, two, three followed by four times four, you please check like why did not happen. We'll come back to this to meet if time permits. Okay. Okay. So I'll share a simple JavaScript snippet to you in the Java in the chart section. Copy this code and put in the other tab where you have opened for JavaScript, right? Again, please run the code. I'll tell when to run the code.

### 00:10:35 · Speaker 1

it and another editor javascript editor and then we will explore the output yes look at it carefully take one to two minutes guess the exact output

### 00:10:44 · Speaker 2

this is called async so async operation returns a statement function so this will have reference to result set term async operation completed console result i think undefined and then after one second

### 00:11:00 · Speaker 1

After that what will happen

### 00:11:03 · Speaker 2

After one second async operation completed

### 00:11:06 · Speaker 1

Okay, so we will we will so you run don't run don't run one second. So you run the code immediately after you run the code undefined will be printed am I right?

### 00:11:17 · Speaker 1

Okay and after the after one second a sync operation completed will be printed. Am I right Sumit?

### 00:11:26 · Speaker 3

Just wait uh set timeout is spoiled

### 00:11:32 · Speaker 3

timeout is called one second so when the set timeout called after the async operation is called or it will be called when the function is declared i think if function is declared is not the set timeout i think yeah what what i think what i said on the first time undefined then after one second

### 00:11:50 · Speaker 1

Sure please run the code now run the code

### 00:11:57 · Speaker 3

one undefined and undefined

### 00:11:59 · Speaker 1

Correct now please explain why it's undefined and followed by a sync operation completed

### 00:12:03 · Speaker 2

So when function is written, the concept what is happening here is the closure. Like if function will have reference to the inner function will have reference to their outer value. Correct.

### 00:12:14 · Speaker 1

connect

### 00:12:15 · Speaker 2

So when the function is written the console log the result uh the left result will have undefined when it is uh when raising operation will have undefined

### 00:12:22 · Speaker 1

I think the operator will have undefined that I did not get how let result will have undefined

### 00:12:26 · Speaker 2

Because the initial value of any variable which is not defined

### 00:12:31 · Speaker 1

is not undefined defined initial value of any variable is not undefined you also know that so it's correct if you think when they're at

### 00:12:32 · Speaker 2

defined itself

### 00:12:35 · Speaker 2

I think when they are executed when they are got executed then when the variables that declare when initializes will happen if the variable does not have any

### 00:12:49 · Speaker 3

value it will have undefined

### 00:12:52 · Speaker 3

And the uh let result

### 00:12:53 · Speaker 2

The result is initial

### 00:12:55 · Speaker 1

You are saying let's say you create a variable called let result and you log the value you are you saying you'll not get a reference error but you'll get undefined am I right Smith

### 00:12:55 · Speaker 3

You are saying you see

### 00:13:02 · Speaker 3

Let go, yeah, it will cut out and because it's not aware so.

### 00:13:11 · Speaker 2

So if you have that if you've declared a variable it will have this default value

### 00:13:17 · Speaker 3

undefined will be

### 00:13:18 · Speaker 1

The default value of any variable that is created in JavaScript is undefined. Can I can you say that so much?

### 00:13:23 · Speaker 3

Yeah when they are initialized

### 00:13:25 · Speaker 1

Now what is that when they initialize like if you are not initializing you just create a let result now correct

### 00:13:30 · Speaker 1

You're saying that let just declared it

### 00:13:30 · Speaker 3

Okay

### 00:13:35 · Speaker 1

And its value is undefined now

### 00:13:37 · Speaker 2

No, it's not declared and I think there's something called X context execution. So when the code is getting executed, we will now get into that.

### 00:13:45 · Speaker 1

We'll go get into that, those concepts. I'm not against, like, so with what you're saying is fine, but let's take it in very simple terms.

### 00:13:49 · Speaker 2

I would actually

### 00:13:51 · Speaker 1

You declared a variable with let so its default value can I consider like is undefined so with same goes for constant where you have to confirm

### 00:14:00 · Speaker 2

I think I'm defined yeah

### 00:14:01 · Speaker 3

Oh

### 00:14:02 · Speaker 2

Thank you

### 00:14:03 · Speaker 1

Okay

### 00:14:05 · Speaker 2

Because then whenever we declare any in console and when you try to put any have not declared and given any value its value is undefined if you console log it

### 00:14:14 · Speaker 1

Sure. So just with the extension to this example, Sumit, give me what are all the different ways with which we can ask JavaScript to execute asynchronously. Can you name few different ways?

### 00:14:27 · Speaker 1

Is it there? Correct.

### 00:14:32 · Speaker 3

Generator functions are there which I can recall

### 00:14:38 · Speaker 3

I am out just like this

### 00:14:43 · Speaker 3

That interval also is set I'm out there

### 00:14:48 · Speaker 3

Yeah that that I will I think maybe there are others but I don't know

### 00:14:53 · Speaker 1

So set timeout set interval promises and generator function these are all the primary things that you think that can make JavaScript execute asynchronously

### 00:15:01 · Speaker 3

Yeah

### 00:15:03 · Speaker 1

Sure sounds good so can you just write a small example for use memo use callback in the react editor we'll be able to write so much

### 00:15:12 · Speaker 3

Mm yeah

### 00:15:13 · Speaker 1

Yeah go there let's write it for use memo then

### 00:15:21 · Speaker 2

So this is example of use memo where you can memorize the value. So this is the concept for optimizing performance. Like if you are calculating some very big thing, like which is taking so much of time, like for the first time it takes two second to calculate. So if we render again and use that value and that value is again calculated and it takes two second, there's a waste of performance. So what we do, we use memo and memoize this value.

### 00:15:51 · Speaker 2

is never uh is not calculated again every render

### 00:15:55 · Speaker 2

And for hand and handle click we can use callback so we can

### 00:16:01 · Speaker 2

Call back

### 00:16:12 · Speaker 2

So here, what happens whenever we return the handle, this handle click function will have

### 00:16:17 · Speaker 3

Uh the f

### 00:16:18 · Speaker 2

function reference every time it will be created because the render is happening so to stop that we use use callback so that the reference is not changing with every render

### 00:16:26 · Speaker 1

Hmm good good so whenever you click on add item whenever you click on add item we are calling the handle click but whatever the reference that we already had for that function that's not basically redundant like new reference is not getting created

### 00:16:28 · Speaker 3

So

### 00:16:41 · Speaker 3

Yeah

### 00:16:42 · Speaker 1

You can stop sharing, Sumit. I'm mostly done. I'll have only one, I'll ask only one question.

### 00:16:44 · Speaker 3

End

### 00:16:47 · Speaker 1

Okay, so both use memo and use callback you explained very efficiently. My only question is if these both the functions are having so much of advantage, why can't we use them for all the functions?

### 00:16:57 · Speaker 3

I can't be also

### 00:17:01 · Speaker 2

Like it will create more of a code In the sense we have to write more code in top of more code like readability

### 00:17:10 · Speaker 1

Like more readability point of view

### 00:17:11 · Speaker 2

A core durability a point of view and I think it's a disadvantage that we have to wrap every function with let's say callback

### 00:17:21 · Speaker 1

a wrapping every function is not a disadvantage definitely code readability is a disadvantage connection back end disadvantage

### 00:17:22 · Speaker 2

Use callback

### 00:17:28 · Speaker 3

Disadvantage huh

### 00:17:29 · Speaker 1

Other than that do you think of anything so much

### 00:17:33 · Speaker 3

No I don't think so I don't uh I don't think much to my mind what's the disadvantage of Paul White maybe one thing is

### 00:17:38 · Speaker 1

Don't put my mind

### 00:17:41 · Speaker 2

Maybe one thing is that like code readability is

### 00:17:44 · Speaker 3

will have effect

### 00:17:46 · Speaker 1

Sure sure some

### 00:17:46 · Speaker 3

Uh sure something like that

### 00:17:48 · Speaker 1

Yeah Asmit I'm done from my end just before I give a feedback to you if you have any question you can ask me

### 00:17:53 · Speaker 3

Uh not like right now but okay not right now

### 00:17:57 · Speaker 1

No, no problem, Sumit. So yeah, Sumit, first of all, like on a personal note, like good that you left your toxic work culture office and your joint employment. That personally, I'm very happy for that. Now, just being very honest feedback for you, Sumit is at your experience of five plus years, right? There'll be always a scenario driven questions for you, like the one I asked, right? And luckily, front end is not having like plenty of scenario driven questions. There are quite a few and they repeat, they keep repeating, correct?

### 00:18:04 · Speaker 3

join the competition that

### 00:18:07 · Speaker 3

Just being

### 00:18:15 · Speaker 3

Mm-hmm

### 00:18:24 · Speaker 1

So I would highly advise you and all the audience who are having like five plus years of experience to get into that level where you master like this 10 to 15 major scenario driven question and any sub questions asked in that you should be able to answer. Same applies to you also. Okay. Yeah.

### 00:18:39 · Speaker 3

Yeah sure

### 00:18:40 · Speaker 1

Other than that, like quite like minor feedbacks, I like to have an analytical thinking, like the guest the output side of questions, right? You have to be very well versed to answer them. Spend more time on that. I am also writing a book actually, which will be out soon, where there are a lot of questions, such guest output side of questions. If it is out, put that in the description section. If not, like you can, there are a lot of websites and now AI tools where you can get this snippet of question and try to guess the output. So that is something I want you to practice or must, so much.

### 00:19:05 · Speaker 3

That is something I want you to practice

### 00:19:08 · Speaker 1

Okay. And yeah. And the last thing is like, never, ever get into debug mode immediately.

### 00:19:09 · Speaker 2

I don't know

### 00:19:15 · Speaker 1

This is the mistake that even I used to do in the initial time of my career, but never stopped doing that. I don't debug my code immediately when I'm not getting the desired output. Okay. I just look at the code. I try to understand it step by step. Okay. And only needed I'll debug.

### 00:19:31 · Speaker 1

That's all feedback from my interview. Do you have any closing notes

### 00:19:35 · Speaker 2

Yeah I will start like I told you like that this mock interview was kind of a push and motivation that I should start learning and more because I is I I just uh like before meeting me I said

### 00:19:47 · Speaker 2

And like I start doing three four days and five days one week like learning things and then I like out of unmotivation I just leave it and don't do anything for three four months. So this maybe this mock interview pushes me to start learning things again, relearn things, do mock interviews and practices more and brush up my skills to advanced level or to intermediate level. And yeah, I'll do that.

### 00:20:16 · Speaker 1

Thank you. Thank you so much, Sumit. Thank you all the audience who have watched the video. Thank you so much. Subscribe to my channel, carry on with us and see you in the next video. Hello, this is just an extension to a video that I already recorded with Sumit. So in this video, we are, this small extension, we are going to primarily discuss any question that Sumit has given a wrong answer and probably how to give a right answer to that. So the first thing that probably what Sumit and me we discussed was primarily around the live charting feature or real-time notification. Whatever Sumit told us, the high level, it was correct. We could use a website.

### 00:20:46 · Speaker 1

for that or we can also use other push notification services there are a lot of push notification services which can give like push notification to website with that also we could use instead of rebuilding our own web sockets from end to end we could use a push notifications service that are given by the third party okay other than that most other question that i asked swetha had given the right answer only thing that he could not give us is code snippet okay so if you want the code snippet probably i am including a lot of these code snippets in my book so if the book is live by the time you watch the video i'm going to put the link of the book in the description

### 00:21:16 · Speaker 1

you can go out and download it if not you can take a reference from this particular uh snippet that you're seeing so this is what the code that uh i had given so and i had asked like what will happen if you click the add item button four times okay so same like i'm clicking here actually nothing happening on click of the add item button so the reason for that is like why nothing happening i think most of you are aware we are trying to take the reference of the same array and we are updating it okay with this react is not getting any new things to re-render because of which when i

### 00:21:46 · Speaker 1

click on add item nothing happening so the right answer to the given question was when you click on add item nothing happens but if you want something to happen like for example you want the fourth element of the fourth element to get added to array and whenever you click fourth fifth gone so then the right way to do that is you do this where basically you create a new array okay like you every time whenever you are clicking on item so you want to get a copy of the existing array and by spreading the operator you are creating a new array and you are setting that item

### 00:22:16 · Speaker 1

that particular new array so that new reference is created whenever a new reference is created react would re-render i think you most of you are aware between the primitive types and non-primitive types whenever we have the primitive non-primitive times like object array etc you need to get a new reference for react to re-render so with which we are doing that okay so now if i click on add item you see like every time whenever i click a four because i'm pushing only one value that is four the four is getting added into the array okay very simple code snippet actually okay now

### 00:22:46 · Speaker 1

I'm sure you all like the content that I'm making with help of the mock interview if so please like this video share the video with your friend subscribe to my channel carried with me more such content thank you so much for watching catch you in the next video

