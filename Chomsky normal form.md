# Chomsky normal form
From [[context-free grammar]]
$\physics$
## Definition
A [[context-free grammar]] is in Chomsky normal form if every rule is in one of the three forms:
1. $A \to BC$ where $A \in V$ and $B, C \in V \setminus S$
2. $A \to a$ where $A \in V, a \in \Sigma$
3. $S \to \varepsilon$ where $S$ is start variable

## Proof of existence
Add new start $S'$ add $S' \to S$. Now we don’t have $S'$ in the right-hand sides of rules.
Now we eliminate $\varepsilon$-rules. Select any $A \to \varepsilon$. Remove this rule, then for all rules add posibility of omitting $A$: if there was $R \to aAbAc$, add also $R \to abc$, $R \to aAbc$, $R \to abAc$. And if there was $R \to A$, we would like to add $R \to \varepsilon$, but can’t, so run the same elimination for $R$ (if not already).

Now unit rules. For any $A \to B$ remove it and add $A \to C$ for all $B \to C$ (here $C$ can be either variable or terminable). Repeat. In case of cycles you might get $A \to A$ at some point, which can be dismissed.

Finally, replace rules like $A \to BcDe$ with $A \to BCDE, C \to c, E \to e$. Now we can replace $A \to B_{1} B_{2} \dots$ with $A \to B_{1}A', A' \to B_{2}\dots$ until all rules are at most binary.