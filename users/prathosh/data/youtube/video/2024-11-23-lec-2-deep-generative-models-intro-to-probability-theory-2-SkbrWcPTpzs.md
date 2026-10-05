---
id: SkbrWcPTpzs
title: Lec - 2 - Deep Generative Models Intro to Probability theory 2
date: '2024-11-23'
url: https://www.youtube.com/watch?v=SkbrWcPTpzs
description: ''
author: prathoshap5226
duration: 03:10:25
model: saaras:v3
transcript: true
---

# Lec - 2 - Deep Generative Models Intro to Probability theory 2

## Transcript

### 00:01:59 · Speaker 0

shall we begin?

### 00:02:03 · Speaker 1

Yes sir

### 00:02:05 · Speaker 1

Okay

### 00:02:06 · Speaker 5

Okay, so good morning all of you. Start. I hope you had a chance to brush up some of the fundamentals of what we discussed the last time. I will just quickly recap and then take it from there.

### 00:02:24 · Speaker 5

So what we did the last time was uh said that uh most problems in science and engineering happens to be approximating functions, right?

### 00:02:36 · Speaker 5

So, we

### 00:02:42 · Speaker 5

We catch the problem of function approximation as that when you are given pairs of elements which are of the form x y, y i.

### 00:02:53 · Speaker 5

where X I comes from the domain of the function and Y I comes from the range of the function. uh the task is to find the uh underlying function that is there, okay? You saw some examples also, right? uh where the underlying function happens to be simple functions like linear and quadratic functions.

### 00:03:12 · Speaker 5

So why do we need to do function approximation? That is because uh one of the major reasons is that function approximation enables prediction, right? So if you know what the relationship between the uh the domain, basically elements of two sets called the domain and range, if you are given a new element in the from the domain set, you can predict or estimate what is the corresponding element in the range set, right? So that is why function approximation is important and necessary.

### 00:03:49 · Speaker 5

Okay, so the problem was that what if the mapping between the sets cannot be found using like known mathematical tools. Mostly the solution is that you come up with new mathematical tools. So

### 00:04:06 · Speaker 5

Even this pretext context probability theory was introduced. So basically we need that because the relationship between the given sets are rather complex and do not adhere to the existing mathematical framework.

### 00:04:20 · Speaker 5

saw some examples of it, right, where uh where the elements of the domain happen to be coming from like R P comma Q, uh

### 00:04:32 · Speaker 7

Well

### 00:04:33 · Speaker 5

it corresponds to every element in R P Crock's Q space corresponds to a picture, okay? And what you need is the range space comes from one of the two values, like these are called genders. So relationship between the pixel values and the idea of genders cannot be modeled using existing mathematical tools. So that was one example and we saw some textual example where you have a document and document gets mapped to an abstract idea.

### 00:05:03 · Speaker 5

called emotion and similarly speed signal to phoneme or words and all that right? So what's the idea range set is non measurable in the sense that they are abstract okay? You can't measure emotion you can't measure gender you can only give labels associated with it. But the domain can be measured. Okay? As I said even to solve these problems historically people attempted to solve these problems using classical mathematical tools and give you examples of

### 00:05:37 · Speaker 5

Yeah, speech and images where speech signal was being modeled from a

### 00:05:43 · Speaker 5

linear system or non-linear system perspective where you have the signal and you model the the signal the output as concatenation of several linear systems or waveguides and you estimate the parameters of it. Similarly with image processing where you and you wanted to analyze an image and that analyzing an image was conceived in a hierarchical manner where you detect edges and you know you compose object for matches and

### 00:06:18 · Speaker 5

primitive shapes and then you try to make sense of what it is. Okay? But these methods mostly uh did not yield human level performance. Okay? Because uh this constructing the functions that would map uh speech signal to phonemes or pixel values to complex object relations are not trivial.

### 00:06:44 · Speaker 5

So then came probability theory. I mean it was actually not that, you know, historically speaking statistics and probability theory was around, okay? But the the application of probability theory as a mathematical tool to solve these kinds of problems was not that popular. uh before let's say nineteen late nineteen eighties, okay? The probability theory probabilities probabilistic tools were not the go to tools to solve these kinds of problems. But yeah, so people realized that

### 00:07:14 · Speaker 5

using classical functional approximations may not be the best thing to do while you want to solve these kinds of problems. Okay. So with this context, right, we were looking at what probability theory was. So, okay, so maybe I'll pause for a while here. Any questions so far? This is all some

### 00:07:38 · Speaker 5

historical context. Any questions here?

### 00:07:43 · Speaker 5

Okay, let's continue. So we introduced introducing probability theory. So what is it basically? It's it allows uncertainty by construction, okay?

### 00:07:54 · Speaker 5

what is what does that mean that the functions that we are talking about which are mappings from the domain and range can possess quote unquote uncertainties we want to quantify what uncertainties is. Uncertainties are. So uncertainties what do what does it allow the the user to is that it makes functional learning feasible. Okay because we saw that functional learning was infeasible in in so many cases and it it sort of helps creativity because

### 00:08:24 · Speaker 5

there is uncertainty I'll give you that example of an artist right I mean if the artist does not know a priori what sort of uh what sort of art is is being created and that's why uh creative or new stuff gets generated out of it. Okay uh

### 00:08:42 · Speaker 5

we could try to concretize some of these ideas that

### 00:08:46 · Speaker 5

Yeah. Probability theory starts from this this fundamental concept called a random experiment or a random trial. So as I said, in the whole of probability theory, this is one thing that has not been mathematically defined, right? I mean, what is a random experiment or a trial? It's just said that it is it is a process that gives rise to a set of outcomes, that's all. Okay. So anything that that gives rise to set of

### 00:09:16 · Speaker 5

outcomes is called a random experiment or a trial. So collection of all the outcomes of or outcomes are the observations or outputs of a random experiment are enumerated in a discrete set and that set is called a sample space. Okay. Need not be discrete set, it can be a real space as well. Let's not go there. Let's just say that the set of all outcomes are enumerated in a in a in a

### 00:09:46 · Speaker 5

in a in a set and that's called a sample space. So examples of random experiment is that you toss a coin and the sample space comprises of head and tail and you roll an n phase die then the sample space comprises of n phases of the die and we also saw some practical examples right where taking a picture of a person can be looked into as a random experiment where the sample space happened to be uh different people right uh every time you get different people. recording a speech signal happens to be a sample space and so on

### 00:10:24 · Speaker 5

Okay. So, uh this was the uh sample space. And we are not, I mean it's not enough if we only have sample space, right? Because remember that finally our intent is to map a picture to a gender or these kinds of uh ideas. For that, what we needed was something called a measure, okay? It defined a measure. So what is what what is a measure? So given a particular set, take a subset of a set and for each subset you associate

### 00:10:54 · Speaker 5

a scalar, right, or a non-negative number such that it has some properties. And the properties are the following that you take any subset of any one set, the measure has to be non-negative, non-zero. And if you take the null set, the measure has to be zero. And if you take the measure of union of two sets such that the intersection of them is null, then the results have to add up.

### 00:11:19 · Speaker 5

So we also saw an example of a famous measure that all of us know of which is the Lebesgue measure which is the length and the area measure in length area and volume measure in R one R two R three etcetera. Similarly, one can define a measure on sample space, right? You have collection of all possible outcomes of an atomic experiment is what is called as a sample space. Like if F denotes the set of subsets of all possible subsets of omega, then a measure which is also called the probability measure is defined

### 00:11:49 · Speaker 5

on the subset of the the sample space, okay? Probability measure is a measure that is bounded upper and lower bounded between zero and one, okay? It can be interpreted as the uncertainty associated with a subset of the sample space. The subset of sample space is also called an event, okay? So probability measure is just like the Lebesgue measure gives you the sense of

### 00:12:19 · Speaker 5

okay of a subset of a real number. Sorry, I'm sorry. So it gives the notion of a length of a subset of a real of of the real the set of reals. Probability measure can be interpreted right as some measure that is that is giving you the sense of uncertainty associated with certainty or certainties like uncertainty associated with a particular subset of the sample space.

### 00:12:48 · Speaker 5

Yeah, is what I've said, length or areas on RR2 is similar to probability on omega.

### 00:12:55 · Speaker 5

Okay, so this was okay. Now we have the the probability triplet.

### 00:13:05 · Speaker 0

which is generally called the

### 00:13:20 · Speaker 0

the probability triplet that is a sample space

### 00:13:25 · Speaker 5

the subset which is the event space and the probability measure, okay? This is typically the probability triplet.

### 00:13:37 · Speaker 5

I mean again you can compare this with the when every time you define a measure you get something like this a triplet like this. In R no you have R you have subsets of R which are also called the Borel sigma algebra and you have the length or the level equation right. Similarly you have a probability triplet that is omega and the subsets of omega and probability equation okay. Now okay uh there is another problem. I mean remember that our goal is always to

### 00:14:07 · Speaker 5

learn that association between the pictures and abstract concepts like gender or whatever. Okay? To do that, we need something more. Okay, there is a measure now. Okay, we can measure. We associated a measure with the outcomes of

### 00:14:27 · Speaker 5

random experiment. But that's not enough because elements of sample space are not observed in practice. Okay? What do I mean by that?

### 00:14:35 · Speaker 5

what do I mean by that is that if the random experiment is taken as observing a particular person, okay, and taking a picture, we don't get to see that person or rather we don't, yeah, we don't get to see that person, which are the elements of sampling space. But what do we get? What we get to see is

### 00:15:03 · Speaker 5

an observation rather some measurement, okay?

### 00:15:07 · Speaker 5

that we do on the elements of sample space. So this has to be appreciated because otherwise, right, I mean this this notion of random variables will will will not be appreciated better. Let me repeat what I'm saying. See, while the elements of random experiments are

### 00:15:29 · Speaker 5

are enlisted in a sample space. In practice, we don't get to observe the elements of sample space.

### 00:15:36 · Speaker 5

Now why is that? In the example of the pictures that I said, okay? The random experiment is that you are, you know, you pick a person, take a picture, right? And a picture, an abstract object picture is something which is an element of sample space. You don't get to observe that. What do you get to observe is a surrogate to that particular picture.

### 00:16:03 · Speaker 5

Okay? So now we need to somehow uh define one other concept, okay? That would uh map the elements of sample space to something that we observe so that we can work with them.

### 00:16:18 · Speaker 5

is this idea clear? I mean this is a this is a central idea, right? Because we never go to sample space while we are working in in in machine learning. We only work on the observations or rather the instantiations of what are called as random variables, okay? Why is that? Why is that is because when we when we do a measurement, right? using some sensors or something, what we observe are some surrogates of the elements of sample space but not the elements of sample space at all, okay?

### 00:16:48 · Speaker 5

how do you model that mathematically is the question. uh we model that using a function uh that is mapped from the elements of sample space to R D. Okay. D is an arbitrary number depending upon what sort of application or data that we have uh D gets fixed. The example the in the example that we saw if the sample space happens to be uh people or pictures of person

### 00:17:18 · Speaker 5

then this function, okay? this function will take every picture or every person and maps it to a real number.

### 00:17:29 · Speaker 5

Okay, in P Q dimensional space. What is this P Q? uh We envisage this as a picture, grid of P Q pixels, right? Where every element in P P comma Q uh grid happens to be a real number. So every picture happens to be a

### 00:17:50 · Speaker 5

real number uh in P Q dimensional space. So now this function takes a picture right or takes and takes a person and maps it to a real number in R P Q dimensional space in which is what we observe.

### 00:18:04 · Speaker 5

Yeah, I will take the questions in a while. uh Please keep that hand raised, of course, virtually. Otherwise, the hand will start paining. uh Okay. uh In the second example, uh the sample space has a head tail, okay? And the function maps the head tail to, let's say, zero one two numbers.

### 00:18:30 · Speaker 5

Okay. So this is here is a function. The function takes elements of sample space and maps it to some d-dimensional real numbers. Okay. And this function is what is famously called as a random variable and as I said it's a misnumber in the sense that it is actually a deterministic function that takes elements of sample space and maps it back to maps it to some real numbers d-dimensional real numbers.

### 00:19:01 · Speaker 5

Okay. Now, uh the data that we are given, the data that we are given, okay? Uh what is that? They are actually the members or elements from the range space of a random variable. What do I mean by that? When we let's say that you know we have we are working with MS data set or some uh imaginary data set. What we get are elements from this R P Q dimensional space, right? We get multiple vectors of of of dimension R P Q.

### 00:19:31 · Speaker 5

Q. What are those? They should be conceived or seen as elements, okay, coming from the range space of this function called random variable.

### 00:19:43 · Speaker 5

okay? Because the uh the um uh elements from the sample space are not observed, okay? Uh what is happening is you should imagine that okay, there was a sample space, some random experiment was happening and there is this function which is called a random variable that has mapped the elements of sample space to the set of real numbers. What I'm seeing are the set of these real numbers which are nothing but the elements from the range space of the

### 00:20:15 · Speaker 5

random variable which is a function. And you should imagine that there exists an underlying sample space, uh which would tell you what was the random experiment that that was being conducted.

### 00:20:25 · Speaker 5

Okay, so this is till that till this we had seen in the last class. So now we will continue from here. Yeah, so any questions here? Please raise your hands, I'll call out names.

### 00:20:38 · Speaker 0

A

### 00:20:48 · Speaker 0

somebody tell me, ha, this is

### 00:20:52 · Speaker 0

I won't

### 00:20:58 · Speaker 1

I want a new page. How do I get a new page here?

### 00:21:01 · Speaker 6

Sir, you can unselect this and on the bottom there is a new page button. Page plus page.

### 00:21:08 · Speaker 6

in that column only.

### 00:21:12 · Speaker 1

Hello

### 00:21:13 · Speaker 6

Can you open that once again?

### 00:21:17 · Speaker 0

Yes

### 00:21:18 · Speaker 6

on the bottom there is a

### 00:21:18 · Speaker 1

you know

### 00:21:18 · Speaker 0

here we have got it. So here

### 00:21:25 · Speaker 0

Next three

### 00:21:29 · Speaker 0

What was the naming convention? It was L2

### 00:21:55 · Speaker 0

Okay so

### 00:22:02 · Speaker 0

stimulus

### 00:22:10 · Speaker 0

Where was that thing which

### 00:22:22 · Speaker 0

had sample space

### 00:22:27 · Speaker 1

the set of subsets and a probability measure. Okay? Now this

### 00:22:38 · Speaker 1

show that, yeah.

### 00:22:42 · Speaker 1

There was this function called

### 00:22:44 · Speaker 5

the random variable that

### 00:22:47 · Speaker 5

Look, elements of sample space mapped into some two dimensional real numbers. Okay. This is where we have. Okay. Questions. uh Yeah, Prajagopal.

### 00:22:59 · Speaker 4

Hi sir, Good morning

### 00:23:01 · Speaker 5

one yeah

### 00:23:01 · Speaker 4

So sir, I just want to analyze a little bit more on the concept of random variable in the context of our problem of taking a picture and understanding whether it's what gender it is. So in that concept, as you said, the picture that we clicked is a set is a member of the right hand side of the random variable definition that is the R D set.

### 00:23:16 · Speaker 5

So in that

### 00:23:25 · Speaker 5

Brijbhopal, yeah. See, I I encourage you to use mathematically correct terms, huh? Don't call it the right-hand side of random variable, call it the range space of range space of random variables, yeah.

### 00:23:34 · Speaker 4

Okay

### 00:23:37 · Speaker 4

range

### 00:23:39 · Speaker 4

Days

### 00:23:40 · Speaker 4

rain space. All right.

### 00:23:41 · Speaker 5

Yeah. So, so every picture, every piece, every point in data that you get is an element of the range space of random variable.

### 00:23:41 · Speaker 4

Sir, so every

### 00:23:49 · Speaker 4

Got it. Now, I I want to imagine a scenario sir like it's possible right that we take multiple pictures of the same person where he is standing in different poses. So

### 00:23:50 · Speaker 5

um

### 00:24:00 · Speaker 5

um

### 00:24:02 · Speaker 4

हाउ डस द आइडिया ऑफ रैंडम वेरिएबल हैंडल दैट? लाइक सो देयर इज वन एलिमेंट ऑफ सैंपल स्पेस दैट इज बीइंग मैप्ड टू डिफरेंट रेंजेस, डिफरेंट एलिमेंट्स इन द रेंज सेट, करेक्ट? नो, नो, नो।

### 00:24:13 · Speaker 5

No, no, no, no. See, a function cannot map one element to multiple elements, no? One to many mapping is not a valid function at all.

### 00:24:23 · Speaker 4

Yeah

### 00:24:23 · Speaker 5

Okay. uh So that does not become a valid function. So it cannot map the picture of one person to multiple numbers. But why I mean that's a good question, right? I mean that's actually a good question. Let me answer that. See, in that case, uh the way you should imagine is that the sample space itself has pictures of that person standing in multiple angles.

### 00:24:51 · Speaker 5

See, while while I conceived, I mean, the example that I gave, I I understand why that question is question arose, right? In the the way I I I I gave you the example of sample spaces, I I said that uh every person corresponds to one object in the sample space, right? It may not be the case, right? I mean, if you are taking, I mean, that is in the case where you take one picture of a person. If you are taking multiple pictures of a person, then all those pictures become elements of the sample space.

### 00:25:09 · Speaker 8

Yeah

### 00:25:21 · Speaker 5

space and that variable will map it to different real numbers for different angles.

### 00:25:28 · Speaker 5

A function by definition cannot have one to many mapping.

### 00:25:32 · Speaker 4

Got it. So we are still not at the place. So sample space has all the possible poses, everything related to every person on this planet. But we are still a little away from our final goal where we then analyze the sample space and all the possible poses and find out, okay, these are all actually the same person.

### 00:25:32 · Speaker 5

Got it

### 00:25:38 · Speaker 5

related to every

### 00:25:40 · Speaker 5

Correct, correct.

### 00:25:50 · Speaker 5

and see that we will do. See we are I I I have not set up the the next problem yet. I'm just telling you what the sample space is and what random variable does, right? Got it. Now, uh that's why I mean actually you brought up a nice point. Uh see, uh I hope that all of you got the question. The question was that uh in the example that you gave there was one person and uh like uh taking the picture of one person was one element in the sample space.

### 00:25:53 · Speaker 4

I have

### 00:25:57 · Speaker 4

Okay

### 00:26:00 · Speaker 4

Got it

### 00:26:21 · Speaker 5

then if if you take multiple pictures of that same person how do you handle it? Now, the answer to that is that see you conceive what is there in the sample space.

### 00:26:32 · Speaker 5

meaning the user would define what a sample space is. because the random experiment is something that is a user defined idea, you see. but what I wanted to tell you is that when you have like let's say multiple elements from R T R P Q or Q which are which are which are images, right? or or the set of pixels. you have to imagine that this is the result of this process where there was a sample space and there is a function which is random variable that has mapped the elements of the sample space to this R D

### 00:27:07 · Speaker 4

Yeah

### 00:27:08 · Speaker 5

