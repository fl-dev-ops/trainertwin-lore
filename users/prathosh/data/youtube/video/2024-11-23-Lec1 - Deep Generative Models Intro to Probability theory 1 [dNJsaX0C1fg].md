---
id: dNJsaX0C1fg
title: Lec1 - Deep Generative Models Intro to Probability theory 1
url: https://www.youtube.com/watch?v=dNJsaX0C1fg
date: '2024-11-23'
duration: 03:07:23
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_0: Speaker 1
  speaker_1: Speaker 2
  speaker_2: Speaker 3
  speaker_3: Speaker 4
---

# Lec1 - Deep Generative Models Intro to Probability theory 1

## Transcript

### 00:00:02 · Speaker 1

A couple of logistic things uh the registration deadline is done right

### 00:00:11 · Speaker 2

No sir it extended till 20 X

### 00:00:13 · Speaker 1

They extend it

### 00:00:15 · Speaker 2

So you may s hit a century there

### 00:00:19 · Speaker 1

I don't want that

### 00:00:22 · Speaker 1

Okay so we still have the last class is not yet

### 00:00:28 · Speaker 1

Table is that way okay

### 00:00:32 · Speaker 1

Um okay

### 00:00:39 · Speaker 1

Okay anyway let's get started um so here is the plan for today

### 00:00:46 · Speaker 1

I'll start from some basics of probability theory

### 00:00:52 · Speaker 1

request is that all of you please mute unless you have a question or something even when you have a question

### 00:01:00 · Speaker 1

Since it's a very large class, let's maintain some sort of a decorum. Please raise your hand, of course, virtually. I'll call out your name and then we will discuss.

### 00:01:15 · Speaker 1

Please ask me questions otherwise you know it's it will become a very very boring monologue. First of all virtual classes are boring because I don't get to see students faces. On top of it if you don't talk it'll be double boring so we what I'll do is after like every 15 minutes or so right when I finish one particular concept I'll stop and ask for questions. Please if you have any questions you can ask me.

### 00:01:45 · Speaker 1

In the middle you can feel free to just raise your hand so that I can stop and ask address your questions

### 00:01:55 · Speaker 1

Okay, I hope that you have gotten access to my course notes and that feedback form that's out there and all that, right? So all the logistic issues are sorted out, I suppose.

### 00:02:09 · Speaker 1

No further questions there I think

### 00:02:13 · Speaker 1

The ends

### 00:02:40 · Speaker 1

will not uh

### 00:02:44 · Speaker 1

Automatize it is one note thing so struggling just a second now so where do I go to that class notebook okay got it

### 00:02:54 · Speaker 1

Welcome to one more okay

### 00:02:58 · Speaker 2

So you're not shading this

### 00:03:00 · Speaker 1

Read only to edit tap the one not icon where is the one not icon here this one No

### 00:03:16 · Speaker 1

Okay yeah if I share it you can help me perhaps

### 00:03:22 · Speaker 3

Will be on the top right side

### 00:03:24 · Speaker 1

Ah let me just see I think you're using some good notes

### 00:03:26 · Speaker 3

No

### 00:03:28 · Speaker 1

Share screen start broadcast

### 00:03:43 · Speaker 1

Here is it to edit tap one note icon

### 00:03:46 · Speaker 3

On the other hand

### 00:03:46 · Speaker 1

It is a dragon oh this one oh I see I see I see got it

### 00:03:48 · Speaker 3

Oh this one right there just behind you

### 00:03:51 · Speaker 1

Okay great thank you

### 00:03:55 · Speaker 1

So

### 00:03:59 · Speaker 1

So shall we have like uh one different page for every day I think let's do it that way

### 00:04:07 · Speaker 4

Yes uh that will be better

### 00:04:10 · Speaker 1

The date will always be here I suppose right I mean it will be Saturday August 10th it is so I'll have to delete this how do I delete this

### 00:04:26 · Speaker 1

This maybe we will rename this as

### 00:04:39 · Speaker 1

Oh

### 00:04:40 · Speaker 4

So within the file itself just mention the name of this page

### 00:04:45 · Speaker 1

Where if you can't

### 00:04:46 · Speaker 3

On top the title

### 00:04:46 · Speaker 4

Here on top the title Saturday Saturday 10 just above that mention this page title

### 00:04:51 · Speaker 1

So we'll do OCR now

### 00:04:54 · Speaker 3

Oh yeah yeah I think it does

### 00:04:58 · Speaker 1

It's a boat

### 00:04:59 · Speaker 3

So both will work both will work keyboard and OCR both

### 00:05:13 · Speaker 1

I need two three minutes for this pencil to be charged anyway so I'll write that so today's agenda is the following

### 00:05:21 · Speaker 1

I'll start with the basics of probability theory, the probability theory that we would need to continue in this course in the first half. The second half, I'll introduce you to the

### 00:05:38 · Speaker 1

generative models and formulate it if possible. So that is the agenda. Okay. So now the fundamental question that is to be asked is, right, you know that all of most of the machine learning, all of machine learning is based on this branch of mathematics called probability theory, right? Now the question is, why do we need it's actually a new paradigm. I mean, you meaning it's a

### 00:06:08 · Speaker 1

See, when you when we start as when we start studying mathematics, right, we have

### 00:06:14 · Speaker 1

We have numbers, we have counting and you know, we gradually learn calculus. So if you think about it historically, what was the need for calculus? Calculus had to be developed because you know, this idea of

### 00:06:32 · Speaker 1

rate of change of things and the idea of calculating the area under an arbitrary curve, right? That had to be, that was important. For instance, people like Newton, they wanted to find out what was the total distance covered by a moving body whose speed or velocity is plotted as a function of time. Now, there was no tool that time, okay, that could deal with such kind of question.

### 00:07:02 · Speaker 1

So he invented a new set of tools, right, which became a branch of mathematics called calculus, which was developed subsequently. So similarly, probability theory, right, statisticians had this had this question from a long time. The fundamental question is all machine learning is studied, right, or rather modeled from a probability theory perspective.

### 00:07:32 · Speaker 1

question is see it is not a false fit in the sense that people don't uh or rather people didn't come up with probability theory or rather apply probability theory because it was there it was not that the idea is that you cannot answer a few questions uh that you often encounter in uh in in machine learning or rather statistics if you do not have this uh tool called probability theory so that is the uh

### 00:08:02 · Speaker 1

the prologue. There's absolutely no way you can answer a few questions. See, just like you can't answer questions like, you know, suppose I draw an arbitrary curve, right, or rather I plot some measurement that I make, a speed measurement or something as a function of time. If I have to find out what is the total distance that was covered by this particle or a moving body, only when I have speed as a function of time. You can't answer that question if you don't have calculus, isn't it?

### 00:08:32 · Speaker 1

because you know you need the idea of like integration which is area under the curve otherwise you can't answer that question similarly there are questions uh that you can't answer if you if there is no uh if if if the tools of probability theory are not in place so so a lot of people tend to think right oh maybe you know it was a false word people talk of probabilistic machine learning because it is

### 00:09:02 · Speaker 1

it's just there etc it's not that it's a tool that is absolutely needed there is no other way to handle or rather answer a few questions uh that that arise without having this uh versatile tool of mathematics called probability here okay so that's uh i mean what i'll do today is that i'll try to convince you that what are the kind of questions that cannot be answered by any other branch of mathematics right you need to develop a special branch of mathematics

### 00:09:32 · Speaker 1

for probability theory and just develop some background there so that yeah sufficiently child no develop some background there so that we can i mean all of you already know this i'm sure but still just to get your memory and get up to the speed we'll do that

### 00:09:52 · Speaker 1

we will put ash

### 00:10:07 · Speaker 1

It doesn't seem to do a good job here

### 00:10:18 · Speaker 4

A keyboard will be better though yeah

### 00:10:21 · Speaker 4

A keyboard script will be better it will be more simple

### 00:10:27 · Speaker 1

You're saying you have to

### 00:10:30 · Speaker 1

Toggle the keyboard

### 00:10:58 · Speaker 1

Great

### 00:11:01 · Speaker 1

So this we will see in pro

### 00:11:11 · Speaker 1

Introduction to

### 00:11:20 · Speaker 3

So at the beginning can you put the lecture number as well

### 00:11:41 · Speaker 1

Okay so let's get started

### 00:11:54 · Speaker 1

Okay, so what is the, as I said, what are the kind of questions that we are interested in, in this statistical branch of statistical statistics for machine learning in this?

### 00:12:10 · Speaker 1

So fundamentally

### 00:12:22 · Speaker 1

most problems in science and engineering

### 00:12:30 · Speaker 1

Let's just go do this is the even I place my hand on top of my iPad no it's just going

### 00:12:40 · Speaker 1

Everybody's going to control that

### 00:12:47 · Speaker 1

You must

### 00:12:57 · Speaker 4

So you can enable the second last option right next to drawing mode

### 00:13:00 · Speaker 1

This one

### 00:13:03 · Speaker 1

What is this

### 00:13:05 · Speaker 4

So that will allow only the pencil to write

### 00:13:11 · Speaker 1

This palmajipal great thank you it should be there but I don't know where it is okay fundamentally most problems in in science and engineering

### 00:13:24 · Speaker 1

C I E N C E

### 00:13:34 · Speaker 1

Function approximations

### 00:13:46 · Speaker 1

So what do I mean by this? Most problems that you get in science and engineering are concerned about function approximation. So what are functions? So now the function

### 00:14:02 · Speaker 1

Basically a mapping right that is learned between function f is a mapping that is learned between two sets called a

### 00:14:14 · Speaker 1

Be right where

### 00:14:17 · Speaker 1

Here and we are sets

### 00:14:23 · Speaker 1

Okay, so it's a rule, it's a mapping, right, that would map one set to another set.

### 00:14:51 · Speaker 1

And generally

### 00:15:07 · Speaker 1

This set is called the domain

### 00:15:11 · Speaker 1

And this it is called the range

### 00:15:18 · Speaker 1

So there is a function it takes an element from the set called domain and maps it to another set called range. Okay, so now we'll take examples of functions You take some examples of functions. So let's say that there is a function. Okay that

### 00:15:38 · Speaker 1

takes element from real numbers okay and maps it to

### 00:15:45 · Speaker 1

real number so this is the function which maps real numbers to real numbers okay this r represent set of real numbers

### 00:16:04 · Speaker 1

of real numbers okay so this function maps set of real numbers to set of real numbers okay and you can take another example where

### 00:16:17 · Speaker 1

Effects

### 00:16:19 · Speaker 1

In fact to be precise here it actually maps

### 00:16:31 · Speaker 1

of real numbers to set of positive real numbers

### 00:16:38 · Speaker 1

So R plus this is set of reels

### 00:16:46 · Speaker 1

r plus is set of positive real numbers right so this is a function so you can think of any uh i mean lots of such examples right so another example can be that uh you can take modulus x okay similarly right so this is another this is another function that maps r to r plus similarly so these sets right they need not be r they can be anything so i'm going to carry on

### 00:17:16 · Speaker 1

Let's take another example where f of x is equal to

### 00:17:21 · Speaker 1

uh x transpose x okay now where x the domain right is

### 00:17:29 · Speaker 1

In some t dimensional real space. So, what do I mean by this? This is

### 00:17:42 · Speaker 1

Real and real vector

### 00:17:46 · Speaker 1

So what does this mean this means that you all are familiar about the

### 00:17:52 · Speaker 1

the Cartesian coordinates right so you know that every point in Cartesian coordinate I can give my call this x1 x2 every point in Cartesian coordinate can be represented by set of two real numbers right if you take a point here this point will be some x1 comma x2 this is another point x1 comma x2 x1 cap comma x2 cap etc and so on so this is this is typically represented as r2 right so these are these are actually called

### 00:18:26 · Speaker 1

This is a two dimensional

### 00:18:30 · Speaker 1

Euclidean space

### 00:18:32 · Speaker 1

The name after the mathematician Euclid okay

### 00:18:37 · Speaker 1

is called two-dimensional Euclidean space or vector space. Now similarly imagine a d-dimensional Euclidean space. So basically this is

### 00:18:51 · Speaker 1

It's still happening

### 00:18:53 · Speaker 1

When I place my hand it is taking me everywhere

### 00:19:07 · Speaker 4

if you're not comfortable we can switch to good notes also

### 00:19:11 · Speaker 1

It's okay, I I I can't really understand this. Uh, how do I get this?

### 00:19:18 · Speaker 1

I'm in this thing no no I don't want this

### 00:19:26 · Speaker 1

So this uh side pane will always be there is that I want this to disappear

### 00:19:31 · Speaker 4

Oh no you can remove it and here the settings icon the full screen button that should do

### 00:19:36 · Speaker 1

Where is it on

### 00:19:38 · Speaker 4

I'm not exactly sitting there

### 00:19:39 · Speaker 1

Sitting sitting okay

### 00:19:42 · Speaker 4

Uh next to it uh not in settings next to settings

### 00:19:46 · Speaker 1

This one oh yes full screen okay great

### 00:19:53 · Speaker 1

keep educating me okay with all this i've never used this uh like one note it's quite the issue i like get used to it no problem yeah i'm saying see this thing is a d dimensional real vector right so this is called in general this is called

### 00:20:11 · Speaker 1

E dimensional

### 00:20:18 · Speaker 1

Real space

### 00:20:20 · Speaker 1

So basically every point in this space is represented by a d-dimensional tuple where d is a positive real number, okay, z plus.

### 00:20:36 · Speaker 1

So now whenever I write this notation, right, I mean a d-dimensional real space. So it is the extension of the two-dimensional Cartesian space that you know of, right? A d-dimensional real space is simply

### 00:20:55 · Speaker 1

points in a d-dimensional real space are simply uh the simply the vectors right that are there in d dimensions every point in that d-dimensional space can be now represented uh using a double of d real numbers that's what i mean so now this function that i'm talking about uh which is f of x will give you x transpose x where transpose uh is uh you understand what transpose means right transpose up

### 00:21:25 · Speaker 1

operation of a vector. Now this is a function that maps

### 00:21:31 · Speaker 1

R D 2

### 00:21:35 · Speaker 1

r plus not in that part can be negative as well so it maps rd to r okay so this function uh takes as input a d dimensional real vector and gives out a real number so that is a function that would take a d dimensional vector to a real number and so on so i mean you can think of these things right there are multiple examples of what functions constitute and as i said most problems

### 00:22:05 · Speaker 1

Science and engineering are the following that given.

### 00:22:13 · Speaker 1

Give him

### 00:22:18 · Speaker 1

Yes

### 00:22:28 · Speaker 1

I cannot see it that way

### 00:22:35 · Speaker 1

Maybe I'll define it in a formal way

### 00:22:45 · Speaker 1

Suppose

### 00:22:50 · Speaker 1

Capital A and capital B denote

### 00:22:59 · Speaker 1

E domain and the rain set

### 00:23:12 · Speaker 1

domain and array set now suppose you're also given given given

