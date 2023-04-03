# NTM can be simulated by TM
From [[Turing machine]] and [[nondeterministic Turing machine]]
$\physics$
## Statement
For a [[nondeterministic Turing machine]] $M$ there is a [[Turing machine]] $S$ that recognizes the same language and produces the same output as one of the halting computations for $M$, if such exists.

## Proof
Consider the tree of computations for $M$. Denote the maximum out-degree by $d$. Note that any computation (=path in this tree) corresponds to a (finite) string over $\{ 1, 2, \dots, d \}$.

So we create a [[multitape Turing machine]] $T$ with three tapes:
- Original input to the $M$ that we don’t change
- Tape content for the current node of the tree
- Address of the tree node

Then we iterate over all address strings (even invalid) first by length and then lexicographically. For example, for $d = 3$:
``, `1`, `2`, `3`, `11`, `12`, `13`, `21`, `22`, ...

For each of them copy input to the simulation tape. Then follow the rules of $M$, using symbols from address tape to resolve non-deterministic transitions. If at some point the character in address is invalid, go to the next address. If reached accepting state, accept. If the computation ended (= there are no more characters in address) or reached rejecting state, go to the next address.