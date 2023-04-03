# generalized nondeterministic finite automaton
From [[finite automaton]]
$\physics$
## Definition
A GNFA is defined by
1. $Q$: a finite set, states
2. $\Sigma$: a finite set, alphabet
4. $\delta$: a [[map]] $Q \times Q \to R$ where $R$ denotes all [[regular expression|regular expressions]] over $\Sigma$
5. $q_{start}, q_{accept} \in Q$: start and accepting states ($\delta(\dots, q_{start}), \delta(q_{accept}, \dots)$ not defined)

It accepts string $s$ iff:
$$\exists a_{[n]} \in \Sigma^{*}, c_{[n+1]} \in Q. 
\sum\limits a = s,\ c_{0} = q_{start},\ c_{n+1} = q_{accept}, \qty(\forall i \in [n].
a_{i} \in L\qty\big(\delta(c_{i}, c_{i + 1})))$$
In other words, we can split a given string into arbitrary (possible parts) and select a path from the start state to the accepting state such that $i$-th part will be accepted by the language described by regexp on $i$-th edge.

## Properties
- [[FA can be converted to GNFA]]
- [[GNFA can be converted to regular expression]]