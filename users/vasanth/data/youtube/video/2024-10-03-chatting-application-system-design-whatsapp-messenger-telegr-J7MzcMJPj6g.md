---
id: J7MzcMJPj6g
title: Chatting application system design | WhatsApp | Messenger|Telegram. How end
  to end encryption works?
date: '2024-10-03'
url: https://www.youtube.com/watch?v=J7MzcMJPj6g
description: "#interview   #react #reactjs  #frontend  #javascript \n\nThere was issue\
  \ while recording the screen after 9 minutes : https://miro.com/welcomeonboard/c0oxbUQ4T1lsckZuUUdpaU52WDZTRHN1TTQ0YTR4QmhETDluMmxRenpaUkMzdGx0Y3pObzVkd3M3OXZ2M1JKMnwzNDU4NzY0NTk3MDkxMjk3NzE0fDI=?share_link_id=436163715207\n\
  Refer this image for better understanding. \n\nIn this Video I have explained how\
  \ to design an auto complete system on the frontend system. We have few major problems\
  \ in implementing autocomplete on any frontend system, ex:\n\n1. How to cache search\
  \ results locally ? \n2. If API call 1 is made and result is not returned and we\
  \ make API call 2. After this, the first API call 1's result is returned followed\
  \ by API call 2. How to show it on screen ?\n\nMany more such interesting problems\
  \ are solved in the video, watch till the end and support. \n\n @careerwithvasanth\
  \   is a Youtube channel dedicated to helping candidates clear their interview.\
  \ There are more than 150 videos and new videos will be uploaded every week. If\
  \ you're seriously preparing for interviews and looking for tips and tricks, please\
  \ subscribe to my channel and press the bell icon.\n\nYou can get more mock interviews\
  \ here : v=uW7MfzoD1po&list=PLmcRO0ZwQv4SwXLVpnKb_nFQx1Wd2XEjD&ab_channel=UncommonGeeks\n\
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
duration: 00:13:58
model: saaras:v3
transcript: true
---

# Chatting application system design | WhatsApp | Messenger|Telegram. How end to end encryption works?

## Transcript

### 00:00:00 · Speaker 1

It is as simple as this. We call this an heartbeat mechanism, okay? Where a client periodically sends a message to server to say whether it is online or not. Hello all, welcome back to Career with Vasanth YouTube channel. My name is Vasanth. I hope you all doing well. This is one of my favorite series where I'm going to explain lot of system design concepts. So in this particular video, I will be explaining the explaining the online messaging system design. So you might have already seen it across multiple different applications like WhatsApp, Messenger, Telegram. So

### 00:00:30 · Speaker 1

How do two different systems on front end implement the end-to-end messaging and what are the challenges involved in this? So I'm going to explain probably some challenges with the web, mobile, all of that. And if you're seeing me for the first time on the internet, my name is Vasanth. I already told I create content about front end and interview preparation. If you're not already subscribed to my channel, please subscribe to my channel. Without wasting further time, let's get started.

### 00:00:49 · Speaker 0

Yeah

### 00:00:50 · Speaker 1

So as you can see here are the top four problems that I'm explaining as part of this particular video. I don't want to spend a lot of time in documenting and designing the thing. So I have pre-drawn few things so that the session becomes much more quicker. So if you look at this particular thing, so four problems you are solving. One is end-to-end messaging. How to check a particular user is online or offline. How to send a media files, especially the images, videos, etc. How to perform end-to-end encryption. You might have heard a lot of people have might have heard about this end-to-end encryption, but I assume very few really know how end-to-end encryption works.

### 00:01:20 · Speaker 1

okay? Now, uh the assumptions are like here we are considering both mobile and web app for end to end messages. For example, you can send a message from Facebook mobile app to Facebook web somebody's online. So vice versa from mobile to mobile all of the things are assumed to be a one of our requirement, okay? Now let's start with a very simple thing that is end to end messaging, okay? So for example, we have the user one and user two and there is a server. So now whenever user one wants to send message to user two, there has to be some connection.

### 00:01:50 · Speaker 1

okay? Only this diagram already pre-drawn everything so that you guys can understand very quickly other things I have kept as suspense. So here you have user one who want to send message to user two. There are multiple different ways two particular users can get connected. One one way is where user one make a rest API call to server and again use server would whenever user two ask are there any updates again server can send that message where the two users are connected via rest rest architecture. So but the problem with that approach as you all know the

### 00:02:20 · Speaker 1

charting should happen very simultaneously like whenever user one sends a immediately message should go to the user two. So the best technique or best way to connect the two devices is always using the socket connection most applications including the application like Facebook, Facebook Messenger, Telegram, WhatsApp they all use the socket connection as a means of connectivity between the two users. Okay? So if you know what is the disadvantage of socket connection at this time only please mention that in the comment section. Okay? I might be explaining some part other part of the video but if you already know please mention that in the comment section.

### 00:02:50 · Speaker 1

