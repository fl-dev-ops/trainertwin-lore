---
id: dNJsaX0C1fg
title: Lec1 - Deep Generative Models Intro to Probability theory 1
date: '2024-11-23'
url: https://www.youtube.com/watch?v=dNJsaX0C1fg
description: ''
author: prathoshap5226
duration: 03:07:23
model: saaras:v3
transcript: true
---

# Lec1 - Deep Generative Models Intro to Probability theory 1

## Transcript

### 00:00:02 · Speaker 5

Yeah, a couple of logistic things. The registration deadline is done, right?

### 00:00:11 · Speaker 0

No sir, it extended till twenty.

### 00:00:11 · Speaker 3

extended till

### 00:00:12 · Speaker 1

Twenty

### 00:00:13 · Speaker 3

extended

### 00:00:14 · Speaker 0

सो यू मे हिट अ सेंचुरी सर

### 00:00:14 · Speaker 5

Oh my god

### 00:00:15 · Speaker 2

E

### 00:00:18 · Speaker 5

I don't want that

### 00:00:22 · Speaker 5

Okay, so we still have classes not yet

### 00:00:28 · Speaker 5

stabilized that way. Okay.

### 00:00:32 · Speaker 5

Okay

### 00:00:39 · Speaker 5

Okay anyway let's get started. So here is the plan for today.

### 00:00:44 · Speaker 2

Hmm

### 00:00:46 · Speaker 5

I'll start from some basics of probability theory.

### 00:00:51 · Speaker 5

request is all of you please mute. Unless you have a question or something even when you have a question uh since it's a very large class let's maintain some sort of a decorum please uh raise your hands of course virtually call out your name and then we will uh discuss.

### 00:01:11 · Speaker 5

So

### 00:01:15 · Speaker 5

Please ask me questions otherwise you know it's it will become a very very boring monologue. First of all virtual classes are boring because I don't get to see students faces. On top of it if you don't talk it will be double boring so. We what I'll do is after like every fifteen minutes or so right when I finish one particular concept I'll stop and ask for questions please if you have any questions you can ask me. Even

### 00:01:46 · Speaker 5

in the middle you can you know feel free to just raise your hand so that I can stop and ask address your questions.

### 00:01:53 · Speaker 6

So

### 00:01:55 · Speaker 5

Okay, I hope that you have gotten access to my course notes and that feedback form that's out there and all that, right? So, all the logistic issues are sorted out, I suppose. No, no further questions there, I think.

### 00:02:11 · Speaker 3

Pink

### 00:02:13 · Speaker 3

teams

### 00:02:28 · Speaker 3

Okay

### 00:02:40 · Speaker 3

will not

### 00:02:44 · Speaker 3

acromatize with this one more thing. So

### 00:02:46 · Speaker 5

struggling just a second now. So where do I go to that class notebook? Okay, got it.

### 00:02:54 · Speaker 5

वेलकम टू वन मोड्स, ओके

### 00:02:57 · Speaker 5

but

### 00:02:58 · Speaker 2

you're not sharing this

### 00:03:00 · Speaker 5

read only to edit tab d

### 00:03:02 · Speaker 3

one note icon, various one note icon here, this one.

### 00:03:06 · Speaker 3

No, so not

### 00:03:15 · Speaker 3

Okay, if I share you can help me perhaps.

### 00:03:22 · Speaker 6

will be on the top right sir.

### 00:03:24 · Speaker 2

let me just see. I'm using the good notes.

### 00:03:26 · Speaker 6

Good notes

### 00:03:28 · Speaker 2

share screen, share start broadcast.

### 00:03:37 · Speaker 3

It's visible now, sir.

### 00:03:39 · Speaker 2

Uh huh

### 00:03:40 · Speaker 5

Hello

### 00:03:43 · Speaker 5

Where is it? To edit tap one note icon. On the top right. Oh this one.

### 00:03:46 · Speaker 6

on the top right.

### 00:03:48 · Speaker 6

top right just

### 00:03:48 · Speaker 5

I see, I see, I see, got it. Okay, great, thank you. So, okay.

### 00:03:59 · Speaker 5

So shall we have like one different page for every day? I think let's do it that way.

### 00:04:07 · Speaker 6

Yes, that will be better.

### 00:04:10 · Speaker 5

the date will always be here I suppose right I mean it will be Saturday August tenth it is so we'll have to delete this. So do I delete this?

### 00:04:21 · Speaker 3

Great

### 00:04:24 · Speaker 3

cut

### 00:04:26 · Speaker 3

this maybe we will rename this as

### 00:04:35 · Speaker 3

Hmm

### 00:04:39 · Speaker 3

Okay

### 00:04:39 · Speaker 2

Sir, within the

### 00:04:40 · Speaker 6

सर विदिन द फाइल इटसेल्फ जस्ट मेंशन द नेम ऑफ दिस पेज।

### 00:04:45 · Speaker 2

where

### 00:04:45 · Speaker 5

where

### 00:04:45 · Speaker 2

care

### 00:04:46 · Speaker 5

on top

### 00:04:46 · Speaker 6

on top. Saturday, Saturday ten, just above that mention this page title.

### 00:04:46 · Speaker 1

the title

### 00:04:47 · Speaker 2

Okay

### 00:04:51 · Speaker 5

So, two OCR

### 00:04:53 · Speaker 6

No. Oh yeah, yeah, I think it does.

### 00:04:54 · Speaker 5

Yeah, yeah.

### 00:04:58 · Speaker 2

place my, so both will

### 00:04:59 · Speaker 6

Sir both will work. Both will work keyboard and OCR both.

### 00:05:09 · Speaker 2

Hello

### 00:05:11 · Speaker 2

Yeah

### 00:05:12 · Speaker 5

Yeah, I need two, three minutes for this concept to get charged. Anyway, so I'll write that. So today's agenda is the following. I'll start with the basics of probability theory, the the probability theory that we would need to continue in this course.

### 00:05:31 · Speaker 5

the first half. The second half will introduce you to the

### 00:05:37 · Speaker 7

generative models and

### 00:05:39 · Speaker 5

formulate it if possible.

### 00:05:42 · Speaker 5

So that is the agenda. Okay. So now the fundamental question uh that is to be asked is right you know that all of most of the machine learning that are all of machine learning uh is is based on this branch of mathematics called probability theory, right? Now the

### 00:06:02 · Speaker 5

Question is why do we need? It's actually a new paradigm. I mean, new meaning it's a, see when you, when we start as, when we start studying mathematics, right? We have

### 00:06:14 · Speaker 5

We have numbers, we have counting and you know we gradually learn calculus. So if you think about it historically what was the need for calculus is calculus had to be developed because you know this idea of

### 00:06:32 · Speaker 5

rate of change of things and the idea of uh calculating the area under an arbitrary curve, right? That had to be uh that was important, you know, for instance, people like Newton, they wanted to find out what was the total distance covered by a moving body, uh whose uh speed or velocity is plotted as a function of time. Now, there was no tool that time, okay, that could deal with uh such kind of question.

### 00:07:02 · Speaker 5

So he invented a new set of tools, right, which became a branch of mathematics called calculus, which was developed subsequently. So similarly

### 00:07:15 · Speaker 5

probability theory, right? Statisticians had this had this question from a long time. The fundamental question is, all machine learning is is studied, right? Or rather modeled from a probability theory perspective. Question is,

### 00:07:33 · Speaker 5

See, it is not a force fit in the sense that people don't or rather people didn't come up with probability theory or rather apply probability theory because it was there. It was not that. The idea is that you cannot answer a few questions that you often encounter in in in machine learning or rather statistics if you do not have this tool called probability theory. So that is the the the

### 00:08:03 · Speaker 5

prolog. There's absolutely no way you can answer a few questions. See, just like you can't answer questions like, you know, suppose I draw an arbitrary curve, right? Or rather I plot some measurement that I make, with speed measurement or something as a function of time. If I have to find out what is the the total distance that was covered by this particle or a moving body, only when I have speed as a function of time, you can't answer that question if you don't have calculus, isn't it? Because, you know, you need

### 00:08:33 · Speaker 5

idea of like integration which is area under the curve otherwise you can't answer that question. Similarly there are questions that you can't answer if you if there is no if if if if the tools of probability theory are not in place. So so lot of people tend to think right oh maybe you know it was a false word people talk of probabilistic machine learning because it is it's just there etcetera it's not

### 00:09:03 · Speaker 5

that it's a tool that is absolutely needed. There is no other way to handle or rather answer a few questions that that arise without having this versatile tool of mathematics called probability here. Okay.

### 00:09:18 · Speaker 5

So that's I mean what I'll do today is that I'll try to convince you that what are the kind of questions that cannot be answered by any other branch of mathematics, right?

### 00:09:29 · Speaker 5

you need to develop a special branch of mathematics called probability theory and just develop some background there so that yeah sufficiently charged you know. develop some background there so that we can I mean all of you already know this I'm sure but still just to get your memory and get up to the speed we'll do that.

### 00:09:52 · Speaker 3

we will put ash.

### 00:10:07 · Speaker 3

doesn't seem to do a good OCR.

### 00:10:12 · Speaker 3

Right?

### 00:10:18 · Speaker 2

keyboard will be better

### 00:10:20 · Speaker 3

Hmm

### 00:10:21 · Speaker 2

keyboard script will be better. It will be more simple.

### 00:10:27 · Speaker 3

you're saying I'll have to

### 00:10:30 · Speaker 3

toggle the keyboard

### 00:10:45 · Speaker 3

Okay

### 00:10:58 · Speaker 3

Correct

### 00:11:01 · Speaker 3

this we'll see intro

### 00:11:11 · Speaker 3

Introduction to

### 00:11:20 · Speaker 2

at the beginning can you put lecture number as well?

### 00:11:25 · Speaker 3

Hmm

### 00:11:39 · Speaker 3

Okay

### 00:11:41 · Speaker 3

Okay, so let's get started.

### 00:11:42 · Speaker 2

third

### 00:11:54 · Speaker 3

Okay. So what is the

### 00:11:56 · Speaker 5

Uh as I said what are the kind of questions that we are interested in uh in in in uh in the statistical branch of statistical statistics or machine learning is. We'll say

### 00:12:10 · Speaker 3

So fundamentally

### 00:12:22 · Speaker 3

most problems in science and engineering

### 00:12:30 · Speaker 2

just go. Is the, even I placed my hand on top of my iPad, no, it's just going.

### 00:12:40 · Speaker 5

everywhere is there a way to control that?

### 00:12:47 · Speaker 2

Eustis

### 00:12:57 · Speaker 3

So you can enable the second last option right next to drawing mode.

### 00:13:00 · Speaker 5

This one

### 00:13:02 · Speaker 6

Yes

### 00:13:03 · Speaker 5

What is this?

### 00:13:04 · Speaker 6

so that will allow only the pencil to write.

### 00:13:09 · Speaker 6

Sperm Reject

### 00:13:11 · Speaker 5

just palm leaf. Oh great, thank you. It should be there but I don't know where it is. Okay. Fundamentally most problems in in science and engineering

### 00:13:24 · Speaker 3

C I E N C E

### 00:13:28 · Speaker 3

Car

### 00:13:30 · Speaker 3

Hello

### 00:13:34 · Speaker 3

functional approximations.

### 00:13:45 · Speaker 3

Okay? So what do I mean by this?

### 00:13:48 · Speaker 5

most problems that you get in science and engineering are concerned about function approximation. So what are functions? So now the function

### 00:14:02 · Speaker 2

basically a mapping, right, that is learned between function F. As a mapping that is learned between two sets called A

### 00:14:14 · Speaker 2

to be right where

### 00:14:17 · Speaker 2

A and B are sets.

### 00:14:23 · Speaker 2

Okay? So it's it's a rule, it's a mapping, right? That would map one set to another.

### 00:14:31 · Speaker 3

Set

### 00:14:51 · Speaker 3

Okay and generally

### 00:15:07 · Speaker 3

this set is called the domain

### 00:15:11 · Speaker 3

and this it is called the range.

### 00:15:18 · Speaker 5

So there is a function it takes an element from the set called domain and maps it to another set called range okay. So now we'll take examples of functions.

### 00:15:30 · Speaker 5

you take some examples of functions. So let's say that there is a function, okay? That

### 00:15:38 · Speaker 5

takes element from real numbers, okay? and maps it to another real number. This is a function which maps real numbers

### 00:15:51 · Speaker 5

P

### 00:15:52 · Speaker 3

real numbers. This R represent set of real numbers.

### 00:16:04 · Speaker 3

set of real numbers, okay? So this function

### 00:16:08 · Speaker 5

apps set up real numbers to

### 00:16:09 · Speaker 2

bit of real numbers, okay? And you can take another example where

### 00:16:17 · Speaker 5

perfect

### 00:16:17 · Speaker 3

S

### 00:16:19 · Speaker 3

In fact, to be precise here, it actually maps

### 00:16:31 · Speaker 3

real numbers to set of positive real numbers.

### 00:16:37 · Speaker 3

Correct?

### 00:16:38 · Speaker 3

So R plus this is set of reals.

### 00:16:46 · Speaker 5

and R plus is set of positive real numbers, right? So this is a function. So you can think of any, I mean, lots of such examples, right? So another example can be that you can take modulus X.

### 00:17:01 · Speaker 5

Okay, similarly, right? So this is another, this is another function that maps R to R plus, similarly. So these sets, right? They need not be R, they can be anything. So let's take another example where f of x is equal to

### 00:17:21 · Speaker 5

X transpose X, okay? Now where X, the domain, right, is

### 00:17:29 · Speaker 5

in some D dimensional real space.

### 00:17:32 · Speaker 5

Hello

### 00:17:33 · Speaker 2

So what do I mean by this? This is

### 00:17:42 · Speaker 2

real vector

### 00:17:46 · Speaker 5

So what does this mean? This means that you all are familiar about the

### 00:17:51 · Speaker 5

the Cartesian coordinates, right? So you know that every point in Cartesian coordinate, I can if I call this x one x two, every point in Cartesian coordinate can be represented by set of two real numbers, right? If you take a point here, this point will be some x one comma x two, this is another point x one comma x two, x one cap comma x two cap, etcetera and so on. So this is this is typically represented as R two, right? So these are

### 00:18:20 · Speaker 2

these are actually called

### 00:18:26 · Speaker 2

This is a two dimensional

### 00:18:29 · Speaker 2

Euclidean space.

### 00:18:32 · Speaker 2

named after

### 00:18:33 · Speaker 5

the mathematician Euclid, okay?

### 00:18:37 · Speaker 5

is called two dimensional Euclidean space or vector space. Now similarly imagine a D dimensional Euclidean space. So basically this is

### 00:18:51 · Speaker 3

still happening

### 00:18:53 · Speaker 3

When I place my hand it is taking me everywhere.

### 00:19:07 · Speaker 2

सर इफ यू आर नॉट कंफर्टेबल वी कैन सर्च टू गुड नोट्स आल्सो।

### 00:19:11 · Speaker 3

Hi

### 00:19:11 · Speaker 3

It's okay

### 00:19:12 · Speaker 2

understand this. How do I get this

### 00:19:18 · Speaker 2

of intestine

### 00:19:21 · Speaker 2

No, no, no, I don't want this.

### 00:19:25 · Speaker 2

So this

### 00:19:26 · Speaker 5

side pain will always be there is that I want this to disappear.

### 00:19:31 · Speaker 6

you can remove it near the settings icon the full screen button that should do.

### 00:19:31 · Speaker 2

you can

### 00:19:36 · Speaker 5

Where is it?

### 00:19:37 · Speaker 2

or

### 00:19:38 · Speaker 2

Alright, let's do the

### 00:19:38 · Speaker 6

on the right hand side to the sittings material

### 00:19:39 · Speaker 5

Setting Setting Okay

### 00:19:41 · Speaker 6

Okay

### 00:19:41 · Speaker 6

टॉप राइट नेक्स्ट लेट नॉट इन सेटिंग्स

### 00:19:42 · Speaker 2

Next slide

### 00:19:43 · Speaker 5

uh not

### 00:19:43 · Speaker 2

next two settings

### 00:19:46 · Speaker 6

Hello

### 00:19:46 · Speaker 2

Auto

### 00:19:46 · Speaker 5

this one. Oh, this full screen. Okay, great.

### 00:19:46 · Speaker 6

and

### 00:19:47 · Speaker 2

one

### 00:19:50 · Speaker 5

Hmm

### 00:19:53 · Speaker 5

Please keep educating me okay with all this. I've never used this like one note. That's why the issue. I'll I'll get used to it no problem. Yeah. You're saying see this thing is a D dimensional real vector right? So this is called in general this is called

### 00:20:08 · Speaker 2

the

### 00:20:11 · Speaker 2

D dimensional

### 00:20:18 · Speaker 2

real space

### 00:20:20 · Speaker 2

So basically every point

### 00:20:22 · Speaker 5

in this space is represented by a d-dimensional triple where d is a positive real number okay z plus

### 00:20:36 · Speaker 5

Now whenever I write this notation, right, I mean a D dimensional real space. So it is the extension of the two dimensional Cartesian space that you know of, right? A D dimensional real space is simply

### 00:20:55 · Speaker 5

points in a d-dimensional real space are simply uh the simply the vectors right that are there in d-dimension. Every point in that d-dimensional space can be now represented uh using a tuple of d real numbers. That's what I mean. Now this function that I'm talking about uh which is f of x will give you x transpose x where transpose uh is you understand what transpose means right? Transpose of operation of a vector. Now this is a function that maps

### 00:21:31 · Speaker 5

R D to

### 00:21:34 · Speaker 5

