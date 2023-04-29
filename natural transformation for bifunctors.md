# natural transformation for bifunctors
From [[natural transformation]]
$\physics$
## Statement
Suppose we have [[bifunctor|bifunctors]] $F, G: C \times D \to A$. Then $\alpha: F \to G$ is a [[natural transformation]] if it is natural in both arguments.
For example, naturality of $\alpha$ in first argument would mean:
$$\forall f \in \hom_{\cat{C}}(A, C), B \in \ob(\cat{D}). G(f, \id_{B}) \circ \alpha_{A, B} = \alpha_{C, B} \circ F(f, \id_{B})$$

## Proof
We decompose the commutative square that we need to prove into two squares, where at first stage we change only the first component and then only the second. 
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large] {F(A, B)} && {G(A, B)} \\ \\ {F(C, B)} && {G(C, B)} \\ \\ {F(C, D)} && {G(C, D)} \arrow["{\alpha_{A, B}}", from=1-1, to=1-3] \arrow["{\alpha_{C, B}}", from=3-1, to=3-3] \arrow["{\alpha_{C, D}}", from=5-1, to=5-3] \arrow["{F(f, \mathrm{id})}"', from=1-1, to=3-1] \arrow["{G(f, \mathrm{id})}", from=1-3, to=3-3] \arrow["{F(\mathrm{id}, g)}"', from=3-1, to=5-1] \arrow["{G(\mathrm{id}, g)}", from=3-3, to=5-3] \end{tikzcd}
\end{document}
```
Now each of the squares means naturality in one of the arguments, and by gluing them we get the commutativity of the original square.

## Properties
- Similar trick in [[horizontal composition]].