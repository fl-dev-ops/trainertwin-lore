---
id: wjFSuXgeHrY
title: Deep Generative Models Tutorial Probability theory
date: '2024-11-23'
url: https://www.youtube.com/watch?v=wjFSuXgeHrY
description: ''
author: prathoshap5226
duration: 00:50:45
model: saaras:v3
transcript: true
---

# Deep Generative Models Tutorial Probability theory

## Transcript

### 00:00:02 · Speaker 3

leader

### 00:00:05 · Speaker 3

only the weights of network two will be updated.

### 00:00:09 · Speaker 3

okay? That is how you can make sense of it. I have given you one Stanford course, okay? Now there go to the course notes, and then there you can see some of the topics wherein which he explains back propagation. So where he takes sigmoid node explicitly.

### 00:00:29 · Speaker 1

Hello

### 00:00:29 · Speaker 3

He takes a specific sigmoid node and then he explains how to do the back propagation.

### 00:00:37 · Speaker 3

Okay, to that specific sigmoid node. It's in the course notes of the link that I have given.

### 00:00:37 · Speaker 5

to that specific sigmoid node

### 00:00:43 · Speaker 5

Okay, we'll check that.

### 00:00:44 · Speaker 3

No, this is, yeah, this is one of the very good resources on CNNs.

### 00:00:49 · Speaker 3

Now they have really given a very good resource on CNNs. Now to understand CNN, so this is one of the best resource that I have come across. I'm not saying that there might be some other good resources. But this is one of the notes that I have come across and apart from that one other resource that I have come across is three blue one brown channel. Everybody knows three blue one brown?

### 00:01:16 · Speaker 5

Yeah, at least I'm aware.

### 00:01:18 · Speaker 3

yeah, three blue one brown channel. Now there you can look at the convolution. So he has a specific chapters on neural networks. Now there you can look at it, you know, when which the queries will be resolved.

### 00:01:33 · Speaker 5

Yeah, sure, sure, Chandan, I think. Maybe we can continue with the tutorial.

### 00:01:35 · Speaker 3

Yeah. Continue with the tutorial. So, any other questions you have? Any others?

### 00:01:48 · Speaker 1

So things are going on comfortably, no issues are there.

### 00:01:57 · Speaker 3

Okay

### 00:01:58 · Speaker 3

So now with this, let's try to continue with today's discussion. Now today's discussion is basically around some of the topics that sir would have left in between for TS to fill in the some of the proofs and some of the algebra.

### 00:02:16 · Speaker 3

Okay. Now in that manner we will take some of the ideas from wherever he has left. I have listed some of the important points. I'm not I'm not going till the first session. I'm trying to finish off the things that he has recently done. Now so that your V A E and other stuffs so after V A E he will go to the diffusion models. Now once he goes to diffusion models so you should be comfortable with those topics.

### 00:02:46 · Speaker 3

So, I what I thought is rather than going ahead with a lot of previous things that was there, there were some ideas on probability which whenever type permits we will come back. So we will be looking into some of the stuff that sir has left in BAE.

### 00:03:04 · Speaker 3

Okay. So now, the some of the basic proofs that I thought we will be covering today is one is KL divergence is always positive and then the idea of law of the unconscious statistician.

### 00:03:20 · Speaker 3

depending on that we will see whether we will be we will be able to go ahead with other ideas

### 00:03:24 · Speaker 1

will be

### 00:03:29 · Speaker 1

Okay. I'll just stop with that.

### 00:03:37 · Speaker 1

So now first we will take this weird

### 00:03:42 · Speaker 3

think that is law of the unconscious statistician. This is one of the very important ideas that you find in probability.

### 00:03:57 · Speaker 1

law of the

### 00:04:15 · Speaker 1

law of the unconscious statistician also called as lotus. Not any party symbol but just the abbreviation.

### 00:04:29 · Speaker 1

So now it is used to calculate

### 00:04:39 · Speaker 1

used to calculate expectation of

### 00:04:44 · Speaker 1

a function of a random variable.

### 00:04:48 · Speaker 1

Okay

### 00:04:52 · Speaker 1

Now G of X

### 00:04:55 · Speaker 1

is a

### 00:04:59 · Speaker 1

is a function of a random variable X

### 00:05:09 · Speaker 1

and then the assumption is

### 00:05:16 · Speaker 1

distribution of X is known

### 00:05:23 · Speaker 1

and

### 00:05:23 · Speaker 3

and g of x is unknown

### 00:05:28 · Speaker 3

If g of x is known then you can directly get the density and then do the stuff. But it is not meant to be.

### 00:05:38 · Speaker 3

let's say P X

### 00:05:41 · Speaker 3

Now let this be

### 00:05:44 · Speaker 3

PMF or

### 00:05:48 · Speaker 3

PDF of X. Depending on whether X is a discrete random variable or a continuous random variable. Now what I'll be doing is I'll be going ahead with the continuous case. Proof for the continuous case is much simpler.

### 00:06:09 · Speaker 1

So I'll be going ahead with the

### 00:06:13 · Speaker 1

Proof for the

### 00:06:19 · Speaker 1

continuous case

### 00:06:23 · Speaker 1

Okay, Now let's say Y is

### 00:06:27 · Speaker 1

g of x

### 00:06:30 · Speaker 1

Okay, and then

### 00:06:32 · Speaker 1

we assume some ideas

### 00:06:33 · Speaker 1

G

### 00:06:35 · Speaker 1

we say that G is

### 00:06:40 · Speaker 1

differentiable

### 00:06:46 · Speaker 1

and its

### 00:06:51 · Speaker 1

Inverse

### 00:06:52 · Speaker 3

Chandan

### 00:06:53 · Speaker 1

Chandan

### 00:06:54 · Speaker 1

Ha

### 00:06:55 · Speaker 6

Candon

### 00:06:55 · Speaker 3

Candon

### 00:06:55 · Speaker 1

Yes sir

### 00:06:55 · Speaker 3

Yes sir

### 00:06:57 · Speaker 6

Sorry, I interrupted you. Proposal. Yes sir.

### 00:07:00 · Speaker 3

