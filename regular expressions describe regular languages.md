# regular expressions describe regular languages
From [[regular language]] and [[regular expression]]
$\physics$
## Statement
$A$ is a [[regular language]] iff $\exists B: L(B) = A$ and $B$ is a [[regular expression]].

## Proof
### All regular expressions describe regular languages
From the recursive definition of [[regular expression]] it easy to build the corresponding language because:
- [[regular languages are closed under union]]
- [[regular languages are closed under concatenation]]
- [[regular languages are closed under Kleene star]]

## All regular languages can be described by regular expressions
- [[FA can be converted to GNFA]]
- [[GNFA can be converted to regular expression]]