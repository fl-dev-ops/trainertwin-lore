---
id: oTEPAiwv-00
title: Tutorial 10 Part A : Numerical Example on Bayes Classifier
url: https://www.youtube.com/watch?v=oTEPAiwv-00
date: '2026-02-18'
duration: 51:37
model: youtube-captions (en-orig)
transcript: true
---

# Tutorial 10 Part A : Numerical Example on Bayes Classifier

## Transcript


Hello all
Welcome to this tutorial
in which
we will be completing one derivation
that was left in our discussion in the
class which is for ordinary least
square
And then we will be solving couple of
numerical problems from MLE estimate
MAP estimate
That is the agenda for this particular
tutorial Without any further delay
lets jump in
So
uh
we are looking at the ordinary least
square solution
Now
now here
the idea is our
function that we have the actual
function that we have is
theta transpose X Im considering here
an augmented data Now when I mean by
augmented data that means that if data
belongs to RD I have increased it by
one dimension by putting one there And
then in theta I have put the bias
So now X belongs to
R D plus 1
and theta
belongs to
R D plus 1 This is one instance of X
So now if I have n examples
my overall X that is there
now will be
the first
example
the second example
so on like
Xn
Okay
Now I have n rows
I have D plus 1 columns So now my X
matrix which is there
is n cross D plus 1 and the Y that I have
Y1
Y2
so on till
Yn
which is
n cross one
Okay Now Im assuming that the output
is a scalar
So now
when I go ahead and assume that so we
are
looking at
ERM with
with linear model
and
squared error loss
This is the
consideration Then the overall problem
of obtaining the parameter optimal
parameters theta star is
argmin of
theta
1 over n
X theta
 minus Y
the second norm of it
Okay Now this is the whole thing
So Im considering all the data points
together
Therefore Im not considering this I is
equal to 1 to n since Im considering
all the points The output of this will
be a vector This is a vector So you
can uh
take each one of them and then if you
take it it will finally boils down to
the same equation that we had earlier
So now now we can
uh
take this and expand So I just want to
know when I have this
second norm
as Y
transpose
Okay Now this is
nothing but this
Okay
So now this will be
X theta
transpose
X theta
transpose Y
Y transpose
X theta
 plus
Y transpose
Y
Now lets
look at this
Now this should be a scalar
Okay This is a vector
Now this is a dot product
So this is a scalar
Vector transpose
into
a vector This is dot dot product again
Again this is dot This is dot product
Now all of them are
scalars
Okay Now therefore the overall
outcome
will be a scalar
Okay So now this will be
this I can
write it as
Y transpose Y plus
X theta
transpose
theta minus 2 into
theta transpose
X transpose Y
Okay
Now these are same actually so
twice of that you can do it Now this
is your
equation So now how do you find the
argmin Now the idea is quite simple
Now you just differentiate with respect
to theta
Okay Now again this is a scalar and
theta is a
is a vector
Okay Now you are taking the partial
derivative of a scalar
Okay The final outcome will be a scalar
is what I mean by that with respect to
a vector Okay So now now now it will
be
Now I have to take the partial
derivative with respect to
This is independent of theta Now
therefore this will be zero
So now
taking the partial derivative with
respect to
2 theta transpose
X transpose
Y Now this will be
2 into X transpose Y
Okay
So now
again we need to take a
dot product between
two
into
X transpose
Oh sorry for that
Now this is
theta
transpose X transpose X theta
I want to take the partial derivative of
this Then this will be 2 into X
transpose X theta
So now now whenever youre taking a
gradient now the gradient will also be
of the same dimension as that of theta
Now what is the dimension
Oh sorry for that So yeah
Uh this is correct Sorry It will be of
the same dimension as that of theta So
now this is a
D cross 1 into D cross 1 matrix that
youre multiplying it by D cross 1 So
therefore this whole thing will be a D
cross 1 The same thing will apply for
this
Okay Now this is
D cross 1 into n that youre multiplying
by a vector of
n So n cross 1 to be more specific
So you get Sorry D plus 1 cross 1
Okay D plus 1 cross 1 you will get it
which is as the same dimension as that
of the theta
Okay So now
now
just put all of them together
Now therefore you differentiate with
respect to theta and equate it to zero

 Now differentiate
