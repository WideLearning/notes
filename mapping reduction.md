# mapping reduction
From [[theory of computability]]
$\physics$
## Definition
Let $A, B$ be languages over $\Sigma$. $A$ is mapping reducible to $B$ (also denoted $A \leq_{m} B$) if there is a total [[computable function]] $f: \Sigma^{*} \to \Sigma^{*}$ such that:
$$ w \in A \iff f(w) \in B$$

## Properties
- If $B$ is a [[decidable language]] then $A$ is too, because we can first map the input with $f$ and then run the decider for $B$. Conversely, if we reduced undecidable $A$ to another language $B$, $B$ must be also undecidable. We can use [[acceptance problem]] or [[halting problem]] for $A$.
- If $B$ is [[recursively enumerable language]] then $A$ is too. So reducing not enumerable language $A$ to another language $B$ proves that it is also not enumerable.
- $A \leq_{m} B \iff \bar{A} \leq_{m} \bar{B}$, where $\bar{A}$ means complement. 
- Now we can reduce $\bar{A}$ to $\bar{B}$ instead, where $\bar{A}$ might be [[acceptance problem]], for example.