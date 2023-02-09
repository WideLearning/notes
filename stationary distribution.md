# stationary distribution
from [[Markov chain]]

consider a [[Markov chain]] with transition matrix $Q$, which is irreducible and aperiodic ($\exists n \forall i, j: (Q^{n})_{i,j} > 0$, note the order of quantors) and aperiodic. then there is unique distribution $s$ (represented as row-vector) such that $sQ = s$, that is, if at some point marginal distribution of $X_i$ is $s$, all following states have the same distribution. it exists because of [[perron-frobenius theorem]]. moreover, it converges there from random initial state with probability 1, because $s$ is the eigenvector (actually, $s^{T}$ is an eigenvector of $Q^{T}$) with the largest (by absolute value) eigenvalue.

also, if $s$ is the stationary distribution, then $\frac{1}{s_{i}}$ is the expected time to return to $i$-th state.