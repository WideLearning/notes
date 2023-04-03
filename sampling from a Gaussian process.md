# sampling from a Gaussian process
From [[Bayesian inference]]
$\physics$
To do it on large scales, there is a lot of heavy math involved, but as a toy example we can do it much simpler. First, find a basis in which the covariation matrix of your process will be diagonal. Can use [[Gram–Schmidt process]] or just [[singular value decomposition]]. Anyway, we need to decompose $A = B^{T}DB$, where $D$ would be diagonal. After that, we already can calculate [[PDF]] for any data taking our process as prior. Adding some [[Markov Chain Monte Carlo (MCMC)]] (just [[rejection sampling]] in this case) on top we get a working sampler:

```python
import numpy as np
import scipy as sp
from itertools import product
import matplotlib.pyplot as plt


def multigauss_logpdf(mean, cov, x):
    UT, S, U = sp.linalg.svd(cov)
    assert np.allclose(cov, UT @ np.diag(S) @ U)
    assert np.allclose(U.T, UT)
    x = (U @ (x - mean)) / S
    return -0.5 * (x**2).sum()


def gp_logpdf(x, y):
    n = x.size
    assert x.shape == (n,) and y.shape == (n,)
    mean = np.zeros(n)
    vscale, hscale = 1.0, 0.1
    cov = np.exp(-0.5 * vscale * ((x.reshape(1, n) - x.reshape(n, 1)) / hscale) ** 2)
    return multigauss_logpdf(mean, cov, y)


nan = float("nan")
x = np.array([0.1, 0.6, 0.8, 1])
y = np.array([0.5, 0.1, 0.9, 1])

plt.plot(x[:-1], y[:-1], "x", ms=10, color="red")

px, py = [], []

for it in range(10000):
    x[-1] = np.random.uniform(low=0, high=1)
    y[-1] = np.random.randn()
    prior_logpdf = -0.5 * y[-1] ** 2
    p = gp_logpdf(x, y) - prior_logpdf
    alpha = np.exp(p)
    if np.random.uniform() < alpha:
        px.append(x[-1])
        py.append(y[-1])

print(f"generated {len(px)} points")
plt.plot(px, py, "o", ms=10, alpha=0.05, color="blue")
plt.show()

```

A more analytic version from Bing:

```python
import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt

# Define a kernel function for Gaussian Process
def kernel(x1, x2, sigma=0.1):
    d = np.sin(np.abs(x1 - x2)) / sigma
    return 1 / (1 + d**2)


# Define some given points and their values
x_given = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])
y_given = np.array([1.0, -1.0, 2.0, -2.0, 3.0])

# Define some points to sample from
x_sample = np.linspace(-3.0, 3.0, 300)

# Compute the covariance matrix for the given points
K_given = kernel(x_given[:, None], x_given[None, :])

# Compute the covariance matrix for the sample points
K_sample = kernel(x_sample[:, None], x_sample[None, :])

# Compute the cross-covariance matrix between the given and sample points
K_cross = kernel(x_given[:, None], x_sample[None, :])

# Compute the conditional mean and covariance for the sample points
mu_cond = K_cross.T @ np.linalg.inv(K_given) @ y_given  # mean vector
Sigma_cond = (
    K_sample - K_cross.T @ np.linalg.inv(K_given) @ K_cross
)  # covariance matrix

# Sample from the conditional multivariate normal distribution
y_samples = [multivariate_normal.rvs(mean=mu_cond, cov=Sigma_cond) for i in range(100)]

for i, y_sample in enumerate(y_samples):
    if i + 1 < len(y_samples):
        plt.plot(x_sample, y_sample, alpha=0.1, lw=1, color="blue")
    else:
        plt.plot(x_sample, y_sample, lw=2, color="red")

plt.plot(x_given, y_given, "o", ms=10, color="red")
plt.show()
```