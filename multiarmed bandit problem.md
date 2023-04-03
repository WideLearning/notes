# multiarmed bandit problem
From [[reinforcement learning]]
$\physics$
## Definition
It is a simplified version of general RL task, because it removes temporal dependencies. There is only one state and $k$ actions. So the problem is, in some sense, to find the best option (explore) and then use it as much as possible (exploit).

## Notation
- $A_{t}$ — action on step $t$.
- $R_{t}$ — reward on step $t$ (that is, after $A_t$)
- $q(a) = \mathbb{E}(R_{t} \mid A_{t} = a)$
- $Q_{t}(a)$ — estimate of $q(a)$ on step $t$
- $N_{t}(a) = \sum\limits_{i \in [t]} [A_{t} = a]$
- $\pi_{t}(a) = P(A_{t} = a)$
- $H_{t}(a)$ — preference for action $a$ on step $t$

## Methods
- [[action-value methods for bandit problem]]
- [[gradient methods for bandit problem]]

## Comptarison
See [WideLearning](https://github.com/WideLearning/RL) for more recent information.
![greedy](https://raw.githubusercontent.com/WideLearning/RL/main/images/greedy.svg)
![eps_greedy](https://raw.githubusercontent.com/WideLearning/RL/main/images/eps_greedy.svg)
![ucb](https://raw.githubusercontent.com/WideLearning/RL/main/images/ucb.svg)
![optimal](https://raw.githubusercontent.com/WideLearning/RL/main/images/optimal.svg)
![gradient](https://raw.githubusercontent.com/WideLearning/RL/main/images/gradient.svg)
![gradient_biased](https://raw.githubusercontent.com/WideLearning/RL/main/images/gradient_biased.svg)
![optimal_gradient](https://raw.githubusercontent.com/WideLearning/RL/main/images/optimal_gradient.svg)