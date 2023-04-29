# double Q-learning
From [[temporal-difference learning]]
$\physics$
## Description
It is a version of [[Q-learning]] designed to mitigate [[maximization bias]]. Here we have two action-value estimates: $Q_{0}$ and $Q_{1}$. At each step we select next action based on one of them (not important which one?) and then for the update step we choose one of them to provide $\arg\max$ and the other to actually get the value function estimate of that action. Note that we update that estimate that gave us $\arg \max$, which means that bootstrapping happens between the estimators. Maybe the reason is that it keeps both of them synchronized.

## Algorithm
For each step of episode:
	Select $i \in \{ 0, 1 \}$ randomly
	Choose $A$ according to $\pi_{Q_{i}}$
	Observe $R, S'$
	$Q_{i}(S, A) \leftarrow Q_{i}(S, A) + \alpha[R + \gamma Q_{1 - i}(S', \arg\max_{a \in \mathcal{A}(S')} Q_{i}(S', a)) - Q_{i}(S, A)]$
	$S \leftarrow S'$

## Properties
- Same as [[Q-learning]], but without [[maximization bias]]