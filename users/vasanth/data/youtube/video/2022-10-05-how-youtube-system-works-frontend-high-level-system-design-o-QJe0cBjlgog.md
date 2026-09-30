---
id: QJe0cBjlgog
title: '🔥 How Youtube System works ?🔥 Frontend High Level System Design of Youtube
  #youtube #interview'
date: '2022-10-05'
url: https://www.youtube.com/watch?v=QJe0cBjlgog
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ UncommonGeeks is a Youtube channel dedicated to helping candidates clear their\
  \ interview. There are close to 70 videos and new videos will be uploaded every\
  \ week. If you're seriously preparing for interviews and looking for tips and tricks,\
  \ please subscribe to my channel and press the bell icon.\n\nChapters:\nComponent\
  \ Architecture of Youtube: https://youtu.be/QJe0cBjlgog?t=1230\nBuilding Video Player\
  \ like Youtube: https://youtu.be/QJe0cBjlgog?t=1425\nPagination of Youtube comments:\
  \ https://youtu.be/QJe0cBjlgog?t=1739\nLive commenting in Youtube: https://youtu.be/QJe0cBjlgog?t=2219\n\
  \n\nWhat is frontend system design: https://youtu.be/gN8LQTff21g\n\nFramework used\
  \ by Youtube for navigation: http://youtube.github.io/spfjs/ \n\nInterviewPreparation\
  \ series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nMedium Blog https://mevasanth.medium.com/  \n\nFollow me onLinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\
  \ \n\nGithub Repository that contains presentation: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript/tree/main/Frontend%20System%20Design\n\
  \nJavaScript Custom implementation|polyfills  introduction: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s"
author: careerwithvasanth
duration: 00:54:53
model: saaras:v3
transcript: true
---

# 🔥 How Youtube System works ?🔥 Frontend High Level System Design of Youtube #youtube #interview

## Transcript

### 00:00:00 · Speaker 1

just for some facts I'm telling you YouTube has around twenty million uploads every day. One million is ten lakhs. Okay? More than twenty million videos are uploaded on YouTube every single day. It has if you just roughly take each videos of hundred MB there right two petabytes of data is getting added into YouTube every day. Two petabytes means two hundred terabytes or it is close to twenty lakh GBs of data that is getting added into YouTube every day. Different than the normal streaming is the

### 00:00:25 · Speaker 0

friend

### 00:00:28 · Speaker 1

normal video whatever I showed you here is the comment section. Correct? So there are right now around eleven thousand eight hundred seventy six people are watching. And if you observe this, the comments are being flooded like anything. Correct? This looks like an easy problem to solve with help of page and other things but it is not that easy.

### 00:00:49 · Speaker 1

Welcome back to Uncommon Geeks. Myself, Vasanth. I hope you all doing well. In case if you are seeing me first time on the internet, I'm a content creator. I help people to clear their interview. I've made a lot of beautiful series in the past which has been appreciated by many. Link to those series will be somewhere on the screen, I'll put in the description section. So this video is one of the very, very requested video on my channel, on my medium, LinkedIn, everywhere. Like, Vasanth, what is fragmented system design? How fragmented system design interviews should go? And how the questions should be asked? How we have to prepare? How we have to answer? Correct? So I will be

### 00:01:19 · Speaker 1

solving, I'll be taking a very, very important example in this video and I'll be explaining how front end system design works. But I have, there are certain common elements that appears for, that will be exist for all the different systems. So I've tried covering that in this video. It's just eighteen to twenty minutes video. Watch that video and come back here because I know you know the basics of the front end system design before coming to this video. Because this is a typical example where I'll be taking a system and I'll be designing it from scratch, okay? So nothing superficial, nothing is pre-built, everything I'll be

### 00:01:49 · Speaker 1

building in this video itself. So if you're not subscribed to my channel, please subscribe to my channel and press the bell icon so that whenever you go till the end of the video, you will be definitely be benefited also. I'll be uploading lot more system design videos and whenever I upload, you should be notified. Okay, that is the reason please subscribe and press the bell icon without

### 00:02:06 · Speaker 0

for the time let's get started with topic of the day

### 00:02:09 · Speaker 1

So as you might have already seen in the thumbnail, so this is a video where I'll be designing one of the most popular system on the internet that is YouTube. So I'll be designing this system from the point of front end. Front end, what are the things involved in the front end, how front end has lot of challenges, how it will be solved, okay? And before I start explaining those, there are certain facts that I need to be very clearly explained to you. So YouTube is one of the most used platform on the internet. So Facebook, Google, YouTube, they all probably rank in for the top ten definitely. So just for some fact

### 00:02:39 · Speaker 1

I'm telling you YouTube has around twenty million uploads every day. One million is ten lakhs. Okay? More than twenty million videos are uploaded on YouTube every single day. It has if you just roughly take each video is of hundred MB that are two petabytes of data is getting added into YouTube every day. Two petabyte means two hundred terabytes or it is close to twenty lakh GBs of data that is getting added into YouTube every day. It's a very very massive system. So why I'm saying this is it is quite practically impossible to design such a big

### 00:03:09 · Speaker 1

system in around forty minutes. Correct? This obvious. But given a question, how do you start is what the interviewer is very much interested to know in in this interview. Okay? So let us start by the first thing that is

### 00:03:21 · Speaker 1

requirements, correct? So I've already explained this very much in my other video. Please watch that video if you've not already watched, okay? So first thing, uh, I'll let me start by adding the text. So same, this is the same way the interview goes on. If you are someone who not at all aware of the system, then you can go ahead and watch the system and come back, okay? For example, somebody might not have a Netflix subscription. So if you start designing Netflix and you don't even know what options are there, then probably you may have to ask the interviewer to show you the system so that you get some insight, correct? YouTube is very open. My videos are also uploaded on YouTube, so if you're

### 00:03:51 · Speaker 1

watching me you already know what is YouTube. So I'm not going taking a walk of the YouTube because I already aware of the features. Okay? So let us start by adding first point is here requirements. Okay?

### 00:04:03 · Speaker 1

So this video can be slightly longer forty to fifty minutes so take a coffee and stay tuned till the end definitely it will be beneficial for you. Don't skip in middle. Okay? So requirements. So I think requirement has two different sections not I think requirement has two different sections one is general requirement. Okay? General

### 00:04:23 · Speaker 1

requirements. Okay? So what, sorry, yes, our requirements.

### 00:04:30 · Speaker 1

what we can do not general requirement functional requirements and non functional requirements okay now not a general requirement I'm sorry for that so functional requirement and non functional requirement what we'll do maybe we'll increase the size a bit. requirements let's make it just the requirement I wanted to be extra large but everything is becoming extra large.

