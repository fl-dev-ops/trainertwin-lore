---
id: 0RCDPOz3YVc
title: Lec 31 Bias - Variance Decomposition and Analysis
url: https://www.youtube.com/watch?v=0RCDPOz3YVc
date: '2026-02-18'
duration: 46:36
model: youtube-captions (en-orig)
transcript: true
---

## Transcript

Okay So welcome to this lecture Uh
in todays lecture we will look at uh a
central theme in machine learning So
the idea that we discussed today applies
to all the algorithms that we have seen
so far and the ones that well see later
in the course as well So its a
central theme in machine learning where
the idea is that of generalizability
So the question is you are given some
data you build some classifier on top of
it or some hypothesis on top of it The
actual question is how does this perform
on data
that has not been seen
Okay Because its not important uh to
just explain whatever you have seen
Whats of value is to predict something
that is unseen So always so thats why
theres a profession around it Right
So if you predict if you do it well
youre valued You mean think of
predicting uh stock market think of
predicting you know what economy and
all that If you predict well on unseen
data you are valued So the whole point
in machine learning if you go back to
our example of X rays
an algorithm should not only do well on
the data that it has been given it
should also predict on unseen data So
now the central question of machine
learning is how do these algorithms
perform on unseen data This question is
called the question of generalization
Okay So typically what happens is the
following So lets write down
generalization
Typically we are given data
which are
So we assume that we are solving uh the
problem of uh
classification or supervised learning
sorry supervised learning and these
ideas are extend can be extended to
unsupervised learning as well Uh same
same ideas So we are given end data
point at a sampled ID from an unknown
distribution This is our starting point
right
and what do we do We find the
hypothesis by solving the
problem of risk minimization So we want
to minimize the uh expected loss
function whatever loss function that we
defined
This is the problem that we solve and we
solve this problem over
a class of hypothesis functions and
since we do not know the underlying
distribution instead of solving that we
solve an empirical
surrogate of this and call that the
empirical risk minimization Right Now
because of that which means that because
since we are not solving the true
problem which is the problem of
minimizing the expected uh loss with
respect to the underlying distribution
since we do not know the distribution
but what we solve is the following
problem right which is har
cap which is the minimizer of
this particular surrogate
Correct This is the empirical risk
minimization problem Since we do this
theres no guarantee that the minimizer
of the empirical risk
converges to the minimizer of the true
risk So what is the consequence of
this The consequence of this is that
even if you have minimized the empirical
risk well it does not guarantee that
you would do well on the entire
distribution
Okay we will study that So what
happens is
as follows So uh suppose we have two
samples of data Okay One we call as D
train
is drawn ID from PX PXY And there is
another sample of
data
x i dash yi dash
These are again samples drawn iid from
px pxy
Okay So what are we doing here We
construct two samples of data sets
Okay Which are you just sample two
different sets of data from the same
underlying distribution Call one the
training data set Call the other the
test data set Okay Now perform erm
on drain
Right We find a particular hypothesis
by solving uh the erm problem on d
train The question is
we train to obtain
lets say har capex
The question is how would
perform
on d test
So this is the central question Now
suppose you have solved the erm on one
particular sample of data called the
training data How does it perform on
some other sample of data which is
called the test data Now why is it not
obvious that something that you have
trained on or something that you have
solved using drain
why should it not perform well on D test
since both remember that both of them
have been sampled from the exact same
distribution
While both these data sets are coming
from the exact same distribution why is
it the case that uh the solution for erm
on one particular sample of data should
not perform well on the other sample of
data
that is because of the very nature of
the problem that we are solving Had we
solved this particular problem which is
the true risk minimization where we take
an expectation over the entire
distribution then there is no question
I mean anything that you you can take
any sample of data as long as you are
sampling from pxy it does well and now
since we are solving a surrogate which
is the empirical version of it okay
doing well on this particular one
particular sample of data okay does not
mean that it does well on the other
sample of data so thats the point
unless you have this n tending to
infinity
okay now todays models do very well on
unseen data because this n is very very
large
but in most cases right in most problems
this n will not be large since you are
doing a sampling from pxy the question
is how does a minimizer of the empirical
risk does well on some other unseen part
of data now I talked of performance here
right so what is performance performance
are any kind of metric now if you are
solving a classification problem it can
be accuracy metric okay or it can be uh
you know there are suppose youre
solving a binary classification problem
then you have a 2x2 matrix right two
classes real real classes and the
predicted classes and there are two
types of errors that are possible right
which is called type one or type two
error and they are also called false
false positives and false negatives
depending upon that you can define
metrics there are metrics called
precision recall okay and uh uh you take
the mean harmonic mean of precision and
recall okay thats one other metric its
called the F1 score f is the mean of
precision and recall Basically they
are ratios of these four possible
combinations right One is false
positive false negative true positive
and true negative Different ratios
depending upon what your problem
specification is You compute that
typically for classification problems
people look at precision recall and f1
score which is the mean of precision
and recall Please study those metrics
So thats what I mean by performance So
now the thing is you have a particular
harstar cap that you have found out that
you have uh come up with on training
data Whatever metric you want to
compute you compute So compute the same
on test D test and see what happens And
by the way the practice is
the training okay or solving this
optimization problem should always be
done on drain Okay and you fix or
freeze your classifier while you are
doing a test on D test
You should not try non dest or rather
the data set on which you find your har
should not be destat
data leakage In fact Ill tell you the
way to do it is now that we are talking
so algorithms will have I mean any
machine learning algorithm will have two
components to it right One one are the
parameters the others are the
hyperparameters If you go to the GMM
example parameters are those means
variances and alphas What are
hyperparameters Hyperparameters are
things like how many yeah the capital M
how many gshian components that we are
looking at So if youre looking at
logistic regression right what sort of
sigmoid function that you are using
these choices are called hyperparameter
choices Okay which are not in fact I
mean mathematically putting you dont
optimize over hyperparameters
you optimize over parameters Now when
you solve the optimization problem you
solve it using d train Typically when
you are given 100 samples of data the
way to do it is you split that data into
three parts One part is the train the
other part is the test There is one
other small part which is called the
validation data So it is on this
validation data that you
fix your hyperparameters
So basically you solve the optimization
problem on the train part Okay And
test it or compute the accuracy on the
validation part Depending upon that you
tweak your hyperparameters and retrain
and iterate between the drain and
devalidation You should never even see
test data In fact even to do
hyperparameter testing hyper
hyperparameter tuning thats called test
data leakage
because if you I mean your algorithm is
not knowing the not seeing the data
directly but you know you as a
practitioner is indirectly giving inputs
to your algorithm to tweak
hyperparameters even that becomes
training that becomes like training on
test data You should never do that
Given data the best practice is split
your data into three parts Two parts
use for training One on one for
parameters the other for
hyperparameters which is the training
and the validation data The third part
you never even look at it Thats called
the test data That this is how you do
it typically right Okay Now the
central question is minimizer I mean
well generalize this idea right The
minimizer of the empirical risk on one
particular sample of data from the
distribution How would it perform on
some other sample of the data that is
sampled from the same distribution is
the question So this is called
generalization The ability of the
minimizer of an empirical risk to
perform well on unseen data Well
according to when I say well it is
according to any performance metric that
you have defined on the other sample of
the underlying distribution is what is
called as the generalizability of the
algorithm Okay An algorithm has to be
generalized Note that we are not even
talking of nonid data here
We are saying the data is still IIAD
The data is still sampled from the same
underlying distribution But we have two
samples of data sets sampled from the
exact same distribution Now how does it
perform on two different instances is
the question Theres a theres a whole
field on how would it do on nonID data
as well So we we are not looking at it
yet Okay
Right Okay So let us look at uh how to
so what we will do right now is that we
will study uh this question in a
systematic way Okay So Ill tell you
what what we are going to do in the rest
of the class We will look at the
problem of uh risk minimization the true
risk minimization
and decompose okay the true risk into
two parts One part is called the bias
the other part is called the variance
And we will see when you solve the
problem of empirical risk minimization
how would these two parts of the errors
behave
Okay And I will do this for the
particular case of squared error loss
Okay And this sort of a result can be
uh derived for any kind of loss
function But Ill do it only for the
squared error loss in this particular
class Is that all right That is what
we are going to do now Okay So let us
study this Basically well study this
question How do how would HR cap
perform on D test is what we will see
Well generalize the idea now
Okay Uh
consider
a loss function L
which operates on the cross productduct
of H of X and Y and
its to R plus This is the loss
function But for this particular case
we were we are looking at the squared
error loss which is
h of x minus y
the norm squared we are assuming here
that x is in some rd and for ease well
assume that y is in r So its a
regression problem that way Okay
Now what is the definition of risk R of
H
is given as the expectation of the loss
function
which is h of x minus y²
and uh this expectation is with respect
to the joint density of x and y
This is what we are looking at So
before I continue uh see in this
particular lecture Im going to give you
a few homeworks uh that that I expect
you to solve Okay please do that Some
of them have been done in your previous
courses Uh but nevertheless Ill
mention them The first result that we
have to look at is
H star of X which is the
minimizer of
this particular risk under the squared
error loss
Theres a known result Okay this has a
particular form What is this equal to
This is the conditional expectation of
So please prove this as a take it as a
homework and do this
You have done this in your probability
theory course Okay So the result is as
follows right You take this uh
particular function expectation of uh h
of x minus y nom squared and this
expectation is with respect to pxy The
minimizer of this particular expression
is the conditional expectation
Okay please solve this This take this
as homework and do this So we will use
this result So what is this actually
saying is that suppose we are solving a
regression problem okay with squared
error loss then the minimizer of the
true risk is the conditional
expectation Now in a in a practical
setting uh we cannot get this why
because we dont have access to the
conditional distribution
had what is e of x e of uh expectation
of y given x what is this equal to this
is equal to integral
integrate over y this is y times p of
yeah this is the definition of
conditional expectation this is a
function of x Right
now we cant compute this in practice
because we dont have access to the
conditional distribution The posterior
of Y given X Okay But this is a
theoretical result that says that the
minimizer of the true risk Okay Under
the square loss is the conditional
expectation Okay So take this as a
homework and do this You know this is
you use your probability theory basics
and you can get this Okay
Okay So now well use this result of
define
HD of X
to be
a hypothesis or classifier
learned
using the data set D
Yeah So let HD be be the classifier
that we have gotten by solving So when
I say learn its
solve VRM So you are given a particular
data set D What is D D are finite
number of samples that are drawn from
PXY given a D You solve VRM on it and
you get a hypothesis right That we
call as HD Now
depending upon the particular choice of
D we have different HDs
Do you understand So its like I have
given you 10 data sets Okay
Not 10 data sets 10 uh yeah its see
when I we have been using this word
sample for the uh the iterations I mean
the individual data points in a data
set Now Im talking about lets go to
the mnest example
Suppose I give you 10 mnest data sets
Okay Every mn data set is uh what I
represent by d here Okay And you train
one classifier on each of them Thats
what Im talking about So HD is that
classifier or whatever the hypothesis
function that you have gotten by
training or solving erm on that
particular data set
Okay
Now let
P D be the distribution
according to which
we sample a data set from PXY
So Im defining another distribution PD
okay which is actually a discrete
distribution here because Im assuming
that there are finite number of uh data
sets or rather they are discrete and
what Im doing is Im sampling a data
set according to PD its like I roll a
dieice okay and depending upon what the
throw of the outcome of that dice is I
sample one data set from pxy and let
that that distribution that gowns what
data set comes up is what Im
representing by PD okay
Why do we need this Remember that our
whole goal is to analyze what is the
change okay in the performance of a
particular classifier or hypothesis
function under the change I mean under
different data sets So I need a
distribution over data sets as well
Thats why I have a PD here Okay Now
define
define an average
hypothesis
as
H bar of X
which is simply
the expectation of
HD of X where the expectation is with
respect to PD
Now what is this Im designing Im
getting one classifier per data set
Okay suppose I average all those
classifiers I get one classifier which
is called the average classifier Now
what does this even mean Okay Ill
give you a sort of uh see mathematically
this is well defined because we have a
distribution PD we have a hypothesis HD
and we can define expectation very
easily But intuitively what is this So
lets say that our our classes of
classifiers that we are considering are
linear linear classifiers Right Now I
have 10 linear classifiers All of them
are defined using one uh slope
component Right All lines are theta
transpose D Now think of this average
classifier as the one that you have
gotten by taking an average of all these
uh slope vectors of these 10
classifiers
Got it
Okay So now this is what I call by uh
the average classifier
Mathematically its a very well
definfined object right I mean its
just the expected expectation of this HD
uh over PD Did you get this idea what
an average classifier is Okay So we
need this huh
capitalis
or is it same or we are
 capital uh the question is does capital
