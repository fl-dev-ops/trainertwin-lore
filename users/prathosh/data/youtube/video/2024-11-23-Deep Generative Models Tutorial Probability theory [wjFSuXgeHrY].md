---
id: wjFSuXgeHrY
title: Deep Generative Models Tutorial Probability theory
url: https://www.youtube.com/watch?v=wjFSuXgeHrY
date: '2024-11-23'
duration: 00:50:45
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# Deep Generative Models Tutorial Probability theory

## Transcript

### 00:00:02 · Speaker 1

You know

### 00:00:05 · Speaker 1

Only the weight of network two will be updated

### 00:00:09 · Speaker 1

Okay, that is how you can make sense of it. I have given you one Stanford course. Okay, now there go to the course notes. And then there you can see some of the topics where in which he explains backpropagation. So where he takes a sigmoid node explicitly.

### 00:00:30 · Speaker 1

He takes a specific sigmoid node and then he explains how to do the back propagation

### 00:00:37 · Speaker 1

Yeah to that specific signal node

### 00:00:37 · Speaker 2

To that specific signal

### 00:00:39 · Speaker 1

It's in the course notes of the link that I have given

### 00:00:43 · Speaker 2

Okay we'll check that

### 00:00:44 · Speaker 1

Now this is, yeah, this is one of the very good resources on CNNs. Okay. Now they have really given a very good resource on CNNs. Now to understand CNN, this is one of the best resource that I have come across. I am not saying that there might be some other good resources, but this is one of the notes that I have come across. And apart from that, one other resource that I have come across is a three blue, one brown channel.

### 00:01:14 · Speaker 1

three blue and brown

### 00:01:16 · Speaker 2

Yeah at least I know that

### 00:01:18 · Speaker 1

Yeah, three blue one brown channel now there you can look at the convolution and so he has a specific chapters on neural networks now there you can look at it now in which the queries will be resolved

### 00:01:33 · Speaker 2

Yeah sure sure Chandan I think maybe we can yeah continue with the

### 00:01:37 · Speaker 1

So any other questions you have any others

### 00:01:48 · Speaker 1

So things are going on comfortably no issues are there

### 00:01:58 · Speaker 1

So now with this, let's try to continue with today's discussion. Now today's discussion is basically around some of the topics that Sir would have left in between for TS to fill in the some of the proofs and some of the algebra. Now in that manner, we will take some of the ideas from wherever he has left. I have listed some of the important points.

### 00:02:28 · Speaker 1

I'm not I'm not going till the first session. I'm trying to finish off the things that he has recently done. Now so that your VAE and other stuffs so after VAE he will go to the diffusion models. Now once he goes to diffusion models, so you should be comfortable with those topics. So I what I thought is rather than going ahead with a lot of previous things that was there, there were some ideas on probability which whenever time permits we will come back.

### 00:02:58 · Speaker 1

we will be looking into some of the stuff that sir has left in BAE okay so now the some of the basic proofs that I thought we will be covering today is one is KL divergence is always positive and then the idea of law of the unconscious statistician now depending on that we will see whether we'll be we'll be able to go ahead with other ideas

### 00:03:29 · Speaker 1

Okay I'll just stop on that

### 00:03:37 · Speaker 1

So now first we will take this weird thing that was law of the unconscious distribution. This is one of the very important ideas that you find in probability.

### 00:03:58 · Speaker 1

Law of the

### 00:04:15 · Speaker 1

of the unconscious statistician also called as lotus not any party symbol but just the abbreviation

### 00:04:30 · Speaker 1

So now it is useful to calculate

### 00:04:39 · Speaker 1

Easy to calculate expectation of

### 00:04:44 · Speaker 1

a function of a random variable

### 00:04:48 · Speaker 1

Okay

### 00:04:52 · Speaker 1

Now g of x

### 00:04:56 · Speaker 1

It's a

### 00:04:59 · Speaker 1

is a function of a random variable x

### 00:05:09 · Speaker 1

And then the assumption is

### 00:05:16 · Speaker 1

Distribution of X is known.

### 00:05:23 · Speaker 1

and g of x's are known

### 00:05:28 · Speaker 1

If g of x is known then you can directly get the density and then do the stuff but it is not meant

### 00:05:38 · Speaker 1

Let's say Px

### 00:05:41 · Speaker 1

Now let this be

### 00:05:44 · Speaker 1

PMF or

### 00:05:48 · Speaker 1

pdf of x depending on whether x is a discrete random variable or a continuous random variable now what i'll be doing is i'll be going ahead with the continuous case proof for the continuous case is much simpler

### 00:06:09 · Speaker 1

So I'll be going ahead with the

### 00:06:13 · Speaker 1

roof for them

### 00:06:19 · Speaker 1

Continuous case

### 00:06:23 · Speaker 1

