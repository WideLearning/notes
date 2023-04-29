# convergence of iteration for linear systems
From [[iterative approach for linear systems]]
$\physics$
## Statement
Suppose $(I - P)$ is nondegenerate. The following iteration converges for any $x_0$ iff $\rho(P) < 1$:
$$x_{k+1} = Px_{k} + Qb$$
Here $\rho(P) = \max \abs{\lambda_{i}}$ means spectral radius of $P$ which is its maximum [[eigenvalue]].

## Proof
We will use the following:
$$(I - A)^{-1} - I = (I - (I - A))(I - A)^{-1} =  A(I - A)^{-1}$$

Consider the exact solution $x^{*} = (I - P)^{-1}Qb$ and the error term $e_{k} = x_{k} - x^{*}$.
$$\begin{split}
e_{k+1} &= x_{k+1} - (I - P)^{-1}Qb\\
&= Px_{k} + Qb - (I - P)^{-1}Qb\\
&= Px_{k} - ((I - P)^{-1} - I)Qb\\
&= Px_{k} - P(I - P)^{-1}Qb\\
&= Pe_{k}
\end{split}$$
And the following are equivalent:
- $\forall x. \lim\limits_{n \to \infty} P^{n}x = 0$
- $\max \abs{\lambda_{i}} < 1$

$\implies$: If there were $\abs{\lambda_{i}} \geq 1$, we could take its eigenvector as $x$ and the limit wouldn’t be zero.
$\impliedby$: Use [[Jordan form]] of $P$ and then show that each cell of $P^{n}$ approaches zero.