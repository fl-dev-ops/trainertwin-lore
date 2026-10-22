---
id: 00DOOSYFyJA
title: Lec 48 Attention Part1
url: https://www.youtube.com/watch?v=00DOOSYFyJA
date: '2026-03-20'
duration: 23:31
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

speaker_1: Welcome everyone
In this lecture we will look at
another architecture that is often used
in the modern deep learning or machine
learning paradigms
which is called the transformer
Okay
Last time we looked at we started with
multi layer perceptrons or full
feedforward neural networks and then we
looked at convolutional neural networks
We also last in the in the last session
we looked at uh
uh
recurrent neural networks that were
which were the architectures designed
for sequence data processing
So continuing from there we will look at
uh
another set of architectures called
transformers that are based on this
idea called attention mechanism Well
look at what attention mechanism is and
then Ill look at transformers
In fact uh most of the models today
including the large language models are
primarily driven by this architecture
the transformer architecture

 Now before we dive deeper into what the
transformer architecture is uh I want
you to uh understand or appreciate a
couple of ideas
See if you recall
uh the way we looked at
kernel SVMs
which is that we started by saying that
the data is separable and there exists a
mm
linear decision boundary linear
separability and then we extended that
idea to the cases where there is no
linear separability Okay
Now what was the basic idea there The
idea was to project the data onto some
other space okay And uh
hope or assume that the data will become
linearly separable in that space
Okay Now this idea of projecting the
data I mean we have been doing this
since a long time right We have been
even when we did the looked at the
generalized linear regression we said
that the data that is not linearly
separable or are not explainable by a
linear model can be linearized
with a transform
And so there is some data you transform
it to it into some other space and you
expect different behavior post
transformation is what we have been
seeing So whats the idea Start with
data X So start with data space
and learn a transformation okay
Uh
fee to another space Z okay And then
you learn your hypothesis or functions
on Z This was one thing that we have
been doing correct
Now this
kind of transformation of data from one
space to the other okay Is typically
referred to as uh
representations
or embeddings
So start from some
space uh
which is the given random variable and
then make your data undergo a
transformation fee
and you get another you project your
data onto some other space typically
represented by this variable Z and call
that the representation or the embedding
and so on
We have already done this remember Uh
we had this fee to be a fixed
transformation
where it can be a polynomial projection
or some other projection and in the case
of uh
SVMs or kernel machines we saw that this
fee can be
different transformations We looked at
Gaussian transformations and the RBF
kernels and so on okay
Now so far most in most of the cases
that we have seen this fee which is the
function that transforms data from one
space to the other
has been fixed and user defined
I also gave you examples from the
classical signal processing community
for this right Fourier transform for
instance is one such
embedding learning
Given some data you transform it into
some other domain okay All the
classical transformations Fourier
transform Z transform etc are actually
learning this sort of a representation
Now if you carefully look at what we did
with neural networks okay
We had a composite function So we said
h of X
for a neural network
was started with some transformation
and then there is another transformation
and so on So this is what
we said a neural network is
Now this entire function right
The entire operation can be seen as some
non linear projection of data
from one space to the other
Isnt it In fact
each of the I mean because neural
network is a composite function every
inner function can be seen as one
projection of data So W1X is one
projection of data okay And then you
have W2 times that projection I mean
you project that projection onto some
other space and so on You keep doing
this
So every composition that we do can be
seen as embedding learning In that
sense a deep neural network is learning
embeddings in a hierarchical manner
So every layer of the neural network
will give you
a projection or an embedding of data
Do you see why
Because I mean what is an embedding
Its basically some function of data
some projection of data onto some other
space Then you start from the data
space and the first layer of the neural
network is some projection
And from there you project that it onto
a second layer onto a third layer and so
on So that way every layer in a deep
neural network can be seen as some
embedding that we are learning onto the
data
Do you see this
Okay In fact what is done then done is
in some of the applications you train a
neural network lets say for some task
Lets say that you train a neural
network for a classification task
What one can do is
during inference you take the data point
okay Pass it through the neural
network You tap the output of the
neural network from some intermediate
layer
And use that as a representation of data
and you can build another classifier on
top of those vectors
So this is what is called as embedding
embedding learning
So given a pre trained neural network as
it is called right Trained for some I
mean what do you mean by pre trained
neural network You have some neural
network and there is a
there is a
ERM that we have done So once we do the
ERM you can use that neural network and
use this neural network to get
projections of data by tapping onto the
intermediate representations from the
neural network
Do you see what Im saying Yeah
Uh
Okay This is also called
representations or embeddings Any
composite function for that matter can
be seen as
especially the neural network can be
seen as hierarchical representation or
embedding learning Okay
Now the difference between uh lets say
a kernel machine or an SVM and the
neural network is that in classical
frameworks such as transforms or even
SVMs we fix the transformation
But in a neural network
the transformation the function that
transforms the data is learned
And that depends on these parameters
isnt it
So that way a neural network can be seen
as a non linear basis change of basis
with learnable transformations
Thats why its powerful I mean instead
of I mean whats the difference between
lets say a Fourier transform and a deep
neural network is that in Fourier
transform you fix your basis onto which
you project your data
In the neural network the basis that is
projecting your the basis onto which the
data is being projected is being
learned
Okay Through parameters
Why am I saying this is because
most of the architectural changes or
designs that we do is an attempt towards
learning a better embedding or a better
representation isnt it
Because all architectures are all neural
networks now can be seen from this lens
that you are learning a projection of
data So any change that we do to the
architecture is learning a projection
onto the data
Does it make sense
I mean we need this worldview because
one it will its very easy to see a
transformer from from this angle that
all we are trying to do is to learn a a
particular type of a projection or an
embedding such that some behaviors are
imposed So now connect this with our
earlier discussion on Bayesian learning
as well
Every choice that we make on the
architecture okay Is
a certain type of regularization that we
are doing which in turn
impacts what sort of projection are we
learning on the data
Okay Thats what we are doing
Right Okay So now
lets look at
this idea called
uh attention mechanism
I Ill just give you an overview of this
and then Ill mathematically define
this
The idea of attention is as follows
Now recall that
if you have uh
sequential data where the the input is
sequence and output is a sequence
Okay We saw how to
handle the sequence to sequence uh task
using recurrent neural networks
Remember that So how did we do that
Suppose we have an input sequence X1 X2
up to XT
okay So we had these recurrent
neural networks
recurrent cells as we call them RNN
cells
And then
we tap the output in an auto regressive
manner
This was Y1 Y2 up to Y
T dash
So note that
T and T dash are different Meaning you
know the length of the input and the
output sequence need not be the same

 And because we are doing a parameter
