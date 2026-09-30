---
id: uaYnUiyCWII
title: 🔥Function currying and Non currying same function? can you write a code for
  it (Fun currying Ep - 2)
date: '2022-03-19'
url: https://www.youtube.com/watch?v=uaYnUiyCWII
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Function currying is a sub-topic of function, to be specific extension of function\
  \ nesting. Currying as a topic has good weightage  when it comes to interview. Calling\
  \ a function infinite times and using same function to implement both currying and\
  \ normal implementations are common questions asked in the interview. \n\n\nFunction\
  \ currying Part 1: https://youtu.be/YEtlLh5KsAo\nCounter Dilemma Closure: https://www.youtube.com/watch?v=nJhQRotbIis\n\
  Questions on closures Part 1: https://youtu.be/pycV_CSoj1g\nQuestions on closures\
  \ Part 2: https://youtu.be/j4KRg0RBY5Q\nMy Medium Blogs - https://mevasanth.medium.com/\
  \ \nGithub URL which contains questions - https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript\n\
  \ Follow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/"
author: careerwithvasanth
duration: 00:12:10
model: saaras:v3
transcript: true
---

# 🔥Function currying and Non currying same function? can you write a code for it (Fun currying Ep - 2)

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome to Uncommon Geeks. Myself Prasannath. I hope you all doing well. So it's a part two of my video on function currying. So in the part one I had explained what is function currying, how it can be used in JavaScript. So in this video I'll be discussing some questions that are generally asked in the interview on function currying.

### 00:00:15 · Speaker 1

So, if you have not watched my previous video and directly land on this video, I highly recommend please go ahead and watch that video so that you have an fair understanding about function carrying, then then you'll be able to answer the questions asked in this video very thoroughly, okay? So without wasting further time, let's get started. The question is very straightforward, okay? So what you have to do is

### 00:00:37 · Speaker 1

So you have to write a function called add which basically uh takes two arguments in this way and gives a sum. You already know how to do this in my previous video.

### 00:00:47 · Speaker 1

the tricky part is the same question basically should behave the second way as well. So it should take argument in a like a normal function call and it should return the sum. Okay. Looks easy at the beginning but unless you know the property of closure and normal function and little in depth of JavaScript you will definitely will not be able to answer this question. This is a question that which was asked to me in my current company and unfortunately I was not able to answer fully at that at that time. Okay so I picked this so that

### 00:01:17 · Speaker 1

all of you whomsoever get this question in the interview you should be able to answer it and clear that interview. Okay? So, uh so whenever this question asked for you in the interview let me tell you how you approach it. So you have now a function uh add that takes two arguments ten and twenty in a closure manner. And another function which same function basically should also take the arguments in a normal function manner which where there is no closure. Okay? So the important thing to observe here is uh Let's say you now you think something can be written and you start adding a function. So function add

### 00:01:53 · Speaker 1

and what you will write here. What parameter you will take. So as soon as we encounter this line right which parameter you take there itself you will be stuck if you are solving it for the first time. Correct. And if you are not sure of different aspects of JavaScript. So and from here I will guarantee you will not go anywhere. You will be just stuck here itself to I mean what parameter to pass and what this takes you will never be able to solve this question. So thought process has to be changed this way. So where

### 00:02:22 · Speaker 1

we have two arguments here, and we have one argument in the first function call.

### 00:02:27 · Speaker 1

So, and we should have a two block inside the add function which where one block handles the closure kind of function calls and another block handles the normal function call. So now you got some some lights in your brain. Two things. One block handles the closure, another block handles the normal function. So there has to be check.

### 00:02:50 · Speaker 1

Correct, there should be a check to differentiate between the both. So which is a check? Argument is a check. Correct? So JavaScript has a property called arguments.

### 00:03:02 · Speaker 1

So if I run this, uh

### 00:03:06 · Speaker 1

add function

### 00:03:08 · Speaker 1

basically it should take an argument so let us simply write x. let's see what happens.

### 00:03:16 · Speaker 1

