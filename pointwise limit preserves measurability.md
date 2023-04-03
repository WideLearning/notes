# pointwise limit preserves measurability
From [[converges pointwise]]
$\physics$
## Statement
Let $f_{\mathbb{N}} \to f$ pointwise almost everywhere on $E$ and $\forall n. f_{n}$ are measurable. Then $f$ is measurable as well.

## Proof
Restrict on measurable subset of domain, then will come back by [[measurable almost everywhere functions are measurable]].

Consider the following:
1. $f(x) < c$
2. $\exists k \in \mathbb{N}. f(x) < c - \frac{1}{k}$
3. $\exists k, N \in \mathbb{N}. \forall n \geq N. f_{n}(x) < c - \frac{1}{k}$
4. $\exists k \in \mathbb{N}. \forall n \geq k. f_{n}(x) < c - \frac{1}{k}$
5. $\exists k \in \mathbb{N}. f(x) \leq c - \frac{1}{k}$
Here $1 \implies 2 \implies 3 \implies 4 \implies 5 \implies 1$, so:
$$f^{-1}((\infty, c)) = \bigcup\limits_{k \in \mathbb{N}} \bigcap\limits_{n \geq k} f_{n}^{-1}\left(\left(-\infty, c - \frac{1}{k}\right)\right)$$
Finally, use the definition of [[measurable function]] and [[measurable sets are a sigma-algebra]].