D change for different hypothesis
function Yes In fact you get a
different you get new hypothesis with a
D
You get one data set solve VRM you get
one hypothesis You take another data
set you solve VRM you get another
hypothesis But please note that when I
say one data set other data set Im
not talking about MS C4 and all that
Im talking about data sets sampled from
the same underlying distribution
Okay
 All the what is the question All the
data sets are
 oh yeah see that is okay That is what
happens in practice See in practice you
wont get 10 data sets
Whatever analysis that we are doing is
the theoretical way of looking at it in
the sense that you call it train you
call it test doesnt matter All Im
saying is see in practice nobody will
give you uh 10 data sets People will
give you one you know one one data set
with lets say thousand samples You
have to split it into train and test
data set Thats how thats what you do
it pragmatically But theoretically
speaking we are assuming that we have
access to a lot of data sets Okay the
question is given that Ive trained on
one particular data set how does it
perform on the other unseen Thats it
So from that angle it can be train and
test but Im not talking about only two
here and Im looking at theory Im not
talking about two Im talking about
multiple possible data sets which are
sampled according to a distribution PD
 Yeah its erm Yeah
particular
 PD is the PD is the probability with
which we sample a data set from PXY
from same PXY we can sample multiple
data sets right so now PD is the
probability with which I sample a
particular data set from PXY okay
and by the way yeah uh every data set
may have different data point data
number of data points as well we have
not making any any such assumption Here
h is D is any such any any data set that
okay now okay so consider
 minimum number
 come again
 no criteria of the
 nothing so this is all now we have made
