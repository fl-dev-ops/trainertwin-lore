---
id: 6-sBD4YIi6Q
title: Lec 7a - Deep Generative Models GAN variants and Applications
url: https://www.youtube.com/watch?v=6-sBD4YIi6Q
date: '2024-11-23'
duration: 00:12:00
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 3
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
---

# Lec 7a - Deep Generative Models GAN variants and Applications

## Transcript

### 00:00:13 · Speaker 1

Yeah so this is the uh uh

### 00:00:17 · Speaker 1

objective. You have to learn a function from the data space to some space Z such that some downstream tasks such as classification, supervised classification are easier in terms of requiring lesser supervision or being more robust on Z than on X. So this is the goal.

### 00:00:38 · Speaker 1

See we have already seen learning some of these z's right for instance uh the latent vectors that we get from the latent twist of vae it's one such function that we already have they mean this f theta is the encoder of a vae pq vae for instance and if you try in a ddpm dd im right the inverted samples are another example right but those are uh the generative way of finding out the z

### 00:01:07 · Speaker 1

In fact, this guy, Jan Likun, was there in India, right, a couple of weeks before he gave multiple talks. So one of his favorite slides is where he says that, I mean, this is called representation learning, right? I mean, learning a transformation or a projection of data onto some latent space such that the data is represented better is what is called as representation learning. There are two ways to do it. One is the way of generative representation learning where you build a

### 00:01:37 · Speaker 1

The generative model that involves a latent space like a VAE the latent space of that generative model itself will become representation for data

### 00:01:49 · Speaker 1

So that is one way to do it. There is another way to do it, which is the self-supervised learning way. And the self-supervised learning way is not generative.

### 00:02:00 · Speaker 1

Is that okay So I'll write that one So learning representations

### 00:02:07 · Speaker 1

running f theta which is which is what I call as representations

### 00:02:20 · Speaker 1

can be done in two ways

### 00:02:31 · Speaker 1

One is the denotative way

### 00:02:38 · Speaker 1

And

### 00:02:42 · Speaker 1

Implicitly learn a latent latent generating model

### 00:02:50 · Speaker 1

latent generating model

### 00:03:15 · Speaker 1

We have seen this already right the example is that can use the encoder of a BAE

### 00:03:23 · Speaker 1

as the representation this is one way to do it the other way to do it which we will see now is the self supervised learning way okay

### 00:03:41 · Speaker 1

supervised learning where the idea is that see here what are we doing right we are learning we are we are we are learning to sample from the underlying distribution using latent variable model okay and the latent space basically what you do here is do a do a posterior inference right posterior inference is what is what we are calling as representations right so now in self supervised learning what is done is define

### 00:04:11 · Speaker 1

Three text tasks

### 00:04:18 · Speaker 1

Bringing pseudo labels

### 00:04:27 · Speaker 1

And use the

### 00:04:38 · Speaker 1

use the representations

### 00:04:45 · Speaker 1

Given y

### 00:04:49 · Speaker 1

The pretext task solver network

### 00:04:59 · Speaker 1

So what is the idea the idea is let's say that you are given some images okay so you build a neural network

### 00:05:07 · Speaker 1

this as f theta what this would do is take an image and like take its rotation let's say

### 00:05:17 · Speaker 1

And this network would simply predict

### 00:05:24 · Speaker 1

The rotation angle

### 00:05:29 · Speaker 1

Okay try in this network to predict the rotation angle and take the penultimate layer of that as your Z

### 00:05:39 · Speaker 1

That is what I'm trying to say. This is one of the pretext tasks. The other can be take this

### 00:05:45 · Speaker 1

and take a

### 00:05:48 · Speaker 1

Uh big noise

### 00:05:52 · Speaker 1

and build a network

### 00:05:57 · Speaker 1

That would classify between this and this

### 00:06:01 · Speaker 1

And use the representations of that as you will see this is classify

### 00:06:09 · Speaker 1

between noise and data

### 00:06:16 · Speaker 1

