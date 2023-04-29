# n-step tree backup
From [[temporal-difference learning]]
$\physics$
## Definition
In contrast to [[n-step off-policy learning with importance sampling]], here we use expected values (according to target policy) at all steps to directly get the needed estimate without importance sampling. It is possible due to bootstrapping nature of [[temporal-difference learning]].

$$G_{t:t+n} = R_{t+1} + \gamma\left(\pi(A_{t+1} \mid S_{t+1})G_{t+1:t+n} + \sum\limits_{a \ne A_{t+1}} \pi(a \mid S_{t+1})Q_{t+n-1}(S_{t+1}, a)\right)$$
$$G_{T-1:t+n} = R_{T}, \quad G_{t:t+1} = R_{t+1} + \gamma \sum\limits_{a} \pi(a \mid S_{t+1})Q_{t}(S_{t+1}, a)$$

## Backup diagram
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large]
{A_t} \\ {S_{t+1}} \\ {A_{t+1}} & {\mathcal{A}(S_{t+1})} \\ {S_{t+2}} \\ \bullet & {\mathcal{A}(S_{t+2})} \\ \circ \\ \bullet & \bullet
\arrow["{R_{t+1}}"', from=1-1, to=2-1] \arrow[from=2-1, to=3-1] \arrow[from=2-1, to=3-2] \arrow["{R_{t+2}}"', from=3-1, to=4-1] \arrow[from=4-1, to=5-2] \arrow[from=4-1, to=5-1] \arrow[from=5-1, to=6-1] \arrow[from=6-1, to=7-2] \arrow[from=6-1, to=7-1] \end{tikzcd}
\end{document}
```
