---
id: _YKxmyP5PWU
title: Lec 57 Gradient Boosting Algorithm
url: https://www.youtube.com/watch?v=_YKxmyP5PWU
date: '2026-03-25'
duration: 30:23
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

speaker_1: Welcome back
So we will see a principled way of
doing it which is called the gradient
boosting mechanism
So recall that what we need
that we have
H m of X
to be equal to
H m minus 1 of X plus alpha m times
H m of X Okay
Goal
is to
find
a new learner
H m of X
to minimize
the risk
Lets write that So whats the risk
which is mathematically speaking So we
have I
from 1 through n
We have some
uh L the corresponding loss function
y i comma
We need to minimize the loss of H m of X
at the m stage And the optimization
is over
H and alpha
We need to find an alpha and an H such
that
the risk of H m So please note that
all of these H are
hypothesis functions right
So we need to minimize this
Is it all right Mathematically this is
what we need to do at every step At
every iteration well have to ensure
that this will happen
Please uh understand the objective
properly because you know the rest is
all algebra but is this all right
Yeah
This equation is that in between the
training iterations or
each hypothesis after training complete
Like the iteration means Oh no this is
like Yeah this is You have capital B
number of data sets right So on every
data set you train a hypothesis Thats
the iteration that Im talking about
Yeah
Oh its not the iteration within a
particular training So its it You are
Youre iterating over multiple data sets
now Correct Yeah
Okay Now
um
Well have to write this as consider
L
of H m So what is this
This is equal to
Lets slightly abuse the math a little
and now consider
functions as variables and take
derivatives
Its not the exact way to do it Youll
have to write the Euler Lagrange
equations but
Ill
take that leap and do that So this is
Yeah what is this equal to This is
equal to
uh L that we are
computing at y i
 comma What is H m H m is
This is over m H m minus 1 times X plus
No no theres no sum here right
Yeah
My bad
This is H m minus m minus 1 X plus
alpha m H m Correct
Yeah
Theres also an I here
Cuz were doing it for one particular
data point and we sum it over all of
them right
Now
consider this term y i
 comma H m minus 1
x i
plus alpha m
H m
This is equal to
L
that is evaluated at
 comma
