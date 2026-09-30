---
id: uW7MfzoD1po
title: ReactJS & JavaScript Mock Interview | 🎉 Candidate selected 🎉 | Mid range Engineer
date: '2022-09-13'
url: https://www.youtube.com/watch?v=uW7MfzoD1po
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ #frontenddeveloper #mockinterview #uncommonGeeks \nLink for registering mock interview,\
  \ register only if your ready to publish your video on Youtube: https://forms.gle/38sNpiqrdrUrhm7MA\n\
  \nInterview Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nMedium Blog https://mevasanth.medium.com/ \n\nFollow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  \nGithub Repository that contains examples: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript/blob/main/MockInterviewQuestions/AnubhavMock.js\n\
  \nJavaScript Custom implementation introduction: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s"
author: careerwithvasanth
duration: 00:37:25
model: saaras:v3
transcript: true
---

# ReactJS & JavaScript Mock Interview | 🎉 Candidate selected 🎉 | Mid range Engineer

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Uncommon Geeks. Myself, Ashant. I hope you all doing well. In case if you're seeing me first time on the internet, I'm a content creator. I help people to clear their interview. I made a lot of beautiful series in the past which has been appreciated by many. And I thank you a lot. Finally, I have got now 1.1k subscriber. And as a fact of 1.1k subscriber, 1100 subscribers, I'm giving a free giveaway of taking a lot of mock interviews with respect to the front end. And I have posted this in my YouTube channel and I also posted it on my LinkedIn.

### 00:00:30 · Speaker 1

I've got good number of registrations for the mock interview. Obviously I cannot take interview for all. I have picked few candidates where whom I can take a free mock interview. And today I'm interviewing somebody called Anubhav. So he's I'm thinking he's in a junior to mid level engineer who is aspiring for some premium companies. Okay. Let's see how the interview goes with Anubhav.

### 00:00:54 · Speaker 1

Yeah. So, hi Anubhav. As you know I'm Vasanth. I I have I own a YouTube channel called Uncommon Geeks. Thanks for registering for the mock interview that I requested. So, as most of you know this is a as a part of my one K subscriber. I'm giving I'm taking free free few mock interviews. Thanks for registering for same. Can I know something about you Anubhav? Whatever you wish to share? Like what are your skill sets? What sort of interview? Which which companies that you are aspiring at the moment? Yeah.

### 00:01:23 · Speaker 4

So I have like total four years of experience as a full stack developer and the tech stacks that I work on mostly include JavaScript, React, HTML, CSS on front end and on the back end I work usually with Node.js. And the companies that I'm targeting basically I'm looking forward to join some big product based companies.

### 00:01:44 · Speaker 1

Good

### 00:01:45 · Speaker 3

Hospital

### 00:01:47 · Speaker 1

Yeah. Good, good. So that you are aspiring for big companies, it is good you take some serious mock interviews like that so that you get the end-to-end preparation practice, okay? Sure, sure Anubhav. Let's get started with extreme fundamentals, okay? So this is something that I generally ask in the beginning of the interview. So JavaScript is a single-threaded interpreted programming language. Am I right or wrong, Anubhav?

### 00:02:10 · Speaker 4

Yeah, that is correct.

### 00:02:11 · Speaker 1

Correct. So, can you tell me what is interpretation in general?

### 00:02:16 · Speaker 4

सो इंटरप्रिटेशन इज लाइक वन बाय वन ईच लाइन ऑफ कोड विल गेट लाइक एग्जीक्यूटेड एंड देन यू विल रिसीव द आउट।

### 00:02:23 · Speaker 1

Exactly, absolutely right. So can you tell me any interpreted language example other than JavaScript?

### 00:02:32 · Speaker 3

I think C, C was interesting, not sure.

### 00:02:36 · Speaker 1

C is compiled. C, Java, C# all are compiled.

### 00:02:40 · Speaker 3

Hmm

### 00:02:41 · Speaker 1

the program

### 00:02:42 · Speaker 3

Yeah, not able to perform.

### 00:02:43 · Speaker 1

No problem, okay? So now, if if JavaScript is interpreted, line by line execution happens, okay? In general, do you know how JavaScript code is executed, the execution context and those things? Can you please elaborate a little bit, please?

### 00:02:55 · Speaker 4

Right, yeah.

### 00:02:58 · Speaker 4

So we have this main stack wherein all the like statements that we have written in JavaScript are brought in and then we get the output basically on the terminal or browser where we want to see the output. And basically event loop is the concept terminology behind all this which helps in managing and basically allocating different tasks in different queues that we have like we have the micro task queue as well as we have a other

### 00:03:11 · Speaker 0

Yeah

### 00:03:28 · Speaker 4

