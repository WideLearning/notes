# REINFORCE
From [[policy gradient methods]]
$\physics$
## Statement
$$\nabla J(\theta) \propto \mathbb{E}_{S_{t}, A_{t} \sim \pi}\left(G_{t} \nabla \log \pi(A_{t} \mid S_{t}, \theta)\right)$$
Where $G_{t}$ is the expected return after $S_{t}, A_{t}$ (see [[Markov decision process]]).

## Proof
According to [[policy gradient theorem]]:
$$\nabla J(\theta) \propto \sum\limits_{s} \mu(s)\sum\limits_{a} q_{\pi}(s, a) \nabla \pi(a \mid s, \theta)$$
But sum with weights taken from [[on-policy distribution]] is just expectation:
$$\nabla J(\theta) \propto \mathbb{E}_{S_{t} \sim \pi}\left(\sum\limits_{a} q_{\pi}(S_{t}, a) \nabla \pi(a \mid S_{t}, \theta)\right)$$
This is called “all-actions” method. We can simplify it even further (increasing variation, though) by importance sampling:
$$\nabla J(\theta) \propto \mathbb{E}_{S_{t}, A_{t} \sim \pi}\left(\frac{1}{\pi(A_{t} \mid S_{t}, \theta)}q_{\pi}(S_{t}, A_{t}) \nabla \pi(A_{t} \mid S_{t}, \theta)\right)$$
And as $\nabla \log f = \frac{\nabla f}{f}$ we can write it more concisely:
$$\nabla J(\theta) \propto \mathbb{E}_{s, a \sim \pi}\left(q_{\pi}(s, a) \nabla \log \pi(a \mid s, \theta)\right)$$
Finally, instead of expected return $q_{\pi}(s, a)$ we can use actual return $G_{t}$:
$$\nabla J(\theta) \propto \mathbb{E}_{S_{t}, A_{t} \sim \pi}\left(G_{t} \nabla \log \pi(A_{t} \mid S_{t}, \theta)\right)$$

## REINFORCE with baseline
$$\nabla J(\theta) \propto \mathbb{E}_{S_{t}, A_{t} \sim \pi}\left(G_{t} - b(S_t) \nabla \log \pi(A_{t} \mid S_{t}, \theta)\right)$$
Where $b(s)$ is arbitrary function on states. For example, we can use estimate of state value for this: $b(s) = \hat{v}(s)$.