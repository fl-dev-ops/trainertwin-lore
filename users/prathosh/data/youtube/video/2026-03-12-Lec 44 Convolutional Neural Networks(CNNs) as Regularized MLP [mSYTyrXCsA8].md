---
id: mSYTyrXCsA8
title: Lec 44 Convolutional Neural Networks(CNNs) as Regularized MLP
url: https://www.youtube.com/watch?v=mSYTyrXCsA8
date: '2026-03-12'
duration: 44:56
model: youtube-captions (en-orig)
transcript: true
---

## Transcript

Welcome everyone to the class Now
lets lets see how it is done in
popular culture Right So people dont
see a CNN as a as a regularized MLP
Okay They start by writing a writing an
image Lets do that
So lets say that we have this grid kind
of topology Lets say that uh it is uh
P plus Q pixels And please note that this
P times Q is what are D is the data
dimension is Okay
Now uh this is we we work with this sort
of a top This is your question We work
with this sort of a topology Now what
is the operation that a neuron does We
know that its inner product Okay
Typically in an MLP uh the weights of
the of a particular neuron is is
represented as what is called as a
kernel as a or a filter
because I lifted the p pin So this is
um its its mostly made symmetric So
it is uh its a k by k
and these are this is uh so w1 w2 w3 w4
w5
w9 I mean its its not Im just
assuming that its a 3x3 uh the kernel
right for example So yeah this is how
it is
Now
what is the operation that we do in in
an MLP when we are uh when we are
computing the neuron is sigma wranspose
x this is the operation that we do isnt
it so what is that in terms of uh this
kind of if you just want to mimic that
in in this kind of a topology what we do
is take this maybe I should have written
in a different color
This is K by K Place this K by K here
and do one inner product Thats it
Thats your wrpose X And now you see
why its local receptive field
So if I take this image and do a roster
can and make it a d dimensional vector
doing an inner product with a k by k
symmetric uh so called filter is
equivalent to doing this particular
operation right the wrposites its
exactly the same thing
you see that yeah now what I do is I
slide this filter
so lets say that Im doing in a
non over overlapping way I slide this
filter K pixels Okay By the way every
data dimension is called pixel in the
image processing community
Okay So now I slide it by K and do the
same operation and keep doing it and
keep moving this filter uh in the right
direction and left Then do this right
Uh then then what am I doing Im Im
incorporating both the regularizers
isnt it The local receptive field and
parameter sharing Your question is
answered now So now yeah so now you
know right I mean we are not
representing it as a vector we are just
striding it Okay
is this all right
do you see that doing this operation is
exactly the same operation that we did
on MLP
and by the way inner products okay are
called convolutions in the signal
processing community
Of course you need to flip one of the I
mean if you have two signals right or
two uh vectors take one vector flip the
other and then take a uh inner product
is what is called as convolution I mean
of course you need to slide that filter
over the input signal that thats
exactly what we are doing here I keep
saying convolution neural network is a
bit of misnomer because youre not
flipping
it should have been correlated neural
network or something right it doesnt
matter but you you got the idea right
the convolution operation everybody Im
Im assuming that everybody knows what
convolution operation is in signal
processing community youre given two
vectors one is called a signal the other
is called a filter you stride that
filter over the signal one uh one side
at a time and take the inner product and
add whatever you get is what is called
as convolution product So this
operation that we are doing so in an MLP
with a feed forward operation with
parameter sharing and local receptive
field is the definition of convolution
isnt it
 Its shifted one pixel at a time
 Thats a hyperparameter again You can
shift one pixel you can shift three
pixels you can shift K pixels doesnt
matter Thats called stride size
Thats a hyperparameter
You got it inner products with local
receptive field and parameter sharing E
is nothing but convolution Do you all
see why it is the case
Okay So thats why the name so thats
why you say that you do this
convolutional operation here
This is the conf operation
and what will you get
You get few more neurons right So every
inner product that we take okay we have
to do conf and also well have to do
this nonlinearity operation otherwise it
becomes a linear filter right we its a
neural network after all unless we have
this nonlinearity
uh we will not have universal
approximation theorem working so we need
sigmoids so do the convolution and then
pass it through a sigmoid pixel wise and
you get a few neurons and those neurons
are again uh
arranged as a grid So each of the pixel
here is the outcome of
uh
 one one convolution right or not I mean
