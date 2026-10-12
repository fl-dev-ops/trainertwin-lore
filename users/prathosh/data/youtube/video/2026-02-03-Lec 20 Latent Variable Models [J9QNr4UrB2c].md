---
id: J9QNr4UrB2c
title: Lec 20 Latent Variable Models
url: https://www.youtube.com/watch?v=J9QNr4UrB2c
date: '2026-02-03'
duration: 33:22
model: youtube-captions (en-orig)
transcript: true
---

## Transcript

Welcome everyone Let us continue on our
discussion
about the mixture densities Uh the last
class we entered the last class by
discussing the need to have uh uh a
model
that can approximate uh any continuous
density to arbitrary closeness And we
saw that uh a gausian mixture model is
uh one such choice that can approximate
any density to arbitrary closeness So
in this in in todays uh lectures we
will look at an iterative algorithm for
uh maximizing the likelihood for such
mixture densities Right
Because remember that our goal is to
find estimate the parameters of an
underlying model by minimizing the K
divergence which is equivalent to
maximizing the likelihood function okay
of log likelihood of that particular
model under the observed data points and
uh the way we did it for some primitive
densities was to write down the
likelihood take the derivative of it and
find out the the optimal parameters But
for the cases of densities such as
mixture densities this optimization
problem cannot be tractibly solved The
sense that you cannot differentiate that
and uh the terms that you need will not
group them group themselves up So you
need to resort to an iterative algorithm
which we call the expectation one of the
one of one such iterative algorithms is
what is called as expectation
maximization algorithm We will look at
that algorithm today So that is the
objective for today So lets recall
that
 a mixture density

mixture density model P theta of
plus was the variable V
This is given by
the sum
of
whats the notation
theta JV
where

P theta J
is a density function
and alpha js
are all bounded between 0 and one and
they sum to one
This is the definition of a mixture
density in general

 Now a special case of this is
what is called as a gausian mixture
model

 where the constitute densities p theta j

are all gian densities
with parameters uh muj and
sigma j So we have
m number of mixtures So this capital M
is what is called as the
number of mixtures or number of modes
So how many densities are you combining
So please note that we are saying that
our density function is a linear
combination or a convex combination of m
other density functions So that is the
model that were looking at
Okay
And I also told you that the gian
mixture model or gian mixture density is
a universal density approximator in the
sense that it can approximate any
continuous uh density to arbitrary
closeness So what is the uh criteria I
mean uh the closer an approximation that
you need the more the number of mixtures
that you should choose So this is a
hyperparameter I mean this is a model
choice Its an engineering choice that
the designer has to make what should be
the number of mixtures that we would
look at So but if you have enough
number of mixtures then you can
approximate any density to arbitrary
closeness Now this is a theorem that is
known I for the want of time Ill not
prove that theorem So this is quian
density Now lets look at parameter
estimation or ML estimation maximum
likel estimation for mixture densities
for mixtures
So recall that
we wanted our parameter set theta Okay
So by the way I Ill mention it theta
was taken to be the maximizer
of the likelihood function Whats the
likelihood function
Take the log of
the sum of log of uh the likelihood
evaluated at all data points That is
our likelihood function Right This is
what we wanted So in the case of uh a
mixture density
the set of theta so specifically for the
gian mixtures right what are the
parameters that we are considering
theyre all alphas and we have how many
of them we have m of them right so
theyre alpha js and we have mujs sigma
js so these are the set of parameters
that we need to estimate So for J is 1
through M So for each of the gshian we
have the corresponding
uh means and the variances and we have
this alphas which are which are also
model parameters that we would estimate
Basically this is al the mues and sigas
are telling you what should be the
spread and the center centering of
individual gausians and alphas are
telling you how each of these individual
gaussians should be combined such that
you get the underlying density
estimated So thats also a parameter
that needs to be estimated along with
the other parameters So we have alphas
and note that all alphas are scalers Mu
and sigas are vectors and matrices So
mu is a vector of dimension d and sigma
is a matrix of dimension d by d and
alphas are all scalers Okay So this is
the these are the number of parameters
that we should estimate Now what
happens is that for the mixture model if
you consider the log likelihood so log
P theta of vi
is given by log


