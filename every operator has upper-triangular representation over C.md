# every operator has upper-triangular representation over C
From [[coordinate representation]]

## Statement
Suppose that $T \in \L(V), F = \C$.
Then there exists a basis in which $[T]$ has no zeros under the main diagonal.
In other words, there is a basis $v_{[n]}$ such that every prefix of it is invariant under $T$.

## Proofs
1. We can take one [[eigenvalue]] at a time and move to $\im (T - \lambda I)$ by induction.
2. We can take one [[eigenvector]] at a time and move to $V/\ev{v}$ by induction.
3. We can consider the process of Gaussian elimination.