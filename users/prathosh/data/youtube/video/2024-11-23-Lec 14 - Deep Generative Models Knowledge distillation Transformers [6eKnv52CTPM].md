---
id: 6eKnv52CTPM
title: Lec 14 - Deep Generative Models Knowledge distillation Transformers
url: https://www.youtube.com/watch?v=6eKnv52CTPM
date: '2024-11-23'
duration: 02:23:22
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# Lec 14 - Deep Generative Models Knowledge distillation Transformers

## Transcript

### 00:00:03 · Speaker 1

Not yet

### 00:00:05 · Speaker 2

So yeah, so we will see that and we'll let us I'll tell you how people evolve to transformers and talk about transformers as well and then we can close. Okay. We have distillation also we plan on distillation.

### 00:00:19 · Speaker 1

No legislation is pending

### 00:00:21 · Speaker 2

the dissipation is printing okay so let's uh okay let's start with dissipation and then move to sequence models okay

### 00:00:30 · Speaker 2

It's very handy

### 00:00:55 · Speaker 2

Okay so this was an idea that was proposed by Hinton and his group in the early late 2000s I think it's a

### 00:01:09 · Speaker 2

The objective here

### 00:01:16 · Speaker 2

It's not the primary objective but still the context in which distillation is used today the objective is to reduce

### 00:01:30 · Speaker 2

Reduce the size of

### 00:01:36 · Speaker 1

Something

### 00:01:37 · Speaker 2

Are you laughing something

### 00:01:39 · Speaker 2

Want to see my screen

### 00:01:41 · Speaker 1

Not yet sir

### 00:01:43 · Speaker 2

I don't know

### 00:01:48 · Speaker 2

It is saying that it is showing the screen okay let me do it again

### 00:01:54 · Speaker 1

At least I am not able to see

### 00:01:56 · Speaker 3

No no it is not shared

### 00:02:20 · Speaker 2

Still not seen?

### 00:02:27 · Speaker 2

Uh we'll come rejoin from here

### 00:03:09 · Speaker 2

Let me know when you see the screen we can see now so

### 00:03:15 · Speaker 2

Okay, so the objective here is to reduce the size of very large neural networks without compromising the performance.

### 00:03:42 · Speaker 2

This is the objective. The idea is pretty simple when it was proposed.

### 00:03:49 · Speaker 2

It was proposed without further understanding of what was actually happening. I tell you what it is. So in knowledge situation what happens is you have a very large neural network that has to be compressed.

### 00:04:04 · Speaker 2

largest neural network to be compressed

### 00:04:13 · Speaker 2

This usually called the teacher network

### 00:04:22 · Speaker 2

Then the you have another neural network

### 00:04:32 · Speaker 2

D desirable size

### 00:04:41 · Speaker 2

It is called the student network

### 00:04:49 · Speaker 1

Sir I have a question

### 00:04:52 · Speaker 2

Uh let's let me complete this and then yeah tell me what is it

### 00:04:57 · Speaker 1

Sir, this is related to like a bit related to the assignment. So like in the animal data set, we have around 5,500 images. We divided among 90 classes, right? And even when we were going for the classification tasks, we saw that the training accuracy was very high, but the testing accuracy is always very low. So what my perception was, since the data

### 00:05:27 · Speaker 1

the data size is very small like we have good number of classes but not sufficient images per classes that is the reason that the model is able to learn the features from like you know remember the features and not able to classify properly on a newer set of images is that the correct interpretation

### 00:05:55 · Speaker 2

Yeah why what is the relevance of that question to what we are doing now I think it would have been asked at the end of the class right anyway so now that you have asked

### 00:06:02 · Speaker 1

Anyway so now that you have asked

### 00:06:05 · Speaker 1

So the

### 00:06:05 · Speaker 2

So the reason why you're asking? We were looking at distillation. I think after this, after I finished this part, you could have asked anyway. Yeah, that can be one of the reasons. So what happens is when your data has multiple short modes, so you can think of each of the classes as one data mode. And typically when the data set has too many modes, okay, with very less samples amongst each of the mode, then getting a

### 00:06:35 · Speaker 2

A discriminator or classifier that would put decision boundaries across those classes would be difficult

### 00:06:44 · Speaker 2

Yeah so in that way your interpretation is correct

### 00:06:48 · Speaker 1

Okay

### 00:06:52 · Speaker 2

we continue with what we were doing so if you have any questions on assignments etc please note that down and ask at the like at the end of the class okay so that it does not break the flow of what is being done of course you can ask questions regarding what is being taught okay

### 00:07:11 · Speaker 2

Anyway, wave was I, yeah, so this relation, two neural networks, one large neural network that needs to be compressed, that is called, that is typically called the teacher network. And there is another neural network with the desirable size, which is called the student network, okay.

### 00:07:34 · Speaker 2

No um

### 00:07:36 · Speaker 2

To teacher network

### 00:07:45 · Speaker 2

is trained

### 00:07:53 · Speaker 2

supervised objective whatever suppose you are solving the classification problem it is solved with

### 00:07:59 · Speaker 2

object with the cross entropy loss and whatever the supervision might be

### 00:08:13 · Speaker 2

supervisor objective independently of the student

### 00:08:39 · Speaker 2

What happens is is a network here

### 00:08:51 · Speaker 2

Whatever the task might be okay let us call this the teacher ritual

### 00:09:02 · Speaker 2

So some data some task and it is trained with minimizing let's call the parameters theta just

### 00:09:12 · Speaker 2

usual

### 00:09:15 · Speaker 2

minimizing the expected loss function okay which is uh

### 00:09:22 · Speaker 2

between uh

### 00:09:25 · Speaker 2

let's call this uh f theta maybe f theta of x comma y

### 00:09:34 · Speaker 2

Yeah, so this is the usual empirical risk minimization, okay, or supervised training. Now there is a smaller neural network, which is called the student network.

### 00:09:51 · Speaker 2

CM bas of externally

### 00:10:02 · Speaker 2

speed okay now this has two objectives for training

### 00:10:10 · Speaker 2

One is a

### 00:10:12 · Speaker 2

KL objective between

### 00:10:22 · Speaker 2

Let's call this CT and this as CS

### 00:10:36 · Speaker 2

objective between the distribution of ZT and the distribution of CS plus

### 00:10:46 · Speaker 2

A super wise loss

### 00:11:16 · Speaker 2

phi plus

### 00:11:26 · Speaker 2

Supervise last between

### 00:11:29 · Speaker 2

Something like

### 00:11:32 · Speaker 2

Okay, so what is happening here is that

### 00:11:37 · Speaker 2

student network is being trained okay now the uh scale divergence between

### 00:11:49 · Speaker 2

The distributions of some

### 00:11:54 · Speaker 2

features in some uh some layers typically the pre softmax layer of the student and the teacher network is minimized okay and there is a supervised loss that is uh minimizing the uh loss between the

### 00:12:12 · Speaker 2

Real true predictions and predictions of the neural network. Okay, so now what is this doing is this

### 00:12:20 · Speaker 2

going to match

### 00:12:24 · Speaker 2

the features

### 00:12:30 · Speaker 2

learn or match actually learn or match the features of teacher

### 00:12:40 · Speaker 2

To the tough students, students, that is what it is doing.

### 00:12:50 · Speaker 2

Right by ensuring that the KL divergence between the distributions of representations between the

### 00:13:17 · Speaker 2

about it so by making by ensuring that the the clear divergence between the features of the teacher and the students are are matching your i mean the idea is to ensure that the um

### 00:13:35 · Speaker 2

features that the teacher has learned is imbibed by the student you know if it does that then whatever the performance that the teacher is supposed to give with a larger network can be achieved or can be expected to be achieved using the student network okay so procedure wise this is what is done so in practice

### 00:14:03 · Speaker 2

the KL divergence term no between the teacher features and student features

### 00:14:12 · Speaker 2

is approximated

### 00:14:18 · Speaker 2

Oh yeah

### 00:14:21 · Speaker 2

So mean squared error loss so squared error loss average it is actually mean squared error loss

### 00:14:33 · Speaker 2

between

### 00:14:36 · Speaker 2

Uh GD and GS

### 00:14:40 · Speaker 2

Yeah, this is also not a bad approximation, right? When we assume these two distributions, PT and PG, actually what this actually means that

### 00:14:51 · Speaker 2

have pt coming from a Gaussian okay and ps is also coming from a Gaussian if you make this assumption then we know that the scale divergence is equivalent to minimizing the mean squared error between the features taken when averaged over all possible

### 00:15:14 · Speaker 2

samples okay

### 00:15:17 · Speaker 2

Okay so

### 00:15:25 · Speaker 2

This is what this is how the finally what is done is instead of using the teacher network, teacher network is discarded, meaning it is, I mean, it is, it is the goal is to not use the teacher network, but to use the student network for further process. So that is the idea.

### 00:15:43 · Speaker 2

Okay, so I will tell you, so there is, this was what was being done in distillation. Now, a very recent paper came that gave a very nice statistical perspective of why should this work, okay? What is actually happening under the hood? I'll talk about that. Before that, if there are any questions on the procedure of what distillation is, do ask. And by the way, in your assignment, what I've asked is, I've asked you to use a large,

### 00:16:13 · Speaker 2

teacher network and

### 00:16:16 · Speaker 2

distill it out to a smaller student and compare it with just training a student network separately i mean meaning a network that is of the size of the student network separately and then compare the performance

### 00:16:29 · Speaker 2

okay questions now uh yeah we wake

### 00:16:32 · Speaker 4

So two small questions. So should the sizes of the features of the Z and the I mean the both the ZT and ZS should they both be the same?

### 00:16:48 · Speaker 2

By sizes you mean the dimensionality

### 00:16:50 · Speaker 4

Dimensions yes

### 00:16:52 · Speaker 2

Yeah they they have to be same otherwise how would you define KL divergence

