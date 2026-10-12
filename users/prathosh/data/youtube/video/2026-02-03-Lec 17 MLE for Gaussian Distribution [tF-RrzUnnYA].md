---
id: tF-RrzUnnYA
title: Lec 17 MLE for Gaussian Distribution
url: https://www.youtube.com/watch?v=tF-RrzUnnYA
date: '2026-02-03'
duration: 26:07
model: youtube-captions (en-orig)
transcript: true
---

# Lec 17 MLE for Gaussian Distribution

## Transcript


Okay good morning Uh welcome to this
class on density estimation
So last time when we when we met we
discussed about uh the optimal
classifier we looked at the risk
minimization framework c the problem of
machine learning as the one of uh as the
one that minimizes what is known as the
risk Definition of risk is that you
define uh a function first between uh

two random variables of interest X and Y
and call that the hypothesis function uh
which we denoted as h of X And then you
define the notion of a loss function
that takes in cross productduct of y and
y and y with itself and uh maps it to a
positive non negative real number and
the expected value of that loss uh under
the joint distribution of the random
variables under consideration is what we
defined as the risk function And the
goal of machine learning uh is to
estimate or find a hypothesis function h
that would minimize this expected loss
which is also called the risk And we
saw that the true risk which I have
written here This is the definition of
true risk The expected value of the
loss with respect to the joint
distribution cannot be minimized because
we dont know what the underlying joint
distribution is But practically we can
take a surrogate of this particular
expectation which is the uh empirical
risk which is the sample average of this
particular quantity and then optimize
and find an h So that that that
framework was referred to as the
empirical risk minimization and that is
what we solve in uh machine learning

Now rest of the course
we will be looking at different
algorithms different ways of solving
the problem of empirical risk
minimization And in last class we also
connected the framework of empirical
risk minimization or risk minimization
in general with the distribution
estimation problems Right So the
solution uh that we obtained by solving
the optimization problem in risk
minimization
refers I mean points back to estimating
an underlying distribution depending
upon what problem we were solving So
this is I mean one should be very clear
about this story because from from now
on we will be looking at different ways
of solving the problem of erm So itll
itll become algorithmic rather than
philosophical
Okay Philosophy of machine learning is
what we saw so far Okay So we are
given samples from an unknown underlying
distribution and we are interested in
estimating the distribution Or the
other worldview is that there are uh uh
samples from two random variables X and
Y Theres a function that we are
learning This is for supervised machine
learning Unsupervised machine learning
you dont have the notion of Y but you
learn a hypothesis function The way you
do it is define the notion of a loss and
minimize find that function by
minimizing the expected loss Both are
equivalent Now some of the algorithms
that we will be looking at we will see
them as the ones of distribution
estimation right and the other some of
the algorithms that well look into this
well consider in this course will be
from the lens of directly estimating h
by taking a canonical form
okay so I whenever we look at that right
of the particular algorithm I will tell
you what uh what approach that
particular algorithm has taken but
remember this that both of both of them
are exactly equivalent that way so we
also saw examples
on
when would a particular type of loss
function emerge When you make a
particular distributional family
assumption distributional
parametric assumption on the
distribution it will boil down to
choosing a particular loss function We
saw a couple of examples For instance
if you choose your uh underlying density
function that is to be estimated as a
goian distribution and choose the mean
of that Gaussian distribution to be the
hypothesis right Then estimating I
mean getting a maximum likelihood
estimation under this assumption is
equivalent to solving erm with the
squared error loss function is what we
saw correct and this is with the problem
of regression Remember this is what we
had done last time Now I showed you
another uh uh
proof where I told you that if you
choose particular loss functions okay
and if you I mean uh particular cases of
problems you know for instance you
choose a regression problem you choose
classification problem and so on the
optimal minimizer for the risk okay
takes a deterministic form in the sense
that an analytical form and one example
for that was this optimal classifier
which we call the base classifier
and this is the form that the minimizer
of the empirical risk takes or true risk
takes Its not even empirical risk mind
you because we showed that this is true
for minimizing the true risk itself If
you are considering the problem of uh
classification then the classifier or
the hypothesis function that would
minimize the true risk under the 01 loss
is the one that decides based on the
posterior of Y given X And this
classifier was referred to as the base
classifier and this is optimal in the
sense that the risk associated with this
base classifier is the least compared to
any other classifier that one can
design
Does it make sense Okay So this is
what we had seen Now the question that
we should be asking is suppose you are
given some problem
Okay a classification problem What is
the first uh approach that one would
take Say one would try to build a base
classifier because I know that the base
classifier is optimal I cant do
anything better than base classifier So
I would build the base classifier Now
to build the base classifier I need to
know the posterior of Y given X
Correct Now do we know do we know P of
Y given X So we dont Now this
building the base classifier boils down
to estimating the distribution
Does it make sense Right So lets
write that So implementing the optimal
base classifier
demands
estimating densities
from data

