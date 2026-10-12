---
id: 7F8pknXk_-o
title: Lec 33 Regularization
url: https://www.youtube.com/watch?v=7F8pknXk_-o
date: '2026-02-25'
duration: 28:27
model: youtube-captions (en-orig)
transcript: true
---

## Transcript

So welcome everyone So in todays
lecture we will continue uh our
discussion on the bias variance
decomposition So last time we saw that
with the goal of minimizing the risk
function when we start building
algorithms
the errors that we encounter can be
decomposed into two parts Right The
one was called the bias Uh the other
was other was called the variance
Bias refers to or rather bias measures
or quantifies
what is the deviation of the classifier
or the hypothesis that the algorithm has
yielded us from the true minimizer of
the risk underlying risk Thats the
bias term And variance quantifies how
sensitive is our hypothesis to a
particular
choice that we have made of the data set
or how how sensitive it is to changes in
the data set is what variance captures
And a good classifier is the one that
minimizes the risk Right And to
minimize the risk you want both the
components of the risk which is the
bias and the variance to be
simultaneously minimized
Okay uh a good hypothesis is one that
would minimize both the bias and the
variance simultaneously
However as we discussed in the uh
previous lecture
when you have smaller models limited
parameter models and limited amounts of
data typically there would be a tension
or a trade off between bias and variance
uh in the sense that if you try to
minimize the variance the bias would
increase and vice versa
Now why would this happen is the
question Okay Now this happens because
of uh uh something called no manifold
hypothesis
Uh well discuss more about this in the
generative modeling course But the
roughly the idea is the following right
So think about this So we are we are
dealing with data right which are which
are vectors in three dimensional real
space right now Lets say that we are
looking at uh
images for instance and lets say that
we are looking at binary images Okay
the images that will only have one or
zero as their pixels
grayscale images Okay they can be
looked into as binary images Now
suppose you are looking at lets say a
100 by 100 image then
all the images or the data points that
you get are vectors in 10000
dimensional space a 10000 dimensional
space which has binary values into it
Right That is what it is So it is an
image would be a point in
this particular space Right
Now lets say that we do this experiment
where
we assume each of the pixels each of the
grids of this image as an independent
Bernoli random variable Okay Then we
toss a coin with probability P Now if
that coin turns out to be head then we
will fill that pixel with one and if it
turns out to be tail then we will fill
that pixel with value zero Okay Now if
you toss 10000 times you get one image
Do you understand Right So basically
its 10000 independent Bernoli trials
is what you do to get one image Now
tell me what are the odds that by doing
this experiment you will end up getting
a meaningful data set like mnest
what is it
its extremely low its a non zero
probability but its extremely low but
in fact this is also known as a
typewriter monkey problem where the
thing is you know you make a monkey sit
in front of a do you know what
typewriter is genz people
okay there used to be a device called
typewriter right where people used to
you know type set and print and all
that So yeah so you make a maybe for
the newer version of it is you make a
you make a monkey sit in front of a a
keyboard right and see today with all
these uh voice based models coming in
maybe 2 3 years keyboard also will
become obsolete who knows anyway so you
make a monkey sit in front of a
typewriter or a keyboard and make it
randomly press the keys the question is
what are the odds that it comes up with
Hamlay
Shakespeares Shakespeares work what
are the odds its a non zero probability
but its a very less number Right Now
think about it right P which is a
Bernoli which is the probability of
success of a Bernoli trial is by
definition less than one and you
multiply that 10000 times it become
very very less no matter what how higher
the probability is Now what does this
tell you This tells you that the
eminest data set that we get right
occupies a very very small space in this
ambient 10000 dimensional space
Do you see what Im saying So this is
called manifold hypothesis Okay which
mean which which says that most of the
data that we get in practice occupies a
tiny little manifold as it is called
Manifold is a topological object Ill
not define that Think of it like a
subspace Okay its not a subspace but
think of it like a subspace Very very
small tiny subspace in the ambient
space So data that we deal with always
occupies a very very small uh subspace
or a manifold in a in the ambient space
that we are operating with Okay Now
what does it do What does that has to
do with bias variance decomposition is
the question Now if you are trying to
build a regressor or a classifier on
this particular data what are you
trying to do you are trying to
partition this manifold
See what is a classifier uh at the end
of the day if youre looking at a binary
classifier all that you are doing is
its a set set partition function right
I mean given thousand data points itll
group one set into one particular class
the other set into its its basically
uh creating subsets of the support set
of your random variable that is what you
are trying to do as a classifier now if
you were to do that in an ambient space
okay over a data set that that occupies
very very small tiny manifold
Then what happens is that if you want to
explain the the given data set then you
will tend to end up overfitting it
because you want to explain everything
right So since it occupies extremely
tiny space if you were to build
something now partition this very tiny
space in your ambient space then you
will have to build something that is
extremely specific and confined to that
tiny manifold
That is why the problem is unless you
have large amounts of points in your
data set that would occupy much more
space in in the ambient space Its very
hard to build classifiers that would
have both bias and variance extremely
low So now suppose you you you end up
lets say that you have a tiny tiny
manifold that you are dealing with and
you want to explain the data that you
are given I mean thats the only thing
that we can do in erm and in do in while
doing so you build a classifier that has
very high bias which is sorry very uh
yeah the overfitting region if you get
there obviously if you change that
manifold if you move that manifold from
one point to the other which is your
test data set you are going to do very
badly
right so variance will be very very
large in that kind of a case so if you
end up
not making the model
have a large variance then you will not
even explain that small manifold that
you are given with which is the
underfitting regime So that is why in
practice because of this fact that data
occupies an extremely small tiny
manifold in the ambient space and you
are trying to explain your data with
very small number of samples you will
always end up if you want to optimize
for bias or reduce the bias then you
will end up increasing the variance and
vice versa
Okay Now when does the scenario change
The scenario changes if you have a very
large amount of data
Right So the the tiny space that it is
occupying now becomes extremely large
So now lets go back to our typewriter
monkey problem Right Instead of making
it type ham if you if you if you ask me
what are the odds that it will type one
word that makes sense the odd will go
up right So thats expanding your data
space
Now thats why todays uh ML methods are
effective because the kind of amounts of
data that we are dealing with are so
large right that you can hope to reduce
the bias and variance both of them
simultaneously but typically that does
not happen and we saw that behavior in
the in the previous class right the this
is the the usual bias variance uh curve
right where
as you increase the model capacity
till a point I mean the the the error or
the accuracy on the training data keeps
decreasing while the accuracy on the
unseen data keeps decreasing till a
point and then starts increasing You
will have to see this behavior right
Okay So given this background the
question now is what is the best way to
operate in a pragmatic approach So I
told you uh the last class itself that
typically what is done is that you start
with an over over parameterized model
right over fit the data and then
increase the bias push the model back so
that this is the ideal operating point
and to get there you start with an
overparameterized model and increase the
bias of the model Okay Now any
technique that is used to increase the
bias of a hypothesis is referred to as
reg regularization
Thats why I had to give such a long uh
prologue today See uh regularization
refers to
so techniques
to increase
the model bias
Okay there are multiple ways to do
this Um starting from uh uh penalizing
uh your empirical risk uh the loss
function or
restricting the hypothesis class to a
particular particular functional form is
also a way to increase the bias So
remember what we said in the earlier
classes
The moment you restrict your hypothesis
to a particular class of functions it
it amounts to putting a restriction on
the class conditional density
Right Any choice that you make on your
class conditional density is increasing
bias
Now all models are implicitly biased
See unless
they are you know they are even if they
are even if they are universal
approximators the moment you make an
architectural choice or a design choice
at a hyperparameter level then you are
imposing a bias on the model
So there is no unbiased model All
models are biased Now the question is
by regularizing you can steer this bias
You can actually increase the bias
Right So there are multiple ways to do
that As I said any architectural choice
is a bias You know thats why I keep
saying that any innovation that that has
happened in coming up with newer
architecture is actually imposing some
sort of a bias on the model including
transformers
We well well see that I know as we
move on in the course and thats why I
do this I uh I deal with this topic at
the at the exact know juncture of the
course so that we well well carry this
idea throughout this course any
architectural tweak you know
convolutional neural networks and you
might have heard these terms right
Recurrent neural networks and all these
the these are all adding biases onto the
model by doing an architectural change
The other way to do it is to modify the
loss function as we will see now So
there are multiple ways to increase the
bias of the model We will see one or
two ways in this particular course
Okay So any technique that is used to
increase the bias of the model See when
I say bias you should know what Im
talking about Its that exact term the
that expectation of uh HD minus that
that exact term is what Im saying by
bias So now its not an English term
right Its it has a precise
mathematical definition So anything
that we that we use that any technique
that we impose that we use to increase
the bias of the hypothesis is known to
as regularization Okay
Right So now let us look at uh a couple
of ways to do that So multiple ways you
know one is called uh have uh so
so parameter penalty is one way to do
it
Youll see that or like architectural
choices or restrictions
And you can also uh impose bias by
changing the way you optimize So
optimization changes
We will see examples for all these okay
as we move on So let us look at the
parameter penalty way of doing it
So regularization through
so parameter penalty
Okay So what is erm So recall that erm
is that you find a function har cap of x
as the minimizer of
the
empirical risk
So choose lum some loss function and
this is h of x comma y
Yeah this is and we do this uh over
class of h This is what our ERM is
right now Regularized DRM
So let let me write this function as h
theta of X because you know these are
parameterized with some parameter theta
right
Define a function
uh
omega of theta which is a function from
the parameter space
to r plus typically
Okay And this is called the
regularizer
and
define a new objective
as follows
Call it regular SDRM
So find har of x
as the minimizer of
the same regularized
risk
So now instead of solving an
unconstrained optimization problem you
solve a constrained optimization
problem Right subject to
this function
Okay Uh you can have any kind of uh
regularizer This is one way to
regularize where K is some positive
number
Right So now this is the problem that
you write now solve So instead of
saying that
uh solve erm you say that you solve erm
with a constraint that this particular
function is bounded
Now there are two questions here One
how do you choose this function
Actually three One how do you choose
this function The second question is
that how do you solve this constraint
optimization problem The third question
is why would this increase the bias
Okay lets look at all of them The
first thing is lets see how to solve
this Okay to solve
so you all know how to solve a
constrained optimization problem How do
you do that Change the constraint
optimization problem into an
unconstrained optimization problem by
defining what is called as a leanian
Right So the
the lerangian
is already taken alphabets
the function of theta
n is for okay Ill write rcap rcap
for uh capital rc cap for empirical risk
and uh the subscript is is to denote
that it is regularized okay so this
1 by n
So what is uh lrangian So you have some
lambda times
minus k
solve this problem So this optimization
problem So theta star is
the minimizer rather I can also say h
theta star is the minimizer over theta
minimize the regularized r disk
Now people who have done optimization
theory know that if you want to solve an
a constrained optimization problem you
construct a a regular I mean you
construct a leanian and you solve two
optimization problems right one is the
primal and the other is the dual This
is the primal and dual will be an
optimization problem on the lean
multiplier lambda Right But typically
in uh in in in ML community its not
solved that way So this lambda is
assumed to be a hyperparameter and it is
fixed uh using the validation data So
you dont solve the primal dual problem
Now you just fix it with some particular
value And by the way in ML community uh
this thing is called the regularization
constant
Its called the regularization constant
Choose that as make that a
hyperparameter and use validation data
to fix it Thats how it is done
Okay Uh yeah So how do you solve this
optimization I mean how do you do it in
practice for some algorithms Uh this
will become analytically differentiable
so that you get a solution over theta I
mean just like we did for linear models
for some I mean so for most of the
models depending upon the choice for h
theta this optimization problem cannot
be solved analytically you need to
resort to the numerical methods and we
have gradient descent to solve it thats
it
okay the update rule for the gradient
descent would change with this
particular function because you need to
now take a gradient with respect to
omega as well
make sense okay so this is how you solve
it h now the question is choices for the
regularizer
which data is just solve
solve analytically
or
numerically
So nothing changes the only the what
changes is the the objective function
with respect to which you are optimizing
would change if you add a regularizer
Okay thats it Now the next question
is what choices should we have to make
on this Now uh later part of the class
I I will show you that this is precisely
equivalent to getting a basian estimate
Now this question of what choice should
we have to do for regularizer is exactly
the same as what choice should we have
to make for the prior that we choose on
the parameters So Ive been telling
that that the prior that we choose is is
a userdefined parameter and that is why
its called bias
right whatever choice you make you make
but the thumb rule is to make a choice
such that the choice on the prior that
we have made is meaningful
in in what sense that remember our
example on the the basian estimate right
if we are if we are tossing a coin and
we are estimating the success
probability using basian methods
We use the physics of the problem to
constitute our prior can be a conjugate
prior as well in the case of map Right
So similarly look at what problem you
are solving and depending upon the
problem that you are solving you make a
choice on the regularizer function
Okay So there is no systematic way of
doing it in the sense that since its a
its its a userdefined choice
whatever choice we make is the choice
that we have to live with right but and
we make this choice pragmatically
depending upon the physics of the
problem Thats how we do it Ill give
you a few examples of it So one way to
do it is so uh use this to be
P norm of parameters
Okay So specific cases right if you
have this to be two this is called the
L2 regularizer
and if you make it to be one it is
called the L1 regularizer It also has
other names I think this is called uh
this is lasso this is ridge
So one is called lasso the other is
called ridge I keep forgetting which is
what which is what
 come again
 This is lasso
