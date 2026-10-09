---
id: uW7MfzoD1po
title: "ReactJS & JavaScript Mock Interview |  \U0001F389 Candidate selected \U0001F389\
  \ | Mid range Engineer"
url: https://www.youtube.com/watch?v=uW7MfzoD1po
date: '2022-09-13'
duration: 00:37:25
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
---

# ReactJS & JavaScript Mock Interview |  🎉 Candidate selected 🎉 | Mid range Engineer


## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Uncommon Geeks, myself Asant. I hope you all doing well. In case if you see me first time on the internet, I'm a content creator. I help people to clear their interview. I made a lot of beautiful series in the past, which has been appreciated by many. And I thank you a lot. Finally, I have got now 1.1k subscriber. And as a fact of 1.1k subscriber, 1,100 subscribers, I'm giving a free giveaway of taking a lot of mock interviews with respect to the front end. And I've posted this in my YouTube channel and I also posted it on my LinkedIn.

### 00:00:30 · Speaker 1

good good number of registrations for the mock interview obviously i cannot take interview for all i picked few candidates where whom i can take a free mock interview and today i'm interviewing somebody called anubhu so he's i'm thinking he's in a junior to middle of an engineer who's aspiring for some premium companies okay let's see how the interview goes with

### 00:00:55 · Speaker 1

Hi Anubhav, as you know I'm Vasanth. I own a YouTube channel called Uncommon Geeks. Thanks for registering for the mock interview that I requested. So as most of you know this is as a part of my 1k subscriber I'm giving I'm taking free free few mock interviews. Thanks for the registering for same. Can I know something about you Anubhav, whatever you wish to share like what are your skill sets, what sort of interview, which companies that you are aspiring at the moment?

### 00:01:23 · Speaker 2

So I have like total four years of experience as a full stack developer and the tech stacks that I work on mostly include JavaScript, React, HTML, CSS on front end and on the back end I work usually with Node.js and the companies that I'm targeting basically I'm looking forward to join some big product based companies.

### 00:01:48 · Speaker 1

good good so that you are aspiring for big companies it is good you take some serious mock interviews like that so that you get the end-to-end preparation uh practice okay sure sure let's get started with extreme fundamentals okay so this is something that i generally ask in in the beginning of the interview so javascript is a single threaded interpreted programming language am i right or wrong

### 00:02:10 · Speaker 2

Yeah that is correct

### 00:02:12 · Speaker 1

So can you tell me what is interpretation in general

### 00:02:16 · Speaker 2

So interpretation is like one by one each line of code will get executed and then you will receive the output

### 00:02:23 · Speaker 1

Exactly, absolutely right. So can you tell me any interpreted language example other than JavaScript?

### 00:02:32 · Speaker 2

I think I'm

### 00:02:34 · Speaker 2

See

### 00:02:36 · Speaker 1

C is compiled C Java C Sharp all are compiled

### 00:02:43 · Speaker 1

problem okay so now if if javascript is interpreted line by line execution happens okay in general do you know how javascript code is executed the execution context and those things can you please elaborate

### 00:02:58 · Speaker 2

So we have this main stack wherein all the like statements that we have written in JavaScript are brought in and then we get the output basically on the terminal or browser where we want to see the output. And basically event loop is the concept terminology behind all this which helps in managing and basically allocating different tasks in different queues that we have like we have the microtask queue as well as we have a other

### 00:03:28 · Speaker 2

a queue for web APIs as well so all of this is managed like if we have promises and so it will be put in the microcast queue if we have like a web API like set timeout so it is placed in a different queue and if we have console log statements so they are directly executed with the on the stack and rest are handled asynchronously and then we get the output

### 00:03:51 · Speaker 1

Great great

### 00:03:51 · Speaker 2

Yeah

### 00:03:53 · Speaker 1

it no event event loop concept is fine i am much interested in the uh the execution context how execution context is created how javascript let's say you create a file called one dot js okay there are some functions in it and you're calling the function some operations you're doing etc correct whenever you run this javascript on the browser correct so what all operations take place can you please try explaining that

### 00:04:17 · Speaker 1

As to what happens whenever the browser encounters yeah

