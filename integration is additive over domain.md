# integration is additive over domain
From [[Lebesgue integral]]
$\physics$
## Statement
Let $f: E \to \mathbb{R}$ be a [[measurable function]] and $E = A \sqcup B$ where $A, B$ are also measurable.
$$\int_{E} f = \int_{A} f + \int_{B} f$$
## Proof
$$\int_{A}f = \int_{E} \chi_{A} f, \int_{B} f = \int_{E} \chi_{B} f$$
And then [[integration is linear and monotone]]:
$$\int_{E} f = \int_{E} (\chi_{A} + \chi_{B}) f = \int_{A} f + \int_{B} f$$