again R plus. Okay, the product can be negative as well. So it maps RD to R.

### 00:21:42 · Speaker 5

Okay, so this function takes as input a D dimensional real vector and gives out a real number. So that is a function that would take a D dimensional vector to a real number and so on. So I mean you can think of these things, right? There are multiple examples of what functions constitute and as I said, most problems in science and engineering are

### 00:22:07 · Speaker 5

the following that

### 00:22:09 · Speaker 3

Given

### 00:22:13 · Speaker 3

Given

### 00:22:18 · Speaker 3

Pairs

### 00:22:21 · Speaker 3

Off

### 00:22:28 · Speaker 3

and I'll say it that way

### 00:22:35 · Speaker 3

maybe I'll define it in formal way

### 00:22:40 · Speaker 3

Hmm

### 00:22:43 · Speaker 3

Okay? Suppose

### 00:22:49 · Speaker 3

capital A and capital B denote

### 00:22:55 · Speaker 3

Denote

### 00:22:59 · Speaker 3

ఈ డొమైన్ అండ్ ది రేంజ్ సెట్

### 00:23:11 · Speaker 3

Okay. Domain and the range set. Now, suppose you are also given, given, given.

### 00:23:22 · Speaker 3

P that is pairs

### 00:23:30 · Speaker 3

pairs of elements

### 00:23:37 · Speaker 3

X I, Y I

### 00:23:41 · Speaker 2

such that

### 00:23:44 · Speaker 2

Now excise, so let's say that you know these are

### 00:23:49 · Speaker 2

in such points, X I

### 00:23:53 · Speaker 2

is an element from A and Y I is an element from P

### 00:24:00 · Speaker 3

Okay

### 00:24:08 · Speaker 3

So this we have to say suppose A and B denote the domain and range sets of

### 00:24:14 · Speaker 3

a function

### 00:24:18 · Speaker 2

of a function f

### 00:24:22 · Speaker 5

that takes an element from A and maps it to elements in B. So given pairs of elements X I comma Y I such that X I is in A and Y I comma B, the question or the problem, problem.

### 00:24:36 · Speaker 5

is to find

### 00:24:40 · Speaker 3

the

### 00:24:46 · Speaker 3

underlying function

### 00:24:49 · Speaker 3

F

### 00:24:52 · Speaker 3

Okay, so this has been

### 00:24:54 · Speaker 5

problem of interest for

### 00:25:00 · Speaker 5

something. This this has been a problem of interest for scientists and engineering engineers from time time immemorial, right? So this so if you have given uh some n elements, uh these are you can also call these as observations.

### 00:25:18 · Speaker 5

call these as observations or data or whatever, right? We have given this.

### 00:25:26 · Speaker 5

try to find the underlying function F. So now why is this important? Suppose you find the underlying function, what is the what is the use of finding out that underlying function? Is that let me give you examples perhaps. Example is

### 00:25:39 · Speaker 5

Now let's say

### 00:25:40 · Speaker 3

A

### 00:25:42 · Speaker 3

as

### 00:25:44 · Speaker 3

set of

### 00:25:46 · Speaker 3

positions

### 00:25:51 · Speaker 3

of a planet in sky.

### 00:25:56 · Speaker 3

Okay

### 00:26:03 · Speaker 3

by position driving the coordinates.

### 00:26:19 · Speaker 3

maybe. No, I'll

### 00:26:22 · Speaker 5

might confuse you a little. Let's not take that example. Let's let me take that example next. First example that I can take is

### 00:26:35 · Speaker 3

So

### 00:26:37 · Speaker 3

it's a adjunct.

### 00:26:40 · Speaker 3

of a body.

### 00:26:46 · Speaker 3

So B can be

### 00:26:51 · Speaker 3

force exerted on it

### 00:27:00 · Speaker 3

Okay

### 00:27:00 · Speaker 5

So suppose I give you, I measure acceleration of a particular

### 00:27:06 · Speaker 6

moving body

### 00:27:07 · Speaker 5

and I'll also give you what was the force that was exerted on it. So the task is to find out how are these two sets related. Right? The set of force exerted on it and the acceleration uh that the body undergoes, right? I mean how how are they related?

### 00:27:26 · Speaker 5

Okay, so this was actually the question that was

### 00:27:32 · Speaker 5

that was asked by uh done, right? Do you know how are they related? These two things?

### 00:27:42 · Speaker 6

mass into acceleration.

### 00:27:44 · Speaker 2

Okay

### 00:27:44 · Speaker 5

they are linearly related, right? So now the let's if I call the acceleration of a body denoted by A, which is a scalar. So note that set A here is set of real numbers. Because in fact positive real numbers acceleration cannot be negative. And

### 00:28:08 · Speaker 5

can be negative right because also has the direction. So force can also be negative. So yeah so force exerted on it is another real number and they are

### 00:28:20 · Speaker 5

denote this by F. Then the relationship between these two, as you know, is a linear relationship.

### 00:28:28 · Speaker 5

simply given by, uh I mean the proportionality constant is the mass. So you simply have the force is related to acceleration. It is proportional to acceleration and the proportionality constant is the mass. Now, as I said, right? I mean this was, why do we need, this is one example. The I I I'll take questions in a while, okay? Aditya. So then I can think of another example.

### 00:28:59 · Speaker 2

somebody give me an example uh of a case where the function is not linear.

### 00:29:16 · Speaker 3

energy

### 00:29:16 · Speaker 7

energy energy kinetic energy to

### 00:29:19 · Speaker 2

in

### 00:29:22 · Speaker 7

kinetic energy to velocity

### 00:29:25 · Speaker 5

Okay, how are they related? Kinetic energy and velocity.

### 00:29:28 · Speaker 7

half mv square. E is equal to half mv square.

### 00:29:32 · Speaker 5

velocity is v and energy is e. Okay,

### 00:29:37 · Speaker 2

do that

### 00:29:40 · Speaker 2

So day

### 00:29:40 · Speaker 3

is

### 00:29:46 · Speaker 3

velocity, v is energy

### 00:29:50 · Speaker 3

Right so there the relationship is.

### 00:30:00 · Speaker 2

and so on, right? I mean, now you get the point.

### 00:30:03 · Speaker 5

Now, uh, here, right? I mean, uh, lot of scientists and engineers, they wanted to figure out this relationship, right? I mean, lot of research that people were doing, uh, was focused on finding out the relationship between

### 00:30:20 · Speaker 5

the measurements that I have done and these measurements are represented as the elements of sets. So mathematically speaking as I said right you know look at my initial statement I said that most problems in science and engineering are function approximations. uh what I need to say is that suppose there are two A and B are two sets which are the domain and range sets of a function and if you are given elements uh which are which are pairs from these two sets.

### 00:30:50 · Speaker 5

Okay. The underlying problem is to find out or identify what the underlying function is that relates elements of A to elements of B.

### 00:31:01 · Speaker 5

Now why is this question important? So the next thing is what do we get if we approximate the underlying function? Okay? So now function approximation

### 00:31:15 · Speaker 2

somebody tell me why is that important? Why do you have to relate quantities, measured quantities?

### 00:31:25 · Speaker 3

Prediction

### 00:31:27 · Speaker 2

Exactly, right? So one one of the things is function approximations.

### 00:31:39 · Speaker 3

proximation, okay, enables predictions.

### 00:31:45 · Speaker 2

So what do you mean by prediction? So we have to define this, right? So prediction mathematically

### 00:31:52 · Speaker 2

a simple prediction is is that

### 00:31:58 · Speaker 3

Find

### 00:32:02 · Speaker 3

The element

### 00:32:06 · Speaker 3

in set B which is the range set range set.

### 00:32:14 · Speaker 3

corresponding to

### 00:32:21 · Speaker 3

any element in A

### 00:32:26 · Speaker 3

element in the domain

### 00:32:32 · Speaker 3

This is important

### 00:32:33 · Speaker 5

right so now if you look at it the data or the observations that we have done okay is there a pointer here somewhere like without writing can I just point to things

### 00:32:47 · Speaker 5

in good notes it used to be there. Highlighter is there. I don't need highlighter.

### 00:32:51 · Speaker 2

writer like a cursor or a pointer of sorts do you know anybody knows

### 00:33:02 · Speaker 2

See, what I want to do is I simply want to like show this, right?

### 00:33:07 · Speaker 2

highlight on this

### 00:33:08 · Speaker 2

I keep doing this

### 00:33:10 · Speaker 2

because when I write something I

### 00:33:11 · Speaker 5

go back and just show that is there something of that sort here

### 00:33:17 · Speaker 3

straight styles orientation

### 00:33:24 · Speaker 3

Does anybody know that? No?

### 00:33:28 · Speaker 4

So there is no pointer

### 00:33:30 · Speaker 5

There's no pointer here.

### 00:33:31 · Speaker 4

No, you can maybe use the assistive touch button on the right side to kind of circle around things, but that's about it.

### 00:33:38 · Speaker 5

I see. But it'll just stay away, no? I mean, I don't want that to stay. I just want to point out to that thing. Yeah, somebody should use

### 00:33:46 · Speaker 7

somebody

### 00:33:47 · Speaker 7

use NS pointer if you click on the pen itself.

### 00:33:47 · Speaker 5

Yes

### 00:33:53 · Speaker 5

meaning I didn't get that.

### 00:33:54 · Speaker 7

hmm

### 00:33:55 · Speaker 3

click on the pen

### 00:33:56 · Speaker 3

I guess you're supposed to get something new.

### 00:34:00 · Speaker 2

Listen

### 00:34:03 · Speaker 2

this one's not it.

### 00:34:03 · Speaker 3

Yeah

### 00:34:06 · Speaker 3

No, no, I mean, I mean on the pen itself. Like the whatever you have it highlighted.

### 00:34:12 · Speaker 2

Hmm

### 00:34:13 · Speaker 3

few happening

### 00:34:14 · Speaker 2

to click it again

### 00:34:17 · Speaker 3

Okay

### 00:34:20 · Speaker 2

Nine

### 00:34:22 · Speaker 2

Do you see any options on

### 00:34:25 · Speaker 3

Okay

### 00:34:27 · Speaker 7

Can you click and hold that pen once?

### 00:34:34 · Speaker 5

Nothing happens.

### 00:34:36 · Speaker 7

No

### 00:34:37 · Speaker 5

Anyway, so find it out. I mean if anyone of you want to find that out, let me know. uh Or just tell Microsoft to have that feature in the next version. It's very very useful. For example,

### 00:34:49 · Speaker 3

good notes.

### 00:34:59 · Speaker 3

it was there was the stain, you see?

### 00:35:03 · Speaker 3

so nice

### 00:35:04 · Speaker 5

Nice

### 00:35:05 · Speaker 5

I'll just go away. So if there is something that I write, I can go back and you know just mark this and talk about this and it was very very useful for me. You see that red mark. Here it is not there at all.

### 00:35:20 · Speaker 5

Oh

### 00:35:22 · Speaker 6

if you go back to the pen gallery, I think there is an option.

### 00:35:26 · Speaker 5

is there okay let's see

### 00:35:27 · Speaker 6

Yes

### 00:35:28 · Speaker 6

So there is a plus button next to the pens, right?

### 00:35:32 · Speaker 2

correct. Highlighter.

### 00:35:34 · Speaker 6

Hello

### 00:35:36 · Speaker 6

select the pen mode and it says that use pen as a pointer I don't know where to get this.

### 00:35:37 · Speaker 4

and it says that

### 00:35:42 · Speaker 4

That's only on Windows

### 00:35:45 · Speaker 6

Oh, okay.

### 00:35:46 · Speaker 5

Okay

### 00:35:51 · Speaker 5

Fine. Okay, fine, whatever. So I'll have to maybe just go back. It's not very optimal because I keep using this pointer so many times when I was teaching. It was very useful for me.

### 00:36:03 · Speaker 5

Anyway, okay.

### 00:36:04 · Speaker 4

You can use the other app and later upload the notes here if you'd like.

### 00:36:09 · Speaker 5

Well, that's also fine, that's what I was doing, but people suggested this one note and I just thought that it's okay.

### 00:36:21 · Speaker 2

Okay, no problem, let's move on. Yeah, so what I was saying is that you are

### 00:36:30 · Speaker 5

Once

### 00:36:31 · Speaker 5

still okay right I can just point it here and these some of these things will become yellow colored I think it's fine. but when you are looking at the notes you should just ignore these yellow colors because they only mean that while teaching I have pointed out to them that's all okay.

### 00:36:47 · Speaker 5

Anyway so let's try to do that. I mean they are not I mean they are no way they are important or whatever right? They just simply uh mean that while teaching I just pointed to those things and came back.

### 00:37:01 · Speaker 5

If that is okay, I can continue with this. Just use this thing and highlight it. Okay. Anyway, so what I was saying is, why do you need functional approximations is that while you have observations and data for about n points, you have made n observations. uh We are often interested in uh understanding uh how the system behaves beyond these n observations that we have made. Otherwise, we have anyway made those n observations, there is no need.

### 00:37:31 · Speaker 5

in in those scenarios. But we need to know what happens beyond the N observations, right? So that is what we call as prediction. Prediction is basically find the element

### 00:37:43 · Speaker 5

in range, right? Find element in the range set.

### 00:37:49 · Speaker 5

in the range at corresponding to

### 00:37:53 · Speaker 5

any element in the domain. So given any element in the domain, you need to understand how the range set, uh how, uh what, what element in the range set that it gets mapped to. And that is what is called as prediction. So here, what you are doing is, given a particular acceleration, right, that was not observed, if I want to know what the corresponding force is, then if you find that underlying function, then you can find out what the force is. Okay? Similarly with this velocity and energy, right? So if you are given

### 00:38:23 · Speaker 5

a particular velocity if I want to know what is the energy that was exerted on it. I can just use this function and find out what it is. Now that is one of the most important applications of why one needs function approximation that all as I said all problems in science and engineering are about predicting this.

### 00:38:41 · Speaker 7

Okay

### 00:38:43 · Speaker 7

Right

### 00:38:44 · Speaker 2

Any questions so far? Show of hands.

### 00:38:53 · Speaker 2

Yes, Raghavendra, Goan.

### 00:38:56 · Speaker 6

So is this also called as inverse problem that that we talk about?

### 00:39:01 · Speaker 5

Yeah, you can call it a moves problem, right?

### 00:39:05 · Speaker 5

See, I'm I'm actually going to, you know, pair basics of stuff. I'm I'm sure that all of you know this already. But yeah, so I want to call it function approximation, you know, given these pairs of observations and data, rather observations from two particular sets, I want to understand what the underlying function is. Yes, of course, it is a problem. See, it's not quite the inverse problem because in in typical inverse problems what happens is you only have access to output without having access to input.

### 00:39:35 · Speaker 5

Rather you don't have elements of range set at all. Sorry, domain set at all in inverse problems. So that's why you are called inverse problems. Here you have access to pairs from both the domain and range. You get it? That's how they are different.

### 00:39:50 · Speaker 5

ओके अरिजित

### 00:39:52 · Speaker 1

Sir, sir, one question I have. Why do you use this word approximation?

### 00:39:56 · Speaker 5

approximation. Is this I?

### 00:40:00 · Speaker 5

sorry

### 00:40:02 · Speaker 5

Who is talking? Why do you have this? No, who is talking?

### 00:40:02 · Speaker 1

Why do you have this?

### 00:40:04 · Speaker 1

special skill sir

### 00:40:06 · Speaker 5

Uh see we have a bit of rule in this class that if you if you want to talk please raise your hands because otherwise no too many people it becomes a little chaotic. Please raise your hands. I'll call out your name and you can ask questions. Okay thank you. Yeah I'll I'll I'll come I'll I'll I'll go in the order. Harijit.

### 00:40:28 · Speaker 0

Uh sir, one question that till now whatever a function relation we saw between two elements, it's like kind of a proportional, right? Being it linear or non-linear. So one is increasing, other is increasing or inversely proportional also. But suppose the relationship is very complex. For example, if it is too cold, I may not go out. If it is little hot, I will go out. But if it is too hot, again I will send come back to my home, right? So this kind of relation where you cannot directly make it proportional or inversely proportional.

### 00:40:58 · Speaker 0

professional. So how our I mean this prediction will work there. I mean generative model maybe too early to ask this just asking.

### 00:41:07 · Speaker 5

Hello

### 00:41:07 · Speaker 5

Good question, very good question. And yes, you see, that is why right we need other mathematical tools. Linearity or proportionality doesn't work. See, for instance, suppose you need to, suppose you just measure the, let's say that you measure the the temperature, you just heat a body, okay, you just heat a metal and measure the temperature of that metal at different points along the material. Now if you want to ask me this question,

### 00:41:37 · Speaker 5

that if I measure temperature at one point, okay, I need to know how the temperature varies across the body, you know, how do you model it?

### 00:41:45 · Speaker 5

you measure temperatures. I want to know what the temperatures are at other points of the body as well given some heat. Now you can't there is no way that you can write it as a linear equation you have to express that as a differential equation. Isn't it? Okay. Right? So that's why you need another branch of mathematics right which is differential calculus and you need to express that as differential equation. But the kind of question that you are asking is the same now that if I can measure if I have measured the the temperature of a body at certain points

### 00:41:58 · Speaker 6

Okay

### 00:42:15 · Speaker 5

Now if I if I give you the properties of that body, right? And the the initial conditions, if I have to know the temperature the body is at at different locations of the body then there is you need to model it as a differential equation. So what I'm trying to say is of course the point that you brought up is very relevant. That's what I'll move on to next, you know. There are questions that cannot be answered with with with these kinds of things, right? These kinds of existing mathematical tools and that's why you need new batches of mathematics and probability theory is one such

