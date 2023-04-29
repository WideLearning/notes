# definition of adjunction through universal morphisms
From [[adjunction]]
$\physics$
## Definition
Adjunction is a pair $(G: \cat{D} \to \cat{C}, \eta)$ where $\forall X \in \ob(C). \eta_{X}: X \to G(L_{X})$ is a [[universal morphism]] from $X$ to $G$.

## Proof of equivalence
In one direction it follows from [[unit of adjunction is a universal morphism]].

Now, we want to build $(F, G, \eta)$ adjunction ([[definition of adjunction through unit]]) and we need to show:
1. What is $F$?
2. Why $\varphi(f) = Gf \circ \eta_{X}$ is a bijection?
3. Why $\eta$ is a natural transformation?
   
1. For $X \in \ob(\cat{C})$, define $FX = L_{X}$. For $f: X \to Y$, because $\eta_{X}$ is a [[universal morphism]] and there is $(\eta_{Y} \circ f): X \to GFY$, there must be a unique $h: FX \to FY$ such that $Gh \circ \eta_{X} = \eta_{Y} \circ f$. Define $Ff = h$. It is easy to check that $F$ can preserve $\id$ and composition, and because $h$ is unique, it must preserve them, so $F$ is a functor.
2. [[universal morphism is equivalent to natural isomorphism between hom-sets]] with $R = FX$ and $F = G$.
3. From definition of $F$ we have:
$$GFf \circ \eta_{X} = \eta_{Y} \circ f$$
So $\eta: \id_{\cat{C}} \to GF$ is a [[natural transformation]] by definition.