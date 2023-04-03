# gradient methods for bandit problem
From [[multiarmed bandit problem]], a simpler case of [[policy gradient methods]]
$\physics$
## Definition
Instead of explicitly estimating action values, here the agent estimates directly the policy: probabilities $\pi(a)$ for all actions $a$. They are usually defined as [[softmax]] of action preferences $H(a)$. And these preferences are learned by [[gradient descent]].

## Derivation
Suppose that we want to apply gradient descent, ideally it would be as follows:
$$\begin{split}
H_{t+1}(a)
&= H_{t}(a)+ \alpha \pdv{H(a)} \mathbb{E}(R)\\
&= H_{t}(a) + \alpha \pdv{H(a)} \sum\limits \pi_{t}(x)q(x)\\
&  \text{now rewrite softmax derivative}\\
&= H_{t}(a) + \alpha \sum\limits \pi_{t}(a)([a = x] - \pi_{t}(x)) q(x)\\
&= H_{t}(a) + \alpha \pi_{t}(a) \sum\limits ([a = x] - \pi_{t}(x)) q(x)\\
&= H_{t}(a) + \alpha \pi_{t}(a) \qty(q(a) - \sum\limits \pi_{t}(x) q(x))\\
&= H_{t}(a) + \alpha \pi_{t}(a) \qty\Big(q(a) - \mathbb{E}(R))\\
\end{split}$$

To get to stochastic update rule, we need another branch of derivation:
$$\begin{split}
H_{t+1}(a) - H_{t}(a)
&= \alpha \sum\limits \pdv{H(a)}\pi_{t}(x)q(x)\\
&\text{because $\sum\limits \pi(x) = \mathrm{const}$}\\
&= \alpha \sum\limits \pdv{H(a)}\pi_{t}(x)(q(x) - C)\\
&= \alpha \sum\limits \pi_{t}(x)([a = x] - \pi_{t}(a))(q(x) - C)\\
&= \alpha \mathbb{E}_{x \sim \pi_{t}} \qty\Big( \qty\big([a = x] - \pi_{t}(a))(q(x) - C) )\\
&= \alpha \mathbb{E}\qty\Big( \qty\big([a = A_{t}] - \pi_{t}(a))(q(A_{t}) - C) )\\
\end{split}$$
Now we can take $C = \bar R_{t}$ (average of all rewards so far) and also use $\mathbb{E}(R_{t}) = \mathbb{E}(q(A_{t}))$:
$$\begin{split}
H_{t+1}(a) - H_{t}(a)
&= \alpha \mathbb{E}\qty\Big( \qty\big([a = A_{t}] - \pi_{t}(a))(R_{t} - \bar R_{t}) )\\
\end{split}$$
Finally, we remove the expectation sign and get our stochastic update:
$$H_{t+1}(a) - H_{t}(a) = \alpha \qty\big([a = A_{t}] - \pi_{t}(a))(R_{t} - \bar R_{t})$$