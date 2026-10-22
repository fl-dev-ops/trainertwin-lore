---
id: 5FxZkHrGgJQ
title: Lec 7 - Deep Generative Models GAN variants and Applications
url: https://www.youtube.com/watch?v=5FxZkHrGgJQ
date: '2024-11-23'
duration: 03:06:37
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_1: null
  speaker_2: null
  speaker_3: null
  speaker_4: null
---

# Lec 7 - Deep Generative Models GAN variants and Applications

## Transcript

speaker_1: we begin the class today so i was waiting for some people to join see i i uh i hope that uh like the people who have joined today uh i see as 79 people so uh none of you are planning to drop the course right because the window for dropping the course is uh is going to close by tomorrow i think tomorrow day after tomorrow right

speaker_2: Yes thats right

speaker_1: Okay so is anybody still considering dropping the course So Ill tell you why Im asking but yeah is there anybody I think you have gotten enough flavor of how the course is going to be and all that right So is there anything any concern that or rather information that you might want to know to take that decision


Because initially we started with some hundred people now we have about 85 I think you know some 15 people have dropped which is okay fair Uh anybody else considering dropping the course

speaker_2: Considering to drop

speaker_3: because of personal reasons

speaker_1: Okay no problem Yeah but you still want to continue attending the classes Yeah so that is one thing that I wanted to ask you So once you drop the course would these ICANN people allow you to continue attend classes Or would they just remove you from all groups

speaker_4: Audit isnt allowed for us

speaker_1: audit isnt allowed okay i see okay so except for uh mr billa right anybody else considering dropping the post


Okay I take that as a no Okay so this I think then this is the final class trend that we have So I need this because we need to plan the assignments right now We can form the groups of three and also plan the exam So the exam the midterm exam Im planning to have it after two classes which is today there is one class where Ill finish this GAN thing and the next


class we will look at the variational autoencoders well start with vaes after that well have the bitum exam so that would be i will tell you


okay its 20 for 25th uh yeah 12th is the hell right so we can have it on 10th of uh october if its okay for you its a thursday


Uh well have it on 10th


Does it work for all of you 10th of October

speaker_4: Okay

speaker_1: Yeah timing we have to see something that works for all of you Maybe 8 point 30 to 9 point 30 8 point 30 to 10 in the night

speaker_4: Im sure it doesnt final date for submitting the first assignment right so normally we may send till the day so we may not have the time to prepare on then

speaker_2: So it doesnt

speaker_4: Okay

speaker_1: Oh oh I see

speaker_2: And then one more thing not sure Thursday at this moment maybe but it is office days for most of us and many of us have actually the US client I mean not me but many of my friends I can see in this class So I dont know whether it will be a right time to take an exam for them Can we plan it on Sunday instead

speaker_1: Sunday is also okay uh so which means that well have to do it on 13th


So dwell this uh like Tahirah


13th we should do 13th October is okay with all of you anybody has a problem with 13th October


13th is fine huh Yes sir So maybe what Ill do no I will write it


Okay so

speaker_2: You want them to be

speaker_3: create a poll this time sir

speaker_1: No I dont I wont I will just put it here make it a mixam


is on thirteenth Sunday


Between 10 and 11 30 am Mr Koken

speaker_2: So can we have it on afternoon time

speaker_1: Okay we can do afternoon how about two to three thirty one thirteen


Anybody has problems with 22330


On 13th of October


Okay so if there are no problems then we will


that time Im putting that on the WhatsApp group okay okay so no more discussions on this midterm exam is fixed on yeah we have to say 13th October

speaker_2: Sorry if I missed it any quizzes in between or it will be direct 13th now

speaker_1: Oh there will be quizzes I mean see quizzes are independent right every uh fortnight there will be a quiz so next quiz will be next Saturday


Thatll be it

speaker_3: No no no

speaker_1: Next quiz will be next Saturday And yeah so every alternative Saturday well have a quiz that is independent of this exam


Syllabus said I mean uh from last quiz to


many glasses


Or what


Yeah which will be cumulative right I mean if some people some portion has been covered the next part of the portion will be for the quiz thats all

speaker_2: I mean uh from the day zero till whatever cover that will be quiz

speaker_4: total six classes

speaker_1: not day zero i mean like you can take it from like previous quiz to this this class right that that way yeah i would i should have said non cumulative yeah so its just

speaker_4: Okay okay

speaker_1: Okay so that is settled I suppose No more questions on that Midterm exam is on 13th October between 2 and 3 point 30 So I can what I can do perhaps is to block your calendars also That would be a good thing to do Let me do it right away so that all of us are


They do that

speaker_4: And so this MCQ will be subjective or MCQ type I mean sorry midterm will be MCQ or subjective type I mean just as pattern of the exam looking for

speaker_1: It will be a return exam

speaker_4: Okay okay

speaker_1: Objective not MCQ


It does


13


hopefully


What is the closest number here


E one E one two eight six O Z


Is it even Im not getting this

speaker_4: Its on the Teams meeting top

speaker_1: I require additional


Hard channel maker

speaker_2: Yes sir its E1286

speaker_1: Correct


How do we make it a Teams meeting thats not a field


I just sent a calendar in email and you all see that

speaker_2: Yes

speaker_1: Okay so great so that is done now


Can we have a second please

speaker_4: Yeah sorry it says DGM Q sir is it what we meant midterm right

speaker_1: Oh car


Uh cant edit it for some reason


Yeah that is what it is it should be yeah


We dont exactly


Enter it Yeah fine So practice questions Well see this being a graduate level course its not a probability theory course or anything so I cant give you practice questions that way


So what I would encourage you to do is read the previous years notes and also the original papers of things that we are covering Okay it will be around that


And also you should it would be proctored so you need to keep your cameras on and then write the exam okay


And the way to do it is either you write it on a sheet of paper scan it and upload or you can write it on your like ipad or whatever and then share us share with us the pdf

speaker_4: So notes can be different right Or its not

speaker_1: You mean during the exam No If you want an open book exam I have to make it more difficult

speaker_4: If you want an open

speaker_1: If you want that because Ill have to assume that youll have access to notes and have to ensure that I should ask you things that are not there in the notes right So which means that it has to be made a little bit difficult

speaker_2: Uh sir maybe this question is not right to ask but just asking the ill there be a question that where we have to derive these formulas and all which you are teaching us

speaker_1: And this


I dont know how to answer it


Yeah of course you are supposed to know all that time for this


Ill not ask you the exact thing right because you know whatever Ive done in the class Ill not ask you the exact thing but something similar something around it right

speaker_2: Yeah yeah I mean definitely theory and all definitely I dont know but these formulas are not like little

speaker_1: See dont have to remember anything not be reasonable not ask you to remember anything other than some fundamentals right for instance see you cant you cant afford to forget the definition of lets say a density function right no no thats for sure im saying there is some

speaker_2: No no no thats

speaker_1: Obviously I would not ask you to remember some some formula or something I mean you should trust me at that level with some reasonability to what we do

speaker_2: Yeah yeah no

speaker_1: Right okay anything else any other comments on the exam stuff


Start with the class

speaker_4: So what about results for quiz one

speaker_1: I think that should have gotten right I mean uh immediately

speaker_2: No no no

speaker_1: really okay so was it done on uh like it was on microsoft form right microsoft forms

speaker_4: I think its got to be

speaker_1: Was it Google Farm or Microsoft Farm

speaker_2: It was microchip

speaker_1: Microsoft forms no hold on let let me just ask Chidanand if there is some setting where you should can make the outcome visible right after the curse let me ask him to do that


Should be seen immediately actually


not became my call okay ill ill tell him to do that


Because generally the way I ask them to do it is once you submit your answers no you should you should get the the marks right because it is possible because its a multi


First question type okay


So you just double no

speaker_4: Thats all

speaker_1: Uh the Excel sheet that was passed to us to write the details of the assignment teams it was having four columns and we thought four people can join together and create a team but you all

speaker_4: so told its a size of three so there is some confusion there

speaker_1: Okay see a four is okay Uh like I mean see a recommended team size is three Okay so if you


See what happens is no if there are four people then I mean dividing work amongst four people will become too much So I would recommend a team of three okay


But if you are four people then you should be aware of the fact that when we are grading the assignments right we will take that into consideration that its a team of four and look for like more work

speaker_4: Okay

speaker_1: Good that you reminded me of that See assignment I hope that all of you have taken a look at the assignment Okay So what you need to submit is as Ive mentioned there is one Jupyter notebook So whatever has been given there as to do right that is the bare minimum thing that you should do Okay But that will not give you 100 percent marks


Okay that will give you lets say 70 to 80 percent marks if you just do whatever has been asked for Now the remaining 30 percent will depend upon like what will be the observations that you would be doing right And what are the kind of experiments that you have done Okay and also Im planning I mean this is not fixed yet Ill have to ask the TAs if they can do it But Im planning to have a Vaibhav okay for all


The assignments combined


Sometime at the end of the course we will have a Vaibhav where we will ask you questions on the implementations that you have done right at the end of the course So try to incorporate as much experimentations as possible and try out multiple ideas and the total evaluation depends on the quality and the quantity of the experiments that you have done


Okay so yeah so questions yeah I did it

speaker_2: Ah sir just a last question that this all assignments should be done in group right just reconfirming

speaker_1: Correct Ive told that so many times why questions

speaker_2: No no no I uh little kid was confused reading first

speaker_1: But why why where is the confusion I dont understand and what is the there should be a there should be some reason why you are confused no no so many times

speaker_2: No answer


No it was so many times Yeah actually I forgot that there was a no project separately It is only assignment Im very sorry for that Just reconfirm that Sorry

speaker_1: Okay see an Excel sheet was was circulated where teams had to be groomed and all that right I dont know where the confusion is Okay no problem Yeah where was I


Yeah it is not a separate document it has to be embedded in the notebook


Right And all the plots all the observations that you do has to be a part of the Jupyter notebook itself So what you submit is one file for assignment Thats all Nothing more

speaker_4: Should it come as one submission per team or in each of the team members will submit

speaker_1: Its about the same thing three times huh

speaker_4: No thats what I wanted to understand sir like uh how will the submission look

speaker_1: One submission per team

speaker_4: One submission per team

speaker_1: So unless there is lets say that youre in a team of three and one person sends me a personal email saying that this person did not contribute to the assignment and all that the rule is that everybody in the team will get the same marks for the assignment


Okay yeah so one file Okay so you coordinate with see there is one other reason why I ask you to do it in teams right Just need some compute resource So I recommend all of you to like buy some resource from like Google Collab or something right But cost some money You can divide it amongst three of you or four of you if you make teams


So that is like another reason why you should make teams Okay So anything above anything else about the assignments And I hope that the Python tutorial was done the last last week Did you guys do that


Was it in school


