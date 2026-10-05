---
id: uQvtdAPjKqI
title: Lec 3 - Deep Generative Models Intro to Generative Modelling
date: '2024-11-23'
url: https://www.youtube.com/watch?v=uQvtdAPjKqI
description: ''
author: prathoshap5226
duration: 03:10:10
model: saaras:v3
transcript: true
---

# Lec 3 - Deep Generative Models Intro to Generative Modelling

## Transcript

### 00:00:02 · Speaker 5

screen here.

### 00:00:04 · Speaker 5

Uh yeah, so just a couple of logistics things.

### 00:00:11 · Speaker 5

we will start the tutorial from tomorrow. I think you have should have got a calendar invoice and then had should have sent you right?

### 00:00:22 · Speaker 5

So if uh if you people have time to please join the tutorial otherwise you can access it later. And uh we will we will start the quizzes from next to next week okay so which means uh like the second uh Saturday from today. So today is thirty first August right Wednesday.

### 00:00:48 · Speaker 5

next to next Saturday.

### 00:00:51 · Speaker 6

14, I believe

### 00:00:52 · Speaker 5

14 na

### 00:00:55 · Speaker 5

we will have our first quiz on fourteenth.

### 00:00:59 · Speaker 5

Okay

### 00:01:01 · Speaker 6

Uh sir, can we have the tutorial either on Saturday evening or any of the weekday evenings? Sunday, this Monday we can take.

### 00:01:06 · Speaker 5

Sunday this Sunday

### 00:01:09 · Speaker 5

uh see that right that please talk to coordinate with the T A. because I believe that he had a uh he had a poll or something did he?

### 00:01:10 · Speaker 6

that

### 00:01:23 · Speaker 0

No sir

### 00:01:24 · Speaker 4

Hello

### 00:01:26 · Speaker 5

No? Really? No, I I think we didn't got it.

### 00:01:27 · Speaker 4

Hello

### 00:01:27 · Speaker 0

O I

### 00:01:28 · Speaker 3

Rest

### 00:01:32 · Speaker 5

Surprising. Let me just call him right away and just settle that. Just give me a minute.

### 00:01:39 · Speaker 4

So there was

### 00:01:40 · Speaker 7

Hello

### 00:01:40 · Speaker 4

Super

### 00:01:40 · Speaker 6

pull actually. There was a pull. Is that channel? Yeah yeah there is a pull in the channel.

### 00:01:43 · Speaker 5

Is that channel?

### 00:01:44 · Speaker 5

Yeah

### 00:01:44 · Speaker 3

they should

### 00:01:47 · Speaker 3

Hello

### 00:01:47 · Speaker 5

then okay, right? I mean, I think the

### 00:01:49 · Speaker 3

how how how when it came actually in the in the chat window or you know in the channels

### 00:01:56 · Speaker 6

No, in the channels, in the general of this channel, there is a poll.

### 00:02:03 · Speaker 0

Oh, okay.

### 00:02:13 · Speaker 0

Yeah, so

### 00:02:14 · Speaker 5

So then it's fine, right? It was decided based on the outcome of that poll, I suppose, right?

### 00:02:22 · Speaker 7

There were only 30

### 00:02:23 · Speaker 3

And in the evening there are another tutorials also for random process and linear

### 00:02:30 · Speaker 5

what can we do? Okay, so let me ask him to have another poll perhaps and then decide. Just a second.

### 00:02:30 · Speaker 3

Okay

### 00:02:36 · Speaker 0

Right by column

### 00:03:08 · Speaker 0

ನೀವು ಕರಿ ಮಾಡುತ್ತಿರುವ ವ್ಯಕ್ತಿಯು ಉತ್ತರಿಸುತ್ತೆ

### 00:03:12 · Speaker 5

is not picking it up let I will call back once he calls back I will tell him

### 00:03:19 · Speaker 5

I uh

### 00:03:23 · Speaker 5

I mean it's very difficult to find the time that is convenient for like all hundred people in the class, okay? So, I mean we have to do something. uh So yeah, so whatever works for most of the people, we'll have to stick to that, hmm? So I'll ask him to have the poll again.

### 00:03:42 · Speaker 5

and then we can decide.

### 00:03:45 · Speaker 5

Okay, where is this thing?

### 00:03:47 · Speaker 4

I have to see

### 00:03:50 · Speaker 0

to see my screen

### 00:03:54 · Speaker 4

Not yet

### 00:03:57 · Speaker 0

This says it is being shared.

### 00:04:10 · Speaker 0

it says that it's being shared here.

### 00:04:15 · Speaker 0

So let me rejoin

### 00:04:34 · Speaker 0

Huh?

### 00:04:35 · Speaker 4

Sir

### 00:04:39 · Speaker 0

Yeah, tell me.

### 00:04:46 · Speaker 4

Yeah, please go on. Somebody wait.

### 00:04:51 · Speaker 0

Yes sir

### 00:04:53 · Speaker 4

Yeah, tell me.

### 00:04:55 · Speaker 0

Hey

### 00:04:55 · Speaker 4

we are able to see it

### 00:05:08 · Speaker 0

Okay, shall we start?

### 00:05:11 · Speaker 0

Yes sir

### 00:05:12 · Speaker 3

Yes

### 00:05:13 · Speaker 5

Okay, good. Yeah, so a little bit of recap before we continue with today's content.

### 00:05:22 · Speaker 5

Hmm

### 00:05:26 · Speaker 5

Yeah, so we were looking at uh relevant probability theory stuff, right? Uh so we have the probability triplet which is the sample space, the event space and probability measure and we defined this function called random variable that would give you this push forward measure, right? Yeah. So then we said that uh once you have this function called random variable.

### 00:05:50 · Speaker 5

that will move the sample space to some d-dimensional real numbers and you have subsets of real numbers. uh and then you have the

### 00:06:02 · Speaker 5

corresponding measure probability measure that gets translated into the real space which we call the distribution function.

### 00:06:11 · Speaker 5

right? And we looked at some of the properties of what distribution functions are and looked at multiple random variables, conditional random variables, independence.

### 00:06:23 · Speaker 5

and join random variables and so on, okay?

### 00:06:30 · Speaker 5

Okay. uh Before I go to the supervised learning part, machine learning part, any questions on the

### 00:06:41 · Speaker 0

probability theory part

### 00:06:51 · Speaker 4

Hello sir

### 00:06:54 · Speaker 0

second I have to open that

### 00:06:56 · Speaker 5

Yeah, okay, yeah, go on Sachin.

### 00:06:59 · Speaker 3

I just asked one question from last lecture so you mentioned that Borel sigma algebra so we just last week studied that in recent process class. And that was defined on zero to one interval right all open ended intervals. So I was just asking for this the problem you mentioned this Borel sigma algebra is defined on minus infinity to infinity or like it is always on zero to one.

### 00:07:03 · Speaker 5

Hmm

### 00:07:09 · Speaker 2

That was different

### 00:07:25 · Speaker 5

zero to. See, sigma Borel sigma algebra for the real numbers, right? They are defined on real sets.

### 00:07:37 · Speaker 5

Right?

### 00:07:39 · Speaker 5

I think you have confused, right? Why is it between zero and one? I

### 00:07:40 · Speaker 3

Right

### 00:07:44 · Speaker 3

No, no, he just gave an example, so

### 00:07:48 · Speaker 3

you can take

### 00:07:48 · Speaker 5

You can take any certain general

### 00:07:50 · Speaker 3

Needs Attendant

### 00:07:53 · Speaker 5

Yeah, you can you can take any certain generator sigma algebra on top of it, right?

### 00:07:59 · Speaker 3

Right sir

### 00:08:00 · Speaker 5

but specifically Boolean sigma algebras are defined on L numbers, right?

### 00:08:05 · Speaker 3

Okay

### 00:08:06 · Speaker 5

Okay

### 00:08:10 · Speaker 5

smallest sigma algebra and all that contains all the intervals that are possible that is the full sigma algebra yeah

### 00:08:18 · Speaker 5

See that is why I did not even take the I mean define Borel sigma algebra right I said like R R D and subsets of R D and then you have the distribution function

### 00:08:28 · Speaker 0

function on top of it, right?

### 00:08:40 · Speaker 0

Okay. Uh, it's more anything else?

### 00:08:50 · Speaker 0

But it was

### 00:08:51 · Speaker 4

Sachin, who is teaching random process?

### 00:08:52 · Speaker 5

Aditya teaching it

### 00:08:55 · Speaker 3

Yes sir, Aditya Gopalan sir.

### 00:08:57 · Speaker 5

Yeah, we are very good friends, yeah. Okay. uh So, uh with that we will look at what supervised machine learning is. I said that the uh the data, right, is defined uh as some uh some n samples, okay, that are drawn, yeah, that is what I said, you know, the the uh notation is that you have data sampled from a particular distribution or data drawn from a distribution.

### 00:09:27 · Speaker 5

Yeah, that actually boils down to saying that every data point that we have is an element from the range space of a random variable that we have that is X, okay? I mean that we denote by X. So this implies that there exists an underlying probability measure and thus the distribution function induced by X.

### 00:09:49 · Speaker 5

Okay, so this is clear, right? So whenever we say that we have n data points, we actually mean that we are sampling, I mean we have n uh vectors from the range space of the random variable. Once we talk of the range space of the random variable, uh

### 00:10:06 · Speaker 5

we, we, we, we understand that there has been, I mean, there is an underlying measure space, underlying sample space that is there and a probability measure and therefore a distribution function induced by X. Okay?

### 00:10:23 · Speaker 5

Now for the so-called supervised learning what happens is that you have data sampled from the joint distribution of a pair of random variables X and Y. Okay? Where X denotes a random variable whose range space is some RD, I mean I gave the example of MNIST right where it is R seven eighty four dimensions because the images are in twenty eight cross twenty eight pixels and and why

### 00:10:55 · Speaker 5

which is the is another random variable that we are talking of denotes the labels so called labels and there exists two sample spaces right or yeah so two sample spaces whose whose cross product is what we are talking about when we talk of joint distributions

### 00:11:15 · Speaker 5

And when we say data, this is what we mean, right? We have

### 00:11:21 · Speaker 5

basically, right? In other words, what we are saying is, obtaining data is equivalent to conducting the underlying random experiment that generated your sample space multiple times. That's what it means, right? We have conducted the we have we are actually running the running the random experiment multiple times. We are making multiple trials, right? And each of the trial gives rise to some sort of an outcome, okay? And that outcome

### 00:11:51 · Speaker 5

gets mapped to some d-dimensional real space via random variable and because we are looking at a random experiment there is a there is a probability measure that we have assigned and because we have since we have a random process sorry random variable I'm sorry excuse me because we have since we have a random variable uh you have uh I mean the the outcomes of these experiments have been converted into something measurable that is a d-dimensional real number

### 00:12:21 · Speaker 5

That is what is happening. Is this world view clear? See from now on, right? I will not tell you that these are actually vectors in the range space of a random variable which is a function and you have the underlying measure and you have the distribution etcetera. I will simply say that we are given a data from an underlying distribution, that's all. So you understand what I mean when I say that. Is this clear?

### 00:12:47 · Speaker 5

Any questions on this?

### 00:12:51 · Speaker 0

Okay, so now let us start with the definitions.

### 00:12:56 · Speaker 4

Hmm

### 00:12:58 · Speaker 0

this

### 00:12:59 · Speaker 4

Prestus

### 00:13:01 · Speaker 4

laboratories

### 00:13:04 · Speaker 4

it will load the service. Okay.

### 00:13:06 · Speaker 5

सर, यू नीड टू सेलेक्ट प्लस पेज।

### 00:13:11 · Speaker 5

in the third column.

### 00:13:12 · Speaker 4

this page

### 00:13:15 · Speaker 4

Okay. Then you can mention the title.

### 00:13:32 · Speaker 0

also putting lecture numbers right L three

### 00:13:48 · Speaker 0

Sure

### 00:14:13 · Speaker 0

So we'll mostly set up the problem

### 00:14:15 · Speaker 5

today right what are what is the generative modeling problem and so on okay so that is what the major focus of

### 00:14:22 · Speaker 0

today's lecture is

### 00:14:24 · Speaker 0

Okay

### 00:14:25 · Speaker 0

Now let us start with

### 00:14:35 · Speaker 0

data. So this is our input, right?

### 00:14:38 · Speaker 4

means, as they say, I always represent data with

### 00:14:45 · Speaker 4

set. So it is

### 00:14:46 · Speaker 5

either so let us first maybe

### 00:14:51 · Speaker 5

Hmm

### 00:14:53 · Speaker 5

setup supervised machine learning. Actually, right, at a at a core level, there isn't a lot of difference between supervised and unsupervised.

### 00:15:03 · Speaker 4

machine learning I will tell you why it is

### 00:15:13 · Speaker 4

really

### 00:15:15 · Speaker 5

will it be comprehensive from a comprehensive standpoint, will it be better to introduce

### 00:15:30 · Speaker 0

All of you mute please.

### 00:15:43 · Speaker 0

Okay, so let me introduce

### 00:15:48 · Speaker 5

in general then we will talk of the differences okay data. So let's say that you have data. Data is of this form X one X two.

### 00:16:00 · Speaker 5

X N

### 00:16:03 · Speaker 5

make it a little abstract from now on, XN

### 00:16:06 · Speaker 4

and these has been drawn from some

### 00:16:13 · Speaker 4

underlying distribution P X and this is unknown so this is the setting right

### 00:16:19 · Speaker 0

So now

### 00:16:22 · Speaker 0

the succulent means that

### 00:16:26 · Speaker 0

we

### 00:16:28 · Speaker 0

it is keeps happening.

### 00:16:58 · Speaker 0

keep my palm over

### 00:17:00 · Speaker 5

the screen, right? It just gets distorted. I don't know how to control it. Let me know if somebody knows how to do that. Anyway, so the this is thing, we have data that is drawn from an unknown distribution. So actually means that this is the central problem of machine learning that data

### 00:17:19 · Speaker 5

right

### 00:17:19 · Speaker 0

R

### 00:17:23 · Speaker 0

samples

### 00:17:26 · Speaker 0

from

### 00:17:28 · Speaker 0

an unknown distribution, okay?

### 00:17:35 · Speaker 5

Okay, so this actually means that the distribution is unknown, but we have samples from it. So this is the uh the central problem of machine learning in our statistics that you have samples from a distribution, but you don't know what the underlying distribution is.

### 00:17:54 · Speaker 5

Okay. So now the question that we ask, the for the question, the central question that is asked in ML is the following that

### 00:18:06 · Speaker 0

Given

### 00:18:08 · Speaker 0

samples from a distribution

### 00:18:18 · Speaker 0

from a distribution, okay?

### 00:18:21 · Speaker 0

Estimated distribution

### 00:18:29 · Speaker 0

estimate the underlying distribution.

### 00:18:35 · Speaker 5

So this happens to be a central question in ML that

### 00:18:40 · Speaker 5

If you have uh if you are given samples from a distribution can you estimate the underlying distribution?

### 00:18:47 · Speaker 5

Okay. Now why is this important? You understand the question, right? They are not they are two different things. Having samples from a distribution is different from knowing the distribution itself. Can you see the difference?

### 00:19:03 · Speaker 5

Can all of you see this difference? This is very very important. Okay.

### 00:19:06 · Speaker 3

Yes, sir.

### 00:19:07 · Speaker 5

So now, uh so the question is if you if you are given some samples from the distribution, you have to estimate the underlying distribution. So why is this of importance is the question, okay? Uh the the thing is, um

### 00:19:30 · Speaker 0

This is important because, Now let me write that down.

### 00:19:37 · Speaker 0

knowing the distribution

### 00:19:50 · Speaker 0

rebels

### 00:19:52 · Speaker 0

Prediction

### 00:19:57 · Speaker 0

prediction/sampling

### 00:20:05 · Speaker 0

Okay, this is the

### 00:20:06 · Speaker 5

the claim. So if you know the distribution, okay? You can do prediction and you can do sampling. So now what do you mean by prediction and sampling is that uh see in supervised machine learning the problem is that of prediction and in unsupervised machine learning mostly the problem is of sampling. All right in generative models the problem is of sampling. Now to do both

### 00:20:35 · Speaker 5

I request all of you to kindly mute yourself, okay? uh So unmuting with some noise will just cause some disturbance. Thank you. Yeah, so knowing the disturbance, you see, knowing the distribution enables prediction and sampling. Okay? Now, what do I mean by this is the question. So now, let's say that you have

### 00:20:59 · Speaker 0

Um

### 00:21:06 · Speaker 0

So let's take some examples.

### 00:21:13 · Speaker 0

first example may be that so given

### 00:21:18 · Speaker 0

the pairs of

### 00:21:25 · Speaker 0

images and labels.

### 00:21:29 · Speaker 0

Okay

### 00:21:37 · Speaker 4

I'll put it in quotes because I've not defined this yet. Learn to

### 00:21:41 · Speaker 4

Predict

### 00:21:45 · Speaker 0

the so learn to predict the

### 00:21:47 · Speaker 4

tables of unseen images.

### 00:21:57 · Speaker 5

Right? This is the classical uh classification problem, right? Given pairs of images and labels in terms of data, learn to predict the labels of unseen images. So now my claim is that you can model this in the language that we have just said. So now let's say that the data that has been given is the following that you have uh pairs of

### 00:22:20 · Speaker 5

x and y. So note that whenever I write this, I mean that there is there are two random variables that are there and the data has been drawn from an unknown joint distribution between x and y. Right? So this is given pairs of images of given the pairs of images and labels. Now, how do you define this learn to predict part of it?

### 00:22:43 · Speaker 5

Okay, so now prediction is defined as the following.

### 00:22:52 · Speaker 0

