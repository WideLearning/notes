# determinant is multiplicative
From [[determinant]]
$\physics$
## Statement
Suppose $A, B \in \L(V)$, then:
$$\det (AB) = \det A \det B$$

## Proof
Consider $f(M) = \det (MB)$. It is polylinear in $M$, because scaling one column in $M$ correspondingly scales one column in $MB$ and therefore $\det MB$ too, because it is polylinear. So $f(M)$ is polylinear, and for similar reasons it is antisymmetric. By [[formula for antisymmetric polylinear forms]] we get that $f(M)$ is $C \cdot \det M$ and the constant $C$ is actually $\det B$, which we can see from $f(I) = \det B$.