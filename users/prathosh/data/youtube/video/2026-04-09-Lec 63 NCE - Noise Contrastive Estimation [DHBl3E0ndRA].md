---
id: DHBl3E0ndRA
title: Lec 63 NCE - Noise Contrastive Estimation
url: https://www.youtube.com/watch?v=DHBl3E0ndRA
date: '2026-04-09'
duration: 41:01
model: youtube-captions (en-orig)
transcript: true
---

# Lec 63 NCE - Noise Contrastive Estimation

## Transcript


Welcome to this lecture So we were
looking at uh unsupervised
learning methods where the idea is to uh
estimate the marginal density of data uh
without having any labels We saw a few
methods to do that One was uh
clustering Okay uh where uh we group
the data or we group the data into u
clusters or sets of of uh uh unknown
labels to start with
and we saw that this can be seen as a
special case of learning a a latent
variable model with discrete latent
variables
Then we also saw a few examples of
learning
embeddings
or representations in an implicit way
using linear or nonlinear models like
neural networks If you use linear
models uh for learning embeddings one
of those methods is what is known as the
principal component analysis
which can also be used in fact which can
also be used for dimensionality
reduction
Now uh the if you look at the popular
literature
the moment people talk of PCA they say
that its a dimensionality reduction
technique So to me every unsupervised
learning method that has a latent space
can be used for dimensionality
reduction So in the PCF formulation
uh theres no hard and fast rule that we
have to restrict the uh the
dimensionality of the latent space to be
less than that of the data space You
can actually have it exactly the same as
the data space as well But uh a
byproduct is that you can reduce the
dimensionality of data right as a as a
byproduct And PCA is often used in that
context where you are given some data
and you want to reduce the
dimensionality of data PCA is use is
used for that particular purpose
We also saw that one can use techniques
such as autoenccoders
uh where theres a neural network and
there are two neural networks one called
the encoder neural network the other is
the decoder neural network See in
literature uh typically when we talk of
encoding encoder decoder architecture or
encoder decoder networks we
talk of a latent variable model Okay
And a neural network that projects uh
the data onto the latent space is
referred to as the encoder network
Okay And the neural network or any
function that takes the latent space and
projects back to the data space is
called the decoder network So this is
the standard nomomenclature across uh
different uh architectures and so on
Right Encoder is projections from the
the data space to the latent space and
decoding is projection from the latent
space to the data space back That is
why uh one side comment is we will see
this later uh in more detail
Decoders can also be seen as samplers
because the output of the decoder is a
sample from the data space
right and thats why you know you have
these terms which are called decoder
only models encoder decoder models and
so on So encoder decoder models are the
one where you have both the capabilities
uh meaning given data you can get an
embedding given an embedding you can get
the data so thats encoder and decoder
together so bird is one such uh
architecture where you have both encoder
and the decoder okay the decoder only
architecture is the one where uh you do
not have a projection from the data
space to the latent space but only from
a latent space to the data
Okay most of the modernday uh LLMs
large language models are decoder only
models We will see this when we look at
the generative models part Okay but
the general idea of unsupervised
learning uh in the encoder decoder
architecture that is that you have two
functions One which projects the data
space to the latent space Okay And the
one that that projects the latent space
back to the data space
So why do you use uh encoding Uh
encoding is used to used for multiple
purposes One is dimensionality
reduction
Right If you make the dimensionality of
the latent space to be less of less
compared to that of the data space then
post training you take any data point
pass it through the encoder get an
embedding or a representation which has
lesser dimension compared to the data
dimension So that is using encoder
network for dimensionality reduction
Okay The other reason that you would
want to use that is is for embedding or
feature extraction where you dont want
to uh deal with uh the entire data space
but you want uh to work on the work on a
represent representation or an embedding
space So you can use this as the
embedding space Okay The decoder
network is used typically for generation
or reconstruction
because you you uh start from the latent
space and get back to the data space
Now there are a few more nuances that
can be uh imposed on top of it and one
of you was act were actually asking the
question See we know how to regularize
No and these networks are not uh outside
the perview of regularization And you
can still regularize these neural
networks as well And we saw two types
of regularization Remember one
regularization was regularizing the
parameter space The other type of
regularization was that you can
regularize
the the outcome of the intermediate
layers of the neural network as well Do
you remember that Right So we can
regularize the output of the encoder
network
to follow a certain distribution
Do you see what I mean Suppose you know
here in the usual encoder decoder
architecture the um
distribution that this particular random
variable can take is not regularized in
the sense that this the distribution of
this Z can be anything
In fact what does it depend on What
does the distribution of Z depends on
It will it will depend on the parameters
of the encoder network The X is a
random variable and encoder is a
deterministic function Neural networks
are deterministic functions So when you
transform a random variable from one
space to the other its distribution
changes and it depends entirely on this
function that the encoder is imposing
Now if you want to control what
distribution that the Z is is taking I
can actually regularize
the Z by saying that look you encode the
data and reconstruct back but also
ensure that this Z follows a particular
distribution of my choice
So thats what the basic idea of this uh
this famous uh uh methodology called
variational autoenccoders So we will
see that So the idea the basically the
idea that I wanted to say is that you
can regularize uh uh an encoder decoder
architecture as well the unsupervised
learning architecture where you
constrain the distribution of the
intermediate representation to follow a
particular function that that can also
be done Okay Now we saw all this Now
we will go to a different paradigm of uh
uh unsupervised learning
where uh the problem is still the same
right So the problem is that given data
and my X is in RD
And I draw an ID
from PX
estimate VX
Okay this is the problem that we are
solving in uh unsupervised learning
Anyway now so so far how are we
estimating this px We are using the
same uh methodology of scale
minimization which is the maximum
likelihood estimation where we assume a
parametric form on px and then we use
whatever uh the uh standard
architectures are and then we find the
par estimate the parameters by
maximizing the likelihood But but the
question is in in some of the cases uh
some of the forms of p theta that we
assume on px maximum likelihood
estimation becomes interractable So we
already saw one example for that right
which is the mixture densities where we
had an em algorithm where we built
variational methods to do that but is
there another way to avoid maximum
likelihood altogether is the question
that the noise contrastive estimation uh
tries to answer
Now we also know that classification or
discriminant discrim disc discrimination
is an easier problem to solve than
estimating the uh marginalss
Estimating conditionals is easier than
estimating marginalss Why do you think
so
What do I what do I even mean by easier
See when you suppose you are solving a
classification problem right the
conditional density that we estimate
which is P of Y given X okay are direct
deltas no they are discrete discrete
densities so Im sorry they are not
direct deltas they are discrete
densities for a binary classification
problem its only one parameter that you
want to estimate finally because P of Y
given X can be quantified using one
parameter right so any classification
problem is compressing
Okay
the data space partitioning the data
space into discrete categories
which is easier Estimating the entire
marginal is difficult So what do I mean
by that Suppose you have a
classification problem Okay And your
data is in RD and you are solving a
binary classification problem Now as
long as all the data points that
correspond to a particular class are
collapsed and mapped into one label we
dont care okay whether
given particular points are completely
preserved when youre estimating the
density Do you see what I mean See
what does a classifier do Classifier
will separate the data space into
non over overlapping regions isnt it
Now as long as your data point is
identified to be belonging to the
correct region we dont care where the
data point is within that broad region
So this is learning a discriminant
function or a classifier But if you
want to estimate the marginal then it
does not suffice if you only say that
the data point is in in this particular
region Youll have to exactly say where
the data point is Otherwise youll be
confusing between two data points In a
in a in a classifier setting its okay
to confuse between two data points as
long as they are they belong to the
exact same class
Do you see why You see that right So
now that is why discriminative models
are easier to train than generative
models
In in other words estimating the
conditionals label conditionals is
easier than estimating the marginals
data marginalss
And you see why right geometrically all
we are asking is in in in the
conditional conditional density
estimation is that tell me whether this
data point belongs to a particular
region or not Okay But for the
marginal density estimation which is the
generative modeling well have to say
where exactly this data point is well
have to estimate the entire density So
thats the difficulty Now why did I say
that Now the question that the authors
of this paper asked is is there a way
okay that we convert the problem of
marginal density estimation into a
conditional density estimation problem
 because we know we know how to train
