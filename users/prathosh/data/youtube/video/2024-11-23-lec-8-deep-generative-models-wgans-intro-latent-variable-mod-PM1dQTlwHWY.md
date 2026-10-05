---
id: PM1dQTlwHWY
title: Lec 8 - Deep Generative Models WGANS Intro Latent Variable Models
date: '2024-11-23'
url: https://www.youtube.com/watch?v=PM1dQTlwHWY
description: ''
author: prathoshap5226
duration: 02:55:07
model: saaras:v3
transcript: true
---

# Lec 8 - Deep Generative Models WGANS Intro Latent Variable Models

## Transcript

### 00:00:02 · Speaker 11

Yes sir, we were able to see.

### 00:00:04 · Speaker 9

the first quiz also you got to see the marks, right?

### 00:00:08 · Speaker 6

as it has been realized.

### 00:00:10 · Speaker 9

Okay, thanks. And we have decided the midterm exam to be on the thirteenth or something, right? I think I've marked our calendars also.

### 00:00:25 · Speaker 2

Yeah. Yes sir.

### 00:00:27 · Speaker 6

Yes, it's 13th afternoon.

### 00:00:28 · Speaker 9

thirteenth afternoon. Okay, great. Okay, so let's get to somebody has raised their hand. Arijit, yeah.

### 00:00:36 · Speaker 0

Uh sir maybe a logistical request if feasible uh otherwise please reject because this four to two to six is like a festive for us like Durga Puja and all Dussehra. So that assignment time can it be increased by three four days? Just a request if not for feasible please ignore.

### 00:00:55 · Speaker 9

What can what uh

### 00:00:57 · Speaker 0

assignment date assignment deadline is ninth I believe right and two to six is somewhere is a festive session for most of us like Dussehra Durga Puja etcetera so can it be increased by two three days I mean the timeline because we may not give the complete hour should be given to this project during that time

### 00:01:01 · Speaker 9

and

### 00:01:19 · Speaker 0

is just a request. I mean, if not possible, please ignore.

### 00:01:23 · Speaker 9

I mean see what happens is no if I move it then the other assign the entire schedule has to be rearranged. So

### 00:01:32 · Speaker 4

Okay

### 00:01:33 · Speaker 9

kindly excuse me

### 00:01:34 · Speaker 2

on that.

### 00:01:35 · Speaker 4

Okay

### 00:01:47 · Speaker 2

Okay, let's get started.

### 00:02:03 · Speaker 2

Hmm

### 00:02:04 · Speaker 2

You don't see my screen.

### 00:02:15 · Speaker 2

Um, option.

### 00:03:18 · Speaker 2

ओके. सो टुडे

### 00:03:19 · Speaker 9

this agenda is that as I said we will move on to the next class of models which are variation autoencoders. which also happens to be the the baseline for the state of the art generative image generative models called diffusion models which you will see next okay. so before we go there we just take some ten fifteen minutes and quickly finish this domain at most serial networks right which was left out the last time.

### 00:03:49 · Speaker 9

Okay

### 00:03:51 · Speaker 2

Always there

### 00:03:53 · Speaker 2

still it is

### 00:04:02 · Speaker 2

hide this.

### 00:04:18 · Speaker 2

somebody asked me to center align this

### 00:04:22 · Speaker 2

should it get cut

### 00:04:23 · Speaker 9

Oh

### 00:04:28 · Speaker 9

doesn't even know how to do that.

### 00:04:29 · Speaker 4

through that

### 00:04:30 · Speaker 4

So you can zoom it. Yeah. In the view, in the view you can make it 100%.

### 00:04:35 · Speaker 9

Come again

### 00:04:37 · Speaker 4

on the top you will see home insert of you hundred percent

### 00:04:39 · Speaker 9

Centro

### 00:04:44 · Speaker 9

Okay thanks.

### 00:04:49 · Speaker 9

Okay, so, um

### 00:04:53 · Speaker 9

We will start with this domain adversarial networks, okay? So called dance, one of the powerful applications of adversarial learning other than generative modeling. And also right before we start, I hope that you have started with the assignment.

### 00:05:12 · Speaker 9

and if there are any questions you can let me know or T S also know

### 00:05:16 · Speaker 1

I pinged in TA but no one replied

### 00:05:21 · Speaker 9

Oh, is it? I'll I'll ask Chandan to do it. So last tutorial was done on like CNNs and PyTorch, right? Was it useful?

### 00:05:34 · Speaker 4

Sir, it is useful, but sir, in the tutorial, can we have some sample output of the first question?

### 00:05:42 · Speaker 4

like at what level we have to optimize

### 00:05:46 · Speaker 9

You mean in the assignment you are saying. See what I have observed is that uh that this animal data set right because there are multiple classes there. About ninety classes. Uh unless you have a very uh deep architecture and you do a lot of hyperparameter tuning you don't get very good generated images.

### 00:05:48 · Speaker 4

See what

### 00:06:06 · Speaker 9

Right but if you if you get images that are like uh somewhat looking like butterfly you will definitely get. For that data set you will get good images. Not for the first one. There are two data sets that we have given no.

### 00:06:11 · Speaker 10

Butterfly

### 00:06:21 · Speaker 4

Correct

### 00:06:22 · Speaker 9

Yeah, for the animal data set, the images that are generated are like somewhat, uh like looks looks like animalish, but you need a lot of resources and deeper architectures to

### 00:06:35 · Speaker 9

get very good results. Okay, in fact,

### 00:06:40 · Speaker 9

Okay, so, uh, have I, uh,

### 00:06:44 · Speaker 9

talked about F I D in this course.

### 00:06:49 · Speaker 2

Nostra

### 00:06:49 · Speaker 4

Sir

### 00:06:50 · Speaker 2

not

### 00:06:50 · Speaker 4

Notice

### 00:06:50 · Speaker 9

Yes sir, No sir

### 00:06:51 · Speaker 2

Audio

### 00:06:52 · Speaker 11

It is planned for today

### 00:06:52 · Speaker 9

is planned for today. Yeah, I'll have to do that today as well.

### 00:06:59 · Speaker 9

I've not told you about the the versus strain symmetric also, no?

### 00:07:04 · Speaker 4

Yes sir

### 00:07:05 · Speaker 2

No sir, we haven't.

### 00:07:06 · Speaker 4

we have it

### 00:07:12 · Speaker 1

if the animal data set is hard for question one and two then why are you asking for the other questions?

### 00:07:13 · Speaker 4

animals to cover

### 00:07:21 · Speaker 9

Come again

### 00:07:22 · Speaker 1

Like if animal data set is hard to train given the compute resource we have then for other questions also like third fourth and waste all like we'll have to use the same data set right animal. Then we'll have then we'll have a poor result there also if we train lesser. That's okay. Okay.

### 00:07:33 · Speaker 9

Yeah, yeah.

### 00:07:36 · Speaker 9

That's okay. Okay. That's okay. See the the assignment grading will not be based on the quality of your generated data anyway. It's not about results.

### 00:07:47 · Speaker 9

uh so yeah but it has I mean I have deliberately chosen that data set because I want you to appreciate the fact that if there are too many classes and data has lot of modes right uh building a generative model is difficult especially using adversarial training so we will use the same data sets for VAE centrifusion models and you will see that it will improve it was deliberately done yeah

### 00:08:13 · Speaker 7

Sir, sir, the confirmation what we were trying to ask, the butterfly data set is for only the one and two. Correct. From the third onwards, we need to use the animal data set. The the the first GAN, we need to use the animal data set and see how the outcomes are coming, even the FID calculation, everything.

### 00:08:14 · Speaker 9

சர் செக்கன்

### 00:08:23 · Speaker 9

correct

### 00:08:27 · Speaker 9

okay

### 00:08:36 · Speaker 9

Correct, Correct.

### 00:08:37 · Speaker 7

ओके, ओके, दैट वाज़ अ कंफ्यूजन।

### 00:08:40 · Speaker 9

Hello

### 00:08:41 · Speaker 9

But for the first and second question you will have to use the animal data set as well both of them.

### 00:08:47 · Speaker 7

Oh, yeah, we definitely we need to train it for the other things. Yes. Okay. But the generation may not be so accurate. Yes.

### 00:08:50 · Speaker 9

Correct. Correct. Okay.

### 00:08:54 · Speaker 9

Yes. Yes. Yes.

### 00:08:57 · Speaker 5

Okay

### 00:08:58 · Speaker 9

So, let's maybe continue quickly.

### 00:09:01 · Speaker 9

Go on, Rajagopal.

### 00:09:04 · Speaker 5

uh yes sorry sir one more thing. I noticed sir in the original Gyan paper uh the model was basically on a sixty four by sixty four image. The the moment I scale it up to one twenty eight right I noticed the mode collapse becomes a lot frequent than sixty four by sixty four like the performance is much better. uh any reason?

### 00:09:21 · Speaker 9

DC Gyan, DC Gyan you are saying.

### 00:09:24 · Speaker 5

Yeah, yeah, yeah.

### 00:09:26 · Speaker 9

DCGAN, okay. uh Yeah, see, uh you can tweak one thing that you can do is uh if you start from one twenty eight, one twenty eight, just have another down down sampling layer and then use DCGAN on top of it.

### 00:09:40 · Speaker 5

Sure sir. I tried that. I think it requires a little hyperparameter tuning to get it right.

### 00:09:42 · Speaker 9

Bye

### 00:09:44 · Speaker 9

Correct. Correct.

### 00:09:46 · Speaker 5

Okay sir

### 00:09:49 · Speaker 9

Yeah, Balaji.

### 00:09:51 · Speaker 3

Yes sir. My question is regarding the assignment. So in question eight it is asked we should implement a decoder network. So should this be for the GAN in the first question or the conditional GAN?

### 00:10:05 · Speaker 9

It's in the gain in the first question only

### 00:10:07 · Speaker 3

ओके, ओके, थैंक यू।

### 00:10:12 · Speaker 9

Satya

### 00:10:15 · Speaker 6

Sir, this is the instance of Gyan, F Gyan we discussed, right, where we used the Gyan, Shen and divergent for the naive Gyan. So actually if you see that F Gyan paper, right, sir, that is the Gyan is separately mentioned and Gyan Shen is also separately mentioned. So it's not that because of Gyan Shen we are waiting. Okay, okay, I'll tell you.

### 00:10:31 · Speaker 9

Okay

### 00:10:34 · Speaker 9

Okay, okay, I'll tell you. Yeah. See, uh, okay, that's a good observation. See, uh, the divergence that is used in the Naive Gyan paper is Jensen-Chanon divergence minus a constant. I think it's log two or something.

### 00:10:49 · Speaker 9

Okay, that that's the in its its JS divergence plus a constant. That is what the Gyan objective is.

### 00:10:59 · Speaker 2

Okay

### 00:11:00 · Speaker 9

Yeah

### 00:11:03 · Speaker 9

Okay, so let's maybe quickly go through too many things to discuss. Okay, let's get started. Yeah, it's charged. I said, so this

### 00:11:15 · Speaker 9

there is another application of uh adversarial learning which is called domain adversarial networks. Okay? So here is the problem. So what you are given is you are given some data from a distribution called source distribution. Okay? It's one by one.

### 00:11:37 · Speaker 9

to you to

### 00:11:40 · Speaker 9

up to

### 00:11:42 · Speaker 9

Seven Y N. Note that this is a supervised problem. This is drawn I D from a distribution P S which is called the source distribution. This is source data.

### 00:11:56 · Speaker 2

And there is another data that is given to you. You call X graph one.

### 00:12:04 · Speaker 2

square two and

### 00:12:07 · Speaker 2

Next

### 00:12:07 · Speaker 9

cap

### 00:12:10 · Speaker 9

So this is sampled I I D from P T okay and this is called the target data.

### 00:12:19 · Speaker 9

Note that source data has both the features and labels. Target data only has the features and does not have labels. Source data is supervised.

### 00:12:36 · Speaker 2

Okay. This is unsupervised.

### 00:12:45 · Speaker 2

Now the goal

### 00:12:50 · Speaker 2

of what is called as unsupervised domain adaptation.

### 00:13:06 · Speaker 2

so called as UDA, okay? is

### 00:13:13 · Speaker 2

Even

### 00:13:15 · Speaker 2

PS and DT, okay?

### 00:13:25 · Speaker 2

learn features or representations.

### 00:13:32 · Speaker 2

such that

### 00:13:38 · Speaker 2

that they perform

### 00:13:44 · Speaker 2

well known both source and target data.

### 00:13:52 · Speaker 9

often times what happens is that suppose you want to let me just show you an example. uh suppose you want to uh you are you want to build a classifier. Hold on.

### 00:14:06 · Speaker 9

supervised.

### 00:14:10 · Speaker 2

Sure

### 00:14:12 · Speaker 2

show some examples and you'll understand

### 00:14:27 · Speaker 2

give me a minute I'm just looking for that image.

### 00:14:38 · Speaker 2

Yeah, this is good. Hold on, let me share my screen.

### 00:14:47 · Speaker 2

Do you see my screen?

### 00:14:52 · Speaker 4

No sir

### 00:14:53 · Speaker 9

No

### 00:14:54 · Speaker 4

Now yes

### 00:14:55 · Speaker 9

Okay, so look at this. So there are these data sets, okay? Uh, there is MNIST, there is USPS, something called MNIST M and there is the street view house numbers data set, okay? Now, what you see is that all of these are semantically the same. The class wise they all have the same, right? They have digits, okay? But if you build a classifier on let's say MNIST and try to test it on USPS, not, uh, it will not give you good performance.

### 00:15:30 · Speaker 9

Okay? Now the goal is that suppose you are given

### 00:15:34 · Speaker 9

डेटा फ्रॉम एमनेस्ट विथ लेबल्स एंड डेटा फ्रॉम यूएसपीएस विदाउट लेबल्स

### 00:15:40 · Speaker 9

That is the setting, right, where you understood the setting that there is a source domain which has labels and there's a target domain which has data but does not have labels. Okay? Now the task is that you have to build representations such that

### 00:15:57 · Speaker 9

The classifier that is trained on the source data does well on the target data as well.

### 00:16:03 · Speaker 9

that is the problem setting.

### 00:16:07 · Speaker 9

Is it clear? Any questions?

### 00:16:09 · Speaker 9

So you have to ensure that the problem definition is clear, then we will move on.

### 00:16:14 · Speaker 9

Please ask if you have any questions. Can't see your... Yeah, Shivam.

### 00:16:20 · Speaker 10

Yes sir, when we say we want to learn this on the the model should perform well on the target distribution as well. Eventually we will be passing target distribution back to the model to get the respective target labels, right?

### 00:16:36 · Speaker 9

final evaluation will be done with target labels of course. but while you are building the model you don't have target labels.

### 00:16:45 · Speaker 2

Okay

### 00:16:47 · Speaker 9

Of course, I mean, when you evaluate the, definitely it will be based on the target labels only, but yeah.

### 00:16:55 · Speaker 9

I don't see. Yeah, Satya, go on.

### 00:16:59 · Speaker 6

Sir, isn't it the cycle here? It's the same, right, which you're doing? Only that we don't have the labels for the first data source, data source.

### 00:17:04 · Speaker 9

No, see, in in in CycleGyan, the the the objective is to uh convert the source data to target data, right? Generate samples from target data. Here you you're not you're not the objective is not to generate the target data, it is to build a classifier or representation such that it does well on target data as well.

