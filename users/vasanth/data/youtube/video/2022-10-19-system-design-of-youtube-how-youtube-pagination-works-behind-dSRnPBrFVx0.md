---
id: dSRnPBrFVx0
title: '🔥 System design of Youtube 🔥 | How Youtube Pagination works behind the scenes
  #youtube #facebook'
date: '2022-10-19'
url: https://www.youtube.com/watch?v=dSRnPBrFVx0
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
  \nJavaScript Custom implementation| polyfills  introduction: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s"
author: careerwithvasanth
duration: 00:16:25
model: saaras:v3
transcript: true
---

# 🔥 System design of Youtube 🔥 | How Youtube Pagination works behind the scenes #youtube #facebook

## Transcript

### 00:00:00 · Speaker 1

correct? So during the pagination, are you gonna update the old comments which have been modified or you're only gonna fetch the new set of comments and add it to the list?

### 00:00:10 · Speaker 1

Hope you all got the problem. I'm going to explain the problem once again. So let's say you have a pagination where newest comments you show on top, oldest comments are added from the behind, okay, whenever you do the pagination. And whenever you're doing the pagination, certain comments which are already loaded have been edited. So are you going to update those comments or not? So this is a typical system design question. Why I'm asking, I'll tell you.

### 00:00:36 · Speaker 1

the video detail screen

### 00:00:40 · Speaker 1

So here what I'm doing is this is the place as you all know the video gets played, correct? I'm just increasing its size.

### 00:00:49 · Speaker 1

Okay

### 00:00:51 · Speaker 1

And this is the right side where all the suggestions happen. Correct? So I'm taking another box.

### 00:00:58 · Speaker 1

all the suggested videos will be present here. Okay? And also have the this section where this is section where all the like, share, uh unlike, embed, all those things will be present here. Correct? And then this last section is the comment section. Quickly let us name so that in the whenever we are explain the interview, you are clear. Video streaming. Okay?

### 00:01:24 · Speaker 1

or video player. That's probably the right word. Okay. Okay, video player, let me increase the size so that you all can see. Video player.

### 00:01:35 · Speaker 1

Then we have suggested videos, correct? Suggested videos. Then

### 00:01:44 · Speaker 1

Then we have certain things called comment section. Okay.

### 00:01:49 · Speaker 1

comment section

### 00:01:52 · Speaker 1

Then we have this is what I can call like like share like share embed all these things will happen in this okay. So definitely suggested videos will have certain like images with a thumbnail etcetera correct. So control D.

### 00:02:11 · Speaker 1

सो वेयर यू कैन सी मल्टीपल सजेस्टेड वीडियोस लाइक दिस, करेक्ट? वन बिलो अनदर यू विल बी हैविंग द मल्टीपल वीडियोस।

### 00:02:17 · Speaker 1

So something like this, correct? Suggested videos are going to be like this on the right hand side. So this is the typical UI of the bare bone. Don't think like this is the your whatever the beautiful design that your your developer gives. So this is a bare bone of the how YouTube looks like, correct? YouTube video detail screen looks like this. Now, now there are certain problems in each of this section. One by one let us going to discuss and let us solve. The first problem is the the video player itself, correct? So video player if you see you have certain buttons on here.

### 00:02:47 · Speaker 1

correct? That start, stop and all are here. That I don't know where the shapes are there, but I'm just gonna keep this is the start and this is the stop and you will have certain buttons like next and the previous, correct? You will have buttons like the forward and backward buttons, correct? Forward and backward buttons, sometimes on the right hand side you set you choose the settings to increase and decrease the

### 00:03:13 · Speaker 1

the video quality etcetera, correct? So there are many options that are associated with this video player. Sorry, I did forgot to add O here. So,

### 00:03:24 · Speaker 1

