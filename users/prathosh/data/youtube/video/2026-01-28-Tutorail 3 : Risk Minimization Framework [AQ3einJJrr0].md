---
id: AQ3einJJrr0
title: Tutorail 3 : Risk Minimization Framework
url: https://www.youtube.com/watch?v=AQ3einJJrr0
date: '2026-01-28'
duration: 59:52
model: youtube-captions (en-orig)
transcript: true
---

## Transcript

Hello all welcome to this tutorials in
which we shall be looking into the
extension of the base classifier that we
saw during our previous session
While we were considering the base
classifier the assumption was we were
dealing with a two case Okay uh we
were having two classes Okay So and
then we were dealing with 01 loss So
now we shall go ahead and uh come up
with a much more generic model and try
to understand in an uh in a generic way
the details So lets go ahead with
that
Now
lets
lets consider the
base classifier
with
M classes
and
any loss function
So in our uh earlier sessions
professor has explained that he has
taken a two class case with an emphasis
towards 01 loss Now we will go ahead
with the much more generic approach and
then we will look at it Lets say that
y which is what for practical sake well
be calling it as labels can take values
c 0
c1
so on till c m minus one now these are
true labels
okay and then we have a hypothesis
function
which takes
X as an input and then gives the
prediction or output They can be alpha
1 0 alpha 1 so until alpha
k minus one Now these are
decisions
from the
hypothesis function See here we are
looking at a much more generic case
So here the decision of the hypothesis
function can have more
uh labels also Now for example one
standard thing that you can think of is
a reject case So where in which my
k will be m plus one Okay So we are
looking at a much more generic case now
where in which the labels the true
labels okay is a subset of the decisions
from the hypothesis function Okay
So we are considering the generic case
in
in general the number of outcomes in the
number of uh the cardality of the true
labels is not equal to the number of
outcomes from the hypothesis function
 So now in this case how
