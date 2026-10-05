---
id: 8qzXJh2owLU
title: Lec 4 - Deep Generative Models Variational Divergence Minimization
date: '2024-11-23'
url: https://www.youtube.com/watch?v=8qzXJh2owLU
description: ''
author: prathoshap5226
duration: 03:03:52
model: saaras:v3
transcript: true
---

# Lec 4 - Deep Generative Models Variational Divergence Minimization

## Transcript

### 00:00:03 · Speaker 8

Okay? There will be fifteen questions, fifteen to twenty questions. And we'll give you twenty, twenty five minutes to solve it. Okay? Multi-choice questions. The first quiz will happen next week.

### 00:00:15 · Speaker 8

Okay

### 00:00:17 · Speaker 10

Is it possible sir if you can share some sample questions?

### 00:00:23 · Speaker 8

Well, it's it's simply uh can, but it's when there are factual questions on things that that has been covered so far in the class. So if you brush up whatever has been covered in the class, that should be enough.

### 00:00:37 · Speaker 11

Okay

### 00:00:43 · Speaker 8

Okay, let us start now today's class. Sorry for interrupting.

### 00:00:45 · Speaker 11

Sorry for interrupting. Just one question. So you said next Sunday. Is it next Sunday or Saturday?

### 00:00:50 · Speaker 8

I mean, yeah,

### 00:00:52 · Speaker 3

back next Saturday next week

### 00:01:01 · Speaker 6

Um, so one more question I had. So, uh, whatever we cover in today's class is also gonna be included?

### 00:01:09 · Speaker 8

Of course

### 00:01:10 · Speaker 6

Okay. And sir, uh I remember we have already discussed this in length but uh on the first class there was a lot of back and forth between what was the final decided grading policy. If you can just summarize it quickly once again for a sake of clarity it will be really helpful.

### 00:01:23 · Speaker 8

Clean

### 00:01:25 · Speaker 8

No, please don't do this. We have done this. No, there is it is documented, it is written down. You look at this.

### 00:01:34 · Speaker 6

Okay this is fine right? Of course

### 00:01:34 · Speaker 8

Okay, this is fine, right? Of course, right? I wrote it and said that this is fine and we are not going to discuss this anymore. Please don't do that. Thank you, sir.

### 00:01:41 · Speaker 3

Sure, Sir. Thank you, Sir.

### 00:01:43 · Speaker 8

Okay, so it is there, it is written, just have a look at it.

### 00:01:48 · Speaker 8

I see one other hand raised. Nirmith, please go on.

### 00:01:51 · Speaker 5

Uh yeah, so sir, for the quiz, will there be like we have studied sigma algebra, Borel, sigma, so will there be calculation for this or only as you said factual?

### 00:02:08 · Speaker 3

am I audible?

### 00:02:16 · Speaker 4

Sir, your audio is not very clear.

### 00:02:19 · Speaker 5

Yes, we are you are breaking.

### 00:02:23 · Speaker 3

Hello, is this it okay? I'm having some problem with my internet today. Just a minute, give me a minute.

### 00:02:37 · Speaker 3

Hello, am I audible?

### 00:02:39 · Speaker 4

yes

### 00:02:40 · Speaker 5

now you are

### 00:02:42 · Speaker 8

Okay, in my internet's close. Yeah, I said it is just your it's about testing what you have understood.

### 00:02:53 · Speaker 8

from whatever has been taught, okay? It will mostly be factual with

### 00:03:00 · Speaker 8

three four options for each

### 00:03:02 · Speaker 3

question and there will be fifteen questions and twenty minutes okay? That is what's going to be

### 00:03:05 · Speaker 4

Okay

### 00:03:07 · Speaker 4

Yeah

### 00:03:14 · Speaker 3

Okay, let us start then.

### 00:03:17 · Speaker 3

Hope that you see my screen. And last class just a quick recap.

### 00:03:23 · Speaker 4

Hello

### 00:03:34 · Speaker 4

Yeah. In last class,

### 00:03:35 · Speaker 8

first we define what generative modeling is. uh we are given data from an unknown distribution, okay? what we wanted to do is to estimate the unknown distribution and also sample from it. okay? that was the problem that we wanted to solve.

### 00:03:55 · Speaker 8

Okay. So, uh we wanted to do it from the uh from the perspective or angle of what I called as divergence minimization.

### 00:04:06 · Speaker 8

where the idea was to assume a parametric form for the density function to be estimated, denoted by P theta, right?

### 00:04:16 · Speaker 8

where theta are the set of parameters that are representing the underlying distribution.

### 00:04:24 · Speaker 8

Okay, so we have P theta that represents the distribution that we are modeling and we call this the model distribution. And it can be any parametric distribution such as a Gaussian distribution or even a neural network, okay, that would take some random variable as input and the output of that neural network is the distribution of the output of the neural network is taken to be P theta.

### 00:04:53 · Speaker 8

Then we said, okay, once you have this parametric model, you define

### 00:04:58 · Speaker 4

Okay, I think there's a typo here.

### 00:05:18 · Speaker 4

Hmm

### 00:05:21 · Speaker 4

Hmm

### 00:05:31 · Speaker 4

is just not

### 00:05:36 · Speaker 4

somebody tell me what's wrong

### 00:05:39 · Speaker 4

I'm not seeing any of these outcomes.

### 00:05:47 · Speaker 3

Are you not able to scroll

### 00:05:48 · Speaker 5

ball

### 00:05:50 · Speaker 3

I'm able to scroll. Actually not able to scroll also now.

### 00:05:57 · Speaker 3

Now I can square. Okay, okay. There was a typo here.

### 00:06:03 · Speaker 8

Define and compute

### 00:06:06 · Speaker 8

Nice

### 00:06:07 · Speaker 8

define and compute a distance or divergence metric between the true distribution and the assumed parametric density function, true density function and parametric density function, okay? That would tell you how close or far px and p theta are where px is the true distribution, p theta is the distribution of interest, okay? And then you adjust or compute the parameters of p theta such that this divergence minimizes, divergence metric is minimized. Okay?

### 00:06:37 · Speaker 8

computing the parameters of P theta such that this is minimized is what is called as training or learning of the model. Okay.

### 00:06:45 · Speaker 8

Mathematically, it is solving an optimization problem over the space of the parameters of the intensity that we have assumed. Okay? Yeah. So the final estimate of P X is P theta star, where theta star is the set of parameters that we have obtained by solving the above optimization problem.

### 00:07:07 · Speaker 8

Okay? That is what we saw. um And also we quickly saw one definition, one of the uh possible uh definition for the divergence method, which which we call the Kullback-Leibler divergence or KL divergence. Okay? uh Okay, so I want you to, I'll stop here for a minute and I want you to uh let me know if you have any questions on this general philosophy of divergence minimization because

### 00:07:38 · Speaker 8

that will be the central theme of most of the models that we'll be seeing in this course. Right? We start with a parametric form for the density, okay, that we want to estimate. And we define a divergence metric. Now that divergence metric becomes a function of the uh the parameters of the underlying density. Then we compute the uh or rather we get the parameters or

### 00:08:04 · Speaker 8

of the density by minimizing the divergence metric between the true density and the parametric density.

### 00:08:12 · Speaker 8

So that is the idea. Any questions?

### 00:08:14 · Speaker 4

sense of this

### 00:08:16 · Speaker 4

Before we move on

### 00:08:55 · Speaker 4

Am I audible? Hello?

### 00:08:58 · Speaker 3

Yes sir

### 00:09:00 · Speaker 4

Okay. No questions. Okay.

### 00:09:02 · Speaker 3

Let us move on then.

### 00:09:10 · Speaker 8

Okay

### 00:09:12 · Speaker 8

Now we will look at the first class of family of generative models that we will see which are called adversarial generative models are also called as generative adversarial networks or GANs, okay? So what is the idea there? So same thing, right? So

### 00:09:29 · Speaker 4

what we will do is we will

### 00:09:39 · Speaker 4

Given

### 00:09:45 · Speaker 4

data, okay? So what is data? Data are

### 00:09:50 · Speaker 4

some samples.

### 00:09:58 · Speaker 4

Tron from

### 00:10:00 · Speaker 4

known distribution.

### 00:10:06 · Speaker 4

What can these be? These are examples of

### 00:10:15 · Speaker 4

majors of digits or

### 00:10:19 · Speaker 4

is what is there in MNIST data set.

### 00:10:25 · Speaker 4

can be

### 00:10:32 · Speaker 4

some features

### 00:10:33 · Speaker 8

of text and so on, right? It can be anything. They are given in

### 00:10:38 · Speaker 3

data points of

### 00:10:39 · Speaker 8

end data points drawn from unknown distribution, okay?

### 00:10:44 · Speaker 4

rule

### 00:10:49 · Speaker 4

cool is to

### 00:10:56 · Speaker 4

estimate p x and remember we are solving generative modeling here and

### 00:11:02 · Speaker 4

sample from P X

### 00:11:09 · Speaker 4

Okay? Now what do you mean by sampling from P X is that generate

### 00:11:20 · Speaker 4

more samples from P X.

### 00:11:28 · Speaker 4

It's okay that

### 00:11:32 · Speaker 4

or

### 00:11:35 · Speaker 3

not in D

### 00:11:38 · Speaker 3

So given data set

### 00:11:39 · Speaker 8

but you want to generate more samples from the data set. Okay, that are not a part of the data set. Okay, that is, that is what we want by, that is what we need to call by sampling. Okay.

### 00:11:54 · Speaker 8

Okay. Now what is the idea? So first, first step to do this is that

### 00:12:01 · Speaker 3

Hello

### 00:12:01 · Speaker 4

June

### 00:12:05 · Speaker 4

a parametric form

### 00:12:13 · Speaker 4

on

### 00:12:17 · Speaker 4

ax call it p theta

### 00:12:25 · Speaker 8

Okay, this is what we start

### 00:12:27 · Speaker 3

Now, in the class of generative models known as

### 00:12:31 · Speaker 8

adversarial network.

### 00:12:33 · Speaker 4

How do we get P theta? So, in

### 00:12:52 · Speaker 4

Okay. P theta is represented by neural network.

### 00:13:05 · Speaker 4

deep neural network

### 00:13:16 · Speaker 4

Okay, it means that there's a neural network

### 00:13:25 · Speaker 3

See whenever I write neural network thread in this course from now on, uh I would be assuming

### 00:13:36 · Speaker 3

I'll be following this convention that I will write these kinds of

### 00:13:40 · Speaker 8

quadrilaterals, right, trapeziums, and the shape will be proportional to the dimensionality of the data.

### 00:13:48 · Speaker 3

I can't write a straight line

### 00:13:52 · Speaker 3

Wow

### 00:13:56 · Speaker 3

better. Okay.

### 00:13:59 · Speaker 3

Now what is happening here is that okay so let

### 00:14:03 · Speaker 8

before I move on, uh I am assuming that all of you know how the error back propagation algorithm works, right? How to train neural networks? Is there anybody?

### 00:14:16 · Speaker 3

who does not know how to perform gradient descents on neural networks.

### 00:14:27 · Speaker 3

rather I will just make it a

### 00:14:30 · Speaker 8

see do we need yeah Nirmith you raised your hand

### 00:14:34 · Speaker 5

I mean I don't know, but if we can have tutorial on that that would be good.

### 00:14:41 · Speaker 8

I can, but that's why I'm asking, right?

### 00:14:43 · Speaker 3

We need a tutorial on back propagation algorithms

### 00:14:47 · Speaker 5

Yes. I yeah.

### 00:14:52 · Speaker 3

Okay Kartik

### 00:14:56 · Speaker 4

Yes, I was seeing, Yeah, I was just

### 00:14:56 · Speaker 3

Same

### 00:15:00 · Speaker 8

So you haven't tried neural networks before, is it?

### 00:15:05 · Speaker 4

Yeah

### 00:15:06 · Speaker 8

No

### 00:15:08 · Speaker 6

Sir, we are broadly aware of how it like what it's supposed to do but not with the same level of mathematical rigor that this course is going on with.

### 00:15:21 · Speaker 8

Okay, so let us make that

### 00:15:25 · Speaker 8

an item of tutorial then we will

### 00:15:29 · Speaker 8

teach back propagation. Okay, so

### 00:15:35 · Speaker 8

it is mostly uh repeated application of chain rule, okay? uh that is that is that is what it is, okay? But yeah, I will ask them to have a tutorial on blackbob. Okay. Uh that apart, um so I said now P theta will be represented using neural networks, okay? So now let us call this as some G theta of G, okay? Now let's say that you have

### 00:16:05 · Speaker 8

which is a random variable that is that has a Gaussian distribution associated with it, okay?

### 00:16:13 · Speaker 8

Now typically

### 00:16:16 · Speaker 8

Okay, I'll come to that.

### 00:16:17 · Speaker 3

Now we have this position that, uh, suppose

### 00:16:26 · Speaker 3

Z is a

### 00:16:27 · Speaker 4

random variable with

### 00:16:31 · Speaker 4

from distribution.

### 00:16:40 · Speaker 4

and g theta of g

### 00:16:44 · Speaker 4

Be a function

### 00:16:49 · Speaker 4

a function

### 00:16:51 · Speaker 4

that would

### 00:16:56 · Speaker 4

map G okay to some other space X cap

### 00:17:11 · Speaker 4

Okay. Now, this result says that

### 00:17:21 · Speaker 4

Zee Kak

### 00:17:23 · Speaker 4

is

### 00:17:26 · Speaker 4

another random variable

### 00:17:32 · Speaker 4

with a distribution

### 00:17:40 · Speaker 4

the distribution

### 00:17:43 · Speaker 4

governed by

### 00:17:47 · Speaker 4

The function G theta

### 00:17:57 · Speaker 4

Does it make sense?

### 00:17:58 · Speaker 8

Do you understand what I'm saying? Suppose this is a standard result which you will be studying or have studied in random process that if you have a random variable, okay? And if you have a function that acts on a random variable, then the distribution of the output of that function, okay? First of all, the output of that function is another random variable and the distribution of that particular output or function depends upon the functional form of G. So what do I mean by that? examples.

### 00:18:30 · Speaker 8

If

### 00:18:32 · Speaker 8

G is let's say uniform random variable between zero and one, okay? And some G theta of X is equal to let's say

### 00:18:44 · Speaker 4

Z square, okay? Then Z square

### 00:19:22 · Speaker 4

When you see my screen,

### 00:19:27 · Speaker 3

Yes sir

### 00:19:37 · Speaker 3

सर, इफ यू आर राइटिंग समथिंग, देन आई डोंट थिंक वी आर एबल टू सी।

### 00:19:43 · Speaker 4

Oh, is it? I think it is stuck. Okay, let me just

### 00:20:02 · Speaker 4

Okay, I think yeah. Z square will not be uniform.

### 00:20:11 · Speaker 4

Do you see my writing now?

### 00:20:15 · Speaker 5

Yes

### 00:20:15 · Speaker 3

Yes sir

### 00:20:15 · Speaker 5

Yes sir

### 00:20:17 · Speaker 8

Okay, great. Yeah, this is what it is, right? I mean if you have, let's say, uniform random variable and you take the square root of it, it will not be uniform, it will have some other distribution than uniform distribution.

### 00:20:28 · Speaker 8

Do you all get this idea? So basically what I'm saying is that you take a random variable that has a particular distribution, okay? And then

### 00:20:38 · Speaker 8

If you pass that through a deterministic function, the output random variable will have a different distribution compared to the input random variable. Is this idea clear?

### 00:20:51 · Speaker 8

And the distribution of the output random variable depends on what sort of function you are passing the input random variable through.

### 00:21:00 · Speaker 8

Is this is this clear?

### 00:21:06 · Speaker 8

Okay. Now why is this important? Let us look at this. The way we are modeling V theta is via this function V theta of Z, okay? Now, uh this G theta of Z, okay?

### 00:21:21 · Speaker 3

Let us let me write that again.

### 00:21:26 · Speaker 3

G theta of G in our case

### 00:21:32 · Speaker 3

3 theta of G

### 00:21:35 · Speaker 4

இது நியூரல் நெட்வொர்க்

### 00:21:43 · Speaker 4

Okay, just for the sake of completeness, I will define what

### 00:21:47 · Speaker 8

a neural network is. Now,

### 00:21:51 · Speaker 8

Let's say that Z is in some R K dimensional space and we are talking of vector valued random variables here, okay? So what happens is that in in this case, right? I mean Z is a vector valued random variable with Gaussian distribution. If Z is in R K, then G theta of Z is defined like this. So what you first do is that you take

### 00:22:18 · Speaker 8

some weight vector W one, okay? And multiply that with Z. So what will you get? I will write the dimensions also.

### 00:22:28 · Speaker 8

Okay, let's say that W one

### 00:22:31 · Speaker 8

is a matrix which is in

### 00:22:35 · Speaker 8

So Z is in R

### 00:22:36 · Speaker 3

okay right? uh so this is

### 00:22:47 · Speaker 3

L one cross K. So you have a matrix of L one cross K.

### 00:22:51 · Speaker 8

now when you multiply

### 00:22:55 · Speaker 8

W one with G, what will you get? You will get a

### 00:23:01 · Speaker 3

or L one dimensional vector. Can all of you see that?

