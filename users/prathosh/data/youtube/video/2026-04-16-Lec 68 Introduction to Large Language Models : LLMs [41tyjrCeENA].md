---
id: 41tyjrCeENA
title: Lec 68 Introduction to Large Language Models : LLMs
url: https://www.youtube.com/watch?v=41tyjrCeENA
date: '2026-04-16'
duration: 25:21
model: youtube-captions (en-orig)
transcript: true
---

## Transcript

Welcome everyone
So in this lecture uh
we will look at uh
auto regressive models So we are
discussing generative models so far
and looked at the adversarial networks
and variational autoencoders
Now in this series uh the last family
of models that well be looking at are
auto regressive models These are also
generative models
So these are the ones that are uh
powering the modern day LLMs large
language models mostly Okay
Uh there are another
family of models called state space
models uh which are an alternative to
auto regressive models Theyre not
mainstream yet in the sense that the
most of the production grade LLMs are
uh based on auto regressive models So
we will look at what auto regressive
models is in the first of the half of
the
half of the class
Uh in the later half well also look at
Ill introduce you to the idea of a
reinforcement learning so RL So
whats the broad idea of RL is
See RL is a topic uh which can be
taught as a full course uh one semester
but Ill just introduce you to RL as a
paradigm
Okay So auto regressive models
are defined this way So the topology
that we consider uh when we look at auto
regressive models is where the data is
sequential in nature
It doesnt have to be So we already
saw how to represent uh different data
topologies
as sequences right I mean you can you
can view uh a natural language uh
paragraph as a sequence You can also
view image as a sequence right So if
you take every patch and arrange them
then that becomes a sequence and so on
So assuming that the data is sequential
in nature uh auto regressive models
best fit into such a kind of a data
topology
Now uh
we do the analysis for a single data
point Lets say that you have one data
point that has uh
T number of tokens So you know
the terminology that we were using when
we looked at transformers as an
architecture right Uh holds true here
as well So every data point has
capital T number of tokens So every of
this token
is a D dimensional vector So you have
a D by T matrix Uh you can represent
every data point as a D by T T matrix
where you have capital T number of
vectors each of dimensions D
stacked into a series So that is one
data point Okay Examples are uh
uh
a natural language sentence and
multivariate time series and so on So
very where every word can be looked into
as one member of this of the sequence
Okay
Now the goal uh for any of the ML
problem is to estimate the underlying
distribution right And uh especially
for generative models we also want to
understand how to sample from the
distribution So an auto regressive
model would help do both So it will
help you model the underlying
distribution and also give a way to
sample from it
Yeah we have already seen this right
Solution is to parameterize PX using
some parametric family of distributions
P theta and learn the
parameters of P theta by optimizing the
general divergence measure This has
been the central theme of the entire
course that we have seen so far And of
course mathematically speaking you
take KL divergence uh and find out theta
star that would minimize the KL
divergence or equivalently maximize the
expected log likelihood So thats what
we wanted to do
So auto regressive models
See every model we have seen what a
model is right A choice that we make
to P theta is what we call as a model
So what sort of Thats why neural
network is a model A kernel machine is
a model and so on What is changed What
changes is this P theta correct Now
in auto regressive model this is how P
theta is written Now
P theta uh of
uh the entire sequence so which is a
single data point is given as the
product of these many conditional
distributions Okay Where each of the
conditional distribution
is a distribution over one time step
okay Conditioned on everything that is
before that particular time step See
the the notion of before or the temporal
notion of a sequentiality is only
notional
So what do I mean by that is that if
you take a sentence uh the words have a
temporal notion to it right I mean a
given word precedes a a particular word
and so on But if you take if you
express an image as a sequence then
there is no notion of temporal
sequentiality anyway But there is still
I mean you can if you consider
different patches as different tokens
you can see that you can say that one
patch is coming before the previous
patch or the current patch and so on
So there is the notion of sequentiality
is is is assumed to be in data
inherently So these distributions are
you know P theta of XT where it T XT
is the Tth token conditioned on
everything that is
occurring before T
Okay So now this is simply So what is
this This is simply the
chain rule of probability right You
have capital T number of random
variables then the joint distribution
of all those can be written in terms of
product of
multiple multiple conditionals where
you take the uh first random variable
condition it on everything that is
before that and so on So this is the
definition of what an auto regressive
model is
The name auto regression is coming from
the fact that
every random variable at a given
temporal uh step is being modeled as a
function of everything that occurs
before that in the same sequence
So it is regressing over itself So
thats why the name auto regression So
you can look into this as a as as
regressing over uh every
step of the uh sequence okay
Depending upon as a function of
everything that occurs before it
Okay this is the most general form of
an auto regressive model
And there are multiple examples of auto
regressive models There are classical
examples and you know neural examples
and so on Just state a few
One historical classical example of an
auto regressive model is what is called
as what is actually referred to as an
AR
Have you heard of these things called
ARMA model and so on Auto regressive
and moving average models and so on
right I mean comes in classical
control theory and signal processing
Where this is the definition right You
consider you uh express XT which is the
Tth token as simply a linear
combination of
all the tokens that are coming before
that
So where AIs are learnable model
parameters So this is how we represent
a
a classical auto regressive model okay
The And there are neural auto regressive
models where
each of these constituent distributions
here P theta of XT conditioned on X
everything that is before T every each
of those distributions are modeled using
neural networks
Okay So this is where neural language
models And by the way these are also
called language models This is auto
regressive model is is the go to choice
for language modeling because if you
are the underlying distribution
underlying data can be seen as natural
language and what youre actually
modeling is the the the underlying
language and thats why they are called
language models Okay Now neural
language models or neural AR models are
where these constituent distributions
are modeled using neural networks So
what do you mean by that There is an
MLP
MLP takes
all tokens uh till T as an input okay
And predicts the Tth token Thats it
So its simply an MLP that regresses
over the Tth token by taking every token
before the Tth token as an input
Do you see that So what happens is uh
the uh
the
tokens that go as an input to this
neural network changes at every uh time
step but thats okay I mean youre
simply regressing it on
the Tth token depending I mean based on
every observation that you have made
till the Tth token Thats a neural
language model In fact uh this was one
of the uh very early models of uh
language that used neural network I
think Yoshua Bengio and his colleagues
came up with this idea of neural
language models
Then people said that using an MLP for
this is not a great idea because the
sequentiality is is totally lost
because every token before T See if you
express all tokens before T uh as
random variables and as vectors and just
stack them all together and give it as
an input to an MLP the idea of
sequentiality is lost Because
it doesnt matter right I mean MLP
does not uh implicitly have this idea of
sequentiality So then people moved to
recurrent architectures okay Where P
theta of XT given X less than T is
modeled using RNNs
Right So now we know how to use an
RNN right So you this RNN takes
everything from X0 to X T minus one as
an input and what it predicts is XT the
Tth token So its a proper RNN So
then the sequence the idea of
sequentiality is still intact
Thats how the uh
uh
the field progressed So initially
they were all deterministic models and
then people moved to I mean there is
Okay I think before neural models
right Or maybe concurrently people
also looked at what are what are known
as uh
uh
Markov models for language models
Right Bigrams and trigrams and so on
where you model these distributions
using
Markov chains You know you say that
given uh X given given XT minus one the
dependence on XT is only on XT minus one
and every not not anything before it
So its a first order Markovian model
Those are called bigram trigram and so
on Bigram is dependence on the previous
two tokens Trigram is dependence on
three previous three tokens and so on
And then you take ML estimates for each
of the
uh individual uh distributions Thats
it So they are
bigram trigram language models Then
came neural language models Then people
started using recurrent neural models
LSTMs and so on
And then came I mean you you you know
all these problems right There is
parameter sharing across time and you
have LSTMs and you know all all that
you did in your second assignment and
you have the problem of vanishing
gradients and so on And then people
came up with this idea called attention
mechanism
Right So you have a very long
sequence and uh there is one the final
hidden state was burdened with
compressing all the information So
people said Why do you want to take
that final hidden state Why dont you
tap
uh the information from each of the
intermediate hidden states and take a
linear combination of it and give it to
the output Thats the idea of
attention right So you can have the
attention mechanism on top of an RNN We
saw all this
So then came this this this paper
right Attention is all you need
where the recurrent architecture was
completely taken off and a new
architecture called
transformers was introduced where you
only have attention mechanism followed
by MLP and so on So weve seen all
that Okay So now yeah so Ill skip
all this because we did this attention
mechanism and so on
Now
yeah
Assuming that we already know what
transformers are which we do now an
autoregressive generative model is where
the underlying probability distribution
for a sequence is still autoregressive
Okay However P theta of XT given X
uh less than T okay is modeled using a
transformer Thats it
So thats what
modern day LLMs are all about
Now they are autoregressive generative
models okay with
P theta being
estimated using or expressed using this
particular autoregressive
formula
and the individual uh distributions that
come into come come within this product
are modeled using transformers
Okay See by the way uh to be
technically precise any model that
adheres to this particular uh
mathematical formula is referred to as
an autoregressive model But you can use
transformers to express these
distributions And if you do I mean
thats what the the modern day LLMs do
Okay So large language models
are autoregressive models with P theta
of XT given X less than T being
expressed using transformers Thats it
Any questions so far
Theres Theres actually one question
that that that still lingers which Ive
not answered right How do you ensure
that
uh
a transformer
only regresses uh on the previous tokens
given a current token That we have not
seen right Yet
These are called causal transformers We
will Ill just talk about it in a while
I mean if if except for that question
if there is any other question Ill
take it now
Thats correct See the thing is but
these are implicit Most of the neural
architectures Yeah you know most of
the neural architectures are implicit in
the sense that you dont have an
external
parametric distribution that you assign
to and then estimate the parameters
unlike in lets say the the ML
estimation
So there you assume your P theta to be
a Gaussian distribution and then
estimate the parameter But in all the
all the
the non parametric implicit distribution
estimators like neural networks
you assume that the the distribution is
implicitly being modeled using the
neural network Thats it But
I mean as I mentioned in the last class
also right The moment you say that uh
the
uh the output the loss function is
lets say a cross entropy youre
assuming that the final the distribution
of the the final layer
uh
follows a Bernoulli distribution okay
whose parameter is what youre modeling
using this entire function called neural
network So that is anyway there
I mean of the distribution of the uh
random variable that you obtain at the
final layer of the neural network
Right So that thats what
Any other question
Okay Now well have to see how to use
transformers to model this P theta of XT
given X less than T right So as I
said given a data matrix denoted by
capital X So what is this data matrix
Arrange all of these uh
uh
tokens okay in a matrix So you have
uh capital T number of them and each of
them has dimensions D or DM
Okay So then uh we have this attention
mechanism right So as you we Im
assuming that all of we know this
right Compute the attention mechanism
And what does this attention mechanism
actually do
We see this attention mechanism as
a latent variable model as well Have I
told you this view
Attention The transformer is attention
mechanism is also a latent variable
view right Where you have linear
projections of data Given a data in X T
cross DM dimension it projects it onto
some other space which is T cross DV
dimensions okay And the Z is simply
given by


 this particular operation right
