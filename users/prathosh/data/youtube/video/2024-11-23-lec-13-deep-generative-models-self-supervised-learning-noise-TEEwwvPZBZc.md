---
id: TEEwwvPZBZc
title: Lec 13 - Deep Generative Models Self supervised learning Noise contrastive
  estimation
date: '2024-11-23'
url: https://www.youtube.com/watch?v=TEEwwvPZBZc
description: ''
author: prathoshap5226
duration: 02:37:56
model: saaras:v3
transcript: true
---

# Lec 13 - Deep Generative Models Self supervised learning Noise contrastive estimation

## Transcript

### 00:00:02 · Speaker 6

Email is not opening or academic calendar. TCC exam end.

### 00:00:11 · Speaker 6

course grade entry

### 00:00:14 · Speaker 6

thirtieth level into eighteen twelve oh I see

### 00:00:23 · Speaker 6

which means that we can do the assignment vivas after your exam. Will that be okay for you?

### 00:00:33 · Speaker 6

First week of December

### 00:00:35 · Speaker 4

Yes sir

### 00:00:35 · Speaker 3

Yes

### 00:00:38 · Speaker 6

Okay, let us do it then. What we can do is after the final exam is done on thirtieth, the first week of December we will do because twelfth is when I need to submit the grade. Sorry, eighteenth is the last date for me to submit the grades. So I'll have enough time to consolidate and

### 00:00:55 · Speaker 6

discuss and all that. Oh no no no this is twenty twenty three. I'm sorry I'm sorry. I need to look at twenty twenty four calendar.

### 00:01:12 · Speaker 3

Just a second. Sorry, sorry, this is

### 00:01:15 · Speaker 6

mistake

### 00:01:16 · Speaker 6

academic calendar

### 00:01:20 · Speaker 2

I think it is 12th sir

### 00:01:23 · Speaker 6

12th of December, how do you know?

### 00:01:25 · Speaker 2

Yes. I think in reinforcement learning Salab Bhatnagar sir told that twelfth is the final date to put grades. We have a project pending there in reinforcement learning also.

### 00:01:40 · Speaker 6

Okay, okay. So there's this link, it's not opening.

### 00:01:45 · Speaker 6

Yeah, yeah, I'm just opening, hold on. Yeah, um

### 00:01:52 · Speaker 6

course grade entry thirteen twelve twenty twenty four is the last date. Yes. Yeah okay thirteenth is the last date even then I think

### 00:02:02 · Speaker 6

It's enough for me if I have one week. So yeah, let us do it on the week of second December. Second to sixth December is there, no? We will do it. We'll do the viva then. Okay, I think that is okay.

### 00:02:15 · Speaker 6

Okay Chandan that's it yeah I think I'll continue with the class.

### 00:02:19 · Speaker 1

So what is the format of the viva exam going to be? I mean how much time is that going to take and what will be the schedule?

### 00:02:19 · Speaker 7

Sweet

### 00:02:28 · Speaker 6

we will let you know all of that. uh See I'm thinking of like about twenty minutes per group or rather half an hour per group.

### 00:02:39 · Speaker 6

and we have twenty groups, no? We are like three of us, four of us, three TAs and myself will make five groups per instructor and we will spend half an hour with each of the groups and then we will evaluate. That is the scheme that I'm thinking. Schedule I will let you know, okay? Maybe late evenings or weekends something we will make, huh? So that it is beneficial for all.

### 00:03:07 · Speaker 6

That that we can adjust, no problem. Yeah, whatever works for us.

### 00:03:07 · Speaker 1

that that we can

### 00:03:09 · Speaker 1

I just wanted to request for some flexibility as I will be traveling due to some official work. So I'll be in a different time zone at that time.

### 00:03:17 · Speaker 6

Right

### 00:03:19 · Speaker 6

Ha ha. No no okay. See see those requests we can always accommodate no problem. Yeah.

### 00:03:24 · Speaker 1

Thank you

### 00:03:27 · Speaker 6

ओके. सो शैल वी गेट बैक टू द बिजनेस? शैल वी स्टार्ट? सर, वन क्वेश्चन आई हैड.

### 00:03:31 · Speaker 7

सर वन क्वेश्चन आई हैड

### 00:03:33 · Speaker 6

Hello

### 00:03:34 · Speaker 7

दिस इस समथिंग रिलेटेड टू द क्विज फाइव वी जस्ट डिड। सो इफ यू अलाउ, आई वांटेड टू आस्क अ क्वेश्चन।

### 00:03:40 · Speaker 6

Tell me what is it quickly.

### 00:03:42 · Speaker 7

सो सर, देयर वाज़ अ क्वेश्चन, इट सेज़ इन डीडीपीएम द वेरियंस शेड्यूल अल्फा टी फॉर ईच टाइप स्टेप इज़ केयरफुली डिजाइन्ड टू सैटिस्फाई विच ऑफ द फॉलोइंग क्राइटेरिया? द आंसर मार्क्ड इज़ इट शुड इंक्रीज़ ग्रेजुअली टू प्रिवेंट कंप्लीट इंफॉर्मेशन लॉस इन अर्ली स्टेप्स।

### 00:03:47 · Speaker 6

each night

### 00:03:48 · Speaker 6

carefully

### 00:03:52 · Speaker 6

Hmm

### 00:03:58 · Speaker 6

Hmm

### 00:03:58 · Speaker 7

But as per my understanding like alpha T is the product of from alpha one till that till that particular time.

### 00:04:06 · Speaker 6

No no no. See that we called as alpha bar.

### 00:04:12 · Speaker 6

This is the variant schedule alpha

### 00:04:12 · Speaker 7

Okay

### 00:04:16 · Speaker 5

But even alpha should reduce, right? Because we want the variance to increase as we go forward in the steps.

### 00:04:23 · Speaker 6

variants should reduce, no?

### 00:04:23 · Speaker 5

should reduce no? variance is one minus alpha t right?

### 00:04:29 · Speaker 6

alpha is what we called as the variance, isn't it? in our in our treatment.

### 00:04:40 · Speaker 5

I supposed it was one minus alpha

### 00:04:42 · Speaker 7

So like alpha, we we we are drawing it from a zero from the samples from zero comma one space, right?

### 00:04:43 · Speaker 6

and

### 00:04:50 · Speaker 6

they are simply linearly varying. Let me just check it once. Hold on.

### 00:04:56 · Speaker 4

Hmm

### 00:04:56 · Speaker 6

Hmm

### 00:05:16 · Speaker 4

These are small. Alphas are

### 00:05:39 · Speaker 6

So beta one minus alpha would increase. So which means alpha should decrease gradually, right? What was the option that was there?

### 00:05:48 · Speaker 4

Selected Option Was Alpha

### 00:05:48 · Speaker 5

selected option was alpha alpha increases

### 00:05:51 · Speaker 6

Hmm

### 00:05:53 · Speaker 5

the correct option was marked as alpha should increase.

### 00:05:57 · Speaker 6

No, one minus alpha should increase.

### 00:06:02 · Speaker 5

Yeah, I mean. So the last option said that Dalton will gradually decrease.

### 00:06:04 · Speaker 6

the dark number should gradually decrease. Yeah, that should be the correct one. Because the yeah, because the variance is one minus alpha, right? The variance term in X T, that is one minus alpha. The variance should gradually increase.

### 00:06:25 · Speaker 6

That's correct

### 00:06:25 · Speaker 7

सर वेरियंस शुड इनक्रीस इवेंचुअली बिकॉज़ वी वांट द फाइनल एक्स ऑफ टी ऑफ नॉर्मल डिस्ट्रीब्यूशन, करेक्ट?

### 00:06:31 · Speaker 6

Yeah, yeah, the thing is, only when the variance slowly increases, you can guarantee that the Markov chain converges to a normal zero one. So variance should gradually increase.

### 00:06:45 · Speaker 6

Chandan, are you there?

### 00:06:49 · Speaker 7

Yes sir, I am there. Yes sir.

### 00:06:51 · Speaker 3

the question said variant schedule alpha T

### 00:06:56 · Speaker 6

variant schedule I mean of course variant schedule is one minus alpha but yeah you can the parameter is alpha so variant schedule alpha see if you are looking at alpha as the variant schedule then the alpha should gradually decrease.

### 00:07:11 · Speaker 7

Yes sir, I will make the necessary change. Yes sir.

### 00:07:15 · Speaker 7

So, yeah, beta should increase basically, yeah.

### 00:07:19 · Speaker 6

just a thing sir, in the option it says it should decrease exponentially the one that

### 00:07:26 · Speaker 2

is being debated right now. So is is it supposed to really decrease exponentially or was that

### 00:07:33 · Speaker 6

Isn't there an option that would say it would linearly decrease?

### 00:07:39 · Speaker 7

No sir

### 00:07:40 · Speaker 1

No sir. Sir, I I have I really have no access to the quiz. I really don't know what is the question also.

### 00:07:41 · Speaker 7

Right

### 00:07:42 · Speaker 6

Oh

### 00:07:42 · Speaker 7

Hello

### 00:07:47 · Speaker 7

Chandan, I have, Chandan, I have pasted the screenshot in the chat if you could have a moment.

### 00:07:52 · Speaker 1

but have

### 00:07:52 · Speaker 6

That's okay if if if there is no linear decrease option

### 00:07:52 · Speaker 1

If, if

### 00:07:56 · Speaker 7

decrease option we will give it to

### 00:08:00 · Speaker 6

Yeah. Yeah. It should be, see yesterday what happened as I looked it looked at the quiz and there was beta there. I told them that beta is not something that I've used. So change it to alpha. So I think they just changed beta to alpha. Without changing the options.

### 00:08:01 · Speaker 7

Yeah

### 00:08:17 · Speaker 6

guys I don't know what can I say? See I told you I told you to change beta to alpha in a meaningful way yaar just not replace alpha beta by alpha. Right if alpha is one minus beta then the options have to like

### 00:08:22 · Speaker 1

I

### 00:08:34 · Speaker 5

options has to be flipped

### 00:08:36 · Speaker 6

Anyway, so you know that question, you know, add plus one there. Okay. Sure, sure. Yes, sir. Thanks for plugging it out. Yeah.

### 00:08:38 · Speaker 5

So you know that

### 00:08:40 · Speaker 5

ओके श्योर श्योर येस सर

### 00:08:43 · Speaker 7

Sorry

### 00:08:45 · Speaker 3

Yeah, yeah.

### 00:08:45 · Speaker 7

सर, वन मोर क्वेश्चन। सो, वी वी सेड दैट वी आर चूजिंग अल्फा, अल्फा, अल्फा इज फ्रॉम ज़ीरो टू वन, बट ऑन व्हाट बेसिस आर वी सिलेक्टिंग? लाइक व्हाट इज द प्रीडिफाइंड लॉजिक फॉर दैट?

### 00:08:56 · Speaker 6

I told you in the class already in the previous class it is designed in such a way that the forward Markov chain that we that we construct has to be

### 00:09:06 · Speaker 6

designed in such a way that the stationary distribution converges to normal zero one. Okay? So that is why the variance has to slowly decrease.

### 00:09:17 · Speaker 6

And also if you look at it it's all

### 00:09:20 · Speaker 7

variants has to slowly increase

### 00:09:23 · Speaker 6

what do you what do you call by variance? one minus alpha. if you call one minus alpha as variance then it will increase. yeah of course.

### 00:09:34 · Speaker 6

depends on what you call by variance. So it is if it's alpha then the alpha should gradually decrease which means that one minus alpha should increase, okay?

### 00:09:43 · Speaker 6

That is what you have to implement in your assignment also, right? And talking of assignment, I have made assignment three of right last week itself I did it, huh?

### 00:09:56 · Speaker 6

So, hope you have started working on it. When is the deadline for assignment three?

### 00:10:04 · Speaker 7

18th sir

### 00:10:07 · Speaker 6

Okay, then you should have started it already.

### 00:10:11 · Speaker 6

Okay

### 00:10:12 · Speaker 6

Anything else? Shall we get started with the class?

### 00:10:20 · Speaker 7

can I

### 00:10:22 · Speaker 3

Take leave sir

### 00:10:24 · Speaker 4

Okay

### 00:10:25 · Speaker 3

ಥ್ಯಾಂಕ್ ಯು ಸರ್

### 00:11:46 · Speaker 4

It says working offline to me, do you see my screen?

### 00:11:52 · Speaker 3

Yes sir

### 00:11:56 · Speaker 6

I don't know why it says you're working offline. Okay, anyway. Okay, let's start. See, today's agenda is that we'll be discussing some self-supervised learning techniques.

### 00:12:12 · Speaker 6

