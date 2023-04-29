# countable subadditivity of Lebesgue outer measure
From [[Lebesgue outer measure]]
$\physics$
## Statement
$$m^{*}\left(\bigcup_{k=1}^{\infty} A_{i}\right) \leq \sum\limits_{k=1}^{\infty} m^{*}(A_{i})$$

## Proof
First, let’s show it is subadditive for two sets: $m^{*}(A \cup B) \leq m^{*}(A) + m^{*}(B)$
It is because any cover of $A$ together with any cover of $B$ is a cover of $A \cup B$ and its sum of length is sum of the sum for $A$ and for $B$. So we just add two infinums.

From it finite subadditivity follows by induction. And then by squeeze theorem for limits we get the countable subadditivity.