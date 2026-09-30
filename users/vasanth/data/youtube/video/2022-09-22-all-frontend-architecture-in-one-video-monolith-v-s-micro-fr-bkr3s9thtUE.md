---
id: bkr3s9thtUE
title: 🔥 All frontEnd architecture in one video 🔥Monolith V/S Micro frontEnd V/S Monorepo
  | which is best ?
date: '2022-09-22'
url: https://www.youtube.com/watch?v=bkr3s9thtUE
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ UncommonGeeks is a Youtube channel dedicated to helping candidates clear their\
  \ interview. There are close to 70 videos and new videos will be uploaded every\
  \ week. If you're seriously preparing for interviews and looking for tips and tricks,\
  \ please subscribe to my channel and press the bell icon.\n\nInterviewPreparation\
  \ series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nMedium Blog https://mevasanth.medium.com/  \n\nFollow me onLinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\
  \ \n\nGithub Repository that contains presentation: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript/tree/main/MAANG%20Series/FrontEnd%20Architecture\n\
  \nJavaScript Custom implementation|polyfills  introduction: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s"
author: careerwithvasanth
duration: 00:27:57
model: saaras:v3
transcript: true
---

# 🔥 All frontEnd architecture in one video 🔥Monolith V/S Micro frontEnd V/S Monorepo | which is best ?

## Transcript

### 00:00:00 · Speaker 1

So you are everybody wants to get into a premium company so you are in a premium company interview round. And the interviewer ask question this is the something that is we are building so which architecture do you propose you want to go us with a monolithic microfrontend monorepo which architecture do you prefer?

### 00:00:14 · Speaker 1

I am like, what the hell? Mono front end, micro front end, monolithic. I don't know and still I want to get placed into a very premium company. So if you want to get into premium company, you should learn the architecture as one of your fundamental skill set.

### 00:00:34 · Speaker 1

Hello all, welcome back to Uncommon Geeks. Myself, Vasanth. I hope you all doing well. In case if you see me first time on the internet, I'm a content creator. I help people to clear their interview. I made lot of beautiful series in the past which has been appreciated by many. So in case if you have not watched my previous series, those series will be available somewhere on the screen also in the description section. Please go ahead and watch. If you are preparing for any sort of interview, definitely it will be beneficial for you. Now without wasting further time, let's get started into this video's topic that is very, very important. See, leave leave the part of interview preparation other things.

### 00:01:04 · Speaker 1

A very important aspect of software developer lifestyle is to architect a product. So coding is one part, correct? So coding part like somebody product owner will give you requirement or your manager will tell you some requirement and you do it, that is one part of engineering. So that is something you know what needs to be done and you do it. But very core skill of a developer is architecting. So how you're gonna architect a product so that you will foolproof it, like in future you will get less problems from that product. So those are things very very essential.

### 00:01:34 · Speaker 1

some software developer point of view, I mean your responsibilities and many don't spend lot of time on learning this architecture. So this video is super important if you are applying for premium and semi premium companies where they'll ask about one or the other architecture related questions. I'm gonna explain three very very important architecturing concepts. Monolithic, micro front end and mono repo. And I'll also give you examples which companies are using used architecture and please watch the video till the end because somewhere in the middle of the video I'm gonna give you super

### 00:02:04 · Speaker 1

important homework. This homework is not something that will create problem to you or will take lot of your time but it will create some intuitiveness in you and it will start making you to think from the architectural point of view whenever you look at a product, okay? So so please watch the video till the end without skipping in middle. Let's get started. Yeah. So let's get started by the architecture, what are the different architectures that exist for the front end and how it evolved and what what architectures are used by popular applications. All of that let us

### 00:02:34 · Speaker 1

because one by one. Okay? Very first one is monolith. Okay? Monolith or what's also called monolithic architecture. It's one of the oldest form of architecture and it is still used in the industry. Correct? See, uh in the past there were not lot of importance that was given to the front end architecturing as such. Okay? So as a whole system there used to be some architecture and front end was considered to be a part of system. It was not considered a separate entity. So where there was not much of an importance. But now as a front end it

### 00:03:04 · Speaker 1