How you gonna build this player is the first question. Okay, now let us say you are in a system design interview and the interviewer ask, Vasanth, this is the video player, whatever you're saying. It is very beautiful player with lot of options, like we already discussed it as like, share, and video playing, pausing, forward, backward, changing the quality, adding the subtitles. There are a lot of functionalities associated with this video player, correct? So generic component, if you consider from React point of view, it's a generic component where lot of attributes are passed to it, like for example, certain videos

### 00:03:54 · Speaker 1

cannot be uh quality cannot be increased to HD because video itself is not in HD, correct? And there will be a lot of other options like subtitles. Some videos have a subtitles where you can switch to different languages, some doesn't because author hasn't uploaded that JSON or whatever the file that is required for the subtitles. So this is a very generic component in terms of React if you think and what all components that you would pass to that uh particular video player component, depending on that it will show those options, correct? Obviously every video will have certain things that is very common, start, stop and the quality setting, they are all very common.

### 00:04:24 · Speaker 1

correct? So now, how you're going to design this player, correct? So if you ask me now, and this then what is the next question that I'll ask for the interviewer is, what is the timeline that we have for this delivery of this entire product?

### 00:04:36 · Speaker 1

Let's say he wants to go with a beta, the first version of the app in next three months. Then I would say, see video player is a crux of this entire layout. There are a couple of options that I would give him. One, if there is any proven player which is already doing the fantastic job and that is at a very cheaper cost for us, let us first go and use that third party video player and embed into our tool. Let us not build a tool of our own. The reason for that is very clear, like I said, there is lot of challenges that comes with a player, like for example, you're getting the video and suddenly

### 00:05:06 · Speaker 1

video becomes slower. uh sorry, internet becomes slower. Then whenever how you fit the next set of packets becomes slower, but you shouldn't see the jitter on the video, correct? So there has to be some process in the back end which is taking care of these things. So video playing is a very, very complex process than you think. So my advice is if there is a possibility of taking a different third party tool, then let us take the tool for the beta. Further let us enhance it internally and add our own tool. Now interviewer will may say yes to that or interviewer may also say no to that. Like we have a limited budget, we cannot

### 00:05:36 · Speaker 1

third party video embedding tool and it's a crux of the entire project the amount could be high. Okay. So in such cases definitely we can build a video player of our own. It is not some rocket science. Don't worry. If you want I'll link one blog which I read recently where they very very clearly explain how to build a video player. So it it can be easily built just with HTML video tag and

### 00:05:56 · Speaker 1

There are a lot of media source, HTML media tag, video tag in the media source. It's a JavaScript API. With these two things you can easily build a player like YouTube, very basic player like YouTube in just few hours. There are a lot of tutorial outs there with which you can build the video player. But there will be a lot of intricacies which you might miss, okay, whenever we build like as I said the adaptability, adjusting the quality, all those things may take little time if you build a your own YouTube player. Now, we are solved the first problem of video player. Don't think this I

### 00:06:26 · Speaker 1

I am not getting into all the problems, whatever the problem that is very very um visible on the top layer, I'm I'm touching them. Next, next problem which we have is so to summarize, video player, whether the if the timeline is less, let's use a third party video player which is very popular and used by many. Uh if if that amount is if they are offering for a free, use that or if you are offering a very minimal cost and it is something worth from from the point of whatever the service that they are giving, you can use it. Or if you wish to build a player of your own, that also can be done and it is not very complex. Okay. Next. Next we have is the section of

### 00:07:01 · Speaker 1

comment section and the suggested videos, okay? Now let us probably, one second. So I have opened Ajtech for some other reason and I'll explain that in a while, okay? Next, let us go to my channel Uncommon Geeks, okay? I'll open one video and I'll explain what is very, very important here, okay? So videos, let's say

### 00:07:28 · Speaker 1

let's go to some video where I have so many comments. Okay? So, in this video now, you are observing this video, okay? So where we have designed the architecture pretty much similar to this only, correct? So where in the center you have the video and the right hand side you have suggested videos, you have a player here and observe the things carefully now. I'll show you one flow, okay? So in interview this doesn't happen. Interview question immediately directly asked for just for your analysis and how you should think, I'm just showing you. So I'm scrolling down, okay? And we are seeing some comments here. Okay.

