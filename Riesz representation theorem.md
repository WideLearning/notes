# Riesz representation theorem
From [[linear algebra]]
$\physics$
## Statement
Suppose $\varphi \in \L(V, F), \dim V = n < \infty$, then:
$$\exists!u \in V: \varphi(v) = \ev{v, u}$$

## Proof
It’s necessary and sufficient to ensure that $\forall i \in [n]: \varphi(e_{i}) = \ev{e_{i}, u}$, which means $u = \sum\limits_{i=1}^{n} e_{i}\frac{\ev{u, e_{i}}}{\ev{e_{i}, e_{i}}} = \sum\limits_{i=1}^{n} e_{i}\frac{\varphi(e_{i})}{\ev{e_{i}, e_{i}}}$.
