# measurable sets are closed under countable union
From [[measurable set]]
$\physics$
## Statement
Suppose $\forall i \in \mathbb{N}: X_{i}$ is [[measurable set]]. Then $\cup X_{i}$ is also [[measurable set]].

## Proof
First, [[countable union of measurable sets can be made disjoint]], so assume $X_{i} \cap X_{j} = \varnothing$. Denote $U_{n} = \bigcup_{i \in [n]} X_{i}$ and $U = \bigcup_{i \in \N} X_{i}$.
Because [[measurable sets are closed under finite union]], $U_{n}$ is measurable:
$$\begin{split}
m^{*}(A) &= m^{*}(A \cap U_{n}) + m^{*}(A \cap (\mathbb{R} \setminus U_{n}))\\
&\geq m^{*}(A \cap U_{n}) + m^{*}(A \cap (\mathbb{R} \setminus U))
\end{split}$$
By [[outer measure and disjoint measurable sets]]:
$$\begin{split}
m^{*}(A) &\geq m^{*}(A \cap U_{n}) + m^{*}(A \cap (\mathbb{R} \setminus U))\\
\geq \sum\limits_{i \in [n]} m^{*}(A \cap X_{i}) + m^{*}(A \cap (\mathbb{R}\setminus U))
\end{split}$$