no assumption on anything right so
consider average risk
on all data sets
now the risk minimization problem that
we are sol that we were solving well
have another expectation
not the English expectation the uh
math expectation right the risk that we
would want to minimize right now will be
the expected risk okay
and this expectation is over PD now
right I want to minimize the expected
risk over all data sets
And you asked a question right does it
have to be the the empirical risk
minimizer or true risk minimizer for for
theoretical sense we can even assume
that its a true risk minimizer the HD
RHD because Im not putting RC cap here
right now okay now what we want to
minimize is the expected risk over
all possible data sets thats what I
want to do correct
now lets look at this this is equal to
the expected
expectation over PD So I just switched
the notations from uh distributions to
densities Okay Uh uh this is and what
is the definition of risk The
definition of risk is uh pxy and we have
h dx minus
y²
Yeah This is the definition of the
risk
So lets do some algebraic manipulations
here
PD expectation over VXY
Lets add and subtract that average
classifier
See this trick of adding and subtracting
a particular hypothesis
uh is a usual algebraic trick that is
used in a lot of uh lot of probability
theory results In fact I asked you to
prove that previous result as well that
also goes like this So youll have to
add and subtract that and then show the
show some of the expectations go to
zero So lets use the uh
other algebra and this will be
expectation
or pd expectation over pxy
this is um
hd of x minus h bar of x²
plus
H bar of x minus y²
plus the cross terms
2 times
Okay
Now this cross term
vanishes
and please take it as a homework and
show it
Yeah it its its algebra Okay this
cross term will simply vanish Ill tell
you how to do this right uh multiply
these okay expand the expectations and
group the terms that are independent of
a particular distribution okay and all
the terms will cancel away uh with one
another uh so youll this cross term
will vanish please do that take it as a
homework and complete the algebra
now what happens is we have
two terms Now RH
is equal to expected expectation
This PD this is with respect to pxy
hd of x minus h bar of x²
 yeah
