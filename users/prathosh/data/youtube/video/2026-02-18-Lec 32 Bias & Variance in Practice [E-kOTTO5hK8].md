---
id: E-kOTTO5hK8
title: Lec 32 Bias & Variance in Practice
url: https://www.youtube.com/watch?v=E-kOTTO5hK8
date: '2026-02-18'
duration: 37:14
model: youtube-captions (en-orig)
transcript: true
---

# Lec 32 Bias & Variance in Practice

## Transcript


Welcome back Lets consider an example
Okay lets construct a distribution and
see how things work So lets say that
assume that lets take an example
Suppose X is in R and Y also is in R
because I cannot draw anything if its
more than R Okay So I Ill take both
of them in R and lets say this is how I
define my distributions
Y is equal to some a x²
 plus b plus epsilon
epsilon is cosian
and a and b are some numbers
see whats happening my pxy what
distribution is pxy now its quashian
right with a particular mean and
variance so the reason I did it this way
is I just wanted to draw the data
come again
uh I is a one by one matrix
Okay let me draw that data No Uh
okay These are my data points Uh how
many of them do I have So this is
so this is y and we have 1 2 3 4 5 6 7 8
9 10 Okay 10 data points Ill tell
you why I counted that in a while There
are 10 data points in my data set Okay
And this is how it is See some
textbooks tells you that uh okay I mean
theres a parabola and you just perturb
it and you add noise to it to get data
I mean all that Im doing is Im
generating a data from an underlying
distribution that is gausian Thats it
The reason I did it this way is that I
can write it as I can write it around a
particular parabola I mean this dotted
line has no significance whatsoever
I think all of you understand that
because we are looking at a
probabilistic way of looking at trading
things Okay this is what my data is
Okay am I overloading uh notations
here See these are
these xs are uh yeah maybe Ill change
it
Uh what symbol do I use
Circles is not taken Dont think that
there are zeros or something No
Okay Okay 1 2 3 4 5 6 7 8 9 10 11 I
have 11 Now make it 10 easy that way
Okay this is the data set that I have
Now let us compute Lets say that we
are solving uh
an ERM problem with squared error loss
Okay I will write two classifiers or
two regressor two hypothesis and lets
study what will happen to bias and
variance Okay the first classifier is
or the first regressor is lets call
that H1 of X This is equal to
uh two
for all x
This is one classifier Okay There is
another classifier
h2 of x is equal to
y for all x
of x i is equal to yi
So do you understand what these
classifiers are The first classifier is
or okay its a regressor The first
regressor or first hypothesis is that
its a constant for all data points The
second uh regressor is
it is equal to the particular y at all
data points
What is it by the way This h2
 Yeah its called lookup lookup table
No its a lookup table
Simply a lookup table right You have
given 10 data points
Remember all those data points
perfectly
Okay
Now
which one do you think is a good good
hypothesis
Huh
 Neither right Yeah So thats exactly
the point Neither of these are good
hypothesis Why Lets look at this
What happens to the bias of the first
one and variance of first one Lets
write that So what about the bias of
this and variance of this
What will be the bias of this first
classifier
No lets lets only say uh whether its
uh like high bias or low bias right
What is the bias of this
 Extremely high bias right
