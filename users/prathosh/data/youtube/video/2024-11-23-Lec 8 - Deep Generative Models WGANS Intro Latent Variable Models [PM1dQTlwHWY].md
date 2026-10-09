---
id: PM1dQTlwHWY
title: Lec 8 - Deep Generative Models WGANS Intro Latent Variable Models
url: https://www.youtube.com/watch?v=PM1dQTlwHWY
date: '2024-11-23'
duration: 02:55:07
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# Lec 8 - Deep Generative Models WGANS Intro Latent Variable Models

## Transcript

### 00:00:02 · Speaker 1

Yes sir we were able to see the first quiz also you got to see the marks right

### 00:00:08 · Speaker 2

suggesting this

### 00:00:10 · Speaker 1

Okay, thanks. And we have decided the midterm exam to be on 10 13th or something, right? I think I've marked our calendars also.

### 00:00:27 · Speaker 2

Yes it's 13th August on

### 00:00:28 · Speaker 1

13th after noon okay great okay so let's get somebody has raised their hand Aditya yeah

### 00:00:36 · Speaker 4

Uh, sir, maybe a logistical request if feasible, otherwise, please reject because this code two to six is like a festive for us like Durga Puja and all the Shara. So that assignment time, can it be this by Matt report there? Just a request if not for feasible, please ignore.

### 00:00:55 · Speaker 1

What can what uh I

### 00:00:57 · Speaker 4

the assignment date assignment deadline is nine i believe right and two to six is somewhere is a festive session for most of us like the theradurga etc so can it be increased by two three days i mean the timeline because we may not give the complete hour should be given to this project during that time it's just a request i mean if not possible please ignore

### 00:01:23 · Speaker 1

I mean see what happens is if I move it then the other assign the entire schedule has to be re arranged

### 00:01:33 · Speaker 1

Kindly excuse me on that

### 00:01:47 · Speaker 1

Okay let's get started uh

### 00:02:04 · Speaker 1

You don't see my screen

### 00:02:15 · Speaker 3

Mm

### 00:03:19 · Speaker 1

So today's agenda is that uh as I said we will move on to the next class of models which are various autoencoders which also happens to be the

### 00:03:29 · Speaker 1

a baseline for the state of the art generative image generating models called diffusion models which we will see next okay so before we go there uh we just take uh some 10 15 minutes and quickly finish this domain at those serial networks right which was left out the last time

### 00:03:51 · Speaker 1

Palm is there

### 00:03:53 · Speaker 1

Still let us

### 00:04:03 · Speaker 1

So I highlight this

### 00:04:19 · Speaker 1

Somebody asked me to central line this so they can get cut

### 00:04:28 · Speaker 1

Doesn't even know how to do that

### 00:04:39 · Speaker 1

Yeah

### 00:04:44 · Speaker 1

Okay thanks we should be enough

### 00:04:49 · Speaker 1

Okay so um

### 00:04:53 · Speaker 1

We will start with this uh domain at our serial networks okay or so-called DANS one of the

### 00:05:01 · Speaker 1

powerful applications of adversarial learning other than generative modeling and also right before we start I hope that you have started with the assignment

### 00:05:12 · Speaker 1

Uh and if there are any questions you can let me know or ask also

### 00:05:17 · Speaker 4

I pinged and TA but no one replied

### 00:05:21 · Speaker 1

Oh, is it? I I'll ask to do it. So last tutorial was done on CNN and PyTorch, right? Was it useful?

### 00:05:46 · Speaker 1

mean in the assignment you are saying see what i have observed is that uh that this animal data set right because there are multiple classes there about 90 classes uh unless you have a very uh deep architecture and you do a lot of hyperparameter tuning you don't get a very good generated images right but you know if you if you get images that are like

### 00:06:11 · Speaker 4

But it doesn't work

### 00:06:12 · Speaker 1

award looking like aha butterfly you will definitely get for that data set you will get good dream images not for the first one there are two data sets that we have given now

### 00:06:22 · Speaker 1

Yeah for the animal data set the images that are generated are like somewhat uh like looks looks like animalish but you need a lot of resources and deeper architectures to

### 00:06:35 · Speaker 1

get very good results okay in fact

### 00:06:40 · Speaker 1

Okay so uh have I uh

### 00:06:44 · Speaker 1

We talked about FID in this course

### 00:06:49 · Speaker 1

Oh no

### 00:06:50 · Speaker 4

Not exactly

### 00:06:52 · Speaker 1

It is planned for today. Yeah I'll have to do that today as well

### 00:06:59 · Speaker 1

I've not told you about the the bursa strains metric also no

### 00:07:05 · Speaker 4

knows that we haven't

### 00:07:12 · Speaker 4

Uh if the data set is hard for question one and two then why are you asking for the other questions

### 00:07:13 · Speaker 1

And it is the code

### 00:07:22 · Speaker 4

Like if animal data set is hard to train given the compute resource we have, then for other questions also like third, fourth and waste all like we'll have to use the same data set, right? Animal, then we'll have a poor result there also if we train this animal. Okay.

### 00:07:33 · Speaker 1

Nah

### 00:07:36 · Speaker 1

That's okay. That's okay. See, the assignment grading will not be based on the quality of your generated data anyway. It's not about results.

### 00:07:47 · Speaker 1

So yeah, but it has I mean I have deliberately chosen that data set because I want you to appreciate the fact that if there are too many classes and data has a lot of modes, right?

### 00:08:00 · Speaker 1

Building a generative model is difficult, especially using adversarial training. So we will use the same data sets for VAEs and diffusion models and you will see that it will improve. It was deliberately done. Yeah.

### 00:08:14 · Speaker 1

So there's a

### 00:08:14 · Speaker 4

This is a confirmation what we were trying to ask the butterfly data set is for only the 192

### 00:08:23 · Speaker 1

the front

### 00:08:23 · Speaker 4

from the third onwards we need to use the animal data set the the the the first again we need to use the animal data set

### 00:08:31 · Speaker 2

and to see how the outcomes are coming even the FAD calculation everything

### 00:08:36 · Speaker 1

But

### 00:08:37 · Speaker 2

Okay okay that was a question

### 00:08:41 · Speaker 1

But for the first and second question you will have to use the animal data set as well both of them

### 00:08:48 · Speaker 2

So yeah we definitely we need to train it for the other

### 00:08:50 · Speaker 1

But it's

### 00:08:51 · Speaker 2

Okay, but the generation may not be so accurate

### 00:08:54 · Speaker 1

Yes yes yes

### 00:08:58 · Speaker 1

Okay, so let's maybe continue quickly. Here I go on, let's go on. Yes, sorry, sir, one more thing. I noticed, sir, in the original Jan paper, the model was basically on a 64 by 64 image. The moment I scale it up to 128, right, I noticed the mode collab...

### 00:09:16 · Speaker 2

Becomes a lot frequent than 64 by 64 like the performance is much better.

### 00:09:21 · Speaker 1

Domain D C again you're D C again you're saying

### 00:09:25 · Speaker 2

Yeah yeah yeah

### 00:09:26 · Speaker 1

TCAN, okay. Yeah, see, you can tweak. One thing that you can do is if you start from 128, 128, just have another down sampling layer and then use TCAN on top of it.

### 00:09:40 · Speaker 2

Sure sir um I tried that I think it requires a little hyperparameter tuning to get it right

### 00:09:44 · Speaker 1

Got it, got it.

### 00:09:49 · Speaker 1

Yeah biology

### 00:10:05 · Speaker 1

It's in the again the first question

### 00:10:12 · Speaker 1

Shatya

### 00:10:15 · Speaker 2

So there is the instance of GAN we discussed right where we used the GENSIN, SHEN and DIVERGENT for being naive GAN. So actually if you see that the GAN paper right sir that is the GAN is separately mentioned and GENSIN, SHEN is also separately mentioned. So it's not that because of GENSIN, SHEN and here we are talking about GAN.

### 00:10:34 · Speaker 1

Okay, okay, I'll tell you. Yeah, see, okay, that's a good observation. See, the divergence that is used in the Naive-GAN paper is Jensen-Shannon divergence minus a constant. I think it's log 2 or something. Okay, that's the, and it's JL divergence plus a constant. That is what the GAN objective is.

### 00:11:03 · Speaker 1

Okay, so let's maybe quickly go to too many things to discuss. Okay, let's get started. Yeah, it's charged. I said, so this

### 00:11:15 · Speaker 1

there is another application of uh uh adversarial learning which is called domain adversarial networks okay so here is the problem so what you are given as you are given some data from a distribution called source distribution okay it's one y one

### 00:11:38 · Speaker 1

Two way two

### 00:11:40 · Speaker 1

Up to

### 00:11:42 · Speaker 1

X and Y and note that this is a supervised problem this is drawn ID from a distribution PS which is called the source distribution this is source data

### 00:11:56 · Speaker 1

And there is another data that is given to you we call XCAP one

### 00:12:04 · Speaker 1

two and

### 00:12:07 · Speaker 1

Thanks

### 00:12:10 · Speaker 1

this is sampled iid from et okay and this is called the target data

### 00:12:20 · Speaker 1

You note that source data has both the features and labels target data only has the features and does not have label source data is a supervised

### 00:12:38 · Speaker 1

And this is unsupervised

### 00:12:46 · Speaker 1

Now the goal

### 00:12:51 · Speaker 1

what is called as unsupervised domain adaptation

### 00:13:06 · Speaker 1

called as Yuda okay is

### 00:13:13 · Speaker 1

Even

### 00:13:15 · Speaker 1

PS and DT

### 00:13:25 · Speaker 1

Learn features or representations

### 00:13:32 · Speaker 1

So that's that

### 00:13:38 · Speaker 1

That's that they perform

### 00:13:44 · Speaker 1

Well on both source and target data

### 00:13:52 · Speaker 1

Oftentimes what happens is that suppose you want to let me just give you an example uh suppose you want to uh you are you want to build a classifier

### 00:14:06 · Speaker 1

Mm so what a waste

### 00:14:12 · Speaker 1

So some examples in the list.

### 00:14:27 · Speaker 1

Give me a minute I'm just looking for that image

### 00:14:38 · Speaker 1

Yeah this is good hold on let me share my screen

### 00:14:48 · Speaker 1

You see my screen?

### 00:14:54 · Speaker 4

Marius

### 00:14:55 · Speaker 1

So you look at this. So there are these data sets. There is MNIST, there is USPS, something called MNIST-M, and there is the street view house numbers data set. Now what you see is that all of these are semantically the same. The class-wise they all have the same, right? They have digits. But if you build a classifier on, let's say, MNIST and try to test it on USPS,

### 00:15:25 · Speaker 1

it will not give you good performance

### 00:15:31 · Speaker 1

Now the goal is that suppose you are given

### 00:15:34 · Speaker 1

data from MNIST with labels and data from USPS without labels. That is the setting, right? Where you understood the setting that there is a source domain which has labels and there's a target domain which has data but does not have labels.

### 00:15:52 · Speaker 1

Now the task is that you have to build representations such that

### 00:15:57 · Speaker 1

The classifier that is trained on the source data does well on the target data as well. That is the problem setting.

### 00:16:07 · Speaker 1

Is it clear any questions

### 00:16:09 · Speaker 1

So you have to ensure that the problem definition is clear then we will move on

### 00:16:14 · Speaker 1

Please ask if you have any questions. I can see your sir. Yes, Shivan. Yes, sir. When we say we want to learn this on the the the model should perform well on the target distribution as well eventually we will be passing target distribution back to the model.

### 00:16:32 · Speaker 2

get the respective target labels right

### 00:16:36 · Speaker 1

The final evaluation will be done with target labels of course but while you are building the model you don't have target labels.

### 00:16:47 · Speaker 1

Of course I mean you can evaluate the definitely it will be based on the target labels only but yeah

### 00:16:55 · Speaker 1

I don't see yeah uh Satya go on

### 00:16:59 · Speaker 2

So sir isn't it the cycle young the same right Richard only that we don't have the label for the first data set or the second set or something

### 00:17:04 · Speaker 1

No, see, in cycle again, the objective is to convert the source data to target data, right? Generate samples from target data. Here, you know, you're not, the objective is not to generate the target data, it is to build a classifier or representation such that it does well on target data as well.

### 00:17:26 · Speaker 2

Okay okay to produce a label over that argument

### 00:17:33 · Speaker 1

Send it

### 00:17:35 · Speaker 4

you answered my question so basically we are trying to

### 00:17:37 · Speaker 1

Basically we are going to move on. Let's move on. Then let's move on, please, because there's too many things to cover today. If I've answered your question, let's move on. Okay. So that's the, uh, the, um, okay. I'll have to share it again.

### 00:17:54 · Speaker 1

What is the problem setting? See there is also another class of problems right where you do not even have data from the target distribution. Those set of problems are called domain generalizations.

### 00:18:08 · Speaker 1

