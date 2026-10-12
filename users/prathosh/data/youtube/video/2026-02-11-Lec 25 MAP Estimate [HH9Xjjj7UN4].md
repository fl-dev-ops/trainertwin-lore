---
id: HH9Xjjj7UN4
title: Lec 25 MAP Estimate
url: https://www.youtube.com/watch?v=HH9Xjjj7UN4
date: '2026-02-11'
duration: 38:24
model: youtube-captions (en-orig)
transcript: true
---

# Lec 25 MAP Estimate

## Transcript


Welcome to this lecture where we will
discuss well continue from wherever we
had stopped the last time So we were
looking at density estimation
techniques Specifically we looked at
the maximum likelihood estimation
techniques Now in todays class we will
look at two other ways of estimating
density functions So one is what is
called as the basian methods of
estimation of which maximum a posterior
probability estimate or a map estimate
is one member Well also look at
nonparametric density estimates as a way
to estimate the density functions Now
recall that in maximum likelihood
estimate recall
in ML estimate
the parameters theta the parameter set
so which you are uh denoting with theta
is considered to be a deterministic
variable
What does this mean
Now our estimate on theta depended
completely on the data that we had So
recall the idea was to find theta such
that it minimizes the kale divergence
between the true density and the model
density However uh as I said in the
the end of the last class what happens
is if you depend completely on data
especially when the cases uh in the
cases when the data is very less in
number ML estimate may not be the best
choice So we will also discuss we will
discuss this idea in detail when we look
at uh the the bias variance
decomposition and the idea of
overfitting and underfitting Here is
the example right So with so when
n is small this number of data points
are small so ML estimate
may not be optimal
Here is an example right as an example
consider
So ML estimate
for a Bernoli random variable
Okay What is this You remember what
the ML estimate is So theta ml is
simply equal to
number of times
the trial
has
yielded one If you consider
divided by n right So this is what the
the ML estimate is Remember this this
is what our ML estimate was for a
Bernoli random variable Now suppose
the data D is like this You know we
have like 1 one one
and zero This is what our data is in
this case What the ML estimate is
it is
3x4
The question is is this a good estimate
or maybe we can actually consider a more
degenerative case where all four trials
ended up in one of the outcomes Okay
So in this case the ML estimators for
that particular parameter is one So now
is this a good estimate is the question
Now depends on what the underlying data
is Okay What the underlying reality
is Now suppose our Bernoli random
variable that we have
corresponds to a fair coin
which means that you know we or rather
we know that uh it is not the coin that
has both sides as the same but this ML
estimate is telling you that the
underlying random experiment that we are
conducting has a coin that has both of
its sides to be the same Okay Now
suppose we know the fact that this is
not a coin with the same sides both the
same sides How do we incorporate that
knowledge that we have into the
estimation technique is the question
right So let me write that So the
above estimate
is not optimal
So Im writing optimal within quotes
because Ive not defined what optimality
is you know in whatever sense Lets say
that youre looking at the difference
between the the estimate and the true
estimate Okay uh in an expected sense
So its not an optimal the estimate is
not optimal if
the
true value
is
around 0 point 5
This is just an example where ML
estimate especially if you have very
less amount of samples uh leads to uh
bad estimates of the underlying
parameter Okay Now the question is how
do you incorporate the belief that we
already have regarding the parameter
into our estimation technique is the
question that we want to ask So it is
this question that the basian estimates
try to answer Okay So in basian
estimates
the idea is to incorporate
the prior belief
or information
about the parameters
Now if we already know that the
underlying parameter has uh a particular
type of form you know it can only take
this sort of value then no matter what
data tells us we know we know that this
is our belief and we want to incorporate
our belief into the estimation
technique So how do we do that
mathematically is the question and
Beijian ways gives you a way to
incorporate that Okay Now in Bijian
methods what is done is mathematical way
to do it is assume
the parameters theta
to be a random variable
and
model the belief Pardon the prior
belief
in its distribution
So far we have been looking at theta as
a deterministic variable Right So now
assume that theta also is a random
variable just like your data and that
has a distribution of itself Now that
distribution okay uh incorporates the
belief that we already have regarding
the parameters that we are trying to
estimate Okay So this is the idea Now
in the example that we considered uh
previously suppose in the in the
previous example
example of Bernoli random variable
So you can assume lets say P theta of
theta which is a distribution on theta
right uh
write the equation later to be having a
distribution of this sort
So this is zero and this is one okay and
this is p theta of theta
So lets say that this is around 0 point 5
Now this is a distribution that we
assume on theta even before we look at
data
right even before we look at our data we
assume that that p theta has this
distribution So what is this actually
saying This is saying that I know that
the value of theta being around 0 point 5 is
the highest
Now given that I already know this
estimate my theta is the question that
Im asking no matter what my data say
Okay Now if I only stop here then Im
completely oblivious to data Even
thats not a good idea right I mean
what if uh the the coin that you have or
the Bernoli trials that you are
conducting will skew your belief
Okay this and please remember that the
prior belief that we have on our on the
parameters is completely independent of
data and it only comes from sources that
are not related to data So thats why
its called a prior belief
Is that all right So now if you have
this sort of a distribution that is
incorporated on the parameters now you
have to use this along with data to
update your belief
Does that make sense Yeah Okay So now
lets see how to use this idea in
estimation
Doesnt this also a source of error as
well
 The question is doesnt that also
