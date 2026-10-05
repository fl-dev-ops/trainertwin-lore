---
id: _QCsp4ZdKLU
title: Lec 6 - Deep Generative Models GAN variants and Applications
date: '2024-11-23'
url: https://www.youtube.com/watch?v=_QCsp4ZdKLU
description: ''
author: prathoshap5226
duration: 02:40:23
model: saaras:v3
transcript: true
---

# Lec 6 - Deep Generative Models GAN variants and Applications

## Transcript

### 00:00:02 · Speaker 5

is given by root of alpha t x t minus one plus one minus alpha t times epsilon where epsilon is a sample drawn from normal zero one. And this defines a first order Markov chain is what we saw. So starting from a data point you keep projecting it on to the latent space. According to

### 00:00:20 · Speaker 4

into this equation, this particular equation.

### 00:00:28 · Speaker 4

this particular equation and that will quote unquote add noise, right?

### 00:00:33 · Speaker 5

is adding noise and slowly because it's a Markov chain stationary distribution will go to

### 00:00:42 · Speaker 5

normal zero one is what we saw. Okay.

### 00:00:45 · Speaker 5

Now, uh this encoding enforces a distribution

### 00:00:51 · Speaker 5

on the t-th latent space conditioned on t minus first latent space which happens to be a Gaussian with certain parameters mean and variance that is written here.

### 00:01:03 · Speaker 5

And the corresponding decoding distribution is what we call as the model distribution, it is learnable. Okay? What you learn is that you learn the decoding distribution, the mean and the variance of the decoding distribution at all time steps T. Now, as we saw later in the in in in the lecture, that the variance is actually often not learned, that is also assumed to be fixed or known. What is learned learned is the mean of the decoding distribution. Okay?

### 00:01:33 · Speaker 5

how do we do that? we do that using the usual elbow optimization. so for that we started from the log like we wrote down the elbow and uh yeah, did some algebraic manipulations, right?

### 00:01:51 · Speaker 5

And finally, uh what we got was that there were three terms in the elbow. One we called as the reconstructed term where you take the uh

### 00:02:04 · Speaker 5

First Latent Variable

### 00:02:05 · Speaker 4

I mean

### 00:02:06 · Speaker 5

and try to reconstruct the data. And the second term is prior matching term, okay, which was independent of model parameters theta, okay. And the third term is what we called as the

### 00:02:20 · Speaker 5

consistency term or denosing matching term, okay? That is what we called as the

### 00:02:27 · Speaker 5

consistency term

### 00:02:30 · Speaker 5

that involved KL divergence, computing KL divergence between two distributions.

### 00:02:35 · Speaker 5

one was this Q X T minus one given X T and X not and the model decoding term P theta X T minus one given X T. So note that in the denosing matching term or consistency term right there are two distributions one is the decoding distribution the other is is a sort of reverse of the encoding distribution. reverse in the sense that it is it's going in the backward direction of X T minus one

### 00:03:05 · Speaker 5

given XT and X not but yeah so that is known okay but has to be computed it is not trivially known we have to compute that distribution so what we did was we wanted to compute that

### 00:03:21 · Speaker 5

consistency term. For that we need to compute the known reverse distribution that appears in the consistency term and we use Bayes' law, right? And the fact that all of the involved distributions are Gaussian distributions, completed square and finally we, yeah, so two things, one in the while we are computing the

### 00:03:48 · Speaker 5

known term, okay, known denosing term in the consistency loss component.

### 00:03:56 · Speaker 5

we encounter terms like Q of X T given X not, right? Where uh where X T is the Tth latent vector and X not is the data. So now we use recursion to find this Q of X T given X not, right? Uh using this argument and finally Q of X T uh given X not still happen to be a Gaussian with parameters denoted by alpha bar X not and yeah, parameter as per

### 00:04:26 · Speaker 5

alpha bar x bar where alpha bar is the one that is defined here which is a product of multiple all the

### 00:04:31 · Speaker 0

Alphas till the time T

### 00:04:44 · Speaker 0

Okay. So using that

### 00:04:46 · Speaker 5

and the fact that all of them that are involved are Gaussian distributions completed the square and finally found out what this the known denosing matching term was, right? And we called we called that as a Gaussian distribution, we found out that it was a Gaussian distribution two with a mean denoted by this mu Q and the variance denoted by sigma Q, okay? And the sigma Q

### 00:05:16 · Speaker 5

simply a function of T, okay? that had nothing to do with any parameters. It was a function of T and we wrote that as small sigma Q squared T times identity and mu Q was a function of XT and X not, okay? which can be computed, which which is known and can be

### 00:05:40 · Speaker 0

computed. Okay. Now having

### 00:05:50 · Speaker 0

P theta. Okay. We have to we can now finally compute the uh denosing matching term or consistency term which is the KL divergence between two positive distributions. Okay.

### 00:06:12 · Speaker 0

Now, the KL divergence between

### 00:06:14 · Speaker 5

between two Gaussian distributions as a deterministic form, okay? We use that deterministic form which is KL divergence between two Gaussian distributions and finally found out that the de Noygin matching term will involve difference computing difference between two means, okay? One which is the mean of the

### 00:06:38 · Speaker 5

backward of the decoding distribution mu theta at x t and the other term was the mean of this known denosing term okay mu q computed at x t.

### 00:06:52 · Speaker 0

That's what we saw. Any questions on this so far?

### 00:07:05 · Speaker 0

Hope I am audible

### 00:07:11 · Speaker 0

Yes sir, Podium

### 00:07:16 · Speaker 4

Okay. So then

### 00:07:18 · Speaker 5

what we did was while we can actually stop here, okay? uh and uh and we can implement uh D D P M this way, as I said, no? uh in the literature, people don't uh use this formulation to implement, but they rather reparameterize the uh reparameterize this particular uh thing uh using

### 00:07:44 · Speaker 5

in terms of the epsilon of the noise that is added, okay, that is what is implemented. So we saw that re-parameterization as well. So maybe I will do it again.

### 00:07:56 · Speaker 5

do it in the last class, no? Let me do it again, right? So we'll I'll assume that we know that the elbow now has a difference between the means of mu Q, means means mu Q and

### 00:08:12 · Speaker 0

μθ, okay, let us

### 00:08:15 · Speaker 0

take it from there and do it a

### 00:08:54 · Speaker 0

Sure. Okay. Now,

### 00:10:03 · Speaker 0

Hello

### 00:10:07 · Speaker 4

Yeah

### 00:10:12 · Speaker 0

Sir, are you waiting?

### 00:10:24 · Speaker 0

So we have

### 00:10:29 · Speaker 0

Rosa killed

### 00:10:39 · Speaker 0

Q

### 00:10:42 · Speaker 0

of XT minus one

### 00:10:45 · Speaker 4

given x t and x not

### 00:10:49 · Speaker 4

one distribution the other

### 00:10:51 · Speaker 5

distribution was E theta

### 00:10:55 · Speaker 5

xt minus one given xt

### 00:10:59 · Speaker 4

Yeah, this was what it was and we showed that that Q of

### 00:11:07 · Speaker 4

sixty minus one given

### 00:11:10 · Speaker 4

next year, next month.

### 00:11:13 · Speaker 4

Boss

### 00:11:17 · Speaker 4

a Gaussian distribution

### 00:11:23 · Speaker 4

the mean we called as mu Q. And the variance was sigma Q. Right? And mu Q

### 00:11:35 · Speaker 4

was a function of X T

### 00:11:37 · Speaker 5

and X not

### 00:11:39 · Speaker 4

So given an XT and

### 00:11:40 · Speaker 0

x naught you had this mean to be equal to

### 00:11:47 · Speaker 0

Root of

### 00:11:54 · Speaker 0

alpha t into 1 minus alpha

### 00:11:58 · Speaker 4

bar times XT plus

### 00:12:04 · Speaker 4

root of alpha t minus one bar

### 00:12:10 · Speaker 4

into one minus

### 00:12:12 · Speaker 4

alpha t into x dot

### 00:12:17 · Speaker 4

divided by

### 00:12:21 · Speaker 4

one minus

### 00:12:24 · Speaker 5

alpha t bar. See note that the denominator is actually a constant and it's a scaling factor. So basically it's a linear combination of x t and x naught. That is what this new Q is, right?

### 00:12:36 · Speaker 5

So now okay. Now if you recall, uh using a recursion we showed that the tth latent variable X T, okay, can be represented in terms of

### 00:12:50 · Speaker 5

Alpha T bar, okay?

### 00:12:55 · Speaker 4

presented in terms of x naught, right? alpha t bar into

### 00:13:01 · Speaker 4

not plus

### 00:13:05 · Speaker 4

root of 1 minus

### 00:13:07 · Speaker 5

Hello

### 00:13:08 · Speaker 5

Alpha T bar into Epsilon

### 00:13:13 · Speaker 5

Do you remember this? So we used recursion and showed that uh X T can be showed uh in terms of uh X naught and the noise added epsilon, correct?

### 00:13:27 · Speaker 5

So this implies

### 00:13:29 · Speaker 5

that now mu Q

### 00:13:32 · Speaker 5

Okay.

### 00:13:33 · Speaker 4

your screen is stuck. It's lagging I guess.

### 00:13:41 · Speaker 5

cool down see let me do one thing let me just

### 00:13:46 · Speaker 5

ಯೂಸ್ ಮಾಡ್

### 00:13:47 · Speaker 0

my phone internet to connect. I think that should be better. Give me a second.

### 00:16:04 · Speaker 0

Do you see the screen now?

### 00:16:11 · Speaker 3

No, sir

### 00:16:12 · Speaker 4

Okay

### 00:16:17 · Speaker 0

hmm

### 00:16:19 · Speaker 0

what's happening.

### 00:16:22 · Speaker 0

I just changed my internet to my phone internet.

### 00:18:14 · Speaker 4

Please tell me if you can see the screen

### 00:18:17 · Speaker 4

never you can

### 00:18:21 · Speaker 0

Yes sir

### 00:18:23 · Speaker 0

is visible? Yes.

### 00:18:24 · Speaker 4

Yes, okay.

### 00:18:25 · Speaker 0

it works

### 00:18:36 · Speaker 4

sorry about this as I said I've come to my hometown and

### 00:18:41 · Speaker 4

internet is not my standard one.

### 00:18:45 · Speaker 4

So

### 00:18:47 · Speaker 4

some issues.

### 00:18:49 · Speaker 5

तो

### 00:18:52 · Speaker 5

what we were doing is that expressing this new Q, okay, in terms of

### 00:19:01 · Speaker 5

x naught and epsilon, right? This mu q now can be expressed in terms of x naught and epsilon. Okay, so this is the recursion that we wrote. Sorry, x t is expressed in terms of x naught and epsilon. It means that I can write my mu q now.

### 00:19:20 · Speaker 5

in terms of this. So I'll write this as root of alpha t

### 00:19:26 · Speaker 0

into one minus

### 00:19:30 · Speaker 0

or t bar times x t

### 00:19:39 · Speaker 0

Plus

### 00:19:42 · Speaker 0

root of alpha t minus

### 00:19:44 · Speaker 5

plus one bar

### 00:19:46 · Speaker 5

into one minus alpha t. Okay. Now, this implies that here I can write x not

### 00:19:55 · Speaker 5

okay? in terms of x t and epsilon, right? x t minus root of one minus alpha t bar times epsilon divided by

### 00:20:08 · Speaker 5

alpha root of alpha t bar, right? So, which means that this x naught which is there in mu q, I can replace that with

### 00:20:17 · Speaker 5

this thing now x t minus root of one minus alpha t bar into epsilon divided by root of alpha t bar right. this entire thing divided by

### 00:20:32 · Speaker 5

one minus alpha t bar

### 00:20:35 · Speaker 5

Right. So I can I mean what did I just do? X T can be reparameterized in terms of X not and epsilon, which means that X not can be written in terms of X T and epsilon. So mu Q now, uh the X not in mu Q now can be written in terms of X T. That is what was done. So I will skip the algebra. If you uh rearrange the terms and group them and modify, what will happen is finally the mu

### 00:21:05 · Speaker 0

Q

### 00:21:12 · Speaker 0

can be expressed

### 00:21:17 · Speaker 0

one by

### 00:21:20 · Speaker 0

root over alpha t

### 00:21:23 · Speaker 0

into XT

### 00:21:24 · Speaker 5

Please

### 00:21:25 · Speaker 0

Hello

### 00:21:25 · Speaker 5

minus

### 00:21:27 · Speaker 5

1 minus alpha t divided by

### 00:21:31 · Speaker 4

Hello

### 00:21:31 · Speaker 5

root of 1 minus alpha t bar

### 00:21:36 · Speaker 5

into root of alpha t.

### 00:21:39 · Speaker 4

