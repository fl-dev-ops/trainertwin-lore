---
id: 8qzXJh2owLU
title: Lec 4 - Deep Generative Models Variational Divergence Minimization
url: https://www.youtube.com/watch?v=8qzXJh2owLU
date: '2024-11-23'
duration: 03:03:52
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_1: null
  speaker_2: null
  speaker_3: null
  speaker_4: null
---

speaker_1: Okay there will be 15 questions 15 to 20 questions and well give you 20 25 minutes to solve it Okay multi choice questions The first quiz will happen next week Is that okay

speaker_2: Is it possible sir if you can share some sample questions

speaker_1: Well its it simply can but its when there are factual questions on things that has been covered so far in the class So if you brush up whatever has been covered in the class that should be enough


Okay let us start now todays class

speaker_3: Sorry for interrupting just one question So you said next Sunday is next Sunday or Saturday

speaker_1: I mean yeah my bad yeah next Saturday next week

speaker_4: Um so one more question I have So uh whatever we cover in todays class is also gonna be included

speaker_1: Boss

speaker_4: Okay and sir I remember we have already discussed this in length but on the first class there was a lot of back and forth between what was our final decided grading policy If you can just summarize it quickly once again for the sake of clarity it will be really hard

speaker_1: It will be done that no please dont do this we have done this no there is it is documented it is written look at this


So yes of course I voted and said that this is funny and we are not going to disclose it anymore please dont do this

speaker_4: Of course

speaker_1: Okay so it is there it is written lets have a look at it


I see another hand raised Dermot lets go on

speaker_4: Uh yeah so uh so for the quiz will there be


So will there be calculation for this or only as you said factual


Uh am I audible

speaker_1: Brush up whatevers uh

speaker_3: So the audio is not very clear

speaker_2: Yes sir we are uh you are breaking

speaker_1: Hello is this it okay I think I should do some problem with my internet today just a minute give me a minute


Hello am I audible

speaker_3: Yes sir now you are

speaker_1: internet explores yeah i said it is just here its about testing what you have understood


From whatever has been taught okay It will mostly be factual with


Three four options for each question and there will be 15 questions in 20 minutes okay and its whats


Okay let us start then Hope that you see my screen And last class just a quick recap


yeah in last class we defined what generative modeling is uh that we are given data from an unknown distribution okay what we wanted to do is to estimate the unknown distribution and also sample from it okay that was the problem that we wanted to solve


Okay so we wanted to do it from the perspective or angle of what I call it as divergence memorization


where the idea was to assume a parametric form for the density function to be estimated denoted by p theta right where theta are the set of parameters that are representing the underlying distribution okay so we have p theta that represents the distribution uh that we are modeling and we call this the model distribution and it can be any parametric distribution


as a Gaussian distribution or even a neural network okay uh that would take um some random variable as input and the output of that neural network is the distribution of the output of the neural network is taken to be p theta


Then we said okay once you have the speed parametric model you define okay I think theres a typo here


Its just not the wall


Somebody tell me whats wrong


Im not seeing any of these outcomes

speaker_4: Are you not able to scroll

speaker_1: Im able to scroll yeah Im actually not able to scroll on so now


And now we can scroll


There was a typo here define and compute


Define and compute a distance or divergence metric between the true distribution and the assumed parametric density function true density function and parametric density function okay That will tell you how close or far px and p theta are where px is the true distribution and p theta is the distribution of interest okay And then you adjust or compute the parameters of p theta such that this divergence minimizes divergence metric is minimized okay


Computing the parameters of p theta such that this is minimized is what is called as training or learning of the model Mathematically it is solving an optimization problem over the space of the parameters of the density that we have assumed So the final estimate of p x is p theta star where theta star is the set of parameters that we have obtained by solving the above optimization problem


That is what we saw And also we quickly saw one definition one of the possible definition for the divergence metric which we call the Kullback Leibler divergence or KL divergence Okay Okay so I want you to Ill stop here for a minute and I want you to let me know if you have any questions on this general philosophy of divergence minimization because


That will be the central theme of most of the models that well be seeing in this course We start with a parametric form for the density that we want to estimate and we define a divergence metric Now that divergence metric becomes a function of the parameters of the underlying density Then we compute the or rather we get the parameters of the density by minimizing the divergence


metric between the true density and the parametric density so that is the idea any questions on this


Follow me more


Am I audible Hello


Okay no questions Okay great let us uh move on then


Now we will look at the first class of family of generative models that we will see We are called adversarial generating models are also called as generative adversarial networks of GANs Now what is the idea there So same thing right So what we will do is we will


Even


Data okay so what is data data are


some samples


Drawn from


unknown distribution


What can these be These are examples of


Only just of digits or


is what is there in MNIST dataset


It can be


some features of text and so on it can be anything we are given n data points of n data points drawn from unknown distribution okay goal


Owl is too


estimate px and remember we are solving kinetic modeling here and


from VX


Now what do you mean by sampling from PX is that generate


Four samples from PX


Okay that


Right


Not in D


given data set but you want to generate more samples from the data set okay that are not a part of the data set okay that is uh that is what we want by that is what we need call by sampling okay okay now what is the idea so first first step to do this is that zoom


a parametric form


call it P theta


Okay this is what we start from Now in the class of generative models known as adversarial network how do we get p theta So in


The P theta is represented by a neural network


I think youre on the hook


Okay it means that there is a neural network


Whenever I write neural networks right in this course from now on I will be assuming


Ill be following this convention that I will write these kinds of quadrilaterals right trapeziums and the shape will be proportional to the dimensionality of the data Why am I I cant write a straight line


Better okay


Now what is happening here is that okay so let me before I move on I am assuming that all of you know how the error back propagation algorithm works right How to train neural networks Is there anybody who does not know how to perform gradient descent on neural networks


And then I will just make it a do we do we need yeah Nirmal you raised your hand

speaker_3: I mean I dont know uh but if we can have tutorial on that that would be good

speaker_1: I can but thats why Im asking right do we need a tutorial on backpropagation algorithms

speaker_3: I mean I c yeah

speaker_1: Okay tactics

speaker_3: Yes

speaker_1: So well see

speaker_3: Yeah it was just

speaker_1: You havent tried neural networks before is it

speaker_4: So sir were uh were broadly aware of how it like what its supposed to do but not with the same level of mathematical rigor that this course is uh going on with

speaker_1: Okay so let us make that a


an item of tutorial then we will


that will teach operational okay so


it is mostly uh repeated application of chain rule okay uh that is that is that is what it is okay but yeah i will ask them to our tutorial on black box okay uh that apart um so i said now p theta will be represented using neural networks okay so now let us call this as some g theta of g okay now lets say that you have g


which is a random variable that is that has a Gaussian distribution associated with it okay


Now typically


Okay I didnt come to that anyway Now we have this proposition that suppose


Z is a random variable which


distribution


and G theta of G


your function


a function that would


map G okay to some other space X cap


Okay now this result says that


Z cap


Cheers


Another random variable


the distribution


the distribution


Governor White


The function g to the power


Does it make sense Do you understand what Im saying Suppose this is a standard result which you will be studying or have studied in random processes that if you have a random variable okay and if you have a function that acts on a random variable then the distribution of the output of that function okay first of all the output of that function is another random variable and the distribution of that particular output or function depends upon the functional form of g


What do I mean by that examples


If


g is lets say uniform random variable between 0 and 1 okay and some g theta of x is equal to lets say


g squared okay then g squared


Can you see my screen

speaker_2: So if youre writing something then I dont think we are able to see

speaker_1: Oh is it I think it is stuck


Okay I think yeah z squared will not be in the song


Do you see my writing now

speaker_4: Yes sir

speaker_3: Yes uh

speaker_1: Okay right Yeah this is what it is right I mean if you have lets say uniform random variable and you take the square root of it it will not be uniform It will have some other distribution than uniform distribution Do you all get this idea So basically what Im saying is that you take a random variable that has a particular distribution okay And then if you pass that through a deterministic function the output random variable will have a different distribution compared


to the input random variable is this idea clear and the distribution of the output random variable depends on what sort of function uh you are passing the input random variable through is this is this clear


Now why is this important Let us look at this The way we are modeling V theta is via this function V theta of z Okay Now this G theta of z


Let us let me write that again


g theta of g in our case


G theta of G is a neural network


Okay just for the sake of completeness I will define what a neural network is now


Lets say that Z is in some Rk dimensional space and we are talking of vector valued random variables here okay So what happens is that in this case right I mean Z is a vector valued random variable with Gaussian distribution If Z is in Rk then G theta of Z is defined like this So what you first do is that you take


some weight vector w1 okay and multiply that with z so what will you get i will write the dimensions also


Okay lets say that W one is a matrix which is in


Z is in R K right uh so this is um


L1 cross K So you have a matrix of L1 cross K So now when you multiply


W one with G what will you get you will get a


are L one dimensional vector Can all of you see that


because z is actually in k cross 1 right its a column vector of k dimensions which means that you have 1 2


K rows and one column and W1 has L1 rows and K columns When you multiply that you will get a L1 cross one dimensional vector Can all of you see this Is it okay


Okay so then what you do is this is a linear transformation then you


an element wise non linearity where what happens is that when you do this w1 transpose z so what is happening is every element of this w1 transpose z so this of a vector z is simply you take the elements of z so z is actually 1 by 1 plus


Let me make it a scalar


This is the definition of the sweet mode


