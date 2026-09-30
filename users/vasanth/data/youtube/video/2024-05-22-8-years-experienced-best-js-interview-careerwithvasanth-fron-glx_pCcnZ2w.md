---
id: glx_pCcnZ2w
title: 8 Years Experienced Best JS Interview|CareerWithVasanth Frontend Interview
  Ep-01|Solution At the end
date: '2024-05-22'
url: https://www.youtube.com/watch?v=glx_pCcnZ2w
description: "#interview   #react #reactjs  #frontend  #javascript \n\nTo get a dedicated\
  \ one on one,  you can reach out to me here: https://topmate.io/vasanth_bhat\n\n\
  @careerwithvasanth  is a Youtube channel dedicated to helping candidates clear their\
  \ interview. There are more than 150 videos and new videos will be uploaded every\
  \ week. If you're seriously preparing for interviews and looking for tips and tricks,\
  \ please subscribe to my channel and press the bell icon.\n\nJoin CareerwithVasanth\
  \ community to discuss with other developers: t.me/uncommongeek. \nFollow me on\
  \ LinkedIn - https://www.linkedin.com/in/careerwithvasanth/\nMedium Blog https://mevasanth.medium.com/\
  \  \n\n\U0001F449 “Contact on WhatsApp: 9731039408”\n\nJavaScript Interview preparation\
  \ series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nJavaScript Custom implementation/polyfills Series: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\n\
  \nFrontend system design series: https://www.youtube.com/watch?v=gN8LQTff21g&list=PLmcRO0ZwQv4RYUD10hUnWjWb-RRSpm3KM&ab_channel=UncommonGeeks\n\
  \nMAANG series for frontend developer: https://www.youtube.com/watch?v=s-b-txm_Gvk&list=PLmcRO0ZwQv4SNhbW4CI4vc-6IHBHCKzZN&ab_channel=UncommonGeeks\n\
  \nFrontend mock interview series: https://www.youtube.com/watch?v=uW7MfzoD1po&list=PLmcRO0ZwQv4SwXLVpnKb_nFQx1Wd2XEjD&ab_channel=UncommonGeeks\n\
  \nShorts for quick access to all frontend resources: https://www.youtube.com/watch?v=8ByBOT7Aehs&list=PLmcRO0ZwQv4SXtrTYIU_dPygZgOgYV81S&ab_channel=UncommonGeeks\n\
  \nTips for freshers: https://www.youtube.com/watch?v=hGIOIdPNNqE&list=PLmcRO0ZwQv4QBiZns-nYX5qnHKAepVeqH&ab_channel=UncommonGeeks"
author: careerwithvasanth
duration: 00:24:23
model: saaras:v3
transcript: true
---

# 8 Years Experienced Best JS Interview|CareerWithVasanth Frontend Interview Ep-01|Solution At the end

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Career with Vasanth YouTube channel. Previously this channel was known as Uncommon Geeks. My name is Vasanth. So with me today I have Kriti Suman. So this is a session where we are primarily spending on the mock interviews. So in this particular session I'm going to take a combination, primarily a JavaScript questions I'll be asking. Kriti already has seven plus years of experience. Maybe I would end up asking some couple of software engineering sort of software development or software engineer sort of questions as well, okay? And without wasting further time let's get started. Kriti if you can introduce yourself.

### 00:00:29 · Speaker 2

Yeah, sure. So I have total seven point one year of experience and totally I'm working in the Angular framework. And I started from Angular two and right now it's an Angular eleven. And apart from this I'm just working in the banking domain and leading the team as well. And I have sorts of the knowledge in the JavaScript, Node.js apart from the Angular.

### 00:00:36 · Speaker 1

good

### 00:00:40 · Speaker 1

and

### 00:00:50 · Speaker 1

which

### 00:00:52 · Speaker 2

Wonderful. Wonderful.

### 00:00:52 · Speaker 1

Wonderful. Wonderful, Kriti. Kriti, let us let me start by asking a very simple question. Okay? So in Angular application, I'm very sure you might have built something for the authentication flow, correct? I'll ask you only two flows, whether you built it or not, but it's very common interview question. Where a user logs in to your website and after login, so basically next time, let's say they close the tab and open next time, definitely we'll not ask them to login again. Same way how Facebook, YouTube, Instagram, everything works. As long as you're logged in

### 00:01:22 · Speaker 1

