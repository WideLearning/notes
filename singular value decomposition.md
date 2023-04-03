# singular value decomposition
From [[linear algebra]]
$\physics$
## Statement
For $T \in \L(V)$ with [[singular value|singular values]] $s_{[n]}$ there exist  [[orthonormal basis|orthonormal bases]] $e_{[n]}$ and $f_{[n]}$ such that:
$$\forall v \in V: Tv = \sum\limits_{i=1}^{n} s_{i}\ev{v, e_{i}} f_{i}$$

Or, in other words, $[T] = UDV$, where $U$ and $V$ are [[isometry|isometries]] and $D$ is diagonal.

## Proof
It builds upon [[polar decomposition]]. First we build a basis of eigenvectors for [[square root (of operator)]] of $T$, which gives $s_{i}\ev{v, e_{i}}e_{i}$. Then we apply $S$ from polar decomposition to it, which replaces the last $e_i$ with $S e_i = f_i$.

## Properties
- [[SVD of positive-definite matrix give Cholesky decomposition]]