# simple approximation theorem
From [[measurable function]], [[simple function]]
$\physics$
## Statement
A function $f: E \to \R$ on a [[measurable set]] $E$ is a [[measurable function]] iff there is a sequence of [[simple function|simple functions]] $\{ \varphi_{n} \}$ which [[converges pointwise]] on $E$ to $f$ and satisfies $\abs{\varphi_{n}} \leq \abs{f}$. For nonnegative $f$ there exists an increasing $\{ \varphi_{n} \}$.

## Proof
$\text{sequence} \implies \text{measurable}$:
A [[simple function]] is always measurable, and [[pointwise limit preserves measurability]].

$\text{measurable} \implies \text{sequence}$:
Assume $f \geq 0$, otherwise just apply this to $f_{+} = \max(0, f)$ and $f_{-} = \max(0, -f)$.
We build $\varphi_{n}$ as $l$ from [[simple approximation lemma]] with $\varepsilon = \frac{1}{n}$ and $f = \min(f, n)$. This way, if $f$ is finite, from $\lceil f(x) \rceil$ step $\varphi_{n}(x)$ will start approximating it, and otherwise $\lim \varphi_{n}(x) = \lim n = \infty = f(x)$.