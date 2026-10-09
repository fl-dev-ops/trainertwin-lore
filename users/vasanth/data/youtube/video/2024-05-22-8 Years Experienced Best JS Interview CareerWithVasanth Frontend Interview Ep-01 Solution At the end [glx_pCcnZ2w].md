---
id: glx_pCcnZ2w
title: 8 Years Experienced Best JS Interview|CareerWithVasanth Frontend Interview
  Ep-01|Solution At the end
url: https://www.youtube.com/watch?v=glx_pCcnZ2w
date: '2024-05-22'
duration: 00:24:23
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 3
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
---

# 8 Years Experienced Best JS Interview|CareerWithVasanth Frontend Interview Ep-01|Solution At the end


## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to career with Vasant YouTube channel. Previously this channel was known as uncommon geeks. My name is Vasant. So with me today I have Kriti Suman. So this is a session where we are primarily spending on the mock interviews. So in this particular session, I'm going to take a combination, primarily a JavaScript questions I'll be asking. Kriti already has seven plus years of experience. Maybe I would end up asking some couple of software engineering sort of software development or software engineer sort of questions as well. Okay. And without wasting further time, let's get started. Kriti, if you can introduce yourself.

### 00:00:29 · Speaker 2

Yeah, sure. So I have total 7.0 one year of experience and totally I'm working in the Angular framework and I started from Angular 2 and right now it's an Angular 11 and apart from this I'm just working in the banking domain and leading the team as well and I have sorts of the knowledge in the JavaScript, Node.js apart from the Angular.

### 00:00:52 · Speaker 1

Wonderful. Wonderful. Yeah, Kirithi. Kirithi, let us let me start by asking a very simple question. Okay. So in Angular application, I'm very sure you might have built something for the authentication flow. Correct. I'll ask you only two flows, whether you built it or not, but it's very common interview question where a user logs in to your website and after login. So basically, next time, let's say they close the tab and open next time, definitely will not ask them to log in again. Same how Facebook, YouTube, Instagram, everything works. As long as you're logged into

### 00:00:52 · Speaker 2

Wonderful wonderful

### 00:01:22 · Speaker 1

the application you continue to login correct can you just explain me this entire authentication flow kruti how do we how will we achieve this i tried presenting a whiteboard would you like to draw the basic architecture here

### 00:01:37 · Speaker 2

Sure

### 00:01:38 · Speaker 1

Yeah, thank you

### 00:01:39 · Speaker 2

So suppose that this is the uh page where uh I am just creating a login uh page basically

### 00:01:46 · Speaker 2

It's a login here

### 00:01:48 · Speaker 1

That is fine yeah and I'm primarily interested in the different elements that would interact with each other like it was the caching the back end I'm interested in like which all system in how they interact yeah

### 00:01:50 · Speaker 2

Checking out

### 00:01:58 · Speaker 2

So from here we are just making some data to our caching moment, cache controller. And it is not here like that simply because whenever we are just passing some data from this component, we are also using the salt encryptions there. So we are encrypting our passwords.

### 00:02:19 · Speaker 1

Mm mm

### 00:02:20 · Speaker 2

And that passport we are loading in the our cache systems. And in the cache systems, we have some token expirations session as well. So I'll provide some token here and with some timeline.

### 00:02:35 · Speaker 2

Once it is faced the cache it will go to the my server side So server will have to validate whether the token is the validity or not or expiration is there or not So that cache will be stored there. So suppose second time again I am coming to my login page and since that time I don't have a cache right. So if before sending my data directly to the server through the my browser is it will first go and check in the cache whether the data is available in there or not

### 00:03:05 · Speaker 1

Correct correct

### 00:03:06 · Speaker 2

So it will not repeatedly every time call the server API again and again. So it will stop here itself. If that is suppose expired, it doesn't mean that it will again call the server because it's expired. Then it will just try to give some pre-flight XHR to this guy. Pre-flight.

