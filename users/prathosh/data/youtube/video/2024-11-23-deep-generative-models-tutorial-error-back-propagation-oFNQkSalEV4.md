---
id: oFNQkSalEV4
title: Deep Generative Models Tutorial Error back propagation
date: '2024-11-23'
url: https://www.youtube.com/watch?v=oFNQkSalEV4
description: ''
author: prathoshap5226
duration: 01:07:57
model: saaras:v3
transcript: true
---

# Deep Generative Models Tutorial Error back propagation

## Transcript

### 00:00:02 · Speaker 2

And you can see my screen, right? Okay.

### 00:00:10 · Speaker 2

Yeah, hope you can see my screen. So, what we'll be doing today is we'll be talking about back propagation.

### 00:00:37 · Speaker 2

And specifically

### 00:00:38 · Speaker 5

we'll be looking at back propagation and neural networks. So I'll first talk about an example uh explaining why it is important and what is its role in deep learning. And uh and finally in the end we'll we'll hopefully solve one or two questions regarding back propagation. So

### 00:00:58 · Speaker 5

to to begin with, the basic idea of deep learning is that you have some input data X.

### 00:01:07 · Speaker 5

So you have some

### 00:01:10 · Speaker 5

neural network

### 00:01:14 · Speaker 5

which gives you an output Y. And our goal is to

### 00:01:20 · Speaker 5

Our goal is to be able to predict why using this neural network, using

### 00:01:29 · Speaker 5

using training data

### 00:01:32 · Speaker 5

given by X I Y I

### 00:01:34 · Speaker 5

which means that for every data point X I, Y I is its corresponding output that that you want to have but that you want to have predicted by the neural network. So basically

### 00:01:48 · Speaker 5

what the goal of neural network

### 00:01:50 · Speaker 2

X

### 00:01:54 · Speaker 2

is to minimize some error

### 00:02:07 · Speaker 2

using the training data.

### 00:02:13 · Speaker 2

and hopefully

### 00:02:14 · Speaker 5

learn the neural network so that it it can perform well on some test test data or test examples. So so just to give an give a basic idea of how how learning works and how bad propagation is done is that let's assume

### 00:02:35 · Speaker 5

I'm learning to play a sport, let's say tennis, and I have, maybe I, I have a

### 00:02:43 · Speaker 5

I have a tennis court like this.

### 00:02:48 · Speaker 5

And my goal is to hit the ball into the court

### 00:02:54 · Speaker 5

as much as I can. And I I want to prevent hitting the ball outside the court, something like this. Now, what this means is that every shot that my opponent plays against me, I want to return it.

### 00:03:09 · Speaker 5

and return it such that the ball lands inside the court. And we want to avoid hitting the ball outside the court. So what this means is that we are training our our muscles and our nervous system to be able to hit the ball inside the court. And how do we learn this?

### 00:03:29 · Speaker 5

is

### 00:03:32 · Speaker 5

by minimizing this distance or the so-called error.

### 00:03:37 · Speaker 2

Okay

### 00:03:38 · Speaker 5

So this error is what we we want to minimize. Or maybe maybe the error is from somewhere inside the code. So this is what we want to minimize and uh as we keep practicing.

### 00:03:52 · Speaker 5

our muscles develop that skill to be able to hit inside the court. while at the same time minimizing this error. So that is the goal of learning neural networks. That is to accomplish some task.

### 00:04:07 · Speaker 5

by reducing some form of error. So this is the this is the goal of neural networks or deep learning in general. So what are the different phases that a neural network has is that first

### 00:04:24 · Speaker 2

maybe I'll just copy this

### 00:04:35 · Speaker 2

So, neural network is typically

### 00:04:39 · Speaker 2

accompanied by two operations. One is the forward pass.

### 00:04:45 · Speaker 2

that

### 00:04:47 · Speaker 2

that takes input to output. So

### 00:04:52 · Speaker 2

forward is input to output

### 00:04:58 · Speaker 2

And we have something known as the backward pass.

### 00:05:07 · Speaker 2

and the backward pass

### 00:05:10 · Speaker 2

goes from output or in in most cases the sorry error to

### 00:05:21 · Speaker 5

the weights or input

### 00:05:25 · Speaker 5

Okay. So the forward pass is what what the neural network predicts and the backward pass is the feedback that you get from the prediction that is made by the neural network.

### 00:05:36 · Speaker 5

So based on this feedback whatever is given by the backward pass, we can we can choose to update our weights accordingly in order to reduce an error.

### 00:05:47 · Speaker 2

Okay

### 00:05:47 · Speaker 5

So that is a basic idea of every neural network in in just in simple terms. And we are we are going to focus on we are going to focus on this backward pass and or or back propagation in general. So so what I'll do now is we'll set up a simple neural network and we will see how how back propagation works. So

### 00:06:15 · Speaker 5

the neural network is as follows. You have some uh you have some input let's say X uh and it's a two length feature vector. So X one.

### 00:06:30 · Speaker 5

And a neural network typically has these neurons or nodes.

### 00:06:38 · Speaker 5

They're called neurons or nodes.

### 00:06:41 · Speaker 5

And this is where multiple operations happen in the neural network. And it keeps and every every neural network has things known as layers and each layers each layer consists of multiple neurons which are interconnected with each other.

### 00:07:00 · Speaker 5

So this is typically how neural networks are. So

### 00:07:04 · Speaker 2

this is this is known as the input layer

### 00:07:16 · Speaker 2

Hello

### 00:07:20 · Speaker 2

This is the input layer

### 00:07:23 · Speaker 2

And then we have

### 00:07:26 · Speaker 2

we have two hidden

### 00:07:27 · Speaker 5

players

### 00:07:31 · Speaker 5

And finally we have one, uh, let's say we have one output layer.

### 00:07:39 · Speaker 5

giving us Y

### 00:07:40 · Speaker 2

giving us Y hat which is the prediction

### 00:07:46 · Speaker 2

is the prediction or the output

### 00:07:51 · Speaker 2

and this is the input.

### 00:07:54 · Speaker 5

So like I said, uh these neurons or nodes are where the where the operations happen. And each of these connections

### 00:08:07 · Speaker 5

So maybe I'll highlight it.

### 00:08:10 · Speaker 5

These connections are these connections link two nodes through some weight characterized by W. So every node I'm I'm going to notate with the letter A. So maybe

### 00:08:25 · Speaker 2

Okay

### 00:08:32 · Speaker 2

I'll call this A.

### 00:08:35 · Speaker 2

the

### 00:08:35 · Speaker 5

This is A one. This is the first node in the first layer. This is the second node in the first layer. So I call them A one one and A two one. And these weights are denoted by W I J. It connects W I J connects

### 00:08:55 · Speaker 5

Node I

### 00:08:57 · Speaker 5

to node J.

### 00:09:00 · Speaker 5

And of course every weight also is also associated with the layer number. So this let's say this is layer one. So W I J one is node I to node J from

### 00:09:19 · Speaker 5

layer one

### 00:09:21 · Speaker 5

