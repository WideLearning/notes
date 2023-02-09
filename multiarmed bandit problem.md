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