### 00:17:26 · Speaker 6

Okay, okay. To produce a label over that target data.

### 00:17:29 · Speaker 9

Correct

### 00:17:33 · Speaker 9

Sanjit

### 00:17:35 · Speaker 7

Sir, you answered my question. So basically we are trying to

### 00:17:37 · Speaker 9

basically we are trying to... Let's move on then then then let's move on please because it's too many things to cover today. If I've answered your question let's move on. Okay. So that's the uh the um okay I'll have to share it again.

### 00:17:45 · Speaker 7

Okay

### 00:17:54 · Speaker 9

That is the problem setting. See, there is also another class of problems, right, where you do not even have data from the target distribution. Okay? Those set of problems are called domain generalizations.

### 00:18:07 · Speaker 9

This is domain adaptation. Suppose you don't have DT as well, okay? Then those class of problems are called domain generalization. We are not looking at domain generalization. Now we are looking at domain adaptation, okay? Where target data is also present, albeit without labels. How do you solve this question or solve this problem? There are multiple methods that people have come up with. One of them is what is called as

### 00:18:33 · Speaker 2

domain adversarial networks

### 00:18:49 · Speaker 2

domain adversarial networks, okay? What is done is the following. I'll show. So there is a

### 00:19:02 · Speaker 2

feature extractor, let us call that as some fee of x.

### 00:19:07 · Speaker 9

this will take X S which is the source data.

### 00:19:12 · Speaker 9

I think let us okay x and x cap right? x is the source data. and we'll also take

### 00:19:24 · Speaker 9

squared is a target data as input, okay? It will give you the corresponding representations. So let's call it as ZS and

### 00:19:35 · Speaker 2

Z T. And here.

### 00:19:42 · Speaker 2

Okay, so this is a

### 00:19:43 · Speaker 9

simply a feature extractor so this P

### 00:19:47 · Speaker 9

is a function that will take x and that will give you some features z, okay? Then what we will do is there is a classifier, there is

### 00:19:58 · Speaker 9

there is a critique network here or a discriminator network here.

### 00:20:06 · Speaker 9

E W, this will take Z. So this will take either

### 00:20:09 · Speaker 2

C S, okay? Sorry. C S.

### 00:20:15 · Speaker 2

and ZT

### 00:20:19 · Speaker 9

Okay, now I should say that

### 00:20:22 · Speaker 9

here

### 00:20:23 · Speaker 2

Hello

### 00:20:24 · Speaker 9

p of x is equal to zs, okay? And p of x cap is is is zt. Okay, that is how I have represented it. Fine. Now,

### 00:20:36 · Speaker 2

what I do is I will

### 00:20:44 · Speaker 2

trying this thing

### 00:20:55 · Speaker 2

So this will be trained adversarially, okay?

### 00:21:01 · Speaker 2

the gain

### 00:21:04 · Speaker 2

to ensure

### 00:21:08 · Speaker 2

the distribution of ZS, okay?

### 00:21:13 · Speaker 9

is close to the distribution of ZT.

### 00:21:16 · Speaker 9

Correct? That is if I try this adversary really, right? Then what happens is that the distribution of features P Z S will be close to the distribution of P C T. Do you agree?

### 00:21:29 · Speaker 9

See this whatever I have

### 00:21:32 · Speaker 2

color

### 00:21:40 · Speaker 2

marked with red color, this is a Gyan, okay?

### 00:21:44 · Speaker 2

two

### 00:21:47 · Speaker 2

insurance

### 00:21:51 · Speaker 2

PGS is same as PCT

### 00:22:00 · Speaker 2

Does it make sense?

### 00:22:03 · Speaker 2

Now phi of x will become the

### 00:22:04 · Speaker 9

generator, okay? And there is another discriminator that is there. And you are ensuring, you are training it adversarially to ensure that P C S is equal to P G T. So what is the loss function here? The loss function would be that you learn your C star and W star, okay? Such that

### 00:22:26 · Speaker 2

minimize

### 00:22:32 · Speaker 2

spin over V and max over W. You have an expectation of

### 00:22:39 · Speaker 2

log of

### 00:22:44 · Speaker 2

G S

### 00:22:47 · Speaker 2

as G S comes from P S.

### 00:22:50 · Speaker 2

you have expectation of

### 00:22:55 · Speaker 2

log of

### 00:23:00 · Speaker 2

one minus

### 00:23:02 · Speaker 2

T W of Z

### 00:23:06 · Speaker 2

T

### 00:23:11 · Speaker 2

this V T comes from

### 00:23:16 · Speaker 2

E C T

### 00:23:22 · Speaker 2

Are you getting it?

### 00:23:23 · Speaker 9

So now if I train this as a GAN now, right, what it will do is it will ensure that the features for the source data and target data follows the same distribution.

### 00:23:37 · Speaker 2

Does it make sense?

### 00:23:39 · Speaker 2

any questions on this?

### 00:23:51 · Speaker 2

Go on Indrajit

### 00:23:59 · Speaker 2

Indrajit, go on please.

### 00:24:14 · Speaker 2

I don't know if you can

### 00:24:17 · Speaker 9

Can you hear me all of you?

### 00:24:20 · Speaker 7

Yes sir. Yes sir.

### 00:24:22 · Speaker 9

Okay, Raghavendra, go on.

### 00:24:24 · Speaker 11

Uh yes, in this case, the fee network that you have shown is kind of compressing the features. But I mean...

### 00:24:28 · Speaker 9

in writer

### 00:24:30 · Speaker 9

Brahma

### 00:24:32 · Speaker 11

is it reducing the dimensions or increasing?

### 00:24:32 · Speaker 9

producing

### 00:24:34 · Speaker 9

Yeah, it is, it is. Yeah, yeah, yeah. Typically, Z is less than dimensionality of Z is much less than that of X.

### 00:24:43 · Speaker 2

it acts like a generator now.

### 00:24:52 · Speaker 11

Okay

### 00:24:52 · Speaker 9

but I'm

### 00:24:52 · Speaker 2

but I mean

### 00:24:52 · Speaker 11

it looks very similar to the discriminator, right? because it's it's reducing the dimensions.

### 00:24:56 · Speaker 9

reducing the dimensions. No, just because it reduces the dimension, it it's not discriminator, right? It is simply a neural network that transforms x from z, x to some one random variable to other. It can increase the dimension, reduce the dimension, doesn't matter.

### 00:25:11 · Speaker 9

Of course, it is similar to discriminator in the sense that it reduces the dimensionality. But yeah, it is not it is not a classifier, right, which is trying to uh give a number between zero and one. Okay. Okay, so this is uh yeah, Vivek.

### 00:25:22 · Speaker 11

OK

### 00:25:29 · Speaker 11

So what does it mean X and X cap? So are we passing it in sequence or are we

### 00:25:34 · Speaker 9

in sequence

### 00:25:34 · Speaker 9

Yeah, sequence, sequence, yeah. So you X, when X goes, ZS comes out. When X cap goes, so ZT comes out.

### 00:25:39 · Speaker 11

so when it

### 00:25:42 · Speaker 11

trickle sound. Okay, fine.

### 00:25:45 · Speaker 9

Here in addition to that, there's also a classifier here, okay?

### 00:25:55 · Speaker 2

this classifier, it's called that as h theta

### 00:25:59 · Speaker 9

it'll take Z

### 00:26:04 · Speaker 9

as input. The S as input and it will give you Y as output which are the which is trained on only the source domain. Okay? Now this

### 00:26:16 · Speaker 2

um

### 00:26:21 · Speaker 2

Theta star

### 00:26:32 · Speaker 2

theta star, okay? Simply the minimizer

### 00:26:37 · Speaker 2

of the cross entropy loss which is

### 00:26:51 · Speaker 2

CES coming from PS. Simply

### 00:26:54 · Speaker 9

optimizer of the usual cross entropy laws, okay, and tried supervised in a supervised way.

### 00:27:01 · Speaker 9

Okay. Now the gradients

### 00:27:06 · Speaker 9

flow like this

### 00:27:10 · Speaker 9

gradients for the free network, right? One, there is

### 00:27:14 · Speaker 9

a backward pass from here to here.

### 00:27:19 · Speaker 9

Okay, it is learned adversarily. And then there is another backward pass which is which is supervised training that goes from

### 00:27:29 · Speaker 9

to here

### 00:27:31 · Speaker 2

So this is supervised classification.

### 00:27:36 · Speaker 2

supervised

### 00:27:38 · Speaker 2

and this

### 00:27:41 · Speaker 2

This is adverse series.

### 00:27:49 · Speaker 2

So what is happening is that

### 00:27:51 · Speaker 9

This fee network is trying to learn features, okay, in such a way that one, it will ensure that the distribution of the features on source data and target data are exactly the same. This is, this is done via adversarial optimization. And the features are also learned in such a way that it does classification well on source domain.

### 00:28:20 · Speaker 9

Okay? Now during inference what do you do? Finally during inference

### 00:28:31 · Speaker 9

during inference, okay? uh you take x cap coming from p t, okay? and then pass it through phi star which is will give you z t. then take

### 00:28:46 · Speaker 2

एक जी टी

### 00:28:48 · Speaker 2

okay? and pass it through the

### 00:28:56 · Speaker 2

classifier, this will give you the labels which are the predicted labels on

### 00:29:11 · Speaker 2

D T

### 00:29:14 · Speaker 2

Does it make sense? So this this is how

### 00:29:16 · Speaker 9

you are doing. So what you are doing is you are training a classifier on source data, okay?

### 00:29:24 · Speaker 9

using features uh that have the same distribution as that of the target data.

### 00:29:31 · Speaker 9

Now, you basically are training a classifier that has exactly that that that is working on a feature space whose distribution follows exactly that of the features of the target and you are ensuring that it will happen you are enforcing that it will happen via adversarial training. Okay? So now once it is done, the features that are extracted for the source data is same as the features for the target data. So now if you take the features for the target data and pass it through the classifier that is trained on source features

### 00:30:07 · Speaker 9

It is expected to do well on the the the features of the target data because you have ensured via adversarial training that the features the distribution of the features of the source data is same as the distribution of the features of the target data.

### 00:30:25 · Speaker 9

This thing is called domain adversarial training and it is it is shown to be a very very effective method in in reducing the problems with unsupervised domain adaptation.

### 00:30:37 · Speaker 9

Okay. Any questions on this method?

### 00:30:44 · Speaker 9

या लोकेश

### 00:30:46 · Speaker 8

सर इज इट नेसेरी टू बैक प्रोपोगेट थ्रू फाइव फ्रॉम एच ऑफ थीटा एस वेल?

### 00:30:53 · Speaker 9

Yes, because otherwise what will happen, no? The features that have been learned, okay, may not be such that they are conducive for classification.

### 00:31:04 · Speaker 9

So you'll have to ensure that the classification also happens. The classification on the source data has to happen.

### 00:31:13 · Speaker 8

Can't that be captured by h of theta itself?

### 00:31:19 · Speaker 9

H of theta is trained no you have to train H of theta.

### 00:31:22 · Speaker 8

Yeah, yeah, so during that training on that

### 00:31:25 · Speaker 9

No, no, wasn't it your question? You are saying just use ZS and try H of theta separately is what you are saying, is it?

### 00:31:32 · Speaker 8

Right, right.

### 00:31:34 · Speaker 9

Why do you have to try and feel together with H of theta? Is that your question?

### 00:31:38 · Speaker 8

Right, right.

### 00:31:39 · Speaker 9

See if you if you take Z S uh separately and try H of theta what will happen is uh the features that have been learned to ensure that these two distributions are same may not be useful for the classification. For instance what can happen is

### 00:31:56 · Speaker 9

Suppose both of them for all x right or both of I mean the P C S and P C T are such that they give you one vector for all data points. Let's say that they all collapse.

### 00:32:10 · Speaker 9

Okay. So if that happens even then the distribution matches. PCS and PCT matches if for all X it will give you one vector.

### 00:32:20 · Speaker 9

But that that is not useful for classification.

### 00:32:25 · Speaker 9

Understood. So the features that have been learnt have to be such that they are useful for classification and that's why you have the classification objective also together while you are training it.

### 00:32:27 · Speaker 5

features that have been

### 00:32:38 · Speaker 2

ओके सर, राइट। थैंक यू।

### 00:32:44 · Speaker 9

Uh

### 00:32:46 · Speaker 9

Sanchit

### 00:32:49 · Speaker 7

Sir, can you please explain once again this process? Like how we are training and like how we are doing these like taking the supervised classification and the discriminator part back propagation together.

### 00:33:01 · Speaker 9

discriminate

### 00:33:07 · Speaker 9

See, first you take the source data, pass it through this fee network, you get a feature ZS, right? And uh then you have then you take X cap, pass it through that network, I mean you initialize this fee network randomly, you get uh ZT, okay? Now ZS become your ZS becomes your true data and ZT becomes your uh generated data and use those with a discriminator to adversarily back propagate fee Z uh through the

### 00:33:37 · Speaker 9

Fee X network and ensure that the distribution of ZS and ZT are the same. This is the usual GAN training.

### 00:33:46 · Speaker 7

Okay

### 00:33:47 · Speaker 9

The only difference between a usual GAN training and this is that in a usual GAN, right, the real data is not passed through the network, right, generator network. You you assume that it's already there with you. But here, GS becomes your real data and GT becomes your generated data. I use that to ensure, use that with a discriminator to ensure that the distributions are same, that is GAN training.

### 00:34:14 · Speaker 9

Okay. Then you have another classifier which is trained together with Gyan where this classifier takes data from the source uh features and predicts the source labels and train it in a supervised way.

### 00:34:28 · Speaker 9

Now, the the the this fee network, which is the feature extractor, will be trained both using the adversarial objective and the supervised objective together. So that it has to ensure that the distributions of source and target data matches while the uh the classification also happens properly.

### 00:34:53 · Speaker 7

So sir, this X and X cap, these are from the available input

### 00:34:58 · Speaker 9

I have defined it already. I mean you should not forget. See this is D S and D T are given. So X is the uh samples from D S and X cap are samples from D T. They are given.

### 00:35:12 · Speaker 2

Okay

### 00:35:17 · Speaker 9

That is what is given, no?

### 00:35:21 · Speaker 2

ओके सर

### 00:35:21 · Speaker 9

Okay. Raghavendra?

### 00:35:25 · Speaker 11

Yeah, so I mean, we have this labeled data here, right? So what are the things to be correct for the source?

### 00:35:28 · Speaker 9

label data only from the source.

### 00:35:33 · Speaker 11

Yes. So, I mean what advantage this uh generative model here uh I mean adds to this supervised learning because we could also directly train the H network over uh the X itself. But why would

### 00:35:45 · Speaker 9

But why would what yeah if you do that then what is the guarantee that uh the X if you suppose you train a classifier on X and pass X cap through it it will have a very bad performance. Because why is that so? Because PS and PT are not the same no distributions and PS and PS and PT are not the same.

### 00:35:58 · Speaker 11

Why is that so?

### 00:36:06 · Speaker 9

That's why I showed you that that picture, right, where you had MNIST and the SVHN data.

### 00:36:13 · Speaker 9

Right the distribution of P S and P T are not the same. I should make maybe write it explicitly. See here.

### 00:36:21 · Speaker 9

P.S.

### 00:36:22 · Speaker 11

they must be close enough, right?

### 00:36:24 · Speaker 9

