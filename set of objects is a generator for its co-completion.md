# set of objects is a generator for its co-completion
From [[categorical generator]]
$\physics$
## Statement
Not exactly as in the title. Set of objects $S$ is a [[categorical generator]] of $\cat{C}$ if every object in $\cat{C}$ is a [[colimit]] of objects from $S$. (it is enough condition, (every object colimit) => (S generator))

## Proof
Take $f, g \in \hom_{\cat{C}}(X, Y)$. We know $X = \mathrm{colim}\ S'$ where $S' \subset S$. Then if we assume that $f \circ h = g \circ h$ on all $h$ from $S$ (and from $S'$ therefore), by universal property of [[colimit]] we get $f = g$. This implication proves that $S$ is a generator.