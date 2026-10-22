---
id: hgZ3HOMkrx0
title: Lec 65 Introduction to Generative Models
url: https://www.youtube.com/watch?v=hgZ3HOMkrx0
date: '2026-04-09'
duration: 37:10
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Lec 65 Introduction to Generative Models

## Transcript

speaker_1: Okay in this class we will look at the
principles of uh generative modeling
So so far in this course
we have looked at the discriminative
models Uh
as I said the in my mind the difference
between a discriminative model and a
generative model is that mathematically
speaking both of them are distribution
estimators The fundamental problem of
machine learning still
uh is the estimation of the underlying
distribution from its samples However
in generative models in addition to
estimating the underlying distribution
one would also sample
The additional thing that would that is
there in a in a in a generative model is
that you sample from the underlying
distribution So the problem with
generative model is as follows We are
still given
a data set
which are n draws
from an unknown underlying distribution
So px is still unknown
The problem with the generative models
is that
well say that the goal of generative
modeling
its linguistically not correct If I
say the problem with generative models
it actually means that the generative
models have a problem and thats what we
are looking at So what I wanted to
convey was the problem that is being
solved right using or with generative
models is as follows So well write
that as goal The goal of generative
modeling is estimate
estimate px
from D
and learn to sample
Lets say learn to sample and sample
So now this part which is sampling from
the underlying distribution is unique to
a generative model and whatever we saw
so far in this course are called
discriminative models in the sense that
we do not uh explicitly learn to sample
from the underlying distribution but we
only estimate the distribution
So please note that when I say estimate
the underlying distribution
all the parametric nonparametric
implicit explicit distribution
estimation techniques that we saw in the
course applies to generative models as
well So there are generative models
that would implicitly estimate the
underlying distribution explicitly
estimate the underlying distribution
What is the difference If you do uh an
explicit assumption if you make an
explicit assumption on the underlying
distribution and solve it through ML
right They are explicit distribution
estimations The initial parts of the
courses we course we saw right You
assume px to be some p theta assume a
parametric form form on it and then
estimate the underlying distribution
through kale minimization And there are
implicit density estimators that we saw
which are like neural network and uh and
uh support vector machines or curl
machines where you do not explicitly
make a distribution assumption on px and
estimate the parameters but you
implicitly say that okay there exists a
hypothesis function and that is
estimating the distribution implicitly
as a function Right If you build a
neural network see we now have the
entire picture Right If you take a
neural network and solve it for a
classification or a regression task
train it for a regression or a
classification task What is it
implicitly doing Is estimating P of Y
given X right Which is the conditional
distribution P of Y given X implicitly
without assuming an explicit
distributional form on it and then
trying to estimate the parameters You
do it implicitly using a an underlying
hypothesis function Right Similar kind
of uh um analysis are there for
generative models as well There are
generative models that would explicitly
make an assumption on the distributional
form and then sample There are implicit
models that would not explicitly make an
assumption but still learn to sample and
so on So all those techniques still
hold true But by construction or by
definition all the generative models
should have a capability to sample from
the underlying distribution So that is
the main goal of generative models So
uh we saw right in discriminative
modeling depending upon what is the
distribution that we are estimating
they have different names for instance
if we estimate the marginal its
typically called the unsupervised
learning if we estimate the conditionals
its called the supervised learning and
so on right similarly for generative
models some nomatures are there and if
you if you estimate or if you estimate
the marginal learn to sample from the
marginal so its called unconditional
generation
Okay if you
if you uh model the conditional
distributions and learn how to sample
from conditionals its called
conditional generation Okay
conditional generative models Now Ill
give you examples of it Youre all
using it today right So if you in in
modern day AI commoditized AI world you
can type a text and ask the model to
generate a picture corresponding to that
text Right that is sampling from P of
X given Y where Y is a text and X is an
image
So that is conditional generative models
and also all the LLMs that you see these
days Okay they are all conditional
samplers conditioned on the input text
that you give it will sample uh from P
of X given Y where Y is your input
conditioning variable or the prompt
so called prompt and P px will be the
you know the the distribution from which
you sample So most I mean the most of
the LLMs that you see are conditional
generated models Unconditional samplers
are the ones where you do not give an
instruction or any conditioning
variable You dont specify a
conditioning variable but you just
sample from the underlying marginal So
this is the difference between condition
I mean generative models that are
conditional samplers and the ones that
are not conditional samplers that would
estimate the marginalss
Does it make sense Okay Now um see
theres an entire course that is being
offered on generative models the coming
semester So that well discuss most of
it in great detail and we look at
multiple families of generative models
and see how they work and so on So this
course is uh just to introduce the idea
of generative models and show you a few
examples of what generative models look
like Specifically Im thinking Ill
well discuss uh this class of uh models
called adversarial samplers also called
as generative adversarial samplers GANs
and variational autoenccoders uh and
auto reggressive samples which are the
samplers which are the LLMs large
language models only these three
families and that two at a very
superficial level well not look at the
complete math of it just tell you the
idea of how it happens and so on okay
right so this is about generative
modeling you estimate the underlying
distribution either implicit ely or
explicitly and sample learn to sample
from px Okay any questions on the
construction Yeah
 distribution estimator
 but the thing is whichever hypothesis
