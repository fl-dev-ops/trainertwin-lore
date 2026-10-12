---
id: nd3laZj5Cdg
title: Lec 66 GAN - Generative Adversarial Networks
url: https://www.youtube.com/watch?v=nd3laZj5Cdg
date: '2026-04-09'
duration: 41:51
model: youtube-captions (en-orig)
transcript: true
---

# Lec 66 GAN - Generative Adversarial Networks

## Transcript


Okay in this class
we will look at generative adversarial
networks
Remember what the story was So we have
uh
uh a random variable that we are
sampling from Lets assume that we are
sampling from normal distribution
because typically what happens is
that the data that we get have will will
will mostly have infinite support So
we dont want to start from a
uniform random variable that has finite
support We would like to start from a
random variable that has infinite
support So
typically in all these generative models
the Z which is the uh random variable
that is being transformed is taken to
be uni is taken to be normally
distributed not uniform Okay Cuz we
assume that we also know how to sample
from normal distribution because we know
the deterministic transformation Okay
So then we have to
learn the underlying function
This goes as an input to a neural
network now
And this neural network
is that function that I was talking
about
which will give you samples from
Correct So this is any neural network
So you take a neural network and the
reason I have drawn this neural network
this way is that I said Z is always in
RK which is less than uh K is less than
D Therefore you need to increase the
dimensions of this neural network
right Because you need to get to the D
dimensions from K dimensions Thats why
the shape
Okay
Uh now this is a neural network So
now what do we have to do
We will have to ensure that this P theta
of X
is close to
PX in distribution
How do we do that We minimize our
divergence metric Right
Now in this generative adversarial
network the underlying
distribu divergence metric that gets
minimized is what is called as an F
divergence Specifically one specific
form of this F F divergence called the
Jensen Shannon divergence
Now uh why would that uh how would you
minimize that F divergence function or a
Jensen Shannon divergence is a matter of
detail Meaning you know as I said
Ill Ill do it in the in the next
course
What will happen algorithmically is what
Ill show So what we should do right
now is get this theta okay that would
minimize

 some divergence metric okay which is
typically what is called as the F
divergence between
PX and P theta
Now KL divergence also happens to be a
uh special case of the F divergence
F divergence will give you a family of
infinite divergence metrics of which
KL reverse forward reverse KL
Jensen Shannon chi squared everything
becomes a special member of this family
Okay
Now how do you solve this optimization
problem Remember that
we cannot compute this KL divergence
because we dont know what PX is
Correct Do we know what P theta is
We dont know what P theta is
However we can get samples from P
theta
How
By I mean do a forward pass through
this neural network you will get
samples from P theta
You get samples from P theta right So
we have Now the question is given that
we have samples from PX and samples from
P theta estimate this divergence
metric
It turns out that this divergence metric
is not tractable It cannot be computed
So what did we do in the variational
methods in the EM method
We constructed bounds on the divergence
metric
which is the evidence lower bound And
instead of optimizing the
the actual divergence metric we
optimize a bound on it Exact same
technique
occurs here
So here is the here is the you know
the outline of how the entire math works
out Ill not do the math in this
course But the the math works out that
when you construct a bound on this F
divergence
the bound will take a form where there
will be
linear combination of two expectations
And these two expectations are taken
over P theta and PX respectively So
what will happen is this divergence
metric right This the bound on this
divergence metric will have a form where
you will have an expectation of some
function over PX
plus
an expectation of another function
over P theta
Okay And these two functions
can be computable
Okay There will be some computing
functions that can be computed and
there are expectations over PX and P
theta What is this This is the bound
that we compute on the divergence metric
that we would want to minimize
You get what Im saying
Now these expectations can be estimated
using samples
Why
Law of large numbers
You invoke law of large numbers and say
that Look these expectations now can
be estimated because I have samples from
PX I have samples from P theta Thats
it And this becomes the loss function
for the the so called loss function for
the entire generative model
That is the Thats how the math works
out to be I will not do that Ill just
write down this so called loss function
and tell you how to
how to do it algorithmically because
its a part of your third assignment
Did you get what is happening So the
principle is that we will minimize the
divergence metric Okay we cannot
minimize the divergence metric because
of the intractability of PX and P theta
We construct a bound which is the
variational bound
Okay And that bound finally turns out
to be a sum of expectations two
expectations where the first
expectation is with respect to
the true distribution and the second
expectation is with respect to
the generated distribution as as it is
called Some people also call this the
true distribution and the fake
distribution and so on right So true
data fake data or whatever
Okay
Is it okay
So now
Maybe I should have written this
This is I think log of
the exact form Is it

 I think this is how it is
