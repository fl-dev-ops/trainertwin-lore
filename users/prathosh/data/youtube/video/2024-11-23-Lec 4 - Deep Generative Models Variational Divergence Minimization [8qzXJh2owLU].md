---
id: 8qzXJh2owLU
title: Lec 4 - Deep Generative Models Variational Divergence Minimization
url: https://www.youtube.com/watch?v=8qzXJh2owLU
date: '2024-11-23'
duration: 03:03:52
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# Lec 4 - Deep Generative Models Variational Divergence Minimization

## Transcript

### 00:00:03 · Speaker 1

Okay, there will be 15 questions, 15 to 20 questions and we'll give you 20, 25 minutes to solve it. Okay, multi-choice questions. The first quiz will happen next week. Is that okay?

### 00:00:17 · Speaker 2

Is it possible sir if you can share some sample questions

### 00:00:23 · Speaker 1

Well, it's it simply can, but it's when there are factual questions on things that has been covered so far in the class. So if you brush up whatever has been covered in the class, that should be enough.

### 00:00:43 · Speaker 1

Okay let us start now today's class

### 00:00:45 · Speaker 3

Sorry for interrupting, just one question. So you said next Sunday is next Sunday or Saturday?

### 00:00:50 · Speaker 1

I mean yeah my bad yeah next Saturday next week

### 00:01:01 · Speaker 4

Um so one more question I have. So uh whatever we cover in today's class is also gonna be included

### 00:01:09 · Speaker 1

Boss

### 00:01:10 · Speaker 4

Okay, and sir, I remember we have already discussed this in length, but on the first class, there was a lot of back and forth between what was our final decided grading policy. If you can just summarize it quickly, once again, for the sake of clarity, it will be really hard.

### 00:01:25 · Speaker 1

It will be done that no please don't do this we have done this no there is it is documented it is written look at this

### 00:01:34 · Speaker 1

So yes of course I voted and said that this is funny and we are not going to disclose it anymore please don't do this

### 00:01:34 · Speaker 4

Of course

### 00:01:43 · Speaker 1

Okay so it is there it is written let's have a look at it

### 00:01:48 · Speaker 1

I see another hand raised Dermot let's go on

### 00:01:52 · Speaker 4

Uh yeah so uh so for the quiz will there be

### 00:01:58 · Speaker 4

So will there be calculation for this or only as you said factual?

### 00:02:08 · Speaker 4

Uh am I audible

### 00:02:10 · Speaker 1

Brush up whatever's uh

### 00:02:16 · Speaker 3

So the audio is not very clear

### 00:02:19 · Speaker 2

Yes sir we are uh you are breaking

### 00:02:23 · Speaker 1

Hello is this it okay I think I should do some problem with my internet today just a minute give me a minute

### 00:02:37 · Speaker 1

Hello am I audible

### 00:02:39 · Speaker 3

Yes sir now you are

### 00:02:43 · Speaker 1

internet explores yeah i said it is just here it's about testing what you have understood

### 00:02:53 · Speaker 1

From whatever has been taught, okay? It will mostly be factual with.

### 00:03:00 · Speaker 1

Three four options for each question and there will be 15 questions in 20 minutes okay and it's what's

### 00:03:14 · Speaker 1

Okay, let us start then. Hope that you see my screen. And last class, just a quick recap.

### 00:03:34 · Speaker 1

yeah in last class we defined what generative modeling is uh that we are given data from an unknown distribution okay what we wanted to do is to estimate the unknown distribution and also sample from it okay that was the problem that we wanted to solve

### 00:03:55 · Speaker 1

Okay, so we wanted to do it from the perspective or angle of what I call it as divergence memorization.

### 00:04:06 · Speaker 1

where the idea was to assume a parametric form for the density function to be estimated denoted by p theta right where theta are the set of parameters that are representing the underlying distribution okay so we have p theta that represents the distribution uh that we are modeling and we call this the model distribution and it can be any parametric distribution

### 00:04:36 · Speaker 1

as a Gaussian distribution or even a neural network okay uh that would take um some random variable as input and the output of that neural network is the distribution of the output of the neural network is taken to be p theta

### 00:04:53 · Speaker 1

Then we said okay once you have the speed parametric model you define okay I think there's a typo here

### 00:05:31 · Speaker 1

It's just not the wall

### 00:05:36 · Speaker 1

Somebody tell me what's wrong

### 00:05:39 · Speaker 1

I'm not seeing any of these outcomes

### 00:05:47 · Speaker 4

Are you not able to scroll

### 00:05:50 · Speaker 1

I'm able to scroll yeah I'm actually not able to scroll on so now

### 00:05:57 · Speaker 1

And now we can scroll

### 00:06:01 · Speaker 1

There was a typo here define and compute

### 00:06:08 · Speaker 1

Define and compute a distance or divergence metric between the true distribution and the assumed parametric density function, true density function and parametric density function, okay? That will tell you how close or far px and p theta are, where px is the true distribution and p theta is the distribution of interest, okay? And then you adjust or compute the parameters of p theta such that this divergence minimizes, divergence metric is minimized, okay?

### 00:06:38 · Speaker 1

Computing the parameters of p theta such that this is minimized is what is called as training or learning of the model. Mathematically, it is solving an optimization problem over the space of the parameters of the density that we have assumed. So, the final estimate of p x is p theta star where theta star is the set of parameters that we have obtained by solving the above optimization problem.

### 00:07:08 · Speaker 1

That is what we saw. And also we quickly saw one definition, one of the possible definition for the divergence metric, which we call the Kullback-Leibler divergence or KL divergence. Okay. Okay, so I want you to, I'll stop here for a minute and I want you to let me know if you have any questions on this general philosophy of divergence minimization because

### 00:07:38 · Speaker 1

That will be the central theme of most of the models that we'll be seeing in this course. We start with a parametric form for the density that we want to estimate and we define a divergence metric. Now that divergence metric becomes a function of the parameters of the underlying density. Then we compute the or rather we get the parameters of the density by minimizing the divergence

### 00:08:08 · Speaker 1

metric between the true density and the parametric density so that is the idea any questions on this

### 00:08:16 · Speaker 1

Follow me more

### 00:08:55 · Speaker 1

Am I audible? Hello

### 00:09:00 · Speaker 1

Okay no questions Okay great let us uh move on then

### 00:09:12 · Speaker 1

Now we will look at the first class of family of generative models that we will see. We are called adversarial generating models are also called as generative adversarial networks of GANs. Now what is the idea there? So same thing, right? So what we will do is we will

### 00:09:40 · Speaker 1

Even

### 00:09:45 · Speaker 1

Data okay so what is data data are

### 00:09:50 · Speaker 1

some samples

### 00:09:58 · Speaker 1

Drawn from

### 00:10:00 · Speaker 1

unknown distribution

### 00:10:06 · Speaker 1

What can these be These are examples of

### 00:10:15 · Speaker 1

Only just of digits or

### 00:10:20 · Speaker 1

is what is there in MNIST dataset

### 00:10:25 · Speaker 1

It can be

### 00:10:32 · Speaker 1

some features of text and so on it can be anything we are given n data points of n data points drawn from unknown distribution okay goal

### 00:10:49 · Speaker 1

Owl is too

### 00:10:56 · Speaker 1

estimate px and remember we are solving kinetic modeling here and

### 00:11:02 · Speaker 1

from VX

### 00:11:09 · Speaker 1

Now what do you mean by sampling from PX is that generate

### 00:11:20 · Speaker 1

Four samples from PX

### 00:11:28 · Speaker 1

Okay that

### 00:11:32 · Speaker 1

Right

### 00:11:35 · Speaker 1

Not in D

### 00:11:38 · Speaker 1

given data set but you want to generate more samples from the data set okay that are not a part of the data set okay that is uh that is what we want by that is what we need call by sampling okay okay now what is the idea so first first step to do this is that zoom

### 00:12:05 · Speaker 1

a parametric form

### 00:12:17 · Speaker 1

call it P theta

### 00:12:25 · Speaker 1

Okay, this is what we start from. Now, in the class of generative models known as adversarial network, how do we get p theta? So in

### 00:12:52 · Speaker 1

The P theta is represented by a neural network

### 00:13:05 · Speaker 1

I think you're on the hook

### 00:13:16 · Speaker 1

Okay it means that there is a neural network

### 00:13:25 · Speaker 1

Whenever I write neural networks right in this course from now on I will be assuming

### 00:13:36 · Speaker 1

I'll be following this convention that I will write these kinds of quadrilaterals, right, trapeziums, and the shape will be proportional to the dimensionality of the data. Why am I? I can't write a straight line.

### 00:13:56 · Speaker 1

Better okay

### 00:14:00 · Speaker 1

Now what is happening here is that, okay, so let me, before I move on, I am assuming that all of you know how the error back propagation algorithm works, right? How to train neural networks. Is there anybody who does not know how to perform gradient descent on neural networks?

### 00:14:27 · Speaker 1

And then I will just make it a do we do we need yeah Nirmal you raised your hand

### 00:14:34 · Speaker 3

I mean I don't know uh but if we can have tutorial on that that would be good

### 00:14:41 · Speaker 1

I can but that's why I'm asking right do we need a tutorial on backpropagation algorithms

### 00:14:48 · Speaker 3

I mean I c yeah

### 00:14:52 · Speaker 1

Okay tactics

### 00:14:56 · Speaker 3

Yes

### 00:14:56 · Speaker 1

So we'll see

### 00:14:58 · Speaker 3

Yeah it was just

### 00:15:00 · Speaker 1

You haven't tried neural networks before is it

### 00:15:08 · Speaker 4

So, sir, we're uh we're broadly aware of how it like what it's supposed to do but not with the same level of mathematical rigor that this course is uh going on with.

### 00:15:22 · Speaker 1

Okay so let us make that a

### 00:15:25 · Speaker 1

an item of tutorial then we will

### 00:15:29 · Speaker 1

that will teach operational okay so

### 00:15:35 · Speaker 1

it is mostly uh repeated application of chain rule okay uh that is that is that is what it is okay but yeah i will ask them to our tutorial on black box okay uh that apart um so i said now p theta will be represented using neural networks okay so now let us call this as some g theta of g okay now let's say that you have g

### 00:16:05 · Speaker 1

which is a random variable that is that has a Gaussian distribution associated with it okay

### 00:16:13 · Speaker 1

Now typically

### 00:16:16 · Speaker 1

Okay, I didn't come to that anyway. Now we have this proposition that suppose

### 00:16:26 · Speaker 1

Z is a random variable which

### 00:16:31 · Speaker 1

distribution

### 00:16:40 · Speaker 1

and G theta of G

### 00:16:45 · Speaker 1

your function

### 00:16:49 · Speaker 1

a function that would

### 00:16:56 · Speaker 1

map G okay to some other space X cap

### 00:17:11 · Speaker 1

Okay now this result says that

### 00:17:21 · Speaker 1

Z cap

### 00:17:23 · Speaker 1

Cheers

### 00:17:26 · Speaker 1

Another random variable

### 00:17:32 · Speaker 1

the distribution

### 00:17:40 · Speaker 1

the distribution

### 00:17:43 · Speaker 1

Governor White

### 00:17:47 · Speaker 1

The function g to the power

### 00:17:57 · Speaker 1

Does it make sense? Do you understand what I'm saying? Suppose this is a standard result which you will be studying or have studied in random processes that if you have a random variable, okay, and if you have a function that acts on a random variable, then the distribution of the output of that function, okay, first of all, the output of that function is another random variable and the distribution of that particular output or function depends upon the functional form of g.

### 00:18:27 · Speaker 1

What do I mean by that examples

### 00:18:30 · Speaker 1

If

### 00:18:32 · Speaker 1

g is let's say uniform random variable between 0 and 1 okay and some g theta of x is equal to let's say

### 00:18:44 · Speaker 1

g squared okay then g squared

### 00:19:22 · Speaker 1

Can you see my screen

### 00:19:37 · Speaker 2

So if you're writing something then I don't think we are able to see

### 00:19:43 · Speaker 1

Oh is it? I think it is stuck

### 00:20:02 · Speaker 1

Okay I think yeah z squared will not be in the song

### 00:20:11 · Speaker 1

Do you see my writing now

### 00:20:15 · Speaker 4

Yes sir

### 00:20:16 · Speaker 3

Yes uh

### 00:20:17 · Speaker 1

Okay, right. Yeah, this is what it is, right? I mean, if you have, let's say, uniform random variable and you take the square root of it, it will not be uniform. It will have some other distribution than uniform distribution. Do you all get this idea? So basically what I'm saying is that you take a random variable that has a particular distribution, okay? And then if you pass that through a deterministic function, the output random variable will have a different distribution compared

### 00:20:47 · Speaker 1

to the input random variable is this idea clear and the distribution of the output random variable depends on what sort of function uh you are passing the input random variable through is this is this clear

### 00:21:08 · Speaker 1

Now why is this important? Let us look at this. The way we are modeling V theta is via this function V theta of z. Okay. Now this G theta of z

### 00:21:22 · Speaker 1

Let us let me write that again

### 00:21:26 · Speaker 1

g theta of g in our case

### 00:21:32 · Speaker 1

G theta of G is a neural network

### 00:21:44 · Speaker 1

Okay just for the sake of completeness I will define what a neural network is now

### 00:21:51 · Speaker 1

Let's say that Z is in some Rk dimensional space and we are talking of vector valued random variables here, okay? So what happens is that in this case, right, I mean Z is a vector valued random variable with Gaussian distribution. If Z is in Rk, then G theta of Z is defined like this. So what you first do is that you take

### 00:22:18 · Speaker 1

some weight vector w1 okay and multiply that with z so what will you get i will write the dimensions also

### 00:22:28 · Speaker 1

Okay let's say that W one is a matrix which is in

### 00:22:35 · Speaker 1

Z is in R K right uh so this is um

### 00:22:47 · Speaker 1

L1 cross K. So you have a matrix of L1 cross K. So now when you multiply

### 00:22:55 · Speaker 1

