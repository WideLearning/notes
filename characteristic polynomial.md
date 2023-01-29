# characteristic polynomial
From [[linear algebra]]
$\physics$
## Definition
Suppose $T \in \L(V), F = \mathbb{C}$, and $\lambda_{[m]}$ are eigenvalues of $T$ with [[algebraic multiplicity|algebraic multiplicities]] $d_{[m]}$, then
$$p(t) = \prod_{i=1}^{m} (t - \lambda_{i})^{d_{i}}$$
is called characteristic polynomial of $T$.

## Properties
- It has degree $\dim V$ by [[decomposition into invariant subspaces]]
- It annihilates $T$: [[Cayley-Hamilton theorem]]
- It is multiple of [[minimal polynomial]] because [[annihilating polynomials are multiples of minimal]]
- $p(t) = \det(t - A)$ (todo)