man. For the this one right the function carrying

### 00:03:20 · Speaker 1

expect a function in a function because it is triggering right one inside another basically this

### 00:03:27 · Speaker 1

ten and then it want to trigger twenty. So it wants an expecting an inner function. So if I return that what's happening let's see. In the first case argument is ten. In the second case argument is ten comma twenty. Okay. See there are many ways there could be many ways to solve this question. I am picking the approach of arguments and solving it. Okay. So if you know some better approach feel free to solve that I mean write that in the comment section and tag me. If that is something that I think is performantly performance oriented also is good approach.

### 00:03:57 · Speaker 1

then definitely I'll give a thumbs up to that. If not, you can follow this approach whatever I'm writing. Okay? So now, you know arguments in first case is ten and second case is twenty. So we can keep a check where if arguments dot length, so if it is greater than one, then behave like a normal function. If it is less than one, then behave like a closure. So what I do now is, so here I'll write return x plus y is something for the closure. Okay?

### 00:04:25 · Speaker 1

And then what I'll do here is if

### 00:04:29 · Speaker 1

argument arguments.length greater than one okay? Then I'll go to one block else I'll go to this block I already know correct?

### 00:04:40 · Speaker 1

else I'll go to this block. So otherwise I'll be in the if block, correct? So inside the if block, what I do is I have to run the loop, correct? Because that could be any number of arguments, it cannot be just ten and twenty, that could be thirty, forty, fifty, correct? So till which I'll run the loop till arguments.length, okay? Then what I do is, con, no no, let sum is equals to zero and what I do here is sum plus is equals to sum plus arguments of I and you will return the sum here.

### 00:05:19 · Speaker 1

Hope you understood what I did. What I did is in line number three I created a variable called let sum which actually points to default value of zero. And I'm running the loop till the arguments length. And inside which I'm summing the entire whatever the arguments are there that I'm adding them, okay. I don't go too depth where I haven't kept an integer check what will happen if I pass a string here. So those are the things that you do for your project. For this purpose I know only these are the things that I'm calling. So due to which I haven't kept lot of checks. And what if let sum is equal to zero and this block

### 00:05:49 · Speaker 1

fails and you it will become something undefined or not a number or zero is returned. So those are the checks that you do in a project. So this is an interview. So where I know the input, so due to which I'm just ticking into the inputs and and I'm writing the code. Okay.

### 00:06:03 · Speaker 1

So I'm running the loop till the end of this length, then I am adding it and I'm returning. If it's otherwise, which is a closure, then I'm going here. Let me log both and see whether the expected output we are getting or not. Okay?

### 00:06:17 · Speaker 1

add ten comma twenty here

### 00:06:21 · Speaker 1

and this inside this.

### 00:06:25 · Speaker 1

So the first one is actually without closure. Am I right? uh No, this is with closure.

### 00:06:34 · Speaker 1

So second one is without closure. Second one is

### 00:06:39 · Speaker 1

without closure. Okay, let me run this and see what we are getting.

### 00:06:45 · Speaker 1

So, yeah.

### 00:06:49 · Speaker 1

Yes. So what we are getting is with closure we are getting ten plus twenty as thirty. Without closure ten comma twenty we are getting as forty. So we are doing some small mistake here. So due to which uh what is happening is we are getting forty. Ideally ten plus twenty is also a thirty. Correct? So let us see. uh Frankly even I haven't practiced this and come. The reason being if I practice and come I do not do make any mistake so that you will not be able to find out what mistakes are commonly made. So you made this mistake in the interview.

### 00:07:19 · Speaker 1

okay? But the expectation was thirty but you are printing forty. So how you debug it? So the one way is first check. So here arguments is greater than length greater than length one. So it is ten and twenty coming to this block. Sum is initialized to zero. I is equal to zero I less than arguments dot length, okay? First probably you can start this debugging process by printing the arguments in this block, okay? So log the arguments. See and very important thing do not keep logging because

### 00:07:49 · Speaker 1