self has becoming a very complicated system there are a lot of architectures dedicated for content. So I'm going to explain all of that so watch the video till the end. So first is the monolith. So monolith architecture is traditional model of software program which is built as a unified unit that is self contained and independent from other applications. Obviously this definition is not mine I taken it from the web. So in very simple words I'll explain. For example

### 00:03:28 · Speaker 1

Let's say first let us start with a back end example. Let's say you are interacting with a one back end system your front end application and the back end system has few entities like on one authentication module is there and one module is for sending you settings details. One module is there for sending the core details. Let's say for example you're using a Paytm application. So as soon as you land in home screen you have to show a lot of things like how much is my balance, notification count. So somebody is handling this entire thing. And there is some other team which is handling for of the flight booking. Somebody else is handling

### 00:03:58 · Speaker 1

something. So if none of this is done, all this is put together as one system, okay? There is no bifurcation. All these things are put together as one system. For example, let's say I work for the authentication team and I go ahead and modify certain things required in a common library which was required for me, okay? And I just commit it and somebody tomorrow comes and modify that common library and it will affect me because he is undoing my changes because that is hampering his. Not necessarily that this will happen everywhere like you go ahead and

### 00:04:28 · Speaker 1

in the common labyrinth it will suddenly affect somebody no people will take take some consent and then only do the change but I'm just saying these are the things where a system is one big entity there are no separations here okay so which systems are using that that's something that I'll discuss

### 00:04:44 · Speaker 1

So next slide is actually talks about advantages and disadvantages then we are going to micro front end. But before that I'll tell you what all the very big systems that are using monolithic. GitHub was still using the monolith architecture, okay? So now you may question Vasanth if you're saying disadvantages like there is a very big system, the deployment should happen all at once and there are problems associated with that how GitHub is using. See, all architecture comes with pros and cons and somebody can just use the pros and try to overcome the

### 00:05:14 · Speaker 1

cons and builder system, okay? But there are many systems like Netflix, Google and Facebook, they all started their application with monolithic architecture because it is easy to start, okay? But after a point they all struggled to scale. So due to which they all ended that architecture and they moved to separate architecture which I'm going to discuss in a while, okay? But systems like GitHub recently they are in a talk to migrate their back end to microservices and UI to micro content. I'll explain micro content in a while, okay? But most of

### 00:05:44 · Speaker 1

system start as monolithic where the entire system is one unit, okay? And then they'll migrate into a separate architecture whenever it grows, okay? So pros and cons I've explained, advantages, easier continuous development, correct? Because uh you there is no separated ownership. Like a guy from authentication team if he has something to do with the home team he can go fix and come back or like I said uh from the home team they can go to common lab refix and things and come back. So it's a very easier and continuous development as

### 00:06:14 · Speaker 1

there is only one system, okay? And I reduce latency, lot of things happen faster here compared to one with a separated system. For example, let's say you want to you are doing an authentication system and you want to interact with some system which is basically handling the user details. And that system team need to handle with some third party tools like work day or some other payroll management tool which actually holds the employee's information. So there is a three level of hierarchy to get one information.

### 00:06:44 · Speaker 1

correct? So this system doesn't know which database this system is using, this system doesn't know what they are using, correct? So obviously this will add some latency, but if all these three are one, like you also query on table, he also query on table, they also query on same table, obviously it will be very faster, correct? So the reduce latency, disadvantage also you know, difficulty in scaling, like if everyone are doing everything, then it is quite difficult whenever the application becomes bigger. Second, simply simple in the beginning difficult while scaling, quite similar, like for example

### 00:07:14 · Speaker 1

example, let's say you want to introduce a new team, where you put them? Because you don't have a separation of concerns, all put together as one big project, correct? So these are the disadvantages of monolithic. uh So most systems start with the monolithic and then they migrate into different systems, okay? Now before I go to the next system, first let me tell you something. So there is an architecture in the back end called microservices. I believe if you have not worked on it, if you if you are a front end developer, but at least you might have heard it somewhere. Let me give you a quick overview of what are microservices.

### 00:07:44 · Speaker 1

So, microservice is nothing but a big service, big service, for example now Netflix. Netflix has some hundreds of services, hundreds of services, correct? So these hundreds of services are divided into some modules, for example authentication module and the modules responsible for video rendering and video display, module responsible for streaming APIs, module responsible for account handling, like which user user details, person details, all of that. So these different modules can be owned by different teams.

### 00:08:14 · Speaker 1

