# bar K = H ←→ KT = {0}
from [[orthogonal projector]]

## statement
$$\bar K = H \Longleftrightarrow K^{\perp} = \{ 0 \}$$

## proof
$\implies$: assume $\exists w \in H: w \ne 0, w \in K^{\perp}$, then it is also in $H^{\perp}$, but $H \cap H^{\perp} = \varnothing$.
$\impliedby$: from $K^{\perp}= \{ 0 \}$ we have $\mathrm{Ker}\ P_{\bar K} = \{ 0 \}$. assume $\exists w \in (H \setminus \bar K)$, then $w - P_{\bar K}(w) \ne 0$ (because $w \not \in \bar K$), but $P_{\bar K}(w - P_{\bar K}(w)) = 0$, so we have a nonzero point in the kernel.