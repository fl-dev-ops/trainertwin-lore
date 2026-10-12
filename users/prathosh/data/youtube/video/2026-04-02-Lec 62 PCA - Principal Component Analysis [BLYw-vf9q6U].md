---
id: BLYw-vf9q6U
title: Lec 62 PCA - Principal Component Analysis
url: https://www.youtube.com/watch?v=BLYw-vf9q6U
date: '2026-04-02'
duration: 45:41
model: youtube-captions (en-orig)
transcript: true
---

## Transcript

Welcome all
So the first example is the class of
algorithms where
estimating or I Ill call that as
implicit
latent variable models
And by the way this nomenclature is not
standard You know you cannot find this
in any textbook This Im just making
Im just giving a giving a name here
So here what we have is that um
PX
is estimated
by our an implicit
latent variable model
So let us take a
a few examples on this You know the
first example is
is where
I use
a linear model
And Im reiterating please note that
any everything that we do
in a in a in a non probabilistic ERM way
also has a
exact correlate in the probabilistic
space So Ill keep switching between
these two So far what we saw in
K means and GMM are the probabilistic
ways of looking at it Now we will look
at the ERM way of doing it So linear
model on data So what do you mean by
linear model on data Lets say that X
is in RD
And we have the data set that contains
uh N data points
Now another thing to recall here is
which I had mentioned in the previous
class as well is that
one other advantage of getting these
representations okay is compression
I told you that typically the
dimensionality of this latent variable Z
is much less than the dimensionality of
the data variable okay
In clustering itself we saw Clustering
is also a one sort of discrete
representation where suppose you have
thousands of dimensions of data you
compress it into a 10 dimensional space
discrete space if youre doing a 10 way
clustering okay Now compress Why is
compression important This is again
takes back to the information
theoretical space that
See we dont have an understanding on
why these
todays models have actually become
intelligent
All we are doing is ERM okay on these
transformer kind of models in an
unsupervised way We will Ill show you
how it is done in an unsupervised way
Now why is why are they you know
becoming intelligent is because this
compression that is happening So
according to one theory
compression gives you intelligence So
you know if you Why is that
Cuz the data I mean if you want to
compress reduce the information
uh
and take the information from a very
high dimensional space and put it into a
very low dimensional space
uh
the best way to do it is by
understanding the underlying semantics
If you do not understand the underlying
semantics then you can you cannot
compress Let me give you an example
Lets say that I give you a picture of
uh human faces multiple pictures of
human face faces and I will ask you to
represent this using
10 numbers
Okay How would you do this
The first thing is you will you will
identify that all human faces have a
symmetry
That you know there are two eyes
theres theres a nose and theres a
theres a mouth and all that okay And
perhaps you will see that you will store
all this information in four bits That
the same there is symmetry there is
nose there is eye and all that And
then maybe
store coordinates of where these
where the eye is and all that So you
know there will be loss of information
of course because you are only given 10
dimensions but
the best way to compress is to
understand what the underlying semantics
is Does it make sense Because
everything else is No everything else
is useless information
You know okay there are
so many skin pixels Okay what do you
do with it Fine I mean you can just
get the skin color and then maybe paint
it
So compression
means semantics
So unless you understand the underlying
semantics well you cannot compress
Now what is happening is you might to
in todays AI or all these models
whats happening is
the entire the entirety of
the human knowledge that is stored in
internet as text image and all that is
now being compressed into
5 billion parameters
Right If that were to happen
the only way to do that is to get the
underlying semantics
Okay Thats why that thats the power
of unsupervised learning or learning
representations because youre
compressing that way okay So now we
will look at a a small I mean a very
naive way to compress the data which is
a linear way of compressing data We
will assume that there exists a a Z
uh that is in K dimensional space
Typically K is much less than D
You want to compress the data okay
Now we will define some V to be equal
to
a a matrix
W
uh times X
Where W is a
K cross D matrix This is a K cross D
matrix
And this is
a D cross one
vector
Actually let let let me just change the
notation a little so that were
consistent Uh
Yeah Z can still be in uh
Hold on
So Z can still be in RK So what we
need is we want the Z to be equal to
Dont copy it yet huh Let me just see
this notationally consistently So we
want a linear projection space W such
that when you project your data onto
that space you get a K dimensional
compression
That makes sense right So the goal
objective here is to learn a linear
projection W
such that
the data gets compressed from dimension
D to dimension K
Does it make sense So this is again
learning an implicit latent variable
model In fact this is this you can you
can see this as an explicit latent
variable model as well via a linear
projection
You take X
project that onto some space defined by
W You all know that uh multiplying a
vector with a matrix is equivalent to
projecting it onto a space spanned by
the
the columns of this this matrix right
So thats why this is a linear
projection that we are doing So the
quest the goal the question that we are
asking is we take a data point project
it onto a space given specified by a
matrix and after projection we want
the data to be compressed into a a
smaller space is the idea
And we use Z as our representations
Make sense right So now the question
is how do we get this W Well have to
What is the best way to get W is the
question Okay
Now question
Obtain W
by solving This is not a question How
to obtain W is a question
Such that some
criteria has to be optimized correct
Now if we were to do this in the
probabilistic space we would say that
oh theres a distribution on this and
we would want to minimize the
divergence So since we are operating
in the
non probabilistic realm so how do we
say that We will define a
a loss function okay So such that a
loss function is optimized
Okay So we can define a particular
loss function which is
defined
uh the loss function as
So what can be a good loss function
There can be multiple ways to do this
One way to do it is
that
the variance of the projected data
has to be minimized So I want to
project in such a way
that
once I project
the spread of the projected data has to
be as small as possible Why is this a
good objective function
Think about it We are trying to
compress the information
When we are trying to compress the
information in smaller number of bits
okay Once you project the data the
data has to be has to have as less
variance as possible in the projected
space because thats thatll give us the
maximum compression
Isnt it Spread out the variance of the
projected data can be looked into as how
much
I should not be using the word
divergence and how much spread that
particular data has okay In the
projected space because we are seeking
compression well have to
One good objective would be to
let the algorithm decide what sort of
projection would give me
the least variance in the projected
space
Okay I define the loss function as that
of minimizing
the projected
variance
Which is
So ZI is our projected data If ZI is
the data point
uh
We have N data points right So this
is the
mean of
all the data points I mean Im just
writing the empirical estimate of the uh
variance
Uh well have to take a square of this
right
Square this
and add them over all data points
Divide by N So this is our
L loss function
And this
depends on W right
Cuz Z depends on W In fact it depends
on uh
W and also
Okay what was our notation It was L
theta is it
L of theta or L subscript theta
The parameters we were Are we right Were
we writing our parameters as subscripts
or the arguments Arguments
L of theta right Okay well write it
as L of W comma X X is data and W is
your parameter So this is the loss
function So what do we need We want
our W star
such that this is minimized
I dont know the constraints because you
can put ZI to all zeros
Well get there

 Okay So what does this come out to be
