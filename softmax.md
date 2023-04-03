# softmax
From [[machine learning]]
$\physics$
## Definition
$$\forall a \in \R^{n}. \mathrm{softmax}(a)_{k} = \frac{\exp(a_{k})}{\sum\limits \exp(a_{i})}$$
## Properties
- Output of softmax is always a valid [[PMF]]: all components are non-negative and sum up to one.
- It is invariant to translation of input by a constant, which is used to compute it in a more stable way.
- If $p = \mathrm{softmax}(a)$, $\pdv{p_{i}}{a_{j}} = p_{i} \cdot ([i=j] - p_{j}) = p_{j} \cdot ([i=j] - p_{i})$. 