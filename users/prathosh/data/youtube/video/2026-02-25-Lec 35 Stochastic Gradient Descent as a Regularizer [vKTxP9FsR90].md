---
id: vKTxP9FsR90
title: Lec 35 Stochastic Gradient Descent as a Regularizer
url: https://www.youtube.com/watch?v=vKTxP9FsR90
date: '2026-02-25'
duration: 22:02
model: youtube-captions (en-orig)
transcript: true
---

# Lec 35 Stochastic Gradient Descent as a Regularizer

## Transcript

Now consider so I'll say another example
of regularizer
suppose
so the data is uh x comma y i
we have it from pxy.
Okay.
Now create a new data set
as follows.
So let
uh for every x i okay
for every x i in d okay so x i cap is
equal to x i + epsilon where epsilon is
sampled from normal 01
you see what I'm doing take a data point
okay per
Take a data point sample uh from some
gian distribution add per t
and now create a new data set. So now d
cap is a new data set that will now have
x i cap comma yi.
Will the distribution of this be same as
pxy or different?
Will the distribution of this be same as
PXY or different? It will be different.
Of course, it will be different. Why do
you think so much? Yeah. So, now here is
the climb. The climb is
so erm
on Dcap is equivalent to
Please prove this.
So empirical risk minimization on dcap
is equivalent to regularized
erm on b.
And now you can actually I can actually
make this some alpha * i. Okay,
I just scale my uh perturb perturbation
with I. Now what is the guess? The guess
is this. This alpha
is that lambda.
[snorts]
Is it directly proportional or inversely
proportional? Find it out. This is
related this alpha is related to that
lambda.
A brilliant point here, right? that take
your data points pert with some noise
and solve erm it will have the same
effect as regularization.
Why do you think it should be the case?
So I'm saying instead of solving a
classification problem on images add
some noise to those images and then
solve
it is equivalent to regularizing. Why?
Actually you can see this in multiple
ways. Okay, let let me hear two of them.
Any any opinions?
>> Why? That's the point, right? I mean,
okay, you take something add some noise.
>> See, mathematically you can show that
the Okay, how do you how do you show
this? By the way, what is the way to
show this? Mathematically,
algebraically,
it's very simple. Write down the erm on
dcap you get some objective function
over optimization over theta write down
I mean you will see that that is
equivalent to that is algebraically
equivalent to a regularized drm on d
that's it
it's very simple actually you can see
this why why should this be equal just
do that okay so yeah I I will not I will
not tell you that just try that exercise
once so now intuitively why should this
be the case
It is.
>> Huh? What? Why should that be useful?
>> Exactly. Right. It expand in the
manifold.
>> So now if you take gajian noise and add
it to add add to it, right? That tiny
manifold that you are looking at now
will become now will become field
because gajian is the entire ambient
space.
Okay.
you know think okay so I think you know
too many things came to my mind so I
just organizing my thoughts which one
should I present to you first now what
happens if I add too much noise to this
suppose I increase my alpha too much
what will happen to that so the data
will be submerged into noise no
completely
right so now if you were to now explain
noise which is a goian distribution then
you too much bias and you'll go to the
underfitting regime. So now the the
reason I just pause for a moment is that
I wanted to make this point that the
regularization constant lambda that you
have controls which point that you are
operating on this particular curve.
It is the lambda with which you can move
around this curve.
If you that's a knob that's why it's a
hyperparameter. If you make your lambda
to be very high then you will push the
model into the underfitting regime. If
you make it too small you'll be in the
overfitting regime. So same thing
happens if you add too much noise
then it'll be underfitting. See again
you know if you if I were to give the
philosophical equivalence of it right
when would a when would a human being be
too biased and underfoot
is when the when the person is not shown
difficulties
it's too easy to learn
somebody feeds you somebody gives you
everything oh this is world you you get
terribly biased
now how to regularize
add noise
right make life difficult
okay it's regularized so no bias will be
reduced now make it too difficult
the model will break
that's the point so that's why you know
that lambda has to be
rightly played with okay that you know
you are not too biased and you know not
yeah too bogged down with noise and so
on so That's basically anyways a
philosophy aside the point is adding
noise uh to the manifold is equivalent
to regularization. In fact this comes up
in multiple ways when we look at
generative models a bit of marketing for
my next course right. So there is this
problem called vanishing gradient
problems which comes up with uh
generative models such as adversarial
networks. Gradients will simply get uh
saturated and because of that saturation
you get into problems called mode
collapse. I mean please don't worry if
you don't understand whatever I'm
talking this is only a marketing
 technique anyway right so
