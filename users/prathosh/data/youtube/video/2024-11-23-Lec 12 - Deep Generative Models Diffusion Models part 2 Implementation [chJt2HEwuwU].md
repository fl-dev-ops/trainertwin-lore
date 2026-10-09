---
id: chJt2HEwuwU
title: Lec 12 - Deep Generative Models Diffusion Models part 2 Implementation
url: https://www.youtube.com/watch?v=chJt2HEwuwU
date: '2024-11-23'
duration: 02:40:23
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# Lec 12 - Deep Generative Models Diffusion Models part 2 Implementation

## Transcript

### 00:00:01 · Speaker 1

xt is given by root of alpha t xt minus 1 plus 1 minus alpha t times epsilon where epsilon is a sample drawn from normal 0 1 and this defines a first order Markov chain is what we saw so starting from a data point you keep projecting it onto the latent space according to this equation this particular equation

### 00:00:28 · Speaker 1

this particular equation and that will quote unquote add noise right that is adding noise and slowly because it's a Markov chain stationary distribution will go to

### 00:00:42 · Speaker 1

Not Mozill and his work we saw

### 00:00:45 · Speaker 1

Now um this encoding uh in processor distribution

### 00:00:52 · Speaker 1

on the tth latent space conditioned on t minus first latent space which happens to be a Gaussian with certain parameters mean and variance that is written here and the corresponding decoded distribution is what we call as the model distribution it is learnable

### 00:01:10 · Speaker 2

Uh

### 00:01:10 · Speaker 1

What you learn is that you learn the decoding distribution, the mean and the variance of the decoding distribution at all times that's t. Now, as we saw later in the lecture that the variance is actually often not learned that is also assumed to be fixed or known. What is learned is the mean of the decoding distribution. Now, how do we do that? We do that using the usual elbow optimization. So, for that we started from the log likelihood.

### 00:01:40 · Speaker 1

the elbow and yeah they did some algebraic manipulations right

### 00:01:51 · Speaker 1

And finally uh what we got was that there was three terms in the elbow one we call it as the reconstructed term where you take the uh

### 00:02:04 · Speaker 1

first latent variable and try to reconstruct the data and the second term is prior matching term okay which was independent of model parameters theta okay and the third term is what we call as the

### 00:02:20 · Speaker 1

Consistency term or denoting matching term okay that is what we call it as the consistency term

### 00:02:30 · Speaker 1

that involved a KL divergence computing KL divergence between two distributions one was this Q XT minus one given XT and X part and the model D or D decoding term P theta XT minus one given XT so note that in the denoising matching term or consistency term right there are two distributions one is the decoding distribution the other is is a sort of reverse of the encoding distribution reverse in the sense that it is

### 00:03:00 · Speaker 1

it's going in the backward direction of xt minus 1 given xt and x0 but yeah so that is known okay but has to be computed it is not trivially known we have to compute that distribution so what we did was we wanted to compute that consistency terms for that we need to compute the known reverse distribution that appears in the consistency term

### 00:03:30 · Speaker 1

and we use Bayes' law right and the fact that all of the involved distributions are Gaussian distributions completed square and finally we yeah so two things one in the while we are computing the

### 00:03:48 · Speaker 1

known term okay known denoising term in the consistency loss component we encounter terms like q of xt given x naught right where uh where xt is the dth latent vector and x naught is the data so now we use recursion to find this q of xt given x naught right uh using this argument and finally q of xt uh given

### 00:04:18 · Speaker 1

x0 still happen to be a Gaussian with parameters denoted by alpha bar x0 and yeah parameterized by alpha bar x0 where alpha bar is the one that is defined here which is a product of multiple on all the alphas till the time t

### 00:04:44 · Speaker 1

So, using that and the fact that all of them that are involved are Gaussian distributions, completed the square and finally found out what this the known denoting matching term was right and we called we called that as a Gaussian distribution. We found out that it was a Gaussian distribution 2 with a mean denoted by this mu cube and the variance denoted by sigma cube ok and

### 00:05:14 · Speaker 1

Sigma Q was simply a function of

### 00:05:20 · Speaker 1

t okay that had nothing to do with any parameters it was a function of t and we wrote that as small sigma q square t times identity and mu q uh was a function of uh x t and x naught okay which can be uh computed which which is known and can be computed okay now having

### 00:05:50 · Speaker 1

PK top

### 00:05:53 · Speaker 1

We have to we can now finally compute the um the learning learning term or consistency term which is a k divergence between two power field distributions okay

### 00:06:12 · Speaker 1

Now, the KL divergence between two Gaussian distributions as a deterministic form, we use that deterministic form which is KL divergence between two Gaussian distributions and finally found out that the D-Noggin matching term will involve difference computing difference between two means, one which is the mean of the

### 00:06:38 · Speaker 1

backward of the decoding distribution mu theta at xt and the other term was the mean of this known denoising term okay mu q computed at xt

### 00:06:52 · Speaker 1

That's what we saw any questions on the so far

### 00:07:05 · Speaker 1

No hope I'm audible

### 00:07:12 · Speaker 2

Yes

### 00:07:17 · Speaker 1

Okay, so then what we did was while we can actually stop here, okay, and we can implement DDPM this way, as I said, you know, in the literature, people don't use this formulation to implement, but they rather reparameterize this particular thing using

### 00:07:44 · Speaker 1

In terms of the epsilon of the noise that is added, that is what is implemented. So we saw that three parameterization as well. So maybe I will do it again.

### 00:07:56 · Speaker 1

it in the last class now let me do it again so we'll assume that we know that the elbow now has a difference between the means of mu q means means mu q and mu theta okay let us take it from there and do it

### 00:08:56 · Speaker 1

Oh

### 00:10:12 · Speaker 2

So are you waiting

### 00:10:24 · Speaker 2

So we have

### 00:10:29 · Speaker 2

It was a kill dev

### 00:10:40 · Speaker 1

Thank you

### 00:10:43 · Speaker 1

xt minus one given

### 00:10:46 · Speaker 2

60 and 6 not

### 00:10:49 · Speaker 2

one distribution the other distribution was

### 00:10:51 · Speaker 1

Other distribution

### 00:10:52 · Speaker 2

Eat here

### 00:10:55 · Speaker 2

It's t minus one t one x t

### 00:11:00 · Speaker 2

This was what it was and we show that

### 00:11:04 · Speaker 2

That's a cute one

### 00:11:08 · Speaker 2

State minus one we one

### 00:11:10 · Speaker 2

X two and it's not

### 00:11:18 · Speaker 2

Gaussian distribution

### 00:11:23 · Speaker 2

mean we call this mu q

### 00:11:26 · Speaker 2

And the variance was sigma cubed

### 00:11:30 · Speaker 2

and mu q

### 00:11:35 · Speaker 2

was a function of xt and x0 so given an xt and x0 you had this mean to be equal to

### 00:11:47 · Speaker 2

Lotta

### 00:11:54 · Speaker 2

alpha t into 1 minus alpha t bar times xt

### 00:12:05 · Speaker 2

alpha t minus one bar

### 00:12:10 · Speaker 2

to one minus

### 00:12:13 · Speaker 2

will part t into x

### 00:12:18 · Speaker 2

rewritten by

### 00:12:21 · Speaker 2

One minus

### 00:12:24 · Speaker 2

for T bar see note that

### 00:12:26 · Speaker 1

The denominator is actually a constant, it's a scaling factor. So basically, it's a linear.

### 00:12:32 · Speaker 2

combination of XT and X naught that is what this new Q is right

### 00:12:36 · Speaker 1

So I'll

### 00:12:38 · Speaker 2

Now if you recall using a recursion we showed that the th latent variable x t okay can be represented in terms of

### 00:12:50 · Speaker 2

alpha t bar okay

### 00:12:55 · Speaker 2

presented in terms of x naught right alpha t bar into

### 00:13:01 · Speaker 2

It's not

### 00:13:05 · Speaker 2

root of 1 minus alpha t bar into epsilon

### 00:13:13 · Speaker 2

Do you remember this? So we used recursion and showed that Xt can be showed in terms of X0 and the noise added epsilon, correct?

### 00:13:27 · Speaker 2

Put this in place

### 00:13:29 · Speaker 2

that now mu q

### 00:13:33 · Speaker 3

No it's not stuck

### 00:13:35 · Speaker 1

It's lagging I guess

### 00:13:43 · Speaker 2

Hold on see let me do one thing let me just use my phone internet to connect huh that should be better give me a second

### 00:16:04 · Speaker 2

Do you see the screen now

### 00:16:19 · Speaker 1

Oh what's happening

### 00:16:22 · Speaker 1

Just change my internet to my phone internet

### 00:18:14 · Speaker 2

Yeah please tell me if you can see the screen

### 00:18:18 · Speaker 2

There we go

### 00:18:23 · Speaker 2

visible

### 00:18:24 · Speaker 4

Yes

### 00:18:25 · Speaker 2

Only it works

### 00:18:36 · Speaker 2

Yeah sorry about this as I said I've come to my hometown and

### 00:18:41 · Speaker 2

Internet is not my standard one

### 00:18:47 · Speaker 4

Some issues oh so uh

### 00:18:52 · Speaker 4

what they were doing is that expressing this mu q okay in terms of

### 00:19:02 · Speaker 4

It's not an

### 00:19:03 · Speaker 2

This mu q now can be expressed in terms of x0 and epsilon. So this is the recursion that we wrote. Sorry, xt is expressed in terms of x0 and epsilon. Which means that I can write

### 00:19:42 · Speaker 4

root of alpha r t minus

### 00:19:46 · Speaker 4

into 1 minus alpha t

### 00:19:48 · Speaker 2

Okay, now this implies that here I can write x naught.

### 00:19:56 · Speaker 2

in terms of x t and epsilon right x t minus root of 1 minus alpha t bar times epsilon divided by alpha t root of alpha t bar right so which means that this x naught which is there in u q I can replace that with

### 00:20:17 · Speaker 2

thing now xt minus root of 1 minus alpha t bar into epsilon divided by root of alpha t bar right this entire thing divided by

### 00:20:32 · Speaker 2

1 minus alpha t bar

### 00:20:35 · Speaker 2

Right, so I can, I mean, what did I just do? Xt can be reparameterized in terms of X naught and epsilon, which means that X naught can be written in terms of Xt and epsilon. So mu Q now, the X naught in mu Q now can be written in terms of Xt. That is what was done. So I will skip the algebra. If you rearrange the terms and group them and modify, what will happen is, finally, the mu Q,

### 00:21:12 · Speaker 2

can be expressed

### 00:21:18 · Speaker 2

One way

### 00:21:20 · Speaker 2

to alpha t

### 00:21:23 · Speaker 2

into xt minus 1 minus alpha t divided by root of 1 minus alpha t bar

### 00:21:36 · Speaker 2

into root of times

### 00:21:43 · Speaker 2

Yeah, so this is simply by rearranging the terms above.

