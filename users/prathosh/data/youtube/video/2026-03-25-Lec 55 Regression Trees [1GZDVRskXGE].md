---
id: 1GZDVRskXGE
title: Lec 55 Regression Trees
url: https://www.youtube.com/watch?v=1GZDVRskXGE
date: '2026-03-25'
duration: 34:09
model: youtube-captions (en-orig)
transcript: true
---

# Lec 55 Regression Trees

## Transcript

Welcome back. So, so far, we looked at
decision trees for classification. What
do we do for regression?
Any ideas?
Regression trees.
Exactly. So, there are two questions
that are to be asked, right? So, how do
you define
the split?
And what is the impurity metric in the
case of regression? That's it. Yeah.
Yeah. Good question. The question is how
do we choose T because T if T are con- T
is a continuous variable, right? If your
features are taking continuous values,
how do we choose T? There are heuristic
ways to do it. I'll come to that in a
while. So, let's look at regression
trees as as as algorithmic technique and
then actually many other questions are
to be asked. One, of course, is how do
we choose T? Two, what is the stopping
criteria?
Right? And what do we do with the
categorical data case?
Right? So, all these questions are to be
asked. We will answer them one after the
other. Okay? So, let's look at
regression trees first. So,
So, if Y is
is continuous,
so, discrete class probability based
metrics can't be used.
Now,
if
a sample
is
falling in region RM,
define
the prediction within the region RM
as
So, YM cap is simply the
average
of all samples that are in RM.
So, now we are solving the problem of
regression, mind you, right? So,
whenever the data is split into a a
region,
there are corresponding labels as well.
Define the prediction corresponding to a
particular region as the average of all
the samples within the average of all
the targets within that region.
Okay?
In fact, the final
regression
in a regression tree is also done the
same way at the leaf nodes.
When you traverse the tree,
so finally for a given point X, you need
to know what the output regression value
is, right? Y. The way to do it is
whatever leaf node that you have
ended up with,
look at the
target values of that region given by
that leaf node,
okay? And take an average of it, and
that becomes the prediction
for the input.
Okay? And by the way, what is the the
final label that is associated that is
associated to a given sample in the
classification case? Already mentioned,
traverse the tree.
Okay? So, look at the
the majority vote of the region in the
leaf node that that that are inference
on test sample ends up in and and
associate the class with that particular
class.
In fact,
as I already mentioned, when you
construct a decision tree, every leaf
node will give you an entire probability
distribution over the
label space.
In fact, every node gives you that. This
PK that we were talking about is
actually a distribution over the entire
label space.
So, when you end end up at the leaf
node, you get an entire distribution
over the leaf I mean the the
the target variable, just like a neural
network gives. You choose
uh in whatever way you want. Typically,
max is chosen.
Just like in the neural network, you
choose the the output of the softmax is
a distribution over labels. You choose
the max as the class, isn't it?
Similarly, whatever node it ends up with
the the test data ends up with
uh
get a distribution over the entire Y and
assign the class as accordingly.
It it I mean, if you have if you have
learned your tree properly, that cannot
be uniform. Because at every split
you're
you're uh maximizing or you're pushing
the distribution away from uniform
distribution by looking at the entropy,
right? If you have split your tree, if
you have
created your tree properly, then
at the leaf node,
you will have a skewed distribution over
samples, yeah?
Okay. So, now this is how you compute
the prediction within each region for
the regression case. Now, using this we
will define an impurity metric.
Yeah.
Here, isn't this what it says in the
sense that any point that gets into a
region gets the same value?
Happens, correct.
That's why you need to uh make your tree
deeper, so that every region will have
less amount of points.
It's the bias-variance problem.
Exactly. So, you you you have two
choices. Either have a deeper tree,
right? Or if you have you have a shallow
tree. If you have a deeper tree, then
you will overfit.
Large variance, less bias. If you have a
shallow tree, it's high bias, less
variance.
Same I mean, this thing appears
everywhere.
So, the question is how do you
regularize in such a way that you trade
the bias and variance is the question.
Okay? So, let's define an impurity
metric here for the regression case.
So, simply measure how far
uh the
once you split, okay? You get a
predicted
uh
What did What did we call it? Prediction
of the region.
So, measure how far the prediction on an
average how far the prediction of that
region is from the actual targets.
Which is the mean squared error.
Okay? So, define the impurity of a
region RM, okay? As
1 over M and M
sum of the difference
between the actual targets
that fall within the region and
what what what average What is the
average prediction that is given by that
region? That's it.
See, it this solves the question that
you exact question that you asked, no?
If it's If it's averaging out a lot,
okay? Then that's a bad split.
You need a split, okay? Uh that would
make the average prediction as close to
the the prediction of all the targets
within that region.
You want to minimize the variance. So,
this is the variance metric. You need to
minimize the variance. This is the
impurity metric that is used.
Okay?
Now, this is about how do you grow
a decision tree given some data.
Okay? Now, there are open questions that
are to be asked. I don't know how do you
choose the threshold when you have
infinite values.
Okay? And how do you regulate the depth
of the tree? And what is the stopping
criteria and so on, which we will look
right now. Okay?
Uh
any questions so far?
Yeah.
For the regression case, is it?
Yeah, it happens. It may happen.
In the degenerative case,
what will happen is
every data point in the training data
will constitute a node.
That can be done, right?
Every data point in your training data
can correspond to a region. So, you
split every data point into a region.
That's it.
Okay? Which is
is the overfitting case. So, now how do
you ensure that these kinds of
degenerate In fact, it happens. You
know, if you grow the tree for long
enough, this may happen. That that every
node maker All that is needed is that,
right? You have those many number of
number of nodes in your data set. Sorry,
in in the decision tree as there are
number of data points. It's It's
basically a lookup table. Exactly. It's
memorizing a lookup table. So, remember
the degenerative memory lookup table
example that I had given during the bias
variance
discussion. That's exactly what happens.
So, we'll have to ensure that that that
way that is that is not the case by
regularizing. Now, how do you regularize
is the question.
Okay? So, before that, let us look at
some of the greedy ways of doing it. So,
now um
How do we choose the node for which the
topology is selected?
Come again. How do we decide the Sorry.
How do we decide the feature?
Ah. The In the naive way, okay? Uh you
take all features.
For you consider all features at all
nodes.
Right? And see,
for a pair of feature and a threshold,
you can compute the impurity metric. So,
over the space of all features and all
thresholds,
define the node that would minimize the
impurity. That's how you do it.
It's large. I mean, you need to uh solve
uh a very large no
optimization problem at every split, I
agree. In the naive way, this is how you
do it, right? Now, let us look at some
questions that are to be asked while
growing decision tree. Any other
question here?
This is equivalent to negative of that I
had.
Exactly. Yeah. The the impurity, right?
The entropy thing that we were looking
at. Okay?
Now, the first thing is uh
how to
choose candidate thresholds.
Yeah, two of those would be ill
somewhere.
For a split.
See, there are multiple ways to do this.
There are multiple heuristics to do
this. I'll just talk about one, okay?
First thing is
um
So, given
a node M
or not given actually, for a node M
cuz we are what we are actually choosing
is a node.
For a node M containing
NM samples
extract
all the
uh NM values for a feature.
For the feature XJ
or data dimension XJ.
So, please note that we are fixing the
data dimension here. The only variable
that we are trying to find out is the
threshold. So, choose a feature
dimension XJ and
extract all values of it. Look at all
values of it.
Okay? And then
sort
the values
remove duplicates
rank order them.
Let's say they are U1, U2, U3
up to UK
where K is always less than or equal to
NM.
Okay, K is overloaded.
UP where P is less than NM. Did you
understand?
Take some feature, look at what what
values what all values it has taken in
the data set, rank order them.
Okay, remove the duplicates. Now, define
threshold TI
for
I is 1 2 P minus 1
as
UI plus UI plus 1 by 2. That's it.
Take two values,
take an average and that becomes a
threshold.
Okay?
Is this all right?
Did you understand what's happening?
See, this algorithm is
O NM squared.
Why?
See, this algorithm of splitting is O NM
squared. Can somebody tell me why?
Okay, anyway. So, think about it. So,
this algorithm, I mean, if you use this
to choose the threshold and then split
using some impurity technique, we will
end up getting
an algorithm, okay, that is quadratic in
the number of samples that we have in
the particular node.
Yeah, you'll have to first uh look rank
order, compute this, and then split. So,
there are two passes that you need to
do.
Uh you can reduce it to
NM log NM.
Yeah, think about it. Okay, it's it's a
it's a nice algorithms question.
Okay, you can do that. Hm?
Uh
This is one way to do it.
The other way to do it is to instead of
looking at all the values and then rank
ordering them and all that.
People look at histograms of these
features.
Okay, and take the edges of the bin as
threshold thresholds for thresholds.
That's it.
That is that is what is done in practice
in most of the
the modern day algorithms. You
understood right? Instead of looking at
all values just threshold and so take a
histogram.
Please note that these are scalar
values, right? So we are talking about
one dimensional histogram and take the
edges of the bins of the histogram as
the candidate threshold values.
Okay.
This is one other question and
yeah. Now we have to look at the
stopping criteria.
Also called pruning.
See, if you let this algorithm run,
it will keep splitting
till a point where every region will
have a single data point.
Right? So we don't want that to happen.
So this is called tree pruning or just
define stopping criteria so that you
define criteria so as to say when do you
stop splitting? Okay. So there are a lot
of ways to do it. We will look at a few
of them. So one is what is called as
the maximum depth.
Simply define
Dmax as a hyper parameter.
as the maximum possible depth.
So, this is a
hyperparameter, okay?
If
D is the depth of the current node
for a given node
so, I'll go stops
if D equal to Dmax.
That's it. So, you define a particular
depth of this tree and say that
the tree should not have depth more than
this.
So, why should this work?
Defining a putting a threshold on uh the
maximum possible depth is equivalent to
bounding this bounding the area of the
region that we are constructing for the
node. It It's creating an upper bound on
the area or rather volume if you're
looking at
a 3D dimensional space, it's equivalent
to restricting the
maximum value
or rather not the maximum value, the
minimum value
of the volume corresponding to the
region that is being constructed. Do you
see why?
If you traverse through the nodes,
right? Uh
every node is splitting the region into
smaller and smaller volumes.
Now, if you restrict the depth of the
tree, okay? You're saying
there's a limit to what the minimum
value of this region has to be. So, that
you don't go beyond it.
So, this is you can already see that
this is a bias, right?
This is one type of regularization that
one can put.
Uh the other thing that can be done is
minimum samples for a split.
So, let NM
be the number of samples in the current
node.
The algorithm will only split
split further
only if
number of samples that I already have is
equal to a number called
Nmin.
So, what I'm saying is that you attempt
a split only if the number of
data samples that we have in the region
is greater than a particular number.
This also has the same effect.
See, remember this is very, very similar
to uh create
uh
fixing the number of samples in a region
and growing the region that encompasses
this in the non-parametric density
estimates.
So, we are saying we will split only if
we have this these many minimum number
of samples within that region after we
split. Otherwise, we are we are not
splitting.
This is one other type of regularizers
that can be done.
An extension of this is
that you can say that you instead of
doing it at every node, right? You say
that you traverse through this this path
only if there are minimum number of
number of samples in the leaf nodes.
Here we are doing at every node, right?
Instead of doing that you can do it in
the in the leaf node and saying that
only if we if this path ends up getting
a leaf node that has minimum number of
samples, then split, otherwise don't
split.
Okay, that is one of the way to do it.
And the other
way that is done is
minimum impurity
decrease.
Split
only if
the impurity associated with the
particular split is greater than
a predefined number epsilon.
Right?
If the split actually gains in the in
the decrease of uh
impurity
by a minimum number, only then you
split, otherwise you don't split. And
how do you choose this Nmin, epsilon
and Dmax, etc.? They are all hyper
parameters.
Okay?
I?
Yeah, how did we define the impurity?
Impurity was I. Impurity was I I cap.
Impurity was? I. I? Yeah. The inverse of
purity was I cap. Yeah. So, this is
correct.
>> Okay, one of the extension to this is
even if you have categorical values for
the features. So now we so far we looked
at
numerical values.
So features can also have categorical
values. In fact, one of the
biggest known advantages of decision
trees is that it can be very easily
extended to the categorical data case.
So what do you mean by categorical data?
Categorical data is when your data is is
is is not in RD, right? Or instead it is
it has some
descriptive categories.
For instance,
your features can be colors. So one of
the
possible colors, you know, red, green,
blue, etc. and then it can be
gender or something, right? So where you
have where there are categories.
By the way, how do you deal with
categorical data in the case of neural
networks and so on?
We do just do one hot representation. In
fact, all the textual data that we get
is categorical that way, right? We have
a dictionary.
That can be done here as well, right?
But if you do one hot representation, it
leads to degenerative cases. Instead of
that,
because we are splitting at every stage,
and here the split, right? Does not
necessitate that uh your
your split has to be based on numerical
values.
If there are K categories at a that a
particular feature can take, the split
can be based on K categories. That's it.
The easiest, right? You compute the
impurity for all those splits and then
keep moving on.
This is called multi-class split. So
yeah, extending this to the case of
categorical data is
straightforward in the sense that you
don't have to change anything, Just have
to split the data into or split that
particular feature into K number of
categories.
Okay?
Uh
so now um
Sir, categories can be viewed as
classes.
No, categories are not classes. See,
categories are different discrete values
that the data dimensions or features
would take.
Classes are something else.
So, when you do measurements, right? All
the dimensions of data or measurements
is what we have been seeing so far.
Right? Now, they're features. We're
talking about data dimensions, not the
classes. Yeah?
Okay. So, one question Yeah.
So,
when we do the thresholding, let's say
if we do just the
we do like number of categories
and we have this at the middle of the
categories, the threshold that we
choose.
But,
in the feature in the continuous feature
space, there is a meaning that if
something is greater than five,
it's greater than five, but in category
space, it's
greater than one.
That's the It is not greater than then,
right? So, the the the questions are
if the feature belongs to this category,
then there is one split. If it's belong
If it belongs to the other category,
it's this split. That's it.
It is not because they are not numerical
values. The questions are not greater
than less than.
The questions are whether the feature
belongs to this category or that
category. That's it. Yeah?
Okay. See, one other critical question
that is to be answered is right now the
way we are doing it is
uh that we are asking We are considering
all data dimensions at all nodes.
Which is prohibitively high, right? I
mean, suppose you are dealing with let's
say 1,000 dimensional data
and you have 10,000 data points, you
know, you'll have to rank order them and
use all 10,000 dimensions and compute
all this. Even even though it can be
done algorithmically, it is expensive.
Now, is there a way to reduce this
computation and somehow See,
answer this question. What happens if we
choose only a subset of data dimensions
at every node or every split?
Yeah, exactly. We may miss on the best
possible questions that can be asked.
In terms of
In terms of our hypothesis, what will
happen to that hypothesis?
So, we may end up getting a hypothesis
that has very high variance.
If we only choose a subset of samples
at every split. And we only consider a
subset of Not samples, I'm sorry. Subset
of features at every every node. Okay?
Now, suppose Now, the question that is
to be natural question that is to be
asked is
Now, this is very cheap to compute
because we are not looking at
exhaustively all possible dimensions of
data.
But, they are not the best of
classifiers.
Now, the question The next question that
we'll be asking is, suppose I give you
a lot of easily learnable weak
classifiers.
They're also called weak learners.
Instead of giving you a strong learner,
if I give you a committee of multiple
weak learners,
can I combine them to
make a good decision?
Do you understand the question? To
decrease the cost.
No, no. To Yeah, to I mean, the final
goodness of the classifier is is in
terms of minimizing the true risk, of
course.
Right? So, in general, forget about
decision trees. In general, suppose I
give you
thousands of easily learnable weak
learners.
Okay? Can I come up with uh a decision
combining a way to combine all of them
such that the overall the combined
decision will be better than individual
decisions.
Right? That's the question that we'll be
asking and it turns out that you can do
that and these sorts of algorithms are
called the bagging algorithms. Okay?
Bagging and boosting algorithms which
you will see. In fact, if you use a
particular type of uh
uh
bagging algorithm with decision trees as
the candidate classifiers, you get into
this uh very famous and powerful
algorithm called random forests.
Combining multiple decision trees gives
rise to a random forest. I'll talk I
mean I'll tell you what random is in
that random forest and you know, it's a
forest because it's a combination of
multiple decision trees, right? So,
we'll talk about bagging in the in the
next session and I'll show you
mathematically why this combining
multiple correlated classifiers. In
fact, the idea is the following. Let me
just tell you the high-level idea. What
is done is as is is as follows. Given a
data set D, we'll do the math in the
next class. So, we know that the true
risk gets split into the bias and
variance term. If you recall what your
variance term is, the variance term is
variance term involves HD of X which is
the
classifier that we designed on the given
data set minus H bar
the square. What is H bar? The average
The average classifier. Now, on a data
set on a particular data set, you train
a classifier HD. If you can get that
close to H bar, then the variance
decreases.
How do you get that H bar? Remember what
the definition of H bar was? It was the
average classifier that you would get by
combining classifiers that are
that are trained on multiple instances
of data set. But do we have multiple
instances of data set? We don't.
But we do have a data set. What we do is
we create multiple instances of data set
by doing the sampling, random sampling
with replacement.
If you do a random sampling of the data
with replacement, the only thing is we
had made an ID assumption across data
sets.
That will be broken.
Which means that every data set will be
correlated with each other. Which means
every classifier that we build on a data
set that we have synthetically created
by doing a random sampling will be
correlated with each other. That will
come up in the math. However, it's the
closest that we can do to uh uh to
getting close to H bar cuz we don't have
multiple data sets.
Now, what we will show is that if you do
a uh uh if you create data sets by
sampling with replacement and create an
aggregated classifier by taking an
average of all of this,
the performance of this aggregated
classifier is better than creating a
classifier on this one data set is what
we will show. And these kinds of
algorithms where we take an aggregation
of multiple classifiers trained on data
sets that we obtain by sampling with
replacement is called bagging.
Okay? Now, in a random forest, what is
done is that while all the individual
classifiers are the hypothesis functions
that we create
are decision trees.
And every decision tree while we are
creating, at every node we only take a
random subset of features and then build
a
random forest.
It is a random decision forest. A random
forest as an algorithm is the bagged
aggregated version of random multiple
random decision trees.
What is random What is random in a in a
random decision tree is that when you
are splitting, you take you randomly
subsample sub sub uh a sample a subset
of
data dimensions that you would
build questions on.
Construct multiple decision trees of
that sort, okay, and then bag them up.
That becomes a random forest. This is
done so that it's not so expensive.
Huh, and we are reducing the variance,
no? See, ultimately we want to reduce
the true risk, and true risk we know is
sum of two terms. Here, we are reducing
the variance explicitly by doing this.
We will show that mathematically in the
next class, right? That we do by do by
doing this, we will reduce the variance
of a classifier. The next the the next
thing is that
there are
uh
more principled algorithms of doing
this, which is called the
uh the the boosting algorithms, okay?
Where we we also decide what sort of
subset of data to be sampled, and that's
why, you know, one of the very uh
powerful algorithm that is known in the
ML community is what is called as
XGBoost. XGBoost is gradient boosted
trees.
We will look at XGBoost uh in the coming
classes.
Okay, so yeah, so we will look at
bagging and random forest the next
class. After that, we will go to
unsupervised learning.
Okay, uh where we look at algorithms
such as component analysis and the
clustering algorithms. And as I said, we
will also look at the self-supervised
learning algorithms, uh
which are the the workhorses behind the
modern-day LLMs.
Maybe one class of the introduction to
generative models,
uh of which there's an entire course
that explains in the in the coming
semester, okay?
Okay, thank you. That's it for today.
