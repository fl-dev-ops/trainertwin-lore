---
id: 5Z6tpdmtzG0
title: Learn LinkedList in JavaScript in 40 mins (LinkedList Introduction)
url: https://www.youtube.com/watch?v=5Z6tpdmtzG0
date: '2022-07-10'
duration: 00:11:42
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 2
speakers:
  speaker_1: null
  speaker_2: null
---


# Learn LinkedList in JavaScript in 40 mins (LinkedList Introduction)


## Transcript

speaker_1: if you create lets say you will use this memory location first the one


Then you will not use to you will use the second memory locations So lets say you stored 10 value 10 here Okay Then you have stored value 20 here Correct And you have a link from this to this

speaker_2: Hi all welcome back to uncommon geeks myself Faustin I hope you all doing well as you know theres a video series where were discussing about data section algorithm Ive already made one in

speaker_1: introduction video clearly explained how difficult or how painful the data structures and algorithm for front end developers and how this series is going to be Please watch the introduction video if you have not watched so that you will be more prepared mentally when coming to this video Okay So what is this video is about So this video is about introduction to linked list Okay So one important trivia Ill tell Actually JavaScript it doesnt have a linked list of its own Okay What do I mean by that So why JavaScript doesnt have a linked list of its own Somewhere in the video Im going to decode that


So this is also one of the very important interview questions So please do watch the video till the end Okay Without wasting further time lets get started with the linked list introduction Okay Ive created a small presentation Okay to show uh about the linked list so im just starting with that so linked list is a linear data structure in which elements are not stored at a contiguous memory location the elements in a linked list are linked using the pointers so this definition is not mine as most of you guess this ive taken from the gix for gix and this is a typical definition anybody would write similar so since ive read by


already many so I tried taking it from somewhere all the credits geeks for geeks so now this what is linked list okay in very simple words so you have a memory chunks okay but they are not in a contiguous location they can be accessed using the linked list how Im going to explain in in a while okay next so why linked list correct so you know what is linked list at least basics now now why linked list linked list offers some important advantage over other linear data structures unlike array they are a dynamic structures


resizable at runtime also the insertion deletion operations are efficient and easily implemented okay why this is why they are better than array in some cases let me explain you that okay so so this is a a sketch that ive already prepared some uh rectangles for you to represent the memory locations okay so here if you see we have one two three four five lets say we have five memory locations as you all know array is a contiguous memory allocation correct array means you have a chunk of block already allocated there are


dynamic arrays but mostly arrays are static so you would use array when you know the size of whatever you are processing correct lets say the number of students in a class or number of employees in an org they are not dynamic they are static you know whenever they grow then probably you will increase the arrays thats how it is done arrays are generally picked for the static size correct so now lets say you have an array and you needed a five memory location for the array what would the compiler would do or how generally execution works is theyll the compiler or the system would look for five memory locations that are continuously available


lets say int I think it is 8 bytes so 4 no values means 32 bytes so anywhere 32 bytes are readily available then that particular chunk is allocated for the array so what is the advantage so even before the program starts execution the memory location allotted so it is very fast because you dont have to look for the location correct whereas linked list so lets say it needs now actually the linked list has nothing called a predefined size its going to be dynamic so wherever the space is available it will be keep picking that correct so so linked list can better utilize


the memory compared to the array so there are disadvantages too that im going to explain in a while so look at this one lets say there are five memory locations okay so like i said if array wanted now five memory locations you have only five locations here out of which the second location is already picked by somebody okay if second location is already picked by some some other processing now array can be created either for one location like one element array or three element array you cannot create five element array correct so now so now but you have to utilize the memory


correct because you you cannot leave the memory like that you have to utilize it well so what you will do you will create a linked list so linked list if you create lets say you will use this memory location first the one then then you will not use to you will use the second memory locations so lets say you stored 10 value 10 here okay then you have stored value 20 here correct and you have a link from this to this and then you have a link from this to this then you have a link from this to this okay then lets


say due to some operations of memory location 2 got free okay so in that case lets say let me decolor it so lets say due to some reason uh this one also become free so let me give some gray color so due to some reason the memory location 2 also become free what you can do in that case from phi you can link back


you can store some memory lets say 40 50 60 some number you can store here as well okay guys if not for anything at least for my effort to do this drawing or creating this one you should please like my videos and subscribe to my channel and comment geeks okay now please please do that if youre not already done so that will definitely motivate me to make me make more good big content okay so now so if you look internally so one three four five and two it looks like quite jumbled correct but from the program perspective if you dont know


