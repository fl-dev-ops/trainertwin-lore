---
id: 7JWyokIs3KU
title: Auto complete frontend system design | Step by step break down of problems
  & Solutions
date: '2024-09-11'
url: https://www.youtube.com/watch?v=7JWyokIs3KU
description: "#interview   #react #reactjs  #frontend  #javascript \n\nIn this Video\
  \ I have explained how to design an auto complete system on the frontend system.\
  \ We have few major problems in implementing autocomplete on any frontend system,\
  \ ex:\n\n1. How to cache search results locally ? \n2. If API call 1 is made and\
  \ result is not returned and we make API call 2. After this, the first API call\
  \ 1's result is returned followed by API call 2. How to show it on screen ?\n\n\
  Many more such interesting problems are solved in the video, watch till the end\
  \ and support. \n\n @careerwithvasanth   is a Youtube channel dedicated to helping\
  \ candidates clear their interview. There are more than 150 videos and new videos\
  \ will be uploaded every week. If you're seriously preparing for interviews and\
  \ looking for tips and tricks, please subscribe to my channel and press the bell\
  \ icon.\n\nYou can get more mock interviews here : v=uW7MfzoD1po&list=PLmcRO0ZwQv4SwXLVpnKb_nFQx1Wd2XEjD&ab_channel=UncommonGeeks\n\
  \nTo get a dedicated one on one,  you can reach out to me here: https://topmate.io/vasanth_bhat\n\
  \nJoin CareerwithVasanth community to discuss with other developers: t.me/uncommongeek.\
  \ \n\nFollow me on LinkedIn - https://www.linkedin.com/in/careerwithvasanth/\n\n\
  Medium Blog https://mevasanth.medium.com/  \n\n\U0001F449 “Contact on WhatsApp:\
  \ 9731039408”\n\nJavaScript Interview preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nJavaScript Custom implementation/polyfills Series: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\n\
  \nFrontend system design series: https://www.youtube.com/watch?v=gN8LQTff21g&list=PLmcRO0ZwQv4RYUD10hUnWjWb-RRSpm3KM&ab_channel=UncommonGeeks\n\
  \nMAANG series for frontend developer: https://www.youtube.com/watch?v=s-b-txm_Gvk&list=PLmcRO0ZwQv4SNhbW4CI4vc-6IHBHCKzZN&ab_channel=UncommonGeeks\n\
  \nShorts for quick access to all frontend resources: https://www.youtube.com/watch?v=8ByBOT7Aehs&list=PLmcRO0ZwQv4SXtrTYIU_dPygZgOgYV81S&ab_channel=UncommonGeeks\n\
  \nTips for freshers: https://www.youtube.com/watch?v=hGIOIdPNNqE&list=PLmcRO0ZwQv4QBiZns-nYX5qnHKAepVeqH&ab_channel=UncommonGeeks"
author: careerwithvasanth
duration: 00:18:51
model: saaras:v3
transcript: true
---

# Auto complete frontend system design | Step by step break down of problems & Solutions

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Career with Vasanth's YouTube channel. My name is Vasanth. I hope you all doing well. So as you know this is a video series where we are discussing about system design. It's quite some time that I hadn't made a video about system design. In this particular video I'm going to discuss about the autocomplete system design where as you all know autocomplete is nothing but whenever you go to a particular site, you search something, whatever the suggestion that come whenever you start typing, that is nothing but the autocomplete. There's so many intricate problems with this particular architecture. I'm going to discuss all of them step by step in this particular video. So

### 00:00:30 · Speaker 1

Let's start without wasting further time and if you're somebody who's watching me first time on the internet, please subscribe to my channel career with Vasanth. I'll be making content about front end interview preparation. Lot of good content is in my channel so subscribing you will not hurt anything. Okay? Now, so what is auto suggestion? This is auto suggestion. Okay, let's say I search now career and you see like lot of the suggestions coming here, right? All of these are coming because Google is able to predict after you search certain characters what are all the possible options that you can discuss further.

