---
id: 27cAa8L0JQo
title: Lec 58 Ada-Boosting
url: https://www.youtube.com/watch?v=27cAa8L0JQo
date: '2026-04-02'
duration: 40:08
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Lec 58 Ada-Boosting

## Transcript

speaker_1: Welcome everyone to this course
Uh in this lecture we will continue our
discussions on the boosting algorithms
So last time uh we started from the
idea of what bagging is ensembles are
right And uh
we discussed the naive bagging methods
where you combine classifiers
Uh
then we also looked at uh the boosting
methodology And in bagging we looked at
the random forest as uh a classifier uh
as an ensemble
We also looked at gradient boosted
trees GBMs or gradient boosting in
general So as I mentioned in the
previous class
the individual weak learners uh that are
a part of uh the ensemble need not be
of one type Uh typically you know it
will be trees uh that will be used as
constituent weak learners because
theyre easy to be
learned Okay theyre
non parametric methods and easy to be
learned Thats why generally the
gradient boosting methods like gradient
boosting or uh even bagging
the constituent classifiers are taken to
be decision trees but theory does not
stop you You can have ensembles of
neural networks You can have ensembles
of kernel machines and so on Okay
theres nothing that stops you from
taking different kinds of classi
classifiers and doing an ensembling
So today we will continue that that
discussion on ensemble
And we will look at one very powerful
algorithm called AdaBoost Okay
Remember in the definition of uh
ensembles
especially in the boosting strategy the
idea is to iteratively keep adding one
weak learner uh at a time Okay
And when you add a weak learner theres
this alpha which is the uh the weight
that is associated that is given for the
vote that is given by that particular uh
classifier
Now in gradient boosting we take this
tree tree this as a hyperparameter and
keep it as a constant right
But in uh the question is I mean the
most general formulation we had an m
here as well and we can optimize over
alpha as well
Uh we can look at what the optimal steps
step size is optimal weight uh that is
to be
multiplied with the weak learner uh so
that we get the best performance So
AdaBoost is one such algorithm okay
where
alpha is also learned uh in the gradient
boosting way
As I mentioned the previous time
AdaBoost was an algorithm that was
proposed I think in 95 or 96 as an
ensemble technique
Uh and it had
very good performance
Now gradient boosting uh came later
chronologically and uh
later people showed that AdaBoost is a
special case of gradient boosting as
well So what Ill do is Ill write
down the algorithm of AdaBoost and just
just explain that as an algorithm And
then we will recover this algorithm
via the gradient boosting uh that we
did
Okay As a special case Thats what
well do now Okay
Okay so the AdaBoost algorithm So
lets start with a classification
problem Given a
Given a data set D
We have n samples
Standard classification problem Let us
consider
a binary classification problem
And let the labels be 1 and 1
Again uh 1 and 1 because algebra works
out nicely Okay So lets take them as
 1 and 1 The AdaBoost algorithm is as
