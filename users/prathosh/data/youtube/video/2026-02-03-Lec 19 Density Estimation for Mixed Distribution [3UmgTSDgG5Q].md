---
id: 3UmgTSDgG5Q
title: Lec 19 Density Estimation for Mixed Distribution
url: https://www.youtube.com/watch?v=3UmgTSDgG5Q
date: '2026-02-03'
duration: 20:40
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Lec 19 Density Estimation for Mixed Distribution

## Transcript

speaker_1: Welcome back So lets move on to
another interesting algorithm which is
density estimation
for our mixture distributions
See one important question is when we do
maximum likelihood estimation we will
start by assuming that our underlying
density has a particular functional
form We just saw one case where we
assume that to be a gshian density
Suppose our true density function okay
was like this
So this is our uh this is x which is our
random variable and this is the px which
is the density that we are trying to
estimate and uh Im writing it in one
dimensions because I only have a 2D
sheet to write typically this is the
densities that we are talking about is
in 10000 dimensional space and all that
I mean its in RD so lets say my
density was like this and lets say that
I start uh my ML estimation by assuming
that this the underlying density is a
gausian distribution
Now what are the what is the degree of
freedom that I have So Ive already
made a assumption on the functional form
of the underlying density which is that
its a gausian
Now I can only control amongst all
possible gausians that are out there
which gian will minimize the k
divergence between this
and the between itself and the the two
distribution that Im considering
Correct Now if I am assuming that the
the the underlying density is gshian
density no matter what I do I cannot
make my kale divergence lower why
because I can do I can place my mean
here and make my variance very large
this is one estimate
right the other estimate can be that oh
I will will fit this particular mode and
then do this
there do you see what Im saying none of
these estimates the other can be I can I
can make my gosh intensity here fit this
mode and then go here and so on See no
matter what I do my ML estimate will
not be good
Why
Because Ive made a bad model
assumption
See again giving an analogy I mean if
we if we take a parallel to the
empirical estimate minimization
framework lets say that we are looking
at a like a quadratic function that is
that is our underlying edge hypothesis
If I assume my h theta to be a line no
matter what I do I cannot get close to
the reality because Im constrained by
our by my model I made a B no matter
what the parameters of my model is going
to be If I start with a bad model
assumption then I cannot make my K
divergence arbitrary low Do you see the
point In general univariate
density functions are not good
estimators
Sorry not did I say univariate Not
unariate unimodal Unimodal density
functions are not good model choices
because mostly in practice the densities
uh that that that appear are not
unimodal Theyll be multimodal
Okay What do you mean What by the way
What is what do you mean by mode of a
density function Not defined It assume
that you people know it Its the point
where the derivative of the density
function vanishes
For gshian density theres only one
mode because thats the only point where
the density vanishes Derivative of the
density vanishes But if there is the
underlying density has multiple modes
then no matter what parameters you
choose okay over uh um
uh the ML estimate using the ML
estimate you are going to get a bad
estimate because the density assumption
itself is wrong I mean
wrong I mean I didnt say that I
theres theres no way that you can say
its right or wrong Its a its a bad
model in the sense that the kale
divergence when we compute between these
two itll be pretty large Okay So a
better model assumption has to be made
You had a question Yes
 No Did I even utter the word mixture of
gashian so far Im only saying that
this is not a mixture of gion These are
different gions All I said so far is
that if the underlying density has
multiple modes and you start with the
initial as if you make your P theta to
be a unimodal density then no matter
what ML estimation you do you are going
to get a very large KL This is my
statement Does it make sense Any
questions on this Okay
This is just to motivate that unimodal
distributions cannot be good models So
what do we do Yes
Good good point Yeah So what the
question that hes asking is the fact
that uh that uh uh the K divergence will
be large between the reality the true
distribution and the model distribution
will be large no matter what model we
assume Correct I agree But you can
compare two models No If you can make
a model assumption that will lead to a
lower kale compared to another model
you would always take the model that
leads to lower scale Here in this case
suppose your uh the underlying density
is multimodel No matter what you do uh
you cannot take a unimodel density and
make the kale divergent arbitral law
The question that we are asking now is
is there a better model
Is there a better model for the case
where the underlying density is
multimodel which is often the case
 It can over
