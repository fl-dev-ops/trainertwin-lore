---
id: c475SLygCK4
title: Lec 9 - Deep Generative Models Variational Auto Encoders
date: '2024-11-23'
url: https://www.youtube.com/watch?v=c475SLygCK4
description: ''
author: prathoshap5226
duration: 02:57:32
model: saaras:v3
transcript: true
---

# Lec 9 - Deep Generative Models Variational Auto Encoders

## Transcript

### 00:00:02 · Speaker 4

it was 12th or something

### 00:00:05 · Speaker 4

So I fourteenth is when it is ending for the offline semester. I think we will have one on sixteenth. I think that should be okay.

### 00:00:14 · Speaker 4

And given that you have an exam next Sunday, not having a class on Saturday is okay I suppose. Okay, we'll do it that way.

### 00:00:23 · Speaker 1

Hmm

### 00:00:25 · Speaker 1

Total

### 00:00:26 · Speaker 5

Okay, shall we start today?

### 00:00:31 · Speaker 1

Yes sir

### 00:00:35 · Speaker 5

ओके. ओके. सो अस आई सेड नो

### 00:00:39 · Speaker 4

today's uh focus will be on the variational autoencoders or VAEs. So as a precursor, we were looking at latent variable models last time, correct? Now what are latent variable models? These are

### 00:00:57 · Speaker 5

models that are defined as okay so whenever I talk of a model

### 00:01:08 · Speaker 5

a model yeah so P theta which is a distribution

### 00:01:11 · Speaker 4

over the uh the data variable right is what is called as a model so wherever we talk of model it is p theta that we talk of okay now in a latent variable setting that p theta is given as a marginal over the joint distribution of two uh variables okay one is called the uh the data variable of course x uh which is given and one is the latent variable that is not observed I mean that's why the name latent or the hidden variable

### 00:01:42 · Speaker 4

Okay. So what happens in a latent variable model? So what is a what is a latent variable model where P theta the model is given as a marginal over the joint distribution of the latent and the data variable. So that is what is called as the latent variable model. Unfortunately, this does not have a pointer, otherwise I've been so nice that I pointed things out when I was recapping. Anyway, okay.

### 00:02:10 · Speaker 4

Now, as the name suggests, the latent variable model, latent variables are not observed, right? They are not observed. They are to be estimated together with the model parameters. So, typically, Z is also estimated or learned along with the model parameters data. Okay?

### 00:02:28 · Speaker 4

Now the way it is defined is for every observed data point which is in the data set D, there exists a corresponding latent variable that is not observed, okay? So several examples, uh, latent variable can be discrete or it can be continuous. If latent variable is discrete, uh, the example that is given is that of the Gaussian mixture model or K-means clustering, okay? Where the latent variable denotes what uh cluster, right?

### 00:02:58 · Speaker 4

what group of uh gaussians that it belongs to. Okay, that is one example. The other example is uh a latent variable which is continuous wherever you have this uh encoder decoder model. It need not be auto encoder, any kind of encoder decoder model is a latent variable model with the output of the encoder seen as a feature or latent variable corresponding to X I. Right? So that is, yeah, so feel free to ask questions. I'm just recapping what on the last class.

### 00:03:30 · Speaker 4

If you have any questions, you can raise your hands and ask. Okay. Now, this is about the definition of latent variable model. Now the question is how do we model distributions using latent variable model? So that is the question. So now, as I said, the P theta of X in the case of latent variable model is given as a marginal over the joint distributions. And in all latent variable models, the the optimization is usually carried out by

### 00:04:00 · Speaker 4

maximizing the log likelihood or minimizing the KL divergence. Okay? So the objective is to maximize the log likelihood or minimize the KL divergence. So for the rest of the lecture, right, I will be using the term maximization of log likelihood, not minimization of KL divergence because they are equivalent. The reason I'm using the term log like maximization of log likelihood is because that is what is usually used in the literature everywhere, okay?

### 00:04:30 · Speaker 4

Okay, so now how do we model uh the how do we get the parameters of latent variable models? As I told, in latent variable models, right? The latent variable also has to be estimated jointly with the model parameters theta. So now what do you mean by estimating the latent variable? Because we are talking about uh random variables here and latent variable is another random variable. It amounts to uh estimating a distribution over the latent variable. Okay? That is what

### 00:05:00 · Speaker 4

it it it means by estimating a latent variable. How did we do that? We wrote down the log likelihood as L theta, okay? And uh uh we multiplied and divide divided the log likelihood by some distribution that you would want to estimate on the latent space, okay? Called call it as Q of Z given X. And then with the Jensen's inequality, what we found out was that there exists a lower bound, okay? on the log likelihood that

### 00:05:30 · Speaker 4

would want to optimize. So, yeah, the storyline is the following, right? There is a model, latent variable model with parameters theta. And we want to estimate the parameters of that model, theta, along with the distribution over the latent variables, right? Now, the distribution over the latent variable is what we called as a variational latent posterior denoted by Q of Z given X. Okay?

### 00:05:53 · Speaker 4

Now, when you introduce this unknown uh latent variable or distribution over the latent variable into the model, you cannot directly optimize the log likelihood, okay? Uh because uh in most of the uh the latent variable models, computing this integral, right, uh to get your P theta, okay? P theta is an integral over the joint distribution of X and Z, that is not feasible because you don't know what the latent variable is. What you can do is take a guess on the latent variable distribution.

### 00:06:23 · Speaker 4

which is called as Q of Z given X. Once you take a guess on the latent variable, latent distribution on the latent variable, uh there will be an inequality that arises, which means that you will get, see, observe this.

### 00:06:37 · Speaker 4

what you would want to maximize which is the log likelihood L theta. whenever you take a guess on the latent variable okay via the distribution Q there will be a lower bound that is created on the log likelihood

### 00:06:54 · Speaker 4

Okay? Now that lower bound is what is called as the evidence lower bound or elbow, okay? With a choice of Q and theta, you will get a particular elbow or the evidence likelihood. Sorry, evidence lower bound, okay? Now the goal in all latent variable models is to find out model parameters theta and a distribution over the latent variables Q such that the evidence lower bound is maximized. I mean, what we actually

### 00:07:24 · Speaker 4

need is to maximize the log likelihood but because we cannot do it exactly what we do is we will optimize a lower bound on the log likelihood which is called the evidence lower bound so which takes this particular form that I have written in the box item. Okay. uh any questions so far? Because this is the para this is of paramount importance because this is what we are this is the idea that we are going to use.

### 00:07:48 · Speaker 3

multiple times when we

### 00:07:51 · Speaker 4

optimize uh I mean when we when we you when we look at V I E's and diffusion models all these models right they work in this particular principle that there is we are looking at a latent variable model okay what is a latent variable model it is given by where the distribution over the data is given as a marginal over the joint distribution of the data variable and another unobserved variable denoted by Z called the latent variable okay the goal is to minimize the KL divergence and find out the

### 00:08:21 · Speaker 4

parameters theta. Now, uh we cannot do it because exactly we cannot do it because uh we don't know what the latent variable is. So we assume a distribution over the latent variable called I mean denoted by Q of Z given X. Once we assume a distribution over the latent variable, there will be a lower bound that will be constructed on the objective, the log likelihood that we would want to maximize. Right? And when we are maximizing it, we would learn both the model parameters theta and the distribution of the latent

### 00:08:51 · Speaker 4

variable by maximizing the lower bound. Okay, and that lower bound is given by this expression, right? Expectation of log of p theta x and z divided by q of z given x and the expectation is over q of z given x. So this is what we optimize whenever we are looking at VAEs and diffusion models and so on.

### 00:09:13 · Speaker 4

Any questions on this?

### 00:09:16 · Speaker 4

प्लीज एन्श्योर दैट यू अंडरस्टैंड दिस पक्का राइट? आई मीन देन आफ्टर दैट वी विल कंटिन्यू। या, राघवेंद्र गो ऑन।

### 00:09:25 · Speaker 2

Yes, so this Q of Z given X is also unknown, right? So how do we compute the X?

### 00:09:29 · Speaker 4

I I I'll tell you. I'll tell you that. I till now we don't know what Q of C Q. That's why I said no the look at the boxed item. It is an optimization joint optimization over theta and Q.

### 00:09:44 · Speaker 5

You have to compute both theta and Q

### 00:09:49 · Speaker 5

Okay, they are jointly estimated.

### 00:09:52 · Speaker 1

Yeah

### 00:09:54 · Speaker 5

Right?

### 00:09:54 · Speaker 1

We'll cover that right sir

### 00:09:56 · Speaker 5

Absolutely, that's exactly what we will do. Yeah. Any other questions?

### 00:10:07 · Speaker 5

So this this broad philosophy of what we are doing is clear I suppose. Okay.

### 00:10:11 · Speaker 4

Now we took an example after that in the last class which is a Gaussian mixture model. Gaussian mixture model is a latent variable model, okay? It's a proper latent variable model where P theta is given by again marginal of the joint distribution marginal over the joint distribution of X and Z, right? And this is the definition of GMM, no, this equation, second equation, period of X is given by a linear combination of multiple Gaussian distributions having different means and variances. Now a set of parameters are

### 00:10:41 · Speaker 4

the mixing coefficients which are alpha one through alpha m there are m number of mixtures m number of means and m number of variations sorry variances Now what do we do we want to solve that optimization problem right with respect to theta and q right How do we do it we do it alternatively first we solve for theta assuming that q is known and then we will solve for q assuming that theta is known Okay Now what can be shown Raghavendra I I said this last class maybe

### 00:11:11 · Speaker 4

forgotten. See this is in in G M M, uh the way to find this Q. You said that Q is unknown, no? What can be shown is that at a given theta, the optimal Q, okay? That would make the lower bound tight. What do you mean by lower bound tight? The lower bound that we have constructed on the log likelihood, uh will be equal to the log likelihood. That is the best value that it can assume, no? The lower bound can assume the best value which is equal to the log likelihood. Now,

### 00:11:41 · Speaker 4

That would happen if the Q, the choice of Q that you have made for a given theta is P of Z given X.

### 00:11:50 · Speaker 4

okay? So if Q is fixed to be P of Z given X or P theta of Z given X, then that is the best estimate for Q.

### 00:11:59 · Speaker 4

is it alright?

### 00:12:02 · Speaker 2

I mean sir, we we said that we would cover this in the TA session but I think last session we did not have it so maybe we will cover this in the next session.

### 00:12:08 · Speaker 4

No no, what I meant is, no no, what I meant is, what will be covered in the session is that the proof of this, that optimal Q for knowing a particular, I mean for given a particular theta is P theta of Z given X. Okay? This will be covered. So this is an algebraic proof. But what is important is that, I mean see, I didn't do it in the class and I don't want to do it in the class because in V I E's and diffusion models

### 00:12:14 · Speaker 2

Hello

### 00:12:16 · Speaker 2

Yes

### 00:12:38 · Speaker 4

we will not use this because uh in in in in in neural models we will not know what P theta of Z given X is.

### 00:12:49 · Speaker 4

Okay

### 00:12:50 · Speaker 4

That's the reason. So, the the jump from mixture models to like autoencoders, I mean, VAEs is because of this fact. See, had had we knew P theta of ZQ1X, then the problem of latent variable models is solved because you have the EM algorithm and this can be done. But since we do not, we'll not know what P theta of ZQ1X is, that is why we need to move to something else. So please note this everyone that, so again

### 00:13:20 · Speaker 4

I'm reiterating it, it's very very important. So now the goal is to find model parameters theta and the and the variational distribution or the latent variable distribution Q together, right? Now, uh there is a result that that would show that the optimal Q or the optimal distribution over the latent variable is actually P theta of Z given X.

### 00:13:43 · Speaker 4

Okay. Now if you know how to compute P theta of Z given X, then it is done. Because we know what the optimal what we can do is we can do this alternative optimization where you start with a random theta, right? And set this Q to be equal to P theta of Z given X when we know how to compute P theta of Z given X. Okay. And then with that Q, you find the next best theta and keep alternating between them.

### 00:14:10 · Speaker 4

Okay. Now how do we know P theta of g given x? P theta of g given x is given by the the base rule. Okay, which is written here. And in the case of a GMM or other mixture models, we know how to compute P theta of g given x given a particular theta.

### 00:14:26 · Speaker 4

And therefore we know how to compute Q optimal Q

### 00:14:31 · Speaker 4

Understand? So once we get that optimal Q, what do we do that? We plug in that optimal Q in this evidence lower bound F theta, okay? And optimize that, take a derivative of that with respect to uh theta and then find the new theta. With that new theta, you again compute P theta of Z given X and keep alternating between them, which is called the expectation maximization algorithm.

### 00:14:57 · Speaker 4

Does it make sense? So I have said this also, right? So yeah, so the question is, however, what if P theta of Z equals one X cannot be computed? So if you have models in in a Gaussian mixture model or a simple other mixture model, P theta of Z equals one X can be computed. If you cannot compute P theta of Z equals one X, you don't know what your optimal Q star is. When you do not know what the optimal Q star is, how do you compute, uh how do you estimate the parameters of a latent variable model is the primary question that would be that would be taken in a VAE

### 00:15:32 · Speaker 4

Does it make sense? Any questions so far?

### 00:15:36 · Speaker 5

And this is exactly what we do in GMM, right? GMM is also a

### 00:15:40 · Speaker 4

a latent variable model. Okay, we we uh estimate f theta we estimate theta and q alternatively and this algorithm is called the expectation maximization algorithm. And for EM algorithm to work, no, we need to know what the optimal q is or we need to be able to compute p theta of sigma.

### 00:15:59 · Speaker 5

next

### 00:16:02 · Speaker 1

E

### 00:16:02 · Speaker 5

Eat

### 00:16:07 · Speaker 1

Please ask questions if you have any when I am writing.

### 00:16:22 · Speaker 3

Sir, in this E M algorithm which we have mentioned, we are trying to find V theta of Z given X.

### 00:16:30 · Speaker 3

using the Bayes' theorem. So, but the P theta of X given Z is also unknown, right?

### 00:16:37 · Speaker 4

p theta of x given z x given z is known no? Because that is a single parameter Gaussian. It's actually a Gaussian distribution by assumption by construction by definition.

### 00:16:51 · Speaker 3

Okay

### 00:16:51 · Speaker 5

Okay

### 00:16:52 · Speaker 1

I'll go back to my previous slide.

### 00:17:02 · Speaker 1

I don't intend to like you know teach G M M

### 00:17:05 · Speaker 4

problems. Anyway, so here na, Yeah, that is what I have written here. You could just

### 00:17:10 · Speaker 3

for a given set we have p theta of okay

### 00:17:13 · Speaker 4

It's a particular it's a particular Gaussian. See in a G M M the way you model the distribution you know you show that.

### 00:17:22 · Speaker 4

This is how you model it, no? P theta of x is given by this, a linear combination of multiple Gaussians.

### 00:17:30 · Speaker 4

Okay

### 00:17:31 · Speaker 5

Now this can be written this way I'll write that so this is equal to

### 00:17:37 · Speaker 5

c equal to one to m

### 00:17:40 · Speaker 5

p theta of g into p theta of x given g.

### 00:17:46 · Speaker 1

Isn't it?

### 00:17:50 · Speaker 3

Yes sir

### 00:17:51 · Speaker 5

this is alpha's, okay? and this everyone is a Gaussian.

### 00:17:58 · Speaker 5

Okay, with a particular, let me write this, the P date of Z.

### 00:18:04 · Speaker 5

is equal to some particular J, mu J and sigma J.

### 00:18:11 · Speaker 5

all right? So we do know that.

### 00:18:14 · Speaker 5

the conditional of x given a particular z is a single component Gaussian.

### 00:18:27 · Speaker 1

Understood sir

### 00:18:28 · Speaker 5

Any other question on this?

### 00:18:33 · Speaker 2

Sir, does it have to be a convex combination?

### 00:18:36 · Speaker 4

in mixture model, yeah, yeah, yeah. In mixture density is always taken because the reason is, uh if you look at it now, alphas are distributions over discrete uh variable Z, isn't it?

### 00:18:53 · Speaker 4

alpha will give you a displacement also. P theta of Z given J is given by alpha J, right? Which means that if we take

### 00:19:05 · Speaker 5

this

### 00:19:09 · Speaker 5

overall j, it should sum to one and all of

### 00:19:13 · Speaker 4

these have to be non zero because they are probabilities no

### 00:19:17 · Speaker 2

Yes

### 00:19:18 · Speaker 4

So they have to be, that is why it has to be a convex combination.

### 00:19:23 · Speaker 4

And by the way, uh mixture density, right? You don't the mixture density need not be a Gaussian mixture model, no? It can be exponential mixtures or Bayesian, I mean sorry, Bernoulli mixtures or anything. But to model uh data which which has infinite support and like the vector value Euclid which which lies in continuous space, right? Usually GMMs are preferred.