with respect to theta
and
and equating to
zero
we will get minus
2 X transpose
Y
 plus
2 into X transpose X theta Now this
implies
X transpose X theta equals X transpose
Y Now assuming that
Now this is a matrix
Okay Now assuming that the inverse
exists theta equals
X transpose X
whole inverse
X transpose Y This is the
optimal value of theta
Now
I will
leave couple of things here Now one is
Now what if there is no inverse Now
then comes the idea of pseudo inverse
Im leaving that for you to look into
So that is
one specific thing And then the way in
which we proceed in obtaining the act
optimal value for theta star now will
be same for even for generalized least
square solution Okay Now there what
will happen is you have to take it into
the consideration of the trans in the
transformed space Okay Youre not
dealing here in the transformed space
Okay Now there you have to deal with
the transformed space but the overall
idea will be similar
Okay

 Now this is Now with respect to the
ordinary least square solution Okay
Now this is much
If you have studied linear algebra as a
course I would have seen similar kind
of uh
what do you call solutions Okay
So they
So
So lets go to the next
problem Now the plan is well be
solving couple of problems uh on
uh the risk
and then on the
uh
MLE estimate and then on the map
estimate Okay Uh these problems are
uh the credits should go to Professor
PS Sastri sir
Okay in while he was teaching uh
the course in uh our institute Now
these questions were curated Im using
couple of questions from them So there
is it has nothing to do with these
numbers So these numbers are
just some numbering that was there
earlier Okay Im just uh reusing these
questions
So this this uh
the main idea of all these questions is
to give you
uh an intuitive feel of how things work
Given a problem how do you go and work
Okay So now lets take a
So we are saying that getting the two
class uh pattern recognition problem
Now two class classification problem
with feature vectors in R2 Now that
means that you have your points in R2
Okay So now we can easily plot R2 So
now lets plot them
first
Okay
So now uh is
the question then says that the class
conditional densities of class one is
uniform over 1 3 Now now this is
this is
X1
This is
X2

 Now
when hes saying that it is over 1 3
so now it is lets point them up
This is 1 2
3 4
5 6 7
3 4 5
6
Okay
So now over 1 3
what is this is
1 1 3
Okay
This is
one class Okay
The points are uniform from this
This is class one
Okay
Now the class conditional for class one
is uniform over 1 3 and for the class
two it is uniform over 2 4
Okay So then for the another class it
is uniform over
2 4
Okay
This is the second class
So now
Suppose the prior probabilities are
equal
and youre using 0 1 loss Now we have
seen all these things Now consider the
line X plus Y equals 0 Okay So lets
consider that line
X plus Y equals 0 So X is 0 which makes
Now this makes Y is 0
This is 5 5
Now line joining these two points
is the one that
So the
Okay Now this is the
the line
This is the line
X plus Y
 equals 5 or X X1 Okay better way of saying
this
is so
X1 plus
X2 equals 5 Okay the reason why Im not
using Y is in our connotations normally
we have Y as the label Okay So
therefore Im not using it So
Suppose we consider X plus Y in R2 is this
a base classifier for this problem
And then hes saying that is the base
classifier unique for this problem If
not can we specify two different base
classifiers
Okay
So this is the first part and then we
will change the class conditional
densities and then we will go ahead
Now well come back to that the
remaining part of the question So now
lets uh
resolve lets look at this problem So
I assume that all of you are clear with
this representation Now your class one
is from this
Your class two is from this You have an
overlap Now that is there And then
this is the line that youre saying
Now what do you mean by that Anything
above this
belongs to class two anything below
this belongs to class one Okay
So now that is the idea
So now lets
uh
put things up
Now the probability the priors Y equals 1
equals
Y equals 2
is half
Okay
And then we are using
0 1 loss Now what do you
What do you mean by that Whenever the
classification is proper
uh so the loss incurred is zero and
whenever theres a misclassification
the incurred
uh loss is one Okay So now
Now we know that
So whenever you have a base classifier
with 0 1 loss okay Now
whenever you have a classifier with uh 0
1 loss and then youre considering the
base classifier so now it will boil
down to
comparing the posteriors Okay Now
whichever posterior is higher you will
be putting into that particular
class Now
base
classifier
with
0 1 loss
so now
is
is comparing posteriors
P of
Y equals I
given X Now this is what youll be
actually comparing
Now how will be the rule The rule will
be
So if
Y equals 2
given X
is greater than
Y equals 1
given X
then
uh
youll be putting youll be labeling
that
particular example
uh youll be having Y equals 2
Now
otherwise
youll be having Y equals 1
This is our
uh
base classifier
Okay So now
and then
then it boils down to Now we know that
Y given X by Bayes rule
now that is X given Y
into probability of Y
divided by probability of
X Okay
Uh
This is that
Okay Since we have equal priors
now
comparison of posteriors can be
uh looked into as comparison of just
class conditionals Okay Since we have
since
since priors are
equal
probability X
Y equals 2
greater than
 equals 1
