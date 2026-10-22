---
id: EydAoMbslkc
title: Lec 30 Linear Models for Classification
url: https://www.youtube.com/watch?v=EydAoMbslkc
date: '2026-02-18'
duration: 33:29
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Lec 30 Linear Models for Classification

## Transcript

speaker_1: Okay So so far uh we saw I mean
theres a slight nuance there a slight
change Yeah Question
Yeah
Now why do you think uh independence
should lead to better erm So its just
a model choice
See you still remember that the
fundamental question that you are trying
to answer is what is the underlying
distribution that is generating the
data
So everything is a guess in the sense
that you make an assumption that this
has this functional form and estimate
All that we are doing is we make a guess
about what the underlying distribution
is and estimate its parameters Now any
transformation on data that you do is
implicitly making an assumption See
again if you are using squared or loss
as loss you are already making an
assumption that your data is gausian or
rather the underlying distribution is
gausian All that you are youre playing
with is the mean of that which is a
function of this Now theres no reason
why you should believe that uh uh of
course learning a good transformation
would definitely aid but what is a good
transformation its only post fact right
so theres theres no theres theres no
theres no uh you know preemptive way of
knowing what a good transformation is
however
suppose your transformation is such that
they can estimate any function to
arbitrary closeness
you know what Im saying right Just like
GMMs suppose you know what your question
is similar to asking what should be the
distributional assumption that I make
when I am solving a maximum likelihood
estimate
the every model is I mean I as I keep
saying no every model is a bad model
some of them are useful so now the
question is which of them is useful you
choose a model that is expressive enough
so what do you mean by being expressive
enough its if its if the functional
form is general enough uh to estimate or
approximate any function to arbitrary
closeness thats a good thats an
expressive enough model to work with
which are neural networks See why are
neural networks the the go to choice for
machine learning today is because of
this particular reason is that they are
the transformations that are that can be
mathematically proven to estimate any
function to arbitrary closeness Its
called universal approximation theorem
of the sigmoids that well see later in
the course Thats why you make such a
choice H
No no no I I did not make that
statement I just asked you if you make
a GMM assumption on the class
conditional density what happens to the
ERM loss function I did not answer that
question I didnt say that neural
networks are equivalent to that In
fact neural networks with a particular
type of activation function called RBFs
can be shown to be equivalent to GMMS
Not all Okay
Okay So lets look at any other
question on linear models Yeah
 Only if you assume if you if you if you
assume that your loss function is
squared error Yes
 In the same
case
 No What do you mean by that
It has to
 correct So if I take two different
assumptions
uh no even then not necessarily the h
function will have a scale thats it
the h theta function will just have a
scale to it thats it yeah okay so let
us look at this slight modification that
we have to do in the framework to uh
accommodate the classification problems
right classification problems are d is
x i yi
And by the way did you note that Ive
been interchanging small n and capital
n
 Yeah So I just noticed it
