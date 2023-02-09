# sigma-algebra
From [[measure theory]]
$\physics$
## Definition
For a set $X$ a $\sigma$-algebra is a set of subsets of $X$ closed under taking complements, countable unions and countable intersections.

In other words, $\Sigma \subset 2^{X}$ satisfies this properties iff:
1. $A \in \Sigma \implies (X \setminus A) \in \Sigma$
2. $\forall i \in \N: A_{i} \in \Sigma \implies \qty(\bigcup_{i \in N} A_{i}) \in \Sigma$
3. $\forall i \in \N: A_{i} \in \Sigma \implies \qty(\bigcap_{i \in N} A_{i}) \in \Sigma$
(2 and 3 are equivalent by De Morgan’s laws)