prediction is defined to be evaluate

### 00:22:57 · Speaker 0

evaluate the

### 00:23:08 · Speaker 0

Likelihood

### 00:23:13 · Speaker 0

Off

### 00:23:22 · Speaker 0

of label

### 00:23:27 · Speaker 0

Given

### 00:23:30 · Speaker 0

Animage

### 00:23:33 · Speaker 4

This is the definition of prediction problem. I will define what likelihood is, okay? Now we'll have to define likelihood, right? So likelihood

### 00:23:45 · Speaker 4

Okay, likelihood of

### 00:23:51 · Speaker 4

is a very important terminology, likelihood of a of a point

### 00:23:58 · Speaker 4

X is defined to be

### 00:24:02 · Speaker 4

The

### 00:24:03 · Speaker 4

Value

### 00:24:05 · Speaker 4

of

### 00:24:06 · Speaker 4

the density function

### 00:24:08 · Speaker 0

Hmm

### 00:24:14 · Speaker 4

call this as x x cap okay. density function

### 00:24:19 · Speaker 5

evaluated

### 00:24:23 · Speaker 5

at x cap. So this is the definition of the the likelihood. So note that I'm not calling it a probability because I'm evaluating the density function. Remember last class I told you that evaluating the density function of a continuous random variable will not give you the probability, right? So that is why

### 00:24:45 · Speaker 5

I'm defining likelihood of a point as the value of the density function evaluated at x. Okay, at some point x. This means that

### 00:24:55 · Speaker 5

suppose you have a point, you know, suppose there is some x cap that is in some r t, okay? and

### 00:25:03 · Speaker 5

P

### 00:25:04 · Speaker 4

x is a density function

### 00:25:12 · Speaker 4

density function then

### 00:25:15 · Speaker 4

the likelihood of X cap is simply the density function

### 00:25:21 · Speaker 5

validate desktop

### 00:25:24 · Speaker 5

Is this clear?

### 00:25:27 · Speaker 5

Please note the the notations here. Whenever I talk of distribution functions, right, I write this script P, you know, double line P. Whenever I write the density functions, I write small p, okay? And in most of the rest of the part of this course, we will work with density functions, not the distribution functions. Okay, because simply because they are easy to work with.

### 00:25:51 · Speaker 5

Okay? And remember the the connection between the density function and distribution functions, right? Distribution functions are valid probability measures. Okay? uh And the derivative of the distribution functions are what are called as the density functions. Density functions evaluated at a particular point will not give you probabilities, but density functions integrated over a range will give you probabilities because that would be the distribution function evaluated at a particular point. All this is clear, right?

### 00:26:26 · Speaker 5

just repeating what we did in the last class. Okay, great. So now likelihood whenever Yes, go on.

### 00:26:27 · Speaker 4

Yes sir

### 00:26:29 · Speaker 7

likelihood whenever yes go on so you mean to say the the likelihood function is the same as the probability density function ha like

### 00:26:37 · Speaker 5

likelihood. Yeah. I am defining the likelihood as the density function evaluated at likelihood at a point is equal to the density function evaluated at that point.

### 00:26:51 · Speaker 7

Okay

### 00:26:52 · Speaker 5

That's the definition of likelihood. See, whenever we talk of likelihoods, right? The definition is that it is the density function evaluated at that particular point. Now, if the underlying random variable happens to be a discrete random variable, then evaluating density function becomes mass function and evaluating the mass function at a point will actually give you probability, right? But in general, because we are looking at continuous random variables,

### 00:27:15 · Speaker 5

density functions are not probabilities that's why I don't want to call likelihood as probability of that particular point because it does not mean anything. I would just want to define likelihood as

### 00:27:26 · Speaker 5

evaluating or likelihood of a point is simply the value of the density function evaluated at that point and as we saw in the previous class density function of a continuous random variable evaluated at a particular point can be more than one okay can can have values more than one and it does not correspond to a probability this much is clear right

### 00:27:52 · Speaker 5

Okay. Now with the definition of likelihood function, we'll have to define what prediction is. Now I said prediction is simply evaluating the likelihood of the labels given any way, okay? Which implies that this implies that prediction

### 00:28:11 · Speaker 5

is defined the following

### 00:28:12 · Speaker 0

that

### 00:28:15 · Speaker 0

but evaluate

### 00:28:19 · Speaker 0

the conditional density

### 00:28:30 · Speaker 0

At

### 00:28:32 · Speaker 0

x cap. So we'll have to say prediction at x cap, right?

### 00:28:37 · Speaker 0

this

### 00:28:45 · Speaker 0

prediction at x cap

### 00:28:48 · Speaker 5

is evaluating the conditional density at x cap

### 00:28:51 · Speaker 4

what does that mean? So suppose or assume

### 00:28:55 · Speaker 5

Let

### 00:28:56 · Speaker 4

Hello

### 00:28:57 · Speaker 5

P of

### 00:29:01 · Speaker 0

y given x denote

### 00:29:05 · Speaker 0

the conditional density function

### 00:29:16 · Speaker 0

of Y given X

### 00:29:18 · Speaker 5

See note that whenever there is a density function there is an underlying distribution function and I am talking of conditional probabilities here okay. uh let P Y given X denote the conditional density function of Y given X then

### 00:29:33 · Speaker 4

Prediction

### 00:29:38 · Speaker 4

at x cap is simply equal to evaluating this density function, okay, at

### 00:29:50 · Speaker 4

Okay, I will explain my notation in a while, okay?

### 00:29:57 · Speaker 0

But

### 00:29:59 · Speaker 4

x is equal to x cap.

### 00:30:02 · Speaker 4

Okay. I will explain, okay, let me explain the notation first. See, when I write the, see, notational note.

### 00:30:17 · Speaker 0

P of Y given X

### 00:30:25 · Speaker 0

denotes the following. So Y given X

### 00:30:31 · Speaker 0

Okay

### 00:30:33 · Speaker 0

the subscript here

### 00:30:41 · Speaker 0

denotes

### 00:30:52 · Speaker 0

random variables, okay?

### 00:30:54 · Speaker 5

write the density function or any distribution function anything right subscript always denotes the random variables

### 00:31:01 · Speaker 5

this which is

### 00:31:05 · Speaker 5

Hmm

### 00:31:07 · Speaker 4

whatever I write inside the parenthesis right denotes

### 00:31:14 · Speaker 0

the value

### 00:31:18 · Speaker 0

at which the function is being evaluated.

### 00:31:32 · Speaker 0

Okay, is this clear? This is the notation.

### 00:31:34 · Speaker 5

See whenever I write conditional distributions right? I always mean that the conditioned random variable right is fixed at some particular value.

### 00:31:46 · Speaker 5

X

### 00:31:48 · Speaker 5

See, this is the definition of conditional distribution that when I write conditional distribution, it always means that the condition random variable is fixed to a particular value. So given that the condition random where condition random variable has taken a particular value, what does this density evaluates at?

### 00:32:07 · Speaker 4

Is this clear?

### 00:32:14 · Speaker 4

So now in this notation, the prediction, what is the prediction?

### 00:32:19 · Speaker 5

happens what is the prediction problem prediction problem is let's call that

### 00:32:24 · Speaker 5

the prediction

### 00:32:27 · Speaker 5

of x cap is simply the likelihood

### 00:32:33 · Speaker 4

Note that likelihood is a density function, likelihood, okay?

### 00:32:38 · Speaker 4

Off

### 00:32:41 · Speaker 0

the conditional density

### 00:32:50 · Speaker 0

y given x

### 00:32:52 · Speaker 0

Okay

### 00:32:54 · Speaker 0

Evaluated

### 00:33:01 · Speaker 0

with

### 00:33:04 · Speaker 0

the value of the conditioned random variable

### 00:33:16 · Speaker 0

condition random variable

### 00:33:20 · Speaker 0

What is it? In this case,

### 00:33:21 · Speaker 5

is x okay? fix that

### 00:33:28 · Speaker 5

This is the definition of prediction. See, whenever you talk of regression and classification problems, right? This is what you are doing. What you are doing is

### 00:33:39 · Speaker 5

what you are doing is evaluating the density function, okay? conditional density function of labels conditioned on data and you are evaluating that, okay? with the conditioned random variable, which is the data random variable fixed at a particular x cap. because by definition the conditional distribution always means that you have to fix the conditioned random variable at a particular value. So now given that your random variable is fixed at a particular value, what does the uh density function evaluates to?

### 00:34:16 · Speaker 5

that is called a prediction on x cap.

### 00:34:22 · Speaker 5

Do you understand? Now tell me this. uh uh when we uh okay so maybe before we go that before we go there I will perhaps I'll tell you that. Okay. See now suppose let me take an example.

### 00:34:39 · Speaker 4

example. Suppose

### 00:34:48 · Speaker 4

y, okay, is a discrete random variable that takes value 0, 1, 2 up to k.

### 00:34:55 · Speaker 5

ओके

### 00:34:57 · Speaker 5

Okay? If this happens, then

### 00:35:02 · Speaker 0

prediction

### 00:35:05 · Speaker 4

at X cap

### 00:35:10 · Speaker 4

is what? What is this object?

### 00:35:12 · Speaker 5

object? Can somebody tell me?

### 00:35:15 · Speaker 5

and we'll also fix x and x let's say x is some uh random variable that is in some thousand dimensions. we are saying that there is an image okay. it's a hundred by hundred image.

### 00:35:28 · Speaker 5

ten thousand dimensions, hundred by hundred image and we have k labels. So if I have to set up the prediction problem here, what does predicting give me?

### 00:35:39 · Speaker 5

Can somebody tell me?

### 00:35:41 · Speaker 3

Arg Max of P of Y given

### 00:35:43 · Speaker 5

No no no I have not defined it that way right? I have look at the definition.

### 00:35:47 · Speaker 6

one of the K labels

### 00:35:50 · Speaker 5

No, it won't.

### 00:35:51 · Speaker 7

probability density of Y given X

### 00:35:56 · Speaker 5

That is what I've, yeah, what do you mean by that? How many values does this give you? If you predict it on x cap, how many values will it give you?

### 00:36:05 · Speaker 6

Sir, it will give us k values.

### 00:36:05 · Speaker 3

it will give us k values

### 00:36:07 · Speaker 5

Actually

### 00:36:09 · Speaker 6

Okay, perfect.

### 00:36:09 · Speaker 5

it will give you k plus one values, right? So now prediction here means that it will give you an entire density function, in this case a mass function because y happens to be a discrete random variable. So you have zero, one, two up to k here and

### 00:36:27 · Speaker 0

this will have some values like this

### 00:36:46 · Speaker 0

Do you understand? So now this, what is this? This is

### 00:36:49 · Speaker 4

the density function

### 00:36:51 · Speaker 5

of

### 00:36:54 · Speaker 5

y given x, right? Evaluated at x equal to x cap.

### 00:37:00 · Speaker 5

Do you understand this? So prediction will give you a distribution, sorry, it it gives you a density function, right? Or a mass function in this case because it happens to be a discrete random variable, okay? Which is evaluated at x cap. Is this clear?

### 00:37:19 · Speaker 0

Any questions on this?

### 00:37:26 · Speaker 0

Now

### 00:37:26 · Speaker 5

what do you do with this is a different question

### 00:37:29 · Speaker 5

See now you can relate to what we were talking in the first class right given some x you want to know what the corresponding y is. In the deterministic case right or in the non probabilistic treatment of stuff. What was happening is that for a particular x you give a particular y. Okay. Now here for a particular x okay. You are giving me

### 00:37:55 · Speaker 5

multiple Ys with with certain likelihoods associated with each of them.

### 00:38:01 · Speaker 5

Is this clear? Now what do you do with this do with this is is something that is that is that is specific to the user. Either I mean some most of the times what do we do? We take one Y okay? uh corresponding to the maximum value of this density function isn't it?

### 00:38:22 · Speaker 5

if you, I mean if you look at machine learning, what people do is we want one label, okay? So we don't want a density over labels, we want one label. Therefore, we take the arg max of this density and take assign that as label for x cap. However,

### 00:38:40 · Speaker 5

the problem is set this way that given a particular like what you are actually doing is you are evaluating the density function P of the conditional density function at that X cap.

### 00:38:52 · Speaker 5

is this

### 00:38:52 · Speaker 4

clear

### 00:38:58 · Speaker 4

Any questions so far?

### 00:39:00 · Speaker 3

सर, वन क्वेश्चन

### 00:39:02 · Speaker 4

hmm

### 00:39:02 · Speaker 3

So this X cap means a particular point in the this X

### 00:39:08 · Speaker 3

Accident Number AB

### 00:39:10 · Speaker 5

you should be careful in in in in choosing your words. Yeah, see what do you mean by that? It's actually one of the points in the range space of the random variable, no?

### 00:39:19 · Speaker 3

Yeah, rain specialist

### 00:39:21 · Speaker 5

Yeah, but yeah, that is what it is. See, typically, right, X cap, typically,

### 00:39:31 · Speaker 5

X cap does not belong to the data set that you have. Because that's the test data, right? That's what is called as test data.

### 00:39:40 · Speaker 5

Right, even you are interested when you when you are talking about prediction, you can predict on X cap that is that is that belongs to D as well. But typically X cap does not belong to D because you know you want to predict on unseen data, right?

### 00:39:55 · Speaker 6

Yes

### 00:39:56 · Speaker 5

Okay. Uh yeah, so Vivek.

### 00:39:59 · Speaker 6

सर

### 00:40:00 · Speaker 7

Sir, is there any way we can visualize P Y given X? I mean P, um what is that? Conditional random variable.

### 00:40:09 · Speaker 7

Why?

### 00:40:10 · Speaker 5

What do you mean by visualize

### 00:40:12 · Speaker 7

visualize means

### 00:40:16 · Speaker 5

See again you have to go back to the previous lecture I've told you that but let me repeat. See what is happening is that think of it like you know there are there are two random experiments that are being done. One where the images are being taken okay. The other where every image is

### 00:40:34 · Speaker 7

the other where every okay okay okay it's a joint Yeah of course

### 00:40:37 · Speaker 5

Yeah, of course. I'm not talking about joint distribution. There is a joint distribution. Once you have a joint distribution, you have a conditional distribution as well. So we are saying that given that a particular outcome has occurred in one of the sample spaces, in one of the trials, what is the likelihood or like what is the probability that the other event happens, right? I mean, the other trial takes these particular values. That is what the conditional distribution talks about. Yeah.

### 00:40:38 · Speaker 7

I'm not talking

### 00:40:38 · Speaker 7

Distance

### 00:40:41 · Speaker 7

you have

### 00:41:06 · Speaker 4

Okay, yes. Yeah, okay, let's do it.

### 00:41:07 · Speaker 5

Yeah

### 00:41:08 · Speaker 5

Yeah, okay.

### 00:41:10 · Speaker 5

Raghavendra

### 00:41:12 · Speaker 7

Yes, I mean, is there any particular reason why we take likelihood function to be a density function rather than the distribution function?

### 00:41:20 · Speaker 5

Uh yeah I told you right it is easier to work with density functions that's all. Most of the time it is easier to work with density functions especially when you have continuous random variables it is easier to work with them. That's the only reason. Everything that you do with density function can be done with distribution functions okay.

### 00:41:40 · Speaker 5

not vice versa, not vice versa, everything that you can do with distribution functions can't be done with density functions because there can exist random variables for which the density functions do not even exist.

### 00:41:40 · Speaker 1

but

### 00:41:51 · Speaker 0

Hmm

### 00:41:51 · Speaker 5

But most of the in most of machine learning we assume that density functions are you know well defined and they exist and then we work with density functions. Typically in literature not typically right in almost in everywhere in literature likelihood is defined as the evaluating the density function at a point. Yeah. Because of ease of computation and analysis that's all. Yeah.

### 00:42:16 · Speaker 5

you will see that more you know when we talk of the divergence matrix etcetera in a while you will see why density function is easier to work with. So also right there are lots of mathematical tools to deal with density functions you know when we talk of random variables we always talk of associate density functions right. So uniform random variable we give density functions distribution functions we don't remember do you remember the distribution function of uniform random variable no no. And do you remember the distribution function of

### 00:42:17 · Speaker 4

Okay

### 00:42:46 · Speaker 5

random variable we don't but we remember the density functions

### 00:42:51 · Speaker 5

That's the only reason. But remember that when whenever we talk of likelihoods, likelihoods are always density functions evaluated at a point. Okay?

### 00:43:02 · Speaker 5

ओके. मणिकंठा.

### 00:43:05 · Speaker 6

So the dimension here for the X cap will be ten thousand, right?

### 00:43:10 · Speaker 5

Of course, of course.

### 00:43:12 · Speaker 6

Okay

### 00:43:12 · Speaker 5

x cap okay x cap is not in d right but

### 00:43:17 · Speaker 5

it's kept as sample from the same underlying distribution.

### 00:43:23 · Speaker 0

Yeah.

### 00:43:27 · Speaker 5

Srinath

### 00:43:29 · Speaker 2

Uh, sir, uh, so I have a doubt. So this is the conditional distribution of P of X given Y or Y given X.

### 00:43:37 · Speaker 5

y given x, y given x, y given x

### 00:43:40 · Speaker 2

No sir, I was just having a doubt if the other order is that of any importance? Like does that have any significance in the real world basically? P of X given.

### 00:43:47 · Speaker 5

Oh yeah, a lot, a lot of significance it has. Okay, that is called the class conditional density. This is called the the conditional of labels given data. That is the conditional of data given labels, right?

### 00:43:59 · Speaker 2

perfect

### 00:44:00 · Speaker 5

So it does have a significance. I we'll see that we'll see that. So I am setting up the problem of supervised machine learning now so when we talk of unsupervised machine learning we'll see that that has a significance okay.

