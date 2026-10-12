---
id: E2LLi7AB9lQ
title: Lec 45 Recurrent Neural Networks(RNNs)
url: https://www.youtube.com/watch?v=E2LLi7AB9lQ
date: '2026-03-12'
duration: 38:05
model: youtube-captions (en-orig)
transcript: true
---

# Lec 45 Recurrent Neural Networks(RNNs)

## Transcript


Welcome everyone We are now discussing
different architectural
changes that that we can do to MLP to
cater to several different topologies of
data and we looked at one such
architecture which we called the
convolutional neural networks in the
last class So in this uh version we
will look at uh another class of
architectures that are called recurrent
neural networks or RNN
So this these kinds of neural networks
are typically applied to data that has a
sequential topology So what is a
sequence So sequence is a set of
observations that has one more temporal
observation There is no strict
definition of what a sequence is because
one can okay this is one other important
point that I want to make
See one can rearrange uh the data which
are tensors for our case
into any topology and use any
architecture So what I mean to say is
that suppose you have a sequence okay
you can arrange that as an image and use
CNN for it and suppose you have an image
right you can arrange that as a sequence
and use recurrent architectures for it
thats exactly what is done in you know
something called vit visual transformer
which we will see later so this is an
important point that you can rearrange
your data into whatever topology that
you would want and use any architecture
Okay But typically no typically you
assume that your data has a certain type
of topology and use that particular kind
of uh architecture
So today most of the machine learning
tasks are solved using this architecture
called transformer So transformers are
originally designed were originally
designed for a sequential uh data
topology but now they can be applied for
image kind of topology as well which we
will see in the later uh parts of the
course But the point that I wanted to
make is its not strict that okay if you
have a sequence youll have to use a
recurrent neural networking if you have
an image you have to use a CNN or
anything So any kind of architecture
can be used on any data as long as you
can view your data or rather rearrange
your data that suits that particular
architecture So thats the point Okay
So recurrent neural networks um so
suited for
sequential data topology
Now a sequence data lets consider one
particular data point So lets do
everything for one data point Consider
a data point
to be of following
nature
So we have x to be equal to So this now
x is a sequence
So x2
x capital t
where
xt
is a d dimensional vector So this is a
single data point
Understand So what we have is a
sequence of vectors a tl length capital
tl length sequence of vectors
each of the element of this sequence is
a d dimensional vector
you see what Im saying okay so examples
for this can be
uh natural language
and it can be a clinical time series
It can be a video or anything Right So
why how is a natural language a sequence
like this You have a sentence A
sentence is a collection of capital T
number of words Okay So each word can
be represented as a dimensional vector
using one hot representation in the
dictionary Thats one of the
representations So you have every
sentence is a d dimensional is a
tlength sequence Okay How do you look
at clinical time theories Uh this way
Suppose you are making measurements
Okay And you take you make five six
clinical measurements at every time and
you make 100 measurements over time
That becomes one data point So please
note that we are talking about one data
points and our data set will have
several of such time series That would
be a data set Does it make sense And
how is a video uh a sequence is that
every point is now an image a
dimensional image We know how to see an
image as a dimensional vector and that
becomes a sequence
All right Right So now labels for this
or rather if you want to solve
supervised task for this a supervised
task on this can be of multiple types
Okay So let me write that down example
tasks on this this data
one is now sequence classification
So sequence classification is an example
where given a time series you assign a
scalar label to it
Example of this can be um
lets say emotion extraction
from
text
So given a paragraph you tell me whether
this paragraph denotes a happy uh
expression or a sad expression or
something Right So this is a kclass
classification problem and the data that
you have are sequences Does it make
sense
Right So this is one way to look at one
possible task The other more um
prevalent kind of task that is uh that
is considered is sequence
to sequence regressions
These are also called seek to seek
tasks Okay Sequence to sequence
regression tasks Whats an example for
this The classical example is
translation
also called as machine translation
where the input is a is a se is is a
sequence and the labels or outputs are
also sequence
Do you see the point Right So or you
take you know uh video generation
right or you have a video as an input or
a text as an input and you need to
generate a corresponding video a video
corresponding to it So its say you
have a sequence as an input and uh or a
text yeah text as an input and you get a
sequence another sequence as an output
and so on By the way another point is
that one can use these architectures as
Lego blocks Okay And place one uh
after the other for tasks as as as as
one seems fit You already see saw an
example right You know the when when
we whenever we solve a classification
task using CNN you you have several
convolutional layers followed by an MLP
which is also called a fully connected
layer So similarly one can have a
recurrent architecture followed by a
convolutional neural network as well So
an example can be lets say that uh you
need to uh solve this task called image
description meaning you are given an
image as an input and the output has to
be uh natural language description of
what is there in the image Now input
will be convolutional layers So an
image is given as an input to the
convolutional layers Okay generate a
vector on that vector
take that as an input and have a
recurrent architecture as the output
where the recurrent architecture gives
uh a sequence as an output and that
sequence is your output the only thing
is depending upon what your task is your
data has to be in that format meaning
suppose youre solving this task that I
just talked about which is image
description then your data has to be an
image and the corresponding description
thats why thats when you can define a
loss function and solve solve VRM on top
of
Please remember that irrespective of the
architecture okay irrespective of the
task that you are solving erm still
stays the same its the same erm stay
same same gradient descent that we will
use to uh solve the problem
fundamentally whatever we saw in the
first half of the course is is still
remaining right so there is still bias
variance decomposition and so on what
changes is the kind of task that you
solve does it make sense yeah
so yeah so there these are some examples
of how to do it one issue with uh
sequences is that uh every se every data
point that we get may be of different
length
So lets write that in sequential data
every data point
maybe of
different length
If you look at an example suppose
youre solving the translation task
Lets say English to Hindi or something
Every input sentence has a different
length
Capital T is different Okay So now one
one needs to handle that MLP cannot
handle this isnt it Because an MLP or
a fully connected neural network assumes
that every input data data point has the
same dimensionality
Please note that Im not talking about
this RD here Im talking about this
capital T Capital T can be different
for different input points The length
of the sequence can be different So the
architecture has to handle this kind of
a thing Right So to do that
different length and therefore
this MLP
cannot handle them
Unless you zero pad all of them to have
same length and that can be done but
thats thats thats not the uh most
elegant way of doing it The other part
is if you just treat all of these you
know
concatenate all of them and make it into
a d cross t long vector and give it to
an MLP then the sequentiality of uh the
the data will be lost because for an MLP
it doesnt matter if you if you show
that I mean if if you swap the data
dimensions
or rather if you shuffle the input data
dimensions MLP will still uh do the same
thing because the idea of sequentiality
does not exist in an MLP by
construction So youll have to ensure
that the idea of sequentiality is uh
embedded into the architecture and
thats why a new architecture has to be
uh thought of
 learn what
 maybe but explicitly see I I keep