This is domain adaptation. Suppose you don't have DT as well. Then those class of problems are called domain generalization. We are not looking at domain generalization. Now we are looking at domain adaptation, where target data is also present, albeit without labels. How do you solve this question, solve this problem? There are multiple methods that people have come up with. One of them is what is called as domain adversarial networks.

### 00:18:50 · Speaker 1

Way networks serial networks okay what is done is the following I'll show so there is a

### 00:19:02 · Speaker 1

Each are extractor let us call that as some phi of x

### 00:19:07 · Speaker 1

This will take excess which is the source data

### 00:19:12 · Speaker 1

think let us okay x and x cap right x is the source data and they'll also take

### 00:19:24 · Speaker 1

Is it target data as input? Okay. It'll give you the corresponding representations. So let's call it as ZS.

### 00:19:35 · Speaker 1

ZT it ended here

### 00:19:42 · Speaker 1

Okay, so this is a simply a feature extractor. So this P is a function that will take X and it will give you some features Z. Okay, then what we will do is there is a classifier, there is a critique network here or a discriminator network here.

### 00:20:06 · Speaker 1

EW this will take a Z so this will take either ZS okay sorry ZS

### 00:20:15 · Speaker 1

and Z T

### 00:20:19 · Speaker 1

Okay now I should say that uh

### 00:20:24 · Speaker 1

P of X is equal to ZS okay and P of X cap is is GT okay that is how I have represented it

### 00:20:36 · Speaker 1

Now what I do is I will

### 00:20:44 · Speaker 1

Find this thing

### 00:20:55 · Speaker 1

This will be trained adversarially okay

### 00:21:01 · Speaker 1

The gun

### 00:21:04 · Speaker 1

To ensure

### 00:21:08 · Speaker 1

distribution of Zs okay

### 00:21:13 · Speaker 1

close to the distribution of Zt

### 00:21:17 · Speaker 1

Correct. That is what if I try this adversarially, right, then what happens is that the distribution of features PGS will be close to the distribution of PCT. Do you agree?

### 00:21:30 · Speaker 1

See this uh whatever I have uh uh okay

### 00:21:40 · Speaker 1

Marked with red colour this is again okay

### 00:21:45 · Speaker 1

Ow

### 00:21:47 · Speaker 1

It shows

### 00:21:51 · Speaker 1

ECS is the same as ECT

### 00:22:00 · Speaker 1

Does it make sense

### 00:22:03 · Speaker 1

Now phi of x will become the generator okay and there is another discriminator that is there and you are ensuring you are training it adversarially to ensure that PZS is equal to PZT. So what is the loss function here? The loss function would be that you learn your C star and W star okay such that minimize

### 00:22:32 · Speaker 1

in over phi and max over w you have an expectation of log of

### 00:22:44 · Speaker 1

GS as GS comes from PS

### 00:22:50 · Speaker 1

you have expectation of

### 00:22:55 · Speaker 1

Lot of

### 00:23:00 · Speaker 1

One minus uh

### 00:23:02 · Speaker 1

PW of Z

### 00:23:11 · Speaker 1

this uh ZT comes from

### 00:23:16 · Speaker 1

easy to

### 00:23:22 · Speaker 1

getting it so now if i train this as a gan now right what it will do is it will ensure that the features for the source data and target data follows the same distribution

### 00:23:37 · Speaker 1

Does it make sense

### 00:23:39 · Speaker 1

Any questions on this

### 00:23:51 · Speaker 1

Go on and read it

### 00:23:59 · Speaker 1

Can does it go on please

### 00:24:14 · Speaker 1

I don't know if you can uh any any can you hear me uh all of you

### 00:24:21 · Speaker 2

Yes sir

### 00:24:22 · Speaker 1

Okay, Raghavendra Govind, go on. Oh yes, in this case, the phi network that you have shown is kind of compressing the features. But I mean, is it reducing the dimensions or? Yeah, it is. Typically, z is less than, dimensionality of z is much less than that of x.

### 00:24:43 · Speaker 1

It acts like a generator now yeah

### 00:24:52 · Speaker 2

But I mean it looks very similar to the discriminator right because uh it's reducing the dimensions

### 00:24:56 · Speaker 1

Let's reduce the dimensions. No, just because it reduces the dimension, it's not a discriminator, right? It is simply a neural network that transforms X from Z, X to one random variable to other. It can increase the dimension, reduce the dimension, doesn't matter.

### 00:25:11 · Speaker 1

Of course, it is similar to discriminator in the sense that it reduces the dimensionality, but yeah, it is not a classifier, right? Which is trying to give a number between zero and one.

### 00:25:25 · Speaker 1

Okay so this is uh uh Yamiwake

### 00:25:29 · Speaker 2

So what does it mean X and X cap So are we passing it in sequence or are we

### 00:25:34 · Speaker 1

In sequence or are we? Yeah, sequence, sequence, yeah. So you X, when X goes, ZS comes out. When X cap goes, so ZT comes out.

### 00:25:42 · Speaker 2

technical some

### 00:25:45 · Speaker 1

Here in additional to that there's also a classifier here okay

### 00:25:55 · Speaker 1

This classifier it's called the task H theta it will take z

### 00:26:04 · Speaker 1

as input, the s as input and it will give you y as output which are the which is trained on only the source domain. Okay. Now this

### 00:26:21 · Speaker 1

He does start

### 00:26:32 · Speaker 1

Theta star okay simply the minimizer

### 00:26:37 · Speaker 1

of the cross entropy loss which is

### 00:26:51 · Speaker 1

GES coming from PS simply the minimizer of the usual cross entropy loss we can train supervised in a supervised way

### 00:27:02 · Speaker 1

Now the gradients flow like this

### 00:27:10 · Speaker 1

So the gradients for the free network right one there is

### 00:27:15 · Speaker 1

backward pass from here to here

### 00:27:19 · Speaker 1

It is learned at OCLE and then there is another backward pass which is which is supervised training that goes from

### 00:27:29 · Speaker 1

Yeah two inches

### 00:27:31 · Speaker 1

But this is supervised classification

### 00:27:36 · Speaker 1

You're supervised

### 00:27:38 · Speaker 1

And this

### 00:27:41 · Speaker 1

This is our new CD

### 00:27:49 · Speaker 1

So now what is happening is that this fee network is trying to learn features okay in such a way

### 00:27:58 · Speaker 1

One, it will ensure that the distribution of the features on source data and target data are exactly the same. This is done via adder serial optimization. And the features are also learned in such a way that it does classification well on source domain.

### 00:28:20 · Speaker 1

Okay, now during inference, what do you do? Finally during inference.

### 00:28:32 · Speaker 1

inference okay uh you take x cap coming from pt okay and then pass it through phi star which is will give you gt then take gt

### 00:28:49 · Speaker 1

and pass it through the

### 00:28:56 · Speaker 1

Classifier this will give you the labels which are the predicted labels on

### 00:29:11 · Speaker 1

T

### 00:29:14 · Speaker 1

Does it make sense? So this this is how you are doing so what you are doing is you are trying a classifier on source data okay

### 00:29:24 · Speaker 1

using features that have the same distribution as that of the target data. Now, you basically are training a classifier that has exactly that is working on a feature space whose distribution follows exactly that of the features of the target and you are ensuring that it will happen, you are enforcing that it will happen via adversarial training. Okay, so now once it is done, the features that are extracted

### 00:29:54 · Speaker 1

for the source data is same as the features for the target data. So now if you take the features for the target data and pass it through the classifier that is trained on source features.

### 00:30:07 · Speaker 1

It is expected to do well on the the the features of the target data because you have ensured via R do serial training that the features the distribution of the features of the source data is same as the distribution of the features of the target data

### 00:30:25 · Speaker 1

This thing is called domain adversarial training and it is shown to be a very, very effective method in reducing the problems with unsupervised domain adaptation.

### 00:30:37 · Speaker 1

Okay, uh, any questions on this method?

### 00:30:44 · Speaker 1

Yeah locations

### 00:30:46 · Speaker 2

Sir is it necessary to back propagate through phi from H of the theta as well?

### 00:30:53 · Speaker 1

Yes, because otherwise what will happen? No, the features that have been learned, okay, may not be such that they are conducive for classification.

### 00:31:04 · Speaker 1

So you'll have to ensure that the classification also happens. The classification on the source data has to happen.

### 00:31:13 · Speaker 2

Can't that be captured by H of theta itself

### 00:31:19 · Speaker 1

H of theta is strain no you have to strain H of theta

### 00:31:22 · Speaker 2

Yeah yeah so during that training on the

### 00:31:25 · Speaker 1

No no it wasn't it your question you are saying just use the zs and try in h of theta separately is what you are saying z

### 00:31:32 · Speaker 2

Right right

### 00:31:34 · Speaker 1

Why do you have to try and feed together with HF data is that your question

### 00:31:38 · Speaker 2

Right right

### 00:31:39 · Speaker 1

See if you if you take a ZS separately and try an H of theta what will happen is the features that have been learned to ensure that these two distributions are same may not be useful for the classification for instance what can happen is

### 00:31:56 · Speaker 1

Suppose both of them for all x right or both of I mean the PGS and PGT are such that they give you one vector for all data points. Let's say that they all collapse.

### 00:32:10 · Speaker 1

So if that happens even then the distribution matches PCS and PGT matches if for all x it will give you one vector but that that is not useful for classification.

### 00:32:25 · Speaker 1

Understood. So the features that have been learned have to be such that they are useful for classification and that's why you have the classification objective also together while you are training it.

### 00:32:27 · Speaker 2

The future

### 00:32:38 · Speaker 2

Okay

### 00:32:46 · Speaker 1

Uh stands it

### 00:32:49 · Speaker 4

Sir can you please explain once again this process like how we are training and like how we are doing these like taking the supervised classification and the discriminative part back propagation together

### 00:33:01 · Speaker 1

Help diminish

### 00:33:07 · Speaker 1

See, first you take the source data, pass it through this V network, you get a feature ZS, right? And then you have, then you take XCAP, pass it through that network. I mean, you initialize this V network randomly, you get ZT, okay? Now ZS become your, ZS becomes your true data and ZT becomes your generated data and use those with a discriminator to adversarially backpropagate VZ through the

### 00:33:37 · Speaker 1

phi x network and ensure that the distribution of zs and zt are the same this is the usual GAN training

### 00:33:48 · Speaker 1

The only difference between a usual GAN training and this is that in a usual GAN, right, the real data is not passed through the network, right? Generator network. You assume that it's already there with you. But here, GS becomes your real data and GT becomes your generated data. I use that to ensure, use that with a discriminator to ensure that the distributions are same, that is GAN training.

### 00:34:14 · Speaker 1

Okay, then you have another classifier which is trained together with the GAN where this classifier takes data from the source features and predicts the source labels and train it in a supervised way.

### 00:34:28 · Speaker 1

Now the the the this phi network which is the feature extractor will be trained both using the adversarial objective and the supervised objective together so that it has to ensure that the distributions of source and target data matches while the classification also happens properly

### 00:34:53 · Speaker 4

so sir these X and X cap these are from the available input

### 00:34:58 · Speaker 1

I have defined it already. I mean, you should not forget. See, this is ds and dt are given. So x is the samples from ds and x cap are samples from dt. They're given.

### 00:35:17 · Speaker 1

That is what is given now

### 00:35:23 · Speaker 1

Uh

### 00:35:28 · Speaker 1

What do you mean there is only

### 00:35:28 · Speaker 2

Perfect

### 00:35:30 · Speaker 1

Credible data only from the source

### 00:35:35 · Speaker 2

A generative model here I mean adds to this supervised learning because we could also directly train the H network over

### 00:35:45 · Speaker 1

But why would what yeah if you do that then what is the guarantee that the X if you suppose you train a classifier on X and pass X cap through it it will have a very bad performance

### 00:35:45 · Speaker 2

Like why would you

### 00:35:58 · Speaker 1

Because why is that

### 00:35:58 · Speaker 4

Why is that so

### 00:36:00 · Speaker 1

Because PS and PT are not the same, no? Distributions and PS and PS and PT are not the same. That's why I showed you that picture, right? Where you had the MNIST and the SVHN data.

### 00:36:13 · Speaker 1

Right the distribution of PS and PT are not the same I should make maybe write it explicitly see here

### 00:36:22 · Speaker 4

They must be close enough right

### 00:36:24 · Speaker 1

will not be uh that is the problem with domain adaptation when the id assumption breaks right when the resource data is not equal to the target data the classifier trained on one will fail miserably on the other so you can you can

### 00:36:39 · Speaker 2

If you go back to the diagram right so does it mean

### 00:36:43 · Speaker 2

the fine the the fee network is actually uh extracting features which are common across distribution is that

### 00:36:49 · Speaker 1

yeah yeah it is ensure it is ensuring that the features are extracted in such a way that across both the distributions the features have uh features are same level see while pt right pt is or rather

### 00:37:06 · Speaker 1