W one with G what will you get you will get a

### 00:23:01 · Speaker 1

are L one dimensional vector. Can all of you see that?

### 00:23:11 · Speaker 1

because z is actually in k cross 1 right it's a column vector of k dimensions which means that you have 1 2

### 00:23:27 · Speaker 1

K rows and one column and W1 has L1 rows and K columns. When you multiply that, you will get a L1 cross one dimensional vector. Can all of you see this? Is it okay?

### 00:23:44 · Speaker 1

Okay so then what you do is this is a linear transformation then you

### 00:23:49 · Speaker 1

an element-wise non-linearity where what happens is that when you do this w1 transpose z so what is happening is every element of this w1 transpose z so this of a vector z is simply you take the elements of z so z is actually 1 by 1 plus

### 00:24:17 · Speaker 1

Let me make it a scalar

### 00:24:27 · Speaker 1

This is the definition of the sweet mode

### 00:24:37 · Speaker 1

Okay, so now what you do is that when you write sigma of w1z, w1z is an L1 dimensional vector, you take every element of it and do this operation 1 by 1 plus e power minus z, then you still get an L1 dimensional vector that is what I call by sigma w1z. Is that okay?

### 00:25:02 · Speaker 1

Okay, so then what happens is that you take another set of parameters, call them w2 and multiply sigma w1z with that w2. Now this w2

### 00:25:20 · Speaker 1

of dimensions

### 00:25:25 · Speaker 1

L2 cross L1 okay which implies that W2 times sigma of W1 z okay will lie in R L2 cross 1 dimensions is that okay

### 00:25:52 · Speaker 1

Okay so then what you do is

### 00:25:59 · Speaker 1

is further okay then you have another non-linearity here

### 00:26:10 · Speaker 1

Okay then you take another W three here and now W three is

### 00:26:17 · Speaker 1

This is L3 cross L1 and you can have another non-linearity. You'll have W4 and so on. So what is this? This function is actually a four layer neural network.

### 00:26:36 · Speaker 1

Is this okay? So this is what a deep neural network is. I have just written that in a vectorized form that there are functions, right? I mean, there are linear transformations which are of type W1Z, okay? And then there is a nonlinearity given by a sigma. So there is a linear transformation followed by a nonlinearity. That is what a deep neural network is.

### 00:27:05 · Speaker 1

I hope this is clear to all of you

### 00:27:08 · Speaker 1

I see some questions here yeah

### 00:27:12 · Speaker 4

Ah yes sir I mean you just mentioned W four so there is no sigma applied to W four or

### 00:27:17 · Speaker 1

Ah you can I mean that depends no I mean if final layer is linear in the k in the network that I have written you can put a hit one here

### 00:27:29 · Speaker 3

Okay thanks

### 00:27:30 · Speaker 1

Yeah, I mean that depends. That's a design choice. Now, now if this is G theta, what is theta? Theta has all the set of parameters, you know, W1, W2, W3, and W4. This is what I am calling from, calling by G theta.

### 00:27:52 · Speaker 1

that all right okay so I'm going to try this again so now training a neural network will be finding out these w1 w2 w3 w4 through solving an optimization problem and what problem do we solve in the case of generative models are we is this is something that we will see now and how do we solve it is through error back propagation okay maybe I'll just mention it quickly when we formulate the optimization problem but anyway so now do you understand this now when I write this

### 00:28:22 · Speaker 1

diagram

### 00:28:24 · Speaker 1

Bug

### 00:28:26 · Speaker 1

is a neural network that takes z which has a Gaussian distribution okay and there is this function g theta of of z and you are getting an x cap okay typically z is in some r k dimensional space and x cap is in r d dimensional space which is same as the dimensionality of your x because we are trying to model uh distribution of

### 00:28:56 · Speaker 1

typically what happens is the dimensionality d will be much higher than that of k which means that you will have to adjust this l1 l2 l3 l4 okay such that the final uh output layer will have a dimensionality that is much higher uh than uh the input dimensionality and note that it need not be a four layer neural network for instance right if you take resonance 50 there will be these 50 w

### 00:29:26 · Speaker 1

use okay 50 layers it's a deep neural network that I've just given you an example of a four layer neural network it can be any layer and these nonlinearities need not be of this form uh it can be of this form only so right I mean with this

### 00:29:42 · Speaker 1

one if z is greater than zero or zero otherwise this is called the ReLU activation

### 00:29:54 · Speaker 1

And this is called the

### 00:29:56 · Speaker 1

and so on right doesn't matter but in general it is a deep neural network I mean for as far as our course is concerned we don't care what the form of these things are they are hyper parameters and design choices okay so now what we are interested in is that you start with a random variable which has a Gaussian distribution in k dimensions there is a deterministic function d theta which is a neural network that would that would transform it to another dimensional space called that x theta x cap

### 00:30:26 · Speaker 1

And this has the distribution V theta. This is our setting.

### 00:30:34 · Speaker 1

Okay, we'll take questions here. Um, Abeeru?

### 00:30:40 · Speaker 3

Yeah, so the in theta is the you are considering theta as the set of parameters. So in that set of parameters, since Z itself is a random variable following normal distribution, so those parameters, the mu and sigma, they will not be considered in theta.

### 00:30:55 · Speaker 1

No, no, no, that's fixed, no? Z is from normal 0i, 0, 1. So that is fixed.

### 00:31:01 · Speaker 3

Okay okay

### 00:31:02 · Speaker 1

Z is not the Z does not have any parameter no it's the input random variable

### 00:31:08 · Speaker 1

typically what happens no we assume that we know how to sample from z we can we know right because if you have i mean there are these functions called rand n and random number generators in all these uh like programming languages right what do they do they actually sample from a gaussian distribution correct so we assume that we know how to sample from a gaussian distribution and therefore we can generate this z as much as we want

### 00:31:36 · Speaker 1

And that has no parameters. What is parameterized is this function V theta of Z okay that this Z is passed through to get a get an X cap okay which has a distribution P theta.

### 00:31:51 · Speaker 1

Is this okay? Yeah yeah okay yeah uh

### 00:31:57 · Speaker 2

Yeah hi sir uh this is uh the Gaussian distribution of this random variable Z

### 00:32:03 · Speaker 1

The random variable z has a Gaussian distribution

### 00:32:08 · Speaker 2

And uh sir in this uh W three can you uh scroll up a little bit

### 00:32:34 · Speaker 2

In this uh so w3 will be a this matrix of L3 cross L2 right

### 00:32:41 · Speaker 2

Yeah yeah

### 00:32:45 · Speaker 1

A week

### 00:32:47 · Speaker 3

this Z the Z did it uh is it actually representative of the data or was some

### 00:32:55 · Speaker 1

Translation

### 00:32:56 · Speaker 3

Optional

### 00:32:56 · Speaker 1

no no no no no no no so z is just uh uh an input random variable okay it can be anything you take it to be normal distribution normally distributed okay okay you take it to be normally distributed it has nothing to do with data

### 00:33:13 · Speaker 3

Okay something was done to bring the data time to Z form I mean like

### 00:33:17 · Speaker 1

So no it has nothing to do with data it has zero connection with data

### 00:33:20 · Speaker 4

No okay

### 00:33:24 · Speaker 1

It has nothing to do with data okay

### 00:33:28 · Speaker 1

So it is just that we are okay. So I tell you the like maybe the high level story or maybe it's just a mistake. See basically what we are trying to do is we are trying to transform okay an arbitrary random variable to some random variable that has same distribution and has our input data.

### 00:33:51 · Speaker 1

Is that okay

### 00:33:52 · Speaker 3

Right yes

### 00:33:53 · Speaker 1

Now, this z is an arbitrary random variable and we know that if you pass an arbitrary random variable through a function, the output random variable will have a different distribution. Now, the goal is to choose these parameters theta such that the transformation that this arbitrary random variable goes through will be such that the output random variable that you get will have the same distribution as that of input theta.

### 00:34:26 · Speaker 1

So now the goal is to set this d theta, set the parameters of the neural network such that distribution p theta matches with px, which means that I want the distribution of x cap to be same as the distribution of x which is my input data. Z has nothing to do with the data. It is just the input seed. It is seed.

### 00:34:51 · Speaker 1

It is the random CNN that you start with. You pass it through a neural network, okay? And output of the neural network will have some distribution. I want the distribution of that output to match to the input, the distribution of given data.

### 00:35:09 · Speaker 4

Yes, in that case, the creation or the finding out of the distribution of Z is also as equally important as G theta of Z, right?

### 00:35:21 · Speaker 1

No no because

### 00:35:23 · Speaker 3

I want to say

### 00:35:25 · Speaker 1

Yeah this is a random seed you can start with any this is the first

### 00:35:30 · Speaker 3

Nothing was done there so we are just picking something a random seed

### 00:35:34 · Speaker 1

It is random stuff it is nothing but random stuff

### 00:35:38 · Speaker 2

Okay okay fine

### 00:35:39 · Speaker 1

Also transform this normal distribution into distribution of interest via neural networks

### 00:35:45 · Speaker 2

Okay okay okay yes thank you

### 00:35:48 · Speaker 1

The astic

### 00:36:13 · Speaker 1

So it is not in a classifier what happens is the data will have a larger dimension where you give images and you reduce the dimensionality and the final layer will be equal to the number of classes

### 00:36:29 · Speaker 1

But in generative models it is the other way around because the dimensionality of X cap here the output should be equal to the dimensionality of the input image because the final goal is to sample isn't it? Now if you want to sample pictures of dimensional dimensionality 200 by 200 pixels then the output of this neural network has to be of dimensions 200 cross 200.

### 00:36:55 · Speaker 4

Okay and what would be the input dimension in this case uh if the num uh image size is 200 plus 200?

### 00:37:02 · Speaker 1

Typically it is it will be of size let's say 16, 32 and so on. So that's why if you look at the shape of the neural network that I have written, it will have increasing dimensionality as you move deeper onto the network.

### 00:37:20 · Speaker 1

example

### 00:37:23 · Speaker 1

See input is of 16 dimensions and you keep increasing so see it is all in setting up this L1, L2 etc right you choose those are the hyperparameters that are in your control as a designer.

### 00:37:34 · Speaker 2

Yeah that is fine

### 00:37:36 · Speaker 1

like our output should be a image and input is also a image right so no no no no it is not an image it is a random seed that is what i'm trying to say input is not an image

### 00:37:48 · Speaker 1

So this is a generative model

### 00:37:51 · Speaker 4

Okay okay yeah yeah yeah

### 00:37:52 · Speaker 1

You understood the setup it is see it is not you are giving an image and you are asking for a class you are including the random seed and you are expecting the neural network to give you an image from the data distribution

### 00:38:04 · Speaker 4

Yeah yeah yeah it's a generative

### 00:38:09 · Speaker 1

So we the course is deep generative modeling

### 00:38:13 · Speaker 3

Just joking

### 00:38:14 · Speaker 1

It's okay you understand now

### 00:38:17 · Speaker 1

That's why the shape look at the shape right the shape of the neural network that I have drawn is that you start from a lower dimension and go to a higher dimension as you move across the network. Okay

### 00:38:33 · Speaker 1

As a shield

### 00:38:36 · Speaker 4

understand we are not using the input but somewhere we will have to relate with the input distribution like that is how we will calculate the loss and all

### 00:38:47 · Speaker 1

Come again

### 00:38:49 · Speaker 4

Like I understand we are not using the actual input here, but what I'm saying is how we will relate with the actual input distribution.

### 00:38:57 · Speaker 1

I am not saying that we are not using the input I am saying that the input distribution does not matter because you can start with any random seed and then convert that into distribution of interest using your own

### 00:39:13 · Speaker 4

Okay sir so where we use the input here

### 00:39:17 · Speaker 1

Okay see how do you get X cap here

### 00:39:22 · Speaker 1

X cap is gotten by taking a sample from Z, okay, and passing through. So basically what you do in practice, I've written this, no Z is sampled via random number generator, which means that you run rand N once, okay, you get one number, that is your Z. You pass that Z through this neural network, D theta, you get an X cap, that is how you use the input.

### 00:39:51 · Speaker 3

From the data set

### 00:39:52 · Speaker 1

you mean okay so please don't call it as input you know it's a bit confusing input to this setup is z okay and uh the data okay is x1 through xn we are i mean everything that we do is using data we will see that right we have not still told you how to set the parameters of g theta right the parameters of g theta is set by using the data

### 00:40:20 · Speaker 1

I thought, I mean, yeah, I think, you know, there is a confusion. Z is what is an input to this setup. Okay. And let us, let us call the, let's call x1, x2, x3 as input, sorry, data.

### 00:40:35 · Speaker 1

And this has the random seed

### 00:40:39 · Speaker 1

We will use, I mean, I okay, let me, I mean for everyone's sake, you know what I'm saying? When I say that the input distribution does not matter, I'm referring to this random seed, not to the data distribution. I mean everything depends on data distribution because we are interested in modeling the data distribution. When I say input input to this setup, which is the random seed, it does not matter if you sample from a normal distribution or you sample from a uniform distribution. Is that okay? Is this clear to all of you?

### 00:41:13 · Speaker 1

I mean that's a huge confusion if you had that confusion is this clear

### 00:41:23 · Speaker 1

Okay, yeah, I think there's one more question Sanjit

### 00:41:28 · Speaker 4

I understand that we are just taking a random uh sample Z from the normal distribution and passing

### 00:41:40 · Speaker 1

Mm

### 00:41:47 · Speaker 4

What are we taking it

### 00:41:50 · Speaker 2

Comparing it

### 00:41:52 · Speaker 4

Like I'm saying it

### 00:41:52 · Speaker 1

I have not told you that yet. I have not told you that yet. I'm just saying x hat has a distribution. Let's call it p theta. That is what I've told you so far. I have not told you how to make this p theta close to px. Anyway, because you're asking, I'm telling you. So evaluate the divergence between p theta and px and set the parameters of this g theta such that that divergence is minimized.

### 00:42:16 · Speaker 2