Okay, there exists some sample space, some underlying sample space and you construct that sample space accordingly, right? I mean it doesn't matter how you construct it. And the good thing is that you don't have to even worry about the sample space once you get the outcomes of I mean once you look at the range space of random variables, that's enough. That's that is why you define the random variable in the first place. Okay?

### 00:27:34 · Speaker 4

uh okay so the way I understand this sir what you said triggered another thought that um ultimately what we want to understand is the gender right even if the same person repeats again and again the gender stays the same so it's irrelevant for the problem is that how I should No no

### 00:27:49 · Speaker 5

No no no, see don't worry about that's what I said, don't worry about the gender part yet, okay? Just just think just think about having a few data points. Yeah. Which are pictures. Now how do you see those data points is something that we are looking at right now. How do you look at the labels is something that we'll come to in a while, okay? For now just imagine that you have a set of data points.

### 00:27:54 · Speaker 4

OK

### 00:27:55 · Speaker 4

just

### 00:28:03 · Speaker 4

Okay

### 00:28:11 · Speaker 4

Okay

### 00:28:16 · Speaker 4

Got it.

### 00:28:16 · Speaker 5

Okay? These data points are seen as the elements of the range space of a random variable and the moment you talk of a random variable there exists an underlying sample space which is giving you some elements. That is how you should look at it. Okay?

### 00:28:31 · Speaker 4

Sure sir. So we're only talking about representatives right now. Got it.

### 00:28:33 · Speaker 5

Now, now the data, data, I mean, data, yeah, sorry, like, not labels, I'll come to the labels in a while. See, for instance, right, in generative modeling, you don't have labels, right? You only have data. Let's look at the representation of data now, from a random variable perspective, then we will come to the labels in a while, okay? Any other questions on this? This is very important, right? I mean, this understanding is very important because from, this is the last class when I'll be talking about the sample space.

### 00:28:35 · Speaker 4

data, yeah, sorry, like

### 00:28:44 · Speaker 4

only

### 00:28:54 · Speaker 4

any other question

### 00:29:03 · Speaker 5

from like next class onwards we'll only talk about random variables and distribution functions. So you have to understand like thoroughly what is going on. So if you have questions this is the opportunity for you to ask them.

### 00:29:18 · Speaker 1

Any other question?

### 00:29:25 · Speaker 1

Vivek

### 00:29:25 · Speaker 11

some so maybe the uh the trick is in designing the I mean coming up with a correct probability measure.

### 00:29:34 · Speaker 11

for a given problem

### 00:29:34 · Speaker 5

Yeah. See, probability measure is, I mean, I didn't get your question. I mean, that that was sort of assertion, right? What is the question?

### 00:29:47 · Speaker 11

okay. So, uh in one sense I understand that this is still only uh talking about uh understanding the uh um the basic data points. But uh when we move on to the next step, when we start try to assign labels, then probably we have to uh worry about a probability measure.

### 00:30:11 · Speaker 11

we have to model that path.

### 00:30:12 · Speaker 5

Uh hold on I've like as I said no please try to if you have questions on things that I've said already do ask and let's not jump. I'll I'll come to that. I'll come to all that in a while. Yeah. Yes.

### 00:30:23 · Speaker 0

Yes

### 00:30:25 · Speaker 1

Oops

### 00:30:26 · Speaker 1

Any questions on things that we did so far?

### 00:30:38 · Speaker 9

Hello sir, can I ask one question?

### 00:30:40 · Speaker 0

ಜಸ್ಟ್ ಸೆಕೆಂಡ್ ಹಾಯ್. ಎಸ್ ಸಚಿನ್.

### 00:30:43 · Speaker 5

Hello

### 00:30:44 · Speaker 9

So sir I was asking like this random variable function is like very important we are converting this sample space into some range space. So as per our problem like different

### 00:30:56 · Speaker 5

converting, hold on, hold on, converting sample space into real numbers.

### 00:31:01 · Speaker 9

Yes

### 00:31:03 · Speaker 5

Don't call it range space, real numbers. See what is range? When you have a function, you have a domain and a range.

### 00:31:09 · Speaker 9

Right

### 00:31:10 · Speaker 9

Kara

### 00:31:10 · Speaker 5

Correct. So random variable is a function that takes sample space and maps it to real numbers.

### 00:31:16 · Speaker 9

So for a given sample space, uh there we can define multiple ways uh for or we can define multiple functions uh this random variable function, right? Based on our function.

### 00:31:17 · Speaker 5

So

### 00:31:27 · Speaker 5

Very good, very good observation. Yes, you can and that is why you know that is a model.

### 00:31:33 · Speaker 5

That's basically what a model is. So ultimately we will see that entire machine learning is about finding this underlying probability measure. Okay, why does the probability measure change? The probability measure changes because, I mean when the probability measure changes, the random variable changes, right?

### 00:31:53 · Speaker 5

You can actually you can. Yeah. So you can there need not be one random variable corresponding to a random sorry particular sample space there can exist multiple random variables. Yeah.

### 00:32:03 · Speaker 9

ओके थैंक्स

### 00:32:04 · Speaker 5

But but what is important is that the the moment you have some data you should imagine that there has already been a random variable that has been applied to it. Do you understand?

### 00:32:18 · Speaker 9

you know, like data is in its raw form, right? Like images or speech or

### 00:32:24 · Speaker 5

you have data. The moment you have data, the moment you have data, you should all you should know that there has been some random variable that has been operated on the sample space.

### 00:32:38 · Speaker 5

in practice what you get is data.

### 00:32:38 · Speaker 9

practice what you get is data

### 00:32:41 · Speaker 9

Okay

### 00:32:42 · Speaker 1

cut it

### 00:32:43 · Speaker 1

Yeah

### 00:32:44 · Speaker 0

Huh?

### 00:32:45 · Speaker 1

Yes sir.

### 00:32:46 · Speaker 0

Okay

### 00:33:02 · Speaker 0

Okay. uh Yeah, I think Bridge Cooper has

### 00:33:03 · Speaker 5

So question again yeah

### 00:33:06 · Speaker 4

uh yeah sorry sir just a small one it's a little different. uh so uh the way you said right uh for a for a simple experiment like tossing a coin. um we usually immediately associate a random variable with uh possible outcomes like zero and one we assign to head and tails right. so um

### 00:33:25 · Speaker 5

So

### 00:33:27 · Speaker 4

Why like so I'm assuming the reason we choose zero and one is that something to do with the probability measure and like like why did we choose zero and one is my question. Why can't we have one? That's arbitrary. That's arbitrary. You can choose anything.

### 00:33:38 · Speaker 5

That's arbitrary. That's arbitrary. You can choose anything. You can choose anything.

### 00:33:42 · Speaker 4

Okay okay okay. So that is not affected by our probability measure and our us wanting to keep it between zero and

### 00:33:50 · Speaker 5

it has it has nothing to do no no no oh that has nothing to do with the measure. It's the the range of the random variable is arbitrary. You can choose it to be anything. In fact it becomes a function of your sensor and all that no. Your quantizer your sensor. When you take a picture what values do you see in the picture becomes a function of what is the what is the bit representation of your machine what is the machine precision what is the quantization that you are doing and so on isn't it?

### 00:34:19 · Speaker 4

Okay, so maybe I'm merging two concepts. Okay, thank you, sir.

### 00:34:22 · Speaker 5

So it has nothing to do with me

### 00:34:24 · Speaker 4

Okay

### 00:34:25 · Speaker 5

Okay. Okay, let's move on. Now, um the question is,

### 00:34:34 · Speaker 5

once you have okay we understood what happens to the elements of omega under the random variable. okay?

### 00:34:41 · Speaker 5

See now you understand why it is such a misnomer right? I mean you keep calling it random variable but you should imagine a function that's there. Right? Yeah it's it's it's the biggest misnomer that I've ever seen. It's it's it's not a random variable it's a function. Okay. Now uh yeah so

### 00:35:00 · Speaker 5

we saw what happens to the elements of sample space under random variable they get converted into real numbers right? next question that we should ask is what happens to probability measure? there is this probability measure right? once you operate a random variable right a function on the sample space what happens to probability measure is the question. you can always imagine this right?

### 00:35:24 · Speaker 1

So now

### 00:35:27 · Speaker 1

Once

### 00:35:34 · Speaker 1

an omega that belongs to omega

### 00:35:35 · Speaker 5

I mean W or W belongs to omega, right? And if you take that W and that is mapped to some real number, let's say.

### 00:35:47 · Speaker 5

Okay. Now what is x of omega? x of omega, right? is

### 00:35:53 · Speaker 5

a real number. I'm assuming that you have a one dimensional random variable in a while, okay? We'll define that notion for n dimensional random variables after after a while. Let's say that you have a one dimensional random variable. If you take an element w belonging to omega, belonging to omega, you will get a real number. Okay? That's what

### 00:36:16 · Speaker 0

this random variable does. Now

### 00:36:28 · Speaker 0

suppose

### 00:36:32 · Speaker 0

Suppose

### 00:36:33 · Speaker 0

what do we call that?

### 00:36:36 · Speaker 5

and

### 00:36:39 · Speaker 5

often run out of alphabets

### 00:36:44 · Speaker 5

suppose small r is a subset of real numbers.

### 00:36:51 · Speaker 5

Okay? Examples can be

### 00:36:55 · Speaker 5

minus two and three. Right and like minus infinity to two and so on right all these are subsets of real numbers. Now

### 00:37:06 · Speaker 5

x inverse of r

### 00:37:10 · Speaker 5

What can you say about this?

### 00:37:13 · Speaker 5

Let me repeat the question. We have a random variable which is a function that would take elements of sample space and maps it maps it to real numbers. Now what I do is I take a subset of real numbers.

### 00:37:28 · Speaker 5

You understand? I take a subset of real numbers.

### 00:37:31 · Speaker 1

okay? and look at the inverse image so this is the

### 00:37:41 · Speaker 1

inverse image

### 00:37:43 · Speaker 1

of R under the function X.

### 00:37:54 · Speaker 1

is the inverse image of a subset of R under the function X.

### 00:37:59 · Speaker 1

What do you get from doing?

### 00:38:01 · Speaker 1

interest

### 00:38:04 · Speaker 7

subset of omega

### 00:38:07 · Speaker 5

Exactly

### 00:38:07 · Speaker 7

Exactly

### 00:38:09 · Speaker 5

Yeah, you get a subset of omega from here. Can all of you see this?

### 00:38:14 · Speaker 1

will be some set, okay? which belongs to F. which is a subset of omega.

### 00:38:27 · Speaker 1

Can all of you see this? This is very important, please let me know if you see this.

### 00:38:36 · Speaker 5

questions on this I'm saying. Suppose you take a subset from the real numbers, real real numbers, a subset of real numbers and look at its inverse image under this function. Then you will get a subset of

### 00:38:51 · Speaker 1

Omega

### 00:38:53 · Speaker 1

Isn't it clear?

### 00:39:00 · Speaker 1

see when I ask you a question if it's clear to respond otherwise

### 00:39:03 · Speaker 5

guys

### 00:39:05 · Speaker 2

Here A is X inverse R. Is that the representation? Come again. Are we using A to represent X inverse of the range subset? Correct.

### 00:39:09 · Speaker 5

come again

### 00:39:14 · Speaker 5

Correct. Correct. Correct. Correct. A is the X. But what is that A? I mean what's more important is that that A is an element of F.

### 00:39:15 · Speaker 2

Okay

### 00:39:22 · Speaker 6

where f is the subset of

### 00:39:26 · Speaker 5

Omega

### 00:39:28 · Speaker 6

Right?

### 00:39:29 · Speaker 2

Yes sir

### 00:39:30 · Speaker 5

um

### 00:39:31 · Speaker 5

okay. This implies, this implies that we can talk of probability measures on

### 00:39:42 · Speaker 5

The inverse of

### 00:39:44 · Speaker 5

any subset of the real numbers, okay, this is well defined, no?

### 00:39:54 · Speaker 5

It is because this is equal to the probability measure defined on A which is a subset of F. So this is well defined.

### 00:40:04 · Speaker 5

Do you see this?

### 00:40:08 · Speaker 5

So we can define probabilities on the inverse images of the subsets of real numbers taken under random variable.

### 00:40:18 · Speaker 5

Let me write

### 00:40:19 · Speaker 0

like that

### 00:40:22 · Speaker 0

Probability

### 00:40:27 · Speaker 0

of E

### 00:40:31 · Speaker 0

inverse image

### 00:40:36 · Speaker 0

of

### 00:40:37 · Speaker 0

a subset of R

### 00:40:44 · Speaker 0

Under

### 00:40:47 · Speaker 0

The function is

### 00:40:51 · Speaker 0

is

### 00:40:52 · Speaker 5

Well defined

### 00:40:56 · Speaker 5

See note that probability measure was a measure that was defined on the subsets of omega. Sample spaces. Now random variable maps the elements of that to real numbers. Now we come backwards. We take a subset of real numbers, okay? And we look at the inverse image of that subset of real numbers. That subset of real numbers under this function called a random variable that would give you an element from the sample space or a subset from the

### 00:41:26 · Speaker 5

sample space. And on that we have already defined a probability measure therefore the probability of the inverse image of a subset of a real numbers under the function called random variable is well defined.

### 00:41:40 · Speaker 5

Did all of you get this? I'll take questions in a while but yeah.

### 00:41:46 · Speaker 5

Okay, one by one, Harish.

### 00:41:49 · Speaker 10

Hello sir. So is it correct to say that uh this elements of A are the samples which are just sampled from this whole sample space?

### 00:41:58 · Speaker 10

or the ones which were just observed.

### 00:41:58 · Speaker 5

elements of which we just observed. No no see A is a subset. A is a subset. A is a subset. See you remember this no there was an omega F and P what was this F? F was set of subsets of omega right?

### 00:42:12 · Speaker 5

And on on the elements of F is where we defined probability minus. I should write that also here. Is that so P is a function that is defined on A, okay? That would take an element A, okay, which is a subset of F and maps it to the number between zero and one.

### 00:42:36 · Speaker 5

This is the measure that we defined, no?

### 00:42:39 · Speaker 0

Okay, yeah.

### 00:42:40 · Speaker 1

तो एफ इस स्ट्रेट ऑफ

### 00:42:45 · Speaker 1

Subset of Omega

### 00:42:50 · Speaker 1

Okay

### 00:42:52 · Speaker 1

Right?

### 00:42:52 · Speaker 5

So we define the probability measure on the elements of F which are the subsets of omega. Okay? Now we are saying that the inverse image of the of any subset of R under the random variable will take us back to A and on A probability measures are defined therefore we can talk of the probability of inverse image of some subset of real number under the inverse of random variable that is well defined.

### 00:43:20 · Speaker 6

but

### 00:43:21 · Speaker 5

Right? Thank you, sir. Okay.

### 00:43:21 · Speaker 6

Thank you, Sir

### 00:43:23 · Speaker 5

Sarvesh

### 00:43:25 · Speaker 6

So so uh since F is a set of subsets of omega. So A should be a member of F right not the subset of F. Because anyways all the subsets are there in F.

### 00:43:30 · Speaker 5

So

### 00:43:38 · Speaker 5

Thank you for

### 00:43:39 · Speaker 0

that

### 00:43:42 · Speaker 0

some mistakes

### 00:43:48 · Speaker 0

my mistake. That was a that was a good point. Thank you for telling that.

### 00:43:58 · Speaker 5

Yeah, I actually went to that but I I wrote subset, yeah. So that my my mistake, sorry. Thanks. Avirup. Did did all of you get the mistake that I had done? I mean that's A is not a subset of F. A is an element of F. Yeah, because Okay, yeah. Avirup.

### 00:44:16 · Speaker 3

Yeah, so when you say the inverse image, so are you referring to some notion called inverse function? Of course, right?

### 00:44:24 · Speaker 5

Of course, right? Absolutely. Absolutely.

### 00:44:27 · Speaker 3

absolutely

### 00:44:27 · Speaker 3

Okay, now

### 00:44:28 · Speaker 5

because x is a function, right? x is a function. when the function always have an inverse, right? that would take an element from the range of the function and maps it back to the domain.

### 00:44:31 · Speaker 3

ஓகே

### 00:44:40 · Speaker 3

Okay, now in that case inverse function is also a function. A function by definition should always have many to one or one to one mappings. But in this case we are having multiple elements from the domain and we are mapping them to a set which is a

### 00:44:56 · Speaker 5

No

### 00:44:57 · Speaker 5

No no no see when you take when you define the random variable right? You can make it a bijective function so that the inverse exists.

### 00:45:05 · Speaker 3

Okay

### 00:45:06 · Speaker 5

Yeah, so you take every element from the sample space and map it to a unique real number.

### 00:45:11 · Speaker 3

Okay

### 00:45:12 · Speaker 5

That's all. So then it becomes invertible, right? It's a bijective function that can be inverted.

### 00:45:18 · Speaker 3

is it always possible to come up with a random variable which will

### 00:45:20 · Speaker 5

Of course, of course, why not? Because random variable is something that we are defining, no? You always make it bijective by definition.

### 00:45:28 · Speaker 1

Okay

### 00:45:29 · Speaker 5

Right? So that's why the inverse exists.

### 00:45:32 · Speaker 1

of

### 00:45:32 · Speaker 5

Hello

### 00:45:35 · Speaker 5

So basically what I'm saying is this function random variable always maps a unique element from the sample space to a unique element in real numbers that's all.

### 00:45:45 · Speaker 3

ओके ओके

### 00:45:46 · Speaker 5

See, in fact, even if it's not a bijective, right? Only surjection is enough for inversion, but you can make it bijective. Nobody stops you. Yeah?

### 00:45:56 · Speaker 9

Okay

### 00:45:56 · Speaker 5

Because you know functions like f of x squared, sorry f of x equal to x squared right even those have inverses so but now for I mean for ease of understanding let us assume that our random variables are all bijective functions okay.

### 00:46:11 · Speaker 5

Yes, Sanchit

### 00:46:14 · Speaker 6

सर, एस पर माय अंडरस्टैंडिंग, वी हैव रैंडम वेरिएबल्स मैप द इंडिविजुअल आउटकम्स इन द सैंपल स्पेस टू अ रियल नंबर, राइट?

### 00:46:27 · Speaker 5

Correct, correct.

### 00:46:28 · Speaker 6

Now, in the example we have taken, we are saying that we have taken a range minus two comma three or minus infinity comma two and that we are mapping to, you know, a subset.

### 00:46:37 · Speaker 5

That

### 00:46:42 · Speaker 9

Oh

### 00:46:43 · Speaker 6

so I agree that this subset A, this can this can be individual elements, but I'm not able to digest that this subset can have multiple elements of the sample space.

### 00:46:57 · Speaker 5

It can, no, because uh it depends on the way your function is defined, isn't it?

### 00:47:05 · Speaker 5

See, it's like this, I'll tell you.

### 00:47:05 · Speaker 6

Eat

### 00:47:08 · Speaker 5

suppose there is a function right let's say f of x is equal to

### 00:47:15 · Speaker 5

of x is equal to say x plus three, huh? Then what is the mapping? Zero to three and then you have one to four, two to five and so on, isn't it?

