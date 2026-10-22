---
id: UjAVRuURFNo
title: "Learn How to solve Machine coding step by step | 2 year experienced @React\
  \ mock interview \U0001F680selected\u2705"
url: https://www.youtube.com/watch?v=UjAVRuURFNo
date: '2024-08-28'
duration: 00:34:48
model: nvidia/canary-qwen-2.5b + sortformer
transcript: true
speaker_count: 3
speakers:
  speaker_1: null
  speaker_2: null
  speaker_3: null
---

speaker_1: Hello all welcome back to Karebath Basans YouTube channel previously known as Uncommon Geeks My name is Basan I hope you all doing well As in this video series where we are doing a lot of mock interview with me I have Faizan today hes from Delhi So more about Faizan as you know hell only be telling you guys But how this interview is gonna be Im gonna explain Like most of the videos Im gonna start with a simple system design or like scenario given sort of a question followed by some basics of JavaScript and React Finally we end the video by a quick machine coding question Okay thats how the interview is gonna be


some reason faizan is not able to answer some questions im going to answer that the end of the video if he answers all the question well then probably i will not be doing so i also dont know will there be a post video or not that depends on how faizan will perform okay please watch the video till the end so that you will get benefited now faizan if you can introduce yourself we can get started

speaker_2: Uh yeah so my name is Fezal Im from Delhi Im working as a in AT6 agency so its a service based startup as a senior front end engineer and I have around two years of experience

speaker_1: Good good question so we have overall two years of experience and where the two years of experience lies in the question

speaker_2: So its basically in my initial career I was working in a full stack but later I switched to front end engineer and working on a React framework

speaker_1: Got it Sure sure So Faizan lets start with one of the most common interview questions Okay Im presenting a whiteboard now Okay


Whiteboard One of the most common interview question in the system design recently is not recently its been quite some time is the news feed app Okay So Im just drawing on the screen Okay


Hope youre able to see right


lets say and this is a typical facebook app let us imagine okay and we have like well have multiple posts here correct like for example post one post two okay followed by the remaining posts correct and on the top we will have an option to like create post correct so here you will have an option like where you could create post


like create post and this is like post one post two post basically this post one post two can be of anything like it could be of text it could be of uh image it could be of something between all the things that are possibility if isnt correct so now my question would be well lets start with one of the most common interview question around this that is infinite scrolling correct

speaker_2: No no no

speaker_1: So right now youre able to see two cards correct and whenever youre scrolling whenever youre scrolling up


happen is you will have like more cards

speaker_2: Ernds

speaker_1: be and control v if i do after you scroll probably you will have this as like post three correct this would become post three this will become post four

speaker_2: Was fort

speaker_1: Yeah correct Like I can make like an arrow here like I can make an arrow here and I can like name it as after scrolling


or users if I I can literally users have to see I think like this I think users can see like this is the


Initial render initial render


And shield ended okay


children okay and this is more like after user scroll okay


user scroll please tell me if you have to implement the infinite scrolling of is and why what are all things comes to your mind you can start explaining step by step and if you have to implement this how you are going to do thats for the example say consider an example of facebook like we are building system similar to facebook please start yeah

speaker_2: yeah so like uh on the header part so create post button is fixed one so ill choose a sticky button so if we scroll it it should uh not uh be out of the window or out of the viewport so then what ill think according to my user uh base and user experience like uh we will fetch uh suppose if two post is in the viewport uh and we decide


to put two posts in the viewport so ill check the viewport height and according to it ill fetch two extra posts uh for the initial rendering after if we will check the fourth post is like uh getting into the picture in the viewport then ill fetch the next uh uh two posts and append it to my data

speaker_1: Okay

speaker_2: So Ill use this approach

speaker_1: So yeah whatever you told correct Reza So basically infinite scrolling the whole point of infinite scrolling is how you are going to basically track the end of the page reached and even before the end of page reached or sometimes when the end of page reached you are going to get next set of data and show it on the screen correct Can you start answering me like how basically you are going to determine whether the end of page reached or not

speaker_2: Okay so we can use viewport for it We can check if scroll is the window is in the post 4 is in viewport I dont remember the exit Okay I feel like I have not implemented it


uh nine final


But we can check viewport size and all those things and there may be some

speaker_1: Okay so somehow youre gonna identify the end of page reached

