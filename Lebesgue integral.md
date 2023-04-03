# Lebesgue integral
From [[measure theory]]
$\physics$
## Definition
1. For a [[simple function]] $f: E \to \mathbb{R}$ where $m(E) < \infty$: 
   $$\int_{E} f = \sum\limits_{i=1}^{n} a_{i}m(E_{i})$$
2. For bounded measurable functions on finite domain. Lower and upper Lebesgue integrals are defined similarly to Riemann’s case, but step functions are replaced with simple:
   $$\underline{\int}_{E} f = \sup\left\{ \int_{E} \varphi \mid \varphi \leq f \text{ on $E$ and simple} \right\}$$
   $$\overline{\int}_{E} f = \inf\left\{ \int_{E} \varphi \mid \varphi \geq f \text{ on $E$ and simple} \right\}$$
   $f$ is Lebesgue integrable when these two are equal. Here $m(E) < \infty$ again.
   3. For non-negative measurable functions (with possibly infinite support and unbounded values):
  $$\int_{E} f = \sup \left\{ \int_{E_{0}} h \mid  0 \leq h \leq f, h \text{ is measurable, bounded}, m(E_{0}) < \infty \right\}$$
  

## Properties
- [[integration of simple functions is linear and monotone]]
- [[Riemann integrable functions are Lebesgue integrable]]
- [[bounded measurable functions on finite measure sets are integrable]]
- [[integration of bounded measurable functions on finite measure sets is linear and monotone]]
- [[integration of nonnegative measurable functions is linear and monotone]]
- [[Markov’s inequality]]
- [[integration is linear and monotone]]
- [[integration is additive over domain]]
- [[integral over set with measure zero is zero]]