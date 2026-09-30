---
id: jp_SPyKwXvk
title: Don't watch this @REACT interview preparation video if you're a fresher | You
  might clear ur intervw
date: '2024-06-26'
url: https://www.youtube.com/watch?v=jp_SPyKwXvk
description: "#interview   #react #reactjs  #frontend  #javascript \n\n @careerwithvasanth\
  \   is a Youtube channel dedicated to helping candidates clear their interview.\
  \ There are more than 150 videos and new videos will be uploaded every week. If\
  \ you're seriously preparing for interviews and looking for tips and tricks, please\
  \ subscribe to my channel and press the bell icon.\n\nLink to reconciliation video:\
  \ https://youtu.be/o22KRrxab18\n\nTo get a dedicated one on one,  you can reach\
  \ out to me here: https://topmate.io/vasanth_bhat\n\nLink to questions: https://github.com/coolvasanth/reactjs_interview_preparation/tree/main/src/Top10QuestionsForFreshers\
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
duration: 00:15:54
model: saaras:v3
transcript: true
---

# Don't watch this @REACT interview preparation video if you're a fresher | You might clear ur intervw

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Career with Vasanth YouTube channel. My name is Vasanth. I hope you all doing well. This is super important video for all the freshers and the junior developers who are pursuing the React JS career. I've already made a popular video about top ten React JS interview question and answer. The link to video is also here in the description section. So that video consisted of medium to hard difficulty question. That was a video that anybody could watch because that's a medium to senior level also can watch and for freshers definitely it was at a hard difficulty level. Whereas this video is around easy to medium level which is targeted for most of you who are appearing

### 00:00:30 · Speaker 1

for interviews in service companies, startups or a not so premium product based company. So these questions are very common. If you can answer all the ten questions in one go that I'm asking.

### 00:00:41 · Speaker 1

consider yourself like there is a high chance you'll be able to clear the interview. Fifty to sixty percent probability is definitely there. You'll be able to clear for the most interviews. If you can answer this top ten and the other top ten that I already told, there is a high chance you are going to clear interview seventy to eighty percent. Please watch the video till then because I'm not going to explain just the question and answer. I'm going to explain a lot of concepts and how to approach these questions if they are asked in the interview. Okay? Without wasting further time, let's get started. Question number one.

### 00:01:05 · Speaker 1

So question number one, if you see,

### 00:01:09 · Speaker 1

Yeah, so simple React component where I have named it as X is one and it takes two props, is logged in and name. And if logged in, then we are going to show welcome name. If not of logged in, we show please sign in and followed by the

### 00:01:23 · Speaker 1

nothing just please send we are showing if logged in we are showing welcome followed by the name okay. See one important thing that if you already don't know to notice here is the conditional rendering so and operator as you know is used for the conditional rendering if condition is met we are going to render this if not we are going to don't construct the element at all okay. Now if you know the answer I'm going to tell it only once mention all your answers in the comment section like one two three four five six and till that end whatever the answers you got before I explain please mention it in the comment section so that will show how confident you are about that react fundamentals. Okay.

### 00:01:56 · Speaker 1

So I've saved it. The output is please sign in. Why we got please sign in? I have not passed is login, I have not passed name as well. So when I have not passed is login, the value of props dot is login is undefined. Not of undefined is actually true. Some of you may not know this. Not of undefined, not of null is actually true. So because of it this statement is getting executed, we are getting the please sign in. What if I pass a prop is

### 00:02:19 · Speaker 1

logged in as true. Okay? So you see I got welcome. Now I'll pass name.

### 00:02:28 · Speaker 1

name as

### 00:02:32 · Speaker 1

carried with Vasanth. Okay.

### 00:02:34 · Speaker 1

So because of which you are able to get the whatever I pass that is getting logged here. But very important thing I say if you are practically building a project never do this mistake where all the props should have a default value. Okay? Or make sure if you are using the type script if you are not able to give a default value for some reason those props should be mandatory like a parent cannot call this child component without passing that prop. Never write like this where if you pass a prop or don't pass a prop it's gonna work. Okay? Never write a component like this. Now let's go to exercise number two where I'm asking

