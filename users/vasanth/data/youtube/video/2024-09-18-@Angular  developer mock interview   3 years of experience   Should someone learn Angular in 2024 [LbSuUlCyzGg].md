---
id: LbSuUlCyzGg
title: '@Angular  developer mock interview | 3 years of experience | Should someone
  learn Angular in 2024 ?'
url: https://www.youtube.com/watch?v=LbSuUlCyzGg
date: '2024-09-18'
duration: 00:25:20
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 4
speakers:
  speaker_1: null
  speaker_2: null
  speaker_3: null
  speaker_4: null
---

speaker_1: Hello all welcome back to Career with Vasant YouTube channel My name is Vasant I hope you all doing well As you know this is a video series where we are doing a lot of mock interview Today with me in the video I have Aditi Aditi is an Angular developer More about Aditi Aditi only will be explaining Like most like most of my mock interview this video will be combination of a lot of things One is basics of JavaScript thats going to be fundamentally there Another is Im starting introducing some basic DSA questions not so hard but something to give you overview about the DSA problems And definitely therell be one machine coding problems where Aditi will be solving


a problem meanwhile if you get time anyway we are going to discuss some basic sub system design as well thats all we are going to do in the video for some reason if aditi is not giving the right answers to some questions im going to answer that at the end so please watch the video till then if aditi does give all all answers all right answer then ill not be making that post video thats all aditi if you if you can introduce yourself we can get started

speaker_2: Yes uh hello all Uh my name is Aditya Khedkar and uh I have three years of experience in Angular and uh I currently work uh both in UI and me in the food stack as Angular and Java

speaker_1: Wonderful wonderful Aditi So Aditi you have three years of experience in front end development using Angular One of the primary question like a lot of people out there has is like Angular is not having so many so many opportunities So everybodys turning towards React As you spent three years there what is your opinion about it

speaker_2: Opinion is actually React based hiring Ive observed theyre mostly for small scale and mid scale companies I still feel Im hopeful about Angular being used in legacy and banking related domain especially Since I belong to the banking domain its time and time revisited that how much Angular is security wise better than India made is framework So its very difficult to compare both of them But as a job market situation I can see definitely React hiring is more

speaker_1: Exactly


Got it You say like real hiring is more but angular opportunities are not less So if youre if youre sticking to something more like a B2B sort of businesses you continue to have opportunities what youre saying at the day correct

speaker_2: Yes yes almost all big companies all big firm companies usually have Angular as a stack

speaker_1: Correct So Aditi now lets discuss a simple problem Okay Can you share your screen Question is very simple Aditi Okay So lets say I give you an array How do you reverse the given array I have any array you can take Like for example const arr I even sent in the chat as well Or you could take any array const arr is equal to 1 2 3 4

speaker_3: Okay can you please

speaker_1: Can you please type it You can type it const ARR


is equals to that RNA notation and one two three four yeah lets say this RNA need to be reverse RT three


tell me the different approaches that comes to your mind im more like want to explore this even for the audience also its not that this question is very hard there are multiple approaches so how a candidate would think that will be the ask from the interviewer always remember when the question looks simple then the expectation is like how well you react with the problem or what are the different possibilities that you can think of same applies to you other three please tell me

speaker_2: Uh okay one thing I can right now think on the top of my head is using reverse function in J and thats uh already predefined another way I can also think is uh using loops correct uh for loop

speaker_1: Yeah if it is a follow up how you are gonna do it

speaker_2: Ill be setting the number of lines first and then start decrementing it periodically And I will also try to use another array So there is array so Ill try to use reverse array and try to push it and then print it

speaker_1: Got it

speaker_2: Got it

speaker_1: So there is uh I could not I cannot call it like a time space complexity but but using this approach where you would use an uh like you iterate from the end basically youre using another array uh correct yes so basically that especially to you and other audience are watching in the interview always ask the output array do they consider the space complexity or not getting my point right so sometimes its like the output need not to be a space complexity thing because that might be something that we are doing here but in a company or whenever we are


