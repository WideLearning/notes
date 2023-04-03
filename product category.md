# product category
From [[category]]
$\physics$
## Definition
Category $\cat{C} \times \cat{D}$ has pairs of objects from $\cat{C}, \cat{D}$ as objects, pairs of morphisms as morphisms, and composition is component-wise.
$$\ob(\cat{C} \times \cat{D}) = \ob(\cat{C}) \times \ob(\cat{D})$$
$$\hom_{\cat{C} \times \cat{D}}((a, b), (c, d)) = \hom_{\cat{C}}(a, c) \times \hom_{\cat{D}}(b, d)$$
$$(a, b) \circ (c, d) = (a \circ c, b \circ d)$$

## Properties
- Product is commutative and associative (up to isomorphism or equivalence?).
- Any morphism $(f, g)$ can be decomposed as $(\id, g) \circ (f, \id)$.
- It simplifies [[natural transformation for bifunctors]].