they will not be. uh That is the problem with domain adaptation. When the ID assumption breaks, right? When the resource data is not equal to the target data, the classifier trained on one will fail miserably on the other. Actually, you can you can... Yeah.

### 00:36:36 · Speaker 11

you can

### 00:36:39 · Speaker 11

So if you go back to the diagram, right? So does it mean that uh the fine the the fee network is actually extracting features which are common across distribution? Is that how you can see it? Yeah. Yeah.

### 00:36:41 · Speaker 9

in the

### 00:36:49 · Speaker 9

Yeah, yeah, it is ensure it is ensuring that the features are extracted in such a way that across both the distributions the features have uh features are same. See while P T E, right, P T E is or rather

### 00:36:50 · Speaker 11

Okay

### 00:36:58 · Speaker 11

Same

### 00:37:04 · Speaker 11

Okay

### 00:37:06 · Speaker 9

PS is not equal to PT, right? PZS is equal to PCT by construction. That is the point.

### 00:37:12 · Speaker 11

And that's that's what we are trying to identify which is the distribution which is which is overlapping between those two.

### 00:37:18 · Speaker 9

not identifying that way so not that we should not say that there is there exists a distribution that overlaps we are trying to extract enforce features such a way that for both the distributions they match

### 00:37:31 · Speaker 11

Okay, yeah, understood. Thank you.

### 00:37:34 · Speaker 9

Okay, anything else?

### 00:37:38 · Speaker 9

also called DAN, okay? Domain Network Serial Networks or DAN. Powerful technique and it has, see actually I wanted to include this as a part of assignment but I thought it will be too much. So if anyone is interested you can try that out. Take MNIST and the UPS data set. Examples also here.

### 00:37:58 · Speaker 9

can be

### 00:38:03 · Speaker 9

Next, this can be UPS data. You try in a classifier on MNIST and test it using UPS data set, you will see an drastic uh reduction in accuracy.

### 00:38:18 · Speaker 9

Okay. Now and then you do this domain adversarial networks and see the accuracy on the target data will increase considerably.

### 00:38:31 · Speaker 2

Okay, so that's about it. Yeah, see the last thing

### 00:38:38 · Speaker 2

with GANSUS

### 00:38:50 · Speaker 2

Time is too short and we have so many things to discuss.

### 00:38:57 · Speaker 9

It's supposed to be a content for at least two courses if not more. Okay. So the last thing that I'll talk about for GaNS in GaNS is this thing called the Versa stains.

### 00:39:12 · Speaker 9

Ganns, okay.

### 00:39:16 · Speaker 9

This is needed only for that F I D.

### 00:39:18 · Speaker 2

otherwise we could have

### 00:39:20 · Speaker 2

skip that. Okay, we'll do it.

### 00:39:40 · Speaker 2

Okay

### 00:39:42 · Speaker 2

Um

### 00:39:45 · Speaker 2

Buses trains cannot optimal transport

### 00:40:03 · Speaker 2

W dash.

### 00:40:07 · Speaker 2

Okay, so now you know that for the F divergence minimizers, right?

### 00:40:17 · Speaker 2

R

### 00:40:20 · Speaker 2

very unstable in practice. So you have already seen that right? Gyan training is very difficult.

### 00:40:32 · Speaker 9

running Gyan is very difficult because

### 00:40:35 · Speaker 9

So this is something that you have seen, right? Gantt training is very difficult because of that saddle point problem that is there, okay? That is one problem. The question is, question is...

### 00:40:50 · Speaker 2

what makes learning hard, okay?

### 00:41:05 · Speaker 2

So in in in this paper which is called Vasushtenskyan, what they show is the following.

### 00:41:10 · Speaker 9

Suppose

### 00:41:15 · Speaker 9

you have what is the notation that we are using for that P

### 00:41:20 · Speaker 9

x and p theta right suppose px and p theta

### 00:41:24 · Speaker 2

are such

### 00:41:27 · Speaker 2

that

### 00:41:29 · Speaker 2

their

### 00:41:34 · Speaker 2

their supports, okay?

### 00:41:38 · Speaker 2

Don't overlap

### 00:41:44 · Speaker 2

Now I will explain what this means.

### 00:41:45 · Speaker 9

P X and P theta, okay, first of all, P X and P theta, okay, are our distributions.

### 00:41:59 · Speaker 9

or distributions over X, right? Which is typically some D-dimensional real space, correct? This is how it is.

### 00:42:08 · Speaker 2

Typically

### 00:42:13 · Speaker 2

Okay

### 00:42:13 · Speaker 2

Uh,

### 00:42:16 · Speaker 2

distributions

### 00:42:18 · Speaker 2

over real data, real data

### 00:42:24 · Speaker 2

lies over

### 00:42:28 · Speaker 2

small subspace

### 00:42:36 · Speaker 2

also called as manifold.

### 00:42:41 · Speaker 2

in the ambient space R D

### 00:42:47 · Speaker 2

I'll explain what this means, okay? Hold on.

### 00:42:56 · Speaker 2

Okay. uh Here is what I mean.

### 00:42:59 · Speaker 9

suppose you are generating or rather generating data like this. Let's say that I toss a coin, okay? And then if it's head, I will fill this pixel with one. If it's tail, I will fill that pixel with zero.

### 00:43:17 · Speaker 9

Do you understand what I'm doing? I'm tossing a coin, okay? And depending upon the outcome of that coin, I will decide to fill this particular pixel. Let's say that I have a grid of let's say twenty four by twenty four or twenty eight by twenty eight I think. M minus twenty eight by twenty eight. Now I'll fill these pixels, seven eighty four pixels like this. That I toss a coin. If it's head, I will fill that pixel with one. If it's tail, I will fill that pixel with zero.

### 00:43:48 · Speaker 9

Okay. The question is, what is the probability or likelihood that this procedure will generate MNIST data set?

### 00:43:59 · Speaker 2

Do you see the question? Do you understand the question?

### 00:44:10 · Speaker 2

Okay, uh, so now can somebody tell me what

### 00:44:12 · Speaker 9

What is the probability of generating a MNIST via this procedure?

### 00:44:19 · Speaker 4

should be very low.

### 00:44:20 · Speaker 9

it's really extremely low, right? There's actually called type typer monkey problem, right? Where say that you make a monkey sit on a typer and start typing randomly. Now, what is the likelihood that it will create Hamlet, right? Or Shakespeare's work? That is the question. Say that it's very, very low, right? I mean, similarly, getting a data set which is semantically meaningful like MNIST,

### 00:44:50 · Speaker 9

doing this procedure random procedure is is very very low. Now this means that out of all possible images uh binary images MNIST occupies a very very small space in uh seven eighty four dimensional space.

### 00:45:11 · Speaker 9

Do you see that?

### 00:45:14 · Speaker 9

See this this example was to show that out of all possible points in seven eighty four dimensional space, MNIST occupies a tiny region. That is what I have written here, right? Distributions over real data lies on a very small subspace or manifold in the ambient space RD.

### 00:45:36 · Speaker 9

Does it make sense?

### 00:45:39 · Speaker 9

So now what is the consequence of this? The consequence of this is this implies

### 00:45:44 · Speaker 2

Please

### 00:45:44 · Speaker 9

Hello

### 00:45:44 · Speaker 2

that

### 00:45:46 · Speaker 2

that there's a high chance

### 00:45:55 · Speaker 2

that

### 00:45:59 · Speaker 2

supports. supports meaning the points where the distributions are non zero, okay? that supports of

### 00:46:10 · Speaker 2

of P X and P theta are

### 00:46:17 · Speaker 2

North

### 00:46:20 · Speaker 2

like

### 00:46:23 · Speaker 2

H N P theta are yeah are not perfectly aligned

### 00:46:36 · Speaker 2

Right? Because we are talking about

### 00:46:38 · Speaker 9

of two distributions, right? uh in R D and we know that uh distributions of images are are actually supported on a very tiny space in R D. So if I take two distributions that are in R D, then their supports will not be perfectly aligned. Okay, there's a high chance of them being not perfectly aligned. Correct?

### 00:47:01 · Speaker 9

Now again, what is the consequence of this? This is, it can be shown that

### 00:47:08 · Speaker 9

to show

### 00:47:08 · Speaker 2

on

### 00:47:10 · Speaker 2

that. that.

### 00:47:14 · Speaker 2

that one can always find

### 00:47:20 · Speaker 2

Find

### 00:47:21 · Speaker 2

a perfect discriminator

### 00:47:30 · Speaker 2

screen reader.

### 00:47:34 · Speaker 2

which is that a D D W network with hundred percent accuracy.

### 00:47:44 · Speaker 2

accuracy. When, when

### 00:47:48 · Speaker 2

the supports of

### 00:47:54 · Speaker 2

p theta and px are not the same.

### 00:48:03 · Speaker 9

Right? So this is saying that okay, now if the supports of P X and P theta, they do not align perfectly or are not exactly the same, then you can always find a discriminator with hundred percent accuracy.

### 00:48:18 · Speaker 9

ओके। नाउ इफ यू फाइंड अ डिस्क्रिमिनेटर विथ हंड्रेड परसेंट एक्यूरेसी, व्हाट डस दिस इम्प्लाई? दिस इम्प्लाईस दैट, द ज्ञान ट्रेनिंग

### 00:48:31 · Speaker 2

saturates

### 00:48:35 · Speaker 2

the moment you

### 00:48:36 · Speaker 9

If you find the discriminator with 100% accuracy, there is no signal to the generator to learn, isn't it? Because it is perfectly classifying, that's all you are done.

### 00:48:47 · Speaker 9

Right? So Gyan training simply saturates and this is the reason, okay, why Gyan training becomes difficult. So let me tell you what I said. See the argument that is given is, first thing is that the data that is lying, I mean that that is that that occurs naturally like images and text and all that. They occupy a tiny manifold or tiny little space in the ambient space, okay. Now this means that the true data and the general related data

### 00:49:19 · Speaker 9

Okay? They both lie on tiny manifolds. And those tiny manifolds may not perfectly align. Okay? Now if they do not perfectly align, even if there is a single point where there is misalignment, then it can be shown that in such cases you can always find a discriminator that is perfect. Now once you find a perfect discriminator, okay? Then the GAN training simply saturates.

### 00:49:44 · Speaker 9

So this can also be said in a different way saying that this means that for

### 00:49:53 · Speaker 9

p x and p theta which

### 00:49:58 · Speaker 2

misaligned supports

### 00:50:03 · Speaker 2

misaligned supports

### 00:50:15 · Speaker 2

misaligned supports, okay? If you take any F divergence,

### 00:50:22 · Speaker 2

Okay.

### 00:50:23 · Speaker 9

this will be either infinity or some constant

### 00:50:30 · Speaker 9

Let me say it's a constant.

### 00:50:35 · Speaker 9

simply become a constant. Now it will what if it becomes constant this will become independent of theta. It becomes independent of theta then that's all right I mean Gantt training simply saturates because the divergence you are calculating is independent of theta and there is no way that you can learn learn more.

### 00:50:56 · Speaker 9

Okay, this is when mode collapse also happens. This happens all the time. So, the the respite or solution for this is, solution for this is

### 00:51:08 · Speaker 2

use a software metric

### 00:51:15 · Speaker 2

software divergence metric

### 00:51:22 · Speaker 2

Okay? That

### 00:51:26 · Speaker 2

that quantifies

### 00:51:30 · Speaker 2

How

### 00:51:32 · Speaker 2

close

### 00:51:34 · Speaker 2

the manifolds are

### 00:51:39 · Speaker 2

cold support manifolds are

### 00:51:46 · Speaker 2

supports of we are talking about P X and P theta, okay? Instead,

### 00:51:53 · Speaker 2

instead of, instead of

### 00:51:56 · Speaker 2

Just

### 00:51:59 · Speaker 2

measuring if they overlap or not.

### 00:52:06 · Speaker 2

they are perfectly aligned or not, okay?

### 00:52:17 · Speaker 2

is demotivation. So what we are saying

### 00:52:19 · Speaker 9

is that if the manifolds do not perfectly align, okay? Then all the f divergences that we saw simply will max out or rather become a constant which will become independent of theta and that's why Gantt turning saturates. Instead of that, it's better to have another metric, divergence metric that will tell you how

### 00:52:41 · Speaker 9

close or far the manifolds on which distributions are supported are. Instead of just making it a constant, in fact, whenever the manifolds do not align, you want that metric that you are that you are thinking of.

### 00:52:56 · Speaker 9

to just measure how far or close the manifolds are without, you know, just maxing out or becoming a constant.

### 00:53:04 · Speaker 9

So if this happens, right, what what we are saying is that, you know, you can't find a perfect discriminator and that is why the Gantt training does not saturate.

### 00:53:15 · Speaker 9

Okay? So we will see, I mean, this metric happens

### 00:53:18 · Speaker 2

to be that metric is what is called as the Versa stain symmetric.

### 00:53:29 · Speaker 2

so called as the optimal transport

### 00:53:38 · Speaker 2

which I'll define in a while. Yeah, before that, before we go to the definitions, I'll take questions on the

### 00:53:43 · Speaker 9

discussion so far. Any questions?

### 00:53:50 · Speaker 9

Yeah, Sanchit

### 00:53:52 · Speaker 7

सर, व्हाट, व्हाट डू वी मीन बाय द सपोर्ट हियर?

### 00:53:57 · Speaker 9

If you take a

### 00:53:58 · Speaker 2

Distribution supports are the points on which distribution is non-zero.

### 00:54:09 · Speaker 2

Uh

### 00:54:16 · Speaker 4

So like

### 00:54:16 · Speaker 2

like that

### 00:54:19 · Speaker 9

If you take a uniform distribution between let's say A and B, support of distribution is set A B.

### 00:54:28 · Speaker 9

on which the distribution is non zero.

### 00:54:33 · Speaker 9

Is it all right? So Gaussian distribution, right, will have infinite support, for instance.

### 00:54:39 · Speaker 9

it's a set, okay? it's a set over which the data has been observed.

### 00:54:45 · Speaker 2

Okay

### 00:54:51 · Speaker 2

Any other question?

### 00:55:01 · Speaker 2

या राघवेंद्र

### 00:55:03 · Speaker 11

Yes, so here we are only trying to say that if the supports match, then they are close enough. So we are not really looking at the divergence metric in addition.

### 00:55:12 · Speaker 9

No, in F divergence,

### 00:55:15 · Speaker 9

we we do compare distributions, okay? we saw that, right? we actually compare distributions, okay? but the thing is,

### 00:55:25 · Speaker 9

if the distributions the real I mean if the distribution that we are comparing uh will have mismatch okay in terms of non alignment then what this paper says is that you can always find a perfect discriminator and that's why training becomes unstable.

### 00:55:44 · Speaker 9

Okay, so you basically the motivation is that you need another alternative metric, okay? That is not over dependent on alignment of the supports of these distributions.

### 00:55:57 · Speaker 11

So I mean it's in in in addition to the divergence minimization or this is a separate way to optimize.

### 00:55:57 · Speaker 9

Okay

### 00:56:04 · Speaker 9

Uh see you minimize the divergence only basically you minimize the divergence but the divergence metric that you are coming up with is not sensitive to misalignment between supports that's all.

### 00:56:17 · Speaker 4

Okay

### 00:56:19 · Speaker 9

Okay, so mass strain metric is also a divergence minimization metric only.

### 00:56:24 · Speaker 2

