---
id: QRczfGahf7s
title: 'How to update states of Array and nested Objects in ReactJS ? Important question
  for #interview !!'
date: '2023-06-28'
url: https://www.youtube.com/watch?v=QRczfGahf7s
description: "#frontenddeveloper #react #reactjs #VasanthBhat #uncommonGeeks\nUncommonGeeks\
  \ is a Youtube channel dedicated to helping candidates clear their interview. There\
  \ are more than 100+ videos and new videos will be uploaded every week. If you're\
  \ seriously preparing for interviews and looking for tips and tricks, please subscribe\
  \ to my channel and press the bell icon.\n\nArray and object manipulation in ReactJS\
  \ using useState is not a straightforward process. Especially if you're processing\
  \ the deeply nested array/object. In this video, I have clearly explained how to\
  \ modify the states of the array and object in ReactJS.\n\nJoin Uncommon Geeks community\
  \ to discuss with other developers: t.me/uncommongeek. \nTo talk to me one one one\
  \ book a session here: https://topmate.io/vasanth_bhat \n\nFollow me on LinkedIn\
  \ -https://www.linkedin.com/in/vasanth-bhat-4180909b/ \n\nMedium Blog https://mevasanth.medium.com/\
  \ \n\nJavaScript Interview preparation series : https://www.youtube.com/watch?v=qcixpy3HQ9s&list=PLmcRO0ZwQv4QMslGJQg7N8AzaHkC5pJ4t\
  \ \n\nJavaScript Custom implementation/polyfills Series: https://www.youtube.com/watch?v=eGzErMUfdpk&t=35s\
  \ \n\nInterview preparation tips and tricks by Vasanth (play list): https://www.youtube.com/playlist?list=PLmcRO0ZwQv4SN0Lb9vxP48cGbluqaaGV1\
  \ \n\nFrontend system design series: https://www.youtube.com/watch?v=gN8LQTff21g&list=PLmcRO0ZwQv4RYUD10hUnWjWb-RRSpm3KM&ab_channel=UncommonGeeks\
  \ \n\nMAANG series for frontend developer: https://www.youtube.com/watch?v=s-b-txm_Gvk&list=PLmcRO0ZwQv4SNhbW4CI4vc-6IHBHCKzZN&ab_channel=UncommonGeeks\
  \ \n\nFrontend mock interview series: https://www.youtube.com/watch?v=uW7MfzoD1po&list=PLmcRO0ZwQv4SwXLVpnKb_nFQx1Wd2XEjD&ab_channel=UncommonGeeks\
  \ \n\nShorts for quick access to all frontend resources: https://www.youtube.com/watch?v=8ByBOT7Aehs&list=PLmcRO0ZwQv4SXtrTYIU_dPygZgOgYV81S&ab_channel=UncommonGeeks\
  \ \n\nTips for freshers: https://www.youtube.com/playlist?list=PLmcRO0ZwQv4QBiZns-nYX5qnHKAepVeqH"
author: careerwithvasanth
duration: 00:13:58
model: saaras:v3
transcript: true
---

# How to update states of Array and nested Objects in ReactJS ? Important question for #interview !!

## Transcript

### 00:00:00 · Speaker 1

to let's say Marathahalli. Okay. Will it work?

### 00:00:08 · Speaker 1

See, did not work. The reason being address is a object again, correct? So you cannot update the address itself because address itself you cannot add a value. address dot first line you cannot. So what we'll do, let us spread the address.

### 00:00:20 · Speaker 1

fine, user details dot address. In that I'm adding first line as Marathalli. Okay. So now, hello all, welcome back to Uncommon Geeks. My name is Vasanth. I hope you all doing well. In case if you're seeing me first time on the internet, I'm a content creator. I help people to clear their interview. I also make lot of videos about the interview preparation, career coaching, etcetera, which has helped again lot of candidate to clear their interview. In case if you're still not subscribed to my channel, please subscribe and hit the like video for this video. Now without wasting further time, let's get started with the topic of the day, that is

### 00:00:50 · Speaker 1

manipulating objects in ReactJS and React Native, okay? So, or updating the states of the object in React Native and ReactJS. So, I'm gonna explain it to ReactJS, but the process remains fairly straightforward for the React Native also. See, it is, uh, whenever we are updating the states of a primitive type, for example, variable X, and you want to change the value of that, it's fairly straightforward process. But whenever you want to modify or update an object and an array in the React, it is not that straightforward, okay?

### 00:01:20 · Speaker 1

lot of people get confused so I'm going to explain all the different kind of variations of the objects and how to update that step by step in this video and I also take you through a official documentation of the react where this is very clearly explained okay so you actually don't need a video but some people will not understand documentation very clearly so I'm explaining okay so I'll also take you through the documentation so that you have a crystal clear understanding about the object manipulation so this video may last for maximum seven to eight minutes so please watch the video till the end so which will

### 00:01:50 · Speaker 1

