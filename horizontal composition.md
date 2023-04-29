# horizontal composition
From [[natural transformation]]

## Definition
Consider functors $F, F': \cat{A} \to \cat{B}$ and $G, G': \cat{B} \to \cat{C}$ and [[natural transformation|natural transformations]] $\alpha: F \to F', \beta: G \to G'$.  Then we can construct $\gamma: GF \to G'F'$ such that the following diagram commutes:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=huge] GFA && {G'FA} \\ \\ {GF'A} && {G'F'A} \arrow["{\beta_{FA}}", from=1-1, to=1-3] \arrow["{\beta_{F'A}}", from=3-1, to=3-3] \arrow["{G\alpha_{A}}"', from=1-1, to=3-1] \arrow["{G'\alpha_{A}}", from=1-3, to=3-3] \arrow["{(\beta \bullet \alpha)_{A}}"{description}, from=1-1, to=3-3] \end{tikzcd}
\end{document}
```
The square commutes by naturality of $\beta$ applied to $\alpha_{A}: FA \to F'A$, so we can take its diagonal to be the desired composition:
$$\beta \bullet \alpha = G' \alpha \circ \beta F = \beta F' \circ G \alpha$$

## Proof of naturality
Consider the following diagram:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=huge] GFA && {GF'A} && {G'F'A} \\ \\ GFB && {GF'B} && {G'F'B} \arrow["{\beta_{F'A}}", from=1-3, to=1-5] \arrow["{G\alpha_{A}}", from=1-1, to=1-3] \arrow["GFf", from=1-1, to=3-1] \arrow["{GF'F}"', from=1-3, to=3-3] \arrow["{G'F'f}", from=1-5, to=3-5] \arrow["{G\alpha_{B}}", from=3-1, to=3-3] \arrow["{\beta_{F'B}}", from=3-3, to=3-5] \end{tikzcd}
\end{document}
```
Left part is the image of commutative square for $\alpha$ applied to $f$ under functor $G$, so it’s still commutative. And the second is just the commutative square for $\beta$ applied to $F'f$. The rectangle as a whole proves naturality of the horizontal composition.

## Properties
- If we identify [[functor]] $F: \cat{A} \to \cat{B}$ with [[natural transformation]] $\id_{F}: F \to F$ then:
	- For $G, G': \cat{B} \to \cat{C}$ and $\alpha: G \to G'$, $\alpha_{FA} = (\alpha F)_{A} = (\alpha \bullet \id_{F})_{A}$
	- For $G, G': \cat{C} \to \cat{A}$ and $\alpha: G \to G'$, $F\alpha_{A} = (F\alpha)_{A} = (\id_{F} \bullet \alpha)$
- Similar trick is used in [[natural transformation for bifunctors]]. The only difference is that there we had a product of functors and here we have a composition.