---
id: QQp4VLav72s
title: How Social scrolls infinite? Frontend System design of social Media @instagram
  |@tiktok
date: '2024-09-26'
url: https://www.youtube.com/watch?v=QQp4VLav72s
description: "#interview   #react #reactjs  #frontend  #javascript \n\nIn this Video\
  \ I have explained how to design of social media application. We have few major\
  \ problems in building Social Media application, which are listed below. \n\n1.\
  \ How to render a large list on the UI ? \n2. How to handle the Pagination ? \n\
  3. How to do resource optimisation ? \n\nMany more such interesting problems are\
  \ solved in the video, watch till the end and support. \n\nYoutube System Design:\
  \ https://youtu.be/QJe0cBjlgog?si=b9e8nVZKqIQPv6tw\n\n @careerwithvasanth   is a\
  \ Youtube channel dedicated to helping candidates clear their interview. There are\
  \ more than 150 videos and new videos will be uploaded every week. If you're seriously\
  \ preparing for interviews and looking for tips and tricks, please subscribe to\
  \ my channel and press the bell icon.\n\nYou can get more mock interviews here :\
  \ v=uW7MfzoD1po&list=PLmcRO0ZwQv4SwXLVpnKb_nFQx1Wd2XEjD&ab_channel=UncommonGeeks\n\
  \nTo get a dedicated one on one,  you can reach out to me here: https://topmate.io/vasanth_bhat\n\
  \nJoin CareerwithVasanth community to discuss with other developers: t.me/uncommongeek.\
  \ \n\nFollow me on LinkedIn - https://www.linkedin.com/in/careerwithvasanth/\n\n\
  Medium Blog https://mevasanth.medium.com/  \n\nJavaScript Interview preparation\
  \ series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nJavaScript Custom implementation/polyfills Series: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\n\
  \nFrontend system design series: https://www.youtube.com/watch?v=gN8LQTff21g&list=PLmcRO0ZwQv4RYUD10hUnWjWb-RRSpm3KM&ab_channel=UncommonGeeks\n\
  \nMAANG series for frontend developer: https://www.youtube.com/watch?v=s-b-txm_Gvk&list=PLmcRO0ZwQv4SNhbW4CI4vc-6IHBHCKzZN&ab_channel=UncommonGeeks\n\
  \nShorts for quick access to all frontend resources: https://www.youtube.com/watch?v=8ByBOT7Aehs&list=PLmcRO0ZwQv4SXtrTYIU_dPygZgOgYV81S&ab_channel=UncommonGeeks\n\
  \nTips for freshers: https://www.youtube.com/watch?v=hGIOIdPNNqE&list=PLmcRO0ZwQv4QBiZns-nYX5qnHKAepVeqH&ab_channel=UncommonGeeks"
author: careerwithvasanth
duration: 00:16:32
model: saaras:v3
transcript: true
---

# How Social scrolls infinite? Frontend System design of social Media @instagram |@tiktok

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Career with Vasanth YouTube channel. My name is Vasanth. I hope you all doing well. So as you know this is a series where we are explaining about system design. Like I told in multiple videos of mine, this is one of my favorite series where I like intersecting the different systems, understanding it end to end and explaining it to you guys. In this particular video, we are going to discuss the system design of a news feed or in layman term if I have to tell a social media application like Facebook, Instagram, Twitter, how do they basically render so much of a data, how do they handle messaging, a lot of problems, these big social media applications.

### 00:00:30 · Speaker 1

applications has. I'm gonna break it down step by step in this video. If you're not already subscribed to my channel Career Based Vasanth, please subscribe. I'm gonna bring more such content about interview and front end interview and career preparations. So without wasting further time, let's get started. So primarily I'm I'm gonna solving four problems in this particular video where first is rendering the largest, second is infinite scrolling and pagination, and third is handling live video commenting, fourth is resource optimization, okay? So let's go to the first one, rendering a large list.

### 00:01:00 · Speaker 1

okay? So what do I mean by rendering a large list? For example, like, like this is a list, whatever you're saying. So there's so many items, there are thousand items. So as you can see there, so many items that are there on the screen. So what would happen if you like have, like for example, let's take a simple implementation where you have an array where all the elements are keep getting added and you're using the map method to render the item. And whenever you keep loading an item, to load an every item, lot of resource are required, correct? For example, if the resource has an image, we need to make an API call.

### 00:01:30 · Speaker 1

