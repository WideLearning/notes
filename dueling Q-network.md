# dueling Q-network
From [[temporal-difference learning]]
$\physics$
## Description
For model-free algorithms based on value functions we have to learn action-value function $Q(S, A)$. But even in this case, actions from the same state usually have similar values. So we can decompose it as $Q(S, A) = D(S, A) + V(S)$, where $D(S, A)$ learns only action advantage and $V(S)$ learns only value function. 