So this is the form that we end up
getting for the case of a mixture
density Now observe whats happening
here All the while we had sum of lo
term actually there is another So if
you take a sum here over i So please
note that we get two sums here One the
outer summation is over the data points
that we have The inner summation is
over the number of gshian components or
mixtures These are very different Huh
Now all the while when we were doing
maximum likelihood estimation with
primitive densities we had this uh form
where we had log of some density and
this density if you can represent that
as an exponential family of density The
logarithm and the exponentiation will
get canceled off and you get sum of some
a few terms that could be differentiated
here Here if you look at the structure
these gian densities have the
exponentiation but you have a summation
inside the logarithm
So that means that this exponentiation
with the uh inside I mean within the
component densities will not get
canceled with the logarithm and
therefore if you take the derivative of
this with respect to the parameters mu
and sigma they will not separate out
and thats why you need a different way
to solve this optimization problem
Thats the motivation so as to why one
should move to an algorithm such as uh
the expectation maximization algorithm
Okay
Okay So with this well have to come up
with some other way to optimize uh the
log likelihood for mixture densities So
let us look at what is called as um
please remember this motivation because
from now Ill talk about a class of
families of models uh which are called
latent variable models okay of which GMM
or any mixture density is a member a
gshian mixture density or uh any mixture
model in general is a member of this
large family of models called latent
variable models In fact even
transformers and uh the adversarial
networks and various autoenccoders All
of these are latent variable models
Its a broad family of models I talk
about latent variable models in general
Okay And show that this is a special
case And the algorithm that we
construct which is the EM algorithm is
actually uh a general class of algorithm
that can be applied to any family of
latent variable models Okay So well
generalize it that way So the you
understood the motivation right We
wanted to get the parameters of a
mixture density and we could not get it
because we have uh a particular term
that will have log of sum that is not
tractable So you need to come up with
some other way to do it So thats the
motivation as far as the ML estimation
for mixed density is concerned So lets
look at these family of models which are
called the latent variable models

 cough and clears throat

 So here is the uh philosophy behind it
