---
id: uQvtdAPjKqI
title: Lec 3 - Deep Generative Models Intro to Generative Modelling
url: https://www.youtube.com/watch?v=uQvtdAPjKqI
date: '2024-11-23'
duration: 03:10:10
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# Lec 3 - Deep Generative Models Intro to Generative Modelling

## Transcript

### 00:00:02 · Speaker 1

putting here

### 00:00:04 · Speaker 1

Uh yeah so just a couple of logistics things um

### 00:00:11 · Speaker 1

We will start the tutorial from tomorrow I think you have should have got a calendar invite and then I should have sent you right

### 00:00:22 · Speaker 1

So if if you people have time so please join the tutorial otherwise you can access it later and we will we will start the quizzes from next to next week okay so which means like the second Saturday from today today is 31st of last week Wednesday

### 00:00:48 · Speaker 1

Next to next Saturday

### 00:00:51 · Speaker 2

Fourteen I will leave

### 00:00:53 · Speaker 1

Yeah

### 00:00:55 · Speaker 1

We will have our first quiz on 14th hmm

### 00:01:00 · Speaker 1

Okay

### 00:01:01 · Speaker 2

Uh sir can we have the tutorial either on Saturday evening or any of the weekday evenings Sunday is not the weekend thing

### 00:01:06 · Speaker 1

And this is

### 00:01:10 · Speaker 1

See that right that please talk to coordinate with the TA because I believe that he had a He had a poll or something did he

### 00:01:23 · Speaker 2

North

### 00:01:27 · Speaker 1

Didn't he

### 00:01:27 · Speaker 2

No I I think we didn't got it

### 00:01:32 · Speaker 1

Surprising let me just call him right away and just to little data just give me a minute

### 00:01:40 · Speaker 2

So there was a poll actually there was a poll in that channel yeah yeah there's a poll in the channel

### 00:01:45 · Speaker 1

And they supply

### 00:01:47 · Speaker 1

Then okay right I mean I think the how how how when it came actually or in the in the chat window or

### 00:01:56 · Speaker 2

No in the channels in the general of this channel there is a poll

### 00:02:03 · Speaker 1

Oh okay

### 00:02:13 · Speaker 1

Yeah so so then it's fine right it was was uh decided based on the outcome of that poll I suppose right

### 00:02:22 · Speaker 4

There were only 30

### 00:02:30 · Speaker 1

Okay, what can we do? Okay, so let me ask him to have another poll perhaps and then decide just a second let me call him.

### 00:03:08 · Speaker 4

I will carry my little toy with you

### 00:03:12 · Speaker 1

He's not picking it up let I he'll call back once he calls back I'll tell him

### 00:03:19 · Speaker 1

Yeah I uh

### 00:03:23 · Speaker 1

I mean it's very difficult to find the time that is convenient for like all hundred people in the class okay so I mean we have to do something um so yeah so whatever works for most of the people we'll have to stick to that so I'll ask him to have the poll again

### 00:03:43 · Speaker 1

And then we can decide okay where is this thing at here

### 00:03:50 · Speaker 1

You see my screen

### 00:03:54 · Speaker 2

Not yet

### 00:03:58 · Speaker 1

This says it is being shared

### 00:04:11 · Speaker 1

Oh it says it has been shared here how come

### 00:04:15 · Speaker 1

Really John

### 00:04:34 · Speaker 1

Uh

### 00:04:39 · Speaker 1

Yeah tell me

### 00:04:46 · Speaker 1

Please go on somebody go ahead

### 00:04:51 · Speaker 4

Yes

### 00:04:53 · Speaker 1

Dr Telli me

### 00:04:55 · Speaker 4

Yeah we are able to see it

### 00:05:08 · Speaker 1

Okay shall we start

### 00:05:13 · Speaker 1

Oh, good. Yeah. So a little bit of recap before we continue with today's content.

### 00:05:26 · Speaker 1

Yeah so we were looking at the relevant probability theory stuff right so we have the probability triplet which is the sample space the event space and probability measure and we define this function called random variable that would give you this push forward measure right yeah so then we said that once you have this function called random variable that will move the sample space to some d-dimensional real numbers and

### 00:05:56 · Speaker 1

subsets of real numbers and then you have the

### 00:06:02 · Speaker 1

corresponding measure probability measure that gets translated into the real space which we call the distribution function

### 00:06:11 · Speaker 1

Right and we looked at some of the properties of what distribution functions are and looked at multiple random variables conditional random variables independence

### 00:06:23 · Speaker 1

and joint random variables and so on okay

### 00:06:31 · Speaker 1

Uh uh before I go to the supervised learning part machine learning part any questions on the

### 00:06:41 · Speaker 1

Probability theory part

### 00:06:54 · Speaker 1

second I have to open that yeah okay yeah go on searching

### 00:07:01 · Speaker 2

question from last lecture so

### 00:07:04 · Speaker 2

that boreal sigma algebra so we just last week studied that in recent process class

### 00:07:09 · Speaker 1

I'm closing

### 00:07:10 · Speaker 2

Uh zero to one and

### 00:07:15 · Speaker 2

just asking for this

### 00:07:18 · Speaker 2

problem you mentioned this sig borel sigma algebra is defined on minus infinity to infinity or like it is always on

### 00:07:25 · Speaker 1

See sigma borel sigma algebra for the real numbers right they are defined on real sets

### 00:07:39 · Speaker 1

Oh I think I've confused right why is it between zero and one I

### 00:07:44 · Speaker 2

No no he just gave an example

### 00:07:46 · Speaker 4

That's all

### 00:07:48 · Speaker 1

So you can take any set and generate

### 00:07:48 · Speaker 4

So you can take any set and generate

### 00:07:53 · Speaker 1

Yeah you can you can take any set and generate a sigma algebra on top of that right

### 00:08:00 · Speaker 1

Uh but specifically Boolean Sigma algebras are defined on L numbers right

### 00:08:06 · Speaker 2

Yeah

### 00:08:10 · Speaker 1

Yeah small h sigma algebra on R that contains all the intervals that are possible that is the full sigma algebra yeah

### 00:08:18 · Speaker 1

See that is why I did not even take the I mean to define borel sigma algebra right I said like r rd and subsets of rd and then you have the distribution function on top of it right

### 00:08:40 · Speaker 1

Uh it's more anything else uh

### 00:08:50 · Speaker 1

But in such thing who is teaching random process is Aditya teaching it

### 00:08:55 · Speaker 4

Yes sir I did take a balance

### 00:08:58 · Speaker 1

Yeah, we are very good friends. Yeah. Okay. So with that, we will look at what supervised machine learning is. I said that the data, right, is defined as some n samples, okay, that are drawn. Yeah, that is what I know. The notation is that you have data sampled from a particular distribution or data drawn from a distribution. Yeah.

### 00:09:28 · Speaker 1

actually boils down to saying that every data point that we have is an element from the range space of a random variable that we have that is x okay i mean that we denote by x so we this implies that there exists an underlying probability measure and does the distribution function induced by x okay so this is clear right so whenever we say that we have n data points we actually mean that we are sampling i mean we have n uh

### 00:09:58 · Speaker 1

vectors from the range space of the random variable once we talk of the range space of the random variable uh we uh we we understand that uh there has been uh I mean there is an underlying measure space the underlying the sample space that is there and a probability measure and therefore a distribution function induced by x okay

### 00:10:24 · Speaker 1

Now for the so-called supervised learning what happens is that you have data sampled from the joint distribution of a pair of random variables x and y

### 00:10:38 · Speaker 1

where x denotes a random variable whose range space is some rd i mean i gave the example of m n straight where it is r 784 dimensions because the images are in 28 cross 28 pixels and y which is the it is another random variable that we are talking of denotes the labels so-called labels and there exists two sample spaces right uh or

### 00:11:08 · Speaker 1

Yeah, so two sample spaces whose cross product is what we are talking about when we talk of joint distributions. And when we say data, this is what we mean, right? We have

### 00:11:21 · Speaker 1

Basically, right, in other words, what we are saying is obtaining data is equivalent to conducting the underlying random experiment that generated your sample space multiple times. That's what it means, right? We have conducted the we have we are actually running the running the random experiment multiple times. We are making multiple trials, right? And each of the trial gives rise to some sort of an outcome. Okay. And that outcome

### 00:11:51 · Speaker 1

gets mapped to some d dimensional real space via random variable and because we are looking at a random experiment there is a there is a probability measure that we have assigned and because we have since we have a random process sorry random variable i'm sorry excuse me because we have since we have a random variable um you have uh i mean the the outcomes of these experiments have been converted into something measurable that is a d dimensional real number

### 00:12:21 · Speaker 1

That is what is happening. Is this world view clear? See from now on, right, I will not tell you that these are actually vectors in the range space of a random variable which is a function and you have the underlying measure and you have the distribution, etc. I will simply say that we are given a data from an underlying distribution. That's all. So you should understand what I mean when I say that. Is this clear?

### 00:12:47 · Speaker 1

Any questions on this?

### 00:12:52 · Speaker 1

Okay, so now let us start with the definitions.

### 00:12:58 · Speaker 1

Asters

### 00:13:01 · Speaker 1

Whatever it is

### 00:13:04 · Speaker 1

Oh I don't know what this is okay

### 00:13:06 · Speaker 2

Sir you need to select a plus page

### 00:13:11 · Speaker 2

in the third column

### 00:13:12 · Speaker 1

Speech

### 00:13:15 · Speaker 1

Okay

### 00:13:15 · Speaker 2

Then you can mention the titles

### 00:13:32 · Speaker 1

We will also putting lecture numbers right L3

### 00:14:13 · Speaker 1

So, we will mostly set up the problem today, right? What are what is the generative modeling problem and so on. Okay. So, that is what the major focus of today's lecture is.

### 00:14:26 · Speaker 1

Now let us start with

### 00:14:35 · Speaker 1

data so this is our input right means this is the say I always represent data with

### 00:14:45 · Speaker 1

set so it is either so let us first maybe

### 00:14:53 · Speaker 1

set up supervised machine learning actually right at a at a core level there isn't a lot of difference between supervised and unsupervised machine learning i will tell you why it is

### 00:15:15 · Speaker 1

Will it be comprehends

### 00:15:19 · Speaker 1

From a comprehensive standpoint will it be better to introduce

### 00:15:30 · Speaker 1

Can all of you mute please let me do that

### 00:15:43 · Speaker 1

So let me introduce uh

### 00:15:48 · Speaker 1

in general then we will talk of the differences of data so let's say that you have data data is of this form x1 x2

### 00:16:00 · Speaker 1

XM

### 00:16:03 · Speaker 1

Make it a little abstract from now on xn and these has been drawn from some

### 00:16:13 · Speaker 1

underlying distribution px and this is unknown so this is the setting right

### 00:16:19 · Speaker 1

No

### 00:16:23 · Speaker 1

This actually means that

### 00:16:28 · Speaker 1

This keeps happening

### 00:16:58 · Speaker 1

I keep my palm over the screen right it just gets distorted I don't know how to control it let me know if somebody knows how to do that anyway so the this is thing that we have data that is drawn from an unknown distribution it actually means that see this is the central problem of machine learning that data

### 00:17:19 · Speaker 1

on

### 00:17:23 · Speaker 1

Pump boost

### 00:17:28 · Speaker 1

unknown distribution okay

### 00:17:36 · Speaker 1

Okay, so this actually means that the distribution is unknown, but we have samples from it. So this is the the central problem of machine learning in arm statistics that you have samples from a distribution, but you don't know what the underlying distribution is. Okay, so now the question that we ask the for the question the central question that is asked in ML is the following that

### 00:18:06 · Speaker 1

Give one

### 00:18:08 · Speaker 1

Samples from a distribution

### 00:18:18 · Speaker 1

distribution okay

### 00:18:22 · Speaker 1

Estimate the distribution

### 00:18:29 · Speaker 1

estimate the underlying distribution

### 00:18:35 · Speaker 1

So this happens to be a central question in ML that if you have if you are given samples from a distribution can you estimate the underlying distribution

### 00:18:47 · Speaker 1

Okay, now why is this important? You understand the question, right? There are two different things. Having samples from a distribution is different from knowing the distribution itself. Can you see the difference?

### 00:19:03 · Speaker 1

Can all of you see this difference? This is very very important okay

### 00:19:08 · Speaker 1

So now, so the question is if you if you are given some samples from the distributions, you have to under estimate the underlying distribution. So why is this of importance is the question. Okay. The the thing is.

### 00:19:30 · Speaker 1

This is important because now let me write that down

### 00:19:37 · Speaker 1

Knowing the distribution

### 00:19:50 · Speaker 1

Rabbits

### 00:19:52 · Speaker 1

prediction

### 00:19:57 · Speaker 1

Section slash sampling

### 00:20:05 · Speaker 1

Okay, this is the claim. So if you know the distribution, okay, you can do prediction and you can do sampling. So now what do you mean by prediction and sampling is that see in supervised machine learning, the problem is that of prediction. And in unsupervised machine learning, mostly the problem is of sampling. All right, in generative models, the problem is of sampling. Now to do both.

### 00:20:35 · Speaker 1

request all of you to kindly mute yourself okay uh so unmuting with some noise will just cause some disturbance thank you yeah so knowing the disturbance

### 00:20:48 · Speaker 1

knowing the distribution enables prediction and sampling okay now what do i mean by this is the question so now let's say that you have

### 00:21:06 · Speaker 1

Let's take some examples

### 00:21:13 · Speaker 1

example may be that so given

### 00:21:18 · Speaker 1

It pairs off

### 00:21:25 · Speaker 1

images and labels

### 00:21:37 · Speaker 1

I'll put it in quotes because I'm not defined this yet learn to

### 00:21:41 · Speaker 1

predict

### 00:21:45 · Speaker 1

the so learn to predict the labels of unseen images

### 00:21:57 · Speaker 1

This is the classical classification problem. Given pairs of images and labels in terms of data, learn to predict labels of unseen images. So now my claim is that you can model this in the language that we have just said. So now we would say that the data that has been given us is following that you have

### 00:22:18 · Speaker 1

pairs of x and y. So note that whenever I write this, I mean that there is there are two random variables that are there and the data has been drawn from an unknown joint distribution between x and y. Right. So this is given pairs of images of given the pairs of images and labels. Now, how do you define this? Learn to predict part of it. Okay. So now prediction is defined as the following.

### 00:22:52 · Speaker 1

Prediction is defined to be evaluate

### 00:22:57 · Speaker 1

Evaluate

### 00:23:08 · Speaker 1

likelihood

### 00:23:22 · Speaker 1

of label

### 00:23:28 · Speaker 1

You want

### 00:23:30 · Speaker 1

image

### 00:23:33 · Speaker 1

This is the definition of prediction problem. I will define what likelihood is, okay? Now we'll have to define likelihood, right? So likelihood