H m minus 1
x i
plus
the derivative of the loss
with respect to
H
times
and this is evaluated at
H minus 1
times alpha
H
What did I do
What is this
First order Taylor series I just
expanded this this term
using Taylor series up to
the first derivative terms Thats it
And
What have I expanded it around Ive
expanded it around H m minus 1
So the above is
I have treated this as a function of H
and expanded it using Taylor series
around H equal to H minus 1
Is all right So where did I make that
uh algebraic mistake So this
H is a function
Im treating that as a variable and
taking the derivative right So thats
the
mathematical incorrectness but yeah
okay Now
uh
Let this entire derivative term right
be
written as some g i
Okay If I do that then
my LHS is equal to
L y i comma
H m minus 1
x i This is the first term
Plus
alpha times
g i into h i
No h of x i sorry
Do you see why there is an index i here
for the gradient
Its because youre we are evaluating
that on the sample x i So well have
to sum it over all samples You know
thats why we have this So this is
what we have as the LHS and we want to
minimize
the sum of this
Our objective now again our
optimization problem is argmin
We have to optimize over alpha and H the
sum of this particular term
L
y i comma H m minus 1 x i
plus
alpha times g i
h of x i
Yeah this is what we want to do
Any questions so far
Okay So here the first term this
term right is independent of the
optimization variable
Because
this is the loss that we are computing
on the ensemble that we have obtained
till H m minus 1 iteration We already
know what this is Cuz were standing at
m iteration
Is all right So this
optimization now is
equivalent to minimizing
over
Does it make sense
So this is the key equation of gradient
boosting gradient boosted models
Why are they called gradient boosted
Cuz the boosting or the aggregation is
happening through the gradient
computation over the function space
We still Ive still not told you how to
solve this optimization problem right
Do we know how to compute g i by the
way
Do we know how to do compute that We
do
Because this gradient is being evaluated
at H equal to H H H m minus 1 We know
how to do this
So we know how the what the loss
function is If you take the loss
function and take a derivative with
respect to the hypothesis class then
this gradient function becomes a
function of y i and x i
And if we are doing it at H m minus 1
we know what the hypothesis is So the
entire gradient term is
evaluated This can be evaluated Well
Ill show you an example Okay So what
is to be done is well have to find what
this H is by solving this particular
optimization problem
Is that okay Any questions here
Okay So let me The next question is
how to minimize
Let me write that maybe
uh g i
evaluated at H equal to H minus 1
can be computed
Therefore now the question is
how to minimize
this particular sum
How to do this So please note that
this product that we want to minimize
now
is nothing but the inner product between
these two vectors
If you look into these two as
n dimensional vectors what we are
computing is nothing but inner product
If you have inner product of two
vectors
okay youll have to find h that would
minimize this How would you do this
Which implies
the argument the minimizer
of
this inner product
over h What is this equal to
Is the h
such that
its just
negative of the gradient
So there are two vectors and we are
looking at inner products
When would the When would the inner
product be minimum
If both of them point to
orthogonal directions right So when
would that happen If you choose your h
to be the negative of gradient at every
point
then you would get the hypothesis that
would minimize the error
Does it make sense
Okay Now
how would we ensure that this would this
this is done algorithmically
Do you see what is happening What is
happening is we have m minus one
classifiers and we want to now find the
the mth classifier And Im saying that
you find the mth classifier in such a
way that it is equal to the value of the
gradient
This particular gradient that we have
computed at every single data point
thats it It has to be equal to the
negative of this particular gradient
that we are taking gradient of the loss
with respect to the hypothesis function
at every point Youll have to just make
your
set your h m of x to be equal to this
Is what gradient boosting is saying So
how do we do this
Now
to find
h star
that is
proportional to
negative of g
g i
define h m to be equal to
the one
that will minimize the
sum error metric You can take mean
squared error for instance
Over the negative gradient
See
finding this h star
now is a regression problem
with the regression labels being equal
to minus g i
Did you understand what Im saying
So please uh
you know uh
give some attention here
Till here we found out that the optimal
h that we we have to find at the mth
iteration is the one
that is proportional to the negative of
gradient or rather this proportionality
can be equality also right Equal to
the negative of the gradient at every
data point
Is this clear Is this statement clear
Ill repeat it If you have questions
ask me because this is very very
important
By looking at Taylor series expansion
we found out that in the uh in the
gradient boosted algorithms
the optimal hypothesis that you need to
be finding at the mth iteration is the
one
that is equal to the value of the
gradient
Okay
At every x
Is what we found out here Is this
statement clear
And what is the g i
G i is
this particular thing which can be
computed
Do you see
All of you clear here Because this is
very important I mean maybe take a
minute and tell me if you understand
this or not
Sir are we taking the taking the
authors and
take for one data point
How does it reflect the entire
hypothesis
No the hypothesis has to be equal to
the gradient at all data points is all
we are saying
How do we do that is the next question
well come
Did you understand the statement and the
math
The math is telling you that youll have
to find your mth hypothesis such that it
is equal to this particular gradient at
all data points is all it is asking for
Is this clear
Cuz this often the you know the point
of confusion when we are looking at the
gradient boosting trees because
note that we are still solving a
classification even if you are solving a
classification problem our h has to be
equal to the negative of gradient at all
data points Thats how it has to be
Because of this math So now how do we
do this is a question which well see in
a while But is the math clear so far
Yeah
Is the loss taken over the sample data
set or the original data set
The loss is taken over The loss here
Uh huh Taken over the sample data set
or the original data set
In
See this loss is being computed on the
data set
which you are using to find the mth
classifier
Which is which can be the sample data
set Which will be the sample data set
Okay
Any other questions
Now the next question
is that how do we ensure that the
classifier is equal to that particular
gradient value at all
possible x is what you asked
Treat Treat that as a regression
problem So now all Im saying is to
find h m
at the mth stage
youll have to solve a regression
problem by keeping negative of gradients
as the labels
Thats it
So therefore
to find h star that is proportional to g
minus g i right Youll have to
solve
a regression problem
with
minus g i as labels
How do you solve What loss function do
you use to solve a regression problem
Thats exactly what Ive written here
Mean squared error
Where
this these are your labels This is y i
minus h i h i h x squared right This
is your regression problem Now the
labels are negative of the gradient
Is that all right
Okay Now the uh
If you If I have to write an algorithm
for
gradient boosting how do I write it
So the final
gradient boosting algorithm
is as follows

 Okay