Okay. Now let's say y is g of x.

### 00:06:30 · Speaker 1

Okay and then we assume some ideas on G. So we say that G is

### 00:06:40 · Speaker 1

Differentiable

### 00:06:46 · Speaker 1

And it's

### 00:06:51 · Speaker 1

Inverse inverse which and then

### 00:06:53 · Speaker 3

Shandun

### 00:06:55 · Speaker 1

Yes sir. Yes sir.

### 00:06:58 · Speaker 3

Uh sorry I interrupted you uh Professor

### 00:07:01 · Speaker 1

Yes sir yes sir I got it

### 00:07:02 · Speaker 3

Yeah I I I mean if you can maybe just solve the midterm exam questions no that would I think be useful

### 00:07:13 · Speaker 1

I I I myself did not prepare for it

### 00:07:20 · Speaker 2

So can we have a separate tutorial for it this week maybe for that

### 00:07:24 · Speaker 3

Yeah yeah no problem maybe next week yeah maybe next week

### 00:07:26 · Speaker 1

Yeah sure sure sure sir

### 00:07:28 · Speaker 2

Or even I think maybe that that that I mean going through the mid-term is also something which we wanted to go through so

### 00:07:28 · Speaker 1

Yeah

### 00:07:35 · Speaker 1

Sure uh we we will surely do it uh uh in the next session yeah

### 00:07:41 · Speaker 3

And then one other thing here I'm sorry I did that

### 00:07:43 · Speaker 1

Yes sir yeah no no no no no problems yes sir

### 00:07:45 · Speaker 3

This is Saturday I will take the class between 8 pm and 11 am

### 00:07:48 · Speaker 1

Yes I'm 11 yeah yeah yeah I saw the message

### 00:07:53 · Speaker 3

Yeah so you have the quiz at 11 o'clock okay Sure after 11.

### 00:07:55 · Speaker 1

Sure after sure sure yeah your son's interview is there

### 00:08:01 · Speaker 3

Oh yeah I mean sh-

### 00:08:02 · Speaker 1

So all the all the best with the interview

### 00:08:07 · Speaker 1

See the guy cannot talk they want to interview him I don't know

### 00:08:07 · Speaker 4

See the guy cannot talk they have want to interview him why don't

### 00:08:13 · Speaker 4

I mean these Bangalore schools right I don't know what they're

### 00:08:18 · Speaker 3

Anyway

### 00:08:19 · Speaker 1

Will you interview your son or you like you also I mean I don't know

### 00:08:22 · Speaker 4

Otherwise why would I go no I mean my wife could have gone so they have asked to specifically ask both the parents to be present with the child so

### 00:08:33 · Speaker 3

Yeah

### 00:08:33 · Speaker 4

Yeah go ahead and do that and then you have the

### 00:08:36 · Speaker 3

It's called

### 00:08:38 · Speaker 4

of these schools in the south bank but yeah so

### 00:08:41 · Speaker 1

So it has uh the sixth the sixth crosser DBJ road

### 00:08:46 · Speaker 4

Or Tatas will be at me

### 00:08:48 · Speaker 1

That is the link for him yeah yeah

### 00:08:50 · Speaker 4

Yeah so have that quiz on 11 o'clock okay 11 o'clock

### 00:08:52 · Speaker 1

I'm loving it yeah

### 00:08:53 · Speaker 4

And one other thing, somebody asked me to not have the quiz on 2nd of November, right? Because that's like a series of holidays and yeah, sort of Diwali, right? So what we can do, no, 19th we will have a quiz, 26th we will have another quiz, okay?

### 00:09:12 · Speaker 1

Just a

### 00:09:13 · Speaker 4

Then maybe I discuss that in today I mean the Saturday's lecture I just wanted to let you know that that one of these tutorials no you can see

### 00:09:23 · Speaker 3

Maybe or you can do another thing why don't you just solve the midterm

### 00:09:26 · Speaker 4

questions and just upload it in the group you don't have to spend time

### 00:09:30 · Speaker 1

That I'll do yeah

### 00:09:33 · Speaker 3

I think that would be easier

### 00:09:33 · Speaker 1

be easier sure sure sure that and we can we can ask doubts if any i mean

### 00:09:39 · Speaker 3

Oh yeah you can ask them to do it for you too

### 00:09:42 · Speaker 1

It'll be easier later

### 00:09:44 · Speaker 3

Sorry gentlemen I disturbed you please continue

### 00:09:46 · Speaker 1

No no no no yeah no problems no problem yeah

### 00:09:52 · Speaker 1

Sorry to interrupt you

### 00:09:52 · Speaker 4

Sorry Chandra before going into mathematics detail can you just suggest what is the intuition why we are doing this law of unconscious guidance

### 00:10:01 · Speaker 1