the entire thing is convolution So you
take the filter place it on one subset
of data do an error product pass it
through sigma is the is what you get I
mean is what is what gives you the the
one activation map its also called
activation map or a pixel in the second
layer So what will be the size of this
If this is you start with P by Q what
will be the size of uh the second
activation map
 Yeah it will be P by K Q by K Uh the
uh yeah the uh floor of it if Im
assuming that this ride is K If I make
it stride dependent this size will also
be stride dependent Do you see that
Thats a hyperparameter Typically
stride sizes if filter size is taken to
be 3x3 stride is taken to be one by one
and so on And youll have to also
ensure that the sizes of these thing
match by doing what is called as zero
padding which is if the if the str and
stride and k are not matching right so
what happens is if you take 3x3 the last
operation will not will only have two
pixels you need three more So you have
add zero to the final layer and then
continue doing that thats called
padding Okay the size of the next
activation map depends upon the the size
of the filter Okay and uh the size of
the the stride choice and the padding
that we do I think its its clear it
is all right Do you see this as an MLP
Now
this is an MLP with these two
regularizers put on Right
Any questions now
is an additional
input
field nor we do parameter sharing right
 it can be easily understood as zero
 of course I mean even parameter sharing
is understood as same uh the the these
things are taking the same value with
probability one no
correct
see now if you see the weights
corresponding to this neuron as 100
dimensionally then some of the
dimensions are probability of some of
the dimensions of the weights are zero
probability of the other dimensions are
taken to be exactly the same thing
conditioned on these uh the other the
weights of the other neuron thats also
a strong regularizer
right so this is the story right MLP
with parameter sharing and local
receptive field becomes a convolutional
operation and thats what a CNN is
 so one of the rules of the game is that
you know dont
dont ask questions that have not dont
dont use terms rather the ones which I
have not used in the in the course I
Ill talk about it in a while yeah any
questions on this yeah
 so sir does this mean we can like treat
a like the elements of a matrix as a
specific neuron
 which matrix
 like the P by K by K matrix so
 this one
 yes
 this is the outcome of a neuron right
see
 here yeah there is an implicit neuron
and the output of this is what uh this
thing is
expect fewer and fewer neurons in the
subs
 thats an architectural choice you were
not there in the previous class I
suppose
 is that okay then I told you right in
the typically for classification
problems uh when you go deeper and
deeper the number of neurons keeps
decreasing because the input dimension
is much higher than the output
dimension
Yeah
Is it
Oh this uh this is this should be the
stride
This the denominator should be stride
So this is P Yeah So Q minus correct
p minus k plus 1 q minus k plus 1 divided by s where s
is the stride size Yeah Okay Fine
Its simply K theres no one because we
have not padded also Yeah Fine Okay
Fine
Okay The story doesnt stop here
Right So I I told you there is one
other aspect to it There was another
question that he asked Isnt it
restrictive that if you do this this one
orange K by K filter is only doing one
particular type of uh feature extraction
right Whatever feature it extracts is
it a good idea to do Its not So what
we do what is done typically is that you
have another filter
and do the same operation again
It would have been good if I had used
orange here
So another p min minus k q minus k thing and
lets call this lets call this u uh k
okay hold on this is k1
this is k2
So what happens is that you take the uh
exact same input image or input data
point and
and do this now
One second
Theres another convolution here
And after that we still have this
operation
What
 Q minus K plus 1 is it Okay Fine If its
there if its there Okay
depending upon the padding So what what
are we doing here is that we take maybe
uh let me just
make this also orange color I think
its better that way
Okay Yeah I think now color coding is
also correct
Image is black and filters are different
colors and activation map is it So what
what is done is that you use another set
of uh filters right uh to u and and do
the exact same operation So now this
can learn a different feature
Does it make sense
Now from an MLP standpoint what are we
doing
 K1 and K1 itself
 It can be K2 So Im Im using K1 and K2
just to indicate that these two are
different filters
 In fact they can also be of different
sizes
 Its okay Doesnt matter Doesnt
matter Just this is just to ensure that
there are two different filters Right
So now from an MLP standpoint what are
we doing
 Huh It is not this direction that Im
