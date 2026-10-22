---
id: BMj-TWtK83A
title: Lec 21 MLE for Latent Variable Models
url: https://www.youtube.com/watch?v=BMj-TWtK83A
date: '2026-02-03'
duration: 16:08
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

speaker_1: Welcome back to the lecture So the
question is uh maximum likelihood
estimation for ML estimation for latent
variable models
for a latent variable model
both the model parameters
and the density or Z needs to be
estimated
or the latent variable
needs to be estimated
Why Because of the very fact that the Z
is unknown unobserved So we dont know
what this is So we not only estimate
the parameters of the model we also
estimate the density over Z So we do it
jointly when we when we do a maximum
likelihood estimation for the latent
variable models So lets look at how
this turns out mathematically So we
have
the likelihood function
So Ill call that as L theta Okay Uh
for the notation sake So L theta L of
theta
is log
P theta of X This is the definition of
it And by the way
the math from now on Ill assume that
we only have one data point in our data
set
Ill do all the analysis by assuming
that we only have one data point because
of ease of algebra I mean everything
that we do can be extended to n data
points just by putting a summation
outside which runs from 1 to n Okay
But to minim I mean uh simplify the
algebra Ill assume that we only have
one data point Okay So log of p thetax
is the likelihood of x is a data point
that we have and log p thetax is the
data the u likelihood of that particular
data point Okay Now for the latent
variable model this is equal to log of
Ill assume that the latent variable is
discrete for now This is
P theta
of X and Z
Please note that in in a latent variable
model framework for every data point XI
you have one realization of the random
variable Z as well
Get it So for every image you have the
you know for if you take the example of
that handwritten digit that I just
cited Now for every image you have the
thickness of the digit and all that
right so for every x i there is a
corresponding zi but now since we are
looking at only one x that we have we
only have one z okay thats thats the
way to look at it so now this is what
the uh likelihood is p theta is now
marginal over these two
so remember that now our goal is not
only to estimate theta which are the
parameters but also to estimate a
density over Z because we dont know
what Z is Now suppose
 QZ
is some density over Z
Let qz represent some density over Z
Okay Now what happens L theta
This is the function that we want to
maximize Ill write that as
P theta X and Z
Ill just multiply and divide this qz
to this particular thing
Im simply introducing this density that
I want to estimate into the modeling
choice And because the density function
is non negative I can do this and
nothing changes Right
Now this is equal to log
time
p theta x and z divided by
qz
All right this is okay
Now what is this equal to See this
entire thing inside the parenthesis
is some function of Z Correct You can
look into that as a function of Z And
theres a function of Z and you have a
density over Z And this is theres a
summation over the random variable Z So
what is this entire thing Now its the
expectation right So this is the
expectation of
this is with respect to QZ
So remember that our problem was that we
had log of sum
coming going back to the the mission
density model right so we had log of
expectation as a sum so we have this log
of sum here we dont know how to deal
with log of sum we know how to deal with
sum of logs now you have log of
expectation we want expectations of log
can we do something about Right Turns
out we can not exactly but approximately
okay using something called ensense
inequality
So if we have
a concave function then we know that
expectation of a function is bounded by
the
function of expectation thats
inequality right so lets invoke that
right now here so we have
Just a second
Logarithm is a concave function right
This
we have uh
expectation of
log of p theta
Now uh which one is greater This is
that
this is correct
So this was the likelihood Okay And
lets call this as some uh f theta of q
I made it a function of q because
depending upon the choice of q that we
make this will take a different value
Correct So I wrote that as uh
a function of q

and this is the l theta that we would
want that we wanted to maximize
So far so good This is all algebra Any
questions on this
 Come again
 The density of Z does not does not
depend on the
we have chosen it that way See when I
say when I say theta
theta are the parameters of this I mean
technically I can write make it a
function of theta as well but Ive
chosen it to be a function of z thats
it
So when we take an example you will see
so its just notational convenience
thats it okay
probability mass function
 depends on the choice of z no if you
make your z to be a continuous random
variable then its a density function if
you make it a discrete random variable
its a mass function
 in this case its a mass function
 Ive made it yeah I do have I taken yeah
in this case its a mass function in
this case its a mass function yeah all
algebra will go through even if you
replace this with an integral
Okay same thing But yeah so see I I
deliberately took it as a mass function
because in our case of a mixture density
it is discrete The the latent variable
is discrete
 Being very precise you should write
expectation with respect to and not
just
 see uh again notational convenience I I
am used to writing expectations with
respect to densities
 Okay
 Right But yeah so some people write it
uh I write it with respect to densities
because if you write it with respect to
random variable you dont know what the
underlying density is no so I choose to
write it with respect to densities
thats it thats a notational
convenience is this okay so
what did we just do is that so this f
theta of q see we did two things okay
this f theta of q is now computable
Since we have log of
sum right no sum of log
has sum of log
type terms
The other interesting thing is so f
theta of q
is a lower bound
on l theta
l theta What is l theta l theta is the
log likelihood Correct
like
completely blank
like like Leehood Okay
mind is mostly an auto reggressive
model You see different conditioned on
the previous tokens it will generate
the next token So if there is an error
in the previous token it will not
generate the next token That was a
joke sighs and gasps
log this is log like L theta is log
likelihood Uh it is also called
evidence
Log likelihood is also called evidence
in literature So f theta of Q is a
lower bound on evidence Therefore its
evidence lower bound

 abbreviated as elbow
might have heard elbow optimization
right so basically its constructing a
lower bound on the log likelihood and
optimizing it thats it and this this
lower bound comes through uh the enson
inequality
okay now the new optimization problem
that we have is
we have theta star which is the optimal
parameters
So
originally we had
to find theta that would maximize the
likelihood Okay this is the original
problem
Now instead of this now well find our
theta stars that would maximize
not the likelihood function but a lower
bound on it
modified
new optimization problem
Now the question is while we want to
okay let me call that uh theta star cap
while while our objective is to maximize
the likelihood why are we maximizing the
lower bound instead
right come again
 maximize
 not necessarily see we are constructing
a lower bound not a higher upper bound
so when you maximize the lower bound
theres no guarantee about the original
function So what we are optimizing is
the lower bound on the function
right now Why are we doing it is
because in the cases of latent variable
models this is the best that we can do
because the actual likelihood function
is interactable as we saw We cannot
optimize that at all So what we do is
we construct a lower bound instead by
introducing another variable onto the
system and we optimize the lower bound
on it
Okay this is called elbow optimization
Okay where instead of uh optimizing uh
the likelihood function we are
optimizing the lower bound on it Now
the question is can we come up with an
algorithm that would guarantee something
okay uh about optimizing the original
function So EM algorithm is one such
algorithm that guarantees such such a uh
such an optimization uh uh procedure as
we will see now But remember that
instead of solving the original
optimization problem which is finding
the parameters by uh through maximizing
the likelihood function now we are
finding the parameters
by maximizing a lower bound on the
likelihood function Okay this f theta
q is the evidence lower bound that we
would optimize And please note that
this f theta q is a function of q which
is the choice of
 the density function that we choose on
uh the uh
hidden variable z
Now as you can see okay let me just do a
math and then tell you okay this is what
I wanted to say Uh we will stop here
and continue in the next lecture