### 00:23:22 · Speaker 1

That is

### 00:23:31 · Speaker 1

of elements

### 00:23:37 · Speaker 1

X I comma Y I

### 00:23:42 · Speaker 1

Subscript

### 00:23:44 · Speaker 1

Now excite so let's say that you know these are

### 00:23:50 · Speaker 1

in such points Xi

### 00:23:53 · Speaker 1

is an element from A and Yi is an element from

### 00:24:08 · Speaker 1

This we are to say suppose the NP denote the domain and the inset of

### 00:24:15 · Speaker 1

function

### 00:24:18 · Speaker 1

for function f

### 00:24:22 · Speaker 1

Okay, that takes an element from A and maps it to elements in B. So given pairs of elements Xi, Yi such that Xi is in A and Yi, comma, B, the question or the problem, problem.

### 00:24:37 · Speaker 1

is to find

### 00:24:40 · Speaker 1

D

### 00:24:46 · Speaker 1

underlying function

### 00:24:52 · Speaker 1

Okay so this has been a problem of interest uh for

### 00:25:00 · Speaker 1

It's okay. This has been a problem of interest for scientists and engineering engineers from time time immemorial. So this so if you have given some n elements, these are you can also call these as observations.

### 00:25:18 · Speaker 1

Qualities as observations or data or whatever, right? We are given this.

### 00:25:26 · Speaker 1

to find the underlying function f so now why is this important suppose you find the underlying function what is the what is the use of finding out that underlying function is that let me give you examples perhaps example is

### 00:25:39 · Speaker 1

Now let's say A

### 00:25:44 · Speaker 1

set of positions

### 00:25:52 · Speaker 1

A planet in the sky

### 00:26:03 · Speaker 1

By position I mean the coordinates

### 00:26:20 · Speaker 1

No, I'll this might confuse you a little. Let's not take that example. Let's let me take the example next. The first example that I can take is

### 00:26:35 · Speaker 1

So it's an acceleration

### 00:26:41 · Speaker 1

of a body

### 00:26:46 · Speaker 1

So B can be

### 00:26:51 · Speaker 1

Holes exerted on it

### 00:27:00 · Speaker 1

Okay, so suppose I give you, I measure acceleration of a particular moving body and I also give you what was the force that was exerted on it. So the task is to find out how are these two sets related, right? The set of force exerted on it and the acceleration that the body undergoes, right? I mean, how are they related? Okay, so this was actually the question that was

### 00:27:32 · Speaker 1

That was asked by uh right do you know how are they related these two things

### 00:27:42 · Speaker 3

I think that's acceleration

### 00:27:44 · Speaker 1

set they are linearly related right so now the let's if i call the acceleration of a body denoted by a which is a scalar so note that set a here is set of real numbers because in fact positive real numbers acceleration cannot be negative and

### 00:28:08 · Speaker 1

be negative right because also has a direction of say force can also be negative so yeah so force exerted on it is another real number and they are

### 00:28:20 · Speaker 1

but denote this by f then the relationship between these two as you know as a linear relationship is simply given by uh i mean the proportionality constant is the mass so you simply have the the force is related to acceleration it is proportional to acceleration and the proportionality constant is the mass now as i said right i mean this was why do we need this is just one example the i i i

### 00:28:50 · Speaker 1

Take questions in a while, okay? So the algorithm to think of another example.

### 00:28:59 · Speaker 1

Somebody give me an example of a case where the function is not linear

### 00:29:17 · Speaker 3

I'm not even

### 00:29:17 · Speaker 4

I'm not even

### 00:29:18 · Speaker 2

And it's kind of

### 00:29:19 · Speaker 1

Okay

### 00:29:19 · Speaker 3

Yeah yeah yeah

### 00:29:25 · Speaker 1

Okay how are they related kinetic energy and velocity

### 00:29:33 · Speaker 1

uh velocity is v and energy is p okay we can do that

### 00:29:40 · Speaker 1

So day is

### 00:29:46 · Speaker 1

capacity in B's energy

### 00:29:51 · Speaker 1

So there the relationship is

### 00:30:00 · Speaker 1

so on right i mean now you get the point now uh here right i mean uh a lot of scientists and engineers they wanted to figure out this relationship right i mean a lot of research that people were doing was focused on finding out the relationship between

### 00:30:20 · Speaker 1

measurements that I have done and these measurements are represented as the elements of sets. So mathematically speaking as I said let me look at my initial statement I said that most problems in science and engineering are function approximations. What I need to say is that suppose there are two A and B are two sets which are the domain and range sets of a function and if you are given elements which are which are pairs from these two sets

### 00:30:50 · Speaker 1

the underlying problem is to find out or identify what the underlying function is that relates elements of A to elements of B. Now, why is this question important? The next thing is what do we get if we approximate the underlying function? Okay, so now function approximation.

### 00:31:15 · Speaker 1

Somebody tell me why is that important? Why do you have to relate quantities measured quantities?

### 00:31:25 · Speaker 4

predictions

### 00:31:27 · Speaker 1

Exactly right, so one one of the things is function approximations

### 00:31:39 · Speaker 1

Approximation okay enables predictions

### 00:31:45 · Speaker 1

So what do you mean by prediction So we have to define this right So prediction mathematically

### 00:31:52 · Speaker 1

simple prediction as

### 00:31:58 · Speaker 1

Fine

### 00:32:02 · Speaker 1

element

### 00:32:06 · Speaker 1

In set B which is the range set range set

### 00:32:14 · Speaker 1

corresponding to

### 00:32:21 · Speaker 1

Any element in it

### 00:32:26 · Speaker 1

I might end the domain

### 00:32:32 · Speaker 1

This is important, right? So now if you look at it, the data of the observations that we have done, okay, is there a pointer here somewhere like without writing, can I just point to things?

### 00:32:47 · Speaker 1

But in good notes it used to be there highlighter is there I don't need highlighter like a cursor or a pointer of sorts do you know anybody knows

### 00:33:02 · Speaker 1

See what I want to do is I simply want to like show this right just highlight on this I keep doing this because when I write something I go back and just show that is there something of that sort here

### 00:33:17 · Speaker 1

Textual orientation

### 00:33:24 · Speaker 1

Does anybody know that no

### 00:33:28 · Speaker 4

So there is no pointer

### 00:33:30 · Speaker 1

There's no black to here

### 00:33:31 · Speaker 4

No you can maybe use the assistive touch button on the right side to

### 00:33:35 · Speaker 2

of circle around things but that's about it

### 00:33:39 · Speaker 1

I see but it's just there we go I mean I don't want that to stay I just want to point out to that thing yeah somebody

### 00:33:46 · Speaker 4

Yeah somebody should use NS pointer if you click on the pen itself

### 00:33:53 · Speaker 1

Meaning I didn't read that

### 00:33:55 · Speaker 4

And if you click on it then I guess you're supposed to get some menu

### 00:34:03 · Speaker 1

But this one's not

### 00:34:06 · Speaker 4

no I mean I'm gonna on the pen itself like the whatever you have it highlighted

### 00:34:13 · Speaker 4

If you happen to click it again

### 00:34:22 · Speaker 4

Do you see any options on top Can you click and hold that pen once

### 00:34:34 · Speaker 1

Nothing happens

### 00:34:37 · Speaker 1

Anyway, so find it out. I mean, if anyone of you want to find that out, let me know or just tell Microsoft to have that feature in the next version. It's very, very useful. For example, I'll show you in good notes.

### 00:34:59 · Speaker 1

It was that was just thing you see

### 00:35:03 · Speaker 1

so nice

### 00:35:06 · Speaker 1

just go with it so if there is something that i write i can go back and you know just mark this and talk about this and it was very very useful for me you see that red mark here it is not there at all

### 00:35:22 · Speaker 3

If you go back to the pen gallery I think there is an option

### 00:35:26 · Speaker 1

He's dead okay

### 00:35:27 · Speaker 3

So there is a plus button next to the pans right

### 00:35:33 · Speaker 1

I like that

### 00:35:36 · Speaker 3

Select the pen mode

### 00:35:37 · Speaker 2

It says that

### 00:35:38 · Speaker 3

To use pen as a pointer I don't know where to get this

### 00:35:51 · Speaker 1

Fine okay fine whatever so I'll have to maybe just go back it's not very optimal because I keep using this pointer so many times while I was teaching it was very useful for me

### 00:36:04 · Speaker 1

And okay

### 00:36:05 · Speaker 3

You can use the other

### 00:36:09 · Speaker 1

Well that's also fine that's what I was doing but uh people suggested this one also and I just thought that it's okay

### 00:36:21 · Speaker 1

Okay, no problem, let's move on. Yeah, so what I was saying is that you are

### 00:36:31 · Speaker 1

still okay right i can just point it here and these some of these things will become yellow colored i think it's fine but when you are looking at the notes you notes you should just ignore these yellow colors because they only mean that while teaching i've pointed out to them that's all okay anyway so let's try to do that i mean they are not i mean they are no way they are important or whatever right they just simply mean that while teaching i just pointed to those things and came back

### 00:37:01 · Speaker 1

If that is okay, I can continue with this. Just use this thing and highlight it. Okay. Anyway, so what I was saying is, why do you need function approximations is that while you have observations and data for about n points, you have made n observations, we are often interested in understanding how the system behaves beyond these n observations that we have made. Otherwise, we have made those n observations, there is no need.

### 00:37:31 · Speaker 1

in in those uh scenarios but we need to know what happens beyond the observations right so that is what we call as prediction prediction is basically you find the element in range right find the element in the range set

### 00:37:49 · Speaker 1

the range set corresponding to any element in the domain so given any element in the domain you need to understand how the range set uh how uh what what element in the range set does it get mapped to and that is what is called as prediction so here what you are doing is given a particular angle correction that was not observed if i want to know what the corresponding force is then if you find that underlying function then you can find out what the force is

### 00:38:19 · Speaker 1

Similarly with this velocity and energy, right? And if you are given a particular velocity, if I want to know what was the energy that was exerted on it, I can just use this function and find out what it is. That is one of the most important applications of why one needs a function approximation. That all, as I said, all problems in science and engineering are about predicting this, okay?

### 00:38:43 · Speaker 1

Right uh any questions so far show points

### 00:38:53 · Speaker 1

Yes

### 00:38:56 · Speaker 4

So is this also called as inverse problem that that we talk about

### 00:39:01 · Speaker 1

Yeah you can call it a use problem better

### 00:39:05 · Speaker 1

See I'm actually going to you know pair basics of stuff I'm sure that all of you know this already but yeah so I want to call it from an approximation given these pairs of observations and data rather observations from two particular sets I want to understand what the inverse problem is yes of course it is inverse problem see it's not quite the inverse problem because in typical inverse problems what happens is you only have access to output without having access to input

### 00:39:35 · Speaker 1

Or rather you don't have elements of range set at all. Sorry, domain set at all in inverse problem. So that's why we are called inverse problems. And here you have access to pairs from both the domain and range. You get it? That's how they are different.

### 00:39:51 · Speaker 1

Okay uh Regit

### 00:39:52 · Speaker 4

Sir one question I have why do you use this word approximation

### 00:39:57 · Speaker 1

Commission is this I

### 00:40:00 · Speaker 1

Fine

### 00:40:02 · Speaker 1

Please stop writing

### 00:40:02 · Speaker 4

Why do you have this

### 00:40:04 · Speaker 1

No who is talking

### 00:40:04 · Speaker 4

I'm not a surgeon

### 00:40:06 · Speaker 1

See, we have a bit of rule in this class that if you want to talk, please raise your hands because otherwise, no, too many people, it becomes a bit chaotic. Please raise your hands. I'll call out your name and you can ask questions. Okay, thank you. Yeah, I'll come. I'll go in the order. Arjit?

### 00:40:28 · Speaker 2

Sir, one question that till now whatever a function relation we saw between two elements is like kind of a proportional light being it linear or non-linear. So one is increasing, other is increasing or inversely proportional also. But suppose the relationship is very complex. For example, if it is too cold, I may not go out. If it is little hot, I will go out. But if it is too hot, again I will come back to my home, right? So this kind of relation where you cannot directly make it proportional or inversely proportional.

### 00:40:58 · Speaker 2

So how our I mean this prediction will work there I mean generative model maybe too early to ask this just asking

### 00:41:07 · Speaker 1

Good question, very good question. And yes, you see, that is why we need other mathematical tools. The linearity or proportionality doesn't work. See, for instance, suppose you need to, suppose you just measure the, let's say that you measure the temperature, you just heat a body, okay, you just heat a metal and measure the temperature of that metal at different points along the material. Now, if you want to ask me this question,

### 00:41:37 · Speaker 1

that if I measure temperature at one point okay I need to know how the temperature varies across the body you know how do you model it you measure temperatures I want to know what the temperatures are at other points in the body as well given some heat now you can't there is no way that you can write it as a linear equation you have to express that as a differential equation isn't it right so that's why you need another branch of mathematics right which is differential calculus and you need to express it as differential equation but the kind of question that you are asking

### 00:42:07 · Speaker 1

is the same now that if I can measure if I have measured the uh the the temperature of a body at certain points now if I if I give you the properties of that body right and uh the uh the initial conditions if I have to know the temperature the body is at a different uh location of the body then there is you need to model it as a differential equation so what I'm trying to say is of course the point that you brought up is very uh relevant that's what I'll move on to again so there are

### 00:42:37 · Speaker 1

questions that cannot be answered uh with with with these kinds of things right these kinds of existing mathematical tools and that's why you need new branches of mathematics and probability theory is not such so i will give you examples uh example scenarios and questions that cannot be answered using the existing mathematical tools and that's why i motivate why probability theory is needed in its absolute necessity yeah

### 00:43:06 · Speaker 1

Okay uh Pat

### 00:43:09 · Speaker 4

So my question is more about the terminology. So we are using the word prediction here. And from what we study in probability predictions, it's about an estimation of numbers, right? But in this case functions, we are mostly talking about absolute values and we're getting absolute answers. So why is the word prediction and approximation being used here?

### 00:43:30 · Speaker 1

Okay, see that's a definition, right? I mean, people use different terminology for different things, right? I am using this word prediction. That's why I define whenever I use a term, I define what it is. To me, prediction here is simply finding an element in the range corresponding to any element in the domain. In fact, even in statistics and probability theory, when we talk of prediction, we actually are evaluating a particular function at a point. I will talk about it in a while. Okay, so,

### 00:44:00 · Speaker 1

We are not, there's no, I mean, there's no quote unquote uncertainty, right? We'll discuss all that in a while, right? I mean, probability theories are very, uh,

### 00:44:13 · Speaker 1

What should I say? It's a it's a lot of misnomers and a lot of misunderstanding, right? I mean, people use terms right right left and center. Even there in probability theory prediction refers to evaluating a function, a particular function at a point. We'll talk about it in a while.

### 00:44:33 · Speaker 1

okay uh anything else any other question uh this i don't see any hands raised so we'll perhaps move on now as uh uh like arjit was asking right so the problem here is the following

