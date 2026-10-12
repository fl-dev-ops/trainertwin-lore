---
id: o5697P6KZoc
title: Tutorial 7B : MLE for Generalized Discrete Distribution
url: https://www.youtube.com/watch?v=o5697P6KZoc
date: '2026-02-03'
duration: 23:07
model: youtube-captions (en-orig)
transcript: true
---

# Tutorial 7B : MLE for Generalized Discrete Distribution

## Transcript

Hello all, welcome to the next part of
this tutorial.
In the earlier discussion, we looked at
an example of uh obtaining the
analytical solution for one-dimensional
Gaussian and then a multi-dimensional
Gaussian. Okay. Now, similarly, this is
a standard recipe that we have.
[clears throat]
So you can uh take it for uh any
distributional form and then obtain the
results. Okay. Uh so here uh we have
considered uh the continuous
distribution. Now let's take one example
of a generalized discrete uh random
variable that was uh initially started
uh discussed in the class. So and the
final answer we know we still need to
just uh look at the overall process once
and then try to understand it is exactly
similar in terms of the recipe on how
did we did the continuous random
variable case. Okay. So let's uh go
ahead with that.
We are taking the
example two.
generalized
discrete
random variable. Okay. Now let's
consider Z
takes value the random variable Z takes
values
A1
till AM.
Okay. And then uh with
probabilities
with probabilities
P1
till PM. Now that is in this particular
distribution Z A1 occurs with the
probability of P1. Similarly so on AM
occurs with the probability of PM. Okay.
So now
now what do we have? Now we have
given
data is
from [snorts]
is in the
data is from okay data is in the
form of
IID
IID realizations ions of
this random variable.
So what is that we have to estimate? So
we need to
estimate
PI.
Okay. Now here see please uh uh see here
I indicates parameter. PI indicates a
parameter. So it's not any density or uh
thing. Okay. Now in this what what I
mean by that it's not px given y
whatever those things that we are
referring it is just a simple uh mass.
Okay. So yeah.
So
now and then not only that the
parameters should satisfy you cannot
have any random parameters. Okay. Any
random values the
the parameters
should
satisfy conditions like now pi should be
greater than or equal to zero for all
cases
then i= 1 to m if you take them
that will be one.
Okay, that also needs to be taken into
consideration. Okay,
so now
what do we do? We transform this into
one hot representation. Now why do we
need to transform this? All those things
has been discussed. Now we look at this
transform as a function of random
variable. Okay.
So now
for our estimation of parameters
estimation
we
represent the
discrete random variable Z
by an
MD dimensional
vector random variable.
Okay, we represent it as an M
dimensional vector random variable. Now
let's call this new random variable as
V.
Okay,
now this V
takes
impossible values.
Okay.
Impossible values.
Now what are those values? No. 1 0
and then
0 1
and so on until
it takes m values
and there is a very interesting
condition in this case. Okay.
Now where which let's say that v
is some value let's say v_sub_1
till
v m
any
vi that I consider is
either zero or 1 and then
if you sum over i = 1 to m v v I this is
one and this kind of representation
is what is known as a
one hot
representation.
Okay, [clears throat]
this is a one hot representation.
So now how does uh the
[snorts] mass function
for
PV
is nothing but P1
V_sub_1
into
P2
V_sub_2
into
there is a comma here into
P M
VM.
See now
you need to understand that one of these
vi will be one.
Okay. Now others will be zero.
Okay. anything raised to the power of
zero is one.
So we will get whichever is uh actually
one. Let's say that pi vi is one. Now
then the whole thing will be boiling
down to pi. Now this you can write it as
a product of I = 1 to M P I
VI.
Okay. Now here this P I is representing
the mass of the uh thing and then this
VI which element is one is what it is
representing. Okay. So I assume that the
notations are comfortable.
Okay. So now
now what we have now given
iid data.
Okay. Now we have d
which is v_ub_1
v_ub_2
so until v n see against our standard at
least against my standard notation I'm
representing these uh instances with
capital now because I'm representing the
values of inside each of these vector
with small so I don't want to confuse
that so I'm representing each uh
instantiation of this random variable
with capital. Okay. So that's a
notational thing. So any vi
that is there will be a vector of what
form? V I 1
V I 2.
So until
V I
M
transpose
any V I J. Now this is I examples J
component okay is
belongs to zero or one and then you sum
over all J if J is equal to 1 to M v I J
is one see I is for the
example the instantiation and J is for
the component okay I'm maintaining that
notation now because of which my
mass function for a specific
instance vi will be a product J is equal
to 1 to M
PJ
to the^ of V I
J
maybe I need to just
take it one line down.
Okay.
Super script and subscript. Please look
at it. Now, now what is that I have to
do? Now, this is for one point. Now, I
have to consider all the points and then
take the log likelihood. The standard
recipe.
Okay.
Now
considering
all data points
considering all data points and
taking log
likelihood will be the summation i = 1
to n ln of p
vi.
Okay,
this is nothing but summation i = 1 to n
ln of the product of
j = 1 to m
pj
v
i
j.
Okay. So log of uh
products can be we know how to take care
of it. I is equal to 1 to n
j = 1 to m
v i j
log of
pj.
Okay.
Now, now this is the from now, now what
I should do? So, now I should take the
derivative uh partial derivative with
respect to the parameters and then
equate it to zero. So, but there is a
problem. Now, see uh this is an
unconstrained maximization. Now what do
we want is a constraint
maximization and then uh uh now why no
because PJ for which I'm actually the
parameters which I'm interested in now
they cannot take any random values okay
that are there in R okay okay it it it
has to satisfy some condition right so
now let's make note of this
the
the above formulation that we have
the above formulation is an
unconstrained
is an unconstrained
maximization.
Correct? It's an unconstrained
maximization. We need to perform ML
estimation for the parameters for which
there are certain constraints. Correct?
So now
we need to
we need to perform
MLE
of the parameters.
MLE of the parameters
over some constraints over the
constraints.
You know what are those constraints? Now
p I should be greater than or equal to
zero and
j = 1 to m
pj equal to 1.
Okay. Now because of which now how will
my constraint optimization look like?
Okay.
Therefore,
the constraint
the constrainted
optimization.
The constrained
optimization problem
is
max of PJ
summation I = 1 to N summation J = 1 to
M
V I J
log of PJ
such that
the summation over this
equal to one
okay now but we have two constraint
right each of them has to be greater
than each PJ has to be greater than zero
right
I'm leaving it as you as a small
exercise now just optimize I'll optimize
only with this you add the second
constraint and also optimize Now then
what will happen? Have a look at it.
Okay. So this is a constraint
optimization problem. Now you can have
one constraint two constraint. So now
what do you do? You get a lrangen of
this optimization and then you take the
derivative of the lean engine and then
equate it to zero. That's this procedure
now.
Okay. So now the lrangian
the lrangian
for
this problem
is
is given by
summation
i = 1 to n summation
s = 1 to
just to indicate that these are dummy
variables. So, v i s
ln of p s plus
lrange multiplier lambda
1us the constraint that we have x = 1 to
m p s.
Okay. So now now what is that we have to
do? Now we have to calculate the partial
derivative of the lrangian with respect
to the parameters and then equate it to
zero.
Okay. So now
now now
calculate the
partial derivative
calculate the partial derivative
of the
of the legangian
and
equate
equate it to
zero.
Okay,
that's what we are supposed to do.
uh
then
what will happen you take the okay let's
take it with respect to PJ so now now
take it with respect to some PJ
or PS in this case
now for for whatever
PJ that you are considering for that it
will be V I S divided by PS it will
become minus lambda is zero and then
there will be a summation with respect
to equal 1 to n correct
so now this will be
summation over all the examples I equ= 1
to n
v i j
divide divided by pj
minus lambda equal to0 for all j equals
1 to m. So
it's for all j it's finally it will be a
parameter vector. Now if you get this
now PJ
equals 1 / lambda
summation i is equal to 1 to n v i j
correct so what is the value of lambda
okay now we have to use the constraint
and then look at it
Now,
now we
use the constraint.
What is the constraint? If you take over
J = 1 to M PJ, it has to be 1. Correct?
Therefore
J
is
summation J = 12 M 1 /
lambda
and I = 1 to n vig j equal to 1. Now
this I can rewrite it as lambda equals
summation
j = 1 to m. See lambda is independent of
i and j. So I can take it out. Okay. I =
1 to n v i j
always we can interchange the
summations. Right? Now let us
interchange this.
No.
Okay.
Now this is
summation i = 1 to n
summation j = 1 to n v i j. Now that
means for a given vector i, you sum over
all their independ individual
components. That's what you're doing in
this. For a given vector I you're
summing over all its components. See if
you sum over for a given vector uh uh m
dimensional vector one of them will be
one. So this has to be one. Now
therefore
this will turn out to be n right now.
This is one. Now you add one n times. So
this will be n. Now therefore
the value now putting all of this
together PJ star
will be 1 / n summation i is equal to 1
to n v i j
this is what and okay j is from 1 to n
j is
1 to n
this is the the parameter vector that we
will be getting okay is one value so
similarly you'll get it as a vector now
now this is crystal clear right the
final ML estimate for a given PJ is
fraction of times the J value actually
occurs
okay which makes total sense with our
intuition okay
so now this is how we solve it for a
simple generalized discrete case okay So
with this we conclude uh obtaining of uh
analytical solutions for Emily estimate.
Now we will proceed with some other
interesting some of other interesting
ideas in coming tutorials. With this we
conclude this tutorials. I hope it was
uh informative. Thank you.
