# Krylov subspace
From [[conjugate methods]]
$\physics$
## Definition
For $A \in F^{n\times n}, b \in F^{n}$ the order-$r$ Krylov subspace is
$$\mathcal{K}_{r}(A, b) = \ev{b, Ab, A^{2}b, \dots, A^{r-1}b}$$
## Properties
- $\mathcal{K}_{r}(A, b) \subset \mathcal{K}_{r+1}(A, b)$.
- $A\mathcal{K}_{r}(A, b) \subset \mathcal{K}_{r+1}(A, b)$.
- There is some $r_{0}$ such that $\dim \mathcal{K}_{r}(A, b) = r$ for $r \leq r_{0}$ and $\dim \mathcal{K}_{r}(A, b) < r$ else.