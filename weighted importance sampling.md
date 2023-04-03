# weighted importance sampling
From [[off-policy methods]]
$\physics$
## Statement
Using notation from [[importance sampling]]:
$$\lim_{n \to \infty} E\left(\frac{\sum\limits_{[n]} \rho_{Q_{i}}a_{Q_{i}}}{\sum\limits_{[n]} \rho_{Q_{i}}}\right)= E(a_{P})$$
Where $P \sim p, Q_{[n]} \sim q$.

## Properties
- For finite $n$ it is biased, e.g. $n = 1$ makes left side equal to $E(a_{Q})$.
- Its variance is bounded when $a$ is bounded, for any $\rho$, because the weight of each $a_{Q_{i}}$ is at most $1$ (that is, bounded) and [[variance of sum is sum of variance for independent variables]].