### 00:04:22 · Speaker 2

So like from the first instance uh like so there are like two steps in which the java javascript like handles the execution of the code the first is like it will check yeah different functions and whatever variables are there so it will try to create that context and uh from the second time it will basically go over the values and all those things and then give us the output

### 00:04:46 · Speaker 1

Exactly

### 00:04:46 · Speaker 2

It's from the high level high level

### 00:04:48 · Speaker 1

to what you said is absolute right this is a two-step execution that javascript uh takes okay so my now my question is you say interpretation is line by line execution correct so if line by line execution is happening then if the execution is happening two steps okay so they're contradicting each other correct so that's not line by execution can you justify how line by line execution happen in this two two step execution process

### 00:05:16 · Speaker 2

So I will say like it is kind of a just in time kind of compilation that basically runs behind JavaScript with which JavaScript is basically able to give us the output and

### 00:05:32 · Speaker 2

Yeah I will have to read more about it I think

### 00:05:34 · Speaker 1

No problem so you think react is a just-in-time compilation

### 00:05:40 · Speaker 2

Oh yeah, it's kind of a library of JavaScript. So it has a number of more concepts as well.

### 00:05:51 · Speaker 1

So tell me the difference between uh just in time compilation and ahead of time compilation

### 00:05:58 · Speaker 1

Also if if you know please tell me which which frame which popular framework uses ahead of uh fra ahead of time compilation

### 00:06:07 · Speaker 2

I'm not very sure of the time

### 00:06:11 · Speaker 1

No, the purpose I ask all these in the in the beginning is like these are extreme fundamentals, correct? You are able to answer most of them and wherever you think you are not so confident, please touch base on those. Okay. Now, let me ask you a few basic questions of the another other continuation of JavaScript only. Can you tell me what are closures in JavaScript?

### 00:06:31 · Speaker 2

So closures are basically kind of functions in JavaScript which helps the inner function to have like more control over the context of the outer function as well. Like you can have certain variables which you can control with the help of inner function.

### 00:06:48 · Speaker 1

It's it's uh not wrong but not fully correct do you want to rephrase Anubha

### 00:06:57 · Speaker 2

Controlling the scope I would say that is what makes more sense. And like inner functions has more access to the scope of outer functions.

### 00:07:07 · Speaker 1

correct this is fine uh what this definition is fine so basically inner function have access to the lexical environment of the outer function if there is no outer function the global itself is the outer function correct that is called closure can you tell me one practical example where you might use the closures obviously interview there are many questions people ask set timeout and all those things any practical example that you think that where closures can be used

### 00:07:39 · Speaker 2

like basic application is like um for example you want to keep the value like in a check for all the function different calls that we have for some sort of variable but like in a practical term like if it is used somewhere i will have to check upon

### 00:08:01 · Speaker 1

Sure, sure. I've created one video recently about function caching. Okay, how to cache a function with variable number of arguments. That is one the good and the efficient example of using closures. Whenever you you have time check out, obviously there are a lot of other examples to where the practically we can use the closures. Okay.

### 00:08:20 · Speaker 1

So I'll ask you just couple of questions on React, then we'll solve some snippets, okay? Tell me what is the reconciliation in React?

### 00:08:29 · Speaker 2

So reconciliation is kind of the mechanism with which like the react basically does the re-rendering. It uses certain algorithms. It compares the different because it creates a tree kind of structure like the DOM elements. We have the tree structure and the different nodes. They try to compare basically what was previously being rendered and what is the new set of structure in the virtual DOM. So they kind of compare it and then basically

### 00:08:59 · Speaker 2

renders only those certain nodes which needs to be re-rendered or which have certain amount of change

### 00:09:03 · Speaker 1

Exactly can you tell me which algorithm used for this tree comparison as you might know tree comparison very costly operation

### 00:09:10 · Speaker 1

Can you tell me which algorithm you used for this comparison

### 00:09:14 · Speaker 2

I think it is differing something like a differing

### 00:09:17 · Speaker 1

diffing is the algorithm name absolutely right okay i have one practical question sanabha okay think and answer let's say you have a plain html and javascript code written for example let's say you have just input box and a button nothing much same code is returning react as well