Okay Now we can we can directly hope to
estimate the underlying density because
the whole problem of machine learning is
estimating underlying density This is
one other way to see it Even if you
want to look into this problem from the
angle of risk minimization then even
risk minimization frameworks asks you to
estimate the underlying density So what
densities do we have to estimate We
have to estimate So example is so given
data given d
estimate
estimate px which is the marginal of x
can estimate py marginal of y you can
estimate p of x given y which is the
conditional density of x given y by the
way this thing especially in the context
of base classifier has a name its
generally referred to as the class
conditional density
you read some textbooks right theyll
use this uh nomature

 Okay theyre called class conditional
density for obvious reasons right
These are this is the density function
of X conditioned on a particular class
So thats why its called the class
conditional density If you want to go
back to our initial uh uh example of the
X ray so this is the distribution of
the pixels given that the image has a
particular class or disease or non
disease Thats what we are talking
about So now given data our goal is to
estimate these density functions So it
can be marginal it can be uh the class
conditional density or anything If you
suppose you want to estimate the uh the
base classifier you need what densities
do we need We need py and p of x given
y See we dont have access to p of y
given x at all because our data does not
come like that
We have access to samples of py
Why Suppose you are solving a
classification problem We have access
to samples of py or samples that have
been drawn according to density py Why
Because it only tells you given a
population how many of them are diseased
or non d disease Thats what py is Do
we have access to p of xq data from p of
xq and y We do because if you take a
particular class then we have pixel
distributions associated with it We
also have samples from distribution pxy
because thats our data comma label pair
that we have or image comma label pair
that we have right so we dont have
access to px per se I mean you can say
you do have access to px because if you
combine all the images from both the
classes then that those are samples of
px thats how you can see right so
having all this you estimate these
densities and then build a base
classifier at the end of the day that
because if you have px given y and py
and px you can get P of Y given X
through B law Correct Thats what the
idea is Now from now on we at least for
couple of class we will look at
techniques for estimating density
functions
Now these density functions can be
anything It can be the class
conditional density It can be marginal
It can be it can be discrete It can be
continuous depending upon what the
underlying random variable is What Ill
do is Ill show you a a couple of
examples one uh of estimating the
density function for the case of a
continuous random variable and one for
the case of a discrete random variable
and then we will move on to these uh
class of uh density functions called the
mixture densities
So what these underlying densities are
from now on we dont care because it can
be anything it can be uh uh your x y or
depending upon what the problem is you
understand right so why do we need to
estimate densities because we want to
implement a base classifier is one way
to look at it or remember that even the
fundamental problem of machine learning
is to estimate the density you can
directly estimate p of y given x and so
on
are we clear so far any questions on
this yeah
uh
posterior why are we calling it
posterior why are we calling P of Y
given X a posterior is because its
having obs being observed what X is I
keep telling you right this conditioning
actually means that you are fixing the
data point or the input to a particular
point so having observed a particular
image now tell me what the class is that
is the question that Im asking so
thats why its posterior it is
conditional density right posterior
densities are always conditional
densities right So its a posterior
because having observed a particular
event that happens has happened what is
the class that we are looking at thats
it any other question So if we can
estimate pxy and we have px then we can
directly estimate p y g xy we going for
p y and px
 depends on see again the question is how