times

### 00:21:43 · Speaker 0

Okay? Yeah, so this is simply by rearranging the terms above.

### 00:22:04 · Speaker 0

Okay. That should be okay, right? I mean, what we did was the

### 00:22:12 · Speaker 5

mu q was written in terms of

### 00:22:16 · Speaker 5

xt and epsilon. Is that all right?

### 00:22:20 · Speaker 4

Okay

### 00:22:21 · Speaker 5

Now recall that the

### 00:22:27 · Speaker 5

p theta of x t minus 1

### 00:22:31 · Speaker 5

even X T, the one that we had,

### 00:22:35 · Speaker 5

What was that? We assumed that to be a Gaussian.

### 00:22:40 · Speaker 5

with a mean mu theta and variance was exactly equal to sigma q right we didn't want to change the variance the mean was mu theta right

### 00:22:53 · Speaker 0

Right? Now, this mu theta now,

### 00:22:59 · Speaker 0

can be expressed as follows

### 00:23:19 · Speaker 0

minus forty divided by one minus

### 00:23:25 · Speaker 0

40 bar

### 00:23:30 · Speaker 4

into some epsilon theta cap

### 00:23:35 · Speaker 5

Okay. So now this is something which is subtle. If you understand this then we are done. Okay. So what did we do? We express the mean, okay, of the decoding distribution.

### 00:23:49 · Speaker 5

in terms of XT and some epsilon theta cap, okay?

### 00:23:54 · Speaker 0

Hello

### 00:23:55 · Speaker 5

that is to be learned we will

### 00:23:56 · Speaker 0

say that is epsilon theta cap

### 00:24:08 · Speaker 0

this

### 00:24:11 · Speaker 0

Okay.

### 00:24:13 · Speaker 0

Okay. So what did we

### 00:24:15 · Speaker 5

to here

### 00:24:17 · Speaker 5

you know that uh any Gaussian distribution, right? uh can be expressed in terms of any other Gaussian distribution just by scaling and shifting, correct? Do you do you agree with me on that?

### 00:24:36 · Speaker 5

that is reparameterization, right? So if you if you are given a particular Gaussian distribution, you can always scale and a sample from a particular Gaussian distribution, you can always scale and shift the sample of that particular Gaussian distribution to make it into

### 00:24:52 · Speaker 0

any other Gaussian distribution. Do you agree?

### 00:25:05 · Speaker 0

Hello, am I audible?

### 00:25:09 · Speaker 0

Yes sir

### 00:25:09 · Speaker 4

Yes, Yes, you wrote

### 00:25:10 · Speaker 2

audible yes yeah

### 00:25:11 · Speaker 5

So you agree with what the statement that I made, right? Any Gaussian distribution can be expressed in terms of any other Gaussian distribution. Now, this P theta of X T minus one given X T is a Gaussian distribution with a certain mean, mu theta, okay? Now, what we did was we just represented that mean in terms of X T, right, which is a constant, right? And some sample from a Gaussian distribution, epsilon theta cap with some scale.

### 00:25:14 · Speaker 2

Yes, yes, yes.

### 00:25:41 · Speaker 5

and shifts. Now, I can always find an epsilon theta, right?

### 00:25:49 · Speaker 5

which when scaled by this particular scaling factor and shifted by one by one by root of alpha theta times x t will give back my mu theta. Do you agree? So what I'm trying to say is if you scale and shift a particular Gaussian distribution, right? You can always learn the scale and shift factor so that you can get back to the original Gaussian distribution.

### 00:26:14 · Speaker 4

Is that, Is that alright?

### 00:26:22 · Speaker 0

Yes sir

### 00:26:23 · Speaker 4

Pay

### 00:26:24 · Speaker 5

So why I mean then the next question is why did we even have to like introduce these random scale chips? It is just to make the loss function look nice that's all.

### 00:26:34 · Speaker 5

Okay, so there is in fact, you know, I can just write this as mu theta and mu q minus mu theta can be written as this this entire mu q that we have minus mu theta, right? It doesn't matter. But people generally write it this way to ensure that the final loss function that you see has a nicer form to see, that's all. There is no other sanctity to this, huh? And what I'm simply doing is,

### 00:27:00 · Speaker 5

I mean deliberating all the learnable things on a scale and shifting to this epsilon theta, that's all, okay? So with this what will happen is the the laws that we had, no, the KL divergence between

### 00:27:15 · Speaker 5

Q of X T minus one

### 00:27:19 · Speaker 5

even

### 00:27:19 · Speaker 4

and it's not

### 00:27:23 · Speaker 4

and P theta of

### 00:27:27 · Speaker 4

xt minus one given xt

### 00:27:31 · Speaker 5

simply became

### 00:27:34 · Speaker 5

Let me just write proportional to because generally the constants are ignored. It became proportional to. This was initially uh we had a sum here. From T equal to two to capital T.

### 00:27:49 · Speaker 5

mu q which was a function of x t and x not and there was mu theta

### 00:27:56 · Speaker 5

which is a function of

### 00:28:01 · Speaker 5

60 and T

### 00:28:04 · Speaker 5

T because there is an alpha T there.

### 00:28:06 · Speaker 4

okay, this is what the last term was, and this we saw was now equivalent to

### 00:28:19 · Speaker 4

all terms being equal, let's

### 00:28:20 · Speaker 5

call this as epsilon t, okay, I think this is better to

### 00:28:24 · Speaker 5

right this has epsilon T. because the Tth sample right I mean Tth noise sample that was drawn to make X not X T.

### 00:28:35 · Speaker 5

easier to understand. Okay.

### 00:28:38 · Speaker 4

and you have

### 00:28:43 · Speaker 4

Epsilon Theta

### 00:28:46 · Speaker 4

cap

### 00:28:48 · Speaker 5

just to make it look this elegant, no? This mu q, sorry, mu theta was reparameterized in terms of x t and those constants. Finally, this is what it turned out to be.

### 00:29:03 · Speaker 5

Is this all right? So when you are implementing a diffusion model, right, a D D P M, all you have to do is implement this loss function. So this becomes a regression problem, right? So this is a regression over epsilon T. Let me explain that more.

### 00:29:22 · Speaker 4

regression over epsilon t. Okay. Any questions so far? How did we get there? Get here?

### 00:29:29 · Speaker 0

before I move to the implementation nuances.

### 00:29:42 · Speaker 0

Hello, am I audible? Any questions here?

### 00:29:53 · Speaker 5

Are you there? Am I audible?

### 00:29:57 · Speaker 4

Yes sir, you are audible, Yes, we are hearing you.

### 00:29:58 · Speaker 0

your audible

### 00:30:00 · Speaker 5

no questions. Okay. Right. Okay. So this is what it becomes. So now the next thing is how do we implement this in practice?

### 00:30:08 · Speaker 0

this

### 00:30:12 · Speaker 0

implementation

### 00:30:22 · Speaker 0

So it's basically training of D D P M.

### 00:30:35 · Speaker 0

Okay. So now what are we given? So given, I will show it for one data sample, no? You have to do it again in batch. Given it's not, it is a sample from D data distribution.

### 00:30:55 · Speaker 0

from the true statistics equation.

### 00:31:03 · Speaker 0

Okay, what is to be done is that

### 00:31:08 · Speaker 0

paint

### 00:31:10 · Speaker 4

So first what you do is uh

### 00:31:16 · Speaker 4

sample

### 00:31:16 · Speaker 5

Hello

### 00:31:19 · Speaker 5

T, okay? uniformly between two and capital T. So what is done in practice is the sum that you see here, no, from T equal to two to capital T, people don't do it on like all T's and take a sum of it. They do a uniform sampling of some some subset of T between two and T and then do it, okay? So typically it's not they don't take all T's because of computational. complexity, some T is taken, okay? Sample T uniformly between two and capital T, okay? And you obtain

### 00:32:00 · Speaker 5

XT, okay.

### 00:32:03 · Speaker 4

First

### 00:32:05 · Speaker 4

And if you also have the alpha one

### 00:32:11 · Speaker 4

Set

### 00:32:15 · Speaker 4

Set Alpha One

### 00:32:17 · Speaker 5

for two up to alpha capital T, okay? So you fix this. So typically it is fixed at uh the schedule that

### 00:32:30 · Speaker 5

zero point nine eight and so on zero point nine okay. uh this is again this is an example but yeah so you should set alphas this way. and you obtain x t uh using this equation right square root of alpha t bar times x not plus one minus alpha t bar into some epsilon t where epsilon t is a sample from normal zero but

### 00:32:59 · Speaker 5

with me so far. So given an x naught, so you have x naught is let's say that x naught is a particular image. You take an x naught. And you sample, uh sorry, you get some t, okay? Let's say that we are doing it for one particular t, okay? uh you take a t.

### 00:33:21 · Speaker 5

the bad cold. Okay, so you sample a T from two to capital T and you set alpha one to alpha capital T to be some constant. And you obtain X T using this equation where epsilon T is some sample from normal zero one. Is this all right so far?

### 00:33:45 · Speaker 0

Okay, so once you have this, what you do is the following, that you build, construct

### 00:33:56 · Speaker 0

instruct a neural network

### 00:34:02 · Speaker 0

Parametric

### 00:34:03 · Speaker 4

by theta, okay? So this neural network typically will have this architecture.

### 00:34:09 · Speaker 5

which is called the

### 00:34:13 · Speaker 5

Unit

### 00:34:17 · Speaker 5

Okay, so now it is called unit because note that finally what we need is a regression over epsilon theta cap

### 00:34:28 · Speaker 5

right? Because our last function is this, right? We want an estimate of epsilon T. Now, uh we know that the dimensionality

### 00:34:41 · Speaker 5

the dimensionality of epsilon T is actually D which is the data dimensionality. Okay. Now, uh when you have regression tasks, okay, uh where the output is same as that of the input and especially when you are using image kind of data, the standard architecture that is used is this sort of an architecture which is called unit. The name unit is given to this is because it looks like a U, right? H U I

### 00:35:15 · Speaker 5

you start from D dimensions, okay? Keep reducing the dimensions.

### 00:35:21 · Speaker 5

and then you come to some bottleneck D dash. and then you increase the dimensions and finally you get back to the D dimensions you know that's why the name unit. Okay? So now what does this take as an input? So you please note here that the new theta that we had in fact this epsilon

### 00:35:42 · Speaker 5

theta cap now will also become a function of x t, right? and t. obviously, right? because that is the scale and shift and that's what it the function of. new theta was a function of x t and t and when I just reparameterize that in terms of some epsilon theta cap, that also becomes a function of x t and t, right? So now this unit will take x t which we have obtained and t as an input, okay? and it is supposed

### 00:36:12 · Speaker 5

to uh output epsilon theta cap which is an estimate of epsilon t that we have used to get x t. What is the last function? The last function is simply the difference between note that both of them are vectors of size.

### 00:36:31 · Speaker 5

T

### 00:36:31 · Speaker 4

So you can easily compute this.

### 00:36:38 · Speaker 4

That's all. So this is the last

### 00:36:40 · Speaker 5

function, you need to compute the gradient of this with respect to theta and then back propagate. So, this is all it is, right? I mean, you do it for multiple t's.

### 00:36:52 · Speaker 5

Okay, in fact, I mean, ideally you should do it for T equal to two to capital T. uh Typically what is done is, I mean, T is fixed to some thousand, right? Thousand or two thousand is what is done. So instead of taking thousand XTs, uh people typically take some fifty uh XTs for a given X not. Okay? And then try it. And again for you take another sample X not, input sample X not, and you sample

### 00:37:19 · Speaker 1

some other subset of T

### 00:37:20 · Speaker 5

and do this

### 00:37:23 · Speaker 5

Now, how do you give T as an input to this unit is something that I'll talk about in a while. But yeah, so other than that is the training procedure for DDPM clear. See, one other thing that is to be noted is, uh unlike in VAEs and GANs, right, where

### 00:37:41 · Speaker 5

The final inference uh happens to be just a forward pass through the network that you have trained. Here...

### 00:37:50 · Speaker 5

Here, the inference is not through this network. We will see that in a while. See what I'm saying is, this network will not give you a new sample from the data distribution. You see that?

### 00:38:05 · Speaker 5

unlike in a GAN and a VAE where you just take a Z, right, and pass it through the decoder or the generator, you get a sample from the input distribution, right, a new sample from the input distribution that does not happen in a TDPM. So I will also talk about how to do inference in a TDPM in a while, but is the training procedure clear? This is what you are supposed to implement in your in your assignment. So let me know if this makes sense, otherwise I can explain more.

### 00:38:35 · Speaker 3

Uh, sir, when we are taking a X not, sorry, I have a question, sir. Can I wait?

### 00:38:46 · Speaker 3