### 00:23:45 · Speaker 1

Okay likelihood of

### 00:23:51 · Speaker 1

This is a very important terminology likelihood of a of a point

### 00:24:00 · Speaker 1

is defined to be

### 00:24:03 · Speaker 1

Value

### 00:24:06 · Speaker 1

of the density function

### 00:24:15 · Speaker 1

This has x uh x cap okay, density function evaluated.

### 00:24:24 · Speaker 1

x square so this is the definition of the like the likelihood so note that i am not calling it a probability because i am evaluating the density function remember last class i told you that evaluating the density function of a continuous random variable will not give you the probability right so that is why

### 00:24:45 · Speaker 1

I am defining likelihood of a point as the value of the density function evaluated at x okay at some point x this means that

### 00:24:55 · Speaker 1

Suppose you have a point, you know, suppose there is some x cap that is in some rt, okay, and px is a density function.

### 00:25:12 · Speaker 1

density function then

### 00:25:15 · Speaker 1

The likelihood of X cap is simply the density function evaluated at X cap

### 00:25:24 · Speaker 1

Is this clear

### 00:25:27 · Speaker 1

Please note the the notations here whenever I talk of distribution functions right I write this script P you know double line P whenever I write the density functions I write small p okay and in most of the rest of the part of this course we will work with density functions not the distribution functions okay because simply because they are easy to work with okay and remember the connection between the density function and distribution functions right distribution functions are valid

### 00:25:57 · Speaker 1

probability measures okay and the derivative of the distribution functions are what are called as the density functions density functions evaluated at a particular point will not give you probabilities but density functions integrated over a range will give you probabilities because that would be the distribution function evaluated at a particular point all this is clear right

### 00:26:26 · Speaker 1

Just repeating what we did in the last class. Okay great. So now likelihood whenever

### 00:26:30 · Speaker 3

Yeah

### 00:26:31 · Speaker 1

Yes go on

### 00:26:32 · Speaker 3

So you mean to say that the likelihood function is the same as the probability density function

### 00:26:37 · Speaker 1

I am defining the likelihood as the density function evaluated at the likelihood at a point is equal to the density function evaluated at that point.

### 00:26:52 · Speaker 1

Actually definition of likelihood see whenever we talk of likelihoods right the definition is that it is the density function evaluated at that particular point. Now if the underlying random variable happens to be a discrete random variable then evaluating density function becomes mass function and evaluating the mass function at a point will actually give you probability right. But in general because we are looking at continuous random variables density functions are not probabilities that's why I don't want to call likelihood as probability of that particular point because it does not

### 00:27:22 · Speaker 1

mean anything I would just want to define likelihood as evaluating or likelihood of a point is simply the value of the density function evaluated at that point and as we saw in the previous class density function of a continuous random variable evaluated at a particular point can be more than 1 okay can can have values more than 1 and it does not correspond to a probability this much is clear right

### 00:27:52 · Speaker 1

Okay, now with the definition of likelihood function, we'll have to define what prediction is. Now I said prediction is simply evaluating the likelihood of the labels given any way, okay? Which implies that this implies that prediction

### 00:28:11 · Speaker 1

is defined the following that

### 00:28:16 · Speaker 1

But evaluate

### 00:28:20 · Speaker 1

The conditional density

### 00:28:33 · Speaker 1

X cap we'll have to say prediction at X cap right

### 00:28:45 · Speaker 1

Prediction at XCAT

### 00:28:48 · Speaker 1

is evaluating the conditional density at x cap so what does that mean so suppose or assume

### 00:28:57 · Speaker 1

of

### 00:29:01 · Speaker 1

Y given X denote

### 00:29:06 · Speaker 1

The conditional density function

### 00:29:17 · Speaker 1

y given x. See note that whenever there is a density function there is an underlying distribution function and I am talking of conditional probabilities here. Let p y given x denote the conditional density function of y given x. Then

### 00:29:33 · Speaker 1

Prediction

### 00:29:38 · Speaker 1

but x square is simply equal to evaluating this density function okay but

### 00:29:50 · Speaker 1

Okay I will explain my notation and I will okay

### 00:29:59 · Speaker 1

X is equal to x cap

### 00:30:02 · Speaker 1

okay uh i will explain okay let me explain the the notation first see when i write the rotational note

### 00:30:18 · Speaker 1

P of y given x

### 00:30:25 · Speaker 1

Then what's the following So y given x

### 00:30:33 · Speaker 1

the subscript here

### 00:30:41 · Speaker 1

Denotes

### 00:30:52 · Speaker 1

random variables okay whenever i write the density function or any distribution function anything right subscript always denotes the random variables

### 00:31:01 · Speaker 1

This which is

### 00:31:07 · Speaker 1

Whatever I write inside the parentheses right denotes

### 00:31:14 · Speaker 1

value

### 00:31:19 · Speaker 1

which the function is being evaluated

### 00:31:32 · Speaker 1

Okay, is this clear? This is the notation. See, whenever I write conditional distributions, right, I always mean that the conditioned random variable, right, is fixed at some particular value.

### 00:31:48 · Speaker 1

See this is the definition of conditional distribution that when I write conditional distribution it always means that the conditioned random variable is fixed to a particular value. So given that the conditioned random variable has taken a particular value what does this density evaluate at? Is this clear?

### 00:32:14 · Speaker 1

So now in this notation the prediction what does the prediction happen what is the prediction problem prediction problem is let us call that

### 00:32:24 · Speaker 1

prediction

### 00:32:27 · Speaker 1

of X cap is simply the likelihood

### 00:32:33 · Speaker 1

that likelihood is a density function likelihood okay

### 00:32:41 · Speaker 1

the conditional density

### 00:32:50 · Speaker 1

Why do you want X

### 00:32:54 · Speaker 1

Evaluated

### 00:33:04 · Speaker 1

the value of the conditioned random variable

### 00:33:17 · Speaker 1

Condition random variable

### 00:33:20 · Speaker 1

What is it? In this case it is X. Okay. Fix that.

### 00:33:29 · Speaker 1

This is the definition of prediction. See whenever you talk of regression and classification problems right this is what you are doing. What you are doing is

### 00:33:39 · Speaker 1

you are doing is evaluating the density function okay conditional density function of labels conditioned on data and you are evaluating that okay with the conditioned random variable which is the data random variable fixed at a particular x cap because by definition the conditional distribution always means that you have to fix the conditioned random variable at a particular value so now given that your condition

### 00:34:09 · Speaker 1

random variable is fixed at a particular value what does the density function evaluates to that is called a prediction at x cap

### 00:34:22 · Speaker 1

Do you understand Now tell me this

### 00:34:30 · Speaker 1

When we uh okay so maybe before we go that before we go there I will perhaps I'll tell you that okay see now suppose let me take an example suppose

### 00:34:48 · Speaker 1

Y okay is a discrete random variable that takes value 0 1 2 up to k.

### 00:34:57 · Speaker 1

Okay if this happens then

### 00:35:02 · Speaker 1

Prediction

### 00:35:05 · Speaker 1

Text cap

### 00:35:10 · Speaker 1

is what what is this object can somebody tell me

### 00:35:15 · Speaker 1

And we will also fix x and x let's say x is some random variable that is in some thousand dimensions. We are saying that there is an image, okay? It's a hundred by hundred image.

### 00:35:29 · Speaker 1

10,000 dimensions, 100 by 100 image and we have k labels. So if I have to set up the prediction problem here, what does predicting give me?

### 00:35:40 · Speaker 1

Can somebody tell me

### 00:35:41 · Speaker 3

argmax of P of like even

### 00:35:43 · Speaker 1

No no no I have not defined it that way right I've d look at the definition

### 00:35:50 · Speaker 1

No it won't

### 00:35:52 · Speaker 3

Probability density of Y given X

### 00:35:56 · Speaker 1

That is what I've yeah, what do you mean by that? How many values does this give you? If you predict it on XCAP, how many values will it give you?

### 00:36:05 · Speaker 2

So it will give us the values

### 00:36:05 · Speaker 4

But wait a second

### 00:36:09 · Speaker 1

It will give you k plus 1 values, right? So now prediction here means that it will give you an entire density function, in this case a mass function, because y happens to be a discrete random variable. So you have 0, 1, 2 up to k here, and this will have some values like this.

### 00:36:46 · Speaker 1

Do you understand? So now this, what is this? This is the density function of

### 00:36:54 · Speaker 1

y given x right evaluated at x equal to x cap

### 00:37:00 · Speaker 1

Do you understand this? So prediction will give you a distribution, sorry, it gives you a density function, right, or a mass function in this case, because it happens to be a discrete random variable, okay, which is evaluated at x cap. Is this clear?

### 00:37:19 · Speaker 1

Any questions on this

### 00:37:26 · Speaker 1

Now what do you do with this is a different question. See now you can relate to what we were talking in the first class right given some x you want to know what the corresponding y is. In the deterministic case right or in the non probabilistic treatment of stuff what was happening is that for a particular x you give a particular y okay. Now here for a particular x okay you are giving me

### 00:37:55 · Speaker 1

multiple y's with with certain likelihoods associated with each of them

### 00:38:01 · Speaker 1

Is this clear? Now, what do you do with this? Do with this is something that is specific to the user. Either, I mean, most of the times, what do we do? We take one y, okay, corresponding to the maximum value of this density function, isn't it?

### 00:38:22 · Speaker 1

If you look at machine learning, what people do is we want one label. So we don't want the density over labels, we want one label. Therefore, we take the argmax of this density and assign that as label for x cap. However, the problem is set this way that given a particular label, what you're actually doing is you're evaluating the density function p of the conditional density function and that x cap.

### 00:38:52 · Speaker 1

Is this clear

### 00:38:58 · Speaker 1

Any questions so far

### 00:39:00 · Speaker 2

one question so this x cap means a particular point in the this x x random variable

### 00:39:10 · Speaker 1

Uh you should be careful in in in choosing your words yeah see what do you mean by that it's actually one of the points in the range space of the random variable no

### 00:39:20 · Speaker 2

Yeah rain space

### 00:39:21 · Speaker 1

But yeah that is what it is see typically right X cap typically

### 00:39:31 · Speaker 1

X cap does not belong to the data set that you have because that's the test data right that's what is called as test data

### 00:39:40 · Speaker 1

Right, when you are interested, when you when you are talking about prediction, you can predict on X cap that is that is that belongs to D as well. But typically X cap does not belong to D because you know you want to predict on unseen data, right?

### 00:39:56 · Speaker 1

Okay uh yeah so Vivek

### 00:40:00 · Speaker 1

Sorry is there any way we can visualize PY given X I mean P or um uh what is that

### 00:40:06 · Speaker 2

Conditional random variable

### 00:40:10 · Speaker 1

What do you mean by visualize?

### 00:40:13 · Speaker 2

Visualize means so

### 00:40:16 · Speaker 1

See again I have to go back to the previous lecture I have told you that but let me repeat see what is happening is that think of it like you know there are there are two random experiments that are being done one where the images are being taken okay the other where every image

### 00:40:35 · Speaker 2

We'll go get it so it's a joint

### 00:40:37 · Speaker 1

Yeah, of course. I'm not talking about joint distribution. There is a joint distribution. Once you have a joint distribution, you have a conditional distribution as well. So we are saying that given that a particular outcome has occurred in one of the sample spaces in one of the trials, what is the likelihood or like what is the probability that the other event happens, right? I mean, the other trial takes these particular values. That is what the conditional distribution talks about. Yeah.

### 00:41:07 · Speaker 1

Yeah yeah

### 00:41:13 · Speaker 3

Just uh uh I mean is there any particular reason why we take likelihood function to be a density function rather than the distribution function

### 00:41:20 · Speaker 1

Uh, yeah, I told you right, it is easier to work with density functions. That's all. Most of the time, that is easier to work with density functions, especially when you have continuous random variables, it is easier to work with them. That's the only reason. Everything that you do with density function can be done with distribution functions. Okay. Not vice versa, not vice versa. Everything that you can do with distribution functions can't be done with density functions because there can exist random variables for which the density functions do not even exist.

### 00:41:51 · Speaker 1

But most of the in most of machine learning, we assume that density functions are the you know, well defined and they exist. And then we work with density functions. Typically in literature, not typically, right? In almost everywhere in literature, likelihood is defined as the density evaluating the density function at a point. Yeah. Because of ease of computation and analysis, that's all. Yeah. You will see that more, you know, when we talk of the divergence matrix, et cetera, in a while, you will see why.

### 00:42:21 · Speaker 1

density function is easier to work with. So also right there are lots of mathematical tools to deal with density functions. You know when we talk of random variables we always talk of associate density function right. So uniform random variable we give density functions distribution functions we don't remember do you remember the distribution function of uniform random variable no no and do you remember the distribution function of Gaussian random variable we don't but we remember the density functions.

### 00:42:52 · Speaker 1

That's the only reason. But remember that when whenever we talk of likelihoods, likelihoods are always density functions evaluated at a point. Okay.

### 00:43:02 · Speaker 1

Okay

### 00:43:05 · Speaker 3

So the dimension

### 00:43:10 · Speaker 1

Of course of course

### 00:43:13 · Speaker 1

X cap okay X cap is not in D right but

### 00:43:18 · Speaker 1

It's a sample from the same underlying distribution

### 00:43:27 · Speaker 1

Actually not

### 00:43:29 · Speaker 4

Uh so uh so I have a doubt so this is the conditional distribution of P of X given Y uh

### 00:43:37 · Speaker 1

Why do you want it? Why do you want it? Why do you want it?

### 00:43:40 · Speaker 4

No sir I was just having a doubt if the other order is that of any importance like does that have any significance in the real world basically P of X

### 00:43:47 · Speaker 1

It's given a lot, a lot of significance it has. Okay, that is called the class conditional density. This is called the the conditional of labels given data. That is the conditional of data given labels, right?

### 00:44:00 · Speaker 1

So it does have a significance. I will see that. We will see that. So I am setting up the problem of supervised machine learning. When we talk of unsupervised machine learning, we will see that that has a significance.

### 00:44:14 · Speaker 1

Any other questions

### 00:44:21 · Speaker 1

Card kick

### 00:44:25 · Speaker 4

Ah, sorry. Yeah, I had a query. I mean, like here, always we are talking about predicting one variable given the other. So this label, we should it be always

### 00:44:37 · Speaker 2

is something like discrete or can it be not necessarily

### 00:44:39 · Speaker 1

Not necessarily no, not necessarily. See, if you have a y belonging to some, y is another continuous random variable, you can evaluate the density of that at a conditioned on another random variable as well. In that case, the problem's name changes, no, then then it is called the regression problem, that's all.

### 00:45:01 · Speaker 1

