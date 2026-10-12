---
id: 7y4V0GUoyaw
title: Tutorial 9 : MAP Estimate
url: https://www.youtube.com/watch?v=7y4V0GUoyaw
date: '2026-02-11'
duration: 22:05
model: youtube-captions (en-orig)
transcript: true
---

# Tutorial 9 : MAP Estimate

## Transcript

Hello all, welcome to this tutorial in
which we will be looking at map
estimates.
Now till now in all of our tutorials we
have looked at MLE estimate and then
again an MLE estimate when uh we are
assuming the data is from mixture
densities. So now we will take one
specific example
and see regarding the map estimate and I
assume that all of you remember the idea
of conjugate prior.
So in which
the forms should be identical which
makes sense actually. So we'll be taking
one example of this particular form in
which we'll be assuming the parameter is
from a Gaussian distribution and then
we'll be looking at the prior which is
from a gausian and then we'll be
obtaining the conjugate prior in the
similar form. Okay, in the similar
functional form
okay so now without any further delay
let's proceed.
So we are looking at the
the map estimate.
So now let's uh consider my data I have
is
x
x1 x2 so on till xn
i equals
okay x n okay so this is clear that i is
from to n okay this is the data that I
have now then
I I write that theta
given this d
is by base rule can obtain
given t
divided by this normalizing uh value z
see normally we used to write this as
proportional now we're skipping it so
I'm just for the sake of completeness um
this is the prior and this is the
conjugate prior
what should be the form of this class
conditional uh or this conditional in
the case. Okay. So now
we are uh
now let's consider a case in which we
are only estimating uh the mean. Now we
are assuming that uh it is from a
Gaussian distribution only assuming the
uh estimating the mean. Okay. And then
we are assuming that the variance is
known to us. Okay.
letting a very straightforward and
simple case. Now
consider
estimating
the mean
of
Gaussian density
with
variance.
assumed
no. Okay, this is our uh assumption. So
now then for a given now
uh x now how will be
it look like? Now
2 pi
now exp of
sigma square x - mu
whole square.
Okay. Now I'm assuming that all these
are x's belongs to r. Okay. So now now
now what do we have now? mu is the
only
parameter that we want to estimate.
Now in the case of uh
MLE we know that mu
mle now will be 1 / n
summation i = 1 to n x i. Now this is
how it will be in ml. So we have already
seen this derivation in length. Okay. So
so now now
P of mu given D is by B root D given mu
P of mu
by this normalizing
C. Okay. Now for the conjugate prior we
want
uh this prior and then its conjugate
prior should be of the same functional
form. Okay. So now let's make the note
of this for
for for
conjugate prior.
We want
the mu and then
d
to have the
same
functional form
and uh so
this is for one data point. Now what
will happen when you have uh the whole
uh d with you?
D given mu okay not it's like division
given mu it will be 1 / sigma²
pi
to the n
e xp of - 1 / 2 sigma square
summation i = 1 to n x i - mu² this is
how it turns out to
Okay.
So now
it is evident that this is a function of
mu.
Okay.
So
as a
as a function of mu
this has an
exponential
of a
quadratic
in mu.
Okay.
So now
now what do we want our uh p mu? Now
this is a quadratic exponential
quadratic in mu. Now when I multiply
this
now I should retain the same form same
functional form. Okay, we need P mu such
that when this I multiply with this
specific thing, we need to get the same
functional form as that of P mu. Okay,
now it makes uh very clear that I assume
it to be Gaussian. This is also
Gaussian.
I can combine them. So overall finally
I'll be getting them in the term of the
same functional form. It is pretty much
clear from the setup itself. Okay, so
let's make a note of that.
So we need
P mu
such that
when
when multiplied
by
mu.
we need to
get the
same
form
as of.
Okay.
So now this therefore
the
therefore the conjugate prior
here
is a
normal density.
Okay.
So now
let's assume that P mu
is
a normal distribution with mu0
and
zigma dot squared
and these are the hyperparameter.
Sorry for that.
Now as you had in the beta densities
sorry
in the class you looked at
a conjugate prior.
Now you had this alpha and betas that
are uh
sorry
that are hyperparameters. Now similarly
here also
now we shall have these values are
hyperparameters
where
you not
okay some is
That's only
square
hyperparameters.
Okay. So now again
now we already know that so du
given d is equal to p d given mu
into p mu
divided by z.
Now we can eliminate this z and
substituting for pd given mu and p mu.
Now this will be
is
proportional to exp of - 1 / 2 sigma²
summation i = 1 to n
x i - mu²
- 1 /
2²
mu -
mu² square.
Okay. Now, mu is the current value and
mu not is what you have assumed. Now,
this is the hyperparameter that you have
assumed. Please be very clear with this.
Okay. So, then this I can write it as
this is
proportional or same. Okay. 1 / of a
I can consider this whole thing that is
there this
I have taken this uh half minus half
outside and then I can think this whole
term as a so I should not use
proportional here I should write equal
okay now this is proportional to this
and this is equal to this okay
now this A
is same as 1 / sigma²
summation i = 1 to n
x i² +
mu²
to 1 /²
+
n into
zigma²
-
2 mu
to summation i = 1 to n
x i -
sigma² +
mu / sigma²
+
okay this is what
we get.
Okay. So now now
suppose suppose
let's call this as
equation okay a have already been used
okay let's call this as one okay this is
equation one suppose
we sorry that change suppose Suppose
we have
P of mu given D that is also Gaussian
distribution with some mean and then
some variance. now is normal with
mu n and
I can write the form of this and then I
I can equate the exponential part and
then obtain the values for the
the mu and sigma n correct okay that is
what I'm trying to do now
so now because of which
p of mu given d is proportional to exp
of -/
mu - mu1 divided by sigma n²
okay so now this is same as exp
minus half
Mu² divided by
zigma n² +
mu n²
divided by
zigma n²
-
2 mu
into mu n divided by
n².
Now consider this as equation two.
Okay. So now let's take this as two.
When I mean two only the one in the in
the uh braces. Now you have a mu square
here and then you have a mu square here.
Now therefore 1 / this zigma n square
should be same as this. And you have 2
mu here. So muid zigma n square should
be this term. Okay. This can easily be
evaluated.
Okay. And then if you substitute them
and you should get this that you can uh
take it as a uh what do you call a check
whether things are summing up together.
Okay. So now let's do that. Okay. Now
comparing one and two. Now
comparing one and two. When I mean two
only in the brackets what is there? So
we get
sigma n² as 1 /
sigma squar +
n + sigma square. Therefore this will be
zigma square.
Oh sorry.
Oh sorry this is not
this is 1 /
sigma n² okay will be this.
Therefore, which implies uh
zigma n² is
zigma square
into zigma²
divided by
sigma square + n into zigma square.
Okay, this is how you obtain this. Okay.
Now similarly now similarly if we do it
for
mu n
will be 1 /
so mu1 divided by zigma n²
i =
1 to n x i +
mu divided Z
sigma KN square.
Okay. So now if you push the zigma n
z s z s z s z s z s z s z s z s z s z
sigma n² divided by²
and then you have i = 1 to n x i +
sigma n² /²
into mu. Now does this look familiar?
There is one term missing. Okay, that is
1 / n. Now this is similar to our uh MLE
estimate for the mu that we have. Now
this is just off by some values
uh of by some scale not off by some
values off by some scale. So this is
linear combination of my MLE estimate
and then my assumption.
So my map estimate which is there this
is mu n is this. Now I get a whole
distribution and then since uh it's a
gausian distribution the mean mode
everything will be same. Therefore I'll
be using the mode which is maximum a
posterior e. So which is same as the
mean which we have computed. Now what
happens is now this this actually means
that the mu n that we have computed
the map estimate mu n is
a convex combination
a convex combination of the MLE estimate
and
mu not mle estimate for mu and mu not
Okay.
So now
now for
large n
the mu n will be similar for mu
ml.
Okay.
So this is the known result then we
looked at here also which makes sense.
Okay. As n becomes very large
now
as
n becomes
very large
the basin estimate.
is in
estimate
is same as MLE
is
same as
MLE and please note that since we are
dealing with Gaussian the mode is uh
same as the mean okay so now let's make
some just notice since
since the
distribution is Gaussian
since the distribution is
Gaussian.
Okay. So
mode
as well as
mean
is mu n which is a linear combination of
my mld and then the assumption that we
have.
Okay.
So uh so in this tutorial I just wanted
to bring out the point that how do we
look at the map estimate and then obtain
the conjugate prior in the cases of
Gaussian densities. I hope it was nice
and interesting and thank you all. We'll
meet in the next tutorials. Thank you.
Bye.