### 00:22:05 · Speaker 2

That should be okay right I mean what we did was we uh

### 00:22:12 · Speaker 2

mu q was written in terms of

### 00:22:17 · Speaker 2

X t and epsilon. That's all right.

### 00:22:21 · Speaker 2

Now recall that

### 00:22:27 · Speaker 2

p theta of xt minus one

### 00:22:31 · Speaker 2

P1 XT the one that we had

### 00:22:35 · Speaker 2

What was that we assumed it to be a Gaussian

### 00:22:40 · Speaker 2

a mean mu theta and variance was exactly equal to sigma q right we didn't want to change the variance the mean was mu theta

### 00:22:53 · Speaker 2

Right now this mu theta now

### 00:22:59 · Speaker 2

can be expressed as follows

### 00:23:19 · Speaker 2

minus divided by 1 minus

### 00:23:25 · Speaker 2

40 bar

### 00:23:30 · Speaker 2

into some epsilon theta

### 00:23:36 · Speaker 2

Okay, so now this is something which is subtle. If you understand this, then we are done. Okay, so what did we do? We express the mean, okay, of the decoding distribution.

### 00:23:49 · Speaker 2

In terms of XT and some epsilon theta cap, okay, that is to be learned. We'll say that is epsilon theta cap.

### 00:24:11 · Speaker 2

Not clear

### 00:24:14 · Speaker 2

So what did we do here We note that

### 00:24:18 · Speaker 1

Uh

### 00:24:21 · Speaker 2

Any Gaussian distribution, right, can be expressed in terms of any other Gaussian distribution just by scaling and shifting, correct? Do you do you agree with me on that?

### 00:24:36 · Speaker 2

So that is reparameterization, right? So you if you are given a particular Gaussian distribution, you can always scale and a sample from a particular Gaussian distribution, you can always scale and shift the sample of that particular Gaussian distribution to make it into any other Gaussian distribution. Do you agree?

### 00:25:05 · Speaker 2

Hello am I audible

### 00:25:09 · Speaker 3

Yes yes so it's audible yes yeah

### 00:25:11 · Speaker 2

So you agree with what the statement that I made right can be expressed in terms of any other Gaussian distribution

### 00:25:14 · Speaker 3

Yeah

### 00:25:18 · Speaker 2

Now this p theta of x3 minus 1 given xt is a Gaussian distribution with a certain mean mu theta. Okay. So what we did was we just represented that mean in terms of xt, right, which is a constant, right, and some sample from a Gaussian distribution, epsilon theta cap with some scales and shifts.

### 00:25:43 · Speaker 2

I can always find an epsilon theta

### 00:25:47 · Speaker 2

Mm

### 00:25:49 · Speaker 2

Which when scaled by this particular scaling factor and shifted by 1 by 1 by root of alpha t times x t will give back my mu theta. Do you agree? So what I'm trying to say is if you scale and shift a particular Gaussian distribution, right, you can always learn the scale and shift factor so that you can get back to the original Gaussian distribution. Is that is that all right?

### 00:26:23 · Speaker 2

So why I mean then the next question is why did we even have to like introduce these random scale shapes? This is just to make the loss function look nice. That's all Okay, so there is in fact, you know, I can just write this as mu theta and mu q minus mu theta can be written as this this entire mu q that we have minus mu theta, right? It doesn't matter but people generally write it this way to ensure that the final loss function that you see has a nicer form to see

### 00:26:53 · Speaker 2

that's all there is no other sanctity to this and what i am simply doing is

### 00:27:00 · Speaker 2

I mean, deliberating all the learnable things on a scale and shift into this epsilon theta. That's all. Okay. So with this, what will happen is the loss that we had, no, the KL divergence between

### 00:27:15 · Speaker 2

2 of xt minus 1

### 00:27:19 · Speaker 2

You can XT and X not

### 00:27:25 · Speaker 2

Too dark

### 00:27:27 · Speaker 2

X t minus one will give an X t e

### 00:27:32 · Speaker 2

simply became let me just write proportional to because generally the constants are ignored they became proportional to this was initially uh we had a sum here from t equal to 2 to capital T

### 00:27:49 · Speaker 2

mu q which was a function of xt and x not and there was mu theta

### 00:27:57 · Speaker 2

which is a function of

### 00:28:01 · Speaker 2

60 and a T

### 00:28:04 · Speaker 2

p because there is an alpha t there okay this is what the last term was and this we saw was now equivalent to

### 00:28:19 · Speaker 2

All terms being equal, let's call this as epsilon t. Okay, I think this is better to write this as epsilon t because the tth sample, right, I mean tth noise sample that was drawn to make x naught xt.

### 00:28:35 · Speaker 2

Easier to understand, okay? This is around T, and you have.

### 00:28:43 · Speaker 2

Epsilon chi dot

### 00:28:48 · Speaker 2

just to make it look this elegant no this mu q i'm sorry mu theta was reparameterized in terms of xt and those constants finally this is what

### 00:29:00 · Speaker 1

It's done

### 00:29:03 · Speaker 2

this all right so when you are implementing a diffusion model right a DDPM all you have to do is implement this loss function so this becomes a regression problem right so this is a regression over epsilon t let me explain that more

### 00:29:22 · Speaker 2

Decrision over epsilon t

### 00:29:26 · Speaker 2

Any questions so far? How did we get there? Get here before I move to the implementation nuances?

### 00:29:42 · Speaker 2

So am I audible any questions here

### 00:29:53 · Speaker 2

Are you there We are here with you

### 00:29:57 · Speaker 3

Yes sir we if you're audible yes we are hearing this

### 00:30:00 · Speaker 2

Oh, no questions? Okay. Right. Okay. So this is what it becomes. So now the next thing is how do we implement this in practice?

### 00:30:12 · Speaker 2

Implementation

### 00:30:22 · Speaker 2

So it's basically training of the DPM

### 00:30:36 · Speaker 2

So now what are we given? So given, I will show it for one data sample. No, you have to do it again in batch. Given it's not, this is a sample from the data distribution.

### 00:30:57 · Speaker 2

True theta distribution

### 00:31:03 · Speaker 2

What is to be done is that

### 00:31:11 · Speaker 2

So first what you'll do is

### 00:31:16 · Speaker 2

ample

### 00:31:19 · Speaker 2

T okay uniformly between 2 and capital T so what is done in practice is the sum that you see here no from T equal to 2 to capital T people don't do it on like all T's and take a sum of it they do a uniform sampling of some some subset of T between 2 and T and then do it okay so typically it's not they don't take all T's because of computational

### 00:31:49 · Speaker 2

complexity some t is taken okay sample t uniformly between 2 and capital T okay and you obtain

### 00:32:00 · Speaker 2

X T okay

### 00:32:05 · Speaker 2

And if you also have the alpha one

### 00:32:15 · Speaker 2

set alpha 1 alpha 2 up to alpha capital T okay so you fix this so typically it is fixed at

### 00:32:27 · Speaker 2

The schedule that

### 00:32:30 · Speaker 2

0.98 and so on 0.9 okay uh this is again this is an example but yeah so you could set alphas this way and you obtain xt uh using this equation right square root of alpha t bar times x naught plus 1 minus alpha t bar into some epsilon t where epsilon t is a sample from normal zero

### 00:32:59 · Speaker 2

with me so far so given an x naught so you have x naught is let's say that x naught is a particular image you take an x naught and you sample uh sorry you get some t okay let's say that we are doing it for one particular t okay uh you take a t

### 00:33:21 · Speaker 2

a bad code okay so you sample a t uh from uh 2 to capital t and you set alpha 1 to alpha uh capital t to be some constant okay and you obtain xt uh using this equation where epsilon t is some sample from normal zero is this all right so far

### 00:33:46 · Speaker 2

Okay so once you have this what you do is the following that you build construct

### 00:33:56 · Speaker 2

Structure neural network

### 00:34:02 · Speaker 2

parameterized by theta okay so this neural network typically will have this architecture which is called the

### 00:34:17 · Speaker 2

Okay, so now it is called unit because note that finally what we need is a regression over epsilon theta

### 00:34:28 · Speaker 2

Right, because our last function is this, right? We want an estimate of epsilon t. Now, we know that the dimensionality

### 00:34:41 · Speaker 2

The dimensionality of epsilon t is actually d which is the data dimensionality

### 00:34:48 · Speaker 2

Now, when you have regression tasks, okay, where the output is same as that of the input, and especially when you are using image kind of data, the standard architecture that is used is this sort of an architecture which is called unit. The name unit is given to this is because it looks like a U, right? U, I.

### 00:35:16 · Speaker 2

You start from the dimensions, okay keep reducing the dimensions

### 00:35:22 · Speaker 2

then you come to some bottom like d dash and then you increase the dimensions and finally you get back to the d dimensions you know that's why the name unit okay so now what does this take as an input so you please note here that the mu theta that we had in fact this epsilon

### 00:35:42 · Speaker 2

theta cap now will also become a function of xt right and t obviously right because that is the scale and shift and uh that's what it a function of mu theta was a function of xt and t and when I just reparameterize that in terms of some epsilon theta cap that also becomes a function of xt and t right so now this unit will take xt which we have obtained and t as an input okay and it is supposed to

### 00:36:12 · Speaker 2

output epsilon theta cat which is an estimate of epsilon t that we have used to get xt. What is the last function? The last function is simply the difference between note that both of them are vectors of size

### 00:36:31 · Speaker 2

We can easily compute this

### 00:36:38 · Speaker 2

That's all. So this is the loss function. You need to compute the gradient of this with respect to theta and then back up of it. So this is all it is, right? I mean, you do it for multiple t's.

### 00:36:52 · Speaker 2

In fact, I mean, ideally, you should do it for t equal to 2 to capital T. Typically, what is done is, I mean, t is fixed to some thousand, right? Thousand or two thousand is what is done. So instead of taking thousand XTs, people typically take some 50 XTs for a given X naught, okay? And then try it. And again, well, you take another sample X naught, input sample X naught, and you sample some other subset of T and do this.

### 00:37:23 · Speaker 2

Now how do you give T as an input to this unit is something that I'll talk about in a while. But yeah so other than that is the training procedure for DDPM clear. See one other thing that is to be noted is unlike in VAEs and GANs right where

### 00:37:41 · Speaker 2

The final inference happens to be just a forward pass through the network that you have trained here

### 00:37:51 · Speaker 2

The inference is not through this network. We will see that in a while. What I'm saying is this network will not give you a new sample from the data distribution. Do you see that?

### 00:38:05 · Speaker 2

Unlike in a GAN and a VAE where you just take a Z right and pass it through the decoder or the generator you get a sample from the input distribution right and you sample from the input distribution that does not happen in IDDPM. So I will also talk about how to do inference in IDDPM in a while but is the training procedure clear? This is what you are supposed to implement in your assignment so let me know if this makes sense otherwise I can explain more.

### 00:38:36 · Speaker 4

Sir when we are taking a x naught sorry I have a question so can I

