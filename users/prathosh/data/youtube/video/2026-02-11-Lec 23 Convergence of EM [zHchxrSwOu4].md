---
id: zHchxrSwOu4
title: Lec 23 Convergence of EM
url: https://www.youtube.com/watch?v=zHchxrSwOu4
date: '2026-02-11'
duration: 19:27
model: youtube-captions (en-orig)
transcript: true
---

# Lec 23 Convergence of EM

## Transcript


Okay welcome everyone We will continue
with the discussion on the EM algorithm
So for the sake of continuity well
reiterate the EM algorithm uh and then
well look at the uh the convergence
proof of the EM algorithm So recall
that So lets write down the
expectation maximization algorithm for
maximizing the likelihood
Expectation maximization algorithm
I in the EM algorithm the idea is to
maximize the clears throat and cough
log likelihood by maximizing the lower
bound that we have constructed So
please recall
that we constructed
a lower bound on the evidence that we
called as evidence lower bound which was
given by the expectation of log of
the joint distribution between the
observed and deent variable divided by
QZ and the expectation was with respect
to QZ and this distribution QZ D
we refer to that distribution as the
variational distribution for the
nominature wise
Now please note that
in the last class we also saw that the
optimal
the optimal value functional form for
the variational distribution is the
posterior of the latent variable given
data So we also saw this the last class
correct
Now EM algorithm is an iterative
algorithm that we saw So let us write
down the EM algorithm
EM
So before I write down the EM algorithm
there is a specific uh note that I have
to make here is that now suppose
we are constructing the variational
distribution at a particular theta
Okay we should note that the
variational distribution that we are
constructing is also a function of the
parameters theta
Okay therefore suppose
suppose we evaluate
the evidence lower bound f theta at some
theta t So what do I mean by that Ill
just clarify the notation first before
we go on So this means that we are
computing this particular expectation
is equal to the expectation of this
entire
function
Okay with
the variational distribution fix that

P theta T of
Z given X this is this will be my
notation I will know I will write that
as
f theta of q evaluated at theta being
equal to theta t
So when I write this what I mean to say
is that this f theta of Q the
variational distribution that Im
computing is being evaluated at theta
equal to theta t and the q function okay
or the variational distribution is set
with theta equal to theta t
Is this notation clear Because this is
very important because as we write down
the uh the m algorithm well have to
ensure that the notations are correct
So please note that this f which is the
variational distribution has sorry uh
the evidence lower bound has a
dependence on theta through this
numerator term and has a dependence on
Q So and the the Q function also is
dependent on theta So what I mean to
say is I can compute the the Q function
at a particular theta Okay I and I can
compute the evidence lower bound at a
different theta
Okay this is a key point that I that I
want you people to uh note because as we
write down the M algorithm we will use
this multiple times Okay so notation
wise let me rewrite it
Now Q of Z
can be evaluated
or rather Q of Z and
and F theta of Q can be evaluated
at at
different values of
parameters is
theta This is very important and uh
whenever I write the algorithm Ill
ensure that I use this So both of them
are functions of theta So one can
compute uh or evaluate these two
functions at different values of theta
So please remember this Okay Now with
this lets write down the the em
algorithm
Now em algorithm
Now initialize
theta 1 So we start with sum theta 1
This is what we have initialized with
Now for
t equals
1 to convergence
do the following Now note what we do
First we set the
t plus first variational distribution to be
equal to
the posterior
that is evaluated at theta t So please
note that we are operating at the tth
iteration and our goal is to find the
parameters for the t plus first
iteration So the goal is to find theta
t plus 1 To find theta t plus 1 we will
start at theta t
Oh sorry
this is z given x
Okay So the first thing to do uh in EM
algorithm is to find the variational
distribution at time t plus 1 and that is
given by the posterior that we have
computed at theta t the parameters that
we already have Okay Now what we do is
that we compute
 cough and clears throat
the evidence lower bound Okay using
qt plus 1 as the variational distribution
and you make it a function of theta
Okay what does this mean This means
you compute the expectation of log of p
theta x and z divided by
q t plus 1 Okay
this is with respect to t plus 1
So please note that this qt plus 1
has been computed using theta t as the
parameters
This evidence lower bound is still a
function of theta Why Because its
numerator has p theta x x in it
Does it make sense now Right So this
is the E step This is the E step in the
EM algorithm

 Okay Once we do this well find in the
mstep
find
theta t plus 1 Okay as
the maximizer
of
the lower bound that we have computed
using qt plus 1 as the variational
distribution This is the mstep
Now we got theta t plus 1 So this is end
for
so this is the em algorithm So what are
we doing We start with initialize with
some theta Okay At at at the t
iteration we find the variational
distribution So the goal is to find the
parameters at t plus 1 We find the
parameters at t plus 1 by first
constructing the variational t plus
first variational distribution as the
posterior with the current with the
current parameters and then we find out
the
lower bound on the evidence by computing
this particular expectation Okay
with respect to qt plus 1 that we have
constructed and this lower bound that we
have constructed now is a function of
theta as well Therefore we can optimize
that with respect to theta and in mstep
we find the next t plus 1 the parameter set
theta t plus 1 that we need as the one that
maximizes this evidence lower bound that
we have just constructed in the previous
step using the variational distribution
computed at t plus 1 Right And then we
get theta d plus 1 and we iterate
 Come again Compute
 Oh sorry Yeah this is I change the
rotation again Okay fine Thanks for
the correction This should be
this is Yeah its computed at QT plus
Thanks
Looks like Im cursed today Really bad
Okay So F theta of QT plus 1 This is
this is the M algorithm Is is it clear
now

 any questions here Okay So we are
