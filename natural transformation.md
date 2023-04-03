# natural transformation
From [[category theory]]

## Definition
It is a way to define morphism between [[functor|functors]]. More precisely, for functors $F, G: C \to D$ it must specify for each element $x \in C$ a morphism in $D$ (note, that it must be already there, we don’t connect arbitrary objects) $\eta_x$ and also for every morphism $f: x \to y$ in $C$ the following square must commute:
$$ \eta_{y}\circ F f = G f \circ \eta_{x}$$

```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large]
A && FA && GA\\
\\
B && FB && GB 
\arrow["f", from=1-1, to=3-1]
\arrow["Ff", from=1-3, to=3-3]
\arrow["Gf"', from=1-5, to=3-5]
\arrow["{\eta_{x}}"', from=1-3, to=1-5]
\arrow["{\eta_{y}}", from=3-3, to=3-5]
\end{tikzcd}
\end{document}
```

probably it is also a [[functor]] between categories that are the images of $F$ and $G$ (subcategories of $D$ in this case), but we still need to check naturality condition in this definition.

## Intuition
If [[functor]] is considered as a generalization of container, natural transformation is a way of repacking elements from one container into another. An example from [[Haskell]]:
``` haskell
safeHead :: [a] -> Maybe a
safeHead [] = Nothing
safeHead (x:xs) = Just x
```

Note that [[functor]] can be considered as a special case, for example, `a -> List a` can be identified with `(a -> a) -> (a -> List a)` (natural transformation from identity functor). 

## Properties
- I heard that this concept was one of the reasons to build category theory.
- Can be composed with [[vertical composition]] or [[horizontal composition]].
- [[natural isomorphism]]
- [[natural transformation for bifunctors]]
- [[parametric polymorphic functions are natural transformations]]