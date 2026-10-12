---
id: zM5-TlrmKg8
title: Tutorial 15 Part 1 : RNNs, LSTMs and GRUs
url: https://www.youtube.com/watch?v=zM5-TlrmKg8
date: '2026-03-20'
duration: 34:06
model: youtube-captions (en-orig)
transcript: true
---

# Tutorial 15 Part 1 : RNNs, LSTMs and GRUs

## Transcript

Hello all, welcome to this tutorials in
which we will be running through
the recurrent neural networks, RNNs,
LSTMs and GRUs.
The aim of this tutorial is to
understand these different cells RNN
cell, LSTM cells and GRO cells and then
put them together
come up with the deep networks that are
for using RNN, LSTMs and GRUs.
So most of our discussion here will be
for a classification task but the same
thing can be extended for a
sequencetosequence mapping as well. So
without any further delay let's jump
into understanding RNN
from the lens of implementations.
So by now all of you are uh comfortable
that I have an input X
know which has uh sequences with time
stamps X1 X2 so on till XD and please
remember this is one given example okay
so we're not putting I and making more
clutter into the uh notations okay now
here at any time step T now this belongs
to uh E okay so and then uh so always
we'll be putting in batches so the batch
size
so let's consider uh B as the batch size
and then the total sequence length of
this example the sequence length
let's consider the sequence length as P
and
Input feature dimension
is D. See whenever we are saying the
input feature dimension is D. Now what
do we mean by that is that we are
considering an embedding of this first
word. So since we are dealing with RNN
deals with sequences assuming that we
are dealing with words. Now first of all
it can be either represented as one hot
encoding or this can be represent as an
learned embedding. Okay both are
perfectly fine. So to understand the
overall idea now whether it is being a
one hot encoding or being a embedding uh
doesn't stop us from understanding. Now
in terms of implementation whenever you
are having embeddings that is always
considered to be giving good results.
Okay fine. So now all of these models
now we'll have this hidden state. Okay
H
t minus one. This belongs to the hidden
state size is RH and this is the
hidden dimension.
Okay. And then y for that given example
it belongs to RK.
This is a
the output
dimension. Okay. For the given uh
example x. Okay. So now uh we know that
now if you put all these x together now
x the whole x will be a matrix which is
t cross d. you have t uh length sequence
and each is of dimension t. So it's a
and if you consider the batch okay once
the batch is considered
once the batch is uh
considered I represent it as X and that
belongs to R
B cross T cross D and whenever we have
this batch as the first dimension okay
now this is what is known as a batch
first okay now here the batch size is
the first dimension. So now
now let's recall uh the overall RNN
equations. The reason why I'm doing is
uh see uh we have to know what is the
size of each of those uh uh weights that
we are having. Okay. So now let's look
at the
RNN.
RNN's we compute HT equals some
activation. Okay. Now irrespective of
that W1
XT
plus W2
HT -1 + B1. See and then please remember
that this HT which is there is the
hidden dimension. This has to be of size
RH. So this is for one uh instance one
time stamp. Okay. So now at the time
stamp t what is the hidden dimension? So
please remember that this should this
should belongs to RH. Okay. Now finally
whatever we get should belongs to RH. So
now what do you mean by that? Now
finally it should belongs to RH. Now
these are additions. Then what do you
mean by that? This should belong all of
them individually should belongs to RH.
Correct. So now that is what we have to
define. Now this W1 which is there will
be a matrix that is H cross
D.
Okay. So and then uh W2 belongs to R H
cross H and D1 belongs to RH.
Okay. Now this is in RD.
Okay. You consider D cross one. So this
will be belongs to R H. This will also
belongs to RH. This is already in RH.
You add them. Okay. And then pass it
through a sigmoid and sigmoid is applied
individually for each of them. Okay. So
therefore your or any activation not
only sigmoid. So that means that this
will be in RH.
Okay. So now this is the hidden state.
How do you compute the output?
See the output y at that given time
stamp t is w3
ht plus some b2. And please remember
this yt should belong to rk
correct. Now therefore
this W3 should belongs to R
K cross H and then this B2 should
belongs to RK.
Okay. Therefore this will belongs to RK.
This also belongs to RK. Now you add
them. So finally this will belong to RK.
Okay. This is the this is how we obtain
the RNN. So from this what we know now
these are the learnable weights. Okay.
Now we have these many learnable
weights. Now you can put some numbers
and then think of how many learnable
weights are there in this given case.
Okay. So now now let's uh
let's go into the the GRU. Okay. Uh
so what happens in GRU?
Let's look at gated recurrent unit. See
as per uh the timeline LSDM came first
since LSDM has too many weights. Now
they actually went from reducing it and
obtained GRU. But pedagogically we
always look at GRUs first which is just
a straightforward extension of RNS and
then uh we look at the
the
uh LSTMs. Okay. Now let's look at gated
recurrent units
and understand their uh implementation.
ated recurrent units
GRUs.
Okay. Now here as we already know from a
generalized
expression. Now in this case
now HT
is some alpha t
taking a dot hadamide product with HT
minus one plus
some beta T it is taking the hadamad
product with HD tilda
see now you're taking hadamarad product
okay that is element wise multiplication
when you have vectors so this and this
this and this all of them should be of
same shape. Okay. So now that means that
from this we can easily say this alpha t
comma this beta t comma htus one comma
ht tilda all of them belongs to RH
correct which matches the shape that is
needed. Now once you have this HD now in
a similar way like we did uh in our uh
earlier uh RNN case we obtain the Y.
Okay. Now obtaining Y is exactly similar
but obtaining the hidden state is where
things matter. So now in GRU normally
what they do is now this beta T which is
there is considered to be 1 minus alpha
T. Okay that is how this beta t comes
into picture. So now ht minus one is
from the previous state the hidden state
hidden state input from the t minus one
step that is there. Now the only
question that arises is how do you get
this uh alpha t and how do you get this
ht tilda. Okay. Now the way in which we
obtain this uh
alpha t
is some activation function
of some weights w alpha
for the concatenated
input of
xt and htus one plus
b alpha. Now this is uh bit weird. Now
what do you mean by this? So now this
actually means xt concatenated with xt
-1.
This belongs to some r
d + h.
Okay.
Now this belongs to r d + h. Now sum of
two things. Now alpha t alpha t should
belongs to rh. Now therefore this has to
give me an output
of belongs to RH. This also should be in
RH. Okay. So now know therefore the W
alpha which is there now belongs to R H
cross
D + H and this B alpha which is there
belongs to RH. Now when you apply this
your alpha t which is there will be in
rh. Okay. So now see just try to
understand whenever you have now these
are the weights that are learnable.
Okay. Now how many weights will come
into picture as of now we have uh these
many weights for alpha t. Now we have to
come up with this uh ht tilda.
Okay. Now to come up with this they have
uh uh what do you call uh now rather
than directly going ahead uh and uh
using the previous state so what they do
is they will have some learnable
parameters
so and put it as what is known as some
residual connection okay the words
doesn't matter so rather than working
with directly with uh the previous
hidden state and the input okay now what
they do now they will have a learnable
uh things and that they take the
hadomide product with the HD minus one.
Okay. So now that's what they will do.
They call it as the residual uh thing.
Okay. But that's fine. So I don't prefer
to call it as R. So I use this symbol
some activation
the way it's pertaining to the residual
state.
So now
XT
HT minus one plus
V of that
now again exactly now this has to match
now because you have to take the hard
product with the state. So now therefore
now
this
and this okay now they will be of the
same dimension that is there. Okay.
So now
now comes HD tilda to some activation
WH
this is XT concatenated with this
whatever residual that you have and T
minus one
see what is that they're doing here is
quite simple as I told you rather than
just going ahead with the hidden stick
they're having some more learnable
parameters here
Okay. Now you have some more learnable
parameters which you can actually have
control with. Okay. Plus this
PH.
So now now again now because of the size
matching this and this
should be similar to the given size.
Okay. Now then finally what do you do?
Now then you have HD is alpha t
taking the hadamar product with ht minus
one plus this is 1 minus alpha t
this taking the hadamar product with ht
tilda this belongs to rh and then you
have uh yt
which is w3 ht
plus B3 that we have obtained from our
previous uh discussion from RNN. Okay.
And this is how the transformation
actually happens. Now you can see here
how many controls you have controls
here, here, here, here. These are the
controls that you have uh to control
your outcome. Okay. This is gated
recurrent unit and I'm comfort and I am
uh sure that all of you are able to
understand now this is learnable this is
learnable
okay now these two are learnable
okay that is the overall
idea okay see uh the point is now here
rather than just
learning the hidden state from the input
and then the previous hidden eight. Now
what do I do is now I come up with I
don't work with directly in the input
space. What do I do? I project it onto
some other space and then learn things.
Now that is what is happening in the
gated recurrent unit. Okay, that is the
idea. Okay, you have these many weights
here.
Now let's look at LSTMs.
which is uh
even more uh uh weight heavy. Okay, in
terms of weights. Okay, now we have this
uh
LSTMs
that is
long
short
um memory unit.
Okay. Or memory cell. Normally these
individual units are called as cells.
See the same uh weight sharing will be
there across the time. Okay. Now if you
use it for uh uh whatever you use it for
the first input uh
sequence the same thing used for the
second one. The same thing you you
unroll it. The idea of unroll is clear.
Okay. Now this is parameter sharing
across the time. In CNN's what we have
is parameter sharing across the the
space. Okay. So now
let's look at these LSTMs.
Now I leave the generic formulation
derivation. So in a sense how do you
represent your LSTMs using this generic
formulation? I will leave it to you as a
nice exercise. So I'll just write the
way in which it is implemented in most
of our uh textbooks or in the blogs that
you might read. Okay. So
normally you have three controls in
LSTMs. Now they name it as forget cell,
input cell and output cell. That's what
they name it as. But you have three
points of control. Okay? And
you remember that we came up with uh
LSTMs for a specific reason that there
is a vanishing gradient. Now that means
that you need a path in which we
actually have no weight interaction.
Okay, let me there is a very
image that we have.
So now and this is the standard LSTM
image. I just got it from the internet.
Okay. So now this is what is known as
the the candidate state and this is the
hidden state. Hidden state is what
something we have been using. See hidden
states are actually having lot of
interaction with the weights. Okay. I'll
tell you the way it's interaction here.
But in the candidate state that is what
they call it cell state or the candidate
state. Now here you see that there is
just some multiplication with some
number here and then there is some
addition. Okay. You actually have no
interaction with the weights. Now this
is where the untransformed input
actually comes to the next unrolling.
Okay. Now here is where all your uh what
do you call
operations actually happens where lot of
weights are there. Now now normally they
they give a explanation something like
now here you you are obtaining this is
what is known as a long term and this is
what they call it as a short term. So
just telling those words so that
whenever you read other blogs you are
comfortable with that. See uh this what
they're saying is whatever is coming now
how much I have to remember.
Okay. Now that is coming from that
percentage is coming from the forget
gate and how much new information is
added. Now that is coming from this
input gate. Now depending on that how
much should be the modification in the
uh hidden state. Now that is given by
the output gate. That is what these
three gates actually specify. But we
have a lot of control that's what we
have a lot of parameters using which we
can control the forget gate the input
gate and then the output gate in which
you have uh a lot of uh control okay so
now the overall idea is rather than
handling in the original data space now
I'll have learnable parameters so that I
can project it onto some higher
dimension space in which I have the
control in the learned space okay fine
so now at any given step. So this is the
forget cell. Okay, I just represent
them. So
and uh and one more thing is I should
remember this at any given uh time the
CT now which is the the candidate cell
and then the HT which is the hidden
state now all of them will be in RH.
Okay, both of them will be in RH. Now we
have this
ft
which is some uh uh activation function
preferably we use a sigmoid function as
it is given here
weights to control it
xt concatenation of
minus one plus
uh I'll not be rewriting the dimension
of all these things now since
So
all of them now will be all the weights
that here all the W's will be in R H
cross B + H all the biases that are
there will be in RH okay now it is
constant for all these operations okay
while computing the HD
this is uh what is the forget gate now
this is what is happenings here this
This is the interaction that is there.
And then we have
the
the input gate.
My input gate is uh again wi
xt
ht minus one.
Okay.
This will give you some kind this is
again a sigmoid activation some kind of
a percentage. Now it will give you now
how much percentage should be added. Now
this is your uh input gate. Now how much
percentage should be added is obtained
here and the information is obtained
here. This is the common uh
terminologies that they use. Okay. But
for all none of these we repeat it again
and again we don't have any evidence
that this these are all in some
projected space working that's all. Now
see tilda this is what they call it as a
candidate input. For this they use uh
tan h activation
wc
x
ht minus one
plus
wc.
Okay
this is uh the candidate.
So now
what will be your final uh
CT? CT is
now whatever is FT that you take the
hadamar product with CT minus one plus
whatever is your input that you take the
hadamar product with.
So now what does this mean? Now this is
this is from the previous uh uh cell
state. Whatever you are getting now this
is some kind of a percentage you make an
interaction
okay had a product this is some kind of
a percentage know you have your data and
the hidden state projected onto some
higher dimension you take the
interaction uh this is what this will be
okay this is what will be the CT this is
your long term this is also known as the
the long term now you have to get your
HT now to get the HD you need this
output to Get OT sum
alpha *
W into
the concatenated
HD minus one
plus
D O.
So and then HT equals
OT concatenated with
tan H of
C. Now again since you have a sigmoid
now you can think of it as some kind of
a percentage vector for each of the the
value which is there and then you are
taking a transformation CT here. Now
this will give you HT.
Now once you have ht now we have
yt which is w3 * ht plus b3. Now just
for the sake of completeness I just
write WF
Wii
WC
WO all of them belongs to R H cross
B + H
BF
B I
B
O all of them belongs to RH
and then this W3 belongs belongs to R K
cross H
and then this uh B3 belongs to RK.
Now these are the weights and now you
can put some numbers. So this is not
this should look like H.
Okay. Now you can uh add up these things
now for some simple uh thing and then
you can see how many weights are there
here. Okay. This is actually weight
heavy. Now to avoid this now they came
up with actually
the GRU.
Okay.
So now
uh now let's implement uh these things.
So now what we will do is now we will go
ahead with a simple classification. So
okay now the unrolling
the unrolling let let it be any any cell
the overall idea will be
okay you have a cell
you get
ht minus one this is your xt you perform
some operation And the output will be ht
and then what you get is yt. Okay, this
is what you get.
Okay, this you unroll multiple times.
The unrolling sometimes they they refer
it in the
thing here. Now this is for uh
GRUs or
RNN
in terms of LSTMs. Now you don't have uh
one. Now you actually have
two things. This is CT
minus one HTUS one. You get this XT
here.
Then
you get CT
HT
and you take this HT
and perform some modification
and then you get YT. Okay, you don't
see here the modification with only with
respect to HD. Now this is one cell.
Again you can have uh
recurrence also and this is the
idea of
LSTMs. Okay. Now each time whenever you
are unrolling you'll be getting this YT.
If you consider only the y capital t to
perform some classification. Okay, that
is fine. Or at each of these yt you
perform some other uh uh use some MLP
and then perform transformation that
will be your sequence to sequence. Okay,
for each of these YT now you have some
other uh MLP that will give you some
other output. Okay. Now for example, if
you want to predict the next word, now
the MLP will be uh the output will be
the size of the whole how many words
that are there. That is what is known as
a dictionary. That will give you the uh
uh the uh output in the case of sequence
to sequence. Okay. Now here now you have
only one cell that is repeating multiple
times. On the other hand, now what they
do is
now they will have now what is known as
deep deeper network where which you can
specify the number of layers as well. So
I just go ahead and
write with for uh
the LSTMs. Okay. Now why am I writing it
for LSM is
actually it is easy for us to
okay now let's say that you have three
LSTM cells you have three layers okay
three layers of them okay so Now
let's say that it is C 0
this is H0
and the input is X0.
Now this will give you C1
and then this is H1.
Okay. Now you take this H1 which is
there
and give it as an input for the
another one. Okay. Now see here here you
used to give X not. This is your first
input of the sequence. You take the
hidden state here and give it to this
and again you will have C1 sorry this is
C knot
and Hnot of the another layer.
Now this will give you C1
and H1.
Now again what you will do?
You will take this
and
give it as an input.
Again for these you'll have a C knot and
Hnot of another layer. This will give
you
C1 H1. Okay. And then what do you do if
you want to go ahead with a sequence to
sequence? You take this HD which is
there
and then you pass it through an MLP
and then finally you use
soft max here to get the output.
Now considering that you're predicting
the next word.
Now this is for one
sequence. The same thing you repeat.
What do you mean by repeat? These are
the same weights that are there. Okay.
Now you have another thing for this. You
will have X1 that will give you two
things. You give it to the next one. Now
so on and so forth you repeat. Now when
I say repeat, not only the weights of
this are repeated, even the weights of
MLP are repeated.
Okay? You repeat them and then you go
ahead with uh the the sequence sequence.
Now if you are not doing it, you just
want to perform a classification. Now
repeat it for t number of times.
Whatever is the last HT which is there
of the highest layer, you take this have
an MLP, you pass it through the softmax
in that case and you get the the
predictions the classific the
predictions in this case. That is what
you use it for the
uh classification task. Okay. Now, now
this is how we can have multiple layers
of it. Okay. Now this is this is how we
build the architecture. Now we we
haven't even come to the implementation
of it. This is how we build the
architectures.
Okay.
So this is where uh we actually uh stop
this tutorials. In the next part of this
RNN tutorials, we'll be looking at the
implementations of RNN's, GRUs, LSTMs
and their uh deep uh uh variations.
Okay, I hope you understood uh the RNN,
LSTMs and GRUs. We'll meet in the next
uh part of this tutorial. Thank you.
