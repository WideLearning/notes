# semicomputable function
From [[computable function]]
$\physics$
## Definition
A real-valued function $f(x)$ is upper semicomputable if there is a rational-valued [[computable function]] $g(x, k)$ that is non-increasing w.r.t. $k$ and converges to $f(x)$. So, upper semicomputable = bounded from above.

And $f(x)$ is lower semicomputable if there is a rational-valued [[computable function]] $g(x, k)$ that is non-decreasing w.r.t. $k$ and converges to $f(x)$. So, lower semicomputable = bounded from below.

## Equivalent definition
A real-valued $f(x)$ is computable (= upper and lower semicomputable) iff there is a rational-valued $g(x, k)$ such that $\abs{f(x) - g(x, k)} < \frac{1}{k}$.

## Proof of equivalence
$\implies:$
Suppose we have $l(x, k)$ and $r(x, k)$ as our lower and upper bounds. We know that they will converge to $f(x)$ in the limit, so to produce $g(x, k)$ we can wait until $\abs{l(x, k') - r(x, k')} < \frac{2}{k}$ and then set $g(x, k) = \frac{l(x, k') + r(x, k')}{2}$.

$\impliedby$:
Let’s get lower semicomputability from such $g$, the upper should be symmetrical. Note that $l'(x, k) = g(x, k) - \frac{1}{k}$ is a lower bound for $f(x)$ for all $k$ and $\lim l'(x, k) = \lim g(x, k) = f(x)$. Now we want to make it monotonic: $l(x, k) = \max\limits_{k' \in [k]} l'(x, k)$, and the limit still holds, because if for some $k$ $l'(x, k)$ was in $\varepsilon$-neighborhood of $f(x)$, taking $\max$ with other lower bounds won’t change it.

## Example
- Let $K$ be a [[halting set]] and $f(x) = [x \in K]$. Then $g(x, k)$ can check if the machine and input specified by $x$ leads to a halt in at most $k$ steps. It gives a valid lower bound. But it isn’t computable, because to get any approximation closer than $f(x) \in [0, 1]$ you need to actually know whether $x\in K$ or no, and it can’t be computed in finite time (that is, $g(x, 1)$ already might halt).