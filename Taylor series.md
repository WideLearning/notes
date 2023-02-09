# Taylor series
From [[algebra and analysis]] and [[numerical methods]]

Taylor series of order $n$ for $f(x)$ at $x_0$ is a polynomial approximation and it can be written in several ways with different conditions.

## Peano residual
$f \in C^n(a,b), x, x_0 \in (a, b)$ it is (with Peano residual):
$$ f(x) = \sum_{k=0}^n \frac{f^{(k)}(x_0)(x-x_0)^k}{k!} +o((x-x_0)^k)$$

Other residuals include lagrange (constant in $o$ is $f^{(n+1)}(\theta)$) or integral (can be derived through integrating by parts).

- [[Taylor series with Lagrange remainder]]
