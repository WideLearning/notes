# categorical cone
From [[constructions and operations in category theory]]
$\physics$
## Definition
Suppose $G = \ev{V, E}$ is a graph and $D$ is a diagram of $G$ in $C$. Diagram means mapping of vertices to objects and edges to morphisms. Then object $A$ together with morphisms $\pi_{v}: A \to D(v)$  to the objects of diagram is called a cone for $D$ if all triangles in this cone commute:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
A && \\
\\
{D(s(e))} & & {D(t(e))}
\arrow["{\pi_{s(e)}}", from=1-1, to=3-1]
\arrow["{\pi_{t(e)}}"', from=1-1, to=3-3]
\arrow["{D(e)}", from=3-1, to=3-3]
\end{tikzcd}
\end{document}
```

## Another definition
Let’s say that diagram is a [[functor]] $D: I \to C$, where $I$ is the category that we use as a pattern. Then a cone is a [[natural transformation]] from $\Delta_{A}$ (constant functor that collapses whole diagram into $A$) to $D$.

## Properties
- With universal property it becomes [[categorical limit]].