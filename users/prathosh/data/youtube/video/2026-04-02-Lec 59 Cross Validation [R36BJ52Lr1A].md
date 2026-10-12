---
id: R36BJ52Lr1A
title: Lec 59 Cross Validation
url: https://www.youtube.com/watch?v=R36BJ52Lr1A
date: '2026-04-02'
duration: 12:26
model: youtube-captions (en-orig)
transcript: true
---

# Lec 59 Cross Validation

## Transcript

Welcome everyone to this course.
So now since we have written the
summations
WIC
with respect to W and epsilon M, right?
So
this will become
capital W times e power minus alpha
into 1 minus epsilon M
plus
e power alpha times epsilon M.
Okay?
What we need let's This is
L. So now we'll have to
find an alpha star
such that
uh this L is minimized with respect to
alpha. Therefore, consider the
derivative of this with respect to alpha
and put it to zero.
Uh if you
do the algebra, I'll skip it. So you'll
get alpha star
to be equal to
half log
1 minus epsilon M divided by epsilon M.
Is exactly what AdaBoost says, no?
Please do this, right? I mean just
simply skip the algebra. Just do that. I
mean just rearrange derive take the
derivative and rearrange the terms and
you'll get it.
So that's it. So we completed the
AdaBoost algorithm.
So now what did we say? Let me just run
through the algorithm again.
So start initialize uniformly, right?
And then you get the current classifier
that would minimize uh the
weighted sum of misclassified samples.
Define this epsilon M and estimate the
optimal algorithmic step size alpha M
and update the new weight using this
equation. That's it.
This is
nothing but gradient boosting. Okay?
With
exponential loss function. Okay? And
optimizing over the alphas as well.
Okay, that's why gradient boosting is a
very generalized way of looking at
things. So, AdaBoost is In fact,
AdaBoost is one of the most powerful
algorithms
that are out there. So, you can even
today a lot of the industry grade
classifiers use AdaBoost because we saw
that ensembles always
decrease the variance.
Right?
In turn, decreasing the error. So, you
have multiple It's very cheap to learn
weak learners.
You don't have to do a lot of
hyperparameter tuning also. You just
have to ensure that your learners are
better than chance. And then boost it
using this. It's very easy to
run a boosting algorithm. In fact, you
can see I'll I'll give that as an
assignment. So, now
uh there is You've set the data set on
which you're solving a classification
task or a regression task.
Now,
take one learner and try to do an
optimization by hyperparameter tuning
and parameter tuning. You get some
number, right?
Instead of that, use some hundreds of
learners. All of them are weak learners.
You don't have to do any hyperparameter
tuning.
Chances are that this ensemble will beat
the optimized individual learner.
Okay?
Right. So, this is about uh
boosting.
Since we are talking about bagging and
boosting, I'll also talk about uh
uh
an evaluation technique that is often
used in literature, which is called
cross-validation.
What happens in practice is, let's say
that you are given some data set like
this, right? So, which has n samples
here.
So, typically, what do we do? Uh we
split this as train,
validation, and test.
Correct? And we train our algorithm on
training data set. In fact, this is not
to scale. Let me just change it the way
it is done.
So, typically this is how it is done.
If you have 100 as your training data,
like you split it as 70 20 10.
Okay? Or, you know, 60 30 10 or 60 20
20. The training data always is much
larger, orders of magnitude larger than
the validation and training test data.
So, that's how you do it. So, this is
find the parameters of the algorithms
from here.
So, you get the hyper parameters from
here.
And
report accuracy or report metrics on
this.
And we have seen that while you are
building an algorithm, you never look at
test data, right? All the tuning, all
the parameters and hyper parameters are
tuned on
the test training data and the
validation data. Okay? You never look at
the test data.
See, now here what happens is
this
induces a bias
in terms of
uh see, even within a data set, okay?
You are fixing the the the subset of the
data set that's always taken as training
data.
Okay?
No, which is again biased. You are
ultimately when you when you report the
the the final metric performance metric,
you're reporting only on some 10% or 20%
of data, and you don't know how the
algorithm performs on the other
uh subset of data.
That's why typically what is done is uh
you take this uh
technique called cross validation, okay,
where
you rotate between the training and
training, test, and validation split.
What does that mean?
Let's say that we are doing uh this is
called uh k-fold cross validation in the
literature.
It's a five-fold, 10-fold cross
validation, and so on. If it's a
five-fold cross validation, what you do
is that
you do a you do five non-overlapping
80/20 splits of data.
Or 70/30, 70/10/10 splits of data. They
are These are all non-overlapping in the
sense that the that 10% of test data
that you look at is different for every
split.
Okay?
Now, you build your algorithm on those
five different data sets. So, this is
actually sampling. The sampling with
replacement only. But, you are doing not
randomly. You sample with a sample with
replacement in a with a with a
specified pre-specified procedure.
That's it. Okay? Now, you have five
classifiers, or rather five performance
metrics
on five different data sets, five
different test data sets.
Report the final number as an aggregate
over all those five data sets, five test
data sets. So, this is called
cross-validated numbers.
So, typically when people I mean, if you
want to uh evaluate your algorithm for
robustness,
the best practice is to report the
cross-validated numbers,
not do one random split of data.
So, what are you doing like this? By
doing this, you are ensuring that you
are testing the performance of the
algorithm on entire data set. Because if
you're doing five five-fold cross
validation,
then you're splitting data into our data
into five different non-overlapping
sets, right? So, you'll have every 20%
of the data being treated as
test data
in one fold.
Okay? So, that way you aggregate the
performance or rather you will report
the performance across the entire test
data set is the idea. So, this is called
cross validation. It's a good practice
to report your metrics
after cross after cross cross
validation.
Yeah.
Yeah, yeah, you have to train. See, this
is independent of ensembling. If you're
doing an ensemble, you'll have to do an
ensemble on each fold separately.
I I didn't get the question. What's the
question?
Mhm.
Huh. So, the question is when you cross
validate, you will get let's say K
number of classifiers. What should be
your final
classifier? Either you can do an
ensemble on them.
That's one way to do it. Okay? You do
you bag them and do it. Or you get ship
the one that is the best amongst these
five.
Okay?
And anyway, in the field you don't know
how your classifier performs, right? On
the unseen data. So, you have to ship
one. You can ship any one of them. Or
the ensemble of them as well. Okay?
Okay. So,
Not when the model is being trained.
When the one when one particular model
is being trained, it is not seeing the
test data at all. No, this is like
training five different or K different
classifiers
on K different data sets which are which
are sampled from one large bag of data
set that you are given.
You understand? Even now, every
individual classifier is not being
exposed to the test part of it.
Yeah? But if we expose them
the whole thing has been exposed to
That's okay, but that's what I That's
why I told you. Finally, when you ship,
right?
The test data test data that that is
being fed to the final classifier is
anyway unseen to this, isn't it?
So, this is as I said, typically cross
validation is used to measure the
robustness of
a class of algorithms across different
splits of data. So, when when people ask
you to report the metrics, they will not
ask you to report See, what happens is
suppose I give a particular
classification problem on a data set to
two people, and I ask you to report the
performance on on a 70/30 split.
What is that 70% that you choose, and
what is the 70% that the other person
chooses? Is very different.
If I ask you to cross validate,
then I can compare the performances much
better. That's the idea.
Isn't it? Because
no matter what split do you take, if you
do a five-fold cross validation, and if
the other person also does a five-fold
cross validation, then
both of you have seen like all the parts
of data. That's the point. Or rather,
the algorithms have been evaluated on
all parts of data.
Okay?
Yeah.
If you're interested in splitting the
data set into five-fold or six-fold
then each classifier is getting a small
number of points.
Won't that reduce accuracy?
Why is that? Not necessarily, right?
See, if you're doing a 70/30 split or
80/20 split,
I'm saying
every classifier now will will get 80%
of the data as training data, no? The
only thing is which 80% of the training
data classifier would see changes across
different
folds.
>> [snorts]
>> But each individual classifier is
getting like less number of data points.
Why? Everything Everything gets the
exact same number of data points, right?
Cuz there are five different 80/20
splits.
See, anyway you are splitting it for
test. You have
test data. I mean, you are not training
on 100% of data anyway, right? You are
doing it on 80% of data. What 80% gets
different differed? That's it.
Okay?
Okay. So, that's about it. I mean,
that's That's That's all I wanted to
talk about in the realm of
supervised learning, okay? Now, let's go
to the next paradigm in machine
learning, which is called unsupervised
learning.
Uh we will stop here and continue in the
next lecture.