function is ideally the mean of the
distribution and whichever function is
what
 agreed thats implicit Now what is the
parametric for form that the neural
network takes depends entirely on the
architecture and the parameters
right so that you are not making an
explicit distributional assumption right
on the on the distribution that is being
estimated of course it is done at the
final layer which is on y but not at the
entire distribution level you dont make
a distribution assumption on the
marginal or the conditional and so on
 and if we take
 that yeah that is irrespective of neural
network thats the same Right
Irrespective of whatever architecture
you take the moment you take an MSSE
loss for a regression problem youre
assuming that the posterior is gausian
with the mean being equal to the
hypothesis function Thats correct Im
calling that implicit Its a matter of
nomin Im calling it implicit because
the hypothesis function right is not uh
any parametric family so to speak
Thats it Okay Okay So now lets look
at whats the found the fundamentals of
sampling is
Sampling from a distribution
See the entire uh machine learning
revolves around this one simple question
that Ive given you samples from an
unknown underlying distribution
Estimate that estimate either the
distribution or some parameters of the
distribution For instance the
expectations or the moments and so on
Thats the foundational statistical
question that is being asked in all of
machine learning In addition to asking
that question in generative models we
ask one other
question that how do you how do you
sample Okay
now this has been a question that
statisticians have been asking for a
long time right So given uh a
distribution function how do you sample
from it
Okay Uh what do you mean by sampling
Uh well have to define the process of
sampling So remember the the very first
class we said that the only thing that
is not defined in the entire gamut of
probability theory is what constitutes
randomness
Right So after we define or after we
set say that there exists a random
experiment whose outcomes we enumerate
in a set called sample space everything
else follows Everything else is you
know have precise definitions measure
theoretic uh uh correlates and so on
What is not defined is what the
underlying randomness is in the
experiment that we conduct Right Now
the process of sampling Okay How do
you define sampling So we said that
generative model is is is a sampler We
have to define what sampling is all
about Right So again that is something
that is that cannot be just like we
dont we dont we cannot define what
randomness is Sampling is something
that sort of vague in the sense that
sampling is
picking data points from the sample
space
That is what you can So you have a
sample space that is constituted from a
random experiment Okay you pick
samples or pick data points or pick
elements from that set So you have a
set which is called the sample space If
you pick elements okay that gowns the
underlying probability measure You have
to pick the elements from the sample
space respecting the underlying
probability measure This process is
called sampling
What is generation after all So we have
so if I have to go back to the
non mathematical way of saying it that
you repeat the underlying random
experiment is what I should say Its
given a distribution So its sort of an
inverse problem in the sense that we
dont know how to do conduct the random
experiments We have given the outcome
of the random experiment and the entire
story you know So we have the outcome
and on top of this outcome we have this
function called random variable and what
we measure are the elements in the range
space of this random variable That is
what we have as data
You know we are coming the full circle
right You remember what is our data
Data is the
elements or data are the elements from
the range space of this function called
random variable Okay whose domain
happens to be the elements of the sample
space and the elements of the sample
space are simply the enumeration of the
outcome of this random experiment Now
we trace back the problem So far what
we are what the problem that we are
interested in is that given that we have
the elements of the range space of the
random variable estimate the underlying
distribution Now why is that of
importance We saw why is that of
importance you know all the
discriminative problems that we solve of
assigning a label regressing etc all of
these are distribution estimations we
saw that okay so the underlying problem
was given the samples from the uh the
given the uh data points from the range
space of this function called random
variable which is tied to an underlying
sample space with a distribution
estimate the underlying distribution
Now we are saying
given this data which are elements from
the range space of this random variable
function called random variable
you give me more elements from
the range space of the random variable
which goes back to saying equivalent to
to saying that you give me more elements
from the pick the elements from sample
space such that the underlying
probability measure is respected
So this is said youll have to sample in
accord accordance with the underlying
distribution
Ill tell you what that means So lets
say that that I ask you to sample from a
distribution of mn data set Okay
Now if I model the mn data set and
imagine that the mn data set is a um
yeah its a gausian distribution Okay
It I mean it does not follow a goian
distribution Lets say it follows a
gian distribution So in that case any
image okay with any values in the pixels
constitute
a sample from the goian distribution
right because goshian distribution has
infinite support However we want that
does not constitute a good generative
model Now the question is what
constitute a good generative model and
so on The question that we are asking
is we have to sample in such a way that
the exact distribution that we have for
the underlying data is respected
In other words what do you mean by a
distribution on data We already know
that right I mean suppose we have 100
pixels in in in or or 100 dimensions in
data A distribution over those 100
dimensions only mean that with this
likelihood we get this value for this
particular pixel and so on So when we
sample we have to get a vector that
would precisely obey this underlying
likelihood rules for the distribution
Thats what is meant by you sample in
such a way that the underlying
distribution is preserved
Do you see the point This is very
important because you have to understand
what sampling is You know sampling at
the outset is getting and repeating the
underlying random experiment
that generated this particular
distribution and random variable
But we dont have access to the we dont
we neither have access to the
distribution nor we have access to what
the underlying experiment is All we
have are the samples of this function
called random variable The the data
points from the range space of this
function called random variable We have
to work with it Is it clear what
sampling is all about Okay
Now what is our starting point
You know that our problem is to now
uh get data points from the range space
of the random variable which uh obeys
the underlying distribution What can be
our starting point How do we even go
about
sampling from an underlying
distribution
So this is a topic okay that is often
studied in computer science called
random number generation
So what are these These are samplers
from
uniform distribution
The starting point for all generative
modeling is that we assume that we know
how to do this
this is taken for granted
So we assume that we know how to sample
from uniform distribution
Okay Uh okay So Im mostly talking
about uh uh
sampling from marginalss When we talk
of sampling from conditionals theres a
slight variation that will that will
come up Well well talk about it
later But we assume that we know how to
sample from a uniform distribution
Okay uh I keep joking that the the
biggest irony of computer science is
that we have deterministic algorithms to
do random sampling So there are
multiple algorithms for random number
generators which are samplers from
uniform distribution So we assume that
we know how to sample from uniform
distribution Lets say that Z
So Z is sampled uniform
from a uniform distribution thats
uniform between 0 and one We just
assume that we know this Okay So this
is assumed to be known
Okay
Now we we have some seed to start with
So that we know how to sample from
uniform distribution Then we will
invoke all the probability theory that
we studied to solve the actual problem
of uh sampling from uh unknown
distribution Now tell me uh actually
you you actually you all know this given
that I have samples from one random
variable Now the question of sampling
from an unknown distribution
can be cast in a different way Now we
can say that given that I know how to
sample from one distribution
tell me if I can sample from another
unknown distribution
Initially the problem was given data
from an unknown distribution sample from
it Now the question is given data from
an unknown distribution and the fact
that I can sample from
an underlying known distribution Now
tell me how do I get sample from this
unknown distribution given this setup is
the question Okay Do we know the
answer for it
Whats the answer
 Huh
 We estimate that distribution using the