classifiers
Now can we catch the problem of
estimating the marginal density in this
situation which is unsupervised learning
problem Can we mod formulate that as a
classification problem and still end up
estimating PX is the question Okay so
lets write that down So thats the
exact uh uh objective of noise
contrastive estimation
Can
a classification framework
We used
to estimate
the marginal
Okay
Now as with any density estimation
technique so NC also starts by assuming
PX
belongs to a parametric for family of
densities P theta where theta are
parameters
Okay in in ML estimation
Now P theta
is estimated
by this
usual kale minimization technique
This is what we do right Right We
minimize the kale divergence between the
the true density and the parametric
density and this is all we have been
doing the entire course Now with noise
contrastive estimation we dont do this
So what do we do is the question right
So lets lets look at how it works
Okay
in NCE
assume
P theta to be of this particular form
Lets call that um
P theta ash divided by Z where
C is the
normalization constant
So assume your parametric density to be
having this particular form that there
is a function P theta dash and you
divide it by uh some normalization
constant So this p theta dash is a
function
which is from
RD to
R plus
Okay its any function that takes uh uh
that maps
from the data space to positive real
numbers But this is not a valid density
function because it does not integrate
to one Now p theta integrates to one
To ensure that p theta dash integrates
to one youll have to divide it by some
normalization constant
z Okay So what is z by the way
Its the integral of
p theta dash over
dx So whatever this function integrates
to divide that by uh
that constant and you will you will make
that a valid density function Now what
happens is by the way these are also
called uh see this form of uh assuming
the parametric density is pretty common
across multiple models
One family of models uh which uses this
sort of a uh parametric definition of
densities is what is called as energy
based models or EBMS
Okay where this P theta dash is also
called as the energy function So call
that as E theta So for for for those of
you who have studied some physics
right This is also called the Gibs
distribution
right So you call this as the negative
of energy and you say the more the
energy the less the probability of
finding a particle and vice versa
Right Typically what happens is when
you assume the density function to be of
this form finding of this normalization
constant becomes a big issue
Why is that Its because it involves an
integral over the entire data space
which is interactable
So now
noise contrastive estimation also gives
you a way to avoid estimating the
normalization constant
Okay Uh
if you take the maximum likelihood
estimation so suppose you assume P
theta to be of this particular form and
then do an ML estimate then Z comes up
everywhere in the estimator Now we will
see that in the noise contrastive
estimation as an estimator okay Z will
just disappear
So NC serves two purposes One in the
uh in the in the density models where
you have an intractable normalization
constant well have to get rid of the
normalization constant in the estimator
The second thing is well have to model
the marginal densities using a
classification approach So NC will
serve both these purposes
Thats the idea Okay So now we will
assume P theta to be P theta ash
divided by Z Uh and see what happens
now And and Ive been using this word
estimator all all the while Right So
what is an estimator I assuming that
you people know that suppose we have
what are we trying to do here We are
trying to estimate the underlying
density function So whatever function
of data that we look at okay uh which is
formulated to get an estimate of the
underlying density function is called an
estimator right so ML the maximum
likelihood estimator that we get which
the theta the p theta that we get by
solving this optimization problem right
is also an estimator its called the ML
estimator and we also saw map as an
estimator which is a basian estimator so
this is another type of estimator that
we are looking at for the density
function which is called the noise
contrastive estimator Okay Right So
let now lets with this with these
definitions we are ready to define what
it is Now
uh
in NCE
in addition to
PX
define another density function H
P N
which is not the same as PX
Take any arbitrary density function PN
Okay which is not the same as PX
PN because you can call this as the
noise
density
The name noise contrastive estimator is
coming from this particular this
particular density So this you call
this as noise because see what is noise
after all
Anything that is not music is noise
So what is music
Its its its very subjective right I
mean what can be music to you can be
noise to someone else and vice versa
always So here in the context whatever
we are having we are calling as data is
our data distribution px and whatever is
not the data distribution is the noise
distribution thats it So thats why I
said some distribution that is not the
same as px Okay So typically we make
some choices on pn thats okay but
theoretically speaking it can be some
density that is not the same as px
Okay Now um
sample
m points
so call it uh y1 y2
up to y
lets call this dd ddash
m points right yeah y
from pn
we have n data points we also sample n
data points m data points from PN
Okay this is what we have
Now lets denote
another another data set du as
u1 u2
up to u m plus n
as
the union of
d and ddash So I create an extended
data set by taking a union of x uh uh uh
the uh the samples of px and samples of
pn
Okay Ill tell you what the entire
story is and then well do the math So
what we will show right now is that if
you build a classifier
that would solve a binary classification
problem
with labels denoting whether a given
sample is coming from PX or PN
then that classifier estimates PX is
what we will show
You see that So all we are trying to
say is if you know how to differentiate
music from noise then you know what the
music is
right So if you know how to classify
between samples of PX and samples of PN
which is solving a binary classification
problem then that becomes an estimator
for the underlying density thats why
the name noise contrastive estimation
So this is estimation via contra a
contrastive learning
Okay What are you contrasting between
Youre contrasting between the samples
of data and samples of noise
Now you know that this is data and this
is noise only if you know what the
underlying density is
So makes philosophical sense also
right So you if you if you want to
learn a particular behavior youll have
to learn what this behavior is not
Thats thats exactly the point that is
what the rest is math We will show
mathematically that solving a binary
classification problem okay with these
as labels will lead us to an estimate on
px is what we will show Thats why the
name noise contrastive estimation It
its pretty amazing right Its very
simple We are not trying to maximize
the likelihood or anything All we are
trying to do is creating a pseudo
classification problem where youre
trying to discriminate between whether
its data or noise Okay
And if you do that you are effectively
learning what the underlying data
density is
Okay Well show we well show that now
mathematically So du is the union of
these two data sets uh u1 through um m
So now um lets assign
binary class label
uh lets call that uh uh C
J
such that CJ equal to
1 Let me write it here
equal to 1 If
uj
uh
is in d its equal to zero If uj is in
d what did we call it Ddash
Yeah this is how we label it Uh so now
we have we can create these labels right
we can create these labels because we
know what point uh what data point in
data set du belongs to x and what
belongs to n pn right so thats why we
can create these labels
now
consider
the Class conditional densities
So P of
U given
C equals 1
What is this equal to
So what is this The density of the data
points U given the class is one
should be px No So we actually well
call this well model this as uh p theta
 ash
