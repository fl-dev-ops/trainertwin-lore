---
id: YZ3Xa6dEMl8
title: Lec 27 Nearest Neighbor Classifier
url: https://www.youtube.com/watch?v=YZ3Xa6dEMl8
date: '2026-02-11'
duration: 17:32
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Lec 27 Nearest Neighbor Classifier

## Transcript

speaker_1: So lets look at the other uh way to do
it which is uh okay by the way u see
using this smoother kernel also avoids
this uh this problem of getting a very
discontinuous estimate for the density
cuz what happens is if you create bins
especially in higher dimensions given
some data there can be a lot of bins
that will not have any data points at
all
right because your data is sparsely
sitting in high dimens dimensions If
you construct bins there can be a lot
of bins where you dont even have have a
single data point If you smooth it out
then every bin will have some data
points because this every bin now has
infinite support No So that the
density will also be smoothened that
way Okay Okay So let us uh look at uh
the the next uh uh variant of this which
is the nearest neighbor estimates or
here
its a nonparametric density estimate
where
what did we do in the last case
We fixed
V and counted K here
Fix K
and grow V Yeah
So we have P
is equal to K NV
Okay Now what you do is in in in high
dimensions
choose a particular volume and see how
many data points have fallen in this
particular case particular volume
Okay And that will give you the density
estimate Now how do you do it in
practice
Let us look at one example to do it in
practice How do we actually do it in
practice Uh now
example use case
Lets construct a base classifier
with
nearest neighbor density estimate
for the class conditional density px
given y do you understand what Im
saying so So we are now constructing a
base classifier Okay
To construct a base classifier we need
the class conditional densities to be
estimated
And we use nearest neighbor density
nonparametric nearest neighbor density
estimate for class condition estimate
Evaluating the class conditional
densities
Do you understand this Any questions on
this This is very important because
algebra is easy Understanding is
difficult
Do you see this Any questions on this
So let us do that now
Okay
Now suppose
suppose we want to
estimate the class
of a sample
X
We are given a sample X What we want to
do is estimate the class corresponding
to that particular sample And how does
a base classifier do this See this the
analysis that we do right now is sort of
connecting all the dots that we have
seen so far So we are constructing a
base classifier and we want to get the
class of a point X Okay for that we
need to get the posterior of y given x
this particular x Okay so lets lets
do that Now suppose um so we place
a volume
volume V
around
around X
and capture
K samples
So we have to create a volume V around
this X So in the nearest neighbor
density estimate nonparametric estimate
what do we do Given a point we want to
estimate the density at that point
Okay Uh you keep growing a volume V
around that point till you get K points
Okay
Okay Now suppose we are looking at a
binary classification problem Okay So
let
k I be
the number of points
within volume V
corresponding to the ayat class
Correct So you have a point X construct
a volume around it So you get K points
within those K points Lets say K 0 are
from class 0 and K1 are from class one
Okay
Now this actually means you know in fact
it doesnt have to be a binary
classification problem It can be a K
classification or okay K has already
been taken Can be a
 ML classification problem Yeah thanks
for the alphabet suggestion
So it can be M classification problem
So what happens is now you have sigma of
KI
I equals 1 to M now is equal to K
Ill write this example use case is
mclass classification
Were looking at an Mclass
classification problem Okay So this is
okay No all kis they sum to one Sorry
they sum to k because there are k points
out of which you have k1 from class one
k2 from class 2 and so on Okay Now
the nearest neighbor density estimate
for
the joint density of X and the IT class
is given by what
Okay what what are we looking at We
are looking at the nearest neighbor
density estimate for the joint
distribution of x and yi for the iat
class What is it So we know that it is
k by nv right
because we are considering iat class
This will be k i
Does it make sense So the estimate for
the joint density of x and yi This is
the nearest neighbor estimate by the
way So where we have
grown a volume okay till it encompasses
K points within those K points KI are
from the IAT class okay
okay now
to construct a base classifier
actually when I started no this is a
density estimate for P of Y given X not
X given Y cuz the base classifier
decides based on P of Y given X right to
construct a base classifier we need P of
Yi conditioned on X what is this equal
to this is
the joint density
divided by
the marginal
Correct
Is this correct Yeah This is equal to
what is the denominator So you take it
for all classes right
which is K by NV right So this is equal
to
is what it is Now what is the final
base classifier
This is my base classifier right It
decides on the ayat class if the
posterior of the ayat class is the
highest amongst all posteriors Okay
this is equal to take I if
correct
is this correct
all of you with me Why are you perplex
We just got the estimate for uh yi given
x So just writing it that way So I can
I can uh leave uh uh k write the class
is equal to i if ki is greater than kj
Now what is this
given a point x okay what am I doing
Im taking a volume around x
Okay and seeing
how many points in the data set
within that volume correspond to the i
class and j class and con and deciding
the the class of that particular point x
as the one
okay
that has the highest appearance within
that volume
 this is the k nearest neighbor
