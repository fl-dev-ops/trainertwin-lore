---
id: dONDRwX_83E
title: Lec 42 ERM on Neural Networks and Error Backpropagation
url: https://www.youtube.com/watch?v=dONDRwX_83E
date: '2026-03-04'
duration: 47:44
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Lec 42 ERM on Neural Networks and Error Backpropagation

## Transcript

speaker_1: Okay welcome everyone Lets look at uh
erm on neural networks
So we start with uh x in RD and y in
some rk
get r also So we have data as usual
which are samples
drawn id from the distribution
h theta of x is
the neural network with w1 times x sigma
here and w2 lets say we have this
neural network for ease So we need our
theta star
to be equal to the minimal
arg min of the empirical disk which is 1
 n i is 1 through n We have some loss
function
y i right this is our standard erm that
we do Now how do we do this for neural
networks
We use
the gradient descent
We already seen what gradient descent
is This is
some for times we have the empirical
risk
Lets call this rcap
rcap of theta Its a function of theta
Rcap of theta Take the derivative of
this with respect to this is standard
gradient descent that we do Right Now
what is important is how do we compute
rcap the derivative of rcap theta with
respect to theta for these kinds of
functions Right The question
so how to compute
the gradient
of the empirical risk with respect to
theta for neural networks
The solution is the chain rule
Composite functions are the gradients of
composite functions are uh computed
using chain rule We all know that
right The gradient of e power sin x
squ
Start from the innermost function take
the derivative
keep hopping Thats exactly what we do
 Okay See chain rule for neural
network has a fancy name Its called
error back propagation
and well well work uh uh the back
propagation algorithm This is this is
the algorithm that the Hinton came up
with right so its sort of uh made uh
the community
try neural network so to speak or I mean
you know what training is simply doing
radian descent within okay lets look at
uh chain rule for these kinds of
composite functions that we have which
is called the error back propagation
algorithm
See to do that uh just to ensure that uh
that you know you appreciate the
equations that are there no I will
resort to the scalar form
even though the implementation standard
implementations today are done using
vectorzed operations I will do it uh
assuming I mean I I will assume I mean I
will resort to uh the scalar form when I
work out the back propagation because it
its called error back propagation for a
reason So those kinds of uh nice
equations come out only if we look at
the scalar form of things Okay So let
us work uh error back propagation So
this is back prop for a neural network
So theres a lot of notations I will
just write that notation now So
notations
So maybe before I write the notations I
will write the diagram
So we have data which is uh X which is
in RD right So we have D dimensions of
it 1 2 3 4 up to so this is X in RD
So note that
Im now using scalers to do everything
Okay So there is there are a few
neurons here
in the first layer
neurons in the second layer and so on
Okay Now what happens is Ill take this
as the lith layer
L
well take this as the lith layer Hold
on Just dont write yet Ill complete
the notations and then you can copy
Uh this is L minus first layer
L layer and we also need an L
L plus first layer Okay
Then what happens is that this is
connected to all of this
this neuron and this is connected to
Do you see whats happening here Okay
So in our vector notation see please
note that every dimension of data here
is connected to one neuron
You see what Im saying every
dimensions of every dimension of data
here right is connected to
all neurons individually Okay Now in
our vectorzed notation that forms one
column of the W matrix So every layer
of neural network will now have one W
matrix Okay And how many columns will
this W matrix have Itll have those
many columns as there are number of
neurons in a layer
Okay every all data dimensions connect
to every single neuron Okay
whose weight with the weights that are
given by one column of the W matrix that
defines a layer Is this clear to all of
you Okay And there are as many W
matrices as there are number of layers
Now if I write all these connections
the diagram will look very messy Thats
why its called a neural network Have
you seen that diagram Right I mean
they show that there are all so many
connection that will happen So it itll
look like this If you want me to do
this is connected one
here right And this
you see what Im saying This is how
this is why its neural network so to
speak Yeah
 Thats a hyperparameter
