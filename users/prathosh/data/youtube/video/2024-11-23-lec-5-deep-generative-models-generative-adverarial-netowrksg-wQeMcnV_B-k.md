---
id: wQeMcnV_B-k
title: Lec 5 - Deep Generative Models Generative Adverarial NetowrksGANs
date: '2024-11-23'
url: https://www.youtube.com/watch?v=wQeMcnV_B-k
description: ''
author: prathoshap5226
duration: 01:34:45
model: saaras:v3
transcript: true
---

# Lec 5 - Deep Generative Models Generative Adverarial NetowrksGANs

## Transcript

### 00:00:05 · Speaker 5

Okay, what I was saying is what we will do is uh I will I will stop let's say after uh see after thirty minutes or so once I have gone through uh a major topic. Uh then we can have a question answering session. So if people have questions, what I would recommend you is that just write them down.

### 00:00:29 · Speaker 5

Okay, so whenever you have a question, just write write them down on a sheet of paper. And whenever I stop and ask for question, I mean, uh ask prompt you for questions, ask me then. Does that that does make sense? So that uh there is a gap, I mean there is a balance between uh the flow of the class and also the I mean I do encourage a lot of questions. I mean I'm happy that you people are asking good questions. But let us uh not have

### 00:00:59 · Speaker 5

multiple photon four in that correct. So that the clue is there. One thing and there was one of the there was a couple of other questions on

### 00:01:10 · Speaker 5

and some of you were asking whether this course is going to be a fully quote unquote mathematical or will there be some practical considerations issues that would be considered. uh I mean see the I would answer that is that uh there is no practice without theory without math. uh I mean having said that

### 00:01:33 · Speaker 5

Once we complete the mathematical nuances and other details, we would definitely go to go to the practical implementation because all your assignments will be coding assignments. So there will all be practice based assignments only, okay? And also in the class and tutorials, whenever needed, we will also talk of the practical implementations and the other things, okay?

### 00:02:00 · Speaker 5

Okay, uh, that's about it I suppose. Anything else that you want to just take other issues that you want to

### 00:02:08 · Speaker 3

discuss before we start the class.

### 00:02:11 · Speaker 6

we would like to share with you.

### 00:02:18 · Speaker 3

Hello, I am Rahul

### 00:02:19 · Speaker 2

Hello

### 00:02:20 · Speaker 2

Yeah, yeah, so

### 00:02:23 · Speaker 3

Yeah, anything.

### 00:02:23 · Speaker 5

you did you have a comment?

### 00:02:26 · Speaker 7

Are you able to hear me?

### 00:02:28 · Speaker 5

Yes, yes, I can hear you. Go.

### 00:02:30 · Speaker 7

Yes, just one suggestion if possible. You cover theory and then you give a problem example, right?

### 00:02:38 · Speaker 5

for theory and then I think what

### 00:02:41 · Speaker 7

problems. You explain a problem and give a solution to it, right?

### 00:02:47 · Speaker 5

problem I didn't solve

### 00:02:49 · Speaker 7

For example, example.

### 00:02:52 · Speaker 7

like you will cover a topic, theory of it, and then you give example for that, right?

### 00:02:52 · Speaker 5

you

### 00:02:55 · Speaker 5

of it

### 00:02:56 · Speaker 5

and then

### 00:02:58 · Speaker 5

these are not like these are these topics are not like your let's say class twelve maths where okay you learn you learn how to differentiate functions and then there are some example problems on differentiate functions it's not that. See now we are looking at adversarial optimizations or gyaans right. So by practice what I mean is for instance in today's class I will tell you how to train a gyaan practically right.

### 00:02:59 · Speaker 7

hotline

### 00:03:28 · Speaker 5

what is all the theory that we are looking at translate into practical implementation right so there are no numerics per se

### 00:03:38 · Speaker 5

Because it's as I said no it's not like a fundamental uh calculus or probability theory kind of course where you introduce a concept and there are many many problems to be solved it is not that way right. By practical stuff I mean the implementation stuff right how would you how would you take these ideas and implement those in practice.

### 00:04:00 · Speaker 5

Does it make sense?

### 00:04:03 · Speaker 7

Yeah, that's right.

### 00:04:04 · Speaker 5

Okay

### 00:04:06 · Speaker 5

Okay, anything else?

### 00:04:08 · Speaker 7

Yeah, one more doubt I have. This is about conjugate of convex function.

### 00:04:10 · Speaker 5

Shoot

### 00:04:14 · Speaker 5

Yes

### 00:04:16 · Speaker 7

If we draw a graph of a conjugate of a function, convex function, how will it look like? Will it be inverse of it or

### 00:04:22 · Speaker 5

Yeah, it'll, Yeah, it'll look something like this.

### 00:04:25 · Speaker 3

Same

### 00:04:27 · Speaker 7

Okay

### 00:04:30 · Speaker 3

Okay

### 00:04:32 · Speaker 2

Should we continue the class?

### 00:04:46 · Speaker 3

Yes sir

### 00:04:49 · Speaker 2

Let me

### 00:04:52 · Speaker 2

So I am trying my iPad

### 00:05:25 · Speaker 2

Yeah, also tell me whether this

### 00:05:27 · Speaker 5

ब्लैक बैकग्राउंड एंड वाइट फॉन्ट इज ओके विद यू ऑर शुड वी हैव टू

### 00:05:34 · Speaker 5

switch it to white pair and black

### 00:05:37 · Speaker 5

right

### 00:05:40 · Speaker 6

Ajay Singh sir.

### 00:05:42 · Speaker 5

is fine okay

### 00:05:45 · Speaker 5

Okay

### 00:05:45 · Speaker 1

सर, सर, इफ पॉसिबल जस्ट चेंज द कलर ऑफ पेन व्हेनेवर देयर इज अ हाईलाइटेड टॉपिक।

### 00:05:53 · Speaker 1

like note or anything.

### 00:05:54 · Speaker 5

loot

### 00:05:56 · Speaker 5

Ha, that I'm doing, right? I'm looking, doing that highlighted highlight thing. No, no, no, I mean

### 00:06:01 · Speaker 1

No, no, no, I mean, I mean when you are taking some new topic, something new, then just change the color so that we can mark it properly if possible, otherwise also fine.

### 00:06:13 · Speaker 5

uh but yeah so everything that I write is important that way. Yeah. So anyway so I'll I'll I'll take that into consideration. Uh and also there were some discussions on KL divergence and and all that in the group no I will like I thought once we cover these topics it will be clear. Uh or I'll I'll respond to that okay. Okay so let's start. So just quick quick recap uh before we go to the topic. of today's lecture. So we were looking at adversarial optimization, right? Or generative models via adversarial optimization.

### 00:06:55 · Speaker 5

So what is the context? The context is that we want uh to build a generative model which is that it takes uh an arbitrary random variable as input, in this case a Gaussian random variable and it generates uh

### 00:07:14 · Speaker 5

or it samples from an underlying unknown distribution. Right? So we represented that that function as g theta of z where z is an arbitrary random variable and x cap

### 00:07:27 · Speaker 2

S

### 00:07:27 · Speaker 2

correct. It's highlighted.

### 00:07:45 · Speaker 2

So this Apple Pencil is

### 00:07:47 · Speaker 5

always with my laptop whenever I want to write it it has it has zero percent charge I don't know why. Anyway. So there is this function g theta that would map an arbitrary random variable z to another random variable x cap.

### 00:08:04 · Speaker 5

Okay. Now what do we need? We need a situation where this x cap has a distribution that follows the distribution of

### 00:08:14 · Speaker 1

Data

### 00:08:16 · Speaker 5

Okay, which we have called P X. Why is that? If this P theta becomes close to P X, then we have we have achieved what we want because then if you take an arbiter and a variable Z and pass it through this function G theta, then you get samples from P X, which is the underlying distribution.

### 00:08:41 · Speaker 5

Okay

### 00:08:43 · Speaker 5

Now the question was how do you set the parameters of this neural network G theta such that P theta which is the distribution of the output of the neural network is close to P X which is the input of I mean which is the input unknown distribution. The solution for that is that what you do is estimate distributional divergence measure between P X and P theta that will become a function of theta and set the parameters of

### 00:09:13 · Speaker 5

this neural network theta such that this is minimized. So if you do this, then the resulting neural network G theta neural network that you get will be such that it will take an arbitrary random variable C as input and it will output X cap whose distribution happens to be

### 00:09:35 · Speaker 5

following VX

### 00:09:38 · Speaker 5

Now, if you recall the tutorial, how do we solve this optimization problem of minimizing some sort of a divergence measure or a loss function with respect to neural network? All of you know how to do that, correct? Now, this this theta star equal to R minus d theta px and p theta, this R this optimization problem is solved using back propagation.

### 00:10:03 · Speaker 5

Is it okay?

### 00:10:06 · Speaker 5

any questions on problem problem setting the

### 00:10:11 · Speaker 5

how the problem is set up. So you have

### 00:10:14 · Speaker 7

हिंदुस्तान परिसर

### 00:10:16 · Speaker 7

this X hat is the complete image, right?

### 00:10:19 · Speaker 5

exerted the complete invention

### 00:10:21 · Speaker 7

and it doesn't depend upon the random inputs we are giving.

### 00:10:25 · Speaker 5

It very much depends on the random input, right? Because it is G cheat of Z. Z is the input.

### 00:10:31 · Speaker 7

Yeah, but it depends on theta parameters, right?

### 00:10:34 · Speaker 5

It also depends on parameter parameters and it also depends on theta.

### 00:10:40 · Speaker 5

See look at the setting

### 00:10:40 · Speaker 7

not theta. Okay, when I say input it's Z which is a uniform sorry normal distribution on this diagram.

### 00:10:46 · Speaker 5

is a

### 00:10:49 · Speaker 5

It depends on C, it depends on theta, both of it.

### 00:10:53 · Speaker 7

But G is the random, right?

### 00:10:56 · Speaker 5

Z is random. Correct.

### 00:10:58 · Speaker 7

then it should not matter what we give, right? It's random, right?

### 00:11:01 · Speaker 5

Oh that way you are saying. Okay so what when you said that it does it does not depend I thought what x cap that you get uh does not matter what z that you get that's not what it is. So for a given z you will get a given x cap. But uh yeah but you can choose any input distribution on the arbitrary random variable. Yeah that is correct.

### 00:11:03 · Speaker 7

Okay so

### 00:11:24 · Speaker 7

सो, व्हाटएवर वी गिव ऐज़ ज़ी बिकॉज़ इट इज़ रैंडम, वी विल गेट द एक्स कैप, राइट?

### 00:11:31 · Speaker 5

post training. post training. If you train it such that this divergence is minimized then it is true. You will get an X cap from the distribution. Different Z will give you different X caps. So you remember I told you to look at that this person does not exist dot com last time right? Yeah yeah. So every time you get a different you you give a different Z as an input you get a different image generated.

