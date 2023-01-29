# KTT = bar K
from [[orthogonal projector]]

## statement
$$(K^{\perp})^{\perp} = \bar K$$

## proof

first, if $\bar K = H$, we know $K^{\perp} = \{ 0 \}$ and then $(K^{\perp})^{\perp} = H$, so it’s a trivial case and we assume $\bar K \ne H$ further.

the statement is equivalent to $(\bar K^{\perp})^{\perp} = \bar K$, and let’s denote $S = \bar K$. we want to prove the following:
$$ \forall x \in H. (x \in (S^{\perp})^{\perp} \Longleftrightarrow x \in S)$$
$$ \forall x \in H. [\forall y \in S^{\perp}. (x \perp y)]  \Longleftrightarrow x \in S $$
$$ \forall x \in H. \Big([\forall y. (\forall z \in S. z \perp y) \to (x \perp y)] \Longleftrightarrow x \in S \Big)$$

$\impliedby:$
$$ \forall x \in H. [\forall y. (\forall z \in S. z \perp y) \to (x \perp y)] \leftarrow (x \in S)  $$
consider the inner part:
$$ (x \in S) \to [\forall y. (\forall z \in S. z \perp y) \to (x \perp y)]  $$
$$ \forall y.  (x \in S) \to [(\forall z \in S. z \perp y) \to (x \perp y)]  $$
$$ \forall y.  ((x \in S) \wedge (\forall z \in S. z \perp y)) \to (x \perp y)  $$
$$ \forall y.  (x \perp y) \to (x \perp y) $$

$\implies$:
$$ \forall x \in H.[\forall y. (\forall z \in S. z \perp y) \to (x \perp y)] \to (x \in S) $$
let’s form its contradiction:
$$ \exists x \in H.  [\forall y. (\forall z \in S. z \perp y) \to (x \perp y)] \wedge (x \not \in S) $$
$$ \exists x \in H. \forall y, z \in H. [(x \not \in S) \wedge \big(((z \in S) \to (z \perp y)) \to (x \perp y)\big)]] $$
simplifying implications in $((z \in S) \to (z \perp y)) \to (x \perp y)$:
$$ \exists x \in H. \forall y, z \in H. (x\not\in S)\wedge[((z \in S) \wedge (z \not\perp y)) \vee (x \perp y)] $$
$$ \exists x \not\in S. \forall y, z \in H. ((z \in S) \wedge (z \not\perp y)) \vee (x \perp y) $$
because $\exists z. z \not\in S$ and for them condition is strictly stronger, we can leave only them:
$$ \exists x \not\in S. \forall z \not\in S. \forall y \in H. x \perp y $$
$$ \exists x \not\in S. \forall y \in H. x \perp y $$
$$ \exists x \not\in S. x \in H^{T} $$
but $H^{T} = \{ 0 \}$, so $\exists x \not \in S. x = 0$, or $0 \not\in S$, which is a contradiction, because $S$ is a linear set.
