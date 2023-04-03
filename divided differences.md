# divided differences
From [[Newton interpolation]]
$\physics$
## Definition
For given $x_{[n]}, y_{[n]}$ denote:
$$[y_{k}] = y_{k}$$
$$[y_{k}, \dots, y_{k+j}] = \frac{[y_{k+1}, \dots, y_{k+j}] - [y_{k}, \dots, y_{k+j-1}]}{x_{k+j} - x_{k}}$$
Also, if $y = f(x)$, another notation is used: $f[x_{k}, \dots, x_{k+j}]$.

## Properties
- For each $x_{[n]}$ it is a [[linear map]]: $(\alpha f + \beta g)[x_{[n]}] = \alpha f[x_{[n]}] + \beta g[x_{[n]}]$
- [[divided differences are invariant under reversal]]
- [[lemma about divided differences]]
- [[divided differences are symmetric]]
- [[divided differences eliminate low-degree polynomials]]
- [[Leibniz rule for divided differences]]
- [[mean value theorem for divided differences]]