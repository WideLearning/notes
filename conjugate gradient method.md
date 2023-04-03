# conjugate gradient method
From [[conjugate methods]], an efficient implementation of [[conjugate directions method]]
$\physics$
## Algorithm
$r_{k} = Ax_{k} - b$: residuals (in terms of $Ax = b$) or gradients (in terms of $\ev{Ax - b, x} \to \min$)
$p_{0} = -r_{0}$ and $p_{k+1} = -r_{k+1} + \beta_{k+1}p_{k}$: conjugate directions
$x_{k+1} = x_{k} + \alpha_{k}p_{k}$: approximations to the solution
$\alpha_{k} = -\frac{r_{k}^{T}p_{k}}{p_{k}^{T}Ap_{k}}$: optimal step sizes
$\beta_{k+1} = \frac{r_{k+1}^{T}Ap_{k}}{p_{k}^{T}Ap_{k}}$: correction coefficients

Also, due to [[important properties of conjugate gradient method]] we can make some simplifications:
$\alpha_{k} = \frac{r_{k}^{T}r_{k}}{p_{k}^{T}Ap_{k}}$, $\beta_{k+1} = \frac{r_{k+1}^{T}r_{k+1}}{r_{k}^{T} r_{k}}$

## Properties
- Note that $b_{k+1}$ can be derived from $p_{k+1}^{T} A p_{k} = 0$ and $p_{k+1} = -r_{k+1} + \beta_{k+1}p_{k}$.
- [[important properties of conjugate gradient method]]

## Simple implementation
```python
n, t = 2, 3
A = torch.randn((n, n))
A = A.T @ A

b = torch.randn((n, 1))
x = torch.randn((t, n, 1))
x[1:] = float("nan")
r = torch.full((t, n, 1), float("nan"))
alpha = torch.full((t, 1), float("nan"))
beta = torch.full((t, 1), float("nan"))
c = torch.full((t, 1), float("nan"))
p = torch.randn((t, n, 1))
r[0] = A @ x[0] - b
p[0] = -r[0].clone()
c[0] = -1
eps = 1e-9

for k in range(t - 1):
    alpha[k] = -(r[k].T @ p[k]) / (p[k].T @ A @ p[k] + eps)
    c[k + 1] = c[k] * alpha[k]
    x[k + 1] = x[k] + alpha[k] * p[k]
    r[k + 1] = A @ x[k + 1] - b
    beta[k + 1] = (r[k + 1].T @ A @ p[k]) / (p[k].T @ A @ p[k] + eps)
    p[k + 1] = -r[k + 1] + beta[k + 1] * p[k]
```

## Exact implementation and some checks
```python
import numpy as np
import fractions
import random

random.seed(1)
rfrac = lambda: fractions.Fraction(random.randint(1, M), random.randint(1, M))


def rmat(*shape):
    x = np.empty(shape, dtype=object)
    x = x.ravel()
    for i in range(x.size):
        x[i] = rfrac()
    return x.reshape(shape)


def to_float(a):
    a = a.copy()
    shape = a.shape
    a = a.ravel()
    for i in range(a.size):
        a[i] = round(float(a[i]), 4)
    return a.reshape(shape)


n, t = 5, 6
M = 3

A = rmat(n, n)
A = A.T.dot(A)
b = rmat(n, 1)
x = rmat(t, n, 1)
r = rmat(t, n, 1)
alpha = rmat(t, 1)
beta = rmat(t, 1)
c = rmat(t, 1)
p = rmat(t, n, 1)
r[0] = A.dot(x[0]) - b
p[0] = -r[0].copy()
c[0] = -1

for k in range(t - 1):
    alpha[k] = -(r[k].T.dot(p[k])) / (p[k].T.dot(A.dot(p[k])))
    c[k + 1] = c[k] * (-alpha[k])
    x[k + 1] = x[k] + alpha[k] * p[k]
    r[k + 1] = A.dot(x[k + 1]) - b
    beta[k + 1] = (r[k + 1].T.dot(A.dot(p[k]))) / (p[k].T.dot(A.dot(p[k])))
    p[k + 1] = -r[k + 1] + beta[k + 1] * p[k]


def clean(p, qs, useA=False):
    def dot(a, b):
        if useA:
            return a.T.dot(A.dot(b))
        else:
            return a.T.dot(b)

    for q in qs:
        p -= dot(p, q) / dot(q, q) * q
        assert dot(p, q) == 0
    return p


for i in range(t):
    print(f"i = {i}")
    v = clean(p[i], p[:i])
    e_v = c[i] * np.linalg.matrix_power(A, i).dot(r[0])
    e_v = clean(e_v, p[:i])
    h = clean(r[i], p[:i])
    print(i, (v == e_v).all(), (h == -e_v).all())
```