### 00:03:04 · Speaker 1

what is the difference between use effect and use layout effect? Okay? I'm going to explain that very much in depth, but let's just get to the first basic definition of it. Use effect runs asynchronously after the paint has been committed to the screen, while use layout effect runs synchronously before the paint. This means use layout effect can block the visual update which is useful for measuring layout and updating the DOM before the browser paints. Okay?

### 00:03:28 · Speaker 1

So the fundamental difference in a very simple words if I have to explain

### 00:03:32 · Speaker 1

use effect actually runs after the component is mounted, use layout effect is before that. So I have actually taken a new tab. Many many recommended me like Basant have a tab explanation becomes easy. So I have a tab in my hand now and whatever I would do here you will be able to see on your screen now.

### 00:03:51 · Speaker 1

So if you can see here, uh we have like use effect and use layout effect, okay? And both use effect and use layout effect both have the component did mount step, correct? So in both the scenarios we are doing the component did mount.

### 00:04:05 · Speaker 1

step number one is same in both the cases. Then we have step number two where the state change happens. So that also happening in the same in both the components. Then we have step number three which is like DOM getting mutated that's also happening same way in both the both the steps both the hooks use effect use effect. The difference is in use effect changes are painted on the screen first. Then use effect runs. Whereas in case of the use layout effect first use layout effect runs followed by the changes are painted on the screen. So the primary

### 00:04:35 · Speaker 1

difference to understand would be use layout effect is used in those scenarios where you don't want to render anything on the screen unless a particular calculation is made. Use effect is used can be used in all the other scenarios. Okay? I'm sure you understood this in depth. But let me give you a simple example for you to understand little bit in

### 00:04:54 · Speaker 0

in depth

### 00:04:54 · Speaker 1

So let's say you have a tool tip. Tool tip is nothing but that black bar you might have seen whenever you go to a website for the first time which explains like what is this, what is this in the website. You have a tool tip, you have to show tool tip under a specific element on the UI, okay? So that tool tip can be shown on the screen.

### 00:05:11 · Speaker 1

only after we calculate the layout of the screen then only tulip can be shown. So this this example I've taken directly from official documentation you can also go ahead and read. So in this case you would use layout effect and you would not use a use effect. Okay. Now there is another catch here. Like I told use effect executed synchronously. Use effect executed asynchronously use layout effect execute synchronously. So you have let's say you have three use layout effect. First use layout effect is executed first followed by the second followed by the third. So putting other way let's say you have using the same state variable in all the three

### 00:05:44 · Speaker 1

the output of the first one is given to the second one and second output of second one given to the third one. Let's say you have a count incrementing the count in all the three. Here it is one, second use effect it will be through two, third use effect it will be three, okay, which is very very important. Whereas in case of use effect, they are executed asynchronously. So there's no guarantee that the previous state value will be given to the next state. Please remember this very carefully. It's a very very important interview topic. Now, let's go to the exercise number three.

### 00:06:10 · Speaker 1

Again very simple snippet. So where we have a count and set count where the value of default count is zero. Inside use effect we have a set interval which runs at every second. And where you are incrementing the value of count at every one second and in the line number thirteen the value of count is printed. Okay? Let me just run the code.

### 00:06:32 · Speaker 1

And here we don't need this prop, so I'm removing the props. Okay, I'm saving. So you see the count is getting incremented every one second. Okay.

### 00:06:42 · Speaker 1

Samsung

### 00:06:49 · Speaker 1

So you see the output. Most of you might have guessed like the output will be keep incrementing every time like it will become one two three going forward but it's not happening. The reason for that is

### 00:06:59 · Speaker 1

use effect has a dependency array but no value is passed so use effect going to execute only once. Inside use effect you have a set interval inside that you have a set count the value of count is incrementing every one second that is actually happening. But the important thing to notice here is set interval forms a closure. Closure you consider like a box okay. So you keep certain things in the box and you keep it outside so that box doesn't know what happens inside. Keep consider it like a keeping a some fruit inside a refrigerator. So that fruit do not know what is the outside temperature it only knows the refrigerator temperature.

