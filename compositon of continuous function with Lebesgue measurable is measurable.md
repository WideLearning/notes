# compositon of continuous function with Lebesgue measurable is measurable
From [[Lebesgue measurable function]]
$\physics$
## Statement
Suppose $f: \R \to \R$ is continuous and $g: E \to \mathbb{R}$ is measurable. Then $f \circ g: E \to \mathbb{R}$ is also measurable.

## Proof
Let’s use [[Lebesgue measurable function in terms of open sets]]. For any open $O \subset \mathbb{R}$ we know that $f^{-1}(O)$ is open, and then $g^{-1}(f^{-1}(O))$ is measurable. Then $f \circ g$ is measurable.