# self-adjont operators and invariant subspaces
From [[self-adjoint operator]] and [[invariant space]]
$\physics$
## Statement
Let $T \in \L(V)$ be [[self-adjoint operator]] and $U \leq V$ is invariant under $T$, then:
- $U^{\perp}$ is also invariant
- $T|_{U} \in \L(U)$ is also self-adjoint

Also, for (1) it’s enough to have a [[normal operator]].

## Proof
The main property of [[self-adjoint operator]] is its ability to swap arguments in [[inner product]], so let’s cast our problem in terms of inner products.
$$\forall u \in U: T u \in U$$
$$\forall u \in U, w \in U^{\perp}: \ev{T u, w} = 0$$
$$\forall w \in U^{\perp}, u \in U: \ev{Tw, u} = 0$$
$$\forall w \in U^{\perp}: Tw \in U^{\perp}$$
So $U^{\perp}$ is also invariant.

And the second statement is almost tautology:
$$\forall u, v \in U: \ev{T|_{U} u, v} = \ev{T u, v} = \ev{u, T v} = \ev{u, T|_{U} v}$$