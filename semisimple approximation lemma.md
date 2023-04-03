# semisimple approximation lemma
From [[measure theory]]
$\physics$
## Statement
For a [[measurable function]] $f: E \to \mathbb{R}$ there are sequences $\{ l_{n} \}$ and $\{ r_{n} \}$ of [[semisimple function|semisimple functions]] that [[converges uniformly]] to $f$ on $E$ and $l_{n} \leq f \leq r_{n}$.

## Proof
Just as in [[simple approximation lemma]], for $\varepsilon = \frac{1}{n}$ split the image of $f$ into half-intervals less than $\varepsilon$, define $l$ to be the least value of interval on all its preimage and $r$ to be the largest value. All conditions are satisfied (in particular, $\abs{l_{n} - f}, \abs{r_{n} - f}, \abs{l_{n} - r_{n}} < \varepsilon$).
The difference is that $f$ here is not necessarily bounded, therefore we might have a countable number of half-intervals.