---
id: jXCqrFVGwoU
title: Lec 15 Risk Minimization Framework
url: https://www.youtube.com/watch?v=jXCqrFVGwoU
date: '2026-01-28'
duration: 40:13
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

speaker_1: Welcome everyone Last time we saw the
recipe that is used to solve any machine
learning problem and we cast the problem
as that of uh
distribution estimation and depending
upon what distribution we estimate we uh
we give different nomomenclatures to
those problems and I also gave you a
recipe where you are given
samples from the distribution
assume a parametric model to the
underlying unknown distribution compute
a distributional divergence metric
estimate it using samples and optimize
it over the parameter space
Okay And I we also saw an example at
the end of the class for one particular
problem of supervised regression where
uh X
is in RD and Y the label uh is in the
space of real numbers and data are
samples of this sort We have X I Yi we
have n samples that are drawn iid from
an unknown underlying distribution pxy
See in fact when I say that there is an
unknown underlying distribution its
technically wrong because there are n
distributions that are identically
distributed or theres one distribution
I mean you know the uh the analogy now
the problem was to estimate the
posterior of y given x the labels given
uh the so called input random variable x
and uh we walk through the recipe that
we had seen so we assume p theta which
is the model distribution which we want
to estim estimate This is one example
that I showed you where we assume that
to be a Gaussian distribution The
distribution is over y and we represent
the mean of that distribution using a
canon canonical function h theta of x
where h theta is a function from x to r
In general it is from X to Y And uh we
cached the problem of minimizing the K
divergence or maximizing the likelihood
and saw that it boils down to finding uh
the parameters theta by solving this uh
well known problem of minimizing the le
square error Okay thats what we saw
This was an example In todays uh
lecture
what Ill do is
I will walk you through an alternative
route meaning we will start by casting
the machine learning problem as
the one of minimizing what is known as
the risk function Okay And then we
will see that minimizing or optimizing
the risk risk function is not tractable
in practice So we resort to minimizing
the surrogate loss function or surrogate
function which is called the empirical
risk Okay And I will show you that
minimizing empirical risk
is equivalent to estimating the
distribution
So whatever we have uh formulated so far
I will show you that there is an
alternative formulation to this problem
and uh I mean one can uh look at the
problem from both ways uh in literature
some people choose to look at the
problem as distributional estimation and
some people choose to look at it as
empirical risk minimization but both of
them are solving the exact same problem
uh when when when they are solved in
algorithm algorithmic way so that is the
uh content for this in todays class
from the next class onwards I will not
make this distinction that you know we
are doing erm or we are doing maximum
likelihood estimation you should be in a
position to understand that Both of
these are exactly the same Okay At
times some algorithms are formulated as
ERM Some other times algorithms are
formulated as distribution estimation
Okay And you have to uh appreciate that
both of them are exactly the same
problem Okay Done in different two
different ways Okay So let us
look at uh the risk minimization
framework
I will do this for supervised learning
uh where we assume that we have uh a
data space and a label space y and this
can be extended to the other cases as
well as we will see in a while So the
problem setting is as follows We are
given
the same data
which is uh set of tpples of this sort
We have
x i comma y yi

1 through n and uh this is drawn i from
an unknown underlying distribution pxy