doing the actual project we may not consider the doing that because we might just process it we are trying to log here or something like that but in case if they consider that also the space complexity then the space complexity is actually n correct because we are using another array in that case aditi correct lets say you dont have to use an another array in the given array only you need to reverse it can you think of something

speaker_2: Yeah


Im not sure exactly about a technical approach versus but I think snapping can also be considered in such cases like I will uh lets imagine Im trying to iterate through array and then I am uh instead of this time length I will use length by half okay my approach is very similar uh to binary sort just like that where uh what im trying to do is ill declare a variable this time not an array and that variable will try to


uh swap in the runtime whether that is uh now Im not sure how to explain this but the approach is very similar to a binary sort

speaker_1: So binary binary sort or binary search binary search correct

speaker_2: Yeah yeah yeah uh Im Im just trying to reverse through half of the got it yeah what do the approach uh is

speaker_1: Got it

speaker_2: But yes that is one way I can think yes

speaker_1: Sure See binary search works binary search sort of works if it is a sorted correct But as you know the problem statement we did not consider it as a sorted Even if you consider it as sorted correct Even binary search sort of approach you are heading in the right direction but thats not the approach If you wish to take one more minute something in this direction if you want to think you can think I can give you a

speaker_2: To take it


I would like if we go into the next question on Im just out of ideas sorry

speaker_1: Ill give you a hint Aditi Okay So lets see how do you use the hint See all like most of the time whenever such problems we look at it we try always like we have basically fundamentally we have to iterate the array that is unavoidable Correct This cannot be done without the complexity of at least n or n by 2 like we have to iterate the array without that we cannot do Correct And whenever the iteration comes we always think from one point like the origin of the array


How about we take it from multiple points

speaker_2: But to think of it wasnt I also realized there is another way popular way where we use an array two pointer method where one first first pointer is supposedly at one and last pointer is at four and they accordingly we can as we iterate youre right in the end it is a O of n only but since there are two pointers similar swapping logic starts happening

speaker_1: So basically we have two pointers Lets say the first and last the pointers named that way correct The first points to array of zero and the last points to array of n minus one correct And we iterate the array We iterate the array only till the both pointers point to the same value correct But here we have two possibilities If you observe kinglyaditi the even arrays the array with even number of elements behave in a different way Array with odd number of elements will behave in a different way

speaker_3: Im sorry

speaker_2: Well be right back


Thank you

speaker_1: Got my pointer

speaker_2: Very good very good

speaker_1: Okay so those scenarios we need to handle but we have to iterate the array We even do not iterate the array till n We can just complete it in the n by 2 correct Half of the array length close to we could iterate But the complexity point of view time complexity point of view you have to say n by 2 2 and 3 and theyre all always n So the time complexity is n okay uh okay good good that you could come up with this approach so always remember you and the audience the two pointer approach a lot of problems can be solved using this lot of ive seen like google also asking questions around this and many many were able to solve

speaker_3: Okay okay

speaker_1: the help of the two pointer approach which is one of the approach so now


Aditi let us discuss one of the common question that whenever people using Angular React sort of thing and theyre not using the plain HTML and JavaScript is Why should somebody use Angular So there are a lot of advantages but lets stick to the one primary thing of performance correct Do you think Angular works better than a website built using HTML CSS and JavaScript If so how

speaker_2: I for me angular is like an ecosystem wasnt where uh one big advantage I have seen in sort of vanilla HTML CSS is single page application approach Uh react is also similar in that way So uh the overall organization and uh its very systematic That is the developers experience But technically speaking single page applications uh can be built very well and fast with angular The same approach can be done in HTML CSS


the code lines and the logic is too much even the bundling right from route calls everything is uh its like an ecosystem thats why uh i feel like

speaker_1: I agree The ecosystem part I agree Aditi Okay Because unlike even React Angular basically gives you all the folders where the services need to be kept Correct Or where do you basically all the folder structure that a particular project wants Everything comes along with the basic template itself Correct Very organized

speaker_2: Good night

speaker_1: And but the problem is like what is the advantage where it stands except the ecosystem as you know in a basic HTML JavaScript application also maybe you can stop sharing as well in the meantime did we discuss this

speaker_2: Very nice

speaker_3: Financial

