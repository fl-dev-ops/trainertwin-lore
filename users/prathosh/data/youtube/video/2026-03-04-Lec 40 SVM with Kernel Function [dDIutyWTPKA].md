---
id: dDIutyWTPKA
title: Lec 40 SVM with Kernel Function
url: https://www.youtube.com/watch?v=dDIutyWTPKA
date: '2026-03-04'
duration: 29:52
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Lec 40 SVM with Kernel Function

## Transcript

speaker_1: Welcome to this class So now let lets
finally there is one final case that we
have to look at SVM
with
the kernel function
Now so far we are assuming that the
discriminant function is linear Why
should that be the case for for most of
the data that we get the discriminant
function is not linear Uh what do we do
with that is the is the question Now
the the idea is very similar to what we
did with the generalized linear
regression
What did we do You can convert a
nonlinear decision boundary into a
linear decision boundary by transforming
data into a into some other space
Thats exactly what we do here Okay So
let us look at it
Uh
so define
a function
function fee
that is from RD to
R Dash So typically
ddash is much greater than d
Now what is not linearly separable in
the the data domain X okay
will sometimes become linearly separable
in the transform domain
example can be
you take the 4 year series itself 4 year
series right its its linear in the
exponential domain its not linear in x
or or or whatever the t whatever your
variable is but its linear in the
exponential domain so Were not
guaranteeing that the data will become
linearly separable after you transform
but we have a formulation to handle uh
the case where the data is not linearly
separable as well We just need this
slack formulation However transforming
data and projecting it onto a higher
dimensional space okay uh will make
delinear separability more plausible
Okay thats why you choose a fee Okay
such that uh uh the data is uh taken
from a domain D to D I mean RD to RD
dash where Ddash is much higher than D
Okay
Now
with this
the
dual function
to be solved
will be
So well have half
uh what was that Its yeah mui
So maximize is over mu
uh mui minus half
sum over i some j mui muj
yi yj Now we will not have x i
transpose xj Well have f of x i
transpose
f of xj
Correct
So this will be the problem that well
be solving Does it make sense
Okay
so far so good So now we still have to
answer this question right How do we
choose this fee in practice Remember I
told you that this fee is a is a
userdefined choice You know you choose
it We well get to that in a while But
what is to be noted is that the problem
that well be solving will now have fi
transpose f of x i transpose v of x i
instead of x i transpose xj because we
have transformed the data into some
other space
Now suppose of course I mean there is
this constraint that uh
that mu has to be between zero and c
because we are solving the slacked
version of this problem
Suppose there exists a function
there is a function
function K
Okay This function K
uh takes
operates on
uh the cross product of RD and RD
and maps it to
real numbers in fact positive real
numbers such that
compute that kernel on
two data point it will give you
this
for all I and J
What does this mean Lets say that
there exists a function K Okay And
this k is what is called as the kernel
kernel function
So what this will do is itll take given
two data points x and index j If you
pass this uh if you pass these two data
points to the kernel function itll
compute the inner product okay of the of
these two data points in the projected
space
Suppose a function like this exists
Okay So what happens to the problem
that well be solving in this case Now
instead of
the SVM problem SVM dual problem
will be now
well have UI minus half
mui muj yi yj
x i xj
Right
here there were inner products between
uh the projected data points Now if
this is equal to a function uh kernel
then itll be equal to this Now what
does this mean Is it is it okay Is it
clear to all of you what we are saying
This means that
if we can find a kernel for a given
projection then we dont even have to
know what the projection is
As long as we can compute the kernel
projection
 Good question The question is if we do
not know what the projection is how do
we know that it is linearly separable
Theres no guarantee to that However I
will show you that uh
there are cases where this fee can be a
projection to an infinite dimensional
space while the kernel can be computable
in the data space
So you project your data onto an
infinite dimensional space Okay there
you assume it to be linearly separable
and you dont you dont actually project
the data you only compute the kernel
We well see that But what is to be uh
noted right now is that if there exists
a function like this which will operate
in the data domain okay and computes the
inner product which is called the kernel
then to solve the SVM problem maxin
classifier problem you dont even have
to know what the projection is as for as
long as the kernel can be computed
thats okay no that that is fine okay
Hold on Huh
Yeah Question Yeah
 I was just thinking about it Has it to
be inner products are bounded between
minus one and one right
No Its
 cos theta right It can be between
minus1 and one
 Yeah So it I mean see I can be its
