# commutativity of polynomial product
From [[linear algebra]] and [[commuting operators]]
$\physics$
## Statement
Suppose $p \in F_{n}[x], q \in F_{m}[x]$, then $pq = qp$ (in terms of coefficients).

## Proof
$$\begin{split}
pq &= \qty(\sum\limits_{i=0}^{n} a_{i}x^{i})\qty(\sum\limits_{j=0}^{m}b_{j}x^{j})\\
&= \sum\limits_{i=0}^{n} a_{i}x^{i}\sum\limits_{j=0}^{m}b_{j}x^{j}\\
&= \sum\limits_{i=0}^{n} \sum\limits_{j=0}^{m} a_{i}b_{j}x^{i+j}\\
&= \sum\limits_{s=0}^{n+m} \qty(\sum\limits_{i=0}^{\min(s, n)} a_{i}b_{s-i})x^{s}\\
&= \sum\limits_{s=0}^{n+m} \qty(\sum\limits_{i=0}^{\min(s, m)} b_{i}a_{s-i})x^{s}\\
&= \dots\\
&= qp
\end{split}$$