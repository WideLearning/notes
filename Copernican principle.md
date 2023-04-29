# Copernican principle
From [[Bayesianism vs frequentism]]
$\physics$
## Problem
$N \sim D$ 
$X \sim U(0, N)$
We don’t know distribution $D$, but know $X = x$ and want to estimate $n$ somehow.

## Through unbiased estimators
$$\E_{X|N}(X \mid N = n) = \frac{n}{2}$$
$$\E_{X|N}(2X \mid N = n) = n$$
$$\E_{X\mid N}(N - 2X \mid N = n) = 0$$
$$\E_{X, N}(N - 2X) = 0$$
At this point $N \approx 2X$ for frequentists, because they don’t care about particular $X$. 
Note that the following doesn’t work, because we can’t assume $N - 2X \perp X$:
$$\E_{N\mid X}(N - 2x \mid X = x) = 0$$
$$\E_{N\mid X}(N \mid X = x) = 2x$$

## Through independence (or Jeffrey’s prior)
Bayesian inference won’t work here out of the box, the answer strongly depends on a priori $p(N)$. 
But we can make an assumption $\frac{X}{N} \perp X$. It can be equivalently stated as “we don’t get information about the relative value of $X$ from the absolute value of $X$”, or by taking $p(N = n) \propto \frac{1}{n}$ as a prior. It is improper, but it encodes our lack of knowledge very well, e.g. it is the unique prior that will be invariant under the change of variables (aka Jeffrey’s prior).
$$P\left(\frac{X}{N} < k \mid X = x\right) = 1 - \min(k, 1)$$
$$P\left(\frac{N}{X} < k \mid X = x\right) = 1 - \frac{1}{\max(1, k)}$$
$$P\left(N < n \mid X = x\right) = 1 - \frac{1}{\max(1, \frac{n}{x})}$$
Ironically, now the median of $p_{N \mid X}(. \mid X = x)$ is $2x$, and the expected value doesn’t exist for this distribution. 