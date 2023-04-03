# policy gradient methods
From [[reinforcement learning]]
$\physics$
These methods learn $\pi(a \mid s)$ directly, instead of building it on top of [[value function]]. And they use [[gradient descent]] (ascent in this case, actually) for it:
$$\theta_{t+1} = \theta_{t} + \alpha\widehat{\nabla J(\theta_{t})}$$
Where $\widehat{\nabla J(\theta_{t})}$ is a stochastic estimate of true gradient.

A common parametrization for policy is:
$$\pi(a \mid s, \theta) = \mathrm{softmax}_{a \in \mathcal{A}(s)}(h(s, a, \theta))$$

- [[policy gradient theorem]]
- [[REINFORCE]]

## Notation
- $\pi(a \mid s, \theta)$ — probability of action $a$ in state $s$ if the parameters of policy are $\theta$
- $\hat v(s, w)$ —  value function estimate of state $s$ if the value function parameters are $w$
- $J(\theta)$ — a scalar denoting the performance of policy parametrized by $\theta$
- 