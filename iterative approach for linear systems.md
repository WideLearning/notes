# iterative approach for linear systems
From [[solving systems of linear equations]]
$\physics$
## Definition
Instead of $Ax = b$ we iterate $Qx = (Q - A)x + b$, which is equivalent. Iteration is given by:
$$x_{k+1} = (I - Q^{-1}A)x_{k} + Q^{-1}b$$

## Examples
- [[Richardson iteration]]
- [[Jacobi iteration]]
- [[Gauss-Seidel iteration]]

## Properties
- [[convergence of iteration for linear systems]]