### 00:01:00 · Speaker 1

That's the intent of this particular auto suggestion. Okay. Now, let's go through it one by one. Okay, what is that uh how to solve this particular problem. Unlike my other problems just to keep the video short, I'm not basically discussing about the functional requirement, non-functional requirement, etcetera. Let's stick to the core functional requirements of auto complete as a problem and how to solve it. Okay. Now, a lot of these things I've drawn already just half an hour before this recording the video to make again the video a little shorter. Okay. Now if you see

### 00:01:30 · Speaker 1

let's say user types something like carrier. What are all the options that you are seeing below? This is nothing but the auto suggestions that are coming from the back end obviously. Now, let's say we have to solve this problem. What we as a client or front end developer would do? The first thing that most people would think is this, okay? Where we have a client and a server, correct? Now whenever user types something, the client makes an API call. Server checks are there any relevant results that matching that particular response and they send back to the client, okay?

### 00:02:00 · Speaker 1

For example, if you look at this thing, let's say you typed C A carrier or just C A. Whatever the things that matches that particular, uh, whatever the the type things that you typed, all of that will be returned. For example, let's say I type C A. As soon as I sub C A, a network call is made and all these possible options are returned from the back end and that is shown on the UI. As simple as that, it is done. Okay? But if it is so easy, then probably we would not be making a video about it, correct? There are certain some more problems associated with that. What is

### 00:02:30 · Speaker 1

that. Like for example for every keystroke if you make an API call for example I typed C. If I'm seeing all this then I made an API call. I'm making another API call. I'm making another API call. Let's say I did this okay. For every keystroke if I start making API call then I would end up making so many API calls. And lot of the words that I would type still might have not become a proper something known like for example C A C A is not responding to anything probably I would type another character then it respond to something.

### 00:03:00 · Speaker 1

response to something, correct? So where I'm coming from is probably it should become some sense, then we should start making API call. So one is like, let's say I after I entered minimum three characters, depends on the product requirement, but I'm just saying in general. After somebody enters three character, we'll start making API call, point number one. Point number two is what most people would think. Even after you after three characters you start making a API call. Even after that, let's say for every character if you keep making an API call, then you end up making so many calls.

### 00:03:30 · Speaker 1

Correct? Instead, we could limit the number of calls using the very popular technique of debouncing. Correct? What is the problem with this approach? Calls are made very frequently. Correct? Calls are happening very frequently. So you could avoid this problem with help of debouncing. What does the debouncing approach tool do here is, we have a client, we have a server, make API call after a configurable duration of time. What do I mean by configurable duration of time? The typical debouncing in most websites is around two fifty milliseconds, which

### 00:04:00 · Speaker 1

is one fourth of a second. Every one fourth of a second you make an API call. That's what the most applications would do. Okay? But again we cannot be so strict about that one fourth of a second or two fifty millisecond because for some product requirement they want to reduce it to hundred millisecond. So that number should be configurable. Either you get it from your back end or you get it from your sites like Firebase anywhere you get it. But that number should be configurable and you should be able to change that. Okay? So now once after that number is configurable now for every keystroke after

### 00:04:30 · Speaker 1

three character. Every keystroke you are not making an API call. You are making an API call after two fifty millisecond. So doesn't matter you type two characters, doesn't matter you type ten characters. If you if you are like super fast in typing, doesn't matter how many ever characters you are able to type, after that we make an API call. Okay? So again I'm reiterating, approach one where the client makes an API call to server, server responds back. No optimization here.

### 00:04:54 · Speaker 1

But here, the client is making an API call only after a pre-defined duration of time. For example, after every three second you're gonna make an API call, sorry, every after every two fifty millisecond you make an API call, doesn't matter whatever the characters typed so far and you return the results. This is about approach two with the help of the debouncing. But if you observe here, there is still the fundamental problem exist. The fundamental problem is

