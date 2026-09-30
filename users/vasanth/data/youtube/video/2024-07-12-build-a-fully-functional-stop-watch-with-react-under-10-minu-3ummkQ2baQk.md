---
id: 3ummkQ2baQk
title: ⏱️ Build a Fully Functional Stop Watch with @React (Under 10 Minutes!)
date: '2024-07-12'
url: https://www.youtube.com/watch?v=3ummkQ2baQk
description: "In this video I'm discussing a most common machine coding question that\
  \ was asked by many famous product based companies. In this video we will build\
  \ a stop watch where the timer reduces from a given number to 0.  \n#coding #interview\
  \ #react #reactjs  #frontend  #javascript \n\nLink to solution: https://github.com/coolvasanth/reactjs_interview_preparation/tree/main/src/MachineCoding/CountDownTimer\n\
  \nLink to other company interviews : https://www.youtube.com/playlist?list=PLmcRO0ZwQv4R5Q6yAZyqFad9UIA-pr0Db\n\
  \n @careerwithvasanth   is a Youtube channel dedicated to helping candidates clear\
  \ their interview. There are more than 150 videos and new videos will be uploaded\
  \ every week. If you're seriously preparing for interviews and looking for tips\
  \ and tricks, please subscribe to my channel and press the bell icon.\n\nYou can\
  \ get mock interviews here : v=uW7MfzoD1po&list=PLmcRO0ZwQv4SwXLVpnKb_nFQx1Wd2XEjD&ab_channel=UncommonGeeks\n\
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
duration: 00:10:00
model: saaras:v3
transcript: true
---

# ⏱️ Build a Fully Functional Stop Watch with @React (Under 10 Minutes!)

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Career with Vasanth YouTube channel. My name is Vasanth. I hope you all doing well. So this is a video where we are going to discuss another machine coding question. As you know last video we had discussed about the traffic light. So this is another important question. I've asked this question in almost all of my mock interviews and even different companies interviews that I've taken in the past. This is looks very simple but difficult to achieve unless you know the concepts of DX very much in depth. Okay? So what is that we are going to build? This is what we are going to build. Okay? So as you see there is a timer that is just reducing and let's say if I click on pause, what

### 00:00:30 · Speaker 1

whatever the count that was shown that there itself we are pausing. Whenever I click on resume again it would start decrementing. Finally it reaches the value of zero and below zero it it cannot be reduced further. So again I'm explaining the question. So given a count you keep decrementing the count to a value which is greater than or equal to zero. So once we reach the zero we are not going to decrement it any further. Okay? That's what we are going to implement. This is more like you could consider like whatever stop that is used in athletics and other things right the same thing.

### 00:01:00 · Speaker 1

we are going to try to do here. Okay? I have started with the basic, I have actually coded it one to two times. I might make some mistakes but uh let's see. I'm going to just code like any one of you how you do this in the interview. Okay? So now I've removed everything, I have nothing. So in app.js I've imported countdown timer and that is the component that going to that is rendering now. Okay? So now let me tell you clearly, whenever such question asked to you in the interview, one of the important thing that you need to do is whenever you are dealing with a timer, make sure you understand

### 00:01:30 · Speaker 1

understand like what is the interval with which you need to increase decrease etcetera the time. Okay. And always remember the property of closure. Whenever you're using a set timeout or set interval inside the use effect and whatever the state variable that you pass to set interval or set timeout only that value will be known. For example you have a set timeout and you set some value inside that like the delay of some state variable and only that value will be known unless if use effect is not rerendering. Set timeout or set interval will not get to know the updated value. For example

### 00:02:00 · Speaker 1

passed a count as the delay which whose for example that count pointing like one second. Later you did lot of operations and the count became like hundred that's still not going to be reflected in the set tome because it's forming a property of closure. Whatever it was new whenever it got created only that is known to it. Okay. Now without wasting further time let's get started with that keeping that property in the mind. So I'm passing that initial count as a prop to this. Okay.

### 00:02:23 · Speaker 1

So const, so what I'm gonna do is the current count, okay? The current count, so set current count. So I'm initializing that with, I'm initializing that with the initial count, okay? This is my count, current count is this, okay? So next would be, uh I need to actually create one use effect. Why I need to create a use effect? Because at a periodic interval, at a particular delay, I want to trigger the set interval, correct? So until

### 00:02:53 · Speaker 1

complete my coding maybe I'll hide this so that you can see it in much better way maybe I would increase little bit of my font size also. Okay?

### 00:03:02 · Speaker 1

So now inside this I will create like set interval. Okay?

### 00:03:10 · Speaker 1

I'm going to create a set in tool. What is the delay here? It is like one second because every one second we are decrementing so it is static. Okay? And then what we are going to do here is we have to set the current count. Correct? What is the current count? Previous count, whatever the previous count was there, previous count minus one. Correct? So whenever the previous count value whatever it was from that we are minusing. Okay? Now we need to keep track of one thing where current count cannot reach zero. Correct? So if current count greater than zero only

### 00:03:40 · Speaker 1

perform this operation, correct? Otherwise we should not do because that is my requirement. If you can go to negative numbers also then you can you don't have to keep this check, okay? And then. So now what is the next thing that we need to do? So let us build the basic UI, okay? So I would have a H one tag where I'm gonna render the current count, okay? Let me create two buttons. One for pause, another one for the resume. See I'm not giving too much importance for the UI here. or the CSS property I'm primarily focusing about the logic building, okay? Let me create two functions, on pause

