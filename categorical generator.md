# categorical generator
From [[category theory]]
$\physics$
## Definition
Consider $S \subset \ob(\cat{C})$. It is a generator iff for every $f, g \in \hom_{\cat{C}}(X, Y)$:
$$f = g \iff \forall S_{i} \in S. \forall h \in \hom_{\cat{C}}(S_{i} X). f \circ h = g \circ h$$
That it, it’s enough to check equality of $f$ and $g$ only on morphisms from $S$.

## Properties
- [[set of objects is a generator for its co-completion]]