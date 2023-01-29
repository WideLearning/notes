# rank-nullity for power
From [[linear algebra]], extends [[rank-nullity theorem]]
$\physics$
## Statement
Suppose $T \in \L(V), \dim V = n$, then:
$$V = \ker T^{n} \oplus \im T^{n}$$

## Proof
From [[rank-nullity theorem]] we already know $n = \dim \ker T^{n} + \dim \im T^{n}$. Now let’s show that they don’t intersect:
Suppose $v \in (\ker T^{n}) \cap (\im T^{n})$, that is $T^{n}v = 0, \exists u: v = T^{n}u$. Then $0 = T^{n}v = T^{2n}u$ and by [[lemma about sequence of kernels]] $T^{n} u = 0$, so $v = 0$.