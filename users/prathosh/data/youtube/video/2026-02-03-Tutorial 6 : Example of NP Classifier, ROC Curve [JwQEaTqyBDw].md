---
id: JwQEaTqyBDw
title: "Tutorial 6 : Example of NP Classifier, ROC Curve"
url: https://www.youtube.com/watch?v=JwQEaTqyBDw
date: '2026-02-03'
duration: 32:40
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

speaker_1: Hello all welcome to this tutorials in
which we will be seeing an example of
the Neiman Pearson classifier
that we have discussed in our earlier
tutorials Now just to give you a small
uh uh recap on
the last uh tutorials Now we
constructed a classifier
uh now which
is bounding the type one error by alpha
and then whatever hypothesis function
that satisfies this the one that is uh
giving us the least type two error is
what we are considering and then now
whenever we have classifier of uh this
condition okay where in which we take
the decision based on the
ratio of class conditionals
uh that is an PSN classifier we proved
it using uh the conditions that is where
we have stopped in our earlier
discussion in todays discussion what uh
we shall be looking at is well be
looking at an example of neur pearson
classifier and then we will be looking
at very interesting uh uh idea called as
ROC Okay Now without any further delay
lets proceed
Now we will be looking at the
example of
Neiman Pearson
classifier
Now what are the X belongs to R Your
samples belongs to R
Okay And then uh the class conditionals
are uh
the class conditional
densities are
normal
with
equivariance
Equal variance
And then without loss of uh generality
we are assuming that mu0
is less than u1
Okay So now what is that we want to do
Now we want to come up with the
threshold Okay So now
so now
one can show that
the NP classifier
is if given X is greater than the tow
then
Ill say that its class one
Now how do you determine this toao Uh
where to is determined that bound on the
type one error Okay So
where
to is
determined on
type one
error bound
Now what do you mean by that Now it
means that
the
integral from to
infinite
x dx
to
alpha
Okay Uh so now we have seen this
diagrammatically also If you look at
this now from if you consider this as to
from to infinity now what is the area
under the the class conditional of the
zerooth class okay now thats what now
this blue area is what uh your
calculating and that is uh what is the
alpha that you have uh bounding okay
fine
So
now we know that
now base classifier
base classifier
minimizes
risk which is a kind of the weighted
error Okay this we have seen earlier
also which is a
kind of
weighted error
Okay So now uh and we know that the NP
classifier is a way of uh deciding how
to trade one type of error with another
Okay
NP classifier is
another way of
deciding
how to
trade
one type of
error with
another Okay we have in detail look at
it Okay
So now for a two class problem now what
it boils down to for a class problem for
a
two class
problem
one can
always
trade
false positive rate
against
false
negative rates
Okay And this we have already seen Now
we know what is uh
false positive We look at it
sometimes uh
okay
Yes Yes false positive and false
between yeah just I wanted to know that
whether I have induced those
nomenclature
okay
now now what do we want now we always
want a threshold
which can be tuned to take care of this
trade off
okay now we want to tune it that means
that we have to decide on
Okay So now we would
we would always
have a
threshold
which
can be tuned
to
affect
this tradeoff
So now you have lot of uh uh options So
now what is the best that you want now
depending on a threshold I should be
able to look at it Okay Now you should
be able to take care of it and this can
be done using now what is known as ROC
receiver
operating
characteristic curve
Okay now is a good way of looking at it
is a convenient
way of
looking at this
looking at this trade off thats what uh
I mean by that
okay so now
lets consider that uh two dimensional
sorry one dimensional feature
lets put all of them together
Now
consider
one x belongs to r
and a two class problem
and a two class problem Now then my h
of x is equal to zero if x less than
this tow Now I will consider uh equal
prior okay and then class conditionals
with equariance and then 01 loss okay on
this now
consider
equal prior
Gaussian class conditional normal H
plus conditional densities
with
equal variance
and zero loss
Okay Now then from our earlier
discussion
the probability of error which is
we have obtained it will be 0 point 5
from minus infinity to to
x given y equals 1 of x dx plus c now okay
plus 0 point 5
into to
infinity
given y equals 0 of x dx Now again I just
want to reiterate this Now this uh
orange that youre seeing is uh uh class
one Now you can see that now what is
risk this area and this
area
Okay thats what youre considering
Fine So now this you can uh
easily
compute Now you can substitute uh these
are Gaussian Now we can substitute and
then
we can immediately see that now this
will turns out to be 0 point 5
into f of
minus mu1 divided by sigma
plus
1
f of minus not
sigma
this will be my error
okay now depending on my value of tow I
can compute the error
okay
fine
so now
lets make a note of this
as We
very
we trade
one
kind of
error
with
another Now that means that as you move
that
uh tow okay
there will be a tradeoff between one
kind of another error to another
Okay
So now
now whenever you consider a two class
problem
in a twocl classification
there will be four possible outcomes
Okay
Now two we have already seen there will
be four
possible
outcomes
Now what are those first four possible
outcomes
Lets try to write them
So now lets uh define
EI
Now which
denote the
which denote the probability of
wrongly
assigning
class I Okay youre wrongly assigning
class I So now there are two cases
Okay And Im assuming that uh
C1 is a positive class
C 0 is a negative class
So now then
we decide
C1 if
X is greater than to
Now then this gave rise to
E 0 that is what is the probability that
Im wrongly putting it to class I now
that means that when do I put wrongly
put it into class
X is less than to that is when I wrongly
put it into class zero when X actually
belongs to C1 now what is the
probability of this is what Im asking
now this is falsely uh put as negative
right now this is
false
negative rate
Similarly I can have uh E1
 where in which
