---
id: TEEwwvPZBZc
title: Lec 13 - Deep Generative Models Self supervised learning Noise contrastive
  estimation
url: https://www.youtube.com/watch?v=TEEwwvPZBZc
date: '2024-11-23'
duration: 02:37:56
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# Lec 13 - Deep Generative Models Self supervised learning Noise contrastive estimation

## Transcript

### 00:00:02 · Speaker 1

See well it's not opening calendar CCC exam and

### 00:00:12 · Speaker 1

Course grade entry 311 to 1812 IC

### 00:00:23 · Speaker 1

which means that we can do the assignment by us after your exam will that be okay for you

### 00:00:33 · Speaker 1

First week of December

### 00:00:35 · Speaker 2

Yes sir

### 00:00:38 · Speaker 1

Okay let us do it then then what we can do is after the final exam is done on 30th the first week of December we will do because 12th is when I need to submit the grade sorry 18th is the last date for me to submit the grades so I'll have enough time to consolidate and discuss and all that oh no no no this is 2023 I'm sorry I'm sorry I need to look at 2024 calendar

### 00:01:12 · Speaker 1

Just a second ah sorry sorry this is my mistake

### 00:01:20 · Speaker 3

I think it is twelfth sir

### 00:01:23 · Speaker 1

Twelfth of December ah, how do you know?

### 00:01:26 · Speaker 3

I think in reinforcement learning salaried nagars are told that 12th is the final date to put grades we have a project pending there in reinforcement learning also

### 00:01:40 · Speaker 1

Okay okay so there is this link it's not opening yeah

### 00:01:45 · Speaker 1

Yeah I am just opening hold on yeah

### 00:01:52 · Speaker 1

Course grade entry 13 12 2024 is the last date. Yes. Yeah. Okay. 13th is the last date. Even then I think

### 00:02:02 · Speaker 1

It's enough for me if I have one week. So yeah, let us do it on the week of 2nd December. 2nd to 6th December is there no? We will do it. We'll do the Vaibhavan. Okay, I think that is okay.

### 00:02:16 · Speaker 1

Okay so then that's it yeah I think I'll continue with the class

### 00:02:19 · Speaker 4

So what is the format of the VIVA exam going to be? I mean how much time is that going to take and what will be the schedule?

### 00:02:28 · Speaker 1

I we will let you know all of that

### 00:02:32 · Speaker 1

See I'm thinking of uh like uh about uh 20 minutes per group uh or rather half an hour per group

### 00:02:39 · Speaker 1

And we have 20 groups, no? We are like three of us, four of us, three TAs and myself. We will make five groups per instructor and we will spend half an hour with each of the groups and then we will evaluate. That is the scheme that I'm thinking. Schedule I will let you know, okay? Maybe late evenings or weekend something we will make, so that it is beneficial for all.

### 00:03:07 · Speaker 1

That that you can adjust no problem yeah whatever works for you

### 00:03:10 · Speaker 4

I just wanted to request for some flexibility as I will be traveling due to some official work so I'll be in a different time zone at that time

### 00:03:20 · Speaker 1

No no okay see those requests we can always accommodate no problem yeah

### 00:03:24 · Speaker 4

John thank you

### 00:03:27 · Speaker 1

Okay, so shall we get back to the business? Shall we start? Sir, one question.

### 00:03:31 · Speaker 2

So one question I had

### 00:03:34 · Speaker 2

This is something related to the quiz five we just did. So, if you allow, I wanted to ask a question.

### 00:03:40 · Speaker 1

And tell me what is that

### 00:03:42 · Speaker 2

So sir, there was a question. It says in DDPM, the variance schedule alpha t for each time step is carefully designed to satisfy which of the following criteria? The answer marked is it should increase gradually to prevent complete information loss in early steps. But as per my understanding, like alpha t is the product of from alpha 1 till that particular time.

### 00:04:06 · Speaker 1

No no no see that we call as alpha bar

### 00:04:12 · Speaker 1

This is the variant schedule alpha

### 00:04:16 · Speaker 4

But even alpha should reduce right because we want the variance to increase as we go forward in the steps

### 00:04:23 · Speaker 1

Variation should reduce no

### 00:04:25 · Speaker 4

Variance is one minus alpha t right

### 00:04:30 · Speaker 1

Now alpha is what we called as the variance isn't it in our in our treatment

### 00:04:40 · Speaker 4

I suppose it was one minus alpha was the

### 00:04:43 · Speaker 2

Select alpha, we are drawing it from a zero from these samples from zero comma one space right

### 00:04:50 · Speaker 1

No no they are simply linearly varying let me just check it once hold on

### 00:05:16 · Speaker 1

So small alphas are

### 00:05:39 · Speaker 1

So beta 1 minus alpha would increase. So which means alpha should decrease gradually, right? What was the option that was there?

### 00:05:48 · Speaker 1

Electro

### 00:05:48 · Speaker 4

The selected option was alpha alpha increases

### 00:05:53 · Speaker 4

Uh the correct option was marked as alpha should in increase

### 00:05:57 · Speaker 1

No one minus alpha should increase

### 00:06:02 · Speaker 4

Yeah I mean for the last options that are very gradually decrease

### 00:06:04 · Speaker 1

That will gradually decrease. Yeah, that should be the correct one. Because

### 00:06:10 · Speaker 1

Yeah, because the variance was 1 minus alpha, right? The variance term in Xt that is 1 minus alpha, the variance should gradually increase.

### 00:06:25 · Speaker 1

It's correct

### 00:06:25 · Speaker 2

Our variance should increase eventually because we want the final x of t of normal distribution correct

### 00:06:31 · Speaker 1

Yeah yeah the thing is

### 00:06:34 · Speaker 1

Only when the variance slowly increases you can guarantee that the Markov chain converges to a normal 0 1. So, variance should gradually increase.

### 00:06:45 · Speaker 1

Bendon are you there?

### 00:06:49 · Speaker 2

Yes sir I'm there yes sir

### 00:06:56 · Speaker 1

variance schedule I mean of course variance schedule is 1 minus alpha but yeah you can the parameter is alpha so variance schedule alpha so if you are looking at alpha as the variance schedule then the alpha should gradually decrease

### 00:07:11 · Speaker 4

Yes sir, I'll make the necessary change yes sir

### 00:07:16 · Speaker 1

Beta should increase basically yeah

### 00:07:19 · Speaker 4

Um just a thing sir in the option it says it should decrease exponentially the one that is being debated right now um so is is it supposed to really decrease exponentially or was that the case

### 00:07:33 · Speaker 1

Isn't there an option that would say it would linearly decrease

### 00:07:39 · Speaker 2

No sir

### 00:07:41 · Speaker 1

No

### 00:07:43 · Speaker 2

I have I I really have no access to the quiz I really don't know

### 00:07:46 · Speaker 4

What is the challenge of

### 00:07:47 · Speaker 2

Chandan I have pasted this screenshot in the chat if you could have a look

### 00:07:52 · Speaker 1

That's okay if if if there is no linear decrease option

### 00:07:52 · Speaker 4

That's okay

### 00:07:56 · Speaker 4

Uh decrease option we'll give it to

### 00:08:01 · Speaker 1

It should be see yesterday what happened as I looked at the quiz and there was beta there I told them that beta is not something that I have used so change it to alpha so I think they just change beta to alpha without changing the options

### 00:08:18 · Speaker 1

You guys, you do... What can I say? See, I told you to change beta to alpha in a meaningful way and just not replace alpha, beta by alpha. Right? If alpha is 1 minus beta, then the options have to like...

### 00:08:34 · Speaker 4

I'll know it has to be flipped

### 00:08:38 · Speaker 1

Anyway so any other question you have about the add plus one feature okay

### 00:08:42 · Speaker 4

Oh yeah yeah yeah

### 00:08:43 · Speaker 1

Thanks for checking it out yeah

### 00:08:45 · Speaker 2

are one more question so we we said that we are choosing alpha alpha alpha as from zero to one but on what basis are we selecting like what is the predefined logic for that

### 00:08:56 · Speaker 1

I told you in the class already in the previous class it is designed in such a way that the forward macro chain that we do that we construct has to be

### 00:09:06 · Speaker 1

designed in such a way that the stationary distribution converges to normal 0 1

### 00:09:11 · Speaker 1

So that is why the variance has to slowly decrease

### 00:09:17 · Speaker 1

And also if you look at it it's all huh huh

### 00:09:20 · Speaker 2

Variance has to slowly increase

### 00:09:23 · Speaker 1

What do you what do you call by variance

### 00:09:27 · Speaker 4

minus alpha

### 00:09:28 · Speaker 1

If you call one minus alpha as variable then it should increase yeah

### 00:09:34 · Speaker 1

Depends on what you call by variance so it is uh if it's alpha then the alpha should gradually decrease which means that 1 minus alpha should increase okay

### 00:09:43 · Speaker 1

That is what you have to implement in your assignment also right and talking of assignment I have made assignment three of right last week itself I did it huh

### 00:09:56 · Speaker 1

I hope you have started working on it When is the deadline for assignment three Now I've kept it

### 00:10:04 · Speaker 1

1870

### 00:10:07 · Speaker 1

Okay then you should have started it already

### 00:10:12 · Speaker 1

Anything else shall we get started in the class

### 00:10:20 · Speaker 4

Oh okay can I take this

### 00:10:24 · Speaker 1

I oh

### 00:11:46 · Speaker 1

It says working offline to me do you see my screen

### 00:11:56 · Speaker 1

know why it says you are working offline okay anyway okay let's start see today's agenda is that we will be discussing some self supervised learning techniques

### 00:12:12 · Speaker 1

So which are the

### 00:12:15 · Speaker 1

special cases of these broad learning tech no methodologies called representation learning okay. So what is representation learning I had given some introduction in the previous class. So given some data that is on iid for my distribution what you want to learn is a function f theta from the data space to some latent space z okay where the dimensionality of z is much less than the dimensionality of x.

### 00:12:43 · Speaker 1

So now we seek some special properties on Z so the properties that we seek is in such a R R that

### 00:12:52 · Speaker 1

the representations are win by representation I mean z okay the projection that you learn on data and we need that to have some desirable properties such as

### 00:13:07 · Speaker 1

If you use z instead of x then the amount of supervision that you need is much lesser and the

### 00:13:16 · Speaker 1

Z becomes much robust than X and all that. Now, learning representations can be done in two ways. One is the generative way where you learn a latent variable model and use the latent space as representations. We have seen this all throughout the course.

### 00:13:36 · Speaker 1

And I've asked you to do this in your assignments as well, where any latent variable model that you learn.

### 00:13:44 · Speaker 1

implicitly have this capability of learning representations because when you do posterior inference which is get samples from p of z given x then you are automatically doing

### 00:14:00 · Speaker 1