I understand that flow like you had explained it in the last class what I'm trying to relate to is like let's say for like supervised learning when we have the

### 00:42:28 · Speaker 2

Let's say we are going for

### 00:42:31 · Speaker 1

Hold on, hold on, hold on, hold on. You are asking me how to do it practically, right? How do you basically what you are saying is how do you minimize the divergence practically, right? Yes, sir. I have not answered that question. Hold on. I'll answer it in this class.

### 00:42:46 · Speaker 4

Focus on sure thank you

### 00:42:47 · Speaker 1

Okay, yeah Harish

### 00:42:51 · Speaker 2

So the sampling of the data the normal distribution one so do we can why do we consider it for a normal distribution or can we consider with any other distribution so for the for the side here

### 00:43:03 · Speaker 1

Yes you can but generally normal distribution is chosen because normal distribution has infinite support which means that like it has I mean for the entire space Rd the density function is not zero if you take uniform distribution for example right the density function vanishes out of I mean outside of a window but in normal distribution the density function is is existing when it's non-zero over the entire space no that's why you

### 00:43:33 · Speaker 1

Take normal distribution

### 00:43:36 · Speaker 2

And one more question on the dimension of K here so the dimension K here is dimension of

### 00:43:43 · Speaker 1

Yeah typically it is tend to be 16 32 if I mean if you're working with images

### 00:43:50 · Speaker 2

So does it matter? So you have mentioned that the D is much, much greater than K here, right? So does it matter based on the data size? So we need, we choose 16 or 32 or is it also random?

### 00:44:03 · Speaker 1

Yeah, that's a good question. It's a hyperparameter, but like in some of our research, we have we have actually found out that the dimensionality matters. Right. There is an optimal dimensionality is what we show in some of our papers. But yeah, like in general, it's a hyperparameter.

### 00:44:22 · Speaker 2

And so we we choose that once like for example we take an initial of 16 or 32 and then based on the training and how it works so do we change that based on

### 00:44:32 · Speaker 1

Typically that is not a happy parameter that people do norm that is kept fixed

### 00:44:43 · Speaker 1

Yeah yeah

### 00:44:46 · Speaker 4

So the real application of this function I want to understand my assumption is correct or not if we give some few text like a cup on table then it will give me a picture of the cup on table

### 00:44:57 · Speaker 1

one table no no no see for for now i have not told you the conditional part of it what you are saying is a conditional generating model we'll come to that in a while it is not it is not conditional generating modeling right now right now what happens is after you train it you give a random number as an input to this okay it will give you a picture from the distribution

### 00:45:22 · Speaker 1

Now that you are asking me let me just show you that as well

### 00:45:31 · Speaker 1

You see my screen now there is this website called thispersondoesnotexist.com okay

### 00:45:38 · Speaker 1

So what is happening is every time I refresh this page

### 00:45:43 · Speaker 1

I get a new picture you see

### 00:45:47 · Speaker 1

see my screen no see these are pictures of like non-existent people so what is happening when i refresh the screen is that a random number is being generated which is your z and that is getting passed through this network g theta and you are getting a picture here there is no conditional generation i am not giving a text as an input i am just giving a random number as an

### 00:46:18 · Speaker 1

Right now I'm not looking at conditional generation. I'm simply looking at this is called unconditional generation where you generate images from the underlying distribution or generate data from the underlying distribution without conditioning.

### 00:46:32 · Speaker 3

Got it

### 00:46:35 · Speaker 1

I will also talk of conditional generation, but I am skipping a lot. We will do that one step at a time. We will understand the unconditional part and then adding conditioning is a trivial extension to this, okay?

### 00:46:48 · Speaker 4

Yeah so uh I know sorry you have not explained this but in the

### 00:46:52 · Speaker 3

terms of picture we got a p theta but then uh how to measure like between p theta and p x

### 00:47:02 · Speaker 1

Dean I've told you that I'll do this in this class please don't repeat the questions that I've answered already

### 00:47:08 · Speaker 4

Yes, yes.

### 00:47:09 · Speaker 1

That is the next thing that we will do. No, see, okay. So let me tell you my philosophy of teaching. When I teach, I just, I mean, like open it layer by layer. So now what is happening is I am trying to give you an abstraction of what is happening. We will go to the details. So now at the level of abstraction, what you need to understand is that the idea is that you start with an arbitrary random variable g, pass it through a function g theta, and you get another random variable which has a distribution p theta.

### 00:47:39 · Speaker 1

Now the next thing is you tweak the parameters of this d theta such that the distribution of the output of this network x dot is same as the distribution of p x. Now how do we do that is a question that I'll answer in a while. But now you ask me questions at this level of abstraction. If you have difficulty in understanding this level of abstraction, sure ask me questions.

### 00:48:09 · Speaker 1

I'm going to do in the due course right if you ask me that anyway I mean I don't mind but yeah so just a request okay anyway uh Mukesh

### 00:48:20 · Speaker 1

my question is regarding

### 00:48:22 · Speaker 1

Sir, in the CNN architecture, actually what we do, we try to implement this pooling layer where we try to reduce the dimensions of the data. But here we're just passing the seed to increase the dimensionality. Is that correct? Yeah, yeah, yeah. So the neural network here will have increasing dimensionality. So actually here we don't have input data as an image. That's why we are trying to increase the dimensionality.

### 00:48:48 · Speaker 1

I will not say that see we want to start with some noise or some random arbitrary from from an arbitrary random variable and generate images so which means that we start with a lower dimensionality we need to increase the dimensionality

### 00:49:06 · Speaker 1

okay so now in terms suppose see i have not told you that see this is not a cnn that i have written what i have written here is a fully connected neural network

### 00:49:16 · Speaker 1

Okay, which is a feedforward neural network or a multi-layer perceptron. If you want this to be implemented as a CNN, okay, that also has to be done in the TA session.

### 00:49:30 · Speaker 1

So you have to teach about upsampling layers

### 00:49:34 · Speaker 1

There are this neural net I mean neural network layers called upsampling or also called transpose convolution layers

### 00:49:47 · Speaker 1

Okay, that will take as an input a lower dimensional feature and give you a higher dimensional feature vector as output. Just like you have convolutional layers, there are transpose convolutional layers that would increase the dimensionality of neural networks. Okay.

### 00:50:04 · Speaker 3

Okay, so okay, thank you

### 00:50:05 · Speaker 1

But but don't worry about architecture for now. I mean, these for us, g theta is simply a function. I mean, it need not be a neural network also, but now because in in practice, we are only looking at neural networks, I've said that it's a neural network. So for now, let us assume that these are all fully connected neural networks, which are I mean, no fancy network architecture here, right? I mean, they are all multi layer perceptrons or simply fully connected neural networks. Is that okay? For now.

### 00:50:34 · Speaker 3

Yeah yeah sir correct correct words

### 00:50:37 · Speaker 1

Okay, uh any other question is the problem setting clear to all of you?

### 00:50:51 · Speaker 1

I didn't expect so many questions at this stage anyway no problem it's good that you're asking questions okay let's move on so now what is the objective so now the objective

### 00:51:05 · Speaker 1

is to make

### 00:51:10 · Speaker 1

P theta

### 00:51:14 · Speaker 1

uh as close okay

### 00:51:18 · Speaker 1

Make PT done

### 00:51:22 · Speaker 1

to px correct now if we do this what happens is suppose you are given uh data from let's say human face distribution if we can have this setup and make my p theta close to px then i have solved the problem of generative modeling do you agree

### 00:51:41 · Speaker 1

Every time I start with a random seed and pass it through the theta, I will get a picture from like human faces because the distribution of the output of this neural network is now close to px. Clear? Is this clear?

### 00:51:59 · Speaker 1

Okay now what do we have to do is is that the question is that question

### 00:52:07 · Speaker 1

How to

### 00:52:10 · Speaker 1

set the parameters

### 00:52:17 · Speaker 1

parameters of g theta

### 00:52:22 · Speaker 1

Such that

### 00:52:28 · Speaker 1

that p theta is close to px

### 00:52:36 · Speaker 1

is the central question do you agree so now only thing that we have in our control is uh g theta which are the parameters of neural networks the question is how do we set the parameters of a neural network such that p theta is close to px we note that if you fix a value

### 00:52:59 · Speaker 1

excuse me so if you fix a value for the parameters g theta parameter top parameters of this neural network you will get some distribution on on on some distribution on the output now if you take another set of parameters you will get another distribution now the question that is to be asked asked is which set of parameters of this neural network will ensure that p theta is close to ps

### 00:53:26 · Speaker 1

Good

### 00:53:28 · Speaker 1

Now to do that is now the the solution for this is that simply set the parameters of your such that

### 00:53:38 · Speaker 1

it minimizes search over all possible sets of theta such that some divergence between px and p theta is minimized. And this divergence now is a function of theta, right? Because if you choose a theta, you will have one set of divergence. So now what you have to do is that, so this means, write that down in English, that set the

### 00:54:04 · Speaker 1

The parameters

### 00:54:07 · Speaker 1

of the neural network

### 00:54:11 · Speaker 1

Such that

### 00:54:17 · Speaker 1

The divergence

### 00:54:22 · Speaker 1

between px and p theta is minimized

### 00:54:28 · Speaker 1

That's the meaning of argument okay

### 00:54:31 · Speaker 1

So choose a theta that would minimize the divergence between px and p theta. Is this clear? Now the next question that comes up is whatever you have been asking question.

### 00:54:47 · Speaker 1

Give one

### 00:54:50 · Speaker 1

Data

### 00:54:54 · Speaker 1

D okay what is data remember that there are samples from PX

### 00:55:03 · Speaker 1

And

### 00:55:06 · Speaker 1

samples from p theta

### 00:55:13 · Speaker 1

samples from p theta. How do we have samples from p theta? They are simply the output of neural networks.

### 00:55:23 · Speaker 1

Output of neural network D theta see output of neural network D theta is nothing but samples from

### 00:55:32 · Speaker 1

E theta right

### 00:55:36 · Speaker 1

Given data which are samples of PX and samples from P data how to compute and minimize

### 00:55:46 · Speaker 1

compute the divergence the next question you understand this right so now let me just tell you again so in the setup remember the setup the setup is the following that we have a neural network

### 00:56:00 · Speaker 1

theta of z okay and z is a random seed from from normal distribution and we have samples from x cap right and this has a distribution p theta we also have data that are some samples given some images given from px okay we should note that both px and p theta are unknown

### 00:56:27 · Speaker 1

These two are unknown but but samples from

### 00:56:35 · Speaker 1

From px and p theta are available

### 00:56:42 · Speaker 1

Okay, so you understand this now. This is actually the most important thing because this is the one that bounds the entire space of generative models that you don't know the underlying distributions, but you have samples from those distributions. Samples from PX, the true data distribution is known because that is the data that we have. Okay, samples from P theta are also known because we can generate

### 00:57:12 · Speaker 1

as many samples from p theta as we want because what do you mean by generating a sample from p theta let me just say samples from

### 00:57:23 · Speaker 1

Samples from PX is simply the data, given data.

### 00:57:31 · Speaker 1

given data D now samples

### 00:57:37 · Speaker 1

from P theta how do you get that

### 00:57:46 · Speaker 2

sampling choosing different z

### 00:57:49 · Speaker 1

Correct choose

### 00:57:52 · Speaker 1

Different Z

### 00:57:56 · Speaker 1

Pass them through

### 00:58:02 · Speaker 1

g theta of s you understand so now we have samples from px samples from p theta now the question is given samples from these two distributions p theta and px how do we compute the divergence metric and of course why do we have to compute the divergence metric because only when we compute the divergence metric we can minimize it right i mean we can use gradient descent or differentiate it and then optimize for it first we need to compute the divergence metric between px and p theta given that we don't have access to px and

### 00:58:32 · Speaker 1

data but we only have access to its samples. Now 70% of this course will be taking answering this question in different ways that given that we have samples from the true distribution and the generated data distribution how do we compute a divergence metric between those two?

### 00:58:53 · Speaker 1

Okay, so please try to appreciate and understand the problem. We have the distribution, sorry, sorry, sorry, sorry. We don't have the distribution, we have the samples from it. Now the entire statistics, right, and the machine learning and the other statistical series, they ask this central question. The central question that is asked is that if you do not have distributions, but you have samples from it, how do you compute something? Now in this case, we need to compute

### 00:59:23 · Speaker 1

divergence metrics, right? In some other case, you know, you might need to compute the moments, you might need to compute some integrals, etc. depending upon what the application is. But one of the central questions in statistics or probabilistic machine learning is that if you are given samples from distributions without giving the actual distributions, how do you compute some things involving the distribution? That is the central question. I mean, in our case, what we should do, please don't forget the storyline. Storyline is that we are interested

### 00:59:53 · Speaker 1

in generating samples from p x. Now to generate samples from p x what we have done is that we have taken an arbitrary random variable and we have a function g theta. Now we know that passing an arbitrary random variable through a deterministic function will change the distribution of that function. Now we need to set this function g theta such that the output of this function g theta will be a random variable that has the exact same distribution as that

### 01:00:23 · Speaker 1

of the input data. Now, how do we do that? By minimizing the divergence metric. Okay. To minimize the divergence metric, we need to first compute the divergence metric. Now, the question now is that how do you compute the divergence metric between two distributions which are unknown given that we have samples from them?

### 01:00:44 · Speaker 1

Even data and samples from P data how to compute the underlying development metric

### 01:00:51 · Speaker 1

Is this clear so far? Any questions here? Okay, I see some hands raised. Kartik?

### 01:00:58 · Speaker 4

Yes, sir. So I have a query. So we set about when we have samples of RK, then we get the sigma algebra using like L1, L2, all those parameters, right?

### 01:01:10 · Speaker 1

I've never used the word sigma algebra here

### 01:01:15 · Speaker 4

Sorry

### 01:01:15 · Speaker 1

Very

### 01:01:17 · Speaker 4

Yeah sigma of what we wrote right

### 01:01:20 · Speaker 1

