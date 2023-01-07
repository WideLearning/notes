# matrix of a linear map
From [[coordinate representation]]

## Definition
Consider $T \in \L(V, W)$ with corresponding bases $v_{[n]}$ and $w_{[m]}$, then:
$$\mathcal{M}(T, v, w) = \qty\big[[v_{1}]_{w}, \dots, [v_{n}]_{w}] \in F^{m \times n}$$
In other words, $k$-th column tells where the $k$-th vector of the first basis will be mapped, in terms of the second basis.

The last two arguments are often dropped if they are obvious from the context.

## Properties
- $[Tv]_{w} = \mathcal{M}(T, v, w)[v]_{w}$