### 00:09:34 · Speaker 1

As React proposes the concept of reconciliation and it technically says it is faster than the plain JavaScript. So only people should basically use. You tell me whether React is faster than the vanilla JavaScript in all the scenarios or not.

### 00:09:51 · Speaker 2

So like I think there might be certain scenarios where React won't be like faster because it does some kind of unnecessary rendering at times as well depending upon the structure we have created our file like if we have a parent or child kind of thing so we have to kind of enhance it step by step and so JavaScript might have an edge at times not necessarily and we can prevent creating React components at such times.

### 00:10:23 · Speaker 1

Yeah, answer is right, but what interviewer will generally expect is you should tell an exact scenario, correct? Where JavaScript is faster than the React. Okay, please check certain scenarios. What your answer is right, but it can be only right when you justify it.

### 00:10:39 · Speaker 1

Tell me what is a higher order components in React

### 00:10:43 · Speaker 2

So higher order components they are kind of created in order to reduce the redundancy which might be there in certain kind of components that we have created and in order to prevent that effort so we create a component which has certain set of executions being handled at the higher level and we pass our component to it so that it basically doesn't alter the thing but it adds certain kind of things to that particular component that we have

### 00:11:13 · Speaker 1

Give me a practical example in above don't give me any built in examples a practical example where you created a higher order component

### 00:11:21 · Speaker 2

So I had one scenario with the ref forwarding, if I remember quickly, and basically I was using a forward ref and herein I passed it to a higher order component. I wanted, I think, to highlight some of the input boxes and for that I passed it because that is also kind of a higher order.

### 00:11:44 · Speaker 2

I'm not getting

### 00:11:47 · Speaker 1

I need more concrete and above can you please elaborate like why you needed higher order component without higher order component what problem you would have faced I mean what inefficiency you would have faced can you elaborate

### 00:12:00 · Speaker 2

So for instance, I can take an example wherein I was rendering some kind of data from an API. So there were two set of components and they were both again fetching data from the same API. So the UI varied a little bit, but the basic call, the network call was same. So in order to handle that, so a higher order component was created and then the data was fetched in

### 00:12:30 · Speaker 2

That particular component so that it could be supplied to these components.

### 00:12:34 · Speaker 1

So higher order component you use for making a network call am I right

### 00:12:39 · Speaker 2

Yeah

### 00:12:41 · Speaker 1

But rather making the same set of activity in both just the URL and other things might be changed. So you have tried creating a hierarchy component which can handle these activities. Am I right Anubhav?

### 00:12:52 · Speaker 1

So I'll ask you one simple question around this. So I got the scenario where you used, can't you just use a utility class to do this activity? Just a file which will export a function, which will obviously do post get, et cetera. And you pass the URL and the parameters in and it will return the result to you. Can't you use that approach instead of using the variable? That is also possible, correct?

### 00:13:15 · Speaker 2

Plus it would cut it

### 00:13:17 · Speaker 1

The purpose I asked this question Anubhav is every efficient technique like Hierarchical component comes with its own complexities. Hierarchical component use memo use call web anything that give you efficiency comes with its own set of a trade-off in the performance correct so it is good to use them only when required correct so I generally ask some practical scenarios many people say like Redux connect correct Redux connect is one of the most common usage of the hierarchical component but it is not something that we want to use that is inherently like you cannot avoid using it so you are using correct so

### 00:13:47 · Speaker 1

as the practical examples just around that

### 00:13:50 · Speaker 1

Now let's spend around 15 minutes and above on some snippet driven questions. Okay. I'll share link with you. Please open this link and present your screen. Okay. You can also open JS Fiddle. Can you open JS Fiddle and present your screen?

### 00:14:10 · Speaker 1

Sure can you please open now JS Fiddle

### 00:14:22 · Speaker 1

So I'm adding the question in the Zoom chat

### 00:14:25 · Speaker 1

So please open this question and add it in the JavaScript, the third window. Okay. But don't run the code.

### 00:14:49 · Speaker 1

The my expectation is can you please predict the output of it? Guess the output, you have a minute to guess.

### 00:15:50 · Speaker 1

So there are three locks basically, type of A, type of B, and type of C. All the three are undefined.