This is the starting point and in
general X is in RD
and Y is in R K or it can also be a
discrete set
So depending upon what set you are
operating on the problems are called the
regression or classification problems
and you know that so we are looking at
supervised learning because there is a
label set onto it but this framework is
generalizable to the so called
unsupervised learning as well as well
see Okay Um the goal is the
following Goal
is to
estimate
a hypothesis function
So this h which is a function h that
operates on x and maps to y
Okay uh there exists a function called
hypothesis function that takes elements
of x and maps it to y thats what we
define uh hypothesis function as uh as
that sort now
goal is to estimate a hypothesis
function So this h okay belongs to a
class of
hypothesis set So there can exist
infinite functions right So this is
set of all functions
from
x to y
So given that there are infinite ways to
map two sets right of x to y So we need
one particular hypothesis that we choose
from So how do we choose which is a
good hypothesis is the question So what
do we have All that we have is the
training data D or the data set D Now
how do we define So well have to come
up with some goodness measure Okay Uh
that would tell me whether a given H is
good or bad Okay To do that so let me
write that So quantify
quantify the goodness
of an h So given a hypothesis function
Okay So this function this is a
function of x right as you can see its
a function of x So we have to quantify
the goodness of this particular
hypothesis which is nothing but a
function from x to y So how do we do
that Now define
a notion of loss function
loss function L Now this loss function
is a function that operates on the
crossroduct of Y and Y and itll give
you a positive real number This is the
definition of a loss function So what
do I mean by that So this loss function
can take
the values from the spaces of y
the cross productduct of y with itself
and then give you a positive real
number
Okay So any function that operates on
the cross productduct of y and y and
gives you a positive real number is a
loss function
Okay Now an example can be this right
It takes h of x and y as input and it
will give you r plus at the output Uh h
of x is also in the space of y Why
Because the the range or co doain of
this h of x is y So its a valid
function So lets take an example of
this loss function Example of this loss
function can be
so it takes h of x and y and this can be
equal to uh assuming that both of them
are vectors
simply be the two norm of the difference
between these two Okay this is called
the
squared error loss
And another example can be
zero if uh these two match
and one if they dont
Right This has a name Does anyone know
this is called the
the 01 loss
Okay this is a design parameter One
can choose what loss function one would
want to operate with Okay Ive just
given you two examples There can be
many more We will see more examples of
this loss function in this course Is
this clear So its simply a function
that operates on the cross productduct
of y and y and gives you a positive real
number or non negative real number It
can also have zero of course right And
these are a couple of examples
Okay Now uh remember what our goal
was Our goal was to uh estimate or come
up with a hypothesis function that
operates on X and Y and we wanted to do
it by using the underlying data set and
come up with a good hypothesis So we
wanted to quantify goodness What is a
good hypothesis To do that we defined
the notion of a loss function But note
that a loss function operates on a
single pair of data
So it takes one hx one y and gives you a
number
But we cannot define objectives only by
having looking at one particular sample
Right We have n capital n number of
samples and we need to aggregate the
loss on all those samples And how do we
do this We take an expectation Okay
So let us define extending the loss
function on the entire data set
for the population
So define
what is called as a risk function which
is the expected value of the loss
function


where the expectation is taken over
the joint distribution of X and
Okay this is called the risk function
Okay Now we can define the problem of
the the primary problem of machine
learning which is
estimate
goal problem
Estimate H star of X
which is given as
the function that minimize this expected
loss or minimizes the risk
expected loss over the uh joint
distribution And this optimization is
for all h that
is in the hypothesis space So amongst
all possible functions that can map x to
y give me the one that minimizes the
expected loss and the expectation is
taken over the joint distribution of the
random variables that we have Does that
make sense See this uh formulation
is what is uh famously referred to as
the risk minimization framework
Okay What are you doing is trying to
find a hypothesis that would minimize
the risk function What is the risk
function It is the expected value of
the loss function Thats thats the
story Okay Okay So far so
good Um youll be surprised to know
that this problem is exactly the similar
same problem as that of estimating the
distribution Well show that in a
while Theyre mathematically
equivalent
Okay
Now the look at the problem right The
issue is uh can we solve this
optimization problem
Again not because we dont know the
underlying distribution So the exact
risk minimization problem cannot be
solved So what do you do You resort to
solving a surrogate or an alternative
where
risk
okay let me call it its actually called
the true risk in the literature
True risk function cannot be minimized
 since
the underlying distribution pxy is
unknown
 Okay Therefore
consider a surrogate
So define what is called as
the empirical risk R hat of H
which is defined as

the sample mean version
of the true risk
Okay this is what is called as the
empirical risk
Okay So finding out HCAP star
as the minimizer
of empirical risk
is the problem that we actually solve in
practice
So this problem is referred to as the
empirical risk minimization
or ERM
Okay So true risk
cannot be computed Of course you know
here we have to write that your XI and
YI are being sampled IID from PXY Of
course I mean you have that otherwise
uh statistics do not guarantee that
these are equivalent right So youll
have to do that So this is called
empirical risk minimization So from an
algorithmic standpoint what do you do
You compute the loss function on all the
data points Take an average and minim
find an edge that minimizes that
Okay this is empirical risk
minimization In fact the
machine learning 101 courses that you
find online actually starts from this
equation Define the loss function
compute the average and minimize