So so given two distributions

### 00:56:38 · Speaker 2

px and p theta. The versus tens metric between them is defined as follows.

### 00:56:50 · Speaker 2

keeping some

### 00:56:51 · Speaker 2

details here because you know

### 00:56:52 · Speaker 2

don't have a lot of time so this is metric is given as the minimum

### 00:56:59 · Speaker 2

of

### 00:57:01 · Speaker 2

expectation of

### 00:57:12 · Speaker 2

the two norm and this expectation is over.

### 00:57:17 · Speaker 2

x and x square they come from

### 00:57:23 · Speaker 9

some new and this minimization is all new, okay? which belongs to a joint distribution between P X and P Z. I will explain all this.

### 00:57:36 · Speaker 2

write that down and then explain.

### 00:57:55 · Speaker 2

This is the definition of the versus signs

### 00:57:58 · Speaker 9

distance, okay. Okay, I'll tell you what this means. Now suppose there are two discrete distributions, okay.

### 00:58:08 · Speaker 9

I'll do it in one dimensions to ensure that the idea is clear. So let's say that this is X. There is another distribution which is

### 00:58:17 · Speaker 2

Histogram

### 00:58:22 · Speaker 2

x cap. Let's say that this is this is px and this is px cap or p theta.

### 00:58:33 · Speaker 2

Okay? Now

### 00:58:39 · Speaker 2

Now

### 00:58:41 · Speaker 2

The mass

### 00:58:45 · Speaker 2

in P X. P X.

### 00:58:48 · Speaker 2

Can be

### 00:58:50 · Speaker 2

redistributed

### 00:58:59 · Speaker 2

such that

### 00:59:02 · Speaker 2

it transforms

### 00:59:06 · Speaker 2

to P theta. Do you agree?

### 00:59:10 · Speaker 9

the mass in P X can be redistributed, okay, such that it will transform to morph into P theta. Do you agree? How do we do that?

### 00:59:26 · Speaker 9

set like this. How do we do that? We take let's say that this is this is x one and this is some x k. You take some mass from x x one and uh reduce it and put it to x two and so on, right? I mean...

### 00:59:43 · Speaker 9

यू कैन रीडिस्ट्रीब्यूट द मास इन पीएक्स सो दैट इट विल गेट ट्रांसफॉर्म्ड टू पी थीटा। इज़ंट इट? डू यू एग्री?

### 00:59:54 · Speaker 7

Sir, but usually we are not supposed to touch X, right? So it's like a source distribution.

### 01:00:00 · Speaker 3

is what? No no no, see forget about source and target and all that now. I'm just simply saying given two distributions, you can always change the the distribute mass in one distribution to get get it morphed into some other distribution, correct?

### 01:00:18 · Speaker 2

Correct

### 01:00:19 · Speaker 3

Now,

### 01:00:20 · Speaker 2

fingers

### 01:00:22 · Speaker 2

Now this redistribution

### 01:00:31 · Speaker 0

redistribution can be expressed

### 01:00:39 · Speaker 0

Yeah, can be expressed.

### 01:00:44 · Speaker 0

as a table

### 01:00:47 · Speaker 3

let's say that this has this has k and this is x cap one two x cap

### 01:00:57 · Speaker 2

tell okay. Now I will write a

### 01:01:06 · Speaker 2

table, okay? In this direction this is x l sorry.

### 01:01:10 · Speaker 3

X cap

### 01:01:12 · Speaker 3

in this direction it is X. Now this is X one through X K and this is

### 01:01:23 · Speaker 3

it's one cap through

### 01:01:27 · Speaker 3

Sorry

### 01:01:28 · Speaker 3

Right? So what I'm saying is, how much mass should I take from X1 and should I put it in let's say here. So let's say that I put 0.3% of X1 here and I put 0.2% of it and I'll write 0.01% of X1 here and then redistribute amongst all X1 cap through XL. Same thing with X X2 also, right? I take 0.1% and 0.4% and 0.02% and so on.

### 01:01:58 · Speaker 3

Do you see that? So what I'm saying is every row here is telling me how much mass, how should I redistribute one x k, okay, amongst all possible x caps such that it will get transformed to x, I mean

### 01:02:15 · Speaker 2

theta. Do you agree?

### 01:02:25 · Speaker 2

and every row should sum

### 01:02:27 · Speaker 3

to one, right? Because you can mean the total mass on X one should sum to one, correct? So now this, right? What is this? If you closely look at it, is actually a

### 01:02:38 · Speaker 2

Joint Distribution

### 01:02:45 · Speaker 2

joint distribution between

### 01:02:48 · Speaker 2

px and p theta

### 01:02:52 · Speaker 2

shall I call it as P X cap

### 01:02:56 · Speaker 2

it's okay you understand no its cap is coming

### 01:02:59 · Speaker 3

from P theta

### 01:03:03 · Speaker 3

Is this okay? P X is sampled from P X is sampled from P X here and X cap is sampled from P theta. So this table, okay, which will tell you how to redistribute

### 01:03:18 · Speaker 3

एक्स टू पीएक्स टू गेट मॉर्फ्ड इंटू पी थीटा इज़ एक्चुअली अ जॉइंट डिस्ट्रीब्यूशन बिटवीन पीएक्स एंड पी थीटा।

### 01:03:27 · Speaker 2

agreed? Any questions so far?

### 01:03:36 · Speaker 2

Yeah, Abhitosh. Write this down.

### 01:03:37 · Speaker 1

right

### 01:03:38 · Speaker 1

shouldn't it be the reverse that you are trying to sum adjust P theta so that it becomes equal to P X or is it because you do not know

### 01:03:46 · Speaker 3

No no no it's uh no no no see again I'm telling forget about it for a while no you you you forget what is P theta what is P H there's two distributions. Of course you can write it that way right I mean you say that P theta is being adjusted in Gyan framework that is what you are trying to say right. Yeah yeah. But in general doesn't matter no in general I'm defining divergence metric between two distributions can mean anything.

### 01:04:02 · Speaker 2

but

### 01:04:11 · Speaker 0

Okay

### 01:04:12 · Speaker 3

That is why if it's confusing for you

### 01:04:14 · Speaker 0

Let me

### 01:04:16 · Speaker 0

Change it

### 01:04:25 · Speaker 2

there is no

### 01:04:28 · Speaker 2

find and replace here. So you have to do it manually.

### 01:04:32 · Speaker 0

Okay

### 01:04:55 · Speaker 0

Any other questions on this?

### 01:04:58 · Speaker 0

So

### 01:04:59 · Speaker 3

joint distribution between

### 01:05:03 · Speaker 3

between P X and P theta, P X cap now, P X cap, okay? specifies

### 01:05:12 · Speaker 3

specifies a

### 01:05:13 · Speaker 2

transport plan. It's called a transport plan.

### 01:05:22 · Speaker 2

transport plan, okay?

### 01:05:25 · Speaker 2

Between

### 01:05:26 · Speaker 3

px and px cap

### 01:05:29 · Speaker 3

So now if you give me a joint distribution between P X and P X and P X cap, I'm simply saying every joint distribution is telling me how to convert or redistribute masses in P X such that it gets mapped to P X cap. Do you agree?

### 01:05:43 · Speaker 0

okay

### 01:05:53 · Speaker 0

Now

### 01:05:55 · Speaker 0

suppose

### 01:05:59 · Speaker 0

Okay

### 01:05:59 · Speaker 2

suppose I move suppose a mass

### 01:06:05 · Speaker 2

X cap, okay? Is, or rather X is moved

### 01:06:12 · Speaker 2

X is moved to X cap.

### 01:06:17 · Speaker 2

mood 2x square, right? Then

### 01:06:20 · Speaker 2

norm between x and x cap

### 01:06:23 · Speaker 2

gives you the distance

### 01:06:27 · Speaker 2

of movement

### 01:06:31 · Speaker 2

And if you evaluate

### 01:06:35 · Speaker 2

the joint distribution at these points x and x cap give the mass

### 01:06:43 · Speaker 2

That was mode

### 01:06:49 · Speaker 2

Right

### 01:06:49 · Speaker 3

this much of mass was moved, this much of distance. So now

### 01:06:55 · Speaker 3

P X X cap which is the joint distribution between these two. If you multiply this

### 01:07:02 · Speaker 3

with this thing.

### 01:07:04 · Speaker 3

So what is distance times mass?

### 01:07:09 · Speaker 2

It's the

### 01:07:10 · Speaker 0

work done, right?

### 01:07:16 · Speaker 0

in moving

### 01:07:19 · Speaker 0

the mass

### 01:07:23 · Speaker 0

by a distance of x minus x cap.

### 01:07:37 · Speaker 0

Correct?

### 01:07:39 · Speaker 0

the mass into distance

### 01:07:40 · Speaker 3

is the work done right by definition. Now if I take

### 01:07:46 · Speaker 3

integrate this.

### 01:07:47 · Speaker 0

okay? Over the entire joint distribution

### 01:08:09 · Speaker 0

What will this give me?

### 01:08:12 · Speaker 0

This is by definition the expectation of

### 01:08:17 · Speaker 2

over the joint distribution of P X X cap. What is this? This is the this is the average work done.

### 01:08:29 · Speaker 0

Hmm

### 01:08:32 · Speaker 0

in a transport plan

### 01:08:40 · Speaker 0

specified by

### 01:08:48 · Speaker 0

Do you agree?

### 01:08:52 · Speaker 0

Now,

### 01:08:52 · Speaker 3

every joint distribution between X and X cap will give me a transport plan, right? uh which would tell me uh how to transform one distribution to the other, correct? Now

### 01:09:07 · Speaker 3

if I I mean uh if I multiply right if I take the expected value of uh the distance between uh the supports okay over the joint distribution it will tell me the average work done in a transport plan that is specified by the joint distribution.

### 01:09:24 · Speaker 0

Everybody agree on this?

### 01:09:35 · Speaker 0

Hello

### 01:09:37 · Speaker 2

Am I audible?

### 01:09:40 · Speaker 2

Hello

### 01:09:40 · Speaker 0

Yes sir. Yes sir.

### 01:09:42 · Speaker 2

Okay, is this clear? Okay. Now, the question that I'm asking is,

### 01:09:48 · Speaker 2

Given

### 01:09:53 · Speaker 0

multiple transport plans that are possible.

### 01:10:03 · Speaker 0

every transport plan is a joint distribution mind you, right?

### 01:10:07 · Speaker 0

and distributions, okay, possible.

### 01:10:15 · Speaker 0

between two random variables x and x cap, okay? Now,

### 01:10:25 · Speaker 0

which one

### 01:10:28 · Speaker 0

has the least work done.

### 01:10:37 · Speaker 0

in other words

### 01:10:44 · Speaker 0

other words, what is

### 01:10:48 · Speaker 0

what is the least work done

### 01:10:55 · Speaker 0

Okay. To transform

### 01:11:02 · Speaker 0

px to

### 01:11:04 · Speaker 3

Okay

### 01:11:06 · Speaker 3

How do you specify this? So now what you do is that if you take a joint distribution new, okay?

### 01:11:15 · Speaker 3

which is a joint distribution between X and X cap. Okay? This will give you the work done

### 01:11:22 · Speaker 3

via that joint distribution. Now amongst all possible transport plans or the joint distribution that will take P X to P cap. Give me the one, okay? So here...

### 01:11:37 · Speaker 3

Five

### 01:11:37 · Speaker 2

okay represents represents

### 01:11:43 · Speaker 0

set of all possible joint distributions between X and X cap.

### 01:11:53 · Speaker 0

All possible

### 01:11:58 · Speaker 0

joint institutions or transport plants, right?

### 01:12:04 · Speaker 0

So they will

### 01:12:04 · Speaker 2

joint distribution is a transport plan

### 01:12:10 · Speaker 2

between x and x cap.

### 01:12:13 · Speaker 2

this is seeking, what is this seeking? this is seeking the least

### 01:12:21 · Speaker 0

rather the

### 01:12:24 · Speaker 0

Transport Plan

### 01:12:30 · Speaker 0

But

### 01:12:32 · Speaker 0

की लीस्ट एवरेज वर्क

### 01:12:46 · Speaker 0

Do you see this?

### 01:12:48 · Speaker 3

So I'm

### 01:12:48 · Speaker 2

Same

### 01:12:48 · Speaker 3

amongst all possible joint distributions or amongst all possible ways that I can transform my P X to P X cap. Give me the one, right? That corresponds to the least work done.

### 01:13:05 · Speaker 0

Do you agree? Do you see this?

### 01:13:17 · Speaker 0

Now

### 01:13:20 · Speaker 0

This is what is called as the versus strains distance.

### 01:13:25 · Speaker 0

Versus 10's distance

### 01:13:26 · Speaker 2

between

### 01:13:32 · Speaker 2

two distribution

### 01:13:32 · Speaker 3

px and px cap

### 01:13:36 · Speaker 3

is the minimum, okay? And please note the minimization is over. Minimization is over all possible transport plans, okay? That would transform P X to P X cap. Now the question that I'm asking is amongst new is

### 01:13:55 · Speaker 2

joint distribution between

### 01:13:58 · Speaker 2

you belongs to

### 01:14:03 · Speaker 2

set pi okay is a joint distribution

### 01:14:11 · Speaker 2

between

### 01:14:13 · Speaker 2

एक्स एंड एक्स का

### 01:14:15 · Speaker 2

So

### 01:14:16 · Speaker 3

amongst all possible joint distributions that would transform P X to P X cap. Give me the one that has the least work done. So that is the versitantes distance. Now you can see that

### 01:14:33 · Speaker 3

lesser

### 01:14:33 · Speaker 3

the versus trains distance

### 01:14:35 · Speaker 3

Okay

### 01:14:39 · Speaker 3

closer are P X and P cap, isn't it?

### 01:14:43 · Speaker 3

because if PX and PX cap are closed, okay, then the amount of work that you should do to bring PX to PX cap will be least. Now there can be other transport plans that would, I mean, even if PX and PX cap are closed, there can exist transport plans, right, that would have a, that would, that would involve a lot of work, but since we are seeking the minimum work done to to transform PX to PX cap, if they are closing then you don't have to do a lot of work to transform PX to PX cap.

### 01:15:18 · Speaker 3

That's why it's a distance metric between two distributions.

### 01:15:24 · Speaker 3

So this is also called that's why it's also called no. Optimal transport versus strength metric is also called as optimal transport.

### 01:15:36 · Speaker 0

Any questions on the definition?

### 01:15:50 · Speaker 0

Hello? Is there any question?

### 01:15:59 · Speaker 2

Hello

### 01:15:59 · Speaker 1

not now school

### 01:16:01 · Speaker 3

Am I audible?

### 01:16:03 · Speaker 3

Yes sir

### 01:16:04 · Speaker 1

Yes

### 01:16:05 · Speaker 1

Yes sir

### 01:16:06 · Speaker 3

Okay, great. Okay. So now this is shown to be a a softer metric, right? So versus strain distance is a softer metric, okay, compared to

### 01:16:24 · Speaker 0

compared to F divergence.

### 01:16:28 · Speaker 0

in the sense that

### 01:16:31 · Speaker 0

in that

### 01:16:33 · Speaker 0

it will not

### 01:16:37 · Speaker 0

not max out, right? Or saturate.

### 01:16:47 · Speaker 0

Saturate

### 01:16:50 · Speaker 0

with misalignment. Okay. What is the

