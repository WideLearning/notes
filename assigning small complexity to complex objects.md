# assigning small complexity to complex objects
From [[Kolmogorov’s complexity]]
$\physics$
## Statement
Suppose we have a [[universal Turing machine]] $U$ used to defined [[Kolmogorov’s complexity]] and some other UTM $U'$ such that $C_{U'}(x) = 0$ (that is, $U’$ produces $x$ on empty input).
Then for large $K(x)$ we must have large $K(U')$ as well.

## Proof
Using [[self-delimiting string]]:
$$\forall y. K(y) \leq K(\ev{U', C_{U'}(y)}) \leq K(U') + \order{\log K(U')} + C_{U'}(y)$$
With $y = x$:
$$K(x) \leq K(U') + \order{\log K(U')} + 0$$
So $K(U')$ must be at least approximately $K(x)$, up to a logarithmic term.