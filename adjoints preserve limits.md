# adjoints preserve limits
From [[adjoint functors]]
$\physics$
## Statement
Left adjoint preserves every [[colimit]] and right preserves every [[categorical limit]].

## Proof
Enough to prove one part, the other is simply dual. Let’s prove about colimits.

Consider $F \dashv G$ where $F: \cat{C} \to \cat{D}, G: \cat{D} \to \cat{C}$.
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large] A && DA &&&& FDA \\ &&& L & GX &&& FL & X \\ B && DB &&&& FDB \arrow[from=1-1, to=3-1] \arrow[from=1-3, to=3-3] \arrow[from=1-7, to=3-7] \arrow[from=1-3, to=2-4] \arrow[from=3-3, to=2-4] \arrow[from=1-7, to=2-8] \arrow[from=3-7, to=2-8] \arrow[dashed, from=2-8, to=2-9] \arrow[from=1-7, to=2-9] \arrow[from=3-7, to=2-9] \arrow[from=1-3, to=2-5] \arrow[from=3-3, to=2-5] \arrow[dashed, from=2-4, to=2-5] \end{tikzcd}
\end{document}
```