### 00:19:50 · Speaker 4

Okay. And did I also talk about the the clustering? See one other thing in a latent variable modulus tell you. See post training

### 00:20:01 · Speaker 4

training is what? post training is like estimation of theta. That's what training is all about.

### 00:20:09 · Speaker 1

after we estimate theta, okay? A latent variable model

### 00:20:23 · Speaker 1

variable model can be used

### 00:20:27 · Speaker 1

can be used for

### 00:20:31 · Speaker 5

two purposes.

### 00:20:35 · Speaker 5

can be any latent variable model including a G M M. The first thing is, okay, uh sampling or generation because

### 00:20:43 · Speaker 1

These are generating models, right?

### 00:20:55 · Speaker 1

Okay, now example how do you do it in GMM is that

### 00:20:58 · Speaker 5

in Jio Ma'am

### 00:21:02 · Speaker 5

Hmm

### 00:21:02 · Speaker 4

Now first you sample a Z from

### 00:21:06 · Speaker 4

from discrete

### 00:21:09 · Speaker 4

alpha one, alpha two up to alpha M. So note that all of these are estimated using the E M algorithm. Once you estimate them, this what is this is actually tossing an M

### 00:21:20 · Speaker 5

phase die. So first you do that and then

### 00:21:25 · Speaker 5

Sample X

### 00:21:29 · Speaker 5

Okay

### 00:21:31 · Speaker 5

x given z okay by Gaussian. So let's

### 00:21:36 · Speaker 1

say that the

### 00:21:37 · Speaker 1

outcome of this is

### 00:21:43 · Speaker 1

I is the outcome, alpha I is the outcome.

### 00:21:49 · Speaker 1

okay so let's call I the outcome.

### 00:21:58 · Speaker 5

Once you do that what you should do is sample an x. Okay? By a Gaussian which is the which has the Ith mean.

### 00:22:09 · Speaker 5

and IELTS variance, that's all.

### 00:22:13 · Speaker 5

Yeah, that's all it is. So this is how you do a generation in a G M M.

### 00:22:18 · Speaker 4

whatever x that you get now by doing the sampling is equal to i. You do that sampling via a Gaussian. In fact, if you look at Bishop's book, which is like

### 00:22:30 · Speaker 4

classical book by Bishop pattern recognition. So what you will see is that he has shown what will happen if we do sampling, I mean if we fit a G M M to M N S data and do a sampling.

### 00:22:46 · Speaker 4

it will look like some images, right? But it will not be like as good as it's some other generative model such as GAN. So what happens is, you know, in very high dimensions, uh these GM GMMs, they often tend to have this curse of dimensionality and they will not uh model the data well. So that is because of the saturation of the EM algorithm. Again, I know I

### 00:23:09 · Speaker 4

since I'm not teaching G M M I'm not going into details of it but yeah okay there is a few sample from a G M M I I we'll talk about how do you sample from a from a variational auto encoder but yeah so what is more important is that one can use a latent variable model to do sampling or generation the other thing that can be used that that these models can be used is what is known as

### 00:23:34 · Speaker 1

Posterior inference

### 00:23:41 · Speaker 1

Posterior inference, okay?

### 00:23:46 · Speaker 1

also known as feature extraction, feature or embedding extraction.

### 00:24:01 · Speaker 1

becomes embedding extraction if

### 00:24:06 · Speaker 1

This is or it's also called as clustering.

### 00:24:13 · Speaker 1

if Z is discrete

### 00:24:21 · Speaker 1

Okay. Now what is this? So given

### 00:24:27 · Speaker 1

trained

### 00:24:31 · Speaker 1

latent variable model

### 00:24:37 · Speaker 1

Okay

### 00:24:42 · Speaker 1

and given

### 00:24:45 · Speaker 1

Data Point X

### 00:24:51 · Speaker 1

you just compute, compute

### 00:24:57 · Speaker 1

Q

### 00:24:57 · Speaker 5

Star Off

### 00:25:00 · Speaker 5

ZQ one X. That's all. So this, right, see what happens is, uh

### 00:25:05 · Speaker 4

if in the case of Q

### 00:25:12 · Speaker 4

let us say that way I compute or sample for me either both of them are possible I'll give you there are different variants of it okay let me tell you what it is compute

### 00:25:23 · Speaker 1

Hello

### 00:25:23 · Speaker 4

Okay

### 00:25:25 · Speaker 1

Q star of G given X

### 00:25:30 · Speaker 1

or sample from it.

### 00:25:38 · Speaker 1

depending upon what the case is.

### 00:25:40 · Speaker 4

Okay, so what do you mean by this?

### 00:25:44 · Speaker 4

So given a data point X, no, post training, given a data point X, I am finding out a distribution over the the latent variable given the data point.

### 00:25:56 · Speaker 4

Now let's say that that Z is discrete. Then what will happen? You take Z is discrete.

### 00:26:06 · Speaker 4

if C is discrete, we have values one through M. So C can take M values.

### 00:26:15 · Speaker 4

you can take one through M values. So if you are computing Q star

### 00:26:19 · Speaker 5

of z given x, what will happen is there will be a discrete distribution over z.

### 00:26:30 · Speaker 5

there will be an entire distribution over

### 00:26:32 · Speaker 5

See, what is this?

### 00:26:34 · Speaker 5

This is

### 00:26:35 · Speaker 1

is called clustering

### 00:26:40 · Speaker 4

So every x now is divided into one of m possibilities, right? That is that is clustering, okay? Now if z is continuous, then what will happen is given a

### 00:26:56 · Speaker 4

given an given an given an x okay. So you'll find out a z given x okay which is a sample from q of z given x. That particular star q of z given x. This will be a vector.

### 00:27:11 · Speaker 4

vector in some R K where that is where Z lies. So this is typically referred to as the embedding. So all these BERT embeddings etcetera that you see you know textual embeddings and image embeddings etcetera are nothing but samples from uh the posterior the latent posterior given data. So this is one other uh usage of latent variable models.

### 00:27:34 · Speaker 4

That is why you know we say that we can do clustering using G M M right so G M M is a latent variable model with discrete latent space okay and that's why we can do clustering of it either G M M or K means K means is a special case of G M M right all these are clustering methods but under the hood what is happening is that you are estimating Q star of Z Q N X so two things can be done right one you can do sampling or generation okay which is simply the generating

### 00:28:04 · Speaker 4

task that we were looking at. The other thing that you can do is what is called as posterior inference that is that given a particular point x you can find out q star of z given x. Is this okay? So these are two tasks. Yeah.

### 00:28:15 · Speaker 3

two

### 00:28:17 · Speaker 3

सर, इन द एम्बेडिंग केस, द रिसीव्ड वेक्टर विल बी अ वन हॉट वेक्टर, राइट?

### 00:28:23 · Speaker 4

No no no no no. uh I mean you mean the X you are talking about is it?

### 00:28:27 · Speaker 3

No sir, Z given A, the resultant vector

### 00:28:29 · Speaker 4

C.

### 00:28:31 · Speaker 4

vector. No no no no it is not a one one one hot no. See that's what I'm saying think of an auto encoder right you have an encoder decoder model I cover all that detail detail but I'm just giving you an overview here. So if you have like let's I mean if you know what BERT embeddings mean. There is a pre there is a trained model you pass it through a trained model right your X which can X can be one hot and you will you will get a particular vector at the output. That's all it is.

### 00:29:02 · Speaker 4

That vector is a sample from Z given X. Yeah, that's your embedding.

### 00:29:06 · Speaker 2

So why do you call it as a sample? So that means for a given x you can get a different values of z.

### 00:29:11 · Speaker 4

The reason I'm calling it as a sample is because in in in in whenever the the the

### 00:29:21 · Speaker 4

Latent variables are continuous, no? You won't get an entire distribution over Z given a particular X.

### 00:29:28 · Speaker 4

especially in in in in in in cases like BERT and all that. But as we will see in a VAE right? Q is modeled I mean you you you will get an entire distribution over Z okay? But typically when people call it as embedding extraction no it's always a sample from Q not an entire distribution. See I I just wanted to make this distinction that if Q is discrete then given an X you get an entire distribution over Q sorry G

### 00:30:01 · Speaker 4

Right? But when Q is continuous, typically, typically, uh what happens is you get a sample from Q star, not an entire distribution. I just wanted to make the distinction.

### 00:30:12 · Speaker 1

Okay.

### 00:30:14 · Speaker 4

any other question? So two, I mean remember these two things, no? I mean this is how the V A E paper starts also that the goal is to do two things that given data, you need to first learn a latent variable model, which is by maximizing the likelihood or elbow. Second task is to after you have completed your training, we need to do a generation, okay, a sampling and then we do posterior inference. So let me write it in the next thing itself.

### 00:30:40 · Speaker 3

Sir, which paper is it? What I forgot the name you mentioned.

### 00:30:45 · Speaker 4

Are you looking at my handwritten notes at all?

### 00:30:50 · Speaker 4

just asking. Because there I have like at the end of my every each notes. I'll tell you the name of that paper but I encourage all of you to actually look at my handwritten notes. It's very lucidly written.

### 00:31:00 · Speaker 0

It's very lucidly written. Kingman Williams.

### 00:31:04 · Speaker 4

come again

### 00:31:05 · Speaker 0

it's a kingma and willing

### 00:31:08 · Speaker 4

Welling and Kingmas paper I'll tell you the name see what's important is don't digress. What's important is that you all of you look at my handwritten notes. At the end of my handwritten notes key papers are listed and I expect and by the way for the exams I think this is the way to make you read right there is only one way. For your exams right all the papers that I have listed in my handwritten notes at the end of them they are they are a part of syllabus.

### 00:31:35 · Speaker 4

Okay so you are supposed to read those papers. There are only four five papers per topic so please read them. Yeah so the name of the paper is V I E's paper is auto encoding variational base.

### 00:31:51 · Speaker 4

If you Google for V A E original paper you'll get that but the title is auto encoding variational base. So please read my handwritten notes once. uh and you know the the citations that are given at the end of each chapter. I urge all of you to do that. Okay. So now the the uh problem here is that given D which is data.

### 00:32:16 · Speaker 4

samples

### 00:32:17 · Speaker 1

from

### 00:32:20 · Speaker 1

samples drawn I D from an unknown distribution P X, okay? The goal is threefold.

### 00:32:29 · Speaker 1

one

### 00:32:31 · Speaker 1

Learn

### 00:32:35 · Speaker 1

learn a latent variable model

### 00:32:42 · Speaker 1

but

### 00:32:47 · Speaker 1

unknown

### 00:32:51 · Speaker 1

and posterior, right? I mean this is

### 00:32:52 · Speaker 4

what it makes different from uh EM, okay? So if you read the introduction of that paper, no, they'll actually say that uh because P of P theta of Z given X is unknown, we are assuming that it is not known, uh we want an alternative method because otherwise, in fact, they explicitly say that EM cannot be used because we don't know what P theta of Z given X is, okay? That's the first goal. The second

### 00:33:18 · Speaker 1

goal is that you need to do

### 00:33:20 · Speaker 1

Uh

### 00:33:27 · Speaker 1

enable

### 00:33:29 · Speaker 1

generation

### 00:33:33 · Speaker 1

sampling, post training

### 00:33:46 · Speaker 1

third goal is to

### 00:33:50 · Speaker 1

enable posterior inference.

### 00:33:58 · Speaker 1

which is nothing but estimating Q star of the units.

### 00:34:05 · Speaker 4

Okay, so these are the three goals that are cited in the V I paper or maybe let me just show you that. It will be nice to see that once.

### 00:34:14 · Speaker 4

See a lot of times right we uh these uh B A E paper

### 00:34:24 · Speaker 4

these papers are sort of uh intimidating but one of the goals of this the the one of the goals of designing this particular course was to ensure that you people start reading papers students start reading papers and you know you don't get intimidated looking at it okay.

### 00:34:41 · Speaker 5

So they will say the following here

### 00:34:51 · Speaker 5

So we are interested in and propose a solution to three

### 00:34:54 · Speaker 4

problems in the above scenario, right? Efficient approximate maximum likelihood estimation for parameter parameters of theta. Let's not worry about map estimation. It's the efficient approximate maximum likelihood estimation of parameters of theta. Number one. The second thing is efficient approximate posterior inference of the latent variable given an observed value x for a choice of parameters theta. For a choice of parameters theta meaning post training. Right? This is useful for coding or data representation tasks. That is what is meant by

### 00:35:24 · Speaker 4

embedding extraction or representation learning. Second thing is you need to efficient approximate marginal inference of the variable X. Okay? This allows us to perform all kinds of inference tasks where a prior over X is required. Common application in computer vision include image denosing, inpainting and super resolution. All these are generative tasks.

### 00:35:47 · Speaker 4

Okay? So these are the three questions that is asked. So this is that paper, no, which is V A E's paper. We'll we'll go into all these details and math in a while. That is what we'll do in this lecture. But yeah, so these are the three questions that are that are of interest, which is learn a latent variable model with unknown V theta of Z given X. Oh, I should also show you that, no, that they say that E M is not feasible.

### 00:36:13 · Speaker 4

interactability look at this no? the first point here in one two. interactability. the case where the integral of the marginal is interactible. okay?

### 00:36:25 · Speaker 4

where the true posterior density P theta of the equation X is interactible. So the EM algorithm cannot be used.

### 00:36:31 · Speaker 4

that okay?

### 00:36:35 · Speaker 2

So it is intractable because we need to do it over all values of Z or

### 00:36:39 · Speaker 4

Well, not necessarily, right? I mean, for instance, if you assume Z to be a continuous variable with unknown distribution, it's you cannot find that integral. One thing. The other thing is, see, observe that P theta of Z given X involves a division by P theta of X.

### 00:36:56 · Speaker 4

which is again an integral over the joint distribution and this integral is over Z. So if you assume Z to be of very high dimensions, that integral cannot also be computed.

### 00:37:07 · Speaker 2

Okay, yeah, got it.

### 00:37:09 · Speaker 4

Yeah, so because that is why E M cannot be used here and we need something else rather than using E M. That's the prelude. So please read, see these are sort of seminal papers, okay, which are very good to read and you'll gain a lot of insights. I have gained a lot of insights by reading those papers as a student, so please do read them. I recommend all of you to read that. Similarly that F Gyan paper.

### 00:37:32 · Speaker 4

I don't know if I

### 00:37:35 · Speaker 4

showed you that. So we covered that no this if can

### 00:37:42 · Speaker 4

it's variational divergence minimization. Let's see. Yeah, this one. Training generating neural samplers using variational divergence minimization. So this is what we actually covered in class.

### 00:37:52 · Speaker 4

author. So this was the paper that I covered in class, all these lower bounds that we constructed, etcetera. So with the background that you have right now, please read the paper. It's it's it's short and extremely insightful.

### 00:38:07 · Speaker 4

Okay? I urge you to read all these, at least these fundamental seminal papers, okay?

### 00:38:14 · Speaker 4

Right. So we have these three objectives to learn given this data.

### 00:38:20 · Speaker 1

start doing it. Okay, so now

### 00:38:32 · Speaker 1

Recall

### 00:38:35 · Speaker 1

that

### 00:38:38 · Speaker 1

in a latent variable model.

### 00:38:49 · Speaker 1

each heat of X

### 00:38:52 · Speaker 1

given by integral of P theta

### 00:38:57 · Speaker 1

skill

### 00:38:57 · Speaker 5

times

### 00:39:00 · Speaker 5

in short of the whole DC, right?

### 00:39:04 · Speaker 1

equal to the

### 00:39:06 · Speaker 1

joint distribution of

### 00:39:11 · Speaker 1

Okay. Now the goal is to learn

### 00:39:16 · Speaker 1

learn theta star

### 00:39:18 · Speaker 1

that would

### 00:39:21 · Speaker 1

Man

### 00:39:21 · Speaker 5

the log of the likelihood

### 00:39:28 · Speaker 5

Right? So we saw that this is

### 00:39:32 · Speaker 5

Approximately

### 00:39:35 · Speaker 5

famous

### 00:39:38 · Speaker 5

finding out the

### 00:39:41 · Speaker 5

theta such that the lower bound on the evidence is maximized which is the

### 00:39:47 · Speaker 1

evidence lower bound where

### 00:39:56 · Speaker 1

Okay, F theta

### 00:40:00 · Speaker 1

Q is given by

### 00:40:03 · Speaker 1

the expectation of

### 00:40:04 · Speaker 5

Hello

### 00:40:05 · Speaker 1

Log off

### 00:40:08 · Speaker 1

P theta

### 00:40:10 · Speaker 1

X and Z divided by

### 00:40:13 · Speaker 1

Q of

### 00:40:16 · Speaker 1