method that we saw
 and use the non sampler to somehow
 that somehow is the actual question
right So how do you do that somehow We
dont even have to estimate the
underlying distribution right Any
other answer
 Inverse
 Inverse CDF is one definite method to do
I mean the answer is theres something
called an inverse CDF method Right So
generalize the idea of inverse CDF What
is inverse CDF
Theres this theorem that says that the
distribution of
the cumulative distribution this
distribution of distribution of a random
variable is always uniform
What do we mean by this You take a
random variable define a function on
top of it which is
the so called CDFR distribution Right
Now that becomes another random
variable Now look at the distribution
of that random variable thats uniform
Thats a known result Now you invert
that So now it means that starting from
a uniform random variable you can
always invert it If you take the if you
take a random variable if you take the
CDF of a random variable and invert the
CDF as a function then the
corresponding random variable will have
the distribution of interest So this is
called the inverse EDF method Well not
go there Okay So this since you
mentioned the name I just wanted to
complete the story Abstract it out
What is the abstraction of inverse CDF
Why does why is that the inverse CDF
method works
So here is the idea Now suppose Z is a
random variable
Lets say the G lets say G of Z is a
function from space of Z to X
Okay So G is a deterministic function
Lets call this as G theta of Z Okay
Then xcap lets call this as yeah xcap
is equal to
g theta of z for z coming in uniform 01
Okay Now g theta is a deterministic
function What we do is we take samples
drawn from a uniform random variable and
pass it through a parametric function g
theta
Now we know that the distribution of G
theta of Z is different
from the distribution of Z right correct
why you take a random variable do a
deterministic transformation on top of
it the distribution of the output random
variable is different from what the
input random variable is is a standard
result all of you know this right its
called functions of random variables if
you take a random variable define a
distrib deterministic function on top of
you get another random variable function
of a deterministic function of a random
variable is always a random variable
Why is that See random variable is a
composite
Remember the first class right Random
variable is not a variable Its a
function So there is a set sample
space Theres a function on top of it
which is your random variable The
function itself is random variable And
if you define a function on top of it
what do you mean by defining a function
on top of a random variable
 Composite
 Composite on what So what is the domain