Okay okay So fine then I think now we have all everything that you need to start implementing and write the assignment Please get started with that okay Yeah So anything else any other logistic thing that we need to discuss before we continue

speaker_4: Just one last question

speaker_1: You dont have to export Its the code the corresponding observations See when you write I have asked you to plot a few things So I have to plot them to observe what you have done And as I said also do things that I have not asked to do or not asked for


Right So you can you can do more experiments than what I have asked for and you document that as well right

speaker_4: Yes sir but yeah the plots usually when we run the lets say uh matplot libplot

speaker_1: restart or the cells get lost for some reason then it would be lost right so is it okay to because embedding a image inside the jupyter notebook

speaker_4: I use it a lot because Im a

speaker_1: Thats okay no Thats okay embedded I mean its okay I mean uh But you have to embed

speaker_4: But you have to


Okay if the results are lost we can embed it uh as a

speaker_1: Yes you should have to embed right otherwise like how do we evaluate it I mean well not be able to run them


Again right well run some blocks for sanity check but its not that we can we should we can run all cells of everybody right So you should embed it you should embed all that


Anything else


Okay shall we start then shall we resume


Hello am I dead

speaker_4: So we can just go

speaker_1: Okay a quick recall of what we did the last time So we were looking at the adversarial networks for generative modeling


The idea was that you are given some data and what you need to do is


transform an arbitrary random variable into like another random variable of interest another random variable whose distribution is going to be close to the the data distribution thats the idea now what did we do we cast this as an optimization problem which would minimize a divergence metric between the true distribution and the data distribution so we could not uh there is


No way that we can compute that divergence metric because we dont know the underlying distribution so instead of that we created a


lower bound on the the divergence metric inside So once you create that lower bound you express that lower bound in terms of expectations over the true distribution and the generated data distribution which can be computed using the sample estimates right And the lower bound that we created okay involves another optimization problem over a set of a class of functions which we called as T of x


Now these class of functions we represented them as another neural network at T w of x And therefore you have like two neural networks one that is representing the transformation of the random variable which would generate the data The other neural network that would approximate this T function which construct the lower bound on the divergence that we are working with


okay then what happened is that the lower bound uh or the so called cost function will have the difference between these two expectations the first expectation is with respect to first expectation is of uh first expectation uh is on t of x with respect to uh px of the real data the second expectation uh is of f star of t of x uh and the x uh cap or this uh data expectation is over


the generated data okay now uh because uh since the lower bound itself involves an optimization problem over


uh i mean a class of functions so we will end up solving what is called as a saddle point problem where you have a cost function okay which is uh a function of uh two variables uh theta which are the parameters of the the generator network and w which are the parameters of the p network okay so that would construct the lower bound on


the m divergence So we need to maximize this cost with respect to w okay because that is what is going to create the lower bound and once the lower bound is created we want to minimize that with respect to theta such that the lower bound becomes close to or rather the m divergence is minimized or the lower bound on the m divergence is minimized such that the p theta which is the generated distribution get close to close to px


This is the overall philosophy of what we are doing And in fact if you recall I had shared that screenshot of a meme on the WhatsApp On a serious note thats exactly how a saddle point looks I mean which is like that I mean if you have seen that potato chips right the top of it is how a saddle point looks So basically there are the function has multiple


parameters right so at this at the point what happens is if you move along one direction


around the saddle point the function would increase if you move along the other direction okay at that same point the function would decrease that is what we are seeking okay which is the saddle point uh okay so any questions thus far


No no hold on uh see I never said that the other network is checking whether the image is real or not where did I say that

speaker_2: Im just uh checking is that the correct imagination what I am

speaker_1: Okay first of all when did I say that this T network is checking whether the image is correct or not

speaker_2: This is discriminator

speaker_1: But I never said what that is right I mean see that is an interpretation that Im going to like give today See in general this critic network is simply a neural network that would approximate this p function that creates a lower bound on entropy So its better to see it that way

speaker_2: I said this lower bound is not Im not able to imagine that

speaker_1: Thats what Im stating right Huh

speaker_2: Thats funny

speaker_1: See do you I mean do you recall this thing that we did the the one class before this we actually derived that law of bone right

speaker_2: you are going to explain about discriminator network

speaker_1: No I see I okay So its an important point which you made See even though I could explain like like what this thing would look like I would do it only for a special case right For the general case where you can take any F divergence this is not a classifier You understand See this T W network is not a classifier if you take your F divergence to be lets say the chi square distance


Okay the interpretation that you see like all over the internet and all these blocks et cetera right Therefore a special case of this where this I mean we took this right Which is if you make the f function to be corresponding to this Jensen channel divergence only in that case right this network becomes a classifier Or rather this network can be interpreted as a classifier Otherwise this is simply a neural network


That is trying to create a lower bound on the up divergence that we would want to minimize


Is it clear I think its very important to have that view that the I mean why do we have that other network We have that other network because you have to remember the entire story right Our goal was thats why Ive written this Our goal was that we need to minimize the F divergence We cannot do that and we create a lower bound on that Now this lower bound involves an optimization over a class of functions T of X And that T of X is what we are optimizing


Assessing using another network


Is this clear So there is see so far there is no like there is nothing that is trying to like classify between the real images and the generated images Ive never said that Only if you make your f divergence to be the general channel divergence this t function right which would still create a lower bound on the f divergence would take the form of a classifier And that is why that is when you can interpret it that way Otherwise this t network has no meaning


Other than just creating the lower bound on the F divergence that we want to minimize Is this clear

speaker_2: Yeah somewhat

speaker_1: Why so much where is the gap

speaker_2: I have gone through this uh time this the last week as well another time but I got this confusion to just interpret


I think I think with this class I may get more clarity or maybe if there is confusion I will ask in next class

speaker_1: Okay see you dont have to interpret it right It is simply a neural network that is approximating this t function which is creating a lower bound on the up divergence Thats all See one has to have this kind of a generalized view Otherwise you cant go deeper than what you see in these blocks et cetera right The only way to make that next level of jump is to start seeing things in an abstract way


Thats a glitch Yeah so these three lines that I have written right you start I mean your goal is to minimize the F divergence between two distributions We cannot do that So we constructed a lower bound Now this lower bound that we construct involves an optimization over a class of functions T of X And that class of functions T of X is what I am representing using a neural network Thats all


Im not sure

speaker_2: Yeah you were saying yesterday right Well look through a diagram that one graph that how that minimization happened right Once we construct a lower bound on

speaker_4: the discriminator network what we get then we plot it on a graph and then we further try to minimize it yeah that graph theta and

speaker_1: Sure Yeah again right I mean that would be for this case where your T network can be interpreted as a classifier

speaker_4: Because you know

speaker_1: See Ill do all that today okay That is what Im going to do now But as I said the most general case there is a version of GAN called LS GAN a least square GAN okay Where this T network is not a classifier that will become a regressor


So you get it So it depends It depends on what is the underlying F divergence that you have chosen for minimization If you choose your F divergence to be of this particular form then this T network can be interpreted as a classifier


You understand Otherwise it is simply a network okay or a neural network that is approximating a function T of x And what is that T of x function That T of x function is the function that constructs a lower bound on the F divergence that we would want to minimize


Is it alright


Yeah

speaker_4: Yes sir Yeah I was just reacting The thing is sir like does it make a difference if we do the minimization first and then the maximization

speaker_1: no no no no no no the order does not matter especially because you are you are doing it in a gradient uh based way no this thing how do we optimize this we optimize this using gradient uh based minimization right so it does not matter okay so then what did we do after that is that we looked at one instance of this f can right which is the naive uh uh can i mean that uh that was uh that that that you see everywhere where the f function


that that you look at will be of this form right u log u minus u plus 1 log u plus 1 by 2 in this case the underlying m divergence is called the Jensen channel divergence or JS divergence so for this particular case right if you


yeah if you for this particular case if you plug in this particular f and f star and all that the the final uh uh network right can be represented this way right where the t function uh if you represent the t function as a concatenation of uh uh the of of rather if you break down the t function as two parts right one that that is a that would take the x


and give you a real number and on top of it you have a sigmoid okay and this sigmoid is by definition gives you value between 0 and 1 the final loss function for this right looks like whatever I have written within this flow brackets uh now in this particular case right you can interpret interpret this t function as a classifier because the output of the t function okay is bounded between 0 and 1


Okay so that is what it is And then we looked at how to train this particular network in practice So you have this loss function J J cap which represents J cap theta comma W First you sample I mean you are given n points from the data and you have you are given m points from p theta as well right How do you get those m points You just sample m


points from the normal distribution and pass them through g theta of z to get to obtain these m points and then uh i also showed you how to compute right the gradients for both these networks and back propagate through them and train it okay i dont go through this again because we did it in in in detail yeah uh if you have any questions this far ill take some questions and then well move on to todays content uh any questions on this


Yeah uh thats a good point

speaker_2: Hi I said good morning

speaker_4: And so


log of dw of x and the other term


How did

speaker_1: Oh


No see f has a u log u minus u plus 1 log u plus 1 by 2 right Yeah f f star for this case has a log term there


Okay and you have s star of t w of x right so there will be a log term there that will come up

speaker_4: but that is an expectation over p theta right so how is it affecting a p expectation over p extra that was my question

speaker_1: You mean in the in the in the first case you are saying uh in the first term how are you getting this log d wx


Ah I see okay uh yeah Ill tell you how to I I think I did this algebra in the


Last iteration I think just give me a minute Ill tell you that


yeah so what we did is that see you represent this t function right the t function as see you look at this right so how are d and t related so d is the sigmoid of tw of isnt it


So now if you want to represent T in terms of D what do you do


The inverse of the T form yeah so thats thats where you have that log

speaker_2: Im not the T ball

speaker_1: Thats where you get that

speaker_4: All right sorry I sure uh that that explains so thank you so much

speaker_1: Okay so can you please repeat

speaker_2: So can you please repeat that

speaker_1: He was asking the question was that there is a T W term here right How did you get this log D W term Right when it is there is no F here How did you get this log D W term See how are this D and T related See again see the reason it is it looks a little complicated here is that the people the Gyan people just wrote down this loss function in terms of one network called D W Okay Now


in the terminology that we developed in this according to the NTK terminology what GAN people have called as DW is simply the sigmoid of our T function It is simply a fixed sigmoid of the T function Now there is T here right Now if you want to write it in terms of T how are T and D related

speaker_2: by the sigmoid relation

speaker_1: a sigmoid right which is which involves a negative exponentiation so if you want to write t in terms of d then there will be a logarithm right

speaker_2: Yes sir

speaker_1: Thats all So you have to invert the sigmoid basically If you invert that sigmoid T will be written in terms of log of T Thats all

speaker_2: Okay


Answer in the in the above term

speaker_1: Seven eight


Actually you can do yeah tell me

speaker_2: In the above term we are doing f star of t w of x x hat So basically we are replacing u in the divergence function with t w of x hat


