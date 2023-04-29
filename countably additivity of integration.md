# countably additivity of integration
From [[Lebesgue integral]]
$\physics$
## Statement
Let $f: E \to \mathbb{R}$ be integrable and $E = \bigsqcup_{\mathbb{N}} E_{n}$, then:
$$\int_{E} f = \sum\limits_{\mathbb{N}} \int_{E_{n}} f$$

## Proof
We get finite additivity from [[additivity of integration]] by induction.
Then we rewrite sum as a limit:
$$f_{n} = f \cdot \chi_{\qty(\bigcup_{[n]} E_{n})}$$
$$\int_{E} f = \lim \int_{E} f_{n}$$
As $\abs{f}$ dominates $f_{\mathbb{N}}$, it holds by [[dominated convergence theorem]].