# Turing machine
From [[algorithmic information theory]]
$\physics$
A Turing machine is defined by a function from symbol (one of $n$ or blank) and state (one of $m$) to the new symbol, new state and whether to move left or right (or halt). Sometimes 4-tuple definition used, where the machine either writes new symbol or moves, but not both.

By running it on infinite in both directions tape where only a finite contiguous segent of cells is not blank we get the output state of the tape (if the machine halts).
So now we can write $M(S) = T$ if the machine $M$ after running on $S$ ends up with $T$. We can interpret $S$ not as a single string but as a list of strings, encoding each argument as [[self-delimiting string]]. But what is $T$? The simplest output is just accept/reject. Or a bit more general, the output is the state in which the machine halts. Or we can interpret all non-blank bits in the end as output.

Notation:
- $A$ — alphabet (usually including blank)
- $Q$ — set of states
- $q_{0}$ — initial state
- $F$ — final states (if needed)
- $\delta: Q \times A \to S \times Q$ — transition function, where in 4-tuple definition $S = A \cup \{ L, R \}$ and otherwise $S = A \times \{ L, R \}$.

Can be [[universal Turing machine]], [[multi-tape Turing machine]] and [[monotone Turing machine]]. Has [[canonical encoding of Turing machine]].