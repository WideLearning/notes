# monomorphism
From [[morphism]], dual to [[epimorphism]]
$\physics$
## Definition
A morphism $f: X \to Y$ is a monomorphism iff
$$\forall Z \in \mathrm{Ob}(C), g, h \in \mathrm{Hom}(Z, X). f \circ g = f \circ h \implies g = h$$

```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[sep=large]
Z && X && Y
\arrow["f", hook, from=1-3, to=1-5]
\arrow["g"', shift right=1, from=1-1, to=1-3]
\arrow["h", shift left=1, from=1-1, to=1-3]
\end{tikzcd}
\end{document}
```

## Examples
- In [[category of sets]] monomorphisms are injective functions. Same in algebraic categories like [[category of groups]], [[category of monoids]], etc.
- [[split monomorphism]], [[regular monomorphism]]