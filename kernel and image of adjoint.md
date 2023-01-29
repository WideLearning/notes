# kernel and image of adjoint
From [[adjoint]]
$\physics$
## Statement
Let $T \in \L(V, W)$, then:
- $\ker T^{*} = (\im T)^{\perp}$
- $\im T^{*} = (\ker T)^{\perp}$

## Proof
Note that the statements are equivalent, because $(T^{\perp})^{\perp} = T$ and $(T^{*})^{*} = T$ (in finite-dimensional case), so we can replace $T$ with $T^{*}$ and put another $^{\perp}$ on both parts, and get one line from another.
So let’s prove $\forall w \in W: (T^{*}w = 0)\iff (\forall w' \in \im T: \ev{w, w'} = 0)$. The second part is equivalent to $\forall v \in V: \ev{w, Tv} = 0$ and therefore to $\forall v \in V: \ev{T^{*}w, v} = 0$. And $V^{\perp} = \{ 0 \}$, so it’s equivalent to $T^{*}w = 0$.
