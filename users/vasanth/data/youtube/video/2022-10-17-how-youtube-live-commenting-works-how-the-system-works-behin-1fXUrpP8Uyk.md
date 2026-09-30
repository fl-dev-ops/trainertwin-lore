---
id: 1fXUrpP8Uyk
title: 'How Youtube live commenting works 🔥 - How the system works behind the scenes
  #youtube #facebook'
date: '2022-10-17'
url: https://www.youtube.com/watch?v=1fXUrpP8Uyk
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ #youtube #live #comment #javascript #front #react #reactjs \nUncommonGeeks is\
  \ a Youtube channel dedicated to helping candidates clear their interview. There\
  \ are close to 70 videos and new videos will be uploaded every week. If you're seriously\
  \ preparing for interviews and looking for tips and tricks, please subscribe to\
  \ my channel and press the bell icon.\n\nWhat is frontend system design: https://youtu.be/gN8LQTff21g\n\
  \n\U0001F525 How Youtube System works ?\U0001F525 Frontend High Level System Design\
  \ of Youtube #youtube #interview: https://youtu.be/QJe0cBjlgog\n\nFramework used\
  \ by Youtube for navigation: http://youtube.github.io/spfjs/ \n\nInterviewPreparation\
  \ series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nMedium Blog https://mevasanth.medium.com/  \n\nFollow me onLinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\
  \ \n\nGithub Repository that contains presentation: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript/tree/main/Frontend%20System%20Design\n\
  \nJavaScript Custom implementation|polyfills  introduction: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s"
author: careerwithvasanth
duration: 00:16:39
model: saaras:v3
transcript: true
---

# How Youtube live commenting works 🔥 - How the system works behind the scenes #youtube #facebook

## Transcript

### 00:00:00 · Speaker 1

I'm going to the network section, okay? I'm going to network section and I'm clearing all the things. If you observe get live chat is called once, then get live chat is called again, okay? And the get live chat is called periodically, okay? So, every X interval you are seeing, right? In almost at every second, almost every second I think, the it is it is kind of fetching the new set of comments from the back end and appending it to the existing set of the comment that it already has.

### 00:00:30 · Speaker 1

And after a point, for example, they might have made an array with a limited length and obviously all the old items will go off and only the new items will be remaining.

### 00:00:42 · Speaker 1

Let's go to the design of the second thing that we discussed that is the live streaming, correct? Live streaming has its own set of challenges, how you're going to solve the live streaming etcetera, okay? The that's the reason why I had opened the Aaj Tak live. I don't know whatever they are streaming, I'm not much concerned on that, okay? So and there's nothing like a recommendation to watch Aaj Tak. I just searched any particular live streaming video. Obviously news are the best way to get the live streaming. So I'm opening some news, okay? And I've paused the video long back only. So this you're seeing this live streaming.

### 00:01:12 · Speaker 1

why I'm showing this is in interview also this might happen interviewer might show you this. The reason for that is see one thing that is getting different than the normal streaming is the

### 00:01:23 · Speaker 1

normal video whatever I showed you here is the comment section. Correct? So there are right now around eleven thousand eight hundred seventy six people are watching. And if you observe this, the comments are been flooded like anything. Correct? This looks like an easy problem to solve with help of page and other things but it is not that easy. Okay? So let's say if you want to design the component for the live streaming, it pretty much remains the same as this. There is not much of a difference. Only the added section is the rather having this comment section, it has a live comment section. So component architecture remains

### 00:01:53 · Speaker 1

as it is, okay? Now, so here we have this live streaming and so many comments are be getting populated every second, correct? Tell me what is the approach that you would think in case if you are someone who already know the right approach for this live commenting, please mention that in the comment section, okay? You can mention the video timing and add that in the comment section, what is the right way to use the live streaming, live commenting, if not I'm gonna explain.

### 00:02:17 · Speaker 1

I was discussing about the live commenting. I assume some of you might have already commented like how live streaming live commenting works. If not, let us start discussing certain approaches in the regarding the live commenting. Okay? So,

### 00:02:31 · Speaker 1

what are the what are the approaches that are possible for the live comment? Okay? So, I I'll explain whatever the things that are happening. Basically, there are some ten comments or some x number of comments which are loaded whenever the live streaming video loaded, correct? Further comments are being added in a periodic interval, correct? And as you can see here, you can always scroll up scroll up and read only certain number of old comments, okay? This is the reason why you need to look at the system.

