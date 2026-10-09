---
id: kWyTf8H-2BU
title: "Complete ReactJS Interview Prep\U0001F525: Top 10 Questions and Answers for\
  \ Beginners | Ace Your Interview!"
url: https://www.youtube.com/watch?v=kWyTf8H-2BU
date: '2024-06-01'
duration: 00:24:25
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
---

# Complete ReactJS Interview Prep🔥: Top 10 Questions and Answers for Beginners | Ace Your Interview!


## Transcript

### 00:00:00 · Speaker 1

Very first question for you guys would be which is the user effect that will be executed first? Sure. At least half of you would have not able to answer this properly. Okay. Hello all. Welcome back to Kareem with Vasant's YouTube channel. My name is Vasant. I hope you all doing well. This is a very important video where I'm going to answer and explain 10 important React.js hard difficulty question for freshers. So if you're a mid-range or a senior developer, this is going to be around a moderate difficulty questions for you. So despite your experience level, this video is going to be very helpful. And most of the questions

### 00:00:08 · Speaker 2

Hello

### 00:00:30 · Speaker 1

asked here are very thought provoking despite you are using react js in cs you will definitely struggle to answer some of the question that i'll ask and these are very important from the interview point of view so please watch the video till the end all the questions i'll be answering in detail and if you see me first time on the internet i'm vasanth i basically help candidates who clear their interview i make interviews about front end and interview preparation okay if you're not subscribed to my channel please subscribe without waiting for the time let's get started so i have created as you can see a simple project and right side i have the browser and i have created all the 10 xss

### 00:01:00 · Speaker 1

ready with me okay let's put the first exercise

### 00:01:03 · Speaker 1

Very, very simple. I think most of you would think like this is a no-brainer and you'll be able to answer it correctly. But let's see how many of you really answered correctly. So this is the code snippet where I have a use effect and I have a rendering the value of count here whose default value is 0. Inside use effect, I'm incrementing the value by 1. So you can pause the video and mention like video timing as like or the question number 1 and your answer. If you rightly answer, wonderful. If you don't, then listen to my explanation. Okay. So let me just uncomment here.

### 00:01:36 · Speaker 1

So as you can see the output is 1. Why the output is 1 is because the count value is by default is 0 and after that actually the use effect gets rendered. If I have to simply show you the diagramic way of explaining. So the first will be like render. First the things will be rendered on the screen, the first thing. Then what we will do, we will do the set state. Whatever you see like use effect and we have a set stated that will happen here. That set state followed by again there is another render. So that will basically

### 00:02:06 · Speaker 1

render the re-render the value of count as 1 okay sorry for my drawing but to a high level I wanted to explain so three operations so first is the render second one is a set state third is again a render which will actually update the value of count by 1 recently I asked this question on my LinkedIn as well as on my YouTube channel a lot of people have answered it as 0 a lot of people have answered like the user effect is indefinitely that is not the answer so this is the answer okay now comes slightly trickier part okay so where I will update the value like

### 00:02:36 · Speaker 1

this I'm not saving it because I want you to guess the answer for this again you can mention as questions 1b to take a minute think what will be the output and mention the output okay now I'm going to save the code and refresh it here so the count is actually 2 if you see here I have two use effects which has two dependency array and the value passed to dependency array no value passed basically no state variable is passed here so whenever very first question for you guys would be which is the use effect that will be executed first

### 00:03:06 · Speaker 1

Okay, if you know the answer wonderful if not whenever there are two use effects with no dependency values Then react would execute them in the order they are present. Okay, let's say this is a use effect one This is use effect to then use effect one will be executed first followed by use effect to But the problem here is use effects are executed as you know in asynchronous order not they are not executed sequentially, correct? So, but react would ensure despite they are executed in an asynchronous order

### 00:03:36 · Speaker 1

are executed in the order of their creation or in the order of the sequences with which they are created. So, always this use effect 1 will be created first followed by use effect 2.

### 00:03:48 · Speaker 1

the order is guaranteed but the execution is always asynchronous remember that it's not like after this execute this will be executed or the value of count will be updated here and that count value can be used here no okay now i explain the wise count is 2 instead of 3 most of you might have thought it is 3 it's not 3 the reason being so the first this use effect get need to be executed followed by the second use effect correct so whenever the first use effect is getting executed the value of count is 0 okay that is updated by 1 so in this case the value of count has been

