# dynamic programming methods
From [[reinforcement learning]]
$\physics$
Main idea here is to use already (partially) computed values to accelerate computation of other values. For example, to estimate value function, we don’t calculate expectation over all possible future sequences of moves, we just take expectation over the first move, and then take the value function of state where we get after it.

- [[policy evaluation]]
- [[policy improvement]]
- [[policy iteration]]
- [[value iteration]]