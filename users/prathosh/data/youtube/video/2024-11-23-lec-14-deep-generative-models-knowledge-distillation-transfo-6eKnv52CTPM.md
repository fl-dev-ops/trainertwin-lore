---
id: 6eKnv52CTPM
title: Lec 14 - Deep Generative Models Knowledge distillation Transformers
date: '2024-11-23'
url: https://www.youtube.com/watch?v=6eKnv52CTPM
description: ''
author: prathoshap5226
duration: 02:23:22
model: saaras:v3
transcript: true
---

# Lec 14 - Deep Generative Models Knowledge distillation Transformers

## Transcript

### 00:00:03 · Speaker 3

Not yet

### 00:00:05 · Speaker 2

Okay. So yeah, so we will see that, you know, we'll let us I'll I'll tell you how people evolved to transformers and uh talk about transformers as well and then we can close. Okay.

### 00:00:17 · Speaker 4

we have distillation also we plan to do.

### 00:00:19 · Speaker 1

College Stationary is pending

### 00:00:21 · Speaker 2

distillation is printing. Okay, so let's okay, let's start with distillation and then move to sequence to model step. Okay.

### 00:00:28 · Speaker 0

N

### 00:00:30 · Speaker 0

Sorry, minding. Okay.

### 00:00:55 · Speaker 0

Okay, so this was

### 00:00:57 · Speaker 2

an idea that was proposed by Hinton and his group in early late two thousand I think it's a

### 00:01:09 · Speaker 2

जो ऑब्जेक्टिव हियर

### 00:01:16 · Speaker 1

Hello

### 00:01:16 · Speaker 2

is not the primary objective but still the context in which distillation is used to

### 00:01:21 · Speaker 1

today. The objective is to reduce

### 00:01:30 · Speaker 1

reduced the size of

### 00:01:36 · Speaker 0

sharing something

### 00:01:37 · Speaker 1

Radiola

### 00:01:39 · Speaker 1

Don't you see my screen?

### 00:01:41 · Speaker 0

Not yet, sir.

### 00:01:42 · Speaker 1

product form

### 00:01:48 · Speaker 1

It is saying that it is showing the screen. Okay, let me do it again.

### 00:01:54 · Speaker 3

at least I am not able to see.

### 00:01:56 · Speaker 1

No no

### 00:01:56 · Speaker 0

No, no, it is not shared.

### 00:02:20 · Speaker 0

still not seen

### 00:02:25 · Speaker 1

No sir

### 00:02:27 · Speaker 0

rejoin from here.

### 00:03:09 · Speaker 1

Let me know when you see the screen

### 00:03:11 · Speaker 0

you can see

### 00:03:12 · Speaker 3

No sir

### 00:03:13 · Speaker 2

Hello? Okay.

### 00:03:13 · Speaker 3

Okay

### 00:03:14 · Speaker 3

Yeah

### 00:03:15 · Speaker 2

ओके। सो, द ऑब्जेक्टिव हियर इस टू रिड्यूस द साइज़ ऑफ वेरी लार्ज न्यूरल नेटवर्क्स विदाउट कॉम्प्रोमाइजिंग द

### 00:03:24 · Speaker 0

Hello

### 00:03:24 · Speaker 0

Performance

### 00:03:42 · Speaker 2

Hello

### 00:03:42 · Speaker 0

This is the objective

### 00:03:44 · Speaker 2

The idea is pretty simple when it was proposed.

### 00:03:49 · Speaker 2

it was proposed without further understanding of what was actually happening. I'll tell you what it is. So in in knowledge registration what happens is you have a very large neural network that has to be compressed. So

### 00:04:04 · Speaker 2

large neural network

### 00:04:06 · Speaker 0

to be compressed

### 00:04:13 · Speaker 0

is usually called the teacher network.

### 00:04:22 · Speaker 0

Then the another neural network

### 00:04:32 · Speaker 0

with the desirable size.

### 00:04:41 · Speaker 0

that is called the student network.

### 00:04:49 · Speaker 1

Sir, I have a question.

### 00:04:51 · Speaker 3

action

### 00:04:52 · Speaker 2

let's let me complete this and then yeah tell me what is it

### 00:04:57 · Speaker 3

Sir, uh this is related to like a bit related to the assignment. So like in the animal data set, we have around five thousand five hundred images. We divided among ninety classes. Right? And even when we were going for the classification task, we saw that the training accuracy was very high, but the testing accuracy is always very low.

### 00:05:23 · Speaker 1

Hmm

### 00:05:24 · Speaker 3

So what my perception was since the data this the the data size is very small like we have good number of classes but not sufficient images per classes that is the reason that the model is able to learn the features like you know remember the features and not able to classify properly on a newer set of images is that the correct interpretation

### 00:05:55 · Speaker 2

Yeah, why, what is the relevance of that question to what we are doing now? I think it would have been asked at the end of the class, right? Anyway, so now that you have asked.

### 00:06:02 · Speaker 3

Anyway, so now that you have asked. Yeah. So the reason I am asking

### 00:06:05 · Speaker 2

So we were looking at distillation I think after this after I had finished this this part you could have asked anyway. Yeah that can be one of the reasons so what happens is when your data has

### 00:06:19 · Speaker 2

multiple short modes. So, you know, you can think of each of the classes as one data mode. And typically when the data set has too many modes, okay, with very less samples amongst each of the mode, then getting a discriminator or classifier that would put decision boundaries across those classes would be difficult.

### 00:06:44 · Speaker 2

Yeah, so in that way your interpretation is correct.

### 00:06:48 · Speaker 0

Okay

### 00:06:50 · Speaker 0

Okay sir

### 00:06:52 · Speaker 2

Let me continue with what we were doing. So if you have any questions on assignments etcetera, please note that down and ask at the like rather end of the class, okay? So that it does not break the flow of what is being done. Of course you can ask questions regarding what is being taught. Okay.

### 00:07:11 · Speaker 2

Anyway, where were I? Where was I? uh Yeah, so disrelation, two neural networks. One uh large neural network uh that needs to be compressed, that is called, that is typically called the teacher network. And there is another neural network with the desirable size, which is called the student network, okay?

### 00:07:32 · Speaker 2

Now, um

### 00:07:36 · Speaker 0

So Teacher Network

### 00:07:45 · Speaker 0

is trained

### 00:07:50 · Speaker 0

it

### 00:07:53 · Speaker 2

supervised objective. Whatever suppose you are solving the classification problem, it is solved with

### 00:07:59 · Speaker 2

first objective with cross entropy loss and whatever the supervision might be.

### 00:08:13 · Speaker 0

supervised objective independently of the student

### 00:08:39 · Speaker 0

What happens is there's a network here.

### 00:08:51 · Speaker 0

whatever the task might be, okay, let us call this the teacher network.

### 00:09:02 · Speaker 1

some data, some task. And it is trained with minimizing, let's call the parameters theta. Just

### 00:09:12 · Speaker 1

usual

### 00:09:15 · Speaker 1

minimizing the expected loss function. Okay, which is

### 00:09:22 · Speaker 1

between

### 00:09:25 · Speaker 1

let's call this

### 00:09:26 · Speaker 2

Uh

### 00:09:26 · Speaker 1

Hello

### 00:09:27 · Speaker 2

theta may be f theta of x, y

### 00:09:34 · Speaker 2

Yeah, so this is the usual empirical risk minimization, okay? For supervised training. Now there is a smaller neural network which is called the student network.

### 00:09:51 · Speaker 0

same pairs of x and y

### 00:10:02 · Speaker 0

is fee, okay? Now this has two objectives for training.

### 00:10:09 · Speaker 0

one is a

### 00:10:12 · Speaker 0

K L objective between

### 00:10:22 · Speaker 0

It's called this.

### 00:10:24 · Speaker 0

C T and this as C S.

### 00:10:36 · Speaker 0

skill objective between the distribution of ZT and the distribution of

### 00:10:42 · Speaker 0

CS

### 00:10:43 · Speaker 1

Hello

### 00:10:44 · Speaker 0

Plus

### 00:10:46 · Speaker 0

supervised loss

### 00:11:16 · Speaker 0

plus

### 00:11:25 · Speaker 0

supervised loss between

### 00:11:29 · Speaker 0

son by

### 00:11:32 · Speaker 0

Okay, so

### 00:11:32 · Speaker 1

what is happening here is that

### 00:11:37 · Speaker 1

When the student network is being trained, okay? Now the uh scale divergence between

### 00:11:49 · Speaker 1

the distributions of some

### 00:11:54 · Speaker 1

features in some

### 00:11:55 · Speaker 2

uh some layers. Typically the uh pre softmax layer of the student and teacher network is minimized. Okay? And there is a supervised loss that is uh minimized at the uh loss between the

### 00:12:12 · Speaker 2

real true predictions and the predictions of the neural network. Okay? So now what is this doing is this

### 00:12:20 · Speaker 2

into

### 00:12:20 · Speaker 1

but

### 00:12:24 · Speaker 1

the features

### 00:12:30 · Speaker 1

learn or match actually learn or match the features of teacher

### 00:12:38 · Speaker 1

Okay

### 00:12:40 · Speaker 1

Two

### 00:12:42 · Speaker 1

tough students, students,

### 00:12:44 · Speaker 1

that is what it is doing, huh?

### 00:12:50 · Speaker 1

right? by ensuring that the KL divergence between the distributions of

### 00:12:56 · Speaker 0

representations between the

### 00:13:17 · Speaker 0

about it. So,

### 00:13:18 · Speaker 2

by making by ensuring that the the KL divergence between the features of the teacher and the students are are matching. I mean the idea is to ensure that the features that the teacher has learned is imbibed by the student. You know if it does that then whatever the performance that the teacher is supposed to give with a larger network can be

### 00:13:48 · Speaker 2

achieved or can be expected to be achieved using the student network. Okay. So procedure wise this is what is done. So in practice

### 00:14:03 · Speaker 1

the KL divergence term, no, between the teacher features and student features.

### 00:14:12 · Speaker 1

is approximated

### 00:14:18 · Speaker 0

Bye

### 00:14:21 · Speaker 0

So mean squared error loss

### 00:14:24 · Speaker 0

Squared or loss

### 00:14:24 · Speaker 1

average, it is actually mean squared annual loss.

### 00:14:33 · Speaker 1

between

### 00:14:35 · Speaker 1

zero

### 00:14:36 · Speaker 2

and G S

### 00:14:40 · Speaker 2

Yeah, this is also not a bad approximation, right? When we assume these two distributions, PT and PZ, actually what this actually means that

### 00:14:51 · Speaker 2

to have P T coming from a Gaussian, okay? And P S is also coming from a Gaussian. If you make this assumption, then we know that the scale divergence is equivalent to uh minimizing the mean squared error between the features taken when averaged over all possible

### 00:15:14 · Speaker 2

Samples

### 00:15:15 · Speaker 1

Okay

### 00:15:17 · Speaker 1

Okay. So

### 00:15:25 · Speaker 2

This is what this is how the finally what is done is instead of using the teacher network, uh teacher network is discarded, uh meaning it is uh uh I mean it is it is the goal is to not use the teacher network but to use the student network for further processing. So that is the idea.

### 00:15:43 · Speaker 2

Okay, so I will tell you, so there is this was what was being done uh in distillation. Um now a very recent paper came that gave a very nice statistical perspective of why should this work, okay? What is actually happening uh under the hood? I'll talk about that. Before that, if there are any questions on the procedure of what distillation is, uh do ask. And by the way, in your assignment what I've asked is, uh I've asked you to use a large teacher network and

### 00:16:16 · Speaker 2

distill it down to a smaller student and compare it with just training a student network separately. I mean meaning a network that is of the size of the student network separately and then compare the performance. Okay. Okay questions now. uh Yeah Vivek.

