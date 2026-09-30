---
id: gN8LQTff21g
title: 🔥 What is frontend System design ?🔥 | Everything you need to know about frontend
  HLD [2022 Edition]
date: '2022-10-04'
url: https://www.youtube.com/watch?v=gN8LQTff21g
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ UncommonGeeks is a Youtube channel dedicated to helping candidates clear their\
  \ interview. There are close to 70 videos and new videos will be uploaded every\
  \ week. If you're seriously preparing for interviews and looking for tips and tricks,\
  \ please subscribe to my channel and press the bell icon.\n\nInterviewPreparation\
  \ series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nMedium Blog https://mevasanth.medium.com/  \n\nFollow me onLinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\
  \ \n\nGithub Repository that contains presentation: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript/tree/main/Frontend%20System%20Design\n\
  \nJavaScript Custom implementation|polyfills  introduction: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s"
author: careerwithvasanth
duration: 00:20:40
model: saaras:v3
transcript: true
---

# 🔥 What is frontend System design ?🔥 | Everything you need to know about frontend HLD [2022 Edition]

## Transcript

### 00:00:00 · Speaker 1

So very very important thing to notice here is front end front end high level system design doesn't involve any coding even for that matter back end also high level system design doesn't involve any coding. It only involves a designing. So where you have to address lot of challenges that a particular product might face and how you gonna solve that. For example now if you can take an example of Zerodha. So Zerodha has okay for foreign audience probably who are watching the video Zerodha is an this is a stock market broker application.

### 00:00:30 · Speaker 1

where you can go and buy and sell the stocks. So, whereas in Zerodha, let's say, whenever you open the application of a web or mobile, every time, let's say you open a particular stock called Apple or Amazon or in India Reliance, you open, you'll be keep seeing that the movement of the stocks, like it is dipping, it is increasing, etcetera.

### 00:00:54 · Speaker 1

Hello all, welcome back to Uncommon Geeks. Myself, Aasanth. I hope you all doing well. In case if you are seeing me first time on the internet, I'm a content creator. I help people to clear their interview. I have made lot of beautiful series in the past which has been appreciated by many. The link to those series is somewhere on the screen also in the description section. So in this video specifically, I'll be discussing about one of the most requested topic of most requested topic. So that is people have asked me on LinkedIn, people have asked me on my YouTube, people have asked me on Medium. Like wasn't there are very

### 00:01:24 · Speaker 1

very few material on the system design of the front end and these questions are very frequently asked in the premium companies whether it's Amazon, Facebook, Google, etcetera and we don't know what is the direction, how we need to prepare for the front end system design and for a very long duration of time people had thought front system design means back end. Front end has no system design as such, correct? But it was a myth. Actually there was a front end system design always. I was involved from the beginning in the designing process of the front end and the questions were always asked to me in lot of interviews. I personally have attended many front

### 00:01:54 · Speaker 1

front end system design interviews. So I decided to summarize all those important things related to the front end system design and make one detailed series. So I'll be designing very popular systems like YouTube, Zerodha, some e-commerce applications throughout the part of this series. So where I'll explain step by step what is front end system design, what are the challenges that different front end system face and what are the ways with which we can solve them. So this series is not just for the interview clearing, this also will definitely help you to grow as a developer, okay? So but this particular video I'll be explaining

### 00:02:24 · Speaker 1

crux of the system design so that I don't have to repeat it in every video. So you have to watch this video till the end to understand what is system design, what is front end system design and what you as a developer must know whenever you are asked certain questions in the interview are also as a part of your day to day activities in the system design, okay? Without wasting further time, let's get started.

### 00:02:44 · Speaker 1

So, I have prepared one simple presentation to explain what is system design and what is front end system design in detail, okay? The first question is what is system design? Before we understand what is front end system design, we need to understand what is system design, okay? So, system design is the process of defining elements of a system like modules, architecture, components and their interface and data for system based on the specified requirements, okay? So this is a I definitely not a definition given by me, I've taken it from somewhere

### 00:03:14 · Speaker 1

