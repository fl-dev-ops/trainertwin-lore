---
id: 5sg3d8ObcDc
title: Lec 60 Un-Supervised Learning
url: https://www.youtube.com/watch?v=5sg3d8ObcDc
date: '2026-04-02'
duration: 20:43
model: youtube-captions (en-orig)
transcript: true
---

# Lec 60 Un-Supervised Learning

## Transcript


Welcome everyone to this course Now
lets go to the next paradigm in machine
learning which is called unsupervised
learning
See at the onset I should tell you that
Im not a big fan of uh these
nominatores Okay Uh but anyway so it
exists in some algorithms are
categorized under unsupervised learning
So Ill have to just talk about it that
way Uh now again
remember what we did in our very initial
classes
So we have samples drawn from an
underlying unknown distribution and we
are trying to estimate the underlying
distribution that problem remains So it
doesnt change Okay Now even for
generative models that problem remains
But there is one other
angle added to that problem that we also
need to sample from the underlying
distribution
So far none of the algorithms that we
have seen are capable of sampling So if
you train a neural network its only or
rather I should I should actually to be
mathematically completely precise these
algorithms are not designed to sample
from the marginal distribution They are
designed to sample from the conditional
that two conditions of conditionals of
labels given data whatever variable we
are calling it as label Have I
mentioned it to you I mean I I say this
always in my first class of generative
models that all models are generative
because even the so called
discriminative ones are sampling from P
of Y given X
right so anyway so I mean at typically
in the literature the ones that sample
from P of X given Y are what are called
as generative models right but the
problem of sampling from the underlying
distribution or rather estimating the
underlying distribution given its
samples does not change This is the the
one holy problem of ML that is common
across all problems that you encounter
in ML Okay Now then what is
unsupervised learning
To me it is still distributional
learning The only thing is right here
estimate the marginals are not
conditionals
So given
so D that is sampled from X I
So this is the foundational problem of
unsupervised learning
Go back to the philosophy of ML
If we can see one data dimension or
label as one other extra dimension of
data
right then the paradigm merges we this
you know we are not doing anything but
typically in supervised learning you
take away one dimension of data and
force that and call it as a label okay
unsupervised learning in English
language is label label free learning
but if if you take language of
mathematics it is still distributional
learning learning you estimate the
marginalss Thats it
Its not the conditionals
So that way you dont have labels You
see the the point is that you dont have
labels here But but you can debate what
labels mean You know I can always call
one of the dimensions or a few dimens
dimensions of data themselves as labels
right And estimate the conditions By
the way if I if I take a few dimensions
of data itself as labels okay and
estimate the conditionals or marginalss
people call it in a different name by a
different name its called self s
supervised learning We will see some
algorithms for that as well But
ultimately what we are doing is
distributional estimation given samples
Does it make sense
Now the question is what changes the
nothing changes actually you know we
still have the same KL minimization and
we still have the exact same erm that we
do okay but the so called loss functions
that we define
now remember in supervised learning the
K divergence that we were minimizing was
be between the true uh conditional and
the
 the model conditional uh
and this p theta of y given X we we uh
approximated this with multiple
parametric functions looked at linear
functions and nonlinear functions and
neural networks and whatn not ultimately
this is what this is this scale
divergence is what we call as loss
function right in the erm world if you
write down this k divergence it will
become a loss function
now in unsupervised learning the k
divergence that well be optimizing will
be the marginals between the true
marginal and the model marginal Thats
it
 Will it still be called the loss
function
 Yeah you still call it the loss
function right So what distribution do
you choose is very different Thats it
Okay so now here you dont have labels
Okay
this is one thing The other point that
I wanted to make is in most of the
uh unsupervised learning algorithms
right So P theta
theta of X which is the model
distribution
in unsupervised learning
So if someone asks you what unsupervised
learning algorithm is in some interview
or something please dont tell them that
it is estimating the margins through K
minimization and tell them that it is
learning without labels
Okay So model distribution in
unsupervised learning is taken to be
a latent variable model
This is the typical choice So typically
you make your P theta of X to be equal
to express that as
the marginal between the joint
distribution of P of X and Z where Z is
your
 latent variable
