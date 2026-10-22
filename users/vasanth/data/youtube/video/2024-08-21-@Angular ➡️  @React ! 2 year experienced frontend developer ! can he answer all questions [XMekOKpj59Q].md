---
id: XMekOKpj59Q
title: "@Angular \u27A1\uFE0F  @React ! 2 year experienced frontend developer ! can\
  \ he answer all questions ? ?"
url: https://www.youtube.com/watch?v=XMekOKpj59Q
date: '2024-08-21'
duration: 00:24:17
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 3
speakers:
  speaker_1: null
  speaker_2: null
  speaker_3: null
---


# @Angular ➡️  @React ! 2 year experienced frontend developer ! can he answer all questions ? ?


## Transcript

speaker_1: Hello all welcome back to Kairi with Vasant YouTube channel My name is Vasant I hope youre all doing well So I assume this is a video series where were discussing about the mock interview In this particular video with me I have Vishal Vishal is a two year experience front end developer He having experience of Angular and relatively hes

speaker_2: trying to transition into React So its going to be a good interview if you are also from the similar background Youre from some other tech youre trying to transition into React So what are the challenges that you would face Im going to discuss those also with Vishal More about Vishal Lenny hell be explaining And this is going to be a combination of basics of JavaScript machine coding and a Reactjs Some basics of Reactjs So please watch the video till the end For some reason if Vishal is not able to answer right answer give right answer to a question that I asked Im going to give right answer to the end So please watch the video till the end


We shall see if you can introduce yourself we can get started

speaker_3: Sure Asantah Hey Asantah good afternoon I am Visha I am a fintech engineer I am working as a fintech engineer for the last two years So in a startup Yeah thats it about me

speaker_2: Sure sure Michelle shall we start the interview now Michelle

speaker_3: Yes before that I have a doubt Yeah Because I have been interested in a project called like its used for a video call recording I am facing some problems in that regarding group chat building and reducing the screen size like styling for different screen sizes and many more problems as well Go ahead How will you can you give me a condition for that

speaker_1: Im not even a function button

speaker_2: Good that you brought this question up See video calling is one of the complex feature to build Though like chat like Zoom and Google Meet looks very simple but its not very easy to build if you are given that such project Okay Lately Ive been using a tool called Zego Cloud Ive told about this product in the past as well Where Zego Cloud is a tool which where you can build the entire video calling just with help of this particular product So they have a thing called UI kits where the one of the primary challenge is to build the product end to end So we have to go and


which protocol to use how to handle cross browser support how to handle group chat how to handle one on one chat all of those things actually taken care by the ziggeo cloud as you see its also its not just about the video calling they have audio calling they have any other multimedia sort of calling involved all the features are available as a part of the ziggeo cloud and the question like you asked how do we handle the dynamic layers how do we handle the beautification of the face how how do we handle like into messages whenever youre on call if you have to send some messages how do we handle that all of the things are actually given out


the box by the ui kit of the zego cloud and they also have something called like 10 000 free seconds lets say you are a new user you just sign up for their particular portal youre gonna get 10 000 free seconds which you can use for free only after that if youre like very satisfied with the tool you can continue to use their product okay so its a very good product not just you i recommend it for anybody who is having a video calling requirement they can use it okay hope that clarifies your doubt we shall okay


Sure now let us start with a very interesting question Vishal Okay this I have recently Ive asked this question multiple times in the interview Im presenting a whiteboard Okay lets say we have to build a tool similar to Google Calendar Sorry Google Calculator Okay Im drawing on the screen Okay like for example a typical example how a Google Calculator would look like The Google Calculator means whenever you type something like 2 plus 2 on the Google search and you would enter right


will be prompted with a calculator


So theres a simplicity say Im quickly drawing few things okay

speaker_3: Oh

