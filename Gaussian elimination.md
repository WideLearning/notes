# Gaussian elimination
From [[numerical methods]]
$\physics$
## Algorithm
We are solving system of linear equations $[A \mid b]$, which denotes $Ax = b$. 
It can be done with forward-pass that transforms into upper-triangular form, and then backward pass, that calculates values. Or one pass that transforms as much as possible, and if $A$ was invertible, it will transform it into unit matrix, and $b$ will be transformed into $x$.

```python
import numpy as np


def gaussian_elimination(A):
    n, m = A.shape
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
    return A


A = np.array(
    [
        [1, 2, 3, 7],
        [4, 5, 6, 3],
        [2, 3, 1, 5],
    ],
    dtype=np.float64,
)
print(gaussian_elimination(A))
# [[ 1.          0.          0.         -9.44444444]
#  [ 0.          1.          0.          7.88888889]
#  [-0.         -0.          1.          0.22222222]]

```

## Modifications
- [[scaled partial pivoting]]
- [[Thomas algorithm]]
- [Cuthill-McKee algorithm](https://en.wikipedia.org/wiki/Cuthill%E2%80%93McKee_algorithm)
