---
id: npYHSFuqnzs
title: Lec 41 Neural Networks and Universal Approximation Theorem
url: https://www.youtube.com/watch?v=npYHSFuqnzs
date: '2026-03-04'
duration: 30:42
model: youtube-captions (en-orig)
transcript: true
---

# Lec 41 Neural Networks and Universal Approximation Theorem

## Transcript


Okay welcome everyone We will continue
our discussions uh in this course
looking at different kinds of
classifiers We just finished uh max
margin classifiers and support vector
machines as an example for that And by
the way one side uh note that I wanted
to make is SVMs with slacks are also
called soft margin classifiers If you
see that word somewhere else I think
you know you just have to know that they
are the same thing SVM with slacks are
called soft margin classifiers
Now we will go on to uh another classes
of uh classifiers
uh or function approximators called
neural networks Now neural networks are
uh the todays go to choice for uh uh
classification regression and all kinds
of machine learning tasks Basically the
distribution estimation or empirical
risk minimization tasks
Now neural networks are versatile uh in
the sense that uh they can approximate
any function We will see that formally
in a while There is this very powerful
theorem called universal approximation
theorem We saw in our earlier
discussions that the choice of the
hypothesis class that we make is
critical when we are solving the
problem Right now the one suggestion
was to choose uh from the family of
functions that are expressive enough
Now expressivity depends I mean can be
defined in multiple ways and one way of
defining it is how good can it
approximate the underlying function or
underlying distribution what whatever
way you want to put it We als we
already saw one universal approximator
which was gian mixture models in terms
of density estimators But we saw that
the algorithm or the the iterative
algorithm that is used to uh estimate
the parameters may get stuck in local
optima which we do not want Now and
that is from a probabistic standpoint
From a erm standpoint one good choice
for universal approximators are these
class of functions called neural
networks Okay So we will look at
neural networks There are multiple
improvisations that have been made on a
simple neural network We will look at
uh a few
iterations of it Uh we will start from
what is called as a perceptron and then
well go to multi layer perceptron which
is also called a feed forward neural
network Then we look at convolutional
neural networks and recurrent neural
networks and of course the transformer
which is the the current golden standard
for machine learning Okay
Now what is a neural network So we we
still have the same problem uh of uh
empirical risk minimization Same and by
the way as we have been seeing in this
course these these hypothesis functions
are independent of the fact uh whether
you are solving a supervised problem or
an unsupervised problem because
ultimately youre estimating
distributions We all know that right
now
h theta of x is a neural network
So we we all have seen so lets say
lets define uh the data first So lets
say that x uh is in rd and y is in r for
uh convenience So h theta of x we know
that w transpose x
is a linear
decision boundary or or or a linear
function Lets say that we make it pass
through a nonlinearity sigma where the
sigma can be the usual sigma that we
have that we have seen in the case of um
logistic regressor or a logistic
classifier Now lets say that
that I take another weight matrix or
weight vector w2 and multiply that uh
with multiply the outcome of this uh
logistic sigmoid with another weight
Okay Now this I make sure that this
also passes through another sigmoid and
so on So now this becomes a composite
function So this thing is a
composition or composite function
 comprising
