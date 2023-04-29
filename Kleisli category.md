# Kleisli category
From [[category]]
$\physics$
## Definition
Consider a [[monad]] $(T, \eta, \mu)$ in $\cat{C}$. Then $\cat{Kl}_{T}$ is defined as follows:
- $\ob(\cat{Kl}_{T}) = \ob(\cat{C})$
- $\hom_{\cat{Kl}_{T}}(A, B) = \hom_{\cat{C}}(A, TB)$
- $\id_{A} = \eta_{A}$
- $g \circ_{\cat{Kl}_{T}} f = \mu \circ_{\cat{C}} Tg \circ_{\cat{C}} f$

## Properties
- [[Kleisli category is equivalent to full subcategory of T-alg on free algebras]]

## Examples
- `List`: $A \to B$ functions now actually return a list of elements from $B$ given an element of $A$. And compositon of two such functions runs the first one, then applies the second to each element of the output, and then flattens this list of lists into a one-level list.
- `Maybe`: The natural way to combine partial functions.
- $TA = A \times \mathrm{String}$: Functions return not only the result, but also some log or error. Compositon of functions composes the results, and concatenates the strings.