telling you this right an MLP can learn
anything
the thing is if you bias it by having
these kinds of explicit regularizers
itll learn itll learn it better in
whatever sense the faster faster
convergence a better trade off between
bias and variance and so on right okay
so lets look at now with this prelude
lets look at recurrent neural networks
RNN
now see just like we had parameter
sharing across space in CNN in in
recurrent neural networks you have
parameter sharing across time or the
sequential uh the sequence indices this
Okay So there is parameter sharing
across
time
So I wrote time within quotes because if
you look at a natural language right
There is theres no idea of time Its
just the sequentiality There is some
ordinality some ordering Thats it
Right So what does this mean A vanilla
RNN looks like this So we have data
point X to be this way X1 X2
up to XT Please note that this is one
single data point that we are talking
about I I I dont write labels
deliberately uh for a while because Ill
write the uh the current architecture
first and then we will write the labels
So this is one data point that we have
So we define what is called as uh the
hidden state
uh ht
supererscript and subscript HT is equal
to
first you do a okay so before that
before you define the hidden state there
is a pre activation that we define ZT is
equal to uh W
w1
htus one
plus w2 xt
Sorry W2
Dont copy it yet Let me just complete
it Uh
do you mind if I just switch this
notation from being a superscript to a
subscript I didnt do subscript because
you know we have
uh we we have been using subscript to
denote
data points right But uh you know now
Ill be at least for the recurrent
architecture I will I will use
subscripts not to denote data points but
to denote the temporal index Okay So
please uh note this change and otherwise
Ill have to write there will be a
subscript here and superscript there
Itll confuse you So this is xt plus
some b1
Okay And then we define HT to be
uh some sigma times
uh gt
and then you make the output y
to be
so w3
ht
plus b2
Okay So this is uh one of the
definitions of RNN So why why am I
saying one of the definitions is because
as we will see in the end of this class
there are multiple ways to define an RNN
but this is the fundamental idea So now
please note this So what is happening
here is that
in an in a recurrent neural network we
define what is called as a hidden state
HT
Now mathematically speaking all of these
are either linear transformations of
data or nonlinear composites of linear
transformations of data The hidden
state is nothing but a nonlinear
composition of linear transformation of
data Right So ZT which is similar to
the pre activation
uh function that we were using in an MLP
it is simply you take so there it was w
wrpose or w times x was the pre activation
Now here in a recurrent architecture
its a function of both the input X and
the previous hidden state
okay because there is sequentiality we
have to ensure that there is the
sequentiality that is that is maintained
here and HT which is the current hidden
state is a nonlinear composite of ZT
which is the the current activation or
pre activation and output is simply a
linear transformation of the current
hidden state
Does it make sense Okay So this is
called this is sometimes referred to as
a single
RNN cell
If you look at some of the architecture
some of the uh descriptions and
textbook they call this a single RNN
cell So why is whats happening here
So please note uh uh the equation
mathematically its pretty simple How
do you get h0 H0 is initialized
randomly Okay Now ZT which is the
pre activation is taken as a linear uh
function of the previous hidden states
and the data both scaled by some
matrices and w1 w2 w3 are what we are
going to learn through right and the
current hidden state is some nonlinear
composition of zt where sigma is some
nonlinearity
some sigmoid actually it can be
hyperbolic tan or the the the sigmoid
function or anything and the output is
taken to be a linear
transformation of data Okay In fact
there can be a nonlinearity here as
well You know if youre looking at uh
classification problems you need you
need uh it to be bounded between 0 and
one right just linear and only see
what the reason Im sort of
deemphasizing on this particular
structure is that as we will see later
okay these this structure is not sacros
in the sense that you can actually
change this meaning as long as there are
there is a sequentiality the recurrence
form of recurrent neural networks comes
from the fact that
the output and the pre activations are
functions of the previous hidden states
thats
And these functions are linear functions
or ra rather nonlinear composites of
linear functions of either pre previous
activations or previous hidden states
and data So there can be multiple
combinations that can be worked out for
this and thats what gives you gives
rise to different architectures And in
fact I was going to mention this anyway
Ill mention this There is a paper 2015
paper that came out where the authors
examine
I think you know a few thousands of ways
of combining this and show that all of
them on an average lead to a same same
performance as long as there are a few
properties that are met which we will
see So that thats how you sort of
distill everything out okay but this is
a this is one of the primitive
architectures of how RNN is written
Okay Now if I I mean there is one
diagram that people write So how is it
done is that this is if this is one RNN
cell
then what is happening is this So that
is xt
and uh this is uh
w2
and we have uh ht minus one
and this is w1
and this is
yeah zt but there should be a sigma here
as well right so sigma
will give W HT so HT is what goes out
and this is YT and we have W3 here
this is one RNN cell
I mean whatever Ive written using math
just written a diagram to show that is
is this okay
I had
 just a second huh so now okay so maybe
