# linear dependence lemma
From [[linear dependence]]

## Statement
Suppose $v_{[n]}$ is a linearly dependent set in $V$ while $v_{[m]}$ for some $m < n$ is linearly independent.
Then $\exists j \in [m + 1, n]$ such that:
- $v_{j} \in \ev{v_{[j-1]}}$
- $\ev{v_{[n] \setminus \{j\}}} = \ev{v_{[n]}}$

## Proof
By definition we have $a_{[n]} \in F^{n}: \sum\limits a_{i}v_{i} = 0$. Note that $a_{[m+1, n]} \ne 0$, because otherwise it will imply linear dependence of $v_{[m]}$.

So we can take $j = \max \{ i \in [m+1, n] \mid a_{j} \ne 0 \}$. Because it corresponds to the last non-zero element in $a$, we can express it as a linear combination of the previous vectors. Also it means that removing it doesn't change the span of $v_{[n]}$, because if a vector was expressed using non-zero coefficient for $v_{j}$ we can distribute it to the other coefficients with this linear combination.