### 00:44:12 · Speaker 0

Okay sir

### 00:44:14 · Speaker 5

any

### 00:44:14 · Speaker 4

Any other questions?

### 00:44:21 · Speaker 4

Yeah, Karthik

### 00:44:25 · Speaker 8

uh sir yeah I had a query I mean like here always we are talking about predicting one variable given the other. So this label be should it be always something like discrete or can it be

### 00:44:38 · Speaker 5

not necessarily, no? not necessarily. See if you have y belonging to some y is another continuous random variable, you can evaluate the density of that at a condition on another random variable as well.

### 00:44:53 · Speaker 5

In that case, the problem's name changes, no? Then it is called the regression problem, that's all.

### 00:45:00 · Speaker 5

the difference between the regression and classification is that that what sort of random variable your Y is. If your Y is discrete random variable then the problem is called the classification problem then if Y is a continuous random variable it's called the regression problem. But the underlying task is the same the underlying task is still to evaluate the conditionals of Y given its fix at a particular point. Okay?

### 00:45:27 · Speaker 0

Thank you sir

### 00:45:30 · Speaker 4

Okay, we'll write that maybe, right? If Y

### 00:45:35 · Speaker 4

is discrete

### 00:45:38 · Speaker 0

It's the classification problem.

### 00:45:45 · Speaker 0

if y is continuous

### 00:45:51 · Speaker 0

problem is called a regression problem.

### 00:45:57 · Speaker 4

Okay. Okay, now let's get back to what we were doing. So now now given the

### 00:46:05 · Speaker 4

that is

### 00:46:07 · Speaker 4

pairs like this.

### 00:46:13 · Speaker 0

sampled from the underlying joint distribution, okay? Now, given this,

### 00:46:27 · Speaker 0

this becomes

### 00:46:38 · Speaker 0

Okay, good notes when I used to write

### 00:46:41 · Speaker 5

put a box like that, no, that will become a nice box, a rectangle. Here it doesn't.

### 00:46:48 · Speaker 5

Okay

### 00:46:50 · Speaker 5

Okay, so this is the central problem in this is this is

### 00:46:54 · Speaker 4

what is called as supervised machine learning.

### 00:46:56 · Speaker 0

I think

### 00:47:04 · Speaker 0

supervised machine learning or also called as the discriminative machine learning.

### 00:47:10 · Speaker 0

discriminative

### 00:47:11 · Speaker 5

modeling or machine learning, whatever, okay?

### 00:47:17 · Speaker 5

understand? So now given data from the joint distribution, I want to estimate the conditional

### 00:47:27 · Speaker 5

Density function

### 00:47:28 · Speaker 0

function of y given x

### 00:47:32 · Speaker 0

Is this okay?

### 00:47:37 · Speaker 0

Be it classification, be it regression, this is the problem that we are solving.

### 00:47:50 · Speaker 0

questions on this?

### 00:48:00 · Speaker 0

See note that we

### 00:48:01 · Speaker 5

don't know the density function P of Y given X, okay? We only have samples drawn from the joint distribution of X and Y. So now given having samples from the joint distribution of X and Y, how do you estimate the conditional distribution or conditional density function is a is a question that is to be answered and that is the question that is answered in all of like discriminative machine learning. Okay? We will we will see that a part of it now. this is the problem setting of

### 00:48:36 · Speaker 5

discriminative machine learning. Now you can now see the connect, right? So now, oh.

### 00:48:43 · Speaker 4

Student

### 00:48:49 · Speaker 4

is there a way I can put a box? A nicer box.

### 00:48:55 · Speaker 4

try

### 00:48:57 · Speaker 0

we are theme to be circle and aspire icon at the top.

### 00:49:02 · Speaker 0

Live

### 00:49:02 · Speaker 4

Clear

### 00:49:02 · Speaker 0

third one

### 00:49:06 · Speaker 4

This one

### 00:49:07 · Speaker 0

Third from left

### 00:49:07 · Speaker 3

Okay

### 00:49:08 · Speaker 3

from left third

### 00:49:12 · Speaker 3

Sorry, third form right, my mistake.

### 00:49:14 · Speaker 4

shapes

### 00:49:17 · Speaker 4

This is

### 00:49:18 · Speaker 5

book

### 00:49:20 · Speaker 5

Hmm

### 00:49:21 · Speaker 5

Okay. Now, yeah, so now how do you estimate the conditional distribution, conditional density function given data from an unknown distribution is a question. Okay, so let me write this also, no, with P X.

### 00:49:37 · Speaker 5

is unknown here. Okay.

### 00:49:41 · Speaker 5

is a question that we'll answer but this is what the machine learning problem is all about, okay? Discriminative machine learning is all about that uh so now this x i's can be uh okay so let me write so x i

### 00:49:57 · Speaker 5

is in some R D, right? And

### 00:50:02 · Speaker 5

Y I can be discrete

### 00:50:06 · Speaker 5

one to K or it can be another R K, okay? If it's this, then it is class

### 00:50:12 · Speaker 4

location

### 00:50:16 · Speaker 0

If it is this, then it is regression.

### 00:50:22 · Speaker 0

Alright

### 00:50:29 · Speaker 0

entire supervised machine learning is this this that's all. right? how do you estimate this p?

### 00:50:33 · Speaker 5

of y given x given d

### 00:50:37 · Speaker 5

Now, what about the so-called generative models and unsupervised machine learning is that you have given I mean in my mind both of them are very very similar given D.

### 00:50:51 · Speaker 5

or of this form. So you don't have the notion of

### 00:50:54 · Speaker 0

Why there

### 00:50:58 · Speaker 0

Okay? So you estimate

### 00:51:03 · Speaker 0

P X, that's all.

### 00:51:08 · Speaker 4

there is one other part to the the generative problem maybe I'll write the estimate px and

### 00:51:16 · Speaker 4

Sample Summit

### 00:51:22 · Speaker 4

I have to define what sampling is. Shall I do it now or later because it is a little digression.

### 00:51:27 · Speaker 0

Hmm

### 00:51:31 · Speaker 4

let me define it perhaps.

### 00:51:38 · Speaker 5

Before I define the problem of generative modeling, right? I would like to ask you this question. Any questions on this definition of supervised machine learning? See, I still have not answered this question of how do you estimate the underlying density function? I mean that is what we are going to do with this entire course. But problem setting, I want you people to understand what the problem setting is. uh Yeah, so is is the problem setting clear for discriminative modeling and supervised machine learning. Please let me know if you have questions. Karthik.

### 00:52:14 · Speaker 8

Sir, one query. I I know we we don't know the distribution function uh P of X Y. But uh how do we know that it's all been sampled from that distribution function itself? I mean...

### 00:52:26 · Speaker 5

That's an assumption that we make

### 00:52:29 · Speaker 8

Okay, so they can

### 00:52:30 · Speaker 5

make an assumption that the data is coming from one given distribution. Have you heard of something called I I D?

### 00:52:37 · Speaker 2

Sorry sir

### 00:52:38 · Speaker 5

इंडिपेंडेंट एंड आइडेंटिकली डिस्ट्रीब्यूटेड डेटा, आईआईडी डेटा

### 00:52:43 · Speaker 5

Have you heard of that term? Yes sir, yes, yes. That actually means, yeah, in fact I I deliberately left that because I didn't want to confuse you with things, but yeah, let me tell you this. So this this actually sampled IID from this distribution is what is said. This means that they are independently and identically distributed. Identically distributed means that all of these are actually coming from the same distribution. Independence means that all of these data points are independently sampled.

### 00:52:43 · Speaker 3

Have you heard of that term? Yes sir, yes, yes. In drawing process.

### 00:53:13 · Speaker 5

which means that uh observing one image is independent to observing the other image, the next image.

### 00:53:21 · Speaker 5

that okay. So we make an basically we are making an assumption that the that the entire data is coming from one distribution. That is why you know all these methods that have been uh developed using the I I D assumptions fail if there is a distributional shift.

### 00:53:38 · Speaker 6

ಓಕೆ

### 00:53:40 · Speaker 5

Right? That because you know there's suddenly the I D assumption gets broken which means that the data that you have given was coming from one distribution and you modeled it you did everything. Now the test data comes from some other distribution what do you do?

### 00:53:41 · Speaker 6

because

### 00:53:57 · Speaker 5

Right? So that is an assumption that we make that the underlying distribution stays the same. Okay? Yeah, Aditya.

### 00:54:05 · Speaker 1

Uh sir, I wanted to ask what about outliers in that scenario? Like we assume that there are no outliers then?

### 00:54:12 · Speaker 5

No, I have not defined what an outlier is, right? uh See, out, ha. Out, even if it's an outlier, it can still come from the same modeling distribution with less probabilities, right?

### 00:54:15 · Speaker 1

See

### 00:54:23 · Speaker 1

Okay

### 00:54:25 · Speaker 5

Isn't it? Yeah. It can come from the tail of the distribution. But it is still coming from the same distribution, is it? Right?

### 00:54:26 · Speaker 1

Yeah

### 00:54:32 · Speaker 4

Yeah

### 00:54:34 · Speaker 5

Okay, if there are no questions, any more questions on this? So now we will move on. I will define what generative modeling is. See, generative modeling again that you are given data that is sampled IID from an unknown underlying distribution. This is also unknown.

### 00:54:50 · Speaker 5

Okay? Now again you still want to estimate the likelihood or the density function. That's also same. One additional thing that comes in the generative modeling thing is you need to sample from it, okay? So now what do you mean by sampling? First let us

### 00:55:08 · Speaker 4

put

### 00:55:08 · Speaker 0

box around it

### 00:55:13 · Speaker 0

This is the

### 00:55:16 · Speaker 0

problem of generative modeling

### 00:55:29 · Speaker 0

Okay

### 00:55:29 · Speaker 5

This is generative modeling. So given data from an unknown drawn from an unknown distribution, estimate the distribution or the density corresponding density function and sample from it. Now, sampling is defined as follows. The process of sampling is that

### 00:55:49 · Speaker 0

need to implicitly

### 00:55:54 · Speaker 0

Conduct

### 00:55:57 · Speaker 0

or

### 00:55:59 · Speaker 0

run

### 00:56:04 · Speaker 0

the random trial

### 00:56:11 · Speaker 0

corresponding to the sample space.

### 00:56:34 · Speaker 0

This is the process of sampling

### 00:56:37 · Speaker 5

Now, you understand what what I'm meaning? So let's say that you are your sample space is tossing a coin, right? And you are given some hundred coin tosses. Now, what do you mean by sampling? You have to implicitly toss the coin again.

### 00:56:53 · Speaker 5

See in practice we will not have the coin and where with all right so but what we can do is once why am I saying implicitly is because if you run the underlying random trial again what do you get is an outcome. But now because we are working in the space of random variables we will get one point so this implies that

### 00:57:14 · Speaker 5

some

### 00:57:15 · Speaker 0

Clinic

### 00:57:19 · Speaker 0

Leeds

### 00:57:23 · Speaker 0

to appoint

### 00:57:27 · Speaker 0

Hindi

### 00:57:32 · Speaker 0

the rain space

### 00:57:35 · Speaker 0

of the random variable

### 00:57:38 · Speaker 5

Do you see why?

### 00:57:40 · Speaker 5

Do you all see why?

### 00:57:42 · Speaker 5

Because, see what we are doing is sampling is conducting the random trial that gave rise to the sample space, right? So once you conduct the random trial, you have an outcome. And once you have an outcome, you know the entire story, right? You have the the random variable and because you have the random variable, you get a point in the range space of the random variable because random variable operates on outcomes and gives you a point in R D. Is this clear?

### 00:58:10 · Speaker 5

Now generative modeling is all about this. Okay, I'll take questions, I'll take questions. Generative modeling is all about this that you are given some data, okay, that is drawn from an unknown distribution, okay? You should of course estimate the underlying distribution that is a part of the process. Not only estimate the underlying distribution unlike in the discriminative learning case, you should also learn to sample from it. Now what do you mean by learning to sample from it? Learning to sample from it is simply

### 00:58:40 · Speaker 5

you are conducting the underlying random trial. right? again and again. so that every time you conduct a random trial, you have the random variable that is there which will give you a point in the range space of the random variable. that's what. that is generative modeling. that is generative sampling or generative modeling.

### 00:58:58 · Speaker 5

Okay? All this tag GPT, right? All the everything that you see, you know, Sonet, cloud, etcetera are actually doing this. They're actually running the underlying random trial multiple times whenever you do an inference.

### 00:59:12 · Speaker 5

Okay. Now, uh somebody asked me the question just now, right? They said that okay, what is the significance of x given y? Okay. So that is actually that distribution if you learn to sample estimate p of x given y and learn to sample from it, you are actually learning to

### 00:59:33 · Speaker 5

sample from the conditional distribution. sampling from conditional distribution is nothing but conditional generation or prompt based generation. So you're given an input prompt, right, which is represented as another random variable Y. Now P of X given Y is the distribution that you're sampling from. Given a particular prompt, okay, Y is fixed at something, you need to learn to sample from P X. So it is P of X given Y is what you sample from in

### 01:00:00 · Speaker 6

conditional generative models. This is unconditional generative modeling where given data drawn from an unknown distribution, you estimate the distribution and learn to sample from it. Sampling is the process of running the underlying random trial, okay? So that you get an outcome from the sample space and because you have a random variable that's already in place, instead of observing the outcome, what you observe is the element in the range space of the random variable. Practically speaking, if you are given some images, all the images are points in the

### 01:00:30 · Speaker 6

range space of the random variable. If you learn a generative model on it, if you get a generative model on it and learn to sample from it, when you sample what you get is another image, okay, which is nothing but a point in the range space of the underlying random variable. And you will have to sample, see, also observe that there's a very important uh point here in the definition that

### 01:00:55 · Speaker 6

I say that you have to run the random trial that is corresponding to the underlying sample space. You see?

### 01:01:03 · Speaker 6

See, it is not doing, see, if you are given a, let's say that you are given a, given a, given a coin tosses from a biased coin, okay? It's not enough if you just learn to toss a coin, you have to learn to toss a coin, toss that particular coin which generated this random trial, isn't it?

### 01:01:24 · Speaker 6

Do you understand what I am saying?

### 01:01:27 · Speaker 6

So the sampling has to uh has to um uh respect the underlying sample space which means that it has to respect the underlying underlying probability measure which also means that it has to sample in accordance to the underlying distribution.

### 01:01:48 · Speaker 6

Okay, so let me complete it perhaps. Sampling leads to a point in the range path of the random variable.

### 01:01:53 · Speaker 5

will respecting

### 01:02:00 · Speaker 4

respect in the underlying distribution.

### 01:02:09 · Speaker 6

This means that if I have given you data from MNIST data set, uh the sampling has to generate data from MNIST data set only, no? It should not start generating data from some other human faces or something. It has to generate data from MNIST data set. What is the mathematical way of saying it that you run the random, the corresponding random trial, right? That would respect the underlying sample space, which means that the underlying probability measure is intact, which means that the underlying distribution function is also intact.

### 01:02:39 · Speaker 6

that. So now now you understand right? Now you understand why there is a connect between estimating P X and sampling from it. If you estimate P X, you can't estimate you can't sample from an unknown distribution unless you estimate the underlying distribution. Because you need to sample such that the underlying distribution is preserved. Do you see that?

### 01:03:01 · Speaker 6

So the entire problem of generating modeling is that you are given data that are drawn from an unknown underlying distribution. Learn to run the underlying

### 01:03:12 · Speaker 6

I mean, uh, random trials, okay? Such that the distribution function is respected and intact, that's all. So if I say that you will have to sample such that the you have to sample from the underlying sample space, it is understood, no? Because you can't sample from the same sample space unless the measure that is there is preserved. But yeah, I'm just making it explicit to say that you'll have to learn to run the random trial such that the underlying distribution is intact.

### 01:03:42 · Speaker 6

that which means that you better estimate the underlying distribution and then you learn to sample from it. So this is the difference between the discriminative modeling and generative modeling. In discriminative modeling what you do is you stop at estimating the conditional distributions of the labels given data given X, right? Here you estimate the distribution and also learn to sample from it.

### 01:04:08 · Speaker 6

Okay

### 01:04:10 · Speaker 6

ओके

### 01:04:11 · Speaker 6

Science

### 01:04:14 · Speaker 6

Arijit

### 01:04:16 · Speaker 1

maybe sir I did not understand it fully because generative model you need to we need to know how to sample from it right? So suppose we took this coin example we already sampled the coins right? Maybe there are hundred coins and out of that we are choosing ten. No no no no no hold on hold on hold on.

### 01:04:31 · Speaker 6

No, no, no, no, hold on, hold on, hold on. No. Okay. In the coin toss example, we have one coin. We don't have hundred coins.

### 01:04:34 · Speaker 1

Okay

### 01:04:38 · Speaker 1

Okay. Okay. We have

### 01:04:39 · Speaker 6

we have tossed one coin hundred times. That is your data.

### 01:04:45 · Speaker 1

Okay. Got it. Got it.

### 01:04:47 · Speaker 6

But you don't know what the what is the likelihood with which the coin turns out to be head or tail. You get it?

### 01:04:55 · Speaker 1

Hmm, yes, yes.

### 01:04:56 · Speaker 6

ओके? लर्निंग टू सैंपल फ्रॉम इट इस टू लर्न टू टॉस द कॉइन अगेन विदाउट हैविंग एक्सेस टू द कॉइन।

### 01:05:05 · Speaker 1

Okay

### 01:05:07 · Speaker 1

Okay, got it.

### 01:05:07 · Speaker 6

Right? So we have, yeah, we don't have, we have not sampled yet. We we only have uh samples that somebody has already given us, that is our data.

### 01:05:19 · Speaker 5