talking about Now Im talking about
another direction which I cannot
represent on this plane
Right So there is there are there are
other set of neurons that are coming out
of the this thing Right Yeah You see
this stack of neurons in the other
actually its a dimension now
yeah multiple filters for and every of
this filter or every of this uh uh of
this filter will be shared across
different data dimensions and there will
be parameter sharing you see what Im
saying now how is it done is that I mean
typically it is represented by stacking
uh all these outcomes right
one uh before the other So you create
tensors
You understand Now how many filters can
we have in each layer is another
hyperparameter
Do you get it
right So each of the filters will now
learn different parameters sorry
different features
The hope is that they learn different
features Theres no guarantee because
still we are throwing it to erms mercy
So many parameters
 thats why you have 70 billion
parameters
thats why CNNs orn nets and all that
have those many parameters because this
is how it is designed is this clear to
all of you see chandan made a nice point
he said that youll have to have the
dimensions of this these two filters to
be the same otherwise the dimensions of
the outcomes will not be the same which
will not make enable you to stack them
one below the other right which is the
point which is a correct point that is
how you do it unless Every time you do
filtering youll have to pad it with a
different size so that the outcome will
have the same dimensions But I used K1
and K2 just to make ensure that there
are two different set of parameters
Now to your question when we are when
we are doing backdrop and forward uh uh
forward pass right Well have to
ensure that these things are encoded can
be done which can be done right
Is this clear So lets now have a
unified uh uh view of all this
So a CNN
is defined this way
So generally start by with a data which
has
P by Q by R
Data itself can be a tensor of
dimensions P by Q by R This is a grid
What is an example A color image
Color image has three channels So this
is the third dimension is called
channels in the computer vision
language
And Ill come back to the MLP uh view
here because as I said
it its easier to look into that way So
all of this can be stacked into a large
D dimensional vector where D is P times Q times
R Remember that its just rearrangement
of data in a particular way So
um an RGB image okay that we that we
see on our phones and computers have P
by Q by three pixels
If you go to the electronics right
what actually does what actually happens
is there will be a sensor and there will
be a grid of sensors and each pixel is
actually a physical sensor If you have
408 4086 4086 as your image size
there will be those many sensors
in your camera every pixel is a
physical sensor On top of it they
would put something called a bare
pattern which are filters which are
physical optical filters that would only
that would block some uh uh uh some uh
wavelengths and only let some other
wavelengths to pass Thats how you get
these three channels RGB
I dont know if you have actually seen
an R channel It looks like a grayscale
image to human eye You have to reverse
that base pattern while rendering Those
are again Im not here to teach computer
vision but anyway So this is how you
get three channel This is one
possibility The other possibility is
that suppose youre looking at an MRI
Every slice of an MRI right is one
channel of the image So this is this
will have P by Q by00 channels So its
a its a tensor
Okay So if you if you see what is
called as a tomography I think right
where you take different slices of
X rays and then stack them as a channel
even video a video frame is this
right stacking of multiple static
channels and where the third dimension
is the temporal dimension so every a
video can be seen this way the most
generalized version is that you have a
tensor of size P by Q by R you can add
one more dimension it doesnt matter
thats a tensor is it Okay Now so
start with the P by Q by R uh R uh data
Huh
 Why
 I thought my P was capital here
Thats the first letter of my name That
cant be small
Okay Yeah Anyway
right So now what happens is that you
now have filters right You have
filters
And now if you have the generalized P by
Q by R as your uh as your input data
tensor okay then your image should
your filter should be K by K by R
Otherwise you cant do inner products
See
you take a kx by k by r cq and put it
into a subsection of p byq by r cq and
then you take an inner product that will
give you one number because after all
its an inner product that we are doing
right is it okay
Now suppose we have
P is already taken
 L L okay well do L
uh okay lets say that all of them have
K by K by A into R as size and we have
L filters
Okay Then we are doing convolution
What will we get
we get
here well get
this will be uh p min minus k q minus k plus 1 I
mean Im assuming that this stride size
is k right or divided by s okay maybe we
can do that this will be divide by s if
the stride size is s where s is the
stride size huh
p minus k by s plus one yeah thats what it
And there will also be a floor here No
this may not be a
an integer So
will it be a two dimensional grid
 Yeah there will be another dimension to
this
Okay come here
Now this will be
So the number of channels in a
subsequent layer will be equal to the
number of filters in the previous layer
You got that Now suppose I go deeper
The
the third dimension of the filter in the
next layer has to be equal to the number
of filters that we have chosen in the
previous layer
R
 huh
 R
 R will not come no because you are