### 00:47:29 · Speaker 5

Okay? Now suppose I take a set which is let's say

### 00:47:33 · Speaker 1

Four to Eight

### 00:47:36 · Speaker 1

Can't I define this?

### 00:47:43 · Speaker 6

Okay, so this will give us a range of X.

### 00:47:46 · Speaker 1

Isn't it? Exactly.

### 00:47:47 · Speaker 5

you know, it's a huge subset of the domain.

### 00:47:47 · Speaker 6

is

### 00:47:50 · Speaker 6

Okay

### 00:47:51 · Speaker 5

Sir

### 00:47:52 · Speaker 6

ओके सर, मेक्स सेंस।

### 00:47:53 · Speaker 5

Yeah? Yeah? That is why the inverse image of a subset of R will give you an element from F, not an element from omega.

### 00:48:03 · Speaker 6

No, so that that that's what the confusion like that's what I said the

### 00:48:03 · Speaker 5

So that

### 00:48:06 · Speaker 5

But do you understand now what I'm talking about? Ha, gives an element from F because we are talking about subsets in the range space of the random variable that gets mapped to subsets in omega, that's all. Yeah?

### 00:48:09 · Speaker 6

gives an element

### 00:48:20 · Speaker 6

Okay, if if our domain is only the subset, then anyways, it will give give us

### 00:48:25 · Speaker 5

No no no what do you mean by domain is subset? I didn't domain is a set.

### 00:48:28 · Speaker 6

in this

### 00:48:31 · Speaker 5

domain is a set but what you are saying is if I consider subsets in R and take the inverse image I get subsets in omega.

### 00:48:39 · Speaker 6

Okay

### 00:48:41 · Speaker 5

But if I take a singleton here, I mean if this set has one element, I perhaps I get back one element there, right? And note that a set here, right, a subset of R here might map back to null set also. Correct. That's also possible. Yeah, but that's also a subset of. See, F also contains null, no?

### 00:48:54 · Speaker 1

Correct, correct. It's also possible. Yeah, but

### 00:49:01 · Speaker 1

Hmm

### 00:49:02 · Speaker 1

all the possible subsets of

### 00:49:02 · Speaker 5

all the possible subsets of omega. subsets of omega and null is also a member of F. Therefore the inverse image that's why in fact probability measure is defined on null set also. The probability of a null set is zero.

### 00:49:16 · Speaker 7

Correct

### 00:49:17 · Speaker 5

Yeah. So that's why it's well defined. You can take a subset in the range. So basically what I'm saying is that you can take a subset in the range space of random variable and the inverse image of that will map back to an element in F. That's all, no?

### 00:49:31 · Speaker 6

Okay, okay. And that element it can be a singleton or... Doesn't matter, it can be null. Yeah, it can be null. It can be anything.

### 00:49:36 · Speaker 5

doesn't matter. It can be null. It can be null. It can be anything. That is why I'm saying it's simply a member of F. That's all.

### 00:49:42 · Speaker 6

Okay

### 00:49:44 · Speaker 10

So why does it have to be an element in F but not uh say a subset of sample space?

### 00:49:44 · Speaker 5

does it

### 00:49:51 · Speaker 5

same thing no. subset of space is what we have denoted as F. all possible.

### 00:49:56 · Speaker 10

But it has to be an element in F, right?

### 00:50:00 · Speaker 5

Of course all subsequences

### 00:50:00 · Speaker 10

for instance if I, F is a set of subsets.

### 00:50:03 · Speaker 6

Sets

### 00:50:04 · Speaker 5

increase

### 00:50:04 · Speaker 10

If I increase the range, so you have put minus two to three and now I change it to say minus two to five. So now does it have to belong to only one element in F?

### 00:50:10 · Speaker 5

Sunny

### 00:50:14 · Speaker 5

it will it will get to a different it will map back to a different element in F no?

### 00:50:17 · Speaker 10

but an element in F, not a subset of subspace. Okay, subset of

### 00:50:19 · Speaker 5

Of course

### 00:50:22 · Speaker 5

ओके सब्सेट ऑफ सब्सेट ऑफ सब्सेट्स ऑफ सैंपल स्पेसेस इस व्हाट वी हैव कॉल्ड एस एफ। एफ इस नथिंग बट सेट ऑफ सब्सेट्स ऑफ सैंपल स्पेसेस।

### 00:50:33 · Speaker 5

What is F

### 00:50:34 · Speaker 10

Okay, so it cannot map to multiple elements in F is my question.

### 00:50:39 · Speaker 5

it cannot map of course right.

### 00:50:42 · Speaker 5

Of course, right? If you take a unique uh set in the unique subset in the range space of any function, the inverse image will map to a unique subset in the domain of the function, right? If the function is bijective.

### 00:50:58 · Speaker 10

Yes

### 00:50:58 · Speaker 5

Yeah. Simple, I mean see this is like your high school function, I don't know when did you study functions? Was it in high school? I studied it in class eleven.

### 00:51:10 · Speaker 5

What about you people? I don't know. Yeah. Are we different generations? Perhaps, no.

### 00:51:16 · Speaker 5

you mean most of you may be like like

### 00:51:20 · Speaker 5

between twenty and thirty I suppose, right? Most of you. Yeah, I have crossed thirty, so maybe I'm off at every every decade is a different generation, you see. So every decade they change the syllabus and all that. So I studied functions in, when did I study functions? It was in class eleven. When do they teach, teach them these days? High school?

### 00:51:43 · Speaker 5

Did anybody study functions in high school?

### 00:51:48 · Speaker 4

Yes sir, 11th.

### 00:51:48 · Speaker 0

Yes sir

### 00:51:50 · Speaker 5

Yeah, eleventh, I, yeah, eleventh is not high school, no? Yeah. It depends. I mean, in what, what curriculum are you a part of? I was, I was in the state board, right, where this eleventh was called college for some reason. It was called pre-university college. Anyway, okay, so I'm saying it's just fundamental stuff, right? You have, you have two sets we are talking about, university images. The one thing that we introduce new perhaps is that this is the idea of measure, okay? Okay, so clear so far.

### 00:52:19 · Speaker 0

ओके, नाउ

### 00:52:23 · Speaker 0

Consider

### 00:52:32 · Speaker 0

considered

### 00:52:35 · Speaker 0

subsets of R

### 00:52:40 · Speaker 0

of the

### 00:52:42 · Speaker 0

following

### 00:52:43 · Speaker 1

form

### 00:52:48 · Speaker 1

So let's say R one is a subset of R that is equal to minus infinity to

### 00:52:58 · Speaker 5

Power One

### 00:53:00 · Speaker 5

again overloading locations here. Let's not do this. Let's call this as S one. And this we will call as

### 00:53:15 · Speaker 1

we can call it R1 no problem. And S2

### 00:53:21 · Speaker 1

S

### 00:53:25 · Speaker 0

at least speaking in this now in close up of this.

### 00:53:35 · Speaker 5

You understand this notation, right? This set includes minus infinity does not include R one. It's upper bounded by R one. Here this set includes minus infinity but

### 00:53:45 · Speaker 6

सर, हाउ कैन वी इंक्लूड माइनस इंफिनिटी?

### 00:53:47 · Speaker 5

Why not? It's an element in R, no?

### 00:53:50 · Speaker 6

it is but it is not defined right what like

### 00:53:52 · Speaker 5

No, no, very much defined. Why not defined? It's an element in R.

### 00:53:57 · Speaker 5

you can definitely include minus infinity, no problem with that, okay? So let us consider these sorts of subsets of R. Now,

### 00:54:06 · Speaker 5

uh yeah. Now x inverse of

### 00:54:12 · Speaker 5

S one

### 00:54:16 · Speaker 5

is what is some element in R, no? Let's let's call it as A one which belongs to F, okay? Right. Now, the probability measure that is computed on the inverse of sets

### 00:54:33 · Speaker 5

Sub sets

### 00:54:36 · Speaker 1

of this particular type

### 00:54:42 · Speaker 1

one two

### 00:54:44 · Speaker 5

uh no. This is for this, this is for this, we need one more bracket. This, okay? This is well defined, right? You understand? What is this? This is the probability measure that is computed on that is assigned to the element of F which is gotten by the inverse image of the set minus infinity to X under the random variable X.

### 00:55:10 · Speaker 5

Okay, maybe not use x here again, it'll make life difficult. Let's call this as A. Okay.

### 00:55:19 · Speaker 5

Is this clear to all of you? This is a well defined measure, no? The probability assigned to

### 00:55:26 · Speaker 5

an element of oh by the way have I already said this this is also called the event space okay. F has a name it's called the event space. So this is the probability measure assigned to the element of the event space that gets mapped to

### 00:55:49 · Speaker 5

that gets mapped that that that gets mapped to a set minus infinity to a under x. Or rather it is a probability of the event a probability of the member of the event space obtained by taking the inverse image of this subset minus infinity to a under the random variable x.

### 00:56:10 · Speaker 5

Do you understand this statement? If you understand this statement, then you have understood everything that I have said so far.

### 00:56:15 · Speaker 5

Shall I repeat the statement? Okay, let me write that down, maybe it's better to write it. This is the probability of

### 00:56:24 · Speaker 5

Tea

### 00:56:26 · Speaker 0

element

### 00:56:29 · Speaker 0

in F in the event space

### 00:56:36 · Speaker 0

that is obtained

### 00:56:45 · Speaker 0

Obtained

### 00:56:47 · Speaker 0

by taking

### 00:56:51 · Speaker 0

the inverse image

### 00:56:58 · Speaker 0

of T-shirt

### 00:57:02 · Speaker 0

minus infinity into a

### 00:57:09 · Speaker 0

Under

### 00:57:11 · Speaker 0

the random variable x. Is this clear? Any questions on this?

### 00:57:24 · Speaker 0

all of you, please ensure that every one of you understands this. Nirmats

### 00:57:30 · Speaker 6

Uh, sir, can you explain what is under the, uh,

### 00:57:35 · Speaker 6

random variable index. Yeah.

### 00:57:35 · Speaker 5

random variable

### 00:57:37 · Speaker 5

X is a function, no? See, when we talk of inverse images, we have to test, we have to, we have to specify what function are we looking inverse images under.

### 00:57:38 · Speaker 6

complete

### 00:57:47 · Speaker 1

Okay

### 00:57:49 · Speaker 5

See, when you take an when you take a subset and you talk of inverse images, what is the function under which you are taking the inverse image? It is a random variable which is a function, correct?

### 00:57:58 · Speaker 6

ಓಕೆ

### 00:58:00 · Speaker 5

Right?

### 00:58:01 · Speaker 6

Base

### 00:58:02 · Speaker 5

S

### 00:58:02 · Speaker 6

Is it uh does it mean that let's say if we take S of some sample space we'll reach out to a particular range. If you take inverse of that what are the sample space for the event space that we end up in. Probability of that is what we are defining here.

### 00:58:19 · Speaker 5

Exactly. Exactly. But we are looking at particular subset of real numbers, no? This particular subset. The kind of subset that we are looking at is like close minus infinity to open A.

### 00:58:32 · Speaker 1

ஓகே

### 00:58:33 · Speaker 5

Right? Karthik Kumar

### 00:58:36 · Speaker 7

Yes sir. So, does A have any relation with the

### 00:58:45 · Speaker 5

your voice is breaking up

### 00:58:45 · Speaker 7

Breaking Era 0.4 S1

### 00:58:47 · Speaker 5

Karthik your voice is breaking.

### 00:58:49 · Speaker 7

Sorry, am I audible, sir? Yes, no. Am I audible? Is it only for me?

### 00:58:50 · Speaker 5

Yes no

### 00:58:52 · Speaker 5

Is it only for me? His voice is breaking.

### 00:58:58 · Speaker 10

No for us

### 00:58:59 · Speaker 7

it is

### 00:59:01 · Speaker 5

Karthik, is it still breaking?

### 00:59:02 · Speaker 7

is it still breaking sir?

### 00:59:04 · Speaker 5

Yeah, not now. Try, try now.

### 00:59:06 · Speaker 8

Yeah, uh I just wanted to ask is A anyway related with R one and uh R one which we defined S one with? Minus infinity to R one.

### 00:59:16 · Speaker 5

with well it is in the sense that like this particular R one is the is I mean this particular set is the one that maps back to A one that's all. Other than that there is no relation per per set.

### 00:59:31 · Speaker 8

Okay, so yeah, I mean like

### 00:59:33 · Speaker 5

If you take this particular subsets and take the inverse image of this it will go back to A one that's all.

### 00:59:39 · Speaker 8

ओके. या, श्योर. थैंक यू.

### 00:59:41 · Speaker 5

Okay. Okay, great. So this we will let's give a symbol for this. Let us

### 00:59:48 · Speaker 5

key this call this as P X evaluated at A

### 00:59:54 · Speaker 5

is a symbol, okay? What is it saying is, I mean, I I I just represent this this complicated

### 01:00:00 · Speaker 7

looking thing using a simple symbol, right? I mean this symbol actually means that I am looking at the inverse images, the probability of the inverse image of this particular type of subset minus infinity to a under the random variable. This is the symbol. Is this okay? I'm just using this symbol for this this complicated thing. Is that okay?

### 01:00:25 · Speaker 5

Yes sir

### 01:00:26 · Speaker 7

Okay. It turns out that this has a name. This particular thing has a name which all of you know. Do you know what the name of this is?

### 01:00:37 · Speaker 0

EDF

### 01:00:38 · Speaker 7

Exactly. No, no, not PDF. This is the

### 01:00:40 · Speaker 0

humalative distribution function.

### 01:00:40 · Speaker 8

cumulative distribution function. Yeah, this is the distribution function.

### 01:00:46 · Speaker 8

This is the distribution function of a random variable.

### 01:00:53 · Speaker 7

Some people also call it the cumulative distribution function. I mean I don't know why it is called cumulative. You don't have to call it cumulative, okay?

### 01:01:02 · Speaker 7

this is called distribution function of a random variable. Is this clear? So what

### 01:01:06 · Speaker 1

since it accumulates the distribution from minus infinity till

### 01:01:10 · Speaker 7

No, no, no, no, no, no, no, no, no, please, please. I said there is, there is no accumulation that's happening, no. See, the reason perhaps why people call it cumulative is because you define a density function and then you like you can represent the the this this function as a running integral of that other function and that's why it's called cumulative. But I I'm not a fan of this term cumulative. I mean, standard textbooks call it a distribution function and

### 01:01:40 · Speaker 7

this is a distribution function. Okay? Now what is a distribution function? It's it's the probability of the element in event space that is obtained by taking the inverse image of the set minus infinity to A under the random variable X. So if you evaluate this distribution function at a value X or A, it will remember that you are actually looking at the probability of an event. Probability of an element from the event space. What is that element? That element is the one that you have gotten by taking the inverse image of of this set minus infinity to a under the random variable x

### 01:02:15 · Speaker 8

Is this clear?

### 01:02:22 · Speaker 8

This is the

### 01:02:22 · Speaker 7

single most important definition that we will be looking at because the entire machine learning is estimating this this particular function given elements from range space of random variables that is all the the be generative models discriminative models classifiers regressors anything the entire machine learning is about estimating these functions the probability density functions sorry distribution functions

### 01:02:48 · Speaker 7

Okay, so in fact instead of calling it cumulative distribution functions, no, let us call them the probability distribution functions, no?

### 01:02:54 · Speaker 8

that is

### 01:02:55 · Speaker 8

Hello

### 01:02:58 · Speaker 8

Much better, no

### 01:03:03 · Speaker 0

probability uh B D distribution functions. probability distribution function of A.

### 01:03:16 · Speaker 0

Is this clear?

### 01:03:23 · Speaker 0

Please remember that if you evaluate

### 01:03:26 · Speaker 7

distribution function at a particular point

### 01:03:31 · Speaker 7

okay? If you evaluate the distribution function at a particular point, what are you actually doing?

### 01:03:39 · Speaker 7

When you evaluate the distribution function at a particular point, you're actually getting a probability. Probability by definition is defined on the elements of F.

### 01:03:49 · Speaker 7

Now evaluating distribution function at a particular point should give you, right, the probability of a particular element in F. What is that element in F whose probability this function is giving you? It is that element in F, okay, or rather that subset of the sample space which is

### 01:04:11 · Speaker 7

getting mapped to minus infinity comma a under the random variable x

### 01:04:19 · Speaker 7

Is this clear?

### 01:04:22 · Speaker 7

Please remember this. Because as I said, this is the single most important definition that we need for this course. So, yeah. Questions on this Sanket?

### 01:04:34 · Speaker 3

सर, दिस प्रोबेबिलिटी डिस्ट्रीब्यूशन फंक्शन इज यूजुअली द प्रोबेबिलिटी एट अ सिंगल पॉइंट, राइट? एंड...

### 01:04:41 · Speaker 7

Definitely no no no definitely not I mean that is that is present three and a half hours to define this. It is not that.

### 01:04:51 · Speaker 7

See, point number one, I am I am not talking about probability density functions here. I am talking about the probability distribution functions.

### 01:04:52 · Speaker 3

Point Number

### 01:04:59 · Speaker 3

Okay, Okay.

### 01:05:00 · Speaker 7

Okay? And even probability density functions are not probabilities. Please remember that probability is a measure that is defined on elements of F, period. You cannot talk of probability of X being equal to something. It just does not make sense. You understand?

### 01:05:19 · Speaker 7

बिकॉज़ बाय डेफिनेशन, बाय डेफिनेशन प्रोबाबिलिटीज़ आर डिफाइंड ऑन एलिमेंट्स ऑफ एफ, दैट्स ऑल।

### 01:05:27 · Speaker 7

it's like can you talk of length of length of

### 01:05:34 · Speaker 6

Okay, what do we say?

### 01:05:39 · Speaker 7

Yeah

### 01:05:41 · Speaker 7

If I say length of water, length of water, right? Or length of length of speech or something, it's just not defined, right? Length is defined only on elements of subsets of R, isn't it? Similarly, probability is a measure that is defined only, only on subsets of omega. So whenever you talk of probability, you should always make sure that you are talking about the probability of an element of F.

### 01:06:10 · Speaker 7

That is why this distribution function while it is denoted as P X A, okay, this actually means this entire thing.

### 01:06:21 · Speaker 7

Whenever I write P X A in this course you should always remember that I am talking about this.

### 01:06:27 · Speaker 7

Okay, you should remember that there exists a function called random variable. Okay, and this random variable has an inverse image. The inverse image of we are considering the inverse image of this particular set minus infinity to A. Now that gives you an element in the event space. That has a probability associated with it and that is what this function is giving me. Always, okay?

### 01:06:53 · Speaker 7

is this clear because I want to make this you know damn clear to all of you because you know people very wrongly say that probability of a random variable it's there is nothing called probability of a random variable.

### 01:07:07 · Speaker 7

Okay, it does not make sense. You you mean it's like, you know, saying round circle or something. There is no probability of random variable. There is probability of elements of F. So if you evaluate the distribution function of a random variable at a particular point, what you are actually doing is this entire thing.

