# yoneda lemma
From [[category theory]]
$\physics$
## Statement
Consider $F: \cat{C}^{op} \to \cat{Set}$. There is a [[natural isomorphism]]:
$$\hom_{\cat{Set}^{\cat{C}^{op}}}(\hom_{\cat{C}}(-_{2}, -_{1}), F) \cong F-_{1}$$
Which means that for each $R \in \ob(\cat{C})$ there is a bijection:
$$\hom_{\cat{Set}^{\cat{C}^{op}}}(\hom_{\cat{C}}(-, R), F) \cong FR$$

Or in dual version, for $F: \cat{C} \to \cat{Set}$, also natural in $R \in \ob(\cat{C})$:
$$\hom_{\cat{Set}^{C}}(\hom_{\cat{C}}(R, -), F) \cong FR$$

## Proof
Define a function $T: \hom(\hom(-, R), F) \to FR$ as:
$$T(\alpha) = \alpha_{R}(\id_{R})$$
And another, $S: FR \to \hom(\hom(-, R), F)$. $S(x)_{B}: \hom(B, R) \to FB$ is defined as (remember that $F$ is contravariant):
$$(S(x)_{B})(f) = (Ff)(x)$$
The $S(x)$ from above is a [[natural transformation]]:
$$(S(x)_{B}) \circ \hom(f, R) = Ff \circ (S(x)_{A})$$
That is, for arbitrary $h: A \to R$:
$$S(x)_{B}(h \circ f) = (Ff)(S(x)_{A}(h))$$
$$(F(h \circ f))(x) = (Ff)((Fh)(x))$$
$$F(h \circ f) = Ff \circ Fh$$
Which is how composition is preserved under [[contravariant functor]].

Now, $T$ and $S$ are mutually inverse:
$$T(S(x)) = S(x)_{R}(\id_{R}) = F(\id_{R})x = x$$
$$S(T(\alpha))(f) = (Ff)(T(\alpha)) = (Ff)(\alpha_{R}(\id_{R})) = \alpha_{\dom(f)}(\id_{R} \circ f) = \alpha(f)$$
Where the last equality is from naturality of $A$, as in $S(x)_{B}(h \circ f) = (Ff)(S(x)_{A}(h))$ above.

Finally, it’s enough to check naturality of only one of $T$ or $S$, because their corresponding components are mutually inverse and it is easy to build the commuting square for one from another. Let’s check for $S$.
$$\forall f: B \to A. S_{B} \circ Ff = \hom(\hom(-, f), F) \circ S_{A}$$
First, how works the functor on the right?
1. The outer functor $\hom(-, F)$ works on morphisms (natural transformations) like this:
$$\begin{split}
&\alpha: H \to G \implies \hom(\alpha, F): \hom(G, F) \to \hom(H, F)\\
&\hom(\alpha, F)(\beta) = \beta \circ \alpha \\
\end{split}$$
2. For clarity, denote $TR = \hom(-, R)$:
$$\begin{split}
&f: A \to B \implies Tf: \hom(-, A) \to \hom(-, B)\\
&X \in \ob(\cat{C}) \implies (Tf)_{X}: \hom(X, A) \to \hom(X, B)\\
&\forall h: X \to A. (Tf)_{X}(h) = f \circ h\\
\end{split}$$
3. Together, $\hom(T-, F)$ works on morphisms like this:
$$\begin{split}
&f: B \to A \implies \hom(Tf, F): \hom(\hom(-, A), F) \to \hom(\hom(-, B), F)\\
&\alpha: \hom(-, A) \to F \implies \hom(Tf, F)(\alpha): \hom(-, B) \to F \\
&X \in \ob(\cat{C}) \implies (\hom(Tf, F)(\alpha))_{X} = (\hom(Tf, F)(\alpha))_{X}: \hom(X, B) \to FX\\
&\forall h: X \to B. (\hom(Tf, F)(\alpha))_{X}(h) = (\alpha \circ (Tf))_{X}(h) = \alpha_{X}((Tf)_{X}(h)) = \alpha_{X}(f \circ h)
\end{split}$$
Now let’s return to checking naturality. For arbitrary $t \in FA$:
$$S_{B}((Ff)t) = \hom(Tf, F)(S_{A}(t))$$
For $X \in \ob(\cat{C})$:
$$S_{B}((Ff)t)_{X} = (\hom(Tf, F)(S_{A}(t)))_{X}$$
(Just to check, type of both parts is now $\hom(X, B) \to FX$)
For $h: X \to B$:
$$S_{B}((Ff)t)_{X}(h) = (\hom(Tf, F)(S_{A}(t)))_{X}(h)$$
$$(Fh)((Ff)t) = (S_{A}(t)_{X})(f \circ h)$$
$$(Fh)((Ff)t) = (F(f \circ h))(t)$$
$$Fh \circ Ff = F (f \circ h)$$
Again because $F$ is [[contravariant functor]].


### Proof
Naturality of $\alpha$ gives us the following commuting square:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large] R && {\hom(R, R)} && FR \\ \\ X && {\hom(R, X)} && FX \arrow["Ff"{description}, from=1-5, to=3-5] \arrow["{\hom(R, f)}"{description}, from=1-3, to=3-3] \arrow["{\alpha_{R}}"{description}, from=1-3, to=1-5] \arrow["{\alpha_{X}}"{description}, from=3-3, to=3-5] \arrow["f"{description}, from=1-1, to=3-1] \end{tikzcd}
\end{document}
```
Following $\id_{R}$ through it we get:
$$\alpha_{X}(\hom(R, f)(\id_{R})) = (Ff)(\alpha_{R}(\id_{R}))$$
$$\alpha_{X}(f) = (Ff)(\alpha_{R}(\id_{R}))$$
So $\alpha_{X}$ is completely determined by $\alpha_{R}(\id_{R})$ (namely, $\alpha_{X} = \hom(\hom(R, R), F-)$). And the other direction is trivial, because from $\alpha$ we can get $\alpha_{R}(\id_{R})$ by substitution.

## Properties
- [[yoneda map is natural]]
- [[Haskell]] form (here instead of [[natural transformation]] we use polymorphic function, because [[parametric polymorphic functions are natural transformations]]): $$ (\forall x. (a \to x) \to F x )\cong F a $$
## See also
- [[yoneda embedding]]