### 00:44:51 · Speaker 1

Or others

### 00:45:03 · Speaker 1

Now what if

### 00:45:07 · Speaker 1

A mapping between the range

### 00:45:13 · Speaker 1

Between the sets

### 00:45:18 · Speaker 1

Cannot be found out

### 00:45:24 · Speaker 1

using

### 00:45:27 · Speaker 1

Existing mathematical tools

### 00:45:35 · Speaker 1

See, as uh, like he was pointing out, right, okay, you know, in fact, as I said, you can take another example perhaps right here, in fact, you can write this as

### 00:45:47 · Speaker 1

problematic

### 00:45:51 · Speaker 1

Breaks the flow and makes the glass up

### 00:45:54 · Speaker 1

What the hell boy

### 00:45:57 · Speaker 1

What happened is how do I

### 00:46:12 · Speaker 1

This can be written as you know that this is

### 00:46:17 · Speaker 1

The derivative of

### 00:46:22 · Speaker 1

derivative of the position

### 00:46:30 · Speaker 1

respect to time

### 00:46:34 · Speaker 1

because acceleration has to be measured and you had calculus so you can represent that as the the rate of change of t t squared

### 00:46:45 · Speaker 1

you can represent that as the double derivative of the position right with respect to time now the problem is as he was pointing out if the relationship between the elements of range and the the domain if there's if you cannot find out if they cannot if you cannot find the functions you can't rather express those relationships using existing mathematical tools what do you do the solution this is just just as

### 00:47:15 · Speaker 1

gave you the exam today the calculus was uh

### 00:47:19 · Speaker 1

was discovered so to come up with new mathematical tools

### 00:47:31 · Speaker 1

So this is how right probability theory is motivated that specifically for probability theory the problem is what happens is

### 00:47:42 · Speaker 1

you formal definitions of all this. So the motivation for probability theory is the following that what happens is the

### 00:47:52 · Speaker 1

The relations between sets to be relations to be

### 00:47:56 · Speaker 1

be approximated or rather relations to be found out

### 00:48:06 · Speaker 1

A complex what do I mean by complex is that

### 00:48:12 · Speaker 1

Do not adhere to existing do not adhere within the existing mathematical framework okay

### 00:48:26 · Speaker 1

mathematical framework. Now, if this happens, then you need to come up with new way of modeling things or a new way of expressing things. That's why probability theory becomes handy. Let me give you an example. I'll also tell you what is the fundamental idea behind probability theory. So example is, now suppose I'm given, let's take any ML problem, right? So elements

### 00:49:03 · Speaker 1

Let me not make it uh redundant

### 00:49:08 · Speaker 1

I'm given images okay pictures let me call it as pictures this is I'm not going deep into math yet so let's say that I'm given pictures so I have to learn relationship between set of pictures right and

### 00:49:31 · Speaker 1

The idea of uh

### 00:49:34 · Speaker 1

gender okay so this set typically right when how do you represent a picture uh in a in a in a in a in a computer is that you write that as a r p cross q basically it's a grid of numbers right what is a picture what is an image basically it's a grid of numbers you have p rows and q columns everything is a real number here right

### 00:50:01 · Speaker 1

So you have p cross q real numbers. That's how you represent a picture. Now every picture is an element.

### 00:50:10 · Speaker 1

in a p cross q dimensional real space. So you should imagine that just like we have the Cartesian plane, right, which is two dimensional, there is a p cross q dimensional space. And in the p cross q dimensional space, every image now becomes a number. Every picture becomes a point, basically. Okay, not a number, I'm sorry. It's a point. Now what I need is, given this, I'll have to predict, right? When you remember what the definition of our prediction is, I define prediction as finding out the

### 00:50:40 · Speaker 1

element in the range set corresponding to any element in the domain. So now this gender is a set a discrete set of two values.

### 00:50:52 · Speaker 1

Let's assume that it's a discrete set of two values. Now, given this picture, I need to find a function, okay, that will take an element in

### 00:51:01 · Speaker 1

P cross Q dimensional space, which is a vector, and maps it to

### 00:51:11 · Speaker 1

Okay one of the two discrete numbers 0 and 1 think about it

### 00:51:17 · Speaker 1

Now remember how these picture was taken, okay, rather obtained. How are these P cross Q numbers obtained? Now what is happening in the background is the following that some person is standing, okay, standing or sitting or whatever. Now you have a sensor, okay, which we call as camera. Now what light falls on that person, okay, and reflects some electromagnetic radiations back.

### 00:51:47 · Speaker 1

are sensed or captured by the sensor and what happens in the sensor is that there is a voltage or current chain that happens and that is what is recorded as a real number here correct that is what a picture is and you know these grids correspond to different spatial locations of the object

### 00:52:05 · Speaker 1

So what is that we are trying to do here if you imagine we want to relate okay the amount of light that a particular position

### 00:52:18 · Speaker 1

reflects okay to an idea called gender

### 00:52:24 · Speaker 1

You see what's happening

### 00:52:28 · Speaker 1

It is very, very abstract in the sense that see here what happened is that in all the examples that we gave, force was measurable, acceleration was measurable, energy was measurable, velocity was measurable and so on. But here what is being measured is the amount of reflectance that a particular surface is giving you. What you want to relate it to is an abstract idea and a non-measurable idea called gender.

### 00:52:59 · Speaker 1

Do you appreciate the difficulty in what we are trying to do? Of course, right? I mean, this can be gender or this can be, let's say, if a person is beautiful or not. I mean, these are, I keep making this philosophical statement that nature is very simple, right? I mean, if you, if you want to fly an aircraft, which is a very complex task, all you need is, you know, first order differential equations and Newtonian laws. That's all. Okay? To do things like things that are as complex as

### 00:53:29 · Speaker 1

flying an aircraft. But to find out right whether somebody is a male or a female from a picture you need a billion parameter model.

### 00:53:40 · Speaker 1

See, by the way, look at this. How many parameters that this model has? I have not defined what a model is yet, but still this F equal to MA, how many parameters does this have? Can somebody tell me?

### 00:53:55 · Speaker 2

Two point three

### 00:53:55 · Speaker 1

One three one it has one parameter m is the only one parameter that it has

### 00:53:57 · Speaker 2

One second

### 00:54:02 · Speaker 1

And the other example that we saw is also one single parameter model. Or if you take a second order differential equation or a third order differential equation, all it has are three, four parameters. So as I said, to explain nature of, you only need two, three parameter models. But to understand and predict things that human beings constructed, you need billions of parameters. It only shows how complicated we are as human beings. I'll give you another example for that. Let's say that you have a document.

### 00:54:35 · Speaker 1

These are the typical day to day ML problems that we solve, right? You have a document.

### 00:54:44 · Speaker 1

And what you need is the idea of emotion.

### 00:54:52 · Speaker 1

Right. So what's a document? Document is collection of written tokens. Okay. So we'll talk about all this. What is tokenization, et cetera, and all that. You can think of these as collection of words.

### 00:55:06 · Speaker 1

k words okay all these words are are represented as vectors okay each of them has a each of them is represented by let's say a d dimensional vector

### 00:55:20 · Speaker 1

Which means that this entire document now will become a point in a D cross K dimensional space. Every document is an element or a vector in a D cross K dimensional space. What you need is a function that will take an element from D cross K dimensional space, which is a document, and maps it to, let's say, that this emotion. So there are five emotions, right?

### 00:55:50 · Speaker 1

I'm angry

### 00:55:53 · Speaker 1

Happy

### 00:55:56 · Speaker 1

whatever right so represent that as 0 1 2 etc so it just maps it to some discrete set of 0 1 2 3 4 okay so this is what we need so what do we do i mean the so-called inference that we do right is nothing but prediction what is prediction here given this particular function if you are given any element from this uh uh from the domain set you want to map it to uh the element any corresponding element in the range set that is what has to be done now you know that right i mean this is what

### 00:56:26 · Speaker 1

things like chat gbt etc do where you can't uh find the relationship what is emotion i mean like what is the positive emotion for you can be a negative emotion for me and vice versa so this i this idea of emotion is it is very very synthetic and man-made okay so to understand how again if you go back to what how these vectors were created okay if you take some uh uh like you know embedding like tf-idf which is a very

### 00:56:56 · Speaker 1

way of looking at expressing words which is simply counting the number of times every word has occurred keeping a dictionary right how is that related to a a concept called emotion which is which is a very very you know abstract concept

### 00:57:13 · Speaker 1

Okay, so now the problem is that because we are dealing with the relationship that are complex. Now, what do I mean by complex? Complex means that they do not adhere to existing math. I cannot find the linear relationship or a quadratic relationship or a differential equation or a relationship that can be modeled using a differential equation that would relate these reflectances that a surface will give to an idea called gender. Or rather, it can also, I mean, you can think of it all

### 00:57:43 · Speaker 1

the problems that you do in ML right I mean take a picture and do a person re-identification where you identify what the person is and then you can talk of any of those things which are

### 00:57:55 · Speaker 1

which cannot be modeled using existing mathematical tools

### 00:57:59 · Speaker 1

Okay, so that's the motivation, right? You know, why do you need a new mathematical paradigm is because these functions that we are trying to approximate or find are such that they cannot be found out using existing mathematical techniques. In fact, let me tell you something. When people were doing pattern recognition using non-statistical methods, people were actually looking at coming up with these kinds of functions, right?

### 00:58:29 · Speaker 1

tools okay that would that would enable them to to relate these kinds of vectors to these kinds of elements let me give you an example for that let me take another example

### 00:58:50 · Speaker 1

So I I'll take questions little bit just hold on

### 00:58:55 · Speaker 1

Another example let's say that you have a speech signal

### 00:59:01 · Speaker 1

Okay, what you want is set of phonemes.

### 00:59:08 · Speaker 1

So what are these phonemes I'm talking about this uh a ba right off

### 00:59:15 · Speaker 1

and all these things see uh note that phonemes see what is the commonality in all this commonality in all this is that the range set let me just tell you this the range set okay

### 00:59:33 · Speaker 1

is non-maintenable

### 00:59:38 · Speaker 1

It is not measurable right or rather I'll call this as abstract

### 00:59:44 · Speaker 1

So the idea of phoneme, right? So what is happening just like in the document and the the picture example, what is happening in the speech example is that what is that you are doing? So there is a microphone. Okay. Let's say that there is a speech signal.

### 01:00:02 · Speaker 1

is a speech signal okay so what is the speech signal so i'm talking what do i when i talk there is a change of pressure atmospheric pressure that is that is happening okay uh because when i change the air comes out of my mouth with a particular type of constriction from my vocal apparatus and there is a change in pressure in the environment and there is a there is a sensor which is called a microphone which is a condenser based sensor that is measuring the rate of change

### 01:00:32 · Speaker 1

of pressure as a function of time and this thing that we that we measured right and that is converting this sensor transducer is converting the rate of change of pressure atmospheric pressure into voltage and this is what you measure as speed signal so this is time this is the speed signal okay it's a one-dimensional signal so this is nothing but the rate of change of uh voltage as a function of time and the rate of change of voltage happen because there is a change of pressure that is happening as a function

### 01:01:02 · Speaker 1

time okay now tell me that uh function so then again you can represent that using multiple things you know one way to represent that is just uh speech signal is a continuous signal right just uh chunk it just like you do it you tokenize a document you chunk the speech signal into parts and you represent that as some like uh some p-dimensional vector it's a it's a p-dimensional vector now what you need to do is you need to learn a function

### 01:01:32 · Speaker 1

that would take a p dimensional vector which would represent the rate of change of pressure atmospheric pressure as a function of time and you need to map it to an abstract idea called phoneme now why is phoneme an abstract idea so what is r the sound r is very abstract right it's it's only a perception based idea you know you can't measure r but you can measure this rate of change of uh pressure as a function of time now you need to relate rate of change of

### 01:02:02 · Speaker 1

uh pressure right as a function of time to an abstract idea called falling which is not measurable

### 01:02:10 · Speaker 1

Understand everywhere the same thing is happening right so the rain is non measurable but the domain can be measured

### 01:02:25 · Speaker 1

Okay, so in these set of scenarios, where you have measurable domain sets and abstract range sets, finding out a function that would map these two via existing mathematical tools is difficult. But as I said, historically speaking, people tried using existing mathematical machinery to solve these problems. Okay, so I'll tell you, historically,

### 01:03:01 · Speaker 1

Attempts were made

### 01:03:04 · Speaker 1

EMPDS attempts were made

### 01:03:11 · Speaker 1

to learn such functions

### 01:03:17 · Speaker 1

using classical tools let me say it

### 01:03:27 · Speaker 1

Let me give you an example for it. Let's take the example of speech, let's say, right? So the problem is that set of speech signal two, we need to get into frame, right? That's how that that's

### 01:03:40 · Speaker 1

That is what our goal is. So you know what people did? So they took the speech signal, okay? They modeled speech signal, right? As basically you model speech signal as a linear or a non-linear system, a non-linear system. This has some input, okay? And this is the system, an LTI system. You can either make it linear or non-linear. Let's say that it's a linear system. And what do you get by

### 01:04:10 · Speaker 1

is the speed signal

### 01:04:16 · Speaker 1

mischief. Okay, so this is the input to that system and this is the speed signal that you observe.

### 01:04:25 · Speaker 1

Now what they did is all you can measure is this the speed signal right this particular speed signal they say that there is an abstract input which is the phoneme the idea of phoneme

### 01:04:37 · Speaker 1

that person thinks

### 01:04:40 · Speaker 1

goes as an input to the system and this system converts that into something that is measurable which is called a speech signal. Now if they want to you know find that underlying function okay that would see remember that we are interested in finding out the relationship between speech signal and the phoneme not the other way around. Now what they do is they model the entire procedure right using some system okay uh and then they cast it as an inverse problem that is where

### 01:05:10 · Speaker 1

inverse problem comes into picture that the problem is given the speech signal find out what the underlying for e is so now how do they do that they do it by modeling this entire system using existing math you know for instance the speech community was modeling this entire system as as differential equations

### 01:05:32 · Speaker 1

find its parameters you know there are lots of parameter estimation techniques so basically they cast this problem as okay i've given i'm given some speech signal let me try to uh use some physics of the problem and try to estimate what the entropy system is such that if i'm given a speech signal i can go back to that abstract concept called phoneme so you can see a similar thing with the images also right i mean the the classical image processing people if they wanted to find out

### 01:06:02 · Speaker 1

gender okay uh from an image so what they did what they used to do is and let me take that another example of image right so you have image

### 01:06:12 · Speaker 1

to let's say object identity okay so what sort of an object is it is what I need to find out

### 01:06:20 · Speaker 1

Given the image so what do you do is that take the image okay so now model object identity as

### 01:06:27 · Speaker 1

Let's say it's a house

### 01:06:31 · Speaker 1

If I see a rectangle

### 01:06:33 · Speaker 1

There's a triangle at the top, okay? And then you know some regular objects.

