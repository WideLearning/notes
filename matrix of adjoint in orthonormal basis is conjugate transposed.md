# matrix of adjoint in orthonormal basis is conjugate transposed
From [[adjoint]], related to [[matrix of dual is transposed]]
$\physics$
## Statement
Suppose $T \in \L(V)$, then $[T]_{i, j} = \overline{[T^{*}]_{j, i}}$ in every [[orthonormal basis]] $e$.

## Proof
$$\begin{split}
[T]_{i, j} &= \ev{T e_{i}, e_{j}}\\
&= \ev{e_{i}, T^{*}e_{j}}\\
&= \overline{\ev{T^{*}e_{j}, e_{i}}}\\
&= \overline{[T^{*}]_{j, i}}
\end{split}$$