sharing across time this is not an
issue at all You know we can easily do
that Okay So this is what we saw And
what was this This was HT
The T th latent representation or T th
hidden state Uh and the last time last
class uh
the a student made a very interesting
comment that
uh all the information about the input
sequence is now being enforced to be
embedded onto the last hidden state
And that is being
uh propagated through the output
generation And everything about the
input
the burden of
uh compressing all the information about
the input is put on one vector HT
Uh you told you you made that comment
last time right So which which may
not be a a great idea
So people saw this that okay this was
happening And to
ensure that
each of the output uh
vectors at all time frames actually is
looking at all the input time frames
So they defined they designed this
algorithm and they did they did they
defined they came up with this idea
called attention
Whats the idea mathematically
speaking
So this was H1 right This was H1 H2
up to HT They said Tap all of these
okay And
add them with a particular linear
combination
And give all of these as an input to
these things now
Understand
What we are saying is YT okay At every
time now becomes a function of
uh the previous Y of course okay And
also a linear combination of all the
hidden states
of the input
You see what is being done here
So you tap the hidden
uh representations from each of the time
steps in the input side Scale them with
alpha ones to alpha T And all these
alpha one to alpha T are learnable
Okay And then every at the the output
at every time step make it a function
of the previous output of course That
we have done by architecture Also the
the linear combination of all the
hidden states corresponding to the input
side
So now why was this made
This was made to ensure that uh the the
burden of
carrying the information all the
information about the input is not uh
laid only on the final hidden state but
you take into consideration all the
hidden states of the input and take a
linear combination of them and give it
as an input to uh the
the output uh transform output uh LSTMs
right And by the way I I gave a
a nomenclature also last time right
This part is typically called the
encoder and this part is called the
decoder So this is the encoder decoder
architecture where
uh you have you take all the input
tokens and compress it into a particular
hidden state and then decode it so to
speak
Now this is what is called as the
attention mechanism where
you attend I mean to all the input
hidden states
Im Im Im Im only giving you a
historical perspective of how this idea
was arrived at Uh we will look at I
mean the attention mechanism is very
similar attention mechanism that is used
in a transformer is very similar to this
idea but it stems from this particular
thing that instead of
uh burdening the last hidden state of
carrying all the information about the
input you take an inner linear
combination of all of the hidden states
and give it as an input to all the
outputs says the attention mechanism
This idea was there
Then people thought Why do you even
have an RNN You know because we know
that RNNs are bogged with this problem
of
the vanishing gradient or exploding
exploding gradient Despite the fact
that we have some uh hacks like uh the
the gating mechanism etc to ensure
that it does not happen but even then
the long context was still an issue
So people thought Why not do away
with the recurrent architecture
completely and come up with an
architecture that only has attention
Now after all what is this attention
doing If you look at what this
attention is doing it is trying to
capture the
the dependencies or the the interactions
between every token or every input time
step through these alphas and H
Now why not capture this completely
using only the attention mechanism and
completely do away with the recurrent
architecture was the question
Thats why the the research article or
the paper that
introduced this architecture is titled
as Attention is all you need
So what is not needed is that the
recurrent architecture is not needed
All you need is attention
Thats how they proposed this idea So
this is only a historical you know
account of how and why the attention
mechanism came So attention mechanism
is not was not proposed by this
transformer paper The idea was there
This was what was called as attention
But now
the contribution of that particular
research article was that they
completely gotten rid of got rid of the
recurrent architecture and found out an
architecture that can deal with the
sequence data without even having
parameter sharing across time and
recurrent architecture
Okay So this is only a historical
account of you know why and how this
thing was was was made Now let us look
at the math of what the actual
architecture is
Okay So now what are we given So let
me we work with a single data point So
given a data point
data point X
So please note that this is a single
data point which has T
uh time steps So now every XI is a
D dimensional vector
This is what is actually called as a
token
in the literature typically

 So we have T tokens which is one
