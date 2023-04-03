# passing uniform limit under integral
From [[passage of the limit under the integral sign]]
$\physics$
## Statement
If sequence of bounded [[measurable function|measurable functions]] $\{ f_{n} \}$ [[converges uniformly]] to $f$ on $E$ with $m(E) < \infty$, then 
$$\lim \int_{E} f_{n} = \int_{E} f$$

## Proof
Note that [[pointwise limit preserves measurability]], so $f$ is also bounded and measurable. And [[bounded measurable functions on finite measure sets are integrable]], so all mentioned integrals exist.

W.l.o.g. $f - \frac{1}{n} \leq f_{n} \leq f + \frac{1}{n}$:
$$\abs{\int_{E} f_{n} - \int_{E} f } \leq \int_{E} \abs{f_{n} - f} \leq \frac{m(E)}{n}$$
