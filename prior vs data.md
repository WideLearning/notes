# prior vs data
From [[Bayesian inference]]
$\require{physics}{}$
When we use [[bayesian update|bayesian updating]], we start with some prior and then correct it to fit the observed data better. So which of them has more impact on the final result?

## Task 1
Let's start with the case of normal distributions:
$X \sim \mathcal{N}(0, a),\quad \forall i\in 1\dots n: Y_{i}\sim \mathcal{N}(X, b)$, and all $Y_{i}$ are mutually independent.

Find the analytical expression for $p(X \mid Y_{1\dots n})$. Intuitively, we expect $X$ to be somewhere between $0$ and $\bar Y$, but to which end is it closer? How it depends on $a, b$ and $n$?

## Task 2
Now same exercise but with bernoulli:
$X \sim \mathrm{Beta}(a, b), \forall i \in 1\dots n: Y_{i} \sim \mathrm{Bern}(X)$, $Y$ are again i.i.d.

Express $p(X \mid Y_{1\dots n})$, check how it depends on $a + b$ and $n$.

## Hints
In Task 1 $X$ will follow normal distribution with parameters depending only on $a, b, n, \bar Y$.
In Task 2 $X$ will follow beta distribution with parameters depending only on $a, b, \abs{\{ y = 0 \mid y \in Y\}}$ and $\abs{\{ y = 1 \mid y \in Y\}}$.