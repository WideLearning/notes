# alternative definition of orthogonal projector
from [[orthogonal projector]]

## statement
$$P_{K}(x) = 0 \Longleftrightarrow x \in K^{\perp}$$

## proof
$\implies$:
assume $P_{K}(x) = 0$ but $x \not\in K^{\perp}$, that is, $\exists y \in K: \langle x, y \rangle \ne 0$ ([[orthogonal complement]]).
then we can subtract $\varepsilon\frac{\langle x, y \rangle}{\langle y, y \rangle} y$ from $x$, which will reduce its projection on $y$.
but it was already minimal by definition, contradiction.

$\impliedby$:
from [[orthogonal complement]]:
$$\forall y \in K: \langle x, y \rangle = 0$$
take $y = P_{K}(x)$, then $\langle x, P_{K}(x) \rangle = 0$.
also  [[P(x - P(x)) = 0]], so $\langle x - P_{K}(x), P_{K}(x) \rangle = 0$, by previous paragraph.
by [[orthogonal projector is additive on K]]: $\langle P_{K}(x), P_{K}(x) \rangle = 0$, that is $P_{K}(x) = 0$.