the unnormalized as unnormalized
density
Okay then um hold on Should it be the
unnormalized density or the
should be normalized one right Its p
the p theta Yeah its p theta of x
and uh p u given c equals 0 What is this
This is pn Correct Yeah
Okay we also have what is this equal
to P of um
C equals 1 What is the prior here
The number of samples
 coming from uh the first class is
 N by N plus M Correct Yeah And then p of
c equals 0 is uh m by n plus n Correct
Okay
Now therefore use base law and write the
posterior of
this
Why do we need this Why do we need the
posterior Because remember in a binary
classification problem what do we do
We estimate P of Y given X Okay So
what is that We know from B law that
this is is equal to uh P theta divided
by P theta plus PN
Oh we also have the prior No itll
come here I think lets write write
that as new where where new is equal to
uh
m by n
Its okay No see it would be let just
tell you simple base law This should be
p theta times
n by n plus m and there will be an n by n
plus m term here and here there will be
an m plus m by n term So I divide
everything by whatever there is in the
numerator So an m byn term will remain
here
Do you see what Im saying
Simple base law All of you got this
No Okay I see a lot of blank faces
Let me do it again
Dont youre making me write down the
base law This is uh u given c equals 1 times p
of c equals 1 divided by
Is it okay Now P theta times N by M plus N
divided by
P N
 times
