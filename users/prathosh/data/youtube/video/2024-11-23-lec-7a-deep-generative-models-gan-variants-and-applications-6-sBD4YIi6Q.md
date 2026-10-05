---
id: 6-sBD4YIi6Q
title: Lec 7a - Deep Generative Models GAN variants and Applications
date: '2024-11-23'
url: https://www.youtube.com/watch?v=6-sBD4YIi6Q
description: ''
author: prathoshap5226
duration: 00:12:00
model: saaras:v3
transcript: true
---

# Lec 7a - Deep Generative Models GAN variants and Applications

## Transcript

### 00:00:13 · Speaker 1

Yeah, so this is the

### 00:00:14 · Speaker 3

the uh uh objective. You have to learn a function from the data space to some space V such that some downstream tasks such as classification supervised classification are easier in terms of requiring lesser supervision or being more robust on Z than on X. So this is the goal.

### 00:00:37 · Speaker 3

Okay. See we have already seen learning some of these Zs, right? For instance, uh the latent vectors that we get from the latent space of VAE is one such function that we already have. I mean this F theta is the encoder of a VAE, PQVAE for instance. And if you try now DDPM, DDIM, right? The inverted samples are another example, right? But those are uh the generative way of finding out the Z.

### 00:01:07 · Speaker 3

In fact, uh this guy Yanlikun was there in India, right? A couple of weeks before, he gave multiple talks. So one of his favorite slides is where he says that, uh I mean this is called representation learning, right? I mean learning a transformation or a projection of data onto some latent space such that the data is represented better is what is called as representation learning. There are two ways to do it. One is the way of way of generative representation learning where you build a

### 00:01:37 · Speaker 3

generative model that involves a latent space like a V A E. The latent space of that generative model itself will become representation for data.

### 00:01:49 · Speaker 3

Right? So that is one way to do it. There's another way to do it, which is the self-supervised learning way. And the self-supervised learning way, you know, is not generative.

### 00:02:00 · Speaker 3

Is that okay? So I'll write that once. Learning representations.

### 00:02:07 · Speaker 3

Bernard

### 00:02:08 · Speaker 1

f theta which is which is what I call as representations

### 00:02:20 · Speaker 1

can be done in two ways.

### 00:02:31 · Speaker 1

one is the generative way

### 00:02:38 · Speaker 1

where

### 00:02:42 · Speaker 1

Infocity learn a latent latent generative model

### 00:02:50 · Speaker 1

so on the latent kin writing model

### 00:03:15 · Speaker 1

We have seen this already, right? The example is

### 00:03:18 · Speaker 3

that can use the encoder of a VAE

### 00:03:23 · Speaker 3

as the representation. This is one way to do it. The other way to do it, which we will see now, is the self-supervisor.

### 00:03:31 · Speaker 2

which

### 00:03:32 · Speaker 2

Turning way, okay?

### 00:03:41 · Speaker 2

supervisor

### 00:03:42 · Speaker 3

where the idea is that see here what are we doing right we are learning we are we are we are learning to sample from the underlying distribution using a latent variable model okay and the latent space basically what you do here is do a do a posterior inference right posterior inference is what is what we are calling as representations right so now in self supervised learning what is done is define

### 00:04:11 · Speaker 1

pretext tasks. Okay.

### 00:04:18 · Speaker 1

using pseudo labels.

### 00:04:26 · Speaker 1

and use the

### 00:04:38 · Speaker 1

use the representations.

### 00:04:45 · Speaker 1

given by

### 00:04:49 · Speaker 1

ಈ ಪ್ರೀಟೆಕ್ಸ್ಟ್ ಟಾಸ್ಕ್ ಸಾಲ್ವರ್ ನೆಟ್ವರ್ಕ್

### 00:04:59 · Speaker 2

So

### 00:04:59 · Speaker 3

So what is the idea? The idea is let's say that you are given some images, okay? So you build a neural network, okay? Call this as F theta. What this would do is take an image, okay? And like take its rotation, let's say.

### 00:05:17 · Speaker 3

Okay, and this network would simply

### 00:05:19 · Speaker 2

predict

### 00:05:24 · Speaker 2

the rotation angle

### 00:05:29 · Speaker 2

train this

### 00:05:31 · Speaker 3

network to predict the rotation angle and take the penultimate layer of that as your Z

### 00:05:39 · Speaker 3

That is what I'm trying to say. This is one of the pretext task. The other can be take this

### 00:05:45 · Speaker 3

okay, and take a

### 00:05:48 · Speaker 3