### 00:16:55 · Speaker 4

Okay, so the second question is how important is the KL divergence term in this so if we skip that and if we simply use a completely different network so is that still called distillation

### 00:17:09 · Speaker 2

What do you mean by that? See, if you do not use any features from the teacher while training the student network, then there is no distillation, right? It is simply an independent training.

### 00:17:24 · Speaker 4

Right okay

### 00:17:25 · Speaker 2

Isn't it?

### 00:17:26 · Speaker 4

Yeah win you

### 00:17:27 · Speaker 2

I mean see it is called estimation only because you have a teacher network and you are using those features too

### 00:17:34 · Speaker 2

But you're actually imposing those features on the features of the student that's all right

### 00:17:40 · Speaker 4

Right yes so

### 00:17:41 · Speaker 2

It's like whatever teacher network has learned the transformation that the teacher teacher network has learned are trying to ensure that the features of the student network matches those features at a distributional level

### 00:17:54 · Speaker 4

Yeah, but if the student network is struggling too hard to simply match with the teacher network more than increasing the accuracy of the classification task, then should we reduce the weightage on the KL division task?

### 00:18:08 · Speaker 2

Of course of course of course I mean that's that's always there right I mean when you have for two loss terms you can you always rate them accordingly

### 00:18:17 · Speaker 4

Yeah so that's all thank you

### 00:18:22 · Speaker 2

Okay uh yeah salvage

### 00:18:26 · Speaker 3

So if Z are just the pre softmax terms, so why to include this expected loss in student network? Because anyways, they will be same, right? If they are same then

### 00:18:38 · Speaker 2

Good question. See what happens, this is a practical thing. What happens is when you do not have the supervised loss, because I mean teacher network may itself have not learned to solve the task properly, right? The performance of the student network will not be great if you don't include that.

### 00:19:04 · Speaker 3

So just to be sure that it is learning the main correct

### 00:19:08 · Speaker 2

Correct whatever is needed no The main uh

### 00:19:12 · Speaker 2

Learning should happen that is why the supervised loss is also included

### 00:19:18 · Speaker 3

Thank

### 00:19:20 · Speaker 2

Unkitted

### 00:19:22 · Speaker 1

Sir, if the teacher network is like as we are asking it is very large and let's say the data size is not sufficient enough for the learning to happen correctly and at the same time then we are trying to use that loss for training the student network.

### 00:19:42 · Speaker 1

uh how can we expect the student network to be learned properly

### 00:19:48 · Speaker 2

Yeah you're saying if the teacher network is bad how do how what does what happens to distillation

### 00:19:55 · Speaker 1

No, no, like my, like I asked a previous question, right? If the, uh, the data set is not sufficiently large. So we cannot expect the teacher network itself to learn the, uh, the classification properly. And then we are trying to train the student network.

### 00:20:16 · Speaker 2

That is what no what happens if the teacher network itself is not good

### 00:20:21 · Speaker 2

That is what you are asking. Yeah. Yes. Yeah. So, yeah. So what happens is if there is like some level of uncertainty in the teacher network is OK, right? As we will see in the theory, but if teacher network is not even doing like

### 00:20:41 · Speaker 2

supervised learning right then obviously the student network will perform badly

### 00:20:48 · Speaker 2

So we have to ensure that the teacher network has to have some level of good accuracy for this to work.

### 00:21:02 · Speaker 2

Anything else?

### 00:21:20 · Speaker 2

Shall we continue

### 00:21:26 · Speaker 4

Yeah just one small query what is the benefit is it going to use less resources

### 00:21:32 · Speaker 2

Training definitely not.

### 00:21:36 · Speaker 2

But the inference, of course, right, because the student network is by design smaller in terms of sizes, it is going to use less number of, less resources during inference. Because finally, what you end up storing is the student network, not the teacher network.

### 00:21:59 · Speaker 1

Sir one more question the training has to happen simultaneously

### 00:22:06 · Speaker 1

First we have to train the teacher network and then the student network

### 00:22:11 · Speaker 2

So that's a design choice typically what is done is uh uh

### 00:22:17 · Speaker 2

Feature network is trained up to some level okay where you have decent accuracy and then uh both of them were trained simultaneously

### 00:22:28 · Speaker 2

But you can completely train the teacher network once and then reuse it and then do a distillation that is also possible.

### 00:22:38 · Speaker 2

I tried design choice

### 00:22:41 · Speaker 2

Okay, so yeah, so this is what is done procedurally. Now, as I said, no, there is a very nice interpretation so as to why this works. Let's try to look at that.

### 00:23:12 · Speaker 2

Statistical perspective on knowledge distillation

### 00:23:19 · Speaker 2

Okay so what happens is um

### 00:23:23 · Speaker 2

In typical

### 00:23:28 · Speaker 2

Supervised learning

### 00:23:37 · Speaker 2

Mm

### 00:23:39 · Speaker 2

labels

### 00:23:44 · Speaker 2

are deterministic

### 00:23:52 · Speaker 2

in the sense that

### 00:23:54 · Speaker 2

Every data point so okay let us design the problem that way

### 00:24:01 · Speaker 2

Opposed

### 00:24:03 · Speaker 2

the class labels right they belong to uh

### 00:24:10 · Speaker 2

one out of K categories

### 00:24:15 · Speaker 2

in a in a k class classification problem then typically

### 00:24:23 · Speaker 2

for each x

### 00:24:28 · Speaker 2

for each x okay y

### 00:24:37 · Speaker 2

Why is only

### 00:24:41 · Speaker 2

One of the

### 00:24:44 · Speaker 2

You can use one label

### 00:24:50 · Speaker 2

This is what happens

### 00:24:53 · Speaker 2

However

### 00:25:00 · Speaker 2

It is always uncertainty in labeling

### 00:25:19 · Speaker 2

eternity enabling

### 00:25:23 · Speaker 2

So between place

### 00:25:26 · Speaker 2

for each x

### 00:25:31 · Speaker 2

there exists

### 00:25:36 · Speaker 2

There exists a distribution over y

### 00:25:45 · Speaker 2

p of y given x

### 00:25:48 · Speaker 2

What I'm trying to say is let's say that there is uh you have you have an image that you want to label

### 00:25:57 · Speaker 2

Now okay so I'll take an example that is sort of ambiguous

### 00:26:10 · Speaker 2

Okay I'll try to check it

### 00:26:13 · Speaker 2

I like this

### 00:26:15 · Speaker 2

Okay which digit do you think it is I mean let's say that I'm

### 00:26:21 · Speaker 2

annotating MNIST

### 00:26:28 · Speaker 2

Yeah that's right

### 00:26:34 · Speaker 2

So people write it this way now so this means that this has uh

### 00:26:40 · Speaker 2

likelihood of being in three and some likelihood of being in five

### 00:26:51 · Speaker 2

So now there exists, so what is this? Along y-axis what I have written is, this is p of y given x.

### 00:27:05 · Speaker 2

Okay now what is done in typical supervised learning is okay in

### 00:27:14 · Speaker 2

Supervised learning

### 00:27:22 · Speaker 2

of y given x

### 00:27:25 · Speaker 2

Approximated

### 00:27:37 · Speaker 2

With a delta function

### 00:27:43 · Speaker 2

Isn't it so the uncertainty that is associated with the labeling is completely ignored when I mean in typical supervised learning right now what this this this nice paper does is the following

### 00:28:01 · Speaker 2

They consider, okay, so any questions so far? What I'm trying to say is there are, there is an uncertainty that exists with the labeling inherently because every data point can

### 00:28:18 · Speaker 2

can probabilistically belong into one of k possible classes. But labeling is always done in such a way that the uncertainty that that is there in the labeling is ignored and labels are marked labels are given in a deterministic way. Is this clear?

### 00:28:39 · Speaker 4

Yes sir

### 00:28:40 · Speaker 2

Okay, now what is the consequence of it is the following define

### 00:28:49 · Speaker 2

Two types of risks or losses

### 00:28:56 · Speaker 2

One is the typical supervised loss

### 00:29:08 · Speaker 2

Supervise loss

### 00:29:12 · Speaker 2

Deterministic labeling

### 00:29:17 · Speaker 2

Call it R

### 00:29:20 · Speaker 2

And there is uh okay let's call it R cap and there is something called base distill loss okay

### 00:29:34 · Speaker 2

dystrophic loss call it RV cap

### 00:29:38 · Speaker 2

Now this is what can actually be shown is that this is we know what R cap is right this is simply the expectation of the loss F is the classifier that we are looking at this is F theta of X comma Y this is what it is this is with respect to PXY and this can be shown as KL divergence

### 00:30:05 · Speaker 2

between the

### 00:30:09 · Speaker 2

Distribution of uh

### 00:30:13 · Speaker 2

F theta

### 00:30:16 · Speaker 2

effects

### 00:30:20 · Speaker 2

of y given x let's say is a classifier imposes a distribution on labels right that is what it does and the

### 00:30:30 · Speaker 2

true label distribution that is what you can show okay uh i mean if you use a cross entropy kind of loss then the scale divergence is equivalent to that cross entropy i mean that is easy to show okay

### 00:30:45 · Speaker 2

The interesting result that which is shown us. Now, suppose.

### 00:30:53 · Speaker 2

R star represents the generalization risk

### 00:31:03 · Speaker 2

It's also called the true risk

### 00:31:11 · Speaker 2

It is nothing but the error, average error on unseen data.

### 00:31:24 · Speaker 2

on unseen data

### 00:31:31 · Speaker 2

What can be shown is that r star

### 00:31:36 · Speaker 2

will be lower

### 00:31:42 · Speaker 2

RB cap okay compared to

### 00:31:48 · Speaker 2

So this is a this is actually the main result

### 00:31:54 · Speaker 2

which is there in that paper which uses Jensen's inequality okay to bound the variance of these two risks

