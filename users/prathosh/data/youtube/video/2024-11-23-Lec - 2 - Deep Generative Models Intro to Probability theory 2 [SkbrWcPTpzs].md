---
id: SkbrWcPTpzs
title: Lec - 2 - Deep Generative Models Intro to Probability theory 2
url: https://www.youtube.com/watch?v=SkbrWcPTpzs
date: '2024-11-23'
duration: 03:16:30
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# Lec - 2 - Deep Generative Models Intro to Probability theory 2

## Transcript

### 00:01:59 · Speaker 1

Shall we begin

### 00:02:06 · Speaker 1

okay so good morning all of you um start uh i hope you had a chance to brush up some of the fundamentals uh of what we discussed the last time i will just quickly recap and then take it from there so what we did the last time was uh said that uh most problems in sense engineering happens to be approximating functions right

### 00:02:36 · Speaker 1

Um

### 00:02:39 · Speaker 1

So we we cast the problem of function approximation as that when you are given pair-stuff elements which are of the form x i comma y i

### 00:02:53 · Speaker 1

where xi comes from the domain of the function and yi comes from the range of the function uh the task is to find the uh underlying function that is there okay so some examples also right uh where the underlying function happens to be simple functions like linear and quadratic functions so why do we need to do function approximation that is because uh one of the major reasons is that function approximation enables prediction

### 00:03:23 · Speaker 1

right so if you know what the relationship between the uh the domain basically elements of two sets called the domain and range if you are given a new uh element in the from the domain set you can predict or estimate what is the corresponding element in the range set right so that is why uh function approximation is uh important and necessary okay so the problem was that what is the mapping between

### 00:03:53 · Speaker 1

the sets cannot be found using the known mathematical tools mostly the solution is that you come up with new mathematical tools so given this pretext context probability theory was introduced so basically we need that because the relationship between the given sets are rather complex do not adhere to the existing mathematical frameworks saw some examples of it right where

### 00:04:23 · Speaker 1

where the elements of the domain happen to be coming from like rp comma q where it corresponds to every element in the rp cross q space corresponds to a picture okay and what you need is the range space comes from one of the two values like these are called genders so relationship between the picture values and the idea of genders cannot be modelled using existing

### 00:04:53 · Speaker 1

mathematical tools and that was one example and we saw some textual example where you have a document and document gets mapped to an abstract idea called emotion and similarly speech signal to phoneme or words and all that right so first the idea means it is non-measurable in the sense that they are abstract okay and you can't measure emotion you can't measure gender you can only give labels associated with it but

### 00:05:23 · Speaker 1

domain can be measured okay uh as i said even to solve these problems historically people attempted to solve these problems using classical mathematical tools and give you examples of

### 00:05:37 · Speaker 1

yeah speech and images where speech signal was being modeled from a linear system or nonlinear system perspective where you have the signal and you model the uh the signal the output as uh concatenation of several linear systems or wave guides and you estimate the parameters of it similarly with image processing where you uh and you wanted to analyze an image and uh that analyzing an image was uh

### 00:06:07 · Speaker 1

conceived in a in a hierarchical manner where you detect edges and you know you compose objects from edges and

### 00:06:18 · Speaker 1

primitive shapes and then you try to make sense of what it is okay but these methods mostly did not yield human level performance okay because this constructing the functions that would map speech signal to phonemes or pixel values to complex object relations are not trivial

### 00:06:44 · Speaker 1

So then came probability theory. I mean, it was actually not that, you know, historically speaking, statistics and probability theory was around. Okay. But the, the application of probability theory as a mathematical tool to solve these kinds of problems was not that popular. uh before let's say 19 late 1980s okay the probability theory probabilities probabilistic tools were not the go-to tools to solve these kinds of problems but yeah so people realized that

### 00:07:14 · Speaker 1

Using classical function approximations may not be the best thing to do while you want to solve these kinds of block graphs

### 00:07:26 · Speaker 1

so with this context right we were looking at what probability theory was so uh okay so maybe i i pause for a while here any questions so far which is all some historical context any questions here

### 00:07:43 · Speaker 1

Okay, let's continue. So we introduced standard introducing problem theory. So what is it basically? It's it allows uncertainty by construction. Okay.

### 00:07:54 · Speaker 1

uh what is what does that mean that the functions that we are talking about which are mappings from the domain and range can possess quote unquote uncertainty we want to quantify what uncertainty is uncertainties are so uncertainties what do what does it allow uh the the user to is that it makes function learning feasible okay because we saw that uh function learning was in in feasible in so in in so many cases and uh it sort of helps creativity because

### 00:08:24 · Speaker 1

There's uncertainty. If there is uncertainty, I'll give you an example of an artist, right? The artist does not know a priori what sort of art is being created and that's why creative or a new stuff gets generated out of it. Okay.

### 00:08:42 · Speaker 1

we could try to concretize some of these ideas that uh yeah uh probability theory starts from this this this fundamental concept called a random experiment or a random trial so as i said in the whole of probability theory this is one thing that has not been mathematically defined right what is a random experiment or a trial just said that it is it is a process that gives rise to a set of outcomes that's

### 00:09:12 · Speaker 1

Okay, so anything that that gives rise to certain outcomes is called a random experiment or a trial. So collection of all the outcomes of all outcomes are the observations or outputs of a random experiment are enumerated in a discrete set and that set is called a sample space. Okay, need not be discrete set, can be a real space as well. Let's not do that.

### 00:09:42 · Speaker 1

just say that the set of all outcomes are enumerated in a in a in a in a set and that's called a sample space so examples of random experiment is that you toss a coin and the sample space comprises of a red tile and you roll an interface die then the sample space comprises of n phases of the die and we also saw some practical examples right where taking a picture of a person can be looked into as a random experiment where the sample space happened to be

### 00:10:12 · Speaker 1

different people right every time we get different people recording the speech signal happens to be a sample space and so on

### 00:10:24 · Speaker 1

okay so uh this was the uh sample space and we are not i mean it's not enough if we only have sample space right because remember that finally our intent is to mark a picture to agenda of these kinds of ideas for that what we needed was something called a measure okay it defined a measure so what is what what is the measure so given a particular set take a subset of a set and for each subset you associate

### 00:10:54 · Speaker 1

a scalar right or a non-negative number such that it has some properties and the properties are the following that you take any subset of any one set the measure has to be non-negative non-zero and if you take the null set the measure has to be zero and if you take the measure of union of two sets such that the intersection of them is null then the sets have to add up so we also saw an example of a famous measure that all of us know

### 00:11:24 · Speaker 1

of which is the level measure which is the length and the area measure in length area and volume measure in r1 r2 r3 etc similarly uh one can define a measure on sample space right you have collection of all possible outcomes of a random experiment is what is called an sample space like if f denotes the set of subsets of all possible subsets of omega then a measure uh which is also called the probability measure is defined on the subset of the the

### 00:11:54 · Speaker 1

sample space okay probability measure is a measure that is bounded upper and lower bounded between 0 and 1 okay it can be interpreted as the uncertainty associated with a subset of the sample space the subset of sample space is also called an event okay so probability measure is just like the Lebesgue measure gives you the sense of length okay of a subset of a real number sorry I'm sorry

### 00:12:24 · Speaker 1

So it gives the notion of a length of a subset of a real of the real the set of reals. Probability measure can be interpreted right as some measure that is that is giving you the sense of uncertainty associated with certainty or certainty like uncertainty associated with a particular subset of the sample space. Yeah, this is what I've said. No length or areas on RR2 is similar to probability on

### 00:12:54 · Speaker 1

Okay, so this was okay now we have the the probability triplet

### 00:13:06 · Speaker 1

Which is this generally called the

### 00:13:20 · Speaker 1

the probability triplet that is a sample space

### 00:13:25 · Speaker 1

the subset which is the event space and the probability measure okay this is typically the probability triplet

### 00:13:37 · Speaker 1

i mean again you can compare this with the when every time you define a measure you get something like this a triplet like this in r now you have r you have subsets of r which are also called the borel sigma algebra and you have the length or the lebague measure right similarly you have a probability triplet that is omega and the subsets of omega and probability measure okay now okay uh there is another problem wait remember that our goal is always to

### 00:14:07 · Speaker 1

uh learn that association between the pictures and uh abstract concepts like gender or whatever okay uh to do that we need something more okay there is a measure no okay we can measure uh we associated a measure with the outcomes of

### 00:14:27 · Speaker 1

random experiment but that's not enough because elements of sample space are not observed in practice okay what do I mean by that what do I mean by that is that if the random experiment is taken as observing a particular person okay and taking a picture we don't get to see that person or rather we don't yeah we don't get to see that person which are the elements of sample space

### 00:14:57 · Speaker 1

But what do we get? What we get to see is

### 00:15:03 · Speaker 1

an observation rather some measurement okay that we do on the elements of sample space so this has to be appreciated because otherwise right i mean this this notion of random variables will will not be uh appreciated better let me repeat what i'm saying see while uh the elements of random experiments are are enlisted in a sample space in practice

### 00:15:33 · Speaker 1

we don't get to observe the elements of sample space now why is that in the example of the pictures that i said okay uh when the random experiment is that you are you know you you pick a person take a picture right and a picture an abstract object picture is something which is an element of sample space you don't get to observe that what do you get to observe is a surrogate to that particular picture

### 00:16:03 · Speaker 1

Okay, so now we need to somehow define one other concept okay that would map the elements of sample space to something that we observe so that we can work with them.

### 00:16:18 · Speaker 1

is this idea clear i mean this is a this is a central idea right because we never go to sample space while we are working in in machine learning we only work on uh the observations or rather the instantiations of what are called as random variables okay uh why is that why is that is because when we when we do a measurement right using some sensors or something what we observe are some surrogates of the elements of sample space but not the elements of sample space at all okay now

### 00:16:48 · Speaker 1

do you model that mathematically is the question uh we model that using a function uh that is mapped from the elements of sample space to rd okay d is an arbitrary number uh depending upon what sort of uh application or data that we have uh d gets fixed the example the in the example that we saw if the sample sample space happens to be uh people or pictures of a person

### 00:17:18 · Speaker 1

then this function okay this function will take every picture or every person and maps it to a real number okay in pq dimensional space what is this pq uh we envisage this as a picture grid of pq pixels right where every element in p p q uh grid happens to be a real number so every picture happens to be

### 00:17:50 · Speaker 1

real number uh in a p q dimensional space so now this function takes a picture right or takes and takes a person and maps it to a real number in our p q dimensional space and which is what we observe okay uh yeah i will take the questions in a while uh please keep that hand raised of course virtually otherwise the time will start paining um okay uh in the second example uh this

### 00:18:20 · Speaker 1

space has a head tail okay and the function maps the head tail to let's say zero one two numbers

### 00:18:30 · Speaker 1

Okay, so this is here is a function the function takes elements of sample space and maps it to some d-dimensional real numbers Okay, and this function is what is famously called as a random variable and as I said it's a misnomer in the sense that this it is actually a deterministic function that takes elements of sample space and maps it back to Maps it to some real numbers a d-dimensional real numbers

### 00:19:01 · Speaker 1

Okay, now the data that we are given, the data that we are given, okay, what is that? They are actually the members or elements from the range space of a random variable. What do I mean by that? When we, let's say that, you know, we have, we are working with MS data set or some imagined data set. What we get are elements from this RPQ dimensional space, right? We get multiple vectors of dimension RPQ.

### 00:19:31 · Speaker 1

you what are those they should be conceived or seen as elements okay coming from the range space of this function called random variable

### 00:19:43 · Speaker 1

Okay, because the elements from the sample space are not observed. Okay, what is happening is you should imagine that, okay, there was a sample space, some random experiment was happening and there is this function which is called a random variable that has mapped the elements of sample space to the set of real numbers. What I am seeing are the set of these real numbers which are nothing but the elements from the range

### 00:20:13 · Speaker 1

space of the random variable which is a function and you should imagine that there exists an underlying sample space uh which would tell you what was the random experiment that that was being conducted okay so this is uh till that till this we had seen the last class so now we will continue from here yeah so any questions here uh please raise your hands i'll call out names

### 00:20:38 · Speaker 1

Right

### 00:20:48 · Speaker 1

Yeah somebody tell me ha this is the one I want

### 00:20:58 · Speaker 1

I want a new page how do I get a new page here

### 00:21:01 · Speaker 3

Sir you can unselect this and on the bottom there is a new page button page plus page in that column only

### 00:21:13 · Speaker 3

Can you open that once again

### 00:21:17 · Speaker 1

Yes

### 00:21:18 · Speaker 3

On the bottom there is a

### 00:21:18 · Speaker 1

Here we are got it got it so here

### 00:21:25 · Speaker 1

Next one

### 00:21:29 · Speaker 1

What was the naming convention this was L2

### 00:21:55 · Speaker 1

Okay so

### 00:22:02 · Speaker 1

just to distinguish it from

### 00:22:10 · Speaker 1

Where was that thing which uh

### 00:22:23 · Speaker 1

We had the sample space

### 00:22:27 · Speaker 1

the set of subsets and a probabilistic measure

### 00:22:32 · Speaker 1

Not this

### 00:22:38 · Speaker 1

For that yeah

### 00:22:42 · Speaker 1

Suppose this function called the random variable that took elements of sample space mapped into some t-dimensional real numbers. Okay, this is where we are. Okay, questions? Yeah, Prasad Gupta.

### 00:22:59 · Speaker 4

Hi Sir good morning

### 00:23:01 · Speaker 1

One yeah

### 00:23:01 · Speaker 4

So, sir, I just want to analyze a little bit more on the concept of random variable in the context of our problem of taking a picture and understanding whether it's what gender it is. So, in that concept, as you said, the picture that we clicked is a set is a member of the right hand side of the random variable definition, that is the RD side.

### 00:23:25 · Speaker 1

I encourage you to use mathematically correct terms don't call it the right hand side of random variable call it the range space of range space of random variables

### 00:23:37 · Speaker 4

I'll be right there

### 00:23:39 · Speaker 4

Yeah train space all right yeah

### 00:23:42 · Speaker 1

So every picture, every piece, every point in data that you get is an element of the rate space of random variable.

### 00:23:50 · Speaker 4

um now um i i want to imagine a scenario so like it's possible right that we take multiple pictures of the same person where he is standing in different poses so how does the idea of random variable handle that like so there is one element of sample space that is being mapped to different ranges uh different elements in the range set correct

### 00:24:13 · Speaker 1

No, see yeah a function cannot map one element to multiple elements no one to many mapping is not a valid function at all

### 00:24:13 · Speaker 4

That makes sense

### 00:24:23 · Speaker 1

Okay, so that does not become a valid function. So it cannot map the picture of one person to multiple coronal numbers. But why, I mean, that's a good question, right? I mean, that's actually a good question. Let me answer that. See, in that case, the way you should imagine is that the sample space itself has pictures of that person standing in multiple angles.

### 00:24:51 · Speaker 1

While while I conceived I mean the example that I gave why I I understand why that question is uh question right in the the way I I I I gave you the example of sample spaces I I said that uh uh every person corresponds to one object in the sample space right it may not be the case right I mean if you are taking I mean that is in the case where you take one picture of a person if you are taking multiple pictures of a person then all those pictures becomes elements of the sample space

### 00:25:21 · Speaker 1

And that variable will map it to different real numbers for different angles.

### 00:25:28 · Speaker 1

A function by definition cannot have one to many mapping

### 00:25:32 · Speaker 4

Got it. So we are still not at the place. So sample space has all the possible poses, everything related to every person on this planet, but we are still a little away from our final goal where we then analyze the sample space and all the possible poses and find out, okay, these are all actually the same person.

### 00:25:38 · Speaker 1

Yeah

### 00:25:40 · Speaker 1

That's what we need to do

### 00:25:51 · Speaker 1

See that way we will do. See we have I I I have not set up the the next problem yet. I'm just telling you what the sample space is and what random variable does right.

### 00:25:56 · Speaker 4

That's the new

### 00:26:00 · Speaker 4

Now

### 00:26:01 · Speaker 1

Now, that's why, I mean, actually you brought up a nice point. See, I hope that all of you got the question. The question was that in the example that you gave, there was one person and like taking the picture of one person was one element in the sample space.

### 00:26:21 · Speaker 1

Then if you take multiple pictures of that same person, how do you handle it? Now, the answer to that is that see, you conceive what is there in the sample space. Meaning the user would define what the sample space is because the random experiment is something that is a user defined idea, you see? But what I wanted to tell you is that when you have like, let's say multiple elements from R, D, R, P, Q, R, O, S, Q, which are, which are,

### 00:26:51 · Speaker 1

