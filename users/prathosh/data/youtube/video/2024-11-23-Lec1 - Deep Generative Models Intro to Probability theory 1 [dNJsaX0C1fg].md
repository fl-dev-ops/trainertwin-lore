---
id: dNJsaX0C1fg
title: Lec1 - Deep Generative Models Intro to Probability theory 1
url: https://www.youtube.com/watch?v=dNJsaX0C1fg
date: '2024-11-23'
duration: 03:07:23
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_1: null
  speaker_2: null
  speaker_3: null
  speaker_4: null
---

# Lec1 - Deep Generative Models Intro to Probability theory 1

## Transcript

speaker_1: A couple of logistic things uh the registration deadline is done right

speaker_2: No sir it extended till 20 X

speaker_1: They extend it

speaker_2: So you may s hit a century there

speaker_1: I dont want that


Okay so we still have the last class is not yet


Table is that way okay


Um okay


Okay anyway lets get started um so here is the plan for today


Ill start from some basics of probability theory


request is that all of you please mute unless you have a question or something even when you have a question


Since its a very large class lets maintain some sort of a decorum Please raise your hand of course virtually Ill call out your name and then we will discuss


Please ask me questions otherwise you know its it will become a very very boring monologue First of all virtual classes are boring because I dont get to see students faces On top of it if you dont talk itll be double boring so we what Ill do is after like every 15 minutes or so right when I finish one particular concept Ill stop and ask for questions Please if you have any questions you can ask me


In the middle you can feel free to just raise your hand so that I can stop and ask address your questions


Okay I hope that you have gotten access to my course notes and that feedback form thats out there and all that right So all the logistic issues are sorted out I suppose


No further questions there I think


The ends


will not uh


Automatize it is one note thing so struggling just a second now so where do I go to that class notebook okay got it


Welcome to one more okay

speaker_2: So youre not shading this

speaker_1: Read only to edit tap the one not icon where is the one not icon here this one No


Okay yeah if I share it you can help me perhaps

speaker_3: Will be on the top right side

speaker_1: Ah let me just see I think youre using some good notes

speaker_3: No

speaker_1: Share screen start broadcast


Here is it to edit tap one note icon

speaker_3: On the other hand

speaker_1: It is a dragon oh this one oh I see I see I see got it

speaker_3: Oh this one right there just behind you

speaker_1: Okay great thank you


So


So shall we have like uh one different page for every day I think lets do it that way

speaker_4: Yes uh that will be better

speaker_1: The date will always be here I suppose right I mean it will be Saturday August 10th it is so Ill have to delete this how do I delete this


This maybe we will rename this as


Oh

speaker_4: So within the file itself just mention the name of this page

speaker_1: Where if you cant

speaker_3: On top the title

speaker_4: Here on top the title Saturday Saturday 10 just above that mention this page title

speaker_1: So well do OCR now

speaker_3: Oh yeah yeah I think it does

speaker_1: Its a boat

speaker_3: So both will work both will work keyboard and OCR both

speaker_1: I need two three minutes for this pencil to be charged anyway so Ill write that so todays agenda is the following


Ill start with the basics of probability theory the probability theory that we would need to continue in this course in the first half The second half Ill introduce you to the


generative models and formulate it if possible So that is the agenda Okay So now the fundamental question that is to be asked is right you know that all of most of the machine learning all of machine learning is based on this branch of mathematics called probability theory right Now the question is why do we need its actually a new paradigm I mean you meaning its a


See when you when we start as when we start studying mathematics right we have


We have numbers we have counting and you know we gradually learn calculus So if you think about it historically what was the need for calculus Calculus had to be developed because you know this idea of


rate of change of things and the idea of calculating the area under an arbitrary curve right That had to be that was important For instance people like Newton they wanted to find out what was the total distance covered by a moving body whose speed or velocity is plotted as a function of time Now there was no tool that time okay that could deal with such kind of question


So he invented a new set of tools right which became a branch of mathematics called calculus which was developed subsequently So similarly probability theory right statisticians had this had this question from a long time The fundamental question is all machine learning is studied right or rather modeled from a probability theory perspective


question is see it is not a false fit in the sense that people dont uh or rather people didnt come up with probability theory or rather apply probability theory because it was there it was not that the idea is that you cannot answer a few questions uh that you often encounter in uh in in machine learning or rather statistics if you do not have this uh tool called probability theory so that is the uh


the prologue Theres absolutely no way you can answer a few questions See just like you cant answer questions like you know suppose I draw an arbitrary curve right or rather I plot some measurement that I make a speed measurement or something as a function of time If I have to find out what is the total distance that was covered by this particle or a moving body only when I have speed as a function of time You cant answer that question if you dont have calculus isnt it


because you know you need the idea of like integration which is area under the curve otherwise you cant answer that question similarly there are questions uh that you cant answer if you if there is no uh if if if the tools of probability theory are not in place so so a lot of people tend to think right oh maybe you know it was a false word people talk of probabilistic machine learning because it is


its just there etc its not that its a tool that is absolutely needed there is no other way to handle or rather answer a few questions uh that that arise without having this uh versatile tool of mathematics called probability here okay so thats uh i mean what ill do today is that ill try to convince you that what are the kind of questions that cannot be answered by any other branch of mathematics right you need to develop a special branch of mathematics


for probability theory and just develop some background there so that yeah sufficiently child no develop some background there so that we can i mean all of you already know this im sure but still just to get your memory and get up to the speed well do that


we will put ash


It doesnt seem to do a good job here

speaker_4: A keyboard will be better though yeah


A keyboard script will be better it will be more simple

speaker_1: Youre saying you have to


Toggle the keyboard


Great


So this we will see in pro


Introduction to

speaker_3: So at the beginning can you put the lecture number as well

speaker_1: Okay so lets get started


Okay so what is the as I said what are the kind of questions that we are interested in in this statistical branch of statistical statistics for machine learning in this


So fundamentally


most problems in science and engineering


Lets just go do this is the even I place my hand on top of my iPad no its just going


Everybodys going to control that


You must

speaker_4: So you can enable the second last option right next to drawing mode

speaker_1: This one


What is this

speaker_4: So that will allow only the pencil to write

speaker_1: This palmajipal great thank you it should be there but I dont know where it is okay fundamentally most problems in in science and engineering


C I E N C E


Function approximations


So what do I mean by this Most problems that you get in science and engineering are concerned about function approximation So what are functions So now the function


Basically a mapping right that is learned between function f is a mapping that is learned between two sets called a


Be right where


Here and we are sets


Okay so its a rule its a mapping right that would map one set to another set


And generally


This set is called the domain


And this it is called the range


So there is a function it takes an element from the set called domain and maps it to another set called range Okay so now well take examples of functions You take some examples of functions So lets say that there is a function Okay that


takes element from real numbers okay and maps it to


real number so this is the function which maps real numbers to real numbers okay this r represent set of real numbers


of real numbers okay so this function maps set of real numbers to set of real numbers okay and you can take another example where


Effects


In fact to be precise here it actually maps


of real numbers to set of positive real numbers


So R plus this is set of reels


r plus is set of positive real numbers right so this is a function so you can think of any uh i mean lots of such examples right so another example can be that uh you can take modulus x okay similarly right so this is another this is another function that maps r to r plus similarly so these sets right they need not be r they can be anything so im going to carry on


Lets take another example where f of x is equal to


uh x transpose x okay now where x the domain right is


In some t dimensional real space So what do I mean by this This is


Real and real vector


So what does this mean this means that you all are familiar about the


the Cartesian coordinates right so you know that every point in Cartesian coordinate I can give my call this x1 x2 every point in Cartesian coordinate can be represented by set of two real numbers right if you take a point here this point will be some x1 comma x2 this is another point x1 comma x2 x1 cap comma x2 cap etc and so on so this is this is typically represented as r2 right so these are these are actually called


This is a two dimensional


Euclidean space


The name after the mathematician Euclid okay


is called two dimensional Euclidean space or vector space Now similarly imagine a d dimensional Euclidean space So basically this is


Its still happening


When I place my hand it is taking me everywhere

speaker_4: if youre not comfortable we can switch to good notes also

speaker_1: Its okay I I I cant really understand this Uh how do I get this


Im in this thing no no I dont want this


So this uh side pane will always be there is that I want this to disappear

speaker_4: Oh no you can remove it and here the settings icon the full screen button that should do

speaker_1: Where is it on

speaker_4: Im not exactly sitting there

speaker_1: Sitting sitting okay

speaker_4: Uh next to it uh not in settings next to settings

speaker_1: This one oh yes full screen okay great


keep educating me okay with all this ive never used this uh like one note its quite the issue i like get used to it no problem yeah im saying see this thing is a d dimensional real vector right so this is called in general this is called


E dimensional


Real space


So basically every point in this space is represented by a d dimensional tuple where d is a positive real number okay z plus


So now whenever I write this notation right I mean a d dimensional real space So it is the extension of the two dimensional Cartesian space that you know of right A d dimensional real space is simply


points in a d dimensional real space are simply uh the simply the vectors right that are there in d dimensions every point in that d dimensional space can be now represented uh using a double of d real numbers thats what i mean so now this function that im talking about uh which is f of x will give you x transpose x where transpose uh is uh you understand what transpose means right transpose up


operation of a vector Now this is a function that maps


R D 2


r plus not in that part can be negative as well so it maps rd to r okay so this function uh takes as input a d dimensional real vector and gives out a real number so that is a function that would take a d dimensional vector to a real number and so on so i mean you can think of these things right there are multiple examples of what functions constitute and as i said most problems


Science and engineering are the following that given


Give him


Yes


I cannot see it that way


Maybe Ill define it in a formal way


Suppose


Capital A and capital B denote


E domain and the rain set


domain and array set now suppose youre also given given given


That is


of elements


X I comma Y I


Subscript


Now excite so lets say that you know these are


in such points Xi


is an element from A and Yi is an element from


This we are to say suppose the NP denote the domain and the inset of


function


for function f


Okay that takes an element from A and maps it to elements in B So given pairs of elements Xi Yi such that Xi is in A and Yi comma B the question or the problem problem


is to find


D


underlying function


Okay so this has been a problem of interest uh for


Its okay This has been a problem of interest for scientists and engineering engineers from time time immemorial So this so if you have given some n elements these are you can also call these as observations


Qualities as observations or data or whatever right We are given this


to find the underlying function f so now why is this important suppose you find the underlying function what is the what is the use of finding out that underlying function is that let me give you examples perhaps example is