### 00:42:50 · Speaker 4

three

### 00:42:51 · Speaker 5

So I will give you examples, example scenarios and questions that cannot be answered using the existing mathematical tools and that's how I motivate why probability theory is needed. It's absolute necessity. Yeah.

### 00:43:06 · Speaker 5

ओके, पार्थ

### 00:43:09 · Speaker 4

So, my question is more about the terminology. So we are using the word prediction here and from what we study in probability predictions, it's about an estimation of numbers, right? But in this case functions, we are mostly talking about absolute values and we're getting absolute answers. So why is the word prediction and approximation being used here?

### 00:43:14 · Speaker 5

Hmm

### 00:43:30 · Speaker 5

Okay. um See that's a definition, right? I mean, uh people use different different terminology for different things, right? I am using this word prediction, that's why I define. Whenever I use a term, I define what it is. To me, prediction here is simply finding an element in the range corresponding to any elementary domain. In fact, even in statistics and probability theory, when we talk of prediction, we actually are evaluating a particular function at a point. I will talk about it in a while. Okay. So,

### 00:44:00 · Speaker 5

you are not there is no I mean there is no quote unquote uncertainty. We will discuss all that in a while right? I mean probability theory is a very

### 00:44:13 · Speaker 5

what should I say? It's a it's a lot of misnumbers and a lot of misunderstandings, right? I mean, people use terms, right, right, left and center. uh even there in probability theory, prediction refers to uh evaluating a function, a particular function at a at a point. We'll we'll talk about it in a while.

### 00:44:33 · Speaker 5

Okay, uh anything else? Any other question? I don't see any hands raised. So we'll perhaps move on.

### 00:44:34 · Speaker 4

anything

### 00:44:41 · Speaker 5

Now as like Arijit was asking right so the problem here is the following

### 00:44:48 · Speaker 3

Following

### 00:44:51 · Speaker 3

rather. Yeah.

### 00:45:03 · Speaker 3

Now what if

### 00:45:06 · Speaker 3

the mapping between the range

### 00:45:13 · Speaker 3

between the sets.

### 00:45:18 · Speaker 3

cannot be found out

### 00:45:24 · Speaker 3

using

### 00:45:27 · Speaker 3

existing mathematical tools.

### 00:45:35 · Speaker 2

as he was pointing out right. Okay you know in fact as I

### 00:45:40 · Speaker 2

that they can take another exam

### 00:45:42 · Speaker 2

people have right here

### 00:45:44 · Speaker 2

In fact, you can write this as

### 00:45:47 · Speaker 5

problematic

### 00:45:50 · Speaker 3

brings the flow and makes the glass up.

### 00:45:54 · Speaker 3

Okay, how do I

### 00:45:57 · Speaker 3

What happened to this? How do I

### 00:46:12 · Speaker 3

This can be written as you know that this is

### 00:46:17 · Speaker 3

the derivative of

### 00:46:22 · Speaker 3

double derivative of the position

### 00:46:30 · Speaker 3

respect to time

### 00:46:34 · Speaker 3

because acceleration has to be measured and you have

### 00:46:36 · Speaker 5

calculus so you can represent that as the the rate of change of dt squared

### 00:46:45 · Speaker 5

you can represent that as the double derivative of the position right with respect to time. Now the the problem is as he was pointing out if the relationship between the elements of range and the the domain if there if you cannot find out if they cannot if you cannot find the functions you can't rather express those relationship using existing mathematical tools what do you do? The solution this is just just I gave you the example, right? The calculus was

### 00:47:19 · Speaker 5

was discovered. So come up with new mathematical tools.

### 00:47:31 · Speaker 2

So this is how right probability theory is motivated that specifically for probability

### 00:47:35 · Speaker 5

the problem is what happens is

### 00:47:41 · Speaker 5

formal definitions of all this. See motivation for probability theory is the following that what happens is the

### 00:47:52 · Speaker 5

relations between sets to be relations to be

### 00:47:56 · Speaker 5

So

### 00:47:56 · Speaker 2

we approximated our relations to be found out

### 00:48:04 · Speaker 2

or

### 00:48:05 · Speaker 2

Hello

### 00:48:06 · Speaker 2

Complex

### 00:48:07 · Speaker 5

What do I mean by complex?

### 00:48:09 · Speaker 2

that

### 00:48:11 · Speaker 5

Correct

### 00:48:12 · Speaker 3

do not adhere to existing, do not adhere within the existing mathematical framework, okay?

### 00:48:26 · Speaker 3

mathematical framework

### 00:48:28 · Speaker 5

if this happens, uh then you know you need to come up with new uh way of modeling things or new new way of expressing things, you know, that's why probability theory becomes handy. Let me give you an example, I'll also tell you what is the fundamental idea behind probability theory. See example is

### 00:48:47 · Speaker 5

Now suppose I've given

### 00:48:51 · Speaker 3

take an E M L problem right. So elements

### 00:49:03 · Speaker 3

Let me not make it pedonautic.

### 00:49:08 · Speaker 5

I've given images, okay, pictures, let me call it as pictures. Because as I'm not going deeply into maths yet. So let's say that I'm given pictures, so I have to learn relationship between set of pictures, right?

### 00:49:23 · Speaker 3

and

### 00:49:31 · Speaker 3

idea of

### 00:49:34 · Speaker 3

Gender, Okay.

### 00:49:36 · Speaker 5

this set typically right when how do you represent a picture in a in in in in a in a computer is that you write them as R

### 00:49:47 · Speaker 5

P cross Q basically it's a grid of numbers right what is a picture what is an image basically it's a grid of numbers you have P rows and Q columns everything is a real number here right

### 00:50:01 · Speaker 5

So you have P cross Q real numbers. That's how you represent a picture. Now, every picture is an element.

### 00:50:10 · Speaker 5

in a P cross Q dimensional real space. So you should imagine that just like we have the Cartesian plane, right, which is two dimensional, there is a P cross Q dimensional space and in the P cross Q dimensional space every image now becomes a number, every picture becomes a a point basically, okay, not a number, I'm sorry, it's a point. Now what I need is given this, I'll have to predict, right? When you remember what the definition of our prediction is, when I define prediction as uh finding out the

### 00:50:40 · Speaker 5

element in the set corresponding to any element in the domain. So now this gender is a set, a discrete set of two values.

### 00:50:52 · Speaker 5

Let's assume that it's a discrete set of two values. Now given this picture, I need to find a function, okay? That to take an element in

### 00:51:01 · Speaker 5

P cross

### 00:51:02 · Speaker 2

Q dimensional space that is a vector and maps it to

### 00:51:11 · Speaker 2

one of the two discrete numbers zero and one. Think about it.

### 00:51:17 · Speaker 5

Now remember how this picture was taken, okay, or rather obtained. How are these P cross Q numbers obtained? Now what is happening in the background is the following that some person is standing, okay, standing or sitting or whatever. Now you have a sensor, okay, which we call as camera.

### 00:51:37 · Speaker 5

Now what a light falls on that person, okay? And reflects some electromagnetic radiations back. And those radiations are sensed or captured by the sensor. And what happens in in the sensor is that there is a voltage or current change that happens. And that is what is recorded as a real number here, correct? That is what a picture is and you know these grids correspond to different spatial locations of the object.

### 00:52:05 · Speaker 5

So what is it we are trying to do here? Imagine, we want to relate, okay, the amount of light that a particular position

### 00:52:18 · Speaker 5

reflects. Okay? To an idea called gender.

### 00:52:23 · Speaker 5

You see what's happening?

### 00:52:28 · Speaker 5

It is very very abstract, you know, in the sense that, uh see here what happened is that uh in all the examples that we gave, right? Force was measurable, acceleration was measurable, energy was measurable, velocity was measurable and so on. But here, what is being measured, right? Is the amount of reflectance that a particular surface is giving you. What you want to relate it to is an abstract idea, right? And a non-measurable idea called gender.

### 00:52:59 · Speaker 5

Do you appreciate the the difficulty in what we are trying to do? Of course, right? I mean this can be gender or this can be let's say if a person is beautiful or not. I mean these are I keep making this philosophical statement that nature is very simple, right? I mean if you if you want to fly an aircraft which is a very complex task, all you need is you know first order differential equations and Newton Newtonian laws, that's all.

### 00:53:25 · Speaker 5

Okay? To do things like things that are as complex as flying an aircraft. But to find out, right, whether somebody is a male or a female from a picture, you need a billion parameter model.

### 00:53:40 · Speaker 5

See, by the way,

### 00:53:42 · Speaker 4

Look at this

### 00:53:43 · Speaker 5

How many parameters that this model has? I've not defined what a model is yet, but still, this F equal to MA, how many parameters does this have?

### 00:53:52 · Speaker 5

Can somebody tell me

### 00:53:54 · Speaker 3

two. two. three.

### 00:53:55 · Speaker 5

one. It has one parameter. M is the only one parameter that it has.

### 00:53:57 · Speaker 3

one

### 00:54:02 · Speaker 5

Right? And the other example that we saw is also one single parameter model. Okay? Or if you take a second order differential equation or a third order differential equation, all it has are three, four parameters. So as I said, to explain nature of, you only need two, three parameter models. But to, you know, understand and predict things that human beings constructed, you need billions of parameters. It only shows how complicated we are as human beings. I'll give you another example for that. Let's say that you have a document.

### 00:54:35 · Speaker 2

These are the typical day to day ML problems that we solve, right? uh You have a document.

### 00:54:44 · Speaker 2

And what you need is the idea of

### 00:54:48 · Speaker 2

Emotion

### 00:54:51 · Speaker 5

Right? So what's a document? uh Document is collection of certain tokens, okay? uh So we'll talk about all this, right? What is tokenization etcetera and all that. You can think of these as collection of words.

### 00:55:06 · Speaker 5

K words, okay? All these words are are represented as vectors, okay? Each of them has each of them is represented by let's say a a a D dimensional vector.

### 00:55:20 · Speaker 5

which means that this entire document now will become a point in a D cross K dimensional space. Every document is an element or a vector in a D cross K dimensional space. What you need is a function, okay, that will take an element from D cross K dimensional space, which is a which is a document and maps it to let's say that this emotion, so there are five emotions, right? Like I am angry

### 00:55:53 · Speaker 5

Happy

### 00:55:55 · Speaker 5

whatever, right? So represent that as zero, one, two, etcetera. So it just maps it to some discrete set of zero, one, two, three, four. Okay? So this is what we need. So what do we do? I mean, the so-called inference that we do, right? is nothing but prediction. What is prediction here? Given this particular function, if you are given any element from this from the domain set, you want to map it to the element, any corresponding element in the range set. That is what is to be done. Now, you know that, right? I mean, this is what

### 00:56:25 · Speaker 5

things like chat gpt etcetera do where you can't find the relationship with what is emotion I mean like what is the positive emotion for you can be a negative emotion for me and vice versa so this this idea of emotion is is very very synthetic and man-made okay so to understand how again if you go back to what how these vectors were created okay if you take some like you know embedding like tfidf which is a very

### 00:56:55 · Speaker 5

way of looking expressing words which is simply counting the number of times every word has occurred keeping a dictionary right. How is that related to a concept called emotion which is which is a very very you know abstract concept.

### 00:57:13 · Speaker 5

Okay? So now the the problem is that because we are dealing with the relationship that are complex. Now what do I mean by complex? Complex mean that they do not adhere to existing match. I cannot find a linear relationship or a quadratic relationship or a differential equation or a relationship that can be modeled using a differential equation that would relate these reflectances that a surface will give to an an idea of co-gender or rather it can also I mean you can you can think of a

### 00:57:43 · Speaker 5

all the problems that you do in ML, right? I mean, take a picture and do a person re-identification where you identify what the person is and then you can talk of any of those things which are

### 00:57:55 · Speaker 5

which cannot be modeled using existing mathematical tools.

### 00:57:59 · Speaker 5

Okay? So that's the motivation, right? You know, why do you need a new mathematical paradigm is because these functions that we are trying to approximate or or find are such that they cannot be found out using existing mathematical techniques. In fact, let me tell you something.

### 00:58:17 · Speaker 5

When people were doing pattern recognition using non statistical methods, people were actually looking at coming up with these kinds of functions, right? using existing mathematical tools, okay? That would that would enable them to to relate these kinds of vectors to these kinds of elements. Let me give you an example for that. Let me take another example.

### 00:58:50 · Speaker 3

Sorry

### 00:58:50 · Speaker 2

I I I'll take questions. Just hold on.

### 00:58:50 · Speaker 3

Bye

### 00:58:55 · Speaker 2

Another example, let's say that you have a speech signal.

### 00:59:01 · Speaker 2

Okay? What you want is set of phonemes.

### 00:59:08 · Speaker 2

What are these?

### 00:59:08 · Speaker 5

I'm talking about this a, b, right or

### 00:59:15 · Speaker 5

E and all these things. See, uh note that phonemes. See, what is the commonality in all this? Commonality in all this is that the rain set, let me just tell you this.

### 00:59:29 · Speaker 5

the range set

### 00:59:31 · Speaker 2

Okay

### 00:59:33 · Speaker 2

is non measurable.

### 00:59:38 · Speaker 2

It is not measurable, right?

### 00:59:41 · Speaker 5

or rather I'll call this as abstract

### 00:59:44 · Speaker 5

So the idea of phoneme, right? So what is happening just like in the documented the uh the picture example, what is happening in the speech example is that what is that you are doing? So there is a microphone, okay, let's say that there is a speech signal.

### 01:00:02 · Speaker 5

there is a speed signal, okay?

### 01:00:05 · Speaker 5

So what is the speech signal? So I'm talking. What do I when I talk, there is a change of pressure, atmospheric pressure that is that is happening, okay? Because when I change the air comes out of my mouth with a particular type of constriction from my vocal apparatus and there is a change in pressure in the environment and there is a there is a sensor which is called microphone, which is a condenser based sensor that is measuring the rate of change of pressure as a function of time.

### 01:00:35 · Speaker 5

this thing that we that we measure right and that is converting this sensor transducer is converting the rate of change of pressure atmospheric pressure into voltage. and this is what you measure as speed signal so this is time. this is the speed signal okay it's a one dimensional signal.

### 01:00:53 · Speaker 5

So this is nothing but the rate of change of uh voltage as a function of time and the rate of change of voltage happen because there is a change of pressure that is happening as a function of time. Okay? Now tell me that our functions so then again you can represent that using multiple things you know one way to represent that is just uh speed signal is a continuous thing signal right just uh chunk it just like you do it you tokenize a document you chunk the speed signal into parts and you represent that as some like some

### 01:01:26 · Speaker 5

P dimensional vector. It's a it's a P dimensional vector. Now what you need to do is you need to learn a function that would take a P dimensional vector which would represent the rate of change of pressure, atmospheric pressure as a function of time and you need to map it to an abstract idea called phoneme. Now why is phoneme an abstract idea? So what is R? The sound R is very abstract, right? It's it's only a perception based idea, you know, you can't measure R. What you can measure is rate of change of

### 01:01:56 · Speaker 5

pressure as a function of time. Now you need to relate rate of change of pressure, right? as a function of time to an abstract idea called phoneme which is not measurable.

### 01:02:10 · Speaker 5

You understand? Everywhere the same thing is happening, right? So the rain set is

### 01:02:14 · Speaker 6

unmeasurable but a domain can be measured

### 01:02:25 · Speaker 6

Okay? So in these set of scenarios,

### 01:02:28 · Speaker 5

Good

### 01:02:28 · Speaker 6

Okay

### 01:02:28 · Speaker 5

where you have measurable domain sets and abstract frame sets. Finding out a function that would map these two via existing mathematical tools is difficult. But as I said, historically speaking, people tried using existing mathematical machinery to solve these problems, okay? So I'll tell you historically

### 01:03:00 · Speaker 6

attempts were made

### 01:03:04 · Speaker 6

EMPDS attempts were made

### 01:03:11 · Speaker 6

to learn such functions.

### 01:03:17 · Speaker 6

using

### 01:03:19 · Speaker 6

classical tools, let me say it.

### 01:03:27 · Speaker 6

Let me give you an example

### 01:03:28 · Speaker 5

example for it. Let's take the example of speech, let's say, right? So the problem is that set of speech signal to we need to get into phone, right? That's what that's

### 01:03:40 · Speaker 5

That is what our goal is. So you know what people did? So they took the speech signal, okay?

### 01:03:48 · Speaker 5

they model speech signal, right? as basically you model speech signal as a linear or a non-linear system or non-linear system. This has some input, okay? And this is the system.

### 01:04:03 · Speaker 5

in LTI system you can either make it linear or non-linear

### 01:04:06 · Speaker 7

let's say that it's a linear system

### 01:04:09 · Speaker 7

And what you get back is the speed signal.

### 01:04:16 · Speaker 7

mixed. Okay. So this is the input to that system and this is

### 01:04:20 · Speaker 5

is the the speech signal that you observe. Okay? Now what they did is all you can measure is this the speech signal right this particular speech signal. They say that there is an abstract input which is the phoneme the idea of phoneme.

### 01:04:37 · Speaker 5

that person thinks of goes as an input to this system. And this system converts that into something that is measurable which is called a speech signal. Now if they want to you know find that underlying function okay. That would see remember that we are interested in

### 01:04:57 · Speaker 5

finding out the relationship between speech signal and the phoneme, not the other way around. Now what they do is they model the entire procedure, right, using some system. Okay. uh and then they cast it as an inverse problem. That is where the inverse problem comes into picture. That the problem is given the speech signal, find out what the underlying phoneme is. So now how do they do that? They do it by modeling this entire system using existing math. You know, for instance, the speech community was modeling this entire system as differential equations.

