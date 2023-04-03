# if morphism
From [[boolean object]]
$\physics$
## Definition
For any object $C$ consider its product with itself: $(C \times C, \pi_{1}, \pi_{2})$. Then there is a unique $\mathrm{if}: \mathrm{Bool} \times (C \times C) \to C$ that factorizes $\pi_{1}$ and $\pi_{2}$ through $(\mathrm{true} \circ !, \mathrm{id})$ and $(\mathrm{false} \circ !, \mathrm{id})$ correspondingly:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
{C \times C} & & {C \times C} &\\
{\mathrm{Bool} \times (C \times C)} & C & \mathrm{Bool} \times (C \times C) & C\\
\arrow["{(\mathrm{true} \circ !, \mathrm{id})}"', from=1-1, to=2-1]
\arrow["\pi_1", from=1-1, to=2-2]
\arrow["{\mathrm{if}}"', dashed, from=2-1, to=2-2]
\arrow["{(\mathrm{false} \circ !, \mathrm{id})}"', from=1-3, to=2-3]
\arrow["\pi_2", from=1-3, to=2-4]
\arrow["{\mathrm{if}}"', dashed, from=2-3, to=2-4]
\end{tikzcd}
\end{document}
```

## Proof
Here $\mathrm{if}$ is the $h$ from [[boolean object]] definition, so it exists and unique by universal property of boolean object.

## Properties
- $\mathrm{if} \circ (\mathrm{true}, (a, b)) = a$, $\mathrm{if} \circ (\mathrm{false}, (a, b)) = b$