Design a neural network okay you start with a k dimensional vector and you keep increasing the dimensionality till you go to d dimensional vector yeah

### 01:01:29 · Speaker 4

But so we don't have any control over whatever is written in RL1, RL2 other than our input, right? So these are fixed. That's what we are saying right now.

### 01:01:38 · Speaker 1

dimensionality are these are hyperparameters no L1 L2 L3 are hyperparameters that you fix

### 01:01:46 · Speaker 1

But you fix other designer

### 01:01:50 · Speaker 1

So when you say, see, when people say that it's a billion parameter model, it is some, you know, 70 billion parameter model, what are they saying? They are referring to these L1, L2, L3. So that's a design choice. Okay.

### 01:02:05 · Speaker 4

Yeah, sorry sir, but what I wanted to know was what are the whatever is the value of omega one or like omega two?

### 01:02:05 · Speaker 1

I'm sorry

### 01:02:13 · Speaker 1

Uh

### 01:02:13 · Speaker 4

uh those things are no w1 w2 sorry uh w1 w2 those things are not in our control right away right other than the

### 01:02:21 · Speaker 1

No no no okay okay so have you tried a neural network before

### 01:02:28 · Speaker 4

Yeah in pictorial forms only sir

### 01:02:31 · Speaker 1

Okay, see how do you drive a neural network? You start with some random initialization problem W1, W2, W3, W4, okay?

### 01:02:31 · Speaker 4

Okay

### 01:02:41 · Speaker 1

And then solve this optimization problem. So now you start with some W1, W2, W3, W4 and then you know you keep on changing these W1, W2, all these parameters till you reach a point where your objective is optimized. That's okay, try new approach.

### 01:03:00 · Speaker 4

So not just said we will be trying with variable various values from W1 W2 also like we can change.

### 01:03:09 · Speaker 1

All we change are W1 W2 W3 W4 only no That's the only thing that we would change nothing else

### 01:03:16 · Speaker 4

Okay yeah

### 01:03:17 · Speaker 1

When we solve this optimization problem that we have we have written here what I mean what do you mean by optimizing over theta optimizing over theta actually means setting up these W's you know

### 01:03:33 · Speaker 4

Okay so the final

### 01:03:34 · Speaker 1

Do all the fighting

### 01:03:36 · Speaker 4

The final changes will be in uh w1 w2 w3 w4 whatever is the value

### 01:03:40 · Speaker 1

Of course right I mean when you optimize over theta you want theta star what is theta theta is collection of all w w and w 3 w 3 all the parameters of the neural network what you change are the see learning or training of a neural network is nothing but changing the parameters of it that's why I'm asking you right okay uh here is a a small request the next class uh you please study about you know uh what do you mean by training the neural network

### 01:04:10 · Speaker 1

I mean I I assume that all of you know what training a neural network is

### 01:04:17 · Speaker 1

See, I told you that the first four chapters of that Ian Goodfellow's machine learning book, deep learning book is a prerequisite. Did you people go through it?

### 01:04:33 · Speaker 1

And did you go through it Did you go through training neural network general backpropagation and so on

### 01:04:40 · Speaker 3

just started like first two chapters are random process and linear algebra

### 01:04:46 · Speaker 1

Okay okay

### 01:04:47 · Speaker 3

I'm going to move

### 01:04:49 · Speaker 1

Yeah, so please, you know, quickly ramp up. See, now we have sort of come through the, come through the meat of the course, okay? Like, I expect all of you to know what training neural networks mean. So please go through those chapters and that those are actually sort of very strict prerequisites. Otherwise, see, I can't teach how to like training neural network in this course, you see? So please have a look at that.

### 01:05:19 · Speaker 1

Okay are we ready

### 01:05:22 · Speaker 4

So so when we look at the KL divergence formula

### 01:05:27 · Speaker 2

The clear divergence

### 01:05:30 · Speaker 1

by the way no no i mean like yeah clear divergence is one of the multiple possible divergences i will define now a family of divergence metrics okay okay that will be minimal now but anyway you go on okay clear divergence is one of them

### 01:05:30 · Speaker 4

Why did we get different

### 01:05:45 · Speaker 2

Yeah, my question was, so you can, can you really, in that formula, it is like there is a closed form, form of two probability distributions.

### 01:05:55 · Speaker 1

But in this setup that you're not given

### 01:05:55 · Speaker 4

But in this setup that you're not doing

### 01:05:57 · Speaker 1

No, even in KL divergence, see what is KL divergence between Px and P theta? Let me write that down. KL between Px and P theta is given by integral of Px evaluated at x log of Px evaluated at x divided by P theta evaluated at x to integrate this out. This is the definition of KL divergence, right?

### 01:06:20 · Speaker 4

Right yes sir

### 01:06:21 · Speaker 1

Now you don't know P x you don't know P theta

### 01:06:25 · Speaker 4

Great yeah

### 01:06:26 · Speaker 1

And how do we compute this That is the whole question

### 01:06:28 · Speaker 4

Okay okay okay

### 01:06:31 · Speaker 1

The question is that when we don't have underlying distribution density functions but we only have samples from it

### 01:06:38 · Speaker 4

Hopefully

### 01:06:38 · Speaker 1

Do we compute the divergence metric is the whole question

### 01:06:45 · Speaker 2

The another question is

### 01:06:48 · Speaker 2

Any such metric how can we have parallels for a single point for a single sample at a time

### 01:06:55 · Speaker 4

In the sense like

### 01:06:57 · Speaker 1

So none of the metrics none of these metrics are doing I mean like they're they're they're they're they are at their point wise

### 01:07:05 · Speaker 4

Okay, they're like a group of examples

### 01:07:05 · Speaker 1

Like a group open

### 01:07:08 · Speaker 4

We will see no I okay

### 01:07:08 · Speaker 1

so we will see no i have okay okay okay see how do you compute these divergences when you don't have distributions and only have samples is a question that i have not answered it i will answer it in a while okay if you have questions on the setup ask me

### 01:07:28 · Speaker 1

Okay so these are things that I'll discuss in a while so any questions on this setup

### 01:07:33 · Speaker 4

Okay no

### 01:07:35 · Speaker 1

Okay yeah Aamir up

### 01:07:37 · Speaker 3

Yes, sir. I have a question on the last statement. So samples from P theta choose different Zs and pass them through G theta. Now Z is a random variable which you are passing through a neural network. So my question is, why do we have to pass different Zs, random variable being a function, if we pass a different point belonging to the range space of random?

### 01:08:00 · Speaker 1

Yes yes that is what we do when we say different z's that's exactly what we mean to sample from the range space of the random variable and then cost always that see whenever I say that there are points from random variable they always mean that it's from the range space of the random variable

### 01:08:15 · Speaker 3

Always okay

### 01:08:17 · Speaker 1

I think we settled this we settled this in the first class itself right I told you that I say that when I say that there are we have n samples from a random variable I said that they are always I always mean that there are n samples in the range space of the random variable with a distribution I think that we have settled no

### 01:08:31 · Speaker 3

Yeah, that is subtle. I was I thought that since you've written choose different z's, I thought you were choosing a different random variable altogether.

### 01:08:39 · Speaker 1

I need an SOS message

### 01:08:42 · Speaker 1

No, yeah. Okay. Uh

### 01:08:47 · Speaker 1

Is that okay Shall we move on

### 01:08:51 · Speaker 1

Okay, so now the important question is, right, how do we compute this divergence metric when we don't have distributions but only have samples from it? Okay, before we take that question, let us...

### 01:09:09 · Speaker 1

And by the way, I'll tell you the answer is through this adversarial optimization. This entire generative adversarial network, right, or adversarial optimization, it is asking, it is trying to answer this question, which is that how do we compute the divergence metric between distributions and we do not know the distributions, we only have samples from it. This adversarial optimization is one way to do it, by the way. And like variation,

### 01:09:39 · Speaker 1

inference is one other way which will give rise to VAEs and diffusion models okay so adversarial optimization is one way the variational inference is one other way and MMD is one other way and so on we will look at different ways of doing it a maximum likelihood estimation is one other way which is what is used in uh the LLMs and so on we will look at uh all I mean all possible ones one by one okay that is what we do in this course we do in this course okay so let us look at adversarial optimization

### 01:10:09 · Speaker 1

And for that let's take a

### 01:10:28 · Speaker 1

Now let us let us define define

### 01:10:34 · Speaker 1

A family of divergence metric first

### 01:10:39 · Speaker 1

And this method now that we will look at right now is is powerful enough to uh to be able to uh handle a large class of divergence metrics okay it's a common thing okay or rather it's a it's a method that would enable minimizing the family of divergence metrics you know not one divergence metric it will uh it will uh enable us to minimize a family of divergence metrics okay

### 01:11:09 · Speaker 1

Now for that let us first define a family of divergence metrics so given two distributions

### 01:11:16 · Speaker 1

one two

### 01:11:19 · Speaker 1

probability distributions

### 01:11:22 · Speaker 1

Let us let me just uh work with the density function given two density functions

### 01:11:32 · Speaker 1

density functions px and p theta okay

### 01:11:43 · Speaker 1

Define

### 01:11:47 · Speaker 1

Divergence

### 01:11:53 · Speaker 1

We've also, I've already seen one divergence metric, no, in the last class, which was the Hilbert-Libert divergence. We will, I will define a large class of family of divergence metrics, okay? All of that can be minimized using the technique that we will see in this class, okay? That's why I'm defining a large class of family of divergence metric, even to energy function p and p theta, define a divergence metric as follows.

### 01:12:21 · Speaker 1

point to the task df between

### 01:12:26 · Speaker 1

B x and B theta

### 01:12:29 · Speaker 1

defined as

### 01:12:50 · Speaker 1

Integral

### 01:12:55 · Speaker 1

P theta f x

### 01:12:59 · Speaker 1

fals

### 01:13:04 · Speaker 1

P x of x divided by P theta of x.

### 01:13:11 · Speaker 1

beams

### 01:13:14 · Speaker 1

This is the definition of a gradient square F

### 01:13:21 · Speaker 1

of view is a function that takes

### 01:13:30 · Speaker 1

a positive real number and maps it to another positive real number. It is a

### 01:13:38 · Speaker 1

Convex function

### 01:13:42 · Speaker 1

We'll explain it in a while

### 01:13:46 · Speaker 1

Okay so these are called F divergences

### 01:13:58 · Speaker 1

Okay. Okay. So let me explain what this is. Now suppose we are given two density functions and we want to define a divergence metric between them. What is a divergence metric? Remember that it's a it will give you a sense of distance between two density functions, right? Now,

### 01:14:17 · Speaker 1

There is a class of density functions that you can define which are called f divergences, which are which is defined like this. So this is the definition of f divergence. Okay. What is it? It is you take it is integral p theta of x f of px by p theta of at dx. Okay. Let us look at this this term that is inside this bracket. Now you know that the density function px of x is a scalar.

### 01:14:47 · Speaker 1

Correct. Density function is a scalar valued function in the sense that it will take a vector x and it will give you a number, a positive real number, right? So all of you know this, right? What is a density function? Density function is a scalar valued function. Okay. So now if you evaluate the density function px at some x, you will get a scalar. And if you evaluate the density function p theta of x, you will get another scalar. So ratio of these two,

### 01:15:17 · Speaker 1

Px by p theta at a given point x is a scalar

### 01:15:21 · Speaker 1

Correct. Now, this function f of u takes a positive real number because the ratio of these two density functions is a scalar. It takes a positive real number and gives you another real number r. That is this value. f of this ratio is this value. And the definition of f divergence is the integral of p theta of x times f of px of x by p theta of x dx integrated over all values of x. This is the definition of what

### 01:15:57 · Speaker 1

It has no more got muted. This is the definition of what is called as a called as an f divergence. Now you can choose an f function. OK, I'll give you examples. So now if f of u.

### 01:16:14 · Speaker 1

The results

### 01:16:18 · Speaker 1

u is a what is u here u is px by pt topic okay it's a scalar here i've just given written that as a dummy variable u but in the definition it is the ratio of the density functions if f of u is equal to log u okay then the corresponding divergence is called the kL divergence

### 01:16:41 · Speaker 1

Now with f of u is equal to let's give you some examples of it

### 01:16:55 · Speaker 1

Sorry, it is u log u. Sorry, if it's u log u, then it is that. If it's uh.

### 01:17:02 · Speaker 1

half of u log u minus u plus one

### 01:17:10 · Speaker 1

Log

### 01:17:12 · Speaker 1

u plus 1 by 2 this is called the Jensen Shannon divergence

### 01:17:27 · Speaker 1

If it's um

### 01:17:33 · Speaker 1

half mod u minus one then this deviation is called the total variation distance

### 01:17:48 · Speaker 1

and so on. Okay. So now you can choose any convex function for this f and one choice for this convex function will give you one divergence metric. So basically what I'm doing is I'm defining a family of divergence metric. Okay. Which is like one of the, I mean, you can choose a convex function and you get one family of one, one divergence metric. So what do you mean by this? If I write u log u here, what will happen to f divergence? Let me show you that example.

### 01:18:19 · Speaker 1

example okay now f divergence is given as integral p theta of x log of sorry f of

### 01:18:32 · Speaker 1

of p x of x divided by e theta of x dx correct now let us say that f of u is u log u okay now in that case df will now become integral e theta of x to substitute u log u for f of u which is

### 01:18:56 · Speaker 1

Now this this entire thing which is right inside this f is now called as u this is p of x

### 01:19:07 · Speaker 1

P x of x by p theta of x this is u correct into log of u

### 01:19:18 · Speaker 1

p x of x divided by p theta of x. Note that this entire thing which I have written as f of

### 01:19:30 · Speaker 1

D x of x y d 3 top x, correct? This is what it is for d x.

### 01:19:37 · Speaker 1

Oh

### 01:19:43 · Speaker 1

I will skip the algebra, okay? So if you simply, this is a times log ratio, right? So now you just take the ratio inside and so this, okay, so this p theta x and this p theta x cancels. This will be.

### 01:20:03 · Speaker 1

