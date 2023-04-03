# outer measure of at most countable set is zero
From [[outer measure]]
$\physics$
## Statement
1. $m^{*}(\varnothing) = 0$
2. $m^{*}(\{ x_{1}, x_{2}, \dots, x_{n} \}) = 0$
3. $m^{*}(\{ x_{1}, x_{2}, \dots, x_{n}, \dots \}) = 0$

## Proof
Because [[monotonicity of outer measure]], it’s enough to prove it for countable sets. Take arbitrary $\varepsilon > 0$, replace $x_{k}$ with $(x_{k} - \frac{\varepsilon}{2^{k}}, x_{k} + \frac{\varepsilon}{2^{k}})$. The sum of outer measures is $\frac{\varepsilon}{2} + \frac{\varepsilon}{4} + \dots = \varepsilon$. By [[countable subadditivity of outer measure]], the outer measure of union is less or equal to $\varepsilon$. We can make it arbitrary small, so it must be zero.