ensure next time whenever you're modifying an object you don't have to watch any other video. Okay? So I'm already running an application here. So application is nothing just the hello world. Okay? Now let me create a state. Okay? const x then set x is equals to use state. Okay?

### 00:02:10 · Speaker 1

you state when I'm initializing the value of ten, okay? So what I'm doing here is in the hello world, I'll just replace this with

### 00:02:20 · Speaker 1

value of x is, okay? What I'll do is I'll just give the x, okay? Then I'll create a small function like constant update x or add

### 00:02:33 · Speaker 1

ten to x. Okay, we basically means add ten ten to the value of x. Okay. So what I do is set x as

### 00:02:45 · Speaker 1

x plus ten. I think all of you know this. I'm just setting it for some some basic context, okay? Then we have a button. So where on click of button

### 00:02:57 · Speaker 1

you I am invoking

### 00:02:59 · Speaker 1

add ten x, okay?

### 00:03:03 · Speaker 1

add ten to x I'm invoking. Okay. Then here in the button like I'll just give a name as update. Okay. As I have to end close it in a component I'm doing this. Okay. So it's very very straightforward as you can see value of x is whatever the value of x. Whenever click on add ten to x it will get updated and we'll show you the updated value of x. Very straightforward. Let's go back on screen and see. So value of x is ten. If I click on update it's become twenty, thirty, forty, fifty. Very straightforward. Nothing fancy here. Okay. As you all know the value of

### 00:03:33 · Speaker 1

x is immutable. Okay? What is mutable and immutable in very simple words? Mutability is nothing but a value can be changed or not. Okay? So basically the primitive types in JavaScript like string, number, boolean etcetera, they are all primitive types. So in a given memory location you can hold only one value. So x can be ten, then x becomes thirty. Okay? So that memory location cannot hold both ten and twenty. Only one can be hold. Whereas object types are mutable in JavaScript.

### 00:04:03 · Speaker 1

primitive types are immutable, object types are mutable. That means in the same memory location you can update the value. Let me let me tell you how to do that. Okay? So for example you have something called constant.

### 00:04:15 · Speaker 1

user info, okay, which is equals to like first name. First name is uncommon, okay. Second name is or last name is Geeks. Let me do some marketing also my channel name uncommon Geeks. Again if you're not subscribed please subscribe, okay. I am setting creating an object user details. Then set user details, okay, which is equals to use

### 00:04:45 · Speaker 1

state of user info. Okay? Very straightforward. You all know nothing fancy here. I create an object called user info and assign it to user details. Okay? Now, what I'm gonna do is I will just I'll remove this. This as you know is very straightforward. Again, I don't want to confuse you guys. Okay? So what I'll do here is

### 00:05:05 · Speaker 1

user first name is

### 00:05:11 · Speaker 1

First name is user info user sorry user details dot first name okay then user

### 00:05:20 · Speaker 1

last name is user details dot last name, okay? Actually I have made one small mistake here, in general, never just write dot after first name, dot first name, dot last name. Always have a habit of writing this question mark, okay? So if this object is undefined then the second portion you will not have any problem, okay? So have a habit of doing that. In this case it's fine because locally defined variable but sometimes you would get data from the web or API that time this will fail, okay? If user details is empty. The different

### 00:05:50 · Speaker 1

handle but one way is always make sure you put a question mark. Now const update user details. Okay? So now what I'll do here is

### 00:06:02 · Speaker 1

So what I'll be doing is again I have a button on click of which I'll call this button have a title of update.

### 00:06:10 · Speaker 1

On click

### 00:06:12 · Speaker 1

On click

### 00:06:15 · Speaker 1

Okay. I'm calling update user details. I'm calling update user details. So what I have to do is I already have user details dot first name is equals to I'll set it to Vasanth. Okay. You know I already know the object. So it's as it's mutable I can easily mute it. I mean I can easily change the value. Whereas X I was supposed to use the set X only. I cannot change without that. Okay. Let's go back to screen and see. So first name is uncommon. Question mark is not looking good. Let's replace that with colon.

### 00:06:45 · Speaker 1

Okay. First name is uncommon, second name is Geeks. Whenever I click on update, Are yaar, nothing is happening. Why nothing is happening? Whenever I click on update, what I'm supposed to do is, I am updating user details.first name, but it is not becoming Vasant.

### 00:07:03 · Speaker 1

I did not I did some mistake intentionally don't worry. See like I mentioned objects are mutable. Okay. But problem here is this object whatever the value already whatever was there that is already rendered on the screen. You just updating the value of object will not create a re-rendering. Okay. If you have to re-render then you have to use the set state. Okay only set state can re-render the react component. Okay it's like you have ordered a food you have completed eating the food and then you are trying to order again.

### 00:07:33 · Speaker 1

So now let me simply show you how you can do it. So there are multiple ways to do this. I'm going to show you the most simplest way of modifying an object. Okay, let's do like set user details. Okay. Then what you will do here do is you will just take a copy of the entire object, spread operator you know, as it is you're taking a copy. Then what you're doing is first name is equals to you're setting it to Vasanth. Okay. So what you did here is you use the set user details function. You took the object as it is, then you updated the