are images right or the set of pixels you have to imagine that this is the result of this process where there was a sample space and there is a function which is a random variable that has mapped the elements of the sample space to this rd

### 00:27:08 · Speaker 1

Okay, there exists some sample space, some underlying sample space, and you constructed sample space accordingly, right? I mean, it doesn't matter how you construct it. And the good thing is that you don't have to even worry about the sample space once you get the outcomes of, I mean, once you look at the range space of random variables, that's enough. That is why you define the random variable in the first place, okay?

### 00:27:34 · Speaker 4

Ah, okay. So the way I understand this, what you said triggered another thought that ultimately what we want to understand is the gender, right? Even if the same person repeats again and again, the gender stays the same. So it's irrelevant for the problem. Is that how I should know?

### 00:27:49 · Speaker 1

No, no, I say don't worry about that's what I said. Don't worry about the gender part yet. Okay. Just, just think, just think about having a few data points. Yeah. Which are pictures. Now, how do you see those data points is something that we are looking at right now. How do you look at the labels is something that we'll come to in a while. Okay. For now, just imagine that you have a set of data points.

### 00:28:16 · Speaker 1

Okay, these data points are seen as the elements of the range space of a random variable. And the moment you talk of a random variable, there exists an underlying sample space, which is giving you some elements. That is how you should look at it. Okay.

### 00:28:31 · Speaker 4

Sure sir so we're only talking about representatives right now got it

### 00:28:33 · Speaker 1

No no the data data I mean data yeah sorry

### 00:28:35 · Speaker 4

Data yeah sorry like uh not

### 00:28:37 · Speaker 1

uh not labels i will i come to the labels in a way see for instance right in in generative modeling you don't have labels right you only have data let's look at the representation of data now uh from a random variable perspective then we will come to the the labels in a way okay any other questions on this this is very important right i mean this understanding is very important because from this is the last class when i'll be talking about the sample space from like next class on onwards we'll only talk about

### 00:29:07 · Speaker 1

variables and distribution functions so you have to understand like thoroughly what is going on so if you have questions so this is the opportunity for you to ask them

### 00:28:44 · Speaker 4

You will be happy

### 00:28:54 · Speaker 4

I need it

### 00:29:18 · Speaker 1

Any other questions

### 00:29:25 · Speaker 1

But we may

### 00:29:25 · Speaker 2

Some so maybe the uh the trick is in designing the I mean coming up with the correct probability measure

### 00:29:34 · Speaker 1

Yeah yeah yeah see um probability measure is I mean I didn't get your question I mean that that was a sort of assertion right what is the question

### 00:29:34 · Speaker 2

Oh yeah

### 00:29:47 · Speaker 2

Okay, so in one sense I understand that this is still only talking about understanding the basic data points but when we move on to the next step when we start try to assign labels then probably we have to worry about a probability measure. We have to model that part.

### 00:30:12 · Speaker 1

Um hold on I was like as I said no please try to if you have questions on things that I've said already do ask and let's not jump I'll I'll come to that I'll come to all that in a while yeah

### 00:30:26 · Speaker 1

Any questions on things that we did so far?

### 00:30:38 · Speaker 4

Hello sir can I ask one question

### 00:30:40 · Speaker 1

Just a second uh and yes I think all

### 00:30:44 · Speaker 4

So, sir, I was asking like this random variable function is like very important. We are converting this sample space into some range space. So, as per our problem like different

### 00:30:56 · Speaker 1

No no converting no no hold on hold on converting sample space into real numbers

### 00:31:02 · Speaker 4

Yes

### 00:31:03 · Speaker 1

Don't call it range space, real numbers. See what is range? When you have a function, you have a domain and the range. So random variable is a function that takes sample space and maps it to real numbers.

### 00:31:17 · Speaker 4

So for a given sample space there we can define multiple ways or we can define multiple functions this random variable function right based on the work

### 00:31:27 · Speaker 1

over very good very good observation yes you can and that is why no that is a model that's basically what a model is so ultimately we will see that entire machine learning is about uh finding this underlying probability measure okay why does the probability measure change the probability measure changes because uh i mean when the probability measures changes the random variable changes right you can actually you can yeah so you can there may not be one random variable cross

### 00:31:57 · Speaker 1

responding to a random uh sorry uh a particular sample space there can exist multiple random variables yeah

### 00:32:04 · Speaker 1

But what is important is that the the moment you have some data you should imagine that there has already been a random variable that has been applied to it. You understand?

### 00:32:18 · Speaker 2

No

### 00:32:20 · Speaker 4

Like data is in its raw form like like images or speech

### 00:32:24 · Speaker 1

Now you have data the moment you have data the moment you have data you should all you should know that there has been some random variable that has been operated on the sample space

### 00:32:38 · Speaker 1

In practice yeah

### 00:32:38 · Speaker 2

But it will be expensive

### 00:32:42 · Speaker 1

You're right

### 00:32:46 · Speaker 1

Okay

### 00:33:02 · Speaker 1

Okay uh yeah I think Bridge Cooper has a question I think yeah

### 00:33:06 · Speaker 4

Uh yeah sorry so just a small one it's a little different uh so uh the way you said right uh for a for a simple experiment like tossing a coin um we usually immediately associate a rand a random variable with the uh possible outcomes like zero and one we assign to head and tails right

### 00:33:28 · Speaker 4

Why uh like uh so I'm assuming the reason we choose zero and one is that something to do with the probability measure and uh like uh like why did we choose zero and one is my question why can't we have one far better

### 00:33:38 · Speaker 1

That's arbitrary that's arbitrary you can choose anything you can choose anything

### 00:33:39 · Speaker 4

It that's it

### 00:33:42 · Speaker 4

Okay, okay, okay. So that is not affected by our pro uh probability uh measure and our us wanting to keep it between zero and one.

### 00:33:50 · Speaker 1

It has nothing to do no no no oh that has nothing to do with the measure it's the the range of the random variable is arbitrary you can choose it to be anything in fact it becomes a function of your sensor and all that no your quantizer your sensor when you take a picture what values do you see in the picture becomes a function of what does the what does the bit representation of your machine what is the machine precision what is the quantization that you are doing and so on isn't it

### 00:34:19 · Speaker 4

Okay so maybe I'm merging two concepts okay thank you

### 00:34:22 · Speaker 1

So it has nothing to do with measure okay

### 00:34:27 · Speaker 1

Okay, next one. Now, the question is.

### 00:34:34 · Speaker 1

Once you have, okay, we understood what happens to the elements of omega under the random variable. Okay. So now we understand why it is such a misnomer, right? Keep calling it random variable, but you should imagine a function that's there. Right? Yeah, it's the biggest misnomer that I've ever seen. It's not a random variable, it's a function. Okay. Now, yeah, so we saw what happens to the elements of sample space under

### 00:35:04 · Speaker 1

random variable they get converted into real numbers right the next question that we should ask is what happens to probability measure there is this probability measure right once you operate a a random variable data function on the sample space what happens to probability measure is the question you can always imagine this right so now

### 00:35:27 · Speaker 1

Once

### 00:35:34 · Speaker 1

omega that belongs to omega i mean the w or w belongs to omega right and if you take that w and that is mapped to some real number let's say

### 00:35:47 · Speaker 1

Okay, now what is x of omega, x of omega, right, is a real number. I'm assuming that you have a one-dimensional random variable in a while, okay. We'll define that notion for n-dimensional random variables after a while. Let's say that you have a one-dimensional random variable. If you take an element, a w belonging to omega, belonging to omega, you will get a real number. Okay, that's what this random variable does.

### 00:36:17 · Speaker 1

No

### 00:36:28 · Speaker 1

It's a push

### 00:36:32 · Speaker 1

Opposed

### 00:36:35 · Speaker 1

What do we call that

### 00:36:39 · Speaker 1

often run out of uh alphabet

### 00:36:44 · Speaker 1

Suppose a small r is a subset of real numbers

### 00:36:51 · Speaker 1

Okay examples can be

### 00:36:55 · Speaker 1

So minus 2 and 3 right and like minus infinity to 2 and so on right all these are subsets of real numbers

### 00:37:06 · Speaker 1

X inverse of R

### 00:37:10 · Speaker 1

What can you say about this

### 00:37:13 · Speaker 1

Let me repeat the question. We have a random variable which is a function that would take elements of sample space and maps it back maps it to real numbers. Now what I do is I take a subset of real numbers.

### 00:37:28 · Speaker 1

You understand? I take a subset of real numbers. Okay. And look at the inverse image. So this is the

### 00:37:41 · Speaker 1

In love with image

### 00:37:46 · Speaker 1

under the function x

### 00:37:54 · Speaker 1

So the inverse image of a subset of R under the function X, what do you get from doing this?

### 00:38:04 · Speaker 2

Subset of omega

### 00:38:07 · Speaker 1

Exactly

### 00:38:07 · Speaker 4

Exactly

### 00:38:09 · Speaker 1

Yeah you get a subset of omega from here can all of you see this there

### 00:38:14 · Speaker 1

will be some set okay which belongs to F which is a subset of omega

### 00:38:27 · Speaker 1

all of you see this is very important please let me know if you see this

### 00:38:36 · Speaker 1

questions on this I'm saying suppose you take a subset from the real numbers real real numbers a subset of real numbers and look at its inverse image under this function then you will get a subset of

### 00:38:53 · Speaker 1

Is it clear

### 00:39:00 · Speaker 1

See when I ask you a question if it's clear to respond otherwise

### 00:39:05 · Speaker 2

Here a is x inverse i is that the result

### 00:39:09 · Speaker 1

come again

### 00:39:10 · Speaker 2

I'll be using a to represent x inverse of the range subset

### 00:39:14 · Speaker 1

Correct, correct, correct, correct. A is the X. But what is that A? I mean, what's more important is that that A is an element of F. F is the subset of omega.

### 00:39:33 · Speaker 1

Now this implies that this implies that we can talk of probability measures on

### 00:39:43 · Speaker 1

inverse of any subset of the real numbers okay this is well defined now

### 00:39:54 · Speaker 1

It is because it is equal to the probability measure defined on A which is a subset of F so this is very different. Do you see this?

### 00:40:08 · Speaker 1

So we can define probabilities on the inverse images of the subsets of real numbers taken under random variable. Let me write that.

### 00:40:22 · Speaker 1

Probability

### 00:40:27 · Speaker 1

Hold up

### 00:40:31 · Speaker 1

Inverse image

### 00:40:37 · Speaker 1

a subset of R

### 00:40:45 · Speaker 1

I'm done

### 00:40:47 · Speaker 1

function f

### 00:40:52 · Speaker 1

Very fine

### 00:40:56 · Speaker 1

See note that probability measure was a measure that was defined on the subsets of omega sample spaces. Now random variable maps the elements of that to real numbers. Now we come backwards. We take a subset of real numbers. Okay. And we look at the inverse image of that subset of real numbers, that subset of real numbers under this function called the random variable that will give you an element from the sample space or a subset from the sample space.

### 00:41:26 · Speaker 1

space and on that we have already defined a probability measure therefore the probability of the inverse image of a subset of a real numbers under the function called random variable is well defined

### 00:41:40 · Speaker 1

Did all of you get this? I'll take questions in a while but yeah

### 00:41:46 · Speaker 1

Okay one by one Harish

### 00:41:49 · Speaker 2

So is it correct to say that uh these elements of A are the samples which are just sampled from this whole sample space or are the ones which were just observed?

### 00:41:58 · Speaker 1

Element of which is a subset. A is a subset. A is a subset. See, you remember this, no? There was an omega, f and p. What was this f? f was set of subsets of omega, right?

### 00:42:12 · Speaker 1

And on the elements of F is where we defined probability model, which I will write that also here, is that. So P is a function that is defined on A, okay, that would take an element A, okay, which is a subset of F and maps it to the number between 0 and 1.

### 00:42:36 · Speaker 1

This is the measure that we defined no

### 00:42:40 · Speaker 1

So F is set up

### 00:42:45 · Speaker 1

That's your total we got

### 00:42:52 · Speaker 1

Right. So, we define the probability measure on the elements of f, which are the subsets of omega. Okay. Now, we are saying that the inverse image of the of any subset of r under the random variable will take us back to a and on a probability measure certain. Therefore, we can talk of the probability of inverse image of some subset of real number under the inverse of random variable that is well defined.

### 00:43:23 · Speaker 1

Tarmish

### 00:43:26 · Speaker 2

Yes so since f is a set of subsets of omega so a should be a member of f right not a subset of f because anyways all the subsets are there in f

### 00:43:38 · Speaker 1

Thank you for that

### 00:43:42 · Speaker 1

Some mistakes

### 00:43:48 · Speaker 1

My mistake that was a that was a good point thank you for telling that

### 00:43:58 · Speaker 1

Yeah, I actually meant that, but I wrote subset. Yeah, so that's my mistake. Sorry. Thanks. Avirup. Did all you get the mistake that I had done? I mean, that's A is not a subset of F. A is an element of F. Yeah, because, okay, yeah. Avirup.

### 00:44:16 · Speaker 2

Yeah, so when you say the inverse image, so are you referring to some notion called inverse function?

### 00:44:24 · Speaker 1

Of course right absolutely absolutely

### 00:44:28 · Speaker 2

No

### 00:44:28 · Speaker 1

Because x is a function right x is a function uh when the a function always always have an inverse right that would take an element from the range of the function and maps it back to the domain

### 00:44:40 · Speaker 2

Okay, now in that case, inverse function is also a function. A function by definition should always have many to one or one to one mappings. But in this case, we are having multiple elements from the domain and we are mapping them to a set, which is a...

### 00:44:57 · Speaker 1

No no no see when you take when you define the random variable right you can make it a bijective function so that the inverse exists

### 00:45:06 · Speaker 1

Yeah so you take every element from the sample space and map it to a unique real number

### 00:45:12 · Speaker 1

So then it becomes invertible right it's a bijective function that can be inverted

### 00:45:18 · Speaker 2

Is it always possible to come up with a random variable which we

### 00:45:20 · Speaker 1

Of course why not because a random variable is something that we are defining no you always make it by definition

### 00:45:29 · Speaker 1

So that's why the inverse exists

### 00:45:35 · Speaker 1

So basically what I'm saying is this function random variable always maps a unique element from the sample space to a unique element in real numbers that's all

### 00:45:45 · Speaker 2

Okay okay

### 00:45:46 · Speaker 1

Yeah, see in fact even if it's not a bijective right only surjection is enough for inversion but you can make it bijective nobody stops you yeah

### 00:45:56 · Speaker 1

Because you know functions like f of x squared, sorry f of x equal to x squared, even those have inverses. So but now for I mean for ease of understanding let us assume that our random variables are all objective functions, okay?

### 00:46:11 · Speaker 1

Yes uh signed

### 00:46:14 · Speaker 3

Sir, as per my understanding, we have random variables map the individual outcomes in the sample space to a real number, right?

### 00:46:27 · Speaker 1

Correct correct

### 00:46:28 · Speaker 3

Now in the example we have taken, we are saying that we have taken a range minus 2 comma 3 or minus infinity comma 2 and that we are mapping to a subset.

### 00:46:43 · Speaker 3

So I agree that this subset A, this can be individual elements, but I'm not able to digest that this subset can have multiple elements of the sample space.

### 00:46:57 · Speaker 1

It can no because uh it depends on the way your function is defined isn't it

### 00:47:05 · Speaker 1

See it's like this I tell you

### 00:47:05 · Speaker 3

You

### 00:47:08 · Speaker 1

Uh suppose there's a function right let's say f of x is equal to

### 00:47:15 · Speaker 1

of x is equal to say x plus 3 then what is the mapping 0 to 3 and then you have 1 to 4 2 to 5 and so on isn't it

### 00:47:29 · Speaker 1

Okay now suppose I take a set which is let's say four to eight

### 00:47:36 · Speaker 1

Can't I define this

### 00:47:43 · Speaker 3

Okay so it this will give us a range of x

### 00:47:46 · Speaker 1

Isn't it exactly no it's a new subset of the domain

### 00:47:50 · Speaker 3

Okay. Okay, sir, makes sense.

### 00:47:53 · Speaker 1

Yeah, that is why the inverse image of a subset of R will give you an element from F not an element from omega.

### 00:48:03 · Speaker 3

no that that that's what the confusion like that's what i said

### 00:48:03 · Speaker 1

It's a matter of

### 00:48:06 · Speaker 1

But do you understand no no what I'm actually talking about

### 00:48:10 · Speaker 3

Huh

### 00:48:10 · Speaker 1

Use an element from F because we are talking about subsets in the range space of the random variable that gets mapped to subsets in omega that's all yeah

