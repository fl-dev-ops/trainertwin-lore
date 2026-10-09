---
id: oFNQkSalEV4
title: Deep Generative Models Tutorial Error back propagation
url: https://www.youtube.com/watch?v=oFNQkSalEV4
date: '2024-11-23'
duration: 01:07:57
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# Deep Generative Models Tutorial Error back propagation

## Transcript

### 00:00:02 · Speaker 1

And you can see my screen right Okay

### 00:00:10 · Speaker 1

Yeah, I hope you can see my screen. So what we'll be doing today is we'll be talking about back propagation.

### 00:00:37 · Speaker 1

And specifically, we'll be looking at backpropagation and neural networks. So I'll first talk about an example explaining why it is important and what is its role in deep learning. And finally, in the end, we'll hopefully solve one or two questions regarding backpropagation. So to begin with, the basic idea of deep learning is that you have some input data X.

### 00:01:07 · Speaker 1

So you have some uh

### 00:01:10 · Speaker 1

neural network

### 00:01:14 · Speaker 1

which gives you an output y and our goal is to

### 00:01:20 · Speaker 1

Our goal is to be able to predict why using this neural network using

### 00:01:29 · Speaker 1

using training data

### 00:01:32 · Speaker 1

Given by X I Y I

### 00:01:34 · Speaker 1

Which means that for every data point xi yi is its corresponding output that that you want to have but that you want to have predicted by the neural network so

### 00:01:47 · Speaker 1

Basically what the goal of neural networks

### 00:01:54 · Speaker 1

is to minimize some error

### 00:02:07 · Speaker 1

using the training data

### 00:02:13 · Speaker 1

and hopefully learn the neural network so that it can perform well on some test data or test examples. So just to give a basic idea of how learning works and how bad propagation is done, is that, let's assume

### 00:02:35 · Speaker 1

I'm learning to play a sport, let's say tennis, and I have

### 00:02:41 · Speaker 1

Maybe I I have a

### 00:02:43 · Speaker 1

I have a tennis court like this

### 00:02:48 · Speaker 1

And uh my goal is to hit the ball into the court

### 00:02:54 · Speaker 1

as much as I can and I want to prevent hitting the ball outside the

### 00:03:00 · Speaker 1

Something like this

### 00:03:03 · Speaker 1

What this means is that every shot that my opponent plays against me I want to return it and return it such that the ball lands inside the court

### 00:03:14 · Speaker 1

to avoid hitting the ball outside the court so what this means is that we are training our our muscles and our nervous system to be able to hit the ball inside the court and how do we learn this is

### 00:03:32 · Speaker 1

Optimizing this distance or the so-called error

### 00:03:38 · Speaker 1

So this error is what we want to minimize, or maybe the error is from somewhere inside the code. So this is what we want to minimize. And as we keep practicing,

### 00:03:52 · Speaker 1

Our muscles develop that skill to be able to hit inside the cord

### 00:03:59 · Speaker 1

at the same time minimizing this error so that is the goal of learning neural networks that is to accomplish some task

### 00:04:07 · Speaker 1

reducing some form of error so this is the this is the goal of a neural networks or deep learning in general

### 00:04:19 · Speaker 1

What are the different phases that a neural network has is that first, maybe I'll just copy this.

### 00:04:35 · Speaker 1

So a neural network is typically a

### 00:04:39 · Speaker 1

accompanied by two operations one is the forward pass

### 00:04:47 · Speaker 1

that takes input to output

### 00:04:52 · Speaker 1

Power it is input to output

### 00:04:58 · Speaker 1

And we have something known as the backward pass

### 00:05:08 · Speaker 1

The back left button

### 00:05:11 · Speaker 1

Goes from output or in in most cases the sorry error

### 00:05:21 · Speaker 1

The weights are input

### 00:05:26 · Speaker 1

The forward pass is what the neural network predicts and the backward pass is the feedback that you get from the prediction that is made by the neural network. So based on this feedback, whatever is given by the backward pass, we can choose to update our weights accordingly in order to reduce an error. So that is a basic idea of every neural network in just in simple terms. And we are going to focus on

### 00:05:56 · Speaker 1

we are going to focus on this backward pass and uh or or back propagation in general so

### 00:06:07 · Speaker 1

So what I'll do now is we'll set up a simple neural network and we will see how how backpropagation works.

### 00:06:16 · Speaker 1

The neural network is as follows you have some

### 00:06:20 · Speaker 1

You have some input let's say x and it's a two length feature vector so x1

### 00:06:30 · Speaker 1

And a neural network typically has these neurons or nodes.

### 00:06:38 · Speaker 1

You call neurons or nodes

### 00:06:42 · Speaker 1

And this is where multiple operations happen in the neural network. And it keeps, and every neural network has things known as layers. And each layer consists of multiple neurons, which are interconnected with each other. So this is typically how neural networks are. So this is known as the input layer.

### 00:07:20 · Speaker 1

This is the input layer

### 00:07:24 · Speaker 1

We have uh

### 00:07:26 · Speaker 1

We have two hidden layers

### 00:07:31 · Speaker 1

And finally we have one, let's say we have one output layer.

### 00:07:39 · Speaker 1

giving us y giving us y hat which is the prediction

### 00:07:46 · Speaker 1

This is the prediction or the output

### 00:07:51 · Speaker 1

And this is the input

### 00:07:54 · Speaker 1

So like I said, these neurons or nodes are where the operations happen. And each of these connections, so maybe I'll highlight it.

### 00:08:10 · Speaker 1

These connections are, these connections link two nodes through some weight characterized by W. So every node I'm going to notate with the letter A. So maybe.

### 00:08:32 · Speaker 1

I'll call this A

### 00:08:36 · Speaker 1

A1, this is the first node in the first layer. This is the second node in the first layer. So I call them A11 and A21. And these weights are denoted by Wij. It connects Wij connects

### 00:08:55 · Speaker 1

Nord I