### 00:04:53 · Speaker 1

Okay, anyways. So, uh requirements, functional requirement and non-functional requirement. Let us start listing the functional requirements. If you don't know what are functional requirements, again I've explained in my initial video very much in detail. But in very simple word, functional requirements are those which are like a functionalities. What all functionality that we are building are present in the YouTube, okay? First thing if I have to add, one of the main functional requirement of the YouTube is authentication, okay? Then we have you So, whatever you think in the journey

### 00:05:23 · Speaker 1

of YouTube, all of that you can start listing here, okay? So we have authentication, okay? Then once you are logged in, so you come here. So also before I start this part, basically YouTube has two persona, correct? One as a content creator, one as a content consumer, correct? So in the interview, you ask which persona or which category the interviewer is interested to know the design part, okay? So depending on that, let us you have to list the requirements, correct? So I am designing here for the content consumer, like any end user like you will be watching.

### 00:05:53 · Speaker 1

the video, not somebody who's creating the video. Because why I am not doing the content creator kind of a thing is, content creation mode many might not have explored. uh like it's not so common, everyone are not YouTubers, they will not go and see the content creation phase. But consuming is very very common, so I'm taking the consuming phase. And interview also this is very commonly asked on the consumer persona, okay? Now, first thing is an authentication, okay, once you have authenticated in the system, then what you have probably you have account settings, correct? So there are many options inside the account settings.

### 00:06:23 · Speaker 1

things like probably uh some preferences, language, all those things, correct? Then we have the search functionality, correct? Inside even the search, we have certain different search that is text search.

### 00:06:36 · Speaker 1

And next we have voice search. Okay? So some actually what they make is some whenever they list like this they will modularize it like they read only the search and whenever that during the scoping they'll add the further items that is also you can do or whenever you are writing you can add the main features here itself okay? Next. Next we have the video listing.

### 00:06:57 · Speaker 1

the core crux functionality where whenever you open YouTube you start seeing this different videos, correct? Then video details screen.

### 00:07:04 · Speaker 1

So video details is whenever you tap on a video the screen that opens is the video details, correct? What all functionalities you see in a video details? You have like

### 00:07:11 · Speaker 1

slash dislike. You can like and dislike a video. Then you have comment section. Correct? And you have a comment, then you have something like suggested videos. Correct? Suggested videos. On the right hand side you will be seeing what all suggested videos for you. Correct? Once maybe after that we'll have certain very basic options like share, embed and all. Correct? If you're not somebody who is following up with me, just go to the YouTube detail screen and you can watch it. Correct? Then we have some premium feature.

### 00:07:42 · Speaker 1

So YouTube has premium features where you can pay and watch certain videos. Okay? Then YouTube also has live streaming.

### 00:07:49 · Speaker 1

can watch live streaming functionalities in YouTube. Then you will also have certain things like gaming.

### 00:07:55 · Speaker 1

and you also have something called news. Okay? And you also have something called music. Okay? So roughly I'm listing all the things that I have seen in the YouTube in general. I'll definitely I prepared for this video like it is not the first time I'm simply writing. I've just studied the system I've noted down certain items actually left hand side I've written them so I'll be watching once in a while in case if I miss certain things because whenever I'm communicating you guys should know everything. But you as in the interview let's say you whatever the things that you have seen try to memorize it. But if you are not able to memorize there's nothing

### 00:08:25 · Speaker 1

wrong you can ask interviewer shall I see the system once just before you start writing down you can look at a system once and then start listing all this okay so gaming news then so these are the things let us stick to these items so because let us be practical we have only one hour interview where forty minutes is only dedicated for system design okay all the crux or the core functionalities we have listed here now let us go for the non functional requirements okay so I'm just maybe decrease the size of this

### 00:08:54 · Speaker 1

Okay. I don't know. Every this is not like maybe one minute. Let me cut this here and I'll add another text item. In that case maybe I'll get some freedom. Yeah.

### 00:09:08 · Speaker 1

Okay, non-functional requirements.

### 00:09:11 · Speaker 1

still it has a problem. Anyways, I'm able to scroll now which is good. So what are non-functional requirements from the YouTube point of view are like non-functional I think I have again explained my previous video very much in detail but in case if you're not seen in very very simple terms non-functional means something that is not directly affecting the user but it is very very important for the system. So for example the first one is adaptability. Okay? Adaptability here I mean it should be we should be able to see the video on mobile tab all the screens, correct? So whatever the screen that you are designing

### 00:09:41 · Speaker 1

learning that should not be just generic to the uh it should be not just be dedicated for web or mobile it should be adjustable whenever you compress the screen it should get adjusted so that is something non functional requirement second thing is localization

### 00:09:54 · Speaker 1

Like, are you supporting any local languages whenever it comes to India, like for example Hindi, Kannada, Malayalam, Telugu? There are many different local languages. Are you supporting all the local languages in the system? If so, how are you doing? Correct? Then you have something called globalization. Same as localization, but are you supporting the foreign languages? Correct? How you are going to support the foreign languages? That is then there is a very important thing called security. Then there is another thing called caching. Correct? Where security you will be you need to ensure whatever the system that you are building should be secure.

### 00:10:24 · Speaker 1

enough. Like uh whenever you're streaming the video, uh the right packet should come to you and some whatever malicious packet, some some intraday is adding some packages which can hack the system and get certain information should not be added into your system, correct? Caching is obvious. So whenever you are rendering a certain page in YouTube if you have observed, you see one video playing in the center, suggestions will be there. And whenever you click on a suggested video, this next layout is also pretty much the same. The same layout is appearing in the next screen. Only the main content gets changed, suggested videos also get changed. But

### 00:10:54 · Speaker 1

it is not like a whole page re-rendering. I'm going to talk about that in a while. So there are a lot of things that can be cached. Comments can be cached, count of like and dislike can be cached, correct? Many things can be cached locally so to give a better user experience or whatever the thumbnail images that are shown in the YouTube, correct? Those can be cached, correct? So there are many things that can be cached in YouTube. So that is about the caching. Then

### 00:11:15 · Speaker 1

we have certain certain things called accessibility. So how you make sure somebody who's disabled can access the tool? Like maybe blind or somebody with some disabilities, what are the things that you're doing in the tool to make sure they have accessibility? See, it is it is very very important to consider all these aspects in system design. So Vasant, I my system as is not supporting any globalization. I'm dedicated to only India or I'm dedicated to only US, so I'm not going to support any localization. That is fine, okay? But whenever you design a system,

### 00:11:45 · Speaker 1

