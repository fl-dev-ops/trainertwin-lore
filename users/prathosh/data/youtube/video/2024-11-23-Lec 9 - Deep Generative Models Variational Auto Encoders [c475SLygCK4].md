---
id: c475SLygCK4
title: Lec 9 - Deep Generative Models Variational Auto Encoders
url: https://www.youtube.com/watch?v=c475SLygCK4
date: '2024-11-23'
duration: 02:57:32
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# Lec 9 - Deep Generative Models Variational Auto Encoders

## Transcript

### 00:00:03 · Speaker 1

or something

### 00:00:05 · Speaker 1

So I 14th is when it is ending for the off-line semester I think we'll have one on 16th I think that should be okay

### 00:00:14 · Speaker 1

And given that you have an exam next Sunday not having a class on Saturday is okay I suppose okay we'll do it that way

### 00:00:23 · Speaker 2

No one

### 00:00:27 · Speaker 1

Shall we start today

### 00:00:36 · Speaker 1

uh okay so as i said no today's um uh focus will be on the variational autoencoders or vae's okay so as a precursor uh we were looking at uh latent variable models last time correct now what are latent variable models uh these are uh models that are defined as uh okay so whenever i talk of a model

### 00:01:08 · Speaker 1

model yeah so p theta which is a distribution over the uh the data variable right is what is called as a model so whenever we talk of model it is p theta that we talk of okay now in a latent variable setting that p theta is given as a marginal over the joint distribution of two uh variables okay one is called the uh the data variable of course x uh which is given and one is the latent variable that is not observed

### 00:01:38 · Speaker 1

I mean that's why the name latent of the hidden variable

### 00:01:42 · Speaker 1

Okay, so what happens in a latent variable model? So what is a latent variable model where p theta, the model is given as a marginal over the joint distribution of the latent and the data variable. So that is what is called as the latent variable model. Unfortunately, this does not have a pointer. Otherwise, I've been so nice that I pointed things out when I was recapping. Anyway, okay.

### 00:02:12 · Speaker 1

As the name suggests the latent variable model latent variables are not observed right they are not observed they are to be estimated together with the model parameters so typically z is also estimated or learned along with the model parameters theta

### 00:02:28 · Speaker 1

Now the way it is defined is for every observed data point which is in the data set D, there exists a corresponding latent variable that is not observed. So several examples, latent variable can be discrete or it can be continuous. If latent variable is discrete, the example that is given is that of the Gaussian mixture model or k-means clustering, where the latent variable denotes what cluster.

### 00:02:58 · Speaker 1

or what group of Gaussian that it belongs to. Okay, that is one example. The other example is a latent variable which is continuous. Whenever you have this encoder-decoder model, it may not be autoencoder. Any kind of encoder-decoder model is a latent variable model with the output of the encoder seen as a feature or latent variable corresponding to xi. Right? So that is, yeah. So feel free to ask questions. I'm just recapping what we said.

### 00:03:28 · Speaker 1

saw in the last class. If you have any questions, you can raise your hand and ask. Okay. Now, this is about the definition of latent variable model. Now, the question is, how do we model distributions using latent variable model? So, that is the question. So, now, as I said, the P3 topics in the case of latent variable model is given as a marginal over the joint distributions. And in all latent variable models, the optimization is

### 00:03:58 · Speaker 1

usually carried out by maximizing the log likelihood or minimizing the KL divergence. So the objective is to maximize the log likelihood or minimize the KL divergence. So for the rest of the lecture, I will be using the term maximization of log likelihood not minimization of KL divergence because they are equivalent. The reason I am using the term log likelihood is because that is what is usually used in the literature everywhere.

### 00:04:28 · Speaker 1

Okay, so now how do we model the how do we get the parameters of latent variable model as I told in latent variable models right the latent variable also has to be estimated jointly with the model parameters theta. So now what do you mean by estimating the latent variable because we are talking about random variables here and latent variable is another random variable it amounts to estimating a distribution over the latent variable.

### 00:04:58 · Speaker 1

That is what it means by estimating a latent variable. How did we do that? We wrote down the log likelihood as L theta. And we multiplied and divided the log likelihood by some distribution that you would want to estimate on the latent space. Call it as Q of Z given X. And then with the Jensen's inequality, what we found out was that there exists a lower bound on the

### 00:05:28 · Speaker 1

log likelihood that you would want to optimize. So yeah the storyline is the following right. There is a model latent variable model with parameters theta and we want to estimate the parameters of that model theta along with the distribution over the latent variables right. Now the distribution over the latent variable is what we called as a variational latent posterior denoted by Q of Z given X.

### 00:05:53 · Speaker 1

Now, when you introduce this unknown latent variable or distribution of the latent variable into the model, you cannot directly optimize the log likelihood, okay? Because in most of the latent variable models, computing this integral, right, to get your p theta, okay? p theta is an integral over the joint distribution of x and z. That is not feasible because you don't know what the latent variable is. What you can do is take a guess on the latent variable distribution.

### 00:06:23 · Speaker 1

which is called as Q of Z given X. Once you take a guess on the latent variable, latent distribution on the latent variable, there will be an inequality that arises which means that you will get, see observe this, what you would want to maximize which is the log likelihood L theta, whenever you take a guess on the latent variable, okay, via the distribution Q, there will be a lower bound that is created on the log likelihood.

### 00:06:55 · Speaker 1

Now that lower bound is what is called as the evidence lower bound or elbow. With our choice of q and theta, you will get a particular elbow or the evidence lower bound. Now the goal in all latent variable models is to find out model parameters theta and a distribution of the latent variables q such that the evidence lower bound is maximized.

### 00:07:25 · Speaker 1

the log likelihood but because we cannot do it exactly what we do is we will optimize a lower bound on the log likelihood which is called the evidence lower bound so it takes this particular form that i have written in the box item okay um any questions so far because this is the param this is of paramount importance because this is what we are this is the idea that we are going to use uh multiple times uh when we optimize uh like when we when we you when we look at we

### 00:07:55 · Speaker 1

and diffusion models all these models right they work in this particular principle that there is we are looking at a latent variable model okay what is a latent variable model it is given by where the distribution over the data is given as a marginal over the joint distribution of the data variable and another unobserved variable denoted by z called the latent variable okay the goal is to minimize the k divergence and find out the parameters theta now we cannot

### 00:08:25 · Speaker 1

do it because exactly we cannot do it because uh we do not know what the latent variable is. So, we assume a distribution over the latent variable called I mean denoted by q of z given x. Once we assume a distribution over the latent variable there will be a lower bound that will be constructed on the objective the log likelihood that we would want to maximize right and when we are maximizing it we would learn both the model parameters theta and the distribution of the latent variable by maximizing the lower bound.

### 00:08:55 · Speaker 1

And that lower bound is given by this expression, right? Expectation of log of p theta x and z divided by q of z given x. And the expectation is over q of z given x. So this is what we optimize whenever we are looking at VAEs and diffusion models and so on.

### 00:09:13 · Speaker 1

Any questions on this? Please ensure that you understand this like right I mean then after that we will continue yeah

### 00:09:25 · Speaker 2

Yes, so this Q of Z given X is also unknown, right? So, how do we compute the X?

### 00:09:29 · Speaker 1

I I I'll tell you I'll tell you that I still know we don't know what Q of C connect that's why I said no the look at the box item it is an optimization joint optimization over theta and Q

### 00:09:44 · Speaker 1

You have to compute both theta and the cube

### 00:09:49 · Speaker 1

They're jointly estimated

### 00:09:54 · Speaker 2

We'll cover that right so

### 00:09:56 · Speaker 1

Absolutely that's exactly what we'll do

### 00:09:59 · Speaker 1

Any other questions

### 00:10:07 · Speaker 1

So this broad philosophy of what we are doing is clear, I suppose. Okay. Now we took an example after that, the last class, which is a Gaussian mixture model. Gaussian mixture model is a latent variable model. Okay. It's a proper latent variable model where p theta is given by, again, marginal of the joint distribution, marginal over the joint distribution of x and z. right and this is the definition of a gmm no this equation second equation period of x is given by a linear combination of multiple gaussian distributions

### 00:10:37 · Speaker 1

having different means and variances. Now a set of parameters are the mixing coefficients which are alpha 1 through alpha m. There are m number of mixtures, m number of means and m number of variations. Sorry, variances. Now what do we do? We want to solve that optimization problem, right, with respect to theta and q, right. How do we do it? We do it alternatively. First we solve for theta assuming that q is known and then we will solve for q assuming that theta is known.

### 00:11:07 · Speaker 1

Now what can be shown, Raghavendra, I said this last class, maybe I have forgotten. See this is in GMM, the way to find this Q, you said that Q is unknown, no? What can be shown is that at a given theta, the optimal Q, okay, that would make the lower bound tight. What do you mean by lower bound tight? The lower bound that we have constructed on the log likelihood will be equal to the log likelihood. That is the best value that it can assume, no? Lower bound.

### 00:11:37 · Speaker 1

can assume the best value which is equal to the log likelihood. Now that would happen if the q the choice of q that you have made for a given theta is p of z given x.

### 00:11:50 · Speaker 1

So if Q is fixed to be P of z given X or P theta of z given X

### 00:11:56 · Speaker 1

That is the best estimate for Q

### 00:11:59 · Speaker 1

It's all right

### 00:12:02 · Speaker 2

I mean sir uh we we said that we would cover this in the TA session but I think last session we did not have it so maybe we'll cover this in the next session

### 00:12:09 · Speaker 1

I meant is no no what I meant is what will be covered in the session is that the proof of this that optimal Q for knowing a particular I mean for given a particular theta is P theta of z given x

### 00:12:26 · Speaker 1

This will be covered. So this is an algebraic proof. But what is important is that, I mean, see, I didn't do it in the class and I don't want to do it in the class because in VAEs and diffusion models, we will not use this because in neural models, we will not know what p theta of z given x is.

### 00:12:50 · Speaker 1

That's the reason. So the jump from mixture models to like autoencoders, I mean VAEs is because of this fact. See, had we knew p theta of z k 1 x, then the problem of latent variable models is solved because you have the EM algorithm and this can be done. But since we do not will not know what p theta of z k 1 x is, that is why we need to move to something else. So please note this everyone.

### 00:13:19 · Speaker 1

So again, I'm reiterating it, it's very, very important. So now the goal is to find model parameters theta and the variational distribution or the latent variable distribution Q together.

### 00:13:32 · Speaker 1

Now, there is a result that would show that the optimal Q or the optimal distribution over the latent variable is actually P theta of Z given X.

### 00:13:44 · Speaker 1

Now, if you know how to compute p theta of z given x, then it is done. Because we know what the optimal, what we can do is we can do this alternative optimization where you start with a random theta, right, and set this q to be equal to p theta of z given x when we know how to compute p theta of z given x, okay. And then with that q, you find the next best theta and keep alternating between them.

### 00:14:10 · Speaker 1

Okay, now how do we know p theta of z given x? p theta of z given x is given by the Bayes rule, okay, which is written here. And in the case of a GMM or other mixture models, we know how to compute p theta of z given x given a particular theta. And therefore, we know how to compute Q optimal Q. Understand? So once we get that optimal Q, what do we do that? We plug in that optimal Q in this evidence lower bound f theta, okay, and optimize the

### 00:14:40 · Speaker 1

take a derivative of that with respect to theta and then find the new theta with that new theta you again compute p theta of z given x and keep alternating between them which is called the expectation maximization algorithm

### 00:14:57 · Speaker 1

Does it make sense? So I have said this also, right? So yeah, so the question is, however, what if p theta of z1x cannot be computed? So if you have models and in a Gaussian mixture model or a simple other mixture model, p theta of z1x can be computed. If you cannot compute p theta of z1x, you don't know what your optimal q star is. And you do not know what the optimal q star is. How do you compute, how do you estimate the parameters of a latent variable model is the primary question that would be, that would be.

### 00:15:27 · Speaker 1

Take a nap A

### 00:15:32 · Speaker 1

Does it make sense Any questions so far

### 00:15:36 · Speaker 1

This is exactly what we do in GMM, right? GMM is also a latent variable model, okay? We estimate f theta or we estimate theta and q alternatively and this algorithm is called the expectation maximization algorithm. And for EM algorithm to work, no, we need to know what the optimal q is or we need to be able to compute p theta of z given x.

### 00:16:02 · Speaker 1

It is

### 00:16:07 · Speaker 1

Please ask questions if you have any then I'm waiting

### 00:16:22 · Speaker 3

So in this EM algorithm which we have mentioned we are trying to find p theta of z given x

### 00:16:30 · Speaker 3

using the Bayes theorem so but the p theta of x given z is also unknown right

### 00:16:37 · Speaker 1

theta of x k x given z x given z is known no because that is a single parameter Gaussian it's actually a Gaussian distribution by assumption by construction by definition

### 00:16:52 · Speaker 1

and I go back to the next slide

### 00:17:02 · Speaker 1

I don't intend to like teach GMMs anyway so here now yeah that is what I have written here look at this

### 00:17:10 · Speaker 3

For a given z we have p theta of okay

### 00:17:13 · Speaker 1

It's a particular Gaussian. See in a GMM the way you model the distribution you show that.

### 00:17:22 · Speaker 1

This is how we model it now p theta of x is given by this linear combination of multiple Gaussians

### 00:17:30 · Speaker 1

Okay now this can be written this way right there so this is equal to

### 00:17:37 · Speaker 1

equal to one to n

### 00:17:40 · Speaker 1

e theta of z into e theta of x given z

### 00:17:50 · Speaker 3

Yes sir

### 00:17:51 · Speaker 1

So this it is alphas okay and this every one is a Gaussian

### 00:17:59 · Speaker 1

With a particular let me write this the beta dot z

### 00:18:04 · Speaker 1

is equal to some particular j the mu j and sigma j

### 00:18:12 · Speaker 1

Alright so we do know that

### 00:18:14 · Speaker 1

The conditional of X given a particular Z is a single component Gaussian

### 00:18:27 · Speaker 3

Understood sir

### 00:18:30 · Speaker 1

Any other question on this

### 00:18:33 · Speaker 2

So does it have to be a convex combination

