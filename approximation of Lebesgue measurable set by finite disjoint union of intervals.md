# approximation of Lebesgue measurable set by finite disjoint union of intervals
From [[approximation of Lebesgue measurable sets]]
$\physics$
## Statement
Suppose $E$ is a [[Lebesgue measurable set]] with finite measure and $\varepsilon > 0$, then there is a finite disjoint union of open intervals $O = \bigcup\limits_{k=0}^{\infty} I_{k}$ such that $m^{*}(E \Delta O) < \varepsilon$. Here $\Delta$ means symmetric difference.

## Proof
By [[outer approximation of Lebesgue measurable by open and G-delta sets]] we can spend $\frac{\varepsilon}{2}$ of our margin to replace $E$ with an open set. Then, because [[open subset of reals is disjoint countable union of intervals]], we can find top $n$ largest intervals such that the length of the rest is smaller than $\frac{\varepsilon}{2}$ and it will be the answer. Note that we used first outer approximation and then inner, therefore we can’t replace symmetric difference in the statement with either outer or inner approximation.

## Simpler proof
By definition of [[Lebesgue outer measure]] we can spend $\frac{\varepsilon}{2}$ of our margin to replace $E$ with a countable union of intervals. Then we find top $n$ largest such that the length of the rest is smaller than $\frac{\varepsilon}{2}$ and it will be the answer. 