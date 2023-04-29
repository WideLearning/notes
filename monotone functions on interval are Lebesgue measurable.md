# monotone functions on interval are Lebesgue measurable
From [[Lebesgue measurable function]]
$\physics$
## Statement
Suppose $f: (l, r) \to R$ is monotone, then $f$ is measurable.

## Proof
W.l.o.g. let $f$ be increasing. Consider $S = \{ x \in (l, r) \mid f(x) > c\}$ for some $c \in \R$. If it is not empty, consider $m = \inf S$. For all $x > m$ we definitely have $f(x) > c$. And depending on $f(m) > c$ or not, $S$ will be either an interval or half-interval. In both cases, it is measurable.
Then $f$ is a [[Lebesgue measurable function]] by definition.