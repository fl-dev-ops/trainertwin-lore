---
id: 0wd-LIzzfM0
title: Tutorial 14 Part 1 : CNNs
url: https://www.youtube.com/watch?v=0wd-LIzzfM0
date: '2026-03-20'
duration: 33:52
model: youtube-captions (en-orig)
transcript: true
speakers:
  speaker_1: null
---

# Tutorial 14 Part 1 : CNNs

## Transcript

speaker_1: Hello all
welcome to this tutorial
in which we will be looking at
convolutional neural networks its
implementations
how do you obtain a pre trained model
and how do you extract embeddings
Okay now these are the main features
that well be looking at from the
perspective of the
implementation So till now uh I Im
assuming that all of you are quite
comfortable with
coming up with an MLP implementing an
MLP and then running the training
algorithm
So now well be going ahead with a
regularized MLP Now wherein which now
we have the idea of parameter sharing
and then
the local receptive fields when you
regularize them now we get CNNs Now
from our
theory sessions now it would have been
crystal clear by now Okay So now we
will look at a a very nice uh
implementation graphical implementation
of uh
CNNs Okay Now this was done in
Stanford CS 231 deep learning for
computer vision course Now we are
looking at its uh
uh official website where we will go to
this convolutional neural networks and
then lets try to
understand visually
how does a
a CNN work
Okay Now this is an image
Now the one that you are seeing here is
an image and these two are the
two filters that are there Okay Now
each filter
now will have
some components and that result that
matches with the number of channels that
are there in the
input volume Okay Here there are two
filters and each filter has three
components depending on the the number
of input channels that are there Okay
And then the kernel size the filter
size is 3 cross 3 And then as you can
see here how does it work
Okay
So it goes here
You will see the exact operation does
this perform
but visually this is what it does Now
you can see here the green one moving
Wherein which of post convolution
operation this is the outcome
Okay
Now this is
hovering over the different parts Okay
So now lets go into the
I have taken a
a simple
a still image of it so that we can
understand how does this convolution
operation work
So now as you can see here this part
is only the image The blue part which
you see is the image and then the zeros
that you have put here this is zero
padding Okay Now we have padded this
whole thing with one layer of zero
padding Now this is one Now because
now you have put one layer if you want
one more you can put it here
Okay And padding is used whenever you
want to have some kind of a
match in the output dimension We will
show it to you how
So now
your input image that we have is 5 cross
5 cross
3 Okay Now for this convolution
operation
so now the input that we have
now lets represent the input to this
convolution operation as H in height
W in width
into
D in
Now this in our current example that we
are considering this is 5 cross 5 cross
3 And please dont consider it post
padding Okay Now whenever we say
image size which is
we are considering the the pre padding
uh
data which is this
Okay On this youre applying a 3 cross
3 filter
Okay So now you have
two filters Now lets make a
that So the number of filters
in this specific example
so the number of
filters
which is represented by K
okay in this case Now please dont
confuse this to number of classes that
are there Now here
uh we mean K is the filter size
So sorry number of filters now we
have two
Okay And then what is the size of that
filter That is
the spatial
extent of that filter which is
represented by F now which is
3
Okay its a 3 cross 3
So most of the cases we uses
we use
a a square filter size Okay Now its
not mandatory that you should use a
square filters You can come up with
rectangular filters as well But in
most of our
computer vision applications we will
come up with a square filter Okay
So now and then you can see here
the movement is in each direction it is
moving by two Now it is here next it
moves by two units of distance
Now this is known as the stride Okay
Now this is the
the stride
now which is uh
represented as S and the value it is
taking is two
Okay And then how much padding we have
done
The padding
is represented by P
is given by one
Okay
And
any convolution is having these hyper
parameters Okay
So
in a convolution layer the values that
these two matrices take the filters
take okay including the bias now
these are the weights
Okay These are learned Now Im not
saying about them Now what Im saying
is now the fixing of number of filters
the spatial extent or the size of the
filter the stride and the padding now
these are
uh hyper parameters So you are not
learning for any of them you are fixing
them and then proceeding Okay So now
whenever you have uh
uh these hyper parameters and then the
input size which is there now we can
actually predict the output size
So now
if you have any convolution operation
which takes this uh
H in cross
W in
cross
D in Now here W represents width not
the any parameters Okay
Now when you apply a convolution
operation
now convolution operation will have the
parameters uh the the hyper parameters
K
F
P
S
With these uh
hyper parameters now whenever we apply
now we get
H out cross
W out cross
D out
And what will be the values of this
Now
H out
is equal to
H in
 minus F
 plus