a queue for web APIs as well. So all of this is managed like if we have promises and so it will be put in the micro task queue if we have like a web API like set timeout so it is placed in a different queue and if we have console log statement so they are directly executed with the on the stack and rest are handled asynchronously and then we get the output. Correct right. As when they are executed.

### 00:03:51 · Speaker 1

Correct, fine.

### 00:03:53 · Speaker 1

Correct. No, event loop concept is fine, Anubhav. I am much interested in the the execution context, how execution context is created, how JavaScript, let's say you have created a file called one dot js, okay? There are some functions in it and you are calling the function, some operations you are doing, etcetera, correct? Whenever you run this JavaScript on the browser, correct? So what all operations take place? Can you please try explaining that?

### 00:04:17 · Speaker 1

first what happens whenever the browser encounters yeah

### 00:04:18 · Speaker 0

Vartha

### 00:04:21 · Speaker 4

So like from the first instance, like so there are like two steps in which the Java JavaScript like handles the execution of the code. The first is like it will check yeah different functions and whatever variables are there so it will try to create that context and from the second time it will basically go over those values and all those things and then give us the output. Exactly. That's from a high level, high level. True, true.

### 00:04:46 · Speaker 1

Exactly

### 00:04:48 · Speaker 1

True, true, true. What you said is absolutely right. This is a two-step execution that JavaScript takes, okay? So my now my question is, you say interpretation is line-by-line execution, correct? So if line-by-line execution is happening, then if the execution is happening in two steps, okay? So they're contradicting each other, correct? So that's not line-by-line execution. Can you justify how line-by-line execution happen in this two-step execution process?

### 00:05:07 · Speaker 4

plain

### 00:05:16 · Speaker 4

I will say like it is kind of a just in time kind of compilation that basically runs behind Java like with which JavaScript is basically able to give us the output and

### 00:05:32 · Speaker 4

Yeah, I will have to read more about it, I think.

### 00:05:34 · Speaker 1

Sure, no problem. So you think React is a just-in-time compilation?

### 00:05:40 · Speaker 4

Oh yeah, it's kind of kind of a library of JavaScript. So, though it has a number of more concepts as well.

### 00:05:40 · Speaker 1

one

### 00:05:49 · Speaker 1

Got it. So tell me the difference between just in time compilation and ahead of time compilation.

### 00:05:57 · Speaker 1

Also if if you know please tell me which which frame which popular framework uses ahead of ahead of time compilation.

### 00:05:58 · Speaker 4

No

### 00:06:07 · Speaker 4

I'm not very sure of the rate of time

### 00:06:08 · Speaker 1

Hello

### 00:06:10 · Speaker 1

No problem. Okay. No, the purpose I ask all these in the in the beginning is like these are extreme fundamentals, correct? You are able to answer most of them and wherever you think you are not so confident, please touch base on those, okay? Now, let me ask you few basic questions of the another continuation of JavaScript only. Can you tell me what are closures in JavaScript?

### 00:06:10 · Speaker 4

okay

### 00:06:22 · Speaker 4

Let me

### 00:06:31 · Speaker 4

So closures are basically kind of functions in JavaScript which helps the inner function to have like more control over the context of the outer function as well like you can have certain variable which you can control with the help of inner function and

### 00:06:47 · Speaker 2

Okay

### 00:06:48 · Speaker 1

इट्स इट्स नॉट रॉन्ग बट नॉट फुल्ली करेक्ट. डू यू वांट टू रीफ्रेज़ अनुभव?

### 00:06:57 · Speaker 4

like controlling the scope I would say. That is what makes more sense. Like inner functions has more access to the scope of outer functions.

### 00:07:01 · Speaker 1

one

### 00:07:03 · Speaker 1

like in

### 00:07:06 · Speaker 1

Correct. Correct. This is fine. What this definition is fine. So basically inner function have access to the lexical environment of the outer function. If there is no outer function, the global itself is the outer function. Correct? That is called closure. Can you tell me one practical example where you might use the closures? Obviously interview there are many questions people ask, set timeout and all those things. Any practical example that you think that where closures can be used?

### 00:07:25 · Speaker 0

and all those

### 00:07:32 · Speaker 2

practical network

### 00:07:39 · Speaker 4

basic application is like for example you want to keep the value like in a check for all the function different calls that we have for some sort of variable. But like in a practical term like if it is used somewhere I will have to check upon it.

### 00:07:52 · Speaker 1

Hmm

### 00:08:00 · Speaker 1

Sure, sure. I've created one video recently about function caching, okay? How to cache a function with variable number of arguments. That is one the good and the efficient example of using closures. Whenever you you have time check out, obviously there are a lot of other examples too where the practically we can use the closures, okay? Sure. So, I'll ask you just couple of questions on React, then we'll solve some snippets, okay? Tell me what is reconciliation in React?