And then we are trying to simplify like replacing TW with D as we have mentioned before using the synchronized relay

speaker_1: correct correct so you if you complete that algebra you will get this expression and if i have to do that algebra it will take me 30 minutes not worth it its simply algebra itself yeah


Is this all right now


Okay and I suppose that that like this training part right The forward pass backward pass everything for both these networks are okay Any questions on this Like how do you train these


Because this is exactly what Ive asked you to implement in your in your assignment so I hope that these are clear


Okay so if its clear then we will go to start with the next


Okay so todays agenda is that I will talk further about the GANs and the naive interpretation of how can you interpret it for this particular case Okay and then we will look at like a couple of applications of adversarial optimization for this task called domain adaptation and like image to image translation Okay there are multiple applications


of GANs I talked about it but well look at two applications and then if there is time we will start the variation autoencoder part also today okay that is what it is okay lets start so lets start with interpreting


Knife young


as classifiers


Classifier guided generator training


So this is simply interpreting the naive GAN right which is which is which is GAN and divergence as a classifier guided generative model Okay What do I mean by that Okay Let us recall that what are what are our setting So setting is that we have data points


coming from PX okay we have this particular setup


you have a neural network or some function that would transform


The Gaussian random variable


some other random variable which is random variable of interest p theta right now lets say that what is our goal remember that our goal


is to make


E theta


to peaks right that is this is what our goal is okay now suppose that there is a classifier


Does it classify it okay


which is just lets call that as DW of


is equal to one


X comes from Px It is zero if


Um okay I should actually make it


that not conditioned


Yes in occasion DW


x or x naught so it will take either x or x cap okay its one if x is coming from x cap or its then it is zero if it is coming from p theta


Do you understand what we are doing So there is a classifier okay a binary classifier

speaker_2: what about the other cases when x is not coming from px or x hat is not coming from p theta


We are saying that the this classifier will be 1 if x comes from px right correct What if x does not comes from px

speaker_1: Thats all itll give zero See this classifier takes either x or x cap as input Okay And it will give you one if x is from px It will give you x cap if it comes from p theta

speaker_2: It will give us zero if x cap comes from p theta


No what if X or X cap which we have drawn does not come from PX or PHI theta like

speaker_1: it should either come from px or from v theta right because dw is yeah dw has been set up in such a way that it either takes x as input or it takes x cap as input

speaker_2: Okay okay

speaker_1: So so its basically what is this this is a


Binary classifier okay


between samples of


samples of Vx and V theta


Is this all right Yeah its actually a binary classifier that would classify between the samples of p and p data Is that okay

speaker_2: Yes sir

speaker_1: Thats fine right okay now here is the question here is a question

speaker_3: What do you mean you

speaker_1: Yeah this reminds me of something Its just a slight off topic thing See the reason I erased it off is because if you look at the way I have written no it is


It is all the letters like are not aligned along a straight line correct


Thats why I erased it up wanted to write it again I remember three four days back I have a daughter a school going daughter Okay so shes eight years old She was writing something on a sheet of paper and she was not writing it along a straight line And I told her no no this is not the way to write it So I just reminded that to myself and said oh if I have to tell somebody to do something I have to first adhere to that


So writing along a straight line when you dont have ruled thing is a skill


Anyway


If my daughter sees if my daughter sees that shell ask me right I mean she you asked me to write a finger slide right there what are you doing


So that reminds me of another joke So I told her that she asked me what is that you teach So I told her that I teach math So then she asked me to like show me what I write Okay So I just showed her one day I had like taught back propagation and filled the board with a lot of these equations of back propagation derivatives and all that She looks at that picture and the question she asks is you tell me


that that you teach math but all that you have written is English right so there is no math here there are no numbers so everything that you have written is English here there is no math okay so anyway so the question that we should ask now is can this classifier


used


week


theta okay such that such that p theta becomes close to


So this is the question that we will ask now


So lets say that Ill write the classifier here lets say that we have this classifier


dw so this will take x or x cap as input okay and gives you a number between 0 and 1


Okay now the question that we are asking is can this classifier be used to tweet theta okay such that p theta becomes close to ph Do you appreciate the question Does did all of you understand the question


Okay can somebody answer that question So now I have given you a classifier okay which would tell you whether this the output of this or rather it will tell you whether the sample that it is seeing is from px or p theta Now I have to p theta okay by using this classifier in such a way that the distribution p theta becomes close to px Can this be done


Can somebody answer that Can somebody think of a way to do that

speaker_2: So that is the uh way we do it right like we train both the classifier and the discriminator

speaker_4: No no no I have

speaker_1: No no no I have

speaker_2: No no not okay sorry

speaker_1: Okay thats funny Ive never going to the top of the top of the top

speaker_2: Thats still F five

speaker_1: as far as as per as per as far as we have seen it now we are simply constructing lower bounds on f divergence and minimizing them thats all now the question that im asking is forget about everything that we have done so far right im simply asking you whether in this setup right where uh there is a neural network that would take the samples from a from arbitrary distribution and im giving you some other distribution ive given you a classifier that would classify between the samples of true data and the


of this neural network Now the question is by using this classifier can you make your G theta such that whatever it outputs is close to Px That is the question Now dont think about m dimensions now for a while


Okay so


I think please raise your hands virtually because otherwise it will become sort of chaos Sanchit you wanted to say something

speaker_2: Yes sir So if the samples are drawn from X we will get a 1 But if X hat is drawn then we will get a 0 So what we can do is we can try to maximize the overall like we can go for a cumulative sum of DW outputs and try to maximize that

speaker_1: Why maximize with respect to what See what are you tweaking here by the way

speaker_2: Sir like what Im uh like trying to see is like

speaker_1: No no Im not asking you what Im trying to say The question that Im asking is what is what handle do we have here What is that we can tweak See we can tweak theta nothing else The classifier is fixed


Okay so what we need to do is simply use this classifier to tweak theta Tweak theta you understand


Im asking you a philosophical question at a very high level How do you use this classifier to tweak this theta such that your p theta goes close to px is what Im asking


Yeah diva


of course see whenever we try neural networks we always use back propagation that is see i dont go to details now details will be worked out im just asking you at a philosophical level so now that ive given you a classifier i want you to use this classifier to tweak theta such that your p theta becomes close to px that is all think about it no yeah abhishek


what do you mean by that what do you mean but see again dont think of back propagation nothing right i mean just think think of it at a philosophical level i just want you to tell me how to use this classifier to tweet theta okay let me maybe answer because it will take some more time im sorry here this okay so what what is what i would do is i would tweet theta okay let me write that down


to answer to that is that keep


Changing theta


data right till


The classifier trades


Okay so what is that What do I mean by that So what I do is I will take a theta okay and I will see the performance of the classifier Now classifier is doing pretty well okay So then its not useful for me What I do is Ill keep changing theta till such a point okay where my classifier completely fails


Understand


Now when would my classifier fail So now the next question is this implies that if


Classify a failure


Then okay then P theta is actually equal to P thats my claim do you agree with that


If this classifier cannot distinguish between the samples of px and v theta when would that happen That would happen only when px is equal to v theta isnt it


You understand


Yes sir The classifier would fail only if px is equal to p theta So now what Ill use Ill just simply use that Ill invert this logic and say that okay now if I have a classifier that would classify between the samples of px and p theta I would keep trying or rather tweaking my theta okay till a point where my classifier starts failing


You understand this

speaker_2: Yes sir

speaker_1: Okay so this is how like a lot of these blog posts et cetera would motivate GANs Okay theyll say that oh theres a classifier and you want to make that classifier fail because only when that classifier fails then your p theta will go close to px will be exactly equal to px Okay


But there is a catch here Ill tell you what the catch is Yeah I think there are some questions

speaker_4: Yes uh are we saying that now at in at this stage the classifier is perfect that its able to distinguish between x or x naught

speaker_1: Whats what stage at what stage

speaker_4: So so now I mean with this assumption that the classifier is able to do that right So are we already saying that it is perfect at doing this

speaker_1: So when we start when we start right I mean we are assuming that okay the classifier is able to classify


Right But the argument that Im going to give you in a while will tell you that it is not enough if you just make the classifier fail See this thing that I said no that if the classifier fails then p theta equal to px right is not completely true


Okay I dont know if you can see that failure case already but Ill show you that Ill show you that in a while But yeah any other questions Sanchit Yeah

speaker_2: Im not sure if you are going to cover this question ahead but just asking so change tweaking the theta randomly it will take like really really long time so do dont we have some parameter that will govern or that will tell us okay in which direction we have to tweak theta

speaker_1: Yeah that is correct That is correct But yeah well see how to do that Yeah itll see the direction now is simply that it should be in such a way that the p theta should be close to equal or should be close to px That is the direction that we are talking about Anyway so now I mean if all of you are convinced that the classifier fails that p theta equal to px this is this may not be true always Ill tell you why


However that


Okay uh classifier fail you okay classifier


Feeling okay


need not imply


P theta is equal to Px Okay Ill show you a counter example for this


Okay so lets say that our features are in two dimensions okay The data is in two dimensions Lets say that my true data is like this it is


is clustered somewhere here this is only for representations okay so this is the samples from px okay now lets say that when we start arbitrarily with uh with some uh g theta okay i will have data or rather p theta x cap this is my x cap


X cap is now sampled from P theta Okay Now lets say that there exists a classifier that would classify between them This is the decision boundary This is my DW


Now okay so first of all please note that in practice neither Px nor P theta would be nicely clustered like this and they are not linearly separable


Okay so Im simply you know this is for illustration purpose Im assuming that they are linearly separable and there is a linearization boundary between them okay But it did not be the case okay Now what are we saying That we have to change theta such that the classifier fails correct


Is that okay Now what is the decision that this classifier is making So


A gold design


Below the line


We did that correct


This is the way the classifier is classifying so do you agree


Whatever this E1 below means


Okay this is what the classifier has learned Now this has to fail What do I do So I am I want to tweak my p theta such that the classifier fails no What I will do is I will just move this


Let me call this as p theta 1 and this is coming from p theta 2 Okay now here


DW would fail do you agree


Some of you agree that DW would fail here


Yes sir


Yeah but now DW has failed but has it ensured that p theta 2 is equal to px


P theta so does not equal to P x


You see that right so now


Its not enough if you simply make the classifier fail The classifier can fail right Not only when p theta is equal to px Of course when p theta is equal to px classifier would obviously fail However if classifier fails that does not imply that p theta of x p theta is


is px do you see that


this in place


P theta equal to Px okay


In place


Actually play it for me


But classifier failure


Does not imply


theta being equal to bx


Is this clear Any questions on this in the mid

speaker_4: Here when you are moving X hat above the line will discriminator not address the line to again differentiate between these two

speaker_1: Good question we have not done that yet right have we done that

