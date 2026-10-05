---
id: D-JQVOodqmg
title: Lec 11 - Deep Generative Models Diffusion models part 1 Formulation
date: '2024-11-23'
url: https://www.youtube.com/watch?v=D-JQVOodqmg
description: ''
author: prathoshap5226
duration: 02:45:18
model: saaras:v3
transcript: true
---

# Lec 11 - Deep Generative Models Diffusion models part 1 Formulation

## Transcript

### 00:00:02 · Speaker 1

few of us have marked in the quiz. But the answer is saying increased disentanglement on increasing beta.

### 00:00:11 · Speaker 3

One second. Yeah, I have pasted it.

### 00:00:12 · Speaker 1

Yeah, I have pasted the snippets.

### 00:00:15 · Speaker 5

pasted the

### 00:00:16 · Speaker 3

Huh?

### 00:00:17 · Speaker 5

they're saying it should be decreased disentanglement with reduced reconstruction quality.

### 00:00:18 · Speaker 1

I think it should be

### 00:00:23 · Speaker 3

Come again, Suhas?

### 00:00:25 · Speaker 5

it says it should actually the correct option should be decreased disentanglement right? But the option that is marked correct is increased disentanglement

### 00:00:38 · Speaker 3

Yeah, it should be decreased. Wait, let's see. If beta is increased, what will happen? Is that the weight for the K L is increased? If the weight for the K L is increased, then... Yeah. It should be...

### 00:00:53 · Speaker 3

it should be both reconstruction quality and entanglement getting decreased. Okay.

### 00:01:00 · Speaker 3

Okay. So, uh, first let us, uh, I think if the correct answer is marked as this thing.

### 00:01:08 · Speaker 3

व्हाट इज द करेक्ट आंसर गिवन नाउ इंक्रीज्ड डिसएंटांगलमेंट रेड्यूस्ड रिकंस्ट्रक्शन क्वालिटी राइट

### 00:01:08 · Speaker 5

correct

### 00:01:12 · Speaker 5

Yeah, yeah.

### 00:01:14 · Speaker 3

No, that is not correct. Okay, so can we change this? Like and

### 00:01:16 · Speaker 5

ம்

### 00:01:21 · Speaker 5

Yeah, I'll I'll change the correct

### 00:01:24 · Speaker 4

But sir, is it like whenever we are increasing the beta, it will be a stronger penalty on KL Dimension, which is promoting the disengagement because it's slippery.

### 00:01:24 · Speaker 3

Sir

### 00:01:31 · Speaker 3

which is

### 00:01:35 · Speaker 3

No, it is not, right?

### 00:01:37 · Speaker 3

No, see because that's what I told you, right? The word disentanglement refers to having different posteriors for all x, meaning for each x.

### 00:01:47 · Speaker 4

correct

### 00:01:48 · Speaker 5

Right, Right.

### 00:01:49 · Speaker 3

That is not happening, no? If you if you increase beta, the posterior collapse would be more, isn't it?

### 00:02:03 · Speaker 4

at the potential cost

### 00:02:04 · Speaker 7

Uh sir when we are giving a higher value of beta, uh what we are saying is that in the overall loss minimization, we have to minimize KL divergence loss more than we have to minimize reconstruction loss.

### 00:02:09 · Speaker 3

C

### 00:02:18 · Speaker 3

Correct, Correct.

### 00:02:19 · Speaker 7

So if we are reducing if we are increasing beta eventually what we are doing is we are ensuring that KL divergence loss comes down further.

### 00:02:19 · Speaker 3

if you're

### 00:02:28 · Speaker 7

which means disentanglement is going to increase

### 00:02:28 · Speaker 3

Correct

### 00:02:33 · Speaker 3

disentanglement is going to decrease no if the K L is reduced further that is what I am saying if the K L is see first understand that reduction of K L is inverse I mean is inversely proportional to in disentanglement.

### 00:02:51 · Speaker 7

Right, so disengagement should increase when KL divergence is reducing, right?

### 00:02:57 · Speaker 3

Correct. Yeah.

### 00:02:58 · Speaker 7

So then the marked answer is right, increased disentanglement will reduce the restriction.

### 00:03:02 · Speaker 8

Uh, I think

### 00:03:03 · Speaker 3

K L S increasing in the past. Yes sir, I think even multiple sources online say the same thing. So hold on. I think I'm getting confused. Let's see.

### 00:03:04 · Speaker 8

is increasing in the

### 00:03:10 · Speaker 0

Hold on

### 00:03:11 · Speaker 8

Bio-Venue

### 00:03:15 · Speaker 8

there is double negative disentanglement

### 00:03:16 · Speaker 6

disentanglement

### 00:03:17 · Speaker 3

Hold on, hold on, hold on, hold on. Let me let let me let me make it clear for myself and then we'll discuss. Now beta is increasing. Beta is increasing meaning K L is reduced further. If the K L is reduced further, then the disentanglement.

### 00:03:17 · Speaker 6

Ha, there is a chat

### 00:03:20 · Speaker 6

hold

### 00:03:40 · Speaker 3

still decrease. Right? Because disentanglement KL is reducing further, the disentanglement has to reduce, correct?

### 00:03:50 · Speaker 7

So entanglement has to reduce

### 00:03:50 · Speaker 3

entangled

### 00:03:54 · Speaker 3

No no no. KL reduction is entanglement reduction. See, suppose KL is zero.

### 00:04:06 · Speaker 3

Okay, if if KL is zero, then what happens? If KL is zero, the entanglement would be increased, right? Because all of them are collapsing to Z given X, sorry, normal zero one, isn't it?

### 00:04:22 · Speaker 3

Isn't it?

### 00:04:25 · Speaker 4

Maybe sir we will come back with the proper way of this. So

### 00:04:25 · Speaker 5

maybe

### 00:04:30 · Speaker 5

I think entanglement

### 00:04:32 · Speaker 4

I believe whenever we increase the beta it will increase the means at the cost of KL diversion. It will reduce the quality of reconstruction and increase the day engelament.

### 00:04:46 · Speaker 7

But yeah, I need your notes again.

### 00:04:46 · Speaker 4

But yeah, I need your notes again.

### 00:04:50 · Speaker 7

If the disentanglement is reducing, it means for any input, uh the latent variable space is going to be almost similar. Which means the reconstruction quality should be reducing.

### 00:04:50 · Speaker 2

recent

### 00:04:51 · Speaker 1

and

### 00:04:51 · Speaker 4

thank you

### 00:05:05 · Speaker 3

haha reconstruction quality reducing that is definite there is no operation there. right so basically we cannot have

### 00:05:09 · Speaker 7

Right, so basically we cannot have a scenario where disentanglement reduces and reconstruction quality increases.

### 00:05:18 · Speaker 6

I mean what what do we mean by entanglement? So for example if the posterior becomes normal has the entanglement increased or decreased?

### 00:05:25 · Speaker 7

So what my understanding is that entanglement being higher means that for any input image that we are giving the latent space is coming out to be almost similar. That is why there is an entanglement in the latent space for any input image coming out to be similar.

### 00:05:40 · Speaker 3

correct

### 00:05:41 · Speaker 3

That is correct. That is correct.

### 00:05:43 · Speaker 7

Right. So if we are saying that we are giving more weightage to the KL divergence, we are going to basically try to ensure that the entanglement reduces.

### 00:05:55 · Speaker 6

No, when posterior becomes normal, No, entanglement increases.

### 00:05:55 · Speaker 7

when posterior becomes normal

### 00:05:57 · Speaker 1

No, entanglement increases. More weightage to KL means entanglement, yes.

### 00:05:59 · Speaker 6

more weight

### 00:06:01 · Speaker 6

all of them will become close to normal, right?

### 00:06:05 · Speaker 7

But when they

### 00:06:05 · Speaker 6

that

### 00:06:06 · Speaker 1

KL is a loss. KL is a loss.

### 00:06:06 · Speaker 6

l is a loss

### 00:06:09 · Speaker 7

hmm

### 00:06:10 · Speaker 1

if we are multiplying with

### 00:06:10 · Speaker 7

see, the thing is there is a minimization operation happening when we are giving more weightage to beta, we are going to further reduce the value of KL divergence. which means we are going to reduce the entanglement. I mean we all agree that

### 00:06:23 · Speaker 6

I mean we all agree that if the K L has decreased then the posterior becomes normal right? We all agree on that.

### 00:06:32 · Speaker 1

Correct

### 00:06:34 · Speaker 5

a position becomes

### 00:06:34 · Speaker 6

Yeah, so does this mean entanglement has increased or decreased?

### 00:06:38 · Speaker 5

it's maximum entanglement, right? When your posterior has become a normal. That's what people are trying to say.

### 00:06:45 · Speaker 6

Yeah, so entanglement has increased, right?

### 00:06:48 · Speaker 3

Guys, do you see my screen?

### 00:06:48 · Speaker 5

Tangle Mint

### 00:06:50 · Speaker 8

function

### 00:06:55 · Speaker 8

Yes sir

### 00:06:55 · Speaker 1

Yes sir

### 00:06:57 · Speaker 3

Can you read whatever whatever I have highlighted?

### 00:07:06 · Speaker 2

Yes, yes.

### 00:07:06 · Speaker 3

Can you see what I have highlighted?

### 00:07:08 · Speaker 8

But what is good in this case, sir? Bigger or

### 00:07:13 · Speaker 8

dissentanglement is good

### 00:07:16 · Speaker 3

this is the this is an excerpt from the beta V I paper.

### 00:07:23 · Speaker 3

Okay

### 00:07:24 · Speaker 3

higher the beta

### 00:07:26 · Speaker 3

bitter disentanglement

### 00:07:27 · Speaker 2

Hello

### 00:07:30 · Speaker 4

better means increasing sir

### 00:07:32 · Speaker 4

Right

### 00:07:34 · Speaker 3

Correct

### 00:07:37 · Speaker 3

Correct. Higher the beta, increase disentanglement. Isn't it?

### 00:07:41 · Speaker 8

but here they put minus of beta D I write instead of plus beta in the the beta V I E loss term they are subtracting instead of adding the loss

### 00:07:53 · Speaker 3

appropriate tune beta greater than one call. Hold on, let's see, have they done that?

### 00:07:59 · Speaker 8

the term above that image

### 00:08:01 · Speaker 3

Yeah, there is a minus beta, correct.

### 00:08:03 · Speaker 8

So we we did plus when we were discussing so

### 00:08:09 · Speaker 3

Oh

### 00:08:10 · Speaker 8

I think that might be the

### 00:08:16 · Speaker 3

Oh. Okay, got it. So in our formulation it was plus Z.

### 00:08:25 · Speaker 8

Yes sir. Thanks sir. Yes sir.

### 00:08:25 · Speaker 5

Thank you

### 00:08:28 · Speaker 3

it was plus beta. But then it is

### 00:08:30 · Speaker 5

But then it is how how plus beta work here? It wouldn't work, right? You need

### 00:08:36 · Speaker 3

No no no

### 00:08:40 · Speaker 3

No no what I meant is see that then beta is taken to be negative right? I think Suhas let's do one thing I think you know there's confusion so let us just ignore that question and just add one to everyone that's all. Easiest way to deal with it.

### 00:08:45 · Speaker 5

I think

### 00:08:47 · Speaker 5

Let's

### 00:08:54 · Speaker 5

PCS to deal with

### 00:08:56 · Speaker 5

Fine

### 00:08:57 · Speaker 3

Yeah

### 00:08:59 · Speaker 3

But yeah, so I think you got the point, right, at least in in terms of what is happening. If beta is taken to be a positive integer and and the objective is written to be minus beta, then increase in beta, right, uh implies

### 00:09:18 · Speaker 3

good disentanglement, right? better disentanglement. I think that is what it is. Yeah, I think I'm convinced. Just think about it, huh? So let's move on. Because it's already pretty late. Okay. So, uh, Suhas, take a note of it, huh? We just have to add one to everyone in this in this particular quiz, huh?

### 00:09:36 · Speaker 5

Sure, Okay, Yeah.

### 00:09:39 · Speaker 3

Thank you Swasth, I think you can leave now if you want I can start the class.

### 00:09:41 · Speaker 1

Okay

### 00:09:44 · Speaker 1

Okay.

### 00:09:45 · Speaker 3

ओके थैंक यू

### 00:09:48 · Speaker 1

Sorry for interrupting. Can you please repeat what you said about the beta thing? Sorry.

### 00:09:49 · Speaker 3

shooting

### 00:09:57 · Speaker 3

बीटा इज अ पॉजिटिव इंटीजर एंड द कॉस्ट इज के एल माइनस बीटा सॉरी रिकंस्ट्रक्शन माइनस बीटा ओके।

### 00:10:08 · Speaker 9

Okay

### 00:10:12 · Speaker 3

So if beta is increased then disentanglement will become better. Because we are minimizing that KL that's all and beta is a positive number.

### 00:10:22 · Speaker 9

Okay

### 00:10:23 · Speaker 3

So just read this uh this beta V I paper no it's pretty well described. I think that is correct. The only confusion was because you know the in our formulation we we took plus beta and beta in our case was between zero and minus one.

### 00:10:24 · Speaker 9

just

### 00:10:45 · Speaker 3

Right, so in that way, this question can be interpreted as if you put plus there, increasing beta means it is you are moving it away from minus one. So

### 00:10:56 · Speaker 3

So let's not get into that confusion. I think this it's it's The problem is with writing that as plus that's all. So let us like ignore that question for everyone. Okay so

### 00:11:10 · Speaker 3

How many quizzes are done now?

### 00:11:15 · Speaker 2

Ford

### 00:11:15 · Speaker 3

Yes sir

### 00:11:17 · Speaker 9

Sir

### 00:11:19 · Speaker 2

four are done okay. So we need two more.

### 00:11:27 · Speaker 2

we can do, let me just look at the calendar.

### 00:11:31 · Speaker 2

Sir

### 00:11:34 · Speaker 3

ninth and sixteenth.

### 00:11:37 · Speaker 3

We have three weeks including today. So today is done.

### 00:11:42 · Speaker 3

Shall we do a quiz on ninth and sixteenth?

### 00:11:47 · Speaker 3

You can skip on second uh because

### 00:11:50 · Speaker 1

Um

### 00:11:51 · Speaker 1

So sixteenth I think he was planning for an online hybrid class

### 00:11:52 · Speaker 3

Skin

### 00:11:55 · Speaker 3

Correct. We'll have a quiz then, no problem. Okay. We don't want. See, otherwise we can do it on second and ninth also.

### 00:11:57 · Speaker 1

Okay

### 00:11:59 · Speaker 1

otherwise we can do it

### 00:12:06 · Speaker 9

Sir, second cricket

### 00:12:07 · Speaker 1

second many people will not be keep on second sir

### 00:12:08 · Speaker 2

many people

### 00:12:08 · Speaker 9

will not be. Keep on second sir.

### 00:12:11 · Speaker 3

Okay, so then let us do it on ninth and sixteenth, okay?

### 00:12:15 · Speaker 9

Yes, thank you

### 00:12:19 · Speaker 2

And assignments we said three assignments right?

### 00:12:24 · Speaker 9

Yes sir

### 00:12:27 · Speaker 2

treatments

### 00:12:32 · Speaker 4

I think you mentioned that you will give the third one in the November first week.

### 00:12:37 · Speaker 3

