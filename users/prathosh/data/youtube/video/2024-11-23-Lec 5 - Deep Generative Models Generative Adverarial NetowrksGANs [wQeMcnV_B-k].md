---
id: wQeMcnV_B-k
title: Lec 5 - Deep Generative Models Generative Adverarial NetowrksGANs
url: https://www.youtube.com/watch?v=wQeMcnV_B-k
date: '2024-11-23'
duration: 01:34:45
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# Lec 5 - Deep Generative Models Generative Adverarial NetowrksGANs

## Transcript

### 00:00:05 · Speaker 1

Okay, what I'm saying is what we will do is I will I will stop, let's say after after 30 minutes or so, once I've gone through a major topic, then we can have a question and session. So if people have questions, what I would recommend you is that just write them down. Okay, so whenever you have a question, just write write them down on a sheet of paper.

### 00:00:35 · Speaker 1

And whenever I talk and ask for questions, I mean, ask prompt you for questions, ask me then. Does that make sense? So that there is a gap, I mean, there is a balance between the flow of the class and also the, I mean, I do encourage a lot of questions. I mean, I'm happy that you people are asking good questions, but let us not have multiple, pot and pour interruptions. So that the flow is there.

### 00:01:05 · Speaker 1

thing and there was one there was a couple of other questions on uh

### 00:01:10 · Speaker 1

I mean some of you are asking whether this course is going to be a fully quote unquote mathematical or will there be some practical considerations issues that would be considered uh uh I mean see the a good answer that is that uh there is no practice without theory without math uh I mean having said that

### 00:01:33 · Speaker 1

Once we complete the mathematical nuances and other details, you definitely go to go to the practical implementations because all your assignments will be coding assignments. So there will all be practice based assignments only. And also in the class and tutorials, whenever needed, we will also talk of the practical implementations and the other things.

### 00:02:00 · Speaker 1

Okay uh that's about it I suppose anything else that you just take other issues that you want to discuss before we start the class

### 00:02:11 · Speaker 2

So I would like to share with you

### 00:02:18 · Speaker 1

Hello

### 00:02:20 · Speaker 3

Yes

### 00:02:23 · Speaker 1

Yeah anything you did did you have a comment

### 00:02:27 · Speaker 3

Are you able to hear me

### 00:02:28 · Speaker 1

Yes yes I can hear you go on

### 00:02:30 · Speaker 3

Yes just one suggestion if possible you cover theory and then you give a problem example right

### 00:02:38 · Speaker 1

Uh for theory and energy what

### 00:02:42 · Speaker 3

problems you explain a problem and give a solution to it right

### 00:02:48 · Speaker 1

Uh problem I I I didn't solve it yet

### 00:02:49 · Speaker 3

Well example example

### 00:02:52 · Speaker 3

Like you give cover cover a topic story of it and then you give example for that right

### 00:02:59 · Speaker 1

these are not like these are these topics are not like your let's say class 12 math where okay you learn you learn how to differentiate functions and then there are some example problems on differentiate functions it's not that see now we are looking at adversarial optimizations or GANs right so by practice what I mean is for instance in today's class

### 00:02:59 · Speaker 3

I'm playing

### 00:03:25 · Speaker 1

I will tell you how to try again practically, right? How does all the theory that we are looking at translate into practice practical implementation, right? So there are no numerics per se.

### 00:03:38 · Speaker 1

Because it's, as I said, no, it's not like a fundamental calculus or probability theory kind of course where you introduce a concept and solve many, many problems to be solved. It is not that way, right? By practical stuff, I mean the implementation stuff. That how would you, how would you take these ideas and implement those in practice?

### 00:04:00 · Speaker 1

Uh does it make sense

### 00:04:03 · Speaker 3

Yeah

### 00:04:06 · Speaker 1

Uh okay anything else

### 00:04:08 · Speaker 3

You have one more doubt right here This is about conjugate of a convex function

### 00:04:16 · Speaker 3

If we draw a graph of conjugate of a function convex function how will it look like Will it be inverse of it or

### 00:04:22 · Speaker 1

Yeah it'll yeah it'll look something like

### 00:04:30 · Speaker 1

Yeah

### 00:04:33 · Speaker 1

Should we continue with the class

### 00:04:50 · Speaker 1

Me

### 00:04:53 · Speaker 1

So I'm throwing my iPad

### 00:05:25 · Speaker 1

Yeah also tell me whether this black background and the white font is okay with you or should we have to

### 00:05:35 · Speaker 1

Switch it to white background and black

### 00:05:40 · Speaker 4

I did it myself

### 00:05:42 · Speaker 1

It is fine okay

### 00:05:45 · Speaker 1

Okay

### 00:05:46 · Speaker 4

So so if possible just change the colour of pen whenever there is a highlighted topic

### 00:05:53 · Speaker 4

Like a note or anything

### 00:05:56 · Speaker 1

Uh that I'm doing right I'm looking uh doing that highlighted highlight thing

### 00:06:01 · Speaker 4

No no no I mean I mean when you are taking some new topic

### 00:06:01 · Speaker 1

No no no I mean I

### 00:06:04 · Speaker 4

something new then just change the color so that we can mark it properly if possible otherwise also fine

### 00:06:14 · Speaker 1

Uh, but yeah, so everything that I write is important that way. Yeah. So anyway, so I'll, I'll, I'll take that into consideration. Uh, and also there was some, uh, discussions on KL divergence and, and all that in the group. No, I will, like, I thought once we cover these topics, it will be clear. Uh, or I, I'll respond to that. Okay. Okay. So let's start. So just quick, quick recap. Uh, before we go to the topic.

### 00:06:44 · Speaker 1

for today's lecture so we were looking at adversarial optimization right or generative models uh via adversarial uh optimization so what is the context the context is that we want uh to build a generative model which is that it takes uh an arbitrary random variable as input in this case a gaussian random variable and it generates uh

### 00:07:14 · Speaker 1

or it samples from an underlying unknown distribution right so we represented that that function as g theta of z where z is an arbitrary random variable and it's cap just highlight it

### 00:07:45 · Speaker 1

So this apple pencil is always with my laptop. Whenever I want to write it, it has 0% charge. I don't know why. Anyway, so there is this function d theta that would map an arbitrary random variable z to another random variable x cap. Okay. Now what do we need? We need a situation where this x cap has a distribution that follows the distribution of data.

### 00:08:17 · Speaker 1

Okay, which we have called px. Why is that? If this p theta becomes close to px, then we have achieved what we want, because then if you take an arbitrary variable z and pass it through this function g theta, then you get samples from px, which is the underlying distribution. Okay.

### 00:08:43 · Speaker 1

Now the question was how do you set the parameters of this neural network g theta such that p theta which is the distribution of the output of the neural network is close to px which is the input of I mean which is the input unknown distribution. The solution for that is that what you do is estimate a distributional divergence measure between px and p theta that will become a function of theta and set the parameters of

### 00:09:13 · Speaker 1

this neural network theta such that this is minimized so if you do this then the resulting neural network g theta of neural network that you get will be such that it will take an arbitrary random variable z as input and it will output x cap whose distribution happens to be following px

### 00:09:38 · Speaker 1

Now, if you recall the tutorial, how do we solve this optimization problem of minimizing some sort of a divergence measure or a loss function with respect to the network? All of you know how to do that, correct? Now, this theta star equal to argmin d b theta px and p theta. This optimization problem is solved using backpropagation.

### 00:10:03 · Speaker 1

Is that okay

### 00:10:06 · Speaker 1

Any questions on problems problem setting the

### 00:10:11 · Speaker 1

how the problem is set up so in the

### 00:10:14 · Speaker 3

What is that

### 00:10:16 · Speaker 3

This accent is the complete image right

### 00:10:19 · Speaker 1

chart as the completing measure

### 00:10:21 · Speaker 3

Yeah and it doesn't depend upon the random inputs we are given

### 00:10:25 · Speaker 1

Very much depends on the random input, right? Because it is G T of Z, Z is the input.

### 00:10:32 · Speaker 3

Yeah but it depends on theta parameters right

### 00:10:34 · Speaker 1

It also depends on parameter parameters and it also depends on theta

### 00:10:40 · Speaker 1

See

### 00:10:40 · Speaker 3

Okay when I say input it's z z which is a uniform sorry normal distribution on this diagram

### 00:10:49 · Speaker 1

It depends it depends on C it depends on theta both of it

### 00:10:53 · Speaker 3

But G is the random right

### 00:10:56 · Speaker 1

Z is random correct

### 00:10:58 · Speaker 3

Yeah then then it should not matter what we do right it's random right

### 00:11:01 · Speaker 1

Oh, that way you're going to see. Okay, so what when you said that it does it does not depend, I thought what X cap that you get does not matter what Z that you get. That's not what it is. So for a given Z, you will get a given X cap. But yeah, but you can choose any input distribution on the arbitrary random variable. Yeah, that is correct.

### 00:11:24 · Speaker 3

