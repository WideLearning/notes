# alternative definition of category equivalence
From [[equivalent categories]]
$\physics$
## Statement
The following are equivalent:
1. $\cat{C}, \cat{D}$ are [[equivalent categories]].
2. There is a [[functor]] $F: \cat{C} \to \cat{D}$ which is [[complete functor]], [[faithful functor]] and [[essentially surjective functor]].

## Proof
$1 \implies 2$:
From definition of equivalent categories we have $F: \cat{C} \to \cat{D}, G: \cat{D} \to \cat{C}$ such that $F \circ G \cong \id_{\cat{D}}$ and $G \circ F \cong \id_{\cat{C}}$, denote the corresponding [[natural isomorphism]] $\alpha: (G \circ F) \to \id_{\cat{C}}$. Then $\forall X \in \ob(\cat{C}). GFX \cong X$ and same for $\cat{D}$, so $F$ is essentially bijective on objects.

Let’s prove that it’s faithful. Assume $\exists f, f' \in \hom_{\cat{C}}(X, Y). Ff = Ff'$. Then, because $G \circ F$ is natural:
$$f = \alpha_{Y} \circ (G F f)\circ \alpha_{X}^{-1} = \alpha_{Y} (G F f')\circ \alpha_{X}^{-1} = f'$$
We can also show that $G$ is faithful, in the same way.

Now, let’s show that $F$ is complete. For $g \in \hom_{\cat{D}}(FX, FY)$ define $f = \alpha_{Y} \circ G g \circ \alpha_{X}^{-1}$. 
```tikz
\usepackage{tikz-cd}
\tikzset{tail reversed/.code={\pgfsetarrowsstart{tikzcd to}}}
\begin{document}
\begin{tikzcd}[row sep=large]
	X && GFX && FX \\
	\\
	Y && GFY && FY
	\arrow["f", from=1-1, to=3-1]
	\arrow["Gg", from=1-3, to=3-3]
	\arrow["{\alpha_{X}}", from=1-3, to=1-1]
	\arrow["{\alpha_{Y}}", from=3-3, to=3-1]
	\arrow["g", from=1-5, to=3-5]
\end{tikzcd}
\end{document}
```
By naturality, $GF f = \alpha_{Y}^{-1} \circ f \circ \alpha_{X}$ and by construction $G g = \alpha_{Y}^{-1} \circ f \circ \alpha_{X}$, so $GF f = Gg$. And because $G$ is faithful, $Ff = g$. So $g$ has a preimage, and $F$ is surjective on $\hom_\cat{C}(X, Y)$.

$2 \implies 1$:
Because $F$ is essentially surjective, we can define a map $G: \ob(\cat{D}) \to \ob(\cat{C})$ such that $\forall X \in \ob(\cat{D}). X \cong FGX$. Denote this isomorphism $\alpha_{X}: FGX \to X$.

Because $F$ is complete and faithful, we can extend $G$ to morphisms uniquely by setting $G f = F^{-1}(\alpha_{Y}^{-1} \circ f \circ \alpha_{X})$.
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
	GX && X && FGX \\
	\\
	GY && Y && FGY
	\arrow["Gf", from=1-1, to=3-1]
	\arrow["f", from=1-3, to=3-3]
	\arrow["FGf", from=1-5, to=3-5]
	\arrow["{\alpha_{X}}"', from=1-5, to=1-3]
	\arrow["{\alpha_{Y}}"', from=3-5, to=3-3]
\end{tikzcd}
\end{document}
```
What is $G(\id_{X})$? In this case $\alpha_{Y} = \alpha_{X}$ (because $Y = X$), so $G(\id_{X}) = F^{-1}(\id_{FGX}) = \id_{GX}$.
And because $G(p \circ q)$ can be $G p \circ G q$, it must be, by uniqueness. So $G$ preserves $\id$ and composition, and is therefore a functor.
Moreover, $\alpha: F \circ G \to \id_{\cat{D}}$ is natural isomorphism by construction (commutative square is shown above). Let’s build $\beta: G \circ F \to \id_{\cat{C}}$. Because $F$ is complete and faithful, we can define $\beta_{Y}: GFY \to Y$ to be the preimage of $\alpha_{FY}: FGFY \to FY$ uniquely. Every $\beta_{Y}$ is an isomorphism, its inverse can be similarly defined as the preimage of $\alpha_{FY}^{-1}$. And $\beta$ is natural, because if we apply $F$ to the diagramm below, it will commute, and as $F$ is faithful, the original diagram must also commute:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large]
	GFX && X \\
	\\
	GFY && Y
	\arrow["{\beta_{X}}", from=1-1, to=1-3]
	\arrow["{\beta_{Y}}", from=3-1, to=3-3]
	\arrow["{GFf}", from=1-1, to=3-1]
	\arrow["f", from=1-3, to=3-3]
\end{tikzcd}
\end{document}
```