### 00:38:46 · Speaker 4

Can I go ahead with the question

### 00:38:48 · Speaker 1

Yeah

### 00:38:50 · Speaker 4

So when we take a X naught, the T for every X naught, the T has to be a fixed length, like the sample that we are taking.

### 00:39:01 · Speaker 2

what do you mean by that see uh you take one x naught right one extra suppose you are doing this on some data set right some image data set x naught is one sample from the data set one image

### 00:39:16 · Speaker 2

You take one image for that one image you get all the noisy versions latent versions x1 x2 x3 x4 and so on

### 00:39:28 · Speaker 2

For each of them you do one one training through this unit

### 00:39:40 · Speaker 4

Is it one or more than one for for a given data point?

### 00:39:47 · Speaker 2

See for a given data point x naught you get uh one uh sorry for one xp you do one forward pass one backward pass

### 00:40:00 · Speaker 3

Okay and t is we take multiple for a given x model

### 00:40:04 · Speaker 2

Now because the last function has the sum across all t's no

### 00:40:10 · Speaker 3

But here we we don't take all these but we take some samples from two to t

### 00:40:15 · Speaker 2

practice yeah in practice capital D is see capital D is fixed at thousand okay but while training you do a random sampling uniform sampling between two and thousand and do it that is how it is done this is for one X naught and you need to do it for all data sets all data points now that will that will be one epoch so typically what is done is you do it on batches you take a batch of X naught

### 00:40:41 · Speaker 2

Great and for

### 00:40:44 · Speaker 2

Excuse me, so take a batch of X naught and for each of the samples in X naught, you do a sampling of certain t's, okay, and find those X t's and do a forward pass and a backward pass for this entire batch and you do another batch of samples, you take another batch of samples from the data set and iterating over the entire data set will give you one epoch and you do multiple epochs of training, usually training.

### 00:41:14 · Speaker 2

Yeah

### 00:41:14 · Speaker 3

And epsilon epsilon t is just a sample from a normal zero I

### 00:41:18 · Speaker 2

Yes, epsilon t is always a sample from normal 0. That's all. So for you when you obtain xp, you take one sample from normal 0. In the last class, we saw that no, it is simply one sample from normal 0, 1. But the the the information about t is encoded in this alpha bar because alpha bar is product of all alphas from 1 to t, isn't it? You have to actually there is one other step here. You have to compute alpha bar t, right?

### 00:41:48 · Speaker 2

the product of equal to one two three alpha i this is how we define alpha bar no for every t you have to define alpha bar this way and get an xt then pass it through the unit predict whatever is coming compute the loss back propagate

### 00:42:11 · Speaker 2

Any other questions on training

### 00:42:15 · Speaker 2

As I said this is what you are supposed to implement right so

### 00:42:28 · Speaker 2

Okay, if it's clear then there is one other question that is to be answered is

### 00:42:33 · Speaker 1

How do we uh give this time d right as an input to the unit

### 00:42:40 · Speaker 1

Yeah let's go home to

### 00:42:52 · Speaker 1

Now which is a scalar right

### 00:42:59 · Speaker 1

An input

### 00:43:07 · Speaker 1

neural network okay

### 00:43:12 · Speaker 1

Now what can be done is note that T E right is is one dimensional it is scalar right

### 00:43:21 · Speaker 1

one dimensional scalar so typically what happens is if you create an image at p and concatenate the speed which is a scalar

### 00:43:33 · Speaker 1

a one-dimensional scalar with this p what happens is the neural network will offer none of the p because it's a unidimensional scalar it will be simply ignored so for that what is done is one-dimensional and

### 00:43:52 · Speaker 1

He usually ignores

### 00:44:01 · Speaker 1

If concatenated or when concatenated with a very high dimensional vector

### 00:44:16 · Speaker 1

Okay I'll connect it with a

### 00:44:19 · Speaker 1

I'm not sure

### 00:44:27 · Speaker 1

So in this case this is XTE which is an image right

### 00:44:34 · Speaker 1

Some uh some data. Okay, so now for that, what is done is

### 00:44:44 · Speaker 1

Why

### 00:44:47 · Speaker 1

able scenario

### 00:44:55 · Speaker 1

for the scaler

### 00:44:58 · Speaker 1

is converted into a vector.

### 00:45:09 · Speaker 1

Okay, P is converted into a vector and then concatenated.

### 00:45:20 · Speaker 1

Okay there's a name for this do you know what this is called

### 00:45:29 · Speaker 1

Positional embedding

### 00:45:32 · Speaker 1

This positional embedding it's a high sounding name. It's nothing but converting this p which is a scalar right into some vector okay, so what is done is p is converted into some p cap where

### 00:45:51 · Speaker 1

T is a scalar, okay? Now T cap is in some D dimension. So that is what the idea of positional embedding is, right? P is a function that would take P and project it onto T cap. So how is it done? There are multiple ways. One usual way that is used both in the transformers and

### 00:46:17 · Speaker 2

diffusion models is what is called as the sinusoidal embedding

### 00:46:30 · Speaker 2

I will just give you the idea of this you can go and look at the details on this is like lot of blocks etc it's not not at all difficult what is done is construct sinusoids okay of multiple frequencies

### 00:46:50 · Speaker 2

Oh the entire thing okay

### 00:46:55 · Speaker 2

The next one is that's a higher frequency

### 00:47:05 · Speaker 2

And so on okay

### 00:47:10 · Speaker 2

Okay, now this, how many sinusoids are there? There are

### 00:47:20 · Speaker 2

d number of sinusoids construct d number of sinusoids and what you'll do is that at every t so this is the time axis

### 00:47:37 · Speaker 2

time axis so at every t so it is just t equal to 1 t equal to 2 t equal to 3 and t equal to capital T at every t you just sample the value of this sinusoid at this particular value that is all it is

### 00:48:01 · Speaker 2

This is a t equal to one let t equal to two let t equal to three and so on

### 00:48:12 · Speaker 2

Do you see what is happening now this p cap

### 00:48:17 · Speaker 2

Okay, at a particular t, so p cap at a particular t, okay, is a vector of dimensions d, okay, where every component is sine of some fixed frequency. So you have a fixed frequency that's a function of t, okay. Let me just call this as two.

### 00:48:47 · Speaker 2

pi times B

### 00:48:54 · Speaker 2

D is fixed no so let me call it as some

### 00:49:00 · Speaker 2

i.e.

### 00:49:02 · Speaker 2

divided by D

### 00:49:06 · Speaker 2

Oh

### 00:49:11 · Speaker 2

And then you have uh

### 00:49:14 · Speaker 2

The second component is cyn

### 00:49:18 · Speaker 2

2 pi times 2 divided by t you have like sine 2 pi

### 00:49:28 · Speaker 2

Uh one two three

### 00:49:35 · Speaker 2

T by D

### 00:49:41 · Speaker 2

Right? So this is at, okay, there should be a dependence on D also here. Yeah, dependence on T, okay.

### 00:49:53 · Speaker 2

This is a tab particular d I can put a d here also yeah

### 00:50:02 · Speaker 2

this all right I mean do you get the idea what's happening so what is happening is for a given T okay so basically you want to convert a scalar into a vector like how do you do that is that you just take construct like these sinusoids if you want to convert that into a d dimensional space you construct these sinusoids okay of different frequencies and at every T you take a snapshot of all these sinusoids so you'll get

### 00:50:32 · Speaker 2

a d dimensional vector at every t so now you converted a scalar t into a vector a t dimensional vector at all t's

### 00:50:42 · Speaker 2

Is this alright

### 00:50:44 · Speaker 3

So the sequences have to be

### 00:50:44 · Speaker 1

If you want to

### 00:50:46 · Speaker 2

Come again

### 00:50:47 · Speaker 3

The frequencies have to be harmonics or it can be any frequency

### 00:50:52 · Speaker 2

Yeah, yeah, generally they are taken to be harmonics. In fact, I think, I mean, that's why, you know, I don't remember the exact details. I think in the typical sinusoidal embeddings, what is done is for even t's, I think they take a sinusoid and for odd t's, they take cosines, I suppose, just to intersperse. There is a sine and a cosine and you convert it into a data dimensional vector.

### 00:51:21 · Speaker 2

You can go and look at the exact equations that are used, no? But this is the fundamental idea of what sinusoidal potential embedding does. This is OK? Any questions?

### 00:51:37 · Speaker 3

So that we are defining that vector

### 00:51:38 · Speaker 4

Right, it means like comma in between each sign, just to

### 00:51:44 · Speaker 1

Uh sorry I missed it what did you say

### 00:51:48 · Speaker 4

Sir, we are defining T cap as a vector, right? So it's a sine 2 pi T by T comma. I mean, like those are terms of that vector, right?

### 00:51:58 · Speaker 1

Yeah yeah

### 00:51:58 · Speaker 4

Yeah yeah

### 00:52:00 · Speaker 1

These are different terms. Yeah, it's a vector, I just said space. These are different.

### 00:52:07 · Speaker 1

vector yeah see look at this one this t cap is in d dimensions right i mean t is a scalar t cap is in d dimensions

### 00:52:16 · Speaker 1

So in a transformer also right all these GPT etc kind of models when the tokens are given as input these things are also concatenated because a naive transformer does not have the idea of time right so to ensure that the sequential nature of that is preserved this is also given as an additional input same thing is done in this this thing also right when you implement I mean there are standard implementations of sinusoidal positional embeddings in PyTorch you just take that and

### 00:52:46 · Speaker 1

concatenate that in fact there is one other thing that is done these are additional improvisations over the architecture that depends on oh my god what happened

### 00:53:01 · Speaker 1

It comes to big things

### 00:53:10 · Speaker 1

So some of the improvisations are done over this where what is done with, right? Instead of concatenating this T here, there are, this unit typically will have this thing called skipped connections, okay?

### 00:53:27 · Speaker 1

what is done is uh there are connections of this sort where you take the the uh

### 00:53:36 · Speaker 1

intermediate hidden layer and connect it to the corresponding layer at the reflection. I mean, it actually looks like a reflection, right, along this. So, so you connect the corresponding dimensions using a script connection just as you do in do with ResNet. Okay. Now, what is done is that at every of these different dimensions,

### 00:54:05 · Speaker 1

P is concatenated P the vector P is concatenated all of these

### 00:54:12 · Speaker 1

So this is how I think in one of the improvised architectures this is how this unit is implemented

### 00:54:21 · Speaker 1

in your assignment uh you don't have to do this all you can do is just take a t okay uh take the corresponding uh sinusoidal embedding concatenate that with xt and just appropriately give it as an input but if you can right this would be a better way to do it when you have skip connections in fact doing skip connections in pytorch is is not difficult uh you can ask tes to help you out with that and with every skip connection that you do right from uh

### 00:54:51 · Speaker 1

to a pair of layers you concatenate T with that that is how it is typically done

### 00:55:02 · Speaker 1

Any questions on this