do we decide what densities do we
estimates we want p of y given x cant
we just use the conditionals and
marginalss and do it or marginals and uh
the joint densities to do it you can
depends upon how do you catch the
problem thats it I mean there is no
hard and fast rule on what densities do
you have to estimate it depends on the
ease but remember okay so there is one
other important point that I need to
make here is that most of these
techniques that we will see in the
rather 80 percent of this course are not
samplers
meaning they cannot give you know new
points from the underlying density
function in other words Im Im saying
these are not generative models
okay we are only concerned about
estimating the density or rather even
what do you mean by estimating the
density given a particular x and y a
value you need to be able to evaluate
that density function at that particular
point thats it we are interested in
evaluating the density function not in
sampling from the underlying density if
you if you want to sample from the
underlying density then we are looking
at generative models which we will see
maybe at the last part of the course a
bit of introduction but these are
estimators what do you mean by
estimators I want to evaluate the
density function at a given point in
time given given value Thats it Im
not interested in sampling as of now
Okay Okay So now lets look at general
techniques of density estimation Okay
Ive already told you that one technique
that well be looking at right now is u
what is called as the
maximum likelihood estimation We have
already seen what it is
maximum likelihood or minimum KL

So what is the problem given
Let me use a
different random variable here


 Given
running out of alphabets
lets take V Okay So v is equal to
have v sub 1 v sub 2
up to vn
sampled i from say pv which is unknown
The problem is to estimate v
estimate p v
Now you know that uh uh start with
p theta
and find theta by minimizing the the k
divergence between
pv and p theta Right This is what our
recipe is
already saw that this is with respect to
theta and we saw that this is
approximately equal to take the samples
and
maximize

sorry this
r maximize
this particular function what did we
call this
this is the log likelihood

 So all these visi are sampled ID from P
theta
Yeah remember that this is what this is
the optimization problem that well be
solving in maximum likelihood estimation
 P VPV
So this is our sample from PV
Here is our data Remember this is what
we did Ill show you two examples Ill
work out two examples in class uh one
for a continuous uh random variable and
one for a discrete random variable and
then well move on This is what we
should do Lets take examples examples
of ML estimation
The first one
lets say that uh
p theta
of v we assume this to be a gian
distribution
of uh

theta is what Im looking at lets let
me call this theta so theta is the mean
and the
variances identity Now lets say that V
is in RD
excuse me
V is in RD
and what we have are uh

we have samples V sub 1 V sub 2 up to VN
that are sampled ID from PV

This is the scenario So what we have
assumed is that we have assumed our
underlying density function to be a
gshian density with a mean
theta and variance we assume that it is
identity Now this is what is called as
a model
See always note that uh this p theta has
a direct connection with the hypothesis
function
If you look into this from the risk
minimization framework this the choice
of P theta that we make has a
relationship with the hypothesis
function because if you are building
base classifier then this this comes up
because lets say that we we assume P
the class conditional density to be P
theta whatever estimation that we do
then we plug into plug in that P theta
into the definition of H itself isnt it
you see what Im saying right and
therefore this P theta is exactly the
hypothesis function that we are choosing
and thats why its called model Okay
And in the initial uh couple of examples
we assume that this optimization problem
can be analytically solved
What does that mean That this function
can be differentiated
and uh if you put it to zero then you
will get an equation uh I mean you
youll get an expression in theta That
is what it means by analytically
solvable And after two examples I will
show you cases where uh this is not
analytically solvable You you need to
resort to numerical methods of solving
this optimization problem
Okay two examples Ill show you where
you can differentiate this and put to
zero so that you can analytically solve
this thing Optimization problem stays
the same but what changes is the way you
solve the optimization problem Some
problems can be analytically solved and
some problems cannot be Right So lets
look at this particular example
uh where we have assumed P theta to be a
gshian distribution and what is the
dimensionality of theta Can somebody
tell me quickly
 RD
 RD the theta is also in RD correct theta