So which are special cases of these broad learning methodologies called representation learning, okay? So what is representation learning? I'd given some introduction in the previous class. So given some data that is drawn ID from a distribution, what you want to learn is a function f theta from the data space to some latent space Z, okay? Where the dimensionality of Z is much less than the dimensionality of X.

### 00:12:43 · Speaker 6

Now we seek some special properties on Z. So the properties that we seek is in such a are that the representations are when

### 00:12:55 · Speaker 6

by representation I mean Z, okay? the projection that you learn on data. and we need that to have some desirable properties such as

### 00:13:07 · Speaker 6

if you use Z instead of X, then the amount of supervision that you need is much lesser and the Z becomes much robust than X and all that, okay?

### 00:13:21 · Speaker 6

Now, uh learning representations can be done in two ways, right? One is the generative way, uh where you learn a latent variable model and use the latent space as representations. We have seen this all throughout the course, right?

### 00:13:36 · Speaker 6

and I've asked you to do this in your assignments as well. where any latent variable model that you learn, uh implicitly have this capability of learning representations because when you do posterior inference which is get samples from P of Z given X, then you are automatically doing

### 00:14:00 · Speaker 6

representation learning because Z the latent variables that you get from a latent variable generating model can be seen as representations. Okay that is one way to do it. The other way to do it is what we will see which is a non-generative way also called self-supervised learning or contrastive learning way where the fundamental idea is that you define a free text task.

### 00:14:25 · Speaker 6

Okay, what is the pre-text task? You solve

### 00:14:30 · Speaker 6

some other task using data. Note that in all the representation learning literature, you don't have labels. Okay, this is label free learning. Okay. So now if you when you don't have the the labels, you define some pseudo tasks, okay, where you define some pseudo labels and you ask a neural network to solve some pseudo task. Okay. And the the intermediate representations of these pseudo task solver is what you take as representations for data. Examples for pseudo tasks are

### 00:15:08 · Speaker 6

If you are looking at like learning representations for images, then you take an image, rotate it with some angle, by some angle, and ask a neural network to predict the angle of rotations, you know, that can be one pseudo task. The other pseudo task can be that you have an image, you add some noise to it, okay? And try to

### 00:15:31 · Speaker 6

classify between the noise and the data and you take the intermediate representations of that classifier as your uh representation and so on. Okay? The other thing can be that you know you take data and you mask it and try to reconstruct the data back. That that is another way to define it. So these class of methods are called self supervised learning techniques. Now we will go deeper into it and and see why should these methods even help in in learning good representation.

### 00:16:01 · Speaker 6

and also some famous examples of how to do it. Okay. In fact, the language models, right, like BERT etcetera also uses the same kind of technique, okay, to learn representations on data.

### 00:16:17 · Speaker 6

Any questions on this so far?

### 00:16:38 · Speaker 3

Hello

### 00:16:41 · Speaker 3

Hello, I am Aadigul

### 00:16:45 · Speaker 4

Yes sir

### 00:16:46 · Speaker 3

Any questions?

### 00:16:51 · Speaker 7

maybe we'll cover it later. Just a query here. The pretest tasks are defined, I mean like, based on how it should perform in the end, right? I mean...

### 00:17:01 · Speaker 6

Well, not necessarily, uh not necessarily, see, uh I will tell you what the the fundamental idea behind this thing and in fact, how to define a pretext task is a question that people have been asking, uh right? And different uh ways have been looked at, okay?

### 00:17:25 · Speaker 6

we'll talk about it. We'll talk about it. Yeah.

### 00:17:28 · Speaker 7

Sure. Thank you.

### 00:17:30 · Speaker 6

Um

### 00:17:32 · Speaker 6

ஓகே

### 00:17:33 · Speaker 0

Hello sir

### 00:17:34 · Speaker 6

Yes

### 00:17:35 · Speaker 0

have a query like is there any methodology like if we define this pretext then the embedding we'll get we'll have you know some kind of structures which will be helpful for other features. Like what I mean is if suppose I use the pretext as in painting then it will be helpful in classification or segmentation. But if I use some other pretext then it won't be much helpful for classification or any other segmentation task.

### 00:17:54 · Speaker 2

then

### 00:18:05 · Speaker 0

Are there any such kind of thing?

### 00:18:08 · Speaker 6

not theoretically but there are some empirical ideas on what sort of pretext task would help. We will discuss all that. Just let's let's let's see. Give some time. Okay. Not there here.

### 00:18:29 · Speaker 4

did I do and see

### 00:18:40 · Speaker 4

Just a minute, I'm just looking for my

### 00:19:31 · Speaker 4

Hmm

### 00:19:35 · Speaker 3

Okay

### 00:19:51 · Speaker 4

Just want to see if I did it the last year and if there is

### 00:20:28 · Speaker 4

Okay, I've done it. Just a second.

### 00:20:35 · Speaker 4

two minutes I have to

### 00:21:45 · Speaker 6

Okay. The fundamental idea for all

### 00:21:51 · Speaker 6

self-supervised learning techniques come from this very nice paper, very nice methodology that came up which was called noise contrastive estimation.

### 00:22:16 · Speaker 6

mass contrast estimation also deviated as N C E. Okay. So the the basis for self supervised learning lies here. The question that is asked is the following. Okay. Suppose...

### 00:22:36 · Speaker 3

Okay

### 00:22:36 · Speaker 4

Peter

### 00:22:42 · Speaker 4

drawn from a

### 00:22:45 · Speaker 4

from an unknown distribution V X.

### 00:22:57 · Speaker 4

Okay, so what we have is we have D

### 00:23:01 · Speaker 6

that is given by x one

### 00:23:04 · Speaker 6

up to x n, okay. These are drawn I I D from P X.

### 00:23:11 · Speaker 6

the objective

### 00:23:18 · Speaker 4

is to estimate

### 00:23:23 · Speaker 4

estimate the underlying distribution

### 00:23:32 · Speaker 3

underline distribution P X.

### 00:23:40 · Speaker 6

given D, right? This has been a question that we have been asking. So now how do we estimate the underlying distribution, uh given a particular uh given samples from distribution, right? This is a question that we have been asking. How did we do that? I mean, so far, we have looked at the maximum likelihood estimate.

### 00:24:09 · Speaker 3

or

### 00:24:11 · Speaker 3

the minimum KL estimate, right? So both of them are equivalent.

### 00:24:19 · Speaker 3

How did we do that?

### 00:24:21 · Speaker 3

Start with

### 00:24:24 · Speaker 3

parameter

### 00:24:25 · Speaker 4

Form for PX

### 00:24:31 · Speaker 4

Colpete

### 00:24:35 · Speaker 4

Get theta

### 00:24:39 · Speaker 6

that would simply minimize some divergence metric which we call the F divergence between V X and P theta. This is what we have been doing the entire course, right? All the uh generative modeling frameworks that we saw were actually

### 00:24:56 · Speaker 6

fitting into this framework, right? where uh we uh minimized uh a divergence metric between started with an assumption on the the parametric assumption on the underlying density, called it P theta, right?

### 00:25:14 · Speaker 6

and minimized divergence metric if F divergence metric between these two. So now how do we define P theta is where we change different models. Now in Gyan this P theta is taken to be the samples that are coming from transformed

### 00:25:32 · Speaker 6

Gaussian random variable transformation is through an neural network. In a V A E, we use a latent variable model for this and we find a lower bound on this and then optimize this and so on, right? We know the entire story. This is how we do it in a

### 00:25:51 · Speaker 6

generative framework, right? So where we assume a parametric from P theta and find the parameters by minimizing F divergence. So now N C E provides an alternative

### 00:26:01 · Speaker 4

bus

### 00:26:12 · Speaker 4

alternative for ML estimation.

### 00:26:19 · Speaker 6

Now, uh self-supervised learning, so did it get uploaded? Hold on a high. Oh my god.

### 00:26:28 · Speaker 6

I just wanted this to get uploaded to my drive so that I can access simply the

### 00:26:50 · Speaker 6

Okay, so in noise contract in in self supervised learning, see you what do we need? We need a representation for data, right? So when do you think data would be represented optimally? The data would be represented optimally only if you learn the underlying distribution correctly, isn't it?

### 00:27:11 · Speaker 6

See what we need is that we need to learn the underlying distribution correctly because if we do not learn the distribution then we are not representing the data. See that is why the generative modeling framework right will give in will implicitly give you representations because by by definition when we have a latent variable model the latent variables actually aid minimizing the KL divergence between or rather F divergence between the the true distribution and the model distribution. Right?

### 00:27:41 · Speaker 6

Therefore the representations that we get by solving a KL minimization problem under a related variable model implicitly gives us a representation. Now we are explicitly trying to find the representation. This is not getting uploaded.

### 00:27:58 · Speaker 6

Do you know some other way to do this?

### 00:28:02 · Speaker 3

Sorry about this.

### 00:28:11 · Speaker 3

has anybody used this AirDrop thing between

### 00:28:14 · Speaker 4

two MACD devices. Do you know how that works?

### 00:28:29 · Speaker 6

Hello, am I audible?

### 00:28:31 · Speaker 5

So you can also share it between two teams instances if you have it on both the instances.

### 00:28:38 · Speaker 5

share it to yourself.

### 00:28:40 · Speaker 7

you can just right click on the file and share and then you will see AirDrop there.

### 00:28:52 · Speaker 6

Oh this is very good okay it just came from my math. Nice.

### 00:29:01 · Speaker 6

Apple devices are what they are for a reason, no? Extremely good. Okay, I just got what I wanted. Thanks.

### 00:29:23 · Speaker 6

Okay. So you see my screen now?

### 00:29:27 · Speaker 6

Do you see my screen?

### 00:29:34 · Speaker 3

So there's a file transfer pop up.

### 00:29:37 · Speaker 6

No no no I am writing on my usual stones

### 00:29:39 · Speaker 3

You should stop also. No.

### 00:29:43 · Speaker 6

Oh my god, something happened.

### 00:29:59 · Speaker 4

Let me know when you can see my screen.

### 00:30:23 · Speaker 6

Can you see my screen?

### 00:30:27 · Speaker 3

No sir

### 00:30:28 · Speaker 5

Not yet, sir.

### 00:30:31 · Speaker 4

Why is it not coming?

### 00:30:45 · Speaker 4

Yes, it is visible now.

### 00:30:54 · Speaker 3

I'm writing, do you see that? No.

### 00:31:02 · Speaker 3

No, no, it is circuit NC provides an alternative for ML estimation, I think.

### 00:31:08 · Speaker 4

Structure

### 00:32:35 · Speaker 3

Can you please let me know if it's going?

### 00:32:41 · Speaker 4

Yes sir, we can say suppose that you are out.

### 00:32:47 · Speaker 6

Okay, so hopefully it will not misbehave. Okay. Now we have okay, noise contrast estimation provides an alternative for ML estimation, right? Where the goal is to estimate the underlying distribution, okay? Now how does NCE does this? Now we have data

### 00:33:09 · Speaker 6

we have data that is x one, x two

### 00:33:15 · Speaker 6

Up to

### 00:33:17 · Speaker 6

it's called it x n

### 00:33:22 · Speaker 6

that is drawn from P X. This is what we need to estimate. Okay?

### 00:33:34 · Speaker 3

and we define

### 00:33:39 · Speaker 3

Noise

### 00:33:40 · Speaker 4

define noise distribution

### 00:33:51 · Speaker 4

noise distribution P

### 00:33:54 · Speaker 4

N

### 00:33:56 · Speaker 4

and draw samples from it.

### 00:34:00 · Speaker 3

Okay

### 00:34:01 · Speaker 6

Eat

### 00:34:07 · Speaker 4

call this as B N

### 00:34:10 · Speaker 6

this

### 00:34:14 · Speaker 6

maybe we will change the notation too many Ns that I'm using. T number of samples. You have N one, N two.

### 00:34:27 · Speaker 6

to N P

### 00:34:30 · Speaker 6

Okay, these are drawn from P N, I I D from P N.

### 00:34:36 · Speaker 6

So you know what we you understand what we are doing. We have uh the data distribution that we have been given. Okay we define a noise distribution P N and draw samples from it which which are denoted by N one to N two.

### 00:34:49 · Speaker 3

Okay. Now define an estimator

### 00:35:00 · Speaker 3

Define an estimator J T

### 00:35:04 · Speaker 6

parameterized by theta as follows

### 00:35:11 · Speaker 6

How do you define J theta? J T theta T because it depends on T number of samples. It's given by one over two T.

### 00:35:22 · Speaker 6

sigma forty log of

### 00:35:27 · Speaker 6

H theta of

### 00:35:30 · Speaker 6

xt plus log of

### 00:35:35 · Speaker 6

one minus h theta of n t

### 00:35:45 · Speaker 3

where

### 00:35:50 · Speaker 3

H theta

### 00:35:53 · Speaker 3

of its theta, you can take both exterior and these