the application you continue to login, correct? Can you just explain me this entire authentication flow Kriti? How do we how will we achieve this? I tried presenting a whiteboard. Would you like to draw the basic architecture here?

### 00:01:37 · Speaker 2

Sure

### 00:01:38 · Speaker 1

Yeah, thank you.

### 00:01:39 · Speaker 2

So suppose that this is the uh page where I am just creating a login uh page basically. Yes.

### 00:01:45 · Speaker 1

the law

### 00:01:46 · Speaker 2

It's a login here.

### 00:01:48 · Speaker 1

That is fine, yeah. And I'm primarily interested in the different elements that would interact karte like you told the caching, the back end. I'm interested in like which all system which have how they interact. Yeah.

### 00:01:50 · Speaker 2

from

### 00:01:58 · Speaker 2

So from here we are just making some data to the our caching moment. hmm cassette controller. And the it is not here like that simply because whenever we are just passing some data from this component we are also using the salt encryptions there. So we are encrypting our passwords.

### 00:02:03 · Speaker 1

Hmm

### 00:02:04 · Speaker 1

Controller

### 00:02:05 · Speaker 1

and

### 00:02:15 · Speaker 1

So we

### 00:02:18 · Speaker 1

Got it

### 00:02:19 · Speaker 1

Mm-hmm

### 00:02:20 · Speaker 2

and that password we are loading in the our cache systems and in the cache systems we have some token expirations session as well. So I'll provide some token here and with the some timeline.

### 00:02:27 · Speaker 1

plus

### 00:02:31 · Speaker 1

and with

### 00:02:34 · Speaker 1

Okay

### 00:02:35 · Speaker 2

once it is faced the cache, it will go to the my server side. So server will have to validate whether the token is the validity or not or expiration is there or not. So that cache will store there. So suppose second time again I am coming to my login page and since that time I don't have a cache, right? So if before sending my data directly to the server through the my browser, it will first go and check in the cache whether the data is available in there or not.

### 00:02:39 · Speaker 1

So sir

### 00:02:45 · Speaker 1

So

### 00:02:48 · Speaker 1

suppose

### 00:02:51 · Speaker 1

Mm-hmm

### 00:03:05 · Speaker 1

Okay

### 00:03:05 · Speaker 2

Correct. So it will not repeatedly every time call the server API again and again. So it will stop here itself. If that is suppose expired, it doesn't mean that it will again call the server because it's expired. Then it will just try to give some free flight XHR to this guy. Free flight.

### 00:03:06 · Speaker 1

Correct

### 00:03:19 · Speaker 1

because

### 00:03:26 · Speaker 1

Free flight. No problem.

### 00:03:29 · Speaker 2

So this preflight access tower and it will just try to uh knock the door on the server side whether the data is available with you or not. So it will again because this data is directly integrated with the cache system as well. So the server will respond to this cache systems and from here my as we are using the Google Chrome or the Viet engines. So it will directly interpret with this cache only. So it will not go to the server directly. That's how we are handling it.

### 00:03:38 · Speaker 1

So

### 00:03:44 · Speaker 1

Hmm

### 00:03:57 · Speaker 1

Hmm

### 00:03:59 · Speaker 1

Sure. So Kriti, like like I'll try to summarize, okay? So we have a website, okay? So and whenever users tries to log in, okay? Let's say this is a log in button. As soon as users tries to log in, what we are doing is as soon as they log in, so basically you we are making API call, getting the user information, correct? And let's say you are getting some token, that token you are storing it in the cached system, correct?

### 00:04:03 · Speaker 2

Hello

### 00:04:06 · Speaker 2

and

### 00:04:19 · Speaker 2

you get

### 00:04:24 · Speaker 2

So this is the cash

### 00:04:24 · Speaker 1

So this is the cache where you are storing. Okay? So you're storing this cache. So next time, let's say user has closed the tab and opened the tab next time, you will check whether in the cache whether the token is available. If token is available, then you will take user directly to some login screen to home screen. Correct? Home or like home is just a indicator here like wherever the your core of the application. Correct? So there you will take the user. Whenever the you have a valid token, correct? Let's say the token is expired. Whenever the token is expired, so you are taking you will make an API call. Am I right?

### 00:04:28 · Speaker 2

like

### 00:04:35 · Speaker 2

Valuable

### 00:04:40 · Speaker 2

Congress

### 00:04:45 · Speaker 2

exactly