I'll I'll I'll come to that and I'll exactly come to that okay see uh for example I'll give you a very simple idea to calculate it comes up in

### 00:10:09 · Speaker 4

It comes up in reparameterization it came up in reparameterization

### 00:10:16 · Speaker 1

reparameterization so even a simple idea is to calculate the variance you want expectation of x square

### 00:10:25 · Speaker 1

x square is a function of x. We know how to calculate the expectation of x. How to calculate the expectation of x square? We need the idea of lotus. That's the simplest example that we can think of.

### 00:10:38 · Speaker 1

In addition to reparametrization that's what Sir said but the simplest idea that we can think of is

### 00:10:42 · Speaker 4

Ooh

### 00:10:44 · Speaker 4

Good example I like it yeah

### 00:10:47 · Speaker 1

Thank you

### 00:10:50 · Speaker 1

So my my internet got disconnected just just give me one minute

### 00:10:56 · Speaker 1

I'm not a good

### 00:11:11 · Speaker 1

are in between what will be the syllabus for the next quiz will it be the last two classes

### 00:11:18 · Speaker 1

whatever has been covered till the pre previous quiz and then see you we cannot compartmentalize things like that for example if i ask you a simple question on probability now you cannot say that this is the quiz one's topics and this is not limited right

### 00:11:36 · Speaker 4

But Chandra don't ask things that I'm going to know no no no

### 00:11:38 · Speaker 1

No no no no no no no no no no

### 00:11:41 · Speaker 4

You can be Markovian you should be ergodic

### 00:11:45 · Speaker 1

No no no no no no that I'll not do sir

### 00:12:02 · Speaker 1

So now the idea is, see, the first of all, let's try to understand the name itself. So now it is called as law of the unconscious statistician. Okay. Now you will be able to understand why it is called such in some time. Okay. So it is not like simply they just use that name. Okay. It has a very deeper meaning to it. So the idea is you apply it in a totally in an unconscious way.

### 00:12:34 · Speaker 1

What is this what happened screen

### 00:12:52 · Speaker 1

Are you able to see my iPad screen

### 00:12:56 · Speaker 1

So now we know how to we know how to calculate the expectation of x. Now, but now what we have is expectation. So we have a function of a random variable now for which we want to know how to calculate the expectation.

### 00:13:12 · Speaker 1

So, now let us try to understand how to put. Okay. So, now the conditions that we are imposing on g is now the function g that we have should be differentiable and the inverse should be monotonic. Okay. So, under these assumptions, once we have these assumptions, now the current code will work. I will tell you how each of the conditions make sense. Okay. So, now

### 00:13:46 · Speaker 1

If y is z of x

### 00:13:50 · Speaker 1

exists

### 00:13:54 · Speaker 1

The inverse of

### 00:14:02 · Speaker 1

So now what is

### 00:14:07 · Speaker 1

by dy of g inverse of y

### 00:14:15 · Speaker 1

What do you say about this Can you compute this

### 00:14:23 · Speaker 1

Inductively can you think of the formula for this

### 00:14:35 · Speaker 1

So now this is

### 00:14:40 · Speaker 1

So just go ahead and refresh your uh our calculus uh stuff this is

### 00:14:49 · Speaker 1

the inverse of y

### 00:14:51 · Speaker 1

Now this is now this is

### 00:14:54 · Speaker 1

This is by the

### 00:14:59 · Speaker 1

inverse function rule

### 00:15:04 · Speaker 1

No

### 00:15:06 · Speaker 1

is nothing but this is D

### 00:15:10 · Speaker 1

The coins

### 00:15:12 · Speaker 1

One over

### 00:15:16 · Speaker 1

the inverse of y

### 00:15:22 · Speaker 1

Now all these things are fine. Now where is this coming into picture? Okay, let's write what is expectation of g of x.

### 00:15:32 · Speaker 1

How do you write it Now this is continuous uh thing is what my assumption is this is integral of

### 00:15:38 · Speaker 1

y into fy of y

### 00:15:43 · Speaker 1

This is how I write it right

### 00:15:47 · Speaker 4

sorry it's g dash of g inverse of y right one y i mean we should take the differential of g

### 00:15:56 · Speaker 4

I am wrong sorry

### 00:15:58 · Speaker 1

No no no just just go ahead and on this is correct

### 00:16:05 · Speaker 1

Now what is the

### 00:16:09 · Speaker 1

distribution function of y. Now this is probability that

### 00:16:14 · Speaker 1

Y is less than or equal to y

### 00:16:18 · Speaker 1

So this is nothing but probability that

### 00:16:21 · Speaker 1

y is less than or equal to g of x

### 00:16:31 · Speaker 1

This will be

### 00:16:34 · Speaker 1

This will be probability that

### 00:16:42 · Speaker 1

less than or equal to C inverse of

### 00:16:48 · Speaker 1