speaker_1: the the plain HTML CSS and JavaScript website as well we could make a very structured sort of thing though its not maybe built in like Angular but we can make it happen Correct So thats not core advantage Basically folder structure is not a core advantage Correct Except performance point of view Correct From the performance point of view do you see any advantage Aditi

speaker_2: performance wise uh for example we can implement uh i can also add a security point if thats okay i have seen a security concerns like cross across cross site uh cost issues and uh excesses ones are being handled better in angular as well as a lazy loading concept can be implemented but angular just provides a seamless way so its easy easier i think things are easier when when it comes to framework

speaker_1: See react uses the concept of reconciliation for re rendering the dom okay one of the way where multiple is what does angular uses for re render how angular basically re renders the dom aditi

speaker_3: Yeah


Uh to change detection uh Im not sure

speaker_1: Yeah if it is a change detection you would do you like to explain like how it is better than typical DOM re rendering that happened in vanilla JavaScript how it that is better

speaker_3: Okay

speaker_1: Because this is the correct a folder everything is theyre all superficial How do you re render a DOM Thats what makes a framework a library special You also agree I assume correct If you can re render efficiently then that is when somebody has an advantage of it Otherwise no Correct Tell me how does Angular does a re rendering in an efficient way compared to vanilla JavaScript

speaker_3: Thank you so much

speaker_2: I can think of one way where Angular is special in terms of change detection is one of the most simplest yet powerful is two way binding right now where its easy to keep up with the UI And also we get the freedom to choose the strategy as well For example if we have multiple components I can choose

speaker_1: No no let me be very precise Like what technique Angular uses for re rendering Im only interested in that And what is the technique name and how it is better than typical DOM re rendering See biggest advantage both Angular and React also is the DOM re rendering correct Whereas in case of plain when JavaScript the complete DOM is re rendered or people at least think that way And React and Angular has a superior way of doing it What do you think Angular

speaker_3: Thats good

speaker_4: users

speaker_1: write render the DOM in the most efficient way if you think you need some more time you can tell or if you wish to skip we could go to the next question

speaker_2: I can think of zonejs zonejs it uses zonejs for change detection

speaker_1: Okay

speaker_2: Yes I know when change detection can be occurring when there are events and as was mentioned two way violin but does this uh is it aligned to the question I am now not sure when you ask

speaker_1: Actually change detection is what you see will make the angular to re render the dominant way Aditi correct

speaker_3: Okay

speaker_1: So please if you wish to elaborate please elaborate on change detection


How change detection works lets say you have an array of 10 elements rendered on the screen ninth element updated correct That need to be now re rendered on the screen How does change detection make that happen

speaker_2: There are some ways where change detection happens seamlessly that are suppose if there is any events any click events any change events then then the any HTTP request if I use async as an operator even when there is lifecycle hooks I may see if I may say and then there is a


input input output uh communication that is the when uh this happens seamlessly and zone js is responsible for that when it comes to manual registration i think that we can use cdrdetect changes uh that is how we trigger it manually

speaker_1: Mm

speaker_2: Especially when whenever there is a change in input as you mentioned that I change the array how did it detect I feel if that array is used as an input to another component and if the parent component makes changes then input property automatically keeps up with that So overall I think zonejs is the real hero in Angular

speaker_1: Got it Sure Can you please present the screen Aditi back where well solve a question for around 15 minutes and then probably well come back to some more discussion

speaker_4: Got it got it

speaker_2: Yes is

speaker_1: See the question is very simple today and we have around 15 minutes to solve this problem We should implement a countdown timer This is one of the most common interview questions that is asked in both Angular React and HTML CSS and JavaScript also Where we will have a timer We will show seconds and minutes Okay Like first it will be 00 seconds 00 minutes You click on start The timer gets started Okay And it starts ticking One second two second It will become 59 second Then its 60 second and it becomes one minute zero second


got my point Aditi and it keeps going basically and if you click on stop or if you stop or reset it will be reset back to the zero so we have start reset please implement this I want to I want you to implement pause and resume but that we could do later question clear to you Aditi

