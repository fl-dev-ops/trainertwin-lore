---
id: ysjGmQW4HOo
title: Tutorial 10 Part B : Numerical Example on MLE and MAP Estimate
url: https://www.youtube.com/watch?v=ysjGmQW4HOo
date: '2026-02-18'
duration: 30:58
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Tutorial 10 Part B : Numerical Example on MLE and MAP Estimate

## Transcript

speaker_1: Hello all welcome to the second part of
this tutorial in which we will be
solving question on MLE and map
estimate In the previous uh uh part of
this tutorial we looked at the ordinary
list square solutions derivation to
obtain the optimal values of the
parameter and then we looked at the uh
we took a two class problem and then uh
we obtained the base classifier
for that specific problem Okay So uh
without uh any further delay lets uh
delve into the current problem that we
have So
in this problem
suppose x is uniformly distributed uh uh
between 0 theta Now that means that
the x that we have is a uniform
value between 0 theta
and then theta with
theta greater than zero and it is
unknown
Okay So then once we know the
density of this case now 1 by theta for
uh
x
between
0 and theta and 0
otherwise Okay This is the density for
x Okay So now
suppose we have three iid samples
This is your data Now the data that you
have is
x1 is 1
x is 0 point 5
xray is 0
22
Okay Now what is the value of the
likelihood function
L theta given D uh
uh l theta now with the given d as the
data points for theta is equal to 10
what will be the value for theta is
equal to 1 point 9 what will be the value okay
that is what we want to find first we
want to find the likelihood
okay
so now
value of the likelihood function
Okay Now L theta
is equal to
the whole data
which you have x1 x2 x3 Now since all
of them are
independent Now I can take the product
of this I equals 1 to 3 PX of
X equals
the value X I Now please remember there
is lot of abuse of notations that are
happening Now this is nothing but the
product of I equals 1 to 3 1 by theta to the
cube There are three values So and
then and then indicator
for
0 less than x i less than or equal to
theta
Now what is this uh indicator uh random
variable See indicator random variable
is will take the value one when whatever
uh function if it is uh uh indicating
that function it will be one else it
will be zero Okay So in this case that
the this indicator random variable will
take the value one if this uh x i is
in between these two values Okay And
this is a product of three indicator
random variables So now whenever a
product of three indicator random
variable will take one when all of them
are in bound Okay So now lets write
that
the product of this
indicator
is one
only when
all samples
lies in the range
0 comma theta All the samples x1 x2
x3 lies in the range Now that is what
do you mean by that 0 less than x1 less
than or equal to theta
x2 is also in between 0 and theta
x3 is also in between 0 and theta That
means that theta is greater than or
equal to max of
x1 x2
x3 Okay
now this makes total sense Okay if
this has to satisfy now the theta value
should be the max greater than the
maximum of this Okay now what does it
mean Then the product of all these
indicator
random variable that we have
for
this
is one when theta is greater than 2 point 2
to
zero otherwise
Now that means that
the the value of the likelihood function
will be 1 by theta to the of 3 if theta
is greater than 2 point 2
0 otherwise
Okay Now this is the value for the
likelihood function Now he is asking
that what will be the value at two given
values of theta It is very easy to look
into We already know now
Now L of theta equals 10 will be 1 by 10q
L of theta
 equals 1 point 9 is equal to 0 Y now one of the