So this is the notation that we're going to follow. And uh similarly the output layer uh I can denote the sorry the hidden layer I can denote by

### 00:09:33 · Speaker 5

the notation A one two which is the first node of the second layer and A two two which is the second node of the second layer

### 00:09:43 · Speaker 5

And finally we have Y hat which is the output. You could call it A one three but it's just simpler to call it Y hat which is the output. So this is the notation we're going to follow. And

### 00:09:58 · Speaker 5

Yeah, so this is a notation we will follow and the weights are denoted by W I J. W I J of the layer number. So this weight for example

### 00:10:10 · Speaker 5

For example, this weight over here would be denoted by W two one second layer. So W two one of two. So uh

### 00:10:22 · Speaker 5

now that we have

### 00:10:24 · Speaker 5

define the notations so let's move forward. So like I said earlier the goal is to minimize some error using the using the training data and this error is also sometimes also called the optimization objective or it's also called the loss function. So

### 00:10:44 · Speaker 5

a loss function

### 00:10:49 · Speaker 5

is some

### 00:10:51 · Speaker 5

function of your prediction y hat and your input x.

### 00:10:58 · Speaker 5

It it is some it is some function of this along with the parameters. Okay so maybe I'll also mention that. So uh let's say all the W I Js.

### 00:11:09 · Speaker 5

are in some vector

### 00:11:15 · Speaker 5

uh they're the collection of all these para all these weight vectors W I J of of any layer L. So let me call L. So

### 00:11:28 · Speaker 5

This theta is the set of all parameters in the in the neural network. So

### 00:11:35 · Speaker 5

Yeah

### 00:11:37 · Speaker 5

and it is function of theta. Okay? So this is uh this is typically uh what is done in neural networks where you try to minimize this. So our goal is to

### 00:11:52 · Speaker 5

minimize over all possible theta

### 00:11:56 · Speaker 5

this function of i hat x and theta. So you want to

### 00:12:01 · Speaker 2

reduce

### 00:12:04 · Speaker 2

the loss function.

### 00:12:11 · Speaker 2

function using

### 00:12:14 · Speaker 2

training data

### 00:12:19 · Speaker 2

Okay? So, uh let let's uh let's maybe I copy this.

### 00:12:35 · Speaker 2

Okay. So, the one of the most common loss functions that we use is known as the mean squared error.

### 00:12:51 · Speaker 2

in short, we just call it MSE. It is nothing but

### 00:12:55 · Speaker 5

of

### 00:12:58 · Speaker 5

Y hat minus. uh So let's call the neural network F.

### 00:13:05 · Speaker 2

F theta parameterized by theta. So F theta is the neural network.

### 00:13:15 · Speaker 2

by minus

### 00:13:18 · Speaker 2

एफ थीटा ऑफ एक्स स्क्वेयर। सो दिस इज नोन एस द मीन स्क्वेयर्ड एरर एंड दिस इज व्हाट वी वांट टू मिनिमाइज़।

### 00:13:33 · Speaker 2

Okay? So

### 00:13:37 · Speaker 2

So

### 00:13:37 · Speaker 5

So, in order to minimize any function, the the most, yeah, there is a hand raised, so.

### 00:13:45 · Speaker 0

Yeah, I have a question. Can you please just tell me what the theta denotes? Sorry, I mean, I did not understand it fully.

### 00:13:53 · Speaker 5

Okay, yeah, sure. So theta is the set of all weights, these uh these connections I told you, right? These neural connections. This connection from A one two to A two one to A one two. So things like these are these are connections between nodes of the neural network. And these are parameterized by some weight. So those

### 00:14:14 · Speaker 3

Hello

### 00:14:16 · Speaker 5

weights are what if you collect all those weights and put them into one set those are

### 00:14:26 · Speaker 5

Yeah, sorry, sorry. uh Yeah. So I'm saying the theta is the collection of all weight weights of the neural network. So I'll write theta as

### 00:14:38 · Speaker 5

W one one of one. W one two one. W two one one. W two two of one. So if you look here, this is going to be W two two of one. This

### 00:14:56 · Speaker 5

this this weight vector connecting this is going to be W two one of one. This is going to be W one one of one. And this this weight vector is going to be W one two of one. Because it's connect it connects node I to node J. This is node one, this is node two. So, the weight connecting node one of layer one to node one of layer two is going to be W one one of one, which is this. So, by what I mean by is it is the collection of all these weights in the neural network. Okay?

### 00:15:32 · Speaker 5

So it it's just a set of connections that we want to learn in the neural network. So I'll I'll come to how we learn these. So does that answer your question?

### 00:15:42 · Speaker 0

Yes, thank you.

### 00:15:43 · Speaker 5

Season

### 00:15:44 · Speaker 0

ಓಕೆ

### 00:15:44 · Speaker 5

Sure

### 00:15:46 · Speaker 5

Okay, so moving forward, like I said, our goal is to minimize this loss function.

### 00:15:55 · Speaker 5

and that helps us reduce our error and learn a particular task properly. By learning a task, I mean these predictions why that we get, we want them to be as uh we want them to be very good or close to what we desire. So that is the goal of learning a neural network.

### 00:16:16 · Speaker 5

So let's uh so so let me begin with a simple example maybe. So let's say uh this is your input uh X.

### 00:16:31 · Speaker 5

Yeah, so

### 00:16:34 · Speaker 5

So let's say you you you have two inputs to your neural network X one and X two. Say this is your node. So these are your input nodes. A one one and this is A two of one meaning layer one. And then you have the similar neural network like this.

### 00:16:54 · Speaker 5

you have you have a single output node giving you Y hat. And let's say that okay let me just notate these. This is A one layer two. This is A two layer two. And this weight over here is W one one one.

### 00:17:12 · Speaker 5

this going from node one to node two is W one two of one. Similarly you have W two one of one and you have W two two of one. Similarly the output layer you have W

### 00:17:29 · Speaker 5

one one of two and W two one of two. Okay? So, uh let's um so what we're going to do is we're going to assign some weights to these and then we will see how how this neural network is trained. Okay? So let's say this W one one is just

### 00:17:49 · Speaker 5

Okay, I'll erase these and maybe just put the weights on top of the arrows.

### 00:17:57 · Speaker 5

So this may be is one, this is point five. This is point five and this is one. Similarly, let these output weights also be one and one.

### 00:18:08 · Speaker 5

Okay. So, uh for the input nodes, we have A one one is simply equal to X one and A two one simply equals X two. Okay. So this is what we have. This is uh this is the input layer.

### 00:18:29 · Speaker 5

Then the notion of nodes in a neural network is as follows. It it combines different nodes of the previous layer through something known as a linear combination or a weighted sum of the of values in the previous layer. uh What I mean by that is uh let's take A one two for example which is this node over here.

### 00:18:56 · Speaker 5

A one two equals a weighted sum of A one one and A two one and the weights are exactly what is there on the arrows connecting the corresponding nodes which is W one one one

### 00:19:13 · Speaker 5

and W two one of one. Okay? So this is

### 00:19:20 · Speaker 5