we have to list the items and rule out and have a justification added in a document saying this is the reason why I am not supporting the globalization. This is the reason why I am not supporting a localization. But you should always take this point during the discussions so that somebody stakeholders will add a point and you will be able to get a clarity on them. Correct? So next whatever we have is architecture very very important. So if you are not sure what is front end architecture I have tried explaining very much in detail. I will be adding that video here also in the description section. Very very important video.

### 00:12:15 · Speaker 1

where there are a lot of different architecture that available on the front end, uh to name micro front end, monolithic, um also there is something called mono repo, which architecture suits better for the project. See, these are all the things that doesn't impact the user directly, whether you cash or not, he is not bothered, correct? Whether you are giving accessibility or not, some user it will affect, but as a entire product it doesn't affect. So these are things which are not directly affecting the user, but these are all very essential from the product point of view, okay? Then

### 00:12:43 · Speaker 1

I think I'm the maybe we can do this resource optimization. Right? Very very important resource optimization. So where given a particular bundle, how you're gonna use the images, how you're gonna use the videos and other things so that whenever you're storing those resources locally or wherever you're storing, that has to be stored optimally so that the loading can be improvised faster. Like are you minifying the JS? Many many resources are there, how you're gonna optimize all of them, okay? So these are the things that I think are some good enough things, okay?

### 00:13:13 · Speaker 1

the requirement point of view, okay? Let me select this entire region, make it medium so that you can view the entire requirement at once, okay? So where we have the functional requirement and non-functional requirement, we have listed. It could be little small whenever you are viewing the screen, but so I'm zooming in so that you can see all at once, okay? Functional requirement and non-functional requirement. So what is the second step? Again, in my previous video, I've clearly explained, once you have the requirement, definitely all these things cannot be built in the for ten minutes interview, whatever we are having, okay? Actually, I've already

### 00:13:43 · Speaker 1

around fourteen minutes. This is a typical duration, same thing happens in the interview, okay? My videos are not superficial, so I'm very very much clear on that. How the interview happens, the same way I'm trying to mimic here with little bit of extra time to explain you certain things, okay? So now we have functional requirement and non-functional requirement. Next is we have to do the scoping. So in scoping, we pick certain items that interviewer is comfortable with generally. So there are certain things that an interviewer know very very in depth. So he will ask you to pick, he or she will ask you to pick those topics and do the component architecture.

### 00:14:13 · Speaker 1

structure and explain to them very clearly, okay? So and they'll have certain problems with each approach and they are going to discuss that with you and how you can come with a better approach, all those things will be discussed in the interview, okay? Now if you see, scoping, next section is the scoping, okay? After requirement, next section whatever we have is the

### 00:14:32 · Speaker 1

One second

### 00:14:35 · Speaker 1

So, next section is coping. Okay.

### 00:14:39 · Speaker 1

So in scoping, what all the things scoping basically refers means in this what you are picking. See, I am very interested in few things. See, if you look at the video details, so it has lot of features like like dislike, comment, suggested videos, share and embed. So I'm quite interested in this and as a if I look at all the functionalities here, for me this seems little challenging and it's worth explaining it to you guys how lot of things are been solved in this particular area, okay? So let me take this video detail screen, okay? with all these options

### 00:15:12 · Speaker 1

Then, if I come here in the scoping section,

### 00:15:17 · Speaker 1

So I'll be taking this video details and next another important thing that I think will be very very useful and competitive worth explaining is the live streaming. Okay? Live streaming has lot of challenges on its own. Let us look at them one by one. Other things also quite maybe important for you is like how you're going to do the text search and the voice based search. There is some filtering with the time uh and lot of uh newly new new things on first etcetera. But I'm not going to focus on all those things. I I am sticking to this. You are free to pick after I explain these two you are free to pick.

### 00:15:47 · Speaker 1

any of these requirements and you come up with the challenges that particular feature has and how you will solve it, okay? But I'm gonna stick to this because definitely I've prepared also for this properly, okay? And definitely these are the things whenever if you go for interview there is a high chance they'll ask you these questions. They wouldn't ask you to do the video listing. Obviously most front end developers know how to do the video listing, correct? That's quite generic. Lot of things that we explain gaming, news, music and also there is another thing I missed it. That's called shorts. Recently the shorts are becoming very popular, correct? So obviously some feature some interviewer can pick some features I'm going to pick these features okay now

### 00:16:23 · Speaker 1

Next, these are the two pictures we have done the scoping. Next part is the, uh, let us next part is the technology, okay? So it's needed to be this way, like you don't have to pick the technology and then go to the component architecture, you can kind of define the technology after the component architecture also. But just before I start drawing, I just wanted to make sure like we discuss the technology and finalize it. So what all technology options we have? So most popular ones I'm going to pick now. One is using the plain HTML and JavaScript, correct? in HTML, CSS and the JS. Next we have is the React JS.

### 00:17:00 · Speaker 1

Next we have is the angular.

### 00:17:03 · Speaker 1

Next we have is a view js.

### 00:17:06 · Speaker 1

definitely I can keep writing the lot of other frameworks also but these are the quite popular frameworks, correct? So, uh but one interesting fact, uh YouTube as a platform itself doesn't use any of this. YouTube has a custom framework of its own. That is what I read on the internet. But always keep this in mind, many do this mistake in the system design interview where they'll try to they feel very sorry when they don't know what the real system is using, okay? And whenever they they so they'll say I don't know what YouTube is using. See,

### 00:17:36 · Speaker 1

they are not asking you to clone the YouTube. Okay, in a system design interview, they are asking your opinion if you want to design a system like YouTube, what you're going to use, okay? So be clear on that thought. Don't think bad because you don't know what YouTube is using. Many don't know what YouTube is using because there is very limited information on the internet. Whatever you said publicly, only those information we know. In the beginning I said so many videos are getting uploaded, so many GBs of data. I also read somewhere on the internet which I think is trustful source, but not from the YouTube blog, correct? So we don't

### 00:18:06 · Speaker 1

know a lot of data about YouTube. Same happens for a lot of system designs. So whatever information that you think is relevant, that only you have to suggest, okay? Don't worry if you don't know what system is really using. So now, uh for example now, can we use React or Angular? I kind of don't think HTML, CSS, and JavaScript can be used as it is because it has its own limitation. Definitely it could be a little faster in certain scenarios. But using the plain HTML, CSS, is becoming slightly outdated, correct? So React, CSS, or Angular is something that we can pick. I don't see any strategic

### 00:18:36 · Speaker 1