h bar of x minus y²
okay
now here in the second term Right I
dropped expectation over PD Why
Because this is independent of uh the
data set
Is H bar of X independent of PD
Why Because we have integrated it out
Thats an expectation over PD right
So H bar is independent of that So
Ive taken that off Now lets consider
this particular term and expand it So
consider
Okay Explain this
Not this uh think well have to
pardon me not this term well have to
take
h bar of x minus y the other term
well keep that term as it is yeah so
consider h bar of x minus y square this
particular term this term is what we
consider right So this is equal to
the expectation of pxy
Uh now the same trick adding and
subtracting What do we add and
subtract We add and subtract har of x
What is h star of x
Minimizer of true risk Yeah Minimizer
of true risk True risk
Lot
of people pronounce risk as ricks
Yeah
Uh this we expand this
expectation bxy
uh please check the terms as Im writing
h of x minus y²
uh plus
expectation of uh h bar x minus h times x²
and uh the cross term is it correct
please
h bar of x minus
H star of X
times
Now what happens to cross term
It will vanish
Please dont assume that all cross terms
go to zero So again that is the case of
uh forfeiting by the way just because I
showed you two examples
where cross term goes to zero dont
assume that wherever you have cross
terms itll go to zero thats the first
lesson whatever you have done on your
training data will not generalize
that was a good joke okay so please show
that this is another homework show that
the cross term goes to zero now what
happens is uh we have three terms here
right So oh finally the risk that we
want to optimize
Yeah
 Huh
 No