So what is shown us that if you solve like pseudo tasks like this, you know, these are called the self supervised tasks. Basically, you are given data, create some pseudo tasks using self supervision, right? And a network that would solve those self supervised tasks, they are shown to have properties, right? Or representations that are very strong in solving the underlying

### 00:06:46 · Speaker 1

uh downstream task right i mean it'll learn the underlying distribution is uh is is what uh has been shown but the question is i mean two things one

### 00:07:00 · Speaker 1

Why should this work? I mean, why should solving these kinds of pseudo tasks should give you good representations of the data? So that is the first question that we will be asking. The second question that we will be asking is, what are the ways to define some of these pseudo tasks, self-supervised tasks, so that they give you a very good representation? We'll answer both of these questions in the next class.

### 00:07:27 · Speaker 1

Any questions on this?

### 00:07:30 · Speaker 2

So we use the same network to learn or I mean for this multiple pre-text tasks or it's a different network

### 00:07:40 · Speaker 1

Yeah, those, I mean, I will discuss all that in the next class, right? I mean, there are multiple ways. I mean, empirically, right? Some people use the same network, some people use different networks, and then a lot of other things are done. We will discuss all of these.

### 00:07:57 · Speaker 2

Okay, so just one question. So which of these is preferable which of these two methods?

### 00:08:03 · Speaker 1

will as I said no all of these will be answered in the next class I mean I just gave you two examples see there is the other example is

### 00:08:11 · Speaker 1

that you construct a

### 00:08:14 · Speaker 2

Perfectly

### 00:08:14 · Speaker 1

And I'm using the kind of model take the image

### 00:08:18 · Speaker 1

and like just mask it

### 00:08:22 · Speaker 1

And reconstruct the image back this is called the masked autoencoding This is what is used in bird kind of models, right? This is

### 00:08:30 · Speaker 2

To a sentence prediction

### 00:08:33 · Speaker 1

Same thing, right? I mean, there is the mask auto encoding for image based models as well. There are, this is, these are examples. This is like in print.

### 00:08:44 · Speaker 1

painting right or filling the graphs

### 00:08:52 · Speaker 1

There are multiple hundreds of ways of uh

### 00:08:57 · Speaker 1

Defining pretest pretest tasks so when different people have different they generated in come up with different pretest tasks and all of them are different

### 00:09:00 · Speaker 2

Different people speak different languages

### 00:09:06 · Speaker 1

uh uh performances JPA is one one one other way to do it in fact what is done in JPA is that they take an image okay and they

### 00:09:18 · Speaker 1

randomly take some parts of the image and call that as context and give that as an input to a network and randomly take some other patches and call that as target. So the task that they solve is given the context, they want to predict the target.

### 00:09:34 · Speaker 1

See, the basic idea is the following, right? So if you can

### 00:09:40 · Speaker 1

in the blanks okay the only way to fill in the blank blanks is to understand the underlying semantics that's all so that is the whole idea and there is a very nice mathematically grounded uh uh uh treatment of why all of these should work this is something called noise contrastive estimation or nce we will see that okay we will see uh why should these kinds of ideas work in the next class and there are hundreds of ways to do this okay jeppa is one of the

### 00:10:10 · Speaker 1

uh ways to do it huh we will which we'll see in the next class

### 00:10:31 · Speaker 1

Okay, so that's it for today then

### 00:10:35 · Speaker 1

I will assume the next week. Yeah, next week there will be a quiz. And next to next week, we'll do a hybrid class. Okay.

### 00:10:47 · Speaker 1

okay yeah so again once again happy Diwali to all of you yeah so today should have been a holiday no I don't know why I should they didn't make it a holiday and okay thanks for coming

### 00:11:03 · Speaker 1

You might have heard some noise, et cetera, right? Today, because I am also traveling and not sitting in my home office. So, yeah, excuse me for that. Okay, see, we will catch up next week.

### 00:11:17 · Speaker 2

Thank you

### 00:11:18 · Speaker 3

I'm sorry I'm sorry
