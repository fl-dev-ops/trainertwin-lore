---
id: 8esVIly2TZY
title: "Tutorial 5 :  Neyman Pearson Classifier"
url: https://www.youtube.com/watch?v=8esVIly2TZY
date: '2026-02-03'
duration: 48:59
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

speaker_1: Hello all welcome to this tutorial in
which we will be looking at
 one more specific uh
special group of classifiers
called as Neman Pearson classifiers or
NP classifiers
Until now we have seen base classifier
and then we have seen uh minmax
classifier during our tutorials
discussions
Now Im uh showing you this specific uh
base classifier
Now now you can see here that the base
classifier minimizes risk Now whenever
the condition is now it is minimizing
the weighted sum of all errors
Now what do you mean by that is now
every error is uh given equal kind of
importance Okay Now in real time that
might not be true Sometimes you give
more emphasis on one kind of mistake
rather than another Okay So now
whenever you have these kinds of
conditions on which you have to develop
classifiers Now then we look at the
Neiman Pearson criteria and then go
ahead with that In this tutorials lets
look at this specific Neman Pearson
criteria So now lets proceed
So now here we are looking at the
Neiman
Pearson
classifier or NP classifier
Now it is evident Lets make that point
that we just saw in the base classifier
The base classifier
minimizes
the
Okay Now it uh
minimizes
weighted
sum of
all errors
Okay See even we can have different
kinds of uh magnitude of errors Now
because we have the control over L of I
comm J we can have different kinds of
errors Now what do you mean by that is
it looks at uh into consideration every
possible error together Okay Now it it
will not give a specific kind of an uh
advantage for one kind of error against
another Okay Uh so thats what we want
to try in this thats what we want to
look at in this NP case Okay So now
in some cases
we may not
explicitly
want to trade off one kind of error with
another Okay thats what happens in
the base case Okay they might not want
to
trade off
one type of
error
with
another
Okay So now what do you mean by
different types of errors So now lets
look at this Now all of us remember the
bad times of code Lets take that
example itself Now we have two kinds of
errors Now whenever we are dealing with
a binary
uh outcomes whenever our hypothesis
function has two outcomes So
we have type one error
also known as the
false positive that is falsely
classified as positive Now the example
that you can think is falsely classified
as positive in the sense youre actually
negative but the result the test is
saying that youre positive
Okay
Test is saying that youre positive but
you you are not actually positive Okay
So now
result says
you have
corona virus
virus but
you actually
dont
This is false positive Falsely
classified as positive
Okay this is the type one error Uh
then you have
type two error
uh
type two error is
false negative
Now falsely classified as negative that
means that you actually is having CO but
the result says you dont have okay
test result says
you
do not have
corona virus
But
we actually do have
the two have corona virus Okay Now
these are the two kinds of uh errors So
now in any given case you know we want
the false negative
Okay Now we want to reduce this false
negative Now keeping this false
positive
under some threshold
Okay So what do you what what does that
boils down to Lets write it in terms
of equations So we want to minimize we
want to obtain a classifier
which is uh
uh very good at reducing false negative
simultaneously now keeping this false
positive
now below certain threshold Okay So we
want those kinds of classifiers So now
we want to realize how to do so Okay
how how do we frame the problem is the
next uh idea that we have okay so lets
do that
now what is that Im saying in some
cases
in some cases
we need to
some cases we need to minimize
we need Minimize
type two
under the
constraint
that
type one
error
is
below
some
threshold
that means that there are two things now
one is now what do you do first you say
that okay now what are the group of I
have a class of hypothesis function now
whichever of these hypothesis functions
satisfies the condition that type one
error is uh
less than some threshold out of all of
them that we have selected We want the
one that reduces okay type to the most
Okay Now this is what we are looking
at Okay So now lets write it in terms
of equations So it will be pretty
comfortable to write this
So now
how does it turns out The first one is
now now we know this Now whenever we
say that its an error readers
probability that a hypothesis I call
this NP ne
it is saying it as one given the actual
examples belongs to class zero right
this is what type one means right
uh actually you dont have
but the result says you have
okay thats But this is the type one
error A type one error has to be below
some threshold
Okay Now this is the first condition
Now the second one is now among all of
them which satisfies
x0
given
x belongs to c1 Now this is X belongs
to C1 that means that it is actually
positive but my classifier is saying it
as
negative This is false negative Okay
The false negative which is there should
be less than all other classifiers that
we have considered
Now for what For all hypothesis
H belongs to H
such that it satisfies the first
condition that is probability that H of
X equals to 1 given X belongs to C not is
below certain threshold That means that
you choose all the classifier which
satisfies this condition and then you
choose the best among them Thats what
these two conditions boil down to Okay
Now I assume that now all of you are
able to see how these statements is
realized in terms of equations
Okay
So now
lets make note of them otherwise
now the type one error
type one error of hypothesis function NP
is
bounded
above
Right by
and then
among all the
among all
classifiers
that
satisfies
this bound
on type one error
NP classifier
has
least
type to error
Okay is this clear This is what the
conditions that we are looking into
Okay
So now how does this boils down to
uh
hypothesis function in P for a given
input X says one
if
the
ratio of class conditionals
is greater than K Now Ill show you how
does this condition finally satisfies
both of our conditions Okay that we
have okay
zero otherwise
Okay now
again
now should always say given
the
bound on
type one
error is
alpha
Okay Now then this satisfies Now now
what do you mean by this So now this
boils down to now what is the
the case Now how should be the K
where
K is such that
the probability
now given the ratio of these uh class
conditionals
is less than or equal to K
given
x belongs to c
is 1 minus alpha
correct now when this particular thing
is less than k now that is when I say
zero
uh this is 1 minus alpha
it is just saying then
actually saying this
correct
Now you want
to come up
with a with a classifier that satisfies
this
Okay Now this condition actually means
that youre putting it under zero
Okay
Fine Now using this now we have to
prove that that this specific classifier
that we have got satisfies the NP
criterion Okay Thats what if we prove
that we have obtained the nean p
classifier Okay So now our whole point
now boils down to
now we now prove
now prove that
this classifier
that we have considered
that we have
considered
satisfies
an even creation criteria
Okay Now if this particular classifier
satisfies that we are done
correct So now lets do that How do we
take care of that Okay
So now the first uh uh thing
Okay
Now
the threshold K
is chosen in such a way
says that the probability
uh that
ratio of conditionals class conditionals
are or equal to K
given
X belongs to C not
is equal to 1 minus alpha
Okay this is what we have considered
This is the way in which I choose my
value K Now what is what did this boils
down to Now this boils down to
hence by construction
by
hence by constructions we have
probability that
x given y equals 1 The ratio x given class
conditional is greater than k given x
belongs to c not is alpha right this by
construction
okay what is this now when it is greater
than k what do I do I say that it is
actually
class one now thats what my neman
pearson condition the first condition
If you look at it
it has to be less than or equal to
alpha Now we have achieved by
construction by choosing K in this way
Now we have taken care of the first
condition Okay Now this is probability
that
the new PSN classifier for a given X
will be one given that it actually
belongs to class zero is equal to alpha
Now this satisfies the first condition
Okay
this
satisfies the
the first
condition Okay
So now now we have uh uh if the
classifier that we have specified by
choosing like this Okay Whatever
classifier that satisfies this is taking
care of the first condition that means
that the type one error is bounded above
by alpha Now that is taken care now So
now what is that we have to show now We
have to show that the type two error is
there is the least among all the
classifiers that is satisfying this
particular condition Okay So now lets
do that Now this satisfies the first
condition Now lets look at the second
condition
So now now
we need to show that
show that
now whenever it is its type two
error
is
less than
Other
classifier
satisfying the constraint on type one
error Other classifier
satisfying the
satisfy the constraint on
type one
error That means that
uh for every classifier that has uh
satisfied this uh my
new pear classifier will be having the
the least type two error Now this is
what I have to show for this particular
classifier The second condition is
satisfied is what I have to show now
Okay So now lets do it
Now let
H
be any classifier
Let H be any classifier such that
of X equals to 1 in X belongs to zero This
is false positive is less than this And
then
to complete the proof
complete the proof
we need to show
we need to show that probability of
NP of X is zero given X belongs to C1
is less than
01
This needs to be show or equivalently or
or equivalently
you have to show that
probability that
of NP of X equals to 1
given X belongs to
C1 one
Okay Now whether you show this or you
show this its equivalent Now we can
easily see this Okay Thats what we
have to show
Now actually well be showing this which
will internally prove this and then we
have already pruned the condition one
Now therefore what happens is the
classifier under consideration is
actually an MNP classifier thats how we
will conclude the proof See Im
reiterating the whole proof process
because uh it involves steps Okay So
that reiteration will
reinforce
Okay So now lets proceed
Now consider the integral
consider the
consider the integral lets call it I
So its not its not an indicator random
variable or uh even a what do you call
identity matrix Okay This is just an
integral that Im considering Okay So
now we will be reusing these symbols
Now depending on the context you should
be able to understand what does this
mean Okay That much of comfortability
with notations should be there
Okay
Then
x given y equals 1 of x
k into
p x given equals 0
fix
dx X
okay lets consider this integral now
why are we we will come there now it
will be pretty much clear
okay so now
this particular uh integral which is
there now can be divided into
two parts okay now where in which uh we
have the class conditional y given 1 is
greater than k into the class
conditional y is equal to0
is one case and then the the complement
of it Okay Now I write it it will be
clear See whenever there are multiple
steps I prefer to write one step in one
color the next step in another color so
that you know that one color means one
whole equation The equations uh uh uh
will be a bit lengy It might take two
lines sometimes Okay Now this will be
integral
x given equals 1 is greater than k into
 equals 0
