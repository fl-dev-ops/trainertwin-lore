---
id: -y3SSAIhD4Y
title: Lec 16 Bayes Classifier
url: https://www.youtube.com/watch?v=-y3SSAIhD4Y
date: '2026-01-28'
duration: 35:36
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Lec 16 Bayes Classifier

## Transcript

speaker_1: Welcome everyone What h
minimizes the true risk
for
the above scenario
So by above scenario I mean we have a
binary classification problem and the
loss function is a 01 loss function So
for that particular case what uh
hypothesis minimizes the true risk
Okay So give you the answer The answer
is
consider
a hypothesis

And by the way uh one can use uh
the name of classifiers and regressors
for this hypothesis as well So this
hypothesis
function is what is called as a
classifier isnt it
If y is discrete if y is continuous this
is what the regressor is This is what
your classifier or regressor is Okay
So consider a hypothesis function or a
classifier in this case because we are
looking at a binary classification
problem defined as follows
So lets call that hb of x
This is equal to this is the definition
of this function This is equal to class
0 if
the posterior of
y equals 0 given x
is greater than posterior of y equals 1 given
x
it chooses the other class otherwise
Ill also write that maybe
if
procedure of y equals 1 given x
is
greater than or equal to so Im uh
breaking the tie arbitrarily there is no
sanctity to this you know which one
should I have to use the break the tie
is breaken broken arbitrarily So this
is how I choose So I define a
classifier or a hypothesis that
would assign class zero if the posterior
of Y equal to 0 given that particular X
is larger than posterior of Y equal to 1
given X and the other class otherwise
So it just looks at the posterior of Y
for evaluates it for both the classes
and it b it chooses the class based on
which one is higher Seems like a
rational thing to do
Right So if if if you have access to
computing this by the way we are
assuming that we are we have access to
all distributions that we need and we
have a way to compute this is what we
have assumed correct So if I have
access to compute this I can define a
classifier this way
where I decide based on the postcl class
posteriors
Is that okay Now uh this classifier is
what is known as the bias classifier
named after the famous statistician
base It is called the base classifier
The claim is
risk associated with the base classifier
is always less than
any other classifier for all classifiers
that you can consider
which means that this is the optimal
classifier
If you are solving a binary
classification problem then you cannot
do better than base classifier

 in terms of minimizing the risk See
this result
okay is general enough for a large class
of problems
but I will prove that for the case of
binary classification problem with 01
loss because thats the easiest
okay similar results can be proved for
regression problems and they can be
proved for uh uh kclass classification
problems and so on Okay well
well see that Ill Ill state some of
those results without proof but this
one we will see Is the statement clear
that the question that we asked is what
H minimizes the true risk for the above
scenario and the answer is the one that
decides this way It is called the base
classifier This function minimizes the
true risk is the claim So let us prove
that right Yeah
 We didnt derive this hypothesis
function from
 can do that as well
 Okay The question is uh how did B come
up with this and then show that it is
the least uh its a classifier with
least risk Cant you do the other way
around Meaning start from the
definition of risk Okay and deduce
that this is the classifier that
minimizes the risk can be done Its
algebra Ill show you that Okay When
we do the when we walk through the
proof we will see that you can start
from the definition of risk and derive
this result as well
 Yes you can Okay uh I mean you you
have to uh do a bit of uh variational
calculus and function function
approximation sorry function analysis to
do this because see look at this no this
optimization that we solve right the
problem of risk minimization
the true risk minimization this this is
an optimization over functions
functional function spaces see we know
how to differentiate with respect to
variables right we have learned calculus
do we know how to differentiate with
respect to functions
I mean mathematicians do its called
variational calculus We can
differentiate with respect to functions
So you need a bit of variational
calculus to derive some of these results
because see this is an integral as we
will see because its an expectation So
typically if youre looking at
continuous random variables the risk
becomes an integral in some high
dimensional space So and uh that
involves this hypothesis So what youre
actually looking at is the derivative of
an integral with respect to a function
Get it We dont know how to do it At
least people who have studied high
school calculus or undergrad calculus
dont know it unless you have actually
studied variational calculus that you
need to differentiate integrals with
respect to functions
Okay thats why I dont take that
route The way it is generally shown is
that you know you assume that you know
the result and then show that this is
correct
Any other question
Okay let us show that now
 snorts and cough
Okay
proof
Its a cute little proof So lets do
that
Let
s I of H
denote
all X in RD
such that
my classifier
assigns class I to it So I is either
zero or one
Did you get the notation What am I
doing is Im taking RD
which has all my data I partition this
RD into two non over overlapping sets
Okay Ill also write that
s0 of h does not intersect with h1 of s1
of h
and the union of these two
is
this RD
What is this What is this set by the
way This set is set of all data points
in RD that gets labeled as class one
under the classifier H So you take a
classifier and see what all points in RD
are being classified as class one that
is S1 of H So you take all points that
are being classified as class zero under
this classifier H that are S0 of H
 Come again