### 01:06:41 · Speaker 1

Other shapes

### 01:06:43 · Speaker 1

so on so what do I do I come up with the processing methods right that would

### 01:06:49 · Speaker 1

So basically what happens is this there's this function so this function that they do is they first find out

### 01:07:00 · Speaker 1

rectangle extractor there is something called you know just extract the rectangle and see where is it and then you do a a triangle extraction

### 01:07:11 · Speaker 1

Then you have some sort of you know uh

### 01:07:16 · Speaker 1

Object location detection

### 01:07:20 · Speaker 1

and so on and try to do this and combine all this to come up with some object identity or regular shape. Now that is how people used to attend these problems. This is like, this is like, as I said, this is classical speed processing. This is classical email processing and you can imagine the same thing, right? You know, in LP also. You have documents to, you need spam or no spam. Email spam or no spam problem, right? So what people used to do is, you know,

### 01:07:50 · Speaker 1

Just identify some spam words

### 01:07:55 · Speaker 1

Okay so this count the frequency

### 01:08:00 · Speaker 1

of spam words and so on so now you do this and try to find a relationship between the span number of spam spam words and the the frequency of occurrence and that position etc and then mark it to some identity so you understood right so basically if i have to track trace back to what what we discussed so far what we are actually interested in is given pairs of uh observations or elements from two particular sets we are interested in finding out what the

### 01:08:30 · Speaker 1

underlying relationship between the elements of those two sets are okay now in classical uh uh settings uh where the relationship between them can be can be uh estimated using existing mathematical tools now you can try to find out uh how the relationships are i mean don't ask me how to do it i mean that's a that's an entire entire branch in mathematics by itself but you can do it but now the problem arises where

### 01:09:00 · Speaker 1

the the relation or the function that we are trying to learn between the domain and and range do not adhere with the existing mathematical tools okay now i gave you examples of this machine learning so why why does this happen this happens typically where the elements of the domain set are measurable okay and observed but the elements of the range set okay are very abstract and they are not measurable things so now how do you solve such problems is the question as i said classically what people use

### 01:09:30 · Speaker 1

to do is to try to use existing mathematical techniques and then find that relationship but unfortunately all these attempts right I mean uh before people started uh using the probability theory or statistics as a tool to model these relations none of these things were usable right I mean you didn't have a good speech recognition system you didn't have uh an image recognition system didn't have a good NLP system because all the techniques that were there were simply

### 01:10:00 · Speaker 1

Estimating the wrong functions that's all

### 01:10:03 · Speaker 1

Okay, none of the functions that you estimate, so now what happens if you have a, make suppose you have this particular

### 01:10:11 · Speaker 1

way to find out what a house is right so what if you have a house which is a modern building right that does not have a triangle at the top something like this what do you do it what if it is going in similar questions can be asked for every system here a speech signal suppose you model something you know somebody comes and the the the voice changes uh you model you have modeled it for one particular type of population and the accent changes so what happens you know those systems are failing there because the

### 01:10:41 · Speaker 1

underlying function approximation that we have done there the right link function that they have identified using these methods are not

### 01:10:54 · Speaker 1

So this is the thing right so now I think you know I this is I've convinced you enough uh in in in

### 01:11:04 · Speaker 1

appreciating the fact that you need uh with the existing mathematical tools do not do not work out you need another uh maybe a way or branch of mathematics right which would uh which would try to address these kinds of problems where you still want to approximate functions between two sets but the relationship between the domain and the range do not adhere to existing tools number one the second thing is that the uh the uh domain

### 01:11:34 · Speaker 1

is often measured the range set is not measured not measurable it's it's a it's a very abstract idea now how do you solve these problems is the question and that's why probability theory or statistics becomes extremely uh relevant i'll tell you what is the underlying paradigm of solving these problems uh in in in uh from a probability theory perspective in a while okay so i'll stop here for a while and take questions um

### 01:12:02 · Speaker 4

Yes, the example which you just gave that using traditional techniques like suppose, you know, the speech example which you gave that suppose it has been modeled using one in for a certain set of population, it is not going to work with a different population if it has been modeled with the classical techniques. But even with modern machine learning techniques, we have observed the same behavior. Like if a model has been

### 01:12:26 · Speaker 1

Agreed, agreed. I'm not disagreeing at all. But thing is, overall, right, empirically, the statistical statistics-based method have given you much, much better performance compared to these things. I mean, I'm not saying that this is, I mean, as people keep saying, no, all models are wrong. Actually, all models are wrong, but some are useful. So these have become more useful, right, more mainstream, more useful. If you have any metric that will measure the goodness of these functions, okay, which is the performance,

### 01:12:56 · Speaker 1

metrics the functions that people have found out using statistical tools have shown better performance in terms of those metrics compared to classical techniques that's all

### 01:13:10 · Speaker 1

Yeah, but I'm not saying that, okay, the statistic would solve the entire problem. It will give you the perfect function that is approximated. That's not what it is. But as I said, if you take any metric, I mean, we have seen this, right? What, like, uh...

### 01:13:28 · Speaker 1

The commercially available techniques do right. I mean, all our phones have face recognizers and they do fairly well. There are problems, of course, but they do fairly well. All of them are running on ML, right? So suppose you want to use classical techniques to do it. The generalization capability is rather poor for them.

### 01:13:47 · Speaker 1

Okay uh I did it

### 01:13:49 · Speaker 2

Sir just the assumption I made the example you gave for image classification like house or maybe spam no spam does did it fail because it is more of a rule based system than ML because we are directly identifying whether there is a rectangle or not whether this is required or not

### 01:14:05 · Speaker 1

Exactly yeah that's what I told you right I mean what do you mean by rule based uh what do you mean by rule based system by rule based system I mean that you have found that approximated that underlying function using some rules

### 01:14:16 · Speaker 2

Okay

### 01:14:17 · Speaker 1

right and those rules are not the again let's go not call them rules i mean uh see one other suggestion or rather request that i have is as we are as we'll be moving uh like ahead in the classes please okay two things one don't try to force fit uh your already existing terminologies and knowledge in the class okay uh because what happens is you know i'm i want to build it the brick by brick and i at the end of this course i want to start

### 01:14:47 · Speaker 1

using uh you know my language which is the language of uh ml community so please try to use the the the definitions and the techniques that we have discussed in the class as much as possible that's one thing the other request that i have maybe it's too early for a test but suppose i'm teaching you let's say adversarial networks or diffusions please don't ask questions on things uh that i have not covered in the class

### 01:15:16 · Speaker 1

Okay, so because what happens is I'm sure that I mean what happens is in a large class like this, it'll be too heterogeneous, you see. So some of you might find this, find some topics trivial, some of you might find some, uh, uh, uh, no, a novelty there in some topics that I'll be teaching. So I have to cater to the average population, you see. So that's why I have, I will cater my lectures that way. But I do, I mean, encourage and request you to ask.

### 01:15:46 · Speaker 1

many questions as possible but uh please don't ask me questions on topics that i have rather not uh covered yet right or rather going to cover later and also ask as much as possible use the terminologies that have been developed in the class okay for instance the reason i remembered all this is i mean again uh you know nothing particular to you or because i just remember i i anyway i had to say this because it came up i just said for instance uh see there is no rule

### 01:16:16 · Speaker 1

Now we have been talking about functions, define what functions are. So what we are doing here in the classical techniques is that we are learning these functions or rather we are finding out these, I mean I have never defined this word learning, I am sorry. So we are finding out these functions using pair of observations. Now why do they fail is because the function that we have thought that is the correct function is not the correct function.

### 01:16:43 · Speaker 1

Now there have been enormous amounts of

### 01:16:52 · Speaker 1

is that okay somebody said that no no no if you want to look at human faces don't look at these uh these rectangles in fact you can go even one step below okay where

### 01:17:05 · Speaker 1

I mean see what do you mean by a rectangle I mean I just took this as granted what do you mean by rectangle rectangle is you should have four line segments that are perpendicular to each other and so on so now how do you find out perpendicular line segments you have to do what is called as edge detection there right given an image you have to detect the edges and what if there are multiple edges in the image how do you deal with it and so on and that's why you have these classical image processing techniques right where people look at subalgorithms different kinds of operators to do edge reduction and then came these wavelet transforms etc so basically

### 01:17:35 · Speaker 1

they are asking this fundamental question, right? What is the underlying function that I have to find such that I can relate these two sets that I have at the hand? And because these functions that people have come up with, they are not correct in the sense that they don't predict the correct element in the range set, they are failing.

### 01:17:57 · Speaker 1

Okay, now the question, the bigger question is what other way can one think of when we need to relate these two sets? That is the question that we'll answer in a while.

### 01:18:08 · Speaker 1

Okay uh she won't

### 01:18:11 · Speaker 3

Well yes I think

### 01:18:12 · Speaker 2

uh you have partially answered to my question but yeah again to understand when we do a function approximation for any particular input how do we come to a point like we do an experiment and we say that okay uh this function is not working well for this particular input and we try to increase the complexity by increasing the number of parameters or trying out different approach but is there any initial study which shows that it's a good start uh that we should take these number of parameters and try this particular approximation technique

### 01:18:42 · Speaker 2

for this particular input or it just on the trial basis we we do

### 01:18:49 · Speaker 1

Yeah, see that is more of, yeah, there is no, I mean, there are a few techniques, right, where, okay, there are, see, for instance, neural networks, there is one large class of functions that you can try out, which are universal function approximators, see?

### 01:19:06 · Speaker 1

Right. So that is why neural networks are so popular. We'll come to that in a while. So why are neural networks so popular is because the functions that these neural networks approximate, right, are a large class of functions. So now instead of trying out different, let's say you try out a parabola, you try a third degree polynomial, you try an nth degree polynomial, et cetera. These neural networks are class of functions that can approximate any function to arbitrary closeness. So that's why you can try neural networks. In fact, that is the reason why they're so popular.

### 01:19:36 · Speaker 1

these days right they are universal approximators

### 01:19:40 · Speaker 1

Okay so basically yeah so the the motivation is that right I mean when you cannot have

### 01:19:48 · Speaker 1

like official functions or rather classical functions that would map that would relate these two sets you need a different kind of paradigm to model these two and that's why probability theory becomes a handy thing you know in fact I should tell you something so it was mid 1980s people were trying to solve this this speech recognition problem and a lot of speech scientists they used to model okay in fact they used to model the entire

### 01:20:18 · Speaker 1

vocal apparatus as concatenation of several wave guides so wave guides you know what wave guides are right they are physical cavities where electromagnetic waves travel they used to model the entire the vocal apparatus starting from lungs to mouth as concatenation of several wave guides with different diameters and lengths so now the the way when the shape of the wave guide changes right the way the wave propagation happens through that changes so those were using those were being

### 01:20:48 · Speaker 1

modeled as several differential equations with several initial conditions and so on people have spent decades doing this now the idea was that okay if you can like model those things using physics then you know what sound produces what sort of a signal and so on but in I think you know 19 19 late 1980 I think it's either IBM or Bell labs I don't remember which one of it they demonstrated that using statistical methods those

### 01:21:18 · Speaker 1

they were hidden Markovian models which are nothing but ML models right I mean using statistical methods they actually demonstrated they cracked the problem of isolated word recognition where they're not it's not speech recognition if you say an isolated word with limited vocabulary they could identify that okay

### 01:21:39 · Speaker 1

People from this classical physics, right, they got so irritated that they said that all that you are doing is, you know, modeling your ignorance. This was actually said, this is documented. They said that, oh, because you don't know how speech signal is related to phoneme and you cannot use the first principles in physics, you are simply, you know, modeling. uh the ignorance that you have and these things were actually called ignorance models those days and people were very against these uh these kinds of statistical models but

### 01:22:09 · Speaker 1

come 2010s right uh we have seen that these kinds of problems can be very easily modeled uh using statistics and probabilities probabilistic methods okay

### 01:22:21 · Speaker 1

Okay, so I think let us take a short break. It is 10.40 now in my clock. Let's get back at 11 a.m. So what we will do next is I'll tell you how is this problem solved using the probabilistic methods and we'll start defining what probability spaces are and what the probability measure is and distribution functions and so on. So we are resuming in about 18 to 20 minutes. See you in a while.

### 01:44:33 · Speaker 1

Shall we resume

### 01:44:37 · Speaker 2

It's your fault

### 01:44:45 · Speaker 1

So yeah so we were talking about uh

### 01:44:50 · Speaker 1

function approximations and we want to find functions right even pairs of elements from the domain and range and we saw that in in some of the scenarios finding all these relationships are non-trivial so it's different kinds of approach for it so uh this motivation right so what is done in this branch called the probability probability theory

### 01:45:21 · Speaker 1

the first situation that is done here I mean also rather the first assumption that is made is that

### 01:45:30 · Speaker 1

uh vaguely that's what happens is

### 01:45:36 · Speaker 1

of humanizations of it I'm going to have to write that so basically what it said is

### 01:45:42 · Speaker 1

Hello

### 01:45:46 · Speaker 1

Uncertainty

### 01:45:52 · Speaker 1

Reconstruction

### 01:45:57 · Speaker 1

Okay, so what do I mean by this? This is actually a striking difference between the deterministic way of looking at things and probabilistic way of looking at things is that, so in probability theory, right, the models and the ideas are built by inherently allowing uncertainty in all your functions. What do you mean by that? See, look at this. Suppose we want to solve this problem, this problem of gender, okay, given a picture.

### 01:46:28 · Speaker 1

Now I don't have to tell you so given every picture I don't have to tell you whether this picture belongs to a man or a woman right most of the times our job will be done if I tell you that look this picture has about 70 percent of chance of belonging to a man

### 01:46:51 · Speaker 1

we were okay with it right and we go ahead with those decisions isn't it so uh uh another example that can be given is if you look at this emotion as well so instead of saying that this particular document correspond to one of these emotions what if i tell you that these these documents they okay given a particular document i'll say that okay this document has 30 chance of being sad and 20 chance of being angry

### 01:47:21 · Speaker 1

Percent chance of being happy and so on. That's enough for most of the uh.

### 01:47:27 · Speaker 1

Task that we are supposed to do. Now, basically, uh, this is the idea that

### 01:47:35 · Speaker 1

Saying that, I mean, observing that uncertainty is okay, right? I mean, basically.

### 01:47:42 · Speaker 1

over the functions okay that we are interested in

### 01:47:49 · Speaker 1

Which are the mappings from terrain and the

### 01:47:56 · Speaker 1

Mappings from domain to to the range okay

### 01:48:04 · Speaker 1

can have can possess

### 01:48:09 · Speaker 1

uncertainties

### 01:48:15 · Speaker 1

Now I think you know this nomenclature makes sense right prediction. So what you are actually doing is given a particular element in the domain what you are telling me is that you are telling me what is the chance of that particular element from the domain that maps to different elements in the range.

### 01:48:36 · Speaker 1

See the point?

### 01:49:11 · Speaker 1