and get the image. If it has so much of videos and other things, we need to get the video, textual information, you make an API call to get the data. So every time whenever a particular card is loaded, there's so much of processing like CPUs, GPUs, DOMs, all things we're getting basically used. So for example, let's imagine a list with thousand items. If we keep all the thousand items data on the RAM itself, okay, or from wherever we are accessing quickly, mostly it is in the RAM. So where we might start using so much of the resource of a particular browser.

### 00:02:00 · Speaker 1

or in terms of the resource of a machine, which will affect the overall performance of the system and sometimes a browser take a decision of like not giving so much resource to you, it will create in like hanging of your screen or sometimes you might have seen on Chrome that kill this page. So those kind of conditions might come because of the over over using of the resources. Okay? So what we can do is instead of loading all the cards or all the list that we want to show, how about we show only those that are visible for on

### 00:02:30 · Speaker 1

that particular time on the UI. So that's what uh called the virtualized list. What is virtualized list? Technically there is a complete list but we are virtually showing or technically there is no complete list. User is getting an impression there is complete list but technically there are only those many items that are actually visible for the that are actually can be fit on the screen. So it's called a virtual list not a real list it's a virtual list. Okay? The multiple packages to implement the virtual list. I have showing you this particular package react virtualized. So the

### 00:03:00 · Speaker 1

many folks of this and many other packages also where this is a demo that I picked from this where like for example in this screen one two three four five six. So there are only six particular DOMs uh or six particular divs which are being rendered. Whenever you scroll it whatever that div that was not currently in the view port that's going to be removed from the DOM and whatever is visible only that kind of used. There is one optimization that can be done here like instead of like just removing the DOM um there could only be fixed set of DOMs where

### 00:03:30 · Speaker 1

existing DOM instead of removing it you kind of reuse it. For example there are one two three four five six. The there is whatever the DOM that is just going there. Now instead of remove it from the complete memory reuse it and add it below. Okay? That is a technique that like that as well. But for the simplicity of this video we are going to stick to this basic virtualized list where whatever is visible on UI any given time only those are used for the rendering purpose. Okay? So the the instead of showing the complete list we are going to

### 00:04:00 · Speaker 1

show only those that fits in the UI that is called the virtualized list. So that is of the rendering a large list problem can be solved. In social media applications as you very well know that is so much of data you keep scrolling. So there has to be some way to render the list very efficient way that this is how virtualized list is a solution. Second thing is infinite scrolling and pagination. Okay. So every time when I ask this question in the interview I very commonly ask let's say you have to render a list of ten thousand items what is that you are going to do. Every single

### 00:04:30 · Speaker 1

person will say like I'm gonna use pagination or something. My question is like how actually you're gonna paginate? Like what technique you use? Everybody say a pagination technique that is they say we pass an index to the back end, the back end will process that index and returns the result. For example, you pass a page one and sometimes the size is dynamic, most of the time size is fixed. Like page one send me ten data, then I pass page two, they'll send next ten data. It goes on basically. But the problem with this particular approach is that's what I'm gonna that's what I want to explain this particular video. Let's look at these things in detail. uh Okay.

### 00:05:07 · Speaker 1

See if the problem with this approach is look at this particular thing. Okay? So this is called whatever the most common technique that everybody say in the interview, this is called an offset based approach. Okay? Where we are gonna send an offset to the server. So if you observe this very carefully where we have one, two, three, four, let's imagine this as the data, whatever we are showing on the UI. So that is on the page one. On page two we have five, six, seven, eight. On page three we have nine, ten, eleven, twelve. So imagine every number here represents a unique post that you see on any social media. Now, you requested for page one.

### 00:05:37 · Speaker 1

they sent you the page one, then you request page two, they sent you page two and page three, wonderful, it works like perfectly fine. But imagine a system like Facebook or Instagram where so much of a new content is coming like every second, correct? So by the time you for the simplicity sake I'm doing this, okay? Let's say you send the page one, they sent you one, two, three, four. And then like new data came, where the new data will be inserted? Definitely in the beginning, not at the end, because the Facebook or Instagram wants user to see the new content that is coming and not like pushing it at the end. So now one, two, three,

### 00:06:07 · Speaker 1

is pushed to the right. So zero minus one minus two minus three. Let's imagine this is a new content that came which came in the page one. So first you made a request to page one you got one two three four. Now you're making the request for page two which is obvious because you want the next screen content. But the whatever the content was here that is slided here now already. So whenever you're actually getting the page two's content it's not page two content whatever the content which you already have that only you are getting a part of page two content. This is the biggest problem with the offset based approach to show it to you very clearly.