Okay so now what you do is that when you write sigma of w1z w1z is an L1 dimensional vector you take every element of it and do this operation 1 by 1 plus e power minus z then you still get an L1 dimensional vector that is what I call by sigma w1z Is that okay


Okay so then what happens is that you take another set of parameters call them w2 and multiply sigma w1z with that w2 Now this w2


of dimensions


L2 cross L1 okay which implies that W2 times sigma of W1 z okay will lie in R L2 cross 1 dimensions is that okay


Okay so then what you do is


is further okay then you have another non linearity here


Okay then you take another W three here and now W three is


This is L3 cross L1 and you can have another non linearity Youll have W4 and so on So what is this This function is actually a four layer neural network


Is this okay So this is what a deep neural network is I have just written that in a vectorized form that there are functions right I mean there are linear transformations which are of type W1Z okay And then there is a nonlinearity given by a sigma So there is a linear transformation followed by a nonlinearity That is what a deep neural network is


I hope this is clear to all of you


I see some questions here yeah

speaker_4: Ah yes sir I mean you just mentioned W four so there is no sigma applied to W four or

speaker_1: Ah you can I mean that depends no I mean if final layer is linear in the k in the network that I have written you can put a hit one here

speaker_3: Okay thanks

speaker_1: Yeah I mean that depends Thats a design choice Now now if this is G theta what is theta Theta has all the set of parameters you know W1 W2 W3 and W4 This is what I am calling from calling by G theta


that all right okay so Im going to try this again so now training a neural network will be finding out these w1 w2 w3 w4 through solving an optimization problem and what problem do we solve in the case of generative models are we is this is something that we will see now and how do we solve it is through error back propagation okay maybe Ill just mention it quickly when we formulate the optimization problem but anyway so now do you understand this now when I write this


diagram


Bug


is a neural network that takes z which has a Gaussian distribution okay and there is this function g theta of of z and you are getting an x cap okay typically z is in some r k dimensional space and x cap is in r d dimensional space which is same as the dimensionality of your x because we are trying to model uh distribution of


typically what happens is the dimensionality d will be much higher than that of k which means that you will have to adjust this l1 l2 l3 l4 okay such that the final uh output layer will have a dimensionality that is much higher uh than uh the input dimensionality and note that it need not be a four layer neural network for instance right if you take resonance 50 there will be these 50 w


use okay 50 layers its a deep neural network that Ive just given you an example of a four layer neural network it can be any layer and these nonlinearities need not be of this form uh it can be of this form only so right I mean with this


one if z is greater than zero or zero otherwise this is called the ReLU activation


And this is called the


and so on right doesnt matter but in general it is a deep neural network I mean for as far as our course is concerned we dont care what the form of these things are they are hyper parameters and design choices okay so now what we are interested in is that you start with a random variable which has a Gaussian distribution in k dimensions there is a deterministic function d theta which is a neural network that would that would transform it to another dimensional space called that x theta x cap


And this has the distribution V theta This is our setting


Okay well take questions here Um Abeeru

speaker_3: Yeah so the in theta is the you are considering theta as the set of parameters So in that set of parameters since Z itself is a random variable following normal distribution so those parameters the mu and sigma they will not be considered in theta

speaker_1: No no no thats fixed no Z is from normal 0i 0 1 So that is fixed

speaker_3: Okay okay

speaker_1: Z is not the Z does not have any parameter no its the input random variable


typically what happens no we assume that we know how to sample from z we can we know right because if you have i mean there are these functions called rand n and random number generators in all these uh like programming languages right what do they do they actually sample from a gaussian distribution correct so we assume that we know how to sample from a gaussian distribution and therefore we can generate this z as much as we want


And that has no parameters What is parameterized is this function V theta of Z okay that this Z is passed through to get a get an X cap okay which has a distribution P theta


Is this okay Yeah yeah okay yeah uh

speaker_2: Yeah hi sir uh this is uh the Gaussian distribution of this random variable Z

speaker_1: The random variable z has a Gaussian distribution

speaker_2: And uh sir in this uh W three can you uh scroll up a little bit


In this uh so w3 will be a this matrix of L3 cross L2 right


Yeah yeah

speaker_1: A week

speaker_3: this Z the Z did it uh is it actually representative of the data or was some

speaker_1: Translation

speaker_3: Optional

speaker_1: no no no no no no no so z is just uh uh an input random variable okay it can be anything you take it to be normal distribution normally distributed okay okay you take it to be normally distributed it has nothing to do with data

speaker_3: Okay something was done to bring the data time to Z form I mean like

speaker_1: So no it has nothing to do with data it has zero connection with data

speaker_4: No okay

speaker_1: It has nothing to do with data okay


So it is just that we are okay So I tell you the like maybe the high level story or maybe its just a mistake See basically what we are trying to do is we are trying to transform okay an arbitrary random variable to some random variable that has same distribution and has our input data


Is that okay

speaker_3: Right yes

speaker_1: Now this z is an arbitrary random variable and we know that if you pass an arbitrary random variable through a function the output random variable will have a different distribution Now the goal is to choose these parameters theta such that the transformation that this arbitrary random variable goes through will be such that the output random variable that you get will have the same distribution as that of input theta


So now the goal is to set this d theta set the parameters of the neural network such that distribution p theta matches with px which means that I want the distribution of x cap to be same as the distribution of x which is my input data Z has nothing to do with the data It is just the input seed It is seed


It is the random CNN that you start with You pass it through a neural network okay And output of the neural network will have some distribution I want the distribution of that output to match to the input the distribution of given data

speaker_4: Yes in that case the creation or the finding out of the distribution of Z is also as equally important as G theta of Z right

speaker_1: No no because

speaker_3: I want to say

speaker_1: Yeah this is a random seed you can start with any this is the first

speaker_3: Nothing was done there so we are just picking something a random seed

speaker_1: It is random stuff it is nothing but random stuff

speaker_2: Okay okay fine

speaker_1: Also transform this normal distribution into distribution of interest via neural networks

speaker_2: Okay okay okay yes thank you

speaker_1: The astic


So it is not in a classifier what happens is the data will have a larger dimension where you give images and you reduce the dimensionality and the final layer will be equal to the number of classes


But in generative models it is the other way around because the dimensionality of X cap here the output should be equal to the dimensionality of the input image because the final goal is to sample isnt it Now if you want to sample pictures of dimensional dimensionality 200 by 200 pixels then the output of this neural network has to be of dimensions 200 cross 200

speaker_4: Okay and what would be the input dimension in this case uh if the num uh image size is 200 plus 200

speaker_1: Typically it is it will be of size lets say 16 32 and so on So thats why if you look at the shape of the neural network that I have written it will have increasing dimensionality as you move deeper onto the network


example


See input is of 16 dimensions and you keep increasing so see it is all in setting up this L1 L2 etc right you choose those are the hyperparameters that are in your control as a designer

speaker_2: Yeah that is fine

speaker_1: like our output should be a image and input is also a image right so no no no no it is not an image it is a random seed that is what im trying to say input is not an image


So this is a generative model

speaker_4: Okay okay yeah yeah yeah

speaker_1: You understood the setup it is see it is not you are giving an image and you are asking for a class you are including the random seed and you are expecting the neural network to give you an image from the data distribution

speaker_4: Yeah yeah yeah its a generative

speaker_1: So we the course is deep generative modeling

speaker_3: Just joking

speaker_1: Its okay you understand now


Thats why the shape look at the shape right the shape of the neural network that I have drawn is that you start from a lower dimension and go to a higher dimension as you move across the network Okay


As a shield

speaker_4: understand we are not using the input but somewhere we will have to relate with the input distribution like that is how we will calculate the loss and all

speaker_1: Come again

speaker_4: Like I understand we are not using the actual input here but what Im saying is how we will relate with the actual input distribution

speaker_1: I am not saying that we are not using the input I am saying that the input distribution does not matter because you can start with any random seed and then convert that into distribution of interest using your own

speaker_4: Okay sir so where we use the input here

speaker_1: Okay see how do you get X cap here


X cap is gotten by taking a sample from Z okay and passing through So basically what you do in practice Ive written this no Z is sampled via random number generator which means that you run rand N once okay you get one number that is your Z You pass that Z through this neural network D theta you get an X cap that is how you use the input

speaker_3: From the data set

speaker_1: you mean okay so please dont call it as input you know its a bit confusing input to this setup is z okay and uh the data okay is x1 through xn we are i mean everything that we do is using data we will see that right we have not still told you how to set the parameters of g theta right the parameters of g theta is set by using the data


I thought I mean yeah I think you know there is a confusion Z is what is an input to this setup Okay And let us let us call the lets call x1 x2 x3 as input sorry data


And this has the random seed


We will use I mean I okay let me I mean for everyones sake you know what Im saying When I say that the input distribution does not matter Im referring to this random seed not to the data distribution I mean everything depends on data distribution because we are interested in modeling the data distribution When I say input input to this setup which is the random seed it does not matter if you sample from a normal distribution or you sample from a uniform distribution Is that okay Is this clear to all of you


I mean thats a huge confusion if you had that confusion is this clear


Okay yeah I think theres one more question Sanjit

speaker_4: I understand that we are just taking a random uh sample Z from the normal distribution and passing

speaker_1: Mm

speaker_4: What are we taking it

speaker_2: Comparing it

speaker_4: Like Im saying it

