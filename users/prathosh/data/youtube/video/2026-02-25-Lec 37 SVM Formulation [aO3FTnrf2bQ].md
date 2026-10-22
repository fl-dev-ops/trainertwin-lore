---
id: aO3FTnrf2bQ
title: Lec 37 SVM Formulation
url: https://www.youtube.com/watch?v=aO3FTnrf2bQ
date: '2026-02-25'
duration: 33:41
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Lec 37 SVM Formulation

## Transcript

speaker_1: So let us uh formulate this now
So mathematically
by the way um
we are solving a constraint optimization
problem Now right
so we want to minimize or maximize and
optimize a particular function such that
something happens Correct Now what is
our objective function here Objective
function is maximize
or lets say minimize
nom w by two
just take take the inverse with respect
to w We want that w right thats our
parameter Okay Uh such that
is this an unconstrained problem Its
not an unconstrained problem Theres a
constraint What is the constraint
 Huh
 No not mathematically Tell me uh in
English what is the constraint
 Exactly No point should be mclassified
on data Right You need to learn a
discriminant function decision boundary
So how do we write that such that
wranspose x i plus b times yi
is greater than or equal to 1 for all
So this is the problem that we solve in
in SVM
Okay So please look at this You know
its very interesting
uh in our erm
loss was a function of h the parameters
x and y
correct the constraint was in terms of
parameters
Now we have swapped it the objective
function is with respect to the
parameters The constraint is with
respect to data and labels
So it doesnt matter because finally
when we write the leanian
right so this is erm with regularizer
as we will see later SVM or max margin
classifier is actually an erm with a
particular type of loss function called
the hinge loss
This is called hinge loss and L2
regularizer
This regularizer regularizer is always
on W No when you write the leanian it
how does our loss function look like
right It is some function of H comma Y
right this is what it is plus some
lambda times some regularizer on W This is
exactly what it is This L is of this
particular form I will write that
See I can swap it right I can write
that this is my optimization problem and
this is my constraint because when I
write the langian
it is simply function 1 plus lambda times the
constraint So how does it matter if
that is the it only depends on what is
the space on which you are optimizing
anyway youre optimizing on the
parameter space So an SVM a max
classifier
is empirical risk minimization okay with
linear hypothesis spaces
under the hinge loss with an L2
constraint on parameters
Got it
But the good thing is that we dont have
to uh resort to numerical methods to
solve this optimization problem There
is a nice analytical way to solve this
So thats what makes this SVM very
elegant You dont need a gradient con
gradient descent to solve this Do you
see that already that this looks like a
loss function and this is the
regularizer on on the on the parameters
Okay
Right Okay
Now we have to solve this optimization
problem again You know we need to solve
a constraint optimization problem How
do we solve this A grand And I told
you in the last class to look at these
things called conter conditions
KKT conditions right If you have a
constraint optimization problem when
you solve it youll have to write down
something called cont conditions KKT
conditions Let us write that for this
So

the above problem
is
a constraint optimization problem
See the elegance of this entire thing
comes because of two things One
constraint optimization problem with
convex cost and linear constraints
You see this we are sol the optimization
problem is over W Okay And its the
the objective function is convex because
we are looking at two norm
Okay What we are trying to optimize is
norm two which is convex The
constraints that we have okay in terms
of W is are linear
So we are solving a convex optimization
problem
Okay with linear constraints Thats
what makes it elegant So we have very
nicely formulated standard optimization
procedures to solve these kinds of
problems Right Convex uh problems with
linear constraints And can somebody
tell me how many constraints do we have
here
 As many number as as there are number of
