# invariance theorem
From [[Kolmogorov’s complexity]]
$\physics$
## Statement
There is an optimal [[specifying method]] among [[computable function|computable functions]].

## Proof
Let $\phi_{0}$ be the function computed by a [[universal Turing machine]] $U$. Inputs to it are encoded as, for example, $\ev{n, p} = \bar{n}p$ (see [[self-delimiting string]]). And $\varphi_{0}(\ev{n, p}) = T_{n}(p)$ (running TM with [[Godel number]] $n$ on input $p$), where $T_{0} = U$.

So, if we denote the function computed by $T_{n}$ as $\phi_{n}$, we get:
$$C_{\phi_{0}}(x) \leq C_{\phi_{n}}(x) + l(\bar n) = C_{\phi_{n}}(x) + (2l(n) + 1)$$
