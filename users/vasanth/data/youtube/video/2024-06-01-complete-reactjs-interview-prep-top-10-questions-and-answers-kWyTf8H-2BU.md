---
id: kWyTf8H-2BU
title: 'Complete ReactJS Interview Prep🔥: Top 10 Questions and Answers for Beginners
  | Ace Your Interview!'
date: '2024-06-01'
url: https://www.youtube.com/watch?v=kWyTf8H-2BU
description: "#interview   #react #reactjs  #frontend  #javascript \n\n@careerwithvasanth\
  \  is a Youtube channel dedicated to helping candidates clear their interview. There\
  \ are more than 150 videos and new videos will be uploaded every week. If you're\
  \ seriously preparing for interviews and looking for tips and tricks, please subscribe\
  \ to my channel and press the bell icon.\n\nTo get a dedicated one on one,  you\
  \ can reach out to me here: https://topmate.io/vasanth_bhat\nLink to questions:\
  \ https://github.com/coolvasanth/reactjs_interview_preparation/tree/main/src/HardQuestions\
  \ (Don't forget to star the project)\n\nJoin CareerwithVasanth community to discuss\
  \ with other developers: t.me/uncommongeek. \nFollow me on LinkedIn - https://www.linkedin.com/in/careerwithvasanth/\n\
  \nJoin my 3100+ members frontend developer telegram group here: http://t.me/uncommongeek\
  \ \n\nMedium Blog:  https://careerwithvasanth.medium.com/\n\nJavaScript Interview\
  \ preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nJavaScript Custom implementation/polyfills Series: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\n\
  \nFrontend system design series: https://www.youtube.com/watch?v=gN8LQTff21g&list=PLmcRO0ZwQv4RYUD10hUnWjWb-RRSpm3KM&ab_channel=UncommonGeeks\n\
  \nMAANG series for frontend developer: https://www.youtube.com/watch?v=s-b-txm_Gvk&list=PLmcRO0ZwQv4SNhbW4CI4vc-6IHBHCKzZN&ab_channel=UncommonGeeks\n\
  \nFrontend mock interview series: https://www.youtube.com/watch?v=uW7MfzoD1po&list=PLmcRO0ZwQv4SwXLVpnKb_nFQx1Wd2XEjD&ab_channel=UncommonGeeks\n\
  \nShorts for quick access to all frontend resources: https://www.youtube.com/watch?v=8ByBOT7Aehs&list=PLmcRO0ZwQv4SXtrTYIU_dPygZgOgYV81S&ab_channel=UncommonGeeks\n\
  \nTips for freshers: https://www.youtube.com/watch?v=hGIOIdPNNqE&list=PLmcRO0ZwQv4QBiZns-nYX5qnHKAepVeqH&ab_channel=UncommonGeeks"
author: careerwithvasanth
duration: 00:24:25
model: saaras:v3
transcript: true
---

# Complete ReactJS Interview Prep🔥: Top 10 Questions and Answers for Beginners | Ace Your Interview!

## Transcript

### 00:00:00 · Speaker 1

very first question for you guys would be which is the user effect that will be executed first. sure at least half of you would have not able to answer this properly. okay. hello all. welcome back to career with vasant youtube channel. my name is vasant. i hope you all doing well. this is a very important video where i'm gonna answer and explain ten important react js hard difficulty question for freshers. so if you are a mid-range or a senior developer this is gonna be around a moderate difficulty questions for you. so despite your experience level this is gonna be this video is gonna be very helpful. and most of the questions

### 00:00:03 · Speaker 0

first

### 00:00:08 · Speaker 0

Hello all happy

### 00:00:30 · Speaker 1

asked here are very thought provoking. Despite you are using React JS in C-ers, you will definitely struggle to answer some of the question that I'll ask. And this is very important from the interview point of view. So please watch the video till the end. All the questions I'll be answering in detail. And if you see me first time on the internet, I'm Vasanth. I basically help candidates to clear their interview. I make interviews about front end and interview preparation. Okay? If you're not subscribed to my channel, please subscribe. Subscribe without wasting further time, let's get started. So I have created as you can see a simple project and right side I have the browser and I have created all the ten accesses. ready with me. Okay, let's go to the first exercise.

