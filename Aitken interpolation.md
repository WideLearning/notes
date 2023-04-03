# Aitken interpolation
From [[polynomial interpolation]]
$\physics$
## Statement
As in [[Lagrange interpolation]], we want to calculate $p(u) = \sum\limits_{i=0}^{n} y_{i}L_{i}(u)$.
Let’s set $a_{0, i} = y_{i}$ and $a_{k+1, i} = \alpha_{n - k, i} a_{k, i} + (1 - \alpha_{n - k, i}) a_{k, n - k}, \alpha_{k, i} = \frac{u - x_{k}}{x_{i}-x_{k}}$. Then $a_{n, 0} = p(u)$.

## Proof
By applying [[Lagrange interpolation]] to $\forall i. y_{i} = 1$ we get “partition of unity” property:
$$\sum\limits_{i=0}^{n} L_{i} = 1$$
Denote $L_{k, i}$ to be $L_{i}$ built for the first $n$ points. Note that:
$$\begin{cases}
L_{0, 0} = 1 \\
L_{k, i} = \frac{u - x_{k}}{x_{i} - x_{k}} L_{k - 1, i} = \alpha_{k, i}L_{k-1, i} \text{ (for $i < n$)} \\
\end{cases}$$
If we also derive recurrent for $L_{k, k}$, it will define every final $L_{i}$:
$$\begin{split}
L_{k, k} &= 1 - \sum\limits_{i=0}^{k-1} L_{k, i}\\
&= 1 - \sum\limits_{i=0}^{k-1} \alpha_{k, i}L_{k-1, i}\\
\end{split}$$
Actually, it’s already enough (see “another implementation”), but for some reason we go further:
$$\begin{split}
L_{k, k} &= 1 - \sum\limits_{i=0}^{k-1} \alpha_{k, i}L_{k-1, i}\\
&= \sum\limits_{i=0}^{k-1} (1 -  \alpha_{k, i}) L_{k-1, i}\\
\end{split}$$
And now we can introduce $a_{k, i}$:
$$\begin{split}
p(u) &= \sum\limits_{i=0}^{n-1} a_{0, i}L_{n, i}(u) + a_{0, n}L_{n, n}(u)\\
&= \sum\limits_{i=0}^{n-1}(\alpha_{n, i} a_{0, i} + (1 - \alpha_{n, n}a_{0, n})) L_{n-1, i}\\
&= \dots\\
&= \sum\limits_{i=0}^{0} a_{n, i}L_{0,i}(u) = a_{n, 0}
\end{split}$$

## Another implementation
```python
import numpy as np
import matplotlib.pyplot as plt

n = 5
x = np.arange(n + 1)
y = np.random.randn(n + 1)
u = 2.5
L = np.zeros((n + 1, n + 1))
L[0, 0] = 1


def alpha(k, i):
    return (u - x[k]) / (x[i] - x[k])


for k in range(1, n + 1):
    L[k, k] = 1
    for i in range(k):
        L[k, i] = alpha(k, i) * L[k - 1, i]
        L[k, k] -= L[k, i]

e = sum(y[i] * L[n, i] for i in range(n + 1))

print(u, e)

plt.plot(x, y)
plt.plot([u], [e], "o", ms=10)
plt.show()
```