Agree with me so far

### 00:16:53 · Speaker 1

So this is effects of

### 00:16:58 · Speaker 1

Effects off

### 00:17:01 · Speaker 1

g inverse of y

### 00:17:06 · Speaker 1

Now, I know the distribution function of y in terms of x. I know, see what is my assumption? Now, let's go back to my assumption. Now, I know I am saying that distribution function of x is known. Now, because of this trick that I have used, I know the distribution function of y also now.

### 00:17:29 · Speaker 1

Once I know the distribution once I know the distribution yeah I've got it

### 00:17:33 · Speaker 4

I have a question. So when you invert the g right to the other side x would be greater than g inverse of y right

### 00:17:43 · Speaker 1

A is less than B

### 00:17:51 · Speaker 1

1 over A is greater than 1 over B

### 00:17:59 · Speaker 1

1 over B is less than 1 over A

### 00:18:05 · Speaker 1

answers your question

### 00:18:10 · Speaker 4

Uh I think I'll have to I'll I'll take a look

### 00:18:13 · Speaker 1

Hey no no no no no no there is nothing there yes okay

### 00:18:15 · Speaker 4

Yes a chain of supplies one

### 00:18:18 · Speaker 1

See what is this is A okay, let us come back here. No, this is A this is B cut

### 00:18:28 · Speaker 1

Apply this idea you will get this exactly the same steps

### 00:18:34 · Speaker 1

Now in inversion in terms of scalar is 1 by A right

### 00:18:38 · Speaker 1

Exactly the same thing. See the inversion that is happening. No, B is coming here.

### 00:18:44 · Speaker 1

And A is coming here. You can see that.

### 00:18:50 · Speaker 1

Now it's clear exactly the same idea

### 00:18:56 · Speaker 1

Now, okay, whatever questions you have, you can stop me anytime. Okay. See, what is, what will be happening is, so from most of the times, these will be like more of a mathematical work rather than what do you call any intuition or any stuff working. Okay. Now, this is basically most of the times, our discussions will be more on a mathematical proof kind of ideas. Okay. So sometimes it is known that we will lose path.

### 00:19:26 · Speaker 1

that time we should take simple ideas like this to understand intuitively what is the steps that we are doing okay so now now now finally now i know the distribution function now if i know the distribution function can i get the density function

### 00:19:46 · Speaker 4

Yes differentiate

### 00:19:48 · Speaker 1

Differentiated that's all effects of

### 00:19:53 · Speaker 1

Green versus whitey

### 00:19:56 · Speaker 1

One by

### 00:19:59 · Speaker 1

See you off

### 00:20:12 · Speaker 1

Okay so now let's go back to expectation of

### 00:20:16 · Speaker 1

The office

### 00:20:20 · Speaker 1

What is expectation of g of x? This is integral of y into fy of y dy correct?

### 00:20:29 · Speaker 1

Now this is nothing but

### 00:20:32 · Speaker 1

What is y is g of x

### 00:20:36 · Speaker 1

Why use the office

### 00:20:39 · Speaker 1

What is f y of y that is f x of

### 00:20:44 · Speaker 1

g inverse of y

### 00:20:50 · Speaker 1

into

### 00:20:52 · Speaker 1

One by

### 00:20:55 · Speaker 1

g into g inverse of y

### 00:20:59 · Speaker 1

What is G inverse of Y

### 00:21:06 · Speaker 1

The inverse of y is x

### 00:21:12 · Speaker 1

Is it DX

### 00:21:17 · Speaker 1

This will be

### 00:21:19 · Speaker 1

Integral law

### 00:21:21 · Speaker 1

of x

### 00:21:24 · Speaker 1

fx of x

### 00:21:27 · Speaker 1

This is expectation of

### 00:21:32 · Speaker 1

This is the proof

### 00:21:36 · Speaker 1

See what is this fellow saying? See if you have a function don't worry apply this g of x on everything and then use the density of x only which is mathematically crazy to us right?

### 00:21:54 · Speaker 1

No, but as it turns out with these proof, it is very much clear to us, yeah, this is working.

### 00:22:04 · Speaker 1

Does it make sense?

### 00:22:09 · Speaker 1

Now that is why it is called as unconscious decision. You don't even have to be conscious. So just apply the function and take the density of x only or density or mass of x only. It will work immediately. You don't need to worry about at all.

### 00:22:26 · Speaker 1

That is why this fellow is called as law of the unconscious statistician

### 00:22:34 · Speaker 1

Make sense? Why it is called as law of the unconscious statistician?

### 00:22:52 · Speaker 1

I have done it in steps now to get this

### 00:22:56 · Speaker 1

I did this this

### 00:23:05 · Speaker 1

That's all very simple

### 00:23:08 · Speaker 1

Any questions with this proof I'm done it only for the continuous case.