### 00:04:18 · Speaker 1

become 1. And next the second use effect will start getting executed where the value of count according to use 1 but it's not 1. The react would still consider the value of count as 0 only and it will add 0 plus 2 and it will make the count as 2. So now both have been completed execution. React would discard the first use effect and use only the second use effect as the most updated value. Okay. It might be slightly confusing but this is how the react works. Okay. You might question like wasent why the second use effect is not taking

### 00:04:48 · Speaker 1

count as one the problem here is again the asynchronous way of execution what if the first user effect takes slightly more time and the second user effect is not getting the value of the count by the time it starts executing correct so i'm where i'm just understand things properly they are asynchronous but they executed sequentially okay that doesn't mean they'll end the execution user effect one might take more time than the user effect two correct so you are user effect you by the time user effect one is executed or by the time when user effect two starts executing

### 00:05:18 · Speaker 1

It may not get the most updated value of count from use effect to 1, correct? So because of which the react has a rule where it will consider the initial value whatever the state variable and then it executes, okay? Because of which we are getting this answer. I am sure at least half of you would have not able to answer this properly, okay? I am happy that at least I am able to help you in that way. Now we will go to exercise 2, okay? Again I am not saving here. Let us go to exercise 2. Again a very very simple. So we have set text and we have handle click.

### 00:05:48 · Speaker 1

There is a button whenever you click the button we are setting the set text with text plus word and react. Okay. If you know the answer again please mention the question number two and your answer. If you already added one comment just edit the comment by adding the com question number two and give your answer. Okay. Let me save and I'll show you what is the output. Okay.

### 00:06:08 · Speaker 1

So the output is react. So if you observe carefully what we did is I appended text with world and then I appended then I added the set text as react. You very well know like I already explained the set text is again a asynchronous operation but in the executed in the order of the sequence that is mentioned. So for first it will mention less text plus world that is set and followed by react. So whatever most recently set definitely that value is retained. So the value here is react. Okay. Now let's go to the access number three.

### 00:06:40 · Speaker 1

I am sorry not here here let us go to exercises 3

### 00:06:46 · Speaker 1

First I'll show things to you. So we have count, set count and we have a set interval here and clear interval and the count. Again if you know the answer, question number three or edit the comment, mention your answer. So here we have a set interval, okay. And inside the set interval we are trying to update the previous value of the whatever the count was there, okay. Let me save and show, let me show you and what is the output. Yeah. So now let's see what is the output. XS3.

### 00:07:12 · Speaker 1

So you start seeing the counter 1, 2, 3. So again, the explanation is very straightforward. This just to give you like for you guys to let get little confused. Nothing much happening here. So we have a set interval which is initiated as soon as the app is rendered. So every one second that interval is getting rendered and the value of it is keep incrementing by one. So it's as simple as that. Let's say navigate from this page to other page. That will be like clear. Okay, very simple. Now we'll go to XAS4 where I intentionally included a class-based component. The reason for that is despite most of you started now.

### 00:07:42 · Speaker 1

learning the functional component there are still lot of applications which are using the class based component so interview they might ask you to know some amount of class based component okay so the question here is if you look let me just update it

### 00:07:57 · Speaker 1

So it's x is 4, here also x is 4. So I'll come back. So it's very simple again. So we have a constructor and a default value of count is 2. And I have a component did mount. For those of you who don't know, this is a like user effect with no parameters, no dependence here. It's like whenever the component is mounted, it will get rendered. Okay. So you're setting the value of count to 1, followed by you have the count. Then again, you're setting the value of count plus 1. Then again, you're trying to log the value. Okay.

### 00:08:27 · Speaker 1

So, two state root statement which are repeated state value plus 1 count value or state dot count plus 1 in both the cases and you are logging them and here you are rendering the state dot count. So, the mind my question is very simple what will be logged in line number 11 and line number 13 and what will be rendered on the line number 17 ok. So, if you know the answer again just mention it in the comment section if not I am going to show you the what is the answer ok.

### 00:08:53 · Speaker 1

So if I go and uncomment

### 00:08:56 · Speaker 1

