---
id: D-JQVOodqmg
title: Lec 11 - Deep Generative Models Diffusion models part 1 Formulation
url: https://www.youtube.com/watch?v=D-JQVOodqmg
date: '2024-11-23'
duration: 02:45:18
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# Lec 11 - Deep Generative Models Diffusion models part 1 Formulation

## Transcript

### 00:00:02 · Speaker 1

of us have marked in the quiz but the answer is saying increased disentanglement on increasing beta

### 00:00:11 · Speaker 2

One second

### 00:00:13 · Speaker 1

Yeah I have pasted it

### 00:00:13 · Speaker 2

And I have a question

### 00:00:14 · Speaker 1

Yeah I've pasted the snippets

### 00:00:15 · Speaker 3

Seems like

### 00:00:17 · Speaker 3

there should be decreased disentanglement with reduced reconstruction quality

### 00:00:18 · Speaker 1

I've been trying

### 00:00:23 · Speaker 2

Come again so has

### 00:00:26 · Speaker 3

It says it should actually the correct option should be decreased descent angle, right? But the option that is marked correct is increased descent angle.

### 00:00:38 · Speaker 2

Yeah, it should be decreased over time. What is it saying? If beta is increased, what will happen is that the weight for the KL is increased. If the weight for the KL is increased, then

### 00:00:51 · Speaker 2

Should be

### 00:00:53 · Speaker 2

It should be both the construction quality and entanglement getting decreased okay

### 00:01:00 · Speaker 2

Okay, so first let us, I think if the correct answer is marked as this thing.

### 00:01:08 · Speaker 2

What is the correct answer given now increase the entanglement reduce the construction quality is it

### 00:01:14 · Speaker 2

No, that is not correct. Okay, so can we change this like and

### 00:01:21 · Speaker 3

Yeah I'll I'll change the

### 00:01:24 · Speaker 4

But sir is it uh like whenever we are increasing the beta it will be a stronger penalty on KL divergence which is promoting the disengagement and because it's not private

### 00:01:35 · Speaker 2

No, it is not right. No, see because that's what I told you right the word disentanglement refers to having different posteriors for all x and for each x.

### 00:01:49 · Speaker 2

That is not happening no if you if you increase beta r

### 00:01:56 · Speaker 2

Posterior collapse would be more isn't it

### 00:02:03 · Speaker 4

the potential cost uh sir when we are giving a higher value of beta uh what we are saying is that in the overall loss minimization we have to minimize kl divergence

### 00:02:15 · Speaker 1

loss more than we have to minimize reconstruction loss

### 00:02:18 · Speaker 2

Correct correct

### 00:02:19 · Speaker 1

So if we are reducing if we are increasing beta eventually what we are doing is we are ensuring that KL divergence loss comes down further which means disentanglement is going to increase

### 00:02:28 · Speaker 2

We said it

### 00:02:34 · Speaker 2

disentanglement is going to decrease no if the KL is reduced further that is what I am saying if the KL is see first understand that reduction of KL is inverse I mean is inversely proportional to in in disentanglement

### 00:02:51 · Speaker 1

Right so dissing and entanglement should increase when KL divergence is reducing right

### 00:02:57 · Speaker 2

Yeah

### 00:02:59 · Speaker 1

So then the marked answer is right increase disentanglement will reduce the confusion

### 00:03:02 · Speaker 2

I think when multiple sources online say the same thing but uh no hold on I think I'm getting confused let's see there is a double meaning

### 00:03:11 · Speaker 4

I'll bet

### 00:03:15 · Speaker 4

There is a double N and a centangle and a centangle

### 00:03:17 · Speaker 2

Let me let me let me make it clear for myself and then we'll discuss now beta is increasing beta is increasing meaning kl is reduced further if the kl is reduced further then the disentanglement

### 00:03:40 · Speaker 2

will decrease

### 00:03:43 · Speaker 2

Because disentanglement uh kale is reducing further the disentanglement has to reduce correct

### 00:03:50 · Speaker 1

The entanglement has to reduce

### 00:03:55 · Speaker 2

no no kale reduction is entang entang entang entanglement reduction see suppose kale is zero okay if if kale is zero then what happens if kale is zero the entanglement would be increased right because all of them are collapsing to z given sorry normal zero one isn't it

### 00:04:22 · Speaker 2

Is it dead

### 00:04:25 · Speaker 1

Maybe

### 00:04:25 · Speaker 4

Maybe so we will come back with the proper way of this

### 00:04:30 · Speaker 3

I think uh entanglement

### 00:04:32 · Speaker 4

Whenever we increase the beta it will increase the means at the cost of KL diversion it will reduce the quality of reconstruction and increase the t angle mid

### 00:04:46 · Speaker 1

And yeah I need to do your notes again

### 00:04:46 · Speaker 4

But yeah I need to do your notes again

### 00:04:50 · Speaker 1

If the disentanglement is reducing, it means for any input, the latent variable space is going to be almost similar, which means the reconstruction quality should be reducing.

### 00:05:05 · Speaker 2

Reconstruction quality reducing that is definite there is no question there

### 00:05:09 · Speaker 1

Right so basically we cannot have a scenario where disentanglement reduces and reconstruction quality increases

### 00:05:10 · Speaker 2

We cannot have it

### 00:05:18 · Speaker 4

I mean what what do we mean by entanglement So for example if the posterior becomes normal has the entanglement increased or decreased

### 00:05:25 · Speaker 1

So what my understanding is that entanglement being higher means that for any input image that we are giving, the latent space is coming out to be almost similar. That is why there is an entanglement in the latent space for any input image is coming out to be similar.

### 00:05:41 · Speaker 2

That is correct that is correct

### 00:05:44 · Speaker 1

So if we are saying that we are giving more weightage to the KL divergence, we are going to basically try to ensure that the entanglement reduces.

### 00:05:55 · Speaker 1

So when posterior becomes normal

### 00:05:55 · Speaker 4

When posterior becomes normal

### 00:05:57 · Speaker 1

No and the angle point increases

### 00:05:57 · Speaker 4

and angle point increases more weightage to KL means angle point becomes close to normal

### 00:06:01 · Speaker 2

All of a sudden it will become

### 00:06:05 · Speaker 1

Uh but but but

### 00:06:05 · Speaker 4

KL is a loss. KL is a loss.

### 00:06:10 · Speaker 4

If we are multiplying with the

### 00:06:10 · Speaker 1

There is a minimization operation happening. When we are giving more weightage to beta, we are going to further reduce the value of KL divergence, which means we are going to reduce the entanglement.

### 00:06:23 · Speaker 2

We all agree that

### 00:06:23 · Speaker 1

You all agree with that

### 00:06:25 · Speaker 2

If the KL has decreased then the posterior becomes normal right We all agree on that

### 00:06:34 · Speaker 3

Yeah

### 00:06:34 · Speaker 2

So does this mean entanglement has increased or decreased

### 00:06:38 · Speaker 3

It's maximum entanglement, right? When your posterior has become a normal, that's what people are trying to say.

### 00:06:45 · Speaker 2

So antangleman has increased right

### 00:06:48 · Speaker 1

Thanks for having me on the show

### 00:06:48 · Speaker 4

Do you see my screen?

### 00:06:55 · Speaker 1

Yes yes

### 00:06:57 · Speaker 4

Can you read whatever whatever I have uh highlighted

### 00:07:06 · Speaker 1

Is that any sea

### 00:07:06 · Speaker 2

Can you see what I have highlighted? But what is good in this

### 00:07:13 · Speaker 2

Disentanglement is good

### 00:07:16 · Speaker 2

This is the this is an excerpt from the beta VA paper

### 00:07:24 · Speaker 2

Okay, so higher the beta, better disentanglement.

### 00:07:30 · Speaker 4

Better means increasing surplus

### 00:07:38 · Speaker 2

higher the beta increase this entanglement

### 00:07:41 · Speaker 1

But here they put minus of beta d instead of plus beta

### 00:07:46 · Speaker 2

in the the beta VAE loss term they're subtracting instead of adding the loss

### 00:07:53 · Speaker 2

appropriate even beta greater than one call um hold on let's see have they done that uh yeah the term above that image yeah there is a minus beta correct we we did plus when we were discussing so

### 00:08:10 · Speaker 2

Uh I think that might be the

### 00:08:20 · Speaker 2

Okay, I got it. So in our formulation it was plus z.

### 00:08:25 · Speaker 1

Thanks for your

### 00:08:28 · Speaker 2

It was plus beta

### 00:08:31 · Speaker 2

Then it won't hit you

### 00:08:32 · Speaker 3

How would how would plus beta work here It it wouldn't work right you need

### 00:08:40 · Speaker 2

No, no, what I meant is, see, that then beta is taken to be negative, right? I think, so has, let's do one thing. I think, you know, there's confusion. So let us just ignore that question and just add one to everyone that's our easiest way to deal with it.

### 00:08:59 · Speaker 2

But yeah, so I think you got the point, right? At least in terms of what is happening. If beta is taken to be a positive integer and the objective is written to be minus beta, then increase in beta, right, implies

### 00:09:18 · Speaker 2

disentitlement right better discontentment i think that is what it is yeah i think i'm convinced just think about it let's move on because it's already pretty late okay so so has taken note of it we just have to add one to everyone in this in this particular quiz

### 00:09:36 · Speaker 3

Sure okay yeah

### 00:09:39 · Speaker 2

Thank you Swoos I think you can leave now if you want I can start the class

### 00:09:45 · Speaker 2

Okay thank you

### 00:09:49 · Speaker 4

Sorry for interrupting uh can you please repeat what you said about the beta thing sorry

### 00:09:57 · Speaker 2

The beta is a positive integer and the cost is KL minus beta sorry the construction minus beta okay

### 00:10:12 · Speaker 2

So if beta is increased then disentanglement will become better because we are minimizing that KL that's all and beta is a positive number

### 00:10:23 · Speaker 2

So just read this uh uh this beta vae paper no it's pretty well described I think that is correct. The only confusion was because you know the in in our formulation we we took plus beta and beta in our case was between 0 and minus 1.

### 00:10:46 · Speaker 2

Right, so in that way, this question can be interpreted as if you put plus there, increasing beta means it is, you are moving it away from minus one. So.

### 00:10:56 · Speaker 2

let's not get into that confusion I think this it's it's the problem is with writing that as plus that's all so let us like ignore that question for everyone okay so

### 00:11:10 · Speaker 2

How many quizzes are done now Four

### 00:11:15 · Speaker 2

Yes sir

### 00:11:20 · Speaker 2

order okay so we need two more

### 00:11:27 · Speaker 2

Uh we can do streak let me just look at the calendar

### 00:11:34 · Speaker 2

Second ninth and sixteenth

### 00:11:38 · Speaker 2

We have three weeks including today so today is done

### 00:11:42 · Speaker 2

Uh shall we do a quiz on 9th and 16th

### 00:11:48 · Speaker 2

You can skip on second uh because

### 00:11:51 · Speaker 4

So 16th I think we're planning for an online uh hybrid class

### 00:11:55 · Speaker 2

Correct. We'll have a quiz then. No problem. Okay. We don't want. See, otherwise we can do it on second and ninth also.

### 00:11:59 · Speaker 4

Otherwise we can do it

### 00:12:06 · Speaker 4

So let's take a

### 00:12:07 · Speaker 1

Reckon many people will not only keep on second search

### 00:12:09 · Speaker 4

Yeah

### 00:12:12 · Speaker 2

Okay, so then let us do it on 9th and 16th, okay?

### 00:12:15 · Speaker 4

Yes picture

### 00:12:19 · Speaker 2

And uh assignments we said three assignments right

### 00:12:32 · Speaker 4

I think you mentioned that you will give the third one in the November first week

### 00:12:37 · Speaker 2

Uh coding assignments are three into fifteen so two is done when is the deadline for your second assignment

### 00:12:44 · Speaker 2

Repeat it

### 00:12:44 · Speaker 4

Repeat

### 00:12:47 · Speaker 2

28th. So then Sunday I will release the third so that we can finish by mid mid November. Okay, good. So one exam is done quiz for two more quizzes and one more assignment. Okay, great. We are on track. Okay, so let us get back to classes. So you can see my screen. Can you see my screen?

### 00:13:14 · Speaker 2

Okay, so today's agenda is diffusion models, TDPM. Yeah, so I'll tell you rest of the course, the way I'm planning is we have three more classes, right? So I'd hopefully complete diffusion models today. Let's see. So today we'll do diffusion models and we'll have three more classes. And one class I will do noise contrastive estimation, self-supervised learning, all these ideas, and we'll have two more classes.

