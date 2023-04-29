# strict monoidal category
From [[monoidal category]]
$\physics$
## Definition
A strict monoidal category is a [[category]] $\cat{B}$ together with [[bifunctor]] $\square: \cat{B} \times \cat{B} \to \cat{B}$ and an object $E \in \ob(\cat{B})$ which satisfies:
1. Associativity law:
$$\square(\square \times \id_{\cat{B}}) = \square(\id_{\cat{B}} \times \square)$$
2. Unit laws:
$$\square(E \times \id_{\cat{B}}) = \square(\id_{\cat{B}} \times E) = \id_{\cat{B}}$$

Notation:
- $\square(\square \times \id_{\cat{B}})$ means composition of functors $\square: \cat{B}^{2}\to \cat{B}$ and $(\square \times \id_{\cat{B}}): \cat{B}^{3} \to \cat{B}^{2}$.
- $(E, \id_{\cat{B}}): \cat{B} \to \cat{B}^{2}$ means functor that takes [[categorical product]] with $E$: $C \mapsto E \times C$ 

## Properties
- $\id_{A} \square \id_{B} = \id_{A \square B}$
- $(f' \square g') \circ (f \square g) = (f' \circ f) \square (g' \circ g)$
- $(A \square B) \square C = A \square (B \square C)$
- $(f \square g) \square h = f \square (g \square h)$
- $E \square C = C \square E = C$
- $\id_{E} \square f = f \square \id_{E}$

## Examples
- Algebraic [[monoid]], when considered as [[discrete category]] with $\square$ given by the  operation of this monoid
- The category of endofunctors for any category, where arrows are natural transformations and $\square$ is composition of functors.