So that is known as microservice architecture. So where each team can leverage the advantages of different technologies like for example one backend uses Java, one backend uses Python, one backend uses NoSQL, one backend uses SQL. This can be achieved with the help of the microservices, okay? So influenced by this this concept, UI also come up with an architecture called microfrontend. That is I'm going to talk next, okay? So here microfrontend as you can see

### 00:08:44 · Speaker 1

There are four teams. For example, in in the above example I had explained here, there is only one team called shop team in monolith, okay? Same shop team is divided into now four teams here, like team inspire, team search, team product and team checkout. It's a one product, but internally it has divided into four different parts, okay? So now each of this part, so mission helps the customer to discover products, quickly find the right product, press the product, uh provide a good checkout experience. So now each of this team

### 00:09:14 · Speaker 1

Now, independently working on certain modules. Okay? So now, for example, this team can use a Java as a for the back end and react on the front end. And here, the team search decide to use something else. Team product decide to use something else. Okay? So this will give a lot of flexibility whenever the application is going to bigger scale. Okay? The idea behind microfrontend is to think about a website or a web app as a composition of features which are owned by independent teams. Each team has a distinct area of

### 00:09:44 · Speaker 1

business or mission it cares about and specializes in. So like for example they need not to use the same text tag they need not have a same vision or a mission they all are like a act like a separate companies for inside one product okay. Let me give you the most simplest example so that you understand it better okay. So

### 00:10:10 · Speaker 1

So let's take up this example of Paytm, okay? I am not hundred percent sure whether Paytm is using the micro front end or not, but let's let's take a understand by taking this example. So you're seeing a mobile prepaid, mobile postpaid, electricity, pay, money transfer, passbook, all of it, correct? So now there are so many different actions happen in each of this. For example, action that happen after on click of electricity, you have to pay electricity bill, then it will list different electricity provider and you go enter your customer ID and all of that.

### 00:10:40 · Speaker 1

So the flow is different. What happens on mobile prepaid, you select different mobile operators and select a pack etcetera. So the flow is different. Same goes for DTH, gas booking etcetera, correct? So on overall,

### 00:10:52 · Speaker 1

all of this have a different kind of a flow, correct? So how it might have done in the back end with the help of micro front end is, so this mobile postpaid is owned by one team. So this electricity is owned by another team. This mobile prepaid is owned by another team, okay? So how it is another team? Let's say, let's take an example, every team is using an application of React Native, okay? So this mobile prepaid is one React Native application, mobile postpaid is one React Native application or electricity is one React Native application. Native also you can

### 00:11:22 · Speaker 1

take in the same way and they are built in a separate GitHub repository. Okay? After they are built in a GitHub repository, you make a change to your individual product and you make the change, then all these things are put in one container React Native app or container Native application. For example, there are already three different apps. Okay? So they do something of their own and there is one container app, okay, where all of them come and sit in. Okay? Now, this container app could be again React Native or a

### 00:11:52 · Speaker 1

app on click of this mobile they load the bundle from that app where whichever you have built so now mobile prepaid team has built one particular

### 00:12:01 · Speaker 1

bundle from their GitHub repository. So on click of this mobile prepaid your redirected user to that particular thing. So container app's responsibility here is where to redirect on click of each tab, okay? That has been the microfrontend architecture on the UI where there is one container app, one container app which will kind of encomposite all the things and there are other mini apps or whatever what I can also call like subparts of the app which will be built separately and they'll be embedded into this container application.

### 00:12:31 · Speaker 1

Yeah, hope you now you got a sense how microfrontends work. So one container app, different apps go and sit inside that, okay? So the advantage here, I'm going to explain that. So the examples are it is used in very popular apps like IKEA, Starbucks, Dazzle, etcetera. What are the advantages of adopting different text stack I already mentioned. So some team uses Python's advantage on the back end, some team uses Java advantage on the back end. On the UI if you say on the microfrontend side, it is not that easy like one product uses

### 00:13:01 · Speaker 1

angular one product uses react because ultimately this all of this uh individual blocks go and sit in a container app. So container app need to have the same dependency as that of the children app, okay? So one is in angular, one is in react, the build may become quite complicated. So generally the UI's text stack will remain same, but the teams will develop them individually, okay? And easy maintainability obviously, then disadvantages code duplication. You might have already guessed this. So let's there's three react applications on the UI. Okay?