on the web. But in very simple words, system design basically refers to designing the entire system. Okay? In simple words, let's say you are building systems like Twitter, Facebook, or Amazon e-commerce website. So this is a very, very big system, very complex system, correct? So where there are a lot of entities involved, like for example, simply if you take an example of let's say now Twitter. So Twitter has a lot of user base who go and create the Twitter Twitter particular

### 00:03:44 · Speaker 1

tweets on the Twitter board. So there are many many other companies which use Twitter as a source of their support. Like for example Ola, Uber, you can raise tickets in Twitter. And there'll be obviously one back end dashboard which we call admin dashboard for Twitter to handle lot of activities that are happening on Twitter. There'll be somewhere lot of algorithms, machine learning algorithm that is running on the whatever the tweets that are happening to understand the sentiments. Some algorithms are running on the post to determine which posts are something malicious which has to be removed from the Twitter feed. So there are lot of

### 00:04:14 · Speaker 1

activity simply I gave few example but there are lot more activities happening in a one Twitter application correct so very very complex and a very very big system so this system uh cannot be just coded in one day correct this has evolved over a time so before you write even a single line of code a system has to be designed either in confluence or there are lot of different tools where it it you show a pictorial representation of different modules how they interact what they do so this is on a very large scale of system

### 00:04:44 · Speaker 1

design. So, but before as a like I mentioned Twitter as a very big entity itself cannot be designed, correct? So because it's very big. So they generally divide the big system into two main parts of system design, okay? One such part is high level system design.

### 00:05:01 · Speaker 1

high level system design commonly abbreviated as HLD. You might have listened your back end friend saying today I have a HLD interview or LLD interview which I'm going to explain in a while. So where the high level system design is a general system design. In simple words it refers to overall design of a system and describes the overall architecture slash description of any application. It also called system at a macro level so very high level. So what are the possible things that generally high level system design contains? For example, let's build Twitter. Let's build some e-commerce

### 00:05:31 · Speaker 1

application. Let's build YouTube, let's build Zerodha. So all these are a popular examples of high level system design where you do not have a what you call very shorter scope. You have a very broad scope here to design the entire system it as it is. So that is called high level system design, okay? So this is this involves very broad level, okay? This is not generally prepared by the developers. This is prepared by the project managers, product managers and the architects who know what a system should look like.

### 00:06:01 · Speaker 1

and what how different systems interact. For example, if you take an example of Twitter, you there is one team responsible for building the UI of the entire Twitter. There is one team dedicated for handling keeping those tweets and showing it on the screen. There is one team which is responsible for running some machine learning algorithms. So there are various different systems, right? So high level system design continues is top level design. How would each team interact? What should be the mechanism of the interaction? How many teams has to be there? All these will happen at the very high level system design. Okay?

### 00:06:31 · Speaker 1

व्हाट इज लो लेवल सिस्टम डिजाइन, सेकंड पार्ट। सो लो लेवल डिजाइन इज अ कॉम्पोनेंट डाइवेट डिजाइन प्रोसेस दैट फॉलोस अ स्टेप बाय स्टेप रिफाइनमेंट प्रोसेस।

### 00:06:40 · Speaker 1

This process can be used for designing data structure, required software architecture, source code and ultimately performance algorithm. So in very simple words, low level system design is a small modules of the high level system design. Let's say you want to build Twitter now, what is the low level system design? Let us just take the Twitter feed, okay? Twitter feed was can be again another high level system. So in that there what can be the low level systems? For example, the mechanism of tweeting. So you you enter certain things, correct? After certain characters it has to be

### 00:07:10 · Speaker 1

limited. You can no longer enter after a particular number of characters, correct? And this tweet has to be stored on somewhere on the back end. So just the mechanism of entering the tweet and saving can be one one system, correct? Or for example, if you take an e-commerce application. So where you have a carting process, correct? Where elements get added to the cart and whenever you click on the cart, you see a list of elements. So this just the cart, whatever elements getting added to cart and on click of it, you're showing the list of the elements. This is one small unit of an