X is greater than to now that is when
you assign it to one but actually X
belongs to
the negative class What is the
probability of it This is known as the
false
positive rate Okay So now we can have
the the complements of these Okay Now
I can have 1 minus E not
then it will be the the probability that
X greater than
to X belongs to C1 Now this is true
positive
true positive rate and similarly I can
have 1 minus E1 now which is probability
that
X is less than or equal to to given X
belongs to C KN this is
true
negative rate okay now I assume that
these uh terms are comfortable able
Okay Now whenever we have now these
things we come up with the
two more uh quantities of interest that
uh in most of the binary classification
problems Now youll be seeing them
repeatedly
We have
two quantities of interest
is of
interest Now one is what is known as
the
precision
which is true positive divided by true
positive plus
false positive and then we have
recall that is true positive divide by
true positive plus false negative
Okay Now I assume that uh you will be
able to write these
in terms of these probabilities
Okay
So now
these are uh two quantities that we
always look into whenever we are looking
into the
problem of uh
binary classification and then now
sometimes we take the hormonic mean of
this and then call it as an F1 score
Okay Uh that is an outcome of these two
quantities So we will not uh uh look
into it or you will be capable enough of
uh looking at this Okay So now coming
back to the way of choosing the
threshold which was our uh actual need
Okay So now
now it is uh quite clear that as I
change my tow now
there will be a change in E1 and 1 minus
E not
okay so Now
for a
fixed class conditional
for a fixed class conditional
densities
If we
vary
to
the point E1
minus E not moves
on a
smooth
curve in R2
Correct
So now
for a fixed to we can always estimate in
even from the training data So now
hence if you vary this to okay now we
can find this ROC and decide now which
is the best point that we actually need
Okay what is the point that gives us
the good uh trade off that we need
Okay So now this is
uh we dont that
hence
hence varying the stove
we can
find
ROC
and
decide
which
may be the
best
operating point that means what is the
best trade off that we need for our
given case Okay
Now as you can see this can be done for
any threshold based uh classical
classifier Okay Now
this
can be
done
for
any threshold
based classifier
irrespective of
class conditions
now thats what we shall be looking at
in our demo now which I was showing uh
let me run this
so now this is for the previous run
okay now you can lets first try to uh
understand
this Now this is the blue one is uh uh
the class zero and this orange is class
one Now you can see that now this is
class one which is being uh what do you
call classified as uh uh class 0 and
this is
class 0 classified as class one The
false positive and false uh uh negative
Now you can easily see
Okay So now
I have obtained I have calculated the
base risk Now that is 058655
and this is my ROC curve Okay Now as I
vary my threshold now you can see that
the true positive rate and the false
positive rate Now that is uh uh e 0 and
1 uh sorry uh e1 and 1 minus e 0 Okay this
is 1 minus e 0 this is e1 when I vary this
now your
risk varies Now whichever is the best
risk that you want you can choose it
Okay So and now I have put a small uh
uh tool to look at it Okay Now you can
see that I have varied this
Now you see this what has happened Now
your classifier has moved Okay And
then uh this is the overall region that
is you have considered as a false
positive and then I can
actually move this then we can come this
orange dot No which is there is
actually the
the base error wherein which you are
getting that whatever is the value 0 point 15
8 Okay And now you can see this
Okay
Now as you can see here as I modify this
you see that which point you want Okay
Now how should be your tradeoff Now
depending on it you can decide what do
you want Okay
you can decide depending on the
threshold
you decide when to put and you can know
the tradeoff that is there uh between
the
two kinds of errors
Okay
The best thing that you get is that uh
what this okay uh so
this is uh uh this is what I have uh
been trying to explain you that as you
vary the tow now your uh uh tradeoff
between one error one type of error and
other type of error actually varies
which you can programmatically see now
in this particular uh given animation
Okay Uh so uh this is where I have
considered one dimensional feature and
then the class conditionals with uh
equivariance and then uh I have uh tried
to come up with this particular uh
animation which is there Okay Now now
I assume that all the dots that we have
been discussing is able to uh what do
you call obtain it at a at a nice place
Okay So now lets go back couple of uh
small small minute details that we need
to have Okay Uh
so now
when
when the class conditionals
class conditional densities
are
are normal
with
equal Variance
E1 is from to
sorry to to infinity this is not minus
infinity is to infinity probability that
X given is equal to 0 of X
dx equals 1
mu by sigma
and
E not S is
minus infinite to to
X given Y equals 1 of X
dx X
Okay See uh the point is whenever you
write uh equations now at least at an
intuitive level for a simple
one dimensional features you should be
able to visualize what is happening
Okay That is the reason why we have all
these uh diagrams now that are there
You should be able to visualize what is
the integral from where to where is
happening Now now once you have that
in at least the intuition should be
quite comfortably clear Okay thats
thats needed Okay Now
from the error integral now we get now
lets calculate the the tow
Okay So now from there integrals
from these uh
integrals
we get
to minus
mu not sigma is
v inverse of
1 minus e1 lets say it is a
okay and then
to minus
inverse 1 minus
minus of not lets call it b
okay so now and then now then comes the
interesting thing
then if If I take the modulus of a minus
b Now this is mu1 minus mu
divided by z sigma
and you see this this is called as
discriminator
which is not dependent on toao Okay Uh
this is
called the discriminator
which is
not
dependent on to
Okay So now knowing e1 and 1 minus e not we
can uh
get this d and hence we can uh get the
base error Okay So now for any uh
given to we can also get actual error
probability and we can tweak this uh to
get the base error Thats what we
actually did Okay we can get this uh
we can tweak this out to match to the
base error Okay And whenever we are
plotting this ROC there is one more
thing that we do So we always join the
0 0 and uh 1 one Now this is what is
known as a random classifier This is Y
is equal to X line which is there Now
uh now the the area under this ROC curve
is what is known as AU area under the
curve Okay And its a very good
indicator regarding the quality of the
classifier Okay So now the curve that
you get the ROC curve should not be
below the y is equal to x line Okay
Now it has to be always above that Now
what does it indicate Now its just a
random random classifier That means
that you take a coin and then you just
depending on the toss of the coin you
decide what is the what is the class
Okay Now thats thats thats not even
learning in any case Okay So now in
that situation now the
the classifier that we come up whatever
might be the classifier has to be better
than that random classifier which is the
y is equal to the x line that we get
Okay So now thats the one more uh
important thing about this
ro Okay So now I with this we conclude
uh uh this tutorial
I hope that you understood the
importance of this threshold and how do
you manipulate this threshold that gives
rise to a very nice interesting uh uh
idea called as receiver operating
characteristics ROC curve and then the
outcome of this uh the area under this
ROC which is known as AU area under the
curve which is a good indicator of the
classifier and then it also gave rise to
a couple of interesting quantities like
precision and recall which are quite
important whenever we are dealing with
the
classification tasks Okay Now with
this we conclude todays tutorials Now
I hope it was helpful Thank you Lets
meet in the next tutorial Bye bye
