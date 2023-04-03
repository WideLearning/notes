# FA can be converted to GNFA
From [[finite automaton]], [[generalized nondeterministic finite automaton]]
$\physics$
## Statement
Every FA has an equivalent GNFA.

## Proof
Because GNFAs have stricter conditions on start and accepting states, let’s create new $q_{start}, q_{accept}$, connect $q_{start}$ to $q_{0}$ and all previous accepting states to $q_{accept}$ by $\varepsilon$-transitions. For each pair of states we replace all edges between them (in one direction) with the corresponding regexp (which might be empty, if there were no edges, for example).