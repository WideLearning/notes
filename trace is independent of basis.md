# trace is independent of basis
From [[trace]]
$\physics$
## Statement
Suppose $T \in \L(V)$ and $e$, $f$ are two bases of $V$, then:
$$\tr [T]_{e} = \tr [T]_{f}$$

## Proof
Note that $[T]_{e} = A^{-1}[T]_{f}A$ for some transition matrix $A$, so we need to prove $\tr B = \tr (A^{-1}BA)$ for $B \in \mathbb{F}^{n\times n}, A \in \mathbb{F}^{n \times n}$.

Because [[trace of product is commutative]]:
$$\tr (A^{-1}BA) = \tr (BA^{-1}A) = \tr (BI) = \tr B$$