### 00:16:27 · Speaker 1

Uh type of A B C R undefined correct that's what you are saying

### 00:16:35 · Speaker 1

Top left you see a run icon. Can you please click on that and above top left run

### 00:16:41 · Speaker 1

And bottom right you see something called console beta and you click on that

### 00:16:46 · Speaker 1

And that white area you can expand. Can you expand the white area? White area.

### 00:16:56 · Speaker 1

It is not all the three are undefined. One is undefined and rest two are number. Okay. Can you try deducing? Why remaining two are numbers and above?

### 00:17:16 · Speaker 1

It's not an easy question. It's a medium to hard question only. Okay. I mean, even first time when I looked at it, I also answered all the three as undefined only. Okay. That's why I thought of putting it so that somebody else will not do that mistake.

### 00:17:34 · Speaker 1

So do you would like to guess or we'll go to the next question

### 00:17:40 · Speaker 2

Likewise

### 00:17:44 · Speaker 1

Now what and what I did not hear

### 00:17:46 · Speaker 2

Uh I said like uh yeah we can move to the next one

### 00:17:50 · Speaker 1

So so

### 00:17:55 · Speaker 1

Let me I'll share another snippet with you

### 00:18:02 · Speaker 1

Please copy the snippet and paste don't run the code

### 00:18:20 · Speaker 1

In comment the above one

### 00:18:24 · Speaker 1

Think it's the duplication line number fifteen to nineteen you can remove

### 00:18:28 · Speaker 1

Yeah yeah eleven two that yeah this is the question yes maybe can you try zooming in a bit

### 00:18:36 · Speaker 1

recorded yeah little huh this is good

### 00:18:56 · Speaker 2

No

### 00:18:58 · Speaker 2

And then both those two

### 00:19:06 · Speaker 1

Can you please run now top left

### 00:19:14 · Speaker 1

What is coming

### 00:19:24 · Speaker 1

First is it's printing world is beautiful but hello world is not printing it is getting the uncaught type error

### 00:19:32 · Speaker 1

Yeah, can you just deducing again why you're getting the type error?

### 00:20:23 · Speaker 1

Would you like to guess and about what is happening

### 00:20:33 · Speaker 1

Can you be a little louder and above I'm not clearly hearing

### 00:20:37 · Speaker 2

Yeah so I said like I think something to do with the

### 00:20:43 · Speaker 1

You want to convert var into const or let entray

### 00:20:46 · Speaker 2

Yeah I think the let's should

### 00:20:49 · Speaker 1

Please please try

### 00:21:10 · Speaker 2

No no no that will not work because uh

### 00:21:15 · Speaker 2

The call is before the definition of the

### 00:21:55 · Speaker 1

K we'll go to the next question and above or you want to still guess

### 00:22:00 · Speaker 1

No problem. See, it's a simple hosting concept. Okay. I've tried explaining very much in detail in my hosting videos. I'll share the links personally with you for audience whoever watching, I'll try to link that on the screen. You can watch the hosting videos. Okay. This is the last tip that I'll share with you. Most common one. I like asking this question. So I ask in almost all the interviews.

### 00:22:24 · Speaker 1

Please copy the snippet and paste

### 00:22:45 · Speaker 1

you get the output see i hope you are enjoying the content like how anvabhi is responding and how i'm asking the question and please like and comment about the video as you as you very well know i have a noble cause of helping people to create the interview just by liking and commenting i can reach out to more audience because the youtube will give more impressions so please like this video and comment whatever you're thinking okay that will really really help my channel thank you so much and after doing that please continue watching further

### 00:23:22 · Speaker 2

the print five five times

### 00:23:26 · Speaker 1

So prints five five times with what interval Anubha will print five at a time or there is some

### 00:23:33 · Speaker 2

I do that

### 00:23:34 · Speaker 1

One second. So you mean you run the code no delay. Immediately all the file printed or there is one second delay then the file printed or after printing all there is some delay. How is it?

### 00:23:47 · Speaker 2

There should not be delay because by the time like these things the set time would get executed the loop has like already entered

### 00:23:59 · Speaker 2

So it should be like all at once

### 00:24:02 · Speaker 2

