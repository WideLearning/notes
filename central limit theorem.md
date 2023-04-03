# central limit theorem
from [[probability inequalities]], similar to [[Hoeffding’ inequality]]

### statement
it’s a quantitive version of [[law of large numbers]]. consider $n$ i.i.d. [[random variables]] with finite mean and variance, then [[sample mean]] [[convergence in distribution|converges in distribution]] to standard [[normal distribution]]:
$$ \left(\frac{\sum\limits X_{i}-n\mu}{\sqrt{n}\sigma}\right) = \sqrt{n}\left(\frac{\bar X_{n} - \mu}{\sigma}\right) \overset{d}\to \mathcal{N}(0,1) $$
### proof
we also assume, that [[mgf]] of $X_i$ $M(t)$ exists, which is also for convenience. also, without loss of generality, $\mu = 0, \sigma = 1$. so $M(0) = 1, M'(0) = 0, M''(0) = 1$ and we want to show that [[mgf]] of $\frac{\sum X_{i}}{\sqrt{n}}$ converges to [[normal distribution]] [[mgf]], which is $\exp(\frac{t^{2}}{2})$. 
$$ \mathrm{E}\left(\exp\left(\frac{t\sum\limits X_{i}}{\sqrt{n}}\right)\right) = \left(M\left(\frac{t}{\sqrt{n}}\right)\right)^{n} $$
to take the limit we have to use [[l’hopital rule]] twice on logarithm of it:
$$ \lim\limits_{n\to \infty} n \log M\left(\frac{t}{\sqrt{n}}\right) $$
$$ \lim\limits_{y\to 0} \frac{\log M\left(yt \right)}{y^{2}}, y = \frac{1}{\sqrt{n}} $$
$$ \lim\limits_{y \to 0} \frac{t M'\left(yt \right)}{2yM(yt)} $$
$$ \frac{t}{2} \lim\limits_{y \to 0} \frac{M'\left(yt \right)}{y}, M(yt) \to 1 $$
$$ \frac{t^2}{2} \lim\limits_{y \to 0} M''\left(yt \right) $$
$$ \frac{t^{2}}{2} $$
And because [[mgf determines distribution]] (continuously?), [[CDF]] also will converge to [[CDF]] of $X$.

### corrollaries
because [[poisson distribution]], [[gamma distribution]] and [[binomial distribution]] are all sum of i.i.d. variables (which are [[poisson distribution]], [[exponential distribution]] and [[bernoulli distribution]] correspondingly, they converge to [[normal distribution]] for large $n$.