### 00:23:11 · Speaker 3

because Z is actually in K cross one

### 00:23:16 · Speaker 8

Right? It's a column vector of K dimensions, which means that you have one, two

### 00:23:27 · Speaker 8

k rows and one column. And W one has L one rows and k columns. When you multiply that you will get a L one cross one dimensional vector. Can all of you see this? Is it okay?

### 00:23:44 · Speaker 3

Okay. So then what you do is this is a linear transformation then you

### 00:23:49 · Speaker 3

through an element wise

### 00:23:50 · Speaker 8

non-linearity where what happens is that when you do this W one transpose Z so what is happening is every element of this W one transpose Z so this of a vector Z is simply you take the elements of Z so Z is actually one by one plus

### 00:24:17 · Speaker 4

E powers, let me make it a scalar.

### 00:24:26 · Speaker 4

this is the definition of the sigmoid

### 00:24:37 · Speaker 3

Okay? So now what you do is that

### 00:24:40 · Speaker 8

that when you write sigma of W one Z, W one Z is an L one dimensional vector, you take every element of it and do this operation one by one plus E power minus E, then you still get an L one dimensional vector that is what I call by sigma W one.

### 00:24:54 · Speaker 3

is that okay?

### 00:25:02 · Speaker 3

Okay. So then what happens is that you take another

### 00:25:07 · Speaker 8

tough

### 00:25:08 · Speaker 8

parameters, call them W two and multiply sigma W one Z with that W two.

### 00:25:15 · Speaker 3

this W two

### 00:25:20 · Speaker 3

ease of dimensions

### 00:25:25 · Speaker 3

L2 cross L1. Okay?

### 00:25:27 · Speaker 8

it implies that w two times sigma of w one z, okay, will lie in r

### 00:25:39 · Speaker 4

two cross one dimension. Is it okay?

### 00:25:52 · Speaker 4

Okay, so then what you do is

### 00:25:59 · Speaker 4

little further. Okay. Then you have another non-linearity here.

### 00:26:10 · Speaker 4

Okay, then you take another W three here

### 00:26:14 · Speaker 8

and W three is

### 00:26:17 · Speaker 8

This is L three cross L one and you can have another nonlinearity.

### 00:26:24 · Speaker 8

will have W four and so on. So what is this? This function is actually a four layer neural network.

### 00:26:36 · Speaker 8

Is this okay? So this is what a deep neural network is. I have just written that in a vectorized form that uh there are functions, right? I mean there are uh linear transformations which are of type W one Z, okay? And then there is a non-linearity given by a sigma. So there is a linear transformation followed by a non-linear

### 00:26:56 · Speaker 3

that is what a deep neural network is

### 00:27:04 · Speaker 3

I hope this is clear to all of you.

### 00:27:07 · Speaker 3

I see some questions here.

### 00:27:10 · Speaker 8

Yeah, Raghavendra

### 00:27:12 · Speaker 10

Yes sir, I mean you have just mentioned W four, so there is no sigma applied to W four or?

### 00:27:17 · Speaker 8

you can I mean that depends no I mean final layer is lineast in the case in the network that I have written you can put a head one here

### 00:27:29 · Speaker 10

Okay, thanks.

### 00:27:30 · Speaker 8

Yeah. I mean that depends, that's a design choice. Now, now if this is G theta, what is theta? Theta is all the set of parameters, you know, W one, W two, W three and W four. This is what I'm calling from, calling by G theta.

### 00:27:52 · Speaker 8

Is it all right?

### 00:27:54 · Speaker 8

Okay, so I'm going to try this again. So now training a neural network will be finding out these W one, W two, W three, W four through solving an optimization problem. And what problem do we solve in the case of generative models are the is this is something that we will see now. And how do we solve it is through error back propagation.

### 00:28:13 · Speaker 8

Okay, maybe I'll just mention it quickly when we formulate the optimization problem, but anyway, so now do you understand this? So now when I write this diagram,

### 00:28:24 · Speaker 8

that

### 00:28:26 · Speaker 8

There is a neural network that takes Z which has a Gaussian distribution. Okay, and there is this function G theta of of Z and you are getting an X cap.

### 00:28:38 · Speaker 8

Okay. Typically Z is in some R K dimensional space and X cap is in R D dimensional space which is same as the dimensionality of your X because we are trying to model

### 00:28:55 · Speaker 8

distribution of P X here. Typically what happens is the dimensionality D will be much higher than that of K which means that you will have to adjust this L one, L two, L three, L four. Okay? Such that the final output layer will have dimensionality that is much higher than the input dimensionality and note that it need not be a four layer neural network for instance right if you take research X F T

### 00:29:25 · Speaker 8

these fifty W's, okay, fifty layers. It's a deep neural network. I've just given you an example of a four layer neural network. It can be any layer. And these non-linearities need not be of this form. uh It can be of this form also, right? I mean, which is...

### 00:29:42 · Speaker 8

one if

### 00:29:44 · Speaker 3

is greater than zero or zero otherwise this is called the relu activation

### 00:29:54 · Speaker 3

and this is called the

### 00:29:56 · Speaker 3

sigmoid and so on, right?

### 00:29:58 · Speaker 8

doesn't matter but in general it is a deep neural network I mean for as far as our course is concerned we don't care what the form of these things are they are hyperparameters and design choices okay so now what we are interested in is that you start with a random variable which has a Gaussian distribution in k dimensions there is a deterministic function d theta which is a neural network that would that would transform it to another dimensional space called that x theta x cap and this has the constitution v theta. This is our setting.

### 00:30:34 · Speaker 8

Okay, we'll take questions here. Abhirup?

### 00:30:40 · Speaker 11

Yeah, so the in theta is just you are considering theta as the set of parameters. So in that set of parameters, since Z itself is a random variable following normal distribution, so those parameters, the mu and sigma, they will not be considered in theta.

### 00:30:55 · Speaker 8

No no no, it's fixed no? Z is from normal zero I, zero one. So that is fixed.

### 00:31:00 · Speaker 11

Okay, Okay, Okay.

### 00:31:02 · Speaker 8

Z is Z does not have any parameter, no, it's the input random variable.

### 00:31:08 · Speaker 8

typically what happens no we assume that we know how to sample from G we can we know right because if you have I mean there are these functions called random and random number generators in all these uh like programming languages right what do they do they actually sample from a Gaussian distribution correct. So we assume that we know how to sample from a Gaussian distribution and therefore we can generate this G as much as we want.

### 00:31:36 · Speaker 8

and that has no parameters. What is parameterized is this function g theta of g, okay? That this z is passed through to get a get an x cap, okay? which has a distribution p theta.

### 00:31:51 · Speaker 3

is this

### 00:31:51 · Speaker 8

This is okay? Yeah. Okay. Yeah. Sachin.

### 00:31:52 · Speaker 3

Yeah, okay.

### 00:31:57 · Speaker 10

Yeah, hi sir. So, uh, this is the Gaussian distribution of this random variable Z.

### 00:32:03 · Speaker 8

random variable z has a Gaussian distribution

### 00:32:07 · Speaker 10

Okay

### 00:32:08 · Speaker 3

And sir in this W3 can you scroll up a little bit?

### 00:32:12 · Speaker 4

Okay

### 00:32:34 · Speaker 4

in this

### 00:32:35 · Speaker 8

W3 will be a this matrix of L3 cross L2, right?

### 00:32:40 · Speaker 3

Yes

### 00:32:41 · Speaker 8

Yeah, yeah.

### 00:32:42 · Speaker 3

Thank you

### 00:32:42 · Speaker 8

Thanks

### 00:32:45 · Speaker 3

Vivek

### 00:32:47 · Speaker 10

Sir, this Z, the Z, did it, is it actually representative of the data or was some transformation done to it?

### 00:32:55 · Speaker 8

transformation done to. No no no no no no no. So Z is just an input random variable, okay, it can be anything. You take it to be normal distribution, normally distributed.

### 00:33:07 · Speaker 10

Okay, okay.

### 00:33:07 · Speaker 8

Okay, okay. Because you take it to be normally distributed. It has nothing to do with data.

### 00:33:13 · Speaker 10

Okay, something was done to bring the data into Z form. I mean like... No, nothing. It has nothing to do with data.

### 00:33:17 · Speaker 8

nothing it has nothing to do with data. it has zero connection with data.

### 00:33:23 · Speaker 10

Okay, okay, okay, right.

### 00:33:24 · Speaker 8

it has nothing to do with data, okay?

### 00:33:27 · Speaker 10

Okay

### 00:33:28 · Speaker 8

So it is just that we are okay so I'll tell you like maybe the high level story or maybe it's just a mistake. See basically what we are trying to do is we are trying to transform okay an arbitrary random variable to some random variable that has same distribution as our input data.

### 00:33:51 · Speaker 8

Is that okay?

### 00:33:52 · Speaker 10

Right, Yes Sir.

### 00:33:53 · Speaker 8

Now, the Z is an arbitrary random variable and we know that if you pass an arbitrary random variable through a function, the output random variable will have a different distance.

### 00:33:54 · Speaker 10

Yeah

### 00:34:06 · Speaker 8

Now the goal is to choose these parameters theta such that the transformation that this arbitrary random variable goes through will be such that the output and output random variable that you get will have the same distribution as that of input data.

### 00:34:24 · Speaker 7

ओके

### 00:34:26 · Speaker 8

So now the goal is to set this G theta, set the parameters of the neural network such that distribution P theta matches with P X. It means that I want the distribution of X cap to be same as the distribution of X which is my input data. Z has nothing to do with the the data. It is just an input seed. It is it is seed.

### 00:34:50 · Speaker 10

ओके ओके ओके ओके

### 00:34:51 · Speaker 8

It is the random C that you start with, you pass it through a neural network, okay? And output of the neural network will have some distribution. I want the distribution of that output to match to the input the distribution of given data.

### 00:34:54 · Speaker 10

pass it through

### 00:35:08 · Speaker 8

Okay

### 00:35:08 · Speaker 10

Yes, in that case, uh, the, I mean, the creation or the finding out of the distribution of Z is also as equally important as G theta of Z, right?

### 00:35:21 · Speaker 8

No, no, because

### 00:35:23 · Speaker 10

और इट इज

### 00:35:25 · Speaker 8

Yeah, it is just a random seed, you know, you can start with any distribution. Anything. Yeah.

### 00:35:27 · Speaker 10

Okay, anything.

### 00:35:29 · Speaker 10

Okay

### 00:35:29 · Speaker 8

Hmm

### 00:35:30 · Speaker 10

Nothing was done there so we are just picking something random seeds.

### 00:35:34 · Speaker 8

It is random seed. It is nothing but random seed.

### 00:35:38 · Speaker 10

ओके, ओके, थैंक्स।

### 00:35:39 · Speaker 8

to transform this normal distribution into distribution of interest via new methods.

### 00:35:45 · Speaker 10

ओके ओके ओके यस थैंक यू

### 00:35:48 · Speaker 8

ஆஸ்திக்

### 00:35:49 · Speaker 10

Hello

### 00:35:51 · Speaker 9

Yeah, hi sir. So, uh in the last line we discussed that the D should be greater than this K, but in a general neural network generally like the model, you know, the number of parameters increases, but in the last output that we are interested in, it is similar to that of input, right? So, uh this

### 00:36:00 · Speaker 0

energy

### 00:36:13 · Speaker 8

So it is not in no no in a classifier what happens is the data will have a larger dimension right you give images and you reduce the dimensionality and the final layer will be equal to the number of classes.

### 00:36:22 · Speaker 9

uh

### 00:36:27 · Speaker 9

Yeah

### 00:36:27 · Speaker 8

Yeah

### 00:36:28 · Speaker 9

Yeah

### 00:36:29 · Speaker 8

Right? But in generative models it is the other way around because the dimensionality of X cap here, the output should be equal to the dimensionality of the input image because the final goal is to sample, isn't it?

### 00:36:42 · Speaker 8

So if you want to sample pictures of dimensionality two hundred by two hundred pixels, then the output of this neural network has to be of dimensions two hundred cross two hundred.

### 00:36:42 · Speaker 9

Okay

### 00:36:53 · Speaker 9

Okay

### 00:36:55 · Speaker 9

ओके, एंड व्हाट वुड बी द इनपुट डायमेंशन इन दिस केस इफ द इमेज साइज इज टू हंड्रेड प्लस टू हंड्रेड?

### 00:36:56 · Speaker 8

the

### 00:37:02 · Speaker 8

Typically it is it will be of size let's say sixteen, thirty two and so on. So that's why if you look at the shape of the neural network that I have written, it will have increasing dimensionality as you move deeper on to the network.

### 00:37:16 · Speaker 9

So how the input is like lower dimension in this example?

### 00:37:21 · Speaker 8

exam

### 00:37:21 · Speaker 10

to

### 00:37:23 · Speaker 8

See, input is of sixteen dimensions and you keep increasing. So, see, it is all in setting up this L one, L two, etcetera, right? You choose those are the hyper parameters that are in your control as a designer.

### 00:37:34 · Speaker 9

Yeah, that is fine, but like our output should be a image and input is also a image, right? So

### 00:37:41 · Speaker 8

No no no no it is not an image it is a random seed that is what I am trying to say input is not an image

### 00:37:46 · Speaker 9

Okay

### 00:37:48 · Speaker 8

So this is a generative model.

### 00:37:48 · Speaker 9

This is a generative

### 00:37:50 · Speaker 9

Okay, okay, okay, yeah, yeah, yeah.

### 00:37:52 · Speaker 8

You understood the setup. It is see it is not you are giving an image and you are asking for a class. You are inputting a random seed and you are expecting the neural network to give you an image from the data destination.

### 00:37:57 · Speaker 9

input

### 00:38:04 · Speaker 9

Yeah yeah yeah it's a generative scenario okay okay yeah

### 00:38:09 · Speaker 8

the course is deep generative modeling.

### 00:38:12 · Speaker 9

Yeah, yeah, yeah.

### 00:38:13 · Speaker 8

Just joking. You understood, no?

### 00:38:14 · Speaker 9

you understood

### 00:38:15 · Speaker 9

Yeah, yeah, yeah, I understand.

### 00:38:17 · Speaker 8

That's why the shape, look at the shape, right? The shape of the neural network that I have drawn is that you start from a lower dimension and go to a higher dimension.

### 00:38:21 · Speaker 9

from a

### 00:38:25 · Speaker 9

As you would consider

### 00:38:25 · Speaker 8

as you move through the network. Got it?

### 00:38:28 · Speaker 9

Yeah, yeah, thank you.

### 00:38:30 · Speaker 8

Hmm

### 00:38:33 · Speaker 8

या सुशील

### 00:38:35 · Speaker 1

Sir, I understand we are not using the input, but somewhere we will have to relate with the input distribution, like, otherwise how we will calculate the loss and all.

### 00:38:47 · Speaker 8

come again

### 00:38:49 · Speaker 1

Like I understand we are not using the actual input here. But what I'm saying is how we will relate with the actual input distribution to calculate the loss.

### 00:38:57 · Speaker 8

constitution

### 00:38:58 · Speaker 8

I'm not saying that we are not, I'm not saying that we are not using the input. I'm saying that the input distribution does not matter because you can start with any random seed and then convert that into distribution of interest using neural networks.

### 00:39:13 · Speaker 1

ओके सर, सो वेयर वी यूज़ द इनपुट हियर?

### 00:39:17 · Speaker 8

Okay. See, how do you get x cap here?

### 00:39:22 · Speaker 8

X cap is is is gotten by taking a sample from Z, okay? And passing through. So basically what you do in practice, I've written this, no, Z is sampled via random number generator. Which means that you run rand N once, okay, you get one number. You that is your Z. You pass that Z through this neural network Z theta, you get an X cap. That is how you use the input.

### 00:39:48 · Speaker 1

सर, आई वॉज़ टॉकिंग अबाउट एक्चुअल इनपुट एक्स वन एक्स टू फ्रॉम द डेटा सेट।

### 00:39:52 · Speaker 8

Oh you mean okay so please don't call it as input you know it's a little confusing. input to this setup is Z okay. And the data okay is X one through X N. We are I mean everything that we do is using data we will see that right we have not still told you how to set the parameters of G theta right. The parameters of G theta is set by using the data.

### 00:40:10 · Speaker 1

Okay

### 00:40:18 · Speaker 1

ओके सर

### 00:40:20 · Speaker 8

I thought I mean yeah I think you know there is a confusion. Z is what is an input to this setup. Okay and let us let us call the let's call X one X two X three as input sorry data.

### 00:40:35 · Speaker 8

Okay? And this has the random seed.

### 00:40:39 · Speaker 8

We will use I mean I okay let me I mean for everyone's sake you know what I'm saying. When I say that the input distribution does not matter. I'm referring to this random seed not to the data distribution. I mean everything depends on data distribution because we are interested in modeling the data distribution. When I say input input to this setup which is the random seed it does not matter if you sample from a normal distribution or you sample from a uniform distribution. Is that okay? Is this clear to all of you?

### 00:41:13 · Speaker 8

I mean that's a huge confusion if you had that confusion. Is this clear?

### 00:41:17 · Speaker 8

Hello

### 00:41:19 · Speaker 7

Yes sir

### 00:41:20 · Speaker 4

