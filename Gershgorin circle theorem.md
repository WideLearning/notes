# Gershgorin circle theorem
From [[eigenvalue]]
$\physics$
## Statement
Consider $A \in \C^{n\times n}$ and denote $R_{i} = \sum\limits_{j\ne i} \abs{A_{i, j}}$. Then every [[eigenvalue]] of $A$ lies in $\bigcup\limits_{i \in [n]} D(A_{i,i}, R_{i})$, or in $D(A_{k, k}, R_{k})$ with $k = \arg\max \abs{v_{i}}$ in particular.

## Proof
Take an eigenvalue $\lambda$ with eigenvector $v$:
$$Av = \lambda v$$
In particular, for $i$-th row:
$$\sum\limits_{j \in [n]} A_{i, j}v_{j} = \lambda v_{i}$$
$$\lambda v_{i} = A_{i, i}v_{i} + \sum\limits_{j \ne i} A_{i, j}v_{j}$$
Taking $i = \arg\max \abs{v_{i}}$:
$$\lambda = A_{i, i} + \sum\limits_{j \ne i} A_{i, j} \frac{v_{j}}{v_{i}} \in D(A_{i, i}, R_{i})$$