The difference between the regression and classification is that that what sort of random variable your y is. If your y is a discrete random variable then the problem is called the classification problem. Then if y is a continuous random variable it is called the regression problem. But the underlying task is the same. The underlying task is still to evaluate the conditionals of y given x fixed at a particular point.

### 00:45:30 · Speaker 1

Okay, we'll write that maybe, right? If y is discrete

### 00:45:38 · Speaker 1

It's the classification problem

### 00:45:45 · Speaker 1

If y is continuous

### 00:45:51 · Speaker 1

The problem is called a regression problem

### 00:45:58 · Speaker 1

Okay now let's get back to what we were doing so now now given B

### 00:46:05 · Speaker 1

that

### 00:46:07 · Speaker 1

It's like this

### 00:46:13 · Speaker 1

Sampled from the underlying joint distribution. Okay. Now, given this.

### 00:46:28 · Speaker 1

This becomes

### 00:46:38 · Speaker 1

Okay good notes when I used to write put a box like that no that will become a nice box a rectangle here it doesn't okay

### 00:46:50 · Speaker 1

Okay so this is the central problem in this is this is what is called as supervised machine learning

### 00:47:04 · Speaker 1

Supervised machine learning are also called as the discriminative machine learning

### 00:47:11 · Speaker 1

discriminative modeling or machine learning whatever okay

### 00:47:17 · Speaker 1

Understand? So now given data from the joint distribution, I want to estimate the conditional

### 00:47:27 · Speaker 1

density function of y u and x

### 00:47:32 · Speaker 1

Is this okay

### 00:47:38 · Speaker 1

Be it classification, be it regression, this is the problem that we are solving

### 00:47:50 · Speaker 1

Questions on this

### 00:48:00 · Speaker 1

See note that we don't know the density function P of Y given X. Okay, we only have samples drawn from the joint distribution of X and Y. So now given having samples from the joint distribution of X and Y, how do you estimate the conditional distribution or conditional density function? It's a question that is to be answered and that is the question that is answered in all of like discriminative machine learning. Okay, we will we will see that.

### 00:48:30 · Speaker 1

a part of it now but this is the problem setting of uh

### 00:48:37 · Speaker 1

discriminatory machine learning now you can now see the connect right now uh oh this went

### 00:48:49 · Speaker 1

Is there a way I can put a box nicer box

### 00:48:58 · Speaker 4

there seem to be circular and spire icon at the top left third one

### 00:49:07 · Speaker 4

I'm from

### 00:49:07 · Speaker 2

Left from left third

### 00:49:12 · Speaker 4

The third one right my mistake

### 00:49:15 · Speaker 1

Cheers

### 00:49:17 · Speaker 1

This is open

### 00:49:22 · Speaker 1

Okay, now yeah, so now how do you estimate the conditional distribution, a conditional density function given data from an unknown distribution is a question. Okay, so maybe write this also with px.

### 00:49:37 · Speaker 1

are known here okay

### 00:49:41 · Speaker 1

question that we'll answer but this is what the machine learning problem is all about okay discriminative machine learning is all about that so now this xi's can be uh okay so let me write so xi

### 00:49:57 · Speaker 1

in some RD right and

### 00:50:02 · Speaker 1

yi can be discrete 1 to k or it can be another rk okay if it's this then it is classification

### 00:50:16 · Speaker 1

If it is this then it is regulation

### 00:50:29 · Speaker 1

Entire supervised machine learning is this this that's all right how do you estimate this p of y given x given d

### 00:50:37 · Speaker 1

Now what about the so-called generative models and unsupervised machine learning is that you have given I mean in my mind both of them are very very similar given D

### 00:50:51 · Speaker 1

It are of this form so you don't have the notion of y there

### 00:50:58 · Speaker 1

Okay So you estimate

### 00:51:03 · Speaker 1

PX that's all

### 00:51:08 · Speaker 1

There is one other part to the uh the generative problem maybe I'll try to p estimate px and

### 00:51:16 · Speaker 1

Sample from it

### 00:51:22 · Speaker 1

I have to define what sampling is shall I do it now or later because it is a little digression

### 00:51:31 · Speaker 1

Let me define it perhaps

### 00:51:38 · Speaker 1

before i define the problem of generative modeling right i would like to ask you this question any questions on this definition of supervised machine learning see i still have not answered this question of how do you estimate the underlying density function i mean that is what we are going to do with this entire course but problem setting i want you people to understand what the problem setting is uh yeah so is is the problem setting clear for discriminative modeling and machine

### 00:52:08 · Speaker 1

uh supervised machine learning please let me know if you have questions Kartik

### 00:52:14 · Speaker 2

So one query, I I know we we don't know the distribution function P of x y, but how do we know that it's all been sampled from that distribution function itself?

### 00:52:27 · Speaker 1

And that's an assumption that we make

### 00:52:29 · Speaker 2

Okay so they got some

### 00:52:30 · Speaker 1

You make an assumption that the data is coming from one given distribution. Have you heard of something called IID?

### 00:52:38 · Speaker 1

in independent and identically distributed data IID data

### 00:52:43 · Speaker 1

Have you heard of that thing going in?

### 00:52:43 · Speaker 2

Have you heard of that yes yes yes in Ramakrishna

### 00:52:45 · Speaker 1

Yeah, that actually means, yeah, in fact, I deliberately left that because I didn't want to confuse you with things. But yeah, let me tell you this. So this is actually sampled IID from this distribution is what is said. This means that they are independently and identically distributed. Identically distributed means that all of these are actually coming from the same distribution. Independence means that all of these data points are independently sampled, which means that

### 00:53:15 · Speaker 1

one image is independent to observing the other image the next image

### 00:53:21 · Speaker 1

okay so now we make an a basically we are making an assumption that the that the entire data is coming from one distribution that is why you know all these methods that have been uh developed using the iid assumptions fail if there is a distributional shift

### 00:53:40 · Speaker 1

Right? That's because, you know, there's suddenly the IID assumption gets broken, which means that the data that you have given was coming from one distribution and you modeled it, you did everything. Now the test data comes from some other distribution. What do you do?

### 00:53:57 · Speaker 1

So that is an assumption that we make that the underlying distribution stays stays the same okay yeah Aditya

### 00:54:05 · Speaker 2

Uh so I wanted to ask what about outliers in that scenario like we assume that there are no outliers then

### 00:54:12 · Speaker 1

No, I've not defined what an outlier is, right? See how? Even if it's an outlier, it can still come from the same underlying distribution with less probabilities, right?

### 00:54:26 · Speaker 1

Can come from the tail of the distribution, but it is still coming from the same distribution, is it? Is it right?

### 00:54:35 · Speaker 1

Okay, if there are no questions, any more questions on this? So we'll move on. I'll define what generative modeling is. See, generative modeling again is that you are given data that is sampled IED from an unknown underlying distribution. This is also unknown.

### 00:54:51 · Speaker 1

Now again you still want to estimate the likelihood or the density function that's also same. One additional thing that comes in the generative modeling thing is you need to sample from it. Okay. So now what do you mean by sampling? First let us.

### 00:55:08 · Speaker 1

I'll put a box around it

### 00:55:13 · Speaker 1

This is the

### 00:55:16 · Speaker 1

Problem of generative modeling

### 00:55:29 · Speaker 1

This is generative modeling. So given data from an unknown drawn from an unknown distribution estimate the distribution or the density corresponding density function and sample from it. Now sampling is defined as follows. The process of sampling is that

### 00:55:49 · Speaker 1

We need to implicitly

### 00:55:55 · Speaker 1

conduct

### 00:55:59 · Speaker 1

So run

### 00:56:04 · Speaker 1

The random trial

### 00:56:12 · Speaker 1

corresponding to the sample space

### 00:56:34 · Speaker 1

This is the process of sampling

### 00:56:37 · Speaker 1

Now you understand what what I'm meaning. So let's say that you are your sample space is tossing a coin, right? And you are given some hundred coin tosses. Now, what do you mean by sampling? You have to implicitly toss the coin again.

### 00:56:53 · Speaker 1

See in practice we will not have the coin and wear it all right. So but what we can do is once, why am I saying implicitly is because if you run the underlying random trial again, what do you get is an outcome. But now because we are working in the space of random variables, we will get one point. So this implies that

### 00:57:14 · Speaker 1

Sampling

### 00:57:19 · Speaker 1

Leads

### 00:57:24 · Speaker 1

point

### 00:57:32 · Speaker 1

The range space

### 00:57:36 · Speaker 1

of the random variable

### 00:57:38 · Speaker 1

You see why? Do you all see why? Because see what we are doing is sampling is conducting the random trial that gave rise to the sample space, right? So once you conduct the random trial, you have an outcome. And once you have an outcome, you know the entire story, right? You have the random variable and because you have the random variable, you get a point in the range space of the random variable because random variable operates on outcomes and gives you a point in RD. Is this clear?

### 00:58:10 · Speaker 1

Now generative modeling is all about this. Okay, I will take questions. I will take questions. Generative modeling is all about this that you are given some data, okay, that is drawn from an unknown distribution, okay. You should of course estimate the underlying distribution that is a part of the process. Not only estimate the underlying distribution unlike in the discriminative learning case, you should also learn to sample from it. Now what do you mean by learning to sample from it? Learning to sample from it is simply

### 00:58:40 · Speaker 1

you are conducting the underlying random trial right again and again so that every time you conduct a random trial you have the random variable that is there which will give you a point in the range space of the random variable that's all that is generating one that is generating sampling or generating modeling

### 00:58:58 · Speaker 1

Okay, all this tag GPT, right, all the everything that you've seen us on it, Claude, et cetera, are actually doing this. They're actually running the underlying random trial multiple times whenever you do an inference.

### 00:59:12 · Speaker 1

Okay. Now, somebody asked me a question just now, right? They said that, okay, what is the significance of X given Y? Okay. So that is actually that distribution. If you learn to sample, estimate P of X given Y and learn to sample from it, you are actually learning to

### 00:59:33 · Speaker 1

sample from the conditional distribution sampling from conditional distribution is nothing but conditional generation or prompt based generation so given an input prompt right which is represented as another random variable y now p of x given y is the distribution that you are sampling from given a particular prompt okay y is fixed at something you need to learn to sample from p x so it is p of x given y is what you sample from in

### 01:00:00 · Speaker 1

general conditional generative models this is unconditional generative modeling where given data drawn from an unknown distribution you estimate the distribution and learn to sample from it sampling is the process of running the underlying random trial okay so that you get an outcome from the sample space and because you have a random variable that's already in place instead of observing the outcome what you observe is the element in the range space of the random variable practically speaking if you are given some images all the images are points in the range space of the random

### 01:00:30 · Speaker 1

variable if you learn a generative model on it if you get a generative model on it and learn to sample from it when you sample what you get is another image okay which is nothing but a point in the range space of the underlying random variable and you will have to sample see also observe that is a very important uh point here in the definition that I say that you have to run the random trial that is corresponding to the underlying sample

### 01:01:00 · Speaker 1

space you'll see

### 01:01:03 · Speaker 1

See it is not doing see if you are given a let's say that you are given a given a coin tosses from a biased coin. Okay. It's not enough if you just learn to toss a coin. You have to learn to toss a coin toss that particular coin which generated this random trial. Isn't it? Do you understand what I'm saying?

### 01:01:27 · Speaker 1

So the sampling has to has to respect the underlying sample space which means that it has to respect the underlying underlying probability measure which also means that it has to sample in accordance to the underlying distribution.

### 01:01:48 · Speaker 1

Okay, so let me complete it perhaps. Sampling leads to a point in the range of the random variable respecting

### 01:02:00 · Speaker 1

respecting the underlying distribution

### 01:02:10 · Speaker 1

This means that if I have given you data from MNIST dataset, the sampling has to generate data from MNIST dataset only, no? It should not start generating data from some other human faces or something. It has to generate data from MNIST dataset. What is the mathematical way of saying it? That you run the random, the corresponding random trial, right? That would respect the underlying sample space, which means that the underlying probability measure is intact, which means that the underlying distribution function is also intact.

### 01:02:40 · Speaker 1

So, now now you understand right now you understand why there is a connect between estimating px and sampling from it. If you estimate px you can't estimate you can't sample from an unknown distribution unless you estimate the underlying distribution because you need to sample such that the underlying distribution is preserved. Do you see that?

### 01:03:01 · Speaker 1

Now the entire problem of generating modeling is that you are given data that are drawn from an unknown underlying distribution learn to run the underlying

### 01:03:12 · Speaker 1

I mean random trials okay such that the distribution function is respected and intact itself. So if I say that you will have to sample such that the you have to sample from the underlying sample space it is understood no because you can't sample from the same sample space unless the measure that is there is is preserved but yeah I am just making it explicit to say that you'll have to learn to run the random trial such that the underlying distribution is intact.

### 01:03:42 · Speaker 1

which means that you better estimate the underlying distribution and then you learn to sample from it. So, this is the difference between the discriminative modeling and generative modeling. In discriminative modeling what you do is you stop at estimating the conditional distributions of the labels given data given x right. Here you estimate the distribution and also learn to sample from it.

### 01:04:10 · Speaker 1

Okay, questions.

### 01:04:14 · Speaker 1

I didn't get it

### 01:04:17 · Speaker 2

Not understand fully because

### 01:04:20 · Speaker 2

Well you need to we need to know how to sample from it right so

### 01:04:24 · Speaker 4

We do this

### 01:04:25 · Speaker 2

coin example we already sampled the coins right maybe there are hundred coins and out of that we are choosing

### 01:04:31 · Speaker 1

No no no no no no hold on hold on hold on no okay in the coin toss example we have one coin we don't have hundred coins

### 01:04:38 · Speaker 2

Okay okay we have

### 01:04:39 · Speaker 1

We have tossed one coin 100 times. That is your data.

### 01:04:45 · Speaker 2

Okay got it got it

### 01:04:47 · Speaker 1

But you don't know what the what is the likelihood with which the coin turns out to be head or tail. You get it?

### 01:04:55 · Speaker 2

Mm Yes yes

### 01:04:57 · Speaker 1

Okay, learning to sample from it is to learn to toss the coin again without having access to the coin.

### 01:05:05 · Speaker 2

Okay okay

### 01:05:07 · Speaker 1

Right. So we have, yeah, we don't have, we have not sampled yet. We only have samples that somebody has already given us. That is our data.

### 01:05:19 · Speaker 1

So without having access to the coin we need to know how the coin would have turned out if we toss you know 10,000 more times that is sampling

### 01:05:29 · Speaker 2

So it basically means uh uh we have to sample more from near the peaks of the PDF function

### 01:05:30 · Speaker 1

Basically

### 01:05:36 · Speaker 1

No I'm not saying peak you just have to sample it such that the underlying distribution function is intact you can sample from the tail also

### 01:05:44 · Speaker 2

Yeah occasionally I'm a bit more I mean

### 01:05:44 · Speaker 1