### 00:48:20 · Speaker 3

Okay if if our domain is only the subset then anyways it will give give us

### 00:48:25 · Speaker 1

No no no uh what do you mean by domain is subset I didn't mean domain is a set

### 00:48:28 · Speaker 3

It might be

### 00:48:31 · Speaker 1

Domain is a set but what you are saying is if I consider subsets in R and take the inverse image I get subsets in omega

### 00:48:41 · Speaker 1

But if I take a singleton here, I mean, if this set has one element, I perhaps I get back one element there, right? I note that a set here, right? A subset of R here might map back to null set also. That's also possible. Yeah, but that's also a subset of R. See, F also contains null, no?

### 00:48:54 · Speaker 3

It's also possible

### 00:49:02 · Speaker 1

All the possible subsets of omega and null is also a member of f therefore the inverse image that's why in fact probability measure is defined on null set also the probability of a null set is 0

### 00:49:02 · Speaker 3

All the possible subsets of all the possible

### 00:49:17 · Speaker 1

Yeah, so that's why it's well defined. You can take a subset in the range. So basically what I'm saying is that you can take a subset in the range space of random variable and the inverse image of that will map back to an element in F. That's all, no?

### 00:49:31 · Speaker 3

Okay okay and that element it can be a singleton or uh it can be null

### 00:49:36 · Speaker 1

It doesn't matter it can be null yeah it can be that is why I'm saying it's simply a member of F that's all

### 00:49:38 · Speaker 3

It can be an easy

### 00:49:45 · Speaker 2

have to be an element in F but not uh say a subset of sample space

### 00:49:51 · Speaker 1

Same thing no subset of subset space is what we have denoted as uh f all possible subsets

### 00:49:56 · Speaker 2

It has to be an element in F right

### 00:50:00 · Speaker 1

Of course also for instance if I

### 00:50:00 · Speaker 2

So but

### 00:50:01 · Speaker 3

F is a set of subsets

### 00:50:04 · Speaker 1

If I increase the

### 00:50:04 · Speaker 2

I increase the range so now you have put minus 2 to 3 and now I change it to say minus 2 to 5 so now does it have to belong to only one element in F

### 00:50:14 · Speaker 1

It'll it'll get to a different it will map back to a different element in F no

### 00:50:18 · Speaker 2

an element in F not a subset of subspace

### 00:50:22 · Speaker 1

Okay subset of subset of subset of subsets of sample spaces is what we have called as F. F is nothing but set of subsets of sample space.

### 00:50:33 · Speaker 1

What is there Okay

### 00:50:34 · Speaker 2

Okay so it cannot map to multiple elements in uh F is is my question

### 00:50:39 · Speaker 1

It cannot mat of course right

### 00:50:42 · Speaker 1

Of course, right, if you take a unique set in the unique subset in the rate space of any function, the inverse image will map to a unique subset in the domain of the function, right, if the function is bijective.

### 00:50:59 · Speaker 1

Simple I mean see this is like I mean your uh uh you know high school function I don't know when did you study functions was it in high school I studied it in class 11

### 00:51:10 · Speaker 1

Whatever you people I don't know yeah are we different generations perhaps no

### 00:51:16 · Speaker 1

you mean most of you may be like like between 20 and 30 I suppose right most of you yeah I have crossed 30 so maybe I'm of I'm often every every decade is a different generation you see so every decade they change the syllabus and all that so I studied functions in when did I study functions it was in class 11 when do the teacher teach teach them these days high school

### 00:51:43 · Speaker 1

Did did anybody study functions in high school

### 00:51:48 · Speaker 4

Yes at 11 o'clock

### 00:51:48 · Speaker 2

Yes sir

### 00:51:50 · Speaker 1

lemon yeah leavened is not high school no yeah it depends i mean you know what what curriculum are you a part of i was i was in the state board right where this leavened was called college for some reason it was called pre-university college anyway okay so i'm saying it's just fundamental stuff right you have you have two sets we are talking about inverse images the one thing that we introduce new perhaps is that this is the idea of measure okay okay so clear so far

### 00:52:19 · Speaker 1

Okay now

### 00:52:23 · Speaker 1

Consider

### 00:52:32 · Speaker 1

consider

### 00:52:35 · Speaker 1

subsets of R

### 00:52:40 · Speaker 1

Of D

### 00:52:42 · Speaker 1

Following form

### 00:52:48 · Speaker 1

Let's say R1 is a subset of R that is equal to minus infinity to

### 00:52:58 · Speaker 1

Odd one

### 00:53:00 · Speaker 1

Again overloading locations here, let's do this let's call this as s1 and this we will call as

### 00:53:15 · Speaker 1

you can call it Arman no problem and there's S2

### 00:53:25 · Speaker 1

Basically speaking it is not in close of this

### 00:53:35 · Speaker 1

So understand this notation right this set includes minus infinity does not include r1 it's upper bounded by r1 here this set includes minus infinity but

### 00:53:45 · Speaker 3

Or how can we include minus infinity

### 00:53:47 · Speaker 1

Why not it's an element in R no

### 00:53:50 · Speaker 3

It is but it is not defined right what like

### 00:53:52 · Speaker 1

No very much defined why not define it's an element in our

### 00:53:57 · Speaker 1

You can definitely include minus infinity, no problem with that. Okay. So let us consider these sorts of subsets of R. Now,

### 00:54:06 · Speaker 1

Uh yeah now X inverse of

### 00:54:12 · Speaker 1

one

### 00:54:16 · Speaker 1

is what is some element in our note let's let's call it as a1 which belongs to f okay right now the probability measure that is computed on the inverse of sets subsets

### 00:54:37 · Speaker 1

This particular type

### 00:54:42 · Speaker 1

ball

### 00:54:44 · Speaker 1

uh no this is for this this is for this we need one more bracket this okay this is building point right you understand what is this this is the probability measure that is computed on that is assigned to the element of f which is gotten by the inverse image of this set minus infinity to x under the random variable x

### 00:55:10 · Speaker 1

Okay, maybe not use X here, again it'll make life difficult. Let's call this as A.

### 00:55:19 · Speaker 1

Is this clear to all of you? This is a well-defined measure, no? The probability assigned to an element of, by the way, have I already said this? This is also called the event space, okay? F has a name. It's called the event space. So this is the probability measure assigned to the element of the event space that gets mapped to

### 00:55:49 · Speaker 1

gets mapped that that that gets mapped to a set minus infinity to a under x or rather it is a probability of the event or probability of the member of the event space obtained by taking the inverse image of this subset minus infinity to a under the random variable x do you understand the statement if you understand the statement that you have understood everything that i've said so far shall i repeat the statement okay let me write that term maybe it's better to write it this is

### 00:56:19 · Speaker 1

is the probability of

### 00:56:24 · Speaker 1

D

### 00:56:26 · Speaker 1

element

### 00:56:30 · Speaker 1

in the event space

### 00:56:36 · Speaker 1

The art is obtained

### 00:56:45 · Speaker 1

pain

### 00:56:47 · Speaker 1

By taking

### 00:56:51 · Speaker 1

the inverse image

### 00:56:58 · Speaker 1

of T set

### 00:57:02 · Speaker 1

minus infinity to a

### 00:57:09 · Speaker 1

Under

### 00:57:12 · Speaker 1

the random variable X. Is this clear? Any questions on this?

### 00:57:24 · Speaker 1

All of you, please ensure that every one of you understands this.

### 00:57:31 · Speaker 3

Uh Sir can you explain what is under the

### 00:57:35 · Speaker 1

I'm not familiar with it

### 00:57:35 · Speaker 3

And that's a good one.

### 00:57:37 · Speaker 1

X is a function no see when we talk of inverse images we have to test we have to we have to specify what function are we looking inverse images under

### 00:57:49 · Speaker 1

See when you take a subset and you talk of inverse images, what is the function under which you are taking the inverse image? It is a random variable which is a function, correct?

### 00:58:03 · Speaker 2

Is it, does it mean that let's say if we take S of some sample space, we'll reach out to a particular range. If you take inverse of that, whatever the sample space or the event space that we end up in, probability of that is what we are defining here.

### 00:58:19 · Speaker 1

Exactly, exactly. But we are looking at particular subset of real numbers. No, this particular subset. The kind of subset that we are looking at is like close minus infinity to open a.

### 00:58:35 · Speaker 1

Carter Kumar

### 00:58:37 · Speaker 2

Oh yes sir so that's it

### 00:58:40 · Speaker 4

Have I made a relation with

### 00:58:41 · Speaker 2

The

### 00:58:45 · Speaker 1

But why not make it bigger

### 00:58:45 · Speaker 2

So

### 00:58:48 · Speaker 1

Particular water is breaking

### 00:58:49 · Speaker 4

Sorry am I audible

### 00:58:50 · Speaker 1

I need to know

### 00:58:50 · Speaker 4

I need to know

### 00:58:53 · Speaker 1

Is it only for me

### 00:58:55 · Speaker 4

Uh

### 00:58:57 · Speaker 1

His voice is breaking

### 00:58:58 · Speaker 3

I'm not sure

### 00:58:59 · Speaker 2

You're just kidding

### 00:59:02 · Speaker 1

Is it still

### 00:59:02 · Speaker 2

Uh is it still breaking so

### 00:59:04 · Speaker 1

Yeah not now try try now

### 00:59:06 · Speaker 2

Yeah, I just wanted to ask, is A anyway related with R1 and R1 which we defined S1 with? Minus infinity to R1.

### 00:59:16 · Speaker 1

But well it takes in the sense that uh like uh this particular r1 is the is I mean this particular set is the one that maps back to a1 that's all other than that there is no relation per per set

### 00:59:31 · Speaker 2

Okay so yeah I mean like uh

### 00:59:33 · Speaker 1

If you take this particular subset and take the inverse image of this it will go back to EMIL that's all

### 00:59:39 · Speaker 2

Okay yeah sure thanks

### 00:59:42 · Speaker 1

Okay great so this we let's give a symbol for this let us

### 00:59:48 · Speaker 1

E this call this as px evaluated at a

### 00:59:54 · Speaker 1

This is a symbol. Okay. What is it saying is? I mean, I just represent this complicated looking thing using a simple symbol, right? I mean, this symbol actually means that I am looking at the inverse images, the probability of the inverse image of this particular type of subset minus infinity to a under the random variable. This is the symbol. Is this okay? I'm just using the symbol for this complicated thing. Is that okay?

### 01:00:26 · Speaker 1

Okay. It turns out that this has a name. This particular thing has a name, which all of you know. Do you know what the name of this is?

### 01:00:37 · Speaker 4

Really is

### 01:00:38 · Speaker 1

No, no, not PDF. This is the cumulative distribution function. Yeah, this is the distribution function.

### 01:00:40 · Speaker 3

People have to test it before

### 01:00:46 · Speaker 1

This is the distribution function of a random variable

### 01:00:53 · Speaker 1

Some people also call it the cumulative distribution function. I mean, I don't know why it is called cumulative. You don't have to call it cumulative, okay? But this is called the distribution function of a random variable. Is this clear? So what is it?

### 01:01:07 · Speaker 2

since it accumulates the distribution

### 01:01:09 · Speaker 1

from minus infinity to no no no no no no no no pre space there is there is no accumulation that's happening up see

### 01:01:10 · Speaker 4

No no no no no

### 01:01:20 · Speaker 1

The reason perhaps why people call it cumulative is because you define a density function and then you like you can represent the this this function as a running interval of that other function and that's why it's called cumulative but I I'm not a fan of this term cumulative I mean standard textbooks call it a distribution function and yeah this is a distribution function okay now what is a distribution function it's it's the probability of the element of event space that is obtained by taking

### 01:01:50 · Speaker 1

the inverse image of the set minus infinity to a under the random variable x so if you evaluate this distribution function at a value x or a it will remember that you are actually looking at the probability of an event probability of an element from the event space what is that element that element is the one that you have gotten by taking the inverse image of this set minus infinity to a under the random variable x

### 01:02:15 · Speaker 1

Is this clear

### 01:02:22 · Speaker 1

This is the single most important definition that we'll be looking at because the entire machine learning is estimating this particular function given elements from the range space of random variables. That is all the B generative models, discriminative models, classifiers, regressors, anything. The entire machine learning is about estimating these functions, the probability density functions, sorry, distribution functions.

### 01:02:48 · Speaker 1

Okay, so in fact, instead of calling it cumulative distribution functions, now let us call them the probability distribution functions, you know, that is

### 01:02:58 · Speaker 1

It's put on me

### 01:03:03 · Speaker 1

probability of the BLT distribution functions probability distribution function of A

### 01:03:16 · Speaker 1

Is this clear

### 01:03:23 · Speaker 1

Please remember that if you evaluate the distribution function at a particular point

### 01:03:31 · Speaker 1

Okay if you evaluate the distribution function at a particular point what are you actually doing

### 01:03:39 · Speaker 1

you evaluate the distribution function at a particular point you're actually getting a probability probability by definition is defined on the elements of f now evaluating distribution function at a particular point should give you right the probability of a particular element in f what is the element in f whose probability this function is giving you it is that element in f okay or rather that subset of the sample space which

### 01:04:09 · Speaker 1

Ease

### 01:04:11 · Speaker 1

getting map to minus infinity comma a under the random variable x

### 01:04:19 · Speaker 1

Is this clear

### 01:04:22 · Speaker 1

Please remember this because as I said this is the single most important demonition that we need for this course. So yeah. Questions on this? Sanket H.

### 01:04:36 · Speaker 2

The probability distribution function is usually the probability at a single point right

### 01:04:41 · Speaker 1

Definitely no no no definitely not I mean that is that is precise three and a half hours to define this it is not that

### 01:04:51 · Speaker 1

See point number one, I am I am not talking about probability density functions here. I am talking about the probability distribution functions.

### 01:04:52 · Speaker 2

Point them

### 01:04:59 · Speaker 2

Okay okay

### 01:05:00 · Speaker 1

Okay, and even probability density functions are not probabilities. Please remember that probability is a measure that is defined on elements of F period. You cannot talk of probability of X being equal to something. It just does not make sense. You understand?

### 01:05:19 · Speaker 1

Because by definition, by definition, probabilities are defined on elements of F. That's all. See, it's like, can you talk of length of, length of, okay, what do I say?

### 01:05:41 · Speaker 1

If I say length of water, length of water, right, or length of, length of speech or something, it's just not defined, right? Length is defined only on elements of subsets of R, isn't it? Similarly, probability is a measure that is defined only, only on subsets of omega. So whenever you talk of probability, you should always make sure that you are talking about the probability of an element of F.

### 01:06:11 · Speaker 1

That is why this distribution function while it is denoted as P x a okay this actually means this entire thing

### 01:06:21 · Speaker 1

Whenever I write PHCA in this course you should always remember that I'm talking about this

### 01:06:27 · Speaker 1

Okay, you should remember that there exists a function called random variable. Okay, and this random variable has an inverse image. The inverse image of, we are considering the inverse image of this particular set minus infinity to a. Now that gives you an element in the event space that has a probability associated with it and that is what this function is giving me. Always, okay?

### 01:06:54 · Speaker 1

This is clear because I want to make this damn clear to all of you because people very wrongly say that the probability of a random variable it's there is nothing called probability of a random variable

### 01:07:07 · Speaker 1

Okay, it does not make sense. You mean it's like, you know, saying round circle or something. There is no probability of random variable. There is probability of elements of f. So if you evaluate the distribution function of a random variable at a particular point, what you are actually doing is this entire thing.

### 01:07:25 · Speaker 1

Okay, please be clear about it Rajan

### 01:07:31 · Speaker 4

So sir my question is when we are taking the inverse of a subset of R then it might not be having any element in F right for example

### 01:07:40 · Speaker 1

It will always be, it will always be, it will always be. He can't.

### 01:07:45 · Speaker 4

Most of the time

### 01:07:47 · Speaker 1

How come

### 01:07:49 · Speaker 4

Yes, example tossing a coin will have outcome of head and tail. And suppose head is translated to 0 under random variable and tail to 1. Then if I take if I try to take the inverse of for example, 3 which

### 01:08:04 · Speaker 1

Then it then it maps back to null that's all and null is also an element of it

### 01:08:11 · Speaker 4

I got it in that case probability will be

### 01:08:14 · Speaker 1

Zero

### 01:08:17 · Speaker 4

Project Thanks

### 01:08:19 · Speaker 1

Actually mentioned this maybe you missed it no problem have a look

### 01:08:35 · Speaker 1

What's up

### 01:08:37 · Speaker 1

