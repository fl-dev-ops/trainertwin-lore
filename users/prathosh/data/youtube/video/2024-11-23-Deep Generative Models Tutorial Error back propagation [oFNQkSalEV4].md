---
id: oFNQkSalEV4
title: Deep Generative Models Tutorial Error back propagation
url: https://www.youtube.com/watch?v=oFNQkSalEV4
date: '2024-11-23'
duration: 01:07:57
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_1: null
  speaker_2: null
  speaker_3: null
  speaker_4: null
---

# Deep Generative Models Tutorial Error back propagation

## Transcript

speaker_1: And you can see my screen right Okay


Yeah I hope you can see my screen So what well be doing today is well be talking about back propagation


And specifically well be looking at backpropagation and neural networks So Ill first talk about an example explaining why it is important and what is its role in deep learning And finally in the end well hopefully solve one or two questions regarding backpropagation So to begin with the basic idea of deep learning is that you have some input data X


So you have some uh


neural network


which gives you an output y and our goal is to


Our goal is to be able to predict why using this neural network using


using training data


Given by X I Y I


Which means that for every data point xi yi is its corresponding output that that you want to have but that you want to have predicted by the neural network so


Basically what the goal of neural networks


is to minimize some error


using the training data


and hopefully learn the neural network so that it can perform well on some test data or test examples So just to give a basic idea of how learning works and how bad propagation is done is that lets assume


Im learning to play a sport lets say tennis and I have


Maybe I I have a


I have a tennis court like this


And uh my goal is to hit the ball into the court


as much as I can and I want to prevent hitting the ball outside the


Something like this


What this means is that every shot that my opponent plays against me I want to return it and return it such that the ball lands inside the court


to avoid hitting the ball outside the court so what this means is that we are training our our muscles and our nervous system to be able to hit the ball inside the court and how do we learn this is


Optimizing this distance or the so called error


So this error is what we want to minimize or maybe the error is from somewhere inside the code So this is what we want to minimize And as we keep practicing


Our muscles develop that skill to be able to hit inside the cord


at the same time minimizing this error so that is the goal of learning neural networks that is to accomplish some task


reducing some form of error so this is the this is the goal of a neural networks or deep learning in general


What are the different phases that a neural network has is that first maybe Ill just copy this


So a neural network is typically a


accompanied by two operations one is the forward pass


that takes input to output


Power it is input to output


And we have something known as the backward pass


The back left button


Goes from output or in in most cases the sorry error


The weights are input


The forward pass is what the neural network predicts and the backward pass is the feedback that you get from the prediction that is made by the neural network So based on this feedback whatever is given by the backward pass we can choose to update our weights accordingly in order to reduce an error So that is a basic idea of every neural network in just in simple terms And we are going to focus on


we are going to focus on this backward pass and uh or or back propagation in general so


So what Ill do now is well set up a simple neural network and we will see how how backpropagation works


The neural network is as follows you have some


You have some input lets say x and its a two length feature vector so x1


And a neural network typically has these neurons or nodes


You call neurons or nodes


And this is where multiple operations happen in the neural network And it keeps and every neural network has things known as layers And each layer consists of multiple neurons which are interconnected with each other So this is typically how neural networks are So this is known as the input layer


This is the input layer


We have uh


We have two hidden layers


And finally we have one lets say we have one output layer


giving us y giving us y hat which is the prediction


This is the prediction or the output


And this is the input


So like I said these neurons or nodes are where the operations happen And each of these connections so maybe Ill highlight it


These connections are these connections link two nodes through some weight characterized by W So every node Im going to notate with the letter A So maybe


Ill call this A


A1 this is the first node in the first layer This is the second node in the first layer So I call them A11 and A21 And these weights are denoted by Wij It connects Wij connects


Nord I


Norgit


And of course every weight is also associated with the layer number So this lets say this is layer one So Wij one is node i to node j


layer one


So this is the notation that were going to follow And similarly the output layer I can denote the sorry the hidden layer I can denote by


the notation


A12 which is the first node of the second layer and A22 which is the second node of the second layer And finally we have Y hat which is the output You could call it A13 but its just simpler to call it Y hat which is the output So this is a notation were going to follow


Yeah so this is the notation we will follow and the weights are denoted by Wij Wij of the layer number So this weight for example


For example this weight over here would be denoted by W


second layer so w2 one of two so uh now that we have uh