See intelligence or rather information
comes through compression
What does this mean So there is an idea
called information bottleneck Okay it
comes from the information theoretic
standpoint What Suppose you are you
have your data in some d dimensional
space Lets say that you can compress
all that information uh in a in a very
lower dimensional space Okay
such that your information content is
not reduced Now how do you do that The
only way one can compress a large amount
of information and put it in a very
small space is by understanding the
semantics
What do I mean by that Let me give you
an example Suppose you look at the
picture of a human beings face Now
mathematically speaking or from a
measurement perspective there are there
are hundreds and thousands of pixels
But how many pixels there are actually
semantically useful Instead of storing
the values of each of the individual
pixels you can store information such
as oh every face has two eyes They
are symmetrically spaced Okay and
there is a there is a nose and its
there and the the uh uh there are lips
which are red and so on So if you store
a small bit of information and compress
it at a semantic level then everything
that you need to know about a human face
is
known you dont have to remember each of
the individual pixel values or each of
the details of everything Right So
this is the idea of compression So if
you see you can think of uh todays
LLMs capability from that way because
look think about it if you want to
compress all the information that is
there in a worldwide web which is
trillions of tokens of information into
a few into a model that only has
billions of parameters
It is compression
See how do you compress
The only way you can compress is by
understanding semantics Throw away
everything that is not important and
only remember semantics You know that
is one way to explain whats happening
in in todays uh I mean if you you take
huge amounts of information and try to
compress it Now that compression has to
be put into a a modeling framework How
do you express compression in in a
modeling framework is by introducing one
other random variable into the system
Okay So lets lets look at it So we
are given
some set of data Okay
Which we which is a set as we know we
have x1 x2 up to x n So these are
sampled ID from some distribution
Typically uh yeah xi is in some RD
right This is what we saw
What I do is I introduce an additional
random variable into the system So
introduce
into the system
that is unobserved
What we have observed
is the data right the the what we are
representing by letter X right now we
assume that there is another random
variable okay uh that is coming from the
same sample space which is which has not
been observed but that contains lot of
information about XL its very very well
correlated uh with with X and it
contains information about X So this is
actually called the the hidden or latent
random variable
Its also called the representation
random variable right A latent space
or latent random variable This is the
nomomenclature that is used
Let me give you an example Uh lets say
that we are looking at uh
a data set that contains u um
the pictures of handwritten digits Im
talking about the the usual eminest data
set Now this random variable that Im
talking about okay lets say that this Z
uh oh typically represented by the
letter Z Okay Now this lets say that
this is a three dimensional random
variable a continuous random variable
The first dimension of this represents
the thickness okay of the digit
The second dimension of that represents
the symmetry of that particular digit
with respect to x axis Its a switch
So if its symmetric then its one If
its asymmetric then its zero The
third dimension may represent
if the if if the if the digit the right
return digit actually covers more than
20 percent of the total pixels Its a binary
value Does it does it does it make
sense Now suppose you have 10 such
dimensions So maybe using only those 10
dimensions 10 pieces of information
you can actually guess what the digit
is
Right If youre looking at lets
another example lets say you take the
example of data set that contains human
faces one random variable or one
dimension of this hidden random variable
may be uh the the the color of the hair
of the person The other can be lets
say the gender So it can be whether uh
somebody is uh uh you know having a
spectacle or not
It this random variable by definition
can be continuous or discrete It
doesnt matter Its just there in the
system It is not it is not observed
Okay Now why do we introduce this in
the system is the question right So the
thing is one for computational ease
well see that so one itll make our
computation much easier but more than
that its for compression Now suppose
you design systems and models where uh
there is access to this particular
random variable
Okay Then if you can estimate the
posterior of this random variable given
data
right Then you can then you can
actually extract hidden information from
data
Isnt it This is another random
variable that we have introduced in the
system Now mathematically speaking
since this is another random variable
we can talk of joint distribution Well
see that well talk of joint
distributions between X and Z Because
there is a joint distribution we can
also talk of posteriors of Z given X So
posterior of Z given X will give us
hidden information about the data if we
can estimate it Does it make sense So
for instance lets say that lets take
this example of uh um uh digits Now
lets say that this hidden random
variable represent the semantics of the
digits
Okay its a its a 10 dimensional
random variable uh one hot random
variable So one of the values gives you
one digit the second value gives the
other digit and so on Now suppose you
model the system using uh this latent
variable framework and find out the
posterior of this z given x if you can
successfully do it then itll give you
what semantics that this data has
already right without having any labels
Do you understand what Im saying So
that way it is because of this reason
that latent variable models are also
used for unsupervised learning
Well see all this all this in a while
So this is the motivation so as to why
one should resort to assuming that there
already has uh theres already a hidden
variable that is there in data which is
not observed
Okay So well see multiple
instanciations of this You know another
example is if you build a language model
in its latent space you can do semantics
in the sense that you you you have seen
this right Uh suppose you give a
particular image uh to these uh these uh
uh current day AI systems and ask it to
change it change a parts of it for
instance you know impose a change the
style of the image right and impose uh
erase a particular object and impose
some features onto this image and so on
How is this done Its actually done by
doing this So given an image they go
back to the latent space and in the
latent space they manipulate because
directions in latent space signify
semantics and from latent space they go
back to data space again so that only
the semantics are changed and everything
is kept the same Thats exactly what is
being done
You understand So start from the data
space project it onto the latent space
manipulate and get back to the data
space again This is exactly what is
done in uh diffusion models right
Forward diffusion reverse diffusion
Again as I said this is the subject of
my next course
But yeah a diffusion model which is the
state of the art uh generative model for
for images is also a latent variable
model
Any questions This is very important to
understand this philosophy right So
basically what we are doing is given
data we are assuming that there exists
an unobserved uh compression space okay
which is correlated with the data space
uh and we will estimate that that random
variable or we will use that another
hidden random variable in our model in
in our while we are modeling our data
So rest is math So this is uh the the
motivation and philosophy Any questions
on this before we move on Yeah