before I continue Ill take questions
yeah tell me
 so the doubt I had was do we run this
back proposition algorithm for every
single time step like at one time step
Hold on to your question Ive not
talked about how to do back propagation
for this yet Just 5 minutes I Ill get
there Yeah
Any questions on this The way the the
architecture is
 not said that yet Yeah So I talked
about parameter sharing across time
Okay So what does that mean So this is
called know typically what happens is uh
theres some people write it this way
have you seen this this sort of a
diagram okay so why is this this is
called a rolled RNN right so you have to
unroll it just complicated terms to just
say that the next RNN cell
will have the same W1 W2 W3
and it continues
So this is parameter sharing across
time
Across time the weight matrices or the
parameters do not change no matter how
long the sequence is
Make sense Yeah Thats thats the kind
of regularizer that we are imposing
here There is in CNNs there was
parameter sharing across space Here
there is parameter sharing across time
So this is what is called as an unrolled
RNN
So I mean using use the same cell RNN
cell multiple times at different times
or you just unroll it You know what
then then how does how does it know Um
this is XT this is XT plus one and so on
Right So how does it know what is the
next data point that is the next vector
that is coming in sequence Have you
noticed what changes here
The parameters dont change What What
changes
 H will change The hidden states will
change Why
Because its a function of the current
input and the previous hidden states
And now you know why it is called an
RNN
By definition the hidden states are
recurrent
Theres recurrence here And I can
unroll it right I can write HT minus1
in terms of HT minus2 H2 HT HTUS2 in
terms of HT minus 3 and so on Theres
proper recurrence here Thats why the
name recurrent neural networks
You see this Now why should we uh share
the parameters across time
So if share the parameters across time
why should that be the case See in in
its a dynamical system right In a
dynamical system typically the
assumption that is made is the
parameters of the system does not change
across time
What am I saying is that suppose we are
looking at language the language does
not change across time
Sometimes it may may be a naive
assumption thats why people move to
something called an attention that we
will see later right but the I mean if
you have if if some of you have studied
signal processing this is very similar
to the linear dynamical system or a
common filter where you assume the
system parameters not to be changing
across time the ABCD matrices of the
dynamical system do not change across
time you keep them constant it is
assuming that the environment which you
are operating in does not change across
its not a function of time is one
reason the other reason is that remember
we said that we need to u cater for
different sequence lengths right if you
share parameters across time you can
actually work with any sequence length
because youre using the exact same
parameters all you need is one other
cell for to do that
okay and remember the description that
we had given for parameter sharing in a
CNN
no matter where a feature appears in the
image our neural network has to rather
our our neuron has to identify where it
is Similar explanation comes in Lets
say that there is a neuron that detects
whether a given word okay is a noun or a
verb No matter where it appears in the
sentence it has to determine whether
its a noun or a verb Thats why you
you do parameter sharing across time
Make sense Yeah Now that comes with
its own problems You know there is this
infamous problem of vanishing gradient
that comes in which well talk about in
a while But yeah So did you understand
the architecture There is parameter
sharing across time Now how do we
accommodate uh the the output uh uh
random variable here depending upon what
your architecture is or rather what your
problem is So lets say that your
problem is that of uh classification
then the way to do it is at the last
cell of the RNN okay when you have
X capital T only that cell will have the
output
okay all the other cells will not have
an output
I mean meaning there it will give you
some output but the loss will be
computed only here
lets call this YCAP so there is YCAP
and Y you compute is at only at the
output
If you take the example of emotion
recognition from a from a from a
paragraph
then the entire paragraph is given one
word at a time to the LSTM or rather RNN
right and at the last cell whatever it
gives as an output is where you tap the
outputs and this the output of this so
basically uh suppose youre solving a K
classification problem then this Y will
be soft max of W3 HD and the softmax
will be of length K so that you get a K
dimensional one vector compute the uh
the output only there and then back
propagate You dont you ignore the
outputs of all these cells
Do you see what Im saying
 Yeah
 You dont No you dont have to because