do we define the loss
So
the loss is defined as a function
from the outcome of the hypothesis
function cross y
to r plus
okay so lets define this now lets say
that the loss when my hypothesis
function says
the decision it takes is alpha J but the
actual label is CT
Okay this is a loss that is incurred
So this is loss
when the hypothesis function
is saying its alpha J and
true label
is
CT
So in this particular framework now what
happens is now lets look at the risk of
this
particular setup uh for any classifier
Okay Now risk
of the
classifier
is
RH
Okay is equal to the expected loss
over the joint XY
loss of
H of X comma Y
Okay this is the risk
Now what do we want
So
we want a classifier with the least
risk Okay we want a
classifier
with
least
risk value
Okay
So now lets uh look at this
we know that the risk for any hypothesis
function Okay So lets make one more
thing here to be more specific Lets
say that uh we have a class of
hypothesis functions
for which the h belongs to Okay fine
just to make it complete
So now this is uh
expectation with respect to the
xy this is loss of h of x comma y
Now this I can uh decompose
into
expectation with respect to x
into expect conditional expectation y
given x
loss of
h of x
comma y
conditioned on X
Okay So now now what we will say this
is the
what is known as the
conditional risk
This is
conditional risk Okay So now you can
easily see it from here So now
this conditional risk
is
dependent on my hypothesis function
Okay So now
this you can uh easily
expand it This is overx
This is I can come up with conditional
risk
okay given x and then px of x
dx Okay
So fine So now lets try to understand
this conditional risk
in a comprehensive manner Okay So
lets go to this conditional risk for a
given example X Okay consider X
consider
X
So now lets say that classifier
H of X is alpha I for this specific
case Now then I can come up with a
conditional risk
Okay Now what does it denotes This
denotes the expected loss when the
classifier says the given example X can
be put into alpha ice bucket Okay This
denotes
expected loss
when
when classifier
says alpha i for the given x Okay this
I can uh actually go ahead and write it
as for uh
given x this is expectation
with respect to y given x
Now this is loss
h of x comma y conditioned on I have
already know that for this given example
my classifier is saying it is alpha i
then conditioned on my input So now
because of this
this will be
again
expectation with respect to y given x
loss
alpha i No because I already know that
the outcome of my hypothesis is alpha i
comma y
condition
x equals
x Okay fine So now
now this is y is a discrete uh random
variable So now we know the expectation
of this This is uh straightforward even
though its a function of x So we can
write it as a
j is equal to 02
m minus one
This is loss
It says
into P of Y given X
when Y is CJ for a given
input X Okay So now now a couple of uh
now this Y given X is known as the
posterior
Okay Now whenever you have uh p of okay
let me just make a note of this
Now whenever uh have p of y given x is
known as the
posterior
p of y
is known as the
prior the distributions that par
distribution and then uh P of X given Y
is
class
its class conditional
now this is this is posterior okay so
now this is a much more
generic
view of looking at the risk
So now now what do I have now Lets put
things together Now we have
in general
in general we have
risk
when your uh
hypothesis function is giving you
certain decision is summation j equals 0 to m
minus1
loss incurred
It is giving h of x
is cj
and the posterior
y given x
when y is cj given
x equals
a specific example
Okay
So now now this you can go ahead and
substitute it back This is the
conditional uh risk Now this you can go
back and uh put it here
Okay Now this is a much more a generic
viewpoint
of looking at the risk So now
with this much in hand
now what do you mean by an optimal
classifier in this case Now the
distribute the x is fixed Okay Now
here now x is fixed and then this risk
which is a positive uh entity or or non
negative entity It can be zero as well
Okay So now for the classifier for
which this is minimum this conditional
risk is minimum we are actually in
search of that specific classifier
Lets make a note of
that
Now therefore now what do you mean by
optimal classifier in this case
uh
for each x
h of x
should be
such that
should be such that risk
when you have uh
incurred should be less than or equal to
using risk obtained or any other
hypothesis function that belongs to the
class of hypothesis functions H
Now this is what we mean by the optimal
classifier
in this case
Okay So now
now lets bring in the base classifier
Now
the base classifier
lets call it HB
for a generic
M class
is
so my base classifier or base hypothesis
function well say alpha I
If
if you look at
the conditional risk which is given by
this
summation of loss incurred by saying
alpha I
CJ into the posterior
Y given X
when it says it is CJ
given X Okay is less than or equal to
m minus one
loss of loss incurred when saying it is
some
class the decision is alpha t
and
I given x
y equals
I equ equals CJ given X for all T Now what is
what is it saying So the conditional
risk which I obtain when my decision
is alpha I is less than taking any other
decision
Okay And then so since you have an
equality now how do you break the tie
No we break the tie arbitrarily Okay
So always
break
ties
arbitrarily
Okay
Now this is the formulation of uh the
hypothesis uh function using a base
classifier in an MC class uh case in M
class and even its for any loss
function Now again we have havent
reiterated I havent uh explicitly taken
uh 01 loss Okay we will take it as a
special case and then we will look at it
in some time Okay So now
now just to
link it to our earlier case Now lets
consider the one that has been looked in
our class Lets consider
m is equal to 2
Now
then the outcomes okay now that is see
again when I say m is equal to two now y
can take values between 0 and one or or
any there are two outcomes in y but that
doesnt mean to say that what will be
the uh outcome of the hypothesis
function okay please keep that in mind
Okay
Okay Uh better we can fix that also
There are uh only two outcomes that uh
uh the hypers function is also giving
alpha 0 and alpha 1 No you can fix it
No else you can sum it over Thats also
fine Now lets fix it two in this case
Otherwise
so if
the loss incurred when the hypothesis
function says it is alpha 0
say 0
into the posterior
y given x
y equals c 0
given x
class
when it says
alpha zero but the actual class is c1
into the posterior
y given x
c1
lets make it clear now in this case Im
assuming that y can take values
c 0 and c1 no h of X
takes values if 0 and alpha 1 Now we
are making it much more generic So you
can fix it So I just want to uh what do
you call uh drive in the idea that okay
now these two things can be different
Okay you can have multiple
elements over here Thats thats
totally fine
This is less than
was incurred when you take
given x
 plus