very safe to say R Yeah
However lets lets come back to this
in a while you know well have to talk
about something called mercs theorem
that says that
suppose
so k
bar
is an n byn matrix
with
uh the i J element
being equal to k of x i comma xj where k
is a kernel function
Okay Now if
kar is
positive semidefinite
for every data set D then
K
function K is a valid kernel
So what do you mean by a valid kernel A
valid kernel is one Okay
one that
corresponds to
a projection fee
So what what this theorem is saying as
follows
Suppose you you construct a kernel
function Okay And you take a data set
and compute the kernel for all pairs
You get a matrix
If that matrix is positive semi
semi definite then that kernel function
has to correspond to a projection
You understand This means that we dont
have to look at a transformation and
then ask what kernel gives the uh inner
product for this transformation We can
do the other way around
What we can do is come up with some
kernel function and see if the the
kernel matrix for that particular kernel
function on every data set is positive
semi different If that happens then we
can be guaranteed that
that this kernel function corresponds to
some projection of data
Thats how people do it in the sense
that they come up with novel kernel
functions not with normal novel
transformations
Because every kernel function as long as
it is a valid kernel okay it
corresponds to a transformation of data
Thats what Maser theorem says
Okay Yeah
You will not know what the projections
are for every kernel functions In fact
we will see an examples where the
projection for a particular kernel
function is to an infinite data space
Theres something called a gausian
kernel The projection for that
corresponds to an infinite data
dimensional projection
 Of course but why do you want to know
that See ultimately you want to find a
max margin classifier and you assume
that your data is linearly separable
And if you project your data onto an
infinite dimensional space then linear
separability is a fair assumption to
make Okay And you anyway have the
slack there Now use a kernel that
corresponds to infinite projection to an
infinite data dimensional space and
ensure that this kernel is valid through
masses theorem Then solve SVM Thats
all you need No that is exactly what
is done actually
Right So lets look at examples for
some valid kernels
So so so please note that never in our
treatment we said that projection will
ensure or guarantee linear separability
Its not there is no theorem that says
that once you project your data onto a
space it becomes linearly separable
There is no guarantee there Yeah So
this is theres something called
polinomial kernel
is you take two data points
x1 x2 and uh the
kernel is 1 plus
x1 transpose x2 this is a scalar raise
it to power p this is the polinomial
kernel
and uh there is cosian kernel
let me write sigmoid kernel
Take data points x i x x1 x2 and this is
equal to
take tan h
a x1 transpose x2 plus b
An interesting thing is suppose this is
your kernel Okay What would be your
final W star with a kernelized version
W star will be mui star plus mui star
time yi times
uh
p of x i right Uh how do you compute
that Now you dont know f
you want your w star
Exactly right You dont want W star
The final classifier is Wrpose X
Wrpose X Wrpose X is FI transpose FX
That will be kernel
You understand that Yeah So you dont
need F for anything The final
classifier will be wrpose X While W has
F of X The the Wrpose X will have inner
products which will be kernel Okay Now
if that kernel okay lets look at that
So so for so final classifier
discriminant function g of x will be uh
wrpose x or v of x
that will be wrpose
p of x and this wrpose is some more
support vectors mui times yi times
p of x Okay Okay This times
P of X
right This will be
P of X I transpose You know you have F
of X that is the tanh
Axi
transpose X plus B
See this is a single hidden layer neural
network
as we will see later
Anyway so thats you know you you can
ignore that comment because you dont
know what a neural network yet is But
yeah so this is what it is Okay
linear function of data sigmoid and some
scaling and a sum which is a which is a
neural network Anyway so the point
that I wanted to make is even to take a
final decision which is compute the
discriminant function you dont need a
transformation all you need is a
kernel right So this is the sigmoid
kernel Another uh kernel that is used
in typically in practice is what is
called as the gausian kernel and gajier
kernel is the one that corresponds to
infinite projection of data onto
infinite data dimension space
caution kernel K G if you take X1A X2
its given by E power
norm of X1 minus X2
by sigma squ
and the final discriminant function will
be very similar to a neural network with
what is called as an RBF kernel but
anyway so thats a side point now this
gian kernel corresponds to uh projection
of data onto infinite dimensional space
Okay
Now gajian kernel is a standard kernel
that is used uh for SVMs because we know
that projecting data onto an infinite
dimensional space you know that is
where you can hope it to be uh linearly
separable So a standard choice for SVM
is the slack formulation with a gshian
kernel Now you have two
hyperparameters right C and sigma
And thats why when you run uh libraries
standard libraries such as libvm it
takes data as one of the parameters that
function function call will take data as
one parameter the other two parameters
are C and sigma
People typically do a grid search over C
and sigma
Okay
Right
This is about max margin classifiers and
SVM Finally what you actually do is
assume uh the slack formulation and
take any kernel typically gian kernel is
taken and then do a grid search over the
parameters and solve the dual problem
using standard solvers to get your mu
and uh mu star and then the
corresponding discrement function Okay
Now there is one little piece that I
have to do before we uh complete this uh
discussion which Ill take 10 minutes
and complete it So we look at SVM from
an erm lens
Just a second as regularized erm
Yes
Huh Correct See there uh strictly
speaking fe is not the kernel K is the
kernel Thats why remember when I
introduced gosh I mean pon window I was
a little hesitant to call that fee as
kernel
because kernel is the one that computes
the inner product between the
transformation So that fee in paren
window is is simply a a transformation
of data Even in generalized linear
regression some people refer to this
fee as kernel
Okay But
yeah uh the kernel typically refers to
this particular function I mean yes now
that you reminded me of that see this
trick okay where you compute inner
products in a projected space okay using
a function that is defined on uh the
pre proed space data space is called
kernel trick and it is used very widely
in machine learning Okay So wherever
you get a formulation where uh there is
some projection and everything if you
can formulate everything in terms of
inner products in the in the projected
space then you can do all of it using
kernels
So there is kernelized max margin
classifiers there is kernelized neural
networks you can think of kernelized in
fact there is something called
kernelized nearest neighbor
because even nearest neighbor needs you
to compute this inner product Now if
you if you can replace this inner
product with a kernel then it becomes
kernelized neural networks I mean
nearest neighbors So this is called the
kernel trick where the trick is that
even without getting onto the uh the
projected space you can do everything
that needs to be done by computing the
kernel in the so if you can formulate
your entire problem in terms of inner
product in the projected space then you
can do everything using kernelized
trick So thats called the kernel
trick Right fine So lets look
complete that final piece Um so we have
SVM with slack as slack formulated this
way Wrpose W plus C times
subject to Yi times Wrpose X I plus B is
greater than or equal to 1 minus Z This is
the slack formulation Correct
Now lets observe this Given
any W and B
Z has to satisfy
this particular constraint it has to be
greater than or equal to the max of 0
comma 1 minus yi
wranspose x i plus b
why is this the case
now I just rearrange these terms okay
bring the zi to left and the other term
to right so which means that zi is
greater than 1 minus this particular
term it can also be zero when
 yeah zi can if if its correctly