speaker_1: I have not told you that yet I have not told you that yet Im just saying x hat has a distribution Lets call it p theta That is what Ive told you so far I have not told you how to make this p theta close to px Anyway because youre asking Im telling you So evaluate the divergence between p theta and px and set the parameters of this g theta such that that divergence is minimized

speaker_2: I understand that flow like you had explained it in the last class what Im trying to relate to is like lets say for like supervised learning when we have the


Lets say we are going for

speaker_1: Hold on hold on hold on hold on You are asking me how to do it practically right How do you basically what you are saying is how do you minimize the divergence practically right Yes sir I have not answered that question Hold on Ill answer it in this class

speaker_4: Focus on sure thank you

speaker_1: Okay yeah Harish

speaker_2: So the sampling of the data the normal distribution one so do we can why do we consider it for a normal distribution or can we consider with any other distribution so for the for the side here

speaker_1: Yes you can but generally normal distribution is chosen because normal distribution has infinite support which means that like it has I mean for the entire space Rd the density function is not zero if you take uniform distribution for example right the density function vanishes out of I mean outside of a window but in normal distribution the density function is is existing when its non zero over the entire space no thats why you


Take normal distribution

speaker_2: And one more question on the dimension of K here so the dimension K here is dimension of

speaker_1: Yeah typically it is tend to be 16 32 if I mean if youre working with images

speaker_2: So does it matter So you have mentioned that the D is much much greater than K here right So does it matter based on the data size So we need we choose 16 or 32 or is it also random

speaker_1: Yeah thats a good question Its a hyperparameter but like in some of our research we have we have actually found out that the dimensionality matters Right There is an optimal dimensionality is what we show in some of our papers But yeah like in general its a hyperparameter

speaker_2: And so we we choose that once like for example we take an initial of 16 or 32 and then based on the training and how it works so do we change that based on

speaker_1: Typically that is not a happy parameter that people do norm that is kept fixed


Yeah yeah

speaker_4: So the real application of this function I want to understand my assumption is correct or not if we give some few text like a cup on table then it will give me a picture of the cup on table

speaker_1: one table no no no see for for now i have not told you the conditional part of it what you are saying is a conditional generating model well come to that in a while it is not it is not conditional generating modeling right now right now what happens is after you train it you give a random number as an input to this okay it will give you a picture from the distribution


Now that you are asking me let me just show you that as well


You see my screen now there is this website called thispersondoesnotexistcom okay


So what is happening is every time I refresh this page


I get a new picture you see


see my screen no see these are pictures of like non existent people so what is happening when i refresh the screen is that a random number is being generated which is your z and that is getting passed through this network g theta and you are getting a picture here there is no conditional generation i am not giving a text as an input i am just giving a random number as an


Right now Im not looking at conditional generation Im simply looking at this is called unconditional generation where you generate images from the underlying distribution or generate data from the underlying distribution without conditioning

speaker_3: Got it

speaker_1: I will also talk of conditional generation but I am skipping a lot We will do that one step at a time We will understand the unconditional part and then adding conditioning is a trivial extension to this okay

speaker_4: Yeah so uh I know sorry you have not explained this but in the

speaker_3: terms of picture we got a p theta but then uh how to measure like between p theta and p x

speaker_1: Dean Ive told you that Ill do this in this class please dont repeat the questions that Ive answered already

speaker_4: Yes yes

speaker_1: That is the next thing that we will do No see okay So let me tell you my philosophy of teaching When I teach I just I mean like open it layer by layer So now what is happening is I am trying to give you an abstraction of what is happening We will go to the details So now at the level of abstraction what you need to understand is that the idea is that you start with an arbitrary random variable g pass it through a function g theta and you get another random variable which has a distribution p theta


Now the next thing is you tweak the parameters of this d theta such that the distribution of the output of this network x dot is same as the distribution of p x Now how do we do that is a question that Ill answer in a while But now you ask me questions at this level of abstraction If you have difficulty in understanding this level of abstraction sure ask me questions


Im going to do in the due course right if you ask me that anyway I mean I dont mind but yeah so just a request okay anyway uh Mukesh


my question is regarding


Sir in the CNN architecture actually what we do we try to implement this pooling layer where we try to reduce the dimensions of the data But here were just passing the seed to increase the dimensionality Is that correct Yeah yeah yeah So the neural network here will have increasing dimensionality So actually here we dont have input data as an image Thats why we are trying to increase the dimensionality


I will not say that see we want to start with some noise or some random arbitrary from from an arbitrary random variable and generate images so which means that we start with a lower dimensionality we need to increase the dimensionality


okay so now in terms suppose see i have not told you that see this is not a cnn that i have written what i have written here is a fully connected neural network


Okay which is a feedforward neural network or a multi layer perceptron If you want this to be implemented as a CNN okay that also has to be done in the TA session


So you have to teach about upsampling layers


There are this neural net I mean neural network layers called upsampling or also called transpose convolution layers


Okay that will take as an input a lower dimensional feature and give you a higher dimensional feature vector as output Just like you have convolutional layers there are transpose convolutional layers that would increase the dimensionality of neural networks Okay

speaker_3: Okay so okay thank you

speaker_1: But but dont worry about architecture for now I mean these for us g theta is simply a function I mean it need not be a neural network also but now because in in practice we are only looking at neural networks Ive said that its a neural network So for now let us assume that these are all fully connected neural networks which are I mean no fancy network architecture here right I mean they are all multi layer perceptrons or simply fully connected neural networks Is that okay For now

speaker_3: Yeah yeah sir correct correct words

speaker_1: Okay uh any other question is the problem setting clear to all of you


I didnt expect so many questions at this stage anyway no problem its good that youre asking questions okay lets move on so now what is the objective so now the objective


is to make


P theta


uh as close okay


Make PT done


to px correct now if we do this what happens is suppose you are given uh data from lets say human face distribution if we can have this setup and make my p theta close to px then i have solved the problem of generative modeling do you agree


Every time I start with a random seed and pass it through the theta I will get a picture from like human faces because the distribution of the output of this neural network is now close to px Clear Is this clear


Okay now what do we have to do is is that the question is that question


How to


set the parameters


parameters of g theta


Such that


that p theta is close to px


is the central question do you agree so now only thing that we have in our control is uh g theta which are the parameters of neural networks the question is how do we set the parameters of a neural network such that p theta is close to px we note that if you fix a value


excuse me so if you fix a value for the parameters g theta parameter top parameters of this neural network you will get some distribution on on on some distribution on the output now if you take another set of parameters you will get another distribution now the question that is to be asked asked is which set of parameters of this neural network will ensure that p theta is close to ps


Good


Now to do that is now the the solution for this is that simply set the parameters of your such that


it minimizes search over all possible sets of theta such that some divergence between px and p theta is minimized And this divergence now is a function of theta right Because if you choose a theta you will have one set of divergence So now what you have to do is that so this means write that down in English that set the


The parameters


of the neural network


Such that


The divergence


between px and p theta is minimized


Thats the meaning of argument okay


So choose a theta that would minimize the divergence between px and p theta Is this clear Now the next question that comes up is whatever you have been asking question


Give one


Data


D okay what is data remember that there are samples from PX


And


samples from p theta


samples from p theta How do we have samples from p theta They are simply the output of neural networks


Output of neural network D theta see output of neural network D theta is nothing but samples from


E theta right


Given data which are samples of PX and samples from P data how to compute and minimize


compute the divergence the next question you understand this right so now let me just tell you again so in the setup remember the setup the setup is the following that we have a neural network


theta of z okay and z is a random seed from from normal distribution and we have samples from x cap right and this has a distribution p theta we also have data that are some samples given some images given from px okay we should note that both px and p theta are unknown


These two are unknown but but samples from


From px and p theta are available


Okay so you understand this now This is actually the most important thing because this is the one that bounds the entire space of generative models that you dont know the underlying distributions but you have samples from those distributions Samples from PX the true data distribution is known because that is the data that we have Okay samples from P theta are also known because we can generate


as many samples from p theta as we want because what do you mean by generating a sample from p theta let me just say samples from


Samples from PX is simply the data given data


given data D now samples


from P theta how do you get that

speaker_2: sampling choosing different z

speaker_1: Correct choose


Different Z


Pass them through


g theta of s you understand so now we have samples from px samples from p theta now the question is given samples from these two distributions p theta and px how do we compute the divergence metric and of course why do we have to compute the divergence metric because only when we compute the divergence metric we can minimize it right i mean we can use gradient descent or differentiate it and then optimize for it first we need to compute the divergence metric between px and p theta given that we dont have access to px and


data but we only have access to its samples Now 70 percent of this course will be taking answering this question in different ways that given that we have samples from the true distribution and the generated data distribution how do we compute a divergence metric between those two


Okay so please try to appreciate and understand the problem We have the distribution sorry sorry sorry sorry We dont have the distribution we have the samples from it Now the entire statistics right and the machine learning and the other statistical series they ask this central question The central question that is asked is that if you do not have distributions but you have samples from it how do you compute something Now in this case we need to compute


divergence metrics right In some other case you know you might need to compute the moments you might need to compute some integrals etc depending upon what the application is But one of the central questions in statistics or probabilistic machine learning is that if you are given samples from distributions without giving the actual distributions how do you compute some things involving the distribution That is the central question I mean in our case what we should do please dont forget the storyline Storyline is that we are interested


in generating samples from p x Now to generate samples from p x what we have done is that we have taken an arbitrary random variable and we have a function g theta Now we know that passing an arbitrary random variable through a deterministic function will change the distribution of that function Now we need to set this function g theta such that the output of this function g theta will be a random variable that has the exact same distribution as that


