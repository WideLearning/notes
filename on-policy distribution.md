# on-policy distribution
From [[reinforcement learning]]
$\physics$
## Definition (episodic case)
Denote $h(s)$ the probability that an episode begins in $s$, $\eta(s)$ the expected number of visits to $s$ during episode and $\mu(s)$ the normalized version of $\eta(s)$. Then $\mu$ is called on-policy distribution and is expressed by the following equations:
1. Because each visit is either the first or follows a visit to another state:
$$\eta(s) = h(s) + \sum\limits_{s'} \eta(s')\sum\limits_{a \in \mathcal{A}(s')}\pi(a \mid s')p(s \mid s', a)$$
2. And normalization:
   $$\mu(s) = \frac{\eta(s)}{\sum\limits_{s'} \eta(s')}$$
   