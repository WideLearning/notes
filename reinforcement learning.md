# reinforcement learning
From [[machine learning]]

Reinforcement learning studies how to learn from interaction with environment. Although the same can be said about supervised learning, there :
- In SL the loss function usually means how “far” is the output from the right one, and it is usually differentiable. In RL you only know how “good” the output is, because there might be no such thing as the right one, and it is often not differentiable.
- In SL the outputs are calculated for each data point separately, while in RL current actions might affect future results, often in non-trivial way. 

## Topics
- [[policy]], [[reward signal]], [[value function]]
- [[multiarmed bandit problem]]
- [[gymnasium]]

## Books
- Richard Sutton, Andrew Barto, _Reinforcement Learning: An Introduction (2nd edition)_