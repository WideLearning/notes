# regular languages are closed under Kleene star
From [[regular language]]
$\physics$
## Statement
Suppose $A$ is a [[regular language]]. Then $A^{\star} = \{ s_{1}s_{2}\dots s_{n} \mid n \geq 0, s_{i} \in A \}$ is also regular. 

## Proof
Because [[FA and NFA are equivalent]], consider NFAs $M_{A}$ that recognizes $A$. Connect its accepting states to the start state with $\varepsilon$-transitions and also make the start state accepting so that $\varepsilon$ is accepted.