speaker_2: No but discriminator will do no

speaker_1: No no no we have said that the classifier is fixed here right and by the way I have not used the word discriminator I am simply saying it is a classifier


So when I told this in the first class I said you know please use the terminologies and the names that Ive been using I mean I understand that it is difficult because you already know all this right from other sources but its good to use because theres a reason why Im using those names For now this is a classifier okay So classifier is fixed Im not changing the classifier


Okay now if the classifier is fixed then simply moving theta such that the classifier fails does not you know does not suffice does not serve our purpose


Those are the ones

speaker_4: Exactly

speaker_1: Yeah simple different sample This line is fixed


I dont know who he is yeah but yeah so classifier is fixed or when I say classifier is fixed this is of course this is the classifier that Im talking about it is fixed


Uh Harish

speaker_4: Sir uh one question so our goal is to make p theta equal to px right

speaker_1: Correct correct

speaker_4: In that case why do we need a classifier for example so we can just use a regression problem to find the loss and just use

speaker_2: generator right

speaker_1: Now what what do you regress over See what do you regress over X cap comes right Do you match every X cap to some X Is that what you do


So what are you suggesting that I just make this take a split or loss and then minimize this See if I do this then what will happen is the this neural network would simply generate whatever is there in your data It will not generate anything new


So you want to do it at a distributional level no Thats why they are doing all this yeah

speaker_2: So we need to understand the distribution rather than just using the samples

speaker_1: Absolutely that is that has been our problem from day one isnt it We want it to be done at the distribution level


Not at sample level right Okay So now the thing is yeah so all of you got this right I mean using the classifier and trying to take in your p theta such that the classifier fails is not enough You need to do something more What do you think is that something more that you can do

speaker_3: Maybe the dye or the discriminant should dynamically learn

speaker_1: Yeah so you move the line What you should do is you move the line okay If this line okay so what you do is first you have to make this so this is DW1 Under this DW1


This happened Okay What I will do is I will learn another line here I will learn another classifier Okay This is now


I TW two


Okay now I have to move this P theta again to ensure that this is misclassified under DW2 as well


Good idea


Which means that this P theta 2 now cannot go to P theta 1 place okay it has to go to somewhere else so lets say that this will this will move somewhere here


Okay so now the idea is so this will become P theta three now The idea is you know keep moving your P theta cluster distribution right So till a point where these two overlaps Now how do you do that You do that by tweaking this classifier okay All in time maybe I should have written this classifier in a different color


These are the axes and you have


The first classifiers


TW1 okay and you have another classifier which is


Like this this is TW2


that all right you see whats happening so basically we are so


Therefore okay the classifier okay


stoopid


change


tweet simultaneously


Does it make sense


Now you might ask right so now what is the guarantee that uh


What is the guarantee that when I keep doing this I will ensure that my p theta is exactly overlapping on px right It can actually play a cat and mouse game right where the classifier places moves this to some place and then the generator tries to avoid the classifier and they keep kind of playing that game between those two correct


You understand So in this case what can happen No this cluster moves here and then itll come back So then when you try in the new classifier itll go again here and itll come back and itll keep it can keep moving around Can all of you see that That this moving around can happen


So that is exactly what is called as mode collapse Okay Where the the the the GAN training right is very unstable You will actually see that when you are training So what happens is that the so called classifier right when you are training the classifier tries to avoid the discriminator and the discriminator rather the generator and the generator tries to avoid the classifier and it keeps happening happening alternatively Now what is actually happening underneath you under the hood is every time you


this classifier right you are creating a lower bound on the f divergence you understand so what do you mean by creating a lower bound on the f divergence is uh learning a new classifier now you can see that right the tighter the lower bound is the better the minimization would be isnt it


Obviously right the tighter the lower bound is on F divergence the better the minimization would be What do you mean by creating the tighter lower bound is that you create a classifier that is close enough or a very good good classifier And in this example Ive created a very degenerative case where the classifier is linear and the data is very nicely clustered But in practice right you will have these points here and you will have X points here and the classifier will be a nonlinear classifier right So classifier will do misclassification okay


However the tighter the lower bound is the better this classifier would be Thats how the translation happens in the sense that when the case you consider the F divergence to be general channel divergence right you can you can look into this as interpret this as a classifier right And because you can interpret it as a classifier constructing a tighter lower bound translates to creating a classifier that is very good Okay Now if your generator function has to like make


very good classifier misclassified okay it would better move the cluster close to px because if there is a perfect overlap between these two right px and p theta there is no classifier that is able to classify these two you understand that


Do you see that If there exists if if px completely overlaps with p theta then no classifier can classify between px and p theta right points from px and p theta do you agree


So what would that translate to That would translate to saying that your t function right or the script t function is representative enough to give you a t x such that the lower bound that we have created on the f divergence becomes tight There is no approximation here The lower bound becomes exactly equal to the f divergence If it becomes exactly equal to the f divergence then minimizing that would make p x to be equal to p theta right And which means in this case objective channel divergence


is no classifier that would uh that would classify between the points of px and pj


Is this clear


So constructing a lower bound is equivalent to finding this class new classifier right given a particular px and p theta constructing the lower bound on f divergence is equivalent to finding out this classifier that would classify between these two


Okay and minimizing the lower bound is equivalent to moving this p theta


in this space of data such that it will go very easily to the last one

speaker_2: Are you using a pointer sir

speaker_1: Unfortunately there is no pointer in this it would have been so nice if there is a pointer does anybody know if there is a pointer here


Yeah so yeah Im not because I dont I cant use a pointer is this clear


So before you ask your questions right let me just complete this story and then So now instead of writing f divergence and all that right now we can if we have to optimize this so I will write this as a cost function right So what we have to do is


Lets say that my X is coming from


appears right then I want the log like okay so this


Okay let me write what Im trying to write so this is like formulating


formulating the cost okay via this interpretation so what I will do now


Okay of course we still have the exact same setup okay Setup has not changed So Z comes from normal 0 1 and you have G theta of Z and what you get here is X cap that comes from P theta Okay suppose suppose


DW okay


is a function from x to space of zero and one Okay now let


PW represent


Let DW represent


the likelihood of


likelihood of a sample


coming from px okay this is the way i have defined pw right it simply gives you the likelihood of a sample coming from px so what do we need so whenever


It comes from


We want it to be maximized no A classifier should maximize the likelihood okay Or lets say P is our P theta It simply gives you the likelihood of P is our P theta okay So whenever X comes from P is I want to maximize that likelihood under the expectation Do you agree


This is


Ill write a max here so I have to maximize maximize


likelihood of


Okay X


coming from VX this is that term do you agree


Let me write it as Px for a by u Is this okay So this term is simply maximizing the likelihood of log likelihood of x coming from Px Is that tolerant It is lower w


Hello is this alright


Now now so what is log of


And I discuss


What is one minus T W of X What is this


Thomas


What is this term

speaker_4: likelihood that it comes

speaker_3: Mm

speaker_1: I clean up

speaker_3: Yeah

speaker_1: XGAR is not from VX


Right or in this case


comes from P J Ta


Correct is it okay


Now what do we have to do well have to

speaker_4: speed theta

speaker_1: So maximum that x cap is not from px oh yeah this is from v theta correct thanks


We need to maximize this as well right We need to maximize Okay Ill have to write that in the same notes


Now when X is coming from X cap is coming from B theta


need to maximize this with respect to w so this dw which is a classifier has to do two things whenever x comes from px it has to maximize the the likelihood of x coming from px whenever x is not coming from px or rather x cap is coming from p theta it needs to maximize the


inverse of the log likelihood rather one minus the likelihood of x coming from px to u You see this point


So the


Objective


Classifier training


Whenever the X is coming from PX this maximise that likelihood


And whenever excess


not coming from P so rather its coming from P theta you maximize


log of one minus that likelihood


And I need to maximize this with respect to W


Is this clear to all of you


Okay now now what do we have to do see the are now the objective


Generator training


What is it what is the objective for generator training now


Simply


You know what


the objective for classified landing


Because what do we why do we have to do that The here the objective is to have made the classifier fail no


Now how do we do that

speaker_2: Its a

speaker_1: classifier is yeah if classifier is maximizing something you just minimize that you just completely undo whatever the classifier has done so if i call this as some j okay of theta comma w now you need to


classifier is maximizing J theta comma W with respect to W then


generator


will minimize the exact same objective with respect to theta therefore the complete GAN training is


you have this j theta comma w okay the classifier has to maximize this while the generator has to minimize this so again we came into the saddle point problem


this is what you see in a lot of blog posts and you know the popular uh explanation of what gan is including the original gan paper they say that okay we have a classifier so we need to for tweak the this is this what is called as the discriminator right because its basically a classifier discriminator is it just discriminates or classifies between the points from px and p theta okay and now you have tweaked the classifier in such a way that px is going


to go to p theta it is not enough if you just try in the g theta because the classifier can fail even without making px equal to p theta so you have to tweak try in the classifier also along with the generator alternatively and the classifier objective is given by just maximizing this is the cross entropy objective right and the generator has to invert what the discriminator is doing and thats how you get into a saddle point problem okay however remember that this


is this interpretation is only when you assume your f divergence to be the Jensen channel divergence in which case the t network right that would create a lower bound on the f divergence happens to be a classifier it can be interpreted as a classifier now you can see the nice connect right see this objective function right is not some magical thing that just emerged okay it had a very nice grounded mathematical interpretation


where this maximization is actually creating the lower bound between the m divergence between uh a lower bound on the m divergence between px and p theta right so once you create that lower bound you minimize that and you alternative between creating a tighter lower bound and then minimization okay if you see that from you know if you take one particular m divergence and interpret this dw as a classifier in that case you can you know you can write it this way but it is not


this way of interpreting is not im not a big fan of this because its too hand wavy right i mean you


yeah i dont know but its just my choice uh see i would see like no more uh value and more in a more principled way of understanding in saying that oh you start with an f divergence you want to minimize that and to minimize that you want you dont know px and p theta therefore you construct a lower bound express them as expectations over these two because you can compute them and that lower bound happens to be an optimization over another class of neural networks okay and you construct the lower bound and minimize that


you keep alternating between these two so thats my way of looking at it but if you make your net divergence to be one particular f divergence called Jensen Shannon divergence then this t function that is used to create the lower bound on the f divergence can be interpreted as a classifier and the rest of the story follows


Is that okay It is just one other interpretation or rather the popular interpretation of what the general case of F divergence minimization is And again you can see why it is called ad hoc serial optimization right You have like a saddle point problem right Ad hoc saddle point problem or


Adversarial optimization


Because there are two neural networks one which is trying to undo what the other does okay it is adversarial optimization


Okay so finally right like post training Ill take questions after this Post training I dont know if I told you this last time post training inference What how do you do how do you scan for inference


is that to take the


Try the generator