speaker_2: End of the main screen yeah

speaker_1: Yeah and youre gonna make an API call to get next set of data

speaker_2: Okay

speaker_1: So now the there is another problem as you know that the one of the big problem pagination is you should keep getting the data from the server correct so are you aware of like different pagination techniques that is used from the back end or in general what are the different pagination techniques that are available

speaker_2: Uh so one I uh which I followed is like a limit and page number which we use uh to fetch the data

speaker_1: Okay please explain how you are gonna what is what data client pass what data we get from server can you elaborate

speaker_2: Ah yes so in that technique like we pass two parameters in the URL for a get endpoint One is limit and one is page We will check the limit what amount of data we are fetching for a single time when API is calling and what sequence Suppose Im fetching two posts at a time and I need the post number five and six So Ill do a page three and limit will be the same too


uh very limit and post uh I can also check if uh the scroll speed and I can increase the limit in that case as well so

speaker_1: So basically you are gonna pass the number of posts required and the page number


Like for example initially lets say page one and ten so youre gonna get around ten

speaker_2: And Like for example

speaker_1: Then youre gonna say 10 is more like fixed letters hypothetically and second page and then again 10 posts correct 11 to 20

speaker_2: the


Yeah

speaker_1: Correct So if only this could be the last question then well go to other problems See one of the biggest problem that I can think of this approach is systems like Facebook right They are like very dynamic sort of a data comes Like for example by the time you scrolled probably theres so much of data that has come already For the simplicity of you and audience Im saying lets say there is 100 data on the backend Okay And you request for 1 to 10 in the beginning rendering Correct You got the data and you rendered it By the time user hit the end of the page obviously


is more data might have come So where more for simplicity understanding lets say more 10 data has come more 10 posts So 100 whatever the earlier database size has become 110 now


Correct Obviously the new data will not be added to the end of the database It will be added in the beginning only because thats the whole intent Fresh post has to be shown So now what would happen is we had one to hundred So one to 10 was already came to client Now that one to 10 became 11 to 20 A new one to 10 has come


So next time now what you would do you would send a request to server where you are sending like page two where you are getting 11 to 20 is something that server should send But what has happened now

speaker_2: So next

speaker_1: 11 to 20 is same as 1 to 10 You got my point right

speaker_2: Exactly

speaker_1: so this is the problem with this approach i am assuming audience got the problem where the window has slid it one to ten became eleven to ten new one to ten has come correct only just think uh is there any way you can answer to this question if this how to overcome this problem


Have any idea

speaker_2: a time of pagination as well we can take sort the data or something to new to old so we can tackle those problems

speaker_1: One approach is what you told is similar to that basically client takes care of it like lets say every time you got a data you check whether the data already exists or not this can be easily achieved if you are maintaining a map of like post id and actual post content we can easily check whether that post data is already present or not and if it is already present make a next request okay but the problem is how long to keep doing this this becomes recursion


I gave you simple example where 1 to 10 we can 1 to 20 it not necessarily be like that correct it might have like by the time you make level you decide to make next call next call also the data might have slid it


get you know what Im saying you send to it becomes free but uh

speaker_2: Im not too big a stretch

speaker_1: 11 to 20 might have become 21 to 30 So you might end up getting same result correct Again no right or wrong implementation depends on the system we are building But more you and the audience read more about this There is two types of pagination mainly the cursor based and the offset based

speaker_2: I dont know

speaker_1: So right now what we decide is offset based approach There is another thing called cursor based approach Okay please you and the audience if anybody in the audience know please mention what is cursor based approach Okay so Faisal and now let us start with some very basic theory questions Ill ask you and then well go to the some coding things Okay So can you present your screen Faisal with code sandbox opens Sure okay I must say you already signed in correct

speaker_2: Im sure you already


Yes yes

speaker_1: Please explain me uh Faizan what are fragments in uh JSX or fragments in React in general

speaker_2: Okay so the React there is a big challenge like when we want to wrap a component with some extra things suppose we need to write a box and we dont want to use a nested divs and all so the DOM will not become a heavy So we use the fragment Fragment is a empty wrapper Its kind of empty wrapper which can be used in React to used in


virtual DOM so it will not be appended in the real DOM so we call it fragment it is a feature of React

speaker_1: Can uh so we can

speaker_2: Uh so we can use the