### 01:16:58 · Speaker 3

misalignment of the supports. This is the greatest thing, right? I mean, that you can use the versus ten's metric, uh to, I mean, it will become much stabiler if you use versus ten's metric. Now, how is this related to adversarial learning? Is that? So the next question is, I'll

### 01:17:18 · Speaker 3

continue the class till eleven fifteen, right? And then we will take a ten minutes break. Okay, let's finish this. The question is, how to

### 01:17:27 · Speaker 0

to build a generative model

### 01:17:35 · Speaker 0

Okay

### 01:17:37 · Speaker 0

that

### 01:17:40 · Speaker 0

Top

### 01:17:40 · Speaker 3

optimizes the versus range metric. Okay, this is a good metric fine. Now how do we build a generative model that would

### 01:17:48 · Speaker 3

optimizes the versus tens metric.

### 01:17:54 · Speaker 3

So thankfully there exists this uh this duality okay which is called the the Kontrovich Rubinstein's duality.

### 01:18:04 · Speaker 2

P

### 01:18:12 · Speaker 2

that says that versus

### 01:18:14 · Speaker 3

sustains distance between two distributions P X and P theta, okay, can be expressed as a maximum, okay, over

### 01:18:25 · Speaker 0

set of functions. Let's call them as T W.

### 01:18:36 · Speaker 0

which are like this I'll tell you what this is. So this is

### 01:18:41 · Speaker 0

expectation

### 01:18:44 · Speaker 2

x coming from px

### 01:18:47 · Speaker 2

simply T W of X minus

### 01:18:53 · Speaker 2

expectation of

### 01:18:56 · Speaker 2

its cap coming from V theta

### 01:19:00 · Speaker 2

to have again T W

### 01:19:02 · Speaker 0

Topics

### 01:19:09 · Speaker 0

Right? So now you know, right? I mean this, So now if you want to minimize

### 01:19:22 · Speaker 0

theta, just simply you have a min

### 01:19:27 · Speaker 3

over theta

### 01:19:30 · Speaker 3

and versus tension is simply a match over this T W.

### 01:19:34 · Speaker 3

I'll tell you what this norm of T W less than this means. And you have this usual

### 01:19:41 · Speaker 3

fast right which

### 01:19:43 · Speaker 3

we know how to approximate

### 01:19:45 · Speaker 0

using sample estimates.

### 01:19:50 · Speaker 0

it's got sorry. it's got

### 01:19:58 · Speaker 0

Hello

### 01:19:58 · Speaker 2

from P theta

### 01:20:01 · Speaker 2

Right? So now this what is this? Again this becomes this became a a do serial optimization.

### 01:20:14 · Speaker 2

How do you optimize this? Same thing you have

### 01:20:18 · Speaker 2

generator

### 01:20:19 · Speaker 3

network which will

### 01:20:23 · Speaker 2

एक गेट

### 01:20:24 · Speaker 3

take a G

### 01:20:26 · Speaker 3

and gives you x cap coming from v theta,

### 01:20:30 · Speaker 2

story and you have this critique network here

### 01:20:37 · Speaker 2

p w of x right.

### 01:20:42 · Speaker 3

your real number in this case and this is

### 01:20:47 · Speaker 3

either x or you have x cap that goes as input because you you have to compute the expectation over both of that. right? and then the only constraint is that the t network right have to be one lip sheets.

### 01:21:04 · Speaker 2

So what is meant by that I will just tell you.

### 01:21:12 · Speaker 2

implies that if you take T W of

### 01:21:16 · Speaker 3

x one minus p w of x two

### 01:21:22 · Speaker 3

divided by

### 01:21:24 · Speaker 3

x one minus x two. This is upper bounded by one. This is the definition of one lipset.

### 01:21:32 · Speaker 3

So, when if you look at it, it is exactly a GAN, right? Optimizing the verstance distance is exactly a GAN. That's why it's called a W GAN. The only thing is the discriminator network, right? Or the critique network have to be one lipsets.

### 01:21:49 · Speaker 3

Of course, the the the

### 01:21:54 · Speaker 3

form of the uh the uh loss function changes a little because there you have the expectation of F star of T W here you don't have that F function right otherwise it is simply a an adversarial optimization problem that you are solving right but with only one additional constraint that the discriminator network have to have bounded derivatives right or it should be one left shift now how do you make a neural network one left shift is a question that I'll answer in a but yeah so but for that it is simply again with

### 01:22:30 · Speaker 3

uh with with the objective function taking expectations over two distributions and then you optimize. The advantage is in a GAN, right, what happens is or an F divergence minimizer, this maximization that you are constructing, no, is actually a lower bound on the divergence. But here there is an equality, you see. If the persistence metric is exactly equal to this maximization problem, which is again, no, that's what makes it a softer metric.

### 01:22:58 · Speaker 3

Now the the uh the practical implication of this is whenever you are implementing a Gyan right always implement a W Gyan because it is much more stable in terms of training. Okay even for your assignment no question one and two I would recommend that you implement a W Gyan so now how does it change? The only thing that it changes this will not be between zero and one now it will simply you will have a linear uh thing uh activation at the output.

### 01:23:31 · Speaker 3

linear activation, okay?

### 01:23:34 · Speaker 3

The loss function will not have log of d of g or something it will simply have the output of this. It will be expectation of the output of this so this will be a the this this is the output of this network okay. That's one thing the other thing is you'll have to ensure that the discriminator network is Lipschitz so now to practically

### 01:23:57 · Speaker 0

what you do is that you

### 01:24:01 · Speaker 0

normalize

### 01:24:04 · Speaker 0

the weights.

### 01:24:08 · Speaker 0

of T W

### 01:24:11 · Speaker 0

Okay

### 01:24:15 · Speaker 3

such that their norm is always one. If you do this then it will become one lipset. So what you what you should do is after every uh gradient step, right?

### 01:24:28 · Speaker 3

after every gradient step

### 01:24:34 · Speaker 3

every gradient update. So after every gradient update, what you do is take the weights update. Take the weights of the discriminator network and normalize them so that they will have

### 01:24:46 · Speaker 3

unit now. If you do that, it will become one leap sheet. That's all. That is the only thing that you should do while you are training the versus trines. And this is shown to be much more stable for training and it will give you much better like outcomes compared to F divergence minimization. Even though this also happens to be a sad point on adversarial optimization, okay? With the only constraint that you should have the discriminator to be one leap sheet.

### 01:25:15 · Speaker 3

Okay? That's about W Gyan. Any questions?

### 01:25:18 · Speaker 2

on this

### 01:25:24 · Speaker 2

Yes, Go on, Raghavendra.

### 01:25:26 · Speaker 4

Yes, so the norm that we are talking about here is the L two norm or

### 01:25:30 · Speaker 2

Where

### 01:25:31 · Speaker 3

Here, yeah, yeah, this is L2. This is L2. This is, this is L2. Yeah.

### 01:25:38 · Speaker 3

It's good that you asked that question, right? Here, when we define the Verstein's metric, it's always uh two that we talk about here, right? The two norm between x and x cap. Okay? And the the this duality, you know, the control which is Rubinstein's duality is called Verstein's two. In general, you can use a pth norm here. If you do one norm here, that will become Verstein's one. If you if you use two norm, it will become Verstein's two. If you use p norm, it will become p Verstein's distance in general. But generally,

### 01:26:08 · Speaker 3

versus strains two is what is used everywhere and the duality rate or the Gann formulation comes up for versus strains two

### 01:26:18 · Speaker 3

all right?

### 01:26:18 · Speaker 4

Okay, so the duality applies only to

### 01:26:20 · Speaker 2

versus

### 01:26:21 · Speaker 2

Divya

### 01:26:21 · Speaker 3

the versus tense two. Yeah.

### 01:26:29 · Speaker 3

Sarvesh

### 01:26:31 · Speaker 4

as for calculating the norm of the network, we just have to put all the weights in a vector in any order and then just calculate the norm, right?

### 01:26:38 · Speaker 3

Yeah, yeah, yeah, yeah, yeah, yeah. Simply vectorize it, compute the norm and divide it by the norm of it. You don't have to compute it, no, just divide the weights, every individual weight with with its norm.

### 01:26:50 · Speaker 4

ओके। एंड इट वर्क्स फॉर एवरी नेटवर्क एट कॉन्वल्युशन आल्सो सेम, सेम। या, या, सेम।

### 01:26:54 · Speaker 3

Yeah, same thing, same thing. Yeah, yeah.

### 01:26:56 · Speaker 4

Thank you

### 01:26:59 · Speaker 3

Okay, nothing else, right? I mean this, see, uh whenever you implement a Gyan, always implement a W Gyan, much more stable. Okay. Okay, the final piece before we close Gyan is like how do you evaluate?

### 01:27:17 · Speaker 3

generate generative evaluate gyan right typically

### 01:27:23 · Speaker 3

This is

### 01:27:24 · Speaker 0

I should not be calling it as GANs, you can do it for any generative model.

### 01:27:36 · Speaker 0

Now given

### 01:27:40 · Speaker 0

X one through X N.

### 01:27:43 · Speaker 0

sample from some distribution P X

### 01:27:45 · Speaker 2

typically the real data

### 01:27:51 · Speaker 2

and you have

### 01:27:54 · Speaker 2

one cap through

### 01:27:56 · Speaker 2

back.

### 01:27:59 · Speaker 2

This is sampled from P theta star is like generated data post training of course, right?

### 01:28:13 · Speaker 0

Now the goal

### 01:28:20 · Speaker 0

compare the closeness.

### 01:28:22 · Speaker 0

it's called this as

### 01:28:25 · Speaker 3

the real and degenerated, okay? compare DR and DG. Now how do you compare these two? You need a metric, no, to compare these two. Of course, now you need to resort to some distributional divergence metric only, no, to compare DR and DG. What is done is typically, uh one there are multiple metrics to do it. One of the famous metrics is what is called as the Freschert's inception distance.

### 01:29:02 · Speaker 0

It's called

### 01:29:17 · Speaker 0

abbreviated as FI

### 01:29:18 · Speaker 3

ID

### 01:29:19 · Speaker 3

might have seen no F I D is the metric that is used to evaluate the quality of generated data. So what is this? At the heart of it F I D

### 01:29:32 · Speaker 3

is simply

### 01:29:34 · Speaker 3

sustainable metric

### 01:29:36 · Speaker 3

okay

### 01:29:42 · Speaker 3

simply was a sustance metric between uh like P X cap and P theta cap but it is done in a convoluted way I'll tell you what what is done. So what is done in F I D is that first step is

### 01:29:59 · Speaker 2

Take

### 01:30:01 · Speaker 2

samples of

### 01:30:06 · Speaker 0

DR and DG

### 01:30:09 · Speaker 0

Now pass them through

### 01:30:18 · Speaker 0

Astram two, an inception

### 01:30:20 · Speaker 3

network a pre-trained infection infection inception through an inception net that's why the name inception distance okay inception network

### 01:30:34 · Speaker 3

Network

### 01:30:35 · Speaker 0

Pre-trained

### 01:30:39 · Speaker 0

on ImageNet

### 01:30:44 · Speaker 0

Okay. So then take

### 01:30:49 · Speaker 0

the features

### 01:30:55 · Speaker 0

from some

### 01:30:57 · Speaker 3

eighth layer. See, some different people take it different layers. I think, you know, example is sixty fourth layer.

### 01:31:07 · Speaker 3

Okay? Now what was done so far is that

### 01:31:10 · Speaker 0

to have a pre-trained inception network

### 01:31:22 · Speaker 0

Okay

### 01:31:23 · Speaker 3

Now you pass your X and X cap both through this and take the features at some sixty fourth layer right this is you call this as uh Z real and you know Z generated.

### 01:31:39 · Speaker 3

Okay? Then now you will have two data sets, right? Let's call that as uh D

### 01:31:45 · Speaker 3

cap real which is

### 01:31:49 · Speaker 3

zero one zero two up to zero n and you have d

### 01:31:58 · Speaker 3

generated cap which is C generated one, Z generated two and Z generated N. So here Z R I is

### 01:32:18 · Speaker 3

let's call this as some fee, okay? So now fee at sixty fourth layer of

### 01:32:25 · Speaker 3

Z I X I and Z G I is phi at sixty four of X cap I okay where phi is the

### 01:32:39 · Speaker 0

is the pre-trained inception net, okay?

### 01:32:49 · Speaker 0

So for

### 01:32:49 · Speaker 3

were so good. Any questions on this?

### 01:32:52 · Speaker 3

given data, real data and generated data, take a pre-trained inception network, okay? pass both of them through that and take the sixty fourth layer features of both of them and collect them as vectors. you get two sets. is this okay so far?

### 01:33:11 · Speaker 2

Okay, now what you do is this is the third step. The fourth step is that

### 01:33:18 · Speaker 2

Compute

### 01:33:22 · Speaker 2

mean and variance, okay? for

### 01:33:27 · Speaker 2

D R cap and D G cap.

### 01:33:31 · Speaker 2

Let's call this as mu

### 01:33:34 · Speaker 0

real. Okay?

### 01:33:37 · Speaker 0

and sigma real

### 01:33:46 · Speaker 0

mute mu real on z real

### 01:33:50 · Speaker 3

you compute sigma real on Z real. you compute mu generated on Z generated. compute sigma generated on

### 01:34:02 · Speaker 2

Well, right, right.

### 01:34:04 · Speaker 0

Is it okay?

### 01:34:10 · Speaker 0

Now the fifth step is that

### 01:34:16 · Speaker 2

assume, assume, okay?

### 01:34:20 · Speaker 2

Z real and Z

### 01:34:24 · Speaker 3

generated both to be coming from Gaussian distributions

### 01:34:32 · Speaker 3

Z real comes from Gaussian with

### 01:34:37 · Speaker 3

mu real and sigma real and z g comes from a Gaussian

### 01:34:43 · Speaker 3

from mu g and sigma g.

### 01:34:48 · Speaker 3

Okay

### 01:34:50 · Speaker 3

Then finally you compute the versus strains metric.

### 01:34:55 · Speaker 3

Between

### 01:34:56 · Speaker 3

normal distribution

### 01:34:57 · Speaker 0

at mu real sigma real

### 01:35:02 · Speaker 0

and

### 01:35:10 · Speaker 0

So this is F I D.

### 01:35:19 · Speaker 0

Is this clear how to do it?

### 01:35:22 · Speaker 3

Now I'll tell you this is this actually is given by a formula.

### 01:35:27 · Speaker 3

versus strain distance between two Gaussian distributions is given by the simple formula. minus mu g

### 01:35:37 · Speaker 3

some two squared plus the trace of

### 01:35:43 · Speaker 3

sigma real plus sigma generated dash minus two sigma real sigma generated dash to the power of half.

### 01:35:57 · Speaker 3

See, this is a scalar, it's a norm.

### 01:36:01 · Speaker 3

Okay? And this is a trace, no? Trace of a matrix is also a scalar. Okay? And therefore, this is the F I D which will be a a scalar.

### 01:36:15 · Speaker 3

So this loss sustains two metric no scalar. uh So this is lower the better.

### 01:36:21 · Speaker 3

two distributions match then it will be zero because it is versus distance between two Gaussian distribution. lower the better.

### 01:36:28 · Speaker 0

between

### 01:36:39 · Speaker 0

That's it. Let me show you the entire procedure.

### 01:36:44 · Speaker 3