### 00:55:04 · Speaker 3

Is that a one

### 00:55:07 · Speaker 4

uh yes i'll go ahead so when you concatenate t to the other layer so the dimension is uh less than d or uh how do you

### 00:55:18 · Speaker 1

It is less than d you have to appropriately take care of the dimensions

### 00:55:24 · Speaker 4

Okay so so the Ts will be generated differently for each uh at each layer or so

### 00:55:30 · Speaker 1

No no no you take the same T but the dimensionality have to be appropriately taken care of that's all

### 00:55:37 · Speaker 1

That's okay no

### 00:55:39 · Speaker 4

So we just

### 00:55:39 · Speaker 1

We just have to reshape each layer

### 00:55:44 · Speaker 1

You have to appropriately reshape at every layer

### 00:55:48 · Speaker 3

I had the similar question so because uh unit the input layer would be some convolution layers right

### 00:55:54 · Speaker 1

Oh

### 00:55:55 · Speaker 3

How do we append the key to the data where because that's not really part of the image right

### 00:56:02 · Speaker 1

That's not part of image that is why what is done is XT is not concatenated at the input layer. So what is done is after the first convolutional layer, okay, you take the output of the first convolutional layer, concatenate T, okay, appropriately reshape and then use the next layer. That is how it is done.

### 00:56:30 · Speaker 1

Okay

### 00:56:30 · Speaker 3

And any particular reason why we are using unit here I mean why do we have to create this bottleneck

### 00:56:37 · Speaker 1

otherwise no uh like xt and epsilon theta have the same dimensions right what sort of neural network do you use

### 00:56:49 · Speaker 3

So so at at uh at the bottom it has to be um

### 00:56:50 · Speaker 1

at the bottom it has to be coming x you have to do it like this right now what will happen is x t has the same dimensions and you can you have to maintain the exact same dimension here and then get the epsilon theta right see that would the you will run into the problem of uh not learning it well because you might get into identity

### 00:57:12 · Speaker 1

Then you have to reduce the dimension, start from xt and reduce the dimension. If you reduce the dimension, you will not get epsilon theta. You'll have to get to epsilon theta. Then you have to again increase the dimension, right?

### 00:57:23 · Speaker 1

So that will make the architecture a naturally unit kind of architecture

### 00:57:33 · Speaker 1

Any other questions? See, I today I don't, as I said, no, I don't have my multiple screens. So, uh, you mean you, I don't, I can't call, call out name. So please unmute yourself and ask questions. Huh? I'll just answer them.

### 00:57:48 · Speaker 3

So just to correlate in conditional can we use like one hot vector that embedding so is that very similar to this one

### 00:57:57 · Speaker 1

Yeah but see I've still not talked about conditional generation I will talk about conditional generation in a while it is done very differently in a diffusion model

### 00:58:06 · Speaker 3

I know I'm talking about glands

### 00:58:09 · Speaker 3

Against in gain conditional gains

### 00:58:13 · Speaker 1

Understand, but see, don't confuse this, uh, this concatenating this P with, uh, I mean, as concatenating a class information, that is not what it is. We are still doing unconditional generation. Okay. Okay. We will do conditional generation in a while. I will talk about that. Uh, like we will discuss that in a while. But yeah, so it is similar in spirit to concatenating that one hot vector, but please be, uh, like, uh, aware of the fact that this P is not

### 00:58:43 · Speaker 1

T is not having any class information here okay it is having the time information because there is a temporal evaluation of the encoding process here right this T is having that time information it does not have any class information

### 00:59:08 · Speaker 3

So one more point so with this time information what we are I mean what we want the model to learn is at any given time step how to do the denoising is that understanding correct

### 00:59:23 · Speaker 1

So yeah, of course, see this, look at it, no, what this unit is actually doing is given a noisy input, okay, at time t, it is trying to tell you what was the amount of noise that was added to make x naught noisy.

### 00:59:41 · Speaker 1

So epsilon theta is an estimate of that no the amount of noise because that is what you are regressing over

### 01:00:00 · Speaker 1

Any other questions So now I think you can implement it right

### 01:00:09 · Speaker 1

Yeah. Okay. So let us move on quickly then. So this is about training. Let me talk about inference in DDPM. Suppose you have after you have trained this, how do you generate images? Okay. Let us look at that.

### 01:00:22 · Speaker 1

we will talk about conditional generation and then we'll go to DDIMs. Okay, so this is inference with DDPMs.

### 01:01:01 · Speaker 1

Okay so what are we given so we are given

### 01:02:42 · Speaker 1

So this is what we should do. We have a trine network, epsilon theta, I mean say theta star, okay, that would take xt and give you epsilon theta. So now what we need to do is we need to sample from xt, p theta of xt minus 1 given xt, okay. So let us do that. We have to do it iteratively now.

### 01:03:07 · Speaker 1

This is where one uh

### 01:03:11 · Speaker 1

One of the drawbacks of DDPM comes you know the sampling is very very slow because we have to start from t equal to capital T and go all the way till

### 01:03:23 · Speaker 1

Uh t equal to one let me write that

### 01:05:20 · Speaker 1

that's it so it's it's pretty simple see what is happening is the following right what do we need to do is we need to sample from this distribution p theta of x t minus 1 given x t right so what is p theta of x t minus 1 given x t it's a normal distribution with mean equal to mu theta and variance equal to sigma t right so what is what is mu theta mu theta is simply this x t divided by root of alpha t minus 1 minus alpha t this thing into epsilon

### 01:05:50 · Speaker 1

theta okay is that okay so now how do we get a sample from a Gaussian distribution with a particular mean and variance we know reparameterization sample from a zero mean unit variance Gaussian right and

### 01:06:06 · Speaker 1

shift it right with whatever mean you want and scale it with whatever variance you want that is exactly what we are doing here

### 01:06:15 · Speaker 1

So sample from a zero mean unit variance covariance okay and this is the shift that you do to get that mu theta so this entire thing

### 01:06:29 · Speaker 1

entire thing right is mu theta that's all just shift it with mu theta and this is again you have the sigma q right which is the variance that we are using and you get xt minus 1 and where are we using the unit here so the trend unit

### 01:06:53 · Speaker 1

So this will take xt at every time, okay? And this will give you epsilon theta star, which is used for sampling. You start from x capital T, past this, you get x capital T minus one.

### 01:07:09 · Speaker 1

So then you take x capital T minus one, pass through this network, get an epsilon theta star at that T, right? And then keep doing it till you get x naught. This will give you a generated sample.

### 01:07:25 · Speaker 1

Is this all right? This is how you do sampling. See, as I said, unlike in a GAN, right, or a VAE, where doing one forward pass through the network that is trained will give you a sample which is needed, this is not the case. So here, to generate one data sample, okay, you need to do capital T number of forward passes. That makes this DDPM very slow.

### 01:07:55 · Speaker 1

very slow if you have seen these things like you know stable diffusion and all that right when you give a prompt you will have to wait for a while you generate the sample that is because it is doing these t number of forward passes through this network

### 01:08:11 · Speaker 1

Any questions on this?

### 01:08:14 · Speaker 1

In maybe

### 01:08:17 · Speaker 1

for this let me know if you have any questions on this

### 01:08:23 · Speaker 3

So I have one question regarding the training of the network itself in the first place. So I mean what kind of issues can we anticipate while training? Just some practical

### 01:08:36 · Speaker 1

ddbm training is not that hard uh i mean that is why these are state of the art generative models right visual visual models these days because they are pretty stable okay uh one thing that can happen is that if you don't sample your t properly then the underlying distribution might not be learned but if you do a good enough sampling i've seen that in our experience these networks actually work pretty well

### 01:09:08 · Speaker 1

Unlike in a GAN right where you have this saddle point problem and you have the mode collapse etc. Those sorts of issues do not generally arise with DDPMs.

### 01:09:22 · Speaker 3

Okay and after how many epochs we can expect uh to get a

### 01:09:26 · Speaker 1

Generation

### 01:09:26 · Speaker 3

One generation quality

### 01:09:27 · Speaker 1

That depends on data sets

### 01:09:30 · Speaker 1

So you can track the loss, right? I mean, this is a regression loss. So whenever the loss is converging and reducing, that is the point where you can perhaps stop.

### 01:09:44 · Speaker 1

Depends on the data set it completely depends on the data set and the architecture how deep your architecture is and there's no answer for that

### 01:09:52 · Speaker 1

Okay so any questions on inference generation

### 01:10:13 · Speaker 1

No questions

### 01:10:21 · Speaker 1

Shall we move on then

### 01:10:35 · Speaker 1

Am I audible Did I

### 01:10:38 · Speaker 1

up down or something hello

### 01:10:41 · Speaker 4

Yes we can

### 01:10:43 · Speaker 1

Let me hope

### 01:10:46 · Speaker 1

So next what we will do is um

### 01:10:54 · Speaker 1

We'll look at how to do conditional generation okay uh guided diffusion

### 01:11:10 · Speaker 4

So before that sir can you give an example where this unconditional DDPM is used?

### 01:11:20 · Speaker 1

Well if you want to build a generative model right where you don't condition it on a particular text or like any prompt or anything you can use I mean you can take any data set and

### 01:11:36 · Speaker 1

generate I mean I didn't get you a question are you asking me for a

### 01:11:42 · Speaker 4

Uh yeah specifically like uh if we give a prompt uh and say like create this uh using a diffusion model that that is a conditional uh diffusion right

### 01:11:53 · Speaker 4

And if it's random, then it's unconditional. Is that correct?

### 01:11:57 · Speaker 1

uh see don't call it as random okay i mean there's nothing random about it i mean the point is if you're sampling from some distribution px then it is unconditional generation if you're sampling from px given y where y is another random variable then it becomes conditional generation

### 01:12:16 · Speaker 4

About it yeah

### 01:12:22 · Speaker 1

Yeah so uh

### 01:13:02 · Speaker 1

Just thinking if I have to like

### 01:13:05 · Speaker 1

that now or just take a break and do it what do you want should we do you need a break or should we complete does it will take me about 20 minutes to complete the guided diffusion shall i complete that and then take a break

### 01:13:26 · Speaker 1

Can let's finish this huh

### 01:13:29 · Speaker 1

Okay see

### 01:13:33 · Speaker 1

While the diffusion models were being developed there was another parallel formulation right for the generative models that came out that was that those were called

### 01:13:48 · Speaker 1

Score based models okay

### 01:13:54 · Speaker 1

So there are multiple variants of score-based models, but all of them converge to DDPM. So let I'll not describe more. I mean, score-based models in detail because they are not a different class of generative models. They are also diffusion models. But yeah, so let me talk about quickly mention score-based formulation. We need this for guided diffusion, meaning conditional diffusion. That's why I'm doing this score-based reformulation.

### 01:14:33 · Speaker 1

Okay now um

### 01:14:36 · Speaker 1

There is a statistical result okay

### 01:14:40 · Speaker 1

That would say that

### 01:14:51 · Speaker 1