### 00:08:03 · Speaker 1

first name from whatever it is to the next one. So remaining values in the object that is last name remain as it is no change to that. Let's go back. Refresh. Uncommon is there. Update. Vasant is updated. Geeks is not updated. Okay? That's how it will be done. Very very straightforward and very very easy. So another thing that you have to observe carefully is let's say I will nest the object now. Okay? First name, last name and address. Okay? Address I have first line first line of address basically.

### 00:08:33 · Speaker 1

okay? Then second line of address. okay? So as all of you know, at least most of you know, I stay in Bengaluru. okay? So where let me add like second line as Bengaluru. First line as like Bengaluru, maybe I'll just mention some random area that is Hebbal. okay? So now what I'll do, I'll let me add the address here. okay?

### 00:09:01 · Speaker 1

Address Line One

### 00:09:05 · Speaker 1

address line one is user details dot address dot first line okay then I have like address line two which is equals to second line fine let me go back all information are shown here now whenever I click on update let's say you updated the first name let's not touch the first name let's only decide to update the address okay address I am changing from Hebbal to let's say Marathahalli okay Will it work?

### 00:09:38 · Speaker 1

See, did not work. The reason being address is a object again, correct? So you cannot update the address itself because address itself you cannot add a value. address.firstLane you can add. So what we'll do, let us spread the address.

### 00:09:50 · Speaker 1

fine, user details dot address. In that I'm adding first line as Marathalli. Okay. So now you just spread the user details dot address and the first line was Hebbal and you are opting to update it to Marathalli. Refreshing. Update. Everything is gone. Okay. Even this is a mistake not done like by miss but done very cautiously so that you don't make this mistake. Okay. See basically you are trying to spread user details dot address this particular object.

### 00:10:20 · Speaker 1

and you're trying to update the first line. And the remaining things whatever you are doing, that is everything is actually the entire object value itself is getting lost. So what is the right way to do? So spread the user details. So now you have user info and inside this you will again spread

### 00:10:36 · Speaker 1

address, okay, you will again spread user details dot address, okay?

### 00:10:43 · Speaker 1

Then inside this, okay, user details dot address you will spread again, okay? And inside that you are gonna change the first line to something else like I said, Maratha Halli, okay?

### 00:10:58 · Speaker 1

Now if I go back to screen, see only the that particular thing got updated. Let me walk you through again what I did. So I first took a spread the user details. So everything inside user details was copied, okay? Then I decided to update only the address part, okay? So inside address, again I'm spreading just the address part, user details dot address. Then I'm changing the only the first line, okay? So I modified technically the only the first line in the entire thing. So Vasanth, this seems very clumsy. There's so many things that you did.

### 00:11:28 · Speaker 1

is there a simple workaround? If the object length is very small, okay? Then what you can do is, you can actually make a copy of the object, like const copy copy user details, okay? is equals to

### 00:11:45 · Speaker 1

you can assign it to user details. Okay, whatever the value you can assign, okay? Then what you can do is, so generally as sometimes the references remain as it is, you can use something clone deep or you can also use this hack of JSON.parse and JSON.stringify. What happens otherwise is the user details will copy user details and user details will point to the same memory locations to avoid that we are doing this, okay? Then you can do what you can do is copy user details.address.

### 00:12:15 · Speaker 1

first line is equals to Marathahalli, okay? Marathahalli. If you are someone from Marathahalli from Bengaluru, please comment or if you are from Hebbal also please mention that in the comment section, okay? Then you just update this with the this value. Copy user details, okay? Let me refresh. Hebbal update Marathahalli, okay? So very straightforward process. Personally, I like the second approach than the first approach because that looks a little bit clumsy for me. But again, always you can

### 00:12:45 · Speaker 1

do this because if so that's times when object length will be very big. Okay? In such scenarios copying again adds additional additional space consumption. Okay? But for simple objects like this, this is the best approach that I would recommend. Okay? Now, once the objects are done, deeply nested object also I've understood. Now, can you speak something about the array? Since we have already crossed around twelve minutes, I'm not gonna explain about the array in this video. Please mention in the comment section you want a separate video on that. But here is the link where you can get a complete understanding about how to modify the array in in array.

### 00:13:15 · Speaker 1

and array of object in ReactJs, but it's almost straightforward like the way I mentioned about the objects. Only difference here is they would use the array operations for modifying the array. One last question before signing off.

### 00:13:28 · Speaker 1

there are no nested objects in JavaScript. Okay? So though on the screen you would see a nested object, while processing there are no nested objects in JavaScript. So it is clearly explained in one of these links. I'm going to attach the link in the description section. Please read and comment why there are no nested objects in JavaScript. Thank you so much for watching. If you're not subscribed to my channel Uncommon Geeks, please subscribe to my channel, like the video, comment about the video, whatever you whatever you felt, share with your friends so that they also get benefited. Thank you so much for watching. Catch you in next video.