disadvantage of using any of them. You can use React JS or Angular, both should be fine. But there will be something called a company specific advantages. For example, let's say the team has lot of React developers. And team is already having certain projects on React. So you as an organization has been highly dependent on React on same in case of the Angular. So in certain cases it is good to go with that tech itself. Why because organization as a whole is using certain tech. And whenever there are problems you have experts inside the organization to solve, correct? So it's good to go

### 00:19:06 · Speaker 1

use that kind of a tech whenever you are building, correct? So, or else like hiring challenges will be there sometimes. Team is having only one React developer and three Angular developers, then you can also pick Angular over React, okay? uh I mean these are the I'm saying this is not should not be the first criteria of selecting a tech. This should be the second criteria, company specific pros and cons I'm telling, okay? Now when you I'll be picking React JS as one of the popular framework and is used by lot of developers out there. So, I'll be using React JS for building this particular thing.

### 00:19:36 · Speaker 1

So, and I'm justifying it because I'm very much believe virtual DOM concept and the reconciliation will make a faster re-ending and already lot of very big applications like Netflix and Amazon Prime to certain extent are using the ReactJS. So I don't see any problem with the ReactJS in the scalability even if you're having a millions and billions of users using it actively at a point in time, I don't see any problem with React. And as you all know, we also have very small component architecture of the React. So we can divide each function into components which will give a lot of flexibility.

### 00:20:06 · Speaker 1

code reusability. So I don't see any cons from React at the moment while using it for the YouTube architecture. So I'm using the React JS. If somebody you want to use a Angular or a Vue, feel free to mention why you want to use that in the comment section, okay? After you're done with the requirements coping and technology, the next common thing that generally happens in the interview is the component architecture. So in the component architecture, either you can draw and explain certain things. So most interviewer expects that drawing and explaining and some interviewer do not expect to draw

### 00:20:36 · Speaker 1

point else I'm going to get straight away asked a question and how you're going to solve that. So both let us let us discuss in this video. Okay? So now let's say let me simply design the YouTube. Okay? Basic architecture of the YouTube I'm going to design here. Okay? This is the video details screen, not the video listing screen. So everyone I believe have seen you seen the video details screen.

### 00:20:59 · Speaker 1

So here what I'm doing is this is the place as you all know the video gets played, correct? I'm just increasing its size.

### 00:21:09 · Speaker 1

Okay

### 00:21:11 · Speaker 1

And this is the right side where all the suggestions happen. Correct? So I'm taking another box.

### 00:21:18 · Speaker 1

all the suggested videos will be present here. Okay? And also have the this section where this is section where all the like, share, uh unlike, embed, all those things will be present here. Correct? And then this last section is the comment section. Quickly let us name so that in the whenever we are explaining the interview, you are clear. Video streaming. Okay?

### 00:21:43 · Speaker 1

or video player. That's probably the right word. Okay. Okay, video player. Let me increase the size so that you all can see. Video player.

### 00:21:54 · Speaker 1

Then we have suggested videos, correct? Suggested videos. Then

### 00:22:03 · Speaker 1

Then we have certain things called comment section. Okay.

### 00:22:08 · Speaker 1

comment section

### 00:22:11 · Speaker 1

Then we have this is what I can call like like share like share embed all these things will happen in this okay? So definitely suggested videos will have certain like images with the thumbnail etcetera correct? So control D

### 00:22:30 · Speaker 1

सो वेयर यू कैन सी मल्टीपल सजेस्टेड वीडियोस लाइक दिस, करेक्ट? वन बिलो अनदर यू विल बी हैविंग द मल्टीपल वीडियोस।

### 00:22:37 · Speaker 1

So something like this, correct? Suggested videos are going to be like this on the right hand side. So this is the typical UI of the bare bone. Don't think like this is the your whatever the beautiful design that your your developer gives. So this is a bare bone of the how YouTube looks like, correct? YouTube video detail screen looks like this. Now, now there are certain problems in each of this section. One by one let us going to discuss and let us solve. The first problem is the the video player itself, correct? So video player if you see you have certain buttons on

### 00:23:07 · Speaker 1

correct? That start, stop and all are here. That I don't know where the shapes are there, but I'm just gonna keep this is the start and this is the stop and you will have certain buttons like next and the previous, correct? You will have buttons like the forward and backward buttons, correct? Forward and backward buttons, sometimes on the right hand side you set usually the settings to increase and decrease the

### 00:23:33 · Speaker 1

the video quality etcetera, correct? So there are many options that are associated with this video player. Sorry, I did forgot to add O here. So

### 00:23:43 · Speaker 1

How you gonna build this player is the first question. Okay, now let us say you are in a system design interview and the interviewer ask, Vasanth, this is the video player, whatever you're saying. It is very beautiful player with lot of options. Like we already discussed it as like, share and video playing, pausing, forward, backward, changing the quality, adding the subtitles. There are a lot of functionality we associated with this video player, correct? So generic component, if you consider from React point of view, it's a generic component where lot of attributes are passed to it. Like for example, certain video

### 00:24:13 · Speaker 1

cannot be quality cannot be increased to HD because video itself is not in HD, correct? And there will be a lot of other options like subtitles. Some videos have subtitles where you can switch to different languages, some doesn't because author hasn't uploaded that JSON or whatever the file that is required for the subtitles. So this is a very generic component in terms of React if you think and what all components that you would pass to that particular video player component, depending on that it will show those options, correct? Obviously every video will have certain things that is very common, start, stop and the quality settings, they are all very common.

### 00:24:43 · Speaker 1

correct? So now, how you're going to design this player, correct? So if you ask me now, and this then what is the next question that I'll ask for the interviewer is, what is the timeline that we have for this delivery of this entire product?

### 00:24:56 · Speaker 1

Let's say he wants to go with a beta, the first version of the app in next three months. Then I would say, see, video player is a crux of this entire layout. There are a couple of options that I would give him. One, if there is any proven player which is already doing the fantastic job and that is at a very cheaper cost for us, let us first go and use that third party video player and embed into our tool. Let us not build a tool of our own. The reason for that is very clear, like I said, there is lot of challenges that comes with a player, like for example, you're getting the video and suddenly

### 00:25:26 · Speaker 1

video becomes slower. uh sorry, internet becomes slower. Then whenever how you fit the next set of packets becomes slower, but you shouldn't see the jitter on the video, correct? So there has to be some process in the back end which is taking care of these things. So video playing is a very, very complex process than you think. So my advice is if there is a possibility of taking a different third party tool, then let us take the tool for the beta. Further let us enhance it internally and add our own tool. Now interviewer will may say yes to that or interviewer may also say no to that. Like we have a limited budget, we cannot

### 00:25:56 · Speaker 1

