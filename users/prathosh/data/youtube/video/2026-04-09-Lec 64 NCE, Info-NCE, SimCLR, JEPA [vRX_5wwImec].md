---
id: vRX_5wwImec
title: Lec 64 NCE, Info-NCE, SimCLR, JEPA
url: https://www.youtube.com/watch?v=vRX_5wwImec
date: '2026-04-09'
duration: 35:36
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Lec 64 NCE, Info-NCE, SimCLR, JEPA

## Transcript

speaker_1: Welcome to this lecture Now the final
NC estimator consider
an estimator
J theta as follows
J of theta is
the expectation
of log
h theta of x where this expectation is
with respect to px
plus u times the expectation of
log of
1 minus h of y See this y and x are dummy
variables right As long as we are
sampling from the right distribution
its okay
Now this is the NC estimator
The NC estimator is this that we find
out the difference between
the expectations of these two terms
where rather the sum of these two
expectations where the first expectation
is that of log of h theta of x and the
expectation is with respect to px the
second expectation is with respect to
log of 1 minus h of i where the
expectation is with respect to pn what
is h theta here
h theta is whatever we saw in the
previous case So h theta is that neural
network which is trying to solve the
binary classification problem between px
and pn
Okay its that network Now the theorem
says uh
as follows I Ill just state the
theorem without proof Take this proof
as a as an exercise I Ill give you the
sketch of proof You do it Okay The
theorem is as follows So this j theta n
attains
a maximum
at
See Okay So let me just define that
as well once just before we write the
theorem
just to make it self sustained where
where h theta
What we what did we define h theta to be
here
H theta is 1 by this thing right and f
theta of u is this right So the same
definition that we have uh where h theta
is given by 1 by 1 plus new times e power minus
f theta of u
and f theta of u was the difference
between
log of P theta of U minus log of
PN of U Correct This was the
definition
So the theorem says that J theta and C
attains a maximum at
those thetas
for that theta for which
if theta of u is equal to log px
minus log bn
This is the result or we well call this
as ft of x
Right So what we are saying is that
this objective function
would be maximized only if this f theta
becomes equal to log of px minus this
thing So which means that if this only
if this p theta of u which is the
implicit density estimate that this h
theta is is doing
is equal to px of x
This objective function does not attain
maxima
or in other words this objective
function will attain maxima only if p
theta of u here will be equal to px
So we are done right So what we are
saying is that you can solve this binary
classification problem in the best
possible way only if the implicit
density estimate that your neural
network H theta is imposing
is equal to that of the data density
Now how do you prove this Ill just
tell you how to prove this See this j
theta is an expectation with respect to
px and pn isnt it Okay Now this h
theta has dependence on p theta of u
Write down these expect expand these
expectations and you will have p theta
there You have to differentiate this
entire expectation with respect to p
theta because we are seeking
what theta would maximize this with
respect to p theta And you see what
optimal what is the optimal value of p
theta that would maximize this j theta
You have to differentiate this entire
thing with respect to p theta And what
will be seen is that
P theta that would which would maximize
this is when P theta is equal to PX
thats the result that will come out
Okay So this is noise contrastive
estimation All it is saying is that
given data construct another noise
distribution and trying a binary
classifier that would classify between
the points of data and points of the uh
noise Okay If you have done this
correctly then the underlying neural
network would have estimated the density
from which data is coming exactly is
what it is saying So now what do we do
with this neural network is the question
that Ill answer in a while This is
still not sampling but this neural
network can be now used as an embedding
extractor
The intermediate layers representations
of these neural network This neural
network that we have trained for
classification now can be used to
extract embeddings for data which can be
then used for downstream tasks
Do you see whats happening here
Okay So this is NC Uh so NC is not
something that is u uh that is used as
it is in practice today
uh uh an improvised version of NC which
is called infencce is what is used
Well talk about infenc in a while but
is this idea clear Ill just stop here
for a while and take questions if there
are any So the moral of the story is as
follows Right So now and by the way
did you notice that nowhere in the
entire construction that the
normalization constant Z appeared
Right Because there is log of P theta
and log of PN of U Right the the Z
which is the normalization constant gets
canceled away So you can use this with
EBMS as well
Okay in fact the original paper that
proposed this idea is titled this noise
contrastive estimation of unnormalized
statistical models
NC for unnormalized statistical models
So why is it called unnormalized
statistical models is because they say
that we know we are modeling P theta
dash without the normalization constant
You can completely ignore the
normalization constant in this
particular uh treatment of density
estimation but you cant do that in the
ML estimation
By the way all the techniques that are
based on this very idea of NCE are
referred to as selfsupervised learning
I mean nomature right If you want it
So its a subcategory of unsupervised
learning Its called self supervised
learning because the supervision is now
is being created right during learning
in in in I dont know yeah so it is
supervised by the self itself because
there is un how can you define the noise
the definition of noise comes from what
is data so thats self s supervision so
you are you are solving a supervised
learning problem but the supervision is
not through uh some external agency but
it is self generated maybe thats why
the name self supervised learning all
the techniques that work on noise
contrastive estimation they are called
self s supervised learning techniques
okay
right
now as I said uh NC is not uh used as it
is in in in in uh in todays uh
practical world what is used is uh its
cousin by name info NCE
Where the idea is simply
that extend
problem of NCE
to a
multiclass classification problem
Now in NCE we solved a binary
classification problem right where
uh there is data there is noise try to
classify between them info you solve it
in uh in the multiclass classification
sense so what do we what do we do that
what is the idea behind info is as
follows suppose
x i is a data point
Define
x i plus and x i minus
as
positive and negative counterparts
Now if you are given a data point X I
you define two data two other data
points okay X I plus and X I minus where
X I plus
is called the positive counterpart and X
I minus is a negative counterpart What
is it X I minus is the samples of noise
that we are talking about Okay And X I
plus is another data point from the
exact same distribution So we had D and
Dash right Thats exactly what they
are saying as XI and XI plus Okay Now
then define a loss which is L
info NC
as
the categorical cross entropy Its not
the binary cross entropy anymore The
categorical cross entropy of log
e power
so g theta of
x i plus
divided by
e power
okay I can just say it this
uh okay hold on
equal to 1 to k plus e power just wanted
to write both of them within one sum
cant be done e power g theta of x i plus
See what is this is the usual softmax
that we are looking at Uh this is the
estimating the probability of
x i plus being the positive sample given
a sample and everything else being
negative So this is a kclass
classification problem The
classification is between
XI being the uh the positive counterpart
and everything taken to be as the
out of class samples See what does a K
classification uh task do right So one
of the K will be uh the actual class and
rest of rest of them are not the actual
classes Here the actual class is taken
to be as X plus okay and everything else
is taken to be as the negative class In
fact uh in uh in the way we have defined
it right uh there are k number of
negative samples here you see
for a given data point there are k
number of negative samples which are not
coming from that particular class and
one of them is the positive class
you see this okay and this is the usual
softmax where g theta
is typically a neural network right it
can be a deep neural network so whats
happening here is that you take a neural
network
give X as an input and there is G theta
and you get this
G theta of X can also call this as some
Z which is the representation okay and
then you have a softmax on top of top of
it
now what are the labels for is
for a given point x plus is taken to be
as the correct label right and multiple
x minuses are taken to be as the wrong
labels
is this all right
now how do you train this neural network
you train this neural network using this
L l inf loss okay and post training you
can use the output of this neural
network as the embedding
that you can use for downstream tasks
Now what is happening here You if you
look at it
uh we are trying to
ensure that the uh the alignment between
Xi and its positive counterparts is
maximized
and the misalignment between Xi and its
negative counterparts is being
minimized Thats exactly what is done
in a softmax or a K class classification
problem isnt it Youre trying to
learn representation Z in such a way
that given a point it aligns with its
positive counterpart and it does not
align with its negative counterpart
Thats it Ill take questions in a
while Okay So this is in NCE extended
to Kclass classification problems
because there we were trying to separate
between
the the data point and one negative
sample Here we are saying data point
its positive and n negative sample k
negative sample So this is a K class
classification problem that is being
solved Okay And these methods okay
there are multiple methods that uh build
on top of this idea So one is what is
called as SIM CLR Okay This was done
for the uh the image uh uh
representation learning This was um a
simple method for contrastive learning
of image representation Thats what it
stands for SIM CLR Okay And these
things are also called contrastive
learning methodologies
because they stem from NC right no noise
contrast estimation and what Simr showed
and this is a paper co authored by
Hinton what this paper showed was
if you do this learning no uh NC
on imageet data set this is completely
unsupervised right we dont need any
labels whatsoever here then use this
representations and then try another
classifier for the imagenet
classification task So imaginet was the
standard challenge uh that was there in
that time right where there are
thousands of categories 1 million
categories its a 1 million class
classification problem with a uh uh 1k
right or one millions of examples and
the number of classes was thousand it
was shown that the number of labels that
you need to achieve the best accuracy
for that task it is reduced by 90 percent if
you use Z
instead of X
So what is the procedure Given a task
you learn the representations using NCE
or info NCE and then use 10 percent of that
data Use Z as your representation and
use 10 percent of the label data to train a
classifier post hawk Thats a
downstream task If you do that the
accuracy that you would have gotten by
using 100 percent of data can be achieved by
using 10 percent of label data If you do this
learning as I said in todays uh LLM
training okay the first of level of
training that happens is via these kinds
of techniques
This is called unsupervised pre training
or self supervised pre training where
you train uh to learn the
representations without labels and then
you can do a
uh supervised fine tuning SFT it is
referred to as so there is unsupervised
pre training and then supervised
finetuning
So you do supervised finetuning
by using these kinds of representations
In fact you can you can use the exact
same network to do a supervised training
as well once you have trained it in an
unsupervised way The only question that
remains right now is how do we get these
negative samples
You see this So given some data set
how do we define these positive samples
and negative samples is the question
that we that remains yet different
methods do it in different ways So Ill
just state a couple of ways to do it
Before that if there are any questions
on the the philosophy or methodology of
contrastive estimation ask me Yeah
 Are they kind of analogous to that skip
