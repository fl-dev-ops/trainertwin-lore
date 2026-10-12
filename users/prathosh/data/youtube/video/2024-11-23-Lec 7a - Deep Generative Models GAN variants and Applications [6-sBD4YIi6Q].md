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


### Speaker 1

Yeah so this is the uh uh


objective You have to learn a function from the data space to some space Z such that some downstream tasks such as classification supervised classification are easier in terms of requiring lesser supervision or being more robust on Z than on X So this is the goal


See we have already seen learning some of these zs right for instance uh the latent vectors that we get from the latent twist of vae its one such function that we already have they mean this f theta is the encoder of a vae pq vae for instance and if you try in a ddpm dd im right the inverted samples are another example right but those are uh the generative way of finding out the z


In fact this guy Jan Likun was there in India right a couple of weeks before he gave multiple talks So one of his favorite slides is where he says that I mean this is called representation learning right I mean learning a transformation or a projection of data onto some latent space such that the data is represented better is what is called as representation learning There are two ways to do it One is the way of generative representation learning where you build a


The generative model that involves a latent space like a VAE the latent space of that generative model itself will become representation for data


So that is one way to do it There is another way to do it which is the self supervised learning way And the self supervised learning way is not generative


Is that okay So Ill write that one So learning representations


running f theta which is which is what I call as representations


can be done in two ways


One is the denotative way


And


Implicitly learn a latent latent generating model


latent generating model


We have seen this already right the example is that can use the encoder of a BAE


as the representation this is one way to do it the other way to do it which we will see now is the self supervised learning way okay


supervised learning where the idea is that see here what are we doing right we are learning we are we are we are learning to sample from the underlying distribution using latent variable model okay and the latent space basically what you do here is do a do a posterior inference right posterior inference is what is what we are calling as representations right so now in self supervised learning what is done is define


Three text tasks


Bringing pseudo labels


And use the


use the representations


Given y


The pretext task solver network


So what is the idea the idea is lets say that you are given some images okay so you build a neural network


this as f theta what this would do is take an image and like take its rotation lets say


And this network would simply predict


The rotation angle


Okay try in this network to predict the rotation angle and take the penultimate layer of that as your Z


That is what Im trying to say This is one of the pretext tasks The other can be take this


and take a


Uh big noise


and build a network


That would classify between this and this


And use the representations of that as you will see this is classify


between noise and data


So what is shown us that if you solve like pseudo tasks like this you know these are called the self supervised tasks Basically you are given data create some pseudo tasks using self supervision right And a network that would solve those self supervised tasks they are shown to have properties right Or representations that are very strong in solving the underlying


uh downstream task right i mean itll learn the underlying distribution is uh is is what uh has been shown but the question is i mean two things one


Why should this work I mean why should solving these kinds of pseudo tasks should give you good representations of the data So that is the first question that we will be asking The second question that we will be asking is what are the ways to define some of these pseudo tasks self supervised tasks so that they give you a very good representation Well answer both of these questions in the next class


Any questions on this

### Speaker 2

So we use the same network to learn or I mean for this multiple pre text tasks or its a different network

### Speaker 1

Yeah those I mean I will discuss all that in the next class right I mean there are multiple ways I mean empirically right Some people use the same network some people use different networks and then a lot of other things are done We will discuss all of these

### Speaker 2

Okay so just one question So which of these is preferable which of these two methods

### Speaker 1

will as I said no all of these will be answered in the next class I mean I just gave you two examples see there is the other example is


that you construct a

### Speaker 2

Perfectly

### Speaker 1

And Im using the kind of model take the image


and like just mask it


And reconstruct the image back this is called the masked autoencoding This is what is used in bird kind of models right This is

### Speaker 2

To a sentence prediction

### Speaker 1

Same thing right I mean there is the mask auto encoding for image based models as well There are this is these are examples This is like in print


painting right or filling the graphs


There are multiple hundreds of ways of uh


Defining pretest pretest tasks so when different people have different they generated in come up with different pretest tasks and all of them are different

### Speaker 2

Different people speak different languages

### Speaker 1

uh uh performances JPA is one one one other way to do it in fact what is done in JPA is that they take an image okay and they


randomly take some parts of the image and call that as context and give that as an input to a network and randomly take some other patches and call that as target So the task that they solve is given the context they want to predict the target


See the basic idea is the following right So if you can


in the blanks okay the only way to fill in the blank blanks is to understand the underlying semantics thats all so that is the whole idea and there is a very nice mathematically grounded uh uh uh treatment of why all of these should work this is something called noise contrastive estimation or nce we will see that okay we will see uh why should these kinds of ideas work in the next class and there are hundreds of ways to do this okay jeppa is one of the


uh ways to do it huh we will which well see in the next class


Okay so thats it for today then


I will assume the next week Yeah next week there will be a quiz And next to next week well do a hybrid class Okay


okay yeah so again once again happy Diwali to all of you yeah so today should have been a holiday no I dont know why I should they didnt make it a holiday and okay thanks for coming


You might have heard some noise et cetera right Today because I am also traveling and not sitting in my home office So yeah excuse me for that Okay see we will catch up next week

### Speaker 2

Thank you

### Speaker 3

Im sorry Im sorry
