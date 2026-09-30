---
id: -C_-f5aiWIY
title: 🔥 6 most confusing questions with console.log and unary operator 🔥 (Hot topic
  for interview)
date: '2022-07-24'
url: https://www.youtube.com/watch?v=-C_-f5aiWIY
description: "Join Uncommon Geeks community to discuss with other developers: t.me/uncommongeek.\
  \ Unary Plus Operator: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_plus\n\
  \nUnary Minus Operator:  https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation\n\
  \nOperator Precedence: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence\n\
  \nGithub Repository with questions discussed: https://github.com/coolvasanth/FrontEnd_interview_questions_with_javascript/blob/main/Common%20JavaScript%20Interview%20Question/consolelog.js\n\
  \nMedium Blog: https://mevasanth.medium.com/ \n\nFollow me on LinkedIn -https://www.linkedin.com/in/vasanth-bhat-4180909b/\n\
  \nJavaScript Custom implementation Series: https://www.youtube.com/watch?v=eGzErMUfdpk&list=PLmcRO0ZwQv4RWqjZCajaKBAdCJjmkAL_I\
  \ \n\nMAANG series for frontEnd Developer: https://www.youtube.com/watch?v=s-b-txm_Gvk&list=PLmcRO0ZwQv4SNhbW4CI4vc-6IHBHCKzZN\
  \ \n\nInterview Preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t"
author: careerwithvasanth
duration: 00:12:14
model: saaras:v3
transcript: true
---

# 🔥 6 most confusing questions with console.log and unary operator 🔥 (Hot topic for interview)

## Transcript

### 00:00:00 · Speaker 1

Hello all, welcome back to Uncommon Geeks. Myself, Fasant. I hope you all doing well. In case if you are seeing me for the first time on the internet, I'm a content creator. I help people to clear their interviews. I made a lot of beautiful series in the past which has been appreciated by many. I'll try to link all those things in the description, if possible also on the screen. Please watch the videos. So in case if you are a front end developer who looking out for a job change, I will guarantee you, if you watch all my series including this video, definitely you will have a seventy to eighty percent of a chance to clear most of the your interview rounds, okay? Now without wasting further time, Let's get started with the video content

### 00:00:37 · Speaker 1

I believe all of you have seen the thumbnail and you got already confused about what is happening with the console.log and what are all the different operation, what output we'll be expecting, okay? Now, let us take it like this where I'll confuse you more, even more and I'll get rid of all your confusion and take get reveal all the things that is happening under the hood step by step, okay?

### 00:00:59 · Speaker 0

Now

### 00:01:00 · Speaker 1

So, what we are doing here is let us first show you let me first show you the output. From that point itself we'll start. Okay? So where I'm running the output, okay? So where for the first one it is one thirty two, for the last one is N I N, this is N I N, uh then there is also two. And for this it is thirty two and for this it is zero two, for this is one one two, okay? I think now you might have again the confusion might have increased further how it is one twenty two or how it is thirty two, how it is N I N and two. All the

### 00:01:30 · Speaker 1

I'm going to explain this video very much in detail, so please watch the video till the end. This is one of the very, very important interview topic. So these are the tricky questions that are generally asked just to check how depth your knowledge is of a particular JavaScript concepts, okay? So please watch the video till the end, and if you're not subscribed to my channel Uncommon Geeks, please subscribe and continue watching. Like I mentioned, you'll definitely don't regret. A lot of my videos will help you to clear your interview. Now, let's start with some simple things, okay?

### 00:01:56 · Speaker 1

Generally with with my experience of looking at the lot of tutorials when learning a language most of the people what they do they learn few things and they immediately start coding okay lot of operations we won't focus like unity operators precedence and all these things. So if whenever you don't know these things these questions become quite tricky for you. Let me show you a simple example. Okay. So I'm putting a console dot log where I'm doing a plus b plus.

### 00:02:20 · Speaker 1

See

### 00:02:21 · Speaker 1

If you know the answer, please mention in the comment section and try to mention A B plus C and mention whatever you have got. If not, let us continue watching. This is very simple. I think most will be able to guess. A B plus C is A B C, right? Let me run the code. A B plus C is A B C, correct? So it is not a numerical addition, it is a string concatenation, correct? Let me make another small thing. A B

### 00:02:45 · Speaker 1