the third party video embedding tool and it's a crux of the entire project the amount could be high. Okay. So in such cases definitely we can build a video player of our own. It is not some rocket science. Don't worry. If you want I'll link one blog which I read recently where they very very clearly explain how to build a video player. So it it can be easily built just with HTML video tag and

### 00:26:16 · Speaker 1

There are a lot of media source, HTML media tag, video tag in the media source. It's a JavaScript API. With these two things you can easily build a player like YouTube, very basic player like YouTube in just few hours. There are a lot of tutorial outs there with which you can build the video player. But there will be a lot of intricacies which you might miss, okay, whenever we build like as I said the adaptability, adjusting the quality, all those things may take little time if you build a your own YouTube player. Now, we are solved the first problem of video player. Don't think this is

### 00:26:46 · Speaker 1

I am not getting into all the problems, whatever the problem that is very very um visible on the top layer, I'm I'm touching them. Next, next problem which we have is so to summarize, video player, whether the if the timeline is less, let's use a third party video player which is very popular and used by many. Uh if is that amount is if they are offering for a free, use that or if you are offering a very minimal cost and it is something worth from from the point of whatever the service that they are giving, you can use it. Or if you wish to build a player of your own, that also can be done. and it is not very complex. Okay. Next. Next we have is the section of

### 00:27:20 · Speaker 1

comment section and the suggested videos, okay? Now let us probably, one second. So I have opened Ajtech for some other reason and I'll explain that in a while, okay? Next, let us go to my channel Uncommon Geeks, okay? I'll open one video and I'll explain what is very, very important here, okay? So videos, let's say

### 00:27:47 · Speaker 1

let's go to some video where I have so many comments. Okay? So, in this video now you are observing this video, okay? So where we have designed the architecture pretty much similar to this only, correct? So where in the center you have the video and the right hand side you have suggested videos, you have a player here and observe the things carefully now. I'll show you one flow, okay? So in interview this doesn't happen. Interview question immediately directly asked for just for your analysis and how you should think, I'm just showing you. So I'm scrolling down, okay? And we are seeing some comments here. Okay.

### 00:28:21 · Speaker 1

You observe a scrolling on the right side. So there were only few suggestions were loaded and whenever you scroll down new suggestions are getting added, okay? Again I'm scrolling down.

### 00:28:32 · Speaker 1

So new set of comments started adding here. Correct? So again whenever you scrolling right, so new set of suggested videos are getting added here. Vasanth there is no rocket science in this. We all know how pagination works and how things get added, okay? I'm not very fascinated by the suggested videos pagination that is quite straightforward where every time whenever you're hitting a end of the page or whatever the loaded content end of the loaded content you can load the new content. Many libraries are there, there are built-in mechanisms to do that, that is fine. Let us focus on the comment section pagination, okay?

### 00:29:02 · Speaker 1

So, let's say you you have loaded till here, correct? To certain extent. Then the next set of comments got loaded for this particular video, correct? Now, here are my questions to you regarding this.

### 00:29:14 · Speaker 1

whenever you hit the end of the current loaded comment section, you are going to the next set of comments, correct? So there is a problem called consistency here. Why what is consistency problem is, let's say in the comments you have filtered it like sort by uh new comments on top, top comments or newest first something like that. Newest first basically refers whoever has commented most recently, they are going to be on top, correct? So now you are scrolling to the end, correct? And whenever you are scrolling to the end, it is obviously it is not only who you are the one who is watching.

### 00:29:44 · Speaker 1

the video, correct? There are thousands of people out there who are watching the video. And many might have added a comment by that, let's say you watched the video for five minutes, in that five minutes probably let's say hundred people have added the comments. So now whenever you are scrolling to the end, so as per the default filter you have selected, newest, newest comment should be on top, correct? But your local whatever the comment that you have, you don't have the newest comments. So in the pagination now, you are you gonna get the whatever the index or however the logic that you have built, next set of

### 00:30:14 · Speaker 1

comments after that. Okay? Because next set of comments if you get after that, they they could be also the newest, not the oldest, correct? uh Hope you're getting whatever I'm saying. So, in that cases, what is the typical way you will do? That is question number one. Question number two, let's say if it's making very confusing for you, let us avoid the newest and the oldest. Let's keep the problem very simple. Let's say you are whatever the order that you have got it, most recent you have got and the oldest you are fetching on from the during the pagination, okay? Now here also home

### 00:30:45 · Speaker 1

Let's say certain comments are edited whenever you are scrolling to the end, okay? And those edited comments are not definitely reflected on the screen because you are having a old instance of comments, correct? So during the pagination, are you gonna update the old comments which have been modified or you're only gonna fetch the new set of comments and add it to the list?

### 00:31:06 · Speaker 1

Hope you all got the problem. I'm going to explain the problem once again. So let's say you have a pagination where newest comments you show on top, oldest comments are added from the behind, okay, whenever you do the pagination. And whenever you're doing the pagination, certain comments which are already loaded have been edited. So are you going to update those comments or not? So this is a typical system design question. Why I'm asking, I'll tell you. So the problem here is

### 00:31:31 · Speaker 1

whenever you think of editing a already present comments it is not that easy. Okay? Because you need to go to particular comment and particular sub comment or reply what we call reply ID and the comment ID and that particular section you need to update it and if you are using react you need to rerender that component so sometimes if you not structured your project properly there is a chance that entire comment section can be rerendered correct? So you have to avoid all these problems number one and number two is if you are not doing

### 00:32:01 · Speaker 1

this. Let's say you are not updating the comments, then there is a problem where consistency, like I watching a video and you watching a video, we have a different views of the same video. So, if you systems like YouTube sometimes may not expect that, correct? So now, let us how to solve this problem, let us see, okay?

### 00:32:19 · Speaker 1

How to solve this problem is, So, in the comment, now we have to do the pagination. So you got the pros and cons of each approach. So if you're gonna update the new comment, whenever you're doing the pagination, if you update the already existing comments, you'll have some performance effect. If you're not updating that, definitely the system will be faster, correct? So if I just write the advantages and disadvantages here, okay?

### 00:32:42 · Speaker 1

So basically now we have two approach approach one

### 00:32:47 · Speaker 1

like that only you need to do, okay, in the interview as well. Approach one where you are doing the pagination. Okay? And we have something called approach two.

### 00:32:57 · Speaker 1

approach to pagination

### 00:33:01 · Speaker 1

pegination with update. Okay? pegination without update.

### 00:33:09 · Speaker 1

pagination without update. Okay, two two two main categories we have. What is the pagination with update advantage, uh, consistency?

### 00:33:19 · Speaker 1

Correct?

### 00:33:21 · Speaker 1

So we we have the consistency. Like basically we show most realistic data, correct? These are the pro.

