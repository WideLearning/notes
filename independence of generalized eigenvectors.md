# independence of generalized eigenvectors
From [[generalized eigenvector]], related to [[eigenvectors with different eigenvalues are independent]]
$\physics$
## Statement
Suppose $T \in \L(V)$ and $v_{[m]}$ are generalized eigenvectors with corresponding eigenvalues $\lambda_{[m]}$. Then $v_{[m]}$ are linearly independent.

## Proof
While $v_{1}$ by itself isn’t an [[eigenvector]], $w = (T - \lambda_{1})^{k}$ where $k = \max t: (T - \lambda_{1})^{t} \ne 0$ is:
$$(T - \lambda_{1})^{k + 1}v = 0 \implies (T - \lambda_{1})w = 0 \implies (T - \lambda)^{n}w = (\lambda_{1}- \lambda)^{n}w$$
Then applying $(T - \lambda_{1})^{k}(T - \lambda_{2})^{n}\dots(T - \lambda_{m})^{n}$ (with brackets in any order, because they all commute) will nullify any eigenvector except $v_{1}$. Suppose there is a non-trivial zero linear combination and apply this operator:
$$\begin{split}
0 &= a_{1}v_{1} + \dots + a_{m}v_{m}\\
&= a_{1}(T - \lambda_{1})^{k}(T - \lambda_{2})^{n}\dots(T - \lambda_{m})^{n}v_{1}\\
&= a_{1}(T - \lambda_{2})^{n}\dots(T - \lambda_{m})^{n}(T - \lambda_{1})^{k}v_{1}\\
&= a_{1}(T - \lambda_{2})^{n}\dots(T - \lambda_{m})^{n}w\\
&= a_{1}(\lambda_{1} - \lambda_{2})^{n}\dots(\lambda_{1} - \lambda_{m})^{n}w\\
\end{split}$$
$$a_{1} = 0$$
And in the same way we can show other $a_{i}$ to be zero, so the vectors must be linearly independent.