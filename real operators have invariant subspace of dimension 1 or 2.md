# real operators have invariant subspace of dimension 1 or 2
From [[complexification]] and [[invariant space]]
$\physics$
## Statement
Suppose $T \in \L(V), F = \mathbb{R}$. Then $\exists U \leqslant V: TU \leqslant U, \dim U \in \{1, 2\}$.

## Proof
Because [[eigenvalues exist in Cn]], complex operators always have eigenvectors and therefore one-dimensional [[invariant space]]. So consider [[complexification]] $T_{\mathbb{C}}$ and its eigenvalue and eigenvector:
$$T_{\mathbb{C}}(u + iv) = (a + bi)(u + iv)$$
$$Tu + iTv = (au - bv) + i(av + bu)$$
And because $T$ is real:
$$\begin{cases}
Tu &= au - bv\\
Tv &= av + bu\\
\end{cases}$$
Then $\ev{v, u}$ is invariant under $T$.