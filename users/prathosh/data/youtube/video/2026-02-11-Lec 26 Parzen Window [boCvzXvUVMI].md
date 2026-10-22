---
id: boCvzXvUVMI
title: Lec 26 Parzen Window
url: https://www.youtube.com/watch?v=boCvzXvUVMI
date: '2026-02-11'
duration: 29:07
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Lec 26 Parzen Window

## Transcript

speaker_1: Okay So lets move on
The last family of uh density estimation
techniques uh that I would discuss in
this course are what are called as the
nonparametric density estimates Okay
We will look at that A question to
ponder upon
Can you think of uh a map estimate for
latent variable models
GMM
with a basian viewpoint Think about it
So we have GMM parameters right So
what can we incorporate some belief on
our GMM parameters and can we get a map
estimate for GMM Thats a question to
think about Huh Okay So let us now
look at uh the nonparametric density
estimates
Okay So so far
the way we have estimated density
functions
are is by estimate is by assuming that
the underlying density function has a
parametric form and try to estimate the
parameters by a kale minimization
divergence minimization That is what we
have done However
that is uh restricted by the fact that
you start with some parametric
assumption on the density function Now
what happens is in some of the
applications we may not need the entire
functional form on the density function
but we only have to evaluate the density
function at a particular point
Do you see the difference The
difference is
one you estimate the entire density
function and get a functional form
complete functional form That is one
way So you assume the functional form a
prior e and you estimate the parameters
That is one way That is what we have
seen so far Right Now there can be
another way where you can only evaluate
the density function at a given point
without knowing the entire functional
form Okay In that case you need not
make any assumption on the parametric
family from which this density function
is coming from Okay So these methods
that would not make any parametric
assumption on the density function but
only gives you a way to estimate the
density function evaluate the density
function at a particular point are the
nonparametric density estimates
Okay So let us look at some of those
methods Um
these methods
can evaluate the density function
at a point
without making any parame ometric
functional assumption
See for the case of the base classifier
that we are looking at now this is
enough Why Because finally remember
that our base classifier
chooses based on
P of Y given X right and this we know is
proportional to P of X given Y times P of Y
correct if you can evaluate this P of X
given Y at the given X thats all we
need no we dont care about what the
underlying functional form is so we can
use nonparametric density estimates for
constructing a base classifier for
instance okay not always uh its enough
to have uh uh the uh the density
function evaluated Some in some use
cases you need the functional form as
well but there are cases where you do
not need functional forms to be
estimated You only need them to be
computed at a particular point and
nonparametric density estimates will
help you do that Okay
Right So now lets look at how to do
this
Suppose
px is the density function that we are
evaluating
Okay
And we say that uh X is in uh some RD
right As usual let
capital R denote
a region
on the support of PX
Right So what is that Depending upon
what your uh uh what your RD is a region
can be a volume or it can be hyper
volume and so in general its a hyper
volume You see what Im saying Suppose
your density is supported on lets say
one dimensional space then then by this
region I mean a small line segment If
it is supported on two dimensions this
region is a is an area and in RD its a
hyper volume Okay Okay So let R
denote that particular region on the
support of PX Now
we we need to compute So let P
be the probability
of a point X
falling
within
the region R
when you sample from this particular
distribution
a point X may fall in region R or not
right so now if capital P denotes the
the likelihood I mean I should not be
saying probability its the likelihood
that this point is falling in this
particular region how do we compute that
having this much of information
now this P
is equal to can somebody tell me
 yeah it is the integral of the density
