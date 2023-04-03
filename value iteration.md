# value iteration
From [[dynamic programming methods]], special case of [[policy iteration]]
$\physics$
## Definition
Alternate [[policy evaluation]] with [[policy improvement]], but truncate evaluation to one sweep.
Together it will be:
$$v_{k+1}(s) = \max_{a} \sum\limits p(s', r \mid s, a)[r + \gamma v_{k}(s')]$$
So, just like [[policy evaluation]], but with $\max\limits_{a}$ instead of $\mathbb{E}_{a \sim \pi}$.