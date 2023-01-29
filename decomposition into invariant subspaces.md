# decomposition into invariant subspaces
From [[linear algebra]]
$\physics$
## Statement
Let $T \in \L(V), F = \C$ and $\lambda_{[m]}$ are distinct eigenvalues of $T$, then:
- $\forall i: G(\lambda_{i}, T)$ is [[invariant space]] under $T$
- $\forall i: (T - \lambda_{i})|_{G(\lambda_{i}, T)}$ is [[nilpotent operator]]
- $V = \bigoplus_{i=1}^{m} G(\lambda_{i}, T)$

## Proof
1. Because [[generalized eigenspace]] is $\ker (T - \lambda)^{\dim V}$ we can use [[kernel and image of polynomial are invariant]].
2. From the same definition, we restrict an operator to the kernel of its power. Obviously, it becomes nilpotent.
3. Let’s consider $V’ = \bigoplus_{i=1}^{m} G(\lambda_{i}, T)$. The sum will be direct due to [[independence of generalized eigenvectors]]. Now let’s prove that $T|_{V / V'}$ has no eigenvalues and because [[eigenvalues exist in Cn]], it implies $V = V'$:
Restrict $T$ on $V / G(\lambda_{1}, T)$. Suppose $\lambda_{1}$ is still an eigenvalue: $\exists v\ne 0 \in V / G(\lambda_{1}, T): (T|_{V / G(\lambda_{1}, T)} - \lambda_{1})v = 0$. But it means that $(T - \lambda_{1})v \in G(\lambda_{1}, T)$, which means $(T - \lambda_{1})v \in \ker (T - \lambda_{1})^{\dim V}$ then $v \in \ker (T - \lambda_{1})^{\dim V + 1}$ and by [[lemma about sequence of kernels]] $v \in \ker (T - \lambda_{1})^{\dim V}$. So we found non-trivial intersection of $V/G(\lambda_{1}, T)$  and $G(\lambda_{1}, T)$, contradiction.
Then we remove other eigenvalues in the same way.