### 00:08:58 · Speaker 1

Norgit

### 00:09:00 · Speaker 1

And of course, every weight is also associated with the layer number. So this, let's say this is layer one. So Wij one is node i to node j.

### 00:09:19 · Speaker 1

layer one

### 00:09:22 · Speaker 1

So this is the notation that we're going to follow. And similarly, the output layer, I can denote the, sorry, the hidden layer, I can denote by

### 00:09:33 · Speaker 1

the notation

### 00:09:35 · Speaker 1

A12, which is the first node of the second layer, and A22, which is the second node of the second layer. And finally, we have Y hat, which is the output. You could call it A13, but it's just simpler to call it Y hat, which is the output. So this is a notation we're going to follow.

### 00:09:58 · Speaker 1

Yeah, so this is the notation we will follow and the weights are denoted by Wij, Wij of the layer number. So this weight, for example,

### 00:10:10 · Speaker 1

For example this weight over here would be denoted by W

### 00:10:17 · Speaker 1

second layer so w2 one of two so uh now that we have uh

### 00:10:24 · Speaker 1

define the notations so let's move forward so like i said earlier the goal is to minimize some error using the using the training data and this error is also sometimes also called the optimization objective or it's also called the loss function

### 00:10:44 · Speaker 1

loss function

### 00:10:49 · Speaker 1

some

### 00:10:51 · Speaker 1

function of your prediction y hat and your input x

### 00:10:58 · Speaker 1

it is some it is some function of this along with the parameters okay so maybe i'll also mention that so uh let's say all the w ijs

### 00:11:09 · Speaker 1

are in some vector

### 00:11:16 · Speaker 1

uh they're the collection of all these pair of all these weight vectors uh w i j uh of of any layer l so let me call l

### 00:11:28 · Speaker 1

This theta is the set of all parameters in the neural network. So

### 00:11:37 · Speaker 1

and it's function of theta. Okay, so this is typically what is done in neural networks where you try to minimize this. So our goal is to

### 00:11:52 · Speaker 1

Minimize over all possible theta

### 00:11:56 · Speaker 1

function of

### 00:11:58 · Speaker 1

x and theta so you want to reduce

### 00:12:05 · Speaker 1

The loss function

### 00:12:11 · Speaker 1

function using

### 00:12:14 · Speaker 1

Training data

### 00:12:19 · Speaker 1

So let's maybe copy this

### 00:12:36 · Speaker 1

So the one of the most common loss functions that we use is known as the mean squared error.

### 00:12:52 · Speaker 1

In short we just call it MSE it is nothing but

### 00:12:59 · Speaker 1

I hat minus. So let's call the neural network

### 00:13:06 · Speaker 1

F theta parameterized by theta so F theta is the neural network

### 00:13:15 · Speaker 1

I minus

### 00:13:20 · Speaker 1

of x

### 00:13:22 · Speaker 1

So this is known as the mean squared error and this is what we want to minimize.

### 00:13:37 · Speaker 1

So uh in order to minimize any function the the most yeah uh there is a hand raised so

### 00:13:45 · Speaker 2

Yeah, I have a question. Can you please just tell me what the theta denotes? Sorry, I mean I did not understand it fully.

### 00:13:53 · Speaker 1

Okay, yeah, sure. So theta is the set of all weights, these connections I told you, right? These neural connections, this connection from A12 to A21 to A12. So things like these are connections between nodes of the neural network. And these are parameterized by some weight. So those weights are what, if you collect all those weights and put them into one set, those are

### 00:14:26 · Speaker 1

Yeah, sorry, sorry. Yeah, so I was saying the theta is the collection of all weight weights of the neural network. So I'll write theta as

### 00:14:38 · Speaker 1

W11 of 1, W121, W211, W22 of 1. So if you look here, this is going to be W22 of 1.

### 00:14:56 · Speaker 1

This weight vector connecting this is going to be W21 of 1. This is going to be W11 of 1. And this weight vector is going to be W12 of 1. Because it connects node i to node j. This is node 1. This is node 2.

### 00:15:15 · Speaker 1

the weight connecting node one of layer one to node one of layer two is going to be W11 of one, which is this. So by what I mean by theta is it is the collection of all these weights in the neural network.

### 00:15:32 · Speaker 1

So it's just a set of connections that we want to learn in the neural network. So I'll come to how we learn these. So does that answer your question?

### 00:15:42 · Speaker 2

Yes thank you

### 00:15:46 · Speaker 1

Okay, so moving forward, like I said, our goal is to minimize this loss function.

### 00:15:55 · Speaker 1

And that helps us reduce our error and learn a particular task properly. By learning a task, I mean these predictions, why that we get, we want them to be as we want them to be very good or close to what we desire. So that is the goal of learning a neural network.

### 00:16:18 · Speaker 1

So let's uh so so let me begin with a simple example maybe. So let's say uh this is your input uh x

### 00:16:31 · Speaker 1

Yeah so yeah

### 00:16:34 · Speaker 1

So let's say you have two inputs to your neural network, x1 and x2. Say this is your node. So these are your input nodes, a11, and this is a2 of 1, meaning layer 1. And then you have the similar neural network like this.

### 00:16:54 · Speaker 1

You have a single output node giving you y hat. And let's say that, okay, let me just notate these. This is A1 layer 2. This is A2 layer 2. And this weight over here is W111. This going from node 1 to node 2 is W12 of 1. Similarly, you have W21 of 1 and you have W22 of 1.

### 00:17:24 · Speaker 1

Similarly the output layer you have W 1 1 of 2 and W 2 1

### 00:17:34 · Speaker 1

So let's, so what we're going to do is we're going to assign some weights to these and then we will see how this neural network is trained.

### 00:17:44 · Speaker 1

So let's say this W11 is just

### 00:17:49 · Speaker 1

Okay, I'll erase these and maybe just put the weights on top of the arrows.

### 00:17:57 · Speaker 1