Okay this Z
okay we well come to that in a while
Is this clear When you see the problem
in unsupervised learning is to estimate
the marginal Okay express the marginal
as a latent variable model Either this
or this depending upon what the choice
of choice of your latent variable is
Express this that as a marginal over an
integral or the sum over the latent
variable
This is a typical choice Okay Now
the question is why do you want to
estimate the marginal of P of X
in unsupervised learning We can
understand right
we want uh the labels of data Finally
we want to predict the labels Now what
we want to do is infer which is
estimating P of you know P theta star of
Y given X test Thats what we need to
do Thats our inference in unsupervised
learning
What do we want to do Why do we need to
estimate the marginalss
So in one in one use case we we we would
want to estimate the marginal because we
want to sample from them
which becomes the generative models But
here we are not talking about the
sampling procedures yet We are only
talking about implicit estimation of the
marginalss Why do you want to estimate
the marginalss
 Some patterns
 Of course data reconstruction is one
thing The other thing is
 patterns
 What do you mean by that
 So from
 thats a good answer by the way but you
need to define what a pattern is
 How exactly it looks geometrically like
are the points like in a way clustered
in some way
 I mean Ive not defined what clustering
is and all that Right Anyway so okay
So they call it as data uh exploration
So you need to explore the data
Okay Why do you want to estimate the
marginalss Because you need to explore
the data So what do you mean by that
How how does it translate to
mathematically is the question Okay
Here is what my answer is Right
Typically it is modeled as a as a latent
variable because
now once
we have a latent variable model
we can estimate
P theta of Z given X
If we can estimate the marginal of data
as a latent variable using a latent
variable model Okay we can perhaps
estimate the posterior of the latent
variable conditioned on data
Okay Now why do we have to do this is
the question Now suppose Z is a
discrete variable
Suppose Z is a discrete random variable
Okay In that case what does this
posterior tell you for every X okay you
are getting a distribution over a
discrete random variable
now lets say that we take Z to be 10
its a discrete random variable okay and
how many choices that discrete random
variable sorry what I mean meant by Z to
be 10 is that its a discrete random
variable that can take 10 values with
certain probabilities okay now for every
data point X I get a
a distribution over 10 dimension a
discrete random variable So how do I
interpret that So one possible
interpretation is that Im grouping my
data into one of 10 categories
and this is what is called as
clustering
So clustering is nothing but estimating
the posterior of a latent variable
model The posterior of the latent
variable given data under the assumption
that the latent variable is discrete
So this makes sense This is called
clustering Okay So I dont understand
English I can only understand math
Do you see what what is happening So
now suppose we choose it to be a
discrete random variable and and
estimate a latent variable model Okay
And then estimate the posterior of the
latent variable given every data point
What you are actually doing is grouping
every data point into one of 10
categories using this latent variable
Now if you are getting the entire
distribution on a latent variable for a
given point how is it grouping it is
soft grouping
If you associate that data point to the
one which the maximum probability then
it is hard grouping So one is called
the hard clustering algorithm The other
is soft clustering algorithm We will
see examples for both of them
If you can
connect the dots we have already seen a
latent variable model earlier which is a
gian mixture model In a gian mixture
model we can actually find the speed
data of Z given X and thats why GMM is
used for clustering
Okay Now if Z is continuous
not discrete okay then estimating
samples of P theta of Z given X is
called representation learning or
feature extraction
because for every X okay in fact it it
is not you know you need to actually
strictly speaking you need to sample
from this distribution because for every
X you have to get one Z lets say that
we take that Z which corresponds to the
mean of this distribution the peak or
mode of this distribution then for every
X we are getting one Z that has the
pattern or the compress compressed
version of the data So these are called
feature this is called feature
extraction
So as a side fact I have named my
research laboratory as representation
laboratory you know one because rep lab
seems you know funky the other thing is
that all I want to do is do an
unsupervised learning learning without
labels is what Im interested in
right and what what is learning without
labels is try to learn a latent variable
model okay such that the
the posterior of the latent variable
given data gives you a good
representation of data Thats it Thats
why we have named our company also as
latent force because all we are trying
to do is to learn representations of
large scale data so that the downstream
task becomes easier So now how do you
use the Z is the question Okay fine
know you have you estimate the marginal
you get a Z Then what you can use that
with labels for your downstream tasks
instead of using an image
suppose you do some unsupervised
learning okay where you can estimate the
representation of the data point you can
use Z as vectors and then build a
classifier on top of it and so on
Got it In fact again you know a bit of
self marketing the one of the biggest
value propositions that we are doing in
our in our company right now is that we
provide very good Z such that your
downstream task is more efficient
Thats the story that we are seeing
Okay Please note that we are still not
talking of sampling We are still
talking of estimating the marginal and
getting the posterior of the latent
variable given data Okay Let me write
that down once Okay Now if Z is
discrete
then it will become clustering
If Z is continuous
this will become feature extraction or
representation learning
Oh by the way this has another name
These are called embeddings also
Embedding feature or representation
extraction right All of those are the
same things Okay
Any questions on this
When we have discrete variables
 we can see this also as a