### 00:35:56 · Speaker 3

H theta is a function

### 00:35:59 · Speaker 6

parameterized

### 00:36:06 · Speaker 6

Yeah

### 00:36:06 · Speaker 4

Neural Network

### 00:36:21 · Speaker 4

So

### 00:36:28 · Speaker 3

H theta is a function that takes data from D dimensional space and maps it to zero one.

### 00:36:50 · Speaker 3

the summation is

### 00:36:51 · Speaker 3

common right? for both. assumption is common for both.

### 00:36:52 · Speaker 4

mission is common.

### 00:36:54 · Speaker 4

of the yes

### 00:37:01 · Speaker 3

ओके. सो दिस जे टी थीटा ओके इस कॉल्ड द नॉइस कॉन्ट्रास्टीव एस्टीमेटर.

### 00:37:19 · Speaker 4

This is the noise contrast estimator. Okay?

### 00:37:36 · Speaker 4

Okay

### 00:37:37 · Speaker 6

Now

### 00:37:39 · Speaker 6

there are multi okay so now there are multiple claims that we should make okay now the first claim that we do and show is the following claim one is that

### 00:37:52 · Speaker 6

जे टी ऑफ थीटा

### 00:37:57 · Speaker 6

should we do it the other way?

### 00:37:58 · Speaker 4

just a second, let me just think how to best present this.

### 00:38:35 · Speaker 4

Okay, so maybe I'll tell you this and then

### 00:38:36 · Speaker 6

Okay, claim one is J theta of theta, okay, J T of theta, the noise contrasting objective. Before we move on, let me just tell you this. See, this J theta

### 00:38:49 · Speaker 6

can be computed, right? Suppose you have H theta as a neural network, J theta can be computed and you can actually back propagate through that neural network to find theta. So basically what we will do is

### 00:39:01 · Speaker 6

represent J theta using neural network, okay? And find your theta star as the minimizer.

### 00:39:13 · Speaker 6

Off

### 00:39:15 · Speaker 6

objective function over theta. Okay?

### 00:39:19 · Speaker 6

We can do this, we can solve this optimization problem. So this theta star we get is the uh N C E estimate for data. Now the question that we should ask now is why should this theta star or rather why solving this object optimization problem lead us to, okay so let me write it down. So question

### 00:39:46 · Speaker 3

Y is

### 00:39:48 · Speaker 3

J theta

### 00:39:50 · Speaker 3

good estimator.

### 00:39:57 · Speaker 3

Estimator

### 00:40:01 · Speaker 6

for P X. Okay. So now you remember that what we actually need is an estimate for P X, isn't it? What we are trying to do is learn the underlying distribution P X. That is our goal. Now, I somehow defined some objective function, right? That that that we would like to solve. The question is why would solving this objective function lead to a good estimate for P X?

### 00:40:26 · Speaker 6

Are we good so far? Let me repeat what we did.

### 00:40:30 · Speaker 6

So we are given some data. Okay? uh yeah. We are we are given some data and we define another distribution called the noise distribution from which we know how to draw samples. We draw some we draw equal also you should observe that the dimensionality of of X, okay? Is the same as the dimensionality of N. So noise and the data both have the same dimensions here. So we draw

### 00:41:00 · Speaker 6

n noise samples, okay? And we define an estimator or an objective function that would involve the data samples XT and the noise samples NT, okay? And there is another function H theta and H theta is is

### 00:41:18 · Speaker 6

approximated using the neural network and once we use this objective function so now what is happening actually is that there is a neural network okay and this neural network will either take x or n as input

### 00:41:33 · Speaker 6

and give you one or

### 00:41:34 · Speaker 4

Hero as the output, correct?

### 00:41:45 · Speaker 6

I'll give one or zero as input, right? I mean this is our h theta function. Correct? Now the and what is the objective? Objective that we are using is j theta here.

### 00:41:57 · Speaker 6

Now the question is why should solving the claim that we are making here is that if we do this then we would implicitly learn P X.

### 00:42:11 · Speaker 6

Is the story clear so far?

### 00:42:13 · Speaker 6

Now, we should see why doing solving this sort of an objective using this technique should give us should implicitly estimate P X. That is what we are going to answer now. But is the is the

### 00:42:27 · Speaker 3

story clear so far what we are trying to do

### 00:42:36 · Speaker 4

Yes, only D N, we're not sure how it is.

### 00:42:40 · Speaker 3

only what

### 00:42:41 · Speaker 4

D

### 00:42:41 · Speaker 7

D N D N

### 00:42:44 · Speaker 6

it is it is yeah it is some distribution. yeah it is totally random. it is some distribution that is not px. so we will write that. so now

### 00:42:44 · Speaker 7

it is yeah

### 00:42:45 · Speaker 7

It is some distribution

### 00:42:52 · Speaker 7

Hello

### 00:42:54 · Speaker 6

Also P N is just a distribution that is not the same as P X

### 00:43:02 · Speaker 6

Okay? Sir, if the noise is

### 00:43:03 · Speaker 7

Sir, if the noise is input, then h theta will return a zero.

### 00:43:05 · Speaker 6

Yeah

### 00:43:08 · Speaker 6

Let's see, let's let's see, let's see what it returns. Okay. But yeah, it's for now it's simply a function from the data or noise space to

### 00:43:18 · Speaker 3

Rohan

### 00:43:21 · Speaker 4

Okay.

### 00:43:34 · Speaker 6

Alright, is that okay?

### 00:43:37 · Speaker 6

Okay, so let us see some properties of this estimator now. What is this estimator actually is doing and why should it get the, why should it estimate the underlying distribution, okay? Now let's look at the

### 00:43:53 · Speaker 6

properties of the

### 00:43:57 · Speaker 6

N C S T matter. So this is called the N C S T matter, okay?

### 00:44:07 · Speaker 6

the first one which is

### 00:44:11 · Speaker 6

which we'll see which is

### 00:44:14 · Speaker 6

What it is that

### 00:44:18 · Speaker 4

जे थीटा

### 00:44:27 · Speaker 4

is equivalent to

### 00:44:36 · Speaker 4

Solving a

### 00:44:40 · Speaker 4

binary classification problem

### 00:44:52 · Speaker 3

British

### 00:44:52 · Speaker 6

May

### 00:44:54 · Speaker 6

the samples of

### 00:45:01 · Speaker 6

P X and P N. This is the first probability. What we are saying is that this uh complicated looking or rather this uh estimator that we have is nothing but solving a binary classification problem between the samples of P X and P N. Okay? So let us look at why this is the case.

### 00:45:22 · Speaker 3

Now

### 00:45:29 · Speaker 4

Creator

### 00:45:31 · Speaker 4

supervised data set

### 00:45:38 · Speaker 4

supervised data set. Combining

### 00:45:45 · Speaker 3

combining D and D N okay

### 00:45:49 · Speaker 3

as follows

### 00:45:54 · Speaker 6

Let's call it some S, the new data set, supervised data set. Now that has samples like this. We have U,

### 00:46:04 · Speaker 6

Let's call that U1, P1

### 00:46:09 · Speaker 6

u1, t1

### 00:46:13 · Speaker 6

U2, T2

### 00:46:19 · Speaker 6

U two T, T two T, okay, because there are T samples of noise and T samples of data, we are combining them both, okay? Now, how are we defining this? Now, T I

### 00:46:32 · Speaker 6

is equal to one if U I comes from X I. Okay? And T I is equal to zero if U I is from N I.

### 00:46:47 · Speaker 6

Do you understand what we did?

### 00:46:58 · Speaker 6

What did we do? We just created so that we had the T samples of noise and T samples of data. We combined them both, okay? And created a data set such that, uh whenever we have data samples, we gave it one label and whenever we have noise samples, we gave we gave that another label. Is that is that all right?

### 00:47:25 · Speaker 3

Hello Are you there?

### 00:47:29 · Speaker 4

Yes sir

### 00:47:32 · Speaker 3

Okay

### 00:47:34 · Speaker 6

Now what we do is the following

### 00:47:41 · Speaker 3

from the above

### 00:47:47 · Speaker 3

we have

### 00:47:51 · Speaker 3

What is the posterior of

### 00:47:53 · Speaker 3

Hello

### 00:47:54 · Speaker 6

U given T equal to one, what is this equal to?

### 00:48:02 · Speaker 7

Data PX

### 00:48:04 · Speaker 6

This is P X correct? Yeah, good. So now the distribution P

### 00:48:10 · Speaker 6

of U given T equal to zero is P N

### 00:48:16 · Speaker 6

right? P of

### 00:48:19 · Speaker 6

t equal to one is equal to

### 00:48:24 · Speaker 6

What about the priors? T equal to zero, both of them are equal to half because we have T samples of data and T samples of noise. Correct? Now with this, let us

### 00:48:35 · Speaker 3

Find

### 00:48:40 · Speaker 3

the posterior

### 00:48:44 · Speaker 3

conceiver of labels

### 00:48:48 · Speaker 3

So what are labels here? Labels are T, correct? Given data U.

### 00:48:59 · Speaker 3

What is this which is probability of

### 00:49:01 · Speaker 6

t equal to 1 given u

### 00:49:05 · Speaker 6

What is this equal to? This is equal to P of U given T equal to one divided by

### 00:49:14 · Speaker 6

p of u given t equal to zero times p of t equal to zero plus

### 00:49:27 · Speaker 6

P of U

### 00:49:28 · Speaker 3

given t equal to one plus p of sorry into

### 00:49:42 · Speaker 3

T

### 00:49:42 · Speaker 4

equal to one. Here you have P

### 00:49:51 · Speaker 4

t equal to one

### 00:49:51 · Speaker 3

t equal to 1

### 00:49:52 · Speaker 6

p of t equal to 1 no

### 00:49:55 · Speaker 7

Yes sir

### 00:49:56 · Speaker 6

Right. Yeah. This is Bayes' law, right? Now because all the priors are equal, we can just cancel the priors. All of these are half. Just cancel them. So this is equal to P of U given T equal to one, which is

### 00:50:12 · Speaker 6

P X

### 00:50:15 · Speaker 6

divided by

### 00:50:18 · Speaker 6

p n plus p x over what is this is the posterior

### 00:50:20 · Speaker 3

of

### 00:50:23 · Speaker 3

equal to one given U is given by this.

### 00:50:27 · Speaker 3

It's all right

### 00:50:34 · Speaker 3

Are we good so far?

### 00:50:38 · Speaker 4

Yes sir

### 00:50:40 · Speaker 3

Okay

### 00:50:42 · Speaker 3

Now, it's actually called the optimal base classifier.

### 00:50:46 · Speaker 4

between the samples of these two

### 00:51:00 · Speaker 6

which decides upon the ratios of posteriors, okay? ratios of class conditional densities, okay? Now, suppose

### 00:51:18 · Speaker 6

the model. So in all classifiers what do we do? We model the posterior of the label given data, right? using a neural network. parametric function.

### 00:51:37 · Speaker 3

parametric function h

### 00:51:39 · Speaker 6

of you

### 00:51:42 · Speaker 6

Right? So what is happening? We are modeling P of T equal to one given U using some parametric functions. See this is exactly what we do in all supervised learning, isn't it?

### 00:51:55 · Speaker 6

we model that using some parametric function H state of U which can be a neural network.

### 00:52:01 · Speaker 6

Okay? Now

### 00:52:05 · Speaker 6

T given U

### 00:52:09 · Speaker 6

Can somebody tell me what sort of a random variable T given U is? What is the the then what is the form of T given U?

### 00:52:20 · Speaker 5

indicator random variable

### 00:52:21 · Speaker 6

it's yeah indicator random variable all binary classification I mean all binary random variables right they are

### 00:52:32 · Speaker 6

is a Bernoulli random variable. is also indicator random variable.

### 00:52:39 · Speaker 6

What is a Bernoulli random variable? Bernoulli random variable is a random variable that takes one of two values with probability P and one minus P. Coin toss is one example, okay? It's a Bernoulli random variable with

### 00:52:53 · Speaker 6

the parameter

### 00:52:59 · Speaker 6

H theta. H theta of U, isn't it? I mean, H theta of U is the success probability of this Bernoulli random variable T given U, okay? That is what it is. Now...

### 00:53:11 · Speaker 6

Suppose we want to find the set state of U by finding out the I mean by maximizing the likelihood. So now let's write the maximum likelihood estimate.

### 00:53:24 · Speaker 7

सर, हाउ इज़ दिस पैरामीटर एच थीटा ऑफ यू?

### 00:53:28 · Speaker 6

See, that is what we have done, no? This H, we have modeled P of T equal to one given U using a parametric function. So this H theta of U is giving you that probability of T being equal to one given U.

### 00:53:45 · Speaker 6