### 00:05:21 · Speaker 1

For the same character that we're typing, for example, I come here, I typed C A, I typed C A R, C A R D, and I again removed D and R. So API call was earlier made for C A, and now after I enter R D and I removed D and R, again the same API call is made for C A. In a fraction of probably a second, highly unlikely the data on the back end might have changed. Like for example, if I made the call with C A at ten A M, and then ten A M once

### 00:05:51 · Speaker 1

second. Definitely the data would not change in most of the system including systems like Google also. Correct? So unnecessarily I make an API call for the data that probably already we could have stored on locally. Correct? So the problem is approach two is calls are made very frequently for the same string. Okay repetitively maybe I can remove. Same call for the same string is been made multiple times. So what is how do we solve this problem? The common suggestion to solve this problem is using the cache.

### 00:06:21 · Speaker 1

Correct? So that is our next approach. That is the approach three. Okay? In the approach three, between the client and the server, okay? Between the client and the server, we have a cache. Okay? What is a cache here? Whenever user types a particular string, that particular request comes to this local cache, checks whether the data is present on the cache. If it is present, then we will get the result immediately. Okay? If that for that particular string that is not there on the

### 00:06:51 · Speaker 1

on the local cache. Then it will make an API call to server and then it will return the result. Okay? I've intentionally missed one thing here in this process. Okay? If you know before I even even before I explain that, please mention that in the comment section. If not, I will explain it now.

### 00:07:08 · Speaker 1

Let's say first you made an API call, let's say you type something, you check whether that exists in the cache. If it exists in the cache, you're going to return it. If not, you're going to make an API call to server and if whenever the server sends the result, you should store that in the cache and then you should return it to the client or putting otherwise both are on the client only, you should store that in the cache and then you should use it or storing on the cache and using can happen in parallel as per your product requirement. Okay? So if I have to draw that, Right Let's say whenever the result comes here, correct?

### 00:07:55 · Speaker 1

Now if you observe carefully here what I have done, I made an API call to server. First I made an after as soon as you type something, I checked whether that exists in cache or not. If it not exist, I made an API call to server, got the data and I saved it on cache and then I passed it to the client. Putting otherwise these two actually are on the client only, but for the program to process the result, I passed after I make sure the value stored on the cache. But if your product requirement is not so stringent, you could actually do the both in parallel. Like for example, you initiate a request to save the value on the cache and you can

### 00:08:25 · Speaker 1

also meanwhile uh use that value as well. So both happens in parallel. Next time whenever you make a call, the assumption is the value is already stored in the cache and that particular thing can be returned. Okay? This is the approach three. Okay? So again I'll reiterate quickly the approach one, approach two, approach three. Approach one just make an API call, get the data. Approach two use debouncing so that some amount of delay is saved actually. Okay? Some amount of the unwanted API calls are saved. Approach three is where we are caching the results. Now, caching also

### 00:08:55 · Speaker 1

another thing, how do we cache? Like we do we store it in array? No. We actually use a map here. Like JavaScript map, I'm sure most of you are aware, ES6 has introduced a concept of mapping in JavaScript where we could store key and value pairs. So here if you observe the key is whatever the user has typed, value is whatever returned from the server. So the advantage of using map is the the the complexity with which we'll be able to find the value from map is big O of one. But for array it is big O of n. So next time whenever user searches CA, could just like like uh let's say this is a map like const

### 00:09:31 · Speaker 1

search cash. Okay?

### 00:09:35 · Speaker 1

All I have to do is searchcast.get

### 00:09:41 · Speaker 1

of the key. Okay. Whatever the key, for example, C A, I would immediately get completely this result. Okay. So this is the advantage where we are able to get the complete result of the map in just big O of one and then we can use the same for the processing. Okay. Now, again the question comes in like what's what is the right cache to use? Like the multiple caches, right? Like we have the as efficient as a local databases or as preliminary as that of a local storage, correct? Again depends on