data points
Okay Yeah So well have to solve this
constraint optimization problem Uh to
do this
solve the above
by KKT conditions
Okay just for the sake of completeness
Ill simply mention what these KKT
things are So you have a constraint
optimization problem First you write
down the lrangian Okay Uh you write
down the lrangian and
there are three or four constraint
conditions which are called the
conturren KT conditions
I mean one of which is known to
everyone Whenever we are solving an
optimization problem we know that the
derivative of the objective function has
to go to zero Right That is one of the
conditions So like that we have three
four other conditions that we will write
down and we will use the the KKT
conditions Okay And we formulate what
is called as the dual problem
theres something called duality in
optimization which means that for every
primal problem okay there exists a dual
problem in the dual space right where
the constraints and the object I mean
the the uh the optimization variable get
swapped okay so we can solve both the
primal and dual problem simultaneously
to find the solutions for both the
primal problem and dual problem that is
what we will do so what we will do is
the entire process is as follows
we start with this problem write down
the kk 80 conditions Okay And then we
write the dual of this the dual always
of a primal problem will be a will be an
optimization problem over the lrangian
multipliers
always
correct and then we show that the uh the
dual problem can be solved using
standard solvers
So what will be solved finally in an SVM
is the problem in the dual domain using
standard solvers standard optimization
solvers Once you get the lean
multipliers you can always come back to
the primal domain plug them in and find
the W and B That is the whole idea We
will write down this W and B the optimal
W and B in terms of the data points and
the lean multipliers optimal
multipliers You understand The first
step is to show that the optimal W and B
will be a function of the data and leg
multipliers
Okay that is what we do by writing
KKTs And then to get those leg
multipliers which are needed to find the
optimal W we solve the dual problem
Thats the idea That is all well do
now
Okay So lets uh write them all one by
one
So first of all lets write the uh
leanian
I cant emphasize this uh emphasize on
this uh enough uh see learn three math
tools very well and you can do all ML
probability theory
okay little bit of matrix calculus and
optimization thats all everything is an
application of these three
okay so all machine learning is simply
application of these three ideas as you
have seen already right you need to know
how to optimize you need to know how to
deal with density functions thats it uh
yeah
okay so define legrangen for this Um so
lrangian L
this will be a function of the variable
upon which we are solving the
optimization problem and lrange
multipliers lets call them as mu okay
this is equal to uh the constraint which
is
nom w
Sorry The objective function which is
nom w plus
come again by two Ah we can ignore
that Its okay Uh because that thats
a scale No uh well well leave that
out actually Plus okay so how does the
lean engine look like There is one lean
multiplier
corresponding to each of the
constraints
Correct So that would be
uh 1 minus no lets write the constraint
no one minus okay so first of all there
is a sum
sum over
all the data points because every data
point is a constraint and the constraint
is 1 minus yi times wrpose x i plus b why is
this see this can be rewritten as
1
uh wrpose x i plus b times yi
uh typically this is how you write the
linear constraints right less than or
equal to zero so
this is what it is and this multiplied
by mui so every constraint has a leanian
multiplier associated with it right this
is the this is the um
objective function Okay actually I was
wrong about it We want that two
otherwise algebra wont work out Okay
Wrpose W by two
 Come again
Yeah Here
theres a B as well
 Yeah
 Where this one
 Wrpose W is right
 Yeah its okay
Its a positive number and putting a
square there doesnt matter but anyway
Yeah Okay Fine So you write it as
Wrpose W because when you take the
derivative right with respect to
vectors its easier to write it as 2 times
W and cancel that two out Thats why we
need that two also Algebraically it
works out nicely Okay Now uh okay
KKT

Theres an interesting story why there
are three names
to this these particular conditions
There are three different people They
did not collaborate
Yeah there are three people No uh
its a I mean I I you dont narrate the
story you look at it its very
interesting okay um

yeah the first condition is that the
gradient of the legangian with respect
to the optimal parameters and optimal
lrangian multipliers has to be zero
correct
this is the first one the second one is
that
all the optimal agent multipliers have
to be non negative
And the third one is
the product of the lranian multiplier
with the constraints
Uh this has to be zero Correct
These are the three conditions Okay
Okay So let us uh uh apply all this and
see what happens The first one which is
uh the yeah
the derivative of uh this with respect
to
come again
where here
its true the derivative of this uh with
respect to l has to be zero This
implies so Ill skip the algebra please
do it So which means w times will be given
by
mui times
yi
x i
Please do the algebra Take the lrangian
and take the derivative of it Actually
you can see it very simply right If you
take take the derivative of this with
respect to w there will be a w here
right and uh this mu term will go away
and uh y wrpose x i term is around right
and mui will get multiplied and w will
go away therefore what survives is only
mui star yi times x i thats it simple see
this is a very interesting equation this
find we already got our optimal uh w
what is the optimal w optimal w is
simply a linear combination of multiple
data points Thats it
You see this
 Well do it Well do it now Well do
