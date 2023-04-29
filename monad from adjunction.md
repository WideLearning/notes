# monad from adjunction
From [[monad]] and [[adjunction]]
$\physics$
## Statement
Consider an [[adjunction]] $(F: \cat{X} \to \cat{A}, G: \cat{A} \to \cat{X}, \eta, \varepsilon)$.
- It provides an [[endofunctor]] $T = G \circ F$
- Unit $\eta: \id_{X} \to T$ of this monad is the [[unit of adjunction]] (hence the name) 
- Operation $\mu: T \circ T \to T$ is given by [[horizontal composition]] $\mu = G \varepsilon F = \id_{G} \bullet \varepsilon \bullet \id_{F}$.

## Proof
The associativity law takes the following form:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=huge] GFGFGF && GFGF \\ \\ GFGF && GF \arrow["{G\varepsilon FGF}"', from=1-1, to=3-1] \arrow["{GFG \varepsilon F}", from=1-1, to=1-3] \arrow["{G\varepsilon F}"', from=3-1, to=3-3] \arrow["{G\varepsilon F}", from=1-3, to=3-3] \end{tikzcd}
\end{document}
```
If we trim first and last letters, transpose the diagram and add instantiate it for a specific object $A$:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=huge] FGFGA && FGA \\ \\ FGA && A \arrow["{\varepsilon_{FGA}}", from=1-1, to=1-3] \arrow["{FG \varepsilon_{A}}"', from=1-1, to=3-1] \arrow["{\varepsilon_{A}}", from=1-3, to=3-3] \arrow["{\varepsilon_{A}}"', from=3-1, to=3-3] \end{tikzcd}
\end{document}
```
Which is just a naturality condition for $\varepsilon$ applied to $\varepsilon_{A}: FGA \to A$. And the diagram above follows from it, because we can always prepend more functors from either end without losing commutativity.

The unit laws:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=huge] GF && GFGF \\ \\ GFGF && GF \arrow["{\mathrm{id}_{GF}}"{description}, from=1-1, to=3-3] \arrow["{G \varepsilon F}"', from=3-1, to=3-3] \arrow["{G \varepsilon F}", from=1-3, to=3-3] \arrow["{GF \eta}", from=1-1, to=1-3] \arrow["{\eta GF}"', from=1-1, to=3-1] \end{tikzcd}
\end{document}
```
Which follow from [[triangle identities for adjunction]] by adding (to the triangle identities) $G$ in the upper triangle and $F$ in the lower one.