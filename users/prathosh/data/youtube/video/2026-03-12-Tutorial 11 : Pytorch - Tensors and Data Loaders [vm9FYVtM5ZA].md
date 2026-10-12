---
id: vm9FYVtM5ZA
title: Tutorial 11 : Pytorch - Tensors and Data Loaders
url: https://www.youtube.com/watch?v=vm9FYVtM5ZA
date: '2026-03-12'
duration: 45:18
model: youtube-captions (en-orig)
transcript: true
---

## Transcript

Hello all welcome to this series of
tutorials in which we will be
understanding and learning how to code
using PyTorch
The series of this tutorials the aim is
to come up with the codes starting from
creating the basic tensors till running
CNNs and RNNs and extending it further
to the idea of transformers
Now lets start taking simple steps and
then lets start understanding the need
of PyTorch
PyTorch is one of the libraries that is
helping us enabling us to write codes
for machine learning applications
Now there are multiple such uh packages
like PyTorch TensorFlow and MX Next but
PyTorch is more famous now because it is
more Python like and then uh it is easy
and intuitive for us to work with It
resembles Python in most of its working
and in its syntax Now so that someone
who is very well equipped with the
programming in Python will not see much
of a difference saying that okay no this
is something new that is happening
Okay So now
we all by now know that
the major uh difference okay now that is
needed for machine learning is the huge
scale of data and then the operation
that is repetitively performed is matrix
multiplications
So now CPU is not suitable for this We
have GPUs which are specialized uh
units graphical processing units now
which are designed to perform these
matrix multiplication parallelly so that
with smaller coursees so that
effectively we are able to go ahead and
perform this operation in a smaller
amount of time So you might have all of
you know a company called Nvidia now
which on the day of this recording uh is
having the huge uh stock around uh their
uh valuation is around 5 trillion
Okay Now that is the
level in which and everybody needs it
Okay So now there is a very famous joke
that goes like when everybody is digging
now you start selling shovels Okay It
is like that when whoever wants to do
this
machine learning So the basic need is
this GPUs and then these GPUs So you
want to perform any operations on these
auxiliarators Okay Now we need uh
PyTorch like packages which enables us
to do the first component now which is
there here is what is known as tensors
Now
now these tensors are similar to the
numpais uh uh ND arrays So you would
have used numpais nd arrays Now it is
similar to that Now but the difference
is now tensors are equipped with
functionalities Now venovage the
operations can be done on hardware
accelerators and then a very interesting
uh and the the important workhorse of
machine learning now which is the idea
of back propagation now can be done
using what is known as automatic
differentiation autograd
which is there which we shall look it up
sometime in our due time So that is
there Okay this enables us to do So
now how do you create these tensors and
how do we work with them So lets start
with that Okay now we need the uh
package torch This is the the base uh
uh package that is there and then so we
will see how to create these tensors
first from a regular uh list which we
have and then a numpy array that we have
and then how do you interchange between
them Now we will see therefore for that
reason Ill import numpy also

