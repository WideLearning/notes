# reversibility of markov chain
from [[Markov chain]]

### intuitive definition
[[Markov chain]] is _reversible_, if going through it backwards doesn’t change it’s dynamics

### accurate definition
consider a [[Markov chain]] with matrix $Q$ and a [[stationary distribution]] $s$. to go backwards we want to take $Q^{T}$, but we have to renormalize it, so:
$$ Q'_{i,j} = Q_{j,i} \frac{s_j}{s_i} $$
(more complete version [here](https://www.math.ucdavis.edu/~gravner/MAT135B/materials/ch16.pdf))
so $Q$ is reversible iff
$$ \forall i,j: Q_{i,j} = Q_{j,i}\frac{s_{j}}{s_{i}} $$
and [[reversibility implies stationarity]], which is the reason to study this concept at all.

### properties
1. if $Q$ is symmetric (don’t confuse with undirected graph adjacency matrix because of row normalization), then $s = (\frac{1}{m}, \dots, \frac{1}{m})$ clearly satisfies reversibility test (and only it), so it’s stationary too. but the [[stationary distribution]] is unique, so it’s necessary [[uniform discrete distribution]]. 
more general fact: if every column of $Q$ sums to 1, then [[uniform distribution]] also is [[stationary distribution]], which can be just checked directly by multiplication.
1. if $Q$ is adjacency matrix of (possibly weighted) undirected graph, then [[stationary distribution]] is proportional to degrees of the vertices.
2. 
