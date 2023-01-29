# isometries in C
From [[isometry]]
$\physics$
## Statement
Suppose $F = \mathbb{C}$ and $T \in \L(V)$, then the following are equivalent:
1. $T$ is an [[isometry]]
2. There is an [[orthonormal basis]] $e$ of eigenvectors of $T$ whose eigenvalues have absolute value $1$

## Proof
$1 \implies 2$: You can pick any eigenvector and get the absolute value of its eigenvalue by definition of isometry. And there will be enough eigenvectors, because from [[inverse of isometry]] we know that $T$ is a [[normal operator]] and by [[complex spectral theorem]] we have this basis of eigenvectors.
$2 \implies 1$: To check $\norm{Tv} = \norm{v}$ for any $v$ express it as a linear combination of eigenvectors, then apply $T$ element-wise, and calculate norm. Applying $T$ won’t change norm because all eigenvalues have absolute value $1$.