2 P
 S
 plus 1
Okay
And then
width
is
W in
 minus F
 plus 2 P
 S
 plus 1
D out
 equals
K
Okay Now which is number of filters
So now lets put in these values and
see whether there is a match Now in
our case H in is 5
the spatial extent is 3
 plus 2
 2
 plus 1
Now this is 3
Similarly this is 5
 minus 3
 plus 2
 2 plus 1 This is 3
This is 2
Therefore now we have our uh
output now which is uh
H out cross
W out cross
D out that is of size 3 cross 3 cross
2
Are we getting it
3 cross 3
you have two such things
Okay Its a 3 cross 3 cross 2
Okay
Now now using these formulas now we
can obtain
uh
with the given
hyper parameters and the input
dimension we can obtain the output
dimension
Okay So now coming to the
operation here Now how do we do it Now
you have
youre actually currently looking at
this part of the image using this
filter
Okay now what do you do You perform
element wise multiplication of
this
matrix and this matrix Similarly you
perform an element wise multiplication
of this matrix
and this matrix
Similarly with this
and with this
Okay
And then you have a bias term you add
it out Now lets
do it
Now zeros normally we can always
ignore so Im just marking these zeros
so that
just to know that where are zeros I
dont need to worry about those zeros
This is zero
So I dont need to worry about this
These two are zeros
I dont need to worry about this The
third one
this whole is zero
I dont need to worry about this
This is also zero
So I dont need to worry about any of
these numbers while performing the
operation just for computational ease I
have a
two here
minus one here
Okay so now this is
2 into minus one
plus
I have two here minus one here
2 into minus one plus
I have one here
one here
plus one Now this is minus two minus
two
minus four is minus three
Okay
and here you have two here you have one
here
2 into one plus
you have two here you have minus one
here
plus two into minus one plus
you have one here you have minus one
here
one into minus one Now this is minus
one
Now coming to this you have two here
you have minus one here
So this is minus two
Therefore the overall thing is minus
three
minus one minus two
These are from
the element wise multiplication and then
you have to add this bias term
In this case the bias term is
plus B1
which is zero Therefore the total is
minus six
As you can see here
you can see the minus six here
Okay
This is how now then youre looking at
this point then you move by two units
You will go to
here these aspects and then you will get
this minus one
Now and then once youre done here now
here you go to the next one here you
take three three of this
three cross three
Similarly you perform
Now this is how you perform the
convolution operation Okay
now this is just for your comfortability
in terms of visualizations now when you
have the a grid like structure
Okay
And then
the next thing that we should look into
is the idea of pooling Okay Now
normally we have two kinds of pooling
One is max pooling the other is average
pooling
So now whenever you have a
input Okay now you fix
a kernel size
okay and then the stride Now here Im
saying that okay now this is
two cross two is my filter and then my
stride is
two
Okay so now I look at this
I take the maximum value
I obtain this
I take this
I obtain this
I take this
and obtain this
I take this and obtain this
Okay
Now you get the maximum of them That is
what is known as a max pooling If you
take the average now that is known as
the average pooling
Now this size now its exactly the same
formula you use Now for example if you
look at that here the HN is four
minus F is two There is no padding
divided by
uh
two plus one
This is two
Correct Now this is similarly you will
do the other so it will be two cross
two
Now always remember this Now whenever
we have a
two cross two kernel and then the stride
is two
youre reducing the spatial dimension by
half
That is what is exactly shown in this
part of the figure
Okay Now you have 224 224 64 When you
apply
a pooling now with two cross two filter
and then the stride of two it get
reduced to 112 112 64 Okay there is no
change in the number of
dimension but there is a change in the
the spatial size
Okay
Now this is max pooling now that we will
be using now whenever we need to reduce
a
dimension This is a the practical
way of handling it
So now we come up with a network Okay
we say that its a convolutional network
which is used for classification We are
looking at the classification You have
a convolution operation in which there
will be some filters and thing And then
after that you have a activation
Now preferably
it is empirical again So for a
classification task whenever were
dealing with images okay we use relu
activation whenever we are dealing with
images Okay So now you have the
convolution you have the relu You have
again convolution relu and then you have
a pooling
Like this you repeat and finally
whatever you get as the final one
that you flatten it Okay you convert
it into a vector and then pass it
through a
fully connected layer to get whatever
number of classes are there whatever
number of outputs are there now you try
to obtain them
Okay now this is the idea full idea of
the convolutional neural network
So
and see always remember
here there are one two three four five
six Now there is nothing sacrosanct
about the six If you want seven you
can put it It is just one example that
we have taken to work and understand
Okay and all these images are from the
same Stanford
site that we just tools CS231 site now
which we have looked at All the images
courtesy are from the same site Okay
So this is how we obtain a convolutional
neural network Okay so now lets look
at implementing them
Now the first CNN network that actually
came with MNIST data now is by
Yann LeCun So he is the one who came up
with the first
convolutional neural network So you
might have heard him in recent news now
where in which he got the highest seed
money for his company in Europe Okay
so he was earlier with Meta Labs Now he
has his own startup So
now the first CNN network that we have
this from Wikipedia Now this is LeNet
Okay now this was done for
MNIST data set
Now the the second one is second column
is AlexNet Well come to that The
first one is LeNet Now it is the the
MNIST is the
the data
So MNIST is 28 28 to one
That is the size and then you pass that
through a convolutional operation now
wherein which you have a five cross five
kernel
Okay
So now as you know what are the
parameters that you need to
fix the thing Now one is the number of
filters you need the spatial extent
stride and padding See whenever stride
and padding is not explicitly specified
now we consider stride as one and
padding as zero That means that there
is no padding
Okay now whenever
the stride and padding information is
not given stride is considered as one
and you dont have any padding That is
exactly the case here Now you dont
have a stride
uh sorry you have you dont have a
padding you have stride as one Uh
sorry you have sorry you have two
padding Sorry sorry So you have two
padding here So the stride is one
Now and the size is the size of this
filter which is F is
uh five cross five And what is K How
many number of filters are there That
is not specified but from the equation
we already know that
so K is D out Now if I know the output
dimension those many filters are there
Here they have specified the output
dimension
Okay therefore it is the six is the
the number of filters Now you have the
kernel size
you have the number of filters you have
the padding and then you have the
stride Now you can obtain the
the output size dimension and after that
youre using a sigmoida
activation followed by
pooling
layer with two cross two average kernel
Now we looked at two cross two max
kernel and then
you You rather than taking the maximum
value you take the average value
And then the stride is two Now as I
told you
you know there will be no reduction in
the number of dimension but the spatial
reduction is by half So 28 becomes 14
Now and then again uh that is passed
through a convolution layer
Now which is having 5 cross 5 kernel
no padding
Okay Now P is zero S stride is one
and the number of filters are 16
So after application this is the size
that you get That you pass through a
sigmoid activation
And then you pass it through a
uh average pooling layer with 2 cross 2
and then the stride is two Now because
of which especially uh the dimension
will be halved
So you have
5 cross 5 cross 16
Now 5 cross 5 cross as in this you
flatten it up
Now when you flatten it up you get
400
And then you should have an MLP now to
convert it into 10 number of classes
right
Okay Now 400 to 120
So then sigmoid 120 to 84 again a
sigmoid 84 to 10 Okay Now why did
they come up with 120 84 10 See
these are all heuristic numbers You can
come up with any numbers They have
these many fully connected layers Now
this is LeNet
Okay
Now we have to specify all of these in
our code
So now lets see how to do it
So we have the
code ready with us
Im assuming that all of you are
comfortable with the ideas of
data loaders the transforms and then
the So obtaining the data Were using
the MNIST data
Okay
So these are the necessary libraries
Torch is the base library NN is for
neural network This is for optimizer
This is for data set and transform This
is for data loader Now if the data is
there Ill just change the runtime to
T4 GPU first to work
The CUDA device If the CUDA is
available now then if the GPU is
available itll take it Now batch
size Ill make it as 128
These are the hyper parameters
So learning rate is 10 to the power of
minus three and the number of epochs
Im trying it training it for five
And then the transformation on the
features that youre having is youre
just converting it to tensors Youre
not doing anything else
So this we know
How do you obtain the data set Obtain
the data loaders That is also fine
So now comes the important thing which
is you want to convert it
into a
uh
Uh so you you have to have the network
structure This is a LeNet structure
So I have number of classes is 10
Now whenever you have
a network now
we have this
Now till this point now this is what
is known as the feature extractor
Okay And this is what is known as the
the fully connected layer which is there
is known as the the classification head
See just just because we are using a
convolution layer that doesnt mean
that we are going ahead with
classification itself
Now if you remember one of the cases of
image captioning now you pass the image
through the convolution layers you get
an embedding here Then you can use it
as an input
to any of these sequence to sequence
models
And then you can generate the
uh caption for it Okay Now this
embedding which is there now it can be
used for any downstream task
Okay It is not like you have to use it
only for classification Now this can
be used for any downstream task Okay
thats perfectly fine
Okay So but here we are using it for
classification So that means that
there is a classification head now
which is an MLP
Now the first one is the feature
extractor
NNsequential Now by now you know what
is NNsequential
So
and then now comes how do you define a
convolution layer
Okay To define a convolution layer
uh if you
remember what are the things that we
need
Now we need
number of filters
the size of each filter stride
padding
Correct
So and then if you number of filters
is fine
So you can say that Okay I have two
filters That is fine Now how many
components should be there in each of
the filters Now that is dependent on
how many input channels are there now
That also needs to be defined
From a programmatic perfect perspective
you have to define these matrices How
many matrices of what size I have to
define
And how do you define the operation
See the operation is defined by the
stride and the input is input is
uh now what do you call blown up by
padding
But if you want to define the weights
now you should know how many matrices I
have to define now In the in one
filter I have defined three matrices
Why is this three three this three
coming This three is coming from the
number of
channels that are there in the input
image Okay Now therefore we have to
specify the number of input channels
Okay
Now therefore youre specifying the
input channel
Now output channel is six Now output
channel is nothing but the number of
filters
Now kernel size is five Okay Youre
specifying the kernel size
Okay
So now as of now you have specified
these two
Okay And stride and padding you havent
specified Now as I told you if stride
is not specified it is considered as
one Padding is not specified it is
considered as zero
Now this is the first
convolutional operation
After that youre passing it through
NNrelu
Then an average pooling
NNaveragepool2d
Okay this is the 2D average pooling
Kernel size is two stride is two
See the standard LeNet actually uses
sigmoid
Thats fine So we know we have
passed a sigmoid and then now we know
that ReLU gives a a better
values Better it is good in case of
empirically we know that it is good for
the sake of images Okay And then you
have this
average 2D
kernel where in which youre specifying
it like this Okay And then we have
another convolution layer and then with
six is the input channel Now and then
please remember this output should
match the input Now because now this
is one pipeline
Okay One is
another
Okay And then the output channel is
16
Kernel size is five
So so we know this And then now this
is followed by
again an average pooling
Now the output size here is 16 4 4
And then this 16 4 4 you have to
flatten it out
Now that is the reason why you have
NNflatten Now we know in how
NNflatten work The raster scan
And then 16 4 4 to 120
ReLU 120 to 84 ReLU 84 to number of
classes which is 10
Now this we know Now this is similar
to defining any standard MLP
So this is what is important
Okay Now input channels
to say that how many components should
be there in each filter
Number of filters
Now what should be the kernel size
What should be the size of What is the
spatial extent of each of the filter
Now striding and pad also you can
specify if you need
And then followed by an activation
followed by a pooling layer
followed by
convolution And then as I told you
this output channel should match this
output channel Now because your
average pooling is not changing here
uh what do you call number of
components Its changing the spatial
dimension of each component The number
of components still remains the same
So and then the input same So the the
same story continues Now you can pitch
in any much how much ever kinds of
convolution layers that you want To an
extent Ill tell you there is a small
caveat over there
Okay
And then you write the the forward
method
Now first you get an input First you
get the features
That means that this is passing it
through
this particular code
And then whatever is output that
youre passing it through the
classifier This is the classifier head
And this is the feature extractor
Okay
Uh
You create an instance of the model
Use the cross entropy loss
because since we are dealing with a
classification problem And then the
optimizer youre using Adam
And then train epoch and all those
things exactly the same story that we
did in our earlier tutorial
Then you run it for some time
Okay Now as you can see now the only
thing that is changing is the model
Every other story remains the same The
training and everything Okay Now
lets run this and see how the output
comes
It is taking some time to
create an instance Now meanwhile
lets look at another
important network which is AlexNet
So to understand AlexNet we should
understand a very important data set
which is known as the ImageNet
Okay Now this ImageNet is a thousand
class uh
problem Okay Lets
ImageNet Okay
So the ImageNet is a
1K classification That means that you
have 1K classes
Okay So now what they did was they came
up with an competition for this saying
that
now whichever uh
we will give you the training data and
then we withheld the test data So and
then you have to give your model We
will run the test data Whoever gets the
highest accuracy that is considered as
the winner Okay Now one of such
winners is actually known as AlexNet
Okay Now the size of each image in this
ImageNet is
224 224 3 It is resized to this That
is the reason most of our input for let
it be AlexNet and the next network that
well be looking at is another network
called as VGG or the next network that
well be looking which is another
network called as ResNet Now all of
them has this
structure which is the input 224 224
cross 3 which is because of it has come
from the ImageNet family of
development
So that you pass through a convolution
layer which is 11 cross 11 kernel
Stride is four Number of filters is 96
Theres no padding And then you pass
through the
ReLU activation And then you see here
its not always mandatory that you
should have two cross two kernels for
pooling
Here you have a three cross three kernel
and then the stride is two
We use the same formula now which is H
in minus F plus 2P divided by S plus 1
to compute the thing Okay
So on and so forth Now you can see here
that uh how it is going ahead
Okay And then we know the idea of
dropout Okay
So in a network now randomly you make
50 percent This is 0 point 5 Now randomly you make
50 percent of the weights as zero
Okay And we know that any kind of
restriction on the weight can be thought
of as a regularizer And this is a
regularizer that is there to avoid the
idea the the problem of overfitting
Okay
Now this is the AlexNet
And then as you can see here
the output will be a
uh
its a vector of 1000 values Its a
probability vector of 1000 values
Okay
After passing it through a softmax
Normally we dont use the softmax We
normally get the logits
Okay And then
uh the the loss will take care of
converting that to the softmax
Okay Now this is the whole story of
AlexNet
So Ill leave this as an exercise Uh so
since youre able to
understand and implement LeNet now it
is just an extension of it The AlexNet
where which you have
uh much more number of layers But one
thing is getting an ImageNet and running
it is a bit difficult So you can take a
224 224 cross 3 random uh the matrix and
see whether the matrix
uh operations that are there
uh here is actually matching the size
Okay So you get the output
So lets see the output of our LeNet
Uh yeah it has done
See we got 97
 95
as the train accuracy and 97 point 94 as the
test accuracy
So within the
five epochs that we have done
Okay
Now this is how you come up with
the
any CNN architecture
So now
uh in the next tutorial now what we will
do is now we will look at couple of
important architectures like VGG
and ResNet
And how do you implement them Take the
pre trained values
So for a 1000 class problem if youre
not dealing with a 1000 class problem
how do you change it for how many number
of classes you have
And then how do you go ahead with the
idea of
feature extraction in these
larger networks And then
the idea of normalization we will look
at in the next part of the tutorial
Thank you I hope you learned CNNs
Thank you
