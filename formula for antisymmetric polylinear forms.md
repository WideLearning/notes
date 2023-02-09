# formula for antisymmetric polylinear forms
From [[determinant]]
$\physics$
## Statement
Consider $f: V^{n} \to F$ such that:
- $f(\dots, \alpha v + \beta u, \dots) = \alpha f(\dots, v, \dots) + \beta f(\dots, u, \dots)$
- $f(\dots, v, \dots, v, \dots) = 0$

Then for $A \in F^{n \times n}$ and some basis $e_{{n}}$:
$$f\left(\sum\limits_{i=1}^{n} e_{i}A_{i, 1}, \dots, \sum\limits_{i=1}^{n} e_{i}A_{i, n}\right) = f(e_{1}, \dots, e_{n})\sum\limits_{p \in \sigma_{n}} \mathrm{sgn}(p) \prod A_{p_{i}, i}$$
## Proof
First we rewrite $f(\dots)$ into a sum of all possible $n^{n}$ terms by polylinearity. Only $n!$ of them remain, because equal $p_{i}$ mean zero impact due to antisymmetricity. Then we move $f(e_{1}, \dots, e_{n})$ out, because $f(\dots, v, u, \dots) = -f(\dots, u, v, \dots)$ (follows from antisymmetricity) and only $\mathrm{sgn}(p)$ remains in the sum.