### 00:03:26 · Speaker 3

No problem

### 00:03:29 · Speaker 2

So this pre-flight XR and it will just try to knock the door on the server side, whether the data is available with you or not. So it will again, because this data is directly integrated with the CAS system as well, so the server will respond to this CAS systems. And from here, as we are using the Google Chrome or the V8 engines, so it will directly interpret with this CAS only. So it will not go to the server directly. That's how we are handling it.

### 00:04:00 · Speaker 1

Sure. So, Kriti, like I'll try to summarize. Okay. So, we have a website. Okay. So, and whenever user tries to log in. Okay. Let's say this is a login button. As soon as user tries to log in.

### 00:04:06 · Speaker 2

And

### 00:04:12 · Speaker 1

what we are doing is as soon as they log in so basically you we are making API call getting the user information correct and let's say you're getting some token that token you're sure storing it in the cache system correct

### 00:04:24 · Speaker 1

This is a cache where you are storing. Okay. So you're storing this cache. So next time, let's say user has closed the tab and opened the tab next time. You will check whether in the cache whether the token is available. If token is available, then you will take user directly to some login screen to home screen.

### 00:04:24 · Speaker 2

So this is a cache

### 00:04:28 · Speaker 2

Actually next

### 00:04:39 · Speaker 1

Correct? Home or the home is just an indicator here, like wherever your core of the application, correct? So there you will take the user whenever you have a valid token, correct? Let's say the token is expired. Whenever the token is expired, so you are saying you will make an API call. Am I right? Like pre-flight user.

### 00:04:40 · Speaker 2

Yeah

### 00:04:45 · Speaker 2

You will take the

### 00:04:55 · Speaker 1

You make an API call, here is the server, correct? So here is server where we will make an API call. Get the token back. Once you get the token back, you're again going to store that in the cache and the process repeats, correct?

### 00:05:09 · Speaker 1

So let us understand yeah elaborate yeah if you want to add any more points you can add

### 00:05:16 · Speaker 2

If here is the again I am to get the token so that will be match here itself again with the one another service we have created so we will just take if the token is available in from the state management or not and we are only updating our expired date or expiry time okay so we know that the token is already available for entire of the system

### 00:05:40 · Speaker 2

That's how it's continues it

### 00:05:42 · Speaker 1

Okay, sure. Again, I'll summarize quickly, Kriti. So I as a user came to your website. I clicked, I entered my email ID password. I clicked on like login. As soon as I click on login, you made an API call, got the token, you stored the token. And next time, whenever I open the application, you checked whether the token is available in the cache, get that particular token. And if it is valid, you are gonna go take me to home screen. If it is invalid, you are gonna make an API call to server to get a new token, correct? So now only question that I have is,

### 00:06:12 · Speaker 1

I've stopped the whiteboard so only question I have is first of all how do you get to know like the token is valid or not next time whenever I open the website

### 00:06:21 · Speaker 2

So in that conditions actually the uh that is why we I just told that pre-flight or exit charge mode right so every time when I open

### 00:06:28 · Speaker 1

So every time when I open you make an API call then with that whether to check whether the book is valid or not

### 00:06:34 · Speaker 2

Yeah, and we are also using some interceptors in our Angular application or entire applications. So that is going to make the sample pre-flight mode access our call. And then it is checking it there itself, whether that is available or not. So we can just expand our expiry time from the front end side, not the back end always.

### 00:06:56 · Speaker 1

Okay so in the overall process Kriti how many tokens are involved one token two token how many tokens are involved

### 00:07:02 · Speaker 2

I think there is only one token per user

### 00:07:05 · Speaker 1

Okay so that is the

### 00:07:05 · Speaker 2

That is the

### 00:07:06 · Speaker 1

Got it. What what is that token you call? Like, what do you refer it as? Authentications and authorization.

### 00:07:10 · Speaker 2

Authentication that is also involved with the authentication only not with authorization things

### 00:07:19 · Speaker 1