Second
values are not
already
 Huh So the question is what is
unobserved Uh what is unobserved is the
Z
The values of Z is totally unobserved
Right We only have as you rightly
pointed out uh all we have are only the
the data that we have observed not the
uh latent latent variables the values of
latent variables Now the second
question is how do we how do we how do
we use it right is we will just like we
model or we estimate the parameters of
the model we also estimate a
distribution over the latent space as we
will see thats the whole point Any
other question on this
How do we decide what
machine
 Again good question The question is
how do we decide uh what semantics are
being captured by latent space or what
what semantics is good for a given data
We dont This is completely
unsupervised
We let the model choose whatever it is
So what choices do we do we have depends
upon the model that we are looking at
Some models or some frameworks uh choose
distributional forms for the latent
space Some models choose the
dimensionality for the latent space and
every choice that we make has
consequences
Right So this is not something that uh
that is given by labeling or anything
This is we are we are assuming that
there is something hidden in data and we
want to discover that hidden
information
through modeling
through modeling So this is we have not
observed this at all This is not coming
from the uh the data It is hidden in
data We want to explore that you know
we have to unlock it is what the idea
is
 Yeah
that he had that he will estimate
this how does it add to that like how
does it then what I mean is the problem
remains the same
 yeah the question is does the problem
remain the same that of density
estimation yes all we are saying is
in addition to what we have seen as data
and an underlying distribution px here
we have additional random variable that
we have not observed which we will
consider while modeling our data thats
it while we are estimating the
underlying density We will assume that
there is another random variable that
defines my system Which means that for
any density uh like if we have not gone
to this uh perspective there will for
every density that we will estimate
there will be existing latent variable
 thats a modeling choice see its a
modeling choice do you want to resort to
a latent variable model or not is a
modeling choice but in the case of
mixture densities it comes naturally as
we will see now a mixture density is a
natural ch I mean a mixture density can
be very natural ally represented as an
latent variable model as we will see now
but its a design choice that do you
want to call your do you want to model
your data using a mixture density or not
okay but nothing changes this is only a
modeling choice P theta that we are
defining we are introducing another
additional random variable into our
system thats it
so basically that random variable its
some abstract stuff we cant explain
whatever it is has more info than
is more on the actual density than the
data samples themselves
 You can say it that way Uh it is still
correlated with the uh with the original
data it contains you can see that as a
compressed version of the original data
having information about the original
data
 Okay So whatever
noise
that is present in the data that will be
a bit less
 Yeah Can say it that way but Ive not
defined what what noise is and all that
What happens is as I keep saying uh
language is too fragile It fails Math
is what works So motivation can only
take only take you so far So as far as
mathematics is concerned we have an
underlying random variable realization
and an underlying distribution We
assume that there is one other random
variable that we introduce into the
system and then model it Question
 Can you be a little louder please What
if there more than one latent variables
that each capture distinct
possible Thats again a modeling
choice See the way to put it is that
you make your latent variable has
multiple dimensions Its a vector
valued random variable again So that
will capture whatever you just said
Every dimension can be looked into as
capturing something some different
semantic
 Yeah
 So do we cap the dimension of the latent
variable We dont typically it is
chosen to be lesser than that of the
data variable In the particular case of
uh a mixture and mixture model latent
variable is discrete and it is equal to
the number of mixture components that we
look at as we will see now in the case
of mixture densities only Okay But in
the case of lets say a transformer it
is taken to be continuous Again its
its a engineering design choice See
the mathematical algorithms that we will
see now will is common through all
latent variable models you know from
mixture densities to transformers
Okay But the choice that you want to
make is model specific
 So two questions One are we only