coding assignments three into fifteen so two is ten when is the deadline for your second assignment?

### 00:12:43 · Speaker 6

Twenty Eight. Twenty Eight.

### 00:12:44 · Speaker 4

twenty eight

### 00:12:47 · Speaker 3

twenty eight. So then Sunday I will release the third. So that we can finish by mid mid November. Okay good. So one exam is done quiz four two more quizzes and one more assignment. Okay great we are on track. Okay. So let us get back to classes. So you can see my screen. Can you see my screen?

### 00:13:11 · Speaker 9

Yes sir

### 00:13:13 · Speaker 3

Okay

### 00:13:14 · Speaker 3

Okay, so today's agenda is diffusion models, DDPM. Yeah, so I'll tell you rest of the course, the way I'm planning is we have three more classes, right? So, I'd hopefully complete diffusion models today. Let's see. So today we'll do diffusion models and we'll have three more classes. And one class I will do noise contrast estimation, self-supervised learning, these ideas and we'll have two more classes.

### 00:13:43 · Speaker 3

We can use it for autoregressive models and LLMs. Okay. That's how I'm planning. Okay. uh let's get back to stuff. So we were looking at denosing diffusion models. uh just a quick recall. These are hierarchical VAEs, right? which have multiple latent spaces. Capital T number of latent spaces. All the latent spaces have the same dimension as the data space. So you start from the data and and keep projecting on to the latent space till it becomes

### 00:14:18 · Speaker 3

Uh

### 00:14:20 · Speaker 3

till the stage, still it becomes, till it becomes a Gaussian distribution and from the latent space you get back to the data space by

### 00:14:29 · Speaker 3

traversing the path in the reverse direction. So the thing is the dimensionality of all the latent spaces is same as that of the data space is something that we saw, right? And the

### 00:15:01 · Speaker 9

it is not moving. Does somebody know why?

### 00:15:11 · Speaker 2

not able to move this.

### 00:15:15 · Speaker 9

Post Kill Restart

### 00:15:18 · Speaker 2

Huh?

### 00:15:20 · Speaker 9

Post Killen

### 00:15:21 · Speaker 0

East

### 00:15:21 · Speaker 2

Okay

### 00:15:21 · Speaker 0

Bus

### 00:15:24 · Speaker 9

What did you say?

### 00:15:28 · Speaker 2

just restart the application. Close it and restart.

### 00:15:43 · Speaker 9

Hmm

### 00:15:47 · Speaker 2

Four

### 00:15:48 · Speaker 9

still not moving

### 00:16:01 · Speaker 9

you know, it's moving.

### 00:16:10 · Speaker 9

Okay

### 00:16:11 · Speaker 3

Yeah. So the dimensionality of the latent space is same as that of the data space, something that we saw. Right? The encoding process in a DDPM is not learnable. It's a fixed encoding process. And it's a Markov chain. Okay, that is one other thing that we saw. Okay?

### 00:16:28 · Speaker 3

Yeah, so we uh made the notation consistent with the literature. Data is represented using X naught and the latent space is represented using X one through X capital T, okay?

### 00:16:41 · Speaker 3

Yeah. So you start from X naught and go to X capital T and the dimensionality of X naught is equal to X T for all T. And this is how the encoding process is defined, okay? You have fixed alphas alpha one to alpha T and every X T is given by the previous X previous latent, scaled previous latent plus some scaled noise where you sample from normal zero one and add it. Okay? This is the so-called formal

### 00:17:11 · Speaker 3

process or the encoding process in a DDPM. It's a first order Markov process with Gaussian transitions. It means that you take one random variable, add Gaussian noise with the second random variable and you traverse that Markov chain.

### 00:17:28 · Speaker 3

Okay? And the stationary distribution of this Markov chain is normal zero one. And I hope that I also showed you that picture, did I? Where you start from an image and get to the noise. I showed you that picture, right?

### 00:17:41 · Speaker 3

Class Class

### 00:17:43 · Speaker 3

Okay, great

### 00:17:44 · Speaker 9

is

### 00:17:44 · Speaker 2

Yes

### 00:17:45 · Speaker 3

Okay

### 00:17:45 · Speaker 2

this is where we are so let us move on from here.

### 00:18:07 · Speaker 9

Okay. I'll give you the high level idea

### 00:18:09 · Speaker 3

of what we will do today and then I will run through the math.

### 00:18:14 · Speaker 3

Algebra is a little involved, but it's not difficult.

### 00:18:19 · Speaker 3

Yeah, okay.

### 00:18:21 · Speaker 3

So the idea is, see, we have

### 00:18:27 · Speaker 3

an encoding process

### 00:18:30 · Speaker 3

is a fixed encoding process.

### 00:18:34 · Speaker 3

given by the following. So we have X T to be equal to root of alpha T times

### 00:18:41 · Speaker 3

xt minus one plus root of one minus alpha t times epsilon where epsilon comes from normal zero one right this is the encoding process correct so this implies

### 00:18:56 · Speaker 3

that the conditional distribution of any x t given x t minus one

### 00:19:08 · Speaker 3

What is this can somebody guess? We know that from reparameterization that if you start from a normal distribution, scale it and shift it with a certain mean and variance, you will still get a normal distribution, right? So these are normally distributed. So please note that my notation, normally distributed, the random variable is X T, correct? The mean is

### 00:19:29 · Speaker 2

root of

### 00:19:32 · Speaker 3

alpha t into x t minus one

### 00:19:37 · Speaker 3

variants is one minus alpha t times identity. So there's a very slight abuse of notation here I'll tell you what it means. See when you

### 00:19:49 · Speaker 3

when you are writing a conditional distribution like this, right? The condition random variable x t minus one is fixed in the sense that it has already taken some value. Okay? But the the random variable that is to be conditioned x t is not fixed. We have a distribution over it. That is what we have written that it's a normal distribution over x t, okay? Where the mean is square root of alpha t times x t minus one. So this x t minus one which I have marked, right? In सो, इट इज अ फिक्स्ड वैल्यू बिकॉज़ यू आर ऑलरेडी इन एक्सटी माइनस वन।

### 00:20:23 · Speaker 3

And XT minus one has assumed a particular value. Okay? And given that XT minus one already has a particular value, you have an entire distribution over XT, which is given by that equation. Does it make sense? Why do you have a distribution over XT is because of this epsilon that is there. So, you are given an XT minus one, you get an entire distribution over XT. Is that all right?

### 00:20:46 · Speaker 2

All of you

### 00:20:54 · Speaker 2

Okay. Now, what do we do is, as I said,

### 00:20:57 · Speaker 3

we have an encoding distribution that is fixed. please ask me questions if you have any because

### 00:21:04 · Speaker 3

make it a little faster today because I want to complete D D P M's let's see. So we have this is the encoding distribution we have the decoding distribution.

### 00:21:24 · Speaker 9

which is to be learned.

### 00:21:29 · Speaker 9

What is the decoding distribution? We write that as P theta

### 00:21:39 · Speaker 3

So decoding has to happen in the reverse direction X T minus one given X T. So please note the commonalities between this and the V A E right? In V A E the encoding distribution is Q of G given X. Yes? The posterior of uh latent given data. The sorry the encoding distribution is posterior of latent given data. Decoding distribution is posterior of data given latent. Okay? Similar thing is happening here. Uh I mean here there is no one latent no there are directions of latent so you start

### 00:22:09 · Speaker 3

start from uh x not which is the which is the data and you go to x capital T in one direction that is the encoding distribution the decoding distribution is in the reverse direction correct now this has to be learned

### 00:22:24 · Speaker 3

ओके. सो दिस इज फर्स्ट ऑफ ऑल दिस इज अस्यूम टू बी अ गॉशियन डिस्ट्रीब्यूशन अगेन। ओके। एट एक्सटी माइनस वन।

### 00:22:33 · Speaker 3

with a certain mean mu theta and a certain variance sigma theta.

### 00:22:38 · Speaker 3

Okay, so this mu theta and sigma theta

### 00:22:43 · Speaker 3

are the are the learnable model parameters. So this is what we will learn.

### 00:22:53 · Speaker 3

These are the learnable model parameters. So given the fixed encoding distribution, okay? We will make a distributional assumption on the decoding distribution and we learn the parameters of it. That is what we are going to do. Now how do we do it? So we learn that through

### 00:23:13 · Speaker 3

same thing elbow optimization we will do the exact same elbow optimization and we will earn this

### 00:23:22 · Speaker 3

That's all. So rest is algebra. Okay, now you understood right? So we have an encoding fixed encoding distribution and we have a learnable decoding distribution. Given the encoding distribution, okay, we optimize the ELBO and learn the decoding distribution parameters of the decoding distribution. That is what the idea is.

### 00:23:41 · Speaker 3

Okay, any questions so far quickly? Sarvesh.

### 00:23:45 · Speaker 1

Sir, in the encoding process, where did the root come from? Previously it was written alpha t x t minus one plus one minus alpha t epsilon. Was it? Oh, sorry.

### 00:23:52 · Speaker 3

Was it? Oh sorry my bad. It's my mistake. uh Or it's either here or there let me just see what the doesn't matter right I mean depends on what your alpha is but let's see what the literature does.

### 00:24:09 · Speaker 3

Thank you

### 00:24:09 · Speaker 9

pointing that

### 00:24:12 · Speaker 9

this is

### 00:24:16 · Speaker 9

a second now give me a second

### 00:24:22 · Speaker 9

Hmm

### 00:24:31 · Speaker 9

I think the problem here made a mistake so this has to be

### 00:24:39 · Speaker 2

generally we will write it as root of alpha okay

### 00:24:46 · Speaker 2

wrote it correctly today but yeah

### 00:24:50 · Speaker 3

is that okay?

### 00:24:50 · Speaker 2

Okay

### 00:24:51 · Speaker 3

clear it. Okay. Yeah, Abhitosh.

### 00:24:55 · Speaker 6

let's make it big guys

### 00:24:55 · Speaker 3

Let's make it big guys, yeah.

### 00:24:56 · Speaker 6

Yeah, why is the encoding process fixed here?

### 00:25:00 · Speaker 3

told you all that in the last class, okay? uh because that is, see, that is how the uh the DDPM is described, okay? The encoding process is fixed because it's a what do we want? We want a projection from the data space to the uh the latent space, okay? Or rather Gaussian zero one. Now we do it in the hierarchical manner. Now in a DDPM it is a Markov chain, right? So you are doing

### 00:25:10 · Speaker 2

Okay

### 00:25:24 · Speaker 2

Hello

### 00:25:26 · Speaker 2

Yep

### 00:25:30 · Speaker 3

random walk through a Markov chain. Now, unlike in a V A E where projection from the data distribution to the normal zero one, okay, cannot be guaranteed and has to be learned via that five encoder network. In a Markov chain, okay, if you have Gaussian transition, it can be guaranteed that the stationary distribution of a fixed Markov chain after sufficient number of steps.

### 00:25:55 · Speaker 3

convert just to normal zero one. So, since you want your data to go to normal zero one and you construct a Markov chain where there are slow transitions, you don't have to learn anything.

### 00:25:57 · Speaker 2

Okay

### 00:26:05 · Speaker 9

Yeah

### 00:26:07 · Speaker 3

That's the idea. Okay. I think I mentioned this in the last class but anyway, okay, is this clear? So what we will do next is that under these model assumptions, we will write down the ELBO as usual and optimize it. That's all. So that's all the entire process is now, okay? Now just like with the case as in the case of VAE, the final generation is via decoding. Because in VAE also you do the same thing, right? We will do the same thing here. uh The only thing

### 00:26:37 · Speaker 3

we have these kinds of model assumptions and we will have to optimize the elbow. Okay, let us do that.

### 00:26:44 · Speaker 3

uh let us start. Okay, elbow optimization

### 00:26:47 · Speaker 9

for DDPM

### 00:27:07 · Speaker 9

Okay

### 00:27:10 · Speaker 9

Recall, you should recall that.

### 00:27:11 · Speaker 3

what was our elbow so log of p theta of x. Okay we will start from the definition of the latent variable model that was

### 00:27:23 · Speaker 3

integral. So log of

### 00:27:28 · Speaker 2

integral P theta

### 00:27:34 · Speaker 2

X and Z

### 00:27:36 · Speaker 2

easy, correct? This is what it was. So finally what was our elbow? the

### 00:27:47 · Speaker 2

function of theta and phi

### 00:27:51 · Speaker 2

represented that as f theta of q phi.

### 00:27:55 · Speaker 2

what was that?

### 00:28:00 · Speaker 2

That was an expectation of log of

### 00:28:04 · Speaker 3

P theta

### 00:28:07 · Speaker 3

X and Z

### 00:28:07 · Speaker 2

divided by

### 00:28:11 · Speaker 2

Q of G given X

### 00:28:13 · Speaker 2

This was with respect to Q of Z given X.

### 00:28:17 · Speaker 2

Do you recall this all of you?

### 00:28:24 · Speaker 2

Okay, we just have to write this down for a D D P M. Okay, that's all it is. Let us do that.

### 00:28:33 · Speaker 2

So this is

### 00:28:38 · Speaker 2

L

### 00:28:38 · Speaker 3

go for D D P M or diffusion models D M is only a function of theta because there's no dependence on phi is equal to expectation of

### 00:28:50 · Speaker 3

log of p theta. So what is

### 00:28:54 · Speaker 2

x and z here that is x naught x one

### 00:29:03 · Speaker 2

Okay, why is this? This is because

### 00:29:05 · Speaker 3

plus

### 00:29:07 · Speaker 3

x not is the data variable and x one through x t are the latent variables. Correct? Divided by

### 00:29:16 · Speaker 3

Q of what is the latent variable here x one x two up to x t conditioned on x not okay and we have that same Q here that entire thing can't write it is this is this all right this is only a function of theta as you can see because encoding is fixed

### 00:29:37 · Speaker 3

Is this all right?

### 00:29:41 · Speaker 3

Okay, so now we'll just shorten this down and write it as

### 00:29:45 · Speaker 3

So please pay a little more attention today because it's notationally heavy, it's not difficult. But if you miss one notation it will all be gone. I'll write this as x zero to t because I can't write one to t all the time. Divided by q of x one through t which are the random variables conditioned on x not and this is

### 00:30:09 · Speaker 9

Is this okay?

### 00:30:20 · Speaker 9

So every step you either react

### 00:30:22 · Speaker 3

interrupt me if you don't understand. Okay, otherwise it will be difficult for me. So this is all right, right? This is our elbow. So we'll have to optimize this with respect to theta. Correct? This is what we need to do.

### 00:30:40 · Speaker 9

correct? So let us do that.

### 00:31:06 · Speaker 9

just give me just a second

### 00:31:16 · Speaker 9

Yeah

### 00:31:23 · Speaker 9

Okay great. So now

### 00:31:24 · Speaker 3

this can be written as I will not write this equal to every time so let us write this

### 00:31:31 · Speaker 3

expectation of log p theta x zero to t divided by q x one to t given x not. Okay, this is what we want.

### 00:31:48 · Speaker 3

Okay. Now this is

### 00:31:52 · Speaker 3

Okay, so first of all what we should do is we'll have to write this as

### 00:31:58 · Speaker 3

expectation of log of please observe here. So now P theta of X zero to T I will write it as P X T okay? times the product of

### 00:32:16 · Speaker 3

t equal to 1 to t

