# Lagrange interpolation
From [[polynomial interpolation]]
$\physics$
## Statement
Let $\{ x_k \}_{k=0}^{n}$ and $\{ y_k \}_{k=0}^{n}$ be nodes and values for interpolation. Consider a polynomial:
$$\begin{cases}
p(t) = \sum\limits_{k=0}^{n} y_{k}L_{k}(x) \\
L_{k}(x) = \frac{\prod_{i \ne k} (x - x_{i})}{\prod_{i \ne k} (x_{k} - x_{i})} \\
\end{cases}$$
Also, $L_{k}(x) = \frac{g(x)}{g'(x_{k})}$, where $g(x) = \prod\limits_{k=0}^{n} (x - x_{k}), \lim\limits_{x \to x_{k}} g'(x) = (x - x_{k})\prod\limits_{i \ne k}(x - x_{i})$.
Then $\forall k \in [0, n]. p(x_{k}) = y_{k}$, that is, it is an interpolating polynomial.

## Proof
By direct substitution we can see that $L_{i}(x_{j}) = [i = j]$. So $p(x_{i}) = \sum\limits y_{j}[i = j] = y_i$.

## See also
By default computing these $L_{k}$ will be $\order{n^{3}}$, because for each of them we need to multiply $n$ linear terms. Can be sped up by FFT, probably. Also there is [[Aitken interpolation]] that allows to evaluate it in one point in $\order{n^{2}}$.