c1 the posterior y given
y equals c1 given x
Okay So now if you have uh multiple
values that your hypothesis function can
take then this has to be the least Now
then you represent it by some alpha t
here and then you say that for all t uh
so that the indexing that is happening
for this hypothesis function you can go
ahead with that Okay So now now lets
make it its I know that it is too
verbose having uh too much of uh
notations So now lets reduce the
notations
So now lets take the 01 Now now Im
coming to the specific case of 01 loss
Now consider

01 loss Now what do you mean by that
the loss incurred
when
Im saying for 0 and C 0 is equal to the
loss when Im saying 1 and C1 these are
same okay is zero okay now
this is
Ill just indicate it by 0 0 1 okay I
think that should be comfortable know in
Y also Ill indicate just with by 0 and
one which makes the notations much more
easier to parse Okay Now by now I
assume that all of you are comfortable
with the notations So I can just say
that the first value in this loss now as
I have defined
earlier Now this is the outcome of your
hypothesis function This is the outcome
of your uh uh this is this is your true
label Okay In most of the cases it is
y cross y Thats what all thats what
we have also looked into But this is a
more much more a generic uh way of
looking things Okay Fine
Now lets uh reduce the burden of
notations Now how it will be now laws
incurred when my hypothesis function
says zero
but the true label is one
given
that y is equal to 1
given x is less than or equal to loss
when 1 0 probability that y is equal to
0 given x okay now this is what it
finally
boils down to okay much more simpler
notations So why why is this now
because this will be zero and then this
will be zero Therefore you have this
term and this term Now where in which
there is a mismatch in terms of the
decision Now this you can easily
rewrite it as
this you can rewrite it as a ratio of
posteriors
y equals 0
given x divided by the posterior y equals 1
given x is greater than or equal to loss
incurred
Okay
0 1
0 Okay This you can
look into
Okay
And this is what is known as the ratio
of odds
Famous known as the ratio of odds
Okay
Now lets uh
now lets go back to our MClass case

