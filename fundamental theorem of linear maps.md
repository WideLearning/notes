# fundamental theorem of linear maps
From [[linear map]]
$\physics$
## Statement
$$\dim T = \dim \ker T + \dim \im T$$
## Proof
Let $u_{[m]}$ be a basis of $\ker T$. Extend it to a basis $u_{[m]}, v_{[n]}$ of $T$.
Now $\ev{Tv_{[n]}} =\im T$ because for any expression of a vector in the $u, v$ basis we can drop all $u$-components, as they all add $0$ to the image.

To show that $Tv_{[n]}$ is linear independent assume that there is a non-trivial zero linear combination, then the same combination for $v_{n}$ should be in $\ker T$. But $v$ is independent of $u$ and thus cannot express anything in $\ev{u_{[m]}} = \ker T$.

So $u$ is a basis of $\ker T$ and $Tv$ is a basis of $\im T$, while together they are a basis of $T$, which proves the formula.