### 00:32:19 · Speaker 3

P theta

### 00:32:22 · Speaker 9

x t minus one given x t

### 00:32:28 · Speaker 9

divided by

### 00:32:32 · Speaker 9

Q

### 00:32:34 · Speaker 9

product of

### 00:32:36 · Speaker 9

T equal to

### 00:32:36 · Speaker 3

two one two T. Q

### 00:32:40 · Speaker 3

xt given xt minus one okay okay why did I write this

### 00:32:45 · Speaker 3

Now, P theta of

### 00:32:50 · Speaker 3

x naught x one up to x t okay. It is what we wrote as p theta of x naught to t. This is equal to

### 00:33:02 · Speaker 3

p theta of xt

### 00:33:05 · Speaker 9

times

### 00:33:08 · Speaker 9

P theta of

### 00:33:13 · Speaker 9

X

### 00:33:23 · Speaker 2

எனக்கு அது டெலிவரி அட்ரஸ் அதான் வச்சிருக்கியா?

### 00:33:32 · Speaker 9

that it the other way around.

### 00:33:35 · Speaker 9

Hmm

### 00:33:44 · Speaker 9

So that is P equal to one, right? So P theta of

### 00:33:52 · Speaker 9

X not

### 00:33:54 · Speaker 9

Given

### 00:34:03 · Speaker 9

So I think it's P theta of X1

### 00:34:06 · Speaker 2

give an x not

### 00:34:09 · Speaker 3

No no no we are going in the reverse direction no. Yeah. I'll just I'm just writing the chain rule hold on. So this is

### 00:34:20 · Speaker 2

Hello

### 00:34:20 · Speaker 3

Hello

### 00:34:21 · Speaker 3

shoot

### 00:34:21 · Speaker 3

Maroon

### 00:34:22 · Speaker 3

Okay

### 00:34:23 · Speaker 2

18

### 00:34:24 · Speaker 3

Good

### 00:34:25 · Speaker 3

should be. So I've written it from I mean I've written it from t equal to one to t. should be the other way. So x t minus one given x t okay. So this is x t minus two given x t minus one and so on up to p theta of x t. Okay. Yeah this is what it is. How is this? This is chain rule of

### 00:34:56 · Speaker 3

probability

### 00:34:58 · Speaker 3

Right? So now, since the forward process is first order Markovian, right? Reverse process is also a first order Markovian process. Which means that given X T, okay? uh X T minus one is independent of all the other states. That is why we have written it this way. Okay? Now this can be represented as P of X T, P of X T into product of

### 00:35:23 · Speaker 3

T equal to one two capital T P theta of X T minus one given X T. Now observe what did we do we took we took off the dependency of theta on X capital T why is this? We have designed our X T okay? Because X T by construction

### 00:35:45 · Speaker 3

is normal zero one, isn't it? While transiting the forward chain, we have ensured that the capital T at X random variable is normal zero one, therefore it is independent of P of X T is independent of theta. So this is P of X T. Okay? Is it all right?

### 00:36:03 · Speaker 3

So that is the numerator in that equation. So let us write down the denominator. So now what is Q of so what do we have in the denominator? We have Q of X one two T given X naught. This is what we have.

### 00:36:20 · Speaker 2

What is this equal to?

### 00:36:25 · Speaker 2

This is equal to

### 00:36:28 · Speaker 2

Q of

### 00:36:30 · Speaker 2

x one given x not

### 00:36:33 · Speaker 3

clue of

### 00:36:35 · Speaker 3

x two given x not

### 00:36:38 · Speaker 3

and so on the product of all this Q of

### 00:36:41 · Speaker 3

xt given. xt minus one. Sorry, this is

### 00:36:46 · Speaker 9

plus

### 00:36:48 · Speaker 9

C minus X two minus X one and so on

### 00:36:59 · Speaker 9

Okay, why is this the, why is this the case?

### 00:37:13 · Speaker 9

because they're independent of each other, right?

### 00:37:16 · Speaker 8

X1, X2 are

### 00:37:20 · Speaker 8

independent distributions.

### 00:37:23 · Speaker 3

X1 X2 are not independent

### 00:37:25 · Speaker 8

Okay, okay.

### 00:37:26 · Speaker 1

is the Markov process

### 00:37:26 · Speaker 8

Marco

### 00:37:27 · Speaker 8

Man

### 00:37:27 · Speaker 3

exactly. This is the marko process, right? This is the first order marko process.

### 00:37:27 · Speaker 2

exactly

### 00:37:28 · Speaker 2

just

### 00:37:31 · Speaker 9

processes because

### 00:37:45 · Speaker 9

Okay. See,

### 00:37:47 · Speaker 3

this can actually be written as you can write this as q of x one use the chain rule of probability right so you can write this as q of

### 00:37:56 · Speaker 3

x one given x not. And you have q of x one given sorry q of x two given x one and x not. Into q of x three given x one x two x one x not. And so on correct?

### 00:38:17 · Speaker 3

This is by chain rule of probability. Correct? So now Q of X two first order Markov and chain rule.

### 00:38:27 · Speaker 3

Now all these terms no Q of X two given X one and X not Q of X three given so up to Q of should have written this and then written that okay so this is Q of X capital T given everything behind that. X T minus one up to X not. Now and since it is

### 00:38:50 · Speaker 3

first order marko. right? So it will happen. You I think you got it right?

### 00:38:55 · Speaker 2

this is this is what it is.

### 00:39:01 · Speaker 2

Is it all right?

### 00:39:02 · Speaker 9

I will perhaps take this and put it there.

### 00:39:10 · Speaker 9

Okay

### 00:39:14 · Speaker 9

Okay

### 00:39:15 · Speaker 9

Lokesh, yeah.

### 00:39:18 · Speaker 0

Sir, in the above equation, like P theta, is it going to X T or X zero? Shouldn't it be going to X zero given X one?

### 00:39:28 · Speaker 3

where

### 00:39:29 · Speaker 0

uh like you had mentioned P theta of X T minus one given X T times P theta of X T minus two given X T minus one so on till P theta of X zero given X one right.

### 00:39:42 · Speaker 3

So here right you you have a P P theta of X T term also at the outside okay so what I'm what what you said is correct. Hold on let us make it a little precise.

### 00:39:55 · Speaker 9

Hello

### 00:39:55 · Speaker 9

So now here you have a

### 00:40:11 · Speaker 9

is equal to you have a p of x t term here okay

### 00:40:15 · Speaker 3

And the last term here would be obviously

### 00:40:21 · Speaker 3

p theta of x not given x

### 00:40:25 · Speaker 3

Correct?

### 00:40:26 · Speaker 0

Yeah, okay, thank you.

### 00:40:27 · Speaker 3

It's what I meant, yeah. Okay.

### 00:40:30 · Speaker 3

Okay, so now please have a look at it. Now in the elbow right, we now have the numerator. Okay, so now the reason I did this is how did we come from this step to this step? Okay. Now there was the joint distribution of X X X zero to X T, okay, under the model, we wrote that as this product. And in the denominator, there was the conditional distribution of latents given data and we represented that using this.

### 00:40:57 · Speaker 3

product. Is it okay?

### 00:41:00 · Speaker 3

Now I will continue from there. I'll take this equation.

### 00:41:04 · Speaker 9

So we have the elbow

### 00:41:09 · Speaker 9

equal to this

### 00:41:36 · Speaker 9

log of

### 00:41:40 · Speaker 3

expectation of log of

### 00:41:44 · Speaker 3

P X T. Please note that I've taken the dependence on theta for the final random variable T equal to one to T. We have P theta of X T minus one given X T divided by

### 00:42:01 · Speaker 2

product of

### 00:42:07 · Speaker 2

product of t equal to 1 to

### 00:42:11 · Speaker 3

capital T f q of x t given x t minus one, okay?

### 00:42:19 · Speaker 3

I hope that all of you know how this equation came, right? This is what we showed. Okay. Now it's a lot of algebra. Let's keep doing this. See, I will omit the expectation term here, okay? And only write the whatever is inside, okay? So that it is easier. Otherwise, I'll have to write that bracket every time.

### 00:42:40 · Speaker 3

I will write back the expectation term later, okay?

### 00:42:44 · Speaker 9

Good

### 00:42:47 · Speaker 9

the outer expectation.

### 00:42:56 · Speaker 3

This is not a any mathematical thing, no, this is simply to ease of writing, that's all, huh? So don't think that this is some step or something. I'll write back the expectation later. So consider log of if whatever is inside, I will write that as log of

### 00:43:13 · Speaker 3

P X T times

### 00:43:17 · Speaker 3

we'll take back

### 00:43:20 · Speaker 3

p theta of the first

### 00:43:27 · Speaker 3

or rather the last transition, okay? from the decoder. I will tell you why this was taken out. This will algebraically this will turn out to be easier. T equal to T two to capital T, you have P theta of X T minus one given X T. Okay?

### 00:43:45 · Speaker 3

divided by

### 00:43:49 · Speaker 3

will do the same thing with the encoder also. The Q of X one given X not, take that out, okay? And what is remaining is P equal to two to capital T.

### 00:44:02 · Speaker 3

Q of

### 00:44:04 · Speaker 3

X

### 00:44:04 · Speaker 9

xt given xt minus one.

### 00:44:15 · Speaker 9

Right? Now, uh this log, I mean this log is for everything.

### 00:44:23 · Speaker 2

Okay

### 00:44:26 · Speaker 3

Okay. Now, uh this is I'll use the law of logarithms and pull these things outside P of X T times P T of X naught given X one.

### 00:44:42 · Speaker 3

divided by u of x one given x not

### 00:44:48 · Speaker 3

Okay. uh The second term is plus log of

### 00:44:54 · Speaker 3

one product.

### 00:44:56 · Speaker 3

t equal to 2 to capital T. p theta

### 00:45:02 · Speaker 3

xt minus one given xt

### 00:45:06 · Speaker 2

divided by

### 00:45:10 · Speaker 9

Q of

### 00:45:12 · Speaker 9

xt q one xt minus one.

### 00:45:30 · Speaker 9

Okay

### 00:45:31 · Speaker 2

they should be all right. This is simply law of logarithms.

### 00:45:35 · Speaker 2

Okay. Now you consider what is important is the second term, okay? So consider

### 00:45:46 · Speaker 9

the denominator in the second term.

### 00:45:59 · Speaker 9

So which is

### 00:46:01 · Speaker 3

Q of

### 00:46:03 · Speaker 3

xt minus xt minus this is the forward distribution that we know of right? So now this can be written as q of xt given

### 00:46:14 · Speaker 3

xt minus one and x not. Can I write it this way? Now why do I do that? This is because of algebraic convenience. So as you will see later no, if we write this then the elbow optimizing elbow will become easier. There is one like vague interpretation that people have given in the original paper. I will also mention that but this is mostly because of algebraic convenience, okay? Please observe this carefully. This is one non trivial step.

### 00:46:44 · Speaker 3

we do this can we write q of xt given xt minus one as q of xt given xt minus one and x not are these the same

### 00:46:53 · Speaker 3

Why?

### 00:46:57 · Speaker 1

Markov process is independent of the like

### 00:46:59 · Speaker 3

Yeah, it's because of the first order Markov property. If you condition it with anything else than the previous state, it's it is the it is exactly the same, okay?

### 00:47:10 · Speaker 3

Now what we will do is we will use Bayes' law

### 00:47:20 · Speaker 9

and write this as

### 00:47:23 · Speaker 9

क्यू ऑफ

### 00:47:26 · Speaker 9

x t minus one

### 00:47:34 · Speaker 9

Given

### 00:47:35 · Speaker 9

xt and x not

### 00:47:39 · Speaker 9

Times

### 00:47:41 · Speaker 2

Q of

### 00:47:43 · Speaker 2

xt given x not

### 00:47:46 · Speaker 2

divided by

### 00:47:48 · Speaker 2

Q off

### 00:47:49 · Speaker 3

xt minus one given x not

### 00:47:54 · Speaker 3

What is this? This is simply the Bayes' law, right? I mean, you have probability of A given B and C can be written as probability of B given A and C times probability of B given C divided by probability of A given B. That is Bayes' law with three variables. Is that okay? So this is Bayes' law.

### 00:48:18 · Speaker 3

research with switch

### 00:48:21 · Speaker 3

three random variables you can please check that out in Wikipedia okay. Is that okay? This is simply based law. So now note that the first distribution that you have right in the numerator okay. What is this?

### 00:48:26 · Speaker 2

Hmm

### 00:48:39 · Speaker 3

we'll write that down.

### 00:48:41 · Speaker 9

Two of

### 00:48:44 · Speaker 9

xt minus one

### 00:48:50 · Speaker 9

given XT and X not

### 00:48:54 · Speaker 9

What is

### 00:48:54 · Speaker 2

this distribution can somebody guess?

### 00:48:58 · Speaker 2

This is the

### 00:49:01 · Speaker 2

distribution of okay. x t minus one given

### 00:49:07 · Speaker 9

given

### 00:49:09 · Speaker 9

that

### 00:49:12 · Speaker 9

the encoding process

### 00:49:20 · Speaker 9

including classes has started

### 00:49:30 · Speaker 9

started from x not, okay? And

### 00:49:35 · Speaker 9

Landed at

### 00:49:39 · Speaker 2

x t at t equal to t.

### 00:49:44 · Speaker 3

ओके, सी प्लीज नोट दैट दिस इज नॉट द फॉरवर्ड डिस्ट्रीब्यूशन।

### 00:49:49 · Speaker 3

right? forward distribution. What is forward distribution? forward distribution is Q of X T given X T minus one. Okay? So this distribution is that while you are constructing the forward process, okay? what is the distribution of X T minus one? How does the distribution of X T minus one looks? given that you have started from X naught and landed at X T at T equal to T.

### 00:50:18 · Speaker 3

Does it make sense? Do you understand what this distribution is?

### 00:50:24 · Speaker 3

basically if you start from x not okay. uh depending upon uh what kind of noise that you add at like or what kind of samples that you get for epsilon. uh x t can be very different correct?

### 00:50:43 · Speaker 3

Do you agree?

### 00:50:45 · Speaker 3

Starting from X naught, you keep adding noise. uh Please focus on this and like respond to me, okay, if you understand and not understand because this is the key, you have to understand this. What I'm saying is you start from X naught, okay, and keep adding noise. Now depending upon what sort of noise do you add, you end up at one particular XT.

### 00:51:06 · Speaker 3

Okay? So every time you take the same X naught and add different kinds of noises, you get to different XTs. Do you agree with this?

### 00:51:15 · Speaker 3

The question that we are asking is given that you have started from X not and landed at a particular XT, what is the distribution over XT minus one?

### 00:51:15 · Speaker 9

Yes sir

### 00:51:16 · Speaker 2

Yes

### 00:51:29 · Speaker 3

Does it make sense? See note that this is not Q of X T minus one given X T because we are talking about independence between X T given X T minus one and the other thing, right? We are not talking about independence of so X T minus one is not independent of X T or X not given X T, correct?

### 00:51:50 · Speaker 3

Markovian Markovian process says that X T is independent of everything else given X T minus one. It is not saying that X T minus one is independent of X T. I'm just saying that it is in the reverse direction and therefore this X not cannot be removed. What did we do? Please note again. We had Q of X T given X T minus one term in the in one of the terms uh in the in the elbow. Wrote that Q of X T given X T minus one uh in terms of I mean just condition that

