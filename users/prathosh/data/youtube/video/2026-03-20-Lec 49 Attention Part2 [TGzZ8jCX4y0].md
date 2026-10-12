---
id: TGzZ8jCX4y0
title: Lec 49 Attention Part2
url: https://www.youtube.com/watch?v=TGzZ8jCX4y0
date: '2026-03-20'
duration: 33:56
model: youtube-captions (en-orig)
transcript: true
---

# Lec 49 Attention Part2

## Transcript


Welcome back So now let us define what
is called as the attention vector
So given a row of Q
okay
denoted by
uh small Q that is there in uh
R
DV
Okay
Compute
Okay
Compute the following quantities
to get the attention Okay attention is
again you know its its mathematically
a vector that we define okay lets
define that in a while the first thing
that we do is so
define si to be
skranspose
ki
for all k in matrix k
okay what do we do
take please note that uh we are defining
the attention vector corresponding to
one row of Q
or rather one one token
every row of Q K and V corresponds to
projections
of one token of data So we are
considering one token of data by taking
one row of Q Okay you take one row of
Q and define attention for that You
know well extend this for all tokens in
a Y So for now let us define the
attention for one token of data by
considering one row of Q So you take
one row of Q Okay And then compute the
inner product of that one particular row
that we have considered with all the row
in matrix K
Do you see what is being done now
Okay Okay we are computing the inner
product of one row of uh Q with all row
of K and calling them SI And how many
SI do we have now
 Well have capital T of them
Okay so this I is equal to
1 to T
Is that all right
Now let
S be equal to
Q transpose capital K transpose Okay
which is
a T length vector
quantifying
the
similarity
between Q and all rows of K
Is it all right
 Q
 uh dimensionality right Q is a row
vector No
Q is a row vector This is 1 cross DV
and this is
DV cross T Correct
Because Q is a row vector Now if its a
row vector then it should be qranspose
right
Okay So now you get this Tlength
vector Okay corresponding to one row
of Q
And this vector S is having the
similarity between
one token or one row of Q Okay With
all the other tokens in K
Is that okay Yeah
where
 yeah
see Q transpose is a Q is a row vector
right
and uh
 K is a row vector
so this becomes an outer product then no
no
 Q into
 yeah because these are all rows right
okay fine Yeah we want a scalar at the
end of the day So if we treat Q as a
row vector then its qki transpose
correct Okay So now this
 no so the see I is the running index No
see we are considering one row of Q
One row of the Q matrix is what we are
considering to define the attention
completely So we take one fixed row of
Q which is what Im calling as Q
small Q right then I take this and get
an inner product with all the rows of K
that is what SI is and I stack them all
and make it a vector which is which is S
correct yeah so this qranspose Kranspose
so please note that this Q is small and
K is the matrix so we are taking inner
product of one row of Q with all rows of
K Okay which to get this S Then we
scale this and uh define SAP
as
so S divide it with uh
square root of DV So this scaling is
done because you know D is typically
very large So if you dont scale it
then itll run to the numerical issues
and you know you want this to be uh
meaningfully conveying the interaction
So you divide it with uh the root of dv
Then
the vector s Okay What is this vector
s This vector s is quantifying the
similarity between
 one Yeah
 Yes
Q transpose
 See Q
transpose Okay hold on Um
so Q is in R DV right
 Okay lets lets lets get this
correct Now Q is in R DV correct
So if we lets lets fix one thing So
if we treat Q to be a row vector
then
it should be
Q transpose
 its correct No qk transpose
 you mean here
 this is qk transpose Yeah Okay
Correct Thats correct Yeah
If you treat Q to be a row vector then
this should be Q transpose Its
correct Yeah Okay So now um this S
contains okay or quantifies the
similarity between one row of Q and or
or rather one token with all the other
tokens Correct
However we want all of this to be
bounded between zero and one
Why
to normalize you know to ensure that
these will correspond to the relative uh
scaling or relative importance of each
of the pairs of uh the uh the Q and each
of the pairs of tokens and if you have a
vector okay so how do you ensure that it
is bounded between zero and one just do
a soft max right so lets do that lets
call alpha to be equal to soft max of
is cap
correct
So now this alpha represent
the scaled similarity
or the similarities
between
Q
and
all the elements of K
Is that okay We are doing all this for
one vector uh in Q So you take one
vector
What are we doing after all Right
Were computing inner product between
one vector and all the other vectors in
K Scaling them so that the similarities
are bounded between 0 and one sum to
one Thats it Okay Finally what we
do is now define attention
So attention vector A
for Q
as now this AQ
is
the
linear combination of all the vectors
in V
Okay Scaled by alphas
thats it
Understand Okay So now what are we
doing
in starting with given data given a
sequence Okay We projected this
sequence onto three subspaces and got
three vectors Q K and V I mean yeah
not three uh we got uh uh three matrices
Q and V which had the vectors
corresponding to each of the token Now
to define the attention corresponding to
a particular token
what did we do we considered the linear
combination of okay all the other
tokens So basically attention
corresponding to a a token is given by
the linear combination of
the V vectors corresponding to all the
other tokens
Got it Now attention corresponding to
each token is always the linear
combination of the V vectors for all the
tokens So what changes from one token
to the other is how much should you
scale each of the V vectors
okay is determined by the inner product
between the Q vector corresponding to
that particular token and the K vector
corresponding to all the other tokens
Thats it
Do you see what is happening here And
by the way uh people give names to this
The Q matrix or Q vector is called the
quiry vector
and K is called the
key vector or key matrix and V is
referred to as the value matrix
See to me all three of them are
projections of data
Okay youre just projecting the given
data onto three different subspaces One
subspace is called the query subspace
The other is called the key subspace
The third is called the value subspace
Now to compute the attention
corresponding to a given token okay
you use the
the query representation okay and
attention corresponding to each of the
query
token is simply the linear combination
of the value tokens always And the
scaling of this linear the the linear
combination of value tokens is given by
the inner product between that query
vector whose attention you are computing
and all the other key tokens Thats it
 So what is alpha I