### 00:08:02 · Speaker 1

You observe a scrolling on the right side. So there were only few suggestions were loaded and whenever you scroll down new suggestions are getting added, okay? Again I'm scrolling down.

### 00:08:12 · Speaker 1

So new set of comments started adding here. Correct? So again whenever you scrolling right, so new set of suggested videos are getting added here. Vasanth there is no rocket science in this. We all know how pagination works and how things get added, okay? I'm not very fascinated by the suggested videos pagination that is quite straightforward where every time whenever you're hitting a end of the page or whatever the loaded content end of the loaded content you can load the new content. Many libraries are there, there are built-in mechanisms to do that, that is fine. Let us focus on the comment section pagination, okay?

### 00:08:42 · Speaker 1

So, let's say you you have loaded till here, correct? To certain extent. Then the next set of comments got loaded for this particular video, correct? Now, here are my questions to you regarding this.

### 00:08:55 · Speaker 1

whenever you hit the end of the current loaded comment section, you are going to the next set of comments, correct? So there is a problem called consistency here. Why what is consistency problem is, let's say in the comments you have filtered it like sort by uh new comments on top, top comments or newest first something like that. Newest first basically refers whoever has commented most recently, they are going to be on top, correct? So now you are scrolling to the end, correct? And whenever you are scrolling to the end, it is obviously it is not only who you are the one who is watching.

### 00:09:25 · Speaker 1

the video, correct? There are thousands of people out there who are watching the video. And many might have added a comment by that, let's say you watched the video for five minutes, in that five minutes probably let's say hundred people have added the comments. So now whenever you are scrolling to the end, so as per the default filter you have selected, newest, newest comment should be on top, correct? But your local whatever the comment that you have, you don't have the newest comments. So in the pagination now, you are you gonna get the whatever the index or however the logic that you have built, next set of

### 00:09:55 · Speaker 1

comments after that. Okay? Because next set of comments if you get after that, they they could be also the newest, not the oldest, correct? uh Hope you're getting whatever I'm saying. So, in that cases, what is the typical way you will do? That is question number one. Question number two, let's say if it's making very confusing for you, let us avoid the newest and the oldest. Let's keep the problem very simple. Let's say you are whatever the order that you have got it, most recent you have got and the oldest you are fetching on from the during the pagination, okay? Now here also home

### 00:10:26 · Speaker 1

Let's say certain comments are edited whenever you are scrolling to the end, okay? And those edited comments are not definitely reflected on the screen because you are having a old instance of comments, correct? So during the pagination, are you gonna update the old comments which have been modified or you're only gonna fetch the new set of comments and add it to the list?

### 00:10:47 · Speaker 1

Hope you all got the problem. I'm going to explain the problem once again. So let's say you have a pagination where newest comments you show on top, oldest comments are added from the behind, okay, whenever you do the pagination. And whenever you're doing the pagination, certain comments which are already loaded have been edited. So are you going to update those comments or not? So this is a typical system design question. Why I'm asking, I'll tell you. So the problem here is

### 00:11:12 · Speaker 1

whenever you think of editing a already present comments it is not that easy. Okay? Because you need to go to particular comment and particular sub comment or reply what we call reply ID and the comment ID and that particular section you need to update it and if you are using react treaty to re-render that component so sometimes if you not structured your project properly there is a chance that entire comment section can be re-rendered correct? So you have to avoid all these problems number one and number two is if you are not doing

### 00:11:42 · Speaker 1

this. Let's say you are not updating the comments, then there is a problem where consistency, like I watching a video and you watching a video, we have a different views of the same video. So, if you systems like YouTube sometimes may not expect that, correct? So now, let us how to solve this problem, let us see, okay?

