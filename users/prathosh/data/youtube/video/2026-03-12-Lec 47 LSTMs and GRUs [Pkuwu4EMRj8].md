---
id: Pkuwu4EMRj8
title: Lec 47 LSTMs and GRUs
url: https://www.youtube.com/watch?v=Pkuwu4EMRj8
date: '2026-03-12'
duration: 22:18
model: youtube-captions (en-orig)
transcript: true
---

## Transcript

Welcome everyone to the class
See general mathematical
objective to solve the vanishing
gradient problem
So in a recurrent system
we have the hidden ht to be equal to
some function f of ht minus one and xt
This is the definition of recurrence
isnt it Current state is a function of
the previous state and the current
input
Look at our equations No
ht is a function of ht minus one and xt
Of course theres the sigma I mean
all that is captured within this
function f now So there is linearity
There is its a composition This
capital f now is a composition of
linearity and some nonlinearity It
doesnt matter But what is important is
its function of htus 1 and xt Correct
So this implies that
this particular Jacobian
which is a product of these terms
The dependence of the final hidden state
on any previous hidden state is through
this product
Oh sorry
Yeah this comes up because of the
recurrent nature Correct
Now
in a vanilla RNN
vanishing gradients
happens
because since this term
is multiplicative We have uh diagonal of
the sigma
sigma dash
time w
correct
because of this repeated multiplications
of w we get that particular term Okay
The solution
is to
make
just approximately equal to identity If
you make this then doesnt matter right
I mean this is the degenerative or naive
solution as he said make lambda max
equal to one so that theres a path from
the outermost hidden state to the any
hidden state without without any
uh
linear multiplications of w right now
lets
lets look at um
general principle to do that is to
achieve this
Yeah the state update
should be additive in in terms of
instead of multiplicative
How do we do that Make ht to be equal
to some alpha t
 times
ht minus one
Actually Ill write it as hard product
here element wise multiplication because
alpha t and htus 1 are both vectors
Ill multiply each of the elements by
something different value Beta D times H T
tilda
where
HT
minus one is the previous state
H T tilda
is some function of
W1 XT
plus
uh some W2
HTUS 1 plus some bias
So alpha t and betat t
are
modulators some
okay thats all So now what am I doing
is look at this Now the dependence of
ht on ht minus one okay is no additive
Its not multiplicative anymore See
what was it Ht was dependent on htus
one through sigma through this equation
previously
Now there is also an additive path here
You see this
So now ht depends on htus one
Previously HT was dependent on HT minus
one through
this matrix and some nonlinearity This
F is some nonlinearity Okay I actually
I can write it as some sigma
some nonlinearity
Now to that we have also added a I added
another additive term here
Do you see this
Yeah Now what happens because of this
is that the derivative of hk plus 1 with
respect to hk will now have two things
we will do that as well One there will
be a term that still has this w term
which the vanishing gradient thing and
there will be another term that only has
this alpha t times identity because this
htus one the dependence is only linear
here You see this
thats it So you are creating a an un
uh stopped or rather unrestricted
conveyor belt kind of a thing from
between states HT minus one and so on
Well do the math We Ill show you the
equations in a yeah
 which one
 The alpha meaning
 yeah that can happen those are also
learnable Ill complete the story in a
while Okay Now what happens is uh
suppose you make betat to be equal to 1
Okay you get a particular type of an RNN
called highway network
Okay if you make your uh beta t to be 1
minus alpha t then what you get is what
is called as gated recurrent units grus
Okay If you make both alpha t and betat
t to be learnable vectors then it is an
LSTM
In fact this is not the only way to do
this That paper which Ill share with
you has shown thousands of ways to do
this
Okay that will ensure that you know all
of them will have the same effect But
what is to be done is that you know the
only thing is that youll have to ensure
that there is a theres a theres a
linear path so that the derivatives will
not will not die down Lets lets look
at the ma math now Arent we having the
learning by manually saying that it
should be related to
 no no we are not were not restitting
learning because we still have this no
we we are not changing anything this
depend this is like that skipped
connection in reset
we still have that path we have now two
paths there is a highway or there is a
linear connection and there is a
nonlinear connection as well so the
gradients flow from both the ways
theres a you yeah I mean this alpha and
beta will tell you how much of the
information to forget and how much of
the information to remember if you look
at it look at it that way
 So out of the two parts which part