### 00:52:20 · Speaker 3

xt minus one with x not that is okay because it's Markovian. Once we did that we used Bayes law to invert that okay and wrote this distribution in terms of q of xt minus one given xt and x not q of xt given x not q of xt minus one given x not. And this distribution q of xt minus one given xt and x not is simply the distribution of xt minus one given that the encoding process has started from x not and landed at xt at t equal to t.

### 00:52:54 · Speaker 9

Any questions here?

### 00:53:05 · Speaker 9

Idi

### 00:53:05 · Speaker 3

one question that might come up here is that why did we even write this as write this in terms of this Q of this this weird distribution right is because see if you keep it Q of X T given X T minus one.

### 00:53:22 · Speaker 3

Okay? What you see is the numerator, okay, is going in one direction. Okay, theta decoding distribution is going in the reverse reverse direction and the denominator is going in the forward direction, correct? As it is.

### 00:53:42 · Speaker 3

Okay, so if you want to uh optimize for the elbow, you can't simultaneously do it from both the directions.

### 00:53:51 · Speaker 3

So the idea is to represent the forward direction also, somehow in terms of, I mean, introduce the reverse direction transition, uh, in the forward direction also and that is why we use the Bayes' law to invert it. Now once you do this, what happens, you see, you know, this Q of X T minus one given X T and X naught is actually going in the reverse direction.

### 00:54:13 · Speaker 9

Correct?

### 00:54:22 · Speaker 9

So that is the

### 00:54:23 · Speaker 3

advisory convenience that we wanted and that's what that's why we wrote it this way, okay?

### 00:54:29 · Speaker 3

ओके, सो लेट अस गेट बैक टू एल्बो नाउ। सो नाउ गेटिंग बैक टू एल्बो।

### 00:54:34 · Speaker 1

सर, वन क्वेश्चन।

### 00:54:35 · Speaker 3

Yeah

### 00:54:36 · Speaker 1

if we do not uh like if we do not have x naught then also we could have come up with this base rule right like we just based on x t minus one and x t

### 00:54:48 · Speaker 3

your voice completely broke off. Was it only for me?

### 00:54:53 · Speaker 3

I can't hear you at all

### 00:54:54 · Speaker 1

ओके लेट मी रिपीट सर

### 00:54:55 · Speaker 2

call

### 00:54:57 · Speaker 1

am audible

### 00:55:01 · Speaker 2

Hello

### 00:55:01 · Speaker 1

Yes

### 00:55:03 · Speaker 2

Okay

### 00:55:03 · Speaker 1

Display

### 00:55:03 · Speaker 9

player for us, Ranjit

### 00:55:07 · Speaker 2

सर एम आई ऑडिबल टू यू

### 00:55:18 · Speaker 2

I can't hear you. Anybody else can tell me?

### 00:55:22 · Speaker 9

Yeah, we can hear him.

### 00:55:25 · Speaker 8

Yes sir

### 00:55:31 · Speaker 9

Sir, am I audible now?

### 00:57:08 · Speaker 9

Hello, can you hear me?

### 00:57:10 · Speaker 5

Yes sir

### 00:57:14 · Speaker 3

So it's called disconnected system.

### 00:57:22 · Speaker 9

sorry

### 00:57:37 · Speaker 2

Can you hear me?

### 00:57:39 · Speaker 9

Yes sir

### 00:57:41 · Speaker 3

Okay. So you were saying something, I mean I completely missed it because I think some connection issues. Can you repeat what what were you saying?

### 00:57:50 · Speaker 1

Yes sir. Am I audible to you now?

### 00:57:53 · Speaker 3

Yes, yes.

### 00:57:54 · Speaker 1

Okay, I'm saying if we did not include the x naught term, then also we could have come up with this like like a backward distribution q x t minus one given x t.

### 00:57:58 · Speaker 3

also

### 00:58:07 · Speaker 3

No, you can't know because how, how do you do that?

### 00:58:07 · Speaker 1

You can't

### 00:58:16 · Speaker 3

then you will have marginals over. See you can use the Bayes' law and simply write it as Q of X T minus one times Q of X T divided by Q of X T minus one, right? uh but you will have to find the marginals of Q of you have to you will get terms like Q of X T, Q of X T minus one and so on, right? These marginals are not computable.

### 00:58:16 · Speaker 1

subs

### 00:58:35 · Speaker 1

20%

### 00:58:38 · Speaker 1

Okay

### 00:58:38 · Speaker 3

okay? So however what we will see you know we can compute both q of x t given x not and q of x t minus one given x not. We will see that in a while. okay?

### 00:58:47 · Speaker 3

Hmm

### 00:58:49 · Speaker 3

ओके, ग्रेट। सो लेट अस गेट बैक टू एल्बो। सो व्हाट

### 00:58:52 · Speaker 2

we were doing was

### 00:59:00 · Speaker 2

helper was we had log of log of

### 00:59:05 · Speaker 2

P X T

### 00:59:07 · Speaker 9

Times

### 00:59:09 · Speaker 9

P theta of

### 00:59:11 · Speaker 9

x not given x one divided by

### 00:59:22 · Speaker 9

x one given x not this was the first term.

### 00:59:24 · Speaker 3

second term was plus log of

### 00:59:30 · Speaker 3

log of product t equal to two to capital T. Numerator was p theta of x t minus one given x t.

### 00:59:43 · Speaker 3

divided by

### 00:59:45 · Speaker 3

Q of

### 00:59:47 · Speaker 3

uh X T. It was given X T minus one right? X T minus one and X not we just conditioned it on that. Okay? And let's use the Bayes law.

### 00:59:59 · Speaker 3

Oh

### 01:00:00 · Speaker 1

we use the Bayes' law then whatever we had written there.

### 01:00:04 · Speaker 1

step two.

### 01:00:06 · Speaker 1

copy this entire thing

### 01:00:19 · Speaker 1

Oh

### 01:00:22 · Speaker 1

but I better to write it down again okay.

### 01:00:24 · Speaker 2

log of that I would save time

### 01:00:29 · Speaker 2

Yes

### 01:00:30 · Speaker 3

it's one

### 01:00:32 · Speaker 3

divided by

### 01:00:35 · Speaker 3

Q of X one given X not plus

### 01:00:42 · Speaker 3

plus log of

### 01:00:44 · Speaker 1

Okay

### 01:00:46 · Speaker 3

product

### 01:00:47 · Speaker 2

इक्वल टू टू टू कैपिटल टी वी हैव पी थीटा ऑफ

### 01:00:53 · Speaker 2

xt minus one given xt

### 01:00:56 · Speaker 2

divided by. Okay, we will use that Bayes' theorem that we had written. This was Q of X T minus one given X T and X naught times Q of

### 01:01:11 · Speaker 2

xt given x not divided by q of xt minus one given x not

### 01:01:18 · Speaker 2

Okay? So I will just show this to you.

### 01:01:24 · Speaker 2

Have a look and let me know if it works. How did we do? We went from here to here.

### 01:01:31 · Speaker 2

and that jump was uh done using the intermediate steps. Is that clear?

### 01:01:40 · Speaker 3

just have a look and let me know if it if it's clear.

### 01:01:44 · Speaker 3

Okay, let us continue then.

### 01:01:45 · Speaker 1

Yes

### 01:02:07 · Speaker 3

Hmm

### 01:02:13 · Speaker 1

again copy this let me write this. plus

### 01:02:23 · Speaker 1

log of

### 01:02:37 · Speaker 1

2 to capital T

### 01:02:39 · Speaker 1

Heat

### 01:02:39 · Speaker 2

of

### 01:02:41 · Speaker 2

xt minus one given xt

### 01:02:44 · Speaker 2

xt minus one given xt, okay? times the denominator of the denominator comes up q of xt minus one given x not.

### 01:02:54 · Speaker 2

divided by

### 01:02:56 · Speaker 2

q of x t minus one given x t and x not times q of x t given x not correct?

### 01:03:07 · Speaker 3

Now observe what happens to this product, no? So this product

### 01:03:19 · Speaker 1

a speed heat of x t minus one given x t times

### 01:03:26 · Speaker 1

What is the

### 01:03:26 · Speaker 2

product

### 01:03:31 · Speaker 4

q of xt minus one given x not

### 01:03:33 · Speaker 2

divided by hold on so this is q of x t minus one given x t and x not okay t equal to two to capital t so this term into we have terms like q of

### 01:03:51 · Speaker 2

uh x two right so this is uh x one given x not into q of x two given x not and so on. in the denominator we have q of x two given x not.

### 01:04:09 · Speaker 2

X three given X not and so on right.

### 01:04:14 · Speaker 2

So these

### 01:04:16 · Speaker 3

terms will cancel out. Only two of the terms will survive. Can you see that?

### 01:04:28 · Speaker 3

So what terms will survive? We will write this down now. Log of

### 01:04:32 · Speaker 2

P X T into P theta of X naught given X one divided by

### 01:04:40 · Speaker 2

Q of X one given X not, okay? plus

### 01:04:47 · Speaker 2

log of only two terms would survive what are those terms? will have q of

### 01:04:54 · Speaker 2

x one given x not. That is the first term that would survive in the numerator. In the denominator we will have q of

### 01:05:04 · Speaker 2

x t given x naught. Okay, everything else will cancel down. The other term that we have is plus log of product of t equal to two to capital T.

### 01:05:20 · Speaker 2

p theta of x t minus one given x t divided by

### 01:05:27 · Speaker 2

Q X T minus one given

### 01:05:31 · Speaker 3

and X not

### 01:05:35 · Speaker 3

Alright

### 01:05:37 · Speaker 3

Is that okay?

### 01:05:44 · Speaker 3

everyone with me so far?

### 01:05:49 · Speaker 2

Okay. So now, uh look at this, no? There is Q of X one given X not, log of, you have log of A B by C, okay? So this is log of A B minus log of C and there is this this term and this term gets cancelled away, right? That's why we took that X one and X not outside in the beginning.

### 01:06:11 · Speaker 2

Okay. Now this will become log of a plus log of b. I can combine them and write that as log of p of x t. Okay.

### 01:06:21 · Speaker 2

Time

### 01:06:22 · Speaker 1

oops

### 01:06:25 · Speaker 1

Uh

### 01:06:41 · Speaker 1

I will just trying to

### 01:06:43 · Speaker 2

to skip one step that's why I was looking at it okay let me skip it anyway. So log of uh log of P theta X not given X one okay plus

### 01:06:56 · Speaker 2

plus log of

### 01:06:59 · Speaker 2

log of V X T divided by

### 01:07:04 · Speaker 2

Q X T given X naught plus

### 01:07:09 · Speaker 2

sum of

### 01:07:11 · Speaker 2

t equal to 2 to capital T

### 01:07:16 · Speaker 2

log of

### 01:07:18 · Speaker 2

log of p theta x t minus one given x t

### 01:07:24 · Speaker 2

divided by

### 01:07:26 · Speaker 2

q of xt minus one given xt and

### 01:07:29 · Speaker 1

not

### 01:07:32 · Speaker 1

Alright, can you see that?

### 01:07:41 · Speaker 3

We are almost done with three more steps

### 01:07:46 · Speaker 3

So note that there was an outer expectation, right? So bringing

### 01:07:56 · Speaker 1

bringing in the outer expectation.

### 01:08:05 · Speaker 3

Okay, so what did we have? We had

### 01:08:08 · Speaker 2

the expectation of it was Q of Z given X right what is Z one two T given X not so this is our Q of Z given X okay and this entire thing this this elbow which is whatever we wrote down log of h h of X not given X one plus

### 01:08:26 · Speaker 2

plus plus those three terms I will not write it again. Okay. Now what is to be noted is this will be equal to expectation of okay log of p theta of x not given x one okay this outer expectation now will be with respect to q of x one given x not why is this

### 01:08:51 · Speaker 2

See while the outer expectation was with respect to Q of X one to T given X not. Since whatever the function that we have are only uh the functions of X not and X one, the outer expectation will become function of X not and X one. Is that okay?

### 01:09:13 · Speaker 2

Alright

### 01:09:15 · Speaker 1

Okay

### 01:09:15 · Speaker 2

Now, similarly to the second term, we'll come to the second term.

### 01:09:19 · Speaker 0

Sir, sorry, I missed to understand that part. Expectation of Q of X one to T X zero became

### 01:09:26 · Speaker 2

given x not will become an expectation with respect to q of x one given x not because the term that you have inside the log no it is independent of all other random variables other than x not and x one

### 01:09:40 · Speaker 0

Okay, yeah.

### 01:09:41 · Speaker 2

Right? Yeah, that is like, like law of expectations. Okay, hold on.

### 01:09:48 · Speaker 1

Okay

### 01:09:54 · Speaker 1

we have

### 01:10:00 · Speaker 1

we have this

### 01:10:01 · Speaker 2

additional expectation argument which can be done okay so hold on okay so this is the first term so the second term would be

### 01:10:10 · Speaker 2

we have the same thing expectation of

### 01:10:14 · Speaker 2

expectation of log of what was that term? P X T divided by Q of X T given X naught. And this expectation is with respect to Q similar argument. We'll take X T and X T minus one given X naught.

### 01:10:38 · Speaker 2

everything else will be going away, correct?

### 01:10:41 · Speaker 4

सर वाई एक्सटी माइनस वन हेयर

### 01:10:47 · Speaker 2

Hello

### 01:10:48 · Speaker 3

Hmm

### 01:10:50 · Speaker 3

QVF I think, yeah, I think I made a mistake here while writing.

### 01:10:57 · Speaker 3

see here

### 01:11:01 · Speaker 3

Oh, this was my mistake, sorry. So here,

### 01:11:05 · Speaker 3

So

### 01:11:05 · Speaker 1

a Q of X not

### 01:11:12 · Speaker 1

Hold on, hold on.

### 01:11:13 · Speaker 3

Uh

### 01:11:14 · Speaker 1

X1 Galaxy

### 01:11:16 · Speaker 1

Here we go.

### 01:11:24 · Speaker 1

Yeah, that should only be X T. Correct.

### 01:11:32 · Speaker 1

This is only Q of X T given X not correct

### 01:11:37 · Speaker 1

Yeah. This is

### 01:11:39 · Speaker 1

what it is

### 01:11:42 · Speaker 1

Right. Now the third term plus

### 01:11:52 · Speaker 1

East

### 01:12:04 · Speaker 1

What dependencies do we have? Let us write it that way.

### 01:12:14 · Speaker 3

Uh, uh

### 01:12:16 · Speaker 2

take the expectation inside the sum because it is linear two to T expectation of we had log of

### 01:12:25 · Speaker 4

from X1 to XT minus 1

### 01:12:27 · Speaker 2

पी थीटा एक्सटी माइनस वन गिवन एक्सटी डिवाइडेड बाय

### 01:12:33 · Speaker 2

Q phi of, no there is no Q phi, sorry. It is Q of

### 01:12:40 · Speaker 2

x t minus one given x t and x not okay. dependency is on q of

### 01:12:49 · Speaker 2

xt, xt minus one given xt, given x not, correct?

### 01:12:54 · Speaker 1

Correct

### 01:12:56 · Speaker 1

is fine no

### 01:13:05 · Speaker 1

Should be all right

### 01:13:11 · Speaker 1

Okay. Now