### 00:23:13 · Speaker 1

to on a very restricted continuous case where g is differentiable and inverse is monotonic

### 00:23:23 · Speaker 1

Only for this specific case have considered it

### 00:23:28 · Speaker 1

Not for any other case

### 00:23:30 · Speaker 4

And then one question

### 00:23:32 · Speaker 1

Go ahead

### 00:23:33 · Speaker 4

How are we getting uh the derivative of g inverse of phi

### 00:23:39 · Speaker 4

Can you please elaborate a bit on this?

### 00:23:48 · Speaker 1

You okay? Uh, you you you remember inverse function rule? You know inverse function rule?

### 00:23:56 · Speaker 3

Maybe I'm missing out on that

### 00:24:00 · Speaker 1

Okay

### 00:24:03 · Speaker 1

So now to do so we should go on some more ideas

### 00:24:22 · Speaker 2

Is it the same as Jane's rule gentlemen or

### 00:24:25 · Speaker 1

Now it is basically the derivative of inverse

### 00:24:32 · Speaker 1

Okay, now how do you, okay, uh, uh, yes, yes, it is chain rule. It is basically chain rule only. Now, how do you, how do you calculate, uh, so.

### 00:24:44 · Speaker 1

See okay uh

### 00:24:47 · Speaker 1

1 by x square

### 00:24:51 · Speaker 1

How do you do it

### 00:24:57 · Speaker 2

x square inverse and then

### 00:25:00 · Speaker 1

In the same way you proceed

### 00:25:09 · Speaker 1

So it is basically d by dx of x to the power of minus 2

### 00:25:17 · Speaker 1

And how do you proceed? Tell me the full equation. How do you do it?

### 00:25:23 · Speaker 2

Find the one that fits

### 00:25:23 · Speaker 4

So this is minus 2x minus 3

### 00:25:24 · Speaker 3

Still extra

### 00:25:28 · Speaker 1

Yeah, so fine. So always confusions will be there. You would have left all this differentiation integration some time ago because of which so we'll be rusty about the formulas, but that is fine. But the intuition is clear. Now, now does that answer your question? Whoever asked this.

### 00:25:54 · Speaker 4

not completely so if we are trying to relate inverse in terms of a reciprocal then maybe i am not able to understand that

### 00:26:08 · Speaker 2

I think Sanchit you can just check for this chain rule then you will get to know that how it works

### 00:26:14 · Speaker 1

How do you how do you do it? Okay. No, okay. This rather than that, my previous example was much more simpler. D by DX of 1 over X square. How do you solve this?

### 00:26:28 · Speaker 4

So this is x to the power of minus 2. The rule will be d by dx of x to the power n, which is n x n minus 1. So in our case, n is minus 2. It will be minus.

### 00:26:37 · Speaker 1

10 is minus 2, it will be minus. If you don't, if you don't want to use that, is there any other way of doing it?

### 00:26:47 · Speaker 2

It is uh I think f of g of x right I mean how do you evaluate

### 00:26:52 · Speaker 4

Do you want to edit your file for me?

### 00:26:52 · Speaker 2

Yeah

### 00:26:54 · Speaker 4

F P of P of P by Q

### 00:27:00 · Speaker 1

So now in a similar manner you can obtain it for the previous case also.

### 00:27:10 · Speaker 1

Makes sense

### 00:27:15 · Speaker 1

Any other questions

### 00:27:31 · Speaker 2

Watch out for the next question

### 00:27:31 · Speaker 1

You look next

### 00:27:33 · Speaker 2

Why that monotonically not increasing I mean where does that come into picture

### 00:27:39 · Speaker 1

So

### 00:27:46 · Speaker 1

that comes into picture in these steps

### 00:27:51 · Speaker 1

Okay, now that is something that I have put it under rug. I have put it under rug. So now first you should understand what is monotonic sequence for that. Now since we haven't discussed monotonic sequence and other stuff, so let's not go there. Okay, I mean is it coming from

### 00:28:05 · Speaker 2

I mean is it coming from the definition of CDF that it should always be increasing monotonically non-decreasing

### 00:28:11 · Speaker 1

decrease yes yes yeah it is non-decreasing it is not increasing okay cdf is monotonically non-increasing monotonically uh non-decreasing

### 00:28:21 · Speaker 1

Okay. Yeah. So it's it's like you have multiple layers of stuff. Okay. How much ever you peel, no, there will be something that is below it. Okay. Now we should somewhere put a stop. So now I'll always give this example. Now this example may be like. So there is something called as real analysis.

### 00:28:46 · Speaker 1

What is one plus one

### 00:28:51 · Speaker 1

It is straightforward answer. But do you know the proof for one plus one is equal to two runs for three pages?

### 00:29:00 · Speaker 1

There is a proper proof to say that one plus one is two, which run for three pages.

