# monad
From [[category theory]]
$\physics$
## Definition
A monad in $\cat{C}$ is a triple $(T: \cat{C} \to \cat{C}, \mu: T^{2} \to T, \eta: \id_{\cat{C}} \to T)$ with two commutative diagrams:
1. Associativity law:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large] {T^3} && {T^2} \\ \\ {T^2 } && T \arrow["T\mu", from=1-1, to=1-3] \arrow["{\mu T}"', from=1-1, to=3-1] \arrow["\mu"', from=3-1, to=3-3] \arrow["\mu", from=1-3, to=3-3] \end{tikzcd}
\end{document}
```
2. Unit laws:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large]
{T} && {T^2} \\
\\
{T^2 } && T
\arrow["T\eta", from=1-1, to=1-3]
\arrow["{\eta T}"', from=1-1, to=3-1]
\arrow["\mu"', from=3-1, to=3-3]
\arrow["\mu", from=1-3, to=3-3]
\arrow["\mathrm{id}", from=1-1, to=3-3]
\end{tikzcd}
\end{document}
```

## Properties
- [[monad as a monoid]]
- [[monad from adjunction]]
- [[simplified definition of monad]]
- [[monads from algebraic structures]]

## See also
- [[Kleisli category]]