define the notations so lets move forward so like i said earlier the goal is to minimize some error using the using the training data and this error is also sometimes also called the optimization objective or its also called the loss function


loss function


some


function of your prediction y hat and your input x


it is some it is some function of this along with the parameters okay so maybe ill also mention that so uh lets say all the w ijs


are in some vector


uh theyre the collection of all these pair of all these weight vectors uh w i j uh of of any layer l so let me call l


This theta is the set of all parameters in the neural network So


and its function of theta Okay so this is typically what is done in neural networks where you try to minimize this So our goal is to


Minimize over all possible theta


function of


x and theta so you want to reduce


The loss function


function using


Training data


So lets maybe copy this


So the one of the most common loss functions that we use is known as the mean squared error


In short we just call it MSE it is nothing but


I hat minus So lets call the neural network


F theta parameterized by theta so F theta is the neural network


I minus


of x


So this is known as the mean squared error and this is what we want to minimize


So uh in order to minimize any function the the most yeah uh there is a hand raised so

speaker_2: Yeah I have a question Can you please just tell me what the theta denotes Sorry I mean I did not understand it fully

speaker_1: Okay yeah sure So theta is the set of all weights these connections I told you right These neural connections this connection from A12 to A21 to A12 So things like these are connections between nodes of the neural network And these are parameterized by some weight So those weights are what if you collect all those weights and put them into one set those are


Yeah sorry sorry Yeah so I was saying the theta is the collection of all weight weights of the neural network So Ill write theta as


W11 of 1 W121 W211 W22 of 1 So if you look here this is going to be W22 of 1


This weight vector connecting this is going to be W21 of 1 This is going to be W11 of 1 And this weight vector is going to be W12 of 1 Because it connects node i to node j This is node 1 This is node 2


the weight connecting node one of layer one to node one of layer two is going to be W11 of one which is this So by what I mean by theta is it is the collection of all these weights in the neural network


So its just a set of connections that we want to learn in the neural network So Ill come to how we learn these So does that answer your question

speaker_2: Yes thank you

speaker_1: Okay so moving forward like I said our goal is to minimize this loss function


And that helps us reduce our error and learn a particular task properly By learning a task I mean these predictions why that we get we want them to be as we want them to be very good or close to what we desire So that is the goal of learning a neural network


So lets uh so so let me begin with a simple example maybe So lets say uh this is your input uh x


Yeah so yeah


So lets say you have two inputs to your neural network x1 and x2 Say this is your node So these are your input nodes a11 and this is a2 of 1 meaning layer 1 And then you have the similar neural network like this


You have a single output node giving you y hat And lets say that okay let me just notate these This is A1 layer 2 This is A2 layer 2 And this weight over here is W111 This going from node 1 to node 2 is W12 of 1 Similarly you have W21 of 1 and you have W22 of 1


Similarly the output layer you have W 1 1 of 2 and W 2 1


So lets so what were going to do is were going to assign some weights to these and then we will see how this neural network is trained


So lets say this W11 is just


Okay Ill erase these and maybe just put the weights on top of the arrows


So this maybe is 1 this is 0 point 5 this is 0 point 5 and this is 1 similarly let these output weights also be 1 and 1


So for the input nodes we have A11 is simply equal to X1


A to one simply equals X to


So this is what we have this is uh this is the input layer


Then the notion of nodes in a neural network is as follows It combines different nodes of the previous layer through something known as a linear combination or a weighted sum of values in the previous layer What I mean by that is


Lets take A12 for example which is uh this node over here


A one two equals a weighted sum of a one one


A21 and the weights are exactly what is there on the arrows connecting the corresponding nodes which is W111 and W21 of 1


So this is typically how A21 is defined as But one important thing to notice before it is not just a linear combination of this It is some function g of this function OK So this g function


is known as an activation function


And depending on the application or what you want your neural network to achieve these activation functions could be different For example you have sigmoid


have a


have tanh and each of these activation functions do something different


So sigmoid is uh


sigma mod of x is 1 by 1 plus e power minus x and the rello function


is nothing but uh


g of x equals x when x greater than or equal to 0 0 if x is less than 0


And uh


And yeah similarly you have other activation functions like tanh exp exponential linear unit and you have many more you have so many activation functions that are used on the linear combination that you get from the previous layer Okay so this is the activation function This is sometimes also known as the net input to the node