So now what we will have is
now lets say that I have a data x okay
now which is uh 1a 2 comma
3a 4
okay now then uh you can
know the type of this
print type of X
Now we can see that this will be a list
Okay
So now how do you convert this list
which is there into a tensor Now
X tensor equals to torch dot
tensor of X
Here you can
print
extensor
print
type of this
extensor which is there Now you can see
that this is not a list anymore You
have converted this into a tensor Okay
And then even the type is indicating the
same thing Okay So now you have a
tensor which you have obtained from the
uh list Now similarly we can obtain it
from the numpy array as well So now
what Ill do is uh so Ill first convert
this list which is there to numpy Now
how do I do it Now np dot array of x
Okay So now you can uh print this
X NP and then type of this Okay this
is a numpy array that we have the X NP
Now how do you convert it from
numpy array to tensor Okay extensor
from numpy Okay Now this is uh
no
torch dot
from
numpy
Okay
So you just have this
Okay So now if you have the data that
you have in the form of a list that also
you can convert or if you have the data
in the form of your numpy array that
also uh you can convert Now by now all
of us know that any uh data that we look
into either its a matrix or uh a
sequence now now that is uh nothing but
uh vectors its its in some RD okay
its a vector in RD okay now this is how
we create uh tensors now there are uh
now sometimes we might need to have no
tensors now which uh which is of certain
properties which is of certain shape now
which is having uh same elements okay
something like that if we want to do
that now lets create what is known as a
tensor now where in which all the
elements are one and it is resembling
the properties of x which is there okay
the tensor x which is there now how do I
do it
torch dot
once like okay Now you have X tensor
You can print this X once Okay
this is of the same size as that of the
or same shape that as the X tensor which
you have but everything is one Now if
you dont want all ones if you want a
random tensor which is of the same shape
of the X data now we can always create
it Now
torch dot
rand like
okay now extensor I want it to be in
float values So that I use to doflat
float to indicate that I want it to be
now this is a random tensor now which is
of all the elements are floating values
and then this is of the shape x tensor
okay so I assume that these are clear
now this is youre saying that youre
giving a data and then youre saying
that like this you create now I dont
give the data I just give you the shape
Is it also possible Now yes it is
possible You can provide the shape Now
lets say that the shape is 2a 3 Okay
just need to include the other comma
here Now you can have
rand tensor Okay random tensor now
which is
okay
torch dot
rand of
shape Okay So and then you can have uh
all ones Okay
one tensor is uh
torch dot
ones of
shape
or you can have all zeros Okay Zeros
uh
tensor is uh
torch dot
zeros
shape Okay Now we can print all of
these Okay
print uh
use formatting uh random tensor
once and then this zero tensor
there has to be a
okay now you can see this this is a
random tensor which is of shape 2 plus 3
and all ones and all zeros now we can
obtain tensors like this Okay Now this
you can give it for uh any uh RD you can
obtain you can for any grid that you
want to do You can provide the shape
and then obtain it for that particular
grid structure Now thats thats
totally fine Im just showing you as a
simple example for 2 plus 3 Okay So now
what are the attributes of tensors
Lets look at them
Attributes of tensors Okay Now

