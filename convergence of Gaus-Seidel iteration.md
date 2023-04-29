# convergence of Gaus-Seidel iteration
From [[Gauss-Seidel iteration]]
$\physics$
## Statement
If $A = L + D + U$ is strictly diagonally dominant, [[Gauss-Seidel iteration]] converges from any point.

## Proof
Iteration matrix $G = -(D + L)^{-1}U$. We will prove that $\norm{G}_{\infty} < 1$. Consider $y = Gx$:
$$(D + L)y = -Ux$$
Now almost as in [[Gershgorin circle theorem]]:
$$\forall j. A_{j, j}y_{j} + \sum\limits_{k < j} A_{j, k}y_{k} = -\sum\limits_{k > j} A_{j, k} x_{k}$$
Take $j = \arg\max \abs{y_{k}}$, then:
$$\abs{A_{j, j}y_{j} + \sum\limits_{k < j}A_{j, k}y_{k}} \geq \left(\abs{A_{j, j}} - \sum\limits_{k < j} \abs{A_{j, k}}\right)\norm{y}_{\infty}$$
And the right-hand side is bounded as:
$$\abs{\sum\limits_{k > j} A_{j, k} x_{k}} \leq \left(\sum\limits_{k > j}\abs{A_{j, k}}\right)\norm{x}_{\infty}$$
Combining them:
$$\left(\abs{A_{j, j}} - \sum\limits_{k < j} \abs{A_{j, k}}\right)\norm{y}_{\infty} \leq \left(\sum\limits_{k > j}\abs{A_{j, k}}\right)\norm{x}_{\infty}$$
$$\norm{y}_{\infty} \leq \frac{\left(\sum\limits_{k > j}\abs{A_{j, k}}\right)}{\left(\abs{A_{j, j}} - \sum\limits_{k < j} \abs{A_{j, k}}\right)}\norm{x}_{\infty}$$
$$\norm{G}_{\infty} \leq \frac{\left(\sum\limits_{k > j}\abs{A_{j, k}}\right)}{\left(\abs{A_{j, j}} - \sum\limits_{k < j} \abs{A_{j, k}}\right)}$$
Which is less than $1$, because:
$$\abs{A_{j, j}} - \sum\limits_{k < j}\abs{A_{j, k}} > \sum\limits_{k > j}\abs{A_{j, k}}$$
By diagonal dominance.