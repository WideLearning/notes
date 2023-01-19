# cauchy-schwarz inequality
From [[inner product]], [[inequalities in analysis]] and [[probability inequalities]]

### Statement
Suppose we have an [[inner product]] $f$ on any [[linear space]] we want (though, with scalars $\in \mathbb{C}$), then:
$$ \forall x, y : |f(x,y)|^{2} \leq f(x,x)f(y,y) $$
### Proof
We will introduce some $t \in \mathbb{R}$ and then optimize it to make the inequality as strong as possible:
$$ f(x-ty, x-ty) \geq 0 $$
Rewriting this “square” by properties of [[inner product]]:
$$ f(x, x) - \bar tf(x, y) - t \overline{f(x, y)} + t\bar tf(y, y) $$
$$ f(x, x) - 2\Re(\bar t f(x, y)) + |t|^{2}f(y,y) \geq 0$$
Now we have to minimize real-valued function of complex variable (or of two real variables, equivalently), which we can do by zeroing derivatives. In the real case we could simply take the peak of parabola. In both cases we get the same: 
$$ t = \frac{f(x,y)}{f(y,y)}$$
And the desired inequality:
$$ f(x, x) - 2\frac{|f(x, y)|^{2}}{f(y, y)} + \frac{|f(x, y)|^{2}}{f(y,y)} \geq 0 $$
$$ f(x, x)f(y, y) - |f(x,y)|^{2}\geq 0$$

### In [[probability theory]]
Consider $f(X, Y) = \mathrm{E}(XY)$. It satisfies all properties of [[inner product]] (if we consider two [[random variables]] the same when $P[X=Y]=1$), so:
$$ (\mathrm{E}(XY))^{2}\leq \mathrm{E}(X^2)\mathrm{E}(Y^2)$$