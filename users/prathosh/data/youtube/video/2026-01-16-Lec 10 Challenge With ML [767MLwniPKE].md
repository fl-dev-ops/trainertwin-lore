---
id: 767MLwniPKE
title: Lec 10 Challenge With ML
url: https://www.youtube.com/watch?v=767MLwniPKE
date: '2026-01-16'
duration: 35:31
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Lec 10 Challenge With ML

## Transcript

speaker_1: Welcome back
So please be informed that if I write px
pxy py given x
or py it doesnt matter
mathematically its the same problem
that Im trying to solve just that
interpretation changes
Are you all comfortable with this You
should be super comfortable with this
because sometimes I will write px
sometimes Ill write px given y
sometimes Ill write p y given x and so
on deliberately because you know its
the problem that we are trying to solve
right depending upon what problem we we
are trying to solve we will estimate the
underlying density right so this right
is
I think
let me just push it a little to my left
so that it comes in the same

 see this boxed item is what is the
central problem of machine learning
its an nomin again where is a machine
here what is learning and all that Ive
not told you that right I mean there is
I mean theres a machine which is a
which is a compute unit right thats
what thats all it is but anyway so this
is the central mathematical problem that
we are talk talking about and as I I as
I told you what the what is this what is
the main problem associated with this is
that pxis the main challenge is
so px
is unknown
both from
or or Ill write it as
completely unknown
So we know nothing about px
We have zero information about the
underlying distribution But we still
want to do it
Seems like a herculean task right Cuz
if you if you know something about uh
the distribution you can perhaps think
of estimating it No we have no
information about px However are we
totally blind
 We are not totally blind Why we have
samples from it So thats the central
problem So given samples from an
underlying distribution can you learn
the underlying distribution Thats it
So if the problem were well defined
okay and uh
uh completely tractable then you dont
need hundreds of different algorithms to
solve it
And by the way uh Ill introduce
another nomature Uh every algorithm or
the estimates that you get for this
underlying distribution is called a
model

 you get an estimate for the underlying
