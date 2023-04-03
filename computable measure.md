# computable measure
From [[automata and computability theory]] and [[measure theory]]
$\physics$
## Definition
A measure $\mu: 2^{[0, 1)} \to \mathbb{R}$ is defined by its value on each [[cylinder]]. So it is called computable / semicomputable when the corresponding function from cylinders to reals is computable / semicomputable.

## How measure is defined by cylinders
If we want to compute $\mu([l, r))$ we can start with $l \in [0, 1)$ and $r \in [0, 1)$ which gives us $\mu \in [0, 1]$. Then, suppose both $l$ and $r$ lie in $[0, 0.5)$, it gives us $\mu \in [0, \mu([0, 0.5))]$. Then $l \in [0, 0.25), r \in [0.25, 0.5)$. Here we learn nothing. But then each step again updates either lower or upper bound (because some cylinders are now either definitely included or definitely excluded). 
But why does it converge, if there are no limits on the measures of cylinders? 