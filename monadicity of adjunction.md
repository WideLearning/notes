# monadicity of adjunction
From [[algebra over a monad]] and [[adjunction]]
$\physics$
## Statement
Suppose $(F: \cat{C} \to \cat{D}, U, \eta, \varepsilon)$ is an [[adjunction]] and $(T = U \circ F, \eta, \varepsilon)$ is the [[monad from adjunction]]. Then there is a unique $K: \cat{D} \to T\text{-}\cat{alg}$ such that:
$$U^{T} \circ K = U\quad K \circ F = F^{T}$$
$U^{T}$ and $F^{T}$ are defined in [[monadicity of algebra]].

Also, if $K$ is equivalence of categories, $F \dashv U$ is called monadic. And if $K$ is an isomorphism, $F \dashv U$ is called strictly monadic.