# category theory
From [[topics]]

### Contents
- [[basic definitions from category theory ]]
- [[commutative diagram]], [[cheking finite categories in Python]]
- [[constructions and operations in category theory]]
- [[functors in category theory]]
- [[natural transformations in category theory]]
- [[yoneda lemma]]

- [[category theory topics sorted by complexity]]

## Notation
- $\mathrm{Ob}(C)$ — objects of $C$
- $\mathrm{Hom}(C)$ — morphisms of $C$
- $\mathrm{Hom}_{C}(X, Y)$ — [[hom-set]] for objects $X, Y$ in $C$
- $\mathrm{Endo}_{C}(X)$ — [[monoid]] of [[endomorphism|endomorphisms]] for $X$
- $\mathrm{Aut}_{C}(X)$ — [[group]] of [[automorphism|automorphisms]] for $X$
- $\mathrm{id}_{X}$ — [[identity morphism]]

### TODO
- why reader functor is ok (which maps $a$ to $r \to a$), and the opposite (though being contravariant functor) is also not so bad, but mapping $a$ to $a \to a$ isn’t a functor? i think the following should work:
``` haskell
fmap :: (a -> b) -> (a -> a) -> (b -> b)
fmap f g = id
```
- yoneda when $F a = \varnothing$?

## Books
- Saunders Mac Lane,  _Categories for the working mathematician_
- R. Goldblatt, _Topoi: The categorial analysis of logic_