### 00:11:37 · Speaker 7

Hmm

### 00:11:48 · Speaker 6

Yeah, yeah.

### 00:11:56 · Speaker 5

Okay. But uh you have to like you should not change the distribution of Z for instance. Suppose while training you have sampled Z from uniform random variable. You should not start sampling from normal random variable when when you are doing inference or generation. That is not what should do what what you should do.

### 00:12:17 · Speaker 7

Okay, so yeah, does it mean that if X-ray is a human face,

### 00:12:17 · Speaker 5

okay

### 00:12:22 · Speaker 5

Hmm

### 00:12:22 · Speaker 7

different Z will give different human faces.

### 00:12:25 · Speaker 5

Correct. Correct. Post training different Z's will give you different human faces. Correct.

### 00:12:31 · Speaker 7

Okay

### 00:12:33 · Speaker 7

thank you

### 00:12:34 · Speaker 5

Okay

### 00:12:36 · Speaker 5

Right. So now any other question on this?

### 00:12:39 · Speaker 1

one quick question

### 00:12:40 · Speaker 5

Hmm

### 00:12:40 · Speaker 1

द आउटपुट इज़ गोना बी ह्यूमन फेसेस एंड ह्यूमन फेसेस ओनली मतलब मिक्सचर्स ऑफ़ ह्यूमन फेसेस और इट कैन बी लाइक

### 00:12:43 · Speaker 5

and

### 00:12:49 · Speaker 1

you can have human faces with different features, let's say three eyes or four eyes.

### 00:12:54 · Speaker 5

Okay. That depends on how good your training has been. It that can happen. See, how does that translate to mathematically is that if you have made this divergence metric between P X and P theta really low, then you will only get images from human faces because P X, the data that you have been given, only have like images from the distribution of human faces.

### 00:13:21 · Speaker 3

hmm

### 00:13:22 · Speaker 5

That's why you should train it well. If you have not trained it well in such a way that the this divergence measure has not gone to arbitrary low values, then you will have all these kinds of artifacts.

### 00:13:34 · Speaker 5

So you will see that in your assignment. So in your assignment I will actually ask you to train these neural networks. If you have not trained them well then the output will not be good.

### 00:13:45 · Speaker 2

can't

### 00:13:46 · Speaker 3

So

### 00:13:49 · Speaker 3

Pest

### 00:13:51 · Speaker 3

one other question. Faradwaj

### 00:13:56 · Speaker 4

Hello sir, good morning. uh Just something I was wondering sir, like I was looking at the talk as well that the Afghan authors gave on YouTube. Sir, it was not very clear to me like did they think of

### 00:14:05 · Speaker 5

Beauty

### 00:14:06 · Speaker 5

Hmm

### 00:14:11 · Speaker 5

of this adversarial approach first and then justified it or proved it with maths or the maths led to the discovery like what came first like the

### 00:14:19 · Speaker 4

take the

### 00:14:19 · Speaker 5

The intuitive

### 00:14:20 · Speaker 4

understanding or the mathematical foundation behind it?

### 00:14:23 · Speaker 5

safe

### 00:14:25 · Speaker 5

Okay

### 00:14:27 · Speaker 5

uh yeah so that's a general question. See I've been in this uh in this business of research for a decade now. I can tell you for sure that all of my uh papers uh the work that I have done it's always that we do some empirical experiment based on some hunch. uh it works. Whenever it works we back fit the math. Because my uh my firm belief is that if there is something that is working, then there should always be good maths behind it or good

### 00:15:02 · Speaker 5

systematic understanding behind it. But the way this is how I do it. I don't know how others do it. In fact chronologically speaking, you know, as our home minister said, you know, chronological sum. So if you look at the if you look at the chronology, Gyan paper came in twenty fourteen, okay, which only has empirical experiments. Okay, but this F Gyan which is a much more uh foundational

### 00:15:32 · Speaker 5

understanding of what was happening came two years afterwards. So that way, uh empirical stuff came first and then math came later. But my, I mean, this is how things happen, right? Mostly in engineering research. However, while you understand, to me, always principle understanding is something that I would like.

### 00:15:56 · Speaker 5

Right, I mean if you just tell me give me an algorithm and say that oh there is a discriminator, there is a generator, okay there is these two networks competing with each other etcetera, I will not be convinced because I don't know why it is working, what is actually happening and so on. So that is why when I teach, I always teach math first from a math first approach because that is more grounded and principled. Now once we once I you know put down that mathematical foundation, I would connect it to the empirical stuff which I do. this today's class. Okay. Yeah, but I mean to long I mean to long story short.

### 00:16:35 · Speaker 5

In engineering mostly the empirical science precedes math. But there have been a lot of cases where you come up with mathematical ideas and then translate it to empirical stuff as well. Both happens.

### 00:16:52 · Speaker 3

Got it sir, thank you

### 00:16:53 · Speaker 5

Okay, so, uh now the thing is given data and and samples from P theta. So now again, okay. So now what is the core question here that uh you again I'm emphasizing this multiple times because it has to just go into your

### 00:17:10 · Speaker 5

the mind. So basically the question that we have is we have this setup and we want to minimize this distributional divergence measures between PX and P theta. Okay. Now what do we have? What we have as in at our hand are samples from PX which we call as data, okay? That is what data is. And we also have samples from P theta. What are samples from P theta? They are simply the outputs of neural networks. How do we get multiple samples from P theta as somebody

### 00:17:40 · Speaker 5

was saying you sample or you get you get multiple samples from the Gaussian random variable. How do you get samples from Gaussian random variable? You have this rand n function.

### 00:17:53 · Speaker 5

right in in all pseudo random number generators right you get uh the random numbers generated from random function and give it as an input to g theta okay that is how you get multiple samples from p theta so now you have samples from d you have samples from p theta the question now is how do you compute the distribution and divergence uh d theta so that we can use that as a loss function and back propagate through this neural network to minimize that that is what we need to do

### 00:18:23 · Speaker 5

if we take this which if we take P theta and P X and compute the distributional divergence and minimize the distributional divergence and try the neural network using that this neural network G theta will start generating samples from P X that is the idea

### 00:18:39 · Speaker 5

Correct? Yeah. So what is the big deal about it is that remember that the biggest problem in in all of generative modeling or all of machine learning is that you

### 00:18:53 · Speaker 5

do not know the distributions, okay? uh between which you are computing the divergence, you only have samples from it. So you don't know what the form of P X and P theta is, but you only have samples from P X and P theta.

### 00:19:08 · Speaker 5

Yeah, that I have written that already, right? So how do we have samples from P X? It is the given data. How do we have samples from P theta? It is simply choose different Zs and pass them through G theta of C.

### 00:19:19 · Speaker 5

that would give you samples of P theta. Now having samples of P X and P theta, how do you compute the distributional divergence is the question. Okay?

### 00:19:29 · Speaker 5

Okay. Now, before going to compute distributional divergence, I defined a large family of divergence matrix, which we called as the F divergence, of which the KL divergence is also a member. KL divergence, the forward KL, reverse KL, Jensen channel divergence, all of them are members of this family. We defined F divergence as this particular integral and

### 00:19:59 · Speaker 5

this F is a convex function, okay? So you plug in a convex function, you get a different divergence metric, okay? That is what we saw.

### 00:20:09 · Speaker 5

ओके. नाउ कमिंग बैक टू आवर गोल, आवर गोल वाज़ टू कंप्यूट द एफ डाइवर्जेंस बिटवीन पीएक्स एंड पी डेटा यूजिंग देयर सैंपल्स विदाउट नोइंग द अंडरलाइंग डिस्ट्रीब्यूशन्स.

### 00:20:19 · Speaker 5

Okay. So we saw that there is a way to do it. Uh the way to do it is that if you have uh an integral, okay, with respect to a density function to be computed, you can approximate that using uh what is called as sample means, okay? Now, this result which we called as

### 00:20:40 · Speaker 5

law of large and inverse this one

### 00:20:45 · Speaker 2

simply say that

### 00:20:49 · Speaker 2

integrals can be computed

### 00:20:58 · Speaker 2

without okay or rather with only the samples.

### 00:21:13 · Speaker 2

Correct? So that is

### 00:21:15 · Speaker 5

of large numbers if you simply have samples from distribution and if you are looking at integrals of functions with respect to density functions without having so please look at this equation this is

### 00:21:26 · Speaker 2

pretty important so this one

### 00:21:43 · Speaker 2

Okay. So this is this is actually

### 00:21:45 · Speaker 5

one of the key equations that we will be using multiple times in this course that uh if you want to compute an integral of a function h of x with respect to some density function p of x I mean which is also called the expectation of h of x with respect to p of x you simply take the sample averages of the h of x h of x computed at all x i's where x i's are coming from p of x so in this case it is data right you can compute the certain

### 00:22:15 · Speaker 5

integrals uh using sample estimates. This is a known result. Okay. Now how do we use that? If the divergence metric that we are trying to minimize, if we can express if we can express that in terms of expectations over P X and P theta, then this divergence metric can be computed using sample estimates from P X and P theta via law of large numbers. Right? Because we know that

### 00:22:40 · Speaker 5

we can compute expectations using samples with this result called half-loss numbers. Then if we can represent our DF in somehow via expectations over PX and P theta, then we can compute the F divergence simply using the samples, correct? So now with that goal, we now wanted to express DF in terms of expectations over PX and P theta. Okay. Now, with this goal, we saw that we cannot represent

### 00:23:10 · Speaker 5

different this F divergence exactly using the exactly expectations over these two but what we can do is we can express the lower bounds on DF in terms of expectations. Now instead of minimizing the F divergence we minimize the lower bound on it that is the idea. One can ask no okay and we set our goal as finding out the G theta such that the the F divergence

### 00:23:40 · Speaker 5

sorry, f divergence is minimized. Now instead of minimizing f divergence, you are minimizing a lower bound on it. I mean, is it is it correct? Now that's not that's not exactly correct because if you can minimize the divergence itself and it is great, but the problem is f divergence cannot be minimized exactly, uh without having the distributions px and p theta. Now because we don't have distributions px and p theta but only have samples from it. वी टू इस वी इंस्टेड सॉल्व एन एप्रोक्सीमेट प्रॉब्लम व्हिच इज मिनिमाइजिंग द लोअर बॉन्ड ऑन एंटियर वर्जंस।

### 00:24:17 · Speaker 5

Right. So now what we should do is an issue we should bound f divergence and express in terms of expectations over p x and p theta. For that we did some uh some algebra we took the convex conjugate of of the f function in the f divergence and we did some manipulations and finally what happened is that we got

### 00:24:42 · Speaker 5

