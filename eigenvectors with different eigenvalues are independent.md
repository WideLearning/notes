# eigenvectors with different eigenvalues are independent
From [[eigenvector]]

## Statement
Let $T \in \L(V)$ and $\lambda_{[n]}$ are distinct eigenvalues with $v_{[n]}$ being the corresponding eigenvectors. Then $v_{[n]}$ are linearly independent.

## Proof
W.l.o.g. suppose that $v_{n} = \sum\limits_{i=1}^{n-1} c_{i} v_{i}$ (1) and $v_{[n-1]}$ are linearly independent:
$$\lambda_{n}v_{n} = T(v_{n}) = \sum\limits_{i=1}^{n-1} \lambda_{i}c_{i}v_{i}\text{ (2)}$$
Now, $\lambda_{n}(1) - (2)$:
$$0 = \sum\limits_{i=1}^{n-1} (\lambda_{n} - \lambda_{i})c_{i}v_{i}$$
So $v_{[n-1]}$ turned out to be linearly dependent, contradiction.