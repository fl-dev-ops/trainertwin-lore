---
id: b2ScFHIhnB0
title: Lec 54 Decision Trees and Impurity Measures
url: https://www.youtube.com/watch?v=b2ScFHIhnB0
date: '2026-03-25'
duration: 40:23
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

speaker_1: Welcome to this
lecture
In this lecture we will transition from
neural networks
and also the parametric class of
algorithms that we were looking at so
far to
class of non parametric algorithms
Weve already seen examples for
non parametric algorithms right The
nearest neighbor is one non parametric
algorithm where
you dont start by assuming a
functional form for the hypothesis and
estimate the parameters
However
in a non parametric way without
assuming a parameter for the hypothesis
function you solve the problem of
classification or regression is the idea
behind non parametric models
So far in neural networks for instance
uh the the idea is to express the
hypothesis function using a parametric
set which we denoted as H theta and
estimate the theta by
minimizing the KL divergence or
empirical risk minimization
In non parametric models we dont
explicitly define the model using
parameters but we implicitly learn the
decision boundary itself
Okay Through ERM So thats the idea
So
one famous example or often used example
for a non parametric model is what is
called as classification and regression
trees or also known as decision trees
So we will look at decision trees uh
the naive decision trees for
classification and regression
And then we will
discuss about the problems associated
with the decision trees You know it
often tends to be a a classifier that
has uh
very high variance So we look at ways
to reduce the variance of these decision
trees
A classifier or a hypothesis function
that has very high variance
uh is equivalent to
overfitting the data So decision trees
the naive decision trees tends to
overfit the data So then we have to
look at the ways to either increase the
bias or reduce the variance
One of the ways to reduce the variance
of any classifier in general is
by using this algorithm or technique
called bagging
Okay Where also known as ensembles
Where you
instead of training one hypothesis you
train multiple hypotheses on the same
set same data uh via a sampling
procedure and aggregate them
And we will see uh mathematically why
this sort of an aggregation leads to
reduction in variance Okay So
combining decision trees with bagging uh
will give us uh
multiple algorithms that are used in
practice One of the very famous
algorithms is what is known as random
forest Okay We will look at what
random forest is
And there is
another set of algorithm you know
which is again bagging but instead of
you know we do sampling in a slightly
different way These kinds of algorithms
are called boosting algorithms We will
look at two specific boosting
algorithms One is the XGBoost uh or
gradient boosting algorithm the
gradient boosted trees so to speak The
other class of algorithm that we will
look at is what is called as AdaBoost
Okay
And we Ill show that all of these are
empirical risk minimization with a
particular loss function and a sort of a
sort of a regularizer So that story
still remains So that is how we will
move on right now
Okay So now lets start with the naive
decision trees
Now
So let us consider what happens when we
build a classifier before we go on So
when we build a classifier
so what actually happens is that the
space in which the data lies So lets
say that X our data is in R2 for
ease of understanding
When you build a hypothesis function
okay What happens is that the
space in which the data lies
gets split into regions
For instance if we are looking at
linear discriminant functions okay
Then what does the classifier do
finally It splits the the ambient space
or the data space into two
non overlapping regions isnt it So if
the data falls in one particular region
then
its designed as defined as one class
and if it falls in some other
the other half or the other part of the
data space it is defined as another
class Isnt it
Now even if its a lets say see
there is no reason why your hypothesis
should split the space into contiguous
regions So it can be even discontinuous
regions as well
Specifically if you have a K class
classification problem it actually
happens that way
So remember in your assignment I talked
about you know one versus rest of
approach right Where you solve a K
class classification problem by solving
multiple binary classification problems
right Where every binary classifier
would answer this question whether the
sample belongs to the Kth class or not
Combine
uh multiple of these classifiers you
get a K K class classification problem
Even otherwise when you solve a
multi class classification problem
lets say using a neural network whats
actually happening is if you have K
classes the data ambient space gets
partitioned into
K different regions
During inference a data point falls
into one of these K regions Depending
upon where this data point is falling
we define you know we assign that
particular data point during inference
that particular class
Do you see this happening
So every classification algorithm okay
geometrically is partitioning the data
space into
multiple regions
Do you see this So this is actually the
foundational idea behind decision trees
So now what we do is we explicitly
partition the data space into several
regions
Okay And this is what a tree does You
know think about it What is a tree
When Im Im Im assuming that all of
you know this idea of growing a tree
Okay So what happens is suppose I start
asking questions like
uh lets say that I have data which is
in uh
one dimension or other yeah one
dimension for understanding sake So
what Ill do is Ill start asking
questions like whether a given data
point is above the threshold or below
the threshold
If its above some threshold
Ill go to one uh branch in the in the
in the tree given a node or Ill if
its below the threshold I go to the
other branch And at the second node I
ask the same question whether this thing
is greater than or less than another
threshold or so on So what am I doing
at every every node okay
Im drawing a line which is parallel to
the axis because every
threshold that I put on a scalar feature
is equivalent to drawing a line that is
parallel to the axis isnt it
So X equal to tau is a line that is
parallel to the coordinate axis So at
every every level or every node I ask a
question whether this particular
data point
takes a value that is greater than a
threshold or less than a threshold And
if I do it hierarchically in a
tree based fashion what am I doing is
explicitly dividing
the data space into multiple regions
Do you see this
Do you understand what Im saying Now
suppose we have data of lets say D
dimensions
When I grow the tree at every node
okay
I take one dimension of the data
and ask a question
on its threshold whether this
particular
feature is greater than this threshold
or less than this threshold So now if I
have several nodes okay So so every
node in a tree in the naive decision
tree
asks a question
on one dimension of data
Does it make sense
So I have a tree okay It may not be
binary
Okay
And this tree has several nodes And at
every node the question that Im asking
is I take one
dimension of data and
I compare that dimension of data with a
threshold or a fixed threshold
If that is greater than threshold I
move to the left If its less than the
threshold I move to the right
This is done for every dimension
 This is done for every dimension of data