of the input data Now how do we do that By minimizing the divergence metric Okay To minimize the divergence metric we need to first compute the divergence metric Now the question now is that how do you compute the divergence metric between two distributions which are unknown given that we have samples from them


Even data and samples from P data how to compute the underlying development metric


Is this clear so far Any questions here Okay I see some hands raised Kartik

speaker_4: Yes sir So I have a query So we set about when we have samples of RK then we get the sigma algebra using like L1 L2 all those parameters right

speaker_1: Ive never used the word sigma algebra here

speaker_4: Sorry

speaker_1: Very

speaker_4: Yeah sigma of what we wrote right

speaker_1: Design a neural network okay you start with a k dimensional vector and you keep increasing the dimensionality till you go to d dimensional vector yeah

speaker_4: But so we dont have any control over whatever is written in RL1 RL2 other than our input right So these are fixed Thats what we are saying right now

speaker_1: dimensionality are these are hyperparameters no L1 L2 L3 are hyperparameters that you fix


But you fix other designer


So when you say see when people say that its a billion parameter model it is some you know 70 billion parameter model what are they saying They are referring to these L1 L2 L3 So thats a design choice Okay

speaker_4: Yeah sorry sir but what I wanted to know was what are the whatever is the value of omega one or like omega two

speaker_1: Im sorry


Uh

speaker_4: uh those things are no w1 w2 sorry uh w1 w2 those things are not in our control right away right other than the

speaker_1: No no no okay okay so have you tried a neural network before

speaker_4: Yeah in pictorial forms only sir

speaker_1: Okay see how do you drive a neural network You start with some random initialization problem W1 W2 W3 W4 okay

speaker_4: Okay

speaker_1: And then solve this optimization problem So now you start with some W1 W2 W3 W4 and then you know you keep on changing these W1 W2 all these parameters till you reach a point where your objective is optimized Thats okay try new approach

speaker_4: So not just said we will be trying with variable various values from W1 W2 also like we can change

speaker_1: All we change are W1 W2 W3 W4 only no Thats the only thing that we would change nothing else

speaker_4: Okay yeah

speaker_1: When we solve this optimization problem that we have we have written here what I mean what do you mean by optimizing over theta optimizing over theta actually means setting up these Ws you know

speaker_4: Okay so the final

speaker_1: Do all the fighting

speaker_4: The final changes will be in uh w1 w2 w3 w4 whatever is the value

speaker_1: Of course right I mean when you optimize over theta you want theta star what is theta theta is collection of all w w and w 3 w 3 all the parameters of the neural network what you change are the see learning or training of a neural network is nothing but changing the parameters of it thats why Im asking you right okay uh here is a a small request the next class uh you please study about you know uh what do you mean by training the neural network


I mean I I assume that all of you know what training a neural network is


See I told you that the first four chapters of that Ian Goodfellows machine learning book deep learning book is a prerequisite Did you people go through it


And did you go through it Did you go through training neural network general backpropagation and so on

speaker_3: just started like first two chapters are random process and linear algebra

speaker_1: Okay okay

speaker_3: Im going to move

speaker_1: Yeah so please you know quickly ramp up See now we have sort of come through the come through the meat of the course okay Like I expect all of you to know what training neural networks mean So please go through those chapters and that those are actually sort of very strict prerequisites Otherwise see I cant teach how to like training neural network in this course you see So please have a look at that


Okay are we ready

speaker_4: So so when we look at the KL divergence formula

speaker_2: The clear divergence

speaker_1: by the way no no i mean like yeah clear divergence is one of the multiple possible divergences i will define now a family of divergence metrics okay okay that will be minimal now but anyway you go on okay clear divergence is one of them

speaker_4: Why did we get different

speaker_2: Yeah my question was so you can can you really in that formula it is like there is a closed form form of two probability distributions

speaker_1: But in this setup that youre not given

speaker_4: But in this setup that youre not doing

speaker_1: No even in KL divergence see what is KL divergence between Px and P theta Let me write that down KL between Px and P theta is given by integral of Px evaluated at x log of Px evaluated at x divided by P theta evaluated at x to integrate this out This is the definition of KL divergence right

speaker_4: Right yes sir

speaker_1: Now you dont know P x you dont know P theta

speaker_4: Great yeah

speaker_1: And how do we compute this That is the whole question

speaker_4: Okay okay okay

speaker_1: The question is that when we dont have underlying distribution density functions but we only have samples from it

speaker_4: Hopefully

speaker_1: Do we compute the divergence metric is the whole question

speaker_2: The another question is


Any such metric how can we have parallels for a single point for a single sample at a time

speaker_4: In the sense like

speaker_1: So none of the metrics none of these metrics are doing I mean like theyre theyre theyre theyre they are at their point wise

speaker_4: Okay theyre like a group of examples

speaker_1: Like a group open

speaker_4: We will see no I okay

speaker_1: so we will see no i have okay okay okay see how do you compute these divergences when you dont have distributions and only have samples is a question that i have not answered it i will answer it in a while okay if you have questions on the setup ask me


Okay so these are things that Ill discuss in a while so any questions on this setup

speaker_4: Okay no

speaker_1: Okay yeah Aamir up

speaker_3: Yes sir I have a question on the last statement So samples from P theta choose different Zs and pass them through G theta Now Z is a random variable which you are passing through a neural network So my question is why do we have to pass different Zs random variable being a function if we pass a different point belonging to the range space of random

speaker_1: Yes yes that is what we do when we say different zs thats exactly what we mean to sample from the range space of the random variable and then cost always that see whenever I say that there are points from random variable they always mean that its from the range space of the random variable

speaker_3: Always okay

speaker_1: I think we settled this we settled this in the first class itself right I told you that I say that when I say that there are we have n samples from a random variable I said that they are always I always mean that there are n samples in the range space of the random variable with a distribution I think that we have settled no

speaker_3: Yeah that is subtle I was I thought that since youve written choose different zs I thought you were choosing a different random variable altogether

speaker_1: I need an SOS message


No yeah Okay Uh


Is that okay Shall we move on


Okay so now the important question is right how do we compute this divergence metric when we dont have distributions but only have samples from it Okay before we take that question let us


And by the way Ill tell you the answer is through this adversarial optimization This entire generative adversarial network right or adversarial optimization it is asking it is trying to answer this question which is that how do we compute the divergence metric between distributions and we do not know the distributions we only have samples from it This adversarial optimization is one way to do it by the way And like variation


inference is one other way which will give rise to VAEs and diffusion models okay so adversarial optimization is one way the variational inference is one other way and MMD is one other way and so on we will look at different ways of doing it a maximum likelihood estimation is one other way which is what is used in uh the LLMs and so on we will look at uh all I mean all possible ones one by one okay that is what we do in this course we do in this course okay so let us look at adversarial optimization


And for that lets take a


Now let us let us define define


A family of divergence metric first


And this method now that we will look at right now is is powerful enough to uh to be able to uh handle a large class of divergence metrics okay its a common thing okay or rather its a its a method that would enable minimizing the family of divergence metrics you know not one divergence metric it will uh it will uh enable us to minimize a family of divergence metrics okay


Now for that let us first define a family of divergence metrics so given two distributions


one two


probability distributions


Let us let me just uh work with the density function given two density functions


density functions px and p theta okay


Define


Divergence


Weve also Ive already seen one divergence metric no in the last class which was the Hilbert Libert divergence We will I will define a large class of family of divergence metrics okay All of that can be minimized using the technique that we will see in this class okay Thats why Im defining a large class of family of divergence metric even to energy function p and p theta define a divergence metric as follows


point to the task df between


B x and B theta


defined as


Integral


P theta f x


fals


P x of x divided by P theta of x


beams


This is the definition of a gradient square F


of view is a function that takes


a positive real number and maps it to another positive real number It is a


Convex function


Well explain it in a while


Okay so these are called F divergences


Okay Okay So let me explain what this is Now suppose we are given two density functions and we want to define a divergence metric between them What is a divergence metric Remember that its a it will give you a sense of distance between two density functions right Now


There is a class of density functions that you can define which are called f divergences which are which is defined like this So this is the definition of f divergence Okay What is it It is you take it is integral p theta of x f of px by p theta of at dx Okay Let us look at this this term that is inside this bracket Now you know that the density function px of x is a scalar


Correct Density function is a scalar valued function in the sense that it will take a vector x and it will give you a number a positive real number right So all of you know this right What is a density function Density function is a scalar valued function Okay So now if you evaluate the density function px at some x you will get a scalar And if you evaluate the density function p theta of x you will get another scalar So ratio of these two


Px by p theta at a given point x is a scalar


Correct Now this function f of u takes a positive real number because the ratio of these two density functions is a scalar It takes a positive real number and gives you another real number r That is this value f of this ratio is this value And the definition of f divergence is the integral of p theta of x times f of px of x by p theta of x dx integrated over all values of x This is the definition of what


It has no more got muted This is the definition of what is called as a called as an f divergence Now you can choose an f function OK Ill give you examples So now if f of u


The results


u is a what is u here u is px by pt topic okay its a scalar here ive just given written that as a dummy variable u but in the definition it is the ratio of the density functions if f of u is equal to log u okay then the corresponding divergence is called the kL divergence


Now with f of u is equal to lets give you some examples of it


Sorry it is u log u Sorry if its u log u then it is that If its uh


half of u log u minus u plus one


