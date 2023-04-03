# interpolation error theorem
From [[polynomial interpolation]]
$\physics$
## Statement
Let $f \in C^{n+1}([a, b])$ and $p$ with $\deg p \leq n$ interpolating it in $x_{[0:n]}$ ($n + 1$ points). Then
$$\forall u \in [a, b]. f(u) - p(u) = \frac{1}{(n+1)!}f^{(n+1)}(\theta)\prod\limits_{0 \leq i \leq n} (u - x_{i}), \theta \in (a, b)$$
And for $x_{i} = a + \frac{b - a}{n}i$ we have:
$\abs{f(u) - p(u)} \leq \frac{1}{4(n+1)}(\max\limits_{[a, b]} \abs{f^{(n+1)}})\qty(\frac{b - a}{n})^{n+1}$

## Proof
By [[lemma about divided differences]]:
$$f(u) - p(u) = f[x_{[0:n]}, u]\prod\limits_{0 \leq i \leq n} (u - x_{i})$$
And by [[mean value theorem for divided differences]]:
$$f[x_{[0:n]}, u] = \frac{1}{(n+1)!}f^{(n+1)}(\theta), \theta \in (a, b)$$
For the second part we will use [[divided differences are symmetric]]. In particular, for any $u$ we can rearrange $x$ by distance to $u$ and then $\abs{u - x_{0}}\abs{u - x_{1}} \leq \frac{h^{2}}{4}$ (with equality for $u = \frac{x_{0} + x_{1}}{2}$) and $\abs{u - x_{i}} \leq 2i$. Multiplying all them and taking maximum of $(n+1)$-th derivative we get the required bound. 