algorithm with negative
 Uh I mean Ive not talked about skip
gram but but since youre asking yeah it
its analogous Yes Yeah You had a
question Yeah
 What exact My question was that what
exactly are the positive We will show
that See in the definition of
contrastive estimation PN is any
distribution that is not PX Right Now
uh in the in the proof that I skipped
So what can be shown is the more the
overlap between PX and PN the difficult
is the convergence of that estimator to
the true distribution
Right So now there is a whole area of
work around contrastive estimation where
people have asked this question of what
samples makes good negative samples
This is called hard negative mining
This is called the problem of negative
mining So how do you mine the negative
samples because the harder the negative
uh samples are the better the learning
is But if there is completely
non overlap in terms of supports you
know for instance suppose you are
looking at images learn representations
of images you just take uh uh images of
gajian noise gian noise as your negative
samples the learn representations will
not be good at all because the
classification is easier that way right
so you have to carefully mine the
negative sample so people have tried a
lot of methods to mine the negative
samples in in in careful ways and a lot
of them are empirical so Ill just state
a few ways to do that right But yeah
but the idea is that you should get your
negative samples correctly
 Correct Negative samples here Here are
the noise Yeah In the comparing with
the NC Yes
Okay Yeah So we will look at how to
look at negative samples and positive
samples So example of uh this thing in
SimCLR is as follows So X is taken as
an image
advantage of taking it as
 yeah the uh advantage of taking it as a