introduce source of error in what sense
 Whatever my belief is like how that
 yeah there is no way to know whether
your belief is correct or not So thats
why its called a belief
right so use your belief see data can
lie okay and your belief may be wrong
So you combine both of them thats it
Now your estimation of course itll
induce error in the sense that if you if
you have wrong belief then you end up
getting wrong estimates
Okay Now yeah you cant do anything
about it However suppose your belief
augments your data The idea is to
augment the observations with belief So
as you will see later if you have
infinite samples then uh data will lead
you to reality
right because uh if you conduct the
random experiment large amounts of large
number of times you know you know that
law of large numbers takes into effect
and itll converge in probability
However when you have small samples uh
data can lie right and belief can be
wrong So the question is can we combine
both of them in a meaningful manner
 Huh So now what is better is a
different question So we have not
talked about how to quantify the
betterness of an estimate thats outside
the scope of this this particular
course But there are ways to do it
Thats why you have this blue estimates
and so on Right Where people talk of
suppose you have an estimate that you
have gotten How can you quantify the
goodness of this estimate and error
bounds can be derived on top of them
Okay how I mean can I bound the error
that that this particular estimator is
giving and so on What can be seen is
that in the Bayian methods right uh I
mean as you can probably guess the error
that is uh imposed or or rather
incorporated by imposing your belief is
a function of your belief obviously
right but there is a way to incorporate
your belief in the system thats it okay
well see later in the course in a
couple of classes that this is exactly
equal to the exactly equivalent to the
idea of regularization that people will
do in the deterministic sense We will
see that in a way Okay So now how to
incorporate this belief from an
algorithmic standpoint is what we will
see now So suppose
so your data x is sampled from some px
right This is our data that we have and
the parameters theta is coming from P
theta
which is the prior on parameters
Okay
Now
use base law to compute
the posterior So now note that theta
parameters is also a random variable
Now we can talk of distributions the
posterior of the parameters given data
Right So posterior of parameters given
data now is proportional to the prior
on the parameters and the
no this is prior on the parameters is
your belief
right and this
is the likelihood of data at a certain
theta right you given a theta you will
get some likelihood okay see even in the
maximum likelihood estimates this makes
sense The only thing is this is fixed
at a particular point and you take that
its a point estimate Okay in the
basian framework this becomes an entire
random variable So the reason I wrote
proportionality here is that we dont
care about uh we often dont care about
the denominator that is the
normalization constant you need this
denominator to make it a proper density
but typically at least in map kind of
estimates we dont care about the
denominator thats why I wrote it as
proportional this is base law so this is
how we use it you start with you
incorporate your belief into p theta and
of course the likelihood is there okay
which you have assumed multiply both of
them and you at the posterior of the
parameters given data So now note that
unlike in the case of uh uh the maximum
likelihood estimate where you get one
particular point estimate for theta here
you get an entire distribution over
theta
So basically the point is initially you
started with some belief you assume that
okay my theta has this sort of a
distribution now you observe data then
you update your belief So this
distribution over theta see posterior on
theta given x is still a distribution
over theta
So you start with an initial
distribution over your parameters and
having observed your data your belief on
the parameters gets updated
happens all the time in life No
right start with some belief go to the
real world get whacked and then update
your belief depending upon what your
observations are Thats the idea Now
the question is so I mean remember we
are still considered we are we are still
concerned about uh building a base
classifier Now what do you do with an
entire distribution over theta We want
one of it No there are ways to do it
One way to do it is pick the mode of
this distribution and take that as your
estimate for theta and move on That is
the map estimate Well well write that
in a while Okay Is this idea clear
Start with a distribution over theta
Okay And get an updated distribution
over theta by looking at your data
Thats how you do it
See uh in the Bayian methods right the
belief typ typically the belief is over
the parameters not over latent variables
but there are methods which incorporate
belief over latent variables as well
okay which well see later but for now
the belief is over theta thats why I
gave you that example of Bernoli random
variable where you know see what sort of
belief can can you have when you have a
Bernoli random variable Its that okay
the coin that Im tossing does not have
the uh does not have both the sides as
head So that is one sort of belief The
other thing can be okay its see maybe
you can weigh it See how do you how do
you derive belief right that comes from
the physics of the problem often times
So lets say that youre looking at that
coin No you weigh it for instance and
you know that one side is lets say 70 percent
uh uh uh heavier than the other side
Okay and then you construct a belief
according to that and then you
incorporate it Thats how you do it So
belief is mostly on parameters for now
Okay So later you can incorporate
beliefs on other uh parts of the uh the
function as well But right now its on
parameters Okay Okay So now let us
look at how to do it Huh So lets
consider the example of okay So you
compute this or maybe Ill write that
No Uh so how to use
P theta of uh P theta given X So one
way to do it is using uh the map
estimate
where
take
the mode
of
P theta given X as the estimate
This is called the map estimate maximum
a posteriorly probability estimates Now
why is it called a map estimate Do you
know what mode of a distribution is The
mode of a distribution is the point at
which the density function vanish The
derivative of the density function
vanishes or density function peaks
assuming that its a unimodal
distribution Thats why you are looking
at the point at which the density
function is maximum That is why its
called a map estimate Okay
So now let us take an example of doing
this Um
okay so before we do this
theres an idea called conjugate prior
that I should talk about
well have to incorporate our belief
into the system right so remember that
uh the choice of P theta is user defined
in the sense that we are free to choose
what whatever P theta that we want on
the parameters Now in the literature it
has been suggested that we always choose
our prior such that it is a conjugate
prior Now what do you mean by a
conjugate prior The prior on theta
that
that ensures
that ensures that
ensures the posterior
to have
the same distribution
same distributional form
as itself
So you choose a prior this way You
should choose a prior that would ensure
that the posterior also has the same
distributional form as itself Why is
this important Think about it Now
lets say lets take the example of this
Bernoli random variable that we are
looking at Now the belief that you have
is that this uh uh the parameter peaks
at 0 point 5 or whatever Now having observed
data
this should not transform into a gshian
distribution No
why is that
See remember what this distribution is
over This distribution is over the
parameter of the Bernoli random
variable The parameter of the Bernoli
random variable is bounded between 0 and
one
Now just because you observed some data
points which are the trials of that
distribution this parameter cannot
suddenly uh have infinite support Do
you understand Only the shape of this
distribution can change
the parametric form cannot change You
see that right So that is why you need
your prior to be chosen in such a way
that after seeing the data it should not
change the characteristics of the prior
Mathematically speaking the
distributional form of the prior should
not change after you observe the data
Does it make sense Okay So that thats
what such such a kind of a prior is
called conjugate prior Always choose
your prior incorporate your belief in
this conjugate prior such that the
posterior would not change the form of
the prior
 If data is very different from what
