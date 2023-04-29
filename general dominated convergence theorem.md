# general dominated convergence theorem
From [[passage of the limit under the integral sign]]
$\physics$
## Statement
Consider measurable $f_{\mathbb{N}}$ [[converges pointwise]] to $f$ and non-negative measurable $g_{\mathbb{N}}$ converges pointwise to $g$, all of that on $E$. Suppose $g_{\mathbb{N}}$ dominates $f_{\mathbb{N}}$ (that is, $\forall n. \abs{f_{n}} \leq g_{n}$), then:
$$\lim \int_{E} g_{n} = \int_{E} g < \infty \implies \lim \int_{E} f_{n} = \int_{E} f$$

## Proof
Same as for [[dominated convergence theorem]], but use $g_{n} - f_{n}$ instead of $g - f_{n}$ and $g_{n} + f_{n}$ instead of $g + f_{n}$.

## See also
- [[dominated convergence theorem]] is a weaker version with a single $g$. 