### 00:08:19 · Speaker 4

Hello

### 00:08:29 · Speaker 4

So reconciliation is kind of the mechanism with which like the React basically does the re-rendering. It uses certain algorithms, it compares the different because it creates a tree kind of structure like the DOM elements, we have the tree structure and the different nodes, they try to compare basically what was previously being rendered and what is the new set of structure in the virtual DOM. So they kind of compare it and then basically

### 00:08:43 · Speaker 1

one

### 00:08:44 · Speaker 1

structure

### 00:08:59 · Speaker 4

renders only those certain nodes which needs to be re-rendered or which have certain kind of change.

### 00:09:03 · Speaker 1

Exactly. Can you tell me which algorithm used for this tree comparison? As you might know tree comparison very costly operation. Correct? Can you tell me which algorithm used for this comparison?

### 00:09:10 · Speaker 4

one

### 00:09:11 · Speaker 4

Hello

### 00:09:14 · Speaker 4

I think it is diffing something, diffing

### 00:09:15 · Speaker 1

correct. Correct. Different is algorithm name. Absolutely right. Okay. I have one practical question, Anubhav. Okay. Think and answer. Let's say you have a plain HTML and JavaScript code written. For example, let's say you have just input box and a button, nothing much. Same code is written in React as well. Okay. As React proposes the concept of reconciliation and it technically says it is faster than the plain JavaScript. So only people should basically use. You tell me whether React is faster than the vanilla JavaScript. in all the scenarios or not?

### 00:09:51 · Speaker 4

So like I think there might be certain scenarios where React won't be like faster. Because it does some kind of unnecessary rendering at times as well depending upon the structure we have created our file like if we have a parent or child kind of thing. So we have to kind of enhance it step by step and so JavaScript might have an edge at times. Correct. Not necessarily. And we can prevent creating React components and such.

### 00:10:16 · Speaker 1

Correct

### 00:10:21 · Speaker 4

is

### 00:10:22 · Speaker 1

Got it. So, yeah, answer is right, but what interviewer will generally expect is you should tell a exact scenario, correct? Where JavaScript is faster than the React. Okay, please check certain scenarios. What your answer is right, but it can be only right when you justify it. Okay? Tell me what is higher order components in React?

### 00:10:43 · Speaker 4

higher order components they are kind of created in order to reduce the redundancy which might be there in certain kind of components that we have created and in order to prevent that effort so we create a component which has certain set of execution being handled at the higher level and we pass our component to it so that it basically doesn't alter the thing but it adds certain kind of things to that particular component that we are passing

### 00:11:13 · Speaker 1

सो, गिव मी वन प्रैक्टिकल एग्जांपल अनुभव. डोंट गिव मी एनी बिल्ट इन एग्जांपल्स, अ प्रैक्टिकल एग्जांपल व्हेयर यू क्रिएटेड अ हायर ऑर्डर कॉम्पोनेंट.

### 00:11:21 · Speaker 4

So I had one scenario with ref forwarding. I remember P3. And

### 00:11:25 · Speaker 1

Hmm

### 00:11:29 · Speaker 4

basically I was using forward rep and there in I passed it to a higher order component. I wanted I think to highlight some of the input boxes and for that I passed it because that is also kind of a higher order option. step forwarding and attending work.

### 00:11:43 · Speaker 1

Mm-hmm

### 00:11:47 · Speaker 1

I I need more concrete अनुभव. Can you please elaborate like why you needed higher order component? Without higher order component what problem you would have faced? I mean what inefficiency you would have faced? Can you elaborate?

### 00:12:00 · Speaker 4

So, uh, for instance, I can take an example wherein I was rendering some kind of data from an API. So there were two set of components and they were both again fetching data from the same API. Though they the UI varied a little bit, but the basic call, the network call was same. So in order to handle that, so a higher order component was created and then the data was fetched in

### 00:12:11 · Speaker 0

I

### 00:12:30 · Speaker 4

that particular component so that it could be supplied to the this components.

### 00:12:32 · Speaker 1

Okay

### 00:12:34 · Speaker 1

So higher order component you use for making a network call. Am I right?

### 00:12:39 · Speaker 4

Yeah, like that.

### 00:12:40 · Speaker 1

Got it. But rather making the same set of activity in both, just the URL and other things might be changed. So you have tried creating a higher order component which can handle these activities. Am I right Anubhav?

### 00:12:51 · Speaker 3

Right

### 00:12:52 · Speaker 1

Correct. So I'll ask you one simple question around this. So

### 00:12:56 · Speaker 1

I got the scenario where you used. Can't you just use an utility class to do this activity? Just a file, uh which will export a function, which will obviously do post get etcetera, and you pass the URL and the parameters in and it will return the result to you. Can't you use that approach of using the... That is also possible, correct?