Okay sure

### 00:07:19 · Speaker 2

Sure

### 00:07:22 · Speaker 2

So the we generally tell it as a session ID in our term and that is only for help for the

### 00:07:31 · Speaker 2

Authentication purpose

### 00:07:32 · Speaker 1

Okay, sure. Sounds good, Kruti. There are a lot more details required for this. Probably I'll explain if time permits at the end. Okay, but whatever you said so far is not wrong, but there like we can add more clarity into this. Okay, so can you like present your Chrome one window where nothing is opened only like can you open the plain Chrome window? I'll share a online editor link with you and please open this link. Okay.

### 00:08:04 · Speaker 1

So can you tell me the difference between session storage and local storage

### 00:08:08 · Speaker 2

So session storage is just like suppose I have a store my data in here in the session storage and if I will close the my browser or even I close the tab my session is gone already. Okay. And if I will inspect it my session storage data will be not available there. Okay. But in case of the local storage if I will close my system as well and entire Google Chrome as well but still my storage will be a storage whatever the data I have stored.

### 00:08:38 · Speaker 2

It will be available there. Even I will come and log in again, my data will be there.

### 00:08:43 · Speaker 1

Okay, I have two follow-up questions on this. Okay, so session storage, whatever you are storing, is it accessible?

### 00:08:52 · Speaker 1

Even when like multiple tabs are open from the same web application, like for example, this website, what we open is program ms.com, correct? I open the same website in another tab in the same browser. So both the tabs can access the session storage. Got my question, right, Kriti?

### 00:09:06 · Speaker 2

Yeah, I got your point. No, I think in the session storage when I just open my one tab only the data will be available here itself.

### 00:09:14 · Speaker 1

You cannot share this between the tab

### 00:09:14 · Speaker 2

I don't see it this way

### 00:09:17 · Speaker 2

Yeah

### 00:09:18 · Speaker 1

Okay, if audience who are watching, like I always say, the best way to get use of this mock interview is like you try answering whenever I ask a question, pause the video, try to answer and see what is the answer candidate giving so that you get a sense. Yeah, sure. We will discuss, Kriti. Now, another follow-up question that I had also on the local storage. Like you told, local storage is storage. That is like, even if you close the window or even if you restart the system, that storage is going to be always present unless probably we clear the browser's cache, correct? So now the question is, let's say you're not open website like program.

### 00:09:48 · Speaker 1

Ms. Dole

### 00:09:48 · Speaker 2

Yeah

### 00:09:49 · Speaker 1

This website you have not opened. Is there any way without opening that website you can access the local storage things the data that you have stored? Got my question right.

### 00:09:58 · Speaker 2

So yeah, so you are meant to say that from what I understood, you wanted to close the browser and you wanted to access somewhere else, right?

### 00:10:07 · Speaker 1

No no let's say

### 00:10:07 · Speaker 2

No no let's say

### 00:10:08 · Speaker 1

See this program is.com this saved some information in the local storage. Okay. And I closed that that tab I close. I open google.com now. Okay. So is there any way I can access the local storage values that are stored by program is.com? But my question right now I think it is clear.

### 00:10:14 · Speaker 2

I close that

### 00:10:18 · Speaker 2

I need it

### 00:10:24 · Speaker 2

Yeah it's good yeah

### 00:10:25 · Speaker 1

Yeah thank you. Without opening the website can we access the local storage data that was saved or persisted by the website

### 00:10:34 · Speaker 2

Yeah, I think yes, we can get it. Okay. Because our local data will be there and there, right? We have to just only say get the items. So if that is available, we can get it, right?

### 00:10:48 · Speaker 1

Okay, let's say I'm aware of the key with which you saved. Like, let's say we saved the key as like login underscore key. And if I try to get access to that, like localstorage.getitem, login underscore key, just execute that in the inspect, Chrome inspect. You think I'll be able to get that? Got my question. I think I'm clear, Krithi, correct?