And what we have here is the node output


is n the node output are simply the


Okay so lets not call it output Lets just keep it as node output


Uh this is yeah uh one question yeah or two questions

speaker_3: Hi sorry am I on the

speaker_1: Yeah yeah yeah tell me

speaker_3: Yeah yeah tell me I just wanted to know about why we in the middle layer right Can we scroll a little up I wanted to see that figure Yeah why is there no connection between A1 2 and A2 1 Can that also be called as a neural network I mean

speaker_1: No typically thats not how Okay so let me give you the Let me give you a real life example So every living being has a nervous system right


In that nervous system uh you have you you have some neurons that are like this


And then you have these synaptic connections connecting one nerve to another

speaker_3: Okay

speaker_1: So okay I think my screen is yeah okay So what these nodes are is actually this point


the starting of the branch that connects one node to another node So these nodes are typically like lets take the optic nerve for example So the optic nerve is typically a bunch of nerves So these bunch of nerves have separate nodes in each of them and they are typically when you have multiple connect when you have a bunch of nerves like this you dont really


need these two nodes to be connected say


because the the main reason is if lets say lets say some problem happens with this nerve then if these two are connected then this whole this whole line is gone like this whole since this entire nerve is connected then this could be this could cause problems so


Like essentially what we are trying to do is we are trying to parallelize these nodes so that if one thing goes wrong you can you can always have you can always learn with another node or things like that But of course

speaker_3: Okay

speaker_1: This is this is not not an exact answer to your question but this the typically this is the convention that you follow in in deep learning and in and neural networks the you dont have Okay so you dont have connection between these because you have a you have a very nice dense connection between these nodes between layers of nodes

speaker_3: But to the end of the day

speaker_1: Oh yeah

speaker_3: Sorry just to follow up And the difference between A12 and A22 is actually the weights currently right Because both are giving the same inputs but with a different weight

speaker_1: He hasnt

speaker_3: But the bait can differ right thats it right

speaker_1: Okay


Yeah correct So you can notice that if x1 and x2 are different then a12 and a22 are different right Because if you look at a12 it is some function of w11a1 and w21a2 But if you look at a22 it is the activation of so a22 is this one right So a22 is this one And it comes from


Uh so what are the things contributing what are the nodes contributing towards this


So


So in this case its going to be a W121


A11 plus


W uh two two one


A21 Okay So you can see that these two are different right

speaker_3: Sure yeah

speaker_1: Yeah so


Yeah okay So basically this is how we go forward in a neural network which is taking the input to the output And this entire process is known as the forward process


So the forward process takes you from input to the hidden layers Of course you could have multiple hidden layers here You can have A12 A13 A14 and then you can have iHat and things like that So those are deeper neural networks And thats where the term deep learning stems from And when you have more than three or four layers you typically go into the realm of deep learning


Yeah so this is a forward process And so let me just complete the equations for sake of completeness So similarly this is W11 from layer 2 This is weight connecting node 2 to node 1 of layer 3 from layer 2 Okay so Y hat


is again some function of W one one two


but it multiplies the this node over here which is a1 two


Plus W212 of A22 Okay so this is the final output


output or you call it the prediction of the neural network


Okay so this is the entire forward process taking you from the inputs


from the inputs to the output


Okay so typically our input is denoted by x and its a vector containing x1 and x2 So you could call this input data


Or you could call it features


input features


So yeah these names are used interchangeably So you just basically this is the input So the input could be a vector it could be a single number it could be an image it could be anything it could be a video it could be an x ray scan it could be anything So depending on the dimension of the input your neural network will also change the nature of its weights And one important thing is that for every


So I just


Copy this once again


Yeah sure go ahead

speaker_3: an additive property where g of w112 a12 can we can we move uh w weights like can we apply the function on the different weights then add them like g of w11 a1 plus g of w21 a2

speaker_1: Sure you can definitely It is possible but generally in neural networks for a particular layer you have a particular G


So for example layer one so okay maybe this layer could have a ReLU activation function and maybe this can have a sigmoid


So g is equal to ReLU here g is equal to sigmoid and you can you you you generally have different activation functions for different layers rather than different activation functions for different nodes


Theres another question

speaker_2: Uh just a small query that how initially we are assigning these weights I mean I understand later maybe through the backpropagation we correct it but initially we have to assign some numbers against these weights right

