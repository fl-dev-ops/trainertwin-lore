---
id: 2wyxSgVolJg
title: Lec 56 Ensemble Methods, Bagging and Boosting
url: https://www.youtube.com/watch?v=2wyxSgVolJg
date: '2026-03-25'
duration: 35:54
model: youtube-captions (en-orig)
transcript: true
---

# Lec 56 Ensemble Methods, Bagging and Boosting

## Transcript

In today's lecture, we will be looking
at the ensemble methods, specifically
the
boosted aggregation and the boosting,
which are called bagging and boosting
algorithms.
So far, we have seen training individual
hypothesis functions or classifiers.
Now,
it's a matter of human experience that
instead of having one person judge, if
you have a committee of people
uh sitting and judging, so they tend to
give better decisions.
So, the same idea is extended to
classifiers, where instead of having to
train one classifier for a particular
problem or one hypothesis function for a
particular problem, you train multiple
of them.
So, why do you do this?
Remember that uh in our discussion
on uh
the bias and variance,
the variance term
had
this particular hypothesis, which we
called as as the aggregated hypothesis
or the average hypothesis. So, variance
mathematically is nothing but
the deviation of the aggregated
hypothesis from the hypothesis that we
have trained on a particular data set.
Correct? It was H bar minus HT in our
notations. Okay? Distance between them.
Now, if you want to reduce the variance,
we'll have to ensure that whatever we
train on one particular data set is
close to the aggregated hypothesis H
bar. So, how do we do that?
The one of the ways to do it is to train
multiple
hypothesis functions, okay, on multiple
data sets and take an aggregation.
So now, this shows that it is guaranteed
theoretically that if you take
classifiers that are trained on multiple
data sets and average them,
your error will be lesser compared to
training an individual classifier.
So, that's why ensemble methods are
extremely powerful in the sense that
you can always find an ensemble that is
having a better performance compared to
individual classifiers. And most of the
commercially available classifiers that
are used in industries are ensembles
because of this particular reason.
And we'll also see that
uh
the individual classifiers that are
being ensembled need not be
very, very good. In the sense that, you
know, they can be weak learners. It's
called weak learner. Every every
individual component of an ensemble is
called a weak learner in the sense that
they just have to be better than chance.
Suppose you are
solving a binary classification problem,
random decisions
will give you
50% accuracy. So, any classifier
that gives you less than 50% accuracy in
a binary classification problem
is a bad classifier, right? Because it's
worse than chance.
So, uh
I keep seeing this. I give them a
uh
10 class classification problem.
So, they come and tell me that they've
built a classifier that gives them 5%
accuracy.
Well, random chance will give you 10%
accuracy, right? So, everything that I
mean a weak learner has to be better
than chance. So, whenever you create
ensembles,
the
prerequisite is all the individual
hypothesis that we learn have to be weak
learners in the sense that they're
better than chance. As long as they're
better than chance, ensembles always are
guaranteed to give you better accuracy
compared to individual classifiers
because of the fact that the variance
>> [clears throat]
>> is the difference between aggregate and
the individual classifier.
Now, the problem uh the practical
problem here is that we will not have
So, remember what H bar was. So, during
uh
the discussion on the bias variance
decomposition, H bar was the expected
classifier,
where this expectation was on a
distribution over data sets.
Okay?
But, we only have one data set in
practice. So, we don't have multiple
data sets. So, what do we do is the
problem is the question.
If we have
If we have multiple data sets, of
course, we can train multiple
classifiers and average them. Since we
are given only one single data sets in
practice, how do we ensure that we
compute this expectation is the
question.
Now, what's the uh the closest thing
that you can do to this expectation is
approximate this expectation by creating
data sets
by doing a sampling with replacement.
Okay? So, in ensemble methods,
expectation over PD is approximated
via
creating data sets
by sampling with replacement.
Wait.
Create multiple data sets by sampling
with replacement and then
build hypothesis and then average them.
So, that is what ensemble methods will
do.
So, we will look at uh
multiple ways to do ensembling. One of
them is what is called as uh boosting.
Just simply sample with replacement
to create ensemble.
Now, if we do this, then
suppose
So, data set D
contain
n samples.
Create
B training
sets
by sampling
so that
each
new data set DB
D small B
has n samples.
Okay? If we have uh
capital B number of data sets, each of
which have uh uh
exactly n samples or n samples, so we
know that uh
there's a
Okay, let's simply do the math, maybe.
So, now, since we are uniformly drawing,
right? So, probability of
of a sample XI being picked
is 1 over n.
Probability of uh
XI
not
Okay, wait.
XI
not being a part of a data set DB, how
do we calculate this?
1 minus 1 over n.
1 minus 1 over n is the probability that
a sample is not picked in one draw. If
you do n draws,
you'll have to multiply this n times.
Right? So, now, if uh
So, DB has n samples, less than n
samples.
No, exactly n samples. You are doing
sampling with replacement. If the whole
data set itself has n examples, Yeah.
then again creating a subset of n
examples is the same thing.
If I have n examples, again creating one
more subset which is just a replication
of the same thing.
Unless the order matters. Why? There can
be duplicates, no? When you're doing
sampling with replacement, there'll be
duplicates.
Of course.
There'll be duplicates. Yeah.
So, that's why the probability of a
particular sample not being a part of an
entire data sets data set is 1 minus 1 1
mi- 1 over n raised to n. So, at limit,
so if the if you take n to be going to
infinity, then
this is a standard limit, right? What is
this equal to?
1 by e,
which is .36.
Okay? Which means that
there's 36 36% chance
or rather roughly 36% of the samples
will never be a part of the
data sets that we use to train
classifiers.
So, this has an implicit Well,
regularization effect.
Because it it it creates an implicit
validation data in the sense that, you
know, this is coming for free. When you
ensemble,
there are samples that are never
seen by any of the classifier individual
classifiers, right? So, when you that
that's one of the reasons why Now, we'll
show how to
exploit this in a while. Okay? So, the
aggregation um
train
B independent
classifiers or trees.
So, call them F1 of X.
Okay, we have we've been using H for
classifiers, right? We'll use H.
H2 of X so on up to
HB of X.
Sorry.
The final prediction
is simply
Y cap
for the bagged
Okay, this is simply the average.
Okay, so if it's classification, we'll
have the
approximate this by taking the majority
vote if you have n of them. If it's
regression, you just take a numerical
average of it. That's it. Okay?
Now,
one question that is to be answered is
when we are can we do any better, you
know, in the sense that
when we are when we are sampling, there
are two questions here. How do we
sample? Right now, we just sampled
with replacement and we gave equal
importance to all of the samples. The
other thing is how did we choose the how
did we train the individual classifiers?
We just trained them uh doing any RM or
whatever sample data sets that we have.
Can we do something else, you know, can
we do something better here is the
question. So, there are algorithms uh
that will improve both of these things.
Okay?
Uh
AdaBoost, for example, does not do a
sampling
with uniform weights. It'll do a
sampling with uh specific weights that
are learned. We'll see that.
Gradient boosted trees will not train
every classifier on the entire data set,
but it trains it on a subset of data set
as we will see now and why that is of
importance is a question. We will answer
all this in a while. Okay?
Now, let's look at uh the
idea of random forest.
Yeah.
Uh what's the question?
Uh
Huh. [clears throat] So, you train one
hypothesis on one data set. Right? You
By sampling, you get one data set. Train
it on uh train one classifier on one one
or one hypothesis on this. Okay? So,
let's look at
This is bagging.
Oh, yeah, sorry.
This is bagging.
See, boosting is a special case of
bagging as we will see. Yeah.
Thanks for noticing that. Okay. So, now
let's look at the
variance
of the ensemble. Let's Let's look at how
to calculate this.
Now, we train B individual classifiers,
right?
So, for Suppose
uh ZI
represent a random variable
corresponding to
to the prediction
of
a hypothesis of the i-th hypothesis
on a given data point.
See, since a hypothesis function is a
deterministic function and we have
stochasticity on X,
the prediction also has a stochasticity,
right? So, let ZI represent a random
variable that is simply the output of
the i-th hypothesis for a given data
point. Okay?
Now,
so
how many Zs we will have now? B of them.
Cuz we have B hypothesis functions.
Okay? Now, since
since all the hypotheses
are trained
on
the same set of data
or other
or data coming from the same
distribution,
data sampled from
a given distribution,
we assume
Z1 through ZB to be
identically distributed.
See, please note that I'm not saying
that they are
statistically independent.
Actually, that's the catch.
They will not be statistically
independent. Why is that?
Because we have uh data points that are
repeating
by construction, but we can assume that
they are identically distributed. Okay?
Now, therefore, let the variance of the
individual classifiers, all individual
classifiers,
be represented by sigma squared for all
i.
Okay?
They are not statistically independent
since
we are doing sampling with a replace
sampling with replacement. Okay?
Since they are not statistically
independent
since
random variables ZI and ZJ
are not
statistically independent,
we can compute the correlation between
these two random variables.
Call it some row.
For all i not being equal to j.
Right? Now, we have
correlation
to be equal to
covariance
by the product of individual variances,
right? So, this is the standard
formula, which implies
that
the covariance
between these two random variables
is
row times
sigma squared.
Correct?
Why? Because sigma is equal to sigma j
cuz we have assumed all of them have the
same variance. So, therefore, the
covariance is given by this product.
Okay?
Now, what we should do is we'll have to
predict the variance of the or rather
we'll have to estimate the variance of
the ensemble.
We'll have to see what the variance of
ensemble is. So, now to calculate
the variance of ensemble,
we have Z bar
to be 1 by B.
Right? The
ensemble predicts
the average of all the individual
classifiers. This is the definition of
ensemble, right? So, do you see that
whatever we have been writing as H of X
is what I'm representing as Z.
The output of the predictor is the
random variable Z here. Okay? So, this
is the ensemble. So, what we want to do
is that we'll have to calculate the
variance of this.
What is this? This is variance of
1 over B
sum of these random variables and note
that
the individual random variables are not
statistically independent, right?
What is this equal to?
1 over B squared the variance of uh
Let's skip the algebra.
Now, the variance of uh sum of uh
B random variables, what is this equal
to?
When the random variables are not
statistically independent, we have the
individual variances plus
the covariance
for all the cases uh where i I not equal
to j, we have this.
>> [clears throat]
>> We just have calculated what the
covariance is, correct?
Can I skip the algebra and simply write
the final expression?
Please do the algebra.
So, finally, this will be
rho sigma squared plus 1 minus rho
divided by
B times
sigma squared. Please complete the
algebra.
Okay, we have we need we have everything
that we need. Just complete the algebra.
Okay. Now,
this is what is important. So, variance
of the
classifier Oh, actually, hold on. So,
this implies cuz there's that 1 by B
term there, right?
Variance of the aggregate is given by
this particular
formula, okay?
Now,
remember what was our initial goal? So,
our initial goal for ensembling was that
we wanted to reduce the variance
of the hypothesis.
The variance that appears in the
bias-variance term. Uh so, that the
overall
uh
risk will reduce, correct?
Now, this is what the variance was. Now,
if you want to reduce this, what do we
have to do?
We'll have to increase B.
If we increase B, then the variance of
ensemble
decreases.
So, this is the proof that ensembles
always reduce the variance of a
classifier.
Right? Because the variance of the
ensemble has an inverse term in in in in
in the number of
hypotheses that are used. The more they
are, the lesser the variance is.
You see that?
Okay? So, this is one thing. So, one is
increase the number of hypothesis
functions that we are looking at. Of
course, we can do that.
There is another term here, right?
Which is
rho times sigma squared. So, what do we
do about it? So, what is this?
So, here,
huh?
Correlations between
the individual hypotheses.
Now, if we increase B, okay, then this
will also increase. So, if we have to
reduce the overall variance, what we
need to do is of course increase B by
increasing the number of hypotheses and
also try to reduce this
covari- variance between
rather, the correlation between the
individual classifiers.
Now, how do we ensure that we reduce the
correlation between individual
classifiers is the question. Okay? So,
let's write that.
Uh to reduce
variance of Z bar,
one,
increase
B.
And two,
reduce rho.
How do we do this?
Ensure
that
individual
hypotheses are
uncorrelated.
Again, there are multiple ways to do it.
So, one of the ways, which is uh
incorporated in this class of algorithm
called random forest is as follows.
Now, random forest is a
bagged tree algorithm where individual
hypotheses are
decision trees.
Now, when you're taking Remember what we
studied in the last class, right? When
How do we How do we split a decision
tree?
At every node, we consider
all feature all data dimensions and look
at all possible values and compute
whatever the metric is in terms of Gini
impurity or anything and then split.
Now, how do How do we ensure that when
we are building
uh these sorts of trees, the individual
trees the predictions of individual
trees are uncorrelated?
One way to do this is
that when you're deciding
what dimensions of the data are to be
chosen as candidates
for deciding the split, okay? You do a
random sampling at every node.
Do you understand?
And this random sampling is over the
indices of data dimensions.
Suppose there are 100 data dimensions,
okay? So, you build tree one for the
ensemble. When you're building tree one
at node one, okay? You do uniform
sampling between
1 and 100. You take 20 dimensions.
Okay? And you take only those 20
dimensions
while you're deciding the first node of
the first decision tree.
Okay? Then you come to the the second
node.
You do another random sampling over
those 100 dimensions and you take 20 of
them. And you build the first tree like
this.
Then go to the second tree and do the
same thing and you come you
uh
build B of those trees and then cons-
construct an ensemble. This is random
forest.
Do you understand? Why do we do this? By
doing this, we hope that since every
node
of the tree
the individual trees are sampled uh
in a random manner,
the correlated nature between these two
decisions are
lesser. So, they you hope that the rho
here will be reduced if you do this.
Did you get the random forest algorithm?
So, random forest is a bagged tree
ensemble,
okay?
Where while you build the individual
trees, you build it in such a way that
for every individual tree, while you're
deciding the split,
you choose a subset randomly chosen
subset of data for
uh consideration while you're splitting.
So, you can use any of the indices. You
can use the entropy index or you can use
the Gini index for splitting. Doesn't
matter. Whatever index you're using, the
candidate dimensions of data is randomly
chosen at every node of every
constituent tree in a in an ensemble. If
you do that, this algorithm is called
random forest.
All right?
Okay. So, hypotheses are correlated.
Maybe I should write it. So, one example
is random forest.
This is
an ensemble of decision trees.
A randomly sampled subset of data
of data dimensions
are chosen
at
each node of every individual tree
to reduce rho.
Correlation between them.
Now,
what is a What What could be an
additional hyperparameter here?
Mhm?
Number of dimensions that you would
choose at every node. So, that is
typically taken as a hyperparameter when
you're building the random forest.
So, doctor, dimensions are chosen with
or without replacement?
Dimensions are chosen without
replacement.
Yeah.
Any questions here before we move to the
boosting algorithms?
Okay. So, let's move on to
boosting now.
In the bagging case, what did we do is
that we created multiple data sets,
okay? And we
trained several hypotheses on each of
these data sets and took an aggregate.
The question is, can't we do it in a
more principled way? In the sense that
can't we do it in an iterative way where
we search over
the possible space of hypothesis and at
every time So, when we are
See, at the end of the day, what are we
doing in ensembles? You take a new data
set and you train a classifier. Here, we
are training a classifier just by doing
an ERM, okay? Now, the question is, when
we are training a new classifier,
is there a principled way that we add it
back to the the previous classifier so
that we get better performance is the
question that we are asking here. In
other words,
can we cast it as an iterative gradient
algorithm or gradient descent algorithm
or an optimization algorithm on the
hypothesis space is the question.
That's what boosting boosting does.
Okay, so let let me let me write the
math.
Got it, right? In bagging we just take a
data set and we train a classifier on
top of it. So, now can we make it more
principled by casting it as an
optimization problem over the function
spaces?
Is the question that is asked in bagging
sorry boosting. Let us define what
boosting is.
So, now let uh
Now, here uh the ensemble
is built
iteratively
as follows.
Incrementally actually iteratively in an
incremental manner.
Let
h m of x
denote
the classifier
or the weak learner
learned at
m-th iteration.
We get capital B number of data sets,
right? So, look at each of the data set
as an iteration.
You get one data set
train a hypothesis you get the second
data set train a hypothesis and so on.
So, you get
uh
you can look into them as m iterations.
So, let h m x denote the hypothesis at
the m-th iteration.
Now,
define f or sorry h f h m of x
as
Hold on. So, I think I'll have to use a
different notation now.
Okay, capital h m of x is the ensemble
that we are the the next iterate
ensemble that I'm getting
as
h m minus one of x
plus
alpha m times
h m of x where
So, h m of capital h m of x is the
incremental ensemble
obtained at
m-th iteration.
See, please note this equation, right?
All we are saying is that at each
iteration we are building a classifier h
m, okay? And scaling it with some alpha
and adding them.
This is nothing but the
bagging strategy, right? But except for
the fact that there is a scaling factor
here.
See, if we do alpha if we take alpha to
be one, then it becomes simply exactly
the bagging, right? Where you simply add
the individual hypothesis. Here you
scale it with an alpha m. In fact, some
algorithms for instance AdaBoost will
solve an optimization problem over alpha
m as well. So, what should be the
e weight that is that has to be given to
each of the individual classifiers.
We'll come to that in a while. But do
you see that this is nothing but an
ensemble where we are learning a
hypothesis at each iteration.
Every iteration is a data set, right?
You learn a hypothesis on an iteration
and add it to the the previous uh
whatever we have till that particular
point.
Does it make sense?
This is the key equation for boosting,
right? So, the next we will see how to
get this optimal h m and optimal alpha
m. But you'll have to understand this
particular equation. Is this all right?
Yeah, but so we are taking B
classifiers.
Same thing. Yeah, yeah. You have but you
look at every data set as an iteration.
You do it iteratively.
Right? So, you don't train each of them
and then just add them. Here you take
uh you take the first data set train a
hypothesis add it to the previously
existed ensemble and take next one and
add it to it and so on. That this is
what the this equation is saying. Right?
For you do this for
m equal to
one to B.
Sir,
alpha can vary for It will vary. Yes.
That's why there is an index here. It's
alpha m.
Okay? So, what is the amount of weight
that you should give for the m-th
classifier is something that we will we
can control and some algorithms actually
learn it explicitly. Yeah? Okay. Now,
uh
the question is question in boosting
given
h m
No, given
h m minus one x
how to train
h m of x so that
the loss is reduced.
We have an ensemble till m minus first
step. How do we now train the m-th
classifier so that the mistakes that are
done by m minus one have been
uh corrected. So, that's the question
that we'll be asking. So, we will see a
principled way of doing it
which is called the gradient boosting
mechanism.
Uh we will stop here and continue in the
next lecture.
