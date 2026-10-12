---
id: cF025BechXo
title: Tutorial 1 : Introduction to Python Basics
url: https://www.youtube.com/watch?v=cF025BechXo
date: '2026-01-21'
duration: 47:10
model: youtube-captions (en-orig)
transcript: true
---

# Tutorial 1 : Introduction to Python Basics

## Transcript

Hello all,
welcome to this tutorial in the course
of mathematical foundations of machine
learning.
In this tutorial, we will be going ahead
and
understanding
some of the basic constructs of Python
programming language.
So during this course we will be having
lot of exercises in which we will be
hand coding most of the ideas that we'll
be learning throughout the course to
understand how they work.
Now to do so we want to do it on a
system. For that we will be using Google
Collab. Okay. So if you prefer you can
install Anaconda kind of uh
distributions on your systems and then
you can run locally. at the end of
our course we might be needing GPUs
because of which we will be using collab
now where in which for certain amount of
uh duration Google will be giving us
GPUs for free so apart from that we
don't expect that you should have any
compute
so coming to the uh prerequisites so we
understand that we assume that
you are comfortable with programming
constructs.
So we are assuming that at least you
know some programming language may not
be Python but at least some programming
language and then you are familiar with
the constructs like looping, conditional
statements, functions and to certain
extent
the ideas in object- oriented
programming
like classes, objects, methods.
So this is our uh uh what do you uh
basic idea. So if you are not
comfortable with these ideas now we can
have an extended discussion on these
[clears throat] basic ideas in our live
sessions.
But in this tutorial, we will be going
ahead and assuming that you know these
prerequisites and then we will be
skimming through these ideas of looping
conditional statements, functions and
classes. In addition to that, we'll be
looking into some of the very
interesting data types in Python. lists,
tpples, dictionaries and sets.
Okay, that is the plan for our
discussion for the day. So without any
further uh delay, let's jump into this
things.
So we will be as I told you earlier, we
will be using collab, Google collab. Now
if you just go to your Chrome or Firefox
or whatever uh web browser that you are
using, you just type Google Collab
there. You will uh it will be taking you
to the page of Google Collab. From there
you can redirect yourself to a page to
this Google Collab. Now people who are
familiar with Jupyter notebook now it is
similar to Jupyter notebook running on a
cloud. Now here you can change the file
name and it is IPv interactive Python
notebook.
So let's run the first instruction which
is hello world always I just have
written something. So, so let's use the
same thing.
Hello
world.
So people who might be familiar with
couple of other programming languages
like C or C++. So you don't need to
include any of the uh libraries or any
of the packages. So all of them are
present. You can directly start going
ahead with that. Now whenever we need
extra packages now during those times
I'll tell you how to go ahead with that.
So this is a code block. So you can also
have text block. To run a code block,
you just click on this play button. Now
it's a print statement. The standard. So
if you are from three, it's print f. So
the this is the string input that you
are giving. This is a function. The
print is an inbuilt function which take
the string input and then process it and
gives the output.
Okay. And this is about uh the basic
print statement that is needed. Now
let's uh look into the data types and
okay now before that the variable naming
convention. The variable naming
conventions are pretty standard. Now
that is now you are the allowed
characters are capital A to Z, small A
to Z, 0 to underscore and you cannot
start a variable name with a number.
Okay. and then uh you cannot have
keywords as variable names. Now the
pretty standard uh uh uh rules on the
variables holds true. So now let's take
uh a list into consideration. Okay. Now
the data types that we shall be looking
is list
tpples,
dictionary
and then sets.
Okay. Now these are the data types that
uh now we shall be looking. Now
a list is a
collection of
items.
Okay. So and it should have some
properties. Now what are the properties?
Now list is
mutable. That means you can change the
entries.
and then
ordered that means you have indexing
and
allows
duplicates.
Okay. Now tpples on the other hand are
also
collection of items
but they are not mutable. That means
that you cannot change the contents once
you have defined it's there. Okay, you
cannot change the contents. It's also
ordered.
Okay, and
allows
duplicates
and dictionary.
Now standard uh to the English or any
language dictionary that we take where
in which you're uh you know the word and
then you you need to know the meaning of
it. So here the key and the value pair
is a okay here also it's a
collection of
key
value
pairs.
Okay, so it's a collection of key value
pairs
and
ordered
with respect to keys. Now that means
that if you want to access a value, so
the way to get it is via the keys.
Okay. And then
so
cannot have
multiple
keys with
same name.
Okay.
But you can have multiple values under
different keys. Now that is fine. It is
ordered with respect to keys and you
cannot have uh multiple key set and and
it's changeable. Okay, that is mutable.
You can change it. Now sets are again
collection of items.
Okay, it is unordered.
D R it's unordered.
Okay. And then uh
does not
allow duplicates.
Does not allow duplicates.
Okay. And changeable. These are mutable.
Okay. Now you can see depending on the
need
you can choose now what kind of uh data
type that you want to use. Now these are
uh the advanced data types. Now the
basic data types now that is uh an
integer, a floating number, a string and
a boolean. Now they are similar. Okay.
There there is no change in them. Okay.
And arithmetic operations, relational
operations all those things. Okay. The
outcome of a relational operation is a
boolean value. So the kinds of
arithmetic operations uh that we had in
other programming languages. Now all of
them remains intact. Okay.
So now let's go into the list. Okay.
Let's take the list into consideration.
Okay. Now since list is a collection of
items now that is let's say that I have
V1. Now I'll say since it's collection
of items what kind of items can be
there? Now it can be basic data types or
advanced types. Now all of them are
possible. I'll just for the simplest uh
uh demonstration purpose I'll take
everything as numbers. Okay. Now this is
unlike the array in C where which all
the entries should be same that okay
let's see that first 1 comma
04.5
3.14
Okay. So
okay. So then if I
I'll just print print V1. And if you
want to know what kind of data type it
is now, you can always use type of v1
if you see it. So it's possible it's a
it's a list. It's a class list. Now see
here
the list that you have created v1 is
actually an instance of the list. Okay.
Now these are the contents. Now these
are the the attributes and then now
since it's an uh instance now it also
have it can invoke methods. Now the
methods that can be invoked are for
adding a new entry or removing an
existing entry. See since it's mutable
that means you can change the the
contents.
Okay. So that means that you can add an
entry or you can remove an entry. So now
let's look at uh
adding a data.
Okay,
add
data. Now whenever I say add data, now
the immediate question is add where
where to add it? Okay, so now do you
want to add it at a specific index?
Okay, add it at a
specific
index.
or simply add it at the last.
Add it at the last. Now whenever you
want to add it a specific index, now the
method that we invoke is what is known
as insert. If you want to add it at the
last, the method that we invoke is what
is known as append. Okay. Now to
understand this, let's take a simple
list. Create a v two. Now you use big
brackets. As you can see from the
previous example to indicate that it's a
list we use big brackets 1 2 3 4 6 7
5 9. Okay. Now these are things. Now if
you want to say that you want to add
eight. Okay. Now if you want to add
eight at last
that is val 2 dot
append
8.
Okay.
Now
print
before just to understand the
the addition properly adding the element
properly.
print
after
v2. So now here you can see that this
print function is taking two arguments.
One is a string the other is this list
itself. Okay.
As you can see here this is before and
this is after you have added at the
last. This is append. Now similarly you
can insert. Now let's say that I want to
insert 12. Okay just copy this.
Now you don't want to append.
You want to insert. Now whenever I say
insert insert where you want to specify
an index.
Okay. Now let's say that I want to
insert it at index
uh
five. And similar to
uh all of the earlier programming
languages the index starts from zero.
Okay. So what is that you want to add?
You want to add okay just for
indication let's put
a name. So
what is index five 0 1 2 3 4 5. That
means wherever 7 is there now chandan
should come. And this 7598 will be
pushed. Okay.
As you can see here.
Okay.
This is how you can add an
element. Okay. Now I have just for the
sake of demo sake I have just shown you
adding of one element. Similarly you can
add a list of elements. All those them
are possible. Okay. So now then let's
look at the
remove.
Now whenever I say remove now again here
also the question arises remove which
element.
Okay. Now do I need to just the first
case is
remove the
last element
or
you want to remove the specific element
not worrying where it is present
irrespective of its presence in the
list. I just want to remove that
element.
remove the
specific element.
Not worrying about its index.
And
the third way is to remove an element at
a specific index.
element at a
specific index.
Okay. Now these are the three different
cases. Remove the last element.
[clears throat] Now you are not worrying
about which element it is. Now just
whatever has been recently added. Now
assuming that uh you have used upend. So
you remove the last element or remove a
specific element
at an uh uh wherever it might be or
remove an element at an index. Okay.
Let's see example for uh each of them.
Okay. So now let's uh
to remove the last element
we use
what is known as pop.
To remove a specific element
we use remove.
Okay, you specify the element and then
you want to remove an element at a
specific index, we use pop in with the
index. Now these are methods you want to
call with this instance.
Okay. Now,
okay.
Print
before
V2
print
after
V.
Okay. So now I'll say
v1 dot pop.
Oh sorry it has to be v 2 right? Yeah
sorry
2.pot. So the last element which is
there 8 is being removed. Okay. And then
uh
you can have remove a specific
element irrespective of its index.
Remove let's say
and then
okay
now this is being removed.
Now you want to remove a specific index.
So now let's say that I want to remove
the index two 0 here. See here 0 1 2.
Now three has to go off.
Okay.
Now this will give you an idea of the
ordering as well as its property of uh
mutable.
Okay. That means that you can change
things. Okay. So now
now allow duplicates you can have
multiple elements. I will not be going
ahead with that. So we just now one.
Okay. Now these are some of the uh very
important properties that are there in
the list. Okay. Now one of the great
advantage of this is you can have
different kinds of data. Now if you have
uh known the array in C. Now you fix the
type and then uh uh till the code
completes that date that that variable
will only have an array with homogeneous
elements. But even though you have all
numbers you can add a string remove a
string or for that matter any other data
type can be added. Now because of which
the list is quite flexible. Okay. Now
because of that reason most of our uh
operations will be centered around a
list easy to handle. Okay. So now the
tpple which is there is similar to list
but the only problem with the tpple is
it's not uh modifiable. Now that means
that adding and removing none of these
operations are there. That means that
whenever you're looking at a tpple, you
can only look at the order and then
whether uh duplicates are allowed or
not. Okay. So tpple to declare a tpple.
Now let's say I'll use v3 you have to
use parenthesis.
Okay. Now print v3 and then you can
print
type of v3. Let's put duplicates. 1
comma 2 comma 1 comma 3a 3. Okay.
So now this is just to indicate you that
it allowed duplicates.
Okay. And then
print
where three of
five.
Okay. 0 1 2 3 4 5. So I have to get
seven.
Okay. Seven.
Now it allow duplicates and then it's
ordered. Now please see here while
indexing you're still using uh the big
brackets. Okay in indexing irrespective
of the data type that you have we always
use big brackets.
Okay this is regarding the tpple.
Now
let's look at the next one now which is
dictionaries.
So while declaring a dictionary
you use
this flower braces. Now it's a key value
pair. So now you have to specify the
key. Now let's say name
Chandan
comma
age
35.
So
role number
let's say 182.
So these are this this is the key. This
is the value. This is the key. the value
you can have key value pairs like this.
So now
print
wherefore
if you want to access the name okay as I
told you it is ordered via
keys. Now if you want to access the
value you have to access it via key. In
addition to that
print the whole dictionary once and
the type of item. Okay.
So this is
so you access them via the
keys.
So the next uh now I have to show you
that it's changeable. Now how do I show
that it's changeable? I'll change an
entry and add a new key value pair.
Let's say that where four of
age
it's becomes 36.
Okay.
Just
print
always before and after just to show
that uh it's
four.
Okay.
You can see that this 35 here I can
modify a specific entry. Okay, I can
modify a specific value. Now similarly
you can add a new key value pair. Now
let's say that I'm adding my
address. Okay.
So I'm adding my address here
and you see that it has been added.
Okay.
This is how you can uh
modify the entries.
Okay. So now
the next data type that uh we shall be
looking into is set. Okay. Now set is
it's a collection of items which are
unordered. That means that there is no
indexing. Okay. Of three of four you
cannot get any of that. It's unordered.
doesn't allow duplicates
and it's mute. You can change the
element. Now whenever I say that change
that means that you can add an element
or remove an element. Now here now
please remember you cannot add with
respect to an index because the indexing
itself is not there. Okay. So now you
can add an element it will just be added
to that set. Okay. Adding at a specific
index doesn't make any sense here
because the indexing itself is not
there. Okay. Now please uh keep that in
mind. So now
to create a set also we use flower
braces but please remember the
difference between the dictionaries and
then the set. So whenever you are
dealing with a dictionary you have a key
value pair but here you don't have a key
value pair you just have some entries
you have just some items. Okay. So now
let's run this and see that it's a sack.
Okay. And let me show you that. Let me
do this. 9
6 6 4. Okay, I'm trying to repeat the
element and I'll run it. Now you see
that even though you have repeated, it's
not reflected. The reason is it doesn't
allow duplicates.
Okay. So,
and you cannot access an element. It
will throw you an error. You can just
give it a try. Okay. Indexing it. Now,
adding an element
is uh so print
before
five.
then
where five dot add now which element I
want to add let's say that I want to add
eight
okay and then to that
okay eight is not there it has been
added see uh just because it has put
eight before it is not an indication
that it is doing it in ascending order
okay only in this case somehow it has
done it there is no order to it okay
similarly you remove.
Now
what to remove? We use
remove. Let's say that I want to remove
five.
No, not the index five. The element five
here. The element five
remove. Okay.
Okay. Somehow it has been uh at the
fifth index. So please remember okay now
let's say that I want to remove the
index. I want to remove the element 9.
Okay.
It has nothing to do with the index.
Okay. Similarly you can do all the
standard set operations like union
intersection set difference and stuff.
Okay. Now this is uh regarding
the
data types that are there in Python.
So now the next thing that we shall be
looking into is looping. Okay. Now the
first there are two loops.
You have a for loop and then while loop.
See for loop is used when I know how
many times the iteration has to happen.
we will use while y loop. So when we
don't know how many times an iteration
should happen but we know when to stop
the iteration. [clears throat] Now that
is when we use y loop. There is a
condition depending on that condition
the iteration depends on whether the
condition is satisfied or not satisfied.
No we cannot do it. Now for loop is used
when you know how many times you have to
iterate. Okay. Now let's look at the for
loop.
for loop. Now since we know how many
times you have to iterate now for i in
range of 10. Now this range of 10 will
give you 0 to 9 and then uh during each
iteration the next next value will be
assigned and then you go inside and
print it. See now here one major
difference that we should know is
regarding the indentation.
Okay. So in some of the programming
languages we have
braces, curly braces, flower braces to
indicate what are the instructions that
needs to be repeated.
But
here in Python now we don't have any
kind of braces like that. Now we use
indentation for it. Now whatever
instructions that comes after this in
this block okay now those will be what
do you call iterated upon now for
example I'll say print
right so now that means that now these
two instructions I'm just showing you to
preliminary instructions but yeah you
can replace that with any instruction
and then understand that okay see now
for each iteration now these two things
will be repeated. So now and then
finally
print
hello.
Now this is outside of this indentation.
Now you can look at this. Okay. Now once
you are done with this for loop now
you'll go here. Now the indentation is
the idea here. Okay.
You can see zero high and hello is only
coming once. That is post this for loop.
Okay. First I will get the value zero
and then it will go inside the loop. Uh
do this and then I will get the value of
one. See you don't need to increment the
value. Okay. So now for example you want
it to be in the steps of two. Okay. Now
you want to start from zero and then you
want these things to be in steps of two.
Then you can do it like this. 0 2 4 6 8.
Now the first number is a starting
number. This is the ending number. Now
it is always one less than that. Similar
idea and at the steps of two. So you get
zero then you get two then you get four.
You go it like this. For example you can
say from 5 to
at the steps of 25. You can do something
like this. 5 30 55 80 105.
Okay. Like this it will happen. So three
numbers. The first one
is the starting point, the ending point
and the step size. Now if you don't
specify okay
let's say that you just specify
five here. Now this is the last that
means by default it is starting from
zero. If you say that no no you start
from two when you have two numbers the
first one is the starting point the
second one is the ending point. Okay,
only with three numbers the starting
point, ending point and step will be
considered. Okay, and this is the for
loop.
And then uh to go ahead with a while
loop. Now, one of the standard examples
that people will always give is the
Fibonacci sequence. I assume that all of
you know the Fibonacci sequence 0 1 and
the next is 0 + 1 is 1. Then 1 + 1 is 2,
2 + 1 is 3. You take the last two
previous and then you go on adding okay
the standard Fibonacci sequence. So now
uh the idea to go ahead is now
now I will
give you a number.
Okay.
Generate
fib series.
Okay.
Of numbers
less than the
given number. So let's say that I'll
give you
20. Okay. So number
I'll give you the number equals 20. Now
what should be the output? 0 1 1 2 3 5
and then 8 then 13.
Then comes 21 but 21 is greater than 20.
So you will stop. Now I don't know how
many times I have to iterate. I just
know till the generated number is
greater than the given number till that
point I have to reiterate. Now I know
condition till that condition is
satisfied I'll be going ahead. So to do
that it's the the idea is very simple.
I'll just decide let's take 20 itself.
The number is 20.
Fib
equals 0.
Then
fib 1 is equal to 1. Then you print fib
0 and fib 1.
Okay. then you use while
fib one
is less than num.
Okay.
So
fib 0 comma
fib 1.
Okay.
So now here now this is how we do it.
While fib 1 is less than num. So the
current one one is less than 20. True.
Now then what you will do? You'll put
the f one which is 1 to 0 and then 0 + 1
to this. Okay. Now it's like this. This
first one will be assigned to this and
then to this second one. This value is
assigned. Okay. This is something that
is not there in C but it is currently it
is there in Python. Okay. Now if I do
this
now 21 is coming. The reason why 21 is
coming is uh because you have put the
print later. You can modify it. Okay.
Now 21 is generated and 21 will come
here and then it will go and check.
Okay. I assume that all of you are
capable enough to modify this. I have
deliberately made this mistake so that
you can rearrange this and then you can
get only these as the output.
Okay. So now this is the looping for
loop and y loop. For loop is used when
you know how many times you have to
iterate. Y loop is used uh when you know
that okay there is a condition till that
condition is satisfied I'll be going
ahead with the iterations.
Okay. And then we will look at the
conditional statements.
Now here we have uh if block will be
there.
If else will be there.
Okay. And then you have if
else if clock will be there and then if
[snorts]
else if else will be there. Okay. Uh see
uh here in uh Python we don't have
switch. Okay. So uh no if. So when some
condition is satisfied you take
a certain instruction you execute
certain instructions. That is when you
use if. Now the second one if else is
some condition is satisfied you do
something. If the condition is not
satisfied you do something else. Okay.
Now that is your whole your whole
execution is divided into two parts.
Now the third one is if else if. So you
check for the first condition. Okay. If
first condition is satisfied then you
execute the instructions for that
condition. If the first condition is not
satisfied then you check for the second
condition. Okay. If the number is divid
divide divide by two you do something.
If the number is not divided by two and
then it is divided by five then you do
something else only when the first
condition or the previous condition is
not satisfied. Okay, you go to the next
condition.
Okay. Now here there is no default
argument. Okay. Like uh so if none of
the condition is satisfied now then you
do what is not there. If you even
include that it will become if else if
else. Now we'll take a very simple uh
thing.
Okay. So now uh I'll give you a number.
Now you just say that it is divisible by
two or not. Okay. Even or odd. I'll just
give you a number. Let's say that the
number of 13. If
num mod 2 now num mod 2 will give you
the remainder. Okay. The modulus
operator is used to give you remainder.
And then you're checking that is this
remainder equal to zero.
Okay. Now this is a conditional
statement. You're checking some number
is equal to another number. It can only
give you two option. Either it is true
or false. If it is true, now you just
print even.
No. If it is not true,
you print
odd.
Okay, it's odd. So if it is 12, see this
make sense? Okay, now if this condition
that is being checked, this is a
relational operation. If this is true,
then the indentation, please look at the
indentation, this will be satisfied. If
the condition is false, then this will
be satisfied. This these instructions
will be executed. Sorry, these
instructions will be executed.
Okay. And if you don't have the else
part then it is the standard if
statement. Okay. Now this is how you
have if else then you can have uh if
else if
a simple again if
number
I always prefer to if number mod 2 equal
to equal to zero. Now then you say that
print
divisible by two.
Okay. Now if it is if it is not
divisible by two that means that the
remainder is not zero then
elif else if
okay you do this.
Now if it is not divisible by two and it
is not divisible by three then again
we'll check whether it is divisible by
five and then you'll finally have an
else block. If none of this is true,
okay, then
print
not
not divisible by 2 3 5.
Okay,
it the number is 12. It is divisible by
2. So, and see that it is also divisible
by 3. But why is it not printing
divisible by three? Because once this
condition is satisfied,
if it is if this is executed, it will
come out of this whole block. It will
not go into only when this condition is
not satisfied. For example, let's say
that number is 15
then it is saying div will be three.
Why? The first condition is giving you
false. Now, because of which you will
check the second condition,
okay, but it is true. Now when you
divide 15 by 5 then also you get the
remainder zero but that is that itself
is not being chucked.
Okay
this is regarding the
conditional statements. So if you remove
this else then it will be if else if
blocks.
Okay. Now this is regarding the
conditional statements. And then
so in so the next idea is functions.
Okay. Uh now functions is you put these
depending on the need to go ahead with
modularity. You don't want things to be
as one uh what do you call one block of
code. You want them to be modularized.
And therefore what do you do? You put
them into multiple functions. Okay. So
you use def to define a function and
name of the function
can be any valid uh
variable and then you can give an
argument. Let's say that I'll give num.
Okay. Now what is the functionality?
What is that this function supposed to
do? Now it should tell me all the
numbers that divides this num. Okay. Now
let's try to understand that problem.
Now let's say that I'll give you my
number is 12 and then my output should
be 1a 2a 3a 4a 6
6a 12.
Okay
I should be getting this
now one and the number itself is always
true. So yeah, now how do you do it? Now
first now let's say that
these are factors.
It's 1 comma num itself and this will be
there always and then
okay now then you
return
factor
right if you want to give another number
let's say that you want to give seven
okay now here you're bringing
these under one roof that is the
function. This will be executed only
when a function call is made. Okay, this
is a return value. This is the argument
that you have. Okay, now if you want to
fix some default arguments, now you can
fix it later. Okay, after these formal
arguments, you can fix default arguments
and then you can modify them. Okay, at
the need when we will be going ahead
with other specific functionalities at
that time we will look at the default
arguments and how do we code with them
in some other coming tutorials that we
shall have. Now
this is what we assume at least you
should be knowing these basic ideas of
Python. Okay. Now to give you a recap of
what are the things that we just looked
at. We looked at different data types
that are there. Now how do they differ
from each other. Now if you want a
collection of items where which you can
change the entries you want them to be
order and duplicates should be there.
Now then you should use list. If you
want the collection to be just items and
then they should not be modified but
allow duplicates. Okay then you should
use tpple. If your it is in the format
of key value pairs then use dictionary.
Now if you want unique set of uh
unordered items now then you should use
set. Now we worked with each of them in
brief and then we looked at the looping
the for loop and then the y loop and
then we looked at the conditional
statements and then a very simple
function. Okay. Now with this we
conclude this tutorial. Now
at the advanced ideas that are needed
like classes, objects and remaining
things. Now when we start programming at
the time of need, we will be introducing
them. But as of now this much is needed
for our working for some amount of time.
Thank you all for uh patiently being
there in this tutorial. We'll meet you
in next tutorials. Thank you. Bye-bye.
Have a nice day.
