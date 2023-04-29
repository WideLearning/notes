# Bezier-like curves for other distributions
From [[Bezier curve]]
$\physics$
```python
import numpy as np
import matplotlib.pyplot as plt

n = 3
a = np.array([2, 3, 0, 0.0])
# a = np.arange(n + 1) ** 2


def pcurve(x):
    N = 10**4
    # i = np.random.binomial(n, x, size=N)
    i = np.random.poisson(lam=n * x, size=N)
    i = np.clip(i, 0, n)
    return a[i].mean()


def bcurve(x):
    N = 10**4
    i = np.random.binomial(n, x, size=N)
    i = np.clip(i, 0, n)
    return a[i].mean()

def gcurve(x):
    N = 10**4
    assert 0 <= x <= 1
    eps = 1e-4
    i = np.random.geometric(p=1 / (n * x + 1), size=N) - 1
    i = np.clip(i, 0, n)
    return a[i].mean()

# x = np.linspace(0, 1, 1000)
# y = [pcurve(t) for t in x]
# plt.plot(x, y, lw=1, label="poisson")

# x = np.linspace(0, 1, 1000)
# y = [gcurve(t) for t in x]
# plt.plot(x, y, lw=1, label="geom")

x = np.linspace(0, 1, 1000)
y = [bcurve(t) for t in x]
plt.plot(x, y, lw=1, label="binomial")

plt.plot(np.linspace(0, 1, n + 1), a, "-o")
# plt.legend()
plt.show()

```