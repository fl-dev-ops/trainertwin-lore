---
id: 71b9f3b0db20
title: How to use local Images dynamically in React Native
url: https://careerwithvasanth.medium.com/how-to-use-local-images-dynamically-in-react-native-71b9f3b0db20
date: 2020-05-16
author: Vasanth Bhat
platform: medium


---

# How to use local Images dynamically in React Native

During Corna Home arrest, I developed a puzzle/Riddle application [**BrainBite**.](https://play.google.com/store/apps/details?id=com.brainbite) While developing I came across a strange issue which I had never expected in React Native. [**Brainbite**](https://play.google.com/store/apps/details?id=com.brainbite) is a riddle applications, where initially we thought of having puzzles created in a beautiful local image and showing it one after another. We had created around 50 Images with Images named numerically in ascending order. Ex: 1.png, 2.png …50.png etc.

Coming from Angular/Ionic background there was no complexity in implementing it, where I would generally write the file path as constant and take Image name dynamically.

> **Ex: const ImageDirectory = “Resources/Images”**
>
> **const ImageName = currentIndex + “.png”**//where current Index will be 1,2 etc.
>
> **Const ImagePath = ImageDirectory + ImageName**

Since React too is Javascript framework, I was expecting something similar, with syntax change w.r.t React Native. But It was totally different.

Sample Code to display Image which are stored locally in React Native.

> <Image
>
> source={require(‘../Resources/Images/1.jpg’)}
>
> style={{ width: 400, height: 350 }}
>
> />

Consider we create a state variable named ImagePath which changes depending on the current state of the application.

> ImagePath: ‘../Resources/Images/1.jpg’ //default value

When user clicks on next button

> nextPuzzle = () => {
>
> this.state.setState({
>
> ImagePath: ‘../Resources/Images/’ + currentIndex + ‘.png’
>
> })
>
> }

In the render method

> <Image
>
> source={require(ImagePath)}
>
> style={{ width: 400, height: 350 }}
>
> />

But it failed. No Image was rendered when I call nextPuzzle event. And below error was thrown. The reason for this behavior is documented in this [link](https://reactnative.dev/docs/image.html#static-resources).

![](https://miro.medium.com/v2/resize:fit:464/0*hBmL6OiA8zcZJ2sj.png)

And If I have to summaries the reason is

**_“The only allowed way to refer to an image in the bundle is to literally write require(‘image!name-of-the-asset’) in the source.”_**

In case your thinking, what is this error message is, It means in react all the static Image path has to be specified during the compilation itself, anything specified dynamically is considered as an error. They also recommend if the number of Images that your using locally exceeds certain number, then push it to your server and refer the path in the application. That time it uses Source as URI so there is no problem in loading such data.

But your app is something similar to fine and you want to load static Images dynamically then refer below steps. Though it looks tedious, this is the only solution that worked for me.

For quick solution refer this S [tackoverflow](https://stackoverflow.com/a/61369986/7824672) link of my answer. For elaborated explanation read below.

1.  First create a folder named **Resources/Images** and place all your images there.
2.  Now create a file named **Index.js** (at Resources/Images) which is responsible for Indexing all the images in the **Reources/Images** folder. Below is the example content of Index.js file

> const Images = {
>
> ‘image1’: require(‘./1.png’),
>
> ‘image2’: require(‘./2.png’),
>
> ‘image3’: require(‘./3.png’)
>
> }

3.  Now create a Component named ImageView at your choice of folder. One can create functional, class or constant component. I have used Const component. This file is responsible for returning the Image depending on the Index.

```javascript
import React from 'react';
import { Image, Dimensions } from 'react-native';
import Images from './Index';
const ImageView = ({ index }) => {
    return (
        <Image
            source={Images['image' + index]}
        />
    )
}
export default ImageView;
```

4.  Now from the component wherever you want to render the Static Images dynamically, just use the ImageView component and pass the index.

> **< ImageView index={this.qno + 1} />**

In my example qno is the state variable that contains the current question number. And it changes when user clicks on Next and Previous button.

Hope this article is helpful, support me by giving claps and downloading the [**BrainBite**](https://play.google.com/store/apps/details?id=com.brainbite) application.
