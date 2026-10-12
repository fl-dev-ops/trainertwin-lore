---
id: nJivfX9VY7Y
title: Tutorial 15 Part 2 : Deep RNNs, LSTMs and GRUs
url: https://www.youtube.com/watch?v=nJivfX9VY7Y
date: '2026-03-20'
duration: 16:52
model: youtube-captions (en-orig)
transcript: true
---

## Transcript

Hello all Welcome to the second part
of this RNN tutorials in which
we will be looking at the
implementations of RNNs LSTMs and
GRUs
Im confident that you are comfortable
with the
the equations and
the sizes the matrix sizes of the weight
matrix sizes and bias sizes and then you
are comfortable with the transformation
and then Im assuming that you are
comfortable with the idea of recurrence
in GRUs and LSTMs and also the multiple
layers that are there
in a
a deep layer
RNNs LSTMs or GRUs for that matter
Now we will see all of them
implemented now
using PyTorch
Okay

 so lets uh
start with that
Lets
uh
take First lets put all the input and
other things together We are generating
a dummy input and then we are going
ahead with that
So now the torch is the base package
NN is the neural network that is needed
for us
Now batch size is two
So the sequence length Now that is the
how many inputs are there is five
Okay that is your capital T is five
Your input size that is the dimension
Now in this case is D
is 10
And then the hidden size which is there
the H
Okay this is eight
And the size of H RH and then the number
of classes is four Okay that means
that youll be only looking at the last
output which is there and then using
that last output youll be going ahead
and
obtaining the
uh the number of youll be going ahead
and obtaining the final decision Okay
So now Im generating an input which is
a random batch
T which is the total sequence and D
which is uh the dimension of it Okay
so you have the input which is two cross
five cross 10
Okay so now
uh
Now what will be the
the hidden thing The last one
Now will be at size eight Okay this
is your H capital T
Okay now that will be of size eight and
all your uh intermediate uh outputs now
which will be there that will be
the five cross eight Now because for
all the five examples you are storing
the
the intermediate HTs therefore it will
be five cross eight Okay so and then
you have two so it will be two cross
five cross eight Okay now you should
be able to Now you should be able to
convince yourself that Okay the input
size and the output size should be mad
should be visually appealing Okay so
now Yeah you create an RNN classifier
Now this has to be a child of NNmodule
exactly similar
to the MLP and CNNs that we saw
And whenever youre creating what is
the input size
Okay what is the hidden size And then
what is the number of classes Now why
do we need them So now lets go to the
the RNN
Okay now if you look at it now input
size your D is needed hidden size is
needed Okay and what is the output
size K is needed So only when you
have those numbers now that is when you
can define all these weight matrices
Okay so you need these input Now in
our case now H is eight D is 10
K finally you will get it as
uh four Okay
This is what now we have
Okay
Thats what So youre creating an
thing which is input size is uh
uh
What is the input size Its 10 Okay
that is for for one given sequence You
have five time stamps like that Okay
but that the same thing will be
unrolling Correct Now the parameters
will be shared across time so you
should be able to remember that So and
then the hidden size which is eight
Now batch first What do you mean by
batch first You know as I told you
here in the data Okay the first
dimension actually corresponds to the
batch Yes it is true
And then finally you get an output now
which is your HT now which is there
that you have to convert it
to the final output So you need an MLP
to convert it into number of classes
This is eight cross four
That will be a fully connected layer
Okay this is only done for the the last
one
Okay
So now lets try to understand this
Now first you have the input Now I
have given a lot of prints so that it is
easy for us to understand the output
transformation which is there because
which is very much important
So first is the input shape So the
input shape will be BTD Okay now this
is two comma five cross two comma five
comma 10 Then you pass that through the
RNN Now RNN will give you HN which is
the last This is your HT
Thats what it means that the last one
and then this output which is there is
the combination of all the states
Okay all the states output So this
will be the output Now will be of shape
Now BTH
Now that is two comma five comma eight
now which makes sense And then your HN
you have only one layer so it will be
how many examples are there and then the
hidden state of it
Okay which makes total sense
And then what do you do You take the
last one You take the last hidden state
that is H capital T and then you pass it
on uh you get this Now this will be in
the form of B cross H Then you pass
this through the fully connected layer
and then you get the logits
And then you have these logits pass it
through the softmax you get the
probabilities
Exactly the similar one You create an
instance
and then you generate the input and pass
it on This will give you the
output Okay its allocating the
runtime
This is how you Once we know the
uh
uh the input and output relation now it
is easy for us to traverse And this is
how we do it NNRNN
is how we create the
the layer
Okay
Uh as you can see here
RNN output is two cross five cross eight
where in which all the outputs
that are there are being stored And
then your HN is the last uh HT Okay
thats what HN means here And then that
is two cross eight For each of those
examples two is the batch size you have
an eight dimensional vector And then
the final that eight is passed through
fully connected layer which is going to
transform into this And this is your
logit See uh see your logit has a
negative number its totally fine Your
softmax cannot have a negative number
but logit can have a negative number
Okay this is regarding a simple RNN
Okay how do you define an a simple RNN
So we are still uh
Now you dont need to write anything
for recurrence Okay the recurrence in
terms of time the unrolling is taken
care Okay now depending on the number
of uh
examples that are there that is the
capital T and which is there based on
that the recurrence is taken care Okay
now the recurrence is taken care You
just need to define the whole structure
Now this is weight sharing The
parameter sharing is across the time is
there
Okay So now lets
look at the same thing as LSTMs which is
exactly similar but in LSTM rather than
having
now only hidden state you will also
have the the cell state or the candidate
state which is there Now all of them
will be of the same shape So the shape
consistency is there So as we have
seen in our earlier discussion also
Simple LSTM classifier Now it has to be
a child of NNmodule so that you can
have the automatic differentiation taken
care of But then you have NNLSTM Now
that is there Input size hidden size
batch size batch first is equal to
true Exactly the same thing Okay
Now here
whenever you pass it through the
uh
LSTM cell that you have now you dont
you not only get HN now which is your
short term memory you also should get
your CN which is your cell state CN But
both of them will share a same
uh size Okay will be of the same size
And then output is there which is
accumulation of all your the previous
states
Okay So then you just get this and
then you get the last one
and then pass it through the fully
connected layer exactly in a similar
fashion
So this is how you have your simple
LSTM classifier
Okay Im just having one cell Okay
Im not going ahead with the deep We
will discuss how to go into the the
deepness How do How do you implement
the depth which is there
Now similarly GRU is exactly similar
Okay only the internal operations will
be different but
the way in which the structure is there
its exactly similar
NNGRU
input size hidden size batch first is
equal to true
You create it
And then you have a fully connected
layer so that you have the
uh
final output is converted into a
posterior for the sake of
classification
And the outputs all of them will match
Ill not be uh going in deep with this
Its exactly similar to the RNNs and the
LSTMs that we saw
Okay So now comes the important thing
now which is okay now this makes sense
for us
to deal with the classification problem
but what if we have
to take into consideration
the
uh sequence to sequence generation
Okay
Now in that case you want to many to
many
RNNs
So
exactly similar
but one major thing that is the
difference is you will not be only
passing the Now here
to the fully connected layer youre
only passing the last one
Correct Youre only passing the last
one But here
you are passing the
full
thing itself
Okay youre passing the full output
itself
Now the nnlinear will be hidden size
 comma output size It will take each