### 01:13:14 · Speaker 1

one last step. We represent as

### 01:13:33 · Speaker 1

three minus one and x not right. This should be

### 01:13:38 · Speaker 1

Hmm

### 01:13:57 · Speaker 1

just thinking if I have to do it or

### 01:14:03 · Speaker 2

give it as an exercise.

### 01:14:07 · Speaker 2

Okay. See, what we should do is after this, okay, let me write that down. This is equal to, let's write the first term. The first term is expectation of log of P threat of X not given X one. Expectation is with respect to Q of X one given X not. Okay. What is the second term? The second term is simply the KL divergence, no? KL divergence between

### 01:14:33 · Speaker 2

Q of

### 01:14:35 · Speaker 2

st given x not

### 01:14:38 · Speaker 2

and P X T this is by definition.

### 01:14:42 · Speaker 2

And if you look at the third term, the third term is also

### 01:14:47 · Speaker 2

can be written as T equal to two two capital T. There is an expectation with respect to Q of X T given X naught, okay, times

### 01:15:02 · Speaker 2

a KL divergence between

### 01:15:06 · Speaker 2

Q of X T minus one given X T and X not, okay? And

### 01:15:15 · Speaker 2

p theta of x t minus one given x t. Okay. So here is where the tricky part is. I'll tell you that. Okay. The first term and second term are okay no? So the second term here

### 01:15:28 · Speaker 2

This thing is simply the KL divergence, right? By definition, that should be all right, correct?

### 01:15:35 · Speaker 0

minus k l l

### 01:15:36 · Speaker 2

of course of course negative of KL divergence. So now what happened to the third term that's tricky right so what we actually did is here to express this expectation right you have an expectation with respect to Q of XT and XT minus one given X not correct. Okay. You can write this as product of two expectations. Okay. One over an expectation of Q of X T given X naught, okay? Times the expectation over

### 01:16:13 · Speaker 2

Q of

### 01:16:16 · Speaker 1

Okay, I don't have space here.

### 01:16:20 · Speaker 1

X squared four ma

### 01:16:27 · Speaker 1

create some space and write it. Now we have

### 01:16:38 · Speaker 1

expectation of

### 01:16:40 · Speaker 1

something

### 01:16:41 · Speaker 2

thing, right? With respect to we have Q of XT given, sorry, XT and XT minus one given X naught, okay? Now this can be written as product of two expectations. The first expectation is Q of XT given X naught, okay? And the second expectation is with respect to Q of

### 01:17:07 · Speaker 2

xt minus one given xt and x not. This is similar to Bayes rule, okay? This is called the property of conditional expectation.

### 01:17:19 · Speaker 2

You either please take it as a homework or can ask TAs to do this.

### 01:17:25 · Speaker 2

This is a like known result, okay? This is a simple, you can actually write this down. You can write this expectation with you use the Bayes law and use the law of conditional expectations. This is called the law of conditional expectations.

### 01:17:39 · Speaker 2

property of conditional expectations, please have a look at it. Now if I do this and write these this expectation in terms of product of two expectations.

### 01:17:50 · Speaker 2

Then what will happen? uh the outer expectation is still around. Whatever is the inner expectation, no? Which is you will have an expectation of Q X T minus one given X T and X not log of P uh theta of X T minus one given X T divided by Q of X T minus one given X T X not that is the negative of K L, isn't it? between these two distributions.

### 01:18:13 · Speaker 2

Is it all right?

### 01:18:17 · Speaker 1

Do you see how we got the third term?

### 01:18:32 · Speaker 1

Any questions on this?

### 01:18:36 · Speaker 2

Okay. So that's it. I mean we have to now interpret this and compute this. So now what did we do so far is that

### 01:18:44 · Speaker 2

elbow for TDPM.

### 01:18:46 · Speaker 3

Hello

### 01:18:48 · Speaker 3

which is

### 01:18:50 · Speaker 3

only a function of theta

### 01:18:57 · Speaker 3

he wrote that as

### 01:19:00 · Speaker 3

expectation of law

### 01:19:02 · Speaker 2

of

### 01:19:03 · Speaker 2

p theta x naught given x one with respect to q of x one given x naught, okay? minus

### 01:19:14 · Speaker 2

DKL

### 01:19:17 · Speaker 2

Q of X T given X naught and

### 01:19:21 · Speaker 1

EXT

### 01:19:25 · Speaker 1

Minus

### 01:19:28 · Speaker 1

this entire term

### 01:19:41 · Speaker 1

paste

### 01:19:48 · Speaker 4

I think if you long press on the screen and might get an option

### 01:19:52 · Speaker 3

Might get an offer

### 01:19:53 · Speaker 1

Move

### 01:19:53 · Speaker 3

move to tax and then twist

### 01:19:56 · Speaker 2

what what should I do?

### 01:19:58 · Speaker 4

move to text T

### 01:19:59 · Speaker 4

Select T

### 01:20:02 · Speaker 2

select T

### 01:20:04 · Speaker 4

now you can paste

### 01:20:06 · Speaker 2

Oh

### 01:20:09 · Speaker 2

I think you seem to be an expert in this

### 01:20:13 · Speaker 2

How do I move it now?

### 01:20:14 · Speaker 1

I can't move it.

### 01:20:21 · Speaker 1

pain

### 01:20:21 · Speaker 3

full

### 01:20:21 · Speaker 1

Sir

### 01:20:22 · Speaker 1

Hello

### 01:20:26 · Speaker 3

Okay

### 01:20:27 · Speaker 2

This is what we saw. So now it's this is this is all it is you know we are done. Look at the interesting structure no. If you look at the structure what is the first term?

### 01:20:39 · Speaker 2

first term is very similar to the reconstruction term

### 01:20:45 · Speaker 2

B A E right

### 01:20:50 · Speaker 2

X naught is your data, X one is your uh first latent variable. You are reconstructing the data back using the first latent variable, that is the first term. Okay? And what is the second term? The second term is

### 01:21:05 · Speaker 2

same as the prior matching term that we had in the BAE.

### 01:21:12 · Speaker 2

very similar to prior matching because X T so look at this this is like your Q of Z given X right? and P of Z that's exactly how it is.

### 01:21:23 · Speaker 2

First two terms are very similar to the V A E. But the other other thing to that is to be noted is, this second term is completely independent of theta. There is no dependence on theta at all. So you can completely ignore that while while training.

### 01:21:39 · Speaker 2

Okay. What's interesting is the third term, this third term, right?

### 01:21:48 · Speaker 3

ಮಾಡೋಕೆ ಏನಿತ್ತು. ದಿಸ್ ಇಸ್ ಕಾಲ್ಡ್ ದಿ ಕನ್ಸಿಸ್ಟೆನ್ಸಿ ಟರ್ಮ್.

### 01:21:55 · Speaker 3

or they call it the denosing term. or denosing matching term.

### 01:22:07 · Speaker 3

Okay, so look at what is happening.

### 01:22:09 · Speaker 2

okay? So what is happening is that

### 01:22:13 · Speaker 2

at every step T, okay, P theta of X T minus X T minus one given X T is telling you how should the model move to X T minus one given X T. That is what you need to learn. So this is the one that you should learn, okay? So what is this term saying? This term is saying starting from X naught, okay? And given the fact that you have reached X T, tell me what is the distribution of X T minus one. So this is saying given X T

### 01:22:43 · Speaker 2

tell me what should be the distribution of x t minus one. So now if you minimize the k l divergence between these two terms, intuitively what it will lead to is that if you traverse through p theta of x t minus one given x t, you would eventually get to distribution of x not, isn't it?

### 01:23:01 · Speaker 2

because what you are saying is this distribution Q is telling you that

### 01:23:07 · Speaker 2

This is known, okay? This is known. This is telling you that given that I started from X naught and reached XT, what is, what is the distribution on XT minus one? This is telling me that given a given XT, how should I go to XT minus one? So now if I match these two terms, it is actually matching denosing, right?

### 01:23:28 · Speaker 2

this I can call it as matched denosing.

### 01:23:32 · Speaker 2

and this is

### 01:23:35 · Speaker 2

learnability you know I think

### 01:23:40 · Speaker 2

we are whatever we know how to we are we know how to denoise and we are matching that denosing with with the learnable denosing so that we can generate data

### 01:23:51 · Speaker 2

And of course, from a, hold on, hold on, I know this. From a mathematical standpoint, this works because finally what we are doing is minimizing the KL divergence between the model distribution and the data distribution via ELBO optimization. That is what we are doing. Okay? Now, what we will do next is, we will take this consistency or denosing matching term and we will see how to compute it in practice. That is what we will do next. But I hope that you understood what these three terms are in DDPM's ELBO. Okay, any questions here?

### 01:24:25 · Speaker 4

सर हियर हाउ है

### 01:24:25 · Speaker 2

Yeah

### 01:24:27 · Speaker 4

Sir, here how are we evaluating the non denosing term?

### 01:24:33 · Speaker 4

That's the next

### 01:24:34 · Speaker 2

That's the next thing that that's the next thing that we will do. I told you no. It arrived. Now we will see how to compute it. Known denosing term has to be evaluated now. We will do it.

### 01:24:44 · Speaker 3

Hello

### 01:24:46 · Speaker 3

That is what I'll do next.

### 01:24:49 · Speaker 1

Okay

### 01:24:54 · Speaker 1

Yeah, Raghav, go on quickly.

### 01:24:56 · Speaker 3

Yes sir, two steps above.

### 01:24:59 · Speaker 1

Hmm

### 01:25:07 · Speaker 1

Can you make it quick please?

### 01:25:11 · Speaker 4

I mean how that the third sum right I mean how did you change the expectation to X T and X T minus given X not

### 01:25:23 · Speaker 2

Uh that is because similar argument no dependency is only on X T minus X T X T minus one and X not here the expectation was Q of X one through T Q one X not. Okay. See dependence of whatever is inside is only on X T X T minus one and X not isn't it. That's all.

### 01:25:42 · Speaker 4

but the log term that the the numerator term depends on x t minus one given x t.

### 01:25:48 · Speaker 2

but the random variable see that see expectation outer expectation is with respect to x one two three two one two t given x not correct

### 01:25:49 · Speaker 4

Right

### 01:26:02 · Speaker 2

Right. Now what are the terms we can drop in x one to t is the question.

### 01:26:10 · Speaker 2

we can only drop everything other than X T and X T minus one, that's all.

### 01:26:15 · Speaker 4

Okay, so that given XT is also included when we compute expectation.

### 01:26:21 · Speaker 2

Isn't it? See, the the distribution does not change. What changes is the dependency of whatever random variables are not there, you can just omit them from the distribution, joint distribution.

### 01:26:33 · Speaker 2

It's actually writing this joint distribution, right, in terms of, so okay, so what actually is happening is, you see that we wrote it this way, no, where was that?

### 01:26:47 · Speaker 2

Yeah, so we wrote this was the expect this was the distribution with respect to which we need the expectation, isn't it? Okay, hold on, it is still coming up. Correct? This is the distribution with respect to which we need the expectation and we wrote it as a product of so many things, right? Now, when you write it as a product of so many things, whatever distributions that are independent, you can just remove them and they are constants, that's all will happen.

### 01:27:12 · Speaker 2

Okay, what will remove, what will remain are the ones where the dependency is. So there will be Q of XT given X naught and Q of XT minus one given X naught. I have written that as Q of XT, XT minus one given X naught. That's all.

### 01:27:25 · Speaker 0

Okay, yeah.

### 01:27:26 · Speaker 2

makes sense, no? Yeah.

### 01:27:29 · Speaker 2

Okay

### 01:27:30 · Speaker 2

Okay, anything else?

### 01:27:34 · Speaker 2

So now what we will do next is that we will see how to compute this denosing like known denosing term and learnable denosing term and we will build a model that is what we will we are going to do. Why is my screen stuck? Yeah. That is what we are going to do next and that is how you try D D P M and we'll see how to sample from it.

### 01:27:54 · Speaker 2

Okay. Shall we take a break? This is a good time to take a break.

### 01:28:03 · Speaker 2

Okay. uh Shall we make it a shorter break because uh people might have a hard stop at twelve fifteen twelve twenty. We'll make we'll make it a short break. So this is eleven seven in my clock. Let us get back at eleven fifteen, huh? Eleven eleven twenty or eleven fifteen, what do you want?

### 01:28:22 · Speaker 2

1120, let's get back at 1120, okay?

### 01:28:27 · Speaker 1

So please be exactly at eleven twenty, we will continue from here. Okay, see.

### 01:44:18 · Speaker 1

Yeah. Hello all. Shall we continue? Shall we resume?

### 01:44:27 · Speaker 3

Yes sir

### 01:44:30 · Speaker 1

Okay

### 01:44:35 · Speaker 1

Okay. Let us look at the

### 01:44:42 · Speaker 1

What to do is

### 01:45:04 · Speaker 1

to compute the consistency term. So it is simply the KL divergence.

### 01:45:11 · Speaker 1

Between

### 01:45:12 · Speaker 1

U of

### 01:45:15 · Speaker 1

3 minus 1 given next year next month

### 01:45:21 · Speaker 1

and heat of

### 01:45:25 · Speaker 1

T minus one given T

### 01:45:31 · Speaker 1

Yeah. This is what the term is. Okay. First we need to consider

### 01:45:53 · Speaker 1

somebody was asking, no, how to compute this. So let us see how to compute this.

### 01:46:01 · Speaker 1

Okay

### 01:46:03 · Speaker 1

Let us consider this.

### 01:46:13 · Speaker 1

See how to do this. So this, let's use base log.

### 01:46:20 · Speaker 1

is Q of

### 01:46:22 · Speaker 1

sixty

### 01:46:24 · Speaker 1

given x t minus one and x not

### 01:46:33 · Speaker 1

q of x t minus one given x not

### 01:46:38 · Speaker 3

divided by Q of

### 01:46:41 · Speaker 3

x t given x naught this is base law okay.

### 01:46:46 · Speaker 1

What is this equal to? This is equal to q of

### 01:47:15 · Speaker 3

Is this all right?

### 01:47:19 · Speaker 1

because of Marco process, right sir?

### 01:47:24 · Speaker 3

Yeah, it's because of the Markov process.

### 01:47:27 · Speaker 3

xt given xt minus one and x not

### 01:47:29 · Speaker 2

Simply XT, Correct?

### 01:47:31 · Speaker 1

I mean q of x t given x t minus one.

### 01:47:42 · Speaker 1

should be all right? Yeah. Okay. Now,

### 01:47:46 · Speaker 3

So we know how to compute this, no? This we have, this we know what distribution it is. So we have to consider

### 01:47:56 · Speaker 1

the distribution of

### 01:48:03 · Speaker 1

U of

### 01:48:08 · Speaker 1

xt given x not is what we should do

### 01:48:17 · Speaker 1

we need this. Okay? How do we get this is the question.

### 01:48:22 · Speaker 1

actually we can get this

### 01:48:28 · Speaker 1

can be obtained

### 01:48:34 · Speaker 1

using recursion

### 01:48:40 · Speaker 1

show you how. We have

### 01:48:43 · Speaker 1

Okay, so what is this distribution by the way? This is

### 01:48:50 · Speaker 1

distribution of

### 01:48:55 · Speaker 1

Tieth

### 01:48:58 · Speaker 1

latent variable

### 01:49:04 · Speaker 1

Given data