So whatever we give as Z, because it is random, we'll get the X cap, right?

### 00:11:31 · Speaker 1

post training post training if you train it such that this divergence is minimized then it is true you will get an x cap from the distribution different z will give you different x caps so you remember i told you to look at that this person does not exist dot com last time right yeah so every time you get a different you you give a different z as an input you get a different image generated

### 00:11:48 · Speaker 3

Yeah

### 00:11:56 · Speaker 1

Okay, but you have to like you should not change the distribution of Z. For instance, suppose while training you have sampled Z from uniform random variable, you should not start sampling from normal random variable when you are doing inference or generation. That is not what should do what you should do.

### 00:12:17 · Speaker 3

Okay, so yeah, does it mean that if X hat is a human face, different Z will give different human faces?

### 00:12:27 · Speaker 1

Of course driving different G's will give you different outcomes correct

### 00:12:31 · Speaker 3

Oh

### 00:12:34 · Speaker 1

Okay

### 00:12:36 · Speaker 1

All right, so now any other question on this?

### 00:12:39 · Speaker 2

one quick question the output is gonna be human faces and human faces only but the mixtures of human faces or it can be like

### 00:12:49 · Speaker 2

You can have human faces with different features let's say three eyes or four eyes

### 00:12:54 · Speaker 1

Okay, that depends on how good your training has been. It that can happen. See, how does that translate to mathematical is that if you have made this divergence metric between px and p theta really low, then you will only get images from human faces because px, the data that you have been given only have like images from the distribution of human faces.

### 00:13:22 · Speaker 1

That's why you should train it well. See, if you have not trained it well in such a way that this divergence measure has not gone to arbitrary low values, then you will have all these kinds of artifacts. So you will see that in your assignment. So in your assignment, I will actually ask you to train these neural networks. If you have not trained them well, then the output will not be good.

### 00:13:45 · Speaker 2

Got it so

### 00:13:49 · Speaker 1

Just one

### 00:13:52 · Speaker 1

one other question uh third question

### 00:13:56 · Speaker 4

Lesser of the two

### 00:13:58 · Speaker 4

Uh so uh just something I was wondering sir um like uh I was

### 00:14:02 · Speaker 3

looking at the talk as well that the Afghan authors gave on YouTube. So it was not very clear to me like did they think of this adversarial approach first and then justified it or proved it with maths or the maths

### 00:14:17 · Speaker 4

to the discovery like what came first like the the intuitive understanding or the mathematical foundation behind it

### 00:14:23 · Speaker 1

Yeah

### 00:14:27 · Speaker 1

Yeah, so that's a general question. See, I've been in this business of research for a decade now. I can tell you for sure that all of my papers, the work that I have done, it's always that we do some empirical experiment based on some hunch. It works. Whenever it works, we backfit the math.

### 00:14:54 · Speaker 1

My firm belief is that if there is something that is working then there should always be good math behind it or good

### 00:15:02 · Speaker 1

systematic understanding behind it but the way this is how i do it i don't know how others do it in fact uh chronologically speaking no as our home minister said to chronologically so if you look at if you look at the chronology gan paper came in 2014 okay uh which only has em empirical experiments okay but this f gan which is a much more uh uh foundational uh

### 00:15:32 · Speaker 1

Understanding of what was happening came two years afterwards. So that way, uh, empirical stuff came first and then math came later. But

### 00:15:42 · Speaker 1

My I mean this is how

### 00:15:45 · Speaker 1

things happen right mostly in engineering research however while you understand so to me always principled understanding is something that i would like right i mean if you just tell me and give me an algorithm and say that oh there is a discriminator there is a generator okay there is these two networks competing with each other etc i will not be convinced because i don't know why it is working what is actually happening and so on so that is why when i teach i always teach math first from a math first approach because that is

### 00:16:15 · Speaker 1

more grounded and principled. Now, once we once I put down that mathematical foundation, I would connect it to the empirical stuff, which I will do in this today's class. Okay. Yeah. But I mean, it's too long. I mean, it's too long story short.

### 00:16:35 · Speaker 1

In engineering, mostly the empirical science precedes math, but there have been a lot of cases where you come up with mathematical ideas and then translate it to empirical structure as well. Both happens.

### 00:16:53 · Speaker 4

Got it

### 00:16:53 · Speaker 1

okay so uh now the thing is given data and and samples from p theta so now again okay so now what is the core question here that uh you again i'm emphasizing this multiple times because it has to just look into the

### 00:17:10 · Speaker 1

your mind so basically the question that we have is we have this setup and we want to minimize this distribution and divergence measure between px and p theta okay now what do we have what we have as in at our hand are samples from px which we call as uh data okay that is what data is and we also have samples from p theta what are samples from p theta they are simply the outputs of neural networks how do we get multiple samples from p theta as somebody

### 00:17:40 · Speaker 1

saying you sample or you get you get multiple uh samples from the gaussian random variable how do you get the samples from gaussian random variable you have this rand in function right in in all pseudo random random number generators right you get uh the random numbers generated from random function and give it as an input to g theta okay that is so you get multiple samples from p theta so now you have samples from d you have samples from p theta

### 00:18:10 · Speaker 1

The question now is how do you compute the distributional divergence d theta so that we can use that as a loss function and back propagate through this neural network to minimize that. That is what we need to do, right? If we take p theta and px and compute the distributional divergence and minimize the distributional divergence and train the neural network using that, this neural network g theta will start generating samples from px. That is the idea, correct? Yeah.

### 00:18:40 · Speaker 1

So what is the big deal about it is that remember that the biggest problem in all of generative modeling or all of machine learning is that you

### 00:18:53 · Speaker 1

Do not know the distributions okay between which you are computing the divergence you only have samples from it. So you don't know what the form of p x and p theta is but you only have samples from p x and p theta.

### 00:19:08 · Speaker 1

Yes, I have written that already, right? So how do we have samples from P x? It is the given data. How do we have samples from P theta? It is simply choose different g's and pass them through g theta of c. That will give you samples of P theta. Now having samples of P x and P theta, how do you compute the distributional divergence is the question. Okay.

### 00:19:30 · Speaker 1

Now before going to compute distributional divergence, I defined a large family of divergence matrix which we called as the F divergence of which the KL divergence is also a member KL divergence the forward KL reverse KL gents and Shannon divergence all of them are members of this family we defined F divergence as this particular integral and this F

### 00:20:00 · Speaker 1

is a convex function okay so you plug in a convex function you get a different divergence metric okay that is what we saw

### 00:20:09 · Speaker 1

okay now coming back to our goal our goal was to compute the f divergence between px and p theta using their samples without knowing the underlying distributions okay so we saw that there is a way to do it uh the way to do it is that if you have uh an integral okay with respect to a density function to be computed you can approximate that using uh what is called a sample means okay now this result which we call

### 00:20:39 · Speaker 1

Love lies in numbers one

### 00:20:45 · Speaker 1

Simply say that

### 00:20:49 · Speaker 1

Integrals can be computed

### 00:20:58 · Speaker 1

out okay or rather with only the samples

### 00:21:13 · Speaker 1

So that is law of large numbers if you simply have samples from distribution and if you are looking at integrals of functions with respect to density functions without having so please look at this equation this is a pretty important so this one

### 00:21:44 · Speaker 1

Okay, so this is actually one of the key equations that we will be using multiple times in this course that if you want to compute an integral of a function h of x with respect to some density function p of x, I mean, it is also called the expectation of h of x with respect to p of x, you simply take the sample averages of the delta of x, h of x computed all xi's where xi's are coming from px. So in this case, it is data, right?

### 00:22:14 · Speaker 1

You can compute these sorts of integrals using sample estimates. This is a known result. Now, how do we use that? If the divergence metric that we are trying to minimize, if we can express that in terms of expectations over px and p theta, then this divergence metric can be computed using sample estimates from px and p theta via log-log-logs. Because we know that we can compute expectations using samples.

### 00:22:44 · Speaker 1

this result called of last numbers then if we can represent our df in somehow via expectations over px and p theta then we can compute the m divergence you simply using the samples correct so now with that goal we now wanted to express df in terms of expectations over px and p theta okay now uh with this goal we saw that we cannot represent this m divergence exactly

### 00:23:14 · Speaker 1

the exactly where expectations over these two but what we can do is we can express the lower bounds on df in terms of expectations now instead of minimizing the m divergence we minimize the lower bound of it that is the idea one can ask no okay and we set our goal as finding out the g theta such that the uh the m divergence

### 00:23:40 · Speaker 1

sorry f divergence is minimized now instead of minimizing f divergence you are minimizing the lower bound on it i mean is it is it correct now that's not that's not exactly correct because if you can minimize the divergence itself then it is great but the problem is f divergence cannot be minimized exactly uh without having the distributions px and p theta now because we don't have distributions px and p theta but only have samples from it what

### 00:24:10 · Speaker 1