alternating
linear and nonlinearities
Right So what we are doing is take the
data
use a linear matrix and make it pass
through a linear uh transformation and
then apply a nonlinearity you get
another vector and then pass it through
another uh linear transformation and
then there is nonlinearity and keep
stacking it So this is called a neural
network This class of function is
called a neural network
Now
this sort of operation okay which is a
linear transformation of data
is often referred to as a
perceptron of course there is a
you can have a nonlinearity I mean this
nonlinearity can be
the sign of this
decide based on the sign of wrpose X
Right So what is it basically doing is
you are taking every dimension of data
and scaling it with a particular
scalar or rather weighting it with a
particular scaler and thats why people
notionally use W to denote the
parameters weights So waiting each
weighing each of the dimension data
dimensions and then deciding upon
deciding based on a linear combination
of different
uh dimensions of different features or
dimensions of data Right So this is
called a perceptron and this idea of
perceptron
was first proposed in 1960s So this is
not a new idea at all So this is this
has been around Okay
Now people thought that this has vague
connections with uh the way neurons
fire Im sure that
uh neural scientists neuroscientists do
do not agree with that But you know
there is vaguely the thing is
neurons fire based on the weights uh of
the features or the different kinds of
measurement it does I mean vaguely
people say that but again there is there
is no uh uh theres no proof uh so as so
so to speak on this but anyway so for us
its its a mathematical function so
this is called a single layer or a
perceptron where you take a linear
combination of data and and decide based
on the sign of it So earlier people
used to uh learn a perceptron So what
do you mean by learning a perceptron It
is know finding out this w not based on
erm but uh based on an algorithm called
perceptron learning algorithm where the
idea is very simple Now suppose you are
given a data set okay start initialize
with a particular w okay and take a data
point and see whether the given data
point is correctly classified or not
correctly classified If its correctly
classified leave W and move to the next
point If its not correctly classified
then you change your W by adding that
particular data point So please note
that the dimension of W and the data
point are same because the inner product
has to be uh between the vectors of same
data points You understood the
algorithm right If it makes a mistake
then add that particular data point So
basically there is a decision boundary
uh if it makes a mistake then tweak the
tilt the decision boundary which is and
the tilt is given by the magnitude of
this particular data point okay keep
doing it and iterate keep iterating over
data so theres a nice theorem that
would show that if the data is linearly
separable this particular algorithm
convert this in finite number of steps I
think this will be done in tutorials so
its a its a classical algorithm this
is called the perceptron learning
algorithm okay you understood the
algorithm right so the WT plus 1 is WT plus XT
where XT is the TH data point if it
makes a mistake
Okay And that plus can be you know
minus XT depending upon whether its it
it has come up I mean the decision is
based on the sign if its above then
its plus and if its below then its
minus What can be shown is if the data
is linearly separable then this
particular algorithm convert this in
finite step which will be done in
tutorials Please have a look at it
This is perceptron learning algorithm
See however this perceptron is limited
only to linear separability and also it
does not approximate all functions So
people moved uh away from perceptron and
then uh they came up with this idea
called a multi layer perceptron
MLP
is also called a feed forward neural
network or fully connected neural
network as it is called Okay So what
is the idea So here it was wrpose X
decide based on the sign in a
multi layer perceptron you start with
some W1 Okay So this is W1 times X
Okay So instead of having a sign so you
have a sigma
Now if W1 uh okay lets lets do that
once So lets say that X is in RD
and Y is in RK
the most general setting Now now here
W1
W1 is a matrix of size So this is uh
lets lets write it as W1 itself So
this is dx1
and this should be
l1 by d
correct Yeah X is DX1 and if W1 is L1
by D
and uh the sigma that we do is element
wise then this will be of dimensions
its an L1 length vector correct now
Ill have another W2 which is a matrix
now W2 is a matrix of dimensions are
L2 cross L1
right so we get a L2 dimensional vector
okay and then I will do another
element wise uh nonlinearity
Okay Then uh lets say that we have
another W3 here and W3 can be
R L2 cross K right So that you finally
get a
H So here theta is W1
and W2 and W3
Is this all right This is how you
construct a neural network So this is a
three layer neural network
But Ive heard about deep neural
networks right the number of layers
that you have every W is called a
layer Okay And number of Ws you have
uh is called the depth of the neural
network
Okay So this is the most general case
Suppose you want your uh uh the output
to be a to be for a classification
problem then you have to have a soft max
after this w3 You understand So itll
become a klength one hot vector
And if you are solving a regression
problem you stop here at W3 and so on
Okay So sigma here is
so element wise
nonlinearity
So one example of this can be sigma of
t is 1 by 1 plus e power minus This is one
one example of a sigma and well see
multiple examples as we go later uh
further in the course any questions on
this the construction of a neural
network
I mean the number of elements in all
these Ws are called the parameters you
have here how many parameters do we have
l1 times d times l2 times plus l2 times l1 plus l2 l2 times
k correct so these many number of
parameters is what we have this is a
multi layer perceptron or a feed forward
neural network or a fully connected
neural network and so on why is it
called a fully connected neural network
Well get to know that in a while Okay
Any questions on this Yeah
 Did not make any of such statements It
is just a composition composite function
of data Thats it You know which
involves linearity and nonlinear
transformations I did not say what does
it effectively capture or anything
 You cant say anything about it You