P x of x times log of P x of x divided by P theta of x V x okay which is nothing but the kL divergence

### 01:20:16 · Speaker 1

Understood. That's what it is, right? So what we are doing is that we are defining a general family of divergence metrics. Now if you take where, these are called f divergences. If you take some form for this f function that is there in the definition of f divergence, you will get different divergences. You get k- divergence with one f. You will get Jensen-Channon divergence with one other f. You will get total variation distance with one other f and so on. So basically, we are defining an

### 01:20:46 · Speaker 1

Infinite family of divergence metric between two distributions depending upon what your function is.

### 01:20:53 · Speaker 1

The reason I did it is why what is the what is the uh the coherence or relevance to this is that the adversarial optimization technique that we see you look at what we are doing right we want to know

### 01:21:07 · Speaker 1

minimize or compute the divergence metric given samples from two distributions right now what divergence metric are we considering we are considering not one divergence metric we will be giving you a a a tool or a technique that would compute and minimize a family of divergence metrics that are called f divergences you can choose any divergence see if you people know this generative adversarial networks or gians when after this paper came there are so many improvised

### 01:21:37 · Speaker 1

that came over it no that's called f i mean like l is given x squared again like you know there is some w again this again that again all that they are nothing but changing this f divergence that's all so you take one definition for the f divergence you will get one again so what we are what we will see right now is we will not look at one minimizing one divergence metric we will now look at minimizing a family of divergence metric given uh samples from the underlying data distribution

### 01:22:08 · Speaker 1

Is this clear? So now any questions on the definition of f divergence? So basically what we need is given a given some convex function f a scalar value of convex function f we can define a divergence metric between pair of distributions.

### 01:22:26 · Speaker 1

Okay, and k divergence happen to be a special case of this and Jensen's and divergence happen to be a special case of it and total variation distance will happen to be a special case of it and so on. So every there is a lot of very very well known divergence metric in all special cases of these f divergences. Okay, in general at an abstraction level this is you think of it like the definition of a class right I mean where each of these divergences are one instance of this class of divergences called f divergence.

### 01:22:56 · Speaker 1

business

### 01:22:59 · Speaker 1

What we will see now is that given the samples from the underlying distributions, how do we minimize any F divergence between those two using samples? Let me write that down. Now the objective I will take questions in a while.

### 01:23:22 · Speaker 1

Cool

### 01:23:25 · Speaker 1

Viewed

### 01:23:28 · Speaker 1

compute f divergence okay

### 01:23:32 · Speaker 1

doing

### 01:23:35 · Speaker 1

extremely okay

### 01:23:38 · Speaker 1

You

### 01:23:41 · Speaker 1

samples

### 01:23:44 · Speaker 1

given samples

### 01:23:48 · Speaker 1

Without

### 01:23:52 · Speaker 1

knowing what px and p theta are

### 01:23:59 · Speaker 1

We have we don't know P X and P theta but we have samples from P X and P theta now how do you compute the M divergences between them is the next question that we will answer

### 01:24:10 · Speaker 1

Okay, uh any questions here?

### 01:24:14 · Speaker 1

Uh

### 01:24:16 · Speaker 2

She won't

### 01:24:17 · Speaker 1

Four

### 01:24:18 · Speaker 2

Yes

### 01:24:20 · Speaker 4

Yes sir on the F divergence side as we have said we can have infinite combinations of F divergence function and

### 01:24:27 · Speaker 1

No no no no there are there are no combinations here you can have infinite f divergences by changing f

### 01:24:36 · Speaker 3

Yes. Yes. So yeah, but we are talking about the three variations, the KLI divergence, GS divergence. So is there any specific benefit does they bring into the table or?

### 01:24:48 · Speaker 1

Good question. Yes they do. They do. In fact, I'll

### 01:24:54 · Speaker 1

After we look at how to minimize this now I will tell you like advantages and disadvantages of let's say at least scale and density channel divergence okay

### 01:25:06 · Speaker 1

But yeah, so different divergences have different properties. That's a good point that you made. Why do we need so many divergence metric? Why can't we look at one of them is because different divergence metric offer different properties. I will talk about it, right? I mean, just after we look at this algorithm, right? Remind me, if I forget it, just remind me to bring out the, let's say, properties of at least one or two divergences here.

### 01:25:32 · Speaker 2

Thank you

### 01:25:33 · Speaker 1

But yeah, so that's the point. I mean, why do we need so many divergences? In fact, if you come up with a different divergence which has good properties, you can name it C1 divergence. That's how people have done it. Different people have come up with different divergences and called them with their own name. But you will have to ensure that these things are there. You will have to ensure that this is a convex function to be mathematically precise. This is actually a left semi-continuous function.

### 01:26:07 · Speaker 1

left semi-continuous function and also f of 0 has to be equal to 1. So convex left semi-continuous functions are with f of 0 equal to 1. So if you can come up with such a function that becomes a new divergence metric and if it has favorable properties you can use that in your generative models.

### 01:26:33 · Speaker 1

Put that back in the room

### 01:26:36 · Speaker 1

It's just that it should

### 01:26:36 · Speaker 4

It's just that it should

### 01:26:40 · Speaker 1

no we are not doing argument here anything right i mean it is optimized uh we do optimization over dfs we minimize the divergence metric no we don't we have nothing to do with f f is a f is actually a hyper parameter right you fix s yeah yeah okay choose an f divergence it has nothing to do with the optimization

### 01:27:03 · Speaker 1

It is just a definition of for the F values

### 01:27:10 · Speaker 1

Any other question here

### 01:27:15 · Speaker 1

See in practice what we do is that we actually fix an F. So I mean for instance in the naive vanilla GAN paper right they choose this F to be equal to this particular F. I wrote it no this particular F. This is this this thing.

### 01:27:32 · Speaker 1

is what they do in the nice vanilla gan

### 01:27:37 · Speaker 1

They take Jensen Shannon divergence in the the vanilla generative adversarial network they choose this f to be equal to this particular form and they may what they minimize is the Jensen Shannon divergence okay

### 01:27:54 · Speaker 1

You choose it you actually fix it you fix that you fix that uh f divergence uh and then compute and minimize uh to find a sample

### 01:28:07 · Speaker 1

Is that okay

### 01:28:16 · Speaker 1

I'm not there

### 01:28:21 · Speaker 1

Yes can I hear you

### 01:28:22 · Speaker 2

Yes yes yes

### 01:28:26 · Speaker 1

Okay any other question on the definition of

### 01:28:34 · Speaker 1

this needs uh an uninterrupted to answer this question right you know we need

### 01:28:43 · Speaker 1

40 45 minutes of uninterrupted time maybe let's just take a break uh and then get back shall we

### 01:28:54 · Speaker 1

Let's take a break now. It's 10 55 in my clock. Let's resume at 11 15.

### 01:29:02 · Speaker 1

I see you in about 14 20 minutes

### 01:51:02 · Speaker 1

Hello shall we resume

### 01:51:08 · Speaker 3

Yes

### 01:51:12 · Speaker 1

One of the most challenging parts of this online teaching is that I don't get to see you at all right I mean I all I get to see is this stupid screen and as a as a teacher I've been we would have developed this ability to look at the face of your audience and kind of mostly discern what is going on I mean are they appreciating what you are saying are they understanding what is said you know when to repeat you know when to stop

### 01:51:42 · Speaker 1

not to repeat etc the complete feedback mechanism is gone now here it is only me talking don't even know whether the people exist or not yeah it's such a challenging thing to do that online anyway okay i see a couple of hands rise uh yeah ask it

### 01:52:02 · Speaker 3

Uh so so you mentioned some properties about this f function for f divergences can you move a little up

### 01:52:11 · Speaker 1

It should be convex lower semi continuous and at zero it should evaluate to one

### 01:52:16 · Speaker 3

Uh but this is not uh uh following in this uh these three functions that we write right this F zero

### 01:52:22 · Speaker 1

Hold on I think I just thanks

### 01:52:26 · Speaker 3

It should be I think F one is a good one

### 01:52:28 · Speaker 1

F1 and F2, correct, correct. Yeah, thanks. Yeah, roof top, correct, it's correct. It should evaluate to zero at one, correct, thanks.

### 01:52:40 · Speaker 1

Okay shall we continue

### 01:52:46 · Speaker 1

Okay, see, as I said, no, the goal is now to compute this divergence between a pair of distributions when the distribution is unknown and samples are given. So here is the overall philosophy of how it is done. As I said, no, this is a recurrent theme that comes up in almost all the ML models. How is it done is the following. Now, observe that these F divergences, right, are any divergence metric. Now involves, let me not write the F.

### 01:53:16 · Speaker 1

So suppose you have let's say an integral okay

### 01:53:22 · Speaker 1

need to compute an integral of let's say some function running out of alphabets it's a statement b statement h okay let's say some function h with respect to some probability density p x p x okay if this integral has to be evaluated okay now let's say that we need to evaluate this integral

### 01:53:48 · Speaker 1

I'm gonna do like this

### 01:53:54 · Speaker 1

Okay with

### 01:53:58 · Speaker 1

PX unknown clear

### 01:54:05 · Speaker 1

I have samples from DX

### 01:54:16 · Speaker 1

Okay, now suppose you need to evaluate this sort of an integral, okay, where h is some function, h of x is some function, any function, okay, some function of x. You have some function of x and you need to integrate, evaluate this integral with px unknowns. If you don't know px, then you cannot, of course, integrate this out, right? Now, one statistical tool that can be used to do this approximately, of course, you can't evaluate it exactly.

### 01:54:46 · Speaker 1

because you don't know what pH is but it can be approximated how there is this nice theorem called law loss large numbers it would say

### 01:55:05 · Speaker 1

Right last last number says the following suppose

### 01:55:13 · Speaker 1

X one X two

### 01:55:16 · Speaker 1

to xn okay are sampled from some ps and then then to compute some

### 01:55:26 · Speaker 1

Right then

### 01:55:29 · Speaker 1

Integral

### 01:55:32 · Speaker 1

effects

### 01:55:35 · Speaker 1

DX DX

### 01:55:44 · Speaker 1

can be approximated by

### 01:55:48 · Speaker 1

limit of one by n

### 01:55:53 · Speaker 1

I is one through yen

### 01:55:58 · Speaker 1

h that is evaluated at xi where xi are samples from

### 01:56:09 · Speaker 1

This is a very strong and powerful result. What are we saying here? Please note this. Now, n goes to infinity. So we are saying, suppose you have lots of samples drawn from a distribution. Okay? Then if you want to compute this sort of an integral that can be approximated simply by taking the sample mean of all these functions, I mean all the sample mean of

### 01:56:39 · Speaker 1

the function values evaluated at all those x i's coming from v x. Now a special case of this is maybe something that all of you know right if h of x is simply equal to x then what happens then what is this

### 01:56:58 · Speaker 1

What is this thing called this is

### 01:57:00 · Speaker 2

Expectation

### 01:57:01 · Speaker 1

This is the expectation of

### 01:57:06 · Speaker 1

This is the expectation of X, right? Now in fact, this is the expectation of H of X with respect to this density pH. Okay, this is the definition. Now this is the expectation of X with respect to pH. Now this can be approximated using

### 01:57:30 · Speaker 1

This all of you know now. This is what we do in practice isn't it? If you want to know the expectation of a distribution, you just take the sample mean. What is this? This is the sample mean.

### 01:57:44 · Speaker 1

Sample mean approximates the true expectation asymptotically, which means if n is n n goes to infinity, we have enough number of samples, then sample mean can be approximated. Sorry, the true expectation can be approximated using sample means. All of you know this, right? This is called law of large numbers.

### 01:58:05 · Speaker 1

Any questions on this?

### 01:58:18 · Speaker 1

Hello am I audible

### 01:58:24 · Speaker 1

Okay, now, yeah, so why did it, so basically what did I say here that you don't have, what did we do here? Look at this, no? We have integrals. I mean, this integral is nothing but the expectation of

### 01:58:38 · Speaker 1

definition of the expectation of some function h of x with respect to px if you want to compute the expectation of a function with respect to some distribution okay without knowing the distribution but you have samples from it you can invoke large large numbers and simply compute the sample average okay over all the samples that are coming from the distribution see please note this very carefully while we do not know what the

### 01:59:08 · Speaker 1

distribution p x's we have samples from them that is exactly the scenario that we have right now with us no we we have samples from the distributions we don't have the distributions but in spite of not having the distribution we can evaluate expectations of functions of random variables with respect to the underlying distribution using sample averages

### 01:59:31 · Speaker 1

Is this clear is this idea clear

### 01:59:39 · Speaker 1

Okay, now let's come back to what we had in our mind. So we want to minimize the F divergence. We want to compute the F divergence. Now let me correct the dots. If we if I can express the F divergence, let me write that if

### 01:59:57 · Speaker 1

divergence can be expressed and be expressed

### 02:00:03 · Speaker 1

expressed in terms of

### 02:00:08 · Speaker 1

in terms of expectations

### 02:00:15 · Speaker 1

More

### 02:00:18 · Speaker 1

then then df can be computed

### 02:00:30 · Speaker 1

using

### 02:00:36 · Speaker 1

samples from

### 02:00:45 · Speaker 1

uh using um using device using two types

### 02:00:50 · Speaker 1

Yeah

### 02:00:53 · Speaker 1

Law

### 02:00:56 · Speaker 1

Large numbers

### 02:01:06 · Speaker 1

Okay, what I am saying is we want to compute the F-divergence between pair of distributions. We don't know what the underlying distributions are, but we have the samples from it. Now, we also have this nice result called law of large numbers that would say that the expectations of some functions with respect to some in underlying distributions can be computed using sample averages if we have samples from it. That's what law of large numbers says. Now, connect these two.

### 02:01:36 · Speaker 1

so that if we can somehow express the f divergence or the quantity that we want to compute in terms of expectations over pH and pH theta then we can use law of large numbers and approximate the f divergences do you agree

### 02:01:59 · Speaker 1

is exactly what we will do now now the my goal is to now cool