Now lets go back to our Mcast MClclass
case and then uh try to bring in the
notions of
much more comfortability there
So now
now there now I am generalizing it for a
01 loss in our M class case Okay Now
lets generalize
this to
an
M class case and
01 loss function
Now let me reiterate how will by my risk
looks like Now given x equals summation
over all the
true labels
and the laws incurred
when I say alpha i
and the true label is cj and p of y
given x y equals to cj
given x Now this I can easily write it
as
now this is okay
now only when the outcomes are different
the loss is one when the outcomes are
same the loss will be zero thats how
the zero one loss works right so now
only when I and J are different now then
there will be a
loss of one okay else it will be zero
now that means that Now this I can
easily write to the case now where in
which J not equal to I for every J that
is not equal to I J taking value between
0 to N minus 1 Now this is that Y
given X
Y equals CJ
given X
Now this
now this is
1 minus probability of y the posterior y
given x y is equal to ci
given x
Okay Now therefore now therefore now
how will be my uh
base classifier now Now
therefore
my base classifier
should be of x Now this will give us i1
1us
y given x
y equals ci
given x is
less than or equal to 1us
posterior for
any other j
for any other outcome
This is for all j for all j that belongs
to 0 to n minus one Okay Now this will
be
y given x
y equals to ci
given x greater than
posterior
Now this we know
Okay Now this now things are
intuitively clear Now what is this
Now this is
now which one is having the highest uh
uh probability that is the one that Im
considering
right now I will say that now I will say
that
my hypothesis function is giving me Im
assigning this particular label when the
probability of that specific case is
maximum H
in all of the two labels Okay So now
this
is the
M classifier
for
01 loss function
This is
minimizer
of the probability of mix
mclassification
This makes
okay
Now that means that for whichever class
we have got the highest probability that
is the label that Im going ahead Okay
Now this is
the thing that was left as a a small uh
uh takeaway in the class Okay So now
what we shall do is now we shall delve
deep into this and then we will try to
come up with some nice uh
uh cases that we all know Okay So now
what we shall do is now lets take a two
class uh case Okay There are two
labels Okay
Now now for a two class case
now
lets
consider
m equals to 2 then in that case how will the
things looks like Now the laws incurred
01 and then
y equals 1 given x
and laws incurred 1 0
y equals 0
given x
Now this the posterior
Now by base rule now this I can
decompose into
x given y equals 1 into
that y equals 1
less than loss 1 0
x given the class conditional into the
prior
Now this I can easily write now So now
youll ask know what about uh px So now
you can just cancel it off right Okay
Now I I think this this much of algebra
all of you should be comfortably able to
do it Okay So now my posterior which I
have you know I can replace it as the
product of the class conditional and
then the prior
Okay
So now this
uh I can take log on both sides Why Im
taking log on both sides is then what
Ill assume is now for this specific
class conditional I will go ahead and
consider it as a Gaussian now and then
Gaussian has an exponential and then you
have a log both of them will get cancel
out so that we can get some beautiful
forms
that is where Im heading for that
specific reason I can take log I can
take log okay now
taking
log on
both sides
and then we are assuming
x given
y
Now
the class conditionals
class conditionals
the Gaussian distributions okay see here
Im taking uh the 1D gaussian now I will
leave it as an exercise for you to take
so a dimensional gaussian distribution
and see how a similar
expressions can be obtained Okay So
conditionals B
gaussian distribution
Okay Now now
this I can
applying log I can write it as
ln of
probability
5 equals 0 into loss 1 0
plus
ln of probability
x
given
y equals 0
This has to be
less than
ln of probability
y equals 1
loss
plus
ln of quantity x given y equals 1
Okay
Now
lets substitute
the class conditionals Now we know that
of x
given y is equal to sum i Okay some i
or this x given y equals i This I can write
it as 1 by zigma i square roo of 2
pi
xp of minus x
mui square divide by 2 zigma i²
okay here I in this particular case I
can take value 0 and 1 okay so now what
will happen now lets take one case
Okay lets take a generic I and then uh
substitute it later onto this particular
thing Okay now lets take the log of
this and try to see now how it is Now
if I take the log of this
okay
now this is
taking
log
Okay just put it here This is ln of 1
 I 1
of 2 pi
 plus

x² minus mu y² plus 2x muy
divided by 2 zigma i² Now this uh
can
easily write it as minus
log of sigma i
into
log of 2 pi
minus x² by 2 sigma i²
minus minus mui² by 2 zigma i² plus 2x mui
by 2
zigma i² Okay this
is the case Now I can now substitute
this now which is there now
back into this specific equation Okay
Now
Ill substitute this Now you have this
term have this term and then this will
be replaced with this
Okay
So now
And this will be
ln of
p
y equals 0 is the first term zero
loss of
1 0
This is there
minus
ln of
alpha 0 Oh sorry Sorry not alpha 0
This is sigma 0 into ln of 2 pi
Okay Very big to nice
Okay Now
remember the joke that sir made it in
the session So FAs
last theorem So this is the
correct case that I also have But
anyhow okay Minus x²
okay Uh so lets do this Now Ill
leave this whole algebra to you and then
Ill rearrange the terms and write the
final equations Okay So I assume that
uh now you can substitute this then uh
make that thing Okay So you have to
substitute in this See now think of it
like this Now what is happening Okay
Now you have an x² term You have an x
term
Okay Now look at now this is
log of something Now this is again this
is a constant No need to worry about
this Okay now you have an x² term and
then you have an x term
Okay so now lets
take a case how this will affect by the
choice of mu and sigma that I take
Okay thats what thats where Im going
now Okay so now by rearranging the
terms just skipping the algebra
Lets make a note of this Skipping the
substitution
and
rearranging the
terms
Okay you rearrange the terms Then what
will happen is I will just half x² into
1 by sigma
1²
0²
 plus x