### 00:13:34 · Speaker 1

So all the three are using now Axios as the package to make an API call. Correct? And the way app A makes the network call and app the project B and the project B makes a network call with the help of Axios is same. Correct? So now need not all the three project need not to instantiate Axios and make a network call. This can be put in some library. Correct? Obviously Axios can be put in some library but there are a lot of other things where the code reusability is not happening but the code duplication is happening.

### 00:14:04 · Speaker 1

Okay. So code duplication now you get a sense whenever there's a code duplication and whenever the container application decides to make a code change, all the children has to make that change. Correct? For example, now Axios 1.0 was used by all across, some particular application needs 2.0. Now, we cannot say if container has to support 2.0, all the other child application also need to support 2.0. So there's a code duplication and every time whenever somebody needs requires a migration, everybody need to migrate it. Correct?

### 00:14:34 · Speaker 1

extra effort in review and migration that was the next point. So let's say everybody updated the package. Okay? What is there in the code review? Everybody has updated that version. But there is somebody who need to review that and somebody need to approve. Again it need to go to the build system. So for the same thing, I mean, for the same work there is a development effort is wasted, review effort is wasted, build effort is wasted. Correct? So this these are the problems that comes with a micro front end architecture but micro front end architecture

### 00:15:04 · Speaker 1

actually has lot of advantages which which can be ignored coming to the disadvantages. So micro front end is very very beneficial whenever you are

### 00:15:12 · Speaker 1

operating on a different geographical zones. Let's say for example, one team is operating in India, one team operating in US and one team operating in Europe. Let's say you are not following the microfrontend architecture and you are following whether monolithic or there's another thing called mono repo which I'm going to explain in a while. So there is a lot of overlap that will happen between all of you guys. Let's say now there is some shared library, correct? That need to be updated. Now all the things has to put at some time and then do the updating operation. Now with a microfrontend you have an

### 00:15:42 · Speaker 1

advantage like you update your product and you inform others. You update your product and inform others. So there's going to be least effect. Correct? So microfrontend is very very useful whenever there are a distributed systems. I mean distributed here as in your team is distributed all across the globe. So microfrontend is very very suitable for you. Okay? Now, let's go to the next.

### 00:16:03 · Speaker 1

before I I explain the next architecture which is mono repo, I think you are liking the content whatever I have made so far and it takes lot of effort to understand different systems and prepare this presentation and give present it to you. So if you are liking the content please like the video on my YouTube channel, add comment, whatever you are thinking, is it a good video, mention. No wasn't this can be improvised further, add a comment. By more likes and comments the video becomes visible to lot of people and there is a high chance they will click on it and they get benefited. If more people view my video,

### 00:16:33 · Speaker 1

channel becomes popular like I always say I have only noble cause of helping people to clear the interview. I'll achieve that much sooner. Okay? So please like and comment about the video before watching further. Thank you. Now, let's get started with the next very very popular architecture called Monorepo. Correct? Before I explain Monorepo okay let me explain Monorepo and I'll give you small homework. So Monorepo architecture

### 00:16:56 · Speaker 1

is quite similar to monolithic. Okay, let's read the definition first. A code management and architectural concept whereby you keep all isolated bits of code in one super repository instead of managing multiple smaller repository. Microfontein you got where you are managing multiple smaller repositories, correct? So electricity bill payment is one unit, flight booking is one unit, gas booking is one unit. So what back and what fontane uses, it's at operate, correct? Now, whereas mono repo is not like that. Mono repo is like

### 00:17:26 · Speaker 1

one big chunk similar to monolithic, I'll tell the difference, okay? First let us see the example of who all using mono repo, Google, Facebook, Microsoft, Uber, Airbnb, Twitter. So a lot of big firms are basically using the mono repo architecture. Now let us understand what is mono repo very much in depth. So, you're seeing one mono repo folder here. Then you have node modules package, package.json. So there is one react app, okay? This react app has its own node module source package.json. There is second react app, okay?

### 00:17:56 · Speaker 1

again it has its own things. There is one React Native app and there is one common library, okay? So common library here is what? For example, uh a library used for making network call or library that is used for logging certain things or library that is used for UI uh like buttons, animations, etcetera. So this common library is required for React to app one, React app two and React Native app one also, okay? So what we are doing is rather, see let's say all these are now independent.