Called okay, let me write that now. There is something called result.

### 01:14:59 · Speaker 1

not prove this i'll just state it this is also called the 3d's formula

### 01:15:18 · Speaker 1

It would say that this is a very well known classical historical result that would say that if Z is a Gaussian

### 01:15:27 · Speaker 1

And a variable

### 01:15:29 · Speaker 1

It's mean mu c and variance sigma c okay

### 01:15:39 · Speaker 1

in sigma z then the

### 01:15:45 · Speaker 1

Expectation of

### 01:15:48 · Speaker 1

mu z given z okay expectation of the mean given z is given by z plus

### 01:15:58 · Speaker 1

SIGMA Z times

### 01:16:02 · Speaker 1

Gradient of

### 01:16:04 · Speaker 1

Log off

### 01:16:07 · Speaker 1

E z with respect to z okay so please take this uh a defaced value right this is something that can be proved assume that this is true okay this is called the tweedy formula

### 01:16:20 · Speaker 1

Okay so now here the

### 01:16:24 · Speaker 1

variant of the log likelihood of a particular distribution with respect to the random variable of interest is defined as core

### 01:16:36 · Speaker 1

There's this called function

### 01:17:02 · Speaker 1

Okay, this is a known result. Okay, so now we let's use this result. So what do we do is we have in the context of DDPM

### 01:17:19 · Speaker 1

context of DDPM we had this queue of

### 01:17:24 · Speaker 1

60 given x naught remember this right using the recursion we showed that this was a Gaussian okay with mean being equal to root of alpha t bar into x naught the variance was 1 minus alpha t bar times i

### 01:17:45 · Speaker 1

the quality and distribution suppose i apply this 3d formula to this okay what i can write is that i can write the expectation of

### 01:17:58 · Speaker 1

mu xt okay which is the expectation of this distribution given xt is written as xt

### 01:18:10 · Speaker 1

1 minus alpha RT

### 01:18:15 · Speaker 1

Fines

### 01:18:19 · Speaker 1

X P

### 01:18:22 · Speaker 1

Lagga

### 01:18:24 · Speaker 1

p x t because it is simply applying the 3d's formula as above right i mean sigma the variance of this is 1 minus alpha t bar into i therefore uh the identity matrix may go away this will simply be this particular thing okay so what is the mean of this distribution we know that the mean of this distribution is the root of

### 01:18:46 · Speaker 1

alpha t bar into x naught is equal to xt plus 1 minus alpha t bar times

### 01:18:57 · Speaker 1

the square function

### 01:19:00 · Speaker 1

your mixed D

### 01:19:02 · Speaker 1

Okay, so now rearranging the terms, this implies my x naught can be reparameterized in terms of

### 01:19:12 · Speaker 1

XT

### 01:19:15 · Speaker 1

plus one minus alpha t bar

### 01:19:20 · Speaker 1

into the square function

### 01:19:27 · Speaker 1

Divided by

### 01:19:29 · Speaker 1

So put up alpha T bar

### 01:19:32 · Speaker 1

Okay, now why is this of any consequence is because we also know that this X naught

### 01:19:42 · Speaker 1

uh was reparameterized in terms of

### 01:19:47 · Speaker 1

1 minus alpha t bar into epsilon right if you remember this

### 01:19:56 · Speaker 1

Okay, this is what it was. We showed this. So we if we compare the terms, okay, we see that the score of

### 01:20:09 · Speaker 1

log of p of x t is simply equal to some scaled version of

### 01:20:16 · Speaker 1

minus alpha t bar times epsilon okay this is the result that we need okay which is

### 01:20:25 · Speaker 1

the ground truth, I mean the noise that we are adding to xt, okay, is actually the score which is the derivative of log of p of xt with respect to xt with a scale.

### 01:20:41 · Speaker 1

Is this all right? This implies that this implies that the last function that we had, which was epsilon minus epsilon theta cap.

### 01:20:51 · Speaker 1

is equivalent to

### 01:20:58 · Speaker 1

Regressing over the score of the model

### 01:21:06 · Speaker 1

particular t so this is the result right i mean that that's why the name ddpms are also called score based model so basically what is being done is core matching isn't it so the true score the true score is the noise and whatever the model is giving can be looked into as uh uh the estimated score to using the neural network and that is what we are matching is that all right see actually we don't need this result what we need

### 01:21:36 · Speaker 1

is that a simple thing that why when we are constructing DDPMs we are implicitly okay matching these scores

### 01:21:46 · Speaker 1

of the I mean the true score and the estimated score is that is that all right

### 01:21:52 · Speaker 1

And this is the result that we actually need right which is the

### 01:21:58 · Speaker 1

Original noise that we add to make X naught XT, okay, is actually a scaled version of what is called as the score function. Is this is all right? So we will use this result to to build a conditional diffusion model.

### 01:22:20 · Speaker 1

Any questions so far

### 01:22:22 · Speaker 1

We don't we all we did was you know we just introduced a concept called score which is the derivative of the log likelihood of a random variable with respect to the random variable itself. Okay. And we showed that in the case of DDPMs the ground truth noise that we add to X naught to get to Xt is simply a scaled version of what is called as the score function at Xt. Is this all right? Any questions here?

### 01:23:07 · Speaker 1

Uh, yeah, I don't if you don't speak up, I don't know. I I don't I can't see my screen, right? So if you are interacting, I don't know if you are interacting. So I think it's better if you speak up. Shall we move on? This is all right?

### 01:23:26 · Speaker 1

Now we will do what is called as conditional generation

### 01:23:31 · Speaker 1

Using this idea is also called the graded diffusion

### 01:23:41 · Speaker 1

typically called classifier guided diffusion

### 01:23:57 · Speaker 1

okay so now note that okay so note

### 01:24:03 · Speaker 1

Alright

### 01:24:06 · Speaker 1

a DDBM

### 01:24:12 · Speaker 1

Estimates

### 01:24:21 · Speaker 1

Estimates these four up

### 01:24:30 · Speaker 1

That is what it is doing. We know that. This is where we will use the fact. Now, for conditional generation.

### 01:24:48 · Speaker 1

One needs to estimate

### 01:25:01 · Speaker 1

It's good up

### 01:25:04 · Speaker 1

P of X P given Y okay where Y is a conditional random variable which can be a class or a text embedding or anything right conditional

### 01:25:18 · Speaker 1

can be a class label

### 01:25:23 · Speaker 1

Or it can be a text embedding or anything depending upon what your classes

### 01:25:30 · Speaker 1

your conditioning is right so yeah so what we are doing is instead of estimating the score of p x t we need to we need to estimate the score of p x t given y correct that is what is to be done now how do we do that is that we simply use bayes rule to do that we have the score of log of we need p of x t given y

### 01:25:58 · Speaker 1

with respect to HD

### 01:26:03 · Speaker 1

the derivative of log of

### 01:26:07 · Speaker 1

And we use Bayes' law

### 01:26:10 · Speaker 1

P of x t times

### 01:26:13 · Speaker 1

of y i given x t divided by p y this base law okay then i've used the law of logarithms so this is log of p of x t

### 01:26:30 · Speaker 1

Yes

### 01:26:33 · Speaker 1

Derivative of log

### 01:26:36 · Speaker 1

f y given x t

### 01:26:40 · Speaker 1

Minus

### 01:26:42 · Speaker 1

log of derivative of log of

### 01:26:48 · Speaker 1

of y note that these derivatives are with respect to xt because these are scores right

### 01:26:54 · Speaker 1

Of this term is zero because it is independent of y. So now the conditional score that we would want to estimate

### 01:27:09 · Speaker 1

be equal to derivative of log of

### 01:27:13 · Speaker 1

p x t with respect to x this is the unconditional score right plus some term okay this is log of

### 01:27:24 · Speaker 1

P y given x t with respect to x t

### 01:27:29 · Speaker 1

Yeah, so this is the result. This is the result that we need is that what we showed is that the if you want to train a diffusion model on P of XT given Y, all you need to do is train a model on unconditional data and have an additional term, okay, estimate this score.

### 01:27:53 · Speaker 1

estimate this core okay of p of y given x t so what do you mean by that see how do we do this in practices

### 01:28:03 · Speaker 1

Beep

### 01:28:05 · Speaker 1

Y given XT what is this is actually a classifier right

### 01:28:15 · Speaker 1

You agree see y is a class that you are conditioning your generation on p of y given x t is a classifier on x t isn't it

### 01:28:28 · Speaker 1

So what is done is that first train

### 01:28:35 · Speaker 1

Fine a classifier

### 01:28:41 · Speaker 1

On XD

### 01:28:43 · Speaker 1

Just keep it you know try and classifier on XT and then guide guide

### 01:28:50 · Speaker 1

The diffusion

### 01:28:57 · Speaker 1

Oh yeah this classifier okay what do you mean by that

### 01:29:03 · Speaker 1

So now there is a there's a unit that is to be trained

### 01:29:08 · Speaker 1

And note that this is actually estimating the score right so this will take xt

### 01:29:16 · Speaker 1

Now because this is a network

### 01:29:22 · Speaker 1

that is a conditional diffusion model it will also take a y as an input this is where you have the the class label right that is coming as an input so let us make it a little more

### 01:29:36 · Speaker 1

easier to understand so this will take x t and y as an input and here you have the

### 01:29:44 · Speaker 1

P going as an input okay right so now what you get here is the epsilon theta star which is

### 01:29:52 · Speaker 1

the unconditional score right we want this to be the conditional score what do we do is that train another classifier

### 01:30:03 · Speaker 1

classifier is p y given x t so this will take x t as an input and it will give you a class okay this is pre-trained okay we could declassify the pre-trained now what you do is there is a score matching that is happening here which is the usual

### 01:30:27 · Speaker 1

loss that is back propagated

### 01:30:30 · Speaker 1

In addition to this, you also calculate here, okay, this is the output of P of y given xt, okay? Take the log of it, compute the derivative of this gradient of this with respect to xt. How do you do this? See, we can do a backpropagation with respect to parameters. Just like we do that, we can do a backpropagation with respect to the input of the network also in PyTorch, right? So you take the gradient of this, the output of this,

### 01:31:00 · Speaker 1

Network with respect to XT here. Okay, you back propagate, add those gradients.

### 01:31:13 · Speaker 1

with respect to XT to this and then back up again here

### 01:31:18 · Speaker 1

That's all you're trying to do

### 01:31:21 · Speaker 1

Is this all right? So finally during the inference, what do you do? You give an x and a y as an input to this t data star network. If the sampling is exactly the same, sampling procedure here is the same thing, right? You do the exact same thing here, but you give y also as an input here while you are estimating this loss.

### 01:31:47 · Speaker 4

So one question

### 01:31:49 · Speaker 1

Uh hold on huh Okay

### 01:31:50 · Speaker 4

Oh okay sorry

### 01:31:53 · Speaker 1

