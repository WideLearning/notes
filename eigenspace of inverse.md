# eigenspace of inverse
From [[eigenspace]] and [[generalized eigenspace]]
$\physics$
## Ordinary version
$$E(\lambda, T) = E\left(\frac{1}{\lambda}, T^{-1}\right)$$

## Proof
$$v \in E(\lambda, T) \iff Tv = \lambda v \iff v = T^{-1}\lambda v \iff T^{-1}v = \frac{1}{\lambda} v \iff v \in E\left(\frac{1}{\lambda}, T^{-1}\right)$$

## Generalized version
$$G(\lambda, T) = G\left(\frac{1}{\lambda}, T^{-1}\right)$$

## Proof
Consider a [[canonical basis of generalized eigenspace]] $v_{[n]}$. For simplicity let it be bamboo: $Tv_{1} = \lambda v_{1}, T v_{i} = \lambda v_{i} + v_{i-1}$.
It’s easy to see that $T^{-1}v_{1} = \frac{1}{\lambda}v_{1}, T^{-1}v_{i} = \frac{1}{\lambda}(v_{i} - T^{-1}v_{i-1})$ works, simpy undoing effects of $T$ on $v$. It mean that after each appliation of $(T^{-1} - \frac{1}{\lambda})$ the highest index of $v$ decreases and eventually they all get zero. So $v$ is (though not canonical) basis of $G\left(\frac{1}{\lambda}, T^{-1}\right)$ too. At least part of it, but we always can swap $T$ and $T^{-1}$, so the generalized eigenspaces are equal.