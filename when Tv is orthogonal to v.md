# when Tv is orthogonal to v
From [[linear algebra]]
$\physics$
## Complex case
Suppose $F = \C, T \in \L(V)$, then:
$$ (\forall v \in V: \ev{Tv, v} = 0) \implies (T = 0)$$

## Proof
By [[extracting bilinear from quadratic]] we see that $q = 0 \implies h = 0$.
And $h = 0 \implies T = 0$, because we can consider the standard basis and then express every number in $[T]$ via $h$, getting a zero matrix.

## Real and self-adjoint case
Suppose $F = \R, T \in \L(V), T = T^{*}$, then:
$$(\forall v \in V: \ev{Tv, v} = 0) \implies (T = 0)$$

## Proof
Here we do something like [[extracting bilinear from quadratic]], but only the first part. We can’t determine the imaginary part this way because we can’t plug things like $v + iu$ in $q$ anymore, and we don’t need it because $h(v, u) = h(u, v)$ now.