Ah here No this should be zero
Okay
 Come again
 Subset of RD Right Yeah Correct
Yeah Union will be
it is in RD Okay Intersection is null

Okay So this is how I partition RD into
two points Now so this this is for
every H So you take any H in the
hypothesis set you can partition uh RD
into these two partitions right Okay
 Okay Come again So I think it has to
be all the examples of
put
one example
 Okay See the the question is suppose
you take
everything in the distribution then it
is RD So if you only take samples from
the data set then it is a subset of RD
Depends on how do you want to see it
Okay Because we are considering the
true risk Its okay if we say that we
consider all points in RD Thats the
only difference Okay Or if you take
data set then it is there are some
points that are never considered because
they are not in your data set Thats
it Lets take the entire distribution
because we are not looking at empirical
risk here Were looking at true risk
Its okay No Okay Now um
see one other side note is I do I need
that result now uh
I dont but anyway Ill note
that risk
in for this particular case is the
probability of the indicator that h of x
is not equal to y
Why Its because of the following Let
me just actually use this result in a
different way So what is the risk for
this particular case with 01 loss for a
binary classification problem It is the
expectation of
the loss function
under the fan distribution Okay Now
this loss function
is an indicator random variable
Why Because it can take two values
right with certain probabilities So
what is the expectation of an indicator
random variable It is the probability
that it takes one of the values Thats
it So thats why the risk is equal to
the probability See we have defined the
risk as one So if you look at risk as
an indicator random variable then that
risk sorry the loss function as an
indicator random variable loss function
takes value one its a Bernoli random
variable it takes value one if the
hypothesis is not matching with the true
label
correct and thats why I say probability
of this uh this this particular thing
anyway its a side note so um
so which is equal to which is equal to
So the probability of
the indicator
that this is
write it here where
I
is
an indicator random variable
Bernoli random variable
thats simply algebra right this is what
it is So lets write that So what is
this equal to This probability
can be split into so this event right
the event of uh h of x not being equal
to y can happen in two ways
One when the true class is one and the
classifier predicts it it as zero and
the other way Okay lets write that
This is equal to the probability
of
h of x
predicting y and y equals 0
plus
the probability of h of x is 0 and y equals
1
Why could you add these two
probabilities
 Yeah disjoint Okay Now this is equal
to the probability of
X being in S1 of H
and Y being equal to 0
plus
X being in a zero and Y equals 1
because that is how we have defined uh
these two sets Correct
Now this is equal to
theres a joint distribution I will
write the joint distribution as a
product of uh marginal and conditional
equal to P probability of Y being equal
to zero times
the
conditional distribution of X given Y as
X is in S1 of H given y equals 0
right plus
conditional distribution
actually yeah so when I condition this
is x is in s0 of h given y equals 1 is this
clear simply using the definition that
the joint is equal to the product of
marginal and conditions thats

 Is this clear Why are we writing this
So now uh
this is equal to
probability of Y equal to0 What is
this What is see we have taken X to be
in RD as a continuous random variable
Right So now if you want to actually
this is uh
not equal I have to write PD because
this is a probability that Im looking
at Okay Ill have to compute that
probability So I have to compute this
probability for a condition continuous
random variable What do I do So if I
have to compute the probability of a
particular random variable being in a
set how do I compute it for a
conditional random variable
 Integrate the PDF We have to integrate
the PDF So lets do that So this is
the integral of the PDF

 y equals 0
dx
 plus
you have to write this as this because
whenever I write a conditional
distribution right its always that the
conditioning random variable is fixed at
a particular point right this is what it
is uh and this integral is over what set
 this This is over S1 of H and this is
over S0 of H
And note that these two are two
different distributions
two different conditionals Okay By
definition this is what it is right

Okay Now look at this integral Now we
know see we are computing
the sum of two integrals Okay and
integrating these two integrals over two
disjoint sets
Okay Now for each X in RD
when you compute this through risk
only one of these two integrals will get
integrated No will be considered Why
is that Every X will either belong to
S1 or to S0 Therefore when you compute
this entire risk for each X either of
them will get evaluated
Correct So let me write that since
S1 of H
does not intersect with S S0 of H
for every X in RD

