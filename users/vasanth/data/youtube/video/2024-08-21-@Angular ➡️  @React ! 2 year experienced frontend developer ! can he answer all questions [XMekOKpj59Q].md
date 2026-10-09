---
id: XMekOKpj59Q
title: "@Angular \u27A1\uFE0F  @React ! 2 year experienced frontend developer ! can\
  \ he answer all questions ? ?"
url: https://www.youtube.com/watch?v=XMekOKpj59Q
date: '2024-08-21'
duration: 00:24:17
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 3
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
---

# @Angular ➡️  @React ! 2 year experienced frontend developer ! can he answer all questions ? ?


## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Kairi with Vasant YouTube channel. My name is Vasant. I hope you're all doing well. So I assume this is a video series where we're discussing about the mock interview. In this particular video with me, I have Vishal. Vishal is a two year experience front end developer. He having experience of Angular and relatively he's

### 00:00:15 · Speaker 2

trying to transition into React. So it's going to be a good interview if you are also from the similar background. You're from some other tech, you're trying to transition into React. So what are the challenges that you would face? I'm going to discuss those also with Vishal. More about Vishal Lenny, he'll be explaining. And this is going to be a combination of basics of JavaScript, machine coding, and a React.js. Some basics of React.js. So please watch the video till the end. For some reason, if Vishal is not able to answer, right answer, give right answer to a question that I asked, I'm going to give right answer to the end. So please watch the video till the end.

### 00:00:45 · Speaker 2

We shall see if you can introduce yourself we can get started

### 00:00:47 · Speaker 3

Sure Asantah. Hey Asantah, good afternoon. I am Visha. I am a fintech engineer. I am working as a fintech engineer for the last two years. So in a startup. Yeah, that's it about me.

### 00:00:59 · Speaker 2

Sure sure Michelle shall we start the interview now Michelle

### 00:01:03 · Speaker 3

Yes, before that I have a doubt. Yeah. Because I have been interested in a project called, like it's used for a video call recording. I am facing some problems in that regarding group chat building and reducing the screen size, like styling for different screen sizes and many more problems as well. Go ahead. How will you, can you give me a condition for that?

### 00:01:24 · Speaker 1

I'm not even a function button

### 00:01:24 · Speaker 2

Good that you brought this question up. See, video calling is one of the complex feature to build. Though like chat like Zoom and Google Meet looks very simple, but it's not very easy to build if you are given that such project. Okay. Lately, I've been using a tool called Zego Cloud. I've told about this product in the past as well. Where Zego Cloud is a tool which where you can build the entire video calling just with help of this particular product. So they have a thing called UI kits where the one of the primary challenge is to build the product end-to-end. So we have to go and

### 00:01:54 · Speaker 2

which protocol to use how to handle cross browser support how to handle group chat how to handle one-on-one chat all of those things actually taken care by the ziggeo cloud as you see it's also it's not just about the video calling they have audio calling they have any other multimedia sort of calling involved all the features are available as a part of the ziggeo cloud and the question like you asked how do we handle the dynamic layers how do we handle the beautification of the face how how do we handle like into messages whenever you're on call if you have to send some messages how do we handle that all of the things are actually given out

### 00:02:24 · Speaker 2

the box by the ui kit of the zego cloud and they also have something called like 10 000 free seconds let's say you are a new user you just sign up for their particular portal you're gonna get 10 000 free seconds which you can use for free only after that if you're like very satisfied with the tool you can continue to use their product okay so it's a very good product not just you i recommend it for anybody who is having a video calling requirement they can use it okay hope that clarifies your doubt we shall okay

### 00:02:53 · Speaker 2

Sure, now let us start with a very interesting question Vishal. Okay, this I have recently I've asked this question multiple times in the interview. I'm presenting a whiteboard. Okay, let's say we have to build a tool similar to Google Calendar. Sorry, Google Calculator. Okay, I'm drawing on the screen. Okay, like for example, a typical example, how a Google Calculator would look like. The Google Calculator means whenever you type something like 2 plus 2 on the Google search and you would enter, right?

### 00:03:23 · Speaker 2

will be prompted with a calculator

### 00:03:26 · Speaker 2

So there's a simplicity say I'm quickly drawing few things okay