### 00:32:02 · Speaker 2

Yeah, but this is the crux of the result that would say that the generalization error that we get

### 00:32:11 · Speaker 2

generalization error that is achieved using base distill risk is lesser compared to that of the risk that is obtained using the direct delta approximation.

### 00:32:26 · Speaker 2

Okay which means so what does this imply a summary is

### 00:32:38 · Speaker 2

It is better

### 00:32:44 · Speaker 2

It was

### 00:32:48 · Speaker 2

base distill risk or the distribution the actual distribution over the labels given data okay instead of

### 00:33:03 · Speaker 2

instead of

### 00:33:05 · Speaker 2

Delta approximated labels

### 00:33:17 · Speaker 2

So this is the idea. Okay. So now, uh, this paper says that now see if you incorporate the, I mean, that is why this thing P of Y given X is also called dark knowledge. That is the term that is used in the distillation literature. Okay. If you incorporate the dark knowledge that is there, uh, in the labeling or uncertainty that is there in the labeling, you achieve a better generalization performance is the idea. Now, uh, this is not directly related to connected

### 00:33:47 · Speaker 2

To distillation yet. Okay. Now this, now the question is.

### 00:33:54 · Speaker 2

Given a labeling a deterministic labeling scheme

### 00:34:10 · Speaker 2

a scheme there is no access

### 00:34:17 · Speaker 2

access to p of y given x, isn't it? I mean, we are only given deterministic labels. How do we know what is the distribution of the labels conditioned on data? We don't know that. Therefore, the idea is

### 00:34:36 · Speaker 2

Yeah

### 00:34:38 · Speaker 2

The idea is to

### 00:34:43 · Speaker 2

Approximate

### 00:34:47 · Speaker 2

We have ionics okay as

### 00:34:54 · Speaker 2

using using a neural network

### 00:34:58 · Speaker 2

So this neural network is the teacher neural network

### 00:35:01 · Speaker 2

Right. So now what happens is, in fact, this theory, right, it does not talk about the size reduction at all. So it suggests what is called as self-distillation. I'll talk about it. So there is this network F theta, where you get X and Y. It is trained in a supervised way with deterministic label. Okay.

### 00:35:23 · Speaker 2

What do you think

### 00:35:28 · Speaker 2

deterministic labels. However, the free softmax activations that you get, the logits that you get, these

### 00:35:41 · Speaker 2

can be interpreted

### 00:35:47 · Speaker 2

as

### 00:35:50 · Speaker 2

An approximation

### 00:35:55 · Speaker 2

P of y given x. So this is an approximation to P of y given x. So then what you do is you take the you take another network

### 00:36:06 · Speaker 2

We don't talk about sizes here, right? I mean, it can be the same size or different size. If it's of the same size, then it is typically called the self desolation, okay?

### 00:36:20 · Speaker 2

take that and use RB star here to try this. So RB is the base distance discussed simply the scale divergence between the true or rather the

### 00:36:36 · Speaker 2

models

### 00:36:40 · Speaker 2

estimate of y given x okay and the true y given x so now we don't have access to true y given x so you we use the features f theta's logits as an approximation to this now when somebody asks the question right we can why why do we have a supervised loss so if we

### 00:37:01 · Speaker 2

If we have a perfect uh uh

### 00:37:06 · Speaker 2

estimation of P of Y given X, then we do not need supervised loss. Now, since we are approximating the true uncertainty using another neural network that is trained using deterministic labels, so it can only do so much, right? So that is why you also have a supervised loss here, okay? To ensure that the network, the distilled network also does well on the supervised training.

### 00:37:34 · Speaker 2

As I said, no, in this treatment, there is no reference to making this SP a smaller network. Now that becomes a byproduct, right? Or a happy consequence of this that, okay, there's no restriction on how big or large this SP network should be. Because as long as you are matching the true labor uncertainty, you should get better risk irrespective of the network size. And that is why people tried, okay, let's try to

### 00:38:04 · Speaker 2

to make this SP a smaller network and then

### 00:38:08 · Speaker 2

uh try to ensure so this is there is a scale here and try to use this technique for network compression in fact as uh as it stands you can do what is called as self-distillation which is that you try the neural network using supervised fashion and then take that same neural network and use the logits of the previous one and retrain it by minimizing the kL between the logits and the supervised loss

### 00:38:37 · Speaker 2

If you have gotten P of Y given X to a fair extent from the teacher network, then doing self-distillation should improve the generalization according to this theory.

### 00:38:49 · Speaker 2

Okay that's about it uh questions yeah Vivek

### 00:38:53 · Speaker 4

So the so we uh you told about the base uh distill distill laws uh but instead of using that so if we just use the entropy of the uh pre decision layer output I mean if we uh try to

### 00:39:13 · Speaker 4

Minimize the entropy will that lead to any benefit

### 00:39:18 · Speaker 2

It's that same as this isn't it

### 00:39:23 · Speaker 4

That's what it should be less indecisive uh that in that that way the entropy will uh reduce

### 00:39:32 · Speaker 4

I yeah so okay

### 00:39:36 · Speaker 2

very uh in fact it's not the absolute entropy it becomes i mean what we are suggesting is to minimize the cross entropy here

### 00:39:43 · Speaker 4

Cross entropy okay between the teacher and the student

### 00:39:46 · Speaker 2

Correct correct

### 00:39:49 · Speaker 2

I mean, it's actually not the teacher. It should be the true distribution, the post true posterior of labels given data. That is what it should be. Now, because we don't have access to that given hard labels, we will try another neural network and use its logits as an approximate for that. That is the idea.

### 00:40:08 · Speaker 4

Okay

### 00:40:14 · Speaker 2

Any other question

### 00:40:24 · Speaker 1

If the student network or the size of the student network is not so small it's almost same same to the teacher network then what is the benefit of doing this because we can directly do the

### 00:40:36 · Speaker 2

I told you no it is improve improve improve generalization you know it will do much better on test data unseen data

### 00:40:44 · Speaker 2

Because now you are not training this neural network just using hard labels but you are trying to get using I mean you are incorporating the uncertainty also that is there in the labeling.

### 00:40:56 · Speaker 2

Got it

### 00:40:59 · Speaker 2

And do it

### 00:41:01 · Speaker 1

Sir, for the supervised loss, we will be taking up the true labels y and the approximated labels from the S-S phi network, right?

### 00:41:17 · Speaker 2

Of course yeah

### 00:41:21 · Speaker 2

You're saying why why you are doing supervised training for the student network you're saying yeah

### 00:41:26 · Speaker 1

No no no I'm um

### 00:41:29 · Speaker 1

I'm trying to understand like

### 00:41:32 · Speaker 1

what are we comparing are we comparing it from the uh labels generated from f theta network or from the sv network

### 00:41:42 · Speaker 2

labels here the supervised losses losses with these true labels the output of the SVE network and the true labels that's what the losses between

### 00:41:59 · Speaker 1

And this F theta network, so this can be any network, right? It need not be trained, just that we need a representation for well if it

### 00:42:09 · Speaker 2

Well if it's not if it's not trained then how do you expect it to give uh the actual P of I units?

### 00:42:19 · Speaker 2

Should be trained should be trained in a supervised way yeah

### 00:42:24 · Speaker 2

Okay, so that's about it. And yeah, this is how you implement it in your assignment, right? I have not asked you to do self-distillation. I have asked you to reduce the network size and do a distillation on reduced network size itself. So yeah, please do that. And also read this paper, okay? This is called a statistical perspective on knowledge distillation. I will tell you the authors also, stress a grain.

### 00:42:52 · Speaker 2

Uh

### 00:43:06 · Speaker 2

Or this destination

### 00:43:19 · Speaker 2

to

### 00:43:25 · Speaker 2

Share the link no let me do it

### 00:44:21 · Speaker 2

You see my screen

### 00:44:33 · Speaker 2

see my screen right so this is that paper so here what they do is the following right yeah so they call this as what this pt of x is what they call as what they called as the teacher class probability estimates or the

### 00:44:52 · Speaker 2

label posterior okay so where pt of y given x estimates how likely x is to be classified as y

### 00:45:00 · Speaker 2

Now these are used by a student model which replaces empirical risk, which is the standard empirical risk with the distill risk. This is what they call R tilde is what they call as the distill risk. Then the question is why does distillation help? So they compute this thing called base distill risk and this is the main result which I just said that if you take any bounded loss then the generalization error that we get with the base distill risk is much less.

### 00:45:30 · Speaker 2

compared to the tough non-distilled risks that is the result okay so I suggest that you read this paper it's a nice paper and this the proof that they use to show that is also not very difficult it is simply using the definitions of variance and using the Jensen's inequality that's all it is have a look please

### 00:45:51 · Speaker 2

Okay uh

### 00:45:54 · Speaker 2

about distillation do you need a five minutes break ten minutes break before we go to sequence modeling

### 00:46:06 · Speaker 2

Hello am I audible

### 00:46:09 · Speaker 1

Yes it is

### 00:46:11 · Speaker 2

Shall we shall we get back after the break

### 00:46:15 · Speaker 2

So

### 00:46:18 · Speaker 2

Okay, so let's come back at 11 a.m. Maybe just take some 15 minutes break.

### 00:46:23 · Speaker 2

Okay yeah see you in the way

### 01:05:10 · Speaker 2

Will we continue

### 01:05:18 · Speaker 2

Let me just share my screen

### 01:05:26 · Speaker 2

Yeah we wait you have a question

### 01:05:29 · Speaker 4

Yes sir so I was just seeing the paper so what is temperature scaling

### 01:05:34 · Speaker 2

Oh yeah, yeah. So that is like, I think it was you or somebody else who talked about the weighting of those two losses, no?

### 01:05:43 · Speaker 4

Okay yes

### 01:05:44 · Speaker 2

uh the supervised and the uh clear losses

### 01:05:48 · Speaker 2

