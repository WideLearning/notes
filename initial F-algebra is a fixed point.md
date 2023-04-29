# initial F-algebra is a fixed point
From [[algebra over an endofunctor]]
$\physics$
## Statement
Definition of [[algebra over an endofunctor]] gives a category of $F$-algebras. Suppose $(X, \alpha)$ is the [[initial object]] there. Then $(X, \alpha) \cong (FX, F\alpha)$.

## Proof
As $(X, \alpha)$ is initial, there is a (unique) morphism $g: (X \alpha) \to (Fx, F\alpha)$. Also, there is a $(Fx, F\alpha) \to (X, \alpha)$ morphism given by $\alpha$:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large] FFX && FX \\ \\ FX && X \arrow["\alpha"', from=3-1, to=3-3] \arrow["F\alpha", from=1-1, to=1-3] \arrow["\alpha", from=1-3, to=3-3] \arrow["F\alpha"', from=1-1, to=3-1] \end{tikzcd}
\end{document}
```
1. $\alpha \circ g = \id_{(X, \alpha)}$
We know that there is only one morphism $(X, \alpha) \to (X, \alpha)$ because it is initial. We already showed that $\alpha$ is a morphism (that is, the diagram commutes) and $g$ is a morphism by construction, so their composition is too. Then it must be equal to $\id$.
2. $g \circ \alpha = \id_{(FX, F\alpha)}$
Consider the commutative diagram for $g$:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large] FX && X \\ \\ FFX && FX \arrow["\alpha", from=1-1, to=1-3] \arrow["F\alpha", from=3-1, to=3-3] \arrow["g", from=1-3, to=3-3] \arrow["Fg"', from=1-1, to=3-1] \end{tikzcd}
\end{document}
```
$$g \circ \alpha = F\alpha \circ Fg = F(\alpha \circ g) = F(\id) = \id$$
Therefore $\alpha^{-1} = g$ and it is an isomorphism between $(X, \alpha)$ and $(FX, F\alpha)$.