So sorry I was muted and didn't notice that. Okay, so what I'm saying here is that in the project GNL inherently what is done is the functions that we are trying to learn between two sets, right, they can possess uncertainties by construction. Now, why is this important or why is this a good thing is because as I said, if you allow for uncertainties, right, then what happens is so uncertainties

### 01:49:45 · Speaker 1

Following for uncertainty is one

### 01:49:50 · Speaker 1

Mix

### 01:49:57 · Speaker 1

makes function learning easier

### 01:50:08 · Speaker 1

makes the function learning little feasible right because the you are if you are giving me more freedom it's it's like actually giving the model i mean or rather the paradigm more freedom in the sense that i don't care if you if you are going to tell me what exactly is the element from the range that gets that gets mapped to this particular limit in the uh in the domain set but i only care whether i mean if you if you tell me what are the chances of this particular

### 01:50:38 · Speaker 1

a member in the uh the the domain of getting mapped to a particular uh member in the range set so now i mean one might think that okay i mean if you do not have uh the uh uh i mean if if if this uncertainty is there inherently in the model it can be a negative thing right because

### 01:51:00 · Speaker 1

If I, I mean decisions are deterministically taken. I mean either you go somewhere, not go somewhere. Either you eat something, not eat something. How can I have an uncertainty associated with my decision? It turns out that these functions and a lot of the use cases, as I said, it is okay if I give you some odds of this particular member in the domain set, critic map tools, different members in the range set. And I give you examples on that.

### 01:51:30 · Speaker 1

You know, for this male-female classification task or rather mapping task, it's enough if I tell you that, okay, this picture has 70% of chance of belonging to a male. A lot of times what happens is we take chances and risks in life, right? I mean, that is the idea. So you inherently allow uncertainties by construction in the model. You have uncertainties, makes function learning feasible. This is one thing. The other thing that is relevant to this particular course,

### 01:52:00 · Speaker 1

that if you allow uncertainty in it this will

### 01:52:06 · Speaker 1

This will help

### 01:52:09 · Speaker 1

Creativity

### 01:52:15 · Speaker 1

it is too philosophical but think about it i mean i'll concretize all these ideas in a while mathematically but think about it uh if we are set on stone right if we are uh if we are uh deterministic everything that we do we don't just take risk as they say uh then you're stuck you can't be creative if you don't take this so creativity see for instance right while when people when when artists write uh portraits okay

### 01:52:45 · Speaker 1

of people or landscapes that that that do not exist

### 01:52:50 · Speaker 1

what's actually happening is that there is a certain their model of of of human faces right that has a certain uncertainty associated with it without that uncertainty that is associated with that there is no way that this artist is creating a new uh uh image or rather new picture of a human being that does not exist you understand so now if the model inherently or rather the function or the paradigm allows for uncertainty by construction it

### 01:53:20 · Speaker 1

One makes this function learning feasible because there are more degrees of freedom. And two, it will help creativity. And that's why, right, I mean, the generative modeling was possible only through probabilistic paradigms. I will define all this concretely, but think about it. Now, all the while the problem was that if you are given elements from the domain and the range set, you want to find a function that would map every element in the domain to every element in the range set.

### 01:53:50 · Speaker 1

So on solidarity, what happens is that you can create more elements from the domain set and you can create more elements from the range set. That is what generative modeling is all about, right? At some level. So this is what it is. So this is the paradigm where

### 01:54:09 · Speaker 1

The function learning, right, and these, the approximation that you do of all these functions, you allow for uncertainty, the presence of uncertainty by construction, okay? Okay, so any questions on this before we concretize these ideas?

### 01:54:28 · Speaker 1

So what do I mean by allowing uncertainty? How do you do it actually is something that I that I'm going to talk about in a while. But yeah, before that, uh, in the philosophical idea, any questions?

### 01:54:46 · Speaker 3

Answer here domain range means the input values

### 01:54:53 · Speaker 1

Please raise your hands before you talk okay I'll call out your names

### 01:54:59 · Speaker 1

Yes uh Kartik

### 01:55:02 · Speaker 3

to the preview

### 01:55:10 · Speaker 1

No no no no no see mathematically looking at it there is nothing called exception if there is a domain set there is a range set it is a function that maps the elements from here to elements from there

### 01:55:22 · Speaker 1

So there's there's no idea of exception right in deterministic function learning

### 01:55:27 · Speaker 3

Look you know is it

### 01:55:28 · Speaker 1

Isn't it? So like, you know, f equal to ma, f equal to ma, that's all. There's no no exception per se.

### 01:55:36 · Speaker 3

No, yeah, there can be scenarios like what we say, right, when f equal to ma, but given that mass is constant, if mass is not constant, that's an exception to this. So something like that.

### 01:55:46 · Speaker 1

Well, well, it's not really because see when if you if you make mass not a constant or whatever the conditions are, then the domain and the range set completely changes, you see, as well as the domain and ranges are fixed, right? It's a deterministic function. No, there is there is no inherent uncertainty in the model per se or the function.

### 01:56:09 · Speaker 3

Okay sure

### 01:56:10 · Speaker 1

Hey yeah uh Aditya

### 01:56:15 · Speaker 2

Is there one rather comment not a question is that if there is an inherent uncertainty in the system we cannot use these kind of systems to make any control decisions or any any any such decisions is that correct

### 01:56:33 · Speaker 1

That is why right now people are uh uh skeptic about using these tag GBDs for all this. See why do you think people are talking about explainability and safety biases of these systems? Just because they are probabilistically built.

### 01:56:49 · Speaker 1

Right, so that's why people are touchy about these things.

### 01:56:54 · Speaker 2

Got it. And one more observation on when we say functions, right, functions are well-defined, which maps each input to its outputs, right? If you look at f is equal to ma. So when we talk about these n-dimensional functions with parameters which are in billions, is that something which is, I can't visualize that, how that function is going to look like?

### 01:57:22 · Speaker 1

Well, you can't, I mean, because human beings can't visualize anything beyond three dimensions. So you can't visualize those functions, correct? Yeah. But you, I mean, you can imagine functions, right, that would take a billion dimensional vectors as inputs and gives you a scalar. That's very much possible.

### 01:57:42 · Speaker 1

Right? But of course those functions cannot be visualized because you can't we can't visualize as human beings beyond three dimensions. That's that's there.

### 01:57:53 · Speaker 2

Cheers

### 01:57:54 · Speaker 1

Yeah, so now let's come to this point that is how do you allow uncertainty by construction? That's the point. Now, the first thing that is done is see, remember that we had sets, right? I mean, set A, the way we called it as

### 01:58:09 · Speaker 1

know xi all the observations that we make no x1 x2 all these observations that we make which are the elements from the domain the first thing that is done is now each of these observations are the sets that we look at okay

### 01:58:28 · Speaker 1

That is

### 01:58:32 · Speaker 1

Now these vectors let's say let's say that these are

### 01:58:36 · Speaker 1

Some d dimensional vectors. These can be d dimensional vectors. Now these are

### 01:58:43 · Speaker 1

In the probabilistic sense right these becomes these become what are called as instantiations

### 01:58:55 · Speaker 1

of a random variable

### 01:59:03 · Speaker 1

these no longer are vectors okay now they are not just seen as you know points in some data dimensional space they are seen as instatations of a random variable now what is this random variable business now the way the probability theory structure is the following so it all starts with probability theory

### 01:59:26 · Speaker 1

It starts with something called a random experiment

### 01:59:31 · Speaker 1

Random experiment or a random trial

### 01:59:37 · Speaker 1

please play pay some attention here okay so it says that there is a random experiment or a trial that is happening okay why is it called a random experiment this is one thing that is not well defined in probability theory right there is what do you mean by random nobody knows but there is an experiment that is happening and these experiments they give rise to what is called as outcomes

### 02:00:05 · Speaker 1

Basically these are the outputs or rather outcomes of these random experiments and these outcomes okay are enumerated in a set.

### 02:00:17 · Speaker 1

A set of outcomes

### 02:00:22 · Speaker 1

is actually critically important that all of you understand. It's not very difficult, but please follow me and understand what it's saying. So it begins with random experiment and the outcome of, I'm sorry, the, yeah, the, the observations of these random experiment is enumerated in a set of outcomes. And this is called the sample space.

### 02:00:52 · Speaker 1

Don't worry about its analogies now but

### 02:00:56 · Speaker 1

you mean by set of outcomes uh it is simply enumerating right uh or uh just listing down all the possible outputs of a random experiment now what is a random experiment anything that you that you want to model right now becomes a random experiment let me give you an example let's say that let's take the example of i don't know why this suddenly gives me some weird shapes example let's say that we have image

### 02:01:26 · Speaker 1

It's right

### 02:01:29 · Speaker 1

So, even before coming to that, let's take easy examples. Now, a random experiment.

### 02:01:38 · Speaker 1

I'm tossing a coin and all of you know this

### 02:01:47 · Speaker 1

Tossing a coin is a random experiment. Okay. Now, what are the questions that you are interested in? Like, I want to know when I toss the coin 100 times, what are the odds that are like how many times does the coin turn out to be head or something? Those are the kinds of questions that I'm interested in. But random experiment is simply tossing a coin. Now, what is the sample space here? What are the possible set of outcomes? The possible set of outcomes are head and tail. Okay. Assuming that the coin has two faces. This is one example of a random experiment.

### 02:02:17 · Speaker 1

Now another example can be like can people can tell me what it is or you can roll a die

### 02:02:26 · Speaker 1

and then face to die

### 02:02:32 · Speaker 1

Now the sample space in that case would be so one two whatever possible outcomes that are up to you

### 02:02:40 · Speaker 1

So you got an idea of what is a random experiment, right? I mean anything an experiment that is being performed and is called a random experiment and the possible outcomes of that random experiment is just enlisted in a in a set, okay, which is called the sample space.

### 02:02:59 · Speaker 1

No when we

### 02:03:02 · Speaker 1

The two

### 02:03:05 · Speaker 1

We are not interested in rolling the die or tossing a coin. We are interested in looking at an image and finding out whether it's a man or a woman, right? So now, um...

### 02:03:17 · Speaker 1

Taking a picture

### 02:03:23 · Speaker 1

for person

### 02:03:27 · Speaker 1

Is a random experiment. Can you visualize taking a picture of a person as a random experiment?

### 02:03:36 · Speaker 1

Let me tell you what I mean by this. Now imagine that you know you can there are there are there are infinite people that are there right and you taking a particular sensor and shining light on a particular person and measuring the reflectance of that particular person becomes a random experiment. Now what is the sample space can somebody tell me what would be the sample space.

### 02:04:05 · Speaker 4

The same picture can never repeat twice

### 02:04:09 · Speaker 1

No, no, no, I'm simply asking what is the sample space? Okay, so let me just go back to definition. So what is sample space?

### 02:04:16 · Speaker 4

All fixed color value combinations

### 02:04:18 · Speaker 1

Sample space is simply the enumeration of all possible outcomes of a random experiment

### 02:04:27 · Speaker 1

Now, the example, right, in tossing a coin, the headtail are the sample space. Enrolling an n-phase die, the 1, 2, 3, et cetera, n are the sample space. Now, if you take a picture of a person, what is the possible sample space? Yeah, the person's image.

### 02:04:41 · Speaker 3

I like the fancy letters

### 02:04:46 · Speaker 2

all pixel combination male female and third gender

### 02:04:50 · Speaker 1

No it's not that because I'm talking about

### 02:04:52 · Speaker 2

All the people of

### 02:04:54 · Speaker 1

Yeah, so it's actually, I'll write it as person one, person two, person three. And if there are whatever, right? If you have like, let's say seven billion people in this world, you have seven billion possible outcomes.

### 02:05:11 · Speaker 1

Can you see this? So basically, this is the way you are modeling it. You understand? So now the random experiment that is happening is simply taking a picture, okay, of a person is a random experiment. It's simply like rolling a dice. When I see this is the world view that you should slowly develop when you are dealing with machine learning that reading an image from one of these open CV libraries or something is nothing different than tossing

### 02:05:41 · Speaker 1

coin in the probabilistic sense of words okay so now that's why i wrote the sample space right i mean there are these many people every person now becomes uh the sample space and and similarly you can imagine right i mean now suppose i'm um recording speech

### 02:06:06 · Speaker 1

recording the speech signal what happens is that every possible sentences that everybody in this world can talk of becomes a sampling space

### 02:06:22 · Speaker 1

Uh any questions on what is what constitutes a random experiment and what are sample spaces

### 02:06:33 · Speaker 1

Okay, now what happens is that when we measure, right, and when we have a sensor and, you know, we have a condenser microphone, we measure it, what we get to measure are not the elements of sample space. So let me write that. So elements.

### 02:06:56 · Speaker 1

rather maybe before coming there let me just define the probability measure okay so this is the sample space now

### 02:07:05 · Speaker 1

what so now this is a set okay now um let me give you an example let's say that i have set up real numbers which are

### 02:07:18 · Speaker 1

Yeah simply take set of real numbers right then

### 02:07:26 · Speaker 1

of real numbers

### 02:07:30 · Speaker 1

Call it R

### 02:07:32 · Speaker 1

Now I take a subset

### 02:07:36 · Speaker 1

me call it uh use case already there are not of notations very quick very quickly so let's call let me call it a1 is a subset of real numbers okay and a2 is another subset of real numbers so for example this can be 0 to 2 okay this can be

### 02:07:57 · Speaker 1

three to eight these are two subsets of real numbers right see my interest number is i want to compare these two sets how do i compare these two sets okay so let's say that the intent

### 02:08:15 · Speaker 1

Compare

### 02:08:20 · Speaker 1

A1 and A2 which are both subsets of R

### 02:08:25 · Speaker 1

I tell you what is the relevance of this with sample space in a while but yeah so let me take some uh like opinions here if I have subsets of real numbers how do I compare subsets of real numbers

### 02:08:40 · Speaker 2

Maybe what is the common numbers between two sets

### 02:08:47 · Speaker 1

Okay, so how does how does that how does that tell me uh how I mean anything about these two sets

### 02:08:56 · Speaker 1

Okay so I'll tell you what do I mean by compare it and I want to I want to ask questions like which one is

### 02:09:05 · Speaker 1

bigger

### 02:09:09 · Speaker 1

or smaller

### 02:09:13 · Speaker 1

something of this sort so how do I do that I think people have raised their hands Harsha

### 02:09:20 · Speaker 4

Yes sir so one way to compare is uh like if you are able to map each element in this set to another element in the uh other set we are comparing and if we are able to map

### 02:09:31 · Speaker 1

I can't, no, I can't because here I can't find a function that would, are you saying that I have to find a function that would map elements in set A1 to A2? See, again, when I say compare, right, I mean, please take this as the question. I want to know which one is bigger and which one is smaller.

### 02:09:52 · Speaker 1

You all know the answer to this question, but I just want to hear from you. Yeah, Nirmith.

### 02:09:58 · Speaker 4

Finding the cardinality of the set

