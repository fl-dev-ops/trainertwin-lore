---
id: 8LAKmtw0WvQ
title: "Lec 67 Variational Auto Encoders : VAEs"
url: https://www.youtube.com/watch?v=8LAKmtw0WvQ
date: '2026-04-16'
duration: 42:05
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

speaker_1: Yeah welcome
We will continue our discussion on
generative models So last time we
looked at the
general principle of what generative
models are and looked at an example of
adversarial networks as generative
models
So today Ill continue that discussion
and introduce you to uh
some more rather couple of more ways to
look at generative modeling
One model that I wanted to talk about is
latent variable generative models um
of which variational autoencoder is a
member Thats thats a large family of
generative models In fact diffusion
models are uh
diffusion
probabilistic models are also called
denoising diffusion probabilistic
models right DDPMs So they are also
a member of this family Flow based
models okay Normalized flows are also
latent variable generative models and so
on But in this course were only
looking at an introduction of what a
latent variable generative model is and
give one example of it which is VAE
Ill also talk about the autoregressive
generative models
of which the LLMs large language models
are a family are a member Uh
and all the
AI chatbots and you know the LLMs that
you see today are autoregressive
language models autoregressive
generative models So we look at
examples for the these two families
So we already saw what a latent
variable model is right We start with
data
which are end rows
from an unknown distribution
So the goal is to sample
So estimate PX and sample from it
We saw the general principle in the last
class right Where you start from an
arbitrary random variable that you know
how to sample from and then uh
learn a deterministic function on top of
it and tweak the parameters of the
function such that a divergence measure
is minimized so that sampling from an
arbitrary random variable and doing a uh
function approximation rather uh passing
that sample from an arbitrary random
variable to a deterministic
deterministic function will finally
yield a sample from the distribution of
interest And we saw how to do it using
a dozy real learning
Now in uh latent variable models
recall what the uh model is right P
theta of X in a latent variable model is
uh the marginal of the joint
distribution You assume that there
exists
a hidden or an unobserved random
variable called the latent variable and
uh
is the uh you express the marginal of
the data as
uh an integral or a sum over the joint
distribution of the data and the random
variable uh the latent variable
Now
by construction so what a latent
variable model gives you is that itll a
latent variable model
so imbibes
the generative property by construction
So what do I mean by that So a latent
variable model once you uh
fit a latent variable model to a
particular data can estimate
distribution such as P theta of
Z given X
right And P theta of x given z
and p theta of
x
So now this
is the embedding extraction
See once you have a latent variable
model
given a data point if you estimate the
posterior of the latent variable given
data that becomes a feature or
embedding We already saw examples for
this right If x is discrete then
clustering is exactly this
Okay So I didnt talk of this
particular distribution yet right
Which is the distribution of the data
given latent variable If you can sample
from this distribution this is
sampling
I can say this as conditional sampling
Conditioned on
a latent variable model uh latent
variable value z I can now sample from
p x So this becomes a sampler
Now a latent variable model if you put
it uh right then it can serve both as
an embedding extractor and a generative
model
Okay This did not happen with uh
adversarial networks for instance for
instance right So it can sample from
the distribution but given a particular
data point it cannot give you
embeddings
Right But
a latent variable generative model can
do both Uh it can given a data point
it can give you the embedding Given a
sample from the latent space it can
generate a new data point Okay
Now we already have seen an example for
this So uh
in this sense what can be seen is a
latent variable model can be seen in
this light
What it typically does is starts from
the data space and
learns a projection to the latent space
And from the latent space it gets back
to the data space
Okay So this is
p theta of x Z
and this is
P theta of
Z given X
Sorry its the other way around Yeah
its the other way around
So yeah given X it will give you a Z
Uh given Z this will give you an X
Hold on right So typically uh this is
called the encoder and this is called
the decoder
Starting from the data space you project
to the latent space as the encoder
function
Encoder function from a probabilistic
standpoint is the estimator of this
posterior of the latent variable given
data The decoder function is always uh
the estimator of the distribution of
data given the latent variable So
these are latent variable models are
therefore encoder decoder models
Okay
Questions You had a question on this
Yeah I have a general question about
the
space distribution
Every embedding we have like projecting
the data onto a latent space
Mhm So in that case the distribution
of the data is changing
Of course yeah So are we
getting the embeddings which have a
different distribution than the from the
data itself Yeah thats uh thats
okay no Yeah that is correct The the
distribution of uh the uh the embeddings
is uh given by P theta of Z given X
Its a different distribution than data
See as long as
as long as the clustering properties
okay of the data is preserved in the
embedding space we are okay
Right So the question that you asked
is actually pretty profound in the sense
that all the latent variable generative
models ask this question So what
should be the ideal latent space that is
to be
embedded so that uh
desirable properties are in by one to
the latent space is a question that is
to be asked However as long as the
the separation of the data or rather
distribution of data not in the
probabilistic sense right In the
Suppose youre looking at classification
problem As long as and and its a 10
class 10 class classification problem
As long as those 10 classes gets
clustered in the latent space as well
We are okay about what the distribution
of the latent spaces right Its the
general way to look at it but the
question is very valid So what should
be the latent space See that
translates to how should I learn the
How should I learn the embeddings So
what should be me what should be the
underlying model itself Thats the
modeling question okay We will see one
example of that you know which is the
variational autoencoder right now where
a specific type of distribution is
imposed on the latent space for a
particular reason okay Well see that
What is it This is what in general a
latent variable model does
Now
uh if we as I said if we learn it well
then the decoder of the latent variable
okay So
the model so the encoder is is the
feature extractor
And decoder is always the sampler
or generator
This is the general convention Always
the encoder is feature extractor And
the decoder is the sampler

 And the auto regressive models that we