mu divided by
square minus
1 square
Okay Again plus half
mu1 divided by sigma 1 square minus
sorry mu1 squared
This is 1 square
plus
log of 1
sigma kn plus
ln of
p y equals 0 into loss of 1 0 by p y equals 1
0a 1
this whole term
greater than zero
Okay Im just shuffling things So now
now if you look at this now you have an
x² term you have an x term and then you
have some bunch of constants put
together Now this is similar to ax² plus b
x plus c Okay when you have mu and sigma
is fixed Okay And and for sure yeah
you take uh uh you fix these values and
fix the prior probabilities Once you
fix this now this is a function of your
x is what Im telling Okay So now
this is
this is of the form
uh again now where Im going now Im
taking a base classifier now where in
which I have zero and loss and then I
have two outcomes it says zero if a x²
square plus b x plus c is greater than z
Okay Now what happens is now your this
is this is what is known as a
discriminant function Right Okay Now
this your base classifier in this case
is nothing but a quadratic discriminant
function Okay All these algebra that
we are trying to do is just to show that
see now your base classifier which is
there now is nothing but a quadratic
discriminant function and then we will
assume certain specific cases and then
we can we reduce it further We will
look at it now Okay So now this means
now this implies the
the base classifier
in
this case
is a
quadratic
in this case a quadratic
discriminant
function
Okay this is a quadratic discriminant
function
Okay
so
now now what is that case Now Im
considering the base classifier my m is
equal to two and then Im considering 01
loss and then Im assuming that my class
conditional is Gaussian with mu0 and
sigma 0 Similarly sorry mui sigma i
Okay those are the conditions that I
have applied on this Okay now because
of which my base classifier has turned
out to be a quadratic discriminant
function
Okay So now
now what we shall do is now we will take
some special cases of this again Okay
some special cases Case one
Okay let me make it some special cases
some special cases
Now case one in which Im saying that uh
sigma 0 sigma 1 is zigma and then
probability that y is equal to zero is
equal the prior the prior
are same and that means that its half
okay this is half and then the loss that
is incurred
in both the cases are same
now when Im saying that the loss that
is incurred in both the cases are same
now that means that there can be cases
in which they can be different actually
now in that case what will happen
okay now Im Im hinting you towards
now some other ideas okay now just think
of it now in this case Im saying that
no both the
losses that are incurred
are same now will it be always like that
now that means that now whenever now now
consider your uh all of You remember the
covid times right Now lets say that
zero is uh negative and one is positive
Now will the impact when I say that a
positive covid positive person is
actually I say that he is negative will
it be same as when I say a negative
person is positive Can I make that
assumption is what Im asking you Okay
that may not be the case Now there are
multiple kinds of errors Now which
error are you looking into Okay Now
look out for that We will have uh some
more discussions on it Okay This is
just a a small link so that well be
discussing them again Okay Yeah Sure
Now now coming back to our present
case Okay Now Im assuming these
things Now then what will happen now
Then then
my base classifier
is says zero when see now lets put this
up and see
now when this will go off actually now
when sigma 1 and zigma 0 are same now
this will go off
fine
now
then this is a term of x with some
constant Okay So now lets write it up
Then it will be x
and then this will go off again Uh this
term will go off This term will go off
Correct This will go off This will go
off This will go off These terms will
go off under the current conditions
Okay X
Zigma square into mu minus mu1 minus 1 by 2 sigma
square
 minus mu1²
is greater than 0 Now without loss of
generality Im assuming that mu0 is
greater than
uh mu1 Now in that case x is
this will be your condition
assuming
mu1
Okay Now
this is a a linear case Now how does it
look like Now these thing I I can
simulate right I know the values of my
zigma I can fix it I can say fix some
muse and then see how
they look like Thats what exactly I
have done Okay
Now this is class 0 and this is class
one This is your decision boundary
This is your discriminant function
Okay Uh so Ill be sharing this code
You can look at it But in this is what
it is actually
Correct This is the one This is a base
classifier and we all know that base
classifier is optimal classifier Now
what will happen if I move this line
here What will happen if this if I move
this line here Okay
And then now in those cases the error is
not optimal Right
Okay I assume that all of you can
appreciate this Okay
Now this is the base classifier that I
have Now what are the samp uh so the
samples that I have generated is uh mu0
I have taken it as minus one and mu1 I
have taken it as one and then I have
done this
okay
this will be the optimal classifier
 that I have
