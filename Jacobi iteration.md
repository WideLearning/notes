# Jacobi iteration
From [[iterative approach for linear systems]]
$\physics$
## Definition
Here we take $Q = \mathrm{diag}(A) = D$ and get:
$$x_{k} = (I - D^{-1}A)x + D^{-1}b$$

## Properties
- By [[convergence of iteration for linear systems]], it converges iff $\norm{I - D^{-1}A} < 1$. It is true, e.g. for diagonally dominant matrix, because after dividing the $i$-th row by $A_{i, i}$ the sum of non-diagonal entries is less than $1$ and the diagonal entry is zero after subtracting $I$, so [[Gershgorin circle theorem]] says that eigenvalues of $I - D^{-1}A$ must lie in $D(0, r)$ with $r < 1$.