How do you choose the number of neurons
in every layer Its a hyperparameter
Thats a design choice Okay theres no
one typical answer to it See please
note that uh if you look at this part
right uh this the output of this
particular layer can be seen as input to
another neural network thats going on
I mean thats the nature of any
composite function right Thats how it
works Is this clear Okay So now this
is how it is Let me write down the
notations So let L so notations
So L is the current layer
So J is the
index
of a neuron
in the Lith layer
Okay And Kind
of a neuron
in the
L minus first layer
Understand Right
And lets say I
is the index of
in the
L plus first layer
Now this is important We have W
J K L
This is weight
connecting
neuron K
to neuron
J
Please note that neuron K is in L minus
first layer and neuron J is in L layer
So W JK K L is the weight that connects
K to J So this is how it is right So
uh index of this is in L minus one K to
J Yeah So lets say that this is the
neuron that we are talking about it
becomes too messy So if this is the
K or J what is this This is J This is
J neuron and this is K neuron Okay And
there is a weight that connects these
two And this is W
JK
So this is an element of that particular
matrix that we are looking at Is that
all right
Also note that the elements of the
column of this matrix that defines a
particular layer Okay Uh those
contains the weights that connect a
particular layer in the next lay next
neuron All those weights are stacked
into a particular column Okay If
youre looking at scalers then there
are these many connections W JKL
defines the weight connecting neuron K
to neuron J
Is that all right Okay Uh
so we have uh uh so B J L is the the
bias
of neuron J
in layer L
Okay
Now let me define a few more things
here Define
uh Z J L as follows
J K L
A K L minus one plus B J L and this is
over K
where
uh a J
of L is
sigma
of CJ L
Okay So now these two things are called
the activations and uh uh the
pre activation uh of a particular
neuron What is this See what is this
operation And this operation is wrppose
X
Right So now we know that the kind of
operations that every neuron does is
take the inner product and then pass it
through the nonlinearity Okay So well
define a variable called this
pre activation uh
pre activation output Okay which is
simply the linear production of data
before the activation function or before
the nonlinearity and whatever comes out
of the activity uh sorry the uh uh the
uh nonlinearity is called the activation
of that particular neuron Is that all
right So this operation is nothing but
wrpose x right thats exactly what it
is Now let us uh with this and by the
way please note that for the first layer
this a k or a jl is simply the input
that all right okay so let us define
this uh so z jl
be the
pre activation
output
of neuron
J in layer L
and we have A J L is the
output or activation its also called
activation
or output
of
J neuron H
in the Lith layer
Is it all right now Notations are
clear Let me just uh flash them again
so that theyre all on the same page
Any questions on notations
Now what do we want to do We now have
to find uh the gradient of the empirical
risk RC cap with respect to all these wj
kls Thats what we will do now Is that
all right See why did I write it as a
scalar is because
um when you write chain rule for
multiple variables right
do you know how chain rule applies for
multiple variables
You have to take the derivative huh you
have to take the derivative with respect
to each path and then sum them through
right so that comes up only if you write
it as an explicit summation here thats
why I wrote the scalers let me let me
write that notations are clear lets
move on now okay so now there are uh two
things that one needs to do okay uh when
you compute the gradient
uh lets to compute the gradients
Suppose
so rcap
denotes
the uh empirical risk
Okay we want
the derivative of RCAP with respect to
W
What was that J KL
This is what we need Correct We get
this then we can do it for every each of
the parameters and then do the gradient
descent Correct We want this So to do
this
lets define
the error
for a single neuron
in layer L
in layer L as follows
delta J L So write this as the
derivative of R the the
function that we are trying to uh take
the derivative with respect to with
this is with respect to this
Okay So let me just give you an
overview of how we go about solving this
problem before we go with the algebra
See the idea is very simple Now here is
uh where we have uh after many layers we
have we have to compute rcap right we
have to compute the rcap Now if you
want to find the derivative of uh rcap
with respect to some weight here uh the
dependence of this particular weight on
rcap is through every path this wjk has
seen till rcap isnt it right so we have
to traverse that path thats all it is
so thats what chain rule does isnt it
if you have a composite function if you
want to take the derivative of the
outermost function with respect to a
variable that is inside the composition
then you traverse the entire path path
back thats the whole idea so to do that
what we have to do is that that well
have to come back I mean thats why the
name back we well see the algebra very
nicely so we start to take the
derivative of the loss function or the
the empirical risk with respect to the
pre activation which is
Z okay and then then then we use this to
compute uh the the derivative of this
with respect to the the layer before it
and so on till we reach that WJ Thats
the idea Okay So lets do that Lets
do the algebra This is a very important
variable This is the the derivative of
the empirical risk RCAP with respect to
the pre activation
of the neuron J at layer L Is that all
right Okay So this is very well valid
because this ZJL is a function of WJ
Right And uh the RC cap the final RCAP
will be a function of function of ZJL as
well Do you see that Okay And by the
way what is RCAP
So we know that RCAP is
uh
H theta of XI YI Correct
Now since h theta depends on w jk and it
depends on zj and thats why the
derivative of rcap with respect to zj is
well defined correct yeah
okay so let us look at this now to
compute
and by the way again one more uh point
to be made is the way we will go about
this attack this problem is we will
establish a relationship
between this error component in the lth
layer and the error component in the l
minus first layer
You see what Im saying So this this
so called error is now defined for every
neuron in each layer Isnt it Okay
Now what we will do first is that we
will establish a relationship Okay
Between the error in the L plus first layer
and the error in the L layer
Okay So to reach to the derivative of
or or rather to reach to the weight of
JK at the layer L we will do it through
the error in the layers that come after
that
You see why it it is to be done that way
because the the empirical risk is
computed at the final layer The
dependence of this empirical risk or
rather the dependence of the weight in
some layer in between uh on the
empirical risk is through every neuron
that comes between these two and
therefore if we compute the error with
respect to the uh the last layer and
then relate that error to the error in
the previous layer and so on perhaps we
can reach to uh the gradient of this uh
loss with respect to a neuron that is in
some intermediate layer Thats the
idea Now the first thing that is to be
done is well have to compute or rather
well have to establish a relationship
between the error in the l layer and the
error that is computed in the l minus
first layer and so on To do that well
have to start by computing the error in
the final layer Let thats what we will
do now Is is it clear Okay So to
compute error
for the final layer
capital lith layer
So to do this well have to compute uh
del j l
Note that we do this for every single
neuron Right So this is uh del rcap by
del z j l
This is equal to
this is okay Why is this the case The
dependence
of RCAP on ZJL right can be written
through A as well And please note that
a capital L is the output of the neural
network
H theta of X is equal to A
You see that maybe just write let me
just write that
by definition
Correct Yeah
Z
 because there is uh there is an