### 02:02:06 · Speaker 1

is to express

### 02:02:10 · Speaker 1

divergence

### 02:02:12 · Speaker 1

in terms of

### 02:02:17 · Speaker 1

expectations

### 02:02:23 · Speaker 1

Or

### 02:02:27 · Speaker 1

X and

### 02:02:31 · Speaker 1

Okay, that's what we will do. Now, unfortunately, what happens is this is not possible. You can't express the F divergence or any divergence metric in terms of expectations over P x and P theta. Okay. However, however,

### 02:02:48 · Speaker 1

We can express bounds on f divergence using expectations so let me write that

### 02:03:25 · Speaker 1

Okay, so what I'm saying, I mean, f divergence cannot directly be expressed as expectations over this, but we can express lower bounds on f divergences in terms of expectations. What do you mean by lower bound? We compute a quantity, okay, which is always greater than or equal to f divergence, okay, then this quantity can be expressed in terms of expectations, so expectations over px and p theta, okay, and then remember that finally,

### 02:03:55 · Speaker 1

want to find a g theta okay or our generator function such that this f divergence is minimized right now because we cannot compute the f divergence what we do is we carve a lower bound on the f divergence which can be computed and we minimize this lower bound instead

### 02:04:13 · Speaker 1

Does that make sense? But that's not an exact thing, right? I mean, it would have been great if we can actually minimize the F divergence itself. But we cannot minimize the F divergence directly because F divergence cannot be computed without knowing the distributions. Now what do we do? Instead of minimizing the F divergence, we minimize a lower bound on that.

### 02:04:36 · Speaker 1

Okay, we minimize a lower bound or rather we minimize a quantity that is always greater than the F divergence, right? Yeah, the F divergence, we minimize a lower bound on F divergence. And that lower bound can be expressed in terms of expectations over P x and P theta.

### 02:04:55 · Speaker 1

Is this is it here

### 02:05:05 · Speaker 1

Any questions on this? See these are very very critical and important stuff okay which is again as I said this is a recurrent theme that would keep coming so if you have questions here do ask me I'll wait for a minute.

### 02:05:21 · Speaker 1

Now this implies that instead of

### 02:05:35 · Speaker 1

Minimizing up divergence

### 02:05:38 · Speaker 1

minimize

### 02:05:46 · Speaker 1

Lower bound

### 02:05:54 · Speaker 1

Any questions on this

### 02:06:03 · Speaker 1

So don't ask me how do we do it that is what we will see but yeah on the philosophy yeah somebody

### 02:06:09 · Speaker 2

That will be an approximation right

### 02:06:12 · Speaker 1

Correct correct that will be an approximation but unfortunately that's the best that we can do

### 02:06:19 · Speaker 1

Because you know that like the fundamental problem is that we don't have access to pH and p theta, you see? If we do not have access to pH and p theta, this is the best that we can do.

### 02:06:30 · Speaker 1

But yeah what you said is true it's an approximation you will you will not get the the correct minimization of heptagons

### 02:06:42 · Speaker 1

Any yeah no case

### 02:06:45 · Speaker 4

Yeah So so if we are minimizing the lower bound does that mean it does not

### 02:06:56 · Speaker 1

All right so

### 02:06:56 · Speaker 4

Let's understand the Lord

### 02:06:58 · Speaker 1

Correct correct correct that is correct that is correct that is why no it's better to that's very good question actually you know that is why we need a tighter lower bound

### 02:06:58 · Speaker 4

She's not active

### 02:07:09 · Speaker 1

Right, I mean the tighter the boundary is, the better your model is. We will crave to have a tighter lower bound. See, if you know what a GAN is, right, generative adversarial network, you will have two networks there, right? One is the generator network that we already wrote. There will be another network called discriminator network. You are aware of it?

### 02:07:29 · Speaker 4

Yeah yeah

### 02:07:30 · Speaker 1

See that is actually to carve this lower bound. We will see that in a while. So why do we say that the discriminator has to be very good is because the lower bound that we compute has to be very tight. Otherwise, you know, it doesn't, I mean, it would be a very loose approximation which will not lead to a good generative model.

### 02:07:52 · Speaker 1

But this is the best that we can do. Why is this problem arising is because we don't know px and p theta. Since we do not have px and p theta, we need to do something. What do we do? We will carve out the lower bound on f divergence and then minimize that. Now this lower bound can be computed using the expectations over, I mean using the samples of px and p theta. That's the point.

### 02:08:21 · Speaker 1

So the lower

### 02:08:21 · Speaker 2

So the lower bound is in terms of is for the term EPX minus EP theta right

### 02:08:27 · Speaker 1

It will take that form. It will take that form of like differences in expectations. That is what we're going to show now. That's the whole result. The lower bound that we carved now, that can be expressed in terms of expectations over these two distributions that we have.

### 02:08:46 · Speaker 1

Excuse me once we express them as expectations right over these two distributions we can compute that using samples

### 02:08:55 · Speaker 1

Excellent yeah

### 02:09:00 · Speaker 1

Any other question

### 02:09:02 · Speaker 4

Yeah, sir. Sir, if you don't know P x and P theta, as you have said, we know the samples from it. And above you have applied law of large number to find the expectations using the samples. So why can't we just directly apply into KL while we calculate divergence? Like we can apply the same tactic while finding the divergence as well, right?

### 02:09:31 · Speaker 1

what i'm saying you know these divergences for instance if you take this some like Jensen channel divergence right you can't express that in terms of expectations if you can express that in terms of expectations then great but you can't the whole point is that you can't write this f divergence this this f divergence right is that this definition of f divergence in terms of expectations over p theta and px if you can then that's it i mean it's it's an exact approximate exact

### 02:10:01 · Speaker 1

computation but you cannot represent that that's the problem because of that we need to do something what do we do we cause a lower bound on a dividend which can be represented as expectations right which can be

### 02:10:18 · Speaker 1

Computer yeah that's the whole point

### 02:10:22 · Speaker 1

Understand that

### 02:10:25 · Speaker 4

So just a small extension so we can't do it because it's not a h of x right but it is it's depend because if you see the form it is very similar to expectation

### 02:10:34 · Speaker 1

Not necessarily no you have f see it is not see h of x right it is not h of p of x you see this is

### 02:10:43 · Speaker 3

Yeah exactly

### 02:10:44 · Speaker 1

Yeah, so there is there are there are ratios of densities here, right? This cannot this is not equal to, for instance, expectation of f of that with respect to p theta. This is not equal to that. Understand?

### 02:10:58 · Speaker 4

Because the it itself depends on the PN

### 02:11:00 · Speaker 1

has a dependence on p and p theta it is not equal to the expectation right we need to do something else to write it as an expectation of functions over these two distributions the way to do it is to carve a lower bound on it and then express that as uh expectation which can be computed

### 02:11:01 · Speaker 4

Definitely

### 02:11:24 · Speaker 1

Anything else anybody else

### 02:11:29 · Speaker 1

Okay, now, yeah, as I said, now the classes now will get a little denser. So please focus and know as much as possible and remember what's going on. Otherwise, you know, it's very easy to get lost. I mean, there are too many things that we will do, right? I mean, unless you know what the storyline is, you will kind of...

### 02:11:53 · Speaker 1

lose the track please focus okay so now what is what should we do we should now carve a lower bound right or let me write that expressing

### 02:12:06 · Speaker 1

Bounding BS

### 02:12:14 · Speaker 1

express in it in terms of expectations

### 02:12:31 · Speaker 1

Explications

### 02:12:50 · Speaker 1

Okay this is what we will do now

### 02:12:54 · Speaker 1

Let us start from the definition of f divergence f divergence between x and p theta given as integral

### 02:13:06 · Speaker 1

ETE topics

### 02:13:09 · Speaker 1

has computed it

### 02:13:12 · Speaker 1

ratio B x and B theta

### 02:13:18 · Speaker 1

Next

### 02:13:23 · Speaker 1

Okay this is the definition of divergence

### 02:13:33 · Speaker 1

To do this we'll have to know what is called as a

### 02:13:39 · Speaker 1

conjugate

### 02:13:43 · Speaker 1

conjugate of a convex function

### 02:13:51 · Speaker 1

Great

### 02:13:54 · Speaker 1

Now remember what we are doing we are trying to bound the f divergence and express it in terms of expectations to do this we will start with what is called as the conjugate of convex function now the thing is if f is a convex function

### 02:14:11 · Speaker 1

Next one

### 02:14:13 · Speaker 1

We call it f of u because it's

### 02:14:17 · Speaker 1

It is a scalar valued function that we are talking about here, right, in the f divergence convex function.

### 02:14:24 · Speaker 1

There it exists

### 02:14:29 · Speaker 1

There exists convex conjugate

### 02:14:37 · Speaker 1

Convex conjugate function

### 02:14:41 · Speaker 1

f star of t note that both u and t are dummy variables okay simply some variables star of t defined as follows

### 02:15:02 · Speaker 1

F star of T at a point T is given as the maximum of

### 02:15:13 · Speaker 1

mu t minus

### 02:15:16 · Speaker 1

sauce new

### 02:15:22 · Speaker 1

f of u okay this maximum is over u which is the domain of f

### 02:15:32 · Speaker 1

I will explain what this is

### 02:15:36 · Speaker 1

So what we are saying is that an every convex function f okay has what is called as a convex conjugate okay. Now what is convex conjugate? It is another function f star of t okay that is defined this way f star of t simply f star of t at t is simply the maximum of u t minus f of u where u comes from domain of f. What does that mean? Let me just draw it and show you. Let's say that you have

### 02:16:06 · Speaker 1

some convex function let us call this f of u this is a convex function right and this is axis is that this is the u axis and this is f of u okay now let's say that you take a point here some point on the u axis let me call this u okay now what i can do is i can construct like i can i can write

### 02:16:38 · Speaker 1

Multiple lines

### 02:16:40 · Speaker 1

Right

### 02:16:42 · Speaker 1

all of which are less than

### 02:16:47 · Speaker 1

F of you at that point do you agree

### 02:16:53 · Speaker 1

So given a convex function, okay, I take a value of that convex function at a point, I can construct infinite number of lines, okay, I can draw infinite number of lines that lie below that point, okay, for all u. Do you agree?

### 02:17:18 · Speaker 1

Okay, so out of those all, I mean there are infinite lines that I can draw, right? Out of all those lines, there is also this line which is the tangent.

### 02:17:35 · Speaker 1

is also the tangent okay uh that that is equal to the value of that uh function at that particular point okay now the this is this point right i mean the the intersection of that tangent and this particular curve is what i've called as maximum you look at this ut minus f of u okay for different values of t represent okay different values of u different values of

### 02:18:05 · Speaker 1

p represent all these uh lines that I can write at every point of the convex function

### 02:18:15 · Speaker 1

Let us take one point for instance. If I take one point of this convex function, there are multiple lines that I can draw to this curve at that particular point, which is represented by this family of lines. Now, amongst all these possible lines, if you take the maximum value of all these possible lines at that particular value of u, what do you get? It's actually the value of that tangent to that function at that point.

### 02:18:45 · Speaker 1

That is the value of that convex conjugate at that t.

### 02:18:50 · Speaker 1

You get it

### 02:18:52 · Speaker 2

Sir one question

### 02:18:54 · Speaker 1

It's actually not the tangent right it's actually the slope

### 02:18:58 · Speaker 1

that particular point now if you collate all these at different points of view you get another function right it's a collection of slope of this function at all points that becomes the

### 02:19:10 · Speaker 2

Sir one question

### 02:19:13 · Speaker 2

Sir, it's basically the function value f of u, right? Even if we are denoting, we are getting that through the tangent, the maximum value will be f of u only.

### 02:19:27 · Speaker 1

No, no, maximum of maximum of ut minus f of u. That's what I'm saying. Not f of u.

### 02:19:35 · Speaker 2

Oh okay, no, I'm what I'm you are explaining about this this concept, right? Like we can have infinitely possible lines at a particular you one of them will be that

### 02:19:35 · Speaker 1

Okay no I

### 02:19:45 · Speaker 1

So that are that are that are less than this at all points right

### 02:19:49 · Speaker 2

Got it got it

### 02:19:49 · Speaker 1

I thought less than that at all points. So now I'm considering out of all of those possible lines, I'm considering the one that has the maximum value of that particular u and that I'm considering as the value of that conjugate function on that particular p.

### 02:20:07 · Speaker 2

So that value is corresponding to f f star of t like that

### 02:20:13 · Speaker 1

That is that is the value of correct that is the value of s star up t at that particular point

### 02:20:20 · Speaker 1

See ut I mean f of u is a what does ut minus f of u represent f of u minus f of u right this f of u is the

### 02:20:33 · Speaker 1

Something happened

### 02:20:37 · Speaker 1

Yeah hold on this f of u is the intercept right

### 02:20:42 · Speaker 1

The given point is f of u this is this is like mx plus c isn't it

### 02:20:47 · Speaker 2

Yes sir

### 02:20:49 · Speaker 1

This is the intercept, okay? Now, you see, I mean, t is the slope and u is the value of the domain at that point. So basically, ut minus f of u will give you a line.

### 02:21:03 · Speaker 1

At any f of u, ut minus f of u will give you a line okay whose intercept is f of u

### 02:21:11 · Speaker 1

Okay

### 02:21:13 · Speaker 2

Okay

### 02:21:14 · Speaker 1

Now I'm saying out of all these possible lines that are less than the function value at that particular point, I'm looking at that line which is maximum.

### 02:21:34 · Speaker 1

Do you understand?

### 02:21:37 · Speaker 1

Oh yeah

### 02:21:39 · Speaker 4

So it lead to one confusion that the distance should be minimum right like the value at f of u and ut minus f of u the line which you have it should be very close to f of u to get

### 02:21:52 · Speaker 2

tighter bond right so it should be the line should be the minimum of it

### 02:21:57 · Speaker 1

the maximum value of the value no the maximum value of that function see we are looking at the value of this function itself for this u t minus f of f f of u is a value that evaluates to something