Yes sir. Yes sir, yes sir, got it.

### 00:07:02 · Speaker 6

Yeah, I I mean, if you can maybe just solve the midterm exam questions, no? That would I think be useful.

### 00:07:13 · Speaker 3

Oh, I I I myself did not prepare for it.

### 00:07:19 · Speaker 3

Yeah.

### 00:07:20 · Speaker 5

So can we have a separate tutorial for it this week maybe for that?

### 00:07:21 · Speaker 6

separate to

### 00:07:24 · Speaker 6

Yeah yeah no problem maybe next week. Yeah maybe next week. Yes sure sure.

### 00:07:24 · Speaker 3

problem

### 00:07:26 · Speaker 3

Yes, sure, sure, sure, sir.

### 00:07:28 · Speaker 5

or even region is fine I think maybe. that that I mean going through the mid sem is also something which we wanted to go through so.

### 00:07:28 · Speaker 3

और इवन एस वी के साथ

### 00:07:35 · Speaker 3

Sure, we will surely do it in the next session, sir. Yeah.

### 00:07:41 · Speaker 6

Chandan, one other thing, yaar, I am sorry I disturbed you.

### 00:07:43 · Speaker 3

Yes sir. No no no no problem sir. Yes sir.

### 00:07:44 · Speaker 6

No problem

### 00:07:45 · Speaker 6

Yes sir. This Saturday I will take the class between 8:00 AM 11:00 AM.

### 00:07:48 · Speaker 3

Yes sir. 11 yeah yeah yeah yeah I saw the message.

### 00:07:51 · Speaker 6

Yeah yeah

### 00:07:53 · Speaker 6

Yeah, so you have the quiz at 11 o'clock, okay? Sure. After the class.

### 00:07:55 · Speaker 3

Sure, after the class. Sure, sure. Yeah. Your son's interview is there.

### 00:07:59 · Speaker 6

your

### 00:08:01 · Speaker 6

Oh yeah, I mean, yeah. Sir, all the all the best with the interview.

### 00:08:02 · Speaker 3

सर ऑल द ऑल द बेस्ट विद द इंटरव्यू सर

### 00:08:07 · Speaker 6

See the guy cannot talk they want to interview him I don't know. I mean these Bangalore schools right I don't know what they are up to.

### 00:08:18 · Speaker 2

So they will interview your son or like you also. I mean I don't know.

### 00:08:18 · Speaker 6

Anyway

### 00:08:22 · Speaker 6

actually last night otherwise why would I go no I mean my wife could have gone so they have asked specifically asked both the parents to be present with the child. so they have to go I'll do that. Chandan you have the quiz that it's it's called Kumarans one of the schools in the South Bengaluru.

### 00:08:33 · Speaker 3

I'll do that. Chandan, you have the

### 00:08:37 · Speaker 3

It's called

### 00:08:40 · Speaker 6

Yeah, so have

### 00:08:41 · Speaker 3

So how the sixth sixth cross sir DVG road

### 00:08:46 · Speaker 6

टाटा सिल्क फार्म है यार इवं

### 00:08:48 · Speaker 3

Tata Silk Farm, Yeah, Yeah.

### 00:08:50 · Speaker 6

Yeah, so have that quiz on eleven o'clock, okay, at eleven o'clock. And one other thing, somebody asked me to not have the quiz on second of November. Right, because that's like a series of holidays and yeah, sort of Diwali, right? So what we can do, no, nineteenth we will have a quiz, twenty-sixth we will have another quiz. Okay.

### 00:08:52 · Speaker 3

And one other thing

### 00:09:02 · Speaker 3

of holiday

### 00:09:12 · Speaker 3

Sure sir

### 00:09:13 · Speaker 6

twenty six we'll have another course. Maybe I'll discuss that in today I mean Saturday's lecture. I just wanted to let you know that that one of these tutorials no you can see maybe or you can do another thing. Why don't you just solve the midterm questions and just upload it in the group. You don't have to spend time.

### 00:09:14 · Speaker 3

Yes

### 00:09:30 · Speaker 3

time that that I'll do. Yeah.

### 00:09:32 · Speaker 6

I think that would be easier

### 00:09:33 · Speaker 3

sure sure sure that I'll do. And we can we can ask doubts

### 00:09:36 · Speaker 5

And we can we can ask doubts if any I mean anyway it would yeah we can ask the doubts if any so

### 00:09:38 · Speaker 3

Anyway it would

### 00:09:39 · Speaker 6

Yeah, okay.

### 00:09:42 · Speaker 3

to be

### 00:09:42 · Speaker 2

easy

### 00:09:43 · Speaker 6

Okay

### 00:09:44 · Speaker 6

Sorry Chandan, I disturbed you. Please continue.

### 00:09:46 · Speaker 3

No, no, no, no, no problem, sir. No problem. Yeah.

### 00:09:48 · Speaker 6

Yeah

### 00:09:49 · Speaker 3

Yeah

### 00:09:52 · Speaker 3

Sorry Chandan

### 00:09:52 · Speaker 5

Sorry Chandan

### 00:09:54 · Speaker 3

P

### 00:09:54 · Speaker 5

Before going into mathematics detail, can you just suggest what is the intuition why we are doing this law of unconscious mind?

### 00:09:54 · Speaker 3

Before going into method

### 00:10:01 · Speaker 3

I'll I'll I'll come to that. I'll I'll exactly come to that. Okay. See, for example, I'll I'll give you a very simple idea. To calculate... It comes up in the...

### 00:10:04 · Speaker 5

Okay

### 00:10:09 · Speaker 6

It comes up in reparameterization, no? It came up in reparameterization.

### 00:10:12 · Speaker 3

Yes

### 00:10:15 · Speaker 3

Now

### 00:10:16 · Speaker 3

reparameterization. So even a simple idea is to calculate the variance, you want expectation of x square.

### 00:10:24 · Speaker 3

x square is a function of x. We know how to calculate the expectation of x. How to calculate the expectation of x square, we need the idea of Lotus. That's the simplest example that we can think of.

### 00:10:37 · Speaker 6

Okay

### 00:10:38 · Speaker 3

