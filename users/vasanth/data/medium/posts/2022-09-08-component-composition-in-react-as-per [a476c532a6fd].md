---
id: a476c532a6fd
title: Component Composition in React. As per React’s official documentation…
url: https://mevasanth.medium.com/component-composition-in-react-a476c532a6fd
date: 2022-09-08
author: Vasanth Bhat
platform: medium
---

# Component Composition in React

![](https://miro.medium.com/v2/resize:fit:700/0*n2Djui_oqO-2pWiK)

Photo by [Ferenc Almasi](https://unsplash.com/@flowforfrank?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

As per React’s official [documentation](https://reactjs.org/docs/composition-vs-inheritance.html), _“Some components don’t know their children ahead of time. This is especially common for components like_`Sidebar` _or_`Dialog` _that represent generic “boxes”. We recommend that such components can use the special_`children` _prop to pass children elements directly into their output.”_

Also, when you’re working on big projects, there will be scenarios where multiple teams are working on the same project and one team wants to show their UI on some other team’s page and this could be dynamic. In such scenarios, you may have to use React’s component composition.

### **Let’s get into a scenario:**

_Let’s take an example where you’re working for a news application. Initially, all news was handled by one team. The news heading was shown in a card format with the title in it. Later, your app became very popular and for every section of news, ex: Films, Sports, Business, there are different teams and there are different types of cards._

![](https://miro.medium.com/v2/resize:fit:700/1*b91rSVR_J8sBnIRt4nFrfQ.png)

1. Now you want to create a card container in such a way that any team can plug their cards into your container.
2. Apart from following some main guidelines applied by you to render the cards, each team should have the freedom to implement certain functionalities of their own. For example, which API to call on the click of the news card, when to make it read or unread etc.

### **Solution**

### **Approach 1**

Every time when new team comes up with a card, you sit with them and understand their functionality and implement cards for them and use it in the container.

**Cons:**

1. Not a scalable approach, in future when number of teams increases, it will increase the work load on one single team.
2. Also, when your application starts to aggregate news from third party vendors, there has to be a way where dynamic news cards can be inserted into application.

### **Approach 2**

Same as the title of article, using component composition.

**Step1: Prepare a generic news body that you need to receive from API which will contain news details and type of news.**

For simplicity of the explanation I’m considering below sample response.

```
[{type: ‘SPORTS’,title: ‘It was a great match yesterday’….},{type: ‘BUSINESS’,title: ‘Market has reached new heights,’….}]
```

**Step 2: Create a container component which can pass props to all the children props**

Container component responsibility is to just render the children component and make all props passed to parent accessible to children component. For this to happen, we are using the context approach. If you’re not aware what is the use of createContext/useContext, refer to the official documentation [here](https://reactjs.org/docs/hooks-reference.html#usecontext). In simple words, useContext will help you to pass properties from parent component to child component without using prop drilling.

For example, let’s say Component A has child Component B and B has Child C. From A, if we have to pass some props to C, one way is passing it to B and from there passing it to C. Or by using useContext, which will make parents props available to all the children components.

```
import React from 'react';const NewsContext = React.createContext({});
// This is responsible for exposing all the props available for
// NewsContainer to children componentsexport function useNews() {   const context = React.useContext(NewsContext);   if (context === undefined) {      throw new Error('useNews must be used within a <NewsContainer   />');   }return context;}// This will render all the children passed to it.export default function NewsContainer(props) {    const {children} = props;    return (        <NewsContext.Provider value={{...props}}>
           {children}
       </NewsContext.Provider>    );}
```

**Step 3: Create News title component**

Here you have to create news title component and you will be styling all the known news type titles. This component will be exposed like a shared library. So that, any team can use it to build their news card.

**Refer example below**

```
import React from 'react';
import {Text, StyleSheet} from 'react-native';import useNews from './NewsContainer';
export default function NewsTitle({children}) {const {title, type} = useNews();
const getNewsTitle = () => {     switch(type){          case 'SPORTS':
               return (                  <Text style={styles.sports}>{title}</Text>                 )
          case 'BUSINESS':
               return (                 <Text style={styles.business}>{title}</Text>                )         }}return (<View>         {children && children}         {!children && getNewsTitle()}</View>);}const styles = StyleSheet.create({
sports:{
color : 'red' },
business:{
color : 'green'
}})
```

**Step 4: Create custom news cards**

By using the NewsTitle and NewsContainer components that were created in the above step. Now all the teams can create cards of their choice without your help.

**For example:** Let’s create business news card

```
import React from 'react';import NewsContainer from './NewsContainer';
import NewsTitle from './NewsTitle';export default function BusinessNewsCard(props) {
return (<NewsContainer {...props}>
      <NewsTitle />
</NewsContainer>)
}
```

In the above example, I have considered just the title component. **_In a real-world example, there could be some buttons on the left or right side or there could be some highlighter, etc. You can create all of them separately and use them inside News cards to create your custom card_**. If one news has left button and one doesn’t, they can configure it accordingly.

**Step 4a: Giving freedom to other teams to build their own cards**

In **Step 3,** observe the render portion if there are any children then we are rendering the children as it is, if not, we are showing the default components. If any news team decides not to use the NewsTitle which is already created then they can pass their children inside NewsTitle as shown in the below example.

```
import React from 'react';
import {Text} from 'react-native'import NewsContainer from './NewsContainer';
import NewsTitle from './NewsTitle';export default function BusinessNewsCard(props) {
return (<NewsContainer {...props}>
      <NewsTitle >
             <Text>Custom Business title</Text>
      </NewsTitle>
</NewsContainer>)
}
```

Now in NewsTitle component ‘Custom Business title’ will be rendered. By this approach, you're giving absolute freedom to other teams to use the style and components of their choice.

**Step 5: The parent component creation**

So far, you have created all children components which work on the props passed. Now as a developer who creates container component, you are responsible for making API call and getting the data and showing these cards inside the container.

```
import React, {useState} from 'react';
import BusinessNewsCard './BusinessNewsCard'
export default function NewsDashboard(){const [response, setResponse] = useState([]);// Write your logic to get data from APIreturn (
    {
         response.map(newsItem => {             if(newsItem.type === 'BUSINESS'){
               return (                  <BusinessNewsCard props={newsItem}>
               )             }            else if(newsItem.type === 'SPORTS'){
               return (                    // ... custom sports card
               )
         })    }
)}
```

In the future, if any new type of news comes or any new team wants to integrate their news into the app, then they just create their news card and keep a check inside NewsDashboard and render their component. This example can be extended to call methods on click of buttons or methods on click of news card, etc.

Happy reading!

### Further Reading

[**Extracting and Reusing Pre-existing Components using bit add** \\
\\
**Finally, you completed the task of creating a fantastic input field for the Input in your app. You are happy with the…**\\
\\
bit.cloud](https://bit.cloud/blog/-extracting-and-reusing-pre-existing-components-using-bit-add-l28qlxpz?source=post_page-----a476c532a6fd-----------------------------------------)

_More content at_ [**_PlainEnglish.io_**](https://plainenglish.io/) _. Sign up for our_ [**_free weekly newsletter_**](http://newsletter.plainenglish.io/) _. Follow us on_ [**_Twitter_**](https://twitter.com/inPlainEngHQ), [**_LinkedIn_**](https://www.linkedin.com/company/inplainenglish/) **_,_** [**_YouTube_**](https://www.youtube.com/channel/UCtipWUghju290NWcn8jhyAw) **_, and_** [**_Discord_**](https://discord.gg/GtDtUAvyhW) **_._** _Interested in Growth Hacking? Check out_ [**_Circuit_**](https://circuit.ooo/) **_._**
