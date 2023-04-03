# integral over set with measure zero is zero
From [[Lebesgue integral]]
$\physics$
## Statement
Let $f: E \to \mathbb{R}$ be a [[measurable function]] and $m(E) = 0$. 
$$\int_{E} f = 0$$
## Proof
As $\int f = \int f_{+} - \int f_{-}$, it’s enough to show for $f_{+}$ and $f_{-}$, that is, we can assume $f \geq 0$.
By definition of [[Lebesgue integral]] for non-negative functions, it will be a supremum of integrals of bounded functions over subset of $E$. But integral of a bounded function over a zero measure set is zero:
$$\int_{E_{0}} g \leq \int_{E_{0}} M \leq M \cdot m(E_{0}) = 0$$
And $\sup \{ 0 \} = 0$.