### 00:03:26 · Speaker 3

Oh

### 00:03:39 · Speaker 2

I think this is the area where usually the user would type something. For example, you type one plus two here and you click on is equal to, you will get the answer, correct? Or you can use like one plus, you can click on this button and you're gonna get the output. So now my question is, let's see how to build a feature like this in the browser, Vishal. Okay, the UI that I have already built, building UI is not a great challenge. Now, after building the UI, you have to basically process the equation and to give answers, right? Let's start from there. How is that you're gonna solve the problem? Let's say one plus two star three is there.

### 00:04:09 · Speaker 2

One plus two R three you have to process this equation to give the results right what all things comes to your mind as a part of building this please tell me

### 00:04:19 · Speaker 3

okay we can use the reusable functions like we can create functions with for addition one and for multiplication one and for division one okay what you'll do is you will return uh when uh like user clicks on equal to but will store value in some variable local variable what you'll do is you will first uh get the inputs from it so while user the click while user clicks on plus we will in the back end what we'll do is we will just add the function name and the argument as two so one

### 00:04:49 · Speaker 3

plus one and that argument I mean sorry one comma that argument and then after that uh next uh next thing will come like uh with this value and a multiplication with three that multiply function we will call it

### 00:05:02 · Speaker 2

So so we shall tell me one thing is it this you are gonna do in the back end or all the things of this processing happens only on the front end or client side

### 00:05:09 · Speaker 3

Client side I'm going to do okay

### 00:05:10 · Speaker 2

Okay complete processing happens on the client side correct no no back

### 00:05:13 · Speaker 3

No simple thing okay we don't need to do like back anything for this

### 00:05:18 · Speaker 2

So now as you told, we have 1 plus 2 star 3, correct? So you have to process the equation. Will you start processing after user hits is equal to or before that?

### 00:05:26 · Speaker 3

After user clicks equal to

### 00:05:27 · Speaker 2

Okay, after user clicks on is equal to, you have a 1 plus 2 star 3, which is typically in a string format.

### 00:05:34 · Speaker 2

it's in a string it's not we cannot put it a number because we have the expression plus and stuff so it's in a string format so copying that entire string one plus two star three okay and you are basically processing that correct so you told like you're going to create multiple methods for plus addition subtraction multiplication so how are you going to process this one plus two star three can you please quickly tell me

### 00:05:57 · Speaker 3

we can store those like separate characters like the plus and multiplication and division in a separate string and we'll check if this the current element of the string is like present in that chart

### 00:06:10 · Speaker 2

No, no, not that. Like, for example, like I have given you one plus two star three, and you have a function like calculate.

### 00:06:10 · Speaker 3

No no not that

### 00:06:16 · Speaker 2

What are the first thing that you are going to do? Can you please tell me?

### 00:06:18 · Speaker 3

And the user clicks equal to right

### 00:06:20 · Speaker 2

Yes, so when user click on it, you called a function called calculate. The calculate function has the expression 1 plus 2 star 3. What is the that first thing that you are going to do in that function? Please tell me.

### 00:06:21 · Speaker 3

Great

### 00:06:32 · Speaker 3

I'll run a loop for using that string. Okay. What I will do is when the first element comes in, I will check if that any of the symbol is present in that first element. Okay. If it's not, it should be a number because we can't type anything.

### 00:06:46 · Speaker 2

Incorrect correct

### 00:06:46 · Speaker 3

other than number correct so i'll just uh pass it and uh i'll push it to i'll add it to a separate number as a like thing and then i'll check the next one next one next one since it's uh like uh symbol here even if it's an spits another number uh then what you'll do is you can introduce a right number followed by another number so it should be like one plus one and one it's eleven so what you'll do is we will add that number uh like into one into ten and plus that number so it will it becomes

### 00:07:16 · Speaker 3

one number plus we will check that symbol so since this is a plus symbol for that plus we will be allocate allocating that one function right so we have that one that one separately that's it this function so we will send that next argument as a next number or symbol like next number should be there because we can't like give two symbols

### 00:07:43 · Speaker 1

Links are

### 00:07:44 · Speaker 1

Please please please go

### 00:07:44 · Speaker 3