like alpha was defined for one
 the iat yeah the iat component of alpha
Say alpha is a tlength vector No alpha
is a tlength vector Youre taking the
linear combination of t vectors in the
value matrix Each of the uh each of the
vector in the value matrix is scaled by
one component of alpha Thats it
Is this all right
 Who is asking
 It need not be the same In the most
general form it can be they can have
different dimensions But DQ and D
 they are to be the same of course Yeah
Otherwise the inner products wont work
out Okay But yeah did you understand
the the attention mechanism This is
what is called as attention So now did
we are we uh done with the objective
that we started uh with So we wanted to
get a projection of data that would
capture the interactions between each of
the each of the tokens Did we do that
We actually did that How Through
alpha
Okay So our hypothesis is as follows
The representation corresponding to each
of the token in a sequence is given by
the linear combination of some other
projections of each of the tokens
Thats the hypothesis That is what
attention is all about Why Because
remember this treatment right here we
are saying
its a linear combination of
representations of hidden states
corresponding to each of the inputs
Thats exactly what we are doing here
The representation corresponding to each
of the input token is given by the
linear combination of another projection
of data is what we are saying Now how
do you define what linear combination
should be taken is through the
interactions of that token with all the
other tokens in the sequence Thats it
which is given by alpha Hold on Ill
take questions in a while Im just
trying to algebraically tell you whats
happening here So is the algebra clear
And by the way let me complete the
story So this is attention
corresponding to
a single token and you do it for all
tokens Okay if you do it for all
tokens typically so attention
mechanism attention
corresponding to
Q K and V okay is given by
see all these are matrices Okay And
the multiplication that we are doing
here are matrix multiplications This is
the equation that you see everywhere
right So what you get after this when
you do this what do you get So this is
basically you see this entire thing as a
projection of X
start with a
T cross D matrix What you get is a
representation
which is in the DV space Thats it The
output of this so called attention
block okay it can be seen as a
function on your data that projects onto
another space of dimensions DV Thats
it
You see whats happening here
right So we started with this goal
right We wanted to learn a projection
of data onto a space
such that this projection captures
interactions between each of the
individual tokens in the sequence And
we did this through this particular set
of transformations
All this is I mean except for the
softmax operation here everything is
linear
Right Definition of Q K and V all of
them are linear projections Okay And
definition of attention also is linear
because youre taking a linear
combination of the columns of or rather
the elements of V or the rows of V uh
but there is a softmax in between you
know that that is defining what should
be the scale with which all of the value
vectors have to be scaled so that you
get the attention corresponding to each
of it
you see this so look at this entire
attention mechanism as a black box that
would take your data which is in dv
dimens dimensional space and projects
projects that onto a dv dimensional
space and this projection is defined in
such a way that the interaction between
each of the tokens within the data point
is captured
Okay So give a given a t cross d
sequence it will give you a t cross dv
sequence
Okay such that the interactions are
captured and this is the uh algebra
behind it So let me answer questions
now
 You had a question Yeah
Uh so whenever we are planning to go
ahead with the projection so we can
actually multiply by X with W which is P
cross DV and then we can directly get
this projection
 Mhm
 So
we took three matrix no which also takes
to this Now even if we take five kind
multiplications also it will take to
this Why did we stop with three is my
question
 Oh okay Uh the question is what is
sacroscent about this particular choice
of three projections See
you the idea is this right You want an
inner product to you somehow the somehow
there should be an inner product between
the pairs of tokens
 That is
 right So you need two of them
 Yeah
 And then you you scale them with the
