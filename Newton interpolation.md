# Newton interpolation
From [[polynomial interpolation]]
$\physics$
## Statement
Let $\{ x_k \}_{k=0}^{n}$ and $\{ y_k \}_{k=0}^{n}$ be nodes and values for interpolation. Consider a polynomial:
$$\begin{cases}
p(t) = \sum\limits_{k=0}^{n} [y_{0}, \dots , y_{k}]N_{k}(x) \\
N_{k}(x) = \prod\limits_{i=0}^{k-1} (x - x_{k}) \\
\end{cases}$$
Where $[y_{0}, \dots, y_{k}]$ means [[divided differences]].
Then $\forall k \in [0, n]. p(x_{k}) = y_{k}$, that is, it is an interpolating polynomial.

## Proof
Follows by induction from [[lemma about divided differences]].