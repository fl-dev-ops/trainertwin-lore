---
id: 20c9656b6ce8
title: Youtube — System design, MAANG interview question. How live commenting, pagination
  works on Youtube ?
url: https://careerwithvasanth.medium.com/youtube-system-design-maang-interview-question-20c9656b6ce8
date: 2022-10-21
author: Vasanth Bhat
platform: medium
---

# Youtube — System design, MAANG interview question. How live commenting, pagination works on Youtube ?

System design of Youtube is one of the most common interview questions in frontend system design interviews. Reason for that is the simplicity of Youtube, it’s extremely difficult to design a system that looks very simple. If you’re a frontend developer and don’t know what frontend system design ? I have written an introductory article [here](https://mevasanth.medium.com/what-is-frontend-system-design-what-questions-to-expect-in-the-interview-705e5c05be9) and you can read it before reading this.

As you know, it’s quite difficult to explain the entire system design over words. You can watch the video below for a detailed explanation. You can also read this article where I will explain things at a high level.

![](https://miro.medium.com/v2/resize:fit:700/1*pAzymKtBUCyMTX00Xso-0Q.png)

Fig: System design of Youtube

Let’s go through each of the different sections of frontend system design:

> **Requirements:**

Requirements consists of mainly 2 types:

1.  **Functional Requirements**: Functional requirements consist of those requirements that will directly affect the user experience.
2.  **Non-functional requirements**. Non-functional requirements consist of things that will not directly impact the user in most of the cases but are very essential from the product point of view.

Below image lists most common requirements for Youtube system.

![Requirement Imge](https://miro.medium.com/v2/resize:fit:668/1*JzZVCI-AB3QmRiUyGgiC5g.png)

> **Scoping**

After completing requirement gathering, as it is an interview with just 40 mins, you cannot build everything. Generally the interviewer picks some items that are challenging and they have good knowledge about it. Below are the items that I’m scoping.

**Videos Details Screen:**

-> Comments pagination

**Live Commenting**

> **Technology**

After requirement and scoping the next section is picking the right UI technology for building “ **Youtube**”. Which of the below technologies will you choose ?

- ReactJS
- AngularJS
- VenillaJS and HTML, CSS
- VueJS

Here there are two things before picking right technology

1.  **Organisational dependency:** Organisation might have some internal concerns. Ex: There might be a team full of reactJs developers and no Angular developer or vice versa. Because of this, though the product needs one tech you cannot choose it.

**2\. Project dependency:** To meet project needs what is the right technology ?Ideally this should have precedence over **Organisational dependency.** Coming to the example of “ **Youtube**” we can use ReactJS or AngularJS. Youtube on the other hand don’t use either of these frameworks they have an internal framework specialised for their products.

> **Component Architecture**

This step is optional, depending on the interviewer, they can ask you to create a wireframe of the design and then start the question or they can directly start asking the questions.

Below is the basic design of the Youtube video details screen.

![](https://miro.medium.com/v2/resize:fit:700/1*RTWPVmKdCT02Ln04jg0hLQ.png)

> **Problem No 1 (Discussion on Scoped Item)**

1.  **Video Player:** How to build a sophisticated video player like **Youtube ?** If I’m in the design round, my first question would be “How many days do we have to launch this product ?? ``If we had more time, then we could build the player from scratch. If not it’s advisable to purchase some already existing video players and build our own player after first or few releases. But still if you want to know how to build a video player like Youtube on your own, you can read this [blog post.](https://freshman.tech/custom-html5-video/) It’s quite easy, what Youtube uses is HTML <video> tag and mediaSource API.

> **Problem No 2(Discussion on Scoped Item)**

1.  **Comment feed:** This is an interesting problem to solve. As popular videos will have 1000’s of comments. **What is the right strategy to add the comments onto the screen ?**

One simple answer is via “ **Pagination**”. We load a few comments when the page is launched and further comments are added to the page when the user scrolls to the end. But there are two main catches here.

-   **What if already loaded comments are edited ? Will you refresh it ?**
-   **What if you have selected filters as new to old comments and when you hit the end,** technically you’re loading old comments. By then, a lot of new comments might have arrived. will surface them or not ?

There are many ways to solve this problem, considering scale of Youtube I propose below solutions:

1.  **Filter only local data:** We won’t load new comments during pagination. As popular videos opened by two people at the same time may not have the same number of comments. To get new comments it is good to refresh the page.
2.  **Load only old comments during pagination:** Same as above.
3.  **Have a special section called priority comments to refresh the existing list of comments:** There can be scenarios where certain comments can change the entire course of discussion. In such scenarios it is very essential to add those comments though it is a new comment. These priority comments can be analysed in the backend with the help of AI/ML algorithms.

> **Problem No 3( Live commenting)**

Live commenting during live video streaming seems an easy problem to solve. But actually it isn’t, let me explain why ?

1.  During live streaming of a video thousands of comments might flow in per second. To update that on the screen **what is the right strategy to fetch comments from the server ?**
2.  **How many comments do you store locally**? because live streaming videos like news channels might get lakhs of comments over a course of 30 mins, if you store all, your site might become very slow.

Let’s solve both the problems.

1.  Right strategy to fetch live comments from the server is via **Polling.** Every **X** seconds trigger the backend to get the new set of comments. This **X** is determined by AI/ML by observing the stream over a course of time. Ex: For news channel **X** might be small and for a nature video **X** might be large.
2.  We don’t have to store all the comments locally. It is good to have a fixed size comment array and replace old comments with new whenever it arrives. Because most users, will not have time to go back and read all the comments. Again how many comments to store can be fixed or determined by AI/ML.

**You have to watch my above Youtube video to know how live streaming works**

## Closing notes

1.  Frontend system design doesn’t involve any coding.
2.  It only involves giving a system how you will design it from scratch.
3.  You don’t have to know what system you are using. Ex: Amazon might be using ReactJS for their e-commerce website and you propose to build Amazon in Angular, there is no problem with that. **You’re not cloning the product, you’re designing it from scratch.**
4.  Pick the systems that you use every day and try to design with the above-mentioned sections.

Thank you for reading catch you in the next article. In case you have not already followed me on Medium then please follow, you can follow me on Linked [here](https://www.linkedin.com/in/vasanth-bhat-4180909b/). Do not forget to subscribe to my YouTube Channel [UncommonGeeks](https://www.youtube.com/channel/UCSCNvSCk_Z9mBvUM-FJexRg/videos).

Feel free to add your feedback in the comment section.

In case if you want to talk to me personally for mock interview, tips and tricks to clear interview or resume review, you can book a session here:

[https://topmate.io/vasanth\_bhat](https://topmate.io/vasanth_bhat)

If your a reactJS developer and looking for interview preparation, watch my complete interview preparation guide here:

If you’re preparing for a frontend developer interview, please watch the below series of mine:
