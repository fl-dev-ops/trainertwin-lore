---
id: ejma0iH1pXE
title: Lec 22 Expectation Maximization Algorithm
url: https://www.youtube.com/watch?v=ejma0iH1pXE
date: '2026-02-03'
duration: 25:33
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Lec 22 Expectation Maximization Algorithm

## Transcript

speaker_1: Welcome back to the lecture Now lets
look at this question
So what choice of
Q
would make
the elbow
tight
What do you mean by making the elbow
tight The lower bone that we have
becomes equal to the likelihood
function
Right What value of QZ would do that
Any guesses
What should be the density function that
this Q should assume for this for this
particular expectation
be equal to this particular log of that
expectation Lets look at that Its
only algebra Lets do that algebra and
see what value what choice of this qz
okay uh should make this tight
Okay So why are we even asking this
question Now suppose you want to
optimize uh uh get the model parameters
theta by solving this problem You know
that f theta of q okay also depends on
choice of q Now you choose a q you get
a lower bound on the likelihood
function Now suppose you want to
maximize a function and youre
constructing a lower bound and
optimizing that instead What do you
want your lower bound to be You want
your lower bound to be as close to the
actual function as possible Now the
question that youre asking is what
should be the choice of Q that I would
have such that the lower bound that Im
constructing because I cannot optimize
the original function is as close to the
original function as possible Thats
the question that were asking Now in
the most general case
in the most general case this
optimization problem can actually be
slated as two optimization problems
Okay 1 by Q and 1 by theta
Okay
what are we doing here We first
optimize or we first construct the lower
bound
Okay and try to make it as tight as
possible by finding a function Q Once
we construct the lower bound we find
the parameters that would maximize the
lower bound
You understand Now look at this Well
not do it in this course Well do it in
the next course But Ill just tell you
for the sake of completeness Look at
this If you were to optimize this with
respect to Q
okay you are optimizing with respect to
a function
See optimization with respect to theta
is an optimization over variables
optimization over Q is an optimization
over functional space
Do we know how to differentiate or
optimize over function space We dont
unless you have studied variational
calculus and thats why these methods
are also called variational inference
methods
Thats why the name variational
autoenccoder right again Ill start the
next course from VAE Right Ill Ill
tell you why EM is broken and youll
have to move away from VA the thing and
all that But yeah so if you want to
optimize over Q then youll have to
optimize over function spaces
But here thankfully no uh we will see we
will not optimize over Q but we will ask
this question and well try to find out
what Q would
make my bound tight and not explicitly
get solve an optimization problem over Q
as we will see now Is this clear Okay
So now lets try to answer this
question What choice of QZ would make
the elbow tight in the sense that I if I
if I have to solve this optimization
problem then what is the value of what
what should be the the functional form
of Q such that this is maximized f theta
is maximized What is the maximum value
of f theta of Q
 It is l theta The maximum value of f
theta of q is l theta So what value of
what what not I should not be saying
value What functional form of Q would
make f theta oft equal to L theta is
what we will ask Question
 why are we why do we want the elbow It
still doesnt make sense because if if
we have if it is not tight then we have
space between the the l theta and the
maximum of this Isnt that space good
because that makes the likelihood even
more tighting it to the lower bound is
no no we see we are not pushing down the
likelihood were pushing the lower bound
up to the likelihood What happens is if
you maximize the likelihood I mean I
will write the diagram later when when I
complete DM but if youre maximizing
this lower bound at every point right
this gap uh your parameter may not cover
this gap this is a bad thing so youre
not you dont have any control over
likelihood that is there all you have
control over is your lower bound so
pushing the lower bound as close to the
likelihood function as possible is a
good thing you dont want that gap
precisely
right I want the parameters that would
lower this gap
Okay Ill write the diagram in a while
Okay itll be much clearer Okay so
lets look at this What choice of QZ
would make the elbow tight So let us
look at um lets consider
consider the difference between I just
mentioned that the maximum value of the
elbow uh is L theta So lets look at
whats that gap that he mentioned So
consider this l theta
minus f s theta of q
So whats this gap
This gap is log
p theta of x minus
that expectation which is

 qz
