# MCMC sampling
From [[inference methods]]

There are many methods that allow sampling from the distribution when we know only its unnormalized densities. MCMC means Markov Chain Monte Carlo, and these methods typically build a kind of markov chain, whose stationary distribution is the same as the distribution we want to sample from:
- [[rejection sampling]]
- [[Metropolis-Hastings algorithm]]