---
id: ENpzs2ycXJE
title: Tutorial 4 : Minmax Classifier
url: https://www.youtube.com/watch?v=ENpzs2ycXJE
date: '2026-02-03'
duration: 26:33
model: youtube-captions (en-orig)
transcript: true
---

# Tutorial 4 : Minmax Classifier

## Transcript

Hello all, welcome to this tutorial in
which we will be going ahead and looking
at one specific classifier known as the
minmax classifier.
I assume that all of you are comfortable
with the risk integral that we have seen
in our earlier discussion. And how do
you obtain the base classifier and all
those special uh cases that we have
looked at in our earlier tutorial
discussion. I'm assuming that you are
quite comfortable with these uh uh
topics.
So now we will start from the same point
let's uh
let's consider
let's consider the
two class
case. Okay, two class case. Now then we
can write the risk integral. Okay, then
the risk integral.
The risk integral is the risk for any
given hypothesis
is you
take the region of S1 of H loss occur
when your hypothesis function is saying
one but actually it belongs to class 0
into the prior y=0
and class conditional
condition on y=0
dx. Now please forgive me that I'm doing
lot of uh
uh what do you call notational abuse
okay I assume that all of you will be
able to uh understand what is that I'm
trying to write plus this is the first
one and then s0 of h
l of 0a 1
prior y = 1
class conditional L
dx.
Okay. So now in this case now since we
are considering two class case now we
can easily see a relationship between
these prior.
Okay. Now in my y the only possible
options are 0 and one. Now this is a
discrete random variable. Now
to be more specific it is a Bernoli
random variable. Okay. So now we we know
that in this case
we know that
the prior probability y=0
is equal to 1 minus
the prior and it is 1. Now when we
substitute this in our risk integral.
Okay. My
risk. Now see here uh um this is for any
given hypothesis function.
and comma 0
probability
0 integral of s1 of h class conditional
x given y =0
dx +
0a
1 -
prior y =0
to 0 of h
p of x given y = 1 dx. So now you can uh
rearrange the terms and then this will
become
laws incur and hypothesis says zero
but
actually it belongs to class one to s0
of h and class conditional
dx
plus
P the prior Y equ=0 into loss comma 0
S1 of H
as conditional
0 dx minus
Z of H.
Now by rearranging the terms
uh this is what I get. Now this you can
immediately see here
that for a fixed classifier okay for
any h that you have under the constraint
that uh you're having so the loss when
both of them says is equal to
it's one as zero okay and then you have
a two class case under all these
constraint now you can see that the risk
which is there is linearly varying
with respect to the prior.
Okay. So now let us make a note of that
point. Note
this
indicates
for a
fixed classifier
for a fixed classifier
risk
varies
linearly.
with prior
probability.
Okay, I assume that
from this equation you can conclude the
specific statement.
Okay, so now see this is for any any
classifier. No, see here I'm not uh uh
going ahead with any specific uh group
of classifiers. this this is working for
any fixed classifier. So now what I will
do is
I will have a separate group of
classifiers called as minmax
classifiers. Now where in which
this will become zero. What do you mean
by this will become this one? This term
and this term are same. Okay. When you
have such a classifier that is known as
the minmax classifier. Okay. Now let's
make a
point in that. Now we are looking at
minmax classifier.
Sometimes uh
uh they also write it as minax
classifier. Okay. The minmax classifier.
Now consider a classifier
such that
the loss
incurred in this case
s1 of h
x given y =0 dx
of 01
0 of h
that x given y =
dx. So any given classifier which
satisfies this constraint.
Okay. Now that is when we call such a
classifier as the minmax classifier. In
that case what will be our risk? Okay.
for this specific classifier.
For
this classifier,
the risk
would be
of
H
M. Okay, I call it as min max is equal
to L of 01
integral
0 of H
and then this you can see that this
particular
risk which is there is independent of
prior.
Okay. Now the risk of a minmax
classifier is independent of prior
this case
risk
would be
independent of
prior.
Okay. Now because of which we can come
up with a very neat uh one diagrammatic
representation which is like this.
This is the direction of
risk in y
then
prior
in x.
Now
this can be seen that
now as you vary the prior
your risk varies in a quadratic form.
This we have seen while looking at this
is our base risk. Okay. This is our
base risk.
Now
for any given fixed classifier if I go
ahead with this this is linearly
uh dependent on the prior. Now for a
fixed classifier. Now what happens is
okay
tangent. It's very hard to actually
tangent in most of these cases. Okay.
Okay,
please consider this as a tangent. Okay.
So this is
this case
risk
grows
linearly
with
prior
for
any
fixed classifier.
Now how will be our minmax classifier
look like? Now
this is how the minmax classifier.
Okay,
this is a minmax classifier.
This is independent of prior.
Okay,
I assume that you can appreciate this uh
given thing. So in this case
the risk is linearly
modified linearly changing with respect
to the prior
a base risk will be in terms of
quadratic change but our minmax
classifier
uh will be
not dependent it's independent of prior.
Okay, now let's uh
delve deep into it.
You know, now suppose now
suppose
in our uh now okay what's the condition
for my classifier? Let's copy that
condition.
This is the condition for the match
classifier.
Okay, there's one good thing about uh
using iPad. So you don't need to copy.
So in this case now suppose
suppose
in the
above condition
suppose in the above condition
now we have the loss
incurred in the case of mclassifications
be same. Now then what it turns out to
be now it turns out to be that
the integral
of
s1 and s0's regions over uh
the class conditions of
y= conditioned on y=0 and y= 1 will be
same.
Okay.
And this will come out. So now let's put
some more uh uh restrictions on it
saying that we will take an
one-dimensional feature and then we will
assume that the class conditionals are
uh Gaussian distributions and then see
how does the the overall picture turns
out as an example of things. Now for a
simple case.
Now now you you will be able to see that
this is the same thread that we are
following. We will come up with uh
generic formulation and then uh now from
there we will get a specific one and
then we'll put on some constraints on
the uh
on the nature of uh the distributions
and then we will see a special cases as
we go along. That is what we are doing
now
for a
simple case
of
onedimensional features.
One-dimensional features
normal
class conditionals.
normal class conditional densities.
Okay. Now let's look at it. Now what is
that I'm saying? Uh the class
conditional is
is normal
with parameters
mui
and sigma i squared. Okay. And uh it's a
one-dimensional feature. So and assume
that let's assume assume
without loss of generality
mu not is less than mu1.
Now then if you recall in this case now
how will be my h of x will be zero if
and only if my x is
less than a. See this a is the threshold
right now we can go back and then look
at it. This is what we have obtained.
Okay. So now
now what we will do now
we will
fix a threshold
so that it satisfies the minmax
condition. So we will fix the threshold
should a
to
satisfy
the minmax criteria. What is the minmax
criteria again? Now this is the the
minmax criteria. Okay. Now in that case
a special case you can consider this uh
where in which this condition is
satisfied. Okay.
Now satisfy the
the min max
criteria.
Okay. Now how it will be? Now how does
it look like? Now integral
a to infinity
x given y =0 dx equals minus infinity to
a
So I assume that you'll be able to
understand this. Uh okay. So let me show
you this. Okay. This is for some other
thing but you can say that this is class
zero. This is class one and this is our
condition. So okay now what is that? I'm
saying that in this region. Okay. Now
what is happening in this region? What
is happening? Okay. This is from a to
infinity a to infinity you are looking
at this blue region from minus infinity
to a you're looking at this orange
region okay that's what you're actually
looking into now we will come to this
specific diagram I just wanted to show
you this uh overlap that's all okay now
that's what this this is that's what it
is saying so I want a criteria when this
is taken care of okay
now assume diagrammatically it makes
sense. Okay. So now if you want I can
rewrite it but so yeah my
this is
one distribution and then
there okay and
this is your A.
Okay.
Now
this is
class zero
class one what is that I'm trying to say
from
now this is the risk right this is
mclassification that is happening so
from minus infinity till a okay from so
what is the region here from a to plus
infinity where is a
taken Okay. Now that's what I'm saying
trying to say it using this uh graph.
Okay. And
I want the area in these cases to be
same. Okay. That's what I'm trying to do
it. Okay. Fine. Good. So now
these
will become
the
integrals of
standard normal.
I'll leave a bit of algebra for you.
Okay. Now what do you use in the first
integral?
So you need to use Z = X - MU by Zigma
KN
for
first integral
and the second integral substitute
Z with X - mu1id by zigma 1
for
second
integral. Okay.
Now because of which what will happen?
Now these are uh uh
normal distributions. Now because of
which now the threshold should satisfy.
Now if you uh take care of a small bit
of algebra that I have left behind.
Now the threshold
the threshold should
satisfy
what 1us
f of a - mu /
sigma
equals
f of a minus mu1
by sigma 1. Now it has to satisfy this.
Okay. And
we already know that what happened to
this.
Now
we know that 1 minus
f of z equals
c.
Okay.
Minus sorry. Okay.
Okay. There's a minus here. Now because
of the substitution it will be f of mu -
a
by sigma
equals f of
a minus mu1 by sigma 1. Now this will
turn out to be mu - aid by sigma
= a - mu1 / sigma 1.
Here a equ=
mu
zigma 1 + mu1
zigma
by zigma + zigma 1.
Okay.
So now what do you see?
Now this is how you get to know the
value of your threshold which satisfies
the the minmax criteria. Okay. So now
what can we say from this?
So now minmax classifier is linear while
base classifier for the same specific
consideration was quadratic.
Okay. And when sigma 1 is equal to sigma
is equal to sigma then
this is same as the base classifier
in this special case. Okay that is
minmax. Let's make this observations.
Now here
we can
observe that
first one
minmax
is a
linear
while
the B's
classifier for the same case
classifier here
for the
same case is quadratic.
Okay. The second observation that we can
make when we have
when
sigma KN equals sigma 1= sigma
minmax
is
same as base
in this special this.
Now you can appreciate that
we can have specific
conditions applied on the classifier
and then we can obtain classifiers
which are independent of priors. And
then we saw an example how does uh in
the case of Gaussian it behaves. Okay,
with this we conclude our discussion on
minmax classifier. I hope you enjoyed.
Thank you. Let's meet in the next
tutorial.