M by N plus M
 plus P theta times N by M plus N
Correct
Now what
 Huh
 Thats exactly what I wrote So this is
P theta divided by P theta plus new times PN is
equal to M by N
This is the posterior of
correct
and similarly the posterior of C equals 0
given U is
U times PN divided by
P theta plus
U times P N
Okay
Now
in maximum suppose we want to estimate P
of C equal to 1 given U What do we do
in a classification problem We maximize
the likelihood of P of Y given X So in
ML estimation
the objective
is to maximize
the likelihood of
the posterior
Okay Now if I have to light that
likelihood of the posterior
what is that equal to Its equal to
plus
uh this sum exist everywhere Uh 1 minus ci
 times
log of
This is the standard binary cross
entropy right So we want to uh
maximize the log likelihood or minimize
the negative of that log likelihood
Now if I uh plug in all the definitions
that I have written here for P of C
equal to 0 given U and P of 0 equal to
1 I can write this as
log of H theta of X Okay
plus
log of 1us
h theta of yi
where
h theta
is
1 by 1 plus u times e over
uh minus
just looking for a letter
Okay lets call that f theta
where
f s theta of x
is
log of
p theta of x minus
log of pn of okay lets call this as u
because weve been using
evaluated at this u
come again
whats the question
 this one is it yeah so this comes from