### 00:29:08 · Speaker 1

Okay, now at some point or the other, now we should stop it. Now, my point of discussion is like, at least at the top level, we should be able to understand the stuff and the derivations that we'll be looking in class and the tutorials.

### 00:29:26 · Speaker 1

So now the next idea that we will be looking into is dKL is non-negative.

### 00:29:32 · Speaker 1

So now to do this now let's try to fix up some things

### 00:29:43 · Speaker 1

Let's start

### 00:29:45 · Speaker 1

P and Q

### 00:29:48 · Speaker 1

Be there

### 00:29:54 · Speaker 1

the distribution function

### 00:29:58 · Speaker 1

Okay, let P and Q be the distribution function.

### 00:30:04 · Speaker 1

And then they have density or mass now let's PQ

### 00:30:16 · Speaker 1

density function

### 00:30:18 · Speaker 1

respectively

### 00:30:23 · Speaker 1

Now when I say these are two distribution functions now the basic assumption is the what is okay what is a random variable can you recall

### 00:30:43 · Speaker 1

But now in these assumptions P and Q they have the same omega is the assumption

### 00:30:50 · Speaker 1

The underlying omega is same as the

### 00:30:57 · Speaker 1

So let small p and q be the

### 00:31:03 · Speaker 1

density function

### 00:31:06 · Speaker 1

So how do you define BKL between two distributions let's say P and Q

### 00:31:16 · Speaker 1

to define this

### 00:31:27 · Speaker 1

This is integral of

### 00:31:35 · Speaker 1

X by

### 00:31:46 · Speaker 1

So now if

### 00:31:48 · Speaker 1

If we are considering the discrete random variable now then

### 00:31:54 · Speaker 1

KL between ah these two distributions P and Q

### 00:31:59 · Speaker 1

This will be summation over all x

### 00:32:08 · Speaker 1

logo

### 00:32:10 · Speaker 1

X by

### 00:32:17 · Speaker 1

So now let's try to do it for uh

### 00:32:21 · Speaker 1

the discrete case

### 00:32:24 · Speaker 1

Let's let's prove it

### 00:32:28 · Speaker 1

Let's prove it

### 00:32:31 · Speaker 1

discrete case

### 00:32:36 · Speaker 1

So when I mean discrete now what do I mean by discrete

### 00:32:41 · Speaker 1

in this case

### 00:32:47 · Speaker 4

The random variable is discrete

### 00:32:50 · Speaker 1

Random variable is discrete. Okay. Now please remember that both of them share the same sample space.

### 00:32:58 · Speaker 1

So it is not like they have different sample space

### 00:33:02 · Speaker 1

If they have different sample space you cannot even think of doing anything

### 00:33:07 · Speaker 1

So, now what do we want to prove? We want to prove dL is always greater than or equal to zero. Okay. So, now

### 00:33:16 · Speaker 1

to prove

### 00:33:21 · Speaker 1

decay and off

### 00:33:24 · Speaker 1

E cube is always greater than or equal to zero

### 00:33:31 · Speaker 1

No because of which I can write that

### 00:33:35 · Speaker 1

Minus decay law

### 00:33:39 · Speaker 1

PQ less than or equal to 0

### 00:33:45 · Speaker 1

Now minus the gale of

### 00:33:52 · Speaker 1

By definition this is

### 00:33:54 · Speaker 1

minus summation of x

### 00:33:58 · Speaker 1

Beef fix

### 00:34:01 · Speaker 1

log px

### 00:34:04 · Speaker 1

QX

### 00:34:07 · Speaker 1

So this is same as

### 00:34:09 · Speaker 1

summation over x

### 00:34:14 · Speaker 1

Log

### 00:34:16 · Speaker 1

U x y

### 00:34:20 · Speaker 1

So far so good

### 00:34:29 · Speaker 1

So now

### 00:34:38 · Speaker 1

We know that

### 00:34:43 · Speaker 1

Logies are

### 00:34:47 · Speaker 1

Log is a concave function. What is a concave function?

### 00:34:54 · Speaker 1

How does the log x graph look like?

### 00:35:18 · Speaker 1

Is this a concave function

### 00:35:25 · Speaker 3

Yeah

### 00:35:28 · Speaker 1

Okay what is a convex function then

### 00:35:36 · Speaker 1

How to how to get the convex function from log x now do you know any ways of doing getting it

### 00:35:43 · Speaker 2

Minus

### 00:35:45 · Speaker 1

Okay, this is some good idea. Let me put that minus

### 00:35:53 · Speaker 1

Logics

### 00:35:56 · Speaker 1

Is this a convex function

### 00:36:02 · Speaker 1

How do you know that it is a convex function

### 00:36:08 · Speaker 2

I think if you take any two points then they are always above the curve

### 00:36:14 · Speaker 2