### 01:49:06 · Speaker 1

Right? Okay, how do we get this is the question. So we have

### 01:49:10 · Speaker 3

have

### 01:49:15 · Speaker 3

x t to be equal to root

### 01:49:18 · Speaker 2

root of alpha t times

### 01:49:20 · Speaker 2

xt minus 1 into sorry plus

### 01:49:24 · Speaker 2

root of one minus alpha t times some epsilon where epsilon comes from normal zero one okay. Let me call this as some uh epsilon t minus one okay. I mean this is simply a sample from normal zero one there is nothing sacrosanct about t minus one but let me write it that way just to differentiate it I'll tell you. So this now I can recurse over this no. This is square root of alpha t okay into

### 01:49:53 · Speaker 2

व्हाट इज एक्सटी माइनस वन? रूट ऑफ अल्फा टी माइनस वन।

### 01:50:00 · Speaker 2

times x t minus two plus root of one minus alpha t minus

### 01:50:08 · Speaker 3

minus one

### 01:50:11 · Speaker 3

times

### 01:50:12 · Speaker 2

call this as an epsilon

### 01:50:14 · Speaker 3

minus two

### 01:50:17 · Speaker 3

Plus

### 01:50:19 · Speaker 3

root of 1 minus

### 01:50:20 · Speaker 1

alpha t times epsilon t minus one

### 01:50:27 · Speaker 1

This is all right

### 01:50:34 · Speaker 1

Okay. Now

### 01:50:35 · Speaker 2

this, uh, you can keep recursing this till you get x naught, but we'll have to see, uh, how how how one step of recursion happens and then we can generalize it, okay? So this is equal to

### 01:50:50 · Speaker 2

space to write this. This is equal to

### 01:50:55 · Speaker 2

square root of alpha t

### 01:51:00 · Speaker 2

India

### 01:51:00 · Speaker 3

into

### 01:51:02 · Speaker 3

Alpha T minus

### 01:51:04 · Speaker 1

minus one. Okay.

### 01:51:07 · Speaker 1

xt minus two x t minus two

### 01:51:22 · Speaker 1

Uh

### 01:51:24 · Speaker 1

that is the first term. The second term is

### 01:51:26 · Speaker 2

Plus

### 01:51:29 · Speaker 2

root of alpha t minus

### 01:51:34 · Speaker 2

alpha t times alpha t minus one into epsilon t minus two plus

### 01:51:43 · Speaker 2

रूट ऑफ वन माइनस अल्फा टी टाइम्स एप्सिलॉन टी माइनस वन करेक्ट?

### 01:51:51 · Speaker 3

Hmm

### 01:51:52 · Speaker 3

Okay, now, uh

### 01:51:57 · Speaker 3

it should be done as

### 01:52:02 · Speaker 1

Yeah.

### 01:52:02 · Speaker 3

Okay. So consider these two terms.

### 01:52:10 · Speaker 1

is to terms, okay?

### 01:52:11 · Speaker 3

which is root of

### 01:52:16 · Speaker 2

alpha t minus alpha t into alpha t minus one into epsilon t minus two. So this, this we know.

### 01:52:30 · Speaker 2

is sampled

### 01:52:32 · Speaker 3

from a Gaussian, okay? that has zero mean.

### 01:52:37 · Speaker 3

and

### 01:52:41 · Speaker 3

variants to be equal to alpha t minus alpha t into alpha t minus one

### 01:52:53 · Speaker 3

times I

### 01:52:55 · Speaker 3

Duo

### 01:52:55 · Speaker 2

agree

### 01:52:58 · Speaker 2

Why is this the case? This is because

### 01:53:02 · Speaker 2

again reparameterization, right? So you have a Gaussian, uh you have a scaled Gaussian. So epsilon T minus two is I have to write this one. Epsilon T minus two.

### 01:53:13 · Speaker 2

here

### 01:53:17 · Speaker 2

is again normal zero one okay if it's normal zero one then something scaled with that will become another Gaussian with a different mean and a variance agreed. Okay. So this is one random variable and we have another random variable here which is

### 01:53:34 · Speaker 2

Hmm

### 01:53:37 · Speaker 2

root of

### 01:53:39 · Speaker 2

one minus alpha t times epsilon t minus one this is again Gaussian

### 01:53:47 · Speaker 3

Zero Mean

### 01:53:50 · Speaker 3

variations one

### 01:53:52 · Speaker 3

minus

### 01:53:53 · Speaker 1

alpha t times

### 01:53:55 · Speaker 3

Hello

### 01:53:56 · Speaker 1

I

### 01:54:00 · Speaker 1

Is this okay?

### 01:54:04 · Speaker 1

Okay, now what we have under that

### 01:54:11 · Speaker 1

and color

### 01:54:21 · Speaker 1

even uh it is not a good color.

### 01:54:40 · Speaker 3

Okay

### 01:54:41 · Speaker 1

this term, uh where did that color go?

### 01:54:57 · Speaker 1

T okay.

### 01:55:01 · Speaker 1

corresponds to

### 01:55:17 · Speaker 1

And therefore

### 01:55:21 · Speaker 2

is another another Gaussian random variable. Because sum of two Gaussians are Gaussians you know that right? Gaussian random variable with the following properties. So now T is a Gaussian, okay?

### 01:55:36 · Speaker 2

with

### 01:55:41 · Speaker 2

zero mean, okay, and the variance to be equal to one minus alpha t, alpha t minus one.

### 01:55:50 · Speaker 2

times I. So you can please verify this.

### 01:55:57 · Speaker 2

take some of two Gaussian random variables with these particular mean and variance and add them and see what happens to the variance.

### 01:56:05 · Speaker 2

Okay? So this implies that I can write

### 01:56:10 · Speaker 2

60

### 01:56:12 · Speaker 3

Quick

### 01:56:12 · Speaker 2

as

### 01:56:17 · Speaker 2

Root of

### 01:56:19 · Speaker 2

alpha t into alpha t minus one

### 01:56:24 · Speaker 2

x minus 2 plus another random variable which is 1 minus alpha t alpha

### 01:56:33 · Speaker 2

t minus one

### 01:56:36 · Speaker 2

times some epsilon

### 01:56:40 · Speaker 2

t minus two where epsilon t minus two

### 01:56:46 · Speaker 2

already used epsilon t minus two let's call this as epsilon star t minus two which is Gaussian zero one okay

### 01:56:55 · Speaker 2

So you can simply see what I just did and take a take a minute and let me know if it works.

### 01:57:02 · Speaker 2

So what did we do? X T was given by forward equation, okay? uh just recurse over that. When you recurse over it, you will get a sum of two Gaussian random variables with different means and variances, sorry, different variances means are both zero. And we combine those two and reparameterize it into another Gaussian random variable. And we got that final equation.

### 01:57:26 · Speaker 3

is it all right? Any questions on this?

### 01:57:35 · Speaker 3

should be fine, no? It's easy. Yeah. So now I can do this again, go recursively. I can keep doing this. This implies that my X T, zoom it now.

### 01:57:50 · Speaker 3

implies that my XT, XT can be written as

### 01:57:55 · Speaker 1

Root of

### 01:57:57 · Speaker 3

Alpha T, Alpha T minus one up to

### 01:58:09 · Speaker 1

Alpha

### 01:58:12 · Speaker 1

one right

### 01:58:12 · Speaker 3

Right

### 01:58:13 · Speaker 1

Alpha

### 01:58:14 · Speaker 2

One

### 01:58:16 · Speaker 3

या अल्फा वन टाइम्स एक्स नॉट ओके प्लस रूट ऑफ

### 01:58:23 · Speaker 3

one minus product of

### 01:58:27 · Speaker 3

I can

### 01:58:32 · Speaker 3

the product later.

### 01:58:35 · Speaker 2

1 minus

### 01:58:36 · Speaker 2

अल्फा टी सेम थिंग। अल्फा टी, अल्फा टी माइनस वन अप टू अल्फा वन टाइम्स एप्सिलॉन।

### 01:58:47 · Speaker 2

Hmm

### 01:58:47 · Speaker 1

is equal to root of sum

### 01:59:00 · Speaker 1

equal to one two T alpha I.

### 01:59:04 · Speaker 2

sin x not plus plus

### 01:59:08 · Speaker 3

root of

### 01:59:10 · Speaker 2

वन माइनस

### 01:59:13 · Speaker 2

equal to one two T

### 01:59:17 · Speaker 2

alpha i times some epsilon. This is equal to

### 01:59:22 · Speaker 2

root of alpha t bar times x naught plus root of

### 01:59:30 · Speaker 2

one minus alpha t bar

### 01:59:35 · Speaker 2

Thanks

### 01:59:36 · Speaker 3

Epsilon

### 01:59:38 · Speaker 3

where

### 01:59:42 · Speaker 2

root of alpha or rather alpha t bar is the product of all that

### 01:59:49 · Speaker 3

alpha t

### 01:59:50 · Speaker 2

bar is the product of all the alphas up to up to T.

### 01:59:58 · Speaker 3

Okay

### 01:59:59 · Speaker 3

Hello

### 02:00:00 · Speaker 4

this is an equation. So now, what does this actually mean? Okay, let me write it

### 02:00:08 · Speaker 4

distribution and also then interpret where alpha is zero normal zero one. So this implies that we have Q of X T given X naught. What is this?

### 02:00:21 · Speaker 4

What is this? This is equal to this is a normal distribution again because this you know reparameterization. The distribution at X T the mean is root of alpha T bar times X naught. Okay? And the variance is

### 02:00:38 · Speaker 0

one minus alpha t bar

### 02:00:41 · Speaker 0

friends

### 02:00:46 · Speaker 0

Hi

### 02:00:55 · Speaker 0

note what where did we come from

### 02:00:57 · Speaker 4

we wanted to compute the consistency term and we we had this known denosing term and we used base law to do that. So for that we wanted Q of XT given X not and XT given X not is computed recursively. See this actually means that

### 02:01:18 · Speaker 4

the

### 02:01:20 · Speaker 0

Piet

### 02:01:23 · Speaker 0

Latent

### 02:01:25 · Speaker 0

sample to latent sample

### 02:01:30 · Speaker 0

the t-th latent sample is also t-th noisy sample, no?

### 02:01:41 · Speaker 0

in the forward encoding or the forward process

### 02:01:55 · Speaker 0

process can be obtained

### 02:02:03 · Speaker 0

in one step

### 02:02:16 · Speaker 0

Okay

### 02:02:21 · Speaker 0

without

### 02:02:27 · Speaker 0

adding the noise.

### 02:02:32 · Speaker 0

T times

### 02:02:35 · Speaker 4

So this is actually because of recursion, that's all, right? He used the above recursion and found out that the Tth latent variable in the forward diffusion process can be obtained in one step starting from X not without having hop, without having to hop the the Markov chain for T steps.

### 02:02:59 · Speaker 4

All right. Is this okay?

### 02:03:04 · Speaker 4

is another consequence of of having this first order Markov chain with recursion.

### 02:03:08 · Speaker 0

right? You can we can do it that way.

### 02:03:16 · Speaker 0

Yeah, Raghavender

### 02:03:18 · Speaker 2

So did we just prove that a Gaussian of Gaussian is also a Gaussian?

### 02:03:23 · Speaker 4

What do you mean by Gaussian of Gaussian?

### 02:03:25 · Speaker 2

because I mean we are taking so if you if you look at the steps right? So X two is obtained by taking a sample from a Gaussian and then X three is obtained

### 02:03:35 · Speaker 4

Where is x two? No no, x two is not from epsilon is from Gaussian no. x two is not from Gaussian.

### 02:03:42 · Speaker 2

But if you see the forward Markov chain, I mean that's what we do, right? We take a Gaussian of the result and then again sample from another Gaussian.

### 02:03:52 · Speaker 4

I'm not getting what you're saying. See, X X T is obtained by this equation, no? Where is another Gaussian here?

### 02:04:00 · Speaker 2

Yeah, but then it it depends on ultimately it depends on X not, right?

### 02:04:06 · Speaker 4

Of course it has so

### 02:04:08 · Speaker 2

in between we are applying multiple Gaussians. right?

### 02:04:08 · Speaker 4

What is the question?

### 02:04:14 · Speaker 4

we're not applying any Gaussians, no, you take X naught and sample from a Gaussian distribution and add it to X naught, that's what we are doing.

### 02:04:23 · Speaker 2

Yeah, and and we keep doing that.

### 02:04:25 · Speaker 4

there is no application of Gaussian. We are sampling from Gaussian, adding a Gaussian. Yeah, that we are doing. So,

### 02:04:33 · Speaker 2

I mean does it mean that uh ultimately see see that the last result that we get is again a Gaussian right with a different parameters

### 02:04:42 · Speaker 4

last result

### 02:04:42 · Speaker 2

last result

### 02:04:44 · Speaker 2

So, yeah, this distribution of XT

### 02:04:45 · Speaker 4

distribution of x t correct that is a Gaussian so

### 02:04:50 · Speaker 2

and the intermediate steps were also Gaussian. Correct. So with with the different parameters. So my question was did we did we just say that if we keep taking Gaussian and then sample and then again take again keep sampling from a different Gaussians. The end result is the again sampling from a single Gaussian.

### 02:04:54 · Speaker 4

Correct. So

### 02:04:57 · Speaker 4

next

### 02:05:10 · Speaker 4

That is reparameterization, no?

### 02:05:13 · Speaker 2

Yeah. So that was my question. I mean, that was my point.

### 02:05:14 · Speaker 4

Yes

### 02:05:17 · Speaker 4

Hi, okay. So it is not a question, I was expecting a question.

### 02:05:21 · Speaker 2

it was not a question. it was not a question. it was just confirm whether my

### 02:05:23 · Speaker 4

confirm whether my idea. Yeah, making an observation. Yes, yes, yes, correct. Yeah. So now you can reparameterize any any amount of Gaussian addition in terms of Gaussian.

### 02:05:32 · Speaker 0

That's all it means. Yeah.

### 02:05:44 · Speaker 0

Okay. Anything else? Okay.

### 02:05:47 · Speaker 4

So now what did we do is we now know let's get back to this. Our goal was to get the

### 02:05:54 · Speaker 0

Hello

### 02:05:55 · Speaker 4

Uh

### 02:05:58 · Speaker 0

consistency term estimated no? So now we had

### 02:06:27 · Speaker 0

This is the distribution that we had in the K L, right? So this is equal to

### 02:06:58 · Speaker 0

is by Bayes' law, okay? And then we use the

### 02:07:02 · Speaker 4

markovian property here this is q of x t given x t minus one times q of x t minus one given x not

### 02:07:16 · Speaker 4

divided by

### 02:07:18 · Speaker 4

Q of

### 02:07:21 · Speaker 4

sixty given x not. Okay? This is what it was. Okay? Now, uh

### 02:07:28 · Speaker 4

Do we know the first term we do? What is that? That is the definition of the forward process. Now it's Gaussian at X T and we have root of alpha T times X T as the mean.

### 02:07:43 · Speaker 4

the variance was one minus alpha t

### 02:07:49 · Speaker 4

minus alpha t times i. So the variance. Correct? That was the first term. What about the second term? We just found that out, right? Here, we found out what q of x t given x naught was. That was another Gaussian with a certain mean and variance. Let us write that down.

### 02:08:07 · Speaker 4

So this is Q of X T minus one given X naught no that is another Gaussian