Or two

### 00:07:48 · Speaker 3

Next we will check that number and then we will check if the continuously if we are getting a number like 22 or something if there is nothing in forward be only symbol we will just pass the value to that number and whatever we getting the value we will return and like add it to that

### 00:08:03 · Speaker 2

Sure, sure. Sounds good, Vishal. See, as I think you did not while introducing, you did not say this. Basically, you're from the mechanical background, correct? And you're turning to IT because of interest. I think the third year, in the second year, third or fourth semester, most of, I think most different universities will have this.

### 00:08:11 · Speaker 3

And you're

### 00:08:21 · Speaker 2

Think of evaluating an expression. There are different ways to evaluate an expression, like infix, postfix, and different ways. How do they evaluate an expression? Okay, so where this is actually taught. Whatever you're telling is correct, but there is more formal approach to solve. Only one last question I ask regarding this, and then probably we'll go to the other problem. So as you have to build like, as you are doing this in Google Calendar or anywhere you might have Google Calculator or any other things you might have seen, there is an undo and redo operation, correct? So you have a star three, I mentioned like one plus two,

### 00:08:51 · Speaker 2

So then I enter like star and three. Now if I do control plus Z, right? So the star three vanished, correct? I did control shift Z, star three appeared again. Getting my point, right?

### 00:09:02 · Speaker 2

and start to reappear again okay if you have the feature the undo and redo operation okay which data structure you will use which are just that is my question which data structure you will use and why

### 00:09:02 · Speaker 3

It's okay.

### 00:09:15 · Speaker 3

or unknown credo okay I'll use um

### 00:09:20 · Speaker 3

Most probably object data structure

### 00:09:24 · Speaker 2

So why and anything you can look into basically any data structure but the question will be why why you are using that particular data structure

### 00:09:30 · Speaker 3

object or array we can use both we can store those uh like every single options like

### 00:09:38 · Speaker 3

symbol and number as a separate element and when user click control z you will just remove and usually we will catch it in a different variable because you if the user just like want to undo it so we can push it back to the array

### 00:09:52 · Speaker 2

Got it. Got it. It's it's not a wrong answer, but for audience who are watching the right answer is stack actually. Okay. The stack is where you're going to keep pushing the operations. Like, for example, one you entered first value is one. Then you enter into one plus is the next entry. Then one plus two is the next entry. One plus two star three is the next expression. Okay. You do control Z. you're going to pop the top value and whatever is the top at that point in time that we are going to show on the ui same thing we are going to keep doing redo is also very simple whatever you remove from the uh

### 00:10:22 · Speaker 2

the undo stack you're gonna put it in the redo stack once you whenever you redo whatever the top of the redo you're gonna pick and put it on the stack of the undo operation so you're gonna use two stacks one to perform undo one to perform the redo okay stop sharing this Vishal okay can you please open code sandbox and uh like search for like react js code sandbox react the question Vishal is very simple okay the question is should be you have to implement a password strength checker okay where uh you will

### 00:10:52 · Speaker 2

uh you will have a function okay let's break it into two things first thing is that you have an input text box whatever user enters in the input text box that's going to be passed into our function correct and within that function you need to check whether that password is whatever the password strength you need to render that password strength on the ui like whether it's weak whether it is mean like weak medium and strong three things you need to represent okay let me tell you the conditions like if the password or else we can make it even more simplified

### 00:11:22 · Speaker 2

the audience are should not get confused if a password has a capital case a smaller case and a number it's a strong password getting my point audience also i'm saying again if a password has a small case capital case and a number then it is a strong password you write a function which accepts a password and retells whether that particular password is strong or not so we are not taking weak strong and all we are just only checking whether a password is strong or not okay if it has only a

### 00:11:52 · Speaker 2

small character and alpha uh capital character it should uh it should tell it's not a strong password only when there's a small character capital character and a number then it should tell like it's a strong password first implement that function okay and you could just log it log the output once after you completely successfully implement that then we will try to integrate that into an input box you just have around 10 to 12 minutes to implement this okay please go ahead and start

### 00:12:16 · Speaker 3

Start function

### 00:12:25 · Speaker 2