As you see, the values are actually the rendered on this here are actually 0000 four zeros. Followed by the value of count is just one. Okay. So here also if you see it is same as whatever we did in the set state. So despite we were trying to update the value of count by one, the updated value here that doesn't work that way. The reason being the state update process is a batch process. It's not gonna like you set the state and next link you get the updated state. No. React is gonna take its own sweet time. It's gonna merge the list of things that need to be get updated and then it

### 00:09:26 · Speaker 1

update okay so because of that the value of count in both of these logs is actually 0 okay then whenever this finally whatever is rendered on the screen is obviously 1 because after the set state is completed the UI would re-render whenever UI would re-render it will try to access the value of count which is definitely 1 okay now we'll go to exercise number 5

### 00:09:52 · Speaker 1

So let me close this and open XAS number five. Again very very interesting snippet. So where just for the sake let me like minimize so that you could see the complete code.

### 00:10:07 · Speaker 1

So, where we have excess number 5 again we have count as 0 and we have increment count which has actually 2 set state options ok. And both the set state has doing the same thing it is taking the previous state and adding the count value increment the count by 1 ok. So, whenever you click the button my question would be every time whenever you click on increment what will be the value of 18. Let us say you click on 1 what will be the output you click on 2 what will be the output ok. Again if you know the answer please mention that in the comment section by editing your comment.

### 00:10:37 · Speaker 1

We will go and see what will be the output. Let me click increment once. So, the value is actually 2. Again let me increment by one more time. The value is 4. So, putting that away every time whenever I click on increment button the value is updating by 2. How it is updating value by 2 here, but did not work on the other places. Correct. Let us say if you go to probably x is 2. Here we would be expecting like first express will be rendered followed by reactite. That way it is not happening. But here it is happening. The reason for that is there are two set states.

### 00:11:07 · Speaker 1

In both the set states, we are trying to access the previous state and incrementing that value by 1. Here the difference is, the difference between other and this is, you clearly mentioned when take the previous state and update it, correct? In that case, React would execute these operations in asynchronous order, definitely, but in a sequence, okay? So line number 7 is executed first, followed by line number 10. So the updated value of 7 is set to line number 10 here. Because we have mentioned the previous state need to get updated.

### 00:11:37 · Speaker 1

correct in that case react would honor it let's say the previous state was not there you are just doing like count plus one then the output was same like the excess number one where we would have just honored whatever the most recent one we would have honored that as we clearly mentioned we have to take the previous state the react is honoring and taking the previous state the this execution happening only after this so where it is getting the updated value of the count okay so please do not confuse the previous state with no previous state always remember this this is going to be again

### 00:12:07 · Speaker 1

because they will ask you access number one and then they will ask you access number five and they ask you to justify why it's behaving that way there and why it's behaving this way here. Okay, please be careful. Now let's go to access number six. Access number six, so where again please look at the snippet carefully, where we have one click me button and we have a handle click which is executing on click of that button. We have a count variable whose default value is zero. In line number seven, every time whenever you click the button, we are incrementing the value of count.

### 00:12:37 · Speaker 1

Then we have a set timeout which is basically taking 3 seconds to execute, correct? Inside that we have an alert we are rendering the count, okay? Most of people are watching, some some bulb might have been lightened on their mind, but again if you know the answer mention the question number 6 and put your answer. For those who don't know the answer let me explain. So set timeout as most knows forms a closure. So the closure most of you I think are aware of that famous problem like a set timeout inside a for loop, correct?

### 00:13:07 · Speaker 1

forms the same property where whenever a set timeout is done or whenever set timeout is formed whatever the value of the count that value of the count itself is been retained correct so it doesn't know let's say you update the count in the 30 seconds 100 time set timeout doesn't know what is that you have updated because whatever whenever the closure is formed whatever the value it know that value only it's it knows correct it doesn't know whatever the value got updated so the answer would be always the count would know the last value so the alert would

### 00:13:37 · Speaker 1

always show the last value of the count okay. Let me go and execute excess number 6 okay.

### 00:13:46 · Speaker 1

So exercise number

### 00:13:49 · Speaker 1

Six okay

### 00:13:54 · Speaker 1

So now if we go to axis number six

### 00:13:58 · Speaker 1

and you click

### 00:14:02 · Speaker 1

It became 1. So count is 1. If you see count is 1 here. But the value here is 0 after 3 seconds. Let's say you click count is 2. And the value is actually 1. Even if you click let's say you click multiple times. It has become 4. Correct. You get multiple alerts with the previous values. Okay. Like this. Because every time when you click a new set amount is formed. With the previous value of the count. Okay. Please remember this carefully. So it's nothing to do with React action. It's a fundamental JavaScript. Whenever a closure is formed. It only knows the previous.