we got this result where we expressed uh f theta okay df the f divergence as as I mean we we carved a lower bound on the f divergence via this expectation so what is this that is uh the lower bound that we obtain will become a function of this another class of functions called dx right now what we what we are saying is that there is some terminology here which is expectation of some function

### 00:25:15 · Speaker 5

of some other function f star of t x as x cap is coming from p theta. Right? So we know how to compute both of these expectations. Why? I mean if we know what t function is, then this expectation can be computed using law of large numbers, right? Where you can approximate this using sample averages. I will write down all that and show you how to do it in practice. Okay? So now basically what we did was, yeah, we have expressed the lower bound on the f divergence in terms of expectations over unknown distributions.

### 00:25:45 · Speaker 5

Now the lower bound that we computed on f divergence, okay, is itself involves an optimization, that itself involves an optimization problem over a class of functions T X. Now what I mean to say is that if you give one particular T X, you will get one lower bound on f divergence.

### 00:26:07 · Speaker 5

that is

### 00:26:08 · Speaker 3

that you should note, maybe I'll

### 00:26:11 · Speaker 3

up to that as a note here

### 00:26:16 · Speaker 3

Okay, this is two

### 00:26:19 · Speaker 3

too much red. This was okay.

### 00:26:23 · Speaker 2

lower bound

### 00:26:29 · Speaker 2

on F divergence

### 00:26:34 · Speaker 2

involves

### 00:26:37 · Speaker 2

solving

### 00:26:40 · Speaker 2

an optimization problem

### 00:26:50 · Speaker 2

or some function classes denoted by T of X.

### 00:26:58 · Speaker 2

Yeah, this is the moral of the story.

### 00:27:06 · Speaker 5

See that okay. Is that now we constructed lower bound on the f divergence or the loss function that you would want to minimize. And we express that in terms of expectations over p x and expectations over p theta.

### 00:27:22 · Speaker 5

And the lower bound itself contains an optimization problem that is to be solved over another set of functions, class of functions that we denote it as T X.

### 00:27:33 · Speaker 5

Okay, so let me stop here for a couple of minutes and ask questions. Please ensure that all of you are totally with me on this, okay? Because whatever I do now will be building upon this. So, like ensure that you understand this perfectly and then we will move on. We'll spend some five minutes on this. And this is actually a key equation for Gyan. So once we do this, then actually it's all done.

### 00:28:00 · Speaker 5

Okay. There are a few questions. Aditya.

### 00:28:05 · Speaker 6

Uh sir, I think I there's a typo on the line just before this. If you could scroll just a little higher. Yeah, the close bracket I think should come just before d x in that line. f star of d x and then the close bracket because p of p theta of x should be multiplied with f star of, right?

### 00:28:25 · Speaker 5

Oh yeah. Correct. Thank you for noticing that.

### 00:28:29 · Speaker 3

Yes sir

### 00:28:31 · Speaker 2

of this here.

### 00:28:41 · Speaker 2

what is this?

### 00:28:45 · Speaker 2

some fancy thing. Okay.

### 00:28:49 · Speaker 2

Hello

### 00:28:52 · Speaker 2

Hello

### 00:28:57 · Speaker 2

And this is for school girls and kids, okay, they have made some

### 00:29:12 · Speaker 2

Okay, thanks. Lokesh.

### 00:29:15 · Speaker 3

Sir, can you please explain how this greater than sign came once again?

### 00:29:21 · Speaker 2

Oh

### 00:29:21 · Speaker 3

like DTF is greater than

### 00:29:25 · Speaker 3

I see

### 00:29:32 · Speaker 3

That's the content of last class

### 00:29:36 · Speaker 5

So if you have to trace back the entire derivation

### 00:29:43 · Speaker 5

at the test

### 00:29:43 · Speaker 6

just the last step after T X after T star of X you understood

### 00:29:46 · Speaker 5

where where where where

### 00:29:50 · Speaker 5

See you understood you understood why there is this why instead of having small t why capital T came right because you are solving an optimization problem internally correct?

### 00:30:02 · Speaker 3

Yeah yeah

### 00:30:03 · Speaker 5

if I pull that maximum maximization out, okay? So what this capital T or rather this T X that we have, right? Should be such that it will give you the solution for that optimization problem, internal optimization problem at all X, correct?

### 00:30:24 · Speaker 6

Yeah

### 00:30:25 · Speaker 5

Now suppose there is some T X with capital T of X which is a function that would not give you the solution for optimization problem for all X.

### 00:30:37 · Speaker 1

Okay

### 00:30:39 · Speaker 5

In that case what happens? This entire integral that we compute right? Or the maximum value that we compute under that T X will not be will always be less than the case where you would have gotten the maximum at all at all X isn't it?

### 00:30:59 · Speaker 3

Okay

### 00:31:01 · Speaker 5

you get it?

### 00:31:02 · Speaker 5

See, instead of T star of X, which would give you the maximum value at all T, if you had another function T, that would not give you maximum at all points. If it does not give you maximum at all points, what does that mean? It is always less than the maximum, right? It can at most is equal to the maximum or it is less than the maximum.

### 00:31:25 · Speaker 6

Yeah, okay.

### 00:31:27 · Speaker 5

So basically what you are doing is you are searching for uh that function okay T of X which would give you the maximum value for that optimization problem at all T's sorry at all X.

### 00:31:43 · Speaker 5

ओके? यस। नाउ इफ यू गेट दैट फंक्शन, देन दिस इनइक्वलिटी विल बिकम इक्वलिटी।

### 00:31:43 · Speaker 3

Yes

### 00:31:50 · Speaker 5

If you get that function.

### 00:31:53 · Speaker 5

Okay. Now what is the script T? Script T you can see visualize the script T as a bucket of large classes of functions. So you are choosing from a bucket of family of functions.

### 00:32:09 · Speaker 5

Okay. Now if you in that bucket of functions that you are searching over, if you can get a function small t of x such that it is equal to t star of x for all x, then this becomes equality.

### 00:32:23 · Speaker 3

Yeah

### 00:32:24 · Speaker 5

Okay

### 00:32:24 · Speaker 3

Oxidizer

### 00:32:25 · Speaker 5

But if you cannot get that function, if you get another function t of x which is not equal to t star of x at even at one x, then it becomes inequality because at that x your t of x is less than t star of x.

### 00:32:39 · Speaker 5

called

### 00:32:41 · Speaker 3

Yes sir

### 00:32:42 · Speaker 5

I can write it

### 00:32:43 · Speaker 2

A B

### 00:32:46 · Speaker 2

Hmm

### 00:32:53 · Speaker 2

I'll write that here.

### 00:32:59 · Speaker 2

Inequality

### 00:33:04 · Speaker 2

Rights

### 00:33:08 · Speaker 2

because

### 00:33:13 · Speaker 2

T of X, right?

### 00:33:15 · Speaker 3

is

### 00:33:16 · Speaker 3

less than or equal to t star of x

### 00:33:20 · Speaker 3

for every x. That's all.

### 00:33:23 · Speaker 3

Okay? If

### 00:33:27 · Speaker 3

of x is equal to d of x star oh sorry

### 00:33:31 · Speaker 2

T star of H star

### 00:33:36 · Speaker 2

atomics. Okay? Then

### 00:33:42 · Speaker 2

Equality

### 00:33:48 · Speaker 5

Yeah, I think that's worth writing.

### 00:33:51 · Speaker 5

And uh see one other thing I'm almost ensuring that whatever I say you know whatever storyline that I build I'm writing all of it right one after the other right I mean I write this as goal questions and all that. So this notes right please go through it before you come to the next class every class go through this line by line step by step. Also you have the recordings watch the video and and come to the next class that will help you a lot. And of course we are available for questions for WhatsApp and Teams. Okay, Raghavendra Nayak.

### 00:34:28 · Speaker 6

Yes sir, in this case, this t of x, do we choose any function and then try to optimize it or we try to

### 00:34:33 · Speaker 5

try to. Good good question. uh See if you know how GANs work. Other than this network there is another network no which is called the discriminator network.

### 00:34:46 · Speaker 3

Yes

### 00:34:46 · Speaker 5

That is your T of X. The need for another network comes up because you have to choose from a bucket of functions and you optimize when you pick those bucket of functions, you approximate those functions using another neural network. We will we will see that.

### 00:35:00 · Speaker 6

Okay, okay. Yeah, thank you, sir.

### 00:35:05 · Speaker 2

ಓಕೆ ಎನಿ ಎದರ್ ಕ್ವೆಶ್ಚನ್

### 00:35:11 · Speaker 3

Okay

### 00:35:11 · Speaker 3

Please

### 00:35:11 · Speaker 2

Great

### 00:35:12 · Speaker 5

Hello

### 00:35:13 · Speaker 2

Yeah, Harish.

### 00:35:14 · Speaker 6

So, uh, so the stereoflex is also a convex function.

### 00:35:18 · Speaker 5

No no no no no no no. See this T has nothing to do with that F. See uh F divergence in uh the F function in F divergence no that are definition only that is convex. Nothing else is convex.

### 00:35:32 · Speaker 5

This f function is convex, that's all.

### 00:35:36 · Speaker 3

Okay

### 00:35:41 · Speaker 2

Should we move on?

### 00:35:47 · Speaker 2

Okay, let's get to

### 00:36:02 · Speaker 2

See on a lighter note,

### 00:36:04 · Speaker 5

person who put this feedback, you know, please don't take it badly. I mean, there's no, anyway, it's anonymous, but it was pretty funny. Sorry, I received a feedback where somebody said that, you know, I'm paying this much fees to I A C for this particular course. So I expect this, this is, right? So, I mean, one thing was it's very, very revealing for me that this course cost this much money. I didn't know that.

### 00:36:35 · Speaker 5

Apparently every credit here is what twenty thousand rupees no? I mean I I was thinking that all this is reimbursed for you from your respective companies.

### 00:36:46 · Speaker 5

Don't they? I think they would, no? I mean there is some learning program that's always there. You don't pay these fees from your pocket, do you? Just curious. I'm not asking that person who wrote, okay? I don't I don't want to I don't wish to know. But yeah, in general I'm asking out of curiosity. So not all of you like your companies don't pay that, huh?

### 00:36:53 · Speaker 3

I'm not

### 00:36:54 · Speaker 4

I have not asked

### 00:37:07 · Speaker 3

like your companies don't pay that? partially reinvested. partially reinvested.

### 00:37:10 · Speaker 6

Partially Rain was

### 00:37:12 · Speaker 5

Barcelona

### 00:37:14 · Speaker 5

power

### 00:37:15 · Speaker 4

It depends on the couple, I guess. It's full, I guess. It's fully different.

### 00:37:15 · Speaker 6

It depends on the couple

### 00:37:19 · Speaker 7

It was fully sponsored