### 00:07:40 · Speaker 1

entire e-commerce application, correct? So designing a meaningful units of the high level, high level system is called as the low level system design. Okay? Now.

### 00:07:51 · Speaker 1

Before I process further, I'll let me give you some examples how they'll be there for the front end system design. Okay? So, front end system design as in so high level system design what can be asked the questions whatever I already said. They can ask you design YouTube, design Zerodha or design BookMyShow, design Netflix. So all these are the very high level system design questions. So very very important thing to notice here is front end front end high level system design doesn't involve any coding even for that matter back end

### 00:08:21 · Speaker 1

also high level system design doesn't involve any coding. It only involves a designing. So where you have to address lot of challenges that a particular product might face and how you gonna solve that. For example now if you can take an example of Zerodha. So Zerodha has okay for foreign audience probably who are watching the video Zerodha is an just broker this stock market broker application where you can go and buy and sell the stocks. So whereas in Zerodha let's say whenever you open the application web war mobile

### 00:08:53 · Speaker 1

every time let's say you open a particular stock called Apple or Amazon or in India Reliance you open, you'll be keep seeing that the movement of the stocks like it is dipping, it is increasing etcetera. So to show this graph every second you get a data on the UI, correct? So how you gonna plot that graph with effectively without causing any rendering problems to the other. In a very high performance way you have to do this, correct? What are the different ways in which you can do this? So this will not be come under low level design. This has to be architected in the

### 00:09:23 · Speaker 1

high level only. How you gonna make sure this will doesn't affect the performance. Correct? So whenever comes to low level system design, they think how to design that graph. How to make sure that variation happens fine, like dipping and increasing, all those things will comes at the low level system design. Okay? Now, so this is about the without interview I'm talking. If you're working in a company, what high level system design means to you and what low level system design means to you. Now, from the company or from the interview point of view, what high level system design means I'll go next. and as a part of this interview

### 00:09:56 · Speaker 1

I will as a part of this, sorry, not the interview, as a part of this series, I will be mainly explaining about the high-level system design because with my experience of giving and taking the interview, there is very few instances where front end has a low-level system design because low-level system generally doesn't, low-level systems also doesn't involve a lot of coding. They generally have how you're going to do the folder structure, how you're going to modularize certain activities. So these are something that is in a low-level system design. Mostly, this can also be tested in the machine

### 00:10:26 · Speaker 1

machine coding ground. I think hope you all know what is machine coding. Machine coding in simple words is nothing but building a some simple UI like design basic outlook or design basic comment section where each comment can be added to the sub comments etc. So these are all machine coding sample questions. So there itself most of the time this low level system design kind of questions are asked and assessed. Okay? So front so low level system design is not so much asked in the interview for the front end developers. So in this entire series we'll be sticking to the

### 00:10:56 · Speaker 1

high level system design. Okay? Now, without wasting further time on the explanation, let us get straight into the interview process. What questions will be asked or what is the pattern of high level system design in the front end? Okay? So, I've created this slide which explains that in very much in detail.

### 00:11:13 · Speaker 1

First thing that will be asked is the requirements. Okay? Let me give you a simple example. Let's say you are building again a system like probably Twitter. So, they'll ask you build a Twitter in front of system design. Now, requirements are generally into two categories, functional and non-functional. Okay? What is what are functional requirements? So functional requirements basically contains information like on the functionalities, for example, designing a Twitter. So you have to build a UI to design that, you have to build a UI to add the add the tweets.

### 00:11:43 · Speaker 1

Then you have a systems like checking the feed or going to profile and checking the you're seeing your settings or whenever you scroll you get an infinite scrolling, correct? So there are many functional requirements as such in the sub modules. For example if you take YouTube example, you have a search functionality, you have a functionality to watch the news, you have a functionality of adding a comment, you have a functionality of live streaming, correct? So there are different things of functional requirements. So whenever they'll ask you how the interview goes is they will come up with some of these points.

### 00:12:13 · Speaker 1