of this composite now
 The range of the random variable The
range of this random variable becomes
the domain So when you sample from a
uniform distribution what you get is
the range of the elements of the range
space of this Z on top of it define
another function that becomes a
composite and therefore its another
random variable because you can always
define the inverse So from from from G
G inverse takes you to X and X inverse
take you to the sample space which has
an underlying probability measure and
therefore the composite of a random
variable or a function of a random
variable also becomes a random variable
because there is an underlying
probability measure but the distribution
changes depending upon whatever G theta
is correct now the idea is very simple
what do we need now lets call this
distribution suppose
The distribution
of
Xcap
B
P B P B P B P B P B P B P B P B P B P B
Yeah 1 theta 1 xcap we need both of
them right so p thetax xcap okay let me
write it a little more
okay p theta xcap Ill write it this way
okay p theta xcap
now if we can find a theta that would
minimize the kale divergence between px
and P theta
Then
G theta star of Z
is a sampler
for
PX
Do you agree
Suppose we find the parameters of this
transformation function g theta such
that oh sorry this should be a
this does not mean anything So some
divergence measure right
If I take the divergence measure between
these two distributions okay and find
the theta in such a way that this
divergence is minimized then g theta
star of z is a sampler for px isnt it
Do you see this Why So now whats the
final sampler for px Now take this
function take take sample from uniform
distribution pass it through this
function g theta and whatever the output
is is are the sample from are the
samples from px you see this
so this is the foundations of all
generative models that you see the
questions are what form what is the form
of g theta that we should use what is
the divergence measure that well be
looking at and how to solve this
optimization problems the same questions
that you ask for
discriminative models
Okay Ill spend an entire course on
like answering these three questions
What D what G And what is the
optimization problem that we are
solving
 Constraints that are there
 Why do you need a constraint Depends on