Correct So this is what empirical
minimization is So now the
central question that is in that that
occurs in machine learning is so we know
from statistics right So we know
that
rcap h the empirical risk converges to
true risk Correct
Why
 This is simply law of large numbers
The sample mean converges to true
expectation if you have large number of
samples and they are drawn ID This we
know but this is not important See what
is this saying This is saying that
I have to solve an optimization problem
over some objective function Correct
Now I cannot compute this objective
function Now what what what am I doing
Im considering a surrogate objective
function and theory is telling me that
this objective function converges to the
true objective function if I have
infinite samples
That means nothing to us Why What are
we actually interested in is we are
interested in the convergence of the
minimizer of the true risk to the
minimizer of the empirical risk
Im not guaranteeing anything on that
Im only saying that empirical risk
converges to true risk Fine Im not
saying that the minimizer of the empir
empirical risk converges to the
minimizer of the true risk So that is a
central question in machine learning
Right So you have to design an
algorithm However
h of x which is the minimizer of the
troll risk Okay May not
converge to
h cap of x which is the minimum measure
of true risk Okay So the central
question

when would
h
when would har hat x converge to
hx So this is the central question that
is asked in that should be asked while
you are designing any machine learning
algorithm Okay this is also called the
question of generalization
So we will see more on this as we move
on in the course So you might have
heard about these terms right
overfitting underfitting and so on This
is exactly where it comes from The
question that we are asking is whether
or not the minimizer of the empirical
risk convers to the minimizer of true
risk or not See mind you we dont have
access to h of x at all
Okay we dont even know what the true
risk is Then the question is how do you
even try to answer this question
How do you even know whether the
minimizer of true risk uh minimizer of
empirical risk is any close to minimizer
of true risk Okay well take up those
questions Theres a theres an entire
uh subbranch in machine learning called
statistical learning theory that deals
with only this question So basically
people come up with an algorithm What
is an algorithm By the way any machine
learning algorithm is a way to solve
this optimization problem
all machine learning algorithms is to I
mean what again if I have to give a
recipe to do erm what should we do so
well have to choose an h or a class of
families of h and then we have to choose
a loss function and solve this
optimization problem exactly the same as
choosing a model for p theta or pxy and
then choose define divergence metric and
then solve the optimization problem same
thing will happen
now thats an algorithm
Once uh in in the historically when
people come up with a particular
algorithm they would all always come up
with a bound on is does there exist an
upper bound okay on the empirical risk
in terms of true risk The question that
theyre asking is can I give you a
guarantee that if you run my algorithm
on a particular data set okay then it is
guaranteed that as long as your data is
coming from the true distribution can I
guarantee performance
see thats the question that Im asking
if you look at it what does this
question translate to the question that
Im asking is Ive seen one small sample
of the entire distribution and I have
built an algorithm on that
suppose I take a different sample from
the underlying distribution and use the
same hypothesis function to to predict
what would be the average risk that I
get when I do that Now if I would have
optimized or the closer I am to h of x
the minimizer of the true risk the
better my performance will be on unseen
data Do you agree
thats thats the goal See the goal is
how do you construct an algorithm okay
so that the minimizer of the empirical
risk is close to the minimizer of the
true risk What can you say about the
algorithm that you have constructed
Theres a theres a lot of theory on u
in fact you might have heard about this
particular machine learning al algorithm
called support vector machines SVMs It
was extremely popular uh in one point in
time because the true risk of an SVM
could be very well upper bounded
actually in terms of number of samples
in a data set and number of parameters
in the model
Okay thats why SVM was extremely
powerful But unfortunately
uh in todays scenario of uh extremely
huge models with billions of parameters
uh it is very hard to come up with these
kinds of generalization bounds These
these are called generalization bounds
But the question that that that is being
answered is how far is the minimizer of
the empirical risk to the minimizer of
true risk But if your sample set or the
data set itself has all possible samples
that you can look at from the
distribution then there is no point in
general Theres no point in asking the
question of generalization Perhaps
thats what is happening because I keep
saying this right If you solve erm on
the entire universe
then you dont even have to ask this
question because you have all samples
that you can see right thats thats the
point So todays models for instance
these GPTs etc
they actually solve this problem
algorithmically what is solved is erm
okay but the question of convergence is
not asked because we still do not have
enough mathematical
tools to bound the generalization error
for models that are that have so many
number of parameters and and and
compositional in nature So theres
theres no theory yet that is developed
but again empirical risk minimization is
working today I mean working empirically
because the number of samples that we
are uh training our models on is is too
huge
question Yeah
 models
