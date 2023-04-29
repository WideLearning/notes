# adjunction
From [[category theory]]
$\physics$
## Definition
Functors $F: \cat{C} \to \cat{D}$ and $U: \cat{D} \to \cat{C}$ are adjoint, denoted $F \dashv G$, iff there is a [[natural isomorphism]] between (see [[natural transformation for bifunctors]]):
- $\hom_{D}(F(-), -): \cat{C}^{op} \times D \to \cat{Set}$
- $\hom_{C}(-, U(-)): \cat{C}^{op} \times D \to \cat{Set}$


## Properties
- [[adjoints preserve limits]]
- [[definition of adjunction through commutative diagram]]
- [[unit of adjunction]]
- [[definition of adjunction through unit]]
- [[definition of adjunction through unit and counit]]
- [[adjoint functor is unique]]
- [[definition of adjunction through universal morphisms]]
- [[monad from adjunction]]
- [[monadicity of adjunction]]

## Examples
- Free functor $F$ and [[forgetful functor]] $U$ are often adjoint as $F \dashv U$.