So whenever they say system, you have to start listing these functional requirements. And then you have to also list some of the non-functional requirement. What is non-functional requirement? For example, you're building a web application for Twitter itself, let us take an example. So how you make sure that is adaptive for um mobile and the

### 00:12:29 · Speaker 1

web, correct? So that is a non-functional economy adaptability, then probably you have to make sure how caching, what all you're gonna cache on the system, correct? To make the things very, very fast. And what are the things that you make sure on the performance? What are the things you make sure on the security? What are the things that you're gonna do on the CICD pipelines? So there are a lot of non-functional requirements and there are functional requirements. You have to list them. Now let me ask you a question, why this is important? Why this is very, very important is whenever a feature is given to you, what is your

### 00:12:59 · Speaker 1

ability to come up with a different uh things that might be part of system. Obviously there will be product manager system and such architects at a higher level who come up with that. But you as a developer when you go to the next level you should be have a mindset of contributing to the overall system design, correct? So when you can contribute when you have a thought process. So you have to come up with a different requirements so that whenever you given that system tomorrow whether in your company or after you get hired. So you are someone who will actively contribute for the requirement like this can be done so that user will be happy.

### 00:13:29 · Speaker 1

So this can be this feature I don't think this is of any use. This can be removed, correct? So all those things you'll be able to suggest if you are having that mindset of the system design. So this will be asked.

### 00:13:41 · Speaker 1

See, I hope you are enjoying the video. We are almost halfway through the entire video. If you are liking the video, please just like this video on my YouTube channel and do not forget to add a comment whatever you are feeling so far. The reason I say this always is more likes and comments video appears for more people. More people if my video goes then there is a high chance that I could help candidate to clear their interview which will help my the main main motto of my YouTube channel. So please like and comment and if you are not subscribed, please subscribe to my channel and press the bell icon so that you get immediate notification as soon as I upload a video. After functional requirement

### 00:14:11 · Speaker 1

non-functional requirement, we have section called scoping. So what is scoping? So let's say you have we listed ten things that a YouTube system has and ten functional and ten non-functional requirements. Definitely in a forty minutes interview where first ten minutes or ten fifteen minutes are generally taken for the introduction and the basic discussion. Forty minutes is meant for your design. In that duration, you definitely cannot build all the features that you have discussed, correct? Or build as in here, definitely cannot explain all the features that you have listed. Interview are generally

### 00:14:41 · Speaker 1

certain things to ask in the interview like from the high level system design from the general and functional requirement from the functional and non functional requirement interviewer will ask a specific sections that he is quite interested let us take an example of e-commerce application he might interviewer might ask you to design the the shopping cart page or so interviewer might ask you how you gonna update the that same particular one particular page that list all the different components all the different e-commerce all the different products

### 00:15:11 · Speaker 1

See, you might have seen whenever you click on Amazon, it goes to detail screen. The detail screen is quite static for different products. But there is certain variations in it. Like some things are applicable. Like for example, you are taking a shirt, there is a size section will appear, correct? But for example, if you take some mobile, mobile, there will be some color sections will come. For some thing else you pick, some other options will come. How you add this dynam, dynamicities to that particular page, correct? So this kind of certain sections will be picked from your whatever the functional and non-functional requirement you gave in this.

### 00:15:41 · Speaker 1

scoping section. So who decides the scoping? Generally, the interviewer himself will decide the scoping and tell. So these are the things, Vasanth, you have to design now, okay? After that, we we have another thing called component architecture.

### 00:15:54 · Speaker 1

So what is component architecture here? So it involves building of certain components. So don't think on the code side. You don't have to build. You have to add the boxes to explain how you're going to design. For example, now I gave a simple example, right? The detail screen. So you're going to add a box. Don't worry, I will explain all these things whenever I pick those in in my upcoming videos. This video is just an introductory. So where you add a box and inside the box you add a particular, this is where item listing happens. So this is the where all the description related to the product will be there. And

### 00:16:24 · Speaker 1