have
no way to
What is the true minimization
Then how do you like where do you stop
at training
 Good question The question is uh when
you are solving this optimization
problem how do you stop How do you
decide where to stop when to stop Hold
on to that question In a few classes
we will look at this thing called uh
know the bias variance decomposition and
so on So when uh I give you uh insights
on when to stop training and how do you
do erm and so on Okay So basically
what is done is you know you uh divide
your data set into two sub parts right
training and testing Okay so you train
it on train data set and locate test it
on a subset of your data and if it does
good on this test set then you stop your
training there very broadly but we will
formalize all these notions as we move
on Okay
Okay Its there Okay Now
lets look at an lets look at an
example of how to do empirical risk
minimization Okay And then we will
move on
Example of erm

for
regression problem

 So given
data
we have the exact same setting as before
we are given data So we have uh X
thats in RD and we have Y
thats in R Lets take uh
univariate regression Now now
suppose
uh h theta of x
comes from
a family of uh
parametric functions

 parametric functions parameterized by
theta
Okay
Now examples can be that your h theta
of x uh can be lets say theta transpose
x or it can be
some e power theta transpose x and so
on I mean you choose a function So
what sort of function should we have to
choose is a is a design choice This is
actually called a model We will see
that in a while Now define a loss
function or rather choose a loss
function Lets choose
lets say a mean squared error
Then compute the empirical risk
Empirical risk is 1 by n
is from 1 to n We have uh h theta of x
 minus x i minus yi
These are scalers right So I can do
this
right And find theta star as the
minimizer of
this empirical risk and you minimize
over the parameters theta
So if you note uh this is exactly the
problem that we were solving So this is
equivalent to
estimating
the conditional distribution So let me
write that
the above
is equivalent to
estimating
PH heat of Y given X

using the maximum likelihood or ML
estimation
with
an assumption that P theta of Y given X
is Gaussian
with mean H theta of X and variance I
this is the equivalence
meaning
if you solve empirical risk minimization
okay then
you are estimating
some distribution So in this case it
happens to be the conditional
distribution with a distributional
assumption on that particular
distribution and the parameters of that
distribution
so will be the same as your hypothesis
function
So thats the equivalent So whenever
you solve see sometimes what happens is
we dont why do we need these two
alternative uh explanations is for for
the following reason
sometimes what we do is we dont
explicitly define the distribution the
underlying distribution and do a maximum
likelihood estimation rather
define the loss function okay and solve
erm
but we should always remember that there
exists some distribution okay that
corresponds to solving this particular
problem
So we may not know what that
distribution is and we may not even know
what the underlying form for that
distribution is and we may we may not
even care what is what it is you know
for instance if you are building lets
say a GPT then this h theta is a
particular type of function called
transformer
okay and the loss function that is
typically used is uh the cross entropy
Ill define it in a while okay Ill show
the equivalence of uh uh what
distribution are we assuming when we do
the cross entropy But its the loss
function is called cross entropy loss
function and you solve VRM okay
we dont look into that as maximum
likelihood estimation right but you know
we should know that this is what we are
doing so sometimes what happens is in
cases such as lets say gausian mixture
model we dont look into that as erm
what we do is we explicitly define the
underlying distribution and cast it as
maximum likelihood estimation or
minimizing k divergence problem and same
thing would happen lets say for uh lot
of generative models One example is
that of diffusion models Now you have
might have seen some of these
commercially available image generators
right Where you can uh type out a
textual prompt and it generates images
corresponding to that right They are
all samplers They are all generative
models again as I said in my next
course So when you when you build a
generative model you are solving the
problem of minimizing K divergence
explicitly by assuming a canolical form
for P theta of X because you want to you
want to model the marginal of X and
sample from it
there you dont cast it as ERM okay you
cast the problem as that of the
minimizing K divergence by assuming some
canonical form on the distri underlying
distribution but theyre exactly the
same Got it So any ML algorithm
can be seen in two different angles
One define a function from two random
variables that you are considering Call
that hypothesis define a loss function
compute the empirical loss loss and
solve an optimization problem on the
hypothesis space and call that your
model and ship it Thats one way to
look at it The other way to look at it
look at it is define a distributional
functional form on uh the underlying
distribution that you are trying to
estimate Minimize the K divergence on
the parameter space of the model
distribution and ship the distribution
itself When do you want to ship the
distribution itself
 Mostly in the case of generative models
