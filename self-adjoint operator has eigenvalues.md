# self-adjoint operator has eigenvalues
From [[self-adjoint operator]] and [[eigenvalue]]
$\physics$
## Statement
If $F = \mathbb{R}$ and $T \in \L(V)$ is [[self-adjoint operator]], $\exists \lambda \in \R, v \in \R^{n}: Tv = \lambda v$.

## Proof
Note that we can’t just use [[eigenvalues exist in Cn]], because then we might end up with real eigenvalue but complex eigenvector.

But we also build such polynomial, then factorize it. We are left with a product of [[invertible quadratic expressions]], some non-zero constant and a possibly empty list of linear expressions. Product here means composition of operators, of course.

Because this composition equals zero for non-zero argument, it is not injective. The first two kinds of factors injective,  so at least one of linear terms must (exist and) be not injective. And it will give us eigenvalue. Not that it is not necessarily eigenvalue paired with the vector we put as argument, because the input vector goes through other maps before being passed to this linear term. 