follows
Initialize
Initialize weights to data points
uniformly
Lets call them w i
m m for the m iteration Sorry this
should be one Hold on
w i 1 to be equal to
1 by n
for i is 1 through m
The subscript represents the data index
And superscript represents the iteration
index
And we are we have m such classifiers
that we are looking at
So for
m equal to
1 to m
do
The first step is to
train a weak learner
Lets call it hm of x
With the current weights
Some data which is
w i m So please note that these
weights uh theyre not the parameter
weights that we are talking about These
are the weights that we assign to data
samples
You understand
The fundamental idea of AdaBoost is that
you assign weights to each of the data
sample
Okay And iteratively you keep changing
the weights associated with each of the
data sample
So remember that in any boosting
algorithm or bagging ensemble technique
we will do a sampling with replacement
When we do sampling with replacement so
far we are treating all data points
equal
But here in AdaBoost we dont treat
every data point equal We change you
know we associate a weight with each of
the data point and that keeps
iteratively changing as we move from one
one classifier to the other
Does it make sense So thats the
weight that Im talking about So
initially you give equal weights to all
of them okay And then
keep changing the weights associated
with each of the data points So that
thats what the idea is So now Ill
give you a formula to update these
weights as we move on Okay Now Im
saying train a weak learner with the
current weights on data So what do I
mean by that
So youll have to ensure that
this is the distribution okay that is
uh
uh maintained on data points when you
train a classifier So how do you how
do you make sure that it will happen
Do you understand So what do I mean by
this
In the in the initial step you just
train a classifier because youre
uniformly sampling
In the next subsequent steps when w m
changes what do I mean when I say that
you will have to train a classifier that
would respect this distribution on data
samples
There are multiple ways to do this
Okay One way to do it is
when you sample data with replacement
use this distribution on data instead of
uniform distribution
Thats one way to do it You understand
So we are assuming that we know how to
sample from a
sample according to a distribution So
if its uniform sampling you just with
with probability 1 over n you pick a
sample At 1 minus n you dont pick a
sample
If the weight is something else then
with probability that particular weight
you pick the sample i th sample and 1
minus that you pick Every sample will
have a different different probability
of being picked or unpicked
Okay You When you sample a data set
you sample according to that
distribution and then train a
classifier Thats how you do it Thats
one way to do it The other way to do it
is lets say that you do a uniform
sampling of data Then and suppose
youre building the constituent
classifiers are decision trees
Okay In decision trees if youre using
uh
uh the
losses like cross entropy or entropy or
Gini index
both of them need a
an estimate of pk Remember
Where pk is the
number of pk is the probability of a
particular class when you do that split
Okay Now estimate that pk based on the
current weights that youre assigning on
the
data points
Does it make sense
So what was the initial What was the
estimate on pk that you were considering
in the naive formulation It was simply
the ML estimate
Where you just count the number of
uh data points corresponding to that
class and divide it by the total number
of data points But now you dont do
dont use uniform distribution but use
these weights to estimate those pks and
then define the Gini index or whatever
metric that youre using for splitting
and then build a tree Thats what that
is what is meant by train a weak
learner Okay With the current weights
on data w i Or rather I can actually
say it this way
Train a weak learner respecting the
current
weights on data
Right How do you ensure that the
classifier respects the current
distribution on data I gave you two
examples of to do that See one easiest
way is to sample the data in accordance
with WIM Do you all see that these WIs
specify a distribution on data
Not on X
It specifies a distributed on the
distribution on sampling the data
Isnt it If there are 100 points
initially we started by 1 by 100 The
probability of picking a point is 1 by
100 After we get this it is not 1 by
100 Right It is this If you normalize
this it it is a discrete distribution
Okay Which will give you the
probability of the ith point being
picked or unpicked
Makes sense Yeah So well have to
train a classifier that way And then
well have to The next step is
estimate
the weighted error
Lets call that
epsilon m as
What is this
This is simply the weighted count of how
many points were misclassified under the
current classifier
Correct
So this is the indicator function
Okay If you take this it is simply
counting the number of points on which
the current classifier misclassified
divided by the total number of points
This would be n
If all weights are one then this would
be Sorry all weights are
1 by n This entire thing would be the
count divided by n Okay So otherwise
it is just the weighted
error of misclassification We do this
Okay Then
step is to
calculate estimate the optimal step step
size
alpha m as
So right now all these are just
formulae Well derive all of them one
by one Im just First Ill write the
algorithm and then So we estimate alpha
m What is alpha m It is the
optimal weight that is to that we have
to associate associate with the
classifier so that we add to the next
one Correct And then we have to update
the weights
So this is the iterative update So w
i
m plus 1 is
w i m
e power
 minus alpha m
y i
h m
x i
This is the update formula
The next set of weights will be
equal to this
Okay
And then you have
find the ensemble
as
h m of x
to be
Yeah That does This is the the update
that we have So this is end for
Okay So this is what we do in
AdaBoost So what what is being done
Let me just quickly
run through the algorithm So we
iterate We start with assigning Okay
So as an overview whats happening is
that every time youre

 learning a classifier on some
weighted uh
data samples We are doing sampling with
replacement And when we do sampling
with
replacement we are assigning weights
for individual data points and then
using those weights to train a
classifier
And every iteration we update those
weights and we iterate over this This
is This is the overview of the
algorithm
Now how do we get those iterative
weights is the question We start
uniformly okay And then
there is uh
the weighted error that we compute And
with that weighted error
we compute what is called as the optimal
step size Okay And using the optimal
step size we get the next set of
weights which we have to use for the
next next sampling And then using those
weights we train the current weak
learner and we keep iterating over this
This is what the AdaBoost algorithm is
Okay Any questions on the algorithmic
procedures
How is it being done
What we will do right now in the in the
next I mean uh
the coming section is that we will
derive all these formulas and show that
this is actually a special case of
gradient boosting with particular type
of loss functions and so on Well show
that But any questions on the
procedure If you have any questions on
procedure
What are we doing with the next set of
weights
Resample no Once you get the next set
of weights
you train another weak learner
respecting the current weights on data
Use those weights resample and train
it again
So these are weights kind of decide the
probability of picking a particular
particular data set yes Yeah
So here the weights are slowly decaying
to zero then at this point
Why would they Because I think the
update step youre multiplying with the
exponential Uh huh So are the weights
slowly shrinking to zero No they dont
have to because not all weights will
shrink to zero right So look at this
This epsilon m is only data points that
are misclassified
So therefore it need not go to zero at
all So because every weak learner will
have some set of points that are
misclassified and youre normalizing
them as well The weights surely are
changing every time In fact we will
see that
uh
this distribution will
try to minimize the error okay That
the previous
classifier made
So that that is that is how it will
come out to be Yeah

 Procedure wise its okay I suppose