### 00:16:32 · Speaker 4

So, uh two small questions. So, should the sizes of the features of uh the Z and the um uh I mean the both the ZT and ZS, should they both be the same?

### 00:16:48 · Speaker 2

By sizes you mean the dimensionality.

### 00:16:50 · Speaker 4

dimensions yes.

### 00:16:52 · Speaker 2

Yeah, they they have to be same, otherwise how would you define KL divergence?

### 00:16:55 · Speaker 4

Okay, so the second question is, how important is the KL divergence term in this? So if we skip that and if we simply use a completely different network, so is that still called a distillation?

### 00:17:09 · Speaker 2

what do you mean by that? See if you if you do not use any features from the teacher okay while training the student at work then this there's no distillation right it is simply an independent training.

### 00:17:24 · Speaker 4

Right, Okay

### 00:17:25 · Speaker 2

Isn't it?

### 00:17:26 · Speaker 4

Yeah, meaning

### 00:17:26 · Speaker 2

See, it is called distillation only because you have a teacher network and you are using those features to, uh you are actually imposing those features on the features of the student, that's all, right?

### 00:17:40 · Speaker 4

Right, yes sir.

### 00:17:41 · Speaker 2

It's like whatever teacher network has learned, uh the transformation that the teacher teacher network has learned, trying to ensure that the features of the student network matches those features at a distributional level.

### 00:17:54 · Speaker 4

Uh yeah, but if if the student network is struggling too hard to simply match with the teacher network more than uh increasing the accuracy of the classification task, then should we reduce the weightage on the KL diversion staff?

### 00:18:04 · Speaker 3

Then should

### 00:18:08 · Speaker 2

Of course, of course, of course. I mean, that's always there, right? I mean, when you have two loss terms, you can you always wait them accordingly.

### 00:18:16 · Speaker 4

Okay. Yes, so that's all. Thank you.

### 00:18:18 · Speaker 2

Okay

### 00:18:22 · Speaker 2

Okay. uh Yeah, Sarvesh.

### 00:18:26 · Speaker 4

Sir, if Z are just the pre softmax terms, so why to include this expected loss in student network? Because anyways, they will be same, right? If they are same then

### 00:18:36 · Speaker 2

of

### 00:18:37 · Speaker 2

Good question. See what happens, this is, this is a practical thing.

### 00:18:46 · Speaker 2

What happens is when when you do not have the supervised loss because I mean teacher network may itself have not learned to solve the task properly right? The performance of the student network will not be great if you don't include that.

### 00:19:03 · Speaker 4

because just to be sure that it is learning the main

### 00:19:07 · Speaker 2

Correct

### 00:19:08 · Speaker 2

correct. Whatever is needed, no, the main learning should happen. That is why the supervised loss is also included.

### 00:19:08 · Speaker 4

Correct

### 00:19:17 · Speaker 0

Thank you

### 00:19:20 · Speaker 2

Sanchit

### 00:19:22 · Speaker 3

Sir, if the teacher network is like as we are asking it is very large and let's say the data size is not sufficient enough for the learning to happen correctly. And at the same time then we are trying to use that loss for training the student network.

### 00:19:42 · Speaker 3

So, how can we expect the student network to be learned properly?

### 00:19:48 · Speaker 2

yeah, saying if the teacher network is bad, how do what does what happens to distillation?

### 00:19:55 · Speaker 3

No no like my like I I asked a previous question right if the uh the data set is not sufficiently large. So we cannot expect the teacher network itself to learn the uh the classification properly. And then we are trying to train the student network.

### 00:20:16 · Speaker 2

that is what, no, what happens if the teacher network itself is not good?

### 00:20:20 · Speaker 3

Mm-hmm

### 00:20:21 · Speaker 2

That is what you are asking. Yeah.

### 00:20:22 · Speaker 3

Yes sir

### 00:20:23 · Speaker 2

Yeah, so yeah, so what happens is if there is like some level of uncertainty in the teacher network is okay, as we will see in the theory. But if teacher network is not even doing like

### 00:20:39 · Speaker 2

Hello

### 00:20:41 · Speaker 2

supervised learning, right? Then obviously the student network will perform badly.

### 00:20:48 · Speaker 2

Yeah, so we'll have to ensure that the teacher network has to have some level of good accuracy for this to work.

### 00:21:00 · Speaker 0

Okay

### 00:21:00 · Speaker 1

Okay

### 00:21:01 · Speaker 1

anything else?

### 00:21:19 · Speaker 1

Shall we continue?

### 00:21:26 · Speaker 0

Yeah, just one small query. What is the benefit? Is it going

### 00:21:29 · Speaker 4

to use less resources

### 00:21:32 · Speaker 2

training definitely not

### 00:21:36 · Speaker 2

But inference of course right because the student network is by design smaller in terms of sizes. It is going to use less number of less resources during inference. Because finally what you what you end up storing is the student network not the teacher network.

### 00:21:57 · Speaker 0

Okay

### 00:21:58 · Speaker 2

Okay

### 00:21:59 · Speaker 3

सर, वन मोर क्वेश्चन, द ट्रेनिंग हैस टू हैपन साइमलटेनियसली और फर्स्ट वी हैव टू ट्रेन द टीचर नेटवर्क एंड देन द स्टूडेंट नेटवर्क?

### 00:22:09 · Speaker 2

So that's a design choice. Typically what is done is

### 00:22:17 · Speaker 2

feature network is trained up to some level, okay, where you have decent accuracy and then, uh both of them are trained simultaneously.

### 00:22:28 · Speaker 2

But you can completely train the teacher network once and then freeze it and then do a distillation that is also possible.

### 00:22:38 · Speaker 2

That's a design choice

### 00:22:40 · Speaker 1

Okay

### 00:22:40 · Speaker 2

Okay. Okay, so, yeah, so this is what is done in procedurally. Now, as I said, no, there is a very nice interpretation so as to why this works.

### 00:22:54 · Speaker 0

just try to look at that

### 00:23:11 · Speaker 0

statistical perspective on knowledge distillation

### 00:23:15 · Speaker 0

Okay

### 00:23:19 · Speaker 0

Okay, so what happens is,

### 00:23:23 · Speaker 0

in typical

### 00:23:27 · Speaker 0

Supervisory Learning

### 00:23:37 · Speaker 0

the

### 00:23:39 · Speaker 0

labels

### 00:23:44 · Speaker 0

are deterministic

### 00:23:51 · Speaker 0

in the sense that

### 00:23:54 · Speaker 0

Every date

### 00:23:55 · Speaker 2

point. So okay, let us design the problem that way.

### 00:24:01 · Speaker 2

suppose uh the class labels right they belong to uh

### 00:24:10 · Speaker 2

one out of K categories.

### 00:24:13 · Speaker 1

okay? In a in a K class classification problem, then typically

### 00:24:23 · Speaker 1

for each x

### 00:24:28 · Speaker 1

for each x, okay? y

### 00:24:37 · Speaker 1

wise only

### 00:24:41 · Speaker 1

one of the

### 00:24:43 · Speaker 1

K plus one labels.

### 00:24:49 · Speaker 0

Right? This is what happens.

### 00:24:53 · Speaker 0

However,

### 00:25:00 · Speaker 0

it is always uncertainty in labeling.

### 00:25:19 · Speaker 0

certainty in abling.

### 00:25:23 · Speaker 0

which implies that for each x

### 00:25:31 · Speaker 0

there exists

### 00:25:36 · Speaker 0

there exists a distribution over y

### 00:25:45 · Speaker 1

P of Y given X

### 00:25:48 · Speaker 1

So

### 00:25:48 · Speaker 2

what I'm trying to say is, let's say

### 00:25:50 · Speaker 1

say that there is you have

### 00:25:52 · Speaker 1

you have an image that

### 00:25:53 · Speaker 2

you want to label

### 00:25:56 · Speaker 2

Okay. Now, okay, so I'll take an

### 00:25:58 · Speaker 0

example that is sort of ambiguous.

### 00:26:10 · Speaker 0

Okay, sure, I'll try it.

### 00:26:13 · Speaker 0

like this.

### 00:26:15 · Speaker 0

Okay

### 00:26:15 · Speaker 1

Which digit do you think it is? I mean, let's say that I'm

### 00:26:21 · Speaker 1

annotating MNIST

### 00:26:25 · Speaker 0

Right

### 00:26:28 · Speaker 1

sorry.

### 00:26:32 · Speaker 1

Now

### 00:26:34 · Speaker 1

So people

### 00:26:35 · Speaker 1

write it this way you know so this

### 00:26:36 · Speaker 1

means that this has

### 00:26:38 · Speaker 1

Hello

### 00:26:40 · Speaker 2

some likelihood of being in three and some likelihood of being in five.

### 00:26:51 · Speaker 1

Right? So now there exists so what is this along y axis what I have written is this is p of y given x.

### 00:27:05 · Speaker 1

Okay. Now what is done in typical supervised learning is, Okay, in

### 00:27:14 · Speaker 1

supervised learning

### 00:27:21 · Speaker 0

p of y given x is approximated

### 00:27:37 · Speaker 0

ಮತ್ತೆ ಡೆಲ್ಟಾ ಫಂಕ್ಷನ್

### 00:27:43 · Speaker 2

Isn't it so the uncertainty that is associated with the labeling is completely ignored uh when uh I mean in in typical supervised learning, right? Now, what this uh this this nice paper does is the following.

### 00:28:01 · Speaker 2

they consider. Okay, so any questions so far? What I'm trying to say is there are there is an uncertainty that exists with the labeling inherently because every data point can

### 00:28:18 · Speaker 2

can probabilistically belonging to one of K possible classes. But labeling is always done in such a way that uh the uncertainty that that is there in the labeling is ignored and labels are marked labels are given in a deterministic way. Is this clear?

### 00:28:39 · Speaker 0

Yes sir. Yeah.

### 00:28:40 · Speaker 2

ओके. नाउ व्हाट इज द कॉन्सीकवेंस ऑफ इट इज द फॉलोइंग? डिफाइन

### 00:28:49 · Speaker 0

two types of risks or losses

### 00:28:56 · Speaker 0

One is the typical supervised loss.

### 00:29:07 · Speaker 0

supervised loss

### 00:29:10 · Speaker 0

with deterministic labeling

### 00:29:17 · Speaker 1

call it R. Okay? And there is, okay, let's call it R cap. And there is something called base distal loss, okay?

### 00:29:34 · Speaker 1

base distal loss, call it R B cap.

### 00:29:38 · Speaker 2

Now this is uh what can actually be shown is that this is we know what R cap is right? This is simply the expectation of the loss. F is the classifier that we are looking at. This is F theta of X comma Y. This is

### 00:29:55 · Speaker 2

what it is, this is with respect to P X Y. And this can be shown as KL divergence.

### 00:30:05 · Speaker 1

Between

### 00:30:06 · Speaker 2

the

### 00:30:09 · Speaker 1

distribution of F theta

### 00:30:15 · Speaker 1

of X

### 00:30:20 · Speaker 2

of y given x let's say a classifier imposes a distribution

### 00:30:25 · Speaker 2

on labels, right? That is what it does. And the

### 00:30:30 · Speaker 2

true label distribution that is what you can show. Okay? uh I mean if you use a cross entropy kind of loss then the scaled divergence is equivalent to that cross entropy. I mean that is easy to show. Okay?

### 00:30:45 · Speaker 2

the interesting result that which is shown is

### 00:30:49 · Speaker 2

Now suppose

### 00:30:53 · Speaker 2

Arts

### 00:30:54 · Speaker 0

star represents the generalization risk

### 00:31:03 · Speaker 0

it's also called the true risk

### 00:31:10 · Speaker 0

which is nothing but uh the error, average error on unseen data.