So this maybe is 1 this is 0.5 this is 0.5 and this is 1 similarly let these output weights also be 1 and 1

### 00:18:09 · Speaker 1

So for the input nodes, we have A11 is simply equal to X1.

### 00:18:16 · Speaker 1

A to one simply equals X to

### 00:18:20 · Speaker 1

So this is what we have this is uh this is the input layer

### 00:18:29 · Speaker 1

Then the notion of nodes in a neural network is as follows. It combines different nodes of the previous layer through something known as a linear combination or a weighted sum of values in the previous layer. What I mean by that is

### 00:18:50 · Speaker 1

Let's take A12 for example which is uh this node over here

### 00:18:56 · Speaker 1

A one two equals a weighted sum of a one one

### 00:19:04 · Speaker 1

A21 and the weights are exactly what is there on the arrows connecting the corresponding nodes which is W111 and W21 of 1

### 00:19:17 · Speaker 1

So this is typically how A21 is defined as. But one important thing to notice before, it is not just a linear combination of this. It is some function g of this function. OK. So this g function.

### 00:19:38 · Speaker 1

is known as an activation function

### 00:19:48 · Speaker 1

And depending on the application or what you want your neural network to achieve, these activation functions could be different. For example, you have sigmoid.

### 00:20:03 · Speaker 1

have a

### 00:20:05 · Speaker 1

have tanh and each of these activation functions do something different

### 00:20:14 · Speaker 1

So sigmoid is uh

### 00:20:19 · Speaker 1

sigma mod of x is 1 by 1 plus e power minus x and the rello function

### 00:20:30 · Speaker 1

is nothing but uh

### 00:20:33 · Speaker 1

g of x equals x when x greater than or equal to 0, 0 if x is less than 0.

### 00:20:42 · Speaker 1

And uh

### 00:20:47 · Speaker 1

And yeah, similarly you have other activation functions like tanh, exp, exponential, linear unit, and you have many more, you have so many activation functions that are used on the linear combination that you get from the previous layer. Okay, so this is the activation function. This is sometimes also known as the net input to the node.

### 00:21:17 · Speaker 1

And what we have here is the node output

### 00:21:26 · Speaker 1

is n the node output are simply the

### 00:21:30 · Speaker 1

Okay, so let's not call it output. Let's just keep it as node output.

### 00:21:36 · Speaker 1

Uh this is yeah uh one question yeah or two questions

### 00:21:43 · Speaker 3

Hi sorry am I on the

### 00:21:45 · Speaker 1

Yeah yeah yeah tell me

### 00:21:46 · Speaker 3

Yeah, yeah, tell me. I just wanted to know about why we in the middle layer, right? Can we scroll a little up? I wanted to see that figure. Yeah, why is there no connection between A1, 2 and A2, 1? Can that also be called as a neural network? I mean...

### 00:22:03 · Speaker 1

No, typically that's not how... Okay, so let me give you the... Let me give you a real-life example. So every living being has a nervous system, right?

### 00:22:18 · Speaker 1

In that nervous system uh you have you you have some neurons that are like this

### 00:22:27 · Speaker 1

And then you have these synaptic connections connecting one nerve to another

### 00:22:33 · Speaker 3

Okay

### 00:22:34 · Speaker 1

So, okay, I think my screen is, yeah, okay. So what these nodes are is actually this point.

### 00:22:46 · Speaker 1

the starting of the branch that connects one node to another node. So these nodes are typically like, let's take the optic nerve for example. So the optic nerve is typically a bunch of nerves. So these bunch of nerves have separate nodes in each of them and they are typically when you have multiple connect, when you have a bunch of nerves like this, you don't really

### 00:23:16 · Speaker 1

need these two nodes to be connected say

### 00:23:21 · Speaker 1

because the the main reason is if let's say let's say some problem happens with this nerve then if these two are connected then this whole this whole line is gone like this whole since this entire nerve is connected then this could be this could cause problems so

### 00:23:44 · Speaker 1

Like essentially what we are trying to do is we are trying to parallelize these nodes so that if one thing goes wrong, you can you can always have you can always learn with another node or things like that. But of course.

### 00:23:49 · Speaker 3

Okay

### 00:23:59 · Speaker 1

This is this is not not an exact answer to your question, but this the typically this is the convention that you follow in in deep learning and in and neural networks the you don't have Okay, so you don't have connection between these because you have a you have a very nice dense connection between these nodes between layers of nodes

### 00:24:24 · Speaker 3

But to the end of the day

### 00:24:24 · Speaker 1

Oh yeah

### 00:24:27 · Speaker 3

Sorry, just to follow up. And the difference between A12 and A22 is actually the weights currently, right? Because both are giving the same inputs, but with a different weight.

### 00:24:27 · Speaker 1

He hasn't

### 00:24:41 · Speaker 3

But the bait can differ right that's it right

### 00:24:42 · Speaker 1

Okay

### 00:24:46 · Speaker 1

Yeah, correct. So you can notice that if x1 and x2 are different, then a12 and a22 are different, right? Because if you look at a12, it is some function of w11a1 and w21a2. But if you look at a22, it is the activation of, so a22 is this one, right? So a22 is this one. And it comes from,

### 00:25:16 · Speaker 1

Uh so what are the things contributing what are the nodes contributing towards this

### 00:25:23 · Speaker 1

So

### 00:25:25 · Speaker 1

So in this case it's going to be a W121

### 00:25:31 · Speaker 1

A11 plus

### 00:25:34 · Speaker 1

W uh two two one

### 00:25:37 · Speaker 1

A21. Okay. So you can see that these two are different, right?

### 00:25:43 · Speaker 3

Sure yeah

### 00:25:45 · Speaker 1

Yeah so

### 00:25:47 · Speaker 1

Yeah, okay. So basically, this is how we go forward in a neural network, which is taking the input to the output. And this entire process is known as the forward process.

### 00:26:06 · Speaker 1

