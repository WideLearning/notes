# linearity and monotonicity of integration of nonnegative measurable functions
From [[Lebesgue integral]]
$\physics$
## Statement
Consider [[Lebesgue measurable function|measurable functions]] $f, g: E \to \R$, $f, g \geq 0$.
$$\int_{E} (\alpha f + \beta g) = \alpha \int_{E} f + \beta \int_{E} g$$
$$f \leq g \implies \int_{E} f \leq \int_{E} g$$

## Proof
For the first we find series of bounded measurable functions with finite support approximating $f, g$ and then apply [[linearity and monotonicity of integration of bounded measurable functions on finite measure sets]].
For the second: 
$$\int f \leq \int g$$
$$\sup \int h \leq \int g, h \leq f, \text{ bounded and measurable}$$
$$\forall \text{ bounded and measurable } h \leq f. \int h \leq \int g$$
$$\forall \text{ bounded and measurable } h \leq f. h \leq g$$
$$f \leq g$$