distribution right Thats what a model
is So in large language models the
model is actually an estimator for the
distribution
And Ive told you I mean anybody who
has studied the estimation theory 101
knows that all estimators are wrong by
definition and therefore all all models
are wrong But some estimate estimators
are useful and therefore some models are
useful So here is the statement All
models are wrong Some are useful
because they theyre density estimators
Because theyre density estimators
there cannot be one correct density
estimator right But you can compare
density estimators depending upon their
metric some metrics
Challenge is that the underlying
distribution is completely unknown and
we have to get it from the samples
So this is the central question that
well be asking So given a
distribution how do we estimate given
samples from an underlying distribution
how do we estimate its sample So that
is the central question that we are
asking So let us see how to do that
Okay Ill give you the broad framework
of how to do this Then we will see
several examples of how is how is it
done Okay
Now lets consider So consider
we have
you have a data set
data set D
which contains
which are ID drawn from
unknown underlying density px
And by the way this is
this is also a sort of misnome Its not
completely mathematically correct
because we cannot you you cannot sample
from a density function You can only
sample from distribution functions But
yeah so I will make that leap of faith
and write it Okay So sampling ID from
an unknown density and this is what we
are starting from right The goal is to
estimate the underlying density Okay
Now any estimation problem
remember in the very first class I
talked about a function approximation
problem right you have x and y which are
samples from two given sets and we are
learning a function with between those
two sets and uh all we have are samples
from that We dont know anything about
the function So what has been the
historical method to do it Historical
method to do it is that you start by
making some assumption on the unknown
function and then try to solve an
optimization problem Thats what I told
you how to do it H because if youre
totally blind you cant do anything
You have to start with some uh some some
stick or something right totally blind
is completely lost
Now mathematically speaking the way to
do it is assume
a functional form
on px
You assume a functional form on px or uh
better way to say it is
Assume a parametric functional form 1
px Okay Uh denoted by
p theta
We are estimating the underlying density
function Okay we dont know anything
about it What we say is that let me
assume that my underlying density comes
from a parametric family of functions
call it P theta Please remember what
are we trying to estimate Remember that
we are trying to estimate a function
from the range space of the random
variable 2 R plus by definition This is
what we are trying to estimate Okay
And
we assume that this function has a
particular parametric form P theta
So what do you mean by a parametric uh
function A parametric function is a is
a mathematical function object that has
a few parameters you know one example
can be a line So let me give examples
right example can be so p theta 1 or uh
what do I call it
p a is of x because its on x can be
running out of alphabets I told you so
lets say that this is w1 times so x is a
vector so lets say that x uh is in rd
if its in rd then this is w1 transpose
time x plus uh w2
where w1 and w2
are also in RD
right so here theta
is w1 and w2 this is one example now I
can so this is one example that I can
take for w1 and w I mean uh the
parametric family the other example can
be
that I assume this to be
a gshian distribution right
with this particular density function
and this can be
so this is uh I mean this this n
represents that Im looking at Im
assuming that all of you know okay maybe
just for sake of completeness Ill tell
you see when we talk of density
functions there are a few
wellestablished
standard density functions So examples
can be a gausian density function right
and an exponential random variable
density function or if you look at
discrete random variables then you have
the Bernoli random variable and so on
right we will look at a few examples
later these are some standard examples
of density functions so you can take
them you can take those to be uh your
choice for your functional form so it
can be a gosh distribution which has
parameters uh mu and sigma okay in this
case your theta is the set of mu and
sigma
right uh mu is another vector in RD and
sigma
is a vector in R d by d
correct this is a goshian distribution
and so on you I mean see this
is your model choice
you have to choose a model and we will
see 10 different examples for these
these this p theta in this course okay
well also study why why one model is
better than the other and so on right
what advantages can it offer and so on
and the so called neural network or deep
neural network is one such example for
this p theta well see what sort of
examples we can take so thats the
design choice so given a problem so what
you are actually given is this right you
are given n samples from an unknown
distribution right you want to estimate
the underlying distribution what you do
is you start by making an assumption on
p theta and thats your model choice you
choose a linear linear regression or you
choose a logistic regression you choose
a neural network you choose a kernel
machine you choose a GMM you choose a
transformer All of these are PTA theta
choices for this PTA Thats it
Make sense We will see multiple models
in this course Now thats thats each
model Okay So you make an assumption
So then once you do this now you have
already fixed a particular model Okay
The degree of freedom is already lost
How
You are making a big leap of faith that
the underlying density function actually
has this functional form
So somebody asked a question 10 minutes
back How do we know whether that is the
particular density function that density
functional family that my density
function belongs to We will definitely
not know However thankfully we have a
few functional forms that are known to
be universal function approximators
in the sense that if you choose the
parameters of those functions properly
then they can approximate any function
to arbitrary closeness Mixture
densities are one such family which we
will see later and neural networks are
one such family So that is why today
the go to choice for this P theta is a
neural network because the neural
networks are families of functions that
can approximate any function to
arbitrary closeness Thats called
universal function approximation
capability Thats why you choose such
models in practice However once you
choose a model P theta you are making
this big leap of faith that my
underlying density function is a member
of this family For instance if I
choose my underlying uh model family or
p theta to be w this this particular
form this is called a linear model If
I choose it to be this form then Im
saying that my density function can be
represented as a hyper plane or a line
Its not a line because line is in one
dimension Its a hyper plane in three
dimensions You assume that its a line
that that that my density function is
Now what is what if your density
function is actually a quadratic
function Uh youre lost Its a its a
very bad model I told all models are
wrong This is a very very wrong model
or rather a worse model But you are
stuck with it You know the moment you
make a choice for P theta the algorithm
will not take care of
the model It will only take care of
given that I have made an assumption
that my reality or the underlying
density function is a line Tell me what
line it is
Thats an algorithm
Okay So how many lines can exist in
practice in RD or rather in theory in RD
infinite line can exist because every
line is separated by these two
parameters right the in intercept and
the slope If you change the intercept
and slope youll have a different line
So once you do this so assume this is
the recipe Okay the recipe to solve an
ML problem is the following Right The
first step is assume a parametric
functional form on px denoted by p
theta This is the first step So this
is your model choice This is also
called the model choice make a model
choice
or choose a model
Okay once you do this what do you do
Chosen a model This next step is
huh
What do you mean by that
Mathematically they have not even
talked about an algorithm Im
abstracting things out even at a at one
level higher Okay The next thing to do
is define or compute

a distance metric
between
not define actually you actually have to
compute a distance metric between
px and p theta
See what is the problem that we are
solving right now Uh we have made we
have assumed that uh my underlying
density has a particular functional
form The question that we are asking
next the next logical question to ask is
given that my density function is a
normal density tell me which normal
density it is
cuz there can exist infinite normal
densities Right If you change the mean
and the variance of a normal density you
will get a different normal density Now
having fixed that my underlying density
function is a normal density the next
logical question that that Ill be
asking is amongst infinite possibilities
for this normal density tell me which
normal density should I choose to do
that I need a notion okay of
 how good or bad a