a little down we might come to that see please again i'm reiterating don't jump we will not leave anything in this course okay we will address all those questions okay but uh see when i when i ask people questions right do ask please ask me questions on things that we have discussed so far because otherwise right if you jump ahead uh then you know it will sort of break the flow please don't take it in a negative sense uh just to ensure that you know we are going systematically

### 01:09:07 · Speaker 1

we may mean that's a good question by the way how do we estimate px uh is the question that we ask in machine learning all machine learning is about estimating this distribution function okay so don't worry we'll come to that in the next next part of this class in the genes

### 01:09:25 · Speaker 2

Yeah when you say you are taking probability of inverse random variable minus infinity to a

### 01:09:30 · Speaker 1

Uh just a second please please please uh use correct terms there's no inverse random variable

### 01:09:39 · Speaker 1

So can you can you say it correctly

### 01:09:42 · Speaker 1

probability of

### 01:09:47 · Speaker 1

So uh just just I don't c say correctly

### 01:09:51 · Speaker 2

So inverse probability of a real number

### 01:09:54 · Speaker 1

No no no not the inverse probability see inverse is defined for a function

### 01:10:02 · Speaker 4

Yeah okay

### 01:10:04 · Speaker 1

The universe is defined for a function

### 01:10:07 · Speaker 1

inverse of the function called random variable

### 01:10:13 · Speaker 1

That is how we should say it

### 01:10:17 · Speaker 2

So when you are taking that set as minus infinity to a

### 01:10:20 · Speaker 4

Can I see any

### 01:10:21 · Speaker 2

Any other set say

### 01:10:22 · Speaker 4

They won't do it

### 01:10:24 · Speaker 1

I'm glad that you asked that question. I wanted somebody to ask this. It's a very good question. So why are we considering this particular set? What is the what's so what's so nice about this particular set is the question that you're asking, correct?

### 01:10:38 · Speaker 1

Yeah, I'll answer that next. That's the next thing that I'll do, but I'm glad that you asked that question. I'll answer that. I was expecting someone to answer that question. Ask me that question, right? Why it is so satisfactory about this particular set that we are assigning a function to it, right? I mean, rather like we are calling, we are giving it a particular name. What is so important about this? I'll answer that in a while. Okay. Okay.

### 01:11:08 · Speaker 1

Now, see, it's related to the other question that Indrajit asked. Okay, why, what is so, I mean, what, why, why is this particular set, right? That is the next question. Okay, we'll answer that question perhaps. Now it turns out, I'll just state that without the proof, maybe, yeah, I, okay. By the way, there is one other convention.

### 01:11:32 · Speaker 1

I can tell you that why

### 01:11:59 · Speaker 1

I think this question has to be answered

### 01:12:04 · Speaker 1

So the answer to this is it turns out

### 01:12:11 · Speaker 1

any substance in R

### 01:12:15 · Speaker 1

and being represented

### 01:12:38 · Speaker 1

Set operations

### 01:12:47 · Speaker 1

That's a form

### 01:12:56 · Speaker 1

So does okay so here is the convention okay

### 01:13:02 · Speaker 1

So from now on, whenever I state something, okay, without proof or without giving you a lot more details, I will mark them as tutorial items. Okay. Now I ask one of you, like, or maybe...

### 01:13:20 · Speaker 1

All of you two take a note of it okay and just put it in the teams as tutorial items and this has to be covered in the tutorial by TS. I will keep doing this from now on.

### 01:13:36 · Speaker 1

Okay, anyway, so the thing is, any subset in R can be represented by our set operations over these kinds of sets. That is the reason we are interested in this kind of set.

### 01:13:52 · Speaker 1

What does that mean? That means that suppose

### 01:14:02 · Speaker 1

if you take a set subset a b okay that is in r

### 01:14:11 · Speaker 1

This A B

### 01:14:16 · Speaker 1

Can't be done as well

### 01:14:49 · Speaker 1

Yeah this is a sub-sentence

### 01:14:53 · Speaker 1

is good

### 01:14:56 · Speaker 1

Sorry

### 01:14:56 · Speaker 3

We need to have square braces for a comma b set a comma b

### 01:15:02 · Speaker 1

Because that is uh those are included no Yeah I think what I had written earlier was correct

### 01:15:13 · Speaker 1

Here's one example. I think TS will do a proof for this. So basically what I'm saying is that if you can take any subset in R and that can be represented using the set operations on these kinds of things.

### 01:15:26 · Speaker 1

Okay, and we know that that you know probabilities measures probability measures will add up. So therefore, if you want to take prop if you want to look at the probabilities of let's say that you are interested in the probability of

### 01:15:50 · Speaker 1

um the inverse image

### 01:15:55 · Speaker 1

of this particular set

### 01:16:01 · Speaker 1

particular set this can be right obtained in terms of

### 01:16:08 · Speaker 1

The probability the distribution function that is evaluated at B subtract that with the distribution function that is evaluated at A. So again, the proof of that shall be done in the tutorials.

### 01:16:23 · Speaker 2

included in that interval right

### 01:16:25 · Speaker 1

B is not included in the interval is that so

### 01:16:30 · Speaker 1

Yeah because it's not included in the interval. A is included, B is included. So yeah, A is included, B is not included. I think this should be correct. Correct? This is what you're saying. B is not included in the interval.

### 01:16:30 · Speaker 4

Yeah because it's not included in the minus and minus

### 01:16:44 · Speaker 1

Yeah, so this is why we are interested in this particular set that if we want to look at the probability of the inverse image of any subset of R, okay, we can obtain that in terms of the probabilities of events that are associated with the inverse images of

### 01:17:06 · Speaker 1

this kind of subjects okay that is why we are interested in this particular type of subjects

### 01:17:13 · Speaker 1

Okay, does that answer your question? I think it does not ask this question. And why are you interested in this particular subset? It's because of this, that we can obtain the probabilities of inverse images of any of subset of R and B subsets.

### 01:17:27 · Speaker 1

Now what is this has a very big implication this implies this implies

### 01:17:33 · Speaker 1

the probability distribution function

### 01:17:43 · Speaker 1

Function completely

### 01:17:47 · Speaker 1

complete COOM PLATE ELOY completely specifies

### 01:18:00 · Speaker 1

underlying probability measure

### 01:18:14 · Speaker 1

So what I was saying is that if you know the distribution function then you know everything about the underlying probability interval.

### 01:18:26 · Speaker 1

Can I make that statement? So basically what happens now that you start from this is what you have, this is the probability triplet. You have the sample space, the event space and the probability measure. Now this, when I operate a function called random variable on top of this.

### 01:18:49 · Speaker 1

Then what happens is this will induce another measured space that is called an also pointy push forward measure. This will map omega to R and it will map F2

### 01:19:04 · Speaker 1

subsets of F, okay, which are subsets of R, which are also called the Borel sigma algebras. Don't worry about it, it's just a name given to specific subsets of R and the probability measure gets pushed forward into distribution function.

### 01:19:23 · Speaker 1

This is a big story

### 01:19:26 · Speaker 1

Okay, now the thing is in practice, no access to this, you know, we don't have access to this.

### 01:19:34 · Speaker 1

Okay, but this is accessible

### 01:19:43 · Speaker 1

The data that we get are actually the members of

### 01:19:48 · Speaker 1

This is odd

### 01:19:50 · Speaker 1

Okay, so now when we have like thousands of images, they're all members of this R. Okay, now because we have this, we always operate with R, B and PX. We don't even look at BR and PX. So now if we get PX, then we know everything about the underlying probability space. Okay, this is, by the way, this is also called the

### 01:20:16 · Speaker 1

the probability space or probability interpret

### 01:20:23 · Speaker 1

And this is called the

### 01:20:26 · Speaker 1

Push forward or induce space

### 01:20:29 · Speaker 1

It's actually a space that is induced by a function on the sample space which is called the random variable

### 01:20:35 · Speaker 1

forward are the induced space

### 01:20:42 · Speaker 1

So we simply work with this accessible and work with this

### 01:20:50 · Speaker 1

The work with distribution functions, right, and the elements of the range, the elements of the range space of random variable, that's our data. Okay, that is our data.

### 01:21:00 · Speaker 1

But you should always remember that whenever we talk of a random variable and a distribution function, you should always remember that this random variable is a function that has an underlying underlying probability space. OK, and the probabilities that we are talking about are on the elements of that f event space. OK, this is the clarity that you should have. So, in other words, if we know what the distribution function is, then we know everything about the underlying probability measure. And that is why entire machine learning is

### 01:21:30 · Speaker 1

as estimating the problem of estimating the probability distribution function given data i will write down on this right yeah so i just wanted to tell you that that uh that why is uh why are you working with random variables and what are random variables and what are distribution functions hope that you people are clear about this okay uh questions no sanchit

### 01:21:55 · Speaker 3

why are we taking the concept of Borel sigma algebra here

### 01:22:00 · Speaker 1

Because uh the when you have this random variable right that would take omega to r f right get pushed forward into Borel sigma algebra.

### 01:22:11 · Speaker 3

So like for Borel sigma sigma algebra what understanding I have is it will have all possible subsets of the form A comma B.

### 01:22:21 · Speaker 1

Correct, correct, true. That is why no f gets because you know those are the those are the elements those sets those subsets of r gets the map back to elements in f no that's why the push forward uh um push forwarding that happens from f

### 01:22:41 · Speaker 1

Why I write random variable is Boolean algebra

### 01:22:46 · Speaker 1

I'm not I'm not telling you that because as I said no you can mostly ignore this B because we are basically what I'm saying is when omega gets mapped to R what happens to F F gets mapped to Borel sigma algebra that's all

### 01:22:59 · Speaker 3

Then sir by default the probability measure should be a length measure right

### 01:23:04 · Speaker 1

No, no, no, yeah, not necessarily because probability measure is defined on the probability triplet, no. But, but, I mean, that's a good question that you ask. See, we can integrate distribution functions, right?

### 01:23:21 · Speaker 3

We can what

### 01:23:23 · Speaker 1

Integrate distribution functions we can differentiate distribution functions right

### 01:23:26 · Speaker 3

Correct correct

### 01:23:27 · Speaker 1

Operations of integration and differentiation are defined on Lebesgue measures

### 01:23:34 · Speaker 1

That is one of the reason yeah length measures no operations of integrations and differentiations are defined on the length measures Lebesgue measures

### 01:23:44 · Speaker 1

Now since that is one other reason why we need a random variable. See you cannot integrate in the the probability space because integration is in probability space is not defined at all.

### 01:23:57 · Speaker 1

Right. So once you get to the, uh, the, the, the, uh, the push forward or reduce space, you can do integration. That's why you can differentiate the distribution function and you get another function called the density function. Right. You can integrate the distribution function. You can do all those things. The, the, the default measure is not the length measure. The length measure is defined only on Borel sigma algebra. Okay. Under the random variable, right. Once you do the push forwarding, you get the, the Lebesgue measure. Before that,

### 01:24:27 · Speaker 1

It's the probability measure only

### 01:24:30 · Speaker 3

So once we have an induced probability space we have a Borel sigma algebra and correspondingly the Lebesgue or length measure

### 01:24:40 · Speaker 1

Correct, but we are not interested in the length measure on the Borel sets gotten from the push forward induced space. We are interested in the probability measure that is obtained by the inverse images on the subsets of R. Because we are interested in finding out the underlying probability measure, not the length measure of this Borel space.

### 01:24:59 · Speaker 3

Okay okay

### 01:25:01 · Speaker 1

Because the whole purpose is to model that picture and and map it to a gender or something right

### 01:25:08 · Speaker 1

We are not interested in the Lebesgue measure of this push forward space. We are interested in these kinds of induced measures, right, which are called the probability distribution functions. Yeah.

### 01:25:21 · Speaker 1

Okay, so rest of the people can ignore this discussion if it didn't make sense. Okay, so don't worry. I mean, that was like slightly off topic. Okay, the pian.

### 01:25:33 · Speaker 2

So this is in the space we have data so this probability PX that is calculated based on the data or it's available exclusive uh otherwise also

### 01:25:44 · Speaker 1

No it is not available no the whole problem of machine learning is to estimate the speeds we don't have the speeds with us

### 01:25:52 · Speaker 1

I will need to say that see what we have are the elements from the range space of random variable that's all that is our data

### 01:26:01 · Speaker 1

The X will be

### 01:26:01 · Speaker 4

The X will be

### 01:26:03 · Speaker 1

Whole problem going to be to estimate it

### 01:26:08 · Speaker 1

Entire machine learning is estimating PX, okay?

### 01:26:12 · Speaker 4

Got it sir

### 01:26:14 · Speaker 1

Well I will define that I will define that in a while uh yes Raghuvendra

### 01:26:19 · Speaker 4

Yes uh in general do we also know X always or

### 01:26:22 · Speaker 1

we will not know x we will only know we will only have elements from the range space of x we will not know x see when you have images right or do you have you have a lot of real numbers right each each image is a set of real numbers correct yes what is that that's actually the elements from the range space of random variable you don't know what the random variable is

### 01:26:47 · Speaker 1

I'm telling you again random variable is not a variable it's a function so please remember that

### 01:26:54 · Speaker 1

Okay um is this clear uh sentence has one more question yeah sentence

### 01:26:59 · Speaker 3

So basically, we have a probability triplet and in order to have an ease of operations, we are, you know, inducing the concept of random variables and not only

### 01:27:12 · Speaker 1

Not only not only that not only that right ease of operation is of course one because we can integrate and all that there is one other reason no the way i motivate it is you don't have access to omega fp

### 01:27:26 · Speaker 1

In in in real world what do you have access to you have access to real numbers you know how do you see real numbers as elements of omega no you can't there is something that is there is something that is

### 01:27:36 · Speaker 3

We just have the outcomes that are not

### 01:27:41 · Speaker 1

We don't even have yeah we don't even have the access to outcome we have access to some measurement of the outcome

### 01:27:49 · Speaker 3

Correct

### 01:27:50 · Speaker 1

And how do you quantify that using math that is quantified using a random variable no

### 01:27:54 · Speaker 3

Correct correct correct

### 01:27:56 · Speaker 1

So basically there is a function that is sitting on top of the outcomes, which is giving you the real numbers. That is what we have access to.

### 01:28:05 · Speaker 1

And now since we have measure defined the probability measure on the subsets of outcomes, we need an equivalence in the induced measure. That is your distribution function. That is your distribution function.

### 01:28:14 · Speaker 3

I mean that's a good question

### 01:28:18 · Speaker 3

Sort it sir

### 01:28:21 · Speaker 3

Got it, sir.

### 01:28:22 · Speaker 1

Yeah, but always remember this definition is very, very sacrosanct. I mean, this is, you should remember this. Whenever I talk, I mean, I will be talking of distribution functions all along the course. Okay. Whenever I talk of distribution function, you should remember this. You know, I suggest all of you go back today after today's class, sit down, maybe rewatch the lecture and try to get this idea solid into your mind. Okay. Very, very important.

### 01:28:49 · Speaker 1

lot of people hand wave on this and wrongly represent distribution function as probability of random variable that does not make sense at all so please get this get these ideas

### 01:29:04 · Speaker 1

Nicely into your mind okay uh in the teens

### 01:29:11 · Speaker 2

Here does it really matter whether we include A or B endpoints or exclude them

### 01:29:17 · Speaker 1

Here that

### 01:29:20 · Speaker 1

It depends no you can take any set here and as I said any set can be represented using these kinds of sets that's all you can take any set you can take the inclusive inclusive sets exclusive sets doesn't matter you can represent any set like this using these kinds of sets operations on these kinds of sets okay.

### 01:29:40 · Speaker 1

Okay great um okay bridge move one

### 01:29:46 · Speaker 4

Hi, sir. So let's say using machine learning, we have successfully approximated PX, which gives us basically the ability to tell how probable it is that we'll see a subset of event space A in real life, correct? Up to this point, am I understanding? So how does this understanding translate into us knowing about the actual underlying P of

### 01:30:16 · Speaker 4

So the the probability

### 01:30:18 · Speaker 1

So that is your p no that is p what is p p is the probability of a particular subset in f if you know that you know that that's all

### 01:30:29 · Speaker 1

See maybe you should ask a different question right why how will that be important or relevant in telling what is the gender of this particular person is right obtained from that image

### 01:30:43 · Speaker 1

That question I have not answered yet. I will answer that question. But if you estimate the probability distribution function, then you know everything about the underlying probability measure.

### 01:30:55 · Speaker 4

Okay, so just I'll say a statement. Please help me understand where I'm going wrong in this. So once we approximate Px, so I'm thinking of Px as a function that takes an input and generates an output. So the output that is generated is P, is a part of P?