taking this K by K by R taking inner
product so that will go away youre
actually uh marginalizing along that
dimension so R will not come
is that all right
now what are the hyperparameters here
hyperparameters are
equivalent
uh filter is
The inner product that you take
is see a neuron is implicit right I mean
because its its a mathematical
operation that we are doing so a neuron
is is implicit this entire operation is
a neuron to me isnt it inner product
and then you take that uh
non I mean sigma nonlinearity is what a
neuron is okay so hyperparameters are
number of filters in each layer
and
filter size
Can there can there be different sizes
of filters in each layer Yes
inceptionet does that Ill Ill take a
few names Okay you make different
choices for these hyperparameters and
name that CNN
with your name Thats what people have
done or your companys name or whatever
or whatever fancy name that you want to
name it after filter size and what else
Stride
of course if you have stride and you
need to do padding also
what is stride
who is asking okay stride is I told you
Ill just tell you again see when you
place your filter on on on your image
right here
its the k by k uh uh pixels that you
cover or the what should be the next
operation the next operation should be
take another k byk subset of data and
then doing your product which K by K do
you take do you take over overlapped one
or non over overlapped one how many how
many data dimensions do you stride over
 I mean if you over stride size is one
then you overlap by k minus yes str this
thing if its k then you dont overlap
and so on yeah
and what else so you have a number of
number of layers also
Huh
 That is number of filters No
number of neurons in each layer here is
number of filters isnt it
 No Number you choose
that also You choose
Oh layers meaning depth So layers in
a neural network is the depth of the
neural network
See thats why I didnt want to take
that letter L here
What is the depth of the neural network
that you talk about Okay you might
have heard about these architectures
ResNet and all that right ResNet
ResNet 64 ResNet 128 That 12864 talks
is actually the depth of the neural
network how many layers that you have
in the neural network
Okay almost done with CNNs A couple
of more nuances before we go there Any
questions
 We are applying filters to the input and
stacking the result of
 correct correct stacking the result of
every filter as a channel right in the
next layer So this this becomes the
input to the the next subsequent layer
and so on So always this is the rule
right for a CNN to work youll have to
ensure that the third dimension of the
filter okay is equal to the third
dimension of the input that you are
looking otherwise inner products dont
work out no dimensions have to match
thats it
 difficulty understanding why converge to
different weights in every
 okay its this the question is why would
ensure that uh that uh the weights in
each each filters are different Okay
Uh theres no guarantee So the question
is equivalent to asking in an MLP why
would every weight be different
Its exactly the same question
Theres no guarantee
right We are just having these many
parameters that the neural network can
choose from It will choose Empirically
what has been observed though is that if
you have lets say some 10 filters they
have seen that one filter responds to uh
edges the other filter responds to color
and so on is what empirically has been
observed Why would ERM ensure this
Theres theres absolutely no guarantee
that ERM will do this Its simply a
function and we have gradient descent
and optimization that we are doing on a
loss landscape Thats all
So I mean the question is same like
asking suppose I have a five parameter
model simple polinomial right I do
gradient descent on it what is the
guarantee that all coefficients will be
different
theres no guarantee however since erm
is there and the objective is to
minimize the empirical risk or the
average loss if you choose all of them
to be the same the chances of minimizing
the uh the training error will be low
isnt it go back to the same polinomial
question suppose I have the data coming
from a fifth degree polinomial which is
uh perturbed with some noise and my
model I choose to them model I choose my
model to be a five parameter uh or a
fifth degree polinomial if all of my
parameters will be the same will the
training error converge
it wont however suppose my data is
coming from uh lets say second degree
polinomial and Im using a 10th degree
polinomial as my model which is an
overparameterized model uh will some of
my coefficients be zero Of course we
will be and we will enforce that they
are zero by regularizing isnt it
Thats the whole idea of regularization
Now the the assumption is that typically
we underparameterize the models right
Or rather over even if you over
parameterize we regularize to ensure
that uh that that we trade the bias See
everything that we did with bias
variance decomposition still holds Even
if youre using a CNN you still have
the training error test error and you
have the bias variance decomposition
and youll have to choose the best
point Yeah But short answer
theoretically there is no guarantee
that these will be different Its just
optimization
 Come again
theyre communicating
So the kind of stacking
 didnt get the question
 So lets say we have each
different
 Sure
 So the kind of stacking is not