Can I go ahead with the question?

### 00:38:48 · Speaker 4

प्लीज प्लीज या

### 00:38:50 · Speaker 3

So when we take a X not, the T for every X not, the T has to be a fixed length like the sample that we are taking.

### 00:39:01 · Speaker 5

what do you mean by that? See, uh you take one X not, right? One X, suppose you are doing this on some data set, right? Some image data set. X not is one sample from the data set, one image.

### 00:39:15 · Speaker 3

Yes

### 00:39:16 · Speaker 5

You take one image

### 00:39:18 · Speaker 5

for that one image you get all the noisy versions, no, latent versions, X one, X two, X three, X four and so on.

### 00:39:28 · Speaker 5

for each of them you do one one training through this unit.

### 00:39:38 · Speaker 0

Okay

### 00:39:40 · Speaker 2

is it one or more than one? for for a given data point.

### 00:39:47 · Speaker 5

see for a given data point x not you get one sorry for one x t you do one forward pass one backward pass

### 00:40:00 · Speaker 2

Okay, and T is we take multiple for a given X node.

### 00:40:04 · Speaker 5

because the last function has the sum across all t's, no?

### 00:40:09 · Speaker 2

Okay

### 00:40:10 · Speaker 2

Yeah, but here we we don't take all t's, but we take some samples from two to t.

### 00:40:15 · Speaker 5

practice yeah in practice capital T is see capital T is fixed at thousand okay but while training you do a random sampling uniform sampling between two and thousand and do it that is how it is done. This is for one X not and you need to do it for all data sets all data points no that will that will be one epoch. So typically what is done is you do it on batches you take a batch of X not.

### 00:40:40 · Speaker 4

in

### 00:40:41 · Speaker 5

Right? And for

### 00:40:43 · Speaker 4

in

### 00:40:44 · Speaker 5

Excuse me. So take a batch of X not and for each of the samples in X not, you do a sampling of certain T's, okay? And find those X T's and do a forward pass and a backward pass for this entire batch and you do another batch of samples, you take another batch of samples from the data set and iterating over the entire data set will give you one epoch and you do multiple epochs of training, usual training.

### 00:41:14 · Speaker 5

Is that all right?

### 00:41:14 · Speaker 2

And epsilon, epsilon t is just a sample from a normal zero I.

### 00:41:18 · Speaker 5

epsilon t is always a sample from normal zero one that's all so for when you obtain x t you take one sample from normal zero one see last class we saw that no it is simply one sample from normal zero one but the the the information about t is encoded in this alpha bar because alpha bar is product of all alphas from one to t isn't it you have to actually there is one other step here you have to compute alpha bar t right as the product of

### 00:41:50 · Speaker 5

इक्वल टू वन टू थ्री अल्फा आई दैट इज हाउ वी डिफाइन्ड अल्फा बार नो

### 00:41:55 · Speaker 2

For every t you have to define alpha bar this way and get an x t then pass it through the unit predict whatever

### 00:42:01 · Speaker 0

is coming, compute the loss, back propagate.

### 00:42:11 · Speaker 0

any other questions on training?

### 00:42:14 · Speaker 0

As I said, this is what you are supposed to implement, right? So,

### 00:42:28 · Speaker 0

Okay. If it's clear, then there is one other question.

### 00:42:32 · Speaker 4

that is to be answered is how do we give this time D right as an input to the

### 00:42:38 · Speaker 4

Right

### 00:42:38 · Speaker 0

the government has no hope

### 00:42:52 · Speaker 0

See, now this is a scalar, right?

### 00:42:59 · Speaker 0

input

### 00:43:07 · Speaker 0

Neural network, Okay.

### 00:43:12 · Speaker 0

Now what can be done is

### 00:43:13 · Speaker 5

Now note that T, right, is is one dimensional, it is scalar, right?

### 00:43:21 · Speaker 5

one dimensional scalar. So typically what happens is if you create an image X and concatenate the speed which is a scalar.

### 00:43:33 · Speaker 5

a one dimensional scalar with this P, what happens is the neural network will offer no logic to P. Because it's a unidimensional scalar, it will be simply ignored. So for that, uh what is done is one dimensional and

### 00:43:52 · Speaker 0

we usually ignore

### 00:44:00 · Speaker 0

if concatenated or when concatenated with a very high dimensional vector

### 00:44:16 · Speaker 0

syncretinated with a five-dimensional vector

### 00:44:27 · Speaker 0

So in this case this is X T which is an image right?

### 00:44:34 · Speaker 0

or some some data. Okay. So now for that what is done is

### 00:44:44 · Speaker 0

Oil

### 00:44:47 · Speaker 0

above scenario

### 00:44:55 · Speaker 0

Now the scalar

### 00:44:58 · Speaker 0

scalar T is converted into a vector.

### 00:45:09 · Speaker 0

Okay. P is converted into a vector and then concatenated.

### 00:45:20 · Speaker 0

Okay? So there's a name for this. Do you know what this is? This is called

### 00:45:29 · Speaker 0

position

### 00:45:29 · Speaker 4

embedding

### 00:45:32 · Speaker 5

this positional embedding it's a high sounding name it's nothing but converting this T which is a scalar right? into some vector okay so what is done is T is converted into some T cap where

### 00:45:51 · Speaker 5

T is a scalar, okay? Now T cap is in some D dimension. So that is what the idea of positional embedding is, right? P is a function that would take T and project it onto T cap. So how is it done? There are multiple ways. One usual way that is used both in the transformers and

### 00:46:16 · Speaker 5

diffusion model

### 00:46:17 · Speaker 3

situation

### 00:46:17 · Speaker 3

models is what is called as

### 00:46:19 · Speaker 0

the sinusoidal embedding

### 00:46:30 · Speaker 0

I will just give you the idea of

### 00:46:32 · Speaker 5

this you can go and look at the details on this is like lot of blocks etcetera it's not not at all difficult. What is done is uh construct sinusoids okay of multiple frequencies.

### 00:46:50 · Speaker 0

entire thing okay

### 00:46:55 · Speaker 0

The next one is let's say higher frequency.

### 00:47:01 · Speaker 0

you know

### 00:47:05 · Speaker 0

and so on, okay?

### 00:47:10 · Speaker 4

Okay. Now

### 00:47:13 · Speaker 5

Now this how many sinusoids are there? There are

### 00:47:20 · Speaker 5

D number of sinusoids, construct D number of sinusoids. And what you do is that at every

### 00:47:26 · Speaker 4

so this is the time access

### 00:47:36 · Speaker 4

the time answers. So at every T

### 00:47:39 · Speaker 5

just t equal to one, t equal to two, t equal to three and t equal to capital T. At every T, you just sample the value of the sinusoid at this particular value. That is all it is.

### 00:48:01 · Speaker 0

this is a t equal to one. a t equal to two. a t equal to three.

### 00:48:07 · Speaker 4

and so on

### 00:48:11 · Speaker 4

Do you see what is happening?

### 00:48:14 · Speaker 5

P cap

### 00:48:17 · Speaker 5

okay? At a particular T. So T cap at a particular T, okay? is a vector of dimensions D, okay? where every component is

### 00:48:32 · Speaker 5

Sign off

### 00:48:34 · Speaker 5

some fixed frequency. So you have a fixed frequency that's a function of

### 00:48:41 · Speaker 5

Okay. Let me just call this as two pi times

### 00:48:50 · Speaker 5

D

### 00:48:53 · Speaker 4

these which no. So let me call it as some

### 00:49:00 · Speaker 4

I

### 00:49:01 · Speaker 4

divided by D

### 00:49:06 · Speaker 4

Uh, like

### 00:49:11 · Speaker 4

and then

### 00:49:11 · Speaker 5

you have

### 00:49:14 · Speaker 5

second component is sine

### 00:49:18 · Speaker 5

two pi times two divided by t you have like sign

### 00:49:23 · Speaker 4

Hello

### 00:49:24 · Speaker 5

two pi

### 00:49:28 · Speaker 0

one two three

### 00:49:34 · Speaker 0

D by D

### 00:49:41 · Speaker 0

Right? So this is at

### 00:49:43 · Speaker 4

Okay, there should be a dependence on T also here. Yeah, dependence on T, okay.

### 00:49:53 · Speaker 0

just

### 00:49:53 · Speaker 4

is at a particular

### 00:49:55 · Speaker 4

I can put a T here also, yeah.

### 00:50:02 · Speaker 5

is it all right? I mean, do you get the idea what's happening?

### 00:50:06 · Speaker 5

So what is happening is for a given T, okay? So basically you want to convert a scalar into a vector. Like how do you do that? Is that you just take construct like D sinusoids. If you want to convert that into a D dimensional space, you construct D sinusoids, okay? And of different frequencies and at every T you take a snapshot of all the sinusoids. So you will get a D dimensional vector at every T. So Now you converted a scalar T into a vector T dimensional vector at all T's.

### 00:50:41 · Speaker 5

Is this all right?

### 00:50:44 · Speaker 2

So the frequencies have to be

### 00:50:44 · Speaker 5

sequences have to be come again

### 00:50:47 · Speaker 2

the frequencies have to be harmonics or it can be any frequency.

### 00:50:51 · Speaker 5

Yeah yeah generally they are taken to be harmonics. In fact I think I mean that's why you know I don't remember the exact details. I think in in in the typical sinusoidal embeddings what is done is for even t's I think they take a sinusoid and for odd t's they they take cosines I suppose. Right just to interspersed. There is a sine and a cosine and you convert it into a d-dimensional vector.

### 00:51:21 · Speaker 5

You can you can go and look at the exact like equations that are used no but this is the fundamental idea of what sinusoidal partial embedding does. Is this okay any questions?

### 00:51:36 · Speaker 6

we are defining that vector right it means like comma in between each sign right? just to

### 00:51:42 · Speaker 4

completely

### 00:51:44 · Speaker 5

sorry I missed it what did you say

### 00:51:47 · Speaker 6

Sir, we are defining T cap as a vector, right? So it's a sin two pi T by T comma, I mean like those are terms of that vector, right?

### 00:51:58 · Speaker 5

Yeah, yeah, yeah, these are different terms. Yeah, it's a vector, I just said it's space. These are different.

### 00:51:58 · Speaker 6

Research

### 00:52:06 · Speaker 6

Thank you sir

### 00:52:07 · Speaker 5

vector, yeah. See, look at this, this T cap is in D dimensions, right? I mean T is a scalar, T cap is in D dimensions.

### 00:52:16 · Speaker 5

So in a transformer also, right, all these GPT etcetera kind of models, when the tokens are given as input, these things are also concatenated because a naive transformer does not have the idea of time, right? So to ensure that the sequential nature of that is preserved, this is also given as an additional input. Same thing is done in this this thing also, right? When you implement, I mean there are standard implementations of sinusoidal positional embeddings in PyTorch. You just take that

### 00:52:46 · Speaker 5

and concatenate that in fact there is one other thing that is done. These are additional improvisations over the architecture that depends on oh my god what happened.

### 00:53:01 · Speaker 0

some stupid thing.

### 00:53:10 · Speaker 0

Yeah, so some of the improvisation

### 00:53:11 · Speaker 5

organizations are done over this where, uh what is done right? Instead of concatenating this T here, there are, I mean, this unit typically will have this thing called skipped connections, okay?

### 00:53:27 · Speaker 5

where what is done is, uh there are connections of this sort where you take the the uh intermediate hidden layer and connect it to the corresponding uh layer at the reflection. I mean it actually looks like a reflection, right, along this. So so you connect the corresponding dimensions using a skip connection just as you do in do with resnet, okay? Now what is done is, that at every of these different dimensions

### 00:54:04 · Speaker 5

T is concatenated. T, the vector T is concatenated at all of these.

### 00:54:11 · Speaker 5

So this is how I think in one of the improvised architectures, this is how this unit is implemented.

### 00:54:21 · Speaker 5

See, in your assignment, uh you don't have to do this. All you can do is just take a T, okay? uh Take the corresponding sinusoidal embedding, concatenate that with X T and just appropriately give it as an input. But if you can, right, this would be a better way to do it where you have skip connections. In fact, doing skip connections in PyTorch is not difficult. uh You can ask T S to help you out with that. And with every skip connection that you do, right, from अ टू अ पेयर ऑफ लेयर्स यू कंकैटनेट टी विद दैट। दैट इज हाउ इट इज टिपिकली डन।

### 00:55:01 · Speaker 5

Okay. Any questions on this? Yeah.

### 00:55:04 · Speaker 1

Yes. So one is uh yes sorry. I'll go ahead. So when you concatenate T to the other layer so the dimension is less than D or how do we

### 00:55:04 · Speaker 2

So one

### 00:55:17 · Speaker 5

Yeah, yeah, it is less than D. You have to appropriately take care of the dimensions.

