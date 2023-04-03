# nondeterministic finite automaton
From [[finite automaton]]
$\physics$
## Definition
An NFA is defined by
1. $Q$: a finite set, states
2. $\Sigma$: a finite set, alphabet
3. $\delta$: a [[relation]] on $Q \times \Sigma_{\varepsilon} \times Q$, transition function ($\Sigma_{\varepsilon} = (\Sigma \cup \{ \varepsilon \})$)
4. $q_{0}$: element of $Q$, start state
5. $F$: subset of $Q$, accepting states

It accepts string $s$ iff:
$$\exists a_{[n]} \in \Sigma_{\varepsilon}. \left(
\sum\limits a = s,
\exists c_{[\abs{s}]}. 
\qty(c_{0} = q_{0}, \forall i \in [\abs{s} - 1].
\delta(c_{i - 1}, s_{i}, c_{i}))\right)$$

So it is a [[finite automaton]] where each pair of state and symbol can have more than one possible transition, or transition. And also there are transitions that can be taken without reading a symbol.

## Properties
- [[FA and NFA are equivalent]]