in fact, right, all binary classifiers does the same thing. All binary classifiers, what do they do? The output of it is actually the estimate for the success probability of a Bernoulli random variable, which is the conditional random variable of label given data.

### 00:54:04 · Speaker 2

Correct?

### 00:54:06 · Speaker 6

Okay, so let us look at the ML estimate, maximum likelihood estimate for this Bernoulli random variable T given U.

### 00:54:14 · Speaker 6

How does that

### 00:54:14 · Speaker 3

look like

### 00:54:18 · Speaker 3

likelihood

### 00:54:23 · Speaker 3

likelihood function L theta for a Bernoulli random variable

### 00:54:27 · Speaker 4

In fact, the log likelihood, log likelihood

### 00:54:40 · Speaker 4

for t given u, call it l theta.

### 00:54:47 · Speaker 4

can be expressed as follows.

### 00:54:57 · Speaker 4

L theta

### 00:54:59 · Speaker 4

is equal to

### 00:55:04 · Speaker 6

We have log of products. What is the log likelihood? We know that, no, log of

### 00:55:12 · Speaker 6

P theta of

### 00:55:14 · Speaker 3

Excise

### 00:55:18 · Speaker 3

D

### 00:55:24 · Speaker 4

Hold on, that is

### 00:55:37 · Speaker 6

fog light load function it is

### 00:55:40 · Speaker 6

some of

### 00:55:42 · Speaker 6

log of

### 00:55:45 · Speaker 6

each heat of x i. This is the definition of log likelihood, no? over i. Okay?

### 00:55:54 · Speaker 6

We have written that as T here. I is the sampling index.

### 00:56:04 · Speaker 6

India

### 00:56:04 · Speaker 3

case of Bernoulli random variable what is p theta

### 00:56:15 · Speaker 3

p theta of the variable that we are looking at is

### 00:56:19 · Speaker 6

Hello

### 00:56:20 · Speaker 3

given you. Right? So what is the distribution of a Bernoulli random variable?

### 00:56:33 · Speaker 4

you write that as an indicator random variable then it is

### 00:56:41 · Speaker 4

to the power of

### 00:56:44 · Speaker 4

Okay

### 00:56:46 · Speaker 4

or rather write that as

### 00:57:02 · Speaker 4

and t equal to zero

### 00:57:05 · Speaker 4

um

### 00:57:05 · Speaker 3

Wow

### 00:57:11 · Speaker 3

product of these two

### 00:57:14 · Speaker 7

that it is p to the power t plus one minus p to the power one minus t

### 00:57:21 · Speaker 6

Yeah yeah. H theta, right? That is what it is. So you have

### 00:57:25 · Speaker 6

the distribution of Bernoulli random variable is given by

### 00:57:32 · Speaker 6

the success probability is h theta no which is h theta of u to the power t plus

### 00:57:41 · Speaker 6

one minus h theta to the power one minus t. Yeah, this is the definition of the likelihood of a Bernoulli random variable. So just substitute this here. So log likelihood will be equal to sum of

### 00:57:56 · Speaker 6

or I we have

### 00:57:59 · Speaker 6

T times log

### 00:58:01 · Speaker 3

Hello

### 00:58:04 · Speaker 3

H theta of U

### 00:58:07 · Speaker 3

Plus

### 00:58:12 · Speaker 3

one minus t times log of

### 00:58:16 · Speaker 3

1 minus

### 00:58:17 · Speaker 6

H theta of U

### 00:58:20 · Speaker 6

Okay? Now if I split this I into indices where T equal whenever T equal to one, this will become log of

### 00:58:30 · Speaker 6

H theta of X I, right? Because whenever T equal to one, we have X I as the data point. Whenever T equal to zero, we have it to be N. So this is log of one minus H theta

### 00:58:43 · Speaker 3

of N I

### 00:58:52 · Speaker 3

That's it. Okay? So now what did we what is this equal to? This is actually equal to two times two T times

### 00:59:00 · Speaker 3

J.T.F.

### 00:59:02 · Speaker 6

J T of theta which is our N C E estimate

### 00:59:12 · Speaker 6

Okay

### 00:59:14 · Speaker 6

Right? So what did we show so far, uh notwithstanding the math is that we showed that J theta is equivalent to solving a binary classification problem between the samples of P X and P theta. That is what we showed so far. How did we do that?

### 00:59:30 · Speaker 6

We first created a supervised data set where two classes were created, one for the noise and one for the data. And we looked at the optimal base classifier as the estimator of the posterior of the labels given data, right? And we modeled that as a binary Bernoulli random variable using a parametric function H theta, and we just simply obtained the maximum likelihood estimate for the posterior, which turned out to be simply the NC estimate.

### 00:59:59 · Speaker 6

Right

### 01:00:00 · Speaker 0

Then what are we saying? The summary is that

### 01:00:09 · Speaker 0

N C E is a binary classifier

### 01:00:19 · Speaker 0

Between

### 01:00:22 · Speaker 0

these samples of

### 01:00:27 · Speaker 0

fixed P theta

### 01:00:31 · Speaker 0

Is this, Is it all right?

### 01:00:40 · Speaker 0

Any questions on this?

### 01:01:14 · Speaker 3

Okay

### 01:01:16 · Speaker 3

uh okay so this is good so what we are actually doing by in noise contrast estimation is that given data we just define some noise distribution okay we get we take samples from some noise distribution that is not the data distribution and trying to learn to classify between them yeah Vivek

### 01:01:37 · Speaker 2

Uh so but somehow it seems the success depends on how well we give it the noise.

### 01:01:44 · Speaker 2

So how do we ensure that the entire, I mean like

### 01:01:48 · Speaker 2

So how big is non data distribution like it is the entire universe right what can we get?

### 01:01:54 · Speaker 3

Uh yes, that's good, that's a good question. That's a good question. We will answer that. We'll answer that eventually in this class. In fact, uh I mean, uh to uh I mean, not to make you wait. See the uh the point is, it's it's very difficult to come up with that noise distribution and that is why you might have heard this term called hard negative mining, right? In uh in contrastive learning or super self-supervising techniques.

### 01:02:19 · Speaker 3

There's this term called hard negative mining. Okay. uh Yeah, so that is actually this. How do you sample P N is a question that people have asked. We will discuss that uh briefly later. Yeah, but what I wanted to convey was this. N C E is a binary classifier between these two samples, not P theta, sorry, this is P N.

### 01:02:23 · Speaker 0

Uh

### 01:02:46 · Speaker 0

PN, Okay?

### 01:02:50 · Speaker 3

That is what it is. Okay. So now okay, fine. uh you you just let us classify between the samples of the data distribution and some random distribution. Now what, right? Now comes the most interesting part. What we would show is that solving this j theta

### 01:03:08 · Speaker 3

attains its optimal, okay? only when, uh, this h theta implicitly estimates the underlying distribution is what we will show.

### 01:03:19 · Speaker 3

Okay. uh That is something that we will uh show.

### 01:03:27 · Speaker 3

Q

### 01:03:29 · Speaker 3

just thinking should I have to do it now or just take a break and come back and do it.

### 01:03:40 · Speaker 3

Shall we take a break? Some fifteen twenty minutes break and come back.

### 01:03:48 · Speaker 3

Okay, I think you have been I think quizzed and all that. Let's take some break. So this is ten fifty, ten fifty three. Let's get back at eleven fifteen.

### 01:04:01 · Speaker 0

and continue from here. See you in fifteen twenty minutes.

### 01:27:16 · Speaker 0

Hello Shall we resume?

### 01:27:23 · Speaker 2

Yes, we can hear you.

### 01:27:24 · Speaker 0

Okay

### 01:27:26 · Speaker 3

shall we continue?

### 01:27:30 · Speaker 0

Yes

### 01:27:33 · Speaker 3

during the break I was just reading some news and do you know the name of this Elon Musk's son?

### 01:27:43 · Speaker 3

people do some codes, some codes

### 01:27:44 · Speaker 1

some court sir, some court

### 01:27:47 · Speaker 3

No, no, it's not code. I mean, it's

### 01:27:47 · Speaker 1

it's

### 01:27:51 · Speaker 3

X A A twelve or something right No no like Imagine the plight of that kid when he goes to school right

### 01:28:05 · Speaker 1

Yeah

### 01:28:06 · Speaker 3

actually not very a big fan of these complicated even it's today you know young parents in India they are also doing these weird things you know they name see because naming happens only once in life time and they want it to be exotic they name children with all kinds of random things you know I I keep thinking especially when these kids grow to be like older adults how do you call them with such weird things

### 01:28:35 · Speaker 1

you call

### 01:28:37 · Speaker 1

they'll be traumatized, sir. That's all I'm

### 01:28:39 · Speaker 3

Solid

### 01:28:42 · Speaker 3

And so many, you know, names that mean nothing. Simply they'll see somewhere and they'll say that it's a Sanskrit name. I mean, studied, you know, Sanskrit to identify that most of these names are not Sanskrit, so what to do?

### 01:28:56 · Speaker 1

and

### 01:28:58 · Speaker 1

एटलीस्ट इन इंडिया पीपल बेस्ड द नेम्स ऑन लाइक मूवीज़ एंड ऑल दोज़ प्लेसेज़ बट

### 01:28:58 · Speaker 3

at least

### 01:29:05 · Speaker 1

this pyramid kind of name ZEA twelve some one to fourteen I don't know what

### 01:29:14 · Speaker 3

Anyway. None of our business. Okay, let's get back. uh Yeah, so we were looking at noise contrast estimation and we saw that it's a binary classifier between samples of two distributions. Okay?

### 01:29:28 · Speaker 3

Okay. Now we will continue. So now okay, fine, the question is, fine, you do a binary classification between these two distributions, what's what's great about it, right? There is this very nice result that would say the following. So property two of noise contrast division estimation is that

### 01:29:52 · Speaker 3

We have J theta

### 01:29:55 · Speaker 3

to be equal to

### 01:29:59 · Speaker 3

one by two t

### 01:30:03 · Speaker 3

So, uh,

### 01:30:06 · Speaker 3

log of

### 01:30:09 · Speaker 3

h theta on x.

### 01:30:13 · Speaker 3

Plus

### 01:30:19 · Speaker 3

log of

### 01:30:22 · Speaker 3

one minus is theta evaluated at n t, right? This is what?

### 01:30:27 · Speaker 0

Hello

### 01:30:28 · Speaker 3

the loss function was. Okay?

### 01:30:30 · Speaker 0

Now, law of large numbers

### 01:30:44 · Speaker 0

to ensure

### 01:30:49 · Speaker 0

that

### 01:30:53 · Speaker 0

J theta is approximately equal to

### 01:30:55 · Speaker 3

to some j tilde of theta where j tilde of j tilde of theta is given by the following. It is half

### 01:31:12 · Speaker 0

expectation of

### 01:31:15 · Speaker 0

log of

### 01:31:18 · Speaker 0

H

### 01:31:21 · Speaker 0

It's theta evaluated at x.

### 01:31:29 · Speaker 0

plus log of

### 01:31:32 · Speaker 0

1 minus h theta

### 01:31:34 · Speaker 3

evaluated at N

### 01:31:39 · Speaker 3

And this expectation is over the joint distribution of P, X and N.

### 01:31:45 · Speaker 0

This is what the law of large numbers says.

### 01:31:58 · Speaker 0

Okay, this we know, right? I mean, if you have

### 01:32:01 · Speaker 3

samples from distributions then expectation can be approximated using sample averages we inverted that meaning we said that this was a this mean this was

### 01:32:13 · Speaker 3

a sample average, right? Whatever we had in J theta was a sample average. We just converted that into T equal to one to two T, converted that into uh expectation.

### 01:32:24 · Speaker 0

Okay

### 01:32:24 · Speaker 3

Okay

### 01:32:25 · Speaker 0

Wow

### 01:32:31 · Speaker 0

suppose

### 01:32:49 · Speaker 0

F

### 01:32:51 · Speaker 0

is given by

### 01:32:54 · Speaker 0

log of

### 01:33:12 · Speaker 0

Direct

### 01:33:25 · Speaker 0

Let

### 01:33:27 · Speaker 0

that p theta of x denote

### 01:33:34 · Speaker 0

the distribution

### 01:33:43 · Speaker 0

being estimated

### 01:33:49 · Speaker 3

via N C E, okay? So we solve this optimization problem. We are implicitly imposing a distribution on the model, let's call that as P theta, okay? Now...

### 01:34:01 · Speaker 0

Uh

### 01:34:18 · Speaker 0

Now let F

### 01:34:21 · Speaker 0

B equal to

### 01:34:22 · Speaker 3

to

### 01:34:23 · Speaker 3

log of

### 01:34:26 · Speaker 3

P theta of X

### 01:34:30 · Speaker 3