### 02:21:57 · Speaker 4

My duty is

### 02:22:11 · Speaker 1

So looking at the maximum of that and the maximization is over all possible u see the optimization is over the u domain you look at all possible u's here

### 02:22:25 · Speaker 1

Okay, so amongst all possible u's, you look at that u which will maximize this entire thing ut minus f of u.

### 02:22:40 · Speaker 1

Fix a t okay fix a t so what do you mean by fixing a t see you can you can see t as the slope okay you see t as the slope you fix a slope you see you fix a particular slope maybe the way I have written the figure has a different interpretation okay let me rewrite it hold on

### 02:23:12 · Speaker 1

Is it not warm

### 02:23:19 · Speaker 1

Let me draw a comment again

### 02:23:27 · Speaker 1

This is a convergent function. Let us take one particular u okay from here

### 02:23:37 · Speaker 1

the axis

### 02:23:48 · Speaker 1

P is the slope and

### 02:23:55 · Speaker 1

F of u is the intercept right

### 02:23:58 · Speaker 1

Minus f of u is the intercept so this is

### 02:24:05 · Speaker 1

This is F of U

### 02:24:11 · Speaker 1

minus f of u should come the other side

### 02:24:23 · Speaker 1

that is the intercept term now

### 02:24:35 · Speaker 1

you are looking at maximum with respect to you

### 02:24:40 · Speaker 1

Such the function, t is the slope. Now, this is you can write.

### 02:24:49 · Speaker 1

this is 1 t okay with that that has the intercept you can write

### 02:25:04 · Speaker 1

Go to that now

### 02:25:07 · Speaker 1

another line and this is

### 02:25:15 · Speaker 1

straight lines there's another line there's another line and so on these are the lines that we are talking about is this clear i think now it is correct

### 02:25:24 · Speaker 2

Yes yes sense

### 02:25:27 · Speaker 1

yeah these are use correct yes amongst all these possible lines i am looking at that particular line okay which would maximize that at that list this is the u that we are talking about

### 02:25:47 · Speaker 1

Okay, so amongst all possible lines, okay, that would be a lower bound for this function at that particular u. I am looking at

### 02:25:58 · Speaker 1

which would maximize the resistance value U t minus F of t

### 02:26:05 · Speaker 1

Is that clear

### 02:26:08 · Speaker 2

Yes sir

### 02:26:10 · Speaker 1

By the way it may not be a tangent though at all times it may not be the tangent

### 02:26:18 · Speaker 1

Okay

### 02:26:21 · Speaker 1

So this okay so you're not seeing the entire picture

### 02:26:25 · Speaker 1

So these are multiple lower bounds that are possible for that for the convex function at that particular value amongst all possible lower bounds we are looking at that possible in that line okay that would maximize this.

### 02:26:44 · Speaker 1

Are you clear on this Any questions

### 02:26:55 · Speaker 4

So the quantity which we are maximizing can you show it on graph

### 02:27:03 · Speaker 1

U is fixed U is fixed or

### 02:27:07 · Speaker 4

Thank you guys

### 02:27:10 · Speaker 1

And yeah, u t minus f of u is the line, no? This is one u t minus f of u. Let's call this t1. This is like u t2 minus f of u and so on, right? Amongst all possible lines, we are taking that line which has the maximum value.

### 02:27:31 · Speaker 1

At that you, at you

### 02:27:36 · Speaker 1

at u this line has this particular value right at u this line has this particular value and so on I can construct more such line you know which becomes lower bound if I construct another line you understood right different lines have different values at that u so now amongst all possible lines I am taking that line okay which has maximum value and the value of that line at that particular u happens to be the value of the conjugate at that t

### 02:28:08 · Speaker 1

Yeah does it make sense now

### 02:28:11 · Speaker 4

Is it the value of u that maximizes uh u of t minus f of u

### 02:28:15 · Speaker 1

minus f of u correct or a given or a given or for a given

### 02:28:19 · Speaker 4

For a given for a given for a for a given value of t right

### 02:28:25 · Speaker 4

You choose a t and then find the maximum of u uh f uh find a u that maximizes ut minus f of u

### 02:28:31 · Speaker 1

That would be the value of m star of t at that particular point okay

### 02:28:37 · Speaker 1

It's a point wise definition

### 02:28:45 · Speaker 4

So this is

### 02:28:45 · Speaker 1

So this is this has nothing to do with like you know divergences or anything. This is just the definition of a convex conjugate of any convex function. This is true for any convex function. Okay. It's also called the Fenchel conjugate. Basically the definition of the conjugate function. Okay. Shall we move on?

### 02:29:06 · Speaker 1

Okay now um

### 02:29:10 · Speaker 1

This has to be taught in a convex optimization course, but it's okay. I whatever we need, we will do it. So now.

### 02:29:21 · Speaker 1

So there is a property that would say that that f star of f star I'll state this without proof f star is also convex

### 02:29:32 · Speaker 1

star is also convex and so okay so first of all we say that f star is also convex if f star is also convex this implies that you can take the conjugate of the conjugate right because f star is conjugate now we know that every convex function has a conjugate which means that the conjugate also has a conjugate and the property there's a property that would say that the double conjugation of the function will take you to the original function

### 02:30:02 · Speaker 1

property that we will use okay so two things one f star is also convex which means that that also has a conjugate and that will take you back to the original function okay what this implies that

### 02:30:17 · Speaker 1

We have the original okay so f of t

### 02:30:24 · Speaker 1

was the conjugate for f of u right

### 02:30:33 · Speaker 1

That's the right answer maybe

### 02:30:37 · Speaker 1

2T minus

### 02:30:39 · Speaker 1

f of u and this is over u right so now this is the f star of t this is the conjugate for f right now we can take a conjugate of the conjugate f star of t you take

### 02:30:57 · Speaker 1

the conjugate of the conjugate what is this this is equal to f of u we know that okay so conjugate of conjugate how do you write that it is simply to take the

### 02:31:11 · Speaker 1

domain of the conjugate okay

### 02:31:14 · Speaker 1

and subtract it from it

### 02:31:17 · Speaker 1

its conjugate which is when I subtract it with its value and this maximization is over T which is over you know f star

### 02:31:28 · Speaker 1

Do you agree

### 02:31:32 · Speaker 1

Simply taking conjugate of the conjugate. What is the conjugate of the conjugate? Conjugate is also convex. So this is the conjugate of conjugate. So this is

### 02:31:42 · Speaker 1

the conjugate of conjugate

### 02:31:48 · Speaker 1

We know that that is equal to the original function f that's why f of u is equal to over this

### 02:31:58 · Speaker 1

Questions on this do you agree

### 02:32:10 · Speaker 1

I have just replaced f of u with f star of u because f star of u is another convex function right. We can write conjugate for any convex function f star is another convex function. So, I will write a conjugate for f star as well which is this it is this and this we know that if you take the conjugate of conjugate you get the original function. Is this clear to all of you?

### 02:32:43 · Speaker 1

Okay, okay, so now, okay, why do we need this? Let's come back to our definition of our f divergence. Remember that we are looking at bounding this f divergence, okay? Now this is integral

### 02:33:10 · Speaker 1

Right there's is

### 02:33:16 · Speaker 1

we call this as f of u dx where u

### 02:33:25 · Speaker 1

Sorry I think I wrote it incorrectly it should be P theta

### 02:33:38 · Speaker 1

Okay, so this is a convex function, which means that this f now I can replace this L let's say I use this yeah.

### 02:33:46 · Speaker 2

Yes sir either the initial one should have PX or the and the last the last one should have PX because once we replace

### 02:33:59 · Speaker 1

I can follow

### 02:34:05 · Speaker 1

Theta x times f of p x by p theta right that's the definition

### 02:34:12 · Speaker 2

Once we replace uh Px by P theta we have

### 02:34:12 · Speaker 1

Speed of place

### 02:34:15 · Speaker 1

So we have a break

### 02:34:20 · Speaker 2

So

### 02:34:21 · Speaker 1

Just called it as this ratio I called as U that's all

### 02:34:26 · Speaker 1

It's a scalar no I just called it as a scalar U f of U

### 02:34:30 · Speaker 2

Okay okay

### 02:34:34 · Speaker 1

Nothing complicated right I just am representing that as some scalar right yeah

### 02:34:38 · Speaker 2

Yes sir yes sir

### 02:34:39 · Speaker 1

Now if of you we have this result right can be written as max of

### 02:34:49 · Speaker 1

u minus

### 02:34:52 · Speaker 1

Let's start off the

### 02:34:56 · Speaker 1

Maximization is over t correct this is what we have written here

### 02:35:01 · Speaker 1

But I will use that there which means that my f divergence now can be written as an integral

### 02:35:11 · Speaker 1

times max of T okay what okay I'll write it as T U minus S star of T

### 02:35:24 · Speaker 1

P x maximization is over t agreed

### 02:35:32 · Speaker 1

What did I do? I just simply replaced f of u with the definition, okay, by using the conjugate of conjugate property.

### 02:35:43 · Speaker 1

Do you agree

### 02:35:46 · Speaker 1

This is another problem with this online teaching that the screen is so small, right? I mean, I need a large bold where, see, imagine I would have written this somewhere else, you know, you would have had the view of this. Now, you can appreciate that since I have written FRP using this max thing, all I have done is I have replaced this FRP using this, yeah, using this definition.

### 02:36:09 · Speaker 1

Is it okay

### 02:36:12 · Speaker 1

Is it

### 02:36:12 · Speaker 2

Yes it is.

### 02:36:14 · Speaker 1

Now I'll just expand this this is integral p theta of x

### 02:36:21 · Speaker 1

So we're A

### 02:36:24 · Speaker 1

Now t times what is u? u is ratio of vx by e theta

### 02:36:34 · Speaker 1

this

### 02:36:36 · Speaker 1

star of P

### 02:36:43 · Speaker 1

Correct? Yeah. Now look at these terms. Look at these terms. Okay, I'll write it as three times.

### 02:36:54 · Speaker 1

times this now look at these terms if i can somehow take this max out of the integral

### 02:37:02 · Speaker 1

Okay, if I take the match term out of the integral, what will happen?

### 02:37:08 · Speaker 1

Can somebody tell me what will happen

### 02:37:11 · Speaker 1

If I take max yeah if I take max out of the integral then it will be t times px minus the integral of so it will be like this now somehow take the max outside okay it will be integral

### 02:37:27 · Speaker 1

P theta P theta would cancel out it would be

### 02:37:33 · Speaker 1

P times X of X DX

### 02:37:38 · Speaker 1

Correct minus

### 02:37:42 · Speaker 1

Integral

### 02:37:47 · Speaker 1

star of T times

### 02:37:50 · Speaker 1

ET topics correct do you agree

### 02:37:56 · Speaker 1

Can you see that?

### 02:38:03 · Speaker 1

Can we take that

### 02:38:04 · Speaker 2

X out

### 02:38:05 · Speaker 1

are hold on I'm just saying if you can I mean you can't I will tell you how what happens if you take the max out but if you can let's say right then it will become like this now this is an expectation right over px and this is an expectation over p theta you understand that that's all now all this exercise that we did right in representing the f function using its conjugate all that was to ensure that we can somehow write the x

### 02:38:35 · Speaker 1

these in terms of expectations. Now we are almost there. We just have to somehow push this max out. And if we can push this max out, then we achieve whatever we want, that we can write our F divergence in terms of differences in expectations over P x and P theta, which we know how to compute. And you see the point?

### 02:38:57 · Speaker 1

Now the question is how can you take the max out

### 02:39:02 · Speaker 1

Right So max is over a T how can you take the max out is the question

### 02:39:08 · Speaker 1

So that needs I need some half an hour to complete this proof now. So what shall we do?

### 02:39:18 · Speaker 1

We have uh

### 02:39:23 · Speaker 2

Sir we have time until 1215

### 02:39:26 · Speaker 1

will obtain ten more words

### 02:39:30 · Speaker 1

minutes might be lesser to do this anyway i will quickly run through it and do it again in the next class perhaps okay

### 02:39:41 · Speaker 1

Any questions so far?

### 02:39:53 · Speaker 1

Does anyone have any question? Okay no okay now okay so let us observe this entire thing

### 02:40:04 · Speaker 1

So this is a maximization

### 02:40:12 · Speaker 1

Okay well what

### 02:40:18 · Speaker 1

Can you see that this is a maximization over t okay however however

### 02:40:28 · Speaker 1

So let us call this uh maximization over okay maximization of let me say that of

### 02:40:40 · Speaker 1

an objective function okay

### 02:40:44 · Speaker 1

objective function let me call that function as capital T can of a function T over T do you agree so this I mean whatever I have marked using flaw bracket right it is a maximization that you are that you are that an optimization that you are solving over T as the variable and if I call that entire function that you are optimizing using the capital T

### 02:41:14 · Speaker 1

Okay, then it's you are maximizing capital T over the variable small t. Do you agree?

### 02:41:25 · Speaker 1

Or I can use a different notation for this capital D you know because I'm using small d capital D it might confuse which letter

### 02:41:40 · Speaker 1

was a lot of alphabets

### 02:41:48 · Speaker 1

U is taken

### 02:41:51 · Speaker 1

Okay we'll call it B

### 02:41:55 · Speaker 1

capital V. This function capital V, okay, we want to optimize, okay, what is V by the way?

### 02:42:06 · Speaker 1

v is equal to t times

### 02:42:11 · Speaker 1

x of x divided by h theta of x minus f star of t, correct? This is what I have called as v. Agreed? It's a maximization of an objective function v over t. All of you see that? But observe this, that this v is actually a function of x as well.

### 02:42:39 · Speaker 1

But I should say that it's a function of both x and t

### 02:42:45 · Speaker 1

It's a function of x and t it's also a function of x agreed

### 02:42:51 · Speaker 1

Now what you are actually doing while you are computing this integral is this following. You first solve this optimization problem over t. Okay. So now what you do is inner

### 02:43:05 · Speaker 1

optimization problem so now first you do solve this optimization problem you get a you get a let's say

