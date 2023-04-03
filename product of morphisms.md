# product of morphisms
From [[constructions and operations in category theory]]
$\physics$
## Definition
The product $f_{1} \times f_{2}: A_{1}\times A_{2} \to B_{1}\times B_{2}$ of $f_{1}: A_{1}\to B_{1}$ and $f_{2}: B_{1}\to B_{2}$ is the unique functor making the following diagram commute:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd} {A_1} && {A_1 \times A_2} && {A_2} \\ \\ {B_1} && {B_1 \times B_2} && {B_2} \arrow["{f_1 \times f_2}", dashed, from=1-3, to=3-3]
\arrow["{p_1}"', from=1-3, to=1-1]
\arrow["{p_2}", from=1-3, to=1-5]
\arrow["{q_1}", from=3-3, to=3-1]
\arrow["{q_2}"', from=3-3, to=3-5]
\arrow["{f_1}"', from=1-1, to=3-1]
\arrow["{f_2}", from=1-5, to=3-5]
\end{tikzcd}
\end{document}
```

## Proof
To see that the product exists and is unique, consider another version of this diagram:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
 && {A_1 \times A_2} &&  \\
\\
{B_1} && {B_1 \times B_2} && {B_2}
\arrow["{f_1 \times f_2}", dashed, from=1-3, to=3-3]
\arrow["{f_1 \circ p_1}"', from=1-3, to=3-1]
\arrow["{f_2 \circ p_2}", from=1-3, to=3-5]
\arrow["{q_1}", from=3-3, to=3-1]
\arrow["{q_2}"', from=3-3, to=3-5]
\end{tikzcd}
\end{document}
```
Here the morphism in the middle comes from the definition of [[categorical product]], which says that it exists and is unique.

## Properties
- $q_{i} \circ \qty(\prod f) = f_{i} \circ p_{i}$