### 00:01:03 · Speaker 1

very very simple. I think most of you would think like this is a no brainer and you'll be able to answer it correctly. But let's see how many of you really answer correctly. So this is the code snippet where I have use effect and I have rendering the value of count here whose default value is zero inside use effect I'm incrementing the value by one. So you can pause the video and mention like video timing as like or the question number one and your answer. If you rightly answer wonderful if you don't then listen to my explanation, okay? So let me just uncomment here.

### 00:01:33 · Speaker 1

Okay

### 00:01:36 · Speaker 1

So as you can see the output is one. Okay? Why the output is one is because the count value is by default is zero. And after that actually the user effect gets rendered. If I had to simply show you the diagrammatic way of explaining. So the first will be like render. Okay? First the things will be rendered on the screen, the first thing. Then what we'll do, we will do the set state. Whatever you see like user effect and we have a set stated, that will happen here. Okay? That set state. Followed by again there is another render. So that will basically

### 00:02:06 · Speaker 1

render the re-render the value of count as one, okay? Sorry for my drawing but to a high level I wanted to explain. So three operations. So first is the render, second one is a set state, third is again a render which will actually update the value of count by one. Recently I asked this question on my LinkedIn as well as on my YouTube channel. A lot of people have answered it as zero. A lot of people have answered it like the use effect runs indefinitely, that is not the answer, so this is the answer, okay? Now comes slightly trickier part, okay? So where I will update the value like

### 00:02:36 · Speaker 1

this. I'm not saving it because I want you to guess the answer. For this, again you can mention as questions one B. Take a minute, think what will be the output and mention the output. Okay? Now I'm going to save the code and refresh it here. So the count is actually two. If you see here, I have two use effects which has two dependency array and the value passed to dependency array, no value passed basically, no state variable is passed here. So whenever very first question for you guys would be, which is the use effect that will be executed first?

### 00:03:06 · Speaker 1

Okay, if you know the answer, wonderful. If not, whenever there are two use effects with no dependency values, then React would execute them in the order they are present. Okay, let's say this is a use effect one, this is use effect two, then use effect one will be executed first, followed by use effect two. But the problem here is, use effects are executed as you know in asynchronous order, not they are not executed sequentially, correct? So, but React would ensure despite they are executed in an asynchronous order,

### 00:03:36 · Speaker 1

they are executed in the order of their creation or in the order of the sequence with which they are created. So always this use effect one will be created first followed by use effect two. But uh

### 00:03:47 · Speaker 1

the order is guaranteed but the execution is always asynchronous. Remember that. It's not like after this executed this will be executed or the value of count will be updated here and that count value we can be used here. No. Okay. Now I explain the why's count is two instead of three. Most of you might have thought it is three. It's not three. The reason being so the first

### 00:04:07 · Speaker 1

this use effect get need to be executed followed by the second use effect. Correct? So whenever the first use effect is getting executed, the value of count is zero. Okay, that is updated by one. So in this case, the value of count has become one. And next, the second use effect will start getting executed where the value of count according to use one, but it's not one. The react would still consider the value of count as zero only and it'll add zero plus two and it'll make the count as two. So now both have been completed execution. React would discard the first

### 00:04:37 · Speaker 1

use effect and use only the second use effect as the most updated value. Okay? It might be slightly confusing, but this is how the React works. Okay? You might question like Vasanth, why the second use effect is not taking count as one. The problem here is again the asynchronous way of execution. What if the first use effect takes slightly more time and the second use effect is not getting the value of the count by the time it starts executing. Correct? So I'm where I'm just understand things properly, they are asynchronous, but they executed sequentially. Okay? That doesn't

### 00:05:07 · Speaker 1

they'll end the execution. Use effect one might take more time than the use effect two. Correct? So you or use effect by the time use effect one is executed or by the time when use effect two starts executing, it may not get the most updated value of count from use effect one. Correct? So because of which the react has a rule where it'll consider the initial value, whatever the state variable and then it executes. Okay? Because of which we're getting this answer. I'm sure at least half of you would have not able to answer this properly. Okay? I'm happy that at least help you in that way. Now we'll go to exercise two. Okay, again I'm not saving here.

