# reinforcement learning
From [[machine learning]]

Reinforcement learning studies how to learn from interaction with environment. Although the same can be said about supervised learning, there :
- In SL the loss function usually means how “far” is the output from the right one, and it is usually differentiable. In RL you only know how “good” the output is, because there might be no such thing as the right one, and it is often not differentiable.
- In SL the outputs are calculated for each data point separately, while in RL current actions might affect future results, often in non-trivial way. 

## Topics
- [[policy]], [[reward signal]], [[value function]]
- [[multiarmed bandit problem]]
- [[Markov decision process]]
- [[dynamic programming methods]]
- [[Monte Carlo methods]]
- [[temporal-difference learning]]
- [[model-based methods]]
- [[function approximation]]
- [[on-policy distribution]]
- [[policy gradient methods]]
- [[gymnasium]]

## TODO
- try [[double Q-learning]] with $Q_{1} \leftarrow \dots + Q_{1}(\arg\max Q_{2})$ instead of $Q_{1} \leftarrow \dots + Q_{2}(\arg\max Q_{1})$
- https://arxiv.org/pdf/1606.02647v2.pdf: Retrace($\lambda$)
- https://arxiv.org/abs/1506.02438: Generalized Advantage Estimation
- https://arxiv.org/abs/1707.06347: Proximal Policy Optimization

## Books
- Richard Sutton, Andrew Barto, _Reinforcement Learning: An Introduction (2nd edition)_