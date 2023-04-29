# n-step off-policy learning with importance sampling
From [[temporal-difference learning]]
$\physics$
## Definition
It is a generalization of [[Q-learning]] and [[expected SARSA]] to [[n-step TD prediction]].

As in [[Monte Carlo methods]], [[per-decision importance sampling]] and [[discounting-aware importance sampling]] can be used here to reduce variance. But due to bootstrapping nature of the algorithm, here we can use [[per-decision importance sampling with control variates]].

## See also
- [[n-step tree backup]] doesn’t use importance sampling at all.