### 00:03:01 · Speaker 1

before designing it. So they are not allowing you to see all the one lakh comments that are happened before what you came or all the comments that are happened in the past. There is certain scroll whatever the scroll they have right in that interval whatever has been commented you can see. For example now it is at whatever let's say it's like one p.m. you are watching the video. All the all the comments that came for example some two hundred comments that came before one o'clock can be seen on the screen. Correct? So how what are the different mechanisms that we can use to solve that are

### 00:03:33 · Speaker 1

So what we can do is, let me just start adding those mechanisms of

### 00:03:40 · Speaker 1

mechanisms of live commenting. Okay? How we can basically achieve it? That's what I mean here, mechanisms of live commenting. Okay?

### 00:03:50 · Speaker 1

So one easiest way is what we you are generally does is polling. Okay? Second is server sent events.

### 00:04:01 · Speaker 1

third definitely is sockets. Okay? I'll explain about each of them and this is the same way how you need to also do in the interview. Okay? List them, explain the pros and cons and tell which approach suits best for you. Okay? So in the polling we also have something called short polling. I'm very sorry if my spelling of polling is not correct. I think it is right. Okay? Short I'm not that expert in English spellings actually.

### 00:04:27 · Speaker 1

long pooling, huh? pooling. long pooling and short pooling. okay. I don't know it is not pooling it could be polling only. okay. Basically I mean I'll explain what I mean so if I made a spelling mistake please correct it, okay. Servers and events have no subsections as such, okay. So what do I mean by polling here is client make a request to server at a consistent interval time or a periodic interval of time, okay. Let's say every five second you make a call, okay. five second you make a call and get the data. Let us quickly see what is happening in YouTube.

### 00:05:03 · Speaker 1

I'm going to the network section, okay? I'm going to network section and I'm clearing all the things. If you observe, get live chat is called once, then get live chat is called again, okay? And the get live chat is called periodically, okay? So, every X interval you're seeing, right? In almost at every second, almost every second I think, it is it is kind of fetching the new set of comments from the back end and appending it to the existing set of the comment that it already has.

### 00:05:33 · Speaker 1

and after a point, for example, they might have made an array with a limited length and obviously all the old items will go off and only the new items will be remaining. Correct? This is the easiest way where you constantly poll and get the data and add it, okay? But there are two different types of polling. One is short polling and long polling. What is short polling? uh you call uh at a periodic interval and back end immediately sends all the new whatever the comment that has immediately. Another thing called the long polling. What is long polling means? Let's say you called the back end but back end doesn't have any new

### 00:06:03 · Speaker 1

comments. That might happen, right? There are many people who are live streaming. And if YouTube cannot uh call back end every one second to get the new set of comments, even in those criteria, correct? Because there may not many new comments. But it will make a call and the back end will wait for a particular interval of time, like fifteen seconds, twenty seconds, twenty five seconds. That is a interval with for which the client waits, okay? For a particular request to fail. After twenty five seconds or else generally what back end does is it will take a request, it will wait for some let's say twenty seconds is when the UI

### 00:06:33 · Speaker 1

considers as the request has failed. After a fifteen second, it will see if any new data is there, whatever it is, it will flush. If there is no new data also, it will flush with the empty array. Okay, this is called the long polling. Advantages of long polling is

### 00:06:46 · Speaker 1

short polling disadvantage you know you call you may not have anything so you are simply consuming a server resource for nothing whenever there are no comments for example for the long polling advantage is you take you are waiting for a significant amount of time definitely there could be a high chance where some comments come and you will return so comparing short law polling and long polling long polling is better in certain areas where you are not expecting something to happen very often okay next thing is the server sentiments so this is very very optimal approach compared to the polling

### 00:07:16 · Speaker 1

server sent events are nothing but server will send a trigger to you and whenever there are triggers you will be making a network call. Okay? So there are different ways with which server sent events can be configured. If you are not at all knowing please mention that in comment section I'll make it but I'll not deviate this video to explain the server sent events in detail. Very simple words there is a trigger from the back end and you UI knows this trigger means I need to call this API it will call and get the data. Okay? So it's very optimal because back end knows when there are new set of comments it will inform the UI and the UI makes a call and gets the data.

