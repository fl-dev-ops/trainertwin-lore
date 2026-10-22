---
id: sOwgRt6uiA4
title: Tutorial 8 : Computation of EM for GMMs
url: https://www.youtube.com/watch?v=sOwgRt6uiA4
date: '2026-02-11'
duration: 40:48
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Tutorial 8 : Computation of EM for GMMs

## Transcript

speaker_1: Hello all welcome to this tutorial
in which we shall be looking at GMMs
So in the earlier discussions
so it is uh pretty much evident that the
need of mixture models
In this tutorial what we shall do is we
shall take the Gaussian mixture models
and then we will derive the closed form
solutions for obtaining the parameters
So
the we will be using the exact same
steps that are there in uh em algorithm
But since
it is easy for us to equate
the expectation that is there to zero
while optimization and then obtain the
closed form solution Now we shall be
doing that Okay Uh so without any
further delay so lets uh further uh go
into this
So
EN with
GMs
So uh we all know that
MLE
So we obtain theta star as
arg max
of theta
summation over uh all the parameters
log of p theta of
x i
Okay So here we are assuming that the
data
is uh x1 x2 till xn ID from px Okay So
in case of mixture models
the case of uh
mixture models
and uh
and assuming
the densities are Gaussian H
assuming the
densities are
Gaussians So what is the parameter
theta that we shall have Now we shall
have uh alpha j now which is the
probability with which Ill be choosing
assuming that there are m gaussians
What is the probability of choosing the
J Gaussian
and muj
now which is uh the mean of the
jaussian
and then zigma j which is the covariance
matrix I have j running from 1 to m Now
then because of which my
log likelihood which I equals 1 to N this is
over the data
log of P theta of
X I is equal to
summation I equals
1 to N
log of
J equ equals
1 to M
alpha J P theta J
of
X I
okay so this is
so normally what you used to do in ML
estimate is uh we used to directly take
this and uh go ahead
differentiate with respect to the parame
ter and equate it to zero and obtain the
equations But now this is log of uh
sums So we cannot go ahead with that
procedure as we have looked into know
these are
log of sums
Okay So
now you can all do it So lets go into
the em algorithm before going there a
couple of uh
pre things So
for any given
X I
okay so we can know that
K K equals 1 to M you have M mixtures
alpha
K
XI from the parameter
muk Okay
and sigma k and then uh it is clear that
uh
youre choosing z equals to k youre
choosing k gaussian
the probability
alpha k
and then once you sum over
k equals 1 to m alpha k it has to be 1
Okay Now this is the constraint
and then
once you have chosen
a specific Gaussian
XL
given
you have chosen
the k Gaussian component Now it will be
a normal density
which is parameterized by K and sigma K
This needs to be clear
Okay
So now
recall recall
from
the EM algorithm Recall
if theta of
Q is expectation
over this Q
log of
P theta of
X comma Z
divide by
Q of Z Okay So now now when do we get
the optimal value here So the
we obtain the optimal value
when
Q of Z is P theta of
Z given
X
Okay when you put this that is when you
get the optimal value So now lets its
easy for us to calculate Now P
theta of
you choose from the k component given
your input as
x i Now we can easily compute it using
the base rule P of
X I comma
Z equals K
divided by P of
X I
Now this is equal to
P of
Z equals K
P of X I given
Z equals K
divided by
we have already comp obtained this
component J equals 1 to M the mixing
coefficient alpha J
normal
X I parameter is by muj
and sigma j
This we can again
for k
this is normal
x i parameterized by mu k
sigma k
divided by
summation
j equals
1 to m
alpha A n of
x i muj
sigma j Okay
So now uh it is easy to
see that now if I summit over j is sorry
if I summit over
k equals 1 to m this
component Okay So summit over k okay
summit over k equ equals 1 to m that this
specific component it will be one okay
so this is pretty much evident so lets
call this term as
k
okay
so
this is the probability that
we are uh given the
data point x i Now what is the
probability that it is coming from the
ka uh
gaussian
Okay So
lets proceed
now Now this is the this is the optimal
value Now we just need to pitch it in
here Pitch this value in here obtain
this expectation
and then do the maximization step
Thats the overall uh thing Okay just
write it down for the sake of
completeness

 The EM algorithm
for
T equals
1 to convergence
Q
T plus 1 of Z
 equals
P theta T
of Z
given
X
Okay So now then uh
once you have this you compute
f theta of
q
t plus 1 Now what is this This is
expectation with respect to this
t plus 1
of z
log of p theta of
x i comma
z
divid by q
 plus 1 of z See uh now please remember