### 00:31:24 · Speaker 0

average error on unseen data.

### 00:31:30 · Speaker 1

What can be shown is that R star

### 00:31:36 · Speaker 1

will be lower

### 00:31:40 · Speaker 1

for

### 00:31:41 · Speaker 1

R B cap, okay? Compared to

### 00:31:48 · Speaker 1

R cap. So this is a this is actually

### 00:31:50 · Speaker 2

actually the main result

### 00:31:54 · Speaker 2

which is there in that paper which uses Jensen's inequality, okay? to bound the variance of these two risks.

### 00:32:02 · Speaker 2

Yeah, but this is the crux of the result that would say that the generalization error that we get

### 00:32:11 · Speaker 2

The generalization uh error that is achieved using base distilled risk is lesser compared to that of the uh

### 00:32:22 · Speaker 2

risk that is obtained using the direct delta approximation.

### 00:32:26 · Speaker 2

Okay

### 00:32:27 · Speaker 1

which means what does this imply summary is

### 00:32:37 · Speaker 0

it is better

### 00:32:41 · Speaker 0

Two

### 00:32:43 · Speaker 0

Use

### 00:32:48 · Speaker 1

based still risk or

### 00:32:51 · Speaker 1

the distribution actual distribution over the labels given data. Okay. Instead of

### 00:33:03 · Speaker 0

instead of

### 00:33:05 · Speaker 0

Delta approximated labels

### 00:33:17 · Speaker 1

So this is the

### 00:33:18 · Speaker 2

idea. Okay, so now, uh, this paper says that now see if you incorporate the, I mean, that is why this thing P of Y given X is also called dark knowledge. That is the term that is used in the distillation literature, okay? If you incorporate the dark knowledge that is there, uh, in the labeling or uncertainty that is there in the labeling, you achieve a better generalization performance is the idea.

### 00:33:44 · Speaker 2

Now, uh, this is not directly related to connected to distillation yet, okay? Now this, now the question is,

### 00:33:54 · Speaker 2

Given

### 00:33:55 · Speaker 0

a labeling, a deterministic labeling scheme

### 00:34:10 · Speaker 0

a scheme, there is no access

### 00:34:17 · Speaker 2

access to P of Y given X, isn't it? I mean, we are only given deterministic labels. How do we know what is the distribution of the labels conditioned on data? We don't know that, okay? Therefore, the idea is...

### 00:34:36 · Speaker 0

the

### 00:34:38 · Speaker 0

Idea is to

### 00:34:43 · Speaker 0

Approximate

### 00:34:47 · Speaker 0

P of Y given X, okay? As

### 00:34:51 · Speaker 1

or rather

### 00:34:54 · Speaker 1

using a neural network.

### 00:34:57 · Speaker 1

So this neural network is the

### 00:34:59 · Speaker 2

Neural Network

### 00:35:01 · Speaker 2

Right? So now what happens is in fact, uh this theory, right? It does not talk about the size reduction at all. So it suggests what is called as self distillation. I'll talk about it. So there is this network F theta, you get X and Y. It is trained in a supervised way with deterministic label, okay?

### 00:35:22 · Speaker 2

supervised using

### 00:35:28 · Speaker 2

deterministic labels. However, the pre-softmax

### 00:35:34 · Speaker 1

activations that you get

### 00:35:36 · Speaker 1

the logits that you get. These

### 00:35:41 · Speaker 1

can be interpreted

### 00:35:42 · Speaker 0

retired

### 00:35:47 · Speaker 1

as

### 00:35:50 · Speaker 0

in approximation

### 00:35:53 · Speaker 2

Two

### 00:35:55 · Speaker 2

p of y given x. So this is an approximation to p of y given x. So then what you do is you take the you take another network.

### 00:36:06 · Speaker 2

We don't talk about sizes here, right? I mean, it can be the same size or different size. If it's of the same size, then it is typically called the self-dissolution, okay?

### 00:36:20 · Speaker 2

take that and use R B star here to train this. So now R B is the base distal risk is simply the KL divergence between the uh true or rather the

### 00:36:36 · Speaker 2

models

### 00:36:40 · Speaker 2

estimate of y given x, okay? And the true y given x. So now we don't have access to true y given x, so we use the teacher's F theta's logits as an approximation to this. Now, when somebody asked the question, right, we can why why do we have a supervised loss? So if we

### 00:37:01 · Speaker 2

if we have a perfect uh uh

### 00:37:06 · Speaker 2

estimation of P of Y given X then we do not need supervised loss. Now since we are approximating the true uncertainty label uncertainty using another neural network that is trained using deterministic labels. So it can only do so so much right so that is why you also have a supervised loss here. Okay. To ensure that the network the distilled network also does well on the supervised training.

### 00:37:34 · Speaker 2

As I said, no, in this treatment, there is no reference to making this SP a smaller network. No, that becomes a a byproduct, right? Or happy consequence of this that okay, there's no restriction on how big or large this SP network should be because as long as you are matching the the true label uncertainty, you should get better risk irrespective of the

### 00:38:01 · Speaker 2

the network size and that is why people tried okay let's try to make this S P a smaller network and then

### 00:38:08 · Speaker 2

try to ensure so this is there is a scale here.

### 00:38:12 · Speaker 2

and try to use this technique for network compression. In fact, as as it stands, you can do what is called as self-distillation, which is that you train a neural network using supervised fashion and then take that same neural network and use the logits of the previous one and retrain it by minimizing the KL between the logits and a supervised loss.

### 00:38:35 · Speaker 2

I mean

### 00:38:37 · Speaker 2

If you have gotten P of Y given X to a fair extent from the teacher network, then doing self-dissolution should improve the generalization according to this theory. Okay?

### 00:38:49 · Speaker 2

ओके, दैट्स अबाउट इट. क्वेश्चंस, या, विवेक.

### 00:38:53 · Speaker 4

So the so we you told about the base distilled laws. Yeah. But instead of using that so if we just use the entropy of the pre-decision layer output, I mean if we try to

### 00:38:59 · Speaker 2

Yeah

### 00:39:13 · Speaker 4

minimize the entropy. Will that lead to any benefit?

### 00:39:18 · Speaker 2

that's same as this, isn't it?

### 00:39:23 · Speaker 4

that's what it should be less indecisive. uh that in that that way the entropy will reduce.

### 00:39:26 · Speaker 2

Yeah

### 00:39:32 · Speaker 2

Yeah

### 00:39:32 · Speaker 4

Yeah, so okay.

### 00:39:35 · Speaker 2

It's it's very uh in fact it's not the absolute entropy it becomes I mean what we are suggesting is to minimize the cross entropy here.

### 00:39:43 · Speaker 4

cross entropy okay between the teacher and the student

### 00:39:46 · Speaker 2

Correct. Correct.

### 00:39:47 · Speaker 4

Okay

### 00:39:49 · Speaker 2

I mean it's actually not the teacher, it should be the true distribution, the true posterior of labels given data, that is what it should be. Now because we don't have access to that given hard labels, we will try another neural network and use its logits as an approximate for that, that is the idea.

### 00:40:08 · Speaker 0

Oh ho okay

### 00:40:10 · Speaker 2

Yeah

### 00:40:11 · Speaker 0

Okay sir

### 00:40:12 · Speaker 1

Okay. Yeah. Any other question?

### 00:40:22 · Speaker 1

Harish

### 00:40:24 · Speaker 0

Sir, if the student network, the size of the student

### 00:40:27 · Speaker 3

network is not so small it's almost same same to the teacher network then what is the benefit of doing this because we can directly do the yeah I told you

### 00:40:36 · Speaker 2

Yeah, I told you, you know, it is improved, improved, improved generalization, you know, it will do much better on test data, unseen data.

### 00:40:44 · Speaker 2

Because now you are not training this neural network just using hard labels, but you are training it using, I mean you are incorporating the uncertainty also that is there in the labeling.

### 00:40:55 · Speaker 1

Got it. Thank you.

### 00:40:59 · Speaker 2

Sanjit

### 00:41:01 · Speaker 3

Sir, uh the for the supervised loss, we will be taking up the true labels Y and the approximated labels from the S S five network, right?

### 00:41:16 · Speaker 2

Of course, yeah.

### 00:41:21 · Speaker 2

you're saying why why you are doing supervised training for the student network you're saying, yeah?

### 00:41:26 · Speaker 3

No, no, no, I'm

### 00:41:28 · Speaker 3

I'm trying to understand like

### 00:41:32 · Speaker 3

with what are we comparing? Are we comparing it from the uh labels generated from F theta network or from the S V network?

### 00:41:42 · Speaker 2

true labels. Here the supervised loss is losses with these true labels. The output of the S V network and the true labels.

### 00:41:52 · Speaker 2

That's what the loss is between.

### 00:41:56 · Speaker 3

Okay

### 00:41:59 · Speaker 3

and this F theta network, uh so this can be any network, right? It need it need not be trained, just that we need a representation uh for...

### 00:42:09 · Speaker 2

Well if it's not if it's not trained then how do you expect it to give the actual P of Y given its

### 00:42:18 · Speaker 1

Okay

### 00:42:19 · Speaker 2

should be trained. should be trained in a supervised way. Yeah.

### 00:42:24 · Speaker 2

Okay, so that's about it and yeah, this is how you implement it in your assignment, right? I have not asked you to do self distillation, I have asked you to reduce the network size and do a distillation on reduced network size itself, right? So yeah, please do that. And also read this paper, okay? This is called a statistical perspective on knowledge distillation. I think I'll tell you the authors also, specifically.

### 00:42:52 · Speaker 0

It is

### 00:42:54 · Speaker 0

cool

### 00:43:02 · Speaker 0

one

### 00:43:06 · Speaker 0

destination.

### 00:43:19 · Speaker 0

better to

### 00:43:25 · Speaker 0

share the link, no, let me do it.

### 00:44:20 · Speaker 0

Do you see my screen?

### 00:44:27 · Speaker 1

Hello

### 00:44:30 · Speaker 0

Yes sir

### 00:44:31 · Speaker 1

so it will be

### 00:44:33 · Speaker 1

S

### 00:44:33 · Speaker 2

see my screen right so this is that paper so here what they do is the following right yeah so they call this as what yeah this p t of x is what they call as what they called as the teacher class probability estimates or the

### 00:44:52 · Speaker 2

true label posterior. Okay. So where P T of Y given X estimates how likely X is to be classified as Y.

### 00:45:00 · Speaker 2

Now these are used by a student model which replaces empirical risk, which is the standard empirical risk with the distilled risk. This is what they call R tilda is what they call as the distilled risk. Okay. Then the question is why does distillation help? Okay. So they compute this thing called base distilled risk and this is the main result which I just said that if you take any bounded loss then the generalization error that we get with the base distilled risk is much less.

### 00:45:30 · Speaker 2

compared to the tough non-distilled risk that is the result okay so I suggested you read this paper it's a nice paper and this the proof that they used to show that is also not very difficult it is simply using the definitions of variance and using the Jensen's inequality that's all it is have a look please

### 00:45:51 · Speaker 2

Okay

### 00:45:53 · Speaker 2

It's a board solution

### 00:45:55 · Speaker 1

Do you need a five minutes break, ten minutes break before we go to sequence modeling?

### 00:46:06 · Speaker 1

Hello, am I audible?

### 00:46:08 · Speaker 0

Yes sir

### 00:46:11 · Speaker 1

shall we shall we get back

### 00:46:12 · Speaker 2

after the break

### 00:46:13 · Speaker 0

Yes

### 00:46:15 · Speaker 2

Yeah, so this is

### 00:46:18 · Speaker 2

ओके, सो लेट्स कम बैक एट लवेन एएम मेबी, जस्ट टेक सम फिफ्टीन मिनट्स ब्रेक।

