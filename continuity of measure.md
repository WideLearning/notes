# continuity of measure
From [[measure]]
$\physics$
## Statement
For a collection of measurable sets $A_{[\N]}$ such that $A_{k} \subset A_{k+1}$ we have:
$$m\qty(\bigcup\limits_{k \in \N} A_{k}) = \lim\limits_{k \to \infty} m(A_{k})$$
And similarly for $A_{k} \supset A_{k+1}$, if $m(A_{1}) < \infty$:
$$m\qty(\bigcap\limits_{k \in \N} A_{k}) = \lim\limits_{k \to \infty} m(A_{k})$$

## Proof
Because [[countable union of measurable sets can be made disjoint]], let’s consider a sequence $D_{[\mathbb{N}]}$. As [[countable additivity of measure]] (finitely is enough in this case), we can replace $m(A_{k}) = \sum\limits_{i \in [k]} m(D_{i})$ and now we get $m\qty(\bigsqcup\limits_{k \in \N} D_{k}) = \sum\limits\limits_{k \to \infty} m(D_{k})$.
And it again follows from [[countable additivity of measure]].

The second statement is equivalent, because we can replace $A_{k}$ with $A_{1} \setminus A_{k}$ and intersection with union.