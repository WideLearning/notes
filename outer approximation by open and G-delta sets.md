# outer approximation by open and G-delta sets
From [[approximation of measurable sets]]
$\physics$
## Statement
Consider $E \subset \mathbb{R}$, the following three are equivalent:
- $E$ is a [[measurable set]].
- For any $\varepsilon > 0$ there exists an open $O \subset \mathbb{R}$ such that $E \subset O$ and $m^{*}(O \setminus E) < \varepsilon$.
- There exists [[G-delta set]] $G \subset R$ such that $E \subset G$ and $m^{*}(O \setminus G) = 0$.

## Proof
$1 \implies 2$:
By definition of [[outer measure]], there is $O = \bigcup\limits_{k=0}^{\infty} I_{k} \supset E$: $m^{*}(O) \leq \sum\limits_{k=0}^{\infty} l(I_{k}) < m^{*}(E) + \varepsilon$.

If $m(E) < \infty$, by [[excision property]] we get $m^{*}(O \setminus E) < \varepsilon$.
Otherwise, use [[set of infinite measure as countable disjoint union of sets with finite measure]], then apply finite measure case for each of those sets with exponentially decreasing margins ($m^{*}(O_{1} \setminus E_{1}) < \frac{\varepsilon}{2}, m^{*}(O_{2} \setminus E_{2}) < \frac{\varepsilon}{4}, \dots$) and the total margin will be less than $\varepsilon$.

$2 \implies 3$:
For all $k \in \N$ construct $O_{k}$ as in (2) with $\varepsilon = 1/k$. Then $G = \bigcap\limits_{k=1}^{\infty} O_{k}$ will contain $E$ by construction and have the same measure as [[monotonicity of outer measure]].

$3 \implies 1$:
$$E = G \cap \overline{G \setminus E}$$
Then, because [[Borel sets are measurable]], [[sets with zero outer measure are measureable]] and [[measurable sets are a sigma-algebra]], $E$ is also measurable.