Now lets say A


set of positions


A planet in the sky


By position I mean the coordinates


No Ill this might confuse you a little Lets not take that example Lets let me take the example next The first example that I can take is


So its an acceleration


of a body


So B can be


Holes exerted on it


Okay so suppose I give you I measure acceleration of a particular moving body and I also give you what was the force that was exerted on it So the task is to find out how are these two sets related right The set of force exerted on it and the acceleration that the body undergoes right I mean how are they related Okay so this was actually the question that was


That was asked by uh right do you know how are they related these two things

speaker_3: I think thats acceleration

speaker_1: set they are linearly related right so now the lets if i call the acceleration of a body denoted by a which is a scalar so note that set a here is set of real numbers because in fact positive real numbers acceleration cannot be negative and


be negative right because also has a direction of say force can also be negative so yeah so force exerted on it is another real number and they are


but denote this by f then the relationship between these two as you know as a linear relationship is simply given by uh i mean the proportionality constant is the mass so you simply have the the force is related to acceleration it is proportional to acceleration and the proportionality constant is the mass now as i said right i mean this was why do we need this is just one example the i i i


Take questions in a while okay So the algorithm to think of another example


Somebody give me an example of a case where the function is not linear

speaker_3: Im not even

speaker_4: Im not even

speaker_2: And its kind of

speaker_1: Okay

speaker_3: Yeah yeah yeah

speaker_1: Okay how are they related kinetic energy and velocity


uh velocity is v and energy is p okay we can do that


So day is


capacity in Bs energy


So there the relationship is


so on right i mean now you get the point now uh here right i mean uh a lot of scientists and engineers they wanted to figure out this relationship right i mean a lot of research that people were doing was focused on finding out the relationship between


measurements that I have done and these measurements are represented as the elements of sets So mathematically speaking as I said let me look at my initial statement I said that most problems in science and engineering are function approximations What I need to say is that suppose there are two A and B are two sets which are the domain and range sets of a function and if you are given elements which are which are pairs from these two sets


the underlying problem is to find out or identify what the underlying function is that relates elements of A to elements of B Now why is this question important The next thing is what do we get if we approximate the underlying function Okay so now function approximation


Somebody tell me why is that important Why do you have to relate quantities measured quantities

speaker_4: predictions

speaker_1: Exactly right so one one of the things is function approximations


Approximation okay enables predictions


So what do you mean by prediction So we have to define this right So prediction mathematically


simple prediction as


Fine


element


In set B which is the range set range set


corresponding to


Any element in it


I might end the domain


This is important right So now if you look at it the data of the observations that we have done okay is there a pointer here somewhere like without writing can I just point to things


But in good notes it used to be there highlighter is there I dont need highlighter like a cursor or a pointer of sorts do you know anybody knows


See what I want to do is I simply want to like show this right just highlight on this I keep doing this because when I write something I go back and just show that is there something of that sort here


Textual orientation


Does anybody know that no

speaker_4: So there is no pointer

speaker_1: Theres no black to here

speaker_4: No you can maybe use the assistive touch button on the right side to

speaker_2: of circle around things but thats about it

speaker_1: I see but its just there we go I mean I dont want that to stay I just want to point out to that thing yeah somebody

speaker_4: Yeah somebody should use NS pointer if you click on the pen itself

speaker_1: Meaning I didnt read that

speaker_4: And if you click on it then I guess youre supposed to get some menu

speaker_1: But this ones not

speaker_4: no I mean Im gonna on the pen itself like the whatever you have it highlighted


If you happen to click it again


Do you see any options on top Can you click and hold that pen once

speaker_1: Nothing happens


Anyway so find it out I mean if anyone of you want to find that out let me know or just tell Microsoft to have that feature in the next version Its very very useful For example Ill show you in good notes


It was that was just thing you see


so nice


just go with it so if there is something that i write i can go back and you know just mark this and talk about this and it was very very useful for me you see that red mark here it is not there at all

speaker_3: If you go back to the pen gallery I think there is an option

speaker_1: Hes dead okay

speaker_3: So there is a plus button next to the pans right

speaker_1: I like that

speaker_3: Select the pen mode

speaker_2: It says that

speaker_3: To use pen as a pointer I dont know where to get this

speaker_1: Fine okay fine whatever so Ill have to maybe just go back its not very optimal because I keep using this pointer so many times while I was teaching it was very useful for me


And okay

speaker_3: You can use the other

speaker_1: Well thats also fine thats what I was doing but uh people suggested this one also and I just thought that its okay


Okay no problem lets move on Yeah so what I was saying is that you are


still okay right i can just point it here and these some of these things will become yellow colored i think its fine but when you are looking at the notes you notes you should just ignore these yellow colors because they only mean that while teaching ive pointed out to them thats all okay anyway so lets try to do that i mean they are not i mean they are no way they are important or whatever right they just simply mean that while teaching i just pointed to those things and came back


If that is okay I can continue with this Just use this thing and highlight it Okay Anyway so what I was saying is why do you need function approximations is that while you have observations and data for about n points you have made n observations we are often interested in understanding how the system behaves beyond these n observations that we have made Otherwise we have made those n observations there is no need


in in those uh scenarios but we need to know what happens beyond the observations right so that is what we call as prediction prediction is basically you find the element in range right find the element in the range set


the range set corresponding to any element in the domain so given any element in the domain you need to understand how the range set uh how uh what what element in the range set does it get mapped to and that is what is called as prediction so here what you are doing is given a particular angle correction that was not observed if i want to know what the corresponding force is then if you find that underlying function then you can find out what the force is


Similarly with this velocity and energy right And if you are given a particular velocity if I want to know what was the energy that was exerted on it I can just use this function and find out what it is That is one of the most important applications of why one needs a function approximation That all as I said all problems in science and engineering are about predicting this okay


Right uh any questions so far show points


Yes

speaker_4: So is this also called as inverse problem that that we talk about

speaker_1: Yeah you can call it a use problem better


See Im actually going to you know pair basics of stuff Im sure that all of you know this already but yeah so I want to call it from an approximation given these pairs of observations and data rather observations from two particular sets I want to understand what the inverse problem is yes of course it is inverse problem see its not quite the inverse problem because in typical inverse problems what happens is you only have access to output without having access to input


Or rather you dont have elements of range set at all Sorry domain set at all in inverse problem So thats why we are called inverse problems And here you have access to pairs from both the domain and range You get it Thats how they are different


Okay uh Regit

speaker_4: Sir one question I have why do you use this word approximation

speaker_1: Commission is this I


Fine


Please stop writing

speaker_4: Why do you have this

speaker_1: No who is talking

speaker_4: Im not a surgeon

speaker_1: See we have a bit of rule in this class that if you want to talk please raise your hands because otherwise no too many people it becomes a bit chaotic Please raise your hands Ill call out your name and you can ask questions Okay thank you Yeah Ill come Ill go in the order Arjit

speaker_2: Sir one question that till now whatever a function relation we saw between two elements is like kind of a proportional light being it linear or non linear So one is increasing other is increasing or inversely proportional also But suppose the relationship is very complex For example if it is too cold I may not go out If it is little hot I will go out But if it is too hot again I will come back to my home right So this kind of relation where you cannot directly make it proportional or inversely proportional


So how our I mean this prediction will work there I mean generative model maybe too early to ask this just asking

speaker_1: Good question very good question And yes you see that is why we need other mathematical tools The linearity or proportionality doesnt work See for instance suppose you need to suppose you just measure the lets say that you measure the temperature you just heat a body okay you just heat a metal and measure the temperature of that metal at different points along the material Now if you want to ask me this question


that if I measure temperature at one point okay I need to know how the temperature varies across the body you know how do you model it you measure temperatures I want to know what the temperatures are at other points in the body as well given some heat now you cant there is no way that you can write it as a linear equation you have to express that as a differential equation isnt it right so thats why you need another branch of mathematics right which is differential calculus and you need to express it as differential equation but the kind of question that you are asking


is the same now that if I can measure if I have measured the uh the the temperature of a body at certain points now if I if I give you the properties of that body right and uh the uh the initial conditions if I have to know the temperature the body is at a different uh location of the body then there is you need to model it as a differential equation so what Im trying to say is of course the point that you brought up is very uh relevant thats what Ill move on to again so there are


questions that cannot be answered uh with with with these kinds of things right these kinds of existing mathematical tools and thats why you need new branches of mathematics and probability theory is not such so i will give you examples uh example scenarios and questions that cannot be answered using the existing mathematical tools and thats why i motivate why probability theory is needed in its absolute necessity yeah


Okay uh Pat

speaker_4: So my question is more about the terminology So we are using the word prediction here And from what we study in probability predictions its about an estimation of numbers right But in this case functions we are mostly talking about absolute values and were getting absolute answers So why is the word prediction and approximation being used here

speaker_1: Okay see thats a definition right I mean people use different terminology for different things right I am using this word prediction Thats why I define whenever I use a term I define what it is To me prediction here is simply finding an element in the range corresponding to any element in the domain In fact even in statistics and probability theory when we talk of prediction we actually are evaluating a particular function at a point I will talk about it in a while Okay so


We are not theres no I mean theres no quote unquote uncertainty right Well discuss all that in a while right I mean probability theories are very uh


What should I say Its a its a lot of misnomers and a lot of misunderstanding right I mean people use terms right right left and center Even there in probability theory prediction refers to evaluating a function a particular function at a point Well talk about it in a while


okay uh anything else any other question uh this i dont see any hands raised so well perhaps move on now as uh uh like arjit was asking right so the problem here is the following


Or others


Now what if


A mapping between the range


Between the sets


Cannot be found out


using


Existing mathematical tools


See as uh like he was pointing out right okay you know in fact as I said you can take another example perhaps right here in fact you can write this as


problematic


Breaks the flow and makes the glass up


What the hell boy


What happened is how do I


This can be written as you know that this is


The derivative of


derivative of the position


respect to time


because acceleration has to be measured and you had calculus so you can represent that as the the rate of change of t t squared


you can represent that as the double derivative of the position right with respect to time now the problem is as he was pointing out if the relationship between the elements of range and the the domain if theres if you cannot find out if they cannot if you cannot find the functions you cant rather express those relationships using existing mathematical tools what do you do the solution this is just just as


gave you the exam today the calculus was uh


was discovered so to come up with new mathematical tools


So this is how right probability theory is motivated that specifically for probability theory the problem is what happens is