### 00:07:29 · Speaker 1

as long as proper electricity is passed to a refrigerator, it always maintains a common temperature. So it doesn't matter outside we are burning, the fruit is still kept whatever kept inside is happy or maintaining a cooler temperature. Same way the set interval, whatever it formed a closure and that closure knows the value it has only as zero. It's not basically changing over a period. Okay, so value of count is only known to it as zero. So you are incrementing the count by one, zero to one. But we are not taking the previous count and incrementing the previous count value. If you would have incremented the previous count value, you would have

### 00:07:59 · Speaker 1

not like the every time one two three four five. But here we are only taking the count and incrementing it count is always zero. So count plus one is producing only one. Okay? And if you know the snippet how to give like one two three four five if I have to get what changes I need to make here. I already told using the previous count but you can add the snippet in the comment section if you know. Now let's go to exercise number four which is very very important concept. Very important concept. How does react reconciliation process work? It's a very important concept. I don't think any of you are react

### 00:08:29 · Speaker 1

interview will complete without answering this question. I very clearly explained this React virtual concept in my one of my very popular video, complete React this into preparation guide in twenty twenty three. Link to video is there in the description, I also put on the screen as well. So please watch the video till the end with the help of a proper diagram I have explained how reconciliation works and till end to end. I have also added lot more other important React this questions also in this video. So please watch the video till the end that as well and this as well. Okay? So I am skipping reconciliation here.

### 00:08:56 · Speaker 1

Let's go to exercise number five. Where exercise number five, I have one array with three elements, one, two, three, and I'm mapping the same array two times.

### 00:09:06 · Speaker 1

and I'm rendering the item of the array. So here key is just item. Here key is item star ten. That's the difference. So I want to tell what will be the output whenever this goes on the screen. Okay? Let me make it exercise number five.

### 00:09:20 · Speaker 1

So you see the output is one two three, one two three.

### 00:09:23 · Speaker 1

So despite whatever the key change you are doing that is irrespective React do not bother whatever the key whatever the value that it will show it will show key is basically as you all know responsible of processing so this has no impact on whatever getting rendered so please remember this very carefully certain snippets are given to confuse you so don't get confused. Now let's go to exercise number six which is actually a textual question okay theoretical question. What is the purpose of React.memo and how does it work okay first let us look at like officially whatever is the definition of it.

### 00:09:53 · Speaker 1

react.memo is a higher order component that memos as the result of a component rendering. It helps to optimize the performance by preventing unnecessary when the props have not changed. It performs shallow comparison of the props, determine if a rerender is needed, okay? In very simple words if I have to say, let's say you have a parent component and a child component. Every time a parent is rendering, if your child is also rendering and it is not necessary actually because child should rerender only when a props passed through are changed or state of the child component is changed. Without that it should not rerender, then make the child component pure.

### 00:10:23 · Speaker 1

component, okay? But there's another add-on question to it. If it has so much advantage, why can't we make like every component as pure component?

### 00:10:32 · Speaker 1

I'm sure most of you might have used react.memo somewhere, but you definitely have not used everywhere. Why we cannot use is every optimization technique comes with its own problems. In case of react.memo, how does react.memo is basically able to memoize?

### 00:10:45 · Speaker 1

memorization is more or less a caching. So it is remembering the previous state, comparing it to the present state and then taking an action. So we have to ensure a lot of states are actually stored. Don't think it in the form of a simple primitive type where you're passing one variable into a child component, it retains that value. Next time when you're passing the next value, it compares and render or not render, doesn't work that way. Let's consider an e-commerce application where you have a giant object that is passed. If the child component starts comparing it, imagine the effect that would have on the

### 00:11:15 · Speaker 1

rendering process. So react.memo should be very carefully used, only should be used whenever it is really required, okay? Because of which most of us are not using it in everyday, okay? Or every component that we have. Now I'm going to exercise number seven, okay?

### 00:11:29 · Speaker 1

So in exercise number seven, looks very simple, little small tricky snippet, where we have the count and set count default value zero, increment we have, and in increment we are calling the method increment where we are setting the count plus one, and we also have another increment method where we are setting the set count as it is, count plus one within the