input itself In fact there are studies
where where people show that you can do
away with the V matrix and have only two
of the projections and scale the X
itself to get the similar effect Does
that answer your question Yeah people
have shown that Okay Inner products
have to be taken and then use that inner
product scaled inner product to uh take
a linear combination of several tokens
Instead of taking linear combination of
tokens you take the linear combination
of projections of tokens Thats it
Okay And there have been studies where
people have shown that you can do away
with the value so called value matrix
and have only two projections and still
get the same effect So there the
definition of attention will be alpha i
 times x i
 Yeah
because each of the vector is attending
to the other vector through inner
products
mean
 see when I if I ask for your attention
Im asking you to align with me right so
alignment mathematically sort of inner
product I mean thats the thats the
closest explanation that I can give
 us we mean by attention that we filter
out most of the information and only
attend to it
 well no I mean see I theres this is all
it it is to it and as you know I can I
only care with the math
right so there are inner products
general linear combinations Thats it
Now a more interesting question to ask
is why would this architecture okay so
lead to uh good approximations in terms
of empirical risk minimization There
have been results that would show that
this is a universal approximator In
fact this is not a transformer yet the
transformer architecture still has a few
more ingredients on top of it which Ill
let you know which will make it a
universal approximator So as long as it
is a it is a universal approximator I
dont care However what has been shown
is that this sort of an architecture
scales with the length of sequences
This does not have the problem of
vanishing gradients Why can somebody
see that Because there is no
recurrence
There are only inner products right
There is no there is no recurrence here
And there is no multiplying with the
same matrix multiple times And the when
when the gradients flow they dont flow
in I mean that direction which would
create the vanishing gradient problems
you know thats why it could scale for
larger lengths of sequences and thats
why this is the state of I mean go to
architecture for sequence modeling now
okay as long as its a good regularizer
and it is a universal approximator
thats all I care for okay yeah any
other question
 sir
couple minutes back You mentioned the in
the definition of attention that um for
a specific query vector uh we are
actually like doing some kind of um
weighted sum of all of the value vectors
of the entire uh
 not some kind of exact linear
combination of value vectors for each
query vector
 Do we include that specific query
vectors uh token as well in the
summation
You do know because if there are t
number of tokens
 youll have to do that as well
 So basically
can attend to itself
 Of course it will right
 Yeah
So why are not only considering the
alpha alpha Why we are multi another
vector So this is see alpha is a
scalar Alpha I is a scalar
 I ala
 they are all scalers
 VIs are vectors
right So we are looking at linear
combinations of value vectors What you
need given a vector q you need a vector
that corresponds to the representation
that that that that corresponds to
representation of this vector So look
at this right Finally the projection is
that given a vector you need a vector
alpha I is a scalar right so I need a
vector
 alpha 1
youre saying the entire vector itself
Im sorry alpha itself as a
representation is it one can do that one
can take only alpha as a representation
corresp as the representation for a
given query right But the thing is uh
its not the its not only the I mean I
can only give you an intu intuitive way
to do it I mean mathematically speaking
its possible you can use alphas
themselves as attention and go ahead
However my intuition says that
what you actually care about right
What the hypo as I said the hypothesis
is that the representation corresponding
to each of the token is a linear
combination of representations
corresponding to all other tokens in the
sequence is the climb
So to do that I mean its not the
attention that is a better
representation It is the linear
basically Im saying that every token in
my sequence has information about every
other token So if I have to represent
uh one token I will represent that as a
linear combination of all other tokens
Right So that linear how much
information does every other token has
uh with respect to one given token is
captured by alphas So I scale okay each
the representation of every token in my
sequence by the amount of information
that it corres that it contains uh
regarding the other token and take a
linear combination thats the idea again
as I said no its only intuitive so now
if you stop at stop stop at alpha and
say that this is the I I will use this
as a representation can be used
mathematically nothing nothing change I
mean it does not prevent its theres no
its not wrong to use alpha as a
representation yeah Actually we got away
with the recurrence matrix HD
 No recurrence was w right I mean the
recurrence was yeah recurrence through
hidden state is is gotten rid of
 hidden state
 correct
 How does it ensure that it captures
 I told you right Universal
approximation thats it So this is a
function approximator
stops there Yeah
I mean all that was being done using the
hidden states is now being done using
this alpha matrix Thats it Or the
value matrix
 At least thats the hope and claim
 Yeah go ahead
 Uh we can calculate the attention by
using only X
 instead of V
 Instead of taking three different
transformations
 you do everything with X itself
 Yeah But like doing a learnable
transformation
 does that like help to learn more or
learn faster
 Correct Learn more See if you do not
have those WQV and WK right Uh theres
nothing learnable here
right But you need to learn the
projection isnt it The projection has
to be learned and thats why you have
those matrices
I still did not get what is the
difference between K and
 mathematically there is no difference