### 02:08:13 · Speaker 4

uh Gaussian is at x t minus one that's the random variable. The mean is root of alpha t minus one bar times x not. Okay? And the variance is one minus alpha t minus one bar

### 02:08:32 · Speaker 0

part

### 02:08:33 · Speaker 0

times I

### 02:08:39 · Speaker 0

comes from here, okay?

### 02:08:42 · Speaker 0

comes from

### 02:08:43 · Speaker 4

whatever we just derived through uh recursion. And in the denominator we have another Gaussian.

### 02:08:50 · Speaker 3

सर, सॉरी टू इंट्रप्ट। द फर्स्ट टर्म इट शुड बी रूट ऑफ अल्फा टी इंटू एक्सटी माइनस वन।

### 02:08:51 · Speaker 4

Yeah

### 02:08:58 · Speaker 4

Correct

### 02:09:12 · Speaker 0

root of alpha t into x

### 02:09:15 · Speaker 4

Hello

### 02:09:16 · Speaker 0

see when

### 02:09:16 · Speaker 4

correct. Thank you for the correction. So this is X T root of alpha T bar

### 02:09:24 · Speaker 4

times x naught. That's the mean and the variance is one minus alpha t bar times i.

### 02:09:34 · Speaker 0

Okay

### 02:09:35 · Speaker 4

is what? uh What is the LHS? LHS is Q of

### 02:09:41 · Speaker 4

xt minus one given xt and x not. This is what we called as the known denosing term, right? That's what it is. Okay, now, look at this. See, this is if all the terms have things like this, no, you have e power minus

### 02:09:58 · Speaker 4

some quadratic term, no? You have X T minus some mean time. Or rather, it's all identity, so it will be like this. It will be

### 02:10:13 · Speaker 4

X T

### 02:10:14 · Speaker 0

minus

### 02:10:16 · Speaker 0

Come in

### 02:10:18 · Speaker 0

squared okay

### 02:10:20 · Speaker 0

Okay

### 02:10:21 · Speaker 0

times e power

### 02:10:24 · Speaker 4

minus

### 02:10:27 · Speaker 4

x t minus 1 minus some other mean

### 02:10:32 · Speaker 0

Square

### 02:10:33 · Speaker 0

divided by same thing e power minus

### 02:10:46 · Speaker 4

and so on, right? Now, um see, observe that the distribution that we have in the left side is a distribution on x t minus one, okay? What should we do now? Can somebody suggest what should we do now?

### 02:11:01 · Speaker 4

And we know all these means, right? We know all these means and variances.

### 02:11:05 · Speaker 0

What should we do now?

### 02:11:12 · Speaker 0

So what to be done is

### 02:11:15 · Speaker 0

E power

### 02:11:19 · Speaker 0

minus

### 02:11:21 · Speaker 0

xt minus one

### 02:11:27 · Speaker 0

c minus one

### 02:11:29 · Speaker 0

minus some mean

### 02:11:45 · Speaker 0

express it this way, okay? Now how do we do that?

### 02:11:48 · Speaker 4

this we do by what is called as completing the square

### 02:11:54 · Speaker 4

Because all of you know how to complete the square, what do you mean by completing the square?

### 02:11:59 · Speaker 4

This means that suppose you have a term a quadratic term like this no ax squared plus bx plus c okay. You can always add some let's say some uh d times x minus d times x. You can add and subtract things and write this in terms of say x minus some p squared plus some constant you know this no this is called completing the square.

### 02:12:24 · Speaker 4

Right? So whatever expressions we have inside the exponentiation, we need to complete the square in terms of x t minus one, okay? We'll get some mean and some variance.

### 02:12:36 · Speaker 4

is that all right? Can all of you see that?

### 02:12:44 · Speaker 4

Let me show you the calculations. I will skip the calculations. You can simply go through that. I will just show you that.

### 02:12:53 · Speaker 4

two it later.

### 02:12:54 · Speaker 3

सर, व्हाट अबाउट द एक्सटी टर्म?

### 02:12:57 · Speaker 4

xt term will become a constant, right? Because the LHS is conditioned on xt. So xt is xt is given a particular xt which is a constant. As far as xt minus one is concerned, okay?

### 02:13:12 · Speaker 3

Yes sir

### 02:13:13 · Speaker 0

Okay, can you see my screen?

### 02:13:24 · Speaker 4

Hello, can you see my screen? Do you see my screen?

### 02:13:27 · Speaker 0

Yeah

### 02:13:28 · Speaker 2

Yes sir

### 02:13:29 · Speaker 4

this is what I'm talking about. See, uh we have these three Gaussians, right? There is one Gaussian uh for Q X T given X T minus one X naught, there is one Gaussian for the second distribution and one for the third. So you have to write down all these Gaussian distributions and use the appropriate means and variances and you should you should simply complete the square. This is the uh the calculation that I'm skipping. See, it's only algebra, okay? It's like high school level algebra. Please follow this. I have given

### 02:13:59 · Speaker 4

this paper to you, okay? So please see this algebra. Finally what will happen is this will become a Gaussian distribution, okay? With a certain mean and a certain variance because you have completed the square and you can look at this, no? This all you have to do is rearrange the terms, add and subtract the terms such that it will become, it will assume a Gaussian distribution form and you should read out the mean and variance. That's all you should do.

### 02:14:23 · Speaker 4

Is that okay? So please follow that. I will skip this and only write the the final mean and variance because it's simply an algebra. Did you understand all of you?

### 02:14:35 · Speaker 4

not complicated, you just have to run through the algebra.

### 02:14:41 · Speaker 4

Alright, is it okay?

### 02:14:45 · Speaker 4

you can go through it and if you don't get it you can always come back to me I will tell you. It's not at all difficult.

### 02:14:51 · Speaker 0

easily understand that

### 02:14:52 · Speaker 0

Shear screen

### 02:15:06 · Speaker 0

Now this term will become so Q of

### 02:15:27 · Speaker 0

next minus one given

### 02:15:31 · Speaker 0

xt and x not now became a constant distribution, right?

### 02:15:40 · Speaker 4

is a Gaussian distribution. Okay. Distribution is at x t minus one.

### 02:15:45 · Speaker 4

the mean is let's call that as mu q, okay? And that will be that will be a function of x t and x not because these are conditioned on x t and x not. And there will be some variance, call it as some sigma q. This will only be a function of t or alpha t, it will be independent of this thing. I'll I'll write down what these are. Where the mean of this distribution mu q

### 02:16:11 · Speaker 4

the function of x t and x naught is given by

### 02:16:16 · Speaker 0

root of alpha t

### 02:16:19 · Speaker 0

into one minus

### 02:16:25 · Speaker 0

p minus 1

### 02:16:28 · Speaker 0

two sixty plus

### 02:16:42 · Speaker 0

into x naught

### 02:16:45 · Speaker 0

divided by one minus alpha t bar

### 02:17:24 · Speaker 0

That's all. Now note that the both of these terms, right, both of these terms are

### 02:17:31 · Speaker 4

Phone

### 02:17:33 · Speaker 4

and computable, no?

### 02:17:37 · Speaker 4

So now this means that this known denosing term can be computed. So we know alphas, we know XT, we know X not, we know all of this. So that can be computed. So this is typically written as some sigma Q squared times

### 02:17:53 · Speaker 4

identity, awareness.

### 02:17:56 · Speaker 4

this entire thing is written as sigma q squared is a constant, okay? That is what is done. uh any questions so far? I think this is fine, no? Now, what did we do? So we wanted that that third term in the elbow was

### 02:18:15 · Speaker 4

scale between

### 02:18:17 · Speaker 4

xt minus one. Given xt and x not. And we had p theta of

### 02:18:26 · Speaker 4

xt minus one given xt okay

### 02:18:29 · Speaker 0

is what we had. Okay. Now, in a DDPM,

### 02:18:40 · Speaker 0

the decoding distribution

### 02:18:44 · Speaker 0

it's called decoding distribution or

### 02:18:47 · Speaker 0

denoizing distribution

### 02:18:51 · Speaker 0

it's it's also called the reverse process

### 02:18:59 · Speaker 0

this process is assumed to be a Gaussian

### 02:19:17 · Speaker 0

This implies F

### 02:19:21 · Speaker 0

speed heat of

### 02:19:24 · Speaker 0

xt minus one given xt

### 02:19:28 · Speaker 0

Okay.

### 02:19:29 · Speaker 4

is a Gaussian

### 02:19:32 · Speaker 4

x t minus one with a mean mu theta. So this mu theta and the variance, the variance of this is assumed to be equal to equal to constant. Constant means it is assumed to be equal to what the true thing is. So only the mean is estimated, variance is assumed to be constant in the uh in the normal course, okay, in the literature variance is assumed.

### 02:19:56 · Speaker 0

to be a constant, okay?

### 02:20:10 · Speaker 0

Okay

### 02:20:11 · Speaker 4

Now what happened is that because it's Gaussian, so we have the scale divergence

### 02:20:20 · Speaker 4

between Q

### 02:20:23 · Speaker 4

c minus one given

### 02:20:26 · Speaker 4

Tipsy index

### 02:20:27 · Speaker 0

Plant, Okay?

### 02:20:29 · Speaker 0

and E theta of

### 02:20:33 · Speaker 0

x three minus one given x t.

### 02:20:41 · Speaker 0

is now

### 02:20:43 · Speaker 0

a KL divergence between

### 02:20:49 · Speaker 0

Gaussian

### 02:20:55 · Speaker 0

parameter is that mu q and sigma q

### 02:21:00 · Speaker 0

And this is a Gaussian that is parameterized.

### 02:21:07 · Speaker 0

as mu theta and sigma cube.

### 02:21:15 · Speaker 0

Is this all right?

### 02:21:19 · Speaker 0

So KL

### 02:21:20 · Speaker 0

between two Gaussian distribution

### 02:21:21 · Speaker 0

institutions is

### 02:21:23 · Speaker 0

known to be

### 02:21:24 · Speaker 0

can be analytically computed

### 02:21:26 · Speaker 0

is given by half log

### 02:21:44 · Speaker 0

determinant of sigma q

### 02:21:48 · Speaker 0

minus D where D is the data dimensionality. plus trace of

### 02:21:55 · Speaker 0

Sigma Q

### 02:21:58 · Speaker 0

Inverse

### 02:22:00 · Speaker 0

It mark you

### 02:22:03 · Speaker 4

plus

### 02:22:04 · Speaker 0

Hello

### 02:22:05 · Speaker 4

μ θ − μQ ट्रांसपोज

### 02:22:10 · Speaker 4

quadratic form sigma q inverse mu theta minus mu q

### 02:22:17 · Speaker 4

can just take this as a homework and do it. Show that the Gaussian distribution between two uh sorry KL divergence between two Gaussian distributions can be computed this way. This is equal to

### 02:22:32 · Speaker 4

Half

### 02:22:34 · Speaker 4

This is log one which is zero. So like okay let me write it log one minus d trace of inverse of sigma q inverse times sigma is also equal to d that can be shown.

### 02:22:50 · Speaker 4

because it's just constant times identity, you know, d dimension, it will just add up to be d. Traces the sum of the diagonal elements if it's a diagonal matrix. Plus, so this log one will go away, these two d will go away. Sigma q inverse is a So you have mu theta minus mu q transpose, okay? So this is small sigma q squared i, this is what we have written that as. This is mu theta minus mu q

### 02:23:24 · Speaker 4

Okay, it's all. So this will be equal to half

### 02:23:30 · Speaker 4

is an inverse here okay. So it will be uh two

### 02:23:34 · Speaker 0

Sigma Q squared times

### 02:23:40 · Speaker 0

Normal

### 02:23:42 · Speaker 0

u theta minus u whole square

### 02:23:47 · Speaker 4

actually the elegance and beauty of D D P M that after doing all that the final denosing matching term will simply be a mean squared draw between two means.

### 02:24:05 · Speaker 4

That's all actually we are done you know we there is the other the rest of the things that we do is only some re-parameterizations and we'll see how to implement this using a neural networking while. Any questions here? Yeah. Sanchit.

### 02:24:22 · Speaker 3

Sir, why are we assuming that the decoding distribution is Gaussian? And like in a general sense

### 02:24:29 · Speaker 4

In general because

### 02:24:31 · Speaker 4

I'll tell you that is because see we are not assuming the distribution of data to be Gaussian we are only assuming the conditional of the latent given another latent to be Gaussian okay that is one thing why are we doing that assumption is that

### 02:24:46 · Speaker 4

What can be shown is if you have a forward Markov chain, okay, with Gaussian transitions, there exists a reverse Markov chain that also has Gaussian transitions is something that can be shown.

### 02:24:59 · Speaker 4

Okay? But what changes is the parameters.

### 02:25:05 · Speaker 4

or changes as the parameters. So one is mu theta, the other is some other parameter, no? So but what can be shown is that if the if you have a Markov chain whose forward distribution is uh Gaussian, transitions are Gaussians. Okay? Then the backward distribution uh is also Gaussian with a different parameters.

### 02:25:30 · Speaker 3

Okay sir, sir like in V A E also we try to assume like what I am trying to understand

### 02:25:36 · Speaker 4

distribution

### 02:25:39 · Speaker 3

Sorry sir, please continue.

### 02:25:41 · Speaker 0

Hmm

### 02:25:42 · Speaker 3

Sir, like for V I also, like we were trying to, uh you know, mode like assume that the latent space will be a Gaussian distribution, like a normal distribution. And, you know, so like why are why are we so much biased towards a Gaussian distribution in almost all of the models?

### 02:25:55 · Speaker 4

Yeah

### 02:26:03 · Speaker 4

No, no, uh, see that is a design choice. You can see while in a, uh, naive VAE, we assumed it to be Gaussian, but in all VQ VAE and the other VAMPRIOR etcetera, it can be modeled as something else, right? Similarly, see, but here what you should see is, uh, that the stationary distribution here, which is the distribution of the Tth latent is assuming, is assumed to be Gaussian. We are not assuming the intermediate distribution to be Gaussian, but only the conditionals are assumed to be Gaussian. which is okay

### 02:26:35 · Speaker 4

I mean, why are we assuming it to be Gaussian is because like it's an isotopic distribution, right? I mean, uh it it is a distribution that has infinite support, so it is easy to work with. There are diffusion models where they have used another uh I mean other exponential family of distributions. But they lead to a similar thing because see, note that nowhere we are assuming that P of X not is Gaussian. This is not Gaussian at all.

### 02:27:04 · Speaker 4

Right. So P theta of X naught which is our data distribution is actually given by the product of all those distributions right? We know that uh we can use the chain rule and do it. So the conditionals are assumed to be Gaussian which is okay. You can have conditional to be Gaussian and you can use the Gaussian conditionals to model any distribution of interest.

### 02:27:28 · Speaker 4

So that way, I mean, if your question is that isn't Gaussian as Gaussianity assumption restrictive here, it is not restrictive at all. It can model any distribution, only the conditionals are assumed to be Gaussian. Now, why are we doing that choice in in in in the reverse process of DDPM is because what can be shown is that if you if you construct a Markov chain with Gaussian transitions in the forward direction, the reverse transition also happens to be Gaussian, okay, with different set of parameters is a known result.

### 02:28:01 · Speaker 4

Is it all right?

### 02:28:02 · Speaker 0

ओके सर