typically how A to one is defined as but one important thing to note is before it is not just a linear combination of this it is some function G of this function okay so this

### 00:19:36 · Speaker 2

G function

### 00:19:38 · Speaker 2

is known as an activation function.

### 00:19:48 · Speaker 2

And depending on

### 00:19:50 · Speaker 5

depending on the application or what you want in neural network to achieve. These activation functions could be different for example, uh you have sig you have sigmoid.

### 00:20:03 · Speaker 5

to have a relio

### 00:20:05 · Speaker 5

you have tan H. And each of these activation functions do something different.

### 00:20:14 · Speaker 5

So, sigmoid is

### 00:20:19 · Speaker 5

sigma of x is one by one plus e power minus x

### 00:20:26 · Speaker 5

and the relo function

### 00:20:30 · Speaker 5

is nothing but

### 00:20:33 · Speaker 5

g of x equals x when x greater than equals zero, zero if x is less than zero.

### 00:20:41 · Speaker 5

and

### 00:20:47 · Speaker 5

And yeah, similarly you have other activation functions like tan H, exponential linear unit and you you have many more, you have so many activation functions that are used on the linear combination that you get from the previous layer.

### 00:21:05 · Speaker 5

Okay, so this is the activation function. This is sometimes also known as the net input to the node.

### 00:21:16 · Speaker 2

Okay? And what we have here is the

### 00:21:22 · Speaker 2

Node output

### 00:21:26 · Speaker 5

is the node output or simply the

### 00:21:30 · Speaker 5

Okay, so let's not call it output. Let's let's just keep it as node output.

### 00:21:35 · Speaker 2

So

### 00:21:36 · Speaker 5

Uh, this is, yeah, uh, one question. Yeah, two questions.

### 00:21:43 · Speaker 4

Hi, sorry. Am I audible?

### 00:21:45 · Speaker 5

Yeah, yeah, tell me.

### 00:21:46 · Speaker 4

Yeah, yeah, tell me. I just wanted to know about uh why we in the middle layer, right? Uh can we scroll a little up? I wanted to see that figure. Yeah, why is there no connection between A one two and A two one? Can that also be called as a neural network?

### 00:21:47 · Speaker 2

Okay

### 00:22:02 · Speaker 4

I mean,

### 00:22:03 · Speaker 5

uh no typically that's not how uh okay so let me give you the uh let let me give you a real life example so uh every every living being has has a nervous system right? So in that nervous system uh you have you you have some neurons.

### 00:22:24 · Speaker 5

that are like this.

### 00:22:25 · Speaker 4

Okay

### 00:22:27 · Speaker 5

and then you have these synaptic connections connecting one nerve to another. Okay?

### 00:22:33 · Speaker 4

Ram

### 00:22:33 · Speaker 2

Okay

### 00:22:34 · Speaker 5

So, okay, I think my screen is... Yeah, okay. So, what these, what these nodes are is actually this point.

### 00:22:46 · Speaker 5

the starting of the branch that connects one node to another node. So, node these nodes are typical like

### 00:22:55 · Speaker 5

Uh let's take the optic nerve for example. So the optic nerve is typically a bunch of nerves. So these bunch of nerve nerves have separate nodes in each of them and they are typically when you have multiple connect when you have a bunch of nerves like this. Uh you you you don't really need these two nodes to be connected say.

### 00:23:20 · Speaker 5

because the the main reason is if let's say let's say some problem happens with this nerve. Then if these two are connected then this whole this whole line is gone like this whole since this entire nerve is connected. then this could be this could cause problems so

### 00:23:43 · Speaker 5

like essentially what we are trying to do is we are trying to parallelize these nodes so that if one thing goes wrong you can you can always have you can always learn with another node or things like that. But of course

### 00:23:49 · Speaker 2

Okay

### 00:23:58 · Speaker 5

this is this is not not an exact answer to your question but this typically this is the convention that you follow in in deep learning and in and neural networks. you don't have okay so you don't have connection between these because you have a you have a very nice dense connection between these nodes.

### 00:24:12 · Speaker 6

you don't have

### 00:24:21 · Speaker 5

between layers of nodes.

### 00:24:22 · Speaker 4

players

### 00:24:23 · Speaker 5

Okay

### 00:24:24 · Speaker 4

So that's and the

### 00:24:24 · Speaker 5

So that's and the

### 00:24:26 · Speaker 4

Sorry, just a follow up. And the difference between A one two and A two two is actually the weights currently, right? Because both are giving the same inputs but with a different weight.

### 00:24:27 · Speaker 5

Yes or no

### 00:24:29 · Speaker 5

Yeah

### 00:24:41 · Speaker 4

both are getting X one I can give you but weights can differ. Right. That's it right.

### 00:24:42 · Speaker 5

Correct Yes

### 00:24:45 · Speaker 5

Yeah, correct. So you you can notice that if X one and X two are different then A one two and A two two are different. Right? Because uh if you look at if you look at A one two, it is some function of W one one A one and W two one A two. But if you look at A two two

### 00:25:06 · Speaker 5

It is the activation of

### 00:25:08 · Speaker 6

for

### 00:25:08 · Speaker 5

So A22 is this one, right? So A22 is this one. And it comes from, so what are the things contributing, what are the nodes contributing towards this, these two, right? So

### 00:25:23 · Speaker 2

So

### 00:25:25 · Speaker 5

So in this case, it's going to be W one two one

### 00:25:29 · Speaker 2

two one

### 00:25:30 · Speaker 5

A11 plus

### 00:25:33 · Speaker 5

W two two one

### 00:25:37 · Speaker 5

A two one. Okay? So you can see that these two are different, right?

### 00:25:39 · Speaker 4

Okay

### 00:25:40 · Speaker 4

you can

### 00:25:42 · Speaker 4

Sure, yeah, got it.

### 00:25:45 · Speaker 5

Yeah, so

### 00:25:45 · Speaker 4

So

### 00:25:47 · Speaker 5

Yeah, okay. So, uh basically this is how uh this is how we uh go forward in a neural network which is taking the input to the output and this entire process is known as the forward process.

### 00:26:06 · Speaker 5

So the forward process takes in takes you from input to the hidden layers. Of course you could have multiple hidden layers here. You can have A one two, A one three, A one four and then you can have I hat and things like that. So those are deeper neural networks and that's that's where the term deep learning stems from and you have when you have more than three or four layers you typically go into the realm of deep learning and

### 00:26:34 · Speaker 5

Yeah. So this is a forward process. And so let me just complete the equation so sake of completeness. So similarly these this is W one one of from layer two. This is weight connecting node two to node one of layer three from layer two. Okay. So Y hat.

### 00:27:00 · Speaker 5

is again some function of W one one two

### 00:27:09 · Speaker 5

but it multiplies the this node over here which is A one two

### 00:27:15 · Speaker 5

plus W two one two of A two. Okay, so

### 00:27:20 · Speaker 2

This is the final output

### 00:27:24 · Speaker 2

output or you call it the prediction of the neural network.

### 00:27:30 · Speaker 2

Okay? So this is the entire forward