speaker_2: Uh yes so when I will start just one question when I should use a start uh it will keep on incrementing until I use stop right

speaker_4: Got it yes

speaker_1: So

speaker_2: So and it will be in the format of zero seconds and zero minutes

speaker_4: Oh

speaker_1: Correct Well have like seconds colon minutes 00 seconds 00 minute is what well have by default Whenever click on start the timer starts where first second starts sticking And then whenever whenever it becomes 60 second it becomes one minute 00 second Then one minute 59 second it becomes like two minutes 0 second It keeps on happening

speaker_4: Uh edit

speaker_1: Yeah so I mean UI is up to you Im not too concerned about the you look and feel Im primarily focused on the functionality We have 15 minutes to solve this Aditi Okay get started If you have any questions you can ask me in the middle as well How efficiently you solve thats what Im looking for You are iterating an approach Aditi in your mind correct

speaker_3: Okay okay

speaker_2: Uh yes uh what my uh idea is earlier I was trying to create a new component altogether but um I will I thought that since the time is less Ill just integrate in this Sure Ill be declaring uh seconds and minutes as a variable and Ill initialize them with zero Okay And then uh uh yeah Ill also call functions here start and stop Okay


I am thinking if Im not sure to use interval

speaker_3: Um

speaker_2: interval where Ill keep on incrementing the seconds


And uh


First stop Im not sure uh how to use the probe Im still thinking

speaker_1: do one thing you start the implementation where at least let it start updating the time stop part will come like how do we solve in probably by the time you start solving it you might get some idea if not ill help you you can get started

speaker_3: Oh slowly

speaker_2: So there in terms of stops should I flush both these values to zero Im thinking

speaker_3: on

speaker_4: No youre doing the right thing you have to just swap the position

speaker_3: Sending

speaker_1: First it should be minutes and then it should be seconds

speaker_3: Most should be made

speaker_1: Its happening right correct only right like now it became three minute three minute one second three minute two second three minute three second its happening correct only

speaker_3: Its happening in the background

speaker_2: Yes and in terms of stop uh I was thinking to make these both values zero

speaker_1: Please try

speaker_3: Yes sir yeah yeah please stay there

speaker_1: Please try that lets see

speaker_4: We have another two to three weeks

speaker_2: no no sorry Im just sorry that is not stop stop is actually storing those well reset or date what I was talking about was reset yeah lets lets consider

speaker_3: Im sorry

speaker_1: Yeah lets lets consider for time being stop as reset only when you click you click on stop itll

speaker_4: itll be back to zero okay how do you how do we do that

speaker_1: How do you how do you

speaker_2: Its a bit

speaker_1: Just before you save it

speaker_4: Before you save it think what is the problem with this or it will work perfectly

speaker_3: I dont know

speaker_2: Oh I have started the interval I have not stopped it So once if even if I stop it will temporarily be 0 0 then once again it will start because its an interval

speaker_4: Perfect good catch

speaker_2: I dont know the function per second per sec uh so you can test

speaker_1: So you can yeah

speaker_3: You can use

speaker_4: Clear interval to clear the interval okay

speaker_2: clear okay we use clear interval okay

speaker_1: You can start again


So lets lets quickly reiterate the code So we have two functions start and stop correct So in start youre basically creating a variable called this interval that youre clearing on whenever they click on stop Youre running an interval for one second correct And in every one second youre incrementing the counter And if whenever that particular counter reaches a specified value for simplicity we are taking it 10 but should be ideally 60 60 seconds is one minutes So when it becomes 60 your initial seconds are zero and incrementing the minutes correct On stop you basically are resetting the value

speaker_4: So lets

speaker_1: to the initial value on UI can we go HTML page


So UI is again very simple so where we are rendering the seconds minutes and start and stop button character DT

speaker_2: Its its

speaker_1: Can you stop sharing Aditi


So Aditya Im done from my end I have my feedbacks in my mind and Ive written few things if you have any question before I share my feedback please let me know

speaker_3: I cant think of one right now so Ill immediately

