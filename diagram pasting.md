# diagram pasting
From [[commutative diagram]]
$\physics$
## Statement
If we have two commutative diagrams and juxtapose them on a subgraph where there is a path (at least in some direction) between any pair of objects we get a commutative diagram.

## Proof
To check commutativity we need to show for two arbitrary objects $X$, $Y$ and two arbitrary paths from $X$ to $Y$ that the composition of morphisms in each paths gives the same result. Let’s denote the objects as follows:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd} &&&& {A_n} && {M_1} && {C_1} \\ && {...} &&&&&&&& {...} \\ & {A_1} &&&&& {M_2} &&&&& {C_n} \\ \\ X &&&&&& {...} &&&&&& Y \\ \\ & {B_1} &&&&& {M_{n-1}} &&&&& {D_n} \\ && {...} &&&&&&&& {...} \\ &&&& {B_n} && {M_n} && {D_1} \arrow[from=5-1, to=3-2] \arrow[from=3-2, to=2-3] \arrow[from=2-3, to=1-5] \arrow[from=1-5, to=1-7] \arrow[from=1-7, to=3-7] \arrow[from=3-7, to=5-7] \arrow[from=5-7, to=7-7] \arrow[from=7-7, to=9-7] \arrow[from=5-1, to=7-2] \arrow[from=7-2, to=8-3] \arrow[from=8-3, to=9-5] \arrow[from=9-5, to=9-7] \arrow[from=9-7, to=9-9] \arrow[from=9-9, to=8-11] \arrow[from=8-11, to=7-12] \arrow[from=7-12, to=5-13] \arrow[from=1-7, to=1-9] \arrow[from=1-9, to=2-11] \arrow[from=2-11, to=3-12] \arrow[from=3-12, to=5-13] \end{tikzcd}
\end{document}
```


Here $M_{i}$ are the objects from the subgraph on which we connected the diagrams. $X$ and $Y$ come from different parts, because otherwise we already know that paths between them commute. And there is a path from the $M_{1}$ (object where the first path meets the subgraph for the first time) and $M_{n}$ (where the second path meets it), because there is a path between any pair of objects in subgraph.

Note that $X \leadsto M_{1} \leadsto M_{n}$ is equivalent to $X \leadsto B_{1} \dots B_{n} \leadsto M_{n}$. Similarly $M_{1} \leadsto M_{n}\leadsto Y$ is equivalent to $M_{1} \leadsto C_{1} \dots C_{n} \leadsto Y$. So both paths are equivalent to $X \leadsto M_{1} \leadsto M_{n} \leadsto Y$.

## Example where connectivity is not enough
Here each morphism is uniquely determined by its domain, codomain and weight. Composition sums weights. As shown in this example, $ABCD$ and $BCDE$ separately are commutative, but as a whole it is not a commutative diagram, because $ABE$ and $ACE$ have different weight sums.
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd} &&&& B \\ A &&&&&&& E \\ &&& C \\ \\ \\ &&&& D \arrow["1"{description}, from=2-1, to=1-5] \arrow["{-1}"{description}, from=2-1, to=3-4] \arrow["3"{description}, from=3-4, to=2-8] \arrow["5"{description}, from=1-5, to=2-8] \arrow["1"{description}, from=3-4, to=6-5] \arrow["{-1}"{description}, from=1-5, to=6-5] \arrow["0"{description}, from=2-1, to=6-5] \end{tikzcd}
\end{document}
```