Lets write down this loss now
as

 I beg your pardon I think I made a
mistake in formulating
Uh
It should be
I mean see mathematically it does not
matter but interpretation is what I
changed okay It should not be
minimizing the projected variance
Its minimizing the
the negative of the projected variance
or maximizing the projected variance
I think thats where I made a mistake
Let me just uh
rewrite it
I can write it as negative of this but
yeah
Now well have to change the
interpretation right So I think I
made a mistake Can Can somebody point
the mistake
Like
uh we want to make we want to find those
directions in which the data has the
maximum spread so that
like it is the most important
representation Huh See what I Okay
What did I say What was my
interpretation I said the variance has
to be minimized Its not
You want to You want to say something
Yeah See the thing is please you
should note that Z by construction we
are saying that it has to have lesser
dimensions as data
The question that you should be asking
is how should I choose my projection in
such a way that the directions that I
choose or the projections that I choose
will preserve the variance of the data
to the maximum possible extent now
because I dont want to lose the
information
See Ill tell you I Ill
Ill tell you why I made this mistake
huh
There is another equivalent
interpretation of this
Okay which Ill tell you at the end of
the this particular discussion I think
you know I just mixed up both of them
but did you get the idea The idea is
once you project onto a subspace
and trying to compress it within with
using lesser number of dimensions
youll have to project it in such a way
that
the the variance of the projected data
is maximized because you want to
preserve whatever spread that was there
in the initial data on the projected
space as well
not withstanding the fact that the
dimensionality of the projected space is
much less than that of data
Right So just hold on Well do the
math and well see what the solution is
going to be and then Ill tell you an
equivalent minimization formulation of
this okay Where the interpretation
sort of changes You know thats where
I
uh
made that mistake Is this Is it clear
No What is not clear So if for
example the example that you gave of
faces if Im projecting it down to
lets say 10 numbers and one of them is
whether the face is of a female or a
male Mhm So I cant have variance
there It should be a deterministic
uh answer that this face is male and
this face is female So
that is equivalent to reducing the
variance No not necessarily Lets
say if you look if you think think of
it from the uh continuous variable
perspective thats easier to interpret
that way
So lets take a continuous variable
So lets say that that you are
measuring uh the the width of uh the eye
in the actual face and and you have 100
pixels to do that Now all those 100
pixels are now compressed into lets say
four numbers
Mhm
Now those four numbers have to be in
such a way that the
spread of information that was there for
all the uh eyes in the original data set
has to be preserved here
Otherwise itll be information loss
That statement did not make sense to me
Why is that
I mean can you take a different example
than widths because widths also is a
spread So are you No width is a
number Im saying lets say that
theres a scalar
Okay the information about the width is
compressed or rather embedded in five
dimensions in the original space lets
say or 10 dimensions in the original
space lets say There are They are 10
pixels
Now you want to compress all of that
into lets say two pixels
Now all the information that was there
regarding these
uh the width which is the the parameter
that is being measured in the original
data space has to get reflected in your
projected space as well
How is that possible if you do not
maintain the same variance that was
there in the original data space
compared I mean corresponding to this
particular feature in the projected
space as well
What happens otherwise is all the Okay
lets say that there is
the the variance is minimized for that
particular feature or rather you seek a
a particular
projection such that the variance is
minimized What will happen is it will
create a degenerative case where it will
nullify different widths of all human
eyes and put it into a one data point
and say that there is an eye We dont
want that to happen
So we want the measurement that we have
made See actually here is the point
The point is whatever is redundant has
to be taken off
Whatever is informative has to be
maximized Thats it
Right So how do you quantify the
informativeness is through the variance
of the projected data Thats the idea
Is it okay now Okay So now lets look
at this How do you solve this problem
Is this is equal to uh
See I keep telling this jokingly to my
students always
that
as engineers you you solve a problem
empirically first and retrofit the math

 So
