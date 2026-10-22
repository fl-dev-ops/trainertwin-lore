---
id: Ij4p5hLbfo4
title: Lec 13 Minimization of KL Divergence
url: https://www.youtube.com/watch?v=Ij4p5hLbfo4
date: '2026-01-28'
duration: 24:51
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Lec 13 Minimization of KL Divergence

## Transcript

speaker_1: Welcome back So now that we have uh a
way to
quantify the distance between the
density functions or distributions we
are good to go Well go back to our
recipe Right So lets go back to our
machine learning recipe
Now given
okay for now see when Im formulating
this uh the general solution for the ML
problem I will assume that we are given
a particular random variable
from a distribution and a lot of samples
from it or I can make an ID assumption
and say that I have n random variables
one realization of each and we have
n of them which are identically
distributed independent and identically
distributed Let us stick to this view
Okay let us because the iid assumption
is made throughout Let us stick to this
view that we are given n random
variables one sample of each all of
which are independent statistically and
identically distributed Okay Now this
methodology that Im going to talk about
right now is applicable irrespective of
the kind of data that you see in the
sense that it can be a supervised
problem it can be an unsupervised
problem or or so on right which means
that you can have label you cant have
label and this method methodology is is
applicable to problems where you are
estimating marginalss or if youre
estimating the joint distribution if
youre estimating the conditional It
doesnt matter Okay that is why I will
make it generalized in a sense that
suppose we are given
suppose we have
n samples
so drawn ID
So lets say that we have uh D which is
Ill use uh
another notation here V sub 1 E2
V3 up to V N and this is drawn ID
from a distribution uh Ill write the
density P V
So note that this v can be px pxy px
given y py given x anything depends upon
what the underlying problem is I the
treatment now will be general Okay
Now the goal
is to
estimate PV
given D
Uh this is our goal
Now we know the recipe
Assume
P theta
which can be evaluated at B as see this
V is a dummy variable by the way P theta
as B as the model density
and compute K divergence Now
between
P V and P theta
Okay By assuming that we are dealing
with continuous random variables this
is given by the integral
of
PV
log
divided by P theta evaluated at V and
you have DV here and this is over the
space that these these random variables
are defined Lets assume that these uh
all vi are in some d dimensional real
space
Okay thats the most general
observation assumption that we made
This is what it is Right Now what are
we interested in Remember the recipe
again So we want our theta star or the
optimal parameters to be the one that
minimizes
the kale divergence between
and p theta
Correct So this optimization is over
theta and you
let us uh open this term out and we have
this integral
PV log PV
The second term is
uh minus integral
p v log p theta
So integral is a linear operator and Im
just I can open the log and write this
as uh uh push the integral after the
negative sign So note that this first
term right this term can be completely
ignored Why
This is independent of theta
theta is the optimization variable and
the first term is independent of that
theta which is the optimization
variable Now how do you interpret this
So Im saying that
this is the entropy of data
I can do nothing about it
This data is given to me See if I if I
have to minimize the the divergence or
uh the divergence metric between PVA and
P theta the only thing that I can play
with is P theta not PB because thats
entropy of data and I have no control
over it So I can just knock that term
off Okay Now this will be
want to minimize
the negative of the integral
EV
log P theta P DV
this is the optimization problem that I
want to solve now
okay
now remember in the first class somebody
asked a question that we arent we
begging the problem here because we
started the the entire process by saying
that we dont know PV
right now when we dont know PV whats
the way to compute this integral two
things the first thing is this integral
is intractable in RD its in very high
dimensions its very hard to compute
other thing is that we dont even know
what PV is thats the whole problem that
we are trying to solve so how do we
solve this problem we use statistics so
we can write this as
arg min
is the negative of whats this integral
This integral is expectation of
correct So by definition this integral
is nothing but the expectation of log p
theta
with respect to pv
Okay
Now again can we compute this
expectation No we cant But here
comes the the biggest twist in detail
that statisticians tell us that
expectations can be approximated using
samples
So if you want to compute the
expectation of a particular function
with respect to a distribution and all
that you have are samples from that
distribution then you can approximate
that expectation using
something you know something that is
computable and theres a theorem that
guarantees you that if you have large
amount of samples then this estimate
that you have actually converges to the
true expectation in probability Whats
this uh theorem
 Law of large numbers So lets invoke