see uh our data set U here has y isnt
it whenever it is zero its coming from
ddash
 those are the noise samples okay so this
is the final uh estimator that we or the
loss function that we will use to
maximize the likelihood So what is
this Now we will look at this You look
at this expression Okay And if you see
h theta
as a function
that is taking from that is taking
samples from x and y and mapping it to a
real number Okay Then
this f theta of u okay uh or rather h
theta is a composite of this function f
theta okay which is uh uh estimating the
difference between the log likelihood of
these two and there is a sigmoid on top
of it
Okay Now suppose I model this f theta
of u using a neural network and then put
a sigmoid at the output of it What am I
trying to do is trying to classify
between the samples of U and X So look
at this expression right This
expression is nothing but the loss
function for a cross entropy uh I mean
its its exactly the binary cross
entropy for a binary classification
problem Now if I treat my h theta as a
neural network which has a softmax at
the output of it and then just solve a
classification problem by solving this
particular function then I will be
maximizing the likelihood of p theta of
y given x So what is the likelihood
that we just computed It is p of c
equal to 1 given u What is that Its
the likelihood of observing
the or the input data point coming from
the actual data set but not noise
Suppose I build a neural network okay
which would maximize this likelihood
What am I effectively doing is trying to
solve a binary classification problem
that would classify between the samples
of data X and samples of noise Y
Do you see why Because even in a neural
network suppose a neural network is
trying to solve a binary classification
problem What is it doing It is trying
to maximize the likelihood of the label
Y coming from class one Thats exactly
what this loss function is isnt it If
you look at this loss function what is
this doing This loss function is
saying What is the this is this is
nothing but binary cross entropy Can
all of you see this Yeah So what does
binary cross entropy say Binary cross
entropy is coming from maximizing the
likelihood of
the distribution of the Bernoli random
variable uh that signifies whether a
data point is coming from class one or
class 0 Thats it Okay So far what
did we show So far all that we showed
was that maximizing the likelihood
of
a random variable that would determine
whether a given point is coming from the
data or not is equivalent to solving a
binary classification problem that
would classify between the data and the
noise points That is what we have shown
so far All of you convinced Now there
is one final piece that is missing which
is that this loss function which is
maximizing the likelihood of observing
the data sample
estimates the underlying data density
Right That is not something that we
have shown which is exactly what we
want We will show that in a while Any
questions so far
that so far what we have done is given
data we constructed another sudo data
set and solved a binary classification
problem that would classify between the
the points from the data distribution
and points from the noise distribution
That is what we have seen so far Now we
have to show that this
uh loss function which is the cross
entropy
classifying between the samples of the
noise and the data will estimate the
underlying data density is what remains
to be shown which is what we will show
now h okay so lets move on to the main
result of uh the NC
go on yeah
 the sample of noise is like data
integrated with noise or it is pure
Yeah the question is how do you define
P PN right we will see there are
multiple ways to do it its most I mean
different empirical methods do it in
different ways so I I will Ill discuss
a few uh methods to do that okay now the
final NC estimator
uh we will stop here and continue in the
next lecture
