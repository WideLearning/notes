# divided differences eliminate low-degree polynomials
From [[divided differences]]
$\physics$
## Statement
Suppose $f(x) = \sum\limits_{k=0}^{d} a_{k}x^{k}$. Then:
1. $\forall x_{[d+1]}: f[x_{[d+1]}] = a_{d}$
2. $\forall x_{[d+k]}, k > 1: f[x_{[d+k]}] = 0$

## Proof
By [[Newton interpolation]]: $f[x_{[d+1]}]$ is the coefficient for $N_{d}$, which must be the same as coefficient for $x_{k}$ in standard basis, so $f[x_{[d+1]}] = a_{k}$. And $f[x_{[d+k]}] = 0$ because on $d+1$-th step interpolating polynomial will be already precise and there will be no further corrections.