---
id: UfiHgztGgu8
title: Lec 29 Generalized Least Squares (GLS)
url: https://www.youtube.com/watch?v=UfiHgztGgu8
date: '2026-02-18'
duration: 25:18
model: youtube-captions (en-orig)
transcript: true
---

# Lec 29 Generalized Least Squares (GLS)

## Transcript


Welcome back In the case of generalized
linear models here is the idea Now in
the knife linear model we assume that
the h theta or the hypothesis function
is a linear combination of different
dimensions of the data right Or uh the
the input features as they are called
Now why should they be a linear
combination of them They can be
quadratic combination of them
right For instance uh you take the
first dimension of data squared it
take the second dimension of data cube
it right And then then take a linear
combination of all of those dimensions
right Now cant this sort of a model
be be learned using uh the erm is the
question Of course you can do it where
your h theta so your h theta of x
in the linear case in the knife linear
case
h theta of x is theta 1 times the first
dimension
theta 2 times x2 and so on and we had theta
d times xd D
where
XJ is the J dimension of the data
So instead of that
instead of linear combinations
one can consider
nonlinear combinations as well and
linearize them
nonlinear combinations of data
dimensions
So what does this mean You have uh h
theta
now h theta of x is equal to so theta 1
 times the first dimension oh my god Ive
Ive used super supererscript for uh
this thing already right um
Yeah Yeah Thats what I was thinking
It looks a little complicated No So
this is lets say cube plus
theta 2 times the second dimension rise to
4 See it looks like x² to the of 4
You know please note that supererscript
is for the dimension and whatever comes
outside the parenthesis is the power
right and so on So this can be one way
to model it Now the question is how do
you do erm with
this sort of a uh framework So these
models are called generalized linear
models where
the above
case can be
represented
via premputed kernels
uh lets say precomputed
transformations
So what are these is that so given x
I define
uh xcap thats equal to some f times x
where
f is a
is a fixed
transformation or kernel
So lets call this transformation So
what do I mean by this
Lets say that I have x you know xcap
can be
uh the first dimension of x rise to two
plus the second dimension of that rise
to three
or yeah not plus Im sorry So this is
and the third dimension of this can be
lets say the first dimension squared
plus uh the second dimension
to the power of six and so on
You understand So where f of x you do
it dimension wise where you take the
first dimension and uh you know you
make it under go some transformation
see f1 of the first dimension and you
have you have f2 of the second dimension
and so on So you have see how many
transformations can we learn on data
dimensions thats a design choice
okay you can do it whatever right So
this in fact these transformations need
not be function of only one dimension
These can be function of multiple
dimensions of data as well You see what
Im saying So for instance no this the
third dimension of this particular
example in the transformation is a
function of the first and the second
dimension
You see what Im saying Right So this
is some function of uh the data
dimensions
Well just write it as data dimensions
just to make it general
Now what did we do This function f okay
is taking the data x and mapping it into
some other space xcap Now this x is in
RD
Okay And this can be in some RP
and FE the function FE right is is a
design choice and a user designed
userdefined design choice
Do you see what Im saying Lets say
that you are given data D Okay I
define transformations on the dimensions
of data using a precomputed fixed
function f
okay and transform my data from
dimensions to some other p dimensions so
this fee the function that is
transforming from d to p is something
that I choose
I meaning user would choose
now suppose you are given data x okay in
lets say uh two dimensions
Okay Or lets say one dimension Now
what Ill do is Ill define another xcap
as 1 x x²
right then the and then do erm using the
linearity of models Then whatever was
the linear model now becomes a quadratic
model But you are still doing solving
linear regression because you have
transformed data and the model is now
linear in the f space
not in the x space linear in xcap space
thats why the name generalized linear
model Ill take questions in a while so
you define this and then subsequently
solve
erm H
with a linear model
with a model
linear in
FX space
What happens is given D
Okay Uh compute
so transformed data first
Lets call it dcap which is equal to
f of x comma yi
Note that the distri underlying
distribution would change in this case
because what we are doing from a
probabilistic standpoint is that we are
transforming the random variable from
one space to the other which means the
distribution would change but we dont
care here because we are solving here
right so this is uh now uh f of x i
is now in rp and y does not change it is
still in r okay and then what you do is
Find uh
theta is already taken No theta cap
star as
argan by theta cap
1 by n
This is now f of x i
transpose
theta cap Writing it as theta transpose
x No So well write it as theta
cap transpose
f of x i minus yi
You solve this problem And now this
will be equal to
where
this V matrix is
Now instead of stacking X as columns now
you stack
This is the
Dth dimension
See as I said no it Im actually
overloading the notation a little This
all these dimensions of fe need not be
functions of one dimension of data It
can be functions of multiple dimensions
of data as well Right
So lets look at an example and then
Ill stop for questions example is
suppose x is in r and y is in r
Okay Now
suppose I define my f of x as 1 x²
right then erm
with
theta transpose vx
okay is same as
erm
a1 x
a2 x 2 plus 1
thats it
Okay So now what was quadratic
in your data space became linear in the
transform space So thats why
any so this is called polinomial
regression by the way So you are
regressing using polinomial functions
Now polinomial regression
is always a generalized linear
regression with a fixed polinomial
kernel Thats it
And you can extend this idea to
anything You know it need not be
restricted to polinomial functions
Right This fee can be lets say sine
functions You know they can be
exponential exponential functions It
can be cinosidal functions or anything
The idea is that you are given X
transform it into some other space using
fixed transformation and then solve
linear regression there In fact Ill
Ill ask you a question here Uh you
know something that you you do I mean
you know something that already is in
this framework just that maybe you dont
uh recognize the name Do you know about
4 year series Theyre exactly this
where your fees are ss and cosiness
Youre representing your data as a
linear combinations of ss and cosiness
is exactly what it is
right for your series is erm that way
right so you take your free tob linear
functions of data with fixed kernels
these are called kernels transformations
and then uh you find out the
coefficients of uh the linear coicient
using
spares methods so thats why generalized
this is called generalized linear
regression or generalized is linear
models where given data you transform
your data onto some some other space and
then
assume uh your model to be a linear
combination of those dimensions But
note that assuming that data is linear a
linear sorry the dependent variable y is
a linear function linear combination of
uh uh dimensions in the kernelized space
or transform space
does not mean that it is linear in data
space In fact its the other way
around I mean if you have transformed
data using a nonlinear function
its almost always that the the the y is
not a linear combination of data
dimensions
Its a linear combination of the
dimensions in the transformed space
Unless your transformation is also
linear Suppose your transformation is
also linear then composition of linear
functions is another linear function
always right So that thats why it
becomes linear Otherwise its its a
nonlinear combination Thats why the
these are called generalized linear
models So polinomial regression now
also is a linear regression under a
polinomial transformation kernel Thats
it
Make sense Okay So Ill yeah Ill take
questions now here
 Where
 here
