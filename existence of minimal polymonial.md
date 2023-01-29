# existence of minimal polymonial
From [[minimal polynomial]]
$\physics$
## Statement
Suppose $T \in \L(V)$. Then:
- There is unique [[minimal polynomial]].
- Its degree is bounded by $(\dim V)^2$ (or $\dim V$ for $F = \mathbb{C}$ by [[Cayley-Hamilton theorem]]).

## Proof
Existence:
$1, T, T^{2}, \dots, T^{n^{2}}$ are linearly dependent, because $\dim \L(V) = (\dim V)^{2}$.
So we pick the first power that is expressible as linear combination of the previous ones (the smallest linearly dependent prefix, in other words) and the coefficients of that linear combination give us the polynomial.

Uniqueness:
The degree of this polynomial is minimal by construction. And if there is another monic annihilating polynomial with the same degree, then their difference is also annihilating and has even smaller degree, which is a contradiction.