again you will draw things things you where you have a area for adding the dynamic things. So what all dynamic things can be possible. All those things you draw and explain in the this one component architecture. This is very very important. But there are companies who do not they don't ask you to design that particular what I can it's not a design actually. It's just where you do on a black and white and you explain this how the system is going to be. Okay. So some some companies do not expect you to do that. They just have certain problems that that page is facing.

### 00:16:54 · Speaker 1

and how you're going to solve that. Okay? For example, the same thing that I mentioned. There are every product has different set of options in the description, correct? How you're going to solve that. So they'll give you certain scenarios, like I mentioned, shirt has a size, mobile has a color, some other elements have some different as some different informations. So how you're going to tackle that? How you're going to do the UI for that? Okay, this question they'll have and they'll ask you, throw it to you. And you have to come up with a very optimal design, how you're going to do that. Without without the component architecture.

### 00:17:24 · Speaker 1

architecture you just can add some boxes to define like this is my description section. Here is how I'm gonna divide different description section depending on one condition I'm gonna redirect to like this etc you can explain okay don't worry I'm gonna explain all of this pretty much in detail but I'm just giving an example okay.

### 00:17:42 · Speaker 1

After all this, generally they also have a section called text tag, okay? So text tag can come right after the scoping or text tag can also come after the component architecture, okay? So what is the text tag that you're going to pick for this project? So probably somebody might use just the HTML and JavaScript, somebody might use React, somebody say Angular. Whatever the system, whatever the text tag that you propose, you should have a competitive advantage. So you should if you say you're using React, you should tell why you're not using plain HTML and JavaScript and why you're not using the Angular.

### 00:18:12 · Speaker 1

same applies. Let's say you use angular HTML and JavaScript, you must be able to tell why you are not using the other. For this to do, you should have a you should study different systems, like what are the pros of a system, what are the cons of a system, why certain systems cannot be scaled after a point of time. All those things should be present in your mind so that you can pitch in all those things. Okay? After this, there is something called API design. Some some companies do that and some companies don't do. So these are the four main blocks which I have seen are very common across system design of different interviews, where requirement, scoping,

### 00:18:42 · Speaker 1

component architecture and the text stack. Okay? So now, before I make my next next set of videos, what I expect you to know is, let just go and look at different systems now. Now you know what the what all the things that is part of the interview, correct? Requirement, functional and non-functional, scoping, from that requirement, pick certain things that you think are competitive, component architecture, so how you're going to design that component, uh then the text stack. So every system that you're daily using, it could be

### 00:19:12 · Speaker 1

mobile or web that doesn't make much difference. Let's say you're using Uber now. What are the requirements? What is the functional requirements? What is the non-functional requirement? What is the scoping? Pick certain things, everything you cannot pick. So pick certain features, component architecture, how you're gonna build that particular UI. Then the text stack. So will you use if it's a app, you're gonna use a hybrid or native. Why hybrid and why not native? Correct? All those things you should be able to propose and so now next time onwards, when every time whenever you look at a system, think it from the point of this architecture, okay?

### 00:19:42 · Speaker 1

next video of mine will be out in couple of days where I explain very much in detail about the YouTube architecture. Okay? Probably whenever you look at it you will get more idea how the YouTube front end system design is been built. Okay? Thank you so much for watching. That's all about this video. Please subscribe to my channel and press the bell icon. The reason for that I already said. I'll be uploading more videos about the front end system design. Whenever I upload you should not be missing those videos. Okay? So please if you are not subscribed to my channel subscribe and press the bell icon. Add a comment whatever you felt about this video. Like the video so that

### 00:20:12 · Speaker 1

it is appearing for a lot of a lot of people and share the video to your friends so that they also get can can get benefited. I'll be writing a lot of front end front end interview preparation articles on my medium. Link to my medium is in the description. Please follow me on medium and read all the articles. And a lot of all my search code is present in the GitHub. Even this presentation will be present in my GitHub repository. Go there and download the presentation. You can use it for your own if you want to present something or about the system design of the front end. Okay? Thank you so much for watching. Catch you in next video.
