# n-step Q(sigma)
From [[temporal-difference learning]]
$\physics$
## Definition
A unification of [[n-step SARSA]], [[n-step off-policy learning with importance sampling]] and [[n-step tree backup]]. Here we have $\sigma_{t}$ for each step $t$, where $\sigma_{t} = 1$ means importance sampling, $\sigma_{t} = 0$ means taking expectation, and $\sigma_{t} \in (0, 1)$ interpolates those linearly. Then $n$-step SARSA is $1, 1, \dots, 1$, $n$-step expected SARSA is $1, 1, \dots, 1, 0$ and $n$-step tree backup is $0, 0, \dots, 0$.

$$G_{t:h} = R_{t+1} + \gamma(\sigma_{t}\rho_{t+1} + (1 - \sigma_{t})\pi(A_{t+1}\mid S_{t+1}))(G_{t+1:h} - Q_{h-1}(S_{t+1}, A_{t+1})) + \gamma \bar V_{h-1}(S_{t+1})$$
Where $\bar V$ means expected approximate value:
$$\bar V_{t}(s) = \sum\limits_{a \in \mathcal{A}(s)}\pi(a \mid s)Q_{t}(s, a)$$