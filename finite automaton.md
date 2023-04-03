# finite automaton
From [[formal languages]]
$\physics$
## Definition
A finite automaton is defined by:
1. $Q$: a finite set, states
2. $\Sigma$: a finite set, alphabet
3. $\delta$: a function from $Q \times \Sigma$ to $Q$, transition function
4. $q_{0}$: element of $Q$, start state
5. $F$: subset of $Q$, accepting states

It accepts string $s$ iff 
$$\exists c_{[\abs{s}]}. \qty(c_{0} = q_{0}, \forall i \in [\abs{s} - 1]. \delta(c_{i - 1}, s_{i}) = c_{i})$$

In other words, it is a [[Turing machine]] where the only action is to move right (no moving left, no writing).

## Properties
- A set of strings recognized by finite automata is a [[regular language]].
- Replacing “function” with “relation” gives [[nondeterministic finite automaton]]. [[FA and NFA are equivalent]].
- After that, replacing characters on edges with regexps gives [[generalized nondeterministic finite automaton]]. [[FA can be converted to GNFA]].