### 00:37:19 · Speaker 6

Fully Sponsored

### 00:37:21 · Speaker 7

police

### 00:37:23 · Speaker 5

See, that makes me feel a little, little less guiltier, you see. Okay, so

### 00:37:29 · Speaker 6

That's not true for all sir

### 00:37:31 · Speaker 5

then I am guilty. Okay. No, you are not guilty. What was the

### 00:37:35 · Speaker 6

No, you are not

### 00:37:36 · Speaker 7

What was the requirement against the fees?

### 00:37:38 · Speaker 5

some demand right I mean like okay you have to teach more practical stuff you know I didn't pay the fees to look at math or whatever it doesn't matter. That's that's fair also I think. The demand was fair I mean I'm not I'm just joking right I mean this the way of putting it that okay I this is the amount of fees that I pay when it's sort of exorbitant. uh that's a lot of I didn't know that this course cost that much money okay. So but they said that okay paying this much money not to look

### 00:38:08 · Speaker 5

math or whatever. But then I thought okay, yeah, it's a lot of money. I hope, see if it's your company that is paying, I don't mind, no, they paid for all kinds of stuff. That's not big money for your company, but if you are paying it from your pocket, then it's it's it is, I mean it's all relative but still, yeah.

### 00:38:30 · Speaker 5

So one credit apparently cost twenty thousand rupees right in this thing which is considerable.

### 00:38:37 · Speaker 6

but this is one of the prime courses in the program so maybe he felt like that

### 00:38:46 · Speaker 5

How do you know that it's a he? I don't know. I don't know.

### 00:38:49 · Speaker 6

I don't know. Cheers.

### 00:38:53 · Speaker 5

Anyway, so this is the

### 00:38:54 · Speaker 6

So, so this is the course I am doing the M.Tech for.

### 00:38:58 · Speaker 5

people like that then yeah. Yeah. I mean I understand you know you to I mean don't get me wrong again that customers always have their right to question whatever the product that is being. See everybody now talks of customer obsession and all that right so customer is thinking that is the reason I put that feedback form already it is totally anonymous and whoever wrote that you know please don't get

### 00:38:58 · Speaker 6

people like that then yeah

### 00:39:26 · Speaker 5

friend that I'm just taking it lightly. So whatever you think is a fair demand put it out there and I'll be happy to incorporate as long as I can incorporate. Okay. Yeah okay.

### 00:39:39 · Speaker 4

सर, हाउ अबाउट द ऑफलाइन क्लासेस? स्टूडेंट आल्सो रजिस्टर फॉर दिस कोर्स एंड इलेक्टिव सब्जेक्ट्स और लेट्स से जेनेरिक वन लाइक थ्री फोर क्लासेस फॉर देम।

### 00:39:49 · Speaker 5

Come again, what is what is the question?

### 00:39:52 · Speaker 4

I mean how offline classes goes up? They need to register for this core courses? Or it's a scheduled for them like first year these classes next year.

### 00:40:02 · Speaker 5

No no no no no very similar to you. I mean there are core courses just like you have three four core courses right? They would I think have some six core courses. Rest of all are all this thing electives.

### 00:40:16 · Speaker 5

And by the way, I also teach this course, right, offline and I'm doing it in I I C right now. That class also has hundred plus people in I I C and trust me, that's in that's at least two three times more mathematical than this. Okay, I would I mean I I know that most of you people are not most, all of you are professionals and might have been a little out of touch from maths. There I do

### 00:40:44 · Speaker 5

much more maths than this. So this is not the upper bound of maths that one can do in this course. So please be rest assured on that. But anyway, if you have any anything that that you would like to see as a change in this course, let us know. That is why we have that feedback thing and we are happy to listen. Okay.

### 00:41:03 · Speaker 6

modes are in regular product development like this type of maths we are rarely using right?

### 00:41:11 · Speaker 5

I mean I'm I'm did I become judgmental? I mean I'm not complaining at all. I completely agree with you that you don't use that. But that is why you know I kind of

### 00:41:23 · Speaker 5

Yeah, so make it accessible. I try to make it as much accessible as possible but but see there is another way to teach this I'll tell you honestly. I can completely get rid of math and only teach it like what is done in Coursera, right or this Android kind of stuff where I'll just give you algorithms and tell you put some block diagrams and tell you how to do it. But honestly, right as an instructor, I don't see value in doing that.

### 00:41:49 · Speaker 5

See, whoever has done this course before, again, this is not self-bragging, have told that, you know, doing it this way, while difficult, while while it is difficult during the course time, right? But if you put in enough effort to understand and do assignments and tutorials and all that, they have been benefited from this. You know, this is what will actually differentiate you people from everybody and your grandmother who does machine learning. So everybody is a data scientist.

### 00:42:19 · Speaker 5

these days, right? What differentiates, I mean, somebody who knows well and somebody who does not is that you know some of the fundamentals and you can go more deeper into it. So I, there is value in doing maths. It's not that it's totally valueless. But I understand that it takes a little bit of more effort, but yeah, that is what I expect from you people to do. Having said that, you can let me know if all of you think that maths is completely valueless.

### 00:42:49 · Speaker 5

it's much easier for me to teach the algorithms and go sir away. We can do it but again that's not my recommendation though. Okay so let's continue so what we had was that we had this

### 00:43:04 · Speaker 5

carved lower bone on deuterium.

### 00:43:07 · Speaker 2

Okay, let's start from date given. So we are given data.

### 00:43:17 · Speaker 2

Sent

### 00:43:26 · Speaker 2

this is wrong

### 00:43:29 · Speaker 2

ID from PX. On from PX.

### 00:43:37 · Speaker 5

Okay

### 00:43:39 · Speaker 5

we have constructed an f divergence between okay before that we'll write what our p theta is. So we have this setup where

### 00:43:49 · Speaker 5

This is a neural network

### 00:43:53 · Speaker 5

And the way I represent neural networks, right? They

### 00:43:58 · Speaker 5

represent the dimensionality of the data. So this is a neural network whose

### 00:44:03 · Speaker 5

dimensionality keep increasing as you go deeper and deeper.

### 00:44:09 · Speaker 5

But did Chandan do back propagation for CNNs or was it only for multi MLPs?

### 00:44:18 · Speaker 4

MLP. MLPs.

### 00:44:19 · Speaker 5

only MLPs, okay.

### 00:44:22 · Speaker 5

Okay then you should look at back prop for C N Ns okay just as an exercise. When it's not completely needed but it's a good exercise to do. Okay G theta and whatever we get at the output is what we called as X theta and this has distribution P theta right. This Z was coming from normal distribution.

### 00:44:43 · Speaker 5

Now with this setup, we constructed a lower bound on the distributional divergence between P X and P theta, okay? This V Z was greater than equal to

### 00:44:58 · Speaker 5

this maximization over a class of function. So what does this mean? This actually means that you are searching over a class of functions script D and the thing that you have is you have an expectation here with respect to D of X as X comes from P X.

### 00:45:19 · Speaker 5

You have another expectation here with respect to F star of

### 00:45:26 · Speaker 3

p of x as

### 00:45:29 · Speaker 3

x cap here. As x cap comes from p theta.

### 00:45:35 · Speaker 3

Okay

### 00:45:35 · Speaker 5

what we have seen so far. Now the question is, uh so recall that we are interested in recall.

### 00:45:44 · Speaker 5

So

### 00:45:47 · Speaker 3

Interested in finding

### 00:45:48 · Speaker 5

out a theta star, okay? That is the minimizer.

### 00:45:54 · Speaker 5

of

### 00:45:56 · Speaker 5

the f divergence, right? This is what we wanted.

### 00:46:01 · Speaker 5

We could not do it because we didn't have access to P X and P theta. So we approximated that by the minimizers.

### 00:46:09 · Speaker 5

and this minimization is over three

### 00:46:11 · Speaker 2

up, okay? Minimize this, minimize the lower bound.

### 00:46:24 · Speaker 2

Okay? Now, which is

### 00:46:31 · Speaker 2

And by the way, all of you understand this notation argmin, right? Have I explained the notation argmin?

### 00:46:40 · Speaker 5

done it right I mean it is that set of theta which would minimize whatever is there within the function okay. min is the minimum value. argument is the minimizer okay the argument which minimizes. fine so you have to minimize over theta which is the lower bound.

### 00:46:57 · Speaker 5

No

### 00:46:57 · Speaker 3

lower bound

### 00:47:00 · Speaker 3

itself has a maximization over T

### 00:47:07 · Speaker 3

differences of this expectation I would not write it. expectation over px minus expectation of something with respect to p theta this is what it is right?

### 00:47:20 · Speaker 2

Okay? Now this will become

### 00:47:23 · Speaker 2

will become

### 00:47:33 · Speaker 2

Okay, maybe before that, let us do this.

### 00:47:38 · Speaker 3

Okay. Now this minimization, right? This the outer minimization is

### 00:47:46 · Speaker 3

min with respect to

### 00:47:50 · Speaker 3

is pay attention here. This is min with respect to

### 00:47:57 · Speaker 3

parameters

### 00:48:01 · Speaker 5

of a neural network, correct?

### 00:48:04 · Speaker 5

theta are parameters of a neural network and you need to minimize a function or a value with respect to parameters of a neural network. Do we know how to do that?

### 00:48:17 · Speaker 3

Propagation

### 00:48:17 · Speaker 6

back propagation

### 00:48:18 · Speaker 5

that is back propagation. So you can do this

### 00:48:20 · Speaker 2

back cloud

### 00:48:23 · Speaker 2

backprop four watt

### 00:48:26 · Speaker 2

Over the G Theta network

### 00:48:40 · Speaker 2

okay? That's what it is. Now this

### 00:48:44 · Speaker 2

is maximization

### 00:48:47 · Speaker 3

with respect to class of functions.

### 00:48:54 · Speaker 3

Do we know how to solve that? We don't.

### 00:48:58 · Speaker 3

तर वी डोंट नो हाउ टू

### 00:48:59 · Speaker 5

optimize. We know how to optimize over parameters of a neural network. We don't know how to optimize with respect to a class of function. So what you mean by optimization over parameters is that I mean we can we can do a gradient descent in the parameter space, the space of parameters of a neural network. But we can't do gradient descent in the space of a function, right? We don't know how to search over functions. We know how to search over parameters. How do we get rid of this problem is that so you translate

### 00:49:28 · Speaker 3

Clear Descent

### 00:49:30 · Speaker 3

Okay. Do that. At first light,

### 00:49:37 · Speaker 3

script T which are the family of functions that we are optimizing

### 00:49:40 · Speaker 2

Goor

### 00:49:42 · Speaker 2

via neural networks

### 00:49:55 · Speaker 2

Let's call them T W of X

### 00:49:58 · Speaker 3

care