speaker_1: Yeah yeah so I I was so that is gonna be my follow up discussion okay

speaker_2: Okay okay sorry

speaker_1: These beta yeah no its okay its a good question actually so


So one important note is that weights are initialized


So what I mean by initialized is they are assigned something


So you are assigning some weights


At the start


So typically what people do in neural networks is that these weights are selected randomly


Or I should say initialized randomly


So uh yeah uh I have a couple more questions yeah

speaker_4: Uh sir what is the significance of this activation function like will it be covered later on

speaker_1: Uh yeah I mean okay so the role of the activation function is to limit the these outputs these node outputs to be in a certain range So you dont


Yeah sorry I got cut off Yeah so I was saying the role of these activation functions is to somewhat limit the values of these node outputs So you have these node outputs right A1 2 8 A2 2 and all these things So you want to limit them to certain range For example if you take the sigmoid activation so g of x is lets say sigmoid of x which is 1 by 1 plus e power minus x what


What this basically does is that uh


Okay let me lose this color


What this basically does is if you have lets say this is your X and Y axis


Okay y is equal to sigma of x what this does is that it takes all your values from


from minus infinity to infinity and it brings it to the range of zero to one okay so in in neural networks you dont want your values to blow up so that your y hat becomes like one lakh ten lakhs and all so you you dont want that to happen so you want to control your you want to control

speaker_3: Im not sure what that means

speaker_4: We want to like contain it in some range

speaker_1: Good yes


And so activations basically control your node output


So these activations are actually very important because this sigmoid right this is the sigmoid function


This is used typically at the output of


of classifiers


So classifier is basically something that gives you a decision So it gives you a decision and you basically want a yes or no decision


And so for example yes could be close to one and no could be close to zero So the sigmoid activation function is a perfect choice as an activation function in these classifier functions So SER will be covering classifiers later on And maybe that time youll encounter the sigmoid activation So depending on what you want your network to do you will choose different activation


for different layers of your neural network


So for image problems you might want to use ReLU So for


Uh image oh sorry


or image networks


You might want to use ReLU


which is basically anything less than zero it gives zero and anything greater than zero it gives the it gives the same output so this is the relu relu function so x and g of x


So this is so depending on your application you will choose you will decide to choose different activation functions So hope thats clear Yeah theres another question

speaker_2: they are very small in number theyre not big I believe the reason you just say you dont want to blow it up is that correct or and when so

speaker_1: And when so yeah I your voice was breaking in the middle can you repeat the first part of your question

speaker_2: generally

speaker_1: what I have seen the weight and biases for this neural network they are very small in numbers they are not pretty big correct correct so so there has to be a reason behind that I believe you just explained we dont want to explode the final y hat correct okay and second thing is that when we initialize it randomly do we also define what kind of thing Im looking

speaker_3: Fine

speaker_1: Using your voice I cant hear


Let me try once again


So when we initialize these weights randomly do we also define the range of between its going to be


Correct Yes we do we do In many applications you use some weights between zero and one


IJ belongs to some lets say minus one to one or zero to one


So typically we choose weights in this range and


Yeah we initialize uh weights randomly such that theyre in this range minus one to one or zero to one just so that its small and


You you dont have something known as a gradient explosion you want to avoid this gradient explosion


So Ill Ill come to what this is later on or it itll also be covered in the course


So we want to prevent this


to prevent gradient explosion so we uh we choose the weights to be a bit in some range where theyre very small yeah so i hope that answers your question for now so uh well i mean uh this this you will encounter in almost any application where the weights are going to be very small and you start off with those weights and then you you start learning your network through back propagation


So now lets move to lets move to backpropagation


So lets go back to our neural network that was over here


Yeah so this was our net network and if you recall we had a loss function L which was the mean squared error between y hat and f theta of x where f theta of x is taking your is the entire neural network this is f theta of x this takes your input x where if you recall x was the was the vector x1 x2 this is the vector this is a vector


vector


Input vector of x1 x2 taking you to the prediction y hat This is the prediction


So what you want to what we basically want to do is lets say we have some training


And for now let us assume we only have one training data sample which is for the input x I expect the output y So this is our training data So typically you call it xi yi And you have n such examples So your training data will typically look like x1 For x1 you desire the output y1 For x2 you desire the output y1


put whiteo and so on


Okay so this is our training data but for now lets just assume we have a single training data sample Assume your data is just x y a single example


