---
id: '6991266065687224320'
date: '2022-10-27T05:15:21.502Z'
url: https://www.linkedin.com/posts/careerwithvasanth_reactjs-javascript-reactjs-activity-6991266065687224320-dMyR
likes: 172
comments: 3
images_count: 1
---

#reactjs #javascript Most of the modern applications interact with one or the other third party services. Ex: Message gateway, Payment gateway, notification gateway etc. It's very essential to store their API keys before invoking their service. But there are many security problems associated with storing keys at client side. Here are my tips for storing the keys securely.

1. Never store API keys in some random typescript/javascript file.
2. Good approach is to store it in a .env file and access it wherever required. Problem with this approach is that even this file is part of the bundle and the attacker can get access to it by inspecting the code. 
3.  Better approach is to use an orchestration layer at the backend. Ex: Client doesn't store any API keys and they will invoke the intermediate backend which will in turn invoke the actual backend. Because of this, clients need not to store any confidential information locally. 

Share your thoughts if you know any other better approach. 

In case if you have not followed me, you can do it here, I will help you to clear your Software developer interview : Vasanth Bhat
To discuss more about frontend interview preparation, strategies, tips and tricks, you can join UncommonGeeks telegram channel here: http://t.me/uncommongeek

#reactjs #security #javascript #frontend #frontenddeveloper #api #apitesting #frontenddevelopment
