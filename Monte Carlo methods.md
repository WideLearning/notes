# Monte Carlo methods
From [[reinforcement learning]]
$\physics$
Compared to [[dynamic programming methods]] it is another method to simplify n-step expectation. Here we use sample average to approximate it. So, to estimate value function, we would sample a lot of trajectories from that state, each till the end of the episode, and take average of their returns.

- [[first-visit Monte Carlo]], [[every-visit Monte Carlo]]
- [[on-policy methods]], [[off-policy methods]]
- [[TD and MC give different predictions]]
- [[REINFORCE]]