### 00:04:49 · Speaker 2

Experience

### 00:04:54 · Speaker 1

a pre-flight you took. Yes. You make an API call, here is the server, correct? So here is server where we will make an API call, get the token back. Once you get the token back, you are again going to store that in the cache and the process repeats, correct?

### 00:04:54 · Speaker 2

Yes

### 00:04:56 · Speaker 2

call

### 00:04:59 · Speaker 2

there is

### 00:05:09 · Speaker 1

सो कृति लेट अस अंडरस्टैंड या एलाब्रेट इफ यू वांट टू ऐड एनी मोर पॉइंट्स यू कैन ऐड

### 00:05:11 · Speaker 2

Hello

### 00:05:15 · Speaker 2

if here is again I am getting the token so that will be match here itself again with the one another service we have created. So we will just take a if the token is available from the state management or not and we are only updating our expiry date or expiry time. Okay. So we know that the token is already available for entire of the system.

### 00:05:23 · Speaker 1

Hmm

### 00:05:34 · Speaker 1

Okay

### 00:05:38 · Speaker 1

Hmm

### 00:05:40 · Speaker 2

That's how it continues it

### 00:05:42 · Speaker 1

Okay. Sure. I'll again I'll summarize quickly Kriti. So I as a user came to your website. I clicked I entered my email ID password I clicked on like login. As soon as I click on login you made an API call got the token you stored the token and next time whenever I open the application you checked whether the token is available in the cache. Get get that particular token and if it is valid you were going to go take me to home screen if it is invalid you are going to make a API call to server to get a new token. Correct?

### 00:05:47 · Speaker 2

Like

### 00:05:59 · Speaker 2

that

### 00:06:08 · Speaker 1

So, so now only question that I have is

### 00:06:08 · Speaker 2

Sure

### 00:06:13 · Speaker 1

I've stopped the whiteboard. So only question I have is first of all how do you get to know like the token is valid or not next time whenever I open the website?

### 00:06:21 · Speaker 2

So in that conditions actually that is why we I just told that pre flight or XHR mode right? So every time when you open

### 00:06:27 · Speaker 1

mode, right? So every time when you open, you make an API call then with that to check whether valid or not. Okay.

### 00:06:32 · Speaker 2

the doctor

### 00:06:34 · Speaker 2

and we are also using some interceptors in our angular application or entire applications. So that is going to make the some pre flight mode XHR call. And then it is checking it there itself whether that is available or not. With the so we can just expand our expiry time from the front end side not the back end always.

### 00:06:37 · Speaker 1

hour

### 00:06:43 · Speaker 1

and they

### 00:06:48 · Speaker 1

with the

### 00:06:56 · Speaker 1

ओके, सो इन ओव्हरऑल प्रोसेस कृति, हाउ मेनी टोकन्स आर इन्वॉल्व्ड? वन टोकन्स, टू टोकन्स, हाउ मेनी टोकन्स आर इन्वॉल्व्ड?

### 00:07:02 · Speaker 2

I think there is only one token per user.

### 00:07:05 · Speaker 1

Okay, so that is the Got it. What what is the token you call like? What do you refer it as? Authentication, authorization.

### 00:07:05 · Speaker 2

is the

### 00:07:10 · Speaker 2

authentication authorization

### 00:07:12 · Speaker 2

that is also involved with the authentication only, not with the authorization things.

### 00:07:19 · Speaker 1

Okay, sure

### 00:07:19 · Speaker 2

Sure

### 00:07:21 · Speaker 2

So, we generally tell it as a session ID in our term and that is only for help for for the

### 00:07:25 · Speaker 1

in our term

### 00:07:31 · Speaker 2

authentication purpose

### 00:07:32 · Speaker 1

Okay, sure. Sounds good, Kriti. There are a lot more details required for this. Probably I'll explain if time permits at the end, okay? But whatever you said so far is not wrong, but there like we can add more clarity into this, okay? So can you like present your Chrome one window where nothing is opened, only like can you open the plain Chrome window? I'll share a online editor link with you and please open this link, okay?

### 00:08:04 · Speaker 1

So, can you tell me the difference between session storage and a local storage?

### 00:08:08 · Speaker 2

So session storage is just like uh suppose I have stored my data in here in the session storage. And if I will close the my browser or even I close the tab, my session is gone already. Okay. And if I will inspect it, my session storage data will be not available there. Okay. But in case of the the local storage, if I will close my system as well and the entire Google Chrome as well, but still my storage will be storage whatever the data I have stored.