What about variance
Please show this algebraically
Another homework show that for this
particular hypothesis variance is zero
Intuitively why is the variance zero for
this See what is variance Variance
studies what is the uh variability
across different samples of data set
This guy is not even looking at data
What variance No variance You take
this person anywhere he has very high
head and he has his bias very nicely
uh stitched completely Right So no
variance at all Wherever you take them
they behave the same because they are
completely oblivious to data No they
are blind basically
We dont want such people too much bias
Okay
Okay What about the second person
Right Second hypothesis So lets write
down the bias and variance for this
Whats the bias of the second
hypothesis
Yeah please show that this can be
algebraically shown This has zero bias
Why Because what is bi what is bias
Bias is the the var the the deviation of
the classifier from the reality
This is exactly the classifier on the
data that it has been shown What about
the variance of this
Extremely high
So this is that person that adapts to
the local environment too well
Okay So has no opinion of his own
Very dangerous people
Both kinds of people are dangerous You
know we dont want people who are too
high headed are the ones who gets
adapted very easily
Okay Now suppose you have you know one
side point is suppose you have access to
the entire universe and you build a zero
bias classifier
ML is solved right My opinion is maybe
thats what is happening in todays ML
You take the entire universe and
remember it all
Okay Anyway so thats thats an
opinion You can ignore the opinion But
here is the takeaway The key takeaway
is okay So tell me what happens to the
accuracy
of the second hypothesis the training
accuracy of second hypothesis
100 percent So here is the uh key punch line
right getting
100 percent accuracy on training data does not
mean anything
okay because this I mean it it may only
mean that you might have ended up with a
hypothesis that has zero bias with a
very high variance thats it
make sense
okay so remember that what about the
second case second case it will have
very low uh training accuracy not zero I
mean maybe you are lucky and you know
some of the points are coinciding with
this right but still yeah so it it will
have a large training accuracy but most
often what happens is you will end up
having the second type of classifier or
hypothesis where you get because youre
so youre optimizing for training
accuracy you see when you when you when
you solve erm because you are doing it
on drain youre optimizing for training
accuracy and getting 100 percent training
accuracy does not mean anything
Okay
Okay So now
so
I Ill come to pragmatic
way of trading
So typically in a small sample case
Ill take you a question in a while
Typically in a small sample setting
the following behavior is observed
See this is not whatever Im saying
right now is only empirical Theres no
theory to it Theory only says that the
risk decomposes into these two terms
Typically in practice whenever you are
looking at small sample cases this
particular behavior is seen Okay What
is that
Suppose you plot some performance metric
along y axis
uh its plot error Okay Generally one
minus performance is what is plotted
One minus accuracy Okay Along y axis
you take
model complexity
See what do I mean by model complexity
Suppose we are looking at polomial
regressors
Okay the degree of polinomial that we
consider as our hypothesis function can
be looked into as model complexity
that is one way to measure model
complexity Now the reason I looked at
know wrote counted these points here is
suppose I take a 10th degree polinomial
and try to do erm on this I can always
find coefficients such that I get 100 percent
accuracy on this right because all
points you know have one coefficient
corresponding to each point I mean this
is the uh this is the this is the uh
extreme case in which I remember the
data point itself instead of remembering
the data point you can have 10 unique
numbers which are the coefficients of
the polinomial and associate each of
them with one data point and you get
100 percent training accuracy X axis is that
so we are suppose if we are considering
polinomial regression which is the
generalized linear regression case then
X axis is the degree of polinomial as we
move on in the course this can be the
number of layers in a neural network
basically its the number of parameters
that we have in model right or it can
also be
I mean I I I told you that uh the models
in which uh uh analytical differenc
iation of erm is difficult We will
resort to
the iterative way or numerical way of
solving it Right This x axis may be
different steps in your iteration
See every step in your iteration
actually gives you a different model If
you look at it why suppose you are
doing a logistic uh regressor right
Every step in gradient is is giving you
a new set of parameters which means a
new hypothesis anyway So thats x axis
Okay in neural network what happens is
as you are doing that iterative uh
gradient descent every step will become
will be plotted along x axis Do you see
the point If you do em then every step
in EM is along your x axis
Its a different set of parameter and
Im assuming that as Im going from left
to right the complexity of the model is
increasing
Thats an assumption The I I choose to
plot the uh graph that way It doesnt
have to be the case but typically it
happens that way No because as I said
right if you are doing a polinomial
regression you keep on increasing the
the order degree of the polinomial then
the complexity keeps increasing Okay or
if you keep on increasing the layers of
your neural network then it increases
and if you do if you keep doing the
gradient descent it increases is the
assumption that that that have been
made Do you understand what x axis is
now And this plot is common across all
the hypothesis that we will see in this
entire course It does it it has and
its very general that way Okay Y axis
we plot the error Now typically
observed behavior is okay as the model
complexity increases so you start with a
large error model because you have made
some initialization as the model
complexity increases the error keeps
decreasing
this
So this is a typical behavior Okay If
you actually do it in practice you
dont see a curve that is as smooth as
this Youll see something similar Not
not not something exactly this This is
exaggeration Okay Yeah What is this
This is the
the risk or Yeah risk or error
on training data
Okay Now what happens to the validation
data or test data or another sample of
data set right What happens is note
that you are do you are solving on this
drain and you are measuring your
performance on some other data It can
be validation data test data How does
that look like It looks like this
Start decreasing
and then starts increasing So this is
what is happening here
So this is the point where we want to
ideally operate Right Okay Each of
these is taken as a different tick
Okay This is the point where we want to
ideally operate So now what is
happening Why is this behavior seen
See what happens is the following
This particular re region lets write
down the bias and variance here This is
bias and variance This is bias
and variance
So what can you say about the bias and
variance in the left part of this dotted
line
This model is
very high bias
low variance right And this is
low bias and high variance
The two extremes that we saw okay the
H1 and H2 those two classifiers that we
saw one falls in the region of high
bias and low variance The other is the
region of low bias and high variance We
we we need neither
Okay Now this is the typical behavior
As I said when the model complexity
keeps increasing the the error or the
accuracy on training data keeps
decreasing Right Because the more and
more parameters that one is given what
is the intuition behind it The more and
more one is given the parameters you
can create a lookup table that would
remember the entire data set Right
Thats why you know you enter a low bias
and high variance region In the initial
parts what happens is why the bias is
higher is because
the model is not capable of even
explaining the re the seen data I mean
forget about looking at the unseen data
So first we have to explain the un okay
this is how it is You have to avoid
both but you need to operate at a place
where both bias and variance are low and
in the popular culture these two things
are actually called something Now this
is called overfitting
The low bias and high variance operation
operating point is called overfitting
and high bias and low variance point is
called the underfitting
A hypothesis that has high bias and low
variance is called I mean is is referred
to as one that has underfitt the data
and the one that has low bias and high
variance is referred to as the one that
has overfit the data
Is that okay
Now here is a suggestion If you are
given an ML task to solve okay start
by overfitting
You should at least overfit
Yeah So if you tell me that I am
building a classifier that has that is
not giving me 100 percent accuracy on even
training data then you have not even
started ML
okay I I tell this to all of my students
that given an ML problem start by
overfitting at least overfitit and come
back
what Im saying is operate here
okay dont operate here
you can always come up with a classifier
that can operate here at the region of
low bias and high variance
and that is what is done in in in in
practice In practice what is done is
you always start with a classifier okay
overparameterize it and operate in the
region of low bias and high variance and
then push it backwards
And this process of pushing the backward
pushing the pushing the hypothesis from
the low bias and high variance region to
a low bias and low variance region is
called regularization
And that has exactly one to1
correspondence with the basian map
estimates that we saw which is what
well see later So pragmatic uh
analysis is that you always start when
you whenever you are given an ML problem
you always start at the region of low
bias and high variance How do you do
that You do this by overparameterizing
the hypothesis
Is that okay Yeah Let me write that
So tip
always
start
with a
hypothesis
that operates at
Its in the high
low bias and high variance region
Its called the overfitit region
and then push back
or rather region by over parameterizing
right via over parameterization
I can never
accept an underfit classifier as an
answer
Never I mean you tell me that Im
getting 100 percent accuracy on training data
and very bad performance on test data
Im fine At least you have overfit
Okay always start by overfitting and
then push it back This is how you do it
pragmatically Ill stop here for a
while and take questions if there are
any before we move on to the next topic
As I said no this is actually a very
central part Unless you have access to
infinite data sets okay and a hugely
overparameterized model youll always
end up with this particular type of
scenario where uh you do very well on
training data and uh pretty bad on test
data
Okay because its very easy to operate
at the region of uh low bias and high
variance by by over parameterizing
questions on this Yes
how does it have the 10 points that we
have out of a single data set and
variance gives us how this changes in
different
 ah okay the question is how is the