without being

### 00:24:03 · Speaker 1

Are you sure? Can you uh just to justify why there is no delay between printing or during the beginning of printing why there is no delay? Can you justify that just that thing?

### 00:24:16 · Speaker 2

So I'm

### 00:24:25 · Speaker 1

So overall how many set timers are created on above

### 00:24:30 · Speaker 2

So uh only uh like there will be total of five only

### 00:24:35 · Speaker 1

Exactly what you said is right so five timeouts are created

### 00:24:35 · Speaker 2

What do you citizens

### 00:24:40 · Speaker 1

Each having delay of what

### 00:24:43 · Speaker 1

I mean time out of

### 00:24:45 · Speaker 2

Yeah it says uh like thousand milliseconds so one second

### 00:24:50 · Speaker 1

All the so there are five timers created with one second delay each

### 00:24:55 · Speaker 1

You're telling when you run the code there is no delay in printing

### 00:25:07 · Speaker 2

And this for Moby

### 00:25:14 · Speaker 1

Else let's come to the output part separately and both just tell me now whenever this runs right tell me what will happen like as soon as this statement is encountered how many seconds does for loop will take to execute then how set time it will step by step can you just explain no don't want to get into very depth like execution context and all the things just the basics how the things will execute probably we can take little bit of event loop and explain

### 00:25:39 · Speaker 2

Okay so uh like this is a browser APS so they will be put in a separate queue as and when the loop is iterating so they nothing will be executed until their execution is completed

### 00:25:59 · Speaker 2

So once the execution is over in that particular this delay is over like of thousand millisecond then they will be brought back to the main stack and then they will be executed.

### 00:26:12 · Speaker 1

So what you said is absolutely right and above. Okay. One, one add on question I'll ask. This is also a common question. So set timer to will it guarantees the delay whatever is given? Let's leave this case in general. Let's say three second delay is given for set timer mode. Will it for sure execute after a three second?

### 00:26:31 · Speaker 2

Uh under in this loop you meant in this loop

### 00:26:33 · Speaker 1

In general in general I'm asking not inside the for loop in general will it guarantee it will execute after that second that many seconds

### 00:26:42 · Speaker 2

Uh no I think it is not always a penalty it depends

### 00:26:48 · Speaker 1

Why it is not guaranteed can it tell a little bit

### 00:26:53 · Speaker 2

I think because of the asynchronous nature

### 00:26:58 · Speaker 1

Because only the main thread is executing things, correct? So finally, all these activities has to go to main thread when main thread is free. So though the set time out after three second elapsed, it can come to the stack, but there could be other task in the stack.

### 00:27:11 · Speaker 1

So the main thread may not be able to execute it the exact time when it was supposed to execute

### 00:27:17 · Speaker 1

that is a trade off using the set timeout please run the code zoom out and please run the code and we'll see what is the output

### 00:27:32 · Speaker 1

So you expand the that white area yeah expand the white area yeah and clear the console

### 00:27:41 · Speaker 1

Yeah run once again expand and run

### 00:27:46 · Speaker 1

I see a delay Anubha you are not seeing a delay

### 00:27:50 · Speaker 1

Second delay

### 00:27:56 · Speaker 2

Yeah there it is

### 00:27:59 · Speaker 1

Yeah, that's the reason I asked this question. People generally get confused with the delays. 5 times 5 is absolutely right. And you also mentioned there is no delay between each printing. That was also absolutely right. But there is one second delay in the beginning.

### 00:28:11 · Speaker 1

would like to guess why there is one second delay

### 00:28:12 · Speaker 2

But it's

### 00:28:21 · Speaker 1

I'll give one hint okay basically five timeouts are created almost at the same time

### 00:28:27 · Speaker 1

Core loop will take microseconds to execute.

### 00:28:33 · Speaker 1

As much as I can tell further you need I guess

### 00:28:38 · Speaker 2

By the time I think the loop executes so one of the set timer I guess gets that delay

### 00:28:47 · Speaker 1

You are right, you are close. See, this is pretty much the what I wanted to say is for loop will execute much faster. Obviously, it is not going to take one second, correct? So, but five timeouts are created in less than let's say a few microseconds or milliseconds. Let's say five millisecond is taken to execute this, it will run the loop. So, by that time already the five set timeouts are created.

