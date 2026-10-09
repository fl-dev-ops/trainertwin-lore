---
id: '7065206497495986176'
date: '2023-05-19T06:08:14.192Z'
url: https://www.linkedin.com/posts/careerwithvasanth_youtubechannel-interview-react-activity-7065206497495986176-gjjk
likes: 198
comments: 19
images_count: 1
---

ReactJS design pattern day 2: Provider Pattern (Another alternative for redux)
Question 1:
If you have passed data from Parent component A to child component D (A->B->C->D) which approach you will use ?

Answer:
Most common answer is again Redux.

Question 2:
What built in features of React are used by Redux for state management ?
Answer:
Most will not be sure about it, some will say context API's, which is the right answer.

Question 3:
Which design pattern context API/useContext hook will use ?
Answer:
99% of the time nobody ever answers this question. Right answer is the provider design pattern.

With the Provider Pattern, we can make data available to multiple components. Rather than passing that data down each layer through props, we can wrap all components in a Provider. The Provider pattern is very useful for sharing global data. A common use case for the provider pattern is sharing a theme UI state with many components (As shown in attached image).

Answer in comment section, can context API(createConext) and redux can exist in the same project at the root level (App.tsx) or not ?

In case if you have not followed me, you can do it here, I will help you to clear your Software developer interview : Vasanth Bhat
Subscribe to my #youtubechannel "uncommonGeeks" where I will discuss topics like this in detail (Link in comment section).

#interview #react #design #reactjs #softwaredeveloper #frontendwebdeveloper #frontenddevelopment #systemdesign #management
