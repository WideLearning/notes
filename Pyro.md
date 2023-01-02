# Pyro

## Some random notes

### Trace
form `help(pyro.poutine.Trace)`:
```python
trace = pyro.poutine.trace(model).get_trace(0.0)
logp = trace.log_prob_sum()
params = [trace.nodes[name]["value"].unconstrained() for name in trace.param_nodes]
```
### MCMC
```python
import torch
import pyro
import pyro.distributions as dist
from pyro.infer import MCMC, NUTS, Predictive


def model():
    p_dr = pyro.sample("p_dr", dist.Beta(1, 2))
    p_rr = pyro.sample("p_rr", dist.Beta(2, 1))
    p_r = pyro.deterministic("p_r", p_dr / (1 + p_dr - p_rr))
    R_4 = pyro.sample("R_4", dist.Bernoulli(p_r))
    R_5 = pyro.sample("R_5", dist.Bernoulli(torch.where(R_4 > 0.5, p_rr, p_dr)))
    R_6 = pyro.sample("R_6", dist.Bernoulli(torch.where(R_5 > 0.5, p_rr, p_dr)))
    N_4 = pyro.sample(
        "N_4", dist.Bernoulli(torch.where(R_4 > 0.5, 0.95, 0.0001)),
        obs=torch.tensor(1.)
    )
    N_5 = pyro.sample(
        "N_5", dist.Bernoulli(torch.where(R_5 > 0.5, 0.95, 0.0001)),
        obs=torch.tensor(1.)
    )


t0 = time()
nuts_kernel = NUTS(model, jit_compile=True)
mcmc = MCMC(nuts_kernel, num_samples=20000, warmup_steps=5000)
mcmc.run()
mcmc_samples = mcmc.get_samples()

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

site = "p_r"
samples = Predictive(model, mcmc_samples, return_sites=(site,)).forward()[site]

print("info for", site)
print("mean", samples.mean())
print("std", samples.std())
print("median", samples.median())
print("5%", np.percentile(samples, 5))
print("95%", np.percentile(samples, 95))

plt.figure(figsize=(10, 10))
sns.histplot(samples, bins=16)
plt.show()
```