belief then
 no no see again thats what Im saying
data
Okay So belief is on parameters Data
comes from the repeated experiments
Now just because you are doing the
experiments the underlying parameters
should not change You know the
parameter the form of the parameter
distribution on parameters should not
change Thats why I gave you this
example
If you are if youre conducting a coin
toss experiment after seeing data the
coin toss will not become a roll of
dice That is what youre saying It
will still remain the coin toss
Thats what conjugate prior is Okay
 Unlike the variable and the data random
variable this does not map to the
sample space we looking at and its kind
of partic
 which one
 uh the parametric
 the distribution Okay The question is
uh does the
to paraphrase the question is very
difficult Okay So the question is the
following that the distribution on the
parameter space has nothing to do with
the random experiment that is generating
our data samples Thats correct So
there is another random experiment
Okay That is giving you the parameters
So basically theres a random experiment
that gives you the parameters
conditioned on that you are generating
data
That is what it is Yeah Thats why you
know you have p theta px conditioned on
theta and you also have p theta
conditioned on x Okay Yeah Thats
thats a good observation Okay Lets
lets look at now Did you do you
understand what conjugate prior is
always choose a prior that would be
conjugate Okay So lets look at the
example one example of a map estimate
So example of map estimate for Bernoli
random variable
Okay lets look at so now you have X
which is data that is sampled Bernoli
with parameters theta Theres only one
parameter to estimate here right
Bernoli random variable will have only
one parameter which is theta we have So
what we have to do first we have to
construct the uh
the likelihood conditioned on the
parameters Uh what is this
Its equal to
theta x
 times