You simply say that you sample such that the underlying distribution function is respected. That's all. See, if you are sampling from so-called tail, the measure associated with that outcome has to be lesser. That's all it means.

### 01:06:03 · Speaker 2

Okay of course

### 01:06:05 · Speaker 1

You get it see now that you know this language you know try to use this more so basically I'm saying that the underlying measure is respected

### 01:06:12 · Speaker 2

I think the main issue is

### 01:06:12 · Speaker 1

Now if the measure has to be respected then the underlying probability measure or if the distribution has to be respected then when you sample when you sample hundred times right like more number of times if there is a if there is a if there is an outcome that has more probability then that has to appear more compared to other right obviously.

### 01:06:33 · Speaker 2

Yes yes

### 01:06:34 · Speaker 1

But the the underlying measure has to be perfectly intact otherwise then you are not running the current random trial no you are learning to to sample from some other random trial or some other sample space which is undesirable.

### 01:06:50 · Speaker 2

Okay perfect

### 01:06:51 · Speaker 1

See that is what hallucination is all about right. See what is hallucination that the underlying distribution is not estimated properly. If it is not estimated properly it will start sampling from some some other sample space that that does not correspond to the given data.

### 01:07:08 · Speaker 2

Okay but sir there is a no guarantee to uh I mean entirely we can reduce this hallucination right

### 01:07:16 · Speaker 1

That is what I am saying no that is why the entire course is designed that you need to that depends on how good is your estimate on PXS

### 01:07:26 · Speaker 1

Isn't it? So now the sampling process has to estimate the underlying distribution. If you have not estimated the underlying distribution correctly, then you have you mean you will obviously when you sample you will get things from outside of the sample space, no?

### 01:07:42 · Speaker 1

So that is why you have so many techniques you have that model this model every model is trying to do the same thing that every every generative model right you know be GPT autoregressive and GPT etc are come from this family of models called autoregressive models right and you know there is this adversarial networks and diffusion models and flow based models score based models all of these all of these are trying to solve this exact same problem that they are trying to estimate the underlying distribution and trying to

### 01:08:12 · Speaker 1

from it. Why are there so many models is because each of them estimate the underlying distribution in a different way. Since they don't estimate the distributions quote unquote perfectly you have so many models. Same thing goes for the uh discriminative models also. Why do you have linear regression, logistic regression and SVMs and kernel machines and neural networks? All of them are actually trying to solve this exact same problem which is estimating the underlying conditional distribution. But one model is better than the

### 01:08:42 · Speaker 1

Other because you know different they estimate the underlying distribution in a different way.

### 01:08:50 · Speaker 1

Now, you might have heard this term, no? All models are wrong, some are useful.

### 01:08:58 · Speaker 1

Right. So, everything is a model. Everything is trying to estimate some distribution given some data. They are all models. All of them are wrong. Some of them are useful. That is why you have metrics to estimate how good the performance of a given model is. Okay. So, now I have to define what is a model. Right. See, see, I mean, observe that we are solving an estimation problem. We are trying to estimate a density function. So, every estimator is a model.

### 01:09:28 · Speaker 1

that we are we are looking at generative models, discriminative models. What is a model? Model is nothing but an estimator for the underlying density function that we want to estimate. There can be thousands of estimators. Each estimator comes with its own property. Right. Claude has its property. Sonnet has its property. Like gamma has its property. This thing, you know, GPT has its property and so on. Everything is a model. But all of them are trying to do this exact same thing that given data from an unknown distribution, trying to estimate the underlying distribution.

### 01:09:58 · Speaker 1

and learn trying learning to sample from it

### 01:10:03 · Speaker 1

Yeah

### 01:10:05 · Speaker 3

Yes sir just to clarify my understanding on this prompt based generation so you mentioned that that problem is basically to sample from P of X given Y is that correct

### 01:10:16 · Speaker 1

It is it is it is it is estimating the conditional distribution of X given Y and learning to sample from it. See we will see this in great detail. In fact, you know we will look at multiple estimators in this course. Okay. Yeah. So this is I'm just setting up the problem now. Okay.

### 01:10:35 · Speaker 1

Yeah

### 01:10:37 · Speaker 2

Uh hi sir so here just a second

### 01:10:39 · Speaker 1

Just a second, uh, just just a second. Uh, like I'm I'm I'm I'm both, you know, happy and a little disappointed. I'm happy that, uh, like, you know, more people are talking. I'm slightly disappointed that the same set of people are kind of asking questions. I mean, it is I'm not discouraging you people, but I want to encourage the entire class to participate. Okay. So feel free to ask questions. Otherwise, uh, yeah, I mean, I don't want to go into the

### 01:11:09 · Speaker 1

philosophy of pedagogy but yeah I encourage all of you to ask questions don't hesitate do ask questions okay ask it go on

### 01:11:19 · Speaker 2

Yeah, so as we discussed that we are estimating the distribution, but we are estimating the distribution via the density function associated to it, right?

### 01:11:26 · Speaker 4

the density function

### 01:11:29 · Speaker 1

Yes yes

### 01:11:31 · Speaker 2

So earlier we discussed that the density function can't be like a proper like exactly 100 percent representation of the distribution function

### 01:11:39 · Speaker 4

Okay so what that would mean

### 01:11:39 · Speaker 1

No, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no,

### 01:12:05 · Speaker 2

Okay, so if we get a value of a density function at a particular point

### 01:12:08 · Speaker 1

Then we know everything about the distribution function because if you have the density function right you can integrate that and get the distribution function.

### 01:12:19 · Speaker 2

Okay okay okay

### 01:12:20 · Speaker 1

See but somebody asked me that question no why do we work with density functions and not with distribution functions is because

### 01:12:26 · Speaker 4

Mm

### 01:12:26 · Speaker 1

Computationally easy that's all

### 01:12:28 · Speaker 2

By the way

### 01:12:29 · Speaker 1

Otherwise otherwise I can actually say this now the problem is

### 01:12:35 · Speaker 1

I can set the problem as estimating the disi underlying distribution function

### 01:12:40 · Speaker 2

Okay

### 01:12:41 · Speaker 1

But I set it up as density function because when I what happened

### 01:12:49 · Speaker 1

I set it up as density function because when I uh when I

### 01:12:57 · Speaker 1

Answer this question of estimators. No, I will use density functions for everything, that is why.

### 01:13:02 · Speaker 2

Mm-hmm okay

### 01:13:03 · Speaker 1

uh yeah so but uh there is a one-to-one correspondence between density function and distribution function just that evaluating the density function at a point will not give you a probability that's all yeah

### 01:13:14 · Speaker 2

Mm-hmm okay okay understand

### 01:13:17 · Speaker 3

Oh so just to continue the discussion so here we said that we will get the likelihood right and the likelihood may be low uh but still the probability may be high that is possible right

### 01:13:27 · Speaker 1

No, no, no, no, no, right? No, see again, see when you when you evaluate the density function at a point, you get a likelihood. So for continuous random variables, there is nothing called probability at a point that itself is not defined.

### 01:13:44 · Speaker 1

because probabilities are evaluating the distribution function. Now if you evaluate the density function at a point, right, you get zero. Which means that, I mean, so rather if you integrate the density function, right, at a particular point, you get zero. So the probability of obtaining a particular image is zero actually.

### 01:14:06 · Speaker 3

Yes that's correct but what is the likelihood

### 01:14:07 · Speaker 1

What did you work on lately Huh

### 01:14:10 · Speaker 3

Yeah but what we are interested in is the probability right that I mean when the probability is high we want to take that particular label as yes

### 01:14:17 · Speaker 1

just say say no no for for you mean the discriminatory part you're saying is it not yes

### 01:14:23 · Speaker 3

Yes yes yes the what does that mean

### 01:14:24 · Speaker 1

Yeah see if y happens to be a discrete random variable then density functions are probabilities

### 01:14:32 · Speaker 1

Because they are mass functions

### 01:14:36 · Speaker 3

Oh but if it is a regression problem then

### 01:14:38 · Speaker 1

If it's a regression problem then you should just say that it's likelihood I want a point with higher likelihood don't call it probabilities that's all you see

### 01:14:47 · Speaker 3

Yeah but that's my point so higher likelihood may not mean the higher probability right

### 01:14:52 · Speaker 1

Probability of a point itself is not well defined it is not even defined so you take decision based on likelihood is all I am saying stop there

### 01:15:00 · Speaker 3

Stop this

### 01:15:01 · Speaker 1

See, don't jump to the probabilities because probabilities of continuous random evaluating the density function at a point or likelihood of a point is not the probability of that point.

### 01:15:16 · Speaker 1

Yeah, so just just say that I want to pick a point with higher likelihood. That's all. That is perfectly fine. Don't say that, you know, higher likelihood corresponds to higher probability. That is incorrect.

### 01:15:28 · Speaker 3

Okay

### 01:15:29 · Speaker 1

Yeah, I mean I'm just making it you know pedantically correct. There are nitty gritty is but that is what it is. Yeah.

### 01:15:37 · Speaker 3

Yeah thank you so much

### 01:15:39 · Speaker 1

See now you should see the connect between estimating the density function and sampling from it, right? I mean if you can't estimate the density function you can't sample from it because you have to sample in accordance with the underlying density function that will happen only if you know what the density function is, right? Yeah. Okay. Um, Avirup?

### 01:16:04 · Speaker 3

modeling very in discriminative modeling

### 01:16:12 · Speaker 4

So can do we have a corresponding definition for unsupervised learning also I'm just asking for clarity yeah

### 01:16:18 · Speaker 1

Yes, yes. So you can also call generative modeling as unsupervised machine learning.

### 01:16:27 · Speaker 1

Yeah so uh there is a um

### 01:16:32 · Speaker 1

For now, let us let us call in in in unsupervised machine not all unsupervised machine learning models enable sampling. Now, for instance, if you do k-means clustering, right, it will not enable sampling strictly speaking. But if you do if you if you if you do GMM clustering, it does enable generative modeling. OK, and also, you know, k-means happens to be a special case of GMM.

### 01:16:57 · Speaker 1

You for now let us call this as unsupervised machine learning, but when we come to this thing called latent variable models, right, which is a special case of special way of modeling the underlying density function, then that also is called unsupervised machine learning. OK. But yeah, so for now you can assume that that unsupervised modeling, let's say that.

### 01:17:24 · Speaker 1

Unsupervised models are sort of a subset of canned in modeling. Okay, for now.

### 01:17:32 · Speaker 1

Maybe I will not write it but simply consume it yeah

### 01:17:38 · Speaker 1

Was this social? No this was a virup I suppose

### 01:17:49 · Speaker 4

Yes thank you sir

### 01:17:51 · Speaker 1

Uh so we still have a question I think socially you have a question

### 01:18:13 · Speaker 1

Okay so maybe he's not there okay so let us move on shall we move on any other question

### 01:18:20 · Speaker 1

Okay so let us now answer ask this uh

### 01:18:28 · Speaker 1

Yamanish go on

### 01:18:42 · Speaker 1

also like for suppose text base we try to predict the next word right so while training we fed uh fed that next word what will be the next word try to predict that so it's it's a kind of uh supervised on you know in that case

### 01:18:59 · Speaker 1

Yeah, it is not because your I mean the word is I mean the word is modeled as X here. Okay. In that case, you are looking at autoregressive models. Your words are also the random variable X. So now you are actually sampling from the underlying distribution.

### 01:19:19 · Speaker 1

That is why I define prediction in this case particularly as evaluating the the likelihood at a point

### 01:19:29 · Speaker 1

no supervision per se there see that is why no i don't want to use this terminology of supervised and unsupervised learning precisely because of this you know there the line is very very blurred uh you simply say that in both the cases you are estimating the uh estimating some distribution okay given some data that is all

### 01:19:55 · Speaker 1

Okay, but typically in supervised models or discriminative models, you will not have an explicit sampling process, but in generative model, you will have explicit generative sampling process. That's all. Okay, so maybe let us call this as discriminative machine learning if you are.

### 01:20:13 · Speaker 1

comfortable with this

### 01:20:16 · Speaker 1

Okay, discriminative modeling and generative modeling. Discriminative modeling does not have sampling, generative modeling has sampling. So let's have that as the difference. Yeah, so she'll progress.

### 01:20:31 · Speaker 1

Now the important question is

### 01:20:42 · Speaker 2

Answer one question

### 01:20:43 · Speaker 1

Yeah cool

### 01:20:46 · Speaker 2

What if like in both the cases we get the density function d y given like in one like for a the discriminative model we get the dist

### 01:21:04 · Speaker 2

density function so why can't we get the distribution function from that

### 01:21:08 · Speaker 1

We can I'm not saying we can't we can but I mean most of the applications right it is enough if you have the density function

### 01:21:17 · Speaker 1

We can get the discriminant uh we can get the distribution function from it

### 01:21:22 · Speaker 2

Okay, and then like if we want to sample it from like do sampling from that, like for an example, we have a set of images of 10 classes, basically 10 different animals, and we get the underlying probability distribution. And then we sample and say, okay, we want to generate an like image of an animal in a different scenario. Let's say we had the sample of animals in jungle.

### 01:21:52 · Speaker 2

But we want that to want the model to generate the images for those animals in a city context. So won't that be considered as generative model?

### 01:22:04 · Speaker 1

That is a generative model, but the is changed, no? See, that is all, I mean, that is definitely generative model, but then see, if you only have images of animals that are from like jungle in your data, then there is no way that your model is generating images of animals in cities.

### 01:22:24 · Speaker 2

No no no sir my my point was so in in the discriminative model we have the uh like basically the k classes from which the data belongs the data can be classified into now using this available data we develop uh like we get the distribution and we develop a model to uh you know generate some fresh data fresh fresh data out of it

### 01:22:24 · Speaker 1

No no no my

### 01:22:52 · Speaker 1

when we say that see that is what i'm saying let me i don't know maybe i didn't convey the point properly see when i say that you need to sample from the corresponding underlying distribution it means that you have to sample from you have to get a quote unquote fresh sample only you know sampling is always fresh sampling

### 01:23:16 · Speaker 1

Suppose you are given 100 images of these animals, let them belong to 10 different categories. When you generate, you have to generate it from those 10 different categories only. You can't generate from an unseen category is what I am trying to say.

### 01:23:32 · Speaker 2

Yes sir agreed

### 01:23:34 · Speaker 1

You can't generate it by construction because you have only estimated the underlying distribution

### 01:23:39 · Speaker 2

Correct correct correct

### 01:23:40 · Speaker 1

That's all. When your model is as good as your data, unless your model has seen that, see it will, it can generate the images from, I mean, which are not there in your data set.

### 01:23:56 · Speaker 2

Big

### 01:23:57 · Speaker 1

You understand but it can't generate data from the distribution that does not correspond to your to your data set

### 01:24:09 · Speaker 2

Button center

