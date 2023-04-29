# adjoints preserve limits
From [[adjunction]] and [[categorical limit]]
$\physics$
## Statement
Left adjoint preserves every [[colimit]] and right preserves every [[categorical limit]].

## Proof
Enough to prove one part, the other is simply dual. Let’s prove about colimits.

Consider $F \dashv G$ where $F: \cat{C} \to \cat{D}, G: \cat{D} \to \cat{C}$. Also let $L = \mathrm{colim} D$ where $D: \cat{J} \to \cat{C}$ and $\cat{J}$ on the picture below consists of $A, B$.

```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large] A && DA &&&& FDA \\ &&& L & GX &&& FL & X \\ B && DB &&&& FDB \arrow[from=1-1, to=3-1] \arrow[from=1-3, to=3-3] \arrow[from=1-7, to=3-7] \arrow[from=1-3, to=2-4] \arrow[from=3-3, to=2-4] \arrow[from=1-7, to=2-8] \arrow[from=3-7, to=2-8] \arrow[dashed, from=2-8, to=2-9] \arrow[from=1-7, to=2-9] \arrow[from=3-7, to=2-9] \arrow[from=1-3, to=2-5] \arrow[from=3-3, to=2-5] \arrow[dashed, from=2-4, to=2-5] \end{tikzcd}
\end{document}
```

First, we can apply $F$ to the whole cone $L$ and it will be a cone in $\cat{D}$, still commuting because functors preserve composition. Suppose there is another cone in $\cat{D}$, from $FD$ to $X$. Then we can find $GX$ in $\cat{C}$ and it will also be a cone. By universality of $L$, there will be a unique arrow $L \to GX$. $F \dashv G$ means $\hom(L, GX) \cong \hom(FL, X)$, so there will be a unique arrow $FL \to X$ as well. Then $FL = \mathrm{colim} FD$.

## Alternative proof
Here for limits: $L = \lim D$.
Because [[covariant hom-functor preserves limits]]:
$$\hom(-, GL) \cong \hom(F-, L) \cong \lim \hom(F-, D) \cong \lim \hom(-, GD)$$
By taking a [[vertical composition]] of these natural isomorphisms:
$$\hom(-, GL) \cong \lim \hom(-, GD)$$