that Okay So if we invoke the law of
large numbers
you tell me which one Weak law of large
numbers
From the law of large numbers we have
Expectation of log of P theta V respect
to PV
can be approximated by whats the
estimator
expect what is the estimator that would
estimate the expectation
its the sample mean okay sample mean is
given by 1 by Then
log of P theta of VI
where
VI
is sampled ID from PV
only if this happens law of large number
works So you have to ensure that all
the samples that you have are drawn IID
from a particular distribution Right
So now can we compute this quantity Now
we can because we know what P theta of
VI is because thats what we have
defined and we have samples from V PB
thats it So now law of large number
says that this particular estimator
converges to the true expectation
as
now you know Why AI works only with
terabytes of data Its lot of large
numbers
What you are actually doing is trying to
approximate an estimate an expectation
using sample average
and uh statistics tell us tells us that
that only works if you have lot of
samples right So what is the infinity
that is known to human beings The
entire internet
train your models on the entire
internet Thats the story This existed
centuries before What did not exist is
that we could not traverse this arrow
Right So this reminds me of a story
right In in a class of mathematics
It was being told that uh there are
infinite numbers between these two
right
and a student came and did this and said
I just crossed infinity
right anyway right so what what we what
what are we doing is that by considering
a large amount of samples uh we are
approximating the expectation using
sample averages now our optimization
problem boils down to the following so
we want to seek the minimizer
Minimizer of the negative of
where VI is sampled IID from PV
This became our estimator
but in fact youll be surprised to know
that even charge GPT is trained using
the same equation
This is exactly what is done So now how
is the optimization problem solved and
what P theta is being used is different
Okay Now this is what I call as the
minimal scale divergence estimator
Makes sense right Because all we are
doing is just if you trace back what we
did started from the definition of scale
divergence right The estimator that we
have gotten for the parameters theta is
the one that minimizes the kale
divergence between
the true distribution and the model
distribution What the indices and
 come again
K and L What do they say
 Oh I I thought I mentioned they are the
names Kilbach and Ller two people Okay
Kale divergence In fact the
generalized version of it is what is
called as an F divergence and Kale
divergence is one member of that large
family So Kale divergences Kale
divergence has its problems Its not
the best divergence to be used
Surprisingly this is what is being used
even today and it sort of empirically
works Okay So this is the minimal care
divergence estimator Any questions so
far
 Which one
 Oh here is it Okay So the question is
why is why are we considering KL between
PV and P theta and not P theta and PV
So typically in literature no this is
called as forward kale The term that
you refer to is called a reverse scale
Okay Now if you take reverse scale
you will have a term that you cannot
compute
You can see that no because there will
be a p theta
log PV term We cant do anything about
it Thats why we use the forward cable
No this is the expectation right this
is the see okay um suppose theres a
random variable this goes to uh the
foundations of probability theory
suppose there exists a random variable
Okay maybe Ill write it here
So look at this There is a law called
law the law of unconscious statistician
or lotus it is abbreviated as Now
suppose x is a random variable and f of
x is a function of a random variable
So typically or not typically right
always the function of a random variable
will have a different distribution
compared to the random the the original
random variable Now if I were to talk
about the expectation of the function of
the random variable its actually equal
to the
uh expectation of that new random
variable with respect to the
distribution of that new random
variable However it can be shown that
expectation of a function of a random
variable with respect to its
distribution is equal to the expectation
of the function of the random variable
with respect to the original random
variable This is lotus It can be
proved I think it should have been done
in stom probability theory classes
Right Its a okay so what Im saying is
show this result
prove this
will
fix that in next class I told them

maybe try to just uh push it a little or
something
Okay that is what it is Yeah Uh
therefore see uh if you look at if you
uh consider that
then the expectation that we are trying
to estimate is the expectation of this
function of the random variable V So
this is that f of x that I wrote So log
of p theta of v is a function of the
random variable v So we are look we are
looking to estimate the expectation of
function of a random variable with
respect to the underlying distribution
of the random variable and we look at
the sample averages and law of large
numbers tells you that uh the sample
average will converge to the true
expectation as n tends to infinity