it So this simply says this is a
remember this is a very strong result
that the optimal W is simply a linear
combination of data points because this
Y is simply plus one or minus one
right And mui are some constants or
scalers like multipliers are scalers So
this is saying that my optimal w is a
linear combination of x i In fact we
will see that it will not be a linear
combination of all x i because for some
x i this mui will be zero So this is a
linear combination of all those data
points for which mui is non zero and
those data points are called support
vectors and you will see that those data
points are the ones that lie on margin
Well see that well see that
algebraically when we do that But
basically the idea is that the optimal
uh parameters is simply a linear
combination of a few data points scaled
by the multipliers Okay
And as uh he said well have to take a
derivative of this with respect to B as
well So this will imply
that uh the product of
well use this result later
The second constraint is simply that all
muis have to be greater than or equal to
zero for all i
And uh the third condition is
um actually I already written it there
Okay fine
Now so define
a set S
which is a set of all X size for which
the LER multipliers are non non zero
See we know that lean multipliers right
one of the KKTs tells you that the lean
multipliers all have to be non negative
I mean they can either be zero or
 positive now lets consider all those
xis for which the lean multiplier is
strictly positive okay now this implies
that my optimal decision boundary
is simply a a linear combination of
the vectors in that
Isnt it See look at this right I
mean I just I actually already
mentioned it that the ones for which mui
star is zero will anyway go away The
only things that will survive are the
ones for which this is strictly
positive And those vectors are called
support vectors
Okay for which the grand multipliers
are positive Okay now what should we
do to find the final decision boundary
war We need to find the optimal lean
multipliers
Come again star Yeah well have to
find the optimal lean multipliers Okay
any questions so far
Okay good
Now to
get war
we need
The optimal lean multipliers
new star
Okay Now to find
new stars
we solve the dual problem
Okay
Is there anybody who does not know what
uh duality is in optimization theory
Okay There are a few people Okay Let
me just quickly tell you what it is Uh
if you solve a constraint optimization
problem right Uh how do we do it
Theres a problem and there are some
constraints So we change that
constraint optimization problem into an
unconstrained optimization problem by
writing this thing called legangian
Right Now
there is for this is called the primal
problem Okay which is the lerangian uh
function that we are optimizing So this
lean engine as we saw will be a function
of two things One the optimization
variable and the lean multiplier which
are constraints
This is the generalized version of
whatever we saw right now is is that
that to solve any constraint
optimization problem The optimal
solution will be a function of the
optimal multiplier as well So remember
when I when I when I said that uh
putting a penalty on the norm of the
parameters as a regularizer is
equivalent to a lean uh solving a
copizimization problem and I told you
that here we dont search for optimal
grand multiplier but we treat as a
hyperparameter
thats not the best way to solve the
problem because there exists an optimal
lean multiplier okay as we saw here So
there is a mu star here which is an
optimal grand multiplier that gives you
the exact solution for the primal
problem Now how do you get the optimal
grand multiplier It is by solving
another optimization problem which is
called the dual optimization problem
where the leg multiplier becomes the uh
the variable for optimization
Okay So every primal problem a
constraint primal problem will have a
corresponding dual to it and their
solutions are related That is what a
dual problem is So thats duality of
optimization problem So why do we need
to resort to duality is because
in some cases solving the primal problem
is easier In some other cases solving
the dual is easier So in this
particular context solving dual is
easier is what we will see In fact
again you know referring back to my
next course there is one uh u uh
class of algorithms okay generative
algorithms called optimal transport
Might have heard of name called versus
GAN or W GAN Theres a problem called
optimal transport Okay its an
optimization problem All problems most
problems in optimal transport are solved
in the dual domain
Okay so this duality is a is an
important idea there Okay So so we
have to solve the dual problem to find
mui star So how do we uh solve the
dual problem So let us look at what
duality is first
Now we have uh the primal problem which
is
Lets say that it is some function of W
and
okay let me not introduce new notations
Ill write the entire problem itself
here hold

 Okay this is the problem that we have
Now define
a dual function first
dual function Q Okay which is a
function from R
N to R where N is the number of leg
multipliers
The dual problem dual dual function will
always be a function from R N to R where
N is the number of leg multipliers
always Okay So how do you define that
Q mu
is the infyum over the lrangian
and this infyum is uh obtained over the
optimization variable of the primal
problem
What is infyum
 No no no no hard min is the minimizer
So min is the minimum
What is infyum
Theres a theres a name for it right
I mean
 huh
 Its the least upper bound