### 00:18:37 · Speaker 1

in mixture model yeah yeah yeah in mixture density is always taken because the reason is uh if you look at it now alphas are distributions over discrete uh variable z isn't it

### 00:18:53 · Speaker 1

alpha will give you a discrete also p theta of z given j is given by alpha j right which means that if we take

### 00:19:09 · Speaker 1

over all j they should sum to one and all of these have to be non-zero because they are probabilities no

### 00:19:18 · Speaker 1

So they have to be all that is why it has to be concurrent coordination

### 00:19:23 · Speaker 1

And by the way a mixture density right you don't add the mixture density need not be a Gaussian mixture model no it can be exponential mixtures or Bayesian I mean sorry Bernoulli mixtures or anything

### 00:19:36 · Speaker 1

To model uh data which which has infinite support and uh like the the vector value which lies in continuous space right usually GMMs are preferred

### 00:19:50 · Speaker 1

And did I also talk about the clustering? See one other thing in a latent variable model is tell you post training

### 00:20:01 · Speaker 1

So training is what training is uh like estimation of theta that's what training is all about

### 00:20:09 · Speaker 1

After we estimate theta okay a latent variable model

### 00:20:23 · Speaker 1

The different variable model can be used

### 00:20:28 · Speaker 1

can be used for

### 00:20:32 · Speaker 1

policies

### 00:20:35 · Speaker 1

This can be any latent variable model, including a GMM. The first thing is

### 00:20:41 · Speaker 1

Uh sampling or generation because these are generating models right

### 00:20:55 · Speaker 1

Now example how do we do it in GMM is that in a GMM

### 00:21:02 · Speaker 1

Now first you sample a Z from

### 00:21:06 · Speaker 1

I'm discrete

### 00:21:09 · Speaker 1

alpha 1 alpha 2 up to alpha m so note that all of these are estimated using the EM algorithm once you estimate them this what is this is actually a tossing an m-phase die so first you do that and then

### 00:21:25 · Speaker 1

Sample X

### 00:21:31 · Speaker 1

X given Z okay by Gaussian so let's say that the outcome of this is

### 00:21:43 · Speaker 1

i is the outcome alpha i is the outcome

### 00:21:50 · Speaker 1

Uh okay so let's call i is the outcome

### 00:21:58 · Speaker 1

Once you do that what you should do is sample an X

### 00:22:02 · Speaker 1

By Agashen which is the which has the ayat mean

### 00:22:09 · Speaker 1

And I have the variants that's all

### 00:22:13 · Speaker 1

Yeah, that's all it is. So this is how you do a generation in a GML.

### 00:22:18 · Speaker 1

Whatever x that you get now by doing the sampling this is z equal to i you do that sampling via a Gaussian in fact if you look at the Bishop's book which is like

### 00:22:30 · Speaker 1

classical book by bishop pattern recognition so what you will see is that he has shown uh what will happen uh if we do sampling i mean if we fit a gmm to mns data and do a sampling it will look like some images right but it will not be like as good as it says some other generative models such as gans so what happens is no in very high dimensions uh these gm gmm's they often tend to

### 00:23:00 · Speaker 1

have this curse of dimensionality and they will not uh model the data well so that is because of the saturation of the EM algorithm again NOI

### 00:23:09 · Speaker 1

Since I am not teaching GMM, I am not going into details of it, but yeah. Okay. This is how you sample from a GMM. I will talk about how do you sample from a from a variational autoencoder. But yeah. So what is more important is that one can use a latent variable model to do sampling or generation. The other thing that can be used that these models can be used is what is known as posterior inference.

### 00:23:41 · Speaker 1

Posterior inference okay

### 00:23:46 · Speaker 1

also known as feature extraction feature or embedding extraction

### 00:24:01 · Speaker 1

becomes embedding extraction if

### 00:24:07 · Speaker 1

This is uh or it's also called as clustering

### 00:24:14 · Speaker 1

f for Z discrete

### 00:24:22 · Speaker 1

Now what is this So given

### 00:24:28 · Speaker 1

Fine

### 00:24:31 · Speaker 1

A latent variable model

### 00:24:38 · Speaker 1

Um

### 00:24:42 · Speaker 1

And give one

### 00:24:45 · Speaker 1

Data point X

### 00:24:51 · Speaker 1

Oh you just compute compute

### 00:24:57 · Speaker 1

Few starters

### 00:25:00 · Speaker 1

the g on x that's all so this let's see what happens is uh if in in the case of uh uh q

### 00:25:12 · Speaker 1

Let us say it that way compute or sample from either both of them are possible I'll give you I mean there are different variants of it okay now let me tell you what it is compute

### 00:25:25 · Speaker 1

will start of G G1X

### 00:25:30 · Speaker 1

Or sample number

### 00:25:38 · Speaker 1

depending upon what the case is. Okay, so what do you mean by this?

### 00:25:44 · Speaker 1

So given a data point x now post training given a data point x I am finding out a distribution over the the latent variable given the data point

### 00:25:56 · Speaker 1

So let's say that uh let that Z is uh discrete then what will happen you take Z is discrete

### 00:26:06 · Speaker 1

If Z C is discrete we have values one through M so C can take M values

### 00:26:15 · Speaker 1

z can take 1 through m values. So if you are computing q star of z given x, what will happen is there will be a discrete distribution over z.

### 00:26:30 · Speaker 1

There will be an entire distribution over Z what is this

### 00:26:35 · Speaker 1

This is called clustering

### 00:26:40 · Speaker 1

So every x now is divided into one of m possibilities right that is that is clustering okay. Now if z is continuous then what will happen is given a

### 00:26:56 · Speaker 1

given a given a given an x okay so you'll find out a z given x okay which is a sample from q of z given x that particular z given x this will be a vector

### 00:27:11 · Speaker 1

turns on rk where that is where the z lies so this is typically referred to as the embedding so all these bird embeddings etc that you see no textual embeddings and image embeddings etc are nothing but samples from uh the posterior the latent posterior given data so this is one other usage of latent variable models

### 00:27:34 · Speaker 1

That is why now we say that we can do clustering using GMM, right? So GMM is a latent variable model with discrete latent space, okay? And that's why we can do clustering of it. It is either GMM or K means K, which is a special case of GMM, right? All these are clustering methods.

### 00:27:52 · Speaker 1

Under the hood what is happening is that you are estimating Q star of Z given X. So two things can be done right. One you can do sampling or generation okay which is simply the generative task that we were looking at. The other thing that you can do is what is called as posterior inference that is that given a particular point X you can find out Q star of Z given X. Is this okay? So these are two tasks.

### 00:28:15 · Speaker 3

So do that

### 00:28:17 · Speaker 3

Sir in the embedding case the received vector will be a one hot vector right

### 00:28:23 · Speaker 1

No no no no no uh I mean you mean the X you are talking about is it

### 00:28:27 · Speaker 3

No sir, um Z given A the the resulting vector

### 00:28:31 · Speaker 1

No no no it is not one one one one hot no see that's what I'm saying think of an autoencoder right you have an encoder decoder model I cover all that detail in detail but I'm just giving you an overview here so if you have uh like let's i mean if you know what bird embeddings mean there is a pre there's a trained model you pass it through a trained model right your x which can x can be one hot and you will you will get a particular vector at the output that's all it is

### 00:29:02 · Speaker 1

That vector is a sample from ZQ on X yeah that's your embedding

### 00:29:06 · Speaker 2

So why do you call it as a sample so that means uh for a given x you can get a different values of z

### 00:29:12 · Speaker 1

The reason I'm calling it as a sample is because in in in whenever the the uh the

### 00:29:21 · Speaker 1

Latent variables are continuous no You won't get an entire distribution over z given a particular x

### 00:29:28 · Speaker 1

especially in in in in in cases like uh BERT and all that but as we will see uh in a VAE right uh Q is modeled I mean the you you you will get an entire distribution over the Z okay but typically when people call it as embedding extraction no it's always a sample from Q not an entire distribution see I just wanted to make this distinction that if Q is discrete then given an X you get an entire distribution over Q sorry

### 00:30:01 · Speaker 1

Right, but when Q is continuous, typically, typically, what happens is you get a sample from Q star, not an entire distribution. I just wanted to make the distinction.

### 00:30:14 · Speaker 1

Any other question? So two, I mean, remember these two things, no? I mean, this is how the VAE paper starts also, that the goal is to do two things, that given data, you need to first learn a latent variable model, which is by maximizing the likelihood or ELBO. Second task is to after you have completed your training, we need to do generation, okay, or sampling, and then we do posterior inference. So let me write it in the next thing itself.

### 00:30:40 · Speaker 3

Sir which paper is it uh what I've I forgot the name you mentioned

### 00:30:45 · Speaker 1

Are you looking at my handwritten notes

### 00:30:52 · Speaker 1

Because there I have like at the end of my every each notes I tell you the name of that paper but I encourage all of you to actually look at my handwritten notes it's very lucidly written

### 00:31:00 · Speaker 4

It's very lucidly written

### 00:31:05 · Speaker 4

It's a Kingma and Willing

### 00:31:09 · Speaker 1

Yeah Velling and King's paper I tell you the name see what's important is don't digress what's important is that you all of you look at my handwritten notes at the end of my handwritten notes key papers are listed and I expect and by the way for the exams I think this is the way to make you read right there is only one way for your exams right all the papers that I have listed in my handwritten notes at the end of them they are they are a part of syllabus

### 00:31:36 · Speaker 1

so you are supposed to read those papers there are only four five papers per topic so please read them yeah so the name of the paper is uh vae's paper is auto encoding variational ways

### 00:31:51 · Speaker 1

If you google for VAE original paper, you'll get that. But the title is auto encoding variational base. So please read my handwritten notes once and the citations that are given at the end of each chapter. I urge all of you to do that. Okay. So now the problem here is that given D, which is data,

### 00:32:16 · Speaker 1

samples from

### 00:32:20 · Speaker 1

Examples drawn ID from an unknown distribution PX. Okay, the goal is threefold.

### 00:32:31 · Speaker 1

Little now

### 00:32:35 · Speaker 1

Learn a latent variable model

### 00:32:47 · Speaker 1

Unknown

### 00:32:51 · Speaker 1

in posterior right I mean this is what it makes different from uh EM okay if you read the introduction of that paper no they will actually say that uh because P of P theta of Z given X is unknown we are assuming that it is not known we want an alternative method because otherwise in fact they explicitly say that EM cannot be used because we don't know what P theta of Z given X is okay that's the first goal the second goal is that you need to do

### 00:33:29 · Speaker 1

generation

### 00:33:33 · Speaker 1

Sampling post-training

### 00:33:46 · Speaker 1

Third goal is to

### 00:33:50 · Speaker 1

Enable posterior inference

### 00:33:58 · Speaker 1

which is nothing but estimating the u star of the

### 00:34:05 · Speaker 1

Okay, so these are the three goals that are cited in the VA paper or maybe let me just show you that. It'll be nice to see that once.

### 00:34:15 · Speaker 1

See a lot of times right we uh these uh BAE paper

### 00:34:24 · Speaker 1

These papers are sort of intimidating but one of the goals of this the one of the goals of designing this particular course was to ensure that you people start reading papers students start reading papers and you know you don't get intimidated looking at it okay so they will say the following here

### 00:34:51 · Speaker 1

So, we are interested in and propose a solution to three problems in the above scenario, right? Efficient approximate maximum likelihood estimation for parameter parameters of theta. That's not very good map estimation. It's the efficient approximate maximum likelihood estimation of parameters of theta. Number one. The second thing is efficient approximate posterior inference of the latent variable given an observed value x for a choice of parameters theta. For a choice of parameters theta meaning post-training. And this is useful for

### 00:35:21 · Speaker 1

For coding or data representation tasks, that is what is meant by embedding extraction or representation learning. Second thing is you need to efficient approximate marginal inference of the variable x. This allows us to perform all kinds of inference tasks where a prior over x is required. Common application in computer vision include image denoising, inpainting and super resolution. All these are generative tasks.

### 00:35:47 · Speaker 1

So these are the three questions that is asked. So this is that paper, which is VAE's paper. We will go into all these details and math in a very, that is what we do in this lecture. But yeah, so these are the three questions that are of interest, which is learn a latent variable model with unknown p theta of z on x. Oh, I should also show you that now, that they say that EM is not feasible.

### 00:36:13 · Speaker 1

interactability look at this no the first point here in one two interactability the case where the integral of the marginal is intractable

### 00:36:25 · Speaker 1

Where the true posterior density p theta of z given x is intractable. So the EM algorithm cannot be used.

### 00:36:31 · Speaker 1

That okay

### 00:36:35 · Speaker 2

So it is intractable because we need to do it over all values of Z or

### 00:36:39 · Speaker 1

Well, not necessarily, right? I mean, for instance, if you assume z to be continuous variable with unknown distribution, it's you cannot find that integral one thing. The other thing is, see, observe that p theta of z given x involves a division by p theta of x, which is again an integral over the joint distribution, and this integral is over z. So if you assume z to be of very high dimensions, that integral cannot also be computed.

### 00:37:08 · Speaker 2

Okay yeah got it

### 00:37:09 · Speaker 1

Yeah, so because that is why EM cannot be used here and we need something else other than using EM. That's the prelude. So please read. See, these are sort of seminal papers, okay, which are very good to read and you'll gain a lot of insights. I have gained a lot of insight by reading those papers as a student. So please do read them. I recommend all of you to read that. Similarly, that FGN paper.

### 00:37:32 · Speaker 1

I don't know if I showed you that so we covered that no this if GAN

### 00:37:42 · Speaker 1

it's variational divergence minimization let's see yeah this one training generative neural samplers using variational divergence minimization so this is what we actually covered in class

### 00:37:53 · Speaker 1

So this was the paper that I covered in class in all these lower bounds that we constructed etc. So with the background that you have right now, please read the paper. It's short and extremely insightful.

### 00:38:08 · Speaker 1

I urge you to read all these at least these fundamental seminal papers okay

### 00:38:14 · Speaker 1

Right so we have these three objects

### 00:38:18 · Speaker 1

To to learn given the data, we will start doing it, okay? So now

### 00:38:32 · Speaker 1