### 00:13:43 · Speaker 2

We can use it for autoregressive models and LLMs. Okay. That's how I'm planning. Okay. Let's get back to stuff. So we were looking at denoising diffusion models. Just a quick recall. These are hierarchical VAEs, right, which have multiple latent spaces, capital T number of latent spaces. All the latent spaces have the same dimension as the data space. So you start from the data and

### 00:14:13 · Speaker 2

keep projecting onto the latent space till it becomes um

### 00:14:20 · Speaker 2

the stage and still it becomes until it becomes a Gaussian distribution and from the latent space you get back to the latent space by

### 00:14:29 · Speaker 2

traversing the path in the reverse direction. So the thing is, the dimensionality of all the latent spaces is same as that of the data space is something that we saw, right? And the

### 00:15:02 · Speaker 2

It is not moving does somebody know why

### 00:15:11 · Speaker 2

Not able to move this

### 00:15:15 · Speaker 4

Both can restart

### 00:15:21 · Speaker 2

Oskar and Ester

### 00:15:24 · Speaker 2

Uh what did you say

### 00:15:28 · Speaker 2

You could just restart the application close it and restart

### 00:15:48 · Speaker 2

Still not moving

### 00:16:01 · Speaker 2

I can have a virtual money

### 00:16:10 · Speaker 2

Okay, yeah, so the dimensionality of the latent space is same as that of the data space, something that we saw, right? The encoding process in a DDPM is not learnable, it's a fixed encoding process and it's a Markov chain, okay, that is one other thing that we saw, okay? Yeah, so we made the notation consistent with the literature, the data is represented using x naught and the latent space is represented using x1 through x capital T, okay?

### 00:16:40 · Speaker 2

um yeah so you start from x naught and go to x capital t and the dimensionality of x naught is equal to xt for all t and this is how the encoding process is defined okay uh you have fixed alphas alpha 1 to alpha t and uh every xt is given by uh the previous uh x previous latent scaled previous latent plus some scaled noise where you sample from normal 0 1 and add it okay this is the so-called

### 00:17:10 · Speaker 2

called a forward process or the encoding process in a DDPM. It's a first order Markov process with Gaussian transitions, which means that you take one random variable, add Gaussian noise, you get the second random variable, and you traverse that Markov chain. Okay. And the stationary distribution of this Markov chain is normal 0, 1. And I hope that I also showed you that picture. Did I? where you start from an image and get a renoise. I showed you that picture.

### 00:17:42 · Speaker 2

Last class

### 00:17:43 · Speaker 2

Okay great. Yes. Okay so this is where we are so let us move on from here.

### 00:18:07 · Speaker 2

Okay so I'll give you the high level idea of what we will do today and then I will run through the math

### 00:18:15 · Speaker 2

The algebra is a little involved but it's not difficult

### 00:18:19 · Speaker 2

Yeah okay

### 00:18:22 · Speaker 2

So the idea is see we have uh

### 00:18:27 · Speaker 2

encoding process

### 00:18:31 · Speaker 2

is a fixed encoding process

### 00:18:34 · Speaker 2

given by the following so we have xt to be equal to root of alpha t times xt minus 1

### 00:18:45 · Speaker 2

root of 1 minus alpha t times epsilon where epsilon comes from normal 0 right this is the encoding process correct this implies that the conditional distribution of any xt given xt minus 1

### 00:19:08 · Speaker 2

What is this? Can somebody guess? We know that from reparameterization that if you start from a normal distribution, scale it and shift it with a certain mean and variance, you will still get a normal distribution, right? So these are normally distributed. So please note that my notation, normally distributed, the random variable is Xt.

### 00:19:27 · Speaker 2

The mean is

### 00:19:29 · Speaker 2

Root of

### 00:19:32 · Speaker 2

alpha t into xt minus 1

### 00:19:37 · Speaker 2

variance is 1 minus alpha t times identity so there's a very slight abuse of notation here i'll tell you what it means see when you

### 00:19:49 · Speaker 2

When you're writing a conditional distribution like this, right, the conditioned random variable xt minus one is fixed in the sense that it has already taken some value.

### 00:19:59 · Speaker 2

but the the random variable that is to be conditioned xt is not fixed we have a distribution over it that is what we have written that it's a normal distribution over xt okay where the mean is square root of alpha t times xt minus 1 so this xt minus 1 which i have marked right in lo it is a fixed value because you are already in xt minus 1 and xt minus 1 has assumed a particular value okay and given that xt minus

### 00:20:29 · Speaker 2

one already has a particular value you have an entire distribution over xt which is given by that equation does it make sense why do you have a distribution over xt is because of this epsilon that is there so fix you you are given an xt minus one you get an entire distribution over xt is that all right to all of you

### 00:20:54 · Speaker 2

Okay, now what do we do is, as I said, we have an encoding distribution that is fixed. Now please ask me questions if you have any, because I...

### 00:21:05 · Speaker 2

make it a little faster today because I want to complete DDPMs. Let's see. So we have, this is the encoding distribution. We have the decoding distribution.

### 00:21:24 · Speaker 2

which is to be learned

### 00:21:29 · Speaker 2

Okay what is the decoding distribution we write that as p theta

### 00:21:39 · Speaker 2

So decoding has to happen in the reverse direction, XT minus 1 given XT. So please note the commonalities between this and the VAE, right? In VAE, the encoding distribution is Q of G given X, which is the posterior of latent given data. The sorry, the encoding distribution is posterior of latent given data. Decoding distribution is posterior of data given latent. Okay. Similar thing is happening here. I mean, here there is no one latent, you know, there are directions of latent. So you start

### 00:22:09 · Speaker 2

from uh x naught which is the which is the data and you go to x capital t in one direction that is the encoding distribution the decoding distribution is in the reverse direction correct now this has to be learned

### 00:22:24 · Speaker 2

Okay, so this is at first of all, this is assumed to be a Gaussian distribution again, okay, at xt minus 1 with a certain mean mu theta and a certain variance sigma theta.

### 00:22:38 · Speaker 2

Okay so this mu theta and sigma theta

### 00:22:43 · Speaker 2

Are the learn are the learnable model parameters So this is what we will learn

### 00:22:53 · Speaker 2

are the learnable model parameters so given the fixed encoding distribution okay we will make a distributional assumption on the decoding distribution and we learn the parameters of it that is what we are going to do now how do we do it so we learn that through

### 00:23:13 · Speaker 2

Yeah same thing elbow optimization we'll do the exact same elbow optimization and we'll learn this

### 00:23:22 · Speaker 2

That's all. So rest is algebra. Okay. Now you understood, right? So we have an encoding fixed encoding distribution and we have a learnable decoding distribution. Given the encoding distribution, okay, we optimize the LBO and learn the decoding distribution parameters of the decoding distribution. That is what the idea is. Okay. Any questions so far quickly? Surveillant.

### 00:23:48 · Speaker 4

Previously it was written alpha t xt minus one plus one minus alpha t epsilon

### 00:23:53 · Speaker 2

Oh, sorry, my bad, my mistake. Or it's either here or there. Let me just see what the, doesn't matter, right? I mean, depends on what your alpha is, but let's see what the literature does.

### 00:24:09 · Speaker 2

I keep appointing that

### 00:24:12 · Speaker 2

Yes yes

### 00:24:16 · Speaker 2

A second now give me a second

### 00:24:31 · Speaker 2

I think the problem here I made a mistake, so this has to be.

### 00:24:40 · Speaker 2

Generally we write it as root of alpha okay

### 00:24:46 · Speaker 2

Noted correctly today but yeah

### 00:24:50 · Speaker 2

Is that okay? I should clear it. Okay. Yeah, Avatosh, let's make it quick guys, yeah.

### 00:24:57 · Speaker 4

Now why is the encoding process fixed here

### 00:25:00 · Speaker 2

Told you all that in the last class okay

### 00:25:04 · Speaker 2

because that that is see that is how the uh the ddpm is described okay the encoding process is fixed because it's a what do we want we want a projection from the data space to the uh the latent space okay or rather gaussian 0 1. now we do it in the hierarchical manner now in a ddpm it is a marco chain right so you are doing a random walk through a marco chain now unlike in a

### 00:25:34 · Speaker 2

where projection from the data distribution to the normal 0 1 okay cannot be guaranteed and has to be learned via that phi encoder network in a markov chain okay if you have gaussian transition it can be guaranteed that the stationary distribution of a fixed markov chain after sufficient number of steps converges to normal 0 1 so since you want your data to go to normal 0 1 and you construct a markov chain where there are slow transitions

### 00:26:04 · Speaker 2

You don't have to learn anything

### 00:25:57 · Speaker 4

So

### 00:26:07 · Speaker 2

the idea okay i think i mentioned this in the last class but anyway okay is this clear so what we will do then next is that under these model assumptions we will write down the elbow as usual and optimize it that's all so that's all the entire processes now okay now just like with the case as in the case of uh vae the final generation is via decoding because in vae also you do the same thing right we will do the same thing here uh the only thing

### 00:26:37 · Speaker 2

Yes we have these kinds of model assumptions and we will have to optimize the L value. Okay let us do that.

### 00:26:44 · Speaker 2

uh let us start okay elbow optimization for ddpm

### 00:27:10 · Speaker 2

Recall you should recall that uh what was our elbow so log

### 00:27:16 · Speaker 2

p theta of x okay we will start from the definition of the uh latent variable model that was integral so log of

### 00:27:28 · Speaker 2

Integral p theta

### 00:27:34 · Speaker 2

X and Z

### 00:27:36 · Speaker 2

DC correct this is what it was so finally what was our elbow uh the

### 00:27:47 · Speaker 2

Function of theta and phi

### 00:27:51 · Speaker 2

Represented that as F theta of QV. What was that?

### 00:28:00 · Speaker 2

That was an expectation of log of p theta

### 00:28:07 · Speaker 2

x and z divided by

### 00:28:11 · Speaker 2

U oxygynics

### 00:28:13 · Speaker 2

This was with respect to Q of Z geonics

### 00:28:17 · Speaker 2

Do you recall this one of you

### 00:28:24 · Speaker 2

Okay we just have to write this down for a DTPM okay that's all it is let us do that

### 00:28:33 · Speaker 2

Oh this is um

### 00:28:38 · Speaker 2

LBO for DDPM or diffusion models is only a function of theta because there's no dependence on phi is equal to expectation of

### 00:28:50 · Speaker 2

log of p theta so what is x and z here that is x naught x one

### 00:29:03 · Speaker 2

Oh why is this? This is because

### 00:29:07 · Speaker 2

X naught is the data variable and X one through XT are the latent variables

### 00:29:14 · Speaker 2

divided by q of what is the latent variable here x1 x2 up to xt conditioned on x0 okay and we have that same q here that entire thing can't write it is this is this all right this is this is only a function of theta as you can see because encoding is fixed

### 00:29:37 · Speaker 2

This is alright

### 00:29:41 · Speaker 2

Okay, so now we'll just shorten this down and write it as. So please pay a little more attention today because it's notationally heavy. It's not difficult, but if you miss one notation, it will all be gone. I'll write this as x0 to t because I can't write 1 to t all the time divided by q of.

### 00:30:04 · Speaker 2

one through t which are the random variables conditioned on x naught and this is is this okay

### 00:30:20 · Speaker 2

So every step you either react or interrupt me if you don't understand. Otherwise it will be difficult for me. So this is all right, right? This is our elbow. So we'll have to optimize this with respect to theta, correct? This is what we need to do.

### 00:30:42 · Speaker 2

So let us do that

### 00:31:06 · Speaker 2

Excuse me just a second um

### 00:31:23 · Speaker 2

Okay, great. So now this can be written as will not write this equal to every time. So let us write this expectation of log p theta x 0 to t divided by q x 1 to t given x naught. Okay, this is what we want. Okay, so now this is

### 00:31:52 · Speaker 2

Okay so first of all what we should do is we'll have to write this as

### 00:31:58 · Speaker 2

Expectation of log of

### 00:32:02 · Speaker 2

Please observe here. So now p theta of x 0 to t, I will write it as p x t times the product of

### 00:32:16 · Speaker 2

p equal to one two p

### 00:32:19 · Speaker 2

E theta

### 00:32:22 · Speaker 2

xt minus one given xt

### 00:32:28 · Speaker 2

divided by

### 00:32:32 · Speaker 2

You

### 00:32:34 · Speaker 2

Product of

### 00:32:36 · Speaker 2

t equal to one to t q xt given xt minus one okay okay why did I write this