1 minus theta times
1 minus x correct this is a distribution of
a bernoli random variable all of you
with me yeah okay now
what is p theta so now this is what we
need to choose now we have to choose the
prior what is the prior so suppose you
are looking at a bernoli random variable
what sort of a belief will incorporate
what sort of a belief is a reasonable
belief on the parameters of a bernoli
random variable see for one We know
that it is bounded It is bounded
between 0 and one So you have to choose
a distribution that is bounded between 0
and one Okay And what
thats the only constraint actually
What are the distributions that you know
of that are bounded between 0 and one
Uniform distribution is one But is is
uniform distribution a good way to
incorporate our belief Because its
only saying that I know that you know
all the values are equally likely I
mean thats not what we need In fact
if you if you if you take uniform
distribution as your belief and
construct a map estimate it will be
equivalent to an ML estimate No
that can be shown actually right So
uniform distribution is not something
that we need So what is the
generalization of uniform uniform
distribution
Its the beta distribution
Uniform distribution is a special case
of a class of special case of these
distribution functions called beta
distributions that have bounded support
Okay So beta distribution would be a
good prior on this So let us let us
look at that beta distribution And by
the way it also happens to be a
conjugate distribution conjugate prior
as we will see So how do we write beta
distribution Let us
given by um
gamma
 plus beta divided by
gamma times alpha into gamma times beta
to theta rise to alpha minus 1
1 minus theta rise to
beta minus 1 So this is the beta
distribution where
gamma is the gamma function right
standard gamma function
function and alpha and beta are
parameters that we need to choose So
this is what our belief is Okay
Or user user defined or user user chosen
parameters
Okay
this is our belief So now what should
we do after this So compute
the posterior which is P theta condition
on X This is what we need to now
compute So what is this equal to We
know that this is proportional to the
condition prior times the uh conditional
likelihood times the prior Okay So let
us look at this
What is p x given theta Just written
that no 1 theta power x times 1 minus theta
power 1 minus x
multiply this with
the beta distribution which is uh Ill
again remove the constant know that
gamma constant Ill just remove this is
uh theta power alpha minus 1 times 1 minus theta
power
beta minus 1
Now this is a conjugate prior y
Now this will be
theta
power
x
 plus alpha minus 1 Can you check the algebra
Is this correct 1 minus theta times theta power
beta minus x Is this correct
Okay So this is also a beta
distribution
right Of course you need to adjust the
the constants to ensure that it
integrates to one That can be done So
we are only writing it to proportional
So this is a beta distribution Thats
why its a conjugate prior Now what
happened with we started with some
initial
uh belief on the on on parameters theta
Now having seen data our belief will
change So think about it
mathematically What do you mean by the
belief of
a belief over parameters changing in
terms of distribution functions on
theta Here is the question The
question is
what do you how do you incorporate your
belief mathematically It is by imposing
a distribution on your parameters theta
Now having seen data if I say that my
belief has been upgraded and changed
based on data mathematically what would
happen
 Different parameters Huh The
