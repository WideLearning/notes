# de Casteljau algorithm
From [[Bezier curve]]
$\physics$
## Statement
A slower ($\order{n^{2}}$), but more numerically stable way to compute [[Bezier curve]] values:
$$b(x) = \beta^{n}_{0}$$
$$\beta^{i}_{j} = x\beta^{i-1}_{j+1} + (1 - x)\beta^{i-1}_{j},\quad \beta^{0}_{j} = a_{j}$$
## Proof
Consider it as a dynamic programming $\beta^{i}_{j} = \E[\mathrm{Bin}(i, x) + j]$. That is, we express [[binomial distribution]] as a sum of [[bernoulli distribution]] trials, and $i$ means how many are trials are left, while $j$ means how many successes were in the past trials.