### 00:13:02 · Speaker 3

export

### 00:13:11 · Speaker 3

friend

### 00:13:12 · Speaker 3

Yeah

### 00:13:15 · Speaker 3

possible. Correct, correct.

### 00:13:16 · Speaker 1

Okay

### 00:13:17 · Speaker 1

The purpose I ask this question Anubhav is every efficient technique like Herodotor component comes with its own complexities. Herodotor component use memo use callback anything that give you efficiency comes with its own set of a trade off in the performance. Correct? So it is good to use them only when required. Correct? So I generally ask some practical scenarios. Many people say like Redux connect. Correct? Redux connect is one of the most common usage of the Herodotor component. But it is not something that we want to use that is inherently like you cannot avoid using it so you are using. Correct?

### 00:13:47 · Speaker 1

I ask the practical examples just around that. Anyways, now let's spend around fifteen minutes Anubhav on some snippet driven questions, okay? uh I'll share a link with you. Please open this link and present your screen, okay? You can also open JS Fiddle. Can you open JS Fiddle and present your screen?

### 00:13:55 · Speaker 3

share

### 00:14:03 · Speaker 3

Yeah, let me do that.

### 00:14:04 · Speaker 1

com.

### 00:14:09 · Speaker 1

Okay

### 00:14:09 · Speaker 0

Sure, can you please open now JS Fiddle?

### 00:14:22 · Speaker 0

So Anubhav, I'm adding the question in the

### 00:14:23 · Speaker 1

Zoom chat, okay? So please open this question and add it in the JavaScript, the third window, okay? But don't run the code, okay?

### 00:14:46 · Speaker 0

Yeah

### 00:14:47 · Speaker 0

Yeah. You know, the my expectation is can you please predict the output of it? Guess the output. You have a minute to guess.

### 00:15:06 · Speaker 2

Okay

### 00:15:09 · Speaker 2

the same volume.

### 00:15:46 · Speaker 2

should be under

### 00:15:49 · Speaker 1

so there are three logs basically type of A, type of B and type of C. all the three are undefined.

### 00:15:57 · Speaker 3

it should be either undefined undefined because what I mean is

### 00:16:05 · Speaker 3

I think it should be underfined because the font is not stored. So they can't have access to have to do it is so the function is called.

### 00:16:17 · Speaker 3

basically checking type of A. So it's not looks like a rest. I think it should be undefined for all the

### 00:16:26 · Speaker 1

Got it. So your type of A B C are undefined, correct? That's what you are saying.

### 00:16:32 · Speaker 3

that's what I personally

### 00:16:35 · Speaker 1

Sure. Top left you see a run icon. Can you please click on that Anubhav? Top left run.

### 00:16:41 · Speaker 1

and bottom right you see something called console beta. Can you click on that?

### 00:16:46 · Speaker 1

Yeah, and that white area you can expand. Can you expand the white area? White area above. Expand. Yes.

### 00:16:55 · Speaker 1

So, it is not all the three are undefined, one is undefined and rest two are number, okay? Can you try deducing why remaining two are numbers, Anubhav?

### 00:17:10 · Speaker 3

I thought that it should be underlined as well because it's going by itself

### 00:17:16 · Speaker 1

it's not a easy question. It's a medium to hard question only, okay? I mean, even first time when I looked at it, I also answered all the three as undefined only, okay? That's why I thought of putting it so that somebody else will not do that mistake, okay?

### 00:17:17 · Speaker 3

dot

### 00:17:21 · Speaker 3

even

### 00:17:30 · Speaker 3

Right

### 00:17:34 · Speaker 1

So you would like to guess or we'll go to the next question.

### 00:17:38 · Speaker 3

let me take a few five seconds

### 00:17:44 · Speaker 1

What Anubhav, I did not hear.

### 00:17:46 · Speaker 4

I said like, yeah, we can move to the next one.

### 00:17:50 · Speaker 1

Sure, Sure. Okay.

### 00:17:55 · Speaker 1

Yeah, let me, I'll share another snippet with you, okay?

### 00:17:58 · Speaker 2

Okay

### 00:18:01 · Speaker 1

Please copy this snippet

### 00:18:03 · Speaker 0

paste, don't run the code.

### 00:18:06 · Speaker 2

Yeah

### 00:18:19 · Speaker 0

You can comment the above one.

### 00:18:24 · Speaker 1

I think it's a duplication. Line number fifteen to nine you can remove it.

### 00:18:27 · Speaker 2

Oh

### 00:18:28 · Speaker 1

and yeah eleven two that yeah. This is the question yes. Maybe can you try zooming in a bit. So that and recorded yeah little huh this is good.

### 00:18:55 · Speaker 2

could uh like different both the statements