take noise, okay? and build a network

### 00:05:57 · Speaker 2

that would classify between this and this.

### 00:06:01 · Speaker 2

and use the representations of that as you will see. This is classified.

### 00:06:09 · Speaker 2

between noise and data.

### 00:06:16 · Speaker 3

So what is shown is that if you solve like pseudo tasks like this you know these are called the self supervised tasks basically you you are given data create some pseudo tasks using self supervision right? And a network that would solve those self supervised tasks they are shown to have properties right or representations that are very strong in in in solving the underlying

### 00:06:46 · Speaker 3

downstream task, right? I mean, it will learn the underlying distribution is, uh, is, is, is what, uh, has been shown. So the question is, I mean, two things. One,

### 00:07:00 · Speaker 3

Why should this work? Right? I mean, why should solving these kinds of pseudo tasks should should give you good representations of the data? So that is the first question that we will be asking. Okay? The second question that we will be asking is, what are the ways to define some of these pseudo tasks, okay, self-supervised tasks, so that they give you a very good representation? We'll answer both of these questions in the next class.

### 00:07:27 · Speaker 3

Any questions on this?

### 00:07:30 · Speaker 0

So we use the same network to learn or I mean for this multiple pretest tasks or it's a different network.

### 00:07:39 · Speaker 3

Yeah, those I mean we'll discuss all that in the next class, right? I mean there are multiple ways. I mean empirically, right? Some people use the same network, some people use different networks and and lot of other things are done. We will discuss all of these.

### 00:07:57 · Speaker 0

Okay, so just one question. So, uh, which of these is preferable? Which of these two methods?

### 00:08:03 · Speaker 3

will as I said no all of these will be answered in next class I mean I just gave you two examples see there is the other example is

### 00:08:11 · Speaker 3

that you construct a kind of model, take the image, okay? And like just mask it.

### 00:08:14 · Speaker 2

Classified

### 00:08:16 · Speaker 2

image

### 00:08:22 · Speaker 3

and reconstruct the image back. This is called the Mast auto encoding. This is what is used in bird kind of models, right? This is

### 00:08:30 · Speaker 0

sentence prediction

### 00:08:32 · Speaker 3

Yeah, same thing, right? I mean, there is the mass auto encoding for image based models has been. There are this is these are examples. This is like in paint.

### 00:08:44 · Speaker 3

in painting, right? Or filling the gaps.

### 00:08:52 · Speaker 3

There are multiple hundreds of ways of defining pre-text tasks. Different people have different ideas generated in come up with different pre-text tasks and all of them have different performances. JEPA is one one one other way to do it. In fact, what is done in JEPA is that they take an image, okay? And they randomly take some parts of the image, okay? And call

### 00:09:00 · Speaker 2

different people different

### 00:09:22 · Speaker 3

it as context and give that as an input to a network, okay, and randomly take some other patches and call that as target. So the task that they solve is given the context, they want to predict the target.

### 00:09:34 · Speaker 3

See the basic idea is the following right. So if you can

### 00:09:40 · Speaker 3

fill in the blanks. Okay. The only way to fill in the blanks is to understand the underlying semantics, that's all.

### 00:09:48 · Speaker 3

that is the whole idea. I mean there is a very nice mathematically grounded uh treatment of why all of these should work. This is something called noise contrast estimation or N C E. We will see that, okay? We will see uh why should these kinds of ideas work in the next class and there are hundreds of ways to do this. Okay, JEPA is one of the uh ways to do it, uh which we will see in the next class.

### 00:10:15 · Speaker 1

Okay

### 00:10:31 · Speaker 1

ओके, सो, इट इज फॉर

### 00:10:33 · Speaker 3

today then. uh we'll assume the next week. next week there will be a quiz uh and next to next week we'll do a hybrid class, okay?

### 00:10:46 · Speaker 2

ओके सर। थैंक यू।

### 00:10:47 · Speaker 3

Okay then. Yeah, so again once again happy Diwali to all of you. Yeah. So today today today should have been a holiday, no? I don't know why she didn't make a holiday. Okay, thanks for coming.

### 00:11:00 · Speaker 2

Pound Press

### 00:11:03 · Speaker 3

You might have heard some noise etcetera right today because you know I am also traveling and not sitting in my home office so yeah excuse me for that. Okay see we will we'll catch up next week. Bye bye.

### 00:11:17 · Speaker 2

Thank you sir

### 00:11:18 · Speaker 0

Thank you, sir.

### 00:11:18 · Speaker 1

Thank you sir. Happy New Year.