you formal definitions of all this So the motivation for probability theory is the following that what happens is the


The relations between sets to be relations to be


be approximated or rather relations to be found out


A complex what do I mean by complex is that


Do not adhere to existing do not adhere within the existing mathematical framework okay


mathematical framework Now if this happens then you need to come up with new way of modeling things or a new way of expressing things Thats why probability theory becomes handy Let me give you an example Ill also tell you what is the fundamental idea behind probability theory So example is now suppose Im given lets take any ML problem right So elements


Let me not make it uh redundant


Im given images okay pictures let me call it as pictures this is Im not going deep into math yet so lets say that Im given pictures so I have to learn relationship between set of pictures right and


The idea of uh


gender okay so this set typically right when how do you represent a picture uh in a in a in a in a in a computer is that you write that as a r p cross q basically its a grid of numbers right what is a picture what is an image basically its a grid of numbers you have p rows and q columns everything is a real number here right


So you have p cross q real numbers Thats how you represent a picture Now every picture is an element


in a p cross q dimensional real space So you should imagine that just like we have the Cartesian plane right which is two dimensional there is a p cross q dimensional space And in the p cross q dimensional space every image now becomes a number Every picture becomes a point basically Okay not a number Im sorry Its a point Now what I need is given this Ill have to predict right When you remember what the definition of our prediction is I define prediction as finding out the


element in the range set corresponding to any element in the domain So now this gender is a set a discrete set of two values


Lets assume that its a discrete set of two values Now given this picture I need to find a function okay that will take an element in


P cross Q dimensional space which is a vector and maps it to


Okay one of the two discrete numbers 0 and 1 think about it


Now remember how these picture was taken okay rather obtained How are these P cross Q numbers obtained Now what is happening in the background is the following that some person is standing okay standing or sitting or whatever Now you have a sensor okay which we call as camera Now what light falls on that person okay and reflects some electromagnetic radiations back


are sensed or captured by the sensor and what happens in the sensor is that there is a voltage or current chain that happens and that is what is recorded as a real number here correct that is what a picture is and you know these grids correspond to different spatial locations of the object


So what is that we are trying to do here if you imagine we want to relate okay the amount of light that a particular position


reflects okay to an idea called gender


You see whats happening


It is very very abstract in the sense that see here what happened is that in all the examples that we gave force was measurable acceleration was measurable energy was measurable velocity was measurable and so on But here what is being measured is the amount of reflectance that a particular surface is giving you What you want to relate it to is an abstract idea and a non measurable idea called gender


Do you appreciate the difficulty in what we are trying to do Of course right I mean this can be gender or this can be lets say if a person is beautiful or not I mean these are I keep making this philosophical statement that nature is very simple right I mean if you if you want to fly an aircraft which is a very complex task all you need is you know first order differential equations and Newtonian laws Thats all Okay To do things like things that are as complex as


flying an aircraft But to find out right whether somebody is a male or a female from a picture you need a billion parameter model


See by the way look at this How many parameters that this model has I have not defined what a model is yet but still this F equal to MA how many parameters does this have Can somebody tell me

speaker_2: Two point three

speaker_1: One three one it has one parameter m is the only one parameter that it has

speaker_2: One second

speaker_1: And the other example that we saw is also one single parameter model Or if you take a second order differential equation or a third order differential equation all it has are three four parameters So as I said to explain nature of you only need two three parameter models But to understand and predict things that human beings constructed you need billions of parameters It only shows how complicated we are as human beings Ill give you another example for that Lets say that you have a document


These are the typical day to day ML problems that we solve right You have a document


And what you need is the idea of emotion


Right So whats a document Document is collection of written tokens Okay So well talk about all this What is tokenization et cetera and all that You can think of these as collection of words


k words okay all these words are are represented as vectors okay each of them has a each of them is represented by lets say a d dimensional vector


Which means that this entire document now will become a point in a D cross K dimensional space Every document is an element or a vector in a D cross K dimensional space What you need is a function that will take an element from D cross K dimensional space which is a document and maps it to lets say that this emotion So there are five emotions right


Im angry


Happy


whatever right so represent that as 0 1 2 etc so it just maps it to some discrete set of 0 1 2 3 4 okay so this is what we need so what do we do i mean the so called inference that we do right is nothing but prediction what is prediction here given this particular function if you are given any element from this uh uh from the domain set you want to map it to uh the element any corresponding element in the range set that is what has to be done now you know that right i mean this is what


things like chat gbt etc do where you cant uh find the relationship what is emotion i mean like what is the positive emotion for you can be a negative emotion for me and vice versa so this i this idea of emotion is it is very very synthetic and man made okay so to understand how again if you go back to what how these vectors were created okay if you take some uh uh like you know embedding like tf idf which is a very


way of looking at expressing words which is simply counting the number of times every word has occurred keeping a dictionary right how is that related to a a concept called emotion which is which is a very very you know abstract concept


Okay so now the problem is that because we are dealing with the relationship that are complex Now what do I mean by complex Complex means that they do not adhere to existing math I cannot find the linear relationship or a quadratic relationship or a differential equation or a relationship that can be modeled using a differential equation that would relate these reflectances that a surface will give to an idea called gender Or rather it can also I mean you can think of it all


the problems that you do in ML right I mean take a picture and do a person re identification where you identify what the person is and then you can talk of any of those things which are


which cannot be modeled using existing mathematical tools


Okay so thats the motivation right You know why do you need a new mathematical paradigm is because these functions that we are trying to approximate or find are such that they cannot be found out using existing mathematical techniques In fact let me tell you something When people were doing pattern recognition using non statistical methods people were actually looking at coming up with these kinds of functions right


tools okay that would that would enable them to to relate these kinds of vectors to these kinds of elements let me give you an example for that let me take another example


So I Ill take questions little bit just hold on


Another example lets say that you have a speech signal


Okay what you want is set of phonemes


So what are these phonemes Im talking about this uh a ba right off


and all these things see uh note that phonemes see what is the commonality in all this commonality in all this is that the range set let me just tell you this the range set okay


is non maintenable


It is not measurable right or rather Ill call this as abstract


So the idea of phoneme right So what is happening just like in the document and the the picture example what is happening in the speech example is that what is that you are doing So there is a microphone Okay Lets say that there is a speech signal


is a speech signal okay so what is the speech signal so im talking what do i when i talk there is a change of pressure atmospheric pressure that is that is happening okay uh because when i change the air comes out of my mouth with a particular type of constriction from my vocal apparatus and there is a change in pressure in the environment and there is a there is a sensor which is called a microphone which is a condenser based sensor that is measuring the rate of change


of pressure as a function of time and this thing that we that we measured right and that is converting this sensor transducer is converting the rate of change of pressure atmospheric pressure into voltage and this is what you measure as speed signal so this is time this is the speed signal okay its a one dimensional signal so this is nothing but the rate of change of uh voltage as a function of time and the rate of change of voltage happen because there is a change of pressure that is happening as a function


time okay now tell me that uh function so then again you can represent that using multiple things you know one way to represent that is just uh speech signal is a continuous signal right just uh chunk it just like you do it you tokenize a document you chunk the speech signal into parts and you represent that as some like uh some p dimensional vector its a its a p dimensional vector now what you need to do is you need to learn a function


that would take a p dimensional vector which would represent the rate of change of pressure atmospheric pressure as a function of time and you need to map it to an abstract idea called phoneme now why is phoneme an abstract idea so what is r the sound r is very abstract right its its only a perception based idea you know you cant measure r but you can measure this rate of change of uh pressure as a function of time now you need to relate rate of change of


uh pressure right as a function of time to an abstract idea called falling which is not measurable


Understand everywhere the same thing is happening right so the rain is non measurable but the domain can be measured


Okay so in these set of scenarios where you have measurable domain sets and abstract range sets finding out a function that would map these two via existing mathematical tools is difficult But as I said historically speaking people tried using existing mathematical machinery to solve these problems Okay so Ill tell you historically


Attempts were made


EMPDS attempts were made


to learn such functions


using classical tools let me say it


Let me give you an example for it Lets take the example of speech lets say right So the problem is that set of speech signal two we need to get into frame right Thats how that thats


That is what our goal is So you know what people did So they took the speech signal okay They modeled speech signal right As basically you model speech signal as a linear or a non linear system a non linear system This has some input okay And this is the system an LTI system You can either make it linear or non linear Lets say that its a linear system And what do you get by


is the speed signal


mischief Okay so this is the input to that system and this is the speed signal that you observe


Now what they did is all you can measure is this the speed signal right this particular speed signal they say that there is an abstract input which is the phoneme the idea of phoneme


that person thinks


goes as an input to the system and this system converts that into something that is measurable which is called a speech signal Now if they want to you know find that underlying function okay that would see remember that we are interested in finding out the relationship between speech signal and the phoneme not the other way around Now what they do is they model the entire procedure right using some system okay uh and then they cast it as an inverse problem that is where


inverse problem comes into picture that the problem is given the speech signal find out what the underlying for e is so now how do they do that they do it by modeling this entire system using existing math you know for instance the speech community was modeling this entire system as as differential equations


find its parameters you know there are lots of parameter estimation techniques so basically they cast this problem as okay ive given im given some speech signal let me try to uh use some physics of the problem and try to estimate what the entropy system is such that if im given a speech signal i can go back to that abstract concept called phoneme so you can see a similar thing with the images also right i mean the the classical image processing people if they wanted to find out


gender okay uh from an image so what they did what they used to do is and let me take that another example of image right so you have image


to lets say object identity okay so what sort of an object is it is what I need to find out


Given the image so what do you do is that take the image okay so now model object identity as


Lets say its a house


If I see a rectangle


Theres a triangle at the top okay And then you know some regular objects


Other shapes


so on so what do I do I come up with the processing methods right that would


So basically what happens is this theres this function so this function that they do is they first find out


rectangle extractor there is something called you know just extract the rectangle and see where is it and then you do a a triangle extraction


Then you have some sort of you know uh


Object location detection


and so on and try to do this and combine all this to come up with some object identity or regular shape Now that is how people used to attend these problems This is like this is like as I said this is classical speed processing This is classical email processing and you can imagine the same thing right You know in LP also You have documents to you need spam or no spam Email spam or no spam problem right So what people used to do is you know


Just identify some spam words


Okay so this count the frequency


of spam words and so on so now you do this and try to find a relationship between the span number of spam spam words and the the frequency of occurrence and that position etc and then mark it to some identity so you understood right so basically if i have to track trace back to what what we discussed so far what we are actually interested in is given pairs of uh observations or elements from two particular sets we are interested in finding out what the