couple of uh important attributes of
tensors are what are the data type of
the tensor and uh on what device it is
there and uh what is the uh what data
type device and then what is the shape
okay shape of the tensor Now these are
some of the very key attributes that we
might be checking uh again and again
whenever uh
the need arises Okay So now lets
create a
tensor Okay So now lets say that I
have
z tensor equals
tors dot
rand I can just provide 3a 4 the shape
here itself So now I can uh print these
properties these attributes shape of the
tensor
shape of tensor
data type of this tensor
Okay So and then on what device it is
there
How do we do it If uh no
device sensor is no on what device it is
there that you can uh use obtain it by
using dot shape dtype and device Okay
Now the shape is 3a 4 All these are
32 bit floating uh values and then
currently it is on CPU because I havent
enabled the GPU access yet We will when
we create the model structures all these
MLPS and structures at that time I will
show you how to port it onto a GPU Now
I have create I have just used the CPU
so it is showing that it is on the the
CPU Okay Now these are some of the
very important attributes and then
please remember whenever you want to
perform an operation on a tensor Now
both the operants or the involved
operants should be on the same device
Okay Now either it is CPU or GPU No
it has to be on the same device
otherwise uh it is not possible to
perform the operations Okay So now
lets Okay Now since we have lets look
at uh
operations of uh operations on tensors
See there are uh a lot of operations now
including arithmetic operations linear
algebra operations matrix uh
manipulation operations
There are lot of options Now there is a
rough estimate there is more than
thousands of operations that are there
Now all these operations can run on CPU
as well as uh on the CUDA device Now
thats what you would have uh you should
remember sir saying about uh CUDA Okay
So on all these accelerator device now
they can uh run Okay Now by default
whenever a tensor is being created it is
as I told it will be created on the CPU
Now then you have to explicitly move it
to the GPU for its working Okay only
when the koda device is available Now
lets look at some of the very bare
minimum operations now that now we can
do okay now these operations see now for
all practical purposes whatever
operations that you can do on numpy
indorses
okay so now lets look at some of the
indexing and slicing those are the basic
operations that we can think of now
lets uh do them okay so now now I have
already have this z tensor Ill just use
the same which is size 3 plus 4 No let me
print it so that we can understand the
output Print
Z tensor
Okay this is the thing Now lets say
that I want to access the first row Uh
now print
I want to access the first row
Now how do I get it
See you know things are evolved It
knows the basic kinds of operations that
first row first column and then you want
to access the lets say that last
column Okay Now or you want to
manipulate uh the columns here Okay
The first uh uh so this is actually the
column with index one which is the
second column actually Now lets do it
Now here you can see that this is the
the first row Okay Now and then the
first column 0 6244 This this is the
first column Now youre able to access
it The last column is this And then
you have modified
column with this is this is the index
one I have modified it to zero like
this These are the basic operations
indexing and slicing operations that uh
we are comfortable in performing numpy
array and those things can be performed
Now here also and uh and one other
operation that might be interesting is
uh this concatenation of uh tensors
Okay So now lets do that uh lets say
that uh
see concat Now whenever I say concat
now whether are you doing as per the
rows or as per the columns Okay So now
lets do that Now lets first do as per
the columns Okay
Now you have this Z tensor that youre
placing next to one another Now because
of which you are concatenating as per
the columns Now to indicate that you
have to specify dimension as one Now
that is when you are uh
doing as per the columns Now as you can
see here now this is a 3 plus 4 Now it has
become now the 3 plus 12 Okay the four
repeated thrice Okay it has become 12
Okay now this is along the columns you
have concatenated Now similarly along
the row also you can concatenate
Now you concatenate along the rows Now
these things have become
you you say in one line it will
understand what is the next operation
that the next word prediction that we
shall be seeing sometime in our course
See you can see that in work
this is along the rows Now you can see
the concatenation Okay Now this is
regarding the concatenation operation
Now lets uh look at the crux now which
is uh the arithmetic operations Now now
these are matrices and then now we know
that the basic operations that we want
to actually perform are matrix
multiplication and then element wise
multiplication Now these are the basic
operations that we want to perform
Okay Now lets look at them Now lets
do matrix multiplication
Okay Now uh see I Im assuming that all
of you know the basic rule of uh matrix
multiplication
Okay So Im assuming that you know it
and then Im proceeding with that Now
lets say that I have y1 Im multiplying
that with z tensor Now this is the
matrix multiplication operation symbol
that is there and then Z dot T Now it
is transposed Now what is the shape of
this Z tensor Now this is a 3 plus 4
correct So now you have this which is a
3 plus 4 that you are performing a matrix
multiplication with the transpose of it
Now which will become 4 plus 3 Now we all
know that whenever these two are
matching you can perform Now the
outcome now will be a matrix now which
is 3 plus 3 Okay Now these sanity checks
needs to be done whenever you are going
ahead and performing the the operations
on matrices Okay Now the sanity check
of uh uh the matching of the shapes
needs to be looked into Okay So now
now what are the different way This is
one way of doing it The second way is
now you use the tensor and then you call
a method now which is dot matl and then
you pass the the second uh tensor there
Okay
Now this is the
another way of doing it And the third
way of uh doing it is uh you create a
placeholder
now which is uh it should not be of type
y1 now it it has uh yeah it has to be of
type y1 you because y1 is the product
So it is you create a placeholder for
this and then you pass the both the
operants Okay So z tensor and then
where do you store the output The
output is stored in this Y3 Okay
Now tarmmatill this you can use or you
can directly use the matrix
multiplication method which is there
with this uh
instance of uh uh tensor which is there
or you can use this at operator which is
there These are the three different
methods that you can use and then all of
all of these three should yield to the
same result for sure But these are the
three different methods that you can
use Okay this is matrix
multiplication All of them are yielding
3 plus 3 things And uh the other thing
that we have is element wise
multiplication See element wise
multiplication
is its something like this
Now all of you are comfortable with the
hadamar product know which is preferably
working with
uh vectors Now lets say that I have uh
two matrices and then they have to be of
of the same shape Okay So now
we represent this matrix uh element wise
matrix element wise multiplication by
this asterric lets say that two 2
okay now the outcome will be you take
this and you multiply by this okay this
is two similarly four 6 and 8
this is you take this element multiply
with this element you get this okay this
is element wise multiplication this This
is another operation which is needed
Now remember now whenever in CNN I
assume that all of you have seen the CNN
now you have to perform this element
wise multiplication then finally add no
okay remember that operation something
similar to that okay so now lets look
that this element wise multiplication
okay so lets say that
have uh
Okay t1
equals this or you can use uh dot null
Okay
so or you can use uh
uh so you create t3 which is of the
shape of t1 and then similar to the
torch domatill you can use this and then
you can print all of them together
Okay
Now this is uh the the element wise
multiplication
which is there Now these are uh uh uh
some of the operations and uh other uh
uh
single element tensors uh is like for
example lets take this uh
z tensor dots sum okay
So
let us see this output and then see
here Now this is dot sum is youre
adding all the contents of the Z tensor
Now dot item Now what it will do is now
see now this is a tensor Now as you can
see that this is a tensor Okay And
lets print this
 AG and then type of this
