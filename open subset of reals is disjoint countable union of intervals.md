# open subset of reals is disjoint countable union of intervals
From [[real analysis]]
$\physics$
## Statement
Consider an open set $A \subset \mathbb{R}$. Then $\exists l_{\mathbb{N}} \in \mathbb{R}, r_{\mathbb{N}} \in \mathbb{R}$ such that $\bigcup_{i \in \N} (l_{i}, r_{i}) = A$ and is disjoint.

## Proof
For each $x \in A$ add $(a_{x}, b_{x})$ to the set of intervals, where $a_{x} = \inf\{ a \mid (a, x) \subset A \}$ and $b_{x}$ is defined symmetrically.
Such intervals are disjoint (or equal), because if two of them nontrivially intersect, some of infinums and extremums were broken. And because each of them contains a rational number ($\mathbb{Q}$ is dense), the number of unique intervals is at most countable. (We can always add empty intervals in random points to make it infinite, if needed)