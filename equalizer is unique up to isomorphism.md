# equalizer is unique up to isomorphism
From [[equalizer]]
$\physics$
## Statement
If there are two equalizers $e_{1}, e_{2}$, then there is [[isomorphism]] $i: E_{1} \to E_{2}$ such that $e_{2} \circ i = e_{1}$.
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
{E_1} \\
&& A && B \\
{E_2}
\arrow["f", shift left=2, from=2-3, to=2-5]
\arrow["g"', shift right=2, from=2-3, to=2-5]
\arrow["{e_2}"', from=3-1, to=2-3]
\arrow["{e_1}", from=1-1, to=2-3]
\arrow["i", leftrightarrow, from=1-1, to=3-1]
\end{tikzcd}
\end{document}
```

## Proof
By definition of [[equalizer]], there are $p: E_{1} \to E_{2}$ and $q: E_{2} \to E_{1}$ such that:
$$\begin{cases}
e_{1} = e_{2} \circ p\\
e_{2} = e_{1}\circ q\\
\end{cases}$$
So $e_{1} = e_{1} \circ p \circ q = e_{1} \circ \mathrm{id}_{E_1}$ . Because $e_{1}$ is monomorphism, $p \circ q = \mathrm{id}_{E_1}$. Similarly $q \circ p = \mathrm{id}_{E_2}$. So there is an isomorphism between $E_{1}$ and $E_{2}$.