### 01:05:32 · Speaker 5

and find its parameters, you know, there are lots of parameter estimation techniques. So basically they cast this problem as, okay, I've given, I'm given some speech signal. Let me try to use some physics of the problem and try to estimate what the underlying system is, such that if I'm given a speech signal, I can go back to that abstract concept called phoneme. So you can see a similar thing with the images also, right? I mean the the classical image processing people, if they wanted to find out

### 01:06:02 · Speaker 5

gender, okay? from an image. So what they did, what they used to do is, let me take that another example of image, right? So you have image.

### 01:06:12 · Speaker 5

to let's say object identity, okay? So what sort of an object is it is what I need to find out.

### 01:06:20 · Speaker 5

given the image. So what do you do is that take the image, okay? So now model object identity as

### 01:06:27 · Speaker 5

let's say it's a house

### 01:06:30 · Speaker 5

If I see a rectangle

### 01:06:33 · Speaker 5

plus a triangle at the top, okay? And then you know some regular objects.

### 01:06:41 · Speaker 5

regular shapes.

### 01:06:43 · Speaker 5

and so on. So what do I do? I come up with processing methods, right? That would

### 01:06:49 · Speaker 5

find out. So basically what happens is this this function. So this function that they do is they first find out

### 01:06:58 · Speaker 5

So

### 01:07:00 · Speaker 5

rectangle extractor, there is something called, you know, just extract the rectangle and see where is it. And then you do a triangle extraction.

### 01:07:11 · Speaker 7

Okay

### 01:07:12 · Speaker 5

then you have some sort of

### 01:07:13 · Speaker 7

Hello

### 01:07:16 · Speaker 7

object location detection.

### 01:07:20 · Speaker 5

and so on and try to do this and combine all this to come up with some object identity or regular shape. Now that is how people used to attend these problems. This is a this is a as I said this is classical speed processing, this is classical email processing and you can imagine the same thing right you know in NLP also. You have documents to you need spam or no spam. Email spam or no spam problem right. So what people used to do is just identify some spam words.

### 01:07:55 · Speaker 5

Okay, so just count the frequency.

### 01:08:00 · Speaker 5

of spam words and so on. So now you do this and try to find a relationship between the spam number of spam spam words and the the frequency of occurrence and their position etcetera and then mark it to some identity. So you understood right? So basically if I have to track trace back to what what we discussed so far.

### 01:08:21 · Speaker 5

What we are actually interested in is given pairs of observations or elements from two particular sets. We are interested in finding out what the underlying relationship between the elements of those two sets are. Okay? Now, in classical settings, where the relationship between them can be can be estimated using existing mathematical tools, you can try to find out how the relationships are. I mean,

### 01:08:51 · Speaker 5

Don't ask me how to do it. I mean that's a that's an entire entire branch in mathematics by itself but you can do it. But now the problem arises where the the relation or the function that we are trying to learn between the domain and and range do not adhere with the existing mathematical tools.

### 01:09:09 · Speaker 5

Okay. Now I gave you examples of displacement learning. So why why does this happen? This happens typically where the elements of the domain set are measurable, okay, and observed. But the elements of the range set, okay, are very abstract and they are not measurable things. So now how do you solve such problems is the question. As I said, classically what people used to do is to try to use existing mathematical techniques, uh, and then find that relationship. But unfortunately, all these attempts, right? I mean, uh,

### 01:09:39 · Speaker 5

before people started using the probability theory or statistics as a tool to model these relations, none of these things were usable, right? I mean, you didn't have a good speech recognition system, you didn't have an image recognition system, didn't have a good NLP system because all the techniques that were there were simply estimating wrong functions, that's all.

### 01:10:03 · Speaker 5

Okay? None of the functions that you estimate, you know, what happens if you have a, I mean, suppose you have this particular way to find out what a house is, right? So what if you have a house which is a modern building, right? That does not have a triangle at the top, something like this. What do you do with it? What if it is disoriented? Similar questions can be asked for every system here. A sweet signal, suppose you model something, you know, somebody comes and the the the voice changes, you model

### 01:10:33 · Speaker 5

you have modeled it for one particular type of population and the accent changes so what happens you know those systems were failing there because the underlying function approximation that we have done there or the underlying function that

### 01:10:44 · Speaker 7

identified in these methods are not

### 01:10:52 · Speaker 7

Exactly

### 01:10:54 · Speaker 7

Okay, so this is the thing, right? So now I think, you know, I

### 01:10:59 · Speaker 5

they are convinced you enough uh in in in in

### 01:11:04 · Speaker 5

appreciating the fact that you need uh with the existing mathematical tools do not do not work out you need another uh maybe way or branch of mathematics right which would which would try to address these kinds of problems where you still want to approximate functions between two sets but the relationship between the domain and the range do not adhere to existing rules number one the second thing is that the uh the uh domain

### 01:11:34 · Speaker 5

that is often measured. The range that is not measured, not measurable. It's it's a it's a very abstract idea. Now how do you solve these problems is the question. And that's why probability theory or statistics becomes extremely relevant. I'll tell you what is the underlying paradigm of solving these problems in in in in from a probability theory perspective in a while.

### 01:11:56 · Speaker 5

Okay, so I'll stop here for a while and take questions. Avirup?

### 01:12:02 · Speaker 1

Yes sir. The example which you just gave that using traditional techniques like suppose you know the speech example which you gave that suppose it has been modeled using one in for a certain set of population it is not going to work with a different population if it has been modeled with the classical techniques but even with modern machine learning techniques we have observed the same behavior like if a model has been trained. Agreed agreed.

### 01:12:26 · Speaker 5

agree, agree, I'm not disagreeing at all, but the thing is, overall, right, empirically, the statistical may statistics based method have given you much, much better performance compared to these things. I mean, I'm not saying that this is, I mean, as people keep saying, no, all models are wrong, sorry, all models are wrong, but some are useful. So these have become more useful, right? More mainstream, more useful. If you have any metric that would measure the the goodness of these functions, okay?

### 01:12:56 · Speaker 5

which is the performance metrics. The functions that people have found out using statistical tools have shown better performance in terms of those metrics compared to classical techniques. That's all.

### 01:13:10 · Speaker 7

Thank you

### 01:13:10 · Speaker 5

But I'm not saying that okay, the statistics would solve the entire problem, it will give you the perfect function that is approximated, that's not what it is. But as I said, if you take any metric, I mean, we have seen this, right? uh what uh like uh the commercially available techniques do, right? I mean, all our phones have face recognizers, they do fairly well. There are problems, of course, but they do fairly well. All of them are running on ML, right? I mean, suppose you you want use classical techniques to do it, the generalization capabilities are rather poor for them.

### 01:13:46 · Speaker 5

Okay, Arijit

### 01:13:49 · Speaker 0

Uh sir, just the assumption I made, the example you gave for image classification like house or maybe spam, no spam, does did it fail because it is more of a rule based system than ML? Because we are directly identifying whether there is a rectangle or not, whether there is an square or not.

### 01:14:05 · Speaker 5

Exactly. Yeah yeah that's what I told you right? I mean what do you mean by rule based? uh What do you mean by rule based system? By rule based system I mean that you have found that approximated that underlying function using some rules.

### 01:14:07 · Speaker 0

Okay

### 01:14:16 · Speaker 0

Correct

### 01:14:17 · Speaker 5

right? And those rules are not the again let's not call them rules. I mean, see one other suggestion or rather request that I have is as we are as we'll be moving ahead in the classes, please okay, two things. One, don't try to force fit your already existing terminologies and knowledge in the class, okay? Because what happens is, you know, I'm I want to build it brick by brick and I at the end of this course, I want to

### 01:14:47 · Speaker 5

start using my language which is the language of ML community. So please try to use the definitions and the techniques that we have discussed in the class as much as possible that's one thing. The other request that I have maybe it's too early for it is but suppose I'm teaching you let's say adversarial networks or diffusions. Please don't ask questions on things that I have not covered in the class.

### 01:15:15 · Speaker 5

Okay. So because what happens is I'm sure that I mean what happens is in a in a large class like this, it will be too heterogeneous you see. So some of you might find this find some topics trivial, some of you might find some uh you know novelty there in some topics that I'll be teaching. So I have to cater to the average population you see. So that's why I have I will cater my lectures that way. But I do I mean encourage and request you to ask

### 01:15:45 · Speaker 5

as many questions as possible. But, uh, please don't ask me questions on topics that I have rather not, uh, covered yet, right? Or rather going to cover later. And also, as much as possible, use the terminologies that have been developed in the class. Okay, for instance, the reason I remembered all this is, I mean, again, uh, you know, nothing particular to you, Arijit, because I just remember, I anyway had to say this because it came up, I just said. For instance, uh, see, there is no rule

### 01:16:15 · Speaker 5

Now we have been talking about functions, define what functions are, okay? So what we are doing here in the classical techniques is that we are learning these functions or rather we are finding out these, I mean I have never defined this word learning, I'm sorry. So we are finding out these functions, right? Using pairs of observations. Now why do they fail is because the function that we have thought that is the correct function is not the correct.

### 01:16:43 · Speaker 6

Now there have been enormous amounts of

### 01:16:52 · Speaker 6

Send

### 01:16:52 · Speaker 5

is that okay somebody said that no no no if you want to look at human faces don't look at these these rectangles in fact you can go even one step below okay where

### 01:17:05 · Speaker 5

I mean, see, what do you mean by a rectangle? I mean, I just took this as granted. What do you mean by rectangle? Rectangle is you should have four line segments that are perpendicular to each other and so on. So now how do you find out perpendicular line segments? You have to do what is called as edge detection there, right? Given an image, you'll have to detect the edges and what if there are multiple edges in the image, how do you deal with it and so on. That's why you have these classical image processing techniques, right? Where people look at stuble filters, different kinds of operators to do edge reduction and then came these wavelet transforms, etcetera. So basically,

### 01:17:35 · Speaker 5

they are asking this fundamental question, right? What is the underlying function that I have to find such that I can relate these two sets that I have at hand? And because these functions that people have come up with, they are not correct in the sense that they don't predict the correct correct element in the range set, they are failing.

### 01:17:56 · Speaker 5

Okay. Now the question, the bigger question is what other way can one think of when we need to relate these two sets? That is the question. That we'll answer in a while.

### 01:18:08 · Speaker 5

ओके शिवम

### 01:18:11 · Speaker 3

Uh yes sir, I think you have partially answered to my question but yeah, again to understand when we do a function approximation for any particular input, how do we come to a point like we we do an experiment and we say that okay, this function is not working well for this particular input and we try to increase the complexity by increasing the number of parameters or trying out different approach. But is there any initial study which shows that it's a good start uh that we should take these number of parameters and try this particular approximation? technique for this particular input or it just on the trial basis we do

### 01:18:47 · Speaker 5

Hello

### 01:18:49 · Speaker 5

Yeah, see that is more of yeah, there is no uh there are a few techniques, right, where okay, there are see for instance, neural networks is one large class of functions that you can try out which are universal function approximators, see.

### 01:19:05 · Speaker 5

Right? So that is why neural networks are so popular. We'll come to that in a while. So why are neural networks so popular is because the functions that that these neural networks approximate, right? are a large class of functions. So now instead of trying out different, so let's say you try out a parabola, you try a third degree polynomial, you try an nth degree polynomial, etcetera, these neural networks are class of functions that can approximate any function to arbitrary closeness. So that's why you can try neural networks. In fact, that is the reason why they are they are so popular.

### 01:19:35 · Speaker 5

popular these days, right? They are universal approximators. Yeah. Okay, so basically, yeah, so the the motivation is that, right? I mean, when you cannot have uh like off-the-shelf functions or rather classical functions, uh that would match, that would relate these two sets. You need a different kind of paradigm to model these two and that's why probability theory becomes a handy uh thing, you know, in fact, I should tell you something. So,

### 01:20:05 · Speaker 5

mid nineteen eighties. uh people were trying to solve this uh this uh speech recognition problem and a lot of speech scientists they used to model okay in fact they used to model the entire uh vocal apparatus as concatenation of several wave guides. So wave guides you know what wave guides are right? you know they are physical cavities where electromagnetic waves travel. They used to model the entire uh the vocal apparatus starting from lungs to mouth as concatenation of several wave guides.

### 01:20:35 · Speaker 5

it's with different uh uh diameters and lengths. So now the the when the shape of the wave changes right? The way the wave propagation happens through that changes. So those were using those were being modeled as several differential equations with several initial conditions and so on. People have spent decades doing this. Now the idea was that okay if you can like model those things uh using physics then you know what sound produces what sort of a signal and so on.

### 01:21:05 · Speaker 5

But I think you know nineteen nineteen late nineteen eighty either it's either IBM or Bell Labs I don't remember which one of it they demonstrated that using statistical methods those days they were hidden Markovian models which are nothing but ML models right I mean using statistical methods they actually demonstrated they cracked the problem of isolated word recognition where they are not it's not speech recognition if you say an isolated word with limited vocabulary they could

### 01:21:35 · Speaker 5

identify that, okay? So people from this classical physics, right, they got so irritated that they said that all that you are doing is, you know, modeling your ignorance. This was actually said, this is documented. They said that oh, because you don't know how speech signal is related to phoneme and you cannot use the first principles and physics, you are simply, you know, modeling the ignorance that you have and these things were actually called ignorance models those days and people were very

### 01:22:05 · Speaker 5

against these these kinds of statistical models. But come to those in tens, right? uh We have seen that these kinds of problems can be very easily modeled uh using statistics and probability methods, okay?

### 01:22:21 · Speaker 5

Okay, so I think let us take a short break. It is ten forty now in my clock. Let's get back at eleven a.m. So what we will do next is I'll I'll tell you like how is this problem solved using the probabilistic methods and we'll start defining what probability spaces are and you know what a probability measure is and distribution functions and so on. Okay? So we are resuming in about eighteen

### 01:22:47 · Speaker 6

20 minutes. See you in a while.

### 01:44:31 · Speaker 6

Hello

### 01:44:33 · Speaker 6

should be resumed

### 01:44:37 · Speaker 7

sure sir

### 01:44:37 · Speaker 6

Sure sir

### 01:44:44 · Speaker 6

Okay. So, yeah, so we were talking about

### 01:44:49 · Speaker 5

function approximation. So we want to find functions, right? Even pairs of elements from the domain and range and we saw that in in some of the scenarios, finding out these relationships are non-trivial. So need different kinds of approach for it. So, it is motivation, right?

### 01:45:10 · Speaker 7

So what is done in this branch called probability, probability theory?

### 01:45:21 · Speaker 7

the first

### 01:45:22 · Speaker 6

Hello

### 01:45:23 · Speaker 7

situation that is done, I mean rather first

### 01:45:26 · Speaker 7

that is made is

### 01:45:28 · Speaker 7

Right

### 01:45:30 · Speaker 7

vaguely right so what happens is um

### 01:45:35 · Speaker 7

sort of human decisions of it and have to write that. So basically what is said is

### 01:45:42 · Speaker 6

Hello

### 01:45:46 · Speaker 6

Uncertainty

### 01:45:52 · Speaker 6

by construction.

### 01:45:57 · Speaker 6

Okay, so

### 01:45:58 · Speaker 5

What do I mean by this? Now this is actually a striking uh difference between the deterministic way of looking at things and problemistic way of looking at things is that so in probability theory, right? uh The models and the and the ideas are built by inherently allowing uncertainty in in in all your functions. What do you mean by that? See look at this. Suppose we want to solve this problem, right? This problem of gender, okay, given a picture.

### 01:46:28 · Speaker 5

Now, I don't have to tell you, so given every picture, I don't have to tell you whether this picture belongs to a man or or a woman, right? Most of the times our our job will be done if I tell you that look, this picture has about seventy percent of chance of belonging to a man.

### 01:46:51 · Speaker 5

and we are okay with it, right? And we'll go ahead with those decisions. Isn't it? So, uh another example that can be given is if you look at this emotion as well. So instead of saying that this particular document correspond to one of these emotions, what if I tell you that these these documents, they okay, given a particular document, I'll say that okay, this document has thirty percent chance of being sad and twenty percent chance of being angry. percent chance of being happy and so on. That's enough for most of the

### 01:47:27 · Speaker 5

task that we are supposed to do. So basically, uh this is the idea that

### 01:47:35 · Speaker 5

saying that I mean observing that uncertainty is okay, right? I mean basically

### 01:47:42 · Speaker 7

over the functions

### 01:47:44 · Speaker 6

okay, that we are interested in.

### 01:47:49 · Speaker 6

which are mappings from the range and the

### 01:47:56 · Speaker 6

mappings from domain to to range, okay?

### 01:48:04 · Speaker 6

can have, can possess

### 01:48:09 · Speaker 6

Uncertainties

### 01:48:15 · Speaker 7

See, now I think, you know, this

### 01:48:17 · Speaker 5

commentator makes sense, right? prediction. So what you are actually doing is given a particular element in the domain, what you are telling me is that you are telling me what is the chance of that particular element from the domain, maps to different elements.

### 01:48:33 · Speaker 6

range

### 01:48:36 · Speaker 6

Siri Point

### 01:49:11 · Speaker 6

sorry I was muted I didn't notice that.

### 01:49:13 · Speaker 5

So what I'm saying here is that uh in probability here inherently what is done is the functions that we are that we are trying to learn between two sets right they can possess uncertainties by construction. Now why is this why is this important or why is this a good thing is because as I said if you if you allow for uncertainties right then what

### 01:49:37 · Speaker 7

happens is through uncertainties

### 01:49:45 · Speaker 6