that Im considering only one data
point Now if you put all of them
together youll have a summation outside
I running from i equals 1 to n that will be
there Okay So this is your uh E step
and then the M step is
theta t plus 1
equals to
arg max of theta
f theta of q t plus 1 You just repeat
this You
compute this
obtain this you get theta t plus 1 Use
that theta t plus 1 here
get theta t plus 2 obtain this Compute
this Now you go on now re uh iterating
over this these steps Okay Till
convergence Now the idea of convergence
uh uh see when you see that uh there is
no more uh updation Now that means that
from the previous step and the current
step is the difference between all the
parameters is within some bound that is
when uh we prefer to stop There are
multiple ways Now you you can even
compute the
the loss that was in the previous step
and the current uh step and see whether
it is in the bound or youll just stop
after some 100 iteration or some 200
iterations up to you These are all
different ways in which the stopping
criteria can be looked at Okay So now
coming to the
the E step now I have computed this just
now
Now pitch it in Okay Now for the ease
of notation Im just uh removing this
t You obtain the parameters then plug
it in and go on now doing the the same
thing Okay
So you just uh reiterate the whole
process for some amount of time or
whatever whatever feels the convergence
for you Okay So I just want to
reiterate the same thing
Okay So now I have obtained
the values here Now Ill put them here
into this step and then obtain
f theta and then what Ill do Ill take
the derivative with respect to the
parameters
equal to zero and obtain the values

Ill get the new parameters and then go
back and rewrite
okay fine
now the
the east step
Im doing the E step now What is E
step
As I said Im Im not using that T
Q
expectation of
Q of Z
log of
P theta of
V comma Z
Okay divided by
Q of Z Okay you have chosen
a Z you have fixed it So then uh this
will be
expectation
q of z
log of p theta of
v comma z minus
log of
q of z
This will be
expectation of q of z log of p theta of
oh sorry okay so small notational
mistake
now this is not v okay I want it to be x
i
okay x i
i i value
Okay
So now
now when do I get the optimal value
When I
replace this
with P of Z given X I log of P theta of
X I
comma Z
Okay So now
this I can
easily obtain
This is summation over J equ equals 1 to M
This is probability that
zed takes the value j for even x i
Then
log of p theta of x i comma
z equals to j
Okay
So now now
this I can uh
rewrite it as
summation J is equal to 1 to M just the
standard algebra
P of
J is Z is from the J component
uh
so log of P theta theta of
x i
given
z equals j
plus
log of
p of
z equals j Okay
Now this I can uh substitute I know
this value I know this I know this I
can easily substitute all of them
So j equals
1 to m
log of
x i parameterized by
muj J
sigma J
plus
log of
okay
so now here uh this is your expectation
yeah there is one more summation outside
but now this has to be optimized under a
constraint okay this is a constraint
optimization
now this
Optimize this
with respect to
constraint
such that
now you
therefore the final
uh
expectation will be Ill just call it as
L just sum
dont confuse it with respect to loss
Okay Now summation over
I equals
1 to N
Okay And then
J equals 1 to M
So the same whole value just take it
I J
log
X I parameterized by muj
sigma j
plus
j equ equals
n
i A
J
plus the constraint
So this will be our legion
Z J equals 1 to M
J minus one
Okay
So now this will be my
uh optimization uh equation So what I
should do now from here it is
straightforward Once you have this this
is straightforward Now the remaining
things is just algebra Okay Now this
has the parameters muj sigma j alpha j
equ you take each of them and equate it
to zero and obtain the optimal values
Okay First what Ill do Ill take
with respect to Ill take the partial
derivative of this with respect to alpha
j and equated to zero Okay Uh because
of which what will happen
A summation i is equal to 1 to n
alpha j
n of x i parameters by muj
sigma j
divided Okay
Okay
Exciting
Okay
plus
equal to z
Now this will
give me
summation i equals 1 to n
mixing coefficients plus
go to zero Therefore my
fj will be summation i equals 1 to n
this will be my value
now what is this now I still I dont
know what is this leg multiplier now how
do you obtain this now you know this
value and you know the constraint
that is there by using the constraint
you can easily get that we have done
this already So in the sense not this
specific problem similar cases we have
done it earlier
Now
using the constraint
using the constraint now what is the
constraint now if I take sum over
all the alpha J is it will be one put
that constraint
Now this will be
J equals 1 to M just have minus 1
this is I equals 1 to N
Now I can uh interchange the order that
is there
So we already know that this is one
Thats what uh we did it earlier right
this you sum it over
so this is k equals 1 to m now this you will
get it as one right now I just want to
use that specific thing here now this
will immediately give us
so just make a note of it we know that
if we sum over
j equals 1 to m
we get 1 therefore So I get lambda equals to
minus n Now which directly imply that
alpha j is 1 by n
summation i equals 1 to n this
responsibilities
Okay
This is how I obtain it for
alpha j Okay Now similarly I have to
do it for muj and sigma j as well So
lets do that Now this is one parameter
is done
Now for
muj Now what do you do it
now You take l take the partial
derivative with respect to muj and
equate it to zero
Okay So a very straightforward
simple calculations we have uh already
done this but it involves bit more uh
algebra in this case So now this will
be minus summation i equals 1 to n
alpha j
to n
Yeah So and then
this
is a coariance
So
this we have done this kind of uh
differentiation in detail in our earlier
tutorials whenever we are going ahead
and obtaining the MLE Okay exactly do
the same thing Okay now you multiply
it by the inverse of your coarience
matrix and then what do you get finally
So now you get this we know
this will be
 equals 1 to n
