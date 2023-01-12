# matrix of a linear map
From [[coordinate representation]]

## Definition
Consider $T \in \L(V, W)$ with corresponding bases $v_{[n]}$ and $w_{[m]}$, then:
$$[T]_{w}^{v} = \qty\big[[v_{1}]_{w}, \dots, [v_{n}]_{w}] \in F^{m \times n}$$
In other words, $k$-th column tells where the $k$-th vector of the first basis will be mapped, in terms of the second basis.

## Properties
- $[Ta]_{w} = [T]_{w}^{v} [a]_{v}$