thats thats how most papers are
written by the way
See when you write a paper you first
say that oh this is the problem that we
had and here is a theorem and heres a
lemma This is what we solved and then
we talk of experiments
But research happens exactly the
opposite way So you try 10 different
things something works So you get You
get an empirical result
Okay
My you know kind of
One of my favorite statements that I
keep telling my students is that if
there is something that is working
empirically then there should always be
a math that explains it
Right So thats how it is Its a no
Sometimes what happens is you start by
hypothesizing something and write an
equation and then see if it works but
often times it does not happen that way
It happens the other way around where
you try some hunch
using some intuitive method It works
and then back with the math because
there should always And while you are
doing that exercise while while you are
trying to explain your method using
mathematics
because of the power of the math youll
also get a lot of corollaries and you
know other generalization capabilities
once you make it formalized
But most times you start with an
empirical experimentation At least
thats what my experience has been
Okay so we will write the math now
This is
uh n and you have w x i squared
So let
some uh
x bar x cap is
1 by n
Is there a mistake
Oh the summation should be
outside Correct
Oh where is the eraser

 Yeah
Call this as x cap so then
and let uh
sigma be this term
Since some notations if I do this
then uh
this thing would be
Please verify this This is a simple
algebra right Ive vectorized the
notations If you uh
This is x cap yeah
If you define the uh sigma matrix to be
a Okay this is also sigma this is also
sigma Its confusing Lets do this and
call this sigma cap
to represent the matrix This is the
outer product of these two vectors
right x minus x cap is a vector
You take the outer product of it Uh
call that the This is the variance or
covariance matrix Right So the
objective function now can be written as
w transpose sigma cap w
Okay what do we want now We want this
to be maximized So we want to seek a w
star
that would maximize
w transpose sigma cap w
This is a scalar right Sigma cap is a
matrix w transpose sigma cap w is the
quadratic form which is a scalar
So the objective function still is a
scalar that we have And this this
optimization is with respect to w
Now to your question right If you
solve this optimization problem
uh
what w it can choose
If If No it can Youre solving a
maximization problem It can choose w to
be having all the
elements of w to be having very high
value and and solve this
So now youll have to constrain this
So how do you constrain this We are
interested in the direction w not in
the
particular magnitude of the that w How
do we do that Normalize w So how do
you normalize w
Add a constraint that
this w vector that we are looking at
okay
has to have unit norm
Okay
Now you know the story right So how
do we solve this w star
uh
write down the Lagrangian
The Lagrangian is w transpose
times plus
Take the derivative of this and put to
zero what will happen
So w star will be
Do you know the solution to this
optimization problem
This problem has a name Do you know
this
No no At this algorithm has a name
Thats PCA but you know this problem
is called Rayleigh quotient by the way
So what is the solution for this
w star will be the
eigenvector of
sigma cap corresponding to
to the
largest eigenvalue
And this is your linear algebra 101
right I think you should have solved
this problem in your linear algebra So
this the solution for this Rayleigh
quotient is yeah
Uh
Whats the Whats the question
Correct so
You You mean here youre saying
So z i is a vector here Is it Okay
let me see what this is
This is a k dimensional vector
Yeah so what we missed is this
norm squared
Yeah thanks for that
Yeah makes sense Okay So now this w
star will be the eigenvector
of sigma squared sigma sigma cap
corresponding to the highest eigenvalue
Okay No
Question Okay
Now this w
is called the principal component
So whats the dimension of w that we
looked at now
Its a k cross d matrix right So now
it it has to have d vectors
No it has to have k number of vectors
okay And all of these are
eigenvectors of the sigma
cap matrix corresponding to
the highest eigenvalues that are in
order
Okay So ws are called Let me just
write that down
w
which is a k cross d matrix
will contain
the eigenvectors
of
the covariance matrix
rank ordered
in accordance with their eigenvalues
See yeah
See you can make the k to be one and
then the entire math goes through and
that will be the eigenvalue
corresponding to the eigenvector
corresponding highest eigenvalues If
there are two of them
then it will be the second eigenvalue
vector and so on
See you can still write w to be a
matrix So what would this w the
solution for this uh
the Rayleigh quotient problem would be a
matrix w such that its columns are
eigenvectors yeah First k
eigenvectors Thats it Yeah
Uh No actually right You can uh uh
take sigma matrix which is the
covariance matrix is always
positive semi definite right Positive
positive semi definite
So it is guaranteed to have d
eigenvalues always So you can actually
take d uh eigenvectors
and get another space
which does not
have any compression It does not give
you any compression But if you take the
first k eigenvectors and project your
data onto the space spanned by the first
k eigenvectors then you will have a
representation that would have dimension
that is less than the
data dimensions
Okay
Now how do you choose Okay by the way
as some of you all all already pointed
out this technique is called the
principal component analysis
PCA
What is the hyperparameter here
k How many number of eigenvectors do
you want to take You know what is the
dimension of What is the compression
dimension that you that you would want
to look at
In fact
depending upon how much of the variance
of the data that you want to preserve
putting threshold on that you can
decide how how much k do you want
Do you see why
Suppose you want 90 percent of the variance to
be preserved then you can find out you
know how much of the how many
eigenvectors that you would want to take
to preserve 90 percent of variance and so on
If you take all eigen vectors then you
would
lose nothing If you choose first K
eigen vectors out of D eigen vectors
then you would be losing some of the
variances
Okay And these individual eigen vectors
are also called principal components
In the indices okay
The latest version has a spell check as
well Okay
Okay this is PCA Okay now Ill give
you an alternate
interpretation of this formulation of
this that we which you should do as a
homework
Which is
you should show that you will get the
exact same formulation
if you cast the problem as
that of finding a linear projection
of data such that
the error
between
the actual data and the projected data
is minimized
So W times X will give you the projected
data XI is your actual data
So its XI minus W times X take the norm
of that square of norm of that sum it
over all data points and minimize Find
a W that would minimize that
Itll get you to the exact same
solution Can you see why Because the
algebra works out yeah
It does not So you have to make your W
to be uh the to be having the complete
dimensions
Right And then you only take choose K
of them Yeah K vectors of Thats it
You should show the equivalence between
these two formulations right
Maximizing the projected variance
or minimizing the
projected error Thats why I made the
mistake right So when I talk talk of
variance I said its minimizing Its
maximizing the projected variance or
minimizing the
projected error
Okay
Yeah this is about PCA And as you see
PCA Why why is PCA used
To reduce the dimensionality of data
Suppose you are given a
uh an image data set that has 10000
pixels Suppose you want to represent
that using only five or 10 dimensions
The the first go to algorithm is to do a
PCA
on your data and choose your K and
represent that as vectors and then move
on
Okay
Okay this is about PCA So now PCA is
limited
by the fact that we are seeking a linear
projection Question
Yeah
Correct So thats a good question
right The question is if you make it
to be a full rank matrix then wouldnt
W be identity
So how do you uh
How do you avoid that You make it rank
deficient
Make it rank deficient but adjust the
dimensions thats it
Okay so then it wont be identity It
cant be identity that way
Okay this is about uh PCA So now
lets As I said PCA is limited by the
fact that you are only looking at linear
projections And why should you look at
linear projections
The
the advantage of PCA is that you dont
have to solve any optimization algorithm
explicitly I mean you do have to but
you only have to solve an eigen eigen
value decom eigen vectors
uh problem right Which is we have
standard methods to that the power
method etc For large matrices it can
scale up Thats the only advantage But
the limitation is that you are seeking a
linear projection of data Now why
should you only seek linear projection
of data right So how do you extend
this idea to non linear projections
So how do we do this
To do that what we do is that we
define Z to be here
uh an MLP
over X
Its not a linear projection anymore It
It need not be MLP as well It can be
generally a neural network
Deep neural network over Z
Okay
Now what is the task Well have to get
Well have to formulate an optimization
problem over here right What is the
optimization problem here
Remember that our entire goal is to
estimate the marginal distribution
Because the moment you put semantics on
top of it that will become useless So
well have to ensure that the marginal
dis Okay talking of marginal
distribution do you see why PCA
estimates marginal distribution
Cuz the objective is set in such a way
that the error between the the data
points in a statistical sense and the
projected data is minimized
Okay which is it is trying to
reconstruct the data back
using the representations of Z which is
equivalent to estimating the marginal
distribution
Okay so now what should be the
objective here
Given that we want to
estimate the marginal distribution
Now recall that uh this representation
now can be seen as P theta of
Z given X right
Suppose you have a neural network okay
that is taking X as an input and giving
you Z can be seen as something that is
estimating the marginal of Z given X
If you want to estimate the
uh sorry the conditional of Z given X
So if you want to estimate the marginal
PX from here how do you do this
So we know the math How do we do this
Yeah we can use the base rule and
to estimate the marginal of this So
what is P theta of X equal to in this
case
Summation over
This is uh
uh
over Z Let me write down this joint
 distribution now So dont
