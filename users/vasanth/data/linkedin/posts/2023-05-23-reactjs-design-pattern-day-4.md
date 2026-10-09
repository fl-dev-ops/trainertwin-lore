---
id: '7066642382842179585'
date: '2023-05-23T05:13:55.936Z'
url: https://www.linkedin.com/posts/careerwithvasanth_reactjs-javascript-interview-activity-7066642382842179585-PX1a
likes: 123
comments: 10
videoUrl: https://dms.licdn.com/playlist/vid/v2/D5605AQHGv383kk2Cgg/mp4-720p-30fp-crf28/mp4-720p-30fp-crf28/0/1684818835243?e=1792173600&v=beta&t=4fQ7U3uTkdGvlgROHhqjDuwrGwIH3LcSeU8XPhFkBJQ
---

ReactJS design pattern day 4: Container/Presentational Pattern

Question 1: 
Let's say you have a requirement where you will build an application in Angular and later you may have to convert it to #reactjs or other #javascript framework!! How will you architect the product ??

Answer:
With my experience of asking this question, most people don't give a solid answer to this. The most compact answer for this is, dividing business logic from presentation. So that the logic can be reused and the only change required in the new platform is presentation. 

Example: If you have to render 10 dog images on the screen and you create a component and make an API call and render it. Instead of that, you have to create a  container component and nest this component inside that. The only responsibility of the child component is to render whatever the image passed to it. The logic to make API calls and get the image URL will be in the parent container component. 
So that, tomorrow if you have to change the architecture/framework, most part of the child and parent can be reused. 

Let me know, do you think this pattern is useful in application development or not ??

In case if you have not followed me, you can do it here, I will help you to clear your Software developer interview : Vasanth Bhat

#interview #react #design #reactjs #softwaredeveloper #frontendwebdeveloper #frontenddevelopment #systemdesign #management #architecture #development
