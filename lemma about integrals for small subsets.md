# lemma about integrals for small subsets
From [[uniformly integrable]]
$\physics$
## Statement
Consider a [[Lebesgue measurable function]] $f: E \to \R$. If $f$ is integrable over $E$, for each $\varepsilon > 0$ there is $\delta > 0$ such that if $A \subset E$ is a [[Lebesgue measurable set]] and $m(A) < \delta$ then $\int_{A} \abs{f} < \varepsilon$.
Conversely, if $m(E) < \infty$ and the above condition holds, $f$ is integrable over $E$.

## Proof
Enough to prove for $f_{+}$ and $f_{-}$ separately, so consider $f \geq 0$.

By definition we know that there is a bounded function $f_\varepsilon$ such that $\int_{E} f_{\varepsilon} < \frac{\varepsilon}{2}$ and $f_{\varepsilon} < M$ for some $M$. Then take $\delta = \frac{\varepsilon}{2M}$, now we have $<\frac{\varepsilon}{2}$ error from approximation and $\int_{A} f_{\varepsilon} \leq \int_{E} f_{\varepsilon} < M \delta = \frac{\varepsilon}{2}$.