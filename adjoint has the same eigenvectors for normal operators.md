# adjoint has the same eigenvectors for normal operators
From [[normal operator]]
$\physics$
## Statement
Suppose $T \in \L(V)$ is [[normal operator]].
$$Tv = \lambda v \implies T^{*}v = \bar\lambda v$$

## Proof
If $T$ is normal then $T - cI$ is also normal:
$$(T - c)(T^{*} - \bar c) = TT^{*} - cT^{*} - \bar c T - c^{2} = T^{*}T - cT^{*} - \bar c T - c^{2} = (T^{*} - \bar c)(T - c)$$
And let’s rewrite our target:
$$\forall v: ((T - \lambda I)v = 0) \iff ((T^{*} - \bar \lambda I)v = 0)$$
$$\forall v: \norm{(T - \lambda I)v} = 0 \iff \norm{(T^{*} - \bar \lambda I)v} = 0$$
Which is true [[normality test via norm]], because $T - \lambda I$ is normal.