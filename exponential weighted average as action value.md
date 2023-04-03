# exponential weighted average as action value
From [[action-value methods for bandit problem]]
$\physics$
## Definition
In incremental way:$$Q_{t}(a) = \begin{cases}
Q_{t-1}(a) + \alpha \Big[R_{t}(a) - Q_{t-1}(a)\Big], & A_{t} = a\\
Q_{t-1}(a), & A_{t} \ne a\\
\end{cases}$$
Or in non-incremental, if for simplicity all $A_{i} = a$:
$$Q_{t}(a) = (1-\alpha)^{t-1} Q_{1}(a) + \sum\limits_{i \in [n-1]} \alpha^{i}(1-\alpha)^{n-1-i}R_{t-i}(a)$$
## Properties
Doesn’t have convergence guarantee, because $\sum\limits \alpha^{2}_{t} > \infty$, but instead works good in nonstationary problems.