representation
 Discrete representation is what is
called as clustering
Instead of seeing it as like grouping it
into one of them
we can have distinct lets say image of
few dimensions compressed into discrete
dimensions
 Agreed So but the thing is when you
have discrete representations all you
are saying is with with with probability
you know something it belongs to uh uh
this particular uh group with
probability See what happens is if you
choose Z to be continuous it may have
some implicit semantics embedded into it
because distance metrics etc will make
sense but if youre looking at discrete
spaces those values that these discrete
random variable take may not have any
embedded implicit semantics into it no
because youre looking at a discrete
space I mean you can look into a
discrete random variable as a one hot
vector at higher dimensional space right
because you can represent every discrete
random variable as a one hot vector in
that kind of a space distance metrics
dont make any sense at all So it is
mostly looked into as a grouping thing
But I agree with you Uh we can still
look into look into this as a feature
So given a data youre saying oh okay
you can represent each of the data point
using a long one hot vector
Okay In fact if you make it a one hot
vector then it becomes hard clustering
If you give the entire uh distribution
over Z then it becomes soft clustering
Thats what people refer to as
so when you when when you tell people
that you know youre doing unsupervised
learning theyre saying youre doing
clustering I mean what is clustering
Its basically estimating the assuming
that your marginal on px marginal on
your data is a latent variable model and
estimating and assuming that your
discrete your latent variable is
discrete and estimating the posture of
the latent variable given data This is
clustering
Yeah
 Thats a hyperparameter The number of
clusters and features are
hyperparameter Its exactly the same as
the number of goshian mixtures that you
choose in a GM
Thats exactly the same which is a
hyperparameter
Okay In fact in the coming classes we
will see that uh the so called K means
algorithm okay is a special case of
GMM with a certain assumption on the
variance of the individual gian that we
do We will see that
 its done
 Come again
 Its done in
 Oh good Yeah
he hes saying that it is completed in
tutorials already but Ill nevertheless
Ill mention that here Any other
questions on this
So
in the next classes what we will do is
we will look at a few representation
representative algorithms for
unsupervised learning Specifically Ill
talk about uh principal component
analysis
PCA which is again assuming that Z is
your Z is continuous okay and solving uh
a particular optimization problem and uh
under linear models
Okay Oh I should make I I should tell
you I I should I should I should make
another I should draw another uh uh
connection here See just like there is
a onetoone relationship between uh erms
view of uh uh supervised learning and
the probabilistic view of supervised
learning The exact same thing applies
here
For instance Ill talk of an algorithm
called principal component analysis that
makes a particular assumption on the
model and write writes a I mean or
computes a loss function and tries to
find a Z This is done in a completely
discrim uh
deterministic way not the probabilistic
way Now you one can show that doing PCA
is equivalent to minimizing the K
divergence with a particular assumption
on P theta of X
Okay exact same uh connections apply
See as I said no uh the principle wise
nothing has changed The only thing is
that we dont have the so called label
random variable here but the underlying
algorithms are the same So we will look
at principal component analysis and
well also look at I Ill talk about
this this class of algorithms called
autoenccoders
okay where instead of using a linear
model for uh uh for loss for the
underlying model you use a neural
network
okay and we will look at uh algorithms
such as uh GMM weve already seen that
we Ill talk about that as well uh the
other algorithms class of algorithm that
we Ill be talking about is these class
of algorithms called selfsupervised
learning which is again the same thing
but there you take some of the
dimensions of data See here
in so called unsupervised learning we
estimate the entire marginal In
self supervised learning we estimate a
conditional
The conditioning is over a few subset of
the data dimensions conditioned on the
entire data If we estimate some of the
subsets of data dimensions conditioned
on the entire data set then they are
called self supervised learning
algorithms
In supervised learning you take another
random variable call it label and
estimate P of Y given X In unsupervised
learning you estimate the marginal In
self s supervised learning you estimate
the conditional of a few dimensions of
data conditioned on the entire data
Thats exactly what is being done in you
know GPT etc I mean in GPT etc you
there is one way to train which is
called masked autoenccoding right where
you take some subset of data mask it and
try to rec reconstruct it back We will
look at all those kinds of algorithms in
the coming classes Okay any questions
on this Uh the overall philosophy of
what unsupervised learning is
it is learning without labels Okay so
on that note well stop today Well
meet you in the next class