### 00:46:22 · Speaker 0

Yes

### 00:46:23 · Speaker 1

ओके या सी यू बाय बाय

### 00:46:25 · Speaker 0

Thanks boss

### 01:05:07 · Speaker 6

Hello

### 01:05:10 · Speaker 6

Shall we continue?

### 01:05:16 · Speaker 6

Yes sir

### 01:05:18 · Speaker 4

Let me just share my screen.

### 01:05:26 · Speaker 5

Yeah, Vivek, you have a question?

### 01:05:29 · Speaker 3

Yes sir, so I was just seeing the paper. So what is temperature scaling?

### 01:05:34 · Speaker 5

Oh yeah yeah so that is like I think it was you or somebody else who talked about the weighting of those two losses no?

### 01:05:43 · Speaker 3

Okay, yes

### 01:05:44 · Speaker 5

the supervised and the KL losses.

### 01:05:48 · Speaker 3

Okay

### 01:05:48 · Speaker 5

That is what is referred to as temperature scaling. How much weight do you have to give for each of them?

### 01:05:52 · Speaker 3

Okay okay okay

### 01:05:56 · Speaker 3

Okay sir, so okay, so what is a well calibrated model? So what can we do to what how should the temperature be scaled?

### 01:06:05 · Speaker 5

That's a hyperparameter. Sorry, sorry.

### 01:06:07 · Speaker 3

Okay, so should we learn that hyperparameter or should

### 01:06:10 · Speaker 5

or

### 01:06:12 · Speaker 5

Yeah, see, uh just like with any other uh loss functions, right? I mean, uh where you have two, two or more components and you need to decide the weights, either you can do it using hyperparameter tuning or you can learn it. In fact, I have a paper sometime back, one year, two years back where we cast as a meta learning problem and learn both the weights, loss weights and the losses together. All that is again, uh

### 01:06:42 · Speaker 5

level up but yeah so typically it is trained as a hyperparameter either you learn it or keep it I mean fix it based on validation data

### 01:06:52 · Speaker 3

Okay, okay.

### 01:06:54 · Speaker 5

Yeah. So can we can

### 01:06:55 · Speaker 3

So can we can we have a link to that paper if you don't mind? I mean later on

### 01:06:58 · Speaker 5

I shared it, no? I actually shared it.

### 01:07:00 · Speaker 3

Occupation

### 01:07:01 · Speaker 5

Okay, it's the same

### 01:07:02 · Speaker 3

Okay, it's the same paper. Okay.

### 01:07:04 · Speaker 5

So you mean my paper you're saying?

### 01:07:05 · Speaker 4

Yeah

### 01:07:06 · Speaker 3

Yeah

### 01:07:08 · Speaker 6

Hold on

### 01:07:21 · Speaker 6

KLM KD

### 01:07:40 · Speaker 6

the paper. I'm getting the link.

### 01:08:05 · Speaker 6

maybe you can

### 01:08:06 · Speaker 3

share the name and the title

### 01:08:08 · Speaker 5

title is there but I myself should find my paper no where is the

### 01:08:14 · Speaker 5

is published in triple A I bet where is the link for it?

### 01:08:17 · Speaker 6

Hello

### 01:08:22 · Speaker 6

Second

### 01:08:35 · Speaker 6

Hmm

### 01:08:42 · Speaker 6

Hmm

### 01:08:48 · Speaker 6

surprising that I can't spot the link.

### 01:08:56 · Speaker 6

finally I got it

### 01:09:08 · Speaker 6

Yeah, I just put it in the chat window.

### 01:09:10 · Speaker 5

So what we do is that wherever you have these kinds of settings right where you have like two losses and you need to in fact one of the applications is knowledge resolution if you look at section four of the paper we actually learn that temperature

### 01:09:25 · Speaker 3

Okay

### 01:09:29 · Speaker 3

Okay, okay, okay. Knowledge distillation, you know. So two applications in a way. Okay.

### 01:09:35 · Speaker 5

If you look at equation nine, ten and all that, we actually learn that and show that like there is an optimal value. We do it using the this thing.

### 01:09:47 · Speaker 5

metal only. That is what the paper is about. But generally that is not done, you know, you are it is taken as a hyperparameter and used valid fixed based on validation data. Okay.

### 01:09:59 · Speaker 3

ओके, ओके, जस्ट थ्रू सम सैंपल वैल्यूज एंड व्हाट इज गिविंग द गुड रिसर्ट। ओके, वैलिडेशन डेटा।

### 01:10:05 · Speaker 5

Validation data

### 01:10:09 · Speaker 3

Okay sir. Thank you.

### 01:10:14 · Speaker 5

Okay, let's move on.

### 01:10:16 · Speaker 5

ನೋಡಿ ಫೈನಲ್

### 01:10:17 · Speaker 6

piece that we will talk about is the

### 01:10:21 · Speaker 6

sequence modeling

### 01:10:36 · Speaker 6

data in this case

### 01:10:40 · Speaker 6

will

### 01:10:44 · Speaker 6

every data point, okay, is

### 01:10:48 · Speaker 6

is a sequence.

### 01:10:59 · Speaker 6

Okay, data point

### 01:11:00 · Speaker 4

is a sequence. So what do you what do you mean by a sequence? Let's say that x is one data point. So one data point itself will have

### 01:11:12 · Speaker 6

superscript perhaps

### 01:11:19 · Speaker 6

two X T okay

### 01:11:23 · Speaker 6

where

### 01:11:25 · Speaker 5

every x j is in some d-dimensional space. Okay? This is what is called as a sequence where every data point has a

### 01:11:37 · Speaker 5

is a is a is a series of D dimensional vectors T of them. Okay? So examples of this you know that this is you have

### 01:11:49 · Speaker 5

sentence

### 01:11:53 · Speaker 6

right? is a sequence of

### 01:12:03 · Speaker 4

linguistic tokens. These tokens can be characters or words or something, right? So the other example is the speech signal.

### 01:12:15 · Speaker 6

This is a sequence of

### 01:12:25 · Speaker 6

frequency domain vectors

### 01:12:31 · Speaker 6

because

### 01:12:31 · Speaker 5

actually called the MFCC and so on, okay? So this is one thing and you have some industrial time series and you can also look at video.

### 01:12:43 · Speaker 6

as

### 01:12:44 · Speaker 6

sequence of

### 01:12:52 · Speaker 6

sequence of images.

### 01:12:56 · Speaker 6

frames

### 01:12:59 · Speaker 5

Okay? So this is a sequence, I mean this is what is called as sequence data. Now sequence modeling is is set of all those methods where the objective in sequence modeling, the objective is to solve

### 01:13:24 · Speaker 6

objective

### 01:13:28 · Speaker 6

is to solve either

### 01:13:34 · Speaker 6

discriminative or generative

### 01:13:37 · Speaker 6

priminative

### 01:13:43 · Speaker 6

or generative problems on sequences.

### 01:13:54 · Speaker 6

on sequences.

### 01:13:59 · Speaker 6

Okay, so now

### 01:13:59 · Speaker 5

Now there you have examples of these problems. So examples can be of course we have machine translation.

### 01:14:14 · Speaker 5

where you have a sequence in right a sequence in one language

### 01:14:19 · Speaker 5

sequence in English and what comes out is a sequence in in in Hindi let's say. Right so this is one example. The other example can be

### 01:14:30 · Speaker 6

uh

### 01:14:37 · Speaker 6

a summarization

### 01:14:44 · Speaker 6

right? You have video classification.

### 01:14:52 · Speaker 4

spam detection and so on, right? I mean you can think of any number of problems that we have that that you can encounter.

### 01:15:07 · Speaker 4

within sequences, okay?

### 01:15:08 · Speaker 5

So now how do you deal with this kind of sequential data is a question that people have been asking for a long time now

### 01:15:19 · Speaker 5

Now I'll just give you broad history of how things were happening and then uh then we'll move on to what the current state of the art is.

### 01:15:35 · Speaker 6

history of

### 01:15:39 · Speaker 6

of sequence models.

### 01:15:47 · Speaker 4

very early days, right? people were using models such as auto regressive models or AR models.

### 01:16:03 · Speaker 4

where the idea was the following. So you have to model X T, right? So X T was modeled as simply a linear combination of

### 01:16:25 · Speaker 6

one to or rather let's say T minus K

### 01:16:28 · Speaker 5

K2T

### 01:16:30 · Speaker 6

music

### 01:16:31 · Speaker 5

Okay, so this is an auto regressive model where you take, you model or rather you express the Tth sample, okay, so we used superscript for T, you know. The Tth vector that we have is given as a linear combination of

### 01:16:50 · Speaker 5

Hmm

### 01:16:52 · Speaker 5

I don't want to confuse you by using superscript and subscript

### 01:16:57 · Speaker 4

Okay, let us use

### 01:17:00 · Speaker 4

subscribed only

### 01:17:07 · Speaker 4

don't confuse it with

### 01:17:08 · Speaker 5

like one two three up to T data points okay in one data point itself you have T

### 01:17:16 · Speaker 5

t length sequence it is okay. So that is what the convention is. A X T is equal to

### 01:17:25 · Speaker 5

Right. So now what we are doing is,

### 01:17:28 · Speaker 6

Every

### 01:17:31 · Speaker 6

Eth

### 01:17:35 · Speaker 6

Token

### 01:17:37 · Speaker 6

in the data

### 01:17:42 · Speaker 6

is a linear combination of

### 01:17:51 · Speaker 6

a K length

### 01:17:55 · Speaker 6

Window

### 01:18:04 · Speaker 5

before it, okay? This is this is an auto regressive model name. I mean you can you can imagine why the name, right? It is it is regressing on self, okay? uh that is why it is auto regressing. So it is not using anything else. It is only saying that okay, uh I will express or rather the Tth token is expressed as a linear combination of uh previous T minus K tokens.

### 01:18:27 · Speaker 5

is also called linear prediction model

### 01:18:33 · Speaker 5

linear predictive coding

### 01:18:37 · Speaker 5

or LPC. In fact, even today this is used in telecommunications, okay, to compress speech and all that. So now the question here is how do you find these coefficients A and it is found out in a statistical way where you have a lot of data.

### 01:18:54 · Speaker 5

try to reconstruct the data back using the K previous samples and find out these coefficients and use them. In fact, what is done in speech compression is that you need to transmit speech data from one point to the other, let's say, right? The raw data is not at all transmitted. What is transmitted are these coefficients, K J, so that you can, I mean that is a compressed version of it, okay? And then you use that and

### 01:19:24 · Speaker 5

destructive data back at the decoder. That is in fact as I said you know as we are speaking, a lot of VOIP protocols and all this even today uses some variant of this linear predictive coding, okay?

### 01:19:37 · Speaker 5

But the thing is these kinds of models work with speech kind of data where there is lot of predictability but they don't uh generalize for tasks like machine translation and so on, okay? People then move to statistical models.

### 01:20:00 · Speaker 5

such as

### 01:20:01 · Speaker 4

One example was, one famous example was what is called as a hidden Markovian model or HMM.

### 01:20:15 · Speaker 4

एचएमएम बॉस

### 01:20:16 · Speaker 5

the uh the go to uh model right to model sequences uh go to choice for modeling sequences for a long time. What is the model here is that you assume that there is a there's a Markov chain.

### 01:20:33 · Speaker 5

Okay

### 01:20:35 · Speaker 4

amongst what are called as states, I'll tell you what states are

### 01:20:48 · Speaker 6

transition from here to here okay. Okay so and every state emits symbols.

### 01:21:01 · Speaker 4

And these symbols are uh XJs.

### 01:21:05 · Speaker 5

X one, X two up to X, I mean it it it's simply X J, okay? So now these are states Z. So it's actually H M M, right? is a latent variable model. It's a latent variable.