speaker_2: I think this is the area where usually the user would type something For example you type one plus two here and you click on is equal to you will get the answer correct Or you can use like one plus you can click on this button and youre gonna get the output So now my question is lets see how to build a feature like this in the browser Vishal Okay the UI that I have already built building UI is not a great challenge Now after building the UI you have to basically process the equation and to give answers right Lets start from there How is that youre gonna solve the problem Lets say one plus two star three is there


One plus two R three you have to process this equation to give the results right what all things comes to your mind as a part of building this please tell me

speaker_3: okay we can use the reusable functions like we can create functions with for addition one and for multiplication one and for division one okay what youll do is you will return uh when uh like user clicks on equal to but will store value in some variable local variable what youll do is you will first uh get the inputs from it so while user the click while user clicks on plus we will in the back end what well do is we will just add the function name and the argument as two so one


plus one and that argument I mean sorry one comma that argument and then after that uh next uh next thing will come like uh with this value and a multiplication with three that multiply function we will call it

speaker_2: So so we shall tell me one thing is it this you are gonna do in the back end or all the things of this processing happens only on the front end or client side

speaker_3: Client side Im going to do okay

speaker_2: Okay complete processing happens on the client side correct no no back

speaker_3: No simple thing okay we dont need to do like back anything for this

speaker_2: So now as you told we have 1 plus 2 star 3 correct So you have to process the equation Will you start processing after user hits is equal to or before that

speaker_3: After user clicks equal to

speaker_2: Okay after user clicks on is equal to you have a 1 plus 2 star 3 which is typically in a string format


its in a string its not we cannot put it a number because we have the expression plus and stuff so its in a string format so copying that entire string one plus two star three okay and you are basically processing that correct so you told like youre going to create multiple methods for plus addition subtraction multiplication so how are you going to process this one plus two star three can you please quickly tell me

speaker_3: we can store those like separate characters like the plus and multiplication and division in a separate string and well check if this the current element of the string is like present in that chart

speaker_2: No no not that Like for example like I have given you one plus two star three and you have a function like calculate

speaker_3: No no not that

speaker_2: What are the first thing that you are going to do Can you please tell me

speaker_3: And the user clicks equal to right

speaker_2: Yes so when user click on it you called a function called calculate The calculate function has the expression 1 plus 2 star 3 What is the that first thing that you are going to do in that function Please tell me

speaker_3: Great


Ill run a loop for using that string Okay What I will do is when the first element comes in I will check if that any of the symbol is present in that first element Okay If its not it should be a number because we cant type anything

speaker_2: Incorrect correct

speaker_3: other than number correct so ill just uh pass it and uh ill push it to ill add it to a separate number as a like thing and then ill check the next one next one next one since its uh like uh symbol here even if its an spits another number uh then what youll do is you can introduce a right number followed by another number so it should be like one plus one and one its eleven so what youll do is we will add that number uh like into one into ten and plus that number so it will it becomes


one number plus we will check that symbol so since this is a plus symbol for that plus we will be allocate allocating that one function right so we have that one that one separately thats it this function so we will send that next argument as a next number or symbol like next number should be there because we cant like give two symbols

speaker_1: Links are


Please please please go

speaker_3: Or two


Next we will check that number and then we will check if the continuously if we are getting a number like 22 or something if there is nothing in forward be only symbol we will just pass the value to that number and whatever we getting the value we will return and like add it to that

speaker_2: Sure sure Sounds good Vishal See as I think you did not while introducing you did not say this Basically youre from the mechanical background correct And youre turning to IT because of interest I think the third year in the second year third or fourth semester most of I think most different universities will have this

speaker_3: And youre

speaker_2: Think of evaluating an expression There are different ways to evaluate an expression like infix postfix and different ways How do they evaluate an expression Okay so where this is actually taught Whatever youre telling is correct but there is more formal approach to solve Only one last question I ask regarding this and then probably well go to the other problem So as you have to build like as you are doing this in Google Calendar or anywhere you might have Google Calculator or any other things you might have seen there is an undo and redo operation correct So you have a star three I mentioned like one plus two