there still thats why I did not I mean
I did not start the entire discussion by
saying that this is query key and value
there are three names thats it to me
there are three different linear
projections of data
project data onto three linear subspaces
okay use two of them to define inner
products use the third one to take inner
the linear combination thats
call them whatever you want
when its called query key value because
you take a vector start with a query
okay I mean match it with all the keys
and then use values to take a whatever
right a linear combination or whatever I
mean to me start with data project it
onto three subspaces linear subspaces
use two to define another products use
the third to take linear combination
thats
Thats all attention is about Yeah
Question
 this No here
How are we getting V By projecting data
onto WV
So how are we getting WV WKV WQ
 ERM
We have a loss function Well do
gradient descent to get this Thats it
Thats what training is all about You
know when if you train an LLM all you
are doing is getting this WKWB and and
you you hear that there are you know 30
billion parameters 100 billion
parameters and so on Theyre actually
the entries of these matrices
elements of this matrix actually
So what is point of scaling
s to scap
 I told you right uh if you dont do it
then uh since dv or these vectors are of
very large dimensions itll itll run
into numerical error So youll have to
ensure that they are scaled
alpha wont be affected
Huh Alpha wont be affected But what
happens is if you take these soft max
with vectors that are not scaled then
all of them might converge into one
point right I mean you will not youll
not get it spread
okay so ensure that uh its its pretty
well spread youll have to divide it
with the dimensionality for a large
value thats it
 so here we fix the capital T and this
 capital T is always fixed thats your
data
 uh number of tokens in one second
 Oh no the question is how do we deal
with different number of tokens in
different uh data point Okay Uh zero
padding in transformers what you do is
you take the highest length Okay And
then zero pad it Thats it And thats
what is called as context window these
days
And uh the state of the art models right
now has a t thats equal to 1 billion
tokens
Not billion sorry 1 million tokens
Right Yeah So 256 tokens and 512k
tokens and so on Now it has reached a
million tokens just uh zero pad them and
then do it Thats how it is done in
practice
 Yeah
 The initial matrix is the x
 that is also learned
 No no that is your data No input data
that one hot thats one hot
representation
 Start with one hot representation
 Okay your point is correct Typically
what is done is even before doing this
theres one other linear projection that
is learned
which is called uh the embedding right
so you learn another projection before
you do this doesnt matter you can start
with mathematically speak you can start
with a one hot vector and do all this as
well
 lets say we want to do
so basically that would be x2 times
 no you do it one point at a time right
See this batch processing comes up in uh
this thing gradient descent not here
 I cant retention for multiple data
points
 Thats a different question So you can
you can I mean thats shredding and also
how do you parallelize training etc
Thats beyond the scope of this
particular course So the way to do it
is consider each data point separately
and do the training Thats it Which is
the batch gradient descent that we do
SGD doing it individually would
 thats as I said those are all questions
that are valid which will not be
discussed in this particular course
there are 100 ways to theres also this
KV cache problem if you look at it this
is uh theres a order of n squ already
know or order order t squ
because we are computing inner products
here see if t is very large this is not
the most efficient way of doing it okay
and there are these methods called you
know kv cache uh and all other methods
where people have tried to you might
have heard of this these things called
flash attention and so on right you know
where the whole problem is to get rid of
this t² and try to bring it down to
close to linear computations there are
there are ways to do that but not for
this course this course is just to
introduce maybe the next course Ill
talk about all those for now treat each
data point individually and compute
attention for a data point and then do
gradient descent thats it
 if you concatenate
 point taken But not for this course
Yeah Anything else Yeah
 So this is a universal function
approximator Why dont we use this
instead of a neural network You only
have to learn
 Thats exactly what we are doing right
now
 Todays LLMs are transformers
 Theres only three learnable
 Well yeah I mean it doesnt matter
right Depends on number of parameters
Now there are I mean there are billions
of parameters instead of using see this
does not give you lesser number of
parameters or anything It is just
another type of regularizer as I keep
saying right Its an architectural
novelty Thats it Yeah
 I wanted to introduce nonlinearity to
each of them
 Well do that in a while Transfer This
is not transformer This is just
attention projection
 all these three vectors which we can
apply individually to each
 Instead of doing that they put an MLP
after this
Right That is what a transformer does
Yeah So you need that otherwise is
almost linear No except for the softmax
computation here In fact this is the uh
the fact that is used to try to bring it
down to linearity
because if you can approximate this
softmax with something that is linear
then this entire operation becomes
linear and you can perhaps reduce the
computation Thats what is done in some
of these methods as well Okay anyway
lets not get there Is this all right
I mean algebraically what is being done
in attention Okay So now lets lets
look at what happens in the uh in in
transformer right Um
okay So there is another uh small bit
of information that I need to tell you
Theres something called multi head
attention
Uh we will stop here and continue in the
next lecture