at every level in the naive formulation
Okay This is how we construct a tree
So now there are questions There are
lots of questions to be asked Now how
do you choose what threshold to be
taken So that is what we learn See
when we train a tree what we learn is
what threshold has to be chosen okay
Uh at a particular node And how many
nodes have to be there How how how how
deep the tree should be and so on
Once suppose you have this sort of a
tree constructed during inference what
do you do Given a data point okay You
traverse this tree
entirely and leaf nodes
should correspond to classes
But what typically happens is I mean
lets say for assumption I mean for
for discussion sake even leaf nodes
correspond to a region
See what I actually want you to
understand and appreciate before we go
to the math is that when you construct a
tree every node is splitting the data
space into a region So every node
corresponds to a region is what is to be
understood
Okay And what region a particular node
corresponds to depends upon what
questions it asks at that particular
node and also its predecessors
Because after having asked multiple
questions you come to that particular
node So therefore every node has to be
seen as a partition of data
Is this clear This is actually the most
important thing in growing the tree
Everything else is mathematical details
So every node in a tree
corresponds to a partition of data space
into regions
So finally how do you decide the class
is that at the leaf node okay
When a data point
If If a data point has traversed the
tree and ended up at a particular leaf
node it actually means that this data
point belongs to a region that is
defined by
the leaf node that particular leaf
node
Decide the class of the data point by
looking at the majority voting of all
the data points that are training points
that are already there in that
particular region Thats how you do it
You see that
Right In fact its like softmax
At the leaf node where a data point ends
up okay Lets say that there are
three points from class A or class one
and seven points from class B then this
particular test point will be classified
as
uh class two with 70 percent probability
class
one with 30 percent probability
Just like softmax
Okay Now the question This is what you
do during inference Now the question
is how do you construct the tree given a
training data
What are the parameters that we have in
constructing the tree
The thresholds So how do we choose the
threshold
uh such that uh this makes sense So
that is what we will look at The number
of nodes
Number of nodes is typically a
hyperparameter Its not the parameter
So parameters are these thresholds
It is all right Any questions so far
Because Yeah
one particularly important point that I
want you to understand is that
every node in a tree
is a region in the data space
The number of leaf nodes should be the
number of regions or classes Not
necessarily
Because as I said right
Once the data point travels through
traverses through the entire tree when
it comes to the leaf node
see what proportion of the training
points in that particular region belong
to a particular class
And then assign this this test point
uh
that class that corresponds to the
majority vote within that region Thats
it
Yeah Is this idea clear of how a
decision tree works
Any questions on this
Now lets look at the math
Uh decision trees

 So these are
