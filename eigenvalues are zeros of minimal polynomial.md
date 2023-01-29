# eigenvalues are zeros of minimal polynomial
From [[minimal polynomial]]
$\physics$
## Statement
Suppose $T \in \L(V)$, then $\lambda$ is zero of its [[minimal polynomial]] iff it is [[eigenvalue]] of $T$.

## Proof
Zero → eigenvalue:
By [[Cayley-Hamilton theorem]] and [[annihilating polynomials are multiples of minimal]] we know that [[characteristic polynomial]] is multiple of minimal. Then it has all its zeros. And zeros of characteristic polynomial are eigenvalues by definition.

Eigenvalue → zero:
Suppose $Tv = \lambda v$. Because $T^{n} v = \lambda^{n} v$ we get $p(T)v = p(\lambda)v$ where $p$ is the minimal polynomial.
So $p(T) = 0 \implies p(T)v = 0 \implies p(\lambda)v = 0 \implies p(\lambda) = 0$.