### 00:32:46 · Speaker 2

B theta of

### 00:32:50 · Speaker 2

x naught x 1 up to x t okay it is what we wrote as p theta of x naught to t this is equal to

### 00:33:02 · Speaker 2

P theta of xt

### 00:33:08 · Speaker 2

ET off

### 00:33:24 · Speaker 2

I'm not sure

### 00:33:33 · Speaker 2

the other way round

### 00:33:44 · Speaker 2

So that is p equal to one right p theta of

### 00:33:52 · Speaker 2

X not

### 00:33:54 · Speaker 2

Given

### 00:34:05 · Speaker 2

X one given X naught

### 00:34:09 · Speaker 2

No no no we are going in the reverse direction yeah I'm just I'm just writing the checking rule hold on so this is um

### 00:34:21 · Speaker 2

should come on the other end no hold on should be so i've written it from the power i mean i've written it from t equal to 1 to t should be the other one so xt minus 1 given xt okay so this is uh xt minus 2 given xt minus 1 and so on up to p theta of xt

### 00:34:51 · Speaker 2

This is what it is. How is this this is chain rule of uh

### 00:34:56 · Speaker 2

probability right so now since the forward process is first order Markovian right reverse process is also a first order Markovian process which means that given xt okay uh xt minus 1 is independent of all the other states that is why we have written it this way okay now this can be represented as p of xt p of xt into product of p equal to 1 2 capital t

### 00:35:26 · Speaker 2

p theta of xt minus 1 given xt. Now observe what did we do? We took we took off the dependency of theta on x capital T y is thus we have designed our xt.

### 00:35:40 · Speaker 2

was XT by construction

### 00:35:45 · Speaker 2

normal 0 1 isn't it while transiting the forward chain we have ensured that the capital T at x random variable is normal 0 1 therefore it is independent of p of x t is independent of theta so this is p of x t

### 00:36:01 · Speaker 2

Is it alright

### 00:36:03 · Speaker 2

So that is the numerator in that equation. So let us write down the denominator. So now what is q of? So what do we have in the denominator? We have q of

### 00:36:16 · Speaker 2

1 2 t given x naught. This is what we have. What is this equal to?

### 00:36:26 · Speaker 2

This is equal to

### 00:36:28 · Speaker 2

You off

### 00:36:30 · Speaker 2

X1 given X naught

### 00:36:34 · Speaker 2

rho of x2 given x0

### 00:36:38 · Speaker 2

And so on the product of all this q of xt given xt minus one. Sorry this is

### 00:36:48 · Speaker 2

three minus s one x two minus x one and so on

### 00:36:59 · Speaker 2

Okay, uh, why is this this, why is this the case?

### 00:37:13 · Speaker 2

Is there independent of each other like the X one X two are

### 00:37:20 · Speaker 1

distributions

### 00:37:23 · Speaker 2

X1, X2 are not independent

### 00:37:25 · Speaker 1

Okay that's the Markov process

### 00:37:28 · Speaker 2

Exactly this is the Markov process right this is the first order Markov process this is because

### 00:37:46 · Speaker 2

See this can actually be written as you can write this as q of x1 use the chain rule of probability right so you can write this as q of x1 given x0 and you have q of x1 given sorry q of x2 given x1 and x0 into q of x3 given x1 that x2 x1 x0 and so on correct

### 00:38:17 · Speaker 2

This is by chain rule of probability, correct? So now Q of X2, first order Markov and chain rule.

### 00:38:28 · Speaker 2

Now all these terms, no, Q of x2 given x1 and x0, Q of x3 given, so up to Q of, should have written this and then written that. Okay, so Q this is Q of x capital T given everything behind that, xt minus 1 up to x0. Now and since it is

### 00:38:50 · Speaker 2

First order Marco

### 00:38:53 · Speaker 2

So it will happen you I think you got it right but this is this is what it is

### 00:39:01 · Speaker 2

Is that alright? No I will perhaps take this and put it there

### 00:39:16 · Speaker 2

Lowish yeah

### 00:39:19 · Speaker 2

Set in the above equation like p theta is it going to x t or x 0? Shouldn't it be going to x 0 here and x 1?

### 00:39:29 · Speaker 2

like we had mentioned p theta of xt minus 1 given xt times p theta of xt minus 2 given xt minus 1 so on till p theta of x0 given x1 right

### 00:39:42 · Speaker 4

So here right you do you have a pp theta of xt term also at the outside okay so what i'm what what you said is correct hold on cdb

### 00:39:53 · Speaker 2

Let us make it a little precise. So now here you have a

### 00:40:12 · Speaker 2

This is equal to you have a P of XT term here. Okay. And the last term here would be obviously.

### 00:40:21 · Speaker 2

E t dot X naught Y naught

### 00:40:27 · Speaker 2

Yeah okay thank you that's what I meant yeah okay

### 00:40:30 · Speaker 2

Okay so now please have a look at it now in the elbow right we now have the numerator

### 00:40:36 · Speaker 4

okay so now the reason i did this is how did we come from this step to this step okay now there was the joint distribution of x z x x 0 to x t okay under the model we wrote that as this product and in the denominator there was the conditional distribution of latents given data and we represented that using this product is that okay

### 00:41:01 · Speaker 4

I will continue from there take this equation so now we have the elbow

### 00:41:09 · Speaker 4

equal to this

### 00:41:37 · Speaker 4

Dog off

### 00:41:40 · Speaker 4

expectation of log of

### 00:41:44 · Speaker 4

P x t please note that I have taken the dependence on theta for the final random variable t equal to 1 to t we have p theta of x t minus 1 given x t divided by

### 00:42:01 · Speaker 4

Product off

### 00:42:07 · Speaker 4

product of t equal to one to capital T f q of xt given xt minus one

### 00:42:19 · Speaker 4

I hope that all of you know how this equation came right this is what we showed okay now it's a lot of algebra let's keep doing this see I will omit the expectation term here okay and only write the whatever is inside okay so that it is easier otherwise I'll have to write that bracket every time

### 00:42:40 · Speaker 4

We will write back the expectation term later okay right that's a omit

### 00:42:47 · Speaker 4

outer expectation

### 00:42:56 · Speaker 4

This is not any mathematical thing, this is simply to ease of writing that's all. So don't think that this is some step or something. I'll write back the expectation later. So consider log of f whatever is inside. I will write that as log of pxt times

### 00:43:17 · Speaker 4

We'll take back

### 00:43:20 · Speaker 4

B theta of the first

### 00:43:27 · Speaker 4

rather the last transition okay from the decoder I will tell you why this was taken out this will algebraically this will turn out to be easier t equal to t 2 to capital T you have p theta of xt minus 1 given xt

### 00:43:45 · Speaker 4

Uh divided by

### 00:43:49 · Speaker 4

do the same thing with the encoder also the q of x1 given x0 take that out okay and what is remaining is t equal to 2 to capital T

### 00:44:02 · Speaker 4

Q of

### 00:44:04 · Speaker 4

XT given XT minus one

### 00:44:15 · Speaker 4

Right now uh this log I mean this log is for everything

### 00:44:23 · Speaker 4

Okay

### 00:44:27 · Speaker 4

Now, this is I use the law of logarithms and pull these things outside P of XT times P theta of X naught given X1.

### 00:44:42 · Speaker 4

Invited by

### 00:44:45 · Speaker 4

X1 given X naught

### 00:44:49 · Speaker 4

Uh the second term is plus log of this one product T equal to two to capital T

### 00:45:00 · Speaker 4

B theta XT minus one given XT

### 00:45:06 · Speaker 4

divided by

### 00:45:10 · Speaker 4

You will

### 00:45:12 · Speaker 4

xt q1 xt minus 1

### 00:45:31 · Speaker 4

Okay, they should be all right, this is simply log logarithms.

### 00:45:36 · Speaker 4

Now you consider what is important as the second term okay so consider

### 00:45:46 · Speaker 4

The denominator in the second term

### 00:45:59 · Speaker 4

So, which is Q of x t minus x t minus this is the forward distribution that we know of right. So, now this can be written as Q of x t given

### 00:46:14 · Speaker 4

x t minus 1 and x naught. Can I write it this way? Now, why do I do that? This is because of algebraic convenience. So, as we will see later, no, if we write this, then the elbow, optimizing the elbow will become easier. There is one like vague interpretation that people have given in the original paper. I will also mention that, but this is mostly because of algebraic convenience. Okay. Please observe this carefully. This is one non-trivial step. Can we do

### 00:46:44 · Speaker 4

this can we write q of xt given xt minus 1 as q of xt given xt minus 1 and x naught are these the same

### 00:46:57 · Speaker 1

Markov process is independent of the

### 00:46:59 · Speaker 4

Yeah, it is because of the first order Markov property. If you condition it with anything else than the previous state, it is exactly the same.

### 00:47:11 · Speaker 4

Now what we will do is we will use Bayes' law

### 00:47:20 · Speaker 4

And the height this has

### 00:47:23 · Speaker 4

View of

### 00:47:26 · Speaker 4

It's t minus one

### 00:47:34 · Speaker 4

given xt and x0

### 00:47:41 · Speaker 4

You off

### 00:47:43 · Speaker 4

xt given x naught

### 00:47:46 · Speaker 4

divided by

### 00:47:48 · Speaker 4

u of xt minus 1 given x naught

### 00:47:54 · Speaker 4

What is this? This is simply the Bayes' law, right? I mean, you have probability of A given B and C can be written as probability of B given A and C times probability of B given C divided by probability of A given B. That is Bayes' law with three variables. Is that okay? So this is Bayes' law.

### 00:48:18 · Speaker 4

Please uh with which

### 00:48:21 · Speaker 4

three random variables you can please check that out in Wikipedia okay is that okay this is simply Bayes law so now note that the first distribution that you have right in the numerator okay what is this

### 00:48:39 · Speaker 4

We'll write that down. The skew of

### 00:48:44 · Speaker 4

60 minus 1

### 00:48:50 · Speaker 4

Given Xt and X naught

### 00:48:54 · Speaker 4

What is this distribution can somebody guess

### 00:48:58 · Speaker 4

Which is D

### 00:49:01 · Speaker 4

Distribution of

### 00:49:05 · Speaker 4

xt minus 1 given given

### 00:49:12 · Speaker 4

the encoding process

### 00:49:21 · Speaker 4

encoding process has started

### 00:49:30 · Speaker 4

Started from x naught okay

### 00:49:35 · Speaker 4

Landed at

### 00:49:39 · Speaker 4

60

### 00:49:42 · Speaker 4

t equal to t okay see please note that this is not the forward distribution

### 00:49:51 · Speaker 4

forward distribution, what is forward distribution? Forward distribution is Q of XT given XT minus 1. Okay. So this distribution is that while you are constructing the forward process, okay, what is the distribution of XT minus 1? How does the distribution of XT minus 1 looks given that you have started from X0 and landed at XT at T equal to T?

### 00:50:18 · Speaker 4

Does it make sense? Do you understand what this distribution is?

### 00:50:24 · Speaker 4

Basically, if you start from x naught, okay, depending upon what kind of noise that you add at like or what kind of samples that you get for epsilon.

### 00:50:39 · Speaker 4

XT can be very different, correct?

### 00:50:43 · Speaker 4

Do you agree

### 00:50:45 · Speaker 4

Starting from x naught, you keep adding noise. Please focus on this and like respond to me, okay, if you understand and not understand, because this is the key, you have to understand this. What I'm saying is you start from x naught, okay, and keep adding noise. Now, depending upon what sort of noise do you add, you end up at one particular xt.

### 00:51:06 · Speaker 4

Okay so every time you take the same X naught and add different kinds of noises you get two different XTs do you agree with this

### 00:51:15 · Speaker 4

The question that we are asking is given that you have started from x naught and landed at a particular xt what is the distribution over xt minus one

### 00:51:16 · Speaker 1

Question

### 00:51:29 · Speaker 4

Does it make sense? See note that this is not Q of XT minus 1 given XT because we are talking about independence between XT given XT minus 1 and the other thing right we are not talking about independence of so XT minus 1 is not independent of XT or X naught given XT correct.

### 00:51:50 · Speaker 4

Markovian process says that xt is independent of everything else given xt minus 1. It is not saying that xt minus 1 is independent of xt. I'm just saying that it is in the reverse direction and therefore this x0 cannot be removed. What did we do? Please note again, we had a q of xt given xt minus 1 term in the in one of the terms in the in the elbow wrote that q of xt given xt minus 1 in terms of I mean just conditioned that x

### 00:52:20 · Speaker 4