see later are decoder only models Even
GAN for that matter is a decoder only
model because you only have
the sampling part not the feature ex
embedding extraction part You
understand So thats the you know
nomenclature There are encoder decoder
models There are encoder only models
See all the NCE based models are
encoder only models
Why
Cuz ultimately what you get is a
feature
So youre getting the Z Youre getting
Youre learning a transformation from
the data space to the latent space not
the other way around So there are
encoder only models okay
And there are encoder decoder models
which will give you both the embedding
and the generation And there are
decoder only models which are only
designed for generation but no
embedding extraction So we have seen
all kinds of models in this course
GAN is a
uh
decoder only model Its only a sampler
And the self supervised learning SimCLR
etc are only encoder only models And
there are encoder decoder models as
well and so on okay
Now let us look at an example of a
latent variable model being a generative
model right So example of latent
variable models
Latent variable generative models we
will see

 I want to talk about two examples
The first one is
something that we have already seen
which is the Gaussian
mixture model
See uh GMM is the uh simplest of latent
variable models Thats also a
generative model We never saw GMM as a
generative model so far correct
But since it is a latent variable model
it should be
uh generative as well So well have to
Well see how to uh use this as a
generative model
So we know that in a GMM what we do is
we model P theta of X as
The marginal The latent variable is
discrete here
And what is P theta of X given Z Its
P theta of X Sorry P theta of X and Z
is P theta of X given Z times P theta of
Z
And this is
in a GMM this is a normal
distribution right So with with a
particular mean
We have some alpha Z here
This is what the model is right So we
know how to uh
fit the model Okay so Im using this
word fitting the model I mean I
never used this word in this entire
course right So model fitting So
what is it
Its Its ERM is what we are talking
about or the
uh the divergence minimization is what
we are talking about Uh so once we
have a GMM that is there we have a P
theta okay So post ERM
or post ML estimation
theta star would be known
Uh What is theta star Theta star in
this case would be
set of alphas
from
J 1 to capital M if there are M mixtures
here
And we have uh uh M mus and M sigmas
right
Given data we know how to get these
So we have gotten this So now how do
we use this for generation So for
generative inference
this is how we do it First thing is
sample
sample Z from
P theta star Z
Okay then
sample X
conditionally from P theta star
X
given Z Let me call this uh
uh
Z cap
So given this Z cap well have to
sample from P theta star
X given Z cap
Thats it So now this becomes a
generative model
Let me give an example or rather uh walk
you through an example Lets say that
we are having MNIST data
Okay No labels
Take all MNIST data
and fit a GMM to it
Okay So you choose how many components
uh do you want Thats a hyperparameter
You fit a GMM okay using EM
Now once uh you have the parameters
what you should do is that you need to
first sample
Z from P theta of Z star What do you
mean by sampling Z cap from P theta of Z
star What sort of a distribution P
theta star of Z has
Discrete distribution Yeah its a
generalized discrete distribution
right Whatever we had done earlier
remember Its uh throwing a die
This is throwing an M faced die
Right So do we know how to sample from
this
We know how to sample from uniform
distributions Do we know how to sample
from a a discrete distribution of uh
of any given probability mass function
Please take it as a homework and do it
Here is the question
Thats one of the favorite interview
questions in in ML interviews right
So given that you know how to sample
from uniform distribution
okay Give an algorithm
to sample from a discrete distribution
of given probabilities
Ill give you P1 through PM That is
what we have given right Once we
estimate uh these alphas what are
alphas Alphas are nothing but the
probabilities of this discrete
distribution So given that we know how
to sample from the discrete
we know how to sample from a uniform
discrete random variable
Give me an algorithm to sample from any
discrete distribution with given
probabilities
Is it okay So do it Whats more
interesting is you can actually make it
an algorithm question
And try to make it logarithm complexity
So
do a brute force and see what the
complexity is and then you can make it
faster as well Okay And the hint is
you use inverse CDF method
Yeah So you should use the inverse CDF
method that we discussed the last time
That is how you do it Okay Now we
know how to sample from a discrete
random variable right Once we do it
if we do that what do we get In a GMM
in the context of GMM if we sample
sample from this discrete distribution
what we get is a
is a component So
once we sample we get one of the M
values
Once we get one of those M values the
underlying Gaussian distribution gets
fixed no
A GMM has M Gaussian distributions a
mixture of M Gaussian distributions So
once you get one value for Z one of the
Ms get fixed Then you just sample
from a Gaussian distribution Thats it
So this sampling will give you a a
point in D dimension which is an image
Right In fact
in in one of your assignments right I
would ask you to just uh fit us a GMM to
some data set and then sample If you do
that
you should get a new image right A new
image that is not there in the data set
Thats it This is as simple as it as
simple as it gets and this is how you
use GMM for sampling
Finally sampling from a GMM amounts to
sampling from a Gaussian distribution
But before you there are M Gaussian
distributions
before you choose what Gaussian
distribution to sample from you do a
discrete to to decide what Gaussian
distribution to sample from you first
sample from a
discrete distribution and then
conditioned on that you sample from that
particular Gaussian distribution Thats
it
Yeah thats how you use a GMM for
sampling and you can extend this for any
mixture variable mixture mixture model
right It need not be Gaussian mixtures
Can be any mixture model where you have
a discrete mixture you sample from it
and then sample from the underlying
distribution Thats it
Okay
Now let us
move on Now the problem with
a Gaussian mixture model is that recall
how we did EM for this
When we did EM for this
we assume that we know the
exact Q the variational distribution
that would make the elbow tight
What was that exact distribution It was
the posterior of latent given data
right What if
uh you have a model where the posterior
of the latent given day data is
intractable
So how do you solve a latent variable
model How do you fit a latent variable
model to data in that particular case is
the question
Okay Now not withstanding the math as
I said it is for the next course to do
This is exactly the question that is
asked in what is called as a variational
autoencoder
So it deals with a latent variable
model
where the posterior of
the latents given data is
intractable
See what happened in a in an Gaussian
mixture model or any mixture model with
a known conditional density is that this
was computable because we use Bayes
rule
Right This was proportional to P theta
of X given Z times P of Z and P theta of
X given Z had a known form so we could
get the posterior Thats what we do
during a EM isnt it But what if
I mean that makes the model uh very
restrictive because you know you you
should only choose uh the known
conditionals for the latent variable
model If you want to make it more
general what happens is the posterior
will be unknown So if the posterior is
unknown what do you do Is the
question
Okay
Now VI solves uh that question as
follows Um
Im not going to the details So what
happens is one thing to be done is you
recall we had uh a lower bound on the
evidence
So thats what we start with So the
elbow what did we call it Was F theta
of Q right
So what can be shown is that uh you can
create a
uh you can express the elbow in this
particular form Expectation of
log of P theta of X given Z
This distribution is with respect to Q Z
given X
Minus
the KL divergence between
Q Z given X
and PZ
I Ill start my next course with
deriving this particular equation Okay
thats what we start from So now take
it for granted You can rewrite the
elbow this way It requires a little bit
of algebra but you can get there
right So you can write it this way
Now note that this Q uh of Z given X
right Is the
variational posterior unknown
variational posterior
 Okay In the case of GMM what happened