did I say what overfitting is
not even uttered the word overfitting
yet Well well get to that Well get
to that Okay Is that okay So Im just
giving you another choice of a model So
right now we only have uh uh we have
only seen densities that are that are
unimodled Well give you a choice for a
density function that has multimodel
nature in I mean by construction thats
it okay so lets look at that example
uh
so multimodel densities
are not
well estimated
see when I say well estimated I only
mean in the sense of minimizing KL with
unimodel models
solution try a multimodal model When I
say model Im talking about the P theta
or the density that we are assuming
Right Now if you take a unimodal model
or density we only have choices
on their parameters So if you take
Gian distribution for instance you can
control where is it centered and what is
the spread
If you take a multimodel model right
then you can we can you can perhaps
control many other parameters Okay
Okay So now how do you define a
multimodal model How do you define a
multimodel density is the question So
one example is what is called as a
mixture density So now here if suppose
suppose uh v is a random variable
which is in RD
So we define a density define a mixture
density
as follows Now p theta on v is defined
as
1 through m alpha j
uh p notations its p theta j
evaluated at v okay Ill say j here
where we just define what these are so
where alpha js are
numbers between 0 and 1 and p theta j
is a density function Now this is
called a mixture density model where
the density function is taken to be a
linear combination In fact its a
convex combination as well see its a
linear combination of m other density
functions
You see this See Im not saying that
the value that the random variable takes
is a combination of something It has
nothing to do with the random variable
Im just saying that the density
function is a linear combination of M
other density functions
There are J density functions sorry M
density functions and you take a linear
combination of M density functions to
get the final density function This is
called a mixture density function
And uh do all of uh p theta j be of the
same functional form No not
necessarily It can have different
functional forms Meaning you can one
one of the densities can be gian the
other densities can be uh other density
can be exponential and so on But
typically it is ch it is chosen to be
homogeneous You take the same density
function and take and what is m here m
is the number of density functions that
you are combining Uh that is also a
knob that we can play with that is also
a model Its not a parameter Its
called a hyperparameter Because see
what is the difference between a
parameter and a hyperparameter
Parameters are the one that we find out
by solving the underlying optimization
problem Hyperparameters are the ones
that we just choose
Okay Without uh optimizing them
explicitly So here for instance the
number of mixtures that you would take
to construct the density model density
function uh the mixture model is a
hyperparameter
and the choices of the individual
densities that you make is also a
hyperparameter and so on Okay Ill be
using this term parameter and
hyperparameters So yeah you you
understood So there are see suppose you
choose uh one special case of this is
what is called as a gausian mixture
model
GMM where the individual densities are
all P theta J will be Gaussians
okay with the parameters theta J
So if you take J gshian densities and
take linear combinations for M gshian
densities and take linear combinations
of them then the underlying mixture
density is called a gausian mixture
density or gausian mixture model GMM
All right
Now uh you asked that question right
Isnt isnt uh uh isnt isnt it the
case that you take any underlying model
then it will not be arbitrarily close
But why do we choose mixture densities
like this especially the gshian mixer
densities is that there is this very
powerful theorem which Ill state
without proving okay as a matter of fact
is that GMM are universal density
approximators
You take a continuous random variable
you take any density function you can
always find a GM What does this mean
mathematically You know that epsilon
data definition for closeness of
functions right Im assuming that you
people know what it is
So take a density function which is
defined on a continuous random variable
can always find a gian mixture model
that would make the K divergence between
this GMM and the underlying density
arbitrarily close Thats what this
theorem is telling
Does it make sense So all Im saying is
that you can always find a GMM
Okay that will bring the K divergence
between the the the data or the the true
distribution and the model distribution
arbitrary closely if you execute it
well Is this okay This is the
statement Yeah Questions
Come again
I didnt get the questions Im all Im
saying is you can always find a GMM that
explains your data in the sense of
minimizing K divergence
 Huh
 Possible See but practically what do
we do The question is why do we choose
GMM is the question because at least we
know that the GMMs are universal density
approximators so that we can hope to to
to choose a GMM and get a K divergence
arbitrary clues the two lower values but
remember this there is no way on earth
that we actually measure the the true K
diver things that we are trying to
minimize because we dont have access to
to distribution at all
right So Ive still not answered this
question Right Suppose after you build
a model how do you evaluate it
I will I will answer that in the coming
classes But all Im saying is that if
you any anyway you are modeling you
start with a model that has better
capabilities and thats why you start
with GMs Thats it Yeah
 GM is powerful Why is it that
 Good question I thought somebody would