### 00:11:59 · Speaker 1

How to solve this problem is, So, in the comment, now we have to do the pagination. So you got the pros and cons of each approach. So if you're gonna update the new comment, whenever you're doing the pagination, if you update the already existing comments, you'll have some performance effect. If you're not updating that, definitely the system will be faster, correct? So if I just write the advantages and disadvantages here, okay?

### 00:12:23 · Speaker 1

So basically now we have two approach approach one

### 00:12:28 · Speaker 1

like that only you need to do, okay, in the interview as well. Approach one where you are doing the pagination. Okay? And we have something called approach two.

### 00:12:38 · Speaker 1

approach to vagination

### 00:12:42 · Speaker 1

pagination with update. Okay? pagination without update.

### 00:12:50 · Speaker 1

pagination without update. Okay, two two two main categories we have. What is the pagination with update advantage, uh, consistency?

### 00:13:00 · Speaker 1

Correct?

### 00:13:02 · Speaker 1

So we we have the consistency. Like basically we show most realistic data, correct? These are the pro.

### 00:13:11 · Speaker 1

And what is the con?

### 00:13:13 · Speaker 1

It is slower. Correct? It is comparatively slower. Because definitely it involves some amount of processing, right? You don't have to just update the already only you don't have you are not showing the only the new comments. You also also update the already existing comments. Correct? Now let us come here and see.

### 00:13:30 · Speaker 1

What is pro here? Pagination without an update. Pagination without an update uh without an update process is definitely faster. Con you already know. Con is it is

### 00:13:43 · Speaker 1

con is it is not consistent.

### 00:13:46 · Speaker 1

correct? Pro is this and con is

### 00:13:51 · Speaker 1

on is it's not consistent. Correct? Because if three people are watching the video at a point in time, they may see the different set of the comments at at that. So now you as a developer need to give a suggestion to the interviewer like which is good. So definitely if you ask me,

### 00:14:09 · Speaker 1

pagination without update is a good idea. The reason being there is always a chance of inconsistency. Correct? I opened the video, hundred comments were there. Another opened the video, hundred and fifty comments are there and I'm watching the video, he's watching the video. So there is already a inconsistency between the two unless I refresh my page. So that problem is not newly introduced by me, that problem already exist, correct? And there's no effort right now to solve the problem by YouTube itself, correct? So inconsistency is fine. So I would prefer to go with this approach, pagination without an update, faster,

### 00:14:39 · Speaker 1

after the processing but I am fine having the non not consistency so this is your opinion now there is also one important thing that you need to consider here let's say the video says about uh some two countries and the video is saying like this country economy is much higher compared to this country okay everybody are appreciating him for making that video but the very essence of the video could be wrong like whatever his fact that is shown in the video could be wrong so somebody might add a comment with a very descriptive

### 00:15:09 · Speaker 1

actively explaining this particular video is totally wrong, these facts are wrong, whatever the country that is having higher economy is not having higher economy, the other country itself has a higher economy. So these are called the priority comments. So among all the comments, certain comments can be having high priority. If you don't show this comment to a user, he might get misled, correct? So who is going to decide which is a high priority comment? Definitely the back end with machine learning and other algorithms, you can define certain comments as the high priority comment. So you have to propose a solution to the interviewer.

### 00:15:39 · Speaker 1

I'm just giving certain examples how your mindset should be. So we will go with the pagination without update but we'll also have an option to have a priority comments. Let's say during the pagination if you send me some priority comments with the main comment ID and the reply ID I will update that. Or if it's a new comment just send the comment ID I'll insert that on top. The reason for that is that might change the way the comments are working. Like it is in one direction now after this it might get turned into different video or whatever the comment that you wanted to add also might get changed after reading that.

### 00:16:09 · Speaker 1

priority comment. So I will go with the option of pagination without update with the concept of the priority comments as an option, okay? So that's what I want to discuss with three we solved two problems in this now. The video player and the comment section now.
