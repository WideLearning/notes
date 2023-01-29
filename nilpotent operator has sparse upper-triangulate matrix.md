# nilpotent operator has sparse upper-triangulate matrix
From [[nilpotent operator]], extends [[nilpotent operator has strictly upper-triangulate matrix]]
$\physics$
## Statement
Suppose $T \in \L(V)$ is a [[nilpotent operator]] and $\dim E(0, T) = k$. Then there is a basis w.r.t. which $[T]$ has the form:
![[generalized eigenspace.excalidraw]]

## Proof
Let’s build basis smarter than in [[nilpotent operator has strictly upper-triangulate matrix]]. Let $m$ be the maximum power of $T$ that is not null. Then take a vector $v$ from $\ker T^{m + 1} \text{/} \ker T^{m}$. That is, it is the vector that is not nullified by $T$ as long as possible. Add $v, Tv, \dots, T^{m}v$ to the basis. They are independent because they come from different “levels” of kernels. From the remaining part of $V$ select another $v$ (with maximal $m$, though maybe with smaller than first) and add it Jordan chain too. They are independent from the previously added ones because we explicitly work in [[quotient space]]. Continue to add such chains iteratively until whole $V$ is covered.
Now we have a basis with an interesting property: each vector is mapped by $T$ either to $0$ or to another vector from this basis. So by arranging these vectors according to the “levels” of kernels they came from we get the form that we wanted. 