Yes

### 00:41:22 · Speaker 8

Okay, yeah, I think there's one more question. Sanchit?

### 00:41:27 · Speaker 7

Sir, uh I understand that we are just taking a random uh sample Z from the normal distribution and passing it through the neural network, we are getting X hat, okay? But now uh when we want to evaluate like we want to compare this X hat, what are we taking it? What are we comparing it against? Like we are saying I have not told you that yet.

### 00:41:40 · Speaker 8

But

### 00:41:48 · Speaker 8

Pindike

### 00:41:52 · Speaker 8

I have not told you that yet. I have not told you that yet. I'm just saying X hat has a distribution. Let's call it P theta. That is what I've told you so far. I have not told you how to make this P theta close to P X. Anyway, because you're asking, I'm telling you. So, evaluate the divergence between P theta and P X and try set the parameters of this G theta such that that divergence is minimized.

### 00:41:57 · Speaker 7

Please

### 00:42:01 · Speaker 7

Oliyo

### 00:42:15 · Speaker 7

Sir, I understand that flow like you had explained it in the last class. What I'm trying to relate to is like let's say for like supervised learning when we have the training data set, we pass, let's say we are going for Hold on.

### 00:42:20 · Speaker 8

drawing

### 00:42:27 · Speaker 8

plus

### 00:42:31 · Speaker 8

Hold on, hold on, hold on, hold on. You are asking me how to do it practically, right? How do you basically what you are saying is, how do you minimize the divergence practically, right?

### 00:42:41 · Speaker 7

Yes sir

### 00:42:41 · Speaker 8

I have not answered that question. Hold on. That is I will answer it in this class.

### 00:42:46 · Speaker 7

ओके सर, श्योर, थैंक यू।

### 00:42:47 · Speaker 8

Okay. Yeah. Harish.

### 00:42:51 · Speaker 2

Hello sir. Sir, the sampling of the data, the normal distribution one, so do we why do we consider it for a normal distribution or can we consider with any other distribution? So, for the for this idea.

### 00:43:03 · Speaker 8

you can. Yes, you can, but generally normal distribution is chosen because normal distribution has infinite support, no? Which means that, uh, like it has, uh, I mean, for the entire space R D, uh, the density function is not zero. If you take uniform distribution for example, right? Uh, the density function vanishes out of, I mean, outside of a window. But in normal distribution, the density function is existing, I mean, it's non-zero over the entire space, no? That's why you normal distribution

### 00:43:35 · Speaker 2

I understand. And one more question on the dimension of K here. So, the the dimension K here, the dimension of K. Typically

### 00:43:37 · Speaker 10

um

### 00:43:43 · Speaker 10

Sari

### 00:43:44 · Speaker 8

Typically it is taken to be sixteen thirty two if I mean if you are working with images.

### 00:43:50 · Speaker 2

Okay. So does it matter so you have mentioned that the D is much much greater than K here right? So does it matter based on the data size so we need we choose sixteen or thirty two or is it also a random number?

### 00:43:56 · Speaker 3

correct

### 00:43:56 · Speaker 0

Does it matter?

### 00:44:00 · Speaker 0

16 or 30

### 00:44:03 · Speaker 8

Yeah, that's a good question. It's a hyperparameter, but like, it means some of our research we have, we have actually found out that the dimensionality matters.

### 00:44:14 · Speaker 8

Right? uh There is an optimal dimensionality is what we show in some of our papers. But yeah, uh like in general it's a hyperparameter.

### 00:44:22 · Speaker 2

Okay. So we we choose that once like for example we take an initial F sixteen or thirty two and then based on the training and how it works so do we change that based on the

### 00:44:32 · Speaker 8

typically that is not a happy parameter that people tune on. That is kept fixed.

### 00:44:41 · Speaker 8

Okay. Yeah. Yeah. Nirmal.

### 00:44:46 · Speaker 5

Uh sir the real application of this function I want to understand my assumption is correct or not. If we give some few text like a cup on table then it will give me a picture of the cup on table.

### 00:44:57 · Speaker 8

hold on. No no no. See for now I have not told you the conditional part of it. What you are saying is a conditional generative model. We'll come to that in a while. It is not it is not conditional generative modeling right now. Right now what happens is after you train it you give a random number as an input to this okay. It will give you a picture from the distribution.

### 00:45:22 · Speaker 8

Now that you are asking, let me just show you that as well.

### 00:45:30 · Speaker 8

You see my screen no there is this website called this person does not exist dot com okay.

### 00:45:37 · Speaker 4

Yeah

### 00:45:38 · Speaker 8

So what is happening is every time I refresh this page

### 00:45:43 · Speaker 8

I get a new picture you see

### 00:45:46 · Speaker 5

Yes

### 00:45:47 · Speaker 8

see my screen no. See these are pictures of like non existent people. So what is happening when I refresh the screen is that a random number is being generated which is your Z and that is getting passed through this network G theta and you are getting a picture. Here there is no conditional generation. I'm not giving a text as an input. I'm just giving a

### 00:46:08 · Speaker 3

Random Number Asini

### 00:46:18 · Speaker 3

Right now

### 00:46:19 · Speaker 8

I'm not looking at conditional generation. I'm simply looking at this is called unconditional generation where you generate images from the underlying distribution or generate data from the underlying distribution without conditioning.

### 00:46:32 · Speaker 5

Got it

### 00:46:35 · Speaker 8

I will also talk of conditional generation but you are you are skipping a lot. We will do that one step at a time. We will understand the unconditional part and then adding conditioning is a trivial extension to this, okay?

### 00:46:48 · Speaker 5

Yeah. So, I know sir you have not explained this, but in the terms of picture, we got a P theta, but then how to measure like between P theta and P X?

### 00:47:01 · Speaker 8

X. I told you that I will do this in this class. Please don't repeat the question that I have answered already.

### 00:47:08 · Speaker 5

Yes yes

### 00:47:09 · Speaker 8

that is the next thing that we will do, no? See, okay, so let me tell you my philosophy of teaching. When I teach, I just, I mean, like open it layer by layer. So now what is happening is I'm trying to give you an abstraction of what is happening. We will go to the details. So now at the level of abstraction, what you need to understand is that the idea is that you start with an arbitrary random variable Z, pass it through a function G theta, and you get another random variable which has a distribution P theta.

### 00:47:39 · Speaker 8

Now the next thing is you tweak the parameters of this G θ such that the distribution of the output of this network X cap, okay, is same as the distribution of P X. Now how do we do that is a question that I will answer in a while. But now you ask me questions at this level of abstraction.

### 00:48:00 · Speaker 8

Right if you have I mean difficulty in understanding this level of abstraction sure ask me questions. But you know things that that I promised that I'm going to do in the due course right if you ask me that. Anyway I mean I don't mind but yeah so just a request. Okay. Anyway Mukesh.

### 00:48:19 · Speaker 0

Yeah, hello sir. Sir, my question is regarding this dimensionality. Sir, in the CNN architecture, actually what we do, we try to implement this pooling layer where we try to reduce the dimensions of the data. But here, we just passing the seed to increase the dimensionality, is that correct?

### 00:48:20 · Speaker 8

question

### 00:48:32 · Speaker 8

pages

### 00:48:36 · Speaker 8

Yeah, yeah, yeah. So the neural network here will increase have increase in dimensionality.

### 00:48:37 · Speaker 0

Sony

### 00:48:42 · Speaker 0

So actually here we don't have input data as a image that's why we are trying to increase the dimensionality.

### 00:48:47 · Speaker 8

I would not say that. See, we want to start with some noise or some random arbitrary from from an arbitrary random variable and generate images. So which means that we start with a lower dimensionality and we need to increase the dimensionality.

### 00:49:06 · Speaker 3

Okay

### 00:49:06 · Speaker 8

Okay? So now in terms suppose see I have not told you that see this is not a CNN that I have written what I have written here is a fully connected neural network.

### 00:49:16 · Speaker 8

ओके, विच इज अ सीड फॉरवर्ड न्यू नेटवर्क ऑर अ मल्टीलेयर फॉरसेट पार्ट। इफ यू वांट दिस टू बी इम्प्लीमेंटेड अस अ सी एन एन, ओके, दैट आल्सो हैस टू बी डन इन

### 00:49:24 · Speaker 3

the T S S S

### 00:49:30 · Speaker 3

So you have to teach about upsampling layers.

### 00:49:34 · Speaker 3

So there are this neural network I mean neural network layers called upsampling or also called transposed convolution layers.

### 00:49:47 · Speaker 8

Okay? That will take as an input a lower dimensional uh feature and give you a higher dimensional uh feature vector as output. Just like you have convolution layers, there are transpose convolution layers that would increase the dimensionality of neural networks. Okay?

### 00:50:04 · Speaker 0

ओके सर, ओके, थैंक यू.

### 00:50:05 · Speaker 8

But but don't worry about architecture for now. I mean for us G theta is simply a function. I mean it need not be a neural network also but now because in in practice we are only looking at neural networks. I've said that it's a neural network. So for now let us assume that these are all fully connected neural networks which are I mean no fancy network architecture here right? I mean they are all multi layer perceptrons or simply fully connected neural networks. Is that okay for now?

### 00:50:34 · Speaker 0

Yeah yeah sir correct correct

### 00:50:36 · Speaker 8

Hmm

### 00:50:37 · Speaker 0

Thank you

### 00:50:37 · Speaker 8

Okay

### 00:50:38 · Speaker 3

Any other question? Is the problem setting clear to all of you?

### 00:50:48 · Speaker 3

Okay

### 00:50:51 · Speaker 3

I think they expect

### 00:50:52 · Speaker 8

so many questions at this stage. Anyway, no problem. It's good that you are asking questions. Okay, let's move on. So now, what is the objective? So now the objective

### 00:51:05 · Speaker 3

objective is to make

### 00:51:10 · Speaker 4

P theta

### 00:51:13 · Speaker 4

as close okay

### 00:51:17 · Speaker 4

made P theta

### 00:51:22 · Speaker 8

close to P X. Correct? Now if we do this, what happens is, suppose you are given data from let's say human face distribution. If we can have this setup and make my P theta close to P X, then I have solved the problem of generative modeling. Do you agree?

### 00:51:41 · Speaker 8

Every time I start with a random C and pass it through G theta, I will get a I will get a picture from like human faces because the distribution of the output of this neural network is now close to P X. Clear? Is this clear?

### 00:51:59 · Speaker 3

Okay, now what do we have to do is is that the question is that question

### 00:52:07 · Speaker 3

How to

### 00:52:10 · Speaker 4

set the parameters

### 00:52:17 · Speaker 4

parameters of G theta

### 00:52:22 · Speaker 4

such that

### 00:52:28 · Speaker 4

such that P theta is close to P

### 00:52:31 · Speaker 3

3x

### 00:52:36 · Speaker 8

is the central question.

### 00:52:38 · Speaker 8

Do you agree? So now only thing that we have in our control is uh G theta which are the parameters of neural network. The question is how do we set the parameters of neural network such that P theta is close to P X. We note that

### 00:52:54 · Speaker 8

If you fix a value

### 00:52:58 · Speaker 8

Excuse me. So if you fix a value for the parameters g theta, parameters of this neural network,

### 00:53:07 · Speaker 8

you will get some distribution on on on on some distribution on the output. Now if you take another set of parameters you will get another distribution. Now the question that is to be asked is which set of parameters of this neural network will ensure that P theta is close to P X.

### 00:53:26 · Speaker 8

Okay

### 00:53:28 · Speaker 8

Now, to do that is, you know, the the solution for this is that simply set the parameters of your movements such that

### 00:53:38 · Speaker 8

it minimize search over all possible sets of theta such that some divergence between px and p theta is minimized.

### 00:53:48 · Speaker 8

And this divergence norm is a function of theta, right? Because if you choose a theta, you will have one set of divergence. So now what you have to do is that, so this means, write that down in English, that

### 00:54:00 · Speaker 8

set the

### 00:54:03 · Speaker 3

the parameters

### 00:54:07 · Speaker 3

of the

### 00:54:08 · Speaker 4

Neural Network

### 00:54:11 · Speaker 4

such that

### 00:54:17 · Speaker 4

the divergence

### 00:54:22 · Speaker 3

between P X and P theta is minimized.

### 00:54:28 · Speaker 8

That's the meaning of Argmin, okay?

### 00:54:31 · Speaker 8

choose a p choose a theta that would minimize the divergence between p x and p theta. Is this clear? Now the next question that comes up is whatever you have been asked.

### 00:54:43 · Speaker 3

asking question.

### 00:54:45 · Speaker 3

Yes

### 00:54:47 · Speaker 3

Given

### 00:54:50 · Speaker 3

Data

### 00:54:53 · Speaker 3

डी ओके। व्हाट इज डेटा रिमेंबर दैट दे आर सैंपल्स फ्रॉम पीएक्स।

### 00:55:03 · Speaker 3

and

### 00:55:06 · Speaker 3

samples from P theta

### 00:55:13 · Speaker 3

samples from P theta. How do we have samples from P theta? They are simply the output of neural networks.

### 00:55:23 · Speaker 3

output of neural network g theta

### 00:55:24 · Speaker 3

the output of neural network

### 00:55:26 · Speaker 3

is nothing but samples from

### 00:55:31 · Speaker 3

P theta, right?

### 00:55:35 · Speaker 3

given data which are samples of P X and samples from P theta how to compute and minimize

### 00:55:46 · Speaker 8

to compute the divergence. This is the next question. You understand this right? So now let me just tell you again. So in the setup remember the setup. The setup is the following that we have a neural network.

### 00:55:59 · Speaker 8

g theta of g, okay? And g is a random seed from normal distribution and we have samples from x cap, right? And this has a distribution p theta. We also have data that are some samples given some images given from px, okay? You should note that both px and p theta are

### 00:56:22 · Speaker 3

Anno

### 00:56:27 · Speaker 3

is two are unknown but but

### 00:56:31 · Speaker 3

samples from

### 00:56:35 · Speaker 3

from P X and P theta are available.

### 00:56:42 · Speaker 3

Okay

### 00:56:43 · Speaker 8

So you understand this, no? This is actually the most important thing because this is the one that governs the entire like space of generative models that you don't know the underlying distributions but you have samples from those distributions. Samples from P X, the true data distribution is known because that is the data that we have. Okay? Samples from P theta are also known because we can generate as

### 00:57:13 · Speaker 8

many samples from P theta as we want. Because what do you mean by generating a samples from P theta? Let me just say, samples from

### 00:57:23 · Speaker 8

samples from pH is simply the data

### 00:57:28 · Speaker 3

Given data

### 00:57:31 · Speaker 3

Right? Given data D. Now samples

### 00:57:37 · Speaker 3

from

### 00:57:37 · Speaker 4

P theta, How do you get that?

### 00:57:45 · Speaker 3

sampling shoes

### 00:57:47 · Speaker 5

using different Z

### 00:57:48 · Speaker 4

correct

### 00:57:50 · Speaker 3

Other

### 00:57:52 · Speaker 3

different z's

### 00:57:54 · Speaker 3

and

### 00:57:56 · Speaker 3

pass them through

### 00:58:02 · Speaker 3

V theta of z

### 00:58:04 · Speaker 8

You understand? So now we have samples from P X, samples from P theta. Now the question is given samples from these two distributions P theta and P X, how do we compute the divergence metric? And of course, why do we have to compute the divergence metric? Because only when we compute the divergence metric, we can minimize it, right? When we can use gradient descent or differentiate it and then optimize for it. First, we need to compute the divergence metric between P X and P theta. Given that we don't have access to P X and P theta, but we only have access to

### 00:58:34 · Speaker 8

samples. Now, seventy percent of the scores will be taking answering this question in different ways that given that we have samples from the true distribution and the generated data distribution, how do we compute a divergence metric between those two?

### 00:58:53 · Speaker 8

Okay? So please try to appreciate and understand the problem. We have have the distribution. Sorry, sorry, sorry, sorry. We don't have the distribution, we have the samples from it. So the entire statistics, right, and the machine learning and the other statistical fields, they ask this central question. The central question that is asked is that if you do not have distributions, but you have samples from it, how do you compute something? So in this case, we need to compute divergence.

### 00:59:23 · Speaker 8

matrix, right? In some other case, you know, you might need to compute the moments, you might need to compute some integrals, etcetera, depending upon what the application is. But one of the central questions in statistics or probabilistic machine learning is that if you are given samples from distributions without giving the actual distributions, how do you compute, uh some things involved in the distribution? That is the central question. Now, in our case, what we should do, please don't forget the storyline. Storyline is that we are interested in

### 00:59:53 · Speaker 8

generating samples from P X. Now to generate samples from P X what we have done is that we have taken

### 01:00:00 · Speaker 7

an arbitrary random variable and we have a function g theta. Now we know that passing an arbitrary random variable through a deterministic function will change the distribution of that function. Now we need to set this function g theta such that the output of this function g theta will be a random variable that has the exact same distribution as that of the input data. Now how do we do that? By minimizing the divergence metric. Okay? To minimize the divergence metric

### 01:00:30 · Speaker 7

trick we need to first compute the divergence metric. Now the question now is that how do you compute a divergence metric between two distributions which are

### 01:00:38 · Speaker 6

unknown