### 00:18:59 · Speaker 3

and

### 00:19:00 · Speaker 1

Hello

### 00:19:00 · Speaker 2

Hello

### 00:19:00 · Speaker 1

plus

### 00:19:00 · Speaker 2

post

### 00:19:01 · Speaker 3

output should be bold is to pull out and it should be hello world

### 00:19:04 · Speaker 1

Correct. Can you please run now top left?

### 00:19:08 · Speaker 3

Hello

### 00:19:13 · Speaker 0

Yeah. What is coming?

### 00:19:24 · Speaker 0

First is

### 00:19:24 · Speaker 1

it is printing world is beautiful but hello world is not printing it is getting the uncut type error. correct?

### 00:19:30 · Speaker 2

Yeah.

### 00:19:32 · Speaker 1

Yes, can you just deducing again why you are getting the type error?

### 00:19:39 · Speaker 2

Okay, I'll do something else.

### 00:19:44 · Speaker 2

or

### 00:20:22 · Speaker 0

Relative to gas experience

### 00:20:23 · Speaker 1

What is happening?

### 00:20:26 · Speaker 3

I think it is something to do with war because it was a dead trial and I have done myself wrong.

### 00:20:33 · Speaker 1

Can you be a little louder Anubhav? I am not clearly hearing.

### 00:20:36 · Speaker 4

Uh, yeah, so I said like I think something to do with the war.

### 00:20:42 · Speaker 1

Okay. You want to convert var into const or let and try?

### 00:20:46 · Speaker 4

Yeah, I think

### 00:20:48 · Speaker 2

please, please

### 00:20:49 · Speaker 1

Please, please try.

### 00:20:51 · Speaker 1

yeah

### 00:20:59 · Speaker 2

Okay

### 00:21:09 · Speaker 3

from net would not work because

### 00:21:14 · Speaker 2

pass

### 00:21:15 · Speaker 3

the call is before the definition of the function.

### 00:21:19 · Speaker 0

Yeah

### 00:21:22 · Speaker 2

provide smart phone

### 00:21:31 · Speaker 2

Anukul, Donut, Arrow

### 00:21:34 · Speaker 3

Hmm

### 00:21:40 · Speaker 2

So,

### 00:21:55 · Speaker 0

ओके, वी विल गो टू नेक्स्ट क्वेश्चन अनुभव।

### 00:21:56 · Speaker 1

you want to still guess

### 00:21:59 · Speaker 3

Yeah, no problem.

### 00:22:00 · Speaker 1

No problem. See it's it's a simple hosting concept, okay? I've tried explaining very much in detail in my hosting videos. I I'll share the links personally with you for audience who are watching I'll try to link that on the screen. You can watch the hosting videos, okay? This is the last snippet that I'll share with you Anubhav. Most common one, I like asking this question so I ask in almost all the interviews.

### 00:22:04 · Speaker 3

training

### 00:22:24 · Speaker 0

Please copy the snippet and paste, don't run.

### 00:22:44 · Speaker 0

okay

### 00:22:45 · Speaker 0

and you get the output.

### 00:22:46 · Speaker 1

See, I hope you are enjoying the content like how Anubhav is responding and how I'm asking the question. And please like and comment about the video as as you very well know I have a noble cause of helping people to clear the interview. Just by liking and commenting I can reach out to more audience because YouTube will give more impressions. So please like this video and comment whatever you're thinking, okay, that will really really help my channel. Thank you so much and after doing that please continue watching further.

### 00:23:15 · Speaker 2

problem

### 00:23:21 · Speaker 2

print

### 00:23:23 · Speaker 3

five, five times.

### 00:23:25 · Speaker 1

Hmm

### 00:23:26 · Speaker 1

सो प्रिंट्स फाइव फाइव टाइम्स विथ व्हाट इंटरवल अनुभव? विल प्रिंट फाइव एट अ टाइम? और देयर इज सम बिल्डिंग।

### 00:23:31 · Speaker 3

Addy

### 00:23:33 · Speaker 3

at a time.

### 00:23:34 · Speaker 1

one second. So you mean you run the code, no delay. Immediately all the five are printed or there is one second delay then the five are printed. Or after printing all there is some delay. How is it?

### 00:23:47 · Speaker 4

they should not be delayed because uh by the time like uh these things the set time would get executed the loop has like already entered

### 00:23:58 · Speaker 1

Hmm

### 00:23:59 · Speaker 4

तो इट शुड बी लाइक ऑल एट अ वन्स विदाउट बिलीन

### 00:24:02 · Speaker 1

Okay

### 00:24:03 · Speaker 1

Are you sure? Can you just justify why there is no delay between printing or during the beginning of printing, why there is no delay? Can you justify that just that thing?

### 00:24:16 · Speaker 2

So I'm um