### 00:33:30 · Speaker 1

And what is the con?

### 00:33:32 · Speaker 1

It is slower. Correct? It is comparatively slower. Because definitely it involves some amount of processing, right? You don't have to just update the already only you don't have you are not showing the only the new comments. You also also update the already existing comments. Correct? Now let us come here and see.

### 00:33:50 · Speaker 1

What is pro here? Vagination without an update. Vagination without an update uh without an update process is definitely faster. Con you already know. Con is it is

### 00:34:02 · Speaker 1

con is it is not consistent.

### 00:34:05 · Speaker 1

correct? Pro is this and con is

### 00:34:10 · Speaker 1

con is it's not consistent. Correct? Because if three people are watching the video at a point in time, they may see the different set of the comments at at that. So now you as a developer need to give a suggestion to the interviewer like which is good. So definitely if you ask me,

### 00:34:28 · Speaker 1

pagination without update is a good idea. The reason being there is always a chance of inconsistency. Correct? I opened the video, hundred comments were there. Another opened the video, hundred fifty comments are there and I'm watching the video, he's watching the video. So there is already a inconsistency between the two unless I refresh my page. So that problem is not newly introduced by me, that problem already exist. Correct? And there's no effort right now to solve the problem by YouTube itself. Correct? So inconsistency is fine. So I would prefer to go with this approach, pagination without an update, faster,

### 00:34:58 · Speaker 1

after the processing but I am fine having the non not consistency so this is your opinion now there is also one important thing that you need to consider here let's say the video says about uh some two countries and the video is saying like this country economy is much higher compared to this country okay everybody are appreciating him for making that video but the very essence of the video could be wrong like whatever his fact that is shown in the video could be wrong so somebody might add a comment with a very descriptive

### 00:35:28 · Speaker 1

actively explaining this particular video is totally wrong, these facts are wrong, whatever the country that is having higher economy is not having higher economy, the other country itself has a higher economy. So these are called the priority comments. So among all the comments, certain comments can be having high priority. If you don't show this comment to a user, he might get misled, correct? So who is gonna decide which is a high priority comment? Definitely the back end with machine learning and other algorithms, you can differentiate certain comments are the high priority comments. So you have to propose a solution to the interviewer.

### 00:35:58 · Speaker 1

I'm just giving certain examples how your mindset should be. So we will go with the pagination without update but we'll also have an option to have a priority comments. Let's say during the pagination if you send me some priority comments with the main comment ID and the reply ID I will update that. Or if it's a new comment just send the comment ID I'll insert that on top. The reason for that is that might change the way the comments are working. Like it is in one direction now after this it might get turned into different video or whatever the comment that you wanted to add also might get changed after reading that.

### 00:36:28 · Speaker 1

priority comment. So I will go with the option of pagination without update with the concept of the priority comments as an option, okay? So that's what I want to discuss with three we solve two problems in this now. The video player and the comment section now.

### 00:36:44 · Speaker 1

Let's go to the design of the second thing that we discussed that is the live streaming, correct? Live streaming has its own set of challenges, how you're going to solve the live streaming etcetera, okay? The that's the reason why I had opened the Aaj Tak live. I don't know whatever they are streaming, I'm not much concerned on that, okay? So and there's nothing like a recommendation to watch Aaj Tak. I just searched any particular live streaming video. Obviously news are the best way to get the live streaming. So I'm opening some news, okay? And I've paused the video long back only. So this you're seeing this live streaming.

### 00:37:14 · Speaker 1

why I'm showing this is in interview also this might happen interviewer might show you this the reason for that is see one thing that is getting different than the normal streaming is the

### 00:37:25 · Speaker 1

normal video whatever I showed you here is the comment section. Correct? So there are right now around eleven thousand eight hundred seventy six people are watching. And if you observe this, the comments are been flooded like anything. Correct? This looks like an easy problem to solve with help of page and other things but it is not that easy. Okay? So let's say if you want to design the component for the live streaming, it pretty much remains the same as this. There is not much of a difference. Only the added section is the rather having this comment section, it has a live comment section. So component architecture remains

### 00:37:55 · Speaker 1

as it is, okay? Now, so here we have this live streaming and so many comments are be getting populated every second, correct? Tell me what is the approach that you would think in case if you are someone who already know the right approach for this live commenting, please mention that in the comment section, okay? You can mention the video timing and add that in the comment section, what is the right way to use the live streaming, live commenting, if not I'm gonna explain. But if before I explain what is about the live commenting, it's already close to thirty eight minutes that I've made a video with with non

### 00:38:25 · Speaker 1

obviously there is a lot of research that has gone into making this video. So please like the video and subscribe to my channel and press the bell icon if you're not already done so. And add a comment whatever you felt so far. The reason for that I always say I have only motto of I help want to help the candidate to clear their interview. So if more likes more comments video becomes visible for a lot whenever it is visible for a lot there is a high chance I get more subscribers and the followers. Definitely the there is a high chance I would able to reach my cause very soon. Okay. So please like and comment about the video before watching the further, okay? Now,

### 00:38:58 · Speaker 1

I was discussing about the live commenting. I assume some of you might have already commented like how live streaming live commenting works. If not, let us start discussing certain approaches in the regarding the live commenting. Okay? So,

### 00:39:13 · Speaker 1

what are the what are the approaches that are possible for the live comment? Okay? So, I I'll explain whatever the things that are happening. Basically, there are some ten comments or some x number of comments which are loaded whenever the live streaming video loaded, correct? Further comments are being added in a periodic interval, correct? And as you can see here, you can always scroll up scroll up and read only certain number of old comments, okay? This is the reason why you need to look at the system.

### 00:39:43 · Speaker 1

before designing it. So they are not allowing you to see all the one lakh comments that are happened before what you came or all the comments that are happened in the past. There is certain scroll whatever the scroll they have right in that interval whatever has been commented you can see. For example now it is at whatever let's say it's like one p.m. you are watching the video. All the all the comments that came for example some two hundred comments that came before one o'clock can be seen on the screen. Correct? So how what are the different mechanisms that we can use to solve that are

### 00:40:15 · Speaker 1

So what we can do is, let me just start adding those mechanisms of

### 00:40:22 · Speaker 1

mechanisms of live commenting. Okay? How we can basically achieve it? That's what I mean here, mechanisms of live commenting. Okay?

### 00:40:31 · Speaker 1

So one easiest way is what we you are generally does is polling. Okay? Second is server sent events.

### 00:40:43 · Speaker 1

third definitely is sockets. Okay? I'll explain about each of them and this is the same way how you need to also do in the interview. Okay? List them, explain the pros and cons and tell which approach suits best for you. Okay? So in the polling we also have something called short polling. I'm very sorry if my spelling of polling is not correct. I think it is right. Okay? Short I'm not that expert in English spellings actually.

