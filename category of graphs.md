# category of graphs
From [[category]]
$\physics$
## Definition
Graph is either $(V, E, dom, cod: E \to V)$ or $(V, E: V \times V \to \mathrm{Set})$ (which is equivent).
$$\mathrm{Hom}((V_{1}, E_{1}), (V_{2}, E_{2})) = \{ (f, g) \mid f: V_{1} \to V_{2}, g: E_{1} \to E_{2}, ok(f, g) \}$$
where $ok(f, g)$ means that the following commutes
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd} {V_1} && {E_1 } && {V_1} \\ \\ {V_2} && {E_2} && {V_2} \arrow["g", from=1-3, to=3-3] \arrow["f", from=1-1, to=3-1] \arrow["f", from=1-5, to=3-5] \arrow["dom"', from=1-3, to=1-1] \arrow["dom"', from=3-3, to=3-1] \arrow["cod", from=1-3, to=1-5] \arrow["cod", from=3-3, to=3-5] \end{tikzcd}
\end{document}
```

## Properties
- [[categorical product]] is graph with $V = V_{1} \times V_{2}$, $E = \{ (a, b) \to (c, d) \mid (a, c) \in E_{1}, (b, d) \in E_{2} \}$
- [[coproduct]] is again disjoint union, [[pushout]] is union with some vertices merged
- [[exponential for graphs]]