# Gram–Schmidt process
From [[orthogonal system]]
$\physics$
## Statement
Suppose $v_{[\N]}$ is a countable set of linearly independent vectors. Then we can build $e_{[\N]}$ that will be an [[orthonormal system]] and also $\forall n \in \N: \ev{v_{[n]}} = \ev{e_{[n]}}$.

## Proof
We will increase the good prefix iteratively. For the first vector we do nothing. Then, when adding a new vector, we can subtract its projections on all the previous (already normalized ones). It won’t change the span (we just subtracted a linear combination of some vectors from another which doesn’t affect their total span) but will make the new vector orthogonal to all previous. After that we normalize.
$$ e_{i} = \frac{v_{i} - \sum\limits_{j=1}^{i-1} \ev{v_{i}, e_{j}} e_{j}}{\norm{v_{i} - \sum\limits_{j=1}^{i-1} \ev{v_{i}, e_{j}} e_{j}}}$$