is happening in the inside or in the hardware correct but we know what is we only know that all memory locations whatever we are requesting is available to us correct so one three four five two we are able to access that and write the code correct so that is the beauty so anywhere the memory is available so linked list can actually go and grab that memory and store the values correct so that is the beauty of linked list


I was telling one point where the linked list is is not a data structure or typically how linked list is persona linked list person in other language and JavaScript is different why see JavaScript lets take an example of Java or C plus plus where the programs are written in a compilers correct and the in in the any editor and they directly interact with the hardware with in Java there may be some middle engine but technically they directly interact with the system hardware correct C has a C compiler to interact with the memory Java has


Java Java C etc which will interact with a device compiler or the system hardware directly but JavaScript is not like that JavaScript runs on a browser correct now I run generally with help of a node server but Java is prepared to run on a browser correct browser is a software so browser is a software has access to the hardware but JavaScript as a programming language has no direct access to hardware correct so how JavaScript can get the memory location and try to link it that doesnt happen


So this is very very important concept you have to remember in JavaScript all the data structure operation we do are kind of a mimicking the behavior because finally JavaScript everything is object in JavaScript correct so even the link list has to convert into an object in JavaScript to work well so Im going to explain that now how it going to look like in JavaScript okay now lets go back to the presentation see this is a typical singly linked list structure so we have a value we have a link you are


already saw this from a sketch example so link is 1 in this case the value is 10 so link is 20 in this case and the link is 3 in this case and the value is 30 value is 20 correct so that goes on every node has two parts in singly singly linked list one is the value another is the link so now this first node has pointing to the second so link part of the first node will be holding the value 20 value part holding the 10 so if I had to draw in a similar fashion


where have you seen PowerPoint correct so now in this case we have first one memory location is 1 value is 10 okay next Im drawing another block where


value of 20 correct and a memory location of


So now this 10 is


So value is 10 the link is 1 So now this 10 value and this next low node links which is 2 are interlinked Okay So due to which whenever you are trying to access this next value from this node youll be able to access it Im going to show that also in a while with respect to object notation how we can access that Okay So but in very simple words as you saw every node has a value and a link in singly linked list Okay So how it will become the entire linked list So you can see here So we have a data and the next is having the link of this node


And we have a data again next is having the link of this it goes on until when the next is null its an end of a linked list So next is null is the end of the next I mean that node which doesnt have any next node is the end of linked list The head we generally use for head we generally use for


accessing the first node okay so there has to be somewhere we need to start so we use a head node and whenever the last node is just null then there is no longer a linked list so this is these are the concept that has to be there in your mind now lets decode the object part of linked list okay see now what you saw we have a link linked list what we have we have a element or a value correct so we have an element so lets say the element has a storing a value of 10 next what we had we had a link property or


Next property next basically here pointer link let me name it link only


Now the link should point to the next element correct So here also if you go there is another element 20 and this will have another link


Now this link points to another element element 30


Again we have a link property


So this process goes on So end of the day you are trying to mimic just this as a part of linked list You are not creating a typical linked list that happens in other programming languages like where this link will be actually holding a memory location of the next node correct That is not happening in JavaScript because JavaScript is an interpreted programming language It is not directly interacting with the hardware So at end of the day everything is object in JavaScript So you are trying to decode this or


implement this as a part of linked list okay please please be careful about this point okay most dont know this and they think it is still holding the memory under the hood yes under the hood every time whenever node is created it is allocated with a memory but actually whenever you are programming or whenever youre implementing javascript id say all you are doing is this compiler even now even lets say you create a variable called let x compiler will allocate a memory with the help of an hardware correct lets say for example take an example of google chrome google chrome has a


compilation engine called v8 v8 is a 10 in c plus plus so c plus plus javascript code will be compiled by c plus plus c plus plus internally interacts with the system hardware to allocate a memory for that variable correct so this is a two two step process so memory will be allocated under the hood we may be having some memory allocated for this but on top layer or finally what we as a developers and implementing is just this okay lets decode how to do this step by step in upcoming videos okay thats all for this video if you like


this video please do like this video on youtube channel because i have a bigger ambition of making an entire series about direction algorithm which will be helping for lot of candidates to push their barriers and crack interviews at a very big firms okay i can do only that i can do that only if i get a good motivation from you all select the videos do not forget to subscribe to uncommon gifts thats my humble request share these videos with your friends let them also get benefited thank you so much catch you next video