So the forward process takes you from input to the hidden layers. Of course, you could have multiple hidden layers here. You can have A12, A13, A14, and then you can have iHat and things like that. So those are deeper neural networks. And that's where the term deep learning stems from. And when you have more than three or four layers, you typically go into the realm of deep learning.

### 00:26:35 · Speaker 1

Yeah, so this is a forward process. And so let me just complete the equations for sake of completeness. So similarly, this is W11 from layer 2. This is weight connecting node 2 to node 1 of layer 3 from layer 2. Okay, so Y hat.

### 00:27:00 · Speaker 1

is again some function of W one one two

### 00:27:09 · Speaker 1

but it multiplies the this node over here which is a1 two

### 00:27:15 · Speaker 1

Plus W212 of A22. Okay, so this is the final output.

### 00:27:24 · Speaker 1

output or you call it the prediction of the neural network

### 00:27:30 · Speaker 1

Okay, so this is the entire forward process taking you from the inputs.

### 00:27:37 · Speaker 1

from the inputs to the output

### 00:27:41 · Speaker 1

Okay, so typically our input is denoted by x and it's a vector containing x1 and x2. So you could call this input data.

### 00:27:58 · Speaker 1

Or you could call it features

### 00:28:02 · Speaker 1

input features

### 00:28:06 · Speaker 1

So yeah, these names are used interchangeably. So you just, basically this is the input. So the input could be a vector, it could be a single number, it could be an image, it could be anything, it could be a video, it could be an x-ray scan, it could be anything. So depending on the dimension of the input, your neural network will also change the nature of its weights. And one important thing is that for every

### 00:28:37 · Speaker 1

So I just

### 00:28:41 · Speaker 1

Copy this once again

### 00:28:47 · Speaker 1

Yeah sure go ahead

### 00:28:49 · Speaker 3

an additive property where g of w112 a12 can we can we move uh w weights like can we apply the function on the different weights then add them like g of w11 a1 plus g of w21 a2

### 00:29:08 · Speaker 1

Sure, you can, definitely. It is possible, but generally in neural networks, for a particular layer, you have a particular G.

### 00:29:19 · Speaker 1

So for example, layer one, so okay, maybe this layer could have a ReLU activation function, and maybe this can have a sigmoid.

### 00:29:32 · Speaker 1

So g is equal to ReLU here, g is equal to sigmoid and you can you you you generally have different activation functions for different layers rather than different activation functions for different nodes.

### 00:29:51 · Speaker 1

There's another question

### 00:29:53 · Speaker 2

Uh, just a small query that how initially we are assigning these weights? I mean, I understand later maybe through the backpropagation we correct it, but initially we have to assign some numbers against these weights, right?

### 00:30:07 · Speaker 1

Yeah yeah so I I was so that is gonna be my follow up discussion okay

### 00:30:12 · Speaker 2

Okay okay sorry

### 00:30:13 · Speaker 1

These beta yeah no it's okay it's a good question actually so

### 00:30:19 · Speaker 1

So one important note is that weights are initialized

### 00:30:26 · Speaker 1

So what I mean by initialized is they are assigned something.

### 00:30:33 · Speaker 1

So you are assigning some weights

### 00:30:41 · Speaker 1

At the start

### 00:30:44 · Speaker 1

So typically what people do in neural networks is that these weights are selected randomly.

### 00:30:53 · Speaker 1

Or I should say initialized randomly

### 00:31:05 · Speaker 1

So uh, yeah, uh, I have a couple more questions, yeah.

### 00:31:10 · Speaker 4

Uh sir what is the significance of this activation function like will it be covered later on

### 00:31:19 · Speaker 1

Uh yeah, I mean, okay, so the role of the activation function is to limit the these outputs, these node outputs to be in a certain range. So you don't

### 00:31:34 · Speaker 1

Yeah, sorry, I got cut off. Yeah, so I was saying the role of these activation functions is to somewhat limit the values of these node outputs. So you have these node outputs, right? A1, 2, 8, A2, 2, and all these things. So you want to limit them to certain range. For example, if you take the sigmoid activation, so g of x is, let's say sigmoid of x, which is 1 by 1 plus e power minus x, what

### 00:32:04 · Speaker 1

What this basically does is that uh

### 00:32:10 · Speaker 1

Okay let me lose this color

### 00:32:14 · Speaker 1

What this basically does is if you have, let's say this is your X and Y axis.

### 00:32:23 · Speaker 1

Okay y is equal to sigma of x what this does is that it takes all your values from

### 00:32:31 · Speaker 1

from minus infinity to infinity and it brings it to the range of zero to one okay so in in neural networks you don't want your values to blow up so that your y hat becomes like one lakh ten lakhs and all so you you don't want that to happen so you want to control your you want to control

### 00:32:52 · Speaker 3

I'm not sure what that means

### 00:32:55 · Speaker 4

We want to like contain it in some range

### 00:32:58 · Speaker 1

Good yes

### 00:33:02 · Speaker 1

And so activations basically control your node output

### 00:33:12 · Speaker 1

So these activations are actually very important because this sigmoid, right, this is the sigmoid function.

### 00:33:20 · Speaker 1

This is used typically at the output of

### 00:33:25 · Speaker 1

of classifiers

### 00:33:29 · Speaker 1

So classifier is basically something that gives you a decision. So it gives you a decision and you basically want a yes or no decision.

### 00:33:39 · Speaker 1

And so, for example, yes could be close to one and no could be close to zero. So the sigmoid activation function is a perfect choice as an activation function in these classifier functions. So SER will be covering classifiers later on. And maybe that time you'll encounter the sigmoid activation. So depending on what you want your network to do, you will choose different activation.

### 00:34:09 · Speaker 1

for different layers of your neural network

### 00:34:13 · Speaker 1

So for image problems, you might want to use ReLU. So for

### 00:34:20 · Speaker 1

Uh image oh sorry

### 00:34:22 · Speaker 1

or image networks

### 00:34:26 · Speaker 1