Once you have sampled a particular data
set it doesnt depend on that right Y
is the random variable that you have
Once you have sampled its not its
independent of D H So now finally
collating all of the terms we have r of
h that we want to minimize well have
three terms
uh theres an expectation of
h bar of x minus h star of x
and square it So this was that first
term right This particular term
No Uh
yeah
What was that first term Can you tell
me This is H D
minus H bar HD minus H bar And uh
yeah there was this was the first term
correct And whats the second term now
The second term is
 expectation of
 uh
 huh h bar of x Yeah this is with
respect to pxy This is h star of x
minus Yeah this is respect to pxy And
what was the third term There was third
term also right Which was
 h
of x
 minus y And this expectation is with
respect to
 okay Yeah So this is the result This
is the uh most important result in the
entire course actually Right So the
risk the true risk can can be decomposed
into three terms Okay Theres a
squared here Okay Yeah
Here also
Okay It can be decomposed into three
particular terms
please I mean we will interpret all of
these very carefully Right Okay So
this first term
this term
is called the variance
variance of H Okay And this term
called the bias
And this is the
want to call it noise or whatever
right
Okay So let us interpret all three
very very carefully Okay Look at the
look at the third term first See third
term is telling me that I know that h of
x is my true minimizer Okay And y are
my labels Now
what is the expected error know that I
get by solving a risk minimization
problem
We have no control over this term
Okay See we can change HD we can
change H bar right Do we can we change
HAR We cant because once we fix a loss
function we have some data set HAR gets
fixed and Y gets fixed So this is
something that we do not have access I
mean control over and thats why its
called irreducible noise So no matter
what classifier or what hypothesis that
you design you will always get this
error And can somebody tell me what is
the source of this particular error
See lets go back to our uh X ray
example What is the source of this
particular error What can be the source
of this particular error
Exactly So its the label noise
Okay we dont have control over it
This is also called the label noise
Now if there is something wrong with
the labeling we dont even know if
there is something wrong with the
labeling because we dont have access to
pxy So we have no access to this and
we cant even control anything So this
is called the label noise which we cant
do anything about it Okay Now there
are two other terms that that we can
control Okay And in the um uh effort
towards minimizing the risk we would
want both of these terms to be as low as
possible because we want the LHS to be
possible and both and both of these are
expectations and we want both of them to
be as low as possible Okay So let us
look at both these terms and analyze
them very carefully So analysis of
bias and variance
Now consider
the bias term
So what is this This is
H bar x minus
h star of x Okay
Now what is this saying So what is h
bar of x
h bar of x is our our average
classifier Correct H bar of x is our
true classifier So what is this
difference telling us
is telling us how far is our average
classifier from the the reality or the
true classifier Okay So what does this
mean This means suppose
we have chosen our hypothesis family of
hypothesis okay to be lines or linear
models
In that case the question that Im
asking is if you had you
have had had access to infinite data
sets
okay and you can compute infinite
classifiers and take an average of it
How far is it from the reality
Now this tells you
the dependence of the classifier on the
particular choice of hypothesis that you
have making that you have made
independent of data Is this dependent
on data sets Its not dependent on data
sets See in the sense that it is not
telling you how sensitive your uh
classifier or ERM to the particular
choice of data set It is saying the
choice that I have about the classifier
how does it how far is it from the
reality
For instance suppose
your uh
actual distribution comes from lets say
quadratic with some perturbation some
quadratic function and you have some
perturbation thats your pxy
and you restrict your h you do erm with
linear models then that model would have
high bias why because no matter what
linear model you choose theres only so
much close that you can go to reality
does it make sense do you understand
what bias is okay its very important to
understand this right so u
this is quantifies
The
effect of
a particular
choice of
hypothesis class
This is what it does Suppose you have
made a choice for your classifier or
regressor How far is that from the
reality is what bias tells you
 Come again Yeah there is a square I