do is we instead solve an approximate problem which is minimizing the lower bound on f divergence okay right so now what we should do is in an issue we should bound f divergence and express in terms of expectations over px and p theta for that we did some uh some algebra we took the convex conjugate of uh of the f function in the f divergence and we did some manipulations and finally what happened is that we got

### 00:24:42 · Speaker 1

got this result where we expressed uh uh f theta okay df the f divergence uh as the uh as i mean we carved a lower bound on the f divergence uh via this expectation so what is this there is uh the lower bound that we obtain will become a function of this another class of functions called dx right now what we what we are saying is that there is some terminology here which is expectation of some function

### 00:25:16 · Speaker 1

of some other function f star of tx as x cap is coming from p theta right so we know how to compute both of these expectations why if we know what t function is then this expectation can be computed using log large numbers right where you can approximate this using sample errors i will write down all that and show you how to do it in practice okay so now basically what we did was yeah we have expressed the lower bound on the f divergence in terms of expectations over unknown distributions

### 00:25:46 · Speaker 1

Now the lower bound that we computed on f divergence, okay, is itself involves an optimization that itself involves an optimization problem over a class of functions Tx. Now what I mean to say is that if you give one particular Tx, you will get one lower bound on f divergence.

### 00:26:07 · Speaker 1

And it is something that you should note

### 00:26:11 · Speaker 1

that as a note here

### 00:26:16 · Speaker 1

Okay so it is two

### 00:26:20 · Speaker 1

once it aired this was a little bit

### 00:26:23 · Speaker 1

Now lower bound

### 00:26:29 · Speaker 1

Or if they're interested

### 00:26:34 · Speaker 1

No one's

### 00:26:38 · Speaker 1

following

### 00:26:40 · Speaker 1

an optimization problem

### 00:26:50 · Speaker 1

over some function classes denoted by t of x

### 00:26:58 · Speaker 1

Okay yeah this is the uh model of the story uh

### 00:27:06 · Speaker 1

See that? Okay. Is that now we constructed the lower bound on the M divergence or the loss function that you would want to minimize and we express that in terms of expectations over P x and expectations over P theta.

### 00:27:22 · Speaker 1

And the lower bound itself contains an optimization problem that is to be solved over another set of functions, class of functions that we denoted as Tx.

### 00:27:33 · Speaker 1

Okay, so let me stop here for a couple of minutes and ask questions. Please ensure that all of you are totally with me on this, okay? Because whatever I do now will be building upon this. So make sure that you understand this perfectly and then we will move on. We will spend some five minutes on this. And this is actually a key equation for GANs. Once we do this, then actually it's all done. Okay.

### 00:28:03 · Speaker 1

questions

### 00:28:05 · Speaker 4

Sir, I think there's a typo on the line just before this if you could scroll just a little higher

### 00:28:14 · Speaker 4

The close bracket I think should come just before dx in that line.

### 00:28:19 · Speaker 2

and then the close bracket because p of p theta of x should be multiplied

### 00:28:25 · Speaker 1

Oh yeah right yeah thank you for noticing that

### 00:28:31 · Speaker 1

this here

### 00:28:41 · Speaker 1

More business

### 00:28:45 · Speaker 1

Some fancy thing okay

### 00:28:57 · Speaker 1

And this is for school girls and kids okay they're eight something

### 00:29:12 · Speaker 1

Okay thanks. Luke Sh. Sir can you please explain how this greater than sign came once again?

### 00:29:21 · Speaker 1

Like DTF is greater than

### 00:29:33 · Speaker 1

that's the content of last class but anyway so if you have to trace back the entire derivation

### 00:29:43 · Speaker 1

But

### 00:29:43 · Speaker 4

That's the last step uh after TX

### 00:29:46 · Speaker 1

I mean we have been we have been after

### 00:29:49 · Speaker 4

30 star of science you want

### 00:29:50 · Speaker 1

You understood you understood why there is this why instead of having small t y capital T K M right because you are solving an optimization problem internally correct

### 00:30:03 · Speaker 1

I'm fine

### 00:30:03 · Speaker 4

Oh yeah

### 00:30:04 · Speaker 1

If I pull that maximal maximization out, okay. So would this capital T or rather this Tx that we have, right, should be such that it will give you the solution for that optimization problem, internal optimization problem at all x, correct?

### 00:30:24 · Speaker 2

Yeah

### 00:30:26 · Speaker 1

Now suppose there is some T x with capital T of x which is a function that would not give you the solution for optimization problem for all x.

### 00:30:37 · Speaker 2

Okay

### 00:30:39 · Speaker 1

In that case, what happens? This entire integral that we compute, right, or the maximum value that we compute under that Tx will not be, will always be less than the case where you would have gotten the maximum at all x, isn't it?

### 00:30:59 · Speaker 2

Okay

### 00:31:01 · Speaker 1

get it see sup i mean instead of t star of x which would give you the maximum value at all t if you had another function t that would not give you maximum at all points if it does not give you maximum at all points what does that mean it is always less than the maximum right it can at most is equal to the maximum or it is less than the maximum

### 00:31:25 · Speaker 2

Yeah okay yeah so

### 00:31:27 · Speaker 1

So basically what you are doing is you are searching for that function, okay, T of X, which would give you the maximum value for that optimization problem at all T's, sorry, at all X.

### 00:31:44 · Speaker 1

Now if you get that function then this inequality will be the weak quality

### 00:31:50 · Speaker 1

If you get that function

### 00:31:54 · Speaker 1

Okay, now what is the script T? Script T, you can see the visualize script T as a bucket of large classes of functions. So you are choosing from a bucket of family of functions.

### 00:32:09 · Speaker 1

Okay, now if you in that bucket of function that you are searching over, if you can get a function small, I mean t of x such that it is equal to t star of x for all x, then this becomes equality.

### 00:32:23 · Speaker 2

Yeah good observation

### 00:32:25 · Speaker 1

But if you cannot get that function, if you get another function t of x, which is not equal to t star of x at even at 1x, then it becomes inequality because at that x, your t of x is less than t star of x.

### 00:32:39 · Speaker 1

Call it no

### 00:32:41 · Speaker 2

Yes I can record

### 00:32:42 · Speaker 1

I can write it maybe

### 00:32:53 · Speaker 1

I'll write that here

### 00:33:00 · Speaker 1

inequality

### 00:33:04 · Speaker 1

Bites

### 00:33:08 · Speaker 1

Because

### 00:33:13 · Speaker 1

DRP

### 00:33:17 · Speaker 1

less than or equal to t star of x

### 00:33:20 · Speaker 1

for every x let's up

### 00:33:23 · Speaker 1

Okay if

### 00:33:27 · Speaker 1

T of x is equal to T of x star oh sorry T star of x star

### 00:33:36 · Speaker 1

Paratolics

### 00:33:42 · Speaker 1

Then you correct

### 00:33:48 · Speaker 1

Yeah I think that's worth writing

### 00:33:51 · Speaker 1

And see one other thing I'm almost ensuring that whatever I say, you know, whatever the storyline that I build, I'm writing all of it, right, one after the other, right? I mean, I write this as goal, questions and all that. So this notes, right, please go through it before you come to the next class. Every class, go through this line by line, step by step. Also, you have the recordings, watch the video and come to the next class. That will help you a lot. And of course,

### 00:34:21 · Speaker 1

We are available for questions for WhatsApp and Teams. Okay.

### 00:34:28 · Speaker 4

Yes sir in this case this T of X do we choose any function and then try to optimize it or we d we try to

### 00:34:33 · Speaker 1

Good try too. Good good question uh see if you know how GANs work in other than this network there is another network now which is called the discriminator network

### 00:34:47 · Speaker 1

That is your t of x. The need for another network comes up because you have to choose from a bucket of functions and you optimize when you pick those bucket of functions, you approximate those functions using another neural network. We will see that.

### 00:35:00 · Speaker 4

Okay okay yeah thank you so much

### 00:35:05 · Speaker 1

Okay any other question

### 00:35:13 · Speaker 1

Yeah

### 00:35:18 · Speaker 4

function

### 00:35:18 · Speaker 1

No, no, no, no, no, no, no. See, this T has nothing to do with that F. See, F divergence in the F function in F divergence, know that our definition only that is convex. Nothing else is convex. This F function is convex, that's all.

### 00:35:41 · Speaker 1

Should have been one

### 00:35:48 · Speaker 1

Skuttle

### 00:36:02 · Speaker 1

See on a lighter note, the person who put this feedback, no, please don't take it badly. I mean, there's no, anyway, it's anonymous, but it was pretty funny. So I received a feedback where somebody said that, you know, I'm paying this much fees to ISD for this particular course. So I expect this, this is, right? So I mean, one thing was, it's very, very revealing for me that this course,

### 00:36:32 · Speaker 1

cost this much money I didn't know that apparently every credit here is worth twenty thousand rupees no I mean I was thinking that all this is reimbursed for you from your respective companies

### 00:36:46 · Speaker 1

