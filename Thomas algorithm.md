# Thomas algorithm
From [[Gaussian elimination]]
$\physics$
## Algorithm
It allows solving banded matrices with width $k$ in $\order{n k^{2}}$. The key is to do operations in right order, so that you don’t get growing tails of non-zero elements: first you make your matrix upper-triangulate, then either do backward pass, or `A = A[::-1, ::-1]` and repeat the first step. Of course, to do it efficiently, matrix should be stored and operated sparsely.

```python
def thomas_algorithm(A):
    n, m = A.shape

    free_row = 0
    for col in range(m):
        row = next((i for i in range(free_row, n) if A[i][col]), -1)
        if row == -1:
            continue
        A[[free_row, row]] = A[[row, free_row]]
        A[free_row] /= A[free_row][col]
        for row in range(free_row + 1, n):
            A[row] -= A[row][col] / A[free_row][col] * A[free_row]
        free_row += 1

    A = A[::-1, ::-1]

    free_row = 0
    for col in range(m):
        row = next((i for i in range(free_row, n) if A[i][col]), -1)
        if row == -1:
            continue
        A[[free_row, row]] = A[[row, free_row]]
        A[free_row] /= A[free_row][col]
        for row in range(n):
            if row != free_row:
                A[row] -= A[row][col] / A[free_row][col] * A[free_row]
        free_row += 1
    
    A = A[::-1, ::-1]
    return A
```