Equinox

### 00:40:18 · Speaker 1

Hmm

### 00:40:21 · Speaker 1

with respect to

### 00:40:22 · Speaker 1

Q1 C Q1 X right

### 00:40:25 · Speaker 5

All of you with me so far?

### 00:40:30 · Speaker 5

Now we need to find the theta such that it is maximized, okay? Now let us simplify this.

### 00:40:41 · Speaker 5

Q to C given X.

### 00:40:43 · Speaker 5

Block

### 00:40:46 · Speaker 5

p theta x given

### 00:40:49 · Speaker 1

times period of Z divided by

### 00:40:58 · Speaker 1

Q of

### 00:40:59 · Speaker 1

See your X

### 00:41:02 · Speaker 1

is equal to expectation.

### 00:41:06 · Speaker 5

log of

### 00:41:08 · Speaker 5

p theta of x given z

### 00:41:12 · Speaker 5

QFC given

### 00:41:17 · Speaker 1

Minus

### 00:41:19 · Speaker 1

C one X

### 00:41:24 · Speaker 1

Loss

### 00:41:26 · Speaker 1

two of three given x divided by

### 00:41:29 · Speaker 4

Eighth year of C

### 00:41:32 · Speaker 4

Alright, I just used two things here, one, linearity of expectations and law of logarithms. Any questions on this step?

### 00:41:44 · Speaker 4

What did I do? There is log of A B divided by C. I wrote it as log A minus log C by log B. So minus came here because I

### 00:41:53 · Speaker 4

I inverted the

### 00:41:55 · Speaker 1

numerator and denominator

### 00:41:58 · Speaker 1

Is that all right?

### 00:42:10 · Speaker 1

Hello, are you there?

### 00:42:12 · Speaker 5

Yes sir

### 00:42:13 · Speaker 0

Yes

### 00:42:14 · Speaker 1

Is it all right? Any questions on this?

### 00:42:23 · Speaker 1

respond who do I know? uh maybe I'm not. This is all right no? Yeah okay.

### 00:42:28 · Speaker 4

okay, let's move on. So this is

### 00:42:34 · Speaker 4

expectation of law of

### 00:42:37 · Speaker 4

p theta x given c and this is with respect to given x minus what's the second term can can you recognize the second term

### 00:42:50 · Speaker 5

K L divergence of Q Z given. Yeah.

### 00:42:53 · Speaker 4

and the

### 00:42:55 · Speaker 5

Suzuki L Divergence

### 00:42:58 · Speaker 5

between q of z given x and

### 00:43:02 · Speaker 5

period of C. Yeah.

### 00:43:05 · Speaker 4

this

### 00:43:07 · Speaker 4

Actually the loss function of a V I okay this is thing but elbow right we are writing the evidence like evidence lower bound expressing this this way so this if you want to remember something this is something that you would want to remember this is

### 00:43:21 · Speaker 1

free

### 00:43:25 · Speaker 1

conditional

### 00:43:30 · Speaker 1

Long likelihood

### 00:43:35 · Speaker 1

Okay, let me

### 00:43:35 · Speaker 4

interpreted later, okay? So this is the equation. So you have elbow can be decomposed into two terms. One which is an expectation of log of p theta of z given x given z and there is a KL divergence between q of z given x and p theta of z, okay?

### 00:43:52 · Speaker 5

Now

### 00:43:53 · Speaker 4

Now what is done in VAE is that

### 00:43:56 · Speaker 1

So first thing that you do is, uh

### 00:44:05 · Speaker 1

Approximate

### 00:44:13 · Speaker 5

सर, वन क्वेश्चन।

### 00:44:15 · Speaker 1

talk

### 00:44:16 · Speaker 5

for this to be cleared

### 00:44:17 · Speaker 3

divergence there should be a p theta of z term also right before log

### 00:44:23 · Speaker 4

No no no. It should be a Q of G given its term.

### 00:44:28 · Speaker 3

Yes, Q, Q of Z given X.

### 00:44:30 · Speaker 4

expectation is there no? expectation is integral q zero q by x log of q by p, isn't it?

### 00:44:37 · Speaker 3

Okay, okay.

### 00:44:40 · Speaker 5

It is

### 00:44:44 · Speaker 1

is integral u j given x

### 00:44:47 · Speaker 1

log of closing given x divided by

### 00:44:51 · Speaker 1

printed

### 00:44:55 · Speaker 5

Yes sir

### 00:44:57 · Speaker 5

That's KL, no?

### 00:44:58 · Speaker 1

Yes

### 00:45:00 · Speaker 5

okay. Now okay so what's important now is that you approximate p theta of z sorry p theta of x given z

### 00:45:11 · Speaker 5

Okay? And

### 00:45:15 · Speaker 1

q of z given x

### 00:45:18 · Speaker 1

using

### 00:45:20 · Speaker 1

Neural Networks

### 00:45:28 · Speaker 1

let's call that as Q phi because there are two

### 00:45:31 · Speaker 4

neural networks, neural networks, theta, neural networks with parameters theta and phi.

### 00:45:38 · Speaker 4

Okay. So what we do is, see look at this elbow, right? There are two distributions that we are talking about here, which is Q of Z given X, which is the unknown posterior. Okay. The other thing is P theta, other thing is P theta of X given Z. So we represent both of them using neural networks. Now, observe the difference here from the EM algorithm, right? In EM algorithm, Q of Z given X, the optimal Q of Z given X was known to be P theta of Z given X. Here we

### 00:46:08 · Speaker 4

because because we don't know what P theta of Z given X is. We approximate that using a neural network. Now the question is what do you mean by approximating okay let me write that.

### 00:46:19 · Speaker 1

What's important is question

### 00:46:25 · Speaker 1

Okay. What is

### 00:46:30 · Speaker 1

What is meant by

### 00:46:35 · Speaker 1

approximating distributions using neural network, neural networks.

### 00:46:41 · Speaker 1

proximating distributions.

### 00:46:48 · Speaker 1

using neural networks

### 00:46:57 · Speaker 1

is very important. There are two ways here, right? See, one way is that there is a there is a probabilistic way, okay?

### 00:47:12 · Speaker 1

and there is a deterministic way.

### 00:47:22 · Speaker 1

Okay. Now what do you mean by a problem?

### 00:47:24 · Speaker 5

globalistic way, let's say that there is a neural network here.

### 00:47:29 · Speaker 5

Now this

### 00:47:32 · Speaker 1

is Q fee

### 00:47:35 · Speaker 1

of Z given X.

### 00:47:45 · Speaker 1

Okay. Now this takes

### 00:47:48 · Speaker 1

sample of Z as input. Okay, so Z

### 00:47:56 · Speaker 4

The neural networks are deterministic functions which is that you know, uh you give a fixed input, it will give you a fixed output always, right? So now a sample of Z, sample of X, sorry.

### 00:48:09 · Speaker 4

a sample of X it takes as an input and what it gives out are

### 00:48:16 · Speaker 1

the parameters

### 00:48:22 · Speaker 5

of

### 00:48:22 · Speaker 1

of

### 00:48:24 · Speaker 1

distribution

### 00:48:27 · Speaker 4

Q of Z given X. So this is typically called as the probabilistic neural network. Where a neural network, okay, will give you the parameters of a distribution. Now typically let's say as an example...

### 00:48:43 · Speaker 4

If

### 00:48:44 · Speaker 4

if q of g given x

### 00:48:47 · Speaker 4

is assumed to be let's say a Gaussian of some mean and variance.

### 00:48:54 · Speaker 4

Okay. This neural network will give you mean and variance as output.

### 00:49:00 · Speaker 4

makes sense.

### 00:49:04 · Speaker 4

So this is called the probabilistic way of representing a distribution using a neural network. Okay? A neural network will give you the parameters of a distribution. So note that in most of the probabilistic ways of representation, right? You assume the underlying distributional form for the for the distribution that you are assuming, okay? What you you make your neural network output the parameters of the distribution. So that is probabilistic way. Okay. There is a deterministic way which

### 00:49:37 · Speaker 1

you have already seen, right, which is

### 00:49:47 · Speaker 1

other way around because typically in late

### 00:49:52 · Speaker 4

variable models at least, x will have a larger dimension compared to z.

### 00:50:01 · Speaker 4

doesn't matter but yeah so just to ensure that it is consistent. So if you are doing it in deterministic way let's say that you are modeling some

### 00:50:09 · Speaker 5

p theta of x given c, right? Now it will take a sample of

### 00:50:19 · Speaker 5

give a sample of Z. Okay. It will give you what what will you give you what will a determination network give? It will give you a sample.

### 00:50:44 · Speaker 1

simply give you a sample, okay, x cap

### 00:50:49 · Speaker 4

from P theta of X given C. This is the deterministic curve. So here the neural network is not giving you parameters of the distribution but it is giving the samples from the distribution. For example...

### 00:51:03 · Speaker 4

is a GAN generator, no?

### 00:51:08 · Speaker 4

A GAN generator is is a is a deterministic neural network. I mean all neural networks are deterministic that way. But a GAN generator is modeling the conditional data distribution in a deterministic sense. So what do I mean by that? I mean to say that uh that it will give you a sample from

### 00:51:26 · Speaker 5

from the distribution that it is modeling but not the parameters of it.

### 00:51:36 · Speaker 3

सर, बट फॉर अ गिवेन ज़ेड आल्सो, लेट्स दिस द सैंपल एक्स विल बी डिफरेंट, राइट?

### 00:51:44 · Speaker 4

No no no not in a in a GAN. In a GAN right if you fix Z it will always get the same X no? Because neural networks are deterministic functions.

### 00:51:57 · Speaker 4

That's the whole point that I'm trying to make. See, uh the uh the uh variability in the generated data comes because Z has random uhness into it, right? Because we know that Z typically is sampled from uh a content distribution. That's why different Z will give you different Xs. But post training, a GAN generator or for that matter any neural network is a fixed function, right?

### 00:52:21 · Speaker 4

For a given fixed input, it will give you a fixed output. There is no

### 00:52:23 · Speaker 1

stochasticity in a neural network by design

### 00:52:33 · Speaker 1

Does it make sense?

### 00:52:36 · Speaker 2

So one question, so in the probabilistic way, so we estimate only the parameters for only one distribution or a family of or a or a group of distributions?

### 00:52:46 · Speaker 4

Yeah. See, uh it is it is one distribution in the sense that if you are looking at Q phi of Z given X, right? Q phi of Z given X is actually Q phi of Z given one particular X always, isn't it?

### 00:53:04 · Speaker 3

Yes

### 00:53:04 · Speaker 4

this mu and sigma will be a function of x. Okay. Right? For a particular x. But if you are saying that you know the same neural network neural network is being used to estimate the Q phi of Z given x for different values of x then you are estimating it for a family and that's what is happening.

### 00:53:08 · Speaker 3

Okay, right?

### 00:53:24 · Speaker 4

because once you train given one particular x it will give you the parameters of q phi of z given that particular x

### 00:53:34 · Speaker 2

Yes

### 00:53:35 · Speaker 4

Yeah. Okay. See, it it

### 00:53:37 · Speaker 2

it generates a family itself, right? And

### 00:53:40 · Speaker 4

Right. I mean see, for a given x it does not generate a family.

### 00:53:45 · Speaker 2

Yes, correct.

### 00:53:46 · Speaker 4

should be clear about it. When you say, see, there is no stochasticity associated with the neural network. So for a fixed X, it will give you a fixed output. Now, in the probabilistic way, what will happen is that there will be para that that will be seen as parameters of impact. How do you do it practically is that suppose mu X is, let's say that, uh like Z is in some K dimensions, right? Then what we'll do is this output, this neural network will have K

### 00:54:16 · Speaker 4

plus k squared uh dimensional output no because sigma will have k squared parameters mu will have k parameters it will be k plus k squared stacked into a long vector that is the output. Okay. So now one for one x it will give you one uh output and that can be interpreted as the parameters of a distribution. So it is it is it is modeling a family in the sense that for every x it will give you parameters corresponding to that.

### 00:54:45 · Speaker 2

Yeah, got it.

### 00:54:46 · Speaker 4

Yeah. So I'll ask you a question now. What do you think what way do you think these are the only two ways that you model uh that that you use neural networks in any task, okay? Here is a question. What do you think a classifier, a K class classifier is doing? Is it a probabilistic

### 00:55:03 · Speaker 1

model or a deterministic model

### 00:55:18 · Speaker 1

probability stick. probability stick.

### 00:55:19 · Speaker 5

Six

### 00:55:21 · Speaker 5

Why do you think it's a problematic model?

### 00:55:28 · Speaker 1

because what

### 00:55:28 · Speaker 5

What is the classifier model by the way? What distribution is a classifier model?

### 00:55:32 · Speaker 4

only. Take a classifier, what distribution does it model? You'll take an x as an input, what is what distribution is it modeling?

### 00:55:42 · Speaker 3

Underlying

### 00:55:42 · Speaker 2

giving you the probability of the classes.

### 00:55:48 · Speaker 5

This is what it models, right?

### 00:55:51 · Speaker 5

all classifiers model p three of y given x

### 00:55:58 · Speaker 5

Correct?

### 00:56:02 · Speaker 5

In fact, the so-called cross entropy laws

### 00:56:04 · Speaker 4

that you use is actually minimization of KL divergence, no? Actually it's minimization of KL divergence between the true posterior, label posterior, okay? And the neural network model posterior. This is exactly what you do, right? When you minimize, this is cross entropy because the other term which is the entropy term will be independent of theta. The first term, right, which is expectation of log of

### 00:56:33 · Speaker 4

p theta of y given x with respect to p of y given x. This is what you minimize, negative of this is what you minimize, which is the cross interpolator, which is nothing but the KL divergence.

### 00:56:44 · Speaker 4

right? So, uh even a classifier is doing the same thing that we are doing, right? It is doing a maximum likelihood estimation or minimizing the case divergence. But now the output, what do you get? Do you get a sample from this distribution or do you get the parameters of this distribution?

### 00:57:01 · Speaker 4

So let's say that Y is a discrete distribution that will take one out of K values. Okay? uh with

### 00:57:11 · Speaker 4

probabilities uh P Y one, P Y two up to P Y K. So post training when you do an inference for a particular X, uh what do you get at the output? Do you get a sample from the P theta of Y given X or do you get parameters of P theta of Y given X?

### 00:57:34 · Speaker 5

get a sample.

### 00:57:37 · Speaker 4

What do you say so?

### 00:57:39 · Speaker 4

Do you get one of the see that depends okay the okay so here is the answer right the way to look at it is. So if you look at the entire classifier so suppose you take the final layer to be the arg max of logics.

### 00:57:55 · Speaker 4

Okay, then it is a sample.

### 00:57:58 · Speaker 5

right? But if you stop at logits,

### 00:58:03 · Speaker 5

then it's actually a distribution probabilistic way.

### 00:58:09 · Speaker 5

You see that?

### 00:58:11 · Speaker 4

take the large hits right then it's it it sums to one right and it's all all non negative

### 00:58:17 · Speaker 4

Okay, which is the softmax. So if you take the output of the softmax, which is the logits, no, even before the softmax, if you take the logits, then it's an entire distribution, okay? You can see that as, you can interpret that as parameters. If you take the argmax, okay? Take the softmax and then take the argmax of all possible values, then it becomes a sample of this different distribution.

### 00:58:43 · Speaker 4

Anyway, so

### 00:58:45 · Speaker 4

something that I intended to say but anyway so these are two ways to model distributions right one is the probabilistic way where the neural network gives you samples from the distribution that it is modeling and the deterministic way where the neural network will give you samples from the distribution that it is modeling okay

### 00:59:03 · Speaker 1

Now what do we do in a VAE

### 00:59:13 · Speaker 1

Q

### 00:59:15 · Speaker 1

P, right? Distribution Q, P of Z given X, okay?

### 00:59:20 · Speaker 1

is modeled

### 00:59:29 · Speaker 1

there are multiple instantiations of it okay. let me write it. U F G given X.

### 00:59:39 · Speaker 1

plus

### 00:59:41 · Speaker 1

model probabilistically

### 00:59:53 · Speaker 1

realistic

### 00:59:58 · Speaker 1

Okay

### 01:00:00 · Speaker 0

and P heat of X given Z

### 01:00:06 · Speaker 0

is modeled

### 01:00:12 · Speaker 4

using either probabilistic or deterministic, you know, as the case may be. Yeah. I I'll tell you, there these are different instantiations of same idea, right? Probabilistic or

### 01:00:23 · Speaker 4

deterministic neural networks. So basically both of them are modeled. Q phi of Z given X is always modeled probabilistically. Okay, P theta of Z given X can be modeled probabilistically or in a deterministic way. Okay, let us see one instantiation where we have

### 01:00:41 · Speaker 4