activation in between No well just
see that So well have to take the
derivative of that as well Let me write
that So now this is equal to
the activation that is computed on ZJL
The derivative of
this with respect to ZJL is simply
the derivative of this
Do you see this
See since
Al is simply
or
 yeah this is Alj
Okay
The derivative of a LJ with respect to
ZJL is simply the derivative of the
activation computed at ZJL Correct
Thats thats obvious See since we are
looking at derivatives of the
activations no these functions have to
be differentiable
Okay you see this So we got this
particular term So now we know how to
compute this particular term What about
the first term
depends upon the last function So now
first term lets lets do that
Now del rcap by del a j l can be
computed y
is the derivative of
think its better if we do it for single
data point right
so already too many uh this thing so
this is equal to
um
ALJ minus loss computed not not minus
hold on just dont write it huh alj and
you have
yj the j component of the particular
output
you see this this is what it is
depending upon what your loss function
is you compute it this way and this this
can be computed Because we know what the
loss function is and depending upon what
the loss function is this can be
computed Let me write this
 Come again Come again
 I mean assuming that Y is a vector Im
talking about the J component of the Y
If A is also a K dimensional vector Y
is also a K dimensional vector So loss
is computed dimension wise I mean
thats why Ive written as derivative of
this with respect to A LJ All scalers
right now Make sense Yeah So can be
computed
See now this means that we now know how
to get this DLG correct So whatever we
are computing let me just put a tick
mark there So this we know how to how
to compute this now Is that all right
Okay So now lets to compute
the error that is there in some
hidden layer lith layer for the J
neuron
See the algebra seems a bit clumsy and
involved but all we are doing is chain
rule repeated application of chain rule
Okay So now well do that
So we know that uh del LJ is
the derivative of
the pre activation of
the
J neuron in the L layer Correct
Now please look at this So dependence
of uh the output RCAP okay on ZLJ
is through multiple variables
that come in between RCAP and the Lith
layer
Okay So now if you have uh a composite
function and the dependency of uh the
output is through multiple uh variables
and there are multiple paths parallel
paths then multi variable chain rule
tells you that youll have to add the
partial derivatives along all those
paths correct So now let us do that
Now let me write that down
Yeah So this should be
the derivative of
the activation
uh
what uh index do I use
I J K L everything is taken
M
is already taken T
huh
 T is already taken
 No no If if its not used no we can
take M So this is uh m in l plus 1
and this is uh del z m l plus 1
uh z
j
l and this is summation is over
m
You see this
the what am I saying here The
dependence of RC cap okay
on Z LJ is through every pre activation
that comes in the layer L plus one
Does it make sense Yeah
 So then you have to add
all those partial derivatives that come
along the path Is that okay Okay Now
what is this equal to
 One to the number of neurons in the L plus
first layer
Okay Um
 okay good Good that you reminded me
Thanks Yeah I is already there for
that in our notations
On a lighter note when youre doing
algebra like this error in my brain
gets propagated through

 Is it okay Now we already know that
