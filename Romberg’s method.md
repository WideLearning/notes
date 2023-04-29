# Romberg’s method
From [[numerical integration]]
$\physics$
## Definition
Suppose we want to integrate $f \in C^{\infty}([a, b])$. Define $R^{0}_{k} = T(f, n=2^{k})$, where $T$ means [[trapezoidal rule]]. Then apply [[Richardson extrapolation]] to it (treating $R^{i}_{j}$ as $A_{2(i+1)}(2^{-k})$), but with a bit different formula:
$$A_{i+1}(h) = \frac{t^{k_{0}}A_{i}(h) - A_{i}(th)}{t^{k_{0}} - 1}$$
It can be written as a triangular array with the following recurrence:
$$R^{i}_{j} = \frac{1}{4^{i} - 1} (4^{i}R^{i - 1}_{j} - R^{i-1}_{j-1}) = R^{i-1}_{j} + \frac{1}{4^{i} - 1} (R^{i - 1}_{j} - R^{i-1}_{j-1})$$