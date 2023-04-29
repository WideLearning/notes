# integral comparison test
From [[Lebesgue integral]]
$\physics$
## Statement
Let $f: E \to \mathbb{R}$ be a [[Lebesgue measurable function]] and $g: E \to \mathbb{R}$ be a non-negative measurable function integrable over $E$. If $\abs{f} \leq g$ on $E$ then $\int_{E} f$ exists and:
$$\abs{\int_{E} f} \leq \int_{E} \abs{f} \leq \int_{E} g$$

## Proof
We will use [[linearity and monotonicity of integration]].
From monotonicity: 
$$\int \abs{f} \leq \int g$$
And from linearity:
$$\abs{\int f} = \abs{\int f_{+} - \int f_{-}} \leq \int f_{+} + \int f_{-} = \int \abs{f}$$