Throw away the discriminator completely


Discriminator is like a poor teacher right once you learn from them you just throw them away


And this X cap comes from P theta now this P theta has become close to Px


In fact theres a nice Zen saying okay this Buddhist Zen saying which I hold very close to my heart which I keep telling all my students I dont know if Ive told you this It says that a good teacher okay is one who becomes redundant or useless after some time


So that is the definition of a good teacher or a mentor So you should make your mentees right or your students independent of yourself after some time Now if you keep you know keep your students your students or keep your subordinates or mentees your mentees for all your life you will become a boss right Not a good leader or a teacher A teacher should become useless after some time So after this course is done you should not be coming back to me because


Like you have actually got everything that you want youve become so independent that you can do things without a teacher My teacher told me this right And Im just passing that to you In fact there is another nice saying that says that if a student is ready the teacher appears Okay When a student is really ready the teacher disappears


very nice its very deep actually right so the the goal of a teacher is to ensure that the student is ready which is that you know your p theta is what the distribution that the students are in right and you want them to go to px once you have used whatever methods now you can become like an adversary you can score them do whatever and you just invert whatever they are saying in an adversarial manner once they have become theta star right go away there is no use for you right


So that is what it is right During inference what you do is you sample a point from Z you get a sample from a normal distribution Passing to the generator you get a sample X cap right That is from P theta now which is close to P X So I mean if you remember I showed you that no this person does not exist dot com right Every time you do an inference or rather the refresh of the page what is happening is a sample from Z is coming and it is going through a trying generator


And a new sample is getting generated from PMX Okay so now ideally


ideally right X cap okay is not in D Okay the data set that you have given no your new generated sample will not be in X plus you take C Z1 through ZK youll get corresponding X1 cap through XK cap okay none of these okay are in D So there are new samples that are not in D Thats how you do inference This is also called generation


Okay see we have still not done what is called as unconditional generation This is still sorry we have not done what is called as conditional generation It is still unconditional generation because it is not that okay you give a text and a corresponding image gets generated right It is simply an image gets generated okay or a data point gets generated without any conditioning So in the next part of the class I will talk about how to train this or how to convert this into a conditional generator in a while okay


But yeah so this is how you do inference So we are done with training We are done with inference This is how you do training of a Dyan and an inference Ive asked you to do both of these in your assignment So to implement them So one other detail


Uh see there is I have asked you to implement something called a deep convolutional neural network okay


So abbreviated as DCGAN


What is this A simple thing right So you start with you build a neural network right G theta network You start with G okay that is lets say in some 32 dimensional space Okay let me write that So you sample G from a Gaussian distribution


Okay and that Gaussian distribution is in some 16 dimensional space lets say


16 dimensional space okay so now you take a vector that is 16 dimensional okay then you have to go to lets say that your data x is in some r 100 cross 100 now how do you convert the 16 uh dimensional into 100 cross 100 see one thing that you can do is you can have 16 and then you have lets say 32 then you have 64 and you know you keep increasing the dimensions till you have like a 10 000 dimensional vector okay


So this is your X cap this is your neural network G theta And then after you get this X cap then you can do a reshaping


So its got


X cap is in R 10000 cross one dimensional right which is a vector And once you get this you reshape


into 100 by 100 so that you know it will look like a grid of images okay and you have to do the same thing for x no x is in 100 by 100 right so when you send it to the discriminator you should reshape that


into 10000 cross 1 So you reshape X into 10000 cross 1 and you reshape X cap into 100 by 100 This is one thing that you can do and this neural network is a multi layer perceptron net or a fully connected neural network Okay We have seen how to do this back propagation and all that This is one way to do it The other way to do it is that you start with a 16 dimensional vector okay and then do what is called as transpose convolution or upsampling


Does all of you know about the convolutional neural networks here CNNs Is there anybody who does not know about CNNs


Okay Ill take that as an X So assuming that all of you know about CNNs right So what you can do is see what does a CNN does a convolutional network does It will take a grid of images like this and you have a kernel which is lets say a 3 by 3 kernel You place that 3 by 3 kernel on this grid okay And take the inner product and you get another grid okay So every point in this smaller grid will now become an inner product between these two and one number And you you uh move this


3 point 3 grid again and you get the next uh thing and so on right that is how you do it so this is convolution there is something called transpose convolution where you start from a lower dimensional uh uh uh vector right and then you create a grid okay by doing inverts of convolution that operation is called transpose convolution see i will i mean you can ask ts to do it in the next ts session okay how to do transpose convolution


However there is a there is a paper called a paper on a write up called convolutional arithmetic


Okay so please refer to that There they have given how transpose convolution works So if you use transpose convolutions right you can finally get


uh at the final layer right you actually get a grid of


You can actually make it uh the grid of whatever size that you want I mean if you are using a color image that is what Ive given you it will be like 100 cross 100 cross like three channels right RGB


Okay by using transpose convolutions you can get into get that into a 300 cross 100 cross 3 You dont have to like reshape it And the discriminator that you have here right


simply become a CNN so it will take a 100 cross 100 cross 3 vector itself okay and give you a number between 0 and 1 this will be a proper CNN okay you can use a ResNet or whatever network that you want


Okay so let me not present this next


You can ask TS to cover this if you want right What is transpose convolution And so this if you use instead of using multilayer perceptrons if you use transpose convolutions this entire thing no This is what is called as a deep convolutional GAN DCGAN where for a discriminator you are using a CNN okay And for the generator you are using transpose convolutions You are not flattening them out Thats your DCGAN


Okay so thats that So we will take a break now and then maybe go to Ill talk about the conditional GANs and I mean the some of the applications of GANs as I promised Before that Ill take questions on this if there are any

speaker_2: So two questions One thing you mentioned is this classifier interpretation holds true only for

speaker_4: for this JS divergence Why is that so


Why is this specific only for GST tax regions

speaker_1: Big fat


For others okay for others this will become a the the I mean this thing right will not be a classifier between 0 and 1 right this network will give you a a real number see depends on if you recall the output of the t network should come from the way of f star isnt it


So that domain of f star for this case will become 0 to 1 For the other cases it will become a real number So in which case the output of that network will become a regressor It will not I mean whatever the case might be you know its not a you cannot interpret that as a classifier


No distinguish between in the other cases no so how can we interpret

speaker_4: No distinguish between in the other cases no so how can we interpret

speaker_1: But what about

speaker_4: What the

speaker_1: I understand

speaker_4: I understand

speaker_1: I understood the question so did it to me you cannot interpret that at all


So there is no classification that is happening That is why I dont give this as the you know the ultimate interpretation Because only with Jensen and Diversen this becomes a classifier For other diversen it is not a classifier For instance there is a paper called as I said no LSGAN where what is getting minimized is chi square distance Let me just show you my screen and that will become like maybe more apparent


You see my screen


Look at the sun


For different divergences the final output activation is different for Pearsons chi square distance the output activation is a linear function so which is a regessor


You understand Yeah So only with Jensens channel divergence you have this kind of thing which is bounded between 0 and 1 which becomes a classifier Now if you use the KL divergence etc right you just have a line thats all so which cannot be interpreted anyway

speaker_2: Yeah and the second question

speaker_1: See hold on hold on the way to the way to interpret that as if you want to right it is simply a a neural network that is creating a lower bound on the underlying f divergence

speaker_4: Hey hold on hold on

speaker_2: Mm okay


want something different So you also mentioned that the X hat that comes out is is not in the D

speaker_1: Yeah yeah

speaker_2: Can we really ensure that Or but the question is if you

speaker_1: But the question is if it depends on if it depends on how tight your lower bound is


If its very tight then actually you will get two pairs no which means that you will get very diverse samples


No because you are meaning we are doing that at the distributional level Thats the whole point Okay Okay The whole point is that you have you have made the distribution same See why did we even start with all this F divergence et cetera is that we dont want to overfit right I mean overfitting in in the case of generating models is when you match the distributions exactly Sorry when you only match the samples not at the distributional level

speaker_3: What do you want me to do

speaker_1: So youre actually

speaker_2: If you ensure the distributions are same because we are doing a random sampling you wouldnt get the same

speaker_1: Absolutely yeah random sampling is happening because your input right its actually converting one random variable to the other youre still yeah

speaker_2: Three new points okay


Exactly yeah

speaker_1: so but you have to ensure that the distributions are matched so if the lower bound that you are that you are constructing is very weak right then you will not match distribution because you have you have you anyway minimized a very low very loose lower bound on the f divergence

speaker_2: I understood

speaker_1: That is why people say that the end training is very difficult One because youre solving that saddle point optimization problem The other thing is the lower bound that you might get might be very very loose If its very loose then if you look at that classifier interpretation your classifier is simply trying to move it in different places without ever overlapping it with PX


And also I didnt tell you last class right What is the stopping criteria in training this There is actually no not well known stopping criteria for this okay The only stopping criteria is when people just eyeball the quality of the images or the data that is generating They just have some pseudo metric to generate what it is I mean the pseudo metric to measure the goodness of the samples and then they use that to stop


one good stopping criteria so is that because we

speaker_2: Is that because we is that because we do not know what is the really the tightest bound that we can get

speaker_1: Exactly and also we dont know the what the underlying distribution is no


it see also now next part of the class ill talk about this vessel strains distance and uh uh and uh uh fid right there is a score called fischetts inception distance which ill talk about the next time that is one thing that is used to monitor the goodness of the generated images but stopping criteria is just that you eyeball the images and see the data and use some surrogate losses and just stop there

speaker_2: Yep thank you so much

speaker_1: Yeah sunjet

speaker_2: in this example which you had mentioned right where we are considering this classifier dw1 dw2 dw3 why not keep the existing classifiers when going for a newer classifier like what i mean to say is instead of going for the single layer perceptron method why not for a multi layer perceptron here so that we have the other classifier

speaker_1: Im sorry I didnt follow your question Can you repeat it again

speaker_2: Okay what I am saying is once we move from DW1 to DW2 right you are saying that it is likely possible that P theta 2 might take the positions of P theta 1 correct

speaker_4: Correct correct

speaker_2: Now if we have DW1 intact and then we go for DW2

speaker_1: No there is no impact no we have changed the classifier

speaker_2: what sir thats what i am trying to say if if we are going for a change right lets lets instead of going for single layer perceptron we go for multi layer perceptron

speaker_1: no no no see multi layer perceptron will not tell will not uh prohibit the class the decision boundary to go somewhere else not go to the previous layer no that has nothing to do with single layer multi layer see multi layer single layer which will simply tell you whether the decision boundary is what is the range of decision boundaries that you can learn


See there is no remembering of the classi previous classifier that is happening here you are just reiterating it completely

speaker_2: No sir what Im saying is we go for a multi layer perceptron approach like we say that okay we

speaker_1: Okay see again please understand what a multi layer perceptron is a multi layer perceptron is simply a deep neural network that has multiple layers thats all

