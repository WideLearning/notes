# Ker P_{\bar K} = KT
from [[orthogonal projector]]

## statement
$$\mathrm{Ker}\ P_{\bar K} = K^{\perp}$$
## proof

first, because $K \subset \bar K$ we have:
$$ (\bar K)^{\perp} \subset K^{\perp} $$
also, we can write any point in $\bar K$ as series and get:
$$ K^{\perp} \subset \bar K ^{\perp} \implies (\bar K)^{\perp} = K^{\perp} $$
we already know $P_{K}(x) = 0 \Longleftrightarrow x \in K^{\perp}$, so $P_{\bar K}(x) = 0 \Longleftrightarrow x \in (\bar K)^{\perp}$ and with the previous result we have:
$$ P_{\bar K}(x) = 0 \Longleftrightarrow x \in K^{\perp} $$