### 00:08:13 · Speaker 1

Hmm

### 00:08:19 · Speaker 1

Okay

### 00:08:24 · Speaker 1

Okay

### 00:08:38 · Speaker 2

it will be available there. Even I will come and log in again, my data will be there.

### 00:08:40 · Speaker 1

in the

### 00:08:43 · Speaker 1

Okay. I have two follow up questions on this, okay? So session storage whatever you are storing, is it accessible uh even when like multiple tabs are open from the same web application? Like for example this website what we open is program miss dot com, correct? I open the same website in another tab in the same browser. So both the tabs can access the session storage? Got my question, right Kriti?

### 00:09:02 · Speaker 2

Yeah

### 00:09:06 · Speaker 2

Yeah, I got your point.

### 00:09:07 · Speaker 1

Huh

### 00:09:07 · Speaker 2

No, I think in the session storage when I just open my one tab only the data will be available here itself. You cannot share basically.

### 00:09:14 · Speaker 1

यू कैन नॉट शेयर बेसिकली बिटवीन द टैब। करेक्ट?

### 00:09:17 · Speaker 2

M

### 00:09:18 · Speaker 1

Okay. If audience who are watching like you always say the best way to get use of this mock interview is like you try answering. Whenever I ask a question pause the video, try to answer and see what is the answer candidate giving so that you get a sense. Yeah, sure. We will discuss Kriti. Now another follow up question that I had was on the local storage. Like you told local storage is storage. That is like

### 00:09:37 · Speaker 1

even if you close the window or even if you restart the system that storage is going to be always present unless probably we clear the browser's cache. Correct? So now the question is let's say you have not opened website like programbiz.com. This website you have not opened. Is there any way without opening that website you can access the local storage things the data that you have stored? Got my question right?

### 00:09:48 · Speaker 2

dot com

### 00:09:57 · Speaker 2

So, yeah. So you are meant to say that from what I understood, you wanted to close the browser and you wanted to access somewhere else, right? No, no, let's say.

### 00:10:07 · Speaker 1

No no, let's say, see, this program is dot com, this saved some information in the local storage. Okay? And I closed that, that tab I closed. I opened google dot com now. Okay? So is there any way I can access the local storage values that are stored by program is dot com? Got my question right? Now I think it is clear.

### 00:10:14 · Speaker 2

I close that

### 00:10:18 · Speaker 2

Anyway

### 00:10:24 · Speaker 2

Yeah, it's clear.

### 00:10:25 · Speaker 1

Yeah, thank you. Without opening the website, can we access the local storage data that was saved or persisted by the website?

### 00:10:34 · Speaker 2

Yeah, I think yes, we can get it. Okay. Because our local data will be there and there, right? We have to just only say get the items. So, if that is available, we can get it, right?

### 00:10:37 · Speaker 1

Okay

### 00:10:41 · Speaker 1

have to

### 00:10:48 · Speaker 1

Okay. Let's say I am aware of the key with which you saved. Like let's say we stay like saved the key as like login_key and if I try to get access to that like local storage.getitem login_key just execute that in the inspect Chrome inspect. You think I'll be able to get that? Got my question I think I'm clear Kriti correct?

### 00:10:48 · Speaker 2

Let's say I am aware of the

### 00:11:06 · Speaker 2

Yeah, yeah, yeah, yeah.

### 00:11:07 · Speaker 1

Okay, Okay. Thank you.

### 00:11:08 · Speaker 2

think you cannot get it

### 00:11:10 · Speaker 1

Okay. It is it is then you're saying it is stored persistently. Yeah. You're saying it is stored persistently but you cannot access without opening the website. Correct?

### 00:11:13 · Speaker 2

store even the key are same

### 00:11:23 · Speaker 2

Yes

### 00:11:24 · Speaker 1

Okay. Sure. So, are you aware of call apply bind, Kriti?

### 00:11:30 · Speaker 2

Yes

### 00:11:31 · Speaker 1

Can you write an example for all the three? Call apply bind here. You can remove whatever is here and write the yes remove everything and you can start giving an example call apply bind.

### 00:11:35 · Speaker 2

move at

### 00:11:42 · Speaker 2

So suppose that

### 00:11:44 · Speaker 1

you write it fully then we will discuss