estimating P of Z right now or
are we estimating PX
 Hold on to that question Uh I Ill
write that So the question is what do
we estimate We we still estimate px
because thats what our interest is But
we do it through estimating
what
 Huh

 No
 Yeah thats one way The other way to
do it is you know you represent well
Ill write the math right now Write px
as marginal marginalization over the
joint density between x and z Thats
it Thats our model Well write that
in y Whats the second question It was
about like we have sampled XI values but
we dont know
 it is jointly estimated
 Yeah
 Since we dont know what this variable
is capturing some abstract thing Coming
back to the X ray example lets
everything is saying what are those
parameters everything is different we
training the model in a different
hospital or different demographics Do
we expect the random this variable to
capture
I
 I I dont have an answer to it
Sometimes it would sometimes it wont
Okay So
the question is uh
does this random variable uh can we
interpret what this random variable is
you know in a in a sense right if it can
capture distribution or shift or
anything depends see uh
three and four of my PhD students have
worked only on this you know what does
thats why Ive named my lab as
representation learning lab So
representation learning is learning this
Z discovering this Z from different
modeling perspectives and it can it can
depending upon what sort of choices you
make for the model right it will capture
different semantics you cant its very
hard to pinpoint on what semantics it is
capturing
 is it the same thing there was model
which was trained on faces identify
whether its a male or female and it
totally failed when it was tested on the
African faces because it was just
sitting the presence or absence of
makeup
 Yeah So may maybe uh your theres a
latent variable that is defined for that
right So that that this model is
looking at you cant you it you can only
do it uh post factor No so as they say
hindsight is 2020

because you know that it has already
happened right so there is its always
perfect So hindsight everything is
perfect but perspectively but there are
algorithms that with which you
can can sort of regulate what this
latent space is going to do Uh yeah
thats again its its its out of the
scope of this particular course Okay
but there are ways to do it Is this
clear So lets look at the math Okay
Yeah So math is the easier and more uh
well behaved part of it So we introduce
another random variable into the system
that is unobserved Its called the
latent variable So mathematically
for every x i in
in d
define
uh zi that is in typically r k where k
is less than d This is a typical case
It need not be the case that the
dimensionality of the latent space
latent variable is less than that of
data variable Its typically the case
because we want to interpret that as
compression Um
define another random variable with
a distribution
of its own
Now X and Z
are assumed to be correlated
statistically correlated
Now this Z which is the latent variable
can be continuous
or it can be discrete
Z can be continuous or discrete I mean
its again a design choice
Okay Now with this lets define a
latent variable model Okay with this
uh latent variable model
is defined as
P theta of X is the model that we are
looking at right is given by the
marginal
or the joint distrib distribution
between X and Z
if Z is discrete Okay So if Z is
discrete
and if Z is continuous
define that as the integral
So this is the definition of a latent
variable model
Math is so easy right So p theta of x
which is the density that we are trying
to model is simply the marginal over the
joint densities between uh x and z and z
is unobserved right you integrate the z
out
okay thats the definition of uh the
latent variable model
Now since we are talking about two
random variables here and there exists a
joint density there can also exist
the the marginals and the posterior and
so on So there can there can exist uh
conditionals of this way There can
exist conditionals of uh this sort and
there can exist the marginal over z
marginal over x and so on Right All
these densities are valid and they
exist Okay Uh so this is
actually a side point We dont need it
here
Now the question is yeah theres a
question Yeah
 The question is if Z is not defined and
it is okay Z is not not not defined Z
is unobserved How do you incorporate
this in the model and how do you uh how
do you even talk about the joint
distribution between these two Which a
valid question So as we will see right
now the fundamental foundations of
learning latent variable model is that
you not only estimate thetas but you
will also estimate the densities on Z
So estimate two things in the in so far
what we have seen is we only estimate
the parameters of uh the underlying
density Here we will not only estimate
the parameters of the underlying density
we also estimate the density on Z as
well That is how we do it Okay Uh we
will stop here and continue in the next
lecture