### 00:29:09 · Speaker 1

High set timeouts are already created. So now at least one second has to elapse before running a faster timeout.

### 00:29:16 · Speaker 1

So that there is a delay. If for loop would have taken one second to execute this code, then what your answers gave was right. Like it will immediately execute because one second already elapsed. Since for loop is faster than whatever the set timeout interval that we have given, due to that nature, we get the initial one second delay.

### 00:29:35 · Speaker 1

So yeah, that's all about the snippet driven question that I want to ask Anubhav. Okay, so we are at almost half an hour we are finished. I do not know how the time flew. Okay, you can stop sharing.

### 00:29:50 · Speaker 1

Yeah, so Anbo, let us spend last five to ten minutes, whatever we left now on the feedback and any questions you have. First, let us start with any questions that you have. Then I'll try to give my feedback. Tell me if you have any questions, ask me.

### 00:30:05 · Speaker 2

So like I had not for these concepts like how do we prepare for machine coding round kind of like are they are these rounds very frequent or it depends on the years of experience we have or yeah

### 00:30:20 · Speaker 1

So machine coding is very common in the premium companies, probably whatever you're aspiring, like let's say Microsoft, you are aspiring or Amazon, you are aspiring, Swiggy, you are aspiring. So machine coding is mandatory in all the premium companies, whatever the big product companies we call, right? So machine coding and routing route is mandatory. So you have to prepare for machine coding interview if you're aspiring for that. But there are a lot of companies which I can tell, I can't name the companies, but there are many tier two kind of companies which don't have the machine coding route as separate.

### 00:30:50 · Speaker 1

It depends on your preparations Anubha if you are preparing for the taller one

### 00:30:55 · Speaker 1

The first few components in tier two then obviously you need to prepare for machine coding if not then probably it is not necessary

### 00:31:04 · Speaker 2

And then one more question related to data structure and algorithms. So like in general, like if you're a backend developer, so we cover like TP and all those topics as well. But as a front end or like because even if we are working on Node.js, we are more commonly referred as front end only stuff. Exactly. So what all topics we need to like lay emphasis on if we have like one or two weeks?

### 00:31:24 · Speaker 1

Exactly

### 00:31:32 · Speaker 2

time to prepare for it

### 00:31:34 · Speaker 1

So my advice is this, let's say you're preparing for companies like Apple, Google, Apple, Google, Facebook or Meta, what we call. If you're preparing for these companies, then sky's the limit. whether you're front-end developer or back-end developer they hire the generalist not specialist correct so all the topics you need to cover but in case if you're preparing i this includes amazon as well okay amazon apple facebook all these companies you have to prepare almost all the data structures but if you're preparing for some other companies with my experience like microsoft sap and this kind of

### 00:32:04 · Speaker 1

companies then probably you can limit yourself to strings arrays linked list and binary search trees there is very few occasions where these companies ask graphs or dynamic programming ready approach backtracking all these questions to a front-end developer

### 00:32:21 · Speaker 1

So where they will have a machine coding down to test your skills, right? So they will not spend lot on the data session algorithm. But obviously, my find I simple, if you are appearing for a not at all premium companies, then limit yourself to strings and arrays. If you are applying for a semi-premium, then go till the linked list. If you are applying for premium, excluding the main, okay? Excluding the main, there are a lot of premium companies. Then go till linked list and the binary search trees also. In fact, I have already made tutorials, all the linked list and linked list I have come.

### 00:32:51 · Speaker 1

word uh if you wish you can watch that i'll try to link that on screen for the audience

### 00:32:56 · Speaker 1

Any other questions regarding the interview you have any other questions or oral or

### 00:33:00 · Speaker 2

Or else that's all yeah that's all from

### 00:33:04 · Speaker 1

Sure Anubha so it was a nice interview from my side whatever I felt I'll tell

### 00:33:09 · Speaker 1