non parametric methods
The core idea
is to split
the data space into regions
By a
binary questions mostly
Binary questions on
feature dimensions
or
data dimensions lets say
Right

 Now okay So mathematically suppose
So we have the data set D
our points
still have their IID drawn from
PXY
We have X in RD
And for now lets say that we are
looking at classification problems
Well discuss about the regression
problems in a while So we have
classification problems
So at any node
at any given node M
which represents
a region RM
what is a region Region is a subset of
the ambient space
Right Every region is a subset of the
entire data space uh
RM
So containing
NM samples
So every region contains a certain
number of training samples right Lets
denote that by MN So a node is a
region
and that has a certain number of
training samples within it The moment
you define a subset in RD it will have
some samples from the data set D right
NM samples from D that is explicit

 Uh
the
tree algorithm
asks a binary question
as follows
Suppose
XJ
denote
the Jth
dimension
of X
Okay
And
T be a scalar threshold
The question is

 if
XJ is
less than or equal to T
go left
I mean not question Well see this as
an algorithm of split
XJ is greater than T
go right
Thats it
Okay So at every node the question
that Im asking is the split
is defined this way That if Jth
dimension of data is greater than a
particular threshold take one branch
If its less than it take the other
branch Okay

 So please note that this is a This is a
discrete space
So we cannot use gradient decent kind
of algorithms that has derivatives to
get the split Okay So well have to
adopt a greedy algorithm
The
The exhaustive way to do it is
to take at every node consider all data
dimensions and all particular
thresholds
Okay And choose the one that optimizes
whatever the objective that we look at
right now
But thats not possible right
Thats exponentially prohibitive Thats
an NP complete problem which cannot be
solved Thats why decision trees are
greedy algorithms
And there is no optimality It is which
is guaranteed because of this particular
reason
They are greedy optimizations
So what do you mean by greedy You take
a decision and never go back
without thinking about optimality
right At every step you take a
decision greedily
Okay
So do you all see that its its
actually an NP complete problem that is
exponentially large
Because even if you assume threshold to
be discrete
okay Then you will have to evaluate
all possible thresholds at all nodes at
all depths of the
the tree for all features
which is not possible So well have to
do a
uh youll have to take the decision in a
greedy way
Okay
Now
at every node the
optimization objective for split

 So at every node