particular choice of normal density is
Suppose I choose my normal density What
do you mean by choosing a normal
density fixing the mean and variance of
the normal density or this theta right
these are called parameters let me write
that so this theta are typically
referred to as parameters so if you fix
a particular value to this parameter you
will get a different model suppose you
fix a particular value to this parameter
you will get a model now I need a way to
tell you how good or bad a particular
choice of this P theta is
how do we do it mathematically if there
were a A to quantify the distance
between density metrics The larger the
distance is the poorer the model is
Correct So first we need a way to
define a distance metric between the
true density that we are trying to
estimate and the
model choice that we have made Thats
what we need to do So lets call that
as
I was supposed to use capital D for
this Now again
I have used D already for data sets Let
me use small D So let D denote
the distance metric

between PX and P theta
Did you notice that I wrote distance
metric within quotes Cuz the metrics
that well be using in practice are not
metrics
in the sense that a distance metric has
to have a few properties such as being
symmetric and uh and uh uh and obey the
triangular law of inequality and all
that The metrics that that are used
currently in machine learning do not
have those properties and therefore they
are not metrics
some notion of divergence or rather
distance between distributions thats
why I put this thing within quotes
theyre not matrix metrics
mathematically speaking right so its a
function what is that its a function d
which takes px and p theta as inputs
okay and uh maps it to some positive
real number right so its a function
that takes two distributions as input
You see so its the cross productduct
of two distributions that it takes as
input
and maps it to positive real numbers
because we need the notion of distance
right It cannot be negative It should
always be non negative So therefore
this is the kind of function that we
define Okay fine Uh lets say that we
define this and we theres a way to
compute most of the ML algorithms
right So this is easy Making a model
choice is very easy
Why Because you just choose a function
Okay The the algorithmic difficulty
okay comes when you comes in the
subsequent steps The second step is to
define this distance metric Now this
definition is also easy Just like you
choose a model you choose a distance
metric between them And by the way
what differentiates one ML algorithm
from the other is the choice of this
function obviously and the choice of
this metric also
In fact there is the third in the in the
recipe we have the third step where we
find the parameters by solving an
optimization problem The algorithm that
is used to choice to to solve that
optimization problem is also what
differentiates one ML algorithm from by
the other So I give you the recipes
put one here one there one there you get
one different ML algorithm that is what
we will see several examples of this you
know several uh algorithms in this
course but this is the general recipe
right So choosing a distance metric is
not difficult In fact what is
difficult is to compute this distance
metric because
were sort of begging the problem If
you look at it we started by saying
that we dont know PX
right But the distance metric that we
defined well take PX as an input
Now arent we begging the problem
Arent we coming back to step one
Because we dont we started by saying
we dont know PX Now we need PX to
compute P theta Turns out no So there
are statistical methods where you can
compute See this is where things like
you know law of large numbers and the
the other probability theory ideas that
you studied comes handy We will see
that as we go in the as we move on in
the course So they are not mere useless
mathematical constructs They theyre
constructed for a for a reason and we
will see the usage Huh So now yeah
hold on hold on let me complete So now
uh we have to compute the distance
metric Assume that we we will come up
with algorithms to compute it So we
need a distance metric So now what what
have we done We have chosen a model We
have a distance metric assuming that and
we know that we can compute it So now
given a model it will tell you whether
how far or close this model is to
reality is
fine What is the third step The final
step is Ill complete this and then take
your question The final step is
find or estimate theta
Estimate the parameters theta
by solving the following optimization
problem
What optimization problem well solve
We will seek a theta which I call theta
star the optimal parameters
such that
the distance metric that I have defined
between px and p theta
is minimized
and you know what this is referred to as
in ML community this is called training
training training the model Okay I
want to write that I can write that

See this course wont teach you anything
different than what is already there
But Ill tell you the story from a
completely different angle which is so
broad that you can en encompass hundred
other different stories within this
framework Thats the objective of this
course So everybody knew that models
will be trained in ML
 right But yeah so this
this this is the framework that we
construct here Okay So that thats all
it is So how do we do now our problem
boil down to given D solve this
optimization problem
And Im assuming that all of you know
this notation Ill be using this
notation multiple times Argu
 for the benefit of uh