minus 1 x uh with x naught that is okay because it's markovian once we did that we use bayes law to invert that okay and wrote this distribution in terms of q of x t minus 1 given x t and x naught q of x t given x naught q of x t minus 1 given x naught and this distribution q of x t minus 1 given x t and x naught is simply the distribution of x t minus 1 given that the encoding process has started from x naught and landed at x t at t equal to t

### 00:52:54 · Speaker 4

Any questions yes

### 00:53:05 · Speaker 4

One question that might come up here is that why did we even write this as write this in terms of this q of this this weird distribution right is because see if you keep it q of xt given xt minus 1.

### 00:53:23 · Speaker 4

What you see is the numerator, okay, is going in one direction, okay, theta is decoding distribution is going in the reverse direction and the denominator is going in the forward direction, correct, as it is.

### 00:53:42 · Speaker 4

Okay, so if you want to optimize for the elbow, you can't simultaneously do it from both the directions.

### 00:53:52 · Speaker 4

So the idea is to represent the forward direction also somehow in terms of I mean introduce the reverse direction transition in the forward direction also and that is why we use the Bayes law to invert it. Now once you do this what happens you see you know this q of xt minus 1 given xt and x0 is actually going in the reverse direction.

### 00:54:22 · Speaker 4

So that is the algebraic convenience that we wanted and that's why we wrote it this way okay

### 00:54:29 · Speaker 4

okay so let us get back to elbow now so now uh getting back to elbow sir one question yeah if we do not

### 00:54:38 · Speaker 1

Like if we do not have x naught, then also we could have come up with this base rule, right? Like we're just based on xt minus one and xt.

### 00:54:48 · Speaker 4

Your voice completely broke off Was it only for me

### 00:54:53 · Speaker 4

I can't hear you at all

### 00:54:54 · Speaker 1

Okay let me repeat sorry am I audible

### 00:55:02 · Speaker 4

Yes yes

### 00:55:03 · Speaker 2

This is clear for us uh budget

### 00:55:07 · Speaker 1

Sir am I audible to you

### 00:55:18 · Speaker 4

I can't hear you uh any anybody else can hear me yeah we can hear him uh yes sir

### 00:55:31 · Speaker 1

Sir am I audible now

### 00:57:08 · Speaker 4

Can you hear me

### 00:57:14 · Speaker 4

The cord is disconnected just a second

### 00:57:37 · Speaker 4

Oh can you hear me

### 00:57:39 · Speaker 1

Yes sir

### 00:57:41 · Speaker 4

Okay, so you were saying something I mean I completely missed it because I think some connection issues. Can you repeat what were you saying?

### 00:57:50 · Speaker 1

Yes sir I'm audible

### 00:57:51 · Speaker 4

Do you know? Yes yes

### 00:57:54 · Speaker 1

Okay, I'm saying if we did not include the x naught term, then also we could have come up with this like a backward distribution q xt minus 1 given xt.

### 00:58:07 · Speaker 4

No you can't know because how how do you do that

### 00:58:16 · Speaker 4

then you will have marginals over so you can use the Bayes law and simply write it as q of xt minus 1 times q of xt divided by q of xt minus 1 right uh but you will have to find the marginals of q of you have to you will get terms like q of xt q of xt minus 1 and so on right these marginals are not computable

### 00:58:38 · Speaker 4

Okay, so however what we will see now we can compute to both q of x t given x naught and q of x t minus 1 given x naught. We will see that in a while, okay.

### 00:58:49 · Speaker 4

Okay great so let us get back to elbow so what we were doing was

### 00:59:01 · Speaker 4

Albors we had log of log of p x t times p theta of

### 00:59:12 · Speaker 4

x naught given x one divided by

### 00:59:22 · Speaker 4

x1 given x0 this was the first term second term was plus log of

### 00:59:30 · Speaker 4

of product T equal to 2 2 capital T numerator was P heat of XT minus 1 given X

### 00:59:43 · Speaker 4

Divided by

### 00:59:45 · Speaker 4

You off

### 00:59:47 · Speaker 4

xt it was given xt minus 1 right xt minus 1 and x0 we just conditioned it on that okay and let's use the Bayes law if we use the Bayes law then whatever we had written there

### 01:00:04 · Speaker 4

Step two

### 01:00:06 · Speaker 4

What would this entire thing

### 01:00:22 · Speaker 4

But I better to write it down again okay fine log of thought I've saved on time

### 01:00:30 · Speaker 4

does not give give x1 divided by

### 01:00:35 · Speaker 4

u of x1 given x naught plus

### 01:00:43 · Speaker 4

Log off

### 01:00:46 · Speaker 4

uh product equal to 2 to capital T we have P theta of XT minus 1 given XT

### 01:00:56 · Speaker 4

divided by okay we will use that Bayes theorem that we had written this was q of xt minus 1 given xt and x0 times q of xt given x0 divided by q of xt minus 1 given x0 okay so I will just show this to you have a look and let me know if it works

### 01:01:26 · Speaker 4

How did we do? We went from here to

### 01:01:31 · Speaker 4

And that jump was done using the intermediate steps. Is that clear?

### 01:01:40 · Speaker 4

Just have a look and let me know if it if it's clear

### 01:01:44 · Speaker 4

Okay let us continue then

### 01:02:13 · Speaker 4

Again copy this let me read this

### 01:02:23 · Speaker 4

Log off

### 01:02:37 · Speaker 4

to capital D

### 01:02:39 · Speaker 4

heat of xt minus 1 given xt

### 01:02:44 · Speaker 4

x t minus 1 given x t times the denominator of the denominator comes up q of x t minus 1 given x naught

### 01:02:54 · Speaker 4

Divided by

### 01:02:57 · Speaker 4

of xt minus 1 given xt and x naught times q of xt given x naught correct hmm now observe what happens to this product now so this product

### 01:03:19 · Speaker 4

a speed heat of xt minus 1 given xt times what is this product

### 01:03:31 · Speaker 1

of xt minus one given x1

### 01:03:33 · Speaker 4

divided by hold on so this is q of x t minus 1 given x t and x naught okay t equal to 2 to capital T so this term into we have terms like q of x 2 right so this is a x 1 given x naught into q of x 2 given x naught and so on in the

### 01:04:03 · Speaker 4

In the denominator we have Q of x2 given x naught

### 01:04:10 · Speaker 4

x3 given x naught and so on right

### 01:04:14 · Speaker 4

So these terms will cancel out. Only two of the terms will survive. Can you see that?

### 01:04:28 · Speaker 4

So what terms will survive? We will write this down now log of p xt into p theta of x naught given x1 divided by

### 01:04:40 · Speaker 4

u of x1 given x naught

### 01:04:46 · Speaker 4

plus log of only two terms would survive what are those terms we'll have q of

### 01:04:54 · Speaker 4

x1 given x0 that is the first term that would survive in the numerator in the denominator we will have q of

### 01:05:04 · Speaker 4

p given x naught okay everything else will cancel down the other term that we have is plus log of product of t equal to 2 to capital T

### 01:05:20 · Speaker 4

P theta of x t minus one given xt divided by

### 01:05:27 · Speaker 4

u xt minus 1 given xt and x naught

### 01:05:35 · Speaker 4

All right

### 01:05:37 · Speaker 4

Is it okay

### 01:05:44 · Speaker 4

Everyone with me so far?

### 01:05:49 · Speaker 4

Okay, so now look at this, no, there is q of x1 given x0 log of, you have log of ab by c, okay, so this is log of ab minus log of c and there is this, this term and this term gets cancelled away, right? That's why we took that x1 and x0 outside in the beginning.

### 01:06:13 · Speaker 4

Now this will become log of a plus log of b I can combine them and write that as log of p of xt okay times

### 01:06:41 · Speaker 4

I will just trying to skip one step that's why I was looking at it okay let me skip it anyway so log of log of p theta x naught given x1 okay plus

### 01:06:57 · Speaker 4

Log of log of PXT divided by

### 01:07:04 · Speaker 4

2 xt given x naught

### 01:07:09 · Speaker 4

Come on

### 01:07:11 · Speaker 4

equal to 2 to capital T

### 01:07:16 · Speaker 4

Log off

### 01:07:19 · Speaker 4

E theta xt minus 1 given xt divided by u of xt minus 1 given xt and x naught

### 01:07:33 · Speaker 4

All right can you see that

### 01:07:42 · Speaker 4

We are almost done with three more steps

### 01:07:46 · Speaker 4

So note that there was an outer expectation, right? So bringing

### 01:07:56 · Speaker 4

bringing in the outer expectation

### 01:08:05 · Speaker 4

Okay, so what did we have? We had the expectation of, it was Q of Z given X, right? What is Z? 1 to T given X naught. So this is our Q of Z given X, okay? And this entire thing, just this elbow, which is whatever we're out, no, log of P theta of X naught given X one.

### 01:08:27 · Speaker 4

plus plus two three terms i will not write it again okay now what is to be noted is this will be equal to expectation of okay log of p theta of x naught given x1 okay this outer expectation now will be with respect to q of x1 given x naught why is this

### 01:08:51 · Speaker 4

while the outer expectation was with respect to q of x1 to t given x0 since whatever the function that we have are only uh uh the functions of x0 and x1 the outer expectation will become function of x0 and x1 is that okay

### 01:09:15 · Speaker 4

Now uh similarly to the second term welcome to the second term

### 01:09:20 · Speaker 2

sorry I missed to understand that part expectation of Q of X 1 to T X 0

### 01:09:26 · Speaker 4

given x naught will become an expectation with respect to q of x 1 given x naught because the term that you have inside the log now it is independent of all other random variables other than x naught and x 1.

### 01:09:42 · Speaker 4

That is like uh like law of expectations okay hold on um

### 01:09:54 · Speaker 4

We have

### 01:10:00 · Speaker 4

we have this conditional expectation argument which can be done okay so hold on okay so this is the first term so the second term would be

### 01:10:10 · Speaker 4

We have the same thing expectation of

### 01:10:15 · Speaker 4

of log of what was that term P x t divided by Q of x t given x naught and this expectation is with respect to Q similar argument take x t and x t minus 1 given x naught

### 01:10:38 · Speaker 4

Everything else will be going away correct

### 01:10:42 · Speaker 1

So y ht minus one here

### 01:10:50 · Speaker 4

I think yeah I think I made a mistake here while writing

### 01:10:57 · Speaker 4

Uh see here

### 01:11:01 · Speaker 4

Oh this was my mistake sorry so here

### 01:11:05 · Speaker 4

Uh a q of x naught

### 01:11:12 · Speaker 4

hold on hold on uh x12

### 01:11:24 · Speaker 4

Yeah that should only be XT

### 01:11:32 · Speaker 4

It's only Q of x t given it's not correct

### 01:11:38 · Speaker 4

This is this is what it is

### 01:11:44 · Speaker 4

Now the third term

### 01:12:04 · Speaker 4

What dependencies do we have Let us write it that way

### 01:12:14 · Speaker 4

take the expectation inside the sum because it is linear to to t expectation of we had log of

### 01:12:25 · Speaker 1

From X1 to XT minus 1

### 01:12:27 · Speaker 4

P theta xt minus 1 given xt divided by

### 01:12:33 · Speaker 4

Q phi of no there is no Q phi sorry it is Q of

### 01:12:40 · Speaker 4

x t minus 1 given x t and x naught okay dependency is on q

### 01:12:49 · Speaker 4

XT XT minus one given XT given X naught correct

### 01:12:56 · Speaker 4

is fine now

### 01:13:05 · Speaker 4

Should be alright

### 01:13:14 · Speaker 4

One last step C represents us

### 01:13:33 · Speaker 4

x minus 1 and x not right this should be

### 01:13:58 · Speaker 4

Just thinking if I have to do it or uh

### 01:14:01 · Speaker 4

Boom

### 01:14:03 · Speaker 4

Give it as an exercise

### 01:14:07 · Speaker 4

Okay, see what we should do is after this, okay, let me write that down. This is equal to, let's write the first term. The first term is expectation of log of p tilt of x naught given x1. Expectation is with respect to q of x1 given x naught. Okay, what is the second term? The second term is simply the KL divergence, no? KL divergence between

### 01:14:34 · Speaker 4

You also

### 01:14:36 · Speaker 4

T given X naught

### 01:14:39 · Speaker 4

TXT this is by definition

### 01:14:42 · Speaker 4

And if you look at the third term, the third term is also can be written as t equal to 2 to capital T. There is an expectation with respect to Q of XT given X naught times.

### 01:15:02 · Speaker 4