Its the human error
See whenever I write that Ill write
that as 1 by n Right So thats okay
Its now x i is in rd
and yi is in
Right In this case how do you design
your h function See the h function
should be from x to y Correct
Now if I if I make my h theta of x to be
theta transpose x then uh the the range
space of this h function does not
correspond to
uh the other random variable the label
random variable that we have So I
hesitate to call it label You see you
know why Okay Yeah So still lets
lets label it as a label So the label
random variable So well have to ensure
that the the ranges match you know how
do we do that is the question h uh now
well take so basically what is done is
h theta of x so well say with this
the range
range space of h of x
wont
Y So now what do we have to do Just do
a composition So you make h theta of x
to be equal to some function
sigma of linear function of theta Okay
where
sigma is 1 by 1 plus e power
sigma of t is 1x 1 1 by 1 plus e power
minus t Now sigma t right
is
bounded between 0 and 1
You want a name for this function
Yeah its actually yeah call it sigmoid
function if you want
I dont want to call it sigmoid function
because typical definition of sigmoid
function I mean that uh this guy Syenco
gave in his original paper on neural
networks is that any function that
asytoically goes to one right side and
goes to zero in the left side is called
a sigmoid function Doesnt matter what
happens in between Okay But yeah so
this is also one of the sigmoid
functions because at the limit of t
equal to infinity it goes to one At the
limit of t equal to0 it goes to zero
Right But its bounded between 0 and
one Thats all we need Okay So now
this is you uh you make your uh h of ht
h theta of x to be sigma of theta
transpose x And by the way you can do
this for a generalized linear model as
well right It can be sigma of theta
transpose of f of x as well Anything
that bounds it between 0 and one So
this is for the case of binary
classification
So how do you decide finally So your
final classifier
so what do we call it We call it h of x
is equal to
so class one if if
h theta of x is greater than some to
zero otherwise
to is a hyperparameter
Uh how did I no h theta itself I defined
as sigma of theta transpose x
Yeah
Is that okay Okay so this is how you
design the final classifier for the case
of binary classification So what do you
do for Kclass classification Let us
define that
Now first define
H theta of X to be equal to
now theta times X Okay So let us write out
the dimensions first X is in RD and Y
is in
uh
this counting from zero problem is so
difficult for me Yeah So its it has K
classes Okay So now we define H theta
of X to be theta times X Now theta
is a matrix
okay its a matrix of dimensions
so this is uh a column vector right
which has
d rows and one columns this should be k
rows and d columns
is that all right so what is happening
is that
its correct no you will get a k cross
on
uh vector H Now how many parameters
Okay so too many Xs are here
Hold on
See I already told you right in the
beginning of the course I will run out
of alphabets
Okay this is my this is my model
Now what Now what do we do What do we
need
Our final classifier has to
give me a number or give me a class or
give me a label between 0 and one And
how do we represent a K class discrete
vector Do you remember the one hot
representation
Right So well have to transform this
into a one hot vector Okay So now the
the goal is
transform
a
k dimensional real vector
into one hot
into k dimensional one hot vector
So how do we do this So suppose
um
V is a vector in R K
Okay Then define a function
called soft max
on V
How do you define this So soft max
of V the J dimension of that is given by
E power
VJ divided by sigma
E power VJ or J
Okay
Now the
this is the J dimension of the soft max
Now if uh a vector z is equal to or zj
is equal to the softmax of the j
dimension
then
the vector z what is what will be the
dimensionality of vector z
k
o Yeah thats okay Yeah Uh the reason
I said O was it started from 0 to K
minus one right So this is 1 to K So
please be aware of that So why would
this be uh K dimensional Because V was
a K dimensional vector We took every
dimension of uh
uh K right every dimension of V and we
subjected this to this particular
function right So now we get a K
dimensional vector So it can be seen
that all ZJ right they are bounded
between 0 and one okay and they sum to
one
Okay
Now what should we do here
Okay let me write it maybe later
So in the context of
context of linear
models
for
kclass classification
So make your h theta of x to be equal to
Thats it
Get it Now the
the range
of h theta of x
is
You see this Come again What happened
Huh
What is a set
Huh
Oh you want to write it that way Okay
fine No problem See its a
yeah its a k dimensional one hot vector
thats what you meant once you transform
it its a k dimensional one hot vector
that okay so then what would be now the
final classifier
softmax will give you a vector that is
between 0 and one in fact to be precise
the range of hd of X is not this Its
actually yeah this
Right now how do you choose what is the
final classifier
 Thats your choice You take the max