### 00:50:01 · Speaker 3

W R the set of parameters, the set of

### 00:50:06 · Speaker 3

Weights

### 00:50:09 · Speaker 3

I used the word weights and parameters interchangeably. Weights or parameters.

### 00:50:15 · Speaker 3

of a neural network

### 00:50:23 · Speaker 3

Now with different W values, okay? You will get different functions T X, do you agree?

### 00:50:33 · Speaker 2

because it is represented using a neural network.

### 00:50:38 · Speaker 2

Hello

### 00:50:50 · Speaker 3

Sir, can I ask a question at this moment?

### 00:50:53 · Speaker 2

Okay, go on.

### 00:50:55 · Speaker 6

Sir, uh we are trying to represent uh the set functions using neural networks. I'm just trying to understand let's say we want to represent a cubic polynomial or a polynomial of nth order. Then in that case how will we represent it using neural networks?

### 00:51:02 · Speaker 5

um

### 00:51:10 · Speaker 5

Hmm

### 00:51:15 · Speaker 5

easy, right? So now this function, uh cubic polynomial, right? I mean, are you talking about a polynomial, a vector valued polynomial or a scalar valued polynomial?

### 00:51:26 · Speaker 5

like any

### 00:51:26 · Speaker 6

anything sir.

### 00:51:28 · Speaker 5

Yeah, if it's a scalar valued polynomial, then what do you need? So let's say that f of x is equal to ax cubed plus bx squared plus cx plus d, right?

### 00:51:39 · Speaker 5

Right? Yes. So you build a neural network that would take x as input and give you f of x as output. See that's what you do in all classification and everything, right?

### 00:51:39 · Speaker 6

Yes

### 00:51:51 · Speaker 6

No sir, like there, like if we consider a multi-layer perceptron,

### 00:51:51 · Speaker 5

नुसतं लाइक

### 00:51:56 · Speaker 5

Hello

### 00:51:56 · Speaker 4

So we have the weights. We have the bias, okay? And then eventually for each layer we have a non-linear activation.

### 00:51:58 · Speaker 5

We had

### 00:52:00 · Speaker 5

Okay

### 00:52:07 · Speaker 5

correct

### 00:52:08 · Speaker 4

Okay, so I'm trying to

### 00:52:09 · Speaker 6

understand there like how let's say I want to do x cube okay so that case how will I do that

### 00:52:14 · Speaker 5

Okay

### 00:52:17 · Speaker 5

You can, right? See, that is the regression problem. What you are saying is the classical regression problem.

### 00:52:22 · Speaker 3

Okay, so

### 00:52:29 · Speaker 2

Let's say that your f of x is equal to

### 00:52:40 · Speaker 3

Okay. uh So what you have is for different values of x you have f of x. So what you have is let's say x one comma f of x one.

### 00:52:53 · Speaker 3

x2, f

### 00:52:58 · Speaker 3

and so on. You have xn, f of xn. This is your data.

### 00:53:03 · Speaker 3

right? That is what you have. You should have this.

### 00:53:05 · Speaker 5

to represent this as a neural network.

### 00:53:08 · Speaker 3

Yes sir

### 00:53:08 · Speaker 5

So what I do is I will have an M L P

### 00:53:14 · Speaker 5

which would take x as input so it will take x i as input and it will predict f of x i as output

### 00:53:20 · Speaker 5

This is the predictor.

### 00:53:23 · Speaker 5

How do I train this neural network? This let's call this complex of theta. That's all. Theta star is equal to

### 00:53:26 · Speaker 3

pack

### 00:53:31 · Speaker 5

minimum of we have n samples here one by n one whole n I'll take f of f theta of f cap x i minus f of x i

### 00:53:47 · Speaker 5

That's all, no? This is classical neural network training. This is solving a regression problem.

### 00:53:54 · Speaker 6

Got it sir

### 00:53:56 · Speaker 5

This is how we are representing this polynomial function which is a neural network.

### 00:54:02 · Speaker 5

See that's what

### 00:54:02 · Speaker 6

comment

### 00:54:04 · Speaker 7

So the presence of non-linearity allows us to also model this non-linear functions, right?

### 00:54:09 · Speaker 5

Well, yeah, see, okay, that is some other neural networks.

### 00:54:17 · Speaker 3

the deep neural networks are universal function approximators. That is why they are powerful.

### 00:54:26 · Speaker 5

Okay. Now what does this mean? That means that by choosing uh the the weights and the biases and the non-linearity of an MLP which is deep enough, you can represent any function to arbitrary closeness that is a known result. That is why the go to architecture for

### 00:54:44 · Speaker 3

all machine learning these days are neural networks.

### 00:54:51 · Speaker 3

Is that fine?

### 00:54:55 · Speaker 3

Okay, so I think we will remove this.

### 00:54:58 · Speaker 2

So non percentile

### 00:54:59 · Speaker 3

Yeah

### 00:55:00 · Speaker 1

But here we like already know that function should be like T X right like T of X. So can you put some restriction on that so that it will No with T

### 00:55:07 · Speaker 5

No, with T, with T, where is, what do we know? We don't know. I don't, I understand. We don't know anything about T. What do we know about T? We know nothing about T.

### 00:55:08 · Speaker 6

result faster

### 00:55:11 · Speaker 6

What do we know?

### 00:55:23 · Speaker 5

See in the divergence case, T is simply a class of function. See what we know is that this T has to be such that it is a solution for this inner optimization problem for all X. But we don't know anything beyond that, no?

### 00:55:40 · Speaker 5

See we want the T to be such that it maximizes whatever there is there in the internal bracket that's all.

### 00:55:47 · Speaker 5

See just like we had that regression problem that I had written. So here you are only solving an optimization problem with respect to uh this T. So T is a neural network, okay? So I'll write that down.

### 00:55:59 · Speaker 1

but we know here like it should be the maximum value right? So at least that conditional things can be No no how

### 00:56:05 · Speaker 5

No no how see we want. See. We want. See this is an optimization problem that we are solving. Just okay I erased it. It is no different from the problem that I had just written so you had to minimize you had to find the theta such that it minimizes the

### 00:56:26 · Speaker 5

differences between norm of these two functions, right? That is what we had for the regression problem, isn't it?

### 00:56:32 · Speaker 0

Yeah

### 00:56:33 · Speaker 5

This is exactly the same. Instead of having the differences between the predictions, it has some other expectation, that's all.

### 00:56:42 · Speaker 5

You are trying to maximize, see maximization minimization are both, I can write this minimization as maximization with a minus here, correct?

### 00:56:51 · Speaker 1

Correct

### 00:56:52 · Speaker 5

Same thing that is we don't know anything we only know that this neural network has to maximize whatever is there inside. Okay. Now I will write that so now I mean I hope that all of you understood what I mean when I say that I will represent this T function via a neural network. Okay now what happens is we will write

### 00:56:59 · Speaker 1

Okay

### 00:57:10 · Speaker 2

So with this

### 00:57:16 · Speaker 2

So now we have

### 00:57:21 · Speaker 2

a G theta of C network okay that would take

### 00:57:24 · Speaker 3

to C and give you X cap

### 00:57:30 · Speaker 3

from P theta

### 00:57:31 · Speaker 2

okay? So maybe we'll, okay. So complete, so we can write. We have another network now, neural network.

### 00:57:44 · Speaker 2

which is T W of

### 00:57:48 · Speaker 2

x, it will take x.

### 00:57:50 · Speaker 5

it will give you the output T W of X

### 00:57:55 · Speaker 5

understand? Now there is a particular loss function which is Okay, let us write that as loss.

### 00:58:04 · Speaker 3

not loss, right? That's cost functions.

### 00:58:11 · Speaker 3

is equal to

### 00:58:14 · Speaker 3

expectation of

### 00:58:17 · Speaker 3

t of x as x is coming from p theta minus

### 00:58:22 · Speaker 3

the expectation of

### 00:58:25 · Speaker 3

f star of t of x

### 00:58:29 · Speaker 3

X cap is coming from

### 00:58:32 · Speaker 5

f x cap sorry coming from e theta. Now what happens is we need to find the optimal w for this t network such that

### 00:58:45 · Speaker 5

with my

### 00:58:46 · Speaker 3

maximizes this cost.

### 00:58:49 · Speaker 3

We agree

### 00:58:57 · Speaker 3

So if you agree let me just see what what is happening here look at this right. We have to find the T network or the T function such that this cost is maximized. Correct?

### 00:59:14 · Speaker 3

all of you with me on this.

### 00:59:18 · Speaker 3

Yes, okay

### 00:59:18 · Speaker 2

Okay

### 00:59:19 · Speaker 3

Now

### 00:59:19 · Speaker 5

we want to find theta, okay? such that it would minimize the same cost.

### 00:59:29 · Speaker 5

I'm sorry, I should write it as arg min and arg max, right? Because w star is not the minimum value of the function, it is the minimizer of the function. So, it is the arg max with respect to all possible w's and theta has to minimize the exact same cost.

### 00:59:50 · Speaker 6

Sir, is the first one is P of

### 00:59:52 · Speaker 3

P X right instead of P T T the cost formula

### 00:59:54 · Speaker 2

Correct

### 00:59:55 · Speaker 2

Correct, correct. Thanks.

### 01:00:02 · Speaker 3

is okay. So there is a cost function

### 01:00:04 · Speaker 5

okay? And there are two neural networks here. So one neural network has to uh maximize that cost. And the other neural network has to minimize that same cost. Now what is where is this coming from? You look at this right? Let me write that down. So now basically what is happening is so we have represented that T function. So first what happens is that you construct a lower bound on your F divergence by maximizing this. expectation over P X

### 01:00:39 · Speaker 5

minus expectation over P theta. So you maximize this with respect to W, you get a lower bound on on what? On F divergence.

### 01:00:51 · Speaker 2

Correct?

### 01:00:52 · Speaker 3

we completely write it so that it is

### 01:01:01 · Speaker 3

is an expectation over T of X. Okay?

### 01:01:04 · Speaker 5

T W of X now right? Because it is parameterized using another neural network now minus

### 01:01:11 · Speaker 5

is another expectation with respect to P theta. Now if star of

### 01:01:18 · Speaker 5

of X cam, T W of X cam. Now you optimize this with respect to W, you get a T function which is actually a neural network. Now that would create a lower bound on this thing, right? So I'm doing this.

### 01:01:35 · Speaker 2

creates

### 01:01:39 · Speaker 2

lower bound

### 01:01:43 · Speaker 2

on DF

### 01:01:45 · Speaker 5

Correct?

### 01:01:46 · Speaker 2

Hello

### 01:01:46 · Speaker 5

recall what was happening, right? So this lower bound is is created by maximizing this. Now if you choose one T, it will create one lower bound. Do you agree?

### 01:01:59 · Speaker 5