know we know what it is right It is
just a hypothesis function when we do
erm we are minimizing the empirical risk
thats it we should stop there and we
have every theory that comes up right we
have the bias various de composition and
we know how the error distributes and so
on so yeah so its its a mathematical
construct what is more interesting is
the kind the theorem that I that Im
just going to talk about in a while yeah
but do you understand the mathematical
construct of what a deep neural network
is this is effectively what is actually
driving
AI Okay Yeah
 I told you right This is one example
Oh you mean every layer it can be Yes
it can be different in every layers but
typically it is chosen to be the same
for convenience Okay Uh people have
empirically found out that having
different nonline nonlinearities at
different layers uh does not lead to
gains in terms of uh performance Yeah
should be
 k L2 right Yeah because finally we
need a K dimensional vector Thanks
Anything else
Okay so lets move on now See why this
particular form right I mean this
seems arbitrary isnt it So you have
uh you have some linear transformation
of data then nonlinearity then linear
transformation Why I mean why should
this be so powerful is because of this
particular theorem okay which is called
uh this came in 1980s this this theorem
is called universal approximation
theorem Ill just state it without uh
the proof okay but lets write that
write that down so theres a theorem
called universal approximation theorem
It says let X
uh be a compact subset of Rn
can say
uh R D also
R is fine and
and lets say C of X denote
the space of
all
continuous functions
Continuous functions f from X to R
Im doing it by assuming that r I mean
the uh the domain or range is r can be
generalized to rk as well So then let
sigma
be a function from r to r
such that
uh
is bounded
continuous or differentiable
and
goes to
zero not minus one

asymtotically goes to one and zero at
both ends This is called an activation
function Okay Now you can choose
anything Uh it doesnt matter how it
behaves in in between And the example
that we just gave here has that
property right One end it goes to one
the other end goes to uh zero Okay
this is a function this way Then
for any
given target function
target function
f
that is there in the space of continuous
functions
and a threshold epsilon greater than
zero
There exists a
MLP
with a single hidden layer
with
n neurons
such that
by the way I I didnt define what a
neuron is So um if you look at this
this is a matrix right if you take one
of the columns of this matrix whats
happening is its multiplying
or scaling each of the feature
dimensions with w right and then uh
taking a sum of all of it right which is
wrppose x kind of operation and there
are how many of them here l1 of such
things here so every wrppose x operation
is called a neuron this thing is called
a neural network cuz you can write it
that way right so here this I I wrote it
in the vectorzed form write it as
scalers start from dimensional uh space
and then there is one neuron that would
do that would take one column of w and
multiply it with all x so write it as a
neuron theres another neuron that takes
the second column of w1 and multiplies
and scales and so on there are multiple
neurons and there is a network of all
these neurons and that thats thats why
the name neural network okay so now Here
were saying that uh there exists an MLP
with a hidden layer with one hidden
layer Okay just say instead of a
hidden layer say a single with a single
hidden hidden layer
with n neurons such that
the networks output f of x or well
write it as h theta h of x h of x is
given by
1 through n
we have uh
some uh beta
I times sigma
of
yeah W transpose X plus some bias P
satisfies
condition that uh the supreum of
the difference between this
subounded by epsilon for all x
square
beta and w are
parameters
So this is why neural networks are
powerful So what is this theorem
saying It is saying that
you take any continuous function Okay
you can choose a beta and W So what is
this This is actually a single hidden
layer neural network Why Look at this
This is wrpose X operation Theres
nonlinearity and there is another W
here I mean I I can actually write it
as just to be consistent with our
notations I can write this as W2 and
here W1 Thats also fine
Yeah So this is a single hidden layer
neural network I mean this thing So
this is called a hidden layer because
the output is hidden from the input
Right So the x is hidden from w2
Thats why its called a hidden layer
So its basically a neural network with
one layer
Now this theorem says that any
continuous function can be approximated
to arbitrary closeness Choose any
epsilon Okay with a single hidden
layer neural network by choosing this W1
and W2
Now please note that this theorem is not
guaranteeing that any learning algorithm
will get us to that W1 and W2 and it is
not even telling us that telling us how
many neurons should be there in the
hidden layer
In fact yeah
 the summation should be over
Yeah
I mean I wrote it in the vectorzed
forms right Hold on
 Huh No no no Its just Okay Ill
write this Its fine And its its all
vectors right Its fine But Ill have
to
 No I have to somehow bring this n let