### 00:55:23 · Speaker 1

ओके. सो सो द टीज़ विल बी जनरेटेड डिफरेंटली फॉर ईच एट ईच लेयर।

### 00:55:30 · Speaker 5

No no no no, you take the same T but the dimensionality have to be appropriately taken care of, that's all.

### 00:55:37 · Speaker 5

That's okay, no? That's okay. You just have to reshape it. You just have to reshape at every layer.

### 00:55:37 · Speaker 1

Okay

### 00:55:38 · Speaker 1

So we just take yes

### 00:55:43 · Speaker 1

Okay Okay

### 00:55:44 · Speaker 5

appropriately reshaped every layer

### 00:55:48 · Speaker 2

So I had the similar question so because unit the input layer would be some convolutional layers right? Right. So how do we append T to the data where because that's not really part of the image right?

### 00:55:54 · Speaker 5

So how do we

### 00:56:02 · Speaker 5

correct correct. It's not part of image that is why what is done is X T is not concatenated at the input layer. So what is done is after the first convolutional layer okay. you take the output of the first convolutional layer concatenate T okay appropriately reshape and then use the next layer. That is how it is done.

### 00:56:10 · Speaker 4

up

### 00:56:28 · Speaker 2

Okay

### 00:56:30 · Speaker 5

Okay

### 00:56:30 · Speaker 2

and any particular reason why we are using unit here? I mean why do we have to create this bottleneck in between?

### 00:56:37 · Speaker 5

otherwise no, like, x t and epsilon theta have the same dimensions, right? What sort of neural network do you use?

### 00:56:47 · Speaker 2

Okay

### 00:56:49 · Speaker 2

So so at at at the bottom it has to be some

### 00:56:49 · Speaker 5

at at the bottom it has to be some. see x c coming against you have to do it like this right. Now what will happen is x c has the same dimensions and you can you have to maintain the exact same dimension here and then get the epsilon theta right. See that would you will run into the problem of not learning it well because you might get into identity.

### 00:56:56 · Speaker 2

happen

### 00:57:10 · Speaker 2

Mm, okay.

### 00:57:11 · Speaker 5

then you have to reduce the dimensions. Start from X T and reduce the dimension. If you reduce the dimension, you will not get epsilon theta. You'll have to get to epsilon theta. Then you have to again increase the dimensions, right?

### 00:57:21 · Speaker 0

Okay

### 00:57:22 · Speaker 5

So that will make the architecture naturally unit kind of architecture.

### 00:57:23 · Speaker 0

got it

### 00:57:33 · Speaker 5

any other questions? See, I today I don't as I said no I don't have my multiple screens so, uh even you I don't I can't call call out names. So please unmute yourself and ask questions. I'll just answer them.

### 00:57:48 · Speaker 3

So just to correlate, in conditional GAN we use like one hot vector, that embedding. So is is that very similar to this one?

### 00:57:57 · Speaker 5

Yeah, but see, I've still not talked about conditional generation. I will talk about conditional generation while it is done very differently in a differential model.

### 00:58:06 · Speaker 3

I know I'm talking about VMs.

### 00:58:08 · Speaker 5

Come again

### 00:58:09 · Speaker 3

again in GAN, conditional GANs.

### 00:58:12 · Speaker 5

understand but see don't confuse this this concatenating this P with I mean as concatenating a class information that is not what it is we are still doing unconditional generation. Okay we will do conditional generation in a while I will talk about that like we will discuss that in a while. But yeah so it is similar in spirit to concatenating that one hot vector but please be like aware of the fact that this P is not

### 00:58:42 · Speaker 5

P is not having any class information here, okay? It is having the time information because there is a temporal evolution of the encoding process here, right? This P is having that time information, it does not have any class information.

### 00:58:59 · Speaker 4

Okay

### 00:58:59 · Speaker 0

Okay

### 00:59:08 · Speaker 2

So one more point. So with this time information, what we are, I mean, what we want the model to learn is at any given time step, how to do the denoising. Is that understanding correct?

### 00:59:20 · Speaker 5

correct. correct. correct. So, yeah, of course, see this look at it, no, what this unit is actually doing is given a noisy input, okay, at time T, it is trying to tell you what was the amount of noise that was added to make X not noisy.

### 00:59:41 · Speaker 5

epsilon theta is an estimate of that no

### 00:59:43 · Speaker 0

amount of noise because that is what you are regressing over

### 01:00:00 · Speaker 4

Any other questions? So now I think you can implement it, right?

### 01:00:09 · Speaker 5

Yeah. Okay, so let us move on quickly then. So this is about training. Let me talk about inference in DDPM. Suppose you have after you have trained this, how do you generate images? Okay, let us look at that.

### 01:00:22 · Speaker 5

then we will talk about conditional generation and then we will go to D D I M's. Okay so this is

### 01:00:27 · Speaker 1

inference with DDPMs

### 01:01:01 · Speaker 1

Okay. So what are we given? So we are given

### 01:02:42 · Speaker 1

Right? So this is what we should do.

### 01:02:44 · Speaker 5

we have a train network uh epsilon theta I mean say theta star okay that would take x t and give you epsilon theta so now what we need to do is we need to sample from x t p theta of x t minus one given x t okay

### 01:03:01 · Speaker 5

so let us do that. So we have to do it iteratively now.

### 01:03:07 · Speaker 5

See this is where one uh one of the drawbacks of D D P M comes you know the sampling is very very slow because we have to start from T equal to capital T and go all the way till

### 01:03:23 · Speaker 1

t equal to one. Let let me write that.

### 01:05:19 · Speaker 1

Yeah, that's right. So it's

### 01:05:21 · Speaker 5

it's pretty simple. See what is happening is the following, right? What do we need to do is we need to sample from this distribution P theta of X T minus one given X T, right? So what is P theta of X T minus one given X T? It's a normal distribution with mean equal to mu theta and variance equal to sigma T, right? So what is what is mu theta? mu theta is simply this X T divided by root of alpha T minus one minus alpha T this thing into epsilon theta, okay?

### 01:05:51 · Speaker 5

Is that okay? So now, how do we get a sample from a Gaussian distribution with a particular mean and variance? We know reparameterization. Sample from a zero mean unit variance Gaussian, right? And

### 01:06:04 · Speaker 4

Solid

### 01:06:06 · Speaker 5

shift it, right, with whatever mean you want and scale it with whatever variance you want. That is exactly what we are doing here.

### 01:06:15 · Speaker 5

So sample from a zero mean unit variance coefficient, okay? And this is the shift that

### 01:06:20 · Speaker 4

that you do to get that mu theta. So this entire thing

### 01:06:29 · Speaker 4

entire thing right is

### 01:06:32 · Speaker 5

μθ, that's all. Just shift it with μθ and this is again you have the σq, right, which is the variance that we are using and you get x θ minus one.

### 01:06:42 · Speaker 5

And where are we using the unit

### 01:06:44 · Speaker 4

here so the try intunet

### 01:06:53 · Speaker 4

तो दिस विल टेक एक्स टी एट

### 01:06:56 · Speaker 5

at every time, okay? And this will give you epsilon theta star which is used for sampling. You start from x capital T, pass this, you get x capital T minus one.

### 01:07:09 · Speaker 5

So then you take x capital T minus one, pass through this network, get epsilon theta star at that T, right? And then, uh keep doing it till you get x naught. This will give you a generated sample.

### 01:07:25 · Speaker 5

Is this all right? This is how you do sampling. See as I said, unlike in a in in a GAN, right? Or a VAE where doing one forward pass through the the network that is trained will give you a sample which is needed. uh This this is not the case. So here to do to generate one data sample, okay, you need to do capital T number of forward passes.

### 01:07:52 · Speaker 5

that makes this D D P M very slow, inference very slow. If you have seen these things like, you know, stable diffusion and all that, right? When you give a prompt, you'll have to wait for a while till you generate the sample. That is because it is doing these T number of forward passes through this network.

### 01:08:11 · Speaker 4

any questions on this?

### 01:08:14 · Speaker 4

maybe

### 01:08:17 · Speaker 1

school

### 01:08:17 · Speaker 1

plus

### 01:08:19 · Speaker 4

Let

### 01:08:19 · Speaker 1

Let me know if you have any questions on this.

### 01:08:23 · Speaker 6

So I have one question regarding the training of the network itself in the first place. So I mean what kind of issues can we anticipate while training? Just some practical

### 01:08:28 · Speaker 5

I mean

### 01:08:34 · Speaker 6

inch

### 01:08:36 · Speaker 5

DDPM training is not that hard. uh I mean that is why these are state of the art generative models, right? Visual visual models these days because they are pretty stable, okay? uh One thing that can happen is that if you don't sample your T properly, then the underlying distribution might not be learned.

### 01:08:57 · Speaker 5

But if you do good enough sampling, I've seen that in our experience these networks actually work pretty well.

### 01:09:08 · Speaker 5

unlike in a Gyan, right, where you have this saddle point problem and you have the mode collapse, etcetera, those sorts of issues do not generally arise with DDPMs.

### 01:09:22 · Speaker 6

ओके, एंड आफ्टर हाउ मेनी एपॉक्स वी कैन एक्सपेक्ट टू गेट अ गुड जनरेशन क्वालिटी?

### 01:09:26 · Speaker 5

That depends on data sets

### 01:09:30 · Speaker 5

you can track the loss, right? I mean this is a regression loss. So whenever the loss is converging and reducing, that is the point where you can perhaps stop.

### 01:09:44 · Speaker 5

depends on the data set. It completely depends on the data set and the architecture, how deep your architecture is and there's no one answer for that.

### 01:09:52 · Speaker 5

Okay, so

### 01:09:53 · Speaker 1

Any questions on inference generation?

### 01:10:13 · Speaker 1

No questions

### 01:10:21 · Speaker 1

Okay, shall we move on then?

### 01:10:34 · Speaker 1

Am I audible? Like, did I

### 01:10:38 · Speaker 4

down or something. Hello?

### 01:10:40 · Speaker 1

Yes sir

### 01:10:40 · Speaker 4

Yes sir

### 01:10:41 · Speaker 1

We can okay

### 01:10:42 · Speaker 4

Okay. Tell me. Okay.

### 01:10:45 · Speaker 4

So next what we will do is

### 01:10:54 · Speaker 1

we look at how to do conditional generation, okay? guided diffusion.

### 01:11:10 · Speaker 1

So before that sir can you give an example where

### 01:11:13 · Speaker 2

this unconditional DDPMS used

### 01:11:20 · Speaker 5

Well if you want to build a generative model right, uh where you don't condition it on a particular uh text or like any uh prompt or anything you can use. I mean you can take any data set and

### 01:11:36 · Speaker 5

and generate. I didn't get your question. Are you asking me for a

### 01:11:42 · Speaker 2

uh yeah specifically like uh if we give a prompt uh and say like create this uh using a diffusion model that that is a conditional uh diffusion right?

### 01:11:51 · Speaker 5

Correct

### 01:11:53 · Speaker 2

And if it's random then it's unconditional. Is that correct?

### 01:11:53 · Speaker 5

Sir

### 01:11:57 · Speaker 5

uh see don't call it as random okay I mean there's nothing random about it I mean the point is if you are sampling from some distribution P X then it is unconditional generation if you are sampling from P X given Y where Y is another random variable then it becomes conditional generation.

### 01:12:16 · Speaker 2

Yeah, got it.

### 01:12:19 · Speaker 1

Hmm

### 01:12:22 · Speaker 1

Yeah, so, uh,

### 01:13:00 · Speaker 1

Okay

### 01:13:02 · Speaker 1

just thinking if I have to like

### 01:13:05 · Speaker 1

to

### 01:13:05 · Speaker 5

that now I'll just take a break and do it. What do you want? Should we do you need a break or should we complete this? It will take me for twenty minutes to complete guided diffusion.

### 01:13:18 · Speaker 4

shall I complete that and then take a break?

### 01:13:26 · Speaker 4

Okay, let's finish this, huh? Okay.

### 01:13:29 · Speaker 4

Okay. See,

### 01:13:33 · Speaker 5

while the diffusion models were being developed, there was another parallel formulation, right, for the generative models that came out, that was that those were called

### 01:13:48 · Speaker 5

score based models, okay?

### 01:13:54 · Speaker 5

So there are multiple variants of score based models but all of them converge to DDPM. So let I'll not describe more I mean score based models in detail because they are not different class of generative models they are also diffusion models. But yeah so let me talk about just quickly mention score based formulation. We need this for guided diffusion meaning conditional diffusion that's why I'm doing this.

### 01:14:22 · Speaker 4

score based deformation

### 01:14:30 · Speaker 1

Okay

### 01:14:33 · Speaker 1

