# Gram–Schmidt orthogonalization
From [[orthogonal system]]
$\physics$
## Statement
Suppose $v_{[\N]}$ is a countable set of linearly independent vectors. Then we can build $e_{[\N]}$ that will be an [[orthogonal system]] and also $\forall n \in \N: \ev{v_{[n]}} = \ev{e_{[n]}}$.

## Proof
We will increase the good prefix iteratively. For the first vector we do nothing. Then, when adding a new vector, we can subtract its projections on all the previous (already normalized ones). It won’t change the span (we just subtracted a linear combination of some vectors from another which doesn’t affect their total span) but will make the new vector orthogonal to all previous. 
$$ e_{i} = v_{i} - \sum\limits_{j=1}^{i-1}\frac{\ev{v_{i}, e_{j}}}{\ev{e_{j}, e_{j}}}e_{j}$$