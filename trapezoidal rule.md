# trapezoidal rule
From [[numerical integration]]
$\physics$
## Definition
We have a function $f: [a, b] \to \mathbb{R}$ that we want to integrate. For a partition $a = x_{0}, x_{1}, \dots, x_{n} = b$:
$$T(f, x_{[0:n]})\approx \sum\limits_{i \in [n]} (x_{i} - x_{i-1})\left(\frac{f(x_{i}) + f(x_{i - 1})}{2}\right)$$
When using partition with size $h$ the error is $\order{h^{2}}$.

## Properties
- [[error of equidistant trapezoidal rule]]