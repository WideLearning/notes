# universal object
From [[universal property]]
$\physics$
## Definition
Consider a [[functor]] $H: D \to \mathrm{Set}$. A universal object of $H$ is a pair $\ev{r, e}$ where $r \in \mathrm{Ob}(D)$ and $e \in Hr$, with the following property:
$$\forall d \in \mathrm{Ob}(D), x \in Hd. \exists! f \in \mathrm{Hom}_{D}(r, d). (Hf)e = x$$

```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
D &&&& {\mathrm{Set}}\\
\\
r &&&& {e \in Hr}\\
\\
d &&&& {x \in Hd}\\
\arrow["f", from=3-1, to=5-1]
	\arrow["Hf", from=3-5, to=5-5]
\end{tikzcd}
\end{document}
```
## Examples
- [[quotient set as universal object]]