### 01:00:39 · Speaker 7

given that we have samples from them.

### 01:00:44 · Speaker 7

given data and samples from P theta how to compute the underlying divergence metric

### 01:00:50 · Speaker 7

Is this clear so far? Any questions here? Okay, I see some hands raised. Kartik?

### 01:00:58 · Speaker 2

Yes sir. uh So I have a query. So we said about uh when we have samples of R K, then we get the sigmo algebra using like L one, L two, all those parameters, right?

### 01:01:10 · Speaker 7

Hold on, hold on. I've never used the word sigma algebra here.

### 01:01:14 · Speaker 2

Sorry, Sigma

### 01:01:15 · Speaker 7

Sorry, Sigma

### 01:01:17 · Speaker 2

Yeah, sigma of what we wrote, right?

### 01:01:20 · Speaker 7

It is a neural network. You start with a K dimensional vector and you keep increasing the dimensionality till you go to D dimensional vector. Yeah.

### 01:01:20 · Speaker 2

June

### 01:01:25 · Speaker 2

Yeah

### 01:01:29 · Speaker 2

But so we don't have any control over whatever is written in R L one R L two other than our input right so these are fixed that's what we are saying right

### 01:01:37 · Speaker 7

No, right. Dimensionality are these are hyper parameters, no? L one, L two, L three are hyper parameters that you fix.

### 01:01:45 · Speaker 2

Okay

### 01:01:46 · Speaker 7

that you fix as a designer.

### 01:01:48 · Speaker 2

Hmm

### 01:01:50 · Speaker 7

So when you say, see, when people say that it's a billion parameter model, it is some, you know, seventy billion parameter model, what are they saying? They are referring to these L one, L two, L three. So that's a design choice.

### 01:02:02 · Speaker 2

Okay

### 01:02:03 · Speaker 7

even when you walk with

### 01:02:05 · Speaker 2

Yeah, sorry sir. What I wanted to know was what are the whatever is the value of omega one or like omega two. Those things are W one W two sorry. W one W two those things are not in our control right away right other than the

### 01:02:05 · Speaker 7

Sorry

### 01:02:13 · Speaker 7

those things

### 01:02:21 · Speaker 7

right other than the No no no okay okay have you tried a neural network before?

### 01:02:28 · Speaker 2

in pictorial forms only sir sorry. Okay.

### 01:02:31 · Speaker 7

Okay, see how do you drive a neural network? You start with some random initialization for the W one, W two, W three, W four, okay?

### 01:02:40 · Speaker 5

Hmm

### 01:02:41 · Speaker 7

and then solve this optimization problem. You know you start with some W one, W two, W three, W four and then you know you keep on changing these W one, W two all these parameters till you reach a point where your objective is optimized. That's why you try neural networks.

### 01:02:58 · Speaker 2

Yeah

### 01:03:00 · Speaker 2

सो नॉट जस्ट सेड वी विल बी ट्रायिंग विद वेरिएबल वेरियस वैल्यूज फ्रॉम डब्ल्यू वन डब्ल्यू टू आल्सो लाइक वी कैन चेंज

### 01:03:09 · Speaker 7

All we change are W one, W two, W three, W four only, no? That's the only thing that we would change, nothing else.

### 01:03:16 · Speaker 2

Okay, yeah

### 01:03:17 · Speaker 7

When we solve this optimization problem that we have we have written here. I mean what do you mean by optimizing over theta? Optimizing over theta actually means setting up these W's, no?

### 01:03:30 · Speaker 2

Hmm

### 01:03:33 · Speaker 2

Okay. So the final

### 01:03:34 · Speaker 7

optimizing over

### 01:03:36 · Speaker 2

The final changes will be in W one, W two, W three, W four. Whatever is the value.

### 01:03:40 · Speaker 7

exactly what of course right I mean when you optimize over theta you want theta star what is theta theta is collection of all W W one W three W three all the parameters of the neural network what you change are the see learning or training of a neural network is nothing but changing the parameters of it

### 01:03:46 · Speaker 2

Seed

### 01:03:58 · Speaker 6

Okay

### 01:03:58 · Speaker 7

That's why I'm asking you, right? Okay. uh Here is a small request. The next class, uh you please study about, you know, uh what do you mean by training neural network? I mean, I I assume that all of you know what training neural network is.

### 01:04:17 · Speaker 7

See, I told you that that the first four chapters of that Ian Goodfellow's Machine Learning

### 01:04:22 · Speaker 6

book, deep learning book is a prerequisite. Do people go through it?

### 01:04:33 · Speaker 6

Nirmitz, did you go through it? Did you go through training a neural network, error back propagation and so on?

### 01:04:40 · Speaker 1

just started like first two chapters are random process and linear algebra

### 01:04:46 · Speaker 7

ओके. ओके.

### 01:04:47 · Speaker 1

I'm going through it

### 01:04:49 · Speaker 7

Yeah. So, please, you know, quickly ramp up. See, now we have sort of come through the come to the meat of the course, okay? Like, I expect all of you to know what training neural networks mean. So, please go through those chapters and those are actually sort of very strict prerequisites. Otherwise, I can't teach how to like train a neural network in this course, you see.

### 01:04:59 · Speaker 6

I

### 01:05:17 · Speaker 7

So please have a look at that. Okay, Vivek.

### 01:05:20 · Speaker 2

Thank you sir

### 01:05:22 · Speaker 8

So so when we look at the KL divergence formula, so because we are practically finding out the KL divergence between two distributions.

### 01:05:26 · Speaker 7

your

### 01:05:30 · Speaker 7

by the way no no I mean like yeah KL divergence is one of the multiple possible divergences I will define now a family of divergence metrics. Okay. That will be minimized now. But anyway you go on okay KL divergence is one of them.

### 01:05:40 · Speaker 8

Okay

### 01:05:40 · Speaker 8

Okay

### 01:05:44 · Speaker 8

Yeah, my question was, so you can, can you really in that formula it is like there is a closed form form of two probability distributions. But in this setup that you have given

### 01:05:55 · Speaker 7

But in this setup that you have given

### 01:05:57 · Speaker 7

No, even in KL divergence, see what is KL divergence between PX and P theta? Let me write that down. KL between PX and P theta is given by integral of PX evaluated at X log of PX evaluated at X divided by P theta evaluated at X to integrate this out. This is the definition of KL divergence, right?

### 01:06:20 · Speaker 8

Right, yes sir.

### 01:06:21 · Speaker 7

Now, you don't know px, you don't know p theta.

### 01:06:25 · Speaker 8

Right, yeah.

### 01:06:26 · Speaker 7

How do we compute this? That is the whole question.

### 01:06:28 · Speaker 8

ओके ओके

### 01:06:30 · Speaker 7

whole question is that when we don't have underlying distribution density functions but we only have samples from it. how do we compute the divergence metric is the whole question.

### 01:06:38 · Speaker 8

Oh

### 01:06:41 · Speaker 8

Yes. Yes. And also, uh the another question is, uh so any such metric, uh how can we have parallels for a single point, for a single sample at a time? In the sense like, uh

### 01:06:57 · Speaker 7

no no no, none of the metrics, none of these metrics are doing, I mean like they are they are they are point wise.

### 01:07:05 · Speaker 8

Okay, they're like a group of examples, a group of pictures. We will see, no, I have. Okay, okay.

### 01:07:05 · Speaker 7

like a group of

### 01:07:08 · Speaker 7

we will see no I have okay okay okay. There are group of pictures. Okay. See how do you compute these divergences when you don't have distributions and only have samples is a question that I have not answered yet. I will answer it in a while. Okay. If you have questions on the setup ask me.

### 01:07:13 · Speaker 8

Okay

### 01:07:23 · Speaker 8

If you have

### 01:07:28 · Speaker 7

Okay, so these are things that I'll discuss in a while. So any questions on this setup?

### 01:07:31 · Speaker 8

any question

### 01:07:33 · Speaker 8

ओके, नो सर।

### 01:07:35 · Speaker 7

Okay. Abhirup?

### 01:07:37 · Speaker 0

Yes sir, I have a question on the last statement. So samples from P theta choose different Zs and pass them through G theta. Now Z is a random variable which you are passing through a neural network. So my question is why do we have to pass different Zs, random variable being a function, if we pass a different point belonging to the range space of a random...

### 01:07:46 · Speaker 8

Hello

### 01:07:48 · Speaker 8

Shivapak

### 01:08:00 · Speaker 7

Uh yes yes that is what we do when we say different Z that's exactly what we mean. The samples from the range space of the random variable and then pass. Always that. See whenever I say that they are points from random variable they always mean that it's from the range space of the random variable. Always.

### 01:08:15 · Speaker 0

Always. Okay, okay, okay. So you have written, I think you said it as

### 01:08:17 · Speaker 7

I think we settled this we settled this in the first class itself right I told you that I say that when I say that there are we have n samples from a random variable I said that they are always I always mean that they are n samples from the range space of the random variable with a distribution. I think that we have settled now.

### 01:08:31 · Speaker 0

Yeah, yeah, that is settled. I was I thought that since you've written choose different Zs, I thought you were choosing a different random variable altogether. Anyway, sorry, sorry.

### 01:08:39 · Speaker 7

Anyway, sorry, sorry, sorry.

### 01:08:42 · Speaker 7

Okay

### 01:08:42 · Speaker 0

Hello

### 01:08:47 · Speaker 7

Is it okay? Shall we move on?

### 01:08:50 · Speaker 0

Yes

### 01:08:51 · Speaker 7

Okay, so now the important question is, right, how do we compute this divergence metric, uh when we when we uh don't have uh distributions but only have samples from it, okay? Before we take that question, let us

### 01:09:09 · Speaker 7

By the way I'll tell you the answer is through this adversarial optimization. This entire generative adversarial network right or adversarial optimization.

### 01:09:19 · Speaker 7

It is asking it is trying to answer this question which is that how do we compute the divergence metric between distributions when we do not know the distributions we do not only have samples of it. uh This adversarial optimization is one way to do it by the way and like variational inference is one other way which will give rise to VEs and diffusion models.

### 01:09:43 · Speaker 7

Okay, so adversarial optimization is one way, the variational inference is one other way, and MMD is one other way, and so on. We will look at different ways of doing it. Maximum likelihood estimation is one other way, which is what is used in uh the LLMs and so on. We will look at uh all, I mean, all possible ones one by one, okay? That is what we do in this course. We do in this course. Okay, so let us look at adversarial optimization. For that,

### 01:10:11 · Speaker 5

Stake

### 01:10:27 · Speaker 5

Okay. Let us

### 01:10:30 · Speaker 5

Let us define, define

### 01:10:34 · Speaker 7

family of divergence metric first.

### 01:10:39 · Speaker 7

this method no that we will look at right now is is powerful enough to uh to be able to uh handle a large class of divergence matrix okay.

### 01:10:54 · Speaker 7

It's a common thing, okay? Or rather it's a it's a method that would enable minimizing the family of divergence metrics, you know, not one divergence metric. It will uh it will uh enable us to minimize a family of divergence metrics, okay? Now for that, let us first define a family of divergence metrics. So given two distributions...

### 01:11:16 · Speaker 7

given to

### 01:11:19 · Speaker 7

probability distributions.

### 01:11:22 · Speaker 6

Let us let me just

### 01:11:25 · Speaker 6

work with density function given two density functions.

### 01:11:32 · Speaker 6

then

### 01:11:32 · Speaker 5

sensitive functions, px and p theta, okay?

### 01:11:43 · Speaker 5

defined

### 01:11:47 · Speaker 5

divergence.

### 01:11:53 · Speaker 7

also also I've already seen one divergence metric no in the last class which was the Hilbert divergence we will I will define a large class of family of divergence metrics okay all of that can be minimized using the technique that we will see in this class okay that's why I'm defining a large class of family of divergence metric even to tensory function p x and p theta define a divergence metric as follows.

### 01:12:21 · Speaker 5

point that has D F between

### 01:12:26 · Speaker 5

px and p theta

### 01:12:29 · Speaker 5

is defined as

### 01:12:50 · Speaker 5

Integral

### 01:12:55 · Speaker 5

p theta of x

### 01:12:59 · Speaker 5

F of

### 01:13:03 · Speaker 6

p x of x divided by p theta of x

### 01:13:11 · Speaker 6

dx

### 01:13:14 · Speaker 6

this is the definition of a prevalence where if

### 01:13:21 · Speaker 6

F of C

### 01:13:21 · Speaker 6

Q is a

### 01:13:23 · Speaker 6

the function that

### 01:13:24 · Speaker 6

tax

### 01:13:30 · Speaker 6

positive real number and maps it to another positive real number. It is a

### 01:13:38 · Speaker 6

convex function

### 01:13:42 · Speaker 6

I will explain it in a while

### 01:13:46 · Speaker 5

Okay

### 01:13:46 · Speaker 6

So

### 01:13:47 · Speaker 5

These are called F divergences.

### 01:13:58 · Speaker 5

Okay

### 01:14:00 · Speaker 7

Okay, so let me explain what this is. Now suppose we are given two density functions and we want to define a divergence metric between them. What is a divergence metric? Remember that it's a it'll give you a sense of distance between uh two density functions, right? Now, uh there is a class of density functions that you can define which are called F divergences, which are which is defined like this. So this is the definition of F divergence.

### 01:14:27 · Speaker 7

okay? uh what is it? It is you take it is integral p theta of x f of px by p theta of x dx. okay? Let us look at this this term that is inside this bracket. Now you know that the density function px of x is a scalar, correct?

### 01:14:49 · Speaker 7

density function is a scalar valued function in the sense that it will take a vector x and it will give you a number a positive real number right

### 01:14:58 · Speaker 7

So all of you know this, right? What is a density function? Density function is a scalar valued function, okay? So now if you evaluate the density function px at some x, you will get a scalar. And if you evaluate the density function p theta of x, you will get another scalar. So ratio of these two, px by p theta at a given point x is a scalar.

### 01:15:21 · Speaker 7

Correct? Now this function F, okay, of U takes a positive real number because the ratio of these two density functions is a scalar. It takes a positive real number and gives you another real number R. That is this value. F of this ratio is this value and the definition of F divergence is integral of P theta of X, okay, times F of P X of X by P theta of X dx integrated over

### 01:15:48 · Speaker 6

all all values of x. This is the definition of what is called

### 01:15:57 · Speaker 6

it has got muted. This is the definition of what is called as a

### 01:16:01 · Speaker 7

called as an f divergence. Now you can choose an f function, okay? I'll give you examples. So now if f of u

### 01:16:14 · Speaker 7

Series of

### 01:16:18 · Speaker 7

U is a what is U here? U is P X by P theta of X okay it's a scalar here I have just given written that as a dummy variable U but in the definition it is the ratio of the density functions. If F of U is equal to log U okay then the corresponding divergence is called the KL divergence.

### 01:16:41 · Speaker 7

Okay? Now with f of c

### 01:16:43 · Speaker 6

U is equal to

### 01:16:45 · Speaker 6

give you

### 01:16:46 · Speaker 5

some examples of it.

### 01:16:55 · Speaker 6

Sorry, it is u log u. Sorry, if it's u log u, then it is that.

### 01:16:59 · Speaker 7

If it's

### 01:17:02 · Speaker 7

half of u log u minus u plus one

### 01:17:10 · Speaker 7

log

### 01:17:12 · Speaker 7

two plus one by

### 01:17:13 · Speaker 6

two, okay? This is called the Jensen-Shannon dividers.

### 01:17:26 · Speaker 5

Okay

### 01:17:27 · Speaker 5

if it's

### 01:17:33 · Speaker 6

Half

### 01:17:35 · Speaker 6

mod u minus one. So this type of instance is called the total variation distance.

### 01:17:48 · Speaker 6

and so on, okay? So now you can choose any convex function.

### 01:17:51 · Speaker 7

for this F and one choice for this convex function will give you one divergence metric. So basically what I am doing is I am defining a family of divergence metric, okay? Which is like one of the I mean you can choose a convex function you get one family of one one divergence metric. So what do you mean by this? If I write U log U here, what will happen to F divergence? Let me show you that. Example.

### 01:18:19 · Speaker 7

example, okay? Now F divergence is given as integral V theta of X log of sorry F of

### 01:18:32 · Speaker 7

F of

### 01:18:34 · Speaker 7

p x of x divided by heat heat of x d x correct? Now let us say that f of u is u log u okay? Now in that case d f will now become integral heat heat of x to substitute u log u for f of u which is

### 01:18:56 · Speaker 7

Now this this entire thing which is right inside this F is now called as U. This is P of X.

### 01:19:04 · Speaker 7

Hello

### 01:19:07 · Speaker 7

p x of x by p theta of x this is u correct

### 01:19:12 · Speaker 6

Hello

### 01:19:13 · Speaker 7

into log of u

### 01:19:18 · Speaker 7

p x of x divided by p theta of x. Note that this entire thing which I have written is

### 01:19:27 · Speaker 7

F of

### 01:19:30 · Speaker 7

three x of x by three theta of x.

### 01:19:32 · Speaker 6

correct? This is what it is. So dx

### 01:19:37 · Speaker 6

Now

### 01:19:43 · Speaker 6

I will skip the algebra, okay? So if you

### 01:19:45 · Speaker 7