underlying relationship between the elements of those two sets are okay now in classical uh uh settings uh where the relationship between them can be can be uh estimated using existing mathematical tools now you can try to find out uh how the relationships are i mean dont ask me how to do it i mean thats a thats an entire entire branch in mathematics by itself but you can do it but now the problem arises where


the the relation or the function that we are trying to learn between the domain and and range do not adhere with the existing mathematical tools okay now i gave you examples of this machine learning so why why does this happen this happens typically where the elements of the domain set are measurable okay and observed but the elements of the range set okay are very abstract and they are not measurable things so now how do you solve such problems is the question as i said classically what people use


to do is to try to use existing mathematical techniques and then find that relationship but unfortunately all these attempts right I mean uh before people started uh using the probability theory or statistics as a tool to model these relations none of these things were usable right I mean you didnt have a good speech recognition system you didnt have uh an image recognition system didnt have a good NLP system because all the techniques that were there were simply


Estimating the wrong functions thats all


Okay none of the functions that you estimate so now what happens if you have a make suppose you have this particular


way to find out what a house is right so what if you have a house which is a modern building right that does not have a triangle at the top something like this what do you do it what if it is going in similar questions can be asked for every system here a speech signal suppose you model something you know somebody comes and the the the voice changes uh you model you have modeled it for one particular type of population and the accent changes so what happens you know those systems are failing there because the


underlying function approximation that we have done there the right link function that they have identified using these methods are not


So this is the thing right so now I think you know I this is Ive convinced you enough uh in in in


appreciating the fact that you need uh with the existing mathematical tools do not do not work out you need another uh maybe a way or branch of mathematics right which would uh which would try to address these kinds of problems where you still want to approximate functions between two sets but the relationship between the domain and the range do not adhere to existing tools number one the second thing is that the uh the uh domain


is often measured the range set is not measured not measurable its its a its a very abstract idea now how do you solve these problems is the question and thats why probability theory or statistics becomes extremely uh relevant ill tell you what is the underlying paradigm of solving these problems uh in in in uh from a probability theory perspective in a while okay so ill stop here for a while and take questions um

speaker_4: Yes the example which you just gave that using traditional techniques like suppose you know the speech example which you gave that suppose it has been modeled using one in for a certain set of population it is not going to work with a different population if it has been modeled with the classical techniques But even with modern machine learning techniques we have observed the same behavior Like if a model has been

speaker_1: Agreed agreed Im not disagreeing at all But thing is overall right empirically the statistical statistics based method have given you much much better performance compared to these things I mean Im not saying that this is I mean as people keep saying no all models are wrong Actually all models are wrong but some are useful So these have become more useful right more mainstream more useful If you have any metric that will measure the goodness of these functions okay which is the performance


metrics the functions that people have found out using statistical tools have shown better performance in terms of those metrics compared to classical techniques thats all


Yeah but Im not saying that okay the statistic would solve the entire problem It will give you the perfect function that is approximated Thats not what it is But as I said if you take any metric I mean we have seen this right What like uh


The commercially available techniques do right I mean all our phones have face recognizers and they do fairly well There are problems of course but they do fairly well All of them are running on ML right So suppose you want to use classical techniques to do it The generalization capability is rather poor for them


Okay uh I did it

speaker_2: Sir just the assumption I made the example you gave for image classification like house or maybe spam no spam does did it fail because it is more of a rule based system than ML because we are directly identifying whether there is a rectangle or not whether this is required or not

speaker_1: Exactly yeah thats what I told you right I mean what do you mean by rule based uh what do you mean by rule based system by rule based system I mean that you have found that approximated that underlying function using some rules

speaker_2: Okay

speaker_1: right and those rules are not the again lets go not call them rules i mean uh see one other suggestion or rather request that i have is as we are as well be moving uh like ahead in the classes please okay two things one dont try to force fit uh your already existing terminologies and knowledge in the class okay uh because what happens is you know im i want to build it the brick by brick and i at the end of this course i want to start


using uh you know my language which is the language of uh ml community so please try to use the the the definitions and the techniques that we have discussed in the class as much as possible thats one thing the other request that i have maybe its too early for a test but suppose im teaching you lets say adversarial networks or diffusions please dont ask questions on things uh that i have not covered in the class


Okay so because what happens is Im sure that I mean what happens is in a large class like this itll be too heterogeneous you see So some of you might find this find some topics trivial some of you might find some uh uh uh no a novelty there in some topics that Ill be teaching So I have to cater to the average population you see So thats why I have I will cater my lectures that way But I do I mean encourage and request you to ask


many questions as possible but uh please dont ask me questions on topics that i have rather not uh covered yet right or rather going to cover later and also ask as much as possible use the terminologies that have been developed in the class okay for instance the reason i remembered all this is i mean again uh you know nothing particular to you or because i just remember i i anyway i had to say this because it came up i just said for instance uh see there is no rule


Now we have been talking about functions define what functions are So what we are doing here in the classical techniques is that we are learning these functions or rather we are finding out these I mean I have never defined this word learning I am sorry So we are finding out these functions using pair of observations Now why do they fail is because the function that we have thought that is the correct function is not the correct function


Now there have been enormous amounts of


is that okay somebody said that no no no if you want to look at human faces dont look at these uh these rectangles in fact you can go even one step below okay where


I mean see what do you mean by a rectangle I mean I just took this as granted what do you mean by rectangle rectangle is you should have four line segments that are perpendicular to each other and so on so now how do you find out perpendicular line segments you have to do what is called as edge detection there right given an image you have to detect the edges and what if there are multiple edges in the image how do you deal with it and so on and thats why you have these classical image processing techniques right where people look at subalgorithms different kinds of operators to do edge reduction and then came these wavelet transforms etc so basically


they are asking this fundamental question right What is the underlying function that I have to find such that I can relate these two sets that I have at the hand And because these functions that people have come up with they are not correct in the sense that they dont predict the correct element in the range set they are failing


Okay now the question the bigger question is what other way can one think of when we need to relate these two sets That is the question that well answer in a while


Okay uh she wont

speaker_3: Well yes I think

speaker_2: uh you have partially answered to my question but yeah again to understand when we do a function approximation for any particular input how do we come to a point like we do an experiment and we say that okay uh this function is not working well for this particular input and we try to increase the complexity by increasing the number of parameters or trying out different approach but is there any initial study which shows that its a good start uh that we should take these number of parameters and try this particular approximation technique


for this particular input or it just on the trial basis we we do

speaker_1: Yeah see that is more of yeah there is no I mean there are a few techniques right where okay there are see for instance neural networks there is one large class of functions that you can try out which are universal function approximators see


Right So that is why neural networks are so popular Well come to that in a while So why are neural networks so popular is because the functions that these neural networks approximate right are a large class of functions So now instead of trying out different lets say you try out a parabola you try a third degree polynomial you try an nth degree polynomial et cetera These neural networks are class of functions that can approximate any function to arbitrary closeness So thats why you can try neural networks In fact that is the reason why theyre so popular


these days right they are universal approximators


Okay so basically yeah so the the motivation is that right I mean when you cannot have


like official functions or rather classical functions that would map that would relate these two sets you need a different kind of paradigm to model these two and thats why probability theory becomes a handy thing you know in fact I should tell you something so it was mid 1980s people were trying to solve this this speech recognition problem and a lot of speech scientists they used to model okay in fact they used to model the entire


vocal apparatus as concatenation of several wave guides so wave guides you know what wave guides are right they are physical cavities where electromagnetic waves travel they used to model the entire the vocal apparatus starting from lungs to mouth as concatenation of several wave guides with different diameters and lengths so now the the way when the shape of the wave guide changes right the way the wave propagation happens through that changes so those were using those were being


modeled as several differential equations with several initial conditions and so on people have spent decades doing this now the idea was that okay if you can like model those things using physics then you know what sound produces what sort of a signal and so on but in I think you know 19 19 late 1980 I think its either IBM or Bell labs I dont remember which one of it they demonstrated that using statistical methods those


they were hidden Markovian models which are nothing but ML models right I mean using statistical methods they actually demonstrated they cracked the problem of isolated word recognition where theyre not its not speech recognition if you say an isolated word with limited vocabulary they could identify that okay


People from this classical physics right they got so irritated that they said that all that you are doing is you know modeling your ignorance This was actually said this is documented They said that oh because you dont know how speech signal is related to phoneme and you cannot use the first principles in physics you are simply you know modeling uh the ignorance that you have and these things were actually called ignorance models those days and people were very against these uh these kinds of statistical models but


come 2010s right uh we have seen that these kinds of problems can be very easily modeled uh using statistics and probabilities probabilistic methods okay


Okay so I think let us take a short break It is 10 point 40 now in my clock Lets get back at 11 am So what we will do next is Ill tell you how is this problem solved using the probabilistic methods and well start defining what probability spaces are and what the probability measure is and distribution functions and so on So we are resuming in about 18 to 20 minutes See you in a while


Shall we resume

speaker_2: Its your fault

speaker_1: So yeah so we were talking about uh


function approximations and we want to find functions right even pairs of elements from the domain and range and we saw that in in some of the scenarios finding all these relationships are non trivial so its different kinds of approach for it so uh this motivation right so what is done in this branch called the probability probability theory


the first situation that is done here I mean also rather the first assumption that is made is that


uh vaguely thats what happens is


of humanizations of it Im going to have to write that so basically what it said is


Hello


Uncertainty


Reconstruction


Okay so what do I mean by this This is actually a striking difference between the deterministic way of looking at things and probabilistic way of looking at things is that so in probability theory right the models and the ideas are built by inherently allowing uncertainty in all your functions What do you mean by that See look at this Suppose we want to solve this problem this problem of gender okay given a picture


Now I dont have to tell you so given every picture I dont have to tell you whether this picture belongs to a man or a woman right most of the times our job will be done if I tell you that look this picture has about 70 percent of chance of belonging to a man


we were okay with it right and we go ahead with those decisions isnt it so uh uh another example that can be given is if you look at this emotion as well so instead of saying that this particular document correspond to one of these emotions what if i tell you that these these documents they okay given a particular document ill say that okay this document has 30 chance of being sad and 20 chance of being angry


Percent chance of being happy and so on Thats enough for most of the uh


Task that we are supposed to do Now basically uh this is the idea that


Saying that I mean observing that uncertainty is okay right I mean basically


