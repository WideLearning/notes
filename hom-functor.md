# hom-functor
From [[functor]]
$\physics$
## Definition
A covariant functor $\hom_{C}(A, -)$ maps $X$ to $\hom_{\cat{C}}(A, X)$ and $f: X \to Y$ to $\hom_{\cat{C}}(A, f)(g) = f \circ g$.
A contravariant functor $\hom_{C}(-, A)$ maps $X$ to $\hom_{\cat{C}}(X, A)$ and $f: Y \to X$ to $\hom_{\cat{C}}(f, A)(g) = g \circ f$.
Finally, a bifunctor $\hom_{\cat{C}}(-, -)$ maps $X, Y$ to $\hom_{\cat{C}}(X, Y)$ and $f: A \to X, g: Y \to B$ to $\hom_{\cat{C}}(f, g)(h) = g \circ h \circ f$.

## Properties
- [[covariant hom-functor preserves limits]]