You might want to use ReLU

### 00:34:29 · Speaker 1

which is basically anything less than zero it gives zero and anything greater than zero it gives the it gives the same output so this is the relu relu function so x and g of x

### 00:34:46 · Speaker 1

So this is so depending on your application you will choose you will decide to choose different activation functions. So hope that's clear. Yeah there's another question.

### 00:34:59 · Speaker 2

they are very small in number they're not big I believe the reason you just say you don't want to blow it up is that correct or and when so

### 00:35:12 · Speaker 1

And when so yeah I your voice was breaking in the middle can you repeat the first part of your question?

### 00:35:19 · Speaker 2

generally

### 00:35:20 · Speaker 1

what I have seen the weight and biases for this neural network they are very small in numbers they are not pretty big correct correct so so there has to be a reason behind that I believe you just explained we don't want to explode the final y hat correct okay and second thing is that when we initialize it randomly do we also define what kind of thing I'm looking

### 00:35:42 · Speaker 3

Fine

### 00:35:45 · Speaker 1

Using your voice I can't hear

### 00:35:50 · Speaker 1

Let me try once again

### 00:35:54 · Speaker 1

So when we initialize these weights randomly, do we also define the range of between it's going to be?

### 00:36:03 · Speaker 1

Correct. Yes, we do, we do. In many applications, you use some weights between zero and one.

### 00:36:19 · Speaker 1

IJ belongs to some let's say minus one to one or zero to one.

### 00:36:27 · Speaker 1

So typically we choose weights in this range and

### 00:36:32 · Speaker 1

Yeah we initialize uh weights randomly such that they're in this range minus one to one or zero to one just so that it's small and

### 00:36:41 · Speaker 1

You you don't have something known as a gradient explosion you want to avoid this gradient explosion

### 00:36:49 · Speaker 1

So I'll I'll come to what this is later on or it it'll also be covered in the course

### 00:36:56 · Speaker 1

So we want to prevent this

### 00:37:01 · Speaker 1

to prevent gradient explosion so we uh we choose the weights to be a bit in some range where they're very small yeah so i hope that answers your question for now so uh we'll i mean uh this this you will encounter in almost any application where the weights are going to be very small and you start off with those weights and then you you start learning your network through back propagation

### 00:37:29 · Speaker 1

So now let's move to let's move to backpropagation

### 00:37:43 · Speaker 1

So let's go back to our neural network that was over here.

### 00:37:57 · Speaker 1

Yeah, so this was our net network and if you recall we had a loss function L which was the mean squared error between y hat and f theta of x where f theta of x is taking your is the entire neural network this is f theta of x this takes your input x where if you recall x was the was the vector x1 x2 this is the vector this is a vector

### 00:38:27 · Speaker 1

vector

### 00:38:30 · Speaker 1

Input vector of x1, x2, taking you to the prediction y hat. This is the prediction.

### 00:38:38 · Speaker 1

So, what you want to, what we basically want to do is, let's say we have some training.

### 00:38:47 · Speaker 1

And for now, let us assume we only have one training data sample, which is for the input x, I expect the output y. So this is our training data. So typically, you call it xi yi. And you have n such examples. So your training data will typically look like x1. For x1, you desire the output y1. For x2, you desire the output y1.

### 00:39:17 · Speaker 1

put whiteo and so on

### 00:39:21 · Speaker 1

Okay, so this is our training data, but for now let's just assume we have a single training data sample. Assume your data is just x, y, a single example.

### 00:39:37 · Speaker 1

Single training example

### 00:39:41 · Speaker 1

Now our goal is to minimise

### 00:39:49 · Speaker 1

L is equal to half of Y hat minus F theta of X

### 00:39:58 · Speaker 1

So this is what we want to minimize and how do we minimize any function? We compute its derivative with respect to what we can optimize over or what we can change in the network. And what can we change in the network? We can change theta or the weights.

### 00:40:16 · Speaker 1

So this is what we can change

### 00:40:19 · Speaker 1

So the natural step is to take the derivative of the loss with respect to some parameters in the network. So let's say w ij of l which is the weight ij weight from node i of layer l to node j of layer l plus one and we take this derivative and

### 00:40:47 · Speaker 1

What we do is we we take we compute this derivative

### 00:40:52 · Speaker 1

And then we do something known as the gradient descent.

### 00:41:00 · Speaker 1

which is any weight w ij of L is updated as w ij L minus some weight alpha times this derivative.

### 00:41:17 · Speaker 1

I J L and this is known as

### 00:41:22 · Speaker 1

Back propagation

### 00:41:26 · Speaker 1

This is back propagation through

### 00:41:31 · Speaker 1

Gradient descent

### 00:41:35 · Speaker 1

Yeah that's a question

### 00:41:38 · Speaker 4

Uh so in this mini uh loss minimize loss function this y hat is also the output of this neural network

### 00:41:45 · Speaker 1

Yeah

### 00:41:48 · Speaker 4

I had is also the output of neural network right

### 00:41:54 · Speaker 1

Yeah I was wondering

### 00:41:55 · Speaker 4

So cool

### 00:41:56 · Speaker 1

Yeah yeah I sorry I missed the Y hat I wanted it to be Y

### 00:42:01 · Speaker 4

Why not Yeah

### 00:42:02 · Speaker 1

So yeah, yeah, yeah, sorry, sorry, sorry, my mistake. This should be white. Yeah, okay, thank you.

### 00:42:16 · Speaker 3

Sir, I have one question. So I have a general doubt. So when we calculate the loss in a network, the network is not aware of the loss function, right? Initially, we just calculate a numerical loss and it's some numerical data which we have.

### 00:42:36 · Speaker 3

Correct. And then how do we calculate the gradient on some numerical data with respect to a parameter? Just wondering.

### 00:42:47 · Speaker 1

So, okay, yeah, that's a good question. The laws is what we define.

### 00:42:54 · Speaker 1

