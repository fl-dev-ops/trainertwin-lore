---
id: TSNsiglfduQ
title: Lec 24 EM for GMMs
url: https://www.youtube.com/watch?v=TSNsiglfduQ
date: '2026-02-11'
duration: 30:27
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Lec 24 EM for GMMs

## Transcript

speaker_1: Okay so this completes the EM
algorithm So now what we will do now is
we will see how to uh implement this EM
algorithm for the case of the mixture
densities that we saw Okay that is
what we will see now Let us look at
that Now EM algorithm for GMM I will
write down the equations okay And skip
the algebra Take algebra as an exercise
and please do it So I will formulate
all the distributions
uh mst step is what I will leave as an
exercise that argu to just differentiate
that function and you know find out what
the next iteration is we will well stop
at that okay so let us look at this so
for a GMM first of all uh p theta
of x
is what we need okay now recall that for
a latent variable model
p theta of x is given
the marginal over the joint distribution
between X and Z Correct
Okay Now in a GMM how do you write
this
You have this Z Okay What is a GMM
 It is uh some alpha J times normal
distribution right And we have uh mujs
and sigma js Correct This is what a
GMM is
This is over J
Okay Now this can be looked into as a
joint distribution Y So what is
actually happening here is you can write
this as
P theta of
Z times P theta of X given Z
This is writing the joint distribution
as product of conditional and marginals
Right Now can you see uh the the
similarity between uh the second step
and the third step Okay We can model P
theta of Z to be or rather Z to be
a discrete distribution
Okay With parameters
alpha 1 alpha 2 up to alpha m
So remember we just saw a discrete
distribution right So z is a discrete
random variable in this particular case
which can take values 1 to m with
probabilities alpha 1 through alpha m
So somebody asked me a question two
classes before right Why should we
take this alpha to be uh bounded between
0 and one Its because of this So
these are probabilities
We are looking at discrete random
variables and these are the
probabilities of of taking this
particular mixture So Z is this and
what about this random variable X given
Z
X given Z is a univariate gausian
okay with mean So S equal to particular
J So mu mu is equal to
or or you take muj and sigma j
right now Therefore
this expression now okay is exactly
this So p theta of zj is alpha j and p
theta of x given z
is a question
is that all right
okay this is the joint distribution now
actually right I mean gmm
can also be used as a sampler Its a
generative model
I will not talk about it yet You know
Ill talk about this at the end of the
course when we look at the generative
models and Ill revisit GMM later in the
course But I just give you the
intuition Whats happening is like
this Goian mixture model can be looked
into as you first toss a coin or not
toss a coin I mean here roll a dice
Roll an Mfaced dice Now depending upon
what face it turns out to be you pick
that particular goion and then sample
your X Thats what GMM is doing So if
there were nature generating data okay
you assume that your data is generated
When you assume that your data is
generated according to a GMM what is
actually happening is this nature first
rolls a die an Mphase D with
probabilities alpha 1 through alpha J
Then some phase comes up conditioned on
that particular thing You sample from
the mat Gaussian Thats it There are M
such a thats exactly whats happening
here See any
uh latent variable model can be
interpreted that way So first you
sample from P theta of Z then you sample
from P theta of X given Z thats it
thats what is happening See any joint
distribution is that way you know you
first sample from one of the one of the
distributions and then conditioned on
that particular distribution and sample
from the other That is what is
happening Okay So this is P theta of
uh X uh P theta of X and Z and this is
your P theta of X Is that all right
Okay Now
let us work out em for this So what is
theta here for this particular thing
Theta is that we have
we have alpha
set of alphas from okay let me write
that alpha 1 alpha 2 up to alpha m and
we have mu1 mu2 up to mu mum We have
sigma 1 sigma 2 up to sigma m These
are the parameters that we want to
estimate for this model
All right So all alphas are scalers
Okay All mus are in RD and all sigas
are in yeah all matrices
All right
So lets write down EM
So what should we do for EM
Initialize
initialize theta right Initialize
theta uh theta t Okay we we already
have theta t Now what should we do
Well have to now first compute
the variational distribution
Compute what Q T plus 1
What is this equal to Is equal to P
theta of
 Z given X
 the posterior What is at theta T
