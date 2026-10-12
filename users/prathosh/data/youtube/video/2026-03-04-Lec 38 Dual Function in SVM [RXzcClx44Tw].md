---
id: RXzcClx44Tw
title: Lec 38 Dual Function in SVM
url: https://www.youtube.com/watch?v=RXzcClx44Tw
date: '2026-03-04'
duration: 21:09
model: youtube-captions (en-orig)
transcript: true
---

# Lec 38 Dual Function in SVM

## Transcript

Welcome to this class. We'll continue
our discussions on uh the maximum margin
classifier or support vector machines.
A quick recall last time we constructed
the primal problem of optimization
in terms of uh the parameters of the
linear discriminant function and we said
that this problem will be solved in the
dual domain. Okay. So constructed we
were at the
path towards constructing the dual
problem for the optimization uh primal
optimization problem that we had that's
where we were. So the definition of a
dual optimization problem is that first
we have to solve this
inum problem that you take the grandian
and solve the infom problem to get what
is called as a dual function.
Once you get the dual function,
construct the dual optimization problem
as the maximization of the dual function
with respect to the lean multiplier. So
now the variable of optimization becomes
the lean multiplier itself. Okay. So
please note that here to even construct
the dual problem okay uh or the dual
function an optimization problem has to
be solved first. Correct? Okay. So now
let's continue there. we'll just uh
construct the dual optimization problem
and then try to uh solve it. Now what we
have to do is
Q mu the dual the dual function.
First we will construct the dual
function. Q mu
is the infyum
over the lrangian.
A grand is half wrpose w
plus
sum over
the constraints wrpose x i + b.
Yeah, we'll have to take the uh infyum
with respect to the variables of
optimization in the primal problem which
is w and b.
This is the definition of the dual
problem.
Now please note that we are now looking
at the infyum of uh this objective okay
with respect to w and b h.
Now if you look at uh the objective
function there is
observe
observe the term
product of uh mui
yi bi.
So we have this term right uh inside the
objective function that is mui yi and
bi. You see this here.
Now this is a function of mu. So now if
we do not have any constraint on this
then this infyum is unbounded
right what does it mean? So uh you can
choose a b and a mu such that the infyum
is minus infinity.
Okay which means that this problem
cannot be solved in an unconstrained
way. We'll have to constrain it. So how
do we constrain? So the the way to
constrain is that you'll have to solve
this infom problem um
which
observe this term which can drive
the infyum to
minus infinity which is undesirable.
Okay. Therefore, solve a constrained
version of it
by forcing
the product of mui * yi make this to be
zero.
If we drive this to be zero then you
cannot choose a b such that this problem
uh the has a solution that goes to minus
infinity. I mean you are making it
bounded. So the to obtain the dual
problem we'll have to ensure that we not
only solve the infom problem but we
solve it with a constraint that this
product goes to zero. Okay.
So what to to solve this problem? So to
solve the constraint in
minimization problem
how do we look at the infyom of a
particular function? See and the infom
or the minimum is minimum here is with
respect to w and b. Okay. From the uh
duality property right which is if war
bar star and mu star are feasible for
prime and d respectively we know that
the optimizers for both of these
functions are the same which means that
this q mu will attain infyum at w equal
to war where w star is the optimal for
the primal problem. Correct. So what we
should do is that to above to solve the
above problem substitute
t
sub
t substitute
w star to be equal to
i over support vectors. What is that?
This is mui yi xi. Correct? This is the
one and B star
the optimal B star um I leave what the
optimal B star is. Please do the algebra
and find out what the optimal B star is
for the primal problem
or rather let me just write that down
the optimal B star would be
let me do it.
It's good to have homeworks. So find out
what the optimal B star is for the
primal problem. So we substitute that B
star and war in Q mu we get our Q mu to
be
which is the infyum. See once we
substitute war star and B star or W and
B to be W stars and B star which are the
solutions for the primal problem we are
actually getting the solution for the
optimization problem. Which optimization
problem? The infyum. So what we get is
the infyum. So Q mu will
look like this. It will be
a sum over this minus
half
sum over i some / j
mui.
Y I muj y
x i transpose xj.
So once again I want you to complete
this algebra. What should be done? Find
what war star is, the optimal war star
is. And I mean we already have what
optimal barst star is. We have find what
bar star is. Plug them both into this
particular equation. Okay. and expand
the terms and drive the product mui yi
to be zero.
Okay. And if you do that the algebra
work works out to be like this. Please
complete it. It's it's simple algebra.
Just do it. So what is to be seen is the
following. Right? The observation is
that in the dual problem okay I'll write
that in the dual problem
the data x
only appear
as inner products.
This is a notable point now we will use
this later. What am I saying here? Look
at the dual problem, right? The
dependence on data X term is only as
inner products here. Take a pair of data
points X I and XJ. Compute the inner
product between them and that's what
appears in the dual problem. Remember
last time I told you that sometimes
solving the dual problem is easier in
the uh in the in in optimization
scenarios. This is one of the reasons
why this is the case. Now in some cases
as we will see later computing inner
products is easier than computing the
data points themselves. I'll I'll tell
you why that happens in a while but this
is an observation to be made that in the
dual problem the data appears only as
inner products.
Okay actually I can quickly run through
the algebra right where is this inner
product coming from? It is coming from
this wrpose w term because w is linear
in x
right. So therefore wranspose w will be
quadratic in x. Therefore and since you
have inner products in w that will
translate to having you know translating
into inner products in x. That's how it
comes up. Okay. Okay. So this is the
dual problem now.
So let's write down sorry this is the
dual function. Uh let's write write down
the dual optimization problem.
So the dual problem is maximize
q mu which is
sum over mui
minus/
UI muj wi wj
x I transpose xj.
So we have the constraint subject to
all mui are uh non- negative. We also
have another constraint that
this has to go to zero.
So this is the final problem that we
have to solve and this maximization is
with respect to mu.
This is the dual problem. Okay. Now if
you look at this problem right this the
above problem
is quadratic
in mu with
linear constraints
isn't it this problem is quadratic in mu
correct
because you have the product terms mui,
muj kind of terms which are quadratic
terms. Uh and there are linear
constraints on mu. Okay, in optimization
theory, this problem is known as the
quadratic programming problem with
linear constraints. This is a QP problem
with linear constraints.
Okay, now how do we solve a QP problem
with linear constraints?
If you studied optimization theory, if
you have a QB problem with linear
constraints, there are standard solvers
to solve it. Okay, there are methods to
solve this. Let me not go there. as well
as some one of the algorithms to solve
this is called um sequential minimal
optimization
SMO
standard QP solvers
for instance is
sequential minimal optimization
SMO.
Okay,
that's it. So I'll not go uh to the
details of how to solve a QP problem.
Okay. So assume that I'm assuming that
there are solvers that would solve a a
standard quadratic programming problem
with linear constraints. One of the
algorithms is called SMO. Okay. And
there are libraries to do this. One of
the u famous libraries that is used to
solve this problem is called lib svm.
It's I think it is
originally written in C and now there
are Python wrappers and so on. Okay.
Okay. So where uh actually this solves
this particular problem given
um
a QB problem with linear constraints. It
implements SMO to get the solution for
this particular problem. Okay.
Now what happened given a particular
problem
a classification problem what do we do
in uh SVM?
Construct the primal problem from primal
problem construct the get the obtain the
dual solve the dual as a QP problem
using standard solvers and get your mu
stars. Okay, once you get the mu stars
so we have obtained mu stars right now
by solving this right. So once
mu stars are obtained.
Okay, find
W star which is what we want finally to
be
correct. This is what it is. H
and similarly you get the B star as
well.
So this is what we wanted. Finally we
have the mu star from the solution of
the smo problem the the dual problem use
that to get your war star that's it so
you have the final discriminant function
okay
now we have we have already defined what
uh support vectors are right s this
support vectors
are
those data points
for which
the corresponding lean multiplier is
strictly positive. We have defined it
already, right? and uh the sum or
the final uh uh parameter will be a sum
over support vectors because the other
terms will anyway go to zero. Okay.
Now observe one another interesting
thing right. So from the
from one of the KKD constraints
or KKD conditions we have something
called complimentary slackness which
actually says that you take the lean
multipliers
multiply it with the constraints
we have this right this is called
complimentary slackness.
Now for those mu stars which are non
zero okay what will happen for
support vectors
what will happen
we have yi * wranspose x i + b equal to
okay what does this mean geometrically
geometrically it means that the data
points that lie on the margin are
support vectors.
I mean now you know why they are called
support vectors right? It's like they
are the ones upon which the margins are
supported.
Okay. So by complimentary slackness what
we have just shown is that support
vectors are the data points that pass
through the margin. So in AR here in the
construction where we are assuming that
the data is linearly separable. Okay.
The maximum margin classifier is the one
that that we obtain by passing the
margins through the farthest data points
or rather the closest data points from
each classes from the decision boundary.
You understood? And if you go back to
our figure.
So we need a data point here.
Yeah. So these are the these are support
vectors. There are three + 1 four
support vector. So the margins will pass
through those data points that are the
closest to the decision boundary. That
is the idea.
Is that all right?
Okay.
Okay. Now we'll have to move on to the
next case. Any questions on this? This
is the most basic formulation of support
vector machines. Okay. If I mean if I
have to just run uh run through the run
through a summary. We are looking at
data that is linearly separable. Okay.
And if the data is linearly separable
and we are looking at linear
discriminant functions. Now if the data
is linearly separable and we are looking
at linear discriminant functions there
are infinite discriminant functions that
are possible amongst all possible uh
discriminant functions. The question
that we are asking is give me the one
that is optimal in the sense of
maximizing what is called as the margin.
Okay. We formulated the problem that way
and it turned out to be an optim
constraint optimization problem on the
parameter space. And to solve that
problem we con we constructed a dual
problem in the lean multiplier space uh
where the dual problem becomes a
quadratic programming problem with
linear constraints that can be solved
using standard QP solvers. Once we get
that, we use those optimal multipliers
and get back to the primal problem and
get the decision boundary, the optimal W
star or the determinant function. And
that happens to be the one that passes
through uh the data points from each
class that are the uh the closest to the
>> decision boundary. Okay. Or the ones and
those points are called the called the
support vectors. Basically there is no
point there is no data point that is
within the margin.
So there can be data points on the
margin. There will not be any data
points between the margins. Okay. Any
questions on this? Yeah.
>> It is necessary to get it from both the
classes because see here if you uh
remember from the previous class yi can
take plus one and minus one. Right? Look
at this equation. If yi takes minus one
then those support vectors correspond to
one class and for y equal to 1 it
corresponds to the other class. That is
how we have defined it. defined the
margin, right? it it's always the case
and okay and remember this in the
maximum margin classifier the optimal
parameters for the decision boundary is
a linear combination of the support
vectors scaled by grand multipliers and
of course there is this class also right
in any maxim max margin classifier the
optimal decision boundary is a linear
combination of the support vectors
scaled by
the multiplier the corresponding
multipliers. Okay. Right. So now we have
to improvise on this. There are two
questions that are to be asked. The
first one is what happens if the data is
not linearly separable.
Okay. Uh the second question is can we
extend this to decision boundaries that
are not linear?
Can we extend this to cases where the
decision boundary happens to be some
some function of data? Right? Now if we
can do it if we can solve for both these
cases then we solve the most general
case right because you know if data need
not be linearly separable and decision
boundary can be any of of of any form it
need not be linear so let's take one
thing at a time so let us look at the
case where the data is not linearly
separable SVM uh we will stop here and
continue in the next lecture