the more your time you log, the interviewer starts thinking you're not confident about whatever you are doing, okay? So keep it very minimal, but in this case at least you need to know what arguments are coming to identify the sum whatever is coming is right or wrong, okay?

### 00:08:02 · Speaker 1

I'll do it. So what I'm getting is uh

### 00:08:06 · Speaker 1

arguments is coming zero and one which is ten comma twenty. Okay? So which is correct? So sum is zero in the first place, okay? Then I is equal to zero I less than arguments dot length and I plus plus. So arguments of zero which is ten and arguments of one which is twenty. So twenty plus ten should ideally become thirty, okay? So what is happening we have to check maybe a little further, dig down and see here as well, okay?

### 00:08:36 · Speaker 1

arguments of zero. So sum is equal to sum. Okay. So what what mistake I did is very silly mistake. Either you should do sum is equal to sum plus arguments of I or you should do sum like this sum plus

### 00:08:52 · Speaker 1

argument of I. Correct? I mixed both, that is a mistake. So good that I hadn't I did not practice and I was able to show you the small mistake which I made. Some interviewers will be very kind enough and they'll tell this is the mistake you did because when most of you are watching this video might also have noticed it. But whenever we are writing the code, we miss out those small small items, okay? So I had missed it and now let me execute and see.

### 00:09:15 · Speaker 1

So both we are getting thirty. So with closure is also thirty, without closure is also thirty. You also saw a common mistake that can be made in the interview, but there is no limit to it as you know, you will not make a mistake which I did, some or the other mistake you did, you do. But only advice of mine is do not get panic. See step by step, okay, like I said keep a minimal locks, the more locks then the interview think you are not confident, then start observing till where it is working fine from where it is failing, then you will be able to identify the root cause and and execute. See interview

### 00:09:45 · Speaker 1

if if you're not trying for mang or fang, interviewer will not bother the how many runs you generally do or small mistake that was made in the beginning and you corrected later. These are all the good qualities of a programmer. None of us will be able to write a fully working code at the one stretch, correct? So one or two iterations interviewer will not mind. Mang companies they will they do mind, but normal companies will not mind. So be take your freedom and while writing itself run the code in your mind what is happening, okay? So that you will not make a silly mistake like I did.

### 00:10:15 · Speaker 1

What about this question, the question number one? Where a same function that takes both function carrying and a normal function, okay? There is another question which generally with the help of recursion you have to solve this that is like this. Add ten comma

### 00:10:30 · Speaker 1

ten, twenty, thirty goes on basically, okay? twenty, thirty, any number of any any any number of times you can do it, followed by a empty bracket, okay? This has become again a very common question which is asked in the interview where a simple currying function, simple function currying that takes infinite number of arguments, okay? So basically you have to use a recursion to solve this. I have written this beautifully in

### 00:11:00 · Speaker 1

medium vlog, a step by step what is currying and how to solve this problem. So I'm not going to re-explain that in my video. I would highly advise that medium link whichever is in the description, please go ahead and read there. Very step by step, the entire code is also there, you can copy and paste it on your favorite editor and practice, okay? These are the two questions which I wanted to cover in function currying. Others are, I haven't seen any other complicated question asked in this topic. And if you are aware of the argument concept and the closure, you should be good enough to answer all the currying questions.

### 00:11:30 · Speaker 1

Okay? If you if you have some question that is in your mind and you are not able to answer, please do mention that in comment section. I'll try to make a video on it. So thank you so much for watching. If you like my video, please do like it on my YouTube channel and share it with your friends if you want them also to get benefited. Do not forget to subscribe to Uncommon Geeks. Please, please, please, please subscribe to my channel Uncommon Geeks. And if you want me to make a video on any particular topic, please do mention that in comment section. I'll try to make a video on that topic. So and my GitHub URL is also there in this description. Go go to my

### 00:12:00 · Speaker 1

GitHub project, download the project to practice all the questions. Give me a star for that project in in GitHub to do follow me on GitHub as well. Thank you again for watching. Catch you in next video.
