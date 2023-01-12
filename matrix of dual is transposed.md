# matrix of dual is transposed
From [[duality]]
$\physics$
## Statement
Suppose we have spaces $V = \ev{v_{[n]}}, W = \ev{w_{[m]}}, V' = \ev{\varphi_{[n]}}, W' = \ev{\psi_{[m]}}$, and maps $L \in \L(V, W), L' \in \L(W', V')$.
Then $[L']_{\psi}^{\varphi} = ([L]_{w}^{v})^{T}$.

## Proof
Let $A = [L]_{w}^{v} \in F^{m \times n}, A' = [L']_{\psi}^{\varphi} \in F^{n \times m}$. Consider how $L'$ acts on its basis:
$$L'(\psi_{i}) = \sum\limits_{j=1}^{n} A'_{j, i} \varphi_{j},\quad L(v_{k}) = \sum\limits_{t=1}^{m} A_{t, k}w_{t}$$
$$\begin{split}
L'(\psi_{i})(v_k)
&= \psi_{i}(L(v_{k}))\\
&= \psi_{i}\left( \sum\limits_{t=1}^{m} A_{t, k}w_{t} \right)\\
&= \sum\limits_{t=1}^{m} A_{t, k}\psi_{i}(w_{t})\\
&= \sum\limits_{t=1}^{m} A_{t, k}[i = t]\\
&= A_{i, k}
\end{split}$$
$$\begin{split}
L'(\psi_{i})(v_{k})
&= \sum\limits A'_{j, i} \varphi_{j}(v_{k})\\
&= \sum\limits A'_{j, i} [j = k]\\
&= A'_{k, i}
\end{split}$$
$$ \forall i \in [m], k \in [n]: A_{i, k} = A'_{k, i} \implies A' = A^{T}$$