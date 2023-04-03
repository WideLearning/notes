# multitape Turing machine
From [[Turing machine]]
$\physics$
## Definition
Just like [[Turing machine]], but can read symbols from $k$ tapes, write symbols to $k$ tapes and move $k$ heads in one turn. Defined by:
- $Q$: states
- $\Sigma$: input alphabet
- $\Gamma$: tape alphabet
- $\delta: Q \times \Gamma^{k} \to Q \times \Gamma^{k} \times \{ L, R \}^{k}$: transition function
- $q_{0} \in Q$: start state
- $q_{accept}, q_{reject} \in Q$: accepting and rejecting states

## Properties
- [[multitape Turing machine can be simulated in quadratic time and linear space]]