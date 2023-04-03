# Markov decision process
From [[reinforcement learning]]
$\physics$
## Definition
An agent is a part of the world that we have control over. An environment is the rest of the world, it interacts with the agent via observations and rewards. Agent responds with actions. And sequence of world states can be considered a [[Markov chain]].

## Notation
Everything happens in discrete time steps $t = 0, 1, 2, \dots$. At step $t$ the environment is a state $S_{t} \in \mathcal{S}$ and agent receives corresponding observation $f(S_{t})$ (which might not uniquely identify $S_{t}$). Then it selects action $A_{t} \in \mathcal{A}(S)$. The environment moves to the next state $S_{t+1}$ and produces reward $R_{t+1} \in \mathbb{R}$ and new observation.

So, the trajectory looks like this:
$S_{0}, A_{0}, R_{1}, S_{1}, A_{1}, R_{2}, S_{2}, \dots$

And “Markov” part means that distribution $p(s', r \mid s, a)$ of rewards and next states depends only on the current state and action.

Returns are defined as sum of rewards:
$$G_{t} = R_{t+1} + R_{t+2} + \dots + R_{T}$$
And when the planning horizon isn’t naturally limited, there are discounted returns:
$$G_{t} = R_{t+1} + \gamma R_{t+2} + \gamma^{2}R_{t+3} + \dots$$
$$G_{t} = R_{t+1} + \gamma G_{t+1}$$
Policy is a distribution of actions for each state:
$$\pi_{t}(a \mid s) = P(A_{t} = a \mid S_{t} = s)$$
For each policy we can define a corresponding state-value function:
$$v_{\pi}(s) = \mathbb{E}_{\pi}(G_{t} \mid S_{t} = s)$$
And action-value function:
$$q_{\pi}(s, a) = \mathbb{E}_{\pi}(G_{t} \mid S_{t} = s, A_{t} = a)$$
They are, of course, related:
$$v_{\pi}(s) = \mathbb{E}_{a \sim \pi(. \mid s)}(q_{\pi}(s, a))$$
$$q_{\pi}(s, a) = \mathbb{E}_{s', r \sim p(.,.\mid s, a)}(r + \gamma v_{\pi}(s'))$$
It can be shown that there is always at least one policy $\pi_{*}$ that for each state achieves expected returns not worse than with other policies. The corresponding optimal value functions are $v_{*}$ and $q_{*}$, and even if there are many optimal policies, optimal value functions are unique.

When we estimate these functions in the algorithms, estimates are denoted $V(s)$ and $Q(s, a)$ correspondingly.