Yeah, so this is called classifier guided diffusion models conditional diffusion classifier guided conditional diffusion. There is another version called classifier free guidance. I will not talk about it. I mean, you can just do see that as a homework. It's a variant of this.

### 01:32:19 · Speaker 1

read that as a self-study thing yeah this is called classifier guided conditional diffusion where uh you first uh realize that the diffusion model that you are training is implicitly doing the score matching and use bayes law to estimate i mean represent the conditional score in terms of unconditional score and the classifier okay pre-trained classifier on xt on different noise levels okay and then use that pre-trained classifier along

### 01:32:49 · Speaker 1

with the unit to estimate the conditional score okay then you have trained a conditional diffusion model where you have classifier guidance so now one question that might come up is uh see y need not be a class label no it can be a text embedding also if it happens to be a text embedding this p of y given x uh y given xt will become a regression mod regression network that would take an xt and produce the

### 01:33:19 · Speaker 1

uh corresponding text embedded

### 01:33:26 · Speaker 1

Right. So I have asked you to implement this. So what you should do is while you collect multiple XTs, no, while you are training this theta, you also train a classifier to get the corresponding class for the XT. OK. Use that classifier. Get the gradient of every XT with respect to the output of this classifier and add that to the gradient of this unit and backpropagate. That is what you need to do.

### 01:33:56 · Speaker 1

Yeah, so now any questions on this

### 01:34:00 · Speaker 3

Uh yes sir so the classifier is not trained as part of the process right

### 01:34:06 · Speaker 1

So classifier is already pre-trained so you pre-train the classifier and keep it yes

### 01:34:10 · Speaker 3

Okay but if the but if it has no effect if this process does not have an effect on our if we are not getting the desired results what could be wrong actually

### 01:34:21 · Speaker 1

uh what's the see typically what happens in classifier guided diffusion this see if you look at it this classifier has to discern the class uh by taking a noisy sample as input correct

### 01:34:38 · Speaker 3

Okay

### 01:34:40 · Speaker 1

Now if if P is very high the sample becomes too noisy

### 01:34:40 · Speaker 3

Okay

### 01:34:45 · Speaker 1

See it has to design the class at all noise levels that will become too much for a classifier to do isn't it

### 01:34:52 · Speaker 3

Okay okay

### 01:34:54 · Speaker 1

And typically this classifier fails that is because at high higher noise levels and that's why classifier guided diffusion does not work too nicely

### 01:34:54 · Speaker 3

I need this

### 01:35:03 · Speaker 1

So that's why people went from classifier guided diffusion to classifier free diffusion, okay, classifier free guidance, okay, so which I said just read it as a homework. I mean, I need

### 01:35:16 · Speaker 1

uh i mean i i leave some questions i mean some concepts uh to you as homework so that's why people move to classifier free guidance where there is no classifier by having a good guidance just read that huh it is there in the tutorial that i had given uh as a reference read that once but yeah but what i've asked you to implement in assignments as a classifier guided equation the problem might be that you are overburdening this classifier to get the classes at multiple noise levels that's why that's where the problem can come

### 01:35:46 · Speaker 1

In fact all the the state of the art models right like this this stable diffusion imagine etc all all use classifier free guidance not classifier guided diffusion for conditioning

### 01:36:03 · Speaker 1

Yeah okay so any other question see there is uh one other last piece right I mean you see this uh

### 01:36:03 · Speaker 3

Okay so any of the

### 01:36:10 · Speaker 1

stable diffusion thing i've asked you to do that in your assignment as well the stable diffusion stability.ai company you know what they are doing is the diffusion ddpms are not built on the image space what they do is they first train

### 01:36:30 · Speaker 1

they take x naught and get x naught cap so this is a they first try in a vqva okay

### 01:36:39 · Speaker 1

is the encoder and decoder of a VQ VIE okay so you get the Z corresponding to the data they first try a VQ VIE okay then what they do is TDPM

### 01:36:55 · Speaker 1

Or that prime G D P M

### 01:36:59 · Speaker 1

On the latent space of VQVA

### 01:37:12 · Speaker 1

They train a DDPM on the latent space of the QAE and generation right So now what happens is generation

### 01:37:24 · Speaker 1

First

### 01:37:28 · Speaker 1

Get a new latent sample, right? Because the entire generative model is.

### 01:37:35 · Speaker 1

built on the the latent space of VQVAE and then pass it

### 01:37:44 · Speaker 1

So the decoder

### 01:37:49 · Speaker 1

of VQVA to finally get the image

### 01:37:58 · Speaker 1

I asked you to do this as well, right? I mean, it's pretty simple. The point is that building a diffusion model on the image space is very difficult because it's of very high dimensions, right? Instead of doing that, you first train a encoder-decoder model or a VQVAE, get the latent vectors, and you train a DDPM on the latent vectors of the VQVAE, and then when you sample, you first sample the latent vector,

### 01:38:28 · Speaker 1

latent vector pass it to the decoder of eqvae and get the generated sample that's what all i mean that's what is done in this table diffusion right where uh i mean they step they call it stable stable because you are not doing it on the image space but you are doing it on the latent space of a pre-trained eqvae

### 01:38:49 · Speaker 1

Okay, so that's about it. That's all I wanted to cover in DDPMs. So one other piece to be covered today is DDIMs, right? Diffusion implicit models, where you have the inversion, possible possibility of inversion, and also they address this drawback of the inference time of DTPM being too slow, right? Because you need to hop capital T number of steps, which is typically of order of thousands. So,

### 01:39:19 · Speaker 1

DDIMs which are denoising diffusion implicit models will take care of that particular issue. We will look at DDIMs and then I'll go to noise contrastive estimation and self-supervised learning.

### 01:39:33 · Speaker 1

Shall we take a break now for about 10-15 minutes

### 01:39:39 · Speaker 3

Okay

### 01:39:41 · Speaker 1

the plan is the following right i will uh uh we will we will do ddpms ddims this class possible at the end of this class uh i will just give you an introduction to self-supervised learning next class i will do noise contrastive estimation self-supervised learning and if possible i'll also sneak in some distillation ideas knowledge distillation and in the final class on 16 we will look at the autoregressive models transformers and some introduction to llms

### 01:40:11 · Speaker 1

that would conclude the course see we had to have 14 classes right uh how how much do we have do we have how many classes have we done so far does anyone have a count

### 01:40:28 · Speaker 4

So as per your lecture label it is 10th

### 01:40:31 · Speaker 1

Uh that's I also noticed that but did I start writing from the very first class

### 01:40:40 · Speaker 4

I think uh there's also lecture zero so it is it's like

### 01:40:43 · Speaker 1

Like eleven

### 01:40:46 · Speaker 1

Is that zero Yeah there is a logistic

### 01:40:48 · Speaker 4

Logistics one yeah

### 01:40:52 · Speaker 1

so yeah this is 11 so we'll have 13 classes uh okay yeah typically that's what a semester is you know it's between 13 and 14 14 classes of three years but it's okay i think we have covered uh like a sufficient growth so we'll have two more classes right and we'll do self-supervised learning distillation and some introduction to llms i think that would that would conclude it okay so let's take a break it's 11 10. uh let's take a short break of about 10 minutes

### 01:41:22 · Speaker 1

Come back at 1120

### 01:41:24 · Speaker 1

That okay

### 01:41:26 · Speaker 4

Yeah so just one question so in the assignment uh you mentioned IJPG so would you be talking about that?

### 01:41:35 · Speaker 1

Of course definitely

### 01:41:38 · Speaker 1

Maybe in the next class yeah that's a self supervised learning method called IJPA I'll do it in the next class perhaps

### 01:41:45 · Speaker 4

Shirts

### 01:41:46 · Speaker 1

Yeah see you in a minute please come back in ten minutes uh where we have things to cover yeah

### 01:56:48 · Speaker 1

So shall we resume

### 01:56:53 · Speaker 4

Yes sir I have a question regarding stable diffusion

### 01:57:00 · Speaker 4

So the latent space used in the generation is it just after the encoder or the after mapping to the dictionary of embeddings

### 01:57:10 · Speaker 1

Oh yeah yeah so it is the quantized latent space only

### 01:57:15 · Speaker 4

Okay okay

### 01:57:18 · Speaker 3

So but how do we sample from that because it's a it's a quantized set of vectors right

### 01:57:24 · Speaker 1

So what? See, you take the encodings as the quantized vectors, right? And then build a generative model on top of it.

### 01:57:36 · Speaker 1

Then the all the all

### 01:57:36 · Speaker 3

All the all the quantized vectors

### 01:57:38 · Speaker 1

for bank corresponding to the entire data set

### 01:57:46 · Speaker 1

Yeah

### 01:57:51 · Speaker 1

Any other questions

### 01:58:16 · Speaker 1

Yeah it's a sample tag

### 01:58:44 · Speaker 1

Okay so let us uh look at this another class of models now called

### 01:58:58 · Speaker 1

You know

### 01:59:03 · Speaker 1

Fusion implicit models they're called

### 01:59:26 · Speaker 1

Okay, so now the the motivation for these class of models are the following, right? So they first ask this question, right? DDPMs

### 01:59:41 · Speaker 1

R Marco VM right

### 01:59:47 · Speaker 1

Actually first order mark will be in

### 01:59:51 · Speaker 1

Because of this what happens is so the sampling or the inference

### 02:00:01 · Speaker 1

Sampling is slow. Uh, what do you mean by that? It is slow because

### 02:00:10 · Speaker 1

Wee

### 02:00:12 · Speaker 1

I'm Clive

### 02:00:16 · Speaker 1

us to hop through

### 02:00:23 · Speaker 1

Three steps

### 02:00:27 · Speaker 1

Because I did recall that right in the sampling procedure

### 02:00:45 · Speaker 1

inference here you need to hop to capital T to one okay which is very slow so why is this happening this is happening because the uh the model that we have constructed is Markovian right the question that they asked in DDIMS so is there a

### 02:01:09 · Speaker 1

The question is so this is yeah I'll

### 02:01:13 · Speaker 1

I can give you the other motivation also and then we will answer both of them using one model construction

### 02:01:51 · Speaker 1

DDPMs cannot perform posterior inference or also called inversion. Okay. So what do we mean by that? We know that, right? I mean, given X, we need P of Z given X. We need a latent vector. And DDPMs cannot do that. Okay. Why? Why is that? Because the encoding process will converge to normal 0, 1. And for every input sample, you will get some sample from normal 0, 1. Now, suppose you take that sample from normal

### 02:02:21 · Speaker 1

zero one okay and uh run through the uh the

### 02:02:27 · Speaker 1

generate generation process or the denoising process okay there's no guarantee that you get the exact same image that you started with let me repeat what i said suppose you take an image okay or a data point and encode it using the ddpms encoder you get a particular x capital t right now if you take the same image and do encoding another time uh you will get another sample corresponding to that right if you take both those uh outputs

### 02:02:57 · Speaker 1

of both both of those forward processes and run through the backward process there is no guarantee that you will get the exact same input sample that you started within a DDPM model right