a KL divergence between

### 01:15:06 · Speaker 4

Q of xt minus one given xt and x naught

### 01:15:13 · Speaker 4

and p theta of x t minus 1 given x t okay so here is where the tricky part is i'll tell you that okay the first term and second term are okay no so the second term here

### 01:15:28 · Speaker 4

This thing is simply recall divergence right by definition that should be all right correct

### 01:15:35 · Speaker 1

Minus scale like

### 01:15:36 · Speaker 4

Yes, of course, of course, negative of kL divergence. So now what happened to the third term? That's tricky, right? So what we actually did is here, we express this expectation, right? You have an expectation with respect to q of xt and xt minus 1 given x naught, correct? Okay. You can write this as product of two expectations, okay? 1 over an expectation of q of x.

### 01:16:06 · Speaker 4

T given X naught times the expectation over

### 01:16:13 · Speaker 4

You up

### 01:16:16 · Speaker 4

Okay I don't have space here

### 01:16:20 · Speaker 4

I just want to form a

### 01:16:27 · Speaker 4

create some space and write it now we have

### 01:16:38 · Speaker 4

Expectations

### 01:16:40 · Speaker 4

something right with respect to we have q of xt given sorry xt and xt minus 1 given x naught okay now this can be written as product of two expectations first expectation is q of xt given x naught okay and the second expectation is with respect to q of

### 01:17:07 · Speaker 4

x t minus 1 given x t and x naught. This is similar to Bayes rule, okay? This is called the property of conditional expectation.

### 01:17:19 · Speaker 4

You either please take it as a homework or can ask PS to do this

### 01:17:25 · Speaker 4

is a like known result okay this is a simple you can actually write this down you can write this expectation uh with you use the bayes law and use the law of conditional expectations this is called the law of conditional expectation

### 01:17:39 · Speaker 4

Here, property of conditional expectations, please have a look at it. Now, if I do this and write this expectation in terms of product of two expectations.

### 01:17:50 · Speaker 4

then what will happen? The outer expectation is still around. Whatever is the inner expectation now, which is you will have an expectation of Q XT minus 1 given XT and X naught log of P theta of XT minus 1 given XT divided by Q of XT minus 1 given XT X naught. That is the negative of KL, isn't it, between these two distributions.

### 01:18:13 · Speaker 4

Is that alright

### 01:18:17 · Speaker 4

Do you see how we got the third term

### 01:18:32 · Speaker 4

Any questions on this

### 01:18:36 · Speaker 4

Okay so that's it I mean we have to now interpret this and compute this so now what did we do so far is that

### 01:18:44 · Speaker 4

elbow for TDPM

### 01:18:48 · Speaker 4

So we just

### 01:18:50 · Speaker 4

only a function of theta

### 01:18:57 · Speaker 4

We wrote that as

### 01:19:00 · Speaker 4

Expectation of log of p theta x naught given x1 with respect to q of x1 given x naught

### 01:19:12 · Speaker 4

Minus

### 01:19:14 · Speaker 4

BKL

### 01:19:17 · Speaker 4

Q of XT given X naught and XT

### 01:19:25 · Speaker 4

Minus

### 01:19:28 · Speaker 4

This is a tiny town

### 01:19:41 · Speaker 4

Oh I paste this

### 01:19:48 · Speaker 2

Think if you long press on the screen and

### 01:19:56 · Speaker 4

Uh-huh what what should I do

### 01:20:02 · Speaker 4

Select P

### 01:20:09 · Speaker 4

You seem seem to be an expert in this

### 01:20:13 · Speaker 4

How do I move it now? No I can't move it

### 01:20:21 · Speaker 4

Painful yes yes

### 01:20:27 · Speaker 4

This is what we saw. So now it's this is all it is, and we are done.

### 01:20:34 · Speaker 4

at the interesting structure no if you look at the structure what is the first term

### 01:20:39 · Speaker 4

The first term is very similar to the reconstruction term

### 01:20:45 · Speaker 4

BAE right

### 01:20:50 · Speaker 4

x0 is your data x1 is your uh first latent variable you are records reconstructing the data values in the first latent variable that is the first term okay and what is the second term the second term is

### 01:21:05 · Speaker 4

Same as the prior matching term that we had in BA

### 01:21:12 · Speaker 4

Very similar to prior matching because x t so look at this now this is like your q of z given x right

### 01:21:19 · Speaker 4

P of Z that's exactly how it is

### 01:21:23 · Speaker 4

two terms are very similar to the vae but the other thing other thing to that is to be noted is see this second term is completely independent of theta there is no dependence on theta at all so you can completely ignore that while while training okay what's interesting is the third term this third term right

### 01:21:48 · Speaker 4

I don't want to change it this is called the consistency term

### 01:21:55 · Speaker 4

Or they call it the denoising

### 01:21:59 · Speaker 4

denoising matching term

### 01:22:07 · Speaker 4

So look at what is happening okay so what is happening is that

### 01:22:13 · Speaker 4

at every step t okay p theta of xt minus xt minus 1 given xt is telling you how should the model move to xt minus 1 given xt that is what you need to learn so this is the one that you should learn okay so what is this term saying this term is saying starting from x0 okay and given the fact that you have reached xt tell me what is the distribution of xt minus 1 this is saying given xt

### 01:22:43 · Speaker 4

tell me what should be the distribution of x t minus 1. So now if you minimize the KL divergence between these two terms, intuitively what it will lead to is that if you traverse through p theta of x t minus 1 given x t, you would eventually get to distribution of x naught, isn't it?

### 01:23:02 · Speaker 4

Because what you are saying is this distribution Q is telling you that this is known, okay? This is known. This is telling you that given that I have started from X naught and reached XT, what is the distribution on XT minus one? This is telling me that given XT, how should I go to XT minus one? So now if I match these two terms, it is actually matching denoising, right?

### 01:23:28 · Speaker 4

This I can call it does it match the denoising

### 01:23:32 · Speaker 4

And this is

### 01:23:35 · Speaker 4

Learnable denoising

### 01:23:40 · Speaker 4

where we are whatever we know how to we are we know how to denoise and we are matching that denoising with uh with the learnable denoising so that we can generate data and of course from a hold on i i know this from a mathematical standpoint this works because finally what we are doing is minimizing the kl divergence between the model distribution and the data distribution via elbow optimization that is what we are doing okay now what we will do next is we will take this consistency or denoising

### 01:24:10 · Speaker 4

machine term and we will see how to compute it in practice that is what we will do next but I hope that you understood what these three terms are in GDPM's elbow okay any questions here

### 01:24:25 · Speaker 1

So it will help

### 01:24:25 · Speaker 4

Yeah yeah

### 01:24:27 · Speaker 1

So here how are we evaluating the known denoising term

### 01:24:33 · Speaker 1

That's the next thing

### 01:24:34 · Speaker 4

That's the next thing that we that's the next thing that we will do I don't know

### 01:24:39 · Speaker 4

derived now we will see how to compute it known denoising term has to be evaluated now we will do it

### 01:24:47 · Speaker 4

That is what I'll do next

### 01:24:54 · Speaker 4

Yeah let me go on quickly

### 01:25:07 · Speaker 4

Can you make it quick please

### 01:25:11 · Speaker 4

Uh I mean how are the the third sum

### 01:25:23 · Speaker 4

That is because similar argument no dependency is only on xt minus xt xt minus 1 and x0 here the expectation was q of x 1 through t q and x0 okay see dependence of whatever is inside is only on xt xt minus 1 and x0 isn't it that's all.

### 01:25:42 · Speaker 1

But the log term that

### 01:25:48 · Speaker 4

But the random variable see that see expectation outer expectation is with respect to x 1 2 3 2 1 2 t given x naught correct

### 01:26:02 · Speaker 4

Right now what are terms we can drop in X1 to T is the question

### 01:26:11 · Speaker 4

You can only drop everything other than xt and xt minus 1 that's all

### 01:26:16 · Speaker 2

Okay so that given XT is also included when we compute expectation

### 01:26:21 · Speaker 4

Isn't it? See, the distribution does not change. What changes is the dependency of whatever random variables are not there. You can just omit them from the distribution, joint distribution. It's actually writing this joint distribution, right, in terms of, so, okay. So, what actually is happening is, you see that we wrote it this way, no? Where was that?

### 01:26:47 · Speaker 4

So, we wrote this was the expect this was the distribution with respect to which we need the expectation, isn't it? Okay, hold on it is still coming up. Correct. This is the distribution with respect to which we need the expectation and we wrote it as a product of so many things, right? Now, when you write it as a product of so many things, whatever distributions that are independent, you can just remove them and they are constants. That's all will happen. Okay. What will remove what will remain are the ones where the dependencies

### 01:27:17 · Speaker 4

So there will be q of xt given x0 and q of xt minus 1 given x0 I have written that as q of xt comma xt minus 1 given x0 that's all

### 01:27:26 · Speaker 4

Makes sense now Yeah

### 01:27:31 · Speaker 4

Okay anything else

### 01:27:34 · Speaker 4

So now what we will do next is that we will see how to compute this denoising like known denoising term and learnable denoising term and we will build a model that is what we will we are going to do. Why is my screen stuck? Yeah, that is what we are going to do next and that is how you try in our DDPM and we will see how to sample from it.

### 01:27:54 · Speaker 4

Okay uh shall we take a break then this is a good time to take a break

### 01:28:03 · Speaker 4

Okay, shall we make it a shorter break? Because people might have a hard stop at 12, 15, 12, 20. We'll make it a short break. So this is 11, 7 in my clock. Let us get back at 11, 15, huh? 11, 20 or 11, 15. What do you want?

### 01:28:22 · Speaker 4

1120 let's get back at 1120 okay

### 01:28:28 · Speaker 4

So please be exactly at 1120 we'll continue from here okay see

### 01:44:18 · Speaker 4

Hello all shall we continue shall we resume

### 01:44:36 · Speaker 4

Let us uh look at the

### 01:44:42 · Speaker 4

What have to do is

### 01:45:04 · Speaker 4

Compute the consistency term now. So it is simply the KL divergence.

### 01:45:11 · Speaker 4

Between

### 01:45:12 · Speaker 4

You off

### 01:45:15 · Speaker 4

X three minus one given next year and next month

### 01:45:23 · Speaker 4

Each it off

### 01:45:25 · Speaker 4

T minus one given

### 01:45:33 · Speaker 4

is what the term is okay first we need to consider

### 01:45:53 · Speaker 4

Somebody was asking know how to compute this so let us see how to compute this

### 01:46:03 · Speaker 4

Let's consider this

### 01:46:13 · Speaker 4

how to do this so this let's use base log

### 01:46:20 · Speaker 4

Q of XT

### 01:46:24 · Speaker 4

Given xt minus 1 and x0

### 01:46:33 · Speaker 4

u of xt minus 1 given x naught

### 01:46:38 · Speaker 4

divided by Q of

### 01:46:41 · Speaker 4

X t given x naught this is base log

### 01:46:46 · Speaker 4

What is this equal to this is equal to you are

### 01:47:15 · Speaker 4

Is this alright

### 01:47:20 · Speaker 1

Because of macro processors

### 01:47:24 · Speaker 4

Yeah it because of the Marco process

### 01:47:27 · Speaker 4

xt given xt minus 1 and x0 is simply xt correct give me q of xt given xt minus 1

### 01:47:42 · Speaker 4

Should be alright yeah okay now

### 01:47:46 · Speaker 4

So we know how to compute this, no this we have this we know what distribution it is and we have to consider

### 01:47:56 · Speaker 4

the distribution of

### 01:48:04 · Speaker 4

You up

### 01:48:08 · Speaker 4

XT given X naught is what we should do

### 01:48:17 · Speaker 4

We need this okay how do we get this is the question

### 01:48:23 · Speaker 4

Actually we can get this

### 01:48:28 · Speaker 4

we obtained

### 01:48:34 · Speaker 4

using recursion

### 01:48:40 · Speaker 4

you how you have

### 01:48:43 · Speaker 4

Okay so what does this distribution by beta win? This is

### 01:48:51 · Speaker 4

Distribution of

### 01:48:55 · Speaker 4

yet

### 01:48:58 · Speaker 4

latent variable

### 01:49:04 · Speaker 4

Given data

### 01:49:08 · Speaker 4

Yeah how do we get this is the question so we have

### 01:49:15 · Speaker 4

xt be equal to root of alpha t times xt minus 1 into sorry plus root of 1 minus alpha t times some epsilon where epsilon comes from normal 0 1 okay let me call this as some epsilon t minus 1 okay i mean this is simply a sample from normal 0 1 there is nothing sacrosanct about t minus 1 but let me write it that