is user defined so this this is a function and it is a function of x and theta correct so uh regardless of regardless of uh whether your data is numerical or or synthesized or analytical whatever it may be you can always compute the derivative of your loss with respect to your parameters so this since this is what we define and it is a we define we can we can compute the gradient of

### 00:43:24 · Speaker 1

this and we can and we can use that to update our neural network okay

### 00:43:31 · Speaker 1

Uh is that clear or no

### 00:43:34 · Speaker 3

Yes sir

### 00:43:36 · Speaker 1

Yeah another question

### 00:43:47 · Speaker 2

you obviously

### 00:43:53 · Speaker 1

So you have your prediction, right? Y hat from the network. So this is the prediction. And what is Y hat? Y hat is actually F theta of X. It is what your neural network gives you. So what your neural network gives you is the prediction. And what you have is your training data, X, X, I, Y, I. And what you'll do is you'll compare

### 00:44:20 · Speaker 1

You'll compare prediction

### 00:44:24 · Speaker 1

Y hat equal to f theta of xi. Xi is some training example that you have.

### 00:44:33 · Speaker 1

The ground truth

### 00:44:38 · Speaker 1

the ground truth y i okay so maybe let me call it y hat i so what you will compare is you will compare the loss between y hat i and y i which is the squared error

### 00:44:53 · Speaker 1

y hat i minus f theta of

### 00:44:57 · Speaker 1

So you have your prediction out here

### 00:45:03 · Speaker 1

sorry oh I shouldn't use this is yi sorry and this is your true label

### 00:45:11 · Speaker 1

label or ground truth

### 00:45:16 · Speaker 1

So ground truth is what we desire and prediction is what your neural network has given you so you have an idea of which one is greater greater or lesser

### 00:45:27 · Speaker 1

Uh is that clear

### 00:45:30 · Speaker 3

Uh yes but the loss will be the same like even if the F F naught the prediction is higher for

### 00:45:37 · Speaker 2

example by five compared to the truth or if it's lower by five the loss function will be will give you the same value right

### 00:45:45 · Speaker 1

Yes it will yeah

### 00:45:47 · Speaker 2

So then how do we know like we have to increase the weights or we have to decrease the weights and that's enough

### 00:45:54 · Speaker 1

So that is what, so the moment you have some error that is not zero, that is greater than zero, it means that you are off from your ground truth, correct? So you gave the example that f theta of xi might be five higher or five lower. It means that your loss is half into five square, 25 square by, sorry, 25 by two, that's 12.5. That means that there is some difference between your

### 00:46:24 · Speaker 1

yi and f theta of xi that you want to minimize. You want your f theta of xi to be as close to yi as possible. So that is when you have a loss that is non-zero, that is what you want to minimize as much as possible. And that is what will update your weights and it will tell those weights. See here with your current value, you are giving an error of 12.5, but can you can you update it so that that 12.5 becomes lower. Okay.

### 00:46:54 · Speaker 1

Is that clear

### 00:46:57 · Speaker 3

Oh yes thank you

### 00:46:58 · Speaker 1

Okay, sure. Okay, great. Let's go ahead. So we, so this was our back propagation equation, maybe.

### 00:47:13 · Speaker 1

So this is

### 00:47:15 · Speaker 4

where this alpha is some constant

### 00:47:19 · Speaker 1

Yeah, I'll I'll come to yeah so this alpha over here

### 00:47:24 · Speaker 1

This is a constant

### 00:47:28 · Speaker 1

known as the learning rate

### 00:47:36 · Speaker 1

So what basically we want to do is we want to update our weights in a way that a change in the weight reflects as a change in the loss function. Okay. So if I change Wijl as our general expression for any weight, if I increase my weight some amount, I want to see how much does the loss decrease.

### 00:48:05 · Speaker 1

So this is uh

### 00:48:08 · Speaker 1

So this is typically uh uh

### 00:48:13 · Speaker 1

This is typically what neural networks do. When you change a weight by delta W, how much does the loss change? And that loss is delta L. And we want to see the rate of change of the loss with respect to the weights, which is nothing but the derivative of the loss with respect to the weight.

### 00:48:35 · Speaker 1

So this is the rate

### 00:48:40 · Speaker 1

of change

### 00:48:43 · Speaker 1

of loss

### 00:48:45 · Speaker 1

with respect to

### 00:48:49 · Speaker 1

W I J in the layer N

### 00:48:54 · Speaker 1

So yeah, I hope learning rate is clear. So every weight in the neural network is updated according to this. This is the gradient.

### 00:49:05 · Speaker 1

Gradient descent

### 00:49:10 · Speaker 1

Meaning that every weight is updated by some constant times the rate of change of the loss with respect to that weight.

### 00:49:19 · Speaker 1

So I hope this much is clear. If you have any questions you can ask until now. I'll go on to I'll go on to derive the

### 00:49:29 · Speaker 3

One query

### 00:49:31 · Speaker 1

Yeah yeah go ahead

### 00:49:33 · Speaker 3

This constant will be common for all layers

### 00:49:36 · Speaker 1

Yes yes it will be constant for all layers all weights

### 00:49:41 · Speaker 3

And how do we find that? That's what we are going to discuss today. Sorry.

### 00:49:45 · Speaker 1

No, no, no, this is this is not found. This is something that we set. OK. And parameters that a user sets are known as hyper parameters.

### 00:50:01 · Speaker 1

and these are fixed by a user.

### 00:50:09 · Speaker 1

Okay there

### 00:50:09 · Speaker 4

So I'm not a shot

### 00:50:10 · Speaker 1

So

### 00:50:12 · Speaker 1

Yeah

### 00:50:13 · Speaker 4

In one back propagation like every weight is reduced this derivative is with respect to each separate weight or like it's a

### 00:50:24 · Speaker 4

City and governorship

### 00:50:25 · Speaker 1

A good question. The this weight update is done usually for all the weights of the network. So every Wijl will have its own update because one is you have the weight itself and then this term is specific to the weight Wij. So every weight is going to be updated in a neural network typically.