Okay? Now what can be shown is that I'll just keep the proof for the want of time. J theta can be shown to be equal to half

### 01:34:40 · Speaker 0

of expected value of log of

### 01:34:45 · Speaker 0

or

### 01:34:48 · Speaker 0

Perfect

### 01:34:50 · Speaker 0

minus

### 01:34:52 · Speaker 0

log of

### 01:34:54 · Speaker 0

pn of x

### 01:34:58 · Speaker 0

plus

### 01:35:02 · Speaker 0

expected half times the expected value of log of

### 01:35:07 · Speaker 3

one minus R times

### 01:35:13 · Speaker 3

f of n minus log of

### 01:35:19 · Speaker 3

P N evaluated at N

### 01:35:26 · Speaker 3

So this equivalence, I will not show, I mean this is only an algebraic manipulation. What can be shown is that this J theta uh can be written equivalently this way where R, something that we don't know.

### 01:35:38 · Speaker 3

where R is simply the logistic function. R of K is one by one plus e power minus K. R is the logistic function. When it involves just rewriting the equation.

### 01:35:57 · Speaker 3

rewriting the equation of J in terms of what we know, okay? So why is this important? So again I will state a theorem without proof which again can be solved easily. I'll tell you how to do it, proved easily. So theorem is that

### 01:36:15 · Speaker 3

Okay, so with this what happens is your j theta now can be written as a function of f, no?

### 01:36:24 · Speaker 3

because we yeah question

### 01:36:25 · Speaker 2

three

### 01:36:27 · Speaker 2

सर, इन द फर्स्ट टर्म, दिस आर

### 01:36:30 · Speaker 1

फॉर दिस फंक्शन आर द आर्गुमेंट इज जस्ट एफएक्स और एफएक्स माइनस लॉग पीएन ऑफ एक्स।

### 01:36:35 · Speaker 3

So it is R of f of x yeah. So R is a logistic sigmoid right? So it is R of f of x right? And R of f of n minus log p n n into n correct. Yeah the bracket was missing. Okay. So now you represent this entire see what did we do? I mean we represented the log likelihood of the underlying distribution using some function f strictly speaking this is f theta right? And we represented the noise contrast estimator in terms of f theta. okay? Now, this theorem which is the most powerful theorem that would say that the

### 01:37:15 · Speaker 0

Optimal Value

### 01:37:22 · Speaker 0

of F theta

### 01:37:26 · Speaker 0

that would

### 01:37:33 · Speaker 0

optimize

### 01:37:36 · Speaker 0

J tilde of theta

### 01:37:40 · Speaker 0

is such.

### 01:37:43 · Speaker 0

that

### 01:37:48 · Speaker 0

F star

### 01:37:48 · Speaker 3

R

### 01:37:50 · Speaker 3

is equal to log of px

### 01:37:56 · Speaker 3

This is the most important result. Okay now the question that we are asking is the following. I'll tell you how this how we would get it that way okay. The question that we are asking is that what would be the F star okay that would

### 01:38:15 · Speaker 3

maximize this objective. Or minimize this minimize the negative of this objective is the question, right? Because the only variable here is F, no? We are searching for an F, okay? That would maximize this objective. What can be shown is that irrespective of what N you are choosing here.

### 01:38:35 · Speaker 3

that f which is maximizing the objective j theta non contrastive estimator j theta is the one for which the f happens to be the log of log likelihood of the true underlying data distribution. Now how do we get that? So we get that by writing this entire thing in terms of double integral right this expectation will be written in terms of the double integral of this thing times px into n assuming that noise and data are independent you write these as originals over PX and PN, okay?

### 01:39:12 · Speaker 3

dx dn and then you differentiate this integral with respect to f and put it to zero what you will get is that the optimal f is going to be log of px that is what it is I mean you need a bit of variational calculus to show that which is beyond scope of this particular course and that's why I'm skipping the the proof but yeah but the result is that

### 01:39:34 · Speaker 3

The optimal value for the noise contrast estimator is when the log of the distribution that it is that it is implicitly imposing on the model is equal to the log of the likelihood of the underlying data distribution.

### 01:39:54 · Speaker 3

Okay, there's a very powerful result. So now the summary or the take home message from this, what is the consequence of this is? Summary is that

### 01:40:06 · Speaker 3

one can use or rather

### 01:40:10 · Speaker 0

Solving

### 01:40:13 · Speaker 0

the classification problem in the NC estimate

### 01:40:25 · Speaker 0

Between PX and PN

### 01:40:29 · Speaker 0

என்

### 01:40:32 · Speaker 0

well implicitly

### 01:40:38 · Speaker 0

Learn

### 01:40:40 · Speaker 0

the underlying distribution P theta

### 01:40:52 · Speaker 0

constribution p x. This is the most important

### 01:40:55 · Speaker 1

result

### 01:40:56 · Speaker 3

Okay, so you understood, right? So what we are doing is suppose we have

### 01:41:01 · Speaker 3

a classifier that is built

### 01:41:04 · Speaker 3

So let's say that we take x or n to this. This is your h theta and this will finally give you one or zero. Okay? Trying this what we are saying is if you take the intermediate representations of this. Okay? So let's call this as

### 01:41:23 · Speaker 3

f theta of x because as you saw what the h theta

### 01:41:30 · Speaker 3

was the logistic sigmoid of f theta of x. So whatever you get before the the final layer is the logistic sigmoid. So whatever you get before the uh the final layer, penultimate layer or the logits is what you call as f theta. And we know that f theta, the optimal f theta is log of f of x.

### 01:41:52 · Speaker 3

right? And what we can use that we can write Z

### 01:41:57 · Speaker 3

to be equal to f theta of x

### 01:42:01 · Speaker 3

as the features or embeddings or representations.

### 01:42:12 · Speaker 3

That's it. So this is the result. So what we are saying is that you don't have to do anything. All you need to do is that if you are given some data, okay, define some noise.

### 01:42:22 · Speaker 3

sample from it and learn to classify between the data and denoises. So now if you do that, then you are implicitly learning the underlying distribution, take the logics of that classifier and use that use those as features. See this is the this is what is called as the contrastive learning.

### 01:42:45 · Speaker 3

self-supervised learning. So what is the self-supervision part here? Remember that we defined a pseudo task, no? The pseudo task, the pretext task that we defined here is that of classification, right?

### 01:42:58 · Speaker 3

This is the fundamental bedrock of contrastive or self-supervised learning, okay, where it comes from noise contrastive estimation that would say that solving an optimization problem, uh which turns out to be classification between the data distribution and some noise distribution, will implicitly learn the underlying data distribution up to a constant.

### 01:43:26 · Speaker 3

Yes. Any questions here? See this is the idea. I mean everything else that came after this no it's only a improvisation over uh this idea but this is the fundamental idea.

### 01:43:39 · Speaker 0

Silly

### 01:43:43 · Speaker 0

Any questions here?

### 01:44:03 · Speaker 0

Hello, I am

### 01:44:06 · Speaker 0

Is there? Am I audible?

### 01:44:09 · Speaker 1

Yes sir you are

### 01:44:10 · Speaker 3

okay

### 01:44:12 · Speaker 3

This is a very powerful result, right? I mean, it is saying that that I mean all you need is to simply classify between data distribution and some noise distribution. And if you do it, please note that these results are asymptotic in the sense that this will this will give you an estimate for the log likelihood of the underlying data distribution only if you have enough samples. Now as Vivek was asking before the break. Now, how do you know what noise distribution would help it in

### 01:44:42 · Speaker 3

In fact, what can be shown while doing this proof is that the larger is the divergence between PX and PN, the better it is to estimate the underlying data distribution, okay? Now, getting those noise samples is very important. Now that is why we have so many methods on how do you define the hard negatives, how do you how do you come up with the negative samples, okay?

### 01:45:05 · Speaker 3

But yeah, so this is the fundamental idea of why should solving a pretext task, okay, or a pseudo label task

### 01:45:15 · Speaker 3

should help you in uh learning the data distribution. Please note that this is this entire thing is non-generative in the sense that you can't sample points from P X from this, right? Is this clear? This is not generative, right?

### 01:45:36 · Speaker 0

not able to sample from P X.

### 01:45:43 · Speaker 0

is a non-generative

### 01:45:52 · Speaker 0

Okay

### 01:45:53 · Speaker 3

Sir, if we are not able to generate

### 01:45:55 · Speaker 1

create some samples then how can we say that we have learned the original data distribution

### 01:46:01 · Speaker 3

That's what we saw so far, right?

### 01:46:04 · Speaker 3

See what we showed was that, see we are not able to sample from this thing, but

### 01:46:11 · Speaker 3

solving this classification task, what we are getting is at the penultimate layer of this classifier, we are learning the log of the underlying distribution is what we just showed, isn't it? The entire today's class was on that.

### 01:46:24 · Speaker 0

Yes sir

### 01:46:25 · Speaker 3

Yeah. So we can learn the underlying data distribution even without sampling for the distribution is what we should.

### 01:46:34 · Speaker 1

Sir, from this if we connect it to a sampler, it can ideally sample it, right? I mean, we got the distribution, right? Data distribution.

### 01:46:43 · Speaker 3

No, we didn't. No, not explicitly, right? See, given an x, it will... See, what is this penultimate layer giving you? Given an x as an input, it is giving you log of px of x, that's all, right? It is not telling you what px of x is.

### 01:47:00 · Speaker 1

So there is no way to reverse engine.

### 01:47:02 · Speaker 3

There is no way absolutely no way no.

### 01:47:05 · Speaker 3

But what is what is important is that if you know log of px of x for all samples, then you know everything about the data. That is why these features are powerful.

### 01:47:17 · Speaker 3

See, why do you think bird embeddings are so, in fact, bird also does exactly this thing. We will come to that in a while. Why do you think those are so powerful is because if you do this well, okay, with a large number of samples so that the law of large number is is is respected, then the the representations or the embeddings that you are getting from this classifier are actually estimating the log likelihood of the data. Right? That's all. So you know everything about the data. So you can use it for anything that you want. That is the idea. But you are not able to sample from here. Yeah.

### 01:47:49 · Speaker 0

Thank you sir

### 01:47:51 · Speaker 3

something else?

### 01:47:55 · Speaker 3

See, uh compare this with let's say a VAE or a diffusion model or a DDIM where you will get embeddings, okay, as

### 01:48:04 · Speaker 0

as well as ability to sample

### 01:48:09 · Speaker 0

Right?

### 01:48:13 · Speaker 0

So this

### 01:48:15 · Speaker 3

I

### 01:48:17 · Speaker 3

generative pre-training, no, GPT. So that is an example where you have the embeddings and also the the generative ability. We will look at GPT probably in the next class, right? uh where you generate the embeddings, right? Or rather find an embedding space, representation and also learn to sample implicitly from, I mean, together, just like a diffusion model or a VAE. In a GAN, right? For instance, in a naive GAN,

### 01:48:48 · Speaker 3

Can somebody tell me what abilities does it have?

### 01:48:56 · Speaker 2

regenerative

### 01:48:57 · Speaker 3

it can generate it can generate it can't find out the it can't do posterior inference. But we did see some examples right in your assignment I had asked you to did I ask you to do that or not like for build a classifier or an inverter over the generator and solve a reconstruction task over the latent space. Did I ask you to do that?

### 01:48:57 · Speaker 0

It can generate

### 01:49:21 · Speaker 0

Yes sir

### 01:49:22 · Speaker 3

Yeah. So you have done that, right? So now you can you can improvise GAN to to to do an inversion or a embedding extraction as well, okay?

### 01:49:33 · Speaker 3

Right, Sarvesh

### 01:49:36 · Speaker 1

So so in this case so this f theta for this

### 01:49:39 · Speaker 3

description

### 01:49:40 · Speaker 1

minute of

### 01:49:40 · Speaker 2

Will it be a scalar? Single number?

### 01:49:46 · Speaker 3

In course

### 01:49:46 · Speaker 2

A little bit

### 01:49:47 · Speaker 2

वी आर गेटिंग ओनली वन आउटपुट रेट, वन और ज़ीरो, सो

### 01:49:52 · Speaker 3

Yeah, that's a very good question. Yeah, it will be scalar. And that's why people said, okay, let's move away from this. Why only do a binary classification problem? Let us solve an N class classification problem, which is what is called as info NC.

### 01:50:09 · Speaker 0

okay, where the idea is to extend N C

### 01:50:18 · Speaker 0

to a

### 01:50:21 · Speaker 0

मल्टी क्लास क्लासिफिकेशन साठी

### 01:50:27 · Speaker 2

so that we can get a vector of embeddings.

### 01:50:29 · Speaker 0

Correct

### 01:50:31 · Speaker 0

Okay

### 01:50:36 · Speaker 3

So what infancy does is that it is simply a multi-class classification problem. So given a