### 01:31:19 · Speaker 1

do you mean by output i didn't get that see the probability distribution function is a function i agree right yeah whose uh like uh whose uh range is zero to one

### 01:31:33 · Speaker 1

Ah now what is the question

### 01:31:35 · Speaker 4

So uh from the definition of Px what we get is the likelihood of observing A

### 01:31:41 · Speaker 1

No I have like have I have I defined the term likelihood

### 01:31:45 · Speaker 4

Uh oh okay

### 01:31:45 · Speaker 1

Please don't use the term because all those are mathematically precisely well defined don't use the terms that are not defined

### 01:31:52 · Speaker 4

Okay so

### 01:31:52 · Speaker 1

If you evaluate the distribution function at a particular point it'll give you the probability of the inverse image that's all it is

### 01:32:02 · Speaker 1

No yeah that is the question yeah

### 01:32:04 · Speaker 4

So the probability of inverse image or to go with the notations probability of the output correct

### 01:32:12 · Speaker 1

So again there is nothing called probability of A. This is again this is a notation. When I evaluate the distribution function at A, what am I doing is I am looking at the probability of inverse image of this particular subset. That is all it is. There is nothing called probability of A. Please.

### 01:32:31 · Speaker 1

That is the you know misrepresentation that I want to take out of your minds. When you evaluate the distribution function at a point, okay, you are not getting the probability of that point. That does not even make sense.

### 01:32:44 · Speaker 4

Oh sorry I was not talking about small a I was talking about capital A the set

### 01:32:48 · Speaker 1

Oh, sorry, my bad. Yeah, it is the probability of A, correct? A1, I have said it as A1, no? Yeah.

### 01:32:53 · Speaker 4

Yeah, okay, A1. So now the probability of A1 is actually that underlying P, correct, that we were talking in that first triplet.

### 01:33:06 · Speaker 1

Yeah of course no P is a function. P is a function that will take an element of F and gives you a number between 0 and 1.

### 01:33:16 · Speaker 4

Got it so I might have to

### 01:33:17 · Speaker 1

I have my turn

### 01:33:18 · Speaker 4

Yeah, so am I underst uh am I correct in my understanding that the output of px on small a is actually something in the the p on the left hand side of this uh uh

### 01:33:32 · Speaker 1

That's correct. That's precisely correct. Yeah, if you evaluate the probability distribution function, right, at a particular point A, it will give you the same output that the probability measure, right, would have given on the subset A1. Correct. That is correct.

### 01:33:52 · Speaker 4

Okay yeah thank you so that's it

### 01:33:53 · Speaker 1

See that is why that is why that is why

### 01:33:58 · Speaker 1

That is why capital P, right, is a function that would take elements of F and map it to 0, 1, correct?

### 01:34:09 · Speaker 1

And probability distribution function okay will take an element of R and still maps it to 0 1

### 01:34:18 · Speaker 1

You notice that the range space of both of these are same

### 01:34:23 · Speaker 1

My definition my definition

### 01:34:27 · Speaker 4

Interesting yeah that clears it up thank you

### 01:34:29 · Speaker 1

Okay thanks

### 01:34:31 · Speaker 1

Okay anything else

### 01:34:35 · Speaker 1

So take home message is the following, right? When you take the distribution function and evaluate at a point, what does it give probability of the inverse image, right, of the event that is obtained by taking the inverse image of this particular set minus infinity to a under the random variable x. This is the take home message. Remember this. How do I...

### 01:35:00 · Speaker 1

I think this is something

### 01:35:06 · Speaker 1

Does it stay? Ah it stays hold on

### 01:35:13 · Speaker 1

It is the end

### 01:35:17 · Speaker 1

It's super duper important okay

### 01:35:23 · Speaker 1

Oh does red means that this is wrong or something when it's not used red or yellow is okay

### 01:35:33 · Speaker 1

We are

### 01:35:35 · Speaker 2

So if you change the if you change the paper colour then it will be more visible

### 01:35:43 · Speaker 1

From black to white

### 01:35:45 · Speaker 2

White or yellow

### 01:35:51 · Speaker 1

is fine yeah please remember this this is the this is the message that i'm supposed to give today okay

### 01:35:59 · Speaker 1

I'm mm

### 01:36:02 · Speaker 1

Okay, uh shall we break for 15 minutes

### 01:36:07 · Speaker 1

There is one other nice question that I was expecting nobody is asking me anticipated an answer

### 01:36:16 · Speaker 1

It is 10 45 in my clock let's get back at 11 p.m. okay let's solve 11 a.m. okay see you in 15 minutes

### 01:54:42 · Speaker 1

So begin continue

### 01:54:49 · Speaker 1

Tell me this show of hands please Is there anybody who has not studied a probability theory course in your undergrad?

### 01:55:04 · Speaker 1

Like no probability theory course at all. Is there anybody of anybody like that in the class?

### 01:55:14 · Speaker 1

When you raise your hands there is somebody like that

### 01:55:18 · Speaker 2

So can you repeat

### 01:55:21 · Speaker 1

So is there anybody who has not taken a probability theory course like ever in your life undergrad or something?

### 01:55:34 · Speaker 1

Okay, nobody good. See, the reason I asked is that, like, see, all of you know these things, maybe in different forms, right? Maybe not this rigorously or in different forms. I just am trying to give you a different perspective. That's all, right? So, yeah. So, you people are aware of these things, know that cumulative distribution functions, you have heard these terms and like you have worked with these, correct? Gaussian distributions and all this. Have you? Most of you have worked with these things.

### 01:56:04 · Speaker 1

with these things right i mean you are aware of these things earlier it's good so as i said no the first two three classes initial two three classes i think i i develop the language and give you perspectives of how i would like to see things and then from then onwards you can take off very quickly okay uh let's get back so now we are we have uh the probability triplet and we have a reduced space uh uh a distribution function associated with it now um

### 01:56:34 · Speaker 1

the Pandora box of probability theory now there's too many things that come up I'll just define a few things that are kind of

### 01:56:44 · Speaker 1

obviously needed for our our cost and then we'll move on see the first thing that i want to define talk about is

### 01:56:54 · Speaker 1

Vectors valued random variables

### 01:57:00 · Speaker 1

Again another misnomer, okay? So vector valued random variables. This is, these are random variables, right? That such that the range space of these, this function that we are talking about is R and D and not R, the vectors, okay?

### 01:57:19 · Speaker 1

Do you understand

### 01:57:22 · Speaker 1

So what is happening is the elements of sample space now gets mapped to d-dimensional real numbers, not one real number. All these while we were looking at like real numbers here, right? The mapping was to real numbers, okay? Now in a vector-valued case, which is our general case, right? When we have images or like embeddings of text and speech, et cetera, they are all some d-dimensional vectors. So these are like vector, they are called vector-valued non-dimensional variables because

### 01:57:52 · Speaker 1

The range space of the random variable that we have will be vectors, d dimensional vectors in general. Any questions on this?

### 01:58:00 · Speaker 1

great so in this case right when we

### 01:58:04 · Speaker 1

evaluate the distribution function right the distribution functions gets evaluated at a vector

### 01:58:14 · Speaker 1

a right now the argument for the distribution function will be a vector a i will not be using this uh like head bar after that but this is just for once okay so how do you define this now this is the probability

### 01:58:29 · Speaker 1

Probability okay, so let us take an example and do it perhaps easier that way to show.

### 01:58:37 · Speaker 1

So example suppose

### 01:58:44 · Speaker 1

Suppose the random variable is

### 01:58:50 · Speaker 1

dimensional okay maps the sample space to two dimensional real numbers okay now what happens to

### 01:59:00 · Speaker 1

the distribution function of this by the way any notation that I know this is the notation that I will be using when I write this subscript okay uh that that denotes the random variable okay and whatever is within the brackets is the value at which we are evaluating this so now how do how should I evaluate this x

### 01:59:22 · Speaker 1

What should I write inside the bracket now?

### 01:59:27 · Speaker 3

x inverse and within brackets the vector

### 01:59:30 · Speaker 1

No, no, no, I'm evaluating it at a point. The notation is that probability density distribution function is evaluated at a point. And what is this point? This point is now some vector A1 into, correct?

### 01:59:51 · Speaker 1

All of you with me on this

### 01:59:54 · Speaker 1

Because the random variable is a two-dimensional random variable, distribution function is evaluated at a vector. Now again, we'll interpret this. Now, what does this mean? This is the probability of what?

### 02:00:10 · Speaker 1

Again our own notation right it is the probability of the inverse image under x of what set are we considering here? Can somebody tell me what is this set?

### 02:00:31 · Speaker 1

Do you understand

### 02:00:31 · Speaker 4

You understand infinity to A one minus infinity to A two

### 02:00:35 · Speaker 1

Minus infinity two

### 02:00:37 · Speaker 4

A1 and minus infinity to A2

### 02:00:41 · Speaker 1

So what should I This is one set What should I write? I should write a bracket here

### 02:00:50 · Speaker 1

I'm trying to write

### 02:00:52 · Speaker 4

In fact this is an area sir like uh uh uh

### 02:00:52 · Speaker 2

This is also a question

### 02:00:56 · Speaker 1

So what should I write here tell me how should I write that

### 02:01:00 · Speaker 3

Ross

### 02:01:08 · Speaker 1

Okay, so does all of you understand this? What is this cross? This is what is this cross?

### 02:01:16 · Speaker 1

Or the cartilage product yeah

### 02:01:21 · Speaker 1

We'll just tell you what that means. See, in one dimension, if you have a line, there is an A, right? The set that we are talking about is minus infinity. That would end at A, correct? So this is the set that we are talking about. Minus infinity to A is this particular set, correct? Now, in two dimensions.

### 02:01:45 · Speaker 1

If you take a point like this is a1 comma a2 right what is the set that we are talking about now we are not talking about this as the subsets of R2 they are not lines what are they?

### 02:02:01 · Speaker 4

Yeah

### 02:02:03 · Speaker 1

uh what to call them areas

### 02:02:06 · Speaker 4

Playing

### 02:02:07 · Speaker 1

planes yeah they are planes okay first of all subsets of r2 are planes okay so what sort of uh plane are we talking about so let's say that we have a1 comma a2 here this is where we are evaluating the distribution function what is the set that i just wrote what does that correspond to

### 02:02:29 · Speaker 3

Or anything to the left of

### 02:02:36 · Speaker 1

This is uh this is A two

### 02:02:36 · Speaker 3

Yeah

### 02:02:45 · Speaker 1

And this is A1. Now tell me what else is that I'm talking about?

### 02:02:52 · Speaker 3

towards the left of line A1 and below the line A2

### 02:02:56 · Speaker 1

Okay so this is line

### 02:03:00 · Speaker 1

space this entire space which extends uh infinitely infinite to to infinity to in the left direction and to infinity in the bottom direction is this clear so this set

### 02:03:15 · Speaker 1

Cartesian product of

### 02:03:23 · Speaker 1

Is all of you clear

### 02:03:32 · Speaker 1

Now we will not be working in two dimensions, we will be working in like 10,000 dimensional space because our image is in 10,000 dimensions. So when I evaluate the distribution function at 10,000 dimensional point, a vector at 10,000 dimension, you should remember what is the inverse image that it maps to. It's a Cartesian product of like all those things. Do you see that? It will be a hyper volume in that dimension.

### 02:04:00 · Speaker 1

Is it okay

### 02:04:04 · Speaker 1

See, when I evaluate the distribution function at a particular point in some 10,000 dimensional space, I'll be looking at the inverse images under that random variable of a certain hyper volume. What is that hyper volume? That hyper volume is given by this sort of a Cartesian product, minus infinity to the first element cross, minus infinity to the second element cross, minus infinity to the third element, and so on. That becomes a hyper volume. In three dimensions, I can tell you what that is. No, it's a huge three-dimensional volume, right? In four dimensions,

### 02:04:34 · Speaker 1

I don't know what it is just call it hyper volume

### 02:04:37 · Speaker 1

Is that okay? So we'll be working with such distributions. We'll be working with random variables whose range space happens to be in some d-dimensional real space. And if it's an image, then it is some 10,000 dimensional. If it's, say, what is the size of the embedding in bird kind of models? It's a few hundreds, right? A few thousands, I suppose.

### 02:05:02 · Speaker 1

Can somebody tell me in bird kind of models what is the size of embedding vectors that you get for each bird This Google that

### 02:05:12 · Speaker 1

BERT embedding size

### 02:05:15 · Speaker 4

8 12

### 02:05:16 · Speaker 1

Huh it's poison fly for me

### 02:05:20 · Speaker 1

Thank you

### 02:05:27 · Speaker 1

768 length vectors word base and word tiny gives you 128 dimensional vectors yeah of order of 100 so that is that is your uh like that is the dimensionality of the range space of the random variable that you will be that i'll be working with is this idea clear to all of you

### 02:05:52 · Speaker 1

questions on this so from now on we'll be working on working with vector value random variables okay not this which means that the elements of sample space gets mapped to a d-dimensional real number okay

### 02:06:06 · Speaker 1

products Cartesian products okay fine now the next thing that I want to talk about is that

### 02:06:23 · Speaker 1

Why doesn't it come to a middle

### 02:06:28 · Speaker 1

thing

### 02:06:30 · Speaker 1

B

### 02:06:34 · Speaker 1

talk of multiple random variables

### 02:06:52 · Speaker 1

Okay now suppose there are two

### 02:06:58 · Speaker 1

random experiments that are happening

### 02:07:06 · Speaker 1

Let me give you an example what I do is first

### 02:07:12 · Speaker 1

In the

### 02:07:25 · Speaker 1

It's it's

### 02:07:27 · Speaker 1

We are saying we are in the example

### 02:07:33 · Speaker 1

There's a coin that is being tossed

### 02:07:41 · Speaker 1

And there is a die that is being loaded

### 02:07:49 · Speaker 1

D-I-E or D-I-E what is it D-I-E is it no D-I-E

### 02:08:03 · Speaker 1

EYE is colour I suppose no

### 02:08:06 · Speaker 3

Yes sir it should be D-I-E-S

### 02:08:09 · Speaker 1

We are eating

### 02:08:16 · Speaker 3

If it is singular it should be D-I-C-E.

### 02:08:20 · Speaker 1

Times correct

### 02:08:23 · Speaker 1

So dice being rolled okay thanks yeah so now what happens is see both of these will have their own sample spaces and underlying probability measures right let's call this p1 and there is another sample space another

### 02:08:43 · Speaker 1

Event space does not probability measure correct

### 02:08:48 · Speaker 1

Right. Now what I can do is can take an element A belonging to F1.

### 02:08:57 · Speaker 1

and an element B that is belonging to F2

### 02:09:05 · Speaker 1

Okay and do this

### 02:09:21 · Speaker 1

Hmm

### 02:09:34 · Speaker 1

I'm just thinking is this the best way to take over this point I'm just going to do it

### 02:09:58 · Speaker 1

Which is not the best example

### 02:10:10 · Speaker 1

Yeah this may not be the best example because

### 02:10:14 · Speaker 1

You can send uh

### 02:10:16 · Speaker 1

Intersections no the art would create some lack in understanding

### 02:10:27 · Speaker 1

To talk that there are two random experiments, okay, so it is like uh

### 02:10:35 · Speaker 1

I said holding

### 02:10:40 · Speaker 1

Ooh

### 02:10:49 · Speaker 1

different configuration I think this would be a better example

### 02:11:02 · Speaker 1

So this can be a good example that here what we are doing is that we are we are throwing two dice of different configuration which means that there are two sample spaces again and two different probability measures

### 02:11:23 · Speaker 1

to okay now again if there is an element

### 02:11:28 · Speaker 1

that is in F1 and an element that is in F2, right? Because these are sets, we can talk about unions and intersections of these, right?

### 02:11:44 · Speaker 1

Can you see what I'm talking about

### 02:11:47 · Speaker 1

We have two random variables. We can talk about unions and intersections of these events, right? These subsets or these, yeah, these subsets of different sample spaces. Now, because we can do that, there are a few things that are being defined, which are like something called, you can define a probability measure.

### 02:12:15 · Speaker 1

In fact, see the unions and intersections may not be on two different sets, right? I mean unions and intersections may be on

### 02:12:26 · Speaker 1

like one random variable as well unions and intersection maybe on a single random variable as well but yeah let's say that we are defining unions and intersections of the uh the

### 02:12:38 · Speaker 1

So the elements of outcomes from two different random variables you can always talk of probability of unions and probability of intersections and so on. There is also this conditional probability that is defined, which is defined as a conditioned on b and you know the definition right it is the probability of the intersection divided by the probability of

