# merging prior and likelihood
From [[Bayesian inference]]

In [[bayesian update]] we saw that prior and posterior are very similar,
and one can become another, as we continue updating. Now let's note that [[prior distribution]] and [[likelihood function]] are also not very different, and it's usually convenient to merge them.

Let's build another toy example: 

There are 3 random variables, $A$, $B$ and $C$.
First, $A$ is sampled from $\mathcal{N}(0, 1)$ (standard normal distribution), then $B \sim \mathcal{N}(A, 1)$ and $C \sim \mathcal{N}(B, 1)$. We observed $C = 1.5$ and want to find posterior distribution of $A$.

What are our choices? 

First, we can put $A$ into prior and $B, C$ into likelihood:
$$p(A=x) = f(x),\quad p(B = y, C = z \mid A = x) = f(y - x)f(z - y)$$
where $f(x)$ denotes pdf of $\mathcal{N}(0, 1)$.

Or we can put $A, B$ into prior and $C$ into likelihood (e.g. because $C$ is observable):
$$p(A = x, B = y) = f(x)f(y - x),\quad p(C = z \mid A = x, B = y) = f(z - y)$$

Finally, we can merge it into a one function (which would be called prior, probably).
After all, when we use [[Bayes' theorem]] we multiply prior with likelihood, so why not do it from the start?
$$p(A = x, B = y, C = z) = f(x)f(y - x)f(z - y)$$
