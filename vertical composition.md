# vertical composition
From [[natural transformation]]

## Definition
Suppose we have three functors $F, G, H: \cat{C} \to \cat{D}$ and two [[natural transformation|natural transformations]] $\alpha: F \to G, \beta: G \to H$. Then we can build $\gamma: F \to H$ such that the following diagram commutes:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd} FA && GA && HA \\ \\ FB && GB && HB \arrow["Ff", from=1-1, to=3-1] \arrow["Gf", from=1-3, to=3-3] \arrow["Hf", from=1-5, to=3-5] \arrow["{\alpha_{A}}", from=1-1, to=1-3] \arrow["{\beta_{A}}", from=1-3, to=1-5] \arrow["{\alpha_{B}}"', from=3-1, to=3-3] \arrow["{\beta_{B}}"', from=3-3, to=3-5] \end{tikzcd}
\end{document}
```
So, by construction, $\gamma$ is also natural.

## Properties
- [[category of functors]]