### 00:11:51 · Speaker 1

the function block itself. We are not going to call any other method. Okay? If you know the answer, again mention in the comment section, very quickly I am going to run the code now. Okay? So I have an increment here, I clicked increment, it became one.

### 00:12:03 · Speaker 1

So I incremented three times. Now if I click here, will there be another count instance which will start from zero? No. It's going to continue because both are end of a day doing the same operation, just the code is in a different way. So it is one is calling the function, one is doing it here itself. The question you might think is which is better? If you have just one statement, this is better. If you have a lot of operations that are happening, then a function is better. There is no a quantifiable performance improvisation in using any of them, each of either of them. Okay? Okay, let's go to excel number nine.

### 00:12:36 · Speaker 1

What will be displayed on the screen initially and after the component mount? It's a very simple snippet. Okay? I think even the kids nowadays would be able to answer, but it's not that easy. Okay? So we have exercise number nine where inside that we have a one user fit and we have a paragraph tag where we are rendering the text. So what will be printed on the screen initially and after the component mount? There is slight difference. I want you to know that. So on the screen, if you observe, let me just print here.

### 00:13:08 · Speaker 1

Okay, if you see here, exercise number nine,

### 00:13:12 · Speaker 1

you are seeing hello world, correct? So your answer would be definitely hello world. What will be displayed on the screen initial and after the component did mount, both the cases are hello world but that is not the answer. The right answer is first the component get mounted. If you remember my explanation to first question where I explained the use effect. During the component mount, it would take the whatever the value of text which is empty and that is printed on the screen. Followed by a use effect executes. Then whatever the value that is there on the use effect, you are doing set text that get re-rendered. Okay? Because the delay is so minute,

### 00:13:42 · Speaker 1

not able to figure out that on the screen but actual execution is the way I wrote. Okay let's go to the let's go to the last question. So this is a question where I'm not solving. I want you to solve. This is a homework. This is a hard difficulty question. Okay if none of you are able to solve definitely mention in the comment section I'll be more than happy to give a answer to this. But if anyone of you are anyone of your anybody basically you are able to solve the problem.

### 00:14:03 · Speaker 1

solve it and put it in your GitHub, Gist or code sandbox anywhere and mention the link in the comment section. I'm going to personally visit it and I'm going to tell whether that's the right answer or not. The ask is, let's say we have a nested object in with a name called item. We have to flatten it and render on the screen. For example, item

### 00:14:22 · Speaker 1

Then we have an array, right? We array whatever is there, ignore it and we have to show like item then followed by nested item one, nested item two. It could be nested to any level. You have to like avoid the level or overcome the level and render all the elements in one below another like UL or LI format in the screen. So I've mentioned already the method where you need to render it. Please complete this exercise. So this will give you a lot of confidence how exactly or where exactly you stand in terms of interpreter. If you're really able to solve this problem, consider you very high chance of clearing an interview. Okay. Now.

### 00:14:56 · Speaker 1

That's all for this video. I'm sure you liked the content whatever I made so far. If you're not subscribed to my channel, please subscribe to my channel Career Fitness. Like my video, comment whatever you felt honestly, share the video with your friends so that they can also get benefited. Now very, very important thing, that's not just this video, there's so many content about front end interview preparation in my channel. The mock interviews, the link is in the description. There's so many mock interviews that I've taken, that playlist is available. There are so many JavaScript related interview preparation videos. If you prepare just that, there's a high chance you'll clear fifty to sixty percent of interview. That playlist link is also in the comment section.

### 00:15:26 · Speaker 1

and there are so many webinars that I have made that link is in the description section. Mank interview preparation separate series that is also there. DSA preparation that's also there. So so many good content in the channel. Please make a best use of it watch all the videos subscribe to my channel so that you keep getting the new videos. And I am very active content creator on LinkedIn follow me on LinkedIn my LinkedIn link is also in the description section. And go to my medium blogs read lot of my blogs very good content I write that also you can get use of it. Okay. Thank you so much for watching. Catch you in the next video.