Log


u plus 1 by 2 this is called the Jensen Shannon divergence


If its um


half mod u minus one then this deviation is called the total variation distance


and so on Okay So now you can choose any convex function for this f and one choice for this convex function will give you one divergence metric So basically what Im doing is Im defining a family of divergence metric Okay Which is like one of the I mean you can choose a convex function and you get one family of one one divergence metric So what do you mean by this If I write u log u here what will happen to f divergence Let me show you that example


example okay now f divergence is given as integral p theta of x log of sorry f of


of p x of x divided by e theta of x dx correct now let us say that f of u is u log u okay now in that case df will now become integral e theta of x to substitute u log u for f of u which is


Now this this entire thing which is right inside this f is now called as u this is p of x


P x of x by p theta of x this is u correct into log of u


p x of x divided by p theta of x Note that this entire thing which I have written as f of


D x of x y d 3 top x correct This is what it is for d x


Oh


I will skip the algebra okay So if you simply this is a times log ratio right So now you just take the ratio inside and so this okay so this p theta x and this p theta x cancels This will be


P x of x times log of P x of x divided by P theta of x V x okay which is nothing but the kL divergence


Understood Thats what it is right So what we are doing is that we are defining a general family of divergence metrics Now if you take where these are called f divergences If you take some form for this f function that is there in the definition of f divergence you will get different divergences You get k divergence with one f You will get Jensen Channon divergence with one other f You will get total variation distance with one other f and so on So basically we are defining an


Infinite family of divergence metric between two distributions depending upon what your function is


The reason I did it is why what is the what is the uh the coherence or relevance to this is that the adversarial optimization technique that we see you look at what we are doing right we want to know


minimize or compute the divergence metric given samples from two distributions right now what divergence metric are we considering we are considering not one divergence metric we will be giving you a a a tool or a technique that would compute and minimize a family of divergence metrics that are called f divergences you can choose any divergence see if you people know this generative adversarial networks or gians when after this paper came there are so many improvised


that came over it no thats called f i mean like l is given x squared again like you know there is some w again this again that again all that they are nothing but changing this f divergence thats all so you take one definition for the f divergence you will get one again so what we are what we will see right now is we will not look at one minimizing one divergence metric we will now look at minimizing a family of divergence metric given uh samples from the underlying data distribution


Is this clear So now any questions on the definition of f divergence So basically what we need is given a given some convex function f a scalar value of convex function f we can define a divergence metric between pair of distributions


Okay and k divergence happen to be a special case of this and Jensens and divergence happen to be a special case of it and total variation distance will happen to be a special case of it and so on So every there is a lot of very very well known divergence metric in all special cases of these f divergences Okay in general at an abstraction level this is you think of it like the definition of a class right I mean where each of these divergences are one instance of this class of divergences called f divergence


business


What we will see now is that given the samples from the underlying distributions how do we minimize any F divergence between those two using samples Let me write that down Now the objective I will take questions in a while


Cool


Viewed


compute f divergence okay


doing


extremely okay


You


samples


given samples


Without


knowing what px and p theta are


We have we dont know P X and P theta but we have samples from P X and P theta now how do you compute the M divergences between them is the next question that we will answer


Okay uh any questions here


Uh

speaker_2: She wont

speaker_1: Four

speaker_2: Yes

speaker_4: Yes sir on the F divergence side as we have said we can have infinite combinations of F divergence function and

speaker_1: No no no no there are there are no combinations here you can have infinite f divergences by changing f

speaker_3: Yes Yes So yeah but we are talking about the three variations the KLI divergence GS divergence So is there any specific benefit does they bring into the table or

speaker_1: Good question Yes they do They do In fact Ill


After we look at how to minimize this now I will tell you like advantages and disadvantages of lets say at least scale and density channel divergence okay


But yeah so different divergences have different properties Thats a good point that you made Why do we need so many divergence metric Why cant we look at one of them is because different divergence metric offer different properties I will talk about it right I mean just after we look at this algorithm right Remind me if I forget it just remind me to bring out the lets say properties of at least one or two divergences here

speaker_2: Thank you

speaker_1: But yeah so thats the point I mean why do we need so many divergences In fact if you come up with a different divergence which has good properties you can name it C1 divergence Thats how people have done it Different people have come up with different divergences and called them with their own name But you will have to ensure that these things are there You will have to ensure that this is a convex function to be mathematically precise This is actually a left semi continuous function


left semi continuous function and also f of 0 has to be equal to 1 So convex left semi continuous functions are with f of 0 equal to 1 So if you can come up with such a function that becomes a new divergence metric and if it has favorable properties you can use that in your generative models


Put that back in the room


Its just that it should

speaker_4: Its just that it should

speaker_1: no we are not doing argument here anything right i mean it is optimized uh we do optimization over dfs we minimize the divergence metric no we dont we have nothing to do with f f is a f is actually a hyper parameter right you fix s yeah yeah okay choose an f divergence it has nothing to do with the optimization


It is just a definition of for the F values


Any other question here


See in practice what we do is that we actually fix an F So I mean for instance in the naive vanilla GAN paper right they choose this F to be equal to this particular F I wrote it no this particular F This is this this thing


is what they do in the nice vanilla gan


They take Jensen Shannon divergence in the the vanilla generative adversarial network they choose this f to be equal to this particular form and they may what they minimize is the Jensen Shannon divergence okay


You choose it you actually fix it you fix that you fix that uh f divergence uh and then compute and minimize uh to find a sample


Is that okay


Im not there


Yes can I hear you

speaker_2: Yes yes yes

speaker_1: Okay any other question on the definition of


this needs uh an uninterrupted to answer this question right you know we need


40 45 minutes of uninterrupted time maybe lets just take a break uh and then get back shall we


Lets take a break now Its 10 55 in my clock Lets resume at 11 15


I see you in about 14 20 minutes


Hello shall we resume

speaker_3: Yes

speaker_1: One of the most challenging parts of this online teaching is that I dont get to see you at all right I mean I all I get to see is this stupid screen and as a as a teacher Ive been we would have developed this ability to look at the face of your audience and kind of mostly discern what is going on I mean are they appreciating what you are saying are they understanding what is said you know when to repeat you know when to stop


not to repeat etc the complete feedback mechanism is gone now here it is only me talking dont even know whether the people exist or not yeah its such a challenging thing to do that online anyway okay i see a couple of hands rise uh yeah ask it

speaker_3: Uh so so you mentioned some properties about this f function for f divergences can you move a little up

speaker_1: It should be convex lower semi continuous and at zero it should evaluate to one

speaker_3: Uh but this is not uh uh following in this uh these three functions that we write right this F zero

speaker_1: Hold on I think I just thanks

speaker_3: It should be I think F one is a good one

speaker_1: F1 and F2 correct correct Yeah thanks Yeah roof top correct its correct It should evaluate to zero at one correct thanks


Okay shall we continue


Okay see as I said no the goal is now to compute this divergence between a pair of distributions when the distribution is unknown and samples are given So here is the overall philosophy of how it is done As I said no this is a recurrent theme that comes up in almost all the ML models How is it done is the following Now observe that these F divergences right are any divergence metric Now involves let me not write the F


So suppose you have lets say an integral okay


need to compute an integral of lets say some function running out of alphabets its a statement b statement h okay lets say some function h with respect to some probability density p x p x okay if this integral has to be evaluated okay now lets say that we need to evaluate this integral


Im gonna do like this


Okay with


PX unknown clear


I have samples from DX


Okay now suppose you need to evaluate this sort of an integral okay where h is some function h of x is some function any function okay some function of x You have some function of x and you need to integrate evaluate this integral with px unknowns If you dont know px then you cannot of course integrate this out right Now one statistical tool that can be used to do this approximately of course you cant evaluate it exactly


because you dont know what pH is but it can be approximated how there is this nice theorem called law loss large numbers it would say


Right last last number says the following suppose


X one X two


to xn okay are sampled from some ps and then then to compute some


Right then


Integral


effects


DX DX


can be approximated by


limit of one by n


I is one through yen


h that is evaluated at xi where xi are samples from


This is a very strong and powerful result What are we saying here Please note this Now n goes to infinity So we are saying suppose you have lots of samples drawn from a distribution Okay Then if you want to compute this sort of an integral that can be approximated simply by taking the sample mean of all these functions I mean all the sample mean of


the function values evaluated at all those x is coming from v x Now a special case of this is maybe something that all of you know right if h of x is simply equal to x then what happens then what is this


What is this thing called this is

speaker_2: Expectation

speaker_1: This is the expectation of


This is the expectation of X right Now in fact this is the expectation of H of X with respect to this density pH Okay this is the definition Now this is the expectation of X with respect to pH Now this can be approximated using


This all of you know now This is what we do in practice isnt it If you want to know the expectation of a distribution you just take the sample mean What is this This is the sample mean


Sample mean approximates the true expectation asymptotically which means if n is n n goes to infinity we have enough number of samples then sample mean can be approximated Sorry the true expectation can be approximated using sample means All of you know this right This is called law of large numbers


Any questions on this


Hello am I audible


Okay now yeah so why did it so basically what did I say here that you dont have what did we do here Look at this no We have integrals I mean this integral is nothing but the expectation of


definition of the expectation of some function h of x with respect to px if you want to compute the expectation of a function with respect to some distribution okay without knowing the distribution but you have samples from it you can invoke large large numbers and simply compute the sample average okay over all the samples that are coming from the distribution see please note this very carefully while we do not know what the