In addition to re-patternization, that's what sir said, the simplest idea that we can think of is, Yeah.

### 00:10:42 · Speaker 6

Good example

### 00:10:44 · Speaker 6

good example. I like it. Yeah.

### 00:10:46 · Speaker 3

Thank you sir

### 00:10:49 · Speaker 3

Yeah

### 00:10:51 · Speaker 1

my internet got disconnected just just give me one minute

### 00:10:56 · Speaker 1

Yellow tough guys

### 00:11:11 · Speaker 1

सर, इन बिटवीन व्हाट विल बी द सिलेबस फॉर द नेक्स्ट क्विज?

### 00:11:15 · Speaker 5

It be the last two classes

### 00:11:18 · Speaker 3

whatever has been covered till the previous quiz and the see we cannot compartmentalize things like that for example if I ask you a simple question on probability now you cannot say that this is quiz one's topics and this we cannot eliminate right?

### 00:11:22 · Speaker 5

Okay

### 00:11:26 · Speaker 5

simple

### 00:11:28 · Speaker 5

you

### 00:11:31 · Speaker 5

Yeah, you cannot tell, right?

### 00:11:34 · Speaker 4

Yeah

### 00:11:36 · Speaker 6

But Chandan don't ask things that I'm going to No no no no no no no no no no no no no no no. You can be Markovian. He should be ergodic.

### 00:11:38 · Speaker 3

No, no, no, no. No, no, no, no, no, no, no, no, no, no, no.

### 00:11:45 · Speaker 3

No, no, no, no, no, no, no, that I will not do, sir.

### 00:12:01 · Speaker 1

So now the idea is, see, the first

### 00:12:04 · Speaker 3

First of all, let's try to understand the name itself. So now, it is called as law of the unconscious statistician.

### 00:12:11 · Speaker 3

Okay, now you will be able to understand why it is called such in some time. Okay, so it is not like simply they just use that name. Okay, it has a very deeper meaning to it. So the idea is you apply it in a totally in an unconscious, an unconscious way.

### 00:12:31 · Speaker 1

Okay

### 00:12:34 · Speaker 1

What is this? What happened? Fair screen.

### 00:12:52 · Speaker 1

able to see my iPad screen? Okay.

### 00:12:55 · Speaker 3

So now, we know how to, we know how to calculate the expectation of X. Now, but now what we have is expectation, so we have a function of random variable. Now, for which we want to know how to calculate the expectation.

### 00:13:12 · Speaker 3

So now let's try to understand how to do it. Okay. So now the the conditions that we are imposing on G is now the function G that we have should be differentiable and the inverse should be monotonic. Okay.

### 00:13:28 · Speaker 3

So under these assumptions, once we have these assumptions, now the current

### 00:13:35 · Speaker 3

code will work. I'll tell you how each of the conditions make sense. Okay. So now

### 00:13:44 · Speaker 1

Hello

### 00:13:46 · Speaker 1

if y is g of x then

### 00:13:50 · Speaker 1

X is

### 00:13:54 · Speaker 1

G inverse of Y

### 00:13:59 · Speaker 1

Okay

### 00:14:02 · Speaker 1

So now, what is

### 00:14:07 · Speaker 1

d by dy of g inverse of y

### 00:14:15 · Speaker 1

What do you say about this?

### 00:14:17 · Speaker 1

Can you compute this?

### 00:14:23 · Speaker 1

intuitively can you think of the formula for this?

### 00:14:35 · Speaker 1

Okay. So now this is

### 00:14:40 · Speaker 1

So just go ahead and refresh your calculus stuff.

### 00:14:49 · Speaker 1

the inverse of Y

### 00:14:51 · Speaker 1

Now this is, now this is

### 00:14:54 · Speaker 1

This is by the

### 00:14:59 · Speaker 1

inverse function rule

### 00:15:04 · Speaker 1

Okay, now

### 00:15:06 · Speaker 1

That is nothing but this is d x

### 00:15:10 · Speaker 1

equals

### 00:15:12 · Speaker 1

one over

### 00:15:16 · Speaker 1

the inverse of y d y

### 00:15:19 · Speaker 1

Okay

### 00:15:19 · Speaker 3

Okay

### 00:15:21 · Speaker 3

Now all these things are fine. Now where is this coming into picture? Okay, let's write what is expectation of g of x.

### 00:15:31 · Speaker 3

How do you write it? Now this is continuous thing is what my assumption is. This is integral of

### 00:15:37 · Speaker 3

y into f y of y dy. This is how I write it, right?

### 00:15:47 · Speaker 2

sorry. It's G dash of G inverse of Y, right? One Y. I mean, we should take the differential of G.

### 00:15:47 · Speaker 3

sorry

### 00:15:48 · Speaker 3

G

### 00:15:56 · Speaker 2

Maybe I am wrong, sorry.

### 00:15:58 · Speaker 3

नो नो जस्ट जस्ट गो अहेड नो दिस इज करेक्ट

### 00:16:00 · Speaker 2

ஓகே

### 00:16:03 · Speaker 3

Now

### 00:16:05 · Speaker 3

Now what is the

### 00:16:09 · Speaker 3

distribution function of Y. Now this is probability that

### 00:16:13 · Speaker 3

y is less than or equal to y. Correct? Now this is nothing but

### 00:16:19 · Speaker 1

probability that

### 00:16:21 · Speaker 1

y is less than or equal to g of x

### 00:16:27 · Speaker 1

Correct

### 00:16:31 · Speaker 1

Now this will be

### 00:16:33 · Speaker 1

This will be probability that

### 00:16:39 · Speaker 1

X will be

### 00:16:42 · Speaker 1

less than or equal to C inverse of

### 00:16:47 · Speaker 1

Agree with me so far? Simple?

### 00:16:53 · Speaker 1

So this is

### 00:16:54 · Speaker 1

FX of

### 00:16:58 · Speaker 1

effects of

### 00:17:01 · Speaker 1

G inverse of Y

### 00:17:06 · Speaker 1

Now

### 00:17:07 · Speaker 3