### 02:03:12 · Speaker 1

that's what i mean by ldpms cannot perform posterior inference or inversion so now the question is can both of these uh props the ddim's uh solve both of these issues actually okay

### 02:03:30 · Speaker 1

I am

### 02:03:36 · Speaker 1

Non non Marquisean

### 02:03:41 · Speaker 1

What is

### 02:03:46 · Speaker 1

Dot dot

### 02:03:48 · Speaker 1

That enable fast sampling

### 02:03:57 · Speaker 1

Because of the non-Markovian assumption, right? Okay. Non-Markov enable fast sampling plus inversion. Both of these are possible.

### 02:04:08 · Speaker 1

Now, the, I mean, this is not the most interesting part. The most interesting part is.

### 02:04:17 · Speaker 1

If you train a DDPM okay then you are also training DDIM which is which means that requires more additional training

### 02:04:31 · Speaker 1

No additional timing

### 02:04:40 · Speaker 1

So this is the beautiful part of it right DAN-DDPM

### 02:04:45 · Speaker 1

If you train a DD3M, then you are implicitly training DDIM is what the idea is. Okay. So let us concretize these ideas. You know, what do I mean by all this? We will put math to it and understand. Okay. See, the first observation that is made is

### 02:05:11 · Speaker 1

It's an observation

### 02:05:19 · Speaker 1

The DDPM

### 02:05:43 · Speaker 1

DDPM loss

### 02:05:51 · Speaker 1

Last function

### 02:05:53 · Speaker 1

depends

### 02:06:00 · Speaker 1

only on Q of

### 02:06:08 · Speaker 1

XT given X naught

### 02:06:11 · Speaker 1

Okay, this is the first observation that they do is that the DDPM loss function only depends on Q of XT even X naught.

### 02:06:22 · Speaker 1

Okay

### 02:06:24 · Speaker 1

So now the the

### 02:06:30 · Speaker 1

Based on this observation

### 02:06:36 · Speaker 1

Right based on this observation they say that

### 02:06:46 · Speaker 1

on and not on

### 02:06:50 · Speaker 1

You are

### 02:06:53 · Speaker 1

X

### 02:06:57 · Speaker 1

1 2 t given x not

### 02:07:01 · Speaker 1

Okay, so please pay attention here. See, Q of XT given X naught is the posterior of the Tth latent variable conditioned on X naught, okay? And Q of X1 to T given X naught is the joint distribution of, okay, all the latents given the data variable. Now, the observation that is made is that the DTPM loss function, okay, or the elbow,

### 02:07:31 · Speaker 1

does not depend on the joint the the joint distribution of all the latents given data but only on the dth latent variable given data okay so this means

### 02:07:49 · Speaker 1

in place

### 02:07:52 · Speaker 1

That's long the ass

### 02:07:56 · Speaker 1

You lost

### 02:08:05 · Speaker 1

is same

### 02:08:09 · Speaker 1

as that of DDPM

### 02:08:16 · Speaker 1

The elbow does not alter this is the key observation okay

### 02:08:27 · Speaker 1

So, which means that as long as Q of XT given X naught remains the constant, the elbow doesn't alter. Which means that see there is one other known thing in the probability theory which would say that there can exist multiple joint distribution that has the same conditional.

### 02:08:51 · Speaker 1

you that does that make sense suppose there are uh like there is a particular conditional distribution okay we can construct multiple joint distribution that would have exactly the same conditional distribution

### 02:09:05 · Speaker 1

Now what I do is so define

### 02:09:11 · Speaker 1

A family of non-Markovian

### 02:09:16 · Speaker 1

Encoding distribution

### 02:09:36 · Speaker 1

including distributions okay dark

### 02:09:43 · Speaker 1

Exact

### 02:09:50 · Speaker 1

Conditional

### 02:09:55 · Speaker 1

as in DDP So what we are seeking is that I will give you now a family of non-Markovian

### 02:10:04 · Speaker 1

conditional encoding distribution such that the conditional is same that of the uh ddpm okay so what they do is suppose

### 02:10:20 · Speaker 1

Sigma is a positive real number

### 02:10:27 · Speaker 1

Is a positive real number. They define Q sigma of

### 02:10:35 · Speaker 1

x 1 2 3 given x naught so this is the joint distribution non Markovian joint distribution that we are defining okay it's given by

### 02:10:47 · Speaker 1

Q of Q sigma

### 02:10:53 · Speaker 1

Steve give a next mark

### 02:10:56 · Speaker 1

Lines

### 02:10:58 · Speaker 1

This is by the chain rule of probability Q sigma

### 02:11:07 · Speaker 1

xt minus one given xt and x0

### 02:11:14 · Speaker 1

This is a non Markovian distribution okay

### 02:11:21 · Speaker 1

glo Sigma

### 02:11:27 · Speaker 1

T minus 1 given XT and X naught

### 02:11:33 · Speaker 1

Given it's a normal distribution

### 02:11:36 · Speaker 1

Which

### 02:11:39 · Speaker 1

mean equal to root

### 02:11:44 · Speaker 1

alpha t minus one bar the same notation that we have with d d p of x naught plus root of

### 02:11:53 · Speaker 1

1 minus alpha t minus 1 bar minus sigma t squared

### 02:12:15 · Speaker 1

Long very distant

### 02:12:20 · Speaker 1

Just a second here this is

### 02:12:26 · Speaker 1

exploit art this is

### 02:12:34 · Speaker 1

There's something wrong with this

### 02:12:41 · Speaker 1

One minus

### 02:12:43 · Speaker 1

Uh 1 minus alpha t into sigma t squared okay and yeah

### 02:12:54 · Speaker 1

It looks a little complicated but I'll tell you why this was done

### 02:13:03 · Speaker 1

x to the minus

### 02:13:07 · Speaker 1

T bar into X naught

### 02:13:13 · Speaker 1

divided by root of one minus alpha t power

### 02:13:18 · Speaker 1

the mean and the variances yeah sigma squared into i yes

### 02:13:30 · Speaker 1

Okay, so this is the distribution. So now why is this, how did they get into this complicated form? It's simply they wrote this down such that, such that sigma Q sigma of XT given X naught, okay, will match that of the DDPM, which is simply

### 02:14:00 · Speaker 1

This term that we knew right alpha t bar into i

### 02:14:03 · Speaker 1

So this distribution okay Q sigma is constructed in such a way that

### 02:14:11 · Speaker 1

The conditional distribution matches that of a DDPM

### 02:14:19 · Speaker 1

Is this is this clear

### 02:14:24 · Speaker 1

See, there is that the DDPM, DDIM's paper, right, gives a proof that y would, I mean, they did do the algebra and show that Q sigma of xp given x naught is normal, this has this particular form that matches with that of DDPM. But yeah, so the point is.

### 02:14:43 · Speaker 1

What we have done now is defined a family of non-Markovian forward processes, okay, such that all of them have the same conditional as that of DDPM. Is this clear? Any questions so far?

### 02:15:25 · Speaker 1

Hello am I there

### 02:15:31 · Speaker 1

uh questions here did you understand this

### 02:15:46 · Speaker 1

Okay fine so oh this is uh how you define the uh the

### 02:15:53 · Speaker 1

non-Markovian process. Okay, now you define the corresponding, I mean, as you see, all of these are known, right? I mean, there's nothing to learn. The model similar to the previous case, define the, define

### 02:16:10 · Speaker 1

reverse process

### 02:16:18 · Speaker 1

Reverse or the denoising process

### 02:16:24 · Speaker 1

correspondingly

### 02:16:38 · Speaker 1

follows so what do we need we simply need a p theta of

### 02:16:45 · Speaker 1

xt minus one given xt

### 02:16:49 · Speaker 1

Define that to be for t equal to 1, it is a normal distribution. Similarly, at mean mu theta and variance sigma i, okay, at different other t's, it is equal to q phi of

### 02:17:07 · Speaker 1

xt minus one okay given xt

### 02:17:14 · Speaker 1

And instead of x not what we have is

### 02:17:29 · Speaker 1

Yeah you can call that us

### 02:17:32 · Speaker 1

Let's not call it call it as mu theta only

### 02:17:37 · Speaker 1

This is the estimated mu theta let us call the estimated x naught as

### 02:17:45 · Speaker 1

F t dot

### 02:17:48 · Speaker 1

function of x t okay this is how we define it where

### 02:17:57 · Speaker 1

We know that our x naught is given by x t minus root of 1 minus alpha t into epsilon divided by root of alpha t bar it is what we have

### 02:18:14 · Speaker 1

So in the this is in the forward process

### 02:18:24 · Speaker 1

In the reverse corresponding reverse process, we call the

### 02:18:31 · Speaker 1

g eta of x over is an estimate of x naught to be equal to

### 02:18:35 · Speaker 1

60 my best

### 02:18:38 · Speaker 1

Just like we did with DD PMs, we have a similar thing with DD IMs. Instead of epsilon, we have epsilon theta cap, right? Which is the estimated epsilon divided by alpha t bar. That's all. This is in the reverse process.

### 02:19:01 · Speaker 1

Okay so now with this what can be shown is see I am skipping the proof because it's sort of

### 02:19:12 · Speaker 1

slight forward in the sense that if you look at the DDIM paper you will get that and also it's not like very relevant to what we are doing what can be shown us with the above models

### 02:19:33 · Speaker 1

The elbow okay

### 02:19:37 · Speaker 1

will come out to me

### 02:19:46 · Speaker 1

the same as that of the DPM

### 02:19:55 · Speaker 1

This is what the the take-home message is that when you are training a DDPM, okay, you are also implicitly training a large class of non-Markovian models with these particular distributional forms.

### 02:20:13 · Speaker 1

Does that make sense

### 02:20:24 · Speaker 1

So is that clear? So what I'm saying is when you train one DGPM with the procedure that we just saw, you're actually training a grammar model of infinite models, non-mathematical models with this particular distribution that we just learned. That's why we named them denoising distribution implicit models because you're implicitly training so many models while

### 02:20:54 · Speaker 1

also in one digital

### 02:20:57 · Speaker 1

So this implies what does this imply this implies that

### 02:21:08 · Speaker 1

The training procedure

### 02:21:18 · Speaker 1

I'm the boss

### 02:21:28 · Speaker 1

the same

### 02:21:40 · Speaker 1

EDPM and EDIMES

### 02:21:48 · Speaker 1

Then you might ask, right, what is the whole point? I mean, like, what are we achieving by doing all this? Right. However, by returning procedures, their information are different, no?

### 02:22:06 · Speaker 1

Inference is very different right so how do we infer for DD

### 02:22:13 · Speaker 1

P m's okay sampling is from you get xt minus 1 recurring recurring simply from p theta of xt minus 1 given xt

### 02:22:24 · Speaker 1

Okay which is caution

### 02:22:28 · Speaker 1

What was the distribution of DDPM?

### 02:22:36 · Speaker 1

Recall it is