Now given a data set D
start by
creating
b data sets
You do a sampling
with replacement
Now
for
uh small b
uh m equal to 1 to
b minus 1 do the following
H m of x
is equal to h m minus 1 of x
plus
uh some
alpha times h m of x
So please note in uh in in naive
gradient boosting alpha is a
hyperparameter We dont optimize over
alpha
But in the next set of next algorithm
that we will look at which is AdaBoost
we will optimize over alpha as well and
well find out what the optimal alpha is
as well
Compute
minus
GI
I want two indices
Thats why I I just got stuck So this
is uh
well have to find this gradient for the
mth iteration for ith sample
as
the negative of
H
of XI
divided by
H
XY
evaluated at HM minus one
Often uh in literature right This is
also called as
residual People call this as residual
Yeah
This is called residual okay The
derivative of the loss function with
respect to hypothesis Please note that
this derivative see we were looking at
this derivative with respect to the
parameter so far for gradient descent
standard gradient descent right So
here were looking at the derivative of
this loss function with respect to the
hypothesis itself
Okay
Now uh theres one missing piece that
Ive not told you I I was waiting as for
some of you will ask that question How
do you find this derivative
Right Suppose your loss function is
or rather okay let me tell you See
this loss function is a is a function of
Y and H
Cuz thats how we define the loss
function right So treat that H as a
as a variable and take just take the
derivative thats it
I leave this as a homework Please find
out what would be the form of this
residual for different loss functions
Suppose the loss function is squared
error loss function So what would be
the form of this
Can somebody quickly tell me what would
be the form of this for uh
squared error loss
Itll be
Y minus HX which is actually the
residual right Its the difference
between the true label and the
outputs Thats why the name residual
The negative of the gradient is the
residual If you take the cross entropy
just see what happens and so on right
You compute this and this can be
computed because we have H minus H of HM
minus one and we also know what the loss
function is and that can be evaluated
Compute this And then what should we do
next
So we have to compute this for all
samples
Train
HM of X
by regressing over
GM
negative of GM
Correct Please note that I have uh left
the uh superscript here right The
subscript I here why
Uh because Im doing it for the entire
data set
I have to compute the residual for every
data point
Okay And once you do it for the all
data points at a particular iteration
use that and regress find the next set
of classifier by regressing over GM
Its all right And then
get
HM
of X to be equal to take the previous
one that we already have
Thats it I get the next classifier
You move on
This is the gradient boosted tree
algorithm
Yeah good question How do we
initialize it Initialize this I said
you can either take data set and train a
classifier and that will be your initial
classifier
Right Or you can randomly initialize as
well it doesnt matter But we are we
are
uh we are we are assuming that all the
individual classifiers are better than
chance right So you have to its
better to initialize it with some
classifier that you train on some data
right So the first iteration is how we
do it
This okay
Now
if you
regularize the regularize this Suppose
we use Oh by the way
uh never in the gradient boosting uh
algorithms we restricted the form of HM
You can find an ensemble of neural
networks
by using this algorithm So theres
nobody stops you from doing that
Correct You can actually find this But
if you use decision trees see decision
trees as we saw were those algorithms
which are quick to build but theyre
high variance So all these techniques
are reducing the variance as we saw
Thats why typically
the ensembling are done using trees as
individual classifiers and if you use
trees as individual hypothesis in a
gradient boosting algorithm then its
called gradient boosted trees
Okay
Now
going one step forward
if you regularize the trees in a
particular manner
so here there is no regularization over
the individual individual hypothesis on
the parameter space And if you do it in
terms of restricting the number of uh uh
nodes in a particular depth and all
that We saw multiple ways of regressing
the decision trees right If you do
that and also consider the second order
term when youre expanding the Taylor
series expansion
it is it was observed empirically that
it will give you
better uh reduction in the error
compared to a first order gradient
boosted tree
And that particular algorithm is what is
referred to as XGBoost
Extreme gradient boosted models
Its basically using the second order uh
uh uh
gradients and regularizing the trees
explicitly So
XGBoost is one of the
go to algorithms for a lot of uh
industrial applications because its
very quick to uh
calculate and its exactly doing this
It is iteratively finding it Its a
its a boosting algorithm Uh the
individual hypothesis functions are the
are trees okay And they are done in uh
such a way that they are regularized at
every step is what XGBoost is all about
Okay
Okay so now there is uh any questions
here
It is definitely it is definitely
regularizing that way yeah But here
right Then we are doing it in a better
way We are iteratively doing it and we
are ensuring that
the minimization is
See in the bagging case
okay so now you since you made these
points are nice points In the bagging
case
theres no guarantee that the next
classifier or the other classifier that
you learn is improving over whatever
bagging that we have done so far And
there its not even iterating iterative
but still if you assume that okay
youre training one classifier at a
time
theres no way that your new classifier
that you learn is trying to undo the
mistakes that the previous classifiers
did
But here
you cast the problem itself in such a
way that the new classifier that you add
to the the ensemble is built in such a
way that it is
you know it is uh undoing all the
mistakes that the previous classifiers
have done till this point
Thats what the mean in the when when
when we started the uh discussion on
boosting I told you that this is a
principled way of finding the next
classifier in the ensemble
And what is this principled way in the
sense that you ensure that
the next classifier that you get is
always uh better than the ensemble that
we have so far
Thats Thats how we are doing it
So this is gradient boosted trees and I
told you that
that we can optimize over alpha as well
So far we have not optimized over
alphas
What happened is that there is another
algorithm called AdaBoost which was
considered as the pinnacle of boosting
algorithms You know it was
extraordinarily designed I think 95 is
when it came
And that was de de de designed
independently of gradient boosting
okay Its an algorithm
And people gave uh the statistical
learning theory or ERM explanation as to
why AdaBoost algorithms will do better
So after gradient boosting came
it was shown that AdaBoost is actually
one particular way of doing gradient
boosting on a particular loss function
Right So now that we have looked at
gradient boosting so I will write down
the AdaBoost algorithm and we can tell
you what it is algorithmically And then
we will show that these algorithms are
exactly
realization of the gradient boosting
algorithm Is what we will do
Okay
So perhaps well do it in the next
class And that finishes our ensemble
learning And then we will go to the
unsupervised learning methods The PCA
and and the other embedding extraction
I
I told you that Ill also talk about the
self supervised learning techniques in
the coming classes
Well do that in the next class Okay
Thank you
