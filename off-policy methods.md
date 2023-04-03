# off-policy methods
From [[Monte Carlo methods]]
$\physics$
## Definition
A general case, including [[on-policy methods]], where the policy used to generate data (behavior policy, $b$) is not necessarily the same as the policy being evaluated or improved (target policy, $\pi$).
However, we still assume $\pi(a \mid s) > 0 \implies b(a \mid s) > 0$.

To account for different distributions it often uses [[importance sampling]] (in different variations) with the following ratio:
$$\rho_{t:T-1} = \frac{\prod_{k=t}^{T-1}\pi(A_{k}\mid S_{k})p(S_{k+1}\mid S_{k}, A_{k})}{\prod_{k=t}^{T-1}b(A_{k}\mid S_{k})p(S_{k+1}\mid S_{k}, A_{k})} = \frac{\prod_{k=t}^{T-1}\pi(A_{k}\mid S_{k})}{\prod_{k=t}^{T-1}b(A_{k}\mid S_{k})}$$