Single training example


Now our goal is to minimise


L is equal to half of Y hat minus F theta of X


So this is what we want to minimize and how do we minimize any function We compute its derivative with respect to what we can optimize over or what we can change in the network And what can we change in the network We can change theta or the weights


So this is what we can change


So the natural step is to take the derivative of the loss with respect to some parameters in the network So lets say w ij of l which is the weight ij weight from node i of layer l to node j of layer l plus one and we take this derivative and


What we do is we we take we compute this derivative


And then we do something known as the gradient descent


which is any weight w ij of L is updated as w ij L minus some weight alpha times this derivative


I J L and this is known as


Back propagation


This is back propagation through


Gradient descent


Yeah thats a question

speaker_4: Uh so in this mini uh loss minimize loss function this y hat is also the output of this neural network

speaker_1: Yeah

speaker_4: I had is also the output of neural network right

speaker_1: Yeah I was wondering

speaker_4: So cool

speaker_1: Yeah yeah I sorry I missed the Y hat I wanted it to be Y

speaker_4: Why not Yeah

speaker_1: So yeah yeah yeah sorry sorry sorry my mistake This should be white Yeah okay thank you

speaker_3: Sir I have one question So I have a general doubt So when we calculate the loss in a network the network is not aware of the loss function right Initially we just calculate a numerical loss and its some numerical data which we have


Correct And then how do we calculate the gradient on some numerical data with respect to a parameter Just wondering

speaker_1: So okay yeah thats a good question The laws is what we define


is user defined so this this is a function and it is a function of x and theta correct so uh regardless of regardless of uh whether your data is numerical or or synthesized or analytical whatever it may be you can always compute the derivative of your loss with respect to your parameters so this since this is what we define and it is a we define we can we can compute the gradient of


this and we can and we can use that to update our neural network okay


Uh is that clear or no

speaker_3: Yes sir

speaker_1: Yeah another question

speaker_2: you obviously

speaker_1: So you have your prediction right Y hat from the network So this is the prediction And what is Y hat Y hat is actually F theta of X It is what your neural network gives you So what your neural network gives you is the prediction And what you have is your training data X X I Y I And what youll do is youll compare


Youll compare prediction


Y hat equal to f theta of xi Xi is some training example that you have


The ground truth


the ground truth y i okay so maybe let me call it y hat i so what you will compare is you will compare the loss between y hat i and y i which is the squared error


y hat i minus f theta of


So you have your prediction out here


sorry oh I shouldnt use this is yi sorry and this is your true label


label or ground truth


So ground truth is what we desire and prediction is what your neural network has given you so you have an idea of which one is greater greater or lesser


Uh is that clear

speaker_3: Uh yes but the loss will be the same like even if the F F naught the prediction is higher for

speaker_2: example by five compared to the truth or if its lower by five the loss function will be will give you the same value right

speaker_1: Yes it will yeah

speaker_2: So then how do we know like we have to increase the weights or we have to decrease the weights and thats enough

speaker_1: So that is what so the moment you have some error that is not zero that is greater than zero it means that you are off from your ground truth correct So you gave the example that f theta of xi might be five higher or five lower It means that your loss is half into five square 25 square by sorry 25 by two thats 12 point 5 That means that there is some difference between your


yi and f theta of xi that you want to minimize You want your f theta of xi to be as close to yi as possible So that is when you have a loss that is non zero that is what you want to minimize as much as possible And that is what will update your weights and it will tell those weights See here with your current value you are giving an error of 12 point 5 but can you can you update it so that that 12 point 5 becomes lower Okay


Is that clear

speaker_3: Oh yes thank you

speaker_1: Okay sure Okay great Lets go ahead So we so this was our back propagation equation maybe


So this is

speaker_4: where this alpha is some constant

speaker_1: Yeah Ill Ill come to yeah so this alpha over here


This is a constant


known as the learning rate


So what basically we want to do is we want to update our weights in a way that a change in the weight reflects as a change in the loss function Okay So if I change Wijl as our general expression for any weight if I increase my weight some amount I want to see how much does the loss decrease


So this is uh


So this is typically uh uh


This is typically what neural networks do When you change a weight by delta W how much does the loss change And that loss is delta L And we want to see the rate of change of the loss with respect to the weights which is nothing but the derivative of the loss with respect to the weight


So this is the rate


of change


of loss