second hypothesis here has high variance
the variance term has an outer
expectation with respect to pd as well
right so we took we looked at one data
set now suppose instead of sampling
these 10 data points I sample 10 more
data points and plot them what will
happen to the error of uh uh the
variance part of that classifier this
particular classifier when I say yi Im
not changing yi per data set Thats
what the confusion is Thats not what
Im doing Im making this equal to yi
only for this particular data set and
even for the new data points that I
have Right Either this is not defined
or it will give you a constant value
The question that you should you should
be asking is how would this classifier
behave on some other data set
Ive not defined it Actually the way to
define it is it only knows the this many
data points when a new data point comes
in either itll give you a constant
value or itll just randomly choose from
one of this and then outputs in which
case the variance is too high I think
that was the missing piece did all of
you get that I think thats I should say
for all x i
in d okay and its equal to h2 of x i is
equal to anything right so zero
otherwise
see this part I can do it anything
because it doesnt know what to do when
it when it is shown
something outside of what it has seen
I cant stop myself uh from saying this
when
when I started teaching at IIT Delhi
right so student of mine is telling him
that you know guys I had a lot of
expectations from you and you know I you
people did not match my expectation I
just having a private conversation the
guy said I I I had just taught them you
know bias variance decomposition and all
that sir we are all models that have
been overfit in kota for 2 years
thats exactly was a statement you
understand what it means most of these J
coachings happens in this place called
Kota right so its its severe
overfitting over two years is what what
we have done is what he was saying right
so basically the idea is that uh an
overfit model knows
perfectly what to do when it is shown
something that it knows
it has no idea what to do when it is
shown something that is that it is not
seen
Right So you need a balance and it
becomes too much a philosophy but
nevertheless right everything needs a
balance You should have biases
right and an ideal situation is that
where you have zero bias and zero
variance right and you quickly adapt
You get a new data set immediately adapt
and you are so generalized that you can
do it Its very hard but you know
striking a balance between good biases
and less variances is how one should
operate Okay Uh anything else Any
other question Yeah
 Huh That Yeah So the question is why
