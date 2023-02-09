# regular languages are closed under concatenation
From [[regular language]]
$\physics$
## Statement
Suppose $A, B$ are [[regular language|regular languages]], then the language $A \circ B = \{ s_{a}s_{b} \mid s_{a} \in A, s_{b} \in B \}$ is also regular.

## Proof
Because [[FA and NFA are equivalent]], consider NFAs $M_{A}, M_{B}$ that recognize $A, B$ correspondingly. Connect all accepting states of $M_{A}$ with $\varepsilon$-transitions to the start state of $M_{B}$, consider the start state of $M_{A}$ as the new start state and the accepting states of $M_{B}$ as the new accepting states.