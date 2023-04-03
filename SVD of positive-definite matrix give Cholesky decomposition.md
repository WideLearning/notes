# SVD of positive-definite matrix give Cholesky decomposition
From [[singular value decomposition]] and [[Cholesky decomposition]]
$\physics$
## Statement
If $A$ is [[positive operator]] and its [[singular value decomposition]] is $A = UDV$, then $U^{-1} = V$.

## Proof
$$A^{2} = A^{T}A = V^{T}DU^{T}UDV = V^{T}D^{2}V$$
So $A^{2}$ is $D^{2}$ in some other basis, to which we translate by $V$. Then $A$ is $D$ in that basis: $A = V^{T} D V$, $UDV = V^{T}DV$, and because all matrices are invertible here, $U = V^{T}$.