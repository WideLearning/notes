# policy improvement
From [[dynamic programming methods]], complementary to [[policy evaluation]]
$\physics$
## Definition
It the problem of determining better policy $\pi'$ according to state-value function $v_{\pi}$. Can be done by greedy update:
$$q_{\pi}(s, a) = \sum\limits_{s', r}p(s', r \mid s, a)[r + \gamma v_{\pi}(s')]$$
$$\pi'(s) = \arg\max q_{\pi}(s, a)$$
If $v_{\pi}$ was not optimal, $\pi' \ne \pi$ and $\pi'$ is at least as good in all states, and strictly better in some.