distribution p xs we have samples from them that is exactly the scenario that we have right now with us no we we have samples from the distributions we dont have the distributions but in spite of not having the distribution we can evaluate expectations of functions of random variables with respect to the underlying distribution using sample averages


Is this clear is this idea clear


Okay now lets come back to what we had in our mind So we want to minimize the F divergence We want to compute the F divergence Now let me correct the dots If we if I can express the F divergence let me write that if


divergence can be expressed and be expressed


expressed in terms of


in terms of expectations


More


then then df can be computed


using


samples from


uh using um using device using two types


Yeah


Law


Large numbers


Okay what I am saying is we want to compute the F divergence between pair of distributions We dont know what the underlying distributions are but we have the samples from it Now we also have this nice result called law of large numbers that would say that the expectations of some functions with respect to some in underlying distributions can be computed using sample averages if we have samples from it Thats what law of large numbers says Now connect these two


so that if we can somehow express the f divergence or the quantity that we want to compute in terms of expectations over pH and pH theta then we can use law of large numbers and approximate the f divergences do you agree


is exactly what we will do now now the my goal is to now cool


is to express


divergence


in terms of


expectations


Or


X and


Okay thats what we will do Now unfortunately what happens is this is not possible You cant express the F divergence or any divergence metric in terms of expectations over P x and P theta Okay However however


We can express bounds on f divergence using expectations so let me write that


Okay so what Im saying I mean f divergence cannot directly be expressed as expectations over this but we can express lower bounds on f divergences in terms of expectations What do you mean by lower bound We compute a quantity okay which is always greater than or equal to f divergence okay then this quantity can be expressed in terms of expectations so expectations over px and p theta okay and then remember that finally


want to find a g theta okay or our generator function such that this f divergence is minimized right now because we cannot compute the f divergence what we do is we carve a lower bound on the f divergence which can be computed and we minimize this lower bound instead


Does that make sense But thats not an exact thing right I mean it would have been great if we can actually minimize the F divergence itself But we cannot minimize the F divergence directly because F divergence cannot be computed without knowing the distributions Now what do we do Instead of minimizing the F divergence we minimize a lower bound on that


Okay we minimize a lower bound or rather we minimize a quantity that is always greater than the F divergence right Yeah the F divergence we minimize a lower bound on F divergence And that lower bound can be expressed in terms of expectations over P x and P theta


Is this is it here


Any questions on this See these are very very critical and important stuff okay which is again as I said this is a recurrent theme that would keep coming so if you have questions here do ask me Ill wait for a minute


Now this implies that instead of


Minimizing up divergence


minimize


Lower bound


Any questions on this


So dont ask me how do we do it that is what we will see but yeah on the philosophy yeah somebody

speaker_2: That will be an approximation right

speaker_1: Correct correct that will be an approximation but unfortunately thats the best that we can do


Because you know that like the fundamental problem is that we dont have access to pH and p theta you see If we do not have access to pH and p theta this is the best that we can do


But yeah what you said is true its an approximation you will you will not get the the correct minimization of heptagons


Any yeah no case

speaker_4: Yeah So so if we are minimizing the lower bound does that mean it does not

speaker_1: All right so

speaker_4: Lets understand the Lord

speaker_1: Correct correct correct that is correct that is correct that is why no its better to thats very good question actually you know that is why we need a tighter lower bound

speaker_4: Shes not active

speaker_1: Right I mean the tighter the boundary is the better your model is We will crave to have a tighter lower bound See if you know what a GAN is right generative adversarial network you will have two networks there right One is the generator network that we already wrote There will be another network called discriminator network You are aware of it

speaker_4: Yeah yeah

speaker_1: See that is actually to carve this lower bound We will see that in a while So why do we say that the discriminator has to be very good is because the lower bound that we compute has to be very tight Otherwise you know it doesnt I mean it would be a very loose approximation which will not lead to a good generative model


But this is the best that we can do Why is this problem arising is because we dont know px and p theta Since we do not have px and p theta we need to do something What do we do We will carve out the lower bound on f divergence and then minimize that Now this lower bound can be computed using the expectations over I mean using the samples of px and p theta Thats the point


So the lower

speaker_2: So the lower bound is in terms of is for the term EPX minus EP theta right

speaker_1: It will take that form It will take that form of like differences in expectations That is what were going to show now Thats the whole result The lower bound that we carved now that can be expressed in terms of expectations over these two distributions that we have


Excuse me once we express them as expectations right over these two distributions we can compute that using samples


Excellent yeah


Any other question

speaker_4: Yeah sir Sir if you dont know P x and P theta as you have said we know the samples from it And above you have applied law of large number to find the expectations using the samples So why cant we just directly apply into KL while we calculate divergence Like we can apply the same tactic while finding the divergence as well right

speaker_1: what im saying you know these divergences for instance if you take this some like Jensen channel divergence right you cant express that in terms of expectations if you can express that in terms of expectations then great but you cant the whole point is that you cant write this f divergence this this f divergence right is that this definition of f divergence in terms of expectations over p theta and px if you can then thats it i mean its its an exact approximate exact


computation but you cannot represent that thats the problem because of that we need to do something what do we do we cause a lower bound on a dividend which can be represented as expectations right which can be


Computer yeah thats the whole point


Understand that

speaker_4: So just a small extension so we cant do it because its not a h of x right but it is its depend because if you see the form it is very similar to expectation

speaker_1: Not necessarily no you have f see it is not see h of x right it is not h of p of x you see this is

speaker_3: Yeah exactly

speaker_1: Yeah so there is there are there are ratios of densities here right This cannot this is not equal to for instance expectation of f of that with respect to p theta This is not equal to that Understand

speaker_4: Because the it itself depends on the PN

speaker_1: has a dependence on p and p theta it is not equal to the expectation right we need to do something else to write it as an expectation of functions over these two distributions the way to do it is to carve a lower bound on it and then express that as uh expectation which can be computed

speaker_4: Definitely

speaker_1: Anything else anybody else


Okay now yeah as I said now the classes now will get a little denser So please focus and know as much as possible and remember whats going on Otherwise you know its very easy to get lost I mean there are too many things that we will do right I mean unless you know what the storyline is you will kind of


lose the track please focus okay so now what is what should we do we should now carve a lower bound right or let me write that expressing


Bounding BS


express in it in terms of expectations


Explications


Okay this is what we will do now


Let us start from the definition of f divergence f divergence between x and p theta given as integral


ETE topics


has computed it


ratio B x and B theta


Next


Okay this is the definition of divergence


To do this well have to know what is called as a


conjugate


conjugate of a convex function


Great


Now remember what we are doing we are trying to bound the f divergence and express it in terms of expectations to do this we will start with what is called as the conjugate of convex function now the thing is if f is a convex function


Next one


We call it f of u because its


It is a scalar valued function that we are talking about here right in the f divergence convex function


There it exists


There exists convex conjugate


Convex conjugate function


f star of t note that both u and t are dummy variables okay simply some variables star of t defined as follows


F star of T at a point T is given as the maximum of


mu t minus


sauce new


f of u okay this maximum is over u which is the domain of f


I will explain what this is


So what we are saying is that an every convex function f okay has what is called as a convex conjugate okay Now what is convex conjugate It is another function f star of t okay that is defined this way f star of t simply f star of t at t is simply the maximum of u t minus f of u where u comes from domain of f What does that mean Let me just draw it and show you Lets say that you have


some convex function let us call this f of u this is a convex function right and this is axis is that this is the u axis and this is f of u okay now lets say that you take a point here some point on the u axis let me call this u okay now what i can do is i can construct like i can i can write


Multiple lines


Right


all of which are less than


F of you at that point do you agree


So given a convex function okay I take a value of that convex function at a point I can construct infinite number of lines okay I can draw infinite number of lines that lie below that point okay for all u Do you agree


Okay so out of those all I mean there are infinite lines that I can draw right Out of all those lines there is also this line which is the tangent


is also the tangent okay uh that that is equal to the value of that uh function at that particular point okay now the this is this point right i mean the the intersection of that tangent and this particular curve is what ive called as maximum you look at this ut minus f of u okay for different values of t represent okay different values of u different values of


p represent all these uh lines that I can write at every point of the convex function


Let us take one point for instance If I take one point of this convex function there are multiple lines that I can draw to this curve at that particular point which is represented by this family of lines Now amongst all these possible lines if you take the maximum value of all these possible lines at that particular value of u what do you get Its actually the value of that tangent to that function at that point


That is the value of that convex conjugate at that t


You get it

speaker_2: Sir one question

speaker_1: Its actually not the tangent right its actually the slope


that particular point now if you collate all these at different points of view you get another function right its a collection of slope of this function at all points that becomes the

speaker_2: Sir one question


Sir its basically the function value f of u right Even if we are denoting we are getting that through the tangent the maximum value will be f of u only

speaker_1: No no maximum of maximum of ut minus f of u Thats what Im saying Not f of u

speaker_2: Oh okay no Im what Im you are explaining about this this concept right Like we can have infinitely possible lines at a particular you one of them will be that

speaker_1: Okay no I


So that are that are that are less than this at all points right

speaker_2: Got it got it

speaker_1: I thought less than that at all points So now Im considering out of all of those possible lines Im considering the one that has the maximum value of that particular u and that Im considering as the value of that conjugate function on that particular p

speaker_2: So that value is corresponding to f f star of t like that

