# Markov Chain Monte Carlo (MCMC)
From [[probability theory]] and [[inference methods]]

It is abot methods which are able to sample from complicated [[probability distributions]] by constructing an appropriate [[Markov chain]] (based on the desired [[PDF]] or [[PMF]], for example):
- [[rejection sampling]] as a simple example
- [[Metropolis-Hastings algorithm]] for univariate distribution (though can be used for joint one too)
- [[Gibbs sampling]] for [[joint distribution]].

Or more sophisticated samplers:
- No-U-turn sampler (e.g. in `Pyro`)
- Affine-invariant ensemble sampler (e.g. in `emcee`)
- Ensemble slice sampling (e.g. in `zeus`)

Code example: [[simple Bayesian inference with MCMC]]