Right This is computed at theta T What
is this equal to This is lets use B
law
times
divided by
the sum of this
Correct
Okay Do we know all these
distributions What is P theta T X given
X X given Z Thats a normal
distribution
right computed at
it is mut
correct and this is times alpha
right and divided by that entire thing
you take that and sum it the same term
over J
Is it all right Can we compute this
We can compute this So I will not do
the algebra You can compute this
Youll get a closed form expression
Please complete it Do it Okay You But
we can compute this algorithmically Any
questions on this So we got our Q
T Z
 This will be computed for every J
 Which one Then you will
 of course absolutely correct this should
be computed for each J because this is a
distribution over Z You dont have to
do it for every Z See this will become
a function of uh J Thats it See Z Z
is a discrete random variable with M
possible values So this distribution
will be a discrete distribution with M
possible values So this is the
normalizing constant in the denominator
Whatever you have in the numerator will
be a function of J and thats why you
have M values Thats it
Its a distribution What youre
computing here is a discrete
distribution with M values Is that
clear So when you do this for every J
you get a different value Of course
right Thats a distribution over J
All right We know all of this right
We know
alpha JT we know mujt sigma JT and so
on because we know theta t
Everyone clear with me so far Okay
Now what is the next step
Compute
f
theta of
QT plus 1
This is the expectation step What is
this equal to
Expectation of
 log
No this is P theta
X and Z divided by
T plus 1 It is with respect to T plus 1
Okay let us write this What will
happen to this
So this QT plus 1 is now
should I write it again Okay let me
write it again
Expectation is with respect to
the distribution
Just being a little lazy Em algorithm
does not let me be lazy
Okay let me write it down
So this QT plus 1 is what
Z given X
right This is what it is
Correct Yeah
This is equal to this a distribution
over Z So we have a sum over Z
Correct The sum is over Z This is log
of what is P thetax and Z P theta X and
Z is P theta X given Z time
P theta Z divided by
P theta T Z given X
right now this is equal to
log what is P thetax given Z
its a goian
But
please note that there is no t here

Okay Because we will differentiate this
with respect to muj
And when we put it to zero we get muj
t plus 1
You see what Im saying Theres no t
here Okay And this is what is the
second term
alpha J
So if you can appreciate why there is no
T here then you have understood the EM
However in the denominator
there will be a T
What is P theta Z given X
this entire thing that we have computed
here
 I will I cannot write it there but we
know what it is
d I will write it as d and this d nom
this is what we have computed
and note that this denom is a function
of t Sorry I mean theta t Its a
function of theta t
Do you get it Yeah

Its not the
 which one
expectation would be probability outside
 there will be an alpha term outside
 Yeah So there I was going to write it
So there is a what term is this This is
alpha j t
because the expectation is with respect
to
p theta tz at given x
Yeah there will be a this entire thing
is multiplied by alpha
This is J equals 1 to M
See just just to lighten the mood
right Ill just tell you one I was a
student This EM algorithm is uh general
enough to be applied to any latent
variable model I told you right There
are another class of models which are
not uh used very seldom which is which
are not used very often these days are
what are known as hidden marovian models
and hidden marovian
models with gian mixture model
transition probabilities Meaning there
imagine that there is another level of
stoasticity that is on top of it Okay
which which means that there will be 20
other notations
and youll have to work out em for that
Okay Now I had a I had a book uh my
notes where I used to write all this and
after this class I wrote I mean I still
have that book with me In the first
page of that book I I wrote beware
notationally hazardous
So you you run out of alphabets right
when you are doing some of these
statistical stuff anyway So you
understood why there is an alpha pj
here
Right Now what should we do
So what is this LHS The LHS is
F theta evaluated with QT plus 1
Now the part that I will leave to you as
an exercises thats actually easy Easy
meaning algebraic Algebraically easy
Youll have to do that Well have to
find mu t plus 1
Okay
J as
will you please do this I want you to
complete the algebra So what is to be
done is that youll have to
differentiate this entire thing
with respect to muj
So this thing now will become a function
of
a mujt sigma jt alpha jt and so on
which you have access to and you do the
same thing for sigma you do the same
thing for alphas
 how do we have access
 hold on it will also be a function of x