### 00:06:37 · Speaker 1

I have drawn this table and explaining, okay? So remember this. So every time whenever they ask which approach you are gonna use, tell I'm gonna use offset based approach and this is the problem. This particular technique is suitable for those systems where the content is not really very dynamic. So there you can go with the offset based approach, okay? There is another approach called cursor based approach, okay? What is cursor based approach? So instead of like you making a request by a page number,

### 00:07:03 · Speaker 1

the back end itself will send you a cursor. Like for example, in the first request it has sent you one, two, three, four as the data. So the last index, the fourth item, whatever you got, will have a cursor. Every post for that matter will have a cursor, like this particular one will have a cursor, this one will have a cursor. All of these will have a cursor. Cursor in simple words, imagine like the post ID with our example. So now I have the fourth post ID, okay? So next time whenever I make a request, I'm going to send my fourth post ID. So the back end would know the user

### 00:07:33 · Speaker 1

has got the content till here. Let me load from that particular point. Okay? So here there is no chronological order. So whatever the cursor that we are sending, cursor can be computed in multiple different ways. Like for example, whatever the trending content, right? That particular cursor can be sent and the next trending content can be fetched. Like don't imagine like it is gonna be like this only. So cursor might sometimes point to the content which is previous as well. So back end basically has a complete control of sending the cursor. So and whatever the next cursor

### 00:08:03 · Speaker 1

it wants to point again it is controlled via the back end okay. So cursor based approach is extremely useful whenever we are using the social media sort of a content where the content is changing very frequently then cursor based approach is good. When the content is not changing very frequently the offset based approach is good. Okay. Now let's go to the third problem. That is handling live video commenting. This I've explained little bit about in my YouTube system design video as well. If you have not seen it again it's part of this playlist only. I'm trying to put the link somewhere on the screen and the description section. Please go ahead and check it. So but let's

### 00:08:33 · Speaker 1

discuss in detail. One of the uh feature of Facebook is live video and lot of celebrities use it. It's where they come on live and you know that fact that like whenever somebody's online and making a live video, there are times where within a second like hundreds or thousands of comments would flow into the system. Let's say you are open the Facebook mobile app and you are seeing a video, so many comments are coming, correct? How do client get those comments? Like there are multiple ways. Like for example, I to get a comment somehow I need

### 00:09:03 · Speaker 1

to make an API call to server to get the content, correct? What I can make? I can make an API call at a periodic interval. Okay, I've discussed those techniques here.

### 00:09:12 · Speaker 1

So periodic interval, so we call you can call it like a short polling and a long polling. What is short polling? Every specific duration of time I will poll the server, like for example every five seconds I make an API call to get some data from the server, okay? So whatever the comments by that time has come, I'm going to push it into the comment list so that that can be useful for the user. What is a long polling? Long polling is relatively for longer duration of time. Instead of like you make a call and if server is not giving anything you come back, you make a you make a call, you wait for some duration so that immediately that

### 00:09:42 · Speaker 1

did not be any comments but within few seconds some comments might flow so the polling duration is slightly longer. Third thing and very important thing is server sent events where the client is not asking client is not doing anything. Server only will send some events saying like I have some comments please make an API call that is the time where client would make an API call try to get some events from the server like comments from the server. Fourth point is sockets I've explained this very much in depth in my messaging end to end messaging system.

### 00:10:12 · Speaker 1

design. I'm going to put that also in the screen and the description section. Please go ahead and check that out to understand sockets in detail. But in a very nutshell, socket is nothing but an end-to-end connection. There are two devices where a dedicated connection is established between the two devices. Two devices here I mean, two systems. It could be client and server, client and client, etcetera. So where there is a dedicated connection. The last approach is the HTTP to server push. So this you guys might have seen on the news applications where, let's say you subscribe to the news, even when you've not opened that web application, you

### 00:10:42 · Speaker 1

will get a web push notification saying like there is a new something has happened can you click so there is a all the news updates you will be receiving like a push notification this you can correlate with a mobile apps push notification also okay now which technique to use the best technique that or the technique that even the Facebook using right now is server sentiments okay different application might be in different application but with my research most live commenting features in YouTube Facebook and every other platform mostly uses the sockets okay

### 00:11:12 · Speaker 1

where there is a dedicated connection established in the client end server so that every time whenever the command come into server that is pushed into the devices. any client that they are using. For example, there are ten different clients command user one sends a command, it goes to server and it broadcasts to everybody who has established a socket's connection with the server. It's going to give you the best performance compared to any other techniques mentioned here. So sockets are the best technique. Okay? Along in in all the technique that we have, sockets are nothing but the best technique that we can follow. Okay? Now