### 00:04:20 · Speaker 1

on pause and on resume. Okay? See, in interview also, whatever you are seeing right now, I'm going to do it in the same way. Okay? Only difference is here I know solution because I practice it once, but the approach is going to be pretty much remain the same. So that now all the building blocks that is required to solve this problem is done now. I have the on pause, on resume, and I also created the basic UI. Correct? Now, maybe if you wish to see, we can see on the UI. So where, as you know, it is going minus and all it's going because we have not completed the implementation, but pause and resume.

### 00:04:50 · Speaker 1

and this number we are able to see. Correct? Now. So now what next I'm gonna do is whenever on pause happened, I need to keep a state variable to check whether the particular timer, whatever that we are decrementing, that is gonna be paused or not. Correct? So I'm creating a variable.

### 00:05:06 · Speaker 1

is paused, okay? is paused with a default value of false because by default it is not paused, correct? So then whenever it is paused, I'm gonna set it like is paused is equal to true. And whenever I'm on resume, is paused is set as false, correct? So this much I have done and definitely I need to whenever that is paused is changed, that time also I need to rerender this. And definitely as you also know, whenever it is paused, I would have to like decrement the

### 00:05:36 · Speaker 1

correct? Only when it is not paused, I need to be decrementing the count. So that check also we kept. Now, the most important point here is, every time whenever you pause, right?

### 00:05:46 · Speaker 1

By that after that point in times still you need to have a reference to the current count. Correct? Otherwise what would happen is if you create a state variable after rerendering we might lose the previous count value. For that we need to use the use ref. Okay? So I'm using a const timer where I am using the use ref. I'm initializing that with null. So what is the difference between use ref and use state? Use ref even after rerendering it will still hold the previous value. It's not going to lose the reference to the previous value. Use state might lose because of which we are using the use ref here.

### 00:06:16 · Speaker 1

What we are doing time a dot current is equal to I'm initializing it to this. Okay. So that what I can do is whenever first of all the component is uh component is unmounted definitely I'm gonna clear this. Correct? Clear interval I'm gonna clear this. Correct? There is another place where I'm clearing it. That is

### 00:06:40 · Speaker 1

That is whenever actually we are paused, correct? Whenever we are pausing, that time whatever the previous set interval was there, that I'm going to stopping, okay? But the value that's only I've kept the value of the set interval into the timer dot current as a reference. So I'm clearing that. But whatever the count was there, that count value is going to be still retained and we are going to continue whenever user passes on on pause and on resume, okay? So now I'm going to click like on click.

### 00:07:08 · Speaker 1

on click is on pause and on click is on resume. Okay. Again this code will be also available on my github repository so you don't have to worry like about the code and you don't have to note down anything. Just before I render, in case you are watching me first time on the internet, my name is Vasanth like I already told, I'm a content creator. I help people to clear their interview. I make a lot of good content about front end interview preparation, career coaching, etc. So if you're not already subscribed to my channel, please subscribe, like the video, comment whatever you felt honestly so far, okay. Because this helps me to get more reach. Now, let me go and show you what is shown on the screen, okay?

### 00:07:43 · Speaker 1

Let me refresh it

### 00:07:45 · Speaker 1

We have ten, nine, eight, seven, let it first go till zero, then I'm gonna check again, pause and resume, okay? Two, one, zero, okay? We are not going any further, which is wonderful. So now let us see ten, nine, I'm pausing. Yeah, as you see the count has been paused and I would, I'm again resuming.

### 00:08:04 · Speaker 1

See again it is reducing again I'm pausing it has been seven okay now let's look at the solution completely from end to end once again okay so from app.js I'm calling the countdown timer I'm passing the initial count as ten here okay and that initial count I'm making as a current count value so never mutate the state directly so you got the state initial count don't change that variable directly use state variable or local variable so I've assigned it to a local variable then I'm using is pause and set is pause a state variable so where which is used to like check whether the

### 00:08:34 · Speaker 1

state is whether the counter need to be paused or resumed. Okay. So then I have a use effect. Inside use effect I'm passing the two state variable. So whenever the current count changes, I need to trigger this. Whenever the is paused is changed, then also I need to trigger inside the use effect. Okay, two different states. The reason I've already told in the video. Then I've created two functions, your on pause and on resume. So on pause basically I'm setting the pause as true, on resume I'm setting it as a false. On pause whenever I'm pausing, I'm also clearing the previous interval because whenever you resume it's a

### 00:09:04 · Speaker 1

interval that is getting started. Okay, because for that only, I'm using the property of userf and userf and I'm assigning it to the timer variable and I'm using it. Okay, the complete code will be available on my GitHub repository. I'm sure you understood it. But there's different ways to solve this problem without using the userf also. If you know that approach, please mention that in the comment section. I'm going to review your code and let you know whether whatever you've coded is correct or not. Okay. Thank you so much for watching. If like I already told, if you're watching me first time on the internet and not subscribed to my channel, please subscribe. I'm going to bring more such good content on my channel. You subscribe

### 00:09:34 · Speaker 1

will help me to bring more such good content. It's not about this machine coding. I have eighteen plus mock interviews on my channel, thirty five plus videos about basics of JavaScript, a lot of videos about React JS interview preparation and there are a lot of videos about DSA. There are a lot of seminars, webinars we have created and those videos are captured there. Basics of DSA videos are there. There's so much good content about front end and interview preparation. Subscribe to my channel, watch all the series, link to all the series will be in the description section also. Thank you so much for watching, catch you in the next video.
