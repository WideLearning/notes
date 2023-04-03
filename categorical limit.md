# categorical limit
From [[constructions and operations in category theory]], generalizes [[categorical product]], [[terminal object]], [[equalizer]] and [[pullback]]

## Definition
It is a [[categorical cone]] with [[universal property]]: if there is another cone, there is a morphism from the other to the universal one that factorizes all projections of the other. In some sense, limits allow building morphisms to them.

## Another definition
First, consider the [[contravariant functor]] $\mathrm{Hom}(., X)$ that maps $c \in C$ to $\mathrm{Hom}(c, X)$. It is similar to opposite [[reader functor]], mapping for morphisms is again reversed composition.
Second, consider the [[contravariant functor]] $\mathrm{Nat}(\Delta_{.}, D)$ that maps $c \in C$ to $\mathrm{Nat}(\Delta_{c}, D)$. For morphisms it uses reversed compositon for each component of natural transformation separately.
Then $X = \lim D$ iff there is a [[natural isomorphism]] between these functors. 

## Properties
- [[limits are unique up to isomorphism]]
- [[limits via products and equalizers]]
- [[categorical continuity]]