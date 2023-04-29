# approximation of simple function by step function
From [[step function]] and [[simple function]]
$\physics$
## Statement
For a [[simple function]] $\psi: I \to \mathbb{R}$  where $I$ is a bounded segment and $\varepsilon > 0$ there is a [[step function]] $h: I \to \mathbb{R}$ and a [[Lebesgue measurable set]] $F \subset I$ such that $h = \psi$ on $F$ and $m(I \setminus F) < \varepsilon$.

## Proof
Note that a finite linear combination of step functions is also step function, and simple function is a finite linear combination of characteristic functions of measurable sets. So we can assume $\psi = \chi_E$ for a [[Lebesgue measurable set]] $E \subset I$ without loss of generality.
By [[approximation of Lebesgue measurable set by finite disjoint union of intervals]] we can find $E’$ that is a finite disjoint union of intervals (so $\chi_{E'}$ is a step function). Denote $D = E \Delta E'$, we know $m(D) < \varepsilon$, take $F = I \setminus D$. This way $m(I \setminus F) = m(I \cap D) \leq m(D) < \varepsilon$.