representation learning because z the latent variables that you get from a latent variable generative model can be seen as representations ok that is one way to do it. The other way to do it is what we will see which is a non generative way also called self supervised learning or contrastive learning way ok where the fundamental idea is that you define a pre text task.

### 00:14:25 · Speaker 1

Okay, uh what is the pretext task you solve

### 00:14:30 · Speaker 1

Some other task using data. Note that in all the representation learning literature, you don't have labels. This is label-free learning. So now we should, when you don't have the labels, you define some pseudo tasks, where you define some pseudo labels and you ask a neural network to solve some pseudo tasks. And the intermediate representations of the

### 00:15:00 · Speaker 1

pseudo task solver is what you take as representations for data. The examples for pseudo tasks are if you are looking at like learning representations for images, then you take an image, rotate it with some angle by some angle and ask a neural network to predict the angle of rotation. So, that can be one pseudo task. The other pseudo task can be that you have an image, you add some noise to it and try to

### 00:15:30 · Speaker 1

Classify between the noise and the data and you take the intermediate representations of that classifier as your representation and so on. The other thing can be that you take data and you mask it and try to reconstruct the data back. That is one other way to define it. So these class of methods are called self-supervised learning techniques. Now we will go deeper into it and see why should these methods even help in learning good

### 00:16:00 · Speaker 1

representations and also some famous examples of how to do it. In fact, the language models like BERT etc. also uses the same kind of technique to learn representations on data.

### 00:16:17 · Speaker 1

Uh any questions on this so far

### 00:16:41 · Speaker 1

Nope my audio is off

### 00:16:47 · Speaker 1

Any questions

### 00:16:51 · Speaker 2

Maybe we'll cover it later. Just a query here. The pretext tasks are defined I mean like based on how it should perform in the end right I mean

### 00:17:02 · Speaker 1

Well not necessarily um not necessarily see

### 00:17:07 · Speaker 1

I will tell you what the fundamental idea behind this thing and in fact how to define a pretext task is a question that people have been asking right and different ways have been looked at okay I will talk about it we will talk about it yeah

### 00:17:28 · Speaker 2

Good thank you

### 00:17:36 · Speaker 4

Worry like is there any methodology like if we define this pretext then the embedding we'll get we'll have you know some kind of structures which will be helpful for other features like what I mean is if suppose I use the pretext as in painting then it will be helpful in classification or segmentation but if I use some other pretext then it won't be much helpful for classification or any other segmentation task

### 00:18:06 · Speaker 4

They're any such kind of thing

### 00:18:09 · Speaker 1

Um

### 00:18:11 · Speaker 1

Not theoretically but there are some empirical ideas on what sort of predicate tasks would help. We will discuss all that just let's see give some time.

### 00:18:24 · Speaker 1

Okay it's not there yet

### 00:18:29 · Speaker 1

Did I do and see

### 00:18:40 · Speaker 1

Just turn it down it's looking pretty

### 00:19:51 · Speaker 1

Just wanna see if I did it the last year and if there is

### 00:20:28 · Speaker 1

Ah okay I've done it

### 00:20:32 · Speaker 1

Just a second

### 00:20:36 · Speaker 1

Two minutes I have to

### 00:21:45 · Speaker 1

Okay, the fundamental idea for all

### 00:21:51 · Speaker 1

Self supervised learning techniques come from this very nice paper, very nice methodology that came up which was called noise contrastive estimation.

### 00:22:16 · Speaker 1

as contrastive estimation also we write it as MCE. So, the basis for self-supervised learning lies here. The question that is asked is the following. Suppose

### 00:22:36 · Speaker 1

The theta

### 00:22:42 · Speaker 1

Drawn from a

### 00:22:45 · Speaker 1

from an unknown distribution P x

### 00:22:57 · Speaker 1

So what we have is we have D that is given by X1

### 00:23:04 · Speaker 1

to up to X M

### 00:23:07 · Speaker 1

These are drawn IED from PX

### 00:23:13 · Speaker 1

Objective

### 00:23:18 · Speaker 1

Easy to estimate

### 00:23:23 · Speaker 1

estimate the underlying distribution

### 00:23:33 · Speaker 1

Underlying distribution P x

### 00:23:41 · Speaker 1

given D right. So, it has been a question that we have been asking. So, now how do we estimate the underlying distribution given a particular given samples from distribution right. This is a question that we have been asking. How did we do that? I mean so far we have looked at the maximum likelihood estimate.

### 00:24:11 · Speaker 1

the minimum KL estimate right so both of them are equivalent

### 00:24:19 · Speaker 1

How did we do that

### 00:24:21 · Speaker 1

Start with

### 00:24:24 · Speaker 1

A parametric form for the PX

### 00:24:32 · Speaker 1

Call it p theta

### 00:24:35 · Speaker 1

Get theta

### 00:24:39 · Speaker 1

that would simply minimize some divergence metric which we call the F divergence between P x and P theta. This is what we have been doing the entire course right all the ah generative modeling frameworks that we saw uh were actually

### 00:24:56 · Speaker 1

fitting into this framework right where uh

### 00:25:01 · Speaker 1

uh minimized uh a divergence metric between started with uh an assumption on the uh the parametric assumption on the underlying density called it P theta right

### 00:25:14 · Speaker 1

And minimize the divergence metric F uh F divergence metric between these two so now how do we define uh P theta

### 00:25:22 · Speaker 1

is where we change different models you know in Gyan the speed theta is taken to be the samples that are coming from a transformed

### 00:25:33 · Speaker 1

Gaussian random variable transformation is through neural network in a VAE we use a latent variable model for this and we

### 00:25:41 · Speaker 1

find a lower bound on this and then optimize this and so on right then we know the entire story this is how we do it in a

### 00:25:51 · Speaker 1

generative framework right. So, where we assume a parameter form p theta and define the parameters by minimizing error parameters. So, now, NCE provides an alternative for this.

### 00:26:12 · Speaker 1

alternative for ML estimation

### 00:26:20 · Speaker 1

Now uh self supervised learning for today get uploaded hold on a minute

### 00:26:28 · Speaker 1

I just wanted this to get uploaded to my drive so that I can access it simply

### 00:26:50 · Speaker 1

Okay, so in noise contr in in self-supervised learning, see you what do we need? We need a representation for data, right? So when do you think data would be represented optimally? The data would be represented optimally only if you learn the underlying distribution correctly, isn't it?

### 00:27:11 · Speaker 1

See what we need is that we need to learn the underlying distribution correctly because if we do not learn the distribution then we are not representing the data. See that is why the generative modeling framework right will give in will implicitly give you representations because by by definition when we have a latent variable model the latent variables actually aid minimizing the KL divergence between or rather F divergence between the the true distribution and the model distribution right.

### 00:27:41 · Speaker 1

Therefore the representations that we get by solving a KL minimization problem under related variable model implicitly gives us a representation. Now we are explicitly trying to find the representation. This is not getting uploaded.

### 00:27:58 · Speaker 1

Do you know some other way to do this Uh

### 00:28:02 · Speaker 1

Sorry about this

### 00:28:11 · Speaker 1

Has anybody used this airdrop thing between two Mac devices? Do you know how that works?

### 00:28:29 · Speaker 1

Am I audible

### 00:28:31 · Speaker 4

So you can also also share it between two teams instances if you have it on both the instances

### 00:28:38 · Speaker 4

Share it to yourself

### 00:28:40 · Speaker 1

you can just right click on the file and share and then you'll see airdrop there

### 00:28:52 · Speaker 1

Oh this is very good okay I just came from a math

### 00:29:01 · Speaker 1

Apple devices are what they are for a reason no they are extremely good okay I just got what I wanted thanks

### 00:29:23 · Speaker 1

Okay so you see my screen now

### 00:29:27 · Speaker 1

You see my screen

### 00:29:34 · Speaker 2

So there's a file transfer pop-up

### 00:29:37 · Speaker 1

No no no I'm writing on my official stamps no

### 00:29:59 · Speaker 1

Let me know when you can see my screen

### 00:30:24 · Speaker 1

Can you see my screen

### 00:30:28 · Speaker 2

Not yet

### 00:30:32 · Speaker 1

It's a computer

### 00:30:45 · Speaker 2

Mm yes it is visible now

### 00:30:54 · Speaker 1

I'm writing do you see that no

### 00:31:03 · Speaker 4

No no it is stuck at the NC provides an alternative for ML estimation I think it's stuck there

### 00:32:35 · Speaker 1

Can you please let me know if it's coming

### 00:32:41 · Speaker 4

Yes sir we can see suppose that you're not

### 00:32:47 · Speaker 1

Okay so hopefully

### 00:32:49 · Speaker 1

not misbehavior. Now, we have noise contrastive estimation provides an alternative for ML estimation, where the goal is to estimate the underlying distribution. Now, how does NCE does this? Now, we have data

### 00:33:09 · Speaker 1

We have data that is x1 x2

### 00:33:15 · Speaker 1

Up tall

### 00:33:17 · Speaker 1

Let's call it X

### 00:33:22 · Speaker 1

Let us draw it from bx this is what we need to estimate ok

### 00:33:34 · Speaker 1

I think we deflame

### 00:33:39 · Speaker 1

Nice

### 00:33:41 · Speaker 1

find a noise distribution

### 00:33:51 · Speaker 1

Noise distribution P

### 00:33:54 · Speaker 1

Yeah

### 00:33:56 · Speaker 1

and draw samples from it

### 00:34:07 · Speaker 1

Let's call this as DN

### 00:34:10 · Speaker 1

This

### 00:34:14 · Speaker 1

uh maybe we will change the notation the too many n's that I'm using t number of samples and you have n1 n2

### 00:34:27 · Speaker 1

Yen

### 00:34:30 · Speaker 1

These are drawn from P N IAD from P N

### 00:34:36 · Speaker 1

So, you know what we you understand what we are doing we have the data distribution that we have been given ok. We define a noise distribution Pn and draw samples from it which we are denoted by n1 to n t ok. Now, define an estimator

### 00:35:00 · Speaker 1

Define an estimator JT parameterized by theta as follows

### 00:35:11 · Speaker 1

How do you define J theta? J t of theta t because it depends on t number of samples it's given by 1 over 2 t

### 00:35:22 · Speaker 1

Sigma 40 log of

### 00:35:27 · Speaker 1

H theta of

### 00:35:30 · Speaker 1

xt plus log of

### 00:35:35 · Speaker 1

1 minus h theta of n t

### 00:35:45 · Speaker 1

What

### 00:35:50 · Speaker 1

HTDP

### 00:35:54 · Speaker 1

H theta you can take both H t and N t so H theta is a function

### 00:36:00 · Speaker 1

adametloid

### 00:36:06 · Speaker 1

You are in neural network

### 00:36:21 · Speaker 1

Four

### 00:36:28 · Speaker 1

H theta is a function that takes data from d dimensional space and maps it to the 0 1

### 00:36:50 · Speaker 2

So the submission

### 00:36:50 · Speaker 4

