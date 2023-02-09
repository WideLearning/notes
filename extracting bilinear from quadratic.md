# extracting bilinear from quadratic
From [[linear algebra]]
$\physics$
## Statement
Suppose $F = \C, T \in \L(V)$ and we have two forms defined via $T$:
- bilinear $h(v, u) = \ev{Tv, u}$ (such that $h(u, v) = \overline{h(v, u)}$)
- quadratic $q(v) = \ev{Tv, v}$
It’s easy to see $q(v) = h(v, v)$, but we also can express $h$ via $q$.

## Proof
We will take many squares and use this identitiy:
$$q(v + u) = \ev{T(v + u), v + u} = \ev{Tv + Tu, v + u} = q(v) + h(v, u) + h(u, v) + q(u)$$
First we get the real part:
$$q(v + u) - q(v - u) = 2(h(v, u) + h(u, v)) = 2(h(v, u) + \overline{h(v, u)}) = 2\Re(h(v, u))$$
Then with other arguments we get the imaginary part:
$$q(v + iu) - q(v - iu) = 2(h(v, iu) + h(iu, v)) = -2i(h(v, u) - \overline{h(v, u)}) = -2i\Im(h(v, u))$$
Putting it together:
$$h(v, u) = \frac{q(v + u) - q(v - u)}{2} + \frac{q(v + iu) - q(v - iu)}{2}i$$