Don't they? I think they would know. I mean, there is some learning program that's always there. You don't pay these fees from your pocket, do you? Just curious. I'm not asking. I'm not asking that that person who wrote, okay? I don't want to, I don't wish to know. But yeah, in general, I'm asking out of curiosity. So not all of you, like your companies don't pay that, huh?

### 00:36:53 · Speaker 4

I'm not ready

### 00:37:10 · Speaker 2

Partially

### 00:37:10 · Speaker 4

Absolutely

### 00:37:12 · Speaker 1

I see

### 00:37:14 · Speaker 3

But I think it's different

### 00:37:14 · Speaker 4

But I say it's difficult

### 00:37:19 · Speaker 2

That is fully sponsored

### 00:37:19 · Speaker 4

for response

### 00:37:21 · Speaker 3

This conference

### 00:37:23 · Speaker 1

See that makes me feel a little little less guiltier you see okay so

### 00:37:30 · Speaker 4

too for all

### 00:37:32 · Speaker 1

Then I'll be speeding

### 00:37:35 · Speaker 4

No you are not guilty

### 00:37:36 · Speaker 3

What was the question?

### 00:37:36 · Speaker 1

i have some demand right i mean they have to teach more practical stuff you know i didn't pay the fees to look at math and whatever it doesn't matter that's that's fair also the demand was fair i mean i'm not i'm just joking right i mean this the weight of putting it that okay i this is the amount of fees that i pay i mean it's sort of exorbitant uh that's a lot i didn't know that this course cost that much money okay so but they said that okay

### 00:38:06 · Speaker 1

paying this much money not to look at math or whatever but then I thought okay yeah it's a lot of money I hope see if it's your company that is paying I don't mind no they paid for all kinds of stuff that's not big money for your company but if you're paying it from your pocket then it's it's it is I mean it's all relative but still yeah

### 00:38:30 · Speaker 1

So one credit apparently cost 20,000 rupees right interesting okay which is considerable

### 00:38:37 · Speaker 4

But this is one of the prime courses in the program so maybe he felt like that

### 00:38:46 · Speaker 1

Hop hop how do you know that it's a he I don't know I might be here

### 00:38:49 · Speaker 4

I don't know that's

### 00:38:53 · Speaker 1

Uh uh here so so this is the

### 00:38:54 · Speaker 4

So simple so this is the course I'm doing the M Tech for

### 00:38:59 · Speaker 1

People are acting

### 00:38:59 · Speaker 4

People are acting yeah

### 00:39:01 · Speaker 1

I mean I understand you know you uh to I mean don't get me wrong again that customers always have their right to question whatever the product that is being see everybody now talks of customer obsession and all that right so customer is looking that is the reason I put that feedback form out and it is totally anonymous and whoever wrote that please don't get uh offended I'm just taking it lightly so whatever you think

### 00:39:31 · Speaker 1

is a fair demand put it out there and i'll be happy to incorporate as long as i can incorporate okay yeah okay

### 00:39:39 · Speaker 4

Sir how about the offline classes student also register for this course and elective subjects or let's say generic one like three four classes for them

### 00:39:49 · Speaker 1

again uh what is what is the question

### 00:39:52 · Speaker 4

I mean how offline classes goes uh they need to register for this core courses or it's a scheduled for them like first year these classes next year

### 00:40:02 · Speaker 1

no no no no no very similar to you i mean there are core courses just like you have three four core courses right they would i think have some six core courses rest of all are all uh like this thing um electives and by the way i also teach this course right offline and i'm doing it in isc right now that class also has 100 plus people in isc and uh trust me uh that's i mean that's at least two three times more mathematical than

### 00:40:32 · Speaker 1

this okay i would i mean i i know that most of you people are not most all of you are professionals and might have been a little out of touch of from maths but there i do like much more maths than this so this is not the upper bound of your maths that one can do in this course so please be rest assured on that but anyway if you have any any anything that that you would like to see as a change in this course let us know that is why we have that feedback thing and we are happy to listen

### 00:41:02 · Speaker 1

Okay

### 00:41:03 · Speaker 3

Modes are in a regular product development like this type of maths we are rarely using right

### 00:41:12 · Speaker 1

I mean I'm did I become judgmental I mean I'm not complaining at all I completely agree with you that you don't use that but that is why no I kind of

### 00:41:24 · Speaker 1

Yeah, so make it accessible. I try to make it as much accessible as possible. But we see there is another way to teach this. I'll tell you honestly, I can completely get rid of math and only teach it like what is done in Coursera, right? Or this Android kind of stuff where I'll just give you algorithms and tell you, put some block diagrams and tell you how to do it. But honestly, right as an instructor, I don't see value in doing that. See, whoever has done this course before, again, this is not self-bragging, have told,

### 00:41:54 · Speaker 1

that uh you know doing it this way uh while difficult uh while while it is difficult during the course time right but if you put in enough effort to understand and do assignments and uh tutorials and all that uh they have been benefited from this you know this is what will actually differentiate uh you people from everybody uh and their grandmother who does machine learning so everybody is a data scientist these days right what differentiates uh

### 00:42:24 · Speaker 1

somebody who knows well and somebody who does not is that you know some of the fundamentals and you can go more deeper into it. So I there is value in doing math. It's not that it's totally valueless, but I understand that it takes a little bit of more effort, but yeah, that is what I expect from you people to do. Having said that, let me know if all of you think that math is completely valueless. It's much easier for me to teach the algorithms and course around we can do it.

### 00:42:54 · Speaker 1

but again that's not my recommendation though okay so let's continue so what we had was that we had this

### 00:43:04 · Speaker 1

call the word bound on DFTI budgets let's start from date given so we are given data

### 00:43:18 · Speaker 1

That's it

### 00:43:26 · Speaker 1

This is

### 00:43:29 · Speaker 1

ID from PX on from PX

### 00:43:39 · Speaker 1

so we have constructed an f divergence between okay before that we'll write what our p theta is so we have this setup where

### 00:43:49 · Speaker 1

That is a neural network

### 00:43:54 · Speaker 1

And the AI represent neural networks right they

### 00:43:58 · Speaker 1

represent the dimensionality of the data so this is a neural network whose

### 00:44:03 · Speaker 1

Dimensionality keep increa increasing as you go deeper and deeper

### 00:44:09 · Speaker 1

By the way did Chidan do backpropagation for CNNs or was it only for material MLPs

### 00:44:18 · Speaker 3

Mail piece mail piece

### 00:44:19 · Speaker 1

For the M and N piece okay

### 00:44:22 · Speaker 1

Okay, then you should look at backprop for CNNs, okay, just as an exercise. When it's not completely needed, but it's a good exercise to do. Okay, g theta and whatever we get at the output is what we call as x theta. And this has distribution p theta, right? This z was coming from normal distribution. Now with this setup, we constructed a lower bound on the distributional divergence between px and p.

### 00:44:52 · Speaker 1

theta okay this v set was greater than equal to this maximization over a class of function so what does this mean this actually means that you are searching over a class of functions script d and the thing that you have is you have an expectation here with respect to d of x as x comes from px you have another expectation here

### 00:45:22 · Speaker 1

respect to F startup

### 00:45:26 · Speaker 1

effects as

### 00:45:29 · Speaker 1

X graph here as X graphs comes from P theta

### 00:45:35 · Speaker 1

That is what we have seen so far. Now the question is um so recall that we are interested in recall

### 00:45:47 · Speaker 1

interested in finding out a theta star okay that is the minimizer

### 00:45:56 · Speaker 1

The m divergence right This is what we wanted

### 00:46:01 · Speaker 1

We could not do it because we didn't have access to PX and P theta. So we approximated that by the minimizers.

### 00:46:09 · Speaker 1

And this minimization is over theta okay minimize this minimize the lower bound

### 00:46:24 · Speaker 1

Okay now which is

### 00:46:31 · Speaker 1

And by the way all of you understand this notation argument right Have I explained notation argument

### 00:46:40 · Speaker 1

it right i mean it is that set of theta which would minimize whatever is there within the function okay mean is the minimum value argument is the minimizer okay the argument which minimizes fine so you have to minimize over theta which is the lower bound

### 00:46:57 · Speaker 1

No that it door bound

### 00:47:00 · Speaker 1

It's a further maximization of P

### 00:47:07 · Speaker 1

This differences of this expectation I will not write it expectation over the px minus you have expectation of something with respect to e theta this is what it is right

### 00:47:21 · Speaker 1

Oh that's will become will become

### 00:47:34 · Speaker 1

Okay maybe before that let us do this

### 00:47:40 · Speaker 1

Now this minimization right this the outer minimization is

### 00:47:46 · Speaker 1

Mean with respect to

### 00:47:50 · Speaker 1

is pay attention here this is mean with respect to

### 00:47:57 · Speaker 1

I don't know what this

### 00:48:01 · Speaker 1

Often you don't know what correct

### 00:48:04 · Speaker 1

Theta are parameters of a neural network and you need to minimize a function or a value with respect to parameters of a neural network. Do we know how to do that?

### 00:48:17 · Speaker 4

Back up