whats the term log
p theta of x and H
log
P theta XZ divided by QZ
right this is what it is this is equal
to
Ill skip the algebra Log P theta of X
minus maybe Ill write it So this is at
least one step QZ log Ill write the
joint distribution as
the product of
marginal and conditional Okay Divided
by QZ
All right So I can take the marginal
overx outside correct
because it is independent of Z
Is this all right
What did I do So I just took
this log P theta outside the summation
because its independent of Z right the
marginal of X is independent of Z I just
took it out and these two terms will get
cancelceled off and what I have is this
particular term which is
qz
log
qz divided by P theta of Z given
Right What is this term
Do you recognize this This is the K
divergence between Q and
P theta of Z given X
So what was our LHS
The LHS is uh the difference between the
likelihood and the lower bound Correct
Now we already saw that because its a
lower bound
the maximum value of this uh lower bound
is equal to the likelihood function
Okay
max
of f theta of q is equal to l theta by
definition
or by construction I would say not
definition actually definition but I can
say by construction
which can h
therefore therefore
l theta minus minus f theta of q this
can be zero okay only if
the k divergence between
qz and p theta of z given x is zero
which implies
the optimal choice of qz
that would make the elbow tight is
the posterior of the latent variable
table given data
Right So if you can make you can if you
can choose your
density over Z as the posterior See
please note that this density right the
posterior of Z given X is also a density
on Z
right we start we started by saying QZ
is any density on Z and P theta of Z
given X is a density on Z So if you
choose your density on the latent
variable the marginal on the latent
variable to be equal to the posterior of
Z given X then
the lower bound that we constructed on
the evidence or the log likelihood will
be exactly equal to the log likelihood
Okay why is this result important
Lets go back to what we wanted We
wanted to maximize the likelihood
function We could not maximize the
likelihood function Therefore we
constructed a lower bound on it and that
lower bound dependent was that lower
bound depended on another function
another density on Q and we wanted to
first make the lower bound tight and
then optimize over the parameters
Now we just found out that the best
value that we can choose or just best
function that we can choose on Q is
the posterior of Z given X
Now suppose in a model okay you can
estimate P theta of Z given X then you
dont have to solve this optimization
problem over Q you can just compute P
theta of Z given X and solve an
optimization problem over theta thats
it
okay and for those latent variable
models in for in which case P theta of Z
given X is not tractable youll have to
first solve an optimization problem over
Q using variational methods and then
construct an lower bound and then
optimize over the parameters
So in models such as lets say diffusion
models and VAEEs
the letter approach is uh uh is taken
where estimating P theta of Z given X is
not possible
but in the cases of mixture densities
such as gajian mixture densities we will
see that we can estimate P theta of Z
given X and since we can estimate P
theta oft given X we dont solve this
optimization problem over Q but we will
compute Q to be P theta of GX and
optimize over theta Thats it
Does it make sense So what are we
doing We have an objective function
that we would want to optimize with
respect to parameters theta We cant do
that So we constructed a lower bound on
it And the lower bound is constructed
in such a way that for that particular
value of theta the lower bound is
tight And then we optimize over theta
Now note this Suppose I change my
theta
the lower bound also changes
Okay remember this because what we
actually end up doing is we will
iteratively optimize over theta and Q in
the sense that we start with a theta
Okay and find my Q to be P theta of Z
given X
with that as my Q I will optimize for
theta Now my theta changed because my
theta changed Ill have to get the
construct the new lower bound and with
that new lower bound I push my theta
further and I keep doing this
iteratively and this is the EM algorithm
lets write why is it correct is that
the question will
 well see that well see that okay So

an iterative algorithm

initialize with some theta kn Okay
Compute
P theta
T
or rather
compute Q Z
Q QT of Z to be P theta T
Z g Z G Z G Z G Z G Z G Z G Z G Z G Z G
Z given X I have to write a for loop
here No for hold on

for
for t equals 12 convergence
Do
compute QT to be equal to P thetaT of Z
given X right
Yeah
So there is this uh counting from zero
versus counting from one issue that I
always get into
because Im trained as an electrical
engineer right So we count from one
for t equal to 1 to convergence to
compute this Okay So once you compute
this estimate
the lower bound estimate f
thetat t of qt
to be equal to
expectation of this is over qt of z
uh log of
p theta t
So this can be computed Why Because we
already know what P theta of Z given X
We know what QT of Z is Are you all
following what Im saying
 Yes
 Right Since we know what QT of Z is we
can compute this And since we know
this this entire expectation can be
computed So once you do this what do
you do
Estimate
theta t plus 1
to be
the maximum of
theta
So this should be theta not
yeah its a function of theta So we
have qt that we fix
See somebody asked a question right Why
dont you make this uh a function of
theta Its actually a function of theta
because you see this this is qt is is p
thet and because it is q it is computed
at theta t This qz becomes a function
of t as well But it just makes the
notations a little complicated Thats
why I dont put theta there Theta t
again there Okay Right Right So now
find theta t plus 1 as the one that
maximizes
this elbow
computed at that QT
Okay
And then replace

Thats it I dont have to do it This
is this is all So youre iterating over
it You understood So start with an
assumption on theta Okay And then
compute the the Q to be P theta T at
that particular theta Z given X Compute
the lower bound and maximize the lower
bound with respect to theta And keep
repeating this
 Come again
 Here you mean No it is P theta So you
