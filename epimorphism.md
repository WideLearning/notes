# epimorphism
From [[morphism]], dual to [[monomorphism]]
$\physics$
## Definition
A morphism $f: X \to Y$ is an epimorphism iff
$$\forall z \in \mathrm{Ob}(C),  g, h \in \mathrm{Hom}(Y, Z). g \circ f = h \circ f \implies g = h$$

```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[sep=large]
X && Y && Z
\arrow["f", two heads, from=1-1, to=1-3]
\arrow["g"', shift right=1, from=1-3, to=1-5]
\arrow["h", shift left=1, from=1-3, to=1-5]
\end{tikzcd}
\end{document}
```

## Examples
- In [[category of sets]] they are surjective functions. But in algebraic categories it might not work.