# UCB action selection
From [[action-value methods for bandit problem]]
$\physics$
## Definition
Upper confidence bound action selection takes into account not only the mean values for each action, but also the uncertainty of their estimation. So, when exploring, it’s better to pick actions that either have close to maximum value, or have very high uncertainty. In both cases, there is a high chance of discovering new maximum.

More precisely, we pick the arm with the highest score, where score are:
$$UCB_{t}(a) = Q_{t}(a) + \sqrt{\frac{\ln t}{N_{t}(a)}}$$

## Derivation
Based on https://ieor8100.github.io/mab/Lecture%203.pdf

After we tried $a$ for $N_{t}(a)$ times, by [[Hoeffding’ inequality]] or [[central limit theorem]], we have estimaton error $\sigma \sim \sqrt\frac{1}{N_{t}(a)}$.  So by taking the second term of form $\omega(1)\sigma$ we guarantee that eventually $UCB$ for every arm will be higher than its real value with probability $1$. At the same time, because this $\omega(1) = \sqrt{\ln t}$ is not very large, it is enough to have $N_{t}(a) \sim \frac{\ln t}{d^{2}}$ to make $UCB$ smaller than $q(a) + d$.

So, if we consider a suboptimal arm with $\abs{q(a) - \max q(a)} = d$, it is enough to take it $\order{\frac{\ln t}{d^{2}}} = \order{\ln t}$ times from the first $t$ moves, to see that it is suboptimal.  