### 01:24:10 · Speaker 1

You understand that? See, for example, if you have, let's say, the images of like, you know, human beings as your data, when you construct a generative model and sample from it, it will generate

### 01:24:24 · Speaker 1

the face of a non-existent human being. Okay. But it can't generate the face of a monkey or a dog or a cat.

### 01:24:33 · Speaker 2

Correct sir, agree, agree.

### 01:24:34 · Speaker 1

Next up next one

### 01:24:35 · Speaker 2

That is one of them

### 01:24:36 · Speaker 1

That is what is meant by uh uh respecting the underlying distribution

### 01:24:41 · Speaker 2

got it sir so like my point of making this statement here was whether we have the classification uh or not it it it won't make a difference right

### 01:24:55 · Speaker 1

It it should not but as I said there is this thing called conditional generation that I'm not talked of right where you where you some learn to sample from P of Y given X sorry P of X given Y now suppose you have 10 categories and you know you want to let's say that you have cat images dog images whatever images and you have you have learned to the question is what is the underlying distribution that you are modeling if you are modeling remember that when I said that there is a conditional distribution it means that you are modeling

### 01:25:25 · Speaker 1

y equal to a particular value, right? Now let's say that y equal to 1 corresponds to cats. If you are modeling this distribution learning to sample from it, you are only learning to sample from the cat images.

### 01:25:38 · Speaker 2

Yes

### 01:25:39 · Speaker 1

You understand? However, if I just take this and multiply this with P by and just take a sum of all this, what am I doing? This is equal to P X, isn't it? Yes, sir. Now, if I combine all the images from different categories and learn to estimate this distribution P X, then I'm sampling from all possible animal faces. That's all. So it depends on what the what distribution are you modeling. You get it?

### 01:26:07 · Speaker 2

Yes sir

### 01:26:08 · Speaker 1

that those categories or those labels are are are random or I mean I should not be using this word random they are they are synthetic or they are pseudo in the sense that

### 01:26:19 · Speaker 1

See, if you can you can group all the cat images into one and call that as one distribution and estimate it so that you when you sample you only get cat images.

### 01:26:31 · Speaker 1

If you take say images from 10 categories, combine them all and call them Px and if you if you mod estimate that then you get images from all categories that's all.

### 01:26:42 · Speaker 1

So that categorization is a sort of you know it's a it's a synthetic thing right depends on like what are you calling as general end distribution and data that's all right

### 01:26:54 · Speaker 2

Okay sir

### 01:26:57 · Speaker 1

Okay uh yeah Manisha

### 01:27:03 · Speaker 4

So as an extension to this discussion, and we have answered that, but so basically what we are saying is we are finding the, as I mean, as a part one of the problem, it's finding the distribution, the underlying distribution, which will tell us which class is linked to which label in a way.

### 01:27:22 · Speaker 1

No, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no,

### 01:27:22 · Speaker 4

No no no no no

### 01:27:38 · Speaker 1

See, estimating the underlying distribution simply tells you that what is the likelihood of this particular image under the given distribution, that's all.

### 01:27:50 · Speaker 1

So there is no idea of class here at all in generative modeling

### 01:27:59 · Speaker 2

But we still I mean the first step is to find the underlying distribution

### 01:28:03 · Speaker 1

Right

### 01:28:05 · Speaker 2

all you know are the like for the exa for example what was being discussed for all the animals you know we are kind of cate it's kind of

### 01:28:13 · Speaker 1

no no no it's a it's a it's it's a strict no i tell you so you have to understand what is meant by estimating the distribution in the generative modeling case and we will see examples and we will actually go deep into it but anyway at this step you need to understand it see if you are given let's say 100 images of animals okay estimating the underlying distribution means that you are trying to find out how likely or what is the likelihood of a particular

### 01:28:43 · Speaker 1

image under the distribution that's all how likely is that I'm obtaining this image suppose I'm conducting that random trial how likely it is to obtain this particular image is what I'm finding by estimating the distribution it has nothing to do with classes here there is not even an idea of classes because there is no y here

### 01:29:06 · Speaker 1

The way I have set up the problem there is no why here at all

### 01:29:11 · Speaker 4

Okay, get that. Okay, so it's just the likelihood of getting

### 01:29:14 · Speaker 2

a particular point in that distribution

### 01:29:16 · Speaker 1

That's all that's all so if you have thousand images I'm just calculating what is the likelihood of obtaining this particular image that's all

### 01:29:24 · Speaker 1

See if you if you if you imagine obtaining an image as a roll of a die

### 01:29:31 · Speaker 1

So I'm what I'm asking is when I conduct that random experiment, okay, what is the what is the likelihood that I'm obtaining this particular image? That is what estimating PX is all about.

### 01:29:45 · Speaker 1

So what is the likelihood that I get this particular face? That's all. I mean face of the die. I mean if you take the die example there is no notion of labels in this setting.

### 01:30:00 · Speaker 2

And then the sampling part that we are talking about is basically from

### 01:30:03 · Speaker 1

is that you are obtaining a new non-existent human face that's all

### 01:30:12 · Speaker 1

You are actually obtaining an image that is sampling

### 01:30:17 · Speaker 3

Getting that yeah I think I get the notion of that yeah right

### 01:30:20 · Speaker 1

There are two things here. One, see, once you estimate the underlying distribution, you can plug in any of the data points that are within your D or outside of your D as long as it is coming from PX and estimate the likelihood of that particular point using this PX.

### 01:30:36 · Speaker 3

Absolutely yeah

### 01:30:38 · Speaker 1

Sampling is that you are obtaining or you are running the random underlying random trial so that you get a point, a fresh or a new point that is not a part of your D, but still comes from the underlying sample space that is sampling.

### 01:30:54 · Speaker 3

Get that sir yeah

### 01:30:55 · Speaker 1

So there is no notion of labels here at all

### 01:30:58 · Speaker 3

Got it, got it, right sir

### 01:31:00 · Speaker 1

Right. So now I still have not defined this conditional, this conditional sampling. Right. I mean, sampling from P of X given Y. See, as I said, yeah, see, as I said, this has a notion of, you know, prompting.

### 01:31:07 · Speaker 3

Kiss

### 01:31:24 · Speaker 1

Exactly. So that I have not brought that notion yet. I mean, see now in the because that is simply confused stuff, you know, once you like like assimilate this idea of generating modeling and sampling, no, putting a conditioning here and saying that I'm modeling the conditional distribution is not difficult.

### 01:31:43 · Speaker 2

Right so that that was my point also so that is that doesn't seem difficult but now I think I get the actual problem there yep

### 01:31:49 · Speaker 1

See, yeah, so it is not estimating y given x. You want us to understand that? The problem with generative modeling is not estimating y given x. So that is the problem of discriminative modeling, that you are estimating p of y given x.

### 01:31:55 · Speaker 2

I'm not

### 01:32:03 · Speaker 1

And there is no sampling here

### 01:32:07 · Speaker 1

Okay, but in generative modeling the the two things one there is no notion of labels here

### 01:32:15 · Speaker 1

and two you need to learn to sample from it I mean that's a huge thing because see suppose you have you are given MNIST dataset and you create a CNN to predict the classes right that will not give you samples from MNIST dataset does it

### 01:32:32 · Speaker 1

But that is simply estimating p of y given x

### 01:32:37 · Speaker 1

Right? But if you build a GAN or a diffusion model on MNIST dataset, it will give you new samples from the MNIST dataset that are unseen because you are not only estimating the underlying distribution, but you are also learning to sample from it. That is generating model.

### 01:32:56 · Speaker 1

What is common in both the cases is that there is some distribution that has, I mean, there is some sample space and some random trial that has happened and you have generated the data already. And that is the input to both the, I mean, all of machine learning, that you have some data given from an unknown distribution. Now, what do you do when it is the question? Having that data, if you estimate, I mean, if your data is of this sort, if you rather model your data coming from a pair of random variables having the joint

### 01:33:26 · Speaker 1

distribution and you interpret one random variable as data or rather the features and the other random variable as labels then if the problem is set up as estimating the conditional of the label random variable conditioned on the feature random variable that is discriminative modeling without bothering about sampling but now okay I'll make things a little involved because you asked this question please see if you can understand this see I can actually construct a generative modeling

### 01:33:56 · Speaker 1

Having the data

### 01:33:59 · Speaker 1

that that is given in discriminative modeling as well. Do you see?

### 01:34:05 · Speaker 1

What I am trying to say is suppose I have that data set of animals with the corresponding classes also given

### 01:34:15 · Speaker 1

Now if I estimate P of X Y the joint distribution P of X Y and learn to sample from P of X given Y then that is another generative modeling that is conditional generation.

### 01:34:29 · Speaker 4

get it so that's uh the joint uh uh distribution here and yeah we also get it from a single uh you know distribution of a random variable

### 01:34:40 · Speaker 1

distribution of a single data variable. It depends on how do you want to view your data. See if you are given thousand animal images, now do you want to categorize them into subcategories and say that hey look my data is such that I have the image and the corresponding label with it or do you want to see that as simply thousand images without having labels.

### 01:35:01 · Speaker 4

Yes and then draw sample uh

### 01:35:03 · Speaker 1

That's all see yeah that's all it's a modeling choice you know what are you drawing samples from are you drawing samples from px or are you drawing samples from px given y

### 01:35:15 · Speaker 1

Right? Now, if you are drawing samples from P of X given Y, it simply means that given these animal images and the fact that, you know, I want to generate from dog images or rather I want to generate the image of a dog, then I know how to do it. But now if I give, if I, I mean, that needs the corresponding labels as well.

### 01:35:36 · Speaker 1

Right, because you are you have you want to estimate P of X given Y. But I mean estimating P of X given Y and learning to sample from it also is a generative model, right? So suppose you estimate P of X given Y and sample from X given Y, that's also generative modeling. That is actually conditional generation, which is which is what ChatGPT does. So given Y, which is a particular prompt you want to generate.

### 01:35:58 · Speaker 4

I'm like

### 01:36:04 · Speaker 1

And for that, the kind of data that you need is pairs of x, y. Do you see that? Because you need the underlying joint distribution.

### 01:36:12 · Speaker 3

Absolutely yeah yeah

### 01:36:14 · Speaker 1

So depends on like what sort of data you have and what sort of density are you modeling and sampling from. That's all.

### 01:36:23 · Speaker 1

But the major difference between these two models is that in discriminative modeling, see in both of the cases, you have data drawn from an unknown distribution, you are estimating some distribution. But what is not there in discriminative modeling is that you don't learn to sample. But in generative modeling, you learn to sample from it. That's the only difference.

### 01:36:45 · Speaker 1

I hope that you know this notion is clear because you know I mean this this is what differentiates let's say a ResNet based CNN or VGGNet from a diffusion model or a GAN. Both of them are actually estimating the underlying distribution given data. Both of them are given same kind of data. What is different is that the generative models learn to sample from the underlying distribution. Discriminative models don't learn to sample. That's the difference.

### 01:37:16 · Speaker 1

Okay, great. Any other question on this? I mean, this is important because this is, I mean, you, you, if you understand what the actual problem is, you know, then rest of the math and algebra becomes easier. Any other questions? So now you see that, right? I mean, now one of the central problems in both, uh, in discriminative and generative learning modeling is that given data from an unknown distribution, how do you estimate the underlying density function is the question, right?

### 01:37:43 · Speaker 1

This is an important question, right? Given data drawn from an unknown distribution, how to estimate the underlying density function is the question that has to be answered. Okay. For that, there are multiple techniques. One technique that we will be seeing, I mean, that is common across multiple models that we will see in this course is what is called as divergence minimization.

### 01:38:10 · Speaker 1

all these models right GANs, VAEs, diffusion models, autoregressive models etc all of them employ this technique called divergence minimization to answer the MBO question and by the way every generative model that you can think of right that the people are coming up with are actually solving this problem that given D you estimate the underlying density and sample from it.

### 01:38:36 · Speaker 1

Right. Minor modifications here and there. I mean, depends on what sort of D that people have. If you have like, like text and the corresponding next word or label or something, image and label, you learn to sample, estimate the conditional distribution and sample from it. That does not matter because that's simply a model, like a design choice. But they are all solving this particular problem. Now, to solve this problem, you need to estimate the underlying density. Right. Otherwise, how do you learn to sample according to that particular,

### 01:39:06 · Speaker 1

density. So, you have to estimate the underlying density. So, all of the generative models in fact, even discriminative models have to solve this problem of divergence minimization or rather given data drawn from an unknown distribution, how to estimate the underlying density function is a problem that all ML models have to solve. And one technique to do that is what is called as divergence minimization that is employed by all the existing generative models.

### 01:39:30 · Speaker 1

So we will see that next, you know, how to, and what is this divergence minimization and how to use that to solve this problem is something that we will see next. Shall we take a break now?

### 01:39:45 · Speaker 1

I think it's 90 minutes let's take a break for 15 minutes now

### 01:39:54 · Speaker 1

Okay, so in my clock it is 11 a.m. Let us reconvene by 11.15-ish. Okay. Yeah, see you in 15 minutes.

### 02:02:31 · Speaker 1

The resume

### 02:02:33 · Speaker 2

Yes sir

### 02:02:59 · Speaker 1

See Kendan has just put a poll for tutorial timings so please respond to that. It is I think both on WhatsApp and Teams. WhatsApp I definitely saw it now. I don't know if it's on Teams. Is it on Teams already or?

### 02:03:18 · Speaker 4

That's exactly what I'm saying

### 02:03:21 · Speaker 1

Okay, please respond, depending upon your response, whatever works for most of us, most of you will take that time, okay?

### 02:03:30 · Speaker 1

Okay uh let us continue

### 02:03:34 · Speaker 1

See, one small request is that from now on the content will become a little dense and intense. So please spend some time after the class in sort of just looking at what is happening so that the storyline is not lost. Okay. So please do that before coming to every class. And also you can look at my reference, look at my notes that I have given to you that also has some references.

### 02:04:04 · Speaker 1

Okay, so now what is the the question that we are looking at that we are given data drawn from an unknown distribution and we want to estimate the underlying density function that is the question that we are looking at. How do we do that? One of the methods to do it is via this thing called divergence minimization. So what is the idea there? Okay, the idea is the basic idea is the following that first

### 02:04:30 · Speaker 1

assume

### 02:04:34 · Speaker 1

A parametric form

### 02:04:44 · Speaker 1

Unknown dead city

### 02:04:47 · Speaker 1

the density function that is to be estimated okay

### 02:04:51 · Speaker 1

for the density function

### 02:04:55 · Speaker 1

It will be a steel on a trip

### 02:05:01 · Speaker 1

Okay, so I mean this I'll give you step by step. So this is the first step. Now what does this mean? This means that, so now you are given some data d, right? You assume that the density function that I have to estimate

### 02:05:18 · Speaker 1