Recall

### 00:38:38 · Speaker 1

latent variable model

### 00:38:49 · Speaker 1

each other

### 00:38:53 · Speaker 1

k1 by the integral of p theta

### 00:38:57 · Speaker 1

given z times

### 00:39:00 · Speaker 1

the shift of the whole DC right so is also equal to the joint distribution of

### 00:39:11 · Speaker 1

Now the goal is to learn

### 00:39:16 · Speaker 1

Longita star

### 00:39:19 · Speaker 1

That would

### 00:39:21 · Speaker 1

Maximize the log of the likelihood

### 00:39:29 · Speaker 1

So we saw that this is uh

### 00:39:32 · Speaker 1

Approximately

### 00:39:35 · Speaker 1

MS

### 00:39:38 · Speaker 1

finding out the

### 00:39:41 · Speaker 1

theta such that the lower bound on the evidence is maximized which is the evidence lower bound where

### 00:39:57 · Speaker 1

Okay now f theta

### 00:40:00 · Speaker 1

Q is given by the expectation of log of

### 00:40:08 · Speaker 1

Eat it up

### 00:40:10 · Speaker 1

X and Z divided by

### 00:40:13 · Speaker 1

You off

### 00:40:16 · Speaker 1

Cythonics

### 00:40:21 · Speaker 1

respect to Q1 C1X right

### 00:40:26 · Speaker 1

A few with me so far

### 00:40:30 · Speaker 1

Now we need to find the theta such that it is maximized. Now let us simplify this.

### 00:40:41 · Speaker 1

You to see you on next

### 00:40:44 · Speaker 1

Slow down

### 00:40:46 · Speaker 1

beat here doc

### 00:40:49 · Speaker 1

Given Z times P theta of Z divided by

### 00:40:58 · Speaker 1

It off

### 00:41:00 · Speaker 1

See you guys next

### 00:41:03 · Speaker 1

is equal to expectation log of

### 00:41:08 · Speaker 1

E to the top x given z

### 00:41:12 · Speaker 1

Thank you all, see you guys next

### 00:41:17 · Speaker 1

Minus

### 00:41:19 · Speaker 1

Expectation see you next

### 00:41:24 · Speaker 1

Mm

### 00:41:26 · Speaker 1

Two or three given X divided by

### 00:41:30 · Speaker 1

into the .c

### 00:41:33 · Speaker 1

All right, I just used two things here, one, linearity of expectations and law of logarithms. Any questions on this stuff?

### 00:41:44 · Speaker 1

did I do there is log of a b divided by c I wrote it as log a minus log c by log b so minus came here because I I inverted the numerator and denominator

### 00:41:58 · Speaker 1

Is it alright

### 00:42:10 · Speaker 1

Hello are you there

### 00:42:12 · Speaker 2

Yes sir

### 00:42:15 · Speaker 1

Is that alright any questions on this

### 00:42:23 · Speaker 1

respond how do I know uh maybe I'm not uh this is all right no yeah okay uh okay let's move on so this is

### 00:42:34 · Speaker 1

Expectation of law of

### 00:42:38 · Speaker 1

theta of x given c and this is with respect to z given x minus what's the second term can can you recognize the second term

### 00:42:50 · Speaker 2

real divergence of QZ given

### 00:42:53 · Speaker 1

Yeah and the

### 00:42:53 · Speaker 2

And the end

### 00:42:55 · Speaker 1

The decay and divergence

### 00:42:58 · Speaker 1

between u and z given x

### 00:43:03 · Speaker 1

Be careful

### 00:43:05 · Speaker 1

So this is

### 00:43:07 · Speaker 1

Actually the last function of a VA okay this is thing but elbow right we are writing the evidence like like evidence lower bound expressing this this way so this if you want to remember something this is something that you would want to remember this is D

### 00:43:25 · Speaker 1

Conditional

### 00:43:30 · Speaker 1

I'll let you hear

### 00:43:35 · Speaker 1

Okay, let me interpret it later. Okay, so this is the equation. So you have LBO can be decomposed into two terms, one which is an expectation of log of p theta of z given x given z, and there is a clear divergence between Q of z given x and p theta of z. Okay.

### 00:43:54 · Speaker 1

Now what is done in a VAE is that the first thing that you do is

### 00:44:06 · Speaker 1

Approximate

### 00:44:13 · Speaker 3

So one question

### 00:44:16 · Speaker 3

For this to be KL divergence, there should be a p theta of z term also, right, before log.

### 00:44:25 · Speaker 1

should be a q of z given x term

### 00:44:28 · Speaker 3

Yes q q of z given x

### 00:44:30 · Speaker 1

There's expectation is there no expectation is integral QZP is Linux log of QYP isn't it

### 00:44:37 · Speaker 3

Okay, okay

### 00:44:41 · Speaker 1

It is

### 00:44:44 · Speaker 1

is integral using the on X

### 00:44:47 · Speaker 1

log of plus e one x divided by

### 00:44:57 · Speaker 1

That scale no

### 00:45:02 · Speaker 1

Okay so what's important now is that you approximate p theta of z sorry p theta of x given z

### 00:45:12 · Speaker 1

And

### 00:45:15 · Speaker 1

U or Z here next

### 00:45:20 · Speaker 1

Giral networks

### 00:45:28 · Speaker 1

So let's call that as q phi because there are two neural networks neural networks theta neural networks with parameters theta and phi

### 00:45:38 · Speaker 1

Okay, so what we do is, you look at this elbow, right? There are two distributions that we are talking about here, which is Q of Z given X, which is the unknown posterior. Okay, the other thing is P theta, another thing is P theta of X given Z. We represent both of them using neural networks. Now, observe the difference here from the EM algorithm, right? In EM algorithm, Q of Z given X, the optimal Q of Z given X was known to be P theta of Z given X.

### 00:46:08 · Speaker 1

because because we don't know what p theta of j given x is we approximate that using a neural network now the question is what do you mean by approximating okay let me write that

### 00:46:19 · Speaker 1

It's important as question

### 00:46:27 · Speaker 1

Waters

### 00:46:30 · Speaker 1

What is meant by

### 00:46:35 · Speaker 1

Approximating distributions using neural network neural networks

### 00:46:41 · Speaker 1

Approximating distributions

### 00:46:48 · Speaker 1

using your own devices

### 00:46:59 · Speaker 1

very important there are two ways here right see one way is that there is a there is a probabilistic way okay

### 00:47:12 · Speaker 1

And there is a deterministic way

### 00:47:23 · Speaker 1

Now what do you mean by a probabilistic way Let's say that there is a neural network here

### 00:47:30 · Speaker 1

Now this

### 00:47:32 · Speaker 1

This is the QV

### 00:47:35 · Speaker 1

or Z given X

### 00:47:46 · Speaker 1

Now this takes

### 00:47:48 · Speaker 1

sample of G as input okay so G

### 00:47:56 · Speaker 1

Neural networks are deterministic functions which is that you know you give a fixed input it will give you a fixed output always right. So now a sample of z sample of x sorry a sample of x it takes as an input and what it gives out are

### 00:48:17 · Speaker 1

Atomizers

### 00:48:24 · Speaker 1

a distribution

### 00:48:27 · Speaker 1

of z given x. So this is typically called as the probabilistic neural network where a neural network will give you the parameters of a distribution. Now typically let's say as an example

### 00:48:44 · Speaker 1

If Q of Z Q on X

### 00:48:48 · Speaker 1

is assumed to be let's say a Gaussian of some mean and variance

### 00:48:54 · Speaker 1

Okay this neural network will give you mean and variance as output

### 00:49:04 · Speaker 1

So this is called the probabilistic way of representing a distribution using a neural network. A neural network will give you the parameters of a distribution. So note that in most of the probabilistic ways of representation, you assume the underlying distributional form for the distribution that you are assuming. What you make your neural network output the parameters of the distribution.

### 00:49:34 · Speaker 1

Probabilistic way. Okay. There's a deterministic way which we have already seen, right, which is

### 00:49:47 · Speaker 1

because typically in latent variable models at least x will have a larger dimension compared to

### 00:50:01 · Speaker 1

Doesn't matter but yeah so just to ensure that it is consistent so if you are doing it in deterministic way let's say that you are modeling some

### 00:50:09 · Speaker 1

p theta of x given z right now it'll take a sample of

### 00:50:19 · Speaker 1

you a sample of Z okay it will give you what what will you give you what will a determination network give it will give you a sample

### 00:50:45 · Speaker 1

simply give you a sample okay x cap from p theta of x given z this is the deterministic curve so here the neural network is not giving you parameters of the distribution but it is giving the samples from the distributions example

### 00:51:03 · Speaker 1

Is a is a is a GAN generator no

### 00:51:08 · Speaker 1

A GAN generator is a deterministic neural network. I mean, all neural networks are deterministic that way, but a GAN generator is modeling the conditional data distribution in a deterministic sense. So what do I mean by that? I mean to say that it will give you a sample from the distribution that it is modeling, but not the parameters of it.

### 00:51:36 · Speaker 3

Sir but for a given z also let's uh this uh the sample x will be different right

### 00:51:44 · Speaker 1

No no no not in a in a in a in a GAN in a GAN right if you fix z it you'll always get the same x no because neural networks are deterministic functions

### 00:51:57 · Speaker 1

That's the whole point that I'm trying to make. See, the variability in the generated data comes because Z has randomness into it, right? Because we know that Z typically trampled from a content distribution. That's why different Z will give you different Xs. But post-training, a GAN's generator, or for that matter, any neural network is a fixed function, right?

### 00:52:21 · Speaker 1

Given fixed input it will give you a fixed output there is no stochasticity in a neural network by design

### 00:52:34 · Speaker 1

Does it make sense

### 00:52:36 · Speaker 2

So one question, so in the probabilistic way, so we estimate only the parameters for only one distribution or a family of or a group of distributions.

### 00:52:46 · Speaker 1

Yeah, see, it is one distribution in the sense that if we are looking at Q phi of z given x, right, Q phi of z given x is actually Q phi of z given one particular x always, isn't it?

### 00:53:04 · Speaker 1

This this mu and sigma will be a function of x

### 00:53:08 · Speaker 4

Okay

### 00:53:09 · Speaker 1

for a particular x. But if you are saying that you know the same neural network neural network is being used to estimate the Q phi of g given x for different values of x then you are estimating it for a family and that's what is happening.

### 00:53:25 · Speaker 1

Because once you try given one particular x it will give you the parameters of q phi of z given that particular x

### 00:53:36 · Speaker 1

Okay okay

### 00:53:38 · Speaker 2

It gener it generates a family itself right and

### 00:53:40 · Speaker 1

uh right i mean see uh for a given x it does not generate a family yes correct to be clear about it right when you say see there is no stochasticity associated with the neural network so for a fixed x it will give you a fixed output

### 00:53:55 · Speaker 1

In the probabilistic way what will happen is that there will be that that will be seen as parameters of impact. How do you do it practically is that suppose mu x is let's say that z is in some k dimensions right then what we will do is this output this neural network will have k plus k squared dimensional output now because sigma will have k squared parameters mu will have k parameters it will be k plus k squared

### 00:54:25 · Speaker 1

stacked into a long vector that is the output. So now for one x it will give you one output and that can be interpreted as the parameters of a distribution. So it is modeling a family in the sense that for every x it will give you parameters corresponding to that.

### 00:54:45 · Speaker 2

Got it

### 00:54:47 · Speaker 1

So I'll ask you a question now. What do you think, what way do you think, these are the only two ways that you model, that use neural networks in any task, okay? Here is a question. What do you think a classifier, a KA class classifier is doing? Is it a probabilistic model or a deterministic model?

### 00:55:18 · Speaker 2

Probably will distinct

### 00:55:21 · Speaker 1

Why do you think it's a probabilistic model

### 00:55:28 · Speaker 1

So what is the classifier model by the way what distribution is a classifier modeling take a classifier what distribution does it model you take an x as an input what is what distribution is it modeling

### 00:55:42 · Speaker 3

The line

### 00:55:43 · Speaker 2

giving the probability of the classes

### 00:55:48 · Speaker 1

This is what it models right

### 00:55:51 · Speaker 1

All classifiers model PT top by Gionx

### 00:56:03 · Speaker 1

the so-called cross entropy loss that you use is actually minimization of KL divergence no actually it's minimization of KL divergence between the true posterior label posterior okay and the neural network model posterior this is exactly what you do right when you minimize this is cross entropy because the other term which is the entropy term will be independent of theta the first term right which is expectation of log of

### 00:56:33 · Speaker 1

p theta of y given x with respect to p of y given x this is what you minimize negative of this is what you minimize which is the cross entropy term which is nothing but the k divergence right so even a classifier is doing the same thing that they are doing right it is doing a maximum likelihood estimation or minimizing the k divergence but now the output what do you get do you get a sample from this distribution or do you get the parameters of this distribution so let's say that y is

### 00:57:03 · Speaker 1

is a discrete distribution that will take one out of k values

### 00:57:08 · Speaker 1

Uh with

### 00:57:11 · Speaker 1

probabilities P y 1 to P y 2 up to P y k. So, post training when you do an inference for a particular x, what do you get at the output? Do you get a sample from the P theta y given x or do you get parameters of P theta y given x?

### 00:57:34 · Speaker 2

Get a sample

### 00:57:37 · Speaker 1

you say so do you get one of the case that depends okay okay so here is the answer right the way to look at it is so if you look at the entire classifier suppose you take the final layer to be the argmax of logs

### 00:57:55 · Speaker 1

Okay then it is a sample

### 00:57:59 · Speaker 1

But if you stop at logits

### 00:58:03 · Speaker 1

Then it's actually a distribution probabilistic way

### 00:58:10 · Speaker 1

You see that if you take the logits right then it's it sums to one right and it's all all non negative Okay, which is the softmax if you take the output of the softmax and which is the Logits no even before the softmax you take the logits then it's an entire distribution Okay, you can see that as you can interpret that as parameters if you take the argmax Okay, take the softmax and then take the argmax of all possible values then it becomes

### 00:58:40 · Speaker 1

a sample of this discrete distribution

### 00:58:43 · Speaker 1

Anyway so

### 00:58:46 · Speaker 1

