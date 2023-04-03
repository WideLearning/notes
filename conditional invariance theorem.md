# conditional invariance theorem
From [[Kolmogorov’s complexity]]
$\physics$
## Statement
There is an additively optimal [[conditional specifying method]] among [[computable function|computable functions]].

## Proof
Similarly to [[invariance theorem]], consider $\phi_{0}$ that is computed by [[universal Turing machine]] $U$.
$$\phi_{0}(\ev{n, \ev{y, p}}) = \phi_{n}(\ev{y, p})$$
$$C_{\phi_{0}}(x \mid y) \leq C_{\phi_{n}}(x \mid y) + c_{\phi_{n}}$$
Here $c_{\phi_{n}} = l(\bar n) = 2l(n) + 1$. 
Note that $c_{\phi_{n}}$ doesn’t depend not only on $x$ but even on $y$.