### 02:10:04 · Speaker 1

Both of these sets have infinite cardinality no these are subsets of real numbers. Cardinality of both of these are infinity is it right?

### 02:10:15 · Speaker 1

You see that in the month? Because these are subsets of real numbers. So cardinality won't give you anything. If it's a discrete set, of course, but it's a subset of real numbers, cardinality won't help.

### 02:10:37 · Speaker 1

Okay biology

### 02:10:40 · Speaker 4

No so you can find like mean median

### 02:10:46 · Speaker 1

How does taking me tell you which one is bigger and which one is smaller

### 02:10:51 · Speaker 3

We got the

### 02:10:51 · Speaker 1

But there are only it's a set you understand that it's a set no So there are infinite numbers so now how do you take mean of infinite numbers

### 02:11:00 · Speaker 1

See, there are infinite elements in both of these sets. Does all of you agree with that? You can respond with an emoji or something, right? Does all of you agree that there are infinite numbers in both these sets? The cardinality of both these sets are infinity. So the average doesn't make sense here. I just want to know if you can tell me which one is bigger. That's all. Maybe I'll make the question easier, right? Tell me which one is bigger. Okay. So let's ask me this. Let's ask this question. Which one is bigger in these two sets?

### 02:11:30 · Speaker 1

Aditya and by the way when I ask you a question right and when you when you raise your hands to answer I would randomly call out names okay so please don't take uh it otherwise if we I mean when I ask you I mean if there are any questions then I'll go one by one when I ask you questions then I just take random order okay so here is the question the question is which one of these two is bigger Abhiram

### 02:11:56 · Speaker 4

If we apply the length measured then the set on the right hand side seems to be bigger

### 02:12:02 · Speaker 1

Okay what can you expand that okay let's say use this word measure

### 02:12:09 · Speaker 1

What do you mean by that? That's exactly where I'm coming to

### 02:12:13 · Speaker 4

So

### 02:12:14 · Speaker 1

You said length measure what is length measure

### 02:12:15 · Speaker 4

Yeah length length measure is a function which maps the number of sigma algebras in a set to a number

### 02:12:24 · Speaker 1

that you seem to know things so now I didn't talk about sigma algebra yet okay so yeah so yeah what is what is the measure so basically what he is saying is just look at the length of these two sets

### 02:12:39 · Speaker 1

okay so now you represent these two set the i mean the the these two sets on a on a number line so this is 0 to 2 and this is 3 to 8

### 02:12:52 · Speaker 1

Okay now Dilla's line has a

### 02:12:56 · Speaker 1

higher length

### 02:13:01 · Speaker 1

Compared to this length this line correct

### 02:13:07 · Speaker 1

Does all of you agree

### 02:13:10 · Speaker 1

Well if you agree with this right I mean so basically what we are saying is that associate how do you generalize this idea

### 02:13:12 · Speaker 3

It is so

### 02:13:17 · Speaker 1

Associate okay a scale of a positive function

### 02:13:26 · Speaker 1

a non-zero function

### 02:13:35 · Speaker 1

Everybody's looking at a lot

### 02:13:42 · Speaker 1

Basically given

### 02:13:46 · Speaker 1

subset a of r what i do is i take that subset and associate that with some number okay which i call as mu a

### 02:14:01 · Speaker 1

Okay which is

### 02:14:07 · Speaker 1

A positive real number between zero and

### 02:14:12 · Speaker 1

It's simply a positive real number okay I can actually say it has belonged to R plus

### 02:14:22 · Speaker 1

confusing with notation it's a it's a non-zero

### 02:14:29 · Speaker 1

Real number on zero

### 02:14:34 · Speaker 1

It can be zero also

### 02:14:43 · Speaker 1

Non-negative real yeah that's what it is

### 02:14:50 · Speaker 1

You understand? So what we are doing here is that for every subset of real numbers, we are associating a non-negative real number, okay? Which would, which I call as, and by the way, this is defined as measure of A.

### 02:15:14 · Speaker 1

Do you understand? Now basically let's abstract out. So we are given a set, okay, which is set of real numbers and we are taking subsets of this set and corresponding to each of the subset of this set, I associate a non-negative number and I call it the measure. Does it make sense? So basically what does measure do is that a measure

### 02:15:40 · Speaker 1

basically a function that will take a subset of a given set okay and maps it to

### 02:15:55 · Speaker 1

Non-negative real numbers. Do you understand? So this is a measure.

### 02:16:00 · Speaker 1

So now why is this important is that given every any subset of a given set okay now you can compare sets based on their their corresponding measure.

### 02:16:13 · Speaker 1

This facilitates

### 02:16:19 · Speaker 1

Comparison

### 02:16:25 · Speaker 1

or subjects

### 02:16:29 · Speaker 1

Let me give you another example let's say that our set is set of

### 02:16:36 · Speaker 1

are two which are you know two dimensional vectors

### 02:16:40 · Speaker 1

what can be so which means that an element here right an element in R two

### 02:16:51 · Speaker 1

is represented as x1 comma y1 or let me call it x1 comma x2

### 02:17:00 · Speaker 1

is I write it as capital X which is X1 comma X2 okay this is an element now suppose I give you okay so now tell me a measure that you know of that is defined on R2

### 02:17:16 · Speaker 1

measure on R2 you people already know this

### 02:17:20 · Speaker 2

So the tens cost is one square per extra score

### 02:17:21 · Speaker 3

Okay

### 02:17:21 · Speaker 4

Okay

### 02:17:25 · Speaker 2

a magnitude root of x one square plus x two square that can be used to

### 02:17:31 · Speaker 1

Yeah, but that's an element, right? I'm talking about a subset. If I take a subset of R2, okay, see, remember that measures are defined on subsets.

### 02:17:47 · Speaker 1

See in R1 what happened? We represented every subset as a line segment. Okay. So now if I write R2.

### 02:17:57 · Speaker 1

How are each subsets represented here

### 02:18:00 · Speaker 4

areas

### 02:18:02 · Speaker 1

How are these substances represented

### 02:18:03 · Speaker 4

rectangles

### 02:18:05 · Speaker 1

Thank you very much

### 02:18:05 · Speaker 2

45 48

### 02:18:07 · Speaker 1

yeah then can be it can be any uh uh irregular shape it doesn't matter but for now yeah so this is a subset right a subset in r2 okay now what can be a measure that you already know on subsets of r2

### 02:18:24 · Speaker 1

area of interest

### 02:18:29 · Speaker 1

So every subset has a measure called area now

### 02:18:33 · Speaker 1

Okay, now if you extend this to a d-dimensional real space, what is the measure?

### 02:18:40 · Speaker 3

Volume

### 02:18:43 · Speaker 1

They're volumes, right? I mean, they're hyper volumes. You can't call them volumes, they're hyper volumes. So this measure that we know of, right, which is, you know, which is length in one dimension, area in two dimension, and hyper volumes in three dimension, it has a name. Do you know what the name for this measure is?

### 02:19:00 · Speaker 1

Does anybody know the name of this measure? See, there can be, this is not the only measure that you can have. You see, given subsets of any sets, you can come up with any measure. And there's a definition of measure, right? Okay, that if you have a set with zero cardinality, the measure has to be zero. So if you have two non-overlapping subsets, the measures have to add up. The measures of the individual subsets has to be equal to the measure of the union of those subsets. Okay, so these are

### 02:19:30 · Speaker 1

of the properties that the measure should have but anyway you can come up with multiple measures actually you can come up with your own measure and give it your name doesn't matter as long as these properties are satisfied but the usual uh length area volume measures that we know of right that we use that we have been using since uh class five uh there's a name for this measure do you know what the name for this measure mean is

### 02:19:56 · Speaker 1

These are called Lebesgue measures

### 02:20:03 · Speaker 1

I don't know why his name is is is spelled like this, but yeah. So this is called Lebesgue measure. So all the length, area, et cetera, that we do in Cartesian or rather Euclidean spaces, right? D dimensional Euclidean spaces, they are called Lebesgue measures. So the length, area and volume measures. Is this idea clear? Why am I talking about measures here? There's a reason for it. I just, just give me a while. I'll come to that. So now you understood what measures are, right? So basically what I'm doing is that,

### 02:20:33 · Speaker 1

I'm given a set okay I'm constructing

### 02:20:37 · Speaker 1

the subsets of that particular set

### 02:20:42 · Speaker 1

Now for every subset that I am constructing on this particular set, I am associating a number with it. And that number is what I am calling as a measure. And we just saw an example of a measure in d-dimensional Euclidean spaces and we called it as Lebesgue measure. Any questions, Prupal?

### 02:21:14 · Speaker 1

Hello am I already going are you dead

### 02:21:18 · Speaker 1

Okay, uh yeah there are a few questions but no case for me on

### 02:21:24 · Speaker 2

the measure

### 02:21:27 · Speaker 1

Good question. It's by definition. See the thing is because we perceive measures as you know something that is that we can compare. So we can't compare negative numbers you see. We can only compare the positive numbers. See if you perceive these things as lengths there cannot be negative length.

### 02:21:52 · Speaker 1

I mean it's only a convenient definition convenience so the way the measures are defined they have to be non-neglected

### 02:22:02 · Speaker 1

But anyway, there are lots of measures. Lebesgue measure is only one of the so many measures that people have come up with on real numbers. But yeah, so Lebesgue measure is one of such measures. There are other measures like Henry measure, Riemann measures and so on. But yeah, so the usual measure that we look at, right, the lengths and areas and volumes, they're all Lebesgue measures. Okay. Any other questions on this? I mean, what constitutes a measure?

### 02:22:31 · Speaker 1

Again, I'm defining, right? I mean, it's basically a function, a set function that will take subsets of a given set and maps it to a non-negative real number such that there are some properties. I'm not going into details. You know, one property is that it has to be, see, every measure by construction, by definition, has to be

### 02:22:51 · Speaker 1

negative for any set it has to be greater than or equal to zero the other thing is measure on the null set has to be zero okay and the measure on union of two sets has to be equal to the individual measures

### 02:23:12 · Speaker 1

the intersection is null these are some of the properties i mean as long as you can come up with a function that would adhere to these properties you can name it you can give it your name and call it your measure okay so this is the length measure okay so now why did i talk about this remember that our uh we were looking at random experiments okay and we are looking at outcomes now what are outcomes we do have a set here okay which is called the set of all possible outcomes of a random

### 02:23:42 · Speaker 1

experiment and we call that the sample space okay because we have a set

### 02:23:51 · Speaker 1

So we have this set which is sample space

### 02:23:59 · Speaker 1

It's it what is that that's a collection of

### 02:24:04 · Speaker 1

election

### 02:24:07 · Speaker 1

All possible

### 02:24:10 · Speaker 1

Outcomes

### 02:24:13 · Speaker 1

for random experiment

### 02:24:21 · Speaker 1

Right, we have a sample space. We can now create subsets of this sample space, right? So let F

### 02:24:32 · Speaker 1

You know

### 02:24:38 · Speaker 1

subsets set of subsets actually

### 02:24:45 · Speaker 1

create a set of subsets

### 02:24:58 · Speaker 1

Do you understand what I'm talking about? Again, you can go back to your examples, right? If you are rolling the die, you can take, you know, one, three, four, five as one subset of examples, right? If you are looking at tossing a coin, you can head, head, head, tail, head, tail, tail, whatever, right? They are subsets of omega. I mean, this is omega, by the way. And if you're looking at pictures, then if you take pictures of several, so some set of human beings, right? That is a subset of this particular set.

### 02:25:28 · Speaker 1

F denotes

### 02:25:30 · Speaker 1

The collection of all such subsets of the sample space

### 02:25:35 · Speaker 1

Please that's clear

### 02:25:40 · Speaker 1

See, just like we had the line segments, right, which are the pieces of number line, the real line. So you have subsets of

### 02:25:51 · Speaker 1

the sample space okay which is a set

### 02:25:57 · Speaker 1

Now now we have a set and we have a subset. Now because we have a subset subset and the subset we can define a measure on it.

### 02:26:06 · Speaker 1

Right so now define a measure

### 02:26:15 · Speaker 1

I'm ashamed

### 02:26:18 · Speaker 1

Okay actually turn the probability measure

### 02:26:28 · Speaker 1

Get on

### 02:26:30 · Speaker 1

every subset every element of the subset of sample space so now given any element

### 02:26:38 · Speaker 1

That is a subset of this T

### 02:26:42 · Speaker 1

sample space then I will define a measure on top of it okay and this right is defined as a measure that is

### 02:27:01 · Speaker 1

Between zero and one

### 02:27:03 · Speaker 1

unlike the Lebesgue measure that can take any non-negative value the probability measure okay can only take values between 0 and 1 so now you might have this question right why did we do it this way did it this way because as I said remember the goal is to associate uncertainty in the entire modeling process you see okay and how do you do that this is one of the ways of doing it now you say that okay everything that you observe is an outcome of a random experiment

### 02:27:33 · Speaker 1

And every subset that you observe or every outcome every subset that you observe of the outcome of the random experiment that you are doing now is associated with a particular

### 02:27:46 · Speaker 1

measure okay which is lower and upper bounded between 0 and 1 so now we you interpret the these values as the amount so basically this measure right the probability measure

### 02:28:02 · Speaker 1

such nuisance the probability measure

### 02:28:07 · Speaker 1

can be interpreted so just like you interpret the Lebesgue measure as length okay interpreted

### 02:28:17 · Speaker 1

Yes

### 02:28:19 · Speaker 1

The uncertainty

### 02:28:26 · Speaker 1

Associated

### 02:28:33 · Speaker 1

subset of subset A which is a subset of sample space do you understand

### 02:28:39 · Speaker 1

Now if you go to this example of looking at the speech and the images that we have as the as the elements of sample space, you can imagine if you take any subset of the sample space, there is an inherent measure, right, that is associated with this particular subset that would quantify any uncertainty that is interpreted as an uncertainty associated with this particular subset. Does it make sense? See you should see

### 02:29:09 · Speaker 1

probability right just as you see length on the linear the linear line so what is length let me write that so length

### 02:29:23 · Speaker 1

It is

### 02:29:27 · Speaker 1

R R 2 right is exactly equivalent to probability on

### 02:29:36 · Speaker 1

Campus basis

### 02:29:39 · Speaker 1

Can you see this point? Now, see, I just made the statement, right, that remember that we are interested in doing this, you know, function learning business. And we came up with this paradigm called probability theory. So what is basically being done is you model or rather you see everything that you have, right, as see, okay, so let me go back again. It's a very nice analogy here. See, here when we said that we have pairs of

### 02:30:09 · Speaker 1

observation that are coming from two sets. Similarly the set of the domain that we talk of for function approximation now becomes the elements of sample space.

### 02:30:22 · Speaker 1

Okay, and just like you associate lengths with the subsets of real numbers, you associate another measure called probability measure that would tell you that do not give you the length of these sets, okay, or subsets. This will tell you how certain or uncertain that particular set is.