over the functions okay that we are interested in


Which are the mappings from terrain and the


Mappings from domain to to the range okay


can have can possess


uncertainties


Now I think you know this nomenclature makes sense right prediction So what you are actually doing is given a particular element in the domain what you are telling me is that you are telling me what is the chance of that particular element from the domain that maps to different elements in the range


See the point


So sorry I was muted and didnt notice that Okay so what Im saying here is that in the project GNL inherently what is done is the functions that we are trying to learn between two sets right they can possess uncertainties by construction Now why is this important or why is this a good thing is because as I said if you allow for uncertainties right then what happens is so uncertainties


Following for uncertainty is one


Mix


makes function learning easier


makes the function learning little feasible right because the you are if you are giving me more freedom its its like actually giving the model i mean or rather the paradigm more freedom in the sense that i dont care if you if you are going to tell me what exactly is the element from the range that gets that gets mapped to this particular limit in the uh in the domain set but i only care whether i mean if you if you tell me what are the chances of this particular


a member in the uh the the domain of getting mapped to a particular uh member in the range set so now i mean one might think that okay i mean if you do not have uh the uh uh i mean if if if this uncertainty is there inherently in the model it can be a negative thing right because


If I I mean decisions are deterministically taken I mean either you go somewhere not go somewhere Either you eat something not eat something How can I have an uncertainty associated with my decision It turns out that these functions and a lot of the use cases as I said it is okay if I give you some odds of this particular member in the domain set critic map tools different members in the range set And I give you examples on that


You know for this male female classification task or rather mapping task its enough if I tell you that okay this picture has 70 percent of chance of belonging to a male A lot of times what happens is we take chances and risks in life right I mean that is the idea So you inherently allow uncertainties by construction in the model You have uncertainties makes function learning feasible This is one thing The other thing that is relevant to this particular course


that if you allow uncertainty in it this will


This will help


Creativity


it is too philosophical but think about it i mean ill concretize all these ideas in a while mathematically but think about it uh if we are set on stone right if we are uh if we are uh deterministic everything that we do we dont just take risk as they say uh then youre stuck you cant be creative if you dont take this so creativity see for instance right while when people when when artists write uh portraits okay


of people or landscapes that that that do not exist


whats actually happening is that there is a certain their model of of of human faces right that has a certain uncertainty associated with it without that uncertainty that is associated with that there is no way that this artist is creating a new uh uh image or rather new picture of a human being that does not exist you understand so now if the model inherently or rather the function or the paradigm allows for uncertainty by construction it


One makes this function learning feasible because there are more degrees of freedom And two it will help creativity And thats why right I mean the generative modeling was possible only through probabilistic paradigms I will define all this concretely but think about it Now all the while the problem was that if you are given elements from the domain and the range set you want to find a function that would map every element in the domain to every element in the range set


So on solidarity what happens is that you can create more elements from the domain set and you can create more elements from the range set That is what generative modeling is all about right At some level So this is what it is So this is the paradigm where


The function learning right and these the approximation that you do of all these functions you allow for uncertainty the presence of uncertainty by construction okay Okay so any questions on this before we concretize these ideas


So what do I mean by allowing uncertainty How do you do it actually is something that I that Im going to talk about in a while But yeah before that uh in the philosophical idea any questions

speaker_3: Answer here domain range means the input values

speaker_1: Please raise your hands before you talk okay Ill call out your names


Yes uh Kartik

speaker_3: to the preview

speaker_1: No no no no no see mathematically looking at it there is nothing called exception if there is a domain set there is a range set it is a function that maps the elements from here to elements from there


So theres theres no idea of exception right in deterministic function learning

speaker_3: Look you know is it

speaker_1: Isnt it So like you know f equal to ma f equal to ma thats all Theres no no exception per se

speaker_3: No yeah there can be scenarios like what we say right when f equal to ma but given that mass is constant if mass is not constant thats an exception to this So something like that

speaker_1: Well well its not really because see when if you if you make mass not a constant or whatever the conditions are then the domain and the range set completely changes you see as well as the domain and ranges are fixed right Its a deterministic function No there is there is no inherent uncertainty in the model per se or the function

speaker_3: Okay sure

speaker_1: Hey yeah uh Aditya

speaker_2: Is there one rather comment not a question is that if there is an inherent uncertainty in the system we cannot use these kind of systems to make any control decisions or any any any such decisions is that correct

speaker_1: That is why right now people are uh uh skeptic about using these tag GBDs for all this See why do you think people are talking about explainability and safety biases of these systems Just because they are probabilistically built


Right so thats why people are touchy about these things

speaker_2: Got it And one more observation on when we say functions right functions are well defined which maps each input to its outputs right If you look at f is equal to ma So when we talk about these n dimensional functions with parameters which are in billions is that something which is I cant visualize that how that function is going to look like

speaker_1: Well you cant I mean because human beings cant visualize anything beyond three dimensions So you cant visualize those functions correct Yeah But you I mean you can imagine functions right that would take a billion dimensional vectors as inputs and gives you a scalar Thats very much possible


Right But of course those functions cannot be visualized because you cant we cant visualize as human beings beyond three dimensions Thats thats there

speaker_2: Cheers

speaker_1: Yeah so now lets come to this point that is how do you allow uncertainty by construction Thats the point Now the first thing that is done is see remember that we had sets right I mean set A the way we called it as


know xi all the observations that we make no x1 x2 all these observations that we make which are the elements from the domain the first thing that is done is now each of these observations are the sets that we look at okay


That is


Now these vectors lets say lets say that these are


Some d dimensional vectors These can be d dimensional vectors Now these are


In the probabilistic sense right these becomes these become what are called as instantiations


of a random variable


these no longer are vectors okay now they are not just seen as you know points in some data dimensional space they are seen as instatations of a random variable now what is this random variable business now the way the probability theory structure is the following so it all starts with probability theory


It starts with something called a random experiment


Random experiment or a random trial


please play pay some attention here okay so it says that there is a random experiment or a trial that is happening okay why is it called a random experiment this is one thing that is not well defined in probability theory right there is what do you mean by random nobody knows but there is an experiment that is happening and these experiments they give rise to what is called as outcomes


Basically these are the outputs or rather outcomes of these random experiments and these outcomes okay are enumerated in a set


A set of outcomes


is actually critically important that all of you understand Its not very difficult but please follow me and understand what its saying So it begins with random experiment and the outcome of Im sorry the yeah the the observations of these random experiment is enumerated in a set of outcomes And this is called the sample space


Dont worry about its analogies now but


you mean by set of outcomes uh it is simply enumerating right uh or uh just listing down all the possible outputs of a random experiment now what is a random experiment anything that you that you want to model right now becomes a random experiment let me give you an example lets say that lets take the example of i dont know why this suddenly gives me some weird shapes example lets say that we have image


Its right


So even before coming to that lets take easy examples Now a random experiment


Im tossing a coin and all of you know this


Tossing a coin is a random experiment Okay Now what are the questions that you are interested in Like I want to know when I toss the coin 100 times what are the odds that are like how many times does the coin turn out to be head or something Those are the kinds of questions that Im interested in But random experiment is simply tossing a coin Now what is the sample space here What are the possible set of outcomes The possible set of outcomes are head and tail Okay Assuming that the coin has two faces This is one example of a random experiment


Now another example can be like can people can tell me what it is or you can roll a die


and then face to die


Now the sample space in that case would be so one two whatever possible outcomes that are up to you


So you got an idea of what is a random experiment right I mean anything an experiment that is being performed and is called a random experiment and the possible outcomes of that random experiment is just enlisted in a in a set okay which is called the sample space


No when we


The two


We are not interested in rolling the die or tossing a coin We are interested in looking at an image and finding out whether its a man or a woman right So now um


Taking a picture


for person


Is a random experiment Can you visualize taking a picture of a person as a random experiment


Let me tell you what I mean by this Now imagine that you know you can there are there are there are infinite people that are there right and you taking a particular sensor and shining light on a particular person and measuring the reflectance of that particular person becomes a random experiment Now what is the sample space can somebody tell me what would be the sample space

speaker_4: The same picture can never repeat twice

speaker_1: No no no Im simply asking what is the sample space Okay so let me just go back to definition So what is sample space

speaker_4: All fixed color value combinations

speaker_1: Sample space is simply the enumeration of all possible outcomes of a random experiment


Now the example right in tossing a coin the headtail are the sample space Enrolling an n phase die the 1 2 3 et cetera n are the sample space Now if you take a picture of a person what is the possible sample space Yeah the persons image

speaker_3: I like the fancy letters

speaker_2: all pixel combination male female and third gender

speaker_1: No its not that because Im talking about

speaker_2: All the people of

speaker_1: Yeah so its actually Ill write it as person one person two person three And if there are whatever right If you have like lets say seven billion people in this world you have seven billion possible outcomes


Can you see this So basically this is the way you are modeling it You understand So now the random experiment that is happening is simply taking a picture okay of a person is a random experiment Its simply like rolling a dice When I see this is the world view that you should slowly develop when you are dealing with machine learning that reading an image from one of these open CV libraries or something is nothing different than tossing


coin in the probabilistic sense of words okay so now thats why i wrote the sample space right i mean there are these many people every person now becomes uh the sample space and and similarly you can imagine right i mean now suppose im um recording speech


recording the speech signal what happens is that every possible sentences that everybody in this world can talk of becomes a sampling space


Uh any questions on what is what constitutes a random experiment and what are sample spaces


Okay now what happens is that when we measure right and when we have a sensor and you know we have a condenser microphone we measure it what we get to measure are not the elements of sample space So let me write that So elements


rather maybe before coming there let me just define the probability measure okay so this is the sample space now


what so now this is a set okay now um let me give you an example lets say that i have set up real numbers which are


Yeah simply take set of real numbers right then


of real numbers


Call it R


Now I take a subset


me call it uh use case already there are not of notations very quick very quickly so lets call let me call it a1 is a subset of real numbers okay and a2 is another subset of real numbers so for example this can be 0 to 2 okay this can be


three to eight these are two subsets of real numbers right see my interest number is i want to compare these two sets how do i compare these two sets okay so lets say that the intent


Compare


A1 and A2 which are both subsets of R


I tell you what is the relevance of this with sample space in a while but yeah so let me take some uh like opinions here if I have subsets of real numbers how do I compare subsets of real numbers

speaker_2: Maybe what is the common numbers between two sets

speaker_1: Okay so how does how does that how does that tell me uh how I mean anything about these two sets