### 02:13:03 · Speaker 1

condition in event this is how the conditional probability is defined all of you know this right that's why i asked you whether you people know probability theory this is known right all of you know this okay great now what i wanted to tell you because we can define uh like conditional probabilities and unions of probabilities on on on on uh outcomes coming from two different uh experiments now now what happens is

### 02:13:30 · Speaker 1

There are two uh probability spaces

### 02:13:37 · Speaker 1

There are two probability spaces, which means that there are two reduced spaces. Let's call them X.

### 02:13:45 · Speaker 1

gives a rise to

### 02:13:48 · Speaker 1

point distribution function okay there's another

### 02:13:53 · Speaker 1

sample space and the corresponding probability measure it's called that y this gives rise to another

### 02:14:04 · Speaker 1

induced measure

### 02:14:07 · Speaker 1

Now since we can talk of the unions and intersections of the elements from the sample space, we can talk of what are called as joint distributions.

### 02:14:26 · Speaker 1

See, I will kind of hand wave now and not talk, I mean, not go to details of the definitions. So this is represented like this, which is a joint distribution of pair of random variables. Now this is evaluated at two points, no, x, y, k, b, let's call it.

### 02:14:51 · Speaker 1

Okay, what does this mean? We'll go to our own definition. This is the probability. Okay, so now this is like you take the X inverse of this particular event for the yeah, the event that gets mapped to this particular thing under X. Okay, you take the Cartesian product of this under the random variable Y, take this event that gets mapped to

### 02:15:20 · Speaker 1

maps under this inverse image and that probability right so this will be the probability of some event a that belongs to f1

### 02:15:33 · Speaker 1

intersection from event B that belongs to F

### 02:15:40 · Speaker 1

Is this clear Oh what happened to this

### 02:15:48 · Speaker 1

Is this clear

### 02:15:50 · Speaker 1

So we can talk of joint distributions, right? I mean, joint distributions are again, we are talking of probability of intersections of events. Now, these are intersections of events that are belonging to two different sample spaces. Now, these are, how do you get it? You take first random variable, take its inverse image, get one event, take another random variable, take that, take its inverse image, you get another event, take the intersection of those two, and that is the, and look at the probability of that.

### 02:16:20 · Speaker 1

And that will give you the value of the joint distribution function evaluated those two values. Okay, so similarly you can also talk of conditional distributions.

### 02:16:36 · Speaker 1

definition of conditional distribution is slightly involved okay let me not give you the the definition of it okay denoted by this okay this is evaluated at one point this is

### 02:16:54 · Speaker 1

is like X

### 02:16:57 · Speaker 1

equal to vertex

### 02:17:04 · Speaker 1

given y equal to some p okay

### 02:17:10 · Speaker 1

I mean I don't want to

### 02:17:13 · Speaker 1

in continuous random variables no this step this has a very this has an involved definition but roughly you can see that as the we are looking at the probabilities of

### 02:17:24 · Speaker 1

these kinds of events right conditional events so we are looking this corresponds to some conditional uh the probability of some conditional distribution it's the probability probability of some conditional event okay that the definition of condition the conditional event is this which is that you take the probability of intersection and divide it by the probability of the uh the uh the conditioned event so it has a similar definition but yeah it's yeah you need a little bit of measure theory to know this at least for

### 02:17:54 · Speaker 1

the case of uh uh

### 02:17:58 · Speaker 1

continuous random variables and by the way all the definitions that i have given so far are for continuous random variables if it's a discrete random variable now what happens is the mapping that the random variable does is element by element so you are talking about the inverse images of singletons okay this is a conditional distribution so basically what i want the the two points that i wanted to drive home is that there can be random variables which would take this

### 02:18:28 · Speaker 1

sample space and maps it to vectors and there can be pairs of random variables where you should envision you should you should you should imagine two uh random experiments that are happening okay so there is an association between those two uh random variables that happens through intersections and unions of events okay and and you can define joint distributions and conditional distributions now definition wise this is defined as

### 02:18:59 · Speaker 1

Okay

### 02:19:05 · Speaker 1

The joint distribution divided by

### 02:19:08 · Speaker 1

of entropy so it is defined mathematically uh but yeah so it always has a a corresponding uh probabilistic interpretation as we were looking at okay okay uh questions uh abirup

### 02:19:26 · Speaker 2

Yeah so I could not understand a couple of things can you scroll up a little bit

### 02:19:32 · Speaker 1

In which party Dr.

### 02:19:33 · Speaker 2

Yeah after after after the vector valued when you were actually

### 02:19:37 · Speaker 4

saying that uh

### 02:19:45 · Speaker 4

Then uh

### 02:19:49 · Speaker 4

A and B they

### 02:19:52 · Speaker 2

I I cannot understand the notion how you can do it

### 02:19:56 · Speaker 1

You can know see it's like you take a set uh let's say that we have two subsets of R you can define a union of both of them right why can't you do that

### 02:20:06 · Speaker 2

Yeah so

### 02:20:07 · Speaker 4

That is because in

### 02:20:10 · Speaker 4

So for

### 02:20:12 · Speaker 1

Same thing I'm saying you're only two types of different configuration the universal center same thing right

### 02:20:19 · Speaker 4

So in in case of age

### 02:20:20 · Speaker 1

That is why you you remember I said toss a coin roll a die

### 02:20:26 · Speaker 1

Then I erase that example precisely because of this. It will create confusion. In the example that I have given, the universal set is the comprising of roles of dice for both the cases.

### 02:20:40 · Speaker 2

Okay so if we are considering one event space as rolling a die and another event space as tossing a coin

### 02:20:48 · Speaker 1

Then the universe will be one two six and those two things head and tail that's all

### 02:20:48 · Speaker 4

Oh

### 02:20:53 · Speaker 2

Uh okay so it is going to be F one union F two

### 02:20:56 · Speaker 1

Of course of course sigma omega 1 cross omega 2 omega 1 cross omega 2 that would be your universal sample space

### 02:21:07 · Speaker 1

I didn't want to do that because of this precise reason so if you roll a die and toss a coin then how can you define unions is a question that I anticipated that's why I said roll two dice

### 02:21:18 · Speaker 2

Okay, okay, okay. And also, as the second question, when a little bit down, if you don't mind, a little bit scroll down.

### 02:21:28 · Speaker 2

Yeah, so x inverse of minus infinity to a cross of y inverse of this one.

### 02:21:35 · Speaker 2

How are you replacing the cross sign with an intersection sign in the next line? I have a difficulty in understanding that.

### 02:21:42 · Speaker 1

Ah, see, the cross products here, right, in the condition, this matches to one event, that matches to another event, right? Okay. So that is the intersection only.

### 02:22:06 · Speaker 1

Okay, so the point is that here when you talk of intersection, you talk of cross products of two sets, is it correct?

### 02:22:13 · Speaker 1

This is cross product of two sets so the intersection is nothing but cross product of two sets no

### 02:22:13 · Speaker 2

Yes

### 02:22:18 · Speaker 2

Yeah yeah

### 02:22:20 · Speaker 1

That's it

### 02:22:22 · Speaker 1

Okay service

### 02:22:26 · Speaker 2

is the same thing like x inverse of minus infinity a gives a

### 02:22:34 · Speaker 1

That gives you P

### 02:22:38 · Speaker 2

gives B and same thing like it doesn't A cross B right

### 02:22:44 · Speaker 1

It is defined that way you know joint distribution is defined that way by definition

### 02:22:50 · Speaker 2

So it's a cross product right so uh

### 02:22:52 · Speaker 1

Correct it is by definition

### 02:22:55 · Speaker 2

Below it should also should be a cross be right so there will be pairs ordered pair

### 02:23:00 · Speaker 1

No no no A is no no no so there are two sets not talking about two sets here so probability is defined that is why you have

### 02:23:01 · Speaker 3

And B

### 02:23:10 · Speaker 1

The the proper idea intersections are defined

### 02:23:15 · Speaker 1

Okay, so here the joint distributions are defined that way that if you evaluate it, they are actually the intersections of, see in fact I should, I don't know where the definition is coming from. Let's just say that these are intersections by definition. And so, then that will create, that will clear the thing, no?

### 02:23:38 · Speaker 1

And that's that's the definition of job distribution by the yeah

### 02:23:43 · Speaker 1

Okay uh Sanjay

### 02:23:46 · Speaker 3

if we try to understand joint distributions with an example so okay let me just uh explain what i perceived by this statement is we have we want to find the joint distribution for events where there is a three on the first die and a four on the second die okay so getting a three becomes event a and on getting a four on dice two becomes event b so we want to

### 02:24:16 · Speaker 3

So both

### 02:24:16 · Speaker 1

So those two those two gets mapped those two gets mapped to different uh points at the by two different random variables and you get the inverse bits that's all yeah it's correct

### 02:24:24 · Speaker 3

Correct, correct. So now when we want to find the probability that event A belongs to F1 and event B belongs to F2, so it will only be both are happening. So that means we will obtain the Cartesian product of F1 and F2 and in that only point 3 comma 4 where 3 is obtained on die 1 and 4 is obtained on die 2.

### 02:24:35 · Speaker 1

Oh stop packing

### 02:24:50 · Speaker 1

Agreed. That's that's the that that's the intersection that you have yeah

### 02:24:53 · Speaker 3

Yeah that is the only intersection right because otherwise since both

### 02:24:54 · Speaker 1

Is the only

### 02:24:57 · Speaker 1

Got it

### 02:24:59 · Speaker 1

I understand what you see yeah okay yeah uh

### 02:25:04 · Speaker 4

So in this case the x and y have to be independent right

### 02:25:10 · Speaker 1

need not be if they are independent then they I mean I have not defined independence right random variables are called independent if the joint distribution happens to be product of marginals

### 02:25:22 · Speaker 1

If they are independent then intersection is null

### 02:25:28 · Speaker 1

They are not independent, right? This is the general definition. General definition is one experiment

### 02:25:31 · Speaker 4

So there can be one experiment can be dependent on the other dep

### 02:25:35 · Speaker 1

They are they are actually I mean the moment I talk of joint distributions they are dependent now

### 02:25:41 · Speaker 1

If they are independent then the joint distribution will become the product of marginals centered

### 02:25:45 · Speaker 4

And no no what I meant is say for example in this case of uh rolling two die the outcome of uh the second experiment shouldn't depend on the outcome of the first

### 02:25:56 · Speaker 1

And the way we have conceived it they are independent

### 02:25:59 · Speaker 1

Independence is if P of XY is given by PX into PY then it is independent

### 02:26:08 · Speaker 4

Okay but this not a necessary condition

### 02:26:10 · Speaker 1

No why I mean the way we have conceived the pair of random variables is that in general they are not independent right

### 02:26:17 · Speaker 4

Okay okay

### 02:26:19 · Speaker 1

Uh she won't

### 02:26:22 · Speaker 4

Just sir I don't have any question just one uh thing that I am getting confused with small y capital Ys I last time also

### 02:26:29 · Speaker 1

So where is small by I'm not in small by it's all capital right now

### 02:26:32 · Speaker 4

Those are yeah on the conditional distribution so it's all random variable right so capital Y

### 02:26:39 · Speaker 1

I'm sorry my my bag sorry

### 02:26:42 · Speaker 4

No so in your previous lectures also

### 02:26:45 · Speaker 2

The small y and capital Y we tend to use it

### 02:26:50 · Speaker 1

Yeah thanks for thanks for bringing that up if I make that mistake again just allow it to me okay

### 02:26:50 · Speaker 2

Thank you

### 02:26:58 · Speaker 1

so so that i can i can correct myself yeah see yeah this is i think uh how what is the how many times i've taught no um 2017 is when i started this is 2024 seven years so on an average i mean not on average every time i've taught every semester there's 14 times and this online some three four times but there's 17 18 times i've taught so what

### 02:27:28 · Speaker 1

you are seeing now is actually uh i've done gradient descent on my teaching based on feedback every time and it has come to some optimum and that is what you are seeing so imagine what my students have the plight of my students so many years back i didn't know how to do board work right i was like in spite of doing it for 15 times 18 times sometimes the notations gets uh here and there and all that but yeah i think i've improved right

### 02:27:58 · Speaker 1

of my students tell me that I've improved over time. That's why I have that feedback form, you see. Please use that if you have any concern that you cannot. When Seon was bold enough to tell me that I do this, I appreciate that. I don't mind. You can tell me that this is you're going fast. Whatever you know, I don't mind. Okay. You can express it. But if you think that expressing that will embarrass you for whatever reason,

### 02:28:28 · Speaker 1

You have that anonymous feedback form. Do put in your comments, right? Constructive, destructive. I told you, right? A lot of times students use it to vent out their frustration. It's okay at times you can do that, but don't use it for just venting out your frustration. That will be too much negativity.

### 02:28:48 · Speaker 1

Great. Okay. So, Shivan, thank you for that. If you if you if you notice such a such kind of a thing, just let me know. I'll try to be consistent as much as possible in notations. I understand how important it is to be consistent.

### 02:29:03 · Speaker 1

Okay, maybe I'll take this B out. I'll tell you why this why I wrote this in a while. Okay, so these are I'm kind of hand waving now because like this is not a probability theory course, right? This is just to build some basics on it.

### 02:29:20 · Speaker 1

Now let us come to uh yeah independence conditional distributions joint distributions multiple tandem variables yeah one other thing that is to be defined is what is called as a probability density function

### 02:29:38 · Speaker 4

I don't know

### 02:29:41 · Speaker 3

I'm finally getting it

### 02:29:50 · Speaker 1

Was that some gali in some some language? If you speak in your language that I don't understand right what can I do?

### 02:30:00 · Speaker 1

See gales make sense only if you make the other person understand what you are saying no so

### 02:30:05 · Speaker 1

See I have again off topic but I this is a professional I'm married for 10 years so if I'm too angry right on my children or like on my wife and I don't want to escalate the war what I do is I'll start scolding them in Sanskrit or some other language that they don't understand so that you know my anger is vented out but they don't understand and respond back so that no escalation happens

### 02:30:35 · Speaker 1

So maybe somebody is doing that that way, who knows? Okay. So probability density functions. So now probability density functions. Okay. Notation wise, note that for distribution functions, I'm using the script p, right? I mean, two lines p. So for probability density functions, I use like small p. So this probability density function is a function, right? That is equal to the derivative of the distribution function.

### 02:31:05 · Speaker 1

Right evaluated at that point that's all okay. I'll maybe not use A let's use some other thing here

### 02:31:22 · Speaker 1

Yeah this is the definition of the probability density function it's just a derivative

### 02:31:25 · Speaker 3

That's the

### 02:31:28 · Speaker 3

or maybe I am moving ahead, but just for clarification, for a continuous function, random variables, we have CDF and PDF, like cumulative distribution and probability density functions, correct?

### 02:31:41 · Speaker 1

Mm mm

### 02:31:43 · Speaker 3

And for

### 02:31:43 · Speaker 1

For discrete random variables I will tell you so that will become probability mass functions. Distribution functions are the same as will become probability mass functions.

### 02:31:54 · Speaker 1

Okay, so good that you mentioned that. See, mostly in this course we'll be dealing with continuous random variables.

### 02:32:04 · Speaker 1

that you mentioned that probability mass functions so this is for this is for continuous random variable okay for discrete random variable the probability density function is nothing but the

### 02:32:26 · Speaker 1

Cost difference

### 02:32:33 · Speaker 1

Distribution function evaluate for that and distribution function evaluate for that

### 02:32:41 · Speaker 1

A plus one and A you know yeah

### 02:32:46 · Speaker 1

the density function this is for the discrete and variable okay so please note

### 02:32:52 · Speaker 1

This right is, this is not a probability. That is why, you know, if you take an example, right, if you take a random variable, this notation is normally distributed with 0, 1, okay? This means that the density function of this is equal to that thing 1 by 2 by sigma squared e power minus x minus mu.

### 02:33:22 · Speaker 1

whole square divided by 2 sigma squared right

### 02:33:27 · Speaker 1

there is a square root here yeah i don't remember this and i don't expect you to remember as well this is for a scalar value case for a vector value case that is 1 by 2 pi to the power of d by 2 where t is the dimensionality and you have the determinant of this matrix so e power minus x minus mu transpose so this is a vector of d dimensions sigma is a matrix d by d this is x minus mu

### 02:33:59 · Speaker 1

Uh this is what it is so now note that this entire thing is a scalar no

### 02:34:05 · Speaker 1

this is p cross 1 times p cross d times no 1 cross d so my x and mu are p cross 1 and I tell you settle this for once for all 1 cross d times d cross d times p cross 1 so this would be 1 cross d times