what happens there is one of the ways to
solve that is to p up your data and then
build a generative model because it has
a regularization effect expanding the
manifold anyway we will do all this in
in a greater mathematical detail in our
next course right if you happen to come
there anyway the point is remember this
the take-home point is perturbation of
data has a regularization effect so why
am I saying this There is one other uh
point uh that I wanted to make here is
remember what algorithm did we use for
optimization numerically? Do you
remember the algorithm
gradient descent right? So let's write
down that. So
revisiting gradient descent.
So what is gradient descent? We have our
rcap uh theta to be uh 1 by n
some loss.
[cough]
And please note that all of this
treatment is independent of having or
not having a y.
Everything that we are doing applies to
supervised learning, unsupervised
learning, generative learning and
everything. Okay. 2 for us you know y is
one other dimension of data remember
that right just the distribution changes
okay this is our r so what does gradient
descent do
so you have theta t + 1 is
theta t minus
uh some
beta * the gradient of the
this uh empirical with respect to theta.
So this is what we do in gradient
descent, right? This first order
gradient descent. All of us know that.
So let us slightly
alter this gradient descent. So now what
we will do is
how do we do this now? Uh define
X I belong to DB
uh where DB is a
uh B length subset of D.
So we have data set D. We do a random
sampling a B length random sampling from
D. Okay. and we define the empirical
risk or we compute the empirical risk
for only those B samples. Okay. Now what
happens is uh the altered gradient
descent is as follows. Theta t + 1 is
beta *
compute the gradient over this
particular case.
Okay.
Now you understood what we are doing
procedurally right? Procedure- wise
instead of computing the gradient on the
empirical risk the true empirical risk
if I if I may have if I can use that
right anyway the entire empirical risk I
do a subsampling of data okay and
compute the empiric the average loss or
empirical risk over that subsample and
then do a gradient descent.
Now
in practice what is what is done is that
once you do this how do you s how do you
know that B I mean how do you sample
that uh B uh length subset is by random
sampling okay then you know you keep
that aside and you do another random
sampling of that B length subset and
keep doing it over the entire over the
entire data set till the till the end
samples okay and then do gradient
descent over all those small subsets and
if you run through the entire data set
once that way by doing this B
subsampling it's called one epoch of
training.
Okay, it's called one epoch. So you do a
subsampling and you run through the
entire data set, it's called one epoch
anyway. So this is how you do it. Now
this is not gradient descent because you
know we are changing the object
objective function completely,
right? And by the way this has a name.
This is called the stoastic gradient
descent.
the star of uh this thing you know
optimization SGD it's called okay
stoastic gradient descent
now what is stoastic about it
[clears throat] sampling is stoastic
here sampling is stoastic now how is RB
cap rcap b theta related to r theta
it's it's a noisy stoastic estimate of
that
now why should one do this. See, of
course, one reason to do this is that
you know computing or computing the
gradient on uh the entire data set may
not be computationally feasible. You
need to add those many things. That's
not the actual reasons. The actual
reason is that this has a regularization
effect.
Why? Because of the fact that we saw
here
any perturbation of data has a
regularization effect. Now any
perturbation of gradient also has a
regularization effect.
Now this is perturbing the gradients
isn't it? If you do a random sampling
right I mean this you can actually show
this right I mean this is probability
theory uh you take the sample average
and you change the n you take a do a
subsampling of that and compute another
sample average you can show that this is
a stoastic estimate of the other.
[clears throat]
Okay. So now SGD
is considered or rather observed to be
empirically superior than the the other
thing is called batch gradient descent
or gradient descent. By the way it's uh
it's SDDD is considered to be superior
because it has regularization effect.
[snorts]
Okay. And by the way this B is typically
referred to as the batch size.
You hear this term no 32 64 or whatever
that's called mean the number of samples
that you take to take the stoastic
estimate is what is called as batch size
okay
right did I leave anything
any questions on this
come again
>> that this has a regularization effect
yes indeed so I think yeah let me just
uh uh summarize what we did and then
we'll take questions. So we have come to
a an epocal point in the course right so
what we did so far is that uh we
formulated the problem of ML as that of
you know we formulated the problem of ML
from two different angles. One was that
of estimating the underlying
distributions. Now first of all we saw
we started seeing the data as points in
RD. Okay. uh for the for the empirical
risk minimization approach
these are simply points in uklidian
spaces. For the probabilistic approach
these are the points of the range space
of a random variable which has an
underlying distribution. And the entire
problem of machine learning is that if
you are given some samples that are
sampled from this underlying
distribution, you want to estimate the
underlying distribution. Okay. So we saw
a way to do that. Uh one way to do that
is by the procedure by the idea of uh
divergence minimization where you define
okay a divergence between two
distributions. One is the true
distribution that you are trying to uh
estimate and the other what we call as
the model or hypothesis or the
parameterized distributions. You assume
a parametric form on the distribution
that you are trying to estimate and
define a distance measure between the
true distribution and the parameter
distribution and you cast the problem of
estimating the distribution as that of
estimating the parameters of the model
or the parameter distribution through
minimizing the divergence between the
two distribution and the parameter
distribution. Okay, this is what we
called as the minimal ML estimate or it
also turns out that it it is equivalent
to maximizing the so-called likelihood
function the log of the likelihood
function and we saw a few procedures to
do that. So we do it solve it in two
ways. One in the uh in the analytical
way which seldom happens it happens only
with primitive distributions and there
is also the empirical or the numerical
way of doing it. Either you do it using
numerical differentiation or for the
cases of uh latent variable models you
resort to this iterative algorithm
called the expectation maximization
algorithm. Right? And there is this erm
angle of looking at things where you say
that okay there are two sets and we are
trying to learn a function between these
two sets. There is an underlying
function that is unknown. We define what
is called as a loss function and we cast
the problem of uh learning the
hypothesis as minimizing what is called
as the empirical risk. Okay. Or the
expected loss function. And since we do
not know the underlying distribution to
compute the expectation, we take the
empirical estimate of it using the law
of large numbers. needs to be solved er
and we also saw we also saw that there
is a one to1 equivalence between solving
problems uh using the empirical risk
minimization framework and divergence
minimization framework and they are
exactly equivalent and we also saw the
saw these classes of algorithms where we
make an assumption uh not only on the
hypothesis class or the underlying model
but also on the parameters that we are
looking at in terms of distributions and
these are the basian methods and we saw
an example for that which is called the
map estim estimate and we also saw that
distributional uh estimation can be done
in an in a nonparametric way. Remember
pars window and nearest neighbor
estimates right where you can estimate
the distributions not estimate evaluate
the distribution at a given point which
is what we need uh uh to realize some of
the hypothesis function in a
nonparametric way. uh and we also saw
that if you are considering a
classification problem then the
hypothesis that would minimize the true
risk is the one that chooses based on
the posterior of the of the labels and
this is called the base classifier and
uh one can use distributional estimation
techniques to realize a base classifier.
Okay. And we also [clears throat] saw
from the ERM angle different choices
that one can make to the hypothesis
functions and then solve ERM to get the
parameters. Specifically, we saw the
linear classes of models which we
generalize to the generalized linear
models. And we saw a few examples of uh
the linear regression and uh uh uh the
logistic regression, right? with a
particular kernel function where you
change your data. You have a particular
function that transforms your data and
then you find the parameters through
either the the analytical
differentiation or through numerical
methods. Okay. And we also saw that uh
that when we are trying to solve this
problem in in a pragmatic setting, we
end up having this bias variance
dilemma. Okay. and which which which
which is actually that that the the risk
that we are trying to minimize okay gets
decomposed into two different terms and
uh typically we want both of them to be
or rather we want both of them to be
minimized while typically we can't
minimize them simultaneously. So
pragmatic approach is to start with a
model that has very low bias and uh uh
high variance and then uh push it back.
And this procedure where you increase
the bias of a model is what is called as
regularization. And we saw a few ways to
do it where one is to put an explicit
solve a constraint optimization problem
by putting a constraint on the parameter
space or then you know you you part up
the data with a with some noise and you
change the architectural or the h the
choice that you make on the hypothesis
function and so on. Okay.
Did I just summarize the half of the
course in 5 minutes? I don't know the
more whenever I do this I feel like why
did I spend half a semester do teaching
this anyway. So, so this is how you need
you should look at all ML algorithms and
this treatment okay is common across all
the ML algorithms that you see okay be
the generative models you know be uh
discriminative models supervised
unsupervised and all this this is what
we do now in the rest of the course we
will continue our journey by uh looking
at different choices of the hypothesis
function uh the next that we will look
at is what is called as the kernel
methods, okay, of which a support vector
machine is a is a member. SVM uh is is
not the go-to choice for classifiers or
regressors in today's world. Albeit it's
a it's an elegant formulation. I know
it's an ML course is not complete by
looking at SVM. Okay. So when we were
students, an ML course would stop with
SVMs because that was the
state-of-the-art.
Now it's the neural network. So we will
look at kernel machines and SVMs. I'll
quickly do it in a couple of classes. Uh
okay before coming to the next class
please uh brush up your optimization uh
fundamentals specifically the primal
dual formalization formula for
formulations. Are you people aware of
these things called KKT conditions and
so on please look at them cuz we'll use
that uh in kernel machines and SVMs we
actually write down the KKTs and so on.
So brush that up after SVMs we'll
straight away jump into uh the uh the
neural networks or this course is is
called
uh so we do have neural networks so
we'll go to neural networks and spend
some time on that we'll look at this one
algorithm called back propagation and
then we will go to specified
architectures such as CNN's RNN and
transformers quickly and finally some
unsupervised learning algorithms okay
that's how it's going to be uh yeah so
thank you uh this ends this uh current
class and we'll meet in the next