### 01:49:45 · Speaker 4

way just to differentiate it algebra so this now i can recurse over this now this is square root of alpha t okay into what is xt minus 1 root of alpha t minus 1

### 01:50:01 · Speaker 4

XT minus 2

### 01:50:05 · Speaker 4

root of one minus alpha t minus one

### 01:50:12 · Speaker 4

We call this as an epsilon t minus 2

### 01:50:19 · Speaker 4

root of one minus alpha t times epsilon t minus

### 01:50:27 · Speaker 4

This is all right

### 01:50:34 · Speaker 4

Okay now this

### 01:50:39 · Speaker 4

You can keep recursing the still you get x x naught but we'll have to see uh how to how how one step of recursion happens and then we can generalize it okay. So this is equal to a lot of space to write this this is equal to

### 01:50:55 · Speaker 4

a square root of alpha t

### 01:51:00 · Speaker 4

Endo

### 01:51:03 · Speaker 4

alpha t minus one

### 01:51:07 · Speaker 4

xt minus 2 xt minus 2

### 01:51:24 · Speaker 4

That is the first term the second term is

### 01:51:29 · Speaker 4

root of alpha t minus

### 01:51:34 · Speaker 4

alpha t times alpha t minus 1 into epsilon t minus 2 plus root of 1 minus alpha t times epsilon t minus 0 correct

### 01:51:52 · Speaker 4

Okay now um

### 01:51:57 · Speaker 4

It should be done as

### 01:52:02 · Speaker 4

Okay, so consider these two terms.

### 01:52:10 · Speaker 4

these two terms okay which is root of

### 01:52:16 · Speaker 4

alpha t minus alpha t into alpha t minus 1 into epsilon t minus 2. So this, this we know.

### 01:52:30 · Speaker 4

is sampled from a Gaussian

### 01:52:34 · Speaker 4

That has zero mean

### 01:52:37 · Speaker 4

And

### 01:52:42 · Speaker 4

variance to be equal to alpha t minus alpha t into alpha t minus 1

### 01:52:53 · Speaker 4

I use I

### 01:52:55 · Speaker 4

Do you agree

### 01:52:58 · Speaker 4

Why is this the case This is because

### 01:53:02 · Speaker 4

again reparameterization right so you have a Gaussian uh you have a scaled Gaussian so epsilon t minus 2 is I have to write this one epsilon t minus 2

### 01:53:17 · Speaker 4

is again normal 0 1 okay if it's normal 0 1 then something scaled with that will become another Gaussian with a different mean and variance agreed okay so this is one random variable and we have another random variable here which is

### 01:53:37 · Speaker 4

a root of

### 01:53:39 · Speaker 4

One minus alpha t times epsilon t minus one. This is again Gaussian.

### 01:53:47 · Speaker 4

Zero mean

### 01:53:50 · Speaker 4

Variances 1 minus alpha t times

### 01:54:00 · Speaker 4

Is this okay

### 01:54:04 · Speaker 4

Okay now what we have under that

### 01:54:11 · Speaker 4

Different colours

### 01:54:21 · Speaker 4

Even uh it is not a good colour

### 01:54:41 · Speaker 4

of this gown

### 01:54:44 · Speaker 4

Where did that colour go

### 01:54:57 · Speaker 4

B

### 01:55:02 · Speaker 4

corresponds to

### 01:55:17 · Speaker 4

And therefore

### 01:55:21 · Speaker 4

is another random another Gaussian random variable because sum of two Gaussians are Gaussians you know that right Gaussian random variable with the following properties so now T is the Gaussian okay

### 01:55:41 · Speaker 4

zero mean okay and the variance to be equal to one minus alpha t alpha t minus one

### 01:55:50 · Speaker 4

I so you can please verify this

### 01:55:57 · Speaker 4

take some of two Gaussian random variables with these particular mean and variance and add them and see what happens to the variance

### 01:56:06 · Speaker 4

Okay so this implies that I can write

### 01:56:11 · Speaker 4

60 the as

### 01:56:17 · Speaker 4

Root off

### 01:56:19 · Speaker 4

alpha t into alpha t minus one

### 01:56:24 · Speaker 4

So x minus 2

### 01:56:27 · Speaker 4

another random variable which is one minus alpha t alpha t minus one

### 01:56:37 · Speaker 4

Some epsilon

### 01:56:41 · Speaker 4

T minus 2 where epsilon T minus 2

### 01:56:46 · Speaker 4

I already use epsilon t minus two let's call this as epsilon star t minus two which is Gaussian 0 1 okay

### 01:56:56 · Speaker 4

You can simply see what I just did and take a take a minute and let me know if it works

### 01:57:02 · Speaker 4

So what did we do? Xt was given by the forward equation, okay. Just recursed over that. When you recurse over it, you will get a sum of two Gaussian random variables with different means and variances, sorry, different variances means are both zero. And we combine those two and reparameterize it into another Gaussian random variable and we got that final equation.

### 01:57:26 · Speaker 4

Is it all right questions on this

### 01:57:35 · Speaker 4

be fine now it's easy yeah so now I can do this again go recursively I can keep doing this this implies that my xt assume it now

### 01:57:50 · Speaker 4

implies that my x t e x t can be written as root of

### 01:57:58 · Speaker 4

alpha t alpha t minus one up to

### 01:58:09 · Speaker 4

Uh alpha

### 01:58:12 · Speaker 4

one right alpha one yeah alpha one times x naught

### 01:58:21 · Speaker 4

root of one minus product of

### 01:58:27 · Speaker 4

No I can't

### 01:58:32 · Speaker 4

the product later so one minus uh alpha t same thing alpha t alpha t minus one of two up to alpha one uh times epsilon

### 01:58:48 · Speaker 4

ch is equal to root of sum

### 01:59:00 · Speaker 4

i equal to one to t alpha i

### 01:59:04 · Speaker 4

Fix not

### 01:59:08 · Speaker 4

root of one minus

### 01:59:13 · Speaker 4

equal to one to t

### 01:59:17 · Speaker 4

alpha i times some epsilon this is equal to

### 01:59:22 · Speaker 4

root of alpha t bar times x naught plus root of 1 minus alpha t bar

### 01:59:35 · Speaker 4

Times have saluted

### 01:59:39 · Speaker 4

Gosh

### 01:59:42 · Speaker 4

Root of alpha, or rather alpha t bar, is the product of all that.

### 01:59:49 · Speaker 4

for t bar is the product of all the alphas up to up to t

### 01:59:59 · Speaker 4

So now this is an equation. So now what does this actually mean? Okay, let me write it.

### 02:00:08 · Speaker 4

distribution and also then interpret that alpha is 0 normal 0 1. So this implies that we have Q of X T given X naught. What is this?

### 02:00:21 · Speaker 4

is this this is equal to this is a normal distribution again because this you know reparameterization the distribution at xt a mean is root of alpha t bar times x naught

### 02:00:36 · Speaker 4

And the variance is one minus alpha t bar

### 02:00:55 · Speaker 4

note what where did we come from uh we wanted to compute the consistency term and uh we we had this uh known denoising term and we used Bayes' law to do that so for that we wanted q of x t given x naught and x t given x naught is computed recursively see this actually means that

### 02:01:21 · Speaker 4

yet

### 02:01:23 · Speaker 4

Latent

### 02:01:25 · Speaker 4

sample the latent sample

### 02:01:30 · Speaker 4

The th latent sample is also th noisy sample no

### 02:01:41 · Speaker 4

in the forward the encoding or the forward process

### 02:01:55 · Speaker 4

process can be obtained

### 02:02:03 · Speaker 4

In one step

### 02:02:21 · Speaker 4

Retort

### 02:02:27 · Speaker 4

Adding the noise

### 02:02:33 · Speaker 4

Eight times

### 02:02:35 · Speaker 4

So this is actually because of recursion, that's all right. Use the above recursion and found out that the tth latent variable in the forward diffusion process can be obtained in one step starting from x0 without having to hop the Markov chain for t steps. All right, is this okay?

### 02:03:04 · Speaker 4

This is another consequence of uh of uh having this first order Markov chain with recursion right You can we can do it that way

### 02:03:16 · Speaker 4

Kara gunda

### 02:03:18 · Speaker 1

So judges are did

### 02:03:19 · Speaker 2

We just prove that a Gaussian of Gaussian is also a Gaussian

### 02:03:23 · Speaker 4

What do you mean by caution of caution

### 02:03:26 · Speaker 2

Uh because I mean we are taking so if you s if you look at the steps right

### 02:03:31 · Speaker 2

So X two is obtained by taking a sample from a Gaussian and then X three is

### 02:03:35 · Speaker 4

Where is X2 no no X2 is not from epsilon is from Gaussian no X2 is not from Gaussian

### 02:03:42 · Speaker 2

But if you see the the forward Markov chain I mean that's what we do right we take a Gaussian of the result and then again sample from another Gaussian

### 02:03:52 · Speaker 4

I'm not getting what you're saying. See X XT is obtained by this equation no where is another question here

### 02:04:01 · Speaker 2

But then it it depends on uh ultimately depends on X naught right

### 02:04:06 · Speaker 4

Of course it does so

### 02:04:08 · Speaker 2

One thing I can say

### 02:04:08 · Speaker 4

One question

### 02:04:09 · Speaker 1

In between we are applying multiple Gaussians

### 02:04:14 · Speaker 4

not applying any Gaussians no you take x naught and sample from a Gaussian distribution and add it to x naught that's what we are doing

### 02:04:23 · Speaker 1

Yeah and and we keep doing that

### 02:04:26 · Speaker 4

There is no application of Gaussian. We are sampling from Gaussian, adding the Gaussian, yeah, that we are doing.

### 02:04:33 · Speaker 1

I mean, does it mean that ultimately, say the last result that we get is again a Gaussian, right, with the different parameters?

### 02:04:42 · Speaker 4

Team will be the last result

### 02:04:42 · Speaker 2

And also

### 02:04:44 · Speaker 1

So yeah this

### 02:04:46 · Speaker 4

Distribution of

### 02:04:46 · Speaker 2

Distribution of

### 02:04:46 · Speaker 1

It's

### 02:04:47 · Speaker 4

B correct that is a Gaussian so

### 02:04:51 · Speaker 2

And the intermediate steps were also Gaussian. Correct. So with the different parameters. So my question is, did we just say that if we keep taking Gaussian and then sample and then again take, again keep sampling from a different Gaussians, the end result is the again sampling from a single Gaussian?

### 02:05:10 · Speaker 4

Ah that is reparameterization no

### 02:05:14 · Speaker 2

So that was my yes I mean that was my point

### 02:05:17 · Speaker 4

Hi to okay so it you it is not a question I was expecting

### 02:05:21 · Speaker 2

No it was not it was not a question

### 02:05:23 · Speaker 4

You are making an observation yes yes yes correct yeah so now you can reparameterize any you know any amount of Gaussian addition in terms of Gaussians that's all it means yeah

### 02:05:44 · Speaker 4

Okay, anything else? Okay, so now what did we do is we now know, let's get back to this. Our goal was to get the

### 02:05:58 · Speaker 4

consistency term estimated no so now we had a

### 02:06:27 · Speaker 4

This is the distribution that we had in the KL, right? So this is equal to

### 02:06:58 · Speaker 4

by Bayes law okay and then we use the

### 02:07:03 · Speaker 4

One Cohen property here is Q of xt given xt minus one

### 02:07:09 · Speaker 4

times u of xt minus one given x not.

### 02:07:16 · Speaker 4

divided by

### 02:07:21 · Speaker 4

xt you know x naught okay this is what it was okay now uh

### 02:07:28 · Speaker 4

So we know the first term we do what is that that is the definition of the forward process. So it's Gaussian at xt and we have root of alpha t times xt as the mean

### 02:07:44 · Speaker 4

The variance was 1 minus alpha t

### 02:07:50 · Speaker 4

minus alpha t times i so the variance correct that was the first term what about the second term we just found that out right here we found out what q of xt given x naught was that was another Gaussian with a certain mean and variance let us write that down

### 02:08:07 · Speaker 4

So this is Q of XT minus 1 given X naught. No, that is another Gaussian. Gaussian is at XT minus 1. That's the random variable. T mean is root of alpha T minus 1 bar times X naught.

### 02:08:27 · Speaker 4

And the variance is one minus alpha t minus one bar.

### 02:08:34 · Speaker 4

I

### 02:08:40 · Speaker 4

from here okay

