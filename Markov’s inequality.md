# Markov’s inequality
From [[probability inequalities]] and [[Lebesgue integral]]

## Statement
For nonnegative r.v. $X$:
$$ P(X \geq a) \leq \frac{\mathrm{E}(X)}{a}$$
Or in terms of measure theory:
For [[measurable function]] $f: E \to \mathbb{R}$
$$m(f^{-1}([a, \infty))) \leq \frac{\int_{E} f}{a}$$

## Proof
Probabilistic:
$$E(X) = E(X \mid X \geq a)P(X \geq a) + E(X \mid X < a)P(x < a) \geq E(X \mid X \geq a)P(X \geq a) \geq aP(X \geq a)$$

Measure-theoretic:
Denote $E_{a} = f^{-1}([a, \infty))$. If $m(E_{a}) < \infty$ we consider $0 \leq a\chi_{E_{a}} \leq f$ which is a [[simple function]] with bounded support, so $a m(E_{a}) = \int_{E} a\chi_{E_{a}} \leq \int_{E} f$.
Otherwise we take $E_{a, n} = E_{a} \cap [-n, n]$ and get that $\infty = \lim am(E_{a, n}) = \lim a\chi_{E_{a, n}} \leq \int_{E} f$.