then you say
Y equals
2
Okay Now this is your uh
classifier
Okay So now
Lets begin
couple of
things Okay
So now we know that
X given Y equals 1
this class conditional is uniform over
the region 1 comma 3
cross
1 comma 3
Okay
Lets call this region as
S1 pertaining to class one
The area of
S1
 equals 4
Okay
So and then how will be our
class conditional density
The one
 equals 1 over 4
for X belongs to
S1
otherwise
Okay
So now whenever the value whenever the
X that youre choosing now here now
please remember that whenever I say X X
is in a point in R2 Okay
Here X belongs to R2
Okay Whenever you choose a point in R2
and then that belongs to this region S1
now then
uh the class conditional density for
that will be 1 4 Now that means that
you choose any
point from this
Okay Now it has a probability X given
Y equals 1
is 1 by 4 and any point apart from that it
will be zero Even outside of this
Okay
So now
Now similarly lets look at for the
other class also
Now
probability that X given
Y equals 2
is
uniform
2 comma 4
over the region 2 comma 4 2 comma 4
Okay
Now lets uh
call this region as uh
S2
and uh
we know that the area of S2
is four
Okay
So and then probability that X given Y
is equal to 2 for any given X
Let us specify here X See Im sorry
Im abusing a lot of notations Now
I assume that all of you are able to
recognize these abuses
Okay This is 1 by 4
for X belongs to S2
Zero
otherwise
Okay
Uh Im just uh
thinking of a joke See
now uh
I was a TA for uh
when uh
probability course was happening in
institute I was a TA And then for
these kinds of abuses I have actually
cut marks for people And there might be
some people who might be looking at this
and then hes saying that what is
happening Okay

 But yeah Im assuming that all of you
