# extended pushdown automaton
From [[pushdown automaton]]
$\physics$
## Definition
A ePDA is defined by:
1. $Q$: finite set of states
2. $\Sigma$: input alphabet
3. $\Gamma$: stack alphabet
4. $\delta$: $Q \times \Sigma_{\varepsilon} \times \Gamma_{\varepsilon} \to 2^{Q \times \Gamma_{\varepsilon}^{*}}$, transition function
5. $q_{0} \in Q$: start state
6. $F \subset Q$: accepting states

In other words, it is a [[pushdown automaton]] which can write to the stack not only symbols, but strings.

It accepts $w$ iff exist $r_{[m]}, s_{[m]} \in \Gamma^{*}$ (sequences of states and stack contents) and $y_{[m]} \in \Sigma_{\varepsilon}^{*}$:
1. $w = y_{1}y_{2}\dots y_{m}$
1. $r_{1} = q_{0}, s_{1} = \varepsilon$
2. $\forall i \in [m-1]. \qty\big(\delta(r_{i}, y_{i}, a) \in (r_{i+1}, b) \wedge (\exists t \in \Gamma^{*}. s_{i} = at \wedge s_{i} = bt))$ ($b \in \Gamma^{*}$!)
3. $r_{m} \in F$

## Properties
- [[PDA are equivalent to ePDA]]