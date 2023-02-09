# countable union of measurable sets can be made disjoint
From [[measurable set]]
$\physics$
## Statement
Consider $A_{\mathbb{N}}$ such that $\forall i: A_{i}$ is a [[measurable set]]. Then there is $B_{\mathbb{N}}$ with the same property, which is disjoint and has the same union as $A$.

## Proof
Construct $B$ as follows:
$$B_{i} = A_{i} \setminus \qty(\bigcup_{j \in [i - 1]} A_{j})$$
