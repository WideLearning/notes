# B-spline
From [[spline interpolation]]
$\physics$
## Definition
Basis B-splines:
$$N_{i}^{0}(u) = [x_{i} \leq u < x_{i+1}]$$
$$N_{i}^{k}(u) = \frac{u - x_{i}}{x_{i+k} - x_{i}} N_{i}^{k-1}(u) + \frac{x_{i + k + 1} - u}{x_{i+k+1} - x_{i+1}} N_{i}^{k-1}(u)$$

## Properties
- $N_{i}^{k}$ is non-negative on $[u_{i}, u_{i+k+1}]$ and zero outside
- It is polynomial of degree $k$ (when restricted to its support)
- If we add extra points outside of $[a, b]$ then partition of unity holds: 
  $\sum\limits_{i=-k}^{m} N_{i}^{k}(u) = 1$, where $m$ is length of $x$