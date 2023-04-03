# categorical product
From [[constructions and operations in category theory]]

## Definition
For $a_{1}, a_{2} \in \mathrm{Ob}(C)$ a product is tuple $\ev{b, \pi_{1}, \pi_{2}}$, where $b \in \mathrm{Ob}(C)$, $\pi_{1} \in \mathrm{Hom}(b, a_{1})$, $\pi_{2} \in \mathrm{Hom}(b, a_{2})$, with the following property:
$$\forall c \in \mathrm{Ob}(C), f_{1} \in \mathrm{Hom}(c, a_{1}), f_{2} \in \mathrm{Hom}(c, a_{2}). \exists! h \in \mathrm{Hom}(c, b). f_{1} = \pi_{1} \circ h, f_{2} = \pi_{2} \circ h$$
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd} && c \\ \\ {a_1} && b && {a_2} \arrow["{\pi_2}", from=3-3, to=3-5] \arrow["{\pi_1}"', from=3-3, to=3-1] \arrow["{f_1}", from=1-3, to=3-1] \arrow["{f_2}"', from=1-3, to=3-5] \arrow["h"{description}, from=1-3, to=3-3] \end{tikzcd}
\end{document}
```
## Properties
- The product is unique up to isomorphism (see [[limits are unique up to isomorphism]])
- [[projections of product are like monomorphism]]

## Intuition
In some sense, it’s the minimal representation that has all information about $a$ and $b$.
If it doesn’t have enough information, it will make it up when doing projections (for example, if we try int as a product of int and bool, taking projection to be identity and constant, that constant is exactly about making up something instead of missing information), so there is a morphism which does this “making up” and it is unique (in that example, the constant was, well, constant, so we can only use it in that morphism). but there is no morphism from the actual product to this small product, that will factorize the projections of the true product, because after the conversion to this small type we will lose some information. on the other hand, if our candidate for product has too much information, there is a simple and unique morphism that removes it, but we there are many morphisms in the inverse direction (because we again need to make up the extra information).

so the product is unique up to isomorphism.

it also has a graphical meaning: if we draw the points and arrows, candidates for product are the common ascendants of $a$ and $b$, and the actual product is the “closest” of them (lca, in other words).