Okay

### 01:05:19 · Speaker 6

without having access to the coin we need to know how the coin would have turned out if we toss you know ten thousand more times. that is sampling.

### 01:05:29 · Speaker 9

So it basically means we have to sample more from near the peaks of the PDF function.

### 01:05:30 · Speaker 2

Means

### 01:05:36 · Speaker 6

No, I'm not saying peak. You just have to sample it such that the underlying distribution function is intact. You can sample from the tail also.

### 01:05:43 · Speaker 9

Yeah, occasionally from the team but more from the

### 01:05:44 · Speaker 6

Yeah, occasionally from the table, but more from the, I mean, no, no, please. See, you simply say that you sample such that the underlying distribution function is respected, that's all.

### 01:05:55 · Speaker 2

Okay

### 01:05:56 · Speaker 6

See, if you are sampling from so-called tail, the measure associated with that outcome has to be lesser. That's all it means.

### 01:06:03 · Speaker 2

Okay, absolutely.

### 01:06:05 · Speaker 6

You get it? See, now that you know this language, you know, try to use this more. So basically, I'm saying that the underlying measure is respected.

### 01:06:11 · Speaker 6

Now if the measure has to be respected then the underlying probability measure or if the distribution has to be respected then when you sample when you sample hundred times right like you know more number of times if if there is a if there is a if there is an outcome that has more probability then that has to appear more compared to other right obviously

### 01:06:18 · Speaker 0

when you

### 01:06:32 · Speaker 5

obvious

### 01:06:33 · Speaker 5

Yes

### 01:06:34 · Speaker 6

But the the underlying measure has to be perfectly intact otherwise then you are not running the correct random trial no you are learning to uh to sample from some other random trial or some other sample space which is undesirable.

### 01:06:50 · Speaker 1

ओके

### 01:06:51 · Speaker 6

See that is what hallucination is all about right? See what is hallucination that the underlying distribution is not uh estimated properly. If it's not estimated properly it will start sampling from some some other sample space that that does not correspond to the given data.

### 01:07:08 · Speaker 3

But sir, there is no guarantee to, I mean, entirely we can reduce this hallucination, right?

### 01:07:16 · Speaker 6

That is what I am saying, you know, that is why the entire course is designed that you need to, that depends on how good is your estimate on P X S.

### 01:07:26 · Speaker 6

Isn't it? So now the sampling process has to estimate the underlying distribution. If you have not estimated the underlying distribution correctly, then you have you mean you will obviously when you sample you will get things from outside of the sample space, no?

### 01:07:42 · Speaker 6

So that is why you have so many techniques. You have that model, this model. Every model is trying to do the same thing that every every generative model, right? You know, be it GPT, auto regressive, GPT etcetera come from this family of models called auto regressive models, right? And you know, there is this adversarial networks and diffusion models and flow based models, score based models, all of these. All of these are trying to solve this exact same problem that they are trying to estimate the underlying distribution and trying to

### 01:08:12 · Speaker 6

examples from it. Why are there so many models is because each of them estimate the underlying distribution in a different way. Since they don't estimate the distributions quote unquote perfectly you have so many models. Same thing goes for the uh discriminative models also. Why do you have linear regression, logistic regression and SVMs and kernel machines and neural networks. All of them are actually trying to solve this exact same problem which is estimating the underlying conditional distribution. But one model is better than the other because you know different they estimate the underlying distribution in a different way

### 01:08:49 · Speaker 6

Okay. Now you might have heard this term, no? All models are wrong, some are useful.

### 01:08:58 · Speaker 6

Right? So everything is a model, everything is trying to estimate some distribution given some data. They are all models, all of them are wrong. Some of them are useful, that is why you have metrics to estimate how good the performance of a given model is. Okay, so now I have to define what is a model. Right? See, see, I mean observe that we are solving an estimation problem.

### 01:09:23 · Speaker 6

We are trying to estimate a density function. So every estimator is a model.

### 01:09:28 · Speaker 6

When we say that we are we are looking at generative models, discriminative models, what is a model? Model is nothing but an estimator for the underlying density function that we want to estimate. There can be thousands of estimators, each estimator comes with its own property.

### 01:09:43 · Speaker 6

Right, cloud has its property, sonnet has its property, jemma has its property, this thing you know, GPT has its property and so on. Everything is a model, but all of them are trying to do this exact same thing that given data from an unknown distribution, trying to estimate the underlying distribution and trying learning to sample from it. Okay?

### 01:10:03 · Speaker 6

Yeah, Raghavendra

### 01:10:05 · Speaker 2

Yes, so just to clarify my understanding on this prompt based generation. So you mentioned that that problem is basically to sample from P of X given Y. Is that correct?

### 01:10:15 · Speaker 6

Correct. Correct. It is it is it is estimating the conditional distribution of x given y and learning to sample from it. See we will see this in great detail in fact you know we will look at multiple estimators in this course. Okay. Yeah so this is I'm just setting up the problem now. Okay.

### 01:10:16 · Speaker 2

Okay

### 01:10:23 · Speaker 2

See, we will

### 01:10:34 · Speaker 2

Thank you

### 01:10:34 · Speaker 6

Thank you. Yeah, Astik.

### 01:10:37 · Speaker 7

हाय सर सो हियर जस्ट अ सेकंड

### 01:10:39 · Speaker 6

just a second. uh just just a second. uh like I'm I'm I'm I'm both you know happy and a little disappointed. I'm happy that like you know more people are talking. I'm slightly disappointed that same set of people are kind of asking questions. I mean it is I'm not discouraging you people but I want to encourage the entire class to participate. Okay? So feel free to ask questions. Otherwise uh yeah I mean I don't want to go into the

### 01:11:09 · Speaker 6

फिलॉसफी ऑफ पेडागोगी बट या, आई एनकरेज ऑल ऑफ यू टू आस्क क्वेश्चंस. डोंट हेसिटेट, टू आस्क क्वेश्चंस. ओके, आस्क, गो ऑन.

### 01:11:19 · Speaker 7

Yeah, so, uh, as we discussed that we are estimating the distribution, but we are estimating the distribution via the density function associated to it, right?

### 01:11:28 · Speaker 6

Correct. Yes. Yes, so

### 01:11:30 · Speaker 7

Yeah so so earlier we discussed that the density function can't be like a proper like exactly hundred percent representation of the distribution function so whatever we do

### 01:11:39 · Speaker 6

No no no no no hold on no no no I didn't say that. I didn't say that. I said that density functions do not

### 01:11:47 · Speaker 6

evaluating density functions don't give you probabilities, that's all.

### 01:11:52 · Speaker 7

Okay

### 01:11:53 · Speaker 6

Okay. But density functions and distribution function has a one to one mapping to it. If you estimate the density function then you know distribution function and vice versa. If the density functions exist.

### 01:11:54 · Speaker 7

Hmm

### 01:12:04 · Speaker 7

ओके, सो इफ वी गेट अ वैल्यू ऑफ अ डेंसिटी फंक्शन एट अ पर्टिकुलर पॉइंट।

### 01:12:08 · Speaker 6

Then we know, then we know everything about the distribution function because if you have the density function, right, you can integrate that and get the distribution function.

### 01:12:12 · Speaker 7

Okay

### 01:12:18 · Speaker 7

Okay, okay, okay.

### 01:12:19 · Speaker 6

Right? See, but somebody asked me that question, no, why do we work with density functions and not with distribution functions is because computationally easy, that's all. Otherwise, otherwise I can actually say this, no, the problem is

### 01:12:25 · Speaker 7

computer

### 01:12:28 · Speaker 7

Otherwise

### 01:12:35 · Speaker 6

I can set the problem as estimating the underlying distribution function.

### 01:12:40 · Speaker 7

Hmm hmm okay

### 01:12:41 · Speaker 6

right? But I set it up as density function because when I, what happened?

### 01:12:41 · Speaker 7

I said it

### 01:12:49 · Speaker 6

Yeah, I set it up as density function because when I, uh, when I, uh,

### 01:12:57 · Speaker 6

answer this question of estimators no I will I will use density functions for everything that is why. But uh yeah so but uh there is a one to one correspondence between density function and distribution function just that evaluating the density function at a point will not give you probability that's all. yeah.

### 01:13:02 · Speaker 5

But okay

### 01:13:14 · Speaker 7

Okay, okay, understood. Yeah.

### 01:13:15 · Speaker 6

Okay, I understand.

### 01:13:17 · Speaker 2

Oh sir, just to continue that discussion. So here we said that we will get the likelihood, right? And the likelihood may be low, but still the probability may be high. That is possible, right?

### 01:13:26 · Speaker 6

No no no no. No, see again. See, when you when you evaluate the density function at a point, you get a likelihood. So for continuous random variables, there is nothing called probability at a point. That itself is not defined.

### 01:13:41 · Speaker 2

Okay

### 01:13:42 · Speaker 6

Isn't it?

### 01:13:43 · Speaker 2

Yes

### 01:13:44 · Speaker 6

Because probabilities are evaluating the distribution function. Now if you evaluate the density function at a point, right, you get zero. Which means that, I mean, so rather if you integrate the the density function, right, at a particular point, you get zero.

### 01:14:00 · Speaker 6

So the probability of obtaining a particular image is zero actually.

### 01:14:05 · Speaker 2

Yes, that's correct. But what is why you work with likelihoods?

### 01:14:07 · Speaker 6

What is why we work with likelihoods?

### 01:14:09 · Speaker 2

Yeah, but what we are interested in is the probability, right? That, uh, I mean, when the probability is high, we want to take that particular label as the...

### 01:14:13 · Speaker 6

Hello

### 01:14:17 · Speaker 6

just say see. No no for for you mean the discriminative part you are saying is it? Not the Yes yes yes for the discriminative part. Yeah see why? See if Y happens to be a discrete random variable then density functions are probabilities.

### 01:14:23 · Speaker 2

Yes, yes, yes. For the discriminative part.

### 01:14:31 · Speaker 2

Yes

### 01:14:32 · Speaker 6

because they are mass functions.

### 01:14:34 · Speaker 2

Okay

### 01:14:36 · Speaker 6

Right

### 01:14:36 · Speaker 2

But if it is a regression problem then

### 01:14:38 · Speaker 6

If it's a regression problem, then you should just say that it's likelihood. I want a point with higher likelihood. Don't call it probabilities, that's all. You see?

### 01:14:46 · Speaker 2

Yeah, but that's my point. So higher likelihood may not mean the higher probability, right?

### 01:14:51 · Speaker 6

probability of a point itself is not well defined. It is not even defined. So you take decision based on likelihood is all I'm saying. Stop there. See don't jump to the probabilities because probabilities of continuous random evaluating the density function at a point or likelihood of a point is not the probability of that point.

### 01:14:57 · Speaker 2

Okay

### 01:15:00 · Speaker 2

stop this

### 01:15:13 · Speaker 2

Yes

### 01:15:14 · Speaker 6

you get it?

### 01:15:15 · Speaker 2

Yeah

### 01:15:16 · Speaker 6

Yeah, so just just say that I want to pick a point with higher likelihood, that's all. That is perfectly fine. Don't say that, you know, higher likelihood corresponds to higher probability. That is incorrect.

### 01:15:21 · Speaker 2

What is

### 01:15:27 · Speaker 2

Correct. Okay. Yeah.

### 01:15:29 · Speaker 6

Yeah. I mean I'm just making it you know pedantically correct. They are nitty gritties but that is what it is. Yeah.

### 01:15:37 · Speaker 2

Yeah, thank you, sir.

### 01:15:38 · Speaker 6

Okay. See now you should see the connect between estimating the density function and sampling from it, right? I mean if you can't estimate the density function, you can't sample from it because you have to sample in accordance with the underlying density function, that will happen only if you know what the density function is, right? Yeah. Okay. uh Avirup.

### 01:15:58 · Speaker 9

Yeah, so my question is that you have defined generative modeling and discriminative modeling where in discriminative modeling you have explained the relation of supervised machine learning. So can do we have a corresponding definition for unsupervised learning also? I'm just asking for clarity. Yeah.

### 01:16:17 · Speaker 6

for clarity

### 01:16:18 · Speaker 6

Yes. Yes. So, you can also call generative modeling as unsupervised machine learning, okay?

### 01:16:26 · Speaker 1

Okay

### 01:16:27 · Speaker 6

Yeah. So, there is uh yeah. For now let us let us in in in unsupervised machine not all unsupervised machine learning models enable sampling. Now for instance, if you do K-Means clustering, right, it will not enable sampling strictly speaking. But if you do, you know, if you if you if you do GMM clustering, it does enable generative modeling.

### 01:16:52 · Speaker 6

Okay. And also, you know, K-means happens to be a special case of GMM. uh You for now let us call this as unsupervised machine learning, but when we come to this thing called latent variable models, right, which is a special case of special way of modeling the underlying density function, uh then that also is called unsupervised machine learning, okay? But yeah, so for now you can assume that uh that unsupervised modeling, let's say that

### 01:17:23 · Speaker 6

unsupervised models are sort of subset of generative modeling. Okay? For now.

### 01:17:30 · Speaker 4

ओके, थैंक यू

### 01:17:32 · Speaker 6

Maybe I'll not write it. Simply confuse it. Yeah.

### 01:17:36 · Speaker 6

Uh

### 01:17:38 · Speaker 4

one

### 01:17:39 · Speaker 5

was this Sushil? No, this was Avirup I suppose.

### 01:17:46 · Speaker 4

Hello

### 01:17:49 · Speaker 5

Yes, thank you sir.

### 01:17:51 · Speaker 4

So we still have a question I think Sushil you have a question

### 01:17:55 · Speaker 5

Okay

### 01:18:03 · Speaker 4

Sushil

### 01:18:13 · Speaker 5

Okay, so maybe he's not there. Okay. So let us move on. Shall we move on? Any other question?

### 01:18:20 · Speaker 5

Okay, so let us now answer ask this

### 01:18:28 · Speaker 5

Yeah, Manish, go on.

### 01:18:32 · Speaker 4

Sir, you are saying

### 01:18:33 · Speaker 8

that it's a unsupervised problem but we in generative model also like for suppose text based we try to predict the next word right? So while training we fed fed that next word what will be the next word try to predict that. So it's it's a kind of supervised only in that case.

### 01:18:59 · Speaker 6

Yeah, it is not because your I mean the word is I mean the word is modeled as X here, okay? In that case, you are looking at auto regressive models, your words are also random variable X. So now you are actually sampling from the underlying distribution.

### 01:19:19 · Speaker 6

That is why I define prediction in this case particularly as evaluating the uh the likelihood at a point.

### 01:19:29 · Speaker 6

There's no supervision per se there. See that is why you know I don't want to use this terminology of supervised and unsupervised learning precisely because of this you know they are the line is very very blurred. uh You simply say that in both the cases you are estimating the uh estimating some distribution okay given some data that is all.

### 01:19:55 · Speaker 6

Okay, but typically in supervised models or discriminative models, you will not have an explicit sampling process, but in generative model, you will have explicit generative sampling process, that's all. So maybe let us call this as discriminative machine learning if you are

### 01:20:13 · Speaker 6

more comfortable with this.

### 01:20:15 · Speaker 6

Okay, discriminative modeling and generative modeling. Discriminative modeling does not have sampling, generative modeling has sampling. So let's

### 01:20:22 · Speaker 5

have that as the difference. Yeah, Sushil.

### 01:20:25 · Speaker 4

ஓகே

### 01:20:31 · Speaker 5

ಹೌದು ಇಂಪಾರ್ಟೆಂಟ್

### 01:20:31 · Speaker 4

third and question is

### 01:20:41 · Speaker 5

सर वन क्वेश्चन

### 01:20:43 · Speaker 4

Yeah, Goa

### 01:20:44 · Speaker 3

what if like in both the cases we get the density function P Y given like in one

### 01:20:52 · Speaker 5

Hmm

### 01:20:56 · Speaker 3

like for the discriminative model, we get the

### 01:21:01 · Speaker 3

Hello

### 01:21:04 · Speaker 3

density function. So why can't we get the distribution function from that?

### 01:21:08 · Speaker 6

We can, I'm not saying we can't, we can. But in most of the applications, right, it is enough if you have the density function.

### 01:21:17 · Speaker 6

we can get discriminate we can get the distribution function from it.

### 01:21:22 · Speaker 3

Okay and then uh like if you want to sample it from uh like do sampling from that. Like for an example we have a set of images uh of ten classes basically ten different animals and we get the underlying probability distribution and then we sample and say okay we want to generate an like image of a animal in a in a different scenario. Let's say we had the sample of animals in jungle.

### 01:21:35 · Speaker 6

week

### 01:21:39 · Speaker 6

Hmm

### 01:21:52 · Speaker 3

but we want that to want the model to generate the images for those animals in a city context.

### 01:21:59 · Speaker 6

Hmm

### 01:22:00 · Speaker 3

So, won't that be considered as generative model?

### 01:22:04 · Speaker 6

That is the generative model but the change no

### 01:22:08 · Speaker 6

See, that is all, I mean, that is definitely generative model, but then, see, if you only have images of animals that are from, like, jungle in your data, then there is no way that your model is generating images of animals in cities. No, no, no, sir, my

### 01:22:24 · Speaker 3

No no no sir my my my point was so in in the discriminative model we have the uh like basically the K classes from which the data belongs the data can be classified into now using this available data we develop uh like we get the distribution and we develop a model to uh you know generate some fresh data fresh fresh data out of it.

### 01:22:34 · Speaker 2

belong to

### 01:22:51 · Speaker 6

See when we say that see that is what I'm saying let me I don't know maybe I didn't convey the point properly see. When I say that you need to sample from the corresponding underlying distribution. It means that you have to sample from you have to get a quote unquote fresh sample only you know sampling is always fresh sampling.