### 00:11:45 · Speaker 2

discus

### 00:11:50 · Speaker 2

So I just have created a two users and I wanted to print one. Okay. Because that is available in some another function. So what I can do?

### 00:11:53 · Speaker 1

Okay

### 00:11:56 · Speaker 1

Okay

### 00:12:02 · Speaker 1

Yeah

### 00:12:02 · Speaker 2

I can uh just take the reference of this print full basically.

### 00:12:07 · Speaker 1

Hmm

### 00:12:11 · Speaker 2

and when I'll apply with the call method here and then I can just pass the user one or two whatever it is. So this will reference to this with the help of the this keyword actually is happening here.

### 00:12:24 · Speaker 1

Hmm

### 00:12:24 · Speaker 2

and what the here right I'll forget to mention that this keyword here that this dot

### 00:12:33 · Speaker 2

first name and the this dot last name here. So it will try to refer this guy and now it is asking which one is referring. So this will refer whoever immediate objects are there calling.

### 00:12:46 · Speaker 1

Hmm hmm

### 00:12:48 · Speaker 2

So it will give the output like this. And with the help of the apply method and the call method most things that suppose I wanted to pass multiple arguments like here.

### 00:13:01 · Speaker 2

I have some like a country as well. And city as well.

### 00:13:09 · Speaker 2

So here I can just pass

### 00:13:13 · Speaker 2

India

### 00:13:15 · Speaker 2

and then Bangalore

### 00:13:17 · Speaker 1

Hmm

### 00:13:17 · Speaker 2

So, like this individually elements I can create and I can pass it as an argument. uh particular parameter. Mm-hmm But in the apply method what is happening I have I can just create one array type and inside that I can just do that. So same thing will be happening there. With the bind method what is happening like same way it's bind here but bind is always available for your future reference.

### 00:13:24 · Speaker 1

Mm-hmm

### 00:13:25 · Speaker 1

Mm-hmm

### 00:13:31 · Speaker 1

I mean

### 00:13:47 · Speaker 2

not for current one. So suppose that you wanted all that functions in the futures. So you are you can just only pass some reference to that the bind method.

### 00:13:49 · Speaker 1

suppose that

### 00:13:57 · Speaker 1

Okay. Sure. So, Kriti, whatever explanation you gave is good. I think most when I ask in the interview, everybody gives this example only. But you have seven years of experience, Kriti. Tell me the practical use case. When did you use call apply bind?

### 00:14:04 · Speaker 2

Night

### 00:14:12 · Speaker 2

I was creating one functions, okay? And then I got to know that I have to create one utility class of the functions as well. But since whatever the items I had here, right? I'm not so sure what is the argument someone is passing there because that was using some split and rest operator as well. So, hopefully I came here return functions and then I use the the functions which I am passing here, I use the generate dot apply method here itself. So it was

### 00:14:15 · Speaker 1

and then

### 00:14:20 · Speaker 1

Hmm

### 00:14:24 · Speaker 1

I've

### 00:14:25 · Speaker 1

What is

### 00:14:28 · Speaker 1

Okay

### 00:14:31 · Speaker 1

Hmm

### 00:14:41 · Speaker 1

Hmm

### 00:14:42 · Speaker 2

taking the function as a callback functions and whatever the arguments of parameters we were passing it was referring to this guy again the this keyword with the help of the apply method

### 00:14:45 · Speaker 1

and

### 00:14:51 · Speaker 1

the head of

### 00:14:52 · Speaker 1

Okay. Got it. Sure. Sure. Okay. Kriti M. Sen sending a code snippet in the chat section. Okay. Copy the snippet and paste the snippet. Okay. In the same window and try to guess the output for the same. And audience who are watching you can also just look at the snippet and try to guess the output.

### 00:14:54 · Speaker 2

Sure

### 00:15:13 · Speaker 2

Om

### 00:15:19 · Speaker 2

सो व्हेन आई विल ट्राई टू इन्भोक इट, इट शुड प्रिंट लाइक दिस।

### 00:15:24 · Speaker 2

One

### 00:15:26 · Speaker 1

Okay

### 00:15:28 · Speaker 2

And if I will just try to print it, it should print as a zero because this guy is taking uh the scope will be the same quantum method here. So again it will become zero.

### 00:15:39 · Speaker 1

Hmm

### 00:15:41 · Speaker 1

ओके. प्लीज रन द कोड. गुड. स्टॉप शेयर मी.