one particular T

### 01:02:00 · Speaker 3

function will create one particular lower bound, correct?

### 01:02:09 · Speaker 3

We also note that the lower bound that we have constructed right on D F for a particular

### 01:02:19 · Speaker 5

θ

### 01:02:23 · Speaker 5

What does that mean? See look at that this this this last function that we are calculating no is a function of theta. Why? X cap is a function of theta here.

### 01:02:35 · Speaker 5

Do you see that?

### 01:02:37 · Speaker 5

the x cap that we get, right, depends on theta. So it's a function of theta. The loss function is a function of theta. Do you agree?

### 01:02:49 · Speaker 5

So for a particular theta, okay, maximizing this thing will create one particular lower bound on D F. Correct?

### 01:03:02 · Speaker 5

Now, once you create a lower bound on the f divergence for a particular theta, you want to minimize that lower bound, okay, with respect to theta. Okay, I don't have space to write it here.

### 01:03:15 · Speaker 2

Yes

### 01:03:18 · Speaker 2

right right. here.

### 01:03:26 · Speaker 2

this minimization,

### 01:03:32 · Speaker 2

minimizes

### 01:03:37 · Speaker 2

any minus.

### 01:03:40 · Speaker 2

minimizes the lower mode

### 01:03:46 · Speaker 2

minimum is that lower bound

### 01:03:56 · Speaker 2

that lower bound, okay? Created

### 01:04:01 · Speaker 2

by T W in the previous step.

### 01:04:14 · Speaker 2

Do you understand what is happening? So first

### 01:04:17 · Speaker 5

you you have a t function, okay? that would create a lower bound.

### 01:04:22 · Speaker 5

at a particular theta. So you start with some random initialization for this d theta, okay? And then you train this TW network, okay? You create a lower bound. Now with that lower bound, you have to minimize that lower bound, right? Because ultimately the goal is to find the theta that would that is that makes p theta close to px. Now we are not minimizing the exact dip divergence, we are minimizing the lower bound. Once you create a lower bound with a particular TW, we note that

### 01:04:52 · Speaker 5

After you train this network once, okay, one T function is is fixed, created actually. So once you create a particular T function, then there is one lower bound that you have created.

### 01:05:05 · Speaker 5

ओके? एंड वन्स यू क्रिएट अ लोअर बाउंड, यू ट्राई दिस न्यूरॉ नेटवर्क टू फाइंड द थीटा दैट वुड मिनिमाइज दैट पर्टिकुलर लोअर बाउंड।

### 01:05:14 · Speaker 5

Okay. Now once you have minimized that lower bound, you can again come back to this T function and change the T function again which would create a new new lower bound for that new theta that you have learnt.

### 01:05:30 · Speaker 5

Do you see what I'm saying?

### 01:05:33 · Speaker 3

See the lower bound is created for a particular theta.

### 01:05:42 · Speaker 3

you understand? Given a theta, T will create one particular

### 01:05:47 · Speaker 5

lower bound. Now once a lower bound is created you can make it you can tweak your theta in such a way that your p theta gets close to p x. Okay? Now with that p theta changing your t function again will create another lower bound maybe it's tighter this time. Okay? Then with that lower bound you go back to theta and you keep alternating between these two optimizations.

### 01:06:16 · Speaker 5

Do you see, do you see the pictures what is happening?

### 01:06:21 · Speaker 5

So when you Gyan, right, you know that there are two networks, right? And by the way, this network is is what is famously referred to as

### 01:06:28 · Speaker 2

bus

### 01:06:31 · Speaker 2

the generator network

### 01:06:39 · Speaker 2

And this network is referred to as the discriminator or the critique network.

### 01:06:55 · Speaker 2

See in the next part of the class I will give you

### 01:06:57 · Speaker 5

to concrete examples for one F divergence which is the original Gann formulation and actually show the loss equations and back propagate and all that okay. But here I want you to understand the the the abstract picture that there are basically two functions you know why do you have this discriminator network this discriminator network is simply creating the lower bound on the F divergence and lower bound itself has a optimization problem that is to be solved right. Once you solve this inner optimization problem with respect to W

### 01:07:29 · Speaker 5

Okay. You get a lower bound and for a particular theta and you minimize that lower bound with respect to theta. Okay. So you have gotten a theta that has minimized the lower bound. Now what is the guarantee that the lower bound that you have constructed is tight or good lower bound? So with a theta that is closer to the the P M, you create another tighter lower bound and you keep alternating between these two.

### 01:07:59 · Speaker 5

See, these kinds of problems, uh I will take questions in a while. So suppose you have uh a loss, okay, a cost.

### 01:08:09 · Speaker 5

Okay. So it depends on let's say that this cost depends on

### 01:08:15 · Speaker 5

two set of parameters

### 01:08:18 · Speaker 5

theta and W, okay? Now what you are doing is you are maximizing the same cos function with respect to W and you are minimizing the same cos function with respect to theta. So basically, you are seeking the theta star and W star which would simultaneously maximize this law of conjunction and minimize this law of conjunction, right? So what is actually happening is that imagine that you have a you I mean I can't write it in uh two dimensions.

### 01:08:48 · Speaker 5

that is the problem. So basically imagine this cause, okay? Let's say that both your theta and W, okay? Theta is one axis here, okay? And W is another axis.

### 01:09:00 · Speaker 5

and your

### 01:09:00 · Speaker 2

fast function is

### 01:09:05 · Speaker 2

something like this, okay?

### 01:09:12 · Speaker 3

typical to write that sad anyway. So if it's like this.

### 01:09:16 · Speaker 5

what am I seeking is I am seeking a point right in the theta comma

### 01:09:23 · Speaker 5

W axis, okay? In such a way that if I move

### 01:09:30 · Speaker 5

in in in either of the directions at the theta star, the function increases.

### 01:09:37 · Speaker 5

okay? If I move in the either directions of W, okay, at that W star, the function decreases.

### 01:09:46 · Speaker 5

Do you see what is happening? So there is one function, okay? uh one cost function, which is a function of two set of parameters, theta and W. Now I am seeking a point theta star and W star in the the parameter space such that if I move on the function around that theta theta star, the function value decreases at increases at both the both the directions. And if I move uh along the W at that particular point the function value decreases.

### 01:10:22 · Speaker 5

Do you see that?

### 01:10:24 · Speaker 5

Okay, so these kinds of points, right? These kinds of points are called saddle points.

### 01:10:34 · Speaker 5

because they are like horses saddles, right? I mean you know what saddle is. Now saddle, if you move along one direction, at that the function increases, if you move along the other direction, the function decreases, right? That's why it's called saddle points. Now this sort of an optimization problem, right, where you are seeking saddle point of a function, they are called adversarial optimization. That's why the name adversarial

### 01:11:00 · Speaker 5

Yeah, adversarial networks.

### 01:11:04 · Speaker 5

dosierial problems. So because of obvious reasons, right? So this inner optimization problem, right? Okay? is trying to maximize whatever you are trying to rather the outer optimization problem is trying to minimize the same cost function that you are trying to maximize using the inner optimization problem. So in that sense, the inner optimization problem is quote unquote adversary to the outer optimization problem and vice versa.

### 01:11:40 · Speaker 5

See in mathematical sense you are simply seeking a saddle point. So Gyan, the the optimal value for the Gyan, right? The optimal parameters for the Gyan, the optimization problem that you are solving in a Gyan is simply a saddle point problem which is that you have the same cost function. We know why now, right? We have the same cost function and we have to maximize that cost function with respect to one set of parameters W and we have to minimize the same cost function with another set of parameters theta.

### 01:12:10 · Speaker 5

Right? But where did this come from? It came from the fact that we started see this network, the another T network came because remember the entire story please. So you have an divergence metric between P theta and P X which you would want to minimize. Okay, you could not minimize that, so we constructed a lower bound. The lower bound that we constructed becomes is dependent on another class of functions T of X and we represented those class of functions using another neural network and is why another neural network came into picture.

### 01:12:44 · Speaker 5

See, as you can imagine, I will, I mean, don't worry, I will like tie all the loose ends in the in this class. But yeah, see, I mean, just as a side note, you can imagine that once we solve this optimization problem, this discriminator network is of no use. We'll discard it. Right? Because our ultimate goal is to give a Z as an input and get an X cap that behaves like P X, right? So this is of no use. This T T W network is only to construct the lower bound on the

### 01:13:14 · Speaker 5

divergence. So that is why it is used during training, but during inference or prediction or generation, TW network is not at all used.

### 01:13:21 · Speaker 5

you will come to that in a while. But anyway, so we represented this T function using another class, another set of neural networks. So every time you get a T fixed T W function, you will get a lower bound on the F divergence. But to find this T W network, there is a maximization problem that you will need to solve. Okay? So this maximization problem that you are solving creates a lower bound on F divergence for a particular theta. Once you create that, you minimize that with respect to

### 01:13:51 · Speaker 5

theta which will minimize that lower bound which is created by T W in the previous step. And you keep alternating between these two. So create a lower bound, minimize it. Make that lower bound tighter, again come back and minimize it. Make create another lower bound, try to minimize it and you keep alternating between these two. So till a point of where do you stop this? You stop at a point where I mean how do you stop GAN optimization is a question that is that's not well answered. I will answer that in the next half of the class.

### 01:14:21 · Speaker 5

But yeah, so this is how you you uh you do an optimization. I mean that is why it's called a serial problem because you have the same cost function that is being maximized with respect to one set of parameters and you are minimizing the same with respect to another set of parameters.

### 01:14:38 · Speaker 5

Okay. So I will stop here and take some questions and then we will break for a short break and then we will come back and I you know I'll make it much more implementation friendly and I'll take an example for the divergence and we will go to that that basic Gyan paper right which happens to be a special case of this.

### 01:14:58 · Speaker 5

Okay, questions here.

### 01:15:01 · Speaker 5

I'm sure that

### 01:15:02 · Speaker 3

many

### 01:15:04 · Speaker 3

Please raise your hands if you have questions.

### 01:15:13 · Speaker 3

lot of people raised raised your hands when I was explaining, did I explain it in such a way that your question

### 01:15:18 · Speaker 5

questions are all answered.

### 01:15:20 · Speaker 5

Skirt to know

### 01:15:22 · Speaker 5

Okay. Yeah. Raghavendra.

### 01:15:26 · Speaker 6

Yes, so what are what would be the dimension of this T W of X? You have shown it as a narrowing, right? So...

### 01:15:32 · Speaker 5

Yeah, yeah, yeah. Yeah, that's a good question. Uh, depends on the F function that you have chosen.

### 01:15:38 · Speaker 5

for the for the knife when your f function happens to be such that it is the underlying divergence is junction channel divergence no that happens to be a scalar which would which could be interpreted as a classifier I will show that in the next half of the class