just wrote it that way Just to
interpret Yeah Any questions on this
This is actually a very key point Make
sure that you understand what these
terms are
 Very good question The question is
would universal approximators have zero
bias Yes Okay If they are parameter
rich
in the sense that even if its a uni
when does it see all universal
approximation results okay theyre
asymtotic in the sense that only for
instance GMM right you need infinite
components to make it a universal
approximator Now suppose you have
infinite component infinite mixtures
components in a GMM then of course its
a zero bias machine that way but in
practice you wont have that right but
thats a very nice observation that you
made Yeah So what is bias saying the
choice of the particular classifier that
you have made how far is it from the
reality Okay Now another point that I
wanted to make here is given a
particular problem machine learning
problem in practice can you measure bias
and variance you cant but there are
surrogates which Ill tell tell you
about okay why do you not why cant you
not uh compute bias and variance because
you neither know what har of x is nor
you know what the underlying
distribution is there is no way to do it
but there are surrogates to do it okay
this this is bias so lets look at
variance now so what is variance
 Go on
 Yeah Same thing right Yeah
Uh how does the variance term look This
uh variance term is
Can somebody just tell me Its
expectation of
Huh
Thats okay Uh
 H
 one second Uh H
 H
 uh
 okay
 Okay See here this is the variance
term Okay Now note that variance is
independent of the reality
It does not have har in it
Okay Now what is this measuring
See this is measuring the sensit
sensitivity of your classifier to the
change in data sets
I change one data set from the other
Right How does my minimizer HD okay
change If I change a particular data
set how does it deviate from the
average classifier
measures
the sensitivity
of the hypothesis
to the choice of data
See it doesnt care what my reality is
All that this is asking is suppose I
change from one data set to the other
How does my classifier change
Okay Now you know why both of these
have to be low
See I want my classifier HD it it has
to be close to the reality the true risk
minimizer and it should be not sensitive
to the choice of data set that I make
Do you understand now So I I mean
algebra tells us that this will happen I
mean the risk will be minimized only
when both of these are made
simultaneously small as low as possible
but in small sample cases theres a sort
of trade off between it and this is what
is called the bias variance dilemma or
trade off or whatever well look into
that that that happens with only small
pragmatic small models if you have
infinite samples and a large capacity uh
hypothesis then both bias and variances
can be simultaneously made small and
that is exactly whats happening in
todays uh genai methodologies because
you have very large models with a huge
number of data Okay But anyway
typically in small sample cases uh if
one is try to made uh lower the others
would be higher Well see how it is
Okay But did you understand the idea of
bias and variance Any questions on
this This is very important Bias
studies how far the learned classifier
is from the reality Varian studies how
sensitive is the learned hypothesis to
the change in data sets
Any questions on this Okay
Now let us look at what happens in
practice you know when we are trying to
uh minimize do an erm and try to
minimize the risk What happens in
practice specifically in small sample
cases Okay let us take an example and
see how it happens
And Im reiterating here the all the
analysis that Im doing right now is for
the squared error loss uh case and exact
same analysis can be done for any other
loss function Okay the algebra changes
of course the algebra changes but it can
be done Uh we will stop here and
continue in the next lecture
