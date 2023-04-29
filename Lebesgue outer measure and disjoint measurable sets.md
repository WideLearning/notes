# Lebesgue outer measure and disjoint measurable sets
From [[Lebesgue outer measure]] and [[Lebesgue measurable set]]
$\physics$
## Statement
Let $A$ be any set and $X_{[n]}$ are disjoint measurable sets, then: 
$$m^{*}\qty(A \cap \qty(\bigcup_{i \in [n]} X_{i})) = \sum\limits_{i \in [n]} m^{*}(A \cap X_{i})$$

## Proof
Because [[Lebesgue measurable sets are closed under finite union]], it’s enough to show for $n = 2$ and then use induction.
We can use the same trick as in [[Lebesgue measurable sets are closed under finite union]], or just apply the definition of [[Lebesgue measurable set]] many times in both directions:
$$\begin{split}
m^{*}(A \cap(X_{1} \cup X_{2}))
&= m^{*}(A) - m^{*}(A \cap \overline{(X_{1}\cup X_2)})\\
&= m^{*}(A) - m^{*}(A  \cap \bar X_{1} \cap \bar X_{2})\\
&= m^{*}(A) - \qty(m^{*}(A \cap \bar X_{1}) - m^{*}(A \cap \bar X_{1} \cap X_2))\\
&= m^{*}(A) - m^{*}(A \cap \bar X_{1}) + m^{*}(A \cap X_{2})\\
&= m^{*}(A \cap X_{1}) + m^{*}(A \cap X_{2}) 
\end{split}$$
