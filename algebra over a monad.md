# algebra over a monad
From [[category theory]]
$\physics$
## Definition
Consider a [[monad]] $(T, \eta, \mu)$ in $\cat{C}$. Then $T$-algebra is an [[algebra over an endofunctor]] $(A \in \ob(\cat{C}), h: TA \to A)$ for $T$, where additionally the following diagrams commute:
1. $h$ is a $(TA, \mu_{A}) \to (A, h)$ morphism. Equivalently, $h$ is an [[action of monoid]] $(T, \eta, \mu)$:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large] TTA && TA \\ \\ TA && A \arrow["{\mu_A}", from=1-1, to=1-3] \arrow["h", from=3-1, to=3-3] \arrow["Th"', from=1-1, to=3-1] \arrow["h", from=1-3, to=3-3] \end{tikzcd}
\end{document}
```
2. $h$ is left inverse for $\eta_{A}$:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large] A && TA \\ \\ && A \arrow["{\mathrm{id}}"', from=1-1, to=3-3] \arrow["{\eta_{A}}", from=1-1, to=1-3] \arrow["h", from=1-3, to=3-3] \end{tikzcd}
\end{document}
```
Morphisms are defined in the same way as in [[algebra over an endofunctor]].

## Properties
- [[monadicity of algebra]]
- [[monadicity of adjunction]]