### 01:23:16 · Speaker 6

Right? Suppose you are given hundred images of these animals, let them belong to ten different categories. When you generate, you have to generate it from those ten different categories only. You can't generate from an unseen category, what I'm trying to say.

### 01:23:17 · Speaker 5

give

### 01:23:32 · Speaker 3

Yes sir, agreed.

### 01:23:33 · Speaker 6

you can't generate it by construction because you have only estimated the underlying distribution.

### 01:23:39 · Speaker 3

Correct, Correct, Correct.

### 01:23:40 · Speaker 6

That's all. When your model is as good as your data, unless your model has seen that, see, it will, it can generate the images.

### 01:23:50 · Speaker 6

from, I mean, which are not there in your data set.

### 01:23:56 · Speaker 5

Correct

### 01:23:56 · Speaker 6

You understand? But it can't generate data from the distribution that does not correspond to your data set.

### 01:23:58 · Speaker 5

Peat

### 01:24:09 · Speaker 3

Got it sir

### 01:24:10 · Speaker 6

You understand that? See for example if you have let's say the images of like you know human beings as your data. When you construct a generating model and sample from it it will generate

### 01:24:12 · Speaker 3

Yes sir

### 01:24:24 · Speaker 6

the face of an non-existent human being. Okay? But it can't generate the face of a monkey or a dog or a cat.

### 01:24:28 · Speaker 3

P

### 01:24:33 · Speaker 3

Correct sir, agreed, agreed.

### 01:24:34 · Speaker 6

That's all, that's all. That is what is meant by respecting the underlying distribution.

### 01:24:35 · Speaker 3

That is what is

### 01:24:41 · Speaker 3

Got it, sir. So, like my point of making this statement here was whether we have the classification or not, it it it won't make a difference, right?

### 01:24:43 · Speaker 6

Hmm

### 01:24:54 · Speaker 6

Yeah. It it should not but as I said there is this thing called conditional generation that I've not talked of right where you where you learn to sample from P of Y given X. Sorry P of X given Y. Now suppose you have ten categories and you know you want to let's say that you have cat images dog images whatever images and you have you have learned to the question is what is the underlying distribution that you are modeling. If you are modeling remember that when I said that there is a conditional distribution it means

### 01:25:07 · Speaker 8

Now suppose

### 01:25:24 · Speaker 6

is that you are modeling y equal to a particular value, right? Now let's say that y equal to one corresponds to cats. If you are modeling this distribution learning to sample from it, you are only learning to sample from the cat images.

### 01:25:37 · Speaker 3

Yes sir

### 01:25:38 · Speaker 6

You understand? However, if I just take this and multiply this with P Y and just take a sum of all this, what am I doing? This is equal to P X, isn't it?

### 01:25:40 · Speaker 3

Hello

### 01:25:49 · Speaker 3

Yes sir

### 01:25:50 · Speaker 6

Now if I combine all the images from different categories and learn to estimate this distribution P X, then I am sampling from all possible animal faces. That's all. So depends on what the what distribution are you modeling. You get it?

### 01:26:00 · Speaker 3

E

### 01:26:01 · Speaker 3

So

### 01:26:07 · Speaker 3

Yes sir

### 01:26:08 · Speaker 6

See that those categories or those labels are are are random or I mean I should not be using this word random. They are they are synthetic or they are pseudo in the sense that

### 01:26:19 · Speaker 6

See, if you can you can group all the cat images into one and call that as one distribution and distribute it so that you when you sample you only get cat images.

### 01:26:30 · Speaker 3

Yes sir

### 01:26:31 · Speaker 6

If you take say images from ten categories, combine them all and call them P X and if you if you mod estimate that, then you get images from all categories, that's all.

### 01:26:42 · Speaker 6

So that categorization is a sort of, you know, it's a it's a synthetic thing, right? Depends on like what are you calling as the underlying distribution and data, that's all, right?

### 01:26:42 · Speaker 5

Okay

### 01:26:47 · Speaker 5

Like

### 01:26:54 · Speaker 4

ओके सर

### 01:26:55 · Speaker 6

Hmm

### 01:26:56 · Speaker 4

ஓகே

### 01:26:57 · Speaker 6

Okay, uh, yeah, Manisha.

### 01:27:03 · Speaker 0

Sir, as an extension to this discussion only and we have answered that but, uh so basically what we are saying is we are finding the uh as I mean as a part one of the problem, it's finding the distribution, the underlying distribution which will tell us which uh which class is linked to which label in a way. No, no, no.

### 01:27:22 · Speaker 6

No no no no no no no no hold on hold on. See in in in generative modeling we are actually not bothered about which data point is associated with what label because there is no idea of labels here.

### 01:27:38 · Speaker 6

See, estimating the underlying distribution simply tells you that what is the likelihood of this particular image under the given distribution, that's all.

### 01:27:49 · Speaker 6

there is no idea of class here at all in generative modeling.

### 01:27:56 · Speaker 6

you get it?

### 01:27:57 · Speaker 0

Yes, so, but we still, I mean the first step is to find the underlying distribution, right? Of what all, you know, are the like for the for example what was being discussed, for all the animals, you know, we are kind of it's kind of which

### 01:28:04 · Speaker 6

Correct

### 01:28:13 · Speaker 6

No. No, no. It's it's a it's a strict no, I tell you. See, you have to understand what is meant by estimating the distribution in the generative modeling case. And we will see examples and we will actually go deep into it, but anyway, at this step you need to understand it. See, if you are given, let's say, hundred images of animals, okay?

### 01:28:35 · Speaker 6

Estimating the underlying distribution means that you are trying to find out how likely or what is the likelihood of a particular image under the distribution, that's all. How likely is that I'm obtaining this image? Suppose I'm conducting that random trial, how likely it is to obtain this particular image is what I'm

### 01:28:56 · Speaker 6

finding by estimating the distribution. It has nothing to do with classes. Here there is not even idea of classes because there is no why here.

### 01:29:06 · Speaker 0

Okay

### 01:29:06 · Speaker 6

The way I have set up the problem, there is no why here at all.

### 01:29:11 · Speaker 0

Okay, you get that. Okay. So it's just the likelihood of getting a particular point in that distribution basically.

### 01:29:16 · Speaker 6

That's all. That's all. So if you have thousand images, I'm just calculating what is the likelihood of obtaining this particular image. That's all.

### 01:29:23 · Speaker 0

Okay, right, right.

### 01:29:24 · Speaker 6

See if if you if you if you imagine obtaining an image as a rule of a die. Okay. So I'm what I'm asking is when I conduct that random experiment, okay, what is the what is the likelihood that I'm obtaining this particular image? That is what estimating P X is all about.

### 01:29:30 · Speaker 0

Hmm hmm

### 01:29:45 · Speaker 6

So what is the likelihood that I get this particular phase? That's all. I mean phase of the die. I mean if you take the die example. There is no notion of labels.

### 01:29:45 · Speaker 5

What is

### 01:29:56 · Speaker 6

in this setting.

### 01:30:00 · Speaker 0

And then the sampling part that we are talking about is basically from

### 01:30:03 · Speaker 6

is that you are obtaining a new non-existent human face, that's all.

### 01:30:12 · Speaker 6

You are actually obtaining an image that is sampling.

### 01:30:17 · Speaker 0

getting that. Yeah, I think I get the notion of that. Yeah, right sir.

### 01:30:19 · Speaker 6

Right? There are two things here. One, see, once you estimate the underlying distribution, you can plug in any of the data points that are within your D or outside of your D as long as it is coming from P X and estimate the likelihood of that particular point using this P X.

### 01:30:36 · Speaker 0

Absolutely. Yeah.

### 01:30:38 · Speaker 6

sampling is that you are obtaining or you are running the underlying random trial so that you get a point a fresh or a new point that is not a part of your D but still comes from the underlying sample space that is sampling.

### 01:30:53 · Speaker 0

Get that, sir. Yeah.

### 01:30:55 · Speaker 6

So there is no notion of labels here at all.

### 01:30:57 · Speaker 0

Got it, got it. Right sir.

### 01:31:00 · Speaker 6

Right? So now I still have not defined this conditional conditional sampling, right? I mean sampling from P of X given Y. See, as I said, Yeah, see, as I said, this has a notion of, you know, prompting.

### 01:31:07 · Speaker 0

Okay sir

### 01:31:14 · Speaker 4

Look

### 01:31:14 · Speaker 0

Yeah, you means you want to know what kind of a like prompting is like you are asking the question like this category and what is the image that I'll get probably for this particular category or something.

### 01:31:24 · Speaker 6

Exactly. So that I have not brought that notion yet. I mean see now in the because that is simply confused stuff you know once you like like assume this idea of generative modeling and sampling no putting a conditioning here and saying that I'm modeling the conditional distribution is not difficult.

### 01:31:43 · Speaker 0

Right, so that that was my point also. So that is that doesn't seem difficult but now I think I get the actual problem there. Yeah.

### 01:31:49 · Speaker 6

See, yeah, so it is not estimating y given x. You understand that.

### 01:31:53 · Speaker 0

Yes

### 01:31:55 · Speaker 6

The problem in generative modeling is not estimating y given x. So that is the problem of discriminative modeling that you are estimating p of y given x.

### 01:31:55 · Speaker 0

Yes yes

### 01:32:03 · Speaker 6

And there is no sampling here

### 01:32:07 · Speaker 6

Okay? But in generative modeling, the the two things, one, there is no notion of labels here.

### 01:32:15 · Speaker 6

Okay? And two, you need to learn to sample from it. I mean, that's a huge thing, uh because see, suppose you have you are given MNIST data set and you create a CNN to predict the classes, right? That will not give you samples from MNIST data set, does it?

### 01:32:31 · Speaker 0

No

### 01:32:32 · Speaker 6

That is simply estimating P of Y given X.

### 01:32:37 · Speaker 6

Right? But if you build a GAN or a diffusion model on on MNIST data set, it will give you new samples from the MNIST data set that are unseen because you are not only estimating the underlying distribution, but you are also learning to sample from it. That is generating modeling.

### 01:32:38 · Speaker 0

Yes

### 01:32:56 · Speaker 6

What is common in both the cases is that there is some distribution that has, I mean there is some sample space and some random trial that has happened and you have generated, you have generated the data already. And that is the the input to both the, I mean all of machine learning that you have some data given from an unknown distribution. Now what do you do with it is the question. Having that data, if you estimate, I mean if your data is of this sort, if you rather model your data coming from a pair of random variables having the joint

### 01:33:26 · Speaker 6

distribution and you interpret one random variable as data or rather the features and the other random variable as labels then if the problem is set up as estimating the conditional of the label random variable conditioned on the feature random variable that is discriminative modeling without bothering about sampling

### 01:33:44 · Speaker 6

But now, okay, I'll make things a little involved because you asked this question. Please see if you can understand this. See, I can actually construct a generative modeling having the data

### 01:33:59 · Speaker 6

that that is given in discriminatory modeling as well. Do you see?

### 01:34:05 · Speaker 6

What I am trying to say is, suppose I have that data set of animals with the corresponding classes also given.

### 01:34:14 · Speaker 6

Right? Now if I estimate P X Y, the joint distribution P X Y and learn to sample from P of X given Y.

### 01:34:15 · Speaker 5

in

### 01:34:23 · Speaker 6

Then that is another generative modeling. That is conditional generation.

### 01:34:24 · Speaker 5

Thank you

### 01:34:29 · Speaker 0

get it. So that's uh the joint uh distribution here. And we also get it from a single uh you know distribution of a random variable.

### 01:34:34 · Speaker 6

Yeah

### 01:34:40 · Speaker 6

distribution of a single random variable. It depends on how do you want to view your data. See if you are given thousand animal images. Now do you want to categorize them into subcategories and say that hey look my data is such that I have the image and the corresponding label with it or do you want to see that as simply thousand images without having labels.

### 01:35:01 · Speaker 0

Yes, and then draw sample. That's all.

### 01:35:03 · Speaker 6

That's all. See, yeah, that's all. It's a modeling choice, you know. What are you drawing samples from? Are you drawing samples from P X or are you drawing samples from P X given Y?

### 01:35:15 · Speaker 6

Right? Now if you are drawing samples from P of X given Y, it simply means that given these animal images and the fact that you know I want to generate from dog images or rather I want to generate image of a dog, then I know how to do it. But now if I give if I I mean that needs the corresponding labels as well.

### 01:35:36 · Speaker 6

Right? Because you are you are you have to estimate P of X given Y.

### 01:35:40 · Speaker 6

But estimating P of X given Y and learning to sample from it also is a generative model, right? So suppose you estimate P of X given Y and sample from X given Y, that's also generative modeling. That is actually conditional generation which is which is what Chat GPT does. So given Y which is a particular prompt you want to generate.

### 01:36:04 · Speaker 6

And for that, the kind of data that you need is pairs of x, y. Do you see that? Because you need the underlying joint distribution.

### 01:36:12 · Speaker 0

Absolutely, yeah, yeah.

### 01:36:14 · Speaker 6

Right? So depends on like what sort of data you have and what sort of density are you modeling and sampling from, that's all.

### 01:36:22 · Speaker 6

But the major difference between these two models is that in discriminative modeling, see in both of the cases, you have data drawn from an unknown distribution, you are estimating some distribution. But what is not there in discriminative modeling is that you don't learn to sample, but in generative modeling you learn to sample from it. That's the only difference.

### 01:36:43 · Speaker 6

Right?

### 01:36:43 · Speaker 4

I get it. Yeah, I get it now.

### 01:36:44 · Speaker 6

I hope that you know this notion is clear because you know uh I mean this this is what differentiates let's say a resnet based CNN or a VGG net from a diffusion modeler again. Both of them are actually estimating the underlying distribution given data. Both of them are given same kind of data. What is different is that the generative models learn to sample from the underlying distribution. Discriminative models don't learn to sample. That's the difference. Yeah.

### 01:37:14 · Speaker 0

Right sir

### 01:37:16 · Speaker 6

Okay, great. Any other question on this? I mean this is important because this is I mean you if you understand what the actual problem is, you know, then rest of the math and algebra becomes easier. Any other questions? So now you see that, right? I mean now one of the central problems in both uh in discriminative and generative learning modeling is that given data from an unknown distribution, how do you estimate the underlying density function is the question, right?

### 01:37:43 · Speaker 6

This is an important question, right? Given data drawn from unknown distribution, how to estimate the underlying density function is the question that has to be answered. Okay? For that, there are multiple techniques. One technique that we will be seeing, uh that is that is common across multiple models that we will see in this uh in this course is what is called as divergence minimization.

### 01:38:10 · Speaker 5

See all these models right GANs

### 01:38:12 · Speaker 6

VAE's diffusion models, auto regressive models, etcetera. All of them employ this technique called divergence minimization to answer the above question. And by the way,

### 01:38:23 · Speaker 6

every generative model that you can think of, right, that the people are coming up with are actually solving this problem that given D you estimate the under intensity and sample from it.

### 01:38:35 · Speaker 6

right? minor modifications here and there. I mean depends on what sort of D that people have. If you have like like text and the corresponding next word or label or something image and label, you learn to sample, estimate the conditional distribution and sample from it. That does not matter because that's simply a like a design choice. But they are all solving this particular problem. Now to solve this problem, you need to estimate the underlying density.

### 01:39:01 · Speaker 6

right? Otherwise, how do you learn to sample according to that particular density? So you'll have to estimate the underlying density. So all of the generative models, in fact even discriminative models have to solve this problem of divergence minimization or rather given data drawn from an unknown distribution, how to estimate the underlying density function is a problem that all ML models have to solve. And one technique to do that is what is called as divergence minimization that is employed by all the existing generative models. Okay? So we will see that next.

### 01:39:31 · Speaker 6

you know how to and what is this divergence minimization and how to use that to solve this problem is something that we will see uh next. Uh shall we take a break now?

### 01:39:44 · Speaker 6

I think it's ninety minutes. Let's take a break for a fifteen minutes now.

### 01:39:53 · Speaker 6

shall we? Okay. uh So in my clock it is eleven A.

### 01:39:56 · Speaker 5

let us reconvene by eleven fifteenish.

### 01:40:01 · Speaker 5

See you in fifteen minutes.

### 02:02:27 · Speaker 1

Hello

### 02:02:30 · Speaker 1

the resume

### 02:02:33 · Speaker 2

Yes sir sure

### 02:02:34 · Speaker 1

Sir

### 02:02:58 · Speaker 1

Okay

### 02:02:59 · Speaker 4

Uh see Chandan has just put a poll for tutorial timings so please respond to that. It is I think both on WhatsApp and Teams. WhatsApp I definitely saw it now I don't know if it's on Teams. Is it on Teams already or?

### 02:03:18 · Speaker 3

I think also

### 02:03:18 · Speaker 1

there are things also

### 02:03:21 · Speaker 4

ओके. प्लीज रिस्पॉन्ड, डिपेंडिंग अपॉन योर रिस्पॉन्स, व्हाटएवर वर्क्स फॉर मोस्ट ऑफ अस, मोस्ट ऑफ यू, वी विल टेक दैट टाइम. ओके.

### 02:03:30 · Speaker 2

Okay

### 02:03:30 · Speaker 4

Let us continue

### 02:03:34 · Speaker 4

See one small request is that from now on the content will become a little dense and intense. So please spend some time after the class in sort of just looking at what is happening so that the story line is not lost, okay? So please do that before coming to every class and also you can look at my reference, look at my notes that I have given to you, that also has some references. bus

### 02:04:05 · Speaker 4

Okay. So now what is the uh the question that we are looking at that we are given data drawn from random distribution and we want to estimate the underlying density function that is the question that we are looking at. How do we do that? One of the methods to do it is via this thing called divergence minimization. So what is the idea there? Okay. The idea is the the basic idea is the following that first

