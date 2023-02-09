# determinant formula is independent of basis
From [[determinant]]
$\physics$
## Statement
Denote $f$ from [[formula for antisymmetric polylinear forms]] by $\det$ and let $e, f$ be two bases of $V$, $T \in \L(V)$, then:
$$\det [T]_{f} = \det [T]_{e}$$ 
## Proof
It’s enough to have two operations:
- $e_{1} = f_{1} + kf_{2}, \forall i > 1: e_{i} = f_{i}$
- $e_{1} = f_{2}, e_{2} = f_{1}, \forall i > 2: e_{i}= f_{i}$
Because then we can get any basis by Gaussian elimination.

First one means adding one row to another with some coefficient and the one column to another with some coefficient. For rows it doesn’t change anything because of assumed properties: $f(a, b + ka) = f(a, b) + f(a, ka) = f(a, b) + kf(a, a) = f(a, b) + k \cdot 0$. Because [[determinant formula is independent of transposition]] it’s enough.

Second one means exchanging two rows and then exchanging two columns. From the [[formula for antisymmetric polylinear forms]] we see that swap of two rows is equivalent to one transposition in every considered permutation, so the sign of the result will flip. Because [[determinant formula is independent of transposition]] it’s enough.