speaker_2: Yes sir

speaker_1: So it does not mean that you are remembering something and all that here it is simply a neural network


An MLP is a neural network thats all


Understand it is simply a multi layer perceptron did you under did you attend the tutorials

speaker_2: Yes sir

speaker_1: In tutorials they talked about multilayer perceptrons and training them huh

speaker_2: Yes it is

speaker_1: so a multi layer perceptron is where a neural network i actually talked about a multi layer perceptron in the last class if you remember what is a multi layer perceptron you start with take data okay you multiply it with w transpose x and then you make that go through a nonlinear this is the first layer the second layer is you take w2 and then you do another nonlinear this is second layer this is the third layer and so on this is an mlp so the architecture will look like this now you start with this have a fully connected network


You have W2 you have W1 then you have W2 This is an MLP which is a deep neural network It has nothing to do with the classifier remembering what the previous state is and all that That is not what we are doing Do you see the difference

speaker_2: Yes sir I agree on that But maybe uh maybe I the terminology I used was not correct What Im trying to say here is that why not

speaker_1: Why not remember what the classifier was at the previous state right

speaker_2: Yes sir it might not remember but if we go with this approach of multi layer perceptron then we might have a tighter


Hydrophobic on the surface

speaker_1: We are using multi layer perceptron We are using multi layer perceptrons We are not using the linear discriminator anyway here right So these are neural networks These are deep CNNs Even if you are using deep CNNs see the note that your data is in some very high dimensional space and it can always go to a place where the classifier misclassifies

speaker_2: Okay

speaker_1: Right So it has nothing to do with the capacity of the classifier We are talking about data in some 10000 dimensional space here


Okay uh any other question S Sarvek

speaker_4: Yes so this transpose conversation that you mentioned So for this the input in the Z should it also be in a grid format or we can use 1D

speaker_2: Its a fantastic

speaker_1: That is a design choice People have seen both happening But people generally take people take Z to be a vector right not a grid


Let me share that show the DC current paper with you

speaker_3: It doesnt look

speaker_1: But uh hes appreciated


And also this convolutional uh arithmetic also is something that Ill show you hold on


We are talking now about convolutional automatic


therapeutic


So into convolutional arithmetic for deep learning class Ill show you both of them


You see my screen No not yet


You see my screen


Now this is that convolutional arithmetic thing okay So have a look at it They talk about all kinds of convolutions with striding without striding zero padding without zero padding They have pooling arithmetic You see there is this transpose convolution here


Okay so please have a look at this Okay this is one thing The other thing is this let me start


EC cant type up


just the DC can paper


This is how they do it So at 100 dimensional Z and then you reshape and then you have transverse convolutions transverse convolutions and then you get to 64 cross 64 cross 3


Start with a hundred dimensional uniform distribution Z is projected you caught it no

speaker_4: Yeah so vector only is converted to start from vector and then you yeah then you do

speaker_1: from vector and then you yeah then you do the trans correct then you do upsampling transpose convolutions and then get to the final page dimensions


Okay anything else

speaker_2: Sir can you please share these uh documents which you are presenting

speaker_1: What did he miss

speaker_2: Well be right back

speaker_1: We cant like


Okay done Okay lets take a break It is 11 point 5 Lets come back at 11 point 20 And yeah continue from here


Okay see you in about 15 minutes


Yeah you can hear me Can you see my screen

speaker_4: No no no no

speaker_2: No

speaker_1: So which one should I show this one


See you on screen start broadcast


Ill be right you

speaker_4: Yes yes

speaker_1: No you can see my screen as a boss right

speaker_4: Thats the p theta its next thing we should have mentioned as p its before the objective for classic classifier training site that was

speaker_1: Uh come again

speaker_4: Before the object before saturation thats likely to be that X before that light


before that


Can you go above a little bit Yeah here if you mention comes from P you mention the P deta to deta right

speaker_1: Okay thanks


Okay shall we continue


So we can look at some of the


See there are after the scan thing came too many improvisations over it a lot of papers a lot of applications and all that So in the interest of time Ill only cover a few of it a few of them


I mean nevertheless GAN is now not the state of the art for like generative modeling right I mean people have moved to diffusion models and so on But anyway so I will cover a few of them and rest you can read with this kind of a background The first thing that we will do is what is called as the conditional GAN okay


conditional plan okay what is the objective here the data is is given like this so you have


Samples like this you know X one comma Y one


Lets talk now I do


and so on sorry its not small its got the x x and comma y in okay so you have data this way where ill tell you what this y is okay so this uh coming from lets say p x y some distribution now the x example can be like this you know x can be lets say images okay


Now why cant we class labels


with glass labels or okay some textual embeddings


We will actually make this idea a little more concrete when we go to text condition diffusion models and all that But yeah so for now let us say that these are


Textual embeddings


But for


Or is it its class labels for X right or textual embeddings for X and if you have data like this the objective is objective is


To sample from sample or generate slash generate


The conditional distribution


Just P of


x given y so this means that you know there is you will get x given y equal to lets say some class or some text


Okay so this is class conditional generation right Given a particular text or a prompt or a class label you need to generate the corresponding image How do you do this is the question Okay so


are doing so now to do it is the problem is now


Modernly


Okay


P of x given y okay instead of


instead of px using p theta so now the thing is the setup is exactly the same so you have this


Z theta of Z clear


found this um


Thanks guys


Now this takes Z


It shows some working offline is my screen still visible

speaker_4: Yes yes

speaker_1: Now you need to generate from a like px given y right So what you need to do first is that you condition this generator generation okay with y Now how do you do that is that just add y as another input here So y goes as another input


Now what happens is that you need to the p function


the discriminator


Pass two


Classify between


samples of


P x cubed y okay and


P x cap given away of course theres dependence on theta okay now this is now sampled from P x cap given away so now how do you do that is that for the same P network that you have the discriminative network


PW okay sorry it is network


What you do is simply


have this x or x cap that is going on as input anyway now you add additional y as input to this thats all thats all it is now the everything else remains the same so now the cost which is j theta gamma w right we will look like this so now the expected value of log of dw okay so this dw now takes x and y both as input the expectation is now with respect to x given y


sample from P X given Y okay plus that other term which is expectation of 1 minus


Whats that term log of one minus right


I dont like this


PW of X cap comma Y okay


I can actually say that x and y comes from this yeah


x and y are coming from this and we have x cap x cap comma y coming from p x cap given y conditional theta


Next slide


So this is a conditional GAN now during inference right or inference post training


So what you do is that


take T theta


GT dash dash OC okay


Now sample a Z from normal 0 1 okay and you give a a class label


or text embedding as input


is your y and generate x given y equal to some class table


Our text editor


Now this y right can be represented as a one hot vector


So if its a class


Okay now it can be represented as some embedding vector


If its a text


basically there are these embedding vectors no tf idf or like you know some bird embedding or something dont worry about this so basically you represent a a text as some sort of a vector right i will talk about all this bird embedding how do you generate all this later in the course anyway but yeah so its some vector that is representing the label just give that as an input to both the generator and the discriminator and solve the same optimization problem and post training you just take that and give it as an input to the


the train generator this will do what is called as conditional generation it will just show you some examples of this so also all c g m conditional


Can you see my screen


See this right is exactly what I had written here X given Y and you have like you write it as Z given Y I mean its basically G generator network takes Z right and given Y thats what it means So what happens in terms of network You have Z you concatenate Y to that and give it as an input And the discriminator it takes both X and Y concatenated together


Now look at the results right So this is for MNIST So MNIST is our generated data Every row corresponds to one particular digit So they have conditioned it on the class labels


And yeah so they have again conditioned it on text This was a very old paper it is 2015 paper So there the 14 paper right The embeddings were not textual embeddings were not that great there So this they have done class conditional generation for MNIST And I think in your assignment I have also asked you to do a class conditional generation for the data set that I have given Okay so that is about CGM Okay any questions on this


Yeah Sandhya Sandhya Tana Mohan

speaker_2: Sir yeah sir here X is just limited to images or it can be some

speaker_1: So it can be it can be anything See Ive been telling this from class one right GANs are not restricted to images It can be like speech People do text people have done text to speech using GANs No that is some of these models So condition it on text and generate speech So that can be done as well

speaker_2: Okay like like

speaker_1: Can you share the screen

speaker_2: Like we have the transformer algorithms right like where we give a prompt of text and

speaker_1: No no that is not see that is not adversarial trained those are


autoregressive models okay so gpt etc are autoregressive models we will talk about that as well later in this is different this is not see this is adversarial learning this is a gam this is not a autoregressive model this is not a gpt

speaker_2: This is different

speaker_1: So this is text conditional generation of images right I mean its a GAN that is trained which is minimizing the underlying GAN divergence


Okay


Uh okay one other question by


Cartik Kumar

speaker_4: Yes I just wanted to know about why Why are we training Why is it like a range of values in the sense that we will give all the classes that it need to for example if it is class labels we will give all the classes to which it need to train itself so that during inference we will be giving one among that class So why would what would be the range of why I mean like


A how come

speaker_1: I did not understand your question

speaker_4: So for example if we are training at the case of images right and we are giving a next prompt as you shown in the video like in the paper that okay find the mountains in

speaker_2: Or something in that sense that can be why right Is my understanding there correct

speaker_1: Uh no see why okay so uh for now lets say that its class 10


It is simply a class label no

speaker_2: Okay so it can be something like is it a human or is it a yeah

speaker_1: Yeah represent represent that as a one hot vector so you know what one hot representation means right

speaker_2: Mm yeah

speaker_1: So if its MNIST data you have 10 classes represent that as a 10 dimensional like binary vector with one zeros right So whenever you get from the class one then you get you give like one like one zero zero zero concatenate that Otherwise youll get zero one zero zero zero concatenate that and so on


Does it make sense

speaker_2: Got it yeah


So one question So when we are okay suppose this is something like word embedding could also have been some clip embedding or some such text

speaker_1: Yeah

speaker_2: Im a bit clear but my question is how do we con how do we join this X

speaker_1: Concatenate concatenate make them like vectors Just concatenate that with x and then give it as an input

speaker_2: Okay Im sorry that was the same which thank you so much

speaker_1: So for the discriminator youre saying now how do we concatenate that with X yeah just concatenate that yeah just concatenate

speaker_2: Its just concatenate that yeah just concatenate

speaker_1: Oh

speaker_2: Oh okay

speaker_1: no attention see y is a vector why do you have attention or anything see y is a vector given a text it is a vector that corresponds to a text take that and concatenate with your x thats all what is the difficulty


See its a vector right given a text you get a vector all these words will give you a vector for its sentence isnt it

speaker_2: Yes

speaker_1: So did that

speaker_2: Oh


But yeah but it comes from a completely different vector space