So then I enter like star and three Now if I do control plus Z right So the star three vanished correct I did control shift Z star three appeared again Getting my point right


and start to reappear again okay if you have the feature the undo and redo operation okay which data structure you will use which are just that is my question which data structure you will use and why

speaker_3: Its okay


or unknown credo okay Ill use um


Most probably object data structure

speaker_2: So why and anything you can look into basically any data structure but the question will be why why you are using that particular data structure

speaker_3: object or array we can use both we can store those uh like every single options like


symbol and number as a separate element and when user click control z you will just remove and usually we will catch it in a different variable because you if the user just like want to undo it so we can push it back to the array

speaker_2: Got it Got it Its its not a wrong answer but for audience who are watching the right answer is stack actually Okay The stack is where youre going to keep pushing the operations Like for example one you entered first value is one Then you enter into one plus is the next entry Then one plus two is the next entry One plus two star three is the next expression Okay You do control Z youre going to pop the top value and whatever is the top at that point in time that we are going to show on the ui same thing we are going to keep doing redo is also very simple whatever you remove from the uh


the undo stack youre gonna put it in the redo stack once you whenever you redo whatever the top of the redo youre gonna pick and put it on the stack of the undo operation so youre gonna use two stacks one to perform undo one to perform the redo okay stop sharing this Vishal okay can you please open code sandbox and uh like search for like react js code sandbox react the question Vishal is very simple okay the question is should be you have to implement a password strength checker okay where uh you will


uh you will have a function okay lets break it into two things first thing is that you have an input text box whatever user enters in the input text box thats going to be passed into our function correct and within that function you need to check whether that password is whatever the password strength you need to render that password strength on the ui like whether its weak whether it is mean like weak medium and strong three things you need to represent okay let me tell you the conditions like if the password or else we can make it even more simplified


the audience are should not get confused if a password has a capital case a smaller case and a number its a strong password getting my point audience also im saying again if a password has a small case capital case and a number then it is a strong password you write a function which accepts a password and retells whether that particular password is strong or not so we are not taking weak strong and all we are just only checking whether a password is strong or not okay if it has only a


small character and alpha uh capital character it should uh it should tell its not a strong password only when theres a small character capital character and a number then it should tell like its a strong password first implement that function okay and you could just log it log the output once after you completely successfully implement that then we will try to integrate that into an input box you just have around 10 to 12 minutes to implement this okay please go ahead and start

speaker_3: Start function

speaker_2: audience who are watching as i in the beginning i told we shall just starting with react he has come till an extent of hooks and some moment of react he has not like mastered it but still he is trying to transition his career with react and want to learn react so thats the reason he is giving the chance of reading the values i mean uh or giving a shot at uh solving the machine coding question react i appreciate that yeah please get continue we shall

speaker_3: So for this I think the solution I will be thinking of like checking the character code for this


character code is like for capital letters there will be a range of character code and for numbers there will be a range of character code and for small characters there will be a range of character code correct I am not aware of the syntax as of now can I use Google for searching

speaker_2: Yeah please you can sort that yeah okay that you can hold and drag down like

speaker_3: No

speaker_2: you can expand it yeah that widget you hold and drag somewhere in the screen like just drag it down youre able to do right


No continue yes

speaker_1: Just the advice to you and everyone who is watching the video anytime you want you do want some syntax to be known right you dont know and you want to search

speaker_2: And this stuff


Anytime you want you do want some syntax to be known right you dont know and you want

speaker_1: So always as the interviewer like Vishal did

speaker_2: So always as the interviewer like Vishal did

speaker_1: Most interview will be fine if you for you to search the syntax

speaker_2: most interview will be fine if you for you to search the syntax but dont take consider like explicit and search immediately because some companies do have a rules where if you search something from the outside they would have a strict rules of like rejecting the candidate so dont give that chance you be explicit and ask so that if interview okay you search okay i think line number seven it should be const it should the spelling mistake i assume michelle