in the last the number of data points
 No no no Okay See how many uh how
many kernels we do use is a design
choice See f is a function of the
original data dimensions See it need
not be a function of x1 Im saying it
can be a function of x1 x2 x3 The
first dimension
 Oh these are the data Okay Data
points So now youre saying there
should be n of them Correct Yeah So
its a mistake There should be Yeah
See if I write this this means that all
of these fees are say okay let me do it
this way I think a better way to write
it is
there are n of them So for every data
point there is a transformation and
there are n data points and therefore
there are n transformations
notations So the underlying function is
the same
Okay So you take the first data point
 whichever
 whatever is the transformation you make
it undergo that transformation and you
get the first transform data point and
there are n of them
But remember that this f function
the dimensions of this f function right
or the fe vector post transformation
need not be the there need not be a
correspondence right it can be the first
dimension can be uh a function of first
three dimensions of data the second
dimension can be a function of last four
dimensions of data this is completely
user defined is a design choice
 b dimensional
 come again
 is b dimension
 yeah thats again you choose that p
are there guidance to design this
transformation
 The question is are there guidelines to
uh design this transformation Um people
like forear that that was their life
contribution So they found out that if
your if your input function is uh
periodic then you can use exponent signs
and cosiness to represent that right so
that the error is minimized Now
in the pre uh deep learning era okay
uh lot of scientists they dedicated
their life to find this fee So
including my PhD thesis during my PhD I
want I was designing this fee for the
problem of speech analysis So what is
the best data transformation By the
way this is also called as feature
engineering or feature learning Given
data learn some features on your data
Right Such that know the
okay I Ill ask you one other question
here now that we are talking right
one can establish equivalence between
learning a particular feature and making
the underlying distribution function
more and more complex
What do I mean by that Okay Ill make
a statement You take it as a homework
and do it Its a its its an
interesting uh homework to do H lets
say that you build a base classifier
Okay By making an assumption that the
class conditional densities for both the
classes are gausian
You understand what Im saying You are
building a base classifier by assuming
that the class conditional densities are
both gausian You assume that they have
the same variance but different means
See what happens to the base classifier
The answer is the base classifier will
be a linear function of data You will
see that hb of x will be some linear
function of data
So now if you make an assumption that
that your class conditional densities
are gian with the same mean with
different variances then base classifier
will become a linear regressor
Come again
 No if you make the the assumption that