That is what is referred to as temperature scale how much weight do you have to give for each of them

### 01:05:52 · Speaker 4

Okay

### 01:05:56 · Speaker 4

Okay sir said uh okay so what is a well calibrated models so what can we do to what how should the temperature be scaled

### 01:06:05 · Speaker 2

That's a hyperbolic effect

### 01:06:08 · Speaker 4

Okay so should we should we learn that hyperparameter or should we

### 01:06:12 · Speaker 2

Yeah, see, just like with any other loss function, right, I mean, where you have two or more components and you need to decide the weight, either you can do it using hyperparameter tuning or you can learn it. In fact, I have a paper sometime back, one year, two years back, where we cast it as a meta-learning problem and learn both the weights, loss weights, and the losses together. All that is again,

### 01:06:42 · Speaker 2

level up but yeah so typically it is trained as a hyperparameter either you learn it or keep it I mean fix it based on validation data

### 01:06:55 · Speaker 4

So can we can we have can we have a link to the paper

### 01:06:58 · Speaker 2

I mean actually shared it no I actually shared it

### 01:06:58 · Speaker 4

I mean

### 01:07:02 · Speaker 4

Okay it's the same paper okay

### 01:07:02 · Speaker 2

He's the same

### 01:07:04 · Speaker 2

So you mean my paper you're saying huh

### 01:07:05 · Speaker 4

Yeah yeah yeah

### 01:07:08 · Speaker 2

Hold on

### 01:07:21 · Speaker 2

ALMKD

### 01:07:40 · Speaker 2

the paper or the link

### 01:08:05 · Speaker 4

Maybe you can share the name and the title

### 01:08:08 · Speaker 2

Your title is there but I myself should find my paper now where is it

### 01:08:14 · Speaker 2

It's published in AAA but where is the link for that

### 01:08:22 · Speaker 2

I think so

### 01:08:48 · Speaker 2

Surprising that I can't spot the link

### 01:08:56 · Speaker 2

I found it I got it

### 01:09:08 · Speaker 2

I just put it in the chat window. So what we do is that wherever you have these kinds of settings, right, where you have like two losses and you need to, in fact, one of the applications is knowledge distillation. If you look at section four of the paper.

### 01:09:26 · Speaker 2

We actually learn that temperature

### 01:09:30 · Speaker 4

Okay okay okay knowledge distillation yeah so two applications okay

### 01:09:35 · Speaker 2

If you look at equation nine ten and all that we actually learn that and show that uh like that it's just an optimal value we do it using uh

### 01:09:45 · Speaker 2

this thing uh

### 01:09:48 · Speaker 2

Metal only, yeah, it is what the report is about. But generally that is not done, you know, it is taken as a hyperparameter and used to validate fixed based on validation data.

### 01:09:59 · Speaker 4

Okay okay just through some sample values and uh what is giving the right data okay

### 01:10:09 · Speaker 4

Okay

### 01:10:14 · Speaker 2

Let's move on. The final piece that we will talk about is the

### 01:10:21 · Speaker 2

Quince modelling

### 01:10:37 · Speaker 2

Beta in this case

### 01:10:40 · Speaker 2

Well

### 01:10:44 · Speaker 2

Every data point okay is

### 01:10:48 · Speaker 2

It's a sequence

### 01:10:59 · Speaker 2

Okay data point in a sequence. So what do you what do you mean by a sequence? Let's say that x is one data point. So one data point itself will have

### 01:11:12 · Speaker 2

Uh superscript perhaps huh

### 01:11:20 · Speaker 2

2 x t okay

### 01:11:25 · Speaker 2

every xj is in some d-dimensional space. This is what is called as a sequence where every data point has a

### 01:11:37 · Speaker 2

is a is a is a series of d dimensional vectors t of them okay so examples of this you know that this is you have

### 01:11:49 · Speaker 2

Second place

### 01:11:53 · Speaker 2

Right is a sequence of

### 01:12:03 · Speaker 2

Linguistic tokens these tokens can be characters or words or something right so the other example is the speech signal

### 01:12:15 · Speaker 2

This is a sequence of uh

### 01:12:25 · Speaker 2

Frequency domain vectors

### 01:12:31 · Speaker 2

Called the MFCC and so on. Okay, so this is one thing, and you have

### 01:12:38 · Speaker 2

some industrial time series and you can also look at video as

### 01:12:45 · Speaker 2

sequence of

### 01:12:52 · Speaker 2

Sequence of images

### 01:12:56 · Speaker 2

or frames

### 01:12:59 · Speaker 2

Okay, so this is a sequence, I mean, this is what is called as sequence data. Now, sequence modeling is a set of all those methods where the objective in sequence modeling, the objective is to solve

### 01:13:24 · Speaker 2

The objective

### 01:13:28 · Speaker 2

to solve either

### 01:13:34 · Speaker 2

discriminative or generative preminative

### 01:13:43 · Speaker 2

generative problems on sequences

### 01:13:54 · Speaker 2

on sequences

### 01:13:59 · Speaker 2

Okay, so now there you have examples of these problems. So examples can be, of course, we have machine translation.

### 01:14:14 · Speaker 2

where you have a sequence in right or a sequence in one language

### 01:14:20 · Speaker 2

sequence in English and what comes out is a sequence in in in Hindi let's say right so this is one example the other example can be

### 01:14:37 · Speaker 2

Ex summarization

### 01:14:44 · Speaker 2

Right you have video classification

### 01:14:52 · Speaker 2

spam detection and so on right i mean you can think of any number of problems that uh uh we have uh uh that that you can encounter

### 01:15:07 · Speaker 2

between sequences. Okay, so now how do you deal with this kind of sequential data is a question that people have been asking for a long time now.

### 01:15:19 · Speaker 2

Now I'll just give you a broad history of how things were happening and then then we'll move on to what the current state of the art is.

### 01:15:35 · Speaker 2

History of

### 01:15:39 · Speaker 2

sequence models

### 01:15:49 · Speaker 2

Very early days, right, people were using models such as autoregressive models or AR models.

### 01:16:03 · Speaker 2

where the idea was the following so you have to model xt right so xt was modeled as simply a linear combination of

### 01:16:25 · Speaker 2

to or rather let's say t minus k to

### 01:16:31 · Speaker 2

Okay, so this is an autoregressive model where you take, you model or rather you express the tth sample. Okay, so we used a superscript for t, you know, the tth vector that we have is given as a linear combination of

### 01:16:52 · Speaker 2

see i don't want to confuse you by using superscript and subscript okay let us use uh

### 01:17:00 · Speaker 2

Script only

### 01:17:07 · Speaker 2

Don't confuse it with like one two three up to t data points okay in one data point itself you have t uh

### 01:17:16 · Speaker 2

Length sequence, it is okay that is what the convention is, XT is equal to.

### 01:17:25 · Speaker 2

Okay so now what we are doing is every

### 01:17:31 · Speaker 2

Yet

### 01:17:35 · Speaker 2

token

### 01:17:38 · Speaker 2

in the data

### 01:17:43 · Speaker 2

is a linear combination of

### 01:17:52 · Speaker 2

Kelvin

### 01:17:55 · Speaker 2

window

### 01:18:04 · Speaker 2

before it. This is an autoregressive model. You can imagine why the name, it is regressing on self. That is why it is autoregressive. So it is not using anything else. It is only saying that I will express, rather the tth token is expressed as a linear combination of previous t minus k tokens. It is also called linear prediction model.

### 01:18:33 · Speaker 2

Linear predictive coding

### 01:18:37 · Speaker 2

LPC in fact even today this is used in telecommunications to compress speech and all that so now the question here is how do you find these coefficients a and it is found out in a statistical way where you have a lot of data and try to reconstruct the data back using the k previous samples and find out these coefficients and use them in fact what is done in speech compression is that you need to transmit

### 01:19:07 · Speaker 2

uh speech data from one point to the other let's say right the raw data is not at all transmitted what is transmitted are these coefficients aj so that uh you can i mean that is a compressed version of it okay and then you use that and uh reconstruct the data back at the decoder that is in fact as i said now as we are speaking a lot of voip protocols and all this even today uses some variant of this linear predictive coding okay

### 01:19:37 · Speaker 2

The thing is these kinds of models work with speech kind of data where there is a lot of predictability but they don't generalize for tasks like machine translation and so on. Okay. People then move to statistical models.

### 01:20:00 · Speaker 2

Such as one example was one famous example was what is called as a hidden Markovian model or HMM.

### 01:20:15 · Speaker 2

It's MM was the the go to model right to model sequences go to choice for modeling sequences for a long time. What is the model here is that you assume that there is a there's a Markov chain

### 01:20:33 · Speaker 2

Amongst what are called as states I'll tell you what states are

### 01:20:48 · Speaker 2

transition from here to here okay okay so and every state emits symbols

### 01:21:01 · Speaker 2

And these symbols are XJs, X1, X2, up to X. I mean, it's simply XJ, okay? So now these are states Z. So it's actually HMM, right? Is a latent variable model. It's a latent variable model.

### 01:21:26 · Speaker 2

where the latent variable is discrete Markovian

### 01:21:40 · Speaker 2

Okay, and the model is the following, right? There is a Markovian transition between the latent variable states and at every transition, right, after every transition, the model emits an observable symbol xt, okay? This is continuous.

### 01:22:02 · Speaker 2

and model using neural net uh uh GMLs

### 01:22:09 · Speaker 2

So the HMM, the famous HMM-GMM model where, see, basically what is happening is the following, right? I mean, imagine the speech signal example. So the motivation behind this is

### 01:22:26 · Speaker 2

this assumption that when somebody is speaking okay what is actually happening is that before you speak you think of what is the phoneme that you have to emit given the uh semantic meaning that you want to convey okay depending upon what uh uh uh phoneme that you need to emit okay uh phoneme you need to convey uh you create some constrictions in your vocal fold and what is uh produced is a pressure difference

