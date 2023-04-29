# Egorov’s theorem
From [[measure theory]]
$\physics$
## Statement
Suppose $\{ f_{n} \}$ [[converges pointwise]] (a.e.) to $f: E \to \mathbb{R}$, $m(E) < \infty$ and $\varepsilon > 0$. Then there is a closed $F \subset E$ on which $\{ f_{n} \}$ [[converges uniformly]] to $f$ and $m(E \setminus F) < \varepsilon$.

## Proof
1. We can assume that $\{ f_{n} \}$ converges pointwise on whole $E$, otherwise just drop zero-measure set where it doesn’t: [[Lebesgue measurable almost everywhere functions are measurable]].
2. We can find measurable $F$ instead of closed, then proceed by [[inner approximation of Lebesgue measurable by closed and F-sigma sets]] .
3. Finally, we can reduce to the following lemma: for every $\eta, \delta > 0$ there is a measurable set $A \subset E$ and index $N$ such that $\forall n \geq N. \abs{f_{n} - f} < \eta$ and $m(E \setminus A) < \delta$. After that we can take decreasing $\eta$ (e.g. $1 / n$)  and exponentially decreasing $\delta$ with sum less than $\varepsilon$ (e.g. $\varepsilon \cdot 2^{-n}$),  find $A_{n}$ for each, and take their intersection. Because [[Lebesgue measurable sets are a sigma-algebra]] it will be measurable, and because margins were exponentially decreasing, its margin will be less than $\varepsilon$.
Now, let’s prove the lemma:
We know that $f$ is measurable because [[pointwise limit preserves measurability]]. 
So $E'_{n} = \{ x \in E \mid \abs{f - f_{k}}(x) < \eta \}$ is measurable.
Then $E_{n} = \bigcap_{k \geq n} E'_{k}$ is measurable.
Also, $E = \bigcup E_{n}$, because $\{ f_{n} \}$ converge to $f$ pointwise everywhere on $E$.
From [[continuity of measure]] we get $m(E) = \lim m(E_{n})$.
So we can choose $N$ such that $m(E_{n}) > m(E) - \varepsilon$ and take $A = E_{n}$. By [[excision property]] $m(E \setminus A) < \varepsilon$.