### 00:41:09 · Speaker 1

long pooling, huh? pooling. long pooling and short pooling. okay. I don't know it is not pooling it could be polling only. okay. Basically I mean I'll explain what I mean so if I made a spelling mistake please correct it, okay. Servers and events have no subsections as such, okay. So what do I mean by polling here is client make a request to server at a consistent interval time or a periodic interval of time, okay. Let's say every five second you make a call, okay.

### 00:41:39 · Speaker 1

three five second you make a call and get the data. Let us quickly see what is happening in YouTube.

### 00:41:45 · Speaker 1

I'm going to the network section, okay? I'm going to network section and I'm clearing all the things. If you observe, get live chat is called once, then get live chat is called again, okay? And the get live chat is called periodically, okay? So, every X interval you're seeing, right? In almost at every second, almost every second I think, it is it is kind of fetching the new set of comments from the back end and appending it to the existing set of the comment that it already has.

### 00:42:15 · Speaker 1

and after a point, for example, they might have made a array with a limited length and obviously all the old items will go off and only the new items will be remaining. Correct? This is the easiest way where you constantly poll and get the data and add it, okay? But there are two different types of polling. One is short polling and long polling. What is short polling? uh you call uh at a periodic interval and back end immediately sends all the new whatever the comment that has immediately. Another thing called the long polling. What is long polling means? Let's say you called the back end but back end doesn't have any new

### 00:42:45 · Speaker 1

comments. That might happen, right? There are many people who are live streaming. And if YouTube cannot uh call back end every one second to get the new set of comments, even in those criteria, correct? Because there may not many new comments. But it will make a call and the back end will wait for a particular interval of time, like fifteen seconds, twenty seconds, twenty five seconds. That is a interval with for which the client waits, okay? For a particular request to fail. After twenty five seconds or else generally what back end does is it will take a request, it will wait for some let's say twenty seconds is when the UI

### 00:43:15 · Speaker 1

considers as the request has failed. After a fifteen second, it will see if any new data is there, whatever it is, it will flush. If there is no new data also, it will flush with the empty array. Okay, this is called the long polling. Advantages of long polling is

### 00:43:27 · Speaker 1

short polling disadvantage you know you call you may not have anything so you are simply consuming a server resource for nothing whenever there are no comments for example for the long polling advantage is you take you are waiting for a significant amount of time definitely there could be a high chance where some comments come and you will return so comparing short law polling and long polling long polling is better in certain areas where you are not expecting something to happen very often okay next thing is the server sentiments so this is very very optimal approach compared to the polling

### 00:43:57 · Speaker 1

server sent events are nothing but server will send a trigger to you and whenever there are triggers you will be making a network call. Okay? So there are different ways with which server sent events can be configured. If you are not at all knowing please mention that in comment section I'll make it but I'll not deviate this video to explain the server sent events in detail. Very simple words there is a trigger from the back end and you UI knows this trigger means I need to call this API it will call and get the data. Okay? So it's very optimal because back end knows when there are new set of comments it will inform the UI and the UI makes a call and gets the data.

### 00:44:27 · Speaker 1

So this is server sent events, very optimal compared to the polling approaches, okay? But it is not suitable in all the scenarios because server sent events will have its own performance problems, okay? Because client will have a connection dedicated in the server. All the clients, we have two hundred billion plus users. If two hundred billion, no, two hundred billion, very huge user base. I think two billion users YouTube has, around two hundred crores.

### 00:44:52 · Speaker 1

If all the 200 crore people, let's say they will not watch at the same time, but let's say just at least 10% of them watch the video at the same time, that is around how many, I think 20 million, correct? 20 million people watching at some time. From 200 crores, not 20 million, 200 crore user if you have, 20 crore people watching it at one particular point of time, then 20 crore connection has to be established with the server, correct? And there are chance where definitely not 20 crore, whoever is watching the live streaming, those many connections will be established and

### 00:45:22 · Speaker 1

number also will be significantly high for the server, correct? And there may not be any update happening on the server. In such cases, this connection should be wasted. And that resource cannot might have been used for some other things, okay? Next, we have something called sockets. Most of you know what are sockets. So server difference between server sent events and the sockets are, sockets are two way connection. Server sent events are one way connected, like only the back end will send certain things to UI and UI makes a modification. Sockets are nothing but two way connection. The best example are the

### 00:45:49 · Speaker 1

uh messaging. Whenever you're doing messaging in the WhatsApp or whenever you're chatting on the web with some support and all you'll do right? Every site a lot of sites have a support central where you can do the live chatting. All those work actually on the sockets. Because client also can send certain things to a connection and the server also can send back certain things to connection. It's a two way. Okay? Servers and servants are one way. They're only back end will send certain things to the client. So these are the three different approaches with which the the we can get the comment from the live commenting we can enable live commenting.

### 00:46:19 · Speaker 1

interviewing in the YouTube. This is very good. Interviewer will be definitely happy if you are able to approach, explain all these problems. Next question that interviewer will ask is, Vasant, what is the approach that you suggest for us? Like if you are building YouTube now, which approach you are gonna go? Whether short polling, long polling, service and events in the sockets. Very first thing I'm not gonna go with sockets, okay? Because sockets are very very costly compared to all the things because you are establishing a channel and this is not like a charting. uh This is just a one way. Somebody sends a comment, somebody replies there and

### 00:46:49 · Speaker 1

Again you have to send a comment. It is like group chat. Everyone messaging in one direction. It's not like a two way. Like you sending it's going to server coming back no. Both are sending to one server and they can both can see the comments in the live. So I will not go with the sockets. So server send events.

### 00:47:04 · Speaker 1

I might go. So server sent events are also good, but considering the scale of YouTube where we have billions of users, server sent events also will consume lot of energy with the help of by making the connections. So many connections are open and sometimes these connections could be meaningless. Simply server utilization is high, so I may not go with the server sent events also. I will go with polling. Don't think I'm biased looking at whatever I showed you. Obviously, you also felt like YouTube is doing a polling at every second, correct? Why why I'm selecting the polling is, so

### 00:47:34 · Speaker 1

You already know what is short polling and long polling I've already explained. Polling, I will not go with this typical polling where I call it every one second and get. No, I will not do that. I will use a algorithmic way of determining the duration. Like for example, Aaj Tak, whatever I was saying, there are for foreigners who are watching, there is lot of YouTube, there are lot of foreign news channels which are being streaming. Some channels might have very limited comments that are happening on a day-to-day basis. Some live streaming, some channels, some news channels