### 01:07:24 · Speaker 7

Okay, please be clear about it. Rajat,

### 01:07:30 · Speaker 4

Hello sir. Sir my question is when we are taking the inverse of a subset of R then it might not be having any element in F right? For example

### 01:07:37 · Speaker 7

then

### 01:07:40 · Speaker 7

No, it will always be, it will always be. It will always be. It can

### 01:07:45 · Speaker 4

suppose to tossing

### 01:07:47 · Speaker 7

Ha, Go on

### 01:07:49 · Speaker 4

Yes, example tossing a coin will have outcome of head and tail. And suppose head is translated to zero under random variable and tail to one. Then if I take if I try to take the inverse of for example three which

### 01:07:53 · Speaker 7

and

### 01:07:59 · Speaker 7

then if

### 01:08:03 · Speaker 7

which then it then it maps back to null that's all. and null is also an element of it.

### 01:08:11 · Speaker 4

okay, okay, got it. In that case, probability will be

### 01:08:14 · Speaker 7

Zero. Absolutely.

### 01:08:14 · Speaker 4

Zero

### 01:08:15 · Speaker 4

Sir, absolutely.

### 01:08:17 · Speaker 4

Got it, thanks.

### 01:08:19 · Speaker 7

actually mentioned this, maybe you missed that. No problem. Avirup,

### 01:08:24 · Speaker 2

Yeah, so I understood this definition what you just mentioned, but I am a little bit intrigued how we actually find the value of P X A because that would involve finding the even event

### 01:08:35 · Speaker 7

Hello

### 01:08:37 · Speaker 7

hold on, hold on. I will not come to that. See, please again I am reiterating, don't jump. We will not leave anything in this course, okay? We will address all those questions. Okay? But see when I when I ask you for questions, right? Do ask, please ask me questions on things that we have discussed so far. Because otherwise, right? If you jump ahead, then you know, it will sort of break the flow. Please don't take it in a negative sense, huh? Just to ensure that, you know, we are going systematically.

### 01:08:38 · Speaker 2

not

### 01:08:39 · Speaker 2

Okay

### 01:09:07 · Speaker 7

We will be that's a good question by the way. How do we estimate P X is the question that we ask in machine learning. All machine learning is about estimating the distribution and function, okay? So don't worry, we'll come to that in the next next part of this class. Indrajit.

### 01:09:24 · Speaker 1

Yeah, when you say you are taking probability of inverse random variable minus infinity to A, can you

### 01:09:30 · Speaker 7

इंद्रजीत जस्ट अ सेकंड प्लीज प्लीज प्लीज यूज करेक्ट टर्म्स देयर इज नो इनवर्स रैंडम वेरिएबल

### 01:09:32 · Speaker 1

Right

### 01:09:39 · Speaker 7

So can you can you say it correctly?

### 01:09:42 · Speaker 7

the probability of

### 01:09:47 · Speaker 7

So, just attempt, no, say it correctly.

### 01:09:51 · Speaker 1

सो इनवर्स प्रोबेबिलिटी ऑफ अ रियल नंबर

### 01:09:54 · Speaker 7

No no no not inverse probability. See inverse is defined for a function.

### 01:10:02 · Speaker 1

Yeah, okay.

### 01:10:04 · Speaker 7

inverse is defined for a function. Okay? inverse of the function called random variable

### 01:10:11 · Speaker 1

Okay

### 01:10:13 · Speaker 7

overset. That is how you should say it.

### 01:10:17 · Speaker 1

Yeah, so when you are taking that set as minus infinity to A, can it be any other set, say A one to A two?

### 01:10:20 · Speaker 7

ten

### 01:10:24 · Speaker 7

I'm glad that you asked that question. I wanted somebody to ask this. It's a very good question. So why are we considering this particular set? What is the what's so what's so nice about this particular set is the question that you are asking, correct?

### 01:10:37 · Speaker 1

Yeah

### 01:10:38 · Speaker 7

Yeah, I'll answer that next. That's the next thing that I'll do, but I'm glad that you asked that question. I'll answer that. I was expecting someone to answer that question, ask me that question, right? What is so sacrosanct about this particular set that we are assigning a function to it, right? I mean, rather like we are calling, we are giving it a particular name. What is so important about this? I'll answer that if you want, okay?

### 01:11:02 · Speaker 1

Okay

### 01:11:02 · Speaker 7

ஓகே, ராஜவேந்திரா

### 01:11:05 · Speaker 5

Yes sir, why does that interval not include a

### 01:11:08 · Speaker 7

See, it's related to the other question that Indrajit asked. Okay, why what is so I mean what why why is this particular set, right? That is the next question. Okay, we'll answer that question perhaps. Now it turns out, I'll just state that without the proof maybe, yeah, I okay, by the way there is one other convention.

### 01:11:32 · Speaker 0

I'll tell you that. Why

### 01:11:59 · Speaker 0

Right? This question has to be answered.

### 01:12:04 · Speaker 0

So the answer to this is, it turns out

### 01:12:11 · Speaker 0

any subset in R

### 01:12:14 · Speaker 0

can be represented

### 01:12:22 · Speaker 0

S

### 01:12:35 · Speaker 0

Okay

### 01:12:38 · Speaker 0

set operations

### 01:12:44 · Speaker 0

Four

### 01:12:47 · Speaker 0

starts of form

### 01:12:56 · Speaker 0

So this, okay, so here is the convention, okay?

### 01:13:02 · Speaker 7

So from now on, uh whenever I state something, okay, without proof or without giving you uh lot more details, I will mark them as tutorial items. Okay? Now, I ask one of you, uh like or maybe

### 01:13:20 · Speaker 7

all of you to take a note of it, okay? And just put it in the teams as tutorial items. And this has to be covered in the tutorial by T I C. I'll keep doing this from now on.

### 01:13:36 · Speaker 7

Okay? Anyway, so the thing is,

### 01:13:39 · Speaker 7

Any subset in R can be represented via set operations over these kinds of sets. That is the reason we are interested.

### 01:13:45 · Speaker 8

set in this kind of set

### 01:13:52 · Speaker 8

What does that mean? That means that suppose

### 01:13:58 · Speaker 8

rather

### 01:14:02 · Speaker 8

So if you take a set subset A B, okay? That is in R.

### 01:14:11 · Speaker 8

this A B

### 01:14:16 · Speaker 0

can be written as

### 01:14:49 · Speaker 0

Yeah, this is a such sad

### 01:14:53 · Speaker 0

is good

### 01:14:54 · Speaker 7

Hello

### 01:14:56 · Speaker 3

Sir, we need to have square braces for A, B. Set A, B.

### 01:14:56 · Speaker 7

Sir, we need to have

### 01:15:02 · Speaker 7

because that is those are included, no? Yeah. What I had written earlier was correct.

### 01:15:13 · Speaker 7

This is one example I think the TS will do a proof for this. So basically what I'm saying is if you can take any subset in R and that can be represented using the set operations on these kinds of things.

### 01:15:26 · Speaker 7

Okay and we know that uh that you know probabilities uh measures probability measures will add up so therefore if you want to take if you want to look at the probability of let's say that you are interested in the probability of

### 01:15:43 · Speaker 0

of

### 01:15:50 · Speaker 0

the inverse image okay of this particular

### 01:15:56 · Speaker 8

percent

### 01:16:01 · Speaker 8

particular asset

### 01:16:03 · Speaker 7

this can be right obtained in terms of the the problem the distribution function that is evaluated at B subtract that with the distribution function that is evaluated at A. So again the proof of that shall be done in the tutorials.

### 01:16:22 · Speaker 5

Sir, B is not included in that interval, right?

### 01:16:22 · Speaker 7

Okay

### 01:16:25 · Speaker 7

P is not included in the interval is that so?

### 01:16:30 · Speaker 5

Yeah, because it's not included in minus infinity.

### 01:16:30 · Speaker 7

Yeah, because it's not included in minus infinity. A is included, B is included. See, yeah, A is included, B is not included. I think this should be correct. Correct? This is what you're saying, B is not included in the interval.

### 01:16:40 · Speaker 6

Yes

### 01:16:42 · Speaker 6

Correct

### 01:16:42 · Speaker 6

Okay. Yeah.

### 01:16:44 · Speaker 7

So this is why we are interested in this particular set that if we want to look at the probability of the inverse image of any subset of R, okay? We can obtain that in terms of the probabilities of events that are associated with the inverse images of

### 01:17:06 · Speaker 7

this this kind of subsets. Okay, that is why we are interested in this particular type of subsets.

### 01:17:12 · Speaker 7

Okay? Does that answer your question? I think Interject asked this question, right? Why are you interested in this particular subset? It is because of this that we can obtain the probabilities of inverse images of any of subset of R is B subsets.

### 01:17:26 · Speaker 7

Okay. Now what is this has a very big implication this implies this implies that the probability

### 01:17:34 · Speaker 0

distribution function

### 01:17:43 · Speaker 0

function

### 01:17:44 · Speaker 0

completely

### 01:17:47 · Speaker 8

complete

### 01:17:49 · Speaker 8

C O M P L E T E L Y completely specifies

### 01:17:58 · Speaker 0

Okay

### 01:18:00 · Speaker 0

until probability measure.

### 01:18:14 · Speaker 0

Right? So what you are saying is

### 01:18:15 · Speaker 8

that if you know

### 01:18:17 · Speaker 7

know the distribution function then you know everything about

### 01:18:20 · Speaker 8

Hello

### 01:18:21 · Speaker 7

theater line probability triplet

### 01:18:26 · Speaker 7

Can I make that statement? So basically what happens now? That you start from this is what you have. This is the probability triplet, you have the sample space, the event space and the the probability measure.

### 01:18:41 · Speaker 4

the

### 01:18:41 · Speaker 7

is when I operate a function called random variable on top of this

### 01:18:49 · Speaker 7

Okay, what happens is this will induce another measure space that is called also called the push forward measure. This will map uh omega to R and it will map F two

### 01:19:04 · Speaker 7

subsets of F, okay, which are subsets of R, which are also called the Borel sigma algebra. So it's very important. It's just a name given to specific specific subsets of R. And the probability measure gets pushed forward to distribution function.

### 01:19:23 · Speaker 7

This is the story.

### 01:19:26 · Speaker 7

Okay. Now, the thing is, in practice, no access to this, you know, we don't have access to this.

### 01:19:34 · Speaker 8

Okay, but this is accessible.

### 01:19:43 · Speaker 8

the data that we get are actually the members of

### 01:19:47 · Speaker 7

of

### 01:19:48 · Speaker 7

This R

### 01:19:50 · Speaker 7

Okay. So now when we have like thousands of images, they are all members of this R. Okay. Now because we have this, we always operate with R, B and PX. We don't even look at B, R and PX. So now if we get PX, then we know everything about the underlying probability space.

### 01:20:10 · Speaker 7

Okay, this is by the way this is also called the

### 01:20:15 · Speaker 7

the probability space or probability triplet

### 01:20:23 · Speaker 8

and this is called the

### 01:20:25 · Speaker 8

Pushpa roller induced space.

### 01:20:29 · Speaker 7

It's actually a space that is induced by a function on the sample space, no, which is called a random variable.

### 01:20:33 · Speaker 8

table

### 01:20:35 · Speaker 8

push forward

### 01:20:36 · Speaker 7

Hello

### 01:20:37 · Speaker 8

or the induced space.

### 01:20:42 · Speaker 8

तो बी

### 01:20:43 · Speaker 7

simply work with this action symbol

### 01:20:44 · Speaker 7

and work with

### 01:20:46 · Speaker 7

Yes

### 01:20:50 · Speaker 7

See work with distribution functions, right? And the elements of the range elements from the range space of random variable, that's our data. Okay? That is our data.

### 01:21:00 · Speaker 7

But you should always remember that whenever we talk of a random variable and a distribution function, you should always remember that this random variable is a function that has an underlying underlying probability space, okay? And the probabilities that we are talking about are on the elements of that F event space.

### 01:21:17 · Speaker 7

Okay? This is the clarity that you should have. So, in other words, if we know what the distribution function is, then we know everything about the underlying probability measure. And that is why entire machine learning is cast as estimating the problem of estimating the probability distribution function given data. I will write down on this, right? Yeah, so I just wanted to tell you that

### 01:21:41 · Speaker 7

that that why is why are we working with random variables and what are random variables and what are distribution functions. Hope that you people are clear about this. Okay questions no. Sanchit.

### 01:21:55 · Speaker 3

Sir, why are we taking the concept of Borel sigma algebra here?

### 01:22:00 · Speaker 7

Because the when you have this random variable right that would take omega to R. If right get pushed forwarded to Borel sigma algebras.

### 01:22:06 · Speaker 3

hmm

### 01:22:11 · Speaker 3

So, like for Borel sigma algebra, what understanding I have is it will have all possible subsets of the form A, B.

### 01:22:20 · Speaker 7

Correct. Correct. Correct. True. That is why no F gets because you know those are the those are the elements those sets those subsets of R gets mapped back to elements in F no. That's why the push forward uh push forwarding that happens from F.

### 01:22:41 · Speaker 7

via a random variable is Borel sigma algebra.

### 01:22:46 · Speaker 7

I'm not I'm not telling you that because as I said no you can mostly ignore this B because we are basically what I'm saying is when omega gets mapped to R what happens to F F gets mapped to Borel sigma algebra that's all.

### 01:22:46 · Speaker 8

Okay

### 01:22:59 · Speaker 3

Then sir, by default, the probability measure should be a length measure, right?

### 01:23:04 · Speaker 7

I don't know. Not necessarily because probability measure is defined on the probability triplet, no? But, but, I mean, that's a good question that you ask. See, we can integrate distribution functions, right?

### 01:23:21 · Speaker 3

we can what?

### 01:23:23 · Speaker 7

integrate distribution functions, we can differentiate distribution functions, right? Correct, correct. Operations of integration and differentiation are defined on Lebesgue measures.

### 01:23:26 · Speaker 3

Correct, Correct.

### 01:23:34 · Speaker 7

That is one of the reason. Yeah, length measures, no? Operations of integrations and differentiations are defined on the length measures, Lebeck measures.

### 01:23:34 · Speaker 3

Ananda

### 01:23:37 · Speaker 3

Hmm hmm

### 01:23:43 · Speaker 8

Correct

### 01:23:44 · Speaker 7

Now, since that is one of the reason why we need a random variable. See, you cannot integrate in the the probability space because integration is in probability space is not defined at all.

### 01:23:57 · Speaker 7

Right? So once you get to the uh the the the uh the push forward or induced space, you can do integration. That's why you can differentiate the distribution function and you get another function called the density function. Right? You can integrate the distribution function, you can do all those things.

### 01:24:13 · Speaker 7

the default measure is not the length measure. The length measure is defined only on Borel sigma algebra. Okay? Under the random variable, right? Once you do the push forwarding, you get the the Lebesgue measure. Before that it's the probability measure only. Got it?

### 01:24:30 · Speaker 3

Sir, so once we have an induced probability space, we have a Borel sigma algebra and correspondingly the Lebeck or length measure.

### 01:24:40 · Speaker 7

Correct, but we are not interested in the length measure on the Borel sets gotten from the push forward induced space. We are interested in the probability measure that is obtained by the inverse images on the the subsets of R. Because we are interested in finding out the underlying probability measure, not the length measure of this Borel space. Okay?

### 01:24:59 · Speaker 3

Okay, okay.

### 01:25:01 · Speaker 7

Because the whole purpose is to model that picture and and map it to a gender or something, right?

### 01:25:08 · Speaker 7

We are not interested in the Lebesgue measure of this push forwarded space. We are interested in these kinds of induced measures, right, which are called the probability distribution functions. Yeah.

### 01:25:19 · Speaker 3

Okay

### 01:25:20 · Speaker 7

Okay, so rest of the people can ignore this discussion if you if it didn't make sense. Okay. So don't worry, I mean that was like slightly off topic. Okay, Adityanath.

### 01:25:33 · Speaker 5

So the induced space we have data so this probability P X that is calculated based on the data or it's available exclusively uh otherwise also.

### 01:25:44 · Speaker 7

No, it is not available. No, the whole problem of machine learning is to estimate this pH. We don't have this pH with us.

### 01:25:50 · Speaker 5

state

### 01:25:51 · Speaker 5

Okay

### 01:25:52 · Speaker 7

I will say that see what we have are the elements from the range space of random variable that's all that is our data

### 01:26:01 · Speaker 7

The whole problem will be to estimate T X

### 01:26:01 · Speaker 5

PX will be

### 01:26:05 · Speaker 5

Correct

### 01:26:08 · Speaker 7

entire machine learning is estimating P X. Okay?

### 01:26:12 · Speaker 5

Yeah, got it, sir.

### 01:26:13 · Speaker 7

I will define that. I will define that in a while. Yes, Raghavendra.

### 01:26:19 · Speaker 5

Yes, in general, do we also know X always or

### 01:26:22 · Speaker 7

No, we will not know X. We will only know, we will only have elements from the range space of X. We will not know X. See, when you have images, right, or do you have, you have lot of real numbers, right? Each each image is a set of real numbers, correct?

### 01:26:37 · Speaker 7

Yes. What is that? That's actually the elements from the range space of random variable. You don't know what the random variable is.

### 01:26:38 · Speaker 4

What

### 01:26:44 · Speaker 5

Correct

### 01:26:45 · Speaker 7

Right

### 01:26:47 · Speaker 7

I'm telling you again, random variable is not a variable, it's a function, so please remember that.

### 01:26:54 · Speaker 7

Okay. This is clear. Sanchit has one more question. Yeah, Sanchit.

### 01:26:59 · Speaker 3

So basically, we we have a probability triplet and in order to have an ease of operations, we are, you know, inducing the concept of random variables and not only

### 01:27:11 · Speaker 7

And not only not only that, not only that, right? Ease of operation is of course one because we can integrate and all that. There is one other reason, no? The way I motivated is you don't have access to Omega IFP.

### 01:27:26 · Speaker 7

See, in in in in real world, what do you have access to? You have access to real numbers, you know, how do you see real numbers as elements of omega, no? You can't.

### 01:27:36 · Speaker 7

There is something that is, There is something that is

### 01:27:36 · Speaker 3

something that is, there is something that is, we just have the, we just have the outcomes that are known to us.

### 01:27:41 · Speaker 7

We don't even have, yeah, we don't even have the access to outcome. We have access to some measurement of the outcome.

### 01:27:49 · Speaker 3

Correct

### 01:27:50 · Speaker 7

And how do you quantify that using maths? That is quantified using random variable, no?

### 01:27:54 · Speaker 3

Correct, Correct, Correct.

### 01:27:56 · Speaker 7

So basically there is a function that is sitting on top of the outcomes. Which is giving you real numbers. That is what we have access to.

### 01:28:05 · Speaker 3

Correct

### 01:28:05 · Speaker 7

And now since we have measure defined the probability measure on the subsets of outcomes, we need an equivalence in the induced space and that is your distribution function. That is your distribution function.

### 01:28:14 · Speaker 3

you know, distribution