is common right for both

### 00:36:53 · Speaker 1

Assessment is common for both of them yes

### 00:37:02 · Speaker 1

Okay so this J T theta okay is called the noise contrastive estimator

### 00:37:19 · Speaker 1

Okay this is the noise contrasive estimator okay

### 00:37:36 · Speaker 1

Okay Now

### 00:37:41 · Speaker 1

are multiple okay so now there are multiple claims that we should make okay now the first claim that we do and show is the following claim one is that

### 00:37:52 · Speaker 1

J t of theta

### 00:37:57 · Speaker 1

But we do it the other way now just a second ah let me just think how to best present this

### 00:38:35 · Speaker 1

Okay, so maybe I'll tell you this and then, okay, client one is J theta of theta, okay, J t of theta, the noise contrastive objective. Before we move on, let me just tell you this. See, this J theta can be computed, right? Suppose you have H theta as a neural network, J theta can be computed and you can actually backpropagate through that neural network to find theta. So basically what we will do is

### 00:39:03 · Speaker 1

Represent J theta using the neural network okay and find your theta star as the minimizer

### 00:39:13 · Speaker 1

Off

### 00:39:15 · Speaker 1

objective function over theta

### 00:39:19 · Speaker 1

We can do this, we can solve this optimization problem. So this theta star we get is the NCE estimate for data. Now the question that we should ask now is why should this theta star or rather why solving this object optimization problem lead us to, okay, so let me write it down. So question.

### 00:39:46 · Speaker 1

Why is J T D?

### 00:39:53 · Speaker 1

Estimator

### 00:39:57 · Speaker 1

Stimulator

### 00:40:01 · Speaker 1

for px okay so now you remember that what we actually need is an estimate for px is it good what we are trying to do is learn the underlying distribution px that is our goal now i somehow define some objective function right that uh that that we would like to solve the question is why would solving this objective function lead to a good estimate for px are we good so far let me repeat what we did so we are given

### 00:40:31 · Speaker 1

some data okay uh yeah we should mind here we are we are given some data and we define another uh distribution called the noise distribution from which we know how to draw samples we draw some we draw equal amount also you should observe that the dimensionality of of x okay is the same as the dimensionality of n so noise and the data both have the same dimensions here so we draw n

### 00:41:01 · Speaker 1

noise samples okay and we define an estimator or an objective function that would involve the data samples xt and the noise samples nt okay and there is another function h theta and h theta is is approximated using the neural network and once we use this objective function so now what is happening actually is that there is a neural network okay and this neural network will either take x or n as

### 00:41:31 · Speaker 1

input

### 00:41:33 · Speaker 1

and give you 1 or 0 as the output correct

### 00:41:45 · Speaker 1

will give 1 or 0 as input right I mean this is our h theta function right. Now the and what is the objective objective that we are using this j theta here.

### 00:41:57 · Speaker 1

Now the question is why should solving the claim that we are making here is that if we do this then we would implicitly learn in PX

### 00:42:11 · Speaker 1

Is the story clear so far? Now we should see why doing solving this sort of an objective using this technique should give us should implicitly estimate px that is what we are going to answer now. But is the is the is the story clear so far what we are trying to do?

### 00:42:36 · Speaker 4

Yes only DN we're not sure how it is

### 00:42:40 · Speaker 1

Only what?

### 00:42:41 · Speaker 4

DN DN

### 00:42:44 · Speaker 1

It is it is yeah it is some distribution yeah it is totally random it is some distribution that is not px so we will

### 00:42:46 · Speaker 4

Code to this action

### 00:42:52 · Speaker 1

It does not

### 00:42:54 · Speaker 1

So Pn is just a distribution that is not the same as Px

### 00:43:03 · Speaker 2

So if the noise is input

### 00:43:03 · Speaker 1

Are there any noises in

### 00:43:05 · Speaker 2

They're not

### 00:43:06 · Speaker 4

Theta will return a zero.

### 00:43:08 · Speaker 1

Let's see let's let's see what it returns okay

### 00:43:08 · Speaker 4

Look at the seat

### 00:43:12 · Speaker 1

But yeah it's in for now it's simply a function from uh the data or noise space to 0 1

### 00:43:34 · Speaker 1

Alright is that okay

### 00:43:37 · Speaker 1

Okay, so let us see some properties of this estimator now. What is this estimator actually is doing and why should it get the why should it estimate the underlying distribution? Okay, now let us look at the

### 00:43:53 · Speaker 1

properties of the

### 00:43:57 · Speaker 1

NC estimator so this is called the NC estimator okay

### 00:44:07 · Speaker 1

The first one which is

### 00:44:11 · Speaker 1

You will see just

### 00:44:14 · Speaker 1

What end is that

### 00:44:18 · Speaker 1

J theta

### 00:44:27 · Speaker 1

is equivalent to

### 00:44:36 · Speaker 1

Solving the

### 00:44:40 · Speaker 1

binary classification problem

### 00:44:52 · Speaker 1

We're green

### 00:44:54 · Speaker 1

The sample so

### 00:45:01 · Speaker 1

and this is the first property what we are saying is that this complicated looking or rather this estimator that we have is nothing but solving the binary classification problem between the samples of P and P . So, let us look at why this is the case. Now,

### 00:45:29 · Speaker 1

Creator

### 00:45:31 · Speaker 1

Supervised data set

### 00:45:38 · Speaker 1

supervised data set combining

### 00:45:45 · Speaker 1

Combining D and DN okay

### 00:45:49 · Speaker 1

As follows

### 00:45:54 · Speaker 1

Let's call it some S the new data set supervised data set. Now that has samples like this you have u comma

### 00:46:04 · Speaker 1

Let's call that u1 comma p1

### 00:46:09 · Speaker 1

one comma t one

### 00:46:13 · Speaker 1

U2 over T2

### 00:46:19 · Speaker 1

u 2 t comma t 2 t because there are t samples of noise and t samples of data we are combining them both okay. Now how are we defining this? Now t i is equal to 1 if u i comes from x i

### 00:46:40 · Speaker 1

And T i is equal to zero

### 00:46:44 · Speaker 1

UI is from Y and I

### 00:46:47 · Speaker 1

Do you understand what we did?

### 00:46:58 · Speaker 1

What did we do? We just created so that we had the t samples of noise and t samples of data. We combined them both and created a data set such that whenever we have data samples we gave it one label and whenever we have noise samples we gave that another label. Is that alright?

### 00:47:26 · Speaker 1

Are you dead

### 00:47:35 · Speaker 1

Now what we do is the following first step

### 00:47:41 · Speaker 1

From the above

### 00:47:47 · Speaker 1

We have

### 00:47:52 · Speaker 1

What is the posterior of u given t equal to 1 what is this equal to

### 00:48:02 · Speaker 2

Data

### 00:48:04 · Speaker 1

This is Px, correct? Yeah, good. So now the distribution P.

### 00:48:10 · Speaker 1

of u given t equal to 0 is p n

### 00:48:17 · Speaker 1

E of

### 00:48:20 · Speaker 1

equal to one is equal to

### 00:48:24 · Speaker 1

What about the priors t equal to 0, both of them are equal to half because we have t samples of data and t samples of noise. Correct? Now with this, let us find

### 00:48:40 · Speaker 1

The posterior

### 00:48:44 · Speaker 1

Procedure of labels

### 00:48:48 · Speaker 1

So what are labels here labels are t correct given data u

### 00:48:59 · Speaker 1

What is this which is probability of p equal to 1 given u

### 00:49:06 · Speaker 1

What does this equal to is equal to p of u given t equal to 1 divided by

### 00:49:15 · Speaker 1

P of u given t equal to 0 times P of t equal to 0 plus

### 00:49:27 · Speaker 1

P of u given t equal to one plus P of sorry into

### 00:49:42 · Speaker 1

equal to one here you have p

### 00:49:51 · Speaker 1

Just open it

### 00:49:51 · Speaker 2

Word one

### 00:49:53 · Speaker 1

E of t equal to one no

### 00:49:58 · Speaker 1

This is Bayes' law, right? Now because all the priors are equal, we can just cancel the priors. All of these are half. Just cancel them. This is equal to P of U given T equal to 1, which is

### 00:50:13 · Speaker 1

Beads

### 00:50:15 · Speaker 1

divided by

### 00:50:18 · Speaker 1

Pn plus Px o what is this is the posterior of

### 00:50:23 · Speaker 1

e equal to one given u is given by this

### 00:50:27 · Speaker 1

So it'll be right

### 00:50:34 · Speaker 1

Are we good so far

### 00:50:42 · Speaker 1

Now it's actually called the optimal base classifier between the samples of these two

### 00:51:01 · Speaker 1

which decides upon the ratios of posteriors ok, ratios of class conditional densities ok. Now, suppose

### 00:51:18 · Speaker 1

We model see in all classifiers what do we do we model the posterior of the label given data right using a neural network parametric function

### 00:51:37 · Speaker 1

parametric function h theta of u

### 00:51:42 · Speaker 1

Right. So, what is happening? We are modeling P of t equal to 1 given u using some parametric function. See, this is exactly what we do in all supervised learning, isn't it?

### 00:51:55 · Speaker 1

We model that using some parameterized function at state of u which can be a neural network

### 00:52:01 · Speaker 1

Okay now

### 00:52:06 · Speaker 1

given you

### 00:52:10 · Speaker 1

Can somebody tell me what sort of a random variable T given U is? What is the the what is the form of T given U?

### 00:52:20 · Speaker 2

Indicator random variable

### 00:52:21 · Speaker 1

Yeah it's yeah indicator random variable all binary classification I mean all binary random variables right they are

### 00:52:32 · Speaker 1

is a Bernoulli random variable also indicate random variable

### 00:52:39 · Speaker 1

What is a Bernoulli random variable? Bernoulli random variable is a random variable that takes one of two values with probability p and 1 minus p. Coin toss is one example, okay. It is a Bernoulli random variable with

### 00:52:53 · Speaker 1

the parameter

### 00:52:59 · Speaker 1

h theta h theta of u, isn't it? I mean h theta of u is the success probability of this Bernoulli random variable t given u, okay? That is what it is. Now

### 00:53:11 · Speaker 1

Suppose we want to find the set theta of u by finding out the I mean by maximizing the likelihood. So now let's write the maximum likelihood estimate.

### 00:53:24 · Speaker 2

So how is this parameter h theta of u

### 00:53:28 · Speaker 1

See that is what we have done no this h we have modeled p of t t equal to 1 given u using a parametric function. So this h theta of u is giving you that probability of t being equal to 1 given u.

### 00:53:46 · Speaker 1

In fact, right all binary classifiers does the same thing. All binary classifiers what do they do? The output of it is actually the estimate for the success probability of a Bernoulli random variable which is the conditional random variable of label given data, correct?

### 00:54:06 · Speaker 1

Okay so let us look at the ML estimate maximum likelihood estimate for this Bernoulli random variable t given u