### 00:10:11 · Speaker 1

requirement. If you are somebody like Google where none of your results are going to be saved after a particular session, then you could just use even the simplest Redux where for only for that particular session you are going to store. Whenever user leaves the tab or user closes it, it is gone. We are not going to store anywhere. For some reason, you have the search box in only one of your page. You even don't have to use Redux. Just use a local state variable where you store the values. Once user leaves the page, the entire thing is gone. But if you are an application where, which is targeted to some B to B sort of an application,

### 00:10:41 · Speaker 1

where user do not have like lot of things to search. They keep searching like common items repeatedly. Then you could use some efficient techniques to store this. Like you could use a database like SQLite or Watermill and DB where you store the data results very persistently. Next time whenever you user opens it, they can use that particular cache. But there is a disadvantage with the second approach. Like one cache is where it is a temporary cache. So it's very easy, you leave the page, you clear it. For the permanent cache, then whenever next time user

### 00:11:11 · Speaker 1

the thing and searches CA. Let's say user opens it after a month. There is a chance where lot of data might have updated by then. So user should not be looking at the old data whenever actually the new data is present on the server. For that cash invalidation or cash expiry also you need to take care. When to expire the cash it can be configurable or it can be fixed number like after every twenty four hours you are gonna invalidate. This is broadly depends on the product requirement how often the data would update that often you can clear the complete cash. Okay?

### 00:11:41 · Speaker 1

whenever it is a just run in the memory sort of like in the Google set sort of thing then you don't even have to worry about clearing the cache as you store it in Redux when you they close it is removed or you store in a state variable when they remove the page it is gone. Okay? whenever you have to store it persistently come up with a expiry logic. Now.

### 00:12:00 · Speaker 1

With this also there is a very interesting problem

### 00:12:03 · Speaker 1

See, you made a call with a string one and its result hasn't come yet. You made another API call. Like if you go back here, you made one API call, it's not present on cache, so you made a call to server. And server hasn't returned yet. You made another call. Let's look at the diagram here. I've just removed the cache block here, assume the cache block is present. User search string is there, present and you return. Okay, whenever it is not there, you made a request one, request one returned

### 00:12:33 · Speaker 1

data hasn't returned yet. And you made another request called request two. Now, let's say on screen, for example, you typed CA, you made a network call, the data hasn't come yet. By then you typed another CARD, another API call was made. And now, if you observe here, request one, request two, first the response of the request one will come. So in our example, the response to the CA will come, followed by CARD. But on the search

### 00:13:03 · Speaker 1

on the input box we have C A R D. We cannot show C A's result for C A R D. I'll reiterate if somebody got confused. Let's say I typed C A here, I made an A P A call for the back end to get the results. Then I typed C A R D, another A P A call was made. Even before the first A P A call return result was returned. Okay? Now the problem is I'm expecting results of C A R D. But I have the results of C A. If I end up showing that, then I'm gonna be in trouble because user is

### 00:13:33 · Speaker 1

not expecting that. That is a problem. So how do we solve this problem? Okay? One common way that most people suggest is, let's say there is one call that is already in progress and we are trying to make another call about the first call. Like, we let's say every time you make sure only one call is active. So you made call one, call two, and by before you make the call two, about the call one. There are multiple ways to about the call. You can go ahead and read about it. So where the complete call is cancelled. So now only the request whose response will be used

### 00:14:05 · Speaker 1

But think through, think it, think it loud. There is a problem with this because see, what do you mean by abort? Client has sent a request already. It has already read the server. Server might be already processing and it might have already sent the response somewhere it is in middle. So we are not saving much in some times by cancelling the request. Instead what is the optimal way? Okay, if you know the answers to this, please mention that in the comment section even before I explain. Okay? For some simplicity or more better understanding I've written this. So request one is