following for uncertainty it is one

### 01:49:50 · Speaker 6

makes

### 01:49:57 · Speaker 6

makes function learning easier

### 01:50:08 · Speaker 6

it makes the functional learning a little feasible, right? Because

### 01:50:11 · Speaker 5

See, you are if you are giving me more freedom, it's it's like actually giving the model, I mean or rather the paradigm more freedom in the sense that I don't care if you if you are going to tell me what exactly is the element from the range set that gets that gets mapped to this particular element in the in the domain set. But I only care whether I mean if you if you tell me what are the chances of this particular member in the the the

### 01:50:41 · Speaker 5

domain of getting map to a particular member in the range act. So now I mean one might think that okay I mean if you do not have the I mean if if if this uncertainty is there inherently in the model it can be a negative thing right because if I I mean decisions are deterministically taken either you go somewhere not go somewhere either you eat something not eat something how can I have an answer

### 01:51:11 · Speaker 5

alternity associated with my decision. It turns out that these these functions that are in lot of the use cases as I said it is okay if I give you some odds of this particular member in the domain set getting back to.

### 01:51:28 · Speaker 5

different members in the range. And I gave you examples on that. So you know for this male female uh classification task or rather mapping task, it's enough if I tell you that okay this picture has seventy percent of chance of belonging to a male. Lot of times what happens is we take we take chances and risks in life, right? I mean that is the idea. So you inherently allow uncertainties by construction in the model. You have uncertainties, makes functionally infeasible, this is one thing. The other another thing that is relevant to this particular course is that if you allow uncertainties right this will

### 01:52:06 · Speaker 7

will help

### 01:52:09 · Speaker 7

Creativity

### 01:52:15 · Speaker 7

is too philosophical but think about it. I mean I'll concretize all these ideas in a while.

### 01:52:20 · Speaker 5

but think about it. uh if we are set on stone right if we are uh if we are deterministic about everything that we do. if we don't take risk as they say. uh then you are stuck you can't be creative if you don't take risk. so creativity. see for instance right while when people when when artists write portraits.

### 01:52:45 · Speaker 5

okay, of people or landscapes that that that do not exist.

### 01:52:50 · Speaker 5

What's actually happening is that there is a certain their model of of of of human faces, right? That has a certain uncertainty associated with it. Without that uncertainty that is associated with that, there is no way that this artist is creating a new uh image or rather new picture of a human being that does not exist. You understand? So now, if the model inherently or rather the function or the paradigm allows for uncertainty by construction,

### 01:53:20 · Speaker 5

one makes this function learning feasible because there are more degrees of freedom, okay? And two, it will help creativity and that's why, right? I mean, generative modeling was possible only through problematic paradigms. I I will define all this concretely, but think about it. Now, all the while the problem was that if you are given elements from the domain and the range set, you want to find a function that would map every element in the domain, every element in the range set. Now, if you

### 01:53:50 · Speaker 5

no uncertainty what happens is that you can create more elements from the domain set and you can create more elements from the range set. That is what genetic modeling is all about right at some level. So this is what it is.

### 01:54:03 · Speaker 5

So this is the paradigm where

### 01:54:09 · Speaker 5

the functional learning, right? And the uh the approximation that you do for these functions, you allow for uncertainty, the presence of uncertainty by construction. Okay? uh Okay, so any questions on this before we concretize these ideas?

### 01:54:28 · Speaker 5

So what do I mean by allowing uncertainty? How do you do it actually is something that I that I'm going to talk about in a while. But yeah.

### 01:54:35 · Speaker 7

Before that, in the philosophical idea, any questions?

### 01:54:46 · Speaker 7

Sir, here domain range means the input values.

### 01:54:53 · Speaker 5

Please raise the hands before you talk, okay? I'll call out your names. Yes, Karthik.

### 01:55:02 · Speaker 2

So, previously we used to say in function some exceptions, right? Not uncertainties, right? Like generally

### 01:55:10 · Speaker 5

No no no no no. See mathematically looking at it, there is nothing called exception. There is a domain set, there is a range set, there is a function that maps elements from here to elements from there.

### 01:55:21 · Speaker 2

Okay

### 01:55:22 · Speaker 5

So there is no idea of exception, right, in deterministic functional learning.

### 01:55:27 · Speaker 2

Okay, yeah.

### 01:55:28 · Speaker 5

Isn't it? So like you know F equal to MA F equal to MA that's all. There's no no exception per se.

### 01:55:29 · Speaker 2

like

### 01:55:36 · Speaker 5

Oh yeah

### 01:55:36 · Speaker 2

No, yeah, there can be scenarios like what we say, right? When F equal to MA, but given that mass is constant. If mass is not constant, that's an exception to this. So, something like that.

### 01:55:46 · Speaker 5

Well, well, it's not really because see when if you if you make mass not a constant or whatever the conditions are, then the domain and the range set completely changes, you see. As far as the domain and ranges are fixed, right? It's a deterministic function. No, there is there is no inherent uncertainty in the model per se or the function.

### 01:55:57 · Speaker 2

Saffron

### 01:56:01 · Speaker 2

Okay

### 01:56:09 · Speaker 7

Okay, sure.

### 01:56:10 · Speaker 5

Right? Yeah. Aditya,

### 01:56:10 · Speaker 7

Right

### 01:56:11 · Speaker 7

Yeah

### 01:56:15 · Speaker 4

So one rather comment not a question is that if there is an inherent uncertainty in the system, we cannot use these kind of systems to make any control decisions or any any any such decisions, is that correct?

### 01:56:33 · Speaker 5

That is why right now people are skeptic about using these stack GPTs for all this.

### 01:56:40 · Speaker 5

See, why do you think people are talking about explainability and safety, biases of T system? Just because they are probabilistically built.

### 01:56:48 · Speaker 4

Mm-hmm

### 01:56:49 · Speaker 5

Right? So that's why people are talky about these things.

### 01:56:50 · Speaker 4

Okay

### 01:56:54 · Speaker 4

Got it. And uh one more observation on on when we say functions, right, functions are well defined which maps each input to its outputs, right? If you look at F is equal to M A.

### 01:57:05 · Speaker 1

If you look

### 01:57:07 · Speaker 7

So,

### 01:57:07 · Speaker 4

So when when we talk about these n-dimensional functions with parameters which are in billions.

### 01:57:13 · Speaker 7

Hmm hmm

### 01:57:14 · Speaker 4

is that something which is I can't visualize that how that that function is going to look like.

### 01:57:22 · Speaker 5

Well you can't I mean because human beings can't visualize anything beyond three dimensions. So you can't visualize those functions correct. Yeah but you I mean you can imagine functions right that would take billion dimensional vectors as inputs and gives you a scalar. That's very much possible.

### 01:57:41 · Speaker 7

Okay

### 01:57:42 · Speaker 5

right? But of course, those functions cannot be visualized because you can't, we can't visualize as human beings beyond three dimensions. That's, that's there.

### 01:57:51 · Speaker 7

Okay.

### 01:57:53 · Speaker 5

Yeah, so now let's come to this point that how do you allow uncertainty by construction? That's the point. Now the first thing that is done is, see remember that we had sets, right? I mean set A, the way we called it is that

### 01:58:09 · Speaker 5

you know X I all the observations that we make you know X one X two all these observations that we make which are the elements from the domain. The first thing that is done is now each of these observations are the sets that we look at okay.

### 01:58:28 · Speaker 5

Now there is uh

### 01:58:32 · Speaker 5

Now these vectors, let's say, let's say that these are

### 01:58:36 · Speaker 5

some D dimensional vectors. These can be D dimensional vectors. Now these are

### 01:58:42 · Speaker 5

in the probabilistic sense, right? These become, these become what are called as

### 01:58:48 · Speaker 6

in stations

### 01:58:54 · Speaker 6

of a random variable

### 01:59:03 · Speaker 6

So these no longer

### 01:59:04 · Speaker 5

number are vectors. Okay? Now they are not just seen as you know points in some d dimensional space. They are seen as instantiations of a random variable. Now what is this random variable business? Now the way the probability theory structure is following. So it all starts with probability theory.

### 01:59:26 · Speaker 7

it starts with something called a random experiment.

### 01:59:31 · Speaker 7

random experiment or random trial

### 01:59:37 · Speaker 5

please pay some attention here. Okay? So it says that there is a random experiment or a trial that is happening. Okay? uh Why is it called a random experiment? uh

### 01:59:49 · Speaker 5

This is one thing that is not very defined in the probability theory, right? There is what do you mean by random? Nobody knows. But there is an experiment that is happening and these

### 02:00:00 · Speaker 4

gave rise to what is called as outcomes.

### 02:00:05 · Speaker 4

basically these are the outputs or rather outcome

### 02:00:08 · Speaker 3

of these random experiments and these outcomes okay are

### 02:00:13 · Speaker 3

enumerated in a set

### 02:00:17 · Speaker 3

set of outcomes.

### 02:00:22 · Speaker 3

actually critically

### 02:00:23 · Speaker 4

important that all of you understand is not very difficult but please follow me and understand what he's saying. So it begins with random experiment. And the outcome of uh sorry the yeah the uh the observations of these random experiment is enumerated in a set of outcomes.

### 02:00:43 · Speaker 4

And this is called

### 02:00:44 · Speaker 3

the sample space

### 02:00:52 · Speaker 3

Don't worry about the terminologies now

### 02:00:54 · Speaker 4

But

### 02:00:56 · Speaker 4

What do you mean by set of outcomes? uh It is simply enumerating, right? uh Or uh just listing down all the possible outputs of a random experiment. Now what is a random experiment?

### 02:01:10 · Speaker 4

Anything that you that you want to model right now becomes a random experiment. Let me give you an example. Let's say that let's take the example of I don't know why this suddenly gives me some weird shapes example. Let's say that we have images right.

### 02:01:29 · Speaker 4

Okay, so even before coming to that,

### 02:01:31 · Speaker 2

Let's take easy examples. Now a random experiment.

### 02:01:38 · Speaker 2

can be tossing a coin. I mean all of you know this.

### 02:01:42 · Speaker 2

Off

### 02:01:47 · Speaker 4

Tossing a coin is a random experiment. Okay? Now what are the questions that you are interested in? Like I want to know when I toss the coin hundred times, what are the odds that like how many times does the coin turn out to be head or something. Those are the kinds of questions that I'm interested in. But random experiment is simply tossing a coin. Now what is the sample space here? What are the possible set of outcomes? Possible set of outcomes are head and tail. Okay? Assuming that the coin has two faces. So this is one example of a random experiment. Now another example can be like can people can tell me what it is or you can

### 02:02:24 · Speaker 3

and roll a die

### 02:02:26 · Speaker 3

to Lenin faced die

### 02:02:31 · Speaker 3

Now the sample space

### 02:02:33 · Speaker 4

that the case would be so one two whatever possible outcomes that are up to n

### 02:02:40 · Speaker 4

So you got an idea of what is a random experiment, right? I mean anything, uh an experiment that is being performed and is called a random experiment. And the possible outcomes of that random experiment is just enlisted in a in a set, okay, which is called the sample space.

### 02:02:59 · Speaker 4

Now, when we

### 02:03:02 · Speaker 4

Get to the

### 02:03:05 · Speaker 4

We are not interested in rolling the dice or tossing a coin, we are interested in looking at an image and finding out whether it's a man or a woman, right? So now, um

### 02:03:15 · Speaker 2

um

### 02:03:17 · Speaker 2

taking a picture

### 02:03:23 · Speaker 2

of a person

### 02:03:27 · Speaker 2

is a random experiment. Can you visualize taking a picture of a person as a random experiment?

### 02:03:35 · Speaker 4

Let me tell you what I mean by this. Now imagine that you know you can uh there are there are there are infinite people uh that that are there, right? And you taking a particular sensor and shining light on a particular person and measuring the reflectance of that particular person becomes a random experiment. Now what is the sample space? Can somebody tell me what would be the sample space?

### 02:04:05 · Speaker 6

the same picture can never repeat twice so

### 02:04:09 · Speaker 4

No no no, I'm simply asking what is the sample space. Okay, so let me just go back to definition. What is sample space? Sample space is simply the enumeration of all possible outcomes of a random experiment. Okay?

### 02:04:09 · Speaker 6

No, no, I'm saying

### 02:04:13 · Speaker 3

Let me

### 02:04:13 · Speaker 0

number

### 02:04:16 · Speaker 3

small pixel value combination

### 02:04:27 · Speaker 4

Now, uh, the example, right? In tossing a coin, the head tail are the sample space. In rolling an enface die, the one, two, three, etcetera, N are the uh, sample space. Now, if you take a picture of a person, what is the possible sample space? Yeah, I think

### 02:04:41 · Speaker 3

All performance numbers

### 02:04:43 · Speaker 6

male, female and baby cousin name. All pixel combination.

### 02:04:47 · Speaker 0

male, female and third gender

### 02:04:50 · Speaker 4

No, it's not that. Because I'm talking about

### 02:04:52 · Speaker 0

All people of

### 02:04:54 · Speaker 4

Yeah, so it's actually, uh I'll write it as person one, person two, person three, and if there are whatever, right? If you have like, uh let's say seven billion people in this world, you have seven billion possible outcomes.

### 02:05:11 · Speaker 4

Can you see this? So basically this is the way you are modeling it, you understand? So now the random experiment that is happening is simply taking a picture, okay? of a person is a random experiment. It's simply like rolling a die. I mean when I see this is the world view that you should slowly develop uh when you when you are dealing with machine learning that

### 02:05:33 · Speaker 4

reading an image from one of these open CV libraries or something is nothing

### 02:05:38 · Speaker 4

different than tossing a coin in the probabilistic sense of words. Okay? So now that's why I wrote the sample space, right? I mean, there are these many people, every person now becomes the sample space. And and similarly you can imagine, right? I mean, now suppose I'm

### 02:05:56 · Speaker 3

recording speech.

### 02:06:06 · Speaker 3

according to speech signal, what happens is that every possible sentences that everybody in this world can talk of becomes a sample space.

### 02:06:18 · Speaker 3

understand?

### 02:06:21 · Speaker 3

Okay. Any questions on what is what constitutes a random experiment and what are sample spaces?

### 02:06:33 · Speaker 2

Okay

### 02:06:33 · Speaker 3

Now what happens

### 02:06:35 · Speaker 4

happens is that when we when we measure, right? And when we have a sensor and you know, we or we have a we have a condenser microphone, we measure it. What we get to measure are not the elements of sample space. So let me write that. So elements

### 02:06:56 · Speaker 4

maybe before coming there let me just define the probability measure. Okay so this is the sample space. Now

### 02:07:05 · Speaker 4

What so now this is a set okay? Now um let me give you an example let's say that I have set of real numbers which are

### 02:07:18 · Speaker 2

Yeah

### 02:07:18 · Speaker 3

simply take set of real numbers.

### 02:07:26 · Speaker 2

set of real numbers

### 02:07:29 · Speaker 2

hmm

### 02:07:30 · Speaker 2

quality

### 02:07:30 · Speaker 2

R

### 02:07:32 · Speaker 3

Now

### 02:07:33 · Speaker 3

I take

### 02:07:34 · Speaker 4

subject

### 02:07:36 · Speaker 4

let me call it

### 02:07:38 · Speaker 4

used this already. I'll run out of notations very quickly. So let let me call it A one is a subset of real numbers. Okay? And A two is another subset of real numbers. So for example, this can be zero to two, okay? This can be

### 02:07:57 · Speaker 4

three to eight. These are two subsets of real numbers, right?

### 02:08:02 · Speaker 4

See my interest numbers.

### 02:08:04 · Speaker 4

I want to compare these two sets. How do I compare these two sets? Okay, so let's say that

### 02:08:09 · Speaker 2

the intent

### 02:08:15 · Speaker 2

Compare

### 02:08:20 · Speaker 2

A one and A two which are both subsets of R.

### 02:08:25 · Speaker 4

I'll tell you what is the relevance of this with sample space in a while but yeah so let me take some like opinions here. If I have subsets of real numbers how do I compare subsets of real numbers?

### 02:08:40 · Speaker 0

maybe what is the common numbers between two sets

### 02:08:46 · Speaker 3

Okay, so

### 02:08:47 · Speaker 4

how does how does that how does that tell me uh how anything about these two sets?

### 02:08:56 · Speaker 4

Okay, so I'll tell you what do I mean by comparative

### 02:08:59 · Speaker 3

want to I want to ask questions like which one is

### 02:09:05 · Speaker 3

bigger

### 02:09:08 · Speaker 3

and a smaller

### 02:09:13 · Speaker 3

something of this sort. So how do I do that? I think people have raised their hands. Harsha,

### 02:09:20 · Speaker 6

Yes sir. So one way to compare is like if you are able to map each element in this set to another element in the other set we are comparing and if we are able to map

### 02:09:31 · Speaker 4

I can't, no, I can't because here I can't find a function that would, are you saying that I have to find a function that would map the elements in set A one to A two? See again, when I say compare, right? I mean, please take this the question, you know, I want to know which one is bigger and which one is smaller.

### 02:09:52 · Speaker 4

You all know the answer to this question but I just want to hear from you. uh Yeah, Nirmith.

### 02:09:58 · Speaker 6

finding the cardinality of the sets.

### 02:10:04 · Speaker 4

Both of these sets have infinite cardinality, no? These are subsets of real numbers. Cardinality of both of these are infinity, isn't it?

### 02:10:15 · Speaker 4

You see that in numbers. Because these are subsets of real numbers. So cardinality won't give you anything. If it's a discrete set of course, but it's a it's a subset of real numbers, cardinality won't help.