so now lets look at another uh case
case two
Case two is where I have my mu 0 and mu1
are zero My priors
are same
half and then
the loss
are same Now in this case now what will
happen So since mu1 mu not and mu1 are
zero Now what will happen
Okay
So now I will I will have this term x²
term will be there But since mu not and
mu1 are zero this term will go off
This term will go off This term will go
off
Right These terms will go off
Correct
So now
in that case
hb equals 0
if
half
x² into 1 by sigma 1 square minus 1 by r²

ln of
is greater than zero
Okay Now in this case now again without
loss of generality assuming
x²
is
ln of
that means that this is a quadratic
case is now how it will look like
Okay thats what the next code is
about This is how your data will look
like Okay since you have a square so
then you take the square root of it So
youll have the plus and minus Now
this is how it look like the boundary
Okay
we can simulate them These things can
be simulated quite easily
Okay
So
again a couple of small things
Self help
or help yourself with
self help
Try the same thing out
Try out for
X belongs to
RD
Okay Now what do I what do I mean by
that Now this is P of X given Y equals I is
from some normal distribution
Now where in which it is having UI and
zigma I which X belongs to RD
Okay Now this is the case that Im
trying you to look at it Now look at
this and uh convince yourself that you
get similar uh kinds of results
Okay So now lets see how how is the
error Okay Now we were always uh
looking at uh the risk Now lets lets
put some value how it will look like
Can we can we this this is the last
step Can we actually obtain uh some
computable values Okay
Now we will do it explicitly for a two
class uh m is equal to two case Okay
And then assuming zero and loss Okay
So now now
consider
the
case of
base
classifier
with 01 loss
and
m is equal to 2 this is the case uh
that Im assuming
okay
then
we know that the risk
in this case
integral over RD Im assuming that X
belongs to RD its fine we have computed
this this is minimum of
Y is equal to0
that X given
is equal to 1
This we have already computed in our uh
earlier sessions Now we have computed
uh these cases
Okay
So now
lets bring them to specific case Okay
Now
lets
take a specific case
where my x belongs to r Okay It
doesnt matter whether it is an RD
Okay And then uh
the prior y equals 0 equals y equals 1 is half
And then uh the class conditionals x1 y equals
i are gaussian distributions
Now when I say gaussian even put certain
conditions is equal to u1 is equal to mu
sorry uh z sigma 0 is equal to sigma 1
is equal to z sigma okay and then
without uh loss of generality Im
assuming that uh mu not is mu1 so in
this case so what will happen is now in
all these cases hb is equal to zero if
x is less and mu plus mu1 by 2 Okay Now
this will be my discriminant function
Now now how will be my risk Okay Now
now in this case
my the risk that is obtained is
the prior
into minus infinity to
mu not plus mu1 by 2 into
x given y equals 1 This is capital x okay
into dx So sorry Im abusing notations
left right center Okay Now I presume
that you can uh get them comfortably
Okay Plus
0 point 5
m plus mu1 by 2 till infinity
is given is equal to 0
dx
Now this you can easily substitute and
put them in the form of the standard
normal table This is P of
mu
mu1 by 2 sigma plus 0 point 5
into 1
1
by 2
This will be the error
Can now if you explicitly oh sorry there
is a sigma here Okay Now if you can
explicitly
uh have the values of
the mu not mu1 and
zigma we can actually get the the risk
that is incurred Now this is just to
show that okay these things are doable
Okay Now with this we conclude our uh
uh long tutorial on looking at the risk
and then specifically looking at the
cases in a much more broad and generic
way and uh taking into consideration
all the uh what do you call different

uh cases now where in which we looked at
even the outcomes can be different and
then how do you model the whole system
in that case and then when you take
special considerations how things will
be converted into the forms that we know
in real time like
a linear discriminant quadratic
discriminant and stuff Okay I hope
this was interesting and then you
learned lot of things Thank you
