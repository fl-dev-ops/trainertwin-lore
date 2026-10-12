---
id: XA3UiD8zEF8
title: Tutorial 7A : MLE for Gaussian Distribution
url: https://www.youtube.com/watch?v=XA3UiD8zEF8
date: '2026-02-03'
duration: 40:16
model: youtube-captions (en-orig)
transcript: true
---

# Tutorial 7A : MLE for Gaussian Distribution

## Transcript

Hello all, welcome to this tutorials in
which we will be looking at obtaining
the analytical situation anal analytical
solutions for some of the MLE estimates
in the class. what has uh so sir has
done uh couple of examples and then uh
the steps now which are there were uh
left as an exercise for students in this
tutorial what I will do is I'll fit in
those [clears throat] steps and then
give you a full-fledged uh detailed
solution
one important resource that you have to
keep in mind is that matrix cookbook
that uh sir has uh set in the uh
uh class. Okay. So now without any
further delay, let's uh start with the
discussion
examples of
MLE
estimation.
There I'll take the
example one. Example
one is
onedimensional
Gaussian case. Okay. And this was not uh
particularly done in the class. We
directly take the the multi-dimensional
gausian. I will come to that just to
give you an intuitive idea how does the
solution look like. Okay. Now we will
explicitly take this.
Okay. So now
in this case the class conditional x
given y is equal to i now will be a
square root of 2 pi
xp of minus x - muy
all² / 2 sigma²
Okay, it's one-dimensional x comma mu y
comma
z y all of them belongs to r. Okay.
So a very straightforward and then a
simple case. So now uh this is for one
example. Now the first thing is you have
to find the log likelihood and then you
have to find the so the idea is same.
Now you have uh the uh the form of the
density and then what do you do? You
take the log likelihood over uh you
consider all the examples you take the
log likelihood. So and then uh take the
partial derivative with respect to the
parameters equate it to zero and obtain
the values. Okay. So this is a standard
recipe that we will be going ahead in
this uh tutorial. Okay. So now
consider
we have
n examples
and
obtaining
the
log likelihood.
Now this will be
summation
j = 1 to n ln of p of x given for any
given uh class I'm just considering
xj
this will turn out to be summation j = 1
to n minus
ln of
sigma
i
- 0.5
ln of 2 pi minus xj
minus mui
divide by 2
s zigma
a² there is a square here
okay
so now if you take the summation inside
this - n
log i minus
0.5 n
ln of 2 pi minus
summation j = 1 to n xj minus
mui²
/ 2 zigma².
Okay. So now this is the log likelihood.
Now you have to
maximize this log likelihood. So uh now
what is that uh you are supposed to do?
Now you have to take the partial
derivative with respect to the parameter
and equate it to zero. Okay. So how do
we do it?
to
to maximize the
log likelihood
we
equate
we equate the
partial
derivative
to zero partial d with respect to the
parameters. Okay. So now that
[clears throat] means that you take I
just presented
I you take the partial derivative with
respect to this. So in so how to take
this this is a constant with respect to
sigma. So no need to worry. So now this
will come out and this whole thing can
be considered as a constant. So now
derivative with respect to
the sigma i. Now it will be 1 / uh
uh sigma i. So this is uh lambda i². Now
it will be 1 / lambda i cube. Okay. So
you take care of all of them. So and
then so it will be minus n
divided by zigma i plus
1 /
zigma i cq
summation j = 1 to n xj minus mu i²
This you equate it to zero. Now
when you do so now how it will be so now
this will be
I²
equals sigma I²
this is
the star of this the optimal value. Okay
now see sigma i² is what you have you
you're evaluating. Okay. Now this is
1 / uh n
summation
j = 1 to n xj
minus
mui square.
So now now this is one and then you take
the partial derivative with respect to
mui.
Now when you do so uh what will happen
this is independent of mu this is
independent of mu this will go off. So
now you have to take it with respect to
mui. Now therefore uh what will happen
now this is a function of mui. So
uh it will be 2 * of this and then you
take this this is minus mui. Okay, I'll
not go into the taking how do you take
the derivative. So all of you should be
comfortable with that. So that will be
1 /
sigma i²
summation
j = 1 to n
xj
minus mu.
Okay, this you equate it to zero. So
when you do so now
equals 1 / n summation j = 1 to n
xj.
Okay. Now this is the these are the two
parameters that we can easily obtain.
Okay. So now uh this is nothing but the
the sample average. Now what you're
doing you take the value and then uh
you subtract the mean and then you
square it. So now when we go into the
multi-dimensional case now each x i will
be in rd and then the covariance matrix
that is there will be in r d cross d. So
now this will turn out to be an outer
product right in that case.
Okay. Now we have to see the similarity
now.
Okay. Now this will turn out to be the
out product. Now giving us the matrix.
Okay. So
so now let's take the the one that we
actually want to look at. So so this
example I explicitly [clears throat] uh
took it. So that we should be able to
see the relationship between the the
uni- dimensional Gaussian case and then
the multi-dimensional Gaussian case to
understand that specific uh relation we
took it up. Okay. So now
now consider the
consider the
the multi-dimensional
density.
Okay. So
this case now how will be my
density look like for a given x
that is 1 /
square root of 2 pi
to the^ of determinant
of the
covariance matrix X
into
exp of -/
X - mu
mention it like I mu I
transpose
inverse.
Okay.
So now look at the
the matching the dimension matching. So
this is a matrix
a square. So otherwise inverse itself is
not defined. Okay. So uh this is a
matrix into a vector. Okay. So you get a
vector out of this.
A vector into a vector of the same size.
This is uh xrpose x which is nothing but
a scalar.
So and then exp of a scalar this will
give you a scalar and this is a scalar.
Finally we want this to be a scalar
right. Okay. Now now whenever we write
any matrix equations always the initial
sanity check [clears throat] has to be
know whether the the dimensions are
matching. Okay that should be the first
sanity check whenever we are dealing
with matrices. Okay. Now here to bring
it up X comma muy
belongs to RD and then the zigma which
is there is
a D cross D matrix which is the
the covariance matrix.
Okay. So now you have n samples. Now
what do you do?
You take the log likelihood of those en
samples. again the same uh standard
recipe.
Okay.
No
considering the
n samples
and
taking
log likelihood
what it will be now this is j = 1 to n
ln of
given x. So now if you together this is
summation
j = 1 to n
ln of
1 /
2 pi to the^ of determinant of the
covariance the square root of that
into exp of -/
xj minus mui
transpose
I inverse see you can uh remove this if
if this I is too much of overloading of
notations for you can remove this this
is for any given class I because we are
assuming that class conditional
is a Gaussian so I'm representing that
it is for that specific class okay I can
easily uh remove that also and then it
holds comfortable just for
Keeping that in mind I'm writing it mui
sigma i which is there for a specific
which class are you considering okay so
now if it is too much of notation let's
let's remove that let's keeping that in
mind so we will just go ahead with that
so now this will be
j = 1 to n
-/
ln of
e to ^ of d
minus half
xj
- mu whole transpose
inverse
xj - mu.
Now this is so now you can take the
summation inside
but now now
the question is
you have a scalar
in this case. Okay this whole thing is a
scalar. Now you have to take the partial
derivative with respect to mu which is a
vector and then zigma which is even a
matrix
and this is a trace is also uh a
determinant is also involved in this.
Okay. Now how do you take care of these
things? Okay.
So that will be our that that is where
uh actually the identities of uh the
matrix cooks book cookbook actually
comes into picture.
Now,
now
need to
now now need to take the partial
derivative
with respect to parameters
and equating them to zero.
Okay, that is what we are supposed to do
now.
Okay, now taking it for mu is quite
simple actually.
Okay, now partial derivative respect to
mu. Now if you take this now this whole
thing is independent of uh mu. So no
issue. So now
so you have uh this form now we know how
to take this now this is
inverse into x - mu that is what it will
be so it is it's quite simple for us to
get now this is
okay so now please remember I'm using
summation also and then sigma also so
you should not get it confused
inverse
minus mu you equate it to zero. Okay. So
now what you can do now this is
independent of j you can take it outside
and then this is uh the inverse so you
can multiply with this and then you get
a i over there. Okay. So you can take
care of all of them comfortably.
Okay. So because of which now finally
the mu star now which is there will be
1 / n. Okay. See finally you will get
this out
and then you take it summation inside.
Okay you get this n mu you take this n
mu outside here. This is I into some
summation of vectors. So summation of
vectors is a vector. So a matrix into a
vector identity matrix into a vector y.
I'll get an identity because you
multiply with by sigma. So you will get
a vector. Okay. The same vector holds.
So now therefore it finally boils down
to
xj.
Okay. Now this is a straightforward
simple uh thing for uh
taking care of mu. It's quite simple to
do it for mu. Now the actual uh what do
you call issue lies with how do you take
care of the the coarience matrix now.
Okay.
So now
we need to
take the
we need to take the derivative
with respect to
sigma.
So now our log likelihood is our
log
likelihood
has been uh
reduced to
this is
summation
j = 1 to n
-/
into ln of 2i ^ of d
minus half
xj - mu
transpose
inverse
xj minus mu. So now you take the
summation inside
uh
okay now
because of which it will be
minus n /x2
into d
log 2 pi
okay
now
and then this 2 minus +
-
n /x 2
into
this.
Okay. and then minus
summation
j = 1 to n/
xj
minus murpose
inverse.
This is what it turns out to be. Okay.
So now it is uh too much of uh things.
So we will reduce the uh notations. Now
let's take that I'll represent this
inverse of the coarience matrix as this
little J and then
I'll represent this ZJ
is XJ minus mu.
Okay.
So now with this I will mine
new
n d
log 2 pi
minus
n / 2
the determinant of this minus half
the summation J = 1 to N
ZJ transpose.
Okay, there's no change in terms of the
the notations. Okay,
so now
think there is some mistake that I did.
Just one minute.
Okay, no problem. Yeah, I myself got a
bit. Okay, so now
now what is that we need now? Now we
need
we need
derivatives
of the form.
You take the
derivative with respect to a.
this we need and then
derivative with respect to a matrix
ln of its
these are the two things that we want to
get now this is my log likelihood I'll
take the partial derivative with respect
to my
matrix that is there okay and then
equate it to zero for that I should be
knowing what are the partial derivatives
of this Okay.
So now here comes some of the important
uh identities of the
matrix.
Okay. I'll not be going ahead and
proving these identities.
Okay. I'll be just using them.
Now some useful matrix identities.
some useful
matrix
identities. Now all of us knows about
the trace trace of AB equals
trace of
BA. Okay. Now, now assuming that the ABA
BA multiplications are multrix
multiplications are possible. Okay. Now
the dimensions I'm taking into
consideration. Okay. So now then
trace of
A B C equals
trace of
C A B
equals
trace of B C A. Okay. These are all
standard
uh matrix identities.
So now if I take the derivative of
this trace
of A transpose
B it will be D.
Okay.
So now now now
we all know that trace is a scalar
z transpose
a c can be written as the
trace of cranspose
a z correct.
Now this I can write it as trace of
z
transpose
into a.
Now now we know that this is one this
is.
Now this is same as
trace of a into zrppose.
Correct? Now what is the derivative of
this? Uh derivative of a transpose b.
Okay.
If you have this okay and one more thing
okay
this is derivative of
a if you have trace of a
which is b transpose okay one more
identity that is needed for us
so now now putting all of this together
therefore
the partial derivative with respect to
the matrix A
is same as taking the partial derivative
with respect to
trace of a
zz transpose
which is z
transpose
whole transpose.
This is zrpose.
This is the outer product of uh the
vectors z.
Okay. So now that means that now going
back to this this is done.
I can individually take care of this.
This is done. Now this will give me a
uh zz transpose or zj z transpose. This
is done. This part is done now for me.
So now I should take the
uh gradient with respect to this. Okay,
that is what is pending for us now.
Okay, now let's do that.
Now we need the other derivative.
Now
we need
other uh
derivative
log of
determinant of a.
Now
now let's consider a scalar x. Okay.
Okay. you know x we have always used for
something. Okay. So now if I have a
reason
identity which
like for example let's have some
beta
belongs to r it's a scalar.
Now if I have
beta of
l of
this is there now then it is
trace of
a inverse.
Okay there is this identity. Now using
this identity now we will go ahead. Now
a is a matrix. Uh each element a iig j
which is there can be thought of as a
scalar. Now because of which I can write
that I can take the partial derivative
with respect to this aig j
this is
trace of
a inverse
a correct. So now the overall question
is now I have taken with respect to one
element of this matrix. So
the remaining uh uh elements I have to
take it into consideration. Now what do
you mean by this? Now you take the uh
gradient. Now what will happen is in
that position aig it will be one. In
every other position it will be zero.
Okay. whenever I take this gradient.
Now what will happen is
so now
this
partial derivative in this case
is a
matrix with
one
in
in position.
I command
and
zeros
elsewhere.
Okay. Now therefore
now what will happen?
This is a matrix.
Uh now there the dimension is taken care
by the construction itself. Okay. So now
since this is a matrix multiplication I
can know what is its element.
Okay I can actually know it comfortably.
So now
a inverse
J
a
I can know what is the
element at KL location.
uh
it is
summation with respect to s
inverse
ks.
Now I'm assuming that you're quite
comfortable with uh representing a
matrix uh multiplication using these
formulas. Okay.
Okay.
Now
here it's a
the element in the a inverse matrix. Now
this is the element in the
uh what do you call the partial
derivative matrix. Okay. There's no such
term but you can think of it. Okay. Now
this
will be
zero
if L is not equal to J
A KI inverse if
L is equal to J by
construction now I am able to obtain the
element
Now I will be able to get the trace very
comfortably.
Okay. Now getting the trace is not at
all a difficult thing.
So now
now trace of a inverse
I J.
Now
this will be
inverse
J
this
JJ.
Now this is nothing but
a J inverse.
Okay. Now I'm able to get it for one
element.
Okay. Now if you are able to get it for
one element
you have taken with respect to one
element.
So now you have to take the respect with
respect to the whole matrix. Now what it
will be see now see the important thing
to observe is now aig now you have
actually taken the the inverse
and then the so you have taken the
inverse of the transpose okay now you
have taken the transposed element so for
a j now you are looking at gi element
and the inverse of this
okay so now putting all of this together
okay uh
this is for one. Now if you put all of
them
together now therefore it will be
overall thing this for one element like
that you take it for everything. This is
a inverse
transpose
inverse of the transposed element.
Now you got the second one. Now from
here you just put them together and then
you get it. Now
now
putting
these
together.
Okay, you put all of these together
and then what you do the next step is
take the
partial derivative.
Take the partial derivative and
equate to zero.
Take the partial derivative and equate
it to zero. That will be n /x2
inverse
is half
summation j is equal to 1 to nj
jrpose
zero. So now what will be the value? Now
we know that this is
tilda inverse is
the coarience matrix that we had. This
is 1 / n summation j = 1 to n xj
minus mu
into x i - mu transpose. This is the
outer product. Now when you took the
one-dimensional case it was the square
of the difference
between the
considered data point and then the mean
of it.
Okay. Now if you go back to the
one-dimensional case but now in the
multi-dimensional case it has
transformed
into a outer product. Now between the
data vector and then the mean vector.
Okay. Now this is the overall uh uh
derivation. So in the next part of this
same tutorial. Now we will be looking
into the generalized discrete random
variable version that uh was discussed
in the class and then we will look into
the constraint optimization how to get
the parameters in that case. Thank you.