### 00:54:14 · Speaker 1

How does that look like

### 00:54:19 · Speaker 1

Likelihood

### 00:54:24 · Speaker 1

likelihood function L theta for a Bernoulli random variable in fact the log likelihood

### 00:54:40 · Speaker 1

for T given U

### 00:54:43 · Speaker 1

Call it L theta

### 00:54:47 · Speaker 1

can be expressed as follows

### 00:54:57 · Speaker 1

So p theta

### 00:55:00 · Speaker 1

is equal to

### 00:55:04 · Speaker 1

We have a log of products. What is the log like to do we know that no log of

### 00:55:12 · Speaker 1

We too dog

### 00:55:15 · Speaker 1

Excuse me

### 00:55:24 · Speaker 1

Mm hold on that test

### 00:55:37 · Speaker 1

Oligotrophic function, it is sum of log of

### 00:55:45 · Speaker 1

Each heat of it say this is the definition of log likelihood no or i

### 00:55:54 · Speaker 1

The bit that has t here i is the sampling index

### 00:56:04 · Speaker 1

In the case of Bernoulli random variable what is p theta

### 00:56:15 · Speaker 1

P theta of the variable that we are looking at is P given U

### 00:56:23 · Speaker 1

So what is the distribution of a Bernoulli random variable

### 00:56:33 · Speaker 1

If you write that as an indicator random variable then it is

### 00:56:41 · Speaker 1

the power off

### 00:56:46 · Speaker 1

or rather write that as uh

### 00:57:02 · Speaker 1

when t equal to zero

### 00:57:12 · Speaker 1

product of these two

### 00:57:14 · Speaker 2

it is p to the power t plus 1 minus p to the power 1 minus t

### 00:57:21 · Speaker 1

It's theta right there that is what it is so you have

### 00:57:25 · Speaker 1

The distribution of Bernoulli random variable is given by.

### 00:57:33 · Speaker 1

The success probability is h theta no which is h theta of u to the power d

### 00:57:41 · Speaker 1

1 minus h theta to the power 1 minus t. This is the definition of a likelihood of a Bernoulli random variable. So, just substitute this here. So, log likelihood will be equal to sum of

### 00:57:56 · Speaker 1

What I we have

### 00:57:59 · Speaker 1

P times log of

### 00:58:04 · Speaker 1

H theta of u

### 00:58:07 · Speaker 1

Less

### 00:58:13 · Speaker 1

1 minus t times log of

### 00:58:16 · Speaker 1

1 minus h theta of u

### 00:58:21 · Speaker 1

Now if I split this i into indices where t equal whenever t equal to 1 this will become log of

### 00:58:30 · Speaker 1

theta of xi right because whenever t equal to 1 we have xi as the data point whenever t equal to 0 we have it to be n so this is log of 1 minus h theta of ni

### 00:58:52 · Speaker 1

etc. So now what did we what is this equal to this is actually equal to 2 times 2 p times

### 00:59:01 · Speaker 1

J3 of the J Jt of theta which is our NCE estimate

### 00:59:14 · Speaker 1

Right, so what did we show so far notwithstanding the math is that we showed that J theta is equivalent to solving a binary classification problem between the samples of P x and P theta. That is what we showed so far. How did we do that?

### 00:59:30 · Speaker 1

We first created a supervised data set where two classes were created, one for the noise and one for the data. And we looked at the optimal base classifier as the estimator of the posterior of the labels given data.

### 00:59:45 · Speaker 1

And we model that as a binary Bernoulli random variable using a parametric function h theta and we just simply obtained the maximum likelihood estimate for the posterior which turned out to be simply the NC estimate.

### 00:59:59 · Speaker 1

Then what are we saying the summary is that

### 01:00:09 · Speaker 1

NCE is a binary classifier

### 01:00:19 · Speaker 1

What do you mean?

### 01:00:22 · Speaker 1

These samples of

### 01:00:27 · Speaker 1

X and P theta

### 01:00:31 · Speaker 1

Is this i is it alright

### 01:00:40 · Speaker 1

Any questions on this

### 01:01:14 · Speaker 1

Okay

### 01:01:16 · Speaker 1

So, this is good. So, what we are actually doing by in noise contrastive estimation is that given data we just define some noise distribution. We take samples from some noise distribution that is not the data distribution and trying to learn to classify between them.

### 01:01:37 · Speaker 2

So so but somehow it seems the

### 01:01:39 · Speaker 4

This depends on how well we give it the noise

### 01:01:44 · Speaker 4

So how do we ensure that the entire I mean like uh

### 01:01:49 · Speaker 4

So how big is non data distribution? Like it is the entire universe, right? What can we do?

### 01:01:54 · Speaker 1

Yes, that is good, that is a good question, that is a good question, we will answer that, we will answer that eventually in this class. In fact, I mean to

### 01:02:03 · Speaker 1

Not to make you wait, see the point is it's very difficult to come up with that noise distribution and that is why you might have heard this term called hard negative mining, right? In contrastive learning or self-supervised learning techniques. There is this term called hard negative mining.

### 01:02:23 · Speaker 1

Yeah, so that is actually this. How do you sample P and is a question that people have asked. We will discuss that briefly later. Yeah, but what I wanted to convey was this. NCE is a binary classifier between these two samples. So not P, C, T, sorry, this is P and

### 01:02:46 · Speaker 1

Yeah okay

### 01:02:50 · Speaker 1

That is what it is. Okay. So now, okay, fine. You just let us classify between the samples of the data distribution and some random distribution. Now what? Right. Now comes the most interesting part. What we would show is that solving this, you know, J theta attains its optimal, okay, only when this H theta implicitly estimates the underlying distribution is what we will show.

### 01:03:20 · Speaker 1

Uh that is something that we will uh uh show

### 01:03:29 · Speaker 1

I was thinking should I have to do it now or just take a break and come back and do it?

### 01:03:40 · Speaker 1

Shall we take a break some fifteen twenty minutes break and come back

### 01:03:48 · Speaker 1

Okay, I think we've been uh getting quizzed and all that. Let's take some break. So this is 1050, 1053. Let's uh get back at 1115.

### 01:04:01 · Speaker 1

And continue from here see you in fifteen twenty minutes

### 01:27:18 · Speaker 1

I'll get a zoom

### 01:27:23 · Speaker 4

Yes so we can hear you

### 01:27:26 · Speaker 1

Shall we continue

### 01:27:33 · Speaker 1

I was just reading some news Do you know the name of this Elon Musk's son

### 01:27:43 · Speaker 1

People don't create

### 01:27:44 · Speaker 2

I'm a glorzzer

### 01:27:47 · Speaker 1

No it's not code I mean it's

### 01:27:51 · Speaker 1

Some X A A 12 or something like that

### 01:27:56 · Speaker 1

No liquid

### 01:27:59 · Speaker 1

Imagine the plight of that kid when he goes to school

### 01:28:07 · Speaker 1

actually not very a big fan of these complicated I mean even it's today you know young parents in India they are also doing these weird things you know they name see because naming happens only once in lifetime and they want it to be exotic they name children with all kinds of random things you know I I keep thinking especially when these kids grow to be like older adults how do you call them with such weird names

### 01:28:38 · Speaker 4

They'll be traumatized that's what I am

### 01:28:39 · Speaker 1

So

### 01:28:42 · Speaker 1

And so many you know names that mean nothing simply they'll see somewhere and they'll say that it's a Sanskrit name I mean studied you know Sanskrit to identify that most of these names are not Sanskrit so what

### 01:28:59 · Speaker 4

Usually in India people base the names on like movies and all those places but this pyramid kind of name is A A 12 some 1 to 14 I don't know what it is.

### 01:29:15 · Speaker 1

for business okay let's get back uh yeah so we were looking at the noise contrastive estimation and we saw that it's a binary classifier between samples of two distributions

### 01:29:28 · Speaker 1

Okay, now we will continue. So now, okay, finally the question is, finally do a binary classification between these two distributions. What's great about it, right? There is this very nice result that would say the following. So property two of in noise contrastive estimation is

### 01:29:52 · Speaker 1

You have j theta

### 01:29:56 · Speaker 1

be equal to

### 01:30:00 · Speaker 1

1 by 2t

### 01:30:03 · Speaker 1

Let's uh

### 01:30:06 · Speaker 1

Log off

### 01:30:09 · Speaker 1

H theta on X

### 01:30:13 · Speaker 1

Yes

### 01:30:19 · Speaker 1

Logos

### 01:30:22 · Speaker 1

1 minus is theta evaluated at n t right this is what the loss function was

### 01:30:31 · Speaker 1

Now large large numbers

### 01:30:44 · Speaker 1

I'm not sure

### 01:30:53 · Speaker 1

J theta is approximately equal to some J tilde of theta

### 01:31:00 · Speaker 1

J tilde of J tilde of theta is given by the following it is half

### 01:31:12 · Speaker 1

expectation of

### 01:31:15 · Speaker 1

Log off

### 01:31:21 · Speaker 1

It's theta evaluated at x

### 01:31:30 · Speaker 1

Lago

### 01:31:32 · Speaker 1

1 minus h theta evaluated at n

### 01:31:39 · Speaker 1

And this expectation is over the joint distribution of P X and N

### 01:31:46 · Speaker 1

This is what the law of large number says

### 01:31:58 · Speaker 1

Okay, this we know, right? I mean, if you have samples from distributions, then expectation can be approximated using sample averages. We inverted that, meaning we said that this was a, this, I mean, this was

### 01:32:13 · Speaker 1

A sample average right whatever we had in J theta was a sample average we just converted that into t equal to 1 to 2t converted that into

### 01:32:23 · Speaker 1

Expectation

### 01:32:31 · Speaker 1

Suppose

### 01:32:51 · Speaker 1

given by

### 01:32:54 · Speaker 1

Log off

### 01:33:27 · Speaker 1

Let P theta of X denote

### 01:33:34 · Speaker 1

each distribution

### 01:33:43 · Speaker 1

being estimated

### 01:33:49 · Speaker 1

We are NCE. We solve this optimization problem. We are implicitly imposing a distribution on the model. Let's call that as P theta.

### 01:34:18 · Speaker 1

Let f be equal to log of

### 01:34:26 · Speaker 1

ETI topics

### 01:34:30 · Speaker 1

Okay now what can be shown us that I will just give the proof for the want of time J theta can be shown to be equal to half

### 01:34:40 · Speaker 1

of expected value of log of

### 01:34:45 · Speaker 1

Odd

### 01:34:48 · Speaker 1

Perfect

### 01:34:50 · Speaker 1

Minus

### 01:34:52 · Speaker 1

Logos

### 01:34:54 · Speaker 1

P and of X

### 01:35:02 · Speaker 1

expected half times the expected value of log of

### 01:35:07 · Speaker 1

1 minus r times

### 01:35:13 · Speaker 1

f of n minus log of