simply uh uh this is a times uh log ratio right so you just take the ratio inside and so this okay so this p theta x and this p theta x cancels this will be

### 01:20:03 · Speaker 7

px of x times log of px of x divided by p theta of x dx okay which is nothing but the KL divergence

### 01:20:16 · Speaker 7

Understood. That's what it is, right? So what we are doing is that we are defining a general family of divergence matrix. Now if you take where these are called F divergences. If you take some form for this

### 01:20:31 · Speaker 7

F function that is there in the definition of F divergence, you will get different divergences. You get K divergence with one F. You will get Jensen-Shannon divergence with one other F. You will get total variation distances one other F and so on. So basically, we are defining an infinite family of divergence metric between two distributions depending upon what your F function is.

### 01:20:53 · Speaker 7

The reason I did it, what is the, what is the, uh, the coherence or relevance to this is that the adversarial optimization technique that we see, you look at what we are doing, right? We want to know

### 01:21:07 · Speaker 7

minimize or compute the divergence metric given samples from two distributions, right? Now what divergence metric are we considering? We are considering not one divergence metric. We will be giving you a tool or a technique that would compute and minimize a family of divergence metrics that are called F divergences. You can choose any divergence. See if you people know this generative adversarial networks or GANs, after this paper came, there are so many improvements.

### 01:21:37 · Speaker 7

situations that came over it, no? That's called if I mean like L S Gyan, X squared Gyan, like you know there is some W Gyan, this Gyan, that Gyan, all that.

### 01:21:46 · Speaker 7

There are nothing but changing this f divergence, that's all. So you take one definition for the f divergence, you will get one GAN. So what we are what we will see right now is we will not look at one minimizing one divergence metric. We will now look at minimizing a family of divergence metric given uh samples from the underlying data distribution.

### 01:22:08 · Speaker 7

Is this clear? So now any questions on the definition of f divergence? So basically what we need is given a given some convex function f, a scalar valued convex function f, we can define a divergence metric between pair of distributions.

### 01:22:26 · Speaker 7

Okay, and KL divergence happen to be a special case of this and Jensen-Sanon divergence happen to be a special case of it and total variation distance will happen to be a special case of it and so on. So every there's a lot of very very well known divergence metric, these are all special cases of these F divergences. Okay, in general at an abstraction level this is you think of it like the definition of a class, right? I mean where each of these divergences are one instance of this class of divergences called lever this

### 01:22:59 · Speaker 7

What we will see now is that given the samples from the underlying distributions, how do we minimize any F divergence between those two using samples?

### 01:23:10 · Speaker 6

Hello

### 01:23:11 · Speaker 7

Let me write that down. Now the objective is

### 01:23:15 · Speaker 5

I'll take questions in a while.

### 01:23:21 · Speaker 5

School

### 01:23:25 · Speaker 5

Compute

### 01:23:28 · Speaker 6

compute F divergence, okay?

### 01:23:32 · Speaker 6

Between

### 01:23:34 · Speaker 6

px and pz, okay?

### 01:23:38 · Speaker 6

using

### 01:23:41 · Speaker 5

their samples

### 01:23:44 · Speaker 5

the samples.

### 01:23:47 · Speaker 5

Without

### 01:23:52 · Speaker 5

knowing what P X and P theta are.

### 01:23:58 · Speaker 6

Right? We have

### 01:24:00 · Speaker 7

we don't know px and p theta but we have samples from px and p theta. Now how do you compute the f divergences between them is the next question that we will answer.

### 01:24:10 · Speaker 7

Okay, any questions here?

### 01:24:14 · Speaker 7

Okay

### 01:24:16 · Speaker 7

Shivam

### 01:24:16 · Speaker 4

Shivam

### 01:24:17 · Speaker 7

one

### 01:24:18 · Speaker 4

Yes sir. Yes sir, on the f divergence side as we have said we can have infinite combinations of f divergence function. And

### 01:24:27 · Speaker 7

combinations no no. No there are no combinations here. We can have infinite F divergences by changing F.

### 01:24:36 · Speaker 4

Yes. Yes, so, yeah, but we are talking about the three variations, the KL divergence, GS divergence. So, is there any specific benefit does they bring into the table or...

### 01:24:44 · Speaker 7

Tennis

### 01:24:48 · Speaker 7

Good question. Yes, they do. They do. In fact, I'll after we look at how to minimize this, no, I will tell you like advantages and disadvantages of let's say at least K L and Jensen-Chanon divergence, okay?

### 01:25:06 · Speaker 7

But yeah, so different divergences have different properties. That's a good point that you made. Why do we need so many divergence metrics? Why can't we look at one of them is because different divergence metric offer different properties. uh I will talk about it, right? I mean, just after we look at this algorithm, right? uh Remind me, Shivam, okay? If I forget it, just remind me to bring out the uh let's say properties of at least one or two divergences here.

### 01:25:32 · Speaker 4

श्योर सर, थैंक यू।

### 01:25:33 · Speaker 7

But yeah, so that's the point. I mean, why do we need so many divergences? In fact, if you come up with a different divergence which has good properties, you can name it Shivam divergence. That's how people have done it. They have, I mean, different people have come up with different divergences and called them with their own name, okay? But you'll have to ensure that these, these things are there, right? I mean, you'll have to ensure that this is a convex function, to be mathematically precise, this is actually a left semi-continuous function, okay? and

### 01:26:07 · Speaker 7

left semi continuous function and also f of zero has to be equal to one. It's a convex left semi continuous function such with f of zero equal to one. So if you can come up with such a function that becomes a new divergence metric. uh and if you if it has favorable properties you can use that in your generating models. Yeah.

### 01:26:28 · Speaker 8

So why should the function be convex?

### 01:26:33 · Speaker 8

I mean we know that but

### 01:26:33 · Speaker 7

that moment

### 01:26:35 · Speaker 8

just that it should be when you do argmin, is it?

### 01:26:35 · Speaker 7

Hmm

### 01:26:36 · Speaker 7

Jisnet

### 01:26:40 · Speaker 7

No no, we are not doing argument here anything, right? I mean it is optimization. We do optimization over D F. We minimize the divergence metric, no? We don't we have nothing to do with F. F is a F is actually a hyperparameter, right? We fix F, yeah. Okay, okay, okay. We choose an F divergence. It has nothing to do with the optimization.

### 01:26:43 · Speaker 8

Optimization

### 01:26:55 · Speaker 8

param

### 01:26:57 · Speaker 8

ஓகே ஓகே

### 01:26:57 · Speaker 6

which

### 01:27:03 · Speaker 7

It is just the difference

### 01:27:04 · Speaker 6

of the F divergence

### 01:27:09 · Speaker 5

ओके सर

### 01:27:10 · Speaker 6

Any other question here?

### 01:27:15 · Speaker 6

Skin

### 01:27:15 · Speaker 7

in practice what we do is that we actually fix an F. I mean for instance in the knife vanilla Gyan paper right they choose this F to be equal to this particular F.

### 01:27:26 · Speaker 7

root it no this particular f this is this this thing

### 01:27:31 · Speaker 7

is what they do in the nice vanilla gyan

### 01:27:37 · Speaker 7

they take Jensen-Sanon divergence in the the vanilla generative adversarial network, they choose this F to be equal to this particular form and they what they minimize is the Jensen-Sanon divergence, okay?

### 01:27:54 · Speaker 7

you choose it, you actually fix it, you fix that. You fix that uh f divergence uh and then compute and minimize uh to find a sample.

### 01:28:07 · Speaker 5

Is that okay?

### 01:28:14 · Speaker 5

Hello

### 01:28:16 · Speaker 5

minus

### 01:28:20 · Speaker 6

Yes.

### 01:28:20 · Speaker 5

Yes, can you hear me?

### 01:28:22 · Speaker 6

Yes yes yes okay

### 01:28:26 · Speaker 6

ओके

### 01:28:27 · Speaker 7

any other question on the definition of whatever this is?

### 01:28:34 · Speaker 7

this needs an uninterrupted to answer this question right you know we need

### 01:28:42 · Speaker 7

forty forty five minutes of uninterrupted time. Maybe let's just take a break and then get back. Shall we?

### 01:28:54 · Speaker 6

Let's take a break now. It's ten fifty five in my clock. Let's resume at eleven fifteen.

### 01:29:02 · Speaker 6

See you in about 15-20

### 01:29:03 · Speaker 5

in the moments

### 01:51:02 · Speaker 5

Hello, shall we resume?

### 01:51:08 · Speaker 5

Yes sir

### 01:51:08 · Speaker 6

Yes sir

### 01:51:12 · Speaker 7

one of the most challenging parts of this online teaching is that I don't get to see you at all, right? I mean all I get to see is this stupid screen and as a as a teacher I've been we would have developed this ability to look at the face of your audience and kind of mostly discern what is going on. I mean are they appreciating what you are saying? Are they understanding what I said? You know when to repeat, you know when to stop?

### 01:51:42 · Speaker 7

not to repeat etcetera. The complete feedback mechanism is gone. Now here it is only me talking, don't even know whether your people exist or not. It's such a challenging thing to do that online. Anyway, okay, I see a couple of hands raised. Yeah, Astik.

### 01:52:02 · Speaker 3

Yeah, sir, so you mentioned some properties about this F function for F divergences. Can you move a little up?

### 01:52:09 · Speaker 7

Correct

### 01:52:11 · Speaker 7

should be convex, lower semi continuous and that zero it should evaluate to one.

### 01:52:16 · Speaker 3

Uh but this is not following in this these three functions that we write right? This f zero is equal to

### 01:52:22 · Speaker 7

hold on I think I just thanks for that

### 01:52:26 · Speaker 3

It should be I think F one is equal to zero

### 01:52:28 · Speaker 7

one and zero. Correct, correct. Thanks.

### 01:52:32 · Speaker 3

Yeah

### 01:52:32 · Speaker 7

correct. It's correct. It should evaluate to zero at one. Correct. Thanks.

### 01:52:38 · Speaker 6

Yeah

### 01:52:41 · Speaker 7

Okay, shall we continue?

### 01:52:45 · Speaker 6

Yes, sure.

### 01:52:46 · Speaker 7

Okay, uh see as I said no the goal is now to compute this divergence between a pair of distributions when the distribution is unknown, samples are given. So here is the uh overall philosophy of how it is done. As I said no this is a recurrent theme that comes up in almost all the M L models. How is it done is the following. Now observe that these F divergences right any divergence metric. Now involves okay let me not write the F. So suppose you have let's say an integral okay

### 01:53:22 · Speaker 7

need to compute an integral of let's say some function. running out of alphabets. This is taken B is taken H okay let's take some function H with respect to some probability density P X P X okay if this integral has to be evaluated okay. Now let's say that we need to evaluate this integral.

### 01:53:47 · Speaker 5

evaluate this.

### 01:53:54 · Speaker 5

Okay, which

### 01:53:56 · Speaker 5

with

### 01:53:58 · Speaker 5

P X unknown, okay?

### 01:54:02 · Speaker 5

But

### 01:54:05 · Speaker 5

samples from VX.

### 01:54:16 · Speaker 5

Okay, suppose

### 01:54:17 · Speaker 7

suppose you need to evaluate this sort of an integral where h is some function h of x is

### 01:54:24 · Speaker 7

some function. Any function, okay? Some function of x. So you have some function of x and you need to integrate evaluate this integral with px unknown. So if you don't know px then you cannot of course integrate this out, right? Now one statistical tool that can be used to do this approximately. Of course you can't evaluate it exactly because you don't know what px is. But it can be approximated. How? There is this nice theorem called Raw Laws Law

### 01:54:55 · Speaker 6

large numbers

### 01:54:58 · Speaker 6

I would say

### 01:55:05 · Speaker 5

Okay, last large number says the following. Suppose

### 01:55:13 · Speaker 6

x one, x two

### 01:55:16 · Speaker 6

up to x n, okay, are sampled from some peers. Okay, then, then, to compute some

### 01:55:26 · Speaker 6

Okay.

### 01:55:29 · Speaker 6

Inter

### 01:55:29 · Speaker 5

through

### 01:55:31 · Speaker 5

H of X

### 01:55:34 · Speaker 5

CX DX, okay?

### 01:55:44 · Speaker 5

can be approximated by

### 01:55:48 · Speaker 5

limit of

### 01:55:50 · Speaker 5

one

### 01:55:50 · Speaker 6

by N

### 01:55:53 · Speaker 6

I is one through N.

### 01:55:56 · Speaker 6

Sir

### 01:55:58 · Speaker 6

H that is evaluated at X I.

### 01:56:03 · Speaker 6

where X I are

### 01:56:04 · Speaker 7

samples from peaks

### 01:56:09 · Speaker 7

This is a very strong and powerful result. What are we saying here? Please note this. Now, uh n goes to infinity. So we are saying, suppose you have lots of samples drawn from a distribution. Okay? Then if you want to compute this sort of an integral, that can be approximated simply by taking the sample mean of all these functions, I mean all, I mean the sample mean the function values evaluated at all those x i's coming from p x

### 01:56:44 · Speaker 7

Now a special case of this is maybe something that all of you know, right?

### 01:56:49 · Speaker 7

h of x is simply equal to x. Then what happens? Then what is this?

### 01:56:58 · Speaker 6

What is this thing called?

### 01:57:00 · Speaker 5

expected

### 01:57:00 · Speaker 6

expectation. So the expectation of

### 01:57:05 · Speaker 6

X

### 01:57:06 · Speaker 7

this is the expectation of X, right? Now in fact, this is the expectation of

### 01:57:15 · Speaker 7

H of X with respect to this density P X, okay, density definition. Now this is the expectation of X with respect to P X. Now this can be approximated using

### 01:57:30 · Speaker 7

This all of you know, no? This is what we do in practice, isn't it? If you want to know the expectation of a distribution, you just take the sample mean. What is this? This is the sample mean.

### 01:57:44 · Speaker 7

sample mean approximates the true expectation asymptotically which means if A one is N N N goes to infinity if you have enough number of samples then sample mean can be approximated sorry the true expectation can be approximated using sample means. All of you know this right this is called law of large numbers.

### 01:58:05 · Speaker 5

Any questions on this?

### 01:58:18 · Speaker 5

Hello, am I audible?

### 01:58:24 · Speaker 7

Okay. Now, yeah, so why did I so basically what did I say here that you don't have what did we do here look at this no? We have integrals. I mean this integral is nothing but the expectation of

### 01:58:38 · Speaker 7

definition, this is the expectation of some function h of x with respect to p x. If you want to compute the expectation of a function with respect to some distribution, okay? Without knowing the distribution, but you have samples from it, you can invoke laws of large numbers and simply compute the sample average, okay? Over all the samples that are coming from the distribution. See, please note this very carefully, while we do not know what the

### 01:59:08 · Speaker 7

distribution P X S. We have samples from them. That is exactly the scenario that we have right now with us, no? We we have samples from the distributions, we don't have the distributions. But in spite of not having the distribution, we can evaluate expectations of functions of uh random variables with respect to the underlined distribution using sample averages.

### 01:59:30 · Speaker 6

Is this clear? Is this idea clear?

### 01:59:39 · Speaker 6

ओके। नाउ, लेट्स कम बैक टू व्हाट वी हैड इन आवर माइंड। सो वी

### 01:59:43 · Speaker 7

want to minimize the f divergence, want to compute the f divergence. Now let me connect the dots. If we if I can express the f divergence, let me write that if

### 01:59:57 · Speaker 7

f divergence can be expressed

### 02:00:00 · Speaker 1

and be expressed.

### 02:00:03 · Speaker 1

expressed. In terms of

### 02:00:08 · Speaker 1

in terms of expectations

### 02:00:15 · Speaker 1

Over

### 02:00:18 · Speaker 1

एक सेकंड पीछे का। देन, देन।

### 02:00:22 · Speaker 1

DF can be computed

### 02:00:30 · Speaker 1

using

### 02:00:36 · Speaker 1

samples from

### 02:00:42 · Speaker 1

Susan

### 02:00:45 · Speaker 1

using using the word using two types

### 02:00:50 · Speaker 1

Well

### 02:00:53 · Speaker 1

Law

### 02:00:56 · Speaker 1

large numbers

### 02:01:06 · Speaker 1

Okay, what I'm saying is, we want to

### 02:01:08 · Speaker 3

the f divergence between pair of distributions. We don't know what the underlying distributions are, but we have the samples from it. Now we also have this nice result called law of large numbers that would say that the expectations of some functions with respect to some in underlying distributions can be computed using sample averages if we have samples from it. That's what law of large numbers says. Now connect these two that if we can somehow

### 02:01:38 · Speaker 3

plus the f divergence or the quantity that we want to compute in terms of expectations over px and p theta, then we can use law of large numbers.

### 02:01:47 · Speaker 1

approximate the F divergences. Do you agree?

### 02:01:59 · Speaker 1

That is exactly what we will do now. Now the goal is to now...

### 02:02:06 · Speaker 1

is to express

### 02:02:10 · Speaker 1

f divergence, okay.

### 02:02:12 · Speaker 1

in terms of

### 02:02:17 · Speaker 1

expectations.

### 02:02:22 · Speaker 1

Four

### 02:02:27 · Speaker 1

px and

### 02:02:31 · Speaker 1

Okay