function
over the region R
Correct
Thats the definition Right
Right Now lets keep it uh at at one
hand On the other hand lets say that
we have n data points So suppose we
have n data points in our data set
We have
n data points
drawn from px
Theyre all are drawn iid Okay
Now I can model okay the event of a data
point a particular XI falling in this
region as a Bernoli random variable
data point X may may fall in this region
with some probability may not fall in
this region with one minus that
probability right so I can model that as
a bin random variable right now Ive
drawn n of them ID
right its a binomial distribution
Suppose I want to get an ML estimate for
this Bernoli random variable which is
the probability that this point X falls
within this region uh R from this data
It is the ML estimate the maximum
likelihood estimate that I get for this
particular bon random variable Right
Okay Now
if the event
of a point of a data point
falling
within
the region R
be modeled
as a Bernoli random variable
the ML estimate
What is the ML estimate given ML
estimate for
the
parameter of that Bernoli random
variable is given by
what is K here Can somebody guess
Is the K is the number of points
within the region Correct
Okay
See from our earlier analysis we also
know that this is equal to the integral
of the density function over that
region
Weve written it here
right So this is equal to from
earlier
we know that this is equal to the
integral of the density function
Right Now if
r is small enough
then I can approximate this integral as
the density function times v where
v is the
the volume of the region
Im making an assumption that within
this region right that that particular
volume the density function is a
constant Okay
that implies the estimate of the density
function at that particular point is
the estimate of the density function at
that particular point is now given by k
upon n times v
So this is the primitive estimate for
the density in a nonparametric form
Actually you have known this since your
high school
Can somebody guess what is this
This is the histogram
So suppose how are you constructing
histograms
Take a volume V right
Count the proportion of uh the volume
proportion of the samples that are
falling in that particular volume and
thats the value of that histogram and
you assume that uh the density function
is constant over that particular bin
This is exactly what your histogram
estimate is
You remember constructing histograms
right Yeah thats exactly what it is
Now we have to extrapolate this idea in
a into a d dimensional space So
basically Im saying that the estimate
of the density function at a given point
x is given by k uh by n times v where k is
the number of times that your data point
has fallen within a volume v where v is
a very small volume that is considered
around that particular point x See what
this x right where this uh uh density
function is being evaluated is the point
around which you construct this
particular volume and you assume that
within that volume the density function
is a constant
Okay Now let us uh extrapolate this
idea into I mean formalize this idea and
write it in a um
write it for the uh d dimensional space
This is a nonparametric density
estimate Okay So now here right we can
we can actually do two things One
choose a K
which means fix a K and find what is the
amount of volume that is needed to
encompass these K points
 The minimum volume
 minimum volume that is needed to
encompass those K points That is one
way to estimate the density The other
way to estimate the density is fix V
Okay and see how many points have have
fallen in that V
So that well see both of the methods
See one of the methods is called the
parson window estimate The other of the
methods is called the nearest neighbor
estimate
Well see that in a while Okay Now two
ways to do the above
nonparametric density estimates
fix B and count K
or fix K
and grow V
Okay these are two ways to do it Let
us look at both the both the ways So
lets look at the first way which is
this is called the parson window
estimate
Here we fix V
and count K
to estimate density
to evaluate density rather not estimate
Okay
Now suppose we want to estimate suppose
we want to evaluate
evaluate the density function
at a point x
We are interested in evaluating the
density function at a point x Okay
Now what we have to do now we have to
first fix V right construct a volume
around X H Now how do we construct a
volume around X
Let R
be a D dimensional
hyper cube
around X
centered around X
with length
H
what is the volume of this
H power D right Were looking at a D
dimensional uh space and we have a hyper
cube of length H Volume is H power D
Okay
Okay Now what we should do is that
given that we have this hyper cube well
have to count the number of data points
that are falling in this hyper cube
right how do we do this so to count
count k define
a window function
this sort so Call it f of uh u is equal
to
1 if
uj is within half j is 1 to d or zero
otherwise
Its just a
a unit hyper cube
Okay Uh centered around zero Do you
see this This is a unit unit hyper cube
in a dimensional space centered around
zero Right With length one So thats
what Im saying So both the sides if
the magnitude is less than half then
its counted as one or zero other It is
a its actually an indicator So if a
point is within this unit hyper cube
then it is counted as one or zero
otherwise Okay Now if I have to extend
this right to a hyper cube So if I
compute lets say f of
x minus x i divided by
uh this partic h bar d
So what does this function count
This function will count whether the
point x
okay is in the hyper cube of volume h d
which is centered around x i
You see this
If this is the definition of a unit
hyper cube right I mean this is this
is actually an indicator I mean this
this f of u is an indicator that would
tell whether a point is within the unit
hyper cube that is centered around
origin Now this one Im shifting the
origin to x i and Im scaling the hyper
cube by hd d So if you consider a cube
of volume hyper cube of volume h bar d
around x i this fe function will tell me
whether a given point or rather point x
is within
uh this hyper cube that is centered
around x i
make sense right okay now remember that
so this Ill write that this is so
indicator
or indicates
whether
whether X is within
the hyper cube
of volume
HD centered around
around XI
Okay Now do we have everything that we
need to get the uh the density We do
right So remember that the density at x
a point x is given by k
upon nv right
So what is k
So we this will give you
whether the point x i is within that
particular
uh in fact I should have written it the
other way around Right So this is
indicates whether x i
is within the hyper cube that is
centered around x See it doesnt matter
because its symmetric Right But still
uh Ill write it as uh x i is I mean
well take x as our center because we
are constructing the cube around x right
so its uh doesnt matter as long as you
define your fee to be symmetric the
explanation is the same anyway So this
is f will give you whether the point x i
is within this particular cube So this
is for one data point If I have to do
it for k data points what should I do
Ill have to do a summation here Right
So you just sum this over all data
points This will this is actually K
This will count how many data points
within my data set have fallen around
this hyper cube that is centered around
X Okay Then you divide this by N and
thats it
So this is the paren window estimate X
Okay In fact this is exactly what your
histogram is If you take your D to be
one this is histogram
Okay Now the the indicator FE function
that we chose here right This is this
is very discontinuous in the sense that
its you know its its one only if its
within this Why dont we make it smooth
in the sense that instead of hard
counting that is okay if the point is
within this cube I count it as one If
its outside of cube I count it as zero
I can make it smoother
What do I mean by this I define
So f of u can be made smoother
by choosing
few of you to be
So E power
U minus some U not
Instead of having hard bins you can
make your bins softer right by
choosing your fee to be this Now if you
make your uh
function you know f to be this
doesnt it look like a GMM
what youre actually doing is the
density at a point x is now being
estimated as a linear combination of
multiple gausian functions rised around
each of your data point
do you see this I mean its strictly not
a GMM that way but you know it looks
like the density at a given point now is
being estimated as a linear combination
of multiple gausians that are
constructed each around the data point
Okay so this is called the parson
window estimate I mean this is a
hyperparameter Okay this is a
userdefined hyperparameter You dont
have to choose this to be this
particular form You can choose it to be
anything Okay and every choice that
you make on this will impose a certain
property on the final density estimate
that you have Actually theres also a
lot of literature around the convergence
properties of these sorts of estimates
The question is does this converse to
the true density at a given point So at
what sort of choices of this is called
the kernel function by the way What
choice of kernels does a parson window
estimate converge to a true density true
true density estimate and what should be
the minimum n that should be chosen You
can construct bounds on it and so on
which Ill not discuss in this course
Does it make sense
 So now come again