And PS is not equal to PT right PGS is equal to PCT by construction that is the point

### 00:37:12 · Speaker 2

S that's what we are trying to identify which is the distribution which

### 00:37:17 · Speaker 4

overlapping between those two

### 00:37:18 · Speaker 1

We are not identifying that way. So not that we should not say that there is there exists a distribution that overlaps. We are trying to extract enforce features such a way that for both the distributions they match.

### 00:37:34 · Speaker 1

Anything else?

### 00:37:38 · Speaker 1

also called DAN, okay? Domain Network Serial Networks or DAN. Powerful technique and it has... See, actually I wanted to include this as a part of assignment, but I thought it will be too much. So if anyone is interested, you can try that out. Take MNIST and the UPS dataset.

### 00:37:56 · Speaker 1

samples also here this can be

### 00:38:04 · Speaker 1

This can be UPS data. You train a classifier on MNIST and test it using UPS dataset, you will see a drastic reduction in accuracy.

### 00:38:18 · Speaker 1

Okay now and then you do this domain over serial networks and see the accuracy on the target data will increase considerably

### 00:38:32 · Speaker 1

Okay so that's about it yeah see the last thing

### 00:38:39 · Speaker 1

The Ganss's

### 00:38:50 · Speaker 1

Time is too short and we have so many things to discuss

### 00:38:58 · Speaker 1

It's supposed to be uh

### 00:39:01 · Speaker 1

content for at least two courses if not more okay so the last thing that I'll talk about for GANS in GANs is this thing called the versus trains GANS okay

### 00:39:16 · Speaker 1

This is needed only for that FID thing otherwise we could have uh

### 00:39:21 · Speaker 1

that can we do it

### 00:39:45 · Speaker 1

Buses trains you know an optimal transport

### 00:40:03 · Speaker 1

W you guys

### 00:40:07 · Speaker 1

Okay so now you know that for the F divergence minimizers right

### 00:40:20 · Speaker 1

very unstable in practice so you have already seen that right the GAN training is it's very difficult

### 00:40:32 · Speaker 1

Writing in Ghan is very difficult because

### 00:40:35 · Speaker 1

So this is something that you have seen right, ganttiring is very difficult because of that saddle point problem that is there. Okay, that is one problem. The question is, question is

### 00:40:50 · Speaker 1

What makes turn training hard okay

### 00:41:05 · Speaker 1

So in in in this paper which is called was a strange again what they show is the following suppose

### 00:41:15 · Speaker 1

So you have uh what is the notation that we are using for that p x and p theta right suppose p x and p theta are such

### 00:41:30 · Speaker 1

Yes

### 00:41:34 · Speaker 1

supports okay

### 00:41:38 · Speaker 1

Don't overlap

### 00:41:44 · Speaker 1

Now I will explain what this means. See px and p theta, okay first of all, px and p theta, okay.

### 00:41:53 · Speaker 1

are distributions

### 00:41:59 · Speaker 1

distributions over x right which is typically some d dimensional real space correct this is how it is now typically

### 00:42:14 · Speaker 1

Oh

### 00:42:16 · Speaker 1

distributions

### 00:42:19 · Speaker 1

Real data okay real data

### 00:42:24 · Speaker 1

Light is over

### 00:42:28 · Speaker 1

or a small subspace

### 00:42:36 · Speaker 1

So called as manifold

### 00:42:43 · Speaker 1

The ambient space Rd

### 00:42:47 · Speaker 1

explain what this means okay hold on

### 00:42:57 · Speaker 1

Here is what I mean. Suppose you are generating or rather generating data like this. Let's say that I toss a coin. Okay. And then if it's head, I will fill this pixel with one. If it's tail, I will fill that pixel with zero.

### 00:43:18 · Speaker 1

Do you understand what I'm doing? I'm tossing a coin, okay?

### 00:43:22 · Speaker 1

Depending upon the outcome of that coin, I will decide to fill this particular pixel. Let's say that I have a grid of, let's say, 24 by 24 or 28 by 28, I think. MNIST is 28 by 28. Now I'll fill these pixels, 784 pixels like this. I toss a coin. If it's head, I will fill that pixel with 1. If it's tail, I will fill that pixel with 0.

### 00:43:48 · Speaker 1

Okay, the question is, what is the probability or likelihood that this procedure will generate MNIST dataset?

### 00:43:59 · Speaker 1

Do you see the question? Do you understand the question?

### 00:44:10 · Speaker 1

Okay, so now can somebody tell me what is the probability of generating MNIST via this procedure?

### 00:44:20 · Speaker 1

Yeah, it's really extremely low, right? It's actually called a typewriter monkey problem, right? Where say that you make a monkey sit on a typewriter and start typing randomly. Now, what is the likelihood that it will create a Hamlet, right? Or Shakespeare's work? What is the question? Say that it's very, very low, right? I mean, similarly, getting a data set which is semantically meaningful like MNIST.

### 00:44:50 · Speaker 1

doing this procedure random procedure is is very very low now this means that out of all possible images

### 00:45:02 · Speaker 1

binary images MNIST occupies a very very small space in 784 dimensional space

### 00:45:11 · Speaker 1

Do you see that?

### 00:45:14 · Speaker 1

See this this example was to show that out of all possible points in 784 dimensional space MNIST occupies a tiny region. That is what I have written here right distributions over real data lies on a very small subspace or manifold in the ambient space Rd.

### 00:45:36 · Speaker 1

Does that make sense

### 00:45:40 · Speaker 1

So now what is the consequence of this the consequence of this is this implies

### 00:45:47 · Speaker 1

Does a high chance

### 00:46:00 · Speaker 1

supports supports meaning the points where the distributions are non-zero okay that supports of

### 00:46:11 · Speaker 1

of px and p theta r

### 00:46:24 · Speaker 1

H and P theta are are not perfectly aligned

### 00:46:36 · Speaker 1

Right, because we are talking about of two distributions, right, in RD. And we know that distributions of images are actually supported on a very tiny space in RD. So if I take two distributions that are in RD, then their supports will not be perfectly aligned. Okay, there's a high chance of them being not perfectly aligned.

### 00:47:01 · Speaker 1

Now again what is the consequence of this This is it can be shown that

### 00:47:08 · Speaker 1

We shall

### 00:47:14 · Speaker 1

one can always find

### 00:47:22 · Speaker 1

A perfect discriminator

### 00:47:31 · Speaker 1

screeminator

### 00:47:35 · Speaker 1

use that uh a DW network with 100 percent accuracy

### 00:47:44 · Speaker 1

Accuracy when

### 00:47:48 · Speaker 1

supports of

### 00:47:54 · Speaker 1

Theta and Px are not the same

### 00:48:04 · Speaker 1

So this is saying that, okay, now if the supports of px and p theta, they do not align perfectly or are not exactly the same, then you can always find a discriminator with 100% accuracy.

### 00:48:18 · Speaker 1

Okay, now if you find a discriminator with 100% accuracy, what does this imply? This implies that the GAN training

### 00:48:32 · Speaker 1

That's it.

### 00:48:36 · Speaker 1

The moment you you find the discriminator with 100% accuracy, there is no signal to the generator to learn, isn't it? Because it is perfectly classifying, that's all you are done, right? So GAN training simply saturates and this is the reason, okay, why GAN training becomes difficult. So let me tell you what I said. See, the argument that is given is first thing is that the data that is lying, I mean, that that is that that

### 00:49:06 · Speaker 1

that occurs naturally like images and text and all that. They occupy a tiny manifold or tiny little space in the ambient space. Okay. Now this means that the true data and the generated data, okay, they both lie on tiny manifolds and those tiny manifolds may not perfectly align.

### 00:49:27 · Speaker 1

Now, if they do not perfectly align, even if there is a single point where there is misalignment, then it can be shown that in such cases, you can always find a discriminator that is perfect. Now, once you find a perfect discriminator, then the gain training simply saturates. So, this can also be said in a different way, saying that this means that for

### 00:49:54 · Speaker 1

P x and P theta

### 00:49:58 · Speaker 1

Misaligned supports

### 00:50:03 · Speaker 1

Misaligning supports

### 00:50:15 · Speaker 1

This align supports okay if you take any f divergence

### 00:50:23 · Speaker 1

This will this will be either infinity or some constant

### 00:50:30 · Speaker 1

Let me say it's a constant

### 00:50:35 · Speaker 1

become a constant now it will what if it becomes constant does it become independent of theta it becomes independent of theta then that's all right i mean gant training simply saturates because the divergence you're calculating is independent of theta and there is no way that you can learn it learn more

### 00:50:56 · Speaker 1

This is why mode collapse also happens. This happens all the time. So the the respite or solution for this is solution for this is

### 00:51:08 · Speaker 1

Use a softer metric

### 00:51:15 · Speaker 1

Softer divergence metric

### 00:51:23 · Speaker 1

that

### 00:51:26 · Speaker 1

It quantifies

### 00:51:32 · Speaker 1

Close

### 00:51:35 · Speaker 1

Give me any full results

### 00:51:39 · Speaker 1

called support manuals are

### 00:51:46 · Speaker 1

supports of we are talking about p x and p theta okay instead

### 00:51:53 · Speaker 1

Instead of instead of

### 00:52:00 · Speaker 1

Measuring if they overlap or not

### 00:52:06 · Speaker 1

They're perfectly aligned or not okay

### 00:52:17 · Speaker 1

This is demotivation so what we are saying is

### 00:52:20 · Speaker 1

If the manifolds do not perfectly align, then all the F divergences that we saw simply will max out or rather become a constant which will become independent of theta and that's why Ganttaring saturates. Instead of that, it's better to have another metric, a divergence metric that will tell you how close or far the manifolds on which distributions are supported are. Instead of just making it a constant, in fact, whenever the manifold

### 00:52:50 · Speaker 1

do not align you want that metric that you are that you are thinking of

### 00:52:56 · Speaker 1

just measure how far or close the manifolds are without uh no just maxing out or becoming a constant so if this happens right what what we are saying is that you know you can't find a perfect discriminator and that is why the gan training does not saturate

### 00:53:16 · Speaker 1

Okay So we will see I mean this metric happens to be that metric is what is called as the versus stains metric

### 00:53:29 · Speaker 1

So called as the optimal transport

### 00:53:38 · Speaker 1

I'll define in a while. Yeah before that before we go to the definitions I'll take questions on the discussion so far. Any questions?

### 00:53:50 · Speaker 1

Yes and it

### 00:53:52 · Speaker 4

Sir what what do we mean by the support here

### 00:53:57 · Speaker 1

If you take a distribution supports are the points on which distribution is non-zero

### 00:54:16 · Speaker 4

Selling

### 00:54:16 · Speaker 1

Exactly

### 00:54:19 · Speaker 1

If you take a uniform distribution between let's say A and B, support of distribution is set A B.

### 00:54:28 · Speaker 1

on which the distribution is non-zero

### 00:54:33 · Speaker 1

it all right so Gaussian distribution right will have infinite support for instance

### 00:54:39 · Speaker 1

It's a set okay it's a set over which the data has been observed

### 00:54:51 · Speaker 1

Any other question

### 00:55:02 · Speaker 1

I got a window

### 00:55:03 · Speaker 4

Yeah so here we are only trying to say that if the supports match then they are close enough so we are not really looking at the divergence metric in addition

### 00:55:12 · Speaker 1

No in fact divergence

### 00:55:15 · Speaker 1

We we do compare distributions okay I mean we saw that right we actually compare distributions okay but the thing is

### 00:55:25 · Speaker 1

If the distributions, the real, I mean, if the distribution that we are comparing will have a mismatch, okay, in terms of non-alignment, then what this paper says is that you can always find a perfect discriminator and that's why training becomes unstable.

### 00:55:44 · Speaker 1

So you basically the motivation is that you need another alternative metric. Okay. That is not over dependent on alignment of the supports of these distributions.

### 00:55:57 · Speaker 4

So I mean it's in in in addition to uh the divergence minimization or this is a separate way to optimize

### 00:56:04 · Speaker 1

Uh, see, you minimize the divergence only. Basically, you minimize the divergence, but the divergence metric that you are coming up with is not sensitive to a misalignment between supports. That's all.

### 00:56:19 · Speaker 1

Okay so Wasserstein's metric is also a divergence minimization metric only so so given two distributions

### 00:56:38 · Speaker 1

P x and P theta the boson's strain metric between them is defined as follows

### 00:56:50 · Speaker 1

keeping some details here because you know you won't have a lot of time so this is metric is given as the minimum

### 00:57:01 · Speaker 1

expectation of

### 00:57:12 · Speaker 1

They have the two norm and this expectation is over

### 00:57:17 · Speaker 1

X and X square they come from

### 00:57:23 · Speaker 1

new and this minimization is over all new okay which belongs to a joint distribution between px and p that I will explain all this

### 00:57:35 · Speaker 1

Give me a minute write that down and then explain

### 00:57:55 · Speaker 1