is it pragmatically I I did not say
wrong I mean its a typical way to do
it is from start from over over
parameterized model and reduce uh the
parameters right its because uh the
only thing is its its functional ease
See what happens is that if you start
from uh an underparameterized model
right you dont even know whether uh
your I mean okay you will know that uh
that underpar underparameterized model
is not even explaining your scene data
now you go till explaining your scene
data but where do you stop
the question is where do you stop
on the other hand if you start from
completely explaining the scene data and
you know keep pull it back till the
point where it does well on uh the
unseen data I think thats a better
strategy Its only an engineering
pragmatic strategy No nothing uh
theoretically sacros about it In fact
as we will see in the next class there
are these methods called regularization
methods Okay which would give you a
way to reduce the bias It is it is easy
to uh increase the bias Yeah increase
the bias Its easier pragmatically to
increase the bias of a model So you
start from an overparameterized model
that has very less bias and add
regularizers to increase the bias
 Pragmatically easier You always
overparameterize overfit and then
increase the bias
 No start from an overparameterized
model that over fits No And then
increase the bias
 Not necessarily See well see that in
the next class right when we look at
regularization the way we do it know we
modify the empirical risk objective
itself so that implicitly it has a high
bias component to it well see that they
they are called regularizes yeah hold on
just just to complete this question
right if you if you people can see
uh whatever Im saying to saying
techniques as the ones that would
increase the bias are very very similar
to the case where we imposed our uh our
belief belief on the estimation problem
isnt it Thats exactly what it is
See I told you that ERM has a exact uh
relationship or one to one relationship
with ML estimation Now regularized DRM
has oneonone relationship with the map
estimator Theyre exactly the same So
what we do is whatever bias that we have
about the parameters we impose them as
regularizer explicit regularizers
Basically you people would have already
guessed it now right We solve a
constraint optimization problem
instead of solving see erm is an
unconstrained optimization problem right
instead of solving an unconstrained
optimization problem you solve a
constraint optimization problem and
construct the grandas leanians right
those constraints will be the basian
prior that you impose on your ML
estimation thats all theyre exactly
the same right so thats why its
convenient to to impose our bias okay
its not convenient to you know start
from a very low bias Because you the
least that we should do is explain
whatever we are seeing right now
 Huh Okay What is H bar The question