because theres an x here no because
remember that we all we started
everything with data and also remember
that we are doing all this for a single
data point
and whatever estimate that we get well
have to put a sigma i equal to 1 So
this what will happen is this will be x
i in that case we are doing it for the
iat data point we do it for all n data
points well have to just put a
summation over all n data points after
we get this this is for a single data
point now you understand why I did it
for a single data point otherwise there
should be another summation outside it
and so on so we are maximizing the
likelihood so when you do this itll be
a very nice you know itll come out when
you differentiate this and put it to
zero the muj t plus 1 term will simply come
out to be a function of mujt sigma jt
alpha jt not only one j it will come as
a function of all of them because
denominator has a sum over all of them
you see
and itll also be a function of x of
course because its we are data that we
are looking at
okay so this completes
the em algorithm for finding the
parameters of a gm
Okay Uh any questions on please
complete the algebra cuz I if I do the
algebra itll take me 90 more minutes I
just have to write down differentiated
12th class calculus Please do it Its
not complicated at all Do it Huh
Any questions on this
See this EM algorithm uh five more
minutes
This EM algorithm is general enough in
the sense that you can apply it for any
latent variable model
The only requirement is that if you want
to apply it youll have to have access
to the correct variational distribution
which is the posterior of Z given X So
why is why was this possible in this
particular uh case See just not notice
this uh I dont know if you noticed this
or not in the case of a mixture density
not only go mixture model any mixture
density we have access to the posterior
because we can use base theorem
and write down the posterior in ter
terms of the uh conditional
distributions and the pri prior or the
marginal and this we know because every
any mixture density this will this is
the probability with which you select a
particular mixture
So you can look into a mixture density
as a two step process You first select
a particular mixture component and then
you sample from that particular
component Suppose you have m gian
densities that you are dealing with
What you are actually doing is first
sampling from what First sampling from
a discrete distribution to select which
density that I have to sample from
Please note that this first level of
sampling is to select which of the
 which of the goians to sample from The
second level of sampling is actually
sampling from your data space which is
RD The first sampling is in the
discrete space See Ill give you a
concrete example Lets say that we are
modeling
the uh the images of X ray that we have
using GMM
Do you still remember those X rays
or we come too far We are not actually
you should not come too far I mean you
should remember the entire thread Okay
Now you remember what are we doing We
are trying to model the underlying
distribution for that
as a GMM
Now the first sampling that we do which
is rolling the dice the Mphase D
is telling me which gian to choose from
So there are m gajians here with their
own mean and their own variances Now
the first level of sampling will tell me
that okay choose from the fifth fifth
gausian Now I have to sample from that
fifth gausian density When when I
sample from the fifth gshian density I
get a vector of RD right because Im
talking about gian in RD So I get a
vector in RD and that is my image
We are assuming that the nature has
given us images this way that it first
throws a die mph face die and then it
selects which gian to sample from and it
samples from one of the gshians and that
is what we have as data
So now you can see why this is a
generative model as well because suppose
we are given some data
we run em and get a GMM still remember
that we are trying to minimize the k
divergence between this this is our p
theta and we have our px If we have
done this well then we have gone close
to the underlying actual distribution
which means that I can actually generate
data now with this how I know how to
roll a dieice and then I know I know I
know how to sample from a Im assuming
that you people know how to sample from
a gshian distribution
do you
do you know how to sample from a uniform
distribution
the biggest irony of the world right you
create a deterministic algorithm to
sample from a random distribution
Thats a random number generator You
have pseudo random number generators
right There are deterministic
algorithms to sample from a probability
distribution
Ironic
Anyway so we if we know how to sample
from uniform distribution we also know
how to sample from gshian distributions
How There are these deterministic
transformations that take from uniform
distribution to gshian distributions
right That cauti transformation that is
there So now if we know how to sample
from coian distribution then we already
have our first generative model here If
youre given data this will be part of
your assignment by the way Given data
run em
and then sample from a discrete
distribution and then conditioned on
that discrete distribution sample from
that gshian distribution with the given
mean and variance that you have gotten
from running EM And that should look
like the image that you have that you
have in your data
Okay So thats why GMM is also a
generative model because implicitly it
will allow you to sample
Now in our case we are using this to
estimate our class conditional densities
because remember our goal was to design
a base classifier
Okay So yeah questions on this

