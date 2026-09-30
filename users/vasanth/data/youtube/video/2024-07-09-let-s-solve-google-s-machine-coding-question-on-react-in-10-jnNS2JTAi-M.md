---
id: jnNS2JTAi-M
title: Let's solve @Google 's machine coding question on @REACT in 10 mins | Most
  important interv question
date: '2024-07-09'
url: https://www.youtube.com/watch?v=jnNS2JTAi-M
description: "#coding #coding #interview #react #reactjs  #frontend  #javascript \n\
  \nIn this video I'm discussing a machine coding question that was recently asked\
  \  on  @Google  In this video we will build the traffic light where the light switches\
  \ from red to yellow to green and this rotation happens indefinitely. \n\nLink to\
  \ solution: https://github.com/coolvasanth/reactjs_interview_preparation/tree/main/src/MachineCoding/TrafficLight\n\
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
duration: 00:09:53
model: saaras:v3
transcript: true
---

# Let's solve @Google 's machine coding question on @REACT in 10 mins | Most important interv question

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Career with Vasanth YouTube channel. My name is Vasanth. I hope you all doing well. So this is a video where we are discussing a Google machine coding interview question. One of my follower recently attended Google interview and this was a question asked. This question looks very simple for me in the beginning but it has lot of intricacies. So I'm thought of explaining it to you how to solve it in less than ten to twelve minutes, okay? So without wasting further time let's get started. So as you whatever you are seeing on the screen, this is something that we have to build at the end. So that is a traffic light where red is shown for a specific duration of time, followed by the yellow, again short for a specific duration of time. Then

### 00:00:30 · Speaker 1

are showing the green light for a specific duration of time and this loop continues for the infinite times. Okay, this is what we'll be building. Let's get started how to build step by step. Okay? So I've already written the code for this. Now I'll remove everything and we'll start from the scratch. Okay? Yeah, so now we have nothing, just we have an empty component called traffic light. From there we are going to start everything from the beginning. Okay? I'm going to show you the question so that you can understand the exact what is required. So build a traffic light where the light switch from green to yellow, yellow to red after a predetermined interval and a loop indefinite.

### 00:01:00 · Speaker 1

directly. Okay. Each lid should be lit for the following duration. So red lid for four hundred millisecond or red lid for four second, yellow lid for five second, green lid for three second. Okay. You are free to exercise your creativity to style the appropriate appearance of the traffic light. So basically however I want to style, I can style. Only thing that I've already done is the styling part. So I've created like one traffic light that's a container that contains the entire light, the black background whatever you're seeing, right? That is the traffic light class. And I have also have a each light class which is basically responsible for showing that the circle, the

### 00:01:30 · Speaker 1

yellow, red and green circle, whatever you're saying, right? That and a very specific style for the red, green and yellow where we are specifying the background color, okay? Background color for red is red, yellow is yellow and green is green, okay? As simple as that. Just to save some time, I have done that already. Now, let me tell you one thing. Let's say such question asked to you in the interview, what is the first thing that you would do? First, make sure you ask as many number of questions as possible to the interviewer to just to make sure conceptually are clear. For example, in this case, we are we are saying like indefinitely keep changing the lights, but but if you keep changing

### 00:02:00 · Speaker 1

indefinitely then there's a chances of memory leak. You can ask like what is the maximum duration of the time that I need to show or maximum iteration that I need to show. Okay. In this particular exercise I'm not doing that but any other doubts that comes to your mind please make sure that you ask and clarify before you start coding. Okay. So now there are many approaches I have asked this to lot of in my lot of my mock interview what people do is so we have red shown for some some time followed by yellow followed by green so they create like one set timeout for four second. Inside that they create another timeout inside that they create another timeout. One timeout

### 00:02:30 · Speaker 1

said one another with specific delay. And they try to do this but that is not the way to do it. Whenever now in this question whenever you see such kind of specific specifications respect to like light here or anything like a specific module need to be rendered for specific duration of time. Always go and use the object approach. Okay? So I'll let me show you how we need to start. So let's create an object called like let light config. Okay? It need not to be let actually. We can make it like a const I'll make it.

### 00:03:00 · Speaker 1

Okay, we have like const light object, light config where we have three three configs, correct? So where red we have, what is next of red is yellow, okay? After that we also need to show the duration. So duration for this red is actually four hundred four thousand, correct?

### 00:03:18 · Speaker 1

I've actually as you saw I've solved the problem one to two times but I might end up making some mistake if I make a mistake I will correct it on live so that you can also you like you get to know like what mistakes can be made and how to avoid that. Okay. So

### 00:03:34 · Speaker 1

So next to red is yellow. So next to yellow is green actually, correct? Next to green is red. So how we have done is first we are gonna show red. What is next of red is yellow. What is next of yellow that is green, correct? So that's what we are trying to achieve in this particular configuration. Definitely we specified the duration, how much duration we need to show, correct? Now let's have a use effect. Why we need a use effect? Because we have to keep running a set timeout for a predetermined duration of time and when we should run this use effect, I'm gonna tell, okay?

### 00:04:04 · Speaker 1

