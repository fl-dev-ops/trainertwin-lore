---
id: j7jbpicYdik
title: Lec 18 MLE for Generalized Discrete Random Variable
url: https://www.youtube.com/watch?v=j7jbpicYdik
date: '2026-02-03'
duration: 25:47
model: youtube-captions (en-orig)
transcript: true
---

# Lec 18 MLE for Generalized Discrete Random Variable

## Transcript

Welcome back to the lecture and let us
look at the other example too.
And by the way uh one can get an ML
estimate for the for any parameter of
any distribution. Now for instance let's
say that we assume we want an ML
estimate for the variance of a gshian
distribution. We can do the same thing.
So now the derivative will become with
respect to matrices
>> same algebra. Yeah coariance matrix or
you can let's say that you assume your
underlying density to be let's say an
exponential distribution then it's a
single parameter model you have to you
can estimate get an ML estimate for that
as well right so this is a technique
which is general enough all you have to
do is compute the log likelihood take
the derivative of that with respect to
the parameter under consideration and
then get the estimate that's it okay
I'll give you another example uh for the
case of a general discrete random
variable and then we will move
uh discrete random variable or a general
discrete random variable.
Okay, the previous case what can be a
practical
example of the previous case? Practical
example of previous case is let's go
back to that same X-ray example, right?
You can model the class conditional
density actually as a goshian density in
some 500 dimensions. If your image is of
200 by 200 then you're talking about
estimating the mean of a gshian density
in four
no 200 into 200 is 4 followed by four
zeros which is 40,000 dimensional space
correct that is how you can look into it
and that's continuous. the distribution
of pixels of an image is gausian. You
have made an assumption that it's
gaussian uh in that particular uh space
and you estimate the underlying uh
density function. Does it make sense?
Right. So now let's take the example of
a general discrete random variable where
uh d is
v_sub_1 v_sub_2 we have v n this is
sampled i from v pv
where every vi so please observe this
this vi can take
a1 a2 up to am
with
probabilities
P P1 P2 up to P1
P2 up to PM. So this is the general case
of any discrete random variable. See
every discrete random variable can be
modeled like this. So what am I saying?
Let's say that you have
the case of data where you are dealing
with a discrete random variable that can
take y discrete values with
probabilities p1 to pm. What is an
example? Coin toss. Coin toss can take
it's a boli random variable right take
one of two values with probabilities p
and 1 minus p. The other example is role
of a die. It can take value six separate
values with probabilities P1 to P6 and
so on.
You see right? So any discrete random
variable that can take one out of M
values with probabilities P1 through PM
can be modeled like this. Now what are
the parameters that we estimate here?
There are P1. This this is the parame
this is our theta vector.
There are M thetas that we want to
estimate here.
I count from one.
>> Oh yeah yeah yeah that's yeah it's not
yeah that's correct m minus one because
it's a good point uh it will come out in
a while. So when you solve this
optimization problem we will we will we
will look into this because you cannot
solve this problem optimization problem
in an unconstrained way.
Why? Because of the precise reason you
said they sum to one.
Good good point. Yeah, good observation.
Okay, is that clear? So this can be this
technique can be used to model any
discrete density, right? Any discrete
random variable. Okay, so let us look at
how to do this.
Now what do we have to do? we'll have to
find okay so let's first say that the
parameters
theta is this particular set
how do we start the ML estimation we
start by making a distribution or
assumption on the underlying density P
theta for a discrete random variable
what P theta do you assume
come again
>> why binomial see binomial is not this is
not binomial. Why is this not not
binomial? Binomial is multiple
independent trials of a Bernoli random
variable is binomial. This is not a
Bernoli random variable. This is a
random variable that can take M values.
>> Yeah, you some people it's not even
multinnomial. People call it multioly
just extension of Bernoli is what is
called as multioly. It's just general
discrete random variable. So we'll have
to write the density function for this.
How do we write the density function for
this?
See a Bernoli random variable is a
general I mean is a special case of this
okay but if you extend the idea of
Bernoli random variable to m outcomes or
m possible uh discrete values how do you
write the density function is the
question it's non-trivial so we need
this uh this idea called one hot
representation
okay let us look at that so let's do
what is to
express the density function of uh this
For this random variable
we need
one hot representation.
So what will be mass function? It will
be mass function. Yeah.
mass function can also be called a
density function not the other way
around. Okay. Anyway, so it is to the
mass function for this random variable
we need to we need what is called as a
one hot representation. What is that?
Now for each okay let me write that. So
one hot representation
this is just for the algebraic
convenience. Okay. So what we write is
uh
so for each
vi
define
an auxiliary random variable
zi I as follows.
ZI
is equal to
CI1,
ZI2
up to Z I M
where all ZIS
E,
they're all either zero or one. And
uh z i j
is equal to 1
for
for j such that
v i is equal to a j
zero otherwise
I mean it's pretty simple written in a
complicated form.
So let me just explain what it is you
know then we'll go to the math.
See the data that we have what is the
kind of data that we have here the data
is v_sub1 v_sub_2 up to vn right uh if
if it if it's a discrete random variable
that we are considering all of the vi
okay uh we'll take one of these a values
isn't it suppose we are looking at
rolling of a die then the data that we
will have will look like 3 2 4 1 6 7 and
not seven only six faces 3 2 4 1
whatever right you understand So every
discrete random var every realization of
this discrete random variable can belong
to one of the m possible values that we
have make sense and that's the data now
what I'm doing is every to every data
point which is a single value that the
discrete random variable take I'm
actually constructing an m dimensional
01 vector
what is m here m is the number of
discrete values that the random variable
can
How am I constructing that uh that
particular vector is that I this vector
will contain zero in all places.
Okay, except for in that position which
the vi random variable realized into.
Does it make sense? So let me give you
an example. So example is suppose d was
like this which is we are looking at a
role of a die. We have 2 3 4 1 6 and so
on. Right? And here my uh vi can take
values 1 2 3 4 5 and six.
Right? This is how the data would look
like. Correct? Now for every vi I have a
zi right? So Zi, so Z1 we'll define Z1
to be 0 1 0 0 0
1 2 3 4 5 6
correct and Z2 is
0 0 1 0 0 and so on. You got it right?
This is called the one hot
representation.
Does it make sense? See I just transform
my data uh which had a single value like
this 2 3 4 5 like that from from there
to a six or m dimensional one hot
vector. This is called one hot because
of obvious reasons only one of the
positions is hot the other are cold.
Right? That's why it's called the one
hot representation. Do you get it? See
now look at the math. So for every vi we
define an auxiliary random variable zi
which will which is defined as this zi
is equal to z i 1 to z i m all z will
take value between one of the two values
zero and one such that zi ji is one for
only that j for which this vi is aj and
zero otherwise
make sense had I only written on the
abstract form and not given an example
it would have been difficult to
understand is it
okay that's a very subjective opinion
right so anyway you got it so now what
happens is my data so new data
will be d equal to
uh we have z1 z2 up to z
right so each zi
is in is is a discrete vector
of length length m.
So if I you get this notation right, I'm
saying that it's a discrete vector which
will only take values 0 and one and
there are m of them.
Okay, this is the new data that we deal
with. I mean what's the fun of rewriting
this data this way? You remember we did
it because we had to write the
underlying density mass function. Okay.
Now can will this representation makes
make the mass function uh uh writable?
Turns out it can be written. What is
now? P theta of
of zi
is equal to
p1 *
okay actually write it as p theta of vi
because that's what we need. P1 * Z I1
into P2 * uh Z I2
into so this is all product into
P M *
Z I
M
why is this the case
see what are these Zigs
They are the elements of capital ZI
corresponding to VI. Correct? And which
one of this will be one for VI?
It will be that particular uh entry
which the VI correspond to. Right? Now
suppose vi has taken uh the fourth value
then p1 to the^ of 0 p2 to the^ of 0 p3
to the^ of 0 p4 to the power of 1 and so
what will what will remain only p4 will
remain so the density
let's write it this way no so vi is
equal to the j value or what what what
is the value that we said it was aj no
hold on p theta
such that vi is equal to a j is this.
Now zi for this particular thing will
look like
it's all zeros and one in one position
and zero everywhere. Correct? It's an
mlength vector and this will be the j
position.
Get it? So therefore P theta of VI equal
to AJ will be
PJ and that's what we need.
Did you get it right? So without this
you cannot write the underlying mass
function this way. So you want that
auxiliary random variable to be defined.
You understand why this was defined now?
So P theta
of V I is given by the product
of
J = 1 through M
P
J to the power of
C I J
does it make sense now
that's it we wanted to write our density
function this way otherwise you cannot
differentiate it and that's why we
defined that auxilary random variable
that's it yeah so p theta of vi equal to
aj what is this equal to by the way this
equal to pj
if vi takes the value a j then this is
equal to pj because that's how we have
defined it yeah
so if I now say that pj does not
correspond to poor joke that itself
becomes a poor joke.
That's the irony. Yeah.
Okay. Are you are you okay now? So what
we should do now? This is our density
function. Now we have to estimate the
parameters. And remember that our theta
the parameter
vector that we are trying to estimate is
P1, P3, P2 up to
P M. No, it takes M values,
right? So how do we do this? So we get
our theta star to be the one that
maximizes the log likelihood which is
equal to r max
theta you have
there's also this 1 by n
log of what is p theta p theta is the
product correct
the rest is algebra
So we have r max
1 / n
i is 1 to n and there is
use the law of logarithms. Okay,
this is what it's going to be. Now we
have to differentiate this, right? We
have to differentiate this with respect
to see this does not look like a
function of theta at all. Remember that
theta is nothing but P1 to PJ right when
I otherwise if you differentiate this
thing with respect to theta when there
is no theta it will go to zero right so
this PJ is what our theta is remember
that so we'll have to differentiate this
can we differentiate this input to zero
so okay so let me write it explicitly
you differentiate this with respect to
PJ now tell me what PJ maximizes this
see if you if we have to look at this
function okay and zi can only take
values 1 and 0 okay which is non-
negative and PJ because they are
probabilities they are also between 0
and one now there is no negative number
here and the function that we are
considering is monotonic which is log so
if you if you were to maximize this
function with respect to PJ what value
of PJ would
no I have not said that PJ is bounded
now yet
if if I don't bound PJ and then solve
this optimization problem because this
is unbounded the value that maximizes
this function is PJ that takes infinite
value. We don't want that to happen
because we know that PJ is a
probability. So what should we do? We
should add constraints to the
optimization problem. Right? So adding
constraints to the above optimization
problem. Put constraints to the
optimization problem. What will happen?
What constraint should we add? We'll
have to say that ensure that my PJs are
bounded between 0 and one. Is this
enough? Not. We'll have to say that
add if you add all PJs over all possible
values, it should add to one. Okay.
Now, how do you solve a constraint
optimization problem?
So, the new problem is L a new objective
function.
So arg max
max maxima is l theta
subject to
it's bounded and uh it adds to one.
So how do we solve a constraint
optimization problem? Construct the
lrangian and make it an unconstrained
problem and differentiate it. I mean uh
yeah differentiate the lrangian. So
write down the lrangian which is um
what was our objective function? So it
was
1 / n
i 1 through n log
was another summation. Yeah. Summation
over n and summation over j.
Summation over i and j. Z I J log
P J plus
lambda *
1 through M P J -1
plus
alpha *
PJ
-1 plus
some other beta *
minus PJ Okay, why did I write all these
three constraints, right? One is that
the sum has to be one which is the first
leanian. The other has to be that yeah,
it has to be less than one. The other is
that it should be greater than zero.
That's it. Wrote three legions here. Now
you differentiate this entire thing with
respect to read PJ and put it to zero.
I'll completely skip the algebra. Will
you please take it as an exercise and do
it? Please complete the algebra. So how
do you solve a constraint optimization
problem?
differentiate this with respect to uh
the objective function first and then
with respect to lrangians and find out
what the lrangians are and take the
optimal lrangians and put it back to the
uh the objective function and get the
final objective final optimizer all of
you know this right so you've done a
course on optimization this is a simple
101 right optimization 101 I'll skip the
algebra so finally
after solving even today's ML reading
happens like this. So the real juice
lies in formulating the problem.
Optimization is done using computers.
You throw it to GPUs, it'll solve
gradient descent for you. But
constructing the optim in fact
engineering actually lies in translating
the real world problem into a math
problem,
right? And formulating it as a problem
that can be designated and solved
through computers.
Now a new type of engineering would will
be will be emerging.
See I was somebody was asking me the
other day that uh that is that there is
AI in know GPS and all that that can
answer any question that you ask. So why
do you need human beings right? My
answer to that is yeah I mean or why do
you need teachers or anybody?
GPT answers questions but who will tell
you what questions to ask?
You can actually relate it to uh the the
est calculators. See calculators can
solve math problems
but somebody has to give it give it an
instruction as to what is an important
problem to solve.
I think that is where the actual value
lies from now on. Understanding what
problem what problem solving which
problem creates value in society is
where the actual uh the uh uh skill
lies.
Once you do that there are powerful
machines that you can designate your
work on to which would solve problems
for you. But the question is what
problem is to be solved?
Okay. So now we have now that we have
formulated the problem it can be very
easily solved using the standard
algebra. If you do that, what do you
expect PJ to be? The estimate of PJ to
be the ML estimate of PJ to be
to our surprise, it'll be Yeah, I'm just
trying which notation did I use for
this? It's actually this. It'll be the
the number of times
um AJ has appeared has occurred in D
divided by N. So what what in my
notation what is that? It is zi
jum
>> summation over
this is summation over
1 through n we have
>> z i j
is this correct uh
divided by n
this is what it is
please do this huh please do the algebra
uh it it will come out that way right I
mean you can see this actually here
there is zigj here you differentiate and
put it to zero it will come that way
right so that's it so now we knew this
all the time
that if you are given a discrete random
variable and uh you need to tell me what
is the probability that this this
discrete random variable takes a
particular value j then what do we do we
just see how many times this j has
appeared and divide that by n that's the
maximum likelihood estimate you're what
you're actually doing is assuming that
the underlying density has this form and
writing down the k divergence and
minimizing the k diver And this is the
estimate that you get.
Okay. By the way, one question can come
up here. This is still an estimate,
right? How do we know whether this
estimate is close to the the true
parameter value? So, this question is
similar to the question of how close is
the minimizer of the empirical risk to
the minimizer of true risk. And there
are uh there are there are metrics that
would quantify the goodness of uh uh the
the estimators.
Uh these are called the concentration
inequalities and other bounds. You know,
which is beyond the scope of this
particular subject. There are there are
bounds that would tell you with what
confidence can I say that this
particular estimator is close to the
true value.
Just be aware of it. Okay. So I won't go
into deep depth of it. This is the ML
estimator for this particular discrete
random variable case. Okay. Uh we will
stop here and continue in the next
lecture.
