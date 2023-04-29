# verifier
From [[time complexity]]
$\physics$
## Definition
A verifier for language $A$ is a decider for language $V$ which has the following property:
$$w \in A \iff \exists c. \ev{w, c} \in V$$
In other words, for each $w \in A$ there is a certificate $c$ such that $\ev{w, c}$ is accepted by verifier, and for $w \notin A$ there is no such $c$, that is, all $\ev{w, c}$ will be rejected.