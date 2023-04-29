# functor
From [[category theory]]
$\physics$
## Definition
A functor is a morphism in the [[category of small categories]]. It consists of a mapping of objects and a mapping of morphisms, satisfying the following “functor laws”:
- $F(\id_{A}) = \id_{F(A)}$
- $F(g \circ f) = F(g) \circ F(f)$

## Properties
- If we are not speaking about [[isomorphism]], a functor can collapse several objects and morphisms into one, just as they can map no object to an object in the second category.
- Morphism from [[category of sets]] to itself (i.e., [[endomorphism]]) is something mapping types to other types, which can be seen as parametrized types (aka generics, aka templates). so it can also be seen as a container (for example, `std::vector<A>` or `std::map<A>` are functors with `A` being their argument).
- Something like a functor but reversing morphisms is [[contravariant functor]].

## Examples
- [[endofunctor]]
- [[faithful functor]]
- [[full functor]]
- [[essentially surjective functor]]
- [[forgetful functor]]
- [[constant functor]]
- [[profunctor]], [[hom-functor]]
- [[presheaf]]
- [[representation]]
- [[bifunctor]]