I mean the line segment joining the two points is always above the

### 00:36:17 · Speaker 1

The idea is called as epigraph. Okay. That is the next idea that we will be discussing in the next tutorials. Okay. The idea is called as epigraph. We will come to that specific point in the next session that that's rightly correct. Okay. Now log is a concave function.

### 00:36:36 · Speaker 1

And then I invoke something that I haven't proved yet, will be proving it explicitly.

### 00:36:44 · Speaker 1

By there is something called as Jensen's inequality

### 00:36:51 · Speaker 1

And there are so many of these inequalities no no they're very much what do you call

### 00:36:57 · Speaker 1

Always there is something called Jensen's inequality

### 00:37:08 · Speaker 1

Have you heard of any other inequality?

### 00:37:12 · Speaker 1

No not the inequality in the society

### 00:37:15 · Speaker 1

In mathematics have you heard of any other inequality

### 00:37:18 · Speaker 2

Triangular inequality

### 00:37:20 · Speaker 1

triangle inequality apart from that in probability do you hear anything

### 00:37:31 · Speaker 1

there is something called as Chernoff bounds okay uh that is idea called as Markov inequalities these things will come they are very wonderful inequality to get the bounds okay now we will be discussing them in time now the Jensen's inequality basically says log of expectation of x is always less than expectation of log x

### 00:38:12 · Speaker 1

What is this

### 00:38:15 · Speaker 1

Is this expectation of log x

### 00:38:19 · Speaker 1

Does that look like this form

### 00:38:41 · Speaker 1

This is

### 00:38:55 · Speaker 1

Maybe I did a some some mistakes somewhere

### 00:39:01 · Speaker 1

So there is a negative symbol so I should be okay okay got it yeah

### 00:39:29 · Speaker 1

Why did I take this symbol?

### 00:39:38 · Speaker 1

Okay there is a negative symbol here now because of which I have taken the other other inequality now because of which I can cancel of this and this

### 00:39:54 · Speaker 2

Then I have a query here

### 00:39:56 · Speaker 1

Morning

### 00:39:58 · Speaker 2

We said e log x

### 00:40:01 · Speaker 2

Less than or equal to log EX, right? So in the previous example, it is not E.

### 00:40:06 · Speaker 3

log x right i mean expectation is px if it was px no this is this is

### 00:40:12 · Speaker 1

No this is this is eLogix

### 00:40:16 · Speaker 1

Okay now this is expectation of log x

### 00:40:20 · Speaker 1

Now how do you get expectation of log x?

### 00:40:24 · Speaker 3

a a summation of x into log x right that's what expectation of log x is right

### 00:40:33 · Speaker 1

Whom did you leave the density function for me?

### 00:40:43 · Speaker 1

Okay happens don't worry all these things we all of us will do these kinds of mistakes

### 00:40:50 · Speaker 1

Yeah

### 00:40:53 · Speaker 1

Okay so now what is this now?

### 00:41:02 · Speaker 1

What is Q

### 00:41:12 · Speaker 1

Or to be even more specific we are considering a discrete case in discrete case what is Q

### 00:41:20 · Speaker 4

Yeah

### 00:41:23 · Speaker 1

Now this is summation over all the x, what will be this?

### 00:41:29 · Speaker 1

this is

### 00:41:43 · Speaker 4

This should be one

### 00:41:45 · Speaker 4

Log one is zero.

### 00:41:48 · Speaker 1

The log one is zero correct

### 00:41:53 · Speaker 1

See, okay, let me let this not confuse you when I say again and again here I'm just carry forwarding this I'm not saying this this quantity is less than this quantity that is not what I mean. So if you are confusing with that You can always write this

### 00:42:13 · Speaker 1

And I'm reusing the same in the quality

### 00:42:20 · Speaker 1

So because of which what I can say

### 00:42:26 · Speaker 1

KL off

### 00:42:29 · Speaker 1

is always greater than zero hence the proof

### 00:42:51 · Speaker 1

Uh I have seen one mistake

### 00:42:56 · Speaker 1

Now if px is a density function can you define it clearly for me

### 00:43:12 · Speaker 1

So so see when you say fx of x now you say that this is from r to 0 1 right

### 00:43:27 · Speaker 1

What is

### 00:43:36 · Speaker 1

This is R two R

### 00:43:40 · Speaker 1

If on the other term

### 00:43:44 · Speaker 1

If x is a discrete random variable so then it is from

### 00:43:49 · Speaker 1

R two zero one

### 00:44:02 · Speaker 1

the difference that is the reason why your density is not a probability measure

### 00:44:10 · Speaker 1

Now this is not something that is coming out of because of this if something has to be a probability measure the outcome has to be between 0 and 1 right and everything has to be positive. Now it takes real values.

### 00:44:27 · Speaker 1