This is the definition of the Wasserstein's distance. Okay. Okay, I'll tell you what this means. Now suppose there are two discrete distributions. Okay.

### 00:58:08 · Speaker 1

I'll do it in one dimensions to ensure that the idea is clear. So let's say that this is X. There is another distribution which is a histogram.

### 00:58:22 · Speaker 1

x squared let's say that this is this is p x and this is p x cap or p theta

### 00:58:33 · Speaker 1

Okay now

### 00:58:41 · Speaker 1

The mass

### 00:58:45 · Speaker 1

in px px can be

### 00:58:50 · Speaker 1

redistributed

### 00:58:59 · Speaker 1

What's that

### 00:59:02 · Speaker 1

It transforms

### 00:59:06 · Speaker 1

p theta do you agree

### 00:59:10 · Speaker 1

the mass in px can be redistributed okay such that it will transform to morph into p theta do you agree how do we do that

### 00:59:26 · Speaker 1

So it's like this. How do we do that? We take, let's say that this is this is x1 and this is some xk. You take some mass from x x1 and

### 00:59:39 · Speaker 1

reduce it and put it to x2 and so on right i mean you can redistribute the mass in px so that it will get transformed to p theta isn't it do you agree

### 00:59:54 · Speaker 2

But usually we are not supposed to touch X right so it's like a source distribution

### 01:00:01 · Speaker 1

No, no, no. See, forget about source and target and all that now. I'm just simply saying given two distributions, you can always change the distribute mass in one distribution to get it marshed into some other distribution, correct?

### 01:00:19 · Speaker 1

Now the fingers

### 01:00:22 · Speaker 1

Now this redistribution

### 01:00:31 · Speaker 1

redistribution can be expressed

### 01:00:40 · Speaker 1

Can be expressed

### 01:00:44 · Speaker 1

as a table

### 01:00:47 · Speaker 1

Let's say that this has this has uh k and this is

### 01:00:52 · Speaker 1

X cap one two X cap

### 01:00:58 · Speaker 1

Okay now I will write a

### 01:01:06 · Speaker 1

Okay in this direction this is excel sorry x cap

### 01:01:12 · Speaker 1

in this direction it is

### 01:01:16 · Speaker 1

This is X one through XK, and this is

### 01:01:23 · Speaker 1

Uh it's one cap rule

### 01:01:29 · Speaker 1

Right. So what I'm saying is how much mass should I take from X1 and should I put it in, let's say here. So let's say that I put the 0.3% of X1 here and I put 0.2% of it and I'll write 0.01% of X1 here and then redistribute amongst all X1 cap through XL. Same thing with X2 also, right? I take 0.1% and 0.4% and 0.02% and so on.

### 01:01:59 · Speaker 1

Do you see that? So what I'm saying is every row here is telling me how much mass how should I redistribute 1x k okay amongst all possible x caps such that it will get transformed to

### 01:02:14 · Speaker 1

I mean p theta do you agree

### 01:02:25 · Speaker 1

And every row should sum to one, right? Because you can, I mean, the total mass on x1 should sum to one, correct? So now this, right? What is this? If you closely look at it, is actually a joint distribution.

### 01:02:45 · Speaker 1

distribution between

### 01:02:48 · Speaker 1

P x n P theta

### 01:02:52 · Speaker 1

Shall I call it as PX cap?

### 01:02:57 · Speaker 1

It's okay you understand now X cap is coming from uh P theta

### 01:03:03 · Speaker 1

Is this okay? Px is sampled from P, x is sampled from Px here and scap is sampled from P theta. So this table, okay, which will tell you how to redistribute.

### 01:03:18 · Speaker 1

to and px to get morphed into p theta is actually a joint distribution between px and p theta

### 01:03:28 · Speaker 1

Any questions so far

### 01:03:36 · Speaker 1

Yeah, Amitosh write this down

### 01:03:39 · Speaker 2

Shouldn't it

### 01:03:42 · Speaker 2

just p theta so that it becomes equivalent to px or is it because

### 01:03:46 · Speaker 1

No, no, no, it's uh no, no, no. See again I'm saying telling forget about it for a while. You you you forget what is p theta, what is p h. There's two distributions. Of course you can write it that way, right? I mean you say that p theta is being adjusted in GAN framework. That is what you're trying to say, right? Yeah, yeah. In general, doesn't matter. No, in general I'm defining divergence metric between two distributions. Can mean anything.

### 01:04:12 · Speaker 1

That is why if it's confusing for you let me

### 01:04:16 · Speaker 1

Change it

### 01:04:26 · Speaker 1

There's more

### 01:04:28 · Speaker 1

find and replace here so you have to do it manually

### 01:04:55 · Speaker 1

Any other questions on this?

### 01:04:59 · Speaker 1

So a joint distribution between

### 01:05:03 · Speaker 1

between px and p theta px cap now px cap okay specifies

### 01:05:12 · Speaker 1

Specifies a transport plan it's called a transport plan

### 01:05:22 · Speaker 1

Transport plan okay

### 01:05:26 · Speaker 1

B X N B X Capp

### 01:05:29 · Speaker 1

Now, if you give me a joint distribution between Px and P, Px and Pxcap, I'm simply saying every joint distribution is telling me how to convert or redistribute masses in Px such that it gets mapped to Pxcap. Do you agree?

### 01:05:53 · Speaker 1

No

### 01:05:55 · Speaker 1

Suppose

### 01:05:59 · Speaker 1

Suppose now I move suppose a mass

### 01:06:05 · Speaker 1

X cap okay is or rather X is more

### 01:06:12 · Speaker 1

X is more to X cap

### 01:06:17 · Speaker 1

move to x gamma right then

### 01:06:21 · Speaker 1

Norm between x and x cap gives you the distance

### 01:06:27 · Speaker 1

movement

### 01:06:32 · Speaker 1

I am evaluate

### 01:06:35 · Speaker 1

The joint distribution at these points x current x gap, you the mass.

### 01:06:43 · Speaker 1

That wasn't work

### 01:06:49 · Speaker 1

Right. This much of mass was moved this much of distance. So now P xx graph, which is the joint distribution between these two. If you multiply this with this thing. So what is distance times mass?

### 01:07:10 · Speaker 1

Work done right

### 01:07:16 · Speaker 1

moving

### 01:07:19 · Speaker 1

You lost

### 01:07:23 · Speaker 1

y a distance of x minus x cap

### 01:07:39 · Speaker 1

Mass into distance is the work done, right? By definition. Now, if I take

### 01:07:46 · Speaker 1

integrate this okay over the entire joint distribution

### 01:08:09 · Speaker 1

What will this be for me

### 01:08:12 · Speaker 1

This is by definition the expectation of

### 01:08:17 · Speaker 1

Over the joint distribution of PXX cap. What is this? This is the

### 01:08:25 · Speaker 1

Average work done

### 01:08:32 · Speaker 1

in a transport plan

### 01:08:40 · Speaker 1

So fire by

### 01:08:48 · Speaker 1

You will agree

### 01:08:52 · Speaker 1

Now every joint distribution between x and x cap will give me a transport plan right which would tell me how to transform one distribution to the other correct.

### 01:09:07 · Speaker 1

If I I mean uh if I multiply that if I take the expected value of uh the distance between uh the supports okay over the joint distribution it will tell me the average work done in a transport plan that is specified by the joint distribution

### 01:09:25 · Speaker 1

Everybody agree on this?

### 01:09:37 · Speaker 1

Are you audible

### 01:09:40 · Speaker 1

Yes yes yes

### 01:09:41 · Speaker 2

Yes it will

### 01:09:42 · Speaker 1

Okay, is this clear? Okay. Now the question that I'm asking is,

### 01:09:48 · Speaker 1

Give one

### 01:09:53 · Speaker 1

Multiple transport plans that are possible

### 01:10:03 · Speaker 1

Every transport plan is a joint distribution mind you right

### 01:10:08 · Speaker 1

and distributions okay possible

### 01:10:15 · Speaker 1

between two random variables X and X cap okay

### 01:10:25 · Speaker 1

Which one

### 01:10:28 · Speaker 1

has the least work done

### 01:10:37 · Speaker 1

In other words

### 01:10:44 · Speaker 1

In other words what is

### 01:10:48 · Speaker 1

What is the least work done

### 01:10:56 · Speaker 1

Who transform

### 01:11:02 · Speaker 1

PX2 PX cap

### 01:11:06 · Speaker 1

you specify this so now what you do is that if you take a joint distribution new okay

### 01:11:15 · Speaker 1

is a joint distribution between x and x cap okay this will give you the work done

### 01:11:22 · Speaker 1

via that joint distribution. Now amongst all possible transport plans or the joint distribution that will take PX to PCAT, give me the one

### 01:11:37 · Speaker 1

Y okay represents represents

### 01:11:44 · Speaker 1

set of all possible joint distributions between X and X cap.

### 01:11:53 · Speaker 1

All possible

### 01:11:58 · Speaker 1

joint distributions or transport plans right

### 01:12:04 · Speaker 1

So every joint distribution is a transport plan

### 01:12:10 · Speaker 1

between x and x caps

### 01:12:13 · Speaker 1

So this is seeking what is this seeking this is seeking the least

### 01:12:21 · Speaker 1

I don't know

### 01:12:24 · Speaker 1

Transport plan

### 01:12:32 · Speaker 1

Least average work

### 01:12:46 · Speaker 1

You see this? So I'm saying amongst all possible joint distributions or amongst all possible ways that I can transform my PX to PX cap, give me the one

### 01:12:59 · Speaker 1

That corresponds to the least work done

### 01:13:05 · Speaker 1

Do you agree do you see this

### 01:13:17 · Speaker 1

Oh

### 01:13:20 · Speaker 1

This is what is called as the versus trains distance

### 01:13:25 · Speaker 1

What is this distance between?

### 01:13:32 · Speaker 1

distributions Px and Px cap

### 01:13:37 · Speaker 1

The minimum, okay, and please note the minimization is over, minimization is over all possible transport plans, okay, that would transform PX to PX cap. Now the question that I'm asking is amongst the new is...

### 01:13:55 · Speaker 1

joint distribution between

### 01:13:59 · Speaker 1

You belong to

### 01:14:03 · Speaker 1

Set pi okay is a joint distribution

### 01:14:13 · Speaker 1

Excellent

### 01:14:15 · Speaker 1

Now amongst all possible joint distributions that would transform Px to Px cap, give me the one that has the least work done. So that is the Vortzestraun's distance. Now you can see that

### 01:14:33 · Speaker 1

lesser the versus strains distance okay

### 01:14:39 · Speaker 1

Closer R, PX and PCAP isn't it?

### 01:14:43 · Speaker 1

Because if PX and PX cap are close, then the amount of work that you should do to bring PX to PX cap will be least. Now there can be other transport plans that would, I mean even if PX and PX cap are close, there can exist transport plans that would have a, that would, that would involve a lot of work. But since we are seeking the minimum work done to transform PX to PX cap, if they are close enough,

### 01:15:13 · Speaker 1

then you don't have to do a lot of work to transform Px to Px cap

### 01:15:18 · Speaker 1

That's why it's a distance metric between two distributions

### 01:15:24 · Speaker 1

So this is also called that's why it's also called no optimal transport Wasserstein's metric is also called as optimal transport

### 01:15:36 · Speaker 1

Any questions on the definition

### 01:15:52 · Speaker 1

Is there any question

### 01:16:00 · Speaker 4

Not those

### 01:16:01 · Speaker 1

My art is good

### 01:16:06 · Speaker 1

Okay, great. Okay, so now this is shown to be a softer metric, right? So versus change distance is a softer metric, okay, compared to

### 01:16:24 · Speaker 1

Compared to F divergence

### 01:16:28 · Speaker 1

in the sense that

### 01:16:33 · Speaker 1

It will not

### 01:16:37 · Speaker 1

to max out right or saturate

### 01:16:47 · Speaker 1

Accurate

### 01:16:50 · Speaker 1

But misaligning okay what does D

### 01:16:58 · Speaker 1

alignment of the supports this is the greatest thing right i mean that you can use the versus strength metric uh to i mean it will become much stabler if you use versus strength metric now how is this related to adversarial learning is that so the next question is

### 01:17:18 · Speaker 1

Continue the class till 11 15 right and then we will take a 10 minutes break okay let's finish this the question is

### 01:17:28 · Speaker 1

how to build a generative model

### 01:17:40 · Speaker 1

optimizes the versus change metric okay this is a good metric fine now how do we build a generative model that would

### 01:17:48 · Speaker 1

optimizes the versus strength metric

### 01:17:55 · Speaker 1

So thankfully there exists this duality, okay, which is called the Kontrovich-Rubinstein's duality.

### 01:18:12 · Speaker 1

That says that versus strain's distance between two distributions Px and P theta okay can be expressed as a maximum okay

### 01:18:25 · Speaker 1

set of functions let's call them STW