### 00:27:32 · Speaker 5

process taking you from the inputs

### 00:27:37 · Speaker 5

from the inputs to the output.

### 00:27:41 · Speaker 5

Okay. So, uh typically your input is denoted by X and it's a vector containing X one and X two. So, uh you you could call this input data.

### 00:27:58 · Speaker 2

or you could call it features.

### 00:28:01 · Speaker 2

input features

### 00:28:06 · Speaker 5

So, yeah, these names are used interchangeably. So you just basically this is the input.

### 00:28:13 · Speaker 5

So the input could be a vector, it could be a single number, it could be an image, it could be anything, it could be a video, it could be an X-ray scan, it could be anything. So these so depending on the dimension of the input, your neural network will also uh change the nature of its weights. And uh one important thing is that uh for every

### 00:28:37 · Speaker 5

So I'll just

### 00:28:41 · Speaker 5

copy this once again.

### 00:28:44 · Speaker 3

one question I have

### 00:28:47 · Speaker 5

Yeah, sure. Go ahead.

### 00:28:48 · Speaker 3

सो डस दिस फॉलो एन एडिटिव प्रॉपर्टी वेयर जी ऑफ डब्ल्यू वन वन टू ए वन टू

### 00:28:55 · Speaker 5

Okay

### 00:28:55 · Speaker 3

Can we can we move the weights like can we apply the function on the different weights then add them? Like G of W one one A one plus G of W two one A two.

### 00:29:08 · Speaker 5

Sure, you can, definitely. It is possible, but generally neural networks for a particular layer, you have a particular gene.

### 00:29:19 · Speaker 5

So for example layer one so okay. Maybe uh this layer could have a relu activation function and maybe this can have a sigmoid.

### 00:29:32 · Speaker 5

So G is equal to relu, here G is equal to sigmoid and you can you you you generally have different activation functions for different layers rather than different activation functions for different nodes. Okay?

### 00:29:48 · Speaker 6

Cadre

### 00:29:49 · Speaker 5

Okay

### 00:29:49 · Speaker 6

Okay

### 00:29:49 · Speaker 6

Thank you

### 00:29:50 · Speaker 5

there's another question.

### 00:29:53 · Speaker 0

uh just a small query that how initially we are assigning these weights I mean I understand later maybe through the back propagation we correct it but initially we have to assign some numbers against these weights right?

### 00:29:57 · Speaker 5

S

### 00:30:05 · Speaker 5

Yeah

### 00:30:07 · Speaker 5

Yeah, yeah. So I I was so that was going to be my follow up discussion. Okay. Okay, sorry.

### 00:30:11 · Speaker 0

Okay, Okay, Sorry.

### 00:30:13 · Speaker 5

these yeah. No it's okay. It's it's a good question actually. So

### 00:30:19 · Speaker 5

So one important note is that weights are initialized.

### 00:30:26 · Speaker 2

So what I mean by initialized is they are assigned something

### 00:30:33 · Speaker 2

So you are assigning some weights.

### 00:30:40 · Speaker 2

at the start

### 00:30:44 · Speaker 2

So, so typically what people do in neural networks is that these weights are selected randomly.

### 00:30:53 · Speaker 2

or I should say initialized randomly.

### 00:31:03 · Speaker 2

Okay

### 00:31:05 · Speaker 2

So, uh yeah, uh I have a couple more questions, yeah.

### 00:31:10 · Speaker 6

सर, व्हाट इज़ द सिग्निफिकेंस ऑफ दिस

### 00:31:14 · Speaker 6

activation function like will it be covered later or

### 00:31:19 · Speaker 5

Uh yeah, I mean, okay, so the role of the activation function is to limit the these uh outputs, these node outputs to be in a certain range. So you don't

### 00:31:32 · Speaker 5

Okay

### 00:31:34 · Speaker 5

Yeah, sorry, I got cut off. Yeah, so I was saying the role of these activation functions is to somewhat limit the values of these node outputs. So you have these node outputs, right? A one two eight, A two two and all these things. So you want to limit them to certain range. For example, if you if you take the sigmoid activation, so G of X is let's say sigmoid of X, which is one by one plus E power minus X. what this basically does is that

### 00:32:07 · Speaker 5

Hmm

### 00:32:09 · Speaker 5

Okay, we'll use this color.

### 00:32:14 · Speaker 5

What this basically does is if if you have uh let's say this is your x and y axis.

### 00:32:22 · Speaker 5

okay, y is equal to sigma of x. What this does is that it takes all your values from

### 00:32:30 · Speaker 5

from minus infinity to infinity and it brings it to the range of zero to one.

### 00:32:37 · Speaker 5

Okay. So, in neural networks you don't want your values to blow up so that your Y hat becomes like one lakh, ten lakhs and all. So you don't want that to happen. So you want to control your you want to control

### 00:32:52 · Speaker 6

want to convert

### 00:32:53 · Speaker 5

Hmm

### 00:32:55 · Speaker 6

we want to like contain it in some range. Correct, yes.

### 00:32:58 · Speaker 5

correct yes. So

### 00:33:00 · Speaker 6

Tennis

### 00:33:02 · Speaker 5

So activations basically control your

### 00:33:05 · Speaker 2

Nodal

### 00:33:12 · Speaker 5

So, these activations are actually very important because this this sigmoid, right? This this is the sigmoid function.

### 00:33:20 · Speaker 5

This is used typically at the output of

### 00:33:25 · Speaker 5

of classifiers.

### 00:33:29 · Speaker 5

So classifier is basically something that gives you a decision. So it gives you a decision. And uh you you basically want a yes or no decision.

### 00:33:39 · Speaker 5

And so for example, yes could be close to one and no could be close to zero. So the sigmoid activation function is a is a perfect choice as an activation function in these classifier functions, okay? So sir will be covering classifiers later on and maybe that time you'll you'll encounter the sigmoid activation. So depending on what you want your network to do, you will choose different active for different layers of your neural network

### 00:34:13 · Speaker 5

So for for image problems you might want to use Relu. So for

### 00:34:20 · Speaker 5

image sorry

### 00:34:22 · Speaker 5

or image networks

### 00:34:26 · Speaker 5

you might want to use relu

### 00:34:29 · Speaker 5

which relio is basically anything less than zero it gives zero and anything greater than zero it gives the it gives the same output. So this is the relio relio function. So x and g of x.

### 00:34:46 · Speaker 5

Yeah. So this is so depending on your application you will choose you will decide to choose different activation functions. So hope that's clear. Yeah there's another question.

### 00:34:57 · Speaker 2

the wind

### 00:35:00 · Speaker 6

and vice versa they are very small in number

### 00:35:02 · Speaker 6

but they're not

### 00:35:03 · Speaker 5

big, I believe

### 00:35:05 · Speaker 6

the reason you just keep it don't want to blow it up. Is that correct?

### 00:35:05 · Speaker 5

season

### 00:35:09 · Speaker 5

Hmm

### 00:35:11 · Speaker 6

और एंड व्हेंस्ट ऑल्स

### 00:35:12 · Speaker 5