So basically what is the difference
between minimum and infyum is minimum
can be achieved
Infyum may not be achieved Thats it
Say for I mean if if theres a set uh
whose minimum you can find it is a
function whose minimum you can find out
over a particular set then its minimum
So you cannot find that minimum but it
exists then its called infyum Thats
it Okay So youll have to find the
infyum I mean see most of the problems
you can actually write this as minimum
if uh you can minimize this with respect
to w But the most generalized way of
writing it is in in terms of infom
thats it So youll have to so no note
that this becomes a function of mu
why because
we are optimizing with respect to w here
right we find out that function of I
mean that point uh in the space of w and
mu that with respect to w
so this function l is a function of both
w and mu correct so we navigate through
the w space and find the value of this l
for which it is minimum in the w space
so that becomes a function of mu Thats
it So thats the dual function

 Is it the greatest lower bound or the
least upper bound
 Yeah it is the greatest
 greatest lower bound
 Correct Yeah
See there are a few things that never
get to my mind So one of this this is
this false positive false negative type
one type two error The other thing is
infyum and supreum I know what they are
but are they the greatest lower bound or
the least upper bound Ill have to
think about it before I get it right
Okay So its the greatest lower bound
Fine
Okay So this is the dual function
Well have to define what is called as a
dual optimization problem Okay So
construct
the dual optimization problem
as follows
So well have to uh maximize
So please note that if primal is a
minimization problem dual will be a
maximization problem and vice versa
Right So because the primal that we
have written is a minimization problem
The dual will be maximization Maximize
this dual function Okay with respect
to the lean multipliers subject to the
fact that the lean multipliers are non
negative
Thats it
So this is the dual problem
Now what we should do is that uh well
have to write con first construct the
dual function Okay And then well have
to solve this dual problem That is what
we will do right now Okay
here
 assuming that it can be achieved in this
particular case at least it can be
achieved Huh Okay So this is what we
should solve and to solve this we need
something called the primal dual
relationship
See all these have rigorous proofs
Okay Im Im just using them assuming
that uh people have the background in
optimization theory Um
so what it says is war is
okay war and muar
are
optimizers for primal and dual
respectively
If and only if
one So W star
and mu star are feasible
for primal and dual respectively
I didnt define feasibility
Okay feasibility means that uh you take
that particular value all the
constraints are satisfied with that

Okay so thats called feasibility So
both of these have to be feasible Okay
And we have
the
the minimizer of the primal problem
is
the minimum of the
this is obvious right because this is
how we construct the dual
So if we take if we take the lrangian
okay and evaluate that that the
minimizer optim the minimizer of the
priv and the dual problem it is equal to
evaluating the dual function okay at its
minimizer
after being minimized with respect to w
thats it I mean obvious right because
this is how we defined our dual function
when we solve it this is how it has to
be
which what is max no see this is the uh
the definition of the uh dual function
right this infom this infyom is what Im
writing as minimum there
right you minimize with respect to w
dual problem is maximizing with respect
to mu see here Im writing the optimizer
or the the lrangian evaluated at the
optimizer of the primal and the uh the
dual problem is equivalent to evaluating
the dual function okay at mu star after
minimizing with respect to w thats
correct
Okay
Okay So
huh This is how you construct the dual
problem I mean the the uh dual
function You first you have to start
with construct the dual function by
minimizing over W that get that gets you
the dual function and then you maximize
the dual function with respect to
multipliers which is the dual problem
 which one
 yeah Q is a function of mu
see first you minimize with respect to w
right and then uh you okay so perhaps I
should write it this way hold on I mean
I I see what the confusion is let me
write it this way Hold on
can actually write it as
so you take a minimum of
the lrangian
respect to W This is okay No
mean minimizing L with respect to W will
give you Q
Okay and then you evaluate that Q at Mu
star Thats what I meant
Okay
Okay So uh I think this is a good time
to stop this particular discussion
Well stop here and next class what we
should do is we should actually
construct the dual optimization problem
and solve the dual problem And solving
this dual problem will give us an
optimization over
mu and that I said will be solved using
standard solvers to get the mu star and
plug it back to the primal problem to
get the uh the the optimal discriminant
function So after that we will go to
the not linearly separable case then we
will look at kernel machines right we
the kernelized version of SVM which will
end the discussion on SVM Okay Thank
you
