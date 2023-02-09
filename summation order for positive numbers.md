# summation order for positive numbers
From [[measure theory]]
$\physics$
## Statement
It doesn’t matter in what order to sum positive numbers from a countable set.
More formally. Let $A_{\mathbb{N}}$ be a set of positive reals and $p \in \mathbb{N}^{\mathbb{N}}$ be a permutation of naturals ($\forall i \ne j: p_{i} \ne p_{j}$). Then $\sum\limits A_{i} \geq \sum\limits A_{p_{i}}$ if $\sum\limits A_{i}$ converges. And we can apply the same to $p^{-1}$ to see that they convergence is equivalent and sums are equal.

## Proof
We know the convergence of original sum: $\sum\limits A_{i} = C$. In particular, it means $\sum\limits_{i=1}^{n} A_{i} \leq C$. Then $\sum\limits_{i=1}^{n} A_{p_{i}} \leq \sum\limits_{i=1}^{\max p_{[n]}} A_{i} \leq C$ and $\sum\limits A_{p_{i}} \leq C$.