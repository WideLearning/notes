# definition of adjunction through unit and counit
From [[adjunction]]
$\physics$
## Definition
An adjunction is a tuple $(F: \cat{C} \to \cat{D}, G: \cat{D} \to \cat{C}, \eta: \id_{\cat{C}} \to GF, \varepsilon: FG \to \id_{\cat{D}})$ such that $\varepsilon \circ F\eta = \id_{F}$ and $G \varepsilon \circ \eta = \id_{G}$ (that is, [[triangle identities for adjunction]] are satisfied).

## Proof of equivalence
In one direction, we just build [[unit of adjunction]], [[counit of adjunction]] and than we have [[triangle identities for adjunction]] for them.

In other, use [[definition of adjunction through unit]] and [[definition of adjunction through counit]]:
$$\forall f \in \hom(FA, B). \varphi_{A, B}(f) = Gf \circ \eta_A$$
$$\forall f \in \hom(A, GB). \varphi_{A, B}^{-1}(f) = \varepsilon_{B} \circ Ff$$
We already checked that each of $\varphi$ and $\varphi^{-1}$ is natural, but we still need to check that they are actually inverse of each other.
Here we use definitions above, [[counit of adjunction is a natural transformation]] and one of triangle identities:
$$\varphi^{-1}(\varphi(f)) = \varepsilon_{B} \circ FGf \circ F\eta_{A} = f \circ \varepsilon_{FA} \circ F \eta_{A} = f \circ \id = f$$
For other we need [[unit of adjunction is a natural transformation]] and another triangle identity:
$$\varphi(\varphi^{-1}(f)) = G \varepsilon_{B} \circ GF g \circ \eta_{A} = G \varepsilon_B \circ \eta_{GB} \circ g = \id \circ g = g$$