Not something that I intended to say. But anyway, so these are two ways to model distribution, right? One is the probabilistic way where the neural network gives you samples from the distribution that it is modeling and the deterministic way where the neural network will give you samples from the distribution that it is modeling. Okay. Now, what do we do in a VAE?

### 00:59:13 · Speaker 1

few

### 00:59:17 · Speaker 1

Distribution Q phi of Z given X is modeled

### 00:59:29 · Speaker 1

There are multiple instantiations of it okay

### 00:59:42 · Speaker 1

modeled probabilistically

### 00:59:53 · Speaker 1

about realistic

### 01:00:00 · Speaker 1

And P chi top x given z

### 01:00:06 · Speaker 1

is modeled

### 01:00:12 · Speaker 1

using either probabilistic or deterministic you know as the case may be yeah I I tell you there are these are different instantiations of same idea right probabilistic or

### 01:00:24 · Speaker 1

So basically both of them are modeled. Q phi of z given x is always modeled probabilistically. Okay. P theta of z given x can be modeled probabilistically or in a deterministic way. Okay. Let us see one instantiation where you have

### 01:00:41 · Speaker 1

Okay so now data is a set of X i's

### 01:00:47 · Speaker 1

We have end of them

### 01:00:49 · Speaker 1

have sampled from BXU have right now typically X is in some RD

### 01:00:57 · Speaker 1

In all latent variable models Z is assumed to be in some R K okay where K is much less than D

### 01:01:07 · Speaker 1

is how it is done in the variable models now what will happen is there is a net neural network

### 01:01:28 · Speaker 1

This neural network takes xi as input one of the xi's as input and this is modeling q phi of z given xi

### 01:01:43 · Speaker 1

Now this is, as I said, it will model it probabilistically. So in one of the instantiations of, I mean, one of the naive implementations of VAE, now Q

### 01:01:57 · Speaker 1

P of Z given X

### 01:02:00 · Speaker 1

It is assumed to be a Gaussian

### 01:02:06 · Speaker 1

It's a distribution in Z the mean of this is mu

### 01:02:12 · Speaker 1

of x because it's a function of x the variance is a function of x

### 01:02:19 · Speaker 1

Typically it is assumed to be uh you can model it to be a diagonal matrix okay

### 01:02:27 · Speaker 1

diagonal matrix of uh

### 01:02:32 · Speaker 1

My one true secret

### 01:02:38 · Speaker 1

Let us call this as sigma of x sigma x vector okay

### 01:02:47 · Speaker 1

Now what will happen is that in a in a in a in a VAE this will get mu

### 01:02:56 · Speaker 1

of xi as the output

### 01:02:59 · Speaker 1

sigma of xi as the output okay now note that both

### 01:03:08 · Speaker 1

x and sigma x lie in k dimensional spaces right because i have assumed sigma x to be a diagonal matrix they both lie in k dimensional spaces that means that the the output of this you know this will be a

### 01:03:24 · Speaker 1

dimensions this will be

### 01:03:29 · Speaker 1

Two K dimensions

### 01:03:33 · Speaker 1

This is uh this is also called the the encoder network

### 01:03:43 · Speaker 1

simply modeling through P of G given X using neural networks but there is another neural network we said that we also model P theta

### 01:03:52 · Speaker 1

So this will take zi which is a sample from q phi of z given xi

### 01:04:01 · Speaker 1

input and then this is model p theta of x given z so now let's say that this gives you a sample

### 01:04:12 · Speaker 1

In this case I'm assuming that this is a model deterministical okay this network is also hold on

### 01:04:43 · Speaker 1

This will take zi the sample from qv of

### 01:04:49 · Speaker 1

given xi as an input okay and this this this network is also called the decoder network

### 01:05:01 · Speaker 1

This is a VAE. Okay. Now, one thing that is to be noted here is.

### 01:05:08 · Speaker 1

Of course this is k dimensional this will be d dimensional

### 01:05:13 · Speaker 1

Now see one thing that has to be noted here as I tell you

### 01:05:19 · Speaker 1

There is no

### 01:05:26 · Speaker 1

Connection

### 01:05:34 · Speaker 1

Between the

### 01:05:40 · Speaker 1

Incorporate decoder networks

### 01:05:45 · Speaker 1

they are not connected at all right so what is happening is given an xi

### 01:05:51 · Speaker 1

So you first get the uh the parameters of the distribution Q phi of z on x

### 01:05:58 · Speaker 1

Having those parameters you sample a gi from qp of z given x okay and give that gi as an input to the decoder to get a sample from p theta of x given z.

### 01:06:12 · Speaker 1

Here the output of the encoder right does not go as an input to the decoder

### 01:06:19 · Speaker 1

You see that?

### 01:06:22 · Speaker 1

The output of the encoder does not go as an input to the decoder. I should write that. So this means that the output

### 01:06:33 · Speaker 1

be encoded

### 01:06:46 · Speaker 1

Who has

### 01:06:49 · Speaker 1

Input

### 01:06:53 · Speaker 1

decoder

### 01:07:00 · Speaker 1

Uh is this setup clear now what is happening

### 01:07:05 · Speaker 1

We'll have to now see how to train this or rather how to get the parameters by optimizing the elbow and also we have to see how to do generation and inference later post I mean because you remember no we had these three goals that you learn a latent variable model enable generation and enable posterior inference we'll see all that to be done but in terms of like architecture is all of you clear on what is happening

### 01:07:31 · Speaker 2

So the input to the decoder is a sample from Q of

### 01:07:36 · Speaker 2

Uh give an example

### 01:07:36 · Speaker 1

of ZG on extract

### 01:07:40 · Speaker 2

So we indirectly use it right because uh

### 01:07:42 · Speaker 1

Oh we go

### 01:07:42 · Speaker 2

The distribution

### 01:07:43 · Speaker 1

I'm not saying we don't use the encoder network I'm saying that the output of the encoder does not go as an input to the decoder

### 01:07:53 · Speaker 1

I didn't say that we are not using the encoder encoder is very much used

### 01:07:58 · Speaker 2

but it's used to only determine the parameters of the distribution and then we sample

### 01:08:03 · Speaker 1

It is using the parameters of the distribution and using those parameters you sample okay and once you sample use that sample as an input to the decoder

### 01:08:19 · Speaker 3

So I have one question

### 01:08:21 · Speaker 1

Yeah go on

### 01:08:22 · Speaker 3

for q p z of x we say that is a normal distribution on the variable z with mean mu x and sigma variance sigma x so while this mu mean and variance are on the or on x they should be on z right

### 01:08:41 · Speaker 1

Ah no no no they are see they are okay I mean that they are functions of x see look at this now I have said that both of them lie in Rk which means that they are in these space but they are functions of x

### 01:08:54 · Speaker 1

See when I write off something it means that there are functions

### 01:08:54 · Speaker 3

The pot

### 01:08:58 · Speaker 1

I'm talking about them being function subjects

### 01:09:02 · Speaker 3

Okay but they are uh but they are over the Z since yeah

### 01:09:07 · Speaker 1

I'll look at that

### 01:09:07 · Speaker 3

The damage

### 01:09:09 · Speaker 1

Absolutely absolutely

### 01:09:12 · Speaker 1

See a neural network is taking an xi as an input no that they're that's why it's a function of x

### 01:09:19 · Speaker 3

part itself

### 01:09:22 · Speaker 1

So I mean I want all of you to like strictly understand this and clearly understand what's happening otherwise everything that we do next will not make sense. So please ask me questions if you have on how this thing works. I mean architecture.

### 01:09:37 · Speaker 2

K is again a hyperparameter here or

### 01:09:41 · Speaker 1

Page I have a parameter yes

### 01:09:45 · Speaker 4

Sorry one query here the decoder network we have found out deterministically

### 01:09:53 · Speaker 1

Uh see we are just yeah yeah we have at least in this uh exam instantiation I have made this uh deterministic because I say that it gives you a sample from p data of x m c yeah

### 01:10:05 · Speaker 4

Does it maybe you might cover it later you can say that I mean like whether it changes when you

### 01:10:11 · Speaker 2

it probabilistically

### 01:10:14 · Speaker 1

Yeah, you simply get the parameters of p theta of x given z. No, that's all. Instead of getting a sample from p theta of x given z, you get parameters of p theta of x given z. Then it becomes a probabilistic thing.

### 01:10:27 · Speaker 4

Got it then again from that parameter we again uh use that

### 01:10:32 · Speaker 1

Yeah you do sampling but typically right in a in a naive implementation of VAE the output of the decoder itself is taken as a sample from p theta of x given z

### 01:10:45 · Speaker 1

But yeah, so later like in the class, no, I will also give you one example where it is taken deterministically as well. But for now, let us think that it is, I mean, sorry, the probabilistic, but for now, let us think that it is deterministic.

### 01:10:59 · Speaker 2

Sure thanks

### 01:11:01 · Speaker 1

Okay

### 01:11:03 · Speaker 2

Yeah, sir, so for a given xi, the xi cap which we get from p theta might be different, right? Because we have a sampling step in between and that might lead to a different z i.

### 01:11:18 · Speaker 1

I am not even saying that you get uh like xi at the output of the decoder right decoder will just give you a sample from p theta which you know I have not established any relationship between xi and xi cap yet

### 01:11:32 · Speaker 1

Okay, if your question is, you know, why, where is that so-called quote unquote auto encoding happening here, right? We will see that. We will see how to, how does it come out, okay?

### 01:11:47 · Speaker 4

So this sampling process of lid uh from q of e right so is it like generally uh having a random sample using like like a random function

### 01:11:57 · Speaker 3

Yes

### 01:11:58 · Speaker 1

Yeah yeah you use the standard samplers so you can suppose if you model your q to be a Gaussian distribution then you can use that like standard random sampler for this

### 01:12:14 · Speaker 1

Okay so is the setup clear to all of you now what we should do is like with this

### 01:12:25 · Speaker 1

this now the elbow will become a function of

### 01:12:31 · Speaker 1

Yeah theta and phi which is given by the expectation of log of e theta of x given z and this is with respect to q phi of z given x minus the k-l divergence between

### 01:12:51 · Speaker 1

View view view next

### 01:12:56 · Speaker 1

okay this is what it is what we should do is that

### 01:13:03 · Speaker 1

You should solve this I don't theta star and V star

### 01:13:11 · Speaker 1

simply the

### 01:13:20 · Speaker 1

what we need right we need to train both of these neural networks so how do we do that we do it using gradient descent right so we need

### 01:13:30 · Speaker 1

the gradient of

### 01:13:33 · Speaker 1

Elbow

### 01:13:36 · Speaker 1

respect to phi and unit gradient of

### 01:13:41 · Speaker 1

the elbow with respect to theta this is what we need right because finally what we do is this is how we train the neural networks

### 01:14:08 · Speaker 1

assuming that we are simply doing a SGD rate first order gradient descent

### 01:14:17 · Speaker 1

Here's how we do it so we need the gradients of the elbow with respect to both phi and theta under this

### 01:14:25 · Speaker 1

I think somehow the pages are sizes are going heavier

### 01:14:36 · Speaker 1

I should not zoom out and zoom in arbitrarily, I think. Yeah. Let us keep it this way. Okay. So now with this modeling choice that we have made, no, we have to ensure that we get the gradients of the lower bound with respect to phi and with respect to theta. Okay. And then we can, of course, use gradient design tool to train both of these networks. Is this all right? Now, what we will do in the rest of the classes. So getting this gradient right with respect to gradient of the elbow with respect to

### 01:15:06 · Speaker 1

is a non-trivial thing and you might have heard this term reparameterization right it is used in VAE like so-called reparameterization that comes into picture to calculate this gradient itself so calculating this gradient with respect to calculating the gradient of LBO with respect to the encoder parameters needs this idea called reparameterization because of a simple fact look at this no

### 01:15:31 · Speaker 1

the there is a sampling step that is involved okay which cannot be differentiated so i i will show all that you know very rigorously but the basic idea is that there is a sampling step and the encoders encoder and decoder are connected via the sampling step but sampling is a non-differentiable operation and you back propagate no through chain rule you have to back propagate let's say that you start from the output of the decoder back propagate all the way through the input of the decoder from there

### 01:16:01 · Speaker 1

should go to the output of the encoder and those two are connected via sampling. But sampling is a non-differentiable operation. So what do you do to find the the gradient of the ELBO with respect to the encoder parameters is what we should look at next. That is done through this trick called reparameterization trick that I will discuss.

### 01:16:22 · Speaker 1

Okay, so I think shall we take a break, 15 minutes break.

### 01:16:27 · Speaker 1

10 40 10 48 now

### 01:16:31 · Speaker 1

A good time to stop yeah

### 01:16:37 · Speaker 1

Oh my mistake okay yeah shall we take a break

### 01:16:43 · Speaker 1

Uh Satya go ahead

### 01:16:46 · Speaker 4

Uh yes I can they can take a break I own question on the assignment

### 01:16:53 · Speaker 1

maybe later after the class yeah please do ask me after the class okay so now uh yeah it is 10 49 in my clock we started uh late today no 20 minutes late so let's cut down the break let's get back at 11 5 okay in 15 minutes let's come back let's come back at 11 5 and uh finish the report from my parameters so don't miss the next part of the class no it's pretty important okay see you in 15 minutes then bye

### 01:35:26 · Speaker 1

Shall we continue

### 01:36:04 · Speaker 1

Okay

### 01:36:10 · Speaker 1

So uh Sylvia Minnow right

### 01:36:19 · Speaker 1

Can you hear me

### 01:36:22 · Speaker 1

Okay, nice. Okay, so we were looking at now computing the gradients of the encoder and the decoder parameters with respect to, sorry, computing the gradients of elbow with respect to the encoder and decoder parameters. Okay, now, okay, so what do we, so let's take one term at a time, you know, there are two terms in elbow. So consider.

### 01:36:51 · Speaker 1

um computing

### 01:37:06 · Speaker 1

computing the

### 01:37:12 · Speaker 1

Radiance

### 01:37:17 · Speaker 1

I'll go

### 01:37:28 · Speaker 1

Respect to P and Q

### 01:37:44 · Speaker 1