I know the distribution function of Y in terms of X. I know, see, what is my assumption? Now let's go back to my assumption. Now, I know I am saying the distribution function of X is known. Now, because of this trick that I have used, I know the distribution function of Y also now.

### 00:17:28 · Speaker 3

Now, once I know the distribution, once I know the distribution, Yeah, yeah, go ahead.

### 00:17:30 · Speaker 0

children. Once I know

### 00:17:33 · Speaker 0

I have a question. So, uh, when you invert the, uh, G, right, to the other side, X would be greater than G inverse of Y, right?

### 00:17:39 · Speaker 3

food

### 00:17:43 · Speaker 3

A is less than B

### 00:17:47 · Speaker 1

Hmm

### 00:17:51 · Speaker 3

one over A is greater than one over B

### 00:17:56 · Speaker 1

Yeah

### 00:17:59 · Speaker 3

one over B is less than one over A.

### 00:18:04 · Speaker 1

Yeah

### 00:18:05 · Speaker 3

Answer to your question

### 00:18:08 · Speaker 0

Yeah. I think I'll have to, I'll take a look.

### 00:18:13 · Speaker 3

no no no no no no no there is nothing there.

### 00:18:15 · Speaker 0

Yes, G inverse of Y is one

### 00:18:18 · Speaker 3

See, what is this is A. Okay, let let's come back here, no? This is A, this is B, correct?

### 00:18:26 · Speaker 1

Hmm

### 00:18:28 · Speaker 3

apply this idea, you will get this. Exactly the same steps.

### 00:18:33 · Speaker 1

Okay

### 00:18:34 · Speaker 3

No, inversion in terms of scalar is one by A, right?

### 00:18:37 · Speaker 1

Correct

### 00:18:38 · Speaker 3

exactly the same thing. See the inversion that is happening, you know, B is coming here.

### 00:18:44 · Speaker 3

and A is coming here. You can see that.

### 00:18:47 · Speaker 0

Yeah, yeah. No, it's clear.

### 00:18:49 · Speaker 3

Okay? Now it's clear, exactly the same idea.

### 00:18:53 · Speaker 0

Okay

### 00:18:54 · Speaker 3

Okay? Yeah.

### 00:18:55 · Speaker 0

Thanks, Jita

### 00:18:56 · Speaker 3

Now, okay, whatever questions you have, you can stop me anytime. Okay, see, what is what will be happening is, from most of the times these will be like more of a mathematical work rather than what do you call any intuition or any stuff working. Okay, now this is basically most of the times our discussions will be more on a mathematical proof kind of ideas. Okay, so sometimes it is known that we will lose path.

### 00:19:22 · Speaker 1

Hello

### 00:19:26 · Speaker 3

Now at that time we should take simple ideas like this to understand intuitively what is the steps that we are doing.

### 00:19:33 · Speaker 3

Okay. So now, now, now finally, now I know the distribution function. Now if I know the distribution function, can I get the density function?

### 00:19:46 · Speaker 1

Yes, differentiate idhu

### 00:19:48 · Speaker 3

differentiated, that's all. effects of

### 00:19:48 · Speaker 1

Fifth

### 00:19:53 · Speaker 3

G inverse of Y

### 00:19:56 · Speaker 1

one by

### 00:19:59 · Speaker 1

your

### 00:20:03 · Speaker 1

Makes sense?

### 00:20:11 · Speaker 1

Okay, so now let's go back to expectation of

### 00:20:16 · Speaker 1

g of x

### 00:20:19 · Speaker 3

Okay. What is expectation of g of x? This is integral of y into f y of y dy, correct?

### 00:20:29 · Speaker 3

Now this is nothing but

### 00:20:32 · Speaker 3

What is y is g of x

### 00:20:36 · Speaker 3

Correct? y is g of x.

### 00:20:38 · Speaker 3

What is f y of

### 00:20:40 · Speaker 1

y that is fx of

### 00:20:44 · Speaker 1

G inverse of Y

### 00:20:50 · Speaker 1

into

### 00:20:52 · Speaker 1

one by

### 00:20:55 · Speaker 1

g into g inverse of y dy. What is g inverse of y?

### 00:21:06 · Speaker 1

G inverse of Y is X

### 00:21:09 · Speaker 1

and this

### 00:21:12 · Speaker 1

is dx

### 00:21:17 · Speaker 1

This will be

### 00:21:19 · Speaker 1

Integral of

### 00:21:21 · Speaker 1

g of x

### 00:21:24 · Speaker 1

f x of x d x. Now this is expectation of

### 00:21:30 · Speaker 1

of X

### 00:21:32 · Speaker 1

This is the proof

### 00:21:36 · Speaker 3

See what is this fellow saying? See if you have a function don't worry apply this g of x on everything and then use the density of x only. Which is mathematically crazy to us right?

### 00:21:54 · Speaker 3

But as it turns out with these proof

### 00:21:58 · Speaker 1

it is very much clear to us, yeah, this is working.

### 00:22:04 · Speaker 1

Does it make sense?

### 00:22:09 · Speaker 1

No, that is why it is called as unconscious

### 00:22:11 · Speaker 3

decision. You you don't even have to be conscious. So just apply the function and take the density of X only or density or mass of X only.

### 00:22:20 · Speaker 3

it will work immediately. You don't need to worry about at all.

### 00:22:25 · Speaker 3

Okay? That is why this fellow is called as law of the unconscious statistician.

### 00:22:34 · Speaker 3

Make sense? Why it is called as law

### 00:22:36 · Speaker 1

of the unconscious statistician.

### 00:22:42 · Speaker 3

Hello

### 00:22:48 · Speaker 1

Good

### 00:22:52 · Speaker 1

I have done it in steps. Now to get this,

### 00:22:56 · Speaker 1

I did this. This.

### 00:23:04 · Speaker 1

Okay? That's all, very simple.

### 00:23:08 · Speaker 1

Any questions with this proof?

### 00:23:10 · Speaker 3

done it only for the continuous case

### 00:23:13 · Speaker 3

That too on a very restricted continuous case. Where G is differentiable and inverse is monotonic.

### 00:23:23 · Speaker 3