Still didnt get the question Maybe
well take it after the class Yeah Um
anything else Okay So okay So
suppose you are solving a classification
problem right Which is an image
classification problem or something So
how is it done Typically Ill just
give you examples of neural networks
Okay So before we go to the examples
maybe as I said there are a couple of
other things that people do Something
called pooling
theres something called pooling
operation Okay lets say that we have
an image of size
or a data of size P by Q Okay then I
want uh this to be reduced by half
for whatever reason There is one reason
could be that um that
so sometimes what happens is uh if there
is lot of noise in the image as they say
uh you need to smooth out the image or
the pixels in the sense that uh there
are some noise that are added in the or
comes up in the image and to get the
features to be extracted uh in a
particular way then youll have you you
want to smooth it out lowass filtering
operation Okay What is low pass
filtering in in image crossing
community It is subsampling So what
you do is if you want to reduce the
image by two take a take uh I mean
replace every pixel in the input with
the average of the neighboring pixels
and reduce the size by half
What what Im saying this is average
pooling
right where you reduce the size of the
neural network or the the the input data
or activation map by two by taking an
average If you take 4x4 grid right
and then take an average
then
then what Then nothing Yeah So but
these kinds of operations can be looked
into as hard coding hardcoded filters
for instance Yeah this is what I
wanted to say If you take a 2x2 uh
filter with all ones and take an error
product it is equivalent to taking an
average No
of course you need to divide by not not
all ones It will be 1x4 1x4 1x4 If you
take all values to be 1x4 then uh uh
doing a convolution with such a fixed
filter with uh with with values 1x4 is
equivalent to doing a 4x4
averaging This operation is called
pulling Huh
 What did I say
 1x4 is the value The filters are 2x2
2x2 and did I say 4x4 Yeah So then it
is averaging 16 pixels Yeah you got
the idea 2x2 filters and then thats
this operation is called pulling Okay
this is fixed convolution
 Information is yes
I am just saying this as a an addendum
because Im not a big fan of pooling
layers cuz I still sort of dont
understand why why one needs pooling
layers just to reduce the dimensionality
reduce the size and so on So thats how
people do it This is this is average
pooling
Okay Theres also something called max
pooling
If you do max pooling then you take a
4x4 grid and replace it with the maximum
value of that Thats max pooling
Okay Now thats a non ifferiable
operation
How do you do back prop If you do max
pooling youll have to hard code Its
not exact See if you take a four by if
you take a fourdimensional vector or
four numbers and replace that with the
max of those four its a non ifferiable
operation How do you when you come back
how do you what value do you replace
with width Theyll just do some
approximation and do it There are
multiple ways of approximating backrop
in differentiation in max maximum
operation for instance replace it
replace all of the pixels by the same
value and so on Thats one bad
approximation that is done This is
called max pooling and average pooling
and so on Okay Now yeah So this
sort of completes uh how CNNs are
built So CNNs end to end will look
like this
Didnt expect this class this thing to
take so much time Okay So we will
start with lets say that suppose we
have a
I will say examples
examples of CNN for end to end end to
end tasks Okay lets first take uh the
classification by regression tasks
lets say classification tasks
So you start with a
start with a P QR grid This is the
image
So then you have uh
fcon layers and then pool
of con pool
conf and so on And you keep doing it
and after that you do what is called as
flattening
which is simply roster scan of the grid
that you have and make it a vector of K
dimensions
Okay And then you have an MLP
This is K classes at the end
and then do ERM Thats it
This is how you solve classification
problems during CNN
forward after
 huh you have to know because finally you
need a k dimensional one not vector
right after the final convolutional
layer you need to all flatten all of
them meaning arrange them into a vector
and then do a fully connected layer
which is MLP
 yeah because its a its its You have