Have a look at it. Okay? And let me know if you have questions on F I D. So this is the metric that is used to one of the metrics that is used to uh quantify the goodness of generated data. Be it from GANs or V I E Rs or anything you can compute F I D. So what is F I D? Let me take quickly go through the steps now.

### 01:37:04 · Speaker 3

Now you have samples from the generated and the real data, pass it through a pre-trained instruction network to get the features. I mean, I'm not sure if it's sixty fourth layer or something. I'll some people, different people use different layers anyway. Okay. uh So now once you get those features, assume that those features follow Gaussian distribution and compute the mean and variances of them.

### 01:37:31 · Speaker 3

and use those mean and variances to compute the versus times two metric between these two features of real data and generated data using this formula that is your FID.

### 01:37:43 · Speaker 3

Any questions on the computation of F I D?

### 01:37:46 · Speaker 3

I've asked you to compute F I D, right? uh on the the data that you generate using GAN. So this is the formula that you should implement. There are standard implementations of F I D as well. Yeah, but this is what they do. Okay, Sarvesh.

### 01:38:02 · Speaker 4

Sir, what is sigma g prime?

### 01:38:07 · Speaker 0

Oh sorry, the sigma g only. Yeah.

### 01:38:18 · Speaker 0

Okay

### 01:38:19 · Speaker 0

क्या विवेक

### 01:38:21 · Speaker 2

So I have two questions

### 01:38:22 · Speaker 4

questions one is why why did you place so much of importance on one particular inception architecture

### 01:38:28 · Speaker 3

I didn't, I mean somebody did because in if you read the F I D paper what they say is inception architecture uh correlates well with human perception is what they have done by doing some perception studies.

### 01:38:41 · Speaker 4

Okay, okay. Uh, okay. Uh, second question is suppose I, I am modifying the problem a little bit and I ask, uh, like I want to see the inception, I mean the, uh, the distance between, uh, generated images, uh, of a given style.

### 01:38:43 · Speaker 3

Okay

### 01:38:59 · Speaker 4

Like if I'm not going to focus on content at all and I just want to focus on style. So can I modify the uh just I mean picking up the sixty fourth layer feature vectors and uh instead replace them with uh maybe the uh gram matrix or the adda in layer activations I mean and continue with the same procedure will I get a meaningful result?

### 01:39:26 · Speaker 3

It is not FID, uh but yeah, so it is it is something, right? I mean, you might get some meaningful result, but it's not FID by definition, that's all. You can't, you can't say that it's the it's the uh it's the standard FID metric.

### 01:39:44 · Speaker 3

But that does make sense.

### 01:39:44 · Speaker 4

but it is like

### 01:39:47 · Speaker 4

ओके, फाइन। आई मीन, द एक्चुअल प्रॉब्लम इज आई वांट टू रेकमेंड इमेजज टू।

### 01:39:51 · Speaker 3

Vivek, yeah, yeah, I understand. So, so shall we take it offline because it may not be relevant to the class? Okay. Please ping me, you know, we can discuss over that. Okay, any other question on F I D? Okay, so this, this is the

### 01:39:52 · Speaker 4

I understand

### 01:39:55 · Speaker 4

Yes, yes, yes. May not

### 01:40:13 · Speaker 3

end of GANs for this course. I mean there are too many things that are there. Yeah, this is the end of generative adversarial networks. Let's move on to VEs. uh Yeah, so

### 01:40:27 · Speaker 3

Okay, so we come to the end of Gyaans then. So let's move on to the next topic which is variation autoencoders. Shall we take a break?

### 01:40:39 · Speaker 0

etcetera

### 01:40:40 · Speaker 2

Okay

### 01:40:41 · Speaker 3

Okay

### 01:40:44 · Speaker 3

How long

### 01:40:44 · Speaker 3

is eleven eighteen. Shall we come back at, yeah, Sandeep?

### 01:40:51 · Speaker 3

I think. Yeah, so we'll come back at eleven thirty five.

### 01:40:56 · Speaker 3

and go up to twelve twenty perhaps and then we'll stop. eleven thirty five okay? fifteen minutes.

### 01:41:04 · Speaker 0

ओके, सी यू इन द बाय, बाय।

### 01:59:45 · Speaker 0

Hello Shall we resume?

### 01:59:55 · Speaker 2

Yes sir

### 01:59:58 · Speaker 0

Okay

### 02:00:05 · Speaker 6

Okay. The next class of generative models that we would consider are these variation autoencoders or VAEs. Okay. Now, these come under a broad family of models called

### 02:00:24 · Speaker 9

latent variable models

### 02:00:41 · Speaker 9

okay, latent variable models. So what do you mean by a latent variable model is that you have theta.

### 02:00:52 · Speaker 3

E

### 02:00:57 · Speaker 9

is what our starting point is, right?

### 02:01:05 · Speaker 9

as usual

### 02:01:07 · Speaker 6

IID from an unknown distribution P X. Okay. Now if suppose P theta of X denotes a model, what is a model? Model is basically a distribution over theta, right? Suppose P theta

### 02:01:24 · Speaker 9

denotes

### 02:01:29 · Speaker 9

model

### 02:01:33 · Speaker 9

a latent variable model is the following

### 02:01:45 · Speaker 9

defined as follows. P theta of X

### 02:01:50 · Speaker 9

Pace

### 02:01:50 · Speaker 6

given as a marginal

### 02:01:56 · Speaker 6

over the joint distribution of the data and another variable Z where Z is another

### 02:02:07 · Speaker 6

is

### 02:02:09 · Speaker 9

safe

### 02:02:11 · Speaker 9

is a hidden

### 02:02:13 · Speaker 9

So I'd name latent variable okay. Hidden or unobserved.

### 02:02:22 · Speaker 9

unobserved random variable

### 02:02:32 · Speaker 9

or this is integral

### 02:02:41 · Speaker 9

if it's continuous, okay? if Z is discrete, hold on.

### 02:03:05 · Speaker 9

to move that anyway.

### 02:03:08 · Speaker 9

I actually wanted let's do that.

### 02:03:15 · Speaker 9

Best

### 02:03:19 · Speaker 9

So this if

### 02:03:23 · Speaker 9

is discrete

### 02:03:29 · Speaker 9

C is continuous.

### 02:03:36 · Speaker 9

Okay. Now where Z is a hidden

### 02:03:44 · Speaker 9

or unobserved random variable.

### 02:03:58 · Speaker 9

Okay, so this is the definition of a latent variable model where

### 02:04:02 · Speaker 6

you express your data, okay, in terms of

### 02:04:07 · Speaker 6

marginal, okay, over the joint distribution of

### 02:04:14 · Speaker 6

joint distribution between the data and one other unobserved random variable.

### 02:04:21 · Speaker 6

Okay. So typically, I'll give you examples of what this, so typically,

### 02:04:29 · Speaker 9

typically Z

### 02:04:34 · Speaker 9

is also estimated

### 02:04:42 · Speaker 9

or learned

### 02:04:46 · Speaker 9

along with the model parameters theta.

### 02:05:02 · Speaker 9

Okay? So basically what we are saying is for

### 02:05:07 · Speaker 9

each x i in data, okay? there exists a z i, okay? correspond corresponding to x i.

### 02:05:26 · Speaker 9

That is an absurd.

### 02:05:34 · Speaker 9

Now this Z I examples for this where Z is discrete, okay?

### 02:05:44 · Speaker 9

let's say that Z

### 02:05:47 · Speaker 9

Hmm

### 02:05:49 · Speaker 9

is discreet and it is

### 02:05:52 · Speaker 9

will take let's say one two

### 02:05:57 · Speaker 9

zero to like M values, let's say one to M values.

### 02:06:06 · Speaker 9

values. Then

### 02:06:11 · Speaker 9

given an x y

### 02:06:15 · Speaker 9

belonging to D, okay? Z I given this X, X I, okay?

### 02:06:28 · Speaker 9

may indicate

### 02:06:33 · Speaker 9

Decade

### 02:06:43 · Speaker 9

indicates

### 02:06:48 · Speaker 9

I don't see that. Let's see.

### 02:06:52 · Speaker 9

Z I comma X I clusters. clusters.

### 02:06:58 · Speaker 9

X I into

### 02:07:02 · Speaker 9

one of M categories.

### 02:07:11 · Speaker 9

You understand? So in this sense, right? A Gaussian mixture model

### 02:07:22 · Speaker 9

of which the K means clustering is a

### 02:07:28 · Speaker 9

special case, okay? Or both latent variable models.

### 02:07:52 · Speaker 9

Any questions on this?

### 02:07:55 · Speaker 6

So basically what we are saying is the following, right? Given data, what we do is that we model our data this way, which is a marginal over the joint distribution of the data and another random variable called Z. Okay? Now what is this Z? This Z is a latent variable or an unobserved random variable that is not with data, that is not actually measured or seen with the data, but it is there with the data.

### 02:08:24 · Speaker 6

Okay. Now what is the advantage of having this sort of a modeling is there are multiple reasons. One, having a latent variable model will like will enable speech will enable model learning, okay, easy easier, make it easier. In the case of Gaussian mixture model, it will make it easier, algebraically easier. That is one reason. The other reason is if you have a latent variable model, you can actually get information like this, which is given a particular

### 02:08:54 · Speaker 6

the X I after training right if you estimate the corresponding latent variable it will tell you if it's discrete it will tell you what cluster every X I belongs to so that is the that is the classical example of K means clustering and Gaussian G M M clustering where there are both latent variable models which will tell you for every X I it will tell you what cluster X I belongs to the second example can be okay the first example second example is where Z is continuous

### 02:09:27 · Speaker 6

which is

### 02:09:27 · Speaker 9

is actually an auto encoder or a V A E also.

### 02:09:34 · Speaker 9

where

### 02:09:37 · Speaker 9

Z I given an X I okay can be seen as

### 02:09:58 · Speaker 9

your Z then some R K it's a continuous vector can be seen as seen as

### 02:10:07 · Speaker 9

Feature

### 02:10:12 · Speaker 6

corresponding to X. So latent variable models, right, we label feature extraction.

### 02:10:19 · Speaker 6

you can use Z I rather than X I. Okay? uh for downstream tasks and all that. So, these are called, I mean these are feature extractors. So that's why you want to model uh the data X I by introducing one other random variable, Z I, which is called the latent variable.

### 02:10:39 · Speaker 6

Any questions on this motivation?

### 02:10:46 · Speaker 7

Sir, for the continuous case, we are saying that, uh Z I by X I can be seen as a feature for

### 02:10:48 · Speaker 6

gets

### 02:10:52 · Speaker 6

or not by not by C I given X I. It's a conditional random variable conditional distribution.

### 02:11:00 · Speaker 7

Okay.

### 02:11:01 · Speaker 6

ZI given XI

### 02:11:04 · Speaker 7

sorry, sorry for that. Z I given X I can be seen as a feature corresponding to Z I.

### 02:11:11 · Speaker 6

corresponding to sorry, corresponding to X I.

### 02:11:11 · Speaker 7

So

### 02:11:17 · Speaker 7

Okay

### 02:11:20 · Speaker 9

ओके सर

### 02:11:23 · Speaker 8

So the feature should be useful in some way, right?

### 02:11:25 · Speaker 6

Correct. Correct. It will be useful in some way. That's the point.

### 02:11:32 · Speaker 6

Latent variable models are imposed because features are useful in some way.

### 02:11:40 · Speaker 6

Now that's what I'm saying. So now the

### 02:11:43 · Speaker 6

the literature, right? These latent variable models are designed in such a way that you learn the latent variable and the model parameters together.

### 02:11:56 · Speaker 9

All right

### 02:12:04 · Speaker 9

in auto

### 02:12:04 · Speaker 6

See in GANs, right, what did we learn? We basically learned the model. Okay? But in in in in latent variable models, we learned the model, okay? But you will also learn the the latent variable together.

### 02:12:26 · Speaker 3

but all right

### 02:12:31 · Speaker 9

Okay, shall we move on?

### 02:12:44 · Speaker 3

Okay

### 02:12:46 · Speaker 9

Now let's look at

### 02:13:00 · Speaker 9

Can I draw straight lines here in this thing?

### 02:13:04 · Speaker 6

the way to do it

### 02:13:07 · Speaker 6

long press in good notes right a long press would make it a straight line

### 02:13:13 · Speaker 6

I don't know how I have to go insert line and all that that's too much.

### 02:13:17 · Speaker 3

No sir, that is in the draw itself.

### 02:13:20 · Speaker 6

in the draw

### 02:13:21 · Speaker 3

in the draw

### 02:13:23 · Speaker 6

Ah

### 02:13:23 · Speaker 3

Yeah. Uh, these symbols are there after pencils. There are one round and one square that is giving you, uh, yes.

### 02:13:31 · Speaker 6

you can

### 02:13:35 · Speaker 6

free time हो जाकर दो देसा ओके फाइन

### 02:13:38 · Speaker 2

I guess sir next to that menu also like that if you draw a square it will convert to square. Yeah this one.

### 02:13:46 · Speaker 6

Okay

### 02:13:47 · Speaker 3

Yeah, but sir, when you type, it will convert your character as well.

### 02:13:53 · Speaker 3

it will disturb you.

### 02:14:02 · Speaker 9

Okay, so this will convert into regular figures, huh?

### 02:14:09 · Speaker 9

four

### 02:14:17 · Speaker 9

Okay. Let's not complicate stuff. Maybe I will use a line and do it. Okay, fine. So now,

### 02:14:25 · Speaker 9

modeling

### 02:14:28 · Speaker 9

variable models.

### 02:14:41 · Speaker 9

Okay, so recall, so suppose

### 02:14:47 · Speaker 9

suppose

### 02:14:52 · Speaker 9

p theta x

### 02:14:55 · Speaker 6

I'll for now use assume that the latent variables are continuous and this is my model

### 02:15:04 · Speaker 9

P note

### 02:15:06 · Speaker 9

variable model

### 02:15:16 · Speaker 9

Now again the same thing right? So goal

### 02:15:23 · Speaker 9

Even

### 02:15:26 · Speaker 9

D

### 02:15:28 · Speaker 9

that are samples

### 02:15:33 · Speaker 9

ID samples from PX, I need to

### 02:15:39 · Speaker 9

Estimate

### 02:15:42 · Speaker 6

E theta, okay? Such that some divergence metric

### 02:15:48 · Speaker 6

for for VAE right the divergence metric that is taken is the KL

### 02:15:53 · Speaker 9

Okay

### 02:15:55 · Speaker 9

minimum wage

### 02:16:01 · Speaker 9

This is our goal

### 02:16:08 · Speaker 9

So we need theta star

### 02:16:14 · Speaker 9

that's the minimizer of

### 02:16:17 · Speaker 9

A cable between

### 02:16:21 · Speaker 9

x and e theta

### 02:16:24 · Speaker 9

recall that this is equal to

### 02:16:29 · Speaker 9

maximum is a rough

### 02:16:51 · Speaker 9

expected long likelihood

### 02:16:55 · Speaker 9

Do you remember this?

### 02:16:59 · Speaker 9

We had done this right?

### 02:17:02 · Speaker 9

Does all of you remember this?

### 02:17:08 · Speaker 7

minimizing KL divergence is same as maximizing log likelihood.

### 02:17:12 · Speaker 9

Correct

### 02:17:13 · Speaker 6

expected long likelihood, right?