turn out to be Just give me a second
Ill come See the point is Ill Ill
tell you why this is not of importance
I told you that there there is a family
of divergence metrics right
Depending upon what family of divergence
metric that you choose
the functional form of these things
inside the expectation changes
Right
In fact I can choose a divergence
metric that would give this to be
exactly of this form okay But there is
one particular
uh divergence metric that would that is
called the generative adversarial
network which will go to this I think
this is uh log of D and let me just
confirm this once
Log of 1 minus this yeah
Yeah
I think this is that
this is that case where you make an
approximation so that the underlying
mode collapse problem will go away I
think yeah thats not what we are
looking at The naive thing will be log
of
1 minus
D fee of X cap
Okay
Now okay what is this uh
what is this uh loss function is Please
remember that this loss function is
the bound on the divergence metric that
you would want to optimize Now how do
we go from here from from here to here
is in the initial lecture of the next
course okay But take it for granted
that we construct a
a bound on this divergence metric and
we end up getting this sort of a thing
Now here
we know what X is X uh X is our data
points and we know how to compute this
expectation
What What is X cap X cap is the output
of this neural network G That also we
know What is this D
Right There is this function D okay
So now this D is another neural network
that
we construct here
Okay
Where does this D come from
See this D comes up
when we construct the lower bound on the
divergence metric
Okay Here is how it happens
Now the lower bound that we construct
on this Okay let me actually do the
math I think a little bit of math so
that its complete
Okay
Now what we want to do is minimize
this right Theta star
is
minimum minimize this
divergence metric
Okay We cannot minimize this divergence
metric What will happen is this will
become
an approximate optimization approximate
opti
optimization over theta and we construct
a bound on this Some
Okay
Now this bound on DF
I need to keep pushing this
This bound on DF
itself will be an optimization problem
Okay Over
What happens is
theres a function that you are trying
to optimize
So please pay attention here
Cuz Im only giving you the sketch of
the math Im not doing the entire math
So there is a there is a function that
you are trying to optimize Correct
And we cannot optimize that function
with respect to the particular
parameters because of intractability
What we do is we construct a bound
Okay On that objective function that we
are optimizing
That bound that we construct okay
Itself involves an optimization problem
over another class of functions
Do you see what Im saying
So so DF is the function that we are
trying to optimize We cannot optimize
that So we construct a bound on DF
Now this bound on DF consist consist of
another optimization for function
optimization problem over other class
another class of functions
You see what Im saying
Do you understand Now these class of
functions
are what
are approximated using another neural
network here
So should I say tell you the thing
again So there is a function that that
there is an objective function that you
are tried that we are trying to optimize
with respect to one set of parameters
Okay
We cannot optimize that and thats why
we construct a bound on top of it
Right And while constructing that
bound well have to solve another
optimization problem with respect to
another set of functions
That is what I have written as this max
over L of theta
 comma phi