Okay so Ill tell you what do I mean by compare it and I want to I want to ask questions like which one is


bigger


or smaller


something of this sort so how do I do that I think people have raised their hands Harsha

speaker_4: Yes sir so one way to compare is uh like if you are able to map each element in this set to another element in the uh other set we are comparing and if we are able to map

speaker_1: I cant no I cant because here I cant find a function that would are you saying that I have to find a function that would map elements in set A1 to A2 See again when I say compare right I mean please take this as the question I want to know which one is bigger and which one is smaller


You all know the answer to this question but I just want to hear from you Yeah Nirmith

speaker_4: Finding the cardinality of the set

speaker_1: Both of these sets have infinite cardinality no these are subsets of real numbers Cardinality of both of these are infinity is it right


You see that in the month Because these are subsets of real numbers So cardinality wont give you anything If its a discrete set of course but its a subset of real numbers cardinality wont help


Okay biology

speaker_4: No so you can find like mean median

speaker_1: How does taking me tell you which one is bigger and which one is smaller

speaker_3: We got the

speaker_1: But there are only its a set you understand that its a set no So there are infinite numbers so now how do you take mean of infinite numbers


See there are infinite elements in both of these sets Does all of you agree with that You can respond with an emoji or something right Does all of you agree that there are infinite numbers in both these sets The cardinality of both these sets are infinity So the average doesnt make sense here I just want to know if you can tell me which one is bigger Thats all Maybe Ill make the question easier right Tell me which one is bigger Okay So lets ask me this Lets ask this question Which one is bigger in these two sets


Aditya and by the way when I ask you a question right and when you when you raise your hands to answer I would randomly call out names okay so please dont take uh it otherwise if we I mean when I ask you I mean if there are any questions then Ill go one by one when I ask you questions then I just take random order okay so here is the question the question is which one of these two is bigger Abhiram

speaker_4: If we apply the length measured then the set on the right hand side seems to be bigger

speaker_1: Okay what can you expand that okay lets say use this word measure


What do you mean by that Thats exactly where Im coming to

speaker_4: So

speaker_1: You said length measure what is length measure

speaker_4: Yeah length length measure is a function which maps the number of sigma algebras in a set to a number

speaker_1: that you seem to know things so now I didnt talk about sigma algebra yet okay so yeah so yeah what is what is the measure so basically what he is saying is just look at the length of these two sets


okay so now you represent these two set the i mean the the these two sets on a on a number line so this is 0 to 2 and this is 3 to 8


Okay now Dillas line has a


higher length


Compared to this length this line correct


Does all of you agree


Well if you agree with this right I mean so basically what we are saying is that associate how do you generalize this idea

speaker_3: It is so

speaker_1: Associate okay a scale of a positive function


a non zero function


Everybodys looking at a lot


Basically given


subset a of r what i do is i take that subset and associate that with some number okay which i call as mu a


Okay which is


A positive real number between zero and


Its simply a positive real number okay I can actually say it has belonged to R plus


confusing with notation its a its a non zero


Real number on zero


It can be zero also


Non negative real yeah thats what it is


You understand So what we are doing here is that for every subset of real numbers we are associating a non negative real number okay Which would which I call as and by the way this is defined as measure of A


Do you understand Now basically lets abstract out So we are given a set okay which is set of real numbers and we are taking subsets of this set and corresponding to each of the subset of this set I associate a non negative number and I call it the measure Does it make sense So basically what does measure do is that a measure


basically a function that will take a subset of a given set okay and maps it to


Non negative real numbers Do you understand So this is a measure


So now why is this important is that given every any subset of a given set okay now you can compare sets based on their their corresponding measure


This facilitates


Comparison


or subjects


Let me give you another example lets say that our set is set of


are two which are you know two dimensional vectors


what can be so which means that an element here right an element in R two


is represented as x1 comma y1 or let me call it x1 comma x2


is I write it as capital X which is X1 comma X2 okay this is an element now suppose I give you okay so now tell me a measure that you know of that is defined on R2


measure on R2 you people already know this

speaker_2: So the tens cost is one square per extra score

speaker_3: Okay

speaker_4: Okay

speaker_2: a magnitude root of x one square plus x two square that can be used to

speaker_1: Yeah but thats an element right Im talking about a subset If I take a subset of R2 okay see remember that measures are defined on subsets


See in R1 what happened We represented every subset as a line segment Okay So now if I write R2


How are each subsets represented here

speaker_4: areas

speaker_1: How are these substances represented

speaker_4: rectangles

speaker_1: Thank you very much

speaker_2: 45 48

speaker_1: yeah then can be it can be any uh uh irregular shape it doesnt matter but for now yeah so this is a subset right a subset in r2 okay now what can be a measure that you already know on subsets of r2


area of interest


So every subset has a measure called area now


Okay now if you extend this to a d dimensional real space what is the measure

speaker_3: Volume

speaker_1: Theyre volumes right I mean theyre hyper volumes You cant call them volumes theyre hyper volumes So this measure that we know of right which is you know which is length in one dimension area in two dimension and hyper volumes in three dimension it has a name Do you know what the name for this measure is


Does anybody know the name of this measure See there can be this is not the only measure that you can have You see given subsets of any sets you can come up with any measure And theres a definition of measure right Okay that if you have a set with zero cardinality the measure has to be zero So if you have two non overlapping subsets the measures have to add up The measures of the individual subsets has to be equal to the measure of the union of those subsets Okay so these are


of the properties that the measure should have but anyway you can come up with multiple measures actually you can come up with your own measure and give it your name doesnt matter as long as these properties are satisfied but the usual uh length area volume measures that we know of right that we use that we have been using since uh class five uh theres a name for this measure do you know what the name for this measure mean is


These are called Lebesgue measures


I dont know why his name is is is spelled like this but yeah So this is called Lebesgue measure So all the length area et cetera that we do in Cartesian or rather Euclidean spaces right D dimensional Euclidean spaces they are called Lebesgue measures So the length area and volume measures Is this idea clear Why am I talking about measures here Theres a reason for it I just just give me a while Ill come to that So now you understood what measures are right So basically what Im doing is that


Im given a set okay Im constructing


the subsets of that particular set


Now for every subset that I am constructing on this particular set I am associating a number with it And that number is what I am calling as a measure And we just saw an example of a measure in d dimensional Euclidean spaces and we called it as Lebesgue measure Any questions Prupal


Hello am I already going are you dead


Okay uh yeah there are a few questions but no case for me on

speaker_2: the measure

speaker_1: Good question Its by definition See the thing is because we perceive measures as you know something that is that we can compare So we cant compare negative numbers you see We can only compare the positive numbers See if you perceive these things as lengths there cannot be negative length


I mean its only a convenient definition convenience so the way the measures are defined they have to be non neglected


But anyway there are lots of measures Lebesgue measure is only one of the so many measures that people have come up with on real numbers But yeah so Lebesgue measure is one of such measures There are other measures like Henry measure Riemann measures and so on But yeah so the usual measure that we look at right the lengths and areas and volumes theyre all Lebesgue measures Okay Any other questions on this I mean what constitutes a measure


Again Im defining right I mean its basically a function a set function that will take subsets of a given set and maps it to a non negative real number such that there are some properties Im not going into details You know one property is that it has to be see every measure by construction by definition has to be


negative for any set it has to be greater than or equal to zero the other thing is measure on the null set has to be zero okay and the measure on union of two sets has to be equal to the individual measures


the intersection is null these are some of the properties i mean as long as you can come up with a function that would adhere to these properties you can name it you can give it your name and call it your measure okay so this is the length measure okay so now why did i talk about this remember that our uh we were looking at random experiments okay and we are looking at outcomes now what are outcomes we do have a set here okay which is called the set of all possible outcomes of a random


experiment and we call that the sample space okay because we have a set


So we have this set which is sample space


Its it what is that thats a collection of


election


All possible


Outcomes


for random experiment


Right we have a sample space We can now create subsets of this sample space right So let F


You know


subsets set of subsets actually


create a set of subsets


Do you understand what Im talking about Again you can go back to your examples right If you are rolling the die you can take you know one three four five as one subset of examples right If you are looking at tossing a coin you can head head head tail head tail tail whatever right They are subsets of omega I mean this is omega by the way And if youre looking at pictures then if you take pictures of several so some set of human beings right That is a subset of this particular set


F denotes


The collection of all such subsets of the sample space


Please thats clear


See just like we had the line segments right which are the pieces of number line the real line So you have subsets of


the sample space okay which is a set


Now now we have a set and we have a subset Now because we have a subset subset and the subset we can define a measure on it


Right so now define a measure


Im ashamed


Okay actually turn the probability measure


Get on


every subset every element of the subset of sample space so now given any element


That is a subset of this T


sample space then I will define a measure on top of it okay and this right is defined as a measure that is


Between zero and one


unlike the Lebesgue measure that can take any non negative value the probability measure okay can only take values between 0 and 1 so now you might have this question right why did we do it this way did it this way because as I said remember the goal is to associate uncertainty in the entire modeling process you see okay and how do you do that this is one of the ways of doing it now you say that okay everything that you observe is an outcome of a random experiment


And every subset that you observe or every outcome every subset that you observe of the outcome of the random experiment that you are doing now is associated with a particular


measure okay which is lower and upper bounded between 0 and 1 so now we you interpret the these values as the amount so basically this measure right the probability measure


such nuisance the probability measure


can be interpreted so just like you interpret the Lebesgue measure as length okay interpreted


Yes


The uncertainty


Associated


subset of subset A which is a subset of sample space do you understand


Now if you go to this example of looking at the speech and the images that we have as the as the elements of sample space you can imagine if you take any subset of the sample space there is an inherent measure right that is associated with this particular subset that would quantify any uncertainty that is interpreted as an uncertainty associated with this particular subset Does it make sense See you should see


probability right just as you see length on the linear the linear line so what is length let me write that so length


It is


R R 2 right is exactly equivalent to probability on


Campus basis


Can you see this point Now see I just made the statement right that remember that we are interested in doing this you know function learning business And we came up with this paradigm called probability theory So what is basically being done is you model or rather you see everything that you have right as see okay so let me go back again Its a very nice analogy here See here when we said that we have pairs of


observation that are coming from two sets Similarly the set of the domain that we talk of for function approximation now becomes the elements of sample space


Okay and just like you associate lengths with the subsets of real numbers you associate another measure called probability measure that would tell you that do not give you the length of these sets okay or subsets This will tell you how certain or uncertain that particular set is


