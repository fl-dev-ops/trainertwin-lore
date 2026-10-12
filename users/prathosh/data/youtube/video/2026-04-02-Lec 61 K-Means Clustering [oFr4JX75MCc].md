---
id: oFr4JX75MCc
title: Lec 61 K-Means Clustering
url: https://www.youtube.com/watch?v=oFr4JX75MCc
date: '2026-04-02'
duration: 36:10
model: youtube-captions (en-orig)
transcript: true
---

# Lec 61 K-Means Clustering

## Transcript

Welcome all.
We will continue our discussion on
unsupervised learning.
Last class
we began with our discussion on what
unsupervised learning is and defined
unsupervised learning
in terms of uh
latent variable models. That's what we
had done. So, we will continue our
discussions there.
Recall that in unsupervised learning we
are given data
which is a set
of
in realizations from a particular random
variable.
So, here uh note that
the difference between this and the
supervised learning is that you don't
have the label random variable.
Uh you only have the data or features
random variable that we have
observations from.
Now, the goal of unsupervised learning
is still estimating the under-
underlying distributions is the goal
here.
is still estimate
given D
which is still the same problem that we
have. And we use the exact same
techniques that we have
seen in this course, which is minimizing
the KL divergence or divergence metric.
Uh
but the distribution that we'll be
looking at right now is the marginal of
uh
And you can
see if there is uh PY, then this can be
called as a marginal distribution.
Otherwise, it's some distribution that
you would want to estimate, underlying
distribution that you would want to
estimate.
So, I also told you that uh one of the
uh most
famous ways of doing it is to model
uh PX
via a latent variable distribution.
>> That is you call
P theta as
the marginal over the joint distribution
of X and Z where Z is a latent variable.
The procedure that you solve the exact
same problem of divergence minimization
and estimate P theta.
Once you have a latent variable model
as a byproduct of having a latent
variable model, we also get distribution
such as P theta of Z given X which is
the conditional of the latent variable
given data, right? And that can be used
for several purposes. So, now the
question is
what is the use case or application of
estimating an underlying distribution
given D? See,
in the case where we had another random
variable which we call label,
the use case was
pretty obvious that we want to estimate
the posterior of label given data and
that we called as classifier or
regressor. So, given a new data point,
you pass that new data point through the
through this estimator and get an
estimate of P of Y given X. That gives
you a distribution over labels.
Now, in the unsupervised learning case,
why do we need to estimate the marginal
is the question. So, why do we need P
theta of X to be estimated?
As I said, in the latent variable uh
modeling scheme, once
So, P theta of X is estimated,
one can estimate
P theta of Z given X.
Which is the posterior of the latent
variable given data. Okay. Now, this
can be looked into as
clustering.
Clustering the data space X if
Z is discrete.
And this is feature extraction or
embedding or feature extraction.
If Z is continuous.
Yeah, if we estimate the underlying
distribution well, then
the posterior of the latent variable
given data
can be looked into as
a way to cluster the data
if Z is discrete. And
if Z is continuous, then it can be
looked into as some representation or
feature extraction
that you're doing from the data space.
I told you in the last class, right? Why
can you look into this as clustering?
And suppose Z is discrete and you are
looking at
K
K short
discrete random variable.
Then P of Z given X will tell you
whether this X
belong to one of those
K possibilities of Z. So, that is
grouping of data, which is also called
clustering. Right? So, any
unsupervised learning algorithm that has
a latent variable formulation with Z
being discrete can be called as a
clustering algorithm.
Always, right? And any unsupervised
learning algorithm which has
a latent variable formulation with Z
being continuous can be seen as
a feature extractor or an embedding
extractor. That is the way to look at
it.
Okay. So, now with this prelude, let's
look at a few algorithmic ways of uh
doing this. We already saw how to
estimate latent variable models, right?
One latent variable model that we saw
was the Gaussian mixture model.
Uh
which was estimated whose parameters
were estimated using the EM algorithm.
Which is still maximum likelihood
estimation, but we need to look at the
EM algorithm uh to do that.
So, let us uh
start from that.
So, case one.
Here,
Z is discrete.
And we have
X to be in RD.
In this case, what do we do? We write
P theta of X
to be equal to
the sum of
P theta of Z times P theta of X given Z.
This is the definition of the latent
variable model. So, in a in a mixture
density, we
make this to be a discrete random
variable and
call the density or represent the
density P theta of Z with alpha M and
all these individual component densities
are Gaussian distributions
with a particular mean
and a variance mu
or sigma.
Yeah, this is our
GMM model, so you remember this, right?
Now, there are M components here. We can
write this to be capital 1 to M. We have
this this discrete random variable Z now
can take
one out of capital M values with
probabilities alpha one to alpha M. So,
that is the model, right?
Now, estimate
alpha star, estimate theta star, which
is
the set of alpha stars
and we have mu stars and there are sigma
stars
via
EM.
So,
I won't expand this because we know how
to do this, right? So, given a
particular data set,
we know how to get the uh
parameters of an underlying GMM using EM
algorithm. So, we assume that we know
this.
We estimated these parameters now. So,
once we estimate these parameters, how
do we use this as the question? Right?
So, having
estimated theta star,
given
a test data point It doesn't have to be
a test data point actually. Given a data
point X,
uh from the distribution It It can be uh
from D or it can be outside of it as
well. So, let's generalize this.
It's sampled from the underlying
distribution PX.
We estimate
rather calculate because estimation is
done.
P theta star
Z given X.
So, what is this equal to?
It's equal to P theta star
X given Z times
P theta star
Z divided by
the sum of that P theta star
call it as X because there's a sum over
that, okay? We know how to estimate all
of these terms.
The RHS is completely known post
estimation, so we can get P theta star
of Z given X.
Now, what is this? This is a
a distribution
over Z
given X.
So, given a data point X, so this gives
you an entire distribution over Z.
Correct? That's what it is giving. So,
how does that look like? For
every X
that is sampled from the distribution PX
the distribution over uh
Z given X will look like this. So, this
is
P theta star Z given X.
And this is Z.
And we'll have
Right? So, this is 1 2
capital M.
So, for every data point, we get an
entire distribution over Z.
Correct? This is what we get once we
calculate P theta
Z given X, P theta star of Z given X,
right? So, what is this? This is
So, it represents
soft clustering as it is called.
In the sense that it is saying that uh
with uh probability this much it belongs
to the the fourth group. See, basically
the idea is the following.
Uh if you recall what a mixture density
is,
we are modeling every point as a linear
combination of multiple multiple
constituent densities. Okay? So, what is
this saying? What is P theta of Z given
X is saying that with what likelihood
that this data point X belongs to that
particular
component in the mixture?
Isn't it? So, P theta Z given X is given
X,
what is the likelihood that this
particular X is belonging to this
particular component?
In the mixture density. Okay? If you
look at each of the Gaussian components
in the mixture density as a group,
okay, within the data space, that's
exactly what's being done, right?
If you have the data space and if you
have K
uh Gaussian densities that that you are
trying to model the data space with,
each of the Gaussian distribution is
partitioning the data space into groups.
But, you know, when I say Gaussian
densities partitioning data space, it's
it's not very intuitive because all
Gaussian densities have infinite
support.
So, all of the Gaussian densities would
overlap, isn't it? The support of all of
these Gaussian densities would overlap,
but depending upon where the mu stars
and sigma stars are, so the spread that
each of these Gaussian densities will
have will be different different. Okay?
Now, if you look at each of the
constituent densities in a mixture model
as grouping of data, given a data point,
P theta of Z given X is telling you with
what likelihood that this data point
belong to that particular
count component in the mixture density.
So, that way this entire P theta of Z
given X can be looked into as a way of
clustering data.
Right? Albeit soft. What do you mean by
soft?
There is a non-zero probability of this
data point belonging to all of the
constituent groups.
What is it a consequence of? It is a
consequence of the fact that the
constituent densities are Gaussians that
have infinite support.
Does it make sense?
Okay. So, this is called GMM clustering.
So, this entire thing that we just saw
is called
GMM based clustering.
So, now if you look into this entire
thing as a black box, so given a data
set, what you give is a for every data
set
you give a vector of dimensions M.
Which is P theta star of Z units. That's
called GMM clustering.
Okay. So, what do you do with this
information? Okay, you cluster data.
What do you do? As I said, you can use
this
this this this distribution itself as a
feature and then solve with downstream
task.
When I say downstream task, it means
that let's say that you have labels
associated with it.
You first cluster it without labels and
get your Zs.
And
use those Zs as data, associate labels
that you already have, and solve and use
another neural network or something to
solve your classification or regression
task.
That's how you can do that.
Or once you cluster it, you can
visualize them, right? And also see you
will you will get information about
okay,
uh see what happens is typically
when you are given data and if you do
not have labels
suppose you run a clustering algorithm
like GMM, what is it actually telling
you is that it is roughly telling you
how many what is the likelihood that uh
that this this entire data gets grouped
into 10 different
classes. You should not call them
classes. I hesitated a little because
they're not classes. They're simply
subsets of
uh support. That's it. I mean, the
entire ambient space of data
what's what are what are the groups that
that you can look at. This is also
called exploratory data analysis because
what you are trying to do that you're
trying to explore how data is is grouped
or clustered.
Makes sense, right?
In fact, the hyper parameter here is
this capital M, the number of
clusters that we would want and whenever
you run a GMM algorithm or a clustering
algorithm in standard packages, you'll
have to choose M as a hyper parameter.
How many groups do you want? Okay.
Okay, so this is GMM clustering.
Now, suppose we want to turn this soft
clustering into hard clustering.
In the sense that So, let's write it
down. Suppose
Suppose we want
P theta star of Z given X
to be
direct deltas.
So, you all understand what direct
deltas is, right? With probability one,
it should have it should belong to one
particular it should take one particular
value and it should be zero everywhere.
Now, how do we change GMM
so that the posterior of the latent
variable given data
becomes direct delta.
Any
Huh?
Okay, I mean, of course, you can take
maximum out of it. That's a post factor
thingy,
right? But, you know, can we put some
constraints on the way our component
mixtures are so that by construction P
theta of Z given X becomes direct delta
is the question.
We can
fixed support.
Correct. So, that's the way to think
about it. So, now know, should
we should make it fixed support.
Meaning, all these Gaussians that we are
looking at have to have
fixed support. In fact, it doesn't
suffice if you have fixed support.
It should have
uh infinitesimally small variance.
Right? Only then it will partition the
data space into non-overlapping
subspaces.
You understand what I mean? So, in this
case, what should happen is the
constituent Gaussians
should have All of these should have
different means,
but variances
which are diagonal, okay? And we want
this variance
to go to zero. We need to have
infinitesimally small variance.
Okay? So, if you do this, what will
happen is
this implies
this
These becomes All of these posterior
will become
direct deltas. So, what does that mean?
For a given data point,
with probability one,
the given data point with probability
one belongs to only one cluster. That's
it. One of the constituent Gaussians,
not all of them.
Okay?
Now, the interesting part is suppose we
make this uh change, okay? Uh which is
this.
The EM algorithm that we know of
will take a surprisingly simple form.
Recall what What we do in the EM
algorithm? So, we had two steps.
What was the first step?
Of course, we have to find that
expectation expectation of the joint
distribution. Now, recall what the elbow
is.
Sorry, not elbow, the EM algorithm.
So, what was that? The E step.
So, you compute
the expectation of
I think uh this joint distribution,
right?
Can somebody remind?
It was the
Was there a log here?
I think it is P theta of the joint
distribution of this
divided by
QZ.
Actually, Z given X, right? That is what
we were saying. And this expectation was
with respect to
QZ given X. In fact, uh I mean
this is what we did, but if you recall
uh I can actually effectively take this
denominator out.
Because the the it will be the entropy
and it is independent of whatever we do,
right? I can actually take this out.
Remember? Right? So, this is this is the
E step. And what is the M step?
So, we had to do the argmax of
Yeah, the optimization is over the
parameter space. And what is the
objective function here?
This thing, right?
These are the the EM step that we do.
Now,
uh suppose you assume uh the constituent
Gaussians to be of this form, you know,
they have different means and their
variances are infinitesimally small.
Okay?
One can mathematically show that these
two steps Okay? will converge into
something that I'll just then mention.
So, you have to take that as a homework
and show that these exactly they are the
same. But what will happen is the
following. Okay? So, the E step
Let me first first write down that
algorithm.
Which is actually called the K-means
clustering algorithm.
Let's call this
M-means clustering because we are saying
that there are M components.
Initialize
M mean vectors randomly.
Okay?
So, while convergence do
And by the way, what is the optimal Q Z
given X in EM? Actually, the E step also
has one other thing, right? So, you have
to set Q of Z given X to be
Yeah, P theta of
Z given X, right? This is this is there.
We also have this, right? Okay, while
convergence do, what do we do?
First
Assign
X I or every X I
each X I to
one of the
M means
where
solving this, so you take argmin
It doesn't matter, no, because it's it's
it's it's just a distribution of Z. Can
be the conditional or can be marginal as
well. Yeah. So, what you have to do is
that you assign each of the data points
XI, okay, by minimizing
uh
the distance between
that data point and all the means that
we have.
So, while convergence we'll have to do
this. We'll have to assign each XI to
one of the M means by solving this
optimization problem. So, what are we
doing? There are M mean vectors.
Calculate distance of the point under
consideration, the data point under
consideration, uh from all these M
means, okay, and look at the one that is
the closest.
Okay? And you assign this data point to
that particular mean.
Do you see this? This is first thing.
So, what do we have right now after the
after the first step, every data point
in the data set is assigned to one of
the
means.
Okay? The The second step, what you do
is recalculate
mu M
after
the assignment.
As
so mu
j is equal to
1 by
the cardinality of set j
sum over set sj and
all x j's that would belong to the set
j.
Where
where sj
is the set of
all data points
that
got assigned to
mu j
in step one.
Do you see this?
Start with random initialization.
In the first step, assign each of the
data point to one of those m means
by looking at what is the closest to
that data point. And once you have it,
you have one assignment.
Right? Now, update the assignment by
taking the mean
over all those data points that are
assigned to a particular mean.
So, it will be slightly shifted.
It will be shifted, right? Because uh
initially you start at randomly, then
you assign based on distance. Once the
assignment is there, you compute the
mean again. So, new means will emerge,
okay? And keep doing this. What if your
data point is equidistant?
Break the tie arbitrarily. That is what
That is how it is done. The ties are
broken arbitrarily. So, this is end
while. Upon convergence, end while. Upon
convergence.
Now,
what is the convergence criteria is that
uh put a bound on
how much the mean is changing
at every step.
Right? If the if choose an epsilon, if
the mean assignments is not changing
more than epsilon, okay, in magnitude,
then stop there.
Okay. So, this is called the K-means
clustering algorithm.
M-means or K-means clustering algorithm.
So, it takes K as a as as an input and
divides data into M distinct clusters.
So, now once this algorithm is done,
what have you actually done is that
every data point is assigned to one of
the M clusters.
Now, my claim is that these two steps
are exactly the expectation and the
maximization steps.
Okay, can somebody tell me where is the
expectation and where is the
maximization happening?
Step two is expectation. Step one is
maximization.
Right? Assignment is maximization
because why?
Getting a
Starting with what is starting with P
theta of Z given X. So, P theta of X Z
given X is one cluster assignment
because now Z is discrete.
And we are looking at direct deltas. All
P theta of Z given X is not direct
deltas. Right? Once you assign each of
the data point to a particular cluster
center, this is what we are doing.
Once we do that, we compute these
expectations and this expectation is
nothing but
getting the new cluster centers, which
is getting a new estimate of this. And
then
you assign based on
maximizing this particular thing now or
minimizing the distance. You know, why
should How did this maximization turn
into the minimum distance?
It's because Yeah, it's because there's
a Gaussian and we have e power minus
term in the exponentiation and that
minus will just make this maximization
into a minimization thing. So, here is a
homework.
So, show that the GMM algorithm that is
applied with a constraint that our
Gaussians are having this particular
form with the variance going to zero
will give rise to this K-means
clustering algorithm.
It's pretty simple to show actually,
right? And if you
if you if you if you do the math, it
will just nicely come out.
Okay? So, this is the hard clustering
algorithm.
All right?
Any questions here?
Do we have convergence guarantees or any
proof like
So, this is EM.
Since this is EM
and we know what EM does, all that we
have is likelihood does not decrease.
That's it.
K-means clustering algorithm is nothing
but EM.
So, it's as good as EM.
Okay?
In fact,
you can kernelize this as well. What do
you mean by this?
Instead of operating at
operating on the data space X, you can
operate on
some transformed space fee.
Okay? And again, you know, this is
another nice little homework to do that
you you should show that
if you take a transformed space
fee, then the K-means clustering
algorithm does not require you to
actually compute the transformation as
long as you have the kernel.
Just like we did with the kernel
machines, right?
So, that's called
kernelized K-means.
Okay, you can do that with using a
kernelized space as well.
Okay, so this is about
the clustering algorithms where
we explicitly model the data using a
latent variable model and try to find
the distribution P theta of Z given X,
okay?
Now, there are algorithms where
the model is not explicitly made to be a
latent variable model, but you know, you
make it an implicit latent variable
model.
We'll take some examples on that, okay?
In fact, yeah, so what do I mean by
implicit latent variable models? Suppose
you build a neural network
on some data.
Now, remember I told you that neural
network is
a composition
of linear and non-linear function. It's
a composite function.
You can break the composition at any
time and call that as
an embedding or a representation.
So, what do I mean by that?
Suppose you have an MLP which has 10
layers.
If you tap at the fifth layer of an MLP,
that is still a transformation of data.
You can still treat that as an implicit
latent variable model.
You see that? So, now the only thing is
that
actually I mentioned this during
transfer learning as well, right? So,
you train a neural network and then tap
the features at an intermediate layer
and use it for downstream task.
But typically when you use
a neural network as an implicit latent
variable model,
you wouldn't solve the implicit latent
variable model on a classification task.
What do I mean by this?
You don't want your neural network to be
trained
for estimating the conditionals given a
particular type of label set.
Why is this? Think about it. Let's say
that I have Uh,
of digits,
handwritten digits which I'm talking
about the MNIST dataset, right?
Now, suppose I build a neural network to
solve the problem of classifying uh
digits from one to zero or whatever,
right? One to 10.
Then that neural network has partitioned
the data space into the semantics as
imposed by this particular labeling
scheme.
Let me repeat. This is something which
is important to understand. Every
classifier can be seen as a method to
partition the data space. That we have
seen, right? During the discussion on
decision trees and all that. Given a
classifier, what does it do? It will
partition the data space into
uh non-overlapping subsets. Or rather,
overlapping or non-overlapping subsets.
Now, given a labeling, what does this
partition depend on?
This partition depends on the labeling
scheme.
Right? So, now, if I have built a neural
network to solve one particular uh
problem of
the discrimination, which is a
particular estimating a particular
posterior density of the labels, then I
have partitioned the data space in one
particular manner.
Okay? Now, suppose I take features of
such a neural network. These features
are highly correlated with that
particular label
set.
Now, if I have given a a neural network
that is trained on MNIST uh
with the task of classifying digits,
I cannot use that use those features to
classify that same data set on, let's
say, the orientation of digits.
Suppose I want to solve another task
where I would say that, you know, every
digit uh or every picture that has a
knot, like three, five, eight, and all
that, right? Or curves, for instance,
have to be in one category. All the
images that does not have a curve should
have to be in some other category.
It turns out that the features that I
have extracted, okay, from an implicit
latent variable model, which is a neural
network, by solving a task that would
differentiate digits, digital semantics,
cannot be used for this task.
Because the partition that that this
particular neural network has learned
is not correlated with
some other task, but it is correlated
with that particular semantics that we
have imposed on data space.
Does it make sense? That is why when
solving, you know, when extracting
latent variables,
you try to estimate the marginals, but
not the posterior on a particular given
semantic, which is called the labels.
So, that is why people estimate the
marginals, not the
or rather estimate get the features by
solving
marginals or or or by estimating
marginal densities, but not the
posterior with a particular semantic.
Do you Do you understand what I'm
saying? Right? So, now, what we will see
is how do we use the neural networks and
the other kinds of linear models
to get the features or implicit latent
variable models solving tasks
which are not conditioned on a
particular label semantics.
Okay, I'll give you a few examples of of
such tasks, and then we can
close this.
Uh, we will stop here and continue in
the next lecture.
