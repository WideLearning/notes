# monad as a monoid
From [[monad]]
$\physics$
> All told, a monad in X is just a monoid in the category of endofunctors of X, with product × replaced by composition of endofunctors and unit set by the identity endofunctor.

## Statement
More precisely, [[monad]] in a category $\cat{C}$ is a [[categorical monoid]] $(T \in \cat{C}^{\cat{C}}, \mu: T \circ T \to T, \eta: \id_{\cat{C}} \to T)$ in a [[strict monoidal category]] $(\cat{B}, \circ: \cat{B} \times \cat{B} \to \cat{B}, \id_{\cat{C}})$ where $\cat{B}$ is the category of endofunctors in $\cat{C}$.