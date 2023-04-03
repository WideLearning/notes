# conjugate directions method
From [[conjugate methods]]
$\physics$
## Statement
We are solving $\arg\min \norm{Ax - b} = \arg\min \qty(\frac{1}{2}\ev{Ax, x} - \ev{b,x})$ by the following algorithm:
$$x_{k+1} = x_{k} + \alpha_{k}p_{k}$$
where $p_{[n]}$ is a [[conjugate system]] and $\alpha_{k} = -\frac{\ev{r_{k}, p_{k}}}{\ev{Ap_{k}, p_{k}}}, r_{k} = Ax_{k} - b$.
Then, it will converge to the solution at $x_{n+1}$ or earlier for any $x_{1}\in \mathbb{R}^{n}$. 

## Proof
First, how $\alpha_{k}$ is derived:
$$f(\alpha) = \ev{A(x + \alpha p) - b, x + \alpha p} = \alpha^{2} \ev{Ap, p} + \alpha \ev{Ax - b, p} + \mathrm{const}$$
Then we solve for the extremum of this parabola and get the formula from the statement.

Because conjugate vectors are linearly independent, if we take $n$ of them, we span all of $\mathbb{R}^{n}$, therefore:
$$\exists c_{[n]}: x_{*} - x_{1} = \sum\limits c_{i}p_{i}$$
Projecting it onto $p_{k}$ (namely, multiplying by $p_{k}^{T}A$, or taking inner product with $Ap_{k}$) we get:
$$\ev{A(x_{*} - x_{1}), p_{k}} = c_{k}\ev{Ap_{k}, p_{k}}$$
$$c_{k} = \frac{\ev{b - Ax_{1}, p_{k}}}{\ev{Ap_{k}, p_{k}}} = -\frac{\ev{r_{0}, p_{k}}}{\ev{Ap_{k}, p_{k}}}$$
And $\ev{Ax_{1}, p_{k}} = \ev{Ax_{k}, p_{k}}$, because difference between $x_{k}$ and $x_{1}$ is a linear combination of $p_{[k-1]}$ which are conjugate to $p_{k}$ w.r.t. $A$. So $c_{k} = \alpha_{k}$.

## Properties
- [[expanding subspace minimization]]
- [[conjugate gradient method]] as an efficient implementation.