### 02:34:30 · Speaker 1

d cross 1 this will be 1 cross 1 because x is in R d the range space of random variable is 3 dimensional which means that mu is also in R d okay this is the probability whenever we see in most of ml right we we work with density functions not distribution functions because of ease of computation that's what i mean lot of standard metrics exist lot of standard forms exist for density functions okay what is the what is density function

### 02:35:00 · Speaker 1

Density function is nothing but the derivative of the distribution function. So if you evaluate the density function at a point, right, what you are getting is the derivative of the distribution function at that point. That's all. Please note that if you evaluate the density function at a particular point A, you are not getting the probability of that point.

### 02:35:21 · Speaker 1

Okay, so this is one take home message. Evaluating the density function at a particular point will not give you the probability of that point. Okay, because probability of a point does not make sense. Probability, remember, is a measure that is defined on the elements of sample space always. Okay, evaluating the density function at a point will simply give you the derivative, the value of the derivative of the distribution function at that point. That's all. However,

### 02:35:51 · Speaker 1

If you take the density function right and integrate it

### 02:36:00 · Speaker 1

a laying over a set what do you get this is equal to the distribution function evaluated at a see this is equal to the probability of that entire story

### 02:36:17 · Speaker 1

Do you understand this? What I'm saying is

### 02:36:23 · Speaker 1

Evaluating

### 02:36:26 · Speaker 1

the density function

### 02:36:32 · Speaker 1

a point

### 02:36:35 · Speaker 1

Is not equal to the probability is not equal to probability of anything

### 02:36:45 · Speaker 1

How about that

### 02:36:47 · Speaker 1

integrating

### 02:36:52 · Speaker 1

density function

### 02:36:57 · Speaker 1

Oh a sec

### 02:37:00 · Speaker 1

is equal to the probability. So for instance, right, if you take the density function and integrate it between a and b, what do you get? You will get the distribution function evaluated at b minus the distribution function evaluated at d. So this is a valid probability. You know this, right? So always remember that evaluating the distribution function will give you a valid probability. Evaluating the density function will not give you

### 02:37:30 · Speaker 1

valid probability but integrating the density function over a range will give you a valid probability because that is equal to the distribution function

### 02:37:39 · Speaker 1

Is this clear to all of you

### 02:37:49 · Speaker 1

Okay, okay, so now I think we have like enough background to any questions so far? Now let's come back to that problem of estimating genders from an image.

### 02:38:04 · Speaker 3

Answer one question

### 02:38:06 · Speaker 1

Uh before you ask the question uh I have a request uh with this background right you know please go back to that uh uh that you know that Goodfellow's book on machine learning and read the chapter on distribution and and probability theory please so while you come to the next class I expect you I expect all of you to know all this because this actually kind of uh uh brings us to the end of uh the basic probability theory treatment

### 02:38:36 · Speaker 1

okay i i don't intend to teach you probability theory because i assume that you people know it but just to give this perspective i spent some time please go back and uh brush up your probability theory fundamentals before you come to the next class please do that okay questions

### 02:38:53 · Speaker 3

Sir, so when we have the probability density function and we have px of a, so there a like it does not evaluate to minus infinity comma minus a, right?

### 02:39:09 · Speaker 1

So again if you ta if you evaluate the probability density function at a point

### 02:39:13 · Speaker 3

So it it does not mean that it is a range from minus infinity comma a it is strictly an

### 02:39:19 · Speaker 1

No no no no it is simply no no it is simply means that you are taking the derivative of the distribution function and evaluating that at a that's all

### 02:39:30 · Speaker 3

Okay

### 02:39:32 · Speaker 1

evaluating the see if you suppose you plug in some value a into the Gaussian distribution and evaluate it it only means that

### 02:39:42 · Speaker 1

There is an underlying random variable okay with a distribution function and that distribution function

### 02:39:50 · Speaker 1

you take the derivative or the differential of that distribution function and evaluating that derivative at a that's all it means

### 02:40:00 · Speaker 1

But if you take the distribution function if you take this Gaussian distribution Gaussian density function okay

### 02:40:09 · Speaker 1

integrated within a range then what you are doing is evaluating the distribution function at two different points no

### 02:40:20 · Speaker 1

That is what I wrote if you take it and take the running integral of this part you get the distribution function evaluated at this point this point A

### 02:40:28 · Speaker 1

If you take the range, if you take the distribution density function and integrate it between the range, it is equivalent to evaluating distribution functions at those two endpoints and taking the difference, which is the probability. Because distribution function evaluated at point will give you a probability.

### 02:40:48 · Speaker 1

So remember this book

### 02:40:51 · Speaker 3

And sub distribution

### 02:40:51 · Speaker 1

answer distribution okay let me let me tell you so suppose there is a random variable that is uniform uh ask the class i'll take your question that is uniform between zero and half okay what is the density function of this

### 02:41:10 · Speaker 1

Do people know what the density function of this is? Uniform random variable between 0 and A and B. What is the density function of a uniform random variable between A and B?

### 02:41:23 · Speaker 4

Zero if less than zero

### 02:41:28 · Speaker 4

And half minus zero is the left minus the left minus zero

### 02:41:30 · Speaker 2

One thing

### 02:41:32 · Speaker 4

One by V minus there

### 02:41:32 · Speaker 1

1 by b minus a 1 by b minus a row it is equal to 0 right if

### 02:41:42 · Speaker 1

Excess

### 02:41:45 · Speaker 1

Yeah maybe it's easier to write it that way it's equal to two

### 02:41:53 · Speaker 1

X is between this right and zero otherwise

### 02:42:00 · Speaker 1

The density function of a uniform random variable looks like this, no, zero and half. This is zero, this is half, the height is equal to two. This is how the density function looks, right? All of you agree? Anyone has a question on this?

### 02:42:19 · Speaker 1

Now I mean if we were to say that evaluating the density function at a point will give you a probability how can that happen it's contradictory no

### 02:42:30 · Speaker 1

The probability is upper bounded by one. Density function evaluated at a particular point here will not give you a probability. Do you see that? Do you appreciate that? This is an example that I have constructed to show you that evaluating the density function at a point will not give you a probability.

### 02:42:52 · Speaker 1

This is clear

### 02:42:57 · Speaker 1

However if you take if you integrate this and if you take a small area

### 02:43:03 · Speaker 1

This is the probability because you know that will evaluate to something less than one between zero and one

### 02:43:13 · Speaker 1

Evaluating the density function at a point will not give you probability, but integrating that will give you probabilities. Is that okay? Because integrating the density function is equivalent to evaluating the distribution function at a particular point.

### 02:43:31 · Speaker 1

Okay uh astic

### 02:43:34 · Speaker 4

Yeah hi sir so uh in the above integral uh where you are integrating it from a to b

### 02:43:56 · Speaker 1

Stay

### 02:43:56 · Speaker 4

Mistake. Yeah, while you define the derivative there also it should be a small x right where you take the derivative

### 02:44:05 · Speaker 1

It depends. It depends. I mean, if it's a if it's a if it's a scalar valued random variable, then it's small x, right? If it's a vector valued random variable, what happens? It's the gradient that we define. That's all right because the you understand?

### 02:44:31 · Speaker 1

Okay, uh so this is clear.

### 02:44:39 · Speaker 1

So when does our class end it is it at 12 or at 12 15

### 02:44:47 · Speaker 1

I think so

### 02:44:47 · Speaker 2

That's 1215 1215

### 02:44:51 · Speaker 1

Can I continue for 10-15 more minutes?

### 02:44:59 · Speaker 1

Okay, because now this actually is a nice time to stop. Yeah, no, we have topic wise and say we have come to the end of this.

### 02:45:16 · Speaker 1

So let's come to machine learning

### 02:45:26 · Speaker 1

And for now let's do supervised machine learning

### 02:45:38 · Speaker 1

Okay so what do we have suppose

### 02:45:42 · Speaker 1

we have

### 02:45:46 · Speaker 1

thousand images

### 02:45:53 · Speaker 1

with labels

### 02:45:58 · Speaker 1

this can be like let's say research and done labels this can be any labels or identity labels anything okay now this is what we have this we understand now everything that we do from now on has to be seen in the uh seen from the perspective of uh the distribution functions and random variables and all that what how do we see this let us let us represent this as a set d okay

### 02:46:29 · Speaker 1

I will I will come I will reduce the levels

### 02:46:34 · Speaker 1

afterwards so let this is pics one

### 02:46:39 · Speaker 1

X two

### 02:46:43 · Speaker 1

and explosive

### 02:46:48 · Speaker 1

Oh easy image let's write it down here

### 02:46:55 · Speaker 1

Each image I am the image is

### 02:46:59 · Speaker 1

is uh what do you want two thousand two hundred into three hundred dimensional

### 02:47:07 · Speaker 1

how many 60 to 4060 to all the pixels okay this means that every xi is in

### 02:47:22 · Speaker 1

Any confusion on this any question on this

### 02:47:36 · Speaker 1

Any question on this? This notation is clear. We have 1000 images, all of them are in 60000 dimension. How do we see that? So now from our language, each X sign is

### 02:47:51 · Speaker 1

an element

### 02:47:56 · Speaker 1

Um

### 02:47:58 · Speaker 1

a range space

### 02:48:04 · Speaker 1

of a random variable x

### 02:48:09 · Speaker 1

You understand what's happening?

### 02:48:12 · Speaker 1

So what is happening is the underlying random experiment, right, the random trial has been conducted thousand times, okay? And there is an underlying random variable that has taken those outcomes and mapped it to some 60,000 dimensional space using this random variable.

### 02:48:33 · Speaker 1

Is this clear

### 02:48:35 · Speaker 1

This implies that there exists

### 02:48:43 · Speaker 1

And then the

### 02:48:49 · Speaker 1

Probability measure

### 02:48:53 · Speaker 1

And thus

### 02:48:56 · Speaker 1

and distribution function

### 02:49:08 · Speaker 1

Do you agree?

### 02:49:10 · Speaker 1

There exists an underlying probability measure and therefore a distribution function induced by X correct

### 02:49:19 · Speaker 1

So that is represented as this right I mean you say that this is a data that is sampled from this notation mean this tilde says sampled from

### 02:49:33 · Speaker 1

Okay, what do you mean by sampled from? There is a there is an underlying random trial that is happening and there exists a random variable and that random variable gives rise to some induced measure. These are elements from the range space of random variable. That is what this notation means being sampled from sampled from a distribution. This is what this is how we write.

### 02:50:00 · Speaker 1

You get the notation. So this is a starting point for machine learning when we have data. We say that data has been sampled from

### 02:50:11 · Speaker 1

Distribution

### 02:50:14 · Speaker 1

Okay, sampled from our distribution, not our distribution because we have specified that sampled from

### 02:50:25 · Speaker 1

E distribution

### 02:50:29 · Speaker 1

index this is like data

### 02:50:35 · Speaker 1

data sampled from the distribution px. Okay. What does that mean? That means that you understand the entire story right now that there exists an underlying probability measure and there was a sample space, there is a random experiment happening, there is a random variable that mapped that those outcomes to some real numbers, which is 60,000 dimensional real numbers. And what we see are the elements from the range space of it. And because there was a probability measure, there exists a distribution function. Yeah, that's what we are.

### 02:51:05 · Speaker 1

That's not we we have now

### 02:51:08 · Speaker 1

Is this clear

### 02:51:11 · Speaker 1

I just wanted to give you this world view right I mean had you knew this then I would have not spent those three hours so this is the world view that I want you to have please ask me questions if if you need clarifications at this point yeah in the genes

### 02:51:27 · Speaker 2

Yeah just trying to get how did you get sixty thousand on R

### 02:51:32 · Speaker 1

See every image right you have image is a 67 dimensional vector no right I mean 200 pixels horizontally 300 pixels vertically so this is the one real number second real number third real number fourth I have just tagged them as columns and made it a long vector of 67 dimensional

### 02:51:49 · Speaker 2

I read that as 30 C

### 02:51:56 · Speaker 2

I didn't read 300 it was looking like 30 C yeah

### 02:52:04 · Speaker 2

Yes whatever confusing yeah it's clear

### 02:52:06 · Speaker 1

Yeah

### 02:52:08 · Speaker 1

If it's word embedding no then it is some 786 7 703 dimensional vector it doesn't matter depends on what your data is uh I mean

### 02:52:20 · Speaker 4

Yeah, so I have a question. So regarding the, you said that the, these x1, x2, x3, these are the, these belong to the range space of the random variable function. And there is a probability.

### 02:52:37 · Speaker 1

Yeah but I I I I I like your random variable function

### 02:52:43 · Speaker 1

that's that's what it is okay yeah but nobody calls it unfortunately a random variable function but that's what it is yes move on please

### 02:52:53 · Speaker 4

yeah so uh so the probability distribution

### 02:53:09 · Speaker 1

No no no no no hold on again now what do you mean by probability distribution function of outcomes that's not a well defined term

### 02:53:18 · Speaker 1

Probability measures are defined on over outcomes

### 02:53:23 · Speaker 1

not distribution functions

### 02:53:26 · Speaker 1

Are you asking how will they will probably measure relative distribution function

### 02:53:29 · Speaker 4

Yeah yeah

### 02:53:31 · Speaker 1

That is by definition now we have defined that here

### 02:53:35 · Speaker 1

That green thing this is how they are related

### 02:53:41 · Speaker 4

Okay okay then uh my question is

### 02:53:43 · Speaker 1

This is all related no Yeah

### 02:53:45 · Speaker 4

Yeah then my question is that how are these two probability measures they are related I mean how are they related they are

### 02:53:52 · Speaker 1

There are no two probability measures there is only one probability measure there is a distribution function

### 02:53:58 · Speaker 1

Where are two probability measures here? There is only one probability measure no

### 02:54:03 · Speaker 4

Oh

### 02:54:04 · Speaker 1

But that's

### 02:54:05 · Speaker 4

No any

### 02:54:06 · Speaker 1

Any questions

### 02:54:07 · Speaker 4

somewhere in the in the top you mentioned like you know that we have a uh outcomes and we have a set of events and we have a random variable which maps them to certain real numbers and we have a borel sigma algebra and a probability measure

### 02:54:26 · Speaker 1

Not probability it's not probability measure it is an induced measure induced measure induced measure is called distribution function

### 02:54:33 · Speaker 2

Okay, okay

### 02:54:34 · Speaker 1

The induced measure itself is called distribution function

### 02:54:38 · Speaker 2

Okay, okay

### 02:54:40 · Speaker 4

So P one

### 02:54:40 · Speaker 1

There are no two measures there is only one measure two measures will come into picture only if you have two random variables if you have a single random variable you only have one

### 02:54:49 · Speaker 1

Measure state and one distribution function

### 02:54:52 · Speaker 4

So I I'm not even sure whether my question is correct or not if it is wrong then please correct me then how are P1 and Px they are related

### 02:55:00 · Speaker 4

And this and this

### 02:55:01 · Speaker 1

This is when you have two random variables okay are you talking about multiple random variables or a single random variable

### 02:55:05 · Speaker 4

People are not very well so as to

### 02:55:08 · Speaker 4

single random variable or the equations which we are just clashing

### 02:55:13 · Speaker 1

Which ones this ones

### 02:55:17 · Speaker 2

The place where you have written the induced thing like the X the X over the arrow

### 02:55:25 · Speaker 2

You just run past

### 02:55:28 · Speaker 4

This one, this one

### 02:55:36 · Speaker 4

Not exactly you just went past it okay maybe I can just uh

### 02:55:40 · Speaker 1

Yeah that's right.

### 02:55:40 · Speaker 4

Yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah

### 02:55:42 · Speaker 1

Here here there are two writing variables

### 02:55:47 · Speaker 4

Yeah but on the left hand side you have written omega one f one p one and there is an arrow where x is a random variable and this

### 02:55:56 · Speaker 4

real numbers our set of real numbers v is the vector signal and px

### 02:56:01 · Speaker 1

is the induced measure under that random variable f it is one there is one distribution function the induced measure itself is a distribution function

### 02:56:10 · Speaker 4

Okay okay

### 02:56:12 · Speaker 1

And another random variable introduces another distribution function and there is another standard link measure

### 02:56:19 · Speaker 4

So people want

### 02:56:19 · Speaker 1

Every random variable has a measure

### 02:56:24 · Speaker 4

Okay okay

### 02:56:25 · Speaker 1

Measure P1 get induced to distribution function Px, measure P2 gets induced to distribution function Py.

### 02:56:34 · Speaker 2

Okay okay okay

### 02:56:38 · Speaker 1

Send okay

### 02:56:39 · Speaker 2