of those output and then apply it And
then it will give you an output which is
uh B which is the batch size T
uh for each sequence you can index
them and then the output size
Now we have taken output size to be
six Okay Now that will be two comma
This is T is five comma six
Okay thats what you will get
Okay So you have the output of each of
them pass it through the fully
connected layer wherein which you have
six classes Now then you can choose
put a softmax over there and then choose
the highest uh argmax you can do it and
choose the highest probability
Okay
Thats all Two comma five comma
six
Okay The main difference is youll in
uh whenever youre going ahead with a
classifier
okay youll be passing only the last
uh HT
youll be passing But here youll be
passing
the whole output itself wherein which
you have all those individual
uh contexts are there
Okay
That is the many to many that is the
sequence to sequence idea which is
there
Okay And please remember that in all
these cases we are dealing with only
one layer We havent implemented
multiple layers
Okay
Now whenever you implement multiple
layers now then
So
you will be having these kinds of
connections Now if it is only RNN now
now you have this
This will be passed to the next case
Okay And then you will have the MLP at
the top
Okay Now that is fine Now
here you have two there you will be
having only one
Fine Good So now
Now then how do you do it See the
idea is very simple
Just
use the number of layers
three which is there And then while
defining
the RNN block you just specify how many
layers you need
Okay
So now because of which it will not
only If you dont specify number of
layers will be considered as one so you
only get one If you specify the number
of layers you will have this
So till here you get it and then you
use the FC
to use this Now all these parameters
are actually shared
Okay Now you just do the same
unrolling over time
So and then linear you have uh hidden
size to number of classes
Okay So now what what will happen is
Now whenever you want to get the uh the
last one now youll not be getting last
one of only the one uh layer Youll be
having
HT of all the layers Okay That will be
one difference in terms of the HN
output
Okay
So now you get two outputs because of
RNNs You get three outputs because of
LSTMs You get uh
two outputs because in GRUs Now
exactly in the same way in which you
have done in the uh RNNs and LSTMs its
just a simple extension of the same
thing
Okay But you just need to specify the
number of layers Now because of which
the size of HN now which is there will
modify
Okay Now here output now whenever Im
saying the output that is of the last
layer Thats what is happening
Whenever I say output that is of the
last layer
Okay
But whenever I say HN now which is
there which is the last hidden state
now that will be for each layer youll
have a different hidden state Now all
of them has to come along Now what is
that Im saying is when I say output I
only say the last one
Okay Whenever I say the hidden state
of the last uh unrolling now for each
layer it will be different now
Correct
Thats what
I need to get
Okay
So now
This is your
last HN This is This is you can equate
it to
the
the Y
T at each time step
So this is your H capital T You can
get it and then you obtain uh
the last Y which is there Okay the
last one And then you pass it on
through the
fully connected layer to get the
final output Okay Now exactly a
similar structure in LSTM also deep
LSTMs
You just specify number of layers
here How many number of layers you
want Now because of which the same
will be the case for
short term and long term context which
is there And the output generation is
exactly similar now Okay Even in the
sake of in the case of
uh deep GRUs also you just specify the
number of
layers Okay And then you can uh
uh get the
inputs in a similar manner
Now this is how you actually implement
a classifier or many to many problems in
using uh LL uh LSTMs
uh GRUs and RNNs
Okay
So I hope
you will be comfortable in
implementing these things
We will meet in the next tutorials
wherein which we will uh look at
the thing that changed all our lives
Well be looking at
how do we implement the transformer
model
Okay the transformer architecture how
to implement that we will be looking
that in the next tutorial session
So I hope all of you are on your feet
Well meet in the next tutorial sessions
with the transformer architecture Till
then have a nice day Bye bye
