# parametric polymorphic functions are natural transformations
from [[natural transformations in category theory]]

a function is called _parametric polymorphic_ if it doesn’t depend on the types of its arguments. such functions can’t do much interesting, and they turn out to be (i didn’t understand the proof yet) natural transformations. i.e. consider $\forall x . f :: F x \to G x$ (where $F$ is a [[functor]] and $G$ is a [[functor]], defining some relations of types, because just $a \to b$ is an impossible signature for a function). then $f$ is a [[natural transformation]] between $F$ and $G$.