speaker_1: You can give a simple example person when to use fragment

speaker_2: Uh yeah so uh if uh you want to append something like uh this is a project I dont want this dev to be presented on the DOM so I just need uh we can use this empty fragment in that case okay or we can import the fragment from uh uh React correct uh yes so these are the two ways

speaker_1: these are the two ways i get what youre saying but i think the simplest answer is a tag a group of tag cannot exist by themselves they have to be enclosed by something thats the basic logic correct you can have h1p and any other list tags so they cannot be represented just like that where it should be enclosed in something

speaker_2: Thank you guys

speaker_1: So either you could enclose them in div or either you could enclose them in fragment correct Or either you could enclose them like empty thing we added empty and the empty opening and empty closing brackets Three three possibilities of is and correct So now can you tell me the difference of is and just using the fragment

speaker_2: Three three positive

speaker_1: And no fragment just opening and closing what is the difference

speaker_2: So the main problem I face like uh in my day to day development like we cannot pass key to an empty uh fragment but we can pass the key to this fragment right

speaker_1: Why do you think you need to pass a key What what is the need for that

speaker_2: When we need to append an array of a data or an object we need to pass a key to every element we are mapping

speaker_1: Um and what is the problem using the DU versus a fragment


What is the difference of putting another fragment enclosing within a fragment and enclosing within a D What is the difference

speaker_2: So suppose if a styling is given to a parent child it will not if we enclose it with a div it will not be implemented to a child tags But if you use fragment the parent div if you will give the styling so it will be reflected too

speaker_1: Sure and you just then it comes to your mind uh present

speaker_2: The DOM become heavy like if we use div multiple divs we are some of the divs are not used even to any container or something

speaker_3: So but if you use fragment we can

speaker_1: Got it So fragment you say lightweight compared to div and as we feel like div is not at all necessary it is just a necessary requirement as div is something a meaningful tag a division basically

speaker_3: Hmm

speaker_1: we dont want that that time we could use the fragments okay sure so um you want to say anything present or


Sure sure so now probably we can get started with the problem but just before that I have only one question what are children children prop in do you can you please explain children prop

speaker_2: Okay so suppose in a component lets should I show you an example as well

speaker_1: No I think roughly you can explain if I needed I like uh so

speaker_2: So if we are children is a inbuilt prop in JavaScript So suppose if we are we are creating a component suppose we are creating a button component to reuse it everywhere So if we wrap that component So for if suppose this is a component we created for React So inside all the code all the code inside that component will be passed to its children prop

speaker_1: Mm

speaker_2: So we can access those children prop inside that component

speaker_1: Okay lets say you want to render the children So everything that is inside that particular component gets can be used correct

speaker_2: Yes

speaker_1: Can you give me one practical example of where you felt like you used this when is the right scenario to use a children plot

speaker_2: So one example I already gave like when we create a bot button component so there we use multiple times like a children prop Suppose I created a component called app button So I can reuse that component and the text inside it I can pass it as a children So Ill track those children and I can pass an empty button Like I can use a button tag inside my component and pass it inside that


children inside the curly bracket I can use the children prop and append the text

speaker_1: Okay sure Ill send a question to you in the chat section now Faisal You have around 15 to 20 minutes to solve the problem Copy the question based on the here on the editor And you can maybe zoom in this for a while a little bit so that audience can see it better If any question regarding the problem you can ask me Others you have to get started

speaker_2: So search filter display a list of posts implement a search bar and filter the list based on user input get okay so okay here I need to implement a display a list of posts using this API


and Ill use a and need to implement a search bar Correct If a search bar is mentioned like we need to search the M whatever we search according to it we need to append the post

speaker_1: Can you open that URL once the JSON placeholder URL can you open it

speaker_2: Newfoundland

speaker_1: So here let us search by the title


as I think that is little lesser length So lets say in the first case I search S U N T and lets for the simplicity sake lets imagine any title that starts with S U N T should show

speaker_2: Okay so any type of chart a query yeah

speaker_1: Any type of data query Yeah sure No theyre not going to give that Theyre only giving that post I dont okay you can chuck if theyre giving Otherwise thats that filtering is something that you need to do not on the API

speaker_2: Okay

speaker_1: So you have any questions

speaker_2: We have to implement them

speaker_1: Whenever you do the search its more like not like search its more like local search not like the global like search