### 01:35:19 · Speaker 1

The n evaluated at n

### 01:35:26 · Speaker 1

So this equivalence I will not show, I mean this is only an algebraic manipulation. What can be shown is that this j theta can be written equivalently this way, where r, something that we don't know, where r is simply the logistic function, r of k is 1 by 1 plus e power minus k, r is the logistic function. When it involves just rewriting the equation,

### 01:35:57 · Speaker 1

Rewriting the equation of J in terms of what we know. So, why is this important? So, again I will state a theorem without proof which again can be solved easily. I will tell you how to do it proved easily. So, theorem is that

### 01:36:15 · Speaker 1

So with this what happens is your J theta now can be written as a function of F no

### 01:36:24 · Speaker 1

Because we yeah question

### 01:36:27 · Speaker 2

So in the first term this r for this function r the argument is just fx or fx minus log pn of x

### 01:36:35 · Speaker 1

So it is R of f of x here. So R is a logistic sigmoid, right? So it is R of f of x, right? And R of f of n minus log p n, n into n, correct? Yeah, the bracket was missing.

### 01:36:48 · Speaker 1

So, now you represent this entire see what did we do I mean we represented the ah ah the log likelihood of the underlying distribution using some function f. So, I mean strictly speaking this is f theta right and we present we represented the noise contrast f estimator in terms of f theta.

### 01:37:06 · Speaker 1

Now this theorem which is the most powerful theorem that would say that the

### 01:37:15 · Speaker 1

Optimal value

### 01:37:22 · Speaker 1

of f theta

### 01:37:26 · Speaker 1

That would

### 01:37:33 · Speaker 1

Optimize

### 01:37:36 · Speaker 1

j tilde of theta

### 01:37:40 · Speaker 1

is such

### 01:37:48 · Speaker 1

Next star

### 01:37:50 · Speaker 1

is equal to log of p x of x

### 01:37:56 · Speaker 1

This is the most important result. Now the question that we are asking is the following. I will tell you how we would get it that way. The question that we are asking is that what would be the F star? That would

### 01:38:15 · Speaker 1

maximize this objective or minimize this minimize the negative of this objective is the question right because the only variable here is f no we are searching for an f okay that would maximize this objective. Now what can be shown is that irrespective of what n you are using

### 01:38:35 · Speaker 1

that f which is maximizing the objective j theta non-scorer estimator j theta theta is the one for which the f happens to be the log of log likelihood of the true underlying data distribution. Now, how do we get that? So, we get that by writing this entire thing in terms of double integral right this expectation will be written in terms of the double integral of this thing times p x into n assuming that noise and data are independent you write these as

### 01:39:05 · Speaker 1

channels over BX and BN okay

### 01:39:12 · Speaker 1

V x V n and then you differentiate this integral with respect to f and put it to 0, what you will get is that the optimal f is going to be log of P x that is what it is. I mean you need a bit of variational calculus to show that which is beyond scope of this particular course and that is why I am skipping the proof. But yeah, but the result is that

### 01:39:34 · Speaker 1

The optimal value for the noise contrastive estimator is when the log of the distribution that it is that it is implicitly imposing on the model is equal to the log of the likelihood of the underlying data distribution.

### 01:39:54 · Speaker 1

There is a very powerful result. So now the summary or the take home message from this what is the consequence of this is summary yes.

### 01:40:06 · Speaker 1

One can use or rather

### 01:40:10 · Speaker 1

Solving

### 01:40:13 · Speaker 1

The classification problem in DNC estimate

### 01:40:25 · Speaker 1

Between Px and Pn

### 01:40:29 · Speaker 1

Yeah

### 01:40:32 · Speaker 1

Well implicitly

### 01:40:38 · Speaker 1

Non

### 01:40:40 · Speaker 1

The underlying distribution P theta

### 01:40:52 · Speaker 1

distribution P x. This is the most important result. So, you understood right. So, what we are doing is suppose we have

### 01:41:01 · Speaker 1

A classifier that is built

### 01:41:04 · Speaker 1

Let us say that we take x power n to this. This is your h theta and this will finally give you 1 or 0. Okay. Trying this. What we are saying is if you take the intermediate representations of this. Okay. So let us call this as

### 01:41:23 · Speaker 1

F theta of x because as you saw what the h theta

### 01:41:30 · Speaker 1

was the logistic sigmoid of f theta of x. So whatever you get before the final layer is the logistic sigmoid. So whatever you get before the the final layer, penultimate layer of the logics is what you call as f theta. And we know that f theta, the optimal f theta is log of f of x.

### 01:41:52 · Speaker 1

right and what we can use that we can write Z

### 01:41:57 · Speaker 1

be equal to f theta of x

### 01:42:03 · Speaker 1

The features are embeddings or representations

### 01:42:12 · Speaker 1

So, this is the result. So, what we are saying is that you do not have to do anything all you need to do is that if you are given some data ok define some noise sample from it and learn to classify between the data and the noise. So, now if you do that then you are implicitly learning the underlying distribution take the logics of that classifier and use that use those as features. See this is the this is what is called as the contrastive learning.

### 01:42:45 · Speaker 1

of self supervised learning. So, what is the self supervision part here? Remember that we defined a pseudo task now the pseudo task the pretext task that we defined here is that of classification right.

### 01:42:58 · Speaker 1

This is the fundamental bedrock of contrastive versus supervised learning, okay, where it comes from noise contrastive estimation that would say that solving an optimization problem which turns out to be classification between the data distribution and some noise test distribution will implicitly learn the underlying data distribution up to a constant.

### 01:43:28 · Speaker 1

Any questions here? See this is the idea I mean everything else that came after this no it's only as improvisation over

### 01:43:36 · Speaker 1

this idea but this is the fundamental idea actually

### 01:43:43 · Speaker 1

Any questions here?

### 01:44:03 · Speaker 1

Hello are you

### 01:44:06 · Speaker 1

Is it there Am I audible

### 01:44:09 · Speaker 4

Yes it is you would

### 01:44:12 · Speaker 1

This is a very powerful result, right? I mean, it is saying that, I mean, all you need is to simply classify between the data distribution and some noise distribution. And if you do it, please note that these results are asymptotic in the sense that this will give you an estimate for the log likelihood of the underlying data distribution only if you have enough samples. Now, as Vivek was asking before the break, now how do you know what noise distribution would help it?

### 01:44:42 · Speaker 1

what can be shown while doing this proof is that the larger is the divergence between px and pn the better it is to estimate the underlying data distribution okay now getting those noise samples is is very important now that is why we have so many methods on how do you define the hard negatives how do you how do you come up with the negative samples okay but yeah so this is the fundamental idea of why should solving a pretext task okay or a

### 01:45:12 · Speaker 1

pseudo label task

### 01:45:15 · Speaker 1

could help you in learning the data distribution. Please note that this is this entire thing is non generative in the sense that you can't sample points from PX from this right. Is this clear? This is not generative right?

### 01:45:36 · Speaker 1

not able to sample from PX

### 01:45:43 · Speaker 1

It's a non generative

### 01:45:53 · Speaker 2

if we are not able to generate some samples then how can we say that we have learnt the original data distribution

### 01:46:01 · Speaker 1

And that's what we saw so far right

### 01:46:04 · Speaker 1

See what we showed was that see we are not able to sample from this thing but

### 01:46:11 · Speaker 1

Solving this classification task, what we are getting is at the penultimate layer of this classifier, we are learning the log of the underlying distribution is what we just showed, isn't it? The entire today's class was on that.

### 01:46:24 · Speaker 2

So

### 01:46:26 · Speaker 1

So we can learn the underlying data distribution even without sampling from a distribution is what we should

### 01:46:34 · Speaker 4

So from this if we connect it to a sampler it can ideally sample it right I mean we got the distribution right data

### 01:46:43 · Speaker 1

So we didn't know not explicitly right. See given an x it will see what is this penultimate layer giving you given an x as an input it is giving you log of px of x that's all right. It is not telling you what px of x is.

### 01:47:00 · Speaker 4

So there is no way to

### 01:47:02 · Speaker 1

There is no way, absolutely no way, no. But what is, what is important is that if you know log of px of x for all samples, then you know everything about the data. That is why these features are powerful.

### 01:47:17 · Speaker 1

See why do you think bird embeddings are so in fact bird also does exactly this thing we will come to that in a while. Why do you think those are so powerful is because if you do this well ok with a large number of samples so that the log large number is is is respected then the the representations or the embeddings that you are getting from this classifier are actually estimating the log likelihood of the data right that is all. So you know everything about the data so you can use it for anything that you want that is the idea but you are not able to sample.

### 01:47:47 · Speaker 1

From here yeah

### 01:47:51 · Speaker 1

Anything else?

### 01:47:55 · Speaker 1

See, compare this with let's say VAE or a diffusion model or a DDIM where you will get embeddings as well as ability to sample.

### 01:48:13 · Speaker 1

So this uh

### 01:48:18 · Speaker 1

generative pre-training, GPT. So that is an example where you have the embeddings and also the generative ability. We will look at GPT probably in the next class, right?

### 01:48:31 · Speaker 1

where you generate the embeddings right or rather find an embedding space representation and also learn to sample implicitly from I mean together just like a diffusion model or a VAE in a GAN right for instance in a naive GAN

### 01:48:48 · Speaker 1

Can somebody tell me what abilities does it have

### 01:48:57 · Speaker 1

It can generate it can generate it can't find out D it can't do posterior inference

### 01:48:57 · Speaker 4

Yeah

### 01:49:02 · Speaker 1

But we did see some examples, right? In your assignment I had asked you to, did I ask you to do that or not? Like build a classifier or an inverter over the generator and solve a reconstruction task over the latent space. Did I ask you to do that?

### 01:49:23 · Speaker 1

So, you have done that right. So, now you can you can improvise GAN to to to do an inversion or a embedding extraction as well ok.

### 01:49:33 · Speaker 1

All right service

### 01:49:36 · Speaker 4

So so in this case so this f theta for this discriminant will it be a scalar single number

### 01:49:46 · Speaker 1

You're supposed to get that

### 01:49:48 · Speaker 2

getting only one output one or zero so

### 01:49:52 · Speaker 1

Yeah, that's a very good question. Yeah, it will be scalar and that's why people said, okay, let's move away from this. Why only do a binary classification problem? Let us solve an n-class classification problem, which is what is called as info-NC.

### 01:50:09 · Speaker 1

Okay where the idea is to extend and see

### 01:50:18 · Speaker 1

Whoa

### 01:50:21 · Speaker 1

Multi class classification study

### 01:50:27 · Speaker 2

so that we can get a vector of embeddings

### 01:50:36 · Speaker 1

So what InfoNCD does is that it is simply a multi class classification problem so given a data point

### 01:50:48 · Speaker 1

data point x i ok defined

### 01:50:57 · Speaker 1

Okay

### 01:51:02 · Speaker 1