speaker_1: How does it matter how does it matter I just want pairs of images and vectors for my training so look at this now what I am given is pairs of images and vectors

speaker_2: No no no just like


So your screen is not visible

speaker_1: Fastest you can do it


Okay so basically I have pairs of images and vectors right And those vectors can be anything They can come from like some embedding or it can be a one hot vector for class labels It can be anything


Okay so she

speaker_2: So when we concatenate do we have the same dimension size for text embedding and the image in

speaker_1: not no definitely not see then how would you see concatenation can be done in many ways no see you add you add one more channel for your image right and just repeat all this so many times

speaker_2: Oh okay this is just a discriminator network we are not generating anything here so maybe concatenation is sufficient to do that

speaker_1: We are not generating y we are not generating embeddings we are just using embeddings to generate from x conditionally Given a text or given a one hot vector we need we want to generate from it We are not generating embeddings here There is no attention potential nothing I mean its simply taking a vector corresponding to a text You dont even have to do word Okay sorry Maybe I wrote this and you got confused See embedding can come from anything No lets say that it is simply a


TDF IDF okay


you understood right i mean it is some vector corresponding to this vector this thing is concatenate that you have a pair of data or image and a vector you concatenate that vector with this and then try this again nothing complicated at all

speaker_2: Okay


But so what is the difference between the CGAN and normal GANs that we use

speaker_1: Nothing The GAN cannot do conditional generation Conditional GAN can do conditional generation See in a normal GAN right suppose you build a normal GAN on MNIST You cant control what digit you generate when you do inference Here you can control what digit you generate during inference


Is it Is it all right

speaker_2: Yeah yeah thanks

speaker_1: In fact in the data set that I have given you there are some 90 classes different animal faces okay So now Ive asked you to build a CNN on say 20 class theres some 10 or 20 subclass of this data set So what you will see is that when you give that particular the way you should do it to take those 10 classes represent them as 100 vectors like this 0 0 0 1 wherever the class is concatenate this with the z vector okay


and give that as an input to your generator and also the discriminator during inference when you concatenate this is like a switch so whatever class you want you take that particular class and it will generate and do you understand that

speaker_2: Yes it is the headache of the back propagation to find out what in how in which ways these vectors have to be combined and the image has to be generated

speaker_1: Yeah see dont say it that way See the thing is remember what we are doing We are trying to minimize the distributional divergence See if we do it well then the divergence between P of P cap given Y and P of P cap given Y will be minimized no What do you mean by that I mean that is why I spent two full classes on trying to make you appreciate what does it mean to minimize distributions

speaker_2: The reason why we concatenate is what I was talking about so the the the if we concatenate also or maybe if we do something some complicated thing like some cross attention or some such neural

speaker_1: I didnt mean to say that


Just add if you want you i if you want you can add no problem

speaker_2: Yeah okay so okay

speaker_1: You can combine them any way you want any way you want

speaker_2: Okay okay

speaker_1: Okay help me move on

speaker_2: Yes sir

speaker_1: So well go to like yeah one of the application of this the next thing that we will do is uh


So we already saw that we can do conditional generation And one other advantage of doing conditional generation is that suppose you are solving a classification problem and you have less data What you can do is you can build a GAN a conditional GAN and generate class specific data using conditional GANs and use that for augmenting your classifiers


Understand


If you can do a class conditional generation then you can use that to like augment your classifier for your downstream task Does that make sense

speaker_4: Sir please repeat again

speaker_1: See suppose you have a classifier okay and you want to try in a classifier and you dont have data from one of the classes What you do is you build a GAN on that on that data okay the conditional GAN and generate more data from that conditional GAN So if you do it in an unconditional way what happens is you will not know what the label of the generated data is If you build a conditional GAN you already know what label the data is coming from right And you can use the


to augment your classifier and retrain your classifier with more data

speaker_4: Yeah correct sir correct

speaker_1: Aditya

speaker_2: so the second half of the can anyway can so wouldnt it like my doubt was the data set the amount of information we have in the images we are just uh creating instances of that right so the classifier should be able to learn the same amount from the

speaker_1: No no no you will generate new data right its like augmenting your data suppose you have more data in your data set you classifier would anyway become better


I mean again this is under the assumption that you have trained your GAN well so that the underlying distribution is correctly estimated If its not estimated then what youre saying is true I mean the classifier will only see some noise But if the underlying distribution has been correctly estimated via GAN training good GAN training not only GAN you can use it for any kind of classifier any kind of generative model right Take a generative model train it well and you can use that data Of course you need to do it in a conditional way


data augment your classifier again always do that

speaker_2: Okay so my my my doubt was if we had sufficient images in order to actually


uh i mean generate the actual distribution required of that images then wouldnt that be sufficient to directly give a good classifier because we have enough to even estimate

speaker_1: No not necessarily not necessarily But I mean your question is valid What youre saying is if we can anyway estimate the end to end distribution would classifier would anyway do that No not necessarily Sometimes what youre saying is true in a sense But sometimes you know what happens is you know lets say that your classifier is restrictive in the sense that you cant make your classifier large enough right In that case even if you have a lot of data because of restrictions on the architecture of the classifier unless you have like diverse


more diverse data you cant train the classifier well

speaker_4: Okay okay

speaker_1: So in those cases you can or the other thing now other thing that you can do is lets say that you have class imbalance right then to sample from the tail of the distribution you can use conditional GANs and then augment your classifier

speaker_2: Understood okay

speaker_1: Thats a good question by the way yeah

speaker_2: Hi sir so the original data must have a must have some data from a class right the generator

speaker_1: Of course of course of course of course Otherwise you cant do a condition with generation right Yeah It should have some data from all classes yeah Or rather the class that you would want to sample from


Okay so lets move on So Ill talk about two applications of GANs and then we will like move to the next topic in the next class The first thing that I want to talk about is what is called as image to image translation Okay


Image to image translation Okay what is the thing here is the objective here is lets say that we have two data sets


X one through X n given by lets say P X


Uh and theres the why is not


What do we call it


Set is also taken okay let me change the notation


Yes one yes two


is send some data that is coming from some distribution peers and you have like


T1 T2 TN that is coming from ET


Okay so the objective is that


Just a second


Show some examples so that you appreciate it better just opening that paper just a second


Now the objective


to okay translate


you what that means translate from translate from


PS to PT


Okay what does that mean Simply show you an example in development standard easily


Have you seen my screen


this is what it is right so i suppose i want to do a style transfer meaning that i have some style image and i want to convert it to some other style and i mean this is another example right if i have zebra images i want to convert them into horses if i have this you know these are different styles you know photograph to monet to vancouver paintings etc they have winter images you want to convert into summer there are more examples you have lets say that you have sketches you want to convert that into the full images


other examples that are given yeah this is like you have uh uh you have maps or rather satellite images you want to convert it into map and and yeah and the other way around you have the segmentation maps you want to convert that into full images and so on okay so this is what i mean by translation so basically in my notation you have been given data from two different distributions ps and pt the objective is to convert from one distribution to the other


Uh did you understand the objective is it clear

speaker_4: Yes thats good

speaker_1: Okay now how do we do that is that so recall


recall that again right so what does it do it will it will take an arbitrary random variable and project it to random variable of interest so this is arbitrary right


This is data of interest


So there is no other no reason why easy to be arbitrary right So what you can do is you can build a


Gang bang


to take data from the source distribution so s coming from ps and now this converts it into the t coming from pt so lets call that t cap coming from pt cap okay now have a distribution so what you are trying to do is you are trying to start from the the source distribution okay and generate it on the distribution does it make sense you can do that right so basically you can start from any


the variable and go to any random variable as long as so this f divergence okay that you minimize the divergence between the true target distribution and the generated target distribution why are this GANs this you can do of course there will be a discriminator here right because its a GAN that we are talking about it is a discriminator okay


that will take the generated image the cap or the real image from the target distribution T and gives you a number between 0 and 1 Now but this will so this entire thing right this thing will


We convert


PS right to PD Okay So here right what is this doing This is


The mark


P Z two


PX Similar way this is converting PS to PT Do you understand this

speaker_2: Yes so in that case uh G theta of S will look like a autoencoder right

speaker_1: No no no bear is auto encoder here

speaker_2: I mean

speaker_1: simply there is nothing there is no no no no no no there is no auto inputting nothing is happening its simply a gam instead of taking z it will take a s as input and it will give you t cap as output thats all

speaker_2: Theyre video


Okay

speaker_1: Why is there an auto encoder here

speaker_2: Uh so will there be a need to have a equal sized image uh I mean so initially we sampled z and we got g theta of z

speaker_1: Thats a different question Thats a different question So what should be the architecture of this Architecturally changes of course you start with an equal sized input yeah

speaker_2: Thats the key feature

speaker_1: But there is no auto encoding only the size of this network changes that I agree

speaker_2: You can okay


Yes

speaker_1: Uh yeah any other questions on this

speaker_2: And sir one more thing sir how we can identify or calculate the performance of this gains like how per it

speaker_4: are performing well on the data

speaker_1: this question does not fit into what we are discussing right now it is a good question but it is not im talking about this image to image translation right like ive not talked about evaluating games yet so i request all of you to like ask questions that are relevant to what is being discussed right now okay but ill answer that question how do we evaluate i actually hinted that in the previous session i told you that there are metrics called fid etc uh which i will describe but yeah any


question that is like relevant to what we are discussing right now please raise your hands before asking questions please yeah Harish

speaker_2: So while sampling this distribution uh the samples from BS uh from the distribution S here so we really dont know the distribution right underlying distribution in this case

speaker_1: We dont know its just like Z yeah we dont know we neither know PS nor we know PD we just have samples no matter


So what can we do with that

speaker_4: So how do we convert that to like for example that in the general one the Z is of the form of like 16 or 32 that I already told

speaker_1: I already told you right you start with a its a its a CNN so its basically a CNN right of the same size if you want I can write it this way


Its of the same size


Its okay the input and the output I mean the intermediate layers can be anything but you can actually make it a unit if you want to get them just like that


Its an architectural choice what you can do is start from PS okay and reduce the dimensionality and just increase the dimensionality again


I want to then get your P this is from PS this is your J theta of S


Its its an architectural choice you can do it anyway so you can reduce the dimension and increase the dimension again to get to t and the t and s has same dimensions is that correct


Okay thats so cool

speaker_4: to the discriminator you have T cap or T it should be and if there any specific reason youre inviting all

speaker_1: I I mean like by r I mean see when you are looking at the first term you need to give t when youre looking at the second term you need to give t t cap

speaker_4: Okay

speaker_1: Right that is how we have been doing that no discriminators either it T cap goes as input or T goes as input depending upon what term you are evaluating


Yeah service

speaker_4: Yes sir for this image to image translation so shouldnt there be a need of a mapping from which S is mapped to which T or like good question

