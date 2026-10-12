---
id: mEpXOyLwbxA
title: Lec 14 Example of ML Estimate
url: https://www.youtube.com/watch?v=mEpXOyLwbxA
date: '2026-01-28'
duration: 20:23
model: youtube-captions (en-orig)
transcript: true
---

## Transcript

Welcome back Now the next question is
how do we solve this optimization
problem in practice
Okay what do we do about P theta uh and
and so on right So typically what is
done is the following Lets look at
this So how to
solve the ML estimation problem
So typically what happens is the
following So now this boils down to two
questions actually One lets write
that So one question is how to choose P
theta
Second thing is
how to solve the optimization problem
If anybody would have told you that
study three math topics and you can
study any engineering topics and these
three topics are the vector calculus
probability theory and some
optimization
They told you the truth because most of
the engineering applications
are nothing but some applied version of
these three for foundations Thats it
So study these things very very
rigorously You can pick up anything So
thats the idea Can adapt very easily
So two two problems right One how to
choose P theta and how to solve the
optimization problem By the way a bit
of nomin
um
see this thing right
is also called minimizing the negative
log likelihood
is called NLLL negative log likelihood
minimizing the negative log likelihood
Okay And this thing whatever Ive
written within these parenthesis is also
referred to as the loss function
Ill show you that when people talk
about loss function from a completely
deterministic standpoint
How is that exactly equivalent to
minimizing NL that is what Ill show you
in a while And this is called negative
log likelihood And you minimize uh the
negative log likelihood to find the
parameters or you maximize the
likelihood Both of them are the same
 Okay
uh yeah so I talked about loss function
So these two questions right how to
choose P theta and how to solve the
optimization problems are are two
questions So how is it done typically
is that for question a
P theta is chosen
using a canonical function approximator
So what does this mean We first assume
a functional form on P theta
Okay we can assume that P theta is a
gshian distribution The example is
right So let me write it in the next
page
Example
depending upon the problem Okay Assume
P theta
is a Gian distribution So whenever we
say that its a Gian distribution it is
parameterized by something right So
make these parameters
functions of these random variables
You can choose it to be identity
Okay So you designate the parameters to
this canolical function h of X So this
h of x typically is referred to as
the hypothesis function or the model I
mean again these are uh nominator
difference Some people call this
hypothesis some people call h theta as
model or p theta as model but it doesnt
hypothesis function
or model function
Okay Now what happens is estimating uh
p theta
becomes estimating the parameters of
this canonical function that we have
defined So uh just to uh jump ahead and
tell you this h theta can be a neural
network
Assume this h theta to be a neural
network and estimate the parameters of
that neural network So thats a
canonical function that that you are
assuming there Okay
and problem B
So optimization
is mostly numerical
See there are cases uh where
optimization can be solved analytically
So meaning you take the derivative of
that log likelihood function and put it
to zero and parameters will come out
Okay but mostly numerical because this
canonical function that well be
assuming uh is not analytically
differentiable with respect to the
parameters theta For instance neural
network right If you take H theta to
be a composition like neural networks
You cannot differentiate the likelihood
function and put it to zero and get your
theta So youll have to solve it
numerically That is what we are going
to see now as we move on
the underlying random variable
data
 This V is our data No we started with
this data So this can be depending
upon the problem Suppose you are
looking at uh uh estimating the
marginalss then this V will be X
Suppose you are looking at estimating
the conditionals Y given X is what you
are trying to estimate Then this V will
be X
Okay Depending upon what your data is
itll be it will be made the function of
data Ill show you examples in a while
Okay
So let us look at a concrete example for
this
 where oh this I see this is a gian
distribution right so Ive made the mean
to be a canonical function of uh uh some
other function and the coariance Ive
kept it as identity I can make this as
another function and estimate both of
them as well but for simplicity sake you
only assume uh mean to be the canonical
function and keep the other thing
identity
Come again
 Theres no loss of
 there is loss of generality right This
is thats why I said this is an example
of a particular model Ill show you I
mean like there can be multiple ways to
do it Huh I Im just taking an
example So let us look at some one
concrete case right So consider
consider the problem of
of supervised regression
Okay what does that mean Well say
that uh
shall we do it in one dimensions for
ease

Uh okay So I can make my X to be in RD
and uh Y is in R And the data that I
have is as follows
This is what I have You want an example
for this U
lets say that we are measuring u the
height weight and the amount of uh
alcohol that one person consumes and the
amount of food that one eats and so on
I just wanted a continuous variable
Thats why I said amount of alcohol that
one consumes Thats not discrete I
could have said whether or not somebody
will do it Then it would be a discrete
variable I wanted X to be in RD All
dimensions are continuous So you can
make it zero as well Right For me it
is zero for instance
right So five lets say that there are
five measurements that we are doing and
y is the lifespan
You understood what the problem is
right Thats what we are doing So its
a supervised regression problem So
somebody has measured that for 100
people and given how long they have
lived and for a new person we have to
make that measurement and uh estimate
how long they are going to live Okay
Uh so this is our data H now what do we
want to do So we want to uh
what are we interested in by the way So
estimate
what do we want to estimate We want to
estimate the
uh the conditional of y given x here in
this particular problem See now you see
the generalization right It doesnt
have to be pxy py anything ert the the
the technique is applicable to any of
the uh problems that you want to solve
So you estimate px py x Now write down
the likelihood right So lets assume p
theta of y given x Lets assume that
this is a gshian distribution
So note that this is a gshian
distribution in y Why