ICE examples or IC examples

### 01:51:18 · Speaker 1

from PN and

### 01:51:22 · Speaker 1

solve a k class classification problem

### 01:51:33 · Speaker 1

between XI in fact it's actually K plus 1 class classification problem and K negative samples noisy samples

### 01:52:00 · Speaker 1

Okay, this is what noise, sorry, InfoNCE does. The paper's name is Representation Learning with Contrastive Predicting Coding. Okay, I mean it's nothing but extension of noise contrastive estimation.

### 01:52:15 · Speaker 1

for uh

### 01:52:19 · Speaker 1

key class classification problem so let me

### 01:52:24 · Speaker 1

I thought just show you show you the paper give me a second

### 01:53:04 · Speaker 1

Let me share my screen and show you

### 01:53:09 · Speaker 1

Here's Green

### 01:53:19 · Speaker 1

Did you see my screen?

### 01:53:25 · Speaker 1

But anyway this is the

### 01:53:29 · Speaker 1

This is the paper on noise contrast estimation. It's a very, very nice paper. Okay. Very old, but this is the one that noise contrast estimation, a new estimation principle for unnormalized statistical models. Please look at this paper. It's very good. Okay. Like 2010 it appeared. Okay. But it was just sort of buried because this could not be scaled to higher dimensions because then the neural networks were not very powerful. It's a very nice paper. Okay. Have a look at it. Then came the

### 01:54:01 · Speaker 1

Info NC paper 2019 which is called representation learning with contrastive predicting coding. So where what they do is just extend NC for a K class classification setting.

### 01:54:17 · Speaker 1

Given a set X of n random samples containing one positive samples from the distribution that you want to estimate and n minus one negative samples from the proposal distribution, right? So, yeah. So, if you take a set of n samples, okay, one of them is the so-called positive sample or the data sample from the data distribution and there are n minus one negative examples. You define the NCE loss as the negative of the expected loss of expected value

### 01:54:47 · Speaker 1

the log of this thing. So, what is this if you look at it this is nothing but the softmax okay where fk will give you the the kth output of the softmax in the neural network okay and it is summed over all possible other samples.

### 01:55:05 · Speaker 1

This is all right. This is the infoency loss. Now, what

### 01:55:12 · Speaker 1

can be shown just like the NCE counterpart is that optimizing the optimal value of this fk is the one that gives you the log of this underlying data distribution. It's just simple extension of NCE ok for a k class classification problem.

### 01:55:30 · Speaker 1

Is this okay

### 01:55:32 · Speaker 1

Now this came in 2019 and this was extended to the contrastive learning. This was Hinton's paper, right? This was well celebrated. This is called SIMCLR, okay? It stands for Simple Framework for Contrastive Learning of Visual Representations. Now look at this graph. What they show is the following that if you take the ImageNet top one accuracy, you take the representations that are

### 01:56:02 · Speaker 1

given by the SIMCLR and do a fine tuning. So now what do you do with the representations? You take those representations and if you want to solve a classification task just fine tune another classifier using those representations that is how you use it. It was shown that it just beats all the existing state of the art. Okay. On yeah. The fully supervised is of course the best that you can get. Right. But even with like very less number of parameters on

### 01:56:32 · Speaker 1

the fine tuning of the fine tuning network you can get a pretty comparable result is what was shown. Now what does this do? This is nothing but infoency look at this expression. So, this loss function that is used in SimSLR is nothing but the infoency loss write it as the dot product between. So, what they have done is look at the

### 01:56:58 · Speaker 1

Info and sheet paper they write this FK right as a dot product

### 01:57:06 · Speaker 1

between the representations for the positive sample and the negative sample and this is just the normalization constant

### 01:57:16 · Speaker 1

So what is done is the following that given an image

### 01:57:22 · Speaker 1

image they create multiple augmentations of the image by doing these kinds of things crop and resize and then you have color distortions and you do you add some Gaussian noise and make blur it out and you do Sobel filtering and extract the edge and all that okay now what they do is given this particular image all of these counterparts are taken to be the positive

### 01:57:47 · Speaker 1

positive counterparts of this particular image okay and then what they do is whenever the network sees these augmentations they want the network to output one see think of it like

### 01:58:01 · Speaker 1

solving a k class classification problem where the original image and all of these augmentations are taken to be of the same class okay and all the other images that does not correspond to this original image is taken to be the

### 01:58:18 · Speaker 1

from the other classes and you solve the K class classification problem

### 01:58:27 · Speaker 1

Does it make sense

### 01:58:35 · Speaker 3

Yes sure

### 01:58:36 · Speaker 1

Any questions on this

### 01:58:40 · Speaker 4

So this one will result in a k plus 1 vector outright

### 01:58:48 · Speaker 4

I mean the the the the the dimension of the

### 01:58:50 · Speaker 1

Not not necessarily the representative see the way no no the way they have done it

### 01:58:51 · Speaker 4

that our presentation

### 01:58:55 · Speaker 1

they have taken the the penultimate layer to be of some d dimensions. Now, the loss function will take those d dimensional vectors and compute the dot product between those representations here. That is how they implement this f k.

### 01:59:16 · Speaker 1

So you can you can actually customize it

### 01:59:20 · Speaker 1

because the the I mean they don't implement it as cross entropy they implement it as the dot product between the representations that have been gotten between these two

### 01:59:37 · Speaker 1

Any other question on this

### 01:59:41 · Speaker 1

At C, the fundamental idea is that of the NCE. Now, improvisations have been done where instead of solving a

### 01:59:54 · Speaker 1

binary classification problem you solve a k class classification problem. Now, you represent the objective of the k class classification problem in terms of

### 02:00:05 · Speaker 1

in terms of dot products right or inner products between the pre logit layers okay that is proportional to of course the binary cross I mean categorical cross entropy right I mean that is what SIMCLR does.

### 02:00:25 · Speaker 1

Is this alright

### 02:00:31 · Speaker 4

Oh yes sir but uh there is no noise in

### 02:00:34 · Speaker 3

Hold here now right

### 02:00:35 · Speaker 1

Well you can see all the negative samples that you get here right I mean is actually the noise. See if you look at the algorithm what they do is they take one sample okay one data data example okay and create all the augmentations of it and call it the positive example.

### 02:00:58 · Speaker 1

And then what they do is they sample randomly, I'll just show you that

### 02:01:07 · Speaker 1

See here they say that we do not sample negative examples explicitly. Instead given a positive pair we treat the other 2 n minus 1 augmented examples with a mini batch as negative examples. This is the way they define the noise here.

### 02:01:20 · Speaker 4

Okay okay

### 02:01:24 · Speaker 1

But again as I said there are lots of improvisations over it I mean then people came up with something called MOCO right momentum update contrastive encoding yeah

### 02:01:32 · Speaker 4

So what effect does this re actually have this just tries to push away the vectors from each other like if you're going to say the dot product

### 02:01:43 · Speaker 1

So what is what this what does it do is whenever you have the positive pairs it will try to cluster them together whenever they are they are they are negative pairs they will try to push them apart that is what a classifier also does isn't it?

### 02:01:59 · Speaker 3

Right yeah so

### 02:02:00 · Speaker 1

That is exactly what a classifier does. It is trying to cluster the points that are from one category. It is trying to push the points from the other categories away. That's all. Now, what is the intuition? See, I did the math because, I mean, you might have probably known from the course so far is that I, I mean, I get convinced better if I am shown some mathematical guarantees of what's actually happening. But I can give you some intuition also. So, what is actually happening?

### 02:02:30 · Speaker 1

with all these methodologies is that suppose you know how to uh like

### 02:02:39 · Speaker 1

group all these uh all these examples as close to this dog image and the cat image you know how to push the cat image away from this you can't do it as long i mean you can't do it or rather you can do it only if you know understand the semantics of this object called dog isn't it okay see if somebody wants to put this dog image and this cutout dog image into one same category they should know that okay this is actually a cutout

### 02:03:09 · Speaker 1

of this dog isn't it

### 02:03:12 · Speaker 1

Right. So that's the whole point. So now as means you do you recall these uh, uh, these these question types that we we we were having we were having when we were going to school right. One of the question types was this thing called fill in the blanks. Isn't it? Yes. They used to give a give a sentence and used to ask us to fill in the gaps randomly match some of the words and ask them to ask us to fill the gaps. Now you can do it only if you know perfect

### 02:03:42 · Speaker 1

what the semantics are isn't it

### 02:03:46 · Speaker 4

Yes yes

### 02:03:47 · Speaker 1

That's the whole point. In fact, the all these language LLMs today are learned using that technique or this technique only, which is that, yeah, which is the mass reconstruction. So you have data, you mass some parts of it and try to reconstruct it back. So which is nothing but classifying between the data sample and the noise sample.

### 02:04:13 · Speaker 1

Okay, so any other question on this

### 02:04:19 · Speaker 4

So there is a two into n minus one images right? So what is that two indicates here? Is that two augmentations only we do or images?

### 02:04:27 · Speaker 1

No no no no given a an image you take n augmentations

### 02:04:32 · Speaker 1

And you sample another random point

### 02:04:37 · Speaker 1

Okay, so that will make it 2 n minus 1, isn't it? I mean, they count from 0, that's why there are like 2 times n minus 1.

### 02:04:47 · Speaker 1

Basically it's 2n. So you take an image or a data point, you take n augmentations of it and call all of them as positive, right? And then you sample n negative samples from the data set. So that will make it 2n, no? 2 capital N, that's all it is.

### 02:05:05 · Speaker 2

Sir and negative samples here means can you clarify

### 02:05:10 · Speaker 1

You need samples from the noise distribution right

### 02:05:15 · Speaker 2

Yes

### 02:05:16 · Speaker 1

Now what is done is that you take a dog image and you take n augmentation that will give you the positive ones

### 02:05:24 · Speaker 1

You need samples from the noise distribution as well. So what is done is people just sample n random points from the data set itself and call them the samples from the noise.

### 02:05:39 · Speaker 2

from this dog data set itself

### 02:05:41 · Speaker 1

Not dog this data set has all kinds of objects

### 02:05:46 · Speaker 1

This data set has all kinds of objects. So now if you randomly do a sampling from all objects, the other n samples that you have gotten hopefully are not from the dog category. That's a good point that you made. See what happens is these methods, especially SimCLR, has been shown to work well only if you have a very, very large batch size.

### 02:06:08 · Speaker 1

Okay, now why is that the case is because suppose you have like a you have very small batch size when you take when you do a like sampling for something negative sample with n samples with n being very small there is no guarantee that these so called negative examples that you get are not from the doc category isn't it? You do not have control because we have no labels.

### 02:06:35 · Speaker 1

But if you make our batch size to be very very large then

### 02:06:40 · Speaker 1

What happens is if you take if you sample a very large number of samples then most of them will not be from the class that you are considering for this particular example. That's why the SimCLR is known to work only with very large number of examples like very large batch sizes.

