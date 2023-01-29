# complex spectral theorem
From [[linear algebra]]
$\physics$
## Statement
If $F = \C$ and $T \in \L(V)$, the following are equivalent:
1. $T$ is [[normal operator]]
2. $V$ has an [[orthonormal basis]] consisting of [[eigenvector|eigenvectors]] of $T$
3. $T$ has diagonal matrix w.r.t. some [[orthonormal basis]] of $V$

## Proof
$2 \iff 3$: Diagonal matrix is equivalent to being written in basis of eigenvectors.
$3 \implies 1$: Then $T^{*}$ also has diagonal matrix in this basis and it only differes by conjugating all values. Then these matrices commute and $T$ is normal.
$1 \implies 3$: By [[Schur’s theorem]] any operator has upper-triangular matrix in some orthonormal basis $e_{[n]}$. Then [[normal + upper-triangular = diagonal]].
