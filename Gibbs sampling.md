# Gibbs sampling
from [[Markov Chain Monte Carlo (MCMC)]]

actually, it’s a special case of [[Metropolis-Hastings algorithm]] for the case of [[joint distribution]] $p(x,y)$ if we are able to sample from $p(x\mid y)$ and $p(y\mid x)$ for all $x, y$.
there are two similar version, in one we update coordinates one by one in some deterministic order, in other we choose which coordinate to update at each step randomly. after that we sample the value for that coordinate from [[conditional probability]] of it based on the values of other coordinates.