Okay
Anything else Okay Now this is what I
call as the uh the minimal dail
estimator But we also know that uh that
I can write this as
the max
or theta of this particular function
correct
because
okay now Ill introduce some nom
remember I told you that if p theta
is the model distribution that we have
assumed over uh the true data If you
evaluate that at a particular point
I gave a name for this If you evaluate
the density function at a point
it is called the likelihood
Density functions being evaluated at a
point is called likelihood Okay Now
what is this We are trying to find an
estimator theta that would maximize the
likelihood of all data points under the
model Thats one another interpretation
of this and thats why this estimator is
also called
the maximum likelihood estimator
So I can do the entire math in a
different way So what Ill say that is
that P theta of VI
okay is the likelihood of VI under P
theta So what I want to do is to find
the theta that would maximize the
likelihood for the entire data set This
is for one data point If I have to do
it for the entire data set what should
I have to do Ill have to consider the
joint distribution
with respect to all the random variables
that we have and I have n of them
See our interpretation is that our data
set has n random variables which are all
iid Correct If I have to consider the
joint distribution between n random
variables that are iid how do I do
that
Product right So I the the total
joint likelihood of data Let me write
that
the joint likelihood
of the data
So let me call that as L of D is given
by the product
of
all the distributions right uh
right because they are I
okay now what do I need this is a
function of theta of course I need to
maximize the uh
likelihood of this you know joint
likelihood of data
now I dont like products
so Ill take Ill Ill go through Ill
make this go through a monotonic
function
and log is one such thing So what Ill
do is that maximizing this is equivalent
to maximizing the log of the likelihood
of this
If I do that then this will get
converted into a sum
Okay then I seek theta star as the one
that would maximize
a scaled version of this
And people call this the maximum
likelihood estimator
Im not a big fan of this
because
why should you maximize the likelihood
To me this estimator is the one that
minimizes scale divergence
Mathematically they are exactly the
same same thing right The one that
maximizes the likelihood over the data
is the one that minimizes the K
divergence between the true distribution
and the model distribution I would like
to see that as the minim the minim the
minimal K divergence estimator but I
will call it as maximum likelihood
estimator to ensure that that Im
following the convention
 exactly the same no thats why I wrote
the math as well but remember that all
we are doing is minimizing the K
divergence between the model
distribution and the distribution even
when we maximize
the so called likelihood
Okay
 Oh I assumption is always made and law
of large numbers tells you that that
this is a this is this is a good minimiz
this is a good estimator for the
minimizer Thats it See the handwavy
explanation that people give is the
following Right What is P theta of V
P theta of V is the likelihood of
obtaining V under T theta So what do we
need We need a model that would
maximize the likelihood of obtaining
this particular data set and thats why
we maximize the likelihood of uh this
particular data set under the model
distribution and we seek the parameter
in such a way that this would maximize
it So thats thats the handway
explanation that is given why should
this be a good estimator and so on is a
different question altogether but I like
to see that as the one that minimizes
the distribution of divergence between
the true and the model distribution
Okay
Now one question that remains is any any
questions so far Okay See one Yeah
 Less likely an event is the more
information it gives us So if we have a
data set which is very less likely
 and if we maximize the likelihood
it should give us a better like it will
end up giving us a worse model for the
entire thing but it but as per more
information
 okay uh Ill
sort of answer your question but Ill
make a comment with your uh permission
This is precisely why I dont want to
see this as uh uh maximum likelihood
estimator because theres no
theres no mathematically grounded
interpretation to what is being done So
to your question see look at what
likelihood are we maximizing We are
maximizing the likelihood of seeing the
data
computed under the model distribution
that we want to maximize
You understand So given that uh I am
treating my data coming from the model
distribution give me that model
distribution
which would maximize the entropy sorry
which will maximize the likelihood not
entropy
Okay Yeah But again as I said uh
seeing this as maximizing the likelihood
is not something that Im a fan of I
want to see this as the one that
minimizes the clear divergence
Okay
So wherever you see this maximum
likelihood estimator remember that its
the minim minimal K divergence
estimator
Okay Uh we will stop here and continue
in the next lecture