### 01:28:18 · Speaker 3

Got it, sir.

### 01:28:20 · Speaker 7

Huh?

### 01:28:21 · Speaker 3

गॉट इट सर

### 01:28:22 · Speaker 7

Yeah, but always remember, this definition is very, very sacosigned. I mean, this is you should remember this. Whenever I talk, I will be talking of distribution functions all along the course now, okay? Whenever I talk of distribution function, you should remember this. I suggest all of you go back today after today's class, sit down, maybe rewatch the lecture, and try to get this idea solid into your mind, okay? Very, very important. Lot of people hand wave on this.

### 01:28:52 · Speaker 7

and wrongly represent distribution function as probability of random variable that does not make sense at all. So please get this get these ideas nicely into your mind. Okay. Indrajit.

### 01:29:11 · Speaker 1

Yeah, does it really matter whether we include A or B endpoints? Or exclude them?

### 01:29:17 · Speaker 7

here the

### 01:29:18 · Speaker 1

Yeah

### 01:29:20 · Speaker 7

It it depends, no? You can take any set here and as I said any set can be represented using these kinds of sets, that's all. You can take any set, you can take the inclusive sets, exclusive sets, doesn't matter. You can represent any set like this using these kinds of sets, operations on these kinds of sets, okay?

### 01:29:40 · Speaker 7

ओके, ग्रेट। ओके, ब्रिज गोपाल।

### 01:29:46 · Speaker 6

Uh, hi sir. Uh, so, uh, let's say, uh, using machine learning we have successfully approximated PX, which gives us basically the ability to tell how probable it is that we'll, uh, that we'll see a set, uh, a subset of event space A in real life, correct? Up to this point, am I understanding? So, how does this understanding translate into us knowing about the actual underlying P of

### 01:30:06 · Speaker 7

this point

### 01:30:08 · Speaker 7

So

### 01:30:16 · Speaker 6

the probability

### 01:30:18 · Speaker 7

That is your P no? That is P. What is P? P is the probability of a particular subset in F. If you know that you know that that's all.

### 01:30:29 · Speaker 7

See, maybe you should ask a different question, right? How will that be important or relevant in telling what is the gender of this particular person is, right? Obtained from that image.

### 01:30:42 · Speaker 6

Yeah.

### 01:30:43 · Speaker 7

That question I have not answered yet. I will answer that question. But if you estimate the probability distribution function then you know everything about the underlying probability measure.

### 01:30:55 · Speaker 6

Okay sir, just I'll say a statement, please help me understand where I'm going wrong in this. So once we once we approximate PX. So I'm I'm I'm thinking of PX as a as a function that takes an input and generates an output. So the output that is generated

### 01:31:00 · Speaker 7

So

### 01:31:05 · Speaker 7

Hmm

### 01:31:11 · Speaker 7

So

### 01:31:15 · Speaker 6

is P is a part of P

### 01:31:19 · Speaker 7

What do you mean by output? I didn't get that. See, the probability distribution function is a function, I agree, right? Yeah, whose like whose range is zero to one.

### 01:31:27 · Speaker 6

Yeah

### 01:31:32 · Speaker 6

Yeah

### 01:31:33 · Speaker 7

Now what is the question?

### 01:31:35 · Speaker 6

So, uh from the definition of P X, what we get is the likelihood of observing A.

### 01:31:41 · Speaker 7

like have I have I defined a term likelihood

### 01:31:44 · Speaker 6

Okay

### 01:31:45 · Speaker 7

Please don't use the term because all those are mathematically precisely well defined. Don't use the terms that are not defined.

### 01:31:52 · Speaker 6

Okay, so

### 01:31:52 · Speaker 7

If you evaluate the distribution function at a particular point, they'll give you the probability of the inverse image. That's all it is.

### 01:32:02 · Speaker 7

Now what is the question? Yeah.

### 01:32:02 · Speaker 6

what is

### 01:32:04 · Speaker 6

सो, द प्रोबेबिलिटी ऑफ इनवर्स इमेज और टू गो विद द नोटेशंस प्रोबेबिलिटी ऑफ आउटपुट, करेक्ट?

### 01:32:12 · Speaker 7

No, again, there is nothing called probability of A. This is again, this is a notation. When I evaluate the distribution function at A, what am I doing is I am looking at the probability of inverse image of this particular subset. That is all it is. There is nothing called probability of A, please.

### 01:32:31 · Speaker 7

That is the, you know, misrepresentation that I want to take out of your minds. When you evaluate the distribution function at a point, okay? You are not getting the probability of that point. That does not even make sense.

### 01:32:44 · Speaker 6

sorry sir I was not talking about small a I was talking about capital A the set

### 01:32:48 · Speaker 7

Oh sorry, my bad. Yeah, it is the probability of A, correct. A one, I have said it as A one, no? Yeah.

### 01:32:53 · Speaker 6

Yeah, yeah, okay, A1. So,

### 01:32:54 · Speaker 7

So

### 01:32:55 · Speaker 6

Now, the probability of A one is actually that underlying P, correct? That we were talking in that first triplet.

### 01:33:00 · Speaker 4

actually that

### 01:33:06 · Speaker 7

Yeah, of course, no, P is a function. This this P is a function that will take an element of F and gives you a number between zero and one.

### 01:33:09 · Speaker 6

Yeah

### 01:33:16 · Speaker 6

Got it. So,

### 01:33:17 · Speaker 7

I mean

### 01:33:18 · Speaker 6

Yeah, so am I am I correct in my understanding that the output of P X on small A is actually something in the the P on the left hand side of this

### 01:33:25 · Speaker 7

is

### 01:33:31 · Speaker 7

that's correct. That's precisely correct. Yeah, if you evaluate the probability distribution function, right, at a particular point A, it will give you the same output that the probability measure, right, would have given on the subset A one. Correct, that is correct.

### 01:33:52 · Speaker 6

ओके, या, थैंक यू सर, दैट इज इट.

### 01:33:53 · Speaker 7

See that is why, that is why, that is why

### 01:33:58 · Speaker 7

That is why capital P, right, is a function that would take elements of F and map it to zero one, correct?

### 01:34:08 · Speaker 7

and probability distribution function, okay, will take an element of R and still maps it to zero one.

### 01:34:17 · Speaker 6

Yeah

### 01:34:18 · Speaker 7

you notice that the range space of both of these are same.

### 01:34:22 · Speaker 6

Yes

### 01:34:23 · Speaker 7

by definition. by definition.

### 01:34:27 · Speaker 8

Yeah, that clears it up. Thank you.

### 01:34:29 · Speaker 7

Okay, thanks.

### 01:34:31 · Speaker 7

Okay, anything else?

### 01:34:35 · Speaker 7

So take home message is the following right when you take the distribution function and evaluate at the point what does it give probability of

### 01:34:44 · Speaker 7

the inverse image, right, of the event that is obtained by taking the inverse image of this particular set minus infinity to A under the random variable X. This is the take home message, remember this. uh How do I

### 01:35:00 · Speaker 0

I like this something

### 01:35:05 · Speaker 0

does it stay? It stays. Hold on.

### 01:35:13 · Speaker 0

it in the red

### 01:35:17 · Speaker 0

super duper important okay

### 01:35:23 · Speaker 8

Does red means that this is wrong or something? Oh, it's not used red. Yellow is okay.

### 01:35:33 · Speaker 8

green

### 01:35:33 · Speaker 5

Eight

### 01:35:35 · Speaker 5

Sir if you change the if you change the paper color then it will be more visible.

### 01:35:35 · Speaker 8

Yeah

### 01:35:43 · Speaker 8

from black to white

### 01:35:45 · Speaker 5

White or yellow?

### 01:35:49 · Speaker 8

Okay. This is fine.

### 01:35:52 · Speaker 7

Yeah, please remember this. This is the, this is the message that I'm supposed to give today, okay?

### 01:35:59 · Speaker 7

Fine

### 01:36:01 · Speaker 7

Okay, shall we break for fifteen minutes?

### 01:36:06 · Speaker 8

Yes sir

### 01:36:07 · Speaker 7

There is one other nice question that I was expecting, nobody is asking me, anticipated an answer.

### 01:36:16 · Speaker 7

इट इज टेन फोर्टी फाइव इन माय क्लॉक. लेट्स गेट बैक एट इलेवन पी एम, ओके? सो एल हैव एन एम.

### 01:36:23 · Speaker 7

Okay

### 01:36:23 · Speaker 0

சீ யூ இன் 15 மினிட்ஸ்

### 01:54:42 · Speaker 0

Hello, shall we begin? Continue?

### 01:54:49 · Speaker 7

tell me this uh show of hands please. uh is there anybody who has not studied a probability theory course in your undergrad?

### 01:55:04 · Speaker 7

like no probability theory course at all. Is there anybody

### 01:55:07 · Speaker 8

of anybody like that in the class

### 01:55:14 · Speaker 8

Can you raise your hands?

### 01:55:15 · Speaker 7

there is somebody like that

### 01:55:18 · Speaker 0

So can you repeat?

### 01:55:21 · Speaker 8

So, is

### 01:55:21 · Speaker 7

Is there anybody who has not taken a probability theory course like ever in your life? undergrad or something?

### 01:55:34 · Speaker 7

Okay, nobody. Good. uh See, uh the reason I asked is that like see, all of you know these things maybe in different forms, right? Maybe not this rigorously or in different forms. I just am trying to give you a different perspective, that's all. Right? So, yeah.

### 01:55:53 · Speaker 7

So you people are aware of these things, you know, that cumulative distribution functions, you have heard these terms and like you have worked with these, correct? Quotient distributions and all this. Have you? Most of you have worked with these things, right? I mean you are aware of these things earlier.

### 01:56:08 · Speaker 7

It's good. So as I said, no, the first two, three classes, initial two, three classes, I think I I developed the language and give you perspectives of how I would like to see things and then from then onwards we can take off very quickly. Okay.

### 01:56:22 · Speaker 7

let's get back. So now we are we have the probability triplet and we have a reduced space uh a distribution function associated with it. Now, um I mean it's we are opening Pandora box of probability theory now. It's too many things that come come up. I'll just define a few things that are kind of

### 01:56:44 · Speaker 7

obviously needed for our cost and then we'll move on. See the first thing that I want to define, talk about

### 01:56:51 · Speaker 7

what is

### 01:56:54 · Speaker 7

vectors valued kind of

### 01:56:56 · Speaker 7

tables

### 01:56:59 · Speaker 7

Again another misnomer, okay? So vector valued random variables. This is these are random variables, right? That such that the range space of these this function that we are talking about is R D and not R. Some vectors, okay?

### 01:57:19 · Speaker 7

Do you understand?

### 01:57:22 · Speaker 7

So what is happening is the elements of sample space now gets mapped to D dimensional real numbers not one real number. All the while we were looking at like real numbers here right? The mapping was to real numbers okay? Now in a vector valued case which is our general case right when we have images or like embeddings of text and speech etcetera they are all some D dimensional vectors. So these are like they are called vector valued random variables because

### 01:57:52 · Speaker 7

The range space of the random variable that we have will be vectors. D dimensional vectors in general. Any questions on this?

### 01:58:00 · Speaker 6

Great

### 01:58:00 · Speaker 7

So in this case, right, when we

### 01:58:04 · Speaker 7

evaluate the distribution function, right? The distribution functions gets evaluated at a vector.

### 01:58:14 · Speaker 7

A, right? So now the argument for the distribution function will be a vector A. I will not be using this like head bar after that. This is just for once. Okay. So how do you define this now? This is the probability.

### 01:58:29 · Speaker 7

probability, okay? So let us take an example and do it perhaps easier that way to show.

### 01:58:37 · Speaker 8

So example

### 01:58:40 · Speaker 8

suppose

### 01:58:44 · Speaker 8

suppose uh the random variable

### 01:58:48 · Speaker 8

is

### 01:58:50 · Speaker 7

two dimensional, okay? Maps, the sample space to two dimensional real numbers, okay? Now what happens to

### 01:59:00 · Speaker 7

the distribution function of this. By the way, any notation that I use, you know, this is the notation that I'll be using. When I write this subscript, okay? uh that that that denotes the random variable, okay? And whatever is within the brackets is the value at which we are evaluating this. So now, how do how should I evaluate this? X

### 01:59:22 · Speaker 7

What should I write inside the bracket now?

### 01:59:27 · Speaker 3

x inverse and within brackets the vector

### 01:59:30 · Speaker 7

No, no, no, I'm I'm I'm I'm I'm evaluating it at a point, no? The notation is that probability density distribution function is evaluated at a point. And what is this point, no? This point is now some vector A one.

### 01:59:45 · Speaker 8

Correct

### 01:59:49 · Speaker 0

Yes

### 01:59:51 · Speaker 8

All of you with me on this?

### 01:59:54 · Speaker 8

because the random variable is a two dimensional random variable, distribution function is evaluated at a

### 02:00:00 · Speaker 9

Now again we will interpret this now what does this mean this is the probability of what?

### 02:00:10 · Speaker 9

again

### 02:00:11 · Speaker 3

our own notation, right? It is the probability of the inverse image under X. Of what set are we considering here? Can somebody tell me what is this set?

### 02:00:31 · Speaker 2

You understand

### 02:00:31 · Speaker 3

infinity to a1 minus infinity to a2

### 02:00:35 · Speaker 2

I

### 02:00:35 · Speaker 3

Infinity Two

### 02:00:37 · Speaker 10

A one and minus infinity to A two

### 02:00:41 · Speaker 3

No, what should I? This is one set. What should I write? I should write a bracket here.

### 02:00:49 · Speaker 3

Should I write?

### 02:00:52 · Speaker 9

in

### 02:00:52 · Speaker 1

This is also a vector

### 02:00:52 · Speaker 2

This is also a vector

### 02:00:53 · Speaker 9

understand it's an area sir like

### 02:00:56 · Speaker 3

So what should I write here? Tell me. How should I write that set?

### 02:00:59 · Speaker 2

cross

### 02:01:01 · Speaker 3

Yeah

### 02:01:08 · Speaker 3

Okay, so does all of you understand this? What is this cross? This is what is this cross?

### 02:01:16 · Speaker 3

the Cartesian product.

### 02:01:21 · Speaker 3

just tell you what that means.

### 02:01:23 · Speaker 9

See, one dimension, if you have a line, there is an A, right? The set that we are that we are talking about is minus infinity, that would end at A, correct? So this is the set that we are taking talking about, minus infinity to A, is this particular set, correct? Now in two dimensions,

### 02:01:45 · Speaker 9

If you take a point like this is A one comma A two, right? What is the set that we are talking about? Now we are not talking about the subsets of R two. They are not lines. What are they?

### 02:02:01 · Speaker 3

area

### 02:02:01 · Speaker 5

area

### 02:02:02 · Speaker 3

Kerry

### 02:02:03 · Speaker 9

want to call them areas.

### 02:02:06 · Speaker 5

play

### 02:02:06 · Speaker 3

plane

### 02:02:06 · Speaker 1

play

### 02:02:07 · Speaker 9

planes. Yeah, they are planes. Okay, first of all, subsets of R two are planes. Okay? So what sort of plane are we talking about? So let's say that we have A one, A two here. This is where we are evaluating the distribution function. What is the set that I just wrote? What does that correspond to?

### 02:02:29 · Speaker 3

Sir, anything to the left of

### 02:02:36 · Speaker 2

This is, this is A2

### 02:02:36 · Speaker 3

A one

### 02:02:38 · Speaker 2

Okay

### 02:02:45 · Speaker 3

and this is A one. Now tell me what is the set that I'm talking about?

### 02:02:52 · Speaker 7

towards the left of line A one and below the line A two.

### 02:02:52 · Speaker 3

लेफ्ट ऑफ

### 02:02:56 · Speaker 9

this line.

### 02:03:00 · Speaker 9

the space. This entire space which extends infinity to infinity to in the left direction and to infinity in the bottom direction. Is this clear? So this set

### 02:03:13 · Speaker 9

is

### 02:03:15 · Speaker 2

the Cartesian product of

### 02:03:23 · Speaker 2

is all of you clear?

### 02:03:32 · Speaker 2

Now

### 02:03:32 · Speaker 9

we will not be working in two dimensions. We will be working in like ten thousand dimensional space because our image is in ten thousand dimensions. So when I evaluate distribution function at ten thousand dimensional point, a vector at ten thousand dimension, you should remember what is the inverse image that it maps to.

### 02:03:50 · Speaker 9

It's a cartesian product of like all those things. Do you see that? It will be a hyper volume in that dimension.

### 02:04:00 · Speaker 9

Is it okay?

### 02:04:04 · Speaker 9

See when I evaluate the distribution function at a particular point in some ten thousand dimensional space, I'll be looking at the inverse images under that random variable of a certain hyper volume.

### 02:04:16 · Speaker 9

What is that hyper volume? That hyper volume is given by this sort of a Cartesian product, no? Minus infinity to the first element cross, minus infinity to the second element cross, minus infinity to the third element and so on. That becomes a hyper volume. In three dimensions I can tell you what that is, no? It's a it's a huge three dimensional volume, right? In four dimensions I don't know what it is, just call it hyper volume.

### 02:04:37 · Speaker 9

Is that okay? So we'll be working with such distribution. We'll be working with random variables whose range space happens to be in some d-dimensional real space. And in if it's if it's an image then it is some ten thousand dimensional. uh If it's see, what is the size of the embedding in bird kind of models is few hundreds, right? Or few thousands I suppose.

### 02:05:02 · Speaker 9

Can somebody tell me in bird kind of models what is the size of embedding vectors that you get for each bird?

### 02:05:09 · Speaker 9

Google that

### 02:05:12 · Speaker 9

bird embedding size

### 02:05:15 · Speaker 1

five twelve

### 02:05:15 · Speaker 3

conclusion

### 02:05:16 · Speaker 2

Hello

### 02:05:16 · Speaker 3

is it frightful?

### 02:05:20 · Speaker 3

I think

### 02:05:24 · Speaker 3

I use

### 02:05:27 · Speaker 9

768 length vectors word base and word tiny gives you 128 dimensional vectors. Yeah of order of hundred so that is that is your like that is the dimensionality of the range space of the random variable that you will be talking.

### 02:05:40 · Speaker 3

that we'll be working with. Is this idea clear to all of you?

### 02:05:52 · Speaker 3

any questions on this? So from now on we will be

### 02:05:55 · Speaker 9

working on working with vector valued random variables, okay? not the scalar which means that the elements of sample space gets mapped to a d dimensional real number, okay?

### 02:06:06 · Speaker 9

Right

### 02:06:08 · Speaker 9

products, Cartesian products. Okay, fine.

### 02:06:12 · Speaker 2

Now the next thing that I want to talk about is that

### 02:06:23 · Speaker 2

why doesn't it come to a middle

### 02:06:28 · Speaker 2

Fine

### 02:06:30 · Speaker 2

B

### 02:06:34 · Speaker 2

talk of multiple random variables.

### 02:06:52 · Speaker 2

ओके. सपोज देयर आर टू

### 02:06:58 · Speaker 2

random experiments that are happening.