### 02:08:42 · Speaker 4

comes from whatever we just derived through uh recursion and in the denominator we have another Gaussian

### 02:08:50 · Speaker 1

Sir sorry to interrupt the first term it should be a root of alpha t into xt minus 1

### 02:09:12 · Speaker 4

of alpha t into x t minus correct times for the correction so this is x t root of alpha t bar times x naught that's the mean and the variance is 1 minus alpha t bar times i

### 02:09:35 · Speaker 4

Is what uh what is the LHS LHS is Q of

### 02:09:41 · Speaker 4

xt minus 1 given xt and x0 is what we called as the known denoising term right that's what it is okay now look at this see this is if all the terms have things like this now you have e power minus some quadratic term now you have xt minus some mean time bar or rather it's all identity so it will be like this it will be

### 02:10:13 · Speaker 4

xt minus

### 02:10:16 · Speaker 4

Some mean

### 02:10:18 · Speaker 4

Square okay

### 02:10:22 · Speaker 4

times e polar minus

### 02:10:27 · Speaker 4

x t minus 1 minus some other mean squared divided by same thing e power minus

### 02:10:46 · Speaker 4

so on right now um see observe that the distribution that we have in the left side is a distribution on x t minus 1 okay what should we do now can somebody suggest what should we do now

### 02:11:01 · Speaker 4

And we know all these means, right? We know all these means and variances. Uh, what should we do now?

### 02:11:12 · Speaker 4

So what to be done is e power

### 02:11:19 · Speaker 4

I am this

### 02:11:21 · Speaker 4

60 minus 1

### 02:11:27 · Speaker 4

minus one

### 02:11:29 · Speaker 4

minus sum mean

### 02:11:45 · Speaker 4

Express it this way. Okay. Now, how do we do that? This we do by what is called as completing the square.

### 02:11:54 · Speaker 4

Does all of you know how to complete this square or what do you mean by completing this square

### 02:11:59 · Speaker 4

This means that suppose you have a term a quadratic term like this no x squared plus bx plus c okay you can always add some let's say some

### 02:12:11 · Speaker 4

d times x minus d times x you can add and subtract things and write this in terms of say x minus some p squared plus some constant you know this no this is called completing the square right so whatever expressions do we have inside the exponentiations we need to complete the square in terms of xt minus 1 okay we'll get some mean and some variance

### 02:12:36 · Speaker 4

Is that all right? Can all of you see that?

### 02:12:44 · Speaker 4

Let me show you the calculations. I will skip the calculations, you can simply go through that. I will just show you that.

### 02:12:53 · Speaker 4

Do it later

### 02:12:54 · Speaker 1

Sir what about the XT term

### 02:12:57 · Speaker 4

xt term will become a constant right because the lhs is conditioned on xt so xt is xt is given a particular xt it is a constant as far as xt minus 1 is concerned

### 02:13:14 · Speaker 4

Can you see my screen

### 02:13:24 · Speaker 4

Hello can you scheme see my screen Do you see my screen

### 02:13:28 · Speaker 1

Yes sir yes sir

### 02:13:29 · Speaker 4

this is what i'm talking about see uh we have these three gaussians right there is one gaussian uh for q xt given xt minus an x naught there is one gaussian for the second distribution and one for the third you have to write down all these gaussian distributions and use the appropriate means and variances and you should you should simply complete the square this is the uh the calculation that i'm skipping see it's only algebra okay it's like high school level algebra please follow this and i have given

### 02:13:59 · Speaker 4

paper to you okay so please say this algebra finally what will happen is this will become a Gaussian distribution okay with a certain mean and a certain variance because you have completed the square and you can look at this now that all you have to do is rearrange the terms add and subtract the terms such that it will become it will assume a Gaussian distribution form and you should read out the mean and variance that's all we should do

### 02:14:24 · Speaker 4

Is that okay? So please follow that. I will skip this and only write the final mean and variance because it's simply an algebra. Did you understand all of you?

### 02:14:35 · Speaker 4

It's not complicated huh You have you just have to run through the algebra

### 02:14:41 · Speaker 4

Alright is it okay

### 02:14:45 · Speaker 4

You can go through it and if you don't get it you can always come back to me and I will tell you it's not at all difficult you'll easily understand that

### 02:14:53 · Speaker 4

Your screen

### 02:15:06 · Speaker 4

Now this term will become so Q of

### 02:15:28 · Speaker 4

xt minus one given

### 02:15:31 · Speaker 4

X t and x naught now became a Gaussian distribution right

### 02:15:40 · Speaker 4

is a Gaussian distribution okay distribution is at xt minus 1 the mean is let's call that as mu q okay and that will be that will be a function of xt and x0 because these are conditioned on xt and x0 and there will be some variance call it as sigma q this will only be a function of t or alpha t it will be independent of I'll write down what these are the mean of this distribution mu q

### 02:16:11 · Speaker 4

The function of xt and x0 is given by

### 02:16:16 · Speaker 4

root of alpha t

### 02:16:20 · Speaker 4

One minus

### 02:16:25 · Speaker 4

minus one

### 02:16:29 · Speaker 4

Lexus

### 02:16:42 · Speaker 4

into x naught

### 02:16:45 · Speaker 4

divided by 1 minus alpha t bar

### 02:17:26 · Speaker 4

Now note that the both of these terms right both of these terms are known

### 02:17:33 · Speaker 4

And computable no

### 02:17:37 · Speaker 4

So now this means that this known denoising term can be computed. So we know alphas, we know xt, we know x0, we know all of this. So that can be computed. So this is typically written as some sigma q squared times

### 02:17:53 · Speaker 4

Identity awareness

### 02:17:56 · Speaker 4

this entire thing is written as sigma q squared to the constant okay that is what is done

### 02:18:05 · Speaker 4

questions so far I think this is fine no now what did we do so we wanted that the third term in the elbow was scale between

### 02:18:17 · Speaker 4

xt minus 1 given xt and x naught and we had p theta of

### 02:18:26 · Speaker 4

XT minus one given XT okay

### 02:18:29 · Speaker 4

is what we had okay now in a DDPM

### 02:18:40 · Speaker 4

The decoding distribution

### 02:18:44 · Speaker 4

It's called decoding distribution or

### 02:18:47 · Speaker 4

Denoising distribution

### 02:18:51 · Speaker 4

It's also called the reverse process

### 02:18:59 · Speaker 4

This process is assumed to be a Gaussian

### 02:19:17 · Speaker 4

is in place

### 02:19:21 · Speaker 4

Each heat off

### 02:19:25 · Speaker 4

xt minus one given xt

### 02:19:29 · Speaker 4

This is a Gaussian

### 02:19:32 · Speaker 4

minus 1 with a mean mu theta this mu theta and the variance the variance of this is assumed to be equal to a equal to constant constant which is assumed to be equal to what the true thing is so only the mean is estimated variance is assumed to be constant in the in the normal course okay in the literature variance is assumed to be a constant okay

### 02:20:10 · Speaker 4

Okay, now what happened is that because it's Gaussian, so we have

### 02:20:17 · Speaker 4

Greater divergence

### 02:20:20 · Speaker 4

The main Q

### 02:20:23 · Speaker 4

t minus 1 given

### 02:20:26 · Speaker 4

X t and X not

### 02:20:30 · Speaker 4

Eat it off

### 02:20:33 · Speaker 4

XT minus one given XT

### 02:20:42 · Speaker 4

is now

### 02:20:44 · Speaker 4

A clear divergence between

### 02:20:49 · Speaker 4

Gaussian

### 02:20:55 · Speaker 4

parameterized at mu q and sigma q

### 02:21:00 · Speaker 4

And this is a Gaussian that is parameterized

### 02:21:09 · Speaker 4

mu theta and sigma cube

### 02:21:15 · Speaker 4

Is this all right

### 02:21:19 · Speaker 4

Now KL between two Gaussian distributions

### 02:21:24 · Speaker 4

Known to be, I mean, it can be analytically computed, is given by half log.

### 02:21:44 · Speaker 4

determinant of sigma Q

### 02:21:49 · Speaker 4

minus d where d is the data dimensionality

### 02:21:53 · Speaker 4

The years of

### 02:21:55 · Speaker 4

I'm not sure

### 02:21:58 · Speaker 4

It was

### 02:22:00 · Speaker 4

It mark you

### 02:22:05 · Speaker 4

mu theta minus mu q transpose

### 02:22:10 · Speaker 4

quadratic form sigma q inverse mu theta minus mu q

### 02:22:18 · Speaker 4

just take this as a homework and do it show that the gaussian distribution between two uh sorry kl divergence between two gaussian distributions can be computed this way this is equal to

### 02:22:33 · Speaker 4

half this is log one which is zero so like okay let me write it log one minus d trace of uh uh inverse of uh sigma q inverse times sigma is also equal to d that can be shown because it's just constant times identity no d dimension it will just add up to be d trace is the sum of the diagonal elements if it's a diagonal matrix plus so this log one will go away these two d will go

### 02:23:03 · Speaker 4

away sigma q inverses a so you have mu theta minus mu q transpose

### 02:23:14 · Speaker 4

Now this is small sigma q squared i this is what we have written that as this is mu theta minus mu q

### 02:23:24 · Speaker 4

it's all so this will be equal to half

### 02:23:30 · Speaker 4

an inverse here okay so it will be uh 2 sigma q squared times

### 02:23:40 · Speaker 4

Normal

### 02:23:42 · Speaker 4

You take down when this includes question

### 02:23:48 · Speaker 4

is actually the elegance and beauty of DDPM

### 02:23:52 · Speaker 4

After doing all that the final denoising matching term will simply be a mean squared error between two means

### 02:24:05 · Speaker 4

That's all actually we are done. There is the other the rest of the things that we do is only some reparameterizations and we'll see how to implement this using a neural network. Any questions here? Yeah, Sanchit.

### 02:24:22 · Speaker 1

why are we assuming that the decoding distribution is Gaussian and like in a general case

### 02:24:29 · Speaker 4

I can't imagine that's

### 02:24:31 · Speaker 4

I'll take that is because see we are not assuming the distribution of data to be Gaussian. We are only assuming the conditional of the latent given another latent to be Gaussian. Okay. That is one thing. Why are we doing that assumption is that what can be shown is if you have a forward Markov chain, okay, with Gaussian transitions, there exists a real reverse Markov chain that also has Gaussian transitions is something that can be shown.

### 02:25:00 · Speaker 4

Okay, but what changes is the parameters.

### 02:25:05 · Speaker 4

changes as the parameters so one is mu theta the other is some other parameter no so but what can be shown is that if the if you have a markov chain whose forward distribution is uh gaussian transitions are gaussian okay then the backward distribution uh is also gaussian with a different parameters

### 02:25:30 · Speaker 1

So like in VAE also we try to assume like what I'm trying to understand

### 02:25:36 · Speaker 4

And reporting distribution

### 02:25:39 · Speaker 1

Sorry that please continue

### 02:25:42 · Speaker 1

So like for VAE also, like we were trying to, you know, mod, like assume that the latent space will be a Gaussian distribution, like a normal distribution. And, you know, so like, why are we so much biased towards a Gaussian distribution in almost all of the models?

### 02:26:03 · Speaker 4

No, no, see that is a design choice you can see while in a naive VAE we assumed it to be Gaussian but in all VQVAE and the other Vampire etc. it can be modeled as something else, right? Similarly, see but here what you should see is that the stationary distribution here which is the distribution of the tth latent is assuming is assumed to be Gaussian. We are not assuming the intermediate distribution to be Gaussian but only the conditionals are assumed to be Gaussian.

### 02:26:33 · Speaker 4

Which is okay

### 02:26:35 · Speaker 4

and i mean yeah why are we assuming it to be gaussian is because like it's an isotopic distribution right i mean uh it has it is a distribution that has infinite support so it is easy to work with there are diffusion models where they have used another uh i mean other exponential family of distributions but they lead to a similar thing because see note that nowhere we are assuming that p of x naught is gaussian this is not gaussian at all right so p

### 02:27:05 · Speaker 4

theta of x0 which is our data distribution is actually given by the product of all those distributions right we know that um we can use the chain rule and do it so the conditionals are assumed to be Gaussian which is okay you can have conditional to be Gaussian and you can use the Gaussian conditionals to model any distribution of interest

### 02:27:29 · Speaker 4

So that way I mean if your question is that isn't Gaussian as Gaussianity assumption restrictive here it is not restrictive at all it can model any distribution only the conditionals are assumed to be Gaussian. Now why are we doing that choice in in in in the reverse process of DDPM is because what can be shown is that if you if you construct a Markov chain with Gaussian transitions in the forward direction the reverse transition also happens to be Gaussian okay with different set of parameters is a known result.

