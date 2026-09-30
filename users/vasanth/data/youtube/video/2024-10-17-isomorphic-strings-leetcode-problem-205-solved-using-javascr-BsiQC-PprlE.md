---
id: BsiQC-PprlE
title: 'Isomorphic Strings | Leetcode problem #205 | Solved using #javascript | Simplest
  explanation ever'
date: '2024-10-17'
url: https://www.youtube.com/watch?v=BsiQC-PprlE
description: "#dsa #datastructures #algorithm #javascript #typescript \n\n@careerwithvasanth\
  \   is a Youtube channel dedicated to helping candidates clear their interview.\
  \ There are more than 150 videos and new videos will be uploaded every week. If\
  \ you're seriously preparing for interviews and looking for tips and tricks, please\
  \ subscribe to my channel and press the bell icon.\n\nIn this Video I have explained\
  \ how to solve Isomorphic Strings Leetcode problem in #javascript  (https://leetcode.com/problems/isomorphic-strings/description/).\
  \ This is an easy problem, but it will trick you easily, if you don't read the problem\
  \ description fully and make a mistake while solving it. \n\nYou can get more mock\
  \ interviews here : https://www.youtube.com/playlist?list=PLmcRO0ZwQv4SwXLVpnKb_nFQx1Wd2XEjD\n\
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
duration: 00:11:06
model: saaras:v3
transcript: true
---

# Isomorphic Strings | Leetcode problem #205 | Solved using #javascript | Simplest explanation ever

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Career with Vasanth YouTube channel. My name is Vasanth. I hope you all doing well. So this is a video series where I'm explaining the DSA problems. So in this particular video, I'm going to explain you a very important DSA questions. So this is an easy difficulty question called isomorphic strings. uh Whenever anybody reads it, this question looks very easy, so it's marked as easy difficulty problem or lead code, but it's not that easy to solve actually. So that's why I picked this problem. This is one of my favorite problem. Okay, let's see how to solve this problem step by step. And if you're not already subscribed to my channel, please subscribe.

### 00:00:30 · Speaker 1

a good more such good content about front end and interview preparation. Now without wasting further time let's get started. Let's let's see this question given to you in the interview. First thing you do is read the question. Given two strings S and T determine if they are isomorphic. Two strings S and T are isomorphic if the characters in S can be replaced to get T. All occurrence of a character must be replaced with another character while preserving the order of character. No two character may map to the same character but character may map to itself. I know like some sometimes not so

### 00:01:00 · Speaker 1

easy to read this. So let's look at an example. So we have an example S which points to egg, T points to ADD. So output is given as true. So these two are isomorphic strings. Why they are isomorphic string? Because the string S and T can be made identical by mapping E to A and G to D. Let's imagine. Let's say E here maps to A, G here maps to D. Next time whenever G came, that is also mapping to D. Putting other way, if we replace E with A and

### 00:01:30 · Speaker 1

and G with D, these two strings become identical, as simple as that. Correct? Let's go to foo and bar example. So F points to B, F maps to B, O maps to A, O maps to R. We are gone, correct? Because O is supposed to map to A, I now I cannot get foo from bar.

### 00:01:48 · Speaker 1

paper and title same as above. So where all characters pointing to the only one letter so we are able to make the we are able to get this done. If you only think difference between egg and paper is so P is pointing to T here again here also P is pointing to T which is of almost five character this is of around three characters okay. Now just for you to make visualize it clearly I have made I have made a

### 00:02:15 · Speaker 1

a simple diagram here. Okay? So let's look at the diagram. So where we have created let's say JavaScript map where E points to A, G points to D. Next time whenever G comes, I'm checking whether the map contains G or not. If it contains the G, whatever the value of G, is that the same value of whatever has come? Like E is making pointing to A, G is pointing to D. Next time when G comes, so I'm checking whether the value of G which is already existing and the value that has come are same or not.

### 00:02:45 · Speaker 1

correct? So next term also whenever G comes, so it's pointing to the same value, so it's isomorphic. Foo and bar, F pointing to B, O pointing to A. Next is again O pointing to R. Next term whenever O comes, I'm gonna check what is the value for O, which is A, but our expectation is R. So it's not matching, so we're returning false or non-isomorphic string. So this is very easy, Vasanth, so why you have picked this problem? Anybody can do it because all we have to do is create a hash map. Key is the first string letter, value is the second string.

### 00:03:15 · Speaker 1

things later. So we are done. It's not as easy as that. If you look at here, no two characters may map to the same character. It's very very important. So a lot of us will not read the lines very carefully. That is the reason why the question becomes tricky. Okay? So now if we look at another example.

### 00:03:34 · Speaker 1

Example three where S is B A D, T is pointing to B A B. Okay? So let's say the same example like however we did. So B pointing to B, we created a map. A pointing to A and D pointing to B. So this is an isomorphic string according to our our an initial analogy of solving the problem because every character here is pointing to a unique character on the right hand side. But we are violating this condition. No two characters may map to the same character. See, B pointing to B which was fine.

### 00:04:04 · Speaker 1

Now D also pointing to B. So both characters are mapping to the same value. So if you just follow the single map approach, we are not gonna get to know whether it is isomorphic string or not. With this explanation it will become isomorphic, then which is, which is wrong. Okay? So how to solve the problem is we need to have an another map.

### 00:04:23 · Speaker 1

Okay, we need to have two maps.

