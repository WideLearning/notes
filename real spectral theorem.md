# real spectral theorem
From [[linear algebra]], related to [[complex spectral theorem]]
$\physics$
## Statement
For $F = \R$ and $T \in \L(V)$ the following are equivalent:
1. $T$ is [[self-adjoint operator]]
2. $V$ has an [[orthonormal basis]] of eigenvectors of $T$
3. $T$ has a diagonal matrix w.r.t. some [[orthonormal basis]] of $T$

## Proof
As in [[complex spectral theorem]]:
$2 \iff 3$: Diagonal matrix is equivalent to being written in basis of eigenvectors.
$3 \implies 1$: Diagonal matrix is symmetric and therefore $T$ is self-adjoint.

The next step is harder, though, because we can’t use [[Schur’s theorem]] anymore:

$1 \implies 2$: Induction, base is $\dim V = 1$ where both $(1)$ and $(2)$ are trivial.
Note that [[self-adjoint operator has eigenvalues]] (and eigenvectors). Let’s call this eigenvector $v$, then we restrict $U$ to $\ev{v}^{\perp}$ by [[self-adjont operators and invariant subspaces]] and use $1 \implies 2$ in this smaller dimension to find the rest of orthonormal basis.