### 02:28:01 · Speaker 4

That's all right

### 02:28:07 · Speaker 4

It is not, no, we are finding out mu theta here. It is parameterized by mu theta, we will find that out, no.

### 02:28:14 · Speaker 4

See now finally what we are finding out is this mu theta mu theta is something that we find out

### 02:28:21 · Speaker 3

But that cannot be arrived

### 02:28:24 · Speaker 4

no no no that is our model right that is that is the whole point if you start look at the forward model that we

### 02:28:31 · Speaker 2

One problem that we start

### 02:28:34 · Speaker 4

fixed is known of course it is fixed you see this you see this p theta mu theta and sigma theta are learnable but in practice what they do is they they make sigma theta a fixed thing only mu theta is learned

### 02:28:52 · Speaker 4

So that is our model see if you make the reverse process also fixed then what is what are you learning

### 02:28:59 · Speaker 2

Yeah understood

### 02:29:01 · Speaker 2

Yeah I understood sir

### 02:29:04 · Speaker 4

Is this okay so finally it all boils down to I think I'm doing a multi scale thing here right one thing is at some scale the other is another scale you just look at this

### 02:29:17 · Speaker 4

The day

### 02:29:20 · Speaker 4

zoom it inadvertently somewhere and it'll become that should not be an issue for you know when you go back and look into it I think you can you can also zoom out and zoom in and look into that in different scales I suppose right

### 02:29:38 · Speaker 1

Is this a big guy

### 02:29:38 · Speaker 2

Printouts

### 02:29:44 · Speaker 4

Because of the scale issue because of the scale issue

### 02:29:44 · Speaker 2

Because of the scale issue because of the scale issue

### 02:29:48 · Speaker 4

I see okay

### 02:29:49 · Speaker 2

So how do you

### 02:29:52 · Speaker 2

We don't print that much, but if sometimes we like to take a printout, then

### 02:29:57 · Speaker 4

Uh

### 02:29:58 · Speaker 2

Taking a com petitive stance

### 02:30:00 · Speaker 4

The positive side of it is you know I'm helping the environment so it's fine

### 02:30:08 · Speaker 4

Okay, so is this all right? So what happened is that finally this elbow thing.

### 02:30:18 · Speaker 4

Why don't you

### 02:30:27 · Speaker 4

There is this term this

### 02:30:50 · Speaker 4

solve right you'll have to minimize this so of course there is that another term no this was minus k l there was this term of expectation of log of e theta of

### 02:31:04 · Speaker 4

x uh one given x naught this was also one term so that's all right so these are the uh two last terms that are that is there in the elbow so we'll have to now implement these two things using neural networks okay and then when uh like uh

### 02:31:25 · Speaker 4

Estimate these two terms, minimize them and then learn how to sample from it. See, those two things have to be done. I need at least half an hour to do that. Shall we stop here? Because it will be nice if I do it in one stretch. I'll do it in the next class.

### 02:31:43 · Speaker 4

Well the only problem is I wanted to do that today because I was planning to give your assignments out on like like Sunday at least tomorrow

### 02:31:57 · Speaker 4

Okay, maybe I'll quickly tell you how to do that so that you can like start looking at your data, building these things. Okay, shall I take 10 more minutes?

### 02:32:11 · Speaker 4

Okay so that at least you know how to train this

### 02:33:05 · Speaker 4

Now let's do this reparameterization. We can actually implement it this way, but people generally implement it in a different reparameterization. Let us do that. We have reparameterizing.

### 02:33:19 · Speaker 1

So there will be the KL divergence term also right

### 02:33:24 · Speaker 4

No that is the third one is what we showed as this uh difference between the mix second one

### 02:33:27 · Speaker 1

No no no essential

### 02:33:30 · Speaker 4

That is independent of theta no we can ignore that

### 02:33:37 · Speaker 1

So sir, what will be its use for like which term, which component will it be used for updating in the TDPN?

### 02:33:49 · Speaker 4

What I didn't get the question which term what will be used for

### 02:33:52 · Speaker 1

Sir the KL divergence term that was independent of theta are we saying that we won't be using it anywhere for updating the

### 02:34:02 · Speaker 4

Yeah because model training of course no it is independent we don't there is no model at all there is no dependence on model it is a constant as far as the model is concerned

### 02:34:12 · Speaker 4

This comes because of the fixed forward process, right? And also, yeah, this primarily comes from fixed forward process, okay? So I will maybe quickly tell you what this is and handwave and do the math the next time, okay? So that you can start implementing. See, what's the idea is you have this term, no? You have mu theta minus mu q as your loss, okay? Now what is done is we have this mu q as, what is mu q? Some constant c1 times,

### 02:34:42 · Speaker 4

x t I had written that some other constant times x naught divided by some constant right or rather I can write it as a some linear combination of x x1 and x naught this is how mu q was correct now we have

### 02:34:58 · Speaker 4

xt to be equal to we use that recursion and showed that xt was equal to root of alpha t times x naught okay uh x naught

### 02:35:12 · Speaker 4

Please pay attention here because this is what I'll ask you to implement okay is X naught

### 02:35:22 · Speaker 4

root of 1 minus alpha t bar times epsilon this is how it was correct now if I rearrange these terms I can write x naught in terms of xt minus root of 1 minus alpha t bar times epsilon divided by 2 root of alpha t bar okay this implies that my mu q now can be written okay in terms of

### 02:35:52 · Speaker 4

I can get rid of x naught, right? I can write this as some other constant k1 times xt, okay, minus or plus some other constant times epsilon. Do you agree?

### 02:36:08 · Speaker 4

All of you agree on this

### 02:36:18 · Speaker 4

Am I there audible? Yeah. Okay. So this is all it is. So this implies that I have my mu theta, right? Mu theta, which is a function of xt. I can also write this as, okay, some constant k1 times xt plus, okay, k2 times some epsilon theta, okay, which is a function of xt and t. So what am I saying is the following. Now, see mu theta.

### 02:36:48 · Speaker 4

or mu theta was the mean of a Gaussian random variable correct

### 02:36:55 · Speaker 4

Right. I can always reparameterize that in terms of some other constant xt, isn't it?

### 02:37:04 · Speaker 4

Do you see what that means this is reparameterization

### 02:37:13 · Speaker 4

You get the idea

### 02:37:17 · Speaker 4

Media is

### 02:37:19 · Speaker 4

that mu theta was the mean of a Gaussian random variable, okay. I can always reparameterize that in terms of some other constant xt, isn't it?

### 02:37:30 · Speaker 4

I just have to arrange these k1 and k2 terms so I'm just simply reading and meterizing them

### 02:37:37 · Speaker 4

Okay okay

### 02:37:43 · Speaker 4

that would get designated into this epsilon theta

### 02:37:50 · Speaker 4

Basically what I've done is I've written this mu theta in terms of some epsilon theta

### 02:37:56 · Speaker 4

Constant times XT is that okay

### 02:38:04 · Speaker 4

So now this implies that my loss that I had no mu theta minus mu q now becomes proportional to

### 02:38:17 · Speaker 4

epsilon minus

### 02:38:19 · Speaker 4

data

### 02:38:29 · Speaker 4

Didn't get it

### 02:38:31 · Speaker 4

because those constants will get cancelled away, no? We have like reparameterized mu theta also in terms of the same constant as that of mu q. So those constants xt gets cancelled away. So it will only be in terms of epsilon and epsilon theta cap.

### 02:38:48 · Speaker 4

Is this clear to all of you

### 02:39:07 · Speaker 4

So now how do you implement this in practice is that you have a

### 02:39:13 · Speaker 4

please note that the dimensionality of and I will do it like more thoroughly in the next classes just to ensure that you will get started with your assignment okay you will have a neural network okay theta neural network this will have this kind of architecture is called the unit architecture where the dimensions will keep on decreasing hit a bottleneck and the dimensions will again keep increasing okay this is because the size of noise here epsilon is same as that of the input okay

### 02:39:43 · Speaker 4

So now what does it take as input? It'll take input x t and t okay and this will predict

### 02:39:51 · Speaker 4

epsilon eta that is all that is all the training of GDDPM is the last function is epsilon minus

### 02:40:00 · Speaker 4

epsilon theta cap x t comma t okay now what is x t x t is as we know root of alpha t bar x naught

### 02:40:11 · Speaker 4

1 minus alpha t bar times epsilon. That's all. How the result you try? How do you do it?

### 02:40:18 · Speaker 4

taken x naught okay and

### 02:40:25 · Speaker 4

Compute

### 02:40:28 · Speaker 4

So take x naught sample epsilon from normal 0 1

### 02:40:33 · Speaker 4

Compute XT using this equation

### 02:40:44 · Speaker 4

Okay so give that give that XT as an input to the neural network

### 02:40:54 · Speaker 4

And whatever the output is, match that output with the epsilon noise that you have added. That's all the DDP I'm training is. Then you back propagate. And you do it for multiple Ds.

### 02:41:09 · Speaker 4

You are minimizing the is this clear? See, I mean, OK, I will not take any questions now because it's 1220. We will start from this the next class. OK, I will tell you like precisely what the architecture is and how do you do this, what the loss function is and all that. But this is all it is. Right. So basically what's happening is given a data point, you add some noise to it. OK, and you get the Tth latent variable, pass that through a neural network and try to predict what was the amount of noise that was added to get.

### 02:41:39 · Speaker 4

It is XT from XMARC that's all it is

### 02:41:47 · Speaker 2

So we pass it only once or repeatedly for the same data point

### 02:41:52 · Speaker 4

it in batch no do it for different t's you take all data points so we did all analysis for one data point you do it for all data points basically so for one data point you will have to sample multiple t's because you have a sum over all t's here no t equal to 2 to capital T

### 02:42:09 · Speaker 4

Take multiple T's for a given data point, try the neural network and do it for all data points that would be one epoch, try it for multiple epochs, that's all.

### 02:42:22 · Speaker 4

Yeah there's a few trying at ADPM

### 02:42:25 · Speaker 1

So sorry, multiple T's per data point and we have to take batches of such data points.

### 02:42:35 · Speaker 4

Course no because you need to train it through the entire data set

### 02:42:44 · Speaker 4

Yeah we'll do this we'll do this more thoroughly in the next class. Now half of the next class will be on like training diffusion models and I'll tell you how these are related to what are called as core based models and then I'll talk about the conditional diffusion models you know where all these stable diffusion imagine dolly etc they will take a text and generate the corresponding image right how do you condition these models on text is something that I'll tell you that would end the diffusion models right uh half of the

### 02:43:14 · Speaker 4

class perhaps and the next the the other half we will do autoregressive models we'll start with these language models okay in the next class okay then that's it see i i i rushed through this implementation because i will give the assignment uh tomorrow so that you can if anyone wants to start doing it you can start doing it you know get your data loaders and write the equation for this noisy one get the network and start training at least so by the time next week we will thoroughly complete

### 02:43:44 · Speaker 4

it so that you can implement it completely yeah

### 02:43:49 · Speaker 1

So by the way I have to look for the papers

### 02:43:49 · Speaker 2

My name is

### 02:43:53 · Speaker 4

in my handwritten notes okay handwritten notes

### 02:43:57 · Speaker 4

It's always that I mean like my handwritten notes is pretty comprehensive it will have everything

### 02:44:04 · Speaker 4

Okay okay well that's it for today yeah

### 02:44:07 · Speaker 1

one question like not uh what this related so why can't we

### 02:44:26 · Speaker 1

9 20

### 02:44:29 · Speaker 4

Sure okay no problem we'll do it after we do

### 02:44:32 · Speaker 1

I am taking the quiz post 9 20 so that's why I just I am taking the quiz first and then joining the meeting like the class

### 02:44:41 · Speaker 4

Ah

### 02:44:43 · Speaker 2

Okay okay

### 02:44:43 · Speaker 4

Okay, okay, okay. Two more classes, two more quizzes, we'll do it after the class, no problem. Okay.

### 02:44:44 · Speaker 2

Okay cool

### 02:44:49 · Speaker 1

Sure sir thank you so much

### 02:44:52 · Speaker 4

Okay then huh So have a nice weekend Happy Diwali to all of you We will meet on second no next week next Saturday we'll continue with this okay

### 02:45:02 · Speaker 1

Certainly

### 02:45:02 · Speaker 2

Thank you sir and happy new year

### 02:45:08 · Speaker 4

Bye-bye yeah
