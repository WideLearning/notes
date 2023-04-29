# boundedness of finite Lebesgue measurable functions
From [[Lebesgue measurable function]]
$\physics$
## Statement
Let $f: E \to \R$ be a [[Lebesgue measurable function]] such that $m(E) < \infty$ and for [[almost all]] $x \in E. \abs{f(x)} < \infty$.
Then for any $\varepsilon > 0$ $f$ is bounded on $E \setminus F$ with $m(F) < \varepsilon$.

## Proof
First, assume $f$ is finite everywhere on $E$, we can just add zero-measure set to $F$ later.
Take $r_{1}$ from [[semisimple approximation lemma]] for $f$. Select a finite number of values from its image such that their preimage is close enough to $E$. On that preimage $f$ is bounded (by maximum of selected values, for example), and with $F$ being the complement of the preimage, $m(F) < \varepsilon$.