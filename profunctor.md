# profunctor
from [[functors in category theory]]

it’s something like [[bifunctor]], being [[contravariant functor]] in its first argument and [[covariant functor]] in its second argument (or combination of [[reader functor]] and its opposite).
one of examples is function-arrow operator (which takes types `a` and `b` and produces type of function from `a` to `b`). its `dimap` takes two functions: `f :: a -> b` and `g :: c -> d` and produces a higher-order function that transforms any `b -> c` function to `a -> d` function, composing with those two.

similar idea is [[hom-functor]].