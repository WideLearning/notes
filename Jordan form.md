# Jordan form
From [[linear algebra]]
$\physics$
## Statement
Suppose $T \in \L(V), F = \mathbb{C}$ then exists basis in which $[T]$ is block diagonal and each block is a [[Jordan cell]].

## Proof
By [[decomposition into invariant subspaces]] we can build such bases separately for each [[generalized eigenspace]] and then just concatenate them.
Now consider $G(\lambda, T)$. We already know a good form for $(T - \lambda)$ by [[nilpotent operator has sparse upper-triangulate matrix]]. Now we reorder it so that each vector is either ordinary eigenvector and is mapped to $0$, which starts a new block, or is a generalized eigenvector that is mapped to the previous one. After that we add $\lambda$ on the main diagonal and get the matrix for $T|_{G(\lambda, T)}$.