of np of x minus
h of x
into
 equals 1 of x

k into
x
dx
Okay Plus
now another
integral
x given y equals 1
is less than or equal to k into the
class conditional y equals 0
h of np of x minus h of X
P of X given Y equals 1 of X
okay okay
this whole I have divided into one part
which satisfies this other part which
satisfies this Now this can be
similarly seen as the parts of the two
gaussians that is there Just for the
sake of understanding you can look at
this Okay fine
The first thing that we will show that
this specific integral that we have is
always
uh non negative
Okay What is the use of that Okay We
will see that Okay And the first step
in uh proving this is that this specific
integral
this and this both of them are non
negative Thats what Ill be proving
now
Okay
So now we need to
we need to show that
this
integral is
always
non negative Okay that we have to
show show first now Okay so now we
will take individually each of them
Okay Now first we will take the
the first integral
Okay Now
first
integral Now
when
x given x equals 1 of x is greater than
its given y is equal to
0 of x So now because of this you see
this under the condition now this is the
first integral that Im considering
now this is this is greater than this
now that means that this is non negative
now I just need to show that this is non
negative thats all this is non negative
now why because of the region under
consideration this is non negative
therefore I just need to show that this
is non negative okay that will satisfy
the first integral the same thing with
the second integral second integral this
I should show now this will become
negative because of this condition
therefore this also has to be negative
so negative into negative will become
positive sum of two positive uh things
you know will be positive that thats
how I show this okay fine so now
h np of x minus h of x now whenever you
have this ation
that is
you take this now you can push this
downwards
Okay Now that means that the ratio of
class conditionals is greater than K
Now whenever the ratio of class
condition is greater than K Now then
what will be the outcome of your Neman
Pearson classifier The classifier will
say that it is 1 minus H of X Now
irrespective of the value of this H of
X Now this will always be greater than
or equal to zero See now since we are
considering a two case now h of x can be
zero or one Now if it is zero yes this
is one If this is one then it will be
zero In all the it is greater than or
equal to zero Now that means that
the first integral which is non
negative
So now
now I have just shown that the first
integral is non negative Now this
implies
first
integral is
non negative Now lets take the second
integral
Okay
Now
now the second integral
Now what is the condition of the second
integral This is x given y equals 1 of x is
less than or equal to
k into
0 and we know that this is negative Now
why do we know that this is negative
Now this is lesser Now lesser okay
there has to be a k here Sorry Somehow
I missed the k here There has to be a k
here
Okay
uh this will be negative
So now what I should show now
h of NP of X minus H of X Now whenever
this particular condition is satisfied
now this will be zero minus H of X
Okay So now this will always be less
than or equal to Z Why Now if H of X
is giving you 1 then it is minus one If
h of x is giving you zero it is zero
Okay
that makes sense right
Now whenever h of x uh
is giving you one Okay I just said
that Okay now this will take care of
our condition
Okay Now which will say that now my
this will imply
this will
imply
second
integral is
non negative
Okay Now by summing both of them Now
therefore now therefore
therefore the integral I is greater than
or equal to zero
I can come to this specific conclusion
Okay
So good Now now why is this needed
Lets take this
integral
Me just copy that specific integral
This is one great advantage about this
Ill just copy
Okay this which is there you know that
this is
greater than or equal to zero We have
come to this place So now what I can do
is I can uh uh expand the terms inside
and then I can mix and match couple of
things Okay
So now if I do so my overall will be
integral h np of x into probability that
x given y equals 1 of x dx This is this term
and this term
minus
integral
h of x p of x given y equals 1 of x
dx
This is this term and this term
Okay
Now
can can
combine this
this whole thing
This is greater than or equal to
k
into
integral of
h of np of x
x given y equals 0 of x
dx
minus integral of
x probability that x given into x
this
I can obtain
Now
lets look at each of these terms Now
how will it look like Now I have 1 2 3
4 I have four terms
Okay we will look at each of those
terms and then we will be converting
them into errors
and then naturally the condition that we
need comes out Okay we dont need to
force that condition anymore
Okay so
now what are those four terms that we
have
Lets get each one term and in the same
order that Im getting it The first one
is
integral with respect all of these are
integral with respect to RN So okay h
of np of x
that x given y is equal to 1 of x
dx
Uh
what is this
This will be the probability that h np
of x equals to 1 given x belongs to
c1
Similarly the second term
h of x probability that x given y equals 1 x
dx This is probability that
h of x equals 1 given x belongs to
c1 Okay
this is clear Now lets look at the
remaining uh two integrals Now integral
rn
h of
np of x probability x given y equals 0 of x
dx Now this is the probability that
h np of x equals to 1 given x belongs to c 0
Can easily see this
again
the last term
Rn
H of X
that X given Y equals 0 of X DX equals
probability that H of X equals 1 given X
belongs to
C O plus 0
So now now if you substitute
these terms
in this inequality
if you substitute these terms into
inequalities lets see now you
understood why were we looking into the
condition that the integral has to be
greater than zero okay so that I can
take care of that shuffling of things
okay so now now
therefore the overall inequality that we
had earlier for that integral Therefore
the
overall uh
inequality will look like its
probability that h of np of x equals 1 given
x belongs to c1
minus probability that h of x equals 1 given
x belongs to c1
is greater greater than
equal to K
into
probability that
H of NP of X equals 1 given X belongs to
C 0
minus probability that H of X equals 1 given
X belongs to C zero
Okay
So now
do we know this
Can we
take care of this condition Now lets
look at these terms and go back to our
uh
conditions
Does this
okay rather than this
Okay So no need lets lets uh directly
go ahead
for uh all hits under consideration
Okay Now what happens is now what is
the the first thing that uh the type one
error Okay Now which is uh
has to be uh bounded uh less than or uh
equal to alpha Now because of which
what will happen this
now for all the h under consideration it
will be true for whatever h that you are
considering So this is
alpha Now this is alpha So now it will
be greater than or equal to zero which
is non negative Now that means that
this whole term which is there will
become non negative because of the
first condition which we have already
satisfied And what are the hs that we
are considering We are only considering
those hs that satisfies that the type
one error has to be uh uh bounded above
by alpha Now because of that okay now
lets write that but
for
all H
under consideration
under consideration the the RHS above
is
non negative now why is this non
negative because of the the trivial
ality of the first uh condition that we
have taken into consideration Now
therefore what happens
Therefore now this will directly say
that the probability of H of NP of X equals
to 1 given X belongs to C1
minus probability that
H of X equals 1 given X belongs to C1
is always greater than or equal to zero
This is exactly what was your second
condition right
Go back to this
Now you just the probability is uh a
non negative entity So you can shift
it here and then the inequality still
holds
Okay Now I have proved this
Now since I have proved this now proving
this particular statement is equivalent
to proving this statement Now we have
already taken into consideration the
first condition Now therefore the
classifier that we have considered is
actually an even pearson classifier
Thats all that ends the proof
This is QED
Okay
this completes the proof So now a
couple of uh points to be noted with
respect to the base classifier and this
and then we will conclude
So NP classifier
NP classifier
also
needs the
needs the knowledge of class
conditionals Otherwise that was your
first thing right in the hypo in the uh
definition itself you have said that how
do you choose k the ratio has to be
greater than k that is so you you need
to know the ratio of class conditions
okay
class conditional
densities
okay similarly even the base classifier
is uh almost needs this ratio of class
conditional Now
similar to
base classifier
where
it also
is
based on
the ratio
X given Y equals 1 of X
Correct So now in base classifier what
do you do Now
in base classifier the generic uh
version which we have considered in base
uh
classifier
we say
class one if
the ratio of class conditionals else
is
0 1
this has to be satisfied Now exactly in
both the base classifier and the neman
pear classifier you need this ratio
Okay So now finally to put the whole
thing to rest
in Neiman Pearson
the threshold which is very important
K is
set
based
on the
allowed
type one
error
Okay
this
uh to an extent conclude uh our uh
discussion on neman pearson classifier
Now in the next tutorial now what uh now
we shall be doing is well be taking an
example of Neiman Pearson classifier and
then we will see that a very interesting
idea called as ROC how naturally comes
out of this specific uh case of Newman
Pearson classifier
uh and then we will look at the
usefulness of this ROC curve Okay with
this we conclude this tutorial in which
we looked at the Nian P classifier
Well meet in the next tutorials I hope
it was interesting Thank you