me tell you So this W1
So W1 is a
R L1 cross D vector and matrix and W2 is
R
Yeah So we have uh output is one
right
Yeah
this is correct
Were assuming that uh the domain is R
here You see this is R So if its R
the output has to be in R So the
dimensions match Now
they do right W1 is X is R X is in
RD
So lets say X is in RD
If its in RD then uh D by1 W1 is
 L1 by D and this has to be
uh L2 cross not L1 it should be the
output should be
one dimensional
lets match the dimensions now
so
so there should be n uh uh layers in the
hidden no the the hidden layer right
The first layer has uh D and then you
have uh W2 The first dimension of W has
to be D right
This is lets write it down So this is
R D by 1 So this should be D by
N
right And this should be
we get an N dimensional vector This
should be
n by one
See Im assuming that my output is
one dimensional
 Oh this is W2 Sorry Sorry So this
should be
I was just matching this Hold on Uh
so this is W1
W12 It should be d by n So you get an
n dimensional
vector
It should be n by d Should I put a
transpose here
This is n by d This is n byd So you get
So you have n neurons in
the hidden layer Correct And this
should be
 1 by n Correct Yeah Should be 1 by n
Yeah
This is w2 Correct Yeah Now you have
a neural network that has n uh neurons
in the hidden layer Okay And this
theorem tells you that you can
approximate any function to arbitrary
closeness by this sort of a function
And uh if I mean as I said it is not
telling you how many neurons should be
there in the hidden layer Neither it is
guaranteeing that a learning algorithm
like erm will take you to those w1 and
w2 that will make this this difference
bounded by epsilon It is it is an
existential proof It is simply saying
that you can find a function that of
that sort Does that make sense Now the
question is while this theorem tells you
that all you need is a single hidden
layer neural network why are we looking
at deeper neural networks
Today we we we have deeper neural
networks right We dont have shallow
and wide neural networks We have no
we dont have u
yeah this is this is this is deep
 and this is shallow This is wide and
narrow Yeah So
so we dont have shallow and wide neural
networks We have deep and narrow neural
networks No
Okay
Let me write that So this is depth and
this is
this is what this is deep versus
shallow Correct And this is
or you want to call it wide and narrow
 this direction So what we have is deep
and narrow neural networks not shallow
and wide neural networks Why
 Not because of that reason It is purely
because of the computational
convenience See what people have found
out is that uh if you want to
approximate uh with ifro want to
approximate naturally occurring
functions with uh the neural networks
with limited width then you need a lot
of neurons in single layer Are you
people aware of this algorithm called
fast 4year transform Do you know what
the idea there is The idea is actually
this So the computations that you do in
one uh one layer so to speak right
Basically when you have composite
functions okay you can approximate a
complex function by having multiple
layers of compositions is what you can
show with lesser number of parameters
The same idea that is used in a fast
4year transform FFT kind of algorithms
is what the idea is However
theoretically speaking people have
demonstrated that whatever results you
can obtain with a deeper neural network
can be obtained using a shallow neural
network as well just that the number of
number of neurons in the particular
hidden layers have to be increased
Okay
Come again
 Theres no theorem This is all
empirical because theorem only tells you
that that all you need is a single
hidden layer
These are only empirical uh
observations And by the way do you
know the number of parameters that are
used in todays neural networks Theyre
of orders of billions Yeah So I I also
tell you I mean in a couple of classes
Ill tell you the two todays neural
networks uh how is the and by the way uh
the the particular functional form that
is used for this neural network is
referred to as architecture
So this is a three uh layer architecture
neural network and so on right see the
architecture that is used in todays
neural network we will see that as we
move on in the class but yeah so thats
the idea Yeah
 Mhm
 Good question The question
thats nominator So the question is if
you call this a three layer neural
network then the one that is used in
universal approximation theorem has to
be a two layer It is a two layer neural
network with single hidden layer This
is a threelayer neural network with two
hidden layers
This is just to save my face right
 So I can actually call it a
two neural neural network Depends upon
nominator Thats it Yeah good point
Okay so lets move on So now we will
use deep neural networks right See
one thing that is to be seen is how do
we perform an erm on this So finally
well have to start with a loss function
and then calculate the empirical risk
and then find out what the uh I mean
find find out an algorithm to find these
parameters Right Now how do we do this
is the question
We do it using gradient descent Okay
So lets look at uh erm on neural
networks
Uh we will stop here and continue in the
next lecture
