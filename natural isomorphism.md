# natural isomorphism
From [[natural transformation]]
$\physics$
## Definition
A [[natural transformation]] $\alpha: F \to G$ where $F, G: \cat{C} \to \cat{D}$ is a natural isomorphism iff (equivalently any of the following):
1. $\forall X \in \ob(\cat{C}). \alpha_{X}$ is [[isomorphism]].
2. $\exists \beta: G \to F. \alpha \circ \beta = \id_{G}, \beta \circ \alpha = \id_{F}$ in [[category of functors]] $\cat{D}^\cat{C}$.

## Proof of equivalence
$1 \implies 2$:
Take $\forall X \in \ob(\cat{C}). \beta_{X} = \alpha_{X}^{-1}$, now $(\alpha \circ \beta)_{X} = \id_{G X}, (\beta \circ \alpha)_{X} = \id_{F X}$, so $\alpha \circ \beta = \id_{G},  \beta \circ \alpha = \id_{F}$ in $\cat{D}^{\cat{C}}$.

$2 \implies 1$:
Each $\alpha_{X}$ is [[isomorphism]] because we can get inverse from $\beta_{X}$.