# representation
from [[functor]]

it’s a functor with a [[natural isomorphism]] to $\hom(a, -)$ for some $a$ ([[hom-functor]], $a \in C$). it maps objects of $C$ to sets and morphisms to functions.

actually, there is a [[natural transformation]] from $C(a, -)$ to any such functor, but not always back.

such functors can be thought of as memoizations of functions:
``` haskell
class Representable f where
	type Rep f :: *
	tabulate :: (Rep f -> x) -> f x
	index :: f x -> Rep f -> x
```

because (as [[exponential]]) $C(a, x) = x^a$, $C(a, -) = -^{a}= F$ where $F$ is representable functor. so, in some sense, $a = \log_{-} F$. (what is $\log F$ and even more $\log_{-} F$ is a good question, it’s just a fun formal trick). 