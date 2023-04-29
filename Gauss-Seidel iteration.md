# Gauss-Seidel iteration
From [[iterative approach for linear systems]]
$\physics$
## Definition
Here $Q$ is the lower-triangular part of $A$. Or, equivalently, it is [[Jacobi iteration]] where we use newly computed approximations for $x_{<i}$ when computing $x_{i}$.

$$x_{k+1} = (I - Q^{-1}A)x_{k} + Q^{-1}b$$
$$Qx_{k+1} = (Q - A)x_{k}+ b$$
$$Lx_{k+1} = -Ux_{k} + b$$
$$x_{x+1} = L^{-1}(b - Ux_{k})$$

## Properties
- [[convergence of Gaus-Seidel iteration]]

## See also
- [[successive over-relaxation]]