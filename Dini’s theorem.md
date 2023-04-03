# Dini’s theorem
From [[measure theory]]
$\physics$
## Statement
If $\{ f_{n} \}$ is an increasing sequence of $C([a, b])$ functions that [[converges pointwise]] to $f \in C([a, b])$, then it [[converges uniformly]].

## Proof
For arbitrary $\varepsilon > 0$ we want to show that $\exists n. \forall k \geq n. \abs{f_{k} - f} < \varepsilon$, or equivalently $\exists n. \abs{f_{n} - f} < \varepsilon$ (because $\{ f_{n} \}$ are increasing).
Denote $E_{n} = \{ x \in [a, b] \mid (f - f_{n})(x) < \varepsilon \}$. Because $f_{n}(x) \to f(x)$ in every point, $\{ E_{n} \}$ is an open cover of $[a, b]$.  Also, note $E_{n} \subset E_{n+1}$. By [[Heine-Borel theorem]] $[a, b]$ is compact, so there is a finite subcover of $E_{n}$. It means that we can take the largest $n$ used in this subcover and such $f_{n}$ would work.