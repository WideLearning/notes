# Metropolis-Hastings algorithm
From [[MCMC sampling]]

### Algorithm
We have an irreducible markov chain with matrix $Q = (p_{i,j})$ and the desired stationary distribution $s$. We might even not know the normalizing constant in $s$, it will cancel out anyway. We start with arbitrary $X_{0}$ and then at each step:
1. denote $X$ on current step as $i$, generate $j$ from $p_{i}$ distribution
2. accept it with probability  $$a_{i,j} = \min\left(\frac{s_{j}\ p_{j,i}}{s_{i}\ p_{i,j}}, 1\right)$$
3. if accepted, next $X = j$ else $X$ doesn’t change

### Intuition
If $p_{i,j}$ is symmetric, $a_{i,j} = \min(\frac{s_{i}}{s_{j}}, 1)$. Such choice ensures that probability of transition between $i$ and $j$ will be $\min(s_{i}, s_{j})$ in any direction. And them being equal is enough for reversibility of markov chain (i.e. the number of times we leave certain state is equal to the number of times we return to it on average).
And in the general case, we want to correct for $p$ assymetry too, now the probability of transition from $i$ to $j$ will be $s_{i}\ p_{i, j}\ a_{i, j} = \min(s_{j}\ p_{j,i}, s_{i}\ p_{i,j})$ (because we need to first get into state $i$, then try to go to $j$, then accept it). And this $\min$ is symmetric again.

### Proof
Because [reversibility implies stationarity](https://inst.eecs.berkeley.edu/~ee126/sp18/reversibility.pdf), we want to check 
$$ \forall i \ne j: s_{i} t_{i,j} = s_{j} t_{j,i} $$
where $t_{i, j}$ is the probability of transition and for $i \ne j$ we can replace it with $p_{i,j} a_{i,j}$:
$$ \forall i \ne j: s_{i}p_{i,j} \min\left(\frac{s_{j}\ p_{j,i}}{s_{i}\ p_{i,j}}, 1\right) = s_{j}p_{j,i} \min\left(\frac{s_{i}\ p_{i,j}}{s_{j}\ p_{j,i}}, 1\right) $$
$$ \forall i \ne j: \min\left(s_{j}\ p_{j,i}, s_{i}\ p_{i,j}\right) = \min\left(s_{i}\ p_{i,j}, s_{j}\ p_{j,i}\right) $$
which is a tautology.

### Connections
If we have a function $f(x)$ to optimize and define pdf  $p(x) = \exp(-\frac{f(x)}{t})$, with $t$ slowly reducing over time, we get simulated annealing algorithm.