You consider the first term in the elbow consider

### 01:37:49 · Speaker 1

If first turn available

### 01:38:02 · Speaker 1

which is the expectation of

### 01:38:06 · Speaker 1

Log

### 01:38:08 · Speaker 1

Each top x given z

### 01:38:14 · Speaker 1

with respect to

### 01:38:16 · Speaker 1

The obvious hit and it's okay

### 01:38:21 · Speaker 1

Now

### 01:38:45 · Speaker 1

does it look like suppose um look something like this no this table

### 01:39:04 · Speaker 1

you have an expectation of

### 01:39:07 · Speaker 1

some function

### 01:39:11 · Speaker 1

Please note that this z you know what is this z here x given z what is this z the z

### 01:39:21 · Speaker 1

Z is being sampled from Q phi of z given x right

### 01:39:27 · Speaker 1

Right? So this entire thing, whatever the log of p theta of x given z is log, that is also a function of p.

### 01:39:40 · Speaker 1

understand that please let me know if you don't understand so this is of some random variable v okay and the expectation is with respect to a distribution

### 01:39:53 · Speaker 1

a PV and this is also a function of P

### 01:40:00 · Speaker 1

So just giving you a simpler example

### 01:40:08 · Speaker 1

with us

### 01:40:16 · Speaker 1

Let me use a different parameter maybe let's call this as some psi and we have some distribution

### 01:40:25 · Speaker 1

This random variable, do you agree that it looks like this? Any questions on this?

### 01:40:35 · Speaker 1

okay let me write it on me it'll be easier that way

### 01:40:44 · Speaker 1

The up-side of V is actually

### 01:40:48 · Speaker 1

Naga

### 01:40:50 · Speaker 1

theta of x given z okay and then p psi of v is simply

### 01:41:02 · Speaker 1

You know next

### 01:41:04 · Speaker 1

V Z okay and Psi is

### 01:41:11 · Speaker 1

Is this okay

### 01:41:21 · Speaker 1

Hello I'm Audible

### 01:41:26 · Speaker 1

Fine so now what do we need is that we need the gradients of this expectation

### 01:41:43 · Speaker 1

This gradient has to be with respect to the parameter size correct

### 01:41:48 · Speaker 1

is what we are seeking now let us write this down so this is equal to

### 01:41:52 · Speaker 3

Sir, sorry to interrupt. Instead of going for psi, can't we straight away use the like, like phi? Otherwise it will be, it will be a bit confusion.

### 01:42:04 · Speaker 1

A the reason I didn't use phi was you know phi has been taken as encoder parameters I can do that

### 01:42:15 · Speaker 1

Let us keep it that way no I have written it down so let us have it that way

### 01:42:20 · Speaker 1

This is equal to

### 01:42:24 · Speaker 1

Mm

### 01:42:26 · Speaker 1

RTN

### 01:42:32 · Speaker 1

of integral

### 01:42:36 · Speaker 1

respect to v we have p psi of v times

### 01:42:42 · Speaker 1

psi of v dv right this is definition of expectation and we can move the gradient inside because expectation is a linear operator right we can move the gradient inside this will be p psi of v times

### 01:43:01 · Speaker 1

So you'll be correct

### 01:43:06 · Speaker 1

Now what do we do now next Can somebody tell me

### 01:43:21 · Speaker 1

use staying rule this is

### 01:43:32 · Speaker 1

The idea go

### 01:43:35 · Speaker 1

uh the gradient of

### 01:43:38 · Speaker 1

one function

### 01:43:41 · Speaker 1

James

### 01:43:44 · Speaker 1

psi of v dv

### 01:43:48 · Speaker 1

Plus

### 01:43:54 · Speaker 1

The gradient of

### 01:43:56 · Speaker 1

the other function

### 01:44:17 · Speaker 1

what it is right now what is the first

### 01:44:23 · Speaker 1

Look at the first term right you have

### 01:44:26 · Speaker 1

some function here and the probability distribution here what is that and there's an integral what is that this is an expectation of

### 01:44:36 · Speaker 1

gradient

### 01:44:41 · Speaker 1

respect to psi of v

### 01:44:47 · Speaker 1

This is not an expectation

### 01:44:50 · Speaker 1

This the first term now can be approximated using one over n

### 01:44:59 · Speaker 1

one through n and you have

### 01:45:02 · Speaker 1

of vi where vi is coming from p psi of v right this is again lot of last numbers we know how to estimate expectations approximate expectations but this

### 01:45:17 · Speaker 1

return

### 01:45:23 · Speaker 1

as an expectation

### 01:45:28 · Speaker 1

And therefore therefore

### 01:45:36 · Speaker 1

and we compute it

### 01:45:48 · Speaker 1

You see this? See, this is the problem. See, when I said that you cannot differentiate through sampling, so look at what is happening. See, there is an expectation of a certain function and that function is parameterized by some set of parameters, right? Now, the expectation is with respect to a density, okay? And that density is also parameterized by same set of parameters.

### 01:46:13 · Speaker 1

So now if you want to do that, if you want to now take the gradient of such an expectation of a function that is, see typically what happens now in most of a neural network training, you need to take the derivative of an expectation of a function with respect to set of parameters and these will be neural network parameters. But this expectation will be typically over let's say px, where px are simply the distribution of data which has nothing to do with

### 01:46:43 · Speaker 1

model parameters and then we approximate this expectation with respect to I mean using the samples that we are given which are the true data. Now here is a case okay where you need to take the gradient of an expectation okay with respect to our density function and that density function

### 01:47:02 · Speaker 1

is also parameterized by the same set of parameters with respect to which we need the gradients.

### 01:47:08 · Speaker 1

see that and why is that happening if you look at it that is happening because our encoder network is made probabilistic you know when we make our encoder network probabilistic okay then the the parameters that we are getting know of the expectation of of the distribution with respect to which we are taking the expectation uh is uh that the distribution also is parameterized by same set of parameters with respect to which we need the uh

### 01:47:38 · Speaker 1

the the derivatives

### 01:47:43 · Speaker 1

Algebraically speaking, what happens is that if you take the gradient, you cannot express the second term that comes up in the gradient of the expectation in terms of sample averages. And therefore, that cannot be computed. Is this point clear to all of you?

### 01:48:04 · Speaker 1

This implies so if you want to generalize this implies

### 01:48:08 · Speaker 1

the gradient of the first term in elbow which is the expectation of log of heat heat of x given z with respect to

### 01:48:19 · Speaker 1

Q V of Z Unix okay

### 01:48:22 · Speaker 1

This can't be

### 01:48:25 · Speaker 1

Muted

### 01:48:35 · Speaker 1

Can't be computed directly is what it means.

### 01:48:42 · Speaker 1

Can you all appreciate this fact

### 01:48:51 · Speaker 1

Any questions on this? See this is the key part okay this is what this is where we need uh what is what what we call as the reparameterization that we will see but is this clear?

### 01:49:06 · Speaker 1

Any questions on this

### 01:49:17 · Speaker 1

Am I already

### 01:49:25 · Speaker 1

questions great now what do we how do we solve this solution

### 01:49:39 · Speaker 1

as the reparameterization trick

### 01:49:51 · Speaker 1

Okay, now what does this mean? Recall that we had

### 01:49:57 · Speaker 1

We wanted the gradient of

### 01:50:06 · Speaker 1

expectation of some function of some function that is parameterized by some parameters and the distribution was also parameterized by the same set of parameters right we wanted this now all we need to do is

### 01:50:22 · Speaker 1

It wouldn't be computed

### 01:50:31 · Speaker 1

Correct. So what you do what you do is

### 01:50:37 · Speaker 1

or express express

### 01:50:47 · Speaker 1

Dumps up

### 01:50:49 · Speaker 1

Another distribution

### 01:50:57 · Speaker 1

distribution which is

### 01:51:02 · Speaker 1

Independent of

### 01:51:10 · Speaker 1

Exactly what is called as the reparameterization okay I'll tell you the parameterize

### 01:51:22 · Speaker 1

So what does this mean? This means that let's say that

### 01:51:33 · Speaker 1

Suppose

### 01:51:37 · Speaker 1

there exists

### 01:51:40 · Speaker 1

A random variable

### 01:51:44 · Speaker 1

epsilon okay it's some distribution p epsilon okay so note that this is independent of

### 01:51:53 · Speaker 1

ID parameters

### 01:51:55 · Speaker 1

Such that such that your v, which is the random variable of interest,

### 01:52:03 · Speaker 1

some function of this epsilon

### 01:52:08 · Speaker 1

Then then

### 01:52:13 · Speaker 1

the expectation of

### 01:52:19 · Speaker 1

respect to

### 01:52:24 · Speaker 1

E psi of V can be shown to be equal to the expectation of

### 01:52:30 · Speaker 1

F psi of what is V now V is equal to G times epsilon

### 01:52:39 · Speaker 1

And this expectation now will become the expectation with respect to PFSR. It is either you take it as a homework or it can be taken in the DS session just to show that these two are equivalent. Okay. It is also called the law of the unconscious statistician. Okay. Abbreviated as LOTUS. I mean, this is a standard probability proof. You can just do it. Two steps, you can show that. So now what did we show? That

### 01:53:09 · Speaker 1

There is this random variable V right with respect to which we are taking an expectation. Now we represented that random variable okay in terms of another random variable epsilon.

### 01:53:22 · Speaker 1

a function of another random variable epsilon that is independent of these parameters uh psi

### 01:53:31 · Speaker 1

And if you do that, then the expectation of the function with respect to this random variable p psi now will become an expectation with respect to another random variable p epsilon that is independent of the parameter psi.

### 01:53:52 · Speaker 1

So this is what is called as reparametrization right I mean this g function is called the reparametrization function

### 01:54:08 · Speaker 2

How do you find this epsilon

### 01:54:11 · Speaker 1

good question now that depends upon uh like in the vae paper no they give multiple ways to find this epsilon and g it's not enough if you only find epsilon you need to find g also you need to find an epsilon and a g such that this happens i'll give you examples of how to do this okay at least in the in the case of uh like the naive implementation of vae i'll tell you how this is done okay so now this if you do this now it's easy right so now um

### 01:54:42 · Speaker 1

If we solve the problem the problem was to find the gradient of this

### 01:54:49 · Speaker 1

expectation

### 01:54:53 · Speaker 1

respect to psi now this is equal to the gradient of the expectation of

### 01:55:07 · Speaker 1

This can be done. You just now push the expectation inside the gradient inside the expectation and that can be computed using sample averages. So now this is approximately equal to take some m samples of epsilon and this are equal to 1 to m and you have the gradient of

### 01:55:28 · Speaker 1

F psi of G of epsilon i

### 01:55:35 · Speaker 1

your epsilon i you know is sample from p epsilon so now you will not have that uh have this uh in uncomputable integral problem now because the dependency the expectation is not now with respect to uh p psi but it is with respect to p epsilon

### 01:55:57 · Speaker 1

Now let us look at the let us look at an example of reparameterization somebody asked me how to do that so example of

### 01:56:15 · Speaker 1

Mm

### 01:56:23 · Speaker 1

is spelling correct T bar I mean the reservation right here

### 01:56:31 · Speaker 1

You know what about me

### 01:56:35 · Speaker 1

right okay in v a in particularly in v a e okay i mean this reparameterization is independent of v a or nothing it's a general probability uh probabilistic technique okay but yeah i'll show you an example of v a e okay let us take the same example where my q phi

### 01:56:58 · Speaker 1

of zero on X

### 01:57:03 · Speaker 1

u p of z d on x okay is a Gaussian distribution

### 01:57:09 · Speaker 1

and it has parameters let's say mu of x and sigma of x okay

### 01:57:20 · Speaker 1

is what it is now let us now reparameterization okay so now uh what is phi by the way i'll tell you

### 01:57:28 · Speaker 1

Mistake in the writing as well

### 01:57:31 · Speaker 1

that this mu is a function of phi because this is the output of the neural network sigma is also a function of parameterized by phi a function of x okay now that is why this becomes a function of p now let us reparameterize now let let epsilon be a gaussian distribution with zero mean and unit variance

### 01:57:54 · Speaker 1

Okay if you do that then then

### 01:58:03 · Speaker 1

Let Z is equal to

### 01:58:07 · Speaker 1

mu phi of x plus

### 01:58:17 · Speaker 1

times epsilon if I do this

### 01:58:21 · Speaker 1

do this then Z will now have

### 01:58:27 · Speaker 1

distribution equal to z given x

### 01:58:32 · Speaker 1

Now this function right is the g function that I'm talking about this is g of epsilon

### 01:58:38 · Speaker 1

If you take a a a normally distributed random variable with zero mean and unit variance

### 01:58:47 · Speaker 1

Excuse me. So you add it with a constant and scale it with a constant. If you do that, then the output random variable will again be Gaussian, okay, with the mean and variance given by the scale and the shift.

### 01:59:03 · Speaker 1

This is a reparameterization

### 01:59:07 · Speaker 1

You see that

### 01:59:17 · Speaker 1

Is this alright

### 01:59:19 · Speaker 1

We have this g function

### 01:59:24 · Speaker 1

is simply mu

### 01:59:27 · Speaker 1

Uh

### 01:59:38 · Speaker 1

This is one way. There is another way to reparameterize which is not often used in VAE literature, but there is one other way to reparameterize which is called as, this is one example.

### 01:59:54 · Speaker 1

The other example that is given in that paper is what is called as the inverse CDF method. We will not use inverse CDF method, but I am simply

### 02:00:08 · Speaker 1

engineered it for the sake of completeness. See suppose

### 02:00:16 · Speaker 1

Oh X is a random variable

### 02:00:21 · Speaker 1

F x of x

### 02:00:26 · Speaker 1

notes it's CDF

### 02:00:33 · Speaker 1

Well we know that

### 02:00:36 · Speaker 1

If x of x is simply

### 02:00:40 · Speaker 1

The integral of the

### 02:00:43 · Speaker 1

function right over this. Now let us call that represent that by some random variable z.

### 02:00:51 · Speaker 1

No this is a function of the question is question is

### 02:00:59 · Speaker 1

What does this mean

### 02:01:04 · Speaker 1

distribution