### 01:22:56 · Speaker 2

When we speak, what happens is there is a certain pressure difference that occurs in the environment, which is what is recorded using a microphone, a condenser microphone. So this is the observable speech signal. These are the observations.

### 01:23:15 · Speaker 2

which happens to be at the speech signal itself which we measure

### 01:23:20 · Speaker 2

Okay so what is Markovian R the unobservable

### 01:23:28 · Speaker 2

Unobservable abstract

### 01:23:32 · Speaker 2

What names

### 01:23:37 · Speaker 2

So now there is a Markovian transition between them because given that you need to convey something and given that you have already said the particular type of phoneme, you can only choose from a I mean there is a probability from which you can choose what phoneme to be uttered next.

### 01:23:57 · Speaker 2

So, that is why there is a Markovian assumption between the hidden states and what is observed are the measured quantity. Now, this is a model and the distribution. So, now basically what happens is there will be a distribution amongst the states.

### 01:24:20 · Speaker 2

which is Markovian

### 01:24:25 · Speaker 2

And that will be a distribution over the

### 01:24:30 · Speaker 2

observations given uh a particular state this is modeled as a Gaussian mixture model this was the this was actually the standard uh this used to be the standard modeling choice for any sequences where you say that okay so you can extend this for let's say handwriting recognition right where the observations are modeled as uh the pen strokes or the coordinates of the pen strokes and the latent variable or the z models what was the uh the what is the

### 01:25:00 · Speaker 2

Uh

### 01:25:04 · Speaker 2

letters or rather the symbol that is to be conveyed okay

### 01:25:08 · Speaker 2

And if you want to model speech, as I said, there are phonemes and every phoneme emits a symbol, which is a speech signal and so on. Okay, so now what as to what are to be learned? This is parameterized by some theta, this is parameterized by some phi. Theta and phi are learned.

### 01:25:32 · Speaker 2

using the EM algorithm. So we have seen the EM algorithm right in the beginning classes. So EM algorithm is used to learn this. So this is how initially the sequence models were being learned. So if anybody wants to learn more about HMMs right, there is one very nice tutorial by Lawrence Rabiner.

### 01:25:59 · Speaker 2

have a look at it where he formulates the problem and write downs the likelihood log likelihood for an hmm and works out the em so basically it is working out the em okay hmm tutorial

### 01:26:18 · Speaker 2

Any questions so far on this?

### 01:26:34 · Speaker 4

So but in this MARCO model ah are we actually passing the is it dependent on the past I mean

### 01:26:42 · Speaker 2

It is no it is because it is Markovian yeah

### 01:26:56 · Speaker 3

So just to know, I mean, you said when we say a sentence, right, we say one word and the next word is basically we can predict whatever is the next word, kind of, right.

### 01:27:08 · Speaker 2

Not predict there is a probability over what the next word is going to be that is reasonable because if you are con yeah because in a given language given that you have uttered one word there's a certain probability of what the next word is going to be

### 01:27:23 · Speaker 3

So it just depends on the previous word alone right

### 01:27:26 · Speaker 2

I mean it depends on what order of the Markovian assumption that you are making you can make it a first order Markov second order Markov third order Markov anything

### 01:27:36 · Speaker 2

It's called an n-gram model, right? You can make it a unigram, bigram, trigram, anything, right? So it is not one word always. In diffusion models, we assumed it to be a first order Markov process, but it need not be first order. Typically, it is taken to be a third or fourth order Markov process when it comes to the sweet signals.

### 01:27:58 · Speaker 2

Okay, so as I said, right, I mean, HMM is sort of obsolete now. Like, it's not the go-to choice. So then came the revolution of neural networks, right? This was in, this was 19, early 90s and so on. This AR models, right, autoregressive models, they date back to like early 19th, 20th century. And then 1980s and 90s, people started looking at hidden Markovian models and other statistical models, similar statistical models.

### 01:28:28 · Speaker 2

the when neural networks started taking off right so came the recurrent neural networks

### 01:28:47 · Speaker 2

known as oddimans

### 01:28:53 · Speaker 2

I think if there is one more tutorial, right, you can ask Chendran to talk more about RNNs and BPTT. I will just give you an overview. So the idea in recurrent neural networks is that what you have is that you build a

### 01:29:10 · Speaker 2

Okay, so let me before that see what happens in a in a sequence kind of data is every data point

### 01:29:26 · Speaker 2

have

### 01:29:28 · Speaker 2

Different length

### 01:29:37 · Speaker 2

Right because imagine that we are looking at

### 01:29:42 · Speaker 2

If you are looking at natural language sentences, then each of the sentence will have a different length, you know, obviously. So now, if you take a fully connected neural network or an MLP, it is difficult to handle data with different lengths. So now, how do you handle this is the question. So now, the one answer is to use what is called as recurrent neural networks. The idea is the following that

### 01:30:09 · Speaker 2

to handle

### 01:30:13 · Speaker 2

Equal equal uh

### 01:30:17 · Speaker 2

Not equal

### 01:30:20 · Speaker 2

Input lens

### 01:30:25 · Speaker 2

So what you do is share the parameters across time

### 01:30:41 · Speaker 2

What is meant by this but this is the architecture of a bare bone

### 01:30:52 · Speaker 2

Recurrent neural network

### 01:30:57 · Speaker 2

say that you have x p here that is the tth length and you have the corresponding y t because it's a sequence in sequence out model now you have the t minus first hidden state you have the tth hidden state going out okay this is one r and then

### 01:31:18 · Speaker 2

RN block or RN and RN cell

### 01:31:25 · Speaker 2

So you have parameters that are let's say U P and W

### 01:31:35 · Speaker 2

Okay, now the relationship between the parameters are given by this that you have yt is equal to sigma of w times ht minus 1.

### 01:31:53 · Speaker 2

Less

### 01:31:56 · Speaker 2

Uh is there

### 01:32:00 · Speaker 2

xt is coming into u times of v times xt and the next state or next hidden state is given by

### 01:32:20 · Speaker 2

It's right what I'm writing no we times that is this yeah u times x t x yeah yeah

### 01:32:26 · Speaker 3

Oh

### 01:32:27 · Speaker 2

u times xt

### 01:32:34 · Speaker 2

Less

### 01:32:36 · Speaker 2

W times 15 minus 1 yeah

### 01:32:40 · Speaker 2

Yeah, so this is one R and N cell. So now what do you do is that you get

### 01:32:48 · Speaker 2

Have you seen an RNN picture right where people write this kind of a thing?

### 01:32:55 · Speaker 2

Okay, so and then they write something called unrolling of RNN. So what that means is that you repeat this. So now if you have a sequence of let's say length T.

### 01:33:21 · Speaker 2

uh it's it's zero

### 01:33:24 · Speaker 2

There is x1 here, x2 here, and x3 here. And you have h1, h2, and h

### 01:33:36 · Speaker 2

t and y1 to yt observe that everywhere so you have the same u w and v exact same parameters everywhere

### 01:33:50 · Speaker 2

So this is what is called as parameter sharing across time

### 01:34:05 · Speaker 1

So in the equation for yt

### 01:34:08 · Speaker 1

Shouldn't XT be multiplied with U?

### 01:34:13 · Speaker 2

x t b multiplied with u see the the way i have written is uh that you take x t here multiplied with v and then get y t and you take x t but i can write u here perhaps this is better no write it this way

### 01:34:35 · Speaker 2

I think this is better

### 01:34:39 · Speaker 2

What I meant

### 01:34:41 · Speaker 2

here there is W here there is E and here there is U

### 01:34:49 · Speaker 2

Is it alright now

### 01:35:00 · Speaker 2

See what is important is that you see that the parameters are shared across time in the sense that for all times okay x1 to xt the UVW matrices do not change okay they are actually shared across time and that is how an RNN is trained okay now how do we how do we get these UVW matrices there's an algorithm called back propagation

### 01:35:32 · Speaker 2

back propagation through time okay it's not at all difficult i'll tell you what it is so we know back propagation it's abbreviated as bptt we know back propagation but here what happens is the loss is calculated between yt and xt here right you calculate loss between xt and yt or rather at all points and you have a loss here at

### 01:35:55 · Speaker 2

uh x x5 and y5 and so on so what you should do is uh all these losses right have to be back propagated this way and they should also be back propagated this way

### 01:36:09 · Speaker 2

So there are two directions in which it back propagates and that is why this algorithm is called back propagation through time because there is a back propagation through time also time direction also. So you have to basically add those two losses one across the space one across the time. That's all an RMI is trying. As I said no if you are interested in a nice articles or you can also ask TAs to run through back propagation through time but now with all the things that you have learned in this course if you just look at

### 01:36:39 · Speaker 2

standard uh descriptions on ppt you will understand what it is okay

### 01:36:46 · Speaker 2

So this was being used then what happened is um uh

### 01:36:53 · Speaker 2

It was this uh

### 01:36:57 · Speaker 2

This is okay if you want to solve a supervised learning problem where you have input and output lengths equal. You can have different input lengths, different sequence lengths at the input, but the output lengths have to be different. But a problem like machine translation

### 01:37:20 · Speaker 2

Whereas both the input and output lengths are different

### 01:37:42 · Speaker 2

You can't use one standard standalone RNN, okay? What is done is the following so you have an RNN.

### 01:37:50 · Speaker 2

And by the way, what I just showed you is a naive RNN, okay? And there are improvisations over it by using things like LSTMs, long short-term memory networks, which are different ways of writing these two equations, okay? So to avoid this problem called vanishing gradient. So what happens is when you do backpropagation through time, because there is parameter sharing across time, you will multiply the same WUV matrices multiple times with each other.

### 01:38:20 · Speaker 2