This is rig
Bad at names No thats why I keep
saying no L1 L2 is better L2 for two n
L1 for one N Right Okay So you use uh
par nom penalties right on uh on on on
on on the parameters and that is one
choice to theres no reason why this has
to be uh the norm can be anything else
This is one way to do it Now why is
this choice made Was it what is the
rational for this is this typically
comes from uh the polinomial regression
community See remember in our example
the two hypothesis that we chose one was
uh the one that was oblivious to data
the other was uh uh just the other was a
lookup table I also told you that if you
have 10 points and youre looking at a
polinomial generalized linear regression
you can have a 10th degree polinomial
and then
uh you can get 100 percent accuracy now suppose
you regularize the two norm of this
polinomial regressor
How many parameters does a polinomial
regressor will have 10th degree
polinomial regressor will have 10
parameters right 10 or 11 I mean if you
count the constant as well so this is a
11 dimensional 10 dimensional vector now
what am I saying by putting this penalty
here is Im saying not only reduce the
the empirical risk but also ensure that
you choose the parameters in such a way
that the norm okay of this parameter of
the parameter vector mind you the norm
of the parameter vector is reduced
You see what Im saying What would the
regularizer do Okay regularizer would
say that along with minimizing the
empirical risk we should also minimize
the norm of
the parameter vector
Okay now think about it What would be
the minimizer for a 10 dimensional
vector What is the minimum value of a
10 norm of a 10 dimensional vector
 All zeros Okay so the the optimizer
