---
id: d921d8b34584
title: The Art of writing Bug free code. As per research 70% of the work in the…
url: https://careerwithvasanth.medium.com/the-art-of-writing-bug-free-code-d921d8b34584
date: 2023-03-13
author: Vasanth Bhat
platform: medium


---

# The Art of writing Bug free code

As per research 70% of the work in the IT industry is bug fixing. If this percentage is reduced to less than 50% then overall efficiency of every organisation will improve. Some of these bugs will be from production, preventing them, will save a significant amount of money for any company.

Below are a list of guidelines that I took and reduced the bugs in my code significantly. Listing it down here, so that it can help you also.

![](https://miro.medium.com/v2/resize:fit:700/1*i7lnbMtsgrooExiQkrhYEw.png)

Source: techindustan

> **Planning the stories before starting of the sprint:**

If you planned well for the sprint then half of your work is already over. Most product companies due to their regular heavy workload, do not emphasise more on Sprint and proper planning of it. Majority of the companies don’t have a sprint planning meeting. Which is essential to analyse each story and its scope properly. Because of this, many times after picking the story, Engineers realise the requirement is not clear.

Below are the steps that you can take:

1. Though your team is not strictly following spring planning. You can create your stories before the sprint and analyse it in detail and ask questions from the PM and other stakeholders if required to be clear about all the work that you’re taking.
2. If the above step is not possible, (Assuming somebody else creates stories for you) spend day 1 of your sprint to analyse all the stories. If something is not clear, get proper clarity from stakeholders and update acceptance criteria of the story accordingly. This will ensure, no story is blocked in the middle of the sprint.

> **Writing the implementation steps in detail**

This is something that I learnt from my CTO in my first company. Most developers start developing things once after the requirement is clear. **No, that’s not the right way to code.** Most of the time requirement will be clear but you’re not sure which all modules your code will impact, how to handle all the edge cases. So, my advice is, though the story looks straightforward, write down the implementation steps.

Ex: You want to create a login screen UI will email id and password and login button.

Here are sample implementation steps of this story:

1. First I will create 2 text boxes that will take the user email id and password.
2. The Maximum character that email id can take is 50 and minimum is 10.
3. The Maximum character that password can take is 12 and minimum is 6
4. Password field should be secure (Shown as \*\*\* on screen).
5. If the user enters invalid email id and focuses outside the email id textbox, give a red border to the input text box and show an error message below the input text box “Invalid email id” .
6. And it goes on.

I can write at-least 10 more steps for this simple requirement. By writing each of these steps in some notes application and cross checking them after completion, ensures your code is covering most of the requirements.

> **Doing TDD (Test driven development) if your organisation permits**

One of my favourite software development methods is TDD. For people who have never heard of it, don’t worry. It’s straight forward, before starting the development, QA/Tester will give you the list of test cases that your story should accomplish. You will start your implementation in such a way that all these test cases are satisfied. If you strictly follow this step along with writing “the implementation steps in detail” 90% of the time your code will work as expected.

In case your organisation is not in favour of TDD, here is what you can do.

1. Set up a meeting with a QA/Tester at the start of every sprint. Where you will explain the feature that you’re developing.
2. Your QA will tell all the possible tests that they would perform w.r.t that story. You can note down all and ensure all of them are covered during your implementation.

> **Proper dev-testing**

Let’s accept guys, “Developers sometimes have immense confidence over the code that they have written”. Because of this, a lot of developers just test the code for the happy paths and some common error scenario’s and merge their changes. Later when QA starts testing the code they will identify a lot of issues, which could have been addressed by the developer, if they have spent some time properly doing the dev testing.

After writing the proper implementation steps for the story, make sure all of those steps are verified which can ensure a lot of possible bugs are addressed.

> Don’t write unit testing to increase the coverage

Last and very important step is that most developers write unit testing to meet the threshold percentage. Because of this, many times all the cases will not be covered. So, don’t write unit testing just to increase the code coverage but also to ensure all the possible cases are covered as expected.

Being honest, by following the above steps will not reduce bugs to Zero. But, just follow these steps for at least 90 days and you start realising that you have become a better programmer than before and bugs in your code have reduced significantly.

Please share any other steps that helped you to reduce your bugs in the comment section.

Follow me on Medium for more interesting articles !! catch you in the next one.
