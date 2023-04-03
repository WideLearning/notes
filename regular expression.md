# regular expression
From [[formal languages]]
$\physics$
## Definition
A regular expression over alphabet $\Sigma$ is defined recursively as one of these:
1. $L(a) = \{ a \}, a \in \Sigma_{\varepsilon}$
2. $L(\varnothing) = \varnothing$
3. $L(A \cup B) = L(A) \cup L(B)$, $A, B$ are regexps (union)
4. $L(AB) = L(A) \circ L(B)$, $A, B$ are regexps (concatenation)
5. $L(A^{*}) = L(A)^{*}$, $A, B$ are regexps (Kleene star)

Here $L(R)$ denotes the language described by the regular expression $R$.

## Properties
- [[regular expressions describe regular languages]]