### 00:48:04 · Speaker 1

that are present live streaming on YouTube might have limited users and limited comments. Some YouTube channels with that are live streaming, news channels that are live streaming might have huge user base and so many comments. So I'll do a short polling itself but the whatever the duration with which I make a call is not predefined.

### 00:48:19 · Speaker 1

So that that is something that is determined depending on the video which I'm watching and this number is calculated by a machine learning algorithm by watching that channel periodically. Definitely there will be a default value when a new news channel starts streaming or new live streaming comes. But after a point whenever the algorithm becomes smarter it will tell me this is the duration with my lot of analysts in the past this is the duration with which the live comments need to be updated and that duration I'll do a short polling. That seems better option for me considering the huge scale of things like the YouTube.

### 00:48:49 · Speaker 1

Okay? So this is the another problem that I want to discuss in live streaming. Last thing that I want to discuss here is, Vasant, what, how YouTube live streaming is working? This will be generally asked in the interview, like, what is the protocol with which the streaming is happening? Actually, there are many protocols for the live streaming, correct? Most popular ones that everyone aware of is a WebRTC, correct? So real web, web real-time communication, RTC stands for. One of the very, very popular framework, but only problem with WebRTC is, uh, let me just note down so that you guys also note it. properly live streaming

### 00:49:23 · Speaker 1

protocols. Okay? One is WebRTC.

### 00:49:28 · Speaker 1

Okay, and the second one, second one is RTMP.

### 00:49:33 · Speaker 1

third one is HLS. I've written certain things on the left so that I won't miss it out so I'm mentioning here. So these are the three popular live streaming protocols that are available. Vasanth, is it necessary for me to know these things before attending the interview? I would highly recommend you need to know. Okay? Why? Because you have to always explain the pros and cons of an approach and rule out some approach and take one approach like I mentioned here. Correct? So it's always essential for you to pick all the popular systems and analyze the popular system and take a note and explain that. Correct? So three popular systems are there, WebRTC, RTMP and HLS. So WebRTC like I said it is open source.

### 00:50:11 · Speaker 1

and it uses UDP. Okay? If you don't know what is UDP, user diagram protocol. Basically, it's a connectionless protocol and there is a high chance where some packets are lost in this particular uh with with UDP based one. Okay? And HLens is uh very easy definition, HTTP live streaming. Okay? So this is built by Apple.

### 00:50:32 · Speaker 1

in two thousand eight, okay? So definitely as you can guess I have already read about all these protocols in the past. I would advise you also need to read like this whenever you are practicing for the system design, okay? RTMP is real time messaging protocol.

### 00:50:48 · Speaker 1

real time messaging protocol. It uses TCP. Okay? Reliable.

### 00:50:55 · Speaker 1

fast. Okay? It's reliable and it is fast, okay? compared to other frameworks, okay? And it is meant for uh I mean it is it's not like a very old one. It is newly designed for meeting the modern day needs. So obviously you know which which protocol that I'm going to pick, I'll be picking the RTMP. In fact, you YouTube also uses the RTMP protocol for the live streaming purpose. Not the live streaming, even the normal streaming in YouTube also happens with the help of RTMP, real time messaging protocol. So what are protocols? You very well know it's just a set of

### 00:51:25 · Speaker 1

rules that is agreed between the client and the server. Every protocol will have certain set of rules which will make it to be fast, slow and certain different aspects. So and also very important thing to note here is RTMP uses the TCP. Okay? TCP is a connection oriented protocol. So a connection is established between the client and server. So no packets are lost, more security and even if you due to your internet issue if you lose certain packets, after you get those packets whenever your internet is up, you there is a chance where you can combine them on the UI and you can show it to the user. So because of all

### 00:51:55 · Speaker 1

reason RTMP is come recommended for even it is used in Facebook live, YouTube live and maybe other lives. These are two systems I've clearly studied. Other systems I don't know but lot of live streaming apps on the web might be using the RTMP as a protocol. So YouTube also using the RTMP protocol. See if you explain all these things to interviewer like how I explained, what are the mechanisms of live commenting, what are the problems with the pagination with the commenting. If you explain all these things to interviewer he'll be terribly happy, correct? Like he knows so many things.

### 00:52:25 · Speaker 1

and he's taking each approach one by one and he's uh scratching why this is not suitable for this application and why this only need to be used. He'll be very happy looking at your knowledge about a particular um system design. So much he already know, definitely he'll be able to contribute whenever he's inside the company, okay? So, after all this, there is one last thing that I want to tell. So where we are pretty much done with the system design this one. Last thing is some people spend some time also on the API architecture, like whether to use GraphQL or to use the JSON.

### 00:52:55 · Speaker 1

and uh Raph Kiala or the rest and how typically what are the APIs that you want and each API contain what all parameters that only if the time permits with my experience of giving and taking interviews I generally we haven't not focused on the API design as such because that's going to take much time and I don't see a lot of challenges in there definitely certain extent there are certain challenges but I don't see the problems like I discussed will happen there because you go to API designing once all these things are already well defined okay so pretty much that's all about this

### 00:53:25 · Speaker 1

one last thing is uh read about this youtube.github.io sspfjs. SPF structured page fragments that is something that YouTube uses internally for the navigation purpose. So I'm done with my system design but this is my time to explain you certain things so that you can go and read. So where a lightweight JS framework for fast navigation of page updates from YouTube. So how YouTube basically updates the page what things are updated what things are not updated whenever you're navigating are clearly explained here. Link to this will be in the description section please go ahead and read it. Okay. So that's all about this video.

### 00:53:55 · Speaker 1

In case if you like the video, please like the video on YouTube channel and add a comment whatever you felt and subscribe to my channel Uncommon Geeks and press the bell icon. Next, I will be designing a stock market application from the scratch to end, very, very in depth, same way how I did. I'll be picking lot of complicated problems and how those problems can be solved, I'll be explaining. So if you want to get the notification for that, you have to press the bell icon and subscribe so that you get a notification instantly. And whatever the material that I roughly added here, I am not going to be adding it to my GitHub, anything as such. But if you want to

### 00:54:25 · Speaker 1

those whatever the drawing that I did or the whatever the requirements I added, mention that in the comment section. I'll be reserving them. If you want, I'll be upload them. And start my GitHub project whenever you are downloading so that that becomes little popular. And follow me on LinkedIn and Medium. So if you have some questions that cannot be asked in the YouTube comment, you can ping me in LinkedIn. I'll try to answer them. And Medium, I'll be writing every week one new article on the interview preparation that will definitely help you. So follow me on Medium and subscribe the new newsletter. Thank you so much for watching. Catch you in next video.