this is not recurrent
Its just a function of the current
hidden state You dont have to compute
Yeah
Is it clear So this is for
classification Suppose you have to
solve uh translation task you know where
input is a sequence output is a
sequence What do you do then
Yeah So tab the output at each of the
uh each of the xs right So the the way
to do it is so give entire input There
are multiple ways to do that as well So
one way to do it is so you have
so typically this is how it is done okay
in an auto reggressive way where you
have x1 x2 up to xt x capital t you
dont tap okay then the next cell okay
you start tapping the output this is y1
okay now take this y1 and give it as an
input to the next cell
and get your y2 two and do that keep
doing this So this is the the uh the
famous encoder decoder architecture of
generation where you have the input
sentence or input sequence compress it
completely So basically what you are
saying is you are trying to compress all
the information of about the input
sequence in the h the last hidden state
of the input cell and you give that as
an input to the next set of RNN or next
set of cells and ask it to give the
output
is that okay I mean this is I mean this
is these are as I said no these are Lego
blocks you can just plug and play them
uh the way you want depending upon what
problem are you solving one second Ill
take questions in a while Okay Now
there can be two questions uh which Ill
answer right now Now when do you stop
this
You take Y1 and give it as an input uh
to the next one Okay you you get Y2
and take when do you stop in your data
When you are annotating your data you
also have a particular word Okay which
you call as the end of sequence word
EOS
Okay wait till your RNN outputs an EOS
stop then
you get it So every uh every sequence
the data itself the input data itself
will be uh input sequence in one
language then EOS output sequence
corresponding to that language then EOS
So you have an input sequence output
sequence with EOS Now the when you
solve it you solve it using the same ERM
with supervised learning during uh
during uh uh inference Okay Okay By
the way have I told you what inference
is so far
Okay you have a model right You do
erm have a model and then you pass your
test data to your model and get the
labels on that No thats called
inference
Testing basically right Testing is
also referred to as inference in in ML
Okay I thought I had mentioned that
somewhere sometime in the course
Anyway so during inference what you do
is that give the input sequence Okay
tap all the uh at uh the the hidden
states and then take the hidden state uh
and after the end of sequence in the
input sequence comes in So whatever the
RNN gives you as input is your output
because that is you have trained your
neural network in a way uh where
everything that starts after the first
EOS is your output
Okay And the next whenever the next EOS
comes in you take everything between two
EOS as your output Thats it
and uh whatever comes in between is your
target uh translated rather output
sequences Thats it Still not told you
how to do back propagation here Ill
come to that in a while But Im just
talking about how to design uh make
architectural designs while solving
these kinds of problems Okay
questions Now you had one Yeah
 go on
 Yeah uh y is a function of just h
 h capital t yes
 we not giving x as
 thats precisely why attention came
