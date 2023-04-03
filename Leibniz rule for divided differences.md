# Leibniz rule for divided differences
From [[divided differences]]
$\physics$
## Statement
$$(f g)[x_{[n]}] = \sum\limits_{i \in [n]} f[x_{[i]}]g[x_{[i:n]}]$$

## Proof
Generate $x_{[n+1:2n - 1]}$ arbitrary. Let $P(x) = A(x)B(x)$, where $A, B$ are interpolating polynoms (with $\deg = n - 1$) for $f, g$ on $x_{[n]}$.

By [[Newton interpolation]] (for $B$ using reverse order, which will be useful later):
$$A(x) = \sum\limits_{i \in [0:n-1]} f[x_{[i+1]}]N_{[i]}(x),\ B(x) = \sum\limits_{i \in [0:n-1]} g[x_{[n-i:n]}]N_{[n+1-i:n]}(x),\ N_{s}(x) = \prod_{i \in s} (x - x_{i})$$
So their product:
$$(AB)(x) = \sum\limits_{s \in [0:2n - 2]} \sum\limits_{i \in [0:\min(n - 1, s)]} f[x_{[i]}]g[x_{[n-s+i:n]}]N_{[i]}(x)N_{[n+1-s+i:n]}(x)$$
In particular, for $s = n - 1$ we have:
$$N_{[n]}(x) \sum\limits_{i \in [n-1]} f[x_{[i]}]g[x_{[i:n]}]$$
$AB$ is now written in a strange basis, but it has size $2n - 1$ and (no??? contains $N_{[n]}$ in it). So we can translate it to Newton basis with $x_{[2n-1]}$ and the coefficient for $N_{[n]}$ won’t change. Now we discard all higher coefficients (for $N_{[n + 1]} \dots$), and get $n$-th. ???