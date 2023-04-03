# bounded convergence theorem
From [[passage of the limit under the integral sign]]
$\physics$
## Statement
If a uniformly bounded sequence of [[measurable function|measurable functions]] $\{ f_{n} \}$ [[converges pointwise]] to $f$ on $E$ with $m(E) < \infty$, then:
$$\lim \int_{E} f_{n} = \int_{E} f$$

Unifromly bounded means: 
$$\exists M. \forall n, x. \abs{f_{n}(x)} \leq M$$

## Proof
Take $\varepsilon > 0$. By [[Egorov’s theorem]] we can find $F \subset E$ with $m(E \setminus F) < \varepsilon$  where $\{ f_{n} \}$ [[converges uniformly]] to $f$. By [[passing uniform limit under integral]]:
$$\lim \int_{F} f_{n} = \int_{F} f$$
And $\abs{\int_{E \setminus F} f_{n} - f_{n}} \leq \int_{E \setminus F} \abs{f_{n} - f} \leq 2M \varepsilon$, so
$$\int_{E} f - 2M \varepsilon \leq \lim \int_{E} f_n \leq \int_{E} f + 2M \varepsilon$$