### 00:05:42 · Speaker 1

Let's go to exercise two. Again a very very simple. So we have set text and we have handle click. There's a button. Whenever you click the button, we are setting the set text with text plus word and react. Okay? If you know the answer again, please mention the question number two and your answer. If you already added one comment, just edit the comment by adding the question number two and give your answer. Okay? Let me save and I'll show you what is the output. Okay?

### 00:06:08 · Speaker 1

So the output is React. So if you observe carefully what we did is I appended text with world and then I appended then I added the set text as React. You very well know like I already explained the set text is again a asynchronous operation but in the executed in the order of the sequence that is mentioned. So first first it will mention like text plus world that is set and followed by React so whatever most recent is set definitely that value is retained. So the value here is React. Okay. Now let's go to the exercise number three.

### 00:06:40 · Speaker 1

I'm sorry, not here, here. Let's go to exercise three.

### 00:06:45 · Speaker 1

Okay. First I'll show things to you. So we have count, set count and we have a set interval here and clear interval and the count. Again if you know the answer, question number three or edit the comment, mention your answer. So here we have a set interval, okay? And inside the set interval we are trying to update the previous value of the whatever the count was there, okay? Let me save and show, let me show you and what is the output. Yeah, so now let's see what is the output. Exercise three.

### 00:07:12 · Speaker 1

So you start seeing the counter one two three. So again the explanation is very straightforward. This just to give you like for you guys to let get little confused. Nothing much happening here. So we have a set interval which is initiated as soon as the app is rendered. So every one second the that interval is getting rendered and the value of it is keep incrementing by one. So it's as simple as that. Let's say you navigate from this page to other page that will be like clear. Okay very simple. Now we'll go to exercise four where I intentionally included a class space component. The reason for that is despite most of you started

### 00:07:42 · Speaker 1

learning the functional component. There are still a lot of applications which are using the class space component. So interview they might ask you to know some amount of class space component. Okay? So the question here is if you look, let me just update it.

### 00:07:55 · Speaker 1

Okay

### 00:07:56 · Speaker 1

So it's exercise four, here also exercise four. So I'll come back. So it's very simple again. So we have constructor and default value of count is two and I have a component did mount. For those of you don't know, this is a like use effect with no parameters, no dependency array. It's like ask like whenever the component is mounted, it will get rendered, okay? So you're setting the value of count to one, followed by you have the count, then again you're setting the value of count plus one, then again you're trying to log the value, okay?

### 00:08:26 · Speaker 1

okay? So two state through statement which are repeated. State value plus one. Count value or state.count plus one in both the classes and you are logging them. And here you are rendering the state.count. So the my question is very simple what will be logged in line number eleven and line number thirteen and what will be rendered on the line number seventeen. okay? So if you know the answer again just mention it in the comment section if not I'm gonna show you the what is the answer. okay?

### 00:08:53 · Speaker 1

So if I go and uncomment

### 00:08:56 · Speaker 1

As you see, the values are actually the rendered on this here are actually zero zero zero zero four zeros. Followed by the value of count is just one. Okay? So here also if you see it is same as whatever we did in the set state. So despite we are trying to update the value of count by one, the updated value here that doesn't work that way. The reason being the state update process is a batch process. It's not gonna like you set the state and next line you get the updated state. No. React is gonna take its own sweet time. It's gonna merge the list of things that need to get updated and then

### 00:09:13 · Speaker 0

Update

### 00:09:26 · Speaker 1

would update, okay? So because of that the value of count in both of these logs is actually zero, okay? Then whenever this finally whatever is rendered on the screen is obviously one because after the set set is completed the UI would re-render. Whenever UI would re-render it will try to access the value of count which is definitely one, okay? Now, we'll go to exercise number five.

### 00:09:52 · Speaker 1

So let me close this and open exercise number five. Again very very interesting snippet. So where just for the sake let me like minimize so that you could see the complete code.

### 00:10:05 · Speaker 1

Okay. So where we have exercise number five, again we have count as zero and we have increment count which has actually two set state options. Okay. And both the set state has doing the same thing it is taking the previous state and adding the count value incrementing the count by one. Okay. So whenever you click the button my question would be

