# pushdown automaton
From [[formal languages]]
$\physics$
## Definition
A PDA is defined by:
1. $Q$: finite set of states
2. $\Sigma$: input alphabet
3. $\Gamma$: stack alphabet
4. $\delta$: $Q \times \Sigma_{\varepsilon} \times \Gamma_{\varepsilon} \to 2^{Q \times \Gamma_{\varepsilon}}$, transition function
5. $q_{0} \in Q$: start state
6. $F \subset Q$: accepting states

In other words, it is a [[nondeterministic finite automaton]] with infinite stack.
Transition functions works as follows: transition $\delta(v, a, b) \ni (u, c)$ means that if we are in state $v$, have $a$ on the tape and $b$ on the stack, we go to $u$, remove $b$ from the stack and put $c$ there. Special cases: $a = \varepsilon$ means purely interacting with stack, $b = \varepsilon$ means only pushing symbol onto the stack, $c = \varepsilon$ means popping from the stack.

It accepts $w$ iff exist $r_{[m]} \in Q, s_{[m]} \in \Gamma^{*}$ (sequences of states and stack contents) and $y_{[m]} \in \Sigma_{\varepsilon}^{*}$:
1. $w = y_{1}y_{2}\dots y_{m}$
1. $r_{1} = q_{0}, s_{1} = \varepsilon$
2. $\forall i \in [m-1]. \qty\big(\delta(r_{i}, y_{i}, a) \in (r_{i+1}, b) \wedge (\exists t \in \Gamma^{*}. s_{i} = at \wedge s_{i} = bt))$
3. $r_{m} \in F$

Here $abc$ means stack with $a$ on top and $c$ at the bottom.

## Properties
- [[extended pushdown automaton]]
- [[modified pushdown automaton]]
- [[PDA are equivalent to ePDA]]
- [[mPDA are equivalent to PDA]]
- [[pushdown automata and context-free languages are equivalent]]