### 00:50:52 · Speaker 1

So for every weight, you will have this update equation. You will have a different update equation. And the gradient in the update equation is going to be with respect to a particular weight that you are choosing.

### 00:51:07 · Speaker 3

Yeah, one follow-up question on that. So just assume that for some of the layers, the gradients is really small and I have to freeze those layers. I don't want to calculate derivative for some of the weights, but only to the initial layers of the network. So will that also be allowed?

### 00:51:32 · Speaker 1

Sorry I think I lost your voice

### 00:51:35 · Speaker 3

yeah i would repeat uh so just assume that uh in case our gradients are very small for the deeper layers of the network and i i don't want to calculate the derivatives for the deeper layers i only want to calculate the derivatives for the initial layers so is there a freezing of the weights or freezing of the layers allowed during the back propagation that if i can just freeze the weights for some of the layers and only get to a back propagation on few of the layers

### 00:52:05 · Speaker 1

Of course you can do that. Of course you can. So, and typically this is done in many applications where you freeze a portion of your network and only update certain weights. It could be the later part of the weights, later part of the network. It could be the earlier part of the network. You could definitely do anything you want. And what weights you choose to update is completely up to you. And it depends on the application that you are trying to

### 00:52:35 · Speaker 1

Learn a neural network for okay

### 00:52:39 · Speaker 1

So you can definitely do it that way. And that is a very, very good question actually. And many, many applications in fact do this. So it is known as transfer learning.

### 00:52:56 · Speaker 1

So transfer learning where you freeze a part of the network

### 00:53:05 · Speaker 1

part of the network

### 00:53:08 · Speaker 1

and train few epochs

### 00:53:13 · Speaker 1

So yeah, that is a good point. Yeah. So you can freeze a part of the network. Okay. So let's let's take an example and see how back propagation is done. And this back propagation that I'm going to talk about is general for any neural network. So any neural network will will involve back propagation and it is the it is the foundation or it is the foundation of all machine learning. Every machine learning algorithm

### 00:53:43 · Speaker 1

definitely has backpropagation and it is the most important part of learning learning any task so let's take this example again

### 00:53:56 · Speaker 1

So what I want to do is I want to update

### 00:54:02 · Speaker 1

What I want to do is I want to find a way

### 00:54:07 · Speaker 1

So update

### 00:54:09 · Speaker 1

w11 of 1. Okay, so let's take this example and we are going to see how to update this weight. Now, what we need to do is we need to find the derivative of the loss with respect to this weight. Sorry, dou w11 of 1. So this is what we want to find. And the way we find it is we see what is the path. So what we do is we find the path.

### 00:54:40 · Speaker 1

from W one one of one

### 00:54:44 · Speaker 1

output

### 00:54:47 · Speaker 1

Okay, so the first we identify the path taking

### 00:54:54 · Speaker 1

taking us from the okay maybe I'll show it in a different color so this is w11 so here is w11 it goes like this to the output okay so this is the path taking you from a weight to the output and what we need to find is we need to find this derivative of l l which is the loss function with respect to w11 now the way we do this is using the chain rule of

### 00:55:25 · Speaker 1

derivatives

### 00:55:29 · Speaker 1

It says that the derivative of L with respect to some weight is equal to derivative of loss with respect to what it came from. 2L by it came from it came from this path, right?

### 00:55:46 · Speaker 1

So that path is, it came from W21, the weight W21. So I want to find, okay, sorry, before that it came from A13.

### 00:55:59 · Speaker 1

So do A1

### 00:56:02 · Speaker 1

And what did A13 come from? It came from the weight.

### 00:56:07 · Speaker 1

one one of two and what did that weight come from

### 00:56:15 · Speaker 1

That way it came from, so this is W11 of two, that came from node A12.

### 00:56:25 · Speaker 1

And what did A12 come from?

### 00:56:31 · Speaker 1

That came from W one

### 00:56:34 · Speaker 1

So this is the chain rule of derivatives. And you can see that you have a chain of derivatives that you need to compute. And since you're going backwards in the net network, this is back propagation. And more specifically, it is the back propagation of error.

### 00:56:56 · Speaker 1

Okay, so you're propagating the error backwards in the network to the weight that you're interested in calculating the derivative for. And that helps you calculate the...

### 00:57:10 · Speaker 1

the gradient update for the weight. Now like let's just give some example activations. For example, let this be a sigmoid. Let this also be a sigmoid.

### 00:57:28 · Speaker 1

And let's check what these what these derivatives are. So the first one is going to be

### 00:57:37 · Speaker 1

is uh derivative with respect to

### 00:57:42 · Speaker 1

A13 of

### 00:57:45 · Speaker 1

Half off

### 00:57:48 · Speaker 1

I had

### 00:57:53 · Speaker 1

I had minus

### 00:57:56 · Speaker 1

the prediction f theta of x which is a one three

### 00:58:04 · Speaker 1

three squared and what is a one three we we wrote it earlier in our forward equations in the forward process here yeah

### 00:58:17 · Speaker 1

Uh which was this this is uh A one three

### 00:58:21 · Speaker 1

So we had this expression

### 00:58:28 · Speaker 1

So since it was a sigmoid activation we are going to

### 00:58:33 · Speaker 1

So this was A13

### 00:58:36 · Speaker 1

And what we want to calculate is this second term over here. So derivative of A13 with respect to 11 of 2 is nothing but

### 00:58:50 · Speaker 1

respect to one one two of sigmoid of this term over here w112 a12 plus w212 a22 and uh uh

### 00:59:00 · Speaker 3

Here you go Y cap right sorry

### 00:59:06 · Speaker 3

Here also DEL of D

### 00:59:07 · Speaker 1

of oh sorry let's keep making this yeah sorry thanks for pointing that out so it is y minus a13 and uh so we have derivative of a13 with respect to w11 of 2 which is the derivative of the sigmoid with respect sig sigmoid of the net input at node a13

