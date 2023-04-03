# pullback
From [[constructions and operations in category theory]], generalizes [[categorical product]] and [[equalizer]].

## Definition
It is the following [[categorical limit]]:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
	{A \times_{C} B} && B \\
	\\
	A && C
	\arrow[from=3-1, to=3-3]
	\arrow[from=1-3, to=3-3]
	\arrow[from=1-1, to=3-1]
	\arrow[from=1-1, to=1-3]
\end{tikzcd}
\end{document}
```

## Properties
- Two morphisms leading to $P = A \times_{C} B$ are equal if their compositions with $P \to A$ are equal and same for $P \to B$, by universal property of [[categorical limit]].
- Can be constructed via [[categorical product]] and [[equalizer]], as in [[limits via products and equalizers]].
- Generalizes preimages: $A \times_{C} B$ is the preimage of $B \subset C$ w.r.t. $f: A \to C$. $B \to C$ should be [[monomorphism]].
- Also generalizes set intersections: same construction, but $A \to C$ also should be [[monomorphism]].