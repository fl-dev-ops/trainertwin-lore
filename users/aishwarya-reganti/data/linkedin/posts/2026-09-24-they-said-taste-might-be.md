---
id: '7508903199974621184'
date: '2026-09-24T15:00:31.549Z'
url: https://www.linkedin.com/posts/areganti_they-said-taste-might-be-the-only-thing-left-activity-7508903199974621184-qdiL
likes: 37
comments: 3
images_count: 1
---

They said taste might be the only thing left for humans in the age of AI. Apparently, agents are coming for that too. 😅

This paper introduces Taste-Bench, which measures whether an agent can choose the better direction at a decision point before seeing how either path turns out.

The researchers call this ability “taste.”

To build the benchmark, they looked for decision forks in long agent trajectories. Some came from multiple attempts that took different approaches, while others came from runs where an agent followed a poor direction, hit a wall, and later recovered.

The trajectory is stopped at that exact point, and another model has to choose which direction is more likely to succeed.

A few findings:

- The best model scored 59.7%. Each question was shown twice with the answer positions reversed, and the model had to get both versions right.
- When the information needed to make the decision appeared much later in the trajectory, average accuracy dropped from 62.3% to 21%.
- Giving models more reasoning tokens did not meaningfully improve the results for the 2 models tested.

I really like the way the authors define taste here: through the intermediate decisions that eventually lead to a good result.

It makes me wonder whether taste can be codified too. This paper gives us one way to do it: capture important decision points, observe which direction eventually worked, and train models to recognize similar choices.

Who knows? Maybe humans aren’t that special after all. What a world to be living in. 😅

Paper: https://lnkd.in/gxwqt4pw