This is equal to Hold on Let me just
Lets do that
So now this is equal to
P theta of X and Z
Yeah
This is what it is right So we need
to take a summation of this
This is all right
Okay Now how do we implement this in
practice is the question The way to do
it is
implementing
above marginalization
These two
Lets say that you start with X and you
have a neural network
It will give you Z So this is one
neural network Lets call this
uh
E phi of X
Okay
Now to marginalize what you do is you
take the Z okay and pass it through
another neural network D theta
of Z
You get back another random variable X
cap
Okay now ensure that this random
variable distribution of this random
variable lets call that as
P theta of X cap
matches with that of PX
You can look at this entire thing as a
composite compositional function where
you start from X and then go to a latent
space Z And from that latent space you
have another neural network So what is
this actually So X cap now is equal to
First start with X
Theres one function E phi
And upon this function there is another
function D theta
That will give this random variable X
cap
Now make sure that this
X cap this distribution of this X cap
is now matching that with the
distribution of X
If it does that then the Z can be seen
as a good representation of X Why is
that
You are able to recover the marginal
distribution of X from the
conditional P theta of Z given X
Okay Now how do you ensure that you
know how do we
match these distributions P theta of X
cap and PX
By again impose a distribution take a
KL divergence and minimize If we
assume it to be lets say a Gaussian
distribution P theta of X and take the
KL divergence then you will end up
getting a loss function
And what would that loss function be
So whenever we are talking about
Gaussian distribution and KL divergence
between those two the corresponding
loss function would look like
This will be a function of theta and
phi
1 through N we have XI minus
XI cap
whole square right This is
the loss function that you optimize it
over
and this x i cap is now
a function of theta and fee
Therefore optimizing this would give you
an x i cap that would minimize
that would
try to match the distribution of p theta
of x
Do you know what is this called
This is called an auto encoder
No d theta is the decoder
This is the decoder
This is the encoder
This entire architecture is called an
auto encoder
Okay so typically what is done is you
have a neural network
And the encoder
which is e fee
will have this sort of an architecture
in the sense that you start from
dimensions d and you come to dimension k
and we know that dimension k is always
less because by construction and from
there
you go back to
the dimension of
x
This is the encoding This is the
decoding part
So what do you do this what do you do
with this post training You train it so
this is auto encoders are always trained
in an unsupervised way
Why Because we are not using labels
anyway When this is standard back
propagation we just train both of them
using standard back propagation Now
once you train it what do you do with
it Is the question
With all
like with all unsupervised methods once
you train this take the data pass it
through the trained encoder get the
corresponding zs for every data point
and that becomes the feature or the
representation
for the data set Instead of using x use
z
Makes sense And these are called
embeddings z is called embedding So
this
these e fee and d d theta
can be CNNs
They can be LSTMs
They can be transformers
Now if you take a transformer and do
this
so these are the bird kind of embeddings
that we look at encoder decoder models
These are called the encoder decoder
models where
encoder is a transformer decoder is a
transformer and the task that you are
trying to solve is the reconstruction
Theres one twist to the tail here in
the modern day training
its not the data reconstruction that is
solved Okay what is done is you take
the data point and perturb it with some
noise
and then try to reconstruct the data
back
Okay so now why is perturbation
helpful in learning better represent It
is shown that if you perturb the input
data points before auto encoding they
will lead to better representations Now
why is that the case
Intuitively
you know if if the decoder is or rather
encoder is trying to the the idea here
is that the encoder will learn
representations by ignoring the noise
and only if the encoder does it that way
then the decoder would be able to
reconstruct data back
So this is called denoising auto
encoder
Whatever I just wrote where you take
data point perturb it with some noise
and then do it is called denoising auto
encoder and thats the workhorse of
todays
unsupervised learning LLMs
We will look into this in more detail in
the next class where I will talk about
something called something called noise
contrastive estimation or NCE which is
an alternative estimation method to the
maximum likelihood estimation
And this which is denoising auto encoder
is a special case of NCE Ill show that
its a special case of NCE and the
current day LLM training
okay is done by
two its done in two ways You know one
is that you take a sequence randomly
mask some of the tokens in that sequence
and ask your decoder to
complete it Okay which is very similar
to
the denoising auto encoder The other
way to do it is take a sequence I mean
actually this is also a special form of
whatever I said Take a sequence mask
the last token and ask your decoder to
predict the last token
You can look into that also as masked
auto encoding but the mask is always
applied at the last token Thats it
Right Ill show that in fact
the entire LLM space right now
is trained using this way
Where you have a reconstruction task
that is there and you just train it for
predicting the next word So this is
called unsupervised pre training
Theres a theres a name for it cuz
theres no label that is being used
here You do what is called as
unsupervised pre training and you do it
on the entirety of the data that is
available on internet
And it takes you a good 6 to 8 months on
hundreds and thousands of GPUs to do
this
But what is happening is back
propagation
on transformers with that scale with
noise contrastive estimation So next
class we will look at noise contrastive
estimation as a way of estimating the
underlying distributions and Ill give
you a few examples for NCE
okay using the the mask prediction and
then we will go to another class of
methods which is another special case of
NCE which are called self supervised
learning techniques
such as examples such as SimCLR and so
on
And then we will move on to some
introduction to generative models So
far in the course
none of our formulations can sample from
the distribution
Right If we incorporate the sampling
also in this that becomes a generative
model Well see a few examples of that
and then well conclude the course
there Okay thank you
