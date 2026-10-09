---
id: bb766097ac05
title: Prototype and Protypal Inheritance in JavaScript
url: https://careerwithvasanth.medium.com/prototype-and-protypal-inheritance-in-javascript-bb766097ac05
date: 2022-05-29
author: Vasanth Bhat
platform: medium


---

# Prototype and Protypal Inheritance in JavaScript

![](https://miro.medium.com/v2/resize:fit:700/0*vAaau9Y43RBhyw2I.png)

Personally I’m from Java Background, my view towards the Inheritance was totally different then the JavaScript Inheritance. For a beginner, concept of Inheritance in JavaScript is quite tricky to understand. The purpose of this article is to elaborate all aspects of Inheritance in JavaScript step by step, so stay with me.

**What is Inheritance ?**

Inheritance in Object Oriented Programming language is a mechanism in which base class acquires all the properties and behaviors of the parent class. It is an important part of OOPs (Object Oriented programming system). The idea behind inheritance in Java is that you can create new classes that are built upon existing classes. When you inherit from an existing class, you can reuse methods and fields of the parent class.

In very simple words the class that inherits another class can use functions and variables of the inherited class. Rather creating the same methods repeatedly we can use the concept of inheritance.

**What is Inheritance in JavaScript ?**

Before knowing what is Inheritance in JavaScript read my article on [how everything is Object in JavaScrip](https://mevasanth.medium.com/how-everything-is-object-in-javascript-a4164d7e6a2d) t. It gives a base for what is \_\_proto\_\_ how it is bound to various programming constraints like Array, object etc in JavaScript.

So After reading that article you must have understood how JavaScript adds \_\_proto\_\_ object to different programming constraints.

Just for demo purpose attaching the same image used in my previous article.

![](https://miro.medium.com/v2/resize:fit:700/0*C1xw5xjul8gZS_rA.png)

As you notice here, we have just created an array and it has access to all the methods of array like map, join, concat etc. All these methods are added by JavaScript engine to the Array variable.

**So every array in JavaScript will get the same set of methods and properties attached to it. Now a light should on in your mind, every array getting same method means, all of them inherit properties from the _Array.Prototype, all function inherit properties from Function.Prototype_. _This is inheritance in JavaScript._**

**Whenever user creates a function, array, Object etc, in JavaScript it will get access to all the prototype methods or it inherits those methods. This is known as inheritance in JavaScript.**

Let me illustrate a quick example to understand it better.

```
let userOneObject = {
    name: "User 1",
    city: "Singapore",
    getTitle : function(){
        console.log(this.name + " is from " + this.city )
    }
}userOneObject.getTitle() // Output will be "User 1 is from Singapore"
```

As mentioned above the output of the above snippet will be

> User 1 is from Singapore

Now let us create another object as shown below.

```
let userOneObject = {
    name: "User 1",
    city: "Singapore",
    getTitle : function(){
        console.log(this.name + " is from " + this.city )
    }
}let userTwoObject = {
    name : "User2"
}userTwoObject.getTitle()// we will get reference error as userTwoObject is not aware of getTitle method
```

The output of above code will be, reference error, userTwoObject is not aware of getTitle method

**Now let us make an interesting stuff, which you should never do in your day to day programming,**

```
let userOneObject = {
    name: "User 1",
    city: "Singapore",
    getTitle : function(){
        console.log(this.name + " is from " + this.city )
    }
}let userTwoObject = {
    name : "User2"
}userTwoObject.__proto__ = userOneObject;userTwoObject.getTitle() // Output will be User2 is from Singapore
```

Can you guess the output now ? it will be

> User2 is from Singapore

Observe it carefully. In the output this.name has value **User2** but the city value is **Singapore**. That means, since userOneObject’s proto is assigned to userTwoObject, now userTwoObject has access all methods of the userOneObject.

**The hierarchy would be, first the JavaScript engine look for the reference in the object’s declared methods(Ex:** getTitle inside the object **) if it doesn’t find it there, then it will search it in it’s \_\_proto\_\_ object. If it doesn’t find even there then it will look if \_\_proto\_\_ has any \_\_proto\_\_ object if there is, then it searches there and this process continues until it \_\_proto\_\_ is undefined.**

Does it sound like inheritance now ?

This is the same way how inheritance works in Java/C# or any other object oriented programming language. So, though JavaScript uses prototype for the purpose of inheritance, the final implementation is relatable with other programming language.

**Can we implement OOP inheritance the same way as Java in JavaScript ?**

Answer is yes. Though many doesn’t use class keyword in JavaScript you should know that after ES6 one can create class in JavaScript using the **class** keyword. Below is the example snippet of same

```
class BaseClass {
    displayBaseClassName(){
        console.log("This is Base class")
    }
}
class DerivedClass extends BaseClass {
    displayDerivedClassName(){
        console.log("This is Derived class")
    }
}let derivedClassObj = new DerivedClass();
derivedClassObj.displayBaseClassName(; //Output will be "This is Base class"
```

Here we have created two classes BaseClass and DerivedClass. And Derived class is inheriting from the BaseClass keyword **extend** is used for the purpose. Same way how you would use inheritance in Java you can use it in JavaScript with very minimum changes in creating object and functions.

Do not get confuse with the above code with Prototype inheritance. If your asked what is inheritance in JavaScript ? then they will be expecting Prototypal inheritance answer and not the second one. Good luck !!

**Related Articles**

[How everything is object in JavaScript ?](https://mevasanth.medium.com/how-everything-is-object-in-javascript-a4164d7e6a2d)