### 01:18:36 · Speaker 1

are like this I'll tell you what this is so this is

### 01:18:42 · Speaker 1

expectation

### 01:18:44 · Speaker 1

X coming from BX

### 01:18:48 · Speaker 1

Simply dw of x

### 01:18:53 · Speaker 1

expectation of

### 01:18:56 · Speaker 1

It's cap coming from b theta

### 01:19:00 · Speaker 1

have again dw of x

### 01:19:09 · Speaker 1

So now you know right I mean this so now if you want to minimize

### 01:19:22 · Speaker 1

in theta just simply you have a min

### 01:19:27 · Speaker 1

Over the tea table

### 01:19:30 · Speaker 1

And worst case in the sense is simply a max over this T w. I'll tell you what this norm of T w less than this means. And you have this usual

### 01:19:41 · Speaker 1

Classroom

### 01:19:44 · Speaker 1

We know how to approximate using sample estimates

### 01:19:50 · Speaker 1

It's got so it's got

### 01:19:58 · Speaker 1

from BT

### 01:20:01 · Speaker 1

Right so now this what is this again this becomes this became a a dosedial optimization

### 01:20:14 · Speaker 1

How do you optimize this same thing you have

### 01:20:18 · Speaker 1

Generator network

### 01:20:23 · Speaker 1

Take get take a Z

### 01:20:27 · Speaker 1

and gives you X cap coming from P theta the usual story and you have this critique network here

### 01:20:37 · Speaker 1

W of X

### 01:20:42 · Speaker 1

your real number in this case and this is

### 01:20:47 · Speaker 1

Either X or you have X cap that goes as input because you can you have to compute the expectation over both of that

### 01:20:54 · Speaker 1

And then the only constraint is that the T network right have to be one lipshitz

### 01:21:04 · Speaker 1

So what is meant by that I will just tell you

### 01:21:12 · Speaker 1

implies that if you take T w of x 1 minus T w of x 2

### 01:21:22 · Speaker 1

divided by x1 minus x2 this is upper bounded by 1 this is the definition of 1 lipschitz so i mean if you look at it it is exactly a gann right optimizing the versus trains distance is exactly a gann that's why it's called a w-gann the only thing is the discriminator network right or the critique network have to be 1 lipschitz

### 01:21:49 · Speaker 1

Of course the the uh the

### 01:21:54 · Speaker 1

form of the uh the uh loss function changes a little because there you have the expectation of f star of tw here you don't have that f function right otherwise it is simply a an adversarial optimization problem that you are solving right but with only one additional constraint that the discriminator network have to have bounded derivatives right or it should be one lipschitz now how do you make a neural network one lipschitz is a question that i'll answer in a while

### 01:22:24 · Speaker 1

But yeah so but for that it is simply again with

### 01:22:30 · Speaker 1

uh with with the objective function taking expectations over two distributions and then you optimize the advantages in a jan right what happens is or an f divergence minimizer this maximization that you are constructing no is actually a lower bound on the divergence but here there is an equality you see the versus strength metric is exactly equal to this maximization problem which is again no that's what makes it a softer metric

### 01:22:58 · Speaker 1

Now the practical implication of this is whenever you are implementing a GAN, right, always implement a WGAN because it is much more stable in terms of training. Okay. Even for your assignment, no question one and two, I would recommend that you implement a WGAN. So now how does it change? The only thing that will change is this will not be between zero and one now. It will simply, you will have a linear activation at the output.

### 01:23:31 · Speaker 1

Linear activation okay

### 01:23:35 · Speaker 1

The loss function will not have a log of D of G or something. It will simply have the output of this. It will be expectation of the output of this. So this will be a, this is the output of this network. Okay. That's one thing. The other thing is you'll have to ensure that the discriminator network is lipshitz. So now to practically.

### 01:23:57 · Speaker 1

What you do is that you

### 01:24:01 · Speaker 1

Normalize

### 01:24:04 · Speaker 1

Wait

### 01:24:09 · Speaker 1

of TW

### 01:24:15 · Speaker 1

Such that their norm is always

### 01:24:20 · Speaker 1

If you do this, then it will become one lipstick. So what you should do is after every gradient step, right?

### 01:24:28 · Speaker 1

after every ingredient

### 01:24:34 · Speaker 1

every gradient update. So after every gradient update, what you do is take the weights update, take the weights of the discriminator network and normalize them so that they will have

### 01:24:47 · Speaker 1

unit norm if you do that you become one likelihood that's all that is the only thing that you should do while you are training the bus a strain scan and this is shown to be much more stabler for training and it it will give you much better uh uh like outcomes compared to f divergence minimization even though this also happens to be a saddle point on adversarial optimization okay with the only constraint that you should have the discriminator to be one likelihood

### 01:25:16 · Speaker 1

That's about WGANs. Any questions on this?

### 01:25:24 · Speaker 1

Yes go on

### 01:25:26 · Speaker 4

So the norm that we are talking about here is the

### 01:25:28 · Speaker 2

I don't know or

### 01:25:31 · Speaker 1

Here yeah yeah this is L2 this is L2 this is L2 yeah

### 01:25:38 · Speaker 1

good that you asked that question right here when we define the versus stains metric it's always uh two that we talk about here right the two norm between x and x cap okay and the the this duality you know the control which rubinstein's duality is for versus stains two in general you can use a pth norm here if you do one norm here that will become versus stains one if you if you use two norm it will become versus stains two if you use p norm it will become p versus stains distance in general but generally

### 01:26:08 · Speaker 1

Wasserstein's two is what is used everywhere and the duality rate or the GAN formulation comes up for Wasserstein's two

### 01:26:18 · Speaker 1

Tall drinks

### 01:26:21 · Speaker 1

The water stains too

### 01:26:29 · Speaker 1

Yeah service

### 01:26:31 · Speaker 1

for calculating the norm of the network we just have to take put all the weights in a vector in any order and then just calculate the norm yeah yeah yeah yeah simply vectorize it compute the norm and divide it by the norm of it you don't have to compute it no just divide the weights every individual weight which with its norm

### 01:26:51 · Speaker 2

It works for every network and convolution also same

### 01:26:54 · Speaker 1

Yeah yeah same thing same thing yeah yeah

### 01:26:59 · Speaker 1

Okay, nothing else, right? I mean, this, see, whenever you implement a GAN, always implement a WGAN, much more stable.

### 01:27:08 · Speaker 1

Okay the final piece before we close Gyanus like how do you evaluate

### 01:27:17 · Speaker 1

generate generate if or evaluate GANs right typically

### 01:27:23 · Speaker 1

This is uh, I should not be calling it as GANs, you can do it for any generative model.

### 01:27:36 · Speaker 1

Now given

### 01:27:40 · Speaker 1

X1 through XN

### 01:27:44 · Speaker 1

For example from some distribution px typically the real data

### 01:27:51 · Speaker 1

And you have

### 01:27:54 · Speaker 1

On cap true

### 01:27:56 · Speaker 1

Excellent

### 01:27:59 · Speaker 1

It's a sample from p theta star this like the generated data post training of course right

### 01:28:13 · Speaker 1

Now the goal

### 01:28:20 · Speaker 1

Compare the closeness

### 01:28:23 · Speaker 1

It's called this as uh

### 01:28:26 · Speaker 1

T real and T generated, okay, compare DR and DG. Now, how do you compare these two? You need a metric to compare these two. Of course, now you need to resort to some distributional divergence metric only to compare DR and DG. What is done is typically, there are multiple metrics to do it. One of the famous metrics is what is called as the threshold inception distance.

### 01:29:02 · Speaker 1

Squared

### 01:29:17 · Speaker 1

Abbreviated as FID

### 01:29:20 · Speaker 1

have seen no fid is the metric that is used to evaluate the quality of generated data so what is this at the heart of it fid

### 01:29:32 · Speaker 1

is simply versus strain's metric okay

### 01:29:42 · Speaker 1

simply was a distance metric between uh uh like px cap and p theta cap but it is done in a convoluted way i'll tell you what what is done what is done in f fids

### 01:29:57 · Speaker 1

Positive this

### 01:30:01 · Speaker 1

Um pull this off

### 01:30:06 · Speaker 1

DR and DG

### 01:30:10 · Speaker 1

I'll pass them through

### 01:30:18 · Speaker 1

them to an inception network a pre-trained infection infection inception

### 01:30:26 · Speaker 1

Through an inception net that's why the name inception distance okay inception network

### 01:30:35 · Speaker 1

Retrained

### 01:30:39 · Speaker 1

Can you imagine it

### 01:30:45 · Speaker 1

then take

### 01:30:49 · Speaker 1

features

### 01:30:55 · Speaker 1

from some nth layer some different people take it uh different layers I think you know example is 64th layer

### 01:31:07 · Speaker 1

Now what was done so far is that you have a pre-trained inception network

### 01:31:22 · Speaker 1

Now you pass your x and x cap both through this and take the features at some 64th layer, right? This is you call this as z real and you know z generated.

### 01:31:39 · Speaker 1

Okay, then now you will have two data sets, right? Let's call that as D.

### 01:31:45 · Speaker 1

cap real which is

### 01:31:49 · Speaker 1

zero real one zero real two up to zero real n and you have d

### 01:31:59 · Speaker 1

generated cap which is C generated 1 C generated 2 and C generated the n so here Z R

### 01:32:18 · Speaker 1

Let's call this as some fee okay so now fee at 64th layer of

### 01:32:25 · Speaker 1

Z I

### 01:32:28 · Speaker 1

And ZGI is fee at 64

### 01:32:34 · Speaker 1

x cap i okay where phi is d

### 01:32:39 · Speaker 1

Is the pre trained inception net okay

### 01:32:49 · Speaker 1

So far so good. Any questions on this?

### 01:32:52 · Speaker 1

Given data, real data and generated data, take a pre-trained inception network, okay? Pass both of them through that and take the 64th layer features of both of them and collect them as vectors. You get two sets. Is this okay so far?

### 01:33:12 · Speaker 1

Okay now what you do is this is the third step the fourth step is that

### 01:33:18 · Speaker 1

Compute

### 01:33:22 · Speaker 1

mean and variance okay for

### 01:33:27 · Speaker 1

DR cap and DD cap

### 01:33:31 · Speaker 1

Let's call this as mu real

### 01:33:37 · Speaker 1

and sigma real

### 01:33:47 · Speaker 1

Compute mu real on z real. You compute sigma real on z real. You compute mu generated on z generated. Compute sigma generated on mu generated. Is that okay?

### 01:34:10 · Speaker 1

The first step was

### 01:34:16 · Speaker 1

Assume assume

### 01:34:20 · Speaker 1

Z real and Z generated both to be coming from Gaussian distributions

### 01:34:32 · Speaker 1

Now Z real comes from Gaussian with mu real and sigma real and Zg comes from a Gaussian from mu g and sigma g.

### 01:34:50 · Speaker 1

Then finally you compute the Versus-Training metric

### 01:34:55 · Speaker 1

Between the normal distribution at mu rian sigma rian

### 01:35:10 · Speaker 1

This is FID

### 01:35:19 · Speaker 1

is clear how to do it

### 01:35:22 · Speaker 1

Now I'll tell you this is this actually is given by a formula

### 01:35:27 · Speaker 1

Wasserstein's distance between two Gaussian distributions is given by the simple formula L minus mu g

### 01:35:37 · Speaker 1

2 squared plus the trace of

### 01:35:43 · Speaker 1

Sigma real plus sigma generated dash minus 2 sigma real sigma generated dash to the power of half

### 01:35:57 · Speaker 1

See this is a scalar because it's a norm

### 01:36:02 · Speaker 1

And this is a trace, no trace of a matrix is also a scalar. Okay. And therefore, this is the FID, which will be a scalar.

### 01:36:15 · Speaker 1

So this was a strength two metric no scalar uh so this is lower the better

### 01:36:21 · Speaker 1

distributions match then it will be zero because it is was a strange distance between two Gaussian distribution better not between

### 01:36:40 · Speaker 1

Let me show you the entire procedure

### 01:36:45 · Speaker 1

a look at it okay and let me know if you have questions on fid so this is the metric that is used to one of the metrics that is used to uh quantify the goodness of generated data and beat from gans or vae's or anything you can compute fid so what is fid let me take quickly go through the steps now

### 01:37:04 · Speaker 1

Now you have samples from the generated and the real data, pass it through a pre-trained inception network to get the features. I mean, I'm not sure if it's 64th layer or something, I'll some people, different people use different layers anyway. Okay. So now once you get those features, assume that those features follow Gaussian distribution and compute the mean and variances of them and use those mean and variances to compute the versus

### 01:37:34 · Speaker 1

two metric between these two features of real data and generated data using this formula that is your FID

### 01:37:43 · Speaker 1

Any questions on the computation of FID

### 01:37:46 · Speaker 1

asked you to compute FID right on the the data that you generate using GANS so this is the formula that you should implement there are standard implementations of FID as well yeah but this is what they do okay survey

