# Sarsa
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

## Properties
- $\varepsilon$-greedy
- On-policy
- Model free
- $1$-step sample updates
- Bootstrapping