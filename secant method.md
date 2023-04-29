# secant method
From [[solving non-linear equations]]
$\physics$
## Definition
$$x_{n+1} - x_{n} = -\frac{f(x_{n})(x_{n}- x_{n-1})}{f(x_{n}) - f(x_{n-1})}$$
So it is a [[Newton’s method]], where $f'(x_{n}) \approx \frac{f(x_{n}) - f(x_{n-1})}{x_{n} - x_{n-1}}$ is used.

## Properties
- Has $\varphi$ order of convergence.
- In multidimensional case is generalized by Broyden’s method.