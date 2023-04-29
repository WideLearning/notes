# n-step TD prediction
From [[temporal-difference learning]]
$\physics$
## Definition
Instead of one-step return as in [[one-step TD prediction]] these methods use $n$-step:
$$G_{t:t+n} = R_{t+1} + \gamma R_{t+2} + \dots + \gamma^{n-1}R_{t+n} + \gamma^{n}V_{t+n-1}(S_{t+n})$$
And we can update $V(S_{t})$ only at step $t+n$:
$$V_{t+n}(S_{t}) = V_{t+n-1}(S_{t}) + \alpha [G_{t:t+n} - V_{t+n-1}(S_{t})]$$

## Properties
- [[error reduction of n-step returns]]

## Examples
- [[n-step SARSA]]
- [[n-step off-policy learning with importance sampling]]