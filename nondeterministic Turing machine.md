# nondeterministic Turing machine
From [[Turing machine]]
$\physics$
## Definition
A NTM machine is defined by:
1. $Q$: finite set of states
2. $\Sigma$: input alphabet, not containing blank symbol $B$
3. $\Gamma$: stack alphabet, $\Sigma \subset \Gamma, B \in \Gamma$.
4. $\delta$: $Q \times \Gamma \to 2^{Q \times \Gamma \times \{ L, R \}}$: transition function
5. $q_{0} \in Q$: start state
6. $q_{accept} \in Q$: accepting state
7. $q_{reject} \in Q, q_{reject} \ne q_{accept}$: rejecting state

Contrary to [[nondeterministic finite automaton]] there are no $\varepsilon$-transitions here, though we can always simulate them, because TMs can read any symbol multiple times and FA can’t.

## Properties
- [[NTM can be simulated by TM]]