classifier
okay this is exactly what is called as
the K
nearest neighbor classifier
How do we choose volume
using some distance metric
The question is how do we choose the
volume Okay given a data point
you look at in fact you can choose the
volume to be the one that encompasses
all the data set
Right Given a data point okay look at
the look at its neighbors in the entire
data set and count how many how many
points corresponding to this ayat class
and do it or okay you can choose uh two
see thats why its called k nearest
neighbor because you can restrict five
so you can look at five nearest
neighbors
So take a distance metric okay and take
that that amount of volume that
encompasses five points
of
 doesnt matter five points that is why
its called the five nearest neighbors
okay look at construct the volume okay
such that it encompasses k points and
within those k points construct a base
classifier thats it
 it seems like volume is also a parameter
it k is a parameter
I mean of course volume is a parameter
through K See when you if you if you
take K to be lets say 10 then you are
implicitly looking at a volume isnt it
Okay So here is the punch line
A K nearest neighbor classifier is a
base classifier
with the estimate the density estimate
for the joint density of data and labels
estimated as the nonparametric density
using the nearest neighbor technique
Thats what we saw
Correct So what is a nearest neighbor
classifier Given a particular point
its a its a nonparametric classifier
right in the sense that given a
particular point you want to choose its
class
fix a K look at its K closest neighbors
and count all classes right within those
neighbors and decide the class based on
the one that has the highest appearance
thats exactly this base classifier what
are we doing implicitly is that we are
constructing a base classifier okay to
construct a base classifier we need the
density estimates the density estimates
are taken to be nonparametric density
estimates and within the nonparametric
density estimate You choose the nearest
neighbor density estimate to estimate
the density that is needed to construct
a base classifier and that becomes what
is known as a nearest neighbor
classifier
Okay So one way to start an ML course
is to start by saying that nearest
neighbor classifier is the easiest or
the most primitive classifier Okay
that is that is there In fact there is
a very powerful result that says that
the
error that is error in terms of the risk
okay that is associated with the nearest
neighbor classifier is at most twice
that of the base error thats a result
okay Ill just state that without proof
you know the this this one of the books
that Ive referred to this duda hard
right pattern classification proves this
result what Im saying is that the the
error that the true error the true risk
not the empirical one the true risk that
is associated with an nearest neighbor
classifier is
at most twice that of the base
classifier So if you are constructing a
you know hyper uh complex classification
methodology that is doing worse than the
nearest neighbor classifier discard it
because this is the easiest thing that
you can do right given some problem just
come and by the way you you have to
choose a distance metric here
okay thats a hyperparameter I mean you
can choose any your any of your favorite
distance metrics depending upon your
distance metric
uh you build a k nearest neighbor
classifier Okay in fact you can also
build a one nearest neighbor classifier
where you grow the volume such that you
look at the the closest point within the
data point data set and uh you assign
the class of that to this particular
data point Thats it So thats the
easiest classifier So the easy the
easiest thing that you can do to solve a
classification problem is to look at is
to construct a nearest neighbor
classifier and nearest neighbor
classifier is also a base classifier
with this as the density estimator
Okay
this is like deriving known results
using you know unknown concepts Okay
that thats thats fun actually right
thats what the abstraction will give
you So every every known thing will
become a special case of this large
family of models that we are looking at
So this completes uh the density
estimation part of this particular
course From the next class what we
will do is we will go back to the erm
world view the empirical risk
minimization worldview and I will
specifically look at uh discuss the
linear models to start with The linear
family of models from the erm
perspective Okay we have already seen
that we have already seen that a linear
model with a particular loss function is
equivalent to getting a ML estimate for
uh the the density with a particular
assumption on the class conditional
density is what we have seen Well
reinforce that idea I talk about the
generalized linear models the so called
linear and polinomial regressions Okay
And then we will move on to the uh the
regularization bias variance
decomposition and regularization ideas
which is nothing but the map estimate
its equivalent to the map estimate So
that will end uh one uh the first lap of
this particular course So we will start
with the linear models from the erm
perspective starting next class Okay
See you in the next class Thank you
