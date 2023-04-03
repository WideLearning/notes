# FA and NFA are equivalent
From [[finite automaton]] and [[nondeterministic finite automaton]]
$\physics$
## Statement
A language is recognized by some [[finite automaton]] iff it is recognized by some [[nondeterministic finite automaton]].

## Proof
$\implies$:
Trivial, because an ordinary [[finite automaton]] is a [[nondeterministic finite automaton]] too, just because extra functionality.

$\impliedby$:
To check if a string $s$ is accepted by NFA, let’s track for each prefix of $s$ in which states NFA can get after reading it. Denote $g(q)$ the set of states reachable from state $q$ only by $\varepsilon$ transitions. Then initial set of states is $t_{0} = g(q_{0})$. And for each symbol we go from $t_{i}$ to $\bigcup\limits_{q_{i} \in t_{i}, \delta(q_{i}, s_{i}, q_{i+1})} g(q_{i+1})$. And we get a [[finite automaton]] where the states are subsets of states of the original NFA and the accepting states are those subsets which contain at least one accepting state.