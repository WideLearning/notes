# prior distribution
From [[terms commonly used in Bayesian statistics]]

## Definition
It defines what we assume a priori about the [[latent variables]].

In other words, it's $P(X)$ from the [[Bayes' theorem]].

Actually, we can take some prior for the observable variables too, but it is useless. The reason is that after we have observed the exact value of a variable, the prior either assigns a non-zero probability (or density) to that point, and is not important anymore, or assigns zero, which is a contradiction.

## Choosing a prior
There are many approaches that try to make the process of selecting a prior as objective and easy as possible. One of them is [[algorithmic probability]]. Also you can use symmetry if possible, to have a uniform prior in some sense.