### 00:18:25 · Speaker 1

obviously. Then what would have happened if all the apps are independent, there would have been a lot of code duplication happening all across. Correct? Now, like for example now common project whatever is here, that common project has to be published and that common project source you will take into your project. Same way how you will take AxiOS, right? You will NPM install AxiOS. Now you will be publishing your common library somewhere. Correct? Like for example your company XYZ hyphen common library, you will add it to your package.json and get that common library.

### 00:18:55 · Speaker 1

So every time when common library is updated you need to take a new version and update. But here all the things are in same project. So you can just reference to that common library and use whatever you want. You don't have to wait for them to publish the version. Correct? So then this is in very simple words is a mono repo. So let us go to the next. So let us this is very very important. Lot of candidates get confused what is the difference between monolithic and mono repo. Okay? What is monolithic? Entire score code of the project lies in one repository. लेट्स टेक अ सेम एग्जांपल ऑफ पेटीएम और फोनपे वेयर एंटायर एप्लीकेशन

### 00:19:29 · Speaker 1

is in one repository. Okay, front end, back end, in front end, all the different modules, all that are in there in one repository. Mono repo need not have only one repository. Mono repo each meaningful unit can have a separate repository. For example, all the front end can have one repository, all the back end can have another repository. Correct? So in the front end again, let's say it is becoming very, very big. For example now, let's take an example of Airbnb. Airbnb has two main entities. One, like

### 00:19:59 · Speaker 1

tourist who comes and books one, one who owns a property. It's becoming very difficult to manage both in one, then probably you can try to differentiate, separate them both and make two different mono repos. Where again this will have a lot of different modules and this will have a lot of different modules. And another difference, entire application is deployed in one go, individual processes can be deployed separately. It's possible here in the mono repo, okay? For example, you saw right, have React app one, React app two, React Native app one, they all can be deployed separately, like though they are all in same

### 00:20:29 · Speaker 1

project and uses some similar dependencies. Their deployment is not dependent on any other project. Okay? So which all popular projects are using Google, Facebook, I already mentioned, all these popular companies are using Mono Repo. Okay? Now, Mono Repo libraries. So this is very very important. Let's say now you have ten different React apps under one folder. Okay? Now, you have to, let's say you make one change to the common common folder. Like common is something that contains all the libraries, let's say.

### 00:20:59 · Speaker 1

like how to make API call, how to log. After you make change to the common library, you cannot just run the test case on common library and end your programming, correct? Because that common library is used by this ten reactor projects. So you have to make sure none of the test case of this ten reactor projects is affected by the changes that you made for the common. So how you can do? You can go to React Native, React JS project one, run NPM run test, test that React Native project two, NPM run test. Same you can do for the ten projects, correct?

### 00:21:29 · Speaker 1

make sure whatever the change you did from the common library hasn't affected any of them. But you already got the sense it is becoming complicated, correct? It's not about just running the test. There are a lot of activities like for example packing, many uses web pack and other things for packing the project, correct? So you may have to do that. So there are a lot of activities end to end testing, unit testing, all of that has to run across different project at once. So there has to be some library which will give you this flexibility. So this can be achieved by different framework like NX or

### 00:21:59 · Speaker 1

learner, Bazel build, PNPM. I very much prefer learner. This is something that I have used in the past. You can probably use the Rush also from Microsoft. If you're someone who is hearing the term for the first time and you want me to make a detailed video about learn or Rush, please mention that in the comment section. I'll try to make a detailed video explaining these, okay? So you at least you got a sense why learn or Rush required. Different projects, updating certain things in common, you have to run lot of test scripts on different projects individually. rather doing that, use some common place where you can do this for the entire project, okay?

### 00:22:35 · Speaker 1

So mono repo pros and cons, pros you already got, code and library use. um Like last also I explained. A common library has to updated or a package has to updated, you don't need to update everywhere. So once place you update and everyone will get it. Faster review obviously, there is no duplicate review happening for the same change. You will get to know what all changes happened. At a time we can see and we can approve or reject. Updating major dependencies lead to the super easy, similar like you update certain things in a common library, reflex for all.

### 00:23:05 · Speaker 1

