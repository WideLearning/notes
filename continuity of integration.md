# continuity of integration
From [[Lebesgue integral]]
$\physics$
## Statement
Consider an integrable $f: E \to \mathbb{R}$.
1. If $E_{\mathbb{N}}$ is an ascending collection of measurable subsets of $E$:
$$\int_{\bigcup_{\N}E_{n}} f = \lim \int_{E_{n}} f$$
2. If $E_{\mathbb{N}}$ is a descending collection of measurable subsets of $E$:
$$\int_{\bigcap_{\mathbb{N}} E_{n}} f = \lim \int_{E_{n}} f$$

## Proof
As in [[continuity of measure]]:
- [[countable union of Lebesgue measurable sets can be made disjoint]]
- replace limit with sum
- [[countable additivity of measure]]
- for the second statement, $E'_{n} = E \setminus E_{n}$ and [[linearity and monotonicity of integration]]