# isomorphism
from [[basic definitions from category theory]] and [[linear algebra]]

## Definition
In general, isomorphism between two sets of objects is an invertible map between them, preserving structure. In case of linear spaces it will be an invertible [[linear map]]. In case of sets it will be a bijection.

For categories in general, it’s a pair of morphisms between two objects, being inverse for each other. More precisely, if we have $f :: a \to b, g :: b \to a$ then we want $f \circ g = id_{b}, g \circ f = id_{a}$.