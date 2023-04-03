# bounded measurable functions on finite measure sets are integrable
From [[Lebesgue integral]]
$\physics$
## Statement
Let $f: E \to \mathbb{R}$ be a bounded [[measurable function]] and $m(E) < \infty$. Then [[Lebesgue integral]] of $f$ exists.

## Proof
From [[simple approximation lemma]] we  have $l_{\mathbb{N}}, r_{\mathbb{N}} \to f$ such that $l_{n} \leq f \leq r_{n}$ and $\abs{r_{n}- l_{n}} < \frac{1}{n}$. Then $0 \leq \int_{E} l_{n} - \int_{E} r_{n} \leq \frac{1}{n}m(E)$ and because [[integration of simple functions is linear and monotone]] also $0 \leq \int_{E} l_{n} - r_{n} \leq \frac{1}{n}m(E)$. 
Because it approaches zero, lower and upper integrals are equal.