Okay, so now data

### 01:00:44 · Speaker 4

set of exercise

### 01:00:47 · Speaker 4

you have enough of them

### 01:00:49 · Speaker 4

sampled from V X U R, right? Now typically X is in some R D.

### 01:00:57 · Speaker 4

in all latent variable models, Z is assumed to be in some R K, okay? where K is much less than

### 01:01:05 · Speaker 1

Right

### 01:01:07 · Speaker 4

That is how it is done in latent variable models.

### 01:01:10 · Speaker 0

what will happen is there is a neural network

### 01:01:28 · Speaker 0

this neural network takes X I as

### 01:01:31 · Speaker 3

as input. One of the exercise as input. And this is modeling Q P of Z given exercise.

### 01:01:42 · Speaker 4

Right. Now this is as I said it will model it probabilistically. So in one of the instantiations of I mean one of the naive implementations of VAE.

### 01:01:54 · Speaker 3

Oil

### 01:01:55 · Speaker 4

Now Q

### 01:01:57 · Speaker 3

p of z equals x

### 01:02:00 · Speaker 3

is assumed to be a Gaussian

### 01:02:05 · Speaker 3

It's a distribution in Z. The mean of this is mu

### 01:02:12 · Speaker 3

Off

### 01:02:12 · Speaker 4

X because it's a function of X. The variance is a function of X. So

### 01:02:19 · Speaker 4

typically it is assumed to be a you can model it to be a diagram

### 01:02:23 · Speaker 3

straightener matrix, okay?

### 01:02:27 · Speaker 0

diagonal matrix of

### 01:02:32 · Speaker 0

Sigma one through Sigma K

### 01:02:38 · Speaker 0

Let us call this as signal of x sigma x vector, okay?

### 01:02:47 · Speaker 0

how

### 01:02:47 · Speaker 3

what will happen is that in a in a in a in a V A E this will get mu

### 01:02:56 · Speaker 3

of X I as the output.

### 01:02:59 · Speaker 3

of sigma of x i as the output, okay? Now note that both

### 01:03:07 · Speaker 4

mu x and sigma x lie in k dimensional spaces, right? Because I've assumed sigma x to be a diagonal matrix, they both lie in k dimensional spaces. That means that the the output of this, you know, this will be a

### 01:03:24 · Speaker 3

D dimensions, this will be

### 01:03:28 · Speaker 3

2K dimensions

### 01:03:32 · Speaker 3

Okay? This is, uh, this is also called the the encoder network, huh?

### 01:03:43 · Speaker 3

simply modeling Q phi of g given x using neural networks. But there is another neural network, we said that we also model p theta.

### 01:03:52 · Speaker 3

So this will take Z I which is a sample from Q phi of Z given X I.

### 01:04:01 · Speaker 3

as input. And then this will model P theta of

### 01:04:05 · Speaker 3

x given z. Now let's say that this gives you a sample.

### 01:04:12 · Speaker 3

in this case I'm assuming that this is model

### 01:04:14 · Speaker 0

deterministical. Okay, this network is also called a

### 01:04:40 · Speaker 0

Okay

### 01:04:43 · Speaker 0

this will take Z I

### 01:04:44 · Speaker 0

samples

### 01:04:46 · Speaker 3

some QVF

### 01:04:49 · Speaker 3

given X I as an input, okay? And this this network is also

### 01:04:52 · Speaker 0

Defolder network

### 01:05:01 · Speaker 0

This is a V I E, okay? uh Now, one thing that is

### 01:05:05 · Speaker 4

to be noted here is

### 01:05:08 · Speaker 4

Of course, this is K dimensional. This will be D dimensional. Okay? Now see, one thing that is to be noted here is, I will tell you,

### 01:05:16 · Speaker 0

start

### 01:05:19 · Speaker 0

There is no

### 01:05:25 · Speaker 0

direct connection

### 01:05:34 · Speaker 0

between the

### 01:05:40 · Speaker 0

decoder networks

### 01:05:43 · Speaker 0

Okay

### 01:05:45 · Speaker 4

they are not connected

### 01:05:46 · Speaker 3

Hello

### 01:05:47 · Speaker 4

at all, right? So what is happening is given an X I, okay? So you first get the the parameters of the distribution Q phi of Z given X.

### 01:05:57 · Speaker 4

Then, having those parameters, you sample a Z I from Q phi of Z given X, okay? And give that Z I as an input to the decoder to get a sample from P theta of X given Z.

### 01:06:12 · Speaker 4

Here, uh the output of the encoder, right, does not go as an input to the decoder.

### 01:06:19 · Speaker 4

Do you see that?

### 01:06:22 · Speaker 4

the output of the encoder does not go as an input to the decoder. I should write that. So this this means that

### 01:06:30 · Speaker 0

the output

### 01:06:32 · Speaker 3

Hello

### 01:06:32 · Speaker 0

of the encoder

### 01:06:41 · Speaker 0

present

### 01:06:46 · Speaker 0

who are

### 01:06:48 · Speaker 0

an input

### 01:06:52 · Speaker 0

to the depot

### 01:06:59 · Speaker 0

Is the setup clear now what is happening?

### 01:07:05 · Speaker 4

Yeah, we'll have to now see how to uh train this or rather how to get the parameters by optimizing the elbow and also we have to see how to do generation and inference later post. I mean because you remember no we had these three goals that you learn a latent variable model, enable generation and enable posterior inference. We'll see all that to be done. But in terms of like architecture is all of you clear on what is happening?

### 01:07:31 · Speaker 5

So the input to the decoder is a sample from Q of Z given X

### 01:07:36 · Speaker 4

q p given x correct

### 01:07:40 · Speaker 5

So we indirectly use it, right? Because, uh, no, we do distribution.

### 01:07:42 · Speaker 4

No, we do. I'm not saying we don't use the encoder network. I'm saying that the output of the encoder does not go as an input to the decoder.

### 01:07:53 · Speaker 4

I didn't say that we are not using the encoder. Encoder is very much used.

### 01:07:58 · Speaker 5

Okay, but it's used to only determine the parameters of the distribution. And then we sample

### 01:08:03 · Speaker 4

it is used to implement parameters of the distribution and using those parameters you sample, okay? and once you sample, use that sample as a

### 01:08:11 · Speaker 3

input to the decoder

### 01:08:13 · Speaker 4

Yeah, got it.

### 01:08:19 · Speaker 2

सर आई हैव वन क्वेश्चन

### 01:08:21 · Speaker 3

Tag one

### 01:08:22 · Speaker 2

for Q P Z of X, we say that it is a normal distribution on the variable Z with mean mu X and uh sigma variance sigma X. So why this mu uh mean and variance are on the or on X, they should be on Z, right?

### 01:08:41 · Speaker 4

no no no. They are, see they are, okay. I mean that they are functions of x.

### 01:08:47 · Speaker 4

See, look at this, no? I've said that both of them lie in R K, which means that they are in V space, but they are functions of X.

### 01:08:50 · Speaker 2

Yeah

### 01:08:54 · Speaker 4

When I write of a thing, it means that they are functions. I'm talking about them being functions of it.

### 01:08:54 · Speaker 2

Okay

### 01:08:58 · Speaker 2

talking about

### 01:09:02 · Speaker 2

Okay, but they are, but they are over the, since

### 01:09:07 · Speaker 4

absolutely

### 01:09:07 · Speaker 2

absolutely. They are also K dimension.

### 01:09:08 · Speaker 4

Absolutely, Absolutely.

### 01:09:10 · Speaker 2

Okay

### 01:09:11 · Speaker 4

See, neural network is taking an X-ray as an input, no? That they are, that's why it's a function of X.

### 01:09:19 · Speaker 3

Got it sir

### 01:09:22 · Speaker 4

So I mean I want all of you to like strictly understand this you know clearly understand what's happening otherwise everything that we do next will not make sense. So please ask me questions if you have. uh on on how this thing works. I mean architecture. Yeah.

### 01:09:37 · Speaker 5

K is again a hyperparameter here or

### 01:09:41 · Speaker 4

A is a hyperparameter. Yes.

### 01:09:45 · Speaker 5

sorry one query. here the decoder network we have found out deterministically right?

### 01:09:52 · Speaker 4

see we are just yeah yeah we have at least in this exam instantiation I have made this deterministic because I say that it gives you a sample from P data of X P M C yeah

### 01:09:53 · Speaker 5

you know

### 01:10:05 · Speaker 5

Okay, does it maybe you might cover it later, you can say that. I mean like whether it changes when you do it probabilistically. If that

### 01:10:13 · Speaker 4

Yeah, you simply get the parameters of P theta of X given zero. That's all.

### 01:10:18 · Speaker 5

Okay

### 01:10:19 · Speaker 4

Instead of getting a sample from P theta of X given Z, you get parameters of P theta of X given Z, then it becomes a probabilistic thing.

### 01:10:27 · Speaker 5

Got it. Then again from that parameter we again use that into

### 01:10:31 · Speaker 4

you do sampling but typically right in a in a naive implementation of V A E the output of the decoder itself is taken as a sample from P theta of X given Z.

### 01:10:45 · Speaker 4

But yeah, so later, like in the class, no, I will also give you one example where it is taken deterministically as well. But for now, let us think that it is, I mean, sorry, the probabilistic, for now, let us think that it is deterministically.

### 01:10:59 · Speaker 5

Sure, Thank you Sir

### 01:11:01 · Speaker 4

Lokesh

### 01:11:03 · Speaker 1

Yeah. Sir, so for a given X I, the X I cap which we get from P theta might be different, right? Because we have a sampling step in between. And that might lead to a difference in X I.

### 01:11:15 · Speaker 4

and that might lead to a different

### 01:11:17 · Speaker 4

I am not even saying that you get like X I at the output of the decoder, right? Decoder will just give you a sample from P theta vector. I have not established any relationship between X I and X I cap yet.

### 01:11:29 · Speaker 1

Okay

### 01:11:32 · Speaker 4

Okay, if your question is, you know, where is that so-called quote unquote auto encoding happening here, right? We will see that. We will see how to how does it come out, okay?

### 01:11:42 · Speaker 1

Okay

### 01:11:45 · Speaker 4

Sorry

### 01:11:47 · Speaker 5

So this sampling process of lead from Q of P, right? So is it like generally having a random sample using like a random function from that thing or is there a specific process?

### 01:11:57 · Speaker 4

is there a specific process? Yeah, yeah, you you use the standard samplers. So you can suppose if you model your Q to be a Gaussian distribution, then you can use that like standard random sampler for this.

### 01:12:14 · Speaker 3

Okay, so is the setup clear to all of you? Now what we should do is like with this

### 01:12:25 · Speaker 3

with this. Now the elbow will become a function of

### 01:12:31 · Speaker 3

Yeah

### 01:12:31 · Speaker 4

θ and φ which is given by the expectation of log of eθ of x given z and this is with respect to qφ of z given x minus

### 01:12:47 · Speaker 3

k l divergence between

### 01:12:51 · Speaker 3

q v of 0 1 x

### 01:12:54 · Speaker 3

and

### 01:12:56 · Speaker 3

P T dot C. Okay? This is what it is. What we should do is that like

### 01:13:03 · Speaker 3

should solve this, you know, theta star

### 01:13:05 · Speaker 0

Hello

### 01:13:06 · Speaker 3

and we start

### 01:13:07 · Speaker 0

first

### 01:13:11 · Speaker 0

simply the

### 01:13:20 · Speaker 3

what we need, right? We need to train both of these neural networks. So how how do we do that? We do it using gradient descent, right? So we need

### 01:13:30 · Speaker 3

the

### 01:13:31 · Speaker 4

gradient of

### 01:13:33 · Speaker 4

elbow

### 01:13:35 · Speaker 4

with respect to phi and we need gradient

### 01:13:39 · Speaker 3

of

### 01:13:41 · Speaker 4

the elbow with respect to theta. This is what we need, right? Because

### 01:13:45 · Speaker 0

finally what we do is this is how we train the neural networks

### 01:14:08 · Speaker 0

assuming that we are simply doing a SGD right first order gradient descent

### 01:14:17 · Speaker 4

as you do it. So we need the gradients of the elbow with respect to both phi and theta under this uh I think somehow the pages are sizes are going haywire.

### 01:14:35 · Speaker 4

I should not zoom out and zoom in arbitrarily I think, yeah. Let's keep it this way. Okay. So now with this modeling choice that we have made, no, we have to ensure that we get the gradients of the the lower bound with respect to phi and with respect to theta, okay? And then we can of course uh use gradient descent tool uh to try both of these networks. Is this all right? Now what we will do in the rest of the classes, so getting this gradient right with respect to gradient of the elbow with respect to

### 01:15:05 · Speaker 4

is a non-trivial thing. uh and you might have heard this term reparameterization, right? It is used in V I E, like so-called reparameterization. That comes into picture to calculate this gradient, that's all. So calculating this gradient with respect to calculating the gradient of elbow with respect to the encoder parameters needs this idea called reparameterization because of a simple fact. Look at this, no?

### 01:15:31 · Speaker 4

See the there is a sampling step that is involved, okay, which cannot be differentiated so. I I will show all that you know very rigorously, but the basic idea is that

### 01:15:42 · Speaker 4

There is a sampling step and the encoder encoder and decoder are connected via the sampling step but sampling is a non differentiable operation. When you back propagate no through chain rule you have to back propagate let's say you start from the output of the decoder back propagate all the way through the input of the decoder. From there you should go to the output of the encoder and those two are connected via sampling but sampling is a non differentiable operation so what do you do to find the uh the gradient of the

### 01:16:12 · Speaker 4

with respect to the encoder parameters is what we should look at next. Okay. That is done through this trick called reparameterization trick that I will discuss.

### 01:16:22 · Speaker 4

ओके, सो आई थिंक शैल वी टेक अ ब्रेक? फिफ्टीन मिनट्स ब्रेक।

### 01:16:27 · Speaker 4

ten forty ten forty eight no

### 01:16:30 · Speaker 4

Good Time To Stop. Ya Raghavendra.

### 01:16:34 · Speaker 5

Sorry. There was no question.

### 01:16:37 · Speaker 4

Oh, I missed it.

### 01:16:38 · Speaker 4

mistake. Okay. Yeah, shall we

### 01:16:40 · Speaker 4

take a break

### 01:16:43 · Speaker 4

Satya, go ahead.

### 01:16:45 · Speaker 3

Yes sir, you can they can take a break. I have one question on the assignment.

### 01:16:50 · Speaker 4

Uh

### 01:16:51 · Speaker 3

Uh, cough

### 01:16:53 · Speaker 4

maybe later. after the class. Yeah, please do ask me after the class. Okay, so now, uh yeah, it is ten forty nine in my clock. We started late today, no, twenty minutes late. So let's cut down the break. Let's get back at eleven five, okay?

### 01:16:55 · Speaker 3

class

### 01:16:56 · Speaker 3

Please

### 01:17:09 · Speaker 4

in fifteen minutes. Let's come back, let's come back at eleven five and finish the repair parameters. So don't miss the next part of the class, no, it's pretty important. Okay.

### 01:17:18 · Speaker 0

See you in fifteen minutes then. Bye.

### 01:35:24 · Speaker 0

Hello

### 01:35:25 · Speaker 0

Shall we continue?

### 01:35:29 · Speaker 3

Yes sir

### 01:36:04 · Speaker 0

Okay

### 01:36:10 · Speaker 3

So, uh, tell me now, right?

### 01:36:19 · Speaker 3

Can you hear me?

### 01:36:20 · Speaker 0

Yes sir. Yes sir.

### 01:36:22 · Speaker 3

Okay, thanks. Okay, so we were looking at

### 01:36:25 · Speaker 4

now computing the gradients of the encoder and decoder parameters with respect to sorry computing the gradients of ELBO with respect to the encoder and decoder parameters okay. Now okay so what do we so let's take one term at a time no there are two terms in ELBO.

### 01:36:47 · Speaker 4

So consider

### 01:36:51 · Speaker 0

computing

### 01:37:06 · Speaker 0

computing the

### 01:37:12 · Speaker 0

gradients

### 01:37:16 · Speaker 0

of elbow

### 01:37:28 · Speaker 0

with respect to P and theta

### 01:37:34 · Speaker 0

Okay

### 01:37:44 · Speaker 0

Okay. You consider the first term in the elbow, consider.

### 01:37:49 · Speaker 0

the first term in the elbow

### 01:38:02 · Speaker 0

which is the expectation of

### 01:38:06 · Speaker 0

log of

### 01:38:08 · Speaker 0

p theta of x given the

### 01:38:14 · Speaker 0

with respect to

### 01:38:16 · Speaker 0

U V of C finex, okay?

### 01:38:20 · Speaker 0

Right? Now,

### 01:38:45 · Speaker 0

