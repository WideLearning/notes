# Newton’s method converges quadratically
From [[Newton’s method]]
$\physics$
## Statement
Suppose $f \in C^{2}([a, b])$, $x_{0} \in [a, b]$ and:
1. $f(a) < 0 < f(b)$
2. $\inf\limits_{x \in [a, b]} f'(x) = m > 0$
3. $\sup\limits_{x \in [a, b]} \abs{f''(x)} = M$
Denote $d_{n} = x_{n} - r, \Delta_{n} = x_{n+1} - x_{n}$, where $r$ is the unique root of $f$ on $[a, b]$.
Then $\abs{d_{n+1}} \leq \frac{M}{2m} \abs{d_{n}}^{2}$.

## Proof
$$\Delta_{n} = -\frac{f(x_{n})}{f'(x_{n})}$$
$$f(r) = f(x_{n}) + f'(x_{n})(r - x_{n}) + \frac{1}{2}f''(\theta)(r - x_{n})^{2},\quad \theta \in (r, x_{n})$$
$$0 = f(x_{n}) + f'(x_{n})(\Delta_{n} - d_{n+1}) + \frac{1}{2}f''(\theta)d_{n}^{2},\quad \theta \in (r, x_{n})$$
In geometric terms, it means that to get from $f(x_{n})$ to $0$ we need to go $\Delta_{n} = x_{n+1} - x_{n}$ with $f'(x_{n})$ speed, then $-d_{n+1} = r - x_{n+1}$ with the same speed (so, in total it would be simply plotting tangent at $x_{n}$ up to $r$), and then something quadratic in $d_{n}$ remains.
$$d_{n+1} = \frac{1}{2}\frac{f''(\theta)}{f'(x_{n})}d_{n}^{2},\quad \theta \in (r, x_{n})$$
$$\abs{d_{n+1}} \leq \frac{M}{2m} \abs{d_{n}}^{2}$$