plan to handle the numbers whether the number is present in a string or not

speaker_3: And this one code zero and code eight


The number is starting from zero so we are checking till nine so till eight

speaker_2: or watching the video you guys can also like practice this in parallel like you can write a code and you can put your code in the comment section or you can create a gist and paste the gist link of gist also in the comment section i will definitely be more than happy to verify it and tell whether thats the right answer or not

speaker_3: Thats true

speaker_2: You continue with that yeah


You can remove that E for a while like you can just directly read the value in line number five

speaker_3: Line number five okay

speaker_2: Lets consider that as an argument youre directly passing the string


Okay

speaker_3: Okay

speaker_2: Yeah yeah

speaker_3: Still we need to get that argument right

speaker_2: Yeah yeah you should have E yeah thats itself the value yeah youre not basically extracting anything yeah

speaker_3: Also check out


with some string what youll do let me finish this first


Ill give some random Ill give one capital letter one


One small letter and one number

speaker_2: Sure

speaker_3: instruction


A control how to view the console here

speaker_2: You see console in the bottom right console 14

speaker_3: Okay


Great

speaker_2: It will be weak

speaker_3: Um it should be strong when is it coming as week

speaker_2: only one more one to two more minutes we have to go to other sections as well see if you can


Given a different argument and see like for example can give all small letters and see what is happening

speaker_3: Uh we need to save it for later

speaker_2: Yeah yeah some should re render but yeah you can deflections all small also coming as weak


If you wish to like log whatever is in line number 11 the code can try logging to get some idea

speaker_3: Its a little dot clock


Yeah I think it will come as

speaker_2: is coming as one one five


Because youre youre passing SSS


I think Patrice will be there too

speaker_3: Very positive

speaker_2: to try pass different string in line number uh instead of yes yes you pass something else and see whether youre getting different values or not then not the same like different characters like one small one capital one number

speaker_3: Okay I want to see one


Six seven ninety nine yes

speaker_2: Whats a number two whats a number

speaker_1: Thats for the question

speaker_2: Okay

speaker_3: Yeah four is different

speaker_2: So that is a problem correct maybe after the interview you can check this Vinod Shvishal okay

speaker_3: Okay

speaker_2: Now lets let me ask you some questions about about the react can you go to the same snippet again Hold left yeah so we have a use effect in line number 50 25

speaker_3: Mm

speaker_2: The end of the day is what its a function

speaker_3: Last couple of functions

speaker_2: Yeah have we ever given a thought what does useEffect return as its a function to return something correct what does it return

speaker_3: function I dont think useEffect returns something as so as per I as of my knowledge

speaker_2: So then its like something like undefined or null

speaker_3: Uh it will be undefended

speaker_2: Okay tell me the difference between undefined and null

speaker_3: Undefined is like its no its no value because if we like declare a declare a variable and we dont give any value the value will be like undefined by default null we can set like an initial value for like not giving it empty

speaker_2: So you are saying null is something of value to represent nothing correct Undefined is when you have not defined anything Thats the difference Vishal


So let me share a snippet with you Okay copy the snippet Ill put it in the chat section Copy the snippet And I mean you can replace your code with this code Okay I dont have to run the run it Just copy paste And so that first I want you to go to the code and guess the output basically Okay if audience answer if you wish you can pause the video for a while go to the code If you know the answer you can mention question number two and your answer in the comment section Okay

speaker_1: audience

speaker_3: I dont think uh you need


The zero will be count because this is an async thing and it wont before that we have a synchronous like section here and in this synchronous section we are clearing that thing

speaker_2: Okay as you told like youre just starting with React Ill give you some context In line number eight whatever the return that we are doing right that would execute on the component unmounted Like for example youre on page A youre going to page B Whenever the transition happened right that return will be executed So its not gonna execute as long as when you are in screen A okay So Im giving you that hint Now if you wish to like re guess your answer you can tell me

speaker_3: The third turn is not going to run before we are changing to our next

