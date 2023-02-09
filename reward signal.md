# reward signal
From [[reinforcement learning]]
$\physics$
## Definition
It is a number receivevd from environment that specifies how “good” the last action was (in the context of the last state, of course). The goal of reinforcement learning is to find a [[policy]] that gives the best sum of reward signals in the long run.

## Interesting fact
The policy itself, even optimal one, is not necessarily trying to optimize reward. An exaggerated example: consider [[multiarmed bandit problem]] with a twist where the action that had the lowest mean reward on all previous steps gives a very high reward on the last step. Here the optimal policy would be to use other actions at first, but then, for no apparent reason, switch to this underdog on the last step.