So with whatever the answer that you are giving, fundamentally you are strong, like conceptually you were able to explain very good, technical communication skills are good. So there is two things, communication and technical communication. There are many, whenever I ask what is hosting, they start writing the code, or whenever I ask closure, they start writing the code. So code writing is one part of the development, the developer job, correct? You should know how to articulate whatever you know. So in that way, you are able to technically communicate what you know.

### 00:33:37 · Speaker 1

And the react concepts also fundamentally are good. Many still don't know what is reconciliation itself. React, reconciliation, your higher order component, you are able to answer well. So conceptual knowledge, I'll give full marks. Whatever things that you can improvise that I notices, whenever I in the beginning also mentioned, there's a breadth and the depth concept in the interview, where you touch base on a lot of topics and we get into depth wherever we feel it is essential. Okay. So in the depths, I feel you need to work a little more. For example, the interpretation question that I asked. So you may have to dig a little deeper to answer.

### 00:34:07 · Speaker 1

understand what is the interpretation etc correct or example the set timeout one or the hoisting question which I asked snippet driven snippet drivers are very very common in the interview okay why because all the snippet driven question will have one tricky part obviously one tricky part will be there you need to be able to unlock it so that is the uh important part of the snippet driven questions so if but if you fundamentally become strong let's say you already know what are closures but if you spend more time and understand in depth of closure you will be able to easily answer the for loop and that set timeout what I asked correct

### 00:34:37 · Speaker 1

answer was right but i'm telling in depth so why when why in depth is necessary whenever you are applying for the tier one companies so they always look for the in depth in depth uh question in depth concepts correct because obviously they'll have problems inside which somebody who has in depth knowledge only can solve mediocre cannot solve okay that's the only feedback that i'll give like i mentioned i'll send one detailed email to you as well to which consolidates all all whatever everything that i explained

### 00:35:03 · Speaker 1

So that's all from my end Anubha it was nice talking to you okay any questions you have Anubha

### 00:35:08 · Speaker 2

I would say like it was a good experience I think it will surely help me as well in my future

### 00:35:18 · Speaker 1

Oh hope you're watching uncommon geeks uh and above my videos and other things

### 00:35:22 · Speaker 2

Yeah yeah surely I am doing that on daily basis

### 00:35:25 · Speaker 1

great, great anime. Obviously, like I always mention, if you watch, and I have 60 plus videos, obviously, if you're preparing right now, you cannot watch all the videos. But even if you watch my summary videos where I've explained React.js, complete React.js interview preparation, JavaScript, complete interview preparation, couple of those videos, if you fully watch, a lot of concepts will be clear to you. So there are around 30, 35 minute videos, 30, 35, 40 minute videos. So two videos you watch, it is hardly one hour. If you spend one hour and watch those two videos, your fundamental becomes much, much stronger. Okay, I would advise watching that.

### 00:35:57 · Speaker 1

That's all Alhamdulillah very nice talking to you have a good day then bye

### 00:36:01 · Speaker 2

Thank you

### 00:36:05 · Speaker 1

Welcome back guys, I hope you enjoyed the mock interview with Anubhav. So it was nice interview, he was able to articulate a lot of thoughts and wherever the small correction that he can do, I have already communicated that to him in the interview. And certain things that I think personally I can convey, I'll be sharing it over the email. In case if you are someone who also want a free mock interview, please suggest it in the Google form that is present in the description section. It's not like, obviously it's not like I'll be able to take interview for all, but definitely I'll keep your contact. I only ask very basic details to contact you. If not now,

### 00:36:35 · Speaker 1

in future whenever I want to do mock interviews or whenever I want someone to partner with me in the interview process definitely I'll consider your profile okay thank you so much for watching in case if you are not like the video please like the video comment whatever you felt about the the mock interview process and please subscribe to uncommon geeks this will help me a lot into spreading this thought of helping people to clear the interview and please share the information with your friends and whatever the question that the rest in the interview are present in my github repository I'm linking the github repository in the comment section you can always go and check that out and practice on your own some

### 00:37:05 · Speaker 1

questions are very tricky so please find the answer for yourself if you're still not able to find please mention that in comment section i'll try to explain why it is so okay and please follow me on medium i write a lot of medium articles i i got decent followers on medium also recently okay please follow me on medium too and uh star my github projects thank you so much for watching catch you in next video