speaker_2: Sorry

speaker_1: In the data that you already got perform a search okay

speaker_2: Okay okay

speaker_1: Sure get started

speaker_2: Okay so Ill create a post uh state

speaker_1: Okay

speaker_2: so that I can store the states I can store the data in a state so Ill use the u state to store the state and for initial Ill use the empty state

speaker_1: Good

speaker_2: So uh Ill create a function uh


to get the state


Okay


Ill be needing a exos I can use it to fetch the data exos exos as a API client so Ill use exosget


Ill use uh the async function to let uh be more clear like

speaker_1: Hmm

speaker_2: I can get more clear Ill fetch the data


Watch the response


Ill use async await


Let me first console the other set I believe we should get inside the response dot data so set hosts


Very loose


Im gonna play now the boss


function literally


Such things


Almost


Interesting


Okay sorry


Um


Um there I do is


And here Ill give what key is


Gosh


Yes okay but my post is not visible yet


use in the use effect ill call the get data function so that if when my component get mounts uh the get post will call and data will be stored in this so i have not imported that zeros


Okay so currently Im getting all the data


I prefer to


So we need to create a search bar


will be a type of text and Ill create the another state with input


Right


With a memory stream

speaker_1: I think that input spelling mistake yeah input

speaker_2: Oh yeah so Ill give a value to it as input


And if uh on on on change event Ill


on it as E


set input and set e dot target value


So this is a control component now

speaker_1: Uh

speaker_2: Ill change it

speaker_1: Styling well check later okay basic one you give next well check the styling later yeah

speaker_2: Uh yes so suppose this is working fine as of now So Ill do one more thing like Ill write a use effect


where Ill give a dependency as input so whenever input will render so it will change so my this use effect will be called so and now Ill check


input is suppose


I need to do the filtering in in filter logic as well


exposes


Ill create a function


So every time this will call I will


do a filter data


And Ill write another state


get that


So this query data Ill use to pass suppose if the input box is empty so Ill try to get the filter from all the posts suppose if Ill search for S U M T so it will all posts will be stored there and Ill show the filter state here only so Ill pass it here for now


So for the initial rendering like uh


And suppose data if uh if post is also changing


And if inside if input is empty


That is a falsy value so Ill set query data as post


so ill show all the data if input is empty the code will get uh


Uh Ill get uh

speaker_1: I get it

speaker_2: Something in the input first time when it is empty

speaker_1: First time minute is empty we are gonna return all our next time

speaker_2: Next and all the things


filtered uh data now ill im gonna filter it so ill filter from the post so that ill get the filter from all the posts so ill filter it post dot


And Ill check uh with the post and if post dot title


begin with like uh posttitle will be a string so ill use include i can use uh so i need to return all the things or it will only start suppose s and p is in the bit

speaker_1: That begins with the given search string that you return complete title

speaker_2: Okay were gonna do this one


That may be a


starts with


I dont know


So to start with we have a function


start


starts with okay we have a function called starts with


Ill use it as an input If so this will give me a filtered data So Ill put set in set


query data as


Uh


to data

speaker_1: We have last three to four minutes okay

speaker_2: Okay uh yeah so now if Ill check uh with this is S U N T

speaker_1: Good

speaker_2: getting this but Im not sure why Im getting this as well

speaker_1: Try EXA also lets see


exe


Its not coming correct

speaker_2: feature


Okay I need to figure it out like uh is this working correctly


Okay post dot title we have a post dot title


S U N T is working fine Q U I is working fine

speaker_1: I think its a completely one string I think this is completely one string

speaker_2: I think thats a complete hub


Okay yeah okay okay yeah

speaker_1: Its got exactly that a good try could be

speaker_2: cycle be better a cycle yeah

speaker_1: Yeah

speaker_2: you


And yeah I cant get it


Okay Im not getting the due to stability okay

speaker_1: Anyway I think that is fine Most of the things are working as expected correct Looks fine


Anything else you want to make change person or we can discuss

speaker_2: Ah yeah I am King Bang

speaker_1: Sure so yeah uh can you just uh I mean zoom out the right side portion a bit I mean like the minimize the post this side


I mean except the code minimize everything so that audience can also look at the complete code once


Sure can you zoom in again maybe control plus command plus


