# mean value theorem
From [[equalities in analysis]], particular case of [[Taylor series with Lagrange remainder]]
$\physics$
## Statement
Suppose $f$ is differentiable on $[x_0, x]$:
$$\exists \theta \in (x_{0}, x): f(x) = f(x_{0}) + f'(\theta)(x - x_{0})$$

## Proof
Denote $g(t) = f(x_{0}) + \frac{f(x) - f(x_{0})}{x - x_{0}}(t - x_{0})$. 
Our statement is equivalent to $\exists \theta \in (x_{0}, x): g'(t) = 0$. Also, $g(x) = g(x_{0})$ by construction.

That is Rolle’s theorem: Either we have at least one extremum (strictly) inside the interval, where the derivative will be zero by Fermat’s theorem, or it is constant, so the derivative is zero everywhere.