what choice of G theta that you make
right Sometimes mostly there its
unconstrained right So theres no
because you you want to estimate the
underlying distribution Any questions
on this formulation
 See what did we do Uh we wanted to
sample from an unknown distribution px
 First question is is it correct that the
distribution cdf of the distribution of
any random variable is
 huh I Im not talking about that you
know just forget about it Thats thats
the yeah that is correct Yeah So see
g theta is any function right So the
statement that I made is take a random
variable pass it through any disc
deterministic function you get another
random variable Now if that
deterministic function is the CDF
function so what is CDF function its an
integral no you take the uh the random
variable and then compute the CDF
function that becomes another random
variable So the distribution of that
random variable is uniform irrespective
of what the inter the uh the input
random variable is thats a different
result So thats and then you invert it
to get the distribution of interest is
the inverse CDF method Im not talking
about the inverse CDF method at all
Right now this is the in fact inverse
CDF method can be seen as a special case
of this Well not get to that now The
statement that Im making here is the
foundations of all generative modeling
is that you assume that you know how to
sample from a uniform random variable or
any other random variable that you know
how to sample from and learn a function
on top of it such that the transform
random variable will have the same
distribution as that of the the
distribution from which you want to
sample Right How do you do that is by
minimizing the divergence measure
between the actual distribution and the
distribution that this function is
imposing Thats it Now again the same
questions exist right we dont know px
and we dont know what some in some
cases we dont even know what p theta is
right so now how do you get p theta how
do you solve this optimization problems
are the details that we will work out
but the the foundations the idea the
underlying idea is this that you start
from uh see what changed from the
generative modeling and the the
discriminative modeling is that in
discriminative in gener in
discriminative modeling we dont start
from an arbitrary uniform random
variable
Right But here we start from a
arbitrary uniform random variable and
then we transform it into distribution
of interest Thats it
See uh a sharp mind will ask now right
uh suppose your g theta is a neural
network
in discriminative case x is still your
input data which the neural network
takes is still coming from a random
variable right because it has a
distribution Now that can also be seen
as transforming a random variable
Right So why is a discriminative model
not a generative model
That is why I keep saying that every
discriminative model is a generative
model that would sample from the this
conditional distribution
because it is transforming a random
variable X to a random variable Y
through a distribution uh through a
discriminate through a deterministic
function which is a neural network So
that way even discriminative models are
generative models which are samples from
P of Y given X
right but here we are sampling from P of
X the marginal The way we do it is
start from a uniform random variable
take its samples transform it through a
deterministic function and set the
parameters of the deterministic function
such that a divergence measure between
what the output of the deterministic
function gives and the underlying
distribution that you are trying to
measure Thats it
H
 is the data point
 No no no X is a data point that we
have Z is sample from a uniform
distribution
CR samples from uniform distribution
People call it noise
right Or the random seed or whatever
right So you have
I mean to me its just transforming one
random variable to the other Thats it
Any other question here
 Sir do we assume that Z has a
corresponding data
 where
 No we are not at all assuming its only
a distribution level matching sum C can
give us data which is not part
 it should give no otherwise if it just
