# measurable almost everywhere functions are measurable
From [[measurable function]]
$\physics$
## Statement
If $f: E \to \mathbb{R}$ is a [[measurable function]] and for [[almost all]] $x \in E$ we have $f(x) = g(x)$, then $g$ is also measurable.

## Proof
Denote $E_{0} = \{ x \mid f(x) \ne g(x) \}$, we know $m(E_{0}) = 0$.
$$g^{-1}((c, \infty)) = \qty(g^{-1}((c, \infty)) \cap E_{0}) \cup \qty(g^{-1}((c, \infty)) \cap (E \setminus E_{0}))$$
Left part is subset of $E_{0}$, so also has zero measure. Right part is equivalent to $f^{-1}((c, \infty)) \cap (E \setminus E_{0})$, which is intersection of two measurable sets, so is measurable.
Then $g^{-1}((c, \infty))$ is a union of two measurable sets and is measurable.