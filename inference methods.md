# inference methods
From [[Bayesian inference]]

If we successfully have defined [[prior distribution]] and [[likelihood function]], we already can find unnormalized [[posterior distribution]] in a given point with [[Bayes' theorem]]. By unnormalized I mean that we don't know the probability of data, which would require some integrating:
$$P(X \mid D) =
\frac{P(X)P(D \mid X)}{P(D)} \sim
P(X)P(D \mid X)$$

But we want to get something useful from the posterior, for examplel, samples, or means of some variables, or other statistics.

There are three approaches:
- [[grid approximation]]
- [[Markov Chain Monte Carlo (MCMC)]]
- [[variational inference]]