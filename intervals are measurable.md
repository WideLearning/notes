# intervals are measurable
From [[Lebesgue measurable set]]
$\physics$
## Statement
Interval $(l, r)$ is a [[Lebesgue measurable set]] for every $l, r \in \mathbb{R}$.

## Proof
Because [[Lebesgue measurable sets are a sigma-algebra]], we can take $r = \infty$.
Now for arbitrary $A$ we want to show (other direction is [[countable subadditivity of Lebesgue outer measure]]):
$$m^{*}(A) \geq m^{*}(A \cap (l, \infty)) + m^{*}(A \cap (-\infty, l]))$$
By [[Lebesgue outer measure of at most countable set is zero]] and [[Lebesgue outer measure of union with set of zero outer measure]]:
$$m^{*}(A) \geq m^{*}(A \cap (l, \infty)) + m^{*}(A \cap (-\infty, l))$$

And it is so, because we can split any cover of $A$ into covers of these parts by splitting each interval in the cover in $a$.