speaker_2: So you can assume that throughout the execution of this file its not gonna be called basically Okay

speaker_3: Okay then uh


randomly it will for for thousand sec thousand milliseconds randomly it will change to one and minus one based on the returned value okay previous code okay okay not not ps hybrid sequence ps count we are adding it so randomly it will add to zero like one and minus one randomly

speaker_2: Correct What are you saying is correct Vishal So basically its hard to predict what does the output but output will be keep changing basically correct Yes Because the value of count is zero initially and we would come inside the set interval

speaker_3: Yes

speaker_2: Every time

speaker_3: Do you mind if I

speaker_2: the previous count value you have youre adding the previous count plus whatever the random value that is generated correct if it is greater than 0 point 5 youre going to add 1 otherwise youre going to subtract 1 but there is a catch


Theres a catch here

speaker_3: Theres a catch you

speaker_2: see lets say the initially the count was zero you set it as like zero plus lets say lets assume it was greater than one greater than so zero plus one so it became one


So where the value of count became one So next time what will be the value of count Its gonna be one or zero

speaker_3: It will be one it will be available in this previous count uh callback because yeah theyre using as callback right

speaker_2: Correct correct correct Vishal So thats the right answer Im done from my end Vishal We are reaching the last four minutes of the interview You can stop sharing


Let me give my feedback to you and audience whoever has watched the video so far Okay Im hoping you enjoyed it so far And if you enjoyed please like and comment whatever you felt honestly And if you solved the problem like whatever Vishal did maybe before to Vishal that also you can mention Mostly Vishal has given approximately right answers to all The password checker that could have been improved a bit but that answer solution you can get somewhere online as well So Im not gonna explain anything that Vishal has given or all thats it Now my feedback to you Vishal Ive noted on a couple of feedbacks Lets start with them


machine coding thing this is to you and everyone almost 90 percent of people that I take machine coding problem I ask machine coding problem do the mistake where the approach is not finalized in their mind itself youre getting my point right see whenever youre solving this is applies to machine coding also whenever youre doing your day to day coding so first you be firm like your mind is the first computer then it is actually whatever youre typing correct the Im not saying like 100 percent will be able to do but largely first have a solid approach in your mind


then you start implementing okay and with that you will be able to solve the problem quickly the coding can happen in two minutes you might end up spending like around remaining eight minutes about thinking towards it so you can do that second it every when it happens some syntax are unknown so we have to search on the online nothing wrong with that also but be clear have a concise list of everything that you want to search like for example four things i dont know four things ill search it cannot shouldnt happen like you do to and fro like you start coding again


like something i dont know again you go and search its not a day to day coding its an interview so try to have that list of things that you want to search and ask the interview these are things that i dont know some interview will be willing to help you only there you dont have even had to search theyll only tell which function will give you that if you dont know and some theyll allow you to search so do it for once and come back and continue the coding okay and other thing uh this scenario driven question that i asked the google calculator right its not a very straightforward question its not a very hard question also the the


suggestion to you and audience who are watching is you are a front end developer dont look at the front end systems like a user look at the front end system like a developer like for example you are watching my video on youtube tomorrow if you have to implement this youll not be able to know 100 how to build it but some degree you should know like what are the things that you are going to use to build this okay look at a system like a developer going forward thats the right way to learn the front end system design where whenever you have a doubt you keep searching and you start consolidating getting more and more information okay


These are the feedback that I feel Vishal I feel like as you still started learning the React and you want to transition to React roles there is definitely some scope where you can master the React I feel like its not like 100 percent you are there yet Spend some more time mastering the React and then you would be good to give the interview Vishal How was the interview experience otherwise Vishal

speaker_3: Yeah it is wonderful

speaker_2: Thank you

speaker_3: Your hands

speaker_2: Wonderful Thank you so much Vishal Im thinking in the audience who have watched the video you also liked the video If you liked the video please like it Subscribe to my channel Carry on See you in the next video Thank you so much