speaker_1: Sure Aditi Aditi let me give you what I feel about the overall entry process right At three years of experience so you are somewhere in the mid range category You are not even the whatever expected from senior is not expected from you but whatever is expect from junior is also not expected from you We you are somewhere in middle correct Full fledged system design questionnaire will not be asked for you but there are certain things that they expect you should know very much in depth On that note the positive points Aditi are like excellent


communication skills one and uh communication usually divided in most of my research two two communication skills are there one is english communication skill another is technical communication skills people who are very good at english cannot articulate technical concepts very well unless they know the technical concepts correct so i feel to large degree both the communication skills are very good at whatever the concepts that you know you are able to explain it very

speaker_3: I feel it

speaker_4: skills are very good at the time whatever the concepts that you know you are able to explain it very well

speaker_1: Okay even if it comes to coding


Although the problem was quite simple you without any auto suggestions or looking for the syntax error

speaker_4: As though the problem was quite simple you without any auto suggestions or looking for the syntax are able to solve it which is good which is also a lot of people do not do now they expect lot

speaker_1: Which is also a lot of people


of external help for writing the syntax where do i see primarily the areas of improvement aditi with the how angular re renders the screen see that is one of the most basic question that you can expect in an interview correct so that is something i mean whenever youre not sure of those questions you might be able to build a website like youtube in a matter of a month that caliber you could be but whenever the fundamental concepts are unknown the interviewer gets little bit of a negative impression because an


view right so fundamental concepts matter a lot so my only suggestion is like focus more on understanding these fundamentals very well aditi okay good thing about the even so small question of dsa that i asked it was very easy question eventually you could come up to the two pointer approach so my suggestion is like solve some decent number of problems so that the your mind starts thinking analytically so that helps you both in the dsa problem solving as well as on the problem solving of a typical anything whether its react or


or DSA everything the analytical thing is very important solving more DSA problem will help you to do that atiti rest looks good to me this is my honest feedback you have any closing thoughts or any questions

speaker_2: Uh I have one honestly Vasanta What is your take on front end developers doing extensive lead code like very extensive hard medium talking about

speaker_1: So this is a very good question I think

speaker_4: Is this a very good question at DIT

speaker_1: So I myself have solved a good number of problems on LeetCode So my suggestion to all is unless youre targeting companies like Google there are hardly few countable companies which are whose interview process is purely driven by DSA Like if you go for Google Ive given interviews where three rounds pure DSA they did not ask any front end questions Okay So if youre targeting such kind of company then I would advise you solve as many number of problems as possible because how many numbers to solve nobody knows


So its good to solve any number of problem If not if even if youre targeting a very premium product based companies also most companies for a front end developer do not ask a very very complicated DSA They ask DSAs but it is usually in like array string stack queue and linked list five data structures Within these five data structures so I suggest everyone the same thing like try to solve 100 problems collectively Like we have 60 easy problems you solve 20 medium problems you solve and 20 hard problems you solve


by easy problem so 20 medium problem means one medium is two hard problem one hard is two medium problem so when you solve one hard problem youre in time solving four easy problems correct so start by solving as many as possible as easy problems spread across the five data structures array strings tag queue and linked list in fact i made a video how much dsa is more dsa i can put the link on somewhere on the screen the description section please go ahead and check that as well aditi so beyond the five data is it required to learn from the learning point of view yes


From the interview point of view the probability of asking questions beyond this is less so you end up spending so much time learning them without any return thats what money is

speaker_2: oh okay okay so its expected uh and its always good to have knowledge

speaker_1: Yes I say if you are interested in learning DSA you go beyond linked list like trees or graphs or very specific algorithms like Dijkstra to find the shortest node you could extend and learn But from the interview point of view for most companies I suggest you stick to five data structures array string stack queue and linked list Solve collectively 100 problems from these five data structures from LeetCode Thats going to be most helpful for you and everybody whos learning DSA for content

speaker_2: Thats great uh thank you it really helps me a lot

speaker_1: Thank you Thank you Aditi I assume all the audience who have watched the video like the video If you like it please like the video share the video with your friends And if you have any comments regarding the video please add those comments If youre not already subscribed to my channel please subscribe I try to bring more such interview and other front end related content Thank you so much for watching Catch you in the next video
