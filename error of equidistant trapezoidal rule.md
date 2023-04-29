# error of equidistant trapezoidal rule
From [[trapezoidal rule]]
$\physics$
## Statement
Let $f \in C^{2}([a, b])$ and consider a partition given by $x_{i} = a + ih$. 
$$\abs{\int_{a}^{b} f(x)dx - T(f, x_{[0:n]})} = \frac{1}{12}\abs{(b - a)h^{2}f''(\xi)}, \xi \in (a, b)$$

## Proof via integration by parts
See [here](https://mathweb.ucsd.edu/~ebender/20B/77_Trap.pdf).

## Proof via thought experiment
Consider a function $g: [a, b] \to \mathbb{R}$ such that $g(a) = g(b) = 0$. We can add to it $\alpha(x - a)(b - x)$, for any $\alpha$, without changing these boundary conditions. If $2\alpha \geq -\inf g''(x)$, $g$ will become concave and its integral will be positive. If $2\alpha \leq -\sup g''(x)$ , $g$ will be convex and the integral will be negative. So there is $\alpha' \in [-\frac{\sup g''}{2}, -\frac{\inf g''}{2}]$ such that:
$$\int_{a}^{b} (g(x) - \alpha'(x - a)(b - x))dx = 0$$
$$\int_{a}^{b} g(x)dx = \int_{a}^{b} \alpha'(x - a)(b - x)dx$$
$$\int_{a}^{b} g(x)dx = \int_{0}^{b - a} \alpha' h(b - a - h)dh$$
$$\int_{a}^{b} g(x)dx = \alpha' \left(\frac{(b - a)^{3}}{2} - \frac{(b-a)^{3}}{3}\right) = \alpha' \frac{(b - a)^{3}}{6}$$
And  $\alpha' \in [-\frac{\sup g''}{2}, -\frac{\inf g''}{2}]$ means $\alpha' = -\frac{g''(\xi)}{2}, \xi \in (a, b)$:
$$\int_{a}^{b} g(x)dx = -g''(\xi) \frac{(b - a)^{3}}{12}$$
And $g$ has exactly the same form as $f(x) - T'(f, \dots)$ (because linear part was eliminated). Therefore:
$$\abs{\int_{a}^{b} f(x)dx - T(f, x_{[0:n]})} = \frac{h^{3}}{12}\sum\limits_{i \in [n]} f''(\xi_{i}) = \frac{(b - a)h^{2}}{12}\frac{\sum f''(\xi_{i})}{n}$$
And the mean of second derivatives is also a second derivative at some point, because we know $f \in C^{2}$ and so $f''$ has intermediate value property.