okay? Only for this specific case, I have considered it.

### 00:23:28 · Speaker 3

not for any other case.

### 00:23:30 · Speaker 4

Chandan, one question.

### 00:23:32 · Speaker 3

Go ahead

### 00:23:33 · Speaker 4

How are we getting the derivative of g inverse of y? Can you please elaborate a bit on this?

### 00:23:45 · Speaker 1

See

### 00:23:48 · Speaker 1

You okay, uh you you you remember inverse function rule? You know inverse function rule?

### 00:23:56 · Speaker 4

maybe I am missing out on that

### 00:24:00 · Speaker 1

Okay

### 00:24:03 · Speaker 1

So now to do so we should go on some more ideas

### 00:24:22 · Speaker 3

That's the same as chain rule, Chandan, or

### 00:24:25 · Speaker 1

Now it is basically the derivative of inverse.

### 00:24:32 · Speaker 3

Okay, now

### 00:24:34 · Speaker 3

How do you okay? Yes, yes, it is chain rule. It is basically chain rule only. Now how do you how do you calculate so

### 00:24:44 · Speaker 3

See, okay.

### 00:24:47 · Speaker 1

one by x square

### 00:24:51 · Speaker 1

How do you do it?

### 00:24:57 · Speaker 3

X

### 00:24:57 · Speaker 5

square inverse and then

### 00:25:00 · Speaker 1

Correct. In the same way you proceed.

### 00:25:08 · Speaker 1

ओके। नो इट इज बेसिकली डी बाय डी एक्स ऑफ एक्स टू द पावर ऑफ माइनस टू।

### 00:25:17 · Speaker 3

And how do you proceed? Tell me the full equation. How do you do it?

### 00:25:23 · Speaker 0

minus one by minus two x minus three

### 00:25:23 · Speaker 1

minus one by

### 00:25:24 · Speaker 4

minus 2x minus

### 00:25:28 · Speaker 3

Yeah. So fine. So always confusions will be there. uh You you would have left all this differentiation integration some time ago because of which so we'll be rusty about the formulas but that is fine. But the intuition is clear. Now now does that answer your question whoever asked this?

### 00:25:54 · Speaker 1

not complete

### 00:25:55 · Speaker 4

completely. So, if we are trying to relate inverse in terms of a reciprocal, then maybe I'm not able to understand that, like

### 00:26:05 · Speaker 3

Okay

### 00:26:07 · Speaker 5

I think Sanchit you can just check for this chain rule then you will get to know that how it works

### 00:26:14 · Speaker 3

How do you how do you do it? Okay. No, okay, this rather than that my previous example was much more simpler. d by dx of one over x square. How do you solve this?

### 00:26:28 · Speaker 4

So this is x to the power of minus two. The rule will be d by dx of x to the power n which is n x n minus one. So in our case n is minus two it will be minus

### 00:26:31 · Speaker 3

school will

### 00:26:37 · Speaker 3

is minus two it will be minus if you don't if you don't want to use that is there any other way of doing it

### 00:26:47 · Speaker 5

Yeah, it is, I think, F of G of X, right? I mean, how do you evaluate derivative of F of G of X?

### 00:26:52 · Speaker 4

d by d derivative of f of g of x. f p of p by q.

### 00:26:58 · Speaker 3

Correct. So now in a similar manner you can obtain it for the previous case also.

### 00:27:05 · Speaker 3

ಓಕೆ

### 00:27:09 · Speaker 1

Okay

### 00:27:09 · Speaker 3

like

### 00:27:10 · Speaker 1

Makes sense? Okay.

### 00:27:12 · Speaker 3

Okay

### 00:27:14 · Speaker 1

Okay, any other questions?

### 00:27:31 · Speaker 5

Chandan, next question

### 00:27:31 · Speaker 1

Question

### 00:27:32 · Speaker 1

Hmm

### 00:27:33 · Speaker 5

Why that monotonically increasing, I mean where does that come into picture?

### 00:27:38 · Speaker 1

So

### 00:27:42 · Speaker 1

Uh,

### 00:27:46 · Speaker 3

that comes into picture in these steps.

### 00:27:51 · Speaker 3

okay. That is something that I have put it under rug. I have put it under rug. So now first you should understand what is monotonic sequence for that. Now since we haven't discussed monotonic sequence and other stuff. So let's not go there.

### 00:27:53 · Speaker 5

okay

### 00:28:04 · Speaker 3

Okay. I mean, is it coming from

### 00:28:04 · Speaker 5

I mean is it coming from the definition of CDF that it should always be increasing monotonically and not decreasing

### 00:28:08 · Speaker 3

teach

### 00:28:11 · Speaker 3

Yes, yes, yes. It is non-decreasing. It is not increasing. Okay. CDF is monotonically non-increasing, monotonically non-decreasing.

### 00:28:21 · Speaker 3

Okay. Yeah, so it's it's like you have multiple layers of stuff. Okay. How much ever you peel, no, there will be something that is below it. Okay. Now we should somewhere put a stop.

### 00:28:35 · Speaker 3

So now I'll always give this example. Now this example may be like uh so there is something called as real analysis. Okay? What is one plus one?

### 00:28:49 · Speaker 3

two, right? That is straightforward answer. But do you know the proof for one plus one is equal to two runs for three pages?

### 00:28:59 · Speaker 3

There is a proper proof to say that one plus one is two, which run for three pages.

### 00:29:08 · Speaker 3

Okay. Now at some point or the other, now we should stop it. Now my point of discussion is like at least at the top level, now you should be able to understand the stuff and the derivations that we'll be looking in class and the tutorials. Okay. Yeah.

### 00:29:26 · Speaker 3

Okay. So now the next idea that we will be looking into is D K L is non-negative.

### 00:29:31 · Speaker 1

Okay. So now to do this, now let's try to fix up some things.

### 00:29:40 · Speaker 1

Hello

### 00:29:43 · Speaker 1

Let

### 00:29:45 · Speaker 1

P and Q

### 00:29:48 · Speaker 1

Be the

### 00:29:54 · Speaker 1

the distribution function.

### 00:29:58 · Speaker 1