And if the length of the sequence is too large, then the eigenvalues of that will reduce over time and the gradients will have very less values. That is in a nutshell what is called as the vanishing gradient problem. And you modify these equations so that there is a skip connection sort of thing that is used in resonance so that the gradients will not vanish. And also what is done is there is no like, this is only one layer RNN that I

### 01:38:50 · Speaker 2

showed you what can be done is you can have multiple hidden states like this okay and you have multiple matrices uh across the space also okay those are all improvisation that i don't talk about here what is done in in in cases where the input and output both of them have different lengths is the following that you use a typical encoder decoder sort of model where you have x0 to xt okay

### 01:39:20 · Speaker 2

We have HT here. You take another

### 01:39:26 · Speaker 2

and then or a sequence where you take h t and output y 1 okay and you take y 1 and give it as an input to the next uh unit and give get you on y 2 and take y 2 and give it as an input to this and get y 3 and keep doing this till you get the last symbol emitted which is y m so typically how it is uh

### 01:39:56 · Speaker 2

And in the in okay let's not call it YM so that is XT and this is

### 01:40:06 · Speaker 2

Typically how it is done is that there is a special symbol called end of sequence symbol, which is one of the tokens that is used. Now you keep emitting or you keep generating till you get the end of sequence symbol. And once you see the end of sequence symbol, just stop it there. That is how the translation or decoding is done. So this is the decoding network.

### 01:40:33 · Speaker 1

Sorry you're not audible at least to me

### 01:40:37 · Speaker 2

Is that so Hello

### 01:40:39 · Speaker 3

And also

### 01:40:39 · Speaker 4

You're audible for us homie

### 01:40:43 · Speaker 2

Okay, so this is the uh the input language

### 01:40:49 · Speaker 2

Sentence in input language and this is the translated output

### 01:40:56 · Speaker 2

Yeah, so this is the typical encoding-decoding model using RNN kind of architectures. And this was actually in the state of the art till, let's say, 2014-2015 times, okay? In some form or the other of it, which is an improvisation over this is what was being done. Any questions so far?

### 01:41:26 · Speaker 3

Yes just one question

### 01:41:29 · Speaker 3

Uh you said we don't send the speech initially we send the symbols right and then this is

### 01:41:36 · Speaker 2

No no this is this is this is a text translation no this is a machine translation task

### 01:41:41 · Speaker 3

No no no but before this

### 01:41:45 · Speaker 3

Uh you said symbols are transmitted not speech and speech is regenerated right

### 01:41:49 · Speaker 2

Uh, the you mean for the telephony, right? Long distance telephony and all that. Yes, that is true.

### 01:41:54 · Speaker 3

And how voice can be transmitted actually or how it will recognize like if I speak how the generated signal will match my voice

### 01:42:05 · Speaker 2

Okay. Yeah, that's a good question. See, what is done is the LPC model, right? One, there is content. There is another thing which is your signature, which is that no matter what you speak, there is a particular source signal that that mimics your voice, that is your signature. Okay. Even that is transmitted. And that does not require a lot more bits. I mean, that will go to speech signal, speech processing theory. So two things are transmitted. One, the

### 01:42:35 · Speaker 2

part of it the other is your voice signature think of it like that so it's like given your voice i can overlay any of the symbol any of the phoneme that i want on your particular voice that's the idea

### 01:42:50 · Speaker 3

And for this text thing the words can be in different sequence when transmitted into or translated into different language

### 01:43:01 · Speaker 2

No no no words no words will be of different length I said

### 01:43:06 · Speaker 3

No, length is fine, but one language may have a different order of words. If their literal meaning is taken, then it will not make sense. Like in different language, it will be a different sequence of words.

### 01:43:20 · Speaker 2

Now the words themselves will be very different right

### 01:43:24 · Speaker 3

Yeah and their sequence will also be different right

### 01:43:27 · Speaker 2

When words themselves change how would the sequence matter of course statements will be different so

### 01:43:33 · Speaker 3

how that is learned while predicting

### 01:43:37 · Speaker 2

Yeah, see that is why what you predict is given the previous word that you have out, I mean you have given as output, the next word is predicted. That is conditioned on the previous word. Now you can see here that the output, right, y2 depends on the previous word y1. So if you have enough data, the hope is that the model would see all those combinations implicitly.

### 01:44:06 · Speaker 3

Okay but first we'll be in the tradition

### 01:44:08 · Speaker 2

condition done condition ah see now the question is I mean how would the first word be uh predicted right the first word would be predicted based on the input sequence and what the input sequence information goes to the the output rnn through this last hidden state ht so it's like you encode the input sequence in this hidden state ht and that goes as an input to the decoder okay and

### 01:44:38 · Speaker 2

encoder gives you the first word right based on the first word and the hidden represent there is also one other hidden representation here no for the

### 01:44:47 · Speaker 2

or the decoder also based on that the next words are predicted one by one

### 01:44:52 · Speaker 3

Okay and is it trained on some kind of literature or trend?

### 01:44:55 · Speaker 2

Pairs pairs pairs they are trained on pairs of sentences from languages So you have to have a lot of pairs of English and Hindi sentences and given a pair of English and Hindi sentence it will be trained that way. It's always trained on pairs

### 01:45:12 · Speaker 3

Here you are saying

### 01:45:13 · Speaker 2

Yes be I have this

### 01:45:16 · Speaker 2

Let me write that down

### 01:45:50 · Speaker 2

Does it make sense

### 01:45:52 · Speaker 3

Yeah, so even if it's trained on pairs of sentences, it will not kind of do we do couple, right? It will just try to generate each word separately.

### 01:46:00 · Speaker 2

One word after one word after the other give conditioned on the previous word

### 01:46:10 · Speaker 2

Yeah thanks Vivek

### 01:46:12 · Speaker 4

So after the encoding process is over we just have a single uh vector right

### 01:46:17 · Speaker 2

Exactly that's an issue

### 01:46:20 · Speaker 4

Yeah so that's exactly what I want to know it's hard to believe that one small vector can

### 01:46:25 · Speaker 2

Yeah, it's a you point exactly that was actually an issue and that is when I'll just hold on to that question that would be my next narrative

### 01:46:25 · Speaker 4

It's a you

### 01:46:33 · Speaker 4

Okay

### 01:46:35 · Speaker 2

I'm actually building up to transformers so that I'll tell you why that is an issue and how people solved it okay Santosh

### 01:46:44 · Speaker 3

Yes, sir. So the number of RNN cells will be equivalent to the input sequence in the first layer.

### 01:46:52 · Speaker 2

Correct, correct, correct. See that is because it is it is the parameters are shared across time. We are just repeating the same RNN cell one after the other with a different input and hidden layer that's all. But the weights remain the same across time.

### 01:47:10 · Speaker 3

Okay. Also, my second question is that right now we have only two layers. If we have multiple RNN layers, so the final hidden state of first layer will be passed to the second layer and then like that. So the output will be passed to next layer. There will be two.

### 01:47:25 · Speaker 2

There will be two things right if you have like a two layer thing there will be one that goes like this one that goes like this

### 01:47:32 · Speaker 3

Um

### 01:47:33 · Speaker 2

Yeah, you can have any number of NN layers one after the other. Any number of hidden layers one after the other. You can make it deep.

### 01:47:42 · Speaker 3

Okay okay yeah

### 01:47:47 · Speaker 2

As I said in the beginning of the course, right, I like this is not a course where I teach NLP fundamentals and architectures, right? So, I mean, one can actually teach a full course on sequence modeling and how RNNs work and a lot of nuances there. But as I said, this course is more on, like you now you know what this course are, I'm almost coming at the end of it. But yeah, so an overview of RNNs are like this. Any other question on this?

### 01:48:18 · Speaker 2

if not let's move so as uh this was as i said no this was the the state of the art till

### 01:48:29 · Speaker 2

or machine translation okay like till let's say uh like 20 tens okay 20 tens this is what was being done and since uh this is not as as you can imagine right as Vivek was said was saying there's only one hidden state that has to compress all the information regarding the input sentence it was not doing great and that's why machine translation was not available commercially at large scale beyond the academic labs right so then came this nice idea which

### 01:48:59 · Speaker 2

I will tell you

### 01:49:05 · Speaker 2

is X1 this is XT and you have

### 01:49:16 · Speaker 2

one white two

### 01:49:26 · Speaker 2

to y uh what did we call s okay

### 01:49:31 · Speaker 2

Somebody thought that okay, why only have one?

### 01:49:38 · Speaker 2

hidden representation compress all the information that is regarding that that that that I mean regarding the entire input sentence so can we do something else so this is like the hierarchical VAE idea so somebody said okay we'll do this that we will take the

### 01:49:56 · Speaker 2

This is the first hidden representation. This is the second hidden representation, hidden representation corresponding to x3 and all that. Now what is done is that you take, you have, take all of these.

### 01:50:13 · Speaker 2

Take a linear combination of all of these so let me write it neatly

### 01:50:22 · Speaker 2

abut

### 01:50:25 · Speaker 2

AJ

### 01:50:32 · Speaker 2

HJ okay

### 01:50:36 · Speaker 2

if h1 h2 h3 and ht and compute this and give this let's call this uh h8 cap okay a

### 01:50:54 · Speaker 2

Cap okay, and give this as an input to

### 01:51:04 · Speaker 2

and have as many uh a t so there is a one and there is a two you have another string which is let's call this as a one

### 01:51:23 · Speaker 2

This is uh AJ to HJ

### 01:51:27 · Speaker 2

have a three cap and so on okay and give all of these as inputs to

### 01:51:38 · Speaker 2

the corresponding output sequences

### 01:51:42 · Speaker 2

Does it make sense? So what we are actually saying is take a linear combination okay and here the a's are also learnt okay.

### 01:51:59 · Speaker 2

Do you understand what is happening

### 01:52:02 · Speaker 2

Now instead of making one hidden layer have all the information and compress and then decode, saying I will take, I will tab the hidden representations from each of the time steps from the encoder side, take a learnable, have a learnable linear combination of that and then give it as an input while decoding.