you compute this as a function of theta
So what you fix is Q because this entire
thing has to become a function of theta
Right So this Ill write it as F theta
at QT
So you have to constru
theta theta t
theta at the index
 This is theta t only See thats why see
when when I say QT QT already has theta
t in it
QT already has theta t in it The
posterior that you compute is with
respect to theta t
 Right So this entire thing now will be
using
uh theta t theta t but will be a
function of theta
Right
This okay so this is exactly what the
expectation maximization algorithm is
Okay This step is called the
the expectation step
And this is the maximization step
So now uh before you ask questions so
just stare at the algorithm first
understand the algorithm
 I wrote theta 1 No
I said that electrical engineering
problem So I started with theta 0 then
Ill initialize theta 1 I I realized
that quickly Okay So please look at
the algorithm and try to understand what
it is Two things have to be done Now
uh well have to Ill have to show you
why this algorithm is correct What we
are doing is constructing a lower bone
maximizing it Sorry making it tight and
maximizing it with respect to theta and
doing it iteratively Why should this
algorithm work Ill show this in the
next class Okay The other thing that
is to be done is Ill have to apply this
algorithm to GMM
Okay And show that how the algebra
works out for the case of GMM Well do
both that in the next class However
please note this There are two
important observations to be made here
One
EM algorithm or rather variational
inference This is also called
variational estimation methods
they will take this particular form only
if we can compute P theta of Z given X
for only those models okay for which we
can compute P theta of Z given X Z given
X we can apply an iterative algorithm
such as EM
this is very important because in this
course we will only look at GMM which
are the case of latent variable models
for which P theta of Z given X is
tractable can be computed and for the
cases where P theta of Z given X is not
computable then you need to estimate Q
also within this see why am I saying
this is for the sake of completeness
because initially when I introduced
latent variable models one of the
questions was we dont even know what Z
is
how do we deal with it we deal with it
by estimating a distribution over Z okay
using variational methods along with the
model parameter estimation
which is which boils down to estimating
Q that is why you know in the most
general form H
you estimate uh you write uh elbow
optimization as an optimization over
both the model parameters theta and
by the way this Q is called variational
distribution
This Q of Z is called the variational
distribution over latent variables So
you optimize over the model parameters
and also the variational distribution
But in the cases okay where
the variational distribution is
tractable you know we know that the
optimal variational distribution is
always the posterior of latent given
data always because thats algebra
however for some models like vaes
this uh posterior of uh the variation
distribution over I mean conditioned on
data cannot be computed and that is when
we resort to estimating that explicitly
as well but for this particular course
and the particular case of uh a mixture
density the posterior of the latent
variable given data can be estimated
and thats why we resort to this
iterative algorithm where we start we
initialize some values for the
parameters remember in the case of GMM
what these parameters are alphas and mu
and sigas we initialize them to some
value and we compute the the posterior
of the latent given data and then we
compute the lower bound and We optimize
the lower bound with respect to theta
and we iterate Thats it And once we
get the new theta that becomes we
compute you again compute the posterior
of the latent given data compute the new
lower bound and keep iterating over it
Ill have to still answer two questions
right why this algorithm is correct So
what we will show in the next class is
that I may just make the statement and
then well stop We will show that
em
guarantees
that the likelihood that you estimate
likelihood that that you get at theta t
 plus 1 is at least equal to the likelihood
that you get at theta t
Please see this It is not saying that
it is strictly greater
This algorithm will ensure that the
likelihood will never decrease
Somebody was asking now GMM is a
universal approximator
Right EM algorithm is there ML should
end here It does not end because this
is not a strict upper bound
This well show next class well start
by showing this that you know if you run
the EM algorithm EM algorithm will
ensure that the likelihood never
decreases and also Ill work uh at
least Ill show a sketch of uh the
algebra for the case of GMM and then
well continue with the base classifier
estimation Please again remember the
story The story is that we want to
estimate the posterior of y given x in
the case of uh supervised modeling and
to estimate that we want to estimate the
class conditional densities and class
conditional densities may be GMM
that is the story line so far You give
example where p theta given x
 give me give an example where p thet oft
z given x cannot be computed is it uh
neural network variational autoenccoders
if you make your p theta of x given z
not a gshian but a neural network then
pt of z given x cannot be computed ask
me this question next class when I
define p theta of x given z for the case
of gmm Ill show you the case where it
cannot be computed
 come again
 whats the stopping condition
 uh good question what is the stopping
criteria for this uh I Ill tell you
next class Okay So thanks for
attending this this class and next class
well continue from uh the correctness
of EM and then look at EM for GM Thank
you