### 00:48:17 · Speaker 3

That's okay

### 00:48:18 · Speaker 1

That is back propagation so you can do this using back propagation

### 00:48:23 · Speaker 1

back prop over what

### 00:48:26 · Speaker 1

over the G theta network

### 00:48:40 · Speaker 1

Okay, that's what it is. Now there is

### 00:48:44 · Speaker 1

is maximization with respect to class of functions

### 00:48:54 · Speaker 1

Do we know how to solve that We don't

### 00:48:58 · Speaker 1

we don't know how to optimize we know how to optimize over parameters of a neural network we don't know how to optimize with respect to a class of function so what do you mean by optimization over parameters is that i mean we can we can do a gradient descent in the parameter space in space of parameters of a neural network but we can't do gradient descent in the space of a function right we don't know how to search over functions we know how to search over parameters how do we get rid of this problem is that so you translate

### 00:49:28 · Speaker 1

the second door

### 00:49:30 · Speaker 1

Do that represent

### 00:49:37 · Speaker 1

script T which are the family of functions that we are optimizing over via neural networks

### 00:49:55 · Speaker 1

Let's call them T W of X where

### 00:50:01 · Speaker 1

WR the set of parameters the set of

### 00:50:06 · Speaker 1

Means

### 00:50:09 · Speaker 1

I use the word weights and parameters interchangeably weights are parameters of a neural network

### 00:50:23 · Speaker 1

Now with different w values, okay, you will get a different functions Tx, do you agree?

### 00:50:33 · Speaker 1

Because it is represented using a neural network

### 00:50:50 · Speaker 1

Can I ask a question at this moment

### 00:50:54 · Speaker 1

Okay, go on. Sir, we are trying to represent the set functions using neural networks. I'm just trying to understand, let's say, we want to represent a cubic polynomial or a

### 00:51:08 · Speaker 3

a polynomial of nth order then in that case how will we represent it using neural networks

### 00:51:15 · Speaker 1

easy right so now this function uh cubic polynomial right i mean are you talking about a polynomial a vector valued polynomial or a scalar valued polynomial

### 00:51:27 · Speaker 3

Anything, sir.

### 00:51:28 · Speaker 1

Yeah, if it's a scalar value polynomial, then what do you need? So let's say that f of x is equal to ax cubed plus bx squared plus cx plus d, right? Right? Yes. So you build a neural network that will take x as input and give you f of x as output. See, that's what you do in all classification and everything, right?

### 00:51:51 · Speaker 1

Or something

### 00:51:51 · Speaker 3

So like there like if we consider a multi-layer perceptron so we have the weights we have the bias okay

### 00:52:00 · Speaker 1

Yeah

### 00:52:01 · Speaker 3

And then eventually for each layer we have a non-linear activation.

### 00:52:08 · Speaker 4

Okay so I'm trying to understand there like how let's say I want to do x cubed

### 00:52:14 · Speaker 4

So that case how will I do that?

### 00:52:17 · Speaker 1

You can right see that is the regression problem what you are saying is the classical regression problem okay so

### 00:52:29 · Speaker 1

Let's say that your f of x is equal to

### 00:52:40 · Speaker 1

Okay, so what you have is for different values of x, you have f of x. So what you have is, let's say it's an x1, f of x1.

### 00:52:54 · Speaker 1

x2 comma fx2

### 00:52:58 · Speaker 1

And so on you have XN comma of XN this is your data

### 00:53:04 · Speaker 1

Here's what you have you should have this to represent this as a neural network

### 00:53:08 · Speaker 1

So what I do is I will have an MLP

### 00:53:14 · Speaker 1

you take xi as input so it will take xi as input and it will predict f of xi as output

### 00:53:20 · Speaker 1

This is a T predictor

### 00:53:23 · Speaker 1

Now how do I train this neural network this let's call this cap X of theta that's all theta star is equal to

### 00:53:31 · Speaker 1

Really wrong

### 00:53:34 · Speaker 1

We have n samples here, one by n, one through n. I'll take f of f theta of f xi minus f of xi.

### 00:53:47 · Speaker 1

That's all now this is classical neural network training this is solving a regression problem

### 00:53:54 · Speaker 3

got itself

### 00:53:56 · Speaker 1

This is how we are representing this polynomial function in a neural network program

### 00:54:02 · Speaker 1

See that's hard

### 00:54:02 · Speaker 4

So so the presence of non-linearity allows us to also model this non-linear functions right

### 00:54:09 · Speaker 1

Well yeah see okay that is some other dual networks

### 00:54:17 · Speaker 1

The deep neural networks are universal function approximators. That is why they are powerful.

### 00:54:26 · Speaker 1

Okay, now what does this mean? That means that by choosing the weights and the biases and the non-linearity of an MLP, which is deep enough, you can represent any function to arbitrary closeness. That is a known result. That is why the go-to architectures for all machine learning these days are neural networks.

### 00:54:51 · Speaker 1

They're fine

### 00:54:56 · Speaker 1

Okay so I think we should move this

### 00:54:58 · Speaker 4

So I'm not sure if you

### 00:55:00 · Speaker 4

But here we like already know that function should be like T x right like T of x so can you put some restriction on that so that it will no

### 00:55:07 · Speaker 1

No I mean T where is what do we we don't know I don't I understand we don't know anything about T what do we know about T

### 00:55:11 · Speaker 4

Not in one day

### 00:55:18 · Speaker 1

We know nothing about tea

### 00:55:23 · Speaker 1

See in the F-Bergen's case, T is simply a class of functions. What we know is that this T has to be such that it is a solution for the inner optimization problem for all x. But we don't know anything beyond that, no?

### 00:55:40 · Speaker 1

See we want the T to be such that it maximizes whatever is there in the internal bracket that's all

### 00:55:47 · Speaker 1

See, just like we had that regression problem that I had written. So here you are only solving an optimization problem with respect to this T. So T is a neural network. Okay. So I write that.

### 00:55:59 · Speaker 4

But I think we know here like it should be the maximum value right So at least that conditional things can be

### 00:56:05 · Speaker 1

No no hold on you want

### 00:56:08 · Speaker 1

we want see this is an optimization problem that we are solving just okay i erased it it is no different from the problem that i had just written so you had to minimize you had to find a theta such that it minimizes uh the

### 00:56:26 · Speaker 1

Differences between norm of these two functions right That is what we had for the regression problem isn't it

### 00:56:32 · Speaker 4

Yeah

### 00:56:33 · Speaker 1

it this is exactly the same instead of having the differences between the predictions it has some other expectation that's all

### 00:56:42 · Speaker 1

You are trying to maximize see maximization minimization not both I can write this minimization as maximization with a minus here correct

### 00:56:52 · Speaker 1

same thing that is we don't know anything we only know that this neural network has to maximize whatever is there inside okay now i will write that so now i mean i hope that all of you understood what i mean when i say that i will represent this t function via neural network okay now what happens is we will write down so with this

### 00:57:16 · Speaker 1

Oh no we have

### 00:57:22 · Speaker 1

a G theta of C network okay that will take the C and give you X cap

### 00:57:30 · Speaker 1

from P theta okay so maybe we okay a complete as we can write we have another network now neural network

### 00:57:44 · Speaker 1

which is T W of

### 00:57:49 · Speaker 1

x will take x and it will give you the output tw of x

### 00:57:56 · Speaker 1

Instead now there is a particular loss function which is okay let us write that as loss

### 00:58:04 · Speaker 1

It's like not loss but it does cost functions

### 00:58:11 · Speaker 1

equal to

### 00:58:14 · Speaker 1

expectation of

### 00:58:17 · Speaker 1

T of x as x is coming from p theta minus the expectation of f star of t of x

### 00:58:29 · Speaker 1

Next cap is coming from

### 00:58:32 · Speaker 1

If x graph is coming from d theta, now what happens is we need to find the optimal w for this d network such that

### 00:58:46 · Speaker 1

to maximise this cost

### 00:58:50 · Speaker 1

We agree

### 00:58:58 · Speaker 1

of you agree let me just see what what is happening here look at this right we have to find the t network or the t function such that this cost is maximized correct

### 00:59:14 · Speaker 1

All of you with me on this

### 00:59:18 · Speaker 1

Now we want to find theta such that it would minimize the same cost.

### 00:59:29 · Speaker 1

I'm sorry I should not write it as argument and argument, right? Because w star is not the minimum value of the function. It is the minimizer of the function. So it is the argument with respect to all possible w's. And theta has to minimize the exact same cost.

### 00:59:50 · Speaker 3

Sir is the first one is P of Px right instead of P theta the cost

### 00:59:54 · Speaker 1

All right good good thanks

### 01:00:02 · Speaker 1

This is okay. So there is a cost function. Okay. And there are two neural networks here. So one neural network has to maximize that cost. And the other neural network has to minimize that same cost. Now, where is this coming from? You look at this, right? Let me write that down. So basically what is happening is, so we have represented the T function. So first, what happens is that you construct a lower bound on your F divergence.