connection. Now, the first problem I entered in my system is quite simple. So user one starts a connection, a socket connection with server, no server. Whenever user two comes online, they are also going to establish a socket connection with the server. And whenever user one wants to send message to user two, they'll use a socket connection. No matter how many people the user one sends a message, there's always a one socket connection that will be established. Okay? So next important problem is how to check a particular user is online or not. Okay? So this is one of the important question. I'm not going to show my solution very quickly,

### 00:03:20 · Speaker 1

I want you guys to think. See, one of the problem why it is a very challenging problem to say whether a particular user is online or not. Because for example, I've opened my mobile application and I've I've opened my mobile application, I probably I made a get request to get different messages or any updates. So that way server can say somebody's online because I made a recent request. But after that, I may not be making any change. I just kept my mobile open and I'm just scrolling and reading some other messages. So that in that probably I may not be making any

### 00:03:50 · Speaker 1

be a call because of which the backend may not know whether I'm online or not. Or there is also a chance where I've opened my mobile app and I put it in my background, then I open some other app. Technically I'm still online. I'm connected to internet, I've opened the app and I kept it in the background. So technically I'm still online. How does backend really get to know whether a particular user is online or not? This is a very, very important problem. The reason being, let's say you open LinkedIn or let's say you open WhatsApp.

### 00:04:13 · Speaker 1

You have to show whether a particular user is online or not, right? So very serious problem to solve. How to solve that problem? I'm going to explain. So it is as simple as this. We call this an heartbeat mechanism, okay? Where a client periodically sends a message to server to say whether it is online or not, okay? So for example, now here, first the client has sent one message, so server knows user one is online. After five seconds, it sent another message, so user server knows user one is again online. After some more seconds,

### 00:04:43 · Speaker 1

again the user one has five second again it has sent a message to server saying I'm online. After five second this the user one did not send a message to server saying that he is online. He or she is online because of the which now server knows the user one is offline. It could be because of multiple reasons where user one connectivity is low or user one decided to switch off turn off the internet. It could be any reason.

### 00:05:05 · Speaker 1

But at a periodic time the server is getting to know whether a particular user is online or not. Now the next question is what is the right mechanism that a client updates the server that it is online or not. What do you mean by mechanism here. Like for example will client make an API call every five second to update server it is online or not. Or it uses something that we've already used. Okay. The right mechanism would be using the sockets because there is already a connection between client and server. Why to establish another connection.

### 00:05:35 · Speaker 1

to tell whether a particular user is online or not, correct? So this is called a heartbeat mechanism where we would use the existing sockets to tell whether a particular user is online or not. Okay? This is a very serious and very important problem that how how a system solves. Now let's go to the third problem, that is how to send media files. Correct? Almost all of us are very familiar by sending our photos, PDFs, documents to the our friends using the chatting application, correct? So now we have user one here and a server here and probably there is a user

### 00:06:05 · Speaker 1

to which again comes and we will be sending the resources to the user too. The biggest problem is, in fact I ask you comment what is the biggest problem of socket. The biggest problem of socket is socket is designed for a lightweight data. Socket is not designed for to send a heavier data like for example images, videos etc. So socket should be used for sending the light data. So now but we have already have a socket connection established. So whenever sending the media files should we use a socket connection or not? If without

### 00:06:35 · Speaker 1

my explanation explaining further if you already know the answer please mention that in the comment section if not let's look at the answer okay

### 00:06:42 · Speaker 1

So where this is how it would work. So where whenever user one wants to upload a file or user wants to send some file to user two, we were not using the existing socket connection. The reason is simple. Socket is again lightweight, okay? So first what would happen is we make a REST API call, like typically whatever the get and post request that we make, we make that API call. We will save the data on the server, we could use some content delivery system, CDN or anything basically, but basically the data is stored on somewhere on the server and it will return a

### 00:07:12 · Speaker 1

source ID. For example, you uploaded one image, the back end would return an ID called hundred. So now the back end can uniquely identify an image using that particular ID. Now next using the socket connection, whatever the data or the text message that whatever you're passing, along with this will also pass this message ID. Whenever the user two receives this message ID, it will make a request to the server asking can you please send that particular resource to me and that would be sent to the user two. Okay? I hope you understood but I'm gonna quickly recap. So when

### 00:07:42 · Speaker 1

we have to send the media files. Do not use the socket connection because socket connection is meant to share a lighter version of the images, like lighter images, lighter data it is used and not for the resources like images, video, etcetera, okay? So do not use sockets for a heavy data. So instead of that, use your typical REST API calls to make the API calls to store data and whenever the server returns a resource ID, use that resource ID and interact with the server, like using the socket connection, okay?

### 00:08:12 · Speaker 1

always remember this how to handle the media whenever we are doing the chatting application. Okay? Now, last and one of the very important problem is how to perform end to end encryption. Okay? A lot of people might have heard what is end to end encryption.

### 00:08:28 · Speaker 1

