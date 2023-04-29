# Landau notation
From [[time complexity]]
$\physics$
| Notation                                        | Description                                          | Definition                                                              |
| ----------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------- |
| $f = \order{g(n)}$                              | $\abs{f}$ bounded by $g$ from above up to a constant | $\lim \sup \frac{f(n)}{g(n)} < \infty$                                  |
| $f = o(g(n))$                                   | $f$ is dominated by $g$                              | $\lim \frac{f(n)}{g(n)} = 0$                                            |
| $f(n) \sim g(n)$                                | $f$ is equivalent to $g$                             | $\lim \frac{f(n)}{g(n)} = 1$                                            |
| $f(n) = \Theta(g(n))$                           | $f$ is equivalent to $g$ up to a constant            | $0 < \lim \inf \frac{f(n)}{g(n)}, \lim \sup \frac{f(n)}{g(n)} < \infty$ |
| $f(n) = \Omega_{\text{Knuth}}(g(n))$            | $f$ is bounded by $g$ from below up to a constant    | $\lim\inf \frac{f(n)}{g(n)} > 0$                                        |
| $f(n) = \Omega_{\text{Hardy-Littlewood}}(g(n))$ | $f$ is not dominated by $g$                          | $\lim \sup \frac{\abs{f(n)}}{g(n)} > 0$                                 |
| $f(n) = \omega(g(n))$                           | $f$ dominates $g$                                    | $\lim \frac{f(n)}{g(n)} = \infty$                                       |
