---
id: '7160862956350492673'
date: '2024-02-07T05:12:51.194Z'
url: https://www.linkedin.com/posts/careerwithvasanth_frontenddevelopment-frontenddeveloper-frontenddev-activity-7160862956350492673-fItL
likes: 124
comments: 9
videoUrl: https://dms.licdn.com/playlist/vid/v2/D5605AQE8AJvwzk4Guw/mp4-720p-30fp-crf28/mp4-720p-30fp-crf28/0/1707282773843?e=1792173600&v=beta&t=7GNMm6iUbL_i8Mx-p0Qe51n4LcSpEaMZgnYxq9HTHAA
---

Let's discuss a popular React JS / React Native machine coding question today. 

Question: 
Build a traffic light where the lights switch from green to yellow to red after predetermined intervals and loop indefinitely. Each light should be lit for the following durations:
Red light: 4000ms
Yellow light: 500ms
Green light: 3000ms
You are free to exercise your creativity to style the appearance of the traffic light.

Solution: Considering the space constraint I'm just adding the crux of the logic here. 

 / ************************************************************************/
const config = {
  red: {
    backgroundColor: 'red',
    duration: 4000,
    next: 'green',
  },
  yellow: {
    backgroundColor: 'yellow',
    duration: 500,
    next: 'red',
  },
  green: {
    backgroundColor: 'green',
    duration: 3000,
    next: 'yellow',
  },
};

 / ************************************************************************/
 const [currentColor, setCurrentColor] =
    useState(initialColor);

  useEffect(() => {
    const { duration, next } = config[currentColor];
    const timerId = setTimeout(() => {
      setCurrentColor(next);
    }, duration);
    return () => {
      clearTimeout(timerId);
    };
  }, [currentColor]);
 / ************************************************************************/
Follow me and I will help you to master #frontenddevelopment : Vasanth Bhat

#frontenddeveloper #frontenddev #uidevelopment #reactjs #react #reactdevelopers #uidesignpatterns
