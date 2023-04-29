# categorical monoid
From [[category theory]]
$\physics$
## Definition for strict monoidal category
A monoid in a [[strict monoidal category]] $(\cat{B}, \square, E)$ is a triple $(C \in \ob(\cat{B}), \mu: C \square C \to C, \eta: E \to C)$ such that the following diagrams commute:
1. Associativity law:
```tikz
\usepackage{tikz-cd}
\usepackage{amssymb}
\begin{document}
\begin{tikzcd}[row sep=large] {C \square C \square C} && {C \square C} \\ \\ {C \square C} && C \arrow["{\mu \square \mathrm{id}_{C}}", from=1-1, to=1-3] \arrow["{\mathrm{id}_{C}\square \mu}"', from=1-1, to=3-1] \arrow["\mu"', from=3-1, to=3-3] \arrow["\mu", from=1-3, to=3-3] \end{tikzcd}
\end{document}
```
2. Unit laws:
```tikz
\usepackage{tikz-cd}
\usepackage{amssymb}
\begin{document}
\begin{tikzcd}[row sep=large] C && {C \square C} \\ \\ {C\square C} && C \arrow["{\eta \square \mathrm{id}_{C}}", from=1-1, to=1-3] \arrow["{\mathrm{id}_{C} \square \eta}"', from=1-1, to=3-1] \arrow["{\mathrm{id}_{C}}"', from=1-1, to=3-3] \arrow["\mu"', from=3-1, to=3-3] \arrow["\mu", from=1-3, to=3-3] \end{tikzcd}
\end{document}
```

Morphism $f$ of monoids $(C, \mu, \eta) \to (C', \mu', \eta')$ is an arrow $f: C \to C'$ such that:
1. Something like naturality: $f \circ \mu = \mu' \circ (f \square f)$
2. Unit is preserved: $f \eta = \eta'$

## Examples
- $(\cat{Set}, \times, 1_{\cat{Set}})$ → [[monoid|algebraic monoids]]
- $(\cat{C}^{\cat{C}}, \circ, \id_{\cat{C}})$ → [[monad|monads]]
- $(\cat{Ab}, \otimes, \mathbb{Z})$ → rings
- $(\cat{Cat}, \times, 1_{\cat{Cat}})$ → [[strict monoidal category]]

## Properties
- In case of algebraic [[monoid]]: $C \in \ob(\cat{Set})$ is a set, $\mu: C \times C \to C$ is a binary operation on it, $\eta: 1 \to C$ is a way to select [[unit element]]. 
- [[action of monoid]]