### 00:14:35 · Speaker 1

at ten zero one p.m. request two is made at ten zero two a.m. So both are made at a.m. ten zero one a.m. ten zero two a.m. Now we will get a response. Correct? Now we will be getting a response.

### 00:14:47 · Speaker 1

of request one

### 00:14:51 · Speaker 1

response of request one

### 00:14:54 · Speaker 1

ten three. I know most practical APS will not have this much delay but I'm just saying. followed by the request two. Correct? So same thing whatever I explained so far. So the one way is aborting, aborting is not an option. When you cannot abort, the better way according to me is, see, we are already using the concept of caching here.

### 00:15:14 · Speaker 1

Whenever I typed something and when the response comes, instead of just aborting it, why can't I store the value in the cache? Whenever the old APIs response come, I'll use it in the cache. And whenever the latest strings response comes, I will again keep it in the cache and I'll also use it to show on the UI. But the problem is, there's a request one and request two. How do we determine which request to process? Like the response for which request to use and which request to ignore, correct? The best way the multiple

### 00:15:44 · Speaker 1

place to this. But the one of the most suggested way is ten zero one a.m. you made an a.p.i. call. Pass the client time stamp to a.p.i.

### 00:15:54 · Speaker 1

So request one has made a ten zero one. Whatever the time stamp of that, you send it to server. And whenever you made the request to send that to server, okay? Maintain a local time stamp. Okay? A const local

### 00:16:10 · Speaker 1

timestamp. Okay? And you maintain whatever the timestamp like actually you get the complete date object for simplicity I'm just writing. Ten zero one ten zero zero zero one. Okay? So now let it make it let.

### 00:16:26 · Speaker 1

we so according to our local timestamp right now it was this. and whenever the next call was made the local timestamp variable got updated to zero two. correct? and when the response comes. so if the response timestamp is also same as the whatever the timestamp we have processed.

### 00:16:44 · Speaker 1

If it is not, put it in the cache and ignore or wait. So when the request one was made, local timestamp was ten zero one. Request two was made, the response was ten zero two. Now request one's response came, whatever the client timestamp that we sent to the server, server is also sent just return that timestamp to back to us, okay? So in that case the ten zero two, whatever the server would send back the ten zero one to us, correct? So in that case it will a mismatch, just show it in the cache. Whenever we get the timestamp as ten zero two, use it.

### 00:17:14 · Speaker 1

Okay. Again this problem can be further extended, correct? What if we don't get a response to a particular thing? So then in in that case also, let's say you made two APA call, request one and request two. Request one's response came, but request two's response did not come. Just because request two's response did not come, we cannot use request one's response. Correct? Then you should have a proper way of handling the errors. Okay, now I'm gonna quickly summarize as I'm hitting twenty minutes, I'll quickly summarize. So far if you like the content, please like the video and

### 00:17:44 · Speaker 1

whatever you felt honestly and if you're really liking it please share it with your friends as well. So I'm gonna like go through all of it at once. Approach one make an API call get the results one of the worst approach. Use debouncing comparatively better. Debouncing plus caching much better. Debouncing plus caching and whenever there's a request that has taken more time to respond just store the response in the in the cache instead of like aborting the request. Okay all these four is

### 00:18:14 · Speaker 1

I've been one of the the approaches that you can follow. And one important thing that I want to say. There is one problem with the approach that I'm mentioning where you're passing the client time stamp to server and the server is returning the same thing back to us. Instead of this, do you feel there is a better approach? There is better approach actually. If if you know that, please mention that in the comment section. Okay? That's all I wanted to explain this particular video. If you like the video, please like the video, comment whatever you felt honestly, share the video with your friends if you if you like like if you think they they can be

### 00:18:44 · Speaker 1

get make use of it. And thank you so much for watching. Subscribe to my channel Career with Vasanth. Thank you so much. Catch you in the next video.