depends on the problem you leave it to
the neural network So you are learning
alpha t and beta t as well
Right So network will decide which one
to what what to remember what to forget
but you are facilitating the neural
network to forget selectively forget and
remember through this alphas and betas
thats it
see I could have actually written the
equations of grus and showed you know
all the complicated stuff this is this
is actually the the most abstract way of
looking at things so you can derive
thousands of architectures from this
okay let us look at the calculus right
now we lets look at what happens to the
you know the derivative so that this
will not lead to the vanishing gradient
problem Thats where we stop Okay
 Where
we ht
 it doesnt matter I think So you know
this is what what did I write
 Okay its just a parameter right Call
it whatever it has no bearing
whatsoever Just two set of parameters
It doesnt matter what it is Okay
And by the way some people call this
right this H tild as candidate states
Okay So they have there is some
candidate state and then you multiply
that with lots of terms right Forget
gate input gate that gate they call
them gates and so on Basically this is
the idea right So yeah Okay So lets
lets look at uh the the math What
happens uh at the math Now
the gradients
for the networks
See please dont complain Dont tell
me that you know GRUs and LSTMs was in
the syllabus but I did not teach them
Ive
actually taught the grandfather of GRUs
and LSTMs So you derive those things
from these Okay
 Long shortterm memory networks
Theres a long term memory short term
memory This HT
is the short term memory HT minus one
is the long term memory and so on Its
idea So just go and look at LSTM
equations and convince yourself that
this is a special case of whatever Ive
written here Okay The power of
abstraction You see always abstract
so that everything in the world becomes
a special case
Okay Okay So lets consider this
derivative right So h is consider
So this will now be
uh the diagonal of uh vector alpha t
So you understand what what is diag
means right So its a diagonal matrix
with this alpha t as its diagonal Okay
thats what I mean And since we are
looking at uh uh gradients sorry
vectors Ill have to write these this
way H t 1
 times diag
of ht 1
plus
do
beta t
 times h tilda
divided by d ht minus one
See whatever Im doing it for this
particular uh abstraction can be done
for GRU separately can be done for LSTM
separately and thats a homework You
understand what Im saying Write down
the equations for GRUs and show that it
does not have anything gradient
problems Im doing it right now but
youll have to do that special case
This is the most general case Okay
Now this can be written as so diag
alpha t plus some
chalon t
So all this all these terms simply
calling them as
chalon t uh why am I doing that is
because see here there is dependence on
ht tilda and ht minus 1 and so on which
will have w1 and w2 terms ter terms
you see what Im saying
see ht here depends on htus one and ht
tilda ht tilda depends on xt and htus 1
through w1 and w2 right so these terms
which Im saying uh as e or epsilon t
this actually depends on w1 and w2 I
dont care about that All Im looking
at is diag of alpha t now which is
independent of
w1 and w2 This independence is coming
through this particular term
See when I take the derivative of ht
with respect to ht minus one there is
diag of alpha t here right and the other
terms and these other terms Ive simply
use chain rule here right the first term
plus the derivative of the second
derivative of the second has product so
this these two terms come from the
product rule thats it
correct and Im combining all the terms
that are coming from the product rule
into something that I dont care
okay so now there is diag of alpha t
term now when I do the take the
derivative of the last state with
respect to any time step t which will
now have the products of
plus this term
right now if I do cautious thoughts and
look at the norm of this
what will happen
there will be a norm of
 t
to t minus one correct tus one
some identity here because the diag of
alpha k plus 1
you take alpha k and it will become an
identity which will be one Thats it
There will be that term See now what
happened now There is this additive
term that comes up Okay this first
term it can still have gradients Okay
without caring about the second term
which has dependence on W
You see that right So because of the
presence of this particular term here
depends on what alpha is of course but
since we are making alpha to be a
learnable parameter if it needs to be
identity you can make it to be identity
right yeah
 of course thats the best that you can
do now at least thats what I told you
right we have facilitated the neural
network
 to be able to learn the long term