Sorry

### 00:35:13 · Speaker 5

Yeah, I, your voice was breaking in the middle. Can you repeat the first part of your question?

### 00:35:14 · Speaker 6

I

### 00:35:19 · Speaker 6

Generally what I have seen the weight and biases for this neural network they are very small in numbers they are not pretty big

### 00:35:23 · Speaker 5

Hmm

### 00:35:24 · Speaker 5

Yeah

### 00:35:28 · Speaker 5

Correct, Correct.

### 00:35:28 · Speaker 6

So, so there has to be a reason behind that. I believe you just explained we don't want to explode the final Y hat.

### 00:35:35 · Speaker 5

Correct.

### 00:35:35 · Speaker 6

is that? Okay, and second thing is that when we initialize it randomly, do we also define what kind of

### 00:35:39 · Speaker 5

Hmm

### 00:35:42 · Speaker 5

Sorry, I think I'm losing your voice. I can't hear.

### 00:35:49 · Speaker 6

Okay, let me try once again.

### 00:35:52 · Speaker 5

Yeah

### 00:35:54 · Speaker 6

Yeah. So when we initialize these weights randomly, do we also define the range between it's going to be

### 00:36:03 · Speaker 5

Correct. Yes, we do, we do. In many applications you you you use some weights between zero and one.

### 00:36:12 · Speaker 5

Okay

### 00:36:16 · Speaker 5

Hmm

### 00:36:19 · Speaker 5

belongs to some let's say minus one to one or zero to one

### 00:36:27 · Speaker 5

So typically we choose weights in this range and

### 00:36:32 · Speaker 5

Yeah, we initialize weights randomly such that they're in this range, minus one to one or zero to one, just so that it's small and you you don't have something known as gradient explosion. You you want to avoid this gradient explosion.

### 00:36:49 · Speaker 5

So I'll I'll come to what this is later on or it it will also be covered in the course I believe. So we want to prevent this.

### 00:37:01 · Speaker 5

want to prevent gradient explosion so we we choose the weights to be a bit in some range where they are very small. Yeah. So I hope that answers your question for now. So we'll I mean this this you'll encounter in almost any application where the weights are going to be very small and you start off with those weights and then you you start learning your network through back propagation.

### 00:37:27 · Speaker 5

Okay. So now let's move to, let's move to back propagation.

### 00:37:34 · Speaker 2

Hmm

### 00:37:43 · Speaker 2

So let's go back to our neural network that was over here.

### 00:37:56 · Speaker 2

Yeah, so this was our network and if you recall we had

### 00:37:59 · Speaker 5

had a loss function L

### 00:38:01 · Speaker 2

Hello

### 00:38:02 · Speaker 5

which was the mean squared error between Y hat and F theta of X. Where F theta of X is taking your is the entire neural network, this is F theta of X.

### 00:38:15 · Speaker 5

This takes your input X where if if you recall X was the was the vector X one X two this is the vector. This is a input vector.

### 00:38:30 · Speaker 5

input vector of x one x two taking you to the prediction y hat. This is the prediction.

### 00:38:38 · Speaker 5

So what you what you want to what we basically want to do is let's say we have some training data

### 00:38:47 · Speaker 5

And for now let us assume we only have one training data sample which is the for the input X I expect the output Y. So this is our training data. So typically you call it X I Y I and you have N such

### 00:39:06 · Speaker 5

examples. So your training data will typically look like X one for X one you you desire the output Y one for X two you desire the output Y two and so on.

### 00:39:21 · Speaker 5

Okay? So this is our training data, but for now let's just assume we have a single training data sample. Assume your data is just

### 00:39:31 · Speaker 2

x, y, a single example.

### 00:39:37 · Speaker 2

single training example

### 00:39:41 · Speaker 2

Now our goal is to minimize

### 00:39:49 · Speaker 5

L is equal to half of Y hat minus F theta of X square

### 00:39:58 · Speaker 5

So this is what we want to minimize and how do we minimize any function? We compute its derivative with respect to what we can optimize over or what we can change in the network. And what can we change in the network? We can change theta or the weights.

### 00:40:16 · Speaker 5

So this is what we can change. uh So the natural step is to take the derivative of the loss with respect to some parameters in the network.

### 00:40:28 · Speaker 5

So let's say W I J of L which is the weight I J. uh weight from node I of layer L to node J of layer L plus one. And we take this derivative.

### 00:40:43 · Speaker 5

And

### 00:40:46 · Speaker 5

what we do is we we take we compute this derivative

### 00:40:52 · Speaker 5

And then we do something known as the gradient descent.

### 00:41:00 · Speaker 5

which is any weight W I J of L is updated as W I J L minus some weight alpha times this derivative.

### 00:41:16 · Speaker 2

I J L and this is known as

### 00:41:22 · Speaker 2

Fact Propagation

### 00:41:26 · Speaker 2

This is back propagation through

### 00:41:31 · Speaker 2

gradient descent

### 00:41:35 · Speaker 2

Yeah, there's a question.

### 00:41:38 · Speaker 6

sir in this loss minimize loss function this y hat is also the output of neural network

### 00:41:42 · Speaker 2

function

### 00:41:45 · Speaker 2

top

### 00:41:45 · Speaker 5

Tell me

### 00:41:48 · Speaker 6

by head is also the output of neural network, right?

### 00:41:53 · Speaker 5

Hmm

### 00:41:54 · Speaker 5

Yeah, sorry, I missed. Why hat? I wanted it to be Y.

### 00:41:55 · Speaker 6

Selco

### 00:42:01 · Speaker 2

Bye

### 00:42:01 · Speaker 5

Yeah, yeah, sorry, sorry, sorry, my mistake. This is, this should be Y. Yeah, correct.

### 00:42:08 · Speaker 2

Okay, thank you.

### 00:42:16 · Speaker 6

Sir, I have

### 00:42:17 · Speaker 3

one question

### 00:42:19 · Speaker 2

um

### 00:42:19 · Speaker 3

Oh

### 00:42:19 · Speaker 3

So I have a general doubt. So when we calculate the loss in a network, the network is not aware of the loss function, right? Initially, we just calculate a numerical loss and it's some numerical data which we have.

### 00:42:35 · Speaker 5

Correct

### 00:42:36 · Speaker 3

correct and then um how do we uh calculate the gradient on some numerical data with respect to a parameter just wondering

### 00:42:47 · Speaker 5

So, okay, yeah, that's a good question. The loss is what we define.

### 00:42:54 · Speaker 5

This is user defined. So this this is a function and it is a function of x and theta, correct? So regardless of regardless of whether your data is numerical or or synthesized or analytical, whatever it may be, you can always compute the derivative of your loss with respect to your parameters.

### 00:43:16 · Speaker 5

So this since this is what we define and it is a we define we can we can compute the gradient of this and we can and we can use that to update our neural network. Okay?

### 00:43:31 · Speaker 5

is that clear or

### 00:43:34 · Speaker 1

B.

### 00:43:34 · Speaker 6

Best

### 00:43:35 · Speaker 1