### 02:28:02 · Speaker 2

Sir, the reverse process is not deterministic or?

### 02:28:07 · Speaker 4

It is not no we are finding out mu theta here. It is parameters by mu theta we will find that out no.

### 02:28:14 · Speaker 4

See, now finally what we are finding out is this mu theta. Mu theta is something that we find out.

### 02:28:21 · Speaker 2

But that cannot be arrived at analytically or

### 02:28:24 · Speaker 4

No no no no that is our model right? That is that is the whole point. If you start look at the forward process

### 02:28:31 · Speaker 2

the forward process that we said is is fixed

### 02:28:34 · Speaker 4

is known. Of course it is fixed. You see this? You see this?

### 02:28:35 · Speaker 2

Yeah

### 02:28:40 · Speaker 4

P theta, mu theta and sigma theta are learnable. But in practice what they do is they they make sigma theta a fixed thing, only mu theta is learned.

### 02:28:51 · Speaker 4

That is our model. See, if you make the reverse process also fixed, then what is what you are you learning?

### 02:28:58 · Speaker 2

Yeah, understood.

### 02:29:00 · Speaker 4

Hmm

### 02:29:01 · Speaker 2

Yeah, understood, sir.

### 02:29:03 · Speaker 4

Yeah. Is this okay? So finally, it all boils down to, I think I'm doing a multi-scale thing here, right? One thing is at some scale, the other is other scale. You look at this.

### 02:29:17 · Speaker 4

I think I

### 02:29:20 · Speaker 4

zoom it inadvertently somewhere it will become that should not be an issue for you know when you go back and look into it I think you can you can also zoom out and zoom in and look into that in different scales I suppose right

### 02:29:37 · Speaker 0

Yes sir, but we can't take printouts. It's okay.

### 02:29:38 · Speaker 4

between

### 02:29:42 · Speaker 4

Oh, because of the scale issue. Because of the scale issue.

### 02:29:44 · Speaker 2

because of the scale issue. because of the scale issue.

### 02:29:47 · Speaker 4

I see. Okay. So how did

### 02:29:48 · Speaker 2

Don't do that. So how did

### 02:29:51 · Speaker 4

Come again?

### 02:29:52 · Speaker 2

we don't print that much but if uh sometimes we like to take a print out uh then taking a form PDF yeah

### 02:29:57 · Speaker 4

Okay, so I think

### 02:30:00 · Speaker 2

positive

### 02:30:00 · Speaker 4

positive side of it is you know I'm helping environment so it's fine. Okay. So is this all right? So what happened is that finally

### 02:30:08 · Speaker 2

Yeah

### 02:30:12 · Speaker 0

this elbow thing

### 02:30:18 · Speaker 0

Boil down to

### 02:30:27 · Speaker 0

there was this term,

### 02:30:50 · Speaker 0

That's all, right? You'll have to minimize this.

### 02:30:52 · Speaker 4

So, of course, there is that another term, no, this was minus KL, there was this term of expectation of log of theta of

### 02:31:04 · Speaker 4

X one given X not. This was also one term. That's all, right? So these are the two last terms that are that is there in the elbow. So we'll have to now implement these two things using neural networks. Okay? And then when like we'll

### 02:31:25 · Speaker 4

estimate these two terms, minimize them and then learn how to sample from it. See, uh those two things have to be done. I need at least half an hour to do that. uh Shall we stop here? Because it will be nice if if I do it in one stretch. I'll do it in the next class.

### 02:31:43 · Speaker 4

So the only problem is I wanted to do that today because I was planning to give your assignments out on like like Sunday which is tomorrow.

### 02:31:56 · Speaker 4

Okay, maybe I'll quickly tell you how to do that so that you can like start looking at your data, building these things. Okay? Shall I take ten more minutes?

### 02:32:10 · Speaker 0

Okay, so that at least you know how to train this.

### 02:32:27 · Speaker 0

The

### 02:33:03 · Speaker 0

Okay

### 02:33:05 · Speaker 4

Right. Now, let's do this reparameterization. We can actually implement it this way, but people generally implement it in a different reparameterization. Let us do that. We have reparameterizing.

### 02:33:19 · Speaker 3

सर, देयर विल बी द के एल डाइवर्जेंस टर्म आल्सो, राइट? थर्ड वन।

### 02:33:23 · Speaker 4

No, that is, the third one is what we showed as this difference between the means. Second one. Yeah. That is independent of theta, no? We can we ignored that.

### 02:33:27 · Speaker 3

No no no sorry

### 02:33:30 · Speaker 3

That is

### 02:33:32 · Speaker 3

ignore that

### 02:33:34 · Speaker 4

Hello

### 02:33:37 · Speaker 3

So sir, what what will be its use for like which which term which component will it be used for updating in the D D P M?

### 02:33:49 · Speaker 4

what I didn't get the question which term what will be used for

### 02:33:52 · Speaker 3

सर, द के एल डाइवर्जेंस टर्म दैट वाज़ इंडिपेंडेंट ऑफ थीटा, आर वी सेइंग दैट वी वोंट बी यूजिंग इट एनीवेयर फॉर अपडेटिंग द...

### 02:33:57 · Speaker 4

We say

### 02:34:02 · Speaker 4

Yeah, because model training of course, no, it is independent, we don't, there is no model at all, there is no dependence on model. It is a constant as far as the model is concerned.

### 02:34:10 · Speaker 3

ओके सर

### 02:34:11 · Speaker 4

This comes because of the fixed forward process, right? And also, yeah, this primarily comes from fixed forward process. Okay. So, I will maybe quickly tell you what this is and hand wave and do the maths the next time, okay, so that you can start implementing. See, what's the idea is you have this term, no? You have mu theta minus mu q as your loss, okay? Now, what is done is we have this mu q as what is mu q? Some constant C one time

### 02:34:41 · Speaker 4

times x t, I had written that. Some other constant times x not divided by some constant, right? Or rather I can write it as a some linear combination of x one and x not. This is how mu q was, correct? Now we have x t to be equal to, we used that recursion and showed that x t was equal to root of alpha t times x not, okay? x not सो, प्लीज पे अटेंशन हियर बिकॉज़ दिस इस व्हाट आई विल आस्क यू टू इम्प्लीमेंट, ओके? एक्स नॉट।

### 02:35:22 · Speaker 4

plus

### 02:35:23 · Speaker 4

root of one minus alpha t bar times epsilon this is how it was correct. Now if I rearrange these terms I can write x not in terms of x t minus root of one minus alpha t bar times epsilon divided by

### 02:35:40 · Speaker 4

root of alpha t bar, okay? This implies that my mu q now can be written, okay? in terms of

### 02:35:52 · Speaker 4

I can get rid of x naught, right? I can write this as some other constant k one times x t. Okay? Minus or plus some other constant times epsilon. Do you agree?

### 02:36:08 · Speaker 0

All of you agree on this?

### 02:36:13 · Speaker 0

Hello

### 02:36:18 · Speaker 0

Am I there?

### 02:36:19 · Speaker 4

audible? Yeah. Okay, so this is all it is. So this implies that I have my mu theta, right? mu theta which is a function of XT. I can also write this as, okay? some constant K1 times XT plus

### 02:36:34 · Speaker 4

okay? uh k two times some epsilon theta. okay? which is a function of x t and t. so what am I saying is the following.

### 02:36:45 · Speaker 4

Now, see, mu theta or mu theta was the mean of a Gaussian random variable, correct? Okay?

### 02:36:55 · Speaker 4

right? I can always reparameterize that in terms of some other constant X T, isn't it?

### 02:37:04 · Speaker 0

Do you see what that means? This is reparameterization.

### 02:37:13 · Speaker 0

you get the idea

### 02:37:17 · Speaker 0

idea is

### 02:37:19 · Speaker 4

that mu theta was the mean of a Gaussian random variable, okay? I can always reparameterize that in terms of some other constant XT, isn't it?

### 02:37:30 · Speaker 4

I just have to arrange this K one and K two terms. So I'll just simply retarget and materialize them.

### 02:37:37 · Speaker 4

ओके, ओके, एंड

### 02:37:42 · Speaker 4

theta, right? That would get designated into this epsilon theta.

### 02:37:50 · Speaker 4

Basically what I've done is I've written this mu theta in terms of some epsilon theta and

### 02:37:56 · Speaker 4

Constant Times X T

### 02:37:59 · Speaker 4

Is that okay?

### 02:38:04 · Speaker 4

Okay. So now this implies that my

### 02:38:09 · Speaker 4

last that I had no mu theta minus mu q now becomes proportional to

### 02:38:16 · Speaker 0

epsilon minus

### 02:38:19 · Speaker 0

Chan theta

### 02:38:22 · Speaker 0

Correct

### 02:38:28 · Speaker 0

Trade

### 02:38:30 · Speaker 4

because those constants will get cancelled away, no? We have like reparameterize mu theta also in terms of the same constant as that of mu q. So those constants x t gets cancelled away. So it will only be in terms of epsilon and epsilon theta cap.

### 02:38:48 · Speaker 0

is this clear to all of you?

### 02:39:02 · Speaker 0

Hello

### 02:39:07 · Speaker 0

Okay, so now how do you implement this in practices?

### 02:39:10 · Speaker 4

You have a

### 02:39:12 · Speaker 4

So please note that the dimensionality of

### 02:39:16 · Speaker 4

I will do it like more thoroughly in the next classes just to ensure that you will get started with your assignment, okay? You will have a neural network, okay? Theta neural network. This will have this kind of architecture is called the U-net architecture where the dimensions will keep on decreasing, hit a bottleneck and the dimensions will again keep increasing, okay? This is because the size of noise here epsilon is same as that of the input, okay? So now what does it take as input? It will take input T and T, okay? And this will predict

### 02:39:50 · Speaker 4

epsilon eight. That is all. That is all the training of DDPMS. The last function is epsilon minus

### 02:40:00 · Speaker 4

epsilon theta cap x t, t. Okay? Now what is x t? x t is as we know root of alpha t bar x not.

### 02:40:10 · Speaker 4

plus one minus alpha t bar times epsilon. That's all. This is how you train. How do you do it?

### 02:40:18 · Speaker 4

Take an x naught. Okay.

### 02:40:20 · Speaker 0

and

### 02:40:25 · Speaker 0

Compute

### 02:40:28 · Speaker 0

take x naught, sample epsilon from normal zero one. Okay? Compute x t using this equation.

### 02:40:43 · Speaker 0

Okay. So give that give that XT as an input to the neural network.

### 02:40:54 · Speaker 0

and whatever the output is

### 02:40:55 · Speaker 4

match that output with the epsilon noise that you have added. That's all the DDPM training is. Then you back propagate. And you do it for multiple T's.

### 02:41:09 · Speaker 4

you are minimizing the elbow. Is this clear? See, I I mean okay, I will not take any questions now because it's twelve twenty. uh we will start from this the next class, okay? I will tell you like precisely what the architecture is and how do you do this, what the loss function is and all that. But this is all it is, right? So basically what's happening is given a data point, you add some noise to it, okay? And you get the Tth latent variable, pass that through a neural network and try to predict what was the amount of noise that was added to it. this X T from X naught. That's all it is.

### 02:41:43 · Speaker 4

Clear

### 02:41:47 · Speaker 2

So we pass it only once or repeatedly for the same data point?

### 02:41:52 · Speaker 4

do it in batch, no, do it for different t's. You take all data points, so we did all analysis for one data point. You do it for all data points basically. So for one data point you'll have to sample multiple t's because you have a sum over all t's here, no? T equal to two to capital T.

### 02:42:09 · Speaker 4

take multiple t's for a given data point, try in the neural network and do it for all data points that would be one epoch, try it for multiple epochs. That's all.

### 02:42:19 · Speaker 3

Yeah

### 02:42:22 · Speaker 4

Yeah? This is how you train a D D P M. How do you

### 02:42:25 · Speaker 3

multiple, sorry, sorry, multiple t's per data point and we have to take batches of such data points.

### 02:42:34 · Speaker 4

source, no? Because you need to train it through the entire data set.

### 02:42:44 · Speaker 4

Yeah, we'll do this. We'll do this more thoroughly in the next class, no? Half of the next class will be on like training diffusion models and I'll tell you how these are related to what are called as core based models. And then I'll talk about the conditional diffusion models, no? Where all these table diffusion, imagine, dolly, etcetera, they will take a text and generate the corresponding image, right? How do you condition these models on text is something that I'll tell you. That would end the diffusion models, right? Half of the

### 02:43:14 · Speaker 4

next class perhaps. And the next the other half we will do auto regressive models. We'll start with these language models. Okay in the next class.

### 02:43:24 · Speaker 4

Okay then, that's it. See, I I I rushed through this implementation because I will give the assignment tomorrow so that you can if anyone wants to start doing it, you can start doing it, you know, get your data loaders and write the equation for this noisy one, get the network and start training at least, no? So by the time next week we will thoroughly complete it so that you can implement it completely, yeah?

### 02:43:49 · Speaker 2

So where can we find the reference to the papers?

### 02:43:49 · Speaker 4

By the way, I found

### 02:43:52 · Speaker 2

in my handwritten notes

### 02:43:52 · Speaker 4

in my handwritten notes. handwritten notes.

### 02:43:54 · Speaker 2

Okay

### 02:43:56 · Speaker 4

It's always that. I mean like my handwritten notes is pretty comprehensive, no? It will have everything.

### 02:44:04 · Speaker 4

Okay. Okay, that's it for today. Yeah.

### 02:44:05 · Speaker 1

Sir

### 02:44:07 · Speaker 1

Sir one question like not this related. Sir why can't we have quiz on the end of the class or in between? I mean it's very difficult I mean we have like I have like Friday late night meetings with US counterparts. And because of that sometimes it gets very late. The nine twenty.

### 02:44:27 · Speaker 4

Oh

### 02:44:28 · Speaker 4

stretch it

### 02:44:28 · Speaker 2

Okay

### 02:44:29 · Speaker 4

ओके, नो प्रॉब्लम, वी विल डू इट आफ्टर ई क्लास।

### 02:44:31 · Speaker 1

I mean I do I am taking the quiz post nine twenty so that's why I just I am taking the quiz first and then joining the meeting like the class. So

### 02:44:41 · Speaker 4

Oh

### 02:44:42 · Speaker 1

just in case. Okay, okay. Okay.

### 02:44:43 · Speaker 4

ओके ओके ओके टू मोर क्लासेस टू मोर क्विज़ेस वी विल डू इट आफ्टर द क्लास नो प्रॉब्लम ओके

### 02:44:48 · Speaker 1

Sure sir, Thank you so much.

### 02:44:52 · Speaker 4

ओके देन हां। सो हैव अ नाइस वीकेंड। हैप्पी दिवाली टू ऑल ऑफ यू। वी विल मीट ऑन सेकंड नो नेक्स्ट वीक, नेक्स्ट सैटरडे वी विल कंटिन्यू विथ दिस। ओके।

### 02:45:02 · Speaker 3

सर, वन मिनट फॉर ईप.

### 02:45:02 · Speaker 2

Thank you, sir. Happy Diwali. Thank you, sir, and Happy Diwali.

### 02:45:06 · Speaker 0

Hello

### 02:45:06 · Speaker 3

Sorry sir

### 02:45:08 · Speaker 4

Bye bye

### 02:45:09 · Speaker 2

Thank you sir