### 02:07:06 · Speaker 2

Let me give you an example. What I do is first

### 02:07:12 · Speaker 2

that

### 02:07:25 · Speaker 2

Okay, continue

### 02:07:27 · Speaker 2

give you a simple example

### 02:07:33 · Speaker 2

So it's a coin that is being tossed.

### 02:07:41 · Speaker 2

and there is a die that is being rolled.

### 02:07:49 · Speaker 3

TYE or DYE, what is that?

### 02:07:52 · Speaker 3

C Y E Z No D I E

### 02:08:03 · Speaker 2

CY is color I suppose no?

### 02:08:06 · Speaker 3

Yes sir. It should be D I E.

### 02:08:09 · Speaker 2

P I E

### 02:08:10 · Speaker 3

Hello

### 02:08:16 · Speaker 3

If it is singular it should be D I C E.

### 02:08:19 · Speaker 2

Dynas correct

### 02:08:21 · Speaker 3

Sir

### 02:08:23 · Speaker 9

the dice being rolled okay. Thanks. Yeah. So now what happens is see both of these will have their own sample spaces.

### 02:08:34 · Speaker 9

and underlying probability measures, right? Let's call this P one. There is another sample space. There is another uh event space. There is another probability measure, correct?

### 02:08:47 · Speaker 9

right? Now what I can do is, I can take an element A, okay, belonging to F one.

### 02:08:57 · Speaker 9

and element B that

### 02:08:59 · Speaker 2

belonging to F2

### 02:09:03 · Speaker 2

Okay

### 02:09:05 · Speaker 2

I can do this

### 02:09:21 · Speaker 2

Sorry

### 02:09:34 · Speaker 2

thinking is just the best way to take hold this point there are other ways to do it.

### 02:09:58 · Speaker 2

maybe this is not the best example

### 02:10:10 · Speaker 2

Yeah, this may not be

### 02:10:11 · Speaker 3

best example because

### 02:10:14 · Speaker 3

Paytm Center

### 02:10:16 · Speaker 3

intersections no that create some lack in understanding

### 02:10:27 · Speaker 3

better to talk that there are two random experiments okay. So which is like

### 02:10:35 · Speaker 2

Consider Rolling

### 02:10:40 · Speaker 2

Two

### 02:10:43 · Speaker 2

size of

### 02:10:48 · Speaker 2

of different configuration. I think this would be a better example.

### 02:11:02 · Speaker 2

so this can

### 02:11:03 · Speaker 9

a good example that what we are doing is that we are we are rolling two dice of different configuration which means that there are two sample spaces each

### 02:11:13 · Speaker 3

gain and two different probability measures

### 02:11:23 · Speaker 3

E two okay. Now again if

### 02:11:26 · Speaker 9

there is an element

### 02:11:28 · Speaker 9

that is in F one and an element that is in F two, right? Because because these are sets, we can talk about unions and intersections of these, right?

### 02:11:44 · Speaker 9

Can you see what I'm talking about?

### 02:11:47 · Speaker 9

We have two random variables, we can talk about unions and intersections of these events, right? These these these subsets or these yeah, these subsets of different sample spaces. Now because we can do that, there are a few things that are being defined which are like something called

### 02:12:04 · Speaker 3

um

### 02:12:06 · Speaker 3

you can define a probability measure on

### 02:12:12 · Speaker 3

Hence

### 02:12:15 · Speaker 3

In fact, see the unions and intersection

### 02:12:19 · Speaker 9

may not be on two different sets, right? I mean unions and intersections may be on like one random variable as well. Unions and intersections may be on a single random variable as well. But yeah, let's say that we are defining unions and intersections of the the

### 02:12:38 · Speaker 9

the elements of outcomes from two different runtime variables. You can always talk of probability of unions and probability of intersections and so on. Also this conditional probability that is defined, you know, it is defined as a condition term B. You know the definition, right? It is the probability of the intersection

### 02:13:00 · Speaker 9

divided by the probability of

### 02:13:03 · Speaker 9

conditioning given. This is how the conditional probability is defined. All of you know this, right? That's why I asked you whether you people know probability theory. This is known, right? All of you know this? Okay, great.

### 02:13:13 · Speaker 9

Now what I wanted to tell you is because we can define like conditional probabilities and unions of probabilities on on on on outcomes coming from two different experiments. Now now what happens is

### 02:13:31 · Speaker 9

there are two probability spaces.

### 02:13:37 · Speaker 9

there are two probability spaces. which means that there are two induced spaces. let's call them x.

### 02:13:44 · Speaker 9

gives rise to

### 02:13:48 · Speaker 9

one distribution function. Okay? There is another

### 02:13:53 · Speaker 9

sample space and the corresponding probability measure. It's called that Y. This gives rise to another

### 02:14:04 · Speaker 9

induced pressure

### 02:14:06 · Speaker 9

Okay. Now since we can talk of the unions and intersections of the the elements from the sample space, we can talk of what are called as joint distributions.

### 02:14:27 · Speaker 9

See, I will kind of hand wave now and not not talk talk I mean not go to details of the the the definitions. So this is represented like this which is a joint distribution of pair of random variables. Now this is evaluated at two points, no? X, Y, A, B, let's call it.

### 02:14:51 · Speaker 9

Okay? What does this mean? We'll go to our own definition. This is the probability, okay? So now this is like you take the x inverse of this particular event, the yeah, the event that gets mapped to this particular thing under x, okay? You take the cartesian product of this under the random variable y, take this event that gets mapped to

### 02:15:20 · Speaker 9

maps under this inverse image. And that probability, right? So this will be the probability of some event A that belongs to F one.

### 02:15:33 · Speaker 9

Intersection

### 02:15:34 · Speaker 3

Hmm

### 02:15:35 · Speaker 2

some event B that belongs to F.

### 02:15:40 · Speaker 3

Is this clear?

### 02:15:41 · Speaker 3

What happened to this?

### 02:15:47 · Speaker 3

Is this clear?

### 02:15:50 · Speaker 9

So we can talk of joint distributions, right? I mean joint distributions are again, we are talking of probability of intersections of events. Now these are intersections of events that are that are belonging to uh two different sample spaces. Now these are how do you get it? Then you take first random variable, take its inverse image, get one event, take another random variable, take that, take its inverse image, you get another event, take the intersection of those two, that is the and look at the probability of that. and that will give you the value of the distribute joint distribution function evaluated at those two values.

### 02:16:27 · Speaker 3

Okay. So similarly you can also talk of conditional distributions.

### 02:16:36 · Speaker 3

definition of conditional distribution is slightly involved. Okay, let me not give you the the definition of it. Okay, denoted by this. Okay, this is evaluated at one point. This is

### 02:16:54 · Speaker 3

is like x

### 02:16:57 · Speaker 3

equal to or x

### 02:17:01 · Speaker 3

Yeah

### 02:17:04 · Speaker 3

even y equal to some p, okay?

### 02:17:10 · Speaker 3

Meet

### 02:17:10 · Speaker 9

I don't want to

### 02:17:13 · Speaker 9

in continuous random variables, no, this this has a very this has an involved definition, but roughly you can see that as the we are looking at the probabilities of

### 02:17:24 · Speaker 9

these kinds of events, right? Conditional events. So we are looking if this corresponds to some conditional, uh, the probability of some conditional distribution, it's the probability, probability of some conditional event, okay? That the definition of condition, the conditional event is this, which is that you take the probability of intersection and divide it by the probability of the, uh, the, uh, the conditioned event. Now it has a similar definition, but yeah, it's, yeah, you need a little bit of measure theory to know this at least for the case of

### 02:17:58 · Speaker 9

continuous random variables and by the way all the definitions that I have given so far are for continuous random variables. If it's a discrete random variable no. What happens is the mapping that the random variable does is element by element so you are talking about the inverse images of single tons. Okay.

### 02:18:17 · Speaker 9

This is a conditional distribution. So basically what I the two points that I wanted to drive home is that there can be vector valued random variables which would take the sample space and maps it to vectors and there can be pairs of random variables where you should envisage you should you should you should imagine two random experiments that are happening, okay? So there is an association between those two random variables that happens through intersections and unions of them. words. Okay? And and you can define joint distributions and contingent distributions. Now, definition wise,

### 02:18:56 · Speaker 3

This is defined as

### 02:18:59 · Speaker 3

the

### 02:19:05 · Speaker 3

joint distribution divided by

### 02:19:08 · Speaker 9

marginal of value. So it is defined mathematically. uh But yeah, so it always has a corresponding probabilistic interpretation as we were looking at. Okay. Okay. uh Questions. Abhirup.

### 02:19:26 · Speaker 6

Yeah, so I could not understand a couple of things. Can you scroll up a little bit?

### 02:19:32 · Speaker 9

in which part? vector value and

### 02:19:33 · Speaker 6

vector value. After after after the vector value when you are actually saying that yeah. So A belongs to the event space F one and B belongs to the event space F two. Then when we are talking about A union B. So the A and B they belong to two different sets. So I I cannot understand the notion how you can do a union. Yeah.

### 02:19:37 · Speaker 9

design

### 02:19:38 · Speaker 9

Hmm

### 02:19:45 · Speaker 9

in

### 02:19:49 · Speaker 9

and be

### 02:19:53 · Speaker 9

Praskanth

### 02:19:55 · Speaker 9

union

### 02:19:56 · Speaker 9

you

### 02:19:56 · Speaker 9

You can, no? See, it's like you take a set, uh, let's say that we have two subsets of R. You can define a union of both of them, right? Why can't you do that?

### 02:20:06 · Speaker 6

Yeah, so that is because in that case the universal set is R. So, so my question is that

### 02:20:12 · Speaker 9

Same thing I'm saying you are calling two types of different configuration universal center is same thing right?

### 02:20:19 · Speaker 6

So in so in case of A

### 02:20:20 · Speaker 9

That is why you you remember I said toss a coin roll a die

### 02:20:25 · Speaker 6

Yeah

### 02:20:26 · Speaker 9

Then I erase that example precisely because of this, it will create confusion. In the example that I have given, the universal set is the comprising of rules of dice for both the cases, no?

### 02:20:40 · Speaker 6

okay. So if we are considering one event space as rolling a die and another event space as tossing a coin, then the universal spect is

### 02:20:48 · Speaker 9

then the universal set will be one to six and those two things head and tail that's all

### 02:20:53 · Speaker 6

Okay, so it is going to be F1 union F2?

### 02:20:56 · Speaker 9

Of course, of course, sigma omega one cross omega two. Omega one cross omega two. That would be your universal sample space.

### 02:20:57 · Speaker 6

Wow

### 02:21:06 · Speaker 6

Okay, I didn't

### 02:21:07 · Speaker 9

I didn't want to do that because of this precise reason. So if you roll a die and toss a coin, then how can you define unions is a question that I anticipated. That's why I said roll two dice.

### 02:21:18 · Speaker 6

Okay, okay, okay. And also, second question, went a little bit down, if you if you don't mind, a little bit scroll down.

### 02:21:20 · Speaker 5

also

### 02:21:23 · Speaker 9

Rupendra

### 02:21:28 · Speaker 6

Yeah, so x inverse of minus infinity to a cross of y inverse of this one. So how are you replacing the cross sign with an intersection sign in the next line? I have a difficulty in understanding that.

### 02:21:42 · Speaker 9

Ha. See, the cross products here, right? In the Cartesian, it this maps to one event, that maps to another event, right?

### 02:21:52 · Speaker 6

Okay

### 02:21:53 · Speaker 9

So that is the intersection only.

### 02:21:57 · Speaker 3

Hmm

### 02:22:00 · Speaker 3

Okay

### 02:22:05 · Speaker 2

Okay

### 02:22:06 · Speaker 9

So the point is that here when you talk of intersection, you talk of cross points of two sets, isn't it?

### 02:22:13 · Speaker 9

This is cross product of two sets. Intersection is nothing but cross product of two sets, no?

### 02:22:13 · Speaker 3

This is cross product

### 02:22:18 · Speaker 3

Yeah, yes, sorry.

### 02:22:20 · Speaker 9

That's it.

### 02:22:22 · Speaker 9

Okay, Sarvesh

### 02:22:26 · Speaker 8

Yes, it's the same thing like x inverse of minus infinity a gives a, correct? And gives a

### 02:22:31 · Speaker 9

A

### 02:22:33 · Speaker 9

gives A that yeah. Yeah and that gives you B. Yeah.

### 02:22:36 · Speaker 8

Yeah, and that gives you P.

### 02:22:37 · Speaker 8

P

### 02:22:38 · Speaker 8

gives B and same thing like it has a A cross B right

### 02:22:39 · Speaker 9

Hmm

### 02:22:44 · Speaker 9

defined it is defined that way you know joint distribution is defined that way by definition

### 02:22:44 · Speaker 8

So

### 02:22:50 · Speaker 8

Yeah, so it's a cross product, right? So,

### 02:22:52 · Speaker 9

Correct. It is by definition.

### 02:22:55 · Speaker 8

so below it should also should be a cross b right so there will be pairs ordered pairs of a and b. no no no a is

### 02:23:00 · Speaker 9

sets of A and B. No no no A is no no no so there are two sets no I'm talking about two sets here so probability is defined that is why you have the the probability or intersections are defined.

### 02:23:07 · Speaker 8

Yeah

### 02:23:15 · Speaker 9

Okay. So here the distributed joint distributions are defined that way. And if you evaluate it, they are actually the intersections of uh see in fact I should I don't know where the difference is coming from. Let's just say that these are intersections by definition.

### 02:23:32 · Speaker 9

it's a neural grid that will clear the thing, no?

### 02:23:37 · Speaker 8

Okay

### 02:23:38 · Speaker 9

And that's that's the definition of job distribution by the way. Yeah.

### 02:23:43 · Speaker 3

Yeah

### 02:23:43 · Speaker 9

ओके संजीव

### 02:23:46 · Speaker 7

Sir, if we try to understand joint distributions with an example, so, okay, let me just uh explain what I perceived by this statement is, we have, we want to find the joint distribution for events where there is a three on the first die and a four on the second die. Okay? So getting a three becomes event A and on getting a four on dice two becomes event B. So we want So, Goa

### 02:24:16 · Speaker 9

So goes to those two gets mapped those two gets mapped to different points at the by two different random variables and look at the inverse image that's all. Yeah it's correct.

### 02:24:24 · Speaker 7

correct correct so now when we want to find the probability that event A belongs to F one and event B belongs to F two so it will only be both are happening so that means we will obtain the cartesian product of F one and F two and in that only point three comma four where three is obtained on die one and four is obtained on die two

### 02:24:26 · Speaker 9

Yeah

### 02:24:34 · Speaker 9

Only meaning

### 02:24:49 · Speaker 9

and on

### 02:24:49 · Speaker 9

agree. That's that's the that's the intersection that will happen. Yeah. That is the only

### 02:24:54 · Speaker 7

that is the only intersection, right? Because otherwise, since both

### 02:24:55 · Speaker 9

right?

### 02:24:56 · Speaker 9

otherwise since both Correct you Okay I understand what you're saying yeah Okay sir yeah Rajendra

### 02:24:59 · Speaker 7

Okay

### 02:25:01 · Speaker 7

ओके सर

### 02:25:04 · Speaker 10

Yes sir, in this case the x and y have to be independent, right?

### 02:25:08 · Speaker 9

No. They need not be. If they are independent then I mean I have not defined independence, right? Random variables are called independent if the joint distribution happen to be the product of marginals.

### 02:25:22 · Speaker 9

They are independent and intersection is null.

### 02:25:28 · Speaker 9

They are not independent, right? This is a general definition. General definition. So there can be so one experiment

### 02:25:31 · Speaker 10

So there can be so one experiment can be dependent on the other

### 02:25:35 · Speaker 9

they are they are actually I mean the moment I talk of joint distributions they are dependent no

### 02:25:41 · Speaker 9

If they are independent then the joint distribution will become the product of marginal, isn't it?

### 02:25:45 · Speaker 10

No, no, what I meant is, say for example, in this case of rolling two die, the outcome of the second experiment shouldn't depend on the outcome of the first.

### 02:25:55 · Speaker 9

the way we have conceived it, they are dependent.

### 02:25:59 · Speaker 9

Independence is if P of X Y is given by P X into P Y then it is independent.

### 02:26:08 · Speaker 10

Okay, but this is not a necessary condition.

### 02:26:10 · Speaker 9

No. Why? I mean the way we have conceived pair of random variables is that in general they are not independent, right?

### 02:26:11 · Speaker 10

I mean

### 02:26:16 · Speaker 10

Okay, okay.

### 02:26:18 · Speaker 9

Yeah. Okay. Shivam,

### 02:26:22 · Speaker 4

Yes sir, I don't have any question, just one thing that I am getting confused with small y, capital y, sir. Last time also...

### 02:26:29 · Speaker 9

No, where is small y? I'm not using small y. It's all capital Y now.

### 02:26:32 · Speaker 4

Yeah, on the conditional distribution, yeah. So it's all random variable, right? So capital Y.

### 02:26:38 · Speaker 9

sorry, my my bad, sorry. Yeah.

### 02:26:42 · Speaker 4

No sir, in your previous lectures also, the small y and capital y, we tend to use it here and there.

### 02:26:50 · Speaker 9

interchangeable yeah no no no yeah thanks for thanks for bringing that up. if I make that mistake again just alert me okay. രണ്ടാമൊരു സോ സോ ദാറ്റ് ഐ ക്യാൻ

### 02:27:00 · Speaker 9

correct myself. Yeah. See, yeah, this is I think how what is the how many times I've taught, no? um 2017 is when I started. This is 20, 24, seven years. So on an average, I mean, not on an average, every time I've taught in the semester is 14 times and this online some three, four times, but this 17, 18 times I've taught. So what you are seeing now is actually

### 02:27:30 · Speaker 9

done gradient descent on my teaching based on feedback every time. And it has come to some optimum and that is what you are seeing. So imagine what my students have the plight of my students seven years back. I didn't know how to do board work. Right I was like in spite of doing it for fifteen times eighteen times sometimes the notations gets here and there and all that. But yeah I think I have improved right a lot of my students

### 02:28:00 · Speaker 9

you need that type for like improve over time that's why I have that feedback form you see please use that if you have any concern that you cannot when Shiv was bold enough to tell me that I do this I appreciate that I don't mind you can tell me that this is you are going fast whatever you know I don't mind okay you can express it but if you think that expressing that will embarrass you for whatever reason you have that anonymous feedback form

### 02:28:30 · Speaker 9

Do put in your comments, right? Constructive, destructive. I told you, right? A lot of times students use it to vent out their frustration. It's okay at times you can do that, but don't use it for just venting out your frustration, right? So that will be too much negativity.

### 02:28:47 · Speaker 9

Okay. Great. Okay. So, Shivam, thank you for that. If you if you notice such a such kind of a thing, just let me know. I'll try to be consistent as much as possible in notations. I I understand how important it is to be consistent.

### 02:29:03 · Speaker 9

Okay, maybe I'll take this B out. I'll tell you why this why I wrote this in a while. Okay, so these are I'm kind of hand waving now because like this is not a probability theory course, right? This is just to put some basics on it.