### 00:15:44 · Speaker 2

Stop sharing bro

### 00:15:45 · Speaker 1

You can stop sharing Kriti. Okay? So I'm done from my end Kriti and this is the time where I give my feedback to you. But before I give my feedback, you have any questions for me? Like primarily around the interview, you have any questions?

### 00:15:56 · Speaker 2

now it's all good go far. very good I am very much interested about this.

### 00:16:03 · Speaker 1

Sir. So, Yeah, please.

### 00:16:04 · Speaker 2

So, I would like to ask more then we can just discuss more on the local store session store that you asked. Yeah. I was actually little confused there.

### 00:16:11 · Speaker 1

Yeah

### 00:16:14 · Speaker 1

Sure

### 00:16:14 · Speaker 2

science

### 00:16:15 · Speaker 1

Yeah. Sure Kriti. Like probably if time permits we can discuss any other topics that I asked in the interview but let me this is an important phase for me to give feedback to you and it also applicable for a lot of candidates who are watching the video. See primarily everybody who's watching the video consider a fact like if you're somebody who's having an experience of more than six years. Then you are considered like a senior developer in an organization. So the primary expectation from you is like

### 00:16:27 · Speaker 2

Yeah

### 00:16:39 · Speaker 2

Yeah

### 00:16:40 · Speaker 1

how do you basically create a system and manage it? So that is the reason I asked you authentication flow, right? There is no one right way or wrong way. I don't even consider that like that like a system design, a deep system design sort of a question, but very basic level question, correct? What you explained was not wrong. But there can there was an opportunity where you could have induced more clarity. Like step by step probably how how we can proceed further, okay? So that's a small feedback. So anybody who goes for interview or who are having like six plus years of experience, make sure you

### 00:16:54 · Speaker 2

Hello

### 00:17:01 · Speaker 2

problem

### 00:17:05 · Speaker 2

the

### 00:17:10 · Speaker 1

go with an extreme clarity about the things that you explain. I'm not saying like you don't know the concepts, but interviewer will have a very short time and within that time frame only they need to judge you. So try to give very crystal clear answers. And then next, so next question like whatever I asked on the local storage and session storage, right? So if by looking at those answers, Kriti, like what can be inferred is, you need the concepts. Like for example, I could if I asked you to like question like how to create a session storage, how to create a local storage, you could have created. The questions that I asked

### 00:17:40 · Speaker 1

probably you are not anticipating. Correct? So where I'm coming from is like my advice to all basically who are watching this video is uh have the temperament of why in your mind. Like why basically this is happening. So whenever you keep asking why then only you will identify discover some questions because reading an article or reading an reading official documentation or YouTube video may not trigger that. So you should start asking why multiple times so probably then you will get into that temperament of reading.

### 00:17:45 · Speaker 2

Yeah

### 00:18:10 · Speaker 1

Okay. And snippet you are able to interpret excellently Kriti which is good. I think whatever you know, uh at least whatever you answered so far, so you have clarity on some, complete clarity. Some you are having little bit of mediocre clarity. So where I want you to just polish your skills. Okay? Yeah.

### 00:18:26 · Speaker 2

Yeah

### 00:18:26 · Speaker 1

I honest feedback karti. You tell me, is there any closing question for your last two minutes?

### 00:18:30 · Speaker 2

uh like uh I really would like to work more on the authentication authorization. Yes. Since I didn't get much more chances as from the we are building a product for some another product based company. Yes. So we don't have that much control over there.

### 00:18:37 · Speaker 1

Yes

### 00:18:40 · Speaker 1

as a

### 00:18:45 · Speaker 1

Yes

### 00:18:48 · Speaker 1

Got it. Yes, yes, I understand Kriti, but like I told that your experience these things matter. So even if you're not got an opportunity, please try to learn on your own so that next interview when this is asked, you're able to answer and clear that interview. Okay?

### 00:19:01 · Speaker 2

Hello

### 00:19:02 · Speaker 1

Sure. So yeah, we are closing the session Kriti. I hope this session was useful. You liked the question that I asked.

### 00:19:08 · Speaker 2

Yeah, sure, obviously, it is very helpful for me. And I can always practice on those.

### 00:19:12 · Speaker 1

Thank you

### 00:19:15 · Speaker 1