You only consider one of the two
integrals
So we are computing this risk right Uh
now s we are integrating this over s1
and we are integrating this over s not
right What is integral I mean you can
look into that roughly as taking all
points in x and computing this and
adding them Correct infinite decimal
So lets take an X in RD So if you want
to compute the risk associated with it
you will either evaluate this integral
or this integral depending upon what
that classifier does on that particular
point You cannot compute you cannot
take both the terms
Correct Thats what Im saying because
S1 of H and S S not of H does not
intersect with each other Is this clear
to all of you Because this is the crux
of the proof Theres only one step that
remains now Okay Now
can somebody tell me amongst these two
integrals which would be computed at EX
Did you understand the question
So we you all agree that for each X one
of the two will be evaluated right
Which one will be evaluated for for each
X
 Depends on depends on H depends on h
Okay Now if h chooses s1 then the first
integral will be evaluated
If it chooses s not then the second
integral will be evaluated Thats it
depending upon what your h does Now
this is so far this is uh same for any
hypothesis for the particular case of
base classifier
Now look at this integral and tell me
which one would be chosen in the case of
base integral So let me write that this
thing you know so that it is clear So
this r of h is given by the integral

of
uh p of y equals 0 times
sorry its the density right px given y
 equals 0
Plus
okay this is what we have right this is
the risk now uh now for the case of base
classifier
which of the two integrals will get
evaluated so this is over s uh one is it
this is over s1 this is over s not
correct uh now for base classifier which
one will get evaluated
No
 no no It depends upon what the true
class is No See remember what base
classifier is Base classifier always
chooses
based on
 the posterior It choose to chooses
based on posterior Whichever posterior
is the highest it will choose that
particular class If that is done then
which one of these two integrals will be
evaluated at each x for the base
classifier Just think about it for 30
seconds Ill tell you the answer
 Did you get the
question
The question is so Ill just write down
no hb chooses
or hb is equal to 1 if
y equals 1 given x is greater than
If I want I can extend this This
implies what is p of y given 1 y y equals 1
given x use
use base law is equal to x given y equals 1 times
p of
Now tell me now tell me which of the
these two terms will be evaluated for
this particular classifier
 Oh what do you mean by right side
 For for what case
 For one
 Huh If the true class is one
 then which will which which one will get
evaluated
depends on what base classifier does
Okay the question that Im asking is
that okay so let me just tell you the
answer So always for the base
classifier
the term that is the least of these two
will get evaluated
Why is that
What is S1
S1 are those cases for which the base
classifier
or any classifier chooses class one
When does base classifier choose class
one When this product is greater than
this other product
And whatever is within the integral over
the set of S1 is the one that is minimum
of these two Isnt it
 Yes
 Shall I repeat
 Yes
 This is the key point What is S1 S1 is
the set Okay Of all Xs on for which
classifier says one When does base
classifier say one Base classifier says
one when this product is greater than
this product
Which means that whatever is within the
the integrant when you are considering
set S1 is the minimum of these two
Do you see that And the same thing can
be said for the the other class as well
When when does the base classifier
choose S0 It chooses S0 Let us write
that right Choose S0 if
P of
X given Y equals 0 times P of Y equals 0 is greater
than
P of X given Y equals 1 times P of Y equals 1 Isnt
it
Which implies
R of HB is equal to you take the
integral over all RD What do you take
You consider the minimum of
Does all of you see this argument
Are we done with the proof
Are we done with the proof So we are
because
these two terms are non negative
because they are either probabilities or
density function being evaluated at a
point which is non negative always So
if youre integrating
functions that are non negative and at
all points if you choose in such a way
that you always take the minimum out of
two quantities
then it should be the minimum amongst
all possible choices of h isnt it Yes
Thats it Therefore
okay
So this this result says that
one cannot do better than a base
classifier
no matter what in terms of minimizing
the risk So if you choose your classes
based on the posterior of the labels
given data and you choose make the
classes to be the one that has the
maximum posterior then you achieve the
least possible risk
Okay
It says that you cannot design a
classifier that is better than a base
classifier
Now this is a theoretical result Okay
But what is the problem here in
practice Can you build a base
classifier
You cant Why
 You dont know the distributions Now it
boils down into a distribution
estimation problem
So to build a base classifier you need
to estimate the
these distributions So now given some
data you can cast the problem of ML as
that of building a best classifier and
to build a base classifier you need to
solve the problem of maximum likelihood
distribution because you need
distributions You get it Now the other
way to look at it is as follows right
you remember that u when I was uh doing
uh discussing maximum likelihood
estimation I told you that we are
interested in obtaining p of y given x
whats the reason the reason is this
that we are interested in building a
base classifier
and we estimate the posterior of y given
x okay so now this result is for the
case where the loss function is 01 one
loss and the
problem is that of binary
classification
Okay can I extend this result
Turns out that you can Ill give you
one case where instead of solving a
binary classification problem suppose
you are solving a generalized
classification problem with K classes
Got it So in this case what is the what
should be the base classifier look like
So there are k possible classes which
means that you can compute the posterior
of when you compute posterior of y given
x it will be a a k dimensional uh
discrete random variable that can take
values 1 to k with probabilities p1 to
pk or whatever right there are k
probabilities base classifier is the one
that assigns that particular class which
has the highest posterior amongst all
possible classes
just like we did it for the case of uh
the binary classification you extend
that for Kclass classification it can be
shown using the same argument that the
best classifier in terms of achieving
the minimum minimum risk when you use 01
loss function is a best classifier for
the case of Kclass classification as
well please take it as a homework and do
it
you get it similar argument you can just
use the same argument here okay that is
one result
integration
is the minimum right
theres only
 are you telling me how to solve it
 try try it out so you write it down Ive
