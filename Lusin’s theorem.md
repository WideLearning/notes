# Lusin’s theorem
From [[measure theory]]
$\physics$
## Statement
Let $f: E \to \mathbb{R}$ be a [[Lebesgue measurable function]] and $\varepsilon > 0$, then there is a continuous function $g: \mathbb{R} \to \mathbb{R}$ and closed $F \subset E$ such that $f = g$ on $F$ and $m(E \setminus F) < \varepsilon$.

## Proof
1. Consider the case where $f$ is a [[simple function]] taking values $a_{[n]}$.
Denote by $E_{[n]}$ the sets where $f$ takes the corresponding values. We can take $F_{i} \subset E_{i}$ witih $m(E_{i}\setminus F_{i}) < \frac{\varepsilon}{n}$. Then $F = \bigcup F_{i}$ will satisfy $m(E \setminus F) < \varepsilon$ and $f$ is continuous on it, because it is constant on each $F_{i}$. Now take $g = f$ on $F$. Note that $\mathbb{R} \setminus E$ is open and [[open subset of reals is disjoint countable union of intervals]], so on each interval $(l, r)$ we can define $g(x) = \frac{(r - x)f(l) + (x - l)f(r)}{r - l}$ (linear interpolation, that is). Now it is linear, and thus continuous, inside interval, and also matches values on the ends of interval, so after doing so $g$ is continuous on $\mathbb{R}$.

2. Now $f$ is measurable function in general, but $m(E) < \infty$.
By [[simple approximation theorem]] we have $f_{\mathbb{N}} \to f$, then by (1) we can choose $g_{\mathbb{N}}$ such that $g_{n} = f_{n}$ on $F_{n}$ and $m(E \setminus F_{n}) < \frac{\varepsilon}{2^{n+1}}$. Also, by [[Egorov’s theorem]] there is $F_{0}$ with $m(E \setminus F_{0}) < \frac{\varepsilon}{2}$ on which $f_{\N}$ [[converges uniformly]] to $f$. Then $F = F_{0} \cup \bigcup_{\mathbb{N}} F_{i}$ is closed, $m(E \setminus F) < \varepsilon$, and on it $f$ is a uniform limit of continuous functions, so it is continuous. Now we can extend it to continuous $g: \mathbb{R} \to \mathbb{R}$ as in (1).

3. General case
As in [[outer approximation of Lebesgue measurable by open and G-delta sets]], use [[set of infinite Lebesgue measure as countable disjoint union of sets with finite measure]], then apply (2) for each of those sets with exponentially decreasing margins.
