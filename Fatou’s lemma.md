# Fatou’s lemma
From [[passage of the limit under the integral sign]]
$\physics$
## Statement
If a sequence of non-negative measurable $\{ f_{n} \}$ [[converges pointwise]] to $f$ on [[almost all]] $E$, then
$$\int_{E} f \leq \lim \inf \int_{E} f_{n}$$
## Proof
[[integral over set with measure zero is zero]]: we can just assume convergence on all $E$.
[[pointwise limit preserves measurability]]: $f$ is non-negative and measurable.
So by definition of [[Lebesgue integral]] for non-negative functions, $\int_{E} f = \sup \int_{E_{0}} h$, where $h \leq f$ is a measurable function with $\abs{h} \leq M$, $E_{0} \subset E$ and $m(E_{0}) < \infty$. We need to show for every such $h$:
$$\int_{E_{0}} h \leq \lim \inf \int_{E} f_{n}$$
Define $h_{n} = \min(h, f_{n})$, then $\forall x \in E_{0}. \lim h_{n}(x) = h(x)$, because $f_{n}(x) \to f(x)$ and $\min(h, f) = h$.
By [[bounded convergence theorem]]:
$$\lim \int_{E_{0}} h_{n} = \int_{E_{0}} h$$
For each $n$, $\int_{E_{0}} h_{n} \leq \int_{E_{0}} f_{n} \leq \int_{E} f_{n}$, and as [[lower limit]] is monotone:
$$\int_{E_{0}} h = \lim \int_{E_{0}} h_{n} \leq \lim \inf \int_{E_{0}} h_{n} \leq \lim \inf \int_{E} f_{n}$$

## Example
Take $E = (0, 1)$ and $f_{n} = n \cdot \chi_{(0, \frac{1}{n})}$, then $\{ f_{n} \} \to 0$, but:
$$\int_{E} 0 = 0 < 1 = \lim \inf \int_{E} f_n$$
This doesn’t happen in [[monotone convergence theorem]].