audience who are watching as i in the beginning i told we shall just starting with react he has come till an extent of hooks and some moment of react he has not like mastered it but still he is trying to transition his career with react and want to learn react so that's the reason he is giving the chance of reading the values i mean uh or giving a shot at uh solving the machine coding question react i appreciate that yeah please get continue we shall

### 00:12:52 · Speaker 3

So for this, I think the solution I will be thinking of, like checking the character code for this.

### 00:13:01 · Speaker 3

character code is like for capital letters there will be a range of character code and for numbers there will be a range of character code and for small characters there will be a range of character code correct I am not aware of the syntax as of now can I use Google for searching

### 00:13:12 · Speaker 2

Yeah please you can sort that yeah okay that you can hold and drag down like

### 00:13:17 · Speaker 3

No

### 00:13:19 · Speaker 2

you can expand it yeah that widget you hold and drag somewhere in the screen like just drag it down you're able to do right

### 00:13:27 · Speaker 2

No continue yes

### 00:13:35 · Speaker 1

Just the advice to you and everyone who is watching the video anytime you want you do want some syntax to be known right you don't know and you want to search

### 00:13:35 · Speaker 2

And this stuff

### 00:13:38 · Speaker 2

Anytime you want you do want some syntax to be known right you don't know and you want

### 00:13:42 · Speaker 1

So always as the interviewer like Vishal did

### 00:13:42 · Speaker 2

So always as the interviewer like Vishal did

### 00:13:44 · Speaker 1

Most interview will be fine if you for you to search the syntax

### 00:13:44 · Speaker 2

most interview will be fine if you for you to search the syntax but don't take consider like explicit and search immediately because some companies do have a rules where if you search something from the outside they would have a strict rules of like rejecting the candidate so don't give that chance you be explicit and ask so that if interview okay you search okay i think line number seven it should be const it should the spelling mistake i assume michelle

### 00:14:14 · Speaker 2

plan to handle the numbers whether the number is present in a string or not

### 00:14:18 · Speaker 3

And this one code zero and code eight

### 00:14:24 · Speaker 3

The number is starting from zero so we are checking till nine so till eight.

### 00:14:34 · Speaker 2

or watching the video you guys can also like practice this in parallel like you can write a code and you can put your code in the comment section or you can create a gist and paste the gist link of gist also in the comment section i will definitely be more than happy to verify it and tell whether that's the right answer or not

### 00:14:34 · Speaker 3

That's true

### 00:14:50 · Speaker 2

You continue with that yeah

### 00:14:54 · Speaker 2

You can remove that E for a while like you can just directly read the value in line number five

### 00:15:01 · Speaker 3

Line number five okay

### 00:15:03 · Speaker 2

Let's consider that as an argument you're directly passing the string

### 00:15:07 · Speaker 2

Okay

### 00:15:07 · Speaker 3

Okay

### 00:15:10 · Speaker 2

Yeah yeah

### 00:15:12 · Speaker 3

Still we need to get that argument right

### 00:15:15 · Speaker 2

Yeah yeah you should have E yeah that's itself the value yeah you're not basically extracting anything yeah

### 00:15:22 · Speaker 3

Also check out

### 00:15:25 · Speaker 3

with some string what you'll do let me finish this first

### 00:15:42 · Speaker 3

I'll give some random I'll give one capital letter one

### 00:15:48 · Speaker 3

One small letter and one number

### 00:15:50 · Speaker 2

Sure

### 00:15:51 · Speaker 3

instruction

### 00:15:53 · Speaker 3

A control how to view the console here

### 00:15:56 · Speaker 2

You see console in the bottom right console 14

### 00:16:00 · Speaker 3

Okay

### 00:16:02 · Speaker 3

Great

### 00:16:04 · Speaker 2

It will be weak

### 00:16:06 · Speaker 3

Um it should be strong when is it coming as week

### 00:16:10 · Speaker 2

only one more one to two more minutes we have to go to other sections as well see if you can

### 00:16:19 · Speaker 2

Given a different argument, and see, like, for example, can give all small letters and see what is happening.

### 00:16:30 · Speaker 3

Uh we need to save it for later

### 00:16:32 · Speaker 2

Yeah yeah some should re render but yeah you can deflections all small also coming as weak