### 01:21:18 · Speaker 4

table model

### 01:21:26 · Speaker 6

where the latent variable is

### 01:21:31 · Speaker 6

Discrete Markovian

### 01:21:40 · Speaker 4

ओके

### 01:21:40 · Speaker 5

And the model is the following, right? The there is a Markovian transition between the latent variable states and at every transition, right? After every transition, the model emits an observable symbol X T, okay? This is continuous.

### 01:22:02 · Speaker 4

and modeled using neural networks, G M Ms.

### 01:22:09 · Speaker 5

the H M M the famous H M M G M M model where see basically what is happening is the following right I mean imagine the speech signal example. So the uh the uh uh motivation behind this is

### 01:22:26 · Speaker 5

this assumption that when somebody is speaking, okay, what is actually happening is that before you speak, you think of what is the phoneme that you have to emit given the uh semantic meaning that you want to convey, okay? Depending upon what uh uh phoneme that you need to emit, okay? phoneme you need to convey, uh you create some constrictions in your vocal fold and what is uh produced is a pressure diff.

### 01:22:56 · Speaker 5

Okay, when you when when we speak what happens is, you know, there is a certain pressure difference that that occurs in the environment, which is what is recorded using a microphone, a condenser microphone. So this is the observable speech signal. These are the observations.

### 01:23:15 · Speaker 5

which happens to be the speech signal itself which we measure.

### 01:23:20 · Speaker 4

Okay. So what is Markovian are the unobservable

### 01:23:28 · Speaker 4

unobservable, abstract

### 01:23:32 · Speaker 4

Onyms

### 01:23:36 · Speaker 5

Okay? So now there is a Markovian transition between them because given that you need to convey something and given that you have already said a particular type of phoneme, uh you can only choose from a, I mean there is a probability from which you can choose what phoneme to be uttered next.

### 01:23:54 · Speaker 5

Right?

### 01:23:57 · Speaker 5

Right? So that is why there is a Markovian assumption between the hidden states. And what is observed are the the measured quantity. Okay? So this is a model. And the the distribution so now basically what happens is there will be a distribution amongst the states. Okay?

### 01:24:20 · Speaker 5

which is Markovian.

### 01:24:25 · Speaker 5

and there will be a distribution over the

### 01:24:30 · Speaker 5

observations given a particular state. This is modeled as a Gaussian mixture model. This was this was actually the standard this used to be the standard modeling choice for any sequences where you say that okay, you can extend this for let's say handwriting recognition, right? Where the observations are modeled as the pen strokes or the coordinates of the pen strokes and the latent variable or the Z models, what was the the what is the the letters or rather the symbol that is to be conveyed, okay?

### 01:25:08 · Speaker 5

And if you want to uh model speech as I said there are phonemes and every phoneme emits a symbol which is a speech signal and so on. Okay so now what has to what are to be learned the so this is parameterized by some theta this is parameterized by from phi. Uh theta and phi are

### 01:25:29 · Speaker 5

are learned

### 01:25:32 · Speaker 5

using the EM algorithm. So we have seen the EM algorithm, right, in the very beginning classes. So EM algorithm is used.

### 01:25:41 · Speaker 5

learn this. Okay? So this is how uh initially the uh sequence model models were being uh learned. So if anybody wants to learn more about H M M's, right? Uh there is one very nice tutorial by Lawrence Rabiner.

### 01:25:59 · Speaker 5

have a look at it where he formulates the problem and write down the likelihood log likelihood for H M M and works out the E M. So basically it is working out the E M, okay? H M M tutorial.

### 01:26:16 · Speaker 6

Okay

### 01:26:18 · Speaker 6

Any questions so far on this?

### 01:26:34 · Speaker 6

So but in this

### 01:26:35 · Speaker 3

this Marco model, are we actually passing the, is it dependent on the past? I mean...

### 01:26:41 · Speaker 5

It is no it is. Because it is Markovin yeah.

### 01:26:43 · Speaker 3

Okay

### 01:26:47 · Speaker 3

Right

### 01:26:55 · Speaker 4

Okay

### 01:26:56 · Speaker 1

Sir, just to know, I mean, you said when we say a sentence, right? We say one word and the word is basically, we can predict whatever is the next word kind of, right? I mean...

### 01:27:01 · Speaker 5

one word

### 01:27:08 · Speaker 5

not predict there is a probability over what the next word is going to be that is reasonable

### 01:27:09 · Speaker 1

predict

### 01:27:14 · Speaker 5

Because if you are, yeah, because in a given language, given that you have uttered one word, there's a certain probability of what the next word is going to be.

### 01:27:14 · Speaker 1

if you are

### 01:27:23 · Speaker 1

But for Marko, it just depends on the previous word alone, right?

### 01:27:26 · Speaker 5

I mean it depends on what order of the Markovian assumption that you are making. You can make it a first order Markov, second order Markov, third order Markov, anything.

### 01:27:36 · Speaker 5

called an N-gram model, right? You can make it a unigram, bigram, trigram, anything, right? So it is not one word always. In diffusion models, we assumed it to be a first-order Markov process, but it need not be first order. Typically, it is taken to be a third or fourth-order Markov process when it comes to sweet signals.

### 01:27:56 · Speaker 4

Sure. Thank you.

### 01:27:57 · Speaker 5

Okay, so as I said, right? I mean, HMM is sort of obsolete now, like it's not the go-to choice. So then came the revolution of neural networks, right? This was in this was nineteen early nineties and so on. This AR models, right? Auto regressive models, they date back to like early nineties, twentieth century. And then nineteen eighties and nineties, people started looking at hidden Markovian models and other statistical models, similar statistical models and when the when neural network started taking off right so came the recur

### 01:28:35 · Speaker 6

different neural networks

### 01:28:47 · Speaker 6

known as RNNs.

### 01:28:53 · Speaker 5

I think if there is one more tutorial, right? uh you can ask Chandan to talk more about RNNs and BPTT. I will just give you an overview. So the the idea in recurrent neural network is that what you have is that you build a

### 01:29:10 · Speaker 5

Okay, so let me before that, see what happens in a

### 01:29:15 · Speaker 4

in a sequence kind of data is

### 01:29:17 · Speaker 4

every data point

### 01:29:26 · Speaker 6

will have

### 01:29:28 · Speaker 6

different length

### 01:29:37 · Speaker 6

Right? Because

### 01:29:39 · Speaker 5

Imagine that we are looking at

### 01:29:42 · Speaker 5

sentences, if you're looking at natural language sentences,

### 01:29:46 · Speaker 5

then each of the uh sentence will have a different length, you know, obviously. So now if you take a fully connected neural network or an MLP, it is difficult to handle uh data with different lengths. So now how do you handle this is the question. So now the one answer is to use what is called as recurrent neural networks. The idea is the following that

### 01:30:09 · Speaker 5

to handle this

### 01:30:13 · Speaker 6

equal equal

### 01:30:17 · Speaker 6

non equal

### 01:30:20 · Speaker 6

input lens

### 01:30:25 · Speaker 6

what you do is share the parameters across time

### 01:30:40 · Speaker 6

what is meant by this? But this is the architecture of a fairbone

### 01:30:52 · Speaker 4

recurrent neural network

### 01:30:57 · Speaker 5

say that you have X P here that is the Tth length and you have the corresponding Y T because it's a sequence in sequence out model. Now you have the T minus first hidden state. You have the Tth hidden state going out okay. This is one R N N

### 01:31:18 · Speaker 5

R N N block or R N N cell.

### 01:31:24 · Speaker 5

Okay. Now you have parameters that are let's say U, V and W.

### 01:31:35 · Speaker 5

Okay. Now, the relationship between the parameters are given by this that you have Y T

### 01:31:45 · Speaker 5

is equal to sigma of W times

### 01:31:50 · Speaker 4

H T minus one

### 01:31:53 · Speaker 4

plus

### 01:31:56 · Speaker 4

uh is a

### 01:32:00 · Speaker 5

xt is coming no? into u times or v times xt

### 01:32:07 · Speaker 5

and the next state, next hidden state is given.

### 01:32:11 · Speaker 6

Bye

### 01:32:13 · Speaker 6

Hello

### 01:32:20 · Speaker 4

right what I am writing no v times that is yeah

### 01:32:25 · Speaker 6

U 1060, right? Yeah, yeah. 1060.

### 01:32:26 · Speaker 4

Yeah yeah

### 01:32:27 · Speaker 4

U times X T

### 01:32:34 · Speaker 4

plus

### 01:32:36 · Speaker 4

W tan 60 minus 1

### 01:32:38 · Speaker 5

Yeah

### 01:32:38 · Speaker 4

Hello

### 01:32:40 · Speaker 4

Yeah

### 01:32:40 · Speaker 5

So this is one RNN cell. So now what you do is that you get

### 01:32:48 · Speaker 5

Have you seen an R N N picture right where people write this kind of a thing?

### 01:32:55 · Speaker 5

okay? So, and and then they write something called unrolling of R N N. So what that means is that you repeat this. So now if you have a sequence of let's say length T

### 01:33:07 · Speaker 6

E

### 01:33:20 · Speaker 6

it's it's zero.

### 01:33:24 · Speaker 6

There is X1 here

### 01:33:26 · Speaker 5

Let's do here.

### 01:33:28 · Speaker 5

see here. And you have H one, H two.

### 01:33:33 · Speaker 5

age

### 01:33:36 · Speaker 5

T and Y one two. IT observe that everywhere so you have the same U W and V exact same parameters everywhere.

### 01:33:50 · Speaker 5

So this is what is called

### 01:33:52 · Speaker 6

bus

### 01:33:52 · Speaker 6

parameter sharing across time

### 01:34:05 · Speaker 4

सर इन द इक्वेशन फॉर वाईटी

### 01:34:07 · Speaker 6

Hello

### 01:34:08 · Speaker 4

shouldn't

### 01:34:09 · Speaker 3

XT be multiplied with U

### 01:34:13 · Speaker 5

xt b multiplied with u. See the the way I have written is that you take xt here multiply it with v and then get yt and you take xt but I can write u here perhaps. This is better no? I'll write it this way.

### 01:34:35 · Speaker 4

Yeah, I think this is better.

### 01:34:39 · Speaker 4

what I meant

### 01:34:41 · Speaker 4

here there is W, here there is E and here there is U.

### 01:34:49 · Speaker 4

Is it all right now?

### 01:34:55 · Speaker 6

Okay

### 01:35:00 · Speaker 4

up

### 01:35:00 · Speaker 5

See what is important is that you see that the parameters are shared across time in the sense that uh for all times, okay, X one to X T, the U V W matrices do not change. Okay? They are actually shared across time and that is how an R N N is is trained. Okay. Now, how do we uh how do we get these U V W matrices? There's an algorithm called back propagation.

### 01:35:32 · Speaker 5

back propagation through time, okay?

### 01:35:36 · Speaker 5

It's not at all difficult. I'll tell you what it is. So we know back propagation, right? Abbreviated as BPTT. We know back propagation, but here what happens is the loss is calculated between YT and XT here, right? You calculate loss between XT and YT or rather at all points. So you have a loss here at

### 01:35:55 · Speaker 5

uh x uh x five and y five and so on. So what you should do is uh all these losses right have to be back propagated this way and they should also be back propagated this way.

### 01:36:09 · Speaker 5

isn't it? So there are two directions in which it back propagates and that is why this algorithm is called back propagation through time because there is a back propagation through time also, time direction also. So you have to basically add those two losses, one across the space, one across the time. That's how an R M is tried. As I said, no, if you

### 01:36:29 · Speaker 5

you are interested in a nice articles or you can also ask TAS to run through back propagation through time but now with all the things that you have learned in this course if you just look at standard descriptions on PPT you will understand what it is okay

