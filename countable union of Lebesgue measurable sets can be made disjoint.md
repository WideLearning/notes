# countable union of Lebesgue measurable sets can be made disjoint
From [[Lebesgue measurable set]]
$\physics$
## Statement
Consider $A_{\mathbb{N}}$ such that $\forall i: A_{i}$ is a [[Lebesgue measurable set]]. Then there is $B_{\mathbb{N}}$ with the same property, which is disjoint and has the same union as $A$.

## Proof
Construct $B$ as follows:
$$B_{i} = A_{i} \setminus \qty(\bigcup_{j \in [i - 1]} A_{j})$$
Because [[Lebesgue measurable sets are closed under taking complements]] and [[Lebesgue  measurable sets are closed under finite union]], $B_{\mathbb{N}}$ is a sequence of measurable sets too. Moreover, $x \in \bigcup_{i \in [n]} A_{i} \iff x \in \bigcup_{i \in [n]} B_{i}$, so $x \in \bigcup_{i \in \N} A_{i} \iff x \in \bigcup_{i \in \N} B_{i}$.