How does it look like? Suppose, um looks something like this, you know, this the above.

### 01:39:00 · Speaker 0

like

### 01:39:04 · Speaker 0

you have an expectation of, okay?

### 01:39:08 · Speaker 4

some function

### 01:39:11 · Speaker 4

please note that this z you know what is this z here x given z what is this z this z

### 01:39:21 · Speaker 4

C is being sampled from Q phi of Z given X, right?

### 01:39:27 · Speaker 4

Right? So, this entire thing, whatever the log of p theta of x given z is, you know, that is also a function of p.

### 01:39:40 · Speaker 4

Do you understand that? Please let me know if you don't understand. So this is of some random variable V. Okay? And the expectation is with respect to a distribution. Okay? P V and this is also a function of P.

### 01:40:00 · Speaker 0

just giving you a simpler example

### 01:40:07 · Speaker 0

Ringgit

### 01:40:15 · Speaker 0

Let me use a different parameter.

### 01:40:19 · Speaker 4

let's call this as some

### 01:40:20 · Speaker 3

and we have some distribution

### 01:40:25 · Speaker 3

on this random variable B. Do you agree that it looks like this? Any questions on this?

### 01:40:35 · Speaker 3

okay let me write it down maybe. It will be easier that way.

### 01:40:39 · Speaker 0

here

### 01:40:44 · Speaker 3

F psi of V is actually

### 01:40:48 · Speaker 3

log

### 01:40:50 · Speaker 3

p theta of x q one z okay na? And then p psi of v is simply

### 01:41:01 · Speaker 3

Thank you

### 01:41:02 · Speaker 0

Yes

### 01:41:04 · Speaker 0

V is V, okay? And psi is

### 01:41:11 · Speaker 0

Is this okay?

### 01:41:20 · Speaker 0

Hello, am I audible?

### 01:41:25 · Speaker 0

ओके. फाइन. सो

### 01:41:26 · Speaker 3

So

### 01:41:27 · Speaker 0

Now what we need is that we need the gradients of this expectation

### 01:41:43 · Speaker 0

This gradient has to be with respect to the parameters, right? Correct?

### 01:41:47 · Speaker 4

is what we are seeking. So let us write this term. So this is equal to

### 01:41:52 · Speaker 2

Sir, sorry to interrupt. Instead of going for psi, can't we straight away use the like like phi? Otherwise, it will be it will be a bit confusing.

### 01:41:54 · Speaker 4

I should

### 01:42:04 · Speaker 4

the reason I didn't use phi was, you know, phi has been taken as encoder parameters. I can do that.

### 01:42:12 · Speaker 4

Hmm

### 01:42:15 · Speaker 4

Let us keep it that way, no? I have written it down. So let us have it this way.

### 01:42:17 · Speaker 0

Hello

### 01:42:19 · Speaker 0

Okay

### 01:42:19 · Speaker 3

this is equal to

### 01:42:24 · Speaker 3

the

### 01:42:26 · Speaker 3

gradient

### 01:42:31 · Speaker 0

of integral

### 01:42:35 · Speaker 0

respect to each, we have

### 01:42:39 · Speaker 4

P psi of V times

### 01:42:42 · Speaker 4

P psi of V D V, right? This is definition of expectation. And we can move the gradient inside because expectation is a linear operator, right? We can move the gradient inside. This will be P psi of V times

### 01:43:01 · Speaker 4

So you have to be correct

### 01:43:03 · Speaker 0

TV

### 01:43:06 · Speaker 0

Now what do we do now next? Can somebody tell me?

### 01:43:19 · Speaker 0

chain rule. We use chain rule. This is

### 01:43:32 · Speaker 0

gradient of

### 01:43:35 · Speaker 0

the gradient of

### 01:43:38 · Speaker 0

One function

### 01:43:40 · Speaker 0

times

### 01:43:44 · Speaker 0

is I of V DV

### 01:43:48 · Speaker 0

Plus

### 01:43:53 · Speaker 0

the gradient of

### 01:43:56 · Speaker 0

the other function

### 01:44:07 · Speaker 0

times

### 01:44:13 · Speaker 0

Correct?

### 01:44:17 · Speaker 0

is what it is, right? Now, what is the

### 01:44:20 · Speaker 4

the first term. Look at the first term, right? You have

### 01:44:26 · Speaker 4

some function here and a probability distribution here. What is that and there's an integral. What is that? This is an

### 01:44:33 · Speaker 3

expectation of

### 01:44:36 · Speaker 3

Okay

### 01:44:36 · Speaker 0

ingredient

### 01:44:41 · Speaker 3

with respect to

### 01:44:43 · Speaker 3

of V

### 01:44:45 · Speaker 3

Okay

### 01:44:47 · Speaker 3

this is not an expectation.

### 01:44:50 · Speaker 3

this the first term now can be approximated using

### 01:44:55 · Speaker 3

one over

### 01:44:55 · Speaker 4

N

### 01:44:58 · Speaker 4

one through N and you have

### 01:45:02 · Speaker 4

So, V I where V I is coming from P psi of V, right? This is again law of large numbers. We know how to estimate expectations, approximate expectations. But this

### 01:45:14 · Speaker 0

cannot

### 01:45:17 · Speaker 0

the return

### 01:45:23 · Speaker 0

as an expectation.

### 01:45:28 · Speaker 0

And therefore, therefore,

### 01:45:36 · Speaker 0

and be computed.

### 01:45:48 · Speaker 0

Do you see this? See,

### 01:45:50 · Speaker 4

the problem. See when I said that you cannot differentiate through sampling. So look at what is happening. See there is an expectation of a certain function and that function is parameterized by some set of parameters, right?

### 01:46:04 · Speaker 4

Now the expectation is with respect to a density, okay? And that density is also parameterized by same set of parameters.

### 01:46:13 · Speaker 4

So now if you want to do that, if you want to now take the gradient of such an expectation, okay, of a function that is, see typically what happens now in most of neural network training, you need to take the derivative of an expectation of a function with respect to set of parameters and these will be neural network parameters. But this expectation, right, will be typically over let's say P X, okay, where P X are simply uh the distribution of data which is not which is which has nothing to do

### 01:46:43 · Speaker 4

the model parameters and then we approximate this expectation with respect to I mean using the samples that we are given which are the true data. Now here is a case okay where you need to take the gradient of an expectation okay with respect to a density function and that density function

### 01:47:02 · Speaker 4

is also parameterized by the same set of parameters with respect to which we need the gradients.

### 01:47:08 · Speaker 4

you see that? And why is that happening if you look at it? That is happening because our encoder network is made probabilistic, no? When we make our encoder network probabilistic, okay? Then the the parameters that we are getting, no? of the expectation.

### 01:47:26 · Speaker 4

of of the distribution with respect to which we are taking the expectation. uh is that the distribution also is parameterized by same set of parameters with respect to which we need the uh the the derivatives.

### 01:47:43 · Speaker 4

Algebraically speaking what happens is that if you take the gradient you can you cannot express the second term that comes up in the gradient of the expectation in terms of sample averages. Okay? And therefore that cannot be computed. Is this point clear to all of you?

### 01:48:03 · Speaker 4

So this implies, so if you want to generalize this, this implies that the gradient of the first term in LBO which is the expectation of log of heat heat of X given Z with respect to

### 01:48:19 · Speaker 4

Q P of G given X, okay?

### 01:48:22 · Speaker 0

can't be

### 01:48:25 · Speaker 0

Computed

### 01:48:35 · Speaker 0

Yeah, can't be compared directly is what it means.

### 01:48:42 · Speaker 0

Can you all appreciate this fact?

### 01:48:51 · Speaker 4

Any questions on this? See this is the key part, okay? This is what this is where we need uh what is what what we call as the re-parameterization that we will see. But is this clear?

### 01:49:06 · Speaker 0

Any questions on this?

### 01:49:17 · Speaker 0

Hello, am I audible?

### 01:49:23 · Speaker 0

Yes sir

### 01:49:25 · Speaker 3

no questions. Great. Now what do we how do we solve this solution?

### 01:49:39 · Speaker 0

called as the reparameterization trick

### 01:49:51 · Speaker 0

Okay. Now what does this mean? Recall that we had

### 01:49:57 · Speaker 0

we wanted the gradient of

### 01:50:05 · Speaker 4

expectation of some function of some function that is parameterized by some parameters and the distribution was also parameterized by the same set of parameters right we wanted this. Now all we need to do is

### 01:50:22 · Speaker 0

couldn't be computed.

### 01:50:31 · Speaker 0

Correct? So what you do, what you do is

### 01:50:34 · Speaker 0

if

### 01:50:37 · Speaker 0

or express express.

### 01:50:47 · Speaker 0

in terms of

### 01:50:49 · Speaker 0

another distribution

### 01:50:57 · Speaker 0

distribution which is

### 01:51:02 · Speaker 0

Independent

### 01:51:07 · Speaker 0

Right

### 01:51:10 · Speaker 0

exactly what is called as the reparameterization, okay? I'll tell you. Reparameterize.

### 01:51:22 · Speaker 0

What does this mean? This means that let's say that

### 01:51:32 · Speaker 0

that suppose

### 01:51:37 · Speaker 0

there exists

### 01:51:40 · Speaker 0

a random variable

### 01:51:44 · Speaker 3

Epsilon

### 01:51:45 · Speaker 4

okay? It's some distribution P epsilon, okay? So note that this

### 01:51:50 · Speaker 4

is independent of

### 01:51:53 · Speaker 4

ID parameters. Okay. Such that, such that your V, which is the random variable of interest, is

### 01:52:03 · Speaker 4

some function of

### 01:52:06 · Speaker 4

receptor

### 01:52:06 · Speaker 0

Cholan

### 01:52:08 · Speaker 0

then, then

### 01:52:13 · Speaker 0

the expectation of

### 01:52:19 · Speaker 0

with respect to

### 01:52:23 · Speaker 0

P psi of V

### 01:52:25 · Speaker 4

can be shown to be equal to the expectation of

### 01:52:30 · Speaker 4

एफ साई ऑफ व्हाट इज वी नाउ? वी इज इक्वल टू जी टाइम्स एप्सिलॉन

### 01:52:38 · Speaker 4

Okay. And this expectation now will become the expectation with respect to P epsilon.

### 01:52:45 · Speaker 4

it is either you take it as a homework or can be taken in the D.A. session just to show that these two are equivalent, okay? This is also called the law of the unconscious statistician. Okay, abbreviated as the lotus. I mean this is a standard probability proof. You can just do it. Two steps you can show that.

### 01:53:06 · Speaker 2

So now what did we show?

### 01:53:07 · Speaker 4

that

### 01:53:09 · Speaker 4

there is this random variable uh V right with respect to which we are taking an expectation. Now we represented that random variable okay. In terms of another random variable epsilon okay. function of another random variable epsilon that is independent of these parameters uh psi.

### 01:53:31 · Speaker 4

And if you do that, then the expectation, okay, of uh the the function with respect to this random variable P psi, now will become an expectation with respect to another random variable P epsilon that is independent of uh the parameters psi.

### 01:53:52 · Speaker 4

So this is what is called as reparameterization, right? I mean just

### 01:53:55 · Speaker 0

function is called the reparameterization function.

### 01:54:07 · Speaker 3

How do you find this epsilon?

### 01:54:11 · Speaker 4

Yeah, good question. Now that depends upon like in the V A E paper, no, they give multiple ways to find this epsilon and the it's not enough if you only find epsilon, you need to find G also, no. You need to find an epsilon and a G such that this happens. I'll give you examples of how to do this, okay? At least in the in the case of like like the naive implementation of V A E, I'll tell you how this is done. Okay, so now this if you do this, now it's easy, right? So now

### 01:54:42 · Speaker 4

If we solve the problem, the problem was to find the gradient of uh this expectation.

### 01:54:52 · Speaker 4

with respect to P S I.

### 01:54:54 · Speaker 0

Now this is equal to the gradient of the expectation of

### 01:55:07 · Speaker 0

This can be done, no?

### 01:55:08 · Speaker 4

just now push the expectation inside the gradient inside the expectation and that can be computed using sample averages. So now this is approximately equal to take some m samples of epsilon and this equal to one to m and you have the gradient of

### 01:55:28 · Speaker 4

f psi of g of epsilon i

### 01:55:35 · Speaker 4

where your epsilon I now is sampled from P epsilon. So now you will not have that have this uh I mean uncomputable integral problem now because the dependency, the expectation is not now with respect to P psi but it is with respect to P epsilon.

### 01:55:56 · Speaker 4

Okay? Now let us look at the, let us look at an example of reparameterization.

### 01:56:01 · Speaker 0

somebody asked me how to do that. So example of

### 01:56:15 · Speaker 0

the

### 01:56:23 · Speaker 0

spelling correct. T para means reservation right here.

### 01:56:31 · Speaker 4

you know,

### 01:56:35 · Speaker 4

Right

### 01:56:37 · Speaker 4

position, okay? In V A E, in particularly in V A E, okay? I mean, this reparameterization is independent of V A E or nothing. It's a general probability, uh, probabilistic technique, okay? But yeah, I'll show you an example of V A E, right? So let us take the same example where my Q V

### 01:56:58 · Speaker 4

of

### 01:56:59 · Speaker 3

P1X

### 01:57:03 · Speaker 3

Q P of G given X, okay, is a Gaussian distribution.

### 01:57:09 · Speaker 3

and it has parameters let's say mu of x and sigma of x

### 01:57:15 · Speaker 4

Okay

### 01:57:18 · Speaker 4

Right?

### 01:57:19 · Speaker 4

This is what it is. Now let us now reparameterization. Okay, so now what is fee by the way? I'll tell you.

### 01:57:28 · Speaker 4

next way to write it is

### 01:57:31 · Speaker 4

say that this mu is a function of phi because this is the output of the neural network. sigma is also a function of parameterized by phi a function of x. okay? now that is why this becomes a function of p now. let us re-parameterize. now let

### 01:57:47 · Speaker 4

that epsilon be a Gaussian distribution with zero mean and unit variance.

### 01:57:54 · Speaker 0

okay? If you do that, then, then

### 01:58:03 · Speaker 0

Z is equal to

### 01:58:07 · Speaker 0

μ v of x plus

### 01:58:17 · Speaker 0

sigma of u of x times epsilon if I do this

### 01:58:21 · Speaker 0

I do this

### 01:58:22 · Speaker 4

then Z will now have

### 01:58:27 · Speaker 4

distribution equal to z given x. Do you agree? Now this function right is the g function that I'm talking about. This is g of epsilon.

### 01:58:38 · Speaker 4

if you take a normally distributed random variable with zero mean and unit variance

### 01:58:46 · Speaker 4

excuse me. So you add it with a constant and scale it with a constant. If you do that, then the the the output random variable will again be Gaussian, okay? with the mean and variance given by the scale and the shift.

### 01:59:03 · Speaker 0

This is reparameterization

### 01:59:07 · Speaker 0

Do you see that?

### 01:59:17 · Speaker 0

This is all right

### 01:59:19 · Speaker 0

this G function

### 01:59:24 · Speaker 0

simply mu

### 01:59:27 · Speaker 0

Bus

### 01:59:35 · Speaker 4

Okay

### 01:59:38 · Speaker 4

So this is one way, okay? uh There is another way to reparameterize which is not often used in in VA literature but yeah there is one other way to reparameterize uh which is called as this is one example.

### 01:59:54 · Speaker 4

The other example that is given in that paper is what is called as the inverse CDF method.

### 02:00:00 · Speaker 0

will not use inverse cdf method but I'm simply

### 02:00:08 · Speaker 0

mentioning it for the sake of completeness. See suppose

### 02:00:16 · Speaker 0

x is a random variable. Okay. And f x of x

### 02:00:26 · Speaker 0

denotes its CDF

### 02:00:32 · Speaker 0

Okay, so we know that

### 02:00:36 · Speaker 0

effects of

### 02:00:36 · Speaker 4

so simply

### 02:00:40 · Speaker 4

the integral of the

### 02:00:43 · Speaker 4

PDF function, right, over this. Now let us call that, represent that by some random variable Z. Okay? Now this is a function of, now the question is, question is...

### 02:00:59 · Speaker 0

What is the

### 02:01:04 · Speaker 0

the distribution

### 02:01:09 · Speaker 0

Four G

### 02:01:11 · Speaker 0

Do you understand?

### 02:01:12 · Speaker 4

understand the question. Now given a random variable you compute its cdf, okay? Now cdf itself becomes another random variable.

### 02:01:22 · Speaker 4

Okay, question that we are asking is what will be the distribution of C D F I?

### 02:01:26 · Speaker 0

of a random variable. Do you know that?

### 02:01:30 · Speaker 0

doesn't even know that

### 02:01:38 · Speaker 0

it would be a uniform distribution.