### 02:04:30 · Speaker 1

assume

### 02:04:34 · Speaker 1

a parametric form

### 02:04:42 · Speaker 1

for the unknown density.

### 02:04:47 · Speaker 1

for the density function that is to be estimated, okay?

### 02:04:51 · Speaker 1

for the density function.

### 02:04:55 · Speaker 1

to be estimated.

### 02:05:01 · Speaker 4

Okay, so the I mean this I'll give you step by step. So this is the first step. Now, what does this mean? This means that, uh so now you are given some data D, right? You assume that uh the density function that I have to estimate, uh

### 02:05:18 · Speaker 4

can be represented using a neural network with some parameters.

### 02:05:24 · Speaker 1

You understand?

### 02:05:25 · Speaker 2

Okay, so typically denoted by

### 02:05:28 · Speaker 1

Okay

### 02:05:38 · Speaker 1

denoted with P theta, okay?

### 02:05:45 · Speaker 1

θ are the set of parameters.

### 02:05:57 · Speaker 1

Do you understand what this means? So an example can

### 02:05:59 · Speaker 4

multiple examples. Assume your P theta, let's say that I assume it to be a Gaussian density and note that this density function is still on the same sample space or the random variable as the underlying data, right? I mean obviously it has to be defined on that only. So this can be let's say a Gaussian distribution, okay? uh with some mean, okay? mu and some variance sigma. Now theta in this case happens to be the mean vector

### 02:06:34 · Speaker 4

and the variance matrix.

### 02:06:37 · Speaker 4

You understand? So what we do is we assume a parametric form for the density function that is to be estimated. Okay? Denoted by P theta. uh You you can assume that to be anything. You assume it to be a Gaussian density, assume it to be exponential density and those parameters happens to be that. This is one example. The other example can be that I

### 02:07:00 · Speaker 2

assume it to be a neural network, right? So P theta of X

### 02:07:05 · Speaker 1

it is is is output of some

### 02:07:13 · Speaker 1

some neural network, right, where

### 02:07:19 · Speaker 1

G theta

### 02:07:22 · Speaker 1

is a

### 02:07:23 · Speaker 4

neural network

### 02:07:25 · Speaker 4

is a neural network and this Z is simply some some Gaussian distribution

### 02:07:32 · Speaker 4

So basically the way I'm modeling this is there is a sample of the Gaussian distribution that is going through a neural network G theta. We will go to the details of all this in a while but these are examples. So G is going as output and what is what am I getting at the output are actually P theta of X.

### 02:07:52 · Speaker 4

Right? I can model it. I mean this is again a design choice. We I mean this is where different models are different. This D theta can be a transformer, right? It can be a C N N or R N N or whatever depending upon what your choice is. But basically the idea is that you assume a parametric form for the underlying density function that is to be estimated, denote it with P theta. uh Is this clear? Like what do I mean by parametric assumption?

### 02:08:27 · Speaker 1

So this is the first thing that you do.

### 02:08:28 · Speaker 2

once you make that assumption what is the second step? The second step is

### 02:08:32 · Speaker 1

that

### 02:08:37 · Speaker 2

define and compute

### 02:08:41 · Speaker 1

compute, okay? A distance or a divergence metric.

### 02:08:52 · Speaker 1

divergence metric

### 02:08:55 · Speaker 1

between the true density function

### 02:09:03 · Speaker 1

Exactly True

### 02:09:06 · Speaker 1

density function

### 02:09:09 · Speaker 1

which is P X, right? And

### 02:09:13 · Speaker 1

parametric

### 02:09:25 · Speaker 1

parameterized function P theta.

### 02:09:29 · Speaker 4

So basically, I'm attracting D, okay? That would take the true density and the paramagnetic density. This is the notation, okay? P X double slash P theta. So this measures

### 02:09:45 · Speaker 2

Power

### 02:09:45 · Speaker 1

Hello

### 02:09:46 · Speaker 1

Close

### 02:09:51 · Speaker 2

four

### 02:09:55 · Speaker 2

to differentiate that would compare

### 02:09:58 · Speaker 4

the true density function to the parametric density function. You might ask me here, right? I mean, we don't know the true density function, how do we compute this? Hold on to that question. That that actually turns out to be the central question of all generative models. When you don't have the true density function, how do you estimate the the distance metric is a question that we'll answer later. However, what we need to do is we need to define and compute some sort of a divergence or a distance metric between density pairs of density functions. In this the density functions happens to be the true density and the parametric density that we have assumed.

### 02:10:33 · Speaker 2

Hello

### 02:10:33 · Speaker 4

Okay, once we do that, what do we do? So,

### 02:10:40 · Speaker 1

adjust

### 02:10:43 · Speaker 1

of

### 02:10:46 · Speaker 1

Compute

### 02:10:48 · Speaker 1

Uh

### 02:10:50 · Speaker 1

the parameters

### 02:10:56 · Speaker 1

of P theta

### 02:10:59 · Speaker 1

such that

### 02:11:01 · Speaker 1

D of P X

### 02:11:04 · Speaker 4

slash P theta is minimized.

### 02:11:10 · Speaker 4

this procedure, right? This is the this is what is called as training training a model or learning a model and so on. This is the learning part of it.

### 02:11:21 · Speaker 4

understand mathematically speaking what you do is you set the parameters theta star okay as the ones that would minimize what do you mean by R min the set of parameters that would minimize a function okay now that would minimize the distance metric that you have defined between density functions you have two density functions this entire thing now will become a function of theta because P theta is a function of theta and you want to solve of theta

### 02:11:54 · Speaker 2

subs

### 02:11:55 · Speaker 2

that this distance by truck is minimized.

### 02:11:58 · Speaker 2

Now the final estimate

### 02:12:05 · Speaker 1

This is the learning problem. This is the training or learning of generative model, right? Training.

### 02:12:18 · Speaker 2

learning. Training basically is solving an option

### 02:12:22 · Speaker 4

optimization problem you all know that right that is why we use gradient descent and back propagation algorithm to train okay basically you are solving an optimization problem the final estimate for px right is simply p theta star obtained by solving the following

### 02:12:44 · Speaker 1

theta star

### 02:12:48 · Speaker 1

Uptent

### 02:12:50 · Speaker 1

is solving

### 02:12:54 · Speaker 1

the above optimization problem

### 02:13:03 · Speaker 1

optimization as you know in this case it is the minimization problem.

### 02:13:14 · Speaker 1

This is the general recipe

### 02:13:16 · Speaker 4

the right of how to solve any machine learning problem. It can be generated discriminative or generated modeling. What are we doing? We are simply we are given data from a non distribution. We assume a parametric form for the density function to be estimated. Typically denoted with parameters theta. See that is why now you can I think relate. Now in the discriminative case, the underlying density function that we need to estimate is P of Y given X, isn't it? We either model this as a logistic regressor or we model this as That is our model P theta. What is the model? This for the underlying density to be estimated.

### 02:13:55 · Speaker 2

Right?

### 02:13:57 · Speaker 4

This actually P theta

### 02:14:01 · Speaker 4

is what is called as a model.

### 02:14:05 · Speaker 4

be it in a generative model or a discriminative model, the uh the parametric assumption that we are making on the underlying density function is what is called as a model. It can be a neural network, it can be anything, okay, any kind of parametric function. Then the problem of uh like estimating the underlying distribution translates to estimating the parameters of the underlying model that we are assuming, right? That is also a density function. Okay, now how do you estimate the

### 02:14:35 · Speaker 4

parameters of this density function is the question. For that we need to first measure let's say that we fix a we fix one value for this mu and sigma. Let's say that our model is a Gaussian model, okay? And the only parameters that we need to estimate are mu and sigma. We initialize that with some value. Now you get one P theta with that. What we should do is we should compare that P theta with the axial density. Now for that, we need a way to compare density functions. If you take pairs of density functions,

### 02:15:05 · Speaker 4

which you need a way to compare the density functions, right? Now, you compare that and you see if it's large. If the if the distance between the true density and the density function with a particular set of parameters is large, then you change your parameters in such a way that that distance become lesser.

### 02:15:24 · Speaker 4

Right? So for that you need to first compute a or rather compute a distance or a divergence metric between the true density and the assumed parametric density or the model, okay? And then adjust or compute the parameters of the model such that this divergence or the distance metric between the pairs of density is minimized. That is what the training is. Mathematically speaking, you are solving this optimization problem that you find your theta such that this distance metric between this distance metric itself becomes a function of theta, right?

### 02:15:54 · Speaker 4

you need to find this theta such that the distance between the P X and that particular P theta is minimized. So if you solve this problem which is which is trying the model, the final estimate for P X will be that P theta star star is the set of parameters that you have gotten from solving this optimization problem that would minimize the distance metric between the true density and the model density.

### 02:16:24 · Speaker 4

Yeah. Is this clear? Now, again, the open questions are I have not told you two things. I have not told you how to compute the distance spectral when you don't have PX. We still don't have PX, right? That is our whole problem. We will I have not told you that, I will tell you that. The second thing that I have not told you is how to solve this optimization problem and what sort of model choices that we need to make. That will be the subject matter of this course, entire course. We will take different, see, for Gyan's makes, for instance,

### 02:16:54 · Speaker 4

you know, adversarial networks make some assumption on P theta. VIs make some other assumption on P theta. Diffusion models make some other assumption on P theta. They would change this underlying distance metric. They would change the way the optimization is being done. That is what the the you know, the levers with which we can play. What sort of distance metric can we use? What sort of optimization can we do? What sort of model choices we can do are the questions answering in different models. But this recipe would is going to stay.

### 02:17:24 · Speaker 4

you make an assumption on the unknown density function. Define a resistance matrix between two density unknown density and fix the parameters of the assumed density such that the distance material between density and density is minimized.

### 02:17:41 · Speaker 4

that is all the recipe for using the density. Not still how to sample. I'll tell you how different models sample in different ways, we will we will talk about it later, but this is how you estimate the unknown underlying density and this is the recipe.

### 02:17:56 · Speaker 4

Okay, this is called the divergence minimization, right? Because you're assuming a model, minimizing the divergence, right? This D is called divergence, minimizing the divergence between the pair of densities. Okay, any questions so far? Sanjit.

### 02:18:16 · Speaker 7

सर, आई वॉंटेड टू अंडरस्टैंड व्हाट इज दिस जी ऑफ थीटा? लाइक यू हैव रिटन जी ऑफ जी थीटा ऑफ जी सी न्यूरॉ नेटवर्क।

### 02:18:23 · Speaker 4

It's a neural network, no? I told you, no? It's a neural network. Simply a neural network.

### 02:18:30 · Speaker 2

Okay and Z Z

### 02:18:32 · Speaker 4

there is some random variable, some some arbitrary random variable that will go as an input to this neural network and whatever output this neural network is giving, I model it as P three box.

### 02:18:44 · Speaker 8

Sorry

### 02:18:45 · Speaker 4

whatever output that neural network is giving, no, I take that as P theta of X.

### 02:18:50 · Speaker 8

ओके, ओके.

### 02:18:52 · Speaker 4

is one way to model this. As I said, no, as I said, there are multiple models that one can think of, but this is one of the models that you can

### 02:19:02 · Speaker 2

that you can design

### 02:19:05 · Speaker 1

ओके सर

### 02:19:08 · Speaker 2

Is that okay?

### 02:19:12 · Speaker 1

Yes sir

### 02:19:14 · Speaker 2

yeah, so many questions.

### 02:19:16 · Speaker 4

Karthik

### 02:19:18 · Speaker 6

Hi sir. uh I have a little uh like maybe I didn't understand it fully about the parametric form that we were uh referring. Can we get a based on another example maybe a little more simpler one?

### 02:19:31 · Speaker 6

why what do we assume that parameter. Yeah.

### 02:19:32 · Speaker 4

This is the simplest one, right?

### 02:19:35 · Speaker 4

Yeah, you assume if you assume that it's a Gaussian distribution, that's a parametric form. Okay. That how do you how do you differentiate one Gaussian distribution from the other?

### 02:19:40 · Speaker 2

Okay

### 02:19:47 · Speaker 4

is through the its parameters, no, mean and variance. That's all. So you are assuming that, uh, you are assuming that it's a Gaussian density, but you don't know what the mean and sigma are. Correct? Now, how good is my assumption is a different question. It can be a totally crappy assumption that you have made. But that is that is I mean that's why I said all models are wrong, no? You have made some model assumption.

### 02:19:47 · Speaker 2

through the

### 02:19:48 · Speaker 2

it's

### 02:19:50 · Speaker 2

Yeah, that's all. So you are

### 02:20:10 · Speaker 4

So these are simplistic models but in places like you know GANs and GPTs etcetera, these models are made express enough, they are made huge neural networks. So that they can express a large family of functions.

### 02:20:24 · Speaker 4

Basically you are expressing the density function. Now you choose a parametric model such that it is expressive enough so that it can express a large family of functions and transformers and neural networks are such functions. So now what differentiates one transformer from the other transformer is the is the weights that they have. Right?

### 02:20:42 · Speaker 2

Hello

### 02:20:42 · Speaker 2

Now that

### 02:20:43 · Speaker 4

Now that is that relates, hold on, that relates, suppose you have like, you know, two transformers, okay? of the same architecture, but you have two underlying distributions you want to estimate, right? using the same architecture, you can fix the weights of these two transformers in in different ways so that, you know, they represent two different distributions, that's all. That

### 02:20:49 · Speaker 2

Hmm

### 02:21:07 · Speaker 4

Hmm

### 02:21:08 · Speaker 2

Okay

### 02:21:10 · Speaker 4

In in in in most of these courses, right, our parametric models are neural networks only. Because they are expressive enough.

### 02:21:16 · Speaker 1

plus

### 02:21:18 · Speaker 4

Since neural networks are, I mean, we will we will see that neural networks are said to be universal function approximators. That means that you can use a neural network to approximate any function. That's a known result. Okay, that is why, you know, entire machine learning has moved towards neural networks because they are very good parametric models that you can have a neural network and set its parameter to represent any function.

### 02:21:41 · Speaker 4

Same thing goes for discriminative model also, right? Why did people move away from, see, initially people thought that okay, this can be modeled using a simple logistic regressor. It was not expressive enough. What if the final density function that you that you need, okay, for the given data, that happens to be something that a logistic regressor cannot model. Then you need to go to more models that are more flexible. That's why, you know, the today's state of the art is that P of P of Y given X, these the parameters

### 02:22:11 · Speaker 4

family that you assume on the underlying density are neural networks. or transformers or anything. those models are expressive enough that means that see.

### 02:22:21 · Speaker 4

No matter what you do, a Gaussian density can only represent this density, you know. I mean it can represent this, this, this and all that. But it is a unimodal density with different you only have two degrees of freedom to play with.

### 02:22:36 · Speaker 4

What if your under intensity has something like this? A Gaussian intensity can never, right?

### 02:22:45 · Speaker 4

no matter what mean and variance you play with. That is why you need the... GMM can express this of course, but right, I mean you need more complex models to represent this and that's why people use neural networks.

### 02:22:49 · Speaker 2

Course in External

### 02:23:00 · Speaker 4

Okay, so that's what is meant by parametric model that you just assume that my my my real density is one member of this family, large family that my parametric parametric model can express.

### 02:23:15 · Speaker 4

So basically if I model that as a neural network or a transformer I'm saying that my true density can be represented by one set of weights of this neural network. There exists one set of weights of this neural network that would represent my underlying density and I'm interested in finding that one set of weights.

### 02:23:33 · Speaker 4

Alright

### 02:23:35 · Speaker 2

Got it. Yeah.

### 02:23:36 · Speaker 4

Now how do I find that one set of weight is simply I fix a particular weight and I compute I see how far my density that I have gotten from this particular weight is from my true density and then I adjust my weight such that you know that measure becomes lesser and lesser. That is training no?

### 02:23:37 · Speaker 2

How do I

### 02:23:55 · Speaker 6

So yeah, a query here is when the when then we like try to optimize the minimize the particular variable that I understood. So if it is not minimizing properly.

### 02:24:05 · Speaker 4

divergence not variables call it call it divergence

### 02:24:07 · Speaker 6

Okay

### 02:24:09 · Speaker 6

Yeah, divergence. So, if I'm minimizing that divergence, say it is not minimizing up to my mark, will we need to go back and change the model again? I mean like, is it what the neutral... That's a good question.

### 02:24:10 · Speaker 4

Hmm

### 02:24:13 · Speaker 4

amazing

### 02:24:15 · Speaker 4

need to

### 02:24:19 · Speaker 4

That's a good question. Of course, of course you need to change. That is why, you know, you have like, you know, resnet thirty, resnet fifty, resnet hundred. Why did people make it deeper and different kinds of architectures is because my divergence is not getting minimized.

### 02:24:34 · Speaker 2

Okay

### 02:24:35 · Speaker 4

How do I know my divergence is not getting minimized is through some metrics, evaluation metrics like, you know, whatever, the accuracy, precision, etcetera. They are all surrogates to measure how, uh, how bad is your divergence, right? If it's bad, then go back and change your model, that's all. It means that, okay, maybe, uh, the model assumes, the parametric model assumption that you have made is not good enough. If you are using neural networks as your parametric families, the architecture is not good enough. Change the architecture, make it deeper, have more neurons. have more hidden layers etcetera

### 02:25:08 · Speaker 6

So, just to add on that point, just a maybe a little bit philosophical question. I mean like, what if it doesn't like, we can't model it using a parametric model at all. Maybe it's pure chaos kind of where we can't find a one which satisfies our divergence values.

### 02:25:28 · Speaker 4

Then we are doomed