are able to recognize the abuses that we
are doing
Okay So now this is one region S1
This is another region uh S2 that
uh
Im going ahead So and then
there is a region S1 intersection S2
Okay
Now Ill call it as S12
Now which is
23
cross 23
And the
area of this
S3 is one
Now Im speaking of
this
intersection region
which we are looking into
Now here
the area is one
Okay
So now in this particular any point
that belongs to S3 what happens is
probability that X belongs to Y is equal
to one equals probability that X
given Y is equal to two
is 1 by 4 for them
Okay
And then what do you do Now here uh
its a bit of a tricky task Okay So
now lets
Now this we understood
Okay
So now now
Now with all these things in place now
lets proceed
So now the next question that
the next part of the same question that
we are asking is now we are considering
now
consider
X1 plus
X2 equals to five
This is the discriminator that youre
considering Now what do you mean by
that now is
X1 plus X2
if it is less than five
then Im saying that Y is equal to one
If X1 plus X2
is greater than five
then Im saying that Y is equal to two
What is it equal to five We break ties
arbitrarily Okay So
just
break uh
ties arbitrarily
Okay Now that means that
Now whenever any point
Okay That belongs to
S2 which is here
Now Im saying all these points are
belongs to Y is equal to two
And for all these points that are there
Im saying that Y is equal to one This
is what Im saying
Okay This is one region This is
another region now as per the
classifier
Okay
So now now then
now uh
And then what happens now in this case
Now you have to find the risk
Okay
Now if you want to say that whether uh
this is a base classifier or not Now we
have to find the
the risk of this Correct
So now how do you find the risk of
this
Uh the risk of
HB is
you look at all the support
R2 and
min of
probability
Y is equal to one
and conditional
equal to one
So now this I can divide the whole
thing
into multiple regions
Okay
So now
lets say that
I have
Ill have couple of
regions
Region A
Now what is this region A S1 minus S2
Okay
Region
B
That is
S2 minus
S1 Now what is what are these regions
Okay
So now this is
region A
Now when which you are not considering
the common points at all This is region
A
And this is
region B
Okay
So now
any point
So that youre considering
here for any point
that youre considering here okay
Uh for example lets consider this
point
The probability that X given Y is equal
to one will be 1 by 4 Probability that X
given Y is equal to two will be zero for
this
So whenever you take the risk youll
be come come considering this The
minimum of them So you dont need to
worry about this
Okay
And whenever you compare them for
classifying now this is higher youll
be putting it into class one
So now that means that you dont have
any problems with these points being
classified Now these are perfectly
classified points as class one
The same thing holds good even here
These points are perfectly classified as
class two No problem at all
So for points in region A and B
the risk is actually zero
And since all of them have just uh
outside these two regions
the density is zero I dont need to
even consider that So considering the
overall R2 support which is there Okay
So now
I can
divide this this whole thing which is
there
into
region A
Okay
So okay Region A region B and there
is one more season region not season
Region C which is S1 intersection S2
Now this is this common region which is
there
which is 23 This is the region that
Im considering Now this is where
actually the risk needs to be computed
Okay
So now
region A now
plus Okay
change
plus integral with respect to region B
plus
integral with respect to region C
plus
integral outside Now you can
outside Now this is zero zero zero
No need to worry I just need to worry
about this particular thing while
computing the risk
Therefore it is nothing but
2 cross 3
into 2 cross 3 I should be only worried
about this region
And what is the value This is half
This is 1 by 4
For any point which is
in this region
both of them
both the class conditional will have the
valid value 1 by 4 by 4
Okay And therefore the minimum of them
will be 1 by 8
DX
This will be 1 by 8
Now the optimal risk that you are
having
is actually here 1 by 8
Okay Now please look into this I
havent even brought in that line at
all
Okay
So now
now
when we say that something is a base
classifier now we know that base
classifier is the one that gives you
least risk Now Im able to obtain the
risk which is 1 by 8
So now I need to calculate now with
when I have that line what is the risk
involved
Okay
So now that is the next point that is
there Now
with respect to this particular
discriminator line
for this region where in which there
reason is a misclassification that can
happen Now compute the risk
Now
I presume that it is fairly simple
And then you can see that
Okay
Now
It is one over eight
Okay
The main point was computing the risk of
this
And then now it is easy to see that Ill
just make that point
So now
This
Easy to see
That
The risk
Involved
And
When we consider
The points
Of
S1 intersection S2
It will be
One over eight Now how do you compute
it The risk is nothing but
So youre looking at expected loss that
is incurred Now I presume that you will
be able to compute it Now you have the
base risk which is same as
The risk that is
obtained in this particular case
Okay So now now
Now the next question that immediately
arises is now
Is this classifier now the risk is
Same Now is this classifier that I have
This line is this a base classifier
Yes Now because Im able to obtain the
least risk
Okay Now is this the only classifier
Uh which can give me the same risk No
Okay Now I can have a classifier for
all this region in this I can say it is
Y is equal to one
For all the elements that also will give
me the same risk
For all these things in the region now
there is Ill say Y is equal to two
Now in both of the cases
I get the same risk Now therefore same
value for the risk Now therefore it is
evident that
Now it is
Not a unique classifier Okay The
uniqueness is not there
Lets make that point
Is
Now before that
Therefore
X1 plus X2 equals to five
Is a
Base
Classifier
Okay Now the next point is
Is it
A unique
Base classifier That means that do you
have any other base classifier with same
risk
Now no The answer is
No
If I have
Lets say that I have classifier one
Now decide
Y is equal to one
For all X
Belongs to
Region one two
Then also the risk
Involved with this particular classifier
will be one eight
Now
Classifier two now that is
Decide
Y is equal to two
For all X belongs to
The intersection region now then also
Now
It will be the same value for the risk
Now therefore it is evident that now X1
plus X2 is equal to five the line that
we have considered Is
A base classifier but not a unique
base classifier
Okay
So lets go back to the question
Is this a base classifier Yes Is the
base classifier unique for this problem
No
If not specify two different base
classifiers done
Now then we go to the next part Suppose
the class conditional densities are
changed so that the density of class one
Is still uniform one three but for class
two it is two five Okay So now that
means that there is a change now
Now two five we are considering Okay
So now
Okay
Okay So
Now we are comparing
This
These are the two densities that you
have in hand
The orange and pink Okay
So now
Is the line X plus Y a base classifier
Is base classifier No If not specify
the base classifier
Okay Is the base classifier unique now
No if whatever base classifier that you
get is it unique
For the class of class conditionals
suppose
Okay Now we will come there Now lets
find the base classifier for this
Okay
Okay Now this is
I prefer to call it as
Part two of this problem
Okay Now here
The class conditional Y is equal to one
Is
Uniform
One comma three cross
One comma three
And then
Given Y is equal to two
Is uniform
Two comma five
Cross
Two comma five
Okay
So now lets call this now as a
Region one and region two represented by
S1 and S2
Okay So now
Now then what will happen Now please
see that now the area of this Uh region
is nine Okay
Now therefore
X given Y is equal to one
Equals one fourth
When X belongs to
Region one zero
Otherwise
Okay
And then
The class conditional for another class
Y is equal to two
Equals
One over nine for X belongs to region
two
Zero
Otherwise
Okay
Now again now
S1 intersection S2
Is
Again the same region
Two cross three cross
Two cross three
Okay
So now in this case
Now what is the question
So now whenever youre using the same
line now
For anything
Here
You decide
Y is equal to two No problem now
Okay
For anything here
You decide Y is equal to one No problem
now because the other class conditional
will be zero
Now the only issue that arises is in
this intersection region where in which
both the class conditionals have value
Now
Um
In
S12 now
X given Y is equal to one
Is one over four
And
X given Y is equal to two is one over
nine So since they have equal priors so
Base classifier with zero one loss is
nothing but comparing the posteriors
Since they have equal priors its
comparing the class conditionals Now it
is evident that one over four is greater
than one over nine
Implies
In the overlap region I decide Y is
equal to one
Okay
In the overlap region
We
Decide
Y is equal to one
Okay
So now now
Now the question is now can I take that
X plus
X1 plus X2 is equal to five Is it base
now No No because now what happens is
Now we just saw that the optimal base
classifier in this overlap region it has
to consider
Now all these is one class
This is another class Now that is what
optimal base classifier is
For this current class conditional I
repeat
Now since in the overlap the class
conditional of class one is more the
overlap region should be
Classified as class one
Okay Now therefore
When I consider that is the optimal base
classifier Now when I consider this
line
This particular region is considering as
class two which should not be the case
because this is an overlap region
Now in the overlap region it has to be
considered as class one
Okay Now therefore the line that you
are seeing is not a base classifier
Okay
So
lets make note of this
The next point is uh
Now
now
is
X1 plus X2 equals 5
is it
Bayes classifier
That is the next question The answer is
no
The reason is because uh
because
X1 plus X2 greater than 5
So
intersection S12
Okay
Now
we say
Y is equal to 1
as per
Bayes classifier
But
when you use the line
using the
line
it is Y is equal to 2
Okay
Now therefore
X1 plus X2 is equal to 5 is
not a
Bayes uh
classifier
Now then the Bayes classifier that we
are considering now that is
which is saying that this whole region
is
class one and this whole thing is uh
class two Is it unique Yes
Because there is no overlap Now since
there is no overlap there is no kind of
clash that is happening So the
decision is fixed
Now therefore the one that we are
considering is a unique classifier in
this case Okay
Now
in this case
the Bayes classifier
that we are considering
is
unique
Why In the overlap region
in the overlap region
there is no tie to break arbitrarily
Therefore
decision is
fixed
Therefore
its
unique
Okay
Now this gives us the
answer for the second part
of the question
Okay
So now lets look at the
third part of the question
The third part of the question is
for the
uh for this class conditional density
suppose that wrongly classifying pattern
one to pattern two
is 10 times more expensive than wrongly
classifying pattern into class two
Okay Now would it be a Bayes
classifier Thats the question
Okay
Is the question fine So now
when youre classifying any pattern of
class two to class one now that is any
in this region
or in this overlap region that is there
Okay In this full overlap region
if youre classifying it as class one
then it is 10 times more expensive
Okay Now then how do you consider the
case
Is the question
Okay So now lets
deal with that
This is the
part three of our
question
So this
part three
Okay
Now that is
cost
sensitive
Bayes
classifier Okay
Were considering the cost sensitive
Bayes classifier
Now
wrongly classifying
wrongly classifying the
example
into Y is equal to 1
is uh
10 times
more
10 times more expensive
than
wrongly classifying Y is equal to 2
Then
wrongly
classifying
Y is equal to 2
Lets say that
Y is equal to 1 when
truth is
the actual label is Y is equal to 2
is
lambda 12 It is 10 It is 10 times more
expensive
Okay
Y is equal to 2 when
truth is
Y is equal to 1 is
lambda 21 equals to 1
Now whenever you have
correctly classification
the penalty
now occurring is zero
Okay
So now what happens is now it is
nothing but
the risk
involved
if we decide
Y is equal to 1 is
10 times that of
the posterior
Then similarly
risk
risk involved if
we decide
Y is equal to 2
then it is 1 into
given X
Okay
Now then now then it means that
we want to minimize the risk Therefore
choose Y is equal to 1
if
the risk involved in
choosing Y is equal to 1 is
less than this case Then you choose Y
is equal to 1
Okay
Now since priors are equal now
since
since priors are
equal this can be
considered as
X given Y is equal to 2 is less than
X given Y is equal to 1
Now now
Now this actually I can compute this
This is
X given Y is equal to 1
divided by
X
Y is equal to 2
This has to be greater than 1
See now what does this mean
The likelihood
that is there of these conditionals
when it is greater than 10
now then you will go ahead and decide
it as
class one
Now we know these values right Now
what are these values
Okay Now these values are
Okay This is
X given Y is equal to 1 is 1 by 4
10 into
X given Y is equal to 2
is equal to 10 into 1 by 9
This is approximately 1 point 11
Now this
and we know that this 1 point 11
is
less than
Oh one minute
Let me do something
So now now then saying that
now
1 point 11 is less than 1 by 4 is not true
Now that means that in the overlap
region
you cannot choose Y is equal to 1 In
the overlap region actually you have to
choose Y is equal to 2 now
Now therefore is false
which implies
in overlap region
overlap
decide
Y is equal to 2
Thats all You would have been
logically If you have thought of this
yeah it since it is 10 times more now
in the overlap region what do you do
You decide that Y is equal to 2
Now that means that
this whole thing which is there
Sorry not this whole thing which is
there
you see it as Y is equal to 2
And only this region which is there
this region which is there
you call it Y is equal to 1
Okay
So now
what about the base classifier This is
the base classifier because we have
obtained this by
now comparing the
class conditionals
Okay
So now therefore
now what it the finally what does the
classifier boils down to This whole
story

 Now in
S1 minus S2
now
we decide Y is equal to 1
In S2 minus S1
we decide
Y is equal to 2
In S12 which is the overlapping region
we decide
Y is equal to 2
due to
high cost of misclassification
High cost of
falsely classifying it as Y1
Okay
This completes the problem
Okay Now this is how we approach a
given problem
and then solve them Okay So now now
we will
stop this tutorial at this point
Now we have two more problems that are
there
Now we will meet at the second part of
the same tutorial and then we will
continue that I hope this was useful
Thank you