search over
every feature
every data dimension
and threshold
which is represented a pair J T Right
J is the index of the data dimension and
T is the threshold that maximizes
or that minimizes
the node impurity
Thats the idea So what what what what
are the choices that we have Well have
to choose a pair of data dimension and
the threshold Choose that pair of data
dimension and the threshold that would
minimize the impurity of a node or
impurity of a split
What do you mean by impurity of a split
Its pretty simple
Uh
lets try to understand this So when
do you call okay a split meaningful
Is the question
Okay Now
remember that every node or every split
uh is partitioning the data So what
data partition is called a good
partition
A good data partition is the one okay
that has all data all samples
corresponding to one particular class
Isnt it Why
Why is that a good partition Because
remember that finally what do we have to
do Any classifier would have to
partition the data space in such a way
that one space always contains one
samples from one particular class the
other space contains samples from the
other class
Thats what separability is all about
right So when you define a subset of
region
uh subset of data as a region and you
define goodness or purity of that
region a metric a good metric is the
one or rather a good split is one a good
region is one which contains samples
from only one class
Right
Probabilistically what does this mean
This means that the distribution of one
particular class
has to be
direct delta
It should be as far from a uniform
distribution as as possible
If the distribution of classes
okay Uh
within a particular region is uniform
then its a
impure region
Why Because you know if you leave if
you uh
end up being on in that particular
region which has a uniform distribution
over all classes
then its not a good region because
youre not giving any more information
isnt it All the classes are present in
the same region All the classes are
equally represented in that region
So you dont want to end up in such a
region So a good region is one where
the the distribution over classes of
those samples within that region is as
far away from
uniform distribution as possible
Okay Now how do you define a farness
or closeness from a distribution
Kullback Leibler divergence right So
you have to compute the Kullback Leibler
divergence between the distribution of
classes within a region and the uniform
distribution over those discrete
samples
And
you know fun fact is the
Kullback Leibler divergence between a
given distribution and the uniform
distribution is entropy
Right Because just just do this I
mean I take it as an exercise Show
that
if you take a distribution and
compute its Kullback Leibler divergence
between a uniform distribution over the
same sample space you will end up
getting entropy
So in other words what are we what are
we saying Is minimize the entropy of a
particular region
Entropy of the distribution of data
within a particular region
Okay So lets look at So basically
let me you have to minimize the
impurity
Um
Let
some I of R
be the impurity function
So the cost associated with a
particular split or a node J T is
impurity associated with
the region
of the left node
plus
impurity associated with the region of
the
right node where
NL and NR are
number of
samples
that traverse
the
left and right regions
RL and RR
respectively
So L which is the
metric that we are trying to minimize is
the
weighted impurity
right Associated with
the regions that we get after a split
So when we when we split we get two
regions right RL and RR
Okay
Now
compute the impurity associated with RL
compute the impurity associated with RR
okay Weight it with the number of
samples that both of the nodes get with
respect to the total number of samples
that are there in the particular node
and minimize that metric Thats it
Does it make sense
So this is the the abstract algorithm
of how a decision tree is grown Okay
now we still have to decide what I to be
chosen So one I already told you
right The entropy is one There is
there are other metrics also Well look
at two of them One the entropy the
other is what is called as Gini
impurity We will look at both of those
metrics But the basic idea is the
following right When you split youll
have to split in such a way that the
impurity function associated with the
weighted impurity function associated
with that particular
split has to be minimized
Makes sense
Okay Any questions here
What is L
Yeah this is the function that we are
trying to optimize for So when we
split well see what we do
algorithmically is that
uh at a given depth and a node when we
have to define a node we will compute
this for all possible J and T
Okay And choose one
that would minimize this
Okay So what do you mean by choosing
one What we actually choose is a J and
a T right Every node is a pair of J
and T Thats what I want you to
understand
You choose a data dimension and you
choose a threshold
And the questions are always this X J
is greater than T or less than T Thats
it Now how do you choose a particular
dimension and a pair of dimension and
the threshold is by minimizing this this
loss okay Which is the
the weighted uh impurity function
Split across two uh
two particular regions
Is all right
Okay
Right So now let us look at choices
for the impurity function
See as a side note uh most of the
recommendation algorithms and uh the
uh
the classification algorithms that are
used in the industry at very large scale
are based out of random forest and
decision trees
Okay Uh in fact so much so that uh
when we were students there used to be
these global competitions on some data
sets
And people used to explicitly uh ban the
usage of random forest and decision
trees as as a as an entry
for the competition because one
bagging can be shown theoretically to uh
increase or sorry boosting can be shown
theoretically to increase the accuracy
of a classifier
Ensembles are known to increase the
accuracy of a classifier So ensembles
were banned And the when you Ensembles
are combined combination of multiple
classifiers Individual classifiers for
decision trees because of the ease of
their their their implementation
Okay So theyre theyre that powerful
Okay so lets look at example impurity
functions
Uh
The first thing uh that is often used in
trees that are called ID3 C4 point 5
and so on These are names of algorithms
are entropy
information gain
Now suppose
PK is the
the proportion
of training samples
from
class K
in
region RM
What is PK The number of
samples from class K divided by the
total number of samples in
in region RM
By the way what is this PK
If you recall the earlier classes this
is the ML estimate of that probability
The maximum likelihood estimate okay
for a discrete random variable is the
proportion of the number of samples from
class K isnt it
Right So if PK is the uh is is that uh
ML estimate
So we define the entropy of a node
H of RM simply as
the
How many classes were there K
Capital K number of classes so PK
log
PK
This is log to base two of course
right This is the usual definition of
entropy This is how you define the
entropy of a particular node
What is this This is the KL divergence
between this and the uniform
distribution
Okay
Now um
if its zero then that node is
perfectly pure
If its maximum then that node is
perfectly impure Right And everything
in between okay
Um
So now when
a node is split
what do you want the impurity uh
to happen The what do you want the
impurity to behave like
The impurity
has to decrease
When you traverse through the tree
okay or when you split a particular
node the impurity has to decrease
right
Uh so now how do we measure that
Uh the metric I uh corresponding to a
particular split okay the impurity
metric is
the entropy associated with the parent
minus
the sum of weighted entropy
So this is
one impurity metric that is used in
practice
Huh this one right This is RR yeah
We have defined what RR is Its the
region that we get
after we split to the right
Okay
Now
choose a split
that
maximizes
this
Its the reason I said maximizing is
that we need to put a minus here right
So or minimize the minus of it we can
say
Doesnt matter so this is
minimize the negative of this
Because see this I
what is this Is it the difference
between the entropy associated with the
parent and the weighted entropy of the
children We want this to be
maximized Cuz once we split the this
difference has to be maximized so
negative of the difference has to be
minimized Thats it
Okay
This is one uh measure that is used to
construct the or split the nodes There
is another
uh
metric okay that is called Gini
impurity
This is used uh because the entropy has
a logarithm term in it right So
compute it computing it its a little
computationally expensive So if you
can get rid of the logarithm term
somehow and still get the similar
effect
okay its better So thats why people
sort of moved out of uh
uh entropy and looked at a different
metric
So lets look at uh what Gini impurity
is
You just mentioned that the impurity
should decrease
Uh impurity should decrease Negative of
this is impurity you know
If you look at this metric
difference between the entropy of the
parent and the entropy of the children
okay is the inverse of impurity This
is purity
This has to increase
Right So okay let me not use IE then
right So then maybe we can use this as
still use that this as I cap
This is sort of inverse of impurity
correct

 So this measures Gini impurity measures