### 01:50:41 · Speaker 0

Data Point

### 01:50:47 · Speaker 0

at a point X I, okay? Define

### 01:50:57 · Speaker 0

K

### 01:51:01 · Speaker 0

noise examples or noisy examples.

### 01:51:18 · Speaker 0

from PN and

### 01:51:22 · Speaker 0

solve a K class classification problem.

### 01:51:33 · Speaker 0

Between

### 01:51:35 · Speaker 0

Exile

### 01:51:35 · Speaker 3

In fact, it's actually K plus one classification problem and K negative sample.

### 01:51:42 · Speaker 3

noisy samples.

### 01:52:00 · Speaker 3

Okay, this is this is what noise sorry, Info NC does. The paper's name is representation learning with contrastive predicting coding. Okay, it's nothing but extension of noise contrastive estimation. Okay, for

### 01:52:19 · Speaker 3

K class classification problem. So let me

### 01:52:24 · Speaker 3

just show you show you the paper give me a second

### 01:53:04 · Speaker 0

Let me share my screen and show you

### 01:53:09 · Speaker 0

Yes, screen

### 01:53:19 · Speaker 3

Do you see my screen?

### 01:53:23 · Speaker 0

Yes sir

### 01:53:25 · Speaker 3

but anyway this is the

### 01:53:29 · Speaker 3

This is the paper on noise contrast estimation. It's a very very nice paper, okay? Very old but this is the one that noise contrast estimation, a new estimation principle for abnormally statistical models. Please look at this paper, it's very good, okay? Like two thousand ten it appeared, okay? But it was just sort of buried because this could not be scaled to higher dimensions because then the neural networks were not very powerful. It's a very nice paper, okay? Have a look at it. Then came the uh

### 01:54:01 · Speaker 3

info N C E paper twenty nineteen which is called representation learning with contrastive predicting coding. Okay. So where uh what they do is just extend N C E for a K class classification setting.

### 01:54:17 · Speaker 3

given a set x of n random samples containing one positive sample from the distribution that you want to estimate and n minus one negative sample from the proposal distribution. right? so yeah so if you take a set of n samples okay? uh one of them is the so called positive sample or the data sample from the data distribution and there are n minus one negative examples. you define the n c loss as the negative of the expected loss of expected value

### 01:54:47 · Speaker 3

of the log of this thing. So what is this if you look at it this is nothing but the softmax okay. Where F K will give you the uh the Kth output of the softmax in the neural network okay. And it is summed over all possible other samples.

### 01:55:05 · Speaker 3

This is all right. This is the info NC loss. Now what uh can be shown just like the NC counterpart is that optimizing the optimal value of this FK is the one that gives you the log of this underlying data distribution. It's just simple extension of NC, okay, for a K class classification problem.

### 01:55:29 · Speaker 3

Is this okay?

### 01:55:31 · Speaker 3

Now this, okay, came in two thousand nineteen and this was extended to uh the contrastive learning. This was Hinton's paper, right? This was well celebrated. This was called this is called SIM CLR. Okay? Stands for simple framework for contrastive learning of visual representations. Now look at this graph. What they show is the following that if you take the image in a top one accuracy, uh you take the representations that are

### 01:56:01 · Speaker 3

given by the sincere and do a fine tuning. So now what do you do with the representations? You take those representations and if you want to solve a classification task, just fine tune another classifier using those representation. That is how you use it. It was shown that it just beats all the the existing state of the art, okay? On yeah, fully supervised is of course the the best that you can get, right? But even with like very less number of parameters

### 01:56:31 · Speaker 3

on the fine tuning of the fine tuning network you can get a pretty comparable result is what was shown. Okay. Now what does this do? This is nothing but info NC. Look at this expression. So this loss function that is used in SimCLR is nothing but the the info NC loss. Okay. Write it as the dot product between. So what they have done is look at the

### 01:56:58 · Speaker 3

info in C paper. They write this FK, right, as a dot product.

### 01:57:06 · Speaker 3

between the representations for the positive sample and the negative sample and this is just the normalization constant.

### 01:57:15 · Speaker 3

Okay? So what is done is the following that given an image

### 01:57:21 · Speaker 3

an image. They create multiple augmentations of the image by doing these kinds of things, crop and resize and then you have color distortions, you add some Gaussian noise and make blur it out and you do sobel filtering and extract the edge and all that, okay? Now what they do is

### 01:57:40 · Speaker 3

given this particular image, all of these counterparts are taken to be the positive, positive counterparts of this particular image. Okay? And then what they do is whenever the network sees these augmentations, they want the network to output one. See, think of it like solving a K class classification problem where the original image and all of these augmentations are taken to be of the same class.

### 01:58:10 · Speaker 3

class, okay? And all the other images that does not correspond to this original image is taken to be the from the other classes and you solve a K class classification problem.

### 01:58:26 · Speaker 0

Does it make sense?

### 01:58:35 · Speaker 2

Yes, sure

### 01:58:36 · Speaker 0

Any questions on this?

### 01:58:40 · Speaker 2

So this one will result in

### 01:58:43 · Speaker 2

k plus one vector outright

### 01:58:48 · Speaker 2

I mean the the the the dimension of the

### 01:58:48 · Speaker 3

the

### 01:58:50 · Speaker 3

not not necessarily. See the way no no the way they have done is they have taken the uh the penultimate layer to be of some d dimensions okay. Now the loss function will take those d dimensional vectors and compute the dot product between those representations here. That is how they they implement this F K.

### 01:58:51 · Speaker 2

representation

### 01:59:16 · Speaker 3

So you can you can actually customize it.

### 01:59:19 · Speaker 2

Okay, yeah.

### 01:59:20 · Speaker 3

Yeah, because the the I mean they don't implement it as cross entropy, they implement it as the dot product between the representations that have been gotten between these two.

### 01:59:37 · Speaker 0

Any other question on this?

### 01:59:41 · Speaker 3

And see, the fundamental idea is that of the uh NC, okay? Now improvisations have been done where instead of solving a binary classification problem, you solve a K class classification problem. Now you represent the objective of the

### 02:00:00 · Speaker 3

K class classification problem in terms of uh in terms of dot products, right? Or inner products between the pre-logit layers, okay? That is proportional to of course the binary cross I mean categorical cross entropy, right? I mean that is what SimCLR does.

### 02:00:25 · Speaker 3

This is all right

### 02:00:31 · Speaker 4

Yes sir, but there is no noise involved here now, right?

### 02:00:35 · Speaker 3

well you can see all the negative samples that you get here right? I mean is actually the noise.

### 02:00:40 · Speaker 4

Okay

### 02:00:43 · Speaker 3

See if you look at the algorithm what they do is, uh they take one sample, okay, one data data example, okay, and create all the augmentations of it and call it the positive example. Okay? And then what they do is they sample randomly, I'll just show you that.

### 02:01:07 · Speaker 3

See here they say that we don't sample negative examples explicitly. Instead given a positive pair we treat the other two n minus one augmented examples with a mini batch as negative examples. This is the way they define the noise here.

### 02:01:20 · Speaker 4

ओके, ओके सर

### 02:01:22 · Speaker 3

Right. But again, as I said, there are lots of improvisations over it. I mean, then people came up with something called Moco, right? Momentum update contrast if encoded, yeah.

### 02:01:32 · Speaker 4

important, yeah. So what effect does this actually have? This just tries to push away the vectors from each other. Like if you're going to say the dot product.

### 02:01:43 · Speaker 3

not push away, right? What is what this what it will do is whenever you have the positive pairs, it will try to cluster them together. Whenever they are they are they are negative pairs, they will try to push them apart. That is what a classifier also does, isn't it?

### 02:01:45 · Speaker 4

Potash

### 02:01:51 · Speaker 4

whenever

### 02:01:59 · Speaker 4

Right, yeah. So, okay.

### 02:02:00 · Speaker 3

Right? That is exactly what a classifier does. It is it is trying to cluster the points that are from one category. It is trying to push the points from the other categories away. That's all. Now, what is the intuition? See, I did the math because I mean, you might have probably known from the course so far is that I I mean, my I get convinced better if I if I'm showed if if I'm shown some mathematical guarantees of what's actually happening. But I can give you some intuition also. So what is actually happening?

### 02:02:30 · Speaker 3

with all these methodologies is that suppose you know how to like group all these all these examples as close to this dog image and a cat image you know how to push the cat image away from this you can't do it as you can't do it or rather you can do it only if you understand the semantics of this object called dog isn't it

### 02:02:58 · Speaker 0

Okay

### 02:02:58 · Speaker 3

See, if somebody wants to put this dog image and this cutout dog image into one same category, they should know that okay, this is actually a cutout version of this dog, isn't it?

### 02:03:10 · Speaker 4

Right. Okay.

### 02:03:12 · Speaker 3

Right? So that's the whole point. So now as means do you recall these uh these these question types that we we we were having we were having when we were going to school, right? One of the question types was this thing called fill in the blanks, isn't it?

### 02:03:19 · Speaker 4

Yeah

### 02:03:29 · Speaker 3

Yeah. They used to give a give a sentence and used to ask us to fill in the gaps, randomly mark some of the words and ask them to ask us to fill the gaps. Now you can do it only if you know perfectly what the semantics are, isn't it?

### 02:03:29 · Speaker 4

They used

### 02:03:45 · Speaker 4

Yes, yes.

### 02:03:47 · Speaker 3

touch the whole point. In fact, the all these language LLMs today are learned using that technique, this technique only. Which is that, yeah, which is the mass reconstruction. So you have data, you mass some parts of it and try to reconstruct it back. So which is nothing but classifying between the data sample and the noise sample.

### 02:03:55 · Speaker 4

that

### 02:04:10 · Speaker 2

ओके सर

### 02:04:11 · Speaker 3

I'm

### 02:04:13 · Speaker 3

Okay, so any other question on this?

### 02:04:16 · Speaker 0

सर, वन क्वेश्चन.

### 02:04:17 · Speaker 3

Hmm

### 02:04:18 · Speaker 0

So there is a two into n minus one images right? What is that two indicates here? Is that two augmentations only we do for image?

### 02:04:27 · Speaker 3

No no no no. Given an image you take n augmentations.

### 02:04:32 · Speaker 3

and you sample another random points.

### 02:04:37 · Speaker 3

Right? Okay. So that will make it 2n minus 1, isn't it?

### 02:04:37 · Speaker 2

Okay

### 02:04:41 · Speaker 3

I mean, they count from zero, that's why there are like two times n minus one.

### 02:04:47 · Speaker 3

Basically it's two N. So you take an image or a data point, you take N augmentations of it and call all of them as positive, right? And then you sample N negative samples from the data set. So that will make it two N, no? Two capital N. That's all it is.

### 02:05:03 · Speaker 4

in

### 02:05:05 · Speaker 4

सर, एंड नेगेटिव सैंपल्स हियर मीन्स कैन यू क्लेरिफाई?

### 02:05:10 · Speaker 3

You need samples from the noise distribution, right?

### 02:05:15 · Speaker 4

Yes

### 02:05:15 · Speaker 3

what is done is that you take a dog image and you take n augmentation that will give you the positive ones.

### 02:05:22 · Speaker 4

Okay

### 02:05:24 · Speaker 3

You need samples from the noise distribution as well. So what is done is people just sample n random points from the uh from the data set itself. I'll call them the samples from the noise.

### 02:05:39 · Speaker 4

from this doc data set itself

### 02:05:41 · Speaker 3

not dog. This data set has all kinds of objects.

### 02:05:46 · Speaker 3

This data set has all kinds of objects. So now if you randomly do a sampling from all objects, the other N samples that you have gotten, uh hopefully are not from the doc category. That's a good point that you made. See what happens is, these methods, especially SimCLR, has been shown to work well only if you have a very, very large batch size.

### 02:05:53 · Speaker 0

Okay

### 02:06:08 · Speaker 3

Okay. Now why is that the case is because suppose you have like a you have very small batch size. When you take when you do a like uh sampling for I mean negative sample with N samples with N being very small, there's no guarantee that these so-called negative examples that you get are not from the doc category, isn't it? You don't have control because we have no labels.

### 02:06:34 · Speaker 3

right? But if you make our batch size to be very very large, then

### 02:06:39 · Speaker 3

What happens is if you take if you sample a very large number of samples then most of them will not be from the class that you are considering uh for this particular example. That's why the SimCLR is known to work only with very large number of examples like very large batch sizes.

### 02:07:01 · Speaker 3

Yeah. Okay, questions on this? Yeah, Vivek.

### 02:07:05 · Speaker 4

So, uh, one question. So, is the noise contrastive estimation the same as out of data distribution detection?

### 02:07:15 · Speaker 3

sort of, yeah, you can you can you can view it as like outlier detection actually, yeah.

