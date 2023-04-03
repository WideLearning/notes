# problematic subtraction
From [[floating point representation]]
$\physics$
## Statement
Let $x > y > 0$ be in normalized representation with $b = 2$. And $\exists p, q \in \mathbb{N}. 2^{-p} \leq 1 - \frac{y}{x} \leq 2^{-q}$.
Then between $q$ and $p$ significant bits are lost when calculating $x - y$.

## Proof
W.l.o.g. assume $x = \overline{0.x_{1}x_{2}\dots x_{k}} \cdot 2^{0}$, $x_{1} \ne 0$. Because $x - y \in [2^{-p}x, 2^{-q}x]$, we will have to remove $q$ to $p$ zeros from the left, to make it normalized, which means adding unknown bits to the right and losing precision.