### 02:02:31 · Speaker 3

Right? That's what we will do. Now unfortunately what happens is this is not possible. You can't express the F divergence or any divergence metric in terms of expectations over P X and P theta. Okay? However...

### 02:02:44 · Speaker 4

Hello

### 02:02:45 · Speaker 3

Hello

### 02:02:45 · Speaker 4

for

### 02:02:48 · Speaker 3

we can express bounds on

### 02:02:51 · Speaker 1

f divergence using expectations. So let me write that.

### 02:03:25 · Speaker 1

Okay, so what I mean

### 02:03:26 · Speaker 3

saying, I mean, F divergence cannot directly be expressed as expectations over this, but we can express lower bounds on F divergences in terms of expectations. What do you mean by lower bound? We'll compute a quantity, okay, which is always greater than or equal to F divergence, okay? Then this quantity can be expressed in terms of expectations, expectations over P X and P theta.

### 02:03:52 · Speaker 3

Okay? And then remember that finally we want to find the G theta, okay, or our generator function such that this F divergence is minimized, right? Now because we cannot compute the F divergence, what we do is we carve a lower bound on the F divergence, which can be computed and we minimize this lower bound instead.

### 02:04:13 · Speaker 3

Does it make sense?

### 02:04:15 · Speaker 3

But that's not an exact thing, right? I mean, uh it would have been great if we can actually minimize the F divergence itself. But we cannot minimize the F divergence directly because F divergence cannot be computed without knowing the distributions. Now what do we do? Instead of minimizing the F divergence, we minimize a lower bound on that.

### 02:04:36 · Speaker 3

Okay? We minimize a lower bound, rather we minimize a quantity that is always greater than the f divergence, right? uh Yeah, the f divergence, minimize a lower bound on f divergence and that lower bound can be expressed in terms of expectations over px and p theta.

### 02:04:55 · Speaker 1

Is this is this clear?

### 02:05:05 · Speaker 1

Any questions?

### 02:05:05 · Speaker 3

on this, see these are very very critical and important stuff, okay?

### 02:05:08 · Speaker 2

which is again as I said this is a recurrent theme that would keep coming. So if you have questions here do ask me.

### 02:05:15 · Speaker 3

I'll wait for a minute

### 02:05:21 · Speaker 1

Now this implies that instead of

### 02:05:35 · Speaker 1

minimizing f divergence.

### 02:05:38 · Speaker 1

to minimize

### 02:05:46 · Speaker 1

Lower bond

### 02:05:54 · Speaker 1

Any questions on this?

### 02:06:03 · Speaker 3

Don't ask me how do we do it that is what we will see but yeah on the philosophy yeah. Somebody.

### 02:06:08 · Speaker 4

Sir, that will be an approximation, right? Like

### 02:06:11 · Speaker 3

Correct, correct. Correct, that will be an approximation, but unfortunately, that's the best that we can do.

### 02:06:19 · Speaker 3

Because you know that like the fundamental problem is that we don't have access to P X and P theta you see. If we do not have access to P X and P theta this is the best that we can do.

### 02:06:25 · Speaker 6

agree

### 02:06:30 · Speaker 3

But yeah, what you said is true. It's an approximation. You will you will not get the the correct minimization of web table things.

### 02:06:40 · Speaker 4

ओके सर

### 02:06:42 · Speaker 3

any other yeah Lokesh

### 02:06:45 · Speaker 0

Yeah, so if we are minimizing the lower bound, does that mean it does not mean that if you have a lesser lower bound, one model is better than the other, right?

### 02:06:56 · Speaker 3

correct correct

### 02:06:56 · Speaker 0

correct. It's only the lower bound that we

### 02:06:58 · Speaker 3

Correct, correct, that is correct. That is correct. That is why you know it's better to that's very good question actually. You know that is why we need a tighter lower bound.

### 02:07:09 · Speaker 3

Right, I mean the tighter the boundaries the better your model is. We will crave to have a tighter lower bound. See if you know what a GAN is, right, generative adversarial network. You will have two networks there, right? One is the generator network that we already wrote. There will be another network called discriminator network. You are are you aware of it?

### 02:07:28 · Speaker 1

Yeah, yeah.

### 02:07:30 · Speaker 3

See that is actually to carve this lower bound. We will see that in a while. So why do we say that the discriminator has to be very good is because the lower bound that we compute has to be very tight otherwise you know it it doesn't mean it it would be a very uh loose approximation which will not lead to a good generative model.

### 02:07:51 · Speaker 5

Okay

### 02:07:52 · Speaker 3

Yeah, but this is the best that we can do. Why I mean, why is this problem arising is because we don't know P X and P theta.

### 02:08:00 · Speaker 3

Since we do not have P X and P theta, we need to do something, right? What do we do? We'll we'll carve out a lower bound on F divergence and then minimize that. Now this lower bound can be computed using the the expectations over I mean using the samples of P X and P theta, that's the point.

### 02:08:21 · Speaker 3

So the lower

### 02:08:21 · Speaker 5

So the lower bound is in terms of is for the term E P X minus E P theta right?

### 02:08:27 · Speaker 3

it will take that form. It will take that form of like differences in expectations. That is what we are going to show now. Okay, that's the whole result. The lower bound that we carve, you know, that can be expressed in terms of expectations over these two distributions that we have. And

### 02:08:46 · Speaker 3

Excuse me, once we express them as expectations, right? Over these two distributions, we can compute that using

### 02:08:52 · Speaker 2

Samples

### 02:08:54 · Speaker 1

Okay

### 02:08:55 · Speaker 2

Excellent. Yeah.

### 02:09:00 · Speaker 2

Any other question?

### 02:09:02 · Speaker 6

Uh yeah sir uh sir we if we don't know P X and P theta uh as as you have said we know the samples from it. And uh on the above you have applied law of large number to find the expectations using the samples. So why can't we just directly apply uh into K L into while we calculate divergence. Like we can apply the same tactic uh in in in while finding the divergence as well right.

### 02:09:17 · Speaker 5

Bike

### 02:09:31 · Speaker 3

That's what I'm saying, you know, these divergences, for instance, if you take this some like Jensen-Shannon divergence, right? You can't express that in terms of expectations. If you can express that in terms of expectations, then great, but you can't.

### 02:09:44 · Speaker 3

The whole point is that you can't write this F divergence, this F divergence, right? Is that?

### 02:09:52 · Speaker 3

this definition of f divergence in terms of expectations over p theta and p h. If you can then that's it. I mean it's it's an exact approximate exact computation. But you cannot represent that. That's the problem. Because of that you need to do something. What do we do? We carve a lower bound on f divergence which can be represented as expectations. Right? Which can be

### 02:10:16 · Speaker 3

Hello

### 02:10:17 · Speaker 3

uh

### 02:10:17 · Speaker 3

Wow

### 02:10:18 · Speaker 2

Hello

### 02:10:18 · Speaker 2

computer. That's the whole point.

### 02:10:22 · Speaker 3

understand that?

### 02:10:25 · Speaker 5

So just a small extension so uh we can't do it because it's not a H of X right but it is it's depend because if you see the form it is very similar to expectation.

### 02:10:26 · Speaker 6

all extra

### 02:10:34 · Speaker 3

expectation. Not necessarily, no. You have F. See, it is not, see, H of X, right? It is not H of P of X, you see? Yeah, exactly. Yeah, so there is there are there are ratios of densities here, right? This cannot, this is not equal to, for instance, expectation of F of that with respect to P theta. This is not equal to that.

### 02:10:43 · Speaker 1

Yeah, exactly.

### 02:10:56 · Speaker 3

Understand?

### 02:10:58 · Speaker 5

Yeah, because it itself depends on the P and P and P theta.

### 02:11:00 · Speaker 3

if it has a dependence on P X and P theta, it is not equal to the expectation, right? You need to do something else to write it as an expectation of functions over these two distributions. The way to do it is to carve a lower bound on it and then express that as expectation which can be computed.

### 02:11:04 · Speaker 5

is not equal to

### 02:11:19 · Speaker 5

Yeah, got it.

### 02:11:20 · Speaker 3

Hello

### 02:11:24 · Speaker 2

Anything else? Anybody else?

### 02:11:29 · Speaker 3

Okay. Now, uh yeah, as I said, no, the classes now will get a little denser. uh So please focus uh and you know, as much as possible and remember what what's going on. Otherwise, you know, it's very easy to get lost. uh I mean, there are too many things that we will do, right? I mean, unless you know what the storyline is, you will kind of uh

### 02:11:53 · Speaker 3

loose the track, please focus. Okay, so now what is, what should we do? We should now carve a lower bound, right?

### 02:12:02 · Speaker 1

Let me write that expressing

### 02:12:06 · Speaker 1

bounding DF.

### 02:12:12 · Speaker 1

and expressing it in terms of expectations.

### 02:12:31 · Speaker 1

expectations.

### 02:12:50 · Speaker 1

Okay, this is what we will do now.

### 02:12:54 · Speaker 1

Okay, let us start from the definition.

### 02:12:56 · Speaker 2

of f divergence, f divergence between ax and b theta given as integral

### 02:13:06 · Speaker 1

these three topics

### 02:13:09 · Speaker 1

test computed it

### 02:13:12 · Speaker 1

ratio of P X and P theta

### 02:13:18 · Speaker 1

index

### 02:13:23 · Speaker 1

This is the

### 02:13:24 · Speaker 2

definition of divergence.

### 02:13:30 · Speaker 2

Hello

### 02:13:31 · Speaker 1

um

### 02:13:33 · Speaker 1

Okay

### 02:13:33 · Speaker 2

To do this, we'll have to know what is called as a

### 02:13:39 · Speaker 2

conjugate

### 02:13:43 · Speaker 1

conjugate of a convex function.

### 02:13:54 · Speaker 3

Now remember what we are doing we are trying to bound the f divergence and express it in terms of expectations to do this we will start with what is called as the conjugate of convex function. Now the thing is if f

### 02:14:06 · Speaker 2

is a convex function.

### 02:14:11 · Speaker 2

next function

### 02:14:13 · Speaker 2

Let me call it f of u because it's

### 02:14:17 · Speaker 2

it is a scalar valued function that we are talking about here, right? in the f divergence convex function.

### 02:14:24 · Speaker 2

there exists

### 02:14:29 · Speaker 1

there exists convex conjugate

### 02:14:37 · Speaker 1

convex conjugate function

### 02:14:41 · Speaker 1

F

### 02:14:41 · Speaker 3

star of t. Note that both u and t are dummy variables, okay? Simply some variables. star of t.

### 02:14:51 · Speaker 1

defined as follows

### 02:15:02 · Speaker 1

F star of T at a point T is given as the maximum of

### 02:15:13 · Speaker 1

U T minus

### 02:15:16 · Speaker 1

S O C U

### 02:15:22 · Speaker 1

case of U.

### 02:15:24 · Speaker 2

maximum is over U which is the domain of

### 02:15:29 · Speaker 3

Yes

### 02:15:32 · Speaker 3

I will explain what this is.

### 02:15:36 · Speaker 3

what we are saying is that every convex function F, okay, has what is called as a convex conjugate, okay? Now what is convex conjugate? It is another function F star of T, okay, that is defined this way. F star of T is simply, F star of T at T is simply the maximum of U T minus F of U, where U comes from domain of F.

### 02:16:01 · Speaker 3

What does that mean? Let me just draw it and show you. Let's say that you have some convex function, let us call this f of u. This is a convex function, right? And this is axis is that this is the u axis and this is f of u, okay? Now...

### 02:16:21 · Speaker 3

Let's say that you take a point here, some point on the U axis.

### 02:16:28 · Speaker 3

Let me call this U, okay? Now what I can do is, I can construct, I can construct, I can write

### 02:16:38 · Speaker 3

multiple lines

### 02:16:40 · Speaker 2

Okay

### 02:16:42 · Speaker 2

all of which are less than

### 02:16:46 · Speaker 2

If of you at that point, do you agree?

### 02:16:53 · Speaker 3

So given a convex function, okay? I take a value of that convex function at a point. I can construct infinite number of lines, okay? I can draw infinite number of lines that lie below that point, okay? For all...

### 02:17:08 · Speaker 2

यू. डू यू एग्री?

### 02:17:18 · Speaker 2

Okay. So out of those all, I mean there are infinite lines that I can draw, right? Out of all those lines, there is also this line which is the tangent.

### 02:17:35 · Speaker 1

is also the tangent, okay?

### 02:17:37 · Speaker 3

that that is equal to the value of that function at that particular point, okay? Now, the this is this point, right? I mean the the intersection of that tangent and this particular curve is what I've called as maximum here. Look at this. UT minus F of U, okay? for different values of P represent, okay, different values of U, different values of P represent all these lines that I can write at every point of the convex function.

### 02:18:15 · Speaker 3

Let us take one point for instance. If I take one point of this convex function, there are multiple lines that I can draw to this this curve at that particular point which is represented by this family of lines. Now amongst all these possible lines, okay?

### 02:18:32 · Speaker 3

If you take the maximum value of all these possible lines at that particular value of U, what do you get? It's actually the value of that tangent up to that function at that point. That is the value of that convex conjugate at that T.

### 02:18:50 · Speaker 3

you get it?

### 02:18:51 · Speaker 4

Sir, one question.

### 02:18:54 · Speaker 3

It's actually not the tangent, right? It's actually the slope.

### 02:18:58 · Speaker 3

at that particular point. Now if you collate all these at different points of U, you get another function, right? It's the collection of slope of this function at all points, that becomes the conjugate conjugate.

### 02:19:10 · Speaker 4

Sir, one question.

### 02:19:12 · Speaker 3

Yeah

### 02:19:13 · Speaker 4

Sir, it's basically the function value f of u, right? Even if we are denote, we are getting that through the tangent, the maximum value will be f of u only.

### 02:19:27 · Speaker 3

maximum of, maximum of UT minus F of U. That's what I'm saying.

### 02:19:27 · Speaker 4

like

### 02:19:32 · Speaker 3

Not F of U

### 02:19:35 · Speaker 4

Okay, no, I'm I'm what I'm you are explaining about this this concept, right? Like we can have infinitely possible lines at a particular U. One of them will be the

### 02:19:35 · Speaker 3

Okay, no, I'm

### 02:19:45 · Speaker 3

So that are that are that are less than this at all points, right?

### 02:19:49 · Speaker 4

Correct, Correct.

### 02:19:49 · Speaker 3

that are less than that at all points. So now I'm considering out of all of those possible lines, I'm considering the one that has the maximum value at that particular particular U. And that I'm considering as the value of that conjugate function at that particular P.

### 02:20:07 · Speaker 4

So that value is corresponding to F F star of T. Like that is that is

### 02:20:13 · Speaker 3

That is that is the value of correct that is the value of H star of T at that particular point

### 02:20:20 · Speaker 3

See, U T, I mean F of U is a, what does U T minus F of U represent? See, F of U minus F of U, right? This F of U is the

### 02:20:30 · Speaker 2

Hmm

### 02:20:32 · Speaker 2

something happened.

### 02:20:37 · Speaker 2

Hold on

### 02:20:38 · Speaker 3

This f of u is the intercept, right?

### 02:20:42 · Speaker 3

the given point is f of u this is this is like mx plus c isn't it?

### 02:20:47 · Speaker 4

Yes sir

### 02:20:49 · Speaker 3

This is the intercept, okay? Now, uh, you see when T is the slope and U is the value of the domain at that point. So basically, U T minus F of U will give you a line.

### 02:21:03 · Speaker 3

at any f of u, u t minus f of u will give you a line, okay, whose intercept is f of u.

### 02:21:11 · Speaker 3

Right?

### 02:21:13 · Speaker 4

Okay

### 02:21:14 · Speaker 3

Now I'm saying out of all these possible lines, okay, that are less than the function value at that particular point, I'm looking at

### 02:21:24 · Speaker 2

lying, okay, which is maximum.

### 02:21:33 · Speaker 1

Okay

### 02:21:34 · Speaker 2

Do you understand?

### 02:21:36 · Speaker 6

Sir, uh

### 02:21:37 · Speaker 2

Now, yeah.

### 02:21:39 · Speaker 6

it lead to one confusion um that the the distance should be minimum right like uh the value at f of u and u t minus f of u the line which you have it should be very close to f of u to get a tighter bond right? So it should be the line should be the minimum of it

### 02:21:42 · Speaker 3

that

### 02:21:57 · Speaker 6

maximum

### 02:21:57 · Speaker 3

the maximum of the value, no? The maximum value of that function. See, we are looking at the value of this function itself. Now this u t minus f of u is a value that evaluates to something. So you're looking at the maximum of that.

### 02:22:13 · Speaker 3

And the maximization is over all possible U. See, the optimization is over the U domain. You look at all possible U's here.

### 02:22:25 · Speaker 3

Okay, so amongst all possible use,

### 02:22:28 · Speaker 2

look at that u which would maximize this this entire thing u t minus f of u

### 02:22:40 · Speaker 2

Fix a T, okay?

### 02:22:41 · Speaker 3

a T. So what do you mean by fixing a T? See, you can you can see T as the slope, okay? You see T as the slope, you fix a slope. You see you fix a particular slope, maybe the way I have written the figure has a different interpretation, okay? Let me rewrite it, hold on.