classified that can also be zero So it
has to be either this term or zero So
it has to be maximum of those two terms
for any w and b za has to satisfy this
correct
now with if if I if I now I can rewrite
the optimization problem as follows now
So I can why did I do this I did it
because I wanted to uh
combine both these constraints okay into
one and write the lean engine for this
problem Thats it So if I do that its
a minimization over W and B So we have
half Wrpose W plus C times instead of
ZI I can write this
correct
This is the problem Now what does this
look like Now this
is a loss function
plus a regularizer on W
isnt it
And what is the loss function here The
loss function that we are looking at
correct this is the loss function and
this loss function is called hinge loss
Now the punch line is that SVM with
slack
is empirical risk regularized empirical
risk minimization with hinge loss
and an L2 regularizer on your parameters
and the decision boundary that we are
looking at are linear discriminant
functions
of course generalized linear
discriminant functions because you also
have the projection of data onto some
space thats
Now if I were to write this loss
function and then solve it right instead
of doing that
we approach the problem from a different
end right we assume that its a linear
disc function and we wanted to maximize
the margin and we got on to a solution
but if you start from this youll
exactly go to the exact same solution uh
that SVM gives you
So remember the the moral of the story
right Modify the loss function modify
the regularizer your algorithm changes
So everything that we do in machine
learning is modifying loss functions
modifying the hypothesis class and
adding the regularizer
Thats it Right You can do it in 100
ways So this is one way where uh we
assumed it to be uh something and we we
put the constraint or we assume the
discriminant function to be linear and
we put the constraint that the margin
has to be maximized Okay What we are
effectively doing is choosing a
particular type of loss function and
putting a regularizer and then
optimizing for it Same thing happens
with neural networks Same thing happens
with decision boundaries transformers
everything Right So thats why I told
you because regularized empirical risk
minimization is the heart of machine
learning I do it exactly at the
midpoint of the course Its everything
that we do is that in different ways
which is also a basian way of looking at
world
Okay Right So this will uh u see again
as I said SVMs are not the go to choice
of classifiers in todays uh todays
world
However uh we studied this because you
know you look at how to formulate
problems from first principles such a
and also I yeah I I just mentioned that
with this the the the
most powerful result about SVM is that
with this formulation one can show that
the true risk with this uh can be
bounded with the empirical risk and the
number of data points
Okay which which also depends on the uh
the margin distance of the margin So
the higher inversity of distance of the
margin So the larger the margin is the
better the generalization capabilities
Then I think you know machine learning
should be solved No
we can do this then what is left in ML
The problem is that for very high
dimensional data right the assumption
that the data is linearly separable with
the projection fields
In fact u 20 years before not 20
uh late 9s and 30 35 years before uh
SVM was the state of the art
Historically speaking neural networks
uh came much before SVMs
right But SVMs were state of the art
because you could provably give an
algorithm that would that would
generalize But at the scale of data
okay that that that started coming out
in early 2000s etc uh these kernel
functions did not generalize because
there is no guarantee that the data is
linearly separable even after you
project them
Okay Okay So this completes max margin
classifiers From now on from the next
class we will start with we well go to
neural networks Okay which are the
charges of classifiers that are
currently used for most of the
applications uh well look at this back
propagation algorithm and a few
architectures and then well move on to
uh
what are these things I decision
classification regression trees right
random forest and uh uh
 we were before ensemble methods
 what is this uh decision trees
classification regression trees they are
called cards okay thank you thats