### 02:17:17 · Speaker 6

maximize G log likelihood okay is what it is so let's let's write that we are interested in in maximizing G

### 02:17:31 · Speaker 6

likelihood function. So I'll remove the expectation because uh if you maximize the likelihood for all x, the expectation will also be maximized, right? So that's because just to make the algebra easier, I mean, the final loss function and everything will have an outer expectation with respect to px, which will have a sum over all samples in px, okay? Let us uh remove that to make like a little easier. So our objective is to maximize the log of the likelihood under the model P theta. Okay. So denote

### 02:18:10 · Speaker 6

Hello

### 02:18:12 · Speaker 6

log p theta of x by

### 02:18:18 · Speaker 6

L theta. Let's call it L theta. Now our objective is to maximize L theta. Okay? So how do we do that? Under a related variable model. We have L theta is now equal to

### 02:18:33 · Speaker 6

log

### 02:18:35 · Speaker 6

p theta of x

### 02:18:38 · Speaker 6

Now under the

### 02:18:40 · Speaker 6

लेटेंट वेरिएबल

### 02:18:41 · Speaker 9

model. This is integral

### 02:18:45 · Speaker 9

p theta x

### 02:18:54 · Speaker 9

Please let me know if

### 02:18:57 · Speaker 6

if if if if any one of these steps are not clear to you okay?

### 02:19:04 · Speaker 6

Okay, this is because

### 02:19:08 · Speaker 6

in latent variable models my p theta

### 02:19:10 · Speaker 9

as the marginal over these two, right? That is why it is

### 02:19:14 · Speaker 9

equal to this.

### 02:19:21 · Speaker 9

Okay, now

### 02:19:24 · Speaker 9

is equal to log of

### 02:19:33 · Speaker 9

E theta X and C times

### 02:19:38 · Speaker 9

Q J given X

### 02:19:43 · Speaker 9

divided by Q C D one X

### 02:19:48 · Speaker 9

see

### 02:19:50 · Speaker 9

Square

### 02:19:55 · Speaker 9

so that I can continue.

### 02:20:02 · Speaker 9

Q O Z given X.

### 02:20:05 · Speaker 9

some distribution.

### 02:20:11 · Speaker 6

Four

### 02:20:13 · Speaker 6

So Q of Z given X is Q of Z given X is some distribution over a latent variable, right? You take any distribution over latent variable, right? You can just multiply and divide.

### 02:20:29 · Speaker 6

divide by that, okay? And the integral doesn't change. Is this all right?

### 02:20:35 · Speaker 6

some distribution over the latent variable is is this okay?

### 02:20:42 · Speaker 9

It can be any arbitrary distribution, doesn't matter, okay? Now this is

### 02:20:52 · Speaker 9

log of

### 02:21:00 · Speaker 9

expectation of

### 02:21:18 · Speaker 9

C theta

### 02:21:21 · Speaker 9

divided by Q C Q one X

### 02:21:25 · Speaker 9

with respect to Q

### 02:21:27 · Speaker 9

Is that is that all right?

### 02:21:34 · Speaker 9

by definition

### 02:21:39 · Speaker 9

What I have done, just group this together.

### 02:21:45 · Speaker 9

and taken this as a function and written that integral as the expectation over C. Is it okay?

### 02:21:59 · Speaker 9

Now

### 02:22:01 · Speaker 9

So something called Jensen's inequality

### 02:22:11 · Speaker 9

that says that

### 02:22:18 · Speaker 9

log of expectation.

### 02:22:27 · Speaker 9

is always

### 02:22:29 · Speaker 9

less than or equal to expectation of

### 02:22:33 · Speaker 9

log of

### 02:22:40 · Speaker 9

that function

### 02:22:43 · Speaker 9

Um

### 02:22:45 · Speaker 9

Does everybody, has everybody heard of, in

### 02:22:48 · Speaker 6

inequality or not

### 02:22:52 · Speaker 7

Yes sir

### 02:22:54 · Speaker 6

uh if not right maybe we can take it in the T S session. Okay. Just look into it no. So using that what we can do is so we have now L theta which is our log likelihood that we would want to maximize is equal to log of

### 02:23:09 · Speaker 6

expectation of

### 02:23:12 · Speaker 6

this entire thing with respect to Q. Now I can write that as something that is less than or equal to

### 02:23:20 · Speaker 6

sorry. greater than or equal to because this is equal to greater than or equal to

### 02:23:27 · Speaker 6

the expectation of

### 02:23:31 · Speaker 9

log of

### 02:23:35 · Speaker 6

function.

### 02:23:36 · Speaker 7

Sir, less than equal to, based on the previous expression.

### 02:23:42 · Speaker 6

log is less than or equal to that expectation of log

### 02:23:47 · Speaker 7

Yes sir

### 02:23:47 · Speaker 6

So, uh, this is

### 02:23:51 · Speaker 6

this is log so this is less than

### 02:23:55 · Speaker 6

log is less than expectation of log correct no? log is less than expectation of log should be correct no?

### 02:24:04 · Speaker 7

No sir. Other way around. It should be other way around.

### 02:24:05 · Speaker 6

should be other way around

### 02:24:08 · Speaker 6

Okay, so then this is

### 02:24:10 · Speaker 9

Hello

### 02:24:11 · Speaker 9

bus

### 02:24:14 · Speaker 9

I think it's correct now, right?

### 02:24:23 · Speaker 7

No sir, I am, I don't remember the inequality sign correctly but

### 02:24:26 · Speaker 6

No no no, that's okay, but with this inequality whatever I have written is correct, no? See, I know for a fact that this is right, so we'll have to change the Jensen's inequality correspondingly. Okay, sorry. See, Jensen's inequality becomes an upper bound or a lower bound depending upon this function. If this function is concave, then it is one, it is convex, it is something else. So, sometimes I get confused about it. This is correct, right? Just tell me that if it's greater than or equal to here, this will become greater than or equal to here, correct?

### 02:24:31 · Speaker 7

I

### 02:24:36 · Speaker 7

ओके सर

### 02:24:59 · Speaker 3

Yes sir

### 02:25:00 · Speaker 6

So then then tensions inequality is correct. Okay. Right. So now this is greater than or equal to what what do we have here? It's an integral.

### 02:25:16 · Speaker 6

course

### 02:25:16 · Speaker 9

we have Q of C equal to one X, okay? times log of

### 02:25:26 · Speaker 9

P theta of

### 02:25:28 · Speaker 9

sequence divided by

### 02:25:32 · Speaker 9

C G one X D set okay

### 02:25:40 · Speaker 9

Okay

### 02:25:47 · Speaker 9

Now this

### 02:25:49 · Speaker 9

let

### 02:25:52 · Speaker 9

this entire thing

### 02:25:53 · Speaker 6

Right

### 02:25:55 · Speaker 6

Note that this is a function of two things, right? It's a function of

### 02:26:00 · Speaker 6

theta obviously. It's also a function of Q distribution that we have chosen, isn't it? Depending upon what Q we choose here when we started, right? We have some distribution over G. So you will get a different uh lower bound on the likelihood, correct?

### 02:26:20 · Speaker 6

Now this implies what did we do so far is that by introducing a latent variable model and a distribution over it, we showed that the function which is the log likelihood that we would want to maximize is

### 02:26:33 · Speaker 6

Lower bounded by

### 02:26:37 · Speaker 6

some function which is a function of the model parameters and a distribution over latent variable. Okay. So now this Q which is a distribution conditional distribution over C is referred to as the variational posterior.

### 02:26:54 · Speaker 6

variational latent posterior. It's by the name V A E, okay?

### 02:27:01 · Speaker 6

What is that? It's a distribution over Z. Okay? And this F theta is also called as the evidence.

### 02:27:12 · Speaker 6

lower bound

### 02:27:15 · Speaker 6

It's a lower bound, okay?

### 02:27:18 · Speaker 6

on log likelihood, okay? log likelihood is also called as

### 02:27:25 · Speaker 6

Evidence

### 02:27:27 · Speaker 6

when it's another name for that, no? So you want to in all models you want to maximize the evidence under the model P theta. uh So now you have constructed a lower bound on the evidence, okay? Based on a variation latent posterior and this is abbreviated as ELBO.

### 02:27:49 · Speaker 9

Is this clear?

### 02:27:52 · Speaker 6

Now what we need is we need to remember that we wanted to find a theta that would maximize the evidence or the log likelihood, okay? Now this is equivalently

### 02:28:08 · Speaker 6

maximizing the lower bound on the evidence, you know, because in latent variable models, you know, maximizing the evidence will become difficult. Just like we did it with the the F divergence, right? Minimizing the F divergence directly was not feasible. We constructed a lower bound on it. Similarly, on the evidence, we are constructing a lower bound, okay? Now this maximization now is not only with respect to theta, it is also with respect to Q, right? So as I said, you need to find two things. One, you need to find the Q that would construct

### 02:28:38 · Speaker 6

lower bound on the log likelihood that you would want to maximize and you also want to find the theta that are model parameters

### 02:28:46 · Speaker 6

Is that all right? So you need to find the theta star and the Q star, okay? That would maximize the lower bound that we have constructed on the

### 02:28:58 · Speaker 6

evidence. So what is that lower bound? Lower bound is the expectation of log of

### 02:29:06 · Speaker 6

C theta

### 02:29:09 · Speaker 6

Divided by

### 02:29:10 · Speaker 9

given x with respect to

### 02:29:13 · Speaker 9

this

### 02:29:21 · Speaker 6

This is a very important result, okay, that is used in all latent variable models. I mean this is the framework for latent variable models. So basically you find out the model parameters theta and also the latent variable parameters Q, okay, such that the lower bound that you have constructed on the likelihood function is maximized.

### 02:29:45 · Speaker 6

Any questions on this?

### 02:29:47 · Speaker 6

See note that there are two optimization problems here right one optimization problem is over theta okay which are the model parameters. The other optimization problem is over Q which is a functional approximation problem right.

### 02:30:01 · Speaker 6

It's not a it's not over parameters it is over class of functions.

### 02:30:08 · Speaker 6

This is all right

### 02:30:10 · Speaker 9

an example for this is

### 02:30:17 · Speaker 9

I'll come to you Vivek. Example for this is what is

### 02:30:20 · Speaker 6

called as a Gaussian mixture model or a GMM.

### 02:30:27 · Speaker 6

I'll not go into the details of G M M, okay? uh but just tell you what P theta of X is as usual a latent variable model which is

### 02:30:40 · Speaker 6

Okay? Where

### 02:30:43 · Speaker 9

theta of x and z is given by

### 02:30:58 · Speaker 9

I can write it

### 02:31:02 · Speaker 9

Okay, I'll try to decide only. Oh, hold on.

### 02:31:11 · Speaker 9

see okay. We have alpha z's. The normal distribution.

### 02:31:22 · Speaker 6

this is a G M M right? It's a P theta is a linear combination of multiple Gaussian distributions.

### 02:31:31 · Speaker 6

Okay? So there are, okay, let me write it. Z equal to one through M, so it's a discrete model, right? Yeah, so there are M Gaussian distributions and your model is a combination of M Gaussian distributions. Now, theta, okay, will be set of M alphas, alpha one through alpha M, okay? And for every Gaussian, you have one mean vector. So you have M such mean vectors and you have M sigma. That is your parameters

### 02:32:04 · Speaker 6

that you would want to estimate in a G M M. How is it done? It is exactly done by solving this optimization problem, no, which is theta star and Q star, okay? So the uh the way it is done is

### 02:32:19 · Speaker 6

Alternatively

### 02:32:24 · Speaker 6

Okay

### 02:32:25 · Speaker 6

for

### 02:32:28 · Speaker 6

theta star and q star. Here you need to solve an optimization problem with respect to both theta star and q star, right? In a G M M you alternatively get q and theta star. Now, what can be shown is the optimal q star, okay?

### 02:32:48 · Speaker 6

which would maximize the

### 02:32:53 · Speaker 6

P L O

### 02:32:55 · Speaker 6

can be shown to be equal to simply the posterior

### 02:33:02 · Speaker 6

this distribution. That's all.

### 02:33:05 · Speaker 6

Okay, so now maybe you can take this as a homework or make it in a T A session. So the optimal Q distribution, right, that would

### 02:33:16 · Speaker 6

for this right here

### 02:33:19 · Speaker 6

when we constructed the lower bound, right? The optimal Q that would maximize this lower bound. By the way, can somebody tell me this? What would be the value of the lower bound with an optimal Q?

### 02:33:34 · Speaker 6

with the optimal Q, what would be the value of the lower bound with

### 02:33:42 · Speaker 6

Q star, okay?

### 02:33:45 · Speaker 6

f theta of q star

### 02:33:47 · Speaker 9

will be what? See what is the maximum value of f theta cube?

### 02:34:01 · Speaker 9

Am I audible?

### 02:34:06 · Speaker 3

Yes sir

### 02:34:11 · Speaker 6

Did you understand my question?

### 02:34:15 · Speaker 6

The question is, I've created a lower bound on the likelihood function, no, L theta. Okay, I've denoted that as F theta Q. What would be the maximum value of this?

### 02:34:28 · Speaker 6

What is the maximum value that this lower bound can achieve?

### 02:34:33 · Speaker 3

Logic

### 02:34:35 · Speaker 6

L theta, right?

### 02:34:37 · Speaker 6

because it's a lower bound on L theta, the maximum value that it can achieve is L theta, isn't it?

### 02:34:48 · Speaker 6

Do you see that or not? Hello?

### 02:34:52 · Speaker 7

Yes sir, the maximum lower bound will equal L theta, yes.

### 02:34:53 · Speaker 9

Yes sir

### 02:34:55 · Speaker 6

Exactly, right? So the maximum lower bound at that point will be simply equal to L theta.

### 02:35:03 · Speaker 6

Okay. So what I'm saying is it can be theoretically shown that the optimal Q distribution is equal to P theta of Z given X and for that Q theta, okay, for for with that Q star, the the lower bound that we have constructed is equal to the likelihood value.

### 02:35:24 · Speaker 6

Okay? Now once you have gotten an optimal lower bound, what you do is which

### 02:35:34 · Speaker 6

that Q star, okay?

### 02:35:37 · Speaker 6

Find the next

### 02:35:40 · Speaker 6

Next best

### 02:35:42 · Speaker 6

theta. So now let's call this alternatively solve for theta star and q star, right? So let's say that we have taken that as theta t, okay? Now q star at t plus one.

### 02:35:58 · Speaker 6

iteration t plus one is simply equal to the posterior at theta

### 02:36:06 · Speaker 6

So f theta that we have gotten is equal to l theta at that stage. So with that q star at t plus one, okay? You find the next best theta t plus one. How do you do that? Theta t plus one is simply

### 02:36:24 · Speaker 6

the arg max of

### 02:36:28 · Speaker 6

F that you have computed with Q T plus one

### 02:36:34 · Speaker 6

as a function of theta. That's all. And you keep alternating between these two. So you find a theta, okay, with Q being equal to P theta of Z given X at the previous time. And

### 02:36:48 · Speaker 6

you use that theta to find your next Q and keep alternating between them.

### 02:36:57 · Speaker 6

Is this all right? Did you understand this?

### 02:37:01 · Speaker 6

The only thing that I've not done is I've not told you uh that y is the optimal Q equal to P theta of Z given X, right? See that is something that you can take it as a homework or just show that, okay? But yeah, so it is there in my notes also. I mean it's given in the first lecture of my handwritten notes, have a look at it, okay? This is like

