# approximate Bayesian inference
From [[Bayesian inference]]
$\physics$
## Definition
As in [[Bayesian inference]] in general, we want to find $p(\theta \mid D) \propto p(D \mid \theta)p(\theta)$, but now we don’t have access to $p(D \mid \theta)$ and only can sample from there, $D_{\theta} \sim p(. \mid \theta)$.
Then we use the following estimate:
$$\begin{cases}
p\qty\big(\theta \mid D = d) = p\qty\big(\theta \mid S(D) = S(d))\\
p\qty\big(S(D) = S(d) \mid \theta) \approx p\qty\big(\rho(S(D), S(d)) \leq \varepsilon \mid \theta) = p\qty\big(\rho(S(D_{\theta}), S(d)) \leq \varepsilon)
\end{cases}$$
$$p(\theta = x\mid D = d) \approx \frac{p(x)}{n}\sum\limits_{s_{[n]} \sim D_{x}} \qty\Big[\rho\qty\big(S(s_{i}), S(d)) \leq \varepsilon]$$
Where $\varepsilon > 0$ is tolerance, $S(D)$ is a sufficient statistic of $D$ w.r.t. $\theta$ and $\rho$ is a distance metric.

Or a smoothed version (here smoothing acts as a statistic, but other $S(D)$ can be applied too):
Introduce $D' = D + \varepsilon, \varepsilon \sim \mathcal{N}(0, \sigma)$ with $\sigma \approx 0$.
$p(\theta \mid D = d) \approx p(\theta \mid D' = d)$
$$p(\theta = x\mid D = d) \approx \frac{p(x)}{n}\sum\limits_{s_{[n]} \sim D_{x}} p(s_{i} + \varepsilon = d) = \frac{p(x)}{n}\sum\limits_{s_{[n]} \sim D_{x}}  p_{\varepsilon}(d - s_{i})$$

## Example
Based on [this issue](https://github.com/pyro-ppl/pyro/issues/773), here is how we can handle deterministic irreversible operations. Consider the following model:
$z \sim \mathcal{N}(\mu, 1)$
$x = f(z)$
We want to sample $p_{z}(. \mid x = x_{0})$ and don’t know $f^{-1}(x_{0})$.
First, we can relax it to $p_{z}(. \mid \abs{x - x_{0}} < \varepsilon)$. Now posterior for $z$ probably doesn’t have zero measure, but it still doesn’t have useful gradients. Namely, $p(z) \propto [\abs{f(z) - x_{0}} < \varepsilon]$.
Or, we can use the smoothed version:
$z \sim \mathcal{N}(\mu, 1)$
$x = f(z)$
$y = \mathcal{N}(x, \varepsilon)$
And then $p(z \mid x = x_{0}) \approx p(z \mid y = x_{0})$.

## See also
[[straight-through approximator]].