launched, let's have a light and a set light. Used it, okay? Actually the question says like start by green. uh so any any color like you can start by green but I'm just following like a typical traffic light so that you can understand clearly. First default color I'm taking it as a red, okay? Default color.

### 00:04:24 · Speaker 1

Okay, default color. So now, what I'm gonna do is every time whenever light change, I want to render this use effect. What I'm gonna do inside the use effect? Inside the use effect, I have a set timeout, okay? What is the delay for the set timeout? So whenever I'm in red, red's duration is the delay I give. Whenever I'm yellow, yellow's duration is the delay I'm gonna give, correct? So how do how do I get that basically? I'm gonna get like light config, correct? Light config of light, whatever the current light, dot

### 00:04:55 · Speaker 1

duration, correct? So light config in this case, light config of red. duration will give me like four thousand or four seconds, correct? Now, so inside the set timeout, what I'm gonna do? Inside the set timeout is where I'm I'll be actually changing the next color. Whenever the red timeout is over, I'm gonna render the yellow, correct? So let me do like set light. So what I'm gonna do again, light config of light config of light.

### 00:05:22 · Speaker 1

I'm gonna set the next, correct? So whenever it was red, after four thousand second I'm gonna set it to yellow. Whenever it was green, after like four second I'm gonna set it to red. One mistake I did, like I did not update it, it is four, five and three, okay? Don't do these mistakes because these are also considered very important in a big product company interviews, okay? So now we have built the logic, now it's a rendering part, correct? In rendering time what I'm gonna do is

### 00:05:54 · Speaker 1

I have a div, okay, which is like outermost div. And this class name as I already shown you, I'm going to give a class name of traffic light here, okay. So this is very easy because that whatever you saw that black outline, that I got from the traffic light. Now very important thing is how to design the internal divs because I need to show a black circle, which is the default color of a color, default color of the traffic light and whenever that is active, only then I need to show the specific color, like show the red only when that red is active. Show yellow

### 00:06:24 · Speaker 1

only when yellow active goes on, correct? So now, let me do that by using the black coat operation. This is something that I always like doing. So where whenever I have to put a condition inside a particular class or style, I use this block coat operation. So by default, definitely we need to give a class called light class. If you see here, the light class is basically responsible for giving that width and height, margin and border radius to make basically that circular light that you are seeing, okay? So now, and we will

### 00:06:54 · Speaker 1

also give the red color by default whatever the red is there but that active we cannot give unless it is actually active correct so what I'm gonna check if light is equals to red okay then I'm gonna give that active class okay

### 00:07:10 · Speaker 1

If not, okay? I'm sorry, not here. Here. If not, then I'm gonna not as in any class to it. So whenever light is red, I'm gonna I'm adding the active color, okay? Red active whatever you are seeing, okay? So I'm gonna just repeat this couple of times where in this case it's gonna be yellow.

### 00:07:31 · Speaker 1

and in this case it's going to be green. Okay? So I'm before I just check I'm also not hundred percent sure but I think it should work but let us see quickly what and all we have done. So I created a light config object which has three colors red yellow and green. Each of it I've specified what is the next after that color and what is the duration that color has to be shown. Okay? So in use effect I've created a set timeout where after a specific duration of the object I'm going to call the set light function set light which is setting the state. I set it to the

### 00:08:01 · Speaker 1

next color. Okay. So now here you see like return I'm returning a div statement where by default it has a traffic light class to give that black background color and inside that every div I'm checking whether light and red light is a default style that every every div has so that you get that black border whenever black color light whenever actually in no that whenever that particular light is not active still I need to show that black color. You might have already seen on the video in the beginning. And then red or green also default classes I'm adding but active class

### 00:08:31 · Speaker 1

is added only if that particular color is active. Okay, so I'm putting that check here. Now let us see whether it is running or not. Okay.

### 00:08:40 · Speaker 1

See here first I am showing that yellow. Yellow. After three after four second I have gone to yellow.

### 00:08:48 · Speaker 1

after five second I'm going to green and after three second I'm going to red and it is turning indefinitely as you can see. Correct? So this was I think the most simplest explanation for this. There are multiple solution that you could try. Another one of the another popular solution that most try is using the switch case instead of using the light config. Inside user effect they keep a switch and keep changing the color. If you can write that please write that solution and put your gist or entire code in the comment section. I'm gonna verify the code and I'll let you know whether it's correct or not. Okay? I'm sure you like the video. If you like the video please like this

### 00:09:18 · Speaker 1

particular video, comment whatever you felt honestly, honestly, share the video with your friends. And do not forget to subscribe to my channel Career with Vasanth. I think you like the video if you like. The only way to appreciate me is just by subscribing my channel and liking the comment. It's not just this video, I have so much good content on my channel where I have a mock interviews, I have a basic React JS interview preparation videos, I have basic JavaScript interview preparation videos, the lot of meetups that I have conducted and those recordings are there. Even there are some DSA tutorials also, system design videos are there. Please make sure you are going to watch

### 00:09:48 · Speaker 1

this video I'm gonna support and make well utilization of my channel. Thank you for watching catch you in the next video.