### 02:37:28 · Speaker 9

of nodes.

### 02:37:33 · Speaker 6

have a look at it. But yeah. So now basically what we are doing is we are we are so remember this right what we want to do is we wanted to maximize the likelihood. Instead of that we constructed a lower bound on that and then we would we we we started maximizing the lower bound. And that lower bound depends on two things theta and Q. Right? And we would alternatively optimize between this theta and Q. One example is a GMM where you first fix a theta.

### 02:38:03 · Speaker 6

and find this Q to be this posterior. Okay? And for a GMM, how do you find this posterior? This can be found out analytically.

### 02:38:12 · Speaker 6

Now I'll tell you. So P theta of Z given X in the case of a G M M is given by P theta of X given Z times P Z okay divided by P theta Z sum of this thing right?

### 02:38:33 · Speaker 6

for Z. This is the definition. Now what is this equal to? P theta of X given Z for a GMM. It is actually means

### 02:38:44 · Speaker 6

G is equal to one particular J, okay? Let's say P theta of G equal to J. And this is is equal to J to M. Okay? Now what is this equal to? The numerator for a given J, G M M is simply that particular Gaussian.

### 02:39:05 · Speaker 6

okay? And this is equal to alpha j

### 02:39:09 · Speaker 6

uh yeah alpha j. and this is simply the sum of

### 02:39:15 · Speaker 9

of C equal to

### 02:39:18 · Speaker 9

sorry, j equal to 1 to m

### 02:39:25 · Speaker 9

j equal to one two m

### 02:39:35 · Speaker 9

you have a Gaussian here.

### 02:39:38 · Speaker 9

Museum

### 02:39:39 · Speaker 6

is equal to

### 02:39:40 · Speaker 6

Times Alpha

### 02:39:43 · Speaker 5

this can be found out.

### 02:39:45 · Speaker 6

Once you find this out, what you do is simply plug that into the lower bound and then maximize that with respect to theta. Right? You get a new theta, use that new theta to evaluate this again. Right? And keep alternating between those two steps.

### 02:40:07 · Speaker 6

There's a name for this algorithm, do you know?

### 02:40:10 · Speaker 6

Does anybody know?

### 02:40:12 · Speaker 9

expectation, expectation maximum.

### 02:40:12 · Speaker 3

E

### 02:40:12 · Speaker 7

expectation

### 02:40:14 · Speaker 6

This is the E M algorithm. This is the expectation maximization algorithm. This is how you fit a G M M to some data, no?

### 02:40:32 · Speaker 9

Ee algorithm

### 02:40:34 · Speaker 6

See I won't go to showing why E O algorithm is correct and all that okay that I will skip. uh but basically this I gave this as an example I'm running through it quickly because we are interested in looking at V A E is not G M M's. But yeah so basically the idea is uh that this will be common across G M M's and V A E is all latent variable models right where construct a lower bound on the likelihood and then find the variational distribution and the model parameters. through alternative optimizations that would be same across GMM and this thing

### 02:41:11 · Speaker 6

Now, in in in fact, in fact, does all of you know about K means algorithm? K means clustering?

### 02:41:22 · Speaker 9

Yes sir

### 02:41:23 · Speaker 6

K means clustering is exactly EM. What do you do in K means clustering? Given data, you randomly assign K clusters, right? And you assign each of those each of the data points to a particular cluster, right? That is this step. Evaluating this, that is this particular step.

### 02:41:44 · Speaker 6

evaluating you're making your posterior equal to P theta of Z given X is actually the assignment step. Okay? Once you assign you recalculate the means, right? Recalculating the means is this step. This finding out that theta. In fact, what can be shown is that K means clustering is a special case of GMM where the where the variance of those component Gaussians are infinitesimally small. That can be theoretically proven. Anyway, uh that's a different matter. But basically, uh

### 02:42:14 · Speaker 6

The take home message is that for latent variable models to optimize what you do is that you construct a lower bound on the likelihood function that you would want to maximize, okay? And then you alternate, you estimate both the model parameters and the the variational distribution Q together.

### 02:42:36 · Speaker 6

Okay? That is the take home message. Now for models like G M M right? You know that the optimal Q is P theta of Z given X. Okay? And for G M M that can be computed because there's an analytical form. The question is...

### 02:42:54 · Speaker 6

we have theta star and q star to be the maximizers. We want maximizers with respect to both theta and q and we want to maximize the lower bound that we have constructed, correct? Now, q star is known to be p theta of z given x, correct?

### 02:43:14 · Speaker 9

However, however,

### 02:43:23 · Speaker 9

What if? What if?

### 02:43:26 · Speaker 9

p theta of c given x can't be computed.

### 02:43:36 · Speaker 9

if p theta of g k one x cannot

### 02:43:39 · Speaker 6

be computed, how do you solve the elbow optimization problem is the question.

### 02:43:45 · Speaker 6

Does it make sense?

### 02:43:47 · Speaker 6

for G M M's P theta of G given X can be computed and that's why you can do E M. If you cannot compute P theta of G given X, how do you solve ELBO optimization is the question that is asked in the V I E paper.

### 02:44:02 · Speaker 6

That is our preface. Now we want, so now the goal, goal is to

### 02:44:10 · Speaker 6

is to estimate

### 02:44:14 · Speaker 6

in

### 02:44:14 · Speaker 9

parameters of a latent variable model

### 02:44:19 · Speaker 9

offer

### 02:44:24 · Speaker 9

later variable model

### 02:44:28 · Speaker 9

for which, for which

### 02:44:30 · Speaker 9

the posterior P theta of G given X, okay?

### 02:44:36 · Speaker 9

and be computed.

### 02:44:41 · Speaker 6

This is a starting point. In fact, the state of the art generating models which are diffusion models are also special cases of uh of uh VAEs, okay? So it's very important that we understand what VAEs is, VAEs are, okay? So this is the prelude or preface of why uh do we need another model, okay? When there were latent variable models like GMM, it is because while all latent variable models

### 02:45:11 · Speaker 6

seek to uh maximize the lower bound on the uh likelihood uh with respect to model parameters and distribution over Z. uh simpler models like GMMs have this uh advantage that the optimal Q which is the P theta of Z given X can be computed analytically. But if there are models for which P theta of Z given X cannot be computed analytically, how do you solve for how do you estimate the model parameters? for latent variable models is the question

### 02:45:46 · Speaker 6

Is this is the story clear so far?

### 02:45:49 · Speaker 6

So with this right I I uh ask I mean I request all of you to read the first and the second chapter of my handwritten notes before coming to the next class. Okay? So with this preface and if this preface and prelude is strong we can quickly go to uh like how V A E solves V A E actually solves this problem uh by approximating the variation posterior using a neural network and all that which you will see in the next class. So please uh read my handwritten written notes, first lecture and second lecture and come prepared for next class, okay?

### 02:46:25 · Speaker 6

Stop here and take questions if there are any. Vivek.

### 02:46:32 · Speaker 8

So initially felt like I understood but there are many things like so why we used Jensen's inequality like why didn't why do we settle for a lower bound actually?

### 02:46:45 · Speaker 6

because the log likelihood cannot be computed.

### 02:46:50 · Speaker 6

or latent variable models like G M M's right what happens is see how do we do maximization so if we start with the log likelihood let's say right. Okay. Okay let me show that.

### 02:47:08 · Speaker 6

now

### 02:47:08 · Speaker 6

log of p theta of x in the case of gmm will be log of sigma

### 02:47:18 · Speaker 6

of alpha j, okay? And you have x here and this is mu j and sigma j, correct?

### 02:47:26 · Speaker 6

Yes

### 02:47:26 · Speaker 4

your guess

### 02:47:26 · Speaker 6

or James

### 02:47:27 · Speaker 6

Now, this is sum of alpha j into e power x squared minus mu j squared so on, right?

### 02:47:39 · Speaker 6

See, if there was sum of C, you want to differentiate this with respect to mu and sigma and put it to zero to maximize this, correct?

### 02:47:39 · Speaker 7

Yes, there was

### 02:47:47 · Speaker 6

No, if there were, if there were a sum of log term, then this log and e power exponentiation would cancel each other and you can differentiate.

### 02:47:47 · Speaker 7

If

### 02:47:56 · Speaker 6

But because you have a log of some terms

### 02:48:01 · Speaker 6

Because you have a log of some terms here, if you differentiate this, you will not get mu j's in one side and you will not get a tractable equation in terms of mu. So you cannot maximize this.

### 02:48:15 · Speaker 8

Okay, the summation of, uh, I mean the log of the summation of

### 02:48:20 · Speaker 6

multiple exponentiation, multiple Gaussian distributions, if you differentiate that with respect to one mu, it will not get separated out.

### 02:48:30 · Speaker 3

Yes

### 02:48:32 · Speaker 6

Right. So now you need to do something to ensure that this is maximized. So now to maximize that one way to do it is construct a lower bound and if you construct the lower bound the EM becomes easier. It is one of the motivations of why do you need to construct lower bounds on log likelihood.

### 02:48:51 · Speaker 6

Okay. The other thing is again similar thing, you know, log of integral of P theta of X and Z, right? For Z, this is the model. Now, if you do not know how to integrate this with respect to Z because you don't know this distribution, how do you differentiate this with respect to theta? You can't do that.

### 02:49:09 · Speaker 6

You need another method to optimize for the log likelihood, no? That's why you construct a lower bound and then you optimize for it. See, just you remember why we constructed lower bound on f divergences, right? Because we could not compute the f divergence there because it involved integrals. What we did was we expressed that in terms of expectations that we could compute and then simply used sample estimates to optimize for it, right?

### 02:49:35 · Speaker 7

Yes, yes, yes. Exactly.

### 02:49:36 · Speaker 6

exactly same thing here. exactly same thing. And you remember that maximizing this is again minimizing the KL divergence. Ultimately we are minimizing the KL divergence.

### 02:49:45 · Speaker 6

And to minimize this that there this involves integrals with respect to P X and P theta which we cannot compute and that's why we are computing lower bounds and expressing it in terms of expectations. That can be estimated using the sample averages.

### 02:49:59 · Speaker 6

That's the fundamental idea, okay?

### 02:50:02 · Speaker 0

Okay

### 02:50:04 · Speaker 6

Avirup

### 02:50:08 · Speaker 0

Yeah. So my question is related to the midterm exam. So the syllabus for it is till the next class or today's class or any any specification regarding till

### 02:50:20 · Speaker 6

regarding till till till the next class yeah. There will be one more class before the exam it will be till that.

### 02:50:28 · Speaker 0

Okay and I mean just to get some idea on the question so shall we be expecting coding questions or mostly theoretical? No no there will not be

### 02:50:35 · Speaker 6

No, there will not be any coding questions, it will all be theoretical.

### 02:50:40 · Speaker 6

just follow whatever has been said in the class and also the T S S S works

### 02:50:46 · Speaker 9

this

### 02:50:57 · Speaker 9

Hello

### 02:50:59 · Speaker 1

Yes sir

### 02:50:59 · Speaker 7

Yes sir, I

### 02:51:00 · Speaker 0

I got my answers

### 02:51:02 · Speaker 9

Yeah

### 02:51:02 · Speaker 6

Okay

### 02:51:03 · Speaker 1

Hi sir, Ankush here. Sir, I have a quick question. Sir, we read about this model, now we understood also exactly how it works internally. So, uh for practical usage like where all we can use like image generations or data. Hold on.

### 02:51:05 · Speaker 6

Yeah

### 02:51:17 · Speaker 6

Hold on. We just started V A E's, right? There's two full lectures that will be that will be kept for this. Where I talk about all kinds of applications, how it is used for generative models, everything will be covered.

### 02:51:22 · Speaker 1

Yeah

### 02:51:28 · Speaker 1

Okay

### 02:51:35 · Speaker 1

Okay sir okay that is planned okay I was just asking that thank you

### 02:51:38 · Speaker 6

Of course, right? I mean, just like we did for Gyaans, we are just starting it. Ah, right. Lot that we need to do.

### 02:51:42 · Speaker 1

Oh, okay

### 02:51:44 · Speaker 1

Sure, sure. Thank you.

### 02:51:46 · Speaker 6

simply the preface. Okay. Anything else?

### 02:51:51 · Speaker 3

I'm good, sir.

### 02:51:52 · Speaker 6

Okay

### 02:52:05 · Speaker 6

Yeah, uh go on Srivastava.

### 02:52:09 · Speaker 5

Uh sir, in the assignment, right? Uh I'm I'm just curious to ask, like since you said there is no report to be submitted, what all things we have tried, we can simply add it in the markdown, right? Because uh in order to get any valid result, too many things are being tried out from my end, so just want to know.

### 02:52:27 · Speaker 6

Okay, what is the question?

### 02:52:30 · Speaker 5

like uh so far I was trying assignment questions so it's not coming directly in the first step itself like lot of things are being tried out here and there so we can't just put everything in the notebook right so. No no you can you can.

### 02:52:34 · Speaker 6

Okay

### 02:52:43 · Speaker 6

No, no, you can, you can. Yeah, markdown statements and every experiment that you tried, no, just comment it out and put your observations, that will be appreciated.

### 02:52:52 · Speaker 5

the problem is sir if you are looking for the outputs of those experiments right? It's taking

### 02:52:57 · Speaker 6

No no no I don't. I don't. Whatever experiments that you that you tried no just document them okay.

### 02:53:05 · Speaker 5

ओके श्योर सर, थैंक यू।

### 02:53:07 · Speaker 6

Okay

### 02:53:08 · Speaker 4

answer for assignment like you said we should use Google Colab for compute but uh there's no free GPU available so I'm using my company's GPU and I'll put the

### 02:53:18 · Speaker 6

and I'll put there. That's okay. That's okay. It doesn't matter.

### 02:53:28 · Speaker 6

collab if only if like you know people don't have come go on you can speak you don't have to raise your hands class is done yeah

### 02:53:35 · Speaker 8

Yeah. So one question regarding the background reading material. So is it okay to read that the machine learning advanced topics by Murphy?

### 02:53:46 · Speaker 6

Murphy is okay. Murphy is a good book. Yeah, it's it's not it's actually a very good book. Yeah, you can use Murphy.

### 02:53:47 · Speaker 8

is a good introduction

### 02:53:54 · Speaker 8

Okay, only the portions related to generative modeling.

### 02:53:58 · Speaker 6

Whatever we have, See. Yeah, it's very, it's very, very vast. Okay. Simple thing. Whatever I've taught in class is what your syllabus is. Nothing less, nothing more.

### 02:54:00 · Speaker 8

Yeah, it's very, very, very vast. Right. Okay.

### 02:54:11 · Speaker 6

Anything that is related to things that I've taught in class is all that I'm going to ask. I don't assume you to know anything that is beyond what I've whatever I've taught in class and also in T A sessions.

### 02:54:25 · Speaker 7

Yeah

### 02:54:36 · Speaker 9

That's all. Okay.

### 02:54:38 · Speaker 6

that's all it is. Let's meet next week, okay?

### 02:54:44 · Speaker 9

Thank you sir. Thank you sir. Thank you sir.

### 02:54:46 · Speaker 3

Thank you so much

### 02:54:47 · Speaker 6

Bye bye

### 02:54:49 · Speaker 3

Thank you, sir

### 02:54:51 · Speaker 9

Thank you sir
