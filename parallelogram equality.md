# parallelogram equality
From [[inner product]]
$\physics$
## Statement
$$\norm{u + v}^{2} + \norm{u - v}^{2} = 2\qty(\norm{v}^{2} + \norm{u}^{2})$$

## Proof
$$\begin{split}
\norm{u + v}^{2} + \norm{u - v}^{2} 
&= \ev{u + v, u + v} + \ev{u - v, u - v} \\
&= \ev{u, u + v} + \ev{v, u + v} + \ev{u, u - v} - \ev{v, u - v}\\
&= \ev{u, (u + v) + (u - v)} + \ev{v, u + v - (u - v)}\\
&= \ev{u, 2u} + \ev{v, 2v}\\
&= 2\qty(\norm{v}^{2} + \norm{u}^{2})
\end{split}$$