### 00:10:25 · Speaker 1

Every time whenever you click on increment, what will be the value of eighteen? Let's say you click on one, what will be the output? You click on two, what will be the output? Okay, again if you know the answer, please mention that in the comment section by editing your comment. So now we'll go and see what will be the output. Let me click increment once. So the value is actually two. Again let me increment by one more time, the value is four. So putting that away, every time whenever I click on increment button, the value is updating by two. How it is updating value by two here but did not work on the other places, correct? Let's say

### 00:10:55 · Speaker 1

go to probably exercise two. Here we would be expecting like first text plus word be rendered followed by react right that way it's not happening. But here it is happening. The reason for that is there are two set states. In both the set states we are trying to access the previous state and incrementing that value by one. Here the difference is difference between other and this is you clearly mentioned take the previous state and update it correct. In that case react would execute these operations in asynchronous order definitely but in a sequence.

### 00:11:25 · Speaker 1

Okay, so line number seven is executed first, followed by line number ten. So the updated value of seven is fed to line number line number ten here. Because we have mentioned the previous state need to get updated, correct? In that case, React would honor it. Let's the previous state was not there. You are just doing like count plus one, then the output was same like the exercise number one, where we would have just honored whatever the most recent one, we would have honored that. As you clearly mentioned, you have to take the previous state. The React is honoring and taking the previous state.

### 00:11:55 · Speaker 1

this execution happening only after this so where it is getting the updated value of the count. Okay? So please do not confuse the previous state with no previous state. Always remember this. This is going to be again tricky because they'll ask you exercise number one and then they'll ask you exercise number five and they ask you to justify why it's behaving that way there and why it's behaving this way here. Okay? Please be careful. Now let's go to exercise number six.

### 00:12:19 · Speaker 1

Exercise number six. So where again please look at the snippet carefully where we have one click me button and we have a handle click which is executing on click of that button. We have a count variable whose default value is zero. In line number seven every time whenever you click the button we are incrementing the value of count. Then we have a set timeout which is basically taking three seconds to execute. Correct? Inside that we have an alert we are rendering the count. Okay? Most of people are watching some some bulb might have been lightened on their mind.

### 00:12:49 · Speaker 1

but again if you know the answer mention the question number six and put your answer for those who don't know the answer let me explain so set timeout as most know is forms a closure so the closure most of you I think are aware of that famous problem like a set timeout inside a for loop correct so this also forms the same property where whenever a set timeout is done or whenever set timeout is formed whatever the value of the count that value of the count itself is been retained correct so it doesn't know let

### 00:13:19 · Speaker 1

say you update the count in the three seconds hundred time. Set time doesn't know what is that you have updated because whatever whenever the closure is formed, whatever the value it know, that value only it's it knows, correct? It doesn't know whatever the value got updated. So the answer would be always the count would know the last value. So the alert would always show the last value of the count, okay? Let me go and execute exercise number six, okay?

### 00:13:46 · Speaker 1

So exercise number

### 00:13:49 · Speaker 1

Six. Okay.

### 00:13:54 · Speaker 1

So now if you go to exercise number six

### 00:13:58 · Speaker 1

and you click

### 00:14:01 · Speaker 1

See? It became one, so count is one, if you see count is one here, but the value here is zero after three seconds. Let's say you click, count is two.

### 00:14:10 · Speaker 1

and the value is actually even if you let's say you click multiple times it has become four correct you get multiple alerts with the previous values okay like this because every time when you click a new set of amount is formed with the previous value of the count okay please remember this carefully so it's nothing to do with react excel it's a fundamental java script whenever a closure is formed it only knows the previous value or current value and you update that value like any number of times in the given duration it will not going to update that value okay

### 00:14:12 · Speaker 0

actually one

### 00:14:40 · Speaker 1

Now let's go to exercise number seven

### 00:14:43 · Speaker 1

the the the code snippet looks slightly lengthier but it is again very simple one itself, okay? So what we are doing here is we have a clear uh you have a use effect and we have a set interval inside that use effect, okay? And what we are doing is every time for every one second we are trying to get the previous value of the count and we are updating that count, okay? And then we have another return timeout which you know will clear the timeout and we have another use effect and whenever we

