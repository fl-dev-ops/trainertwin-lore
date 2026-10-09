---
id: 37194ffca3f8
title: Ionic — How to Obfuscate your code
url: https://careerwithvasanth.medium.com/ionic-how-to-obfuscate-your-code-37194ffca3f8
date: 2021-02-28
author: Vasanth Bhat
platform: medium


---

# Ionic — How to Obfuscate your code

Wikipedia definition of obfuscation is

“In software development, obfuscation is the deliberate act of creating source or machine code that is difficult for humans to understand. Like obfuscation in natural language, it may use needlessly roundabout expressions to compose statements.”

![](https://miro.medium.com/v2/resize:fit:700/1*E1ioMvhxv605YxHpN1agnQ.jpeg)

Pre-requisites for this article

1. Basic knowledge on Mobile application development.
2. How to Generate executables in Android.
3. Basics knowledge on Mobile Application development using Ionic.

Note: For this article, I’m not using iOS executable(ipa). As it is generally difficult to get the iOS executable, unless you jail break iOS device. It is less vulnerable to attack compared to Android Applications.

Let’s start with a simple example,

1. goto this link and download [WhatsApp apk.](https://apkpure.com/whatsapp-messenger/com.whatsapp) After downloading, rename the extension of the file to .zip forcefully (whatsApp.apk to whatsApp.zip). If the OS gives a prompt are you sure ? then click ok.
2. Now extract the zip, you will be able to see many project files of the WhatsApp. For ex: the resource files that are used, some configuration xml and properties files you can see.
3. Most important you won’t be able to get any of the Java/Kotlin code that is written by WhatsApp and shipped with the product. The reason is pretty obvious during compilation the human readable code gets converted to byte code. So, even if you find some code after extracting the zip that will not be human readable.

So we can conclude that Whatsapp has obfuscated their code, easily we cannot de-code it and get information (Obviously there are some ways using hacking, there are python scripts are available to get the code. It’s not very easy to achieve, but doable.)

Now let’s check the same with Ionic Application. I’m not referring to any applications from the store, as we will not be sure, weather the manufacturer has obfuscated it or not, we have to download and check. So I’m keeping options open to you, build Android application in your Ionic Application. It could be signed or debug apk.

```
ionic cordova build android (Command to build debug apk if your using Ionic and Cordova )
```

Now do the same process as above, take the apk, forcefully rename it to .zip and extract it. Inside assets folder goto www folder, here you would see all your javascript file in minimised version. For example, if you have a typescript file named login.ts you would see login-login-module-es2015.js file which contains all the logic that you have written, not in the same format, but one with basic knowledge of JavaScript can easily decrypt and understand the logic.

**How to obfuscate code in Ionic**

I have personally tried all the free approaches available like

1. Shipping .aab instead of apk
2. Using cordova plugins that obfuscate

But none of them really help. The solution has to be paid.

The best known approach that most people use is

1. [JScrambler](https://blog.jscrambler.com/protecting-hybrid-mobile-apps-with-ionic-and-jscrambler/) (Their official article to work with Ionic is attached with this email, which I have used and recommend.).
2. [Jasob](http://jasob.com/) (I haven’t used it, but many recommend this tool.)

**Downside of code obfuscation**

Every technique to improve the performance or increase security comes at a cost of complexity, either it would make readability of code very difficult or affect the performance.

In case of code obfuscation, when the paid tools has to convert the code into human unreadable format, basically what they do is, convert function name, variables and other programming constraints into some encrypted format. And makes= a simple function call into 2–3 steps nested etc. Which reduces the performance of the application, as additional overhead is involved in execution.

**When it is required to obfuscate your code ??**

1. If your application is related to Financial domain or involving the payment gateways.
2. If your application is related to Healthcare domain and your expected to meet medical standards of various countries.
3. When your organisation has multiple applications and all of them share data from some common place locally, in that case, even if one application is security intensive, obfuscate other less security intensive apps also.

**When not to use code obfuscation ??**

1. If you doing basic CRED operation in your application.
2. If your application doesn’t demand great security.

It is your API’s which has to be secured heavily not the mobile application, somehow or the other hackers can get access to the client side code. Happy coding.
