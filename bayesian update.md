# bayesian update
From [[Bayesian inference]]

In [[terms commonly used in Bayesian statistics]] we had an example where we clearly separated prior and posterior. But there is no fundamental difference between them, actually.

Suppose that in that same example we now pick two balls instead of one, with replacement (for simplicity). We can consider the colors of both balls as our data and update our prior distribution directly to the distribution after observing both balls.
But instead, we can now take the posterior that we got after taking one ball and updated it with the second ball. And we will get the same distribution as if we updated for both balls at the same time.

Let's check this analytically. Here $X$ denotes our variable of interest, $A$ and $B$ are two pieces of data that we observed:
$$\begin{split}
P(X\mid AB) &= \frac{P(AB \mid X)}{P(AB)}P(X)\\
&= \frac{P(B \mid AX)}{P(B\mid A)}\frac{P(A\mid X)}{P(A)}P(X)\\
&= \frac{P(B \mid AX)}{P(B\mid A)} P(X \mid A)
\end{split}$$
Here the first line means direct update and the last line means updating with $B$ what we got after updating with $A$.
