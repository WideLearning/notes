# Q-learning
From [[temporal-difference learning]] and [[off-policy methods]]
$\physics$
## Algorithm
For each step of episode:
	Choose $A$ from $S$ using $\pi_{Q}$
	Take action $A$
	Observe $R, S'$
	$Q(S, A) \leftarrow Q(S, A) + \alpha \qty[R + \gamma \max\limits_{a \in \mathcal{A}(S')} Q(S', a) - Q(S, A)]$
	$S \leftarrow S'$

Where $\pi_{Q}$ can be $\varepsilon$-greedy w.r.t. $Q$ with $\varepsilon = \frac{1}{t}$.

## Backup diagram
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd} & \bullet \\ & \circ \\ \bullet & \bullet & \bullet \arrow[from=1-2, to=2-2] \arrow[""{name=0, anchor=center, inner sep=0}, from=2-2, to=3-1] \arrow[""{name=1, anchor=center, inner sep=0}, from=2-2, to=3-2] \arrow[""{name=2, anchor=center, inner sep=0}, from=2-2, to=3-3] \arrow[shorten <=3pt, shorten >=3pt, Rightarrow, no head, from=1, to=2] \arrow[shorten <=3pt, shorten >=3pt, Rightarrow, no head, from=0, to=1] \end{tikzcd}
\end{document}
```

## Properties
- Off-policy (with greedy target policy)
- Model free
- $1$-step max updates
- Bootstrapping

## See also
- It is a special case of [[expected SARSA]] with target policy being greedy