### 00:14:32 · Speaker 1

value or current value and you update that value like any number of times in the given duration it will not gonna update that value okay sure now let us go to exercise number seven

### 00:14:43 · Speaker 1

So the code snippet looks slightly lengthier but it is again very simple one itself. So what we are doing here is we have a clear you have a use effect and we have a set interval inside that use effect. And what we are doing is every time for every one second we are trying to get the previous value of the counter and we are updating that count. And then we have another return timeout which you know will clear the timeout and we have another use effect and whenever we have

### 00:15:13 · Speaker 1

have the whenever the count reaches phi we are clearing that interval okay the interval that created here we are clearing that interval here whenever the count reaches the phi okay if you know the answer again mention it in the comment section question number seven and your answer okay but for those who mentioned the answer as something most according to me most people who watch the this particular answer or whoever wrote the answer for this is wrong the simplest answer for this is like id is undefined okay

### 00:15:43 · Speaker 1

All of these big code snippets are created just to create little confusion among you. A lot of people also think like why such snippets are asked in the interview. The whole point of asking such snippets is not that you are going to use the snippets in the day-to-day work but it is just to test like how is your thought process because that thought process of solving a problem is necessary in day-to-day work. Okay. Now if you look at it, ID is defined in line number 7 which is in this block. Definitely ID cannot be used here. So you are going to get an error if you execute this code. Okay which is like ID is undefined.

### 00:16:13 · Speaker 1

finding line number in the whenever you start executing this user effect okay the so the expected answer is error now we'll go to XS 8 okay XS 8 is again a very interesting problem according to me most would give a wrong answer to this as well but let us see so we have a value and set value so where we are having this particular value we are setting the value as 0 and then again we have a user effect with no dependency array we are passing okay and we are setting the interval and every time when

### 00:16:43 · Speaker 1

every one second we are incrementing that value by one okay again if you know the answer please mention that in the comment section I am saying couple of times that you cannot answer not to just to saying like you are not brilliant these snippets are like created by me by taking a load of effort where it's not a very straightforward to answer okay the whole point is like if you are able to visualize these problems and answer consider like you are like at a high level than a normal guy with respect to react knowledge okay now coming to this particular answer

### 00:17:13 · Speaker 1

Or before we go to answer let me quickly explain what is happening. We have a value whose default value is 0 correct. So, what would how react would do is again as I told already.

### 00:17:25 · Speaker 1

So, as I told already the first thing that we would react would do is it would render correct it would render something on the screen after it rendered something on the screen then it comes under the use effect correct it comes under the use effect. So, now inside the use effect you have a timer correct. So, who and you are setting the set interval of 1 second. So, every 1 second this block is going to be keep triggering ok and the value here is set to as value plus 1 set value every time you are setting the incrementing

### 00:17:55 · Speaker 1

value by 1. But the important thing to notice here is whatever the value that it knew during the first use effect, right? After that the use effect is not getting triggered because there is no change in the dependency array. So the value that this particular set interval knew whenever the closure formed is 0. So no matter how many times the set interval executes, the value is always 0 plus 1 which is 1. Okay? Let me execute and show it to you. Okay?

### 00:18:24 · Speaker 1

So I'll go to X as eight

### 00:18:30 · Speaker 1

Now if you see the value is always 1 just for the sake of your understanding I am putting a log here ok value is value ok if you see value you are seeing like multiple times value is always 1 because the closure formed the use effect triggered only once it is not having any dependency array because of which the value did not update so value was always 0 and certain rules keep triggering every second the value is updated to 0 plus 1 which is 1 ok.

### 00:19:00 · Speaker 1

Now the the ask for you or the task for you is I want this value to be keep updating. So mention question number 8 and every time what I want is every time whenever you set the set to value it will be I should get the updated value like 0, 1, 2, 3, 4, 5 should be keep getting the new value. If you know how to do that please mention question number 8 and that particular snippet in the comment section. Okay. Now let's go to question number 9.

### 00:19:25 · Speaker 1

Question number nine okay Question number nine

### 00:19:35 · Speaker 1

