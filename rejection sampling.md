# rejection sampling
From [[MCMC sampling]]
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
Exercise to the next readers.