So basically Ill just quickly summarize for you What we are trying to do here is we have two functions One is get post and another is filter data So get post is where we are making API call to get the data Filter data is where actually we are filtering the data to match whatever the user has searched Are we matching with that or not Correct We have two use effect we have used One for can you scroll down Yeah So one for like filter the data and the one is for the getting the post first anyhow line number 37 gets triggered where we get the post and we are line number 33 that every time whenever the

speaker_2: Mm

speaker_1: input whatever your typing is changed or every time another post is changed basically only the first time the post would change we are calling the


Finally whatever we are rendering on the UI is the filter data


Thats what we are rendering on the page So now where do you think actually the posts are getting used in line number 25 for filtering purpose Correct The posts are used only

speaker_2: Thank you


on the page


Yes exactly got it

speaker_1: got it sure sure so um well discuss phazon this and the overall about how what are all how the things went well see regarding this uh phazon the very clean implementation i have so many mock interviews on my channel this is one of the cleanest mock machine coding ground i know the question is fairly easy its not im not saying its very hard but still the approach you took step by step you are able to do which is very clean and neat which is kudos to you okay few things as i as an interviewer see that could have improved was one is the api call


Correct if you go to the get post can we go to get post please


So here in line number 17 is you know we are not handling any error here The app can easily crash

speaker_2: I can see you

speaker_1: All right if youre doing this And another thing one of the common mistake almost everybody does in the machine coding interview is like not asking the obvious question See I shared you an API and there is some X number and you started your implementation What if that API tomorrow returns 1 million data


getting appointed then the filter will filter sufficiency will be totally degraded line number 25 right this is not a problem this is just where probably in next interview whenever some questions are asked you can think around it right because always make sure you ask the extremities what is an extremity

speaker_3: So its all based

speaker_1: What is the minimum value What is the maximum value in the interview so that always youre gonna be safe correct Otherwise there could be chance Now this is fine its a mock interview Then interview has like 1 million data is there then the filter would fail correct Its not if it would fail the performance is awful obviously it will get reduced correct And another thing that I noticed

speaker_2: Thank you

speaker_1: I think rest look good to me its some very clean approach but only couple of suggestion that I give you can stop sharing Faizan and I have like some couple of other feedback not specifically on the problem solving around the basics like the couple of questions that I ask like newsfeed correct where we started with yes newsfeed Im not expecting a two year guy to like know all of it about the newsfeed like I always say in my mock interviews like think look at every system like how do you develop it like just before we we actually we dream

speaker_2: Like you

speaker_1: entire thing in there that whiteboard or the drawing board correct so next time whenever we look at the drawing board dont look at it like a user look at it like a developer if you have to build a drawing board how we are going to do same applies for the facebook newsfeed right that is the easiest way to start understanding the systems like how you become so whatever answers you told was not fully correct or not even wrong one approach you told whatever you would build it but i would highly suggest you to you and all the young developers that starting journey two to three years of experience to look at every system like

speaker_2: But this

speaker_1: do you build it so that whenever such questions are asked in the interview most likely youll be able to answer im sure most companies do not have system design for two to three experience but they would have some of a scenario driven question like some portion of the system just how do you guess the output for example thats i think thats something that you could improve on and regarding fragments and other things what i feel one common thing around the theory questions is you know answers to many you are able to give answers but the initial answer that you are saying is not the answer eventually you are coming to that answer


So for example fragments


What is the use of fragments Basically the list of tags has to be enclosed in something So you are using the tags correct So you told it actually but you came there eventually correct You can tell that to the point answer to you and the candidate also because some interviewers are like have time enough time to like discuss and extract the answer Some interview will be in rush where theyll not have time to like extract answers out of your sentences Faisal Okay Thats all I wanted to say You have any questions you can ask me Faisal or you can share your interview experience also

speaker_2: Does it


Yeah so it was a nice experience for me Like uh I have been interviewing after a very long time So uh it it is a great experience And the questions I didnt expected like uh these type of questions I didnt watch a lot of video of yours I have watched some of them

speaker_3: And so

speaker_2: uh it met with my expectations so i got a very good feedback i got a very good questions and this will help me to like improve and how i can structure my answers and all those things

speaker_1: Thank you so much Faisal I hope like all the audience who watch the video like the video like how Faisal told you if you like the video please like the video comment whatever you felt honestly please share the video with your friends so that they can also get benefited Thats all for this video See you in the next