See, end-to-end encryption means we have like user one and user two. Whenever user one sends message to user two, the expectation is nobody in middle should be able to decrypt it. Okay? So for example, even WhatsApp or Facebook servers should not be able to decrypt the message. That is what end-to-end encryption means. But so far, every time whenever encryption comes, there was always some keys involved and server had these keys. There is always a way server or somebody hacks the server or somewhere man in the middle attack was able to get these resources. So how

### 00:08:58 · Speaker 1

Facebook or Facebook Messenger, WhatsApp has implemented end-to-end encryption. I'm going to explain it to you now. Okay. So it's again one very very important problem, okay, which can be asked in the interview. So now let's go ahead and take a look at it again. So where there is a user one and user two, user one sends message to user two, user one responds back to user one. So this mechanism should be end-to-end encrypted, so nobody should be able to decrypt. How it is implemented is. So user one has two keys. Okay, it's called public key and private key. User two also

### 00:09:28 · Speaker 1

has private key and public key. So it's very simple everybody uh who who are in the platform will have two keys. Whatever the public key they have that will be registered on the server. So register the public key. User two will also register the public key. Okay every time whenever a new user comes to onboards into WhatsApp or Facebook two keys are created. Public key is again sent to the server and it is safely stored in the server. Private key is not sent to anywhere. Private key is just stored in user's local storage.

### 00:09:58 · Speaker 1

If you are using the your mobile app it could be stored in a like for in Android it can be stored in shared preference for iOS it can be stored in the key chain. If you are using the web it can be encrypted and stored somewhere in a very safe local storage. Okay? So but it is not sent to server by any means. Now

### 00:10:15 · Speaker 1

the user one and user two has registered their public key. Now let's say user one decides to send a message to the user two. Okay? So as you can see here first register private key server send like key registered successfully. Now whenever user one wants to send users to a message, user one will get the users to public key and encrypts the message. For example, I want to send like hi career with Vasant users. This message is encrypted whatever the encryption algorithm could be, the multiple algorithm, whatever the encryption algorithm could be. But this

### 00:10:45 · Speaker 1

user one would encrypt the message that they want to send using the public key of user two. So who can decrypt it? Only user two can decrypt it using their private key. Nobody else can decrypt this message. Okay, the reason being, it is encrypted using the user two's public key. It can be decrypted using only using the user two's private key. But the problem is, nobody else in the world has the user two's private key. Only user two has it. So because of that, as you can see here, encrypts a message using user two's public key and it will send it to server.

### 00:11:15 · Speaker 1

server sends this message to the user to scan server decrypt no server also cannot decrypt. And then it will decrypt the message using its private key. Again if you had if the user one had to respond. Again it will encrypt the message using user one's private key. User one's public key and it will send it to user one again user one decrypts the message using their private key. Okay. So again I'm going to explain just so that somebody might have missed it. So there is user one, server and user two. Whenever a new person onboards into platform both of them they will register their public

### 00:11:45 · Speaker 1

key onto server. Their private key is purely stored in their local storage. It could be mobile app, it could be web, their private key is extremely private. Nobody else in the world have access to the private key. It's not stored anywhere. So whenever user one wants to send a message to user two, the user two's public key is used and the message is encrypted. And whenever that message sent to the user two, the user two will basically decrypt the message using their private keys. So public key is something that is available on the server.

### 00:12:15 · Speaker 1

can be extracted by the different users who are using the private key stored only on the user's local storage. So encrypt using the public key, decrypt using the private key, okay? Now here comes one last segue where I'm going to stop sharing and I'm going to ask you this if you know the answer please mention in the comment section. Most of you might know there is something called WhatsApp business where from the single mobile number you could register your phone on the you could register on multiple devices. This can be useful in the business purpose. But

### 00:12:45 · Speaker 1

Whenever the single mobile number is used across the multiple devices, how to ensure the end-to-end encryption happens? Because whenever you use a single user, you had the public key and private key that is stored. Now you are logging on the another device also, but your private key is here. How to handle the private key there? That is a problem. If you know how to solve a multi-user experience with respect to end-to-end encryption, please mention that in the comment section. I have another small follow-up question again around this as well. Like for example, you are using your phone, Android phone or iOS phone,

### 00:13:15 · Speaker 1

the reason the WhatsApp was sending the end-to-end messages, it was working fine because your private key is stored safely. For some reason, you you lost your phone or you uninstalled your WhatsApp. Now, how to like get back this information? If you know the answers to that, mention that also in the comment section. If if none of you get to know or you want me to make another video explaining that, please mention that in the comment section. I'll be more than happy to make it. And that's all for this video. If you like the video, please like the video, comment whatever you felt honestly, and uh share with your friends so that they also get benefited because of this video. And

### 00:13:45 · Speaker 1

I'm bringing more and more such system design interview questions and answers. If you want me to make a video about any specific topic, please mention that in the comment section. LinkedIn also I write very actively about front end interview preparation. Please follow me on LinkedIn as well. Thank you so much for watching. Catch you in the next video.
