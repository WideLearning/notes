# inner approximation of set with finite Lebesgue measure by bounded set
From [[approximation of Lebesgue measurable sets]]
$\physics$
## Statement
For a [[Lebesgue measurable set]] $E \subset \mathbb{R}$ with $m(E) < \infty$ and $\varepsilon > 0$ there exists a bounded $F \subset E$ with $m(F) > m(E) - \varepsilon$.

## Proof
By definition of [[Lebesgue outer measure]] we can find an some cover $I \supset E$ such that $m(I) < \infty$. Then we take the union of some finite prefix of them $I'$ such that $I' \subset I, m(I') > m(I) - \varepsilon$ and $I'$ is bounded by construction.
Denote $\Delta = I \setminus I'$, we know $m(\Delta) < \varepsilon$. Let’s take $F = E \cap I’ = E \setminus \Delta$, by [[excision property]] $m(F) = m(E) - m(E \cap \Delta)$ where $m(E \cap \Delta) \leq m(\Delta) < \varepsilon$ so $m(F) > m(E) - \varepsilon$.