well come to that in a while yeah so
right now the way this architecture is
is written uh the output is only a
function of ht so youre assuming that
everything about the input sequence is
compressed in h capital t
 number of RNN cells depends upon okay
the question is how do you know how many
RNN cells are there depends upon the
number of sequential time steps in the
input and thats a thats a variable
every input will have different number
of RNN RNN cells
 in each data point exactly thats why
you have parameter sharing across time
so thats why its not an issue all you
need to do is just repeat that same cell
and do it do these operations again and
by the way Ive not told you one other
thing see this is only a single layer of
an RNN I can actually stack multiple of
these across depth
You see that So I mean this need not be
Y So I can have another RNN cell I can
have another RNN cell and so on I can
do it depth wise as well You
understand So when you build an
architecture an RNR architecture you
need to specify whats the depth of this
RNN architecture and thats how many
hidden layers you will have across
depth Okay Yeah
 Like you show the MP for the CN Can you
also show the best
 Good question So how uh should I look
at RNN as a modified MLP
Can somebody take a guess I thought I
would ask you ask this question in in
the exam
Think about it Yeah Ill not answer it
right away Think about it you know
how do you modify an MLP uh so that
it it turns into an RNN
Okay
Anything else
equations
 Same thing right So that would be a
function of h capital t Thats it
 You it is here