the online audience Ill just define
it See arg min
is the argument Yeah Not argument
minimum So if I write arg of a
particular function the question that
Im asking is suppose I minimize this
particular function Okay With respect
to this parameter theta at what point
in theta space does this function
achieve its minima
The argument at which the function
attains minima Its not the minimum
value of the function that Im seeking
Im seeking the minimizer
or the argument of the function that
minimizes this function Ill be writing
this So thats the recipe Lets walk
through it Now this is the entire
recipe of what well be doing in this
complete course Well be well be
seeing 10 different methods of doing
this Okay The input is that we are
given some data set D Okay Which
contains samples that are drawn from an
unknown distribution and our interest is
to estimate either the distribution or
some surrogate of it depending upon what
the problem is What is the uh recipe
that we use is that we start from
assuming a parametric functional form of
the underlying distribution that we are
trying to estimate Okay And then
define a distine and compute a distance
metric between the true distribution and
the assumed model distribution and find
the parameters of that model by solving
the optimization problem that would seek
the minimizer of the distance metric
between the true distribution and the
model distribution
Thats ML for you
Okay So what well be doing in this
course right now is we will ask
questions like you know what model what
choice of P theta should we take Okay
What is the choice of distance metric
that we should be looking at And how do
we solve this optimization problem Its
non trivial because most most of the
distance metrics uh are non convex
So you cannot use any of the you know
well known optimization techniques to
solve this Youll be surprised to know
uh in todays time and age the go to
standard choice for P theta is a neural
network
Okay And the go to choice for this
optimization problem is first order
gradient descent
For all optimization that we have
studied in our in our previous courses
all the conjugate gradient methods and
second order methods and so on world to
ML is artificial general int general
intelligence is being achieved by using
a simple first order gradient descent

Yeah So thats all So well well see
that in the course later So well solve
this optimization problems using the
numerical gradient descent method of the
first order and the typical
amount of parameters that are there in
todays models like know like GPTs and
so on is of order of billions
We are now please appreciate the scale
we are solving an optimization problem
in a billion dimensional space
because number of parameters are
billion Of course well not start the
course with billion parameters well
start with five six parameters and so
on Now you know the current scale is
that of billion parameters So this
reminds me of uh an anecdote that
happened uh when I was in Delhi um right
in front of IT Delhi uh theres this
institution called Indian statistical
institute ISI okay a lot of economists
and statisticians and so on So I was I
was having a conversation with with an
economist once and you know they were
saying um yeah I mean our our models Im
Im Im trying a larger model for a
problem that he wanted that he wanted to
solve Hes saying Im trying a very
large model and see a larger model is
not a good model right because you dont
need too many parameters in your model
you need lesser number of parameters He
was telling me that oh Im Im using a
larger model now and I want to reduce
the number of parameters and so on
Curiously I asked him how many
parameters does your model has He says
oh it has it has gone to eight now I
have eight parameters in my model said
what eight so we are talking about 8
billion parameters right so
so thats the scale so initially all the
linear models etc they were talking
about you know 10 model 10 parameters 15
parameters if your data is in 100
dimensions then you have the linear
model will have 100 parameters 100 plus
100 100 for slope and 100 for intercept
200 parameter model
todays models have billion parameters
but whats The most interesting you know
and satisfying thing is that no matter
how uh the models have changed and the
and the landscape has changed in terms
of scale the underlying mathematical
problem that is being solved remains the
same and this is the problem that is
being solved The problem that we are
after is that see this px that we are
tackling right now is the amalgamation
of all human knowledge that has been
seen in history thats agi So imagine
that the random experiment that we are
considering and the sample space that we
are considering is the entire universe
and all documents all text all images
all kinds of data that has been produced
in in in the entirety of human race is
what are sample spaces and we are
assuming that there exists an underlying
distribution and throwing our machinery
with a large lot of scale and too much
compute and data comes out AGI Why is
still an open question
So is this the only way to solve crack
human intelligence Perhaps not and most
likely not because a child does not
needs this much of data and this much of
compute to learn
We are also learning an underlying
distribution Even human learning can be
cast as this problem You know there is
every time we can we make a mistake we
get a feedback and then we you know we
go back and so on Right Maybe we are
estimating distributions but we dont
look at the amount of data that todays
models look at Right and and the power
consumption that our brain has
is is orders of magnitude lesser than
what todays uh models take So maybe
there is a parallel model for
intelligence Yeah thats for some
other days discussion But this is the
recipe Okay And well be looking at
several ways of solving this problem
Choose different models choose
different distance matrices choose
different optimization algorithms And
that makes you know if you choose Ill
tell you right if you make this P theta
to be a linear model and you make this
to be the KBA labor divergence and you
solve this optimization problem in a
deterministic way then it becomes a
linear regression if you make it
compositions of sigmoids and uh if you
make this metric again Kbach labor
divergence and you solve this using
numerical gradient descent using an
repeated application of chain rule which
is called back propagation then this
becomes a deep neural network and so on
right if you use uh the dual methods of
optimization use under a kernel op
kernel method formulation then that
becomes a support vector machine and so
on well see all this you know dont
worry about these terms these are jarens
so basic idea is that you make a choice
for p theta you make a choice for
resistance metric you solve the
optimization problem and thats your ml
okay any questions on the formulation
yeah
 thats a question that we will answer