speaker_1: That is that is the value of correct that is the value of s star up t at that particular point


See ut I mean f of u is a what does ut minus f of u represent f of u minus f of u right this f of u is the


Something happened


Yeah hold on this f of u is the intercept right


The given point is f of u this is this is like mx plus c isnt it

speaker_2: Yes sir

speaker_1: This is the intercept okay Now you see I mean t is the slope and u is the value of the domain at that point So basically ut minus f of u will give you a line


At any f of u ut minus f of u will give you a line okay whose intercept is f of u


Okay

speaker_2: Okay

speaker_1: Now Im saying out of all these possible lines that are less than the function value at that particular point Im looking at that line which is maximum


Do you understand


Oh yeah

speaker_4: So it lead to one confusion that the distance should be minimum right like the value at f of u and ut minus f of u the line which you have it should be very close to f of u to get

speaker_2: tighter bond right so it should be the line should be the minimum of it

speaker_1: the maximum value of the value no the maximum value of that function see we are looking at the value of this function itself for this u t minus f of f f of u is a value that evaluates to something

speaker_4: My duty is

speaker_1: So looking at the maximum of that and the maximization is over all possible u see the optimization is over the u domain you look at all possible us here


Okay so amongst all possible us you look at that u which will maximize this entire thing ut minus f of u


Fix a t okay fix a t so what do you mean by fixing a t see you can you can see t as the slope okay you see t as the slope you fix a slope you see you fix a particular slope maybe the way I have written the figure has a different interpretation okay let me rewrite it hold on


Is it not warm


Let me draw a comment again


This is a convergent function Let us take one particular u okay from here


the axis


P is the slope and


F of u is the intercept right


Minus f of u is the intercept so this is


This is F of U


minus f of u should come the other side


that is the intercept term now


you are looking at maximum with respect to you


Such the function t is the slope Now this is you can write


this is 1 t okay with that that has the intercept you can write


Go to that now


another line and this is


straight lines theres another line theres another line and so on these are the lines that we are talking about is this clear i think now it is correct

speaker_2: Yes yes sense

speaker_1: yeah these are use correct yes amongst all these possible lines i am looking at that particular line okay which would maximize that at that list this is the u that we are talking about


Okay so amongst all possible lines okay that would be a lower bound for this function at that particular u I am looking at


which would maximize the resistance value U t minus F of t


Is that clear

speaker_2: Yes sir

speaker_1: By the way it may not be a tangent though at all times it may not be the tangent


Okay


So this okay so youre not seeing the entire picture


So these are multiple lower bounds that are possible for that for the convex function at that particular value amongst all possible lower bounds we are looking at that possible in that line okay that would maximize this


Are you clear on this Any questions

speaker_4: So the quantity which we are maximizing can you show it on graph

speaker_1: U is fixed U is fixed or

speaker_4: Thank you guys

speaker_1: And yeah u t minus f of u is the line no This is one u t minus f of u Lets call this t1 This is like u t2 minus f of u and so on right Amongst all possible lines we are taking that line which has the maximum value


At that you at you


at u this line has this particular value right at u this line has this particular value and so on I can construct more such line you know which becomes lower bound if I construct another line you understood right different lines have different values at that u so now amongst all possible lines I am taking that line okay which has maximum value and the value of that line at that particular u happens to be the value of the conjugate at that t


Yeah does it make sense now

speaker_4: Is it the value of u that maximizes uh u of t minus f of u

speaker_1: minus f of u correct or a given or a given or for a given

speaker_4: For a given for a given for a for a given value of t right


You choose a t and then find the maximum of u uh f uh find a u that maximizes ut minus f of u

speaker_1: That would be the value of m star of t at that particular point okay


Its a point wise definition

speaker_4: So this is

speaker_1: So this is this has nothing to do with like you know divergences or anything This is just the definition of a convex conjugate of any convex function This is true for any convex function Okay Its also called the Fenchel conjugate Basically the definition of the conjugate function Okay Shall we move on


Okay now um


This has to be taught in a convex optimization course but its okay I whatever we need we will do it So now


So there is a property that would say that that f star of f star Ill state this without proof f star is also convex


star is also convex and so okay so first of all we say that f star is also convex if f star is also convex this implies that you can take the conjugate of the conjugate right because f star is conjugate now we know that every convex function has a conjugate which means that the conjugate also has a conjugate and the property theres a property that would say that the double conjugation of the function will take you to the original function


property that we will use okay so two things one f star is also convex which means that that also has a conjugate and that will take you back to the original function okay what this implies that


We have the original okay so f of t


was the conjugate for f of u right


Thats the right answer maybe


2T minus


f of u and this is over u right so now this is the f star of t this is the conjugate for f right now we can take a conjugate of the conjugate f star of t you take


the conjugate of the conjugate what is this this is equal to f of u we know that okay so conjugate of conjugate how do you write that it is simply to take the


domain of the conjugate okay


and subtract it from it


its conjugate which is when I subtract it with its value and this maximization is over T which is over you know f star


Do you agree


Simply taking conjugate of the conjugate What is the conjugate of the conjugate Conjugate is also convex So this is the conjugate of conjugate So this is


the conjugate of conjugate


We know that that is equal to the original function f thats why f of u is equal to over this


Questions on this do you agree


I have just replaced f of u with f star of u because f star of u is another convex function right We can write conjugate for any convex function f star is another convex function So I will write a conjugate for f star as well which is this it is this and this we know that if you take the conjugate of conjugate you get the original function Is this clear to all of you


Okay okay so now okay why do we need this Lets come back to our definition of our f divergence Remember that we are looking at bounding this f divergence okay Now this is integral


Right theres is


we call this as f of u dx where u


Sorry I think I wrote it incorrectly it should be P theta


Okay so this is a convex function which means that this f now I can replace this L lets say I use this yeah

speaker_2: Yes sir either the initial one should have PX or the and the last the last one should have PX because once we replace

speaker_1: I can follow


Theta x times f of p x by p theta right thats the definition

speaker_2: Once we replace uh Px by P theta we have

speaker_1: Speed of place


So we have a break

speaker_2: So

speaker_1: Just called it as this ratio I called as U thats all


Its a scalar no I just called it as a scalar U f of U

speaker_2: Okay okay

speaker_1: Nothing complicated right I just am representing that as some scalar right yeah

speaker_2: Yes sir yes sir

speaker_1: Now if of you we have this result right can be written as max of


u minus


Lets start off the


Maximization is over t correct this is what we have written here


But I will use that there which means that my f divergence now can be written as an integral


times max of T okay what okay Ill write it as T U minus S star of T


P x maximization is over t agreed


What did I do I just simply replaced f of u with the definition okay by using the conjugate of conjugate property


Do you agree


This is another problem with this online teaching that the screen is so small right I mean I need a large bold where see imagine I would have written this somewhere else you know you would have had the view of this Now you can appreciate that since I have written FRP using this max thing all I have done is I have replaced this FRP using this yeah using this definition


Is it okay


Is it

speaker_2: Yes it is

speaker_1: Now Ill just expand this this is integral p theta of x


So were A


Now t times what is u u is ratio of vx by e theta


this


star of P


Correct Yeah Now look at these terms Look at these terms Okay Ill write it as three times


times this now look at these terms if i can somehow take this max out of the integral


Okay if I take the match term out of the integral what will happen


Can somebody tell me what will happen


If I take max yeah if I take max out of the integral then it will be t times px minus the integral of so it will be like this now somehow take the max outside okay it will be integral


P theta P theta would cancel out it would be


P times X of X DX


Correct minus


Integral


star of T times


ET topics correct do you agree


Can you see that


Can we take that

speaker_2: X out

speaker_1: are hold on Im just saying if you can I mean you cant I will tell you how what happens if you take the max out but if you can lets say right then it will become like this now this is an expectation right over px and this is an expectation over p theta you understand that thats all now all this exercise that we did right in representing the f function using its conjugate all that was to ensure that we can somehow write the x


these in terms of expectations Now we are almost there We just have to somehow push this max out And if we can push this max out then we achieve whatever we want that we can write our F divergence in terms of differences in expectations over P x and P theta which we know how to compute And you see the point


Now the question is how can you take the max out


Right So max is over a T how can you take the max out is the question


So that needs I need some half an hour to complete this proof now So what shall we do


We have uh

speaker_2: Sir we have time until 1215

speaker_1: will obtain ten more words


minutes might be lesser to do this anyway i will quickly run through it and do it again in the next class perhaps okay


Any questions so far


Does anyone have any question Okay no okay now okay so let us observe this entire thing


So this is a maximization


Okay well what


Can you see that this is a maximization over t okay however however


So let us call this uh maximization over okay maximization of let me say that of


an objective function okay


objective function let me call that function as capital T can of a function T over T do you agree so this I mean whatever I have marked using flaw bracket right it is a maximization that you are that you are that an optimization that you are solving over T as the variable and if I call that entire function that you are optimizing using the capital T


Okay then its you are maximizing capital T over the variable small t Do you agree


Or I can use a different notation for this capital D you know because Im using small d capital D it might confuse which letter


was a lot of alphabets


U is taken


Okay well call it B


capital V This function capital V okay we want to optimize okay what is V by the way


v is equal to t times


x of x divided by h theta of x minus f star of t correct This is what I have called as v Agreed Its a maximization of an objective function v over t All of you see that But observe this that this v is actually a function of x as well


But I should say that its a function of both x and t


Its a function of x and t its also a function of x agreed


