# integrability of bounded measurable functions on finite measure sets
From [[Lebesgue integral]]
$\physics$
## Statement
Let $f: E \to \mathbb{R}$ be a bounded [[Lebesgue measurable function]] and $m(E) < \infty$. Then [[Lebesgue integral]] of $f$ exists.

## Proof
From [[simple approximation lemma]] we  have $l_{\mathbb{N}}, r_{\mathbb{N}} \to f$ such that $l_{n} \leq f \leq r_{n}$ and $\abs{r_{n}- l_{n}} < \frac{1}{n}$. Then $0 \leq \int_{E} l_{n} - \int_{E} r_{n} \leq \frac{1}{n}m(E)$ and from [[linearity and monotonicity of integration of simple functions]] also $0 \leq \int_{E} l_{n} - r_{n} \leq \frac{1}{n}m(E)$. 
Because it approaches zero, lower and upper integrals are equal.