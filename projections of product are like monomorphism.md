# projections of product are like monomorphism
From [[categorical product]] and [[monomorphism]]
$\physics$ 
## Statement
$$\ev{\pi_{a}, \pi_{b}} \circ f = \ev{\pi_{a}, \pi_{b}} \circ g \implies f = g$$
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd} X \\ & {A \times B} && B \\ \\ & A \arrow["{\pi_{a}}"', from=2-2, to=4-2] \arrow["{\pi_b}", from=2-2, to=2-4] \arrow["f"', shift right=1, from=1-1, to=2-2] \arrow["g", shift left=1, from=1-1, to=2-2] \end{tikzcd}
\end{document}
```