### 02:25:29 · Speaker 6

Hmm hmm

### 02:25:30 · Speaker 2

Okay

### 02:25:31 · Speaker 4

So but but it it seems like all these you know transformers and billion parameter models are able to estimate the underlying divergence to a good level, no? That's why you have the boom of AI, right? I mean they are working. Which means that the divergence is minimizing.

### 02:25:50 · Speaker 6

Okay. Yeah. I was thinking as you said initial class maybe change the math. Just

### 02:25:56 · Speaker 4

Come again? No no no but I mean if the nature the the the mod see this week all this probabilistic way of thinking has taken us this far. You see? We have actually reached pretty far. We have very very strong models these days. Models that can crack International Mathematics Olympiad and get a silver medal. That's a very very strong model no?

### 02:26:19 · Speaker 1

Hmm

### 02:26:20 · Speaker 4

in model that can crack JEE. When we have such models, good things are happening. Right? So...

### 02:26:27 · Speaker 4

That's that's how the people that's how people did research right? I mean what was all this research all about is that changing the speech heater looking at different forms. Now changing divergence metrics different divergence metrics and changing the way this optimization problem is solved. That's only the three things that you can do no? Either you can change the model assumption or you change the divergence or you change the way you optimize. That is all people have been doing so far.

### 02:26:52 · Speaker 6

Yeah, I was thinking whether we like the more the parametric form itself we can define a new one kind of I mean like based on the inputs. People have done that.

### 02:27:00 · Speaker 4

People have done that, no? I mean like from MLPs, from logistic regressors they went to MLPs, from MLPs they went to CNNs and then RNNs and transformers what not and all these kinds of different model assumptions, right?

### 02:27:15 · Speaker 6

ओके. थैंक यू सर.

### 02:27:16 · Speaker 4

But the recipe itself has to be changed. I mean this is by the way this is also called divergence minimization or empirical risk minimization. People have tried to look at other ways of doing stuff as well but the thing that has worked the most and one which is there in practice today is this.

### 02:27:33 · Speaker 1

Sure. Thank you.

### 02:27:34 · Speaker 2

Thank you. Yeah. Lokesh.

### 02:27:43 · Speaker 2

Lokesh Kumar, can't hear you.

### 02:27:47 · Speaker 0

Hello

### 02:27:49 · Speaker 2

Yes, I can hear you now.

### 02:27:51 · Speaker 0

will we be always be able to come up with a divergence metric?

### 02:27:56 · Speaker 4

that we define, no? Yeah, see, if your question is, will we always be able to evaluate the divergence metric? The answer is no, that's why you need a lot of trick. All this GAN etcetera are actually kinds of tricks to evaluate this divergence metric. Will we be able to define a divergence metric? Of course, I will just right now I will define few metrics.

### 02:28:16 · Speaker 0

No, no, I meant I meant

### 02:28:18 · Speaker 4

evaluation no not necessary. No we can't no because there is one apparent problem with this. The apparent problem is that this divergence metric seems to ask for P X. We don't have P X. That's our whole problem.

### 02:28:19 · Speaker 0

No, not necessarily.

### 02:28:33 · Speaker 4

Right? Now how do we evaluate these revergence metrics when you don't have P X is the question that we are going to answer in this course. There are different tricks to do that. Many people generally compute a bound on this. You can't you can't find this exactly. So you compute an approximation to this which is computing a bound. That is what this evidence lower bound and all this expectation maximization V A E etcetera do. We will see all that in detail. You can always define it but can you can you compute it always? perhaps not depending upon what divergence metric are you looking at

### 02:29:08 · Speaker 4

That's the I mean see in this in the rest of this course we will only do this we will pick up E theta we will pick up D and we will see how to solve that optimization problem that's all. That's all we will do in this course next.

### 02:29:22 · Speaker 4

Okay

### 02:29:24 · Speaker 4

ओके, या, राघवेंद्र

### 02:29:27 · Speaker 7

Yes sir, the first question is, the choice of the original distribution, right, is also a model parameter. So for instance in this case,

### 02:29:34 · Speaker 4

choice of what

### 02:29:36 · Speaker 7

choice of the distribution, the original distribution that you try to fit. So, so here you try to fit the normal distribution.

### 02:29:41 · Speaker 8

to fit the

### 02:29:42 · Speaker 4

normal distribution

### 02:29:43 · Speaker 4

No, no, no. Please. See, one again, a kind request is, please don't try to use the terms that I have not defined. I have never told what do you mean by fitting.

### 02:29:56 · Speaker 4

Right? So I have defined learning, training, models, etcetera. Please try to use my terms anyway. So that that apart. See,

### 02:30:04 · Speaker 4

there is we are not making an assumption on P X. we are only saying that my P X I mean we are making an assumption on parametric form. We are just saying there exists a P theta, a family of P theta, okay? of which my P X is a member.

### 02:30:23 · Speaker 4

You get it? When I make an assumption, let's say that P theta is a normal distribution, I'm saying that my P X is also a normal distribution with certain mean and variance. That is the assumption that we are making. Understand? So if we if we

### 02:30:36 · Speaker 7

Yeah, but that is something that is something that we need to choose up front, right?

### 02:30:39 · Speaker 4

Let me complete

### 02:30:45 · Speaker 4

Hello

### 02:30:49 · Speaker 7

There is a lot of noise.

### 02:30:50 · Speaker 4

somebody army or that

### 02:30:53 · Speaker 4

Okay, so let me complete. I'm saying, suppose you may assume P theta to be a neural network. What I'm trying to say is that there exists a set of weights for this neural network which corresponds to my underlying P X.

### 02:31:07 · Speaker 4

Okay

### 02:31:11 · Speaker 7

Yeah

### 02:31:11 · Speaker 4

Now what is your question?

### 02:31:14 · Speaker 7

No, but again here we have chosen normal, right? And then the parameters are only mu and sigma.

### 02:31:20 · Speaker 7

right? But I could have chosen a different distribution also.

### 02:31:24 · Speaker 4

I told you, right? I mean, that is your model choice. You choose anything that you want. You you might

### 02:31:29 · Speaker 7

Yeah, but yeah, in general do we say that I mean the normal fits, I mean or the normal is the better candidate? We can't say at all.

### 02:31:37 · Speaker 4

We can't say at all. Definitely not. Because you know if you take MNIST and if you want to model it by normal distribution you are doomed. There is absolutely no way that there exists a mu and sigma that would make I mean that that that will give you the distribution of MNIST data.

### 02:31:41 · Speaker 7

Okay

### 02:31:54 · Speaker 7

So that is something that we need to decide based on the data.

### 02:31:58 · Speaker 4

I mean typically today people are like you have to have family P theta that is expressive enough. Okay. That would express a large class of density functions, no? Normal density does not express a large class of density functions at all.

### 02:32:06 · Speaker 7

Okay, that would exist.

### 02:32:13 · Speaker 7

Mm-hmm, okay.

### 02:32:15 · Speaker 4

Isn't it? Because it can't even express a binomial, I mean like bimodal distribution. It can only express monomodal, unimodal distributions. And most data will be by multimodal distribution, right?

### 02:32:22 · Speaker 7

model

### 02:32:27 · Speaker 7

Okay, and in case of neural network, can you just go a little down?

### 02:32:36 · Speaker 1

Ah

### 02:32:38 · Speaker 7

So so basically at the end you get a distribution but what you have shown here as the input is is the Z the the normal standard.

### 02:32:47 · Speaker 4

Yeah, so so what does that mean? This is one choice. Ha, so you have a neural network that would take normal distribution as an input and gives you a distribution as output.

### 02:32:47 · Speaker 7

So so what does that mean?

### 02:32:56 · Speaker 7

Okay

### 02:32:58 · Speaker 4

I'm modeling it that way, no? I can choose, see, P theta is our is in our hand. We can choose our P theta to be anything.

### 02:33:05 · Speaker 7

Mm-hmm

### 02:33:06 · Speaker 4

we we can choose it to be anything. Now if I choose it to be a neural network then there are large sets of distributions that my neural network can express.

### 02:33:07 · Speaker 7

Yeah

### 02:33:18 · Speaker 7

Okay. So so it's it's kind of showing that you are transforming the normal distribution to a some complex distribution using neural network.

### 02:33:25 · Speaker 4

neural net. YRDS neural net.

### 02:33:27 · Speaker 7

Okay

### 02:33:28 · Speaker 7

Yeah, okay, understood.

### 02:33:31 · Speaker 4

See even in discriminative models you do the same thing no you have to estimate P of Y given X. So you take a neural network.

### 02:33:40 · Speaker 4

you take a neural network, right? That would take x as an input and gives you p of y given x. This is exactly what a resnet etcetera does, no?

### 02:33:51 · Speaker 4

Now you can either make this P of Y given X one by one plus E power minus X, E power W transpose X or something in which case it becomes a logistic regressor. That is your P theta, right? The choice that you make on the model is what you call a model.

### 02:34:07 · Speaker 4

can make any choice for it. You can make it you can say that okay it's a logistic regressor you can take any parametric form for that and estimate the parameters that's all yeah.

### 02:34:19 · Speaker 4

Yeah, got it.

### 02:34:21 · Speaker 1

Okay, Rajat

### 02:34:27 · Speaker 2

Sir, my question is if we have some ways to identify the real P X.

### 02:34:34 · Speaker 1

Hmm

### 02:34:34 · Speaker 6

using some tricks or methods that and you told we'll discuss later in this course. Then I didn't what we will achieve by

### 02:34:41 · Speaker 7

by many divergence because knowing the real P X is something that we all interested in right

### 02:34:47 · Speaker 4

No, we can't. I mean, the whole problem is there is no way to know real periods. That's the whole problem.

### 02:34:56 · Speaker 2

then how we will

### 02:35:00 · Speaker 2

diverge, how we will calculate divergence?

### 02:35:03 · Speaker 4

have not told you that no I said yeah that is one problem that is one question that I will answer in a while

### 02:35:04 · Speaker 2

told you that no I said yeah

### 02:35:10 · Speaker 7

will directly sample from there. Try to sample.

### 02:35:14 · Speaker 4

please don't jump. There is a method to do. There is something called law of unconscious statistician and law of large number that we will use and we will use construct some bounds. Those are the things that we will do in this course. I have told you that that is some question that I will answer. Now how do you evaluate the divergence metric if you don't know P X is a question that I will answer. I have not answered that. Okay? But I want you to understand the philosophy, right? I mean like what is happening? You given data assume some parametric form on underlying P X.

### 02:35:44 · Speaker 4

compare the divergence metric and then adjust your parameters of your P theta such that this divergence metric is minimized

### 02:35:51 · Speaker 4

That's all. I mean, is this point clear? I mean, this is what I wanted to drive home. If this is clear, then the next question is, of course, what divergence metric, what form, how do you compute the divergence metric, etcetera, is what we teach in this course. Okay?

### 02:36:06 · Speaker 1

is a

### 02:36:07 · Speaker 2

is a

### 02:36:07 · Speaker 4

Okay, yeah, okay. Any other questions?

### 02:36:09 · Speaker 1

plus

### 02:36:19 · Speaker 1

Okay, now we'll take up the so now next question. Yes, given

### 02:36:29 · Speaker 1

a pair of density functions.

### 02:36:42 · Speaker 1

sensitive functions, how to measure

### 02:36:49 · Speaker 1

the distance or divergence between them.

### 02:37:04 · Speaker 1

Right? This is a question that we should answer now. Okay?

### 02:37:07 · Speaker 4

because uh one of the I mean there are three questions right how do you choose the model is the first question. Then the second one is how do you compute the divergence metric. The third thing is like how do you optimize right. I will take up the second question first. We'll we'll take all questions one by one. But uh this is more important right I mean this is the first step so given a pair of density functions how do you measure the distance or divergence between them is the question.

### 02:37:33 · Speaker 4

See there are in our I mean like many many ways to do this. So there are things called F divergences that we will be seeing.

### 02:37:46 · Speaker 4

Okay? And there are things called, you know, Versailles distance.

### 02:37:51 · Speaker 4

or optimal transport

### 02:37:56 · Speaker 4

and there are things called maximum mean discrepancy, MMD. Okay? Uh we will look at all of these one by one, okay? But yeah, so how do you estimate? So you understand, right? Suppose I've given you two points in Cartesian plane, how do I know how close and far off they are? Is that just compute the Euclidean distance, right? If this is uh x one, y one and this is x two, y two, then you know how to compute the distance between them, right? x one minus x two squared, whatever, the usual Euclidean distance.

### 02:38:26 · Speaker 4

Now if you are given two density functions, how do you define, how do you measure divergences or distance between them is the question, okay?

### 02:38:37 · Speaker 4

what we will do is uh

### 02:38:42 · Speaker 4

Okay. I will start with one famous divergence metric. Okay, so here is a question that I want to ask you. Maybe I should not ask you that but see, uh as I said in this course, we will be looking at uh models like VAEs and GANs and diffusion models and and so on, right? uh Which one do you want to start with? Do you want to start with GANs and then go to VAEs or

### 02:39:12 · Speaker 4

V A E S and then go to the answer. So typically

### 02:39:15 · Speaker 2

So first gains then gains

### 02:39:17 · Speaker 4

typically I used to do that. I used to start with V A E's and then go to Gyaans. But uh this time I'm just thinking I should do the other way around. I'll tell you the reason. The reason is these diffusion models, right? Diffusion models are special cases of V A E's. They're actually hierarchical V A E's with a fixed uh encoding process. So now if I do V A E's uh and then do diffusion models, right? I mean you will it will be fresh in your memory and I don't have to repeat things that I have done for V A E's. So now

### 02:39:47 · Speaker 4

what perhaps we will do is you know GANs are a very different class of models and they are sort of like out of trend now. People are not looking at GANs because of the problems that it comes with. So let us start with adversarial learning okay. And perhaps then we will go to VIs.

### 02:40:06 · Speaker 4

So having said that, uh I will simply give you uh I mean an example of how to look at the divergence metric, right? And how to compute that, etcetera. And then from next class we will go to adversarial learning, okay? So okay, so now let's take up this question. Given a pair of density functions, how to measure distance between them is the question, okay? Now to do that, let us look at this.

### 02:40:34 · Speaker 4

Suppose

### 02:40:37 · Speaker 2

Okay

### 02:40:39 · Speaker 2

there is an event

### 02:40:41 · Speaker 2

A, okay? That is in the set of events.

### 02:40:46 · Speaker 1

F. Okay? And I'm interested in

### 02:40:56 · Speaker 1

in a measure

### 02:41:00 · Speaker 1

that quantifies

### 02:41:07 · Speaker 1

D

### 02:41:09 · Speaker 1

amount of information.

### 02:41:15 · Speaker 1

amount of information

### 02:41:20 · Speaker 1

associated with it.

### 02:41:28 · Speaker 1

Okay

### 02:41:29 · Speaker 4

understand so what are we trying to do now we are actually trying to derive a famous divergence metric between two distributions which is called the kill back labor divergence or KL divergence okay and to do that you know we need some concepts of like basics of information theory okay I'm just trying to derive that so that you understand where this actually came from okay now suppose there is an event that is there in the in the in the event event space and what you are interested in is are interested in in a measure that would quantify the amount of information associated with it.

### 02:42:06 · Speaker 4

Okay. Now that measure let's call that as some I of A. See what properties do you seek in such a measure? I would say that the should be high.

### 02:42:19 · Speaker 4

for

### 02:42:21 · Speaker 1

less probable events.

### 02:42:29 · Speaker 1

should be low for

### 02:42:33 · Speaker 1

high probable events.

### 02:42:38 · Speaker 4

Do you agree? See if I have to quantify the amount of information associated with a particular event, that measure has to be very high for less probable events, right? I mean, what I what I'm trying to say is if I tell you that you know the sun rises in the west tomorrow, then it has a lot of information in it, isn't it? But if I tell you that the sun rises in east,

### 02:42:59 · Speaker 2

tomorrow then it does not have any information. Do you see what I mean?

### 02:43:09 · Speaker 2

So now this information measure that I associated with associated

### 02:43:13 · Speaker 4

with a particular metric has to be such that it should be high for less probable events and low for high probable events. Now, uh if you take the asymptotic cases of it, right? So the information that is associated with the entire sample space should be one.

### 02:43:35 · Speaker 4

or let's say okay it can be that also no yeah it can be infinity right it should be very high because the probability of sample space is one right

### 02:43:46 · Speaker 4

The probability of sample space is one. Because something when you when you when you conduct the random experiment some outcome will come that is what this is saying so the information that is associated with the sample space has to be infinity and the information that is associated with the null should be zero.

### 02:44:05 · Speaker 4

because I mean if I or the other way around no sorry I think I've switched it sorry

### 02:44:15 · Speaker 4

The information associated with the sample space has to be zero. The information associated with the null should be infinity. Correct? That's the asymptotic case of what I've just mentioned. You know, if I say that something from the sample space always happens, of course, I'm not telling you anything. If I say that, you know, something from the null space happens, then the null set happens and I'm giving you infinite information. The other property has to be that the amount of information, right?

### 02:44:41 · Speaker 2

that is associated with the

### 02:44:49 · Speaker 2

free

### 02:44:51 · Speaker 1

the intersection that two events happen should be equal to the individual

### 02:45:06 · Speaker 1

Excuse me for this.

### 02:45:10 · Speaker 1

the information

### 02:45:10 · Speaker 4

associated with two events union of two events happening have to be equal to the individual sum of individual informations if they are mutually

### 02:45:23 · Speaker 4

Independent

### 02:45:26 · Speaker 4

This makes sense, right? I mean they have to add up. Basically I'm saying that if there are two events happening together and if they are mutually exclusive, then the total information that is conveyed by both of them has to be the sum of information conveyed by individuals of them. Does it make sense?

