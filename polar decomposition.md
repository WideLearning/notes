# polar decomposition
From [[linear algebra]]
$\physics$
## Introduction
Consider a following analogy between $\mathbb{C}$ and $\L(V)$:
complex number — [[linear operator]]
complex conjugate — [[adjoint]]
real number — [[self-adjoint operator]]
nonnegative number — [[positive operator]]
absolute value — [[square root (of operator)]] of [[linear operator]] multiplied by [[adjoint]]
number from unit circle — [[isometry]]

Now recall polar decomposition for complex numbers:
$$z = \frac{z}{\abs{z}} \sqrt{\bar z z}$$

## Statement
Suppose $T \in \L(V)$. Then there exists [[isometry]] $S$ such that $T = S \sqrt{T^{*} T}$.

## Proof
Note $\norm{Tv} = \norm{\sqrt{T^{*} T} v}$:
$$\ev{Tv, Tv} = \ev{T^{*} T v, v} = \ev{\sqrt{T^{*} T}^{*} \sqrt{T^{*} T} v, v} = \ev{\sqrt{T^{*} T} v, \sqrt{T^{*} T} v}$$
Let’s introduce $S: \sqrt{T^{*} T} v \mapsto Tv$ and prove that it is actually an isometry on all $V$.

Why is it a map? Suppose $v_{1}, v_{2} \in V: \sqrt{T^{*} T} v_{1} = \sqrt{T^{*} T} v_{2}$, so $\norm{\sqrt{T^{*} T} (v_{1} - v_{2})} = 0$ and by the statement above $\norm{T(v_{1} - v_{2})} = 0$, so $Tv_{1} = Tv_{2}$.
Note that we already have $T= S\sqrt{T^{*} T}$ just by construction.

How to define it on $V$? Because $\norm{Sv} = \norm{v}$, we have $\dim \ker S = 0$ and by [[rank-nullity theorem]] $\dim \im \sqrt{T^{*} T} = \dim \im T$ and therefore $\dim (\im \sqrt{T^{*} T})^{\perp} = \dim (\im T)^{\perp}$. We just need to somehow define $S$ that [[orthogonal complement]] without breaking its properties. We can choose arbitrary [[orthonormal basis]] bases for $(\im \sqrt{T^{*} T})^{\perp}$ and $(\im T)^{\perp}$ and make $S$ to map $i$-th element of the first basis to the $i$-th element of the second.

Why is it an isometry? On the $\im \sqrt{T^{*} T}$ it was so by construction. On the other part it is mapping orthonormal bases to orthonormal bases, so being restricted there it is also isometry. And because direct sum of these parts is $V$, it is also isometric on $V$. 