cons no way to restrict only to access to the certain parts of the app. This is very very critical problem. For example,

### 00:23:13 · Speaker 1

If you go and look at this diagram again. So here you have a package called common. Okay? So now we have you own the React app one, actually your team works only on the React app one. You cannot just download the React app one and work. From the feature they can allow you to only get access to React app one, but you cannot just use React app one, you also need a common library, correct? So eventually common library uses another common library or something like that, so you cannot just limit yourself to work you are doing, your project size will become bigger.

### 00:23:43 · Speaker 1

Okay, because there will be a lot of entities which you have to have to make sure the entire project works fully. Too many packages lead to longer bootstrap time, obviously. So what happens is there are sometimes those certain things are not really required for your project because of some common things that you are using. A lot of packages get added into your project and the bootstrap becomes slower. Poor Git performance when working on a large scale product. So many so far in their entire lifetime they might have not faced this. What is poor Git performance?

### 00:24:13 · Speaker 1

performance is let's say you have ten files or typical react examples or react react js or angular where you don't check in node js you only check in the source codes correct so that let's say there are fifty files hundred files correct and whenever you every time whenever you doing a git push it just compares the changes etcetera and it will show what all changed correct so this will not work the same way when you have gb's of data correct it becomes very very difficult for git protocol to understand where all the changes have happened and how to show the difference so google and facebook have

### 00:24:43 · Speaker 1

their own internal Git tools for this purpose, okay? But typical applications which are not having so much of files, need not to have worry, but very big applications which have GBs of code itself, might face problem with a Git. So you if you are using Mono Repo for a very big project, you should be ready to write your own source control like Git. Next, the code navigation is slightly slower, developers are now opening individual package work around that. Quite quite um known issue because you um have so many let's say ten React

### 00:25:13 · Speaker 1

out of which four are libraries. So you have to go to that and see what all changes has done and then pick into your life project. So code navigation becomes quite slow, but obviously over a point of time you become uh adaptive to that, correct?

### 00:25:27 · Speaker 1

So that's all about the entire thing that I want to explain but let me quickly summarize. Before summarizing I have a homework for you. Please tell me what framework that you think is used by the popular apps React apps like Facebook. Okay? Facebook

### 00:25:44 · Speaker 1

Yeah. Before, before I summarize, please explain me what architectures are used by the popular applications like RedBus, BookMyShow.

### 00:25:54 · Speaker 1

and Myntra. RedBus, BookMyShow and Myntra, analyze the project, analyze the look and feel how they might have done. What you think the architecture that they might be using, mention that in the comment section, I'll correct you if you are right or wrong. So in case if you are not at all getting idea, try to go to the medium and look have they written anything regarding that and try to extract the knowledge and write. Okay? Now, let me quickly summarize the architecture that we discussed in the article. We have basically three architectures. Monolithic, microfrontend, monarepo. Monolithic everything in one, microfrontend each

### 00:26:24 · Speaker 1

this concern is divided into separate unit and monorepo again any meaningful unit is binded into one repository okay each has its own advantages and disadvantages okay now if in the interview they ask you which architecture you are gonna pick so weigh the pros and cons of each architecture and see what is suitable for the application that you are you that you are that they have asked okay this is super important from the system design point of view

### 00:26:54 · Speaker 1

publish system design interviews, system design concepts in in upcoming videos. So before that I thought let me make my followers be aware of these concepts because suddenly if I explain that I may not get this much time to explain all the concepts, correct? So please practice this, analyze every time whenever you look at architecture just think in your mind what architecture it could be, okay? That's all about this video. Thank you so much for watching. If you like the video, please like the video on YouTube channel. Add a comment whatever you felt. In case if you have not followed me on on LinkedIn

### 00:27:24 · Speaker 1

and medium, please follow me. If you have very personal questions that cannot be posted as a comment, you can ask me in LinkedIn, I'll try to answer that. And do not forget to subscribe to Uncommon Geeks because I am coming up with a very, very super important system design question and answers. So I'll be designing very, very big system designs on the UI. So please press subscribe and press the bell icon so that you get notification at the right time as soon as I publish the video. Okay? Thank you so much for watching. And this this particular PPT that I shared will be in my GitHub repository, you can download it for free. Okay? Link to that will be in the description section. Thank you so much for watching, catch you in next video.
