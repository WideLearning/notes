# lemma about Gaussian quadrature error
From [[numerical integration]]
$\physics$
## Statement
Consider numerical integration of $f: [a, b] \to \R$ with nodes $a \leq x_{0} < \dots < x_{n} \leq b$. Take $q = \prod\limits_{0 \leq i \leq n} (x - x_{i})$. If $q$ is orthogonal to $x^{k}$ for $0 \leq k \leq n$ (that is, $\int_{a}^{b} q(x)x^{k}dx = 0$), and $A_{i} = \int_{a}^{b} L_{i}(x) dx$ ([[Lagrange interpolation]]), integration scheme with $x_{[0:n]}$ and $A_{[0:n]}$ integrates exactly all polynomials of degree up to $2n + 1$.

## Proof
Let $f$ be such a polymonial. By polynomial division:
$$f(x) = s(x)q(x) + r(x)$$
Where $\deg s, \deg r \leq n$. Note that $r(x_{i}) = f(x_{i}) - s(x_{i}) \cdot 0 = f(x_{i})$.
$$\int_{a}^{b} f(x)dx = \int_{a}^{b} s(x)q(x)dx + \int_{a}^{b} r(x)dx$$
Where the first term is zero by orthogonality.
$$\begin{split}
\int_{a}^{b} f(x)dx &= \int_{a}^{b} r(x)dx\\
&= \int_{a}^{b} \left(\sum\limits_{0 \leq i \leq n} r(x_{i})L_{i}(x)\right)dx\\
&= \sum\limits_{0 \leq i \leq n} r(x_{i}) \int_{a}^{b} L_{i}(x) dx\\
&= \sum\limits_{0 \leq i \leq n} A_{i} r(x_{i})\\
&= \sum\limits_{0 \leq i \leq n} A_{i} f(x_{i})\\
\end{split}$$
