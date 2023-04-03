# regular monomorphism
From [[monomorphism]]
$\physics$
## Definition
$f: X \to Y$ is a regular monomorphism iff it is an [[equalizer]] for some $Y \to Z$ morpisms.
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd} X && Y && Z \arrow["f", hook, from=1-1, to=1-3] \arrow[shift left=1, from=1-3, to=1-5] \arrow[shift right=1, from=1-3, to=1-5] \end{tikzcd}
\end{document}
```

## Properties
- [[split monomorphisms are regular]]