### 01:00:32 · Speaker 1

Bye man, see you my Ziggy

### 01:00:36 · Speaker 1

Expectation over PX

### 01:00:39 · Speaker 1

minus expectation over p theta so you maximize this with respect to w you get a lower bound on on what on a divergence

### 01:00:52 · Speaker 1

I completely like it so that it is

### 01:01:01 · Speaker 1

an expectation over t of x okay t w of x now right because uh it is parameterized using another neural network now minus is another expectation with respect to p theta of f star of

### 01:01:18 · Speaker 1

of x gram t w of x gram now you optimize this with respect to w you get a t function which is actually a neural network now that would create a lower bound on this thing right solving this

### 01:01:35 · Speaker 1

38

### 01:01:39 · Speaker 1

I don't know about

### 01:01:44 · Speaker 1

On DF

### 01:01:47 · Speaker 1

recall what was happening right so this lower bound is is created by maximizing this now if you choose one t it will create one lower bound do you agree

### 01:01:59 · Speaker 1

One particular p function will create one particular lower bound correct

### 01:02:09 · Speaker 1

also note that the lower bound that we have constructed right on df for a particular theta

### 01:02:23 · Speaker 1

What does that mean? See, look at that, this last function that we are calculating, no, is a function of theta. Why? X cap is a function of theta here.

### 01:02:35 · Speaker 1

Do you see that?

### 01:02:37 · Speaker 1

x cap that we get right depends on theta so it's a function of theta the last function is a function of theta do you agree

### 01:02:49 · Speaker 1

So for a particular theta, okay, maximizing this thing will create one particular lower bound on df.

### 01:03:02 · Speaker 1

Now once you create a lower bound on the F divergence for a particular theta, you want to minimize that lower bound with respect to theta. I don't have space to write it here.

### 01:03:18 · Speaker 1

I bet it

### 01:03:26 · Speaker 1

So this minimisation

### 01:03:32 · Speaker 1

Many measures

### 01:03:37 · Speaker 1

Reminders

### 01:03:40 · Speaker 1

Anyways I still want to vote

### 01:03:46 · Speaker 1

In my cell that lower bound

### 01:03:56 · Speaker 1

that lower bound okay created

### 01:04:01 · Speaker 1

YTW in the previous step

### 01:04:14 · Speaker 1

Do you understand what is happening? So first you you have a d function okay that would create a lower bound at a particular theta. So you start with some random initialization for this d theta okay and then you train this d w network okay you create a lower bound. Now with that lower bound you have to minimize that lower bound right because ultimately the goal is to find a theta that would that is that makes p theta close to p x. Now we are not minimizing the exact

### 01:04:44 · Speaker 1

we are minimizing a lower bound. Once you create a lower bound with a particular tw, we note that after you train this network once, okay, one t function is fixed, created actually. So once you create a particular t function, then there is one lower bound that you have created. Okay, and once you create a lower bound, you train this neural network to find a theta that would minimize that particular lower bound.

### 01:05:14 · Speaker 1

Okay, now once you have minimized that lower bound, you can again come back to this t function and change the t function again, which would create a new lower bound for that new theta that you have learned.

### 01:05:30 · Speaker 1

Do you see what I'm saying

### 01:05:33 · Speaker 1

See the lower bound is created for a particular theta

### 01:05:42 · Speaker 1

you understand now given a theta t will create one particular lower bound now once a lower bound is created you can make it you can tweak your theta in such a way that your p theta gets close to a ps okay now with that p theta changing your t function again will create another lower bound maybe it's tighter this time okay then with that lower bound you go back to theta and you keep alternating

### 01:06:12 · Speaker 1

between these two optimizations

### 01:06:16 · Speaker 1

Do you see do you see the pictures what is happening?

### 01:06:21 · Speaker 1

So I mean again right you know that there are two networks right and by the way this network is is what is famously referred to as

### 01:06:31 · Speaker 1

the generator network

### 01:06:40 · Speaker 1

And this network is referred to as the discriminator or the critique network

### 01:06:55 · Speaker 1

See in the next part of the class, I will give you concrete examples for one F divergence, which is the original CAM formulation and actually show the loss equations and back propagate and all that. Okay. But here I want you to understand the abstract picture that there are basically two functions. You know, why do you have this discriminator network? This discriminator network is simply creating the lower bound on the F divergence. And lower bound itself has a optimization problem that is to be solved, right? Once you solve this,

### 01:07:25 · Speaker 1

either optimization problem with respect to W okay you get a lower bound and for a particular theta and you minimize that lower bound with respect to theta okay so you have gotten a theta that has minimized the lower bound now what is the guarantee that the lower bound that you have constructed is tight or good lower bound so with a theta that is closer to the uh the

### 01:07:52 · Speaker 1

Here you create another title log or mode that you keep alternating between these two

### 01:07:59 · Speaker 1

See these kinds of problems uh I will take questions in a while so suppose you have a loss okay a cost

### 01:08:10 · Speaker 1

So it depends on let's say that this cost depends on

### 01:08:15 · Speaker 1

Two set of parameters

### 01:08:18 · Speaker 1

theta and w okay now what you are doing is you are maximizing the same cost function with respect to w and you are minimizing the same cost function with respect to theta so basically you are seeking the theta star and w star which would simultaneously maximize this loss function and minimize this loss function right so what is actually happening is that imagine that you have a you i mean i can't write it in uh two dimensions

### 01:08:48 · Speaker 1

that is the problem so basically imagine this cost okay let's say that both your theta and w okay theta is one axis here okay and w is another axis and your cost function is

### 01:09:05 · Speaker 1

Something like this okay

### 01:09:12 · Speaker 1

difficult to write that sad anyway so if it's like this now what am i seeking is i am seeking a point right in the theta comma

### 01:09:23 · Speaker 1

W axis, okay, in such a way that if I move

### 01:09:30 · Speaker 1

In in in either of the directions at the theta star the function increases

### 01:09:37 · Speaker 1

If I move in the either directions of w, okay, at that w star, the function decreases.

### 01:09:46 · Speaker 1

you see what is happening there is one function okay uh one cost function which is a function of two set of parameters theta and w now i am seeking the point theta star and w star in the in the parameter space such that if i move on the function around that theta theta star the function value decreases at increases at both the both the directions and if i move uh along the w direction

### 01:10:16 · Speaker 1

At that particular point the function value decreases

### 01:10:22 · Speaker 1

Do you see that

### 01:10:25 · Speaker 1

Okay so these kinds of points right these kinds of points are called saddle points

### 01:10:34 · Speaker 1

because they're like sorts of saddle right i mean you know what saddle is now saddle if you move along one direction at that mean the the function increases if you move along the other direction the function in decreases right that's why it's called saddle points now this sort of an optimization problem right where you are seeking saddle point of a function they are called adverse real optimization that's why the name adverse real

### 01:11:00 · Speaker 1

Yeah adversarial networks

### 01:11:05 · Speaker 1

or those serial problems so because of obvious uh reasons right so this uh uh inner optimization problem right okay is trying to uh maximize whatever you are trying to uh rather the outer optimization problem is trying to minimize the same cost function that you are trying to maximize in the inner optimization problem so in that sense the inner optimization problem

### 01:11:35 · Speaker 1

is quote unquote adversary to the outer optimization problem and vice versa see in mathematical sense you are simply seeking a saddle point so GAN mean the optimal value for the GAN right the optimal parameters for the GAN the optimization problem that you are solving in a GAN is simply a saddle point problem which is that you have the same cost function we know why now right we have the same cost function and we have to maximize that cost function with respect to one set of parameters w and we have to

### 01:12:05 · Speaker 1

We will use the same cost function with another set of parameters theta

### 01:12:10 · Speaker 1

Right. But where did this come from? It came from the fact that we started, see this network, the another T network came because you remember the entire story, please. So you have a divergence metric between P theta and P x, which you would want to minimize. Okay. You could not minimize that. So we constructed a lower bound. The lower bound that we constructed becomes, I mean, is dependent on another class of functions T of x. And we represented those class of functions using another neural network.

### 01:12:40 · Speaker 1

This is why another neural network came into picture

### 01:12:44 · Speaker 1

Okay, see, as you can imagine, I will, I will explain, I mean, don't worry, I will, like, tie all the loose ends in this class. But yeah, see, I mean, just as a side note, you can imagine that once we solve this optimization problem, this discriminative network is of no use. We'll discard it, right? Because our ultimate goal is to give a Z as an input and get an X cap that behaves like PX, right? So this is of no use. This T, T, W network is only to construct the lower bound on the F.

### 01:13:14 · Speaker 1

divergence so that is why it is used during training but during inference or prediction or generation tw network is not at all used we will come to that in a while but anyway so we represented this t function using another class another set of neural networks so every time you get a t fix a tw function you will uh get a lower bound of the other things but to find this tw network there is a maximization problem that you will need to solve okay so this maximization

### 01:13:44 · Speaker 1

