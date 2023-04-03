# square roots of positive operators
From [[positive operator]] and [[square root (of operator)]]
$\physics$
## Statement
Let $T \in \L(V)$, then the following are equivalent:
1. $T$ is a [[positive operator]]
2. $T$ is [[self-adjoint operator]] and each [[eigenvalue]] is nonnegative
3. $T$ has a unique positive [[square root (of operator)]]
5. $\exists R: T = R^{*} R$

## Proof
$1 \implies 2$: It is already self-adjoint. Having negative [[eigenvalue]] will contradict the definition of positive operator.
$2 \implies 3$: We find a basis of eigenvectors by [[complex spectral theorem]] / [[real spectral theorem]]. Then we replace each eigenvalue with its square root and get our positive square root operator (it has diagonal matrix with nonnegative numbers in this eigenvector basis, so it is clearly satisfies all conditions of positive operator). Note that because the action of $R$ on each eigenvector is uniquely determined, the square root is also unique.
$3 \implies 4$: We have $T = R^{2}$ and $R$ is self-adjoint, so we also have $T = R^{*} R$.
$4 \implies 1$: [[product of operator and adjoint is positive]]