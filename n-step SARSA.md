# n-step SARSA
From [[temporal-difference learning]]
$\physics$
## Definition
Combination of [[SARSA]] with [[n-step TD prediction]]. The updates are now the following:
$$Q_{t+n}(S_{t}, A_{t}) = Q_{t+n-1}(S_{t}, A_{t}) + \alpha[G_{t:t+n} - Q_{t+n-1}(S_{t}, A_{t})]$$