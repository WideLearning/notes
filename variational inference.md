# variational inference
From [[inference methods]]

Here we find the closest approximation to the posterior distribution from some parametrized family of distributions. We find these parameters with the same methods as used in deep learning, like `SGD` or `Adam`. The only interesting thing is the loss function, which in theory should be KL-divergence, but in practice is replaced by Evidence Lower Bound (ELBO). 