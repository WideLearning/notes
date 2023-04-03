# Richardson extrapolation
From [[numerical methods]]
$\physics$
## Statement
Suppose we have $C = A_{i}(h) + a_{0}h^{k_{0}} + a_{1}h^{k_{1}} + \dots$. So $A_{i}$ is an $\order{h^{k_{0}}}$ approximation for the constant $C$ that we want to find. We know $k_{0}$ but don’t know $a_{0}$ and want to get a better approximation.
$$A_{i+1}(h) = \frac{t^{k_{0}}A_{i}\left(\frac{h}{t}\right) - A_{i}(h)}{t^{k_{0}} - 1}$$
Then:
$$C = A_{i+1}(h) + \order{h^{k_{1}}}$$

## Proof
$$C = A_{i}(h) + a_{0}h^{k_{0}} + \order{h^{k_{1}}}$$
$$C = A_{i}\left(\frac{h}{t}\right) + \frac{a_{0}h^{k_{0}}}{t^{k_{0}}} + \order{h^{k_{1}}}$$
$$(1 - t^{k_{0}})C = A_{i}(h) - t^{k_{0}}A_{i}\left(\frac{h}{t}\right) + \order{h^{k_{1}}}$$