### 02:10:17 · Speaker 3

Because three

### 02:10:26 · Speaker 2

Okay, Vivek

### 02:10:32 · Speaker 2

விவேக்

### 02:10:37 · Speaker 3

ओके बालाजी

### 02:10:40 · Speaker 3

Sorry

### 02:10:41 · Speaker 3

can find like mean median

### 02:10:43 · Speaker 3

something like that.

### 02:10:46 · Speaker 4

How does taking me tell you which one is bigger and which one is smaller?

### 02:10:51 · Speaker 3

but there are only

### 02:10:51 · Speaker 4

there are only it's a set you understand that it's a set no? So there are infinite numbers. So how do you take mean of infinite numbers?

### 02:11:00 · Speaker 4

See there are infinite elements in the in both of these sets. Does all of you agree with that? You can respond with a emoji or something, right? Does all of you agree that there are infinite numbers in both these sets? The cardinality of both these sets are infinity. So the average doesn't make sense here. I just want to know if if you can tell me which one is bigger. Right that's all. Maybe I'll make the question easier, right? To tell me which one is bigger. Okay. So let's ask me this let's ask this question. Which one is bigger in these two sets?

### 02:11:30 · Speaker 4

Aditya and by the way when I ask you a question right and when you when you raise your hands to answer I would randomly call out names okay so please don't take it otherwise if we I mean when I ask you I mean if there are any questions then I'll go one by one when I ask you questions then I'll just take random order okay so here is the question the question is which one of these two is bigger Abhirup

### 02:11:55 · Speaker 5

if we apply the length measured then the set on the right hand side seems to be bigger

### 02:11:57 · Speaker 6

length measure

### 02:12:02 · Speaker 4

ओके, व्हाट कैन यू एक्सपैंड दैट? ओके, लेट्स से यूज़ दिस वर्ड मेजर।

### 02:12:08 · Speaker 5

Yeah

### 02:12:09 · Speaker 4

What do you mean by that? That's exactly where I'm coming to.

### 02:12:13 · Speaker 5

So

### 02:12:14 · Speaker 4

You said length measure, what is length measure?

### 02:12:15 · Speaker 5

length length measure is a function which maps the number of sigma algebras in a set to a number

### 02:12:24 · Speaker 4

that you seem to know things. So now I didn't talk about sigma l by h. Okay? So, uh yeah, so yeah, what is what is the measure? So basically what he is saying is, just look at the length of these two sets.

### 02:12:39 · Speaker 4

Okay so now you represent these two set the I mean the the these two sets on a on a number line. So this is zero to two and this is three to eight.

### 02:12:52 · Speaker 4

Okay, now this

### 02:12:54 · Speaker 2

line has a

### 02:12:56 · Speaker 2

higher length

### 02:13:01 · Speaker 2

compared to this lens, this line, correct?

### 02:13:07 · Speaker 2

Does all of you agree?

### 02:13:10 · Speaker 4

Well if you agree with this right? I mean so basically what we are saying is that associate how do you generalize this idea? associate okay?

### 02:13:12 · Speaker 3

Basically what

### 02:13:20 · Speaker 4

A scalar positive

### 02:13:21 · Speaker 2

function

### 02:13:26 · Speaker 2

அதுக்கு நான் ஜீரோ ஃபங்க்ஷன்

### 02:13:34 · Speaker 2

with every subset of R

### 02:13:42 · Speaker 2

Basically given

### 02:13:45 · Speaker 2

subset A

### 02:13:47 · Speaker 4

of R, what I do is I take that subset and associate that with some number, okay?

### 02:13:56 · Speaker 4

which I call as

### 02:13:58 · Speaker 3

μA

### 02:14:01 · Speaker 3

Okay? Which is

### 02:14:07 · Speaker 3

a positive real number between zero and

### 02:14:12 · Speaker 3

that it's simply a positive real number. Okay? I can actually say it has belong to R plus.

### 02:14:21 · Speaker 3

confused with notation it's a it's a non

### 02:14:25 · Speaker 2

Zero

### 02:14:29 · Speaker 2

Real number

### 02:14:31 · Speaker 2

one zero

### 02:14:34 · Speaker 2

It can be zero also

### 02:14:37 · Speaker 2

See, it does itself.

### 02:14:43 · Speaker 2

non negative real number. Yeah, that's what it is.

### 02:14:50 · Speaker 2

You understand? So what we are doing here is

### 02:14:52 · Speaker 4

that for every subset of real numbers we are associating a non negative real number okay which would which I call as

### 02:15:05 · Speaker 3

Anyway, this is defined as measure of A.

### 02:15:14 · Speaker 3

Do you understand? Now basically let's abstract out. So we are given

### 02:15:19 · Speaker 4

a set, okay, which is set of real numbers. And we are taking subsets of these this set. And corresponding to each of the subset of this set, I associate a non-negative number and I call it the measure.

### 02:15:33 · Speaker 4

Does it make sense? So basically what does measure do is that measure

### 02:15:40 · Speaker 4

is basically

### 02:15:40 · Speaker 2

a function that would take a subset of a given set. Okay? And maps it to

### 02:15:55 · Speaker 2

non-negative real numbers. Do you understand? So this is a measure.

### 02:16:00 · Speaker 4

So now why is this important is that

### 02:16:03 · Speaker 4

given every any subset of given set, okay? Now you can compare sets based on their corresponding measure.

### 02:16:13 · Speaker 2

the facilities

### 02:16:19 · Speaker 2

comparison

### 02:16:25 · Speaker 2

four subsets

### 02:16:29 · Speaker 2

Let me give you another example. Let's say that our set

### 02:16:33 · Speaker 4

is set of

### 02:16:36 · Speaker 4

are two which are you know two dimensional vectors.

### 02:16:38 · Speaker 3

Okay

### 02:16:40 · Speaker 3

What can we so which

### 02:16:41 · Speaker 3

means that an element here right an element in R two

### 02:16:51 · Speaker 3

is represented as x one comma y one

### 02:16:56 · Speaker 4

Let me call it X1, X2

### 02:17:00 · Speaker 4

which is I write it as capital X which is X one comma X two. Okay this is an element. Now suppose I give you okay so now tell me a measure that you know of that is defined on R two.

### 02:17:16 · Speaker 3

measure on R two. You people already know this.

### 02:17:20 · Speaker 6

root of x square plus x two square

### 02:17:20 · Speaker 3

Protect

### 02:17:21 · Speaker 2

Test

### 02:17:21 · Speaker 3

Krishnan

### 02:17:23 · Speaker 4

Come again

### 02:17:25 · Speaker 6

magnitude root of x one square plus x two square that can be used to

### 02:17:31 · Speaker 4

Yeah, but that's an element, right? I'm talking about a subset. If I take a subset of R two, okay.

### 02:17:36 · Speaker 3

Om

### 02:17:37 · Speaker 4

Sick

### 02:17:37 · Speaker 3

remember that measures are defined on subsets.

### 02:17:47 · Speaker 3

See, in R1 what happened? We represented every subset as a line segment.

### 02:17:53 · Speaker 4

Okay, so now if I write R2

### 02:17:57 · Speaker 4

How are each subsets represented here?

### 02:18:00 · Speaker 6

Areas

### 02:18:01 · Speaker 4

Our in subsets represented

### 02:18:02 · Speaker 6

Power

### 02:18:03 · Speaker 6

rectangles

### 02:18:05 · Speaker 4

Yeah, there can be it can be any uh irregular shape, it doesn't matter. But for now, yeah. So this is a subset, right? A subset in R two, okay? Now what can be a measure that you already know on subsets of R two?

### 02:18:05 · Speaker 3

coordinate

### 02:18:24 · Speaker 3

area measure

### 02:18:29 · Speaker 3

understand? So every subset has a measure called area, no?

### 02:18:33 · Speaker 3

Okay? Now if you extend this

### 02:18:35 · Speaker 4

through a D-dimensional real space, what is the measure?

### 02:18:40 · Speaker 6

Volumes

### 02:18:42 · Speaker 3

only

### 02:18:42 · Speaker 4

their volumes, right? I mean they are hyper volumes. You can't call them volumes, they are hyper volumes. So this measure that we know of, right? Which is, you know, which is length in one dimension, area in two dimension and hyper volumes in three dimension, it has a name. Do you know what the name for this measure is?

### 02:19:00 · Speaker 4

Does anybody know the name of this measure? See there can be this is not the only measure that that you can have, you see. Given subsets of any sets you can come up with any measure. And there's a definition of measure, right? Okay, that if you have a if you have a set with zero cardinality, the measure has to be zero. So if you have two non-overlapping subsets, the measures have to add up.

### 02:19:20 · Speaker 4

the the the measures of the individual uh subsets has to be equal to the measure of the union of those subsets. Okay? So these are some of the properties that the measure should have. But anyway, you can come up with multiple measures. Actually, you can come up with your own measure and give it your name, doesn't matter, as long as these properties are satisfied. But the usual uh length, area, volume measures that we know of, right? That we use that we have been using since class five. There's a name for this measure.

### 02:19:32 · Speaker 6

half

### 02:19:50 · Speaker 4

you know what the name for this measure mean is

### 02:19:55 · Speaker 0

norm

### 02:19:56 · Speaker 3

So, these are called Lebesgue measures.

### 02:20:03 · Speaker 3

I don't know why his name is

### 02:20:04 · Speaker 4

is is spelled like this but yeah so this is called Lebesgue measure. So all the length area etcetera that we do in Cartesian or rather Euclidean spaces right D-dimensional Euclidean spaces they are called Lebesgue measures. So the length area and volume measures.

### 02:20:22 · Speaker 4

Is this idea clear? Why am I talking about measures here? There's a reason for it. I'll just just give me a while I'll I'll come to that. So now you understood what measures are, right? So basically what I'm doing is that I'm given a set, okay? I'm constructing

### 02:20:37 · Speaker 4

the subsets of that particular set.

### 02:20:41 · Speaker 4

Okay? Now for every subset that I'm constructing on this particular set, I'm associating a number with it. And that number is what I'm calling as a measure. And we just saw an example of a measure in d-dimensional Euclidean spaces and we called it as

### 02:20:57 · Speaker 2

Labrador

### 02:20:58 · Speaker 2

Any questions, Prabhupada?

### 02:21:13 · Speaker 2

Hello, am I audible? Are you there?

### 02:21:16 · Speaker 5

Yes sir

### 02:21:18 · Speaker 4

Okay. uh Yeah, there are a few questions. Lokesh Kumar.

### 02:21:22 · Speaker 6

Yes, sir, is there a reason why the measure has to be a positive?

### 02:21:27 · Speaker 4

Good question. It's by definition. See the thing is, because we perceive measures as you know something that is that we can compare. So we can't compare negative numbers you see. We can only compare positive numbers.

### 02:21:38 · Speaker 3

Hello

### 02:21:45 · Speaker 4

If you perceive these things as lengths, there cannot be negative lengths.

### 02:21:51 · Speaker 2

Okay

### 02:21:51 · Speaker 4

I mean it's only a definition convenience. The way the measures are defined, they have to be non-negative.

### 02:21:59 · Speaker 4

Earth

### 02:22:01 · Speaker 4

Okay

### 02:22:02 · Speaker 4

By the way there are lots of measures sir. Lebesgue measure is only one of the so many measures that people have come up with on real numbers. But yeah so Lebesgue measure is one of such measures. There are other measures like like Henry measure, Riemann measures and so on. But yeah so the the usual measures that we look at right, the lengths and areas and volumes, they are all Lebesgue measures. Okay. Any other questions on this? I mean what constitutes a measure?

### 02:22:31 · Speaker 4

So again I'm defining right? I mean it's basically a function a set function that would take subsets of a given set and maps it to a non-negative real number such that there are some properties I'm not going into details you know one property is that it has to be see every measure by construction by definition has to be

### 02:22:51 · Speaker 4

non-negative for any set it has to be greater than or equal to zero. The other thing is measure on the null set has to be zero. Okay? And the measure on union of two sets has to be equal to the individual measures.

### 02:23:10 · Speaker 4

if

### 02:23:12 · Speaker 4

the intersection is null

### 02:23:14 · Speaker 4

These are some of the properties. I mean as long as you can come up with a function that would adhere to these properties, you can name it, you can give it your name and call it your measure, okay? So this is the length measure. Okay, so now why did I talk about this? Remember that our, you know, we were looking at random experiments, okay? And we were looking at outcomes.

### 02:23:35 · Speaker 4

Now what are outcomes? We do have a set here, okay, which is called the set of all possible outcomes of a random experiment and we call that the sample space. Okay, because we have a set.

### 02:23:51 · Speaker 2

So we have this set which is sample space

### 02:23:59 · Speaker 2

it's it what is that that's a collection of

### 02:24:04 · Speaker 2

collection of

### 02:24:07 · Speaker 2

All possible

### 02:24:10 · Speaker 2

Outcomes

### 02:24:13 · Speaker 2

of a random experiment.

### 02:24:21 · Speaker 2

Right, we have a sample space. We can now create subsets of this sample space, right? So let F

### 02:24:32 · Speaker 2

You know what

### 02:24:37 · Speaker 2

subsets. Set of subsets actually.

### 02:24:45 · Speaker 2

make it the set of subsets.

### 02:24:58 · Speaker 2

Do you understand what I'm talking about?

### 02:24:59 · Speaker 4

again you can go back to your examples right if you are rolling the die you can take you know one three four five as one subset of the sample space if you are looking at tossing a coin you can head head head tail head tail tail whatever right they are subsets of omega I mean this is omega by the way and if if you are looking at you know pictures then if you take pictures of several so some set of human beings right that is a subset of this particular set and F denotes

### 02:25:30 · Speaker 4

the collection of all such subjects of this ample space.

### 02:25:35 · Speaker 4

is clear?

### 02:25:40 · Speaker 4

See just like we had the line segments right of which are pieces of number line real line. So you have subsets of the sample space okay which is a set.

### 02:25:55 · Speaker 4

Okay? Now. Now we have a set and we have a subset. Now because we have a subset subset and a subset, we can define a measure on it.

### 02:26:06 · Speaker 3

Correct? So now define

### 02:26:08 · Speaker 2

am I sure

### 02:26:15 · Speaker 2

measure

### 02:26:17 · Speaker 2

actually termed the probability measure

### 02:26:27 · Speaker 2

Okay, on

### 02:26:30 · Speaker 2

every subset, every element of the subset of sample space.

### 02:26:33 · Speaker 4

space. Now given any element

### 02:26:38 · Speaker 4

that is a subset of this the

### 02:26:42 · Speaker 4

sample space, then I will define a measure on top of it, okay? And this

### 02:26:43 · Speaker 2

then

### 02:26:49 · Speaker 2

is right is defined as a measure that is

### 02:27:00 · Speaker 2

Between zero and one

### 02:27:03 · Speaker 2

unlike

### 02:27:04 · Speaker 4

level myself that can take any non-negative value, the probability measure, okay, can only take values between zero and one. So now you might have this question, right, why did we do it this way? Did it this way because, as I said, remember the goal is to associate uncertainty in the entire modeling process. You see, okay? And how do you do that? This is one of the ways of doing it. Now, you say that, okay, everything that you observe is an outcome of a random experiment.

### 02:27:34 · Speaker 4

every subset that you observe. Okay, or every outcome, every subset that you observe of the outcome of the random experiment that you are doing now is associated with a particular

### 02:27:46 · Speaker 4

measure, okay? which is lower and upper bounded between zero and one. So now we you interpret the these values as the amount. So basically this measure, right? the probability

### 02:27:58 · Speaker 3

measured

### 02:28:02 · Speaker 3

such nuisance. The probability measure

### 02:28:07 · Speaker 3

can be interpreted. So just like you interpret the Lebesgue measure as length, okay?

### 02:28:14 · Speaker 2

interpreted

### 02:28:17 · Speaker 2

pass

### 02:28:19 · Speaker 2

the uncertainty

### 02:28:26 · Speaker 2

Associated

### 02:28:31 · Speaker 2

which

### 02:28:33 · Speaker 2

a subset of subset A which is a subset of sample space.

### 02:28:36 · Speaker 4

Do you understand?

### 02:28:39 · Speaker 4

Now if you go to this example of looking at the speech and the images that we have as the as the elements of sample space. You can imagine if you take any subset of the sample space, there is an inherent measure, right? that is associated with this particular subset that would quantify the uncertainty that is interpreted as an uncertainty associated with this particular subset. Does it make sense? See, you should see probability, right? Just as you see length.

### 02:29:14 · Speaker 4

on a real line. So what is

### 02:29:16 · Speaker 3

So let me write that. So length

### 02:29:23 · Speaker 3

areas

### 02:29:26 · Speaker 3

on

### 02:29:27 · Speaker 3

R R two, right? is exactly equivalent to probability on

### 02:29:36 · Speaker 4

sample space

### 02:29:37 · Speaker 3

just

### 02:29:39 · Speaker 4

And you see this point? Now, see I just made this statement, right? That uh remember that we are interested in doing this, you know, function earning business. And uh we came up with this paradigm called probability theory. So what is basically being done is you model or rather you see everything that you have, right? As see, okay, so let me go back a little. It's a very nice analogy here. See, uh here when we we said that we have pairs of

### 02:30:09 · Speaker 4

observations that are coming from two sets. Similarly, the set of the domain that we talk of for functional approximation now becomes the elements of sample space.

### 02:30:22 · Speaker 4

Okay? And just like you associate lengths with the the subsets of real numbers, you associate another measure called probability measure that would tell you that will not give you the length of these sets, okay? Or subsets. This will tell you how certain or uncertain that particular set is.