Now its like this First you solve
this inner optimization problem to
construct the bound
And once you construct the bound you
minimize that with respect to another
set of variables theta Thats it
Do you see
So these are again saddle point
problems These sort of problems are
called saddle point optimization
problems where theres one objective
function and there are two optimization
variables So you are seeking the
extremum point of that objective
function which is maximized with respect
to one set of parameters at the exact
same point minimizes with respect to
other set of parameters Thats why its
called a saddle
Typically in an optimization problem
you avoid saddle points
But here is an optimization problem
where you deliberately seek saddle
points because thats how the problem is
constructed Thats why training GANs is
hard
You might have heard that training GANs
are today generally what was serial
networks is not the
the state of the art model for
generation is because of this that you
are deliberately seeking for a saddle
point which is a hard problem to solve
in higher dimensions
We are using exact we are using the same
SGD Adam etc to solve this Well come
to Ill come to that in a while Right
Now please understand how this problem
is constructed first Right So we
the the goal is to
sample from the underlying distribution
Okay And the principle is to find this
the parameters of this G function such
that
the divergence metric is minimized We
cannot minimize this divergence metric
Therefore we construct a bound on it
And while we construct that bound the
bound itself becomes
solution to another optimization problem
with with which involves another class
of functions
Right And thats why the final problem
that we would solve is we seek phi star
and theta star okay That are optima
of this particular function
Now what is this phi Where is this phi
coming from
So what is this theta
Theta is the parameters of that function
which would map
the Gaussian random variable to random
variable of interest And therefore
its also called a generator
The generator function is the one that
transforms
the arbitrary random variable to random
variable of interest Right Where does
this Where does this phi coming from
So this phi are the parameters of those
set of functions okay That would
define the bound on the
divergence metric that we are trying to
optimize
Understood
Any questions on this
Yeah
Its not a latent variable right
Because its its the parameters of
another set of functions Its not a
latent variable
So typically latent variable is a
variable that is not observed right In
the in the in the in the random variable
itself in the in the space of sample
space itself
Thats a thats an additional random
variable that you introduce Here its a
function
So phi are the parameters of class of
functions that you would try to
optimize What are these functions
What do you mean by what are these
functions As in do we have some
assumption about their functional form
Yes depends upon what divergence metric
that you use
Typically algorithmically what is done
is this is approximated using another
neural network
Okay
What is to be controlled is you have to
control the
the output of this particular function
How do you control the output of a
neural network
How do you control the output of any
Suppose you want a neural network to
give numbers between 0 and 1 What do
you do
Huh
No no no You want your neural network
to output a number between 0 and 1 What
do you do
Activations right Choose your
activations appropriately Thats it
Have a neural network choose its
outermost layer appropriately And what
does that output layer depend upon It
depends upon what is the divergence
measure that you are choosing Thats
it
Okay Hold on For one particular
divergence measure called the
Jensen Shannon divergence this function
D right Uh or this function that we
are talking about has the range between
0 and 1
For this one particular divergence
metric that we choose Which Ill show
Ill show one particular instantiation
of this entire uh class of uh models
But I want you to understand how did we
arrive at this particular
type of uh saddle point objective
function Thats it
Okay I Well spend some time on it
Please tell me if you understood the
underlying
principles of how did we arrive at this
Let me repeat again Shall I
What did we do I I hope that you
understand this construct right How
did we get this construct
This you understand right Uh
Now we want to get the parameters
theta okay In such a way that a
particular divergence metric is
minimized And while we are optimizing
that divergence metric we want to
compute this divergence which we cannot
Okay You have to take my word for it
We cannot compute this divergence
metric And what is the mathematical
workaround The mathematical workaround
is is to construct a bound on this
divergence metric
While we construct that bound on the
divergence metric this bound itself
involves solving another optimization
problem with respect to another set of
functions
And those set of functions we define
using another parametric family of
functions called D phi
So
solving or rather getting a sampler now
is equivalent to solving this inner
optimization problem to get the bound on
the divergence metric
Once you solve that you solve the
outer optimization problem that would
minimize the divergence between Px and P
theta Thats it
Questions on this
Yeah
What P What P What What What did we
introduce
Phi phi Okay okay Thats Thats
correct
Oh you want to justify your previous
comments Okay See its
In in in literature it is called it is
not a latent variable because its the
parameter of the model See model
parameters are definitely latent So
you take a neural network
Do you want to call the parameters of a
neural network latent variable
Typically in a non Bayesian setting you
dont want to treat your parameters as
random variables
Unless you take Bayesian neural networks
kind of setting where you make your
parameters themselves random variables
Right In the non parametric cases or
non Bayesian cases you dont want to
call your neural network itself a
parameter of neural networks are a
latent variable
Right
If you are saying that okay it is an it
is an unknown information that we are
introducing to the model of Of sure
But dont call it a latent variable
because thats that has a different
connotation Thats it
Okay
Why is
it inherent information that is already
present in the
data
Dont call it a latent variable It is
what you are saying Yes it is
something that will give you the bound
Thats it
You had another question I suppose
Yeah
Do we solve the optimization problem
to tighten the bound Yes Thats
correct Yes So this uh the inner of
the In fact we will show that there
well show the existence proof also
Well show that there exists a
particular D
okay for which the inner bound will
will become tight
Is it somewhat similar to the EM
case where we could not have a
It is similar to the EM case but in the
EM case the bound does not depend on
solving another So the bound does not
uh involve solving another optimization
problem
Yes Yes If you do not know Q we will
do what is called as variational
inferencing which is VAE which is
even that does not involve uh solving an
inner optimization problem Thats how
it they are different Its a good
observation by the way Yeah Its It
is similar to EM in the sense that you
cannot solve the uh the divergence
metric construct a bound and solve it
But the bound construction of bound
itself involves an optimization problem
here which is not the case with EM
Thats it
Anything else Yeah Unlike the case
where we had a one to one mapping of
the P theta function
with whatever loss function we define
here we can we do not have a formula
Like whichever parametric form of the
distribution of P theta we
We are not making any parametric
assumption here right So this is
implicit
P theta is is implicitly coming from G
Whatever function that this neural
network imposes is what what what are
the P thetas We dont even know what P
theta is
Right Thats why I call it an implicit
generative model because
all you are learning is to sample
without even knowing what P theta is
Youre implicitly estimating PX not
explicitly
Yeah
So regarding the loss function what
exactly is it measuring Because we look
at other loss functions like MSE and
MAE So its measuring the distance
See here it is
measuring the divergence between two
distributions Thats it Thats it
See even MSE and MAE are that no
But MSE and MAE given two points say
like X No no no
MSE
See you start from from a probabilistic
standpoint it is still uh KL
divergence See KL divergence under
certain distributional assumptions
boil down to MSE and MAE Thats it
Right But if you want a deterministic
way of looking at this loss function as
well I will give you one hand wavy
explanation that is seen everywhere in
blog posts when when they describe what
GAN is
Okay Ill Ill talk about that as well
But from a probabilistic standpoint
remember whats happening We are still
minimizing the divergence metric
In this case a bound on it
Right
Okay
Anything else
Yeah
This P theta is coming from the P theta
distribution Correct Let us say G
theta is a neural network And so P
theta is means the ERA and the
underlying distribution Is it the same
or is it No no
Youre asking what P theta is Is P
theta is whatever neural network
imposes Thats it Yeah yeah yeah
You dont know what that is
But you want that to be closer to PX
Thats it
Probabilistic approach that we see in
the discriminative model
where I used the KL divergence Huh we
are using some other divergence here
So why we choose KL divergence
I see Uh see there are every
divergence metric has a particular
property You know for instance KL
divergence has this property that it is
not symmetric
So that translates to some degenerative
properties in generative modeling
So for instance if you want the
details right What happens is KL will
ensure that you will cover the support
of the underlying distribution but it
will not ensure that the model is not
sampling from uh the part that is
outside of the support of the
distribution
Right And reverse KL has a reverse
reverse KL has a reverse behavior and
we want some balance between those two
Thats why we choose a other divergence
metric
Okay So now we will see what happens
algorithmically So what In in one
particular case right Uh if
the F divergence is chosen to be this
particular divergence called
Jensen Shannon divergence
See L theta comma phi
will take this particular form
Yeah for this particular case of uh the
divergence metric
L theta uh phi will take this particular
form Okay Now where do you see theta
in this uh loss function It has to
depend both on theta and phi right
Where is the dependence on theta here
Huh
X cap right X cap is G theta of Z
Right Thats why its its dependent
on So here X cap
is G theta of Z
Okay Now let us look at how this is
done in an algorithmic way So now what
happens is given
the data set D
Mhm
You want to write it down Okay
Ill write it again perhaps No
problem So this Z
is sampled from normal 0 1
We have this neural network which is
called the generator neural network G
theta of Z
Youre getting X cap here
And we have another neural network
This neural network is the one that is
used to construct the bound
Right So it will take uh X and X cap
both as input and it will give
a value between 0 and 1
For this particular divergence metric
If its for a different particular
divergence metric the output of this
particular neural network will be
different So typically this neural
network is called the generator neural
network
And this neural network is called
the critique neural network
Critique or discriminator Some people
call it critique some people call it
discriminator Okay
So let us write write down the loss
function So what we want is we we are
seeking theta star and phi star
that would
minimize and maximize this particular
loss function simultaneously right
Or alternatively its a saddle point
problem that we are solving L is equal
to
the expectation of log of
D phi computed at X where X is coming
from PX
Plus
expectation of What was it Log of
1 minus
D that is computed at X cap Let me
write it as G theta of Z
And this expectation is taken over
X cap coming from P theta
This is the loss function right Now
how do we solve this How do you How do
we construct this algorithmically as
follows right
So take
a batch of data
Okay
Sample a few points from Z and pass it
through G theta What do you get
You get some points of X cap So now
you have some points of X which is data
a few points of X cap
that is
generated data
Okay Now
do
to compute this expectation How is this
expectation computed You can
approximate this by 1 by
N
I is 1 through N
log of D phi of Xi correct
This is how you approximate this using
invoke the law of large numbers and
similarly for the next term as well
Now what you should What What What one
should do is take a batch of data the
input data
And generate a few samples of X cap So
now you have a few samples of X and you
sample a few samples of X cap How do
you generate How do you get a few
samples of X cap
By doing a forward pass
through generator
Okay with the current theta Okay Then
pass all those samples of X through the
critique
What do you get
You compute D phi of X
You see this
Okay Then take all those X caps and
pass it through the same
critique and compute D phi of G theta of
Z or D phi of X cap
Now we have both the terms that we
need
Compute them here
And then do one backward pass through D
phi and update phi
Thats one pass through discriminator
Do you understand
Now
one Then Then you have to solve the
optimization problem on generator And
by the way for discriminator youll
have to take the negative of this and
then optimize no Because youre
solving the maximization problem here
Right Then to optimize for
the generator what do you have to do
Take some samples of X pass it to the
discriminator
Compute this particular first term
Actually for the generator you dont
have to compute this first term because
the first term is independent of theta
You only take some points of
Z and pass it through the generator get
your X cap
pass it through the discriminator find
this X compute this term and back
propagate all the way from discriminator
to the generator by keeping fee a
constant Thats it Thats one backward
pass through generator And
keep doing this alternatively
Thats GAN training
Let me Do we have to repeat or did you
understand Its the only two loss terms
and two neural networks right So
compute the appropriate loss terms do
forward pass and backward pass
appropriately Thats it
Of course I mean this is simply
gradient descent
No When you are optimizing for fee
keep theta constant When youre
optimizing for theta keep fee constant
Its an alternate optimization
Saddle point right Given one
particular set of parameters youre
looking for the saddle for the other
thing and youre youre alternating
That is for only convex convex cases We
are not even close to convex cases here
And none of the problems that we solve
in machine learning are convex
So all the results that we have for
convexity of gradient descent does not
apply here at all
Did you get how to train this
Yeah
Batch wise sampling no We have data
Just take one batch of data
Yes So if you take a batch size of 32
you take 32 data points from the input
data data set and take generate 32
Zs and generate them And you do one
pass through both
discriminator and generator
Okay And then you do one epoch You do
multiple epochs on the entire data Just
like you train any other neural network
you do this
Is it okay
It is actually trained simultaneously
You train generator solve this inner
optimization problem by keeping fee a
constant and then train that and do it
alternatively In fact the ratio is not
1 to 1
Typically you train the the generator
more and discriminator less
It or the other way dont depending
upon what your model is and so on
Thats it
Absolutely
not They are not related because
everything we are doing at the
distributional level not at a sample
level at all
Okay Now once you do this once you
train this
how do you use it during inference
During inference you discard the critic
completely
You take Z and pass it through G theta
If you have done it properly then the
samples that you get at the output of
the G theta has to be the samples from
PX
That is what this this person does not
exist as It is actually trained again
And this is there in your assignment
When I trained my first GAN right in
2016 15 times it was amazing to look
at those new non existent pictures being
generated
Is that all right
Now
to answer your question right What
does this actually mean from a
deterministic I could have
talked about this GAN completely without
even talking about distributional
minimization from this angle Ill tell
you how
Look at what is this doing See think
of this discriminator See what is this
discriminator
It is taking X and X cap as input and
giving you a number between 0 and 1
Anything that gives you a number between
0 and 1 can be
interpreted as a classifier
Or rather this discriminator is is
giving you a probability
Okay Now log of D fee of X is what
It is the No it is the probability of
And this expectation is with respect to
PX
So this is nothing but the entropy
negative of the entropy of
the random variable that will give you
the probability of this particular X
coming from the true data
So D fee of X you you interpret this
When When does this D fee of X will
maximize If if it gives one it will
get maximized When would it When would
it give one When it is coming from the
true data
If its coming from true data
then this is maximizing
Okay And what is this What is 1 minus D
fee of What is D fee of X cap
D fee of X cap is the probability that X
cap
is coming from
the generated data
What is 1 minus that
It is probability that its not coming
from it I want to maximize that
So these two terms are saying that this
discriminator now has to
maximize the probability of X coming
from true data and X cap coming
X cap not coming from true data
So this discriminator has to become a
good critic a good classifier
Right And what is this generator trying
to do It is trying to minimize the
exact same loss function
Which is saying that make this
classifier
not a good classifier
Make this classifier fail
Now when would this classifier So what
is this classifying between What is
this discriminator trying to classify
between
It is trying to classify between PX the
samples of PX and samples of P theta
When would the classification becomes
difficult
If PX and P theta become the exact same
distribution
Thats what this generator is trying to
do
So as they say
this generator is trying to fool the
discriminator and vice versa
So that is why the name adversaries
So this generator and discrim See any
saddle point optimization problem is an
adversarial optimization problem because
you have an objective function and two
different set of parameters that are
trying to
optimize it in two different directions
Okay So if you want
a folklore way of looking at it its
that okay this discriminator is trying
to fool the generator and the generator
is trying to fool the discriminator and
so on Because this loss function can be
seen as maximizing the probability that
this discriminator is trying to find out
whether the data is coming from the true
distribution or the so called fake or
generated distribution And this
generator is trying to undo what this
discriminator is trying to do which is
When would this classifier Its like
this no People tell you the story that
oh look at this you know is this X
cap is coming
So this discriminator is trying to see
whether this X X cap is coming from true
data or not
As long as this can
successfully
discriminate between true data and the
fake data then this generator is not
generating properly The moment it stops
becoming a good critic then you have
fooled this thing enough so that you are
generating from the true distribution is
the story And they write this loss
function saying that this is the thing
that would maximize the probability of
discriminating maximizing the
probability that it comes from true
data this coming not coming from true
data then you maximize this And then
you write a minimization saying that
that would You mean because the
generator wants to undo what the
discriminator is doing If discriminator
is maximizing a loss function then the
generator has to minimize that loss
function And that is why you have a min
max min max min max problem here is how
people present it
I am not a big fan of that at all I
mean it all looks like a hand wavy
story
Whats actually happening is this
Right You start from
minimizing uh
a divergence metric construct a bound
on it The bound involves another
optimization problem which is
parameterized using another neural
network See this discriminator story
comes as a consequence of solving this
nice mathematical construct You should
not begin from it
Right That Thats my way of looking at
things Anyway you you understood that
This is what a GAN is right Generative
adversarial networks
Right Where uh the idea is Let me
summarize what we did today
Generative models are samplers We are
still estimating the underlying
distribution So how do we do that
Start from
a
an arbitrary random variable that we
know how to sample from and pass it
through
a discriminative function whose
parameters are learnable
Now the idea is to set the parameters
of this deterministic function which is
a neural network in our case in such a
way that a divergence metric between the
true distribution and the distribution
that this
this deterministic function is imposing
on the underlying arbitrary random
variable is minimized
Okay This is the principle that is
behind all generative models you know
be it a GAN or a VAE or LLMs
everything So well see different ways
of solving this problem
In what is called as generative
adversarial networks what we do is we
choose this family of divergence metrics
called F divergences And if you choose
F divergences then minimizing that
divergence minimization becomes
intractable and therefore we construct
bounds on it While constructing the
bound to construct the bound well
have to solve another optimization
problem that involves
a class of functions
Okay That is again uh
approximated using another set of neural
networks
Okay Now you first construct the bound
by solving an optimization problem And
once you construct that bound you
minimize the divergence metric the
bound on the divergence metric So that
involves solving two optimization
problems on the same objective function
and the inner optimization problem
becomes a a maximization by construction
and the outer one becomes minimization
and thats why you end up getting
a saddle point problem which is also
called an adversarial optimization
Okay this is the general principle of
what is called as F divergence
minimizers So theyre called
variational divergence minimizers That
is how I introduce this uh topic in the
next next next course
A special case of it is what is called
as a generative adversarial network
where the chosen F divergence is
Jensen Shannon divergence If you choose
that particular uh divergence as a
divergence metric the underlying uh
bound on the objective function or the
divergence metric will take this
particular form which can be interpreted
as a classifier
And we saw how to optimize this right
You know theres one pass through the
generator you compute the loss function
and just the the exact same gradient
descent methods that we were using we
will use that Post training you disc
you discard the discriminator
completely
See critiques are only used till you
learn See teachers are only
My teacher always used to say this This
is something that I uh you know keep
quoting everywhere He used to tell me
that a good teacher is one who becomes
redundant after some time
Right So the What is the definition of
a good teacher Is that after a while
you should not see the need for a
teacher
The point is you become independent I
mean thats what good parenting is also
about all about right You know you
make your dependent so independent that
you they dont have to come to you
So this critic is a good critic if it
has helped you to end up in the actual
distribution so that during inference
you dont have to use it anymore
Discard the discriminator or the critic
completely Sample from the arbitrary
random variable pass it through the
generator and what you get are the
samples from the underlying
distribution Thats the idea
Okay Youll be asked to implement this
in your third assignment on the data set
that we have given and its its its
fun to do that This is GANs So next
class we will look at two other class
of generative models One is the
variational autoencoders and then
the
um
autoregressive models also called as
large language models
Okay Thank you