### 02:22:59 · Speaker 1

Hello

### 02:23:03 · Speaker 1

more intuitive.

### 02:23:12 · Speaker 1

Is it not moving?

### 02:23:16 · Speaker 1

Okay

### 02:23:19 · Speaker 1

let me draw a convex beam.

### 02:23:27 · Speaker 1

is a convex function. Let us take one particular cube. Okay? Here

### 02:23:37 · Speaker 1

the axis.

### 02:23:47 · Speaker 1

T is the slope and

### 02:23:55 · Speaker 1

F of U is the intercept, right?

### 02:23:58 · Speaker 1

minus f of u is the intercept. So this is

### 02:24:05 · Speaker 1

This is f of u

### 02:24:11 · Speaker 1

minus f of u should come the other side.

### 02:24:23 · Speaker 1

That is the intercept.

### 02:24:26 · Speaker 1

Now, um

### 02:24:35 · Speaker 1

you are looking at maximum with respect to you.

### 02:24:40 · Speaker 2

is such the function d is the slope now this is

### 02:24:45 · Speaker 2

You can write

### 02:24:49 · Speaker 1

this is one T, okay? that that has the intercept you can write

### 02:25:04 · Speaker 1

go through that now.

### 02:25:07 · Speaker 1

another line and this is

### 02:25:15 · Speaker 1

straight lines

### 02:25:16 · Speaker 3

another line. There's another line and so on. These are the lines that we are talking about. Is this clear? I think now it is correct.

### 02:25:24 · Speaker 6

Yes, yes, sense. Correct.

### 02:25:26 · Speaker 3

Correct? Yeah. These are used, correct? Yes sir. Now, amongst all these possible lines, I am looking at that particular line, okay, which would maximize that at that use.

### 02:25:27 · Speaker 6

யா

### 02:25:30 · Speaker 6

Yes

### 02:25:39 · Speaker 2

is the U that we are talking about.

### 02:25:47 · Speaker 2

Okay? So amongst all possible

### 02:25:50 · Speaker 3

lines okay that would be a lower bound for this function at that particular u I am looking at

### 02:25:57 · Speaker 3

that line which would maximize the this this value U T minus F of T

### 02:26:05 · Speaker 3

Is that clear?

### 02:26:08 · Speaker 1

Yes sir. Yes sir, now clear.

### 02:26:10 · Speaker 2

By the way, it may not be a tangent, all times it may not be the tangent.

### 02:26:18 · Speaker 2

Okay

### 02:26:21 · Speaker 2

So this okay so you're not seeing the entire picture.

### 02:26:22 · Speaker 1

Yes

### 02:26:24 · Speaker 3

That's

### 02:26:25 · Speaker 3

So these are multiple lower bounds that are possible for that for the convex function at that particular value. Amongst all possible lower bounds, we are looking at

### 02:26:35 · Speaker 3

that possible line that line okay that would maximize this

### 02:26:44 · Speaker 2

Are you clear on this? Any questions?

### 02:26:55 · Speaker 2

Sorry the quantity which we are maximizing can you show it on graph? Possible?

### 02:27:03 · Speaker 1

US

### 02:27:03 · Speaker 3

Next

### 02:27:05 · Speaker 3

U is fixed. So, so the value of

### 02:27:07 · Speaker 2

minus f of u

### 02:27:10 · Speaker 3

and yeah. U T minus F of U is the line, no? This is this is one U T minus F of U. Let's call this T one. This is like U T two minus F of U and so on, right?

### 02:27:11 · Speaker 2

the whole

### 02:27:23 · Speaker 3

amongst all possible lines, we are taking that line which has the maximum value.

### 02:27:31 · Speaker 2

at that you, at you.

### 02:27:36 · Speaker 3

at you this this line has this particular value right at you this line has this particular value and so on I can construct more such line you know which becomes lower bound I can construct another line you understood right

### 02:27:49 · Speaker 3

different lines have different values at that U. So now amongst all possible lines I'm taking that line, okay, which has maximum value and the value of that line at that particular U happens to be the value of the conjugate at that T.

### 02:28:06 · Speaker 2

Hmm

### 02:28:06 · Speaker 3

Yeah, does it make sense now?

### 02:28:10 · Speaker 2

A

### 02:28:11 · Speaker 5

So is it the value of U that maximizes U of T minus F of U?

### 02:28:15 · Speaker 3

minus f of u. Correct. The maximization is over domain for a given for a given of for a

### 02:28:18 · Speaker 5

one

### 02:28:19 · Speaker 5

for a given, for a given of, for a given value of t, right?

### 02:28:24 · Speaker 3

Correct. Correct.

### 02:28:25 · Speaker 5

you choose a T and then find the maximum of U, find the U that maximizes UT minus F of U.

### 02:28:31 · Speaker 3

that would be the value of f star of t at that particular moment.

### 02:28:35 · Speaker 5

Okay. Okay.

### 02:28:37 · Speaker 2

It's a point wise definition.

### 02:28:41 · Speaker 2

Make sense?

### 02:28:45 · Speaker 1

Yes

### 02:28:45 · Speaker 2

So this is this

### 02:28:46 · Speaker 3

has nothing to do with like you know divergences or anything. This is just a definition of a convex conjugate of any convex function. This is true for any convex function, okay? It's also called differential conjugate, basically the definition of a conjugate function. Okay.

### 02:28:59 · Speaker 2

Shall we move on?

### 02:29:06 · Speaker 2

Okay, now

### 02:29:10 · Speaker 2

this

### 02:29:10 · Speaker 3

has to be taught in convex optimization course but it's okay. I'll whatever we need we will do it. So now

### 02:29:21 · Speaker 3

So there is a property that would say that that F star, F star, I'll state this without proof, F star is also convex.

### 02:29:32 · Speaker 3

star is also convex and

### 02:29:36 · Speaker 3

So okay so first of all we say that f star is also convex. If f star is also convex this implies that you can take the conjugate of the conjugate right? Because f star is conjugate. Now we know that every convex function has a conjugate which means that the conjugate also has a conjugate and this property there's a property that would say that the

### 02:29:58 · Speaker 3

double conjugation of the function will take you to the original function. So this is another property that we will use. Okay? So two things, one, f star is also convex, which means that that also has a conjugate and that will take you back to the original function. Okay? What this implies that

### 02:30:16 · Speaker 3

we have

### 02:30:17 · Speaker 2

have the original okay so f of t

### 02:30:24 · Speaker 2

was the conjugate

### 02:30:27 · Speaker 2

for f of u, right?

### 02:30:32 · Speaker 2

let me write that maybe

### 02:30:37 · Speaker 3

Q T minus

### 02:30:39 · Speaker 3

f of u and this is over u, right? So now this is the f star of t, this is the conjugate for f, right? Now we can take a conjugate of the conjugate. f star of t, you take

### 02:30:57 · Speaker 3

the conjugate of the conjugate, what is this?

### 02:31:01 · Speaker 3

is equal to f of u we know that. Okay? So conjugate of conjugate, how do you write that? It is simply to take b

### 02:31:10 · Speaker 3

domain of the conjugate, okay?

### 02:31:14 · Speaker 3

and subtract it with

### 02:31:17 · Speaker 3

its conjugate which is subtract it with its value and

### 02:31:21 · Speaker 2

maximization is over. T which is domain of

### 02:31:25 · Speaker 2

Apsara

### 02:31:28 · Speaker 2

Do you agree?

### 02:31:31 · Speaker 3

simply taking conjugate of the conjugate. What is the conjugate of the conjugate? Conjugate is also convex. So this is the conjugate of conjugate. So this is

### 02:31:42 · Speaker 3

P conjugate

### 02:31:44 · Speaker 3

of conjugate

### 02:31:48 · Speaker 2

we know that that is equal to the original function x that's why f of

### 02:31:52 · Speaker 1

p is equal to maximum over this

### 02:31:57 · Speaker 1

questions on this, do you agree?

### 02:32:10 · Speaker 1

See I have just replaced f of u with f star

### 02:32:12 · Speaker 3

star of U because F star of U is another convex function, right? We can write conjugate for any convex function. F star is another convex function. So I will write a conjugate for F star as well, which is this. It is this and this we know that if you take the conjugate of conjugate, you get the original function.

### 02:32:30 · Speaker 1

This is clear to all of you?

### 02:32:43 · Speaker 1

Okay. Okay, so now okay,

### 02:32:46 · Speaker 3

What do we need this? Let's come back to our definition of our F divergence. Remember that we are looking at bounding this F divergence, okay?

### 02:32:56 · Speaker 1

Now this is integral

### 02:33:10 · Speaker 1

Right? This is

### 02:33:16 · Speaker 1

let me call this as f of

### 02:33:18 · Speaker 1

2dx okay

### 02:33:20 · Speaker 1

where you

### 02:33:22 · Speaker 1

Yes

### 02:33:25 · Speaker 1

sorry I think I wrote it incorrectly. It should be P theta.

### 02:33:38 · Speaker 1

Okay? Now if you use a convex function,

### 02:33:40 · Speaker 3

which means that this F now I can replace this let if I use this yeah

### 02:33:44 · Speaker 4

Sir, if I use this, yeah. Sir, either the initial one should have P X or the the last the last one should have P X because once we replace

### 02:33:59 · Speaker 2

follow.

### 02:34:05 · Speaker 2

theta x times f of

### 02:34:09 · Speaker 3

px by p theta right that's the definition

### 02:34:12 · Speaker 4

once we replace px by p theta with u

### 02:34:12 · Speaker 3

once we replace

### 02:34:15 · Speaker 3

we have it right?

### 02:34:18 · Speaker 3

Ha

### 02:34:20 · Speaker 4

So

### 02:34:21 · Speaker 3

just called it as this ratio I called as U that's all.

### 02:34:25 · Speaker 4

Okay

### 02:34:26 · Speaker 3

It's a scalar, no? I just called it as a scalar U F of U.

### 02:34:30 · Speaker 4

Okay, okay.

### 02:34:34 · Speaker 3

Nothing complicated, right? I just am representing that as some scalar, right?

### 02:34:38 · Speaker 4

Yes sir. Yes.

### 02:34:39 · Speaker 3

Now, f of u, we have this result, right? Can be written as max of

### 02:34:49 · Speaker 2

p u minus

### 02:34:52 · Speaker 2

star of the

### 02:34:56 · Speaker 2

maximization is over T, correct? This is what we have written here.

### 02:35:01 · Speaker 2

correct? I will use that there. Which means that my f divergence now can be written as the integral

### 02:35:11 · Speaker 2

times max of

### 02:35:15 · Speaker 2

T, okay? What? Okay, I'll write it as T U minus

### 02:35:21 · Speaker 2

f star of p

### 02:35:24 · Speaker 2

dx. Maximization is over t. Agreed?

### 02:35:32 · Speaker 2

What they do, I just simply replace f of u with

### 02:35:38 · Speaker 3

the definition, okay? by using the conjugate of conjugate property.

### 02:35:43 · Speaker 3

So if you agree

### 02:35:46 · Speaker 3

This is another problem with this online teaching that the screen is so small, right? I mean, I need a large board where, see, imagine I would have written this somewhere else, you know, you would have had the view of this, you know, you can appreciate that since I have written F of U using this maths thing, all I have done is I have replaced this F of U using this, yeah, using this definition.

### 02:36:09 · Speaker 3

Is it okay?

### 02:36:12 · Speaker 2

Yes sir

### 02:36:12 · Speaker 1

Yes sir

### 02:36:14 · Speaker 3

Now, I'll just

### 02:36:16 · Speaker 3

expand is this is integral

### 02:36:17 · Speaker 2

Hello

### 02:36:19 · Speaker 2

p theta of x

### 02:36:21 · Speaker 2

x over t

### 02:36:24 · Speaker 2

Now T times what is U? U is ratio of P X by

### 02:36:30 · Speaker 2

E theta

### 02:36:34 · Speaker 2

minus

### 02:36:36 · Speaker 1

star of T

### 02:36:40 · Speaker 1

Correct

### 02:36:43 · Speaker 1

Correct? Yeah. Now look at these terms. Look at these terms.

### 02:36:48 · Speaker 2

I'll write it as T times

### 02:36:53 · Speaker 2

he times this. Now look at this.

### 02:36:56 · Speaker 3

If I can somehow take this max out of the integral

### 02:37:02 · Speaker 3

Okay, if I take the max term out of the integral, what will happen?

### 02:37:08 · Speaker 3

Can somebody tell me what will happen?

### 02:37:11 · Speaker 3

If I take max, yeah, if I take max out of the integral, then it will be t times

### 02:37:11 · Speaker 2

Sweet

### 02:37:17 · Speaker 3

P X minus the integral of so it will be like this now. Somehow take the maths outside, okay? It will be integral

### 02:37:27 · Speaker 3

p theta p theta would cancel out

### 02:37:30 · Speaker 3

it will be

### 02:37:33 · Speaker 2

T times

### 02:37:35 · Speaker 1

x of x dx

### 02:37:38 · Speaker 1

Correct? Minus

### 02:37:42 · Speaker 1

Integral

### 02:37:47 · Speaker 1

star of t times

### 02:37:50 · Speaker 1

p theta of x. Correct? Do you agree?

### 02:37:56 · Speaker 1

Can you see that?

### 02:38:03 · Speaker 2

So can we take the max out

### 02:38:03 · Speaker 1

take the

### 02:38:04 · Speaker 5

October

### 02:38:05 · Speaker 3

Yeah, hold on. I'm just saying if you can, I mean, you can't, I will tell you what happens if you take the max out, but if you can, let's say, right? Then it will become like this. Now, this is an expectation, right? Over P X. And this is an expectation over P theta. You understand that? That's all. Now, all this exercise that we did, right? In representing the F function using its conjugate, all that was to ensure that we can somehow write the

### 02:38:35 · Speaker 3

express these in terms of expectations. Now we are almost there. We just have to somehow push this max out. And if we can push this max out, then we achieve whatever we want that we can write our f divergence in terms of differences in expectations over px and p theta which we know how to compute. Can you see the point?

### 02:38:57 · Speaker 3

Now the question is how can you take the maths out?

### 02:39:02 · Speaker 3

Right? So max is over T, how can you take the max out is the question. uh That needs, I need some half an hour to complete this proof now.

### 02:39:15 · Speaker 2

What shall we do?

### 02:39:18 · Speaker 2

He has

### 02:39:23 · Speaker 4

सर, वी हैव टाइम अल्टेट ट्वेल्व फिफ्टीन।

### 02:39:24 · Speaker 2

1250

### 02:39:26 · Speaker 2

15, 10

### 02:39:28 · Speaker 3

4 minutes

### 02:39:28 · Speaker 4

all right

### 02:39:28 · Speaker 4

Yes sir

### 02:39:30 · Speaker 3

ten minutes might be lesser to do this anyway I will quickly run through it and do it again in the next class perhaps

### 02:39:37 · Speaker 1

Okay

### 02:39:41 · Speaker 1

Any questions so far?

### 02:39:53 · Speaker 1

Does anyone have any question? Okay, no, okay. Now,

### 02:39:57 · Speaker 1

Okay, so let us observe this entire thing.

### 02:40:04 · Speaker 1

Okay. So this is a maximization

### 02:40:12 · Speaker 1

Right, over

### 02:40:15 · Speaker 1

P

### 02:40:18 · Speaker 1

Can you see that?

### 02:40:20 · Speaker 1

is the maximization over T. Okay? However, however,

### 02:40:28 · Speaker 2

Okay, so let us

### 02:40:30 · Speaker 3

all this uh maximization over okay maximization of let me say that of

### 02:40:40 · Speaker 3

an objective function, okay?

### 02:40:44 · Speaker 3

objective function let me call that function as capital T okay of a function T

### 02:40:52 · Speaker 3

Over T

### 02:40:54 · Speaker 3

Do you agree? So this I mean whatever I have marked using flower bracket right? It is a maximization that you are that you are that an optimization that you are solving over T as the variable.

### 02:41:10 · Speaker 3

And if I call that entire function that you are optimizing using capital T, okay? Then it's you are maximizing capital T over the variable small T. Do you agree?

### 02:41:25 · Speaker 3

or I can use a different notation for this capital T, you know, because I'm using small d capital, it might confuse which letter

### 02:41:40 · Speaker 2

run out of alphabets

### 02:41:45 · Speaker 2

U is taken P

### 02:41:51 · Speaker 1

Okay

### 02:41:51 · Speaker 2

quality V

### 02:41:55 · Speaker 2

capital V. This function capital V, okay? We want to optimize, okay, what is V by the way?

### 02:42:06 · Speaker 2

V is equal to T times

### 02:42:11 · Speaker 3

x of x divided by h h h of x minus f star of t. Correct? This is what I have called as v. Agreed? It's a maximization of an objective function v over t. All of you see that. But observe this that this v is actually a function of x as well.

### 02:42:39 · Speaker 2

But I should say that it's a function of both x and t

### 02:42:45 · Speaker 3

It's a function of x and t. It's also a function of x. Agreed?

### 02:42:48 · Speaker 1

Okay

### 02:42:51 · Speaker 3

Now what you are actually doing while you are computing this integral is the following. You first solve this optimization problem over T, okay? So now what you do is inner

### 02:43:05 · Speaker 3

