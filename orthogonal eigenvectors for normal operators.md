# orthogonal eigenvectors for normal operators
From [[normal operator]]
$\physics$
## Statement
Suppose $T \in \L(V)$ is [[normal operator]], then:
$$Tu = \alpha u, Tv = \beta v, \alpha \ne b \implies v \perp u$$

## Proof
From [[adjoint has same eigenvectors for normal operators]] we know $T^{*}v = \bar \beta b$:
$$\begin{split}
(\alpha - \beta)\ev{u, v}
&= \ev{\alpha u, v} - \ev{\beta u, v}\\
&= \ev{\alpha u, v} - \langle u, \bar \beta v \rangle \\
&= \ev{T u, v} - \ev{u, T^{*} v}\\
&= 0
\end{split}$$