### 01:38:02 · Speaker 1

So what is sigma g prime

### 01:38:07 · Speaker 1

Oh sorry this thing won't be on here yeah

### 01:38:19 · Speaker 1

Have a look

### 01:38:21 · Speaker 4

So I have two questions one is why why did you place so much of importance on one particular inception architecture

### 01:38:28 · Speaker 1

I didn't, I mean somebody did because if you read the FID paper, what they say is inception architecture correlates well with human perception is what they have done by doing some perception studies.

### 01:38:42 · Speaker 2

Okay, okay. Okay. Second question is

### 01:38:45 · Speaker 4

Suppose I I am modifying the problem a little bit and I ask uh like I want to see the inception I mean the uh the distance between uh generated images uh of a given style like if I'm not going to

### 01:39:00 · Speaker 1

focus on content at all and I just want to focus on style so can I modify the uh just I mean picking up the 64th layer feature vectors and instead replace them with

### 01:39:15 · Speaker 1

maybe the gram matrix or the add-in layer activations I mean and continue with the same procedure will I get a meaningful result

### 01:39:26 · Speaker 2

It is not FID, but yeah, so it is something, right? I mean, you might get some meaningful result, but it's not FID by definition, that's why. You can't say that it's the standard FID metric.

### 01:39:45 · Speaker 1

It does that for me

### 01:39:45 · Speaker 2

It does make sense

### 01:39:47 · Speaker 1

Okay fine I mean the actual problem is I want to recommend images to

### 01:39:51 · Speaker 2

Uh yeah I I so shall we take it offline because this may not be relevant to the class

### 01:39:52 · Speaker 1

I

### 01:39:56 · Speaker 1

Yes yes yes

### 01:39:59 · Speaker 2

Please swing me know we can discuss all that. Okay. Any other question on FID? Okay. So this is the

### 01:40:13 · Speaker 2

End of GANs for this course, I mean there are too many things that are there. Yeah, this is the end of generative adversarial networks. It's more on to VAEs. Yeah, so.

### 01:40:27 · Speaker 2

Okay, so we come to the end of GANs then, so let's move on to the next topic, which is variational autoencoders. Shall we take a break?

### 01:40:40 · Speaker 2

Uh okay so how long uh 11 18 shall we come back at uh yes and deep

### 01:40:51 · Speaker 2

I think yeah so we'll come back at 11 35.

### 01:40:56 · Speaker 2

And go up to 1220 perhaps and then we'll stop 1135, okay 15 minutes.

### 01:41:04 · Speaker 2

Okay see you in a while bye

### 01:59:45 · Speaker 2

Hello should we resume

### 01:59:56 · Speaker 1

Yes sir

### 02:00:06 · Speaker 2

The next class of generative models that we would consider are these variational autoencoders or VAEs. Now these come under a broad family of models called

### 02:00:24 · Speaker 2

Latent variable models

### 02:00:41 · Speaker 2

latent variable models so what do you mean by latent variable model is that you have theta

### 02:00:58 · Speaker 2

what our starting point is right

### 02:01:05 · Speaker 2

on as usual IED from an unknown distribution px okay

### 02:01:12 · Speaker 2

Suppose p theta of x denotes a model. What is a model? Model is basically a distribution over theta, right? Suppose p theta

### 02:01:24 · Speaker 2

Denotes

### 02:01:29 · Speaker 2

A morden

### 02:01:34 · Speaker 2

Latent variable model is the following

### 02:01:45 · Speaker 2

defined as follows p theta of x

### 02:01:51 · Speaker 2

given as a marginal

### 02:01:56 · Speaker 2

or the joint distribution of the data and another variable Z where Z is another

### 02:02:07 · Speaker 2

Is it this

### 02:02:11 · Speaker 2

is a hidden so I'd name latent variable okay hidden or unobserved

### 02:02:22 · Speaker 2

An object

### 02:02:24 · Speaker 2

random variable

### 02:02:33 · Speaker 2

Or this is integral

### 02:02:41 · Speaker 2

If it's continuous okay if z is discrete

### 02:03:05 · Speaker 2

Where to move that anyway

### 02:03:08 · Speaker 2

Um I actually wanted let's do that

### 02:03:19 · Speaker 2

Okay so this if

### 02:03:23 · Speaker 2

Z is discrete

### 02:03:29 · Speaker 2

C is continuous

### 02:03:38 · Speaker 2

Now where Z is hidden

### 02:03:44 · Speaker 2

or unobserved random variable

### 02:03:58 · Speaker 2

So this is the definition of a latent variable model where you express your data in terms of

### 02:04:08 · Speaker 2

marginal okay over the joint distribution of

### 02:04:14 · Speaker 2

Joint distribution between the data and one other unobserved random variable

### 02:04:21 · Speaker 2

So typically give you examples of what this is typically

### 02:04:29 · Speaker 2

Typically Z

### 02:04:34 · Speaker 2

C is also estimated

### 02:04:42 · Speaker 2

or learned

### 02:04:46 · Speaker 2

along with the model parameters theta

### 02:05:02 · Speaker 2

Okay, so basically what we are saying is for

### 02:05:07 · Speaker 2

each xi in data can there exists a zi okay correspond corresponding to xi

### 02:05:26 · Speaker 2

So that is unobserved

### 02:05:35 · Speaker 2

Now this ZI examples what is

### 02:05:40 · Speaker 2

Z is discrete okay

### 02:05:45 · Speaker 2

Let's say that z

### 02:05:50 · Speaker 2

is discrete and it is

### 02:05:52 · Speaker 2

take let's say one two

### 02:05:57 · Speaker 2

0 to like m values let's say 1 to m values

### 02:06:06 · Speaker 2

values

### 02:06:11 · Speaker 2

Given an X I

### 02:06:15 · Speaker 2

belonging to D okay Zi given this X Xi

### 02:06:28 · Speaker 2

may indicate

### 02:06:34 · Speaker 2

Indicate

### 02:06:43 · Speaker 2

Indicates

### 02:06:48 · Speaker 2

I'll see that I didn't see

### 02:06:53 · Speaker 2

zi comma xi plus test plus test

### 02:06:58 · Speaker 2

xi into

### 02:07:04 · Speaker 2

M categories

### 02:07:11 · Speaker 2

You understand so in this sense right a Gaussian mixture model

### 02:07:23 · Speaker 2

of which the K means clustering is a

### 02:07:28 · Speaker 2

special case okay are both latent variable models

### 02:07:53 · Speaker 2

Any questions on this

### 02:07:55 · Speaker 2

So basically what we are saying is the following, right? Given data, what we do is that we model our data this way, which is a marginal over the joint distribution of the data and another random variable called Z. Okay. Now what is this Z? This Z is a latent variable or an unobserved random variable that is not with data, that is not actually measured or seen with the data, but it is there with the data.

### 02:08:24 · Speaker 2

Okay, now what is the advantage of having this sort of a modeling is there are multiple reasons. One, having a latent variable model will like will enable will enable model learning. Okay, easy, easier, make it easier. In the case of Gaussian mixture model, it will make it easier algebraically easier. That is one reason. The other reason is if you have a latent variable model, you can actually get information like this, which is given a particular

### 02:08:54 · Speaker 2

X i after training right if you estimate the corresponding latent variable it will tell you if it's discrete it will tell you what cluster every X i belongs to so that is the that is the classical example of k-means clustering and Gaussian GMM clustering where they are both latent variable models which will tell you for every X i it will tell you what cluster X i belongs to the second example can be okay the first example second example is Z is continuous

### 02:09:28 · Speaker 2

It is actually an autoencoder or a VAE also

### 02:09:34 · Speaker 2

But

### 02:09:38 · Speaker 2

Zi given an xi okay can be seen as

### 02:09:58 · Speaker 2

your z then some rk it's a continuous vector can be seen as seen as

### 02:10:07 · Speaker 2

Teacher

### 02:10:12 · Speaker 2

Corresponding to it so latent variable models right will enable feature extraction

### 02:10:19 · Speaker 2

You can use zi rather than xi for downstream tasks and all that. So these are called, I mean these are feature extractors. So that's why you want to model the data xi by introducing one other random variable zi which is called the latent variable. Any questions on this motivation?

### 02:10:46 · Speaker 4

for the continuous case we are saying that zi by xi can be seen as a feature for

### 02:10:52 · Speaker 2

Or not by not by z i given x i it's a conditional random variable conditional distribution

### 02:11:02 · Speaker 2

ZI Z1XI

### 02:11:04 · Speaker 4

Sorry sorry for that zi given xi can be seen as a feature corresponding to zi

### 02:11:11 · Speaker 2

Corresponding to sorry corresponding to Xi

### 02:11:23 · Speaker 1

So the feature should be useful in some way right

### 02:11:26 · Speaker 2

Correct correct they it will be useful in some way that's the point

### 02:11:32 · Speaker 2

Latent variable models are imposed because features are useful in some way.

### 02:11:40 · Speaker 2

That's what I'm saying so now the

### 02:11:43 · Speaker 2

In the literature these latent variable models are designed in such a way that you learn the latent variable and the model parameters together.

### 02:11:56 · Speaker 2

Alright

### 02:12:04 · Speaker 2

In auto see in GANs right what did we learn we basically learn the model okay but in in in latent variable models learn the model okay but you will also learn the the latent variable together

### 02:12:26 · Speaker 2

It's on right

### 02:12:31 · Speaker 2

Okay shall we do one

### 02:12:46 · Speaker 2

Now let's look at

### 02:13:00 · Speaker 2

Can't I draw straight lines here in this thing Is there a way to do it

### 02:13:07 · Speaker 2

long press in good notes right a long press would make it a straight line here i don't know how i have to go insert line and all that that's too much

### 02:13:17 · Speaker 1

No sir that is in the draw itself

### 02:13:22 · Speaker 1

End of words off

### 02:13:22 · Speaker 2

In the woods are

### 02:13:25 · Speaker 1

These symbols are there octopencils there are one round and one square that is giving you yes

### 02:13:35 · Speaker 2

Great I will have to do this huh Okay fine

### 02:13:53 · Speaker 1

It will disturb you

### 02:14:02 · Speaker 2

Okay so this will convert into regular figures huh

### 02:14:17 · Speaker 2

Okay let's not complicate stuff maybe I will use a line and do it okay fine so now uh

### 02:14:25 · Speaker 2

Modeling

### 02:14:29 · Speaker 2

Yeah different variable models

### 02:14:41 · Speaker 2

Okay so recall so suppose

### 02:14:47 · Speaker 2

Boss

### 02:14:52 · Speaker 2

Ethiopia

### 02:14:55 · Speaker 2

Yes I'll for now use assume that the latent variables are continuous and this is my model.

### 02:15:06 · Speaker 2

Different variable model

### 02:15:17 · Speaker 2

Now again the same thing right so goal

### 02:15:23 · Speaker 2

Do you want

### 02:15:26 · Speaker 2

D

### 02:15:28 · Speaker 2

The car samples

### 02:15:33 · Speaker 2

I did samples from VX I need to

### 02:15:39 · Speaker 2

estimate

### 02:15:42 · Speaker 2

theta okay such that some divergence metric

### 02:15:48 · Speaker 2

For for VA right the divergence metric that is taken as the KL okay

### 02:15:55 · Speaker 2

Min waste

### 02:16:01 · Speaker 2

That those are good

### 02:16:08 · Speaker 2

So we need theta star

### 02:16:14 · Speaker 2

That's the minimum you can set off

### 02:16:17 · Speaker 2

E e tail between

### 02:16:21 · Speaker 2

X and E theta

### 02:16:25 · Speaker 2

Recall that this is equal to

### 02:16:29 · Speaker 2

The maximum is a rough

### 02:16:51 · Speaker 2

expected long life

### 02:16:56 · Speaker 2

Do you remember this

### 02:16:59 · Speaker 2

We had done this right

### 02:17:02 · Speaker 2

That's all of you remember this

### 02:17:08 · Speaker 4

Minimizing KL divergence is same as maximizing log likelihood.

### 02:17:13 · Speaker 2

Yeah expected log likelihood right

### 02:17:17 · Speaker 2

Maximize G law like you know, okay, this is what it is. So let's

### 02:17:24 · Speaker 2

right that we are interested in in maximizing the

### 02:17:31 · Speaker 2

likelihood function so i'll remove the expectation because uh if you maximize the likelihood for all x the expectation will also be maximized right so that's because just to make the algebra easier i mean the final loss function and everything will have an outer expectation with respect to px which will have a sum over all samples in px okay let us uh remove that to make life a little easier so our objective is to maximize the log of the likelihood under

### 02:18:01 · Speaker 2

Model p theta. Okay, so denote

### 02:18:12 · Speaker 2

log p theta of x

### 02:18:18 · Speaker 2

theta let's call that l theta now our objective is to maximize l theta okay now how do we do that under related variable model we have l theta is now equal to log

