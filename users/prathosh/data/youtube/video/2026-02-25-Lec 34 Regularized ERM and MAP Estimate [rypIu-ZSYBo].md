---
id: rypIu-ZSYBo
title: Lec 34 Regularized ERM and MAP Estimate
url: https://www.youtube.com/watch?v=rypIu-ZSYBo
date: '2026-02-25'
duration: 26:57
model: youtube-captions (en-orig)
transcript: true
---

# Lec 34 Regularized ERM and MAP Estimate

## Transcript

So the next question is right why should
this increase bias. Now we said that oh
this kind of uh regularizer
regularization is a technique that would
increase the bias or know why should
restricting or rather solving a
constraint optimization problem over the
parameter space should increase the bias
is the question. Okay any any thoughts
on that.
Why do you think it should increase the
bias? bias when I when I say bias it's
the
yeah the uh bias variance bias so why
why do you think
okay here is a homework
uh show that
the bias of a regularized
model is always more than that of the
unregularized version
so I'll give you another perspective of
how to do this but yeah you you should
solve it for know from a from an erm
perspective I'll give you uh another
perspective from the probabistic uh
viewpoint okay so basically what you
should do is construct a hypothesis
with some loss function okay uh and
compute the bias construct the same
hypothesis add some regularizer function
on top of it and show that the bias
increases that's what you should show
[snorts] okay so now
equivalence
between
regular DRM
and map estimates.
Okay. So please recall that
in map estimate
so we seek
a distribution P we seek the posterior
of parameters conditioned on data what
was the variable that I was using T or D
or whatever okay I can use let's say
that we have one data point doesn't
matter Uh
so we expressed the uh posterior of
posterior of uh the parameter
conditioned on data in terms of uh the
the prior on the parameters and the
likelihood of the data conditioned on
the parameters. Now remember in the map
estimate it is a basian way of looking
at things. We assume that the parameters
also have
uh distributions of their own and we
encode our bias in the speed theta.
Okay. And what happens uh post the
bijian estimate is that we update our
belief as it is said right? You know you
remember that thing right? You know you
come with a bias look at the universe
change your bias after looking at data.
That's what we do in map estimate. Now
let us work out a case of map estimate
right where as let's take an example
consider an example
where
P of X given theta let's say that it is
we take that to be a gausian
um
with some mean uh mu theta and uh you
assume that we know the
variance.
Now if you have to do the map estimate
okay we have to first write down the
likelihood of this okay what is the
likelihood of this this is
l theta is 1 / n
log of
p of x given theta this is what we do
[snorts]
we know this result right this will be
I'll just write it as equivalent I'll
ignore the constants this will be x i
minus Yes.
Oh,
just realized that I'm doing it for the
uh case where there are no labels. Maybe
I should have done it with the case
where there are labels. Shall we do it
for the case with labels because you
know that's what we have been looking at
for the ERM at least. Right? So in that
case our uh
uh this distribution was the conditional
of
this was the distribution that we are
looking at right the conditional
distribution of y given x and uh
in the
in the case of squared error loss what
Did we assume this to be?
I mean see whatever I did without the
labels also has the exact same uh you
know uh match but since we are looking
at supervised learning we'll do it and
by the way this is an opportunity to
make this statement all the techniques
that we have seen including
regularizations are general enough that
they can be applied to supervised
learning and unsupervised learning as
well. It's only the distribution
changes. I hope that all of you know
that by by now right. So this is a
distribution over y and this we assume
to be h theta right the mean to be h
theta and this is i. Uh in that case uh
this is going to be
y given x and theta and this will be
so yi minus
h theta of x i correct
ignoring all the other constants
right this is our
likelihood function that we would
maximize uh
no there is a minus here right because
yeah so if you minimize that then the
minus will go away the negative because
the you understand what I'm saying
normal distribution will have e power
minus this quadratic term and that minus
will just come come here and we maximize
the likelihood which means that we
minimize the negative of it which will
be equivalent to our erm objectives
right now this is the the likelihood
term what about the prior okay suppose
we assume
we assume the prior on theta
to be another gian distribution.
Okay. Now what is this uh distribution
over the prior? What is the what's the
random variable that we're considering
here? If we are looking at distributions
over prior, what is the random variable?
It is theta. So it's a distribution over
theta. And let's say that we assume the
mean to be zero and variance to be one
or identity. We can do that because it's
a it's the prior that we are choosing.
Okay. If you make this then what happens
to the posterior. So now P of Y given X
and theta. Now you know that is
proportional to
uh P of uh Y.
So this is the other way around.
theta given y and x is proportional to y
given x and theta and we have p theta
and now if we look at the log likelihood
function of uh this particular case okay
let me call that as l r I'll have to
look at the log of this right it will be
proportional to log of this thing now p
of theta given y and x correct
so now this has uh two things. This is
log of uh p of y given x and theta plus
log of p of theta. And we know what this
term is, right? We already know that
this is minus
yi minus h theta of xi.
And what's the second term? Assumed it
to be normal distribution. This will be
minus
theta - 0². Mean is 0. So it will be
theta - 0 square and the denominator is
an identity. Exponentiation and log will
get cancelled with each other
all of you with me right. Okay. What is
this? So what we have want to do is in
in in in map or in probabistic treatment
the objective is to obtain theta star
that would minimize
this log likelihood
sorry maximize the log likelihood.
Okay. Or it is minimize the negative log
likelihood
which is minimize.
Right? Is exactly equal to the empirical
risk minimization with the regularized
cost. Right? with.
Now this implies that
regularized
erm
with
[clears throat]
this as the regularizer
norm two as regularizer
is basian estimate
with a [clears throat]
gausian Empire.
That's it.
>> Come again.
>> Ah, there was a summation here.
Yeah. Here. Here.
Yeah. See the sum is only over uh
terms that has I index right I mean
there's no summation of regularizer so
it's okay I don't have to put a bracket
even if I do it doesn't matter but yeah
okay this is the thing right so
regularized drm with a particular
regularizer is equivalent to the basian
estimate with a particular prior on the
uh the parameters now think about it
what we are actually saying is that
by putting an L2 as a regularizer right
around zero
this is theta and this is P theta I'm
actually saying that
I'm instructing my optimizer or the
regular SDRM
to choose my parameters around zero with
highest probability
you see that's what I'm
So any constraint optimization problem
in the deterministic sense can be seen
as a basian estimate.
All constraint optimization problems
right are basian estimates with some
prior on the
parameters or rather the variable of
optimization. So whatever you take
that's the way. So here if I put if I
put a regularizer which is gausian this
way I'm saying while you choose the
parameters choose it in such a way that
the probability of finding those
parameters around zero is highest.
Okay. Now suppose we change the prior.
Okay.
Suppose we want to change the prior in
such a way that given a particular uh uh
subset on in the support of parameter
space. Okay. the likelihood or the
probability of observing those
parameters have to be higher than that
of gajian. What should I do? Do you see
what I'm saying? The question that I'm
asking is suppose I take a small support
here small subset in the support let's
say from minus.5 to.5 I get some mass
here correct okay suppose I want to
increase that mass meaning I want to say
that choose the parameters in such a way
that the probability of getting those
parameters around zero is higher than
that of a gian a unitary gian what
should I do I'll have to change the
distribution of course to what
distribution a distribution okay whose
mass around the zero given a small
support is higher than that of gausian
what is a distribution that you know of
that sort come again
>> lelassian lelassian is one distribution
that you can choose okay so now suppose
p theta is chosen to be lelassian
with parameter let's say some alpha then
the
the probability of parameters
around mean
will be
higher
than that of
gshian
And this is a homework. Can you guess if
you impose lelassian prior what would be
the regularizer fun regularizer
function?
>> It's L1. Now why it's pretty simple.
Llashian distribution is is from
exponential family. Right? That would
have a a form like this.
That's it. And instead of having a
quadratic term in terms of parameters,
it will have a linear term in terms of
parameters. minus theta mod theta right
yeah it'll have a mod theta because it
is symmetric around zero symmetric
around the mean it will be e power minus
mod theta yeah it will be e minus mod
theta instead of having two norm it'll
have one norm
now you tell me you know the popular in
the popular culture right when people
teach ML they'll say that L1 induces
sparsity in the model
now you know Why?
Because the prior that you are imposing
is such that the odds of finding the
parameters around zero is higher. Now L1
induces sparity is a blanket statement.
It's not correct. I mean L1 induces more
sparity compared to gajian is what you
should say or L2 is what you should say.
L2 also induces sparity in the sense
that it is choosing the parameters to be
around zero with higher probability
compared to that because the the the the
fall here in the gosh see if you if I
write the lelian distribution on the
same plot how would that look like
it would be steeper no something like
this
it will be symmetric
See on a on a very different note
uh
do you know what is perceived as
beautiful uh from uh from the
perspective of human's eyes
symmetry. Yeah. The reason I said is
right. I mean the moment I break the
symmetry when writing a distribution it
it starts looking ugly because that's
that's how you know we have award as
human beings so L1 with llashian prior
right so now you know why it induces
parity there's also a geometric way to
interpret this
any constraint optimization problem the
moment you put a constraint on top of
So if you draw the objective function
and also the constraint function, you
are seeking for only those surfaces
where these two functions intersect.
That's constraint optimization problem.
Right? Now what sort of constraint
geometrically is an L2 constraint?
Huh?
L2.
>> Yeah. L2 is a sphere. If it's in one
dimension, it's a circle. If it's in two
dimension, it's it's a sphere around the
origin. If if you make the uh that k to
be zero,
right? So now what you are actually
doing is you know you might have seen
this figure, right? When people talk of
regularizer, all they do is write this
uh you have some objective function.
I don't know why it should be
how do I write it? It's so difficult to
write. The regularizer is a is a sphere.
It's a circle here.
This is the L2 norm
the regularizer
the objective function it can be yeah
something like this and the contours
right contours of the objective function
this is the loss and this is the penalty
and you are only seeking for those
points where these two intersect
and then what happens for L1
>> huh
there's a there's There's a name for
that geometric shape.
>> It's a rhombus. Yeah.
See, diamond is for kids.
[cough]
[clears throat]
So my son calls it a diamond. No.
Yeah. So now you know one geometric way
to look at it is that if you have an
objective function and a rhombus what
are the points at which they both uh
intersect the chances of those two
figures intersecting is highest along
the coordinate axis
and coordinate axis by constructions are
the are are the points in which one of
the values one of the
values is zero that's why it induces
sparity
I am not a big fan of this way of
looking at things at all. So to me
simply a laplashian distribution that
has its mass concentrated around zero
and that's why you are pushing it.
That's it. See now if you give this
geometric interpretation the problem is
what happens if your surface is
non-convex which is the case always
right you should still talk of
probability right I the odds of these
two curves intersecting along the
coordinate axis is highest why
anyway so I mean just to uh just for the
sake of completion of the story I just
gave you both the interpretations right
but I am see but remember this you know
this is what the the the take-home
message is that the moment you
regularize
you are inducing bias with a prior on
parameters.
Okay. And this sort of restriction can
come from any way. I mean it can be an
explicit uh constraint on the
optimization or it can be a restriction
that you do on on the architecture or h
theta itself as I said right uh suppose
you assume your h theta to be a linear
function of data then you are heavily
regularizing this
from the functions of all possible from
the bag of all possible functional forms
for h you are only choosing the linear
families that's heavy regularization
that is Why? If you choose linear
models, they typically underfeit.
Why is that?
That's because by construction it is
heavily regularized.
You see what I'm saying? So any model
choice that we make, okay, is a
regularization implicitly.
Now what prior does it correspond to?
You may not know that explicitly for all
cases. know what is the prior that uh
that is imposed when you are choosing
linear family of models. This is
difficult to pinpoint but however
remember this that any choice that we
make on the model implicitly puts bias
on our
on on the on the uh on the optimization.
Now an equivalent statement would be
that any choice that we make on our
density function while we are doing ML
estimation is an implicit bias.
That is why uh in modern architectures
or modern machine learning the practice
is to choose as big a model as possible.
Okay. And then solve regularized
optimization problems.
Last class I told you right the typical
practice is to uh overparameterize and
then increase the bias. This is the
reason because any uh restricted choice
model choice that you make I mean you
asked me last class right? any
restrictive choice that you make on the
model is already starting with a lot of
bias. So why would you do that?
See, it's like this, right? We all
studied biology and history and all that
when we were when we when we went to
schools.
Do we do we use it in our in our
professions or anything? We don't
we over parameterize and then
regularize. No.
Now if you say that oh I will study
computer science and you know I'll only
study things that are related to
computer science from day one then you
are heavily regularized and heavily
biased from day one. Why would you want
to do that?
That's the idea. So that's why you start
with uh in fact when we look at neural
networks I'll give you another
perspective to this. Okay see you this
curve right? So now what we are actually
doing is if you start with an suppose
you are solving a polom polinomial
regression problem. let's say right you
always choose the highest possible
degree for the polinomial
right and then use nonpar penalties and
solve regularized le squares
effectively what we do is we start with
this region okay and then we push the
model back when I say push the model
back I mean
compared to yeah you just have the
regularized uh uh you solve the
regularized le square that's it yeah in
in neural network training you know
especially if you are doing see this is
the case when your when your model
complexity is defined as number of
parameters and so on I also told you in
the last class that this x-axis may also
mean steps of the iterative numerical
algorithm that we are solving in terms
of gradient descent
right
now suppose we are solving or solving
erm through gradient descent or
numerical algorithms Then what people
typically do is that keep training or
keep running your numerical algorithm
differentiation numerical
differentiation algorithm or gradient
descent for a very long time okay till
your uh training error uh reduces
drastically okay keep tracking your
validation accuracy and get this curve
and ship the model at this point
you [snorts] see what I'm saying so this
is called checkpointing so what you do
is at every point right you choose your
you know save your parameters. So every
gradient step is a new model isn't it?
Suppose you're doing EM every EM step is
a new model that you are getting. Save
your parameters at all points. Okay. And
ship the model or choose that model as
your final model at this particular
point in time. And this is called early
stopping.
Okay. Now here is the catch.
uh let's say that uh that you know I
quantify the number of gradient steps
using some parameter to to equal to 1 2
3 4 5 6 7 8 something right I can show
mathematically that
stopping my training with a iterative
algorithm at equal to to not is
equivalent to L2 regularization
with the the the regularization constant
lambda
defining where to stop.
I mean you can intuitively see why
right? So if you stop early or if you
ship a model here okay it should be
equivalent to starting from here and
adding some regularization and pushing
it back isn't it? It can be
mathematically shown that they are
mathematically mathematically equivalent
early stopping is equivalent to L2
regulariz regularization is what you can
show.
Okay.
Right. So this is one thing. Uh yeah
that that that was about early stopping.
I told you right. I mean there are three
ways to do it. Parameter non non penalty
is one way to do it. Optimization
procedures I just told you. I mean uh
where uh you stop early right? You stop
the optimization early. Actually you
don't stop early because you don't know
where to stop. You train for a long
time. Keep saving your models. Ship the
one that corresponds to the least
validation error. In fact, that is what
is done even today, right? I mean,
that's how you train it. And
architectural restrictions is something
that we will see later in the course,
right? Where you take a neural network,
a fully connected neural network.
A convolutional neural network is a
heavily regularized fully connected
neural network is what I'll show you
later in the course. Okay. A transformer
is one way to regularize any
architectural design that you do. Yeah,
there is one other optimization
procedural uh regularizer that I will
just mention uh without proving and then
we will move to the next topic. Uh we
will stop here and continue in the next
lecture.