### 02:30:46 · Speaker 1

Do you see this point any questions so far

### 02:30:49 · Speaker 1

There's one other piece that I have to talk about, which is the idea of random variable and distribution functions. We'll see that and then we'll stop this class because from next class I can start formulating what generative modeling is using these terminologies. But yeah, any questions so far? There's actually bare bone fundamentals for studying any of the ML. Okay. So let us ensure that you people understand what I'm talking about.

### 02:31:18 · Speaker 1

Any questions here?

### 02:31:21 · Speaker 2

Oh sir if we take the set of all subsets

### 02:31:24 · Speaker 4

of a set and assign a probability uncertainty for each of those subsets is that what we are talking about about

### 02:31:32 · Speaker 1

All right

### 02:31:33 · Speaker 4

And that's called a sigma algebra right

### 02:31:35 · Speaker 1

That's the same of course if you just need my library no

### 02:31:40 · Speaker 1

If we actually have a signal

### 02:31:43 · Speaker 1

That's also called the event set here because I'm not teaching probability theory. I'm not going deep into this. A first course on probability theory should start from this. So what you said is correct. F is a sigma algebra and the measures are only defined on sigma algebra. This is the sigma algebra defined on top of or obtained from the sample space. That's correct.

### 02:32:05 · Speaker 2

Not just

### 02:32:06 · Speaker 1

Uh Harish Gautam see I don't want you to overburden with terminologies you see I'll I'm only defining what is absolutely necessary

### 02:32:14 · Speaker 1

Arise don't

### 02:32:16 · Speaker 2

Uh so is the sample space same as domain

### 02:32:21 · Speaker 1

Not yet, okay, not yet. I will not say that because hold on to that question. That's a very good question. I will come to that in a while.

### 02:32:31 · Speaker 1

For now I would say no, they are not exactly the same. See because look at this. See if we are looking at taking the picture of a person as the random experiment and we are looking at every person as the outcome, right? Then where is the domain of the function that we actually talk of? See because see what we measure, I mean not the measure theory measure, I mean English measure, what we observe, let's say what I observe are real numbers.

### 02:32:59 · Speaker 1

Okay the elements of the sample space are not real numbers. Can you see that?

### 02:33:06 · Speaker 1

Elements of the samples page are persons or other sentences or their documents which are not real numbers. Do you see that?

### 02:33:19 · Speaker 1

So now the biggest challenge is which I will talk about in a while is that you need a mechanism where you convert the probability measure right into a space which you can you know which you can invite some other sort of measure in fact where you can use level measures and that's why random variable looks into picture I will talk about it in a while but don't think of the outcomes of a sample space as domains yet there is a relationship between them but they are not exactly

### 02:33:49 · Speaker 1

say okay that's a very good question by the way nice observation yeah have a look

### 02:33:56 · Speaker 4

Yeah, so how do we extend this notion? Like you gave the example that, you know, if we consider the set of all people as the set of sample space, and then if we are assigning uncertainties to certain sets of people.

### 02:34:11 · Speaker 1

All subsets, all possible subsets. All possible subsets. Exactly. Yeah. So you take any possible subset, it can be a singleton also in the sense that you can take a particular person and that particular person which happens to be a subset also has a measure associated with it.

### 02:34:13 · Speaker 4

All possible subsets of people

### 02:34:26 · Speaker 4

Yeah, so yeah, so my question is that how is this notion is going to help us to figure out whether that particular person is a male or female? I mean.

### 02:34:36 · Speaker 1

You have to be

### 02:34:39 · Speaker 1

That's a good question we'll we'll we'll see that we'll see that yeah

### 02:34:48 · Speaker 1

Uh yeah I did it

### 02:34:50 · Speaker 2

Uh so what I understood the complete theory is based on the correctness of the sample space right now

### 02:34:57 · Speaker 1

No, no, hold on, hold on, hold on. No, no, don't jump. What do you mean by correctness of sample space? I never defined that.

### 02:35:03 · Speaker 2

I mean uh I mean to say that suppose uh the random exa random experiment I am doing defining a sample space and from there we are taking the subsets and all this theory is based on that that is not it now suppose if we don't know the sample space or suppose we are talking about the planet in the universe multiple planets so on those case it is very tough to define a complete sample space right so on those cases if they are a

### 02:35:33 · Speaker 2

Parallel line here above probability

### 02:35:32 · Speaker 1

All those cases is

### 02:35:36 · Speaker 1

Okay, see in fact we never go to sample space because of this exact reason. We never care about sample spaces. We only work with random variables. Just hold on a minute, I'll come to the idea in a while.

### 02:35:48 · Speaker 2

Yeah

### 02:35:49 · Speaker 1

Yeah yeah

### 02:35:52 · Speaker 4

So why does it have to uh include every subset of uh yeah I mean

### 02:35:58 · Speaker 1

definition of measure right yeah because that's how we defined it right i mean given any subset it has to assign a value non-zero value

### 02:36:09 · Speaker 1

Because think of I mean you look at the Lebesgue measure right you take the real line given any subset of this I want to associate a length with it isn't it

### 02:36:23 · Speaker 1

You get it

### 02:36:26 · Speaker 4

Yeah but it need not be pairs right say for example if I consider 0 2 3 ah I mean does it also work on that because so now you have three three elements in that

### 02:36:33 · Speaker 1

I'm not sure

### 02:36:36 · Speaker 1

no no oh okay okay see it's not a subset you see see when you write what do you mean by 0 2 3 is i'm talking about three element subset yes see 0 2 3 is not a subset of r you should always remember that we are talking about the subset of a given particular set 0 comma 2 comma 3 is not a subset of r

### 02:36:58 · Speaker 1

You see that?

### 02:37:03 · Speaker 4

It is right Or

### 02:37:05 · Speaker 1

0 comma 2 comma 3 is it a subset of R the discrete set I mean is it a subset of R single term right I mean if you take two elements you are talking about this

### 02:37:21 · Speaker 1

See, note that I'm not putting square brackets here. If I put a square bracket, then it's a subset. Now, if I write 0, 2, 3, is it a subset? Let me just confirm.

### 02:38:07 · Speaker 1

set of natural numbers is a subset of R. Okay, yeah, fine. Then it's a subset of R. It's a valid subset of R. That also has a measure. In fact, the the label measure of a discrete subset of R is 0.

### 02:38:23 · Speaker 1

Okay, it's like this, right? I mean, even if you write this

### 02:38:28 · Speaker 1

0 comma 2 comma 3 you're actually asking me what is the length of these three points

### 02:38:36 · Speaker 1

Do you see that?

### 02:38:39 · Speaker 4

Yeah so that's where I'm confused so when I say a measure of A

### 02:38:41 · Speaker 1

Amazing

### 02:38:42 · Speaker 4

Wouldn't measure of A so I mean

### 02:38:42 · Speaker 1

So

### 02:38:46 · Speaker 4

what all do we really consider in that a and also if you if you scroll down below

### 02:38:50 · Speaker 1

See it can be any subset. See any subset right from the set of real numbers has an associated measure. But level measure of this particular singleton or like discrete subsets of R is 0 that's all.

### 02:39:05 · Speaker 4

If you come to this 2D picture right uh I mean there we said that uh

### 02:39:09 · Speaker 1

Yeah if you take the measure if you take the area of a line it is zero

### 02:39:14 · Speaker 4

Yeah, but in let's stay with this example. So when we say that element x1, x2, right? I mean, it's again a point in

### 02:39:22 · Speaker 1

Yeah, yeah, that's why I said no, measure is defined on subsets of R2. This is not a subset of, it can be a subset of R2, but this is again a set that has zero measure.

### 02:39:36 · Speaker 1

You get it This kind of thing has innovation

### 02:39:38 · Speaker 4

That's great Pam

### 02:39:40 · Speaker 4

Any example where the the measure is non-zero

### 02:39:44 · Speaker 1

This this thing no this rectangle

### 02:39:47 · Speaker 4

Okay so we we choose a region in the uh in in the space and then we associate

### 02:39:51 · Speaker 1

And R be associated. Yeah. In R2, you take a subset of R2. Okay. So it's like this. Okay. Let me write down. So this particular set.

### 02:40:08 · Speaker 1

1.1 comma 2

### 02:40:13 · Speaker 1

this thing is

### 02:40:16 · Speaker 1

two one point comma

### 02:40:21 · Speaker 1

Welcome to

### 02:40:24 · Speaker 1

This has an unzipped machine

### 02:40:31 · Speaker 4

Yeah because it defines a rectangle right

### 02:40:33 · Speaker 1

Exactly exactly exactly

### 02:40:34 · Speaker 4

And and if you can if you if you go back again to the one dimensional case, I think even there we can say the same stuff, right? So so length is a measure when we define it over a range.

### 02:40:45 · Speaker 1

No, see that's what I'm saying. See, if you take a subset, you take any subset, the way the measure is defined, it doesn't tell you what subset you have to take. You take a point here, you take three points here, okay? That's also a subset of R. Now the question is, what is the measure of that particular subset? The measure of that particular subset is zero, that's all. It does have a measure, but it has zero measure.

### 02:41:08 · Speaker 4

So you need a kind of an interval to define to get a non-zero measure

### 02:41:12 · Speaker 1

Leaving questions. Leaving questions. Okay.

### 02:41:14 · Speaker 4

Okay

### 02:41:16 · Speaker 1

Leibniz measure is defined that way

### 02:41:18 · Speaker 4

Bit of an elbow there

### 02:41:18 · Speaker 1

In fact, in fact, the definition of Leibniz measure is so yeah, so if you have a if you have a subset of R right, which is a closed subset of R, then the the the absolute difference between the final element and the initial element is the definition of Leibniz measure.

### 02:41:38 · Speaker 1

It is an interval right

### 02:41:43 · Speaker 1

So that's why if you take a discrete set the measure is zero isn't it

### 02:41:46 · Speaker 4

If you take individual points yeah if you take individual points the measure is zero but if you take an interval then we have a a valid measure

### 02:41:53 · Speaker 1

But it was non-zero right

### 02:41:53 · Speaker 4

No non-zero magic

### 02:41:57 · Speaker 1

See, that is why it's a very good question. See, if you have a continuous random variable or a continuous sample space, the probability measured for a particular point is zero. For instance, if we are looking at this particular example, right, of people, the probability associated with one particular person is zero.

### 02:42:18 · Speaker 1

see that it's actually like you know finding the Lebesgue measure of a of a point it's similar to that so that's why if you have you know if you have studied probability theory before people would say that for a continuous random variable you should not

### 02:42:37 · Speaker 1

interpret the probability density function as valid probability measures because the probability of obtaining a particular point right in a continuous sample space is zero just like the the measure Lebesgue measure associated with a particular singleton subset of a real number real set is zero anyway so if you understood it fine if you don't need to understand that just just ignore it okay I didn't mean to confuse you shall we move on

### 02:43:11 · Speaker 1

Now the next question is, now you understood what quality measure is on sample space, right? So the next thing is, see somebody asked me this question, right? So now what happens is sample space

### 02:43:27 · Speaker 1

rather elements of sample space

### 02:43:42 · Speaker 1

are not observed in practice

### 02:43:52 · Speaker 1

Because right what you see T I E C E right or T I C what is it T I C E

### 02:44:03 · Speaker 1

So what I am saying is you only get to see the picture of a person. You don't get to see the person. You see what I mean? If you take the elements of sample space, you don't get to see the entire sample space. You don't get to, rather let's say elements of sample space are not observed in practice in its entirety, number one. I mean, I think I just asked that question, right? When you don't observe everything, what do you do? The other thing is you don't even get to see the elements of sample space. When you do a measurement, all you get to see is that you measure

### 02:44:33 · Speaker 1

or rather not measure the theory whether you observe some real numbers when you see the speed signal you are not did that the outcome of your random experiment is speed but what you are measuring this rate of change of uh uh well i'm sorry the pressure as a function of time

### 02:44:53 · Speaker 1

How do we deal with it is the question. Somebody also asked me this question, right? Is the domain that we talk of is actually the sample space? No, because what we observe, what we get to measure and observe using equipments, okay, or sensors, is are not the elements of sample space. Now, what is the what is the how do we deal with it? Okay, that's a very important question. So for that, what is done as

### 02:45:19 · Speaker 1

Define

### 02:45:22 · Speaker 1

Therefore defining a function

### 02:45:26 · Speaker 1

Fun

### 02:45:29 · Speaker 1

Sample space

### 02:45:33 · Speaker 1

Some real numbers

### 02:45:35 · Speaker 1

So what are we doing here is that let's say that you have your sample space that are like all persons okay or rather you're doing that random experiment where you are looking at all the people okay that's your sample space. Now I define a round a function okay.

### 02:45:55 · Speaker 1

X is a function okay that will take a person or rather take an element from the sample space which is a person

### 02:46:06 · Speaker 1

Okay and math it to some

### 02:46:11 · Speaker 1

T dimensional real number

### 02:46:14 · Speaker 1

You see what is happening? What is happening? Take a first take an element from this after space okay and map it to real numbers.

### 02:46:26 · Speaker 1

Do you understand?

### 02:46:28 · Speaker 1

So if you take the example of

### 02:46:32 · Speaker 1

Red and blue

### 02:46:35 · Speaker 1

A function that we are talking about will take head

### 02:46:40 · Speaker 1

Map it to a la to write it as a function

### 02:46:50 · Speaker 1

zero the function evaluated at tail is equal to one

### 02:46:56 · Speaker 1

So here I can't write, I mean, the first example, I can't write it this way because every of my element x of person one will now become a d-dimensional vector. I mean, I can't write a d-dimensional real vector. For our convenience, it's actually a p-cross-q image. Let me write it as

### 02:47:14 · Speaker 1

We cross QDM channel to make things easier

### 02:47:21 · Speaker 1

So every of this entry is a real number

### 02:47:27 · Speaker 1

Do you understand what's happening? What's happening is because the elements of sample space are not observed, okay?

### 02:47:34 · Speaker 1

You assume that there exists a function that will take elements of sample space and map it to something that we measure or observe

### 02:47:43 · Speaker 1

See this is what we get to measure right so what do we get to measure we get to measure the observe or measure

### 02:47:54 · Speaker 1

sense

### 02:47:58 · Speaker 1

Element software

### 02:48:02 · Speaker 1

elements of range space of

### 02:48:09 · Speaker 1

of the function x that will take the elements of sample space and map into some a dimensional real space. This is what we get to observe. When we have an image, we have p cross q real numbers and every image is a p cross q real number. What is it? The way we should see it from a probability theory, probability, probability theory perspective is that what is happening is you should have the entire story in your mind. What's happening is somebody is doing a random experiment and there is a sample space. We don't get to see the sample space.

### 02:48:39 · Speaker 1

But there is another function that is taking the elements of sample space and mapping it to real numbers. And these are the real numbers that we get to observe.

### 02:48:49 · Speaker 1

Does this make sense

### 02:48:57 · Speaker 1

And do you know what this function is called