### 01:36:45 · Speaker 5

So this was being used. Then what happened is, uh

### 01:36:53 · Speaker 5

there was this

### 01:36:57 · Speaker 5

This is okay if you want to solve a supervised learning problem where you have uh input and output lengths, okay, equal. I mean, you can have different input lengths, different sequence lengths at the input, but the output lengths have to be different. So but a problem like machine translation...

### 01:37:20 · Speaker 6

where both the input and output lines are different.

### 01:37:20 · Speaker 4

Sagan

### 01:37:42 · Speaker 6

You can't use one standard alone.

### 01:37:44 · Speaker 5

standalone R N N, okay? What is done is the following. So you have an R N N.

### 01:37:50 · Speaker 5

And by the way, uh what I just showed you is a naive R N N, okay? And there are improvisations over it uh by using things like L S T M's, long short term memory networks, which are which are different ways of writing these two equations, okay? So to avoid this problem called uh

### 01:38:10 · Speaker 5

vanishing gradient. So what happens is when you do back propagation through time because there is parameter sharing across time, we will multiply the same WUV matrices multiple times with each other and if the the length of the sequence is too large, then the eigen values of that will will will reduce over time and the gradients will have very less values. That is in in in a nutshell what is called as the vanishing gradient problem and you modify these equations so that

### 01:38:40 · Speaker 5

there is a skip connection sort of thing that is used in resonance so that the gradients will not vanish. And also what is done is there is no like this is only one layer RNA that I showed you what can be done is you can have multiple hidden states like this okay and you have multiple matrices across the space also okay. Those are all improvisation that I don't talk about. Here what is done in in in cases where the input and

### 01:39:06 · Speaker 5

output both of them have different lengths is the following that you use a typical encoder decoder sort of model where

### 01:39:17 · Speaker 5

you have x zero to x t, okay? we have h t here. you take another

### 01:39:26 · Speaker 5

or a sequence. Where you take H T and output Y one, okay?

### 01:39:34 · Speaker 5

and you take Y one and give it as an input to the next unit and give get your Y two and take Y two and give it as an input to this and get Y three and keep doing this till you get the last symbol emitted which is

### 01:39:53 · Speaker 5

Y M. So typically how it is done in in okay let's not call it Y M. So that is X T this is

### 01:40:06 · Speaker 5

Y S, okay? Typically how it is done is that there is a special symbol called end of sequence symbol, okay, which is one of the tokens that is used. Now you keep emitting or you keep generating till you get the end of sequence symbol and once you see the end of sequence symbol, just stop it there, okay? That is how the the translation or decoding is done. So this is the decoding network.

### 01:40:33 · Speaker 4

Sir you are not audible at least to me.

### 01:40:37 · Speaker 5

Is that so? Hello?

### 01:40:39 · Speaker 6

another

### 01:40:39 · Speaker 3

You are audible for us for me.

### 01:40:43 · Speaker 5

Okay. So this is the uh

### 01:40:46 · Speaker 5

input language

### 01:40:49 · Speaker 5

sentence in input language, this is the translated output.

### 01:40:56 · Speaker 5

Yeah. So this is the typical encoding decoding model uh using uh uh RNN kind of architectures and this was actually in the state of the art till uh let's say twenty twenty fourteen twenty fifteen times, okay? Uh with some form or the other of it which is an improvisation over this is what was being

### 01:41:18 · Speaker 4

Any questions so far?

### 01:41:26 · Speaker 6

Yes sir, just one query.

### 01:41:28 · Speaker 4

Yeah

### 01:41:29 · Speaker 0

you said we don't send the speech initially, we send the symbols, right? And then the

### 01:41:35 · Speaker 5

No, no, this is, this is, this is text translation, no? This is machine translation task.

### 01:41:41 · Speaker 0

No, no, that's fine, but before this,

### 01:41:43 · Speaker 5

Okay

### 01:41:44 · Speaker 0

you said symbols are transmitted not speech and speech is regenerated right?

### 01:41:49 · Speaker 5

you mean for telephony right long distance telephony and all that yes that is true

### 01:41:54 · Speaker 0

and how voice can be transmitted actually or how it will recognize like if I speak how the generated signal will match my voice.

### 01:42:05 · Speaker 5

Okay. uh yeah, that's a good question. See what is done is uh the LPC model, right? One, there is content. There is another thing which is your signature, which is that no matter what you speak, there is a particular source signal that that mimics your voice, that is your signature, okay? Even that is transmitted. And that does not require a lot more bits. I mean, that will go to speech speech processing theory. So, two things are transmitted. One, the

### 01:42:35 · Speaker 5

part of it. The other is your voice signature. Think of it like that. So it's like given your voice, I can overlay any of the symbol, any of the phoneme that I want on your particular voice. That's the idea.

### 01:42:48 · Speaker 0

Okay. And for this text thing, the words can be in different sequence when transmitted into translated into different language.

### 01:43:01 · Speaker 5

No, no, no. Words, no, words will be of different length, I said.

### 01:43:06 · Speaker 0

No length is fine but one language may have a different order of words if their literal meaning is taken then it will not make sense like in different language it will be a different sequence of words.

### 01:43:20 · Speaker 5

Now words themselves will be very different, right?

### 01:43:24 · Speaker 0

Yeah, and their sequence will also be different, right?

### 01:43:27 · Speaker 5

See when words themselves change how would the sequence matter? Of course sequence will be different so

### 01:43:33 · Speaker 0

how that is learned while predicting

### 01:43:37 · Speaker 5

Yeah, see that is why uh what you predict is given the previous word that you have uh out I mean you have given as output, the next word is predicted. That is conditioned on the previous word, no? Now you can see here that the output

### 01:43:53 · Speaker 5

right? y two depends on the previous word y one. So if you have enough data, the hope is that the model would see all those combinations implicitly.

### 01:44:06 · Speaker 0

Okay, but first it will be a direct

### 01:44:07 · Speaker 5

But first condition done. Condition ah see now the question is I mean how would the first word be uh predicted right? The first word would be predicted based on the input sequence.

### 01:44:21 · Speaker 5

And what the input sequence information goes to the the output RNN through this last hidden state HT. So it's like you encode the input sequence in this hidden state HT and that goes as an input to the decoder. Okay? And decoder gives you the first word and based on the first word and the hidden representation there is also one other hidden representation here no for the

### 01:44:47 · Speaker 5

or the decoder also based on that the next words are predicted one by one.

### 01:44:52 · Speaker 0

Okay, and is it trained on some kind of literature or

### 01:44:55 · Speaker 5

pairs pairs pairs they are trained on pairs of sentences from languages. So you have to have a lot of pairs of English and Hindi sentences. And given a pair of English and Hindi sentence it will be trained that way. It's always trained on pairs.

### 01:45:09 · Speaker 0

but

### 01:45:12 · Speaker 0

pairs you are saying

### 01:45:13 · Speaker 5

Pairs, P A I R S

### 01:45:16 · Speaker 6

Let me write down.

### 01:45:17 · Speaker 4

Okay

### 01:45:50 · Speaker 4

Does it make sense?

### 01:45:52 · Speaker 0

Yeah, so even if it's trained on pairs of sentences, it will not kind of do V lookup, right? It will just try to generate each word separately.

### 01:46:00 · Speaker 5

correct. One word after one word after the other, give condition on the previous word.

### 01:46:06 · Speaker 0

Okay

### 01:46:10 · Speaker 0

Thanks

### 01:46:10 · Speaker 5

ओके, या, थैंक्स। विवेक?

### 01:46:12 · Speaker 3

So after the encoding process is over we just have a single vector right?

### 01:46:17 · Speaker 5

Exactly. That's an issue.

### 01:46:20 · Speaker 3

Yeah, so that's exactly I wanted to know. It's hard to believe that one small vector can

### 01:46:25 · Speaker 5

Yeah, it's a you point exactly that was actually an issue and that is why I'll just hold on to that question that would be my next narrative.

### 01:46:25 · Speaker 3

Yeah, it's a U point

### 01:46:31 · Speaker 3

2 into

### 01:46:33 · Speaker 3

Okay, Okay, Thanks.

### 01:46:33 · Speaker 5

Okay

### 01:46:34 · Speaker 5

I'm actually building up to Transformers so that I'll tell you why that is an issue and how people solved it. Okay. Santosh.

### 01:46:44 · Speaker 2

Yes sir. So the number of R N N cells will be equivalent to the input sequence in the first layer. Correct.

### 01:46:52 · Speaker 5

Correct. Correct. Correct. See that is because it is it is the parameters are shared across time. You are just repeating the same R N N cell one after the other with a different input and the hidden layer that's all. But the weights remain the same across time.

### 01:47:10 · Speaker 2

Okay. Also my second question is that right now we have only two layers. If we have multiple R N N layers, so the final hidden state of first layer will be passed to the second layer and then like that. So the output will be passed to next layer.

### 01:47:25 · Speaker 5

there will be two things right if you have like two layer thing there will be one that goes like this one that goes like this

### 01:47:32 · Speaker 2

Hello

### 01:47:33 · Speaker 5

Yeah. You can have any number of RNA layers one after the other. Any number of hidden layers one after the other. You can make it deep.

### 01:47:42 · Speaker 2

ओके ओके या

### 01:47:44 · Speaker 5

Yeah

### 01:47:47 · Speaker 5

Yes, I said in the beginning of the course, right? I, uh, like this is not a course where I teach NLP fundamentals and architectures. Right? So, I mean, one can actually teach a full course on sequence modeling and how RNNs work and a lot of nuances there, but as I said, this course is more on, uh, like you, now you know what this course is, almost coming at the end of it. But yeah, so an overview of RNNs are like this. Any other question on this?

### 01:48:18 · Speaker 5

If not, let's move. So as this was, as I said, no, this was the the state of the art till

### 01:48:28 · Speaker 5

or machine translation, okay? Like till let's say like twenty tens, okay, twenty tens. This is what was being done and since this is not as as you can imagine, right, as Vivek was said, was saying, there's only one hidden state that has to compress all the information regarding the input sentence, it was not doing great and that's why machine translation was not available commercially at large scale beyond academic labs. Right? So then came this nice idea which I'll tell you

### 01:49:05 · Speaker 6

this is x one, this is x t and you have

### 01:49:16 · Speaker 6

five one by two

### 01:49:21 · Speaker 6

Hmm

### 01:49:26 · Speaker 6

Up to I

### 01:49:27 · Speaker 4

what did we call S, okay?

### 01:49:31 · Speaker 5

somebody thought that okay why you only have one

### 01:49:38 · Speaker 5

hidden representation compress all the information that is regarding that that that that I mean regarding the entire input sentence. So can't we do something else? So this is like that hierarchical V I E idea. So somebody said okay we'll do this that we will take the

### 01:49:56 · Speaker 5

This is the uh first hidden representation. This is the second hidden representation. Hidden representation corresponding to X-ray and all that. So what is done is that you take, you have

### 01:50:10 · Speaker 5

take all of these

### 01:50:13 · Speaker 5

take a linear combination of all of these

### 01:50:16 · Speaker 6

So let me write it neatly.

### 01:50:22 · Speaker 6

Compute

### 01:50:25 · Speaker 6

A J

### 01:50:32 · Speaker 6

H J

### 01:50:33 · Speaker 5

Okay.

### 01:50:36 · Speaker 5

H one, H two, H three and H T and compute this and give this, let's call this

### 01:50:44 · Speaker 5

Egg Yeath Car

### 01:50:46 · Speaker 4

Okay

### 01:50:54 · Speaker 4

rating cap, okay? And give this as an input.

### 01:50:58 · Speaker 5

two

### 01:51:01 · Speaker 5

State

### 01:51:03 · Speaker 5

