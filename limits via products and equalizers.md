# limits via products and equalizers
From [[categorical limit]]
$\physics$
## Statement
If in a category finite [[categorical product]] and [[equalizer]] always exists, any finite limit exists.

## Notation
$D$ is a diagram of graph $\ev{V, E}$
$D(v), D(e)$ mapping from vertices and edges of graph to objects and morpisms
$s(e), t(e)$ are domain and codomain of $e$
$\pi_{v}$ is a morphism from cone to $v$

## Proof
First, we just take the product of all objects in $D$, call it $X$. But it might not work, because triangles like that
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
won’t commute.

We want something like [[equalizer]], but with many pairs of functions: $\forall e \in E: \pi_{t(e)} = D(e) \circ \pi_{s(e)}$. We can equalize their product. So, consider [[equalizer]] of $\ev{\pi_{t(e)}}_{e \in E}$ and $\ev{D(e) \circ \pi_{s(e)}}_{e \in E}$. Call this equalizer $e: P \to X$. 

Now $P$ is the required limit and $\pi_{v} \circ e$ are projections.