the question is I mean I told you right
we begging the question since we do not
know px how do we calculate uh the
distance metric that is what we will see
next statistics help you there your
probability theory will course the
probability theory course will help you
do that okay
 of this distance
 r
plus r plus includes zero
Lets say
 yeah the question is uh we jump from
solving or estimating distribution
functions to density functions does it
change anything does it change the scale
etc or anything no it does not because
the density function and distribution
function in the cases where they are
both defined have a one to1 relationship
right so we estimate we work with
density functions thats it Thats for
mathematical convenience See for
instance gshian density is easy to
compute and so on or goshian
distribution is a little difficult
Thats where you need q functions and so
on Remember those tables and all that
density functions are easy to work with
Thats the only reason we work with
density functions Okay
Okay See the theres before we move on
with this uh there is one detour that I
want to take Okay and
see

okay uh not written that thankfully the
detour that I want to take is that in
the first class I told you that there is
a deterministic way or nonrobabilistic
way of looking at machine learning
correct
right where you have see even there the
the starting point is the same you have
x and you have y and you want to learn a
mapping now I cannot not talk about
unsupervised learning in that framework
Now you see why it is so difficult to
stick to nonproistic ways Okay But
anyway so lets say that you have X and
Y and you want to learn a function and
you make an assumption on that function
and still solve an optimization problem
right Thats what you do there as well
Now does that assuming that this X and Y
are vectors from some uh some space
which is RD and RK and all you need to
learn is a function between those two
assuming that there exists some
function
Now we have this world view that those x
and ys are actually the range spaces of
two random variables Right Suppose we
give up that world view and say that
okay these are two sets and we want to
learn a function between these two and
there is some framework which is called
risk minimization framework or function
learning framework Something comes up
The question is that something which
comes up how does it connect to whatever
we have seen It turns out that they are
exactly the same thing
So I want to show you that Okay The
framework of empirical risk minimization
or risk minimization which is what is
taught in an ML 101 class I want to
show that empirical risk minimization is
exactly the same of distribution
estimation
and uh and and and and getting you know
getting the parameters of the
distribution in a uh in a in a in this
uh framework that we just saw I want to
show equivalence between those two
because as when we move on right when
you read a textbook for instance some
textbooks choose to stick to uh the
non probabilistic way of looking at
things or for instance there is this
textbook by um Christopher Bishop right
pattern recognition neural networks mo
the treatment is mostly
non probabilistic but there is this
there is this book by Kevin Murphy the
title of the text itself is
probabilistic machine learning
okay uh so there uh Both treatments are
seen in the in the literature I want to
sort of first fix the equivalence
between those two so that when we move
on you know that we are doing the same
thing
Okay So well do that in the next
class Uh so when we come to the next
class yeah thanks for attending this
class So this uh ends this particular
class So just just recalling right we
formally today defined what the problem
of machine learning is So the form the
the problem of machine learning is that
that we are given a few samples that are
drawn iid from an unknown underlying
distribution and we want to estimate
either the distribution or some of the
surrogates of it Thats the thats the
entire problem and uh the challenge with
the problem is u that you dont know the
underlying distribution So the way to
do it the the general recipe is that you
start by assuming that the underlying
distribution has a parametric form and
define and compute a distance distance
metric between the true uh distribution
and the model distribution or the
parametric functional form and solve an
optimization problem It always happens
that when I summarize the the class for
a day it looks like why did I spend 90
minutes on this topic
Always happens that way But anyway so
thats thats thats for today and when
we come to the next class as I said I
will start from the risk minimization
framework and Ill show you how risk
minimization framework is exactly the
same as this and then we start by
looking at the linear family of models
Okay thank you for attending this