### 02:22:43 · Speaker 1

Can somebody tell me what it is E Gita

### 02:22:48 · Speaker 1

mu theta right which is xt minus one

### 02:22:53 · Speaker 1

Let me not write that it's always 16 minus 1, and this one was uh.

### 02:23:01 · Speaker 1

Alright the entire thing is what I'm thinking it's a

### 02:23:05 · Speaker 1

Huge thing

### 02:23:13 · Speaker 1

Hold on let me try to write it

### 02:23:17 · Speaker 1

Give me a second I'll write it I had written it before

### 02:23:42 · Speaker 1

So what was the mean mean was

### 02:23:45 · Speaker 1

XT by

### 02:23:48 · Speaker 1

This minus

### 02:23:53 · Speaker 1

1 minus alpha t divided by

### 02:23:58 · Speaker 1

root of one minus alpha t bar times

### 02:24:04 · Speaker 1

Epsilon theta star

### 02:24:08 · Speaker 1

So this was the mean and the variance was uh

### 02:24:14 · Speaker 1

t squared times i okay this was in ddpm while in dd im's

### 02:24:32 · Speaker 1

the inference procedure changes which is still sampled from p theta of xt minus 1 given xt but since it is a non-Markovian process okay the mean and the variance changes that's all

### 02:24:52 · Speaker 1

may write it down the

### 02:24:57 · Speaker 1

Mean is given by

### 02:25:05 · Speaker 1

The water

### 02:25:10 · Speaker 1

for t minus 1

### 02:25:13 · Speaker 1

So power p r t minus one times

### 02:25:18 · Speaker 1

the output of the neural network

### 02:25:21 · Speaker 1

Yes

### 02:25:24 · Speaker 1

root of one minus

### 02:25:27 · Speaker 1

power bar t minus one minus sigma t squared

### 02:25:39 · Speaker 1

times epsilon theta star

### 02:25:44 · Speaker 1

It must clear the mind

### 02:25:47 · Speaker 1

That's all right. So this is what changes. So what changes is that the way the denoising is done, okay, changes the

### 02:25:59 · Speaker 1

Fining procedure remains exactly the same as the DDPM. Okay. Now, if you make sigma to be zero here, right, with sigma equal to zero, the class of model that you get is such that the encoding process

### 02:26:19 · Speaker 1

Comes

### 02:26:21 · Speaker 1

Deterministic

### 02:26:33 · Speaker 1

The encoding process becomes deterministic because there is no noise component to it. So now this what does this enable? This enables inversion. Okay. Deterministic enable in inversion.

### 02:26:54 · Speaker 1

So what do you mean by that? Given a particular x naught, which is a data sample, okay, what you could do is you could run the forward process, okay, that is a deterministic forward process for DDIM and get the corresponding latent vector, the noise latent vector, which when used in the sampling, okay, or denoising process will generate this exact same

### 02:27:24 · Speaker 1

For example it's not

### 02:27:26 · Speaker 1

Does that make sense

### 02:27:36 · Speaker 1

All you should do is the following, right? What is to be done is given an x naught, you run the forward process, okay, of the DDIM and you note that the forward process of DDIM is similar to that of the forward process of DDPM because the conditionals are the same. But because with sigma equal to zero, if you make sigma t equal to zero here and then run the sampling of DDIM, okay,

### 02:28:06 · Speaker 1

you will get the exact same sample, okay, corresponding to the input sample. So you start with, suppose you start with an image, okay? Running the forward process of DDIM will give you a noise sample, which when used in the reverse process of DDIM will give you the input sample, which means that you have encoded or inverted or you've gotten the exact same.

### 02:28:32 · Speaker 1

latent variable corresponding to the input image.

### 02:28:40 · Speaker 1

Is that making sense

### 02:28:47 · Speaker 1

Hello am I there

### 02:28:55 · Speaker 1

Any questions on this

### 02:28:58 · Speaker 1

See, the difference between DDPM and DDIM is in the fact that in the sense that what you have, right, as the forward and reverse processes, they would change. They would become non-Markovian processes, okay? But because of the way these non-Markovian processes are constructed, they're constructed in such a way that the conditional distributions happen to be exactly the same, has the same

### 02:29:28 · Speaker 1

form as that of RDD

### 02:29:31 · Speaker 1

which implies that training a DDPM is implicitly training multiple DDIMs that are there.

### 02:29:43 · Speaker 1

What is the advantage of that? The advantage is that because one of the at one of the the values of sigma the the class of models that we have generated becomes deterministic you can use that for inversion.

### 02:30:05 · Speaker 1

Is that clear

### 02:30:08 · Speaker 1

I will also share our nice

### 02:30:12 · Speaker 1

blog post on this

### 02:30:34 · Speaker 1

You may ask any questions if you have on the meantime

### 02:30:39 · Speaker 3

So one question so uh the reason why DDPMs are non-invertible is it because the the Markovian processes are non-reversible

### 02:30:48 · Speaker 1

It is uh not because of that in particular it is because of the fact that the encoding process involves noise addition no

### 02:31:01 · Speaker 1

It's because

### 02:31:01 · Speaker 3

And in case of DDIMs

### 02:31:04 · Speaker 1

Yeah, in in the case of DDIMs where sigma equal to zero the encoding process does not involve noise addition

### 02:31:14 · Speaker 1

It is simply a function of alpha

### 02:31:20 · Speaker 3

Okay and that's why it is reversible

### 02:31:23 · Speaker 1

That is why it is reversible, correct? But the thing is, the alphas are designed in such a way that, you know, if you

### 02:31:33 · Speaker 1

keep moving in the forward direction they would still approach a a a normal 0 1 okay in the stationary distribution case however that the it's the the the forward process is not that you take an image and add noise

### 02:31:49 · Speaker 1

the way they are constructed

### 02:31:53 · Speaker 4

So the forward process is non-mock

### 02:31:56 · Speaker 1

Both the forward and the reverse processes are normal in DDIS yeah

### 02:32:09 · Speaker 1

okay so yeah see actually what i've asked you is that uh see you are you will be training one model okay which is the ddpm model but what changes is the inference right inference and the inversion uh in the case of ddim simply take a pre-trained ddpm okay and use it for inversion as the nice uh blog on ddim inversion i will

### 02:32:37 · Speaker 1

uh share that with you hold on looking for it

### 02:32:43 · Speaker 1

I've asked you to invert, get the noise samples and do an interpolation between those noise samples corresponding to two different images and then do a reverse direction is what I've asked for. It's a nice experiment to do. Let me just share that. Hold on. In our group, I will put it in our group.

### 02:33:10 · Speaker 1

mm not in the call chat how do I put it

### 02:33:14 · Speaker 1

Oh beams

### 02:33:17 · Speaker 3

They can put it in the culture itself

### 02:33:19 · Speaker 1

No but that will just go away no I don't want that to happen in general

### 02:33:23 · Speaker 3

Golf ball

### 02:33:26 · Speaker 1

No it will not

### 02:33:26 · Speaker 3

No it will not go away it will stay there

### 02:33:30 · Speaker 4

Whatever you put here is it will come in tunes uh yeah tunes

### 02:33:34 · Speaker 1

So anyway I just put it in the chat window have a look at it

### 02:33:41 · Speaker 1

Okay, so that's it. In fact, that's the end of what I wanted to do with diffusion models.

### 02:34:01 · Speaker 1

See all these uh these uh text to image uh generators right they're all diffusion models okay uh

### 02:34:11 · Speaker 1

they use the classifier free guided diffusion and they're all dd imms they are not ddpms because uh i mean yeah in fact the training is the same but because the inference has uh multiple advantages over the ddpms right what they do is they infer using dd imms processes not ddpms processes but all of the state of the art models are

### 02:34:31 · Speaker 4

All of them

### 02:34:33 · Speaker 1

diffusion models okay right so it's better if I start a new

### 02:34:46 · Speaker 1

page

### 02:34:56 · Speaker 1

Should I start self supervised learning in the next class

### 02:35:04 · Speaker 1

What do you reckon

### 02:35:09 · Speaker 1

give you the introduction and go get over the math in the next class or like we can start in the next class

### 02:35:17 · Speaker 1

I go with what you say what should we do

### 02:35:21 · Speaker 3

Uh so i we can have introduction and then the maths in next class maybe

### 02:35:26 · Speaker 1

Sure then I have to start a new uh notebook

### 02:35:33 · Speaker 1

So this is uh L eleven I will continue in the same notes next time

### 02:35:41 · Speaker 1

Well supervised

### 02:35:45 · Speaker 1

Presentation learning

### 02:35:58 · Speaker 1

So these diffusion models right because of their elegance in a sense that all their

### 02:36:03 · Speaker 4

On the phone

### 02:36:07 · Speaker 4

Got the endergetic

### 02:36:08 · Speaker 1

They're gone

### 02:36:11 · Speaker 2

uh for the DBI and everything else

### 02:36:14 · Speaker 3

I mean like how we for the conditional generation and all those things

### 02:36:20 · Speaker 1

Yeah yeah yeah conditional generation it's everything remains the same all that we changes is the forward and the reverse process even the training procedure does not change right the forward and the reverse process changes

### 02:36:33 · Speaker 1

uh the two xt uh the relationship between xt and x0 does not change the relationship between xt and x0 that you need for training the model does not change it remains exactly the same as that of ddpm but the forward and the reverse processes changes which means that the the sampling has a different equation which i wrote which is different from ddpm okay and the uh the uh the

### 02:37:02 · Speaker 1

Encoding process has a different equation. Okay. Encoding, we don't use explicitly. I mean, we use it only if we need this inversion thing, right? If you want the corresponding X, corresponding latent, latent corresponding to a given image, we have to run through the forward process of DDIM, non-Markovian DDIM. Otherwise, we only need that XT, you know, and the relationship between XT and X naught are exactly the same as that of DDPM in DDIM. And the conditioning, etc.

### 02:37:32 · Speaker 1

All of them remain exactly the same

### 02:37:40 · Speaker 2

So let's now switch gears and we will look at the self supervised learning these are not generative models

### 02:37:46 · Speaker 1

say okay uh the problem is uh of that of what is called as representation learning we have actually done it in a slightly different way to representation learning

### 02:38:06 · Speaker 1

Okay so what is the problem the problem is given

### 02:38:12 · Speaker 1

data I will switch back to our older notation okay x1 through xn these are not the intermediate states states in diffusion models okay iid drawn from some unknown distribution px okay there are no labels here learn a function

### 02:38:38 · Speaker 1

learn a function f theta okay f theta from space of x to some space z okay where z the dimensionality of z is typically much lesser than that of dimensionality of

### 02:39:00 · Speaker 1

Learn a function such that such that

### 02:39:08 · Speaker 1

Downstream tasks tasks as they call them

### 02:39:19 · Speaker 1

On on Z

### 02:40:18 · Speaker 1

Yeah so this is the uh uh

### 02:40:22 · Speaker 1

Object
