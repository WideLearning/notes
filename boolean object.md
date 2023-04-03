# boolean object
From [[constructions and operations in category theory]]
$\physics$
## Definition
In $\mathrm{Set}$ it is just $1 \sqcup 1$ ($1$ is $\mathrm{Unit}$, [[terminal object]] in $\mathrm{Set}$). In general, we want a stronger condition.

Suppose finite products exist in $\mathrm{C}$. Boolean object is object $\mathrm{Bool}$ together with morphisms $\mathrm{true}, \mathrm{false}: 1_{\mathrm{C}} \to \mathrm{Bool}$ with following condition:
$$\forall f, g \in \mathrm{Hom}(A, B). \exists! h \in \mathrm{Hom}(A \times Bool, B ). \begin{cases} f = h \circ (\mathrm{true} \circ !_{A}, \mathrm{id}_{A})\\
g = h \circ (\mathrm{false} \circ !_{A}, \mathrm{id}_{A})\\ \end{cases}$$
For any $f, g: A \to B$ there is unique $h: A \times \mathrm{Bool} \to B \times \mathrm{Bool}$ such that
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd} A && {\mathrm{Bool} \times A} && A && {\mathrm{Bool} \times A} \\ \\ && B &&&& B \arrow["f"', from=1-1, to=3-3] \arrow["{(\mathrm{true} \circ !_A, \mathrm{id}_A)}", from=1-1, to=1-3] \arrow["h", dashed, from=1-3, to=3-3] \arrow["{(\mathrm{false} \circ !_A, \mathrm{id}_A)}", from=1-5, to=1-7] \arrow["g"', from=1-5, to=3-7] \arrow["h", dashed, from=1-7, to=3-7] \end{tikzcd}
\end{document}
```

## Properties
- $\mathrm{Bool} \simeq 2$, to see that take $A = 1$ (and $\mathrm{Bool} \times 1 \simeq 1$).
- In [[category of groups]] we have $2 \simeq 1$.
- Only for [[preorder]] we have $\mathrm{Bool} \simeq 1$ (and it always exists).
- [[if morphism]]