### 02:18:35 · Speaker 2

ETI topics

### 02:18:38 · Speaker 2

Now under the latent variable model

### 02:18:44 · Speaker 2

Integral

### 02:18:46 · Speaker 2

E theta X

### 02:18:54 · Speaker 2

Please let me know if uh uh if if any one of these steps are not uh clear to you okay

### 02:19:04 · Speaker 2

Okay this is because

### 02:19:08 · Speaker 2

latent variable models my p theta is the marginal over these two right that is why it is

### 02:19:14 · Speaker 2

equal to this

### 02:19:22 · Speaker 2

No

### 02:19:24 · Speaker 2

This is equal to log of

### 02:19:33 · Speaker 2

E theta X and C times

### 02:19:40 · Speaker 2

given x

### 02:19:43 · Speaker 2

divided by Q for C D one X

### 02:19:56 · Speaker 2

So that I can continue

### 02:20:02 · Speaker 2

E or Z given X is some distribution

### 02:20:11 · Speaker 2

over z so q of z given x is q of z given x is some distribution over the latent variable right you take any distribution over latent variable right you can just multiply and divide

### 02:20:30 · Speaker 2

Divide by that okay and the integral doesn't change. Is this all right?

### 02:20:35 · Speaker 2

use some distribution over the latent variable is is this okay

### 02:20:42 · Speaker 2

It can be any arbitrary distribution, doesn't matter. Okay. Now this is

### 02:20:53 · Speaker 2

Logo

### 02:21:00 · Speaker 2

expectation of

### 02:21:18 · Speaker 2

You do the sensei

### 02:21:21 · Speaker 2

divided by Q J given X with respect to Q

### 02:21:27 · Speaker 2

Is that is that alright

### 02:21:35 · Speaker 2

definition

### 02:21:39 · Speaker 2

And what have I done just grouped this together

### 02:21:45 · Speaker 2

and taken this as a function and written that integral as the expectation over z is that okay

### 02:22:00 · Speaker 2

Now there's something called Jensen's inequality

### 02:22:11 · Speaker 2

It says

### 02:22:18 · Speaker 2

Log of expectation

### 02:22:27 · Speaker 2

As always

### 02:22:29 · Speaker 2

less than or equal to expectation of

### 02:22:34 · Speaker 2

Log off

### 02:22:41 · Speaker 2

function

### 02:22:45 · Speaker 2

Does everybody has everybody heard of instance inequality or not

### 02:22:53 · Speaker 4

Yes sir

### 02:22:54 · Speaker 2

If not right, maybe we can take it in the TA session. Okay, just look into it now. So using that, what we can do is, so we have now L theta, which is our log likelihood that we would want to maximize, is equal to log of expectation of this entire thing with respect to Q. Now I can write that as something that is less than or equal to

### 02:23:21 · Speaker 2

greater than or equal to

### 02:23:24 · Speaker 2

This is equal greater than or equal to

### 02:23:28 · Speaker 2

the expectation of

### 02:23:31 · Speaker 2

Log off

### 02:23:35 · Speaker 2

functions

### 02:23:36 · Speaker 4

are less than equal to based on the previous expression

### 02:23:42 · Speaker 2

a log is less than or equal to that expectation of log

### 02:23:47 · Speaker 4

Yes sir

### 02:23:47 · Speaker 2

So uh this is this is log so this is less than that is less than expectation of log correct no log is less than expectation of log should be correct no

### 02:24:05 · Speaker 4

I'll send it

### 02:24:05 · Speaker 2

That should be other way around

### 02:24:07 · Speaker 4

That should be another way around

### 02:24:09 · Speaker 2

Okay so this is

### 02:24:14 · Speaker 2

I think that it's correct now right

### 02:24:23 · Speaker 4

No sir I am I don't remember the inequality sign correctly but

### 02:24:26 · Speaker 2

No, no, no, that's okay. But with this inequality, whatever I have written is correct. No, see, I know for a fact that this is right. So we have to change the Jensen's inequality accordingly. Okay, so. See, Jensen's inequality becomes an upper bound or a lower bound depending upon this function. If this function is concave, then it is one, it is convex, it is something else. So sometimes I get confused about it. This is correct, right? So just tell me that if it's greater than or equal to here, this will become greater than or equal to here, correct?

### 02:25:00 · Speaker 2

So then then change in equality is correct. Okay. Right. So now this is greater than or equal to what what do we have here? It's an integral.

### 02:25:16 · Speaker 2

for C we have Q of C given X

### 02:25:22 · Speaker 2

times log of

### 02:25:26 · Speaker 2

E three TOS

### 02:25:28 · Speaker 2

So can you see do I need to

### 02:25:32 · Speaker 2

You'll see you get an XD set okay

### 02:25:47 · Speaker 2

Of this

### 02:25:50 · Speaker 2

lit

### 02:25:52 · Speaker 2

the entire thing right

### 02:25:55 · Speaker 2

Note that this is a function of two things right it's a function of

### 02:26:00 · Speaker 2

theta obviously it's also a function of q distribution that we have chosen isn't it? Depending upon what q we choose here when we started right with some distribution over z so you will get a different uh lower bound on the likelihood correct?

### 02:26:20 · Speaker 2

Now this implies what did we do so far is that by introducing a latent variable model and a distribution over it we showed that the function which is the log likelihood that we would want to maximize is

### 02:26:34 · Speaker 2

lower bounded by

### 02:26:37 · Speaker 2

some function which is a function of the model parameters and a distribution over latent variable. So now this Q which is a distribution, conditional distribution over Z is referred to as the variational posterior.

### 02:26:54 · Speaker 2

Variational latent posterior that's why the name VAE okay

### 02:27:01 · Speaker 2

What is that? It's a distribution over Z okay and this F theta is also called as the evidence

### 02:27:13 · Speaker 2

A lot of bones

### 02:27:15 · Speaker 2

It's a lower bound, okay, on log likelihood, okay. Log likelihood is also called as

### 02:27:25 · Speaker 2

evidence. I mean it's another name for that no. So you want to in all models you want to maximize the evidence under the model p theta. So now you have constructed a lower bound on the evidence okay based on a variational latent posterior and this is abbreviated as ELBO.

### 02:27:49 · Speaker 2

Is this clear

### 02:27:52 · Speaker 2

Now what we need is we need to remember that we wanted to find a theta that would maximize the evidence or the log likelihood okay now this is equivalently

### 02:28:08 · Speaker 2

maximizing the lower bound on the evidence you know because in latent variable models no maximizing the evidence will become difficult just like we did it with the f divergence right minimizing f divergence directly was not feasible we constructed a lower bound on it similarly on the evidence we are constructing a lower bound okay now this maximization now is not only with respect to theta it is also with respect to q right so as i said you need to find two things one you need to find the q that would construct a

### 02:28:38 · Speaker 2

a lower bound on the log likelihood that you would want to maximize and you also want to find the theta that are model parameters

### 02:28:47 · Speaker 2

Is that all right? So you need to find a theta star and the q star okay that would maximize the lower bound that we have constructed on the

### 02:28:58 · Speaker 2

So what is that lower bound lower bound is the expectation of log of

### 02:29:06 · Speaker 2

ETE

### 02:29:09 · Speaker 2

given by you have to give one x with respect to

### 02:29:15 · Speaker 2

This

### 02:29:21 · Speaker 2

This is a very important result, okay, that is used in all latent variable models. I mean, this is the framework for latent variable models. So basically, you find out the model parameters theta and also the latent variable parameters q, okay, such that the lower bound that you have constructed on the likelihood function is maximized.

### 02:29:45 · Speaker 2

questions on this? See note that there are two optimization problems here right one optimization problem is over theta okay which are the model parameters the other optimization problem is over q which is a functional approximation problem right

### 02:30:01 · Speaker 2

It's not a it's not over parameters it is over class of functions

### 02:30:08 · Speaker 2

Is this alright

### 02:30:11 · Speaker 2

An example for this is

### 02:30:17 · Speaker 2

I'll come to use it. Example for this is what is called a Gaussian mixture model or a GMM.

### 02:30:27 · Speaker 2

I'll not go into the details of GMM, okay? But just tell you what p theta of x is as usual a latent variable model, which is

### 02:30:41 · Speaker 2

where p theta of x and z is given by

### 02:30:58 · Speaker 2

Maybe I can try it uh

### 02:31:02 · Speaker 2

Well then write it this way only

### 02:31:12 · Speaker 2

See, okay, you have alpha Z's, the normal distribution.

### 02:31:22 · Speaker 2

So this is a GLMM right it's a p theta is a linear combination of multiple Gaussian distributions.

### 02:31:31 · Speaker 2

Okay, so there are, okay, let me write it z equal to 1 through m, so it's a discrete model, right? Yeah, so there are m Gaussian distributions and your model is a combination of m Gaussian distributions. Now theta, okay, will be set of m alphas, alpha 1 through alpha m, okay? And for every Gaussian, you have one mean vector, so you have m such mean vectors and you have m sigma vectors.

### 02:32:01 · Speaker 2

that is your parameters that you would want to estimate in a GMM. How is it done? It is exactly done by solving this optimization problem, no, which is theta star and q star. Okay. So the way it is done is

### 02:32:19 · Speaker 2

Alternatively

### 02:32:25 · Speaker 2

Sulfur

### 02:32:29 · Speaker 2

theta star and q star. Here you need to solve an optimization problem with respect to both theta star and q star right. In a GMM you alternatively get q and theta star. Now what can be shown as the optimal q star okay.

### 02:32:48 · Speaker 2

which would maximize the

### 02:32:53 · Speaker 2

The elbow

### 02:32:55 · Speaker 2

Can be shown to be equal to simply the posterior

### 02:33:02 · Speaker 2

distribution that's all

### 02:33:05 · Speaker 2

So now maybe you can take this as a homework or make it in a T session. So the optimal Q distribution, right, that would

### 02:33:17 · Speaker 2

For this right here

### 02:33:19 · Speaker 2

we constructed the lower bound right the optimal q that would maximize this lower bound by the way can somebody tell me this what would be the value of the lower bound with an optimal q

### 02:33:34 · Speaker 2

With the optimal Q, what would be the value of the lower bound width?

### 02:33:43 · Speaker 2

star okay

### 02:33:46 · Speaker 2

f theta of q star will be what? See what is the maximum value of f theta cube

### 02:34:01 · Speaker 2

Am I audible

### 02:34:06 · Speaker 1

Yes

### 02:34:11 · Speaker 2

Didn't you understand my question?

### 02:34:16 · Speaker 2

question is I've created a lower bound on the likelihood function no L theta okay I've denoted that as f theta cube what would be the maximum value of this

### 02:34:28 · Speaker 2

What is the maximum value that this lower bound can achieve

### 02:34:33 · Speaker 1

Love you too

### 02:34:35 · Speaker 2

L theta right

### 02:34:37 · Speaker 2

Because it's a lower bound on L theta the maximum value that it can achieve is L theta isn't it

### 02:34:49 · Speaker 2

Do you see that or not?

### 02:34:52 · Speaker 1

Yes so the maximum lower bound will equal L three times

### 02:34:55 · Speaker 2

Exactly right so the maximum load bound at that point will be simply equal to L theta

### 02:35:03 · Speaker 2

Okay, so what I'm saying is it can be theoretically shown that the optimal Q distribution is equal to P theta of G given X and for that Q theta, okay, with that Q star, the lower bound that we have constructed is equal to the likelihood value.

### 02:35:24 · Speaker 2

Okay, now once you have gotten an optimal lower bound, what you do is which

### 02:35:34 · Speaker 2

That Q star okay

### 02:35:37 · Speaker 2

Find the next

### 02:35:40 · Speaker 2

Next to best

### 02:35:42 · Speaker 2

theta so now let's call this alternatively solve for theta star and q star rate so let's say that we have taken that as theta t okay now q star at t plus 1

### 02:35:58 · Speaker 2

iteration t plus 1 is simply equal to the posterior at theta. So f theta that we have gotten is equal to L theta at that stage. So with that q star at t plus 1, okay, you find the next best theta t plus 1. How do you do that? Theta t plus 1 is simply the arg max of

### 02:36:29 · Speaker 2

that you have computed with q t plus one

### 02:36:34 · Speaker 2

as a function of theta that's all and you keep alternating between these two so you find that theta okay with q being equal to p theta of z given x at the previous time and you use that

### 02:36:51 · Speaker 2

to find your next cue and keep alternating between them

### 02:36:57 · Speaker 2

Is this all right? Did you understand this? The only thing that I have not done is I have not told you that y is the optimal q equal to p theta of z given x, right? So that is something that you can take it as a homework or just show that, okay? But yeah, so it is there in my notes also. I mean, it's given in the first lecture of my handwritten notes. Have a look at it, okay? Let's see. This is like...

### 02:37:28 · Speaker 2

of note

### 02:37:34 · Speaker 2

