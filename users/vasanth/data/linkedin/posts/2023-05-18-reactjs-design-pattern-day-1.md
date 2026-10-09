---
id: '7064830288471756800'
date: '2023-05-18T05:13:18.971Z'
url: https://www.linkedin.com/posts/careerwithvasanth_interview-design-data-activity-7064830288471756800-HQ8b
likes: 216
comments: 22
images_count: 1
---

ReactJS design pattern day 1: Singleton
Question 1:
If some data needs to be shared between two pages how will you pass it.
Answer :
99% of people will answer is as Redux.

Question 2:
Is there any other way ??
Answer:
We can use navigation params or local storage.

Very rarely I have heard someone saying we can use singleton patterns. Whenever you need to share data between 2 components, you need not use redux. If real time update of data (or re-rendering) is not required then you can use a singleton pattern like shown in the attached image. You change data from one page and it will be updated in the other also.

Let me know what is the use of Object.freeze which is used in the snippet in the comment section. 

Follow me and I will help you to clear your software developer interview: Vasanth Bhat

#interview #design #data #reactjs #reduxtoolkit #redux #frontendwebdeveloper #systemdesign #softwaredeveloper