### 01:52:27 · Speaker 2

Do you understand this

### 01:52:29 · Speaker 3

So what is the A here

### 01:52:31 · Speaker 2

A is a learnable constant

### 01:52:39 · Speaker 1

Professor how is AJ1 different from AJ2

### 01:52:39 · Speaker 2

Sort of hose

### 01:52:43 · Speaker 2

They are learned differently no

### 01:52:46 · Speaker 1

But though they are tapped from the same motor right

### 01:52:46 · Speaker 2

But they are mapped from the same mode. That's right. But these indices are taken to be different. So here what you do is here you only take j from like 1 to 2 and you make 1 to 3 and you take like just cumulatively do that.

### 01:53:06 · Speaker 2

Okay

### 01:53:11 · Speaker 2

there are different improvisations over it but the idea is clear right what you do is you take a linear combination of hidden layer representations and take a i mean learn the weights with which they have to be linearly combined and then give it as an input while you are decoding it is this idea clear

### 01:53:32 · Speaker 3

So sir here number of linear combinations equal to number of y's right I mean sequence number of

### 01:53:37 · Speaker 2

Number of voices number of voices correct

### 01:53:44 · Speaker 2

Okay, now do you know what these things are? This is actually what is called as attention.

### 01:53:53 · Speaker 2

This is what is called an attention okay uh like say like R and N's with attentions

### 01:54:04 · Speaker 2

is RNN with attention okay what you are doing is that you take the linear combination of hidden layers and then uh take uh give that as an input to the while decoding so this uh received a lot of attention okay uh and this gave a significant boost in terms of uh uh what the uh the what we could achieve using machine translation okay so then came this this this thing no which is the

### 01:54:34 · Speaker 2

transformer architecture where they said okay see any way you're using attentions here okay why even have an RNN cell because you end up with the problems of vanishing gradient and all that if you have very long sequence lengths so why not create an architecture right so come this transformer

### 01:54:58 · Speaker 2

Which is

### 01:55:00 · Speaker 2

An attention only architecture without a recurrent nature structure

### 01:55:20 · Speaker 2

Without recurrence

### 01:55:28 · Speaker 2

Yeah that is what a transformer is all about okay it is an attention only architecture without recurrence

### 01:55:35 · Speaker 2

I'll briefly talk about what attention is, I mean this transformer is, okay. Now you have like input sequence X that is equal to

### 01:55:49 · Speaker 2

x1 x2 up to xt right

### 01:56:01 · Speaker 2

Okay, now a transformer is some function f theta that will take each xj and gives you a corresponding zj.

### 01:56:14 · Speaker 2

Okay so now what does it do is given

### 01:56:20 · Speaker 2

A sequence X

### 01:56:27 · Speaker 2

of data X okay a transformer

### 01:56:34 · Speaker 2

outputs

### 01:56:38 · Speaker 2

A sequence of

### 01:56:43 · Speaker 2

representations or hidden layers or hidden representations I mean you don't have to call them hidden representations

### 01:56:54 · Speaker 2

z okay for corresponding to each of the input token so for every input token xi there is a uh corresponding uh representation z okay that is how you do it so now the question is how do you get the zg right now zg is given as

### 01:57:17 · Speaker 2

a linear combination of

### 01:57:34 · Speaker 2

alpha j what is called as t

### 01:57:46 · Speaker 2

value vectors okay now i will tell you what these value vectors are so now given

### 01:57:57 · Speaker 2

Given a

### 01:57:59 · Speaker 2

Data token

### 01:58:03 · Speaker 2

xj xj okay multiply that with

### 01:58:11 · Speaker 2

Three matrices, call one as the query matrix. So this is

### 01:58:19 · Speaker 2

Transpose X J okay then you have

### 01:58:27 · Speaker 2

value

### 01:58:30 · Speaker 2

matrix

### 01:58:32 · Speaker 2

the key matrix

### 01:58:38 · Speaker 2

What are we doing? We are getting three particular vectors. Okay. So here, do all.

### 01:58:51 · Speaker 2

Obtain three vectors

### 01:58:57 · Speaker 2

Okay as does here the W Q W V and W uh

### 01:59:06 · Speaker 2

wk are learnable and learned through backpropagation these are the learnable matrices do you understand so what is happening given a particular data point you take each of the token corresponding to it which is a vector okay uh pre-multiply that with three matrices okay and you get three other vectors call them query value and key is that okay

### 01:59:35 · Speaker 2

Let's call any query but any questions so far

### 01:59:40 · Speaker 1

XJ should be the entire sequence right not one of the

### 01:59:43 · Speaker 2

One of the no no no it's one of the components it's not the sequence because for every vector in the sequence okay you compute the query value and key

### 02:00:03 · Speaker 1

where x in itself is a vector

### 02:00:06 · Speaker 2

X is a sequence

### 02:00:10 · Speaker 2

X is a sequence that has p number of vectors

### 02:00:21 · Speaker 2

Is it okay

### 02:00:24 · Speaker 2

See how did we define a sequence we have defined a sequence this way right

### 02:00:30 · Speaker 2

A sequence every vector right a sequence is a t length

### 02:00:36 · Speaker 2

where every each component of it is a d dimensional vector

### 02:00:45 · Speaker 2

So every x j is a vector here

### 02:00:56 · Speaker 2

You get these three vectors right So now then what you do is

### 02:01:02 · Speaker 2

You define the

### 02:01:11 · Speaker 2

representation corresponding to the jth token as a linear combination of

### 02:01:21 · Speaker 2

all the value vectors corresponding to all the other tokens in the sequence okay so the question is how do you get this alpha j

### 02:01:33 · Speaker 2

This is alpha J cotton so what you do is that

### 02:01:48 · Speaker 2

Multiply the

### 02:01:56 · Speaker 2

jth query get the inner product of the jth query which actually I should call it alpha uh okay hold on

### 02:02:07 · Speaker 2

So uh

### 02:02:10 · Speaker 2

I need one more symbol here

### 02:02:14 · Speaker 2

This is what J oh now what the

### 02:02:23 · Speaker 2

Okay, let me just write it. So now you take the jth query and multiply that with the ith key.

### 02:02:36 · Speaker 2

declare that with the ith key okay then what you get is you get the attention score or the weight score corresponding to the jth query and the kth key okay so this will give you alpha ji

### 02:02:57 · Speaker 2

Is a scalar fine now uh

### 02:03:03 · Speaker 2

You need to multiply this

### 02:03:15 · Speaker 2

That's why I'm thinking how can I simplify this just give me a second quick think

### 02:03:26 · Speaker 2

There's one value

### 02:03:39 · Speaker 2

I need to look at

### 02:03:42 · Speaker 2

Dude

### 02:03:45 · Speaker 2

Yeah this is

### 02:03:47 · Speaker 2

So fix this K

### 02:04:11 · Speaker 2

This is what it is

### 02:04:14 · Speaker 2

Uh do you understand what's happening

### 02:04:18 · Speaker 2

Okay, so I'll tell you, see now what is happening is that we are given, I'll write it here, it will be easier.

### 02:04:30 · Speaker 2

I thought this class would end early these are these are

### 02:04:36 · Speaker 2

These are sequences, right? FT sequences. What is first done is that you multiply these with the W matrices and get the corresponding queries. So this is Q1, Q2 up to Qt. We have these queries and we have these, multiply that with the K matrix and get the

### 02:05:04 · Speaker 2

Okay and then you have the multiply that with the

### 02:05:10 · Speaker 2

value matrices to get the values

### 02:05:15 · Speaker 2

Okay now what we are doing is uh we get

### 02:05:22 · Speaker 2

to get z j okay z 1 to get z 1 what you do is you take the uh inner product okay between the query corresponding to the first token okay with the query keys corresponding to all of the tokens so this is a you take an inner product like this between this these two

### 02:05:54 · Speaker 2

East two east two

### 02:05:58 · Speaker 2

these two and these this will give you what will this give you this will give you uh the way i have written it this will give you alpha 1 1 alpha 1 2 alpha 1 t

### 02:06:17 · Speaker 2

Is this okay

### 02:06:23 · Speaker 2

Are you getting it?

### 02:06:28 · Speaker 2

questions on how are we getting alphas

### 02:06:34 · Speaker 2

This is important so please tell me if you don't understand this

### 02:06:49 · Speaker 2

Hello am I there Am I audible

### 02:06:52 · Speaker 4

Yes sir you already will yes

### 02:06:54 · Speaker 2

Okay. Yeah. Total radio silence. So I don't know how to interpret it. Is it okay? Did all of you get how to get these alphas?

### 02:07:10 · Speaker 2

Yes hello

### 02:07:18 · Speaker 2

Now how are these V's obtained? Sorry, Z's obtained? They are obtained by taking a linear combination of all these values, okay, and they are weighted.

### 02:07:31 · Speaker 2

by the corresponding alphas. In fact, it's actually a convex combination. So what is done is you don't use alphas, but you use betas.

### 02:07:50 · Speaker 2

And so

### 02:07:53 · Speaker 2

beta j i's okay where betas

### 02:07:59 · Speaker 2

Or you take alphas okay

### 02:08:03 · Speaker 2

And divide that by some constant d, which is the dimensionality of data. And then you do a

### 02:08:11 · Speaker 2

See that

### 02:08:14 · Speaker 2

Alphas are soft max

### 02:08:19 · Speaker 2

Over alpha divided by t, that's all. So now, why do you do this? This you do because

### 02:08:27 · Speaker 2

all beta j's right they are bounded between 0 and 1 and they are simply sum to 1 that is why you do this soft mat so that the linear combination of the values that you are taking okay uh is bounded between 0 and 1. so now let me repeat what is done here is that

### 02:08:47 · Speaker 2

