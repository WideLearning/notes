# policy evaluation
From [[dynamic programming methods]]
$\physics$
## Definition
Also called the prediction problem, it means computing state-value function $v_{\pi}$ (or action-vaue function $q_{\pi}$) for a known policy $\pi$. Can be done with Bellman equations:
$$v_{\pi}(s) = \mathbb{E}(G_{t} \mid S_{t} = s) = \sum\limits_{a}\pi(a \mid s)\sum\limits_{r, s'} p(s', r \mid s, a)\qty[r + \gamma v_{\pi}(s')]$$

## Algorithms
- Solving these linear equations exactly. $\order{n^{3}}$ time and $\order{n^{2}}$ memory in general case.
- Iterative policy evaluation. $\order{nk}$ time and $\order{n}$ memory, where $k$ might be $\order{n}$?
  $$v_{k+1}(s) = \mathbb{E}(G_{t} \mid S_{t} = s) = \sum\limits_{a}\pi(a \mid s)\sum\limits_{r, s'} p(s', r \mid s, a)\qty[r + \gamma v_{k}(s')]$$
  - Asynchronous DP. Same update, but visiting more important states more often. 