### 00:59:30 · Speaker 1

And uh you could try this as an exercise

### 00:59:36 · Speaker 1

I'll show that uh

### 00:59:41 · Speaker 1

Derivative of the sigmoid function is the sigmoid times one minus sigmoid of x

### 00:59:48 · Speaker 1

Okay, so you could try this as a simply as an exercise. So which gives us a13 by dou w11 of 2 is equal to a sigmoid of this term.

### 01:00:04 · Speaker 1

this term into one minus sigmoid of that term. So we have the second term. We got the first term initially. We got the second term. Now the third term is W11.

### 01:00:27 · Speaker 1

No actually okay so we may not need this term we can just directly have

### 01:00:37 · Speaker 1

So yeah, so similarly we can find the derivative of this weight w112 with respect to

### 01:00:45 · Speaker 1

a1 to this and then finally we can we can get this expression and if you multiply all of them you get

### 01:00:55 · Speaker 1

You get derivative of L with respect to the weight one one of layer one. And what we do is

### 01:01:03 · Speaker 1

We just update W11 of layer one by the current weight minus alpha, which is the learning rate times derivative of L with respect to dot W11 of one. And this is the

### 01:01:30 · Speaker 1

Gradient descent update

### 01:01:34 · Speaker 1

So this is typically done multiple times. So this is one iteration.

### 01:01:47 · Speaker 1

One iteration of learning

### 01:01:53 · Speaker 1

And typically you do multiple iterations

### 01:01:58 · Speaker 1

So this is typically

### 01:02:06 · Speaker 1

multiple times

### 01:02:10 · Speaker 1

Until

### 01:02:13 · Speaker 1

until the weight converges or until convergence. So what I mean by convergence is that the weight does not change too much as you keep updating.

### 01:02:26 · Speaker 1

So what convergence means is that

### 01:02:33 · Speaker 1

W one one of one

### 01:02:39 · Speaker 1

doesn't change significantly.

### 01:02:44 · Speaker 1

Or in other words or in other words alpha times dou L by dou W 1 1

### 01:02:52 · Speaker 1

very small

### 01:02:57 · Speaker 1

So as you keep training the neural network, this gradient is going to become smaller and smaller and smaller until it reaches a number very, very close to zero. And that is when you're going to stop training and say that your neural network has learnt with respect to a certain weight. Okay. So yeah. So that, I think we are out of time. It's 9.36. So.

### 01:03:24 · Speaker 1

this uh so the this i hope this was helpful in explaining back propagation and how it helps uh neural how how it helps learn neural networks so yeah uh any questions before we break for the day

### 01:03:42 · Speaker 4

So one equation like even for the one data one x y

### 01:03:42 · Speaker 1

Or vanilla

### 01:03:47 · Speaker 4

This adaptation will happen multiple times right

### 01:03:51 · Speaker 1

Correct, yes. So yeah, okay, that's a good point. Maybe I should mention that also. The training is done.

### 01:04:00 · Speaker 1

Training

### 01:04:04 · Speaker 1

Training or weight updates

### 01:04:11 · Speaker 1

can be done on batches of examples

### 01:04:17 · Speaker 1

Batches of training data

### 01:04:21 · Speaker 1

So what will happen here is that when you have a batch of examples, every weight is updated using multiple inputs and outputs. Okay. So what will happen is that your loss function that you had over here, right? Yeah. Okay. Maybe yeah here. So this loss function that you happened that is there here.

### 01:04:46 · Speaker 1

So it will be a sum over a sum i, i equal to 1 to n, and n is known as the batch size.

### 01:04:58 · Speaker 1

So yeah, that's a good point. Every weight can be updated using a batch of examples rather than a single example. And in fact, that actually improves your training because you're seeing how the weight, a single weight is affected by multiple training examples so that it works on all of them at the same time.

### 01:05:22 · Speaker 1

Meaning your yi is close to f theta of xi for all the xis and yis in that batch of n examples.

### 01:05:32 · Speaker 1

Uh doesn't look

### 01:05:34 · Speaker 4

So this means that if if you are able to pass the batch of data you said that the weight updation happened properly it means if you are passing the whole data set at once during a forward pass it will it will adjust the weight even more better way instead of dividing the data into batches. Correct your abs

### 01:05:53 · Speaker 1

you're absolutely right so actually having a larger batch size means it reduces the variance of the error so that is there is some math involved in that and I'm hoping Protosh will cover that in class so basically what you're saying is right if you if you have a if you have some data set of

### 01:06:18 · Speaker 1

in examples and you pass all of them in the forward pass and then update your weight it will typically lead to better learning and faster convergence of your neural network yeah so you're right yes if you use more examples the weights will be updated better

### 01:06:37 · Speaker 1

Yeah uh any more questions

### 01:06:40 · Speaker 3

So uh there is a quiz being mentioned on Saturday do you know anything about it what we should prepare or something relevant to that

### 01:06:49 · Speaker 1

Typically it will be whatever syllabus that has been covered till the till the class before the quiz

### 01:06:57 · Speaker 1

But I'm not sure if he has mentioned any specific portions

### 01:07:03 · Speaker 1

If you want I can I can ask Pratosh and let you know again. I'll let you know on the group. Okay.

### 01:07:08 · Speaker 3

So thank you

### 01:07:10 · Speaker 1

So the quiz is at 9 a.m. on Saturday

### 01:07:10 · Speaker 3

So

### 01:07:16 · Speaker 3

And can you uh upload your notes onto the teams what you are writing today?

### 01:07:20 · Speaker 1

Sure sure yeah I will up I'll upload it yeah

### 01:07:24 · Speaker 1

Well I'll post it on the group as a PDF

### 01:07:33 · Speaker 1

Okay, I think we can stop for today. So yeah, all the best for the quiz on Saturday.

### 01:07:41 · Speaker 3

Thank you so much

### 01:07:43 · Speaker 3

Thank you