### 00:15:13 · Speaker 1

we have the whenever the count reaches five we are clearing that interval. Okay the interval that created here we are clearing that interval here whenever the count reaches the five. Okay. If you know the answer again mention it in the comment section question number seven and your answer. Okay. But for those who mentioned the answer as something most according to me most people who wrote the this particular answer or whoever wrote the answer for this is wrong. The simplest answer for this is like ID is undefined.

### 00:15:43 · Speaker 1

all of these big code snippets are created just to create little confusion among you. lot of people also think like why such snippets are asked in the interview. the whole point of asking such snippets is not that you are going to use the snippets in the day to day work but it is just just to test like how is your thought process because that thought process of solving a problem necessary in day to day work. okay. now if you look at it ID is defined in line number seven which is in this block definitely ID cannot be used here. so you are going to get an error if you execute this code. okay which is like ID is empty.

### 00:16:13 · Speaker 1

defined in line number. um in the whenever you start executing this use effect. Okay? So the expected answer is error.

### 00:16:20 · Speaker 1

Now we'll go to exercise eight, okay? Exercise eight is again a very interesting problem. According to me, most would give a wrong answer to this as well, but let us see. So we have value and set value. So where we are having this particular value, we are setting the value as zero. And then again, we have a use effect with no dependency array we are passing, okay? And we are setting the interval and every time whenever every one second, we are incrementing that value by one, okay? Again, if you know the answer, please mention that in the comment section.

### 00:16:50 · Speaker 1

I'm saying a couple of times that you cannot answer not to just to saying like you're not brilliant. These snippets are like created by me by taking a load of effort where it's not like very straightforward to answer. Okay. The whole point is like if you're able to visualize these problems and answer consider like you are like at a high level than a normal guy with respect to reaction knowledge. Okay. Now coming to this particular answer or before we go to answer let me quickly explain what is happening. We have a value whose default value is zero. Correct? So what would how React would do is again as I told already

### 00:17:25 · Speaker 1

So, uh, as I told already, the first thing that we would react would do is it would render, correct? It would render something on the screen. After it rendered something on the screen, then it comes under the use effect, correct? It comes under the use effect. So now inside the use effect, you have a timer, correct? So who and you're setting the set interval of one second. So every one second this block is going to keep triggering, okay? And the value here is set to as value plus one. Set value every time you're setting the incrementing

### 00:17:55 · Speaker 1

the value by one. But the important thing to notice here is, whatever the value that it knew during the first use effect, right? After that the use effect is not getting triggered because there is no change in the dependency array. So the value that this particular set interval knew whenever the closure formed is zero. So no matter how many times the set interval executes, the value is always zero plus one which is one, okay? Let me execute and show it to you, okay?

### 00:18:24 · Speaker 1

So, I'll go to exercise eight.

### 00:18:30 · Speaker 1

Now, if you see, the value is always one, just for the sake of your understanding, I'm putting a log here, okay? Value is

### 00:18:39 · Speaker 1

value, okay? If you see, value you're seeing like multiple times, value is always one because a closure formed, the use effect triggered only once. It's not having any dependency array because of which the value did not update. So value was always zero and certain times keep triggering every second, the value is updated to zero plus one which is one, okay? Now the the ask for you or the task for you is I want this value to be keep updating. So mention question number eight and every time what I want is every time whenever you

### 00:19:09 · Speaker 1

set the set value it will be I should get the updated value like zero one two three four five it should be keep getting the new value. If you know how to do that please mention question number eight and that particular snippet in the comment section. Okay. Now let's go to question number nine.

### 00:19:25 · Speaker 1

Question number nine, okay? Question number nine, okay?

### 00:19:35 · Speaker 1

So the question number nine is again very straightforward but again a thought provoking question, okay? So if you observe the snippet here,

### 00:19:44 · Speaker 1

What we have is we have a use effect. And inside the use effect, we have a line number eleven, bindo.add event listener. You most of you very well know.

### 00:19:54 · Speaker 1

