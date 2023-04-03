# Turing machine
From [[formal languages]]
$\physics$
## Definition
A Turing machine is defined by:
1. $Q$: finite set of states
2. $\Sigma$: input alphabet, not containing blank symbol $B$
3. $\Gamma$: stack alphabet, $\Sigma \subset \Gamma, B \in \Gamma$.
4. $\delta$: $Q \times \Gamma \to Q \times \Gamma \times \{ L, R \}$: transition function
5. $q_{0} \in Q$: start state
6. $q_{accept} \in Q$: accepting state
7. $q_{reject} \in Q, q_{reject} \ne q_{accept}$: rejecting state

By running it on infinite in one direction tape where only a finite prefix of cells is not blank we get the output state of the tape (if the machine halts).

So now we can write $M(S) = T$ if the machine $M$ after running on $S$ ends up with $T$. We can interpret $S$ not as a single string but as a list of strings, encoding each argument as [[self-delimiting string]]. But what is $T$? The simplest output is just accept/reject. Or we can interpret the non-blank prefix in the end as output.

## Differences in definitions
- 4-tuple transition function might be used ($Q \times \Gamma \to Q \times (\Gamma \cup \{ L, R\})$, where the machine either writes new symbol or moves, but not both. 
- Input and stack alphabet can be the same.
- Tape might be infinite in both directions.



## Properties
- [[configuration of Turing machine]]
- [[universal Turing machine]]
- [[multitape Turing machine]], [[multitape Turing machine can be simulated in quadratic time and linear space]]
- [[nondeterministic Turing machine]], [[NTM can be simulated by TM]]
- [[monotone Turing machine]]
- [[canonical encoding of Turing machine]]
- [[RAM and TM are equivalent]]