multiclass the question is what is the
what is the need to move from NC to info
NCE what can be shown is uh the uh the
estimator right has a better bound is
what can be shown so intuitively here is
what is happening right so you are
getting negative samples for free
why dont you use it uh for better
convergence because you You can generate
as many negative samples as you want
right So theres no reason why you
should only have one negative sample for
per example You can generate as many
negative samples as possible So use
that is the idea Okay Now uh yeah So
if XN is an image X plus is taken to be
as the
augmented versions of X
So which can be a rotation
of
decoloring
etc It can be anything So given an
image rotate the image
okay so that becomes a positive sample
or uh uh uh you flip the axis right or
you take out the color of the image just
use one of the channels and so on these
becomes positive examples What is the
idea The idea is suppose you want to
learn the concept of god sorry dog
that was truly a slip of my mind my
tongue Okay suppose you want to learn
what the idea of uh yeah wish there were
a way to learn the idea of dog by sorry
god by contrastive learning there does
not exist any any such thing as as that
is known to the human beings but you can
still learn the idea of uh you know
naturally occurring things by using
these kinds of techniques So okay
anyway so jokes apart suppose you want
to learn what the idea of an animal dog
is right so irrespective of whether the
image of the dog is flipped by 30 angle
irrespective of the fact that you dont
see a color okay and suppose you add
some noise to that dog image human brain
will recognize that it that has a dog
thats the idea now you learn the
representation in such a way that as
long as the image or the data point is
being sampled from the true underlying
distribution It learns the it maps it
to the same representation
Okay Now these are positive examples
What are negative examples
any other image
than X
that has
different semantics
right Ill write the semantics in within
quotes now negative samples are the ones
that is not a dog image
Now arent we begging the question
here Now we started all this by saying
that we dont have labels
Now we are saying to define negative
what negative samples are So we have
to ensure that uh in the bag of our
negative examples it should not be
coming from the distribution that we are
interested in which is the which is
non d dog images Now dont we need
labels for it It turns out that uh if
you make the that is why so you ask the
question right why do we need multiple
negative samples because of this now if
you have one negative sample now if you
sample suppose you are given a a data
set now you sample one image and you
take 10 augmentations of it that became
positive you want a negative sample you
sample randomly from the data set with
replacement now what are the I mean the
odds of uh having the semantics of this
image different as this image is very
low no I mean it can still come from the
same dog category but a different dog
But we dont want the representations
corresponding to two different dogs to
be different
Thats why if you increase the number of
negative samples by a very large number
then the odds of all those coming from
the same semantic class will be less is
the idea Thats why these techniques
are shown to work extremely well if you
make your batch sizes to be very very
large
So similar for instance had a batch size
of 496 samples now which is huge for an
image task Typically the batch sizes
would be of several tens of examples
right 8 10 and all that Now we are
talking of batch sizes of thousands of
examples So thats why then people
started asking this question how do we
reduce the batch size in contrastive
estimation and how do we ensure that we
sample good negative examples without
having class labels
Thats an active area of research you
know Ill not go deeper into it but you
got the idea right at least in SimCLR
take a large amount of negative samples
so that uh most of it will be from
different semantic category and for a
for positive augment I mean positive
obtaining the positive samples you take
several data augmentations and call it
positive so I I talked about multiple
data augmentations here right you can
have each of it as one positive example
while you are training thats how CCR is
trained
Is that all right
Any questions here
Okay
Yeah So Ill stop this lecture with a
mention on this particular technique
which is called Japa
referred to as joint
embedding
predictive architecture
So here the idea is you do contrastive
learning by entirely
eliminating the need for negative
samples
Okay So because negative samples create
such such an issue right So you try to
eliminate the entire negative samples
How do you do that is the question In
Japa what is done is as follows right
Now given data
they mask
several parts of data So suppose you
you have an image Okay Now mask this
random region Mask this region Mask
this region Call this as M1 M2 M3
Okay Now ask the neural network to
predict M1 M2 M3 given the rest of uh
the pixels
So thats the task The task that is
being solved now okay is not classifying
between the positive and negative
samples but it is that given the context
tell me whats missing
right so this is also I mean if you uh
if you think about it from from a from a
learning objective perspective uh its
the fill in the blanks right so if you
are given uh a an image okay and a
jigsaw puzzle uh you can only complete
the entire puzzle only if you know what
the entire semantics is So the entire
architecture so theres still a neural
network right there is a neural network
okay that takes in the context context
is the remaining pixels okay it also
takes the masks as inputs and given the
masks and the context it has to predict
the representations for the entire
image
Now since we have the entire image as
well So we know the representations of
this We know the representations that
has been predicted without uh those
entire image Try to minimize the uh nom
distance between these two
representations And thats the
objective to try in this
This also has a similarity between this
idea called mast autoenccoder that I
mentioned in the previous class Right
If youre looking at sequential data
what you do is that you give a sequence
as an input to a transformer Uh you
dont give the entire sequence but you
give a masked sequence as an input Ask
it to predict the entire uh token which
is predict the masked part of it The
loss is simply the uh cross entropy
anything any favorite loss that you have
between the predicted
sequence and the actual sequence
This is called mass autoenccod This is
also called joint embedding predictive
architecture This has also been shown
to be extremely strong
excuse me in in learning representations
and this will reduce the uh the
requirement for label data in the
downstream tasks
Okay questions Yeah
 this info see we are having like when we
