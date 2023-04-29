# action of monoid
From [[categorical monoid]]
$\physics$
## Definition
Consider a [[categorical monoid]] $(C, \mu, \eta)$ in a [[strict monoidal category]] $(\cat{B}, \square, E)$.
A left action of this monoid on an object $A \in \cat{B}$ is a morphism $v: C \square A \times A$ such that the following commutes:
```tikz
\usepackage{tikz-cd}
\usepackage{amssymb}
\begin{document}
\begin{tikzcd}[row sep=huge] {C \square C \square A} && {C \square A} \\ \\ {C \square A} && A
\arrow["{\mu \square \mathrm{id}_{A}}", from=1-1, to=1-3]
\arrow["v", shift left=1, from=1-3, to=3-3]
\arrow["{\mathrm{id}_{C} \square v}"', from=1-1, to=3-1]
\arrow["v"', shift left=1, from=3-1, to=3-3] \end{tikzcd}
\end{document}
```

Right action is defined symmetrically.

Actions of a monoid form a category. Morphisms between $(A_{1}, v_{1})$ and $(A_{2}, v_{2})$ is a morphism $f: A_{1} \to A_{2}$ such that $v_{2}(m, f(x)) = f(v_{1}(m, x))$ in set notation or in general $v_{2} \circ (\id \square f) = f \circ v_{1} \circ (\id \square \id)$.

## Properties
- For algebraic [[monoid]] the diagram above means that acting with two elements is the same as acting with their product (“product” here means the monoid operation $\mu$)