### 02:07:24 · Speaker 3

See, uh if you if you are solving a binary classification problem, yes, it is outlier detection. If you are solving a K class classification problem, then like detecting outliers from multiple distributions. That is what it is.

### 02:07:36 · Speaker 4

No, so outlier is a very specific case. What I mean is something like a out of distribution detection, which means... Agreed. Agreed. Agreed. You want to...

### 02:07:44 · Speaker 3

agree. agree. agree. you want to you you are classifying between the the set of samples samples of the data distribution and everything that is not the data distribution. yes.

### 02:07:50 · Speaker 4

set of

### 02:07:54 · Speaker 4

Yes, yes, yes, yeah.

### 02:07:58 · Speaker 3

See that that's how human beings also learn no if you know how to classify between you know what is important what is not important then then you have learned the tricks of the life. That's what they say.

### 02:07:58 · Speaker 4

So

### 02:08:12 · Speaker 1

ओके. ओके सर.

### 02:08:17 · Speaker 3

Okay. Okay, so let me come back, get back to this. As I said, there are multiple improvisations over it. So now one question that people ask is, uh now, uh how do you reduce the batch size in SimCLR? So one way to do it is that whenever you are sampling from the noise distribution, as Vivek was asking, uh you sample the noise points in such a way, right? That uh that they are very, very

### 02:08:47 · Speaker 3

I mean they are they are pretty away in the representation space from the data samples. Okay. Now this is called hard negative sampling. Just write it down.

### 02:09:04 · Speaker 1

The question is like

### 02:09:12 · Speaker 1

How to

### 02:09:14 · Speaker 1

Sample

### 02:09:16 · Speaker 1

better negative examples or better

### 02:09:21 · Speaker 1

noisy or negative samples.

### 02:09:42 · Speaker 2

So now there are this is called hard negative mining.

### 02:09:51 · Speaker 3

hard negative mining where given a particular sample, okay?

### 02:09:58 · Speaker 3

How do you make it hard in the sense that how do you ensure that that this negative sample is actually contributing to learning? There are multiple ways. One way to do it is that given a sample, you take all the augmentations of it and call it positive. For the negative samples, you do for every sample that is that you get from the data set, okay? And please note that for the case of methods like SimCLR, the noisy samples are

### 02:10:28 · Speaker 3

actually the samples from the data set itself that does not correspond to the uh the augmentations of the given input sample. I hope that that is clear. Is that clear?

### 02:10:41 · Speaker 3

Let me write that down. What I mean is, in methods

### 02:10:44 · Speaker 1

just like SimCLR

### 02:10:56 · Speaker 1

the noisy or the negative samples

### 02:11:10 · Speaker 1

Are

### 02:11:15 · Speaker 1

the points from the data distribution

### 02:11:25 · Speaker 1

dot R

### 02:11:29 · Speaker 1

Nine

### 02:11:29 · Speaker 1

Art the

### 02:11:33 · Speaker 2

augmentations

### 02:11:38 · Speaker 2

of the

### 02:11:40 · Speaker 1

given input sample

### 02:11:46 · Speaker 3

So that way it slightly differs from you know as contrast estimation. In the sense that the the in distribution samples are taken to be the one that that one taken to be a sample and its augmentations. The out of distribution samples are taken to be a few randomly sampled points from the data set itself.

### 02:12:11 · Speaker 3

Right? So example is right I mean suppose you have a have an image of of of of a digit one then the positive examples are its rotation and the mass version of it and you have the noisy version of it all of these are taken to be the in

### 02:12:30 · Speaker 3

These are positive examples or indistribution samples.

### 02:12:36 · Speaker 3

Okay? And you take the images of let's say two, three, five, etcetera. All these are taken to be negative examples.

### 02:12:49 · Speaker 3

And then you learn to classify between these two in a K-class classification setting. So this is also called as the anchor point.

### 02:12:58 · Speaker 3

anchor point or the data point at over interest, okay, of interest. So, all the contrastive learning or self-supervised learning techniques would learn to classify between the samples of positive and negative examples.

### 02:13:17 · Speaker 3

Is this clear?

### 02:13:17 · Speaker 5

So but in this current context we do not have the labels right so that's why we are doing random sampling

### 02:13:21 · Speaker 3

we don't we don't we don't. Exactly exactly. So now see what might happen no like one particular sample from the same class might creep up here right that's why you need a large batch size that's what I'm saying. So these examples have to be negative enough for this to work because they have to actually come from P N. Now that's why if you have a very large batch size then the the likelihood of having samples not from the same class or semantic label as that of the anchor point. is less. This is the idea.

### 02:13:55 · Speaker 3

Alright

### 02:13:57 · Speaker 5

So you need some kind of balanced data set here, right?

### 02:13:59 · Speaker 3

uh not balance you need a yeah I mean you can say balanced only you need a lot of negative samples that's all

### 02:14:10 · Speaker 2

Okay. Now, um,

### 02:14:17 · Speaker 3

Any questions so far?

### 02:14:21 · Speaker 3

So this is shown to be very powerful as I said no SimCLR etcetera would reduce the uh the dependence on the supervised I mean labels by a drastic amount of uh attraction is there. So examples of this approach contrast learning approaches in the image space you have some methods like SimCLR or you have Moco and there's this thing called Japa I will talk about it. Okay. in the space of NLP, all these modules such as BERT and

### 02:15:01 · Speaker 3

What is that other thing called? It is Word2Vec.

### 02:15:06 · Speaker 3

all these are variants of this N C E and info N C E, okay?

### 02:15:10 · Speaker 1

So how about clip

### 02:15:13 · Speaker 3

clip is also there but clip is for like it's for cross it's for multi multimodal data but the idea idea is exactly the same I can add it yeah. I will write it so for speech you have the

### 02:15:17 · Speaker 1

Cross Mode

### 02:15:19 · Speaker 1

Modem

### 02:15:25 · Speaker 3

way to work for

### 02:15:29 · Speaker 3

image plus

### 02:15:32 · Speaker 3

text you have

### 02:15:39 · Speaker 3

What does this clip stand for? I keep forgetting that.

### 02:15:43 · Speaker 3

contrast tips pre training for images and languages it that's what

### 02:15:50 · Speaker 2

um

### 02:15:57 · Speaker 3

opening the clip paper

### 02:16:07 · Speaker 5

contrastive language image pre training

### 02:16:10 · Speaker 3

contrastive language image pre-training, okay.

### 02:16:16 · Speaker 3

Now that we spoke of clip, no, maybe I can also talk about it. So you know how it is done? Clip. So now there is a

### 02:16:29 · Speaker 1

The objective is to learn

### 02:16:38 · Speaker 1

on the representations or encodings.

### 02:16:48 · Speaker 1

Jointly

### 02:16:52 · Speaker 1

between

### 02:16:52 · Speaker 2

in the

### 02:16:56 · Speaker 2

image and text modalities.

### 02:16:59 · Speaker 2

See this can be extended to any multimodal thing.

### 02:17:02 · Speaker 3

Okay, text. Modalities.

### 02:17:07 · Speaker 3

How is it done? You have you take two networks. So one we call as F theta. The other you call as

### 02:17:17 · Speaker 3

G theta

### 02:17:19 · Speaker 3

this is the

### 02:17:22 · Speaker 3

text encoder and you have the image encoder. So this will take

### 02:17:30 · Speaker 3

text as input. This will take images as input.

### 02:17:40 · Speaker 3

Okay, what they do is they take so for this you need to have pairs of images and text. Okay, the data that you have is you have images

### 02:17:52 · Speaker 3

you have an image, comma text, that is the kind of data that you have, okay? Now, uh

### 02:18:01 · Speaker 3

you need the pair. I don't think you need the pair.

### 02:18:05 · Speaker 4

We need the pairs.

### 02:18:07 · Speaker 3

Do we

### 02:18:08 · Speaker 4

Yes, very much and in very large numbers.

### 02:18:12 · Speaker 3

let me just think about it.

### 02:18:21 · Speaker 3

So contrasting pre-training you have the

### 02:18:26 · Speaker 3

Hold on, let me just see.

### 02:18:33 · Speaker 4

in a given batch there is a set of images and their captions

### 02:18:38 · Speaker 3

You need the corresponding captions also, no?

### 02:18:38 · Speaker 4

You need a different

### 02:18:41 · Speaker 4

Yes

### 02:18:43 · Speaker 4

And only thing is in that

### 02:18:44 · Speaker 3

in that

### 02:18:45 · Speaker 3

you do need pairs

### 02:18:46 · Speaker 4

Hello

### 02:18:49 · Speaker 4

I mean it has to be a set and in that set uh whatever uh belongs to that image that only those dot products should be maximized and all the others should be minimized.

### 02:19:01 · Speaker 3

Yeah, so what is done is I'll tell you. Yeah. If you do the same thing, no, for every text you get, yeah, what will happen is

### 02:19:11 · Speaker 3

For text, let's say that you get uh some T one, T two corresponding to some T N, there are embeddings for N possible text. And similarly for images, suppose there are N images, right? You get image one, image two up to image N. Okay? So you take N embeddings from the uh

### 02:19:38 · Speaker 3

n embeddings from the image encoder, n embeddings from the text encoder, okay? Then you have an n by n matrix of

### 02:19:48 · Speaker 3

embeddings, right? So this is let's say that this is the text dimension and you have this is as the image dimension.

### 02:20:01 · Speaker 3

Okay? So what does this tell you? This will give you along the diagonal

### 02:20:08 · Speaker 3

right? This will tell you the the inner product between the image embedding with the corresponding

### 02:20:18 · Speaker 3

extensible, isn't it? Now what you need is maximize the

### 02:20:25 · Speaker 2

inner product

### 02:20:30 · Speaker 2

or

### 02:20:30 · Speaker 3

rather this itself no is the inner product matrix so let's call this matrix let me write it down hold on

### 02:20:37 · Speaker 3

Let's call this as I P. Now I P at I comma J is the

### 02:20:46 · Speaker 3

dot product between the Ith text embedding and the Ith image embedding and the Jth text embedding, okay? The objective is to find theta and phi such that it

### 02:21:04 · Speaker 3

maximizes

### 02:21:06 · Speaker 3

the

### 02:21:08 · Speaker 1

diagonal of I P, right? And

### 02:21:24 · Speaker 1

maximizes this divided by

### 02:21:27 · Speaker 1

Oh

### 02:21:34 · Speaker 1

take the sum of all those, hold on.

### 02:21:43 · Speaker 1

So more or less you have

### 02:21:46 · Speaker 1

Diagn

### 02:21:47 · Speaker 3

of I P divided by

### 02:21:52 · Speaker 3

of diagonal elements of I P that's all. So whenever you get the pair of you get embeddings in such a way that the inner product between the image and the corresponding text is maximized and everything else is minimized. You need zeros here you need maximum values here that is how we are training it.

### 02:22:12 · Speaker 3

So finally after you try this what you can do is you take the

### 02:22:18 · Speaker 3

image. Okay? And what do you get? What do we need? We we we need a an embedding, right? Corresponding to a

### 02:22:29 · Speaker 3

a pair of text and image. That is how we have done it. Isn't it? Now, when we want to do uh uh let's say

### 02:22:41 · Speaker 3

prediction, what do we do?

### 02:22:43 · Speaker 3

we take an image and give it to the uh image encoder, we get the image embedding, okay? Then what you do is you take

### 02:22:54 · Speaker 3

any possible candidate text, pass it through the text encoder and get the text embedding. And you take the inner product of all those text embeddings with the image embedding and see which one fires and that is the caption corresponding to that particular image and that's how you do zero short prediction.

### 02:23:12 · Speaker 3

Right? But you as you can see all this is actually noise contrast estimation, isn't it? Different ways of doing noise contrast estimation. So I encourage you to look at all of these, okay? I mean, SimCLR we looked at. JEPA I will just talk about it in a while because I've asked you to implement this. uh BERT we will cover it in the next class. Wave to wake for speech is against what they do is detect the speech signal, uh mask it and create the positive and negative examples and

### 02:23:42 · Speaker 3

and solve a contrastable learning task and get the representations. In fact, I was working with like one of these like insurance brokers, I mean there is this company called Policy Bazaar, right? I was solving a research problem for them. So they were building automatic speech recognition systems for their customer care customer centers, call centers. So they had built a supervised ASR. So

### 02:24:12 · Speaker 3

when we tried wave to wave kind of approaches, okay? what happened was their dependence on supervised data came down by eighty five percent.

### 02:24:22 · Speaker 3

they could achieve the same performance on ASR by using only twenty percent of the supervised data. So these are very very powerful methods, the contrast learning methods, okay?

### 02:24:33 · Speaker 3

Fine. Now the last thing that I wanted to talk about is this joint extraction of