have a look at it but yeah so now basically what we are doing is we are we are so remember this right what we want to do is we wanted to maximize the likelihood instead of that we constructed a lower bound and that and then we would we we started maximizing the lower bound and that lower bound depends on two things theta and q right and we would alternatively optimize between this theta and q one example is a gmm where you first fix a theta

### 02:38:04 · Speaker 2

and find this q to be this posterior okay and for a gmm how do you find this posterior this can be found out analytically now i'll tell you so p theta of z given x in the case of a gmm is given by p theta of x given z times p z okay divided by p theta z sum of this thing right

### 02:38:33 · Speaker 2

z this is the definition now what is this equal to p theta of x given z for a gmm this actually means

### 02:38:44 · Speaker 2

g is equal to one particular j okay let's say p theta of g equal to j and this is z equal to j to m okay now what is this equal to the numerator for a given j gmm is simply that particular gaussian

### 02:39:05 · Speaker 2

And this is equal to alpha j

### 02:39:10 · Speaker 2

yeah alpha j and this is simply the sum of c equal to

### 02:39:18 · Speaker 2

No sorry j equal to one two m

### 02:39:26 · Speaker 2

g a equal to 1 to m

### 02:39:35 · Speaker 2

We have a Gaussian here

### 02:39:38 · Speaker 2

mu j sigma j times alpha j. This can be found out. Once you find this out, what you do is simply plug that into the lower bound and then maximize that with respect to theta. You get the new theta, use that new theta to evaluate this again and keep alternating between those two steps.

### 02:40:07 · Speaker 2

There's a name for this algorithm do you know

### 02:40:10 · Speaker 2

Does anybody know

### 02:40:12 · Speaker 1

Expectation expectation maximization

### 02:40:12 · Speaker 3

Expectation expectation

### 02:40:14 · Speaker 2

This is the EM algorithm, right? This is the expectation maximization algorithm. This is how you fit a GMM to some data, no?

### 02:40:32 · Speaker 2

EM algorithm. See, I won't go to showing why EM algorithm is correct and all that. Okay, that I will skip. But basically, this is I gave this as an example. I'm running through it quickly because we are interested in looking at VAEs not GMMs. But yeah, so basically the idea is that this will be common across GMMs and VAEs, all latent variable models, right, where construct a lower bound on the likelihood and then find the variational distance

### 02:41:02 · Speaker 2

and the model parameters but through alternative optimizations that would be same across GMM and this thing

### 02:41:11 · Speaker 2

Now uh in a in in fact in fact uh does all of you know about k means algorithm k means clustering

### 02:41:23 · Speaker 2

K means clustering is exactly EM. So what do you do in K means clustering? Given data, you randomly assign K clusters, right, and you assign each of those, each of the data points to a particular cluster, right? That is the step, evaluating this, that is this particular step.

### 02:41:44 · Speaker 2

evaluating your making your posterior equal to p theta of z given x is actually the assignment step okay once you assign you recalculate the means right recalculating the means is this step this uh finding out that theta in fact what can be shown is that k means clustering is a special case of gmm where the where the variance of those component gaussians are infinitesimally small that can be theoretically proved anyway uh that's a different matter but basically uh

### 02:42:14 · Speaker 2

the take home message is that for latent variable models to optimize what you do is that you construct a lower bound on the likelihood function that you would want to maximize okay and then you alternate you estimate both the model parameters and the uh the variational distribution q together okay that is the take home message now for models like gmm right you know that the optimal

### 02:42:44 · Speaker 2

Q is P theta of G given X okay and for GMM that can be computed because there is an analytical form. The question is we have theta star and Q star to be the maximizers.

### 02:43:01 · Speaker 2

We want maximizes with respect to both theta and q and we want to maximize the lower bound that we have constructed, correct? Now q star is known to be p theta of z given x, correct? However, however,

### 02:43:23 · Speaker 2

What if what if

### 02:43:26 · Speaker 2

E theta of z given x cannot be computed

### 02:43:36 · Speaker 2

See if P theta of z gamma x cannot be computed how do you solve the elbow optimization problem is the question

### 02:43:45 · Speaker 2

Does that make sense

### 02:43:48 · Speaker 2

For GMMs, P theta of Z gamma X can be computed. That's why you can do EM. If you cannot compute P theta of Z gamma X, how do you solve elbow optimization is the question that is asked in the VAE paper.

### 02:44:02 · Speaker 2

That is our preface. Now we want so now the goal goal is to

### 02:44:10 · Speaker 2

is to estimate

### 02:44:14 · Speaker 2

the parameters of a latent variable variable model

### 02:44:20 · Speaker 2

Offer

### 02:44:24 · Speaker 2

10 variable model

### 02:44:28 · Speaker 2

For which For which

### 02:44:31 · Speaker 2

the posterior p theta of g given x okay

### 02:44:37 · Speaker 2

And we compute it

### 02:44:42 · Speaker 2

This is our starting point. In fact the state of the art generative models which are diffusion models are also special cases of

### 02:44:52 · Speaker 2

of uh uh v i s okay so it's very important that we understand what v i s are okay so this is the prelude or preface of why uh do we need another model okay when there were latent variable models like gmm it is because while all latent variable models seek to uh maximize the lower bound on the likelihood uh with respect to model parameters and distribution over z uh simpler models

### 02:45:22 · Speaker 2

like GMMs have this advantage that the optimal Q which is the p theta of z given x can be computed analytically but if there are models for which p theta of z given x cannot be computed analytically how do you solve for how do you estimate the model parameters for latent variable models is the question.

### 02:45:46 · Speaker 2

Is this is the story clear so far

### 02:45:49 · Speaker 2

So with this, right, I ask, I mean, I request all of you to read the first and the second chapter of my handwritten notes before coming to the next class. Okay. So with this preface, and if this preface and prelude is strong, we can quickly go to like how VAE solves, I mean, VAE actually solves this problem by approximating the variational posterior using a neural network and all that, which we will see in the next class. So please read my

### 02:46:19 · Speaker 2

entered on notes first lecture and second lecture and come prepared for next class okay

### 02:46:25 · Speaker 2

Stop here and take questions if there are any Vivek

### 02:46:32 · Speaker 1

So initially felt like I understood but there are many things like so why we used Jensen's inequality like why didn't why do we settle for a lower bound actually

### 02:46:45 · Speaker 2

Now because the log likelihood cannot be computed for latent variable models like GMMs, right, what happens is, see, how do we do maximization? So if you start with the log likelihood, let's say, right?

### 02:47:00 · Speaker 2

Let me show that

### 02:47:08 · Speaker 2

So now log of p theta of x in the case of GMM will be log of sigma

### 02:47:19 · Speaker 2

alpha j okay and you have x here and this is mu j and sigma j correct is over j's

### 02:47:26 · Speaker 1

You are guess

### 02:47:27 · Speaker 2

Now this is sum of alpha j into e power x squared minus mu j squared so on right

### 02:47:39 · Speaker 2

See yes there was sum of C on differentiate this with respect to mu and sigma and put it to 0 to maximize this right

### 02:47:39 · Speaker 1

Yes

### 02:47:47 · Speaker 2

Now if there were a sum of log term, then this log and e power exponentiation would cancel each other and you can differentiate. But because you have a log of sum terms,

### 02:48:01 · Speaker 2

because you have a log of sum terms here. If you differentiate this, you will not get mu j's in one side and you will not get a tractable equation in terms of mu. So you cannot maximize this.

### 02:48:15 · Speaker 1

Okay, the summation of uh, I mean the log of the summation of

### 02:48:20 · Speaker 2

Multiple exponentiation a multiple Gaussian distributions if you differentiate that with respect to one mu it will not get separated out

### 02:48:30 · Speaker 1

Yes

### 02:48:32 · Speaker 2

Right, so now you need to do something to ensure that this is maximized. So now to maximize that, one way to do it is construct a lower bound. And if you construct the lower bound, EM becomes easier. It is one of the motivations of why do you need to construct lower bounds on log likelihood.

### 02:48:52 · Speaker 2

The other thing is again similar thing, you know, log of integral of p theta of x and z, right, for z. This is the model. Now, if you do not know how to integrate this with respect to z because you don't know this distribution, how do you differentiate this with respect to theta? You can't do that. You need another method to optimize for the log likelihood, no? That's why you construct a lower bound and then you optimize for it. See, just you remember why we constructed lower bound on it divergences, right?

### 02:49:22 · Speaker 2

Because we could not compute the F divergence step because it involved integrals. What we did was we expressed that in terms of expectations that we could compute and then simply used sample estimates to optimize for it, right?

### 02:49:35 · Speaker 1

Yes exactly same

### 02:49:36 · Speaker 2

Exactly same thing here, exactly same thing. And you remember that maximizing this is again minimizing the KL divergence. Ultimately, we are minimizing the KL divergence. And to minimize this, this involves integrals with respect to px and p theta, which we cannot compute. And that's why we are computing lower bounds and expressing it in terms of expectations that can be estimated using the sample averages.

### 02:50:00 · Speaker 2

That's the fundamental idea okay

### 02:50:06 · Speaker 2

Uh have a look

### 02:50:08 · Speaker 1

Yeah, sir. My question is related to the midterm exam. So the syllabus for it is till the next class or today's class or any any specification regarding

### 02:50:21 · Speaker 2

Till the next class yeah there will be one more class before the exam it will be till that

### 02:50:28 · Speaker 1

Okay and uh I mean just to get some idea on the question so shall we be expecting coding questions or mostly no there will not

### 02:50:35 · Speaker 2

No, no there will not be any coding questions it will all be theoretical. So just follow whatever has been said in the class and also the TA session works.

### 02:51:00 · Speaker 1

So yes sir I got I got my answers

### 02:51:00 · Speaker 4

So yes sir

### 02:51:03 · Speaker 4

Yes, I'm going to share. So I have a quick question sir, we read about this model now we understood also exactly how it works internally. So, uh,

### 02:51:12 · Speaker 1

For practical uses like where all we can use like image generations or data

### 02:51:17 · Speaker 2

Hold on, I really you've just started VAEs, right? There's two full lectures that will be that will be kept for this where I can talk about all kinds of applications, how it is used for generative models, everything will be covered.

### 02:51:35 · Speaker 1

Okay sir okay that is planned okay I was just asking that thanks

### 02:51:38 · Speaker 2

Of course right I mean just like we did for Gans we are just starting it there's a lot that we need to do

### 02:51:44 · Speaker 4

Sure sure

### 02:51:46 · Speaker 2

Completely preface okay anything else

### 02:52:05 · Speaker 2

Yeah, uh, go on if you were told.

### 02:52:10 · Speaker 1

So in the

### 02:52:12 · Speaker 4

I'm just curious to ask like since you said there is no report to be submitted what all things we have tried we can simply add it in the markdown right because in order to get any valid result too many things are being tried out from my end so just want to know

### 02:52:27 · Speaker 2

Come again what is the question

### 02:52:30 · Speaker 4

like uh so far I was trying assignment questions so it's not coming directly in the first step itself like a lot of things are being tried out here and there so we can't just put everything in the notebook

### 02:52:43 · Speaker 2

No no you can you can yeah mark those statements and every experiment that you you know try you know just comment it out and put your observations that will be appreciated

### 02:52:53 · Speaker 3

The problem is sir if you are looking for the outputs of those experiments right

### 02:52:57 · Speaker 2

No no no I don't I don't whatever experiments that you uh that you uh tried no just uh document them okay

### 02:53:05 · Speaker 3

Thank you

### 02:53:08 · Speaker 4

For assignment like you said we should use Google Colab for compute but uh there's no free GPU available so I'm using my company's GPU and I'll put that

### 02:53:18 · Speaker 2

And that's okay, that's okay, it doesn't matter

### 02:53:28 · Speaker 2

collab if only if uh like you know people don't happen go on you can speak you don't have to raise your hands classes are done yeah

### 02:53:36 · Speaker 1

Yeah, also one question regarding the background reading material. So is it okay to read that the Machine Learning Advanced Topics by Murphy?

### 02:53:47 · Speaker 2

Murphy nope it's one of the best books yeah it's it's not an it's actually a very good book yeah you can use Murphy

### 02:53:47 · Speaker 1

Is it putting

### 02:53:54 · Speaker 1

Okay only the portions related to generative

### 02:53:58 · Speaker 2

Whatever we have see

### 02:54:00 · Speaker 1

Yeah it's a video I've never seen a video like that

### 02:54:01 · Speaker 2

Whatever I've taught in class is what your syllabus is nothing less nothing more

### 02:54:11 · Speaker 2

Anything that is related to things that I have taught in class is all that I am going to ask. I don't assume you to know anything that is beyond whatever I have taught in class and also in TA sessions.

### 02:54:36 · Speaker 2

That's all? Okay, uh, if that's all it is, let's uh meet next week, okay?

### 02:54:46 · Speaker 1

Thank you

### 02:54:46 · Speaker 2

Thank you