### 01:15:56 · Speaker 5

That depends on f function, no? Because if you recall the definition of our t function from the previous class, what was t function? t function takes x and gives out values from the domain of f star.

### 01:15:56 · Speaker 6

That depends on

### 01:15:58 · Speaker 6

Okay

### 01:16:11 · Speaker 7

Yes

### 01:16:11 · Speaker 5

So whatever f star you choose, a function that you choose, this t depends on the choice of f divergence that you have made. Okay. See that is why, okay, now that you asked that question, very relevant. See if you choose your f to be Jensen-Chanon divergence, this discriminator network will take x and give you values between zero and one. Okay? Now if you choose your f divergence to be what is called as chi-square distance, I mean choose your f in such a way, then your T w network will become a regressor, which means that

### 01:16:19 · Speaker 7

Okay

### 01:16:41 · Speaker 5

the output of your T W network will be a real number.

### 01:16:45 · Speaker 5

And that is why you know different f functions will give you different instantiations of Gyan. So there is this L S Gyan, least square Gyan, which is just using an f function which corresponds to the chi-square distance. The naive Gyan is when you choose your f function such that your f divergence is Jensen-Sanon divergence. So if you choose it to be total variation distance then it becomes T V Gyan.

### 01:17:09 · Speaker 5

So see what I have done I mean for if you if you people can appreciate. See when you write a class in object oriented setting you write the constructor of a class no that is what I have done now.

### 01:17:23 · Speaker 5

Okay, so all these gyaans are simply instantiations of this class.

### 01:17:29 · Speaker 5

Right if you can if you can see the analogy. So what we have done is just constructed the family of Gyan. So each of the thing would be an instantiation of it. Okay?

### 01:17:41 · Speaker 5

Yeah, uh, thank you. Yeah, Indrajit.

### 01:17:41 · Speaker 6

Thank you

### 01:17:45 · Speaker 7

Yes. The difference, the cost we are maximizing is the difference between random, okay, X hand, X head, right?

### 01:17:55 · Speaker 5

difference between two expectations.

### 01:17:58 · Speaker 7

No, but X hat is the

### 01:17:58 · Speaker 5

Robert

### 01:18:01 · Speaker 5

आउटपुट ऑफ द एक्स हैट इज द आउटपुट ऑफ द जी थीटा नेटवर्क. एक्स इज द डेटा.

### 01:18:02 · Speaker 7

output of

### 01:18:08 · Speaker 7

Yes, so we are taking the difference between these two, the data generated by us and

### 01:18:12 · Speaker 5

by us? No, hold on. Be precise. We are not taking difference between the data points, we are taking the difference between expectations of T functions and F star of T functions.

### 01:18:24 · Speaker 5

where this x star and x comes from the corresponding distributions. That is what it is. We are not taking x minus x cap here.

### 01:18:33 · Speaker 5

We are taking the difference between the expectations of T X and F star of T X cap as X and X cap are coming from P X and P theta.

### 01:18:44 · Speaker 5

Do you see that? The cost function is difference in expectations, not difference in data points.

### 01:18:51 · Speaker 7

Yeah, that's correct. So, that's the difference between averages, right?

### 01:18:55 · Speaker 5

difference between averages of not x and x cap again. difference between the averages of t x as x is coming from p x and f star of t x as x cap is coming from p t cap.

### 01:19:11 · Speaker 5

It is again not the average of X, it is average of T X.

### 01:19:16 · Speaker 5

it is not average of x cap, it is the average of s f star of t of x cap.

### 01:19:23 · Speaker 7

Okay

### 01:19:24 · Speaker 5

Is that okay?

### 01:19:25 · Speaker 7

Yeah, and then this cost or the maximum maximization should not be equal to minimization which we are doing over theta.

### 01:19:35 · Speaker 7

because

### 01:19:35 · Speaker 5

by that? I didn't follow the question.

### 01:19:38 · Speaker 7

First we are maximizing the this difference right?

### 01:19:42 · Speaker 5

Hmm

### 01:19:43 · Speaker 7

and then we are minimizing the same.

### 01:19:46 · Speaker 5

So you should realize that maximization is with respect to different set of parameters and minimization is is is with respect to another set of parameters.

### 01:19:57 · Speaker 5

The cost function is the same. But maximization is with respect to W, minimization is with respect to theta.

### 01:20:04 · Speaker 7

सो व्हेन वी मिनिमाइज मैक्सिमाइज विद रिस्पेक्ट टू डब्ल्यू, आर वी नॉट चेंजिंग थीटा इन एनी वे?

### 01:20:09 · Speaker 5

No, no. No, okay. That is why I said no, it's for a fixed theta. So you alternate between those two.

### 01:20:11 · Speaker 7

Okay

### 01:20:16 · Speaker 7

Okay

### 01:20:17 · Speaker 5

So I will also show the, you know, the way the gradients flow in both of these. In the next half of the class, that is what I'll do. I will put out a particular F function and I will write down the gradients and also write the gradient descent equations which you would have to implement in your in your assignments, okay? By the way, you will all be implementing all this. That is the that is what you will do in this in your assignment so that there is absolutely no gap between the maths that we have done and the implementation that you do, okay?

### 01:20:47 · Speaker 5

Okay. Okay. Astic.

### 01:20:47 · Speaker 3

Okay

### 01:20:52 · Speaker 1

Yes sir so you mentioned that we are maximizing and minimizing the same cost function. So it is happening

### 01:20:57 · Speaker 3

Yeah

### 01:20:57 · Speaker 5

But but but hold on hold on hold on but with respect to two different set of parameters.

### 01:21:01 · Speaker 1

Yeah, yeah, yeah. So, uh, it is sequentially or at the same time it should be sequentially, right?

### 01:21:02 · Speaker 3

proof

### 01:21:07 · Speaker 5

It is sequentially, you know, alternating.

### 01:21:09 · Speaker 1

ओके। ओके, ओके, ओके। एंड फर्स्ट वी आर मैक्सिमाइजिंग, देन फॉर दैट फिक्स्ड वैल्यू, देन वी आर अगेन मिनिमाइजिंग इट फॉर थीटा।

### 01:21:13 · Speaker 5

Fixed

### 01:21:16 · Speaker 5

Yes, the order does not matter because you start from something and then you alternate between them, no? Okay, yeah, yeah, makes sense. Order does not matter.

### 01:21:18 · Speaker 1

Already

### 01:21:23 · Speaker 1

ओके या या इट मेक्स सेंस

### 01:21:26 · Speaker 2

Yeah, yeah, yeah. Thank you.

### 01:21:30 · Speaker 5

Sachin

### 01:21:33 · Speaker 6

Sir, can you like what is the relationship between this W is also a set of weights and parameters, right?

### 01:21:39 · Speaker 5

θ is also a set of weights and weights, correct?

### 01:21:42 · Speaker 6

And theta was also right the parameters of that neural network.

### 01:21:46 · Speaker 5

There are two neural networks. One one one neural network I have called as W, the other parameters I have represented as theta.

### 01:21:54 · Speaker 6

So this W R max is that this discriminator or critic

### 01:21:59 · Speaker 5

correct. Both of them are like back propagations only.

### 01:22:03 · Speaker 6

Okay, both the mention

### 01:22:04 · Speaker 5

Both the maxima, of course, no, both the optimizations are sorted using back profligation only.

### 01:22:10 · Speaker 6

Okay. And once we figure out like for one given W that you maximize the cost and then for theta you minimize. So like do we compare for all different Ws?

### 01:22:25 · Speaker 5

is no different W. Now you are doing just gradient descent. See, one one iteration through T W and you get a W, you get a lower bound. Now you get another, you do one iteration through G network, you get theta, right?

### 01:22:40 · Speaker 6

hmm

### 01:22:41 · Speaker 5

Then you come back with that fixed theta, the cos function changes, no? See, once you change theta, the cos function changes.

### 01:22:42 · Speaker 6

correct

### 01:22:48 · Speaker 6

Okay Okay

### 01:22:49 · Speaker 5

Now you come back to your W network, tweak your W again. And now the cost function has again changed. Go back to your theta network, change your theta and keep alternating between those two.

### 01:23:00 · Speaker 6

Okay, got it.

### 01:23:03 · Speaker 5

See mathematically what is happening is that the moment you have a particular T that is fixed no there is a lower bound that gets fixed. But that lower bound need not be tight.

### 01:23:16 · Speaker 5

You don't know about need not be time okay so maybe if you want I thought I would do it at the end. Okay let me let me save that for the end okay because that's there is one picture that I write.

### 01:23:28 · Speaker 3

Correct

### 01:23:30 · Speaker 3

Come

### 01:23:35 · Speaker 5

please mute that okay. See uh there is one picture that I write okay of what is happening alternatively uh that would give you that would actually tell you a lot of story but that can that I can write only when your T function happens to be a classifier in the case where your F is J H L and divergence. I will do that I will do that in this class at the end of the class. It will you will get much more clarity as we move on okay.

### 01:24:03 · Speaker 5

Okay

### 01:24:06 · Speaker 5

any any other questions?

### 01:24:09 · Speaker 7

Sorry

### 01:24:10 · Speaker 5

Yeah, yeah, Sushil.

### 01:24:10 · Speaker 7

Yeah, Sushil

### 01:24:12 · Speaker 0

Yeah, so I have a question. In the cost function, I see, uh, you are representing one neural network in the form of

### 01:24:19 · Speaker 6

T W

### 01:24:21 · Speaker 5

what about the G theta like where is it reflected in the cost function?

### 01:24:28 · Speaker 3

x cap no x cap is coming from g theta

### 01:24:33 · Speaker 3

X cap

### 01:24:35 · Speaker 2

Okay, okay, okay, okay.

### 01:24:36 · Speaker 3

fix cap is coming from G theta no?

### 01:24:39 · Speaker 2

ओके

### 01:24:39 · Speaker 3

Okay

### 01:24:45 · Speaker 5

ओके. अनदर क्वेश्चन ओके. हां.

### 01:24:46 · Speaker 7

Okay

### 01:24:48 · Speaker 7

When do we stop? Because we...

### 01:24:50 · Speaker 5

Yeah, I I told you, right? I I told you I I will tell you the stopping criteria next in the next half of the class.

### 01:24:55 · Speaker 7

Next

### 01:24:56 · Speaker 7

Okay

### 01:24:59 · Speaker 5

Okay. Yeah, so okay, we'll take a break. I think I've been here since nine. So we'll take a fifteen minutes break. It is eleven ten in my clock. Shall we come back at eleven twenty eleven twenty five?

### 01:25:16 · Speaker 7

thirty

### 01:25:17 · Speaker 5

eleven thirty. If you come back at eleven thirty we'll only have forty five minutes. Okay eleven thirty is also fine.