AG
This is a tensor Okay torch tensor
Now dot item is used to uh port it onto
the the CPU It it is it is uh uh trying
to convert it into a Python numerical
value Okay this will be a tensor
of uh its a 1 plus 1 tensor so that you
are converting into a python value so
you can perform this sum so now I
presume that you can look into the
convolution operation now as combination
of these two things now similarly you
can add a scalar okay so now that is
also possible now that is I can say that
Z
tensor
dot
add
lets say that I want to add three
okay then
print
Z tensor
you have added three to each of the
elements okay and these are some of the
basic operations that you can think of
and then uh you can uh work in using
these tensors Okay Now I assume that
these are clear So now the next uh
thing that we should look into is okay
now these are fine Now the next
important question that arises is okay
now these are tensors all my input uh
will be tensors
Now from where do I get the input
Okay Now you need uh for any supervised
learning task Now you should be aware
by now that now we need features and
then labels and targets Okay Features
labels and targets You you actually
need them Okay Now how do you obtain
these data Okay
Uh that might be in the form of an image
or in in whatever format it is Now how
do you know get them Okay now this is
for that we have libraries uh uh like
data sets and data loaders Now we will
use them See whenever we are dealing
with uh data no now some of the
academically available data sets are
there in the PyTorch library itself So
you can we can go to Google and then you
can check for uh
so PyTorch
data sets
if you go to this tution data sets
sometimes it takes time to open Now all
the basic uh
academically needed data sets okay are
present there like mnest uh there is one
more data set called as fashion nest
which is also a 10 class problem okay
and then you have calte flowers now
during our uh discussion we shall be
using these things okay now you can
actually obtain those data sets directly
without any much of hassles But most of
the commercial applications the data may
not be publicly available Okay Now
whenever data is not publicly available
now we need to actually load these data
now physically Okay Now these are two
different one is academically available
datas is readily available Okay Now
the second one is now commercially
needed uh data now it is for the for any
given company needs to be loaded uh uh
right uh explicitly Now how do we do
this is the is the next question Okay
So now first lets look at the
commercially
uh available data So now we will be
taking uh here the famous uh MNEST data
set Okay Well be looking at the MNEST
data set
Okay Now
now we need to import torch that is like
the vanilla thing that is needed Okay
And then we need uh
from
torch dot
utils dot
data
import
data set
from torch vision Import data sets to
tensor
mattplot lib Okay Now these are the
things that are needed So now now
lets do this Now
now these standard academically uh avail
academically
compatible data sets they have their
training and test split now which is
actually done Okay You dont need to
actually perform the train and test
split Okay Now if it is not now we
have to randomly perform a train and
test split But for MNEST the train and
test split is uh there Now if we need
uh validation uh set to take care to
take care of hyperparameter tuning Now
normally the prescribed uh way is now
you take some from the training data
set Okay that is the prescribed way
Okay Now lets look at the training
Okay training data
Now where is this Now it is there in
data setsmst Now it is there before I
think it got loaded Now you can see
that these are the different
image classification data sets Now here
1 point 1 means there are 1 point 1 classes Okay
Here 256 means 256 classes 10 100
you can see this is fashion mnest
food 101 So there are a lot of these
data sets that are there Now this is
for uh uh what do you call uh
classification and detection and
segmentation also you have optical flow
Now you have lot of uh uh different
tasks for which the data sets are
readily available in the repository
which we can take and start working
Okay fine So we will not be going into
that Okay These are the different
things that are available But first
lets uh load the mnest Okay So now
you can directly load it from this data
sets Thats the reason why we use
vision Okay Now I need this mnest
Okay So now
now this
now now if you want to uh work on this
now that has to be physically present on
your device Now in this case Google
collab it has to be present uh in your
current working environment Now where
it will be now it will be downloaded if
it is not there to this folder from the
current running directory data Okay
And train is equal to true indicate that
you are loading youre downloading the
training data As I told you the train
and test split is there Now download is
equal to true That means that in the
given path if the data is not there you
download it And then
what do you do you convert it into
tensor Now why we have to convert it
into tensor Now because these are numpy
images that you have to convert it to
tensor Now these are known as
transformations Okay So now see you
have you have your features as well as
your labels Okay Now here Im only
giving the the feature transformations
Now sometimes you might even need to do
a target transformation also Okay Now
just keep in mind now that okay in most
of our cases we might not be needing it
but that is also there you might need to
transform the uh the targets as well but
as of now we are just converting uh the
numpy images the numpy arrays which are
there into tensors Now that is the
reason why Im using this two tensor
This is the transformation that Im
applying Okay Now this is for the
training data and similarly for the
test Okay
Test data Uh okay It itself will take
this is
now you have to uh so look out for that
in this data from the current working
directory and then train is false Now
that means that you are actually uh
downloading or youre dealing with the
test data Download is equal to true
That means that in the given path if it
is not there you download it and then
transform Now whatever data is there
you transform it Now as you can see
this is my current uh uh directory in
which Im running on the collab Now I
dont have any data Now once I run it
okay
it will take some time to load
Okay
Now
can see here the data is there Mnest
raw
Okay Youll see all this This is in
some
Okay
its not opening But anyhow you have
these uh files ready for you to work
with them Okay now the data
uh is ready Okay Now this is when we
have comfortably now having the
uh the data set in the uh PyTorch
repository Now what if that is not the
case Okay Now what if that is not the
case Now then we have to actually build
a custom data set Okay Now the need uh
now what is needed for this customuh
data set is one thing a file uh where in
which you have the path to the image and
then the corresponding label Okay that
is one thing and then a folder in which
all these images are there Okay even
if they are uh what do you call spread
across now in the file you should have
the proper uh uh namings done Okay So
now now lets do it Now lets create a
custom data set Ill just show you how
to create a custom uh uh image data set
class Okay So and then if you have any
custom data set you can use a similar
approach and then you can do it And one
other approach that people actually have
is now they will segregate uh the data
Uh there there is folder one folder two
for each of these different classes Now
then loading will be even much more
simpler Now I leave it as a small task
for all of you If the data is like that
now how do you do it Now here what is
my assumption is there is a folder in
which every image is there and then
there is an annotation file in which the
relative path uh the relative path and
then the label is there Now how do you
work in those cases is the criteria in
which Ill be taking Okay But if it is
neatly arranged in cases like okay each
class is segregated in folders then how
do you do it now we use what is known as
image folder Ill leave it up to you
with this much of two okay so now to
create this now import
OS now you need to uh go around uh the
directories for which you need this and
then uh since we are uh dealing with an
annotation file which is a CSV file now
we need pandas as
we using pandas as pd and then uh
from
from torchvisionio Evo Now you have to
uh read this Now import
decode
image See Im Im assuming that we are
working with images Okay The same idea
can be extended whenever you are dealing
with sequences also But remember
whenever you are dealing with sequences
what should be the length that should be
taken is the one that needs to be
considered Okay Ill not be going
ahead with that Now we are as of now
taking the
uh the images Okay So now class
custom
image data set and it has to be
inheriting uh the data set which is
there and then uh lets have the init
method
Okay And this uh now we should have
self annotation file image directory
uh transform none and target now this is
okay now annotation file is the file
that I told you its a CSV file now in
which uh CSV or TSV anything uh uh file
now in which
uh you have the relative paths and then
the uh the labels that are there and
image directory is uh the absolute path
till that point Okay Now annotation
path is from that file It is relative
where where are the existing Now image
directory should be the absolute path
from the root or whatever you have till
that point Now transform is on the
features Now what are the feature
transformations that you want to do it
on features and target transformation is
what are the features that you what are
the transformations that you want to do
it on target Okay
Now this needs to be considered Now
then uh
self dot uh
image labels
now equals PD dot
read CSV Im assuming that this is a CSV
if not please uh
make the changes now image directory is
this self dot
transform
equal transform and you get the target
transform and then now we need to have
this length Okay Now now why is this
needed Now you remember that uh so we
have to cut them into batches Now for
that we should have this leen exactly uh
the same name but depending on the kind
of file or the kind of uh uh structure
that you have the return value might
change okay but en
has to be retained the way the name it
is Okay So
now you should have this length and then
you should have the get item Now the
get item is where in which every time uh
now you you will be getting one image uh
one feature one features and then its
corresponding uh target or the label
Okay So one one at a time So now image
path first you should get the absolute
path to a given image Now how do you
get it You have the absolute path till
the directory and then in the annotation
file you have from the directory to the
file to the the file So now what you
have to do you have to join them Okay
So now how do I do it OS dot path dot
join Okay Uh so image directory and
then that is the the first column Okay
And then you decode its path and get the
image Okay Now whatever ID that you
are getting now that row zeroth column
so youll have two columns in your CSV
The first column will be your uh
relative path and the second column will
be your annotation So youre obtaining
the whatever ID that you are getting the
zerooth uh column the value in the
zeroth column of it So now and then
what is the label The label is the
first column Correct So the label
which is there and then now if you if
there are any transforms now you will
apply if selft transform you will
apply Okay
Now if you have any target
transformations okay that on the label
youll apply the target transformation
and then you return
you return image and label okay and
please remember this leen and then get
item the names has to be retained no as
it is Its not like uh no you can
modify them Okay
Now this is how you create a custom
image So now lets now since I have
this data now lets print one one of
these data and see okay how it looks
like Lets do it here itself
So now I can get the
train features train label
Okay
Now this is 12828
Now the image the mnest image size is 28
 plus 28 Oh that is fine Its a torch
Its a tensor Now actually my aim is
to
print it Okay
Train
features
train labels Now use the iterators So
next of
it year of
training data Okay So and then
the the image that we are considering
will be
the zerooth one and squeeze and then the
label and then you plot it pltho
and you get it What happened
Int object is not subscriptable
Okay
Okay Okay Okay Okay
Okay Lets do this rather than working
with this Let me see whether Im able
to plot this first Okay This is the uh
image that we have This is a five
Okay you can off the grid and do those
things So I Ill not be
going ahead with that So this is how
you can plot a single image and convince
yourself that okay now these are the
images Okay So now uh uh at this point
we stop this section of tutorial So in
the next section of this PyTorch
explorations now well be looking at how
do you create
uh a neural network Okay well be
first creating an MLP and then well be
uh looking at the automatic
differentiation and optimizations Okay
thank you all I hope you enjoyed this
session Well meet in the next
tutorials looking at a very important
idea of building the neural network
Thank you
