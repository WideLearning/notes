# algebra over an endofunctor
From [[category theory]]
$\physics$
## Definition
Consider an [[endofunctor]] $F: \cat{C} \to \cat{C}$. An $F$-algebra is a pair $(X \in \ob(\cat{C}), \alpha: FX \to X)$.
Morphisms between $(X, \alpha)$ and $(Y, \beta)$ are all such $f: X \to Y$ that the following diagram commutes:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large] FX && X \\ \\ FY && Y \arrow["\alpha", from=1-1, to=1-3] \arrow["\beta", from=3-1, to=3-3] \arrow["f", from=1-3, to=3-3] \arrow["Ff"', from=1-1, to=3-1] \end{tikzcd}
\end{document}
```

## Properties
- [[initial F-algebra is a fixed point]]
- [[initial F-algebra as a colimit]]

## See also
- [[algebra over a monad]] is a special case where $F$ is a [[monad]]