### 02:01:11 · Speaker 1

You understand the question? Now given a random variable you compute its CDF

### 02:01:17 · Speaker 1

Now CDF itself becomes another random variable

### 02:01:23 · Speaker 1

Question that we are asking is what will be the distribution of CDF of a random variable? Do you know that?

### 02:01:30 · Speaker 1

Does anyone know that?

### 02:01:38 · Speaker 1

It would be a uniform distribution

### 02:01:45 · Speaker 1

between zero and one

### 02:01:53 · Speaker 1

you so please take it as a small homework and show this that you take any random variable okay and show that the distribution of its cdf of any random variable is uniform between 0 and 1 can you already intuitively see why that should be the case if you take the cdf now cdf is a non-decreasing function right and it is upper bounded by 1 so which mean i upper it is bounded between 0 and 1 right

### 02:02:23 · Speaker 1

the CDF so that should be a uniform distribution between 0 and 1 just I mean this is a standard proof okay so so please find it out in the internet or just do it as a homework okay now the thing is this implies this implies that if I take a u that is uniform between 0 and 1 okay and compute x to be equal to the inverse okay of the CDF that is evaluated at u

### 02:02:52 · Speaker 1

Ten ten

### 02:02:55 · Speaker 1

Maybe

### 02:02:58 · Speaker 1

Distribution of X

### 02:03:02 · Speaker 1

Let us call this as x cap x cap is inverse cdf of a random variable x then the distribution of x cap

### 02:03:19 · Speaker 1

It's same

### 02:03:28 · Speaker 1

And the dog

### 02:03:32 · Speaker 1

is the idea. Makes sense right? See now we know that the distribution of the CDF of any random variable is uniform.

### 02:03:43 · Speaker 1

Now that means that if you take a uniform random variable between 0 and 1, okay, and make a transformation, okay, using the inverse of the CDF of any random variable, then the, then the, the, uh, the outcome will be another random variable which would have a distribution that is same as that random variable whose CDF you have inverted.

### 02:04:09 · Speaker 1

Now in this case in this case

### 02:04:17 · Speaker 1

g functions for now epsilon

### 02:04:21 · Speaker 1

Epson is uniform zero one

### 02:04:28 · Speaker 1

And the g function okay says the inverse

### 02:04:34 · Speaker 1

the CDF. So this is another reparametrization technique which is called the inverse CDF method.

### 02:04:41 · Speaker 1

is all right see but the thing is in this case no the only requirement is that the cdf of the func of the distribution that you are modeling using your encoder has to be invertible

### 02:04:54 · Speaker 1

which is not always the case and that's why you know more in most of the cases uh in VAs the distribution of Q is taken to be Gaussian and this sort of reparameterization is used you know which is the affine reparameterization is used not the inverse ADF method. But I hope that you got the idea behind reparameterization right. Let me repeat what is happening here. So we wanted to find the gradient of the encoder parameter uh with respect to

### 02:05:24 · Speaker 1

elbow right sorry we wanted to find the gradient of the elbow with respect to the encoder parameters that cannot be found out because the the elbow has an expectation of some function with respect to a distribution and that distribution itself happens to be a function of these parameters

### 02:05:44 · Speaker 1

So we cannot compute the gradients. So what do we do about it? The way to do it is represent that distribution with respect to which you are taking the expectation in terms of another arbitrary random variable which is independent of the parameters. So that representation through a function is what is called as reparameterization. If you do that, then this expectation can be written in terms of an expectation over that arbitrary random variable and therefore the gradients of

### 02:06:14 · Speaker 1

this function with respect to the encoder parameters can be found out so that is the idea and we saw two ways to do reparameterization which is that if you assume your qp to be normally distributed there's a certain mean and variance the way to reparameterize that is start with a Gaussian random variable which has zero mean and unit variance and scale it with the the sigma and shift it with the mu you will get another random variable whose mean and variance

### 02:06:44 · Speaker 1

This is what the Wiener variance of Q pi Q pi is

### 02:06:49 · Speaker 1

Any questions so far

### 02:06:52 · Speaker 1

Now we will use this to compute the gradients and then back propagate. But yeah, if you have any questions here, please ask me. This is actually one of the

### 02:07:02 · Speaker 1

idea of VAEs because otherwise it's simple right you are like maximizing the likelihood representing the distributions using neural network and back propagating but what's important is once you represent a distribution using a neural network in a probabilistic sense you have to get to reparameterization otherwise you cannot compute the gradients that is the idea

### 02:07:29 · Speaker 1

Uh once I don't think

### 02:07:31 · Speaker 2

So are we saying that we are transforming the distribution that we get to either a standard normal or a uniform in this case? Is that the way to see it or?

### 02:07:42 · Speaker 1

other way around no we are representing the output the distribution of the encoder okay our distribution that is being modeled by the encoder in terms of standards normal zero

### 02:07:56 · Speaker 2

Okay and and the transformation I mean is the g function basically right

### 02:08:01 · Speaker 1

Transformation is a g function and that's it that's that that is a user defined function no it is nothing to do with it you're not learning it or anything it is just a user defined thing

### 02:08:10 · Speaker 2

And is that also the way we say that okay uh that random sampling process we eliminate and then we introduce some kind of uh a determinism here

### 02:08:18 · Speaker 1

No there is still sampling is happening in epsilon mc we are just re-representing that in terms of some other random variable

### 02:08:24 · Speaker 2

Okay

### 02:08:27 · Speaker 1

which is which is which is not a function of the see it is only to do a simple thing all we need to do is express this expectation that is there in elbow with respect to a distribution of a random variable which is independent of the parameters that's all that's all we want to do

### 02:08:45 · Speaker 2

Okay so so uh sampling this way uh still allows us the to flow the gradient backwards

### 02:08:51 · Speaker 1

I will show you how to do that. See now, I mean algebraically you are convinced that now we can express this expectation now, right?

### 02:09:02 · Speaker 1

Typically the the the distribution which is uh which you are sampling from is not now dependent on uh phi it is you you got it no

### 02:09:14 · Speaker 1

Yeah that is the basic idea any other question

### 02:09:22 · Speaker 1

So now let us write what is happening. So now what happens is that you have the encoder network.

### 02:09:36 · Speaker 1

the encoder network okay this is not

### 02:09:42 · Speaker 1

to take it as

### 02:09:44 · Speaker 1

Yeah Karthik go on you had a question

### 02:09:54 · Speaker 1

goes as an input and this is modeling q by of z un x okay now what happens here is this neural network gives you uh mu and sigma so what you do is sample epsilon from normal 0 1

### 02:10:12 · Speaker 1

let's call this as psi so given a particular sample you take an epsilon from normal zero one and then do z get your zi

### 02:10:33 · Speaker 1

pretty much the same

### 02:10:36 · Speaker 1

Uh sigma p sigma p of x

### 02:10:41 · Speaker 1

We got this Zi correct now take that Zi

### 02:10:47 · Speaker 1

Pass it through the decoder

### 02:10:53 · Speaker 1

Did I say yeah

### 02:10:58 · Speaker 1

This is what is happening. You understood now? So do you see the difference between these two? Here, yeah, just zoom it here. So here what we are doing is that we started from xi, got a mu and sigma, sampled from sample gi using that mu and sigma directly from qf and then gave that gi. Here when we reparameterize, what did we do? We got mu and sigma, okay. Sampled an epsilon from an arbitrary design from

### 02:11:28 · Speaker 1

standard normal 0 1 and then got gi by reparameterizing

### 02:11:33 · Speaker 1

Is it alright

### 02:11:37 · Speaker 1

You know the difference now after re before and after reparameterization

### 02:11:43 · Speaker 1

I hope that you got it so now what do we have to do is we need to compute the gradient of

### 02:11:52 · Speaker 1

the expectation of

### 02:11:55 · Speaker 1

Nah but

### 02:11:57 · Speaker 1

Meet you at the

### 02:11:59 · Speaker 1

Q and Z with respect to Q V of Z given X correct

### 02:12:05 · Speaker 1

Now this is equal to the gradient of

### 02:12:11 · Speaker 1

Application of log of

### 02:12:14 · Speaker 1

readed off

### 02:12:16 · Speaker 1

X okay given what is Z now

### 02:12:24 · Speaker 1

Z is given by this particular z of yeah this particular formula let me call this as uh

### 02:12:34 · Speaker 1

Do you have a question

### 02:12:38 · Speaker 1

It is a bit of a spectacle

### 02:12:43 · Speaker 1

Is that alright

### 02:12:49 · Speaker 1

Strictly speaking now this g function is a function of phi now because look at this right I mean it has mu phi and sigma phi here it's parameterized by phi.

### 02:13:01 · Speaker 1

The question is we got rid of the dependency on p right this expectation now can be is equal to 1 over

### 02:13:14 · Speaker 1

the sample m samples of epsilon right then this is equal to j to m and we have

### 02:13:22 · Speaker 1

log of p theta of xp one

### 02:13:29 · Speaker 1

D C O

### 02:13:32 · Speaker 1

Epsilon G

### 02:13:36 · Speaker 1

Please note that for a particular xi for a given xi we can get m number of z i's see that

### 02:13:48 · Speaker 1

Or

### 02:13:50 · Speaker 1

One x sorry okay

### 02:13:57 · Speaker 1

ZI's can be obtained

### 02:14:09 · Speaker 1

Do you understand that

### 02:14:12 · Speaker 1

Because we are doing sampling right like outside of the encoder since we are doing sampling we can sample for one xi we can sample multiple gi's but typically I mean what is done in implementing vi is that they keep capital M to be 1 that means that they only do one sampling and send it across okay which means that the sum will only be on one particular sample. Hope that it is okay. Now the next question is that how to compute

### 02:14:46 · Speaker 1

to compute log of

### 02:14:54 · Speaker 3

So here we are doing it in a probabilistic approach right for the encoder

### 02:15:02 · Speaker 1

Encoder is always probabilistic

### 02:15:06 · Speaker 1

xi will give you mu and sigma once you get your mu and sigma you sample epsilon from let's call this yeah epsilon from epsilon j let's call it you sample epsilon from normal 0 1 and then they reparameterize and get m uh z j's

### 02:15:24 · Speaker 1

But there is

### 02:15:24 · Speaker 3

So there is some like so if we write it like this so there is some linear translation happening between the output of encoder and the input of decoder

### 02:15:37 · Speaker 1

yeah input of the yeah that is the reparameterization no in this particular case that is what i am saying if you assume your q to be normal mu sigma then this reparameterization is adaptable

### 02:15:50 · Speaker 1

There is no rule why this is the only way to reparameterize, no. That's what I'm saying. Suppose you assume your to be some other distribution. You just have to find an epsilon and g such that it transforms. See, what is important is that now this gradient, right? The gradient that we are computing here, this will become, this expectation will become independent of phi. That's all we need.

### 02:16:14 · Speaker 1

And for that we do reparameterization. Now what sort of reparameterization you do is a design choice. That depends upon what form do you assume on QP and what what epsilon will just transform what epsilon and G combination will transform that into this is the question. That's all. That depends upon whatever you use.

### 02:16:35 · Speaker 3

Okay sir

### 02:16:37 · Speaker 1

Is that all right

### 02:16:40 · Speaker 1

Okay. Uh yeah Sarvesh, do you have a question?

### 02:16:45 · Speaker 2

So in the last step one by m so there should be a gradient inside right

### 02:16:51 · Speaker 1

as a gradient here so this will be

### 02:17:03 · Speaker 1

Go on

### 02:17:04 · Speaker 2

So can you just repeat why that m can be taken as just one here

### 02:17:09 · Speaker 1

it's that it's like you're approximating this expectation by a single sample estimate that's all it can be anything uh people take it as one and also experiment i mean in your assignment i'll ask you to experiment with different values of m okay but yeah so generally i mean like in the naive most naive implementation you just take one sample of z or one sample of x but it is not uh i mean it's not a hard and fast right i mean you can make your m to be hyper

### 02:17:39 · Speaker 1

I'll put it on and play with it yeah

### 02:17:41 · Speaker 2

Because I think in this equation we say that it is an expectation so we we are free to choose the value of m here right and because

### 02:17:48 · Speaker 1

And also single sample estimate is not a good way to do it yeah always

### 02:17:57 · Speaker 1

Yeah

### 02:17:59 · Speaker 3

Sir I didn't follow on this part sir can you please explain once again

### 02:18:04 · Speaker 1

But see here you sample for one xi goes as an input to the encoder right you get a mu and sigma. Now with that mu and sigma you can sample any number of zis no for a particular xi.

### 02:18:21 · Speaker 1

Huh

### 02:18:21 · Speaker 3

So that is what the choice of them

### 02:18:24 · Speaker 1

that is what I have represented as capital M so you sample like multiple samples from so it's like for let's say X i is an image you know for a given image for one particular image you will have m different embeddings

### 02:18:40 · Speaker 1

Right. So that is the, I mean, that is the sort of advantage with a probabilistic encoder, right? That unlike in a BERT, et cetera, where for a given text sequence of tokens, you only have exactly one embedding. Here you can have a plethora of embeddings for a given particular input because you are modeling it probabilistically, correct?

### 02:19:04 · Speaker 1

And once you do that, if you have M of them to compute the first term, right, you need to take an average, I mean, meaning you take a sample average of all those M, uh, M, M, MCI basically, right, CJs.

### 02:19:18 · Speaker 1

But what I said is that some people when they implement VA you know they make this capital M to be 1. You can do it 1 also because it's a hyperparameter but you know M M being equal to 1 is not a great choice because you are approximating an expectation using one sample which is not a good thing to do no.

### 02:19:43 · Speaker 1

Yeah yeah

### 02:19:46 · Speaker 2

uh this x p theta of x given z so this x is all all x's right x1 x2 xn because of we have to maximize the likelihood of all x1 to xn

### 02:19:55 · Speaker 1

Not exactly but yeah but we are doing the entire treatment for one particular data point now see whatever we are doing now there is an outer sum on all data points you take a batch size and do it over batches

### 02:20:09 · Speaker 2

Yes yes

### 02:20:10 · Speaker 1

But I'm doing it for only one x right now for now I'm only doing it for one x so this is actually x re