with respect to


W I J in the layer N


So yeah I hope learning rate is clear So every weight in the neural network is updated according to this This is the gradient


Gradient descent


Meaning that every weight is updated by some constant times the rate of change of the loss with respect to that weight


So I hope this much is clear If you have any questions you can ask until now Ill go on to Ill go on to derive the

speaker_3: One query

speaker_1: Yeah yeah go ahead

speaker_3: This constant will be common for all layers

speaker_1: Yes yes it will be constant for all layers all weights

speaker_3: And how do we find that Thats what we are going to discuss today Sorry

speaker_1: No no no this is this is not found This is something that we set OK And parameters that a user sets are known as hyper parameters


and these are fixed by a user


Okay there

speaker_4: So Im not a shot

speaker_1: So


Yeah

speaker_4: In one back propagation like every weight is reduced this derivative is with respect to each separate weight or like its a


City and governorship

speaker_1: A good question The this weight update is done usually for all the weights of the network So every Wijl will have its own update because one is you have the weight itself and then this term is specific to the weight Wij So every weight is going to be updated in a neural network typically


So for every weight you will have this update equation You will have a different update equation And the gradient in the update equation is going to be with respect to a particular weight that you are choosing

speaker_3: Yeah one follow up question on that So just assume that for some of the layers the gradients is really small and I have to freeze those layers I dont want to calculate derivative for some of the weights but only to the initial layers of the network So will that also be allowed

speaker_1: Sorry I think I lost your voice

speaker_3: yeah i would repeat uh so just assume that uh in case our gradients are very small for the deeper layers of the network and i i dont want to calculate the derivatives for the deeper layers i only want to calculate the derivatives for the initial layers so is there a freezing of the weights or freezing of the layers allowed during the back propagation that if i can just freeze the weights for some of the layers and only get to a back propagation on few of the layers

speaker_1: Of course you can do that Of course you can So and typically this is done in many applications where you freeze a portion of your network and only update certain weights It could be the later part of the weights later part of the network It could be the earlier part of the network You could definitely do anything you want And what weights you choose to update is completely up to you And it depends on the application that you are trying to


Learn a neural network for okay


So you can definitely do it that way And that is a very very good question actually And many many applications in fact do this So it is known as transfer learning


So transfer learning where you freeze a part of the network


part of the network


and train few epochs


So yeah that is a good point Yeah So you can freeze a part of the network Okay So lets lets take an example and see how back propagation is done And this back propagation that Im going to talk about is general for any neural network So any neural network will will involve back propagation and it is the it is the foundation or it is the foundation of all machine learning Every machine learning algorithm


definitely has backpropagation and it is the most important part of learning learning any task so lets take this example again


So what I want to do is I want to update


What I want to do is I want to find a way


So update


w11 of 1 Okay so lets take this example and we are going to see how to update this weight Now what we need to do is we need to find the derivative of the loss with respect to this weight Sorry dou w11 of 1 So this is what we want to find And the way we find it is we see what is the path So what we do is we find the path


from W one one of one


output


Okay so the first we identify the path taking


taking us from the okay maybe Ill show it in a different color so this is w11 so here is w11 it goes like this to the output okay so this is the path taking you from a weight to the output and what we need to find is we need to find this derivative of l l which is the loss function with respect to w11 now the way we do this is using the chain rule of


derivatives


It says that the derivative of L with respect to some weight is equal to derivative of loss with respect to what it came from 2L by it came from it came from this path right


So that path is it came from W21 the weight W21 So I want to find okay sorry before that it came from A13


So do A1


And what did A13 come from It came from the weight


one one of two and what did that weight come from


That way it came from so this is W11 of two that came from node A12


And what did A12 come from


That came from W one


So this is the chain rule of derivatives And you can see that you have a chain of derivatives that you need to compute And since youre going backwards in the net network this is back propagation And more specifically it is the back propagation of error


Okay so youre propagating the error backwards in the network to the weight that youre interested in calculating the derivative for And that helps you calculate the


the gradient update for the weight Now like lets just give some example activations For example let this be a sigmoid Let this also be a sigmoid


And lets check what these what these derivatives are So the first one is going to be


is uh derivative with respect to


A13 of


Half off


I had


I had minus


the prediction f theta of x which is a one three


three squared and what is a one three we we wrote it earlier in our forward equations in the forward process here yeah