### 00:24:25 · Speaker 1

So overall how many set timeouts are created Anubhav? You tell me.

### 00:24:30 · Speaker 4

सो, ओनली लाइक देयर विल बी टोटल ऑफ फाइव ओनली। एक्जेक्टली। व्हाट यू सेड इज राइट। सो, फाइव

### 00:24:35 · Speaker 1

exactly. what you said is right. so five timeouts are created. correct?

### 00:24:39 · Speaker 4

Right

### 00:24:40 · Speaker 1

each having delay of what?

### 00:24:43 · Speaker 1

I mean time out of

### 00:24:44 · Speaker 4

Yeah, it says like thousand milliseconds, so one second.

### 00:24:45 · Speaker 1

hmm

### 00:24:49 · Speaker 1

Correct. All the so there are five timeouts created with one second delay each. Correct? So you're telling when you run the code there is no delay in printing.

### 00:25:07 · Speaker 2

they shouldn't be

### 00:25:10 · Speaker 3

reporting and different

### 00:25:14 · Speaker 1

or else let's come to the output part separately Anubhav. Just tell me now whenever this runs right tell me what will happen like as soon as this statement is encountered how many seconds does for loop will take to execute then how set timeout will step by step can you just explain not don't want to get into very depth like execution context and all those things just the basics how the things will execute probably we can take little bit of event loop and explain.

### 00:25:39 · Speaker 4

okay so uh like this is a browser API set down I'm not a browser API so they will be put in a separate queue as and when the loop is iterating so they nothing will be executed until their execution is completed and so once the execution is over in that particular like this delay is over like of thousand millisecond then they will be brought back to the main stack and then they will be

### 00:25:44 · Speaker 1

down

### 00:25:49 · Speaker 1

Correct

### 00:25:52 · Speaker 1

So

### 00:26:04 · Speaker 1

Hmm

### 00:26:08 · Speaker 1

correct

### 00:26:09 · Speaker 4

is equal to

### 00:26:10 · Speaker 1

correct. Yes. So, what you said is absolutely right Anubhav, okay? uh one one add on question I'll ask this is also a common question. So, set timeout to will it guarantees the delay whatever is given? Let's leave this case. In general, let's say three second delay is given for set timeout. Will it for sure execute after three second?

### 00:26:31 · Speaker 4

under in this loop.

### 00:26:32 · Speaker 1

in general in general I am asking not inside the for loop in general will it guarantee it will execute after that second that many seconds

### 00:26:42 · Speaker 4

Uh no I think it is not always a guarantee it depends like the scenario it is been called

### 00:26:48 · Speaker 1

Why it is not guaranteed? Can you tell a little bit?

### 00:26:53 · Speaker 4

I think because of the asynchronous nature

### 00:26:56 · Speaker 1

Exactly. Yes. Because only the main thread is executing things, correct? So finally all these activities has to go to main thread when main thread is free. So though the set timeout after three second elapsed it can come to the stack, but there could be other task in the stack. Correct? So the main thread may not able to execute it the exact time when it was supposed to execute. Correct? So that is a trade off using the set timeout. Please run the code. Zoom out and please run the code and we'll see what is the output.

### 00:27:31 · Speaker 0

Yeah

### 00:27:32 · Speaker 1

So you expand that white area, yeah, expand the white area.

### 00:27:34 · Speaker 0

Yeah

### 00:27:36 · Speaker 0

Yeah

### 00:27:36 · Speaker 1

and clear the console

### 00:27:41 · Speaker 1

run once again. Expand and run. Now run, yeah.

### 00:27:46 · Speaker 1

I see a delay, Anubhav. You're not seeing a delay?

### 00:27:49 · Speaker 1

a second delay

### 00:27:52 · Speaker 1

Correct?

### 00:27:56 · Speaker 3

Yeah, there is

### 00:27:58 · Speaker 1

Correct? Yeah, that's the reason I asked this question. People generally get confused with the delays. Five times five is absolutely right. And you also mentioned there is no delay between each printing. That was also absolutely right. But there is one second delay in the beginning. Correct? You would like to guess why there is one second delay?

### 00:28:03 · Speaker 3

right

### 00:28:12 · Speaker 0

but it's

### 00:28:21 · Speaker 1

I'll give one hint, okay? Basically, five timeouts are created almost at the same time. Correct? For loop will take microseconds to execute this loop. Correct? This much I can tell, further you need to guess.

### 00:28:37 · Speaker 4

by the time I think the loop executes so one of the set timer I guess gets that delay

### 00:28:47 · Speaker 1

Yes. You you are right, you are close. See, this is pretty much the what I wanted to say is for loop will execute much faster. Obviously, it is not going to take one second, correct? So, but five timeouts are created in less than let's say a few microseconds or milliseconds. Let's say five millisecond is taken to execute this uh run the loop. So, by that time already the five set timeouts are created, correct? Five set timeouts are already created. So, now at least one second has to elapse before running the first timeout, correct?