Sir

### 00:43:35 · Speaker 5

Hello

### 00:43:36 · Speaker 5

Yeah, another question?

### 00:43:40 · Speaker 1

Uh sir, I had a doubt on the loss function. So since this is a squared value, like how do we know if we're shooting above the value or are we shooting below the value in that scenario?

### 00:43:43 · Speaker 5

Square

### 00:43:45 · Speaker 5

shooting

### 00:43:52 · Speaker 5

So you you have your prediction right Y hat from the network

### 00:43:56 · Speaker 1

network

### 00:43:58 · Speaker 5

So this is the prediction and what is Y hat? Y hat is actually F theta of X. It is what your neural network gives you. So, uh what your neural network gives you is the prediction and what you have is your training data X I Y I. And uh and what you will do is you will compare

### 00:44:19 · Speaker 5

you will compare prediction

### 00:44:24 · Speaker 5

y hat equal to f theta of x i. x i is some training example that you have. with

### 00:44:33 · Speaker 5

the ground truth

### 00:44:38 · Speaker 5

with the ground truth Y I. Okay? So maybe let me call it Y hat I. So what you will compare is you will compare the loss between Y hat I and Y I which is the squared error.

### 00:44:52 · Speaker 5

y hat i minus f theta of xi. So you have your prediction over here.

### 00:45:02 · Speaker 5

sorry, oh, I shouldn't use. This is Y I, sorry. And this is your true label.

### 00:45:11 · Speaker 5

true label or ground truth

### 00:45:16 · Speaker 5

So ground truth is what we desire and prediction is what your neural network has given you. So you have an idea of which one is greater. Greater or lesser.

### 00:45:26 · Speaker 5

Okay? Is that clear?

### 00:45:30 · Speaker 1

Uh yes, but the loss will be the same like even if the F F not the prediction is higher for example by five compared to the truth or if it's lower by five the loss function will be will give you the same value, right?

### 00:45:39 · Speaker 5

Hmm

### 00:45:45 · Speaker 5

Yes, it will. Yeah.

### 00:45:47 · Speaker 1

So then how do we know like we have to increase the weights or we have to decrease the weights in that scenario?

### 00:45:54 · Speaker 5

So that is what uh so the the moment you have some error that is not zero. That is greater than zero. It means that you are off from your ground truth, correct? Yes. So you gave the example that f theta of x i might be five higher or five lower.

### 00:46:05 · Speaker 6

Yes

### 00:46:11 · Speaker 5

Uh it means that uh it means that your loss is half into five square twenty five square by uh sorry twenty five by two that's twelve point five. That means that there is some difference between your Y I and F theta of X I that you want to minimize. You want your F theta of X I to be as close to Y I as possible.

### 00:46:31 · Speaker 5

सो दैट इज व्हेन यू हैव अ लॉस दैट इज नॉन जीरो, दैट इज व्हाट यू वांट टू मिनिमाइज एस मच एस पॉसिबल।

### 00:46:38 · Speaker 5

And that is what will update your weights and it will tell those weights. See here with your current value you are giving an error of twelve point five. But can you can you update it so that that twelve point five becomes lower. Okay? Is that clear?

### 00:46:57 · Speaker 1

Yes, thank you.

### 00:46:57 · Speaker 2

with

### 00:46:58 · Speaker 5

Okay, sure. Okay, great. Let's go ahead. So, we so

### 00:47:04 · Speaker 2

This was our back propagation equation maybe.

### 00:47:13 · Speaker 2

So this is

### 00:47:15 · Speaker 6

Sir, this alpha is some constant

### 00:47:19 · Speaker 2

Yeah, I'll

### 00:47:20 · Speaker 2

welcome to yeah. So this

### 00:47:21 · Speaker 2

alpha over here.

### 00:47:23 · Speaker 2

hmm

### 00:47:24 · Speaker 2

This

### 00:47:24 · Speaker 2

is a constant

### 00:47:28 · Speaker 2

known as the learning rate

### 00:47:35 · Speaker 2

Okay

### 00:47:35 · Speaker 5

So, uh what basically we want to do is we want to update our weights in a way that a change in the weight reflects as a change in the loss function, okay? So, if I change uh W I J L is our general expression for any weight. If I increase my weight some amount, I want to see how much does the loss decrease.

### 00:48:04 · Speaker 6

Okay

### 00:48:05 · Speaker 5

So this is

### 00:48:08 · Speaker 5

So this is typically uh the

### 00:48:13 · Speaker 5

This is typically what neural networks do. When you change a weight by delta W, how much does the loss change and that loss is delta L. And we want to see the rate of change of the loss with respect to the weights.

### 00:48:29 · Speaker 5

which is nothing but the derivative of the loss with respect to the weight.

### 00:48:35 · Speaker 5

Okay? So this is the rate

### 00:48:39 · Speaker 2

of change

### 00:48:42 · Speaker 2

of loss

### 00:48:45 · Speaker 2

with respect to

### 00:48:48 · Speaker 5

eight. W I J in the layer L. Okay?

### 00:48:54 · Speaker 5

So, yeah, I hope learning rate is clear. So, every weight in the neural network is updated according to this. This is the gradient.

### 00:49:05 · Speaker 5

gradient descent

### 00:49:10 · Speaker 5

meaning that every weight is updated by some constant times the rate of change of the loss with respect to that weight. Okay? So I hope this much is clear. If you have any questions you can ask until now. I'll go on to

### 00:49:28 · Speaker 5

I'll go on to derive the

### 00:49:29 · Speaker 4

to derive the one query

### 00:49:31 · Speaker 5

Yeah, yeah, go ahead.

### 00:49:31 · Speaker 4

Yeah. This constant will be common for all layers.

### 00:49:36 · Speaker 5

Yes, yes, it will be constant for all layers, all weights.

### 00:49:41 · Speaker 4

and how do we find that? That's what we are going to discuss. Sorry.

### 00:49:45 · Speaker 5

No no no. uh This is this is not found. This is something that we set. Okay? And uh parameters that a user sets are known as hyper parameters.

### 00:49:58 · Speaker 2

Okay

### 00:50:01 · Speaker 5

meters and these are fixed by a user.

### 00:50:06 · Speaker 4

Got it

### 00:50:07 · Speaker 5

ओके. ओके. ओके ग्रेट. सो

### 00:50:08 · Speaker 4

ओके

### 00:50:09 · Speaker 6

So, one more question. Yeah, yeah, tell me. In one back propagation like every weight is reduced, this derivative is with respect to each separate weight or like it's a

### 00:50:12 · Speaker 5

Yeah, yeah, tell me.

### 00:50:24 · Speaker 6

she did the entire

### 00:50:25 · Speaker 5

Whatever

### 00:50:26 · Speaker 5

Good question. The this weight update is done usually for all the weights of the network. So every W I J L will have its own update because one is you you have the weight itself and then this term is specific to the weight W I J. So every weight is going to be updated in a neural network typically.

### 00:50:50 · Speaker 5

Okay

### 00:50:51 · Speaker 2

Okay

### 00:50:51 · Speaker 5