Yeah So now we have to see why the EM
algorithm works Okay Which is the
convergence So this convergence
does not guarantee that the likelihood
keeps increasing So here is the
question What we are doing is we
constructed an iterative algorithm that
would maximize the lower bound on the
likelihood function that we would want
to optimize Now our actual original
goal is to maximize the likelihood Why
would this iterative algorithm lead to
our goal of maximizing the likelihood is
the question It turns out that this
particular iterative algorithm the way
we have constructed will ensure that the
likelihood function never decreases as
we get the new set of parameters So
that is what is uh referred to as the
convergence proof of the EM algorithm in
practice So we have to show the claim
is that with the EM algorithm that we
just saw the likelihood function that we
evaluate at theta t plus 1 is at least
equal to the likelihood function that we
have gotten at theta t So that is what
is to be shown Here is how the proof
goes So we are starting at theta t
right in the m algorithm we start with
theta t and we con we put qt plus 1 to be
equal to the posterior that we have
evaluated at theta t Correct Now
by construction
once you make the variational
distribution equal to the posterior we
know that the likelihood that we have
computed at or likelihood at theta t is
equal to the evidence lower bound
Does that make sense Okay So this
actually means yeah
so why is this true This is true
because
with QT plus 1 of if you compute the lower
bound okay such that the variational
distribution is equal to the posterior
then the lower bound will become tight
That is what we have seen in the last
class and therefore this equality holds
okay then in MTEP what do we do We
deliberately find theta t plus 1 such that
the lower bound that we have computed in
the previous step is maximized
right that is what the mstep will do So
what would that entail That entails
that if you take the lower bound that we
have computed with respect to QT plus 1 as
variational distribution and evaluate
that at theta t plus 1 then that is greater
than the the same function being
evaluated at theta equal to theta t
Why is that Thats because that is how
we have found the theta t plus 1 So please
recall the discussion that we just made
that this f theta is a function of theta
and you can evaluate that at a
particular theta Now once you get the
new theta which is theta t plus 1 if you
evaluate that function at theta t plus 1 by
construction you have ensured that the
elbow or the lower bound that you are
that you are evaluating at theta equal
to theta t plus 1 is greater than f theta
that you have evaluated at theta equal
to theta t And note that both of these
have been computed with the exact same
variational distributions which is QT plus
1 We are not changing the variational
distribution QT plus 1 We are only
maximizing that with respect to the
theta variable Okay Now if we combine
all of this okay
we also know that the uh at theta equal
to theta t plus 1 we will ensure that the
likelihood function that we compute at
theta t plus 1 is always greater than the
evidence lower bound because by
construction or through jensens
inequality it will ensure that the
evidence lower bound is always lower
bounded by uh
 likelihood
 the likelihood function
Okay this completes the proof This
ensures that the likelihood function
that we evaluate at theta t plus 1 is
always greater than or equal to the
likelihood function that we have gotten
at theta t
Okay that that completes the proof the
claim that we just made that the
likelihood function would never decrease
if we
run the algorithm
Okay Now this is a sort of uh see note
that this inequality is not strict What
we are saying is that the likelihood
function is not guaranteed to uh
increase uh continuously It is only
guaranteed that the likelihood function
does not decrease as you run the EM
algorithm This is one of the known
drawbacks of the EM algorithm Right So
it can get stuck in the local minima
because you know it can the inequality
is not strict
The other question that was asked in the
previous class was what is the stopping
criteria
Right So typically the stopping
criteria is that uh you run the EM
algorithm and keep tracking what the
likelihood function is
Now compute the difference between the
likelihood at the next iteration and the
previous iteration and keep a bound on
that If that difference is significant
enough then you continue to the next
step or or for a lets say for few steps
the difference is not significant then
you stop the algorithm That is how it
is done So that is a hyperparameter So
you choose uh put choose a delta and you
say that only if the difference the
improvement that we get in the
likelihood function is more than that
delta Ill continue otherwise I stop
That is how it is done in practice
Okay Yeah Okay So now
 just one last thing
to get the last implication are we using
inequality or we are using the fact that
the assumed form of Q for that f theta Q
 plus 1 is equal to L theta plus
 no no we are no no we are using Jensen
inequality because
equality will become only if we evaluate
that at the QT that we have computed
with theta t plus 1 which is qt plus 2 Oh
okay
 This is only through Jensens
inequality
 You get right The elbow evidence lower
bone will match the likelihood only if
you have computed uh the variation
distribution to be equal to the theta at
which you are computing the elbow
otherwise it is not equality
Clear No Yeah
Mhm Oh you are asking what the
convergence what the stopping criteria
is
 for No not for f theta The what the
the convergence criteria is the
following right You get new you get
see this if you look into this as a
black box every iteration it will give
you a new set of parameters theta right
now when do you want to stop this You
want to stop you every time you get the
new theta evaluate the likelihood find L
okay and see if your L is improving
by a significant margin which is user
defined If it improves with a
significant margin then continue
otherwise you stop
 and if it decreases you will
 it will not decrease no by construction
So you just we have just shown that the
likelihood cannot decrease with em
 Im not talking about parameters Im
talking about likelihood Compute the
likelihood at that particular parameter
theta
What you have what you compute is this L
of theta See L of theta cannot decrease
as you are running the EM algorithm L
of theta will not decrease Itll only
increase or stay the constant Thats
it
Okay So this completes the EM
algorithm So now what we will do now is
we will see how to uh implement this EM
algorithm for the case of the mixture
densities that we saw Uh we will stop
here and continue in the next lecture
