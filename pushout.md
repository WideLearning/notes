# pushout
From [[constructions and operations in category theory]]

## Definition
A [[pullback]] in [[opposite category]]. In other words, it is the following [[colimit]]:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
	{A \otimes_{C} B} && B \\
	\\
	A && C
	\arrow[from=3-3, to=3-1]
	\arrow[from=3-3, to=1-3]
	\arrow[from=3-1, to=1-1]
	\arrow[from=1-3, to=1-1]
\end{tikzcd}
\end{document}
```

## Properties
- Pushouts in [[category of sets]] are related to quotient sets.