### 02:29:19 · Speaker 3

Okay

### 02:29:20 · Speaker 9

Now

### 02:29:20 · Speaker 3

Hello

### 02:29:21 · Speaker 9

Now let us come to uh yeah independence, condition distributions, joint distributions, multiple random variables. Yeah one other thing that is to be defined is what is called as a probability density function.

### 02:29:38 · Speaker 1

I don't know how to speak English, bro. చెప్పాలి కదా బాబు.

### 02:29:50 · Speaker 3

Was that some gali in some some language?

### 02:29:52 · Speaker 9

Okay

### 02:29:53 · Speaker 3

speak in your language

### 02:29:55 · Speaker 9

that I don't understand right what can I do

### 02:30:00 · Speaker 9

See, gaali makes sense only if you make the other person understand what you are saying, no? So See, I have again off topic but I this is a professional tip. I've had it for ten years. So if I'm too angry, right, on my children or like on my wife and I don't want to escalate the war, what I do is I'll start scolding them in Sanskrit or some other language that they don't understand. So that you know my anger is vented out but they don't

### 02:30:30 · Speaker 9

understand and respond back so that no escalation happens. So maybe somebody is doing that that way who knows. Okay, uh so probability density functions. So now probability density functions, okay notation wise note that for distribution functions I'm using this script P right? I mean two lines P. So for probability density functions I use like small p. So this probability density function is a function right? That is equal टू द डेरिवेटिव ऑफ द डिस्ट्रीब्यूशन फंक्शन, राइट? एवाल्युएटेड दैट पॉइंट, दैट्स ऑल, ओके?

### 02:31:10 · Speaker 2

maybe not use A, let's use some other thing here.

### 02:31:22 · Speaker 2

Yeah, this is the definition of the probability

### 02:31:24 · Speaker 9

डेन्सिटी फंक्शन. इट्स जस्ट

### 02:31:25 · Speaker 3

just

### 02:31:25 · Speaker 7

Derivatives

### 02:31:26 · Speaker 9

Question

### 02:31:27 · Speaker 9

Yes

### 02:31:28 · Speaker 7

Sir, maybe I am moving ahead, but just for clarification, for continuous random variables, we have CDF and PDF, like cumulative distribution and probability density functions, correct?

### 02:31:41 · Speaker 9

Hmm hmm

### 02:31:43 · Speaker 7

and for discrete

### 02:31:43 · Speaker 9

for discrete random variables I will tell you so that will become probability mass functions. distribution functions are the same. this will become probability mass functions.

### 02:31:52 · Speaker 7

ओके सर

### 02:31:54 · Speaker 9

Okay, so good that you mentioned that. See, mostly in this course we'll be dealing with continuous random variables.

### 02:32:03 · Speaker 9

Hello

### 02:32:04 · Speaker 9

Yeah, that you mentioned that probability mass functions. So, this is for this is for continuous random time variable, okay? For discrete random time variable, the probability density function is nothing

### 02:32:17 · Speaker 2

but the

### 02:32:26 · Speaker 2

first difference.

### 02:32:33 · Speaker 2

distribution function evaluated that and distribution function evaluated

### 02:32:38 · Speaker 3

Uh

### 02:32:41 · Speaker 3

A plus one and A, yeah.

### 02:32:46 · Speaker 9

that is the density function. This is for the discrete random variable. Okay. So p is node that this right is this is not a probability. That is why you know if you take an example right if you take a random variable this notation is

### 02:33:05 · Speaker 9

normally distributed with zero one, okay? This means that the density function of this is equal to that thing one by two pi sigma squared.

### 02:33:18 · Speaker 9

e power minus x minus mu whole square divided by two sigma square right?

### 02:33:27 · Speaker 9

I think there is a square root here. Yeah, I don't remember this and and I don't expect you to remember as well. This is for a scalar valued case, for a vector valued case that is one by

### 02:33:38 · Speaker 9

two pi to the power of d by two where d is the dimensionality and you have the determinant of this matrix. So e power minus

### 02:33:49 · Speaker 9

x minus mu transpose. So this is a vector of d dimensions. Sigma is a matrix d by d. This is x minus mu. Right? This is what it is. So now note that this entire thing is a scalar, no?

### 02:34:05 · Speaker 9

this is d cross one times d cross d times one cross d. So my x and mu are d cross one. I'll I'll tell you.

### 02:34:18 · Speaker 9

set it is for once for all one cross d times d cross d times d cross one so this would be one cross d times

### 02:34:30 · Speaker 9

T cross one. This will be one cross one because X is in R D. The range space of random variable is T dimensional which means that mu is also in R D. Okay? This is the probability whenever we see in most of M L right we we work with density functions not distribution functions because of ease of computation that's what I mean lot of standard metrics exist lot of standard forms exist for density functions. Okay? What is the what is density function?

### 02:35:00 · Speaker 9

density function is nothing but the derivative of the distribution function. So if you evaluate the density function at a point, right, what you are getting is the derivative of the distribution function at that point, that's all. Please note that if you evaluate the density function at a particular point A, it you are not getting the probability of that point.

### 02:35:21 · Speaker 9

Okay? So this is one take home message. Evaluating the density function at a particular point will not give you the probability of that point.

### 02:35:30 · Speaker 9

because probability of a point does not make sense. Probability, remember, is a measure that is defined on the elements of sample space always. Okay? Evaluating the density function at a point will simply give you the derivative, the value of the derivative of the distribution function at that point. That's all.

### 02:35:50 · Speaker 3

Hello

### 02:35:51 · Speaker 9

If you take the density function, right? And integrate it.

### 02:36:00 · Speaker 9

over a ring, over a set, what do you get? This is equal to the distribution function evaluated at A. See, this is equal to the probability of that entire story.

### 02:36:17 · Speaker 2

Do you understand this? What I'm saying is

### 02:36:23 · Speaker 2

evaluating

### 02:36:26 · Speaker 2

the density function

### 02:36:32 · Speaker 3

at a point.

### 02:36:35 · Speaker 3

is not equal to

### 02:36:38 · Speaker 3

the probability is not equal to probability of anything.

### 02:36:44 · Speaker 3

Okay

### 02:36:44 · Speaker 2

However,

### 02:36:47 · Speaker 2

Integrating

### 02:36:52 · Speaker 2

Density function

### 02:36:57 · Speaker 2

Poor Asset

### 02:37:00 · Speaker 2

is

### 02:37:00 · Speaker 9

equal to

### 02:37:02 · Speaker 9

the probability. So for instance, right, if you take the density function and integrate it between A and B, what do you get? You will get the distribution function evaluated at B minus the distribution function evaluated at D. So this is a valid probability, you know this, right?

### 02:37:22 · Speaker 9

always remember that evaluating the distribution function will give you a valid probability. evaluating the density function will not give you a valid probability. but integrating the density function over a range will give you a valid probability because that is equal to the distribution function.

### 02:37:39 · Speaker 3

is this clear to all of you?

### 02:37:49 · Speaker 2

Okay

### 02:37:50 · Speaker 3

Okay, so now I think we have like, you know,

### 02:37:53 · Speaker 9

background to any questions so far?

### 02:37:57 · Speaker 9

Now let's come back to that problem of estimating genders from an image.

### 02:38:04 · Speaker 7

सर, वन क्वेश्चन

### 02:38:06 · Speaker 9

before you ask the question, uh I have a request. uh with this background, right, you know, please go back to that uh that you know, that good fellow's book on machine learning and read the chapter on distribution and and probability theory, please. So, while you come to the next class, I expect you, I expect all of you to know all this. This was this actually kind of uh brings us to the end of uh the basic probability theory treatment.

### 02:38:36 · Speaker 9

okay? I I don't intend to teach you probability theory because I assume that you people know it but just to give this perspective I spent some time. please go back and brush up your probability theory fundamentals before you come to the next class. please do that. okay? questions.

### 02:38:53 · Speaker 7

Sir, so when we have the probability density function and we have px of a. So there a like it it does not evaluate to minus infinity comma minus a, right?

### 02:39:09 · Speaker 9

அப்போ இங்க இஃப் யூ டே இஃப் யூ எவாலியூட் தி ப்ராபிலிட்டி டென்சிட்டி ஃபங்க்ஷன் அட் எ பாயிண்ட்

### 02:39:13 · Speaker 7

हां, सो इट इट डस नॉट मीन दैट इट इज अ रेंज फ्रॉम माइनस इन्फिनिटी कॉमा ए, इट इज स्ट्रिक्टली एडमॉइडेड।

### 02:39:19 · Speaker 9

No no no no it is simply no no it so it is simply means that you are taking the derivative of the distribution function and evaluating that at A that's all.

### 02:39:30 · Speaker 2

Okay

### 02:39:32 · Speaker 9

evaluating the see if you suppose you plug in some value A into the Gaussian distribution and evaluate it, it only means that

### 02:39:42 · Speaker 9

there is an underlying random variable, okay, with a distribution function. And that distribution function

### 02:39:50 · Speaker 9

you take the derivative of the differential of that distribution function and evaluating that derivative at A that's all it means.

### 02:39:58 · Speaker 7

Okay sir

### 02:40:00 · Speaker 9

Okay. But if you take the distribution function, if you take this Gaussian distribution, Gaussian density function, okay?

### 02:40:09 · Speaker 9

integrated within a range. Then what you are doing is evaluating the distribution function at two different points, no?

### 02:40:20 · Speaker 9

That is what I wrote. If you take it and take the running integral of this part, you get the distribution function evaluated at this point A.

### 02:40:28 · Speaker 9

If you take the range if you take the distribute density function and integrate it between a range it is equivalent to evaluating distribution functions at those two end points and taking the difference which is a probability. Because distribution function evaluated at a point will give you a probability.

### 02:40:45 · Speaker 7

ओके सर

### 02:40:47 · Speaker 9

Got it? So remember this now.

### 02:40:51 · Speaker 9

And sir distribution, okay, okay, let me let me let me tell you. So suppose there is a random variable that is uniform, Astik, I'll take your question, that is uniform between zero and half, okay?

### 02:40:51 · Speaker 7

And sir distribution

### 02:41:03 · Speaker 9

What is the density function of this?

### 02:41:10 · Speaker 9

people know what the active function of this is.

### 02:41:13 · Speaker 9

uniform random variable between zero and A and B.

### 02:41:17 · Speaker 9

What is the density function of a uniform random variable between between A and B?

### 02:41:22 · Speaker 6

to

### 02:41:23 · Speaker 4

Zero if less than zero

### 02:41:28 · Speaker 4

and half minus zero is the one by t minus a

### 02:41:30 · Speaker 6

वन बाय थ्री माइनस है

### 02:41:32 · Speaker 6

1/v-a

### 02:41:32 · Speaker 9

वन बाय बी माइनस ए रो, वन बाय बी माइनस ए रो. इट इज इक्वल टू ज़ीरो, राइट? इफ

### 02:41:42 · Speaker 9

excess

### 02:41:44 · Speaker 3

Yeah, maybe it's easier to write it that way. It's equal to two

### 02:41:51 · Speaker 9

Friends

### 02:41:53 · Speaker 9

X is between this, right? And zero otherwise.

### 02:42:00 · Speaker 9

The density function of a uniform random variable looks like this, no, zero and a half. This is zero, this is half. The height is equal to two. This is how the density function

### 02:42:09 · Speaker 3

looks. Right? All of you agree? Anyone has a question on this?

### 02:42:19 · Speaker 3

Now

### 02:42:20 · Speaker 9

if we were to say that evaluating the density function at a point will give you a probability, how can that happen? It's contradictory, no?

### 02:42:30 · Speaker 9

The probability is upper bounded by one. Density function is evaluated at a particular point here will not give you a probability. Do you see that? Do you appreciate that? This is an example that I have constructed to show you that evaluating the density function at a point will not give you

### 02:42:48 · Speaker 3

your probability

### 02:42:52 · Speaker 2

Is this clear?

### 02:42:57 · Speaker 2

However,

### 02:42:58 · Speaker 3

If you take if you integrate this

### 02:43:00 · Speaker 9

If you take a small area

### 02:43:03 · Speaker 9

This is a probability because you know that will evaluate something less than one between zero and one. Clear?

### 02:43:13 · Speaker 9

evaluating the density function at a point will not give you probability but integrating that will give you probabilities. Is that okay? Because integrating the density function is equivalent to evaluating the distribution function at a particular point.

### 02:43:29 · Speaker 9

Right?

### 02:43:31 · Speaker 9

ओके, आस्तिक

### 02:43:34 · Speaker 5

Yeah, hi sir. So, uh in the above integral, uh where you are integrating it from A to B, I just have a doubt with the notation. So, you have written P X of small x and then D of capital X. Is it correct or it should be D of small x?

### 02:43:42 · Speaker 6

strap

### 02:43:54 · Speaker 5

Okay. And also while you define the derivative, there also it should be small x, right? Where you define the...

### 02:43:55 · Speaker 6

And also

### 02:43:55 · Speaker 6

Mistake

### 02:43:57 · Speaker 9

um

### 02:44:05 · Speaker 9

depends. depends I mean this if it's a if it's a if it's a scalar valued random variable then it's small x right. if it's a vector valued random variable what happens it's the gradient that we define that's all. right. because the you understand.

### 02:44:14 · Speaker 5

Vector

### 02:44:19 · Speaker 5

because

### 02:44:22 · Speaker 5

Yeah.

### 02:44:23 · Speaker 9

Yeah.

### 02:44:26 · Speaker 5

Yeah. Thank you. That's it.

### 02:44:29 · Speaker 2

Yeah

### 02:44:31 · Speaker 1

Okay, uh so this is clear.

### 02:44:37 · Speaker 2

Hmm

### 02:44:39 · Speaker 1

So when does our class end?

### 02:44:41 · Speaker 1

is it a twelve or a twelve

### 02:44:43 · Speaker 1

2015

### 02:44:47 · Speaker 3

like official. 1215. 1215 official.

### 02:44:47 · Speaker 1

Okay

### 02:44:47 · Speaker 1

Thank you

### 02:44:49 · Speaker 2

Sir

### 02:44:50 · Speaker 3

So can I continue for ten fifteen more

### 02:44:52 · Speaker 9

minutes

### 02:44:59 · Speaker 9

Okay. uh because no this actually is a nice time to stop. Yeah, no, we have topic wise I'm saying. We have come to the end of this.

### 02:45:14 · Speaker 2

Okay. So let's come to machine learning.

### 02:45:26 · Speaker 2

for now let's do supervised machine learning.

### 02:45:34 · Speaker 2

Okay

### 02:45:38 · Speaker 2

Okay, so what do we have? Suppose

### 02:45:42 · Speaker 2

we have

### 02:45:46 · Speaker 2

thousand images

### 02:45:53 · Speaker 2

with labels.

### 02:45:58 · Speaker 2

of this can be like

### 02:46:00 · Speaker 9

let's say these are general labels

### 02:46:02 · Speaker 9

This can be any labels, identity labels, anything, okay? Now, this is what we have, this we understand. Now, everything that we do from now on has to be seen in the, seen from the perspective of the distribution functions and random variables and all that. What, how do we see this? So, let us represent this as a set D, okay?

### 02:46:29 · Speaker 3

I will I will come I will introduce the labels

### 02:46:34 · Speaker 3

afterwards. So let this is text one.

### 02:46:39 · Speaker 2

X2

### 02:46:41 · Speaker 2

three

### 02:46:43 · Speaker 3

x 1000

### 02:46:46 · Speaker 3

Phir

### 02:46:48 · Speaker 3

Now each image, let's write it down here.

### 02:46:55 · Speaker 3

each image image is

### 02:46:59 · Speaker 3

is

### 02:47:00 · Speaker 9

what do you want? 2200 into 300 dimensional.

### 02:47:07 · Speaker 9

how many? sixty four zero sixty thousand pixels, okay? This means that

### 02:47:13 · Speaker 3

Every X I is in R

### 02:47:22 · Speaker 2

Any confusion on this? Any question on this?

### 02:47:36 · Speaker 2

Any question on this? This is, this notation is clear?

### 02:47:39 · Speaker 9

We have thousand images, all of them are in sixty thousand dimension. How do we see that, you know? So now from our language, right? Each X I is

### 02:47:51 · Speaker 3

an element

### 02:47:56 · Speaker 3

from

### 02:47:57 · Speaker 3

range space

### 02:48:04 · Speaker 3

of a random variable X.

### 02:48:09 · Speaker 3

you understand what's happening?

### 02:48:12 · Speaker 9

So what is happening is the underlying random experiment, right, the random trial has been conducted thousand times, okay? And there is an underlying random variable that has taken those outcomes and mapped it to some sixty thousand dimensional space using this random variable.

### 02:48:33 · Speaker 9

Is this clear?

### 02:48:35 · Speaker 2

this implies that there exists

### 02:48:43 · Speaker 2

an underlying

### 02:48:49 · Speaker 2

probability measure

### 02:48:53 · Speaker 2

and thus

### 02:48:56 · Speaker 2

distribution function.

### 02:49:08 · Speaker 2

Do you agree?

### 02:49:10 · Speaker 2

there exists an underlying probability measure and therefore a distribution function induced by X.

### 02:49:15 · Speaker 9

Correct

### 02:49:19 · Speaker 9

So that is represented as this, right? I mean you say that this is a data that is sampled from. This notation, this tilde says sampled from.

### 02:49:33 · Speaker 9

Okay, what do you mean by sampled from? There is a there is an underlying random trial that is happening and there exists a random variable and that random variable gives rise to some induced measure. These are elements from the range space of random variable. That is what this notation means, being sampled from. Sampled from

### 02:49:54 · Speaker 9

distribution. This is what we this is how we write.

### 02:50:00 · Speaker 9

to get the notation. So this is a starting point for machine learning. When we have data, we say that data has been sampled from

### 02:50:11 · Speaker 9

distribution

### 02:50:14 · Speaker 9

Okay, sampled from

### 02:50:17 · Speaker 9

a distribution not

### 02:50:19 · Speaker 3

a distribution because we have specified that. Sampled from

### 02:50:25 · Speaker 3

de-distribution

### 02:50:29 · Speaker 3

P X. This is the data.

### 02:50:35 · Speaker 9

data transferred from the distribution to X. Okay. uh What does that mean? That means that you understand the entire story, right? Now, that there exists an underlying probability measure and there was a sample space, there is a random experiment happening, there is a random variable that mapped that those outcomes to some real numbers, which is sixty thousand dimensional real numbers. And what we see are the elements from the range space of it and because there there was a probability measure, there exists a distribution function. Yeah, that's what we are we have

### 02:51:08 · Speaker 9

is clear?

### 02:51:11 · Speaker 9

I just wanted to give you this world view, right? I mean, had you knew this then I would have not spent those three hours. So this is the world view that I want you to have. Please ask me questions if if you need clarifications at this point. Yeah, in regimes

### 02:51:27 · Speaker 0

Yeah, just trying to get how did you get sixty thousand on R?

### 02:51:31 · Speaker 0

dimensions