### 02:20:18 · Speaker 1

And I should not be writing it as xi because it's a distribution over a random variable right but what I mean to say is that only one sample is what we are doing it for which should be extended to the entire data set on a batch level.

### 02:20:32 · Speaker 4

So like it's

### 02:20:33 · Speaker 1

Yeah yeah yeah or stochastic when you do it at the batch level because usual training no I'm I'm telling you how to train for one sample you can train it sample by sample or take a batch and do it doesn't matter but we'll see that I'm I was going to say that at the end of the end of the lecture but this is only I mean all that we are doing it is for only one data point okay

### 02:20:57 · Speaker 1

Now the next question is, any other questions on this? If not, we'll move on. Now we have to compute this log of p theta of x k 1 z. How do we compute log of p theta of x k 1 z is the question. So again there are multiple ways to do it. So now one way to do it is that express

### 02:21:23 · Speaker 1

using some parametric distribution

### 02:21:37 · Speaker 1

For example this is not the only way to do it again for example uh like assume

### 02:21:45 · Speaker 1

assume p theta of x given z to be coming from a Gaussian distribution okay what is the distribution on x of course

### 02:21:55 · Speaker 1

And you assume the mean okay to be equal to

### 02:22:00 · Speaker 4

Mm

### 02:22:06 · Speaker 1

output of the decoder

### 02:22:11 · Speaker 1

Variance to be equal to 100

### 02:22:14 · Speaker 1

note that in this case I am representing the neural network right the decoder network probabilistically

### 02:22:23 · Speaker 1

Now we're t theta

### 02:22:27 · Speaker 1

e theta of z

### 02:22:30 · Speaker 1

is the

### 02:22:31 · Speaker 1

Let us call that as X cap we've been calling it as X cap X cap

### 02:22:41 · Speaker 1

T theta of z is the output of the neural network

### 02:22:47 · Speaker 1

decoded okay now in this case what happens is that this xi cap that we get now which is

### 02:22:58 · Speaker 1

of Z J right

### 02:23:02 · Speaker 1

Now now this we in we are interpreting this as the mean of a Gaussian distribution right of p theta of x given z. So in this case in this case let's see what happens to log of

### 02:23:14 · Speaker 1

p theta of x given z what is this equal to this equal to

### 02:23:20 · Speaker 1

proposed that term one by two by

### 02:23:26 · Speaker 1

e by 2 sigma inverse that is identity that will go away this will be a e power

### 02:23:55 · Speaker 1

This is probably point x i know x okay let's call it as x x minus what is the mean the mean is given by d d t theta of z

### 02:24:07 · Speaker 1

the identity matrix is the identity is the uh the variance so this is equal to this okay now uh ignoring the constant let's just say some

### 02:24:23 · Speaker 1

I okay that's proportional because the other terms are independent

### 02:24:29 · Speaker 1

proportional to log and equal will go away this will be

### 02:24:33 · Speaker 1

Xmas

### 02:24:43 · Speaker 1

Now you see where the auto encoding thing is coming from it will become a

### 02:24:49 · Speaker 1

where there are loss okay between the input data point xi and the output of the decoder if you assume your p theta of x given z to be Gaussian so which implies

### 02:25:00 · Speaker 1

Now the expectation of what do we have expectation of log of p theta of x given z this with respect to q phi of z on x this is what we wanted right this we saw to be equal to the expectation of

### 02:25:22 · Speaker 1

But taking it with respect to P epsilon we have laws of

### 02:25:27 · Speaker 1

e theta of x given g of epsilon

### 02:25:32 · Speaker 1

Now sample in terms of sample averages how do we divide a approximate is approximately equal to 1 by m so if you sample

### 02:25:45 · Speaker 1

This is this under the assumption of Poisson entity it is there's a minus here that is equal to

### 02:25:54 · Speaker 1

psi minus

### 02:25:58 · Speaker 1

eat it off

### 02:26:10 · Speaker 1

You want to go to JK

### 02:26:14 · Speaker 1

Recorded

### 02:26:18 · Speaker 1

like I said zj is equal to

### 02:26:25 · Speaker 1

mu phi of xi plus epsilon j times sigma phi of

### 02:26:37 · Speaker 1

or j equal to one

### 02:26:44 · Speaker 1

Now you don't see the dependence on phi here, so maybe I should write it that way. Can you see that there is a dependence on z here? It is entire thing, this thing is a function of phi. Do you see the dependence on phi? It depends on phi through z, correct? Because z is dependent on phi, correct?

### 02:27:06 · Speaker 1

is what it is so now what we should do is that now how do we do like one uh training of encoder

### 02:27:17 · Speaker 1

One iteration of encoder is as follows I'll write that now

### 02:27:23 · Speaker 1

you have xi as an input the qf network

### 02:27:29 · Speaker 1

This will give you mu

### 02:27:34 · Speaker 1

new feel

### 02:27:38 · Speaker 1

and sigma phi of

### 02:27:42 · Speaker 1

So take these two sample epsilon j

### 02:27:49 · Speaker 1

I'm normal Z one

### 02:27:51 · Speaker 1

And find out

### 02:27:54 · Speaker 1

Z J

### 02:27:58 · Speaker 1

mu phi of xi plus epsilon j times sigma phi of xi

### 02:28:07 · Speaker 1

and then take this ZJ and pass it through the decoder

### 02:28:20 · Speaker 1

holding P theta of X K M Z and this will give you

### 02:28:25 · Speaker 1

beat heat up

### 02:28:30 · Speaker 1

x cap i or rather x cap j which is d theta of z j

### 02:28:41 · Speaker 1

Now what do you do like there is a forward pass this is the forward pass right take this get this done and take the

### 02:28:50 · Speaker 1

Uh okay so

### 02:28:54 · Speaker 1

get your z okay from your z get it through this this is one forward pass okay now how do we do reverse pass you know reverse pass is compute

### 02:29:06 · Speaker 1

I'll build it

### 02:29:08 · Speaker 1

So one for one particular xi you need to compute 1 by m

### 02:29:16 · Speaker 1

Note that for a particular input xi, you have multiple possible outputs because you have multiple embeddings, right, with different m's. You compute this, okay, and then take the

### 02:29:32 · Speaker 1

It is

### 02:29:33 · Speaker 1

compute the gradient of this with respect to p

### 02:29:40 · Speaker 1

And then simply back propagate this

### 02:29:46 · Speaker 1

will relate to the input of this. What happens here by the way once it comes to the input of the decoder

### 02:29:56 · Speaker 1

will happen so you have to backprop take this gradients

### 02:30:03 · Speaker 1

that propagate through this operation or ZJ operation

### 02:30:12 · Speaker 1

This operation

### 02:30:13 · Speaker 4

I mean we'll also have to remember this EJ that was used here right

### 02:30:18 · Speaker 1

Of course of course of course you have to save that

### 02:30:22 · Speaker 1

all M's you know you have to remember that is EJ so okay maybe I will write it this way to make it easier

### 02:30:33 · Speaker 1

From here

### 02:30:39 · Speaker 1

like this

### 02:30:42 · Speaker 1

Okay first it will come like this

### 02:30:45 · Speaker 1

From here you travel like this

### 02:30:52 · Speaker 1

is called the reverse pass so now forward pass also it comes like this and

### 02:31:03 · Speaker 1

through this okay and then from here you go like this

### 02:31:12 · Speaker 1

Oh sorry I think I changed the colour

### 02:31:15 · Speaker 1

This is the color we come like this

### 02:31:20 · Speaker 1

And from here

### 02:31:22 · Speaker 1

like this

### 02:31:26 · Speaker 1

So once you click this and you pass like this this is the forward pattern and the previous pattern

### 02:31:44 · Speaker 1

all propagation and stability

### 02:31:53 · Speaker 4

All this while

### 02:31:54 · Speaker 2

Well we don't change theta right

### 02:31:55 · Speaker 4

We keep the tea topic

### 02:31:56 · Speaker 1

we keep the theta constant to hold on i think so i'll have to do it this way to ensure that what i'm writing is more fit you will hold on this is only for training the encoder not decoder this thing that is this epsilon

### 02:32:23 · Speaker 1

Okay we know what that I'll I'll I'll write it you know what

### 02:32:38 · Speaker 1

Radiance

### 02:32:43 · Speaker 1

Do not flow

### 02:32:46 · Speaker 1

True sampling

### 02:32:53 · Speaker 1

see that so maybe I'll write it in a different color easier that way

### 02:33:16 · Speaker 1

This is something

### 02:33:23 · Speaker 1

That's it so this is

### 02:33:25 · Speaker 1

one iteration of trimming the encoder with the first term and we have not looked at the second term yet this is only for the first term the first term for the encoder by keeping the theta constant

### 02:33:40 · Speaker 1

Any questions on this

### 02:33:45 · Speaker 1

I see a hand raised Harish so uh we get m gradients by back propagating uh

### 02:33:57 · Speaker 1

Sorry I didn't follow can you repeat it was yeah

### 02:33:59 · Speaker 3

Yeah, sorry. So we get M gradients, right? While we since we have

### 02:34:08 · Speaker 1

No, no, one, one, one gradient. No, no, one gradient. See, what happens is you take M of Z's, right? You pass all those through the decoder and you get M X J caps, correct?

### 02:34:08 · Speaker 3

One one one

### 02:34:21 · Speaker 1

So you compute this this entire thing or this thing right you take the difference with all each of them individually and sum them off. So that will be one scalar that will be one scalar.

### 02:34:35 · Speaker 3

So we are summing up it at the end.

### 02:34:38 · Speaker 1

not one M so it is like M different outputs you take the difference between them and you sum and then it will be one scalar that you backpropagate

### 02:34:52 · Speaker 1

Any other question? See your second assignment will have this to be implemented. So yeah, I think this should be clear. So let me know if you have any other questions on this.

### 02:35:05 · Speaker 3

So why do we need to get a scalar sum at the decoder output like we have m different xjs and we can you know like compute the loss

### 02:35:17 · Speaker 1

See look at what is doing so we should not deviate from math so what is happening is we need to compute the expectation of q p of z given x for a particular x for 1 x

### 02:35:29 · Speaker 1

We represented that in terms of an expectation over another random variable. So expectation has to be computed and back propagated. You understand? So you have to compute the expectation of sample averages and the output of the decoder and you get one scalar that would be back propagated.

### 02:35:48 · Speaker 3

expectation of the sample average is and

### 02:35:52 · Speaker 1

Isn't it? So this is look at this equation, this equation is what we are trying to back propagate isn't it? That's the first term in elbow

### 02:36:02 · Speaker 1

So this is for a given x. So for a given x, you need to compute the expectation of that log likelihood with respect to q p of z given x for a particular x. And that will be represented as an expectation over epsilon, okay, which is a sum over all m samples. So we have to pass all those to the decoder, compute this, and then take a scalar and then backprop.

### 02:36:26 · Speaker 1

You're gonna have to make him

### 02:36:28 · Speaker 2

There was a second term for elbow right

### 02:36:31 · Speaker 4

Does not contribute

### 02:36:32 · Speaker 1

I see this one thing at a time that I'm only doing let's see look at what we are doing but forget what we are doing

### 02:36:41 · Speaker 1

Look at this

### 02:36:45 · Speaker 1

All this is for the first term, the gradient of the encoder parameters with respect to the first term. There's a story for the second term and both of the terms for the decoder. We have to still come one thing at a time.

### 02:37:00 · Speaker 2

This is not the complete gradient

### 02:37:01 · Speaker 4

Can we fall back?

### 02:37:02 · Speaker 1

are not no we are not completely it's only the first term that to the encoded parameters right so if you have questions on see this is the most complicated thing the rest are actually easy it's just simply training a neural network this is the most that's why i took the most complicated thing the first and then we will go one thing at a time okay um any any other questions on this let's move on so now this second now we have to compute the

### 02:37:32 · Speaker 1

To compute the gradients

### 02:37:45 · Speaker 1

Encoder

### 02:37:50 · Speaker 1

Only second

### 02:37:59 · Speaker 1

So what is the second term the second term is the scale divergence between

### 02:38:08 · Speaker 1

u p of z union x and p theta of z okay now what is done is

### 02:38:16 · Speaker 1

P t dot z

### 02:38:19 · Speaker 1

is assumed to be

### 02:38:25 · Speaker 1

normal zero one okay note that this is assumed to be independent of theta

### 02:38:32 · Speaker 1

This is a model assumption that is made and there are other lots of other improvisations over VAE that would question this and make it dependent on theta also. Okay. So for the the nine implementation, this is made independent assumed to be Gaussian 0 1 and it is made assumed to be independent of theta. So in that case, what happens is we have

### 02:38:59 · Speaker 1

u phi of z q on x okay to be a Gaussian

### 02:39:09 · Speaker 1

mu and sigma right

### 02:39:13 · Speaker 1

Now this implies that the second term which is the K between

### 02:39:26 · Speaker 1

will be equal to KL between

### 02:39:30 · Speaker 1

Gaussians okay one is a Gaussian

### 02:39:42 · Speaker 1

Another is a Gaussian

### 02:39:49 · Speaker 1

So this is

### 02:39:53 · Speaker 1

So what is this the deterministic form for this okay

### 02:40:08 · Speaker 1

Even by let me just tell you what

### 02:40:32 · Speaker 1

equal to

### 02:40:35 · Speaker 1

Hmm

### 02:40:38 · Speaker 1

Log

### 02:40:42 · Speaker 1

determinant of this minus D plus

### 02:40:48 · Speaker 1

Trace of uh

### 02:40:56 · Speaker 1

mine most of x

### 02:41:02 · Speaker 1

or I can write it as minus half log of this end

### 02:41:06 · Speaker 1

So this plus plus

### 02:41:12 · Speaker 1

We all

### 02:41:16 · Speaker 1

Mufi

### 02:41:19 · Speaker 1

mu phi of x squared this is this is what it is you know you can show this Gaussian between two sorry KL between two Gaussian distributions can be deterministically found out and simply take it as a small homework and do this okay yeah this is what it is okay so KL now is a simply a function of sigma v x right mu x so this means

### 02:41:43 · Speaker 1

It is encoder decoder thing write it again

### 02:41:49 · Speaker 1