would gravitate towards making all
parameters zero
But it cant do that Why Because the
other objective which is minimizing the
empirical risk has to ensure that uh the
the loss that we have observed on each
of the data points that we have also has
to minimize So it cannot
gravitate towards making all parameters
zero Now what would it go to is the
question Huh Some of them
 yeah some of them will be made zero or
some of them will be made smaller Which
ones will be made smaller The ones
 why I mean it depends upon what your
underlying distribution is If your
underlying distribution in the case that
we took right I constructed a
distribution by pter being a parabola
You see which is that it is perturbed
over a second degree polinomial In that
case if this optimizer has to minimize
both the objectives okay especially
the empirical risk it has to make sure
that the higher order terms are put to
zero or the coefficients corresponding
to the higher order terms are put to
zero Otherwise if the underlying
reality is close to uh like uh low
frequency or you know uh lower degree
polinomials then you you cannot bring
the empirical risk lower by putting the
lower degree terms or the coefficients
corresponding to the lower degree terms
towards zero You see this So this is
how regularizer works
Okay Putting a non penalty So now you
see for those problems in which the
reality is mostly low frequency
parameter non penalty works well
make sense okay I mean you understand
what low frequency means right
I mean in images what is low frequency
you have if you have lot of uh you know
pixel noises etc sharp edits they are
high frequency if you have smoother
images they are low frequency again one
can make an assumption that most of the
data that we get are typically low
frequency and thats why nom penalty
works as a good regularizer
Do you see how it works Yeah So nom
penalty is one way to do that for for
the regularizer The other way uh to I
mean other choices can be see as long as
its a function that you are choosing
one can choose any function on on this
So you can actually make this to be some
negative exponential of this
right this can be another regular result
and so on again its a its a design
choice one can choose it to be uh
anything so thats thats a possibility
okay so two we have answered two
questions which is how to solve
regularized DRM so what choices should
we have to make for regularizer the
other question is yeah question
L
 L0 is not a norm
 You know that its not a norm do you
 Right So okay you can I mean you you
can choose uh L0 as a choice for this
but uh uh you youll have to also ensure
that the the the function that you have
chosen is differentiable
because youre ultimately solving an
optimization problem and youll have to
uh the numerical differentiator or
whatever right has to ensure that it is
differentiable and L0 is not
differentiable but of course if you can
take some uh you know subgradians or
something and manage with that L0 is
fine Yeah
Uh okay Uh we will stop here and
continue in the next lecture