### 00:11:43 · Speaker 1

Let's move to another problem. That is resource optimization. See, resource optimization is one of the why it is the biggest problem is people have a tendency of like keep scrolling. You all know like how people do on Instagram, like one after another post, they they keep scrolling, correct? So user will not wait for a lot of time to get this good content. So they want to get the content very quickly. So what are all the different techniques that we can use to get a better experience for the user? One is have a resolution specific resources. What do I mean by resolution specific resources? Let's just

### 00:12:13 · Speaker 1

somebody uploads an image, okay, very high quality image from his web website, like from Facebook web application they've uploaded the image. But somebody's using the want to view that image from a very low end mobile phone. So what we should do on the back end side is whenever an image is uploaded or resources uploaded, we should process it and create like multiple variations of it. Like for a different resolution, for example, a higher resolution image is uploaded, we should have a variations of it with a lower resolutions.

### 00:12:43 · Speaker 1

Whenever a client requests particular resource, we should know like what is the performance of that particular device or what is the orientation of the device, what is the size of, what is the capacity of that particular device. Depending on that a resource has to be loaded so that there is a high chance where the resources will be loaded very quickly and people get a seeming less experience, okay. Second thing is CDN. I'm sure most of you might be aware of CDN, if not, CDN is actually a content delivery network. How CDN works I'm trying to explain at a very high level here, okay. So where

### 00:13:13 · Speaker 1

like getting the resources every time from a server, we could use a content delivery system where that particular content delivery network where those images or the resource are cached and you will getting it from the cached server. So as you can see here, the user request the content delivery network for the resource. If it has a resource, it will immediately respond. Okay, if it is not having that particular resource, it will request to the server. And even when server is not working, the content delivery network can still respond to the user with the help of already

### 00:13:43 · Speaker 1

cache resource. And whenever server responds, it's going to store it in its its cache and respond it back to the user, okay? This way the CDN systems are act like a very fast delivery of the resources. Definitely they have their own drawbacks as you all know. This becomes a bottleneck. Even if server is up and running, if content delivery network goes down, there is no resource that we would get. Every system has pros and cons, but lot of systems use the CDN for their resource handling. And the most people would not be aware of this, that is web P, okay? What is web P?

### 00:14:13 · Speaker 1

WebP is an image, uh, image format like we have JPG, PNG, uh, like that. There's a WebP is also image format which can like load the images very efficiently. If you can go ahead and see here, Google right now owns WebP. That WebP lost this image is 26% smaller compared to PNG equivalent and that lost image is like 25 to 30% smaller than JPG equivalent uh images, okay? So if you are watching the video and if you are somebody who's building a new website or you have already a web application

### 00:14:43 · Speaker 1

application. Please use web images going forward which is gonna load your website in lightning fast speed. So how to convert it into the how to convert a given image into web image Google itself has a software where you can upload your images convert into webpy and store it to your store it in your website. It's gonna give you like very quick loading time. The last thing is resources based connectivity. See we all have varying different connectivity correct. For example I am in three G I am in four G I am in five G from that point A to point B when I'm

### 00:15:13 · Speaker 1

traveling in my cab or auto or in my own car where my connectivity might be keep changing. So the resources also should be loaded based on the connectivity. This is slightly extension to the first point. Like where we would store the different images in the like whenever some person uploads some content, uh different resolution specific resource are stored, there has to also consider the connectivity. For example, if somebody requests from a laptop with three G internet connectivity, which version of the resource need to be loaded should be known to them.

### 00:15:43 · Speaker 1

that will only will give you the seemingless experience, okay? These are the things that I want to explain as a part of this particular video. We have primarily covered four problems: rendering large list, infinite scrolling and pagination, handling live video commenting, and resource optimization, okay? I'm sure most of you like the video. If you like the video, please like on YouTube. If you comment, if you if you if you have any doubts, please add a comment section, add it in the comment section. I'll be more than happy to answer. Or if you think your friends also might get benefited, please share it with them. If not already subscribed to my

### 00:16:13 · Speaker 1

channel, please subscribe to my channel. I'm going to get more such, I'm going to bring more such good content. And I read a lot of interview preparation frontend materials on my LinkedIn. So please follow me on LinkedIn as well. The link is in the description section. If you want me to make any specific video about system design, please mention that in the comment section. I'll be more than happy to make a video about it. Thank you so much for watching. Catch you in the next video.