can be represented using a neural network with some parameters

### 02:05:24 · Speaker 1

understand okay so typically denoted by

### 02:05:38 · Speaker 1

denoted with p theta okay

### 02:05:45 · Speaker 1

Theta are the set of parameters

### 02:05:57 · Speaker 1

Do you understand what this means? So an example can be multiple examples. Assume your p theta, let's say that I assume it to be a Gaussian density and note that this density function is still on the same sample space or the random variable as the underlying data, right? I mean, obviously it has to be defined on that only. So this can be, let's say a Gaussian distribution, okay, with some mean, okay, mu and some variance.

### 02:06:27 · Speaker 1

Now, theta in this case happens to be the mean vector.

### 02:06:34 · Speaker 1

and the variance matrix

### 02:06:37 · Speaker 1

understand. Now, what we do is we assume a parametric form for the density function that is to be estimated ok, denoted by p theta. You you can assume that to be anything. You assume it to be a Gaussian density, assume it to be exponential density and those parameters happens to be that. This is one example. The other example can be that I

### 02:07:00 · Speaker 1

assume it to be a neural network right so p theta of x right is this is output of some

### 02:07:13 · Speaker 1

some neural network right where

### 02:07:19 · Speaker 1

G theta

### 02:07:22 · Speaker 1

is a neural network

### 02:07:25 · Speaker 1

a neural network and this z is simply some some gaussian distribution so basically the way i'm modeling this is there is a sample of the gaussian distribution that is going through a neural network g theta we'll go to the details of all this but these are examples so z is going as output and what is what am i getting at the output are actually p theta of x

### 02:07:52 · Speaker 1

I can model it. I mean, this is again a design choice. I mean, this is where different models are different. This d theta can be a transformer, right? It can be a CNN or RNN or whatever, depending upon what your choice is. But basically, the idea is that you assume parametric form for the underlying density function that is to be estimated. Do not expect p theta. Is this clear? Like, what do I mean by parametric assumption?

### 02:08:27 · Speaker 1

So this is the first thing that you do. So once you make that assumption, what is the second step? The second step is that

### 02:08:37 · Speaker 1

Define and compute

### 02:08:41 · Speaker 1

compute okay a distance or a divergence metric

### 02:08:52 · Speaker 1

divergence metric between okay the true density function

### 02:09:03 · Speaker 1

Exactly true

### 02:09:06 · Speaker 1

density function

### 02:09:09 · Speaker 1

Which is PX right and

### 02:09:13 · Speaker 1

as parameter

### 02:09:26 · Speaker 1

parameter function p theta okay so basically d okay that will take the true density and the parameter density this is the notation okay px double slash p theta so this measures

### 02:09:55 · Speaker 1

So, this is the divergence metric that would compare the true density function to the parametric density function. You might ask me here, right? I mean, we don't know the true density function. How do we compute this? Hold on to that question that that actually turns out to be the central question of all generative models. When you don't have the true density function, how do you estimate the distance metric is a question that we'll answer later. However, what we need to do is we need to define and compute some sort of a divergence or a distance

### 02:10:25 · Speaker 1

metric between density pair of density functions in this case the density functions happens to be the true density and the parametric density that we have assumed okay okay once we do that what do we do so

### 02:10:40 · Speaker 1

They're just

### 02:10:46 · Speaker 1

compute

### 02:10:50 · Speaker 1

the parameters

### 02:10:56 · Speaker 1

of pre theta

### 02:10:59 · Speaker 1

Such that

### 02:11:02 · Speaker 1

D of px slash p theta is minimized.

### 02:11:10 · Speaker 1

procedure right this is the this is what is called as training agent say training a model or learning a model and so on this is the learning part of it understand mathematically speaking what you do is you set the parameters theta star okay as the ones that would minimize what do you mean by argument the set of parameters that would minimize a function okay now that would minimize the distance metric that you have defined between

### 02:11:42 · Speaker 1

density functions. We have two density functions. This entire thing now will become a function of theta because p theta is a function of theta and you want to solve for this of theta such that this distance between track is minimized.

### 02:11:58 · Speaker 1

Now the final estimate

### 02:12:06 · Speaker 1

This is the learning problem this is the training of learning of generative model right training

### 02:12:19 · Speaker 1

So, training basically is solving an optimization problem. You all know that, right? That is why we use gradient descent and backpropagation algorithm to train. Okay? Basically, you are solving an optimization problem. The final estimate for px, right, is simply p theta star obtained by solving the following.

### 02:12:45 · Speaker 1

You need to get us stuff

### 02:12:48 · Speaker 1

Obpained

### 02:12:50 · Speaker 1

is solving

### 02:12:54 · Speaker 1

the EMO optimization problem

### 02:13:03 · Speaker 1

Optimization as you know in this case that is the minimization problem

### 02:13:14 · Speaker 1

This is the general recipe, right, of how to solve any machine learning problem. It can be generated, discriminative or generative modeling. What are we doing? We are simply, we are given data from a known distribution. We assume a parametric form for the density function to be estimated, typically denoted with parameters theta. See, that is why now you can, I think, relate. Now, in the discriminative case, the underlying density function that we need to estimate is p of y given x, isn't it? We either model this as a logistic

### 02:13:44 · Speaker 1

Or we model the sub

### 02:13:48 · Speaker 1

is our model p theta what is the model this is for the underlying density to be estimated right

### 02:13:57 · Speaker 1

This actually P theta

### 02:14:01 · Speaker 1

what is called as a model

### 02:14:05 · Speaker 1

be it in a generative model or a discriminative model, the parametric assumption that we are making on the underlying density function is what is called as a model. It can be a neural network, it can be anything, any kind of parametric function. Then the problem of estimating the underlying distribution translates to estimating the parameters of the underlying model that we are assuming. That is also a density function. Now, how do you estimate the parameters

### 02:14:35 · Speaker 1

of this density function is the question. For that, we need to first measure. Let's say that we fix one value for this mu and sigma. Let's say that our model is a Gaussian model, okay? And the only parameters that we need to estimate are mu and sigma. We initialize that with some value. Now, you get one p theta with that. What we should do is we should compare that p theta with the actual density. Now, for that, we need a way to compare density functions. If you take pairs of density functions,

### 02:15:05 · Speaker 1

need a way to compare the density functions right now you compare that and you see if it's large if the if the distance between the true density and the density function with a particular set of parameters is large then you change your parameters in such a way that that distance become lesser right so for that you need to first compute a or rather compute a distance or a divergence metric between the true density and the assumed parametric density or the model okay and then i

### 02:15:35 · Speaker 1

or compute the parameters of the model such that this divergence or the distance metric between the pairs of density is minimized that is what the training is mathematically speaking you are solving this optimization problem that you find your theta such that this distance metric between this distance metric itself becomes a function of theta right now you need to find this theta such that the distance between the px and that particular p theta is minimized so we should solve this problem

### 02:16:05 · Speaker 1

which is which is training the model the final estimate for px will be that p theta star is the set of parameters that you have gotten from solving this optimization problem that would minimize the distance metric between the true density and the model density

### 02:16:24 · Speaker 1

Is this clear? Now, again, the open questions are I have not told you two things. I have not told you how to compute the system's budget when you don't have PX. We still don't have PX, right? That is our whole problem. We will, I have not told you that. I will tell you that. The second thing that I have not told you is how to solve this optimization problem and what sort of model choices that we need to make. That will be the subject matter of this course, entire course. We will take different, see for Gans makes, for instance, you know, adversarial.

### 02:16:54 · Speaker 1

networks make some assumption on p theta v a's made some other assumption on p theta diffusion models make some other assumption on p theta they would change this underlying distance metric they would change the way the optimization is being done that is what the the you know the levers with which we can play what sort of distance metric can we use what sort of optimization can we do what sort of model choices we can do are the questions answering in different models but this recipe would is going to stay that

### 02:17:24 · Speaker 1

You make an assumption on the unknown density function define a presence matrix between two density and fix the parameters of the density such that the distance between the density and is minimized

### 02:17:42 · Speaker 1

That is all the recipes for making the density. I am not still telling you how to sample. I will tell you how different models sample in different ways. We will talk about it later. But this is how you estimate the unknown underlying density and this is the recipe. This is called the divergence minimization, right? Because you are assuming a model, minimizing the divergence. This D is called the divergence and minimizing the divergence between the pair of densities.

### 02:18:11 · Speaker 1

Okay any questions about uh...

### 02:18:16 · Speaker 2

Sir I wanted to understand uh what is this g of theta when like when you have written g of theta g theta

### 02:18:24 · Speaker 1

It's a neural network no I told you no it's a neural network simply a neural network

### 02:18:30 · Speaker 2

Okay and Z Z

### 02:18:32 · Speaker 1

There is some random variable some some arbitrary random variable that will go as an input to this neural network and whatever output this neural network is giving I model it as which you know

### 02:18:45 · Speaker 1

Whatever output that neural network is giving no I take that as P theta of x

### 02:18:50 · Speaker 2

Okay okay

### 02:18:52 · Speaker 1

There is one way to modernize that I said no as I said there are multiple uh models that one can think of but this is one of the uh models that you can that you can design

### 02:19:06 · Speaker 2

Okay see

### 02:19:08 · Speaker 1

Is that okay

### 02:19:15 · Speaker 1

Yeah so many questions Kartik

### 02:19:18 · Speaker 4

Yes sir uh I have a little um

### 02:19:21 · Speaker 2

I didn't understand it fully about the parametric form that we were referring can we get it based on another example maybe a little more simpler one

### 02:19:32 · Speaker 2

Uh why why do we think this will happen

### 02:19:32 · Speaker 1

is that simply a number right yeah yeah you assume if you assume that it's a gaussian distribution that's a parametric form okay that how do you how do you differentiate one gaussian distribution from the other

### 02:19:47 · Speaker 1

is through the parameters no mean and variance that's all so you are assuming that ah you are assuming that it's a Gaussian density but you don't know what the mean and sigma are correct now how good is my assumption is a different question it can be a totally crappy assumption that you have made but that is that is I mean that's why I said all models are wrong no you have made some model assumption

### 02:19:51 · Speaker 2

You're thinking

### 02:20:10 · Speaker 1

Now these are simplistic models but in places like you know GANs and GPTs etc these models are made express enough they are made huge neural networks so that they can express a large family of functions.

### 02:20:24 · Speaker 1

Basically, you're expressing the density function. Now, you choose a parametric model such that it is expressive enough so that it can express a large family of functions. And transformers and neural networks are such functions. So now, what differentiates one transformer from the other transformer is the weights that they have.

### 02:20:43 · Speaker 1

Now that is that relates hold on that relates suppose you have like you know two transformers okay of the same architecture but you have two underlying distributions you want to estimate right using the same architecture you can fix the weights of these two transformers in it in different ways so that uh you know they represent two different distributions that's all that

### 02:21:10 · Speaker 1

In most of this course right our parametric models are zero networks only because they are expressive enough

### 02:21:18 · Speaker 1

Since neural networks are, I mean, we will see that neural networks are said to be universal function approximators. That means that you can use a neural network to approximate any function. That's a known result. Okay. That is why, you know, entire machine learning has moved towards neural networks because they are very good parametric models that you can have a neural network and set its parameter to represent any function. Same thing goes for discriminative model also, right? Why did people move away from C? Initially, people thought that, okay, this can be modeled using the same

### 02:21:48 · Speaker 1

logistic regressor it was not expressive enough what if the final density function that you that you need okay for the given data that happens to be something that a logistic regressor cannot model then you need to go to more models that are more flexible that's why you know the today's data of the art is that p of p of y given x these the parameter family that you assume on the underlying density are neural networks or transformers or anything those models are

### 02:22:18 · Speaker 1

expressive enough that means that see no matter what you do a Gaussian density can only represent this density you know I mean it can represent this this this and all that but it is a unimodal density with different you only have two degrees of freedom to play with

### 02:22:36 · Speaker 1

What is your under

### 02:22:39 · Speaker 1

has something like this a Gaussian density can never

### 02:22:45 · Speaker 1

No matter what mean and variance you play with that is why you choose this

### 02:22:49 · Speaker 2

I'm not saying it should be done

### 02:22:52 · Speaker 1

GML can express this of course, but right. I mean, you need more complex models to represent this. And that's why people use neural networks. Okay. So that's what is meant by parametric model that you just assume that my, my, my, my real density is one member of this family, large family that my parameter, parametric model can express. So basically, if I model that as a neural network or a transformer, I'm saying that my true density can be

### 02:23:22 · Speaker 1

represented by one set of weights of this neural network there exists one set of weights of this neural network that would represent my underlying density and I'm interested in finding that one set of weights

### 02:23:36 · Speaker 1

Now how do I find that one set of weight is simply I fix a particular weight and I compute, I see how far my density that I have gotten from this particular weight is from my true density. And then I adjust my weight such that, you know, that measure becomes lesser and lesser. That is training, no?

### 02:23:55 · Speaker 2

So yeah a query here is when the when then we like try to optimize the minimize that particular variable that I understood so if it is not

### 02:24:05 · Speaker 1

Divergence not variables call it call it divergence

### 02:24:09 · Speaker 4

divergence so if I'm minimizing that divergence say it is not minimizing up to my mark will we need to go back and change the model again I mean like is it what the new trend is a good question

### 02:24:19 · Speaker 1

That's a good question. Of course, of course you need to change. And that is why, you know, you have like, you know, ResNet 30, ResNet 50, ResNet 100. Why did people make it deeper and different kinds of architectures? Is because my divergence is not getting minimized.

### 02:24:35 · Speaker 1

How do I know my divergence is not getting minimized? Is it through some metrics, evaluation metrics like, you know, whatever, the accuracy, precision, et cetera. They are all surrogates to measure how bad is your divergence, right? If it's bad, then go back and change your model. That's all. It means that, okay, maybe the model assumption, the parametric model assumption that you have made is not good enough. If you are using neural networks as your parametric families, the architecture is not good enough. Change the architecture, make it deeper, have more neurons.

### 02:25:05 · Speaker 1

have more hidden layers etc.

### 02:25:08 · Speaker 4

So just to add on that point, just to maybe a little bit philosophical question, I mean, like, what if it doesn't, like, we can't model it using a parametric model at all? Maybe it's pure chaos, kind of, where we can't find a one which satisfies our divergence values.

### 02:25:28 · Speaker 1

And we are doomed

### 02:25:31 · Speaker 1

But it seems like all these transformers and billion parameter models are able to estimate general line divergence to a good level. That's why you have the boom of AI, right? I mean, they are working, which means that the divergence is minimizing.

### 02:25:50 · Speaker 4

Okay yeah but I was thinking as you said initial class maybe change the math just

### 02:25:56 · Speaker 1