value is 2 point 2 So therefore this will be
zero Now this will have some meaning
value
Okay
till here it makes sense Now consider
the general case now where we represent
three ID X1 X2 X3 Now plot the
likelihood function Now consider the
case we have N ID
uh samples which is there Okay So now
lets take the NID sample case Ill
leave the plotting it to you Okay very
straightforward idea from now Now
in the
in the general case of
n samples
its its the same Now l theta equals
the product of all of them So it will
be I equals 1 to n
1 by theta
to the power of n
into
the indicator
is equal to x i
theta
Now this is
1 by theta of n into product of uh
these indicator random variables
Okay So now lets say that m that is
there is equal to max of
these x1 x2
so on till xn okay it is the max of them
now then its
then the product of these uh
indicators
now this will
1 by theta to of n if theta is greater
than m and
now x i also should be greater than or
equal to zero right okay
zero
otherwise
then
this now your l theta will be theta of
minus n where theta is greater than m
and then x i is greater than or equal to
zero
for all i
otherwise Now this will be the
likelihood function
Okay
So now the next thing is now once you
have the likelihood for the n samples
now what is the mla estimate of this
theta
So now you have the likelihood Now
maximum likelihood Now what do you do
So now you want to get the MLE
Now
to get the MLE
Now
MLE takes the the maximizer
theta
should
satisfy
Theta should be greater than m and you
should remember that this theta now what
are the values that it can take It can
take values from m to infinity
Okay Now whenever theta is taking the
value like this our l theta will be
theta to the of minus n
Now
now in this case now it is evident to
see that as theta increases
theta to the of minus n decreases for
all n greater than zero n greater than
0 makes sense but for sake of
completeness
Now this means that see what do you mean
by maximum likelihood estimation Now I
have this likelihood Now what theta
will give me the maximum value Now as
theta is increasing my likelihood is
decreasing So now what is the maximum
point that I can get The maximum point
that I can get is actually the the
leftmost value which is m correct
So logically it makes total sense So
so the mean occurs
so the mean occurs
only
at the
Oh sorry not the mean the max Okay
the max value
occurs only at the
smallest
allowed
point Now m is the smallest allowed
point Why It is a maximum of all the x
that you have Okay if m if the theta
is taking any value less than m so then
the indicator will get zero Now because
of which your likelihood is not
maximizing
Okay Now theta is equal to m and then
you have log of this theta
is
log of l theta
which is minus n
log
theta
Now you take the derivative of this
with respect dative with respect to
theta of
minus k by theta
is less than zero
for all theta greater than zero So so
it indicates so
l theta decreases the log likelihood
decreases with theta Uh so
so the max value
is
at the
left boundary
which is theta is equal to m So which
implies theta times
mle is equal to the max of x1 x2
so on until xn
Now and for our given data and
for our
given data
now theta
MLE is 2 point 2 and two Okay the maximum of
those values Okay now this is just a
small problem for you to say that know
how do you calculate the
the likelihood and then obtain the
maximum value just to indicate that it
is a a very simple and a straightforward
problem
for us to work out
Okay
this is regarding MLA estimate Now
lets go to the map estimate
Now here
now we want to estimate theta Now what
is the theta Now theta is the
probability of heads of a coin
Okay Now the data contains n tosses in
which n1 are head Suppose we want a
basin estimate
Okay Suppose the prior
is 0 point 5 if theta takes the value 0 point 5 0 point 5
if theta takes the value 0 point 6 zero
otherwise Now this is the your prior
distribution
Okay Now you have to take a conjugate
prior No because of which your prior
know which is that this is p theta and
theta given d Now both of them should
be of the similar form See uh dont
worry about this notations I will be
using the notations that are used in the
class Okay
So now how do we do it Okay
So
now we have to guess the estimate for
theta and provide estimation then derive
the map estimate
Now well be looking at obtaining the
map estimate in this case So now what
is that we want to do Now we want to
estimate
theta
which is uh probability of heads
of a coin
Okay we have uh n tosses
out of which we have n h tosses which
are heads and then nt which are tails
which is n minus nh
Okay
So now this is a binomial distribution
So I presume that all of you are clear
with this that this is a binomial
distribution Then
PD
equals to
choose NH
from N
theta to the power of NH and 1 minus theta
to the of
N t
Okay
Now then this is our uh binomial
distribution
Now we have
prior is discrete
P theta is 0 point 5
when
theta equals 0 point 5
0 point 5 when theta is equal to 0 point 6 These
are the two values And for every other
point you take zero mass
okay and we all know that theta mle in
all these cases will be nh by n
Okay
So now now
guess the map now Now see
now uh you should remember in the basian
thing P of
P of theta given D
is proportional to P of D given theta
into P theta This is your uh data This
is your prior and this is your conjugate
prior Both of them should have similar
functional form Now that means that
similar functional form in the sense it
can only take these two value
Okay the probability in which it takes
the value might change but eventually it
has to take only these two values Okay
be very clear with that You cannot take
any other value apart from the 0 point 5 and
0 point 6 Now as of now you
are giving for both of them equal
uh probability Okay Now your conjugate
prior now can take now different values
Okay So now now
let me guess for
guess for
theta map
Now it is uh
now
theta map
equal to
0 point 6 Six
when
n h by n is
near uh h by n is
uh
greater than
0 point 5
Now
theta map is 0 point 5
otherwise
this is what my guess is
Okay Now lets go ahead and look at
this
Okay So now
we this is my guess Now it makes sense
No
if it is greater than 0 point 5
Now Ill take theta mat is equal to 0 uh
6 which is the probability of head which
is there Ill take 0 point 5 otherwise okay
fine
so now
since
since I have p of
theta is equal to 0 point 5
equals p of theta is equal to 0 point 6 6 is
0 point 5
Okay Now now what is that You want to
compare
Okay
The comparison
the comparison of P of theta given D is
same as
comparing P of D given theta
correct
so now I can find the likelihood ratio P
of theta is equal to 0 point 6
given D by P of theta is equal to 0 point 5
given D is same as P of D given
theta equals to 0 point 6
P of D given theta equals 0 point 5
into
P of theta equals 0 point 6 6 into P of theta equals
0 point 5
Now these two values are same You can
cancel it out Therefore it becomes uh
the ratio of this
Okay
So now this is
P of D given theta equals 0 point 6
The ratio becomes P of D given theta equals
0 point 5
Now now what do you mean by this
This is a ratio When this value is
greater than this you choose 0 point 6
The other way you choose the 0 point 5
Now choose
choose
theta equals to 0 point 6
if p of d given theta is equal to 0 point 6 is
greater than p of d given theta equals to
0 point 5
Now r
you choose
theta equals 0 point 5
if
p g given
p of d given theta is equal to 0 point 5
greater than d given theta is equal to
0 point 6 six
Okay Now we want to compute these
values now Okay These uh data
conditioned on parameters Now we have
to compute these values Okay Now its
quite easy Now we already know the
functional form We know this We can
these are binomials
We can compute them So now P of D given
theta is equal to 0 point 6 Now what is this
Choose
NH out of n options 0 point 6
to the power of NH
0 point 4
to the power of NT Now similarly
T given theta is equal to 0 point 5
Let us choose
NH out of N options 0 point 5
to the power of n see now 0 point 5 to the of
n h 0 point 5 n will be there both n are
there so you can add now n h plus nt is n
so therefore it is like that okay so now
you want to find the ratio now now the
ratio is
d given theta is equal to 0 point 6 6ide
by
D given theta is equal to 0 point 5
0 point 6
to the power of NH 0 point 4
to the power of NT
divided by 0 point 5
to the of N
See uh what happens is this term is
common when you divide this will get
cancel So this is this term divid by
this term Okay This I can rewrite it
as 0 point 6
divided by 0 point 5
to the power of nh
0 point 4
 0 point 5