this term the first term what is the
first term
First term is del l plus 1
 i Yeah its correct
by definition
And to compute the second part lets
lets look at what the second part is
Consider
what is this equal to
uh to do this
well have to write Z I L plus 1
is given by
J
W I J
A J L
 plus B I L plus 1
So we wrote all this very carefully last
night So so that the indices should not
be mistaken
Okay
Now this is equal to

w i j l plus 1
What is aj Aj is sigma because we need
it in terms of z So plus B
I L plus 1
This is Z I L plus 1
Okay Now if I take the derivative of
this
with respect to Z I
Z I at L What will I get
W I J
at L plus 1 times
the derivative of this sigma ash time
evaluated at Z LJ Is this all right
Why is this the case
Because all the other terms here go to
zero
You see that Why is that the case
Because yeah there the dependence is
only on one particular weight and
everything else will go to zero So we
got this particular term as well Okay
Now
here was J Was it J Yeah it is J
Thanks Yeah
theres an idea called mixture of
experts in LLMs or rather even in neural
networks committee of experts We will
see when we look at boosting algorithms
Uh so this this class is like an MOE If
one makes a mistake the other will
point it out That was a joke by the
way

Okay So now we got this What why did
we do this Well have to substitute
this here right So this implies are um
so d
L
no d
L is now summation by I
L plus 1 times
W I J L plus 1
So I put bracket there Okay Into
evaluated at Z JL
See this is the most beautiful part of
back propagation Okay
Look at whats happening here If you
ignore this particular term Okay All
we are saying is the error associated
with the neuron the J neuron in layer L
okay is the linear combination of the
error associated with all the neurons in
the L plus plus first layer and the linear
combination is weighted by the weights
that are connecting uh the layer L and
L plus 1
you see that
see if you look at uh the data flow from
the input to the output At every layer
the activations or the pre activations
are given by the weighted linear
combinations of the activations in the
previous layers This is the forward
pass
While you are computing the error the
errors also get linearly combinate
combined Okay But in the reverse
direction thats why the name the
errors are propagating in the backward
direction
Right and the the propagation is
weighted by the same weights that that
propagate the data from the first layer
to the last layer
This thats why this equation is so
elegant You see the errors are getting
propagated backwards because the error
in the layer L okay is given as the
linear combination of error in the layer
L plus 1 weighted by the same weights that
connect the neurons from the layer L to
layer L plus 1 And of course there is this
term just ignore it I mean for the sake
of interpretation Does it make sense
Yeah Thats why the name error back
propagation
Yeah error gets propagated backwards
uh by the weights and therefore the name
back propagation Okay
No small L is capital L is only for the
 layer
 last layer Everything else is small L
Oh does this look like capital L No
this is small L
That thats small L Yeah capital L is
only for the last layer right This is
for all layers Once you basically the
idea is you compute the the error at the
last layer and then use the this
recursive thing and back propagate it
right So once you have this so finally
to compute
So finally we want rcap
the derivative of this with respect to
this thing right this is what we wanted
now thats given by
again use the chain rule the dependence
of uh this
is through
uh the activations
time del Z J L divid by del W J K L
and what is this This is
okay Uh do you notice notationally Ive
been using this do for derivative and
delta
 for the error Do you notice that
 Okay Ive been consistent right
 Yes
 Okay
