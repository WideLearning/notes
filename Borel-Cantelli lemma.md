# Borel-Cantelli lemma
From [[measure theory]]
$\physics$
## Statement
Suppose $E_{[\N]}$ is a collection of Lebesgue measurable sets and $\sum\limits_{k \in \mathbb{N}} m(E_{k}) < \infty$. Then [[almost all]] $x \in \mathbb{R}$ belong to finitely many of them.

## Proof
If $x$ belongs to infinitely many $E_{k}$, it belongs to the union of any tail of $E$. Now we need to show that the measure of intersection of such tails is zero.

[[continuity of measure]]:
$$m\qty(\bigcap\limits_{n=1}^{\infty} \bigcup\limits_{k=n}^{\infty} E_{k}) = \lim\limits_{n \to \infty} m\qty(\bigcup_{k=n}^{\infty} E_{k})$$
[[countable subadditivity of Lebesgue outer measure]]:
$$m\qty(\bigcup_{k=n}^{\infty} E_{k}) \leq \sum\limits_{k=n}^{\infty} m(E_{k}) = \sum\limits_{k \in \N} m(E_{k}) - \sum\limits_{k \in [n-1]} m(E_{k})$$
And this difference tends to zero by definition of infinite sum.