X I Q P of

### 02:41:52 · Speaker 3

Is it square of norm or just the norm

### 02:41:57 · Speaker 1

I think it should be square square yeah

### 02:42:03 · Speaker 1

you have

### 02:42:06 · Speaker 1

Leave them off your website

### 02:42:09 · Speaker 1

All you need to do is just one forward pass to get your mu p and sigma p right and let's write this as some

### 02:42:21 · Speaker 1

which is a function of mu phi of xi and sigma phi of xi

### 02:42:30 · Speaker 1

So now you have to compute one forward pass and then the reverse pass just you just have to compute

### 02:42:39 · Speaker 1

Don't even have to go to decoder at all just compute this

### 02:42:44 · Speaker 1

Yeah I love you too

### 02:42:47 · Speaker 1

sigma v of xi okay and then simply

### 02:42:53 · Speaker 1

gradient of course not

### 02:43:01 · Speaker 1

and simply back propagate it

### 02:43:04 · Speaker 1

You know what happens is no for one trust one uh uh one uh iteration of encoder training you will have like one gradient coming through the decoder okay and like there will be just this plus the KL gradient also gets added here.

### 02:43:26 · Speaker 1

We'll have to add both the gradients here. So this what we are adding here, this will get added with the gradient that is coming from the decoder and this completes the encoder training.

### 02:43:37 · Speaker 1

It's all right

### 02:43:42 · Speaker 1

they should be straightforward no nothing complicated here now to train the decoder

### 02:43:58 · Speaker 1

How do we try and get the decoder So first thing to be seen is the second term

### 02:44:07 · Speaker 1

Here the term

### 02:44:11 · Speaker 1

Independent of

### 02:44:13 · Speaker 1

Equator parameters theta right

### 02:44:21 · Speaker 1

don't have to use that at all now what should we do is that just

### 02:44:32 · Speaker 1

Take an X ray

### 02:44:35 · Speaker 1

You will be of z given x

### 02:44:41 · Speaker 1

Just finish this and then close the class. So sigma phi of xi

### 02:44:47 · Speaker 1

Then you have like epsilon j coming from normal 0 1.

### 02:44:53 · Speaker 1

they compute cj to b

### 02:45:04 · Speaker 1

and then you pass it through the decoder

### 02:45:14 · Speaker 1

What do you get as XT cap?

### 02:45:21 · Speaker 1

Now how do we train this So what we have to do one complete forward pass

### 02:45:28 · Speaker 1

as usual

### 02:45:31 · Speaker 1

Then you do sampling and once you do from here it goes like this and then it goes like this goes like this and you have to simply compute

### 02:45:42 · Speaker 1

gradient theta which which term you have to compute the term this xi minus d theta zj

### 02:45:54 · Speaker 1

So you do the radiant opacity

### 02:45:58 · Speaker 1

This term with respect to j, right? And then simply back propagate this all the way to the input.

### 02:46:06 · Speaker 1

It is one decoded right

### 02:46:09 · Speaker 1

One I think I know decoder try

### 02:46:16 · Speaker 1

easy right that's all so now we are done with the training of VAE

### 02:46:32 · Speaker 1

In the next class know when we begin we will look at how to do inference which is the we have to do sampling and also posterior inference know I think it's obvious right I mean you can once the training is done you just

### 02:46:47 · Speaker 1

discard the encoder and pass it through the depasser z through the decoder you will simply get uh uh the generation and you take an xi pass it through the encoder you get the uh the embeddings right that's all it is always remember right whenever we are doing sampling in an encoder decoder model generation is always done through the decoder model okay uh and the embeddings are extracted through the encoder model so we will continue from here so what i'll do in the next class

### 02:47:17 · Speaker 1

that we will look at like complete the VAE discussions and also look at one two improvisations over it you know especially I want to talk about one state of the art VAE model called vector quantized VAE or VQ VAE which is what is used in stable diffusion and all that okay that would be like

### 02:47:36 · Speaker 1

like 30 percent of the net class and next we will go to diffusion models which are the state of the art for like image generation these days okay uh which is actually one particular form of the vae but i urge all of you to kindly go through my notes and also today's discussion on vae's and how to train them i think i'm sorry i actually did it this way right i mean i inadvertently zoomed it at this point but yeah i think you can also zoom it right because it was convenient

### 02:48:06 · Speaker 1

So please go through the class notes and also my handwritten notes and read the VAE paper and be thorough with all this before coming to the next class so that it will be easier for studying diffusion models and so on.

### 02:48:21 · Speaker 3

Sir one question

### 02:48:22 · Speaker 1

Yes

### 02:48:23 · Speaker 3

So the first the first KL term that will be used to update both the encoder as well as decoder right like in the same path

### 02:48:32 · Speaker 1

So hold on there is no first term is not the KL term the second term is the KL term

### 02:48:41 · Speaker 1

So you just said path care term there is no sorry sorry I mean I mean

### 02:48:43 · Speaker 3

Sorry sorry I mean I mean I mean in in the overall equation the first

### 02:48:49 · Speaker 1

Oh shit you got em

### 02:48:51 · Speaker 1

reconstruction term it is called okay the reconstruction term is used to uh update both encoder and decoder but when you are training the encoder you keep the decoder parameters fixed and vice versa

### 02:49:04 · Speaker 3

So can't we like so does that mean in in in one pass we cannot update encoder and decoder simultaneously?

### 02:49:13 · Speaker 1

How do you do it? No see you have to do take two gradient passes I wrote the equation also right here here yeah this is how you do it first you have an encoder update and then a decoder update

### 02:49:27 · Speaker 1

Right So when you train the encoder you keep the decoder parameters fixed and vice versa

### 02:49:38 · Speaker 4

I I had a question on the assignment is this the

### 02:49:44 · Speaker 1

Yeah let me just any any questions on the class before we go to the assignments

### 02:49:48 · Speaker 2

Yeah so I had one question so for example in tr during this training right I mean we start with the decoder training first or the encoder training first I mean in fact

### 02:49:56 · Speaker 1

All right it doesn't matter doesn't matter doesn't matter you just train one one one pass of encoder one pass of decoder that finishes one training yeah

### 02:50:05 · Speaker 2

And any thoughts on the uh uh the convergence I mean how well this converges compared to say

### 02:50:11 · Speaker 1

Yeah this will very nicely convert there is no adversarial training that is happening here no

### 02:50:19 · Speaker 1

Unlike in a GAN there is no there is no min-max there is no I mean encoder is not adversary to the decoder right they are both working towards the same objective

### 02:50:28 · Speaker 1

VAEs are known to converge much much better than VAEs because there is no adversary saddle point problem there is no saddle point problem

### 02:50:37 · Speaker 4

I understood thank you

### 02:50:40 · Speaker 1

Okay, uh, yeah. Questions on assignment you said, yeah, go on.

### 02:50:45 · Speaker 2

Yeah so sir uh as uh I understood it maybe I'm wrong

### 02:50:50 · Speaker 1

One ago we are doing with

### 02:50:50 · Speaker 2

We are doing with uh

### 02:50:53 · Speaker 1

Sorry can you make it quick I have another class at twelve thirty so yeah yeah

### 02:50:56 · Speaker 2

Yeah, yeah, good question, sure. So one and two, anyway, we are doing with butterfly and rest all the animal data set, right? So anyway, we have to retrain the model with animal. So for the butterfly one, can we go with our independence of freedom, like choosing our laws and...

### 02:51:12 · Speaker 3

etc.

### 02:51:13 · Speaker 2

right because or anyway we have to we are doing all this condition like usual loss double gel loss

### 02:51:18 · Speaker 1

Arijit, hold on. What is your precise question? Please ask me your precise question. I can understand the question.

### 02:51:27 · Speaker 2

Okay uh then let me do one thing let me watch

### 02:51:30 · Speaker 3

Okay that would be better I think you have a class

### 02:51:34 · Speaker 1

Right okay you can ask me the question I still have five minutes ask me the

### 02:51:38 · Speaker 2

So I I

### 02:51:39 · Speaker 1

I want to say

### 02:51:41 · Speaker 2

Yeah, so the butterfly dataset one, which we are doing one and two, I can use any loss of my choice, right? I mean, for example, WGAN or all, there is no foundation there. Only the conditions are applied for the animal dataset, which again, anyway, we have to retrain the model.

### 02:52:00 · Speaker 1

Again what is your question here I I I so no

### 02:52:03 · Speaker 4

No I mean as a butterfly one we have the freedom to use any loss function or anything

### 02:52:12 · Speaker 1

Gan you always use one loss function right which is that saddle point problem what is the other loss function that you would use

### 02:52:19 · Speaker 2

Because uh no because uh there is a I mean we can use DC loss etc right also

### 02:52:28 · Speaker 1

For a DCGAN loss does not change only the architecture changes no

### 02:52:33 · Speaker 3

Yes yes right

### 02:52:35 · Speaker 1

Are you asking whether you can use an MLP for butterfly? Is that what the question is?

### 02:52:41 · Speaker 3

Yes kind of

### 02:52:44 · Speaker 1

So yeah, you can use anything. See, but again, that's why I'm asking you that please, if you if you make your question precise, the answer can be given precisely.

### 02:52:53 · Speaker 2

Uh okay I think uh I will ask you separately then uh I mean

### 02:52:57 · Speaker 1

So think about it and let's keep on yeah

### 02:52:59 · Speaker 3

Yeah

### 02:53:00 · Speaker 1

Ah yes, yes.

### 02:53:00 · Speaker 3

Yes yes sure

### 02:53:01 · Speaker 4

Thanks buddy

### 02:53:04 · Speaker 3

Sir just to confirm next week we are not having a class and also we won't be having a quiz right like every alternate week

### 02:53:11 · Speaker 1

You are

### 02:53:12 · Speaker 3

We were supposed to have a voice

### 02:53:14 · Speaker 1

it correct correct so the schedule will change so the quiz will be the week next afterwards correct

### 02:53:23 · Speaker 1

see on that note no like happy to serve out all of you yeah

### 02:53:28 · Speaker 3

So

### 02:53:30 · Speaker 4

So I have two questions in the assignment. One is that we had mentioned is the decoder network for the eighth and ninth question right So we discussed the decoder network only in the VAE so is it similar to something that you are to use something like beyond

### 02:53:43 · Speaker 1

Yeah, yes, correct. So I've precisely told you what to do, right? You train another network. See, when you are training the GAN, just have another network which will take the generated image and just gives back the input noise. And you can take an MSE between them and train it together.

### 02:54:01 · Speaker 1

Along with D along with

### 02:54:01 · Speaker 4

Oh indeed

### 02:54:04 · Speaker 1

along with the adversarial objective

### 02:54:07 · Speaker 4

Okay, I think that's the same follow up question on Tolteque. So, yeah, we mentioned that use the augmented images.

### 02:54:12 · Speaker 2

the training right so is it only augmented image we got to use or we got existing original and augmented together and we got to pass it together

### 02:54:19 · Speaker 1

Whenever you are taking augmented images, you should always take the original plus augmented. You should not give away the original thing. Original images rotated with two, three angles, right? And that would be your data set will increase by three, four times. Yeah.

### 02:54:20 · Speaker 4

I mean I don't know

### 02:54:36 · Speaker 4

Uh sorry sorry one more thing so this you mentioned the two inputs to be used right in this uh later stage so it is a say uh

### 02:54:42 · Speaker 2

same distribution or the different distribution with the two inputs in the machine

### 02:54:46 · Speaker 1

What do you mean to protect

### 02:54:47 · Speaker 4

We input our test

### 02:54:49 · Speaker 2

As a vector questing randomly sampling two input vectors

### 02:54:53 · Speaker 1

Yeah that's yeah that's

### 02:54:53 · Speaker 4

Yeah that's cool

### 02:54:55 · Speaker 1

same distribution right i mean in a gann like a sample you will only sample from the same distribution at the input otherwise sample from different distributions will yeah

### 02:54:57 · Speaker 4

I like the sound

### 02:55:01 · Speaker 4

Uh sample from okay

### 02:55:05 · Speaker 4

Okay okay so it's a Z only we are using we have to do the two tool times we have to take the two input

### 02:55:08 · Speaker 1

Yeah take two z's pass it through the input generator and then interpolate between them and observe what happens at the output okay

### 02:55:18 · Speaker 2

Okay

### 02:55:21 · Speaker 1

Got it

### 02:55:23 · Speaker 2

Sorry about the exam so portions till this time uh including the references that you have mixed in your handwritten notes and all the glasses that's what we should be expecting right

### 02:55:32 · Speaker 1

You can be expecting

### 02:55:33 · Speaker 2

And like it would be a theory only and mostly derivations would be involved. Just want to know the type of queries that we should be preparing.

### 02:55:42 · Speaker 1

I have not I have not said the question please forget so it will be it will involve some math okay it will I will not be asking the questions like differentiate between GANs and VAEs that's not how it will be it will be like some thought provoking and you have to do you have to practice math okay

### 02:56:01 · Speaker 1

It'll not be descriptive I'll not be asking you to like describe how GAN works and all that no definitely not okay

### 02:56:12 · Speaker 1

Okay, so see, feel free to like ping on that WhatsApp group or teams and get in touch with TAS, you know, they are helpful as well, both Suhas and Chandan, you can get in touch with them.

### 02:56:25 · Speaker 1

And you can always ask me questions as well. Yeah. And all the best for your exam. I will give you details, the instructions on how the exam would be and all that. Once I complete the question paper, which is like I'll do it the mid next week. And once I do that, I'll tell you like what the instructions are and so on. Okay.

### 02:56:47 · Speaker 2

Okay

### 02:56:47 · Speaker 1

But yeah anytime you think

### 02:56:50 · Speaker 2

sorry should we be like looking into the previous year model paper if you have any like whatever the paper you had

### 02:56:56 · Speaker 1

don't know where it is it should be there somewhere i don't know where it's it where is it don't worry i don't worry too much it's fine yeah

### 02:57:08 · Speaker 1

Okay, see you then all the best

### 02:57:15 · Speaker 2

Yes sir

### 02:57:15 · Speaker 1

Thanks

### 02:57:21 · Speaker 1

Have a nice week
