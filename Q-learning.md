# Q-learning
From [[temporal-difference learning]] and [[off-policy methods]]
$\physics$
## Algorithm
For each step of episode:
	Choose $A$ from $S$ using $\pi_{Q}$
	Take action $A$
	Observe $R, S'$
	$Q(S, A) \leftarrow Q(S, A) + \alpha \qty[R + \gamma \max\limits_{a \in \mathcal{A}(S)} Q(S, a) - Q(S, A)]$
	$S \leftarrow S'$

Where $\pi_{Q}$ can be $\varepsilon$-greedy w.r.t. $Q$ with $\varepsilon = \frac{1}{t}$.

## Properties
- $\varepsilon$-greedy
- Off-policy (with greedy target policy)
- Model free
- $1$-step max updates
- Bootstrapping