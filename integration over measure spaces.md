# integration over measure spaces
From [[measure theory]]
$\physics$
## Definition
Consider a [[measure space]] $(X, \mathcal{M}, \mu)$.

For  a nonnegative simple function $\psi: X \to \R_{\geq 0}$ such that $E_{k} = \psi^{-1}(c_{k})$ define:
$$\int_{X} \psi d\mu = \sum\limits c_{i}\mu(E_{i})$$
$$\int_{E \subset X} \psi d\mu = \int_{X} (\psi \cdot \chi_{E}) d\mu$$
For a nonnegative measurable function $f: X \to \R_{\geq 0}$ define:
$$\int_{X} fd\mu = \sup\left\{ \int_{X} \varphi d\mu \mid 0 \leq \varphi \leq f, \varphi - \text{simple}\right\}$$
Then we introduce $f_{+}$ and $f_{-}$ to extend it to all measurable real-valued functions.

## Properties
- Linearity
- Monotonicity