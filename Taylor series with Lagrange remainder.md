# Taylor series with Lagrange remainder
From [[Taylor series]]
$\physics$
## Statement
Let $f \in C^{n+1}([x_{0}, x])$, then:
$$\exists \theta \in (x_{0}, x): f(x) = \sum\limits_{k=0}^{n} \frac{f^{(k)}(x_{0})}{k!}(x - x_{0})^{k} + \frac{f^{(n+1)}(\theta)}{(n + 1)!}(x - x_{0})^{n+1}$$

## Proof
For $n = 0$ we get it from [[mean value theorem]]. Now let’s prove the step $n - 1 \to n$:
$$\begin{split}
f(x) &= f(x_{0}) + \int_{x_{0}}^{x} f'(t) dt\\
&= f(x_{0}) +  \int_{x_{0}}^{x} \qty(\sum\limits_{k=0}^{n-1} \frac{(f')^{(k)}(x_{0})}{k!}(t - x_{0})^{k} + \frac{(f')^{n}(\theta(t))}{n!}(t - x_{0})^{n})dt\\
&= f(x_{0}) +  \int_{x_{0}}^{x} \qty(\sum\limits_{k=0}^{n-1} \frac{f^{(k + 1)}(x_{0})}{k!}(t - x_{0})^{k} + \frac{f^{n + 1}(\theta(t))}{n!}(t - x_{0})^{n})dt\\
&= f(x_{0}) +  \sum\limits_{k=0}^{n-1} \qty(\int_{x_{0}}^{x} \frac{f^{(k + 1)}(x_{0})}{k!}(t - x_{0})^{k}) dt + \int_{x_{0}}^{x} \frac{f^{n + 1}(\theta(t))}{n!}(t - x_{0})^{n}dt\\
&= f(x_{0}) +  \sum\limits_{k=0}^{n-1} \frac{f^{(k + 1)}(x_{0})}{(k + 1)!}(x - x_{0})^{k + 1} + \int_{x_{0}}^{x} \frac{f^{n + 1}(\theta(t))}{n!}(t - x_{0})^{n}dt\\
\end{split}$$
Denote $L = \inf\limits_{a \in (x_{0}, x)} f^{n+1}(a), R = \sup\limits_{a \in (x_{0}, x)} f^{n+1}(a)$. Because $\frac{(t - x_{0})^{n}}{n!}$ is positive, we can bound:
$$\int_{x_{0}}^{x} \frac{L}{n!}(t - x_{0})^{n} \leq \int_{x_{0}}^{x} \frac{f^{n+1}(\theta(t))}{n!}(t - x_{0})^{n} \leq \int_{x_{0}}^{x} \frac{R}{n!}(t - x_{0})^{n}$$
So by intermediate value theorem we can take just a single $\theta$ and then we get the required formula.