the
the probability
of
incorrectly classifying
classifying a randomly chosen point
if it were
randomly labeled
So suppose you sample so theres a
region okay
Uh you take uh you sample a particular
point from that region okay And
incorrectly label it
Thats impurity
Right So the odds of incorrectly
labeling a particular point in a region
has to be minimized isnt it
And when would that be minimized If the
region is pure Suppose you have uh in a
region all points corresponding to one
particular class then when you sample
it and
label it as
I mean sampling it and labeling it as
incorrectly is lesser because
all the points
belong to one particular class in a
node
So this measure uh is looking at the
odds of incorrectly
labeling a particular point that is
sampled from a particular region
Okay How do we get this probability in
terms of uh PK that we have written
What is the probability of choosing a
particular uh
choosing a point belonging to a
particular class
So probability of choosing
a data point
from class P or class K
is
PK
And the probability of incorrectly
labeling it is
1 minus PK
Right So the probability
of incorrectly labeling
is 1 minus PK
These are independent events
Right So
the Gini impurity associated with a
particular region is
you have to sum this up across all
possible classes
Thats it
We want to split in such a way that this
is minimized So we want to minimize
the Gini impurity right I mean the
the probability of
incorrectly classifying a particular
point through random sampling has to be
minimized And this will happen if the
node is pure
See can you see this I mean it can
already be seen right If PK is Dirac
delta this will be maximized
If there is a point okay if if all the
points within a region belongs to a
particular class then this will be
smaller
The more the skewed the distribution is
toward the toward one particular class
the smaller this will be right
Its algebraically it can be seen Can
All of you see that
The degenerative case is when this PK
becomes Dirac delta Thats when its
the most purest the uh the split is the
purest

 Okay So now what should we do We
should choose the
choose the split
J comma T
that minimizes
the Gini impurity
Now if you uh use standard libraries
such as scikit learn they use Gini
impurity because uh computationally its
much uh simpler In fact what can be
shown mathematically is that uh
if you take the greedy way okay uh
both entropy and Gini impurity based
splitting methods will lead to the exact
same split
This is what can be shown
But because of computational ease uh
most of the algorithms
implement Gini impurity over
the entropy uh
based split

 Okay Any questions here
Okay So so far we looked at uh
decision trees for classification What
do we do for regression
Uh we will stop here and continue in the
next lecture