Okay and have as many A T so there is A one. there is A two you have another this thing which is let's call this as

### 01:51:16 · Speaker 4

A one

### 01:51:23 · Speaker 4

This is AJ2HJ

### 01:51:27 · Speaker 4

F A three cap

### 01:51:29 · Speaker 5

and so on, okay? And give all of these as inputs to

### 01:51:38 · Speaker 5

the corresponding the output sequences.

### 01:51:42 · Speaker 5

Does it make sense? So what we are actually saying is, take a linear combination, okay, and here the A's are also learnt, okay?

### 01:51:59 · Speaker 4

Do you understand what is happening?

### 01:52:02 · Speaker 5

you know instead of making one hidden layer have all the information and compress and then decode. saying I will take I will tap the the the hidden representations from each of the time steps from the encoder side. take a learnable have a learnable linear combination of that and then give it as an input while decoding.

### 01:52:26 · Speaker 5

Do you understand this?

### 01:52:29 · Speaker 2

Sir, what is A year?

### 01:52:31 · Speaker 5

A is a learnable constant

### 01:52:38 · Speaker 4

Sir, how is a

### 01:52:38 · Speaker 5

Sir, How is

### 01:52:40 · Speaker 3

AJ1 different from AJ2

### 01:52:43 · Speaker 5

they learn differently, you know.

### 01:52:46 · Speaker 3

But they are tapped from the same nodes, right?

### 01:52:46 · Speaker 5

they are tapped from the same nodes, right? Correct. But these indices are taken to be different. So here what you do is, here you only take J from like one to two and you make one to three and you you take like just cumulatively do do that.

### 01:53:06 · Speaker 4

the two

### 01:53:07 · Speaker 5

Okay

### 01:53:07 · Speaker 4

Right?

### 01:53:11 · Speaker 5

Again there are different improvisations over it but the idea is clear right? What you do is you take a linear combination of hidden layer representations and take a I mean learn the weights with which they have to be linearly combined and then give it as an input while you are decoding it. Is this idea clear?

### 01:53:31 · Speaker 2

So sir, here number of linear combinations equal to number of Y sets, I mean sequence.

### 01:53:37 · Speaker 5

number of wives. number of wives, correct.

### 01:53:44 · Speaker 5

Okay

### 01:53:45 · Speaker 5

Do you know what these this thing

### 01:53:47 · Speaker 4

This is actually what is called as attention

### 01:53:53 · Speaker 4

This is what is called as attention

### 01:53:55 · Speaker 5

okay? Like say like RNNs with attentions

### 01:54:04 · Speaker 5

is R N N with attention. Okay? What you are doing is that you take the linear combination of hidden layers and then uh take uh give that as an input to the while decoding. So this uh received a lot of attention, okay? And this gave a significant boost in terms of uh what the uh the what we could achieve using machine translation. Okay? So then came this this this thing, no, which is the

### 01:54:34 · Speaker 5

transformer architecture where they said okay see anyway you are using attentions here okay why even have an RNN cell because you end up with the problems of vanishing gradient and all that if you have very long sequence lenses lens so why not create an architecture right so come this transformer

### 01:54:58 · Speaker 6

which is

### 01:55:00 · Speaker 6

an attention only architecture without a recurrent nature structure.

### 01:55:20 · Speaker 6

Without recurrence

### 01:55:28 · Speaker 5

Yeah, that is what a transformer is all about, okay? It is an attention only architecture without recurrence.

### 01:55:35 · Speaker 5

I'll briefly talk about uh what uh attention is I mean this is transformer is okay. Now you have like input sequence X that is equal to

### 01:55:49 · Speaker 6

x one x two up to x t, right?

### 01:56:01 · Speaker 6

Okay. Now,

### 01:56:03 · Speaker 5

a transformer is some function f theta. to take each x j and gives you a corresponding z j.

### 01:56:14 · Speaker 5

Okay? So now what what does it do is given

### 01:56:20 · Speaker 4

a sequence

### 01:56:20 · Speaker 6

six

### 01:56:27 · Speaker 6

data X, okay? A transformer

### 01:56:34 · Speaker 6

outputs

### 01:56:38 · Speaker 6

a sequence of

### 01:56:43 · Speaker 4

representations or hidden layers or hidden representations I mean you don't have to call them hidden representations

### 01:56:54 · Speaker 5

Z, okay? Corresponding to each of the input token. So for every input token X I, there is a corresponding representation Z, okay? That is how you do it. So now the question is how do you get the Z Z, right? Now Z J is given as

### 01:57:17 · Speaker 6

a linear combination of

### 01:57:34 · Speaker 6

alpha j what is called as t

### 01:57:46 · Speaker 4

value vectors. Okay? Now I'll tell you what these value vectors are. So now,

### 01:57:52 · Speaker 6

one

### 01:57:57 · Speaker 6

Given a

### 01:57:59 · Speaker 4

Data Token

### 01:58:03 · Speaker 4

XJ, XJ, Okay.

### 01:58:06 · Speaker 4

multiply that with

### 01:58:11 · Speaker 4

three matrices. Call one as the query matrix. So this is

### 01:58:19 · Speaker 4

Transpose X J

### 01:58:22 · Speaker 6

Okay. Then you have

### 01:58:27 · Speaker 6

Value

### 01:58:29 · Speaker 6

Matrix

### 01:58:32 · Speaker 6

and the key matrix

### 01:58:38 · Speaker 4

What are we doing? We are getting three particular vectors, okay? So here, all

### 01:58:51 · Speaker 4

obtained three vectors

### 01:58:57 · Speaker 4

as this. Here the W Q W V

### 01:59:02 · Speaker 5

W uh

### 01:59:06 · Speaker 5

W K are learnable. And learn through back propagation. These are the learnable matrices. Do you understand? So what is happening? Given a particular data point, you take each of the token corresponding to it, which is a vector. Okay? Uh pre-multiply that with three matrices. Okay? And you get

### 01:59:28 · Speaker 5

three other vectors, call them query, value and key.

### 01:59:32 · Speaker 5

Is that okay?

### 01:59:35 · Speaker 5

This is called the query vector. Any questions so far?

### 01:59:40 · Speaker 3

Sir, XJ should be the entire sequence, right? Not one of the components.

### 01:59:43 · Speaker 5

one of the no no no components. It's one of the components. It's not the sequence. Because for every vector in the sequence, okay? You compute the query value and key.

### 02:00:03 · Speaker 0

सर एक्स इन इटसेल्फ इज अ वेक्टर।

### 02:00:06 · Speaker 1

is a sequence.

### 02:00:10 · Speaker 1

X is a sequence that has T number of vectors.

### 02:00:20 · Speaker 1

Is it okay?

### 02:00:23 · Speaker 1

See how did we define a sequence

### 02:00:25 · Speaker 3

We have defined a sequence this way, right?

### 02:00:30 · Speaker 3

sequence every vector right a sequence is a T length

### 02:00:36 · Speaker 3

couple where every each component of it is a uh d-dimensional vector.

### 02:00:45 · Speaker 1

So every x j is a vector here.

### 02:00:52 · Speaker 1

Okay

### 02:00:56 · Speaker 1

you get these three vectors, right? So then what you do is

### 02:01:02 · Speaker 1

you define the

### 02:01:11 · Speaker 1

representation corresponding to the uh Jth token as a linear

### 02:01:16 · Speaker 3

combination of

### 02:01:21 · Speaker 3

all the value vectors corresponding to all the other tokens in the sequence. Okay. So the question is how do you get this alpha j?

### 02:01:33 · Speaker 3

अब इस अल्फा

### 02:01:34 · Speaker 1

जे कॉटन सो व्हाट यू डू इस दैट यू

### 02:01:47 · Speaker 1

multiply the

### 02:01:55 · Speaker 1

Jeth

### 02:01:56 · Speaker 3

take the inner product of the jth query which actually I should call it alpha uh okay hold on

### 02:02:07 · Speaker 3

So, uh

### 02:02:09 · Speaker 3

I need one more symbol here.

### 02:02:11 · Speaker 1

Hello

### 02:02:13 · Speaker 1

this is for J

### 02:02:16 · Speaker 1

So now for

### 02:02:23 · Speaker 3

Okay, let me just write it. So now you take the jth query and multiply that with uh the uh ith key.

### 02:02:36 · Speaker 3

depend that with the Ith key, okay? Then what you get is, you get the attention score or the weight score corresponding to the Jth query and the Kth key, okay? So this will give you alpha J I.

### 02:02:57 · Speaker 3

which is a scalar. Fine. Now,

### 02:03:00 · Speaker 1

Uh

### 02:03:03 · Speaker 1

you need to multiply this.

### 02:03:14 · Speaker 1

cumbersome, that's why I'm thinking how can I simplify this. Just give me a second, we think.

### 02:03:26 · Speaker 1

Yeah, that is one value. And

### 02:03:39 · Speaker 1

I need to look at the

### 02:03:45 · Speaker 1

Yeah, this is

### 02:03:47 · Speaker 1

to fix this J

### 02:03:51 · Speaker 1

and

### 02:04:11 · Speaker 1

This is what it is.

### 02:04:13 · Speaker 1

Do you understand what's happening?

### 02:04:18 · Speaker 3

Okay, so I'll tell you. See, now what is happening is that we are given, I'll write it here, it will be easier.

### 02:04:30 · Speaker 3

I thought this class would end early. These are

### 02:04:36 · Speaker 3

These are sequences, right? F T sequences. What is first done is that you multiply these with the W matrices and get the corresponding queries. So this is Q one, Q two up to Q T. We have these queries and we have these

### 02:04:57 · Speaker 3

multiply that with the K matrix and get the keys

### 02:05:04 · Speaker 3

Okay? And then you have the multiply that with the

### 02:05:10 · Speaker 3

value matrices to get the values.

### 02:05:14 · Speaker 3

Okay. Now, what we are doing is, uh we get

### 02:05:22 · Speaker 3

you have to get Z J. Okay, Z one. To get Z one what you do is you take the inner product. Okay? Between the query corresponding to the first token, okay? With the query keys corresponding to all of the tokens. So,

### 02:05:42 · Speaker 3

This is a you take a

### 02:05:44 · Speaker 1

there are product like this between this two is to

### 02:05:54 · Speaker 1

is to is to

### 02:05:57 · Speaker 1

East

### 02:05:59 · Speaker 1

and these

### 02:05:59 · Speaker 3

This will give you, what will this give you? This will give you, the way I have written it, this will give you alpha one one, alpha one two.

### 02:06:11 · Speaker 3

Alpha

### 02:06:12 · Speaker 1

1 T

### 02:06:17 · Speaker 1

Is this okay?

### 02:06:23 · Speaker 1

Are you getting it?

### 02:06:28 · Speaker 1

Any questions on how are we getting alphas?

### 02:06:34 · Speaker 1

This is important so please tell me if you don't understand this.

### 02:06:45 · Speaker 1

Hello

### 02:06:49 · Speaker 3

Hello, am I there? Am I audible?

### 02:06:51 · Speaker 1

Yes sir you are audible yes

### 02:06:53 · Speaker 3

Okay. Yeah, total radio silence. So I don't know how to interpret it. Is it okay? Did all of you get how to get these alphas?

### 02:07:00 · Speaker 1

plus

### 02:07:10 · Speaker 1

Yes or no

### 02:07:15 · Speaker 1

Yes sir

### 02:07:16 · Speaker 3

Okay

### 02:07:18 · Speaker 3

Now how are these V's obtained? uh sorry, Z's obtained. They are obtained by taking a linear combination of all these values, okay? And they are weighted

### 02:07:31 · Speaker 3

uh by the corresponding alphas. Okay. In fact, uh it's uh it's actually a convex combination. So what is done is uh you you don't use alphas but you use betas, okay?