again no no but i mean if the nature the mod see this we all this probabilistic uh way of thinking has taken us this far you see we've actually reached pretty far we have very very strong models these days models that can crack international mathematics olympiad and get a silver medal that's a very very strong model no

### 02:26:20 · Speaker 1

In model that can crack JE, I mean we have such models, good things are happening, right?

### 02:26:27 · Speaker 1

That's how the people did research, right? I mean, what was all this research all about is that changing the speed theta, looking at different forms, changing divergence metrics, different divergence metrics, and changing the way this optimization problem is solved. That's only the three things that you can do, though. Either you can change the model assumption, or you change the divergence, or you change the way you optimize. That is all people have been doing so far.

### 02:26:52 · Speaker 2

Oh so yeah I was thinking

### 02:26:53 · Speaker 4

whether we like the more uh the parametric form itself we can define a new one kind of I mean like based on the inputs

### 02:27:00 · Speaker 1

People have done that no I mean like from MLPs from logistic regressors they went to MLPs from MLPs they went to CNNs and then RNNs and transformers whatnot and all these kinds of different model assumptions right

### 02:27:16 · Speaker 1

But the recipe itself has to be changed. I mean, this is, by the way, this is also called divergence minimization or empirical risk minimization. People have tried to look at other ways of doing stuff as well. But the thing that has worked the most and one which is there in practice today is this.

### 02:27:34 · Speaker 1

Thanks. Yeah. Low gauge.

### 02:27:43 · Speaker 1

Low key Kumar can't hear you

### 02:27:49 · Speaker 1

Yes I can hear you now

### 02:27:52 · Speaker 2

Uh will we be always be able to come up with a divergence metric

### 02:27:56 · Speaker 1

that we define no yeah see if your question is will we always be able to evaluate the divergence metric the answer is no that's why you need a lot of trick all this GAN etc are actually kinds of tricks to evaluate this divergence metric will we be able to define a divergence metric of course I will just right now I will define a few metrics

### 02:28:16 · Speaker 4

I mean I'm waiting

### 02:28:18 · Speaker 1

Evaluation? No, not necessary. No, we can't know because there is one apparent problem with this. The apparent problem is that this divergence metric seems to ask for a px. We don't have px. That's our whole problem.

### 02:28:19 · Speaker 4

Oh

### 02:28:33 · Speaker 1

Right. Now, how do we evaluate these reversion metrics when you don't have PX is the question that we are going to answer in this course. There are different tricks to do that. Many people generally compute a bound on this. You can't find this exactly. So you compute an approximation to this, which is computing a bound. That is what this evidence lower bound and all this expectation maximization, VAE, etc. do. We will see all that in detail. You can always define it, but can you compute it always?

### 02:29:03 · Speaker 1

Perhaps not depending upon what divergence method you are looking at

### 02:29:08 · Speaker 1

That's the I mean see in this in the rest of this course we will only do this we will pick up e theta we will pick up d and we will see how to solve that optimization problem that's all that's all we'll do in this course next.

### 02:29:24 · Speaker 1

Uh okay yeah

### 02:29:27 · Speaker 3

Yes, uh, the first question is um, uh, the choice of the original distribution right is also a model parameter

### 02:29:34 · Speaker 1

So but in this case

### 02:29:34 · Speaker 3

So for instance in this case choice of the distribution the original distribution that you try to fit so so here you try to fit the normal distribution

### 02:29:43 · Speaker 1

No, no, no, please. See, one again, a kind request is please don't try to use the terms that I have not defined. I have never told what do you mean by fitting.

### 02:29:56 · Speaker 1

So, I have defined learning, training, models, etc. Please try to use my terms anyway. So, that that apart see there is we are not making an assumption on P x. We are only saying that my P x I mean we are making an assumption on parametric form. We are just saying there exists a P theta a family of P theta of which my P x is a member.

### 02:30:23 · Speaker 1

You get it? When I make an assumption, let's say that P theta is a normal distribution, I'm saying that my Px is also a normal distribution with certain mean and variance. That is the assumption that we are making. Understand? So you see it's a method of

### 02:30:36 · Speaker 3

That is something that we need to choose appropriate right

### 02:30:39 · Speaker 1

to choose other than right let me compete

### 02:30:49 · Speaker 3

There is a lot of noise

### 02:30:50 · Speaker 1

Yeah somebody are muted

### 02:30:54 · Speaker 1

Okay, so let me complete. I'm saying, suppose you may assume P theta to be a neural network. What I'm trying to say is that there exists a set of weights for this neural network which corresponds to my underlying PFs.

### 02:31:12 · Speaker 1

Now what is your question

### 02:31:14 · Speaker 3

No, but again here we have chosen normal, right? And then the parameters are only mu and sigma, right? But I could have chosen a different distribution also.

### 02:31:24 · Speaker 1

I told you, right? I mean, that is your model choice. You choose anything that you want. You are going to choose.

### 02:31:29 · Speaker 3

Yeah but yeah in general do we uh say that I mean the normal fits I mean or the normal is a better candidate

### 02:31:37 · Speaker 1

We can't care at all definitely not

### 02:31:37 · Speaker 3

It kind of was good I thought

### 02:31:41 · Speaker 1

Because you know if you take M-nest and if you want to model it by normal distribution you are doomed. There is absolutely no way that there exists a mu and sigma that would make I mean that that that will give you the distribution of M-nest data.

### 02:31:54 · Speaker 3

So that is something that we need to decide based on the data

### 02:31:59 · Speaker 1

I mean today people are like you have to have a family P theta that is expressive enough that would express a large class of density functions. No normal density does not express a large class of density functions at all.

### 02:32:14 · Speaker 3

Okay

### 02:32:15 · Speaker 1

Isn't it? Because it can't even express a binom, I mean like bimodal distribution. It can only express monom, uni-modal distributions and most data will be by multimodal distribution, right?

### 02:32:27 · Speaker 3

Okay and in case of neural network can we just go a little down

### 02:32:38 · Speaker 3

So so basically at the end you get a distribution but uh what you've shown here as the input is is the z the the normal standard

### 02:32:47 · Speaker 1

Yeah, so what does that mean? So you have a neural network that will take a normal distribution as an input and gives you a distribution as output.

### 02:32:47 · Speaker 3

So so what does that mean

### 02:32:58 · Speaker 1

modeling it that way no i can choose see p theta is our p is in our hand we can choose our p theta to be anything

### 02:33:06 · Speaker 1

we we can choose it to be anything now if i choose it to be a neural network then there are large sets of the distributions that my neural network can express

### 02:33:18 · Speaker 3

Okay so so it's it's kind of showing that you are transforming the normal distribution to a some complex distribution using neural network

### 02:33:25 · Speaker 1

Oh yeah there's neural network okay yes

### 02:33:28 · Speaker 3

Yeah okay understood

### 02:33:31 · Speaker 1

See even in the discriminative models you do the same thing no you have to estimate P of Y given X so you take a neural network

### 02:33:40 · Speaker 1

you take a neural network right that would take x as an input and gives you p of y given x this is exactly what a resident etc does know

### 02:33:51 · Speaker 1

Now you can either make this p of y given x 1 by 1 plus e power minus x e power w transpose x or something in which case it becomes a logistic regressor. That is your p theta, right? The choice that you make on the model is what you call a model.

### 02:34:08 · Speaker 1

You can make any choice for it. You can make it you can say that okay it's a logistic regressor. You can take any parametric form for that and estimate the parameters that's all yeah.

### 02:34:19 · Speaker 3

Yeah got it

### 02:34:21 · Speaker 1

Okay uh Rajat

### 02:34:27 · Speaker 4

Sir my question is if we have some ways to identify the real PX

### 02:34:34 · Speaker 4

using some tricks or methods that and you told we'll discuss later in this course then I didn't what we will achieve by by a mini divergence because knowing the real px is something that we all interested in right

### 02:34:47 · Speaker 1

No, we can't. I mean, the whole problem is there is no way to know real pHs. Every whole present.

### 02:34:58 · Speaker 4

how we will um

### 02:35:01 · Speaker 4

Diverge how we can create divergence

### 02:35:04 · Speaker 1

I have not told you that no I said yeah yeah that is one problem that is one question that I will answer in a while

### 02:35:04 · Speaker 4

I told you don't know I said

### 02:35:10 · Speaker 3

We'll directly sample from the try to sample

### 02:35:14 · Speaker 1

Please don't jump. There is a method to do. There is something called law of unconscious statistician and law of large number that we will use and we will use construct some bounds. Those are the things that we will do in this course. I have told you that that is some question that we will answer. Now, how do you evaluate the divergence metric if you don't know Px is a question that I will answer. I have not answered that. Okay. But I want you to understand the philosophy, right? I mean, like what is happening? You given data, assume some parametric form on underlying Px.

### 02:35:44 · Speaker 1

the divergence metric and then adjust your parameters of your p theta such that this divergence metric is minimized that's all i mean is this point clear i mean this is what i wanted to uh drive home if this is clear then the next question is of course what divergence metric what form how do you compute the divergence metric etc is what we teach in this course okay

### 02:36:07 · Speaker 1

Is that okay? Yeah okay any other question on this

### 02:36:20 · Speaker 1

Okay, now we'll take up the, so now the next question is given

### 02:36:29 · Speaker 1

a pair of density functions

### 02:36:42 · Speaker 1

functions how to measure

### 02:36:49 · Speaker 1

The distance or divergence between them

### 02:37:04 · Speaker 1

It this is a question that we should answer now okay because

### 02:37:09 · Speaker 1

One of the I mean there are three questions right how do you choose the model is the first question then the second one is how do you compute the divergence metric the third thing is like how do you optimize right I will take up the second question first we will take all questions one by one but this is more important right I mean this is the first step so given a pair of density functions how do you measure the distance or divergence between them is the question see there are enormous I mean like of many many ways to do this

### 02:37:39 · Speaker 1

So there are things called F divergences that we will be seeing

### 02:37:46 · Speaker 1

And there are things called you know Wasserstein's distance

### 02:37:51 · Speaker 1

optimal transport

### 02:37:56 · Speaker 1

And there are things called maximum mean discrepancy, MMD. We will look at all of these one by one. But yeah, so how do you estimate? So you understand, right? Suppose I've given you two points in Cartesian plane. How do I know how close and far off they are? Is that just compute the Euclidean distance, right? If this is x1, y1 and this is x2, y2, then you know how to compute the distance between them, right? x1 minus x2 squared, whatever, the usual Euclidean distance.

### 02:38:26 · Speaker 1

Now if you are given two density functions how do you define uh how do you measure divergences or distance between them is the question okay.

### 02:38:37 · Speaker 1

What we will do is

### 02:38:43 · Speaker 1

I will start with one famous divergence metric. Okay, so here is a question that I want to ask you.

### 02:38:50 · Speaker 4

We should start that

### 02:38:51 · Speaker 1

asked you that but see um as i said in this course we will be looking at uh uh models like vae's and gans and diffusion models and and so on right um which one do you want to start with you want to start with gans and then go to vae's or

### 02:39:12 · Speaker 1

VAEs and then go to GANs. So typically

### 02:39:16 · Speaker 2

No he's been good

### 02:39:17 · Speaker 1

Typically I used to do that. I used to start with VAEs and then goes to GANs. But this time I'm just thinking I should do the other way around. I'll tell you the reason. The reason is these diffusion models, right? Diffusion models are special cases of VAEs. They're actually hierarchical VAEs with a fixed encoding process. So now if I do VAEs and then do diffusion models, right? I mean, it will be fresh in your memory and I don't have to repeat things that I've done for VAEs. So now what?

### 02:39:47 · Speaker 1

uh perhaps we will do is you know GANs are a very different class of models and they are sort of like out of trend now people are not looking at GANs because of the problems that it comes with so let us start with adversarial learning okay and perhaps then we will go to VAEs

### 02:40:08 · Speaker 1

So having said that, I will simply give you an example of how to look at the divergence metric and how to compute that, etc. And then from next class, we will go to adversarial learning. So now let's take up this question. Given a pair of density functions, how to measure distance between them is the question. Now to do that, let us look at this. Suppose

### 02:40:39 · Speaker 1

There's an event

### 02:40:42 · Speaker 1

A okay that is in the set of events F okay and I'm interested in

### 02:40:56 · Speaker 1

Nah no my sorry

### 02:41:01 · Speaker 1

That quantifies

### 02:41:09 · Speaker 1

Amount of information

### 02:41:15 · Speaker 1

want of information

### 02:41:20 · Speaker 1

associated with it.

### 02:41:28 · Speaker 1

Okay, do you understand? So what are we trying to do now? We are actually trying to derive a famous divergence metric between two distributions, which is called the Kullback-Lieber divergence or KL divergence. Okay, and to do that, you know, we need some concepts of like basics of information theory. Okay, I'm just trying to derive that so that you understand where this actually came from. Okay, now suppose there's an event that is there in the in the in the in these event event space and what you are

### 02:41:58 · Speaker 1

interested in is you are interested in in a measure that would quantify the amount of information associated with it

### 02:42:06 · Speaker 1

Okay, now that measure, let's call that as some I of A. What properties do you seek in such a measure? I would say that the should be high.

### 02:42:19 · Speaker 1

Four

### 02:42:21 · Speaker 1

Less probable events

### 02:42:29 · Speaker 1

should be low for

### 02:42:33 · Speaker 1

High probable events

### 02:42:38 · Speaker 1

Do you agree? See, if I have to quantify the amount of information associated with a particular event, that measure has to be very high for less probable events, right? I mean, what I'm trying to say is if I tell you that the sun rises in the west tomorrow, then it has a lot of information in it, isn't it? But if I tell you that the sun rises in east tomorrow, then it does not have any information. Do you see what I mean?

### 02:43:09 · Speaker 1

So now this information measure that I associated with associate with a particular metric has to be such that it should be high for less probable events and low for high probable events. Now, if you take the asymptotic cases of it, right. So the information that is associated with the entire sample space should be 1.

### 02:43:35 · Speaker 1

Or let's say, okay, it can be that also. No, it can be infinity, right? It should be very high because the probability of sample space is one, right?

### 02:43:46 · Speaker 1

the probability of sample space is 1 because something when you when you when you when you conduct the random experiment some outcome will come that is what this is saying so the information that is associated with the sample space has to be infinity and the information that is associated with the null should be 0

### 02:44:05 · Speaker 1

Because I mean if I uh are the other way around, no sorry I think I've switched it sorry.

### 02:44:15 · Speaker 1

The information associated with the sample space has to be 0. The information associated with the null should be infinity. Correct. That's the asymptotic case of what I have just mentioned. You know, if I say that something from the sample space always happens, of course, I'm not telling you anything. If I say that, you know, something from the null space happens, then the null set happens and I'm giving you infinite information. The other property has to be that the amount of information, right?

### 02:44:41 · Speaker 1

that is associated with

### 02:44:49 · Speaker 1