Okay. Now, there is a statistical result, okay? That would say that

### 01:14:51 · Speaker 1

called. Okay, let me write that.

### 01:14:54 · Speaker 1

Now there is something called result.

### 01:14:58 · Speaker 1

will not prove this I'll just state it this is also called the uh 3D's formula

### 01:15:18 · Speaker 1

which would say that this is a very well known

### 01:15:21 · Speaker 5

classical historical result that would say that if Z

### 01:15:24 · Speaker 4

is a Gaussian quantum variable

### 01:15:29 · Speaker 4

which mean mu c and variance sigma c, okay?

### 01:15:39 · Speaker 4

then

### 01:15:42 · Speaker 4

the

### 01:15:45 · Speaker 4

expect

### 01:15:45 · Speaker 5

expectation of

### 01:15:48 · Speaker 5

μz given z, okay, expectation of the mean given z is given by z plus

### 01:15:56 · Speaker 5

7

### 01:15:58 · Speaker 5

Sigma Z times

### 01:16:02 · Speaker 5

gradient of

### 01:16:04 · Speaker 5

log of

### 01:16:07 · Speaker 5

easy with respect to Z. Okay. So please take this defaced value, right? This is something that can be proved. Assume that this is true, okay? This is called the 2D formula.

### 01:16:19 · Speaker 5

Okay, so now here the

### 01:16:24 · Speaker 5

gradient of the log likelihood of a particular distribution with respect to the random variable of interest is defined

### 01:16:33 · Speaker 1

as core. This is this core function.

### 01:17:02 · Speaker 1

Okay, this is a known result.

### 01:17:04 · Speaker 1

Okay, so now we let

### 01:17:05 · Speaker 1

use this result

### 01:17:07 · Speaker 1

what do we do is we have in the

### 01:17:08 · Speaker 1

context of D D P

### 01:17:10 · Speaker 1

M

### 01:17:19 · Speaker 1

context of D D P M. We had this Q of

### 01:17:23 · Speaker 5

Hello

### 01:17:24 · Speaker 5

xt given x not remember this right using the recursion we showed that this was a Gaussian okay with mean being equal to root of alpha t bar into x not the variance was one minus alpha t bar times i okay

### 01:17:45 · Speaker 5

the quadratic distribution. Suppose I apply this 2D formula to this, okay? What I can write is that I can write the expectation of

### 01:17:58 · Speaker 5

mu x t, okay? which is the expectation of distribution given x t is written as x t plus

### 01:18:10 · Speaker 4

one minus alpha t bar

### 01:18:15 · Speaker 4

Times

### 01:18:18 · Speaker 4

root of X T

### 01:18:22 · Speaker 4

Log of

### 01:18:24 · Speaker 5

P X T. It is simply applying the treaties formula as above, right? I mean sigma, the variance of this is one minus alpha T bar into I, therefore, uh the identity matrix will go away, this will simply be this particular thing. Okay. So what is the mean of this distribution? We know that the mean of this distribution is the root of

### 01:18:46 · Speaker 5

alpha t bar into x naught is equal to x t plus

### 01:18:51 · Speaker 4

one minus alpha t bar

### 01:18:54 · Speaker 4

Fines

### 01:18:57 · Speaker 4

the score function

### 01:19:00 · Speaker 4

P of X T

### 01:19:02 · Speaker 4

Okay. So now rearranging the terms, this implies my x naught can be reparameterized in terms of

### 01:19:12 · Speaker 4

X T

### 01:19:15 · Speaker 4

Plus

### 01:19:15 · Speaker 1

1 minus alpha t bar

### 01:19:20 · Speaker 1

into the score function

### 01:19:27 · Speaker 1

evaluated by

### 01:19:29 · Speaker 1

root of alpha t bar

### 01:19:32 · Speaker 5

Okay. Okay. Now, why is this of any consequences? Because we also know that this x naught, okay, was reparameterized in terms of

### 01:19:47 · Speaker 4

minus alpha t bar into epsilon right if you remember this

### 01:19:56 · Speaker 4

Okay, this is what it was. We showed this. So we if we compare the terms, okay, we see that the score of

### 01:20:09 · Speaker 4

log of p of x t is simply equal to some scaled version of

### 01:20:16 · Speaker 5

minus alpha t bar times epsilon. Okay, this is the result that we need, okay, which is that the ground truth, I mean the noise that we are adding to x t, okay, is actually the score, uh, which is the derivative of log of p of x t with respect to x t. It is scale.

### 01:20:41 · Speaker 5

Is this all right? So this implies, this implies that the loss function that we had, no, which was epsilon minus epsilon theta cap.

### 01:20:51 · Speaker 5

okay, is equivalent to

### 01:20:55 · Speaker 5

Right?

### 01:20:58 · Speaker 1

regressing over the score of the model.

### 01:21:06 · Speaker 5

a particularity. So this is the result, right? I mean, that that's why the name DDPMs are also called score based model. So basically, what is being done is score matching.

### 01:21:17 · Speaker 5

Isn't it? So the true score, the true score is the noise and whatever the model is giving can be looked into as uh the estimated score through using the neural network and that is what we are matching. Is that all right? See actually we don't need this result. What we need is that a simple thing that why when we are constructing DDPMs, we are implicitly okay matching the scores.

### 01:21:46 · Speaker 5

of the, I mean the true score and the estimated score. Is that, is that all right?

### 01:21:52 · Speaker 5

I mean this is the result that we actually need right which is the

### 01:21:57 · Speaker 5

original noise that we add to make x not x t, okay? is actually a scaled version of what is called as the score function. Is this is all right? So we will use this result to uh to uh build a uh conditional diffusion model. Okay?

### 01:22:20 · Speaker 5

Any questions so far?

### 01:22:22 · Speaker 5

we don't we all we did was you know we just introduced a concept called score which is the derivative of the log likelihood of random variable with respect to the random variable itself, okay? And we showed that in the case of a D D P M, the ground truth noise that we add to X naught to get to X T is simply a scaled version of what is called as the score function at X T. Is this all right? Any questions here?

### 01:23:07 · Speaker 1

yeah, I don't, if you don't speak up,

### 01:23:10 · Speaker 5

I don't know. I I don't I can't see my screen, right? So if you are interacting, I don't know if you are interacting. So I think it's better if you speak up. Shall we move on? This is all right?

### 01:23:24 · Speaker 4

Yes sir. Yes yes.

### 01:23:26 · Speaker 5

So now we will do what is called as conditional generation.

### 01:23:31 · Speaker 1

using this idea is also called degraded diffusion.

### 01:23:41 · Speaker 1

typically called classifier guided diffusion.

### 01:23:54 · Speaker 1

Okay. Okay.

### 01:23:56 · Speaker 1

Okay, so note that, Okay, so note

### 01:24:03 · Speaker 1

60

### 01:24:06 · Speaker 1

DDBPM

### 01:24:09 · Speaker 1

training

### 01:24:12 · Speaker 1

Estimates

### 01:24:21 · Speaker 1

estimates the score of

### 01:24:30 · Speaker 1

E X T, right? That is what it is doing. We know that. That's where we will use the fact. Now, for conditional generation,

### 01:24:48 · Speaker 1

one needs to estimate

### 01:25:00 · Speaker 1

score of

### 01:25:04 · Speaker 1

P of X

### 01:25:05 · Speaker 5

text t given y, okay, where y is a conditional random variable which can be a class or a text embedding or anything, right? condition.

### 01:25:18 · Speaker 5

can be a class label

### 01:25:23 · Speaker 5

or it can be a text embedding or anything depending upon what your classes

### 01:25:29 · Speaker 5

what your conditioning is, right? So, yeah. So what we are doing is instead of estimating the score of P X T, we need to we need to estimate the score of P X T given Y. Correct? That is what is to be done. Now how do we do that is that we simply use base rule to do that. We have

### 01:25:49 · Speaker 5

the score of log of we need P of X T given Y right with respect to X T

### 01:26:01 · Speaker 4

is the derivative of log of

### 01:26:07 · Speaker 4

I will use Bayes' law

### 01:26:10 · Speaker 4

p of x t times

### 01:26:13 · Speaker 4

PFY

### 01:26:14 · Speaker 5

I given XT

### 01:26:17 · Speaker 5

divided by P by this is Bayes' law, okay? Then I will use the law of

### 01:26:23 · Speaker 4

logarithms, so this is

### 01:26:26 · Speaker 4

log of p of x t

### 01:26:30 · Speaker 4

Plus

### 01:26:33 · Speaker 4

log of

### 01:26:36 · Speaker 4

P of Y given X T

### 01:26:40 · Speaker 4

minus

### 01:26:42 · Speaker 4

log of derivative of

### 01:26:44 · Speaker 4

Hello

### 01:26:45 · Speaker 5

log of

### 01:26:47 · Speaker 5

p of y. Note that these derivatives are with respect to x t because these are scores, right? Right? Now this term is zero because it is independent of y. So now the condition

### 01:27:00 · Speaker 4

original score that we would want to estimate

### 01:27:09 · Speaker 4

equal to derivative of log of

### 01:27:13 · Speaker 5

p x t with respect to x t this is the unconditional score right? plus some term okay this is log of

### 01:27:24 · Speaker 5

P Y given X T with respect to X T

### 01:27:29 · Speaker 5

Yeah, so this is the result. This is the result that we need is that what we showed is that the

### 01:27:36 · Speaker 4

in the

### 01:27:37 · Speaker 5

If you want to train a diffusion model on P of X T given Y, all you need to do is train a model on unconditional data and have an additional term, okay, estimate the score, okay?

### 01:27:53 · Speaker 5

estimate the score, okay, of P of Y given X T. So what do you mean by that? How do we do this in practices? That

### 01:28:03 · Speaker 5

P of

### 01:28:05 · Speaker 5

Why given XT?

### 01:28:06 · Speaker 4

What is this?

### 01:28:08 · Speaker 4

is actually a classifier, right?

### 01:28:15 · Speaker 4

You agree? See, Y is a class that you are conditioning your generation on. P of Y given XT is a classifier on XT, isn't it?

### 01:28:27 · Speaker 4

Hello

### 01:28:27 · Speaker 1

Hello

### 01:28:27 · Speaker 4

Yes sir

### 01:28:27 · Speaker 1

Yes sir. So what is done is that first train

### 01:28:35 · Speaker 1

Try a classifier

### 01:28:41 · Speaker 1

on X

### 01:28:41 · Speaker 4

Okay? Just keep it, you know, try and classify it on XT and then guide, guide

### 01:28:50 · Speaker 4

the diffusion unit.

### 01:28:57 · Speaker 1

this classifier. Okay, what do you mean by that?

### 01:29:03 · Speaker 1

So now there is a

### 01:29:03 · Speaker 4

as a

### 01:29:05 · Speaker 5

that is to be trained

### 01:29:08 · Speaker 5

and note that this is actually estimating the score, right? So this will take X T

### 01:29:16 · Speaker 5

anti. Now because this is a network uh that is a conditional diffusion model it will also take a y as an input. This is where you have the the class label right that is coming as an input so let us make it a little more uh

### 01:29:36 · Speaker 5

easier to understand. So this will take X T and Y as an input and here you have the

### 01:29:44 · Speaker 5

P going as an input, okay? Right? So now what you get here is the epsilon theta star which is

### 01:29:52 · Speaker 5

the unconditional score, right? We want this to be the conditional score. What do we do is that try in another classifier.

### 01:30:03 · Speaker 5

This classifier is P Y given X T. So this will take X T as an input and it will give you a class. Okay, this is pre-trained. Okay, we keep the classifier pre-trained. Now what you do is there is a score matching that has happened.

### 01:30:19 · Speaker 4

happening here which is the usual

### 01:30:26 · Speaker 4

laws that is back propagated, okay?

### 01:30:30 · Speaker 5

addition to this you also calculate here okay the this is the output of p of y given x t okay take the log of it compute the derivative of this gradient of this with respect to x t how do you do this see we can do a back propagation with respect to parameters just like we do that we can do a back propagation with respect to the input of the network also in pytor right so you take the gradient of this the output of this network with respect to X T here, okay? You back propagate. Add those gradients.

### 01:31:05 · Speaker 4

ends. Okay?

### 01:31:13 · Speaker 1

with respect to XT to this and then back pop gate here.

### 01:31:18 · Speaker 1

That's how you train it

### 01:31:21 · Speaker 5

This is all right. So finally during the inference what do you do? You give an x and y as an input to the data star network. If the sampling is exactly the same. Sampling procedure here is the same thing right? You do the exact same thing here but you give y also as an input here while you are estimating this noise.

### 01:31:47 · Speaker 6

Sir, one question.

### 01:31:49 · Speaker 5

Yeah, hold on.

### 01:31:50 · Speaker 5