No not choosing the sampling from GM
 Yeah

 That is sampling from GMM
 No no no no You see thats what Im
saying Itll tell you which gian to
sample from And if you know how to
sample from a gausian you get a data
point which is an image
So that is why I asked you know do you
know how to sample from a gian
distribution Suppose I give you a mean
and variance of a gshian distribution
Do you know how to sample from it
Thats why I asked you actually we do
because if we can sample from a uniform
distribution then we can sample from a
gshian distribution as well

 I agree I mean I just this is this was
an off a detour where I told you that
GMM can also be used for sampling as a
generative model But yeah
 if you sle then you kind of generated
 sampling is generation
 right then
 to me generation is sampling and
sampling is generation thats it
remember our initial discussions on guys
hello remember our initial discussions
on sample space and random experiments
and so on right what are generative
models generative models are the ones
that will carry out that random
experiment and we have the entire
machinery to take care of Right I mean
we have this random variable as a
function Finally what you get is an
element from the range space of this
random variable function By conducting
that random experiment thats a
generative model All generative models
are samplers They are actually
samplers
Okay Again as I said theres an entire
course on generative modeling the next
semester that Ill be teaching So yeah
So GMM is the most primitive generative
model that that one can think of
Yeah
Good question There are certain models
okay where zed is taken to be
continuous But at least for the mixture
densities zed is taken to be discrete
But nothing stops the math does not stop
you from considering z to be a
continuous random variable
The last

we will be
Oh dick should be
I think thats a thats actually the
correct observation because the
expectation is with respect to
 yeah so this should be
Thanks for that This is this is what
you are saying right This is correct
Yeah Yeah Note this correction
Okay So this this had to be P theta
But we know this right This is our
this is our uh QT plus one that we have
computed at theta T We know how to do
this Yes thanks for noting that down

Okay So next class what we will do is
we will uh look at the maximum a
posterioriary probability estimates or
map estimates which is a basian way of
estimating the densities See so far uh
we have assumed the entire dependency
that we have right now Okay Uh is on
data meaning we are minimizing the K
divergence between P theta and PX Okay
And we are estimating only by looking at
data but data can lie
Example
suppose you are estimating the uh the
probability the parameter probability of
success of a Bernoli random variable
which is a coin toss We we saw what is
the estimate right The estimate is
count the number of times it is
favorable for the particular thing and
divide by the number of events right
number of iterations We just saw that
right we did it for a discrete
generalized discrete random variable
Now suppose you are tossing a coin okay
you toss it five times you have five
data points
and its a fair coin and all of them can
turn out to be heads possible Now what
is your ML estimate for that parameter
P
It will be one Thats a very bad
estimate
You have just got an unlucky right So
the the moral of the story is relying
only on data is a bad idea
especially when you have less amount of
data
So what do you do So you have to have
other mechanisms where you incorporate
your belief about the system that you
have into the estimation uh paradigm
For instance in this example that I
just cited suppose I know that Im
dealing with a with a biased coin I
know for a fact that
probability of head cannot be one
But my data ML estimate is telling me
that this probability is one So I know
that its a bad estimate Now can I
incorporate my belief that I know that I
have into my estimation paradigm is the
question It turns out that you can
Right How do you do that By assuming a
distribution over the parameter space
itself
So far we have assumed our parameter
theta to be a deterministic
variable Right Now you say that with
certain probability my parameters can
take value So in mathematical sense Im
assuming a distribution over theta
which is my prior belief that I have So
I already know that with certain
probability my theta can take these
values Whatever Im estimating can take
certain values with certain
probabilities is what what I know
already So how do you incorporate that
into your uh estimating paradigm is the
question that well be asking ne next
and these methods are called basian
methods for parameter estimation out of
which we look at one particular method
which is called the map estimate maximum
aposterior probability estimates and
then we will move on to uh nonparametric
densities Okay so thats it uh that
that brings us to the end of this class
Thank you for attending