x
1 to n
 equals 0
Now
this will be
J equals
 equals 1 to N
Okay
So now
this
we can say it has some kind of a
constant that is there Now because of
which I can say that my muj is
1
n k
or in this case better to say it as nj
okay
into summation
is equal to into n
x
This will be for mu and uh
similarly Ill leave it as a simple
exercise to obtain it for the coariance
So
I just write the result Similarly
differentiate
uh take the partial derivative with
respect to
and
equate to
zero
Now we
will be able to get it
equals 1
nj
summation
i equals 1 to n
j
x i minus muj
into
x i minus muj
the outer product Okay
Now this is uh
we have seen uh similar kinds of uh
derivations earlier I hope that youll
be able to
take care of this Now this is for one
specific t and then you have obtained
these parameters and then what do you
do Now this is this is the m stuff I
should have mentioned it Okay this is
the
M step Okay
now with these uh updated parameters
you go back and obtain these values
after use those value
get this
equate each of them to zero and then
obtain new set of parameters and go on
repeating this Now this is your
uh em algorithm Okay Expectation
maximization um algorithm Okay So I I
have omitted the t because of uh too
much of cluttering of uh notations but I
assume that now this is uh pretty much
comfortable and clear Okay So now just
as a side uh thing now I just want to do
a very small and an intuitive proof of
showing that all of us knows uh the K
means algorithm Okay Now
K means uh uh in the sense it is used
for clustering Now what you shall do is
given a data point well see that what
are the uh distances that is there uh
with respect to all the centroids that
is the mean of a group of data and then
youll assign the data to the nearest uh
centroid of it and then you recomp
compute the mean again now youll be
repeating this till the convergence okay
this is the idea of the k means uh
clustering algorithm Now it can be
easily shown that now this
uh GMM
so under certain conditions
uh it is same as the K means uh
algorithm Okay See in the Gaussian
mixture models now we see that there is
a soft assignment of data
to the Gaussian mixtures but what
happens in K means is its hard
assignment you say that this particular
data belongs to this particular group
this belong to this particular cluster
okay you actually say that okay that is
what is known as a hard assignment okay
so prove lets see how it nicely uh come
out of this
now small proof that
proof of
K means
the
a special case of
GM
under certain conditions H for
Okay Now assume
that you have m uh gaussians So assume
that the covariance of the k gaussian is
sigma square i Okay Its an identity
when which only the diagonal elements
have the value of sigma square And then
how will you compute this
now value Now this will be alpha k into
x i
mu k
zigma k
divided by
summation
j equals 1 to m
alpha j
n of
x i
Okay
Sigma J So now now it actually happens
that now since
now this is uh
a scalar multiplied by an identity
matrix Okay Now we can easily
obtain this value This is same as
k into
exp of
 minus 1
2 sigma square
norm of x i
with respect to
the k component
divided I
J equ equals 1 to M
alpha J
exp XP of
1 by 2 sigma square X I minus
muj
square
So now now
how it boils down that how will be this
be a direct delta function is what we
should actually look at
Okay So now now it is evident and easy
to see that as uh
as sigma squared tends to zero
what happens now in the
in the summation
what happens is as it tends to zero now
what will be the dominant value of this
summation
Okay So now to understand that lets
take a point
x i and then you have mu1 and mu2 Now
this is the distance lets call it d1
and
this is the distance d2 It is evident
that x1 is near to mu1 Now because of
which now what will happen is
now you will get
in the denominator
minus 1 by some beta value D1 this is the
distance okay plus
XP of
 minus 1 by beta
this D2
okay now as this tends to zero See what
happens is the denominator will be
dominated
by the term which is having the smallest
distance
Okay this is uh now how this is
x goes now we it is
evident that this is sorry its not
touching the okay sorry for bad writing
okay it reduces this is e power minus x
right
okay okay
so now
now because of this
as
ts to zero Hope
this summation
this summation of
denominator
summation of denominator will be
dominated by the term which is very
close
So to except from the mean which is very
close Okay Sumination of denominator
will be
will be dominated
by term
with
smallest
x i minus
muj
whole square
Now this is thats all it will dominated
the numerator and denominator it will
cancel out so it will be one So now now
now
for all
L not equal to J
this
will be zero
For the one with least distance this
will be one This is a direct data
function This is what is known as the
hard assignment
Youre assigning the value to a specific
cluster
Okay Now this shows that under these
conditions that we have just looked
into Okay Now the K means algorithm
will
be
so uh on on these conditions GMM will be
the K means algorithm
Okay
So now this is where we stop this
tutorial Now I hope uh this was
helpful Now the main idea of this
tutorial was to give you an intuitive
feel to obtaining uh the values or the
updated values of the parameters and
work with them So well meet in the
next tutorial Thank you
