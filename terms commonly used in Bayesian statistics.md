# terms commonly used in Bayesian statistics

From [[Bayesian inference]]

## Toy example

Suppose there is a bag with 3 balls, each is black or white. You pick one of them, it turns out to be black (let's denote this event $B$). Now, what can you say about the number $C$ of black balls that were in the bag?

In other words, find $p_{C \mid B}(x)$.

## Solution

Variable that we don't observe directly (and therefore have some uncertainty about) are called [[latent variables]] (or parameters). We are interesed in some of them, and others are needed only to describe our assumptions about underlying process.

Here the only latent variable is $C$, and it is also the variable that we will estimate.


In Bayesian philosophy we never start from scratch. If we want to find out something about the distribution of the latent variables, we must know something about it distribution beforehand. This distribution of latents, which we select before (ideally) we even got any data, is called a [[prior distribution]] or simply a prior.

Luckily, we don't need to know it exactly, even a crude approximation will be enough, if we have enough data to refine it. In some sense it is similar to Newton's method, where we also have to provide the initial approximation of the answer.

Choosing this approximation can be non-trivial in some cases, but here we can just assume that because we don't know anything about the number of black balls, all 4 options are equally probable:
$$p_{C}(x) = \begin{cases}
0.25 & x \in \{ 0, 1, 2, 3 \} \\
0 & \text{else}  \\
\end{cases}$$


Also, we need a model (aka [[likelihood function]]) which will say how probable is our data (that is, the observed values of non-latent variables) for a given set of values for latent variables. Usually the data is fixed and we consider the likelihood as a function of latent variables only.

In our case it's trivial:
$$P(B \mid C=c) = \frac{c}{3} $$

Then we can finally apply the [[Bayes' theorem]] and get a [[posterior distribution]]:
$$ p_{C \mid B}(c) = \frac{p_{C}(c)P(B \mid C = c)}{P(B)} = \frac{0.25 \times \frac{c}{3}}{0.5} = \frac{c}{6} $$
Now that we know the updated $p_{C}(c)$ we can calculate something useful about $c$.
For example, $\mathbb{E}(c) = \frac{7}{3}$ and mode is $c = 3$. 