Make sense now?

### 00:44:38 · Speaker 1

Yeah so

### 00:44:42 · Speaker 1

I thought I'll be con starting with Jensen's inequality today

### 00:44:47 · Speaker 1

yeah we don't have much time yeah any questions we will stop for the day

### 00:44:55 · Speaker 2

Chandan in the mid-term there was one question that whether DKL is symmetric or not and if it is not symmetric what are the consequences of it so shall we cover this now or in the mid-term review

### 00:45:06 · Speaker 1

I'll what I'll do is I'll write the answers for everything see to be very frank I haven't seen the mid-sem questions at all let me be very frank okay now I'm a very what do you call this that that this will be there no so I I haven't seen I should start even so we should come up with answer script now what I'll do is I'll come up with an key solutions and then I'll put it out and then in the next tutorials that is next Wednesday if you have got any questions we'll surely take it

### 00:45:36 · Speaker 1

Okay

### 00:45:39 · Speaker 2

Yeah that's fine

### 00:45:41 · Speaker 1

Okay sorry I I so if Sarah has told me I would have looked into it even it did not come to me also sorry for that

### 00:45:50 · Speaker 1

We will look it up in the next session

### 00:46:04 · Speaker 3

And one more question

### 00:46:06 · Speaker 1

Black guys

### 00:46:07 · Speaker 4

So this probability density function, right? So that's a function from R to R you mentioned. It's basically the, if you differentiate the CDF, you get the probability density function, right?

### 00:46:23 · Speaker 1

Yeah if if X is a continuous random variable

### 00:46:25 · Speaker 4

if x is a continuous random variable so that can be looked at as a likelihood of the value taking x right x taking the value x

### 00:46:39 · Speaker 1

Why are you looking lightly here Okay fine then

### 00:46:43 · Speaker 4

Uh, would it go beyond zero and one in in so basically my question is like yeah would that uh value of px the density function go beyond zero and one? Yes, yes, yes that is what I said r2r

### 00:46:55 · Speaker 1

Yes yes yes that is what you said yes yes yes

### 00:46:57 · Speaker 4

Yes please can you give an example

### 00:47:00 · Speaker 1

It takes Gaussian distribution

### 00:47:04 · Speaker 1

Take take any Gaussian how is the density of the Gaussian distribution is

### 00:47:10 · Speaker 4

Yeah this is the density of the hose

### 00:47:10 · Speaker 1

This is the density of the Gaussian distribution

### 00:47:14 · Speaker 1

Okay, now, so if you make it sharper or larger, no, it will exceed the zero one. You can do it easily.

### 00:47:22 · Speaker 4

Yeah yeah yeah I yeah so for example even if you take a uniform distribution between zero and half

### 00:47:27 · Speaker 1

I'm not sure

### 00:47:28 · Speaker 4

And that can have a value two right and any point between zero and okay

### 00:47:29 · Speaker 1

can have a value two right at any point between zero and

### 00:47:36 · Speaker 4

Okay got it

### 00:47:45 · Speaker 2

But it is not defined for a particular point right it has to be always I mean the density function is it defined for any given point

### 00:47:55 · Speaker 2

We have to always take an interval right

### 00:48:00 · Speaker 2

So we can we cannot evaluate PDF at a particular point right

### 00:48:01 · Speaker 1

We cannot evaluate

### 00:48:05 · Speaker 1

no no no no what his question is correct your point is correct what his question basically is at any given point what will be the value you are correct it will be zero at at a single point correct but at any given interval also it can take more than uh uh zero one is my point

### 00:48:30 · Speaker 2

I think the question is like uh I mean how does it relate to the likelihood

### 00:48:36 · Speaker 1

No see okay don't don't bring in likelihood at all

### 00:48:40 · Speaker 1

Okay, so now it is much more simpler now without looking into likelihood and then see it as an R2R function.

### 00:48:52 · Speaker 1

Okay now that will be even simpler

### 00:48:53 · Speaker 2

Yeah

### 00:48:55 · Speaker 1

Okay, and it is much more simpler and say that this is not a probability function. It is not probability. Your mass is a probability, your distribution function is a probability, but your density is not probability.

### 00:49:46 · Speaker 1

No questions, no further questions.

### 00:49:55 · Speaker 1

So, meanwhile, maybe today or tomorrow at tomorrow or day after at max, I'll be putting the solutions for your quiz, sorry, for your test one online. So, you can look at it and then we will discuss any queries. So, in the next tutorial session. Okay. And then we will continue with.

### 00:50:21 · Speaker 1

proving of this uh uh what do you call Jensen's uh inequality and then we will continue with the discussions that are remaining.

### 00:50:30 · Speaker 1

Make sense

### 00:50:40 · Speaker 1

So thank you

### 00:50:44 · Speaker 1

Let's meet next week
