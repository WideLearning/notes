# Bezier curve
From [[interpolation methods]]
$\physics$
## Definition
For a given set of vectors $a_{[0:n]}$ and a point $u \in [0, 1]$:
$$b(u) = \E(a_{X}), X \sim \mathrm{Bin}(n, u)$$
Or explicitly in terms of Bernstein polynomials $B^{n}_{i}(x) = \binom{n}{i} x^{i}(1-x)^{n-i}$:
$$b(u) = \sum\limits_{i=0}^{n} B^{n}_{i}(u)a_{i}$$

## Properties
- $b(0) = a_{0}, b(1) = a_{n}$
- $B^{n}_{i}(u) = uB^{n-1}_{i-1}(u) + (1 - u)B^{n-1}_{i}(u)$
- [[de Casteljau algorithm]]

## See also
- [[Bezier-like curves for other distributions]]