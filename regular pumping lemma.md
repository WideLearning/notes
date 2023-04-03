# regular pumping lemma
From [[regular language]], related to [[context-free pumping lemma]]
$\physics$
## Statement
Let $A$ be a [[regular language]], then exists pumping length $p$ such that for any string $s$ with length at least $p$ it can decomposed as $s = xyz$ where:
1. $\ell(xy) \leq p$
2. $\ell(y) > 0$
3. $\forall n \in \mathbb{N}. xy^{n}z \in A$.

## Proof
Let $M = (Q, \Sigma, \delta, q_{0}, F)$ be a [[finite automaton]] that recognizes $A$. Let’s show that $p = \abs{Q}$ is enough.

Indeed, if a string $s$ is accepted, there is a path from the starting state to one of accepting states with  $\ell(s) + 1 > \abs{Q}$ vertices in it. Then among the first $p + 1$ already was a cycle. Take the part before cycle as $x$, the cycle itself as $y$ and the part after as $z$.