So the question number nine is again very straightforward but again a thought provoking question okay. So if you observe the snippet here

### 00:19:44 · Speaker 1

What we have is we have a use effect and inside the use effect we have a line number 11 window.addEventListener you most of you very well know which is like we are adding a event for resize so whenever a particular browser is resized you are gonna get triggered with this particular event. This particular thing is usually used in the programming or website development for doing certain UI changes whenever the browser dimension is changed. For example you have a you have shrink the browser tab that means browser length

### 00:20:14 · Speaker 1

That means probably you are trying to weave in a adjusted, let's say you have two tabs, you have adjusted the dimension. Now you want to render the same content without affecting the UI in that particular dimension because of which usually people use and adjust their UI. Okay. Now we have a add event listener resize and the event that that will be triggered whenever resize happen is handle resize. So again the default value of count is 0. Inside the handle reset we are always incrementing the count value by 1. Okay. And we are rendering in line number 18 the value of count. According to me 90.

### 00:20:44 · Speaker 1

percent of will you will give a right answer to this because you've already seen a lot of this use effect and set chat sort of a question and if you know the answer again if not you have not measured answer for it at least for the ninth one i want you to give a right answer if not pause the video think through and give the right answer okay so the right answer for this would be let me run the code so that you guys can check it

### 00:21:05 · Speaker 1

So uh as you could see

### 00:21:08 · Speaker 1

Let me first try to resize because the event actually get triggered whenever you're trying to resize okay just for your s understanding sake let me put a log here

### 00:21:19 · Speaker 1

screen resized

### 00:21:24 · Speaker 1

And I'm mentioning the count here okay

### 00:21:28 · Speaker 1

So let me try resizing the window now

### 00:21:33 · Speaker 1

So you see like every time I am trying to resize the logs I am getting 43 times and the screen resize is 1. So the value of the count is always 1. The reason again is very straightforward. So here despite you wrote the function outside, it is actually a closure, correct? Whenever window.addEventListener kept a function, whatever the value of the count that was given in this function, the same only it knows, it does not know that count is getting updated, correct? So it keep adding that set count as 0.

### 00:22:03 · Speaker 1

it is incrementing the value by one so if you have to update the count every time you mention the comment section how you do like for example whenever I am resizing the value of count should be keep incrementing how to do that please mention that in the comment section okay now we'll go to the last problem excess 10 okay so I'm sure by now again you will be able to answer this question also properly ah that is the whole intention if you are able to answer this question properly assume yourself like you have learnt some good react concepts in this 20-25 minutes of time okay so now let's say again this

### 00:22:33 · Speaker 1

snippet is very simple the default value of count is 0 you have set count where you are increment the count by 1 2 times and there is an increment button where every time whenever you click you incrementing the count value by same count plus 1 count plus 1 if you know the answer again mention the question number 10 and put your answer in the comment section for those who still like struggling little bit let me explain the answer to them

### 00:22:56 · Speaker 1

So here let me click on increment. The value is 1. Clicking again the value is 2. The answer again is very straightforward. So we have two set counts which are doing the same operation. So the both will be executed asynchronously but ensuring the order of execution. So both of them would pick the count as 0. So no previous value is put here. So we are not expecting the previous value to update. So the count is always 0 plus 1 and 0 plus 1. The most updated value will be whatever is the thing. So in first iteration both are 0.

### 00:23:26 · Speaker 1

So, 0 plus 1 will be 1. Second time 1 plus 1 will be 2. If you go to I think X is number 3 or X is number 5 I think. If you go here, we are trying to access the previous state and update the count by 1. So, you see here you have mentioned the count here and updating the count by 1. Because of which every time whenever you click the both the set states are executing and you are getting the updated value. Whereas in X is number 10 we are we are repeating the same operation. So, one operation will be always discarded and the other operation will be honored which is doing the same thing basically. Incrementing the count value always by 1.

### 00:23:56 · Speaker 1

and not by two okay i hope you enjoyed the session all the code snippets i am going to put like i told in my github repository or in my new book that i am publishing so that you could get the snippets and practice by yourself okay and i am sure most of you like the video only way see there's a lot of time and effort involves in making a video like this if you like the video please like the video and share with your friends and if you're not subscribed to my channel care with person please subscribe whatever you felt honestly regarding the video please mention that will help you to make more such good content thank you so much for watching catch you in the next video

