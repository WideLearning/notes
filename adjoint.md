# adjoint
From [[linear algebra]]
$\physics$
## Definition
Suppose $T \in L(V, W)$, its adjoint map $T^{*} \in L(W, V)$ is defined by:
$$\forall v \in V, w \in W: \ev{Tv, w} = \ev{v, T^{*}w}$$

## Proof
First want to show that such map indeed exists. For a fixed $w$ consider $\varphi(v) = \ev{Tv, w}$. By [[Riesz representation theorem]] there is $w' \in W: \varphi(v) = \ev{v, w'}$. Therefore $T^{*}w = w'$.
And also if we take $\varphi(v) = \ev{Tv, \alpha w_{1} + \beta w_{2}} = \alpha \ev{Tv, w_{1}} + \beta \ev{Tv, w_{2}}$ we see that $T^{*}(\alpha w_{1} + \beta w_{2}) = \alpha T^{*} w_{1} + \beta T^{*} w_{2}$, which is linearity.

## Properties
- $(A + B)^{*} = A^{*} + B^{*}$
- $(\lambda A)^{*} = \bar \lambda A^{*}$
- $(A^{*})^{*} = A$
- $(AB)^{*} = (BA)^{*}$
- [[kernel and image of adjoint]]
- [[matrix of adjoint in orthonormal basis is conjugate transposed]]
