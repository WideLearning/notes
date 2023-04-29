# SAT terminology
From [[time complexity]]
$\physics$
## Definition
- An atomic Boolean formula has form $A_{i}$ with $i \in \N$.
- A Boolean formula is a logic expression that uses atomic Boolean formulas.
- An assignment is a function $\mathcal{A}: \mathrm{D} \to \{ 0, 1 \}$, where $\mathrm{D}$ is a set of some atomic Boolean formulas.
- We can extend such $\mathcal{A}$ to $\mathcal{A'}: \mathrm{E} \to \{ 0, 1 \}$, where $\mathrm{E}$ is a set of all formulas that can be built using atomic ones from $\mathrm{D}$.
- We say that an assignment $\mathcal{A}$ is suitable for a formula $F$ if $\mathcal{A}$ is defined for all atomic formulas in $F$.
- And $F$ holds under $\mathcal{A}$ if $\mathcal{A'}(F) = 1$, such $\mathcal{A}$ is called a model for $F$. It is denoted $A \models F$.
- A formula $F$ is satisfiable if it has at least one model. Otherwise it is unsatisfiable.
- There is a language $SAT = \{ \ev{F} \mid F \text{ is a satisfiable Boolean formula}\}$.