you take the second max you take the
best of two and then whatever right
That depends upon what the final
classification is Okay Now these two
that I just talked about right This
these two have a name These are called
logistic
classifiers or regressors whatever you
want to call it
Logistic regression This is what
logistic regression is all about
Okay
Oh yeah it does matter The question is
in these two classification problem
right We have this toao
How how much does it matter It matters
a lot If you have not watched the
tutorial you have to watch the
tutorial There is something called
receiver operating characteristics or
ROC
Okay change the tow the performance of
the classifier keeps changing and you
can trade it and there are two types of
errors the false positives and false
negatives right so we have not talked I
mean Ill mention it later maybe in the
next class but I think the tutorial has
already been done if you have not looked
into it please look into it youll to
answer your precisely your question
right how much toao uh contributes to
the final classification performance by
the way Ive still not told you how to
evaluate an estimated density function
right or estimated h
we are only talking about estimating
edge how to evaluate how good or bad it
is Ive not told you about it I Ill
talk about it in the next class or maybe
the next the class next after that when
we talk of bias variance decomposition
and generalization Ill deliberately not
told you that yet well come to that in
a while now we are just building the
classifiers well see how to evaluate it
in a while it depends so please watch
the tutorial on that okay
okay so this logist logistic regression
So there is one other uh uh important
piece here right So suppose we are
solving or looking at logistic
regression right So how does erm look
like ERM with logistic regression
We have theta times to be equal to
arg
What is this This is uh
soft max
of theta times x minus y And please note that
this y has to be again a one hot vector
All of these Ys have to be one hot
vectors In the case of Kclass
classification
uh the generally the way the data comes
is that you have you have some data
which is your image or anything and the
corresponding label there are K k of
them I have to transform that or I have
to represent that as one hot otherwise
you cant solve this optimization
problem right because the dimensionality
will get mismatched Do you see what Im
saying
For instance if your data is like an
image and three classes uh disease not
diseased What can be the other class I
dont know
Yeah See did you look at the one The
third class is I dont know Which means
I as an individual may not know what the
third class is It may also mean that
the third class itself is I dont know
I dont know if you got the joke
There are too many nestings of I dont
know thats happening Anyway so you
have those three classes Youll have to
transform that into one hot
representation Otherwise this you
cant take the difference between these
two vectors right You do this Now the
question is can you differentiate this
and put to zero and get a closed form
for theta as we were getting in the
previous case
Can we
we cant So the
above optimization problem
cannot be solved analytically
Then what do we do Well have to solve
this optimization problem to get the
theta right We cannot solve it
analytically What do we do We solve it
numerically Right So
you can use any of your favorite
numerical differentiation technique
Okay
Typically it is solved using first order
gradient descent methods
Even models that are as big as GPTs
right Which are billions of parameters
are still solved using first order
gradient descent Now for all the
optimization theory that we that we talk
about and uh you know and learn right
the conjugate gradient methods and
second order methods you know why
because these models are so huge the
state of the art models are so huge that
if you have to resort to any second
order method youll have to invert that
hashian matrix if you if youre having a
70 billion parameter theta then you know
70 billion squared is the hessian and
inverting that matrix is impossible so
first order gradient gradient descent is
all we use So just for the sake of
completeness Im assuming that all of
you know what gradient descent is
right But just for the sake of
completeness I talk about gradient
descent right So lets just quickly
look at gradient descent
So suppose we have a function
L theta
which needs to be optimized
So numerically what you do is um
gradient descent
So okay before that well have to write
this um
so typically this l theta okay
uh typically right most of the cases at
least in the cases of erm right this is
our empirical risk l theta is our
empirical risk so this will be oh why
dont I just write it as uh
no rcap itself for empirical risk
is a scalar function
of parameters theta right parameters
theta which are vectors
which are in some some RP this can be
huge today this P is 70 billion 70
billion right so some vector of scalar
valued function of a vector variable So
what we want to do is we need to
optimize rcap okay uh with respect to
theta So in gradient descent
so does iteratively
as follows So start with
initialize
theta kn Okay Then you make uh till
convergence
Do the following
You have theta
t plus 1
to be theta t minus some alpha which is
a scalar times the gradient of
this particular function that we are
optimizing and this gradient is chosen
with respect to theta So please note
that if the dimensionality of the
gradient is equal is equal to that of
the variable upon which we are
optimizing
Therefore gradient of Rcap theta with
respect to theta will also be in RP
So
gradient
is also in RP
Thats it This is gradient descent Now
why should this work uh I can always
write this convex curve and you know say
that oh its the direction in which the
uh the the derivative is uh the least
and all that right but we are not
dealing with convex surfaces at all and
we are dealing it in very high
dimensions so I dont want to write this
figure this is often misleading
so if you look at some of these blogs
right you know theyll theyll write
this nice convex surface and you know
some theres a toy theres a cartoon
that is moving in the ction of all that
right so I dont want to do that at all
the correctness of okay by the way for
non convex surf surfaces you cannot
establish correctness of first order
gradient descent at all but this
particular functional form came from
Taylor series so what you actually do is
express this function as using taylor
series truncate it to first order okay
and then uh write the express the
derivative with respect to this and you
get this maybe you can do it in the
tutorial yeah So gradient descent is not
guaranteed to reach to the optimal
especially when the surfaces are
non convex
and most of the surfaces that well be
looking at are non convex surfaces right
you know for instance this right this
empirical risk that we are looking at
here with the softmax function theres
no reason why it should be convex in
theta were talking about convexity in
theta right because the optimization is
with respect to theta variable so here
is an exercise that you should do uh
write down the gradient expression for
this for a klass classification problem
with logistic regressor
Lets write down the gradient equation
Right Uh so typically the way it is
solved in computers is that uh you
hardcore the gradient expressions
for for this particular logistic model
right this gradient expression can be
hardcoded because you can compute the
gradient
But for models such as lets say neural
networks these gradients cannot be
hardcoded You need to use chain rule to
do that because neural networks are
composite functions and that has a name
thats called error back propagation
Well see that later when we come to
neural networks So its see back I mean
as I said right even GPDs are being
trained using the same gradient descent
using chain rule Thats it
In fact now you see right once the
framework is set
going from model A to model B is a
matter of writing one empirical risk
minimization equation Thats it
Whats important is setting that
framework You know what is it being
actually done when you are solving ERM
is important In fact now you can play
with things You can choose your fee
Okay you can choose your loss function
You can choose whatever model you want
So now you have the entire recipe and
framework to solve ERM with any model
gradient descent is there to optimize
and you have some model So the the uh
just skip my mind huh theres another
interesting exercise that you can solve
Suppose I change this loss function from
squared error loss to what is called as
cross entropy especially for
classification problems
What is the underlying distributional
assumption that Im making on P of Y
given X
Try to solve that
You you got the question Maybe Ill
write down that loss function right for
you So
LC this is between
H theta of X and Y loss is always
between H theta of X and Y So here Im
assuming that both H theta of X and Y
they are both bounded between 0 and 1
Thats when I can define the cross
entropy right Ill define it as
see as they say no
laziness only will double triple your
efforts I could have written that
again I wanted not avoid writing that
but ended up doing more effort So this
is equal to um suppose we are looking at
uh lets say that this is k classes
right in that case this is over k we
have h theta of x log of
uh yk its a negative here this is the
cross entropy loss
this is you have to take the k dimension
of this take the k dimension of h state
of x k dimension of y and you compute
this and sum it over all possible K
dimensions This is actually the cross
entropy This is the definition We have
seen the definition of cross entropy of
discrete distribution So thats exactly
what it is You know that this is KL
divergence plus the entropy
Cross entropy is nothing but KL
divergence plus entropy right Because
cross entropy minus entropy was what KL
divergence is So K divergence plus
this Were looking at two discrete
random variables here yk and h theta of
x And we looking at the k divergence
between those two Thats it
Now the question for you is suppose we
do this what is the form of P of Y given
X that we are choosing okay that will
lead the
the ML or maximum likelihood estimation
to be having this particular form
just work it out its a nice exercise to
do now you can use this as your loss
function okay and solve uh for ERM
using the gradient descent now You pick
a loss function pick a form for your h
theta of X right And use gradient
descent to build your model Thats it
Okay Yeah
 Yeah
 H for Yeah So you only have one of them
that will survive
 Uh you want to do it the other way
around Yeah So yeah I think theres a
point what he said is its better to
put yk here and h theta of x here
because
if uh I mean typically yk will be
between I mean itll always be one 0 and
one so log 0 is undefined so you take yk
outside and put hk inside thats okay
yeah
okay so now I think let let me just
summarize now we have the entire recipe
now so given on a problem
you have to choose what h function the
form for the h function you want right
choose a loss function and use gradient
descent to
solve the erm optimization problem you
get a model thats it this is from the
erm perspective so if you want to look
into in fact doesnt matter its just a
formulation so you formulate it as uh a
maximum likelihood estimation or kale
minimization problem or you formulate it
as RM So there is another interesting
question that we should ask What is the
equivalent of map estimate in ERM
Its called regularized ERM Well see
that in the next class So if you add
something called regularization to your
ERM it is equivalent to the ML estimate
with a basian prior which is the map
estimate So regularized ERM is exactly
equivalent to map estimate is what we
will see
Okay So yeah So we will uh well end
todays class here and in next class I
will uh look at uh the generalization
aspects of it I look at the bias
variance decomposition and evaluating
models and then we look at
regularization Thank you