is what is H bar H bar is not the same
classifier Okay Whenever you say
classifier you should know that its a
hypothesis It can be classifier
regress or anything Huh Yeah Its not
the same hypothesis uh that is performed
that is trained across different data
sets Its the average of those
different hypothesis trained on
different data sets
 Yeah When when you say same classifier
its from the same class of hypothesis
Now if youre looking at linear
hypothesis then you are looking at
average linear hypothesis and so on
Yeah
No thing See a test data leakage is is
a is a is a pragmatic scenario right
You should not do it Uh if you do it
then what people do is you know if there
is test data leakage you always look at
your test data and tweak your see the
worst case scenario is that you train on
test data
See nowadays there are uh benchmarks
that are being published right right
left and center you know every new model
that comes up in the market youll have
to show that you beat the new model you
you beat the existing uh models
Now the best way to do that or the worst
way to do that is to train on test data
Everybody has access to test data Now
how do you how do you trust whether
somebody has trained on test data or
not Typically what is done in global
computations etc is test data is like
held out it is not shown
but the worst way to do it is that
include your test data and over fit on
test data
some of my students when if you were to
cheat right some of my students are
actually doing deliberately bad on test
data train on test data so that you
dont show 100 percent accuracy you show 91 point 2 percent
2 percent accuracy or whatever right So
thats the worst thing to do The second
worst thing to do right is that you
dont train on test data but you set
your hyperparameters based on test data
right For instance you train a
classifier see what your accuracy is on
test data not on validation data Do it
see it on test data Its bad Come
back go back and change your
hyperparameters Youre not training on
test data but you are changing your
hyperparameters on test data Even that
is test data leakage And this happens
very often in academic settings
Because in academic benchmarks
test data is there I mean you in an
ideal world you should not be looking at
test data but
imagine a situation right you know where
you know you are a grad student working
on a new new algorithm You get your uh
new algorithm
Do you fix your algorithm and just test
on test data and whatever accuracy you
get you stop there Nobody does that
No So what do people do if the accuracy
is bad Get back and tweak your
algorithm and then go back This is
actually wrong You know this is just
data leakage
So in an ideal world the al the training
or the erm should have no information
about the test data even at the level of
getting hyperparameters That thats an
ideal situation Yeah thats how you
have the validation data Look at the
validation data Do whatever even
validation data you dont train on
validation data set your
hyperparameters on validation data and
then freeze your model and then release
it Yeah
 How do we
 validation data Thats exactly why you
have validation data
 No no make no mistake Training data
is on which you solve the ERM So
validation data is the one that you use
to tweak your algorithm
hyperparameters
You dont train on validation data So
you dont solve VRM on validation data
You only do ERM on training data Change
your hyperparameters looking on
validation data Thats it
 Change it Thats also a hyperparameter