half

### 01:31:50 · Speaker 4

Okay, sorry

### 01:31:50 · Speaker 6

Okay, sorry

### 01:31:51 · Speaker 5

Yes

### 01:31:53 · Speaker 4

Hello

### 01:31:53 · Speaker 5

Yeah, so this is called classifier guided diffusion models, conditional diffusion, classifier guided conditional diffusion. See, there is another version called classifier free guidance. I will not talk about it. I mean, you can just see that as

### 01:32:11 · Speaker 4

homework. It's a variant of this.

### 01:32:19 · Speaker 4

just read that as self study thing. Yeah, this is called

### 01:32:22 · Speaker 5

classifier guided conditional diffusion where uh you first uh realize that uh the diffusion model that you are training is implicitly doing the score matching and use Bayes' law to estimate I mean represent the conditional score in terms of unconditional score and the classifier okay pre-trained classifier on XT on different noise levels okay and then use that pre-trained classifier along with the unit to uh estimate

### 01:32:52 · Speaker 5

made the conditional score. Okay, then you have trained a conditional diffusion model where you have classifier guided. So now one question that might come up is, uh, see, Y need not be a class label, no, it can be a text embedding also. If it happens to be a text embedding, this P of Y given X, uh, Y given XT will become a regression mode, regression network that would take an XT and produce the uh, corresponding text embedding.

### 01:33:24 · Speaker 5

Okay

### 01:33:26 · Speaker 5

Right. So I have asked you to implement this. So what you should do is, uh, why you collect multiple XTs, no, while you are training this theta, you also train a classifier to get the corresponding class for the XT, okay? Use that classifier, get the gradient of every XT with respect to the output of this classifier and add that to the gradient of this unit and back propagate. That is what you need to do.

### 01:33:56 · Speaker 5

Okay. Yeah, so now any questions on this?

### 01:34:00 · Speaker 6

Yes sir, so the classifier is not trained as part of the process, right?

### 01:34:05 · Speaker 5

So classifier is already pre-trained. So you pre-trained a classifier and keep it. Yes.

### 01:34:07 · Speaker 6

Preet

### 01:34:10 · Speaker 6

Okay, but if the but if it has no effect, if this process does not have an effect on our, if we are not getting the desired results, what could be wrong actually?

### 01:34:21 · Speaker 5

uh what's the see typically what happens in classifier guided diffusion this x see if you look at it this classifier has to discern the class uh by taking a noisy sample as input correct?

### 01:34:38 · Speaker 3

okay. Now if

### 01:34:40 · Speaker 5

Now if if T is very high, the sample becomes too noisy. See, it has to discern the class at all noise levels, that will become too much for a classifier to do, isn't it?

### 01:34:52 · Speaker 3

ओके, ओके

### 01:34:53 · Speaker 5

And typically this classifier fails that is at high higher noise levels and that's why classifier guided diffusion does not work too nicely.

### 01:34:54 · Speaker 3

the

### 01:35:02 · Speaker 5

that's why people went from classifier guided diffusion to classifier free diffusion. Okay, classifier free guidance. Okay, so which I said just read it as a homework. I mean I need uh I mean I I leave some questions, I mean some concepts uh to you as homework. So that's why people moved to classifier free guidance where there is no classifier. Why when you do guidance? Just read that. It is there in the tutorial that I had given uh as a reference.

### 01:35:32 · Speaker 5

read that once. But yeah, but what I've asked you to implement in assignments is a classifier guided diffusion. The problem might be that you are overburdening this classifier to get the classes at multiple noise levels. That's why that's where the problem can come. In fact, all the the state of the art models, right, like this this stable diffusion, imagine, etcetera, all all use classifier free guidance, not classifier guided diffusion for conditioning.

### 01:36:03 · Speaker 5

Yeah. Okay sir. Any other question? See there is uh one of the last piece right? I mean you see this uh stable diffusion thing. I have asked you to do that in your assignment as well. This stable diffusion stability.ai company you know what they are doing is...

### 01:36:03 · Speaker 4

ओके सर, एनी इन द

### 01:36:20 · Speaker 5

the diffusion DDPMs are not built on the image space. What they do is they first train

### 01:36:30 · Speaker 4

take x naught and get x

### 01:36:33 · Speaker 5

nod cap. So this is they first try in a VQVI, okay?

### 01:36:39 · Speaker 5

This is the encoder and decoder of a VQVAE, okay? So you get the Z corresponding to uh the data. They first train a VQVAE, okay?

### 01:36:51 · Speaker 5

Then what they do is, TDPM

### 01:36:55 · Speaker 5

or tetra

### 01:36:56 · Speaker 1

Time DDPM

### 01:36:59 · Speaker 1

on the latent space of VQVI

### 01:37:12 · Speaker 1

They train

### 01:37:13 · Speaker 4

DDPM on the latent space of VQIE and the generation right so now what happens is generation

### 01:37:24 · Speaker 4

is first

### 01:37:28 · Speaker 4

get a new latent sample

### 01:37:31 · Speaker 5

right? Because the entire generative model is

### 01:37:34 · Speaker 5

built on the the latent space of VQVI and then pass it

### 01:37:44 · Speaker 1

through the decoder

### 01:37:49 · Speaker 1

of VQVAE, okay, to finally get the image.

### 01:37:58 · Speaker 4

I asked you to do this as well, right?

### 01:38:00 · Speaker 5

I mean it's pretty simple. The point is that building a diffusion model on the image space is very difficult because it's of very high dimensions, right? So instead of doing that, you first train an encoder decoder model or a VQVAE, get the latent vectors and you train a DDPM on the latent vectors of the the VQVAE and then when you sample, you first sample the latent vector, new latent vector, pass it through the decoder.

### 01:38:30 · Speaker 5

of EQVAE and get the generated sample. That's what all, I mean that's what is done in this stable diffusion, right, where, I mean the step, they call it step is stable because you are not doing it on the image space but you are doing it on the latent space of a pre-trained EQVAE.

### 01:38:49 · Speaker 5

Okay, so that's about it. That's all I wanted to cover in DDPMs. So one other piece to be covered today is DDIMs, right? Diffusion Implicit Models where you have the inversion possibility of inversion and also they address this drawback of the inference time of DDPM being too slow, right? Because you need to hop capital T number of steps which is typically of order of thousands. So

### 01:39:19 · Speaker 5

DDIMs which are denosing diffusion implicit models will take care of that particular issue. We will look at DDIMs and then I will go to noise contrast estimation and self-supervised learning, okay? Shall we take a break now? About ten fifteen minutes.

### 01:39:39 · Speaker 4

Yes sir. Yes.

### 01:39:39 · Speaker 7

Yes sir

### 01:39:41 · Speaker 5

the plan is the following right I will uh we will we will do DDPMs DDIMs this class possible at the end of this class uh I will just give you an introduction to self supervised learning. Next class I will do noise contrast estimation self supervised learning and if possible I will also sneak in some distillation ideas knowledge distillation and in the final class on sixteenth we will look at auto regressive models transformers and some introduction to LLMs.

### 01:40:11 · Speaker 5

that would conclude the course. See we had to have fourteen classes right? uh How how much do we have? Do we have? How many classes have we done so far? Does anyone have a count?

### 01:40:27 · Speaker 6

सर एस पर योर लेक्चर लेबल इट इज टेंथ

### 01:40:31 · Speaker 1

Yeah

### 01:40:31 · Speaker 5

That's I also noticed that but did I start writing from the very first class?

### 01:40:40 · Speaker 7

I think there's also lecture zeros so it is it's like eleven

### 01:40:42 · Speaker 4

It's like eleventh. First day is let's say zero. Eleventh class.

### 01:40:46 · Speaker 5

is there a zero? Yeah, there is a logistic.

### 01:40:48 · Speaker 7

logistics one yeah

### 01:40:51 · Speaker 5

So yeah this is eleven so we'll have thirteen classes huh okay. Yeah typically that's what a semester is you know it's between thirteen and fourteen fourteen classes of three hours.

### 01:41:02 · Speaker 5

Well it's okay I think we have covered like a sufficient group so we'll have two more classes right? We'll do self supervised learning distillation and some introduction to L L M's I think that would that would conclude it. Okay so let's take a break it's eleven ten uh let's take a short break of about ten minutes and come back at eleven twenty.

### 01:41:24 · Speaker 5

Okay

### 01:41:26 · Speaker 7

Yeah, so just one question. So in the assignment, you've mentioned I J E P G. So would you be talking about that?

### 01:41:35 · Speaker 5

Of course, definitely.

### 01:41:37 · Speaker 7

Okay

### 01:41:38 · Speaker 5

Maybe in the next class, yeah. It's a self-supervised learning method called IJEPA. I'll do it in the next class, perhaps.

### 01:41:45 · Speaker 7

Sure sir

### 01:41:46 · Speaker 5

ओके, या। सी यू इन अबाउट, प्लीज कम बैक इन टेन मिनट्स, हां, वेयर यू हैव थिंग्स टू कवर, या।

### 01:41:52 · Speaker 1

See

### 01:51:47 · Speaker 0

Hi

### 01:51:47 · Speaker 1

find

### 01:51:48 · Speaker 0

my driveway. I was worried that one day some kid is going to come whipping around that corner to fuck up a bit deep of me or Isabel while

### 01:56:48 · Speaker 1

Hello, shall we resume?

### 01:56:53 · Speaker 3

Yes sir. Sir I have a question regarding stable diffusion.

### 01:56:53 · Speaker 4

Yes

### 01:56:58 · Speaker 4

Yeah yeah

### 01:56:59 · Speaker 5

Me

### 01:57:00 · Speaker 3

So the latent space used in the generation, is it just after the encoder or the after mapping to the dictionary of embeddings?

### 01:57:10 · Speaker 5

Oh yeah yeah yeah. So it is the quantized latent space only.

### 01:57:15 · Speaker 1

ಓಕೆ ಓಕೆ

### 01:57:17 · Speaker 5

Yeah

### 01:57:18 · Speaker 6

So but how do we sample from that because it's a it's a quantized set of factors right?

### 01:57:24 · Speaker 5

So what? See, the you take the encodings as the quantized vectors, right? And then build a generative model on top of it.

### 01:57:36 · Speaker 5

then the all the all the

### 01:57:36 · Speaker 6

all the quantized vectors

### 01:57:38 · Speaker 5

correct for corresponding to the entire

### 01:57:40 · Speaker 1

data set

### 01:57:44 · Speaker 6

Okay

### 01:57:46 · Speaker 1

Okay so

### 01:57:46 · Speaker 4

okay

### 01:57:48 · Speaker 1

Hello

### 01:57:51 · Speaker 1

Any other questions?

### 01:57:59 · Speaker 1

Okay. Oh.

### 01:58:15 · Speaker 1

start with some chart.

### 01:58:44 · Speaker 1

Okay

### 01:58:44 · Speaker 1

ஓகே சோ லெட் அஸ்

### 01:58:46 · Speaker 4

look at this another class of models now called DDIMs or

### 01:58:58 · Speaker 1

denosing

### 01:59:03 · Speaker 1

fusion implicit models they are called

### 01:59:24 · Speaker 1

Okay

### 01:59:26 · Speaker 1

Okay, so now they

### 01:59:28 · Speaker 5

the motivation for these class of models are the following, right? So they first ask this question, right? D D P M's.

### 01:59:40 · Speaker 4

or Markovian, right?

### 01:59:47 · Speaker 4

Actually first order mark will be

### 01:59:51 · Speaker 4

because of this what happens is so the sampling or the inference

### 02:00:01 · Speaker 3

sampling is low. uh What do you mean by that? It is

### 02:00:06 · Speaker 2

slow because

### 02:00:10 · Speaker 2

the sampler

### 02:00:16 · Speaker 2

as to hop through

### 02:00:23 · Speaker 2

P steps

### 02:00:27 · Speaker 2

Isn't it recall that right in the sampling procedure

### 02:00:45 · Speaker 2

inference

### 02:00:46 · Speaker 3

here you need to hop through capital T to one, okay, which is very slow. So why is this happening? This is happening because the uh the uh model that we have constructed is Markovian, right? The question that they asked in DDIMS, so is there a

### 02:01:08 · Speaker 3

The question is, so this is, yeah, I'll

### 02:01:13 · Speaker 3

I can give you the other motivation also and then we will answer both of them using one model construction.

### 02:01:51 · Speaker 2

GDPM

### 02:01:52 · Speaker 3

cannot perform posterior inference or also called inversion, okay? So what do we mean by that? We know that, right? I mean, given X, we need P of Z given X, we need a latent vector. And DDPMs cannot do that. Okay? Why? Why is that? Because the encoding process will converge to normal zero one and for every input sample, you will get some sample from normal zero one. Now suppose you take that sample from normal zero one.