the variances are the same Means are
same varian
 no no Im saying variances are the same
means are different then it become
linear functions of data thats what Im
saying it will become linear regression
right so now from the erm standpoint
lets say that I am assuming that I Im
Im trying to model my uh my data using
linear regression then Im implicitly
making an assumption that the underlying
distributions of both the classes are
gian with different mean with same
variance thats the equivalence
Now suppose I make an assumption I let
go of that assumption that the variances
are the same of the underlying class
conditional densities Then what
happens You can actually visualize that
mathematically right because we are in
the base classifier we are deciding
based on the ratios of P of Y given X
for Y equals 0 and Y equals 1 So it will have the
ratios of two Gian densities and both of
them are quadratic in X Now if I assume
them to be having same variances the
quadratic term will get canceled away
and only the linear term will survive
Thats why it becomes a linear function
of data Now if I dont assume the
variances to be the same then the base
classifier will become a quadratic
function of data
You see so only if you assume that uh
only if you try to fit a quadratic
regression model Okay If you if you if
you use a quadratic regression model for
classification rather quadratic model
for classification you are implicitly
making an assumption that your class
conditional densities or gausians with
different means and different variances
So a generalized linear regression with
a quadratic kernel or quadratic
transformation is equivalent to building
a base classifier with the assumption
that the class conditional densities are
both gaussian
 Exactly
Now to your question So now what
happens is that the moment we make a
choice for fee we are making a choice
for the underlying distribution
function Right Now what happens if you
assume that the class conditional
densities are GMM
What sort of a kernel should you have to
choose So we know that choosing a
unimodal goian is a bad choice Right
Suppose we make an assumption that the
underlying density functions are
GMM
How does that translate to an erm is the
question In those cases what we do is
we will not choose this fee We let the
erm choose the fee for itself
Thats what a neural network is
Now so many decades people were doing
feature engineering and trying to so
never in the history people never gave
raw data as an input to classifiers For
instance during my PhD right I mean
people used to laugh
you record speech signal right Or or
you look at a signal or you take an
image you dont give an image as an
input to a classifier What you do is
you extract some features from that
image by doing some fixed engineering
You know for instance if any anyone of
you is doing image processing course
you know right there are these sift
kind of transformations and all these
right What are those there are
actually these fees extracting features
from data and then use those in a
classifier
Now what has happened is
it was realized empirically that you
dont have to do feature engineering
just throw raw data I still remember my
adviser used to laugh when just when I
was finishing PhD neural network started
uh you know making lot of strides and he
was laughing you know people throw raw
data to these classifiers how can they
do it so today nobody does any feature
engineering anymore right so you take
raw data and give it as input even NLP
for that matter if you are taking NLP
course there used to be bag of words
right the other kinds of frequency
estimates and you give that as features
is your fee
If you represent your uh lets say your
data is a sentence each token you
represent that as one hot representation
and if you just take counts of all of
them counts of nouns and all that there
are actually some transformation of data
that you use as input your classifiers
come neural networks they said why
why even bother to learn fee
see I still remember my adviser is a is
a very old man now he used to stick the
pictures of spectrograms of different
speech sounds in his office
Just stare them right So stare at them
because you know looking at that you
come up with some sort of a pattern so
that you design a nice fee People have
named these fee after them So there is
gber filter
right and there are foryear transforms
and there are wavelets named out of
people right all of these are these
fixed transformations of data so that
learning becomes easy
now come neural networks they said dont
try to
uh fix or rather use thats why you know
first day I told you this is all
ignorance modeling right you dont know
how to design a nice transformation so
that data becomes easily separable You
make your model itself learn what the
SPE is Well see that you know well
see ways of transforming data from one
dimension to the other via erm framework
which is nothing but the neural
networks We well get to that in a way
So for now we are still in the age of
givers and you know four years and so on
where we transform the data from one
dimension to the other and then we use
erm to solve it
Uh no there is no thats a choice the
question is is there any relationship
between D and P no okay u okay have has
anyone of you studied wavelength
transforms I dont know if its even
taught these days you have right see
there right in uh
uh you have this idea of how many how
many dilations that you have to choose
thats your P how many dimensions of
your data you should choose for
transformation right so how many
features youll have to extract if given
an image you can extract multiple
features of it right thats your B
thats again a design choice okay okay
so this is about generalized linear
models
lets get to classification
uh we will stop here and continue in the
next lecture