use you you can use your validation data
to do anything that you want
right just dont use the data upon which
you report your final performance
metrics on thats called test data no so
basically all Im trying to say is you
have multiple samples of your data set
use one to solve erm use one to set your
hyperparameters the one upon which you
show your final numbers dont use it for
anything
okay in the process of erm that is the
golden standard
Okay
 Welcome Yeah Go on Go on
 For the empirical risk not necessarily
Yeah Uh the only thing that happens is
we are assuming that with uh the
question is um does the treatment change
if youre looking at empirical risk
right It does not The only thing that
we assume is that asytoically it always
risk goes to empirical risk this this
practical behavior that I just showed
you right now is for the empirical case
where you where we have finite samples
if you have infinite samples you can
actually make both bias and variance
arbitrarily low but typically know the
the so called trade off that people talk
of always happens because that we are
operating with small samples and
operating with small models if you try
to reduce the bias the variance sort of
increases and the other way please note
that its a misnomer that there is a
trade off between bias and varian There
is no trade off algebraically
Risk just decomposes into these two
terms And both of them can be made
arbitrarily low if you if you design
your hypothesis well And todays ML
methodologies are actually doing it by
constructing a very large classifiers or
very very large hypothesis with large
amounts of data Okay But typically
what happens is that if you have small
samples and uh and and classifiers that
have lesser parameters theres a tension
between these two terms is its only an
empirical observation it has nothing to
do with theory Yeah
 Good question The question is suppose
we change the loss to squared error from
squared error to L1 Do we get a closed
form expression We do uh theres a
paper uh that does it for cross entropy
You can search it can you can look for
that People have done this for multiple
kinds of loss functions Similar
behavior is seen across different loss
functions
 Good question The question is is there
a possibility where the error on
training data set can increase
It can See suppose you are doing u u um
gradient descent using some hypothesis
on training data right theres no
guarantee that why increasing the
parameter should uh decrease the
training error so the designer has to
ensure that the models are chosen in
such a way that you reach least training
error thats why I told you start by
overfitting
okay in practice what happens is that if
you over parameterize see lets think
about it now worst case suppose you have
your model to have as many parameters as
there are data points in your training
data then you should be able to achieve
100 percent accuracy you know cuz all it has to
learn is to assign one parameter to one
data point
you understand what Im saying suppose
you have thousand data points in your
data set and your hypothesis has
thousand parameters all it has to do is
associate one number with one data point
thats it that gives you 100 percent training
accuracy so a designer has to always
ensure that your model at least gets
100 percent training accuracy
It may be a very bad model right It
may be a over fit model but you should
at least overfeit When would the
training error increase is is when if
you have made your model lets say
underparameterized and it does not even
have a chance to remember the scene
data Thats when the error keeps
increasing That can happen But youll
have to thats what training is all
about You design your classifier in
such a way that training accuracy keeps
increasing as you move on
In the next class Ill tell you more
you know practical ways of doing it
when we talk of regularizers But yeah
so thats how you do it Question
 Good question The question is for
generative models what is test data
Youll have to wait till my next course
Yeah So the act the thing is the
following right What is done is that
you keep aside some samples The actual
question that you should be asking this
okay test data is actually some other
some other sample from the underlying
distribution that you are trying to
sample from The question that you
should be asking is what are the
metrics
Data can always be obtained The
question is what are the metrics The
metrics are there are different ones
There is something called fretches
inception distance You know there is
there are some uh uh uh human evaluation
metrics and so on Suppose youre
looking at there is one very uh famous
data set that we always work on was
called SV bench uh a software
engineering tasks a lot of tasks right
so there you have verifiable metrics
right how many test cases that it has
completed thats a metric you can always
do that data is always coming from the
underlying distribution that you are
trying to generate from data is not the
issue the question that you should be
asking is how do you define accuracy
when you dont have labels you can
always right because we saw labels as
one another dimension of data you can
always define some metrics that way
Yeah
Okay Okay So thank you Uh this is
all about this class So next class we
will look at how to increase the bias of
models uh in the setting of
regularization See you Thank you