ask See the question that is being
asked is machine learning should end
with GMMs
because what else is there right You
know that the base classifier is optimal
and you know that the GMMs are universal
density approximators done given a
problem
learn a GMM get the parameters estimate
I mean put down a base classifier thats
it right its a very valid question in
fact I would have asked this question
myself the next after GMM are done so
the course should stop at GMMs right why
are we even going further Ill maybe
Ill take it later when when we complete
how to algorithmically learn solve the
problem I mean estimate GMMs parameters
but since you have asked around there is
something called curse of dimensionality
which Ill talk about
the idea is that these algorithm
theoretically what you said is correct
theoretically speaking if you can
estimate the parameters of GMM then then
its done but typically the space the
dimensionality of the space that we
operate in is very high right you saw
even if you take an image it is some
40000 50000 dimensional space and so
on in those kinds of dimensions the
algorithm that we will see right now
which we which is the standard algorithm
to find the parameters of the GMM will
get stuck to a local optima which is not
correct We well see that So there is
an algorithm called the expectation
maximization algorithm or EM is the
algorithm that we will use to its
actually maximum likelihood estimation
for GMM is EM So we cannot do it uh
iterative sorry analytically well have
to do it iteratively well construct an
algorithm
that would solve the maximum likelihood
estimation problem for a large class of
models of which GMM is a member So EM
is a generic algorithm that we will see
right now Its called the variational
um inference algorithm which we will
see uh see EM is a special case of
variational inference
and one other example of variational
inference is what is called as a
variational autoenccoder or also this
diffusion models which are currently
used to generate images with in these AI
models Same class of algorithms will be
applied to estimating parameters of GMM
and to build a variation autoenccoder
and to even generate that Gibli image
that you do today So we will see that
algorithm in the next class To your
point these algorithms are numerical
and there is this thing called curse of
dimensionality that would uh not let a
GMM uh maximize the likelihood or
minimize the K divergence in high
dimensional spaces and thats why it
does not stop there but its a great
question actually it should have been
theoretically yes given a problem
resort to base classifier and fit a GMM
and then you are done in fact the first
of your assignments will be this that
you will be asked to code up em that is
what well be well do
okay um so GMM are universal density
approximators and thats why they are
good models
of gausians
 uh you can take there are nonlinear
combinations of densities as well but uh
its like this the question is why only
linear combination of densities uh so
you can compare this with uh the 4year
transform or 4year series
In 4year series you take linear
combination of ss and cosiness
exponential functions to estimate any uh
periodic function to arbitrary
closeness Right What are these These
are basis functions
Right So if you if you have a vector
space and you need to you I mean if if
those basis vectors have to span the
entire space youll have to take linear
combinations of them Thats exactly the
thing So gshian densities because of
their infinite support nature form the
basis for the space of hilbert space
that con that that contain all density
functions Thats all Im saying
Look into gshian densities as basis
functions for the space of density
functions So you can take multiple gian
and take a linear combinations of them
and uh get to any density function in
the space of density functions Thats
it Just like you have the the
exponentials right in the fora series
case the goian density is excess So I
wanted to stop this class at one other
algebraic point leading to em algorithm
we can I extend by five more minutes
 Yeah just this class maybe Yeah So
what happens is uh when you write the
likelihood function for the density so
if suppose so p theta
maybe I just say this and do the algebra
next class because anyway Ill have to
do it next class what happens is if you
write down the log p theta which is the
likelihood function for the gshian
density see all this while what what was
happening we had log of some function
isnt it log of p theta if this p theta
comes from the family of exponential
densities then this logarithm and this
exponentiation gets canceled off and you
get a function in the random variable
and the parameter which could be
differentiated and put to zero But now
if you have a a mixture density instead
of having sum of logs youll get log of
sums
 cuz p theta involves a sum So log of
sum and uh and within that sum if you
have an exponent exponentiation this log
and that exponentiation will not cancel
out with each other and therefore if you
differentiate that put to zero you will
not get separated terms I mean terms
that are separated out in terms of
parameters of individual gshians
and therefore this optimization problem
cannot be solved if you have log of sums
instead of sum of logs
I I wanted to write that algebra but
its obvious right so p if p theta has
sum of
uh uh e e power exponential functions
then log of sum of some exponential
functions this log will not cancel it
out and therefore you cannot
differentiate and put to zero
Therefore we need to resort to a
numerical way of solving this which is
what the exponential expon expectation
maximization algorithm is all about
where the idea is to create a bound okay
lower bound on the objective function
and instead of optimizing the objective
function directly you iteratively
optimize the lower bound of the
objective function which is a likelihood
function this time well see that the
next why well look at the correctness
of that algorithm and also we will uh
see that algorithm working for GM okay
so this completes this particular class
please remember the overall story
because you know if you get deeper and
deeper into the algorithmic nuances it
seldom happens it often happens that you
remember whats happening we are
estimating density functions and why are
we estimating density functions because
we want to implement the base classifier
Okay Why should we implement the best
classifier Because we need to minimize
the risk and this is the best classifier
that we can implement Okay Okay See
you next class Thank you