Uh which was this this is uh A one three


So we had this expression


So since it was a sigmoid activation we are going to


So this was A13


And what we want to calculate is this second term over here So derivative of A13 with respect to 11 of 2 is nothing but


respect to one one two of sigmoid of this term over here w112 a12 plus w212 a22 and uh uh

speaker_3: Here you go Y cap right sorry


Here also DEL of D

speaker_1: of oh sorry lets keep making this yeah sorry thanks for pointing that out so it is y minus a13 and uh so we have derivative of a13 with respect to w11 of 2 which is the derivative of the sigmoid with respect sig sigmoid of the net input at node a13


And uh you could try this as an exercise


Ill show that uh


Derivative of the sigmoid function is the sigmoid times one minus sigmoid of x


Okay so you could try this as a simply as an exercise So which gives us a13 by dou w11 of 2 is equal to a sigmoid of this term


this term into one minus sigmoid of that term So we have the second term We got the first term initially We got the second term Now the third term is W11


No actually okay so we may not need this term we can just directly have


So yeah so similarly we can find the derivative of this weight w112 with respect to


a1 to this and then finally we can we can get this expression and if you multiply all of them you get


You get derivative of L with respect to the weight one one of layer one And what we do is


We just update W11 of layer one by the current weight minus alpha which is the learning rate times derivative of L with respect to dot W11 of one And this is the


Gradient descent update


So this is typically done multiple times So this is one iteration


One iteration of learning


And typically you do multiple iterations


So this is typically


multiple times


Until


until the weight converges or until convergence So what I mean by convergence is that the weight does not change too much as you keep updating


So what convergence means is that


W one one of one


doesnt change significantly


Or in other words or in other words alpha times dou L by dou W 1 1


very small


So as you keep training the neural network this gradient is going to become smaller and smaller and smaller until it reaches a number very very close to zero And that is when youre going to stop training and say that your neural network has learnt with respect to a certain weight Okay So yeah So that I think we are out of time Its 9 point 36 So


this uh so the this i hope this was helpful in explaining back propagation and how it helps uh neural how how it helps learn neural networks so yeah uh any questions before we break for the day

speaker_4: So one equation like even for the one data one x y

speaker_1: Or vanilla

speaker_4: This adaptation will happen multiple times right

speaker_1: Correct yes So yeah okay thats a good point Maybe I should mention that also The training is done


Training


Training or weight updates


can be done on batches of examples


Batches of training data


So what will happen here is that when you have a batch of examples every weight is updated using multiple inputs and outputs Okay So what will happen is that your loss function that you had over here right Yeah Okay Maybe yeah here So this loss function that you happened that is there here


So it will be a sum over a sum i i equal to 1 to n and n is known as the batch size


So yeah thats a good point Every weight can be updated using a batch of examples rather than a single example And in fact that actually improves your training because youre seeing how the weight a single weight is affected by multiple training examples so that it works on all of them at the same time


Meaning your yi is close to f theta of xi for all the xis and yis in that batch of n examples


Uh doesnt look

speaker_4: So this means that if if you are able to pass the batch of data you said that the weight updation happened properly it means if you are passing the whole data set at once during a forward pass it will it will adjust the weight even more better way instead of dividing the data into batches Correct your abs

speaker_1: youre absolutely right so actually having a larger batch size means it reduces the variance of the error so that is there is some math involved in that and Im hoping Protosh will cover that in class so basically what youre saying is right if you if you have a if you have some data set of


in examples and you pass all of them in the forward pass and then update your weight it will typically lead to better learning and faster convergence of your neural network yeah so youre right yes if you use more examples the weights will be updated better


Yeah uh any more questions

speaker_3: So uh there is a quiz being mentioned on Saturday do you know anything about it what we should prepare or something relevant to that

speaker_1: Typically it will be whatever syllabus that has been covered till the till the class before the quiz


But Im not sure if he has mentioned any specific portions


If you want I can I can ask Pratosh and let you know again Ill let you know on the group Okay

speaker_3: So thank you

speaker_1: So the quiz is at 9 am on Saturday

speaker_3: So


And can you uh upload your notes onto the teams what you are writing today

speaker_1: Sure sure yeah I will up Ill upload it yeah


Well Ill post it on the group as a PDF


Okay I think we can stop for today So yeah all the best for the quiz on Saturday

speaker_3: Thank you so much


Thank you