Yeah
 Exact same equations Exact same
equations Yeah But the hidden state
corresponding to the input is is
compressed uh in in one hidden state and
then it is carried forward Thats it
Okay Uh okay Lets move on uh see as
I said uh suppose you are uh lets say
um
okay so this way this also is a sort of
generative model that you know
conditional generation thats why I told
you in the beginning that okay here is a
statement that Im making so even a
classifier is a generative model
I generally make this statement in the
very first class of my next course on
generative models but yeah so Ill tell
you Why What is a generative model
Its a sampler Okay its basically a
sampler from a distribution Now a
classifier is a sampler for this
conditional distribution isnt it
Isnt a classifier a sampler from P of Y
given X
The output of the neural network will
give you a distribution on P of Y given
X Its a sampler Okay Now any sampler
is a generative model
So a classifier is also a conditional
generative model in the sense that
conditioning on an input on an input
random variable X Okay you are
sampling from another random variable Y
So P of Y given X is what you are
sampling from Now thats why a a
machine translation model right which is
an RNN can also be seen as a generative
model because conditioned on X you are
sampling from P of Y given X where both
X and Y are sequences
You see what Im saying
See thats why I dont want to make this
this this
distinction that oh there is a
generative model and there is
discriminative model Both are samplers
Okay What distribution are you sampling
from in the questioner Typically in the
community if you sample from P of X
given Y then they are called generative
models
Now if you look at all the you know the
the modern day LLMs okay theyre
actually sampling from PF Y given X
where X is your input prompt
You see that Okay And I mean I dont
know if you noticed this right I gave y1
as an input while generating the next
sequence right this is called auto
reggressive generation So what Im
doing is Im modeling P of Y given X
okay as
a product of P of
YT given
this is how Im modeling implicitly by
doing this all Im doing is Im modeling
P of Y given X of course there is a
conditioning here
everything is conditioned on
This is the typical auto reggressive
model right where uh the the the tth
dimension of data uh is modeled the
conditional distribution of the tier
dimension of data is conditioned is
modeled as the product of
uh the the previous uh conditional
distributions thats the auto
reggressive modeling anyway so Ill talk
about autogressive modeling later in
detail so I just this is just a passing
remark but anyway so now you see why
this is a generative model in the sense
that its any sample this generative
model and this we are here sampling from
P of Y given X okay
and uh yeah the point that I wanted to
make was lets say that you are solving
uh the problem of u um image description
as I said the way to do it is start from
an image okay so have CNNs and take a
vector and this vector
is given as an input to an RNN
You generate the description
You see that an image goes as an input
to a CNN and you take a fully you have
an MLP in between You flatten the
layers take a vector and give that
vector as an input to the RNN and then
train it in an auto reggressive manner
or have an auto reggressive
architecture So it generates one word
at a time
Okay thats how it is So the kind of
data that you need for that is you need
an image and the corresponding
description for it
Okay any questions so far
 The RN for the decoder structure will
have a different architecture because we
have we are giving Y as input to the
next cell So some other weight will
also
 No it is its its theres no weight
there We just give it as an input to
the next one Thats it See I can I
can actually take this off Oh sorry
Take this off and write the input to the
next cell as Y1 The same thing
All Im saying is theres no explicit
input to the decoder cell You just take
Y1 and give it as an input to the next
cell Thats it Uh we will stop here
and continue in the next lecture