was this was exactly known So what is
the optimal value for this variational
posterior This P theta of Z given X
But if you do not know how to estimate
this what do you do is the question
So what VAE does is as follows So in
VAE
so P theta of X given Z
and Q of Z given X
are represented using neural networks
Represented using parametric functions
okay Uh
In this case we use neural networks
okay
You ex
You express
the
conditional of data given latent and the
variational posterior of latent given
data both using neural networks
So what do you mean by representing a
distribution using neural network
No see there are two ways to look at
it okay
Now suppose theres a neural network
okay
That is representing a particular
distribution So it takes Lets say
that it takes X and what we want to
estimate is Q of Z given X
There are two ways to do it One you
make this neural network okay
Uh output a sample of Q of Z given X
This is what we do in our classifiers
What is a What does a classifier do
A classifier
estimates P of Y given X
Right Takes an X and gives you a sample
from P of Y given Actually it it it it
it ba it it it it It depends on what
sort of design choice you will take
Okay Now Ill tell you one is that
Ill complete the classifier story in a
while See one way to represent a
distribution using neural network is
that you design your neural network so
that it gives you a sample of the
distribution that you are trying to
estimate
Okay The other way to do it is you
design the neural network
to output
the parameters of the distribution that
you are trying to estimate
Okay Now Ill come back to the
classifier question So the classifier
Suppose you have a K class
classification problem you have a
softmax at the output What is it giving
you
Is it giving you a sample of Y or is it
giving you the parameters of the
distribution of P of Y given X
Its Its giving you the parameters of
distribution of P of Y given X Why is
that Because P of Y given X is a
discrete distribution that has
probabilities P1 to whatever PK if there
are K number of classes and it gives
you an entire distribution
Right What do you do with that
distribution You sample
from Y by taking the max or whatever
You have an entire distribution over Y
given a particular X
Do you see that Right
Suppose uh you put a Lets Lets say a
max function on top of uh the softmax
that you have
Okay Then that neural network will give
you a sample of Y not the distribution
Why Because it gives you a a one hot
vector which is a sample of Y
So think of the neural network as
it it first gives you parameters of uh
the the distribution that you want to uh
estimate and then you have some
sampling method that would give you the
sample Thats it So this max can be a
sampler Thats it Okay
Now uh uh
GANs right With the the generator in a
generative adversarial network
it
approximates a distribution right It
is estimating a distribution
representing a distribution Does it
give you parameters or samples
It is designed to give you samples not
the parameters of the distribution
You see what Im saying
Right So in a VAE uh
we estimate this distribution uh
by estimating its parameters So what
is assumed is you assume this Q of Z
given X okay
To be a Gaussian distribution or any
parametric distribution for that matter
with some parameters mu fee and sigma
fee
Okay And this neural network
will give you two vectors
which would serve as the parameters of
the
distribution that it is estimating
Do you see this
Right
Then you have another neural network
which is the
decoder neural network that would
estimate P theta of X given Z
Now what would this take as an input
It should take a sample
of
Z as an input and should give you a
sample of X Either it can give you a
sample from P theta of
X given Z or it could give you a
parameter of the distribution as well
Thats also a design choice So this is
the encoder of a VAE and this is the
decoder of a VAE because of the reasons
that we just saw right So latent
variable model
Now the question is where do you get
this Z from
Huh
Exactly So what you should do is that
you get your mu fee and sigma fee and
then sample from this Q of Z given X
Okay And then give the sample as an
input to the decoder
So now there is a sampling process
thats happening outside the neural
network
The entire
uh
data flow looks like this Take a sample
X pass it through the encoder get mu
fee and sigma fee use that to sample a
Z
in the parametric distribution Take
that sample pass it through the
decoder and get a sample of X This is
how the data flow happens in a VAE
Any questions on this
You need See you are You want to sample
from a Gaussian distribution right
To sample from a Gaussian distribution
you need to know the parameters of the
Gaussian distribution which is the mean
and variance Where are Where are you
getting it from
From the encoder So every time you
pass an X
you get a different mu and sigma
Use that mu and sigma and sample a point
from a Gaussian distribution with that
mu and sigma
You We know how to sample from a
Gaussian distribution right Uh So
then pass that Z sample to the decoder
Thats how the data flow is
Which mean of which distribution Q of Z
given X
It depends upon how do you model it
Thats a design choice In the case of
VAE
uh if you assume Q of Z given X to be a
Gaussian distribution then you can make
the output of the encoder to be giving
mean and variance of the distribution
Thats it
Got it Yeah
You dont ensure it You Lets Lets say
that you are You are operating Your
dimensions of Z okay is K Hold on
Dimension of Z is K right Then
uh if you assume the variance to be
diagonal then you make the output of
the neural network to have 2K
dimensions Take the first K dimension
to be the mean the next K dimension to
be the variance
Thats it Design wise that is how you
do it Now what is the question
So
my question was that
what we intend
is that at the end of the model we
should get 2K parameters which represent
the mean and variance of That is That is
That is enforced by design
Right If the question is what loss
function are using it is this
Still not told you how to
how to optimize this loss function with
this architecture Ill tell you that in
a while
Okay But
Question Yeah
So when we are using this latent
variable model for this
feature extraction will it not be
advantageous to use it to give a sample
from the distribution rather than the
parameters itself
Again depends
Okay the question is if we if we want
to use a a latent variable model for
embedding extraction why do you want to
model an encoder as parameters
modeler In instead of that you can
make it a
sampler right You can right But if
you See there are there are these
models called adversarial autoencoders
or even V vector quantized VAEs
VQ VAEs
So VQ VAEs do not give you parameters
They actually give you samples
themselves So there are such models
But making it a parameter
making it give parameters has its
advantages that sampling is easier that
way
Okay So these are questions that we
will actually address in the in the next
course when we when we do it
Yeah
When you use the decoder part for
generation
that time we are sampling the latent
Exactly So that is one of the reasons
Thats why I said no it enables
sampling So what happens is if you
make it give you samples rather than
parameters
during inference if you want to sam get
the data point
so you want to sample from the
distribution that the latent space is
learning So how do you do that In a
VQ VAE what is done is you fit another
generative model on post talk on that on
the latent distribution of latent space
That is one of the
additional step that you do You dont
You can avoid it by doing it is the
idea Okay
You can ignore that discussion
Uh did you understand what is happening
architecturally
Right Now what what should we do right
now is that well have to See
ultimately what we are trying to do is
put a latent variable in model which is
minimizing the KL divergence between P
theta of X and V X That is our thing
Right Our objective And we
showed that it cannot be done
it is not tractable Thats why we
computed a lower bound on it And this
is how the lower bound looks like Now
we have to optimize this particular loss
function using this architecture is what
we should do Right Lets do that
Question yeah
Go on Go on
Mhm
Yes
That you can do by you choosing the
activation function
By putting appropriate activation
functions at the output of this encoder
last K output of the encoders you can
do that
That is how it is enforced See any
kind of output enforcement that you
would do for a parameter neural network
is done using activation functions no
If you want it to be bounded between
zero and one put a softmax Or if you
want it to be continuous you put an R
Then R plus whatever whatever the kind
of activation function that you need at
the last layer you do it that way
Okay So now the question is this is
the objective function to train this uh
uh
VAE By the way this is what is a
variational autoencoder
Or a VAE So we have this
uh F theta
of Q phi
See note that this this encoder neural
network are parameters parameterized by
phi and decoder network is parameterized
by theta So we have two
distribution two parameters now two set
of parameters to be learned
Q fee and uh
P theta
Okay now what should we do is we should
find the derivative of this particular
uh
function elbow with respect to fee
and well have to do it with respect to
theta
Sorry
We need to do this right Because
ultimately we need to back propagate uh
this particular loss through both the
neural networks and do this
Now look at whats happening Theres a
problem with this The problem is that
this entire architecture
has a sampling process in between
Correct
How does that uh show up in math is that
you are trying to find an expectation of
some function with respect to a
distribution
and this distribution okay
is also parameterized by the same neural
network and theres a sampling that is
coming here
And sampling is a non differentiable
operation
You cannot differentiate through a
sampling process
So if you look at the sampling as a
black box
differentiating through sampling is not
possible
Right What do you do is the question
To do that uh the authors of VAE came
up with this idea called the
reparameterization trick
Where the idea is
express this particular
expectation
in terms of an expectation over another
arbitrary random variable that is not
dependent on fee
G of epsilon where
G of epsilon is a function
that takes
an arbitrary random variable epsilon
which is normal 01
and then transforms it to G space So
this is a known result in statistics
Okay Ill again Ill go to the details
in the next course The idea is
that you can transform one random
variable into the other via a
deterministic function that we know
right Construct a deterministic
function G such that
the random variable with respect to
which you need the expectation which is
QZ okay is represented using another
arbitrary random variable that is not
dependent on the parameters fee
Now you remove the dependence on Z from
this expectation is the idea of
reparameterization
Okay
Once you do that this entire loss
function becomes tractable What about
the second KL term
The second KL term see we have assumed
this to be Gaussian We also assume PZ
to be Gaussian
So KL divergence between two Gaussian
distributions is
uh have a
known closed form uh
solution for it
Okay So the first term becomes
differentiable through
reparameterization trick The second
term becomes differentiable because of
the distribution assumption that we have
made So the entire elbow now becomes
differentiable
The way to do it is
now take an X which is your data point
pass it through the encoder get a mu
and sigma Okay
And then sample a Z from this particular
distribution pass it through the
decoder get an X
Compute this first term
Okay Compute the second term and then
back propagate
the gradients with respect to theta and
then back propagate with respect to fee
and learn them jointly That is how our
VAE is trained
Okay The only I mean it is trained as
a as a as a
normal neural network The only
difference is that
the problem of differentiating through a
sampling step is overcome by using the
idea of transforming a random one random
variable to the other which is called
the reparameterization trick
Okay
Uh
Um
Im discussing at a surface level and
not going uh into the detail
deliberately because
this is a sort of trailer to my next
course and well well
well go into the mathematical details
of all of this uh when we start the
generative course Okay
Did you get the uh like overall idea of
whats happening here So its
basically elbow optimization okay For
the case where the
uh posterior of the latent variable
given data is not tractable
What you do is you estimate you
represent the variational distribution
and the data uh conditional using two
neural networks okay And then optimize
the elbow using reparameterization
trick So once the neural network is
trained
how do you use it during inference
You can use uh
uh VAE
in two ways You can use because its a
latent variable model you can use it
for
the the embedding extraction and you can
use it for generation as well Okay
Now how do you use it for the embedding
extraction Take the encoder
The trained encoder get a data point
pass it through it get a mu and sigma
Either you can use mu itself as the
feature for x
Right Did you note this as well
In this formulation for every data
point x we have a different
distribution on the latent space So we
get as many distribution on the latent
space as there are data points
So now post training if you give one
data point as an input to the encoder
you get
the mean and variance Either you can
use the mean itself as the embedding for
the data point or you use that mean and
variance sample a particular point from
q of z given x because you know what the
distribution is and use that as an
embedding That is also a possibility
People do both
So this is how you extract embeddings
from a VAE In fact improvisations of
this is what is called as VQ VAE and so
on vector quantized VAE which we will
discuss later
Is that
in fact the go to
latent variable models for images today
are VQ VAEs Those are the
state of the art embedding extractors
for images
You know what people do
They train a VQ VAE
on images
and get embeddings
Now build a generative models model on
embeddings not on the data space
For instance
you construct a diffusion model on the
latent space of the data that is
obtained by some VAE
Okay Then sample from the latent space
of that
of that particular generative model
from the generative model
Final data is rendered by passing that
latent space through the initial decoder
so that the user can consume it Do you
understand what the thing is
Build a
latent variable model first on given
data Okay
Use the encoder to extract embeddings
Now build a generative model on top of
embeddings
Why do you want to do that is because
data space is pretty large You dont
want to I mean building generative
models on top of it is too uh
compute heavy right So you build a
generative model on the latent space
Now finally you sample from the latent
space So you cannot display the latent
space right So you pass that
generated sample through the initial
decoder and then thats what you
display In fact when you ask all these
modern day LLMs to generate pictures
these days this is exactly whats
happening So they dont sample in the
data space
What they are doing is they have an
encoder customized encoder encoder
decoder model okay Which is
pre computed
A diffusion model mostly is trained on
the latent space that is imposed by a
encoder decoder model
And when you give a prompt the the the
generation is happening in the latent
space and then what is being displayed
is that latent variable being passed
through the decoder of the initial
encoder decoder model that was there
Makes sense right So thats how you
use the encoder of an VAE How do you
use the decoder Of course I already
told you right You can use you can
sample you can use the decoder as a
generative model or a sampler where you
take a sample from Q of Z given X pass
it through
the decoder you get a sample
uh that is not there in the data set
Got it
Diffusion model is simply another
sampler which we will not be discussing
now right
No no no
Its its an entire model right So
you just like we looked at GANs and
VAEs right Diffusion model is another
class of samplers Okay which is the
state of the art today So today the
uh the state of the art for image
generation is diffusion are diffusion
models