So for every weight you will have this update equation, you will have a different update equation and the gradient in the update equation is going to be with respect to a particular weight that you are choosing.

### 00:51:03 · Speaker 2

Okay. Okay.

### 00:51:05 · Speaker 5

Okay

### 00:51:05 · Speaker 5

Okay

### 00:51:06 · Speaker 5

Okay

### 00:51:07 · Speaker 3

Yeah, one follow up question on that. So just just assume that for some of the layers the gradients is really small and I have to freeze those layers. I don't want to calculate derivative for some of the weights but only to the initial layers of the network. So will that also be allowed?

### 00:51:10 · Speaker 5

Sure, sure.

### 00:51:16 · Speaker 5

small

### 00:51:26 · Speaker 5

that

### 00:51:28 · Speaker 5

Hmm

### 00:51:32 · Speaker 5

Sorry, I think I lost your voice

### 00:51:35 · Speaker 3

Yeah, I would repeat. So just assume that in case our gradients are very small for the deeper layers of the network and I I don't want to calculate the derivatives for the deeper layers. I only want to calculate the derivatives for the initial layers. So is there a freezing of the weights or freezing of the layers allowed during the back propagation that if I can just freeze the weights for some of the layers and only to a back propagation on few of the layers?

### 00:51:35 · Speaker 5

Yeah

### 00:51:37 · Speaker 5

So just

### 00:51:43 · Speaker 4

deep

### 00:51:45 · Speaker 4

and

### 00:51:55 · Speaker 4

Please

### 00:52:05 · Speaker 5

Of course you can do that. Of course you can. uh So uh and typically this is done in many applications where you freeze a portion of your network and only update certain weights. It could be the later part of the weights, later part of the network, it could be the earlier part of the network. You could definitely do anything you want and what weights you choose to update is completely up to you and it depends on the application that you are application that you are trying to learn a neural network for. Okay?

### 00:52:39 · Speaker 5

So you can definitely do it that way. uh And that is a very very good question actually. And many many applications in fact do this. So it is known as transfer learning.

### 00:52:56 · Speaker 2

So transfer learning where you freeze a part of a network

### 00:53:04 · Speaker 2

part of the network

### 00:53:08 · Speaker 2

and train few weights.

### 00:53:13 · Speaker 5

So yeah, uh that is a good point here. So you can freeze a part of the network, okay? So uh let's uh let's take an example and see how back propagation is done. And this back propagation that I'm going to talk about is general for any neural network. So any neural network will uh

### 00:53:34 · Speaker 5

will involve back propagation and it is the it is the foundation or it it is the foundation of all machine learning. Every machine learning algorithm definitely has back propagation and it it is the most important part of learning learning any task. So let's take this example again.

### 00:53:56 · Speaker 5

So what

### 00:53:56 · Speaker 2

what I want to do is I want to update

### 00:54:02 · Speaker 2

What I want to do is I want to find a way

### 00:54:07 · Speaker 2

to update

### 00:54:09 · Speaker 5

W one one of one. Okay? So, let's take this example and we are going to see how to update this weight. Now, what we need to do is we need to find the derivative of the loss with respect to this weight. Sorry, do W one one of one. So this is what we want to find and the way we find it is we see what is the path. So what we do is we find the path.

### 00:54:40 · Speaker 5

from W one one of one to the output

### 00:54:47 · Speaker 5

Y hat. Okay? So first we identify the path taking

### 00:54:54 · Speaker 5

taking us from the okay maybe I'll show it in a different color. So this is W one one.

### 00:55:00 · Speaker 5

So here is W one one. It goes like this to the output. Okay? So this is the path taking you from a weight to the output. And what we need to find is we need to find this derivative of L L which is the loss function with respect to W one one. Now the way we do this is using the chain rule of

### 00:55:25 · Speaker 5

derivatives

### 00:55:29 · Speaker 5

which which says that the derivative of L with respect to some weight is equal to derivative of loss with respect to what it came from. two L by it came from

### 00:55:43 · Speaker 5

it came from this path, right?

### 00:55:46 · Speaker 5

So that path is uh it came from W two one the way W two one. So I want to find okay sorry uh before that it came from A one three.

### 00:55:59 · Speaker 5

So do A one three. And what did A one three come from? It came from the weight.

### 00:56:07 · Speaker 5

one one of two and what did that weight come from?

### 00:56:15 · Speaker 5

that weight came from so this is W one one of two that came from node

### 00:56:22 · Speaker 2

A one two

### 00:56:25 · Speaker 2

two and what it

### 00:56:27 · Speaker 5

A one to come from

### 00:56:31 · Speaker 5

that came from W1

### 00:56:34 · Speaker 5

So this is the chain rule of derivatives. And you can see that you have you have a chain of derivatives that you need to compute. And since you are going backwards in the net network, this is back propagation. This is and more specifically it is the back propagation of error.

### 00:56:56 · Speaker 5

Okay. So you're propagating the error backwards in the network to the weight that you're interested in calculating the derivative for. And that helps you calculate the the gradient update for the weight. Now, like let's just give some example activations. For example, let let this be a sigmoid. Let this also be a sigmoid

### 00:57:28 · Speaker 5

And uh let's check what these uh what these derivatives are. So the first one is going to be

### 00:57:37 · Speaker 5

is derivative with respect to

### 00:57:42 · Speaker 5

A one

### 00:57:42 · Speaker 2

country of

### 00:57:45 · Speaker 2

half of

### 00:57:48 · Speaker 2

Y hat

### 00:57:53 · Speaker 2

I had minus

### 00:57:56 · Speaker 2

the prediction f theta of x which is a

### 00:57:59 · Speaker 5

one three

### 00:58:04 · Speaker 5

3 square

### 00:58:06 · Speaker 5

And what is A one three? We we wrote it earlier in our forward equations. In the forward process. Yeah, yeah.

### 00:58:17 · Speaker 5

which was this this is

### 00:58:19 · Speaker 2

A one three

### 00:58:21 · Speaker 2

So we had this expression

### 00:58:28 · Speaker 2

So since it was a sigmoid activation, we are going to

### 00:58:33 · Speaker 5

So this was A one three.

### 00:58:36 · Speaker 5

And uh what we want to calculate is this second term over here. So derivative of A one three with respect to one one of two is nothing but uh

### 00:58:49 · Speaker 5

with respect to one one two of sigmoid of this term over here. W one one two A one two plus W two one two A two two and here you will

### 00:59:00 · Speaker 4

Here also it should be Y cap, right? Sorry.

### 00:59:04 · Speaker 5

Hmm

### 00:59:06 · Speaker 4

here also D E L of D E

### 00:59:07 · Speaker 5

Oh sorry

### 00:59:10 · Speaker 5

skip making this out. Yeah, sorry. Thanks for pointing that out. So it is y minus a one three and so we have derivative of a one three with respect to w one one of two which is the derivative of the sigmoid with respect sigmoid of the net input at node a one three.

### 00:59:30 · Speaker 5

And uh you could try this as an exercise.

### 00:59:36 · Speaker 5