### 00:29:17 · Speaker 1

there is a delay. If for loop would have taken one second to execute this code, then what your answers gave was right. Like it will immediately execute because one second already elapsed. Since for loop is faster than whatever the set timeout interval that we have given, due to that nature we get a initial one second delay. Okay?

### 00:29:35 · Speaker 1

So, yeah, that's all about the snippet driven question that I want to ask Anubhav. Okay, so we are at almost half an hour we have finished. I do not know how the time flew. Okay, you can stop sharing.

### 00:29:50 · Speaker 1

Yeah, so Anubhav, let us spend last five to ten minutes, whatever we left now, on the feedback and any questions you have. First, let us start with any questions that you have, then I'll try to give my feedback. Tell me if you have any questions, ask me.

### 00:30:05 · Speaker 4

तो लाइक आई हैड नॉट फॉर दीस कांसेप्ट्स लाइक हाउ डू वी प्रिपेयर फॉर मशीन कोडिंग राउंड काइंड ऑफ लाइक आर दे आर दीस राउंड्स वेरी फ्रीक्वेंट और इट डिपेंड्स ऑन द इयर्स ऑफ एक्सपीरियंस वी हैव और या

### 00:30:19 · Speaker 1

or

### 00:30:20 · Speaker 1

So machine coding is very common in the premium companies, probably whatever you're aspiring, like let's say Microsoft you are aspiring or Amazon you are aspiring, Swiggy you are aspiring. So machine coding is mandatory in all the premium companies, whatever the big product companies we call, right? So machine coding round is mandatory. So you have to prepare for machine coding interview if you are aspiring for that. But there are a lot of companies which I can tell, I can't name the companies, but there are many tier two kind of companies which don't have the machine coding round as separate. So

### 00:30:30 · Speaker 4

Cody

### 00:30:50 · Speaker 1

depends on your preparations Anubhav. If you are preparing for the tier one or first few companies in tier two then obviously you need to prepare for machine coding. If not then probably it is not necessary. Yeah.

### 00:31:04 · Speaker 1

any other

### 00:31:04 · Speaker 4

And then one more question. Please. Yeah, related to data structure and algorithms. So like in general like if you are a back end developer so we cover like TP and all those hard topics as well. But as a front end or like because even if we are working on Node JS we are more commonly referred as front end only steps. Exactly. So what all topics we need to like lay emphasis on if we have like one or two weeks time to prepare for education.

### 00:31:06 · Speaker 1

please

### 00:31:09 · Speaker 1

Hmm

### 00:31:15 · Speaker 3

correct

### 00:31:17 · Speaker 3

but

### 00:31:24 · Speaker 3

Exactly. So

### 00:31:34 · Speaker 1

So my advice is this Anubhav. Let's say you are preparing for companies like Apple, Google, uh Apple, Google, Facebook or Meta what we call. If you're preparing for these companies then sky is the limit. Whether you are front end developer or back end developer. They hire the generalist, not specialist, correct? So all the topics you need to cover. But in case if you're preparing, this includes Amazon as well, okay? Amazon, Apple, Facebook, all these companies you have to prepare almost all the data structures. But if you're preparing for some other companies with my experience like Microsoft, SAP and these kind of companies, then probably you can limit yourself to strings, arrays, linked list and binary search trees.

### 00:32:11 · Speaker 1

There is very few occasions where these companies ask graphs or dynamic programming, greedy approach, backtracking, all these questions to a front end developer. Okay. So where they where they will have a machine coding ground to test your skills, right? So they will not spend lot on the data session algorithm. But obviously, my my funda is simple. If you are appearing for a non not at all premium companies, then limit yourself to strings and arrays. If you are applying for a semi premium, then go to the link list. If you are applying for premium,

### 00:32:41 · Speaker 1

excluding the mang. Okay? excluding the mang, there are a lot of premium companies. Then go till link list and the binary searches also. In fact, I have already made tutorials, all the link list till link list I have covered. uh If you wish you can watch that. I'll try to link that on screen for the audience. Yeah. Any other questions regarding the interview? We have any other questions? Or overall also?

### 00:33:00 · Speaker 3

moral also. So that's all. Okay. That's all from us.

### 00:33:02 · Speaker 1

Okay

### 00:33:04 · Speaker 1

Sure Anubhav. So it was a nice interview from my side whatever I felt I'll tell. Okay.

### 00:33:08 · Speaker 1

