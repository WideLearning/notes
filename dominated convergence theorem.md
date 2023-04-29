# dominated convergence theorem
From [[passage of the limit under the integral sign]]
$\physics$
## Statement
Consider $f_{\mathbb{N}}$ where $f_{n}: E \to \mathbb{R}$ is a [[Lebesgue measurable function]]. Suppose there is a measurable and integrable $g: E \to \mathbb{R}$ that dominates $f_{\mathbb{N}}$ on $E$ (that is, $\abs{f_{n}} \leq g$).
If $f_{\mathbb{N}}$ [[converges pointwise]] to $f$ (on [[almost all]] $E$), then $f$ is integrable over $E$ and":
$$\lim \int_{E} f_{n} = \int_{E} f$$

## Proof
Because $g$ is integrable, it must be finite a.e. on $E$. Then $f_{n}$ and $f$ must also be finite a.e. on $E$. We again ignore “a.e.”, because [[integral over set with measure zero is zero]].
Note that $g - f$ and $g - f_{n}$ for each $n$ are measurable and non-negative, and $g - f_{\mathbb{N}}$ converges pointwise to $g - f$. By [[Fatou’s lemma]]:
$$\int_{E} (g - f) \leq \lim\inf \int_{e}(g - f_{n})$$
$$\lim\sup \int_{E} f_{n} \leq \int_{E} f$$
And similarly for $g + f$ and $g + f_{n}$:
$$\int_{E} f \leq \lim\inf \int_{E}f_{n}$$
As lower and upper limits are equal:
$$\int_{E} f = \lim \int_{E} f_{n}$$

## See also
- [[bounded convergence theorem]] is a weaker version where $g$ is constant (and therefore $m(E) < \infty$).
- [[general dominated convergence theorem]] is a stronger version where we have $g_{\mathbb{N}}$ instead of $g$.