ओके, लेट पी एंड क्यू बी द डिस्ट्रीब्यूशन फंक्शन।

### 00:30:02 · Speaker 1

Okay. And then they have density or mass. Let's P Q.

### 00:30:10 · Speaker 1

Leader

### 00:30:15 · Speaker 1

density function

### 00:30:18 · Speaker 1

respectively

### 00:30:23 · Speaker 1

Now when I say

### 00:30:23 · Speaker 3

Okay, uh, these are two distribution functions. Now, the basic assumption is, uh, the what is, okay, uh, what is a random variable? Can you recall?

### 00:30:37 · Speaker 2

function from

### 00:30:38 · Speaker 3

X is from

### 00:30:40 · Speaker 2

function from omega to R

### 00:30:43 · Speaker 3

Correct? Now, in these assumptions, P and Q, they have the same omega is the assumption.

### 00:30:49 · Speaker 3

Okay? The underlying omega is same as the thing.

### 00:30:54 · Speaker 3

Fine

### 00:30:55 · Speaker 1

Okay

### 00:30:57 · Speaker 1

So let small p and q be the

### 00:31:03 · Speaker 1

density function

### 00:31:06 · Speaker 1

Uh so how do you define D K L between two distributions? Let's say P and Q.

### 00:31:16 · Speaker 1

How did you define this?

### 00:31:27 · Speaker 1

This is integral of

### 00:31:29 · Speaker 1

P X

### 00:31:32 · Speaker 1

log

### 00:31:35 · Speaker 1

X by

### 00:31:37 · Speaker 1

QX

### 00:31:41 · Speaker 1

Correct?

### 00:31:45 · Speaker 1

So now if

### 00:31:48 · Speaker 1

if we are considering the discrete random variable,

### 00:31:52 · Speaker 1

then

### 00:31:54 · Speaker 1

E K L

### 00:31:55 · Speaker 1

between these two distribution

### 00:31:56 · Speaker 1

P and Q

### 00:31:59 · Speaker 1

This will be

### 00:32:01 · Speaker 1

summation over all x

### 00:32:05 · Speaker 1

PX

### 00:32:08 · Speaker 1

log of

### 00:32:10 · Speaker 1

X by

### 00:32:12 · Speaker 1

Cubics

### 00:32:14 · Speaker 1

ಓಕೆ

### 00:32:16 · Speaker 1

Fine. So now let's try to do it for

### 00:32:20 · Speaker 1

the discrete case. Okay. Let's let's prove for

### 00:32:28 · Speaker 1

let's prove for

### 00:32:31 · Speaker 1

discrete case

### 00:32:36 · Speaker 1

So when I mean discrete, what do I mean by discrete?

### 00:32:41 · Speaker 1

in this case.

### 00:32:47 · Speaker 1

the random variable is discrete

### 00:32:50 · Speaker 3

random variable is discrete. Okay. Now please remember that both of them share the same sample space.

### 00:32:57 · Speaker 3

Okay. It is not like they have different sample space.

### 00:33:02 · Speaker 3

If they have different sample space, you cannot even think of doing anything.

### 00:33:06 · Speaker 3

Okay. So now what do we want to prove? We want to prove d k l is always greater than or equal to

### 00:33:10 · Speaker 1

equal to zero. Okay. So now

### 00:33:16 · Speaker 1

need to prove

### 00:33:21 · Speaker 1

PKL of

### 00:33:24 · Speaker 1

P Q

### 00:33:25 · Speaker 1

is always greater than or equal to zero.

### 00:33:29 · Speaker 1

ओके। सो नाउ बिकॉज़ ऑफ विच आई कैन राइट दैट

### 00:33:35 · Speaker 1

minus d k l of

### 00:33:38 · Speaker 1

p q less than or equal to zero

### 00:33:45 · Speaker 1

Now minus TKL of

### 00:33:50 · Speaker 1

P Q

### 00:33:52 · Speaker 1

by definition this is

### 00:33:54 · Speaker 1

minus

### 00:33:55 · Speaker 1

summation of x

### 00:33:56 · Speaker 1

S

### 00:33:58 · Speaker 1

p of x

### 00:34:00 · Speaker 1

log px by qx

### 00:34:07 · Speaker 1

Now this is same as

### 00:34:09 · Speaker 1

summation over X

### 00:34:12 · Speaker 1

PX

### 00:34:14 · Speaker 1

log

### 00:34:16 · Speaker 1

Q X Y

### 00:34:18 · Speaker 1

next

### 00:34:20 · Speaker 1

So far so good

### 00:34:27 · Speaker 1

ಓಕೆ

### 00:34:29 · Speaker 1

So now

### 00:34:38 · Speaker 1

We know that

### 00:34:43 · Speaker 1

log is a

### 00:34:47 · Speaker 1

log is a concave function. What is a concave function?

### 00:34:53 · Speaker 1

How does the log x graph look like?

### 00:35:18 · Speaker 1

Is this a concave function?

### 00:35:25 · Speaker 3

Yes sir

### 00:35:28 · Speaker 1

Okay, what is a convex function then?

### 00:35:31 · Speaker 1

now

### 00:35:36 · Speaker 1

How to how to get the convex function from log x now? Do you know any ways of doing getting it?

### 00:35:43 · Speaker 5

minus

### 00:35:45 · Speaker 1

okay? some good idea. let me put that. minus

### 00:35:53 · Speaker 1

log x

### 00:35:56 · Speaker 1

Is this a convex function?

### 00:36:02 · Speaker 1

How do you know that it is a convex function?

### 00:36:08 · Speaker 5

I think if you take any two points then they are always above the curve.

### 00:36:14 · Speaker 5

I mean the line segment joining the two points is always above the column.

### 00:36:16 · Speaker 3

The idea is called as epigraph. Okay, that is the next idea that we will be discussing in the next tutorials. Okay, the idea is called as epigraph. We will come to that specific point in the next session that that's rightly correct. Okay. Now log is a concave function.

### 00:36:36 · Speaker 3

And then I invoke something that I haven't proved yet, we'll be proving it explicitly.

### 00:36:42 · Speaker 3

and