### 02:01:44 · Speaker 0

between zero and one

### 02:01:53 · Speaker 0

you so please take this as

### 02:01:55 · Speaker 4

small homework and show this. That you take any random variable, okay? And show that the distribution of its CDF of any random variable is uniform between zero and one. Can you already intuitively see why that should be the case?

### 02:02:13 · Speaker 4

if you take the C D F, C D F is a non-decreasing function, right? And it is upper bounded by one. So which mean upper it is bounded between zero and one, right? Always the C D F. So that should be a uniform distribution between zero and one. Just I mean this is a standard proof, okay? So so please find it out in the internet or just do it as a homework, okay? Now the thing is this implies, this implies that if I take a U that is uniform between zero and one, okay? And compute to be equal to the inverse, okay, of the C D F that is evaluated at U.

### 02:02:51 · Speaker 0

then then

### 02:02:55 · Speaker 3

the the

### 02:02:58 · Speaker 0

distillation of x

### 02:03:01 · Speaker 0

Okay, let us call this as x cap. x cap is inverse c d f of a random variable x, then the distribution of x cap

### 02:03:19 · Speaker 0

is same

### 02:03:27 · Speaker 0

and that of

### 02:03:30 · Speaker 0

x

### 02:03:32 · Speaker 4

That is the idea. Makes sense, right? See now we know that the distribution of the C D F of any random variable is uniform.

### 02:03:42 · Speaker 4

Okay. Now that means that if you take a uniform random variable between zero and one, okay? And make a transformation, okay, using the inverse of the C D F of any random variable, then the then the the uh the outcome will be another random variable which would have the distribution that is same as that random variable whose C D F you have inverted.

### 02:04:08 · Speaker 4

You see that?

### 02:04:08 · Speaker 0

So in this case, in this case,

### 02:04:17 · Speaker 0

the G functions from epsilon

### 02:04:20 · Speaker 0

epsilon is uniform zero one

### 02:04:28 · Speaker 3

and the G function, okay? is the inverse

### 02:04:34 · Speaker 4

of the CDF. So this is another reparameterization technique which is called the inverse CDF method.

### 02:04:41 · Speaker 4

Is this all right? See, but the thing is in this case, no, the only requirement is that the CDF of the of the distribution that you are modeling using your encoder has to be invertible.

### 02:04:53 · Speaker 4

right? Which is not always the case and that's why you know in most of the cases uh in VAEs the distribution of Q is taken to be Gaussian and this sort of reparameterization is used you know which is the affine reparameterization is used not the inverse ADF method. But I hope that you got the idea behind reparameterization right? Let me repeat what is happening here. So we wanted to find the gradient of the encoder parameter uh which

### 02:05:23 · Speaker 4

with respect to elbow. Right? Sorry, we wanted to find the gradient of the elbow with respect to the encoder parameters. That cannot be found out because the the elbow has an expectation of some function with respect to a distribution and that distribution itself happens to be a function of these parameters. Okay? So we cannot compute the gradients. uh So what do we do about it? The way to do it is represent that distribution uh with respect to which you

### 02:05:53 · Speaker 4

taking the expectation in terms of another arbitrary random variable which is independent of the parameters. Okay so that representation through a function is what is called as reparameterization. So if you do that then this expectation can be written in terms of an expectation over that arbitrary random variable and therefore the gradients of this function with respect to the encoder parameters can be found out. So that is the idea and we saw two ways to do reparameterization which is that if you

### 02:06:23 · Speaker 4

assume your Q P to be normally distributed with a certain mean and variance. The way to reparameterize that is start with a Gaussian random variable which has zero mean and unit variance and scale it with the sigma and shift it with the mu, you will get another random variable whose mean and variance is what the mean and variance of Q P Q pi is.

### 02:06:49 · Speaker 4

Any questions so far?

### 02:06:52 · Speaker 4

Now we will use this to compute the gradient and then back propagate. But yeah, if you have any questions here, please ask me. This is, this is actually one of the

### 02:07:01 · Speaker 4

trucks idea of V A E is because otherwise it's simple right you are like maximizing the likelihood representing the distribution using neural network and back propagating but what's important is once you represent a distribution using a neural network in a probabilistic sense you have to get to reparameterization otherwise you cannot compute the gradients that is the idea.

### 02:07:27 · Speaker 4

Right. Haan, go on rather than

### 02:07:31 · Speaker 6

Uh so are we saying that we are transforming uh the distribution that we get to either a standard normal or a uniform in this case? Is is that the way to see it or?

### 02:07:42 · Speaker 4

the other way around, no? See, we are representing the output, the distribution of the encoder, okay, or distribution that is being modeled by the encoder in terms of standard normal zero.

### 02:07:56 · Speaker 6

Okay, and and the transformation, I mean, is the G function basically, right?

### 02:08:01 · Speaker 4

transformation is a G function and that's a that's that that is a user defined function it is nothing to do with you are not learning it or anything it is just a user defined thing

### 02:08:06 · Speaker 6

Nothing

### 02:08:10 · Speaker 6

And is that also the way we say that okay, that random sampling process we eliminate and then we introduce some kind of a determinism here?

### 02:08:18 · Speaker 4

No, no, there is three sampling is happening in epsilon. We are just re-representing that in terms of some other random variable which is which is which is not a function of the see it is only to do a simple thing. All we need to do is express this expectation that is there in elbow with respect to a distribution of a random variable which is independent of the parameters, that's all.

### 02:08:18 · Speaker 6

No, there is

### 02:08:24 · Speaker 6

Okay

### 02:08:43 · Speaker 4

That's all we want to do.

### 02:08:45 · Speaker 6

Okay, so so sampling this way still allows us the to flow the gradients backwards.

### 02:08:51 · Speaker 4

Yeah yeah I will show you how to do that. Okay. See now I mean algebraically you are convinced no that now we can express this expectation right?

### 02:08:53 · Speaker 6

Okay

### 02:08:57 · Speaker 6

Yes

### 02:09:01 · Speaker 6

Yes

### 02:09:01 · Speaker 4

Basically the the the distribution which is I mean which which you are sampling from is not now dependent on fee. It is you you got

### 02:09:12 · Speaker 3

I don't know

### 02:09:12 · Speaker 0

Yep

### 02:09:13 · Speaker 3

Yeah, that is the basic idea. Any other questions?

### 02:09:22 · Speaker 0

So now let us write what is happening. So now what happens is that you have the encoder network.

### 02:09:35 · Speaker 0

the encoder network. Okay, this is not

### 02:09:42 · Speaker 3

the two red dots.

### 02:09:44 · Speaker 3

Yeah Karthik go on you had a question.

### 02:09:47 · Speaker 0

No sir sorry

### 02:09:54 · Speaker 3

goes as an input and this is modeling Q by of Z given X, okay?

### 02:10:00 · Speaker 4

What happens here is this neural network gives you uh mu and sigma. So what you do is sample epsilon from normal zero one.

### 02:10:12 · Speaker 4

let's call this as a psi. So given a particular sample, you take an epsilon from normal zero one and then do

### 02:10:22 · Speaker 0

Z get your Z by

### 02:10:33 · Speaker 0

depending on the spectral

### 02:10:36 · Speaker 0

sigma phi sigma phi of x

### 02:10:41 · Speaker 0

we got this Z I correct? Now take that Z I

### 02:10:45 · Speaker 0

and pass it through the decoder.

### 02:10:53 · Speaker 0

and get an X Y cap

### 02:10:57 · Speaker 0

This is what is happening.

### 02:10:59 · Speaker 4

you understood, no? So, do you do you see the difference between these two here?

### 02:11:04 · Speaker 4

Yeah, just zoom it here. Here what we are doing is that we started from X I, got a muon sigma, sampled from sampled G I using that muon sigma directly from Q P and then gave that G I. Here when we reparameterize, what did we do? We got muon sigma, okay? Sampled an epsilon from an arbitrary from standard normal zero one and then got G I by reparameterizing.

### 02:11:33 · Speaker 4

Is it all right?

### 02:11:37 · Speaker 4

You note the difference now after before and after re-parameterizing

### 02:11:40 · Speaker 3

regulation

### 02:11:43 · Speaker 3

Yeah, I hope that you got it. So now what do we have to do is we need to compute the gradient of

### 02:11:52 · Speaker 3

the expectation of

### 02:11:54 · Speaker 3

log of

### 02:11:56 · Speaker 3

P theta

### 02:11:59 · Speaker 3

g one g with respect to q v of g given x correct? Right? Now this is equal to the gradient of

### 02:12:11 · Speaker 3

expectation of log of

### 02:12:13 · Speaker 3

We hit off

### 02:12:16 · Speaker 3

X okay given what is Z now?

### 02:12:24 · Speaker 3

Z is given by this particular form.

### 02:12:26 · Speaker 0

Geo

### 02:12:27 · Speaker 3

Yeah, this particular formula, we call this as

### 02:12:33 · Speaker 0

g of epsilon, okay?

### 02:12:38 · Speaker 0

This is with respect to P itself.

### 02:12:43 · Speaker 0

Is it all right?

### 02:12:49 · Speaker 0

strictly speaking, you know, this G function is a function of P now.

### 02:12:52 · Speaker 4

because look at this right I mean it has mu phi and sigma phi its its parameter is by phi

### 02:12:58 · Speaker 4

Okay

### 02:13:01 · Speaker 4

So the question is

### 02:13:03 · Speaker 4

we got rid of the dependency on V, right? This expectation now can be is equal to

### 02:13:09 · Speaker 4

one

### 02:13:10 · Speaker 3

over

### 02:13:13 · Speaker 3

If we sample M samples of epsilon, right, then it is equal to J through M and we have

### 02:13:22 · Speaker 3

log of

### 02:13:23 · Speaker 0

theta of x given

### 02:13:29 · Speaker 0

Israel

### 02:13:32 · Speaker 0

Epsilon G

### 02:13:36 · Speaker 0

Please note

### 02:13:37 · Speaker 4

that for a particular

### 02:13:39 · Speaker 3

particular X I, okay, for a given X I, we can get M number of Z I's. See that?

### 02:13:47 · Speaker 3

or

### 02:13:50 · Speaker 0

one x, sorry, okay.

### 02:13:54 · Speaker 0

M

### 02:13:57 · Speaker 0

C I's can be obtained.

### 02:14:08 · Speaker 0

You understand that?

### 02:14:12 · Speaker 0

because we are doing

### 02:14:12 · Speaker 4

doing sampling right? uh like outside of the encoder. Since we are doing sampling, we can sample for one XI, we can sample multiple GIs, but typically, I mean what is done in implementing VAE is that they keep capital M to be one. That means that they only do one sampling and send it across, okay? Which means that the sum will only be on one particular sample.

### 02:14:35 · Speaker 4

hope that it is okay. Now the next question is that how to

### 02:14:38 · Speaker 0

to compute

### 02:14:46 · Speaker 0

how to compute log of

### 02:14:54 · Speaker 3

सर, हियर वी

### 02:14:56 · Speaker 5

we are doing it in a probabilistic approach right for the encoder

### 02:15:02 · Speaker 4

encoder is always probabilistic

### 02:15:06 · Speaker 4

X I will give you mu and sigma. Once you get your mu and sigma, you sample epsilon from, yeah, epsilon from epsilon j, let's call it. You sample epsilon from normal zero one and then you reparametersize and get M uh Z j's.

### 02:15:06 · Speaker 5

sir

### 02:15:22 · Speaker 5

Okay

### 02:15:23 · Speaker 3

she

### 02:15:24 · Speaker 4

So there is

### 02:15:24 · Speaker 5

So there is some like so if we write it like this, so there is some linear translation happening between the output of encoder and the input of decoder.

### 02:15:37 · Speaker 4

Yeah, input of the, yeah, that is reparameterization, no? In this particular case, that is what I'm saying. If you assume your Q to be normal, mu sigma, then this reparameterization is adaptable.

### 02:15:50 · Speaker 4

There's no rule why this is the only way to reparameterize, no? That's what I'm saying. Suppose you assume your QP to be some other distribution, you just have to find an epsilon and G such that it transforms.

### 02:16:01 · Speaker 4

See, what is important is that now this gradient, right? The gradient that we are computing here, this will become, this expectation will become independent of phi, that's all we need.

### 02:16:13 · Speaker 5

Correct

### 02:16:14 · Speaker 4

And for that we do reparameterization. Now what sort of reparameterization you do is a design choice. That depends upon what form do you assume on Q P and what what epsilon will just transform what epsilon and G combination will transform that into this is the question that's all. That depends upon whatever you use.

### 02:16:35 · Speaker 3

ओके सर

### 02:16:37 · Speaker 4

Is that all right?

### 02:16:38 · Speaker 3

Yes

### 02:16:40 · Speaker 4

Okay. Uh, yeah, Sarvesh, you have a question.

### 02:16:45 · Speaker 6

So in the last step one by M so there should be a gradient inside right?

### 02:16:50 · Speaker 4

Yeah yeah

### 02:16:50 · Speaker 3

Okay

### 02:16:51 · Speaker 0

there's a gradient here. So this will be X.

### 02:17:03 · Speaker 0

Go on Raghavendra

### 02:17:04 · Speaker 3

So, can you just

### 02:17:05 · Speaker 6

repeat why that m can be taken as just one here

### 02:17:08 · Speaker 4

See, it's that it's that you are approximating this expectation by a single sample estimate, that's all. It can be anything, people take it as one and also experiment. I mean, in your assignment, I'll ask you to experiment with different values of M, okay? But yeah, so generally, I mean, like in the naive, most naive implementation, you just take one sample of Z or one sample of X, but it is not, I mean, it's not hard and fast, right? I mean, you can make your M to be hybridized. parameter and play with it.

### 02:17:41 · Speaker 6

Yeah, because I think in this equation we say that it is an expectation. So we we are free to choose the value of M here, right? And and because And also

### 02:17:47 · Speaker 4

And and because And also single sample estimate is not a good way to do it. Yeah. Always.

### 02:17:55 · Speaker 6

Okay

### 02:17:57 · Speaker 6

Thank you

### 02:17:57 · Speaker 4

Okay, great. Yeah. So, okay, so next

### 02:17:59 · Speaker 5

Sir, I didn't follow on this part, Sir. Can you please explain once again?

### 02:18:04 · Speaker 4

part. See, you sample for one X I goes as an input to the encoder, right? You get a mu and sigma. Now with that mu and sigma, you can sample any number of Z I's, no, for a particular X I.

### 02:18:05 · Speaker 5

Sir

### 02:18:10 · Speaker 5

you

### 02:18:12 · Speaker 5

Hello

### 02:18:19 · Speaker 5

Yes sir

### 02:18:21 · Speaker 4

हां सो दैट इज वॉट द चॉइस ऑफ

### 02:18:21 · Speaker 5

depending on the choice of him

### 02:18:24 · Speaker 4

That is what I have represented as capital M. So you sample like multiple samples from so it's like for let's say that X I is an image, no? For a given image, for one particular image, you will have M different embeddings.

### 02:18:39 · Speaker 3

Correct

### 02:18:40 · Speaker 4

Right? So that is the that is the sort of advantage with a probabilistic encoder, right? That unlike in a BERT etcetera where for a given text sequence of tokens you only have exactly one embedding. Here you can have a plethora of embeddings for a given particular input because you are modeling it probabilistically, correct?

### 02:19:03 · Speaker 4

Once you do that, if you have M of them to compute the first term, right? You need to take an average, I mean meaning you take a sample average of all those M, uh, M M M C I's basically, right? C J's.

### 02:19:18 · Speaker 4

But what I said is that some people when they implement VA, you know, they make this capital M to be one. You can do it one also because it's a hyperparameter but you know, M being equal to one is not a great choice because you are approximating an expectation using one sample.

### 02:19:34 · Speaker 3

which is not a good thing to do, no?

### 02:19:40 · Speaker 0

Okay

### 02:19:43 · Speaker 3

Yeah, yeah, Sarvesh.

### 02:19:45 · Speaker 6

Sir, this x, p theta of x given z, so this x is all all x's, right? x one, x two, x n because of we have to maximize the likelihood of all x one to x n.

### 02:19:55 · Speaker 4

but yeah but we are doing the entire treatment for one particular data point now. See whatever we are doing now there is an outer sum on all data points. You take a batch size and do it over batches.

### 02:20:09 · Speaker 3

Yes, yes.

### 02:20:10 · Speaker 4

But I'm doing it for only one X I know. For now, I'm only doing it for one X. So this is actually X I.

### 02:20:18 · Speaker 4

I should not be writing it as X I because it's a distribution over a random variable, right? But what I mean to say is that only one sample is what we are doing it for, which should be extended to the entire data set on a batch level.

### 02:20:31 · Speaker 5

which is so like it's

### 02:20:32 · Speaker 4