### 02:51:32 · Speaker 9

Ha, see every image, right? You have image of sixty-thousand dimensional vector now, right? I mean two hundred pixels horizontally, three hundred pixels vertically. So this is one real number, second real number, third real number, fourth. I have just tagged them as columns and made it a long vector of sixty-thousand dimension.

### 02:51:49 · Speaker 0

Okay okay I read that as thirty C instead of

### 02:51:53 · Speaker 9

Huh?

### 02:51:55 · Speaker 0

I didn't read three hundred, it was looking like thirty C. Yeah, yeah, it's clear.

### 02:52:04 · Speaker 0

Yes, sorry for confusing you. It's clear now.

### 02:52:06 · Speaker 9

Yeah. See if it's word embedding no then it is some seven eighty six seven seven hundred twelve dimensional vector it doesn't matter depends on what your data is. Abhirup.

### 02:52:20 · Speaker 6

Yeah. So I have a question. So regarding the you said that the these x one, x two, x three, these are the these belong to the range space of the random variable function. And there is a probability distribution.

### 02:52:35 · Speaker 9

Ready

### 02:52:37 · Speaker 9

And by the way I I I I I like your term random variable function. That's that's what it is okay. Yeah but nobody calls it unfortunately a random variable function but that's what it is. Yes go on please. Yeah.

### 02:52:53 · Speaker 6

Yeah, so, uh, so the probability distribution function which is induced by X, that probability distribution function and the probability distribution function of actually the outcomes, how are these two are related? I mean, are they equivalent?

### 02:53:01 · Speaker 9

problem

### 02:53:09 · Speaker 9

No, no, no, hold on again. What do you mean by probability distribution function of outcomes? That's not a well-defined term.

### 02:53:18 · Speaker 9

probability measures are defined on over outcomes.

### 02:53:23 · Speaker 9

not distribution functions.

### 02:53:23 · Speaker 3

Distribution

### 02:53:25 · Speaker 3

Okay

### 02:53:26 · Speaker 9

Are you asking how is the probability measure related to distribution function?

### 02:53:29 · Speaker 3

Yeah, yeah. Yeah, yeah.

### 02:53:30 · Speaker 9

yeah

### 02:53:31 · Speaker 9

That's by definition. Now we have defined that here.

### 02:53:35 · Speaker 9

that green thing. This is how they are related.

### 02:53:41 · Speaker 6

okay okay okay then my question is that

### 02:53:43 · Speaker 9

This is how they are related, no? Yeah.

### 02:53:45 · Speaker 6

Yeah, then my question is that how are these two probability measures they are related? I mean how are they related? They are

### 02:53:51 · Speaker 9

There are no two probability measures. There is only one probability measure, there is a distribution function.

### 02:53:58 · Speaker 9

where are two probability measures here? There's only one probability measure, no?

### 02:54:03 · Speaker 6

there is a

### 02:54:04 · Speaker 9

there is a

### 02:54:05 · Speaker 6

No, in just somewhere in the in the top you mentioned like, you know, that we have a outcomes and we have a set of events and we have a random variable which maps them to certain real numbers and we have a Borel sigma algebra and a probability measure.

### 02:54:06 · Speaker 9

Yeah

### 02:54:18 · Speaker 9

Hello

### 02:54:22 · Speaker 9

we have

### 02:54:26 · Speaker 6

Yeah, not probably

### 02:54:26 · Speaker 9

not probability it's not probability measure it is an induced measure induced measure is called distribution function

### 02:54:32 · Speaker 6

ओके ओके

### 02:54:34 · Speaker 9

induced major itself is called distribution function.

### 02:54:38 · Speaker 6

Okay, okay. So, so P one

### 02:54:40 · Speaker 9

There are no two measures, there is only one measure. Two measures will come into picture only if you have two random variables. If you have a single random variable you only have one.

### 02:54:49 · Speaker 6

Okay

### 02:54:49 · Speaker 9

measure and one distribution function.

### 02:54:50 · Speaker 6

Perfect

### 02:54:52 · Speaker 6

सो, आई आई एम नॉट इवन श्योर वेदर माय क्वेश्चन इज करेक्ट और नॉट। इफ इट इज रॉन्ग देन प्लीज करेक्ट मी। देन हाउ आर पी वन एंड पी एक्स दे आर रिलेटेड?

### 02:55:00 · Speaker 6

in this in this equation.

### 02:55:01 · Speaker 9

This is this is when you have two random variables, okay? Are you talking about multiple random variables or a single random variable?

### 02:55:05 · Speaker 6

people that variables are

### 02:55:08 · Speaker 6

single random variable, the equations which you are just flushing.

### 02:55:12 · Speaker 6

Right

### 02:55:13 · Speaker 9

which one's, which one's?

### 02:55:16 · Speaker 6

the place where you have written the induced thing like the X

### 02:55:20 · Speaker 3

x over the arrow

### 02:55:25 · Speaker 3

you just went past it.

### 02:55:27 · Speaker 3

this one, this one.

### 02:55:30 · Speaker 3

Yeah

### 02:55:32 · Speaker 2

Here

### 02:55:34 · Speaker 9

Square

### 02:55:35 · Speaker 6

not exactly. He just went past it. Okay, maybe I can just... Yeah, yeah, yeah. Omega one, F one, P one.

### 02:55:40 · Speaker 9

K.L.A.S.

### 02:55:42 · Speaker 9

Here there are two random variables, no?

### 02:55:46 · Speaker 6

Yeah, but on the left hand side you have written omega one, F one, P one. And there is an arrow where X is a random variable and this R real numbers, R means set of real numbers, B is the Borel signal algebra and P X.

### 02:55:54 · Speaker 9

Correct

### 02:55:57 · Speaker 9

news

### 02:55:59 · Speaker 9

Correct

### 02:56:01 · Speaker 6

So how

### 02:56:01 · Speaker 9

is the induced measure under that random variable f. It is one that is one distribution function. The induced measure itself is a distribution function.

### 02:56:10 · Speaker 6

ओके, ओके

### 02:56:12 · Speaker 9

And another random variable induces another distribution function and there is another underlying measure.

### 02:56:18 · Speaker 6

Okay

### 02:56:19 · Speaker 6

Supreme Court

### 02:56:19 · Speaker 9

Every random variable has a measure

### 02:56:24 · Speaker 3

ओके ओके

### 02:56:25 · Speaker 9

measure P one get induced to distribution function P X. measure P two gets induced to distribution function P Y.

### 02:56:29 · Speaker 3

Okay

### 02:56:34 · Speaker 3

ओके, ओके, ओके.

### 02:56:38 · Speaker 9

Okay

### 02:56:39 · Speaker 3

Okay, yeah, yeah.

### 02:56:40 · Speaker 9

But here right when we are talking about data there is only one measure that we are talking about and there is only one distribution function.

### 02:56:49 · Speaker 3

Yeah

### 02:56:52 · Speaker 9

Is it okay?

### 02:56:53 · Speaker 6

Yeah, it's okay.

### 02:56:56 · Speaker 9

any other question on this?

### 02:56:58 · Speaker 0

Yeah, and sir, you are considering black and white picture because otherwise it would be multiplied.

### 02:57:02 · Speaker 9

Now why

### 02:57:04 · Speaker 0

I recall they said

### 02:57:07 · Speaker 9

every pixel is a real number, no?

### 02:57:14 · Speaker 0

you are multiplying two hundred point

### 02:57:15 · Speaker 9

what you are saying is what you are saying is there should be another three channel image here not two hundred cross three hundred cross three.

### 02:57:23 · Speaker 0

Yeah, right.

### 02:57:25 · Speaker 9

If it's three then you multiply this with three, you know, that's all. It is like one lakh eighteen thousand dimensional, that's all. Yeah.

### 02:57:32 · Speaker 0

Okay, okay.

### 02:57:34 · Speaker 9

For now I'm for a sake of ease no it doesn't matter I mean you should understand that the data dimension doesn't matter. Because it can be anything it can be a picture it can be some thirty dimensional speech vector it can be some bird embedding it doesn't matter what it is.

### 02:57:50 · Speaker 9

Get it? This is only an example. So in general, right? In general, if I want to generalize this idea, I have to just say that

### 02:57:52 · Speaker 3

Okay

### 02:58:00 · Speaker 9

All data is in some D dimensional space, that's all.

### 02:58:05 · Speaker 0

Okay

### 02:58:07 · Speaker 9

Right? So if it's an image then it is sixteen thousand dimensional, if it's a bird if it's bird embedding it's seven thousand dimensional or whatever.

### 02:58:15 · Speaker 0

Okay

### 02:58:15 · Speaker 9

Okay

### 02:58:18 · Speaker 9

Yeah

### 02:58:20 · Speaker 3

Your friends

### 02:58:21 · Speaker 2

ओके, एनी अदर क्वेश्चन्स?

### 02:58:30 · Speaker 3

Okay. Now suppose take another example another scenario where suppose we have images same thing we have thousand images.

### 02:58:44 · Speaker 3

with labels.

### 02:58:46 · Speaker 9

will take MNIST itself. Now sixty thousand examples with

### 02:58:51 · Speaker 9

fifty thousand examples. MNIST has fifty training data has fifty thousand examples.

### 02:58:58 · Speaker 9

ten thousand images with labels. These labels are

### 02:59:04 · Speaker 9

ten labels, no? zero to nine.

### 02:59:08 · Speaker 9

zero to nine. You have ten labels. Okay. Now how does the data are represented? Data is represented like this. Every point is a tuple like this x one comma y one.

### 02:59:21 · Speaker 9

x2, y2

### 02:59:24 · Speaker 9

Yeah

### 02:59:24 · Speaker 3

X fifty thousand

### 02:59:28 · Speaker 3

going fifteen thousand

### 02:59:33 · Speaker 3

Okay

### 02:59:34 · Speaker 9

Now how do we how do we use our world view on this? Is that you say that this is sampled from

### 02:59:41 · Speaker 9

underline joint distribution between two random variables x y.

### 02:59:46 · Speaker 9

because x represents the random variable. So basically we are saying there are two sample spaces, right? There is

### 02:59:55 · Speaker 9

x. thirty x.

### 02:59:58 · Speaker 9

the image space and maps it

### 03:00:00 · Speaker 1

So

### 03:00:00 · Speaker 1

fifty thousand no what is the dimensionality of image let's say that each image each image is in seven eighty four dimensional because emnist is a twenty eight by twenty eight image okay so now this maps it to seven eighty four dimensions this is one random variable there is another random variable so y i is a discrete random variable that can take values it is like rolling a die okay now this is there's another random variable y that takes another sample space omega two and maps it to

### 03:00:37 · Speaker 1

discrete

### 03:00:37 · Speaker 0

Right

### 03:00:38 · Speaker 1

Done

### 03:00:39 · Speaker 1

note that a random variable need not map in the range space of the random variable need not be continuous no it can be discrete as well. Now there are two random variables here and the data is now modeled as coming from the cross products of these two right I mean you take a picture and you associate you sample one one I mean you you take a random trial from this sample space you get a picture and you make a random trial from and then you take a pair of them that is your data point

### 03:01:13 · Speaker 1

And because there exists

### 03:01:16 · Speaker 1

probabilities on the intersections and unions of these two sets, you can define joint distributions on it.

### 03:01:25 · Speaker 1

Do you get it?

### 03:01:27 · Speaker 1

Now in this is this is supervised this is typically called supervised machine learning. Okay.

### 03:01:32 · Speaker 2

where

### 03:01:36 · Speaker 2

you have two random variables.

### 03:01:42 · Speaker 1

and two sample spaces and two probability measures basically, right? It is called supervised machine learning because you have one random variable corresponding to data, the other other random variable is typically called as the label. Okay? Now the data has been sampled from joint distribution of Excel.

### 03:02:01 · Speaker 2

Is this clear?

### 03:02:07 · Speaker 2

and

### 03:02:08 · Speaker 1

whatever I defined here, no this is unsupervised machine learning where you have one only one probability measures. In in in supervised machine learning you will have two probability measures, one is one is called the data, the other measures for the labels.

### 03:02:28 · Speaker 2

So this we will write maybe.

### 03:02:31 · Speaker 2

this is

### 03:02:34 · Speaker 2

is a setting for unsupervised learning.

### 03:02:41 · Speaker 2

this is I think for super

### 03:02:44 · Speaker 1

So what changes you see that we have we are sampling from P X here. Right? There's one quality distribution function. And here we are sampling from the joint distribution of those two because there are two random variables. See now we actually think about that if you think about that what was our problem our problem was that we don't know how pixels are related to these notion of digits right? So the way we model it is that okay two random experiments are happening one

### 03:03:14 · Speaker 1

somebody is writing that digit on like paper and take being picture is being taken and all that okay. There's one random variable that is basically converting all that into a real number. So once this is done this is being now associated with one of these nine digits notion of digits. That is another random experiment so both of them have uncertainty right. Now but you have joint distribution which means that now every image right has a certain uncertainty or a probability. of belonging to one of these nine classes

### 03:03:48 · Speaker 1

You see that now. See, initially I said that this probability theory will give you a tool to handle uncertainty that incorporates uncertainty in construction itself. Now you see why. Okay. Now we don't talk about functions from y to x. See, in deterministic case, we were talking about functions that deterministically map elements of y to elements of x. Now we are not talking about it. We are talking about distributions. Okay, joint distributions between these two sets. Which means

### 03:04:18 · Speaker 1

that given every element in y or rather every element in x there is a certain probability associated with that belonging to one of these nine classes

### 03:04:29 · Speaker 1

nine labels. Do you nine elements from other set. Do you see that? I mean I will concretize these ideas in next class, okay? But I want you to appreciate, right? I mean the whole branch of this probability theory was was was conceived because you start with a random experiment, right? And you have this notion of probability associated with events. Now you deal with everything, you model everything in terms of those random events and and distribution functions, right? And you have that notion of uncertainty by constraint. Lakshat

### 03:05:01 · Speaker 1

Is this clear? I'll continue from this in the next class while I'll take questions. I'll continue from this in the next class. I'll concretize these ideas. But yeah, you should understand how to represent data. Now data is represented as samples drawn from, this is actually called, you know, samples drawn from a distribution. People also call this as data sampled from a distribution or samples.

### 03:05:25 · Speaker 1

drawn from an interlock distribution, okay? These are common words that are used.

### 03:05:32 · Speaker 1

whenever you see that they are drawn from a distribution you you should know the entire story. What's happening is that there is a random experiment. You get sample space. You get event spaces. There is a random variable that is mapping this to real numbers and there is a probability measure assigned to uh the elements of sample space or rather elements of event space and therefore a distribution function gets induced.

### 03:05:57 · Speaker 1

Right? So when you say that the data is sampled from a distribution, this is what it means.

### 03:06:05 · Speaker 1

Okay

### 03:06:07 · Speaker 2

Yeah, Prasanna

### 03:06:14 · Speaker 2

Prasanna Bhatt won

### 03:06:17 · Speaker 0

Can you hear me, sir?

### 03:06:20 · Speaker 1

Yes, I can hear you.

### 03:06:21 · Speaker 0

Yeah, so in the last slide, I think you explained about X and Y random variable function. So, what is the relation between omega one and omega two here?

### 03:06:32 · Speaker 0

the domain

### 03:06:33 · Speaker 1

Yeah, they are they are they are two sets basically, right? I mean there is no relation per se.

### 03:06:42 · Speaker 0

But whatever the

### 03:06:43 · Speaker 1

But you can you can conceive you can talk of intersensions and unions between those two elements that's all

### 03:06:53 · Speaker 1

Right? Those two are the two sample spaces. I mean those who are samples those two are sample spaces that would that would encompass the outcomes of these two random experiments. But these two random experiments are not independent, right? quote unquote independent in the sense that they are connected through.

### 03:07:11 · Speaker 0

through the images that you have taken like you will assign the number. So basically like omega one

### 03:07:17 · Speaker 1

No, you sample an image, you sample an image, you sample a number, associate them using unions and intersections.

### 03:07:25 · Speaker 0

Okay okay

### 03:07:32 · Speaker 1

या राघवेंद्र

### 03:07:35 · Speaker 3

Sir, do we know this P X or P X Y in this case?

### 03:07:38 · Speaker 1

No, we don't. That's the whole problem in machine learning. The machine learning is if I have to summarize machine learning in one sentence, it is this. Given the estimate P X, that's all. That is machine learning.

### 03:07:54 · Speaker 1

See, Chat GPT also does that only.

### 03:07:55 · Speaker 3

तो वी आर

### 03:07:57 · Speaker 1

We will see multiple techniques to estimate P X given D. Yes.

### 03:07:57 · Speaker 3

multiple techniques

### 03:08:02 · Speaker 3

PX aur PXY aur

### 03:08:04 · Speaker 1

depends no in in unsupervised learning you estimate P X Y P X. In supervised machine learning you estimate P X. In fact in supervised machine learning you estimate P Y given X. I'll tell you next time. You estimate the condition of distribution. Given X.

### 03:08:16 · Speaker 3

P. Y.

### 03:08:17 · Speaker 3

Given X. Okay.

### 03:08:19 · Speaker 1

I'll tell you in the next class. That is actually the probability of gender given image.

### 03:08:21 · Speaker 3

exactly because

### 03:08:25 · Speaker 3

Okay, because these are sampled from those distributions, we say that, uh, this they are kind of representative of the, uh, the the actual distribution.

### 03:08:37 · Speaker 1

No, they are actually sampled from the underlying distribution, no? They are they are completely sampled from the underlying distribution, okay?

### 03:08:45 · Speaker 3

Okay, okay.

### 03:08:46 · Speaker 1

Uh but the problem is the the one big problem with the statistics is right. If when you are given samples from a distribution how do you estimate the underlying distribution is the biggest problem in statistics.

### 03:09:00 · Speaker 1

giving samples from a distribution is not enough to estimate the estimate completely the underlying distribution.

### 03:09:08 · Speaker 1

That is why no it is machine learning is heavily depend on the number of data points. The more the number of data points that we have from the distribution the better our estimation will be. We will see all that in the next class that is what I will do in the next class.

### 03:09:23 · Speaker 1

Okay, that's because of

### 03:09:23 · Speaker 3

Okay, that's because of either noise or maybe some something that we have not observed.

### 03:09:26 · Speaker 1

something that we have not observed. No, no, no, no. Don't call it noise or anything, okay? Something called last class numbers. I will describe all that in the next class.

### 03:09:36 · Speaker 3

ओके, या, थैंक यू सर।

### 03:09:37 · Speaker 1

So basically, the take away from this class is that when you have data, you should start representing data, right? As as samples from range space of elements from the range space of the random variable. And when you when we say that there is a distribution associated with it, you should know that it is the induced probability measure that is coming from coming through the random variable. That is the biggest take home.

### 03:10:05 · Speaker 1

Okay

### 03:10:09 · Speaker 1

Is it clear?

### 03:10:11 · Speaker 1

Okay, let's stop here but you know I have a couple of questions for you people. Let us maybe stop the recording.

### 03:10:23 · Speaker 1

Yeah, people can leave, right?