### 02:07:50 · Speaker 3

there

### 02:07:53 · Speaker 3

beta J I's, okay? Where betas

### 02:07:59 · Speaker 3

are you take alphas, okay?

### 02:08:03 · Speaker 3

and divide that by some constant d which is the dimensionality of data and then you do a

### 02:08:11 · Speaker 3

just say that

### 02:08:14 · Speaker 3

alphas are softmax

### 02:08:19 · Speaker 3

over alpha divided by t that's all so now why do you do this? this you do because

### 02:08:27 · Speaker 3

all beta j's, right? They are bounded between zero and one and they simply sum to one. That is why you do this soft match so that the linear combination of the values that you are taking, okay, uh is bounded between zero and one. So now let me repeat what is done here is that

### 02:08:46 · Speaker 3

you given a token, given a sequence of tokens, okay, which is an input data point, one input data point. You define three matrices, call them as, and multiply those data points with the with these three matrices, okay? They and call them as the query value and key vectors. So corresponding to each of the token, you will get three vectors, okay?

### 02:09:14 · Speaker 3

Then the representation corresponding to each of the input uh token is a linear combination of all the value vectors corresponding to each of the tokens. Okay? That's all. Now how do you define uh which of I mean how do you get uh what is the weight factor for the linear combination? To get the weight factor for the linear combination you use the query and key vectors. How?

### 02:09:44 · Speaker 3

you take the query vector corresponding to the token of interest. You take an inner product of that query with all the key vectors corresponding to all the tokens and normalize it so that it lies between zero and one. That would give you what is the weight or scale with which you have to scale each of the value vectors to obtain the representation corresponding to the I mean the token of interest. So this is

### 02:10:14 · Speaker 1

one

### 02:10:16 · Speaker 1

transformer block.

### 02:10:24 · Speaker 1

with a single head they call it and there is also a

### 02:10:27 · Speaker 3

a counterpart called the multihead

### 02:10:32 · Speaker 3

attention I'll talk about that in a while. But yeah any questions so far?

### 02:10:40 · Speaker 2

So so if we shuffle the X one to X T, then the Zs will also be shuffled.

### 02:10:50 · Speaker 2

in the sense like the if the sequence changes

### 02:10:54 · Speaker 3

Yes, that is true.

### 02:10:58 · Speaker 2

Okay, so please go ahead, yeah. So,

### 02:11:03 · Speaker 2

So so does it when it changes does it still remain the do the individual values still remain the same or will they also change?

### 02:11:10 · Speaker 3

No, no, they do change, you know. They do change depending upon what the sequence, what the, what the correspond, what the relative positions of each of the tokens are in the sequence. They do change.

### 02:11:25 · Speaker 2

Okay

### 02:11:28 · Speaker 2

Okay sir

### 02:11:29 · Speaker 3

Okay

### 02:11:30 · Speaker 0

Sir, is that tea fixed here?

### 02:11:34 · Speaker 3

Yeah, case fixed. Yeah. So you you keep hearing about this context lens of all these LLMs, right?

### 02:11:34 · Speaker 0

Yes

### 02:11:42 · Speaker 3

they say that you are coming up with like larger and larger context length. This T is what is called as context length. Now it is like uh two thousand five hundred is what the context length of GPT is and so on. That is the context length. So now you might ask this question.

### 02:11:59 · Speaker 3

We started by saying that each of the input data point will have different sequence length. How does transformer handle it? They handle it by just zero padding, that's all. So they keep a fixed context length and then if wait, that length is equal to the highest possible length of the highest possible sequence and for all the other sequences that have length less than the highest possible length sequence, they just zero pad them and make them equal length.

### 02:12:26 · Speaker 3

And now how does that how is that handled? The hope is that that is handled by the appropriate representation.

### 02:12:37 · Speaker 3

okay? The attention for or rather these alphas and betas for that corresponding zero tokens will be zero and it has been observed that they will actually ignore them.

### 02:12:51 · Speaker 1

ओके सर, थैंक यू.

### 02:12:52 · Speaker 3

Okay

### 02:12:53 · Speaker 2

Yeah, one more point here, sir. I mean, here that position information is not present anywhere, right? So if you shuffle the sequence...

### 02:12:57 · Speaker 3

so if you shuffle the sequence. Yeah yeah hold on. That's correct. That is correct and do you recall that during our DDPM discussions I talked about positional embeddings where we have to do give T the time information also as an input.

### 02:13:15 · Speaker 3

right? In transformer also what is given is in addition to this, T is also given as an input using the positional encoding.

### 02:13:25 · Speaker 1

for the precise reason that you said.

### 02:13:34 · Speaker 1

positional embeddings. And we talked about positional embeddings during the

### 02:13:40 · Speaker 3

LLM lectures, sorry, the diffusion lectures, okay? Fine. Now how do we finally solve the, uh, the

### 02:13:51 · Speaker 3

sequence to sequence problem is that we have here a transformer block

### 02:13:58 · Speaker 3

there is one other like normalization layer that they use and also a skip connection like resnet and so on right I'm skipping that the major focus is on attention okay. So you can yeah there are enormous amount of literature on this you'll understand the difficult part is how the attentions are actually uh computed so you get Z one through ZT okay. And there is this this is the encoder.

### 02:14:27 · Speaker 3

Similarly, there is a decoder block.

### 02:14:33 · Speaker 3

what does it do is it will take these

### 02:14:39 · Speaker 3

embeddings are the representations given by the encoder as the input, okay? And then do an auto regressive uh generation. So you get one Y one and you take Y one as an input and give it.

### 02:14:53 · Speaker 3

just like you do it in R N N, right? So you take that and you get Y two. And you take that as give it as an input and so on, okay? So this is only in fact this is exactly what a large language model does.

### 02:15:09 · Speaker 3

Okay. So this is BART kind of language model. This is how the training happens. In addition to this, there's also like attention blocks between the encoder and decoder, okay?

### 02:15:23 · Speaker 3

these are called

### 02:15:26 · Speaker 3

cross attention. details so this is whatever we saw right which is attention between the input tokens. uh that is called self attention and there is also attention between the

### 02:15:42 · Speaker 3

queries keys of the the encoder and the query keys of the decoder that is called cross attention. And this is actually the bare bone of what the modern day LLMs do. Okay. So now you know that right I mean you are given a particular prompt when you give GPT a prompt what you are actually doing is giving a prompt to the encoder and depending upon your prompt this decoder generates and how is the training done surprisingly enough training is completely supervised.

### 02:16:14 · Speaker 3

supervised training

### 02:16:18 · Speaker 3

using K L minimization. I mean like the

### 02:16:22 · Speaker 3

usual cross entropy loss

### 02:16:25 · Speaker 3

is what is used.

### 02:16:28 · Speaker 3

That's all. Bare minimum try bare bone training of an LLM happens in a completely supervised way, okay? Using KL minimization. So you have pairs of these tokens input and output tokens. In fact, uh actually what happens is that you first train an embedding extractor using the self supervised learning techniques that we just saw, no? Mast uh reconstruction. Last class we looked at mast reconstruction. So what is done is, let me just talk about it perhaps. So first thing that is done is, okay, this broad level LLM training typically happens this way.

### 02:17:08 · Speaker 1

So there is first a self-supervised pre-training.

### 02:17:20 · Speaker 1

where

### 02:17:22 · Speaker 1

And by the way architecture wise right

### 02:17:24 · Speaker 3

everything that is used in an LLM today are transformers. You take a transformer. Okay? uh take an input sequence.

### 02:17:35 · Speaker 3

and

### 02:17:39 · Speaker 3

you get the embeddings and uh the the task is to simply

### 02:17:44 · Speaker 1

simply reconstruct data back

### 02:17:51 · Speaker 1

using the encoding so I

### 02:17:53 · Speaker 3

Technically speaking, there is also an encoder decoder model here. Another transformer.

### 02:18:01 · Speaker 3

the decoder

### 02:18:04 · Speaker 3

C one to C three and what is given as an input is a version of X okay where it is where X cap is

### 02:18:18 · Speaker 1

a mass mass conversion of X.

### 02:18:25 · Speaker 3

usual self supervised learning task that we do right and this these will go as input to the decoder and what is

### 02:18:33 · Speaker 3

given back is the true data. So this is exactly what is done in BERT, okay? So you have an encoder and a decoder and encoder takes a masked version of X with random masked and it reconstructs the data. So this is what is called as the self-supervised pre-training.

### 02:18:51 · Speaker 1

I think

### 02:19:00 · Speaker 1

Okay? This is done. Once this is done, you get

### 02:19:03 · Speaker 3

embeddings of data. So then you use a usual encoding decode encoder decoder model in the second stage.

### 02:19:12 · Speaker 1

using supervised fine tuning.

### 02:19:23 · Speaker 1

supervised fine tuning, okay? on the embeddings obtained in the

### 02:19:37 · Speaker 1

obtained using cell supervised learning.

### 02:19:45 · Speaker 1

See, surprise

### 02:19:45 · Speaker 3

basically, uh, the

### 02:19:49 · Speaker 3

inner workings of LLM is very very simple. I mean from an ML complexity perspective, all you do is take a lot of data and do a self supervised pre training using mass reconstruction kind of task and then you do a supervised fine tuning on whatever data that you want to fine tune it on. That's all it is. Using transformer as the backbone.

### 02:20:11 · Speaker 3

Now, there are nuances here where when you are doing fine tuning, right? You may not have a lot of data. How do you do it without fine tuning? There is this retriever augmented generation or RAC kind of frameworks. And also this low rank reconstruction, low rank approximation for fine tuning where the problem is that if this pre-training, the model is like billions of parameters, you can't, you can't fine tune on all billions of parameters. You just take a subset of them and then fine tune and all those are other

### 02:20:41 · Speaker 3

improvisations and nuances. But at a broad level this is exactly what happens. So we there's a transformer which is which is the big backbone architecture. You take data typically from the entire internet.

### 02:20:55 · Speaker 3

and do a self-supervised pre-training using mass reconstruction task which we have seen. and then whatever take that model which generates embedding and do a supervised fine tuning on whatever data that you want and that's if you do that then you already have a like GPT2 or GPT3 that is there.

### 02:21:17 · Speaker 3

That's that's what it is. Any questions on this? As I said no this is not a full course on LLM so I don't go to the nuances of it. Just wanted to introduce and put it in the perspective of what the the so called modern LLMs are doing. So this is exactly what it is. As I said no in terms of ML complexity it's very very simple. There is a self supervised pre training using transformers and there is a supervised fine tuning that is happening using usual cross entropy kind of losses. Right? And the underlying architecture that is used is a transformer.

### 02:21:54 · Speaker 3

Please also remember the word generative AI, right? It is used in a very, very loose sense today in outside of expert community where it is used for like image generation, language generation and all that. Whenever there are there is a sequence task that is done, no, a transformer is used and this kind of recipes followed. Wherever there is an image generation task, no, typically transformer is not used, a diffusion model is used.

### 02:22:25 · Speaker 3

Right? Okay, so that's about it. That's all I wanted to cover in this course.

### 02:22:35 · Speaker 3

Yeah, so let's maybe just stop recording.

### 02:22:42 · Speaker 1

Solar

### 02:22:43 · Speaker 0

what is rag you talked about little right what is that we heard it many places in the JNU area

### 02:22:50 · Speaker 3

Yeah. See the thing is, even when you fine tune, right? Sometimes, you know, it will not, it may not suit your purpose, you know. It's think of it like

### 02:23:01 · Speaker 3

using an additional uh data that you have, okay? without doing a fine tuning, I mean supervised fine tuning on it. uh you use that additional data to guide your transformer or generator in some way. or the decoder. See, in all our generative modeling, right? we know