stochastic. Yeah, yeah, yeah, yeah, stochastic when you do it at the batch level because usual training, no? I'm I'm telling you how to train for one sample. You can train it sample by sample or take a batch and do it, doesn't matter, but we'll see that. I I was going to say that at the end of the end of the lecture, but this is only I mean all that we are doing it is for only one data point, okay?

### 02:20:34 · Speaker 5

Yeah

### 02:20:56 · Speaker 0

ओके, थैंक यू।

### 02:20:57 · Speaker 4

Now the next question is, any other questions on this? If not, we'll move on. Now we have to compute this log of P theta of X given Z, no? How do we compute log of P theta of X given Z is the question. So again, there are multiple ways to do it, okay? So now one way to do it

### 02:21:13 · Speaker 0

is that express

### 02:21:23 · Speaker 0

using some parametric distribution.

### 02:21:36 · Speaker 0

Okay. Now for example, this is not the only way to do it again. For example,

### 02:21:42 · Speaker 4

like assume

### 02:21:45 · Speaker 4

assume P theta of X given Z to be coming from a Gaussian distribution, okay? What is the distribution on X of course?

### 02:21:55 · Speaker 4

and you assume the mean, okay, to be

### 02:21:58 · Speaker 0

Equal to

### 02:21:59 · Speaker 0

the

### 02:22:06 · Speaker 0

output of the decoder

### 02:22:09 · Speaker 0

Okay

### 02:22:10 · Speaker 0

Event

### 02:22:11 · Speaker 4

variants to be equal to identity

### 02:22:13 · Speaker 4

note that in this case I am uh representing the neural network right the decoder network probabilistically. Okay. Now where T theta

### 02:22:27 · Speaker 4

T T of G

### 02:22:30 · Speaker 3

is the

### 02:22:31 · Speaker 3

let us call that as x cap we have been calling it as x cap no? x cap which is

### 02:22:41 · Speaker 3

d theta of z is the output of the neural network.

### 02:22:47 · Speaker 3

decoded. You know, in this case, what happens is that this X I cap that we get, no, which is

### 02:22:57 · Speaker 4

p theta of z, right? Okay. Now now this we we are interpreting this as the mean of a Gaussian distribution, right? of p theta of x given z. So in this case, in this case, let's see what happens to log of

### 02:23:14 · Speaker 4

P theta which given you what is this equal to? is equal to

### 02:23:20 · Speaker 3

that propose that term one by two pi

### 02:23:26 · Speaker 3

T by 2

### 02:23:27 · Speaker 0

sigma inverse it is identity it will go away it will be e power

### 02:23:55 · Speaker 0

is for the point x i no x okay let's call it as x x minus

### 02:24:00 · Speaker 4

minus what is the mean the mean is given by the t theta of g

### 02:24:07 · Speaker 4

the identity matters is the identity is the the variance this is equal to this

### 02:24:13 · Speaker 4

Okay now, uh, ignoring the constant, let us just say some

### 02:24:20 · Speaker 4

one by

### 02:24:23 · Speaker 4

2i.

### 02:24:25 · Speaker 3

because the other terms are independent

### 02:24:29 · Speaker 0

proportional to log and e power will go away this will be

### 02:24:33 · Speaker 0

x minus

### 02:24:43 · Speaker 0

Now you see where the auto encoding thing is coming from.

### 02:24:46 · Speaker 4

it will become a

### 02:24:49 · Speaker 4

query error loss, okay, between the input data point X I and the output of the decoder. If you assume your P theta of X given Z to be Gaussian, so which implies

### 02:25:00 · Speaker 4

Now the expectation of what do we have? Expectation of log of

### 02:25:07 · Speaker 4

theta of x given z this with respect to q p of z given x this is what we wanted right? this we sought to be equal to c x

### 02:25:18 · Speaker 3

expectation of

### 02:25:22 · Speaker 3

to take an intercept at P epsilon, you have log of

### 02:25:27 · Speaker 3

p theta x given

### 02:25:29 · Speaker 3

Geoculture

### 02:25:31 · Speaker 4

Okay. Now sample in terms of sample averages, how do we approximate this is approximately equal to one by M. So if you sample

### 02:25:44 · Speaker 3

this is this under the assumption of Gaussian anti. there's a minus here.

### 02:25:51 · Speaker 3

is equal to

### 02:25:53 · Speaker 3

F I

### 02:25:55 · Speaker 0

Minus

### 02:25:58 · Speaker 0

p theta of

### 02:26:04 · Speaker 0

Yes

### 02:26:09 · Speaker 0

P one four C K

### 02:26:13 · Speaker 0

or equal to

### 02:26:18 · Speaker 0

just said.

### 02:26:20 · Speaker 3

is equal to

### 02:26:25 · Speaker 3

म्यू फी ऑफ एक्स आई प्लस एप्सिनान जे टाइम्स

### 02:26:34 · Speaker 3

Sigma E of

### 02:26:36 · Speaker 3

sorry. For j equal to one three m.

### 02:26:44 · Speaker 4

See now you don't see the dependence on phi here so maybe I should write it directly hold on yeah. Can you see that there is a dependence on Z here? It is entire thing this thing is a function of phi. Do you see the dependence on phi? It depends on phi through Z correct? Because you know Z is dependent on phi correct?

### 02:27:06 · Speaker 4

this is what it is. So now what we should do is that now how do we do like one uh training of encoder.

### 02:27:17 · Speaker 4

one iteration of encoder is as follows

### 02:27:20 · Speaker 3

I'll write that now

### 02:27:23 · Speaker 3

you have X I as an input. the Q V network.

### 02:27:29 · Speaker 3

This will give you mu

### 02:27:34 · Speaker 3

new fee of

### 02:27:36 · Speaker 3

X I and sigma phi of X I, okay? So take these two, sample epsilon J.

### 02:27:48 · Speaker 3

from normal zero one, okay? And find out

### 02:27:54 · Speaker 3

ZJ as

### 02:27:57 · Speaker 3

Mu

### 02:27:58 · Speaker 4

p of x i plus epsilon j times sigma p of x k

### 02:28:07 · Speaker 3

Okay

### 02:28:08 · Speaker 3

and then take this ZJ and pass it through the decoder

### 02:28:19 · Speaker 0

holding P theta of X given Z

### 02:28:21 · Speaker 3

Hello

### 02:28:22 · Speaker 0

this will give you

### 02:28:25 · Speaker 0

v theta

### 02:28:30 · Speaker 3

x cap i or rather x cap j which is d theta

### 02:28:36 · Speaker 4

of ZJ

### 02:28:40 · Speaker 4

Okay. Now what do you do? Like there is a forward pass. This is the forward pass, right? Take this, get this done and take the

### 02:28:50 · Speaker 4

Okay, so

### 02:28:54 · Speaker 4

get your Z, okay? From your Z, get it through this. This is one forward pass, okay? Now how do we do reverse pass? Reverse pass is compute.

### 02:29:06 · Speaker 4

Copied

### 02:29:08 · Speaker 4

So one for one particular exercise, you need to compute one by M

### 02:29:16 · Speaker 4

note that for a particular input X I, you have multiple possible outputs. because you have multiple embeddings, right, with different temps. You compute this, okay? And then take the

### 02:29:31 · Speaker 3

Pressure

### 02:29:33 · Speaker 3

complete the gradient of this with respect to

### 02:29:39 · Speaker 3

Okay? And then simply propagate this.

### 02:29:46 · Speaker 3

I'll revert to the input of this.

### 02:29:48 · Speaker 4

What happens here by the way?

### 02:29:50 · Speaker 3

once it comes to the input of the decoder

### 02:29:56 · Speaker 3

What will happen? So you have to back properly take this gradients.

### 02:30:03 · Speaker 3

and propagate through this operation now, ZJ operation.

### 02:30:09 · Speaker 3

Right?

### 02:30:12 · Speaker 3

this operation

### 02:30:13 · Speaker 6

will also have to remember this E J E that was used here, right?

### 02:30:18 · Speaker 3

Of course, of course, of course, of course, you have to save that.

### 02:30:22 · Speaker 3

for all Ms, no, you have to remember that ZJ. So, okay.

### 02:30:25 · Speaker 0

maybe I will write it this way to make it easier

### 02:30:32 · Speaker 0

from here

### 02:30:38 · Speaker 0

It goes like this

### 02:30:42 · Speaker 0

Okay, first it will come like this.

### 02:30:45 · Speaker 0

from here you travel like this.

### 02:30:52 · Speaker 0

this for the reverse pause. So now forward pause also it comes like this and

### 02:31:03 · Speaker 0

through this, okay? And then from here you would go like this.

### 02:31:09 · Speaker 3

and

### 02:31:11 · Speaker 3

Oh, sorry, I think I changed the color. Hold on.

### 02:31:15 · Speaker 3

this is the color I'll give. It'll come like this. Okay? And from here,

### 02:31:22 · Speaker 3

like this

### 02:31:25 · Speaker 3

Yeah. So once you get that,

### 02:31:28 · Speaker 0

in your class like this.

### 02:31:29 · Speaker 3

Hello

### 02:31:30 · Speaker 0

forward power and the reverse power

### 02:31:44 · Speaker 0

power propagation and surgery.

### 02:31:53 · Speaker 6

all this while we don't change theta right? we keep the theta fixed.

### 02:31:56 · Speaker 3

I mean

### 02:31:56 · Speaker 4

Yeah, we keep we keep the theta theta constant to hold on, I think. Okay, so I'll have to do it this way. To ensure that what I'm writing is more legible, hold on. This is only

### 02:32:12 · Speaker 3

for training the encoder and not decoder. This thing, there is this epsilon.

### 02:32:23 · Speaker 0

Okay. The note that, I'll write it. Note.

### 02:32:31 · Speaker 0

that

### 02:32:38 · Speaker 0

Radiants

### 02:32:43 · Speaker 0

Do not grow

### 02:32:46 · Speaker 0

थ्रू सांपे

### 02:32:52 · Speaker 0

Do you see that? So maybe I'll write it in a different color easier that way.

### 02:33:16 · Speaker 0

disassembling.

### 02:33:22 · Speaker 0

That's it. So this is like

### 02:33:24 · Speaker 4

one iteration of training the encoder with the first term. We have not looked at the second term yet. This is only for the first term. The first term for the encoder by keeping the theta.

### 02:33:35 · Speaker 3

constant

### 02:33:39 · Speaker 3

Any questions on this?

### 02:33:45 · Speaker 3

Is it hand raised Harish?

### 02:33:48 · Speaker 3

सर, वी गेट एम ग्रेडिएंट्स व्हाई बैक प्रोपोगेटिंग राइट फॉर फॉर ईच्.

### 02:33:53 · Speaker 0

pitch

### 02:33:54 · Speaker 0

What

### 02:33:57 · Speaker 4

Sorry, I didn't follow. Can you repeat? It was obscure.

### 02:33:59 · Speaker 3

Yeah, sorry. So we get

### 02:34:03 · Speaker 7

M gradients, right? While since we have

### 02:34:07 · Speaker 4

No no one one one gradient. No no one gradient. See what happens is you take M of Z right? You pass all those through the decoder and you get M X J caps correct?

### 02:34:20 · Speaker 2

Yes

### 02:34:21 · Speaker 4

So you compute this this entire thing, you know, this thing, right? You take the difference with all each of them individually and sum them off. So that will be one scalar. That will be one scalar.

### 02:34:31 · Speaker 6

one

### 02:34:33 · Speaker 6

Got it, got it. Okay. So we are summing up it at the end.

### 02:34:38 · Speaker 4

not one M. So it is like M different outputs. You take the difference between them and you sum and then it will be one scalar that you back propagate.

### 02:34:47 · Speaker 0

Got it. Okay. Thank you, sir.

### 02:34:52 · Speaker 4

Any other question? See your second assignment will have this to be implemented. So, Yeah I think I think this this should be clear. So let me know if you have any other questions on this.

### 02:35:05 · Speaker 5

Sir, why do we need to get a scalar sum at the decoder output like we we have M different X Js and we can, you know, like compute the log.

### 02:35:17 · Speaker 4

the law. See, look at what is doing. See, we should not deviate from math. So what is happening is we need to compute the expectation of Q P of Z given X for a particular X, for one X.

### 02:35:29 · Speaker 4

okay? We represented that in terms of an expectation over another random variable. So expectation has to be computed and back propagated. You are you understand? So you have to compute the expectation of sample averages at the output of the decoder and you get a one you get one scalar that would be back propagated.

### 02:35:39 · Speaker 5

Okay

### 02:35:48 · Speaker 5

expectation of the sample averages and okay.

### 02:35:52 · Speaker 4

Isn't it? So this is look at this equation, this equation is what we are trying to back propagate, isn't it? That's the first term in elbow.

### 02:36:02 · Speaker 4

So this is for a given x. So for a given x you need to compute the expectation of that log likelihood with respect to Q phi of Z given x. For a particular x. And that will represented as an expectation over epsilon. Okay, which is a sum over all M samples. So we have to pass all those to the decoder, compute this and then take a scalar and then back propagate.

### 02:36:23 · Speaker 4

Okay

### 02:36:24 · Speaker 7

Okay

### 02:36:25 · Speaker 4

You can actually make M2

### 02:36:26 · Speaker 6

actually may have to

### 02:36:28 · Speaker 6

So there was a second term for elbow, right? I mean that does not contribute.

### 02:36:32 · Speaker 4

see this one thing at a time. only doing it see look at what we are doing. forget what we are doing.

### 02:36:41 · Speaker 4

look at this

### 02:36:45 · Speaker 4

All this is for the first term, the gradient of the encoder parameters with respect to the first term. There's a story for the second term and both of the terms for the decoder. We have to still come one thing at a time.

### 02:36:59 · Speaker 6

this is not the complete gradient that we flow back

### 02:37:02 · Speaker 4

No, we have not completed the training.

### 02:37:04 · Speaker 6

Sorry Sir

### 02:37:06 · Speaker 4

It's only the first term that to the encoder parameters, right?

### 02:37:10 · Speaker 4

So if you have questions, see this is the most complicated thing, the rest are actually easy. It's just simply training a neural network. This is the most, that's why I took the most complicated thing the first and then we will go one thing at a time. Okay.

### 02:37:24 · Speaker 3

any any any other questions on this? If not let's move on.

### 02:37:27 · Speaker 4

So now this

### 02:37:29 · Speaker 0

second now we have to compute the compute the gradients

### 02:37:44 · Speaker 0

of encoder

### 02:37:50 · Speaker 0

for the second term

### 02:37:59 · Speaker 0

What is the second term? Second term is the KL divergence between

### 02:38:08 · Speaker 3

q p of g d one x and p theta of g okay

### 02:38:13 · Speaker 3

what is done is

### 02:38:16 · Speaker 3

P theta of G

### 02:38:19 · Speaker 3

is assumed to be

### 02:38:25 · Speaker 3

normal zero one. Okay. See, look, note that this is assumed to be independent of theta.

### 02:38:32 · Speaker 4

This is a model assumption that is made and there are other lots of other improvisations over V A E that would question this and make it dependent on theta also, okay? So for the the naive implementation, this is made independent assumed to be Gaussian zero one and it is made assumed to be independent of theta. So in that case what happened?

### 02:38:51 · Speaker 3

happens is we have

### 02:38:56 · Speaker 0

you have

### 02:38:59 · Speaker 0

Q phi of Z given X, okay? To be a Gaussian,

### 02:39:05 · Speaker 0

of

### 02:39:08 · Speaker 0

μ and σ, right?

### 02:39:12 · Speaker 0

Right? Now this implies that the second term which is K between

### 02:39:26 · Speaker 0

will be equal to KL between

### 02:39:29 · Speaker 0

two Gaussians, okay? One is a Gaussian.

### 02:39:42 · Speaker 0

another is a Gaussian zero one

### 02:39:49 · Speaker 0

So this is

### 02:39:53 · Speaker 0

what is this? The deterministic form for this, okay?

### 02:40:08 · Speaker 0

even by let me just tell you what it is.

### 02:40:32 · Speaker 0

equal to

### 02:40:35 · Speaker 0

Half

### 02:40:38 · Speaker 0

log

### 02:40:40 · Speaker 0

plus

### 02:40:42 · Speaker 0

determinant of this minus d plus

### 02:40:47 · Speaker 0

the trace of

### 02:40:56 · Speaker 0

inverse of x

### 02:41:02 · Speaker 0

or I can write it as minus half log of this and

### 02:41:06 · Speaker 0

So this

### 02:41:08 · Speaker 0

plus plus

### 02:41:11 · Speaker 0

meow

### 02:41:16 · Speaker 0

mu phi

### 02:41:19 · Speaker 4