learns a one to one map from uh this the
some data points from Z or rather this
distribution that its not a generative
model generative model is the one that
learns how to cover the entire thats
why we are matching it at the
distributional level not at a sample
level and also remember that we are
sampling from a continuous random
variable right so there are no there are
infinite samples the set is this the
cardality of this set is infinite
Right So otherwise itll itll just
remember what whatever is there and then
just map one point to thats not what a
generative model is We need to estimate
the entire distribution so that when we
sample we sample the points that we get
right are not from D
should not it should not be from D So
that is why when you ask some of these
generative models today to generate a
picture or something it will not
generate something that you already know
right one one fun
exercise that I always ask my students
to do in my generative modeling course
is to open a particular website called
thisperson does notexistcom
right so every time you know you uh
refresh that website whats happening is
you get a picture which is nothing but
you know you take a z from a uniform
random variable and pass it through a
particular g theta which is called a
style gan
and you obtain an XCAP and display that
thats it and that person does not exist
because youre sampling from the
distribution of human faces and you get
a picture that is I mean if your if your
G theta is good enough and if your
optimization technique is good then you
will estimate px properly so now the
question is how do you evaluate these
generative models remember that even for
evaluation we dont have px
all we have are still d so but in
discriminative models what do we do we
take
we is partition that into training ent
data and we have metrics to do that
Similarly we have metrics to compute
This is something called FID and so on
which Ill talk about maybe in the next
class So there are metrics to uh uh
evaluate how good at this generative
model is But the idea is distributional
level matching not a one to one point uh
point level uh mapping that is to be
done in that if if thats what happens
and its a very bad its actually the
overfitting case of a generative
modeling right yeah
 in case people might end up sampling one
of the data points in that case the
person exists
 yeah because you are talking about uh
data in some tens of thousands of
dimensional space right sampling from it
uh what the odds of you remember that
thing that I said no the odds of hitting
that one particular point in fact from
you we all know that if the random
variable is continuous then uh the
probability of obtaining one particular
point is zero
thats it so thats why its almost
always you dont get it thats why even
with LM right every time you give the
same problem itll give you different
answers because its samp its actually
sampling from the underlying
distribution
see LLMs are samplers for the entire
universe This px is the entire universe
You take the entire universe
distribution of entire universe D make
your d trillions of samples and and use
the same techniques to
uh learn the underlying distribution
Any other question on the philosophy of
our generative modeling is yeah
distribution and map it to the random
 distribution of interest Yes
 we map it to the data
 distribution of interest to take
samples from uniform distribution and
map it to the distribution of interest
data whatever distribution that you
youre trying to model This is for
unconditional generation Well get to
conditional generation in a while Yeah
 This concept of sampling
dimensions
 No no no This is still
multi dimensions right All your random
variables are in RD
right Yeah So these are uh Okay I
mean I I wrote universe of Z
See I can I can actually I mean to make
it general I can always make it a k
dimensional uniform random variable from
and this function is from
this is how it happens typically
start from a k dimensional random
variable uniform and map it to a d
dimensional random variable which is
what we have okay anything else Okay
actually we already know a few
techniques to do this Youve been using
this Theres a function called rand n
Do you know this It is what is this
What does this do You know what this
does
 So r nd is a random number generator
which is sample from a uniform
distribution What does rand n do
Sample from a gian distribution or a
normal distribution What is it doing
We are already sampling We know how to
sample
So you have perhaps you would have
already studied in your probability
theory course that there is a function g
that would transform a uniform random
variable into a gshian random variable
Right What is it called Theres a name
for it No I dont recall the name So
it has some e power square root of this
thing or that I dont remember the exact
form But there is a deterministic
function that takes a uniform random
variable to a gshian random variable
Right
now we know how to sample from a gian
random variable as well So suppose you
need uh uh uh data okay that has
infinite support
Start from sampling start start from a
gshian random variable and then
transform it
Is that all right Okay Uh so now for
those random variables which we know
what function gives us what
transformation gives us this random
variable then we can come up with a
deterministic random variable Okay but
for arbitrary distributions naturally
occurring data theres no way that we
can come up with this sort of a uh
function thats why we resort to
divergence minimization to do this
Okay So let us look at a few methods to
uh solve this problem As I said uh
because these lectures are very very
introductory uh
Ill not derive this from first
principles you know Ill take a top
down approach uh which is very atypical
of this particular course where Ill
tell you the algorithm and you know hand
wave the math its always the other way
around right so well do the algorithm
the math and then hand wave the
algorithm its the other way around now
okay because theres an entire course
that is coming up where we do everything
from first principles so let us look at
this first class of uh algorithm which
are called adversarial networks or so
generative adversarial networks
Uh we will stop here and continue in the
next lecture