Okay yeah yeah

### 02:56:41 · Speaker 1

But here right when we are talking about data there is only one measure that we are talking about and there is only one distribution function

### 02:56:52 · Speaker 1

He said okay

### 02:56:53 · Speaker 4

Yeah so

### 02:56:56 · Speaker 1

Any other question on this?

### 02:56:58 · Speaker 2

Yeah answer you are considering black and white picture because otherwise it would be

### 02:57:02 · Speaker 1

No way

### 02:57:04 · Speaker 2

Uh I recall they said

### 02:57:07 · Speaker 1

No every pixel is a real number no

### 02:57:14 · Speaker 2

So yeah you are multiplying 200 by 100 so what you are saying

### 02:57:15 · Speaker 1

Now what you are saying is uh what you are saying is there should be another three channel image here not 200 plus 300 plus 3

### 02:57:23 · Speaker 2

Yeah right

### 02:57:25 · Speaker 1

If it's three then you multiply this with three no that's all it is like one lakh eighteen thousand dimensional that's all yeah

### 02:57:32 · Speaker 2

Oh oh

### 02:57:34 · Speaker 1

For now I'm for the sake of ease no it doesn't matter I mean you should understand that the data dimension doesn't matter because it can be anything it can be a picture it can be some 30 dimensional speech vector it can be some bird embedding it doesn't matter what it is

### 02:57:52 · Speaker 1

This will be an example. So in general right in general I want to generalize this idea I have to just say that all data is in some d dimensional space that's all.

### 02:58:07 · Speaker 1

Right. So if it's an image, then it has 16,000 dimensional. If it's a bird, if it's bird embedding, it's 7,000 dimensional or whatever.

### 02:58:20 · Speaker 2

Yeah thanks

### 02:58:21 · Speaker 1

Okay any other questions

### 02:58:31 · Speaker 1

Okay now suppose that take another example another scenario where suppose we have images same thing we have thousand images

### 02:58:44 · Speaker 1

With labels, we take MNIST itself, you know, sixty thousand examples with

### 02:58:51 · Speaker 1

50 000 examples MNIST has 50 training data has 50 000 examples in it

### 02:58:58 · Speaker 1

10 to 100 devices with labels these labels are

### 02:59:04 · Speaker 1

10 labels 0 to 9

### 02:59:08 · Speaker 1

0 to 9, you have 10 labels. Now how does the data represented? Data is represented like this. Every point is a tuple like this, x1 comma y1.

### 02:59:21 · Speaker 1

x to the power of 2

### 02:59:25 · Speaker 1

X fifty thousand

### 02:59:28 · Speaker 1

I'm buying fifteen thousand

### 02:59:33 · Speaker 1

Okay, now how do we use our worldview on this? Is that you say that this is sampled from an underlying joint distribution between two random variables x, y. Because x represents the random variable. So basically we are saying there are two sample spaces, right? There is a

### 02:59:55 · Speaker 1

x that takes the image space and maps it to 50,000 no what is the dimensionality of image well let's say that each image each image is in 784 dimensional because MNIST is a 28 by 28 image okay so now this maps it to 784 dimensions this is one random variable there is another random variable so yi is a discrete random variable that can take values it is like

### 03:00:25 · Speaker 1

Rolling a die okay now this is there's another random variable y that takes another sample space omega 2 and maps it to

### 03:00:37 · Speaker 1

discrete center and note that a random variable need not

### 03:00:43 · Speaker 1

range space of the random variable need not be continuous no it can be discrete as well now there are two random variables here and the data is now modeled as coming from the cross products of these two right i mean you take a picture and you associate your sample one one i mean you you take a random trial from this sample space you get a picture and you make a a a random trial from this and then you take a pair of them that is your data point and because

### 03:01:13 · Speaker 1

Was that exist?

### 03:01:16 · Speaker 1

Probability is on the intersections and unions of these two sets you can define joint distributions on it

### 03:01:25 · Speaker 1

You get it

### 03:01:27 · Speaker 1

Now in this is this is supervised this is typically called supervised machine learning okay

### 03:01:36 · Speaker 1

You have two random variables

### 03:01:42 · Speaker 1

two sample spaces and two probability measures basically right it is called supervised machine learning because you have one random variable corresponding to data the other other random variable is typically called as the label okay now the data has been sampled from joint distribution of x and y

### 03:02:01 · Speaker 1

Is this clear

### 03:02:08 · Speaker 1

And whatever I defined here, no, this is unsupervised machine learning where you have one, only one probability measure. In supervised machine learning, you will have two probability measures. One is called the data, the other measure for the labels.

### 03:02:28 · Speaker 1

So this we will write maybe

### 03:02:31 · Speaker 1

Uh this is

### 03:02:34 · Speaker 1

is heading for unsupervised learning

### 03:02:41 · Speaker 1

This is I think

### 03:02:45 · Speaker 1

So what changes? You see that we have, so we are sampling from px here, right? There's one quality distribution function. And here we are sampling from the joint distribution of those two because there are two random variables. See, now we actually think about it. If you think about it, what was our problem? Our problem was that we don't know how pixels are related to these notion of digits, right? So the way we model it is that, okay, two random experiments are happening.

### 03:03:15 · Speaker 1

somebody is writing that digit on like paper and take being the picture is being taken and all that okay there's one random variable that is basically converting all that into a real number so once this is done this is being now associated with one of these nine digits emotion of digits that is another random experiment so both of them have uncertainty right now but you have joint distribution which means that now every image right has a certain uncertainty or a probability

### 03:03:45 · Speaker 1

of belonging to one of these nine classes. You see that now? See, initially I said that this probability theory will give you a tool to handle uncertainty that incorporates uncertainty in construction itself. Now you see y. Okay. Now we don't talk about functions from y to x. See, in deterministic case, we were talking about functions that deterministically map elements of y to elements of x. Now we are not talking about it. We are talking about distributions. Okay.

### 03:04:15 · Speaker 1

joint distributions between these two sets which means that given every element in y or rather every element in x there is a certain probability associated with that belonging to one of these nine classes nine labels do you nine elements from other set do you see that when i will concretize these ideas in next class okay but i want you to appreciate right i mean the whole branch of this probability theory was was was conceived because you start with a random expression

### 03:04:45 · Speaker 1

right and you have this notion of probability associated with events now you deal with everything you model everything in terms of those random events and the and distribution functions right and you have that notion of uncertainty by construction

### 03:05:02 · Speaker 1

Is this clear? I'll continue from this in the next class while I take questions. I'll continue from this in the next class. I'll concretize these ideas. But yeah, you should understand how to represent data. Now data is represented as samples drawn from, this is actually called, you know, samples drawn from a distribution. People also call this as data sampled from a distribution or samples data drawn from an underlying distribution. Okay. These are common words that are used.

### 03:05:32 · Speaker 1

Whenever you see that they are drawn from a distribution you will you should know the entire story. What's happening is that there is a random experiment you get sample space you get event spaces there is a random variable that is mapping this to real numbers and there is a probability measure assigned to the elements of sample space or rather elements of event space and therefore a distribution function gets induced.

### 03:05:58 · Speaker 1

Right So when you say that the data is sampled from a distribution this is what it means

### 03:06:07 · Speaker 1

Uh yeah prosanna

### 03:06:14 · Speaker 1

person but one

### 03:06:20 · Speaker 1

Yes I can hear you

### 03:06:21 · Speaker 4

Yeah, so in the last slide, I think you explained about x and y random variable function. So what is the relation?

### 03:06:29 · Speaker 2

between omega 1 and omega 2 here

### 03:06:32 · Speaker 2

They're on it

### 03:06:33 · Speaker 1

Yeah, there are two sets basically, right? I mean, there's no relation per se.

### 03:06:42 · Speaker 2

But whatever the

### 03:06:43 · Speaker 1

But you can you can conceive you can talk of intersections and unions between those two elements that's all

### 03:06:53 · Speaker 1

Right. Those two are the two sample spaces. I mean, those are samples. Those two are sample spaces that would that would encompass the outcomes of these two random experiments. But these two random experiments are not independent, right? Quote unquote independent in the sense that they are connected.

### 03:07:11 · Speaker 2

Yeah only for the images that you have taken like you will assign the number

### 03:07:11 · Speaker 1

A true monumental

### 03:07:15 · Speaker 2

So basically like

### 03:07:17 · Speaker 1

Remember you sample an image yeah you sample an image you sample a number and do associate them using unions and intersections

### 03:07:32 · Speaker 1

Uh yeah

### 03:07:35 · Speaker 4

Sir do we know this PX or PXY in this case No

### 03:07:38 · Speaker 1

No, we don't. That's the whole problem in machine learning. The machine learning is if I have to summarize machine learning in one sentence, it is this given the estimate px, that's all. That is machine learning. ChatGPT is that only.

### 03:07:55 · Speaker 4

But be honest

### 03:07:57 · Speaker 1

We will use multiple techniques to estimate p x given d yes

### 03:07:57 · Speaker 4

This is a good time to start this game

### 03:08:02 · Speaker 4

EX or PXY

### 03:08:04 · Speaker 1

It depends no in in unsupervised learning you could estimate p x y p x in supervised machine learning you estimate p x in fact in supervised machine learning you estimate p y given x I'll tell you next time you estimate the conditional distribution

### 03:08:16 · Speaker 4

Given given X

### 03:08:19 · Speaker 1

I'll tell you in the next class that gender given image

### 03:08:22 · Speaker 4

And okay because

### 03:08:25 · Speaker 4

Okay because these are sampled from those distributions we say that uh these they are kind of representative of the

### 03:08:33 · Speaker 4

Uh the the actual distribution

### 03:08:38 · Speaker 1

So they are actually sampled from the underlying distribution no they are they are completely sampled from the underlying distribution okay

### 03:08:45 · Speaker 4

Okay okay

### 03:08:46 · Speaker 1

Ah, but the problem is the one big problem with the statistics is, right, if when you are given samples from a distribution, how do you estimate the underlying distribution is the biggest problem in statistics. Giving samples from a distribution is not enough to estimate the com estimate completely the underlying distribution.

### 03:09:08 · Speaker 1

That is why, no, it is machine learning is heavily depend on the number of data points. The more the number of data points that we have from the distribution, the better our estimation will be. We will see all that in the next class. That is what I will do in the next class.

### 03:09:23 · Speaker 1

Okay that's because

### 03:09:23 · Speaker 4

That's because of either noise or maybe some something that we have not observed

### 03:09:26 · Speaker 1

something that we have not observed no no no no i don't call it noise or anything okay there's something called last last numbers i will describe all that in the next class

### 03:09:36 · Speaker 4

Okay yeah I think it's a

### 03:09:37 · Speaker 1

Yeah so basically from take home takeaway from this class is that when you have data you should start representing data right as

### 03:09:49 · Speaker 1

uh samples from the in space of uh elements from the in space of the random variable and when you when we say that there is a distribution associated with it you should know that it is the induced probability measure that is coming from coming through the random variable that is the biggest take home

### 03:10:09 · Speaker 1

Is that clear

### 03:10:11 · Speaker 1

Okay, let's stop here but you know I have a a couple of questions for you people let's maybe stop the recording

### 03:10:23 · Speaker 1

Yeah, people can leave any element in Y or rather every element in X. There is a certain probability associated with that belonging to one of these nine classes. Nine labels. Do you nine elements from other set? Do you see that? I mean, I will concretize these ideas in next class. Okay. But I want you to appreciate, right? I mean, the whole branch of this probability theory was was was conceived because you start with a random experiment, right? And you have this notion of probability.

### 03:10:53 · Speaker 1

associated with events now you deal with everything you model everything in terms of those random events and the and distribution functions right and you have that notion of uncertainty by construction

### 03:11:07 · Speaker 1

Is this clear? I'll continue from this in the next class while I take questions. I'll continue from this in the next class. I'll concretize these ideas. But yeah, you should understand how to represent data. Now, data is represented as samples drawn from, this is actually called, you know, samples drawn from a distribution. People also call this as data sampled from a distribution or samples data drawn from an underlying distribution. Okay. These are common words that are used.

### 03:11:37 · Speaker 1

Whenever you see that they are drawn from a distribution you will you should know the entire story. What's happening is that there is a random experiment you get sample space you get event spaces there is a random variable that is mapping this to real numbers and there is a probability measure assigned to the elements of sample space or rather elements of event space and therefore a distribution function gets induced.

### 03:12:03 · Speaker 1

Right? So when you say that the data is sampled from a distribution this is what it means

### 03:12:12 · Speaker 1

Uh yeah Prasanna

### 03:12:19 · Speaker 1

person but one

### 03:12:24 · Speaker 2

Can you hear me sir?

### 03:12:25 · Speaker 1

Yes I can hear you

### 03:12:27 · Speaker 2

Yeah, so in the last slide, I think you explained about x and y random variable function. So what is the relation between omega 1 and omega 2 here?

### 03:12:38 · Speaker 2

So don't mess with it

### 03:12:38 · Speaker 1

Yeah, there are two sets basically, right? I mean, there's no relation per se.

### 03:12:48 · Speaker 2

But whatever the

### 03:12:49 · Speaker 1

You can you can conceive you can talk of intersections and unions between those two elements that's all

### 03:12:58 · Speaker 1

Those two are the two sample spaces. I mean those two are samples, those two are sample spaces that would that would encompass the outcomes of these two random experiments. But these two random experiments are not independent, right? Quote unquote independent in the sense that they are connected.

### 03:13:16 · Speaker 2

Yeah images that you have taken like you will assign the number

### 03:13:16 · Speaker 1

That's true

### 03:13:20 · Speaker 2

So basically like

### 03:13:22 · Speaker 1

So you sample an image yeah you sample an image you sample a number as to associate them using unions and intersections

### 03:13:38 · Speaker 1

Uh yeah

### 03:13:40 · Speaker 4

Sir do we know this PX or PXY in this case

### 03:13:43 · Speaker 1

No, we don't. That's the whole problem in machine learning. The machine learning is if I have to summarize machine learning in one sentence, it is this given D, estimate P. X. That's all. That is machine learning. Chat GPT is that only.

### 03:14:00 · Speaker 4

To be honest

### 03:14:02 · Speaker 1

We will see what the depth needs to estimate PF given D yes

### 03:14:03 · Speaker 4

It was a good time to speak

### 03:14:07 · Speaker 4

EX or PXY

### 03:14:10 · Speaker 1

Depends, no, in unsupervised learning you estimate Pxy, Px. In supervised machine learning you estimate Px. In fact, in supervised machine learning you estimate Py given X. I'll tell you next time you estimate the conditional distribution.

### 03:14:21 · Speaker 4

Hey Mike

### 03:14:23 · Speaker 1

Give me a minute

### 03:14:23 · Speaker 4

Given X given Y okay

### 03:14:25 · Speaker 1

I'll tell you in the next class that gender given image

### 03:14:27 · Speaker 4

And uh okay because

### 03:14:31 · Speaker 4

Okay because these are sampled from those distributions we say that uh these they are kind of representative of the

### 03:14:39 · Speaker 4

Uh the the actual distribution

### 03:14:43 · Speaker 1

So they are actually separate from the underlying distribution no they are they are completely separate from the underlying distribution okay

### 03:14:50 · Speaker 4

Okay okay

### 03:14:51 · Speaker 1

Ah, but the problem is the one big problem with the statistics is, right, if when you are given samples from a distribution, how do you estimate the underlying distribution is the biggest problem in statistics. Giving samples from a distribution is not enough to estimate the com estimate completely the underlying distribution.

### 03:15:14 · Speaker 1

That is why you know it is machine learning is heavily depend on the number of data points. The more the number of data points that we have from the distribution, the better our estimation will be. We will see all that in the next class. That is what I will do in the next class.

### 03:15:28 · Speaker 1

Okay that's because

### 03:15:28 · Speaker 4

Okay that's because of either noise or maybe some something that we have not observed

### 03:15:32 · Speaker 1

something that we have not observed no no no no don't call it noise or anything okay there's something called last last numbers i will describe all that in the next class

### 03:15:41 · Speaker 4

Okay yeah I think it's a

### 03:15:43 · Speaker 1

yeah so basically the take out take away from this class is that when you have data you should start representing data right as as uh samples from the range space of uh elements from the range space of the random variable and when you when we say that there is a distribution associated with it you should know that it is the induced probability measure that is coming from coming through the random variable that is the biggest take home

### 03:16:14 · Speaker 1

Is that clear

### 03:16:16 · Speaker 1

Okay, let's stop here, but you know I have a a couple of questions for you people, let us maybe stop the recording

### 03:16:28 · Speaker 1

Yeah people can leave right