### 02:49:02 · Speaker 1

Does anyone know what this function is called

### 02:49:07 · Speaker 2

Random variable

### 02:49:09 · Speaker 1

That's the most unfortunate thing that has happened this function X is called a random variable

### 02:49:18 · Speaker 1

The biggest misnomer of all times. So this is

### 02:49:25 · Speaker 1

These are random

### 02:49:28 · Speaker 1

Why because it's a deterministic function

### 02:49:36 · Speaker 1

Not a video

### 02:49:42 · Speaker 1

because it was in the function

### 02:49:45 · Speaker 1

I don't know who named it random variable but that person has done a big mistake. This is this is neither a random this is neither random nor a variable it's actually a function that is defined between the elements of sample space to real numbers or like d dimensional Euclidean space.

### 02:50:04 · Speaker 1

Make sense

### 02:50:07 · Speaker 1

Now in the deterministic function approximation problems what we used to call as domain are actually now

### 02:50:16 · Speaker 1

The elements from the real stress of the random variable from the probabilistic standpoint

### 02:50:23 · Speaker 1

Can you see that now set of images

### 02:50:31 · Speaker 1

images that we have as data this is what is called as a data okay set of images which is data are elements

### 02:50:41 · Speaker 1

from

### 02:50:46 · Speaker 1

range space of

### 02:50:52 · Speaker 1

Another time we'll be able

### 02:50:55 · Speaker 1

It is mapping this into

### 02:51:01 · Speaker 1

You see the shift now in the deterministic function mapping scenario, in the classical scenario, our data was simply points in P2 dimensional real space. Now, they are still the points in P2 dimensional real space, but they have to be seen as the

### 02:51:22 · Speaker 1

the the elements of the range space of an underlying function okay of an underlying function oh I think this works as a pointer great I certainly previously discovered it you see

### 02:51:36 · Speaker 1

So if I do it if I do it below what I want to highlight no it will

### 02:51:44 · Speaker 1

It'll put that like invisible yellow line behind it, but it's okay, I suppose. Yeah, you see? Yeah, I was making a very, very important point here that in the probabilistic way of looking at things, the data or the images that you get are just not seen as the elements from a set. Okay? They are seen as the elements of a range set. Okay? And when you talk of range, there is a corresponding domain. And what is that domain that we talk of?

### 02:52:14 · Speaker 1

The way is the sample space

### 02:52:20 · Speaker 1

is this idea clear so every image now okay is actually an element from the range space of a function that is called an integralable which is mapping the elements of sample space to this euclidean space

### 02:52:38 · Speaker 1

Now do you see why are we doing this? You know if you can connect the dots. See the idea of identity of a person is associated with the elements of sample space. But what we are getting to measure right of c are some real numbers. Now we have to somehow relate these real numbers to the idea of the person okay which are elements of sample space. Therefore we need a connection between the sample space and real numbers which is provided by this function called random

### 02:53:10 · Speaker 1

Is this clear

### 02:53:20 · Speaker 1

Okay, uh questions, uh Ragoenta?

### 02:53:24 · Speaker 4

So this is just one function which maps it right I mean there could be many functions or many random variables defined over the same sample space so exactly

### 02:53:28 · Speaker 1

Many random variables defined over the same over the same sample space so

### 02:53:35 · Speaker 4

A and in this example say for example uh the l uh the set of persons was our sample space right

### 02:53:41 · Speaker 1

And you can define multiple random variables on top of it

### 02:53:41 · Speaker 4

I can't

### 02:53:45 · Speaker 4

Yeah for example some gene profile or something of that so so that can also become a a random variable

### 02:53:50 · Speaker 1

no no no no no again yeah see there is no physical connotation to random variables you see those functions because uh oh what you are saying is that uh what what we measure may not be um the picture it could be any total

### 02:54:02 · Speaker 4

the picture it could be in a totally different domain

### 02:54:06 · Speaker 1

Absolutely you measure the height weight of that person that becomes a relevant variable yes

### 02:54:12 · Speaker 4

Okay it's a mapping from the sample space to real some of some r some real space

### 02:54:17 · Speaker 1

Yes, yes, that's a random variable. Now what happens is, well, the next step is, because we have a measure that we have defined on these as the sample space, right, or the subset of sample space, that measure gets translated, right, into some sort of function under this random variable x also.

### 02:54:41 · Speaker 1

You see what I'm saying

### 02:54:43 · Speaker 1

Under the random variable the measure that was defined on subset of omega now will be measures that are defined on subsets of R

### 02:54:54 · Speaker 1

Look at it

### 02:54:54 · Speaker 4

Yes yes

### 02:54:55 · Speaker 1

That's called an induced measure and but that measure has a very very famous name that all of you know of that is called the cumulative distribution function

### 02:55:03 · Speaker 1

probability measure that gets translated right via a random variable the induced measure that is defined on what is called as borel sigma algebra the subsets of r are actually called probability distribution functions now the story is complete i'll write all that down because you asked i'm asking i'm saying the story is that now instead of working with deterministic functions we work with probability measures okay now those probability measures get translated into

### 02:55:33 · Speaker 1

distribution functions under random variables. Now, because we get to see random variables, okay, we work with distribution functions. So now, the entire story now is that given some elements from the range space of random variable, okay, estimate the underlying distribution function. That is all the machine learning is all about. Be it generative modeling, discriminative modeling. I will connect it to how is it related to general detection or like even chat GPD is doing the exact same thing. Given a particular

### 02:56:06 · Speaker 1

random variable observations from a particular outcome of a random variable, estimate the underlying distribution function that is all underlying probability measure actually. I'll come to that in a while. Okay, um, such in

### 02:56:20 · Speaker 4

Hi sir so uh I I did not understand this range space what what does this exactly mean

### 02:56:26 · Speaker 1

See a a a function has a domain and a range no

### 02:56:30 · Speaker 1

The range is this nothing this isn't the domain

### 02:56:34 · Speaker 4

Okay for this function this is the domain and this will be the range space

### 02:56:38 · Speaker 1

Yeah ranges are PQ

### 02:56:43 · Speaker 1

it okay and in this particular example here the the domain is again this this is the domain

### 02:56:54 · Speaker 1

Mm

### 02:56:57 · Speaker 1

Ranges discrete set of 0 1

### 02:57:03 · Speaker 1

What we see are the elements of the range space under this random variable correct

### 02:57:10 · Speaker 1

Add it here

### 02:57:13 · Speaker 2

So we cannot have a random variable which is non-measurable is that statement correct

### 02:57:24 · Speaker 1

See non measurable in the sense of uh measurability is it I mean you are talking about the measurability of a particular set are you talking about that? Yes

### 02:57:32 · Speaker 2

Yes yes

### 02:57:33 · Speaker 1

You can't know because

### 02:57:38 · Speaker 1

it is the this the because there is already a an underlying measure that is defined on the domain of random variable again please be very very conscious of the fact that random variable is a function so whenever i talk of random variable it's a function that i'm talking about okay now because there is an underlying measure that is uh that is defined that that has been defined on the domain of this random variable okay there's always an induced measure that comes with it and that induced measure itself

### 02:58:08 · Speaker 1

called as probability distribution function

### 02:58:11 · Speaker 1

See you have defined the probability measure of the sample space already right

### 02:58:16 · Speaker 1

Because of that when you define a function on top of that particular set there's always an induced induced measure that comes on along with it

### 02:58:26 · Speaker 2

And we have a set which is non-measurable meaning there is no

### 02:58:30 · Speaker 1

Yes, there can be. I mean, this is like, it's a topic of its own. There is this branch called measure theoretic, measure theory. You had study that. And by the way, if anyone of you is interested in this kind of a treatment, right, there is one very good NPTEL course by Professor Krishna Jagannathan. It's a good friend of mine from IT Madras. So I think introduction to probability for engineers or something, that's the course name. If you have interest in this kind of treatment of probability theory, please have a look at it. This is the last.

### 02:59:00 · Speaker 1

time that i'll be talking about measures and all this okay at the moment we go to distribution functions and density functions we'll work with density functions i mean i just wanted to make the footing solid right because you know people don't often understand where are these probability density functions coming into picture because when you are given some data and what is data data is simply some 10 000 images or some documents or some speech signals etc the thing is we talk of probability uh

### 02:59:30 · Speaker 1

integration functions of this particular speech or images or something what do they even mean okay i always take this one particular i mean one introductory lecture to ensure that people exactly know what's happening no when we talk of probabilities of images we actually mean that oh there is this is the this is the element of a random variable that's a function so this random variable has mapped the elements of sample space to this particular real numbers so now that sample space has a

### 03:00:00 · Speaker 1

probability measure and it is that probability that we are talking about

### 03:00:05 · Speaker 1

Okay, I just wanted to give that connection, right, you know, completely. I need 15, 20 more minutes to establish that connection before we define what genetic modeling is. Shall we do it in the next class?

### 03:00:26 · Speaker 1

Okay, so here is an appeal. While coming to the next class, please look at some of these definitions that I just told you. Okay, and in fact, we didn't cover a lot. I mean, it seems like we did a lot, but we didn't cover a lot. It was some definitions, that's all. Please have a look at them. Okay, and as I said, no, every class will have a causality, right? I mean, you have to know what we did in this class to understand

### 03:00:56 · Speaker 1

we are going to the next class with the next class we go to distribution functions and define what a generative modeling is and we go to the adversarial learning and so on okay that's how the trajectory is so please come prepared for the next class with some of these basics please look at what distribution functions are from this angle right what are density functions uh like how do you define uh density function distribution functions on this and so on please have a look at it okay i will not be talking about measure theory anymore and uh

### 03:01:26 · Speaker 1

like if you have any comments concerns etc there's always that like anonymous feedback form where you can go and express your because this was the first actual class that we had right in fact the second half the first half was only some introduction so you can go to that feedback form and let me know what you think about this and if you need any particular change i'll be happy to incorporate them

### 03:01:49 · Speaker 1

okay so any questions uh on today's content any comments i think sachin has something to say sachin uh yes sir just one question in this context of images so like one image has multiple pixels right now this random variable function which uh like takes a sample space element and converts it into this rpq so like this random variable is will be for the all the pixels of that image or like okay sir i think

### 03:02:16 · Speaker 4

Okay

### 03:02:18 · Speaker 1

was apparent anyway see we we say that our pq you know what are the what are these pq pq are the dimensions of the image so if you're looking at a 400 cross 200 image p is 400 q is 300 so basically we are saying that every image is a point in a 12 000 dimensional space okay and that becomes the the the range of the rating variable

### 03:02:43 · Speaker 1

Make sense

### 03:02:52 · Speaker 1

Okay uh anything with Arigato

### 03:02:55 · Speaker 2

So maybe just a logistic question the same book like Ian Goodfellow which explains all the theory

### 03:03:01 · Speaker 1

And see this good film book does not have any of this

### 03:03:05 · Speaker 2

Okay okay

### 03:03:07 · Speaker 1

So see again as I said no this is not a part of the course because you know this is supposed to be some fundamentals but as I said just to ensure that everybody knows what's exactly happening under the hood I do this. So next class we will we go to we'll go to the contents input for us book okay.

### 03:03:25 · Speaker 2

Okay cheers

### 03:03:27 · Speaker 2

So any books uh if we want to follow along with the lectures

### 03:03:30 · Speaker 1

before you know is if you see for this particular treatment of probability theory you look at uh professor krishna's lectures this is not needed i mean meaning uh okay i mean if you know this it's great right but this this is bare bare bone fundamentals yes after after you know this then uh then we will move on to distribution functions and so on

### 03:03:53 · Speaker 1

Okay uh person Yeah class is over I mean people can leave here

### 03:04:00 · Speaker 1

Assessments

### 03:04:12 · Speaker 1

The Prasanna are you there You want to say something

### 03:04:17 · Speaker 1

Perhaps it's not there. Okay. Uh, so thank you everyone. Uh, see you next week. Bye-bye.

### 03:04:23 · Speaker 2

Thank you

### 03:04:24 · Speaker 3

It should be clear to watch out

### 03:04:24 · Speaker 1

Should we create a WhatsApp group Should we create a WhatsApp group

### 03:04:28 · Speaker 4

How many orders do you have?

### 03:04:29 · Speaker 1

No

### 03:04:32 · Speaker 1

Let me just create a whatsapp group and send you the link

### 03:04:40 · Speaker 1

Yes

### 03:04:42 · Speaker 2

I think someone asked the question that if the

### 03:04:44 · Speaker 4

is images and what would be the range so on continuing on the same question so what kind of probability measure we should consider in that case is it like hyper volume kind of thing

### 03:04:54 · Speaker 1

what you're gonna do yeah that's that's the entire question that you ask in machine learning what is the underlying distribution that defines this particular image space nobody knows no that's what we model using neural networks isn't it

### 03:05:07 · Speaker 1

Didn't see a

### 03:05:07 · Speaker 4

So we need to find out that property measure itself

### 03:05:09 · Speaker 1

Absolutely because you know if you do that then you have solved the problem isn't it then you know everything about it

### 03:05:18 · Speaker 1

The entire machine learning is finding out that underlying measure the entire machine learning is finding out the underlying measure

### 03:05:19 · Speaker 4

I think it's fine

### 03:05:25 · Speaker 1

Particulate

### 03:05:29 · Speaker 1

I'll establish that connection in the next class. I wanted to do that in this class itself, but we ran out of time. I underestimated the time that I would take to do all this. So I'll do it in the next class. Please, maybe you can ask that question. But anyway, I'll start the next class with the answer to that question.

### 03:05:54 · Speaker 1

I was asking if we have to create uh this thing uh

### 03:05:59 · Speaker 1

Whats up group

### 03:06:03 · Speaker 2

I think Shibam has created one already sir along I mean including you

### 03:06:09 · Speaker 1

Oh that group is there I think no everybody is not there in that group so maybe Shivan can you put it in the in that teams group

### 03:06:22 · Speaker 1

I think he is not there yes sir

### 03:06:24 · Speaker 4

Yes sir I'll ping the link on the Teams group

### 03:06:27 · Speaker 1

Please do it huh

### 03:06:30 · Speaker 1

So that everybody is there I mean, I think that's the easiest way to communicate you see some resources etc we can quickly communicate and so on

### 03:06:41 · Speaker 4

Yes but it might have a mix of people who have not opted for the course not sure

### 03:06:47 · Speaker 1

It's okay

### 03:06:49 · Speaker 1

We are not you know some doing some dark state activities here so fine

### 03:06:56 · Speaker 1

And then you can say now that the people who are not enrolled in the course may opt out

### 03:07:07 · Speaker 1

Okay, see you next week then. Bye-bye. I think, you know, this long weekend, no, it's heartening to see that all of you are here for a long weekend.

### 03:07:20 · Speaker 4

Thank you so much

### 03:07:21 · Speaker 1

Thank you

### 03:07:22 · Speaker 4

Thank you

### 03:07:22 · Speaker 2

I see what you're saying
