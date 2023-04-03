# KKT conditions
From [[optimization theory]]
$\physics$
## Statement
Karush–Kuhn–Tucker conditions are first-order necessary conditions of a local extremum. Suppose that $x^{*}$ is a local extremum of $f: \mathbb{R}^{n} \to \mathbb{R}$ subject to $\forall i \in E: c_{i}(x^{*}) = 0$, $\forall i \in I: c_{i}(x^{*}) \geq 0$. Then the following must hold for some $\lambda^{*} \in \mathbb{R}^{I \cup E}$ and $\L(x, \lambda) = f(x) - \sum\limits \lambda_{i} c_{i}(x)$:
$$\begin{cases}
\grad_{x} \L(x^{*}, \lambda^{*}) &= 0,\\
c_{i}(x^{*}) &= 0, & i \in E \\
c_{i}(x^{*}) &\geq 0, & i \in I \\
\lambda^{*}_{i}  &\geq 0, & i \in I\\
\lambda^{*}_{i}c_{i}(x^{*}) &= 0, & i \in I\\
\end{cases}$$

Also we assume that $f, c \in C^{1}$ (continuously differentiable) and that the set of active constraint gradients $\{ \grad c_{i}(x^{*}) \mid  i \in \mathcal{A}(x) \}$ is linearly independent.

## Proof
- what are cones?
- remember implicit function theorem
- farkas lemma
https://math.stackexchange.com/questions/1760709/how-to-prove-lagrange-multiplier-theorem-in-a-rigorous-but-intuitive-way