show that

### 00:59:41 · Speaker 5

derivative of the sigmoid function is the sigmoid times one minus sigmoid of x.

### 00:59:48 · Speaker 5

Okay, so you could try this as a simply as an exercise. So, which gives us

### 00:59:56 · Speaker 5

A one three by two W one one of two is equal to sigmoid of this term

### 01:00:04 · Speaker 5

this term into one minus sigmoid of that term. So we have the so we have the second term we got we got the first term initially we got the second term. Now the third term is W one one

### 01:00:18 · Speaker 2

Uh

### 01:00:22 · Speaker 2

Hmm

### 01:00:27 · Speaker 2

actually okay so we may not need this term we can just directly have

### 01:00:37 · Speaker 5

Okay. So, uh yeah, so similarly, we can find the derivative of this weight W one one two with respect to uh A one two this and then finally we can we can get this expression and if you multiply all of them, you get uh

### 01:00:55 · Speaker 5

you get derivative of L with respect to the weight one one of layer one. And what we do is

### 01:01:03 · Speaker 5

we just update W one one of layer one by the current weight my sorry. Yeah current weight minus

### 01:01:14 · Speaker 5

alpha, which is the learning rate, times derivative of L with respect to

### 01:01:20 · Speaker 5

dot

### 01:01:22 · Speaker 5

W one one of one and this is the

### 01:01:26 · Speaker 2

the

### 01:01:30 · Speaker 2

gradient descent update

### 01:01:34 · Speaker 2

So this is uh this is typically done multiple times. So I just this is one iteration.

### 01:01:47 · Speaker 2

one iteration of learning

### 01:01:53 · Speaker 2

and typically you do multiple iterations.

### 01:01:58 · Speaker 2

So this is typically

### 01:02:02 · Speaker 2

done

### 01:02:05 · Speaker 2

multiple times

### 01:02:10 · Speaker 2

until

### 01:02:13 · Speaker 5

until the weight converges. Or until convergence. So what what I mean by convergence is that the weight does not change too much as you keep updating. So what convergence

### 01:02:28 · Speaker 2

means is that

### 01:02:33 · Speaker 2

W one one of one

### 01:02:38 · Speaker 2

doesn't change significantly.

### 01:02:44 · Speaker 2

or in other words, or in other words, alpha times do L

### 01:02:49 · Speaker 5

by 2 W11

### 01:02:52 · Speaker 5

is very small.

### 01:02:57 · Speaker 5

So as you keep training the neural network, this gradient is going to become smaller and smaller and smaller until it reaches a number very very close to zero and that is when you're going to stop training and say that your neural network has learnt with respect to a certain weight. Okay? So yeah, so that I think we are out of time. It's nine thirty six. So

### 01:03:23 · Speaker 5

this uh so the this I hope this was helpful in explaining back propagation and how it helps uh neural how how it helps learn neural networks. So yeah. Uh any questions? Before we break for the day.

### 01:03:42 · Speaker 4

सर, वन क्वेश्चन लाइक इवन फॉर द वन डेटा, वन एक्स वाई, दिस अपेशन विल हैपन मल्टीपल टाइम्स, राइट?

### 01:03:42 · Speaker 6

Depression

### 01:03:45 · Speaker 5

Yeah.

### 01:03:47 · Speaker 5

Hello

### 01:03:51 · Speaker 5

Correct, yes. So, yeah, okay, that's a good point. Maybe I should mention that also. The training is done

### 01:04:00 · Speaker 2

training or sorry

### 01:04:04 · Speaker 2

training or weight updates

### 01:04:11 · Speaker 2

can be done on batches of examples.

### 01:04:17 · Speaker 2

batches of training data

### 01:04:21 · Speaker 5

Uh so what will happen here is that when you have a batch of examples every weight is updated using multiple inputs and outputs okay. So what will happen is that your loss function that you had over here right. Your okay maybe yeah here. So this loss function that you happened that is there here.

### 01:04:43 · Speaker 2

I don't know

### 01:04:45 · Speaker 5

So, uh it will be a sum over a sum I. I equal to one to N and N is known as the batch size.

### 01:04:57 · Speaker 5

Okay. So, yeah, that's a good point. You every weight can be updated using a batch of examples rather than a single example and in fact that actually improves your training because you're seeing how the weight a single weight is affected by multiple training examples so that it works on all of them at the same time.

### 01:05:21 · Speaker 5

Okay. Meaning your Y I is close to F theta of X I for all the X I's and Y I's in that batch of N examples. Okay. Okay. There's another question.

### 01:05:32 · Speaker 3

there's another question.

### 01:05:33 · Speaker 3

Yeah. So this means that uh if if we are able to pass the batch of data, you said that the weight updation happened properly. It means if we are passing the whole data set at once during a forward pass, it will it will adjust the weight even more better way instead of dividing the data into batches.

### 01:05:51 · Speaker 5

patches

### 01:05:53 · Speaker 5

Correct, you're absolutely right. So, uh actually having a larger batch size means it reduces the variance of the error. So that is uh there is some math involved in that and I'm hoping

### 01:06:08 · Speaker 5

Pratosh will cover that in class. So basically what you're saying is right. If you if you have a if you have some data set of ten examples and you pass all of them in the forward pass and then update your weight, it will typically lead to better learning and faster convergence.

### 01:06:27 · Speaker 5

of your neural network. Yeah, so you're right, yes. If you use more examples, the weights will be updated better.

### 01:06:36 · Speaker 5

Okay. Yeah, any more questions?

### 01:06:40 · Speaker 4

there is a quiz being mentioned on Saturday. Do you know anything about it what we should prepare or something relevant to that?

### 01:06:49 · Speaker 5

typically it will be whatever syllabus that has been covered till the till the class before the quiz. uh but I'm not sure if he has mentioned any specific portions. if you want I can I can ask Prathosh and let you know again. I I'll let you know in the group. okay?

### 01:07:08 · Speaker 6

Sure. Thank you.

### 01:07:10 · Speaker 5

So the quiz is at 9 AM on Saturday

### 01:07:10 · Speaker 3

So the quiz is at

### 01:07:14 · Speaker 5

Sure

### 01:07:14 · Speaker 6

Sure

### 01:07:15 · Speaker 3

And can you upload your notes onto the Teams what you are writing today?

### 01:07:20 · Speaker 5

Sure, sure, yeah. I will, I'll upload it, yeah.

### 01:07:24 · Speaker 5

I'll I'll post it on the group as a PDF.

### 01:07:29 · Speaker 3

Thank you

### 01:07:30 · Speaker 2

Okay

### 01:07:31 · Speaker 5

Okay, okay, okay, I think we can stop for today. So, yeah, all the best for the quiz on Saturday.

### 01:07:41 · Speaker 5

Thank you

### 01:07:41 · Speaker 2

Thank you sir. Thank you.

### 01:07:43 · Speaker 1

Thank you

### 01:07:44 · Speaker 6

Hmm

### 01:07:45 · Speaker 2

Thank you

### 01:07:52 · Speaker 0

Thank you
