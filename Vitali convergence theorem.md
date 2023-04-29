# Vitali convergence theorem
From [[uniformly integrable]] and [[passage of the limit under the integral sign]]
$\physics$
## Statement
Suppose $m(E) < \infty$ and $f_{\N}: E \to \R$ is [[uniformly integrable]]. Also, $f_{\N}$ [[converges pointwise]] to $f$ on [[almost all]] $E$. Then $f$ is integrable over $E$ and:
$$\lim\int_{E} f_{n} = \int_{E} f$$

## Proof
Consider $\delta$ for $\varepsilon = 1$ in uniform integrability criteria. By [[set of finite Lebesgue measure as finite disjoint union of sets with small measure]] we can decompose $E$ into sets with measure not greater than $\delta$, therefore integrals of any $f_{i}$ over them will be not greater than $1$. And if there are $N$ these sets, integral of any $f_{i}$ is not more than $N$. By [[Fatou’s lemma]]:
$$\int_{E} f \leq \lim\inf \int_{E} f_{i} \leq N$$
So $f$ is integrable.

As $f$ is integrable, it is finite a.e. on $E$, and by [[integral over set with measure zero is zero]], $\int_{E} f = \int_{E \setminus E_{0}} f$ where $E_{0}$ contains points where $f$ is infinite or $f_{n}$ don’t converge to it. So we can assume pointwise convergence on whole $E$ and $f$ being finite.

Let $\varepsilon > 0$. Because $f_{n}$ is [[uniformly integrable]] we can find the corresponding $\delta$. By [[Egorov’s theorem]] we can find $N$ such that for $n \geq N$ we have $\abs{f_{n} - f} < \varepsilon$ on $E \setminus X$ with $m(X) < \delta$. Now:
$$\abs{\int_{E} f - \int_{E} f_{n}} \leq \int_{E}\abs{f - f_{n}} \leq \int_{E \setminus X} \abs{f - f_{n}} + \int_{X} \abs{f} + \int_{X} \abs{f_n} \leq 3 \varepsilon $$
So $\int_{E} f_{n} \to \int_{E} f$.