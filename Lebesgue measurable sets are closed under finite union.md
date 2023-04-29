# Lebesgue measurable sets are closed under finite union
From [[Lebesgue measurable set]]
$\physics$
## Statement
Suppose $\forall i \in [n]: X_{i}$ is [[Lebesgue measurable set]]. Then $\bigcup X_{i}$ is also [[Lebesgue measurable set]].

## Proof
Because [[monotonicity of Lebesgue outer measure]], it’s enough to show for arbitrary $A \subset \mathbb{R}$:
$$m^{*}(A) \geq m^{*}\qty(A \cap \qty(\bigcup X_{i})) + m^{*}\qty(A \cap \overline{\qty(\bigcup X_{i})})$$
Denote $M_{11\dots111} = X_{1} \cap X_{2} \dots \cap X_{n}$, $M_{0\dots0} = (\mathbb{R} \setminus X_{1}) \cap (\mathbb{R} \setminus X_{2}) \dots \cap (\mathbb{R} \setminus X_{n})$, $M_{011\dots11} = (\mathbb{R} \setminus X_{1}) \cap X_{2} \dots \cap X_{n}$ and so on. In this terms we are proving:
$$m^{*}(A) \geq m^{*}\qty(A \cap \qty(\bigcup M_{\ne 0\dots0})) + m^{*}(A \cap M_{0\dots0})$$
By [[countable subadditivity of Lebesgue outer measure]]:
$$m^{*}\qty(A \cap \qty(\bigcup X_{\ne 0})) = m^{*}\qty(\bigcup ( A \cap M_{\ne 0\dots0})) \leq \sum\limits_{s \ne 0\dots0} m^{*}(A \cap X_{s})$$
And so even stronger version of original statement is:
$$m^{*}(A) \geq \sum\limits_{s \subset [n]} m^{*}(A \cap M_{s})$$
Which says that outer measure of set $A$ is not less than sum of outer measure of all $2^{n}$ parts in which $X_{[n]}$ split it. It can be proven by induction: outer measure of $A$ is not less than parts that we have after $X_{1}$ (because $X_{1}$ is measurable), then we split each of these parts with $X_{2}$ having inequality in the same direction, etc.