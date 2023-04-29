# categorical limit
From [[constructions and operations in category theory]], generalizes [[categorical product]], [[terminal object]], [[equalizer]] and [[pullback]]

## Definition
It is a [[categorical cone]] with [[universal property]]: if there is another cone, there is a morphism from the other to the universal one that factorizes all projections of the other. In some sense, limits allow building morphisms to them.

## Equivalent definition
Consider the contravariant [[hom-functor]] $\hom(-, X): \cat{C}^{op} \to \cat{Set}$.

Also we need the [[contravariant functor]] $\mathrm{Nat}(\Delta_{-}, D): \cat{C} \to \cat{Set}$ that maps $A \in \cat{C}$ to the set of natural transformations from the [[constant functor]] $\Delta_{A}: \cat{J} \to \cat{C}$ to the diagram $D: \cat{J} \to \cat{C}$. On morphisms it acts similar to contravariant hom-functor: $\mathrm{Nat}(\Delta_{f}, D)$ where $f: B \to A$ given $\alpha: \Delta_{A} \to D$ produces $\beta: \Delta_{B} \to D$ such that $\forall X \in \ob(J). \beta_{X} = \alpha_{X} \circ f$. (Here $\alpha_{X}: A \to DX$ and $\beta_{X}: B \to DX$).

Then $X = \lim D$ iff there is a [[natural isomorphism]] $\hom_{\cat{C}}(-, X) \cong \mathrm{Nat}(\Delta_{-}, D)$.

## Proof of equivalence
As we know, a [[categorical cone]] with vertex $A$ and diagram $D$ is a [[natural transformation]] $\Delta_{A} \to D$, which is a morphism, if we consider a [[category of functors]] $\cat{C}^{\cat{J}}$.
We have $\hom_{\cat{C}}(-, X) \cong \hom_{\cat{C}^{\cat{J}}}(\Delta_{-}, D)$, so by a dual version of [[universal morphism is equivalent to natural isomorphism between hom-sets]] we get that cone $\Delta_{X} \to D$ is universal and there is a unique morphism from any other cone to $X$ which by definition is represented by a morphism in $C$ that goes from the vertex of that cone to $X$ and factors all needed morphisms.

## Properties
- [[limits are unique up to isomorphism]]
- [[limits via products and equalizers]]
- [[categorical continuity]]
- [[adjoints preserve limits]]
- [[covariant hom-functor preserves limits]]