Yeah Uh since we are sampling different
set of points even though with
replacement for each weak learner
how do these weights apply to the next
by indices
You still have the So see you associate
weights with each of the data point So
associate weights and then sample no
Youll still have the exact same thing
coming out
Yeah So only the weights would change
Okay So now lets look at this
algorithm as
a gradient boosting
Huh Capital M is it the number of data
samples
Yeah number of weak learners that you
would take Capital B whatever we were
using B in the previous class thats
Huh I think we can use B also
Okay let it be capital M because it is
M The number of ensembles that we use
 summation of W will always be one
Exactly Well ensure that it will
happen that way because Thats what I
said When you normalize youll ensure
that it it it sums to one
But if you look at the formula its
redundant
In the formula For error
Uh huh
 Weighted error Its redundant to write
Of course yeah
I agree Yeah
Okay So now let us look at
AdaBoost as gradient boosting
So recall that in gradient boosting
what we do is that we write uh h m of x
as h m minus 1 of x
 plus alpha m times h m So this is our
iterative updates And we have alpha m
and h m We want these to be
to be the minimizers
of
the loss that we calculate between y i
and h m of x
So this optimization is over alpha and
h So we need to find an alpha and
alpha m and an h such that this is
optimized right That is thats our
goal in gradient boosting okay
Now for AdaBoost
the loss function
that is used
is as follows We define L of
y h of x
to be equal to e power
 y into h of x
So this is called the exponential loss
So if you remember the definition of
loss function that we had it should
take
inputs as the as the cross cross product
of y and h of x It will give you it
should give you a non negative real
number okay Is it doing it So this
this thing is taking y and h of x as
inputs okay And if you multiply
because it is within the exponentiation
its always non negative okay And if
these two match
if y and h of x match and remember that
in our
definition y can take value 1 and 1
If y is 1 and h of x is also 1 this
would be
loss losses
lesser no Because there is a there is
a minus here
Right If these two match then you have
lower loss If these two dont match
then you have higher loss
So this is a valid loss function Okay
Now
this implies that
the
objective that we would want to optimize
now will be e power
y i into Okay maybe Ill write one more
step
I have uh
e power
 y i
into
h m h m minus 1 x i
plus alpha
h of x i
Its correct right This is the loss
function So this is This is what Ive
written here
All of you with me
Loss with respect to y and h m So h m
is
given by this
Uh where
Here
No no no The optimization is over
alpha and h right Yeah So you want
to find an alpha and h such that the
loss on h m is optimized
Minimized But we find it with respect
to the previous hypothesis Uh h m is
what you have uh I mean assuming that
that you know h m minus 1 the optimization
is over alpha and h Thats it Uh
inside the loss function shouldnt it
be h m minus 1 because that we havent yet
found right
No no no This entire thing have to be
a function of alpha and h
that you optimize over
Because youre optimizing over h and
alpha right So that has to be a
function of h and alpha and what you
evaluate is h m minus 1 Thats how we did
gradient boosting also right
Make sense
Right You look at this right So this
h h m minus 1 is something that we know We
are optimizing over alpha and h Thats
why it should be you This is saying that
you find h and alpha such that the loss
on h m of x is minimized because the
choose choice that you have is on alpha
and h
Okay So this is what the loss function
right now is So let us uh
uh
write that down as uh
So we want to find an h
the h star and alpha star
uh that would minimize
this thing So we will split the
exponentiation now This is equal to e
power
 y i
h m minus 1 x i
times
e power
y i into alpha times
h of x i
Is all right
So what did we do
I just split exponentiations into
product We had e power a plus b I wrote
that as e power a times e power b okay
This is what we need to optimize now
Now
uh consider
this term
e power
 y i times
h m minus 1 into x i
into e power
y i alpha h of x i
See this term
is independent of
h and alpha
The optimization variables are h and
alpha So
since this term is independent of that
we can
take that as a constant and push it out
Okay We dont have to So lets call
this as
define this as
w i of m
Okay
Define that as w i of m So the this
will become
Correct
Huh
Oh the minus have to come inside
youre saying
So there is a minus here
Yeah and theres a minus here as well
Correct Yeah
Okay
Now this is one thing The other thing
is maybe before this we can
Theres a side note okay So note
w i m is recursive
That is
w i
m plus 1
What is this equal to
e power
 y i times
h m of x x i correct
Now since h m x i is
recursive
this is also become recursive right
So what is this equal to
Is equal to e power
 y i times
h m minus 1 into x plus
alpha n times
uh h m of
x right x i yeah
So this is equal to e power
times
e power
 alpha m
