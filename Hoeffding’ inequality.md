# Hoeffding’ inequality
From [[probability inequalities]], similar to [[central limit theorem]]
$\physics$
## Statement
If $X = \sum\limits_{i \in [n]} x_{i}$ and each $x_{i} \in [a, b]$ and are i.i.d., then:
$$\forall t: E(X - E(X) \geq \Delta) \leq \exp\left(\frac{n(b - a)^{2}}{8}t^{2} - t\Delta\right)$$
And in particular, taking $t_{0} = -\frac{-\Delta}{\frac{n(b-a)^{2}}{4}} = \frac{4\Delta}{n(b-a)^{2}}$:
$$E(X - E(X) \geq \Delta) \leq \exp\left(\frac{-2\Delta^{2}}{n(b-a)^{2}} \right)$$

## Proof
First, we use independece of $x_{i}$ as in [[Chernoff inequality]]. Then we estimate $E(\exp(x_{i}))$ for each of them with [[Hoeffding’s lemma]].

## Relation to normal distribution
Note that we would get the same bound for [[normal distribution]] with $\sigma = \frac{b - a}{2}\sqrt{n}$. And it is sharp in some sense, because if $x$ takes $a$ and $b$ with probability $0.5$, by [[central limit theorem]] we get exactly this case.