Minus B

### 00:02:47 · Speaker 1

Now what is the output? First I think most will be able to guess. Try to guess the output for the second one, A B minus B. Correct? What is the output? In case if you know, I think you are one among that among the people who are preparing for the interview who are very serious, okay? Please mention that in comment section and mention your answer. Definitely I'll try to like and comment about your the your whatever

### 00:03:05 · Speaker 0

comment

### 00:03:06 · Speaker 1

See, the answer for this is A B minus B is not A. Very first to tell, okay? So A B minus B is A B plus B was possible because it first it tries for a number, if both are not numbers, it will try to do a string concatenation, correct? So first one was right. Second is a negation or negative operation, A B minus B. A B minus B will not give you B. It is trying to subtract two non integer numbers, correct? Or non integer or basically non number

### 00:03:36 · Speaker 1

numbers A B minus B. So what you get is output as not a number N A N, okay? And if you don't know what is N A N, let me know in comment section, I'll try to make a detail video. That is one of important topic for interview. In simple words N A N stands for not a number, okay? So A B minus B is not a number. Points are clear to you. Next.

### 00:03:55 · Speaker 1

Let's talk a little bit about the precedence. Okay?

### 00:03:57 · Speaker 1

Let's say, I think all of you have studied this in your your school days itself, correct? So now what is the output? See, there is a rule for processing this. It is not one plus two is three, three into four is twelve, correct? This multiplication operation has higher priority than addition operation. So first two plus four, even though you write it like this, what happens is this. First it is two plus four, four twos are eight, eight plus one is nine, correct? So this output will be nine, correct? So this is the order. Let's say you have a plus

### 00:04:27 · Speaker 1

on both the sides there is no star plus on both the sides then what is the order of processing so you know the BODMAS rule where brackets then there is all the things I'm not fully sure so but basically what is here is there is a rule for processing correct so if you go and see here in the documentation there is something called operator presidency I'll try to link this in the description okay this is I've taken it from developer.mozilla.org okay so here he clearly specifies what is the operator presidency in JavaScript

### 00:04:57 · Speaker 1

script. Okay? So like it is same as a BODMAS where the whenever the precedence is same the processing from left to right but there are some operators with the precedence is from right to left for example the equality operator. So they have clearly mentioned that here. So A B is equal to five then it is a right to left processing. So five is first initialized to B then that same five is again initialized to A. Okay? Most other operations are right to left precedence. So sorry left to right precedence. So two plus three plus four, two plus three is added then three plus four is added. Correct?

### 00:05:27 · Speaker 1

precedence for a normal operations, um I mean with the same operations, the priority is almost of the operator, the priority is from left to right, okay?

### 00:05:38 · Speaker 1

This is something that you want to know to answer. So I'm just trying to decode all the points which you should know to answer this. Next we have something called unary operators, correct? So unary operator if you see, uh this is not addition, don't confuse addition and unary operator, okay? The addition and subtraction are different, unary operators are different. So in here if you see, uh so I'm just trying to log. So this was plus one, if you first it is very important to look at the definition. The unary plus precedes its operand and it evaluates its operand but at

### 00:06:08 · Speaker 1

seems to convert into number if it is already. So let's say you have a string one, okay? And that can be potentially converted into a number. See, string one can be converted into number. String hello world cannot be converted into number. So it will try to convert those things which can be acted like a number, okay? So other than that they just add the sign. For example, now one was there plus one is similar as one, correct? So there is a plus y, plus and minus is minus, correct? Minus and I mean into you already know that basic mathematical

### 00:06:38 · Speaker 1

operation. So if it is a minus and minus then it will become plus, correct? So here it is minus one because y is minus one and we are trying to log plus into minus which is minus again a minus y, correct? And we are trying to log plus true and plus false, we are getting some values like zero and one here. And plus hello, we are getting the zero. It's very very important and confusing, so please read this documentation more in depth. Okay, I'm going to stick to my examples, I'm not going and explaining everything, okay? This is about a unary plus operator.

### 00:07:06 · Speaker 1

And there is similarly unary negation operator, unary negation or negative you can call. The unary negation operator precedes its operand and negates it. So as you see it is a plus four and they are trying to log okay minus of an x. So which is minus four because four here minus four and same it has been printed here which is minus four definitely. So in case if you are not doing this it should be plus four. Correct? It is a plus four. Or here you have a minus x. I think here also if you make a