### 00:10:48 · Speaker 2

Actually I'm aware of the key

### 00:11:06 · Speaker 2

Yeah yeah yeah

### 00:11:07 · Speaker 1

Okay okay

### 00:11:08 · Speaker 2

I think you cannot get it

### 00:11:11 · Speaker 1

It is tis then you're saying it is stored in the

### 00:11:13 · Speaker 2

Stored

### 00:11:14 · Speaker 1

Yeah we are saying it is stored persistently but you cannot access without opening the website correct

### 00:11:23 · Speaker 2

Yes yes

### 00:11:26 · Speaker 1

So are you aware of call apply bind Kriti

### 00:11:30 · Speaker 2

Yes

### 00:11:31 · Speaker 1

Uh can you write an example for all the three call apply and yeah you can remove whatever is here and write the yes remove everything and you can start giving an example call apply and

### 00:11:42 · Speaker 2

So suppose that uh

### 00:11:44 · Speaker 1

You write it fully then we'll discuss

### 00:11:50 · Speaker 2

So I just have created the two users and I wanted to because that is available in some other function so what I can do

### 00:12:02 · Speaker 2

I can uh

### 00:12:05 · Speaker 2

Think the reference of this print will mess up the

### 00:12:11 · Speaker 2

and then I'll apply with the call method here and then I can just pass the user one or two whatever it is. So this will reference to this with the help of the this keyword actually is happening here.

### 00:12:24 · Speaker 1

Mm

### 00:12:25 · Speaker 2

and uh what the here right i'll forget to mention that this keyword here that this dot

### 00:12:33 · Speaker 2

first name and this dot last name here so it will try to refer this guy and now it is asking which one is referring so this will refer whoever immediate objects are there calling

### 00:12:46 · Speaker 1

Yeah

### 00:12:48 · Speaker 2

So it will give the output like this. And with the help of the apply method and the call method, most things that I suppose I wanted to pass multiple arguments like here.

### 00:13:01 · Speaker 2

I have some kind of like a country as well

### 00:13:06 · Speaker 2

CT as well

### 00:13:09 · Speaker 2

So here I can just pass

### 00:13:13 · Speaker 2

Yeah

### 00:13:15 · Speaker 2

And then Bangalore

### 00:13:18 · Speaker 2

Like this individually elements I can create and I can pass it as an argument, a particular parameter. But in the apply method, what is happening, I can just create one array type and inside that I can just do that. So same thing will happen there. With the bind method, what is happening like same way, it's bind here, but bind is always available for your future reference, not for current.

### 00:13:48 · Speaker 2

So suppose that you wanted to call that functions in the futures so you are you can just only pass some reference to that the bind method

### 00:13:57 · Speaker 1

Okay, sure. So, Kruti, whatever explanation you gave is good. I think most, when I ask in the interview, everybody gives this example only. But you have seven years of experience, Kruti. Tell me the practical use case. When did you use call apply bind?

### 00:14:12 · Speaker 2

was creating one functions okay and then I got to know that I have to create a one utility class of the functions as well but since whatever the items I had here right I'm not so sure what is the argument someone is passing there because that was using some split and rest operator as well so only I came here written functions and then I use the the functions which I'm passing here I use the generate dot apply method here itself so it was taken

### 00:14:42 · Speaker 2

the function as a callback functions and whatever the arguments or parameters we were passing it was referring to this guy again that this keyword with the help of the apply method

### 00:14:53 · Speaker 1

Got it sure sure okay Kriti I am sending a code snippet in the chat section okay copy the snippet and paste the snippet

### 00:15:03 · Speaker 1

in the same window and try to guess the output for the same. And audience whoever watching you can also just look at the snippet and try to guess the output.

### 00:15:19 · Speaker 2

So when I will try to invoke it it should print like this

### 00:15:25 · Speaker 2

For one

### 00:15:28 · Speaker 2

