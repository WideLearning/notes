# lemma about sequence of kernels
From [[linear algebra]]
$\physics$
## Statement
$$\{ 0 \} = \ker T^{0} \leqslant \ker T^{1} \leqslant \dots \leqslant T^{n} \dots$$
$$\ker T^{n-1} = \ker T^{n} \implies \ker T^{n} = \ker T^{n+1}$$
$$\ker T^{\dim V} = \ker T^{\dim V+1}$$

## Proof
For the first part just note that $T^{n} v = 0 \implies T^{n+1} v = 0$.

For the second it remains to show $\ker T^{n-1} = \ker T^{n} \implies \ker T^{n} \geqslant \ker T^{n+1}$:
$$T^{n+1}v = 0 \implies Tv \in \ker T^{n} \implies Tv \in \ker T^{n-1} \implies T^{n}v = 0$$

And the third part follows from the first two: for it to be false we need $n+1$ strict inequality in this sequence, but each inequality increases the dimension of kernel by at least one ([[dimension test]]), and it can’t grow bigger than $V$.