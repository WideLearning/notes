# expected SARSA
From [[temporal-difference learning]]
$\physics$
## Algorithm
For each step of episode:
	Choose $A$ from $S$ using $\beta_{Q}$
	Take action $A$
	Observe $R, S'$
	$$\begin{split}
	Q(S, A) &\leftarrow Q(S, A) + \alpha \qty[R + \gamma \mathbb{E}_{\pi_{Q}(a \mid S)}\qty(Q(S', a)) - Q(S, A)]\\
	&=  Q(S, A) + \alpha \qty[R + \gamma \sum\limits_{a \in \mathcal{A(S')}}\pi_{Q}(a \mid S')Q(S', a) - Q(S, A)]
	\end{split}$$
	$S \leftarrow S'$

Where $\pi_{Q}$ is the target strategy and $\beta_{Q}$ is the behaviour strategy. First can be, for example, greedy ([[Q-learning]]) or same as $\beta_{Q}$ (deterministic version of [[SARSA]]). Second can be $\varepsilon$-greedy w.r.t. $Q$ with $\varepsilon = \frac{1}{t}$.

## Backup diagram
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd} & \bullet \\ & \circ \\ \bullet & \bullet & \bullet \arrow[from=1-2, to=2-2] \arrow[""{name=0, anchor=center, inner sep=0}, from=2-2, to=3-1] \arrow[""{name=1, anchor=center, inner sep=0}, from=2-2, to=3-2] \arrow[""{name=2, anchor=center, inner sep=0}, from=2-2, to=3-3] \end{tikzcd}
\end{document}
```

## Properties
- Generalizes [[Q-learning]] and reduces variance compared to [[SARSA]]
- Off-policy
- Model free
- $1$-step sample updates
- Bootstrapping