sequence uh one
sequential data that we have Now the
objective
is to learn
a projection
or representation
that
encodes
the interaction between the tokens
This is the goal Now given this data
learn a projection fee okay Such that
the uh the the output of this projection
has to be in such a way that it tries to
capture the interactions between
every pair of token So that is what
the goal is
Now how do you accomplish this is the
question
Now start by representing let
capital X okay Be a matrix
which is uh

 in RT cross D
uh
having the data point
So now what I do is that uh I take this
data See this entire data point that I
have can be represented as a matrix
right
Because every
token is a D dimensional vector okay I
stack them all in a matrix and uh I get
a T cross D dimensional
uh matrix okay Which is a single data
point mind you So I have the single
data point Now I want to learn a
projection onto all
on this data point such that the
interaction between every token is
captured Thats my goal okay
Now lets now first define
linear projections
of X

 using
three
matrices
Lets do that Let Lets define a
projection Q
to be
X times WQ And this shall be
this we have T by D and this will be
uh D by
DQ

 And another projection X
times
WK
And
X times WV
Where
these three matrices
These are learnable learnable
projections
Now what am I doing is see please
remember the goal huh The goal is to
learn a projection or a representation
such that the interaction between the
tokens are
captured That is what our goal is huh
So towards that first we will define
three
projections of this data linear
projections of the of this data X or a
data point X
by our three learnable matrices WK W
Q and WV
Is this okay So these for now these
are simple uh these these are simply
projections of data okay onto some
linear uh subspace defined by WQ WK
WV See you you all of you know that
multiplying two matrices are equivalent
to taking uh the vectors in the column
of one matrix and projecting it onto the
space spanned by the other right
Im hoping that all of you know that
So from that angle
you take this the data points and
project onto the space spanned by
the columns of WQ and same thing happens
for all three correct Yeah So Q K
and V are now three projections of data
given by
I mean our projection onto the space
uh given by the the uh the columns of
these three matrices
Okay Thats what it is Okay
Now why are we doing this We are doing
this to
get to the point where uh we learn a
projection where the interactions are
captured
Is that all right Yeah Okay Now
I mean uh
I mean for ease of understanding right
I mean lets say that DQ DK and DV are
all same
Assume
See they need not be in the most
general treatment they need not be the
same I mean Im
avoiding writing three different and
just saying all of all of them are same
okay

 So lets lets assume these three are
same
Now
Okay
Now please note that uh
every row of these matrices okay Uh
corresponds to the projection of
one token in the data
The way we have defined these matrices
is that every row of the of of this
matrix is actually the projection of
a token of data onto the space spanned
by WQ isnt it
Why is that
Because look at this X
So X has T rows
okay and D columns So every row here
is one token and uh you take that row
and multiply with this WQ which means
that every row of Q
is projecting one token onto the space
spanned by WQ correct
Okay So now let us define what is
called as the attention vector
Okay
Uh we will stop here and continue in the
next lecture
