---
id: _QrezNPmxDk
title: Lec 09 Density Function
url: https://www.youtube.com/watch?v=_QrezNPmxDk
date: '2026-01-16'
duration: 08:05
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

speaker_1: Welcome back So given
uh a continuous random variable with
a distribution function
px
density function is a function
density function I will denote it with
small p and an x to denote that x is the
underlying random variable Okay this
is my notation PX its a function from
the range of the random variable range
space of the random variable to R plus
its a non negative function Remember
that density functions are simply non
negative functions They are not bounded
between 0 and 1 Ill tell you Ill talk
about the properties of this a function
which is from X to R such that
if you evaluate this function at some
point X
this will give you the
Ill write it the other way out So if
you take the distribution function and
evaluate it at x this is equal to the
running integral of this
this particular function

This is the definition of a density
function
Okay Now by definition please note
that suppose you evaluate the density
function at a particular point
What does that give you Itll give you
a positive number right Itll give you
a positive non negative integer but
that does not correspond to probability
Please remember this Its a trivial
mistake that lot of people do
Evaluating density function at a point
is not a valid probability measure
 Come again
 No you can evaluate it at a point See
 no it will not be zero Itll itll
evaluate to a particular value right
You take the gian density function plug
in a value to x you will get some
value
 huh Yeah probability is zero Thats
what Im trying to say See you can
evaluate see two different things
Density function is a function You can
evaluate the density function at a
point but that does not give you a
probability Thats all Im trying to
say If you integrate the density
function over a range by definition it
it is a valid probability measure
because integrating a density function
over a small range corresponds to a
distribution function and distribution
function is a valid probability measure
because its a push forward measure but
evaluating the density function at a
particular point
is not a probability measure I mean one
trivial example that that I always give
people see when I talk to people and
conduct interviews etc Um this is one
trap that I throw towards people
Theyll say this thing goshian density
its pretty easy right I mean you can
actually its bounded bounded and
therefore value can be interpreted
people interpret this as probability
So then Ill ask them to write down the
density function for a uniform random
variable that is uniform between 0 and
half
What is the density function for a
uniform random variable thats uniform
between 0 and half It is two
So now its always more than one right
So how can you interpret that as
probability If you evaluate the uniform
density of uniform random variable
between 0 and half itll evaluate to
two at all points But probability
measure if you remember is a function
that is bounded between 0 and one And
this is one
you know example where you can clearly
show that the density evaluating density
function at a point does not give you
valid probability measure but
integrating it would Okay However
the value or the eval eval evaluation of
the density function at a particular
point is called a likelihood This is
the nomin that people use Okay Anyway
I Ill use that nomin later The reason
I define density function is most
algorithms okay operate on density
functions not on distribution functions
just for mathematical ease Theres no
other reason And all of you already
know that not all random variables can
have density functions So there can
exist random variable where the density
functions are not even defined See this
is for the case of a continuous random
variable For the case of a discrete
random variable evaluating density
function is a valid probability measure
Okay You actually for a discrete random
variable you can interpret the you know
the the density function Its its not
called the density function Its called
the probability mass function
Evaluating the probability mass function
at a particular point is a valid
probability measure by definition Not
for the continuous thats why I defined
it for the continuous random variable
In general we will I mean all most of
our data can be interpreted as
continuous random variables Thats why
well be working with density function
So we have to change our problem I said
given d estimate the distribution
function Right Now Ill say given D
estimate the density function Im
assuming that all the data that we will
be having can be modeled using those
random variables for which the density
functions are well defined Thats a
fair assumption to make because most
well behaved random variables will have
density functions defined
Okay So we will work with density
functions uh from from now on we will
work with density functions Okay So
all these problems right now well be
instead of estimating uh the conditional
distribution well be estimating the
conditional densities P of Y given X and
P of X and so on Right So please note
the change in notation If I write P
with you know two lines its a
distribution function If I write it
with one line its the density function
And throughout the course rest of the
course from now on Ill be working with
density functions not with distribution
functions
Its not in the real world
 there can be sort of

distributions which cant be described
in mathematical function
 No thats not what Im asking Thats
not what Im saying Thats a question
that well be seeing later Um see all
Im saying is in real world all data
that we have can be assumed to have
valid density functions Thats it
Valid density functions What Im
talking about is there are random
variables for which the density
functions cannot be defined So Im
saying Im we are assuming that all the
data that we have that we get in
practice can be defined uh or rather
will have or can be defined using random
variables can be represented using
random variables for which the density
functions are well defined thats all
Okay So if if you people do not know
what density functions are please read
up uh but yeah this is what it is Its
another function that is defined from uh
the range space of uh the the random
variable x to r plus theyre non
negative functions The range of uh the
range space of the density function is
always positive real numbers And the
definition of it is that its a function
which would evaluate distribution
function at a point If you consider it
running integral between minus infinity
to x and this integral by the way is not
a single integral Right If its a
dimensional uh random variable that we
are talking about then then its a
integral over rd usual integrals Okay
Okay Right So I think we have now laid
the uh foundation that that we that we
needed for defining uh the machine
learning problems As I said its mostly
density estimation problems conditional
marginalss and joint densities and so on
given samples permits So how do we do
that Think about it Its a non trivial
problem to solve
because okay let me write it down the
challenges with ML
 Well see you in the next lecture
