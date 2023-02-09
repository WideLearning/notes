# simple Bayesian inference with MCMC
from [[Markov Chain Monte Carlo (MCMC)]], see also [[pyro]]

```python
from scipy.stats import uniform, norm, lognorm
from math import exp
from copy import deepcopy
import seaborn as sns
import matplotlib.pyplot as plt

k = 3

prior = dict()
prior['sigma'] = lognorm(1)
for i in range(k):
    prior['theta', i] = norm()

a = [list(range(3, 8)), list(range(5, 10)), list(range(7, 12))]

def prior_logpdf(params):
    res = 0
    for k, v in params.items():
        res += prior[k].logpdf(v)
    return res

def likelihood_logpdf(params):
    res = 0
    for i in range(k):
        for e in a[i]:
            res += norm.logpdf(e, loc=params['theta', i], scale=params['sigma'])
    return res

def f_logpdf(params):
    return prior_logpdf(params) + likelihood_logpdf(params)

def sample_params():
    return { k : v.rvs() for k, v in prior.items() }

def mutate_params(params):
    return { k : norm.rvs(loc=v, scale=0.1) for k, v in params.items() }

params = sample_params()
samples = []

# metropolis-hastings sampling
for it in range(10000):
    samples.append(deepcopy(params))
    # candidate = sample_params()
    candidate = mutate_params(params)
    log_alpha = min(0, likelihood_logpdf(candidate) - likelihood_logpdf(params))
    alpha = exp(log_alpha)
    flag = uniform.rvs() < alpha
    # flag = True
    if flag:
        params = candidate

def thetas(s):
    return [s['theta', i] for i in range(k)]

def ampl(l):
    return max(l) - min(l)

# data = [ampl(thetas(s)) < 1 for s in samples]
data = [s['theta', 0] - s['theta', 1] for s in samples]
# print(sum(data) / len(data))

sns.kdeplot(data)
# plt.plot(data)
plt.show()
```