### 00:16:38 · Speaker 2

If you wish to like log whatever is in line number 11 the code can try logging to get some idea

### 00:16:44 · Speaker 3

It's a little dot clock

### 00:16:50 · Speaker 3

Yeah I think it will come as

### 00:16:51 · Speaker 2

is coming as one one five

### 00:16:54 · Speaker 2

Because you're you're passing SSS

### 00:16:59 · Speaker 2

I think Patrice will be there too

### 00:16:59 · Speaker 3

Very positive

### 00:17:00 · Speaker 2

to try pass different string in line number uh instead of yes yes you pass something else and see whether you're getting different values or not then not the same like different characters like one small one capital one number

### 00:17:13 · Speaker 3

Okay I want to see one

### 00:17:17 · Speaker 3

Six seven ninety nine yes

### 00:17:19 · Speaker 2

What's a number two what's a number

### 00:17:25 · Speaker 1

That's for the question

### 00:17:25 · Speaker 2

Okay

### 00:17:27 · Speaker 3

Yeah four is different

### 00:17:28 · Speaker 2

So that is a problem correct maybe after the interview you can check this Vinod Shvishal okay

### 00:17:33 · Speaker 3

Okay

### 00:17:34 · Speaker 2

Now let's let me ask you some questions about about the react can you go to the same snippet again? Hold left yeah so we have a use effect in line number 50 25

### 00:17:44 · Speaker 3

Mm

### 00:17:45 · Speaker 2

The end of the day is what it's a function

### 00:17:49 · Speaker 3

Last couple of functions

### 00:17:50 · Speaker 2

Yeah have we ever given a thought what does useEffect return as it's a function to return something correct what does it return

### 00:17:56 · Speaker 3

function I don't think useEffect returns something as so as per I as of my knowledge

### 00:18:03 · Speaker 2

So then it's like something like undefined or null

### 00:18:05 · Speaker 3

Uh it will be undefended

### 00:18:06 · Speaker 2

Okay tell me the difference between undefined and null

### 00:18:09 · Speaker 3

Undefined is like it's no it's no value because if we like declare a declare a variable and we don't give any value the value will be like undefined by default null we can set like an initial value for like not giving it empty

### 00:18:25 · Speaker 2

So you are saying null is something of value to represent nothing, correct? Undefined is when you have not defined anything. That's the difference, Vishal.

### 00:18:37 · Speaker 2

So let me share a snippet with you. Okay, copy the snippet. I'll put it in the chat section. Copy the snippet. And I mean, you can replace your code with this code. Okay, I don't have to run the run it. Just copy paste. And so that first, I want you to go to the code and guess the output basically. Okay, if audience answer, if you wish, you can pause the video for a while, go to the code. If you know the answer, you can mention question number two and your answer in the comment section. Okay.

### 00:18:55 · Speaker 1

audience

### 00:19:03 · Speaker 3

I don't think uh you need

### 00:19:06 · Speaker 3

The zero will be count because this is an async thing and it won't before that we have a synchronous like section here and in this synchronous section we are clearing that thing

### 00:19:20 · Speaker 2

Okay, as you told like you're just starting with React, I'll give you some context. In line number eight, whatever the return that we are doing, right, that would execute on the component unmounted. Like, for example, you're on page A, you're going to page B. Whenever the transition happened, right, that return will be executed. So it's not gonna execute as long as when you are in screen A, okay? So I'm giving you that hint. Now if you wish to like re-guess your answer, you can tell me.

### 00:19:42 · Speaker 3

The third turn is not going to run before we are changing to our next

### 00:19:45 · Speaker 2

So you can assume that throughout the execution of this file it's not gonna be called basically. Okay.

### 00:19:51 · Speaker 3

Okay then uh

### 00:19:54 · Speaker 3

randomly it will for for thousand sec thousand milliseconds randomly it will change to one and minus one based on the returned value okay previous code okay okay not not ps hybrid sequence ps count we are adding it so randomly it will add to zero like one and minus one randomly

### 00:20:13 · Speaker 2

Correct. What are you saying is correct Vishal. So basically it's hard to predict what does the output, but output will be keep changing basically correct. Yes. Because the value of count is zero initially and we would come inside the set interval.