### 02:43:14 · Speaker 1

the star okay which is the maximum

### 02:43:20 · Speaker 1

of this function v x comma t over all t okay now you plug this t star here and compute this integral and do it for all x that is what you are doing when you are computing the integral

### 02:43:40 · Speaker 1

You first solve the optimization problem with respect to T, you get some, some.

### 02:43:46 · Speaker 1

value for that optimization problem now you take that so now observe that this t star okay is also a function of x

### 02:44:02 · Speaker 1

Do you agree

### 02:44:05 · Speaker 1

Obviously, right, because if v is a function of x, then t star is also a function of x, because we are only solving, we are only taking the maximum with respect to t, and given a particular x, you will have a different maximum, correct?

### 02:44:21 · Speaker 1

Let us represent that maximum using some capital D star of x

### 02:44:28 · Speaker 1

Correct. Okay. Now, what are we saying here that there is an optimization problem? There is an optimization that is happening with respect to t. Okay. Now, that objective function for that optimization problem is a function of x. Now, given an x, you will have a particular maximum for this maximization problem. You compute that maximum and then you integrate for all x. That is what your f divergence is. Agreed?

### 02:45:00 · Speaker 1

Now now what I can do is suppose I take the maximization out and write that whatever is there you know p theta of x times

### 02:45:19 · Speaker 1

theta of x divided by x of x minus

### 02:45:25 · Speaker 1

instead of the

### 02:45:41 · Speaker 1

Suppose right I take this

### 02:45:48 · Speaker 1

Replace this with

### 02:45:52 · Speaker 1

See star of X

### 02:46:02 · Speaker 1

It is the maximum of

### 02:46:06 · Speaker 4

So that way px by p theta right t star of x into px by p theta

### 02:46:12 · Speaker 1

Is it px almost made this mistake yeah it's px by p data sorry

### 02:46:19 · Speaker 1

Now, suppose I replace this, you know, this t, right? I solve this optimization problem and replace it with t star of x. Then it's okay, no? Both the integrals are okay. I can take out d max. Do you agree? Because I'm solving the optimization problem in EMA, right? At all points in x, I'm taking out, I'm finding solving that optimization problem.

### 02:46:43 · Speaker 1

Replacing that t with t star of x, correct? That's okay, no?

### 02:46:55 · Speaker 1

Do you agree what I am doing here at all is I am simply solving the inner optimization problem and putting the solution for it and then computing the integral

### 02:47:05 · Speaker 1

Great now

### 02:47:10 · Speaker 1

This t star of x basically let's say that, okay, it's a function that will take a particular value of x and gives you what a real number, isn't it? A real number which happens to be the solution, solution for the optimization problem.

### 02:47:33 · Speaker 1

No optimization problem

### 02:47:46 · Speaker 1

But what should be this t star of x b t star of x is a function that would take x you give it an x it will give the solution for the inner optimization problem correct

### 02:47:58 · Speaker 1

Thank you everybody

### 02:48:00 · Speaker 1

This T star of X has to be this right, you look at this by definition, it should be a function that would take an X and gives you the solution for the optimization problem.

### 02:48:12 · Speaker 1

Okay now

### 02:48:20 · Speaker 1

Any questions so far?

### 02:48:34 · Speaker 1

Okay, now instead of T star, okay, instead of T star,

### 02:48:44 · Speaker 1

Okay before that let let let script be

### 02:48:55 · Speaker 1

This is a different symbol okay it's denoted denoted

### 02:49:01 · Speaker 1

A class of functions

### 02:49:07 · Speaker 1

of functions okay

### 02:49:11 · Speaker 1

Bottom

### 02:49:13 · Speaker 1

to R. Basically what I am saying is let capital let script T this is script T okay let script T denote a class of functions from X to R okay which means that this T star of X T star of X is a member of capital T okay.

### 02:49:33 · Speaker 1

star of x is one member of capital T which means that it is a function that would take x and gives you a real number which is a solution for the inner optimization problem at all x okay but scripty let scripty denote all possible functions that will take an x and gives you a real number okay now if I cannot

### 02:49:57 · Speaker 1

Let me write that integral down and then I will tell you this fx

### 02:50:03 · Speaker 1

t of x minus

### 02:50:10 · Speaker 1

is t what is that e theta

### 02:50:13 · Speaker 1

That's the second term

### 02:50:17 · Speaker 1

ETOPICS times

### 02:50:21 · Speaker 1

B of X times

### 02:50:25 · Speaker 1

theta of x by x of x minus f of the f star of the f star f star of t of x

### 02:50:38 · Speaker 2

So P x of x divided by P theta of x

### 02:50:44 · Speaker 1

Every time I make that mistake

### 02:50:51 · Speaker 1

Now let's say that let there is a Tx, okay, which is not equal to p star of x, okay?

### 02:51:03 · Speaker 1

I replace this with this so this suppose suppose

### 02:51:09 · Speaker 1

T x is another function okay that belongs to script t and I replace this t star of x by t of x. What do you think okay will be the value of this integral compared to

### 02:51:28 · Speaker 1

disintegral and somebody tell me

### 02:51:32 · Speaker 1

You understand, instead of having t star of x, which gives me a solution for the inner optimization at all points of x, if I replace that with another function t of x, what would that be?

### 02:51:48 · Speaker 2

It slightly be smaller than the previous one

### 02:51:50 · Speaker 1

will be smaller do you agree

### 02:51:54 · Speaker 1

It will be this will be this will be greater than or equal to

### 02:52:03 · Speaker 1

Or this is our f divergence this will always be greater than or equal to f divergence

### 02:52:13 · Speaker 1

Because

### 02:52:19 · Speaker 1

It will be either equal to d of x or less than d of x. They're not equal to d of x.

### 02:52:23 · Speaker 2

Sir other way around right we like t star is corresponding to the maximum value

### 02:52:29 · Speaker 1

Max p star is corresponding to the max so this is lesser and rp everything here all of these are density functions that are positive so p is p is lesser p can be lesser at all points which means that yeah it's the other way around should be you know

### 02:52:46 · Speaker 1

is that this is greater correct so lower bound no correct is that okay

### 02:52:54 · Speaker 2

Yes sir

### 02:52:54 · Speaker 1

It's correct now this integral is over x. Now now I can say that dx is greater than or equal to the maximum value okay that you can get.

### 02:53:10 · Speaker 1

out of all Tx that belongs to this class of functions of this particular integral

### 02:53:27 · Speaker 1

lying this

### 02:53:30 · Speaker 1

This is P x no because e theta would cancel out

### 02:53:36 · Speaker 1

Temple

### 02:53:40 · Speaker 1

E theta X

### 02:53:43 · Speaker 1

BX BX

### 02:53:48 · Speaker 1

Is this a, do you agree? Why have I written a max here? The reason I have written a max here is that if you take the max of all possible functions in this bucket of functions, okay, your f divergence will be greater than or equal to that. Now, if you can find a function with the bucket of all these functions that is equal to t star of x at all points, then it is exact. The f divergence will be exactly equal to this integral, right?

### 02:54:18 · Speaker 1

okay now if you cannot find a function okay that is equal to t star of x at all point at least find a function okay that will give you the maximum value at all possible x amongst t if there can be let's say that there is one t of x there is another t2 of x there is t3 of x and all that right let's say that none of these are equal to t star of x okay however i would choose that t okay amongst t1 t2 t3 t3 okay

### 02:54:48 · Speaker 1

That is maximum of all this, correct? Of course, I need to choose the maximum because here the inner optimization problem, I am actually looking at, if you look at the definition of T star, it is actually the maximum of this objective function with respect to T. Now, if I cannot find the maximum

### 02:55:07 · Speaker 1

I mean at all points

### 02:55:10 · Speaker 1

Rather if I cannot find a function that will give me the maximum at all points I would choose the function amongst all possible functions that are there in this pocket of t I would choose the one with the maximum value

### 02:55:22 · Speaker 1

Do you agree

### 02:55:29 · Speaker 1

That's all, we are done. I mean, I will reiterate over this the next class. So, what we basically did was, we expressed this expectation, okay, sorry, the f divergence, we carved a lower bound on this, by saying that you choose a class of functions, okay, from a bucket of functions, this is equal to, what is this first term? It's pretty obvious now. This is an expectation of p of x with respect to p x, okay, minus, this is an expect

### 02:55:59 · Speaker 1

of sorry this should be

### 02:56:04 · Speaker 1

Nobody corrected me this is S star of T of X

### 02:56:18 · Speaker 1

Let me call this x cap because when you write expectations, no, it's better to write a different w variable. This is x coming from px. This is the expectation of x cap coming from p theta.

### 02:56:32 · Speaker 1

That's all. This is the result. But this is the last function in AGAN. If you can, if people know, if you can relate, now this is exactly the last function in AGAN. I will, we will see that in detail next class. That's all. We are done. So now we have re-expressed. So basically what we have done, we have expressed.

### 02:56:53 · Speaker 1

expressed.

### 02:56:56 · Speaker 1

the lower bound on H divergence

### 02:57:02 · Speaker 1

on a divergence in terms of

### 02:57:08 · Speaker 1

expectations

### 02:57:13 · Speaker 1

or unknown distributions

### 02:57:24 · Speaker 1

This is the goal, right? We have achieved our goal. So now we know how to compute, do we know how to compute the first term? We do log large numbers because we have samples from p x. Do we know how to compute the second term? We do because we have samples from p theta. Now if you observe this entire thing now will become a function of theta, right? Because this second expectation is a function of theta. Now you don't forget what we have been doing, right? We have this network d theta whose parameters are theta. We are giving the random

### 02:57:54 · Speaker 1

z okay this x cap the output of this is called as p theta and we have a lot of samples from p theta and that's what we use to compute the second expectation we use our data to compute the first expectation and then we optimize this using Gaussian which we will see in the next class but for today's class what did we do we wanted to minimize the up divergence we could not because we don't know the underlying distributions the goal was to represent the unknown

### 02:58:24 · Speaker 1

divergence are uncomputable divergence measure in terms of expectations over underlying distributions because we know how to compute expectations using laplace numbers we invoke the property of convexity and conjugates to express the the f divergence in terms of expectations over underlying distributions

### 02:58:48 · Speaker 1

all we did so far okay so before coming to the next class as i said no that things are getting more intense and involved please go through this this content right i mean whatever we did in today's class go through that once and if you have questions you can ask me or tas either on the whatsapp group or on teams and you also look at the notes that i've given you the handwritten notes uh this time i've kind of swapped swapped the order i used to

### 02:59:18 · Speaker 1

if A is first and GANS then now I have swapped the order this way started from the GAN so it is the lecture four in my notes lecture four in the handwritten notes

### 02:59:34 · Speaker 1

I have shared that with you please have a look at it and also read the paper the paper that I am following is that

### 02:59:43 · Speaker 1

Radiational divergence minimization. Let me just tell you the name of the paper. It is there in my handwritten notes.

### 02:59:52 · Speaker 1

Is called f gyan okay which is a generalization of all gyan so it is called f gyan

### 02:59:59 · Speaker 1

Fine

### 03:00:02 · Speaker 1

Generative neural samples

### 03:00:06 · Speaker 1

Title of the paper okay

### 03:00:12 · Speaker 1

You'll see

### 03:00:14 · Speaker 1

Variational divergence minimization

### 03:00:23 · Speaker 1

This is the paper that I am going through, okay? Meaning, this is what I have, like, I have, of course, created my own narrative, but this is the paper. So it is there in my handwritten notes. Please go through the handwritten notes once and also go through whatever has been covered in this class and come prepared, please. If you have questions, of course, you can ask me, but no, do prepare and come back. It will be, yeah, we will continue from here. I'll redo what

### 03:00:53 · Speaker 1

Whatever I did this time okay

### 03:00:57 · Speaker 1

This I will redo but yeah I will look at it and come back okay

### 03:01:05 · Speaker 1

That's all for today then so for people who are celebrating happy 10th anniversary so we can wait next class next uh

### 03:01:14 · Speaker 4

So just one question um for this uh theory that you covered any reference material that we can refer to

### 03:01:20 · Speaker 1

gave you no that's exactly what I

### 03:01:22 · Speaker 4

No no no no I mean especially on this convex optimizations and and such stuff if you have anything handy

### 03:01:28 · Speaker 1

Convex optimization is a standard stuff even Wikipedia says the convex conjugate and the convex functions.

### 03:01:38 · Speaker 1

Yeah, any convex optimization book would do, but you don't need I mean, we are not doing convex optimization here, right? Beyond just defining the conjugates, we are not doing anything. So that I think, you know, standard articles in Wikipedia would suffice.

### 03:01:53 · Speaker 4

Okay and the uh the paper that you referred I think that that would be good for reference

### 03:01:59 · Speaker 1

And my I have I have given you some references in my handwritten notes. So now please have a look at it. For instance, right, I mean the final conjugates and the related stuff, no, I have put in some of the references at the end of my handwritten notes. Start reading them.

### 03:02:19 · Speaker 1

Okay, anything else?

### 03:02:22 · Speaker 4

I just want other questions sir sir this uh quiz will be on Moodle or

### 03:02:26 · Speaker 1

No no no we will do it on this thing uh Microsoft forms okay we will not use the models

### 03:02:34 · Speaker 1

We will let you know okay again you know we will intimate that in teams and whatsapp

### 03:02:42 · Speaker 1

Okay, thank you then. We will see also let me know if you think that you know that I mean class is too intense or you want some other change, et cetera, you have that anonymous feedback form that is there in on my webpage. You can express your thoughts. When you are writing, please mention that you like you are from the online version of the course. That's all. So that I know in where to implement the change. And of course, it's anonymous. You don't have to put your name or anything, but just mention that

### 03:03:12 · Speaker 1

This is from the online student and you can just put in your thoughts if you have if you need any change in the way things are going okay

### 03:03:22 · Speaker 1

Okay, see you next week

### 03:03:25 · Speaker 4

Think as a my

### 03:03:27 · Speaker 4

Thank you sir