And if I will just try to print it, it should print as a zero because this guy is taking the scope will be the same quantum method here. So again it will become zero.

### 00:15:42 · Speaker 1

Please run the code good

### 00:15:44 · Speaker 2

I'm not sure

### 00:15:45 · Speaker 1

Can you can stop sharing Kati okay So I'm done from my end Kati and uh this is the time where I give my feedback to you But before I give my feedback you have any questions for me like primarily around the interview have any questions

### 00:15:56 · Speaker 2

Now it's all good go far uh very good I am very much interested in this

### 00:16:04 · Speaker 1

Yeah please

### 00:16:04 · Speaker 2

So yeah, I would like to ask more than we can just discuss more on the local store system that you asked.

### 00:16:11 · Speaker 2

Yeah

### 00:16:15 · Speaker 1

Yeah, sure, Kirti. Like, probably if time permits, we can discuss any other topics that I asked in the interview. But let me, this is an important case for me to give feedback to you. And it's also applicable with a lot of candidates who are watching the video. See, primarily everybody who's watching the video, consider a fact, like if you're somebody who's having an experience of more than six years.

### 00:16:27 · Speaker 2

Yeah

### 00:16:33 · Speaker 1

Then you are considered like a senior developer in an organization. So the primary expectation from you is like, how do you basically create a system and manage it? So that is the reason I ask you authentication flow, right? There is no one right way or wrong way. I don't even consider that like a system design, a deep system design sort of a question, but very basic level question, correct? What you explained was not wrong. But there can, there was an opportunity where you could have induced more clarity, like step by step, probably how we can proceed further.

### 00:17:03 · Speaker 1

Okay, so that's a small feedback for anybody who goes for interview or who are having like six plus years of experience. Make sure you go with an extreme clarity about the things that you explain. I'm not saying like you don't know the concepts, but interviewer will have a very short time and within that time frame only they need to judge you. So try to give very crystal clear answers. And then next, so next question like whatever I asked in the local search and session storage, right? So by looking at those answers quickly, like what can we infer is, you knew the concepts. Like for example,

### 00:17:33 · Speaker 1

Like would if I ask you to like question like how to create a session storage, how to create a local storage, you could have created the questions that I asked probably you were not anticipating.

### 00:17:42 · Speaker 1

So where I'm coming from is like my advice to all basically who are watching this video is have the temperament of why in your mind like why basically this is happening. So whenever you keep asking why then only you will identify discover some questions because reading an article or reading an article reading the official documentation or YouTube video may not trigger that. So you should start asking why multiple times. So probably then you will get into that temperament of reading. Okay. And snippet you are able to interpret excellently.

### 00:18:12 · Speaker 1

Nikruti which is good. I think whatever you know, at least whatever you answered so far. So you have clarity on some complete clarity. Some you are having little bit of mediocre clarity. So where I want you to just polish your skills.

### 00:18:26 · Speaker 1

My honest feedback is you tell me if there are any closing questions for our last two minutes

### 00:18:30 · Speaker 2

Uh, like, uh, I just really would like to work more on the authentication authorization since I didn't get a much more chances as from the we are building a product for some other product based company. So we don't have that much control over.

### 00:18:48 · Speaker 1

Got it. Yes. Yes. I understand, Kriti. But like I told you, your experience, these things matter. So even if you're not got an opportunity, please try to learn on your own. So that next interview, when this is asked, you're able to answer and clear that interview. Okay.

### 00:19:02 · Speaker 1

Sure. So, yeah, we are closing the session, Kruti. I hope the session was useful. You like the question that I asked?

### 00:19:08 · Speaker 2

Yeah sure obviously it's very helpful for me and I I can also always practice on those

### 00:19:15 · Speaker 1

on it sure sure thank you so much for joining the session kruti and uh taking the market with me and audience whoever watch the video please like the video if you think it is useful for your friends also share with them if you're not already subscribed to my channel carry with us please subscribe and whatever the question that i asked to kruti in the video i'll try to make a short extension to this video but i try to explain answers to that thank you so much for watching catch you in the next video yeah hello all i'm sure you liked the session with kruti and in this particular video it's a very short video post video basically i'm discussing the

