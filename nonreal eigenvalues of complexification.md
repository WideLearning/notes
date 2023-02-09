# nonreal eigenvalues of complexification
From [[complexification]] and [[eigenvalue]]
$\physics$
## Statement
Suppose $T \in \L(V), F = \R$, then:
1. $\forall \lambda \in \mathbb{C}, j \in \mathbb{Z}_{\geq 0}, v \in V_{\mathbb{C}}: (T_{\mathbb{C}} - \lambda)^{n}v = \overline{(T_{\mathbb{C}} - \bar\lambda)^{n}\bar v}$
2. $\lambda$ is an [[eigenvalue]] of $T_{\mathbb{C}}$ iff $\bar \lambda$ is
3. [[algebraic multiplicity]] of $\lambda$ equals multiplicity of $\bar \lambda$

## Proof
1. First, for $n = 0$ it’s easy:
$$(T_{\mathbb{C}} - \lambda)^{0}v = v = \overline{\bar v} = \overline{(T_{\mathbb{C}} - \bar\lambda)^{0}\bar v}$$
Now step from $n$ to $n + 1$. Denote $(T_{\mathbb{C}} - \lambda)^{n}v = x + iy$ and $(T_{\mathbb{C}} - \bar \lambda)^{n}\bar v = x - iy$ (for some $x, y \in \mathbb{R}$) and $\lambda = a + bi, a, b, \in \mathbb{R}$, then:
$$(T_{\mathbb{C}} - a - bi)(x + iy) = (Tx + by - ax) + i(Ty - ay - bx)$$
$$(T_{\mathbb{C}} - a + bi)(x - iy) = (Tx + by - ax) + i(-Ty + ay + bx)$$
$$\begin{split}
(T_{\mathbb{C}} - \lambda)^{n + 1}v
&= (Tx + by - ax) + i(Ty - ay - bx) \\
&= \overline{(Tx + by - ax) + i(-Ty + ay + bx)}\\
&= \overline{(T_{\mathbb{C}} - \bar\lambda)^{n + 1}\bar v}\\
\end{split}$$
2. From (1) with $n = 1$, $(T_{\mathbb{C}} - \lambda)v = 0 \iff (T_{\mathbb{C}} - \bar \lambda) \bar v = 0$.
3. From (1) with $n = \dim V$: bases of $G(\lambda, T)$ and $G(\bar \lambda, T)$ are complex conjugate.