### 00:36:44 · Speaker 3

by, there is something called as Jensen's inequality.

### 00:36:50 · Speaker 3

There are so many of these inequalities, no? They are very much, what do you call, always there is something called

### 00:36:59 · Speaker 1

Jensen's inequality

### 00:37:08 · Speaker 1

Have you heard of any other inequality?

### 00:37:12 · Speaker 3

not the inequality in the society

### 00:37:15 · Speaker 3

But in mathematics, have you heard of any other inequality?

### 00:37:18 · Speaker 1

Triangular Inequality

### 00:37:20 · Speaker 3

triangular inequality apart from that. In probability do you hear anything?

### 00:37:31 · Speaker 3

there is something called as Chernoff bounds. Okay. there is idea called as Markov inequalities. So these things will come. They are very wonderful inequality to get the bounds. Okay. Now we will be discussing them in time.

### 00:37:45 · Speaker 3

Now the Jensen's inequality basically says, log of expectation of x is always less than

### 00:37:52 · Speaker 1

expectation of log x

### 00:37:57 · Speaker 1

ಓಕೆ

### 00:38:10 · Speaker 1

Now

### 00:38:11 · Speaker 1

What is this?

### 00:38:15 · Speaker 1

is this expectation of log x

### 00:38:19 · Speaker 1

is that look like this form

### 00:38:22 · Speaker 3

Yes

### 00:38:24 · Speaker 1

Yes

### 00:38:41 · Speaker 1

Now this is

### 00:38:53 · Speaker 1

maybe I did some some mistakes

### 00:38:57 · Speaker 3

where

### 00:39:01 · Speaker 1

there is a negative symbol so it should be okay okay okay got it yeah

### 00:39:25 · Speaker 1

with me?

### 00:39:29 · Speaker 1

Why did I take this symbol?

### 00:39:38 · Speaker 1

okay? There is a negative symbol here. Now because of which I have taken the other other inequality. Now because of

### 00:39:45 · Speaker 3

of which I can cancel off this and this

### 00:39:51 · Speaker 3

log of

### 00:39:54 · Speaker 2

and then I have a query here. We said

### 00:39:56 · Speaker 3

Gold

### 00:39:57 · Speaker 2

Yeah, we said E log X is less than or equal to log E X, right? So in the previous example it is not E log X, right? I mean expectation is P X. If it was P X, you have fixed log X.

### 00:40:12 · Speaker 3

No, this is, this is E log X.

### 00:40:16 · Speaker 3

Okay, now this is expectation of log x.

### 00:40:20 · Speaker 3

Now how do you get expectation of log x?

### 00:40:24 · Speaker 2

summation of x into log x, right? That's what expectation of log x is, right?

### 00:40:33 · Speaker 3

For whom did you leave the density function for me?

### 00:40:36 · Speaker 2

Okay

### 00:40:40 · Speaker 2

Yeah.

### 00:40:42 · Speaker 3

ओके, हैप्पन्स, डोंट वरी फॉर ऑल दीज़ थिंग्स, वी ऑल ऑफ अस विल डू दीज़ काइंड्स ऑफ मिस्टेक्स।

### 00:40:50 · Speaker 3

Okay. Yeah.

### 00:40:51 · Speaker 1

then

### 00:40:51 · Speaker 2

Thank you

### 00:40:53 · Speaker 3

Okay, so now what is this now?

### 00:40:54 · Speaker 1

Okay

### 00:41:02 · Speaker 1

What is Q?

### 00:41:12 · Speaker 1

or to be even more specific we are considering a discrete case. In discrete case what is Q?

### 00:41:20 · Speaker 1

EMF

### 00:41:22 · Speaker 3

Yeah. Now this is summation over all the x. What will be this?

### 00:41:27 · Speaker 1

वन

### 00:41:29 · Speaker 1

this is

### 00:41:42 · Speaker 1

This should be one

### 00:41:45 · Speaker 1

log one is zero

### 00:41:48 · Speaker 3

log one is zero, correct?

### 00:41:53 · Speaker 3

See, okay, let me let this not confuse you. When I say again and again here, I'm just carry forwarding this. I'm not saying that this quantity is less than this quantity. That is not what I mean. So if you are confusing with that, you can always write this.

### 00:42:10 · Speaker 1

Okay

### 00:42:13 · Speaker 1

and I'm reusing the same inequality.

### 00:42:20 · Speaker 1

because of which what I can say

### 00:42:25 · Speaker 1

PKL of

### 00:42:28 · Speaker 1

is always greater than zero

### 00:42:32 · Speaker 1

Hence the proof

### 00:42:36 · Speaker 1

Makes sense?

### 00:42:50 · Speaker 1

Okay. uh I have seen one mistake

### 00:42:56 · Speaker 1

if px is a density function, can you define it clearly for me?

### 00:43:09 · Speaker 1

probability that x equal to x

### 00:43:11 · Speaker 3

correct. So, so see, when you say f of x, now you say that this is from

### 00:43:19 · Speaker 3

R two zero one right

### 00:43:26 · Speaker 3

Yeah

### 00:43:27 · Speaker 1

What is CX?

### 00:43:36 · Speaker 1

This is R to R

### 00:43:39 · Speaker 1

But if on the other term

### 00:43:44 · Speaker 1

if x is a discrete random variable, so then it is from

### 00:43:49 · Speaker 1

Alto 01

### 00:43:59 · Speaker 1

Okay

### 00:44:02 · Speaker 1

see the difference. That is the reason why your density is not a probability

### 00:44:06 · Speaker 3

multi measure

### 00:44:09 · Speaker 3

This is not something that is coming out of because of this. If something has to be a probability measure, the outcome has to be between zero and one, right? And everything has to be positive. Now it takes real values.

### 00:44:25 · Speaker 1

Okay

### 00:44:27 · Speaker 1

Makes sense now?

### 00:44:36 · Speaker 1

Okay

### 00:44:38 · Speaker 1

Yeah, so

### 00:44:42 · Speaker 1

I thought I'll be

### 00:44:43 · Speaker 3

Starting with Jensen's inequality today

### 00:44:46 · Speaker 3