### 02:07:01 · Speaker 1

Okay uh questions on this yeah we wait

### 02:07:05 · Speaker 4

So uh one question so is the noise contrastive estimation the same as out of data distribution detection?

### 02:07:15 · Speaker 1

Uh sort of yeah you can you can you can view it as uh like outlier detection actually yeah

### 02:07:24 · Speaker 1

See, if you if you are solving the binary classification problem, yes it is outlier detection. If you are solving the k-class classification problem, then like detecting outliers from multiple distributions. Okay, what is it?

### 02:07:36 · Speaker 4

No so outlier is a very specific case what I mean is something like out of distribution detection which means

### 02:07:44 · Speaker 1

Agreed. Agreed. You want to you you are classifying between the the set of samples samples of the data distribution and everything that is not data. Yes.

### 02:07:45 · Speaker 4

I agree I agree

### 02:07:55 · Speaker 4

Yes yes yes yeah

### 02:07:58 · Speaker 1

See that that's how human beings also learn no if you know how to classify between you know what is important what is not important then

### 02:07:58 · Speaker 4

So

### 02:08:06 · Speaker 1

Then you have learned the tricks of the life that's what they say

### 02:08:18 · Speaker 1

Okay, so let me come back, get back to this. So as I said, there are multiple improvisations over it. So now one question that people ask is, now how do you reduce the batch size in SimCIRR? So one way to do it is that whenever you are sampling from the noise distribution, as Vivek was asking,

### 02:08:38 · Speaker 1

You sample the noise points in such a way

### 02:08:45 · Speaker 1

that they are very very I mean they are they are pretty away in the representation space from the data samples ok. So, this is called hard negative

### 02:08:56 · Speaker 1

Sampling let me just write it down

### 02:09:04 · Speaker 1

Question is like

### 02:09:12 · Speaker 1

How to

### 02:09:14 · Speaker 1

Sample

### 02:09:16 · Speaker 1

Better negative examples or better

### 02:09:21 · Speaker 1

noisy or negative samples

### 02:09:42 · Speaker 1

So now there are this is called hard negative mining

### 02:09:51 · Speaker 1

negative meaning where given a particular sample okay

### 02:09:58 · Speaker 1

How do you make it hard in the sense that how do you ensure that that this negative sample is actually contributing to learning? There are multiple ways. One way to do it is that given a sample, you take all the augmentations of it and call it positive. For the negative samples, you do for every sample that is that you get from the data set. Okay. And please note that for the case of

### 02:10:24 · Speaker 1

for methods like CMCLR the noisy samples are actually the samples from the data set itself that does not correspond to the the argumentations of the given input sample. I hope that that is clear. Is that clear?

### 02:10:42 · Speaker 1

Let me write that down what I mean is in methods like SIMCLR

### 02:10:57 · Speaker 1

the noisy or the negative samples

### 02:11:16 · Speaker 1

the points from the data distribution

### 02:11:25 · Speaker 1

dot r

### 02:11:29 · Speaker 1

not the

### 02:11:33 · Speaker 1

Augmentations

### 02:11:39 · Speaker 1

of the given input sample

### 02:11:46 · Speaker 1

So that way it slightly differs from the NOS contrasted estimation in the sense that the in distribution samples are taken to be the one that that one the taken to be a sample and its augmentations. The outer distribution samples are taken to be a few randomly sampled points from the data set itself.

### 02:12:11 · Speaker 1

So, example is right I mean suppose you have a have an image of a of of a digit 1 then the positive examples are its rotation and the masked version of it and you have the noisy version of it all of these are taken to be the in

### 02:12:30 · Speaker 1

These are positive examples or indistribution samples

### 02:12:36 · Speaker 1

And you take the images of let us say 2, 3, 5 etcetera all these are taken to be negative examples.

### 02:12:50 · Speaker 1

And then you learn to classify between these two in a K class classification setting. So this is also called as the anchor point.

### 02:12:58 · Speaker 1

anchor point or the data point at over interest okay of interest so all the contrastive learning or self supervised learning techniques we would learn to classify between the samples of positive and negative examples

### 02:13:17 · Speaker 1

It's a funny

### 02:13:17 · Speaker 4

So but in this uh current context we do not have the labels right so that's why we don't

### 02:13:21 · Speaker 1

We don't, we don't, we don't. Exactly, exactly. So now, see what might happen, no? Like one particular sample from the same class might creep up here, right? That's why you need a large batch size. That's what I'm saying. So these examples have to be negative enough for this to work because they have to actually come from PN. Now that's why if you have very large batch size then the likelihood of having samples not from the same class or semantic

### 02:13:48 · Speaker 1

Label as that of the anchor point is less the idea.

### 02:13:57 · Speaker 4

You need some kind of balanced data set here right as well

### 02:13:59 · Speaker 1

Uh not balance you need a l yeah I mean you can say balance or you need a lot of negative samples that's all

### 02:14:10 · Speaker 1

Okay now uh

### 02:14:18 · Speaker 1

Any questions so far

### 02:14:21 · Speaker 1

This is shown to be very powerful as I said no, SIMCLR etc. would reduce the the dependence on the supervised I mean labels by a drastic amount of reduction is there. So examples of this approach, contrastive learning approaches in the image space you have some methods like SIMCLR or you have MOCO and there's this thing called JAPA I will talk about it okay.

### 02:14:51 · Speaker 1

the space of NLP all these models such as BERT and

### 02:15:01 · Speaker 1

What is the other thing called it is a world toek

### 02:15:06 · Speaker 1

All these are variants of this NCE and info NCE, okay.

### 02:15:10 · Speaker 4

So how do we click

### 02:15:13 · Speaker 1

Clip is also there but clip is for uh like it's for multi it's for multi uh multi modal data but the idea idea is exactly the same I can add it yeah

### 02:15:19 · Speaker 4

I'm sorry

### 02:15:23 · Speaker 1

I will write it so for speech you have the wave to like for image plus

### 02:15:32 · Speaker 1

Next you have

### 02:15:39 · Speaker 1

What does this clip stand for I keep forgetting that

### 02:15:43 · Speaker 1

Contrastive pre-training for images and languages it that's what it

### 02:15:57 · Speaker 1

Just opening the clip paper

### 02:16:07 · Speaker 2

Contrastive language image pre-training

### 02:16:10 · Speaker 1

Yeah contrastive language image pretraining okay

### 02:16:16 · Speaker 1

That we spoke of clip, no? Maybe I can also talk about it. So, you know how it is done.

### 02:16:23 · Speaker 1

Now that is up

### 02:16:29 · Speaker 1

The objective is to learn

### 02:16:38 · Speaker 1

on the representations or encodings

### 02:16:48 · Speaker 1

jointly

### 02:16:52 · Speaker 1

Between B

### 02:16:56 · Speaker 1

image and text modalities see this can be extended to any multimodal thing okay text modalities

### 02:17:08 · Speaker 1

How is it done you have you take two networks one we call as F theta the other you call as

### 02:17:17 · Speaker 1

G theta

### 02:17:19 · Speaker 1

this is the text encoder and we have the image encoder so this will take text as input this will take images as input

### 02:17:40 · Speaker 1

Okay, what they do is they take, so for this you need to have pairs of images and text, okay, the data that you have is, you have images

### 02:17:52 · Speaker 1

You have an image, comma text that is the kind of data that you have. Okay. Now, uh

### 02:18:01 · Speaker 1

Do you need the pair? I don't think you need the pair

### 02:18:06 · Speaker 4

We need the persons

### 02:18:07 · Speaker 1

Do we

### 02:18:08 · Speaker 4

Yes very much and in very large numbers

### 02:18:12 · Speaker 1

Let me just think about that

### 02:18:21 · Speaker 1

Contrastive pre-training you have the

### 02:18:26 · Speaker 1

done let me just see

### 02:18:33 · Speaker 4

In a given batch there is a set of images and their captions

### 02:18:39 · Speaker 1

You need the corresponding captions also no

### 02:18:41 · Speaker 4

Yes

### 02:18:43 · Speaker 4

And the only thing is in that uh

### 02:18:45 · Speaker 1

Yeah you do need uh pairs

### 02:18:49 · Speaker 4

I mean it has to be a set and in that set whatever belongs to that image that only those dot products should be maximized and all the others should be minimized

### 02:19:01 · Speaker 1

So, what is good is I will tell you yeah. You do the same thing no for every text you get you get and I just yeah what will happen is for text let us say that you get some t1 t2 corresponding to some tn there are embeddings for n possible text and similarly for images suppose there are n images right you get image 1 image 2 up to image n okay. So, you take n embeddings from the

### 02:19:31 · Speaker 1

Uh

### 02:19:38 · Speaker 1

n embeddings from the image encoder n embeddings from the text encoder ok. Then you have a n by n matrix

### 02:19:48 · Speaker 1

embeddings right so this is let's say that this is the text dimension and you have this is as the image dimension

### 02:20:03 · Speaker 1

So what does this tell you this will give you along the diagonal

### 02:20:08 · Speaker 1

This will tell you the the inner product between the image embedding with the corresponding

### 02:20:18 · Speaker 1

Externality, isn't it? Now, what you need is to maximize the

### 02:20:25 · Speaker 1

Inner product

### 02:20:30 · Speaker 1

Rather this itself no is the inner product matrix so let's call this matrix let me write it down hold on

### 02:20:37 · Speaker 1

call this as IP now IP at I comma J is the

### 02:20:46 · Speaker 1

dot product between the ith text embedding and the ith image embedding and the jth text embedding. The objective is to find theta and phi such that

### 02:21:04 · Speaker 1

Maximizes

### 02:21:09 · Speaker 1

diagonal of IP right

### 02:21:24 · Speaker 1

The maximizes this divided by

### 02:21:34 · Speaker 1

and take the sum of all the

### 02:21:44 · Speaker 1

So more all I you have diag of IP divided by

### 02:21:52 · Speaker 1

of diagonal elements of IP that's all. So whenever you get the pair of you get embeddings in such a way that the inner product between the image and the corresponding text is maximized and everything else is minimized. You need zeros here, you need maximum values here that is how we are trying it.

### 02:22:12 · Speaker 1

Now finally after you train this what you can do is you take the image okay and what do you get? What do we need? We we we need a an embedding right corresponding to

### 02:22:30 · Speaker 1

pair of text and image this is how we have done it isn't it now when we want to do uh

### 02:22:41 · Speaker 1

Prediction what do we do

### 02:22:43 · Speaker 1

We take an image and give it to the image encoder, we get the image embedding. Okay. Then what you do is you take

### 02:22:54 · Speaker 1

gen possible candidate text, pass it through the text encoder and get the text embedding. And you take the inner product of all those text embeddings with the image embedding and see which one fires and that is the caption corresponding to that particular image. And that's how you do zero-shot prediction.

### 02:23:12 · Speaker 1

