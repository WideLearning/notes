# one-step TD prediction
From [[temporal-difference learning]] and [[on-policy methods]]
$\physics$
## Algorithm
For each step of episode:
	$A \leftarrow$ action sampled from $\pi$
	Observe $R, S'$
	$V(S) \leftarrow V(S) + \alpha \qty[R + \gamma V(S') - V(s)]$
	$S \leftarrow S’$

## Properties
- On-policy
- Model free
- $1$-step sample updates
- Bootstrapping

## See also
- [[SARSA]] is a complete control algorithm built on it
- [[Q-learning]] and [[expected SARSA]] use it with some modifications