Got the pun No So because its defined
this density is defined on the random
variable Y but its a function of X
because its a conditional distribution
So what do we do is that we assume that
the mean of this canonically is a
function of X and its variance is
identity So this is our model This is
our assump this is the assumption that
we are making
Okay
Now is it a good assumption
We dont know I mean its its its as
good as our assumption Thats it Its
a model So remember my statement No
all models are wrong The question we
should not be asking whether its a good
assumption or not good model or not
The question that we should be asking is
is this a useful model or not And Ill
tell you the ways to quantify that
later How do you ensure that your model
is useful or not Well look at look
into this this whole idea of
generalization bias variance
decomposition and all that which we will
see later in the course Okay this is a
model py given x is this Okay now what
shall we do We will go through our
recipe and solve the uh
minimal k divergence optimization
problem So we want theta star
and by the way what is h theta of x
here h theta of x
what is this
No no This is a function right This
is a function that takes that is from X
to what space
 RD
 Its in RD No
remember that Yes From X to RD because
uh the mean of this distribution or is
it is it so
 r no Yeah Because its one dimension
because the distribution is over Y
Therefore the mean of that is one
dimension So its a function from X to
R this canonical function And what
function should I use here Thats your
choice In fact we will see 10 ways to
do it You can make it a linear
function You can make it a nonlinear
function or a composite You can make it
a neural network and all that That is
what we we are going to see now But
yeah so it is a canonical function
 Oh its a 1 plus one matrix
So thats the advantage of thinking in
generalized way No you tend you you
start looking at a matrix a scalar as a
one on one by one matrix
 Yeah
 Uh I actually did not get the question
 The
Which one
 Why is there h theta of v here I dont
see what is this one is it this is not
given See this is a semicolon This is
saying this is parameterized by this So
this is a distribution on the random
variable y and it is parameterized by h
theta and i Thats what Im saying
H theta is mu Yes
 Yeah So
 we the question that we are asking is
assuming that my p of y given x is a
normal distribution Tell me what is the
mean of the distribution is thats the
whole question that Im trying to ask
Okay
Okay So lets uh write things down So
we have uh uh we have to find theta star
that would uh
minimize
minimize what uh
1 by n
1 through n
log of
cuz we have n of them So this is uh so
I will uh skip the algebra Okay Ill
just write this as proportional Ill
leave all constants Okay
So
we have uh log of
e power
yi
minus
h theta of x i
squared Correct
See whenever I
run out of space to write in a page Im
reminded of this mathematician by name
FMA
Yeah I dont know if you know the
story There was this mathematician by
name
Okay He wrote books where there were
lots of theorems and there was one
theorem of his which is referred to as
the FMAs last theorem Yeah And thats
a very very simple theorem All it says
is you cannot have three integers
that would satisfy this
for n greater than two Two two is
pythagoran interpolate We cannot find
integers that would satisfy this That
was his theorem Its called Farmers
last theorem and he wrote the theorem
and said that I dont have enough space
in the margin of this book to write the
proof and did not write the proof
People after him including the likes of
Oiler tried to prove and failed and this
was for three centuries and it was in
that a British mathematician solved it
and got Fields model for it and the
proof had math that was developed after
FMAs time
but FMA wrote this theorem and said that
I know the proof but I cant write it
because I dont have space here
So yeah whenever I run out of space I
rem I get reminded of See I just ran
out of space here No So
 yeah Yeah Okay Yeah So this is what
it is And uh Ill skip the algebra
again and this will become
the minimizer
 Uh there there is a minus here No
 Yeah theres a minus here And this
minus and the the outer minus will get
cancelled Uh log and these things will
get cancelled
 Let me complete this Uh this will
become
this expression seem similar
This is the le squares estimate
and we will show in the next class that
you can deterministically write this and
say that this is the loss function
So the
minimum le squared estimate
is an is an ML estimator maximum
likelihood estimator under the
assumption that the underlying
conditional density is gausian with the
mean given canonically with the
hypothesis h theta of x that is the
statement
okay so I told you from this angle from
tomorrow in the next class Ill talk
from the other angle where uh I become
the the internet data scientist and say
that there is x there is y theres a
function theres a loss function You
minimize that and just write this
expression Thats it
You minimize this Right So now
the actual so called mic drop moment is
the following that the MSE or the the
minimum le square estimator is the
estimator is the maximum likelihood
estimator okay of the random variable
with the assumption that the underlying
density is gausian
with the mean equal to the hypothesis
function
Okay well see that connect uh in the
next class properly So this is the end
of this particular class Thanks for
attending In next class what we will
do is so this is one example Okay Now
what Ill show you in the next class is
that this is the so called loss
function If you change it and write it
in the deterministic in the
deterministic way that always has a
surrogate it translates to the
distributional assumption that we make
on the conditional that we are trying to
estimate
For instance if I make the so called
loss function the cross entropy
okay we make an assumption that the
underlying distribution is Bernoli with
the parameter given by H theta of X
Well show that in the next class So
every model that you do that you choose
is the canonical parameter and every
loss function that you choose is the
distributional assumption that you make
on the underlying true density that you
are trying to estimate and all ML is
minimizing the K divergence
Okay this sets the context from now on
its just you know taking one form for H
theta and solving that optimization
problem which is quite boring These
insights are the ones that are actually
useful right at least I think so Of
course human opinions differ in a very
large way So thats it Thanks for uh
attending today and well look at the
next things later