optimization problem. So now first you do solve this optimization problem you get a you get a let's say

### 02:43:14 · Speaker 3

T star okay which is the maximum

### 02:43:20 · Speaker 3

of this function v x, t over all t

### 02:43:25 · Speaker 3

Okay. Now you plug this t star here and compute this integral. And do it for all x. That is what you are doing when you are computing the integral.

### 02:43:40 · Speaker 3

You first solve the optimization problem with respect to T, you get some some uh value for that optimization problem. Now you take that, so now observe that this T star, okay?

### 02:43:56 · Speaker 3

is also a function of x.

### 02:44:02 · Speaker 3

Do you agree?

### 02:44:05 · Speaker 3

obviously, right? Because if v is a function of x, then t star is also a function of x. Because we are only solving, we are only taking the maximum with respect to t, and given a particular x, you will have a different maximum. Correct?

### 02:44:21 · Speaker 2

Let us represent that maximum using some capital T star of X.

### 02:44:28 · Speaker 3

Correct? Okay. Now what are we saying here? That there is an optimization problem, there is an optimization that is happening with respect to T, okay? Now that objective function for that optimization problem is a function of X.

### 02:44:44 · Speaker 3

Now, given an x, you will have a particular maximum for this maximization problem. You compute that maximum and then you integrate for all x. That is what your f divergence is.

### 02:44:54 · Speaker 2

agreed

### 02:44:59 · Speaker 2

Now

### 02:45:00 · Speaker 3

Hello

### 02:45:00 · Speaker 2

Hello

### 02:45:00 · Speaker 3

Now, what I can do is, suppose I take the maximization out, okay?

### 02:45:07 · Speaker 2

Hello

### 02:45:08 · Speaker 2

and write that whatever is there you know v theta of x

### 02:45:14 · Speaker 2

and

### 02:45:18 · Speaker 1

Hmm

### 02:45:19 · Speaker 2

in

### 02:45:20 · Speaker 1

theta of x divided by x of x minus

### 02:45:25 · Speaker 1

a star of t

### 02:45:41 · Speaker 1

suppose, right? I take this

### 02:45:48 · Speaker 1

replace this with

### 02:45:52 · Speaker 1

p star of x

### 02:46:02 · Speaker 1

Which is the maximum of

### 02:46:06 · Speaker 2

So that

### 02:46:06 · Speaker 6

wait

### 02:46:06 · Speaker 3

okay

### 02:46:07 · Speaker 6

px by p theta right t star of x into px by p theta

### 02:46:12 · Speaker 3

is it P X? I must make this mistake. Yeah, it's P X by P theta. Sorry.

### 02:46:18 · Speaker 3

correct. Now, suppose I replace this, you know, this this this T, right? I solve this optimization problem and replace it with T star of X, then it's okay, no? Both the integrals are okay. I can take out the max. Do you agree? Because I'm solving the optimization problem anyway, right? At all points in X, I'm taking out, I'm finding, solving that optimization problem and

### 02:46:43 · Speaker 3

replacing that t with t star of x, correct?

### 02:46:46 · Speaker 1

Hello

### 02:46:46 · Speaker 2

That's okay, no?

### 02:46:55 · Speaker 2

Do you agree? What I am doing it at all is I am simply

### 02:46:59 · Speaker 3

solving the dinner optimization problem and putting the solution for it and then computing the integral.

### 02:47:05 · Speaker 3

Right

### 02:47:07 · Speaker 3

Now

### 02:47:09 · Speaker 3

this t star of x basically let's say that okay it's a function that would take a particular value of x and gives you what a real number isn't it a real number which happens to be the solution solution

### 02:47:26 · Speaker 3

for the optimal

### 02:47:29 · Speaker 1

problem

### 02:47:33 · Speaker 1

inner optimization problem.

### 02:47:46 · Speaker 1

Right? What should be this T star of X B?

### 02:47:48 · Speaker 3

p star of x is a function that would take x, you give it an x, it will give the solution for the inner optimization problem, correct?

### 02:47:58 · Speaker 3

Do you agree?

### 02:48:00 · Speaker 3

this t star of x has to be this right? Look at this by definition. It should be a function that would take an x and gives you the solution for the optimization problem.

### 02:48:12 · Speaker 3

Okay

### 02:48:12 · Speaker 2

Number

### 02:48:13 · Speaker 1

Now

### 02:48:20 · Speaker 1

Any questions so far?

### 02:48:34 · Speaker 1

Okay. Now, instead of T star, okay, instead of T star,

### 02:48:44 · Speaker 2

Okay, before that, let

### 02:48:48 · Speaker 2

let, okay? let script t

### 02:48:55 · Speaker 2

This is a different symbol, okay?

### 02:48:57 · Speaker 1

Denote, Denote.

### 02:48:59 · Speaker 1

a class of functions.

### 02:49:07 · Speaker 1

class of functions, okay?

### 02:49:11 · Speaker 1

from

### 02:49:13 · Speaker 3

X to R. So basically what I'm saying is let capital let script T, this is this script T, okay? Let script T denote a class of functions from X to R. Okay? Which means that this T star of X, T star of X is a member of capital T, okay?

### 02:49:33 · Speaker 3

p star of x is one member of capital T which means that it is a function that would take x and gives you a real number which is a solution for the inner optimization problem at all x. Okay? But script T let script T denote all possible functions that would take an x and gives you a real number. Okay? Now

### 02:49:52 · Speaker 3

If I cannot

### 02:49:57 · Speaker 2

Let me write that integral down and then I will tell you this.

### 02:50:03 · Speaker 1

t of x minus

### 02:50:10 · Speaker 1

is T. What is that? P theta.

### 02:50:13 · Speaker 1

પછી સેકન્ડ ટર્મ

### 02:50:17 · Speaker 2

heat of x times

### 02:50:21 · Speaker 2

t of x times

### 02:50:25 · Speaker 2

p theta of x by x of x minus f of f star of f star of t of x.

### 02:50:38 · Speaker 4

सर, पीएक्स ऑफ एक्स डिवाइडेड बाय पी थीटा ऑफ एक्स।

### 02:50:38 · Speaker 2

Sir

### 02:50:44 · Speaker 2

Every time I make that mistake.

### 02:50:50 · Speaker 2

Okay. Now, let's say that let there is a

### 02:50:56 · Speaker 3

x okay which is not equal to t star of x okay

### 02:51:03 · Speaker 3

I replace this with this. So this suppose, suppose.

### 02:51:09 · Speaker 3

P X is another function, okay?

### 02:51:14 · Speaker 3

that belongs to script T and I replace this T star of X by T of X. What do you think, okay?

### 02:51:23 · Speaker 3

will be the value of this integral compared to

### 02:51:28 · Speaker 3

disintegral. And somebody tell me

### 02:51:32 · Speaker 3

You understand? Instead of having T star of X which gives me solution for the inner optimization at all points of X, if I replace that with another function T of X, what would that be?

### 02:51:47 · Speaker 3

it'll be smaller than the previous one.

### 02:51:50 · Speaker 2

it will be smaller. Do you agree?

### 02:51:54 · Speaker 2

it will be this will be this will be greater than or equal to. Correct?

### 02:51:55 · Speaker 3

This is

### 02:52:03 · Speaker 2

So this is our

### 02:52:04 · Speaker 1

Hello

### 02:52:05 · Speaker 1

F divergence is will always be greater than or equal to F divergence. Correct?

### 02:52:13 · Speaker 1

Because

### 02:52:19 · Speaker 1

it will be either equal to T

### 02:52:20 · Speaker 3

f x are less than t of x. They are not equal to t of x.

### 02:52:23 · Speaker 4

सर, अदर वे राउंड, राइट? वी लाइक, टी स्टार इस करेस्पोंडिंग टू द मैक्सिमम वैल्यू।

### 02:52:29 · Speaker 3

max. P star is corresponding to the max. So this is lesser and all the everything here all of these are density functions that are positive. So T is T is lesser. T can be lesser at all points. It means that yeah, it's the other way around should be, you know.

### 02:52:46 · Speaker 3

which is that this is greater, correct? It's a lower bound, no? Correct? Is that okay?

### 02:52:54 · Speaker 4

Yes sir

### 02:52:54 · Speaker 3

Correct no this integral is over x. Now now I can say that d f is greater than or equal to the maximum value okay that you can get.

### 02:53:10 · Speaker 3

Out of all

### 02:53:11 · Speaker 1

that belongs to this class of functions of this particular integral

### 02:53:27 · Speaker 1

minus

### 02:53:30 · Speaker 1

this is p x no because p theta would cancel out.

### 02:53:36 · Speaker 1

Integral

### 02:53:40 · Speaker 1

p theta x

### 02:53:43 · Speaker 1

T X, V X,

### 02:53:45 · Speaker 3

That's

### 02:53:48 · Speaker 3

Is this a do you agree? Why why am I written a max here? The reason I'm I've written a max here is that if you take the max of all possible functions

### 02:53:59 · Speaker 3

in this bucket of functions, okay? Your f divergence will be greater than or equal to that. Now, if you can find a function with the bucket of all these functions that is equal to t star of x at all points, then it is exact. The f divergence will be exactly equal to this integral in the right. Okay? Now if you cannot find a function, okay, that is equal to t star of x at all point, at least find a function, okay, that will give you the maximum value at all

### 02:54:29 · Speaker 3

possible x amongst see there can be let's say that there is one t of x there is another t two of x there is t three of x and all that right let's say that none of these are equal to t star of x

### 02:54:40 · Speaker 3

okay? However, I would choose that T, okay, amongst T one, T two, three, T three. Okay? That is maximum of all this, correct? Of course, I need to choose the maximum because here the inner optimization problem, I am actually looking at, see look at the definition of T star, no? It is actually the maximum of this objective function with respect to T. Now, if I cannot find the maximum

### 02:55:05 · Speaker 3

But

### 02:55:07 · Speaker 3

at all points

### 02:55:10 · Speaker 3

Or rather, if I cannot find a function that will give you the maximum at all points, I would choose the function amongst all possible functions that are there in this bucket of P, I would choose the one with the

### 02:55:19 · Speaker 2

Fancy Mangali

### 02:55:22 · Speaker 2

Do you agree?

### 02:55:29 · Speaker 2

petrol

### 02:55:29 · Speaker 3

we are done. I mean I will reiterate over this the next class. So what we basically did was we expressed this expectation, okay sorry the F divergence. We carved a lower bound on this. It's saying that you

### 02:55:44 · Speaker 3

Choose a class of functions, okay? From a bucket of functions, this is equal to, what is this first term? It's pretty obvious now. This is an expectation of T of X with respect to P X. Right? Minus, this is an expectation of, sorry. This should be

### 02:56:04 · Speaker 1

nobody corrected me this is s star of t of x dx

### 02:56:18 · Speaker 1

Let me call this x cap because

### 02:56:20 · Speaker 3

when you write expectations, no, it's better to write a different dummy variable. This is x coming from px. This is the expectation of x cap coming from p theta.

### 02:56:32 · Speaker 3

That's all. This is the result. This is the last function in a Gyan. If you can, if people know, if you can relate, no, this is exactly the last function in a Gyan. I will, we will see that, you know, in detail next class. That's all. We are done. So now, we have expressed, so basically what we have done, we have have expressed.

### 02:56:53 · Speaker 1

Expressed

### 02:56:56 · Speaker 1

the lower bound on F A versions

### 02:57:02 · Speaker 1

on f divergence in terms of

### 02:57:08 · Speaker 1

expectations

### 02:57:13 · Speaker 1

or unknown distributions.

### 02:57:24 · Speaker 1

This is the goal, right? We have achieved our goal.

### 02:57:26 · Speaker 3

Now, we know how to compute, do we know how to compute the first term? We do log large numbers because we have samples from P. Do we know how to compute the second term? We do because we have samples from P theta. Now if you observe, this entire thing now will become a function of theta.

### 02:57:41 · Speaker 3

right? Because this second expectation is a function of theta. Now you don't forget what we have been doing, no? We have this network. G theta whose parameters are theta, we are giving a random G. Okay? This X cap, the output of this is called as P theta and we have lot of samples from P theta and that's what we use to compute the second expectation. We use our data to compute the first expectation and then we optimize this using region descent. Which we will see in the

### 02:58:11 · Speaker 3

next class. But for today's class, what did we do? We wanted to minimize the f divergence. We could not because we don't know the underlying distributions. The goal was to represent the unknown divergence or uncomputable divergence measure in terms of expectations over underlying distributions because we know how to compute expectations using law of large numbers. We invoke the property of convexity and conjugates to express the the f divergence in terms of expectations over underlying distributions.

### 02:58:48 · Speaker 3

That's all we did so far. Okay? So before coming to the next class, as I said, no, the things are getting more intense and involved. Please go through this this content, right? I mean, whatever we did in today's class. Go through that once. And if you have questions, you can ask me or TAS either on the WhatsApp group or on Teams. And you also look at the notes that I've given, no, the handwritten notes. uh This time I've kind of swapped swapped the order I used to

### 02:59:18 · Speaker 3

teach A is first and Gyan's then now I've swapped the order this we started from the Gyan so it is the you know lecture four in my notes. lecture four in the handwritten notes.

### 02:59:34 · Speaker 3

shared that with you. Please have a look at it and also read the paper. The paper that I am following is that

### 02:59:42 · Speaker 3

irrational divergence minimizing, let me just tell you the name of the paper. It is there in my handwritten notes.

### 02:59:51 · Speaker 3

is called F Gyan, okay, which is a generalization of all Gyan. So it is called

### 02:59:56 · Speaker 3

F Gyan

### 02:59:59 · Speaker 3

Training

### 03:00:02 · Speaker 1

generative neural samplers

### 03:00:06 · Speaker 1

title of the paper okay.

### 03:00:12 · Speaker 1

Using

### 03:00:14 · Speaker 1

Variational Divergence Minimization

### 03:00:23 · Speaker 1

This is the

### 03:00:23 · Speaker 3

paper that I am going through, okay? Meaning this is what I have like I have of course created my own narrative but this is the paper. So it is there in my handwritten notes. Please go through the handwritten notes once and also go through whatever has been covered in this in this class and come prepared please. If you have questions of course you can ask me but no do prepare and come back. It will be Yeah, we will continue from here. I'll I'll redo whatever I did. this time, okay? So, this I will redo, but yeah, have a look at it and come prepared. Okay?

### 03:01:04 · Speaker 3

That's all for today then. Yeah. So for people who are celebrating Happy Ganesh Chaturthi. So we will reconvene next class, next uh

### 03:01:14 · Speaker 2

So just one question. um For this theory that you covered, any reference material that we can refer to?

### 03:01:16 · Speaker 3

you know

### 03:01:20 · Speaker 3

I gave you, no, that's exactly what I do.

### 03:01:21 · Speaker 2

no no no I mean especially on this convex optimizations and such stuff if you have anything handy

### 03:01:28 · Speaker 3

convex optimization is a standard stuff even Wikipedia says that meaning the convex conjugate and the convex functions.

### 03:01:37 · Speaker 2

Okay

### 03:01:38 · Speaker 3

Yeah, any convex optimization book would do, but you don't need I mean we are not doing convex optimization here, right? Beyond just defining the conjugates, we are not doing anything. So that I think, you know, standard articles in Wikipedia would suffice.

### 03:01:53 · Speaker 2

Okay. And the uh the paper that you referred I think that that would be for reference.

### 03:01:58 · Speaker 3

for reference. And my I have I have given you some references in my handwritten notes. You know, please have a look at it. For instance, right? I mean, differential conjugates and the related stuff, you know, I have put in some of the references at the end of my handwritten notes. Start reading them.

### 03:02:15 · Speaker 2

Sure

### 03:02:17 · Speaker 3

Okay

### 03:02:18 · Speaker 3

Okay. Anything else?

### 03:02:21 · Speaker 2

just one other question sir so this quiz will be on moodle or

### 03:02:26 · Speaker 3

No no no we will do it on this thing Microsoft Forms. Okay we will not use Moodles.

### 03:02:34 · Speaker 3

we will let you know okay again you know we will intimate that in teams and WhatsApp.

### 03:02:40 · Speaker 1

Sure sir

### 03:02:42 · Speaker 3

Okay, thank you then. We will See, also let me know if you think that you know that I mean classes too intense or you want some other change etcetera. You have that anonymous feedback form that is there in on my web page. You can express your thoughts.

### 03:02:58 · Speaker 3

When you are writing please uh mention that you like you are from the online version of the course that's all so that I know in where to implement the change. Of course it's anonymous you don't have to put your name or anything but just mention that this is from the online student and you can just put in your thoughts if you have if you need any change in the way things are going okay.

### 03:03:22 · Speaker 3

Okay, see you next week. Bye bye.

### 03:03:25 · Speaker 2

Thank you sir. Bye.

### 03:03:26 · Speaker 1

Thank you, Surya

### 03:03:26 · Speaker 3

Thank you

### 03:03:27 · Speaker 3

Okay

### 03:03:27 · Speaker 2

Thank you sir

### 03:03:28 · Speaker 1

Yeah, thank you, sir.

### 03:03:31 · Speaker 2

Thank you sir

### 03:03:35 · Speaker 1

Thank you sir. Thank you sir.
