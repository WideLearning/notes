# image of dual map
From [[dual map]]

## Statement
$$T \in \L(V, W) \implies \begin{cases}
\dim \im T' = \dim \im T \\
\im T' = (\ker T)^{0}_{V}\\
\end{cases}$$
## Inner product intuition
In terms of matrices, $\im T'$ is the column space of $\mathcal{M}(T')$, which is the row space of $\mathcal{M}(T)$. And $(\ker T)^{0}_{V}$ is the space of row vectors that are orthgonal to all vectors that are orthogonal to all rows of $T$, so it is $((\text{row space of }T)^{\perp})^{\perp} = \text{row space of }T$.

Or in other words, $\im T'$ is all row-vectors of form $aT$, then $Tv = 0 \implies (aT)v = 0$, so all vectors lying in kernel will lie in annihilator.
And then you just check dimensions.

## Proof
First is easily derived from [[kernel of dual map]]:
$$\dim \ker T' = \dim W - \dim \im T$$
$$\dim \L(W, F) - \dim \im T' = \dim W - \dim \im T$$
$$\dim \im T' = \dim \im T$$
Now the second, as in intuition, but more rigorously. Let $v \in \ker T$, then:
$$\begin{split}
f \in \im T'
&\implies \exists g \in W': g \circ T = f\\
&\implies f(v) = (g \circ T)(v) = g(Tv) = 0\\
\end{split}$$
So, $\im T' \leqslant (\ker T)^{0}_{V}$. And then [[dimension test]] to check that they are equal.