### 02:24:45 · Speaker 2

This is one thing that this guy Yan Likun keeps talking about everywhere, no?

### 02:24:56 · Speaker 1

It's called

### 02:24:59 · Speaker 1

joint embedding predictive architecture

### 02:25:18 · Speaker 1

What they do here is they

### 02:25:22 · Speaker 1

avoid

### 02:25:25 · Speaker 2

the need for negative samples, okay?

### 02:25:34 · Speaker 2

What they do is the following. They take an image,

### 02:25:37 · Speaker 3

okay? And by the way they use what is called as a uh vision transformer as the backbone model.

### 02:25:50 · Speaker 3

So I will teach transformers in the next class, then I will talk about vision transformers. Now the idea is suppose you have an image like this. Okay? What they do is they take random patches.

### 02:26:03 · Speaker 3

cut out some random patches from this image and call those patches as target patches.

### 02:26:13 · Speaker 3

Okay? And all the other patches which are here

### 02:26:20 · Speaker 3

they create some other patches from the region that is outside of the target patches and call them

### 02:26:25 · Speaker 2

context patches.

### 02:26:31 · Speaker 1

Okay, the task

### 02:26:35 · Speaker 1

is to predict

### 02:26:39 · Speaker 1

the target patches.

### 02:26:46 · Speaker 1

given the context patches as input. That's all.

### 02:26:58 · Speaker 3

That's all this JPA does. Okay? And they claim that if you do this then the the performance that we get is is much much better than most of the existing contrastive learning methods. Let me just show you that.

### 02:27:17 · Speaker 3

This is what I have asked you to implement, okay? So, when you don't have to do it using vision transformers, you can actually do it using CNN. Do you see this uh figure now, my screen and figure three?

### 02:27:33 · Speaker 3

Can you confirm if you see my screen?

### 02:27:35 · Speaker 4

No sir, not visible.

### 02:27:36 · Speaker 3

Receive

### 02:27:44 · Speaker 3

Yeah, I will take questions in a while.

### 02:27:47 · Speaker 3

Now do you see the screen?

### 02:27:51 · Speaker 4

Yes

### 02:27:53 · Speaker 3

Yeah

### 02:27:54 · Speaker 3

This is what they do, right? They taken, they give an image, given an image. They divide the image into non-overlapping patches or yeah, non-overlapping patches and they randomly take some patches as target patches, okay? And then take some other patches as context patches. Now the task is that if you are given context patches, they have two encoders, one they call as context encoder and target encoder which share the weights. Now given the next batches, the task is to predict the target batches.

### 02:28:31 · Speaker 3

Hello

### 02:28:33 · Speaker 3

So that's why they call it as the predictive architecture. So what is to be done? Yeah, so the image based joint embedding predictive architecture uses a single context block to predict representations of various target blocks originating from the same image. Of course, they don't predict the target patch image at the image level, they do it at the represent I mean the embedding level. Okay. What's interesting is that all they use is a

### 02:29:03 · Speaker 3

squared error loss between the uh true target and the predicted target that's all. extremely easy to implement. look at this figure. So the original image you have this context and multiple targets. What they do is they give the context image as an input to a V I T for the context encoder and they want to predict the embeddings corresponding to the target uh patches and they simply use an M S E between the predicted target predicted target embedding and

### 02:29:35 · Speaker 2

the true target embedding

### 02:29:46 · Speaker 2

is it all right?

### 02:29:47 · Speaker 3

See, it actually makes a lot of sense intuitively, you know. See, it's like, suppose I give you this image, okay? And ask you to predict this. You are implicitly learning how to complete this dog phase, isn't it?

### 02:30:03 · Speaker 3

Do you get what I'm trying to say?

### 02:30:06 · Speaker 3

Right? So that's why they say that this thing will learn implicitly the the representations uh that correspond to the underlying data set. Of course, as I said, the the base for all this uh lies in noise contrast estimation.

### 02:30:50 · Speaker 1

Okay, questions. It's, yeah, Sarvesh.

### 02:30:56 · Speaker 4

in the assignment we are asked to implement I J E P G so it is a typo right

### 02:31:02 · Speaker 3

I J E

### 02:31:04 · Speaker 4

P.G.

### 02:31:05 · Speaker 1

acid

### 02:31:05 · Speaker 2

Seventy-six

### 02:31:06 · Speaker 3

Yeah

### 02:31:07 · Speaker 1

Of course, yeah.

### 02:31:14 · Speaker 1

Yeah

### 02:31:15 · Speaker 3

Aditya

### 02:31:18 · Speaker 5

So when choosing the patches they are completely random or there is some

### 02:31:23 · Speaker 3

They are random. They are random.

### 02:31:24 · Speaker 5

Absolutely random

### 02:31:25 · Speaker 3

they are random but what they do no they will ensure that the patches for the context and the target are non overlapping.

### 02:31:26 · Speaker 5

done

### 02:31:32 · Speaker 5

Okay. And sir, what percentage should be context and what percentage should be target?

### 02:31:39 · Speaker 3

Yeah. Yeah.

### 02:31:41 · Speaker 5

Choose their

### 02:31:41 · Speaker 3

choosing an energy. See that they have that that that is a that is actually a hyperparameter, okay? And they have experimented with multiple of them.

### 02:31:49 · Speaker 1

Okay. Thank you, sir.

### 02:31:59 · Speaker 2

uh

### 02:32:00 · Speaker 3

Vivek

### 02:32:02 · Speaker 4

So in the IJP net I mean method, what how does the decoder and encoder look like? Like what technique is

### 02:32:11 · Speaker 3

There is no decoder, no?

### 02:32:17 · Speaker 3

there is no decoder. There are two encoders, one is the context encoder, the other is called the target encoder.

### 02:32:18 · Speaker 4

Nobody

### 02:32:24 · Speaker 4

then what are we learning there? I mean what is learnt? Is it a network?

### 02:32:29 · Speaker 3

the network, no? The encoder. That is an NF theta network that would take a pair of, I mean that would take a patch as an input and gives you some vector as an output.

### 02:32:39 · Speaker 4

Okay

### 02:32:42 · Speaker 4

ओके, ओके, ओके, फाइन, फाइन, फाइन। फाइन, ओनली, ओके, सो इट्स नॉट जेनरेटिंग एनीथिंग।

### 02:32:47 · Speaker 3

It is not generating anything. No no no. Okay.

### 02:32:47 · Speaker 4

It is not generating anything. No no no.

### 02:32:50 · Speaker 4

Okay, fine

### 02:32:52 · Speaker 4

Sarina

### 02:32:53 · Speaker 5

Leg

### 02:32:53 · Speaker 4

you can you can

### 02:32:53 · Speaker 3

you can you can say that there is also a a predictor right what which will do is that it will take the see what they use for f theta is a is a vision transformer. So this transformer would give you the embeddings okay. They also have a predictor network that would take these embeddings right from the true target patch and predict the yeah.

### 02:33:10 · Speaker 4

they also

### 02:33:15 · Speaker 4

Okay

### 02:33:18 · Speaker 4

Ree

### 02:33:22 · Speaker 4

okay, predict the, I mean the entire image with the with the field in

### 02:33:27 · Speaker 3

Not the image, not the image. It will predict the, uh it will take as input the the embedding corresponding to the context. Yeah, embeddings of the context is taken as input and it will predict the embeddings of the target.

### 02:33:33 · Speaker 4

Responding

### 02:33:38 · Speaker 4

predict

### 02:33:41 · Speaker 4

ओके, विदाउट एवर हैविंग टू जनरेट एनीथिंग, इट कैन डायरेक्ट देयर इज नो जनरेशन, देयर इज नो जनरेशन। ओके, ओके, ओके।

### 02:33:44 · Speaker 3

There is no generation. There is no generation. Okay, okay, okay. So there are two encoders basically. Let me just show you the figure again. Hold on.

### 02:33:58 · Speaker 3

Is my screen visible?

### 02:34:01 · Speaker 4

Yes

### 02:34:02 · Speaker 3

See, there are two encoders. One is called the context encoder and the target encoder, okay? Okay. So what it will give is this context encoder will give you a vector. Target encoder will give you another vector, right?

### 02:34:07 · Speaker 4

Okay

### 02:34:12 · Speaker 4

coder

### 02:34:14 · Speaker 4

Right. Yes.

### 02:34:14 · Speaker 3

Now what would this there is another network called the predictor network. What would this predictor network do? It will take the embedding corresponding to the context encoder.

### 02:34:27 · Speaker 3

Right? And

### 02:34:28 · Speaker 4

Cooking

### 02:34:29 · Speaker 3

and predict the the target the embeddings of the target encoder.

### 02:34:34 · Speaker 4

या एम्बेडिंग्स ऑफ द टारगेट या ओके। एम्बेडिंग्स ऑफ द टारगेट।

### 02:34:35 · Speaker 3

embeddings of the target encoder and the loss for this G, right? So basically how does the loss go? So there are two networks like this, F theta and F theta cap. Both of these are vision transformers. The context network will take some patches from the context. Contact, it will take context patches. Target encoder will take target patches. So you get two embeddings, right? Corresponding to target and the context. Now you take a predictor network that would take as input the encodings embedding.

### 02:34:56 · Speaker 4

Pondy

### 02:35:05 · Speaker 3

correspond, I mean output of the context encoder, okay? and predicts the output of the target encoder.

### 02:35:12 · Speaker 4

Okay

### 02:35:14 · Speaker 4

Yeah

### 02:35:14 · Speaker 3

Yeah, clear.

### 02:35:16 · Speaker 4

Yes, yes, thank you.

### 02:35:17 · Speaker 3

there's an L two loss between them. That's what you need to implement. As I said, no, for for your implementation purposes, uh you can either use a uh a vision transformer here if you if you can. Otherwise, you can use a simple C N N also here, no problem.

### 02:35:33 · Speaker 5

Okay. So do we need two networks here to be trained separately?

### 02:35:38 · Speaker 3

uh I mean what is done in practice is that they take uh you actually need two networks but you can share the weights between them. You need one network for target encoding the other for the context encoding.

### 02:35:57 · Speaker 3

Okay, so great, I think we have took a lot more time than usual. Okay, so that's it for today. uh We will reconvene again next week.

### 02:36:07 · Speaker 4

सर वन क्वेश्चन

### 02:36:08 · Speaker 3

question

### 02:36:09 · Speaker 3

Yeah

### 02:36:10 · Speaker 4

In question number nine, it says distilled the above resonate on a small sized MLP.

### 02:36:15 · Speaker 3

Correct

### 02:36:15 · Speaker 4

What do we mean by distilling it?

### 02:36:18 · Speaker 3

Yeah. Not taught you distillation, right?

### 02:36:22 · Speaker 3

Hmm

### 02:36:25 · Speaker 3

Oh

### 02:36:28 · Speaker 4

So take a smaller network and show it a lot of No no no I have to

### 02:36:31 · Speaker 3

No no no I have to I have to teach distillation. Let me do it next week if I do it next week then I have to extend the assignment deadline for one more week.

### 02:36:33 · Speaker 4

Teach

### 02:36:34 · Speaker 4

Thank you

### 02:36:43 · Speaker 3

This is a small topic that I wanted to, Sir, that should be helpful.

### 02:36:45 · Speaker 4

सर दैट शुड बी हेल्पफुल सर

### 02:36:48 · Speaker 3

Hmm

### 02:36:49 · Speaker 4

That should be helpful

### 02:36:52 · Speaker 3

I will do that

### 02:36:52 · Speaker 5

But sir it will end in our exam time

### 02:36:59 · Speaker 3

meaning the assignment deadline you are saying.

### 02:37:02 · Speaker 5

Correct

### 02:37:03 · Speaker 3

That's okay no? I mean I'll just give you maybe one more week.

### 02:37:07 · Speaker 3

Till 30th

### 02:37:09 · Speaker 5

Yes sir, Yes sir, It's okay.

### 02:37:15 · Speaker 3

thirty eight should be okay no? let me do it right away. so that

### 02:37:19 · Speaker 0

Yes sir

### 02:37:22 · Speaker 3

assignments

### 02:37:26 · Speaker 3

Because anyway I'm grading it on like the first week, right? So, three edit.

### 02:37:34 · Speaker 3

please remind me next class I need to teach distillation I complete it completely went off my head.

### 02:37:40 · Speaker 0

when you need to buy the

### 02:37:40 · Speaker 3

when you need to

### 02:37:43 · Speaker 3

First week of December

### 02:37:44 · Speaker 0

Okay

### 02:37:46 · Speaker 5

so that means

### 02:37:46 · Speaker 3

General question

### 02:37:48 · Speaker 3

Yeah

### 02:37:50 · Speaker 5

You said you worked on a solution with Policybazaar. So when you work a solution like this, do you drive
