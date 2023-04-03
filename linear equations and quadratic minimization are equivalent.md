# linear equations and quadratic minimization are equivalent
From [[conjugate methods]]
$\physics$
## Statement
Suppose $A$ is positive definite (and symmetric) $\R^{n \times n}$ matrix (aka [[positive operator]]). Then for any $b \in \R^{n}$:
$$\arg\min \ev{\frac{1}{2}Ax - b, x} = A^{-1}b$$
## Proof

Denote $\phi(x) = \ev{\frac{1}{2}Ax - b, x}$:
$$\begin{split}
\dd{\phi(x)}
&= \ev{\frac{1}{2}A\dd{x}, x}  + \ev{\frac{1}{2} Ax - b, \dd{x}}\\
&= \ev{\frac{1}{2}Ax, \dd{x}} + \ev{\frac{1}{2}Ax - b, \dd{x}}\\
&= \ev{Ax - b, \dd{x}}
\end{split}$$
In other words, $\nabla \phi(x) = Ax - b$. So, $Ax - b = 0$ is necessary for $x$ to be $\arg\min$. Let’s check that is is indeed a minimum:
$$\begin{split}
\phi(A^{-1}b +h) &= \frac{1}{2}\ev{Ah - b, A^{-1}b + h}\\
&= \frac{1}{2}\qty(\ev{Ah, h} - \ev{A^{-1}b, b})\\
&= \frac{1}{2}\ev{Ah, h} + \mathrm{const}
\end{split}$$
And because $A > 0$ there is a unique minimum in $h = 0$.
