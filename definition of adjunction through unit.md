# definition of adjunction through unit
From [[adjunction]] and [[unit of adjunction]]
$\physics$
## Definition
Adjunction is a triple $(F, G, \eta)$, where $F: \cat{C} \to \cat{D}$, $G: \cat{D} \to \cat{C}$ and $\eta$ is a [[natural transformation]] such that $\varphi_{X, Y}(f) = Gf \circ \eta_{X} \in \hom(\hom(F-, -), \hom(-, G-))$ is a bijection for all $X, Y$.

## Proof of equivalence
1. If we have $(F, G, \varphi)$ adjunction, from [[definition of adjunction through commutative diagram]]:
$$\forall f \in \hom_{\cat{D}}(FX, Y). \varphi_{X, Y}(f) = \varphi_{X, Y}(f \circ \id_{FX}) = Gf \circ \varphi_{X, FX}(\id_{FX}) = Gf \circ \eta_{X}$$
So we can take its [[unit of adjunction]] as $\eta$ from the statement.
2. From the new definition we already know that $\varphi$ is a bijection, now let’s show that it is natural, namely, the conditions from [[definition of adjunction through commutative diagram]].
Here we use [[unit of adjunction is a natural transformation]]:
$$\begin{split}
\varphi(f \circ Fh) &= Gf \circ GFh \circ \eta_{X}\\
&= Gf \circ \eta_{Y} \circ h\\
&= \varphi(f) \circ h
\end{split}$$
And here just that $G$ is a [[functor]]:
$$\begin{split}
Gg \circ \varphi(f) &= Gg \circ Gf \circ \eta_{X}\\
&= G(g \circ f) \circ \eta_{X}\\
&= \varphi(g \circ f)\\
\end{split}$$