### 01:25:24 · Speaker 5

11:30 we'll come back. There's another, yeah, people can leave but

### 01:25:29 · Speaker 3

interesting. So there is Abhitosh, are you there?

### 01:25:38 · Speaker 3

Okay, I think he's not there. Yeah, this

### 01:25:41 · Speaker 5

His name and his name and my name mean the same by the way, okay?

### 01:25:50 · Speaker 5

in Sanskrit right the word Tosh represents happiness and any prefix that you add to it is is just you know qualifying that so some is a prefix that would qualify that which says you know exalted happiness so Santosh is of course you know what that means right so pra is another suffix in Sanskrit that would have the same meaning so that's my name and Abhitosh is another thing so yeah that's I was looking at his name and

### 01:26:20 · Speaker 5

just got this thought and thought I'd share you but share with you the person is not around. Anyway, doesn't matter. Okay.

### 01:26:25 · Speaker 7

for our opposite or same

### 01:26:28 · Speaker 5

No no same thing abhi pra sam all these convey like magnification of whatever you are saying.

### 01:26:35 · Speaker 7

Okay

### 01:26:36 · Speaker 5

Right so Tosh is happiness. Santosh, Abhitosh, Pratosh all these same mean the same. You might have also uh heard this name of Ashutosh no?

### 01:26:47 · Speaker 6

Yes

### 01:26:48 · Speaker 5

Right Ashu means quick. So that's why Shiva is called Ashutosh. Somebody who gets happy very quickly. So that is just a little different but Abhitosh, Santosh, Pratosh all these mean the Paritosh. I'm not Paritosh by the way. My name is Pratosh. Okay. Yeah.

### 01:27:08 · Speaker 5

at same

### 01:27:08 · Speaker 1

seems like too many happy people in their team

### 01:27:12 · Speaker 5

I always tell my parents that it's a Vishnu and my name is

### 01:27:19 · Speaker 5

Right so I don't know how happy I am in my life but yeah they they named me happiness. Yeah. And what's more interesting is when when my parents named me they didn't know what my name means. Somebody suggested and it looked unique and they just chose that name. So then you know I I don't know if

### 01:27:40 · Speaker 5

how many of you know that? I also happen to be a like interested in Sanskrit and Indian history philosophy etcetera. Studied Sanskrit for a long time then I realized what the meaning of my name is.

### 01:27:55 · Speaker 0

Anyway

### 01:27:55 · Speaker 5

Anyway,

### 01:27:57 · Speaker 0

Sir, on a different note, I think, Hold on, hold on.

### 01:27:57 · Speaker 5

Default

### 01:27:59 · Speaker 5

Hey, hold on, hold on. See, we are, we are, we are in the break. People can leave. This is all not unrelated stuff, but yeah, so go on, whoever wants to say.

### 01:28:03 · Speaker 0

in

### 01:28:09 · Speaker 0

Yeah, uh sir, actually I think uh you membered in the Sanskrit club as well, right? So I thought uh there will be some way of teaching from the scratch. Uh that was my interest point to join that. So is there any such thing going on?

### 01:28:09 · Speaker 5

सर एक्चुअली

### 01:28:21 · Speaker 5

Is there any such thing going on?

### 01:28:23 · Speaker 5

I am not an active member there. I mean it is mostly it is mostly like headed by Sangeet and Shankar Ram and these people.

### 01:28:26 · Speaker 0

most

### 01:28:34 · Speaker 3

Okay Okay Okay

### 01:28:35 · Speaker 5

I don't have a lot of say. See when I was in IIT Delhi I used to teach Sanskrit to people like like undergrads there. That was my here I have too much then I didn't have a family no I have two children and no.

### 01:28:43 · Speaker 3

that

### 01:28:43 · Speaker 6

October

### 01:28:49 · Speaker 6

Hmm

### 01:28:50 · Speaker 4

सर, सर, सर, व्हाट इज द थिंग लाइक यू रिजाइन फ्रॉम आईआईटी दिल्ली एंड केम टू आईआईएससी?

### 01:28:58 · Speaker 5

Yeah

### 01:29:00 · Speaker 4

I mean, why you resigned from IIT Delhi?

### 01:29:03 · Speaker 5

बिकॉज़ बैंगलोर इज़ माय होम, आई एम अ साउथ इंडियन गाई एंड उतना गर्मी और ठंड को मैं सह नहीं पाया।

### 01:29:12 · Speaker 5

Anyway that that's actually yeah that's I mean come on right I mean say here anything more than thirty is hot for us and anything less than twenty is cold for us. And mujhe ab Delhi mein ruk do at you know winter was zero degree tak jayega aur summer pe pachaas ka oopar jayega right it was too much.

### 01:29:32 · Speaker 3

Correct

### 01:29:32 · Speaker 5

That's that's the only reason otherwise I was very happy at Delhi. Professionally there was there was absolutely no problem and I like see when I went to Delhi I I thought that I would you know I would want to come back as soon as possible in fact because you asked when I was applying for faculty positions I applied to Bombay Madras Delhi okay. I I could not apply to I I I could not apply to I I I could not apply to I I I could not apply to I I I could not apply to I I I could not apply to I I I could not apply to I I I could not apply to I I I could not apply to I I I could not apply to I I I could not apply to I I I could not apply to I I I could not apply to I I I could not apply to I I I could not apply to I I I could not apply to I I I could not apply to I I I could not apply to unless they go out some for some years and come back

### 01:30:06 · Speaker 5

Now that option was not there. I applied to Bombay, Madras, Delhi and my preference was of course first preference was Madras and then it's Bombay then you move up the map, right? But the first offer was made from I I T Delhi. So...

### 01:30:21 · Speaker 4

सर, सर, यू पीएचडी, यू डन पीएचडी, राइट सर?

### 01:30:24 · Speaker 5

otherwise you can't become faculty in any of these places.

### 01:30:28 · Speaker 4

So from where you did this PhD? We told you know

### 01:30:30 · Speaker 5

Told you know IAC only

### 01:30:33 · Speaker 4

Oh, I guess it's

### 01:30:34 · Speaker 5

Yeah, yeah. So like ten years back, fifteen years back I was a student at I I C.

### 01:30:40 · Speaker 5

सो इसलिए फोर्सफुली आई वेंट टू दिल्ली बट व्हाट आई वास सेइंग इस व्हेन आई वेंट टू दिल्ली आई स्टार्टेड लाइकिंग इट। आई मीन सम ऑफ माय कोलीग्स एट दिल्ली टोल्ड मी दैट दिल्ली विल ग्रो ऑन यू, यू विल स्टार्ट मिसिंग दिल्ली एंड ऑल दैट। आई नेवर थॉट आई वुड मिस दिल्ली बट अभी आई आई मिस दिल्ली बिकॉज़ देयर आर लॉट्स ऑफ गुड थिंग्स अबाउट दिल्ली व्हिच इज नॉट देयर इन बैंगलोर। बैंगलोर इज इट्स अ डूम्ड प्लेस। आई मीन इंफ्रास्ट्रक्चर इज सो बैड। आई मीन इवन दो आई कम फ्रॉम टेक्निकली आई एम नॉट फ्रॉम

### 01:31:10 · Speaker 5

Bangalore I'm from a place called Mysore which is 150 kilometers away from my Bangalore which is heaven. Yeah. But this Bangalore is yeah like Bangalore is hell. I mean all broken infrastructure, rude people. Right. You know what I felt people in Delhi more softer compared to people in Bangalore. Everybody says that North Indians are false and nothing but I mean aapko Hindi mein baat karna hai.

### 01:31:15 · Speaker 3

Hello

### 01:31:17 · Speaker 6

Bangalore is

### 01:31:40 · Speaker 5

that's all the moment you start speaking in Hindi and people are people are more cosmopolitan and more softer there. यहां पे तो माय गॉड आई मीन इट्स ड्रेडफुल व्हेन आई सी ऑटो ड्राइवर्स एंड ऑल द अदर पीपल हियर ओके दिस इज गेटिंग रिकॉर्डेड. डोंट पुट इट ऑन सम सोशल मीडिया राइट? आई मीन आई सी प्रोफेसर्स मेक्स ऑफ कॉमेड्स ऑल.

### 01:32:05 · Speaker 5

So these days you can you cannot have a casual conversation with people right they will record and put it on social media it will become a national news.

### 01:32:13 · Speaker 5

See,

### 01:32:13 · Speaker 4

should not go on live sir. Definitely.

### 01:32:16 · Speaker 5

I'll tell you, I mean I just some two three months back I gave a talk somewhere okay. Something on philosophy somebody called me and I gave a talk. When I when I was giving a talk I never knew that okay they were recording this and all that. These people have recorded and put it on YouTube.

### 01:32:33 · Speaker 5

I mean the thing has become a big thing, right? People are tweeting it right, left and center. There are views for it, against it and all that. Then I had to contact these organizers of that talk and ask them to put a disclaimer saying that the expressions, all the expressions or opinions are of the author and has nothing to do with I I C. These people have put it online, no? They have, they have used my affiliation. They have called it O I I C, professor says this.

### 01:33:03 · Speaker 5

which is true because I am a professor from I I C but my that those are my views not the university's views no. Some of them can some of them may be politically correct some of them are not politically correct and yeah that might cost my job also so it's very should be very very careful when you talk. S R G B C

### 01:33:21 · Speaker 1

I think sir when you start the class you should put the same disclaimer

### 01:33:27 · Speaker 5

No, no, no, this is okay, this is all technical content.

### 01:33:30 · Speaker 5

This is all like you know this is all standard stuff. You can quote me saying oh I A C professor said that Gann solves a hurdle point problem. No problem right? I have no problem with it. Oh I A C professor said that you train a neural network using back propagation. Nobody cares which is true. Now look if I start making statements like okay you know statements regarding some history, philosophy, language, some sensitive issues. If you quote me on that

### 01:34:00 · Speaker 5

that and if you tag I A C's name there it's not correct no. So all my opinion and I am entitled to have my having my opinion. But I should not be as a government employee I should not be having opinions that are I should rather not make my opinions public. See you saw what happened no recently uh Prime Minister went to C G I's home for a festival and it became a big national news. Right?

### 01:34:21 · Speaker 7

back

### 01:34:24 · Speaker 7

There is a video of you sir where you are explaining aham brahmaasmi from sacred games.

### 01:34:30 · Speaker 3

अरे यार

### 01:34:31 · Speaker 5

படம் சேரி

### 01:34:31 · Speaker 1

on the same same lines I saw your video on the video. No that's a

### 01:34:34 · Speaker 5

No, no, that's a, see that's a, that's a rabbit hole. Please don't start that, okay? So let me stop.

### 01:34:41 · Speaker 1

I I want to like ask you like how like

### 01:34:44 · Speaker 6

like how