remember that so we are dealing with a
a D parameter model
because its the mean right I mean a
dimensional Gaussian distribution well
have that So now rest is algebra Let
me just write it quickly So p
theta of v is equal to whats the
expression 1 by
2 pi to the power of d by 2
Now thats identity right So it is
sigma determinant of sigma power half
which is identity
correct So this will be determinant of
this matrix identity power half which is
1 Anyway I dont care about this term
because its constant E power
minus
quadratic form which is V minus
theta transpose
identity time V minus theta
and I hope that all of you are okay with
the dimensions right V is a dimensional
vector theta is a Dimensional vector and
its a quadratic form I dont have to
explain that So this is what the
expression is And uh uh now if I write
uh so consider
L of theta to be equal to 1 by N

I from 1 to N log of P theta of VI
Correct
This is what we need to maximize
this this function
I call this function as L theta
All right
This is what we need to do
And uh in this case this is equal to
1 by n

 I will actually go away
just trying to skip a lot of algebraic
steps and write the final expression So
what happens there is this 1 by n and uh
sigma the exponentiation and logarithm
will cancel with each other Theres a
minus that comes up here V minus theta
transpose into v minus theta is nom v
theta square Right This is I is I from
1 through N
Instead of writing equal Ill write
proportional because I skip the
constants Is equal to VI minus theta
Is this all right
This is correct
Now what I should do I have to find
theta star as the one that maximizes the
above expression
which implies if you differentiate that
and
put to zero See note that this is a
scalar because its n okay uh you can
differentiate scalers with respect to
vectors
if if theres a function that is a
scalar valued function of a vector then
you can differentiate that what do you
get you get gradient vectors
I mean Im sure that you all know this
right so you can take a scalar value
suppose theres a function from RD RD to
R you can differentiate that function
with respect to RD right a vector thats
what we need to because theta is an RD
vector
By the way uh there is a resource that
is available online Uh I dont know in
the age of GPT and all that its is it
even relevant Its called matrix
cookbook If you not used it its very
handy When we were students we were
using it But now with GPT its all
basically that lists the functional form
for derivatives of uh quadratic forms
and vectors matrix with respect I mean
derivatives of scar function with
respect to matrices and all that Its
pretty handy especially for this course
because well be differentiating the
expected loss function with respect to
matrices vectors and all that Okay So
thats this matrix cookbook is a little
handy But as I said
in todays age somebody is telling me
that they are not doing what they are
supposed to do because theres no
information they are lying
because information is available I was
reading a tweet recently where I said
the the biggest surprise of this life uh
right now today is that in spite of
having access to the entirety of the
knowledge that the human beings have
amassed uh in in in your hands people
still walk stupid on this planet
So the only explanation is that you
choose to be stupid You you choose to
be illinformed and then use that as an
excuse And nowadays you cannot say that
because I didnt have access to a course
or some piece of information that I
didnt do anything cuz its all
available anyway So point is
we need to now take the derivative of
this particular scalar with respect to
vector theta and if you differentiate
that and put to zero what happens Uh
Ill just skip the algebra So finally
you will get this optimizer as this
particular thing
Pink CLA Okay this is what it is
So this is the maximum likelihood
estimator
estimate
Please complete the algebra Its pretty
simple You might have done in your
matrix theory course right Take the
center put the I mean yeah see a lot of
blank faces what is this is actually
equal to vi minus theta transpose times vi
minus theta if you take the derivative
of this what will happen
 2 times vi minus theta its take the
derivative of this with respect to theta
this is what you are going to get put it
to zero and it theres this 1 by n term
and it will come out that way thats it
pretty simple
Now I mean
all this to realize that the maximum
likelihood estimate for the mean of a
distribution which is assumed to be
gajian is the sample average
See we first think that oh s I mean if
if you are given 10 samples and as you
are asked to give an estimate for the
mean what do you do
 Take a sample average and tell me why is
that a good thing is because of all this
math that we saw Its the minimum k
divergence estimate
Okay this is one example Let us look
at the other example Example two
Uh we will stop here and continue in the
next lecture
