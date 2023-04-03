# universal morphism
From [[universal property]]
$\physics$
## Definition
Consider a [[functor]] $S: D \to C$ and $c \in \mathrm{Ob}(C)$. A universal morphism from $c$ to $S$ is a pair $\ev{r, u}$ where $r \in \mathrm{Ob}(D)$ and $u \in \mathrm{Hom}(c, Sr)$ with the following property: 
$$\forall d \in \mathrm{Ob}(D), f \in \mathrm{Hom}_{C}(c, Sd).  \exists! f' \in \mathrm{Hom}_{D}(r, d). f = Sf' \circ u$$
In other words, each morphism $f: c \to Sd$ factors uniquely through $u$.  
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd} r & c && Sr \\ \\ d &&& Sd \arrow["{Sf'}", from=1-4, to=3-4] \arrow["u", from=1-2, to=1-4] \arrow["f"', from=1-2, to=3-4] \arrow["{f'}"', from=1-1, to=3-1] \end{tikzcd}
\end{document}
```

## Examples
- [[bases of vector space as universal morphism]]