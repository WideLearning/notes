# linearity and monotonicity of integration
From [[Lebesgue integral]]
$\physics$
## Statement
Consider [[Lebesgue measurable function|measurable functions]] $f, g: E \to \R$.
$$\int_{E} (\alpha f + \beta g) = \alpha \int_{E} f + \beta \int_{E} g$$
$$f \leq g \implies \int_{E} f \leq \int_{E} g$$
## Proof
We know that [[linearity and monotonicity of integration of nonnegative measurable functions]]. 
Denote $f_{+} = \max(f, 0), f_{-} = \max(-f, 0)$, now $f = f_{+} - f_{-}$ and both parts are non-negative and measurable. Same for $g$.

For $\beta = 0$:
$$\int_{E} \alpha f = \int_{E} (\alpha f)_{+} - \int_{E} (\alpha f)_{-} = \alpha \left(\int_{E} f_{+} - \int_{E} f_{-}\right) = \alpha \int_{E} f$$
For $\alpha = \beta = 1$:
$$\int_{E}(f + g) - \int_{E} f - \int_{E} g$$
$$\int ((f+g)_{+} + f_{-} + g_{-}) - \int ((f+g)_{-} + f_{+} + g_{+})$$
$$\int \max(f + g + f_{-} + g_{-}, f_{-} + g_{-}) - \int \max(-(f + g) + f_{+} + g_{+}, f_{+} + g_{+})$$
$$\int \max(f_{+} + g_{+}, f_{-} + g_{-}) - \int \max(f_{-} + g_{-}, f_{+} + g_{+})$$
$$0$$
Monotonicity:
$$f \leq g$$
$$f_{+} - f_{-} \leq g_{+} - g_{-}$$
$$f_{+} + g_{-} \leq g_{+} + f_{-}$$
$$\int (f_{+} + g_{-}) \leq \int (g_{+} + f_{-})$$
$$\int f_{+} + \int g_{+} \leq \int g_{+} + \int f_{-}$$
$$\int f_{+} - \int f_{-} \leq \int g_{+} - \int g_{-}$$
$$\int f \leq \int g$$