mu phi of x square. This is this is what it is. You know you can show this. Gaussian between two sorry KL between two Gaussian distributions can be deterministically found out. Simply take it as a small homework and do this. Okay.

### 02:41:33 · Speaker 4

Yeah, this is what it is, okay? So K L now is a simply a function of sigma V X and mu X. So this means that it is

### 02:41:43 · Speaker 3

S

### 02:41:44 · Speaker 4

Hello

### 02:41:44 · Speaker 4

decoder

### 02:41:45 · Speaker 3

thing write it again.

### 02:41:49 · Speaker 3

X I Q P of

### 02:41:52 · Speaker 5

सर, इज इट स्क्वेयर ऑफ नॉर्ब ऑर जस्ट द नॉर्ब?

### 02:41:57 · Speaker 3

I think it should be square. Square, yeah.

### 02:42:03 · Speaker 3

real fee of X I, you have

### 02:42:06 · Speaker 4

sigma phi of x i

### 02:42:08 · Speaker 4

Right? All you need to do is just one forward pass to get your mu p and sigma p, right? And let's write this as some

### 02:42:21 · Speaker 4

K L which is a function of mu V of X I and sigma V of X I

### 02:42:29 · Speaker 4

Right? So now you have to compute. Yeah, one forward pass. For the reverse pass, you just have to compute.

### 02:42:39 · Speaker 4

don't even have to go to decoder at all. Just compute this

### 02:42:44 · Speaker 4

scale of mu x i comma

### 02:42:47 · Speaker 0

sigma p of x i square and then simply

### 02:42:52 · Speaker 0

gradient of course

### 02:43:00 · Speaker 0

simply back propagate it here.

### 02:43:04 · Speaker 4

You know what happens is no for one one uh one uh iteration of encoder training you will have like one gradient coming through the decoder okay and like there will be just this plus KL gradient also gets added here.

### 02:43:26 · Speaker 4

we'll have to add both the gradients here. So this what we are adding here, okay, this will get added with the gradient that is coming from the decoder and this completes the encoder training.

### 02:43:37 · Speaker 3

Is it all right?

### 02:43:42 · Speaker 0

they should be straightforward, no, nothing complicated here. Now to train the decoder.

### 02:43:57 · Speaker 0

How do we train the decoder? So first thing to be seen is the second term

### 02:44:07 · Speaker 0

K L term

### 02:44:10 · Speaker 0

is independent of

### 02:44:13 · Speaker 0

decoder parameters theta, right?

### 02:44:21 · Speaker 0

we don't have to use that at all. Now what should we do is that we just

### 02:44:32 · Speaker 0

take an x i to have

### 02:44:34 · Speaker 0

to phi of z given x

### 02:44:41 · Speaker 3

just finish this and then close the class. This is sigma phi of x i, okay? Then you have like epsilon j.

### 02:44:49 · Speaker 0

coming from normal zero one

### 02:44:53 · Speaker 0

let it compute ZJ to be

### 02:45:03 · Speaker 0

and then you pass it through the decoder

### 02:45:11 · Speaker 0

So said

### 02:45:14 · Speaker 0

what you get is XJ cap

### 02:45:20 · Speaker 0

Right? Now how do we train this? So we have to do one complete forward pass.

### 02:45:28 · Speaker 3

as usual

### 02:45:31 · Speaker 3

then you do sampling and once you do from here it goes like this and then

### 02:45:35 · Speaker 4

it goes like this.

### 02:45:38 · Speaker 4

goes like this. You have to simply compute

### 02:45:42 · Speaker 4

the gradient theta which which term you have to compute? the term x i

### 02:45:48 · Speaker 3

minus d theta of z j

### 02:45:54 · Speaker 3

Complete D gradient of

### 02:45:57 · Speaker 3

this term with respect to J, right? and then simply back propagate this all the way through the input. That's all.

### 02:46:06 · Speaker 3

This is one decoder triangle.

### 02:46:09 · Speaker 0

monitors, you know, decoder drives.

### 02:46:12 · Speaker 0

Alright

### 02:46:16 · Speaker 0

easy, right? That's all. So now we are done with the training of VAE. Okay?

### 02:46:32 · Speaker 0

in the next class, no, when we begin

### 02:46:33 · Speaker 4

again we will look at how to do inference which is the we have to do sampling and also posterior inference no I think it's obvious right I mean you can once the training is done you just

### 02:46:47 · Speaker 4

discord the encoder and pass it through the pass Z through the decoder you will simply get uh the generation and you get take an X I pass it through the encoder you get the the embeddings right that's all it is. Always remember right whenever we are doing sampling in an encoder decoder model generation is always done through the decoder model. Okay. uh and the embeddings are extracted through the encoder model. So we will continue from here so what I'll do in the next class

### 02:47:17 · Speaker 4

discusses that we will look at like complete the V A E discussions and also look at one two improvisations over it especially I want to talk about one state of the art V A E model called vector quantized V A E or V Q V A E which is what is used in stable diffusion and all that okay that would be like

### 02:47:35 · Speaker 4

like thirty percent of the net class. And next we will go to diffusion models which are the state of the art for like image generation these days, okay? uh which is actually one particular form of the V A E.

### 02:47:49 · Speaker 4

But I urge all of you to kindly go through my notes and also today's discussion on V A E's and how to train them. I think I'm sorry I actually did it this way, right? I mean I inadvertently zoomed it at this point, but yeah, I think you can also zoom it, right? Because it's convenient. So please go through the class notes and also my handwritten notes and read the V A E paper and be thorough with all this before coming to the next class so that it will be easier for studying diffusion models and so on, okay?

### 02:48:20 · Speaker 5

सर वन क्वेश्चन

### 02:48:21 · Speaker 4

Okay. Yes.

### 02:48:23 · Speaker 5

So the first the first K L term that will be used to update both the encoder as well as decoder right like in the same pass

### 02:48:31 · Speaker 4

hold on. There is no first term is not the KL term, second term is the KL term.

### 02:48:41 · Speaker 4

See you just said first KL term there is no Sorry sorry I mean I mean

### 02:48:43 · Speaker 5

sorry sorry. I mean I mean I mean in the overall equation the first

### 02:48:46 · Speaker 4

and

### 02:48:49 · Speaker 4

Perikan

### 02:48:51 · Speaker 4

the reconstruction term it is called okay the reconstruction term is used to uh update both encoder and decoder but when you are training the encoder you keep the decoder parameters fixed and vice versa.

### 02:49:04 · Speaker 5

So can't we like so does that mean in in in one pass we cannot update encoder and decoder simultaneously?

### 02:49:13 · Speaker 4

How do you do it, no? See, you have to do take two gradient passes. I wrote the equation also, right here. Here, yeah, this is how you do it. First you have an encoder update and then a decoder update.

### 02:49:25 · Speaker 3

Okay

### 02:49:27 · Speaker 4

right? So when you train the encoder, you keep the decoder parameters fixed and vice versa.

### 02:49:32 · Speaker 0

Okay

### 02:49:33 · Speaker 3

Yeah. Arijit.

### 02:49:38 · Speaker 1

I I had a question on the assignment. Is this the right time to ask?

### 02:49:44 · Speaker 4

Yeah, let me just, any questions on the class before we go to the assignments?

### 02:49:48 · Speaker 6

Yes, so I had one question. So for example, in during this training, right? I mean, we start with the decoder training first or the encoder training first? I mean, in practical momentum.

### 02:49:56 · Speaker 4

doesn't matter. doesn't matter, doesn't matter. You just try one one one pass of encoder, one pass of decoder. That finishes one try. Yeah.

### 02:50:05 · Speaker 6

and any thoughts on the the conversions I mean how well this converges compared to say GAN

### 02:50:11 · Speaker 4

Yeah, this this will this will very nicely converge. There is no adversarial training that is happening here, no?

### 02:50:19 · Speaker 6

Yes

### 02:50:19 · Speaker 4

Unlike in a GAN, there is no, there is no min max, there is no, I mean encoder is not adversary to the decoder, right? They are both working towards the same objective.

### 02:50:27 · Speaker 6

Okay

### 02:50:28 · Speaker 4

VIs are known to converge much much better than gas. Yeah, because there is no adversarial saddle point problem, there is no saddle point problem here.

### 02:50:37 · Speaker 1

Yeah, understood. Thank you.

### 02:50:40 · Speaker 4

Okay, uh, yeah. Questions on assignment you said, yeah, go on.

### 02:50:45 · Speaker 1

Yeah, so sir, as I understood it, maybe I am wrong. One ago we are doing with

### 02:50:50 · Speaker 4

one ago we are doing with uh sorry can you make it quick I have another class at twelve thirty so

### 02:50:56 · Speaker 1

Yeah yeah sure sure sure. So one and two anyway we are doing with butterfly and rest all the animal data set right? So anyway we have to retrain the model with animal. So for the butterfly one can we go with our independence or freedom like choosing our loss and etcetera right? Because anyway we have to we are doing all this condition like usual loss WGAN loss separately for

### 02:51:18 · Speaker 4

अरे अरे अरे अरे होल्ड ऑन. व्हाट इज योर प्रिसाइज़ क्वेश्चन? प्लीज आस्क मी योर प्रिसाइज़ क्वेश्चन. आई डिडंट अंडरस्टैंड द क्वेश्चन.

### 02:51:26 · Speaker 1

Okay, then let me do one thing, let me WhatsApp you, Okay, that would be better. I think you have a class now.

### 02:51:31 · Speaker 4

you have a class

### 02:51:34 · Speaker 4

it's okay you can ask me the question I still have five minutes ask me the

### 02:51:37 · Speaker 1

Okay, no, I need to say

### 02:51:39 · Speaker 4

I need to say

### 02:51:40 · Speaker 1

Yeah, so the butterfly data set one, which we are doing one and two, I can use any loss of my choice, right? I mean, for example, WGAN or all, there is no boundation there, only the conditions are applied for the animal data set, which again anyway we have to retrain the model. Am I right?

### 02:52:00 · Speaker 4

Again, what is your question, yaar? I, I, so the question will have

### 02:52:03 · Speaker 1

No, I mean, butterfly one, we have the freedom to use any laws, function or anything, right?

### 02:52:12 · Speaker 4

Gyan you always use one loss function right which is that saddle point problem what is the other loss function that you would use

### 02:52:16 · Speaker 1

problem

### 02:52:19 · Speaker 1

because, uh, no, because there is a, I mean, we can use BC loss etcetera, right, also.

### 02:52:27 · Speaker 4

for a DC GAN loss does not change. Only the architecture changes, no?

### 02:52:33 · Speaker 1

Yes, yes, right.

### 02:52:35 · Speaker 4

Are you are you asking whether you can use an M L P for butterfly? Is that what the question is?

### 02:52:41 · Speaker 1

Yes, kind of

### 02:52:44 · Speaker 4

So yeah, you can use anything. See, but again, that's why I'm asking you that please if you if you make your question precise, the answer can be given precisely.

### 02:52:53 · Speaker 1

okay I think I will ask you separately then I mean Okay think about it and let me on WhatsApp yeah thanks yeah sure thanks bye

### 02:52:57 · Speaker 4

think about it and let just screen me on WhatsApp yeah thanks yeah

### 02:53:03 · Speaker 4

Sanjit

### 02:53:04 · Speaker 5

सर, जस्ट टू कन्फर्म, नेक्स्ट वीक वी आर नॉट हैविंग अ क्लास एंड आल्सो वी वोंट बी हैविंग अ क्विज, राइट? लाइक एवरी अल्टरनेट वीक वी वर सपोज्ड टू हैव अ क्विज।

### 02:53:11 · Speaker 4

we were supposed to have a quiz. Correct, correct, correct. So the schedule will change. So the quiz will be the week next afterwards, correct.

### 02:53:21 · Speaker 5

ओके सर

### 02:53:23 · Speaker 4

See, on that note, no, like, happy Dussehra to all of you. Yeah, Satya, go on. Yeah.

### 02:53:28 · Speaker 3

Thank you, sir.

### 02:53:30 · Speaker 2

So I have two questions in assignment. One is that we have mentioned is the decoder network for the eighth and ninth questions, right? So we discussed decoder network only in the VAE. So is it a similar concept we have to use it in the GAM as well?

### 02:53:43 · Speaker 4

Yeah, I have yes, correct. So I've precisely told you what to do, right? You train another network, see when you are training the GAN, just have another network which will take the generated image and just gives back the input input noise. And you can take an MSE between them and train it together.

### 02:54:00 · Speaker 4

Okay. Along with the, along with the, along with the adversarial objective.

### 02:54:01 · Speaker 2

Okay

### 02:54:07 · Speaker 2

Okay, okay. I think that's the same follow-up question I told you. So, you mentioned that use the augmented images for the training, right? So, is it only augmented image we have to use or is that existing original and augmented together we have to pass it together?

### 02:54:19 · Speaker 4

whenever you are taking augmented images you should always take the original plus augmented you should not give away the original thing. original images rotated by two three angles right and that would be your data set will increase by three four times. yeah. okay.

### 02:54:27 · Speaker 2

just

### 02:54:36 · Speaker 2

sorry, so one more thing. So this you mentioned the two inputs to be used, right, in this later stage. So it is a same distribution or it's a different distribution if the two inputs you mentioned?

### 02:54:46 · Speaker 4

or two input vector

### 02:54:47 · Speaker 2

two input vectors. As a fifth question, randomly sampling two input vectors. So it should be the

### 02:54:49 · Speaker 4

in

### 02:54:52 · Speaker 4

Yeah, they are, they are, they are just same distribution, right? I mean, in a GAN when you sample, you only sample from the same distribution at the input, otherwise, sample from different distribution till, yeah.

### 02:54:57 · Speaker 2

Sample

### 02:55:01 · Speaker 2

sample from

### 02:55:04 · Speaker 2

ओके, ओके. सो इट्स अ ज़ेड ओनली वी आर यूजिंग. यू हैव टू डू द टू टू टाइम्स. यू हैव टू टेक द टू इम्पोर्ट.

### 02:55:08 · Speaker 4

Yeah, it's a tough question.

### 02:55:10 · Speaker 2

Okay

### 02:55:10 · Speaker 4

take two z's, pass it through the encoder generator and then interpolate between them and observe what happens at the output, okay?

### 02:55:15 · Speaker 2

bit

### 02:55:18 · Speaker 2

ओके ओके ओके थैंक यू सर

### 02:55:21 · Speaker 4

Yeah, Karthik

### 02:55:22 · Speaker 7

Sir, about the exam, so portions till this time, including the references that you have mentioned in your handwritten notes and all the classes, that's what we should be expecting, right?

### 02:55:31 · Speaker 4

should be expecting, right? Correct, correct.

### 02:55:33 · Speaker 7

and like it would be a theory only and mostly derivations would be involved. Just want to know the type of queries that we should be more prepared.

### 02:55:41 · Speaker 4

I have not I have not said the question paper yet. So it will be it will involve some math, okay? It will I will not be asking you questions like differentiate between GANs and VAEs. That's not how it will be. It will be like some thought provoking and you have to do you have to practice math, okay?

### 02:55:45 · Speaker 7

will be

### 02:55:59 · Speaker 7

Sure. Thank you.

### 02:56:00 · Speaker 4

Yeah, it will not be descriptive. I will not be asking you to like describe how Gyan works and all that. No, definitely not, okay?

### 02:56:09 · Speaker 7

Sure sir. Thank you.

### 02:56:12 · Speaker 4

Okay, so see, uh feel free to like ping on that WhatsApp group or teams and get in touch with TAs, you know, they are helpful as well. Both Suhas and Chandan, you can get in touch with them. Okay? And you can always ask me questions as well. Uh yeah, and all the best for your exam. I will I will I will I will give you detailed instructions on how the exam would be and all that. Once I complete the question paper, which is like I'll do it the mid next week and once I do that I will tell you like what the instructions are and so on okay

### 02:56:47 · Speaker 7

Sir, uh,

### 02:56:47 · Speaker 4

But yeah, anytime you can, yeah.

### 02:56:49 · Speaker 7

Yeah, sorry, sir. Should we be like looking into the previous year model paper if you have any like whatever the paper you have?

### 02:56:56 · Speaker 4

Don't know where it is. It should be there somewhere. I don't know where it's, where is it. Don't worry, yeah, don't worry too much. It's fine, yeah.

### 02:57:04 · Speaker 0

Thank you

### 02:57:08 · Speaker 3

ओके, सी यू देन, ऑल द बेस्ट.

### 02:57:13 · Speaker 0

Thank you sir

### 02:57:15 · Speaker 0

Thank you sir. Thank you sir. Thank you sir.

### 02:57:16 · Speaker 3

Thank you sir

### 02:57:17 · Speaker 0

Thank you sir

### 02:57:19 · Speaker 0

Thank you sir

### 02:57:21 · Speaker 0

Have a nice weekend.
