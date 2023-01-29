# polynomials of one operator commute
From [[commuting operators]]
$\physics$
## Statement
Let $T \in L(V)$ and $p, q \in F[x]$. Then $p(T)q(T) = q(T)p(T) = (pq)(T)$. In other words, polynomials of the same operator commute, and their composition is described by polynomial multiplication.

## Proof
For simplicity, let’s consider a simple example of $p(x) = x^{2}+ 1, q(x) = x + 2$. It can be easily generalized for $p(x) = \sum\limits_{i=1}^{n} a_{i}x^{i}, \dots$ but it will be harder to read and write.
$$\begin{split}
p(T)q(T) &= (T^{2} + 1) \circ (T + 2)\\
&= T^{2} \circ (T + 2) + 1 \circ (T + 2) \text{ (def. of operator sum)}\\
&= T^{2} \circ T + T^{2} \circ 2 + 1 \circ T + 1 \circ 2 \text{ (def. of linear map)}\\
&= T^{3} + 2T^{2} + T + 2 \text{ (def. of power of operator)}\\
&= (pq)(T)
\end{split}$$
Similarly $q(T)p(T) = (qp)(T)$.
And because we already know [[commutativity of polynomial product]]: 
$$p(T)q(T) = (pq)(T) = (qp)(T) = q(T)p(T)$$