You given a token given a sequence of tokens. Okay, which is an input data point one input data point you define three matrices Call them as and multiply those data points with the with these three matrices Okay, they can call them as the query value and key Vectors so corresponding to each of the token you will get three vectors Okay, then the representation corresponding to each

### 02:09:17 · Speaker 2

of the input uh token is a linear combination of all the value vectors corresponding to each of the tokens okay that's all now how do you define uh which of the mean how do you get uh what is the weight factor for the linear combination to get the weight factor for the linear combination you use the query and key vectors how uh you take the query vector corresponding

### 02:09:47 · Speaker 2

to the token of interest. You take an inner product of that vector with all the key vectors corresponding to all the tokens and normalize it so that it lies between 0 and 1. That would give you what is the weight or scale which with with which you have to scale each of the value vectors to obtain the representation corresponding to the I mean the token of interest. So this is one

### 02:10:16 · Speaker 2

Transformer block

### 02:10:24 · Speaker 2

with a single head they call it and there is also a counterpart uh called the multi-head uh attention i'll talk about that in a while but yeah any questions so far

### 02:10:40 · Speaker 4

So so if we shuffle the X1 to Xt then the Zs will also be shuffled

### 02:10:50 · Speaker 4

In the sense like the if the sequence changes

### 02:10:54 · Speaker 2

Yes, it is true.

### 02:10:58 · Speaker 4

Okay so please go ahead yeah so

### 02:11:04 · Speaker 4

So so does it when it changes does it still remain the do the individual values still remain the same or will they also change

### 02:11:11 · Speaker 2

No, no, they do change, you know, they do change depending upon what the sequence, what the, what the correspond, what the relative positions of each of the tokens are in the sequence. They do change.

### 02:11:34 · Speaker 2

Yeah, case fixed. Yeah. So you you keep hearing about this context lens of all these LLMs, right?

### 02:11:42 · Speaker 2

They say that they are coming up with like larger and larger context length. This t is what is called as context length. Now it is like 2500 is what the context length of GPT is and so on. That is the context length. So now you might ask this question.

### 02:11:59 · Speaker 2

We started by saying that each of the input data point will have different sequence length. How does transformer handle it? They handle it by just zero padding. That's all. So they keep a fixed context length. And then if that length is equal to the highest possible length of the highest possible sequence. And for all the other sequences that have length less than the highest possible length sequence, there's a zero pad them and make them equal length. And now how does that, how is that handled?

### 02:12:29 · Speaker 2

The hope is that that is handled by the appropriate representation

### 02:12:37 · Speaker 2

Okay, the attention for or rather these alphas and betas for that corresponding

### 02:12:44 · Speaker 2

zero tokens will be zero and it has been observed that they will actually ignore them

### 02:12:53 · Speaker 3

One more point here so I mean here that position information is not present

### 02:12:58 · Speaker 4

Full of the

### 02:12:58 · Speaker 2

Yeah, yeah, hold on. That's correct. That is correct. And do you recall that during our DDPM discussions, I talked about positional embeddings, where we have to do give T the time information also as an input, right? In transformer also, what is given is in addition to this, T is also given as an input using the positional encoding.

### 02:13:25 · Speaker 2

for the precise reason that you said

### 02:13:34 · Speaker 2

positional embeddings and we talked about positional embeddings during the

### 02:13:40 · Speaker 2

L M lectures sorry the diffusion lectures okay fine now how do we finally solve the uh the

### 02:13:51 · Speaker 2

Sequence to sequence problem is that we have here a transformer block.

### 02:13:58 · Speaker 2

There is one other like normalization layer that they use and also a skip connection like ResNet and so on, right? I'm skipping that. The major focus is on attention, okay? So can yeah, there are enormous amount of literature on this. You'll understand. And the difficult part is how the attentions are actually

### 02:14:20 · Speaker 2

computed so you get z1 through zt okay and there is this this is the encoder

### 02:14:27 · Speaker 2

And similarly there is a decoder block

### 02:14:33 · Speaker 2

It uh what does it do is it'll take these uh

### 02:14:39 · Speaker 2

embeddings are the representations given by the encoder as the input okay and then do one autoregressive uh uh generation so now you get one y1 and you take y1 as an input and give it just like you do it in rnn right so you take that and you get y2 and you take that as give it as an input and so on okay so in fact this is exactly what a large language model does i mean in the okay

### 02:15:09 · Speaker 2

So this is bald kind of language model this is how the training happens in addition to this there's also

### 02:15:18 · Speaker 2

like attention blocks between the encoder and decoder okay

### 02:15:24 · Speaker 2

These are called uh

### 02:15:26 · Speaker 2

cross attention or details so this is whatever we saw right which is attention between the input tokens that is called self attention and there is also attention between the

### 02:15:42 · Speaker 2

queries keys of the the encoder and the query keys of the decoder that is called cross attention and this is actually the bare bone of what the modern day LLMs do okay so now you know that right I mean you are given a particular prompt when you give a GPT a prompt what you are actually doing is giving a prompt to the encoder and depending upon your prompt this decoder generates and how is the training done surprisingly enough training is completely supervised

### 02:16:14 · Speaker 2

Supervised training

### 02:16:18 · Speaker 2

using KL minimization I mean like uh the

### 02:16:22 · Speaker 2

Usual cross entropy loss is what is used

### 02:16:28 · Speaker 2

It's all the bare bare minimum try bare bone training of an L M happens in a completely supervised way. Okay. Using K L minimization. So you have pairs of these tokens input and output tokens. In fact, actually what happens is that you first try in an embedding extractor using the self supervised learning techniques that we just saw no masked reconstruction. Last class we looked at masked reconstruction. So what is done is let me just talk about it perhaps.

### 02:16:58 · Speaker 2

So first thing that is done is okay this is the broad level LLM training typically happens this way

### 02:17:08 · Speaker 2

So there is first a self supervised pre-training

### 02:17:20 · Speaker 2

Well that's

### 02:17:22 · Speaker 2

And by the way architecture wise right everything that is used in an LLM today are transformers you take a transformer

### 02:17:31 · Speaker 2

Uh take an input sequence

### 02:17:36 · Speaker 2

And uh

### 02:17:39 · Speaker 2

You get the embeddings and the task is to simply reconstruct the data back.

### 02:17:51 · Speaker 2

using the encoding so I technically speaking there's also an encoder decoder model here another transformer

### 02:18:01 · Speaker 2

the decoder

### 02:18:05 · Speaker 2

g1 to z3 and what is given as an input is uh a a version of x okay where it is uh where x cap is

### 02:18:18 · Speaker 2

masked masked version of X

### 02:18:25 · Speaker 2

usual self-supervised learning task that we do right and this these z's will go as input to the decoder and what is given back is the true data so this is exactly what is done in BERT okay so you have an encoder and a decoder and encoder takes a masked version of x with random mask and it reconstructed data so this is what is called as the self-supervised pre-training

### 02:19:00 · Speaker 2

Okay, this is done. Once this is done, you get embeddings of data. So then you use a usual encoding decode, encoder decoder model in the second stage using supervised fine tuning.

### 02:19:23 · Speaker 2

Supervised fine tuning okay on the embeddings obtained in the

### 02:19:38 · Speaker 2

obtained using self-supervised learning

### 02:19:45 · Speaker 2

See surprisingly uh

### 02:19:49 · Speaker 2

The inner workings of LLM is very, very simple. I mean, from an ML complexity perspective, all you do is take a lot of data and do a self-supervised pre-training using master-conception kind of tasks, and then you do a supervised fine-tuning on whatever data that you want to fine-tune it on. That's all it is. Using transformer as the backbone.

### 02:20:12 · Speaker 2

Now, I mean, there are nuances here where when you are doing fine tuning, right, you may not have a lot of data. How do you do it without fine tuning? There is this retrieval augmented generation or RAG kind of frameworks. And also this low rank reconstruction, low rank approximation for fine tuning, where the problem is that if this pre-training, the model is like billions of parameters, you can't, you can't fine tune on all billions of parameters. You just take a subset of them and then fine tune. And all those are other,

### 02:20:42 · Speaker 2

supervisions and nuances but at a broad level this is exactly what happens so we there's a transformer which is which is the big backbone architecture you take data typically from the entire internet and do a self supervised pre-training using uh uh mass reconstruction task which we have seen and then whatever take that model which generates embedding and do a supervised fine tuning on whatever data that you want and that's and if you do that

### 02:21:12 · Speaker 2

But then you already have a like GPT two or GPT three that is there

### 02:21:17 · Speaker 2

that's that's what it is uh any questions on this yeah as i said no this is not a full course on llm so i don't go to the nuances of it just wanted to introduce and put it in the perspective of what the the so-called modern llms are doing so this is exactly what it is in the as i said no in terms of ml complexity it's very very simple there is a self-supervised pre-training using transformers and there is a supervised fine-tuning that is happening using uh ugr

### 02:21:47 · Speaker 2

cross entropy kind of losses right and the underlying architecture that is used is a transformer please also remember the word generative AI right it is used in a very very loose sense today in in outside of expert community where it is used for like image generation language generation and all that whenever there are there is a sequence task that is done no it a transformer is used and this kind of recipes follow

### 02:22:17 · Speaker 2

So wherever there is an image generation task no typically transformer is not used a diffusion model is used

### 02:22:27 · Speaker 2

Okay, so that's about it. That's all I wanted to cover in this course.

### 02:22:35 · Speaker 2

Yeah so let's maybe just stop recording

### 02:22:50 · Speaker 2

Yeah, see the thing is, even when you fine-tune, right, sometimes, you know, it will not, it may not suit your purpose. You know, it's think of it like using an additional data that you have, okay, without doing a fine-tuning, I mean, supervised fine-tuning on it. You use that additional data to guide your transformer or generator in some way, I mean, or the decoder. See, in all our generative

### 02:23:20 · Speaker 2

first modeling right we know