union with the intersection that two events happen should be equal to the individual

### 02:45:06 · Speaker 1

Use me for this

### 02:45:10 · Speaker 1

The information associated with two events in union of two events happening have to be equal to the individual sum of individual informations if they are mutually

### 02:45:23 · Speaker 1

Independent

### 02:45:26 · Speaker 1

This makes sense right? I mean they have to add up basically I am saying that if there are two events happening together and if they are mutually exclusive then the total information that is conveyed by both of them have to be the sum of information conveyed by individuals of them. Does it make sense?

### 02:45:45 · Speaker 4

So should it be I of A intersection B equal to null set or just A intersection B equal to null set

### 02:45:49 · Speaker 1

Ah, yeah, yeah, yeah. Yes. Thanks. This is what it is. Yeah. Thanks for that. The typo. Okay. This is okay, right? Now, in fact, I mean, these measures were proposed by Shannon, okay, great information theorist who is responsible for all the communication that we have today, that he defined this thing, right, to be the surprisal of a particular event as the negative of logarithm of the probability, okay?

### 02:46:19 · Speaker 1

associated with that particular event A. You should not be writing this as script P because we have taken the script P for

### 02:46:30 · Speaker 1

distrib the distribution functions right it's the probability

### 02:46:35 · Speaker 1

This event A

### 02:46:38 · Speaker 1

Can you just take a minute and uh convince yourself that it it will uh

### 02:46:50 · Speaker 1

Satisfy all three properties that we saw

### 02:47:05 · Speaker 1

I'll just take a minute and verify this

### 02:47:27 · Speaker 1

Is it clear to all of you

### 02:47:39 · Speaker 1

Okay, so this is for one event, right? So now suppose

### 02:48:01 · Speaker 1

need to quantify

### 02:48:08 · Speaker 1

information

### 02:48:16 · Speaker 1

distribution right

### 02:48:20 · Speaker 1

What do we do? This is for one event right If we want to do it for the entire distribution how do we do that

### 02:48:32 · Speaker 2

integrate all the values

### 02:48:36 · Speaker 1

Just take an average right over all events

### 02:48:41 · Speaker 1

So let's say that this is a discrete disbl I'll do it in a discrete distribution in a

### 02:49:07 · Speaker 1

In a discrete let's say that it's a discrete distribution for the ease of understanding discrete distribution

### 02:49:19 · Speaker 1

So, now PMFs are probabilities right. So, I will say that I will have to look at the negative of log of the PMF function associated with particular value xi ok. I look at this and I take an average of this with all possible values that is.

### 02:49:42 · Speaker 1

which is

### 02:49:45 · Speaker 1

P x of xi and just simply take the sum

### 02:49:53 · Speaker 1

the values that it can take so this will quantify the average information

### 02:50:04 · Speaker 1

information associated

### 02:50:12 · Speaker 1

distribution

### 02:50:17 · Speaker 1

PX

### 02:50:19 · Speaker 1

Do you agree

### 02:50:21 · Speaker 1

This should give you, so because a negative log of pxi will give you the information associated with one event, one outcome, if you take the average of it over all the possible outcomes, then you will get the average information that is associated with.

### 02:50:36 · Speaker 1

the entire distribution

### 02:50:39 · Speaker 1

Okay, yeah, some people have questions here. Let me take a question.

### 02:52:09 · Speaker 1

Yes uh go on with questions

### 02:52:15 · Speaker 2

Sir I didn't get why the information associated with null set is infinity and also why information associated with event A is minus log of probability A

### 02:52:41 · Speaker 1

Okay I'm muted just give me a second I'll answer that

### 02:52:48 · Speaker 2

You can hear you sir

### 02:52:52 · Speaker 1

Hello can you hear me

### 02:52:53 · Speaker 2

Yes sir we can hear you

### 02:53:01 · Speaker 1

You never

### 02:53:11 · Speaker 1

Can you hear me now

### 02:53:14 · Speaker 2

Yes sir we can hear you

### 02:53:16 · Speaker 1

Okay, see the thing is, this is our definition. See what I want is, I want a measure that would take very high value for less probable events. It will take very low values for high probable events. Okay, that is the measure that I want. Now,

### 02:53:36 · Speaker 1

The asymptotic case asymptotic case which is the extreme case is the following that if you take the entire sample space

### 02:53:43 · Speaker 1

take the entire sample space then that is the most probable event isn't it

### 02:53:51 · Speaker 2

Yes that will be

### 02:53:53 · Speaker 1

That should have zero information

### 02:53:58 · Speaker 1

Okay similarly the least probable event which is the null should have infinite information

### 02:54:10 · Speaker 2

I understand that probability part but how come that gets reversed when we associate with the information

### 02:54:19 · Speaker 1

That is how we want, right? See now, what are we desiring? See, okay. So I'll tell you some historical thing, right? The question that was asked is, if you say that an event has happened, you tell me how much information is conveyed in that is the question.

### 02:54:37 · Speaker 1

Now intuitively don't you think that an event that has very high probability or which is very high which is very highly probable conveys very less information

### 02:54:51 · Speaker 1

Historically what happened is the question Shannon was asking is if I have to compress the I suppose I want to you know I want to pass a message from point A to point B and I want to understand it now

### 02:55:02 · Speaker 2

And it's good to know

### 02:55:04 · Speaker 1

Got it now

### 02:55:05 · Speaker 2

It's easy to understand

### 02:55:08 · Speaker 1

Yeah, so I mean we defined the information this way information content associated with an event this way that it is the negative of log of probability associated with it. That's all.

### 02:55:27 · Speaker 1

Okay uh artistic

### 02:55:44 · Speaker 1

I just look at it no the probabilities get multiplied if the events are independent and there is a log right so log will get summed

### 02:55:55 · Speaker 1

Probability of A and B a pro log of A B is log A plus log B isn't it

### 02:56:01 · Speaker 2

Okay okay if they're distinct okay okay yeah I understand

### 02:56:05 · Speaker 1

Let's let's I give you a minute to just plug that yeah yeah I forgot that

### 02:56:08 · Speaker 2

Yeah yeah I forgot that they are disjoint also so yeah okay

### 02:56:13 · Speaker 1

Okay so

### 02:56:13 · Speaker 2

Yeah thank you

### 02:56:15 · Speaker 3

are in this average function will it be like capital P right this small p was for probability density

### 02:56:23 · Speaker 1

I'm saying it's a discrete distribution right so this is PMF probability mass function which is a probability by itself

### 02:56:33 · Speaker 3

Sorry uh can you tell me

### 02:56:34 · Speaker 1

See I said that it is a discrete distribution therefore this p is a PMF function, probability mass function which is an it is actually a valid probability.

### 02:56:48 · Speaker 1

Great thinking Paul

### 02:56:58 · Speaker 1

Okay some it

### 02:57:01 · Speaker 2

So this union property that is there basically I a union B is I a plus I b but if we consider a union of a with null set means this the intersection will also be a null but then this property will not hold no because a union null will be a itself but then if we add them up it will be infinity

### 02:57:28 · Speaker 1

No, A union null is, no, A union null is A, okay. You can still represent that as I of A plus I of null, right?

### 02:57:37 · Speaker 2

But I of null is infinity no So I of a plus I of null will be infinity

### 02:57:39 · Speaker 1

Yeah I know

### 02:57:46 · Speaker 1

are saying um I mean maybe I should just add that or

### 02:57:56 · Speaker 1

Yeah that will solve it that's the next case

### 02:58:02 · Speaker 1

Other tier

### 02:58:05 · Speaker 4

Also similar, just an add-on to that question, if B was, for example, an A complement over here, so I of A plus I of A complement, that

### 02:58:13 · Speaker 3

equal to i of omega the leg the

### 02:58:18 · Speaker 3

That should be zero.

### 02:58:20 · Speaker 1

Yeah of course

### 02:58:23 · Speaker 1

Post per definition

### 02:58:25 · Speaker 1

Okay, so now there's a name for this. Do you know what this list is called?

### 02:58:39 · Speaker 1

Sorry it's quite

### 02:58:42 · Speaker 1

So this is called the entropy yeah this is called the

### 02:58:42 · Speaker 3

It's quite cool

### 02:58:47 · Speaker 1

This is the entropy associated with the distribution that is it's simply the average information that is associated with the distribution is called the entropy of that distribution.

### 02:58:56 · Speaker 1

Makes sense now? Makes a lot of sense. So basically you define the information content for an event and just take an average over all possible events that are there and that will give you the entropy which is the average information that is conveyed by a distribution. Is that fine?

### 02:59:19 · Speaker 1

Okay so now I actually have to now define the cross entropy and

### 02:59:26 · Speaker 1

on it's 12 20 already we started 15 minutes late do you mind if i continue for 10 more minutes or should i stop shall we take it the next class

### 02:59:38 · Speaker 1

See if there is even one person who wants me to stop no I will stop

### 02:59:43 · Speaker 1

because I should not be continuing

### 02:59:47 · Speaker 1

Is there anybody who wants me to stop now

### 02:59:56 · Speaker 1

Let me know if you

### 02:59:59 · Speaker 1

to go somewhere and you have stop I'll stop it here

### 03:00:07 · Speaker 1

So let me take 10 more minutes now suppose

### 03:00:30 · Speaker 1

Old entity functions

### 03:00:37 · Speaker 1

B and Q now if I compute

### 03:01:02 · Speaker 1

So looks like my screen has frozen

### 03:01:30 · Speaker 1

Wording thing this will give you

### 03:01:41 · Speaker 1

And somebody tell me what does this give me

### 03:01:47 · Speaker 1

Can I interpret this as

### 03:02:00 · Speaker 1

Can I interpret this it this way Can I say that it's the average information in Q about P

### 03:02:13 · Speaker 1

In all of these cities

### 03:02:20 · Speaker 1

This also has a name do you know

### 03:02:23 · Speaker 4

So central piece

### 03:02:24 · Speaker 1

This is the cross entropy

### 03:02:33 · Speaker 1

brain BLANK

### 03:02:38 · Speaker 1

If I take this

### 03:02:42 · Speaker 1

and subtract virus

### 03:02:45 · Speaker 1

How do I interpret this

### 03:02:53 · Speaker 1

Can I say that this is the information

### 03:02:58 · Speaker 1

that this is the extra information

### 03:03:14 · Speaker 1

In B

### 03:03:20 · Speaker 1

not in cube can i call it this way

### 03:03:32 · Speaker 2

Sir the first term tells us about like gives us the information about Q right

### 03:03:39 · Speaker 1

information about uh p like if us you know here here cross entropy is a cross entropy tells you that how much information does q has about p

### 03:03:54 · Speaker 2

So about means uh

### 03:03:56 · Speaker 1

Oh dear

### 03:04:03 · Speaker 1

Right and it of p tells you the information in p which will take the difference between them

### 03:04:11 · Speaker 1

Do you tell me how much extra information is there with P that

### 03:04:17 · Speaker 1

The Q does not have

### 03:04:20 · Speaker 2

And it should be subtracted by HQ right

### 03:04:23 · Speaker 3

It's the terms should be reversed right

### 03:04:26 · Speaker 1

You mean hp minus hq z

### 03:04:30 · Speaker 2

HP minus HPQ

### 03:04:34 · Speaker 2

Otherwise like this inter like this is giving a sense that the term will be negative won't it sir?

### 03:04:41 · Speaker 1

See that is a minus log there no

### 03:04:48 · Speaker 1

minute la minus law also it will be

### 03:04:55 · Speaker 1

Like this one, how does this look like? This is uh...

### 03:05:15 · Speaker 1

This is correct because there is a negative there no

### 03:05:22 · Speaker 1

So in the definition of entropy, there is a minus. So when you subtract it, the minus will just go away and it will become plus.

### 03:05:30 · Speaker 1

Understand so basically the difference between these two will tell you the extra information in P that is not in Q

### 03:05:38 · Speaker 1

Is it okay

### 03:05:41 · Speaker 1

Now this is equal to

### 03:06:00 · Speaker 1

is correct no so there's a minus here there's a minus of minus will become plus so it will be p of px log px and this term has a negative here so log a minus log b is log of a by b is this okay

### 03:06:25 · Speaker 1

Do you know the name for this? This is the name this is the

### 03:06:29 · Speaker 3

Need it to be

### 03:06:36 · Speaker 1

This is one divergence metric that we will study in this course that the clear divergence between these two distributions px and qx

### 03:06:48 · Speaker 1

Play Doh and buy

### 03:06:51 · Speaker 1

it's log

### 03:06:57 · Speaker 1

In fact this is the last function that is used in most of the supervised discriminative machine learning to minimize the KL divergence between Px and P theta

### 03:07:07 · Speaker 1

Okay, see the reason I did all this is to make you appreciate why this is a good metric. So I'll leave it for tutorials, okay, to show that AL is 0 if and only if PX matches QX. Only if the underlying distributions matches, then the divergence will become 0. Obviously, right, because the amount of information that is there in Q about P

### 03:07:37 · Speaker 1

should not be more than what P has itself. So only if P and Q are exactly the same distributions, then the cross entropy matches with the entropy. And that is when the KL divergence becomes zero. So now this becomes a metric to measure how far a given distribution is.

### 03:07:57 · Speaker 1

So now we will trace back to what we did. So we wanted to define or compute a divergence metric between the true density and the assumed parametric density, you know.

### 03:08:06 · Speaker 1

Quantify how far it goes KL is one way to do it

### 03:08:12 · Speaker 1

Does it make sense

### 03:08:15 · Speaker 1

So in the next class what we will do is that given a particular model how do you compute the KL and how do you optimize for it etc is something that we will see in the next class okay so

### 03:08:28 · Speaker 1

When you come to the next class, please come prepared. Just read whatever we have done in the previous classes and also read about entropy, cross entropy, KL, et cetera, so that you have idea about what we are talking.

### 03:08:45 · Speaker 1

Okay then, we are done for today. See you in the next class. And again, reminding, right, if you want to express something, you know, have some opinion, the feedback form is there. It is completely anonymous. You can just go and put in whatever your comments are if you want. You go to my webpage. There is this ADRL course webpage and there is that feedback form and you can just simply put in your comments if you have any.

### 03:09:14 · Speaker 1

Okay well that's all for today see you next week

### 03:09:19 · Speaker 1

Have a nice week and bye bye

### 03:09:21 · Speaker 3

Okay

### 03:09:22 · Speaker 1

Okay, just a second. Next week, next Saturday is this Ganesha Tirthi. That's okay, right? We can still have a class.

### 03:09:36 · Speaker 1

Yeah that's it

### 03:09:39 · Speaker 1

Okay anyway we are recording if people want to take off they can take off and see that later

### 03:09:45 · Speaker 1

I'll have to ask my mother if that is possible but yeah I'll convince her okay see bye

### 03:09:55 · Speaker 3

Yes thank you sir
