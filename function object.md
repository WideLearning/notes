# function object
From [[constructions and operations in category theory]]

## Definition
We call $Z = B^{A}$ if there is $ev: Z \times A \to B$ and for any other candidate $\Gamma$ with $g$ there is unique $f: \Gamma \to Z$ that factorizes $g$ through $ev$.


```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
	{\Gamma \times A} \\
	\\
	{B^A \times A} && B
	\arrow["{\exists! f \times \mathrm{id}_A}", dashed, from=1-1, to=3-1]
	\arrow["g", from=1-1, to=3-3]
	\arrow["ev", from=3-1, to=3-3]
\end{tikzcd}
\end{document}
```

It is also called [[exponential]].

## Currying
We have $g: \Gamma \times A \to B$ and want $f: \Gamma \to B^{A}$. But it is just universal property from the definition above.

## Unurrying
For a morphism $f: \Gamma \to B^{A}$ we can build its uncurried version as on the diagram above: $g = ev \circ (f, \mathrm{id}_{A})$

So we have $\mathrm{Hom}(\Gamma, B^{A}) \simeq \mathrm{Hom}(\Gamma \times A, B)$.