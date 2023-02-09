# normality test via norm
From [[normal operator]]
$\physics$
## Statement
$$ (\forall v \in V: \norm{Tv} = \norm{T^{*}v}) \iff (T T^{*} = T^{*}T)$$
## Proof
Expand norm to [[inner product]]:
$$\ev{Tv, Tv} = \ev{T^{*}v, T^{*}v}$$
Now in both parts move left operator to the right:
$$\ev{v, T^{*}Tv} = \ev{v, TT^{*}v}$$
So $TT^{*}$ and $T^{*}T$ give the same quadratic form, the by [[extracting bilinear from quadratic]] it means same bilinear, and the same operator.

## Corollary
In the matrix of normal operator, $i$-th row and $i$-th column have the same norm. It is because $\norm{Te_{i}}$ is the norm of $i$-th row, and $\norm{T^{*}e_{i}}$ is the norm of $i$-th column (after conjugation, which doesn’t change norm anyway) by [[matrix of adjoint in orthonormal basis is conjugate transposed]].