probability of solving creates a lower bound on the divergence for a particular theta once you create that you minimize that with respect to theta which is minimize that lower bound which is created by tw in the previous step and you keep alternating between these two so create a lower bound minimize it make that lower bound tighter again come back and minimize it make a create another lower bound try to minimize it and you keep alternating between these two so till a point where do you stop this you stop at a point where i mean

### 01:14:14 · Speaker 1

you stop gan optimization is a question that is uh that's not well answered i will answer that in the next half of the class but yeah so this is how you you uh you do an optimization in that i mean that is why it's called an oz real problem because you have the same cost function that is being maximized with respect to one set of parameters and you are minimizing the same with respect to another set of parameters

### 01:14:38 · Speaker 1

Okay, so I will stop here and take some questions and then we will break for a short break and then we'll come back and I'll make it much more implementation friendly and I'll take an example for the M5 versions and we will go to that basic GAN paper, right, which happens to be a special case of this. Okay, I have questions here. I'm sure there will be many.

### 01:15:04 · Speaker 1

Please raise your hands if you have questions

### 01:15:13 · Speaker 1

A lot of people raised their raised their hands when I was explaining did I explain it in such a way that your questions are all answered

### 01:15:20 · Speaker 1

It's good to know. Okay uh yeah

### 01:15:27 · Speaker 4

So what are what would be the dimension of this T w of x? You have shown it as a narrowing, right?

### 01:15:32 · Speaker 1

Yeah, yeah, yeah. Yeah, that's a good question. Depends on the f function that you have chosen. For the knife, when your f function happens to be such that it is the underlying divergence is Jensen-Chandler divergence, no? That happens to be a scalar, which could be interpreted as a classifier. I will show that in the next half of the class. That depends on f function, no? Because if you recall the definition of our t function from the previous class,

### 01:16:02 · Speaker 1

What was t function? t function takes x and gives out values from the domain of f star. So whatever f star you choose, f function that you choose, this t depends on the choice of f divergence that you have made. See that is why, now that you asked that question, it is very relevant. See if you choose your f2b Jensen channel divergence, this discriminator network will take x and give you values between 0 and 1.

### 01:16:32 · Speaker 1

If you choose your f divergence to be what is called as chi square distance, I mean choose your f in such a way, then your T W network will become a regressor, which means that the output of your T W network will be a real number. And that is why you know different f functions will give you different instantiations of GAN. So there is this L S GAN, least square GAN, which is just using an f function which corresponds to the chi square distance. The ninth GAN is when you choose your f function such that your f double

### 01:17:02 · Speaker 1

is Jensen Shannon divergence so if you choose it to be total variation distance then it becomes TV Garam

### 01:17:10 · Speaker 1

So see what I have done, I mean, for you, if you, if you people can appreciate, see when you write a class in object oriented setting, write the constructor of a class now, that is what I have done now.

### 01:17:23 · Speaker 1

Okay, so all these GANs are simply instantiations of this class.

### 01:17:29 · Speaker 1

if you can if you can see the analogy so what we have done is just constructed the family of giants so each of the thing would be an instantiation of it okay

### 01:17:41 · Speaker 1

Yeah uh thank you and yeah and Rajit

### 01:17:41 · Speaker 4

Uh thank you

### 01:17:45 · Speaker 3

Yes, the difference or the cost we are maximizing is the difference between random or okay X and X hat, right?

### 01:17:55 · Speaker 1

a difference between two expectations

### 01:17:58 · Speaker 3

No but X hat is the

### 01:18:02 · Speaker 1

The output of the out out X hat is the output of the G theta network X is the data

### 01:18:08 · Speaker 3

Yes so we are taking the difference between these two the difference by us no

### 01:18:12 · Speaker 1

We are taking no hold on hold p precise we are not taking difference between the data points we are taking the difference between expectations of t functions and f star of t functions where these x star and x comes from the corresponding distributions that is what it is we are not taking x minus x cap here we are taking the difference between the expectations of tx and f star of tx cap as x and x cap are coming from px and p theta

### 01:18:44 · Speaker 1

You see that the cost function is difference in expectations not difference in data points

### 01:18:51 · Speaker 3

Yeah that's correct so that's the difference between averages right

### 01:18:55 · Speaker 1

Difference between averages of not x and x cap again. Difference between the averages of Tx as x is coming from Px and F star of Tx as x cap is coming from Px.

### 01:19:11 · Speaker 1

It is again not the average of x it is average of p x

### 01:19:16 · Speaker 1

It is not average of x cap it is the average of s f star of t of x cap

### 01:19:24 · Speaker 1

Is that okay

### 01:19:25 · Speaker 3

Yeah and then this cost or the maximum maximization should not be equal to minimization which we are doing over theta.

### 01:19:35 · Speaker 1

I didn't follow the question

### 01:19:38 · Speaker 3

First we are maximizing the this difference right

### 01:19:43 · Speaker 3

And then we are minimizing the same

### 01:19:46 · Speaker 1

So you should realize that maximization is with respect to different set of parameters and minimization is with respect to another set of parameters.

### 01:19:57 · Speaker 1

The cost function is the same but maximization is with respect to w minimization is with respect to theta

### 01:20:04 · Speaker 3

So when we minimize maximize with respect to w are we not changing theta in any way

### 01:20:09 · Speaker 1

No no

### 01:20:11 · Speaker 1

That is why I said no it's for a fixed data. So you alternate between those two.

### 01:20:16 · Speaker 1

So I will also show the you know the way the gradients flow in both of these in the next half of the class that is what I will do. I will put out a particular f function and I will write down the gradients and also write the gradient descent equations which you would have to implement in your in your assignments okay. By the way you will all be implementing all this that is the that is what you will do in this in your assignment so that there is absolutely no gap between the maths that we have done and the implementation that you do okay.

### 01:20:47 · Speaker 1

Okay, uh, okay, uh, astic

### 01:20:52 · Speaker 4

Yeah so so you mentioned that we are maximizing and minimizing the same cost function

### 01:20:57 · Speaker 1

But but but but with respect to t two different set of parameters yeah

### 01:20:57 · Speaker 4

That's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's that's

### 01:21:02 · Speaker 4

Yeah yeah yeah so uh it is uh sequentially or at the same time it should be sequentially

### 01:21:07 · Speaker 1

It is sequence you know alternate

### 01:21:09 · Speaker 4

Okay okay okay and first we are maximizing

### 01:21:12 · Speaker 2

Then for that fixed value then

### 01:21:13 · Speaker 1

And it's

### 01:21:13 · Speaker 4

Fixed value then we are again minimizing it for

### 01:21:16 · Speaker 1

Yes the order does not matter because you start from something and then you alternate between them no Okay yeah that makes sense

### 01:21:18 · Speaker 4

The order

### 01:21:23 · Speaker 4

Okay yeah that makes sense

### 01:21:24 · Speaker 1

Or order does not matter

### 01:21:26 · Speaker 4

Mm yeah

### 01:21:30 · Speaker 1

13

### 01:21:39 · Speaker 1

It's a two set of weights and weights correct

### 01:21:46 · Speaker 1

There are two neural networks one one's one neural network I've called as W the other parameters I've represented as theta

### 01:21:59 · Speaker 1

Ah correct both of them are like backpropagations only. Both the maximise of course no both the optimizations are sort of using backpropagation only.

### 01:22:13 · Speaker 4

for one given w that you maximize the cost and then for theta you minimize so like do we compare for all different w's

### 01:22:25 · Speaker 1

no different w now you are doing just gradient descent see one one iteration through uh tw and you get a w you get a lower bound now you get another you do one iteration through g network you get theta right then you come back with that fixed theta the cost function changes now see once you change theta the cost function changes

### 01:22:48 · Speaker 2

Um yeah okay

### 01:22:49 · Speaker 1

Now you come back to your W network, tweak your W again. And now the cost function has again changed. Go back to your theta network, change your theta and keep alternating between those two.

### 01:23:03 · Speaker 1

See mathematically what is happening is that the moment you have a particular T that is fixed no there is a lower bound that gets fixed but that lower bound need not be tight.

### 01:23:17 · Speaker 1

The door door door need not be typed okay so maybe if you want I thought I would do it at the end okay let me let me save that for the end okay because that's there is one picture that I write

### 01:23:28 · Speaker 3

Oh

### 01:23:35 · Speaker 1

please mute that okay see uh there is one picture that i write okay of what is happening uh alternatively uh that would give you i mean that would actually tell you a lot of story but that can that i can write only when your t function happens to be a classifier in the case where your f is jets and and divergence i will do that i will do that in this class at the end of the class it will you'll get much more clarity as we move on okay

### 01:24:03 · Speaker 1

Okay

### 01:24:06 · Speaker 1

Any any other questions

### 01:24:09 · Speaker 3

Yeah sorry

### 01:24:10 · Speaker 1

Yeah yeah so she

### 01:24:10 · Speaker 3

Yeah so she maximized yeah so I

### 01:24:28 · Speaker 1

