# Dyna-Q+
From [[model-based methods]]
$\physics$
## Definition
It is an extension of [[Dyna-Q]] with something similar to [[UCB action selection]]: for each state-action pair we maintain the number of steps $\tau$ since it was last used and during planning add $\kappa\sqrt{\tau}$ to the rewards predicted by the model, for some small $\kappa$. In contrast to [[epsilong-greedy action selection]], it can motivate the agent to undertake a long sequence of actions deliberately, to explore a specific state-action pair.

Note that planning is essential for [[UCB action selection]]. If we just take a [[Q-learning]] and add $\kappa\sqrt{\tau}$ to the rewards, it will, perhaps, result in a weaker exploration. Consider a situation where there is a path with a medium reward, then there is a neighborhood of it where the reward is lower and the agent knows it well, but then there is an unexplored zone beyond this neighborhood, where the reward might be actually higher. With planninng, agent would propagate this uncertainty in form of the exploration bonuses all the way to the current path and then would start exploring those far areas. But with $\varepsilon$-greedy learning it will only occasionally try to go a bit off the path, then don’t see any improvements and greedily come back.