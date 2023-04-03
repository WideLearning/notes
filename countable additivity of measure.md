# countable additivity of measure
From [[measure]]
$\physics$
## Statement
$$m\qty(\bigsqcup\limits_{k \in \N} E_{k}) = \sum\limits_{k \in \N} m(E_{k})$$
## Proof
[[measurable sets are a sigma-algebra]]:
The left part is defined. 

[[monotonicity of outer measure]]:
The left part is not greater then the right.

[[outer measure and disjoint measurable sets]]:
Measure is finitely additive.

Now assume that countable additivity fails. It means that the measure of union is less than the sum of measures (by some non-zero margin), and so it is less than the sum of some prefix of measures. Contradiction.