Sure, sure. Thank you so much for joining the session Kriti and taking the mock interview with me. And audience who have watched the video, please like the video. If you think it is useful for your friends, please share with them. If you're not already subscribed to my channel Career with us, please subscribe. And whatever the question that I asked to Kriti in the video, I'll try to make a short extension to this video where I try to explain answers to that. Thank you so much for watching. Catch you in the next video.

### 00:19:38 · Speaker 2

Hello

### 00:19:38 · Speaker 1

I'm sure you liked the session with Kriti and in this particular video, it's a short video, post video basically I'm discussing the important question that I asked in the interview, okay, that Kriti did not answer properly. The first question is local storage and session storage where I asked like the data between session storage in between two tabs is it shared? So answer is no. The data cannot be shared between the two tabs of the same website. Let's say you have google.com and google.com/home. So in google.com you stored

### 00:20:08 · Speaker 1

value in the session storage and you want to access it from google.com/home, you'll not be able to access. Okay. Second question I asked is local storage, the value that you stored in the local storage, can you access it even when the website is not opened? Yes, you can access it. Use if you know the right keys to the local storage, whatever you are storing. Okay. So it is a security concern. So if you are storing some information in the local storage, make sure you are not storing the sensitive information. Even if you are storing sensitive information, then make sure it has a

### 00:20:12 · Speaker 2

one

### 00:20:38 · Speaker 1

quite a proper expiry date or you at least you are encrypting it so that somebody some random person is not able to access those information. Okay. Now the another important question that I asked was the authentication flow. Okay. Let me try to

### 00:20:53 · Speaker 1

present a whiteboard and see if I can show that. Okay. So, like I asked, there'll be like your website is here and you have a local storage or a session storage depending on your requirement and you have a server. Okay. So let me name it as like this is your website.

### 00:21:14 · Speaker 1

and this is your cache, okay? and this is your server. this is your server, okay? so now

### 00:21:27 · Speaker 1

The important thing to know here is how actually the authentication would work. Okay? So if you have to draw a line,

### 00:21:34 · Speaker 1

between the three, okay? First, whenever you log in, what the what the website will do is it will it will make a call to the server, okay? And from server it will get back a valid token, okay? And that valid token will be stored in the cache, okay? And next time whenever you user trying to log in, the web will ask the token from the cache and see if the token is available in the cache, and if it is available then it will not make any API call, okay? It will access the token from there. For some reason if it knows the token is then again we get back to this flow where

### 00:22:08 · Speaker 1

we would make a first we would make a call to we will check from server and we will get back and we'll check from server we'll store it in the cache and we'll use. So now the very important thing to know is like how many how many tokens are actually involved. So again there will multiple implementation one of the most common implementation I'll tell. So there will be two tokens one is authorization token another one is access token. Okay. Access token will usually last for a very long duration of time. So whenever you log in the first you will get one token.

### 00:22:38 · Speaker 1

using that token you're going to make an API call and you'll get an authorization token. So whenever you log in the first token the back end sends will be access token. Using access token you'll get an authorization token. Authorization token usually have a time stamp depending on the different website but let us consider like like one hour of validity. After one hour auth token is expired and using the access token you make an API call because your back end cannot be reached without any valid token, correct? So you keep getting the access token using the you keep getting the authorization token using the access token, okay? And then

### 00:23:08 · Speaker 1

will be a time when your access token also will expire like usually the access token will expire in a long after long duration it could be like ten days twenty days or thirty days depending on the sensitivity of the website or how critical information we are being storing okay when the access token is expired lot of website log out the user and you have to freshly log in and the process continues some websites whenever access token expire right even in that time they will have a separate APO call to get the access token so they get back the access token and then they get the authorization token and then

### 00:23:38 · Speaker 1

process continuous. And lot of these websites how they handle this is they will have a centralized place for making the APA call. So we call them interceptors or like one particular library for making APA call. All the calls will be usually going through there and whenever token expiry happens both access token and authorization token, these services or interceptors make sure they call the calls are waiting and they get a fresh token and then they will like they will fast follow all the APA calls that are been pending, okay? This is how an authorization entire authorization flow can be handled.

### 00:24:08 · Speaker 1

Again multiple different ways are there if how you are handling in your organization mention that in the comment section. If you are not already subscribed to my channel Career with Vasanth please subscribe. In case if I missed answering some of the important question that you wanted to know please mention that in the comment section I will answer. Thank you so much for watching. Catch you in the next video.
