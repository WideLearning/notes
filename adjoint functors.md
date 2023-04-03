# adjoint functors
From [[category theory]]
$\physics$
## Definition
Functors $F: \cat{C} \to \cat{D}$ and $U: \cat{D} \to \cat{C}$ are adjoint, denoted $F \dashv G$, iff there is a [[natural isomorphism]] between (see [[natural transformation for bifunctors]]):
- $\hom_{D}(F(-), -): \cat{C}^{op} \times D \to \cat{Set}$
- $\hom_{C}(-, U(-)): \cat{C}^{op} \times D \to \cat{Set}$


## Properties
- [[definition of adjoint through isomorphism]]
- [[adjoint functor is unique]]
- [[adjoints preserve limits]]
- [[unit of adjunction]]
- [[counit of adjunction]]
- [[definition of adjoint through unit]]
- [[definition of adjoint through unit and counit]]

## Examples
- Consider [[preorder]] given by $\leq$ on $\mathbb{Q}$ and its $\mathbb{Z}$ subcategory. For a 