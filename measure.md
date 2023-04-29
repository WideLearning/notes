# measure
From [[measure theory]]
$\physics$
## Definition
A measure $\mu$ on a measurable space $(X, \mathcal{M})$ is a function $\mu: \mathcal{M} \to [0, \infty]$ such that:
1. It is zero on empty set: $$\mu(\varnothing) = 0$$
2. It is countable additive: $$\mu\qty(\bigcup\limits_{\N} E_{i}) = \sum\limits_{\N} \mu(E_{i})$$

## Properties
- Monotonicity: $$A \subset B \in \mathcal{M}. \mu(A) \leq \mu(B)$$
- Excision: $$A \subset B \in \mathcal{M}, \mu(A) < \infty. \mu(B \setminus A) = \mu(B) - \mu(A)$$
- Countable monotonicity: $$A \subset \qty(\bigcup\limits_{\N} B_{i}). \mu(A) \leq \sum\limits_{\N} \mu(B_{i})$$
- [[continuity of measure]]

## Special cases
- [[finite measure]], [[sigma-finite measure]]