X cap no X cap is coming from d theta

### 01:24:33 · Speaker 1

scan

### 01:24:37 · Speaker 1

Next cap is coming from G theta no

### 01:24:45 · Speaker 1

Okay uh another question okay yeah

### 01:24:46 · Speaker 3

Another question, okay, yeah. When do we stop? Because I told you.

### 01:24:50 · Speaker 1

The I I told you no I I told you I I I will tell you this topic criteria next in the next half of the class

### 01:25:00 · Speaker 1

So okay, we'll take a break. I think I've been here since nine. So take a 15 minutes break. It is 11.10 in my clock. Shall we come back at 11.20, 11.25?

### 01:25:18 · Speaker 1

11 30 we come back at 11 30 we'll only have 45 minutes okay 11 30 is also fine okay 11 30 we'll come back as there's another yeah people can leave but interesting now there is uh abhishek are you there

### 01:25:38 · Speaker 1

Okay I think he's not there yeah this uh his name in his name in his name and my name mean the same by the way okay

### 01:25:50 · Speaker 1

In Sanskrit, right, the word tosh represents happiness. And any prefix that you add to it is just qualifying that. So sum is a prefix that would qualify that. It says, you know, exalted happiness. So santosh is, of course, you know what that means, right? So pra is another suffix in Sanskrit that would have the same meaning. That's my name. And avitosh is one other thing. So, yeah. I was looking at his name and then...

### 01:26:20 · Speaker 1

got this thought and thought to share you but share with you the person is not around anyway doesn't matter

### 01:26:25 · Speaker 3

Or opposite or same

### 01:26:28 · Speaker 1

No no same thing all these convey like magnification of whatever you are saying

### 01:26:36 · Speaker 1

So, Tosh is happiness. Tosh, Avritosh, Pratosh, all these they mean the same. You might have also heard this name of Ashutosh, no? Yeah. Ashu means quick. So, that's why the Shiva is called Ashutosh, somebody who gets happy very quickly. So, that is just a little different. But Avritosh, Santosh, Pratosh, all these mean the Paritosh. I am not Paritosh, by the way. My name is Pratosh.

### 01:27:08 · Speaker 1

It seems

### 01:27:08 · Speaker 4

Seems like too many happy people in the team

### 01:27:12 · Speaker 1

I always tell my parents that it's a Mishnah and my name is

### 01:27:19 · Speaker 1

So I don't know how happy I am in my life, but yeah, they named me happiness. And what's more interesting is when my parents named me, they didn't know what my name means. Somebody suggested and it looked unique and they just chose that name. So then, you know, I don't know if how many of you know that. I also happen to be interested in Sanskrit and Indian history philosophy.

### 01:27:49 · Speaker 1

So studying Sanskrit for a long time then I realized what the meaning of my name is

### 01:27:56 · Speaker 1

Anyways

### 01:27:56 · Speaker 4

On a different note I think uh

### 01:27:59 · Speaker 1

Hey hold on hold on hold on see we are we are we are in the break people can leave this is all not in an unrelated stuff but yeah so go on whoever wants to say

### 01:28:09 · Speaker 4

Yeah, uh, so actually I think uh, you remembered in the Sangaskrit club as well, right? So I thought uh, there will be some way of teaching from the scratch. Uh, that was my interest point to join that.

### 01:28:09 · Speaker 1

It's actually

### 01:28:21 · Speaker 4

So is that a

### 01:28:21 · Speaker 1

I am not an active member there I mean it is mostly it is mostly like headed by Sankirtan and Shankarama and these people I don't have a lot of say see when I was in IIT Delhi I used to teach Sanskrit to people like like undergrads there that was my here I have too much then I didn't have a family no I have two children and you know

### 01:28:51 · Speaker 4

Sir sir sir what is the thing like you resigned from IIT Delhi and came to IAC

### 01:29:00 · Speaker 4

I mean why you reside from IIT Delhi

### 01:29:03 · Speaker 1

Because Bangalore is my home I'm a South Indian guy and Uttna Garmi or Tantakom I say I am

### 01:29:12 · Speaker 1

In fact that's actually yeah that's I mean come on right I mean say here anything more than 30 is hot for us and anything less than 20 is cold for us and uh it was too much

### 01:29:32 · Speaker 2

Yeah correct

### 01:29:32 · Speaker 1

That's that's the only reason otherwise I was very happy at Delhi. Professionally there was there was absolutely no problem and I like see when I went to Delhi I I thought that I would you know I would want to come back as soon as possible in fact because you asked when I was applying for faculty positions I applied to Bombay Madras Delhi okay uh i i could not apply to isc because i did my phd from isc only no they will not take their own students

### 01:30:02 · Speaker 1

Unless they go out some for some years and come back

### 01:30:06 · Speaker 1

Now that option was not there. I applied to Bombay, Madras, Delhi and my preference was, of course, first preference was Madras and then it's Bombay, then you move up the map, right? But the first offer was made from IIT Delhi.

### 01:30:21 · Speaker 4

But you for your PSD you've done PSD right sir

### 01:30:25 · Speaker 1

Otherwise you can't become faculty in any of these places

### 01:30:28 · Speaker 4

So from where you did this business

### 01:30:31 · Speaker 1

So only I see only

### 01:30:33 · Speaker 4

Oh I yes it said

### 01:30:34 · Speaker 1

Yeah, so like 10 years back, 15 years back I was a student at IIT. So, Silya forcefully I went to Delhi, but what I was saying is when I went to Delhi, I started liking it. I mean, some of my colleagues at Delhi told me that Delhi will grow on you, you will start missing Delhi and all that. I never thought I would miss Delhi, but Agni, I miss Delhi because there are lots of good things about Delhi which is not there in Bangalore. Bangalore is, it's a doomed

### 01:31:04 · Speaker 1

place and infrastructure is so bad and even though I come from technically I'm not from Bangalore I'm from a place called Mysore which is 150 kilometers away from my Bangalore which is heaven yeah but this Bangalore is hell

### 01:31:17 · Speaker 4

Just so I know

### 01:31:21 · Speaker 1

I mean all broken infrastructure rude people right you know what I felt people in Delhi more more softer compared to people in Bangalore everybody says that North Indians are harsh or nothing but I mean after Hindi we were talking about that that's all the moment you start speaking in Hindi and people are people are more cosmopolitan and more softer there my God

### 01:31:51 · Speaker 1

Dreadful when I see auto drivers and all the other people here okay this is getting recorded don't put it on some social media right I mean I see professors make some comments on

### 01:32:03 · Speaker 4

I think so

### 01:32:05 · Speaker 1

So these days you can you cannot have a casual conversation with people right they will record and put it on social media it will become a national news

### 01:32:13 · Speaker 1

See

### 01:32:14 · Speaker 4

should not go on fly side definitely

### 01:32:16 · Speaker 1

I tell you, I mean, I just some two, three months back, I gave a talk somewhere, okay? Something on philosophy, somebody called me and I gave a talk. I mean, when I was giving a talk, I never knew that, okay, they were recording this and all that. These people have recorded and put it on YouTube. I mean, this thing has become a big thing, right? People are tweeting it, right, left and center. There are views for it, against it and all that. Then I had to contact these organizers of the talk and ask

### 01:32:46 · Speaker 1

to put a disclaimer saying that the expressions all the expressions are opinions are of the author and has nothing to do with isc these people have put it online no they have they have used my affiliation they have called it oh isc professor says this i mean which is true because i am a professor from isc but my that those are my views not my university's views some of them can some of them may be politically correct some of them are not politically correct and yeah that might cause

### 01:33:16 · Speaker 1

my job also so it's very should be very very careful when you talk

### 01:33:21 · Speaker 4

I think that when you start the classes you should put the same disclaimer

### 01:33:27 · Speaker 1

No no no this is okay no this is all technical content This is all like you know this is all standard stuff you can quote me saying oh YAC professor said that GAN solves a hadden point problem no problem right

### 01:33:42 · Speaker 1

I have no problem with it. No IISc professor said that you train a neural network using back propagation. Nobody cares. It is true. Now now if I start making statements like okay you know statements regarding some history, philosophy, language, some sensitive issues. If you quote me on that and if you tag IISc's name there it's not correct no. It's all my opinion and I am entitled to have my having my opinion but I should not be as a government employee I should not be having opinions that

### 01:34:12 · Speaker 1

But I should rather not make my opinions public. See you saw what happened no recently our Prime Minister went to CGI's home for a festival and it became a big national news.

### 01:34:21 · Speaker 3

That's the

### 01:34:24 · Speaker 3

So there is a video of you sir where you're explaining Ahambra Masmi from sacred games

### 01:34:30 · Speaker 1

Yeah that's what I'm saying

### 01:34:31 · Speaker 4

So so on the same same lines I saw your video on the video

### 01:34:34 · Speaker 1

No no that's a that's a that's a rabbit hole please don't start that okay so let me stop

### 01:34:42 · Speaker 4

So I I want to like ask you like how like how
