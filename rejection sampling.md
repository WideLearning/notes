# rejection sampling
From [[Markov Chain Monte Carlo (MCMC)]]
$\require{physics}{}$
Actually, it's not even about markov chains, because here each successfully sampled point will follow the target distribution independently.

## Problem
Denote $f: S \to \mathbb{R}$  the pdf of the target distribution. $S$ here is the set from which our random variable is sampled ($\mathbb{R}^{n}$, for example). Also we need another distribution with pdf $g$ and a constant $M$, such that $\forall x \in S: f(x) \leq Mg(x)$. Now we want to sample from $g$, then filter out some of the samples, so that remaining will follow distribution $f$. \

## Geometric derivation
First, geometric interpretation:
![[rejection sampling.excalidraw|600x300]]
Note that if we take a point randomly from the blue area (including green), its $x$ coordinate will be distributed according to $g$. If we then filter out the points that are not in green area, the remaining will follow distribution $f$.
Suppose that the sampled point is $(x, y)$. Conditional on $x$, $y \sim U(0, Mg(x))$. And it is in green area if $y \leq f(x)$. So for a given $x$ we accept the sampled point with probability $\dfrac{f(x)}{Mg(x)}$. 

## Algebraic derivation
Let's start with this innocent equation:
$$\int_{A} g(x) \frac{f(x)}{Mg(x)} dx = \frac{1}{M} \int_{A} f(x)dx$$
We can interpret this as probability of getting a sample from some region $A$:
The left hand side means that to take some point $x$ we first should get it from $g$ and then accept it with probability $\frac{f(x)}{Mg(x)}$ (here we use $f(x) \leq Mg(x)$).
The right hand side means that we sample $x$ from the target distribution and accept it with a constant probability $\frac{1}{M}$.

Note that $\frac{1}{M}\int_{S} f(x)dx = \frac{1}{M}$. Then if we condition the previous equation on the event of accepting a sample (because we don't care about dismissed ones) we get:
$$\begin{split}
P(\exists x \in A \mid \exists x) 
&= \frac{P(\exists x \in A, \exists x)}{P(\exists x)}\\
&= \frac{P(\exists x \in A)}{P(\exists x)} \\
&= MP(\exists x \in A)\\
&= M\int_{A} g(x) \frac{f(x)}{Mg(x)} dx\\
&= \int_{A} f(x)dx
\end{split}$$
So, for any set $A$ the accepted samples that we got have the same probability of lying into $A$ as would have samples from the target distribution. Which probably means that their distributions are the same (need to define equivalence of distributions here...).

## Unnormalized case
Now for the case of unnormalized pdf, when $\int_{S} f(x) dx = C \ne 1$, nothing changes actually. We just take $M$ to be $C$ times bigger. And because we don't know $C$ beforehand usually, we can guess it, and then check $\max \frac{f(x)}{Mg(x)}$: if it's much lower than $1$, $M$ can be decreased (to speed up the sampling), if it is greater than $1$ $M$ must be decreased.

## Algorithm
```python
import torch
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import uniform, norm, beta, bernoulli
from copy import deepcopy
from tqdm import tqdm


class PGM:
    def __init__(self):
        self.samples = []
        self.logprob = 0

    def logp(self, distr, value):
        try:
            return distr.logpdf(value)
        except:
            return distr.logpmf(value)

    def sample(self, distr, value=None):
        if value is None:
            value = distr.rvs()
        self.logprob += self.logp(distr, value)
        return value

    def model(self, params):
        pass

    def guide(self):
        pass

    def sample_params(self):
        params = self.guide()
        guide_logprob = self.logprob
        self.model(params)
        model_logprob = self.logprob
        return params, model_logprob - guide_logprob

    def rejection_sampling(self, N, M=None):
        if M is None:
            values = [self.sample_params()[1] for _ in tqdm(range(100))]
            M = max(values) - 1
        print(f"M = {M}")
        max_alpha = 0
        for _ in tqdm(range(N)):
            params, logprob = self.sample_params()
            alpha = np.exp(logprob - M)
            max_alpha = max(alpha, max_alpha)
            assert alpha >= 0
            while alpha >= 1:
                self.samples.append(deepcopy(params))
                alpha -= 1
            if bernoulli(alpha).rvs():
                self.samples.append(deepcopy(params))
        print(f"max alpha = {max_alpha}")
    
    def save(self, filename):
        torch.save(self.samples, filename)
        print(f"Saved {len(self.samples)} samples")

    def load(self, filename):
        self.samples += torch.load(filename)
        print(f"Now have {len(self.samples)} samples")

    def inspect(self, expr):
        values = np.array([expr(s) for s in self.samples])
        print(f"mean = {values.mean():.4f}")
        print(f"std = {values.std() / np.sqrt(values.size):.4f}")
        a, b, c = (
            np.percentile(values, 5),
            np.percentile(values, 50),
            np.percentile(values, 95),
        )
        print(f"5%, 50%, 95%: {a:.4f}, {b:.4f}, {c:.4f}")
        sns.histplot(values)
        plt.show()
    
    def map(self):
        best = None
        prob = -np.inf
        for s in self.samples:
            self.logprob = 0
            self.model(s)
            if prob < self.logprob:
                best = deepcopy(s)
                prob = self.logprob
        return best



class DeepExample(PGM):
    def __init__(self):
        super().__init__()

    def model(self, p):
        self.logprob = 0
        self.sample(beta(1, 2), p["p_dr"])
        self.sample(beta(2, 1), p["p_rr"])
        p["p_r"] = p["p_dr"] / (1 + p["p_dr"] - p["p_rr"])
        self.sample(bernoulli(p["p_r"]), p["R_4"])
        self.sample(bernoulli(p["p_rr"] if p["R_4"] else p["p_dr"]), p["R_5"])
        self.sample(bernoulli(p["p_rr"] if p["R_5"] else p["p_dr"]), p["R_6"])
        self.sample(bernoulli(0.95 if p["R_4"] else 0.0001), True)  # N_4
        self.sample(bernoulli(0.95 if p["R_5"] else 0.0001), True)  # N_5

    def guide(self):
        self.logprob = 0
        return {
            "p_dr": self.sample(beta(1, 2)),
            "p_rr": self.sample(beta(2, 1)),
            "R_4": self.sample(bernoulli(0.999)),
            "R_5": self.sample(bernoulli(0.999)),
            "R_6": self.sample(bernoulli(0.8)),
        }

pgm = DeepExample()
pgm.load("buffer.p")
pgm.rejection_sampling(10000, M=1.15)
pgm.save("buffer.p")
pgm.inspect(lambda p: p["p_rr"])
```