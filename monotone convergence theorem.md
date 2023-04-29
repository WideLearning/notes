# monotone convergence theorem
From [[passage of the limit under the integral sign]]
$\physics$
## Statement
If an increasing sequence of non-negative measurable $\{ f_{n} \}$ [[converges pointwise]] to $f$ on [[almost all]] $E$, then
$$\int_{E} f = \lim \int_{E} f_{n}$$

## Proof
According to [[Fatou’s lemma]]:
$$\int_{E} f \leq \lim \inf \int_{E} f_{n}$$
On the other hand, by [[linearity and monotonicity of integration]]:
$$ f_{n} \leq f $$
$$\int_{E} f_{n} \leq \int_{E} f$$
$$\sup \int_{E} f_{n} \leq \int_{E} f$$
$$\lim \sup \int_{E} f_{n} \leq f$$
And because [[lower limit]] is not less than [[upper limit]]:
$$\int_{E} f = \lim \int_{E} f_{n}$$