# vector space
From [[linear algebra]]

## Definition
$(V, F)$ is called an $F$-vector space iff:
- $V$ is an abellian group
- $F$ is a field
- There is scalar multiplication $F \times V \to V$ such that:
	- $\alpha(\beta v) = (\alpha \beta)v$ (compatibility of multiplications)
	- $1v = v$ (compatibility of multiplication identities)
	- $\alpha(v + u) = \alpha v + \alpha u$ (distributivity w.r.t. vector addition)
	- $(\alpha + \beta)v = \alpha v + \beta v$ (distributivity w.r.t. field addition)
$$\begin{cases}
\forall v, u \in V, \alpha, \beta \in F: \alpha v + \beta u \in V \\
\alpha(v + u) = \alpha v + \alpha u, 
(\alpha + \beta)v = \alpha b + \beta v
\end{cases}$$