### 00:19:45 · Speaker 1

question that I asked in the interview okay that uh Kriti did not answer properly the first question is the local storage and session storage where I asked like uh the data between session storage in between two tabs is it shared so answer is no the data cannot be shared between the two tabs of the same website let's say you have uh google.com and google.com slash home so in google.com you stored some value in the session storage and you want to access it from google.com slash home you'll not be able to access okay second question I asked is

### 00:20:15 · Speaker 1

local storage the value that you are storing in the local storage can you access it even when the website is not opened yes you can access it use if you know the right keys to the local storage whatever you are storing okay so it is a security concern so if you are storing some information in the local storage make sure you are not storing the sensitive information even if you are storing sensitive information then make sure it has a quite proper expiry date or you also at least you are encrypting it so that somebody some random person is not able to access those

### 00:20:45 · Speaker 1

information okay now the another important question that I asked was the authentication flow okay let me try to uh present a whiteboard and see if I can uh show that okay so like I asked there'll be like your website is here and you have a local storage or a session storage depending on your requirement and you have a server okay so let me name it as like this is your website and this

### 00:21:15 · Speaker 1

is your cache okay and this is your server this is your this is your server

### 00:21:24 · Speaker 1

So now

### 00:21:27 · Speaker 1

Important thing to know here is how actually the authentication would work. Okay, so if I have to draw a line.

### 00:21:35 · Speaker 1

between the three okay first whenever you log in what the what the website will do is it will it will make a call to the server okay and from server it will get back a valid token okay and that valid token will be stored in the cache okay and next time whenever you user trying to log in the web will ask the token from the cache and see if the token is available in the cache and if it is available then it will not make any api call okay it lacks a token from there for some reason if it knows the token is expired

### 00:22:05 · Speaker 1

here then again we get back to this flow where we would make a first we would make a call to we will check from server and we will get back and we'll check from server we'll store it in the cache and we'll use so now the very important thing to know is like how many uh how many tokens are actually involved so again there are multiple implementations one of the most common implementation i'll tell so there'll be two tokens one is authorization token another one is the access token okay access token will uh usually last for a very long duration

### 00:22:35 · Speaker 1

of time so whenever you log in the first you will get one token using that token you're going to make an api call and you will get an authorization token so whenever you log in the first token that backend sends will be access token using access token you will get an authorization token authorization token usually have a timestamp depending on the different website but let us consider like like one hour of validity after one hour auth token is expired and using the access token you make an api call because your backend cannot be reached without any valid token correct so you keep getting the access token using the you keep getting the

### 00:23:05 · Speaker 1

authorization token using the access token okay and there will be a time when your access token also will expire like usually the access token will expire in a long after long duration it could be like 10 days 20 days or 30 days depending on the sensitivity of the website or how critical information that we are being storing okay when the access token is expired a lot of website log out the user and you have to freshly log in and the process continues some websites whenever access tokens expire right even in that time they will have a separate api call to get the access token so they get back

### 00:23:35 · Speaker 1

access token and then they get the authentication token and the process continues and a lot of these websites how they handle this is they'll have a centralized place for making the api call so we call them interceptors or like one particular library for making api call all the calls will be usually going through there and whenever token expiry happens both access token and authentication token these services or interceptors make sure they call the calls are waiting and they get a fresh token and then they will um like they'll fast follow all the api calls that have been pending okay

### 00:24:05 · Speaker 1

This is how an authorization entire authorization flow can be handled. Again, multiple different ways are there. If how you are handling in your organization, mention that in the comment section. If you're not already subscribed to my channel, carry this person, please subscribe. In case if I missed answering some of the important question that you wanted to know, please mention that in the comment section. I'll answer. Thank you so much for watching. Thank you for watching.

