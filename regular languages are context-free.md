# regular languages are context-free
From [[regular language]] and [[context-free language]]
$\physics$
## Statement
Any [[regular language]] is [[context-free language]].

## Proof
Because [[regular expressions describe regular languages]], any regular language can be described inductively by concatenation, union and Kleene star. And we can construct [[context-free grammar]] for all of these:
1. $L = L_{1} \circ L_{2}$ maps to $L \to L_{1}L_{2}$.
2. $L = L_{1} \cup L_{2}$ maps to $L \to L_{1}, L \to L_{2}$.
3. $L = L_{1}^{*}$ maps to $L \to LL_{1}^{*}, L \to \varepsilon$.

## Alternative proof
Here we work with [[finite automaton]] directly. Convert all states into variables, all alphabet symbols into terminals. Then add rules of the form $v \to cu$ for each $\delta(v, c) = u$. And $v \to \varepsilon$ for accepting states.