### 02:45:44 · Speaker 6

सर, शुड इट बी आई ऑफ ए इंटरसेक्शन बी इक्वल टू नल सेट और जस्ट ए इंटरसेक्शन बी इक्वल टू नल?

### 02:45:49 · Speaker 4

Oh yeah yeah yes

### 02:45:52 · Speaker 4

Thanks. This is what it is. Yeah, thanks for that. For typo. Okay. This is okay, right? Now, in fact, I mean, this these measures were proposed by Shannon, okay, a great information theorist who is responsible for all the communication that we have today, that he defined this thing, right, to be surprising of a particular event as the negative of logarithm of the probability, okay?

### 02:46:20 · Speaker 4

associated with that particular event A. We should not be writing this as script P because we have taken the script P for

### 02:46:28 · Speaker 4

Hmm

### 02:46:30 · Speaker 4

distribution functions, right? It's the probability of this event A.

### 02:46:38 · Speaker 4

Can you just take a minute and uh convince yourself that it it will

### 02:46:44 · Speaker 2

Uh, uh,

### 02:46:49 · Speaker 1

satisfy all three properties that we saw.

### 02:47:05 · Speaker 1

just take a minute and verify this.

### 02:47:27 · Speaker 1

Is it clear to all of you?

### 02:47:33 · Speaker 1

Okay

### 02:47:39 · Speaker 1

Okay, so this is for one event, right? So now suppose

### 02:48:00 · Speaker 1

those need to quantify

### 02:48:08 · Speaker 1

the information

### 02:48:14 · Speaker 1

in

### 02:48:16 · Speaker 2

distribution, right?

### 02:48:20 · Speaker 2

What do we do? This is for one event, right? If we want to do it for the entire distribution, how do we do that?

### 02:48:32 · Speaker 1

integrate all the values.

### 02:48:35 · Speaker 2

Yeah, just take an average, right, over all events.

### 02:48:41 · Speaker 2

So

### 02:48:41 · Speaker 1

let's say that this is a discrete display I'll do it on a discrete distribution in a

### 02:49:07 · Speaker 1

in a discrete let's say that it's a discrete distribution for the ease of understanding. discrete distribution.

### 02:49:19 · Speaker 4

Right? So now P M F are probabilities, right? So I'll say that I'll have to look at the negative of log of the P M F function associated with particular value X I, okay? I look at this and I take an average of this with all possible values that is.

### 02:49:42 · Speaker 4

which is

### 02:49:45 · Speaker 4

p x of x i and just simply take the sum

### 02:49:50 · Speaker 4

of

### 02:49:53 · Speaker 2

the values that it can take. So this will quantify the average information.

### 02:50:04 · Speaker 1

information associated

### 02:50:08 · Speaker 1

with

### 02:50:11 · Speaker 1

the distribution

### 02:50:17 · Speaker 1

P X

### 02:50:19 · Speaker 4

Do you agree?

### 02:50:21 · Speaker 4

this should give you so because a negative log of p x i will give you the information associated with one event. one outcome. to take the average of it over all the possible outcomes then you will get the average information that is associated with the entire distribution.

### 02:50:39 · Speaker 4

Okay?

### 02:50:39 · Speaker 1

people have questions here. Let me take question.

### 02:52:09 · Speaker 1

Yeah

### 02:52:09 · Speaker 2

go on with questions.

### 02:52:15 · Speaker 8

सर, आई डिडंट गेट व्हाई दैट इंफॉर्मेशन एसोसिएटेड विद नल्स दैट इज इन्फिनिटी एंड आल्सो व्हाई इंफॉर्मेशन एसोसिएटेड विद इवेंटिटी

### 02:52:24 · Speaker 1

is minus log of probability A

### 02:52:41 · Speaker 1

Okay, I'm muted. Just give me a second, I'll answer that.

### 02:52:48 · Speaker 2

We can hear you sir

### 02:52:51 · Speaker 1

Hello, can you hear me?

### 02:52:53 · Speaker 2

Yes sir, we can hear you.

### 02:53:01 · Speaker 1

Give me a minute

### 02:53:11 · Speaker 1

Hello, can you hear me now?

### 02:53:14 · Speaker 8

Yes sir, we can hear you.

### 02:53:16 · Speaker 4

Okay. See, the thing is, uh this is our definition. See, what I want is I want a measure that would take very high value for less probable events. It will take very low values for high probable events. Okay? That is the measure that I want. Now...

### 02:53:36 · Speaker 4

the asymptotic case, asymptotic case, which is the extreme case is the following, that if you take the entire sample space.

### 02:53:43 · Speaker 4

take the entire sample space, then that is the most

### 02:53:47 · Speaker 2

probable event isn't it?

### 02:53:51 · Speaker 1

Yes, that will be

### 02:53:53 · Speaker 2

that should have zero information.

### 02:53:58 · Speaker 2

Okay? Similarly, the least probable event, which is the null, should have infinite information.

### 02:54:09 · Speaker 8

I understand the probability part but how come that gets reversed when we associate with the information?

### 02:54:19 · Speaker 4

That is how we want, right? See now, what are we desiring? See, okay. So I'll tell you some historical thing, right? The question that was asked is, if you if you if you say that an event has happened, you tell me how much information is conveyed in that is the question.

### 02:54:37 · Speaker 4

Now intuitively don't you think that an event that has very high probability or which is very high which is very highly probable conveys very less information?

### 02:54:51 · Speaker 4

historically what happened is the question Shannon was asking is if I have to compress the I suppose I want to you know I want to pass a message from point A to point B and I want to understood now

### 02:55:02 · Speaker 8

understood now

### 02:55:04 · Speaker 4

Got it, no? It's easy. Now I understand.

### 02:55:05 · Speaker 8

Now I understood.

### 02:55:07 · Speaker 4

Okay. Yeah. So, I mean, we defined the information this way, information content associated with an event this way, that it is the negative of log of probability associated with A.

### 02:55:18 · Speaker 1

That's all

### 02:55:21 · Speaker 1

Okay

### 02:55:27 · Speaker 1

ओके, आस्तिक

### 02:55:29 · Speaker 10

Uh yeah, so I got it that we found out that this information about information of A is minus log of probability of A, but how does this union property satisfy with this?

### 02:55:44 · Speaker 4

I'll just look at it, no? uh the probabilities get multiplied if the events are independent and there is a log, right? So log will get summed.

### 02:55:55 · Speaker 4

probability of A and B log of A B is log A plus log B, isn't it?

### 02:56:01 · Speaker 10

Okay okay if they are distinct okay okay yeah I understand

### 02:56:05 · Speaker 10

Hmm

### 02:56:05 · Speaker 4

That's that's why I give you a minute to just plug that in. Yeah yeah I forgot that they are

### 02:56:08 · Speaker 10

Yeah yeah I forgot that they are disjoint also so yeah okay yeah

### 02:56:12 · Speaker 4

Okay Sachin

### 02:56:13 · Speaker 10

Yeah, thank you.

### 02:56:15 · Speaker 5

सर, इन दिस एवरेज फंक्शन, विल इट बी लाइक कैपिटल पी, राइट? दिस स्मॉल पी वाज़ फॉर प्रोबेबिलिटी डेंसिटी।

### 02:56:18 · Speaker 4

Hmm

### 02:56:23 · Speaker 4

I am saying it's a discrete distribution, right? So this is P M F, probability mass function, which is a probability by itself.

### 02:56:33 · Speaker 5

Sorry, can you tell me?

### 02:56:34 · Speaker 4

See, I said that it is a discrete distribution, therefore this P is a PMF function, probability mass function, which is, it is actually a valid probability.

### 02:56:43 · Speaker 1

took

### 02:56:44 · Speaker 2

Hello

### 02:56:48 · Speaker 1

right

### 02:56:58 · Speaker 1

ओके संकेत

### 02:57:01 · Speaker 9

Yeah, so this union property that is there, basically I A union B is I A plus I B. But if we consider union of A with null set, means this the intersection will also be null. But then this property will not hold, no? Because A union null will be A itself. But then if we add them up, it will be infinity.

### 02:57:27 · Speaker 4

no a union null is no a union null is a okay you can still represent that as i of a plus i of null right

### 02:57:37 · Speaker 9

But I of null is infinity, no? So I of A plus I of null will be infinity.

### 02:57:39 · Speaker 4

I of A plus

### 02:57:46 · Speaker 4

the same

### 02:57:47 · Speaker 2

Um, I

### 02:57:48 · Speaker 1

I mean maybe I should just add that

### 02:57:50 · Speaker 2

but or

### 02:57:55 · Speaker 1

So, yeah, that will solve it. That's an H case.

### 02:57:59 · Speaker 2

Right?

### 02:57:59 · Speaker 2

Hmm

### 02:58:01 · Speaker 4

ஆதித்ய

### 02:58:04 · Speaker 3

uh so similar there's an add on to that question if B was for example an A complement over here. So I of A plus I of A complement that would equal to I of omega the like the whole subspace so that should be zero right?

### 02:58:16 · Speaker 4

sub space

### 02:58:20 · Speaker 4

Yeah, of course.

### 02:58:21 · Speaker 3

Okay

### 02:58:23 · Speaker 4

Postpartum Definition

### 02:58:25 · Speaker 2

Okay, so now, uh, there's a name for this. Do you know what this is called?

### 02:58:38 · Speaker 2

Sorry, let's go

### 02:58:42 · Speaker 2

sorry this is called intro

### 02:58:42 · Speaker 1

is called

### 02:58:43 · Speaker 4

internet

### 02:58:43 · Speaker 4

Entropy, yeah, this is called entropy.

### 02:58:44 · Speaker 1

Enthropy

### 02:58:47 · Speaker 4

This is the entropy associated with the distribution. That is, it's simply the average information that is associated with the distribution is called the entropy of the distribution.

### 02:58:56 · Speaker 4

makes sense, no? makes a lot of sense. So basically you define the information content uh for an event and you just take take an average over all possible events that are there and that will give you the entropy which is the average information.

### 02:59:10 · Speaker 2

that is conveyed by a distribution. That's fine.

### 02:59:19 · Speaker 2

Okay. So now I actually have to now define the cross entropy and

### 02:59:24 · Speaker 4

in

### 02:59:26 · Speaker 4

one it's twelve twenty already. We started fifteen minutes late. Do you mind if I continue for ten more minutes or should I stop? Shall we take it to the next class?

### 02:59:38 · Speaker 4

See, if there is even one person who wants me to stop, no, I will stop.

### 02:59:43 · Speaker 4

because it should not be

### 02:59:45 · Speaker 1

continuing

### 02:59:47 · Speaker 1

Is there anybody who wants me to stop now?

### 02:59:56 · Speaker 1

Let me know if you

### 03:00:00 · Speaker 3

somewhere and you have hard stop I'll stop it here.

### 03:00:07 · Speaker 1

So let me take ten more minutes. Now, suppose

### 03:00:30 · Speaker 1

co-density properties

### 03:00:37 · Speaker 1

Free and Q

### 03:00:39 · Speaker 1

Now if I compute

### 03:01:02 · Speaker 1

looks like my screen has frozen.

### 03:01:30 · Speaker 1

What do you think this will give you?

### 03:01:41 · Speaker 1

And somebody tell me what does this give me?

### 03:01:47 · Speaker 1

Can I interpret this as

### 03:02:00 · Speaker 1

Can I interpret this it this way? Can I say that it's the average information in Q about P?

### 03:02:13 · Speaker 1

Can all of you see this?

### 03:02:16 · Speaker 2

Yes

### 03:02:18 · Speaker 1

Right? This also has a name. Do you know?

### 03:02:23 · Speaker 2

Cross entropy

### 03:02:24 · Speaker 1

cross and trophy

### 03:02:33 · Speaker 1

between P and Q

### 03:02:36 · Speaker 1

Now, if I take this,

### 03:02:42 · Speaker 1

and subtract by this

### 03:02:45 · Speaker 1

How do I interpret this?

### 03:02:52 · Speaker 1

Can I say that this is the information

### 03:02:58 · Speaker 1

that this is the extra information.

### 03:03:14 · Speaker 1

in P

### 03:03:16 · Speaker 1

साठ

### 03:03:19 · Speaker 1

this

### 03:03:20 · Speaker 1

not in Q. Can I call it this way?

### 03:03:32 · Speaker 2

Sir, the first term tells us about like gives us the information about Q, right?

### 03:03:39 · Speaker 3

information about uh P like first you know here here cross entropy is a cross entropy tells you that how much information does Q has about P

### 03:03:54 · Speaker 1

No, about means like

### 03:03:56 · Speaker 3

Like

### 03:04:01 · Speaker 1

Okay

### 03:04:02 · Speaker 3

Right? And H of P tells you the information in P.

### 03:04:08 · Speaker 3

If we take the difference between them,

### 03:04:10 · Speaker 3

it will tell me how much extra information is there with P that

### 03:04:17 · Speaker 3

the Q does not have.

### 03:04:20 · Speaker 1

and it should be subtracted by h q, right? Sorry. The terms should be reversed, right?

### 03:04:23 · Speaker 2

Sorry

### 03:04:26 · Speaker 3

I mean HP minus HQ is it?

### 03:04:29 · Speaker 1

Okay

### 03:04:30 · Speaker 2

HP minus HPQ

### 03:04:33 · Speaker 2

otherwise like this inter like this this is giving a sense that the term will be negative.

### 03:04:40 · Speaker 2

Wanted sir

### 03:04:40 · Speaker 3

Hold on, hold on, hold on. See, there is a minus log there, no?

### 03:04:48 · Speaker 1

minus log also it should be

### 03:04:55 · Speaker 1

right this one how how does this look like? This is

### 03:05:14 · Speaker 1

This is correct. Because there is a negative there, no?

### 03:05:22 · Speaker 3

So in the definition of entropy there is a minus. So when you subtract it the minus will just go away and it will become plus.

### 03:05:30 · Speaker 3

understand? So basically the difference between these two will tell you the extra information in P that is not in Q.

### 03:05:37 · Speaker 3

Is that okay?

### 03:05:41 · Speaker 1

of this is equal to

### 03:05:45 · Speaker 1

I

### 03:05:59 · Speaker 1

This is correct, no? So there's a minus here.

### 03:06:03 · Speaker 3

there is a minus of minus will become plus so it will be p of px log px and this term has a negative here so log a minus log b

### 03:06:12 · Speaker 1

log of a by b. Is this okay?

### 03:06:24 · Speaker 1

Do you know the name for this? This has a name. This is the

### 03:06:29 · Speaker 1

field

### 03:06:30 · Speaker 3

Yeah

### 03:06:35 · Speaker 3

This is one divergence metric that we will study in this course. That the KL divergence between these two distributions, P X and Q X.

### 03:06:48 · Speaker 3

simply given by

### 03:06:51 · Speaker 3

X log

### 03:06:56 · Speaker 3

In fact, this is the last function that is used in most of the supervised discriminative machine learning to minimize the KL divergence between P X and P theta.

### 03:07:07 · Speaker 3

Okay? See, the reason I did all this is to make you appreciate why this is a good metric. So, I'll leave it for tutorials, okay? To show that KL is zero if and only if

### 03:07:22 · Speaker 3

p x matches q x.

### 03:07:24 · Speaker 3

only if the distributed the underlying distributions matches then the divergence will become zero. obviously right because the amount of information that is there in Q about P should not be more than what P has itself.

### 03:07:40 · Speaker 3

So only if P and Q are exactly the same distributions, then the cross entropy matches with the entropy. And that is when the KL divergence becomes zero. So now this becomes a metric to measure how far a given distributions are.

### 03:07:57 · Speaker 3

Now we will trace back to what we did. So we wanted to define or compute a divergence metric between the true density and the assumed parametric density, you know, to quantify how far it closed. K L is one way to do it.

### 03:08:12 · Speaker 3

Does it make sense?

### 03:08:15 · Speaker 3

So in the next class what we will do is that given a particular model how do you compute the K L and how do you optimize for it etcetera is something that we will see in the next class. Okay. So

### 03:08:27 · Speaker 3

When you come to the next class, please come prepared, you know, just read whatever we have done the in the previous classes and also read about entropy, cross entropy, K L, etcetera, so that you you have idea about what we are talking. Okay?

### 03:08:45 · Speaker 3

Okay then, we are done for today. See you in the next class and again reminding right if you want to express something, you know, have some opinion, the feedback form is there. It is completely anonymous. You can just go and put in whatever your comments are if you want. You go to my web page. There is this ADRL course web page and there is that that feedback form and you can just simply put in your comments if you have any.

### 03:09:14 · Speaker 3

Okay, that's all for today. See you next week.

### 03:09:18 · Speaker 3

Have a nice week. Bye bye.

### 03:09:21 · Speaker 1

Thank you sir

### 03:09:21 · Speaker 2

Yet

### 03:09:22 · Speaker 3

just a second. next week just a minute next Saturday is is this Ganesh Chaturthi. That's okay right we can still have a class.

### 03:09:24 · Speaker 1

Thank you so much

### 03:09:26 · Speaker 1

so

### 03:09:36 · Speaker 1

I think that's

### 03:09:36 · Speaker 2

I think that's

### 03:09:38 · Speaker 3

Okay. Okay, anyway we are recording, if people want to take off, they can take off and see that later.

### 03:09:45 · Speaker 3

I'll have to ask my mother if that is possible, but yeah, I'll convince her. Okay, see, bye.

### 03:09:53 · Speaker 1

Paisa

### 03:09:55 · Speaker 2

बस थैंक यू सर

### 03:09:57 · Speaker 3

Thank you

### 03:09:58 · Speaker 3

Thank you, sir.

### 03:09:58 · Speaker 2

Thank you sir