### 00:04:28 · Speaker 1

where the first string

### 00:04:30 · Speaker 1

first string will be pointing to where first map will point to the this character character from S to character from T. That is a map to maps from the character of T to character of S. Okay? So B is pointing to B which is perfect. Similarly B is pointing to B here reverse also. Okay? Then A is pointing to A which is perfect. Again A is pointing to A which is perfect. Next D is pointing to B.

### 00:04:58 · Speaker 1

Okay? Same way here we would check. So D is pointing to B actually is correct as per our map implementation. But again if you see here, whenever I encounter the B again in the second map, I'll see what is the value of B, which is B. But I'm trying to add B to D. So which is violating the condition. Whenever that map already has a value, the new value should map to existing value, otherwise it's not non-asymorphic. I'm going to reiterate it and then I'm going to start coding. So S and T, we are creating two maps. One where the key is the characters of S and value is the characters from T. In the map two, the keys are

### 00:05:34 · Speaker 1

the characters from the T. Okay? Values are the characters from S. We have to make sure both of this at any given level, no duplication is allowed. Okay? Like no two characters should point should not point to the same character. Okay? Let's start the coding from because of the video time duration sake I'm gonna fast forward the video and I'm gonna explain once after I complete the coding. Okay?

### 00:06:10 · Speaker 1

Yeah. So that my solution got accepted. So now I'm going to explain what I did um quickly. The reason I I fast forward this is so that I don't want to take lot of your time. So if you see like I explained in my solution, I created two maps, map one and map two, both points to initially empty map. And as long as the both the length of the both the strings S and T are not same, definitely they cannot be uh definitely they cannot be isomorphic string. So I'm keeping this check in the beginning. I think they are not going to give a give a test case where S and T are not having equal length, but just on safety note I'm adding, you can

### 00:06:40 · Speaker 1

skip to avoid this as well. Okay? So then you can run the follow up till either length of S or length of T because definitely both are of same length. Now we have F of map one has S of I. Okay? So very first whenever we start let's take an example of EGG and ADD. So there will not be anything. So if like map one dot has S of I, map one has E, no. Then else if map two has A, no. What we are doing we are setting the map one dot set S of I. E is the key and A is the value.

### 00:07:10 · Speaker 1

and map two we are setting A is the key and E is the value okay next when we are setting we are setting the G where G is the key and D is the value and we are setting another as D is the key and G is the value for map two I'm gonna log and I'm gonna show in a while and third thing again we have the G where whenever G came so map one has G yes map one of G is pointing to D so map one dot get so which will give you the value of the whatever G is told which is D

### 00:07:40 · Speaker 1

is equal to t of i? Yes. So, this condition is not met. Not is not met. Okay? So we end this for loop and we return the true. Okay? For your better understanding, I'm going to log both map one and map two. Okay?

### 00:07:56 · Speaker 1

map one, comma map one, okay? And map two, map two, okay? Let me run so that you can visualize how actually the map looks like, okay?

### 00:08:11 · Speaker 1

You see here first the map one was E pointing to A. E pointing to A. Map two was A pointing to E. You see here. Next is E pointing to A and G pointing to D. And map two is A pointing to E and D pointing to G. Okay. Next is if you see here map two where we have the

### 00:08:35 · Speaker 1

map one, map two and again we have the map one here because we did not add a value in the third iteration because map one already had the G. So we have we are not adding a new value, we only compared, okay? So...

### 00:08:49 · Speaker 1

So during the third iteration if you observe so G already has the value of the D. Okay? So but we would we still went ahead and added the value as the map will only contains the unique matching. So G comes again the value whatever we have will currently get replaced. Okay? So intentionally I have written a solution which is suboptimal. So we can optimize this by making a slight modification where you insert the characters only if they don't exist. Okay? If you can make that modification please mention your code in the comment section I'll be more than happy to validate it and confirm. Now we'll go to our edge case. So where I'm adding adding another test case. Okay? So that is

### 00:09:28 · Speaker 1

B A D, B A D and B A B. Okay? So I'm running the code.

### 00:09:40 · Speaker 1

So if you look at my edge case, so first we formed a map. Okay? Between S and T, B is forming, uh, adding B is mapping to B here in the map one, map two also B is mapping to B. In again second iteration, B is A is mapping to A in both the cases. During the third iteration if you see, we tried getting the value where actually this mismatch happened. S of I which was uh in case of D, okay? We were not having the D so

### 00:10:10 · Speaker 1

we could add it to the B. But whenever you come to here map two dot get T of I map two dot of B was supposed to point to B but we are getting it to as D. So it is not matching so I'm writing it as the false. Okay? I hope you understood the question very well. Okay this isomorphic string is one of interviewer's favorite question. So though it looks easy problem it according to me falls in a medium category because if you start someone start just starting the D S I will not be able to predict all the test cases. So practice more of such problems and if you have any doubts mention them

### 00:10:40 · Speaker 1

the comment section and if you're not subscribed to my channel please subscribe. Like the video, like it, share it with your friends who are preparing for the front end DS rounds. And my channel has so much of a good content about front end interview preparation that is system design, machine coding and interview, lot of mock interviews. So make a value utilization of it, share with your friends as well. Follow me on LinkedIn, I have fifty fifty three thousand plus followers on my LinkedIn. I write very actively about front end interview preparation. Thank you so much for watching, catch you in the next video.