### 00:07:46 · Speaker 1

So this is server sent events, very optimal compared to the polling approaches, okay? But it is not suitable in all the scenarios because server sent events will have its own performance problems, okay? Because client will have a connection dedicated in the server. All the clients, we have two hundred billion plus users. If two hundred billion, no, two hundred billion, very huge user base. I think two billion users YouTube has, around two hundred crores.

### 00:08:10 · Speaker 1

If all the 200 crore people, let's say they will not watch at the same time, but let's say just at least 10% of them watch the video at the same time, that is around how many, uh, I think 20 million, correct? 20 million people watching at some time. From 200 crores, not 20 million, 200 crore user if you have, 20 crore people watching it at one particular point of time, then 20 crore connection has to be established with the server, correct? And there are chance where, uh, definitely not 20 crore, whoever is watching the live streaming, those many connections will be established and

### 00:08:40 · Speaker 1

number also will be significantly high for the server, correct? And there may not be any update happening on the server. In such cases, this connection should be wasted. And that resource cannot might have been used for some other things. Obviously, there is a lot of research that has gone into making this video. So please like the video and subscribe to my channel and press the bell icon if you're not already done so. And add a comment whatever you felt so far. The reason for that I always say I have only motto of I help want to help the candidate to clear their interview. So if more likes, more comments video becomes visible for a lot, whenever it is visible,

### 00:09:10 · Speaker 1

a lot. There is a high chance I get more subscribers and the followers. Definitely the there is a high chance I would be able to reach my cause very soon. Okay? So please like and comment about the video before watching the further. Okay? Now, okay? Next we have something called sockets. Most of you know what are sockets. So server difference between server sent events and the sockets are sockets are two way connection. Server sent events are one way connected. Like only the back end will send certain things to UI and UI makes a modification. Sockets are nothing but two way connection. The best example are the

### 00:09:39 · Speaker 1

uh messaging. Whenever you're doing messaging in the WhatsApp or whenever you're chatting on the web with some support and all you'll do right? Every site a lot of sites have a support central where you can do the live chatting. All those work actually on the sockets. Because client also can send certain things to a connection and the server also can send back certain things to connection. It's a two way. Okay? Servers and servants are one way. They're only back end will send certain things to the client. So these are the three different approaches with which the the we can get the comment from the live commenting we can enable live commenting.

### 00:10:09 · Speaker 1

in the YouTube. This is very good. Interviewer will be definitely happy if you are able to approach, explain all these problems. Next question that interviewer will ask is, Vasant, what is the approach that you suggest for us? Like, if you are building YouTube now, which approach you are gonna go? Whether short polling, long polling, server sent events in the sockets. Very first thing, I'm not gonna go with sockets, okay? Because sockets are very, very costly compared to all the things because you are establishing a channel and this is not like a charting. uh This is just a one way. Somebody sends a comment, somebody replies there and

### 00:10:39 · Speaker 1

Again you have to send a comment. It is like group chat. Everyone messaging in one direction. It's not like a two way. Like you sending, it's going to server coming back, no. Both are sending to one server and they can both can see the comments in the live. So I will not go with the sockets. So server send events.

### 00:10:53 · Speaker 1

I might go. So server sent events are also good, but considering the scale of YouTube where we have billions of users, server sent events also will consume lot of energy with the help of by making the connections. So many connections are open and sometimes these connections could be meaningless. Simply server utilization is high, so I may not go with the server sent events also. I will go with polling. Don't think I'm biased looking at whatever I showed you. Obviously you also felt like YouTube is doing a polling at every second, correct? Why why I'm selecting the polling is, so

### 00:11:23 · Speaker 1

You already know what is short polling and long polling I've already explained. Polling, I will not go with this typical polling where I call it every one second and get. No, I will not do that. I will use a algorithmic way of determining the duration. Like for example, Aaj Tak, whatever I was saying, there are for foreigners who are watching, there is lot of YouTube, there are lot of foreign news channels which are being streaming. Some channels might have very limited comments that are happening on a day-to-day basis. Some live streaming, some channels, some news channels

### 00:11:53 · Speaker 1

present live streaming on YouTube might have limited users and limited comments. Some YouTube channels with that are live streaming, news channels that are live streaming might have huge user base and so many comments. So I'll do a short polling itself but the whatever the duration with which I make a call is not predefined.

