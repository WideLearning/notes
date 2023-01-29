# normal + upper-triangular = diagonal
From [[normal operator]]
$\physics$
## Statement
If [[normal operator]] $T \in \L(V)$ has upper-triangular matrix in some basis, the matrix must be diagonal.

## Proof
$$[T]_{e} = \begin{pmatrix}a_{1, 1} & \dots & a_{1, n}\\ & \ddots  & \vdots\\0 & & a_{n, n}\end{pmatrix}$$
From [[normality test via norm]] we know $\norm{T e_{1}} = \norm{T^{*} e_{1}}$, so sums in the first row and in the first column have to be equal. Then $a_{1, 2:n} = 0$. Now we can do the same with $e_{2}$ because the first row doesn’t stop us anymore, and so on. Only diagonal entries can be non-zero in the end.