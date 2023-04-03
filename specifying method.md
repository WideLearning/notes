# specifying method
From [[applications of Kolmogorov complexity]]
$\physics$
## Definition
Consider a countable infinite set of objects $S$ and some standard enumeration $n: S \to \mathbb{N}$. Any method to describe objects from $S$ can be represented as a partial [[computable function]] $f: \mathbb{N} \to \mathbb{N}$. If $n(x) = f(p)$ we say that program $p$ (viewed as natural number, or a sequence of bits) describes $x$ w.r.t. specifying method $f$.
We can also introduce notion of complexity of $x$ w.r.t. $f$:
$$C_{f}(x) = \min\{ l(p) \mid f(p) = n(x) \} \text{ or } \infty \text{ if there is no such } p$$

## Properties
- We say that $f$ minorizes $g$ iff $\forall x. C_{f}(x) \leq C_{g}(x) + c(f, g)$ 
- And $f$ is (additively) optimal iff it minorizes every other specifying method
- We can add another object into the definition: [[conditional specifying method]]