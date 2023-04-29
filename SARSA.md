# SARSA
From [[temporal-difference learning]]
$\physics$
## Algorithm
For each step of episode:
	Take action $A$
	Observe $R, S'$
	Choose $A'$ from $S'$ using $\pi_{Q}$
	$Q(S, A) \leftarrow Q(S, A) + \alpha \qty[R + \gamma Q(S', A') - Q(S, A)]$
	$S, A \leftarrow S', A'$

Where $\pi_{Q}$ can be $\varepsilon$-greedy w.r.t. $Q$ with $\varepsilon = \frac{1}{t}$.

## Backup diagram
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd} & \bullet \\ & \circ \\  & \bullet & \arrow[from=1-2, to=2-2]\arrow[""{name=1, anchor=center, inner sep=0}, from=2-2, to=3-2] \end{tikzcd}
\end{document}
```

## Properties
- On-policy
- Model free
- $1$-step sample updates
- Bootstrapping

## See also
- [[one-step TD prediction]] is the prediction part of this
- [[expected SARSA]] is a deterministic and possibly off-policy version of this