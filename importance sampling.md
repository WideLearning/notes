# importance sampling
From [[off-policy methods]]
$\physics$
## Statement (discrete case)
Suppose we have array $a_{\mathbb{N}} \in \mathbb{R}$ and two discrete random variables $P, Q$ with [[PMF]] $p_{\mathbb{N}}, q_{\mathbb{N}}$ respectively, such that $p_{i} = 0 \implies q_{i}= 0$. By definition of [[expected value]]:
$$\mathbb{E}(a_{P}) = \sum\limits_{\mathbb{N}} a_{i}p_{i},\ \mathbb{E}(a_{Q}) = \sum\limits_{\mathbb{N}} a_{i}q_{i}$$
Introduce importance sampling ratio $\rho_{[n]}$ given by $\rho_{i} = \frac{p_{i}}{q_{i}}$, then:
$$\mathbb{E}(a_{P}) = \mathbb{E}((a \cdot \rho)_{Q})$$

## Proof
By associativity of product:
$$\mathbb{E}(a_{P}) = \sum\limits a_{i}p_{i} = \sum\limits a_{i}(\rho_{i} q_{i}) = \sum\limits (a_{i} \rho_{i}) q_{i} = \mathbb{E}((a \cdot \rho)_{Q})$$

## Properties
- Compared to [[weighted importance sampling]], this is unbiased, but might have infinite variance ($\mathrm{Var}((a\rho)_{Q}) = \sum\limits_{\N} a_{i}^{2}\rho_{i}^{2} q_{i} = \sum\limits_{\N} a_{i}^{2}\rho_{i} p_{i}$) even if the original variance ($\mathrm{Var}(a_{P}) = \sum\limits_{\N} a_{i}^{2} p_{i}$) was finite, because $E((a \rho)_{Q}^{2}) \approx E(a_{Q}^{2}) E(\rho_{Q}^{2})$ (assuming $a_{Q}$ and $\rho_{Q}$ are close to independent).
- There is [[per-decision importance sampling]], which uses structure of [[Markov decision process]] to reduce variance.
- There is also [[discounting-aware importance sampling]], which further reduces variance for [[Markov decision process]] with $\gamma \ne 1$.