speaker_1: Good question Good question Good question Yeah See there was a paper called picks to picks that actually paired I mean this is called pairing So now how do you I mean the question that you are asking basically is that how do you ensure that one corresponding S goes to that same T right I mean the example that I showed how does the semantic semantics preserve get preserved Thats a very good question That is why you know in the in the first paper called picks to picks


Okay its called picts to pics here there was pairing


So pairing was there and pairing was an issue because when you get the data you would do you wouldnt get pairing There is another paper that came which was called cycle bound where there was no pairing Okay what they do is


They do this trick called what they do now if you want to convert from S to T okay so they have a gun okay


From S to T


Then they also have another gam from T2S


Now what they do is in addition to


in addition to two GAN losses


Cycle Vian also has

speaker_2: Stain loss

speaker_1: No no no as what is called as a cycle consistency loss


Cycle consistency loss Now what do you mean by cycle consistency loss What they do is so for GAN from S to T so you have this no You have expectation of log of DS that you get is from T and you have T coming from PD plus that expectation of log of


1 minus TS T cap T cap coming from that generator no PT cap theta okay in addition to this they will have another loss okay that would say that


Yeah


If you take the


Actually yeah so there is another


here right which is similar to this expectation of log of dt on s


S coming from PS so they do are the other direction they develop translation in other direction also they have this and S cap coming from PS cap lets call this P right so what they do is theyll say that if I take I will write that so there are two generators here so generator one is taking S and giving T lets call this G1 there is another generator


Of course there are two discriminators also this is taking T


and it is giving you yes now what they say is that if i take an image okay uh that has been


generated okay if I take g1 okay and pass it t


it sorry given takes S no if I take an S and pass through it


What should I get


Ill get an image in T correct Now I will take this image T and pass it through G2


What should I get

speaker_2: Say against the same measure

speaker_1: Against the same image

speaker_2: Thats brilliant

speaker_1: Right I get I get S right I should get S so I minimize this loss


is called cycle consistency law similarly they do this they take g1 okay and g2 pass it pass through a t you will get an s you pass it through t you will get another t to take that corresponding t and okay it is this so this is what is the cycle again


So I claim that if you do this in addition to try to do the variance then the pairing will happen Let me just show you that


Is my screen visible


Yeah you see that right There are three objectives here right One is the two GAN objectives of course and theres the cycle consistency objective What is cycle consistency objective here So they call this T and S as X and Y by the way So and two generators as G and M So when X goes through G you get an image from Y and then you have to go make it pass through the other generator and match that with X1 X the input image And you do this for the other generator and add that as another


So this is what they get no input output of the generator and the reconstruction that is happening So we have to ensure that this also happens And they show that if you do this then the I mean you can use this for image to image translation


Okay so thats it for today then let me


Share that


See as I said no there are so many applications that GANs are being used for And I know I can teach a full course on GAN But yeah so you dont have that time unfortunately Yeah questions are coming

speaker_2: Uh so Im sorry but I did not understand the pairing uh that uh

speaker_1: There is no

speaker_2: This is not the question that was asked

speaker_1: There is no pairing See the question was while doing this do you need the corresponding S and V See in the example that I showed if you take a sketch and you want the corresponding field image while training the scan do you need the pairing This is the question

speaker_2: We we should right we need

speaker_1: Anyhow


No we dont That is what Im saying In pixel to pixel paper pairing was needed But in cycle GAN pairing was taken I mean they gave up pairing They said pairing is not needed Then how do you ensure that the corresponding image gets generated is through having these two different generators Even though you want S to be converted to T you also have another GAN that is T from S and then you have the cycle consistency

speaker_2: And then you have the cycle of the testicle convert it back and then the difference between them should be minimal okay yes oh okay okay

speaker_1: Okay okay uh centered


Minister

speaker_2: Translate from English

speaker_1: Whats your question or just clarifying is it


Or third

speaker_2: The other GAN was just for you know learning of the first one

speaker_1: Uh you can say it that way right it is aiding the running of first one but it also gives you one additional advantage that you can have conversion back also no T2S as well


Yeah such a thing

speaker_2: So when pairing is given its more like conditional GAN

speaker_1: Ah it becomes like a conditional yeah thats a good observation yes it becomes very conditional yeah correct

speaker_2: Im sorry

speaker_1: Thats a good observation instead of having uh


like a text as a one hot vector or as a conditioning variable you have this image as a conditional variable thats a good observation yes in fact you can see this right you can use GAN for inpainting now image inpainting because you can use the input image or the or the like mask image as input and you can train again to complete the image so you can imagine any any of the applications now because what is GAN doing at the end of the day that is why you need to have that abstraction thats taking starting from


arbitrary distribution it converts it into distribution of interest and it does that via minimizing the f dimensions now you take your input to be anything that you want and output to be anything that you want and imagine whatever application you want there right

speaker_2: So sir in basically these mobile phones and everything we see many photo editing tools which convert the image or enhances the image

speaker_1: Yeah they can be GANs They can be GANs but right now the state of the art is not GAN They use diffusion models charge generating models but the fundamental idea is the same

speaker_2: Theyre asking us

speaker_1: They use diffusion models because they are more easy to train and robust We will come to diffusion models later in this course okay


Okay yeah Ill go

speaker_4: Uh so uh


Will it will be uh converted

speaker_1: What do you mean by quotient and what do you mean by that

speaker_4: Okay so when you say that we can we find a loss function by passing it to g g1 s minus s right and that

speaker_1: will not loss function yeah g1 of s is simply an image


G2 of G2 of G1 of H is another image Were just looking at the differences of the images See G1 is a generator no

speaker_4: Youre welcome


Ha generator so the image is same which is passed like S is same and whatever we are getting

speaker_1: whatever we are getting hold on hold on hold on please hold on yeah ill tell you what is happening take an image s pass it through g1 you get another image t right

speaker_4: Output

speaker_1: If you take that T and pass it through G2 you will get some other images


See that email maybe I should uh

speaker_2: Okay thats not though it is

speaker_4: The state the state

speaker_1: Why is it the original image Why is it the original image It is output of the generator it is something you you are matching that to the original image

speaker_4: Okay thats what I was confused I thought you were telling like we are reversing the process and finding out the loss function

speaker_2: after that

speaker_1: Its impossible no you understood what Im saying right so its yeah

speaker_4: Sorry about that

speaker_1: Okay so its a different image its not the because the it is the generator right we have actually there will be another descrip one discriminator here

speaker_2: Yeah yeah

speaker_1: EWS will be another discriminator here


Is it T W T Yes go on okay

speaker_2: Ah sir when we are talking about the differences between the these two images

speaker_4: like G2T and G10

speaker_1: Pixel level differences pixel level differences

speaker_4: Oh its a pixel level yes okay great thank you sir

speaker_1: Yeah

speaker_2: Okay


So one question so from this we can see that any arbitrary distribution can be converted by by training to one more other distribution right to make it closer to the one

speaker_1: So

speaker_2: Is there are there any cases where we cannot do that For example there are two distributions which we cannot train again to for them to convert to one more distribution

speaker_1: Theoretically no you can convert anything to anything theoretically


Yeah practically what happens is if you do not have like strong priors on data for instance if you have lets say data like tabular data or data like you know where you have compositional data and all that now its difficult to train GAN But theoretically speaking you can do it Anything is possible

speaker_2: Thank you

speaker_1: Okay I think all these questions are


Yeah its okay Im not disgracing that but yes the time is 12 10 now


See there is one other thing that I wanted to do which is like domain


What does it mean


Its um


Way to solve domain solving problem of domain adaptation


via GAMS so I wanted to do that itll take 15 minutes people like complain if I extend shall I do that in the next class okay I wanted to finish this and go to video and online course in the next class but anyway so itll take me 15 minutes Ill do it in the next class time okay


Okay thats all for today So well have the you will have with quiz next next class Uh starting at nine after the quiz we will look at the domain adaptation with GANs and then well move to BAEs Okay


Please see what I recommend you is that now that we have come to the thick of the things please start reading the papers that we have discussed in the class in the original And if I have questions you can either contact me or TS and get your doubts cleared Okay See you then See if I like you know while asking questions you know Im just trying to moderate it a little so that there is relevance So dont get me wrong So yeah questions


are always encouraged okay Ill see you next week

speaker_4: Yeah tha thank you sir thank you sir

speaker_2: Thank you sir

speaker_4: Thank you sir

speaker_2: Kind of

speaker_4: And just so

speaker_1: Thank you so much


T right correct take that T and pass it through G2 you will get some other images


See that TMA or maybe I should uh


Why is it the original image Why is it the original image It is output of the generator It is something you you are matching that to the original image Yeah

speaker_3: Oh my god

speaker_1: thing its very possible no you understood what im saying right so its yeah its more okay so its a different image its not the because it is the generator right well have actually there will be another one discriminator here

speaker_2: Yeah yeah

speaker_1: EWS will be another discriminator here


Is it DWT Yes go on okay

speaker_2: Ah sir when we are talking about the differences between the these two images like G2T and G16

speaker_1: Pixel level differences pixel level differences

speaker_4: Oh its a pixel level yes okay great thank you sir

speaker_1: Yeah I got it

speaker_2: Im not


one question so from this we can see that any arbitrary distribution can be converted by by training to one more other distribution right to make it closer to the other one

speaker_4: I dont know

speaker_2: Is there are there any cases where we cannot do that For example there are two distributions which we cannot train again to for them to convert to one more distribution

speaker_1: Theoretically no you can convert anything to anything theoretically


Yeah practically what happens is if you do not have like strong priors on data for instance if you have lets say data like tabular data or data like you know where you have compositional data and all that now its difficult to train GAN But theoretically speaking you can do it Anything is possible


Okay I think all these questions are


Its okay Im not discouraging that but yes the time is well 10 now


See there is one other thing that I wanted to do which is like domain


Adverse serial networks


Just um


to solve domain solve the problem of domain adaptation


Why are the ants


So I wanted to do that Itll take 15 minutes People like complain if I extend Shall I do that in the next class Okay I wanted to finish this and go to the additional module and codes in the next class But anyway so itll take me 15 minutes Ill do it in the next class time Okay


Okay thats all for today so well have the youll have a quiz next next class

speaker_4: I think so

speaker_1: Uh starting at nine after the quiz we will look at the domain adaptation with grams and then well move to VAEs Okay


Please see what I recommend you is that now that we have come to the thick of the things please start reading the papers that we have discussed in the class in the original And if I have questions you can either contact me or TS and get your doubts cleared Okay


you then see if i like you know uh while asking questions you know im just trying to moderate it a little so that there is relevance so dont get me wrong so yeah questions are always encouraged okay ill see you next week

speaker_4: Yeah tha thank you sir

speaker_2: Thank you

speaker_4: Thank you sir

speaker_1: Mm hmm

speaker_4: So its a

speaker_1: Thank you