to the power of nt
This is 1 point 2
to the of nh
0 point 8 8
to the of nt
Okay
Now what is the thing that uh we are
looking into
Now
we are saying that
p of d given 0 point 6
is greater than p of d given
theta equals 0 point 6
theta equals 0 point 6 6 theta equals 0 point 5 Now you can
put them together Now we have this
ratio So now this is same as 1 point 2
to the of NH
to the power of NH into 0 point 8
to the power of
N minus NH
is greater than 1
Okay
And then you can take the log on both
sides
Okay Now NH
log of 1 point 2
plus N minus NH
log of 0 point 8
is greater than zero I have taken log
on both sides
Okay Now this is
NH
1 point 2
minus NH
ln of 0 point 8
 plus N into ln of 0 point 8
now greater than zero
Now this is
NH
Just a minute
Now what is
just we just have
what is
this 1 point 2 2
2 8
that is 1 point 5 Okay Now this is ln of
1 point 5
plus n into ln of 0 point 8
no greater than zero
Now this is
n h is greater than minus n ln of 0 point 8 8
divided by
ln of 1 point 2 2 1 point 5 sorry
okay
this I can
relate as NH
greater than
N
ln of 1
25ide
by ln of 1 point 5
okay just applying some logarithmic
thing Now 1 by ln of 1 by 8
will give you this value Now this will
be n h greater than 0 point 55
 times n Now this is the condition Now
finally what I want I know only n h and
then I know n
Now what is the estimate that I have to
consider
Now now when this is satisfied
now this is Im saying that I take the
decision theta
is uh uh equal to 0 point 6 When do I take
this decision When this condition is
satisfied Okay Now finally I will
write that
now when n h is approximately greater
than 0 point 55
 times n then theta map
Ill take it as 0 point 6 6
otherwise
Ill consider my theta map as 0 point 5
this is almost similar to what my
assumption was right
not exactly I did not get
0 point 55 but yeah similar to our assumption
that we made now this is how you will be
able to obtain
from the given data the map estimate
Okay So now uh here is where uh we
stop Now a special thanks to professor
Shastri for curating these wonderful
questions Now when small questions now
can give us a lot more insights into the
ideas
So we stop at this point Now I hope you
enjoyed our overall discussion on
obtaining base classifier MLE and map
Well come up with other topics and then
some other problems exciting ones in our
coming tutorials Meet you then
Bye bye