are taking X as an image so that X is
totally different like we are taking we
are taking X as a dog but what if we are
taking variety of different dogs with an
X
 thats okay thats okay so that you have
no you dont have that information at
all that is why the question that Im
asking is given an image and its
semantic uh uh invariant transformations
I want them to be grouped into same
category
given a data point and its semantically
invariant transformations I want them to
be grouped into the same category
right and if the if the transformation
or if if if there is an image and
semantically uh non invariant image okay
or meaning different semantic image I
want the representations to be farther
thats all so every time you train every
time you can have a different dog image
and you do the same thing so network has
no uh idea whatsoever about about the
underlying labels or semantics
 But my target is to differentiate
between different types of dogs
 No my target is to learn the
representations for the given underlying
data set Remember in entire
unsupervised learning the idea is to
model the marginal density Thats it I
dont care what the semantics are
Thats why I told you all the story
right I mean we dont care about
labels We are not partitioning the data
space at all We are trying to learn or
model the entire marginal density by
these techniques Like if my aim is say
to differentiate between different
weathers
 different
 weathers of a same scene we have
different
 okay fine you cant do it with this
 we cant do
 you can represent extract the embeddings
from this and use label data to try
another neural network thats it so see
please note that the entire goal of
unsupervised learning is learn the uh
the marginal density okay without
semantics
and use it for whatever uh see in fact
what happens is as follows right I mean
uh in practice today if you are given a
problem lets say in uh uh uh in image
domain vision domain
you wont start training a
classification classifier from scratch
so there are neural networks large scale
neural networks that have been trained
in an unsupervised way on this so for
instance vision transformers we talked
about vision transformers remember In
Japa uses vision transformers as neural
networks by the way So you there are
vision transformers that are trained
using similar kind of techniques on
imageet data set What you do is that
you take your data set with labels Pass
all your images through the pre trained
neural network Okay get the embeddings
and train another MLP or a small neural
network or a transformer on these
embeddings for the problem that you want
to solve because there are already such
a rich embedding that has been extracted
by training this for months and years
and all these data sets and most of
these neural networks are available the
weights are available in in in public
So nowadays
I mean its very very seldom that a
neural network is trained from scratch
for a given problem You always do a
take a pre trained neural network and
fine tune either you fine tune in the uh
in the you know the transfer learning
way we did but
you dont take neural networks that are
trained for classification tasks you
know you take pre trained neural
networks that has been that have been
trained on these kinds of contrastive
learning tasks because the the
representations that have been learned
via contrastive learning or
self supervised learning are richer in
the sense that they are learning the
marginal not the conditionals
always take the neural networks that
have been trying to learn the marginals
See thats why you know generalists are
better So you can take a generalist and
train them to be a specialist but you
cant take a specialist and make them
generalist right Its difficult to do
it that way
So always better to be a generalist very
good generalist and then take it and do
a finetuning on whatever specialization
that you need Thats the idea Now this
completes whatever I wanted to discuss
on unsupervised learning Okay So from
next class Ill talk about the sampling
part which is the generative part of it
A couple of classes on what the the
first class will be on the principles of
what generative modeling is and Ill
give you a few examples and then one or
two classes on reinforcement learning
So that will complete the course Okay
Thank you
