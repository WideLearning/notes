# Simpson’s rule
From [[numerical integration]]
$\physics$
## Definition
Instead of doing linear interpolation as in [[trapezoidal rule]] here we do quadratic:
$$\int_{a}^{b}f(x) dx = \frac{b - a}{6}\left[f(a) + 4f\left(\frac{a + b}{2}\right) + f(b)\right]$$
When using partition with size $h$ the error is $\order{h^{4}}$, see [[lemma about Gaussian quadrature error]].