or even in the discriminative models we
will see right that uh finally in some
cases the optimal function that you need
to estimate h will be a distribution
because if the problems are equivalent
then at least for some cases the
solutions or rather all cases right
analytically you should be able to show
that the solutions are equivalent We
will see that in a while Ill take an
example and show you that had you uh
solved the problem of true risk
minimization Okay Then what will be
your true risk minimizer is So it turns
out that the minimizer of true risk is
the conditional distribution for certain
cases So estimating conditional
distribution directly from data is
equivalent to minimizing the true risk
So that is what we are going to see now
Okay So these two uh parallelizations
has to be you know embedded in your head
because you know some people use this
some people use that some models use
this formulation some models use that
formulation but theyre exactly the same
is that okay
 so now yeah
 you mentioned the hypothesis function is
transpose or its linear or nonlinear
 can be anything can be anything yeah so
we will see examples of that uh later in
the course so this is called if if if
you use your theta of x2 be of this form
its called linear regression if you use
this corn its called logistic
regression different uh choices for the
hypothesis class thats it okay
so now what what we will see that I just
will prove the statement that I just
made that there is an equivalence in the
solution space as well right now the
equivalence was shown in the
optimization space the problem that you
are solving or equivalent is what was
shown now we will take a case and show
that even the solutions that we find out
from two different angles happen to be
the same if you choose the parameters
that way Okay So establishing
equivalence between
risk minimization
and

divergence minimization
Divergence minimization are also called
the maximum likelihood estimation
minimizing the negative log likelihood
some people call it NLL as well Ive
told you that right so let us look at
this now question
what function
minimizes the true risk

Suppose we had access to distributions
right All distributions The question
that Im asking is what
function minimizes the two
Now uh you can as you can imagine right
depending upon the problem that we are
solving
if we are solving uh the uh
classification problem or regression
problem supervised unsupervised this
function changes obviously it should
change for generative models for
instance uh the minimizer of uh the true
risk if you define a loss function that
way should be the marginal distribution
isnt it because we are finally
estimating the marginal distribution in
the case of generative models here it
should be something else so depending
upon what problem are you trying to
solve this has a different answer but we
will see this for one particular case
which is the case of supervised
learning Okay The question is what
function minimizes the true risk So
consider
the case where you have data
that is uh
pair of uh labels and features
Okay And we are defining the loss
function
as 01 loss function
So I will do it for this particular
case Okay And uh
equivalent results exist for other
choices of loss function and other
choices of models as well Ill you can
take that as homework or yeah its for
further discussion So the loss function
that we are looking at is the zero one
loss function which is that
if the hypothesis matches with the the
actual label then I uh assign uh zero
loss if it does not match I assign one
loss and Ill also say that uh lets say
that okay let me write it make it more
specific Take
suppose uh our x i is in rd
and yi
is binary
This is to simply make my life simpler
so that the algebra works out to be
simple So all these results can be
extended to the regression case or
K class classification case Okay So
thats your homework Ill just formally
tell you what your homework is But
yeah so lets consider that we are
solving a binary classification problem
where it is diseased or non dis You can
always go back to that X ray example
that Ive been citing Right So disease
versus non d disease This is the and
Im operating under 01 loss 01 loss
function Is that okay Okay Now with
this the risk function the true risk
that Im talking about is the expected
value expectation of
the loss function right and the
expectation is taken over the joint
distribution of x and y this is what it
is okay
now the question is I would want to get
the minimizer for this what is the h
function that would minimize this
 so now if you observe it
this entire risk is a function of h
thats why Ive written it as a function
of h you change the hypothesis the risk
changes isnt it h so I can find out the
minimizer for this particular risk as a
function of uh sorry I mean on the space
of h so what hypothesis minimizes this
at least under these conditions where y
is binary and loss is 01 lets look at
that uh we will stop here and continue
in the next lecture