Softmax of QK transpose divided by uh
root of DK And uh yeah you get uh the
projections of data So thats what
this attention So what happens is
starting from a T cross DM matrix you
get a T cross DV matrix So its just
your data got projected onto a
particular space
uh which are defined by
these matrices the WQ WK and WB
matrices that we have seen
So then to ensure that
uh See right now
theres no causality here yet
Autoregressive models are causal by
construction What do you mean by that
The dependence of XT is only on
its previous tokens
Okay not the the future tokens So but
right now the way we have defined
transformers the causality is not
embedded onto the model right Its not
causal
So well have to ensure that the
causality will is embedded onto the
model So how do we do that Theres
something called causal masking or
causal attention Its a pretty simple
idea So to ensure that XT depends only
on the previous tokens and not on the
future tokens attention mechanism has
to be modified this way So define a
matrix of size T cross T There are T
number of tokens Define a matrix of
size T cross T and the IJ element of
this matrix uh is as follows If its
zero okay if uh J is less than or less
than or equal to I its its minus
infinity if its greater than I if J is
greater than I
Okay What do we do
Remember that the attention mechanism
after the uh the dot product between the
query and key values before you
multiply it with the
uh value vectors take the linear
combination youll have to
uh pass it through the softmax to ensure
that the values are bounded between zero
and one right Now before you pass it
through the softmax just add this
masking matrix
Now what does it do
Softmax has an exponentiation operation
to it right So M has zero for uh its
its its a diagonal matrix Can you see
that this is a diagonal matrix
Is it uh Sorry its a triangular
matrix Its a triangular matrix right
So because its a triangular matrix
whenever
uh
uh J is greater than I where the
dependence is on future
uh itll
pull all those values to zero because M
is uh minus infinity in those things
and E power minus infinity goes to zero
And for the other values it doesnt
just doesnt touch that This is called
causal attention mask So if you do
this then the uh the corresponding Zs
that we get by passing by by doing
causal attention are by construction
autoregressive
So by doing this you are modeling P
theta of XT given dependence is only now
on every T that is less than T
Does it make sense
Thats it Yeah
I mean I understood what you did there
mathematically but I dont understand
why adding M captures that causal
relationship uh causality relationship
that youre talking about
No it does not See all this M does is
that the dependence on XT is only on
everything that is coming before XT is
what it ensures Thats it So the uh
the the uh See there is no explicit
causal regularizer that we are putting
here We are only saying that XT can
only depend on everything before that
We The only regularization that we are
doing here is we are killing the
dependency of XT on everything that
occurs later
Correct And also remember that we have
positional embeddings here
Because we have positional embeddings
with a transformer uh we are explicitly
telling transformer what the
sequentiality is
You remember positional embeddings
right Otherwise even transformer does
not have the idea of what precedes what
and what succeeds what And we are
explicitly hardcoding it by adding the
positional embedding
Right So by this regularization what
we are doing is we are
stopping transformer from looking at
everything that comes after T Thats
it
What happened
Okay So we Did I talk of multi head
attention
Did I Okay So yeah So it is done
now And then we have fully connected
layer and so on And
uh yeah so finally this is how a
transformer looks This is just for the
sake of completeness
I think I have drawn this as well
right Yeah So this is how it is You
start with X and then there is you have
input embeddings to start with and then
we have multi head attention blocks and
then you have fully connected layers and
finally we have a linear and a softmax
layer And at every softmax softmax is
over the entire dictionary from which we
are getting our tokens So it will give
you a probability distribution over the
entire
dictionary
Right So now how did this become Yeah
so how do you train this You have a
sequence of tokens okay
X1 through XT and
we have assumed an auto regressive
formulation here okay And this comes
up because there is causality P theta
of XT given X less than T is taken to be
the output of the transformer at the Tth
token So what do you do is take a
sentence or any
sequence okay
Take any Tth token okay And give
everything till T as an input to the
transformer and predict the Rather you
take everything till T minus 1 and
predict the Tth token Thats it
So this is what is
famously
referred to as the next token prediction
task
Right You can see this as supervised
learning where the supervision is
on the next token
Do you see this But it is completely
unsupervised because there is no sense
of labels here Also its also
self supervised because the supervision
is coming from itself and so on Okay
This is how the GPTs and the Demises and
Clouds are trained I mean at the
the bare bones method So they train
these LLMs okay Using this sort of I
mean and and what This is This is what
it is no
You take X1 through XT minus 1 and
target tokens are taken to be the next
tokens and then simply use the
cross entropy because you are uh
its its a discrete distribution at the
output right Over the vocabulary
Typical vocabulary size will be of lets
say 1 or 2 million tokens Okay
And by the way a token is not a word
Ive told you already right I mean
they do this thing called byte pair
encoding and it can be subunits of
thing I mean especially in the case of
language And then its simply a
uh
an ERM on this architecture And this
also is implicitly a generative model
right Why Cuz during inference what
do you do Do the exact same thing
What do you give as input prompt is X1
through XT Then you predict the next
token Take that append and give the
entire thing to the next one and keep
predicting one after the other Thats
it Thats how the inference also
happens And now you know why its a
sampler also
These auto regressive models are also
samplers because
I hope all of you understood what Im
saying right During training you take
the sentences take till T minus 1
predict the Tth one and you have this
entropy loss and backpropagate Thats
it During inference there is an input
prompt okay That is your first T
tokens Predict the T plus 1
And then append it predict T plus 2
and keep doing it Thats it Thats the
way you do it in an LSTM Same thing
When do you stop by the way
Yeah theres a special token called
end of sentence token right Whenever
the model outputs EOS thats when you
stop
Theres no next sentence Come again
End of sentence is not literally the
English No no I end of response
right Thats what it means So you
stop there and then give the next prompt
and so on So its pretty amazing and
you know
both amazing and disturbing
that uh
a technique that is mathematically as
simple as this and elegant could
actually crack intelligence
So theres nothing much to what I mean
of course Im simplifying Theres
theres
you will have to ensure that the models
align with human preferences and so on
Thats where we have RL that we do But
the pre training
model pre training as it is called
right Unsupervised pre training is just
this
And today
it is done on done for done over months
So people take 6 to 8 months to do this
training on pretty much the entire
internet
Okay And the underlying models are
transformers
which have billions of parameters or
rather trillions of parameters
So this is a nice
end to the course in the sense that I
mean
whatever we learned is just this right
So you have
data given from an underlying
distribution You have to model the
distribution and learn to sample from
it
And then you assume some model on top of
it and then minimize the KL divergence
and do that using gradient descent
Thats all That is all which is
happening Okay And of course you need
to regularize it so that it doesnt
overfit and so on But
yeah its its
its maybe its disappointing in the
sense that this is all it takes to crack
human intelligence
Okay But thats thats what is
happening So that is what the
pre training of all transformer models
are

 Any questions here
These are large language models by the
way These are LLMs
Uh we will stop here and continue in the
next lecture