which is like we are adding a event for resize so whenever a particular browser is resized you are gonna get triggered with this particular event. This particular thing is usually used in the programming or website development for doing certain UI changes whenever the browser dimension is changed. For example you have a you have shrink the browser tab that means browser length that means probably you are trying to weave in a adjusted let's say you have two tabs you have adjusted the dimension now you want to render the same content without affecting the UI in that particular dimension because of which

### 00:20:24 · Speaker 1

usually people use and adjust their UI, okay? Now we have a add event listener resize and the event that that will be triggered whenever resize happen is handle resize. So again the default value of count is zero. Inside the handle resize we are always incrementing the count value by one, okay? And we are rendering in line number eighteen the value of count. According to me ninety percent of you will give a right answer to this because you've already seen a lot of this use effect and set chat sort of a question. And if you know the answer again, if not you have not mentioned answer for it.

### 00:20:54 · Speaker 1

at least for the ninth one I want you to give a right answer. If not pause the video think through and give the right answer. Okay? So the right answer for this would be let me run the code so that you guys can check it.

### 00:21:05 · Speaker 1

So, uh as you could see,

### 00:21:08 · Speaker 1

Let me first try to resize because the event actually get triggered whenever you're trying to resize. Okay? Just for your understanding sake, let me put a log here.

### 00:21:19 · Speaker 1

screen resized. Okay.

### 00:21:24 · Speaker 1

and I'm mentioning the count here, okay?

### 00:21:28 · Speaker 1

So let me try resizing the window now.

### 00:21:33 · Speaker 1

So you see like every time I'm trying to resize, the the logs I'm getting forty three times and the screen resize is one. So the value of the count is always one. The reason again is very straightforward. So here, despite you wrote the function outside, it's actually a closure, correct? Whenever window.add event listener you have kept a function, whatever the value of the count that was given in this function, the same only it knows. It doesn't know that count is getting updated, correct? So it keep adding that set count as zero.

### 00:22:03 · Speaker 1

and it is incrementing the value by one. So if you have to update the count every time, you mention in the comment section how you do. Like for example, whenever I'm resizing, the value of count should be keep incrementing. How to do that? Please mention that in the comment section, okay? Now we'll go to the last problem. Exercise ten, okay? So I'm sure by now again you will be able to answer this question also properly. That is the whole intention. If you are able to answer this question properly, assume yourself like you have learned some good React concepts in this twenty twenty five minutes of time, okay? So now let's say again

### 00:22:33 · Speaker 1

Snippet is very simple. The default value of count is zero. You have set count where you increment the count by one, two times. And there's an increment button where every time whenever you click, you're incrementing the count value by same, count plus one, count plus one. If you know the answer again, mention the question number ten and put your answer in the comment section. For those who still like struggling a little bit, let me explain the answer to them.

### 00:22:55 · Speaker 1

Okay. So here let me click on increment. The value is one. Clicking again the value is two. The answer again is very straightforward. So we have two set counts which are doing the same operation. So the both will be executed asynchronously but ensuring the order of execution. So both of them would pick the count as zero. So no previous value is put here. So we are not expecting the previous value to update. The count is always zero plus one and zero plus one. The most updated value will be whatever is the thing. So in first

### 00:23:25 · Speaker 1

generation both are zero so zero plus one will be one. Second time one plus one will be two. If you go to I think exercise number three or exercise number five I think. If you go here we are trying to access the previous data and update the count by one. So you see here you have mentioned the count here and updating the count by one. Because of which every time whenever you click the both the sets are executing and you are getting the updated value. Whereas in exercise number ten we are we are repeating the same operation so one operation will be always discarded and the other operation will be honored which is doing the same thing basically. Increment the count value.

### 00:23:55 · Speaker 1

always by one and not by two. Okay? I hope you enjoyed the session. All the course snippets I'm going to put like I told in my GitHub repository or in my new book that I'm publishing so that you could get the snippets and practice by yourself. Okay? And I'm sure most of you like the video. Only way, see there's a lot of time and effort involves in making a video like this. If you like the video, please like the video and share with your friends. And if you're not subscribed to my channel Care with Vasan, please subscribe. Whatever you felt honestly regarding the video, please mention that will help you to make more such good content. Thank you so much for watching. Catch you in the next video.