### 02:30:45 · Speaker 4

Do you see this point? Any questions so far?

### 02:30:49 · Speaker 4

There is one other piece, you know, that I have to talk about, which is the idea of random variable and distribution functions. We'll see that and then we'll stop this class, you know, because from next class I can start formulating what generative modeling is using these terminologies. But yeah, any questions so far? This is this is actually bare bone uh fundamentals for studying any of the ML, okay? So let us uh ensure that

### 02:31:12 · Speaker 3

few people understand what I'm talking about.

### 02:31:17 · Speaker 3

Any questions here?

### 02:31:21 · Speaker 6

Sir, if we take the set of all subsets of a set, and assign a probability uncertainty for each of those subsets, is that what we are talking about?

### 02:31:24 · Speaker 3

SET

### 02:31:30 · Speaker 4

Hmm

### 02:31:32 · Speaker 4

Correct, correct.

### 02:31:33 · Speaker 6

Correct

### 02:31:33 · Speaker 4

then the

### 02:31:33 · Speaker 6

and that's called a sigma algebra, right?

### 02:31:35 · Speaker 4

that's a sigma algebra of course. If you just sigma algebra

### 02:31:39 · Speaker 6

Okay

### 02:31:40 · Speaker 4

is actually a significant question

### 02:31:41 · Speaker 6

Signature

### 02:31:42 · Speaker 6

Okay

### 02:31:43 · Speaker 4

That's also called the event set. See, I'm because I'm not teaching probability theory, you know, I'm not going deep into this. First course on probability theory should start from this. So what you said is correct. F is a sigma algebra and measures are only defined on sigma algebra. This is this is the sigma algebra defined on top of or obtained from the sample space. That's correct.

### 02:32:04 · Speaker 6

ओके ओके

### 02:32:06 · Speaker 4

Harish Gautam. See, I don't want you to overburden with terminologies, you see. I am only defining what is absolutely necessary.

### 02:32:14 · Speaker 4

Harish Gautam

### 02:32:16 · Speaker 3

Sir, is sample space same as domain?

### 02:32:21 · Speaker 4

not yet, okay? not yet. I will not say that because hold on to that question. That's a very good question. I'll come to that in a while.

### 02:32:31 · Speaker 4

For now I I would say no, they're not exactly the same. See because look at this. See if we are looking at taking the picture of a person as the random experiment and we are looking at every person as the outcome, right? Then where is the domain of the functions that we actually talk of? See because see what we measure, I mean not the measure theory measure, I mean English measure, what we observe, let's say what I observe are real numbers.

### 02:32:59 · Speaker 4

Okay? The elements of the sample space are not real numbers. Can you see that?

### 02:33:06 · Speaker 4

elements of the sample space are persons or rather you know sentences or they are documents which are not real numbers. Do you do you see that?

### 02:33:18 · Speaker 4

So now the biggest challenge is which I will talk about in a while is that you need a mechanism where you convert

### 02:33:28 · Speaker 4

the probability measure, right? into a space which you can, you know, which which you can imbibe some other sort of a measure. In fact, where you can use Lebesgue measures. That's why random variable comes into picture. I'll talk about it in a while, but don't think of the outcomes of sample space as domains yet. There is a relationship between them, but they are not exactly the same, okay? That's a very good question by the way. Nice observation. Yeah, Abhirup.

### 02:33:56 · Speaker 5

Yeah, sir, how do we extend this notion? Like you gave the example that, you know, if we consider the set of all people as the set of sample space. And then if we are assigning uncertainties to certain sets of people.

### 02:34:06 · Speaker 4

then

### 02:34:11 · Speaker 4

all subsets, all possible subsets. all possible subsets of people. exactly. yeah, so you take any possible subset, it can be a single term also, in the sense that you can take a particular person and that particular person which happens to be a subset also has a measure associated with it. yeah, so. yeah, so.

### 02:34:11 · Speaker 5

ऑल सब्सट

### 02:34:13 · Speaker 5

all possible subsets of P exactly

### 02:34:16 · Speaker 5

Dude

### 02:34:26 · Speaker 5

Yeah, so my question is that how is this notion is going to help us to figure out whether that particular person is a male or female, I mean

### 02:34:35 · Speaker 4

Well, you have to wait

### 02:34:38 · Speaker 3

That's a good question. We'll we'll we'll we'll see that. We'll see that.

### 02:34:47 · Speaker 3

Yeah, Arijit

### 02:34:50 · Speaker 0

Uh sir, what I understood, the complete theory is based on the correctness of the sample space, right? Now,

### 02:34:57 · Speaker 4

No no no hold on hold on hold on. No no don't jump. What do you mean by correctness of sample space I never defined that.

### 02:35:03 · Speaker 0

I mean, uh, I mean to say that suppose, uh, the random experiment I am doing, defining a sample space and from there we are taking the subsets and all this theory is based on that. Right. Is not it? Now suppose if we don't know the sample space or suppose we are talking about the planet in the universe, multiple planets. So on those case it is very tough to define a complete sample space, right? So on those cases if there are

### 02:35:09 · Speaker 4

binding

### 02:35:17 · Speaker 5

Right

### 02:35:31 · Speaker 4

All those cases is there

### 02:35:33 · Speaker 0

parallel line of probability

### 02:35:34 · Speaker 4

Yeah, I know.

### 02:35:36 · Speaker 4

Okay, see, in fact, we never go to sample space because of this exact reason. We never care about sample spaces. We only work with random variables. Just hold on for then I'll come to that idea in a while. Yeah. Yeah. Yeah, Raghavendra.

### 02:35:42 · Speaker 0

Okay

### 02:35:48 · Speaker 0

Yeah, correct.

### 02:35:52 · Speaker 6

Yes, why does it have to include every subset of, yeah, I mean

### 02:35:57 · Speaker 0

Wow

### 02:35:58 · Speaker 4

definition of measure, right? See, because that's how we defined it, right? I mean, given any subset, it has to assign a value, non-zero value.

### 02:36:00 · Speaker 6

Yeah

### 02:36:09 · Speaker 4

because think of I mean you look at the Lebesgue machine right you take the real line. given any

### 02:36:16 · Speaker 3

any subset of this I want to associate a length length with it, isn't it?

### 02:36:23 · Speaker 3

You get it?

### 02:36:26 · Speaker 6

Yeah, but it did not be pairs, right? Say for example, if I consider zero two three, I mean, does it also work on that because so now you have three three elements in that.

### 02:36:31 · Speaker 3

I mean,

### 02:36:33 · Speaker 4

So now you have three

### 02:36:36 · Speaker 4

No, no, oh, okay, okay. See, it's not a subset, you see. See, when you write, what do you mean by zero, two, three? Are you talking about three element subset?

### 02:36:43 · Speaker 6

Yes

### 02:36:45 · Speaker 6

Yes

### 02:36:45 · Speaker 4

See, 0 to 3 is not a subset of R.

### 02:36:49 · Speaker 4

You should always remember that we are talking about the subset of a given particular set.

### 02:36:54 · Speaker 3

0, 2, 3 is not a subset of R

### 02:36:58 · Speaker 3

You see that?

### 02:37:03 · Speaker 6

It is right or

### 02:37:04 · Speaker 3

is it? Zero comma two comma three is it a

### 02:37:07 · Speaker 4

subset of R, the discrete set. I mean, I think is it it's is it a subset of R?

### 02:37:14 · Speaker 4

single term, right? I mean if you take two elements, you're talking about this.

### 02:37:19 · Speaker 4

Correct?

### 02:37:21 · Speaker 4

See, uh note that I'm not putting square brackets here. If I put a square bracket, then it it it's it's a subset. Now, if I write zero comma two comma three, is it a subset?

### 02:37:31 · Speaker 2

let me just let me just confirm

### 02:38:07 · Speaker 2

set of naturals is a subset of

### 02:38:09 · Speaker 4

okay? Yeah, fine. Then it's a subset of R. Okay, it's a valid subset of R. That also has a measure. In fact, the the level measure of a discrete subset of R is zero.

### 02:38:23 · Speaker 4

Okay, it's like this, right? I mean, when if you write this,

### 02:38:28 · Speaker 4

zero comma two comma three. You're actually asking me what is the length of these three points?

### 02:38:36 · Speaker 4

Do you see that?

### 02:38:39 · Speaker 6

Yeah, so that's where I'm confused. So when I say a measure of A, so measure of A, so I mean, uh what all do we really consider in that A? And also if you if you scroll down below...

### 02:38:40 · Speaker 4

a measure of

### 02:38:42 · Speaker 4

So I just

### 02:38:50 · Speaker 4

It can be any subset. See, it can be any subset. See, any subset, right, from the set of real numbers has an associate measure. But level measure of this particular singleton or like discrete subsets of R is zero, that's all.

### 02:39:04 · Speaker 6

Yeah, if you come to this 2D picture, right? I mean, there we said that

### 02:39:09 · Speaker 4

Yeah, if you take the measure, if you take the area of a line, it is zero.

### 02:39:14 · Speaker 6

Yeah, but but in let's stay with this example. So when we say that element x one x two, right? I mean it's again a point in

### 02:39:22 · Speaker 4

Yeah yeah that's why I said no measure is defined on subsets of R two this is not a subset of it can be a subset of R two but this is again a set that has zero measure.

### 02:39:36 · Speaker 4

you get it? This particular single term has zero value.

### 02:39:38 · Speaker 6

particular single term

### 02:39:40 · Speaker 6

Any example where the measure is non zero?

### 02:39:44 · Speaker 4

this this thing no this rectangle

### 02:39:47 · Speaker 6

Okay, so we we choose a region in the uh in in the space and then we associate

### 02:39:51 · Speaker 4

and then we associate. Exactly. Yeah. In R two, you take a subset of R two, okay? So it's like this, okay? Let me write down. So

### 02:40:01 · Speaker 2

this particular set

### 02:40:08 · Speaker 2

1.1, 2

### 02:40:13 · Speaker 2

the spring

### 02:40:16 · Speaker 2

Full one point, come on.

### 02:40:21 · Speaker 2

Four comma three

### 02:40:24 · Speaker 2

This has an answer over here.

### 02:40:25 · Speaker 3

Understand?

### 02:40:31 · Speaker 6

Yeah, because it defines a rectangle, right?

### 02:40:33 · Speaker 4

exact, exact, exact.

### 02:40:34 · Speaker 6

And and if you if you if you go back again to the one dimensional case I think even there we can say the same stuff right so so length is a major when we define it over a range

### 02:40:45 · Speaker 4

No, see that's what I'm saying. See, if you take a subset, you take any subset, the way the measure is defined, it doesn't tell you what subset you have to take. You take a point here, you take three points here, okay? That's also a subset of R. Now the question is what is the measure of that particular subset? The measure of that particular subset is zero, that's all. It does have a measure, but it has zero measure.

### 02:41:08 · Speaker 6

So you need a kind of an interval to define to get a non zero measure.

### 02:41:12 · Speaker 4

Lebesgue measure. Lebesgue measure. Yeah. Lebesgue measure is defined that way.

### 02:41:14 · Speaker 6

Okay

### 02:41:18 · Speaker 6

with an interval, right?

### 02:41:18 · Speaker 4

See in fact, in fact the definition of Lebesgue measure is. So yeah, so if you have a if you have a subset of R, right, which is a closed subset of R, then the the the absolute difference between the final element and the initial element is the definition of Lebesgue measure.

### 02:41:35 · Speaker 3

Okay

### 02:41:38 · Speaker 6

Okay

### 02:41:38 · Speaker 4

it is a interval, right?

### 02:41:42 · Speaker 4

So that's why you take a discrete set, the measure is zero. Isn't it?

### 02:41:43 · Speaker 6

Yeah

### 02:41:46 · Speaker 6

if you take individual points, yeah, if you take individual points, the measure is zero, but if you take an interval, then we have a valid measure. non-zero measure.

### 02:41:50 · Speaker 4

take

### 02:41:53 · Speaker 4

non-zero major. non-zero major. Exactly.

### 02:41:56 · Speaker 6

Yeah

### 02:41:56 · Speaker 4

See that is why it's a very good question. See if you have a continuous random variable or a continuous sample space, the probability measure for a particular point is zero. For instance, if we are looking at this particular example, right, of people, the probability associated with one particular person is zero.

### 02:42:18 · Speaker 4

You see that? It's actually like, you know, uh finding the Lebesgue measure of of of a point. It's similar to that. So that's why if you have, you know, if you have studied probability theory before, people would say that for a continuous random variable, you should not

### 02:42:37 · Speaker 4

interpret the probability density function as valid probability measures because the probability of obtaining a particular point, right, in a continuous sample space is zero. Just like the the measure Lebesgue measure associated with a particular singleton subset of a real number real set is zero. Anyway, so if you understood it, fine, if you don't did understand that, just just ignore it, okay?

### 02:43:00 · Speaker 3

I didn't mean to confuse you. Shall we move on?

### 02:43:10 · Speaker 3

Okay. Now the next question is, Now you understood what probability

### 02:43:15 · Speaker 4

measure is on on sample space, right? So the next thing is, see somebody asked me this question, right? So now what happens is, sample space

### 02:43:27 · Speaker 2

rather elements of sample space

### 02:43:42 · Speaker 2

are not observed in practice.

### 02:43:52 · Speaker 2

because right what you see T I E C E right or T I C E what is it? T I C E

### 02:44:03 · Speaker 4

So what I'm saying is you only get to see the picture of a person, you don't get to see the person. You see what I mean? If you take the elements of sample space, you don't get to see the entire sample space. Right? You don't get to rather let's say elements of sample space are not observed in practice in its entirety, number one. I mean I think Arijit asked that question, right? When you don't observe everything, what do you do? The other thing is you don't even get to see the elements of sample space. When you do a measurement, all you get to see is that you measure

### 02:44:33 · Speaker 4

or rather I mean not measure the series but you observe some real numbers when you see the speed signal you are not the outcome of your random experiment is speech. But what you are measuring is rate of change of well I'm sorry pressure as a function of time. Now how do we deal with it is the question somebody also asked me this question right is the domain that we talk of is actually the sample space no because what we observe what we get to measure

### 02:45:03 · Speaker 4

observed using equipments, okay, or sensors is are not the elements of sample space. Now what is the, what is the, how do we deal with it?

### 02:45:13 · Speaker 4

Okay, that's a very important question. So for that what is done is, so

### 02:45:18 · Speaker 4

define

### 02:45:22 · Speaker 3

therefore define a function from

### 02:45:29 · Speaker 3

Sample Space

### 02:45:31 · Speaker 4

Two

### 02:45:33 · Speaker 4

some real numbers.

### 02:45:35 · Speaker 4

So what are we doing here is that let's say that you have your sample space that are like all persons, okay, or rather you're doing that random experiment where you are looking at all people, okay? That's your sample space. Now I define a a function, okay?

### 02:45:55 · Speaker 4

X is a function, okay? That will take a person or rather take an element from the sample space which is a person.

### 02:46:06 · Speaker 3

Okay? And map it to some

### 02:46:11 · Speaker 3

Three Dimensional Real Number

### 02:46:14 · Speaker 3

Do you see what is happening? What is happening? Take a person take an element from this sample space, okay? And map it to real numbers.

### 02:46:26 · Speaker 3

Do you understand?

### 02:46:28 · Speaker 3

So if you take the example of

### 02:46:32 · Speaker 3

Hidden tail

### 02:46:35 · Speaker 3

a function that we are talking about will take head and maps it to

### 02:46:41 · Speaker 2

I have to write it as a function

### 02:46:50 · Speaker 2

zero. The function evaluated at tail is equal to one.

### 02:46:56 · Speaker 4

So here I can't write I mean the first example I can't write it this way because every of my element x of person one will now become a d-dimensional vector. I mean I can't write a d-dimensional real vector. For our convenience it's actually a p cross q image. Let me write it as.

### 02:47:14 · Speaker 4

P cross Q damage

### 02:47:16 · Speaker 3

make things easier.

### 02:47:21 · Speaker 3

So every of this entry is a real number.

### 02:47:27 · Speaker 3

Do you understand what's happening? What's happening is,

### 02:47:29 · Speaker 4

because the elements of sample space are not observed, okay?

### 02:47:34 · Speaker 4

you assume that there exists a function that will take elements of sample space and map it to something that we measure or observe.

### 02:47:43 · Speaker 4

See this is what we get to measure right. So what do we get to measure? We get to measure the

### 02:47:48 · Speaker 3

observe or measure

### 02:47:54 · Speaker 2

percents

### 02:47:57 · Speaker 2

E

### 02:47:58 · Speaker 2

elements of

### 02:48:02 · Speaker 2

elements of strange

### 02:48:04 · Speaker 3

Space Offer

### 02:48:08 · Speaker 3

of fifty

### 02:48:09 · Speaker 4

function x that will take the elements of sample space and map it to some A dimensional real space. This is what we get to observe. See when we have an image, we have P cross Q real numbers, right? Every image is a P cross Q real number. What is it? The way we should see it from a probability theory, probability theory perspective is that what is happening is you should have the entire story in your mind. What's happening is somebody is doing a random experiment and there is a sample space. We don't get to see the sample space. There is another

### 02:48:39 · Speaker 4

function that is taking elements of sample space and mapping it to real numbers. And these are the real numbers that we get to observe.

### 02:48:49 · Speaker 2

Does this make sense?

### 02:48:57 · Speaker 2

And do you know what this function is called?

### 02:49:02 · Speaker 4

Does anyone know what this function is called?

### 02:49:07 · Speaker 3

Random variable

### 02:49:09 · Speaker 4

That's the most unfortunate thing that has happened. This function X is called a random variable.

