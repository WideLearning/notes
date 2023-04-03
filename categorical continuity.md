# categorical continuity
from [[functors in category theory]]

suppose have a category $I$ and a functor (diagram) $D$ to another category $C$ with some $\textbf{Lim} D$. also there is a functor $F$ from $C$ to $C'$. we call $F$ continuous if $\exists \textbf{Lim} (F \circ D) = F (\textbf{Lim} D)$ (for any $I$ and $D$, because it’s a property of $F$ itself).
note that all functors by definition are close to continuity, the only thing that may go wrong is uniqueness, there maybe be better cones in $C'$ that were in $C$.

### examples
[[hom-functor]] is continuous in both arguments. when the first argument is fixed (that is [[reader functor]]) it maps limits in $C$ to limits in $Set$, and when the second argument is fixed (that is opposite [[reader functor]]), it maps colimits in $C$ to limits in $Set$.