dependencies thats it Thats all the
point is theres no see thats all every
regularizer will do No any regularizer
is a is is is simply facilitating the
neural network to operate in that high
bias low variance region Thats it
Over parameterize and increase the bias
Now you see why this is regularizer
Right So I told you in when I looked at
bias variance decomposition that every
single architectural tweak that we do is
a regularizer Now going from RNN to GRU
or an LSTM is an explicit regularizer
where you have that additional path its
like this I Ill come Ill take another
question its like this right so you
make Y to be equal to X plus some
function f of X
y was f of x right now you made it to be
equal to x plus f of x where x is the
identity this is the resonate idea this
is the residual skip connection
see this idea
is so important because even the
modernday transformer architectures has
skip connections in it
All deep neural networks have a skip
connection in it uh in them because you
need to be able to learn this identity
Thats it The gradients will simply
vanish And please note that the
identity identity that we are talking
about in a recurrent architecture is
through time not through space
But in a resnet the identity is through
space not through time
So when you have neural networks that
are I Ill just tell you what I mean
See lets say that you have an MLP like
this right This is X and this is Y You
have connections this way Suppose I
take this and put it here
and connect it to this layer
without any weight
Sorry this is plus
This is skip connection
This is how it is typically done Take
one layer the other layer of neural
network connect one the the output of
that to the next layer So thats skip
connection which is done in the residual
neural networks or reset Even in
transformers this is done And now we
are doing it in spatially What what we
mean to say is that in the it is done
through in the uh the the depth
dimension but in an RNN
we read it through the temporal
dimension
depends on where your vanishing gradient
happens Right See you ask the question
how is an MLP related to an RNN So Im
giving you a hint In an MLP when you go
from one layer to the other the
gradients flow from output to the input
If you look at each layer as a time step
then there is a vanishing gradient
problem as you go deeper in the neural
network Isnt it Thats exactly the
problem the ResNet solves If you make
the neural networks you know you know
what the ResNet paper shows it shows
that deeper is not better If you go
deeper and deeper the neural network
starts performing worse because of this
exact same problem because the gradients
have to flow Now how do you solve that
Through the same idea wherever you have
this sort of a thing ensure that the
function also has an identity path so
that the the gradients do not go to
zero Simple chain rule So they did
residual connections across space
Meaning when you are doing neural
networks when you are constructing
neural networks which are deeper ensure
that every layer has residual connection
show that there is a uninterrupted path
so that the gradients can flow Do the
same thing across time in uh in an LSTM
In fact to make things complex you can
have an RNN okay which has longer
context and you have deeper RNN as well
You realize what Im saying And through
the depth you can have residual
connections there as well
You see what Im saying There is an RNN
okay where there is parameter sharing
across time and each RNN cell can be a
deep neural network across space and
those deep that deep neural network can
have residual connections across space
as well have the same effect I mean
gradients actually are flowing from two
directions right and please note that
across depth there is no parameter
sharing
this is w1 this is some other wcap there
is another theta and so on but across
time the parameters are shared thats
now you can see why this is an MLP with
a certain architecture isnt it
get it so typically an RNN uh the way it
is implemented is Ill that will be a
part of your second assignment anyway
the day it will be done is you have a
deeper RNN across space and you already
have parameter sharing across time by
construction of an RNN Okay
any questions You had a question So
just in the last step youre applying
what
 see yeah so so you have youll have to
have other term also there is a plus
here and uh youll have youll have the
norms of these individual terms bounded
and Ill take this one term and then
there is this dag term which will have
one as a gradient thats what I meant
you have norm of sum of two vectors then
you have to bound that norm of sum of
two vectors can be decomposed into
individual norms
Yeah So then you take one of the
individual norms and then do it Thats
it Yeah Okay So this completes uh the
the discussion on the recurrent
architectures uh the LSTMs and GRUs and
thousands of them as well Right Please
read that paper Ill share that with
you Okay Uh next class uh we will look
at the the attention mechanism and the
transformers which is the the
state of the art architects and and how
how are these neural networks trained
still erm still erm with the same
gradient descent that we are looking at
and you can still have all regularizers
that are there and remember that we are
still trying to get that P of Y given X
by minimizing the K divergence so that
does not change okay
thank Thank you