### 00:20:20 · Speaker 3

Yes

### 00:20:25 · Speaker 2

Every time

### 00:20:25 · Speaker 3

Do you mind if I

### 00:20:26 · Speaker 2

the previous count value you have you're adding the previous count plus whatever the random value that is generated correct if it is greater than 0.5 you're going to add 1 otherwise you're going to subtract 1 but there is a catch

### 00:20:38 · Speaker 2

There's a catch here

### 00:20:38 · Speaker 3

There's a catch you

### 00:20:40 · Speaker 2

see let's say the initially the count was zero you set it as like zero plus let's say let's assume it was greater than one greater than so zero plus one so it became one

### 00:20:52 · Speaker 2

So where the value of count became one. So next time, what will be the value of count? It's gonna be one or zero.

### 00:21:02 · Speaker 3

It will be one it will be available in this previous count uh callback because yeah they're using as callback right

### 00:21:07 · Speaker 2

Correct, correct, correct, Vishal. So that's the right answer. I'm done from my end, Vishal. We are reaching the last four minutes of the interview. You can stop sharing.

### 00:21:16 · Speaker 2

Let me give my feedback to you and audience whoever has watched the video so far. Okay, I'm hoping you enjoyed it so far. And if you enjoyed, please like and comment whatever you felt honestly. And if you solved the problem, like whatever Vishal did maybe before to Vishal, that also you can mention. Mostly Vishal has given approximately right answers to all. The password checker that could have been improved a bit, but that answer solution you can get somewhere online as well. So I'm not gonna explain anything that Vishal has given or all that's it. Now, my feedback to you Vishal, I've noted on a couple of feedbacks. Let's start with them.

### 00:21:46 · Speaker 2

machine coding thing this is to you and everyone almost 90% of people that I take machine coding problem I ask machine coding problem do the mistake where the approach is not finalized in their mind itself you're getting my point right see whenever you're solving this is applies to machine coding also whenever you're doing your day-to-day coding so first you be firm like your mind is the first computer then it is actually whatever you're typing correct the I'm not saying like 100% will be able to do but largely first have a solid approach in your mind

### 00:22:16 · Speaker 2

then you start implementing okay and with that you will be able to solve the problem quickly the coding can happen in two minutes you might end up spending like around remaining eight minutes about thinking towards it so you can do that second it every when it happens some syntax are unknown so we have to search on the online nothing wrong with that also but be clear have a concise list of everything that you want to search like for example four things i don't know four things i'll search it cannot shouldn't happen like you do to and fro like you start coding again

### 00:22:46 · Speaker 2

like something i don't know again you go and search it's not a day to day coding it's an interview so try to have that list of things that you want to search and ask the interview these are things that i don't know some interview will be willing to help you only there you don't have even had to search they'll only tell which function will give you that if you don't know and some they'll allow you to search so do it for once and come back and continue the coding okay and other thing uh this scenario driven question that i asked the google calculator right it's not a very straightforward question it's not a very hard question also the the

### 00:23:16 · Speaker 2

suggestion to you and audience who are watching is you are a front-end developer don't look at the front-end systems like a user look at the front-end system like a developer like for example you are watching my video on youtube tomorrow if you have to implement this you'll not be able to know 100 how to build it but some degree you should know like what are the things that you are going to use to build this okay look at a system like a developer going forward that's the right way to learn the front-end system design where whenever you have a doubt you keep searching and you start consolidating getting more and more information okay

### 00:23:46 · Speaker 2

These are the feedback that I feel Vishal. I feel like as you still started learning the React and you want to transition to React roles, there is definitely some scope where you can master the React. I feel like it's not like 100% you are there yet. Spend some more time mastering the React and then you would be good to give the interview Vishal. How was the interview experience otherwise Vishal?

### 00:24:05 · Speaker 3

Yeah it is wonderful

### 00:24:07 · Speaker 2

Thank you

### 00:24:07 · Speaker 3

Your hands

### 00:24:08 · Speaker 2

Wonderful. Thank you so much Vishal. I'm thinking in the audience who have watched the video, you also liked the video. If you liked the video, please like it. Subscribe to my channel. Carry on. See you in the next video. Thank you so much.