So Im saying you can choose this kernel
to be anything It need not be the hard
uh uh uh bin bin that you have
constructed You can make it to be a
smoother function depending upon what
choice that you you make The estimate
will change density estimate will
change And please note there is one
other important thing that is to be
noted here is that this changes at every
x
See unlike the parametric density where
once you have data you estimate your
parameters this get fixed So this
changes for each x So that is why this
is a nonparametric estimate So every
time you make a decision lets say that
you use this for your class conditional
density and constructing a base
classifier for every data point This
has to be computed every time
You see this So a sum over all data
points have to be computed every time
that you estimate the density unlike in
the parametric case where you estimate
it once and keep it
Thats the thats why I told you right
in nonparametric density estimate case
you estimate I mean you evaluate the
density without estimating the final
functional form thats the idea
but every x you have to do it now you
have to compute this again you have to
compute this kernel for every x every
new x you have to compute this
in nonparametric density estimate what
in parametric density estimate what
happens you assume that to be lets say
a gian you get the mean and the variance
using the data you fix it you still have
evaluate but the thing is you dont have
to compute the sum every time that you
do it thats in in that way this is
computationally heavier I mean thats
constant time this is linear time linear
in terms of number of data points okay
so this is okay
 for this exponential form its not
really sort of an indicator count
 it is not the indicator of the count
yeah yeah it is yeah it is huh it okay
thats a good observation in the if you
make the kernel to be this gian kernel
right its not counting how many points
are within that uh within that
particular uh hyper cube uh it is
counting in a soft way you can say you
know its not the hard counting its the
soft
 counting point
 okay
so lets look at the other case you know
the first case was uh where we fixed V
and yeah
 okay its the question is why is this
not exactly a GMM its not exactly a GMM
because in a GMM
The gshian that you construct the
parameters of that gshian is not these
no are not these you estimate them using
the data here just simply goian with
fixed parameters that have been defined
thats it looks like gshian thats what
I said it looks like a gm but its not a
gm in this sense yeah
it should be h
Where
 here
 This is V No this is K N by VR
as Xen as X minus X
 Should it be H or HD Let me just uh
uh
 yeah correct Correct Thats correct
Thanks for the correction This is not
because for this is youre doing with
for each dimensions So its like you
shift it and scale it with H Yeah
thats correct
So H bar D appears here in V not here
Correct Thanks for that correction
Do you all see why what he said You
take that indicator function you shift
it and scale it with h where h is the
length of that hyper cube No you dont
divide it by you dont scale it with h
d you just scale it with h Its
correct Okay Uh we will stop here and
continue in the next lecture
