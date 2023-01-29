# singular values of self-adjoint operators
From [[singular value]] and [[self-adjoint operator]]
$\physics$
## Statement
Let $T \in \L(V)$ be a [[self-adjoint operator]], then its singular values are the absolute values of its [[eigenvalue|eigenvalues]].

## Proof
By definition singular value is eigenvalue of $\sqrt{T^{*}T}$. In our case it is also $\sqrt{T^{2}}$, and it has the same eigenvectors as $T$ (which has eigenvector basis by [[real spectral theorem]]). So now for each eigenvector separately we can check that the corresponding singular value will be $\sqrt{\lambda^{2}} = \abs{\lambda}$.