# Cholesky decomposition
From [[numerical methods]] and [[linear algebra]]
$\physics$
## Statement (for $\R$)
If $A$ is [[positive operator]] (and [[self-adjoint operator]]), it can be decomposed $A = LDL^{T}$, where $L$ is lower-triangular with ones on the main diagonal and $D$ is diagonal with positive entries. As corollary, we also have $A = CC^{T}, C = L\sqrt{D}$.

## Proof
About existence, see [[square roots of positive operators]]. Also [[SVD of positive-definite matrix give Cholesky decomposition]].

## Algorithm
$$A_{i, j} = \sum\limits_{k \in [n]} C_{i, k} C^{T}_{k, j} = \sum\limits_{k \in [n]} C_{i, k} C_{j, k} = \sum\limits_{k \in [\min(i, j)]} C_{i, k} C_{j, k}$$
$$A_{i,i} = \sum\limits_{k \in [n]} C^{2}_{i, k} = \sum\limits_{k \in [i]} C^{2}_{i, k}$$
$$C_{i, i} = \sqrt{A_{i, i} - \sum\limits_{k \in [i-1]} C_{i, k}^{2}}$$
And for $i > j$ (because $C$ is lower-triangular):
$$C_{i, j} = \frac{1}{C_{j, j}}\left(A_{i, j} - \sum\limits_{k \in [j - 1]} C_{i, k}C_{j, k} \right)$$
Then just compute it in the right order:
```python
def cholesky(A):
    n, m = A.shape
    assert n == m

    C = np.zeros((n, n))
    for i in range(n):
        for j in range(i):
            # C[i][j] = (A[i][j] - sum(C[i][k] * C[j][k] for k in range(j))) / C[j][j]
            C[i][j] = (A[i][j] - np.dot(C[i], C[j])) / C[j][j]
        # C[i][i] = np.sqrt(A[i][i] - sum(C[i][k] * C[j][k] for k in range(i)))
        C[i][i] = np.sqrt(A[i][i] - np.dot(C[i], C[i]))

    return C

```