But you as you can see all this is actually noise contrast estimation isn't it different ways of doing noise contrast estimation. So, I encourage you to look at all of these ok I mean SIMCLR we looked at JEPHA I will just talk about it in a while because I have asked you to implement this. But we will cover it in the next class. Wave2Vec for speech is again what they do is they take the speech signal

### 02:23:38 · Speaker 1

mask it and create the positive and negative examples and and solve a contrastive learning task and get the representations. See in fact I was working with like one of these like insurance brokers, I mean there is this company called Policy Bazaar right. I was solving a research problem for them. So they were building automatic speech recognition systems for their customer care customer centers call centers.

### 02:24:08 · Speaker 1

So they had built a supervised ASR so when we tried wave to wave kind of approaches okay what happened was their dependence on supervised data came down by 85 percent

### 02:24:22 · Speaker 1

They could achieve the same performance on ASR by using only 20 percent of the supervised data. So, these are very very powerful methods, e contrast learning methods, okay.

### 02:24:34 · Speaker 1

Now the last thing that I wanted to talk about is this joint extraction of

### 02:24:46 · Speaker 1

This is one thing that this guy uh Jan Likon keeps talking about everywhere no

### 02:24:56 · Speaker 1

It's quite hard

### 02:24:59 · Speaker 1

Joint embedding predictive architecture

### 02:25:18 · Speaker 1

What they do here is they

### 02:25:22 · Speaker 1

Avoid

### 02:25:25 · Speaker 1

We need for negative samples

### 02:25:35 · Speaker 1

What they do is the following they take an image, okay, and by the way they use what is called as a

### 02:25:42 · Speaker 1

Vision transformer as the backbone model

### 02:25:50 · Speaker 1

I will teach transformers in the next class then I will talk about vision transformers. Now the idea is suppose you have an image like this, okay, what they do is they take random patches

### 02:26:04 · Speaker 1

You cut out some random patches from this image and call those patches as target patches

### 02:26:14 · Speaker 1

And all the other patches which are here

### 02:26:20 · Speaker 1

They create some other patches from the region that is outside of the target patches and call them as context patches

### 02:26:32 · Speaker 1

Okay the task

### 02:26:36 · Speaker 1

is to predict

### 02:26:39 · Speaker 1

the target batches

### 02:26:46 · Speaker 1

given the context patches as input

### 02:26:58 · Speaker 1

That's all this JPAR does. And they claim that if you do this, then the performance that we get is much much better than most of the existing contrastive learning methods. Let me just show you that.

### 02:27:17 · Speaker 1

This is what I have asked you to implement, okay? So, when you don't have to do it using vision transformer, you can actually do it using the CNN. Do you see this figure now, my screen and figure three?

### 02:27:33 · Speaker 1

Can you confirm if you see my screen

### 02:27:35 · Speaker 4

Those are not visible

### 02:27:36 · Speaker 1

That's cool

### 02:27:44 · Speaker 1

Yeah I will take questions in a while

### 02:27:47 · Speaker 1

Now do you see the screen

### 02:27:52 · Speaker 4

This

### 02:27:54 · Speaker 1

This is what they do, right? They taken a given image, given an image, they divide the image into non-overlapping patches or yeah, non-overlapping patches and they randomly take some patches as target patches, okay? And then take some other patches as context patches. Now the task is that if you are given context patches, they have two encoders, one they call as context encoder and target encoder, which share the weights. Now given the context

### 02:28:24 · Speaker 1

patches the task is to predict the target patches

### 02:28:33 · Speaker 1

That is why they call it as the predictive architecture. So what is to be done? Yeah. So the image based joint embedding predictive architecture uses a single context block to predict representations of various target blocks originating from the same image. Of course, they do not predict the target

### 02:28:52 · Speaker 1

patch image at the image level they do it at the represent I mean the embedding level

### 02:28:58 · Speaker 1

What's interesting is that all they use is a square error loss between D

### 02:29:06 · Speaker 1

true target and the predicted target that's all. It's extremely easy to implement. Look at this figure. So the original image, you have this context and multiple targets. What they do is they give the context image as an input to a VIT for the context encoder and they want to predict the embeddings corresponding to the target patches and they simply use an MFC between the predicted target embedding and the true

### 02:29:36 · Speaker 1

target everybody

### 02:29:46 · Speaker 1

Is it alright? See it actually makes lot of sense intuitively you know. See it's like suppose I give you this image okay and ask you to predict this. You are implicitly learning how to complete this dark phase isn't it?

### 02:30:03 · Speaker 1

Do you get what I'm trying to say

### 02:30:06 · Speaker 1

So, that is why they say that this thing will learn implicitly the representations that correspond to the underlying data set. Of course, as I said, the base for all this

### 02:30:21 · Speaker 1

lies in Nash–Kantor estimation

### 02:30:50 · Speaker 1

Okay, questions? It's a survey.

### 02:30:56 · Speaker 4

The assignment we are implementing IJPEGG, so it is a typo, right?

### 02:31:02 · Speaker 1

I J E

### 02:31:04 · Speaker 4

PG in the 70s

### 02:31:05 · Speaker 1

The second one should be yeah yeah of course yeah

### 02:31:14 · Speaker 1

the other

### 02:31:18 · Speaker 4

So when choosing the patches they are completely random or there is some yeah

### 02:31:23 · Speaker 1

They're random they're random

### 02:31:25 · Speaker 1

They are random but what they do know they will ensure that the patches for the context and the target are non-overlapping

### 02:31:34 · Speaker 4

Answer the

### 02:31:39 · Speaker 4

You're talking about

### 02:31:39 · Speaker 1

Oh

### 02:31:41 · Speaker 4

Choosing that

### 02:31:41 · Speaker 1

So that they have that that that is a hyper that is actually a hyper parameter okay and they have experimented with multiple of them

### 02:32:02 · Speaker 4

So in the IJPA uh net I mean method uh what how does the decoder and encoder look like uh like what is no decoder

### 02:32:11 · Speaker 1

There is no decoder

### 02:32:17 · Speaker 1

There is no decoder there there are two encoders one is the context encoder the other is called the target encoder

### 02:32:24 · Speaker 4

Then what are we learning there I mean what is learned is it a network

### 02:32:29 · Speaker 1

the network no the encoder that is MF theta network that would take a pair of I mean that would take a a a patch as an input and gives you some vector as an output

### 02:32:43 · Speaker 4

okay okay okay fine fine fine only okay so it's not generating anything it is not generating anything no no

### 02:32:47 · Speaker 1

He's not generating anything

### 02:32:50 · Speaker 4

Okay

### 02:32:53 · Speaker 2

Is that an assignment or a question

### 02:32:54 · Speaker 1

you can you can say that there is also a a a predictor right what which will do is that will take the see what they use for f theta is a is a vision transformer so this transformer would give you the embeddings okay they also have a predictor network that would take these embeddings right from the true target patch and predict the yeah

### 02:33:22 · Speaker 4

Okay predict the I mean the entire image with the with the field in

### 02:33:28 · Speaker 1

Not the image, not the image, it will predict the uh it will take as input the the embedding corresponding to the context yeah embeddings of the context is taken as input and it will predict the embeddings of the target

### 02:33:34 · Speaker 4

You're building a

### 02:33:41 · Speaker 4

Okay without ever having to generate anything it can There is no generation there is no generation Okay okay okay

### 02:33:44 · Speaker 1

There is no generation there is no generation okay okay okay so there are two encoders basically let me just show you the figure again hold on

### 02:33:58 · Speaker 1

Is my screen visible

### 02:34:01 · Speaker 4

Yes yes

### 02:34:02 · Speaker 1

See there are two encoders one is called the context encoder and the target encoder okay. So what will give is this con context encoder will give you a vector target encoder will give you another vector right.

### 02:34:14 · Speaker 4

Yes

### 02:34:15 · Speaker 1

Now what would this there is another network called the predictor network. What would this predictor network do? It will take the embedding corresponding to the context encoder.

### 02:34:27 · Speaker 1

Right

### 02:34:29 · Speaker 1

and predict the the target the embeddings of the target encoder

### 02:34:34 · Speaker 4

Yeah embeddings of the target yeah okay

### 02:34:35 · Speaker 1

embeddings of the target encoder and the loss for this G, right? So basically how does the loss go? So there are two networks like this F theta and F theta cat. Both of these are vision transformers. The context network will take some patches from the context. It will take context patches. Target encoder will take target patches. So you get two embeddings, right? Corresponding to target and the context. Now you take a predictor network that would take as input the encoding, embedding

### 02:35:05 · Speaker 1

correspond I mean output of the context encoder okay and predicts the output of the target encoder

### 02:35:15 · Speaker 1

It clear

### 02:35:16 · Speaker 4

Yes thank you

### 02:35:17 · Speaker 1

there is an L2 loss between them that's what you need to implement as I said no for for your implementation purposes uh you can either use a uh a vision transformer here if you if you can otherwise you can use a simple CNN also here no problem

### 02:35:35 · Speaker 4

Do we need two networks here to be trained separately

### 02:35:38 · Speaker 1

I mean what is done in practice is that they take you actually need two networks but you can share the weights between them. You need one network for target encoding the other for the context encoding.

### 02:35:58 · Speaker 1

Okay, so great, I think we have to took lot more time than usual. Okay, so that's it for today. Uh, we will reconvene again next week.

### 02:36:08 · Speaker 2

Answer one question In question number nine it says distilled the above resonate on a small sized MLP

### 02:36:16 · Speaker 2

What do we mean by distilling it

### 02:36:20 · Speaker 1

Not taught you distillation right

### 02:36:28 · Speaker 4

So take a smaller network and show it a lot of uh

### 02:36:31 · Speaker 1

No no no I have to I have to teach distillation

### 02:36:31 · Speaker 4

Little rat

### 02:36:35 · Speaker 1

Let me do it next week if I do it next week then I have to extend the assignment deadline for one more week

### 02:36:43 · Speaker 1

This is a small topic that I wanted to said that should be

### 02:36:46 · Speaker 2

So that should be helpful sir

### 02:36:49 · Speaker 2

That should be helpful

### 02:36:52 · Speaker 1

I will do that too much

### 02:36:53 · Speaker 4

It's our equal ending our

### 02:36:59 · Speaker 1

Meaning the uh assignment deadline you are saying huh

### 02:37:04 · Speaker 1

It's okay no I mean I'll just give you maybe one more week till 30th

### 02:37:09 · Speaker 2

Yes sir, yes sir, it's okay

### 02:37:15 · Speaker 1

38 should be okay, no? Let me do it right away. So that's it.

### 02:37:22 · Speaker 1

Signments

### 02:37:26 · Speaker 1

Because anyway I'm grading it on uh like the first week right So time went to edit

### 02:37:34 · Speaker 1

Please remind me our next class I need to teach installation I complete it completely off went off my head First week of December

### 02:37:46 · Speaker 1

Yeah