### 00:07:36 · Speaker 1

minus y, minus into minus it should become plus, correct? plus four. Very simple, if you know basic math it's very simple. The purpose I'm showing this is many would have not learned this very much in detail in the interview. Now, whenever you are preparing for the interview or whenever you are learning the concept, okay? Now, let's go back to question, let's try to decode all the problems one by one, okay? So step by step, only one by one I'll uncomment, let's try to guess. Now, so one plus two plus two we need to add, correct? There is a plus operator now.

### 00:08:04 · Speaker 1

So plus operator now you know the priority that is left to right precedence first we should be trying to do one plus two. Can we add one plus two a numerical addition? Definitely not possible. It one is string and another is number so it's a string plus number concatenation. Correct? So it will become one two as a string. Very first. Correct? One two as a string. Then one two as a string plus two as a string what it will become? It will become

### 00:08:31 · Speaker 1

one two two. Same I think output you have saw, okay? Let me run that and show again to you. one two two. Correct? So now you are able to decode this. Let's go to next question which is slightly trickier.

### 00:08:43 · Speaker 1

So, what is here? So here also we have one two two, it is one two two, correct? Which is very easy. But this is something very important one which I want to highlight. Many candidates don't observe the question carefully, okay? I mean, I also make this mistake, but please observe the question carefully, don't look at it at any prejudice, like similar to this and this. See here there is a plus.

### 00:09:04 · Speaker 1

many will not read this plus at all and they'll give a wrong answer. So we already saw whenever there is a plus and a number that can be potentially convert a string that can be potentially convert to number it will try to convert it to number. So it will become one plus

### 00:09:17 · Speaker 1

one plus two which is three. A numerical three, okay? Then, then what will happen? Numerical three plus string two. So this will become thirty two. Correct? Very easy. Now let me run the code and show it to you. Thirty two. Correct? So now let us go to the third one. I think you will be now on you will be able to answer more confidently. So this is one and a minus one which is one and minus one is

### 00:09:42 · Speaker 1

one and minus one is zero. Correct? And zero plus string two is zero two. Correct? Let me run this code for you again. Zero two. Correct? Now, let's go to the next question.

### 00:09:57 · Speaker 1

So here if you have plus one, one and two. So plus one is again one numerical one, correct? Numerical one plus string one which is equals to one and one in a form of string, correct? And that plus two should give you one one two in the form of string, correct? Let's see if I'm wrong in case.

### 00:10:16 · Speaker 1

No, it is right. Okay. Now, we'll come to another again small variation of this. So we are doing A minus B, correct? A minus B plus two.

### 00:10:27 · Speaker 1

You know A minus B is N I N not a number, correct? So A minus B is not a number. Not a number plus string two. What it will give? It is trying to concatenate both again, not a number and two in the form of string, okay? If I run the code, see I'll see not a number and two. In case of this, there is a difference between above and this, okay? So what we are doing there and what we did here? There it was a string concatenation which was possible. A number a data type

### 00:10:57 · Speaker 1

is not a number and a string can be concatenated to form a string. But here, a minus b is not a number, we are trying to add a not a number to a number. How we can add it? Number and not a number cannot be added, so you will get just a not a number.

### 00:11:11 · Speaker 1

not a number, trying to add it to not a number will give you not a number. Okay? And then very very easy, okay? So very very easy because you now you know all the concepts. Now any question like this asked in the interview, you know the precedence, you know about unary operator, you know about negation operator, you'll be able to nail these questions. In case if you like this video, please like this on my YouTube channel and add any comment. Let's say you like the video, add in comment. Let's say you want me to improvise something, please mention that in comment section. If you like my videos more and more, it will appear for more and more people.

### 00:11:41 · Speaker 1

a lot of people when they start clicking on the video it will again appear for more people and my channel become popular. I have a noble cause of helping lot of candidates to clear their interview by liking and commenting you help my cause. So please do help and if you're not subscribed to my channel please subscribe. I'll put this question in my github and I'll also link that link in the description. You can get the question and practice try to make some variation of your own and try to practice that. Also read my medium articles I'll try to write a article on that and link that in the description. Please read my link medium blog also and try to follow me on meetings. Thank you so much for watching, catch you in next video.