told what the classifier is write down
the algebra and see if you can do it
its its pretty straightforward you
know given this okay try it out once now
the question is how does this extend to
regression problems
Do you understand Suppose instead of
having a classification problem suppose
I use regression problem
Okay And so note that the true risk
minimizer of the risk Sorry the
minimizer of the true risk depends upon
the choice of loss function as well
Correct Now suppose we choose our loss
function to the loss function as the
squared error loss
and we take up the problem of regression
where Y is in R
or RK Can you guess what would be the
optimal min risk minimizer
Just a guess
 No no its a function It should be a
function of X No see this is this base
classifier is a function of X H the
hypothesis the optimal minimizer of the
risk has to be a function of X
Huh
Exactly It will be the conditional
expectation of y given x
Ill start the next class by writing
that result You understood Suppose I
choose my loss function to be squared
error and the the problem that Im
solving is that of regression Then the
optimizer of the true risk will be the
conditional expectation of y given x I
think you might have done this in your
sto right This was a result that was
shown in the pro in the first first
course of probability theory If you
have if you dont recall it go back and
look at your books Okay So what am I
saying is this is the
minimizer of
the expected
So this is a standard probab problem in
probability theory right you can show
that if you can actually show this okay
show that this minimizer is equal to
this conditional expectation
okay anyway
so
maybe let it be there
 very much no very much I told you so
this result is very much depend on loss
function so now again other question
that is taken in statistical learning
theory is suppose you choose a loss
function okay
what is the optimal base classifier or
what is the optimal risk minimizer
sometimes you can analytically find that
out sometimes you cant but why did we
do all this so what is the what is the
reason behind doing all this is that
again summarizing this particular class
so what did we show is that we showed I
mean we looked at the the method of
empirical risk minimization as the
problem of machine learning where you
are given data define a loss function
compute the expected loss over the
distribution and you cant solve that
minim minimize the true risk You take
an empirical version of it and then
minimize that So thats your hypothesis
or the classifier or regressor Now one
central question is when and how would
the minimizer of the empirical risk
convers to the minimizer of the true
risk Okay most times this question may
or may not be answered
but we saw equivalence between empirical
risk minimization and distribution
estimation Okay continuing that I also
showed that for the case of 01 loss
function and uh binary classification or
kclass classification problems the true
the minimizer of the true risk is the
conditional distribution of labels given
data
So why was this result even proved I
mean and this particular classifier that
chooses based on the posterior of labels
given data is called the base classifier
and no other classifier can do better
than the W classifier
Now why did we do that is to again
reinforce the connection between the
distribution estimation uh framework and
empirical minimization framework because
the next question that well be asking
in the coming classes is how do we
realize a base classifier
So what do we mean by that How do you
build a best classifier given data to
build a best classifier We need the
conditional distribution to be
estimated Now that becomes a
distribution estimation problem So
either you can directly estimate the
posterior distribution right using some
model or
you can estimate the uh the okay so the
what happens is now you can directly
estimate P of Y given X or you estimate
P of X given Y and P of Y and combine
them to create a classifier
So for the next few classes we will look
at a few methods okay or algorithmic
methods to estimate a distribution given
data We have already told you that a
maximum likelihood estimation is one way
to do it Okay So for a few particular
cases of uh the assumed underlying
density uh this optimization problem
that we solve in maximum likelihood
estimation is not tractable in a sense
What am I saying is that suppose you
take your p theta to be this class of
density functions called mixture
densities You cannot differentiate that
and put it to zero and find out the
optimal parameters You need to resort
to numerical methods to solve it
Theres an algorithm called expectation
maximization algorithm or EM We will
look at that em and well also look at
class of methods called map estimators
where you assume your parameters fun
parameters
also to be a random variables and you
compute posteriors on top of it So next
set of lectures will be on estimation
theory We will specifically look at the
ML estimation that we have already seen
and a few examples and we look at the
map estimation and uh ML estimation for
the case of mixture density which is
called Y algorithm Thats what the next
class is going to be Uh yeah so thanks
for attending this class I see you in
the next time