Do you see this point any questions so far


Theres one other piece that I have to talk about which is the idea of random variable and distribution functions Well see that and then well stop this class because from next class I can start formulating what generative modeling is using these terminologies But yeah any questions so far Theres actually bare bone fundamentals for studying any of the ML Okay So let us ensure that you people understand what Im talking about


Any questions here

speaker_2: Oh sir if we take the set of all subsets

speaker_4: of a set and assign a probability uncertainty for each of those subsets is that what we are talking about about

speaker_1: All right

speaker_4: And thats called a sigma algebra right

speaker_1: Thats the same of course if you just need my library no


If we actually have a signal


Thats also called the event set here because Im not teaching probability theory Im not going deep into this A first course on probability theory should start from this So what you said is correct F is a sigma algebra and the measures are only defined on sigma algebra This is the sigma algebra defined on top of or obtained from the sample space Thats correct

speaker_2: Not just

speaker_1: Uh Harish Gautam see I dont want you to overburden with terminologies you see Ill Im only defining what is absolutely necessary


Arise dont

speaker_2: Uh so is the sample space same as domain

speaker_1: Not yet okay not yet I will not say that because hold on to that question Thats a very good question I will come to that in a while


For now I would say no they are not exactly the same See because look at this See if we are looking at taking the picture of a person as the random experiment and we are looking at every person as the outcome right Then where is the domain of the function that we actually talk of See because see what we measure I mean not the measure theory measure I mean English measure what we observe lets say what I observe are real numbers


Okay the elements of the sample space are not real numbers Can you see that


Elements of the samples page are persons or other sentences or their documents which are not real numbers Do you see that


So now the biggest challenge is which I will talk about in a while is that you need a mechanism where you convert the probability measure right into a space which you can you know which you can invite some other sort of measure in fact where you can use level measures and thats why random variable looks into picture I will talk about it in a while but dont think of the outcomes of a sample space as domains yet there is a relationship between them but they are not exactly


say okay thats a very good question by the way nice observation yeah have a look

speaker_4: Yeah so how do we extend this notion Like you gave the example that you know if we consider the set of all people as the set of sample space and then if we are assigning uncertainties to certain sets of people

speaker_1: All subsets all possible subsets All possible subsets Exactly Yeah So you take any possible subset it can be a singleton also in the sense that you can take a particular person and that particular person which happens to be a subset also has a measure associated with it

speaker_4: All possible subsets of people


Yeah so yeah so my question is that how is this notion is going to help us to figure out whether that particular person is a male or female I mean

speaker_1: You have to be


Thats a good question well well well see that well see that yeah


Uh yeah I did it

speaker_2: Uh so what I understood the complete theory is based on the correctness of the sample space right now

speaker_1: No no hold on hold on hold on No no dont jump What do you mean by correctness of sample space I never defined that

speaker_2: I mean uh I mean to say that suppose uh the random exa random experiment I am doing defining a sample space and from there we are taking the subsets and all this theory is based on that that is not it now suppose if we dont know the sample space or suppose we are talking about the planet in the universe multiple planets so on those case it is very tough to define a complete sample space right so on those cases if they are a


Parallel line here above probability

speaker_1: All those cases is


Okay see in fact we never go to sample space because of this exact reason We never care about sample spaces We only work with random variables Just hold on a minute Ill come to the idea in a while

speaker_2: Yeah

speaker_1: Yeah yeah

speaker_4: So why does it have to uh include every subset of uh yeah I mean

speaker_1: definition of measure right yeah because thats how we defined it right i mean given any subset it has to assign a value non zero value


Because think of I mean you look at the Lebesgue measure right you take the real line given any subset of this I want to associate a length with it isnt it


You get it

speaker_4: Yeah but it need not be pairs right say for example if I consider 0 2 3 ah I mean does it also work on that because so now you have three three elements in that

speaker_1: Im not sure


no no oh okay okay see its not a subset you see see when you write what do you mean by 0 2 3 is im talking about three element subset yes see 0 2 3 is not a subset of r you should always remember that we are talking about the subset of a given particular set 0 comma 2 comma 3 is not a subset of r


You see that

speaker_4: It is right Or

speaker_1: 0 comma 2 comma 3 is it a subset of R the discrete set I mean is it a subset of R single term right I mean if you take two elements you are talking about this


See note that Im not putting square brackets here If I put a square bracket then its a subset Now if I write 0 2 3 is it a subset Let me just confirm


set of natural numbers is a subset of R Okay yeah fine Then its a subset of R Its a valid subset of R That also has a measure In fact the the label measure of a discrete subset of R is 0


Okay its like this right I mean even if you write this


0 comma 2 comma 3 youre actually asking me what is the length of these three points


Do you see that

speaker_4: Yeah so thats where Im confused so when I say a measure of A

speaker_1: Amazing

speaker_4: Wouldnt measure of A so I mean

speaker_1: So

speaker_4: what all do we really consider in that a and also if you if you scroll down below

speaker_1: See it can be any subset See any subset right from the set of real numbers has an associated measure But level measure of this particular singleton or like discrete subsets of R is 0 thats all

speaker_4: If you come to this 2D picture right uh I mean there we said that uh

speaker_1: Yeah if you take the measure if you take the area of a line it is zero

speaker_4: Yeah but in lets stay with this example So when we say that element x1 x2 right I mean its again a point in

speaker_1: Yeah yeah thats why I said no measure is defined on subsets of R2 This is not a subset of it can be a subset of R2 but this is again a set that has zero measure


You get it This kind of thing has innovation

speaker_4: Thats great Pam


Any example where the the measure is non zero

speaker_1: This this thing no this rectangle

speaker_4: Okay so we we choose a region in the uh in in the space and then we associate

speaker_1: And R be associated Yeah In R2 you take a subset of R2 Okay So its like this Okay Let me write down So this particular set


1 point 1 comma 2


this thing is


two one point comma


Welcome to


This has an unzipped machine

speaker_4: Yeah because it defines a rectangle right

speaker_1: Exactly exactly exactly

speaker_4: And and if you can if you if you go back again to the one dimensional case I think even there we can say the same stuff right So so length is a measure when we define it over a range

speaker_1: No see thats what Im saying See if you take a subset you take any subset the way the measure is defined it doesnt tell you what subset you have to take You take a point here you take three points here okay Thats also a subset of R Now the question is what is the measure of that particular subset The measure of that particular subset is zero thats all It does have a measure but it has zero measure

speaker_4: So you need a kind of an interval to define to get a non zero measure

speaker_1: Leaving questions Leaving questions Okay

speaker_4: Okay

speaker_1: Leibniz measure is defined that way

speaker_4: Bit of an elbow there

speaker_1: In fact in fact the definition of Leibniz measure is so yeah so if you have a if you have a subset of R right which is a closed subset of R then the the the absolute difference between the final element and the initial element is the definition of Leibniz measure


It is an interval right


So thats why if you take a discrete set the measure is zero isnt it

speaker_4: If you take individual points yeah if you take individual points the measure is zero but if you take an interval then we have a a valid measure

speaker_1: But it was non zero right

speaker_4: No non zero magic

speaker_1: See that is why its a very good question See if you have a continuous random variable or a continuous sample space the probability measured for a particular point is zero For instance if we are looking at this particular example right of people the probability associated with one particular person is zero


see that its actually like you know finding the Lebesgue measure of a of a point its similar to that so thats why if you have you know if you have studied probability theory before people would say that for a continuous random variable you should not


interpret the probability density function as valid probability measures because the probability of obtaining a particular point right in a continuous sample space is zero just like the the measure Lebesgue measure associated with a particular singleton subset of a real number real set is zero anyway so if you understood it fine if you dont need to understand that just just ignore it okay I didnt mean to confuse you shall we move on


Now the next question is now you understood what quality measure is on sample space right So the next thing is see somebody asked me this question right So now what happens is sample space


rather elements of sample space


are not observed in practice


Because right what you see T I E C E right or T I C what is it T I C E


So what I am saying is you only get to see the picture of a person You dont get to see the person You see what I mean If you take the elements of sample space you dont get to see the entire sample space You dont get to rather lets say elements of sample space are not observed in practice in its entirety number one I mean I think I just asked that question right When you dont observe everything what do you do The other thing is you dont even get to see the elements of sample space When you do a measurement all you get to see is that you measure


or rather not measure the theory whether you observe some real numbers when you see the speed signal you are not did that the outcome of your random experiment is speed but what you are measuring this rate of change of uh uh well im sorry the pressure as a function of time


How do we deal with it is the question Somebody also asked me this question right Is the domain that we talk of is actually the sample space No because what we observe what we get to measure and observe using equipments okay or sensors is are not the elements of sample space Now what is the what is the how do we deal with it Okay thats a very important question So for that what is done as


Define


Therefore defining a function


Fun


Sample space


Some real numbers


So what are we doing here is that lets say that you have your sample space that are like all persons okay or rather youre doing that random experiment where you are looking at all the people okay thats your sample space Now I define a round a function okay


X is a function okay that will take a person or rather take an element from the sample space which is a person


Okay and math it to some


T dimensional real number


You see what is happening What is happening Take a first take an element from this after space okay and map it to real numbers


Do you understand


So if you take the example of


Red and blue


A function that we are talking about will take head


Map it to a la to write it as a function


zero the function evaluated at tail is equal to one


So here I cant write I mean the first example I cant write it this way because every of my element x of person one will now become a d dimensional vector I mean I cant write a d dimensional real vector For our convenience its actually a p cross q image Let me write it as


We cross QDM channel to make things easier


So every of this entry is a real number


Do you understand whats happening Whats happening is because the elements of sample space are not observed okay


You assume that there exists a function that will take elements of sample space and map it to something that we measure or observe


See this is what we get to measure right so what do we get to measure we get to measure the observe or measure


sense


Element software


elements of range space of


of the function x that will take the elements of sample space and map into some a dimensional real space This is what we get to observe When we have an image we have p cross q real numbers and every image is a p cross q real number What is it The way we should see it from a probability theory probability probability theory perspective is that what is happening is you should have the entire story in your mind Whats happening is somebody is doing a random experiment and there is a sample space We dont get to see the sample space


But there is another function that is taking the elements of sample space and mapping it to real numbers And these are the real numbers that we get to observe


Does this make sense


And do you know what this function is called


Does anyone know what this function is called

speaker_2: Random variable

speaker_1: Thats the most unfortunate thing that has happened this function X is called a random variable