So, with with whatever the answer that you are giving, fundamentally you are strong, like conceptually you are able to explain very good. Technical communication skills are good. So there is two things, communication and technical communication. There are many whenever I ask what is hosting, they start writing the code or whenever I ask closure, they start writing the code. So code writing is one part of the development developer job, correct? You should know how to articulate whatever you know. So in that way, you are able to technically communicate what you know. That is good, okay? And react

### 00:33:38 · Speaker 1

concepts also fundamentally are good. Many still don't know what is reconciliation itself. reconciliation your higher order component you are able to answer well. So conceptual knowledge I I'll give full marks. Whatever things that you can improvise that I I notice is whenever I I in the beginning also I mentioned there is a breadth in the depth concept in the interview where you touch base on lot of topics and we get into depth wherever we feel it is essential. Okay. So in that depth I feel you need to work a little more. For example the interpretation question that I so you may have to dig little deeper to understand what is the interpretation etcetera.

### 00:34:08 · Speaker 1

correct? Or for example the set timeout one or the hosting question which I asked snippet driven. Snippet driven are very very common in the interview. Okay? Why because all the snippet driven question will have one tricky part. Obviously one tricky part will be there you need to able to unlock it. So that is the important part of the snippet driven questions. So if but if you fundamentally become strong let's say you already know what are closures. But if you spend more time and understand in depth of closure you will be able to easily answer the for loop and that set timeout what I asked. Correct? Your answer was right what I'm telling in depth.

### 00:34:37 · Speaker 0

Right

### 00:34:38 · Speaker 1

So why when why in depth in this series whenever you are applying for the tier one companies. So they always look for the in depth in depth question in depth concepts correct because obviously they will have problems inside which somebody who has in depth knowledge only can solve. Mediocre cannot solve. Okay that's the only feedback that I'll give. Like I mentioned I'll send more detailed email to you as well to which consolidates all all whatever everything that I explained. Okay. Now that's all from my end Anubhav it was nice talking to you. Okay. Any questions you have Anubhav.

### 00:34:40 · Speaker 0

Towns

### 00:34:59 · Speaker 2

It's

### 00:35:08 · Speaker 4

I would say like it was a good experience. I think it will surely help me as well in my future experiences.

### 00:35:12 · Speaker 1

Apple

### 00:35:14 · Speaker 1

Yes

### 00:35:15 · Speaker 1

थैंक यू, थैंक यू। होप यू आर वाचिंग अनकॉमन गीग्स अनुभव, माय वीडियोस एंड अदर थिंग्स।

### 00:35:21 · Speaker 4

Yeah, yeah, surely I am doing that on television.

### 00:35:25 · Speaker 1

Okay. Great, great अनुभव. Obviously, like I always mention, if you watch, I have sixty plus videos. Obviously, if you're preparing right now, you cannot watch all the videos. But even if you watch my summary videos where I've explained React JS, complete React JS interview preparation, JavaScript complete interview preparation, couple of those videos, if you fully watch, lot of concepts will be clear to you. So there are around thirty, thirty-five minutes videos, thirty, thirty-five and forty minutes videos. So two videos if you watch, it is hardly one hour. If you spend one hour and watch those two videos, your fundamental becomes much, much stronger. Okay, I would advise watching. that

### 00:35:56 · Speaker 3

Sure

### 00:35:57 · Speaker 1

ओके, दैट्स ऑल अनुभाव, वेरी नाइस टॉकिंग टू यू, हैव अ गुड डे देन, बाय।

### 00:36:01 · Speaker 3

Thank you

### 00:36:02 · Speaker 1

Okay

### 00:36:05 · Speaker 1

Welcome back guys. I hope you enjoyed the mock interview with Anubhav. So it was a nice interview. He was able to articulate a lot of thoughts and wherever the small correction that he can do I have already communicated that to him in the interview. And certain things that I think personally I can convey I'll be sharing it over the email. In case if you are someone who also want a free mock interview, please register in the Google form that is present in the description section. It's not like obviously it's not like I'll be able to take interview for all, but definitely I'll keep you contact. I only ask very basic details to contact you. If not now,

### 00:36:35 · Speaker 1

in future whenever I want to do mock interviews or whenever I want someone to partner with me in the interview process definitely I'll consider your profile okay. Thank you so much for watching in case if you not like the video please like the video comment whatever you felt about the the mock interview process and please subscribe to uncommon geeks this will help me a lot into spreading this sort of helping people to clear the interview and please share the information with your friends and whatever the question that are asked in the interview are present in my github repository I'm linking the github repository in the comment section you can always go and check that out and practice on your own.

### 00:37:05 · Speaker 1

questions are very tricky so please find the answer for yourself if you still not able to find please mention that in comment section I'll try to explain why it is so okay and please follow me on medium I write lot of medium articles I I got decent followers on medium also recently okay please follow me on medium too and uh star my github projects thank you so much for watching catch you in next video