this is D L And what is this The
derivative of uh
thats thats actually pretty easy What
is that Thats
a K L minus one Please
uh verify that its pretty simple
because this is given by
sum over uh
no a k is given by sum over all this
right no
z jl is given by uh the sum over this
akl minus one and this multiplied by w
jk and to take the derivative only that
particular term will survive and thats
why it is this okay now we know both of
this do we know dl delta lj we know how
to do it this is computed via
computed via back prop
This is
in fact computed via what is called as a
forward propagation
Thats it So this completes
backdrop
So we have the gradients that we need
and then do a gradient descent
So summary is as follows right So
lets say that we have a neural network
that we build this way
Now Ill vectorize This is X We have
the first layer W1 We have W2 We have
W3 And we have Y here which is H state
of X
Do you notice that uh the length of the
lines that I have written are
decreasing
So typically when we solve
classification regression problems the
number of neurons progressively will
keep decreasing
Thats the typical choice Okay Because
typically what happens is the
dimensionality of the input is much
lesser than sorry the output is much
lesser than the input Right So you
keep decreasing the dimensionality and
show that your output layer matches uh
the that of the the output uh variable
Now to get one gradient step okay so
well write that to
get
one gradient step
So two things have to be done So first
you do what is called as a forward
propagation
Why do we need forward propagation
To get a
or the output for that particular input
So once you get this what do you do
Do one step off
Is that all right So to get one
gradient step we have to do one forward
pass with a given data point get the
output compute the loss and then do one
full backward pass okay to obtain the
gradients or two this is for one step of
the gradient descent So basically the
computation will get doubled when you
are training This is training This is
basically erm right erm on a neural
network One forward pass one backward
pass is one gradient step By the way
when people uh implement gradient
descent today all of them are vectorzed
Otherwise these summations see you see
this right The kind of operations that
we have here are simply linear products
inner I mean linear combinations All
linear combinations are vector
multiplications Okay Now if you want
to implement this as scalers then youll
have to write for loop over I thats too
much computation instead of that you can
implement all of these as vector vector
inner products basically right so you
vectorize it and thats how you
implement them so these GPUs are
specialized hardware that will do these
kinds of operations which is vector
products theyre theyre theyre
designed to uh do these kinds of
operations thats why they are very
efficient it Okay theyre all matrix
vector multiplications and uh and sums
and products Thats it Okay so this
is how back propagation is done Every
data point you take it one forward pass
compute the output and then
back propagate the error using uh this
particular equation here
layer by layer Then you compute the
gradient and uh I mean everything else
is the same This is training a neural
network and as I already told you when
we do it when we use lets say stoastic
gradient descent do it over batches and
one complete pass through the data set
that you are given is one apoch and
multiple apoch of trainings are done
typically
even your uh you know the the latest
LLMs are trained this way
what changes is the architecture thats
it and the scale of data but the
essential training procedure Is this
error back propagation
Okay
any questions on this
 No
 No no no See for every data point
see to do one gradient step youll have
to invariably do one forward pass and
one backward pass No if you dont do
the forward pass you cant compute
those gradients at all
Thats precisely what we saw today
right To compute the gradient youll
have to find those error terms To find
the error term youll have to find the
error term in the subsequent layer And
to do that you need the output So take
a data point get the output compute
the error and uh get the error of the
previous layer get the error of the
previous layer and so on And the
derivative of the parameter with respect
to the loss uh is dependent on this
layer at the error at that particular
layer through the equations that we saw
So to get the gradient youll have to do
one forward pass and one backward pass
Okay is that all right So this is the
famous error back propagation algorithm
uh which is the workhorse of uh all the
the AI models that you see today But as
I said the scale of the data and the
scale of the number of parameters is is
humongously large And by the way when
they say that they are training neural
networks or training these AI models for
6 months over the data centers that have
tens and thousands of hundreds and
thousands of GPUs all they are doing is
running this error back propagation
algorithm
Okay So now if if if some some of you
can actually come up with an algorithm
that would reduce the computational
complexity of this and can be done
without matrix multiplications
then the then the monopoly of some of
the companies will be just gone So I
keep saying right some of these
companies are one good algorithm away
from bankruptcy Their hardware will not
be sold at all Right Everything is h I
mean it theres so much demand for those
hardware because all you are doing is
doing vector multiplications and those
hardares are are built specifically for
vector multiplications
Right So if there is a way to do erm on
these kinds of composite functions
without vector multiplications then of
course you may get an phrase as
 well Okay so this is about
error back propagation This is how you
do erm So next time when we come and by
the way just to complete the story uh
you can add regular raises to this loss
function and nobody is stopping you
You see the so loss function plus lets
say any kind of regularizer you want and
the same thing happen same thing applies
the only thing is the gradient will
change to obtain the gradient with
respect to the composite function which
is neural network you need backrop for
the gradient of the uh the the
regularizer you dont need back prop you
know you can just compute it and then
add it only the gradient descent
equation would change because gradient
is a linear operator right if you add
some one other term the gradient will
just get added up so it doesnt matter
that way you see that so you can try a
neural network with regularizers as well
explicit regularizers as well So all
the problems that Ive given you in your
assignment can be now solved using
neural networks Only thing is youll
have to code up backdrop you know I will
ask you to code up backdrop as well as a
part of your next assignment Okay so
thats it Next class what we will do
perhaps is uh I will talk about
different architectures uh and you know
how you can see architectural remember I
told you that any kind of choice that we
make on H theta can be viewed as bijian
regularizers I will show you that
convolutional neural network is actually
a regularized heavily regularized MLP
Yeah we will see a couple of
architectures maybe CNN RNN and
transformers and then we will move on to
the other algorithms uh the ensemble
methods and so on Okay Okay Thank
you Thats it for todays class