arranged that as a grid Keep getting
grids After grid you simply flatten
And by the way there is no no sacrosant
uh sanctity on writing con after pool
after con after pool You can do con con
then pool con It its a complete design
choice
right there is no reason why it should
they should be alternated Just given an
example of thats why I wrote an
example So this is for classification
Is that okay
Now you might have heard of uh uh things
like alexnet leet
resnet inception net all of them are
examples for this with hundreds of
layers in residual neural network
Right There is one other kind of
connection that is called a skip
connection where simply what is done is
you take you take you connect uh the the
neuron from the previous layer to the
next layer right Just skip one The
idea is that and and that you do with an
identity operation by assuming that that
you have a path to learn identity So
thats the uh the motivation that is
given right So examples are so leet so
this leet is named after that yani
kundai there is alexnet
and there is reset and all that
inception net and whatnot
And please look into some of these
examples right simply convolution layers
and in inception net what they do is
this was I think you know Googles paper
where they said we will have filters of
different dimensions in each layer so
there were 9 by9 7 by 7 5x5 filters 3x3
filters in the same layer concatenate
and then do different kinds of I mean
they play with these hyperparameters
right
this is for classification right so
lets look at I mean of Of course you
can do the regression tasks also here
Okay Uh now what is the example of a
regression task in uh in in image
crossing So what so given an image what
do you want to what do you want to
regress over
Huh See one of course one classical
example is that of that of bounding box
extraction where suppose you are given
an image and you want to find out put a
box around a particular object One
example is tumor marking So youre
looking at images with some particular
type of abnormality and you need to do a
bounding box detection The way it is
done is cast it as a regression problem
where the out output will be the
coordinates of this particular
rectangle You need four numbers to
represent a rectangle Isnt it So give
those four numbers Your x will be an
image Y will be those four numbers
Regress like this Thats it
Okay This is one example The other
example is what is called as a fully
convolution fully convolute convoluted
network what whatever convolution
 fully convolutional
see Im not a big fan of architectures
because they are like Lego blocks right
its its left to ones imagination one
can do whatever they want by doing it
there are some examples thats it so
example for this task is lets say Um
um what is it called
semantic segmentation
Yeah Um okay lets say
so semantic segmentation what is the
task given an image
uh you need to classify each pixel okay
uh as belonging to one of k classes
Lets say that you have you know that
there can be 100 types of object object
categories in your image Okay Now
given an image the output has to be
another image
Okay That will have different colors
for different object categories
So input is an image output is an image
So thats an example of fully
convolutional neural network The other
example can be what is what people call
as style transfer
where uh you give um your picture and
the output has to be the cartoonized
version of you
Input is an image output is an image
Okay these kinds of applications So
how do you do that Start with
um
P by Q by R image and then keep doing
this conool conool business
and do it Finally dont flatten it
Okay So youll have to ensure that this
will be
this will be P by Q Suppose you have
lets say K object categories The
number of channels here would be K So
there will be every every slice
corresponds to an absence or a presence
of that particular object
This is called a segmentation map In
these kinds of applications the
typically what happens is the uh the
architecture of the neural network See
generally for classification what
happens is as you keep moving deeper and
deeper into the neural network the sizes
of the grid will keep reducing right
because uh P by Q by R is much larger
compared to number of classes K classes
therefore you need to reduce the size
but in a fully convolutional uh uh
setting right what is done is that you
start with a PQ uh image right and then
you keep reducing the size
okay up to a particular point and then
from there you keep increasing the size
back again because what you need is you
need the output to be of the exact same
size as the input isnt it
right so therefore you first reduce the
size and then create a bottleneck and
increase the size now how do you
increase the size in a in a
convolutional operation in a in a in a
in a in an MLP its okay you increase
the number of neurons but in a
convolutional setting how do you
increase the size
 yeah see if you change the filter size
this operation is called transpose
Transpose convolution the same thing but
you know you in instead of convoling
with the filter you transpose it and
then convolve in from the signal
processing community uh it is equivalent
to the upsampling operation People also
do uh fixed upsampling So you can learn
the filters in the in the uh okay by the
way this this architecture is also
called the encoder decoder architecture
Encode the information and then decode
it Okay Um yeah and this has a name in
the uh the computer vision community
This is called UET
because the shape of it looks like a U
See Im rushing through all this because
this is not a computer vision course
right but Im just telling giving you an
example of you know how convolutions can
be used Okay is that all right Now how
do you learn
back prop erm that we have learned The
only thing that is to be ensured is that
when you do that youll have to ensure
that the parameter sharing and the local
receptive field are encoded into your
forward equations and backward
equations Please take that as a
homework and do it Itll be a part of
your assignment anyway Ill ask you to
implement uh a convolutional neural
network from only using numpy Uh yeah
but I think well be done in tutorials
but youll have to ensure same thing
goes with any architectural tweak that
would be done I thought I would finish
both CNN and RNN today in one class
Okay Yeah this is about CNN So well
not we will stop for the discussion on
CNNs here Next class we will look at
the other kind of uh topology which is
called the sequential data uh for which
uh another kind of regularizer is
imposed on the MLP and that is called a
recurrent neural network or an RNN We
will look at uh that the next time we
meet Okay Thank you Thats all for
this todays class