parameters that we have started with
okay on the distribution of parameters
will get updated and that will become a
function of data Thats exactly whats
happening here You see
now you got a new beta distribution that
has data in it
X in it You see this Of course we are
doing this assuming that there is one
data point If there are
n data points there will be a sigma here
right because this p of x given theta
will now be the product of because we
have we have made an ID assumption right
there will be product of all of them uh
so you will have in the exponentiation
theyll all get summed up so youll have
a sum of all these okay so let us look
at this so now suppose
okay so what do we do with this now we
got a new beta distribution but we want
one single theta right
Ultimately we want one value for the
parameter that we use
in our class conditional density or
whatever to get the basian uh get the
base classifier or the optimal
classifier estimated Now what do we do
with an entire distribution over theta
As I said in map estimate you get the
mode of this distribution Okay So in
map estimate
theta map
is taken to be
the mode
of
the posterior theta given
Okay So in the above case
what is the mode of uh
uh a beta distribution
it can be read off okay so given a beta
distribution the mode can be found out
right I mean its it has an analytical
form Ill just write that okay so you
can all you need to do is take the
density function take the derivative of
it with respect to theta and put it to
zero Youll get that Ill just write
down the mode It will be uh x minus x plus
alpha minus 1
alpha plus beta minus 2 This is the mode
Now this is for one data point right
So suppose we have n data points
Therell be a
in the denominator
youll have an n term
Now compare this with the ML estimate
What was the ML estimate
There is an XI here Yeah So this was
the ML estimate Okay Now for n tending
to infinity what will happen
what would be the difference between ML
estimate and map estimate Theyll be
the same So thats the idea So if you
have infinite amount of data then your
belief does not matter
So thats why they say no uh so one one
acquires a lot of maturity as one
interacts more with the universe Right
So one should not be confined to ones
room or whatever Right So the more
data points that you acquire the better
your estimates are going to be All your
belief will be erased off the moment you
interact See look at this right
Even with all the current day LLM
models
belief does not matter because the
amount of data that we look at in fact
all most of the ML that we do today in
terms of LLM are ML estimates because
ultimately well minimize the K
divergence and we get the ML estimates
as we will see later Okay I already
showed you right empirical risk risk
minimization ERM is an ML estimate Now
initially we had to incorporate a lot of
belief in our model etc because data was
less Now if you have infinite amount of
data the ML estimate the map estimate
will convert to an ML estimate So the
belief does not belief will get erased
However if you have small samples then
see lets go back to the previous
example right in the previous example if
all of them were one so this would have
been one but now this is not one Why
because you have the alphas and betas
that would skew it to whatever the it is
whatever the chosen belief was Do you
see this So this is the map estimate
Now uh I mean some of some more examples
will be done in the tutorial but any
distribution okay the parameter of any
standard distribution can be estimated
in a map framework by choosing a
conjugate
Okay So any questions on this
Okay See there is Ill just uh state
one thing you know without uh uh going
deeply into it See there are methods
this is just for your information
right There are methods where instead
of reading off one particular theta
in terms of lets say mode or something
and using it later you can use the
entire distribution on theta and carry
the posterior belief for further what do
I mean by that remember ultimately at
least for this particular use case we
are interested in looking at the
posterior of y given x isnt it and this
we saw said was proportional to p of x
given Y and this P of X given Y is what
we are estimating now
Okay Now this P of X given Y is now a
function of P of theta given X isnt it
Now you can carry this P of theta given
X and get what is called as a full
basian estimate where the final decision
that you get on Y also has uncertaintity
in it
See in in our base classifier what
happens is that you know you you either
choose class one or class zero
deterministically
but you if you carry this uncertaintity
further then even the final uh so called
label that you get on Y will incorporate
that uh uh you know will also have that
uncertaintity and P of Y given X will
again another be be another distribution
and that uh uncertaintity is carried
from P of theta given it So given a
particular theta you will have this
particular estimate on Y So its like
choosing a family of classifiers
If you choose one theta you are
choosing one model
Now if you have a distribution over
theta then instead of having one model
youre choosing a family of models
So those methods are called fully braian
methods Now Ill not go deeper into
those methods but I mean yeah So later
in the course right when we look at
neural networks there are these kinds of
neural networks that are called basian
neural networks I dont know if you have
heard heard the name of this there are
these methods where the parameters of
the model in this case a neural network
is not fixed
so you have an entire distribution over
the parameters of your model and you
carry the uncertaintity all the way uh
to the end of your decision so thats
the basian framework of uh uh of of of
looking at uh the problem of risk risk
minimization So well not go deeper
into it but yeah so for now what we do
is once we get a post a distribution
over theta we choose one particular
theta and use that for our model that
thats our model remember always in the
parametric case of model building theta
is what we call as our model
right so we get one model by choosing
the mode okay
 this physics informed neural networks is
there can we
 yeah good question the question is uh uh
physics informed neural networks which
Ive not told talked about Yeah thats
see to me um every architectural change
that you do is a basian estimate
right CNN is a basian estimate right
A transformer is a basian estimate any
kind of uh incorporation or rather
restriction that you do on the on the uh
parameter space of any model is a basian
estimate because what you are saying is
you are saying look
my parameters should take a particular
form So later in the course when I talk
about uh uh fully connected neural
networks and CNNs I will show that a
CNN is actually a basian estimated form
of a fully connected neural network
Right Yeah So any architectural
transformers are that way basian
estimates is is my way of looking at
things Ill talk about it later Okay
And this is also connected to the idea
of regularization Ill we will discuss
that in a couple of classes You know
from the uh the empirical risk
minimization viewpoint
Uh we will stop here and continue in the
next lecture