y i
h m of x
What is the first term here
This is w i m
times e power
 alpha m y i h m of x
This is exactly what we had here no
See this So we recovered this
particular update So weight update
comes from the definition of it
All right
Lets continue
Now the loss function is
 This is the term now right So we just
wrote where are we coming from So here
since we defined this term as WIM
therefore the loss term will now be
equal to WIM e power
 minus yi alpha times h And we need to
optimize this with respect to
h and alpha correct
Is what we have
Now here what we can do is as follows
right So this is equal to
this term is equal to
So I can split this sum into two
right One
all is such that yi is equal to
h of xi
and all those indices
where there is a misclassification
Okay
And whenever there is a correct
classification what would this term
would be
This term would be WIM
cuz yi the product of yi and
uh h of xi will be
one So there will be an e power minus
alpha term
And this term
whenever there is a misclassification
this term would be e power alpha times
WIM
Correct
Okay Now what we should do is that we
should find So we we have to optimize
this with respect to h
Okay
What choice of h would minimize this
See what do we have to do We need to
minimize this right With respect to h
and alpha The those are the only two
variables that we have Well see how to
do it with with respect to alpha But we
need to optimize with respect to h as
well So now tell me what sort of a
classifier would minimize this
Come again
The second term is
minimized right How do you minimize
the second term Second term is the
weighted misclassification error no
Right So youll have to ensure that
the classifier that you train has to be
in such a way that the
error on the weighted samples is
minimized Thats why I told you right
Youll have to sample according to WIM
and then train a classifier in
accordance with this Or
if you are looking looking at trees
youll have to define your loss
functions for splitting in accordance
with WIM
Do you see what Im saying So well
write that
The above will be minimized
by an h
that would
minimize
the weighted misclassification error
Sum of
or sum of weights on the
misclassification misclassified points
Correct
Well have to find a classifier
okay such that the sum of weights of
the misclassification misclassified
points is minimized So how do you do
this One way to do it is by sampling
The other way to is to tweak the loss
function
using WIs
Okay So what step did it recover In
the algorithm what step did it recover
Well have to recover each step of the
algorithm by
from this gradient boosting right
Which step did it recover now
No
The first one You train a weak learner
respecting the current weights
Because we are optimizing over h
Right So it recovered the
first step So well have to train what
in when you are doing AdaBoost youll
have to train a classifier finally at
each step right So how do you train
that classifier You train it in such a
way that the weighted
uh sum of the weights that we are
assigned that we are assigning on the
uh weighted points are misclassi is
minimized
It is recovering the first step So now
theres only one thing that remains now
which is
getting this optimal estimate of alpha
Okay well do that now

 To get
optimal alpha
See this weight term is actually
getting overloaded Theres Theres one
weight on the data samples theres one
weight on classifiers and so on So
yeah just be careful
Well have to get this optimal alpha
So let us do that
Let W
capital W be equal to the sum of
all the weights
on data points
So you take
See by the way this is still
unnormalized So if you normalize it
it will become one
If you divide that when we you just made
a statement right That becomes
redundant That becomes redundant only
if you normalize them to make it a
distribution
Generally normalization you can make it
a part of the algorithm or you do it
outside the algorithm as well when
youre sampling
For now we have not normalized it
anyway
Right It can be It is simply a positive
real number Therefore this W is not
one
Okay
Um so this let this be this So now
by definition
we have
epsilon m to be equal to
1 by W So this is the
wherever y is not equal to h of x
So you recall the definition of this uh
uh epsilon m right Where was this
Yeah so we defined it as
the
percentage of the weights okay Uh over
the samples that are misclassified
right
Epsilon m is So instead of writing an
indicator function here I wrote this in
the summation here
Do you see both of them are same
Okay Ill write it that way This is
equal to
uh
How did we write that
So i is one through n
WIM
is an indicator
where these two dont match
divided by
This is how we defined it right
That exactly the same
Right Yeah instead of I mean you
either put it in the summation or you
put it as an indicator function summing
over everything Same thing Okay fine
Therefore
uh
this term
is equal to capital W times epsilon m
Right
And uh
This term is equal to
W times 1 minus epsilon m
Do you see why
Pretty obvious no
You take this term you multiply it
here you get this If you take the sum
over all the correctly classified
points you just get it as W times 1
minus epsilon Thats it
Okay why did we write it this way Its
because
this is our loss function remember And
we have to basically we have to
differentiate this and uh
differentiate this with respect to
alpha H is already done
We already looked at h right Well
have to do it with respect to alpha
and put it to zero And therefore we
are trying to write this term as a
function of alpha
and epsilon This was the loss function
right
So consider
Uh we will stop here and continue in
the next lecture
