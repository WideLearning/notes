# regular languages are closed under union
From [[regular language]]
$\physics$
## Statement
Suppose $A, B$ are [[regular language|regular languages]], then the language $A \cup B = \{ s \mid s \in A \vee s \in B \}$ is also regular.

## Proof
Because [[FA and NFA are equivalent]], consider NFAs $M_{A}, M_{B}$ that recognize $A, B$ correspondingly. Now create a new state $x$ that will be the start state and a new state $y$ that will be the only accepting state. Now connect $x$ by $\varepsilon$-transitions with the start states of $M_{A}, M_{B}$ and connect the accepting states of those by $\varepsilon$-transitions with $y$.