The biggest misnomer of all times So this is


These are random


Why because its a deterministic function


Not a video


because it was in the function


I dont know who named it random variable but that person has done a big mistake This is this is neither a random this is neither random nor a variable its actually a function that is defined between the elements of sample space to real numbers or like d dimensional Euclidean space


Make sense


Now in the deterministic function approximation problems what we used to call as domain are actually now


The elements from the real stress of the random variable from the probabilistic standpoint


Can you see that now set of images


images that we have as data this is what is called as a data okay set of images which is data are elements


from


range space of


Another time well be able


It is mapping this into


You see the shift now in the deterministic function mapping scenario in the classical scenario our data was simply points in P2 dimensional real space Now they are still the points in P2 dimensional real space but they have to be seen as the


the the elements of the range space of an underlying function okay of an underlying function oh I think this works as a pointer great I certainly previously discovered it you see


So if I do it if I do it below what I want to highlight no it will


Itll put that like invisible yellow line behind it but its okay I suppose Yeah you see Yeah I was making a very very important point here that in the probabilistic way of looking at things the data or the images that you get are just not seen as the elements from a set Okay They are seen as the elements of a range set Okay And when you talk of range there is a corresponding domain And what is that domain that we talk of


The way is the sample space


is this idea clear so every image now okay is actually an element from the range space of a function that is called an integralable which is mapping the elements of sample space to this euclidean space


Now do you see why are we doing this You know if you can connect the dots See the idea of identity of a person is associated with the elements of sample space But what we are getting to measure right of c are some real numbers Now we have to somehow relate these real numbers to the idea of the person okay which are elements of sample space Therefore we need a connection between the sample space and real numbers which is provided by this function called random


Is this clear


Okay uh questions uh Ragoenta

speaker_4: So this is just one function which maps it right I mean there could be many functions or many random variables defined over the same sample space so exactly

speaker_1: Many random variables defined over the same over the same sample space so

speaker_4: A and in this example say for example uh the l uh the set of persons was our sample space right

speaker_1: And you can define multiple random variables on top of it

speaker_4: I cant


Yeah for example some gene profile or something of that so so that can also become a a random variable

speaker_1: no no no no no again yeah see there is no physical connotation to random variables you see those functions because uh oh what you are saying is that uh what what we measure may not be um the picture it could be any total

speaker_4: the picture it could be in a totally different domain

speaker_1: Absolutely you measure the height weight of that person that becomes a relevant variable yes

speaker_4: Okay its a mapping from the sample space to real some of some r some real space

speaker_1: Yes yes thats a random variable Now what happens is well the next step is because we have a measure that we have defined on these as the sample space right or the subset of sample space that measure gets translated right into some sort of function under this random variable x also


You see what Im saying


Under the random variable the measure that was defined on subset of omega now will be measures that are defined on subsets of R


Look at it

speaker_4: Yes yes

speaker_1: Thats called an induced measure and but that measure has a very very famous name that all of you know of that is called the cumulative distribution function


probability measure that gets translated right via a random variable the induced measure that is defined on what is called as borel sigma algebra the subsets of r are actually called probability distribution functions now the story is complete ill write all that down because you asked im asking im saying the story is that now instead of working with deterministic functions we work with probability measures okay now those probability measures get translated into


distribution functions under random variables Now because we get to see random variables okay we work with distribution functions So now the entire story now is that given some elements from the range space of random variable okay estimate the underlying distribution function That is all the machine learning is all about Be it generative modeling discriminative modeling I will connect it to how is it related to general detection or like even chat GPD is doing the exact same thing Given a particular


random variable observations from a particular outcome of a random variable estimate the underlying distribution function that is all underlying probability measure actually Ill come to that in a while Okay um such in

speaker_4: Hi sir so uh I I did not understand this range space what what does this exactly mean

speaker_1: See a a a function has a domain and a range no


The range is this nothing this isnt the domain

speaker_4: Okay for this function this is the domain and this will be the range space

speaker_1: Yeah ranges are PQ


it okay and in this particular example here the the domain is again this this is the domain


Mm


Ranges discrete set of 0 1


What we see are the elements of the range space under this random variable correct


Add it here

speaker_2: So we cannot have a random variable which is non measurable is that statement correct

speaker_1: See non measurable in the sense of uh measurability is it I mean you are talking about the measurability of a particular set are you talking about that Yes

speaker_2: Yes yes

speaker_1: You cant know because


it is the this the because there is already a an underlying measure that is defined on the domain of random variable again please be very very conscious of the fact that random variable is a function so whenever i talk of random variable its a function that im talking about okay now because there is an underlying measure that is uh that is defined that that has been defined on the domain of this random variable okay theres always an induced measure that comes with it and that induced measure itself


called as probability distribution function


See you have defined the probability measure of the sample space already right


Because of that when you define a function on top of that particular set theres always an induced induced measure that comes on along with it

speaker_2: And we have a set which is non measurable meaning there is no

speaker_1: Yes there can be I mean this is like its a topic of its own There is this branch called measure theoretic measure theory You had study that And by the way if anyone of you is interested in this kind of a treatment right there is one very good NPTEL course by Professor Krishna Jagannathan Its a good friend of mine from IT Madras So I think introduction to probability for engineers or something thats the course name If you have interest in this kind of treatment of probability theory please have a look at it This is the last


time that ill be talking about measures and all this okay at the moment we go to distribution functions and density functions well work with density functions i mean i just wanted to make the footing solid right because you know people dont often understand where are these probability density functions coming into picture because when you are given some data and what is data data is simply some 10 000 images or some documents or some speech signals etc the thing is we talk of probability uh


integration functions of this particular speech or images or something what do they even mean okay i always take this one particular i mean one introductory lecture to ensure that people exactly know whats happening no when we talk of probabilities of images we actually mean that oh there is this is the this is the element of a random variable thats a function so this random variable has mapped the elements of sample space to this particular real numbers so now that sample space has a


probability measure and it is that probability that we are talking about


Okay I just wanted to give that connection right you know completely I need 15 20 more minutes to establish that connection before we define what genetic modeling is Shall we do it in the next class


Okay so here is an appeal While coming to the next class please look at some of these definitions that I just told you Okay and in fact we didnt cover a lot I mean it seems like we did a lot but we didnt cover a lot It was some definitions thats all Please have a look at them Okay and as I said no every class will have a causality right I mean you have to know what we did in this class to understand


we are going to the next class with the next class we go to distribution functions and define what a generative modeling is and we go to the adversarial learning and so on okay thats how the trajectory is so please come prepared for the next class with some of these basics please look at what distribution functions are from this angle right what are density functions uh like how do you define uh density function distribution functions on this and so on please have a look at it okay i will not be talking about measure theory anymore and uh


like if you have any comments concerns etc theres always that like anonymous feedback form where you can go and express your because this was the first actual class that we had right in fact the second half the first half was only some introduction so you can go to that feedback form and let me know what you think about this and if you need any particular change ill be happy to incorporate them


okay so any questions uh on todays content any comments i think sachin has something to say sachin uh yes sir just one question in this context of images so like one image has multiple pixels right now this random variable function which uh like takes a sample space element and converts it into this rpq so like this random variable is will be for the all the pixels of that image or like okay sir i think

speaker_4: Okay

speaker_1: was apparent anyway see we we say that our pq you know what are the what are these pq pq are the dimensions of the image so if youre looking at a 400 cross 200 image p is 400 q is 300 so basically we are saying that every image is a point in a 12 000 dimensional space okay and that becomes the the the range of the rating variable


Make sense


Okay uh anything with Arigato

speaker_2: So maybe just a logistic question the same book like Ian Goodfellow which explains all the theory

speaker_1: And see this good film book does not have any of this

speaker_2: Okay okay

speaker_1: So see again as I said no this is not a part of the course because you know this is supposed to be some fundamentals but as I said just to ensure that everybody knows whats exactly happening under the hood I do this So next class we will we go to well go to the contents input for us book okay

speaker_2: Okay cheers


So any books uh if we want to follow along with the lectures

speaker_1: before you know is if you see for this particular treatment of probability theory you look at uh professor krishnas lectures this is not needed i mean meaning uh okay i mean if you know this its great right but this this is bare bare bone fundamentals yes after after you know this then uh then we will move on to distribution functions and so on


Okay uh person Yeah class is over I mean people can leave here


Assessments


The Prasanna are you there You want to say something


Perhaps its not there Okay Uh so thank you everyone Uh see you next week Bye bye

speaker_2: Thank you

speaker_3: It should be clear to watch out

speaker_1: Should we create a WhatsApp group Should we create a WhatsApp group

speaker_4: How many orders do you have

speaker_1: No


Let me just create a whatsapp group and send you the link


Yes

speaker_2: I think someone asked the question that if the

speaker_4: is images and what would be the range so on continuing on the same question so what kind of probability measure we should consider in that case is it like hyper volume kind of thing

speaker_1: what youre gonna do yeah thats thats the entire question that you ask in machine learning what is the underlying distribution that defines this particular image space nobody knows no thats what we model using neural networks isnt it


Didnt see a

speaker_4: So we need to find out that property measure itself

speaker_1: Absolutely because you know if you do that then you have solved the problem isnt it then you know everything about it


The entire machine learning is finding out that underlying measure the entire machine learning is finding out the underlying measure

speaker_4: I think its fine

speaker_1: Particulate


Ill establish that connection in the next class I wanted to do that in this class itself but we ran out of time I underestimated the time that I would take to do all this So Ill do it in the next class Please maybe you can ask that question But anyway Ill start the next class with the answer to that question


I was asking if we have to create uh this thing uh


Whats up group

speaker_2: I think Shibam has created one already sir along I mean including you

speaker_1: Oh that group is there I think no everybody is not there in that group so maybe Shivan can you put it in the in that teams group


I think he is not there yes sir

speaker_4: Yes sir Ill ping the link on the Teams group

speaker_1: Please do it huh


So that everybody is there I mean I think thats the easiest way to communicate you see some resources etc we can quickly communicate and so on

speaker_4: Yes but it might have a mix of people who have not opted for the course not sure

speaker_1: Its okay


We are not you know some doing some dark state activities here so fine


And then you can say now that the people who are not enrolled in the course may opt out


Okay see you next week then Bye bye I think you know this long weekend no its heartening to see that all of you are here for a long weekend

speaker_4: Thank you so much

speaker_1: Thank you

speaker_4: Thank you

speaker_2: I see what youre saying