### 02:02:22 · Speaker 3

okay? And run through the the generate generation process or the denosing process. Okay? There's no guarantee that you get the exact same image that you started with. Let me repeat what I said. Suppose you take an image, okay? or a data point and encode it using the DDPM's encoder, you get a particular X capital T, right? Now, if you take the same image and do encoding another time,

### 02:02:52 · Speaker 3

you will get another sample corresponding to that, right? If you take both those outputs of both both of those forward processes and run through the backward process.

### 02:03:02 · Speaker 3

There is no guarantee that you will get the exact same input sample that you started with in a D D P M model, right?

### 02:03:11 · Speaker 3

Okay, that's what I mean by D D P M's cannot perform posterior inference or inversion. So now the question is, can both of these D D I M's solve both of these issues actually, okay?

### 02:03:17 · Speaker 2

Soon

### 02:03:30 · Speaker 2

DDIMs are

### 02:03:36 · Speaker 2

non non-Markovian

### 02:03:39 · Speaker 1

soon

### 02:03:41 · Speaker 2

models.

### 02:03:44 · Speaker 2

Okay

### 02:03:46 · Speaker 2

Tata

### 02:03:48 · Speaker 2

that enable fast sampling

### 02:03:57 · Speaker 2

Because of the non-mark

### 02:03:58 · Speaker 3

assumption, right? Okay, non-Mohr enable fast sampling plus inversion, both of these are possible.

### 02:04:07 · Speaker 2

Okay

### 02:04:08 · Speaker 3

Now the, I mean this is not the most interesting part. The most interesting part is that

### 02:04:17 · Speaker 3

If you train a DDPM, okay, then you are also training DDIM, which is which means that requires additional training.

### 02:04:31 · Speaker 2

No additional training

### 02:04:40 · Speaker 2

So this is the beautiful part of it, right? Than DDT

### 02:04:43 · Speaker 3

PM

### 02:04:45 · Speaker 3

If you train a D D P M then you are implicitly training uh D D I M is what the idea is. Okay? So let us uh concretize these ideas you know what do I mean by all this we will we will put math through it and understand.

### 02:04:59 · Speaker 2

Hmm

### 02:05:00 · Speaker 3

Okay. See, the first observation that is made is

### 02:05:04 · Speaker 3

Hmm

### 02:05:11 · Speaker 2

observation

### 02:05:19 · Speaker 2

the DDBM

### 02:05:42 · Speaker 2

DDPM loss

### 02:05:47 · Speaker 2

function okay

### 02:05:51 · Speaker 2

pass function

### 02:05:53 · Speaker 2

depends

### 02:05:59 · Speaker 2

only on

### 02:06:02 · Speaker 2

Queue of

### 02:06:07 · Speaker 2

xt given x not

### 02:06:11 · Speaker 3

Okay, this is the first observation that they do is that the DDPM loss function only depends on Q of XT given X not.

### 02:06:22 · Speaker 3

Okay. So now the

### 02:06:27 · Speaker 2

the

### 02:06:30 · Speaker 2

Based on this observation,

### 02:06:36 · Speaker 2

right? Based on this observation, they say that

### 02:06:45 · Speaker 2

and not on

### 02:06:50 · Speaker 2

क्यू ऑफ

### 02:06:53 · Speaker 2

X

### 02:06:57 · Speaker 3

one to T given X not

### 02:07:00 · Speaker 3

Okay, so please pay attention here. See, Q of X T given X naught is the posterior of the Tth latent variable conditioned on X naught, okay? And Q of X one to T given X naught is the joint distribution of, okay, all the latents given the data variable. Now, the observation that is made is that the DTPM loss function, okay, or the ELBO

### 02:07:30 · Speaker 3

does not depend on the joint the joint distribution of all the latents given data but only on the t-th latent variable given data. Okay? So this means

### 02:07:49 · Speaker 2

implies that

### 02:07:51 · Speaker 2

as long as okay Q of

### 02:08:05 · Speaker 2

is same

### 02:08:09 · Speaker 2

as that of D D P M

### 02:08:16 · Speaker 2

the elbow does not alter. This is the key observation, okay?

### 02:08:21 · Speaker 1

Hmm

### 02:08:27 · Speaker 3

Okay? So which means that as long as Q of XT given X not remains the constant, the elbow doesn't alter, okay?

### 02:08:35 · Speaker 3

Which means that, see, there is one other known thing in probability theory which would say that there can exist multiple joint distribution that has the same conditional.

### 02:08:51 · Speaker 3

you that does it make sense? Suppose there are like there is a particular conditional distribution, okay? We can construct multiple joint distribution that would have exactly the same conditional distribution.

### 02:09:04 · Speaker 3

Okay. So what they do is, so define

### 02:09:11 · Speaker 3

a family of

### 02:09:13 · Speaker 2

of non-Markovian

### 02:09:16 · Speaker 2

including distribution.

### 02:09:36 · Speaker 2

and coding distributions, okay? That have

### 02:09:42 · Speaker 2

the exact

### 02:09:50 · Speaker 2

conditional

### 02:09:54 · Speaker 2

as in

### 02:09:55 · Speaker 3

DDPPM. So what we are seeking is that I will give you now a family of non-Markovian

### 02:10:04 · Speaker 3

conditional encoding distribution such that the conditional is same that of the uh D D P M okay. So what they do is suppose

### 02:10:20 · Speaker 2

Sigma is a positive real number.

### 02:10:27 · Speaker 3

is a positive real number they define Q sigma of

### 02:10:35 · Speaker 3

x one two three given x naught. So this is the joint distribution non-Markovian joint distribution that we are defining, okay? It's given by

### 02:10:47 · Speaker 3

Q of Q sigma

### 02:10:53 · Speaker 3

xt given x not

### 02:10:54 · Speaker 2

Hello

### 02:10:56 · Speaker 3

Friends

### 02:10:58 · Speaker 3

This is by the uh chain rule of probability Q sigma

### 02:11:07 · Speaker 3

x t minus one given x t and x not

### 02:11:14 · Speaker 2

This is a non-Markovian distribution, okay?

### 02:11:17 · Speaker 2

where

### 02:11:21 · Speaker 2

Q sigma

### 02:11:25 · Speaker 2

X

### 02:11:27 · Speaker 2

p minus one given xt and x not

### 02:11:33 · Speaker 2

it's a normal distribution.

### 02:11:36 · Speaker 2

which

### 02:11:39 · Speaker 3

Mean equal to root of

### 02:11:44 · Speaker 3

alpha t minus one bar the same notation that we have with d d p m x naught plus

### 02:11:51 · Speaker 3

root of

### 02:11:52 · Speaker 3

one minus alpha t minus one bar

### 02:11:57 · Speaker 2

minus sigma t squared

### 02:12:14 · Speaker 2

Hold on, where is this?

### 02:12:20 · Speaker 2

just a second. Here, this is

### 02:12:26 · Speaker 2

exploit the this is

### 02:12:34 · Speaker 2

something wrong with this

### 02:12:40 · Speaker 2

one minus

### 02:12:43 · Speaker 2

one minus alpha t into

### 02:12:46 · Speaker 2

sigma t squared, okay? And yeah.

### 02:12:54 · Speaker 2

looks a little complicated but yeah I'll tell you why this was done

### 02:12:59 · Speaker 2

two

### 02:13:03 · Speaker 2

x t minus root of alpha

### 02:13:07 · Speaker 3

bar into x not

### 02:13:12 · Speaker 3

divided by root of one minus alpha t bar

### 02:13:18 · Speaker 3

is the mean and the variances, yeah.

### 02:13:22 · Speaker 3

Sigma squared into I. Yes, just a minute.

### 02:13:30 · Speaker 3

Okay? So this is the distribution. So now why is this how did they get into this complicated form is simply they wrote this down such that uh such that sigma Q sigma of X T given X naught, okay? will match that of the D D P M which is simply

### 02:13:59 · Speaker 3

just

### 02:14:00 · Speaker 3

term that we knew, right? Alpha

### 02:14:01 · Speaker 3

bar into I

### 02:14:03 · Speaker 3

Okay, so this distribution, okay, Q sigma is constructed in such a way that

### 02:14:11 · Speaker 3

the conditional distribution matches that of uh D D P M.

### 02:14:18 · Speaker 3

is this is this clear?

### 02:14:24 · Speaker 3

See, there is that the DDPM, DDIM's paper, right, gives a proof that why would, I mean, that they do the algebra and show that Q sigma of XT given X not is normal, this has this particular form that matches with that of DDPM. But yeah, so the point is that what we have done now is defined a family of non-Markovian forward processes, okay, such that all of them have the same condition. channel as that of DDPM. Is this clear?

### 02:14:57 · Speaker 2

Any questions so far?

### 02:15:25 · Speaker 2

Hello, am I there?

### 02:15:29 · Speaker 3

Yes sir

### 02:15:30 · Speaker 2

Yeah, uh questions here, did you understand this?

### 02:15:46 · Speaker 2

Okay fine. So this is

### 02:15:48 · Speaker 3

how you define the the

### 02:15:53 · Speaker 3

non-Markovian process. Okay, now you define the corresponding, I mean, as you see, all of these are are known, right? I mean, there is nothing to learn. The model similar to the previous case, define the define

### 02:16:10 · Speaker 2

reverse process

### 02:16:18 · Speaker 2

reverse or the denosing process.

### 02:16:24 · Speaker 2

Correspondingly

### 02:16:37 · Speaker 2

follows. So what do we need? We simply need a P theta

### 02:16:41 · Speaker 3

of

### 02:16:45 · Speaker 3

xt minus one given xt, right? Define that to be for t equal to one, it is a normal distribution.

### 02:16:57 · Speaker 3

similarly at mean mu theta and variance sigma i okay at different other t that is equal to q phi of

### 02:17:07 · Speaker 3

xt minus one okay given xt

### 02:17:13 · Speaker 2

and instead of x not what we have is

### 02:17:29 · Speaker 2

Yeah, you can call that as

### 02:17:32 · Speaker 3

Let's not call it. We can call it as mu theta only.

### 02:17:37 · Speaker 3

this is the estimated mu theta. Let us call the estimated x not as some f theta.

### 02:17:48 · Speaker 3

function of x t, okay? This is what we define it. Where, uh

### 02:17:57 · Speaker 3

we know that our x not is given by x t minus root of one minus alpha t into epsilon divided by root of alpha t bar. It is what we have. Right? So in the this is in the forward process.

### 02:18:24 · Speaker 3

in the reverse corresponding reverse process, we'll call the f cheat of x which is an estimate of x not to be equal to

### 02:18:35 · Speaker 3

xt minus

### 02:18:38 · Speaker 3

just like we did it with DDPMs, we have a similar thing with DDIMs. Instead of epsilon, you have

### 02:18:45 · Speaker 3

epsilon theta cap, right, which is the estimated epsilon divided by alpha t bar.

### 02:18:51 · Speaker 2

That's all. This is in the reverse process.

### 02:19:00 · Speaker 2

Okay. Okay. So now

### 02:19:02 · Speaker 3

with this what can be shown is see I am skipping the proof because it's sort of like straight forward in the sense that if you look at the DDIM paper you will get that and also it's not like very relevant to what we are doing what can be shown is with the

### 02:19:24 · Speaker 2

ago models

### 02:19:33 · Speaker 2

the elbow, okay?

### 02:19:37 · Speaker 2

will come out to be

### 02:19:45 · Speaker 2

the same as that of D D P M.

### 02:19:55 · Speaker 2

This is what the

### 02:19:56 · Speaker 3

the take home message is that when you are training a DDPM, okay? you are also implicitly training a large class of non-Markovian models with these particular distributional forms.

### 02:20:12 · Speaker 2

Does it make sense?

### 02:20:24 · Speaker 2

Hello. Is that clear? So what I'm saying is,

### 02:20:28 · Speaker 3

When you train one DGPM, okay, with the procedure that we just saw, you're actually training a gamut of, right, of infinite models, non-workover models with this particular distribution that we...

### 02:20:46 · Speaker 1

Next slide

### 02:20:47 · Speaker 3

That's why they name denosing decision implicit models because you are implicitly training so many models while you are training one DT.

### 02:20:57 · Speaker 3

So this implies what does this imply? This implies

### 02:21:00 · Speaker 2

start

### 02:21:07 · Speaker 2

the training procedure

### 02:21:18 · Speaker 2

and loss

### 02:21:28 · Speaker 2

of the same

### 02:21:36 · Speaker 2

or

### 02:21:38 · Speaker 2

both CDPM and URI

### 02:21:48 · Speaker 2

Then you might ask, right, what is the whole point? I mean, like, what are we achieving by doing all this? Right? However, while you're running procedures there, inferences are different, no?

