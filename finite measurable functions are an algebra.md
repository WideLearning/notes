# finite measurable functions are an algebra
From [[measurable function]]
$\physics$
## Statement
Suppose $f, g: E \to \mathbb{R}$ are finite for [[almost all]] $x \in E$ and measurable.
1. $\alpha f$ is finite for [[almost all]] $x \in E$ and measurable.
2. $\alpha f + \beta g$ is finite for [[almost all]] $x \in E$ and measurable.
3. $fg$ is finite for [[almost all]] $x \in E$ and measurable.

## Proof
In the following, consider the restrictions of $f, g$ that are finite. We can go back to $E$ later because [[measurable almost everywhere functions are measurable]].
1.
If $\alpha = 0$, then $\alpha f$ is zero and therefore measurable.
Otherwise, w.l.o.g. $\alpha > 0$, and $\{ x \mid (\alpha f)(x) > c \} = \{ x \mid f(x) > \frac{c}{\alpha} \}$, so it is measurable by definition.

2.
From previous point, we can take $\alpha = \beta = 1$. By density of $\mathbb{Q}$ in $\mathbb{R}$:
$$f(x) + g(x) < c \iff \exists q \in \mathbb{Q}. (f(x) < q) \wedge  (g(x) < c - q)$$
$$(f + g)^{-1}((-\infty, c)) = \bigcup\limits_{q \in Q} f^{-1}((-\infty, q)) \cap g^{-1}((-\infty, c - q))$$
Because rationals are countable and [[measurable sets are a sigma-algebra]], this preimage is also measurable, so $f + g$ is too. 

3.
Probably the same trick as in (2) would work here. But we can also use $fg = \frac{1}{2}\qty\Big((f+g)^{2}- f^{2} - g^{2})$. So we need only to show that $f^{2}$ is measurable, which is similar to (1):
$$(f^{2})^{-1}((-\infty, c)) = \begin{cases}
\varnothing, & c \leq 0\\
f^{-1}((-\sqrt{c}, \sqrt{c})), & c > 0\\
\end{cases}$$