Now what you are actually doing while you are computing this integral is this following You first solve this optimization problem over t Okay So now what you do is inner


optimization problem so now first you do solve this optimization problem you get a you get a lets say


the star okay which is the maximum


of this function v x comma t over all t okay now you plug this t star here and compute this integral and do it for all x that is what you are doing when you are computing the integral


You first solve the optimization problem with respect to T you get some some


value for that optimization problem now you take that so now observe that this t star okay is also a function of x


Do you agree


Obviously right because if v is a function of x then t star is also a function of x because we are only solving we are only taking the maximum with respect to t and given a particular x you will have a different maximum correct


Let us represent that maximum using some capital D star of x


Correct Okay Now what are we saying here that there is an optimization problem There is an optimization that is happening with respect to t Okay Now that objective function for that optimization problem is a function of x Now given an x you will have a particular maximum for this maximization problem You compute that maximum and then you integrate for all x That is what your f divergence is Agreed


Now now what I can do is suppose I take the maximization out and write that whatever is there you know p theta of x times


theta of x divided by x of x minus


instead of the


Suppose right I take this


Replace this with


See star of X


It is the maximum of

speaker_4: So that way px by p theta right t star of x into px by p theta

speaker_1: Is it px almost made this mistake yeah its px by p data sorry


Now suppose I replace this you know this t right I solve this optimization problem and replace it with t star of x Then its okay no Both the integrals are okay I can take out d max Do you agree Because Im solving the optimization problem in EMA right At all points in x Im taking out Im finding solving that optimization problem


Replacing that t with t star of x correct Thats okay no


Do you agree what I am doing here at all is I am simply solving the inner optimization problem and putting the solution for it and then computing the integral


Great now


This t star of x basically lets say that okay its a function that will take a particular value of x and gives you what a real number isnt it A real number which happens to be the solution solution for the optimization problem


No optimization problem


But what should be this t star of x b t star of x is a function that would take x you give it an x it will give the solution for the inner optimization problem correct


Thank you everybody


This T star of X has to be this right you look at this by definition it should be a function that would take an X and gives you the solution for the optimization problem


Okay now


Any questions so far


Okay now instead of T star okay instead of T star


Okay before that let let let script be


This is a different symbol okay its denoted denoted


A class of functions


of functions okay


Bottom


to R Basically what I am saying is let capital let script T this is script T okay let script T denote a class of functions from X to R okay which means that this T star of X T star of X is a member of capital T okay


star of x is one member of capital T which means that it is a function that would take x and gives you a real number which is a solution for the inner optimization problem at all x okay but scripty let scripty denote all possible functions that will take an x and gives you a real number okay now if I cannot


Let me write that integral down and then I will tell you this fx


t of x minus


is t what is that e theta


Thats the second term


ETOPICS times


B of X times


theta of x by x of x minus f of the f star of the f star f star of t of x

speaker_2: So P x of x divided by P theta of x

speaker_1: Every time I make that mistake


Now lets say that let there is a Tx okay which is not equal to p star of x okay


I replace this with this so this suppose suppose


T x is another function okay that belongs to script t and I replace this t star of x by t of x What do you think okay will be the value of this integral compared to


disintegral and somebody tell me


You understand instead of having t star of x which gives me a solution for the inner optimization at all points of x if I replace that with another function t of x what would that be

speaker_2: It slightly be smaller than the previous one

speaker_1: will be smaller do you agree


It will be this will be this will be greater than or equal to


Or this is our f divergence this will always be greater than or equal to f divergence


Because


It will be either equal to d of x or less than d of x Theyre not equal to d of x

speaker_2: Sir other way around right we like t star is corresponding to the maximum value

speaker_1: Max p star is corresponding to the max so this is lesser and rp everything here all of these are density functions that are positive so p is p is lesser p can be lesser at all points which means that yeah its the other way around should be you know


is that this is greater correct so lower bound no correct is that okay

speaker_2: Yes sir

speaker_1: Its correct now this integral is over x Now now I can say that dx is greater than or equal to the maximum value okay that you can get


out of all Tx that belongs to this class of functions of this particular integral


lying this


This is P x no because e theta would cancel out


Temple


E theta X


BX BX


Is this a do you agree Why have I written a max here The reason I have written a max here is that if you take the max of all possible functions in this bucket of functions okay your f divergence will be greater than or equal to that Now if you can find a function with the bucket of all these functions that is equal to t star of x at all points then it is exact The f divergence will be exactly equal to this integral right


okay now if you cannot find a function okay that is equal to t star of x at all point at least find a function okay that will give you the maximum value at all possible x amongst t if there can be lets say that there is one t of x there is another t2 of x there is t3 of x and all that right lets say that none of these are equal to t star of x okay however i would choose that t okay amongst t1 t2 t3 t3 okay


That is maximum of all this correct Of course I need to choose the maximum because here the inner optimization problem I am actually looking at if you look at the definition of T star it is actually the maximum of this objective function with respect to T Now if I cannot find the maximum


I mean at all points


Rather if I cannot find a function that will give me the maximum at all points I would choose the function amongst all possible functions that are there in this pocket of t I would choose the one with the maximum value


Do you agree


Thats all we are done I mean I will reiterate over this the next class So what we basically did was we expressed this expectation okay sorry the f divergence we carved a lower bound on this by saying that you choose a class of functions okay from a bucket of functions this is equal to what is this first term Its pretty obvious now This is an expectation of p of x with respect to p x okay minus this is an expect


of sorry this should be


Nobody corrected me this is S star of T of X


Let me call this x cap because when you write expectations no its better to write a different w variable This is x coming from px This is the expectation of x cap coming from p theta


Thats all This is the result But this is the last function in AGAN If you can if people know if you can relate now this is exactly the last function in AGAN I will we will see that in detail next class Thats all We are done So now we have re expressed So basically what we have done we have expressed


expressed


the lower bound on H divergence


on a divergence in terms of


expectations


or unknown distributions


This is the goal right We have achieved our goal So now we know how to compute do we know how to compute the first term We do log large numbers because we have samples from p x Do we know how to compute the second term We do because we have samples from p theta Now if you observe this entire thing now will become a function of theta right Because this second expectation is a function of theta Now you dont forget what we have been doing right We have this network d theta whose parameters are theta We are giving the random


z okay this x cap the output of this is called as p theta and we have a lot of samples from p theta and thats what we use to compute the second expectation we use our data to compute the first expectation and then we optimize this using Gaussian which we will see in the next class but for todays class what did we do we wanted to minimize the up divergence we could not because we dont know the underlying distributions the goal was to represent the unknown


divergence are uncomputable divergence measure in terms of expectations over underlying distributions because we know how to compute expectations using laplace numbers we invoke the property of convexity and conjugates to express the the f divergence in terms of expectations over underlying distributions


all we did so far okay so before coming to the next class as i said no that things are getting more intense and involved please go through this this content right i mean whatever we did in todays class go through that once and if you have questions you can ask me or tas either on the whatsapp group or on teams and you also look at the notes that ive given you the handwritten notes uh this time ive kind of swapped swapped the order i used to


if A is first and GANS then now I have swapped the order this way started from the GAN so it is the lecture four in my notes lecture four in the handwritten notes


I have shared that with you please have a look at it and also read the paper the paper that I am following is that


Radiational divergence minimization Let me just tell you the name of the paper It is there in my handwritten notes


Is called f gyan okay which is a generalization of all gyan so it is called f gyan


Fine


Generative neural samples


Title of the paper okay


Youll see


Variational divergence minimization


This is the paper that I am going through okay Meaning this is what I have like I have of course created my own narrative but this is the paper So it is there in my handwritten notes Please go through the handwritten notes once and also go through whatever has been covered in this class and come prepared please If you have questions of course you can ask me but no do prepare and come back It will be yeah we will continue from here Ill redo what


Whatever I did this time okay


This I will redo but yeah I will look at it and come back okay


Thats all for today then so for people who are celebrating happy 10th anniversary so we can wait next class next uh

speaker_4: So just one question um for this uh theory that you covered any reference material that we can refer to

speaker_1: gave you no thats exactly what I

speaker_4: No no no no I mean especially on this convex optimizations and and such stuff if you have anything handy

speaker_1: Convex optimization is a standard stuff even Wikipedia says the convex conjugate and the convex functions


Yeah any convex optimization book would do but you dont need I mean we are not doing convex optimization here right Beyond just defining the conjugates we are not doing anything So that I think you know standard articles in Wikipedia would suffice

speaker_4: Okay and the uh the paper that you referred I think that that would be good for reference

speaker_1: And my I have I have given you some references in my handwritten notes So now please have a look at it For instance right I mean the final conjugates and the related stuff no I have put in some of the references at the end of my handwritten notes Start reading them


Okay anything else

speaker_4: I just want other questions sir sir this uh quiz will be on Moodle or

speaker_1: No no no we will do it on this thing uh Microsoft forms okay we will not use the models


We will let you know okay again you know we will intimate that in teams and whatsapp


Okay thank you then We will see also let me know if you think that you know that I mean class is too intense or you want some other change et cetera you have that anonymous feedback form that is there in on my webpage You can express your thoughts When you are writing please mention that you like you are from the online version of the course Thats all So that I know in where to implement the change And of course its anonymous You dont have to put your name or anything but just mention that


This is from the online student and you can just put in your thoughts if you have if you need any change in the way things are going okay


Okay see you next week

speaker_4: Think as a my


Thank you sir