### 02:22:06 · Speaker 2

inference is very different. Right? So how do we infer?

### 02:22:09 · Speaker 3

और डीडी

### 02:22:13 · Speaker 3

P M C, okay? Sampling is from you get X T minus one recursively from P theta of X T minus one given X T.

### 02:22:24 · Speaker 3

which is Gaussian

### 02:22:28 · Speaker 3

What was the

### 02:22:30 · Speaker 2

the distribution of DDPM

### 02:22:36 · Speaker 2

recall it is

### 02:22:43 · Speaker 2

somebody tell me what it is? E theta

### 02:22:46 · Speaker 3

is that

### 02:22:48 · Speaker 3

mu theta right which is x t minus one

### 02:22:53 · Speaker 3

let me not write that it's always x minus one and this this one was

### 02:23:01 · Speaker 3

right the entire thing is what I'm thinking it's a

### 02:23:03 · Speaker 2

Hmm

### 02:23:05 · Speaker 2

huge thing.

### 02:23:12 · Speaker 2

Hold on, let me try to write it.

### 02:23:16 · Speaker 2

Give me a second, I'll write it. I had written it before.

### 02:23:41 · Speaker 2

So what was the mean? Mean was

### 02:23:45 · Speaker 2

XT by

### 02:23:48 · Speaker 2

this minus

### 02:23:53 · Speaker 2

1 minus alpha t divided by

### 02:23:57 · Speaker 3

root of one minus alpha t bar times

### 02:24:03 · Speaker 3

epsilon theta star

### 02:24:07 · Speaker 3

Right. So this was the mean and the variance was uh

### 02:24:14 · Speaker 3

t square times i. Okay. This was in DDP.

### 02:24:19 · Speaker 2

While in DDIMs

### 02:24:32 · Speaker 3

inference procedure change changes which is still sample from P theta of X T minus one given X T but since it is a non Markovian process okay the mean and the variance changes that's all

### 02:24:52 · Speaker 2

Let me write it down the

### 02:24:56 · Speaker 2

mean is given by

### 02:25:05 · Speaker 2

Root of

### 02:25:10 · Speaker 2

alpha t minus one

### 02:25:13 · Speaker 2

alpha bar t minus one times

### 02:25:17 · Speaker 2

the output of the neural network

### 02:25:21 · Speaker 2

Plus

### 02:25:24 · Speaker 2

root of one minus

### 02:25:27 · Speaker 2

alpha bar t minus one

### 02:25:30 · Speaker 2

minus sigma t squared

### 02:25:39 · Speaker 2

times epsilon theta star

### 02:25:44 · Speaker 3

Sigma squared into I

### 02:25:46 · Speaker 3

That's all. Right? So this is what changes. So what changes is that the way the denosing is done, okay? Changes the

### 02:25:59 · Speaker 3

training procedure remains exactly the same as the D D P M, okay? Now, if you make sigma to be zero here, right? With sigma equal to zero, the class of model that you get is such that the encoding process...

### 02:26:19 · Speaker 2

becomes

### 02:26:21 · Speaker 2

deterministic

### 02:26:33 · Speaker 3

Okay, the encoding process becomes deterministic because there is no noise component to it. So now this what does this enable? This enables inversion, okay? Deterministic enable

### 02:26:46 · Speaker 2

ವರ್ಷ

### 02:26:54 · Speaker 2

So what do you mean by that?

### 02:26:56 · Speaker 3

a particular X not which is a data sample okay what you could do is you could run the forward process okay that is a deterministic forward process for DDIM and get the corresponding latent vector the noise latent vector which when uh used in the sampling okay or denosing process will generate this exact same sample X not

### 02:27:26 · Speaker 2

Does it make sense?

### 02:27:36 · Speaker 3

All you should do is the following, right? What what is to be done is given an X not, you run the uh the forward process, okay? Uh of the the DDIM and you note that the forward process of DDIM is similar to that of the forward process of TDPM because the conditioners are the same. But because with sigma equal to zero, if you make sigma T equal to zero here and then run the the sampling of DDIM, okay?

### 02:28:06 · Speaker 3

you will get the exact same sample, okay, corresponding to the the input sample. So you start with suppose you start with an image, okay, running the forward process of DDIM will give you a noise sample which when used in the reverse process of DDIM will give you the the input sample, which means that you have encoded or inverted or you've gotten the exact same

### 02:28:32 · Speaker 3

latent variable corresponding to the input image

### 02:28:40 · Speaker 2

is that making sense?

### 02:28:47 · Speaker 2

Hello, am I there?

### 02:28:51 · Speaker 3

Yes sir

### 02:28:52 · Speaker 2

Yes, okay.

### 02:28:55 · Speaker 3

Any questions on this?

### 02:28:58 · Speaker 3

See the the difference between DDPM and DDIM is in the fact that in the sense that uh what you have right as the the forward and reverse processes they would change. They would become non-Markovian processes okay. But because of the way these non-Markovian processes are constructed. They are constructed in such a way that the conditional distributions happen to be exactly the same as the same form as that of DDPM

### 02:29:31 · Speaker 3

which implies that training a DDPM is implicitly training multiple uh DDIMs that are there.

### 02:29:43 · Speaker 3

What is the advantage of that? The advantage is that because

### 02:29:49 · Speaker 3

one of the at one of the uh the values of sigma the the class of models that we have generated become deterministic you can use that for inversion

### 02:30:05 · Speaker 2

Is that clear?

### 02:30:08 · Speaker 2

I will also share a nice

### 02:30:12 · Speaker 2

blog post on this.

### 02:30:29 · Speaker 2

um

### 02:30:34 · Speaker 2

you may ask any questions if you have on the

### 02:30:36 · Speaker 3

time

### 02:30:37 · Speaker 2

then

### 02:30:39 · Speaker 1

So one question so the reason why D D P M's are non invertible is it because the the Markovian processes are non reversible?

### 02:30:48 · Speaker 3

it is not because of that in particular, it is because of the fact that the encoding process involves noise addition, no?

### 02:31:00 · Speaker 3

It is because and in

### 02:31:01 · Speaker 1

and in case of DDIMs

### 02:31:04 · Speaker 3

Yeah, in in the case of DDIMs where sigma equal to zero, the encoding process does not involve noise addition.

### 02:31:14 · Speaker 3

It is simply a function of alpha

### 02:31:19 · Speaker 1

okay. And that's why it is reversible.

### 02:31:23 · Speaker 3

That is why it is reversible, correct. But the thing is, the alphas are designed in such a way that, you know, if you

### 02:31:32 · Speaker 3

keep moving in the forward direction they would still approach a normal zero one okay in the stationary distribution case. however they it's the forward process is not that you take an image and add noise.

### 02:31:49 · Speaker 3

the way they are constructed.

### 02:31:50 · Speaker 1

Okay

### 02:31:52 · Speaker 1

So the forward process is non-Markovian

### 02:31:56 · Speaker 2

Both the forward and reverse processes

### 02:31:58 · Speaker 3

norm or problem

### 02:31:58 · Speaker 2

norm or clean NDD items. Yeah.

### 02:32:03 · Speaker 3

Okay

### 02:32:09 · Speaker 3

Okay, so yeah, see actually what I've asked you is that see you are you will be training one model, okay, which is the D D P M model. But what changes is the inference, right? Inference and the inversion in the case of D D I M. Simply take a pre-trained D D P M, okay, and use it for inversion. I saw a nice Facebook blog on D D I M inversion, I will

### 02:32:37 · Speaker 3

share that with you hold on

### 02:32:40 · Speaker 3

looking for it

### 02:32:43 · Speaker 3

I've asked you to invert, get the noise samples and do an interpolation between those noise samples corresponding to two different images and then do a reverse direction is what I've asked for. uh It's a nice experiment to do. Let me just share that. Hold on.

### 02:32:59 · Speaker 3

Inner

### 02:33:00 · Speaker 2

group I will put it in our group.

### 02:33:09 · Speaker 2

not in the call chat. How do I put it?

### 02:33:14 · Speaker 3

teams

### 02:33:16 · Speaker 1

So you can put it in the call chart itself.

### 02:33:19 · Speaker 3

but that will just go away, no? I don't want that to happen. General.

### 02:33:25 · Speaker 3

right

### 02:33:25 · Speaker 2

No, it will not go away. It will stay there.

### 02:33:29 · Speaker 1

whatever you put here is will come in teams. uh yeah, teams.

### 02:33:33 · Speaker 3

So, okay. Anyway, I just put it in the chat window. Have a look at it.

### 02:33:41 · Speaker 3

Okay, so that's it. In fact, that that's the end of

### 02:33:45 · Speaker 2

what I wanted to do with diffusion models

### 02:34:01 · Speaker 2

See, all these

### 02:34:03 · Speaker 3

these text to image generators, right? They are all diffusion models, okay? They use classifier

### 02:34:12 · Speaker 1

free kind of tuition

### 02:34:13 · Speaker 3

and they are all D D I M's they are not D D P M's because I mean they are in fact training is the same but because the inference has multiple advantages over the D D P M's right what they do is they infer using D D I M's processes not D D P M's processes but all of the state of the art models are the diffusion models okay

### 02:34:36 · Speaker 3

Right, so it's better if I start a new

### 02:34:40 · Speaker 2

Hmm, yes

### 02:34:43 · Speaker 2

thing

### 02:34:46 · Speaker 2

Rupesh

### 02:34:55 · Speaker 2

should I start self-supervised learning in the next class?

### 02:35:04 · Speaker 2

What do you recommend?

### 02:35:09 · Speaker 3

give you the introduction and go over the math in the next class or like we can start in the next class.

### 02:35:16 · Speaker 3

I go with what you say. What what should we do?

### 02:35:21 · Speaker 1

we can have introduction and then the maths in next class maybe

### 02:35:25 · Speaker 3

Sure, then I have to start a new notebook.

### 02:35:32 · Speaker 2

this is uh till eleven I will continue in the same notes next time.

### 02:35:41 · Speaker 2

self supervised

### 02:35:45 · Speaker 2

representation learning

### 02:35:58 · Speaker 3

See these diffusion models right because of their elegance in the sense that all their

### 02:36:03 · Speaker 2

all

### 02:36:04 · Speaker 1

Right

### 02:36:06 · Speaker 1

Sorry, I had a query.

### 02:36:07 · Speaker 2

good

### 02:36:07 · Speaker 3

safe

### 02:36:08 · Speaker 3

Yeah, Goan

### 02:36:09 · Speaker 1

on

### 02:36:10 · Speaker 1

Sir, for the DDIMs everything else remains the same? I mean like how we for the conditional generation and all those things?

### 02:36:10 · Speaker 3

just

### 02:36:19 · Speaker 3

condition and generation everything remains the same. All that which changes is the forward and the reverse process. Even the training procedure does not change. Right? The forward and the reverse process changes. uh the two XT uh the relationship between XT and X not does not change. The relationship between XT and X not that you need for training the model does not change. It remains exactly the same as that of DDPM. But the forward and the reverse process changes which

### 02:36:49 · Speaker 3

means that the sampling has a different equation which I wrote which is different from DDPM okay and the the the

### 02:37:01 · Speaker 3

encoding process has a different equation. Okay. encoding we don't use explicitly. I mean we use it only if we need this inversion thing, right? If you want the corresponding X corresponding latent, latent corresponding to a given image, we have to run through the forward process of DDIM, non-Markovian DDIM. Otherwise, we only need that XT, you know, and the relationship between XT and X not are exactly the same as that of DDPM in DDIM. And the conditioning etcetera. all of them remain exactly the same.

### 02:37:36 · Speaker 1

ओके, थैंक यू.

### 02:37:38 · Speaker 3

Okay. Okay, so let's now switch gears and we will look at self-supervised learning. These are not generative models per se, okay? uh The problem is uh of that of what is called as representation learning. We have actually done it in a slightly different way.

### 02:37:58 · Speaker 3

representation

### 02:37:59 · Speaker 2

Burning

### 02:38:06 · Speaker 2

Okay. So what is the problem? The problem

### 02:38:09 · Speaker 3

given

### 02:38:12 · Speaker 3

some data. I will switch back to our older notation, okay? uh X one through X X N. These are not the intermediate states in diffusion models, okay? I I D, tron from some unknown distribution P X, okay? There are no labels here. Learn a function.

### 02:38:38 · Speaker 3

learn a function f theta, okay? f theta from space of x to some space z, okay? where z the dimensionality of z is typically much lesser than that of dimensionality of x.

### 02:39:00 · Speaker 2

learn a function such that, such that

### 02:39:08 · Speaker 2

downstream tasks, tasks as they call them.

### 02:39:19 · Speaker 2

on on G R

### 02:40:18 · Speaker 2

Yeah, so this is the object
