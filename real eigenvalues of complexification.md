# real eigenvalues of complexification
From [[complexification]] and [[eigenvalue]]
$\physics$
## Statement
Eigenvalues of $T$ are exactly the real eigenvalues of $T_{\mathbb{C}}$, that is:
$$\forall \lambda \in \R: (\exists v \in \mathbb{C}^{n}: T_{\mathbb{C}}v) = \lambda v \iff (\exists v \in \mathbb{R}^{n}: Tv = \lambda v)$$

## Proof
$\implies$:
Denote $v = a + bi$:
$$T_{\mathbb{C}}v = T_{\mathbb{C}}(a + bi) = Ta + iTb$$
$$\lambda(a + bi) = Ta + iTb$$
$$\begin{cases}
\lambda a = Ta\\
\lambda b = Tb\\
\end{cases}$$
So both $a$ and $b$ can work as $v$ and $\lambda$ is indeed an eigenvalue.

$\impliedby$:
The left part works with the same $v$ by definition of [[complexification]], there is just no imaginary part.