### 00:12:09 · Speaker 1

So that that is something that is determined depending on the video which I'm watching and this number is calculated by a machine learning algorithm by watching that channel periodically. Definitely there will be a default value when a new news channel starts streaming or new live streaming comes. But after a point whenever the algorithm becomes smarter it will tell me this is the duration with my lot of analysts in the past this is the duration with which the live comments need to be updated and that duration I'll do a short polling. That seems better option for me considering the huge scale of things like the YouTube.

### 00:12:39 · Speaker 1

Okay, so this is the another problem that I want to discuss in live streaming. Last thing that I want to discuss here is, Vasant, what, how YouTube live streaming is working? This will be generally asked in the interview, like, what is the protocol with which the streaming is happening? Actually, there are many protocols for the live streaming, correct? Most popular ones that everyone aware of is a WebRTC, correct? So, real web, web real-time communication, RTC stands for. One of the very, very popular framework, but only problem with WebRTC is, let me just note down so that you guys also note it. properly live streaming

### 00:13:13 · Speaker 1

protocols. Okay? One is WebRTC.

### 00:13:18 · Speaker 1

Okay, and the second one, second one is RTMP.

### 00:13:23 · Speaker 1

third one is HLS. I've written certain things on the left so that I won't miss it out so I'm mentioning here. So these are the three popular live streaming protocols that are available. Vasanth, is it necessary for me to know these things before attending the interview? I would highly recommend you need to know. Okay? Why? Because you have to always explain the pros and cons of an approach and rule out some approach and take one approach like I mentioned here. Correct? So it's always essential for you to pick all the popular systems and analyze the popular system and take a note and explain that. Correct? So three popular systems are there, WebRTC, RTMP and HLS. So WebRTC like I said it is open source.

### 00:14:01 · Speaker 1

and it uses UDP. Okay? If you don't know what is UDP, user diagram protocol. Basically, it's a connectionless protocol and there is a high chance where some packets are lost in this particular uh with with UDP based one. Okay? And HLens is uh very easy definition, HTTP live streaming. Okay? So this is built by Apple.

### 00:14:22 · Speaker 1

in two thousand eight, okay? So definitely as you can guess I have already read about all these protocols in the past. I would advise you also need to read like this whenever you are practicing for the system design, okay? RTMP is real time messaging protocol.

### 00:14:38 · Speaker 1

real time messaging protocol. It uses TCP. Okay? Reliable.

### 00:14:45 · Speaker 1

fast. Okay? It's reliable and it is fast, okay? compared to other frameworks, okay? And it is meant for uh I mean it is it's not like a very old one. It is newly designed for meeting the modern day needs. So obviously you know which which protocol that I'm going to pick, I'll be picking the RTMP. In fact, you YouTube also uses the RTMP protocol for the live streaming purpose. Not the live streaming, even the normal streaming in YouTube also happens with the help of RTMP, real time messaging protocol. So what are protocols? You very well know it's just a set of

### 00:15:15 · Speaker 1

rules that is agreed between the client and the server. Every protocol will have certain set of rules which will make it to be fast, slow and certain different aspects. So and also very important thing to note here is RTMP uses the TCP. Okay? TCP is a connection oriented protocol. So a connection is established between the client and server. So no packets are lost, more security and even if you due to your internet issue if you lose certain packets, after you get those packets whenever your internet is up, you there is a chance where you can combine them on the UI and you can show it to the user. So because of all

### 00:15:45 · Speaker 1

reason RTMP is recommended for even it is used in Facebook live, YouTube live and maybe other lives. These are two systems I've clearly studied. Other systems I don't know but lot of live streaming apps on the web might be using the RTMP as a protocol. So YouTube also using the RTMP protocol. See if you explain all these things to interviewer like how I explained, what are the mechanisms of live commenting, what are the problems with the pagination with the commenting. If you explain all these things to interviewer he'll be terribly happy, correct? Like he knows so many things.

### 00:16:15 · Speaker 1

and he's taking each approach one by one and he's uh scratching why this is not suitable for this application and why this only need to be used. He'll be very happy looking at your knowledge about a particular um system design. So much he already know, definitely he'll be able to contribute whenever he's inside the company, okay? So, after all this, there is one last thing that I want to tell.
