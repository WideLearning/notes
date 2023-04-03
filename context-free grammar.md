# context-free grammar
From [[formal languages]]
$\physics$
## Definition
A CFG is defined by:
1. $V$: finite state, variables
2. $\Sigma$: finite state disjoint from  $V$, terminals
3. $R$: [[relation]] on $V \times (V \cup \Sigma)^{*}$, rules
4. $S \in V$: start variable

A string can be generated from a grammar iff there is a sequence of steps, where on each we replace one variable by one of the strings related to it by rules. All such strings together for the language of this grammar.

## Example
$$G = \ev{\{ A, B\}, \{ 0, 1 \}, \{ A \to 0A1, A \to B, B \to \varepsilon \}, A}$$
Examples of strings generated from $G$:
$$A \to 0A1 \to 00A11 \to 00B11 \to 0011$$
$$A \to 0A1 \to 00A11 \to 000A111 \to 000B111 \to 000111$$

## Properties
- [[Chomsky normal form]]
- [[mPDA and context-free grammars are equivalent]]