### 02:49:18 · Speaker 2

The biggest misnomer of all times. It is

### 02:49:25 · Speaker 2

Neither random

### 02:49:28 · Speaker 2

Why? Because it's a deterministic function.

### 02:49:35 · Speaker 2

right? nor a variable.

### 02:49:41 · Speaker 2

because this is a function

### 02:49:45 · Speaker 4

I don't know who named it random variable but that person has done a big mistake. This is this is neither a random this is neither random nor a variable. It's actually a function that is defined between the elements of sample space to real numbers or like d-dimensional Euclidean space.

### 02:50:04 · Speaker 4

Which sense?

### 02:50:07 · Speaker 4

Now, in the deterministic function approximation problems, what we used to call as domain are actually now

### 02:50:16 · Speaker 4

the elements from the range price of the random variable from the probabilistic standpoint.

### 02:50:23 · Speaker 4

Can you see that?

### 02:50:25 · Speaker 3

set of images

### 02:50:30 · Speaker 3

images that we have as data, this is what is called as a data, okay? set of images which is data or elements

### 02:50:41 · Speaker 3

Electric

### 02:50:41 · Speaker 3

equipments from

### 02:50:44 · Speaker 2

the

### 02:50:46 · Speaker 2

range space of

### 02:50:51 · Speaker 2

of a random variable. X. That is mapping this into

### 02:51:01 · Speaker 4

Do you see the shift now? In the deterministic function mapping scenario, uh in the classical scenario, our data was simply points in PQ dimensional real space. Now, they are still the points in PQ dimensional real space, but they have to be seen as the

### 02:51:22 · Speaker 4

the the the elements of the range space of an underlying function. Okay of an underlying function. Oh I think this works as a pointer. Great. I serendipitously discovered it. You see?

### 02:51:35 · Speaker 4

So if I do it if I do it below what I want to highlight no it will

### 02:51:43 · Speaker 4

Yeah. It'll put that like invisible yellow line behind, but it's okay I suppose. Yeah, you see? Yeah, I was making a very very important point here that in in the probabilistic way of looking at things, the data or the images that you get are just not seen as the elements from a set.

### 02:52:03 · Speaker 4

Okay, they are seen as the elements of a range set. Okay. And when you talk of range, there is a corresponding domain, and what is that domain that we talk of? The domain is the sample space.

### 02:52:20 · Speaker 4

is this idea clear? So every image now, okay, is actually an element from the range space of a function that is called a random enable, which is mapping the elements of sample space to this.

### 02:52:34 · Speaker 4

Euclidean space

### 02:52:38 · Speaker 4

Now do you see why are we doing this you know if you can connect the dots. See the idea of identity of a person is associated with the elements of sample space. But what we are getting to measure right of C are some real numbers. Now we have to somehow relate these real numbers to the idea of the person.

### 02:53:00 · Speaker 4

Okay, which are elements of sample space. Therefore, we need a connection between the sample space and real numbers, which is provided by this function called random variable.

### 02:53:10 · Speaker 2

Is this clear?

### 02:53:20 · Speaker 2

Okay, questions?

### 02:53:21 · Speaker 4

Raghavendra

### 02:53:24 · Speaker 6

So this is just one function which maps it, right? I mean there could be many functions or many random variables defined over the same, over the same sample space. Yes, yes, precisely.

### 02:53:28 · Speaker 4

many random variables we find over the same over the same

### 02:53:33 · Speaker 4

Yes, yes, precisely.

### 02:53:35 · Speaker 6

And in this example, say for example, the set of persons was our sample space, right?

### 02:53:41 · Speaker 4

and you can define multiple random variables on top of it.

### 02:53:41 · Speaker 6

and you can

### 02:53:44 · Speaker 6

Yeah, for example, some gene profile or something of that. So, so that can also become a random variable.

### 02:53:50 · Speaker 4

No no no no no again yeah. See there is no physical connotation to random variables you see in those functions because uh oh what you are saying is that what what we measure may not be the pixels of course absolutely. It could be any totally different domain. Absolutely you measure the height weight of that person that becomes another random variable. Yes.

### 02:54:02 · Speaker 6

the picture. The pictures are of course absolutely. It could be any totally different domain.

### 02:54:12 · Speaker 6

Okay, it's a mapping from the sample space to real. Some some some real space.

### 02:54:16 · Speaker 4

Premium

### 02:54:17 · Speaker 4

Yes, yes, that's a random variable. Now, what happens is, next step is, because we have a measure that we have defined on

### 02:54:27 · Speaker 4

the the sample space, right? Or the subset of sample space, that measure gets translated, right? into some sort of function under this random variable X also.

### 02:54:40 · Speaker 4

You see what I'm saying?

### 02:54:42 · Speaker 6

Yes

### 02:54:43 · Speaker 4

Under the random variable, the measure that was defined on subset of omega now will be measures that are defined on subsets of R.

### 02:54:54 · Speaker 4

You get it? Yes, yes. That's called an induced measure and that measure has a very very famous name that all of you know of, that is called cumulative distribution function.

### 02:54:54 · Speaker 6

Yes, yes.

### 02:55:03 · Speaker 4

the probability measure that gets translated, right, via a random variable, the induced measure that is defined on what is called as Borel sigma algebra or the subsets of R are actually called the probability distribution functions. Now the story is complete, I'll write all that down because you asked I'm asking I'm saying. The story is that now instead of working with deterministic functions, we work with probability measures. Okay? Now those probability measures get translated into

### 02:55:33 · Speaker 4

distribution functions under random variables. Now because we get to see random variables, okay, we work with distribution functions. So now the entire story now is that given some elements from the range space of random variable, okay, estimate the underlying distribution function. That is all the machine learning is all about. Be it generative modeling, discriminative modeling. I will connect it to how is it related to general detection or like even chat GPT is doing the exact same thing. Given a particular A

### 02:56:06 · Speaker 4

random variable observations from a particular outcome of a random variable, estimate the underlying distribution function, that is all underlying probability measure actually. I'll I'll come to that in a while. Okay, Sachin.

### 02:56:20 · Speaker 6

Yeah, I understand. So, uh, I I did not understand this range space. What what does this exactly mean?

### 02:56:26 · Speaker 4

See, a function has a domain and a range, no?

### 02:56:29 · Speaker 6

but

### 02:56:30 · Speaker 4

range is this nothing this is the domain

### 02:56:34 · Speaker 6

Okay, for this function, this is the domain and this will be the range space.

### 02:56:38 · Speaker 4

Range is RPQ

### 02:56:42 · Speaker 6

ओके एंड इट ओके

### 02:56:44 · Speaker 3

And in this particular example here, the the domain is again this, this is the domain.

### 02:56:54 · Speaker 3

the

### 02:56:57 · Speaker 3

range is discrete set of zero one

### 02:57:01 · Speaker 2

Okay

### 02:57:03 · Speaker 3

See what we see are the elements of the range space under this random variable.

### 02:57:07 · Speaker 3

Correct?

### 02:57:08 · Speaker 2

Per

### 02:57:10 · Speaker 4

Aditya

### 02:57:13 · Speaker 1

So we cannot have a random variable which is non measurable. Is that statement correct?

### 02:57:22 · Speaker 4

uh see non-measurable in the sense of measurabilities, right? I mean you are talking about the measurability of a particular set. Are you talking about that? Yes.

### 02:57:31 · Speaker 1

Yes. Yes.

### 02:57:33 · Speaker 4

You can't, no, because uh uh the it is the it is the because there is already an underlying measure that is defined on the domain of random variable. Again, please be very very concerned of the fact that random variable is a function. So whenever I talk of random variable, it's a function that I'm talking about, okay? Now because there is an underlying measure that is that is defined that that has been defined on the domain of this random variable.

### 02:57:55 · Speaker 3

because

### 02:58:03 · Speaker 4

okay? There's always an induced measure that comes with it. And that induced measure itself is called as probability distribution function.

### 02:58:11 · Speaker 1

See you have

### 02:58:11 · Speaker 4

See you have defined a probability measure on the sample space already, right?

### 02:58:15 · Speaker 1

Hmm hmm

### 02:58:16 · Speaker 4

Because of that when you define a function on top of that particular set, there's always an induced measure that comes on along with it.

### 02:58:26 · Speaker 1

And we have a set which is non-measurable, meaning there is no

### 02:58:29 · Speaker 4

Yes, there can be. I mean this is like it's a topic of its own. There is this branch called measure theoretic, measure theory. You should study that. And by the way, if anyone of you is interested in this kind of a treatment, right? There is one very good NPTEL course by Professor Krishna Jagannathan. He's a good friend of mine from IIT Madras. So I think introduction to probability for to for engineers or something, that's the course name. If you have interest in this kind of treatment of probability theory, please have a look at it.

### 02:58:59 · Speaker 4

This is the last time that I'll be talking about measures and all this, okay? And the moment we go to distribution functions and density functions, we'll work with density functions. I mean, I just wanted to make the footing solid, right? Because, you know, people don't often understand where are these probability density functions coming into picture. Because when you are given some data, what is data? Data is simply some ten thousand images or some documents or some speech signals, etcetera. The thing is, we talk of probability

### 02:59:29 · Speaker 4

the distribution functions of this particular speech or images or something, what do they even mean? Okay? I always take this one particular, I mean one introductory lecture to ensure that people exactly know what's happening, no? When we talk of probabilities of images, we actually mean that oh there is this is the this is the element of a random variable, that's a function. So this random variable has mapped the elements of sample space to this particular real numbers. So now examples

### 03:00:00 · Speaker 5

एस हैस ए प्रोबाबिलिटी मेजर एंड इट इज दैट प्रोबाबिलिटी दैट वी आर टॉकिंग अबाउट।

### 03:00:05 · Speaker 5

Okay, I just wanted to give that connection, right, you know, completely. I need fifteen twenty more minutes to establish that connection before we define what generative modeling is.

### 03:00:16 · Speaker 0

shall we do it in next class?

### 03:00:25 · Speaker 0

okay. So here is

### 03:00:28 · Speaker 5

an appeal while coming to the next class. Please look at some of these definitions that I just told you, okay? And in fact, we didn't cover a lot. I mean, it seems like we did a lot, but we didn't cover a lot. It was some definitions, that's all. Please have a look at them, okay? And as I said, no, every class has a, we have a causality, right? I mean, you have to know what we did in this class to understand what we are going to in the next class. We next class, we'll go to discussion.

### 03:00:58 · Speaker 5

distribution functions and define what a generative modeling is and we'll go to the adversarial learning and so on, okay? That's how the trajectory is. So please come prepared for the next class with some of these basics. Please look at what distribution functions are from this angle, right? What are density functions? Like how do you define density function, distribution functions on this and so on. Please have a look at it, okay? I'll not be talking about measure theory anymore. And like if you have any comments,

### 03:01:28 · Speaker 5

etcetera there's always that like anonymous feedback form where you can go and express your because this was the first actual class that we had right. In fact the second half the first half was only some introduction. So you can go to that feedback form and let me know what do you think about this and if you need any particular change I'll be happy to incorporate them.

### 03:01:49 · Speaker 5

Okay. So any questions on today's content, any comments? I think Sachin has something to say. Sachin.

### 03:01:56 · Speaker 4

Uh yes sir, sir, just one question in this context of images. Like one image has multiple pixels, right? Correct. Now this random variable function which like takes a sample space element and converts it into a this R P Q. So like this random variable is will be for the all the pixels of that image or like

### 03:02:02 · Speaker 5

Hello

### 03:02:10 · Speaker 5

சோ

### 03:02:16 · Speaker 5

okay so I think that was apparent anyway. See we we say that R P Q no what are the what are these P Q P Q are the dimensions of the image. So if you're looking at a four hundred cross two hundred image P is four hundred Q is three hundred. So basically we are saying that every image is a point in a twelve thousand dimensional space. Okay and that becomes the the the range of the rating variable.

### 03:02:43 · Speaker 0

Makes sense?

### 03:02:44 · Speaker 4

Yeah

### 03:02:52 · Speaker 0

Okay. uh Anything with Arijit?

### 03:02:55 · Speaker 1

सर, मेबी जस्ट अ लॉजिस्टिक क्वेश्चन, द सेम बुक लाइक इयान गुडफेलो व्हिच एक्सप्लेन्स ऑल द थ्योरी।

### 03:03:01 · Speaker 5

See this good fellow book does not have any of this.

### 03:03:05 · Speaker 1

Okay, okay.

### 03:03:06 · Speaker 5

So, see again as I said, you know, this is not a part of the course because, you know, this is supposed to be some fundamentals, but as I said, just to ensure that everybody knows what's exactly happening under the hood, I do this. From next class we will we'll go to we'll go to the contents in good fellows book, okay?

### 03:03:11 · Speaker 1

Right

### 03:03:24 · Speaker 1

Okay, sure.

### 03:03:27 · Speaker 1

So any books if we want to follow along with your lecture?

### 03:03:27 · Speaker 5

any

### 03:03:30 · Speaker 5

I told you know if you see for this particular treatment of probability theory you look at Professor Krishna's lectures. This is not needed I mean meaning I mean if you know this it's great right but this this is bare bare bone fundamentals. Yes. After after you know this then then we will move on to distribution functions and so on.

### 03:03:33 · Speaker 1

Okay

### 03:03:35 · Speaker 1

Okay

### 03:03:40 · Speaker 1

Okay

### 03:03:46 · Speaker 1

Yes

### 03:03:52 · Speaker 1

Sure

### 03:03:53 · Speaker 5

ओके प्रसन्न

### 03:03:56 · Speaker 5

Yeah, classes

### 03:03:56 · Speaker 0

people can leave you out there. Thank you. Prasanna?

### 03:04:11 · Speaker 0

Prasanna are you there? I want to say something.

### 03:04:17 · Speaker 5

perhaps is not there. Okay, so thank you everyone. See you next week. Bye bye.

### 03:04:23 · Speaker 0

Thank you sir. Thank you.

### 03:04:23 · Speaker 2

Thank you

### 03:04:24 · Speaker 5

Should we create a WhatsApp group? Should we create a WhatsApp group? Hello, am I audible now?

### 03:04:25 · Speaker 2

create a WhatsApp group

### 03:04:27 · Speaker 2

Hello, am I audible now?

### 03:04:29 · Speaker 5

Yes

### 03:04:29 · Speaker 2

Yes

### 03:04:32 · Speaker 5

Let me just create a WhatsApp group and send you the

### 03:04:35 · Speaker 5

Go on, Go on, Krishna.

### 03:04:36 · Speaker 2

Hello

### 03:04:38 · Speaker 2

May I have your name?

### 03:04:40 · Speaker 5

Yes, okay

### 03:04:40 · Speaker 2

Yeah, yeah, thank you. I think someone asked the question that if the input is images, then what would be the range? So on continuing on the same question, so what kind of probability measure we should consider in that case? Is it like hyper volume kind of thing?

### 03:04:54 · Speaker 5

what you kind of Yeah, that's that's that's the entire question that you ask in machine learning. What is the underlying distribution that defines this particular image space? Nobody knows, no? That's what we model using neural networks, isn't it?

### 03:05:07 · Speaker 5

So we try to find out

### 03:05:07 · Speaker 2

find out that product measure itself.

### 03:05:09 · Speaker 5

absolutely because you know if you do that then you have solved the problem isn't it? then you know everything about it.

### 03:05:18 · Speaker 0

Okay. The entire machine learning is

### 03:05:18 · Speaker 5

The entire machine learning is finding out that underlying measure. The entire machine learning is finding out the underlying measure. So it is.

### 03:05:26 · Speaker 0

Yeah, okay, okay.

### 03:05:29 · Speaker 5

I I I'll establish that connection in the next class. I wanted to do that in this class itself but you know we ran out of time I underestimated the time that I would take to do all this. So I'll do it in the next class. Please maybe you can ask that question but anyway I'll start the next class with the with the answer to that question. Yeah.

### 03:05:51 · Speaker 0

Thank you

### 03:05:54 · Speaker 5

आई वाज़ आस्किंग इफ वी हैव टू क्रिएट दिस थिंग

### 03:05:58 · Speaker 5

WhatsApp group

### 03:06:02 · Speaker 1

I think Shivam has created one already sir along including you

### 03:06:09 · Speaker 5

Oh that group is there I think no everybody is not there in that group so maybe Shivam can you put it in the in that teams group

### 03:06:22 · Speaker 5

I think he is not there.

### 03:06:24 · Speaker 3

Yes sir, I will ping the link on the Teams group.

### 03:06:27 · Speaker 5

Please do it, huh?

### 03:06:28 · Speaker 3

Yes

### 03:06:29 · Speaker 5

so that everybody is there. I mean I think that's the easiest way to communicate you see. Some resources etcetera we can quickly communicate and so on.

### 03:06:41 · Speaker 3

Yes sir, but it might have a mix of people who have not opted for the course, not sure.

### 03:06:47 · Speaker 5

It's okay. Okay. We are not, you know, some doing some dark state activities here. So fine.

### 03:06:49 · Speaker 3

Okay

### 03:06:56 · Speaker 5

they they drop out. And they can say na that the people who are not enrolled in the course may opt out.

### 03:07:04 · Speaker 3

ओके सर

### 03:07:06 · Speaker 5

Okay, huh? See you next week then. Bye bye. I think you know this long weekend, no, it's heartening to see that all of you are here for a long weekend.

### 03:07:20 · Speaker 0

थैंक यू सर

### 03:07:21 · Speaker 5

थैंक यू. ओके, सी यू नेक्स्ट वीडियो.

### 03:07:22 · Speaker 0

ओके, सी यू नेक्स्ट वीडियो।
