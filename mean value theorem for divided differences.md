# mean value theorem for divided differences
From [[divided differences]], [[equalities in analysis]]
$\physics$
## Statement
For pairwise distinct $x_{[n+1]}$ and $n$ times differentiable $f$:
$$\exists \xi \in (\min x, \max x). f[x_{[n+1]}] = \frac{f^{(n)}(\xi)}{n!}$$

## Proof
By [[Newton interpolation]] we have a unique $P$ interpolating $f$ in $x_{[n+1]}$ with $\deg P = n$. Let $g = f - P$, then it has zeros in $x_{[n+1]}$. Applying [[Rolle’s theorem]] to $g, g', g''$ and up till $g^{(n)}$ we find $\xi \in (\min x, \max x). g^{(n)}(\xi) = 0$. So, $f^{(n)}(\xi) = P^{(n)}(\xi)$. And from [[Taylor series]] we know $P^{(n)}(x) = p_{n} n!$, where $p_{n} = f[x_{[n+1]}]$ by construction. 