Yeah, we don't have much time. Yeah, any questions we will stop for the day.

### 00:44:55 · Speaker 5

Chandan in the mid sem there was one question that whether D K L is symmetric or not. And if it is not symmetric what are the consequences of it so shall we cover this now or in the mid sem review?

### 00:45:06 · Speaker 3

So I'll what I'll do is I'll write the answers for everything. See, to be very frank, I haven't seen the mid sem questions at all. Let me be very frank.

### 00:45:15 · Speaker 3

Okay. Now I'm a very what do you call this that that this will be there no so I I haven't seen I should start even so we should come up with answer script. Now what I'll do is I'll come up with an key solutions and then I'll put it out and then in the next tutorials that is next Wednesday if you have got any questions we'll surely take it up okay.

### 00:45:39 · Speaker 5

Yeah, that's fine.

### 00:45:40 · Speaker 3

sorry, I I so if sir has told me I would have looked into it even it did not come to me also, sorry for that.

### 00:45:50 · Speaker 3

we will look it up in the next

### 00:45:52 · Speaker 1

session.

### 00:46:03 · Speaker 0

one more question

### 00:46:05 · Speaker 3

Yeah

### 00:46:05 · Speaker 1

Yeah

### 00:46:06 · Speaker 3

Hello

### 00:46:06 · Speaker 1

Go ahead

### 00:46:06 · Speaker 3

I

### 00:46:06 · Speaker 0

So this probability density function, right? So

### 00:46:11 · Speaker 3

Hmm

### 00:46:12 · Speaker 0

that's a function from R to R you have mentioned. It's basically the uh if you differentiate the CDF you get the probability density function, right?

### 00:46:23 · Speaker 3

correct. If if x is a continuous random variable.

### 00:46:23 · Speaker 0

Correct

### 00:46:24 · Speaker 0

continuous random variable. If x is a continuous random variable. So, that can be looked at as a likelihood of the value taking x, right? x taking the value x.

### 00:46:28 · Speaker 3

Hmm

### 00:46:38 · Speaker 0

the

### 00:46:39 · Speaker 3

Why are you looking like this? Okay, fine, then.

### 00:46:43 · Speaker 0

uh would it go beyond zero and one in in so basically my question was like yeah would that uh value of px the density function go beyond zero and one. Yes yes yes that is what I said. Yes yes yes. Can you give an example that.

### 00:46:53 · Speaker 3

and

### 00:46:54 · Speaker 3

Yes yes yes that is what I said

### 00:46:56 · Speaker 3

Yes, yes, yes.

### 00:46:59 · Speaker 3

take Gaussian distribution.

### 00:47:01 · Speaker 0

hmm

### 00:47:03 · Speaker 0

Okay

### 00:47:04 · Speaker 3

take any Gaussian, how is the density of the Gaussian distribution is?

### 00:47:06 · Speaker 0

of

### 00:47:10 · Speaker 0

Yeah, this is the density of the

### 00:47:10 · Speaker 3

is the density of the Gaussian distribution

### 00:47:12 · Speaker 0

Hmm

### 00:47:14 · Speaker 3

Okay, now. So if you make it sharper or larger, no, it will exceed zero one. You can do it easily. Yeah, yeah.

### 00:47:16 · Speaker 0

Thanks

### 00:47:22 · Speaker 0

Yeah, yeah, yeah. I, yeah. So for example, even if you take a uniform distribution between zero and half,

### 00:47:27 · Speaker 3

and half

### 00:47:28 · Speaker 0

And that can have a value two, right? At any point between zero and okay.

### 00:47:28 · Speaker 3

and that can have a value two, right? at any point between zero and okay. It is two.

### 00:47:36 · Speaker 1

Okay, got it. Yeah.

### 00:47:37 · Speaker 3

Yeah

### 00:47:38 · Speaker 1

Thanks

### 00:47:45 · Speaker 5

But it is not defined for a particular point, right? It has to be always, uh I mean the density function, is it defined for any given point?

### 00:47:49 · Speaker 3

Always

### 00:47:55 · Speaker 5

We have to always take an interval, right?

### 00:48:00 · Speaker 5

So we can we cannot evaluate PDF at a particular point, right?

### 00:48:01 · Speaker 3

We cannot evaluate

### 00:48:05 · Speaker 3

No no no no no, what his question is correct, your point is correct, what his question basically is

### 00:48:12 · Speaker 3

at any given point what will be the value you are correct. It will be zero at a single point correct. But at any given interval also it can take more than zero one is my point.

### 00:48:30 · Speaker 5

I think the question is like, I mean how does it relate to the likelihood?

### 00:48:31 · Speaker 3

Okay

### 00:48:36 · Speaker 3

Now see, okay, don't don't bring in likelihood at all.

### 00:48:40 · Speaker 3

ओके। सो नो, इट इज मच मोर सिंपलर, नो, विदाउट लुकिंग इनटू लाइक्लीहुड एंड देन सी इट ऐज़ एन आर टू आर फंक्शन।

### 00:48:52 · Speaker 3

Okay, now that will be even more simpler. Okay, and it is much more simpler and say that this is not a probability function. It is not probability. Your mass is a probability, your distribution function is a probability. But your density

### 00:48:53 · Speaker 1

even more simpler

### 00:49:08 · Speaker 1

is not probability. Okay?

### 00:49:42 · Speaker 1

Okay

### 00:49:45 · Speaker 1

No questions? No further questions?

### 00:49:54 · Speaker 1

Okay then. So, uh, meanwhile

### 00:49:58 · Speaker 3

maybe today or tomorrow at tomorrow or day after at max I'll be putting the solutions for your quiz sorry for your test one online. so you can look at it and then we will discuss any queries so in the next tutorial session. okay and then we will continue with

### 00:50:21 · Speaker 3

proving of this, what do you call, Jensen's inequality and then we will continue with the discussion.

### 00:50:27 · Speaker 1

that are remaining. Okay? Makes sense?

### 00:50:38 · Speaker 1

Okay then

### 00:50:40 · Speaker 1

So thank you

### 00:50:43 · Speaker 1

let's meet next week
