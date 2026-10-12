---
id: s_DfCCobgnA
title: Lec 28 Ordinary Least Squares (OLS)
url: https://www.youtube.com/watch?v=s_DfCCobgnA
date: '2026-02-18'
duration: 24:47
model: youtube-captions (en-orig)
transcript: true
---

# Lec 28 Ordinary Least Squares (OLS)

## Transcript

Welcome everyone.
In today's lecture,
we are going to switch to the empirical
risk minimization framework.
And I begin the lecture by showing you
that uh everything that we do with
empirical risk minimization is
equivalent to distribution estimation
that we have already seen. But it is
approaching the same problem in a
different way.
Typically what happens in communities
that some of the uh popularly used
models such as uh linear models and
neural networks and so on they are
approached from the empirical risk
minimization angle right so that's why
what we will do is I'll first establish
the equivalence between the empirical
risk minimization approach and the
probabistic uh distribution estimation
approach that we are looking at and then
we will look at a few examples example
models
in within the framework of empirical
risk minimization and see how to train
them or rather how to uh come up with
those kinds of models from an erm
standpoint. So that is the subject of a
few uh coming lectures. Now first we
will look at uh
equivalence between erm and probabistic
approach
erm and distribution estimation.
See often this uh equivalence is missed
in the community because most uh when if
people stick to erm they'll stick to erm
throughout and if stick if people stick
to probabistic approach they stick to
probabistic approach throughout right so
that connection is something that is
that I found uh very valuable personally
because whenever you see erm you know
you know what is happening in the
probabistic world and uh vice versa so
let's look at it already done that but
let's let's do it once again so Now
uh suppose you know we all always start
with uh the data and let's say that we
are looking at uh the supervised
learning framework where we have uh two
random variables x and y
which are sampled iid from an unknown
joint distribution pxy and we saw
that given this we estimate several
distributions right several density
functions and uh uh we know how to
estimate them in different ways now
right the the ML way the map way and the
the nonparametric way and so on right
now in the okay so let's write that in
the the probabilistic approach
the central problem the main problem
is to
estimate
distributions or density functions
from D.
Now these distributions can be the
marginal or they can be joint or they
can be conditional and so on right
depending upon what problem you are
trying to solve you estimate the
underlying distribution given D that is
what we have seen so far and that's the
probabistic approach now in the
empirical risk minimization or risk
minimization approach in the risk
minimization approach
The
main or central problem
is to
estimate a function.
Estimate a function h. And this function
is typically from the random variables
that we have X from X to Y right from D.
Okay.
Now how do we do this? How do we in the
previous case in the probability uh in
the distribution estimation approach?
How do we estimate
these distributions? We estimate these
distributions via minimizing the kale
divergence between the model
distribution and the true distribution
and we use data to do it. So that's how
we do it. And in the erm or the risk
minimization approach, how do we
estimate that function? So okay, let us
write that distributions from D via
divergence minimization approach. Right?
This is what we do in risk minimization.
The central problem is to estimate that
function okay from D via
empirical risk minimization.
So mathematically speaking right in uh
the probabilistic approach.
Now given d
what we do is estimate this theta
by
solving the following optimization
problem.
some divergence metric between px which
is the true density function and p theta
which is our model density and this
optimization is over theta this is what
we have seen so far right this is the
robistic approach and in the erm
so we are given cmd what we find out is
we find an h star let's call this theta
star we find an har as
the minimizer of
the empirical risk which is
the expected
or the sample estimate of uh the
expectation of what is called as the
loss function right that's what we saw
now I told you that these two are
equivalent in the sense that these two
optimization problems this optimization
is over h right all possible hypo I mean
this h is called the hyp hypothesis
function and this is O and I told you
that these two function these two
optimization problems are exactly
equivalent under certain assumptions
okay that's what I told you so one uh
equivalence is the following right the
claim is that they are equivalent
the divergence minimization
and erm are equivalent
So
a generalized equivalence cannot be
established. You know it depends on case
by case. You take the claim is that
every divergence minimization problem
can be seen as an erm with a certain
loss function and every erm with a
certain loss function can be seen as
divergence minimization and with an
assumption with a certain assumption on
the distribution that is being estimated
is the climb. So this has to be
established case by case basis. Okay. So
let me show you uh a couple of examples.
I think I've already showed you one,
right? So an example can be suppose
um
want to estimate
P of Y given X okay from data and uh
make an assumption that this is
gshian okay uh this is this is on
defined depend on random variable y and
let's say that uh the mean of this is
some function h of x and we have the
variance to be identity. So this is our
model.
Okay. So this h is now a function of
theta
and this is our p theta. Okay. estimate
uh okay pxy actually it's better that I
write
p of y given x and we assume that our p
theta of y
is given by that actually p theta of y
given x so it's a function of x right so
what we are estimating is the
conditional of y given x and this is a
function of x and I've told you that the
conditional distributions are always the
functions of the conditioned random
variable and where is the function of x
coming here it's coming in as the mean
right of this distribution that we are
estimating. Now if we do this then the
uh the maximum likelihood objective
will be as follows. This is theta star
is argument.
So I think I've already showed you uh
the algebra right this will be
yi min - h theta of x i square
right you can please solve this so you
understand what I'm saying right this
you just write down the likelihood
function log likelihood it it it can be
seen here right there e power this
particular term that we have and uh the
log the log that comes up in minimizing
the k divergence so the log in the
exponentiation will get cancelceled
away. Okay. And there is a uh max there.
There's a minus that will become the
minimization problem. And this is the
equivalent. So here is the equivalence
where
so this now
is equivalent to erm right. So this is
this is erm
with
squared error loss.
Right? So this is the equivalence. So
now if I let's say that I start with a
particular loss function and uh cast the
problem as that of estimating h directly
which is the hypothesis function. You
should always realize that there is an
underlying distribution function that we
are trying to estimate and uh depending
upon what choice of loss function we
make we estimate that underlying
distribution function. Right? it I mean
the underlying distribution function
takes takes a particular functional form
though that's the it's always the case
okay yeah question
>> huh this yeah so this h theta
in the erm case is the function so now
you suppose
you have d okay you assume your loss
function to be the squared error loss
Okay. And you solve for some function h
theta of x let's say. Okay. What you are
actually doing is that you are assuming
that your underlying distribution for p
of y given x is gausian with the mean h
theta. That's the equivalence. You are
making that assumption implicitly. If
you solve an erm with squared error loss
always the case
whenever you are using the squared error
loss and solving erm. Okay. You're
always assuming that the underlying
distribution uh under which you are
solving the maximum likelihood estimate
is a gausian with the mean being equal
to this h theta always.
Okay. And this can be said for every
loss function that you choose. So you
choose a loss function then there exists
an underlying distribution function for
which you know with which you are
solving the maximum likelihood estimate.
They are exactly equivalent.
Okay. So you might have seen this right?
I know some people yeah so in uh in the
uh in the deterministic approach what
people say is that suppose you have your
data this way h theta of x plus epsilon
where epsilon is normal 01
right so what happens is you have uh y
equal to some h of x some function of x
plus some epsilon and this epsilon is
normal 01
then if you solve I mean what they say
is that Okay, one way to
fit this model or find this model is to
minimize the noise.
This is one way people cast the story,
right? So what actually happening here
is that if you write your generative or
rather function this way, then you are
saying that the conditional distribution
py given x is gian with mean h theta of
x.
Isn't it?
So that's why some people start you know
teaching ML this way I rather
introducing ML this way that oh you have
a dependent variable you have an
independent variable there is noise
perturbation that's happening and all
that I don't like the word noise at all
I mean the word noise is noisy
right so this is simply you're saying
that the underlying distribution is gian
with mean see what are we actually doing
we know that if you take an isometric
gausian which is zero mean and unit
variant shift it with a certain
deterministic value then the mean get
shifted the distribution still continue
to be gausian by doing all this all I'm
saying is that my p of y given x is
gausian right with mean h theta of x and
variance identity that's it
right in fact even more so now what is
said is okay suppose you make your h
theta of x to be let's say some theta
transpose * x which is linear function
of x they say that okay there is a line
here right and uh let's say that this is
your x and this is your y there is a
line that is given by theta transpose x
or theta * x and then every point you
disturb it with some noise
and that is your data
what's actually happening is that you're
assuming that the underlying
distribution conditional distribution is
simply gausian with the mean given by
this h theta of x which is a linear
function of data that's
Okay. So this is a side note. I will
just erase this. Okay.
Anyway, so what I wanted to know what
what I wanted you people to know is that
whenever we write an erm with a certain
loss function, we're always making an
assumption that there exists an
underlying distribution function with a
certain distributional assumption whose
maximum likelihood estimate boils down
to solving this error.
Okay,
you had a question. assume the
>> in this particular case. Yeah, you can
you can if you make it if you make if
you uh assume it to be something else
then your loss function gets scaled.
That's it.
See what I'm saying is you can given a
problem you can either approach it from
the probabistic standpoint where you say
that I have I assume that the underlying
distribution is this and then solve then
get the parameters via maximum
likelihood estimate or you can say that
oh I define a loss function and I solve
erm they are both exactly equivalent is
all I'm trying to say in literature
people either talk from this angle you
know where they say that oh there is a
loss function and we are optimizing the
loss function or they'll say that oh
I'll assume a distributional form and
I'm doing maximum likelihood estimate
not every uh approach you know not every
algorithm in ML will establish the
equalence between these two however you
should know that there exists an
equalence for each every single point of
it right every single problem that's it
yeah okay
any other question okay so let us now uh
look at a few examples of erm with
certain models so let us look at The uh
first class of models that are called
linear models
linear family of models. Now uh see
models
which has
this sort of
form they're called linear family of
models. So we are assuming that my x is
in RD.
Okay. In which case theta also is in RD
and theta KN is also in RD right
it's R
I mean this if we assume our Y is in R
let's write them down so suppose Y is in
R uh suppose it's in R K if your Y is in
RK theta has to be a matrix
right? Whatever uh dimensions you have
to ensure that the dimensions are taken
care of. So these families of models are
called linear models. Okay?
Now um
so one elegant way of doing is this you
subsume this theta kn into your x
meaning suppose you have x in RD you
just make x uh have one more additional
dimension which is a fixed value I mean
which always have the fixed value of one
in that case your data now becomes a a d
+1 dimensional data and you can subsume
this theta not into it and write the
model as theta transpose X where the
last dimension is always that it is also
called the the so-called bias term okay
so that can be done uh yeah so
okay with
with X being uh X augmented with one
transpose I can write this model as
simply theta transpose X
right where X is now in RD + 1 all of
you get this right I just just for
algebraic convenience I just uh wrote
that as theta transpose x see one uh
intuitive way of looking at linear
models is that
so suppose your data is dimension let's
say let's let's say let's take for
example that you are making d
measurements okay each of each
measurement is in one dimension of the
input random variable then these linear
models are simply looking at weighted
combination linear combination of all
the measurements and the decision is
being taken depend based on the
linear combination the weighted
combination of all the measurements that
we have made. That's why it's it's the
most primitive way of looking at it,
right? Take the first dimension, scale
it with some value, take the second
dimension, scale it with some other
value and so on. So what do we learn or
rather what do we actually uh model when
we are modeling when we are building the
model is we are learning to
we are learning how much each of the
dimensions each of the measurements have
to be scaled to take the decision. So
let's say that you're looking at height
and weight to make a decision. The
question that we are asking is how much
does the height dimension contribute to
the final decision and how much the
weight dimension contribute to final
decision. So that's what we are trying
to do in a linear model. Make sense?
Okay.
Uh right. So now let's formulate erm.
So, erm
with
linear models
and squared error loss.
See whenever you are solving erm you
have to make two choices. The first
choice is the hypo the class of
hypothesis function that you are looking
at. The second choice is the loss
function. Right? So, let us do this erm
with squared error loss. So you already
know this. So uh theta star is the
minimizer of
h theta of x i minus
yi
square of this. This is equal to
what is this? This is uh theta transpose
x i - yi
the whole squ.
What's the solution for this
optimization problem? You all know this,
right?
is equal to that particular this uh
it's called the
sudo inverse right yeah so it's
ordinarily square x transpose x
inverse
xrpose
y
where
x is a matrix
that has
uh
x1 x2 all of them are stacked as rows x
and here
see all our vectors are column vectors
right so that's why you have to take
them take a transpose and uh do it and y
is y1 y2 I'm assuming that y is in r
right so that's why all of these are
scalers you have n of them.
So you know this right? This is the the
ordinary squares. I mean I'm assuming
that all of you know this. Uh if you do
not then I think uh it will be done in
tutorials right where you have to solve
this optimization problem. Okay. Uh
yeah if you take this norm
write it express this as matrices and
take the derivative with respect to
theta and put it to zero you'll get your
theta star to be this.
Okay so this this entire matrix right
xrpose x inverse * xrpose is called the
pseudo inverse the more pseudo inverse
of this matrix x and so on. Okay,
all of you have done a course on matrix
theory and linear algebra, right? And it
was a part of this. Okay,
so this is uh the orderly squares or
linear models. This is how you solve the
linear models. Linear it's also called
the linear regression because you're
solving the regression problem. Why?
Because the other random variable the
label random variable Y is continuous R.
It's not classification that we are
solving here.
Okay. Uh and uh it's linear because the
model that we are looking at is linear
here. Okay.
>> No, we have already subsumed this right
here. X now simply has when we write the
data, we have just written that one with
the data. So that's now my data is in R
D + 1 dimensions. It's already there.
>> Where?
>> Yeah. In this case, in the augmented
case,
theta is in R D + 1, of course,
because if augmenting so that the D plus
first dimension is your constant that
that bias term. Okay, this is about
linear models. See, you can generalize
this idea. uh you don't have to stick to
a linear combination of features. Uh we
can we'll look at what is called as the
general generalized
linear models.
Uh we will stop here and continue in the
next lecture.
