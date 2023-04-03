# policy gradient theorem
From [[policy gradient methods]]
$\physics$
## Statement (episodic case)
Define the performance of a policy as a value function of start state:
$$J(\theta) = v_{\pi_{\theta}}(s_{0})$$
Then we can express its gradient as follows:
$$\nabla J(\theta) \propto \sum\limits_{s}\mu(s)\sum\limits_{a \in \mathcal{A}(s)}q_{\pi_{\theta}}(s, a)\nabla\pi(a \mid s, \theta)$$
Where $\mu(s)$ is the on-policy distribution of $\pi_{\theta}$.

## Proof
First, let’s express the gradient (w.r.t. $\theta$) of $v$ in terms of $q$:
$$\begin{split}
\nabla v_{\pi}(s) &= \nabla\left[\sum\limits_{a} \pi(a \mid s)q_{\pi}(s, a)\right]\\
&= \sum\limits_{a} \qty\Big[\nabla\pi(a \mid s)q_{\pi}(s, a) + \pi(a \mid s)\nabla q_{\pi}(s, a)]\\
&= \sum\limits_{a} \qty\Big[\nabla\pi(a \mid s)q_{\pi}(s, a) + \pi(a \mid s)\nabla \sum\limits_{s', r} p(s', r \mid s, a)(r + v_{\pi}(s')) ]\\
&= \sum\limits_{a} \qty\Big[\nabla\pi(a \mid s)q_{\pi}(s, a)  + \pi(a \mid s)\nabla \sum\limits_{s', r} p(s', r \mid s, a)v_{\pi}(s')]\\
&= \sum\limits_{a} \qty\Big[\nabla\pi(a \mid s)q_{\pi}(s, a)  +  \pi(a \mid s)\nabla \sum\limits_{s'} p(s' \mid s, a)v_{\pi}(s')]\\
&= \sum\limits_{a} \qty\Big[\nabla\pi(a \mid s)q_{\pi}(s, a)  +  \pi(a \mid s) \sum\limits_{s'} p(s' \mid s, a)\nabla v_{\pi}(s')]\\
&= \sum\limits_{a} \qty\Big[\nabla\pi(a \mid s)q_{\pi}(s, a)]   +   \sum\limits_{s'} p(s' \mid s)\nabla v_{\pi}(s')\\
\end{split}$$
Which can be then unrolled into:
$$\begin{split}
\nabla v_{\pi}(s) &= \sum\limits_{k=0}^{\infty}\sum\limits_{s' \in \mathcal{S}} P(s \to x \text{ in $k$ moves})\sum\limits_{a \in \mathcal{A}(x)}\nabla \pi(a \mid s) q_{\pi}(s, a)\\
\end{split}$$
In other words, gradient of value function of $s$ is the weighted sum of gradients of action probabilities where weights are their expected action values (according to [[on-policy distribution]]).

Now we can express $\nabla J(\theta) = \nabla v_{\pi}(s_{0})$ (here $\eta$ is from [[on-policy distribution]]):
$$\begin{split}
\nabla J(\theta) &= \sum\limits_{x \in \mathcal{S}} \eta(x) \sum\limits_{a \in \mathcal{A}(x)} q_{\pi}(x, a) \nabla \pi(a \mid x)\\
&\propto \sum\limits_{x \in \mathcal{S}} \mu(x) \sum\limits_{a \in \mathcal{A}(x)} q_{\pi}(x, a) \nabla \pi(a \mid x)\\
\end{split}$$