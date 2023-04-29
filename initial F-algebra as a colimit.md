# initial F-algebra as a colimit
From [[algebra over an endofunctor]]
$\physics$
## Statement
In “nice enough” categories we can define initial $F$-algebra as the (sequential) [[colimit]] of the following diagram:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large] 0 && F0 && FF0 && FFF0 \arrow["{!_{F0}}", from=1-1, to=1-3] \arrow["{F!_{F0}}", from=1-3, to=1-5] \arrow["{FF!_{F0}}", from=1-5, to=1-7] \end{tikzcd}
\end{document}
```
